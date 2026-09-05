"""Verification of a trace.

- replay: re-run the policy over the logged responses; every typed output, every
  hedge and every thought must be identical.
- world: every fact re-derived against the snapshot and the index; every
  resolution the agent could state compared with the oracle; every verdict of a
  universal claim compared with the oracle's membership; the final answer
  compared with the oracle's answer (a proposed patch is applied to an in-memory
  copy and the snapshot re-indexed).
- hedges: each hedge word's band contains the exact probability it stands for.
- adherence and calibration, as before.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction

from .analysis import DYNAMIC, UNKNOWN, Index, Need, Target, exports, resolve_name
from .knowledge import Seen
from .obligations import Chain, elem_key
from .render import hedge_band
from .runner import ReplaySource, make_goal, run, seed_task_knowledge, task_names
from .snapshot import Call, Response, Snapshot


def replay(trace: dict, prior) -> dict:
    src = ReplaySource(trace["steps"])
    try:
        t2 = run(trace["task"], src, prior, trace["seed"], trace["budget"], depth=trace.get("depth", 2))
    except RuntimeError as e:
        return {"ok": False, "detail": str(e)}
    if len(t2["steps"]) != len(trace["steps"]):
        return {"ok": False, "detail": f"step count {len(t2['steps'])} vs {len(trace['steps'])}"}
    for a, b in zip(trace["steps"], t2["steps"]):
        for k in ("thought", "hedges", "choice", "forecast", "plan", "candidates", "items", "outcome", "facts"):
            if a[k] != b[k]:
                return {"ok": False, "detail": f"step {a['step']} field {k} differs"}
    if t2["answer"] != trace["answer"] or t2["final_thought"] != trace["final_thought"]:
        return {"ok": False, "detail": "answer or final thought differs"}
    return {"ok": True, "detail": "bit-identical replay"}


class PatchedSnapshot(Snapshot):
    """A snapshot with one file's text replaced in memory."""

    def __init__(self, base: Snapshot, path: str, text: str):
        self.root = base.root
        self.name = base.name
        self.files = base.files
        self.fileset = base.fileset
        self.dirs = base.dirs
        self.py_files = base.py_files
        self._patched = {path: text}
        self._base = base

    def text(self, rel: str) -> str:
        return self._patched.get(rel) or self._base.text(rel)

    def lines(self, rel: str):
        return tuple(self.text(rel).split("\n"))


def oracle_outputs(task, index: Index, answer):
    """Oracle output for every step of the chain, given the (agent's) resolve output as the target."""
    outs = []
    target = None
    for i, st in enumerate(task["chain"]):
        op = st["op"]
        if op == "resolve":
            target = index.resolve(st["module"], st["name"])
            outs.append(target.to_json())
            continue
        if target is None:
            target = Target("def", st["def_path"], int(st["def_line"]), st["name"], st.get("def_kind", ""))
        if op == "importers":
            outs.append(sorted((f"{p}:{ln}" for p, ln, _, _ in index.importers_of(target)), key=elem_key))
        elif op == "subclasses":
            outs.append(sorted((f"{p}:{ln}:{c}" for p, ln, c in index.subclasses_of(target)), key=elem_key))
        elif op == "callers":
            outs.append(sorted((f"{p}:{ln}" for p, ln in index.callers_of(target)), key=elem_key))
        elif op == "not_overriding":
            subs = index.subclasses_of(target)
            m = st["method"]
            outs.append(sorted((f"{p}:{ln}:{c}" for p, ln, c in subs if not any(mem.kind == "def" and mem.name == m for mem in index.members_of(p, c))), key=elem_key))
        elif op == "expose":
            outs.append({"package": st["package"], "target": target.to_json()})
    return outs


def check_patch(snap, index, package, name, target_json, patch) -> tuple:
    """Apply the proposed patch in memory, re-index, and check the claim."""
    if not patch or patch.get("path") != package:
        return False, "no patch or wrong file"
    text = snap.text(package)
    new_text = text + ("" if text.endswith("\n") else "\n") + patch["append"] + "\n"
    ps = PatchedSnapshot(snap, package, new_text)
    ix2 = Index(ps)
    r = ix2.resolve(package, name)
    ok = r.to_json() == target_json
    return ok, f"after patch `{name}` in `{package}` resolves to {r}"


def world_check(trace: dict, snap, index) -> dict:
    results = []

    def rec(ok, what, detail=""):
        results.append({"ok": bool(ok), "what": what, "detail": detail})

    for st in trace["steps"]:
        call = Call(st["call"]["tool"], tuple(st["call"]["args"]))
        logged = Response.from_json(st["response"])
        truth = snap.call(call, capped=True)
        rec(truth.to_json() == logged.to_json(), f"step {st['step']} response reproduces", str(call))
        for f in st["facts"]:
            k = f["kind"]
            if k == "listing":
                true = snap.children(f["dir"])
                if f["complete"]:
                    rec(list(true) == f["entries"], f"step {st['step']} listing complete", f["dir"])
                else:
                    rec(true[: len(f["entries"])] == f["entries"] and len(true) > len(f["entries"]), f"step {st['step']} listing prefix", f["dir"])
            elif k == "grep":
                true = snap.call(Call("grep", (f["pattern"], f["scope"])), capped=False)
                th = [[p, int(l)] for p, l, _ in (x.split(":", 2) for x in true.lines)]
                if f["capped"]:
                    rec(th[: len(f["hits"])] == f["hits"] and len(th) > len(f["hits"]), f"step {st['step']} capped grep is a strict prefix", f["scope"])
                else:
                    rec(th == f["hits"], f"step {st['step']} uncapped grep is exhaustive", f["scope"])
            elif k == "outline":
                mi = index.modules.get(f["path"])
                hdr = f["header"]
                ok = mi is not None and hdr["dynamic"] == mi.dynamic
                if mi is not None:
                    st_all = "none" if mi.all_names is None else ("dynamic" if mi.all_names == DYNAMIC else "static")
                    ok = ok and hdr["all_status"] == st_all
                    if f["complete"]:
                        filt = f["filter"]
                        want = [b for b in mi.all_bindings if filt is None or b.kind == "star" or b.name == filt or b.src_name == filt
                                or (b.kind == "class" and any(x.split(".")[-1] == filt for x in b.bases))]
                        got = f["bindings"]
                        ok = ok and sorted((b.line, b.name, b.kind) for b in want) == sorted((b["line"], b["name"], b["kind"]) for b in got)
                rec(ok, f"step {st['step']} outline matches the analyzer", f["path"])
            elif k == "all_names":
                mi = index.modules.get(f["path"])
                rec(mi is not None and mi.all_names == f["value"], f"step {st['step']} __all__ matches the analyzer", f["path"])
            elif k == "members":
                want = sorted((m.line, m.kind, m.name) for m in index.members_of(f["path"], f["cls"]))
                if f["complete"]:
                    rec(want == sorted(tuple(e) for e in f["entries"]), f"step {st['step']} members match the analyzer", f"{f['path']}:{f['cls']}")
            elif k == "calls":
                mi = index.modules.get(f["path"])
                want = [] if mi is None else mi.calls.get(f["name"], [])
                if f["complete"]:
                    rec(want == f["lines"], f"step {st['step']} call sites match the analyzer", f"{f['path']}:{f['name']}")
                if f.get("count") is not None:
                    rec(len(want) == f["count"], f"step {st['step']} call count matches", f"{f['path']}:{f['name']}")
            elif k == "error":
                if f.get("missing"):
                    rec(not (snap.is_file(f["missing"]) or snap.is_dir(f["missing"])), f"step {st['step']} missing path really is missing", f["missing"])
    # derived claims: rebuild knowledge; compare every statable resolution / module path / export with the oracle
    K = Seen(task_names(trace["task"]))
    seed_task_knowledge(K, trace["task"])
    for st in trace["steps"]:
        K.absorb(st["step"], Call(st["call"]["tool"], tuple(st["call"]["args"])), Response.from_json(st["response"]))
    n_res = 0
    for (m, n) in sorted(K.closure):
        r = resolve_name(K, m, n)
        if isinstance(r, Need):
            continue
        n_res += 1
        o = index.resolve(m, n)
        rec(r.key() == o.key(), "agent resolution agrees with oracle", f"{m}:{n} -> {r} (oracle {o})")
    for p, lines in K.stmts.items():
        for ln, bs in lines.items():
            for b in bs:
                if b.kind in ("from", "import"):
                    mp = K.module_path(b.src, p)
                    if mp is UNKNOWN:
                        continue
                    rec(mp == index.module_path(b.src, p), "module path agrees with oracle", f"{b.src} from {p}: {mp}")
                if b.kind == "from" and b.src_name:
                    mp = K.module_path(b.src, p)
                    if mp in (UNKNOWN, None):
                        continue
                    ex = exports(K, mp, b.src_name)
                    if not isinstance(ex, Need):
                        rec(ex == exports(index, mp, b.src_name), "export claim agrees with oracle", f"{mp} exports {b.src_name}: {ex}")
    # hedges
    for st in trace["steps"]:
        for h in st.get("hedges", []):
            band = hedge_band(h["word"])
            p = Fraction(*h["p"])
            rec(band is not None and ((band[0] < p <= band[1]) or (p == 0 and band[0] == 0)), f"step {st['step']} hedge word matches its probability", f"{h['word']} for {float(p):.2f}")
    # answer and verdicts
    t = trace["task"]
    ans = trace["answer"]
    if trace["stopped"] == "certificate" and ans and not ans.get("stuck"):
        oracle = oracle_outputs(t, index, ans)
        for i, (st, o) in enumerate(zip(ans["steps"], oracle)):
            if st["op"] == "expose":
                ok, detail = check_patch(snap, index, o["package"], o["target"]["name"], o["target"], (st["output"] or {}).get("patch"))
                rec(ok, "proposed patch verified by re-indexing", detail)
            else:
                rec(st["output"] == o, f"final {st['op']} output equals the oracle", f"{len(st['output']) if isinstance(st['output'], list) else st['output']} vs {len(o) if isinstance(o, list) else o}")
        # verdict rows of universal claims
        goal = make_goal(t)
        goal.open_items(K)
        for op, o in zip(goal.ops, oracle):
            if op.kind in ("importers", "subclasses", "callers", "not_overriding"):
                truth = set(o)
                for row in op.table(K):
                    m, key, v, reason = row
                    if v == "in":
                        rec(key in truth if op.kind != "not_overriding" else f"{[c for c in op.classes if c[0] == m and c[2] == key][0][0]}:{[c for c in op.classes if c[0] == m and c[2] == key][0][1]}:{key}" in truth, f"{op.kind} verdict `in` agrees with oracle", f"{key}: {reason}")
                    elif v == "out":
                        if op.kind == "callers" and key == m:
                            rec(not any(x.startswith(m + ":") for x in truth), "callers module ruled out agrees with oracle", f"{m}: {reason}")
                        elif op.kind == "not_overriding":
                            rec(not any(x.endswith(":" + key) and x.startswith(m + ":") for x in truth), "not_overriding verdict `out` agrees with oracle", f"{m}:{key}: {reason}")
                        else:
                            rec(key not in truth, f"{op.kind} verdict `out` agrees with oracle", f"{key}: {reason}")
    n_ok = sum(1 for r in results if r["ok"])
    return {"ok": n_ok == len(results), "n_checks": len(results), "n_ok": n_ok, "failures": [r for r in results if not r["ok"]][:20], "n_resolutions": n_res}


def adherence_stats(trace: dict) -> dict:
    c = defaultdict(int)
    for st in trace["steps"]:
        a = st.get("adherence")
        c["first" if a is None else a["status"]] += 1
    return dict(c)


def calibration(traces: list, bins=5) -> list:
    rows = defaultdict(lambda: [Fraction(0), 0, 0])
    for tr in traces:
        for st in tr["steps"]:
            for l, p in st["forecast"].items():
                p = Fraction(*p)
                b = min(bins - 1, int(float(p) * bins))
                rows[b][0] += p
                rows[b][1] += 1
                rows[b][2] += 1 if st["outcome"] == l else 0
    out = []
    for b in sorted(rows):
        s, n, h = rows[b]
        out.append({"bin": f"{b / bins:.1f}-{(b + 1) / bins:.1f}", "n": n, "mean_forecast": float(s / n), "realized": h / n})
    return out
