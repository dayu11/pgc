"""What the agent has seen, as typed facts, and a partial-knowledge resolver.

`Seen` implements analysis.Knowledge over the responses received so far. It
answers UNKNOWN whenever the evidence does not settle a question; the shared
resolver then returns a Need, which the policy turns into a call. Every fact
carries the step that witnessed it so the checker can trace it.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Optional

from .analysis import (DYNAMIC, UNKNOWN, Binding, Knowledge, Need, Target, exports, package_dir,
                       parse_outline_line, relative_base, resolve_name)
from .snapshot import Call, Response, parse_grep_line, parse_read_line

# ----------------------------------------------------------------------------
# Line-level statement parsing (what an engineer reads off a grep or read line)
# ----------------------------------------------------------------------------

_RX_FROM = re.compile(r"^(\s*)from\s+(\.*[\w\.]*)\s+import\s+(.*)$")
_RX_IMPORT = re.compile(r"^(\s*)import\s+(.*)$")
_RX_DEF = re.compile(r"^(\s*)(?:async\s+)?(def|class)\s+(\w+)")
_RX_ASSIGN = re.compile(r"^(\s*)([A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)\s*(?::[^=]*)?(?:[+\-*/|&^%@]|//|\*\*|<<|>>)?=(?!=)")
_RX_ALL_START = re.compile(r"^\s*__all__\s*(?:\+?=)\s*(.*)$")


@dataclass(frozen=True)
class Incomplete:
    """A statement whose bound names are not on the seen line (continuation)."""
    path: str
    line: int
    src: Optional[str]


def _strip_comment(s: str) -> str:
    out = []
    quote = None
    for ch in s:
        if quote:
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
        elif ch == "#":
            break
        out.append(ch)
    return "".join(out)


def parse_line(path: str, line: int, text: str):
    """Parse one source line into bindings. Returns (bindings, incomplete_or_None)."""
    t = _strip_comment(text.rstrip())
    m = _RX_FROM.match(t)
    if m:
        indent, src, rest = len(m.group(1)), m.group(2), m.group(3).strip()
        if rest.endswith("\\"):
            return [], Incomplete(path, line, src)
        if rest.startswith("("):
            if ")" not in rest:
                return [], Incomplete(path, line, src)
            rest = rest[1 : rest.index(")")]
        if rest == "*":
            return [Binding(path, "*", line, "star", src=src, col=indent)], None
        out = []
        for part in rest.split(","):
            part = part.strip()
            if not part:
                continue
            bits = part.split()
            if len(bits) == 1 and re.fullmatch(r"\w+", bits[0]):
                out.append(Binding(path, bits[0], line, "from", src=src, src_name=bits[0], col=indent))
            elif len(bits) == 3 and bits[1] == "as":
                out.append(Binding(path, bits[2], line, "from", src=src, src_name=bits[0], col=indent))
            else:
                return out, Incomplete(path, line, src)
        return out, None
    m = _RX_IMPORT.match(t)
    if m:
        indent, rest = len(m.group(1)), m.group(2).strip()
        if rest.endswith("\\") or rest.startswith("("):
            return [], Incomplete(path, line, None)
        out = []
        for part in rest.split(","):
            bits = part.strip().split()
            if len(bits) == 1 and re.fullmatch(r"[\w\.]+", bits[0]):
                top = bits[0].split(".")[0]
                out.append(Binding(path, top, line, "import", src=top, col=indent))
            elif len(bits) == 3 and bits[1] == "as":
                out.append(Binding(path, bits[2], line, "import", src=bits[0], col=indent))
            else:
                return out, Incomplete(path, line, None)
        return out, None
    m = _RX_DEF.match(t)
    if m:
        return [Binding(path, m.group(3), line, m.group(2), col=len(m.group(1)))], None
    m = _RX_ASSIGN.match(t)
    if m and not t.lstrip().startswith(("return", "yield", "assert", "raise", "if ", "elif ", "while ", "for ")):
        names = [n.strip() for n in m.group(2).split(",")]
        if all(n not in ("def", "class", "import", "from", "lambda") for n in names):
            return [Binding(path, n, line, "assign", col=len(m.group(1))) for n in names], None
    return [], None


def parse_all_list(lines_text: list) -> Optional[object]:
    """Given source lines starting at an `__all__ =` statement, return the list of
    names, DYNAMIC if not a literal list, or None if the statement is cut off."""
    first = _strip_comment(lines_text[0])
    m = _RX_ALL_START.match(first)
    if not m:
        return DYNAMIC
    if "+=" in first.split("=")[0] + "=":
        pass
    buf = []
    depth = 0
    started = False
    for raw in lines_text:
        s = _strip_comment(raw)
        buf.append(s)
        for ch in s:
            if ch in "([":
                depth += 1
                started = True
            elif ch in ")]":
                depth -= 1
        if started and depth <= 0:
            break
    else:
        return None  # ran out of window before the bracket closed
    if not started:
        return DYNAMIC
    text = "\n".join(buf)
    rhs = text.split("=", 1)[1]
    if "+=" in text.split("\n")[0].split("[")[0]:
        return DYNAMIC
    import ast as _ast
    try:
        node = _ast.parse(rhs.strip(), mode="eval").body
    except SyntaxError:
        return DYNAMIC
    if isinstance(node, (_ast.List, _ast.Tuple)) and all(isinstance(e, _ast.Constant) and isinstance(e.value, str) for e in node.elts):
        return [e.value for e in node.elts]
    return DYNAMIC


_RX_HEADER = re.compile(r"^module (\S+) lines=(\d+) dynamic=(yes|no) all=(none|dynamic|static@(\d+))$")


# ----------------------------------------------------------------------------
# Facts
# ----------------------------------------------------------------------------

@dataclass
class Fact:
    kind: str
    data: dict
    step: int

    def to_json(self):
        return {"kind": self.kind, "step": self.step, **self.data}


# ----------------------------------------------------------------------------
# Seen knowledge
# ----------------------------------------------------------------------------

class Seen(Knowledge):
    def __init__(self, task_names=()):
        self.files = set()
        self.dirs = {"."}
        self.listing = {}  # dir -> (entries tuple, complete)
        self.stmts = {}  # path -> {line: [Binding]}
        self.incomplete = {}  # path -> {line: Incomplete}
        self.closure = {}  # (path, name) -> list[Binding]
        self.all_closed = set()  # paths whose complete outline was seen
        self.stars_known = {}  # path -> list[Binding]
        self.header = {}  # path -> dict(lines, dynamic, all_status, all_line)
        self.all_known = {}  # path -> list | None | DYNAMIC
        self.greps = {}  # (pattern, scope) -> (hits tuple, capped)
        self.names = set(task_names)  # grounded identifiers, paths, module specs
        self.facts = []
        self.root_known = False  # root listing complete
        self.first_seen = {n: "task" for n in task_names}
        self._step = "task"
        self.missing = set()  # paths established not to exist
        self.calls_made = set()
        self.reads = set()
        self.outline_stmts = {}  # path -> {line: [Binding]} from outlines only (module level)

    # ---- grounding ----
    def ground(self, *xs):
        for x in xs:
            if x:
                x = str(x)
                if x not in self.names:
                    self.first_seen[x] = self._step
                self.names.add(x)

    def provenance(self, s: str) -> str:
        w = self.first_seen.get(str(s))
        if w is None:
            return "derived"
        return "task" if w == "task" else f"step {w}"

    def is_grounded(self, s: str) -> bool:
        return s in self.names

    def note_path(self, p: str):
        self.files.add(p)
        self.ground(p)
        d = p
        while "/" in d:
            d = d.rsplit("/", 1)[0]
            self.dirs.add(d)
            self.ground(d)

    # ---- absorb responses ----
    def absorb(self, step: int, call: Call, resp: Response) -> list:
        new = []
        self._step = step
        self.calls_made.add(call.key())

        def fact(kind, **data):
            f = Fact(kind, data, step)
            self.facts.append(f)
            new.append(f)

        if resp.error:
            target = None
            if call.tool in ("ls", "grep", "read", "symbols") and ("not a directory" in resp.error or "no such" in resp.error or "not a python file" in resp.error):
                target = call.args[1] if call.tool == "grep" else call.args[0]
                self.missing.add(target)
            fact("error", call=call.key(), error=resp.error, missing=target)
            return new
        if call.tool == "ls":
            d = call.args[0]
            self.dirs.add(d)
            entries = tuple(resp.lines)
            self.listing[d] = (entries, not resp.capped)
            if d == "." and not resp.capped:
                self.root_known = True
            for e in entries:
                full = e if d == "." else f"{d}/{e}"
                if e.endswith("/"):
                    self.dirs.add(full[:-1])
                    self.ground(full[:-1])
                else:
                    self.note_path(full)
            fact("listing", dir=d, entries=list(entries), complete=not resp.capped)
        elif call.tool == "grep":
            pattern, scope = call.args
            hits = []
            for l in resp.lines:
                p, ln, text = parse_grep_line(l)
                self.note_path(p)
                hits.append((p, ln, text))
                self._absorb_stmt(step, p, ln, text)
            self.greps[(pattern, scope)] = (tuple(hits), resp.capped)
            fact("grep", pattern=pattern, scope=scope, hits=[[p, ln] for p, ln, _ in hits], capped=resp.capped)
        elif call.tool == "read":
            path, start, count = call.args[0], int(call.args[1]), int(call.args[2])
            self.note_path(path)
            texts = []
            for l in resp.lines:
                ln, text = parse_read_line(l)
                texts.append((ln, text))
            # join parenthesised / backslash-continued statements inside the window
            i = 0
            while i < len(texts):
                ln, text = texts[i]
                bs, inc = parse_line(path, ln, text)
                if inc is not None:
                    joined = text
                    j = i + 1
                    while j < len(texts):
                        joined += " " + texts[j][1].strip()
                        b2, inc2 = parse_line(path, ln, joined.replace("\\", " "))
                        if inc2 is None and (")" in joined or not joined.rstrip().endswith("\\")):
                            bs, inc = b2, None
                            break
                        j += 1
                    i = j
                self._record_stmt(step, path, ln, bs, inc)
                i += 1
            self.reads.add((path, start, count))
            fact("read", path=path, start=start, count=count, n=len(texts))
            # __all__ list if the window starts on it
            if texts and _RX_ALL_START.match(_strip_comment(texts[0][1])):
                val = parse_all_list([t for _, t in texts])
                if val is not None:
                    self.all_known[path] = val
                    fact("all_names", path=path, value=val)
        elif call.tool == "symbols":
            path = call.args[0]
            filt = call.args[1] if len(call.args) > 1 else None
            self.note_path(path)
            head = _RX_HEADER.match(resp.lines[0]) if resp.lines else None
            if head is None:
                fact("error", call=call.key(), error="bad symbols header")
                return new
            hdr = {"lines": int(head.group(2)), "dynamic": head.group(3) == "yes", "all_status": head.group(4).split("@")[0],
                   "all_line": int(head.group(5)) if head.group(5) else None}
            self.header[path] = hdr
            if hdr["all_status"] == "none":
                self.all_known[path] = None
            elif hdr["all_status"] == "dynamic":
                self.all_known[path] = DYNAMIC
            bindings = [parse_outline_line(path, s) for s in resp.lines[1:]]
            stars = [b for b in bindings if b.kind == "star"]
            nonstar = [b for b in bindings if b.kind != "star"]
            for b in bindings:
                self.ground(b.name, b.src, b.src_name)
                self.stmts.setdefault(path, {}).setdefault(b.line, [])
                if b not in self.stmts[path][b.line]:
                    self.stmts[path][b.line].append(b)
                self.outline_stmts.setdefault(path, {}).setdefault(b.line, [])
                if b not in self.outline_stmts[path][b.line]:
                    self.outline_stmts[path][b.line].append(b)
            if not resp.capped:
                self.stars_known[path] = stars
                if filt is None:
                    self.all_closed.add(path)
                    for b in nonstar:
                        self.closure.setdefault((path, b.name), [])
                    names = {b.name for b in nonstar}
                    for n in names:
                        self.closure[(path, n)] = [b for b in nonstar if b.name == n]
                else:
                    self.closure[(path, filt)] = [b for b in nonstar if b.name == filt]
            fact("outline", path=path, filter=filt, header=hdr, bindings=[b.to_json() for b in bindings], complete=not resp.capped)
        return new

    def _absorb_stmt(self, step, path, line, text):
        bs, inc = parse_line(path, line, text)
        self._record_stmt(step, path, line, bs, inc)

    def _record_stmt(self, step, path, line, bs, inc):
        if bs:
            self.stmts.setdefault(path, {})[line] = bs
            for b in bs:
                self.ground(b.name, b.src, b.src_name)
        if inc is not None:
            self.incomplete.setdefault(path, {})[line] = inc
            self.ground(inc.src)

    # ---- Knowledge interface ----
    def _roots(self):
        """Candidate source roots in oracle order, or UNKNOWN if the root listing is unknown."""
        roots = ["."]
        for r in ("src", "lib"):
            if r in self.dirs:
                roots.append(r)
            elif not self.root_known:
                return UNKNOWN
        return roots

    def _missing(self, p):
        q = p
        while True:
            if q in self.missing:
                return True
            if "/" not in q:
                return False
            q = q.rsplit("/", 1)[0]

    def _dir_exists(self, d):  # True / False / UNKNOWN
        if d == "." or d in self.dirs:
            return True
        if self._missing(d):
            return False
        pd = package_dir(d)
        pe = self._dir_exists(pd)
        if pe is False:
            return False
        plst = self.listing.get(pd)
        if plst is not None and plst[1]:
            return (d.rsplit("/", 1)[-1] + "/") in plst[0]
        return UNKNOWN

    def _exists_file(self, p):  # True / False / UNKNOWN
        if p in self.files:
            return True
        if self._missing(p):
            return False
        d = package_dir(p)
        name = p.rsplit("/", 1)[-1]
        de = self._dir_exists(d)
        if de is False:
            return False
        lst = self.listing.get(d)
        if lst is not None and lst[1]:
            return name in lst[0]
        return UNKNOWN

    def _find(self, base, parts):
        stem = "/".join(parts)
        if base != ".":
            stem = f"{base}/{stem}" if stem else base
        if not stem or stem == ".":
            cand = "__init__.py" if base == "." else f"{base}/__init__.py"
            e = self._exists_file(cand)
            return cand if e is True else (None if e is False else UNKNOWN)
        e1 = self._exists_file(stem + ".py")
        if e1 is True:
            return stem + ".py"
        if e1 is UNKNOWN:
            return UNKNOWN
        e2 = self._exists_file(stem + "/__init__.py")
        if e2 is True:
            return stem + "/__init__.py"
        return None if e2 is False else UNKNOWN

    def module_path(self, spec, from_module):
        level = len(spec) - len(spec.lstrip("."))
        rest = spec.lstrip(".")
        parts = rest.split(".") if rest else []
        if level > 0:
            base = relative_base(from_module, level)
            if base is None:
                return None
            return self._find(base, parts)
        roots = self._roots()
        if roots is UNKNOWN:
            # we may still succeed under '.' since the oracle tries it first
            r = self._find(".", parts)
            return r if r not in (None,) else UNKNOWN
        for root in roots:
            r = self._find(root, parts)
            if r is UNKNOWN or r is not None:
                return r
        return None

    def unknown_dirs_for(self, spec, from_module):
        """Directories whose listing would settle module_path(spec, from_module)."""
        level = len(spec) - len(spec.lstrip("."))
        rest = spec.lstrip(".")
        parts = rest.split(".") if rest else []
        out = []
        roots = self._roots()
        if level > 0:
            base = relative_base(from_module, level)
            bases = [base] if base is not None else []
        elif roots is UNKNOWN:
            bases = ["."]
            out.append(".")
        else:
            bases = roots
        for base in bases:
            stem = "/".join(parts)
            if base != ".":
                stem = f"{base}/{stem}" if stem else base
            if not stem or stem == ".":
                continue
            # the directory holding `name.py`, and the package directory itself
            d = package_dir(stem)
            if self._exists_file(stem + ".py") is UNKNOWN:
                out.append(d)
            elif self._exists_file(stem + "/__init__.py") is UNKNOWN:
                out.append(stem)
        # de-duplicate, keep order; prefer the shallowest known-to-exist ancestor
        seen = []
        for d in out:
            dd = d
            while dd not in self.dirs and dd != "." and not self._missing(dd):
                dd = package_dir(dd)
            if self._missing(dd):
                continue
            if dd not in seen:
                seen.append(dd)
        return seen

    def submodule(self, pkg_dir, name):
        return self._find(pkg_dir, [name])

    def bindings(self, module, name):
        k = (module, name)
        if k in self.closure:
            return self.closure[k]
        if module in self.all_closed:
            return []
        return UNKNOWN

    def stars(self, module):
        return self.stars_known.get(module, UNKNOWN)

    def all_names(self, module):
        if module in self.all_known:
            return self.all_known[module]
        return UNKNOWN

    def is_dynamic(self, module):
        h = self.header.get(module)
        return UNKNOWN if h is None else h["dynamic"]

    # ---- convenience ----
    def outline_known(self, path, name) -> bool:
        return (path, name) in self.closure or path in self.all_closed

    def candidate_module_files(self, spec, from_module):
        """Module files that would satisfy the spec and whose existence is unknown, most likely first."""
        level = len(spec) - len(spec.lstrip("."))
        rest = spec.lstrip(".")
        parts = rest.split(".") if rest else []
        roots = self._roots()
        if level > 0:
            base = relative_base(from_module, level)
            bases = [base] if base is not None else []
        else:
            bases = ["."] if roots is UNKNOWN else roots
        out = []
        for base in bases:
            stem = "/".join(parts)
            if base != ".":
                stem = f"{base}/{stem}" if stem else base
            if not stem or stem == ".":
                continue
            for cand in (stem + ".py", stem + "/__init__.py"):
                if self._exists_file(cand) is UNKNOWN and cand not in out:
                    out.append(cand)
        return out

    def known_all_line(self, module):
        h = self.header.get(module)
        return None if h is None else h.get("all_line")

    def statements_at(self, path, line):
        return self.stmts.get(path, {}).get(line, [])
