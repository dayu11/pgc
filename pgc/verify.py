"""Verification of a trace.

- replay: re-run the policy over the logged responses; every typed output and
  every thought must be identical.
- world: every fact is re-derived against the snapshot and the index; every
  resolution the agent could state is compared with the oracle; the final
  answer is compared with the oracle's answer.
- adherence: each call is the branch the previous plan named for the realized
  outcome (or the plan was open-ended).
- calibration (across traces): forecast probability against realized frequency.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction

from .analysis import DYNAMIC, UNKNOWN, Need, exports, resolve_name
from .goals import CompositeGoal, CoverGoal, ResolveGoal
from .knowledge import Seen
from .runner import ReplaySource, make_goal, run, task_names
from .snapshot import Call, Response


def replay(trace: dict, prior) -> dict:
    src = ReplaySource(trace["steps"])
    try:
        t2 = run(trace["task"], src, prior, trace["seed"], trace["budget"], depth=trace.get("depth", 2))
    except RuntimeError as e:
        return {"ok": False, "detail": str(e)}
    if len(t2["steps"]) != len(trace["steps"]):
        return {"ok": False, "detail": f"step count {len(t2['steps'])} vs {len(trace['steps'])}"}
    for a, b in zip(trace["steps"], t2["steps"]):
        for k in ("thought", "choice", "forecast", "plan", "candidates", "items", "outcome", "facts"):
            if a[k] != b[k]:
                return {"ok": False, "detail": f"step {a['step']} field {k} differs"}
    if t2["answer"] != trace["answer"] or t2["final_thought"] != trace["final_thought"]:
        return {"ok": False, "detail": "answer or final thought differs"}
    return {"ok": True, "detail": "bit-identical replay"}


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
                        want = [b for b in mi.all_bindings if f["filter"] is None or b.kind == "star" or b.name == f["filter"] or b.src_name == f["filter"]]
                        got = f["bindings"]
                        ok = ok and sorted((b.line, b.name, b.kind) for b in want) == sorted((b["line"], b["name"], b["kind"]) for b in got)
                rec(ok, f"step {st['step']} outline matches the analyzer", f["path"])
            elif k == "all_names":
                mi = index.modules.get(f["path"])
                rec(mi is not None and mi.all_names == f["value"], f"step {st['step']} __all__ matches the analyzer", f["path"])
            elif k == "error":
                if f.get("missing"):
                    rec(not (snap.is_file(f["missing"]) or snap.is_dir(f["missing"])), f"step {st['step']} missing path really is missing", f["missing"])
    # derived claims: rebuild knowledge and compare every statable resolution with the oracle
    K = Seen(task_names(trace["task"]))
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
                    o = index.module_path(b.src, p)
                    rec(mp == o, "module path agrees with oracle", f"{b.src} from {p}: {mp} (oracle {o})")
    for p, bs in K.stmts.items():
        for ln, lst in bs.items():
            for b in lst:
                if b.kind == "from" and b.src_name:
                    mp = K.module_path(b.src, p)
                    if mp in (UNKNOWN, None):
                        continue
                    ex = exports(K, mp, b.src_name)
                    if isinstance(ex, Need):
                        continue
                    rec(ex == exports(index, mp, b.src_name), "export claim agrees with oracle", f"{mp} exports {b.src_name}: {ex}")
    # answer
    t = trace["task"]
    g = t["given"]
    ans = trace["answer"]
    if trace["stopped"] == "certificate":
        if t["family"] in ("resolve", "composite"):
            o = index.resolve(g["module"], g["name"])
            rec(ans["target"] == o.to_json(), "final resolution equals the oracle", f"{ans['text']} vs {o}")
        if t["family"] == "cover" or (t["family"] == "composite" and "statements" in ans and ans.get("target", {}).get("kind") == "def"):
            from .analysis import Target
            tgt = Target(**{k: v for k, v in ans["target"].items()}) if t["family"] == "composite" else Target("def", g["def_path"], g["def_line"], g["name"], g.get("def_kind", ""))
            imps = index.importers_of(tgt)
            want = sorted(f"{p}:{ln}" for p, ln, _, _ in imps)
            rec(sorted(ans["statements"]) == want, "final import set equals the oracle", f"{len(ans['statements'])} vs {len(want)}")
        # every verdict in the last cover state
        last = trace["steps"][-1]["goal_state"] if trace["steps"] else {}
        if "verdicts" in last:
            goal = make_goal(t)
            if isinstance(goal, CompositeGoal):
                goal.open_items(K)
                cov = goal.cover
            else:
                cov = goal
            if cov is not None:
                truth = {f"{p}:{ln}" for p, ln, _, _ in index.importers_of(cov.target)}
                for p, ln, v, reason in cov.verdict_table(K):
                    if v in ("in", "out"):
                        rec((v == "in") == (f"{p}:{ln}" in truth), "verdict agrees with oracle", f"{p}:{ln} {v}: {reason}")
    n_ok = sum(1 for r in results if r["ok"])
    return {"ok": n_ok == len(results), "n_checks": len(results), "n_ok": n_ok, "failures": [r for r in results if not r["ok"]][:20], "n_resolutions": n_res}


def adherence_stats(trace: dict) -> dict:
    c = defaultdict(int)
    for st in trace["steps"]:
        a = st.get("adherence")
        if a is None:
            c["first"] += 1
        else:
            c[a["status"]] += 1
    return dict(c)


def calibration(traces: list, bins=5) -> list:
    """Per probability bin: mean forecast vs realized frequency, over (step, label) pairs."""
    rows = defaultdict(lambda: [Fraction(0), 0, 0])  # sum p, count, hits
    for tr in traces:
        for st in tr["steps"]:
            fc = {l: Fraction(*p) for l, p in st["forecast"].items()}
            for l, p in fc.items():
                b = min(bins - 1, int(float(p) * bins))
                rows[b][0] += p
                rows[b][1] += 1
                rows[b][2] += 1 if st["outcome"] == l else 0
    out = []
    for b in sorted(rows):
        s, n, h = rows[b]
        out.append({"bin": f"{b / bins:.1f}-{(b + 1) / bins:.1f}", "n": n, "mean_forecast": float(s / n), "realized": h / n})
    return out
