"""Goal state machines. A goal turns what the agent has seen into open needs
and, when nothing is open, into an answer with a certificate.

- ResolveGoal: what definition does a name bound in a module resolve to.
- CoverGoal: every import statement in the snapshot that imports a definition.
  Greps find candidate modules; one filtered outline per module settles its
  statements exactly; each statement's source is resolved with the shared resolver.
- CompositeGoal chains them: resolve first, then cover the result.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .analysis import UNKNOWN, Need, Target, exports, package_dir, resolve_name
from .knowledge import Seen
from .prior import pattern


@dataclass(frozen=True)
class OpenItem:
    kind: str
    key: tuple
    desc: str
    need: Optional[Need] = None
    data: tuple = ()


class ResolveGoal:
    family = "resolve"

    def __init__(self, module: str, name: str):
        self.module = module
        self.name = name

    def open_items(self, K: Seen) -> list:
        r = resolve_name(K, self.module, self.name)
        if isinstance(r, Need):
            return [need_item(r, K)]
        return []

    def result(self, K: Seen):
        r = resolve_name(K, self.module, self.name)
        return None if isinstance(r, Need) else r

    def answer(self, K: Seen):
        r = self.result(K)
        if r is None:
            return None
        return {"target": r.to_json(), "text": str(r)}

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


class CoverGoal:
    family = "cover"
    CLASSES = ("IMPORT", "STAR")

    def __init__(self, target: Target, name: str):
        self.target = target
        self.name = name

    # ---- coverage bookkeeping from grep facts ----
    def _grep(self, K, pc, scope):
        return K.greps.get((pattern(pc, self.name), scope))

    def covered(self, K: Seen, pclass: str, scope: str) -> bool:
        anc = scope
        while True:
            for pc in (pclass, "IMPORT_OR_STAR"):
                g = self._grep(K, pc, anc)
                if g is not None and not g[1]:
                    return True
            if anc == ".":
                return False
            anc = package_dir(anc)

    def capped_at(self, K: Seen, pclass: str, scope: str) -> bool:
        for pc in (pclass, "IMPORT_OR_STAR"):
            g = self._grep(K, pc, scope)
            if g is not None and g[1]:
                return True
        return False

    def uncovered_scopes(self, K: Seen, pclass: str):
        out = []

        def walk(scope):
            if self.covered(K, pclass, scope):
                return
            if self.capped_at(K, pclass, scope):
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

    def candidate_modules(self, K: Seen):
        """Modules with at least one grep line matching an import or star pattern."""
        mods = set()
        pats = {pattern(pc, self.name) for pc in ("IMPORT", "STAR", "IMPORT_OR_STAR")}
        for (pat, scope), (hs, capped) in K.greps.items():
            if pat in pats:
                for p, ln, text in hs:
                    if p.endswith(".py"):
                        mods.add(p)
        return sorted(mods)

    def statements(self, K: Seen, p: str):
        """(line, binding) pairs in module p that could import the name: from-bindings
        of the name and star imports. Requires the outline to be known."""
        out = []
        bs = K.bindings(p, self.name)
        if bs is UNKNOWN:
            return UNKNOWN
        # only module-level statements count: those come from outlines, never from grep lines
        for ln, lst in sorted(K.outline_stmts.get(p, {}).items()):
            for b in lst:
                if b.kind == "from" and b.src_name == self.name and b.module == p:
                    out.append((ln, b))
        stars = K.stars(p)
        if stars is UNKNOWN:
            return UNKNOWN
        for s in stars:
            out.append((s.line, s))
        # dedupe by (line, kind, src)
        seen, final = set(), []
        for ln, b in out:
            k = (ln, b.kind, b.src, b.name)
            if k not in seen:
                seen.add(k)
                final.append((ln, b))
        return final

    def verdict(self, K: Seen, p: str, b):
        """('in'|'out', reason) or Need, for one statement."""
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

    def open_items(self, K: Seen) -> list:
        items = []
        for pc in self.CLASSES:
            for kind, scope in self.uncovered_scopes(K, pc):
                if kind == "grep":
                    items.append(OpenItem("cover", ("cover", pc, scope), f"cover `{scope}` for {pc.lower()} lines", data=(pc, scope)))
                else:
                    items.append(OpenItem("split", ("split", scope), f"list `{scope}` to split a capped grep", data=(scope,)))
        for p in self.candidate_modules(K):
            st = self.statements(K, p)
            if st is UNKNOWN:
                items.append(OpenItem("outline", ("outline", p, self.name), f"outline `{p}` for its `{self.name}` imports", data=(p, self.name)))
                continue
            for ln, b in st:
                v = self.verdict(K, p, b)
                if isinstance(v, Need):
                    items.append(need_item(v, K))
        final, seen = [], set()
        for it in items:
            if it.key in seen:
                continue
            seen.add(it.key)
            final.append(it)
        return final

    def answer(self, K: Seen):
        if self.open_items(K):
            return None
        ins = []
        for p in self.candidate_modules(K):
            for ln, b in self.statements(K, p):
                if self.verdict(K, p, b)[0] == "in":
                    ins.append((p, ln))
        ins = sorted(set(ins))
        return {"statements": [f"{p}:{ln}" for p, ln in ins], "count": len(ins)}

    def verdict_table(self, K: Seen):
        rows = []
        for p in self.candidate_modules(K):
            st = self.statements(K, p)
            if st is UNKNOWN:
                rows.append((p, 0, "pending", "outline not yet seen"))
                continue
            if not st:
                rows.append((p, 0, "none", "no import of the name in this module"))
            for ln, b in st:
                v = self.verdict(K, p, b)
                rows.append((p, ln, "pending" if isinstance(v, Need) else v[0], "" if isinstance(v, Need) else v[1]))
        return rows


class CompositeGoal:
    family = "composite"

    def __init__(self, module: str, name: str):
        self.resolve = ResolveGoal(module, name)
        self.cover = None
        self.name = name

    def _advance(self, K: Seen):
        if self.cover is None:
            r = self.resolve.result(K)
            if r is not None and r.kind == "def":
                self.cover = CoverGoal(r, r.name)

    def open_items(self, K: Seen):
        self._advance(K)
        if self.cover is None:
            return self.resolve.open_items(K)
        return self.cover.open_items(K)

    def answer(self, K: Seen):
        self._advance(K)
        if self.cover is None:
            r = self.resolve.result(K)
            if r is None:
                return None
            return {"target": r.to_json(), "text": str(r), "statements": [], "count": 0, "note": "target is not a definition"}
        a = self.cover.answer(K)
        if a is None:
            return None
        return {"target": self.cover.target.to_json(), "text": str(self.cover.target), **a}

    @property
    def phase(self):
        return "resolve" if self.cover is None else "cover"


def current_name(goal, K: Seen) -> str:
    """The symbol the policy should build patterns from, at this point of the goal."""
    if isinstance(goal, CompositeGoal):
        goal = goal.resolve if goal.cover is None else goal.cover
    if isinstance(goal, CoverGoal):
        return goal.name
    hops = goal.chain(K)
    return hops[-1][1] if hops else goal.name


def need_item(need: Need, K: Seen) -> OpenItem:
    if need.kind == "bindings":
        return OpenItem("bindings", ("bindings", need.module, need.arg), f"close the namespace of `{need.module}` for `{need.arg}`", need)
    if need.kind == "stars":
        return OpenItem("stars", ("stars", need.module), f"know the star imports of `{need.module}`", need)
    if need.kind == "all":
        return OpenItem("all", ("all", need.module), f"know what `{need.module}` exports", need)
    if need.kind == "module_path":
        return OpenItem("module_path", ("module_path", need.module, need.arg), f"locate the module `{need.arg}` imported by `{need.module}`", need)
    if need.kind == "submodule":
        return OpenItem("submodule", ("submodule", need.module, need.arg), f"check whether `{package_dir(need.module)}` has a submodule `{need.arg}`", need)
    raise KeyError(need.kind)
