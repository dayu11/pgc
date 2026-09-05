"""Task generation with full access: candidates, skeletons, quotas, floors."""
from __future__ import annotations

import hashlib
import random
from collections import defaultdict

from .analysis import Index, Target, exports
from .prior import pattern
from .snapshot import CAPS, Snapshot

SEMANTICS = ("A module is a .py file; source roots are the repository root and, if present, src/ and lib/. "
             "`from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the "
             "single star-import source of M that exports N. A module exports N if its literal __all__ lists N or, without "
             "__all__, if N is public and bound in it. Multiple bindings, non-literal __all__, external star imports and "
             "dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.")


def bucket(n, edges):
    for i, e in enumerate(edges):
        if n <= e:
            return str(e) if i == 0 or edges[i - 1] + 1 == e else f"{edges[i - 1] + 1}-{e}"
    return f"{edges[-1] + 1}+"


def resolve_candidates(name: str, snap: Snapshot, ix: Index):
    out = []
    for p, mi in sorted(ix.modules.items()):
        if mi.parse_error or mi.dynamic:
            continue
        for b in mi.all_bindings:
            if b.kind != "from":
                continue
            if len(mi.bindings(b.name)) != 1 or b.src_name.startswith("_"):
                continue
            tgt = ix.resolve(p, b.name)
            if tgt.kind != "def":
                continue
            chain = ix.chain(p, b.name)
            hops = len([h for h in chain if h[0] != "*"])
            if hops < 2:
                continue
            star_checks = resolve_star_checks(ix, chain)
            star = any(h[0] == "*" for h in chain)
            alias = b.name != b.src_name
            decoys = len(ix.defs_named(tgt.name)) - 1
            skel = {"family": "resolve", "hops": bucket(hops, [2, 3]), "star": star, "alias": alias,
                    "decoys": bucket(decoys, [0, 1]), "relative": b.src.startswith("."), "from_init": mi.is_init}
            floor = hops + star_checks
            asp = f" as `{b.name}`" if alias else ""
            text = (f"In `{p}`, line {b.line} imports `{b.src_name}` from `{b.src}`{asp}. Under the declared semantics, which "
                    f"definition does the module-level name `{b.name}` bound by this statement resolve to? Answer with `path:line`.")
            out.append({"family": "resolve", "repo": name, "text": text, "semantics": SEMANTICS,
                        "given": {"module": p, "line": b.line, "name": b.name, "spec": b.src, "src_name": b.src_name},
                        "oracle": {"target": tgt.to_json(), "hops": hops, "chain": [list(h) for h in chain]},
                        "skeleton": skel, "floor": floor})
    return out


def resolve_star_checks(ix, chain):
    """Later star imports on each hop module must be checked for exporting the name:
    one outline each, plus one read when the source has a literal __all__."""
    n = 0
    for h in chain:
        if h[0] == "*":
            continue
        m, name = h
        mi = ix.modules.get(m)
        if mi is None:
            continue
        bs = mi.bindings(name)
        line = bs[0].line if len(bs) == 1 else None
        for s_ in mi.stars:
            if line is not None and s_.line < line:
                continue
            mp = ix.module_path(s_.src, m)
            if mp is None:
                continue
            n += 1
            if isinstance(ix.modules[mp].all_names, list):
                n += 1
    return n


INFEASIBLE = 10 ** 6


def cover_floor(snap, ix, tgt: Target, imps):
    from .snapshot import Call

    def count(pc, scope):
        return len(snap.call(Call("grep", (pattern(pc, tgt.name), scope)), capped=False).lines)

    def cov(pc, scope):
        if count(pc, scope) <= CAPS["grep"]:
            return 1
        children = snap.children(scope)
        if len(children) > CAPS["ls"]:
            return INFEASIBLE  # a capped listing cannot be split, so completeness cannot be certified
        total = 1  # a listing to split
        for e in children:
            full = e if scope == "." else f"{scope}/{e}"
            if e.endswith("/"):
                total += cov(pc, full[:-1])
            elif e.endswith(".py"):
                total += cov(pc, full)
        return total

    n_both = count("IMPORT_OR_STAR", ".")
    greps = 1 if n_both <= CAPS["grep"] else cov("IMPORT", ".") + cov("STAR", ".")
    # candidate modules: every module with a matching line needs one outline
    lines = snap.call(Call("grep", (pattern("IMPORT_OR_STAR", tgt.name), ".")), capped=False).lines
    mods = {l.split(":", 1)[0] for l in lines if l.split(":", 1)[0].endswith(".py")}
    # sources to resolve: every module some candidate imports the name from (targets and decoys)
    sources = set()
    for p in mods:
        mi = ix.modules.get(p)
        if mi is None:
            continue
        for b in mi.all_bindings:
            if (b.kind == "from" and b.src_name == tgt.name) or b.kind == "star":
                mp = ix.module_path(b.src, p)
                if mp:
                    sources.add(mp)
    decoy_sources = {mp for mp in sources if ix.resolve(mp, tgt.name).key() != tgt.key()}
    return greps + len(mods) + len(sources - mods), n_both > CAPS["grep"], len(decoy_sources)


def cover_candidates(name: str, snap: Snapshot, ix: Index):
    out = []
    seen_targets = set()
    for p, mi in sorted(ix.modules.items()):
        if mi.parse_error or mi.dynamic:
            continue
        for b in mi.all_bindings:
            if b.kind not in ("class", "def") or b.name.startswith("_"):
                continue
            if len(ix.from_imports_of_name(b.name)) < 2:
                continue
            tgt = ix.resolve(p, b.name)
            if tgt.kind != "def" or tgt.key() in seen_targets:
                continue
            seen_targets.add(tgt.key())
            imps = ix.importers_of(tgt)
            if not (3 <= len(imps) <= 60):
                continue
            dirs = {q.rsplit("/", 1)[0] for q, _, _, _ in imps}
            if len(dirs) < 2:
                continue
            floor, root_caps, n_decoy_src = cover_floor(snap, ix, tgt, imps)
            star = any(k == "star" for _, _, k, _ in imps)
            n_sources = len({ix.module_path(bb.src, q) for q, ln, k, _ in imps for bb in ix.modules[q].all_bindings if bb.line == ln and bb.kind in ("from", "star")})
            skel = {"family": "cover", "importers": bucket(len(imps), [5, 12]), "sources": bucket(n_sources, [1, 3]),
                    "star": star, "decoy_sources": bucket(n_decoy_src, [0, 1]), "root_caps": root_caps}
            text = (f"`{tgt.name}` is defined at `{tgt.path}:{tgt.line}` ({b.kind}). List every module-level import statement in the "
                    f"snapshot that imports this definition: `from ... import` statements naming it (directly or with `as`), and star "
                    f"imports of modules that export it. Answer as `path:line` entries.")
            out.append({"family": "cover", "repo": name, "text": text, "semantics": SEMANTICS,
                        "given": {"def_path": tgt.path, "def_line": tgt.line, "name": tgt.name, "def_kind": b.kind},
                        "oracle": {"statements": [f"{q}:{ln}" for q, ln, _, _ in imps], "count": len(imps)},
                        "skeleton": skel, "floor": floor})
    return out


def composite_candidates(name, snap, ix, resolves, covers):
    by_target = {tuple(c["oracle"]["statements"]) and (c["given"]["def_path"], c["given"]["def_line"]): c for c in covers}
    out = []
    for r in resolves:
        t = r["oracle"]["target"]
        c = by_target.get((t["path"], t["line"]))
        if c is None:
            continue
        text = r["text"] + " Then list every module-level import statement in the snapshot that imports that definition (from-imports naming it, directly or with `as`, and star imports of modules that export it), as `path:line` entries."
        skel = {"family": "composite", **{k: v for k, v in r["skeleton"].items() if k != "family"}, "importers": c["skeleton"]["importers"], "root_caps": c["skeleton"]["root_caps"]}
        out.append({"family": "composite", "repo": name, "text": text, "semantics": SEMANTICS, "given": dict(r["given"]),
                    "oracle": {"target": t, "statements": c["oracle"]["statements"], "count": c["oracle"]["count"]},
                    "skeleton": skel, "floor": r["floor"] + c["floor"]})
    return out


def skeleton_key(skel: dict) -> str:
    return "|".join(f"{k}={skel[k]}" for k in sorted(skel))


def select_tasks(cands: list, per_repo: int, seed: int, family_quota: dict = None) -> list:
    """One task per skeleton cell per repository, families balanced, deterministic."""
    rng = random.Random(seed)
    by_cell = defaultdict(list)
    for c in cands:
        by_cell[skeleton_key(c["skeleton"])].append(c)
    cells = sorted(by_cell)
    rng.shuffle(cells)
    chosen = []
    fam_count = defaultdict(int)
    quota = family_quota or {"resolve": per_repo // 3 + 1, "cover": per_repo // 3 + 1, "composite": per_repo // 3 + 1}
    for cell in cells:
        c = rng.choice(sorted(by_cell[cell], key=lambda x: x["text"]))
        if fam_count[c["family"]] >= quota.get(c["family"], 0):
            continue
        fam_count[c["family"]] += 1
        chosen.append(c)
        if len(chosen) >= per_repo:
            break
    for c in chosen:
        c["id"] = f"{c['repo']}-{c['family']}-" + hashlib.sha256(c["text"].encode()).hexdigest()[:8]
        c["cell"] = skeleton_key(c["skeleton"])
    return sorted(chosen, key=lambda c: c["id"])


def generate(name: str, snap: Snapshot, ix: Index, per_repo: int, seed: int, max_floor: int = 30) -> dict:
    res = resolve_candidates(name, snap, ix)
    cov = cover_candidates(name, snap, ix)
    comp = composite_candidates(name, snap, ix, res, cov)
    pool = [c for c in res + cov + comp if c["floor"] <= max_floor]
    chosen = select_tasks(pool, per_repo, seed)
    cells = {skeleton_key(c["skeleton"]) for c in pool}
    return {"chosen": chosen, "pool_size": {"resolve": len(res), "cover": len(cov), "composite": len(comp)}, "pool_cells": len(cells)}
