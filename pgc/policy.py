"""The decision half: grounded candidates, a cap-aware outcome model, and a
depth-2 contingency search over open items. Pure function of (seen, prior, seed).

All arithmetic is in Fractions so replay is bit-identical.
"""
from __future__ import annotations

import hashlib
import random
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Optional

from .analysis import UNKNOWN, package_dir
from .obligations import OpenItem
from .knowledge import Seen
from .prior import Prior, depth_kind, pattern, scope_kind
from .snapshot import Call

F = Fraction
ALL_WINDOW = 30
STMT_WINDOW = 12


@dataclass
class Candidate:
    call: Call
    serves: set
    provenance: str
    outcomes: list = field(default_factory=list)  # [(label, prob, resolved_keys, spawned_h)]
    v1: Optional[Fraction] = None
    v2: Optional[Fraction] = None
    plan: dict = field(default_factory=dict)  # label -> Call | "done" | "continue"

    @property
    def p_cap(self):
        return sum((p for l, p, _, _ in self.outcomes if l == "cap"), F(0))

    @property
    def spawned(self):
        return sum((p * s for _, p, _, s in self.outcomes), F(0))

    def forecast(self):
        return {l: p for l, p, _, _ in self.outcomes}


class Policy:
    def __init__(self, prior: Prior, name: str, seed: int):
        self.prior = prior
        self.name = name  # the symbol the task is about; used for pattern construction
        self.seed = seed
        self._h_b_mod = None

    # ------------------------------------------------------------------ costs
    def mtype(self, path: str) -> str:
        return "init" if path.endswith("__init__.py") else "mod"

    def h_b(self, path: str) -> Fraction:
        hop_mod = self.prior.hop("mod")
        if self._h_b_mod is None:
            denom = 1 - hop_mod["reexport"] - hop_mod["star"]
            self._h_b_mod = (1 + hop_mod["reexport"] * self.h_mp() + hop_mod["star"] * 1) / denom
        if self.mtype(path) == "mod":
            return self._h_b_mod
        hop = self.prior.hop("init")
        return 1 + hop["reexport"] * (self.h_mp() + self._h_b_mod) + hop["star"] * (1 + self._h_b_mod) + hop["none"] * 1

    def h_mp(self) -> Fraction:
        return F(1)

    def hop_dist(self, K: Seen, M: str, names: set) -> dict:
        """Distribution over what closing `names` in M will reveal, conditioned on what has
        been seen about those names in M: a from/import line, a definition, or use as the
        head of a dotted base (`grammar.Grammar`), else the module-type prior."""
        seen_kinds = set()
        for ln, bs in K.stmts.get(M, {}).items():
            for b in bs:
                if b.name in names and b.kind != "star":
                    seen_kinds.add(b.kind)
        if seen_kinds & {"from", "import"}:
            return {"def": F(1, 100), "reexport": F(93, 100), "star": F(1, 100), "none": F(5, 100)}
        if seen_kinds & {"def", "class", "assign"}:
            return {"def": F(94, 100), "reexport": F(2, 100), "star": F(1, 100), "none": F(3, 100)}
        # a name used anywhere as the head of a dotted base (`grammar.Grammar`) denotes a module:
        # in the module that binds it expect an import; in its source package expect a submodule
        used_as_module = any(b.kind == "class" and any("." in x and x.split(".")[0] in names for x in b.bases)
                             for stmts in K.stmts.values() for bs in stmts.values() for b in bs)
        if used_as_module:
            if self.mtype(M) == "init":
                return {"def": F(3, 100), "reexport": F(30, 100), "star": F(2, 100), "none": F(65, 100)}
            return {"def": F(3, 100), "reexport": F(92, 100), "star": F(1, 100), "none": F(4, 100)}
        return self.prior.hop(self.mtype(M))

    def h_bindings(self, K: Seen, M: str, name: str) -> Fraction:
        """Expected calls to close `name` in M and follow whatever that reveals; uses the same
        conditional distribution as the outcome model, so resolving the item and paying for
        what it spawns nets exactly the one call."""
        hop = self.hop_dist(K, M, {name})
        after_all = self.prior.allstat(self.mtype(M))["static"] * 1
        return (1 + hop["reexport"] * (self.h_mp() + self.h_b("x.py")) + hop["star"] * (1 + self.h_b("x.py") + after_all)
                + hop["none"] * (F(1) if self.mtype(M) == "init" else F(0)))

    def h_cover(self, K: Seen, pc: str, scope: str, depth: int = 0) -> Fraction:
        sk = scope_kind(scope, scope in K.files)
        g = self.prior.grep(pc, sk)
        hits_cost = g["mid"] * self.prior.grep_mid_hits(pc, sk) * self.prior.src_new() * (self.h_mp() + self.h_b("x.py"))
        cap_cost = g["cap"] * self.h_split(K, scope, depth + 1) if depth < 2 else g["cap"] * 2
        return 1 + hits_cost + cap_cost

    def h_split(self, K: Seen, scope: str, depth: int = 1) -> Fraction:
        dk = depth_kind(scope)
        child_scope = (scope + "/child") if scope != "." else "child"
        n = self.prior.children(dk)
        return 1 + n * (self.h_cover(K, "IMPORT", child_scope, depth) if depth < 2 else F(1))

    def h(self, K: Seen, it: OpenItem) -> Fraction:
        if it.kind == "bindings":
            return self.h_bindings(K, it.need.module, it.need.arg)
        if it.kind in ("stars", "all", "submodule", "members", "calls"):
            return F(1)
        if it.kind == "outline":
            return F(1) + self.prior.src_new() * (self.h_mp() + self.h_b("x.py"))
        if it.kind == "module_path":
            # locating the module is always followed by closing it
            return self.h_mp() + self.h_b(self._likely_path(K, it))
        if it.kind == "cover":
            pc, scope = it.data
            return self.h_cover(K, pc, scope)
        if it.kind == "split":
            return self.h_split(K, it.data[0])
        return F(1)

    def _likely_path(self, K: Seen, it: OpenItem) -> str:
        cands = K.candidate_module_files(it.need.arg, it.need.module)
        return cands[0] if cands else "x.py"

    # ------------------------------------------------------------- candidates
    def candidates(self, K: Seen, items: list) -> list:
        cands = {}

        def add(call: Call, item: OpenItem, prov: str):
            k = call.key()
            if k in K.calls_made:
                return
            if call.tool == "grep":  # an uncapped grep at an ancestor already covers this scope
                pat, scope = call.args
                anc = scope
                while True:
                    g = K.greps.get((pat, anc))
                    if g is not None and not g[1]:
                        return
                    if anc == ".":
                        break
                    anc = package_dir(anc)
            if k not in cands:
                cands[k] = Candidate(call, set(), prov)
            cands[k].serves.add(item.key)

        for it in items:
            if it.kind == "bindings":
                M, n = it.need.module, it.need.arg
                add(Call("symbols", (M, n)), it, f"module `{M}` ({K.provenance(M)}), name `{n}` ({K.provenance(n)})")
                add(Call("symbols", (M,)), it, f"module `{M}` ({K.provenance(M)})")
            elif it.kind == "stars":
                M = it.need.module
                add(Call("symbols", (M,)), it, f"module `{M}` ({K.provenance(M)})")
            elif it.kind == "all":
                M = it.need.module
                L = K.known_all_line(M)
                if L is not None:
                    win = ALL_WINDOW if (M, L, ALL_WINDOW) not in K.reads else 60
                    add(Call("read", (M, L, win)), it, f"`__all__` of `{M}` starts at line {L} (outline header)")
                else:
                    add(Call("symbols", (M, self.name)), it, f"module `{M}` ({K.provenance(M)})")
            elif it.kind == "module_path":
                frm, spec = it.need.module, it.need.arg
                for d in K.unknown_dirs_for(spec, frm):
                    add(Call("ls", (d,)), it, f"`{spec}` imported by `{frm}` should live under `{d}`")
                n = self._name_for_spec(K, frm, spec) or self.name
                for cand in K.candidate_module_files(spec, frm)[:2]:
                    add(Call("symbols", (cand, n)), it, f"`{spec}` would be `{cand}` if that file exists; one call both checks and closes it")
                is_module_name = any(b.kind == "class" and any("." in x and x.split(".")[0] == n for x in b.bases)
                                     for ln, bs in K.stmts.get(frm, {}).items() for b in bs)
                if not is_module_name:
                    scopes = ["."] + [r for r in ("src", "lib") if r in K.dirs]
                    for sc in scopes:
                        add(Call("grep", (pattern("DEF", n), sc)), it, f"a `def`/`class {n}` statement would reveal the module file; `{n}` {K.provenance(n)}")
            elif it.kind == "submodule":
                M, n = it.need.module, it.need.arg
                d = package_dir(M)
                lst = K.listing.get(d)
                if lst is None:
                    add(Call("ls", (d,)), it, f"package directory of `{M}`")
                # probes settle existence even when the listing is capped
                for cand in (f"{d}/{n}.py", f"{d}/{n}/__init__.py") if d != "." else (f"{n}.py", f"{n}/__init__.py"):
                    if K._exists_file(cand) is UNKNOWN:
                        add(Call("symbols", (cand, n)), it, f"a submodule `{n}` would be `{cand}`; outlining it settles whether it exists")
            elif it.kind == "outline":
                p, n = it.data
                add(Call("symbols", (p, n)), it, f"`{p}` had a matching line ({K.provenance(p)}); its outline names every `{n}` import exactly")
            elif it.kind == "cover":
                pc, scope = it.data
                add(Call("grep", (pattern(pc, self.name), scope)), it, f"{pc.lower()} lines naming `{self.name}` under `{scope}` ({K.provenance(scope)})")
                if pc in ("IMPORT", "STAR"):
                    add(Call("grep", (pattern("IMPORT_OR_STAR", self.name), scope)), it, f"import and star lines under `{scope}` in one call")
            elif it.kind == "members":
                m, cls = it.data
                add(Call("members", (m, cls)), it, f"the members `{cls}` defines itself ({K.provenance(m)})")
            elif it.kind == "calls":
                p_, n = it.data
                add(Call("calls", (p_, n)), it, f"call sites of `{n}` in `{p_}` that refer to the module-level binding")
            elif it.kind == "split":
                (scope,) = it.data
                lst = K.listing.get(scope)
                if lst is None:
                    add(Call("ls", (scope,)), it, f"children of `{scope}` to split the capped grep")
                else:  # the listing itself is capped: try the narrower per-class patterns instead
                    for pc in ("IMPORT", "STAR"):
                        add(Call("grep", (pattern(pc, self.name), scope)), it, f"the combined grep capped at `{scope}` and its listing is capped too; {pc.lower()} lines alone may fit")
        out = sorted(cands.values(), key=lambda c: c.call.key())
        for c in out:
            c.outcomes = self.outcomes(K, c, items)
        return out

    def _name_for_spec(self, K: Seen, frm: str, spec: str) -> Optional[str]:
        for ln, bs in K.stmts.get(frm, {}).items():
            for b in bs:
                if b.kind == "from" and b.src == spec:
                    return b.src_name
        return None

    def _probe_missing(self, K: Seen, c: Candidate, items: list) -> Fraction:
        """Probability that a probed module file does not exist. Uses the form prior
        (module vs package), the external-package prior for absolute specs whose
        top-level directory is unseen, what listings already establish, and the
        split across candidate roots."""
        P = self.prior
        M = c.call.args[0]
        is_init = M.endswith("__init__.py")
        d = package_dir(M)
        if is_init and K._dir_exists(d) is True:
            return F(1, 50)  # the package directory is there; only a missing __init__.py would fail
        p_exists = (P.src_is_package() if is_init else 1 - P.src_is_package())
        by_key = {it.key: it for it in items}
        for k in c.serves:
            it = by_key.get(k)
            if it is None or it.kind != "module_path":
                continue
            spec = it.need.arg
            cands = K.candidate_module_files(spec, it.need.module)
            n_bases = max(1, len({cc.split("/")[0] if cc.count("/") >= 1 else "." for cc in cands}))
            if not spec.startswith("."):
                top = spec.lstrip(".").split(".")[0]
                top_dir = top if not M.startswith(("src/", "lib/")) else M.split("/")[0] + "/" + top
                if K._dir_exists(top_dir) is not True:
                    p_exists *= (1 - P.abs_external())
                p_exists /= n_bases
            break
        return 1 - p_exists

    # ---------------------------------------------------------- observation
    def outcomes(self, K: Seen, c: Candidate, items: list) -> list:
        by_key = {it.key: it for it in items}
        served = [by_key[k] for k in sorted(c.serves) if k in by_key]
        keys = set(c.serves)
        call = c.call
        P = self.prior
        if call.tool == "symbols":
            M = call.args[0]
            mt = self.mtype(M)
            hop = P.hop(mt)
            stat = P.allstat(mt)
            after_all = stat["static"] * 1
            n = call.args[1] if len(call.args) > 1 else None
            unknown_file = M not in K.files and M not in K.header
            if any(it.kind == "outline" for it in served) and not any(it.kind in ("bindings", "module_path") for it in served):
                spawned = P.src_new() * (self.h_mp() + self.h_b("x.py"))
                return [("ok", F(49, 50), keys, spawned), ("cap", F(1, 50), set(), F(0))]
            names = {n} if n is not None else {it.need.arg for it in served if it.kind == "bindings" and it.need is not None}
            hop = self.hop_dist(K, M, names) if names else hop
            base = [
                ("def", hop["def"], keys, F(0)),
                ("reexport", hop["reexport"], keys, self.h_mp() + self.h_b("x.py")),
                ("star", hop["star"], keys, 1 + self.h_b("x.py") + after_all),
                ("none", hop["none"], keys, F(1) if mt == "init" else F(0)),
            ]
            if unknown_file:  # a probe: the file may not exist
                pm = self._probe_missing(K, c, items)
                base = [(l, p * (1 - pm), r, sp) for l, p, r, sp in base] + [("missing", pm, set(), F(0))]
            if n is None:  # unfiltered: may cap
                pc = P.symcap(mt)
                return [(l, p * (1 - pc), r, sp) for l, p, r, sp in base] + [("cap", pc, set(), F(0))]
            return base
        if call.tool == "ls":
            d = call.args[0]
            pc = P.lscap(depth_kind(d))
            spawned = F(0)
            for it in served:
                if it.kind == "split":
                    spawned += P.children(depth_kind(d)) * self.h_cover(K, "IMPORT", d + "/child" if d != "." else "child", 1)
                elif it.kind == "module_path":
                    spawned += self.h_b(self._likely_path(K, it))
            if d == "." and K._roots() is UNKNOWN:
                # the root listing also fixes the source roots, which every later absolute import needs;
                # count that as half a call saved per absolute import still open
                n_abs = sum(1 for it in items if it.kind == "module_path" and not it.need.arg.startswith("."))
                spawned -= F(1, 2) * n_abs
            return [("complete", 1 - pc, keys, spawned), ("cap", pc, set(), F(0))]
        if call.tool == "grep":
            pat, scope = call.args
            sk = scope_kind(scope, scope in K.files)
            pcls = pattern_class(pat)
            g = P.grep(pcls, sk)
            if pcls == "DEF":
                # a def/class hit locates the module only if the import's source is a plain module
                # that itself defines the name; a package (`from flask import x`) is not located this way
                res, spawned = set(), F(0)
                for it in served:
                    if it.kind != "module_path":
                        continue
                    spec = it.need.arg
                    single_abs = (not spec.startswith(".")) and ("." not in spec.lstrip("."))
                    roots_known = spec.startswith(".") or K._roots() is not UNKNOWN
                    if not single_abs and roots_known:
                        res.add(it.key)
                        spawned += self.h_b(self._likely_path(K, it))
                return [("zero", g["zero"], set(), F(0)), ("mid", g["mid"], res, spawned), ("cap", g["cap"], set(), F(0))]
            cover_keys = {k for k in keys if k[0] == "cover"}
            # a directory that holds few python files (docs, CI config) is far more likely to come back empty
            share = F(1) if scope in K.files and scope.endswith(".py") else (F(1, 50) if scope in K.files else P.dir_share(scope))
            p_zero = g["zero"] + (1 - g["zero"]) * (1 - share)
            p_mid = g["mid"] * share
            p_cap = g["cap"] * share
            # follow-up work on hits is inevitable whichever scope is searched first; closing a scope with
            # more expected candidates is the larger step forward, so it is not charged here
            return [
                ("zero", p_zero, keys, F(0)),
                ("mid", p_mid, keys, F(0)),
                ("cap", p_cap, cover_keys, self.h_split(K, scope) if cover_keys else F(0)),
            ]
        if call.tool == "read":
            pf = P.allfit()
            return [("fits", pf, keys, F(0)), ("long", 1 - pf, set(), F(0))]
        if call.tool in ("members", "calls"):
            return [("ok", F(19, 20), keys, F(0)), ("cap", F(1, 20), set(), F(0))]
        return [("ok", F(1), keys, F(0))]

    # ---------------------------------------------------------------- search
    def choose(self, K: Seen, items: list, step: int, depth: int = 2, preferred_key: Optional[str] = None):
        cands = self.candidates(K, items)
        if not cands:
            return None, []
        hval = {it.key: self.h(K, it) for it in items}
        H0 = sum(hval.values(), F(0))

        def v1(c: Candidate, live: set, H: Fraction) -> Fraction:
            val = F(1)
            for _, p, resolved, spawned in c.outcomes:
                val += p * (H - sum((hval[k] for k in resolved if k in live), F(0)) + spawned)
            return val

        live0 = set(hval)
        for c in cands:
            c.v1 = v1(c, live0, H0)
        for c in cands:
            val = F(1)
            plan = {}
            for label, p, resolved, spawned in c.outcomes:
                rem = live0 - resolved
                H_rem = sum((hval[k] for k in rem), F(0)) + spawned
                if not rem and spawned == 0:
                    best, nxt = F(0), "done"
                    # a search that returns candidates opens work the abstract state does not carry
                    if c.call.tool == "grep" and label == "mid" and any(k[0] == "cover" for k in c.serves):
                        nxt = "continue"
                else:
                    best, nxt = None, "continue"
                    for c2 in cands:
                        if c2 is c or not (c2.serves & rem):
                            continue
                        v = v1(c2, rem, H_rem)
                        if best is None or v < best or (v == best and c2.call.key() < nxt.key()):
                            best, nxt = v, c2.call
                    if best is None:
                        best = H_rem
                val += p * best
                plan[label] = nxt
            c.v2 = val
            c.plan = plan
        score = (lambda c: c.v2) if depth >= 2 else (lambda c: c.v1)
        best_v = min(score(c) for c in cands)
        ties = [c for c in cands if score(c) == best_v]
        preferred = [c for c in ties if c.call.key() == preferred_key]
        if preferred:
            choice = preferred[0]  # keep the plan when it is as good as any alternative
        else:
            rng = random.Random(int(hashlib.sha256(f"{self.seed}:{step}".encode()).hexdigest(), 16))
            choice = ties[rng.randrange(len(ties))] if len(ties) > 1 else ties[0]
        return choice, sorted(cands, key=lambda c: (score(c), c.call.key()))


def pattern_class(pat: str) -> str:
    """Recover the pattern class from the regex text (independent of the symbol)."""
    if pat.startswith(r"^\s*(?:async\s+)?(?:def|class)"):
        return "DEF"
    if pat == pattern("STAR", "x"):
        return "STAR"
    if pat.startswith(r"^\s*class\s+\w+\s*\("):
        return "SUBCLASS"
    if pat.startswith(r"\b") and pat.endswith(r"\s*\("):
        return "CALL"
    if r"|\*)" in pat:
        return "IMPORT_OR_STAR"
    return "IMPORT"


def classify_outcome(call: Call, resp, K: Seen, served_kinds: set) -> str:
    """Name the outcome class of an actual response, for plans and calibration."""
    if resp.error:
        return "missing" if call.tool == "symbols" else "error"
    if call.tool == "symbols":
        M = call.args[0]
        if resp.capped:
            return "cap"
        if served_kinds == {"outline"}:
            return "ok"
        n = call.args[1] if len(call.args) > 1 else None
        if n is None:
            return "def"
        bs = K.bindings(M, n)
        if bs is None or bs == []:
            return "star" if K.stars(M) else "none"
        if len(bs) == 1 and bs[0].kind in ("def", "class", "assign"):
            return "def"
        if len(bs) == 1:
            return "reexport"
        return "none"
    if call.tool == "ls":
        return "cap" if resp.capped else "complete"
    if call.tool == "grep":
        if resp.capped:
            return "cap"
        return "zero" if not resp.lines else "mid"
    if call.tool == "read":
        return "fits" if call.args[0] in K.all_known else "long"
    if call.tool in ("members", "calls"):
        return "cap" if resp.capped else "ok"
    return "ok"
