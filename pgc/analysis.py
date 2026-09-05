"""Static analysis of Python modules: the declared resolution semantics.

The same resolver serves three parties:
- the setter, with full knowledge (the Index), to choose tasks and compute answers;
- the checker, with full knowledge, to verify the agent's resolution claims;
- the agent, with partial knowledge (what it has seen); wherever knowledge is
  missing the resolver returns a Need instead of guessing. This makes the
  agent's conclusions sound by construction relative to the oracle.

Semantics (v0), stated so a task can declare it:
- A module is a .py file. Source roots are the repository root and, if present,
  `src/` and `lib/`. `import a.b` resolves to `<root>/a/b.py` or
  `<root>/a/b/__init__.py`, first root wins. Relative imports resolve from the
  importing module's package directory. Modules outside the snapshot are external.
- A module-level binding of a name is a def, class, assignment, or import at the
  top level of the module, including inside top-level if/try/with/for blocks.
- `from M import N` binds N to: M's single top-level binding of N; else the
  submodule M/N if M is a package; else the single star-import source of M that
  exports N. A module exports N if its static `__all__` lists N, or, without
  `__all__`, if N is public and bound in the module (directly or via its own
  star imports).
- Bindings take effect in source order: a star import placed after an explicit
  binding of N overrides it if its source exports N, so such star imports are
  checked; star imports placed before the explicit binding are not.
- More than one candidate binding, a non-literal `__all__`, an external star
  import, or a dynamic construct in a module on the path makes the answer
  ambiguous. The setter never asks about ambiguous names.
"""
from __future__ import annotations

import ast
from dataclasses import dataclass, field
from typing import Optional, Union


class _Unknown:
    def __repr__(self):
        return "UNKNOWN"


UNKNOWN = _Unknown()
DYNAMIC = "DYNAMIC"


@dataclass(frozen=True)
class Binding:
    module: str
    name: str
    line: int
    kind: str  # def | class | assign | import | from | star
    src: Optional[str] = None  # module spec as written (leading dots for relative)
    src_name: Optional[str] = None  # for `from`: the imported name before `as`
    conditional: bool = False
    col: int = 0

    def outline(self) -> str:
        if self.kind == "import":
            return f"{self.line} import {self.name} <- {self.src}"
        if self.kind == "from":
            return f"{self.line} from {self.name} <- {self.src} {self.src_name}"
        if self.kind == "star":
            return f"{self.line} star <- {self.src}"
        return f"{self.line} {self.kind} {self.name}"

    def to_json(self):
        return {"module": self.module, "name": self.name, "line": self.line, "kind": self.kind,
                "src": self.src, "src_name": self.src_name, "conditional": self.conditional, "col": self.col}


def parse_outline_line(module: str, s: str) -> Binding:
    """Inverse of Binding.outline (col and conditional are not carried)."""
    parts = s.split(" ")
    line = int(parts[0])
    kind = parts[1]
    if kind == "import":
        return Binding(module, parts[2], line, "import", src=parts[4])
    if kind == "from":
        return Binding(module, parts[2], line, "from", src=parts[4], src_name=parts[5])
    if kind == "star":
        return Binding(module, "*", line, "star", src=parts[3])
    return Binding(module, parts[2], line, kind)


@dataclass
class ModuleInfo:
    path: str
    all_bindings: list = field(default_factory=list)
    stars: list = field(default_factory=list)
    all_names: Union[list, None, str] = None  # list | None | DYNAMIC
    dynamic: bool = False
    parse_error: bool = False
    n_lines: int = 0

    def bindings(self, name: str) -> list:
        return [b for b in self.all_bindings if b.name == name and b.kind != "star"]

    @property
    def is_init(self) -> bool:
        return self.path.endswith("/__init__.py") or self.path == "__init__.py"


_DYN_CALLS = {"globals", "exec", "eval", "__import__"}


def _target_names(t):
    if isinstance(t, ast.Name):
        return [(t.id, t.col_offset)]
    if isinstance(t, (ast.Tuple, ast.List)):
        out = []
        for e in t.elts:
            out += _target_names(e)
        return out
    if isinstance(t, ast.Starred):
        return _target_names(t.value)
    return []


def parse_module(path: str, text: str) -> ModuleInfo:
    mi = ModuleInfo(path=path, n_lines=text.count("\n") + 1)
    try:
        tree = ast.parse(text)
    except (SyntaxError, ValueError):
        mi.parse_error = True
        return mi
    all_nodes = []

    def visit_body(body, conditional):
        for node in body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                mi.all_bindings.append(Binding(path, node.name, node.lineno, "def", conditional=conditional, col=node.col_offset))
                if node.name in ("__getattr__", "__dir__"):
                    mi.dynamic = True
            elif isinstance(node, ast.ClassDef):
                mi.all_bindings.append(Binding(path, node.name, node.lineno, "class", conditional=conditional, col=node.col_offset))
            elif isinstance(node, ast.Assign):
                for t in node.targets:
                    for n, col in _target_names(t):
                        mi.all_bindings.append(Binding(path, n, node.lineno, "assign", conditional=conditional, col=col))
                        if n == "__all__":
                            all_nodes.append(node)
            elif isinstance(node, ast.AnnAssign) and node.value is not None:
                for n, col in _target_names(node.target):
                    mi.all_bindings.append(Binding(path, n, node.lineno, "assign", conditional=conditional, col=col))
                    if n == "__all__":
                        all_nodes.append(node)
            elif isinstance(node, ast.AugAssign):
                for n, col in _target_names(node.target):
                    mi.all_bindings.append(Binding(path, n, node.lineno, "assign", conditional=conditional, col=col))
                    if n == "__all__":
                        all_nodes.append(node)
            elif isinstance(node, ast.Import):
                for a in node.names:
                    if a.asname:
                        mi.all_bindings.append(Binding(path, a.asname, node.lineno, "import", src=a.name, conditional=conditional, col=node.col_offset))
                    else:
                        top = a.name.split(".")[0]
                        mi.all_bindings.append(Binding(path, top, node.lineno, "import", src=top, conditional=conditional, col=node.col_offset))
            elif isinstance(node, ast.ImportFrom):
                spec = "." * (node.level or 0) + (node.module or "")
                for a in node.names:
                    if a.name == "*":
                        b = Binding(path, "*", node.lineno, "star", src=spec, conditional=conditional, col=node.col_offset)
                        mi.all_bindings.append(b)
                        mi.stars.append(b)
                    else:
                        mi.all_bindings.append(Binding(path, a.asname or a.name, node.lineno, "from", src=spec, src_name=a.name, conditional=conditional, col=node.col_offset))
            elif isinstance(node, ast.If):
                visit_body(node.body, True)
                visit_body(node.orelse, True)
            elif isinstance(node, (ast.Try, getattr(ast, "TryStar", ast.Try))):
                visit_body(node.body, True)
                for h in node.handlers:
                    visit_body(h.body, True)
                visit_body(node.orelse, True)
                visit_body(node.finalbody, True)
            elif isinstance(node, (ast.With, ast.AsyncWith)):
                visit_body(node.body, True)
            elif isinstance(node, (ast.For, ast.AsyncFor, ast.While)):
                if isinstance(node, (ast.For, ast.AsyncFor)):
                    for n, col in _target_names(node.target):
                        mi.all_bindings.append(Binding(path, n, node.lineno, "assign", conditional=True, col=col))
                visit_body(node.body, True)
                visit_body(node.orelse, True)
            elif isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
                f = node.value.func
                if isinstance(f, ast.Name) and f.id in _DYN_CALLS:
                    mi.dynamic = True
                if isinstance(f, ast.Attribute) and f.attr in ("import_module",):
                    mi.dynamic = True

    visit_body(tree.body, False)

    # __all__
    if all_nodes:
        if len(all_nodes) == 1 and isinstance(all_nodes[0], (ast.Assign, ast.AnnAssign)):
            v = all_nodes[0].value
            if isinstance(v, (ast.List, ast.Tuple)) and all(isinstance(e, ast.Constant) and isinstance(e.value, str) for e in v.elts):
                mi.all_names = [e.value for e in v.elts]
            else:
                mi.all_names = DYNAMIC
        else:
            mi.all_names = DYNAMIC

    # dynamic namespace manipulation anywhere in the module
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            f = node.func
            if isinstance(f, ast.Name) and f.id == "globals":
                mi.dynamic = True
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Subscript) and isinstance(t.value, ast.Attribute) and t.value.attr == "modules":
                    mi.dynamic = True
    return mi


# ----------------------------------------------------------------------------
# Targets and Needs
# ----------------------------------------------------------------------------

@dataclass(frozen=True)
class Target:
    kind: str  # def | module | external | ambiguous | unresolved
    path: Optional[str] = None
    line: Optional[int] = None
    name: Optional[str] = None
    detail: str = ""

    def to_json(self):
        return {"kind": self.kind, "path": self.path, "line": self.line, "name": self.name, "detail": self.detail}

    def key(self):
        return (self.kind, self.path, self.line, self.name)

    def __str__(self):
        if self.kind == "def":
            return f"{self.path}:{self.line}"
        if self.kind == "module":
            return f"module {self.path}"
        return f"{self.kind}({self.detail})"


@dataclass(frozen=True)
class Need:
    """A piece of knowledge the resolver lacks. The agent turns these into calls."""
    kind: str  # module_path | bindings | stars | all | submodule
    module: str  # module path the need is about (or the importing module for module_path)
    arg: Optional[str] = None  # name, or module spec

    def key(self):
        return (self.kind, self.module, self.arg)

    def __str__(self):
        return f"{self.kind}({self.module}, {self.arg})"


class Knowledge:
    """Interface. Return UNKNOWN when the answer is not established."""

    def module_path(self, spec: str, from_module: str):  # -> str | None | UNKNOWN
        raise NotImplementedError

    def submodule(self, pkg_dir: str, name: str):  # -> str | None | UNKNOWN
        raise NotImplementedError

    def bindings(self, module: str, name: str):  # -> list[Binding] | UNKNOWN
        raise NotImplementedError

    def stars(self, module: str):  # -> list[Binding] | UNKNOWN
        raise NotImplementedError

    def all_names(self, module: str):  # -> list | None | DYNAMIC | UNKNOWN
        raise NotImplementedError

    def is_dynamic(self, module: str):  # -> bool | UNKNOWN
        raise NotImplementedError


def package_dir(module_path: str) -> str:
    """Directory that acts as the module's package for relative imports."""
    if "/" not in module_path:
        return "."
    return module_path.rsplit("/", 1)[0]


def relative_base(module_path: str, level: int) -> Optional[str]:
    d = package_dir(module_path)
    for _ in range(level - 1):
        if d == ".":
            return None
        d = "." if "/" not in d else d.rsplit("/", 1)[0]
    return d


def resolve_name(K: Knowledge, module: str, name: str, visited=()):
    """Resolve `name` as bound in `module`. Returns Target or Need."""
    key = (module, name)
    if key in visited:
        return Target("ambiguous", module, None, name, "cycle")
    visited = visited + (key,)
    dyn = K.is_dynamic(module)
    if dyn is UNKNOWN:
        return Need("bindings", module, name)
    if dyn:
        return Target("ambiguous", module, None, name, "dynamic module")
    bs = K.bindings(module, name)
    if bs is UNKNOWN:
        return Need("bindings", module, name)
    stars = K.stars(module)
    if stars is UNKNOWN:
        return Need("stars", module, None)
    # a later star import that also exports the name would override an explicit binding
    # (Python binds in source order), so only star imports after the binding are checked
    explicit_line = bs[0].line if len(bs) == 1 else None
    star_sources = []
    for s in stars:
        if explicit_line is not None and s.line < explicit_line:
            continue
        mp = K.module_path(s.src, module)
        if mp is UNKNOWN:
            return Need("module_path", module, s.src)
        if mp is None:
            if not bs:
                return Target("ambiguous", module, None, name, f"external star import {s.src}")
            continue
        ex = exports(K, mp, name)
        if isinstance(ex, Need):
            return ex
        if ex == "AMBIGUOUS":
            return Target("ambiguous", module, None, name, f"star source {mp} has dynamic __all__")
        if ex:
            star_sources.append(mp)
    if len(bs) > 1:
        return Target("ambiguous", module, None, name, "multiple bindings")
    if len(bs) == 1:
        if star_sources:
            return Target("ambiguous", module, None, name, "binding and star source both provide the name")
        b = bs[0]
        if b.kind in ("def", "class", "assign"):
            return Target("def", module, b.line, name, b.kind)
        if b.kind == "import":
            mp = K.module_path(b.src, module)
            if mp is UNKNOWN:
                return Need("module_path", module, b.src)
            if mp is None:
                return Target("external", None, None, name, b.src)
            return Target("module", mp, None, name)
        if b.kind == "from":
            mp = K.module_path(b.src, module)
            if mp is UNKNOWN:
                return Need("module_path", module, b.src)
            if mp is None:
                return Target("external", None, None, name, f"{b.src}.{b.src_name}")
            return resolve_name(K, mp, b.src_name, visited)
    # no explicit binding: submodule of a package?
    if module.endswith("__init__.py"):
        sub = K.submodule(package_dir(module), name)
        if sub is UNKNOWN:
            return Need("submodule", module, name)
        if sub:
            return Target("module", sub, None, name)
    if len(star_sources) > 1:
        return Target("ambiguous", module, None, name, "multiple star sources export the name")
    if len(star_sources) == 1:
        return resolve_name(K, star_sources[0], name, visited)
    return Target("unresolved", module, None, name, "no binding")


def exports(K: Knowledge, module: str, name: str, visited=()):
    """Does `module` export `name` under `from module import *`? True/False/'AMBIGUOUS' or Need."""
    if module in visited:
        return False
    visited = visited + (module,)
    al = K.all_names(module)
    if al is UNKNOWN:
        return Need("all", module, None)
    if al == DYNAMIC:
        return "AMBIGUOUS"
    if al is not None:
        return name in al
    if name.startswith("_"):
        return False
    bs = K.bindings(module, name)
    if bs is UNKNOWN:
        return Need("bindings", module, name)
    if bs:
        return True
    stars = K.stars(module)
    if stars is UNKNOWN:
        return Need("stars", module, None)
    for s in stars:
        mp = K.module_path(s.src, module)
        if mp is UNKNOWN:
            return Need("module_path", module, s.src)
        if mp is None:
            return "AMBIGUOUS"
        ex = exports(K, mp, name, visited)
        if isinstance(ex, Need) or ex == "AMBIGUOUS" or ex is True:
            return ex
    return False


# ----------------------------------------------------------------------------
# The full-knowledge index
# ----------------------------------------------------------------------------

class Index(Knowledge):
    def __init__(self, snap):
        self.snap = snap
        self.modules = {}
        for f in snap.py_files:
            self.modules[f] = parse_module(f, snap.text(f))
        self.roots = [r for r in (".", "src", "lib") if snap.is_dir(r)]
        self._cache = {}
        self._by_src_name = {}
        self._defs_by_name = {}
        self._star_modules = []
        for p, mi in self.modules.items():
            if mi.stars:
                self._star_modules.append(p)
            for b in mi.all_bindings:
                if b.kind == "from":
                    self._by_src_name.setdefault(b.src_name, []).append(b)
                elif b.kind in ("def", "class", "assign"):
                    self._defs_by_name.setdefault(b.name, []).append((p, b.line, b.kind))

    # -- Knowledge --
    def module_path(self, spec, from_module):
        level = len(spec) - len(spec.lstrip("."))
        rest = spec.lstrip(".")
        parts = rest.split(".") if rest else []
        if level > 0:
            base = relative_base(from_module, level)
            if base is None:
                return None
            return self._find(base, parts)
        for root in self.roots:
            p = self._find(root, parts)
            if p:
                return p
        return None

    def _find(self, base, parts):
        stem = "/".join(parts)
        if base != ".":
            stem = f"{base}/{stem}" if stem else base
        if not stem or stem == ".":
            cand = "__init__.py" if base == "." else f"{base}/__init__.py"
            return cand if self.snap.is_file(cand) else None
        if self.snap.is_file(stem + ".py"):
            return stem + ".py"
        if self.snap.is_file(stem + "/__init__.py"):
            return stem + "/__init__.py"
        return None

    def submodule(self, pkg_dir, name):
        return self._find(pkg_dir, [name])

    def bindings(self, module, name):
        mi = self.modules.get(module)
        if mi is None or mi.parse_error:
            return []
        return mi.bindings(name)

    def stars(self, module):
        mi = self.modules.get(module)
        return [] if mi is None else mi.stars

    def all_names(self, module):
        mi = self.modules.get(module)
        return None if mi is None else mi.all_names

    def is_dynamic(self, module):
        mi = self.modules.get(module)
        return True if mi is None or mi.parse_error else mi.dynamic

    # -- oracle services --
    def resolve(self, module, name) -> Target:
        k = (module, name)
        if k not in self._cache:
            r = resolve_name(self, module, name)
            assert not isinstance(r, Need), r
            self._cache[k] = r
        return self._cache[k]

    def resolve_binding(self, b: Binding) -> Target:
        return self.resolve(b.module, b.name)

    def chain(self, module, name):
        """Hops visited while resolving, for difficulty measurement."""
        hops = []
        visited = set()
        cur = (module, name)
        while cur not in visited:
            visited.add(cur)
            m, n = cur
            hops.append(cur)
            bs = self.bindings(m, n)
            if len(bs) == 1 and bs[0].kind == "from":
                mp = self.module_path(bs[0].src, m)
                if mp is None:
                    break
                cur = (mp, bs[0].src_name)
                continue
            if not bs:
                # star route
                srcs = []
                for s in self.stars(m):
                    mp = self.module_path(s.src, m)
                    if mp and exports(self, mp, n) is True:
                        srcs.append(mp)
                if len(srcs) == 1:
                    cur = (srcs[0], n)
                    hops.append(("*", srcs[0]))
                    continue
            break
        return hops

    def defs_named(self, name):
        return list(self._defs_by_name.get(name, []))

    def from_imports_of_name(self, name):
        return list(self._by_src_name.get(name, []))

    def importers_of(self, target: Target):
        """Statement-level: from-imports whose source resolves the name to target, and
        star imports of modules that export the name from target."""
        out = []
        for b in self._by_src_name.get(target.name, []):
            mp = self.module_path(b.src, b.module)
            if mp and self.resolve(mp, b.src_name).key() == target.key():
                out.append((b.module, b.line, "from", b.name))
        for p in self._star_modules:
            for s in self.modules[p].stars:
                mp = self.module_path(s.src, p)
                if mp and exports(self, mp, target.name) is True and self.resolve(mp, target.name).key() == target.key():
                    out.append((p, s.line, "star", target.name))
        return sorted(set(out))
