"""The obligation algebra.

An obligation turns what the agent has seen into open needs and, when nothing is
open, into a typed output with a certificate. Obligations compose into a Chain:
each step's output is the next step's input, under type constraints.

    Resolve(module, name)            -> Target            witness chain
    Importers(target)                -> [statement]       ForAll modules: coverage + per-statement verdicts
    Subclasses(target)               -> [class]           ForAll modules: coverage + per-class base resolution
    Callers(target)                  -> [call site]       ForAll modules: coverage + per-module binding + call sites
    NotOverriding(classes, method)   -> [class]           ForAll given elements: members lookup
    Expose(target, package)          -> patch             closure of the package + a computed one-line import

Universal claims are discharged by coverage (uncapped searches partitioning the
tree) plus a verdict with a reason for every candidate; the verdicts that fail
are the counterexamples. Existential claims are discharged by witnesses.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .analysis import UNKNOWN, Need, Target, exports, package_dir, resolve_dotted, resolve_name
from .knowledge import Seen
from .prior import pattern

SUPERSETS = {"IMPORT": ("IMPORT_OR_STAR",), "STAR": ("IMPORT_OR_STAR",)}


@dataclass(frozen=True)
class OpenItem:
    kind: str
    key: tuple
    desc: str
    need: Optional[Need] = None
    data: tuple = ()


def need_item(need: Need, K: Seen) -> OpenItem:
    if need.kind == "bindings":
        return OpenItem("bindings", ("bindings", need.module, need.arg), f"check the top-level names of `{need.module}` for `{need.arg}`", need)
    if need.kind == "stars":
        return OpenItem("stars", ("stars", need.module), f"find the star imports of `{need.module}`", need)
    if need.kind == "all":
        return OpenItem("all", ("all", need.module), f"read what `{need.module}` exports", need)
    if need.kind == "module_path":
        return OpenItem("module_path", ("module_path", need.module, need.arg), f"find where `{need.arg}` (imported by `{need.module}`) lives", need)
    if need.kind == "submodule":
        return OpenItem("submodule", ("submodule", need.module, need.arg), f"check whether `{package_dir(need.module)}` has a submodule `{need.arg}`", need)
    raise KeyError(need.kind)


def elem_key(x: str):
    parts = x.split(":")
    return tuple(int(p) if p.isdigit() else p for p in parts)


def dedupe(items):
    out, seen = [], set()
    for it in items:
        if it.key not in seen:
            seen.add(it.key)
            out.append(it)
    return out


# ---------------------------------------------------------------------------
# Resolve
# ---------------------------------------------------------------------------

class Resolve:
    kind = "resolve"

    def __init__(self, module: str, name: str):
        self.module = module
        self.name = name

    @property
    def symbol(self):
        return self.name

    def current_name(self, K):
        hops = self.chain(K)
        return hops[-1][1] if hops else self.name

    def open_items(self, K: Seen):
        r = resolve_name(K, self.module, self.name)
        return [need_item(r, K)] if isinstance(r, Need) else []

    def output(self, K: Seen):
        r = resolve_name(K, self.module, self.name)
        return None if isinstance(r, Need) else r

    def certificate(self, K: Seen):
        return {"kind": "witness-chain", "hops": [list(h[:3]) + [h[3] if not isinstance(h[3], tuple) else list(h[3])] for h in self.chain(K)]}

    def chain(self, K: Seen):
        hops = []
        m, n = self.module, self.name
        seen = set()
        while (m, n) not in seen:
            seen.add((m, n))
            bs = K.bindings(m, n)
            if bs is UNKNOWN:
                hops.append((m, n, "open", None))
                break
            if len(bs) == 1 and bs[0].kind == "from":
                mp = K.module_path(bs[0].src, m)
                hops.append((m, n, "reexport", (bs[0].src, mp if mp not in (UNKNOWN, None) else None)))
                if mp in (UNKNOWN, None):
                    break
                m, n = mp, bs[0].src_name
                continue
            if len(bs) == 1:
                hops.append((m, n, bs[0].kind, bs[0].line))
                break
            if not bs:
                stars = K.stars(m)
                if stars is UNKNOWN:
                    hops.append((m, n, "open", None))
                    break
                nxt = None
                for s in stars:
                    mp = K.module_path(s.src, m)
                    if mp not in (UNKNOWN, None) and exports(K, mp, n) is True:
                        nxt = mp
                if nxt:
                    hops.append((m, n, "star", nxt))
                    m = nxt
                    continue
            hops.append((m, n, "other", None))
            break
        return hops

    def state(self, K: Seen):
        return {"chain": [[m, n, k, (list(e) if isinstance(e, tuple) else e)] for m, n, k, e in self.chain(K)]}


# ---------------------------------------------------------------------------
# ForAll over modules found by search
# ---------------------------------------------------------------------------

class ForAllModules:
    """Domain: modules with a line matching one of the pattern classes for `name`.
    Coverage: every scope is covered by an uncapped grep of the class (or a superset
    class) at the scope or an ancestor; a capped grep is split by a complete listing."""
    classes = ()

    def __init__(self, target: Target, name: str):
        self.target = target
        self.name = name

    @property
    def symbol(self):
        return self.name

    def current_name(self, K):
        return self.name

    # ---- coverage ----
    def _grep(self, K, pc, scope):
        return K.greps.get((pattern(pc, self.name), scope))

    def covered(self, K, pc, scope):
        anc = scope
        while True:
            for c in (pc,) + SUPERSETS.get(pc, ()):
                g = self._grep(K, c, anc)
                if g is not None and not g[1]:
                    return True
            if anc == ".":
                return False
            anc = package_dir(anc)

    def capped_at(self, K, pc, scope):
        for c in (pc,) + SUPERSETS.get(pc, ()):
            g = self._grep(K, c, scope)
            if g is not None and g[1]:
                return True
        return False

    def uncovered_scopes(self, K, pc):
        out = []

        def walk(scope):
            if self.covered(K, pc, scope):
                return
            if self.capped_at(K, pc, scope):
                lst = K.listing.get(scope)
                if lst is None or not lst[1]:
                    out.append(("split", scope))
                    return
                for e in lst[0]:
                    full = e if scope == "." else f"{scope}/{e}"
                    if e.endswith("/"):
                        walk(full[:-1])
                    elif e.endswith(".py"):
                        walk(full)
                return
            out.append(("grep", scope))

        walk(".")
        return out

    def candidate_modules(self, K):
        pats = {pattern(c, self.name) for pc in self.classes for c in (pc,) + SUPERSETS.get(pc, ())}
        mods = set()
        for (pat, scope), (hs, capped) in K.greps.items():
            if pat in pats:
                for p, ln, text in hs:
                    if p.endswith(".py"):
                        mods.add(p)
        return sorted(mods)

    # ---- per module: subclasses implement ----
    def module_items(self, K, module):
        """Open items for this module, or [] when its verdicts are all settled."""
        raise NotImplementedError

    def module_elements(self, K, module):
        """[(element_key, verdict 'in'|'out', reason)] or UNKNOWN when items are open."""
        raise NotImplementedError

    # ---- generic ----
    def open_items(self, K):
        items = []
        for pc in self.classes:
            for kind, scope in self.uncovered_scopes(K, pc):
                if kind == "grep":
                    items.append(OpenItem("cover", ("cover", pc, scope), f"search `{scope}` for {self.describe_class(pc)}", data=(pc, scope)))
                else:
                    items.append(OpenItem("split", ("split", scope), f"list `{scope}` to split a capped search", data=(scope,)))
        for m in self.candidate_modules(K):
            items.extend(self.module_items(K, m))
        return dedupe(items)

    def describe_class(self, pc):
        return {"IMPORT": f"imports of `{self.name}`", "STAR": "star imports", "SUBCLASS": f"classes deriving from `{self.name}`", "CALL": f"calls of `{self.name}`"}[pc]

    def output(self, K):
        if self.open_items(K):
            return None
        out = []
        for m in self.candidate_modules(K):
            for key, v, reason in self.module_elements(K, m):
                if v == "in":
                    out.append(key)
        return sorted(set(out), key=elem_key)

    def table(self, K):
        rows = []
        for m in self.candidate_modules(K):
            el = self.module_elements(K, m)
            if el is UNKNOWN:
                rows.append((m, None, "pending", "not yet examined"))
                continue
            if not el:
                rows.append((m, None, "none", "matching line but nothing relevant at module level"))
            for key, v, reason in el:
                rows.append((m, key, v, reason))
        return rows

    def certificate(self, K):
        cov = {pc: [k for k, v in K.greps.items() if not v[1] and k[0] in {pattern(c, self.name) for c in (pc,) + SUPERSETS.get(pc, ())}] for pc in self.classes}
        rows = self.table(K)
        return {"kind": "forall", "coverage": {pc: [list(k) for k in v] for pc, v in cov.items()},
                "witnesses": [list(r) for r in rows if r[2] == "in"], "counterexamples": [list(r) for r in rows if r[2] == "out"]}

    def state(self, K):
        rows = self.table(K)
        return {"candidates": self.candidate_modules(K), "table": [list(r) for r in rows],
                "uncovered": {pc: self.uncovered_scopes(K, pc) for pc in self.classes},
                "n_in": sum(1 for r in rows if r[2] == "in"), "n_out": sum(1 for r in rows if r[2] == "out"),
                "n_pending": sum(1 for r in rows if r[2] == "pending")}


class Importers(ForAllModules):
    kind = "importers"
    classes = ("IMPORT", "STAR")

    def statements(self, K, p):
        if not K.outline_known(p, self.name):
            return UNKNOWN
        out = []
        for ln, lst in sorted(K.outline_stmts.get(p, {}).items()):
            for b in lst:
                if b.kind == "from" and b.src_name == self.name and b.module == p:
                    out.append((ln, b))
        stars = K.stars(p)
        if stars is UNKNOWN:
            return UNKNOWN
        for s in stars:
            out.append((s.line, s))
        seen, final = set(), []
        for ln, b in out:
            k = (ln, b.kind, b.src, b.name)
            if k not in seen:
                seen.add(k)
                final.append((ln, b))
        return final

    def verdict(self, K, p, b):
        mp = K.module_path(b.src, p)
        if mp is UNKNOWN:
            return Need("module_path", p, b.src)
        if mp is None:
            return ("out", f"`{b.src}` is outside the snapshot")
        if b.kind == "from":
            r = resolve_name(K, mp, self.name)
            if isinstance(r, Need):
                return r
            if r.key() == self.target.key():
                return ("in", f"`{b.src}` resolves `{self.name}` to the target")
            return ("out", f"`{b.src}` resolves `{self.name}` to {r}")
        ex = exports(K, mp, self.name)
        if isinstance(ex, Need):
            return ex
        if ex is not True:
            return ("out", f"star import of `{b.src}`, which does not export `{self.name}`")
        r = resolve_name(K, mp, self.name)
        if isinstance(r, Need):
            return r
        if r.key() == self.target.key():
            return ("in", f"star import of `{b.src}`, which exports `{self.name}` from the target")
        return ("out", f"star import of `{b.src}` binds `{self.name}` to {r}")

    def module_items(self, K, p):
        st = self.statements(K, p)
        if st is UNKNOWN:
            return [OpenItem("outline", ("outline", p, self.name), f"look at `{p}`'s imports of `{self.name}`", data=(p, self.name))]
        items = []
        for ln, b in st:
            v = self.verdict(K, p, b)
            if isinstance(v, Need):
                items.append(need_item(v, K))
        return items

    def module_elements(self, K, p):
        st = self.statements(K, p)
        if st is UNKNOWN:
            return UNKNOWN
        out = []
        for ln, b in st:
            v = self.verdict(K, p, b)
            if isinstance(v, Need):
                return UNKNOWN
            out.append((f"{p}:{ln}", v[0], v[1]))
        return out


class Subclasses(ForAllModules):
    kind = "subclasses"
    classes = ("SUBCLASS",)

    def class_entries(self, K, p):
        if not K.outline_known(p, self.name):
            return UNKNOWN
        out = []
        for ln, lst in sorted(K.outline_stmts.get(p, {}).items()):
            for b in lst:
                if b.kind == "class" and b.module == p:
                    for base in b.bases:
                        if base.split(".")[-1] == self.name:
                            out.append((ln, b, base))
                            break
        return out

    def verdict(self, K, p, base):
        r = resolve_dotted(K, p, base)
        if isinstance(r, Need):
            return r
        if r.key() == self.target.key():
            return ("in", f"base `{base}` resolves to the target")
        return ("out", f"base `{base}` resolves to {r}")

    def module_items(self, K, p):
        ce = self.class_entries(K, p)
        if ce is UNKNOWN:
            return [OpenItem("outline", ("outline", p, self.name), f"look at the classes in `{p}` that derive from `{self.name}`", data=(p, self.name))]
        items = []
        for ln, b, base in ce:
            v = self.verdict(K, p, base)
            if isinstance(v, Need):
                items.append(need_item(v, K))
        return items

    def module_elements(self, K, p):
        ce = self.class_entries(K, p)
        if ce is UNKNOWN:
            return UNKNOWN
        out = []
        for ln, b, base in ce:
            v = self.verdict(K, p, base)
            if isinstance(v, Need):
                return UNKNOWN
            out.append((f"{p}:{ln}:{b.name}", v[0], v[1]))
        return out


class Callers(ForAllModules):
    kind = "callers"
    classes = ("CALL",)

    def module_items(self, K, p):
        if not K.outline_known(p, self.name):
            return [OpenItem("outline", ("outline", p, self.name), f"check what `{self.name}` means inside `{p}`", data=(p, self.name))]
        r = resolve_name(K, p, self.name)
        if isinstance(r, Need):
            return [need_item(r, K)]
        if r.key() != self.target.key():
            return []
        if (p, self.name) in K.calls_known or p in K.calls_unsure:
            return []
        return [OpenItem("calls", ("calls", p, self.name), f"list the call sites of `{self.name}` in `{p}`", data=(p, self.name))]

    def module_elements(self, K, p):
        if not K.outline_known(p, self.name):
            return UNKNOWN
        r = resolve_name(K, p, self.name)
        if isinstance(r, Need):
            return UNKNOWN
        if r.key() != self.target.key():
            why = "the name is not bound at module level here" if r.kind == "unresolved" else f"the name resolves to {r} here"
            return [(f"{p}", "out", why)]
        if p in K.calls_unsure:
            return [(f"{p}", "out", "call sites cannot be established for this module")]
        lines = K.calls_known.get((p, self.name))
        if lines is None:
            return UNKNOWN
        if not lines:
            return [(f"{p}", "out", "the module binds the name but never calls it by bare name")]
        return [(f"{p}:{ln}", "in", "bare-name call of the module-level binding, which resolves to the target") for ln in lines]


# ---------------------------------------------------------------------------
# ForAll over a given finite set
# ---------------------------------------------------------------------------

class NotOverriding:
    kind = "not_overriding"

    def __init__(self, classes: list, method: str):
        self.classes = [tuple(c.split(":")) if isinstance(c, str) else tuple(c) for c in classes]  # (module, line, name)
        self.method = method

    @property
    def symbol(self):
        return self.method

    def current_name(self, K):
        return self.method

    def open_items(self, K):
        items = []
        for m, ln, cls in self.classes:
            if (m, cls) not in K.members_known:
                items.append(OpenItem("members", ("members", m, cls), f"look at what `{cls}` in `{m}` defines itself", data=(m, cls)))
        return dedupe(items)

    def table(self, K):
        rows = []
        for m, ln, cls in self.classes:
            mem = K.members_known.get((m, cls), UNKNOWN)
            if mem is UNKNOWN:
                rows.append((m, cls, "pending", "members not yet seen"))
            elif mem is None:
                rows.append((m, cls, "out", "no such class at module level"))
            elif any(kind == "def" and name == self.method for _, kind, name in mem):
                rows.append((m, cls, "out", f"defines `{self.method}` itself"))
            else:
                rows.append((m, cls, "in", f"does not define `{self.method}`"))
        return rows

    def output(self, K):
        if self.open_items(K):
            return None
        return sorted((f"{m}:{ln}:{cls}" for (m, ln, cls), row in zip(self.classes, self.table(K)) if row[2] == "in"), key=elem_key)

    def certificate(self, K):
        rows = self.table(K)
        return {"kind": "forall-given", "witnesses": [list(r) for r in rows if r[2] == "in"], "counterexamples": [list(r) for r in rows if r[2] == "out"]}

    def state(self, K):
        rows = self.table(K)
        return {"table": [list(r) for r in rows], "n_in": sum(1 for r in rows if r[2] == "in"), "n_out": sum(1 for r in rows if r[2] == "out"),
                "n_pending": sum(1 for r in rows if r[2] == "pending")}


# ---------------------------------------------------------------------------
# Repair: expose a definition from a package
# ---------------------------------------------------------------------------

class Expose:
    kind = "expose"

    def __init__(self, target: Target, package_init: str, name: str):
        self.target = target
        self.package = package_init
        self.name = name

    @property
    def symbol(self):
        return self.name

    def current_name(self, K):
        return self.name

    def open_items(self, K):
        r = resolve_name(K, self.package, self.name)
        if isinstance(r, Need):
            return [need_item(r, K)]
        return []

    def spec(self):
        """Import spec for the target module as seen from the package."""
        pkg_dir = package_dir(self.package)
        tpath = self.target.path
        if tpath.endswith("/__init__.py"):
            tmod = tpath[: -len("/__init__.py")]
        else:
            tmod = tpath[:-3]
        if pkg_dir != "." and tmod.startswith(pkg_dir + "/"):
            return "." + tmod[len(pkg_dir) + 1:].replace("/", ".")
        # climb to a common ancestor with leading dots
        up, base = 1, pkg_dir
        while base != "." and not tmod.startswith(base + "/"):
            base = package_dir(base)
            up += 1
        if base == ".":
            return None
        return "." * up + tmod[len(base) + 1:].replace("/", ".")

    def output(self, K):
        if self.open_items(K):
            return None
        r = resolve_name(K, self.package, self.name)
        dyn = K.is_dynamic(self.package)
        if r.kind != "unresolved" or dyn is not False:
            return {"patch": None, "reason": "the package already binds the name" if r.kind != "unresolved" else "the package uses dynamic namespace code"}
        spec = self.spec()
        if spec is None:
            return {"patch": None, "reason": "no relative import path from the package to the target"}
        return {"patch": {"path": self.package, "append": f"from {spec} import {self.name}"},
                "claim": f"after the patch, `{self.name}` in `{self.package}` resolves to {self.target}"}

    def certificate(self, K):
        return {"kind": "repair", "precondition": f"`{self.package}` does not bind `{self.name}` and is not dynamic", "patch": (self.output(K) or {}).get("patch")}

    def state(self, K):
        r = resolve_name(K, self.package, self.name)
        return {"package": self.package, "bound": None if isinstance(r, Need) else r.kind != "unresolved", "spec": self.spec()}


# ---------------------------------------------------------------------------
# Composition
# ---------------------------------------------------------------------------

class Chain:
    """Steps: dicts with an `op` and its parameters. The first step must be a
    Resolve or carry a target; later steps take the previous output."""

    def __init__(self, task: dict):
        self.task = task
        self.steps = task["chain"]
        self.ops = []
        self.stuck = None
        self._build_first()

    def _build_first(self):
        st = self.steps[0]
        if st["op"] == "resolve":
            self.ops.append(Resolve(st["module"], st["name"]))
        else:
            tgt = Target("def", st["def_path"], int(st["def_line"]), st["name"], st.get("def_kind", ""))
            self.ops.append(self._make(st, tgt, None))

    def _make(self, st, target, prev_output):
        op = st["op"]
        if op == "importers":
            return Importers(target, target.name)
        if op == "subclasses":
            return Subclasses(target, target.name)
        if op == "callers":
            return Callers(target, target.name)
        if op == "not_overriding":
            return NotOverriding(prev_output or [], st["method"])
        if op == "expose":
            return Expose(target, st["package"], target.name)
        raise KeyError(op)

    def _advance(self, K):
        while len(self.ops) < len(self.steps) and self.stuck is None:
            cur = self.ops[-1]
            if cur.open_items(K):
                return
            out = cur.output(K)
            nxt = self.steps[len(self.ops)]
            if isinstance(cur, Resolve):
                if out.kind != "def":
                    self.stuck = f"the name resolves to {out}, not a definition"
                    return
                self.ops.append(self._make(nxt, out, None))
            elif isinstance(cur, Subclasses):
                self.ops.append(self._make(nxt, cur.target, out))
            else:
                self.stuck = f"cannot chain {nxt['op']} after {cur.kind}"
                return

    @property
    def current(self):
        return self.ops[-1]

    @property
    def phase(self):
        return self.current.kind

    def current_name(self, K):
        return self.current.current_name(K)

    def open_items(self, K):
        self._advance(K)
        if self.stuck:
            return []
        return self.current.open_items(K)

    def answer(self, K):
        self._advance(K)
        if self.stuck is None and self.current.open_items(K):
            return None
        steps = []
        for op in self.ops:
            out = op.output(K)
            steps.append({"op": op.kind, "output": out.to_json() if isinstance(out, Target) else out})
        final = steps[-1]["output"] if steps else None
        return {"final_kind": self.current.kind, "final": final, "steps": steps, "stuck": self.stuck}

    def certificate(self, K):
        return [op.certificate(K) for op in self.ops]

    def state(self, K):
        return {"phase": self.phase, "step": len(self.ops), "of": len(self.steps), **self.current.state(K)}
