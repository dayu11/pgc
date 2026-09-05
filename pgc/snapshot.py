"""A pinned, read-only snapshot and the capped deterministic tools over it.

Every tool is a pure function of (call, snapshot). Results are sorted before the
cap is applied, so the same call always returns the same bytes. The oracle uses
the same implementation with the caps removed.
"""
from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Optional

CAPS = {"ls": 40, "grep": 20, "read": 60, "symbols": 40, "members": 40, "calls": 40}
TEXT_EXT = {".py", ".pyi", ".md", ".rst", ".txt", ".toml", ".cfg", ".ini", ".yaml", ".yml", ".json", ".in"}
SKIP_DIRS = {".git", "__pycache__", ".tox", ".venv", "node_modules", ".mypy_cache", ".pytest_cache"}
MAX_FILE_BYTES = 2_000_000
MAX_LINE_CHARS = 200


@dataclass(frozen=True)
class Call:
    tool: str
    args: tuple

    def key(self) -> str:
        return json.dumps([self.tool, list(self.args)])

    def __str__(self) -> str:
        if self.tool == "ls":
            return f"ls({self.args[0]!r})"
        if self.tool == "grep":
            return f"grep({self.args[0]!r}, {self.args[1]!r})"
        if self.tool == "read":
            return f"read({self.args[0]!r}, {self.args[1]}, {self.args[2]})"
        if self.tool in ("symbols", "members", "calls"):
            return f"{self.tool}({', '.join(repr(a) for a in self.args)})"
        return f"{self.tool}{self.args!r}"


@dataclass(frozen=True)
class Response:
    tool: str
    lines: tuple
    capped: bool
    error: Optional[str] = None

    def to_json(self):
        return {"tool": self.tool, "lines": list(self.lines), "capped": self.capped, "error": self.error}

    @staticmethod
    def from_json(d):
        return Response(d["tool"], tuple(d["lines"]), d["capped"], d.get("error"))


def _norm(rel: str) -> str:
    rel = rel.strip()
    if rel in ("", "."):
        return "."
    rel = rel.replace("\\", "/")
    while rel.startswith("./"):
        rel = rel[2:]
    return rel.rstrip("/") or "."


class Snapshot:
    """An immutable view of a directory tree. Only text files are visible."""

    def __init__(self, root: str | Path, name: Optional[str] = None):
        self.root = Path(root).resolve()
        self.name = name or self.root.name
        files = []
        dirs = set()
        for dp, dns, fns in os.walk(self.root):
            dns[:] = sorted(d for d in dns if d not in SKIP_DIRS)
            rel_dir = _norm(os.path.relpath(dp, self.root))
            dirs.add(rel_dir)
            for fn in fns:
                p = Path(dp) / fn
                if p.suffix not in TEXT_EXT:
                    continue
                try:
                    if p.stat().st_size > MAX_FILE_BYTES:
                        continue
                except OSError:
                    continue
                files.append(_norm(os.path.relpath(p, self.root)))
        self.files = tuple(sorted(files))
        self.fileset = frozenset(self.files)
        for f in self.files:
            d = f
            while "/" in d:
                d = d.rsplit("/", 1)[0]
                dirs.add(d)
        dirs.add(".")
        self.dirs = frozenset(dirs)
        self.py_files = tuple(f for f in self.files if f.endswith(".py"))

    # ----- raw access -----
    @lru_cache(maxsize=None)
    def text(self, rel: str) -> str:
        return (self.root / rel).read_text(encoding="utf-8", errors="replace")

    @lru_cache(maxsize=None)
    def lines(self, rel: str) -> tuple:
        return tuple(self.text(rel).split("\n"))

    def is_file(self, rel: str) -> bool:
        return _norm(rel) in self.fileset

    def is_dir(self, rel: str) -> bool:
        return _norm(rel) in self.dirs

    def children(self, rel: str) -> list:
        """Immediate entries of a directory: names, directories with a trailing slash."""
        rel = _norm(rel)
        prefix = "" if rel == "." else rel + "/"
        out = set()
        for f in self.files:
            if f.startswith(prefix):
                rest = f[len(prefix):]
                if "/" in rest:
                    out.add(rest.split("/", 1)[0] + "/")
                else:
                    out.add(rest)
        return sorted(out)

    def files_under(self, scope: str) -> list:
        scope = _norm(scope)
        if scope in self.fileset:
            return [scope]
        prefix = "" if scope == "." else scope + "/"
        return [f for f in self.files if f.startswith(prefix)]

    # ----- tools -----
    def call(self, call: Call, capped: bool = True) -> Response:
        cap = CAPS[call.tool] if capped else None
        try:
            if call.tool == "ls":
                return self._ls(call.args[0], cap)
            if call.tool == "grep":
                return self._grep(call.args[0], call.args[1], cap)
            if call.tool == "read":
                return self._read(call.args[0], int(call.args[1]), int(call.args[2]), cap)
            if call.tool == "symbols":
                return self._symbols(call.args[0], cap, call.args[1] if len(call.args) > 1 else None)
            if call.tool == "members":
                return self._members(call.args[0], call.args[1], cap)
            if call.tool == "calls":
                return self._calls(call.args[0], call.args[1], cap)
        except Exception as e:  # tools never raise; they return an error response
            return Response(call.tool, (), False, error=f"{type(e).__name__}: {e}")
        return Response(call.tool, (), False, error=f"unknown tool {call.tool}")

    def _ls(self, rel: str, cap) -> Response:
        rel = _norm(rel)
        if not self.is_dir(rel):
            return Response("ls", (), False, error=f"not a directory: {rel}")
        entries = self.children(rel)
        capped = cap is not None and len(entries) > cap
        return Response("ls", tuple(entries[:cap] if capped else entries), capped)

    def _grep(self, pattern: str, scope: str, cap) -> Response:
        scope = _norm(scope)
        if not (self.is_dir(scope) or self.is_file(scope)):
            return Response("grep", (), False, error=f"no such path: {scope}")
        try:
            rx = re.compile(pattern)
        except re.error as e:
            return Response("grep", (), False, error=f"bad regex: {e}")
        out = []
        for f in self.files_under(scope):
            for i, line in enumerate(self.lines(f), start=1):
                if rx.search(line):
                    out.append(f"{f}:{i}:{line[:MAX_LINE_CHARS]}")
                    if cap is not None and len(out) > cap:
                        break
            if cap is not None and len(out) > cap:
                break
        capped = cap is not None and len(out) > cap
        return Response("grep", tuple(out[:cap] if capped else out), capped)

    def _read(self, rel: str, start: int, count: int, cap) -> Response:
        rel = _norm(rel)
        if not self.is_file(rel):
            return Response("read", (), False, error=f"no such file: {rel}")
        lines = self.lines(rel)
        start = max(1, start)
        want = count if cap is None else min(count, cap)
        chunk = lines[start - 1 : start - 1 + want]
        out = tuple(f"{start + i}:{l[:MAX_LINE_CHARS]}" for i, l in enumerate(chunk))
        capped = cap is not None and count > cap and len(lines) >= start - 1 + count
        return Response("read", out, capped)

    def _symbols(self, rel: str, cap, filt: Optional[str] = None) -> Response:
        """Outline of module-level bindings. Line 1 is a header with the module's
        dynamic status and its `__all__` status; star imports are always listed;
        with a name filter only bindings of that name (or importing it) follow."""
        from . import analysis  # local import keeps module dependencies one-way
        rel = _norm(rel)
        if not self.is_file(rel) or not rel.endswith(".py"):
            return Response("symbols", (), False, error=f"not a python file: {rel}")
        mod = analysis.parse_module(rel, self.text(rel))
        if mod.parse_error:
            return Response("symbols", (), False, error="syntax error")
        if mod.all_names is None:
            all_status = "none"
        elif mod.all_names == analysis.DYNAMIC:
            all_status = "dynamic"
        else:
            all_line = min(b.line for b in mod.all_bindings if b.name == "__all__")
            all_status = f"static@{all_line}"
        header = f"module {rel} lines={mod.n_lines} dynamic={'yes' if mod.dynamic else 'no'} all={all_status}"
        bindings = mod.all_bindings
        if filt is not None:
            bindings = [b for b in bindings if b.kind == "star" or b.name == filt or b.src_name == filt
                        or (b.kind == "class" and any(x.split(".")[-1] == filt for x in b.bases))]
        entries = sorted((b.outline() for b in bindings), key=lambda s: (int(s.split(" ", 1)[0]), s))
        capped = cap is not None and len(entries) > cap
        return Response("symbols", (header,) + tuple(entries[:cap] if capped else entries), capped)


    def _members(self, rel: str, cls: str, cap) -> Response:
        """Direct members of a module-level class: `line kind name`, after a header."""
        from . import analysis
        rel = _norm(rel)
        if not self.is_file(rel) or not rel.endswith(".py"):
            return Response("members", (), False, error=f"not a python file: {rel}")
        mod = analysis.parse_module(rel, self.text(rel))
        if mod.parse_error:
            return Response("members", (), False, error="syntax error")
        classes = [b for b in mod.all_bindings if b.kind == "class" and b.name == cls]
        if not classes:
            return Response("members", (), False, error=f"no module-level class {cls} in {rel}")
        header = f"class {cls} in {rel} definitions={len(classes)}"
        entries = [m.outline() for m in mod.members.get(cls, [])]
        capped = cap is not None and len(entries) > cap
        return Response("members", (header,) + tuple(entries[:cap] if capped else entries), capped)

    def _calls(self, rel: str, name: str, cap) -> Response:
        """Lines with `name(...)` calls whose bare name refers to the module-level binding."""
        from . import analysis
        rel = _norm(rel)
        if not self.is_file(rel) or not rel.endswith(".py"):
            return Response("calls", (), False, error=f"not a python file: {rel}")
        mod = analysis.parse_module(rel, self.text(rel))
        if mod.parse_error:
            return Response("calls", (), False, error="syntax error")
        if mod.calls_unsure:
            return Response("calls", (), False, error="scope analysis unavailable for this module")
        lines = mod.calls.get(name, [])
        header = f"calls of {name} in {rel} count={len(lines)}"
        entries = [f"{ln}:{self.lines(rel)[ln - 1][:MAX_LINE_CHARS]}" for ln in lines]
        capped = cap is not None and len(entries) > cap
        return Response("calls", (header,) + tuple(entries[:cap] if capped else entries), capped)


def parse_grep_line(line: str):
    """'path:line:text' -> (path, line, text)."""
    p, l, t = line.split(":", 2)
    return p, int(l), t


def parse_read_line(line: str):
    l, t = line.split(":", 1)
    return int(l), t
