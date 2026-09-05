"""Task generation with full access, by composing operations.

Operations and their types:
    resolve(module, name) -> target
    importers(target) -> [statement]     subclasses(target) -> [class]     callers(target) -> [call site]
    not_overriding([class], method) -> [class]                          expose(target, package) -> patch

Chains are composed under those types. Every chain gets an oracle answer per step,
a skeleton cell for diversity quotas, and an omniscient-floor estimate. Tasks whose
answer touches unsupported behaviour, private names, or uncertifiable coverage are
never generated.
"""
from __future__ import annotations

import hashlib
import random
from collections import defaultdict

from .analysis import Index, Target, exports
from .obligations import elem_key
from .prior import pattern
from .snapshot import CAPS, Call, Snapshot

SEMANTICS = ("A module is a .py file; source roots are the repository root and, if present, src/ and lib/. "
             "`from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the "
             "single star-import source of M that exports N; bindings take effect in source order. A module exports N if its "
             "literal __all__ lists N or, without __all__, if N is public and bound in it. A class derives from a definition "
             "when a base written as a bare name or `module.Name` resolves to it. A call site is `name(...)` where the bare name "
             "refers to the module-level binding (not a parameter or local). Multiple bindings, non-literal __all__, external "
             "star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.")

INFEASIBLE = 10 ** 6


def bucket(n, edges):
    for i, e in enumerate(edges):
        if n <= e:
            return str(e) if i == 0 or edges[i - 1] + 1 == e else f"{edges[i - 1] + 1}-{e}"
    return f"{edges[-1] + 1}+"


# ---------------------------------------------------------------- floors

def cover_cost(snap, name, pc):
    """Calls an omniscient agent needs to cover the tree for a pattern class, or INFEASIBLE."""

    def count(scope):
        return len(snap.call(Call("grep", (pattern(pc, name), scope)), capped=False).lines)

    def cov(scope):
        if count(scope) <= CAPS["grep"]:
            return 1
        children = snap.children(scope)
        if len(children) > CAPS["ls"]:
            return INFEASIBLE
        total = 1
        for e in children:
            full = e if scope == "." else f"{scope}/{e}"
            if e.endswith("/"):
                total += cov(full[:-1])
            elif e.endswith(".py"):
                total += cov(full)
        return min(total, INFEASIBLE)

    return cov(".")


def candidate_modules(snap, name, classes):
    mods = set()
    for pc in classes:
        for l in snap.call(Call("grep", (pattern(pc, name), ".")), capped=False).lines:
            p = l.split(":", 1)[0]
            if p.endswith(".py"):
                mods.add(p)
    return sorted(mods)


def star_checks(ix, chain):
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


# ---------------------------------------------------------------- per-operation candidates

def resolve_steps(name, snap, ix):
    """Resolve steps with at least one re-export hop and a definition as target."""
    out = []
    for p, mi in sorted(ix.modules.items()):
        if mi.parse_error or mi.dynamic:
            continue
        for b in mi.all_bindings:
            if b.kind != "from" or len(mi.bindings(b.name)) != 1 or b.src_name.startswith("_"):
                continue
            tgt = ix.resolve(p, b.name)
            if tgt.kind != "def":
                continue
            chain = ix.chain(p, b.name)
            hops = len([h for h in chain if h[0] != "*"])
            if hops < 2:
                continue
            decoys = len(ix.defs_named(tgt.name)) - 1
            out.append({
                "step": {"op": "resolve", "module": p, "line": b.line, "name": b.name, "spec": b.src, "src_name": b.src_name},
                "target": tgt, "floor": hops + star_checks(ix, chain),
                "skel": {"hops": bucket(hops, [2, 3]), "star": any(h[0] == "*" for h in chain), "alias": b.name != b.src_name,
                         "decoys": bucket(decoys, [0, 1]), "relative": b.src.startswith(".")},
                "text": (f"In `{p}` line {b.line}, `{b.src_name}` is imported from `{b.src}`" + (f" as `{b.name}`" if b.name != b.src_name else "")
                         + f". Which definition does the module-level name `{b.name}` actually refer to? Give `path:line`."),
            })
    return out


def target_stats(snap, ix, tgt: Target, kind: str):
    """Everything the setter needs to decide which operations a target supports."""
    st = {}
    # importers
    imps = ix.importers_of(tgt)
    if 3 <= len(imps) <= 60 and len({q.rsplit("/", 1)[0] for q, _, _, _ in imps}) >= 2:
        cov = min(cover_cost(snap, tgt.name, "IMPORT") + cover_cost(snap, tgt.name, "STAR"), cover_cost(snap, tgt.name, "IMPORT_OR_STAR"))
        if cov < INFEASIBLE:
            mods = candidate_modules(snap, tgt.name, ("IMPORT", "STAR"))
            sources = set()
            for p in mods:
                for b in ix.modules[p].all_bindings:
                    if (b.kind == "from" and b.src_name == tgt.name) or b.kind == "star":
                        mp = ix.module_path(b.src, p)
                        if mp:
                            sources.add(mp)
            decoy_src = {mp for mp in sources if ix.resolve(mp, tgt.name).key() != tgt.key()}
            # a star-import source with a literal __all__ costs an extra read to check the export
            star_reads = 0
            for p in mods:
                for b in ix.modules[p].all_bindings:
                    if b.kind == "star":
                        mp = ix.module_path(b.src, p)
                        if mp and isinstance(ix.modules.get(mp).all_names if mp in ix.modules else None, list):
                            star_reads += 1
            st["importers"] = {"answer": sorted((f"{q}:{ln}" for q, ln, _, _ in imps), key=elem_key), "floor": cov + len(mods) + len(sources - set(mods)) + star_reads,
                               "skel": {"importers": bucket(len(imps), [5, 12]), "star": any(k == "star" for _, _, k, _ in imps), "decoy_sources": bucket(len(decoy_src), [0, 1])}}
    if kind == "class":
        subs = ix.subclasses_of(tgt)
        if 2 <= len(subs) <= 40:
            cov = cover_cost(snap, tgt.name, "SUBCLASS")
            if cov < INFEASIBLE:
                mods = candidate_modules(snap, tgt.name, ("SUBCLASS",))
                decoys = 0
                for p in mods:
                    for b in ix.modules[p].all_bindings:
                        if b.kind == "class" and any(x.split(".")[-1] == tgt.name for x in b.bases) and (p, b.line, b.name) not in subs:
                            decoys += 1
                st["subclasses"] = {"answer": sorted((f"{p}:{ln}:{c}" for p, ln, c in subs), key=elem_key), "floor": cov + len(mods) + len({p for p, _, _ in subs}),
                                    "skel": {"subclasses": bucket(len(subs), [3, 8]), "decoy_classes": bucket(decoys, [0, 1])}}
                # a method some subclasses override and some do not
                methods = [m.name for m in ix.members_of(tgt.path, tgt.name) if m.kind == "def" and not m.name.startswith("__")]
                best = None
                for m in methods:
                    lacking = [f"{p}:{ln}:{c}" for p, ln, c in subs if not any(mm.kind == "def" and mm.name == m for mm in ix.members_of(p, c))]
                    if 0 < len(lacking) < len(subs):
                        best = (m, sorted(lacking, key=elem_key))
                        break
                if best:
                    st["not_overriding"] = {"method": best[0], "answer": best[1], "floor": len(subs), "skel": {"overriders": bucket(len(subs) - len(best[1]), [1, 3])}}
    calls = ix.callers_of(tgt)
    if 2 <= len(calls) <= 60:
        mods = candidate_modules(snap, tgt.name, ("CALL",))
        ok = all(not ix.modules[p].calls_unsure and len(ix.modules[p].calls.get(tgt.name, [])) <= CAPS["calls"] for p in mods if p in ix.modules)
        cov = cover_cost(snap, tgt.name, "CALL")
        if ok and cov < INFEASIBLE and len(mods) <= 25:
            confirmed = {p for p, _ in calls}
            st["callers"] = {"answer": sorted((f"{p}:{ln}" for p, ln in calls), key=elem_key), "floor": cov + len(mods) + len(confirmed),
                             "skel": {"call_sites": bucket(len(calls), [4, 12]), "caller_modules": bucket(len(confirmed), [1, 3]), "false_positive_modules": bucket(len(mods) - len(confirmed), [0, 2])}}
    # expose: a non-dynamic package __init__ that does not bind the name and can import it relatively
    from .obligations import Expose
    for p, mi in sorted(ix.modules.items()):
        if not mi.is_init or mi.dynamic or mi.parse_error or mi.bindings(tgt.name) or p == tgt.path:
            continue
        if any(ix.module_path(s.src, p) and exports(ix, ix.module_path(s.src, p), tgt.name) is True for s in mi.stars):
            continue
        spec = Expose(tgt, p, tgt.name).spec()
        if spec is None:
            continue
        mp = ix.module_path(spec, p)
        if mp and ix.resolve(mp, tgt.name).key() == tgt.key():
            stars = sum(1 + (1 if isinstance(ix.modules.get(ix.module_path(s_.src, p), None) and ix.modules[ix.module_path(s_.src, p)].all_names, list) else 0)
                        for s_ in mi.stars if ix.module_path(s_.src, p))
            st["expose"] = {"package": p, "floor": 2 + stars, "skel": {"package_depth": bucket(p.count("/"), [1, 2]), "star_sources": bucket(len(mi.stars), [0, 2])}}
            break
    return st


def target_text(tgt: Target, kind: str) -> str:
    return f"`{tgt.name}` is defined at `{tgt.path}:{tgt.line}` ({kind})."


OP_TEXT = {
    "importers": "list every module-level import statement in the repository that brings in that definition, including through re-exports and star imports, as `path:line`.",
    "subclasses": "list every class that derives from it directly, as `path:line:ClassName`, making sure each base name really resolves to this definition.",
    "callers": "list every call site of it: bare-name calls whose module-level binding resolves to this definition, as `path:line`.",
}


def compose_text(head: str, ops: list, stats: dict, tgt: Target) -> str:
    parts = [head]
    for i, op in enumerate(ops):
        lead = "Then" if i == 0 and head.endswith("`path:line`.") else ("Then" if i > 0 else "First,")
        if op in OP_TEXT:
            parts.append(f"{lead} {OP_TEXT[op]}")
        elif op == "not_overriding":
            parts.append(f"Among those subclasses, which do not define `{stats['not_overriding']['method']}` themselves? Same format.")
        elif op == "expose":
            pkg = stats["expose"]["package"]
            parts.append(f"{lead} propose the one-line change to `{pkg}` that makes `from {pkg.rsplit('/', 1)[0].split('/')[-1]} import {tgt.name}` resolve to this definition; give the exact line to append.")
    return " ".join(parts)


def generate(name: str, snap: Snapshot, ix: Index, per_repo: int, seed: int, max_floor: int = 32) -> dict:
    pool = []
    rsteps = resolve_steps(name, snap, ix)
    # targets: classes and functions with enough structure around them
    stats_cache = {}

    def stats_for(tgt: Target, kind: str):
        if tgt.key() not in stats_cache:
            stats_cache[tgt.key()] = target_stats(snap, ix, tgt, kind)
        return stats_cache[tgt.key()]

    def add(chain, head_text, ops, tgt, kind, base_floor, base_skel, given):
        st = stats_for(tgt, kind) if ops else {}
        if any(op not in st and op != "resolve" for op in ops):
            return
        steps = list(chain)
        floor = base_floor
        skel = dict(base_skel)
        oracle = []
        for op in ops:
            if op == "not_overriding":
                steps.append({"op": op, "method": st[op]["method"]})
                given["method"] = st[op]["method"]
            elif op == "expose":
                steps.append({"op": op, "package": st[op]["package"]})
                given["package"] = st[op]["package"]
            else:
                steps.append({"op": op})
            floor += st[op]["floor"]
            skel.update(st[op]["skel"])
            oracle.append({"op": op, **{k: v for k, v in st[op].items() if k in ("answer", "method", "package")}})
        if floor > max_floor:
            return
        family = steps[-1]["op"]
        skel["chain"] = "→".join(s["op"] for s in steps)
        text = compose_text(head_text, ops, st, tgt)
        pool.append({"family": family, "repo": name, "chain": steps, "given": given, "text": text, "semantics": SEMANTICS,
                     "oracle": {"target": tgt.to_json(), "steps": oracle}, "skeleton": skel, "floor": floor})

    for r in rsteps:
        tgt = r["target"]
        kind = next((b.kind for b in ix.modules[tgt.path].all_bindings if b.line == tgt.line and b.name == tgt.name), "def")
        given = {k: v for k, v in r["step"].items() if k != "op"}
        add([r["step"]], r["text"], [], tgt, kind, r["floor"], r["skel"], dict(given))
        for ops in (["importers"], ["subclasses"], ["subclasses", "not_overriding"], ["callers"], ["expose"]):
            add([r["step"]], r["text"], ops, tgt, kind, r["floor"], r["skel"], dict(given))
    seen_targets = set()
    for p, mi in sorted(ix.modules.items()):
        if mi.parse_error or mi.dynamic:
            continue
        for b in mi.all_bindings:
            if b.kind not in ("class", "def") or b.name.startswith("_") or len(ix.from_imports_of_name(b.name)) < 2:
                continue
            tgt = ix.resolve(p, b.name)
            if tgt.kind != "def" or tgt.key() in seen_targets:
                continue
            seen_targets.add(tgt.key())
            given = {"def_path": tgt.path, "def_line": tgt.line, "name": tgt.name, "def_kind": b.kind}
            head = target_text(tgt, b.kind)
            first = {"op": None}
            for ops in (["importers"], ["subclasses"], ["subclasses", "not_overriding"], ["callers"], ["expose"]):
                st = stats_for(tgt, b.kind)
                if ops[0] not in st:
                    continue
                chain0 = {"op": ops[0], "def_path": tgt.path, "def_line": tgt.line, "name": tgt.name, "def_kind": b.kind}
                if ops[0] == "expose":
                    chain0["package"] = st["expose"]["package"]
                add([chain0], head, ops[1:], tgt, b.kind, st[ops[0]]["floor"], dict(st[ops[0]]["skel"]), dict(given, **({"package": st["expose"]["package"]} if ops[0] == "expose" else {})))
    chosen = select_tasks(pool, per_repo, seed)
    fam_pool = defaultdict(int)
    for c in pool:
        fam_pool[c["family"]] += 1
    return {"chosen": chosen, "pool_size": dict(fam_pool), "pool_cells": len({skeleton_key(c["skeleton"]) for c in pool})}


def skeleton_key(skel: dict) -> str:
    return "|".join(f"{k}={skel[k]}" for k in sorted(skel))


def select_tasks(pool: list, per_repo: int, seed: int) -> list:
    """One task per skeleton cell per repository, families balanced, deterministic."""
    rng = random.Random(seed)
    by_cell = defaultdict(list)
    for c in pool:
        by_cell[skeleton_key(c["skeleton"])].append(c)
    cells = sorted(by_cell)
    rng.shuffle(cells)
    fams = sorted({c["family"] for c in pool})
    quota = max(1, -(-per_repo // max(1, len(fams))))
    chosen, fam_count = [], defaultdict(int)
    for cell in cells:
        c = rng.choice(sorted(by_cell[cell], key=lambda x: x["text"]))
        if fam_count[c["family"]] >= quota:
            continue
        fam_count[c["family"]] += 1
        chosen.append(c)
        if len(chosen) >= per_repo:
            break
    for c in chosen:
        c["id"] = f"{c['repo']}-{c['family']}-" + hashlib.sha256(c["text"].encode()).hexdigest()[:8]
        c["cell"] = skeleton_key(c["skeleton"])
    return sorted(chosen, key=lambda c: c["id"])
