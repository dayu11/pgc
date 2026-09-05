"""Priors fit on held-out repositories, stored as exact rationals.

Everything the policy believes about unseen parts of a repository comes from
here. Labels are free: the tools are deterministic, so the fitter runs them
uncapped on the training repositories and counts.
"""
from __future__ import annotations

import hashlib
import json
import random
from fractions import Fraction

from .analysis import Index
from .snapshot import CAPS, Call, Snapshot

PATTERN_CLASSES = ("DEF", "IMPORT", "STAR", "IMPORT_OR_STAR")


def pattern(pclass: str, name: str) -> str:
    n = name
    if pclass == "DEF":
        return rf"^\s*(?:async\s+)?(?:def|class)\s+{n}\b"
    cont = rf"^\s*(?:\w+(?:\s+as\s+\w+)?\s*,\s*)*{n}\b(?:\s+as\s+\w+)?\s*,?\s*\)?\s*$"
    if pclass == "IMPORT":
        return rf"^\s*from\s+\S+\s+import\s+.*\b{n}\b|{cont}"
    if pclass == "STAR":
        return r"^\s*from\s+\S+\s+import\s+\*"
    if pclass == "IMPORT_OR_STAR":
        return rf"^\s*from\s+\S+\s+import\s+(?:.*\b{n}\b|\*)|{cont}"
    raise KeyError(pclass)


def scope_kind(scope: str, is_file: bool) -> str:
    if is_file:
        return "file"
    if scope == ".":
        return "root"
    return "dir1" if "/" not in scope else "dir2"


def depth_kind(d: str) -> str:
    if d == ".":
        return "root"
    return "dir1" if "/" not in d else "dir2"


class Counter2:
    """Counts with Laplace smoothing, serialised as exact fractions."""

    def __init__(self, labels):
        self.labels = list(labels)
        self.n = {l: 0 for l in self.labels}

    def add(self, label, k=1):
        self.n[label] += k

    def dist(self):
        tot = sum(self.n.values()) + len(self.labels)
        return {l: Fraction(self.n[l] + 1, tot) for l in self.labels}


def fit_prior(repos: dict, exclude: str, seed: int = 0, samples_per_repo: int = 120) -> dict:
    """repos: name -> (Snapshot, Index). Fit on every repo except `exclude`."""
    rng = random.Random(seed)
    grep = {(pc, sk): Counter2(("zero", "mid", "cap")) for pc in PATTERN_CLASSES for sk in ("root", "dir1", "dir2", "file")}
    grep_mid_hits = {(pc, sk): [0, 0] for pc in PATTERN_CLASSES for sk in ("root", "dir1", "dir2", "file")}
    hop = {"init": Counter2(("def", "reexport", "star", "none")), "mod": Counter2(("def", "reexport", "star", "none"))}
    symcap = {"init": Counter2(("fits", "cap")), "mod": Counter2(("fits", "cap"))}
    allstat = {"init": Counter2(("none", "static", "dynamic")), "mod": Counter2(("none", "static", "dynamic"))}
    lscap = {k: Counter2(("fits", "cap")) for k in ("root", "dir1", "dir2")}
    children = {k: [0, 0] for k in ("root", "dir1", "dir2")}  # [sum, count]
    allfit = Counter2(("fits", "long"))
    src_new = Counter2(("new", "known"))
    decoy = Counter2(("target", "other"))
    src_form = Counter2(("module", "package"))
    abs_ext = Counter2(("external", "internal"))
    training = []
    for name, (snap, ix) in sorted(repos.items()):
        if name == exclude:
            continue
        training.append(name)
        # directories
        for d in sorted(snap.dirs):
            ch = snap.children(d)
            k = depth_kind(d)
            lscap[k].add("cap" if len(ch) > CAPS["ls"] else "fits")
            children[k][0] += len([c for c in ch if c.endswith("/") or c.endswith(".py")])
            children[k][1] += 1
        # modules
        for p, mi in sorted(ix.modules.items()):
            t = "init" if mi.is_init else "mod"
            symcap[t].add("cap" if len(mi.all_bindings) + 1 > CAPS["symbols"] else "fits")
            allstat[t].add("none" if mi.all_names is None else ("dynamic" if mi.all_names == "DYNAMIC" else "static"))
            if isinstance(mi.all_names, list):
                lines = [b.line for b in mi.all_bindings if b.name == "__all__"]
                start = min(lines)
                # how many lines does the literal span?
                txt = snap.lines(p)
                depth = 0
                span = 0
                for i in range(start - 1, len(txt)):
                    span += 1
                    depth += txt[i].count("[") + txt[i].count("(") - txt[i].count("]") - txt[i].count(")")
                    if depth <= 0 and i >= start - 1:
                        break
                allfit.add("fits" if span <= 30 else "long")
        # hops: for from-bindings, what kind of binding sits at the source
        froms = [b for mi in ix.modules.values() for b in mi.all_bindings if b.kind == "from"]
        rng.shuffle(froms)
        for b in froms[:samples_per_repo * 3]:
            mp = ix.module_path(b.src, b.module)
            if not b.src.startswith("."):
                abs_ext.add("external" if mp is None else "internal")
            if mp is None:
                continue
            smi = ix.modules.get(mp)
            if smi is None:
                continue
            src_form.add("package" if smi.is_init else "module")
            t = "init" if smi.is_init else "mod"
            bs = smi.bindings(b.src_name)
            if len(bs) == 1 and bs[0].kind in ("def", "class", "assign"):
                hop[t].add("def")
            elif len(bs) == 1 and bs[0].kind in ("from", "import"):
                hop[t].add("reexport")
            elif not bs and smi.stars:
                hop[t].add("star")
            else:
                hop[t].add("none")
        # grep outcome distributions over sampled names and scopes
        names = sorted({b.name for mi in ix.modules.values() for b in mi.all_bindings if b.kind in ("def", "class") and not b.name.startswith("_")})
        rng.shuffle(names)
        dirs = sorted(snap.dirs)
        for n in names[:samples_per_repo]:
            for pc in PATTERN_CLASSES:
                for sc in rng.sample(dirs, min(3, len(dirs))) + [rng.choice(snap.py_files)]:
                    r = snap.call(Call("grep", (pattern(pc, n), sc)), capped=False)
                    k = (pc, scope_kind(sc, snap.is_file(sc)))
                    cnt = len(r.lines)
                    if cnt == 0:
                        grep[k].add("zero")
                    elif cnt > CAPS["grep"]:
                        grep[k].add("cap")
                    else:
                        grep[k].add("mid")
                        grep_mid_hits[k][0] += cnt
                        grep_mid_hits[k][1] += 1
        # importer statistics: are import sources new, are they decoys
        defs = [(p, b) for p, mi in ix.modules.items() for b in mi.all_bindings if b.kind == "class"]
        rng.shuffle(defs)
        for p, b in defs[:40]:
            tgt = ix.resolve(p, b.name)
            if tgt.kind != "def":
                continue
            seen_src = set()
            for q, mi in ix.modules.items():
                for fb in mi.all_bindings:
                    if fb.kind == "from" and fb.src_name == b.name:
                        mp = ix.module_path(fb.src, q)
                        if mp is None:
                            continue
                        src_new.add("known" if mp in seen_src else "new")
                        seen_src.add(mp)
                        decoy.add("target" if ix.resolve(mp, fb.src_name).key() == tgt.key() else "other")

    def fr(x):
        return [x.numerator, x.denominator]

    theta = {
        "training_repos": training,
        "grep": {f"{pc}|{sk}": {l: fr(v) for l, v in c.dist().items()} for (pc, sk), c in grep.items()},
        "grep_mid_hits": {f"{pc}|{sk}": fr(Fraction(s, max(1, m))) if m else fr(Fraction(3)) for (pc, sk), (s, m) in grep_mid_hits.items()},
        "hop": {t: {l: fr(v) for l, v in c.dist().items()} for t, c in hop.items()},
        "symcap": {t: {l: fr(v) for l, v in c.dist().items()} for t, c in symcap.items()},
        "allstat": {t: {l: fr(v) for l, v in c.dist().items()} for t, c in allstat.items()},
        "lscap": {k: {l: fr(v) for l, v in c.dist().items()} for k, c in lscap.items()},
        "children": {k: fr(Fraction(s, max(1, m))) for k, (s, m) in children.items()},
        "allfit": {l: fr(v) for l, v in allfit.dist().items()},
        "src_new": {l: fr(v) for l, v in src_new.dist().items()},
        "decoy": {l: fr(v) for l, v in decoy.dist().items()},
        "src_form": {l: fr(v) for l, v in src_form.dist().items()},
        "abs_ext": {l: fr(v) for l, v in abs_ext.dist().items()},
    }
    theta["hash"] = hashlib.sha256(json.dumps(theta, sort_keys=True).encode()).hexdigest()[:16]
    return theta


class Prior:
    """Typed access to a fitted theta, as Fractions."""

    def __init__(self, theta: dict):
        self.theta = theta
        self.hash = theta["hash"]

    @staticmethod
    def _f(x):
        return Fraction(x[0], x[1])

    def grep(self, pclass, skind):
        d = self.theta["grep"][f"{pclass}|{skind}"]
        return {k: self._f(v) for k, v in d.items()}

    def grep_mid_hits(self, pclass, skind):
        return self._f(self.theta["grep_mid_hits"][f"{pclass}|{skind}"])

    def hop(self, mtype):
        return {k: self._f(v) for k, v in self.theta["hop"][mtype].items()}

    def symcap(self, mtype):
        return self._f(self.theta["symcap"][mtype]["cap"])

    def allstat(self, mtype):
        return {k: self._f(v) for k, v in self.theta["allstat"][mtype].items()}

    def lscap(self, dkind):
        return self._f(self.theta["lscap"][dkind]["cap"])

    def children(self, dkind):
        return self._f(self.theta["children"][dkind])

    def allfit(self):
        return self._f(self.theta["allfit"]["fits"])

    def src_new(self):
        return self._f(self.theta["src_new"]["new"])

    def decoy(self):
        return self._f(self.theta["decoy"]["other"])

    def src_is_package(self):
        return self._f(self.theta["src_form"]["package"])

    def abs_external(self):
        return self._f(self.theta["abs_ext"]["external"])
