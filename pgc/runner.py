"""The generate loop, in live mode (against a snapshot) or replay mode (against
logged responses). Produces a trace: per step the thought, the typed sidecar,
the call, the response, the outcome class, the facts, and plan adherence."""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from fractions import Fraction

from .goals import CompositeGoal, CoverGoal, ResolveGoal, current_name
from .analysis import Target
from .knowledge import Seen
from .policy import Policy, classify_outcome
from .prior import Prior
from .render import render_final, render_thought
from .analysis import Binding
from .snapshot import Call, Response


def seed_task_knowledge(K: Seen, task: dict):
    """What the task text asserts is known: the paths it names exist, and the
    statement it quotes is a from-import at that line."""
    g = task["given"]
    for k in ("module", "def_path"):
        if g.get(k):
            K.note_path(g[k])
    if task["family"] in ("resolve", "composite") and g.get("spec") and g.get("src_name"):
        b = Binding(g["module"], g["name"], int(g["line"]), "from", src=g["spec"], src_name=g["src_name"])
        K._record_stmt("task", g["module"], int(g["line"]), [b], None)


def fr(x):
    return [x.numerator, x.denominator] if isinstance(x, Fraction) else x


class ReplaySource:
    """Serves logged responses; refuses any call that deviates from the log."""

    def __init__(self, steps):
        self.steps = steps
        self.i = 0

    def call(self, call: Call):
        if self.i >= len(self.steps):
            raise RuntimeError("replay: more calls than logged")
        logged = self.steps[self.i]
        if logged["call"]["key"] != call.key():
            raise RuntimeError(f"replay: step {self.i + 1} called {call} but log has {logged['call']['text']}")
        self.i += 1
        return Response.from_json(logged["response"])


class LiveSource:
    def __init__(self, snap):
        self.snap = snap

    def call(self, call: Call):
        return self.snap.call(call)


def make_goal(task: dict):
    g = task["given"]
    if task["family"] == "resolve":
        return ResolveGoal(g["module"], g["name"])
    if task["family"] == "cover":
        return CoverGoal(Target("def", g["def_path"], g["def_line"], g["name"], g.get("def_kind", "")), g["name"])
    if task["family"] == "composite":
        return CompositeGoal(g["module"], g["name"])
    raise KeyError(task["family"])


def task_names(task: dict):
    g = task["given"]
    names = [str(v) for k, v in g.items() if isinstance(v, (str, int))]
    return names


def phase_of(goal):
    if isinstance(goal, CompositeGoal):
        return goal.phase
    return goal.family


def run(task: dict, source, prior: Prior, seed: int, budget: int, depth: int = 2) -> dict:
    K = Seen(task_names(task))
    seed_task_knowledge(K, task)
    goal = make_goal(task)
    policy = Policy(prior, task["given"]["name"], seed)
    steps = []
    prev_plan, prev_outcome, prev_facts, prev_keys = None, None, [], set()
    answer, stopped = None, "budget"
    for step in range(1, budget + 1):
        items = goal.open_items(K)
        if not items:
            answer = goal.answer(K)
            stopped = "certificate"
            break
        policy.name = current_name(goal, K)
        preferred = None
        if prev_plan is not None:
            pl = prev_plan.get(prev_outcome)
            preferred = pl.key() if pl is not None and not isinstance(pl, str) else None
        choice, ranked = policy.choose(K, items, step, depth=depth, preferred_key=preferred)
        if choice is None:
            stopped = "no grounded call serves the open items"
            break
        adherence = None
        if prev_plan is not None:
            planned = prev_plan.get(prev_outcome)
            if planned is None:
                status = "unplanned"  # the realized outcome was not among the forecast classes
            elif planned == "done":
                status = "deviated"
            elif planned == "continue" or planned is None:
                status = "open-ended"
            elif planned.key() == choice.call.key():
                status = "followed"
            elif {it.key for it in items} - prev_keys or planned.key() in K.calls_made or not any(planned.key() == c.call.key() for c in ranked):
                status = "replanned"  # new items opened, or the planned call is no longer available
            else:
                status = "deviated"
            adherence = {"planned": (planned if isinstance(planned, str) or planned is None else planned.key()), "status": status}
        active = goal
        if isinstance(goal, CompositeGoal):
            active = goal.resolve if goal.cover is None else goal.cover
        thought = render_thought(step, K, active, items, choice, ranked, prev_facts, adherence, seed, policy.name, phase_of(goal))
        resp = source.call(choice.call)
        new_facts = K.absorb(step, choice.call, resp)
        served_kinds = {k[0] for k in choice.serves}
        outcome = classify_outcome(choice.call, resp, K, served_kinds)
        goal_state = {}
        if phase_of(goal) == "resolve":
            gg = goal.resolve if isinstance(goal, CompositeGoal) else goal
            goal_state["chain"] = [[m, n, k, (list(e) if isinstance(e, tuple) else e)] for m, n, k, e in gg.chain(K)]
        else:
            gg = goal.cover if isinstance(goal, CompositeGoal) else goal
            goal_state["verdicts"] = [list(r) for r in gg.verdict_table(K)]
            goal_state["uncovered"] = {pc: gg.uncovered_scopes(K, pc) for pc in gg.CLASSES}
        steps.append({
            "step": step,
            "thought": thought,
            "items": [{"kind": it.kind, "key": list(it.key), "desc": it.desc} for it in items],
            "candidates": [{"call": str(c.call), "key": c.call.key(), "v1": fr(c.v1), "v2": fr(c.v2), "p_cap": fr(c.p_cap),
                            "forecast": {l: fr(p) for l, p in c.forecast().items()}, "serves": sorted(list(k) for k in c.serves)} for c in ranked],
            "choice": {"call": str(choice.call), "key": choice.call.key(), "provenance": choice.provenance, "v2": fr(choice.v2)},
            "forecast": {l: fr(p) for l, p in choice.forecast().items()},
            "plan": {l: (nxt if isinstance(nxt, str) else nxt.key()) for l, nxt in choice.plan.items()},
            "call": {"text": str(choice.call), "key": choice.call.key(), "tool": choice.call.tool, "args": list(choice.call.args)},
            "response": resp.to_json(),
            "outcome": outcome,
            "facts": [f.to_json() for f in new_facts],
            "adherence": adherence,
            "goal_state": goal_state,
        })
        prev_plan, prev_outcome, prev_facts, prev_keys = choice.plan, outcome, new_facts, {it.key for it in items}
    hindsight = hindsight_table(task, steps, answer) if stopped == "certificate" else {}
    final = render_final(answer, stopped, steps, hindsight, task["family"])
    return {
        "task": task,
        "seed": seed,
        "depth": depth,
        "theta_hash": prior.hash,
        "budget": budget,
        "steps": steps,
        "answer": answer,
        "stopped": stopped,
        "n_calls": len(steps),
        "final_thought": final,
        "hindsight": {str(k): v for k, v in hindsight.items()},
        "open_at_stop": [it.desc for it in goal.open_items(K)] if stopped != "certificate" else [],
    }


def hindsight_table(task, steps, answer) -> dict:
    """For each step, is the certificate still derivable without its response?
    Dropping a response also drops every later call that was grounded by it
    (a path, name or line first seen in that response), transitively."""
    calls = [Call(st["call"]["tool"], tuple(st["call"]["args"])) for st in steps]
    resps = [Response.from_json(st["response"]) for st in steps]
    # provenance: which step first introduced each argument
    K = Seen(task_names(task))
    seed_task_knowledge(K, task)
    intro = {}  # step -> set of steps it depends on
    for i, (c, r) in enumerate(zip(calls, resps)):
        deps = set()
        for a in c.args:
            a = str(a)
            w = K.first_seen.get(a)
            if w not in (None, "task") and w != i + 1:
                deps.add(w)
        if c.tool == "read":
            # the start line came from the outline header of that file
            for j in range(i):
                if calls[j].tool == "symbols" and calls[j].args[0] == c.args[0]:
                    deps.add(j + 1)
                    break
        intro[i + 1] = deps
        K.absorb(i + 1, c, r)
    out = {}
    for skip in range(1, len(steps) + 1):
        dropped = {skip}
        changed = True
        while changed:
            changed = False
            for j, deps in intro.items():
                if j not in dropped and deps & dropped:
                    dropped.add(j)
                    changed = True
        K2 = Seen(task_names(task))
        seed_task_knowledge(K2, task)
        goal = make_goal(task)
        for i, (c, r) in enumerate(zip(calls, resps)):
            if i + 1 in dropped:
                continue
            K2.absorb(i + 1, c, r)
        out[skip] = not (goal.answer(K2) == answer)
    return out


def trace_markdown(trace: dict) -> str:
    t = trace["task"]
    lines = [f"# {t['id']}", "", f"**Repository:** {t['repo']}  ", f"**Family:** {t['family']}  ", f"**Seed:** {trace['seed']}, prior {trace['theta_hash']}", "",
             "## Task", "", t["text"], "", f"*Declared semantics:* {t['semantics']}", ""]
    for st in trace["steps"]:
        lines.append(f"## Step {st['step']}")
        lines.append("")
        lines.append(st["thought"])
        lines.append("")
        lines.append(f"**Call:** `{st['call']['text']}`")
        lines.append("")
        r = st["response"]
        body = "\n".join(r["lines"][:25])
        more = f"\n... ({len(r['lines']) - 25} more lines)" if len(r["lines"]) > 25 else ""
        cap = " (capped)" if r["capped"] else ""
        err = f"error: {r['error']}" if r["error"] else ""
        lines.append(f"**Response**{cap}: outcome `{st['outcome']}`")
        lines.append("")
        lines.append("```")
        lines.append(err or body + more)
        lines.append("```")
        lines.append("")
        lines.append("<details><summary>sidecar</summary>")
        lines.append("")
        side = {k: st[k] for k in ("items", "candidates", "choice", "forecast", "plan", "adherence", "facts", "goal_state")}
        lines.append("```json")
        lines.append(json.dumps(side, indent=1)[:6000])
        lines.append("```")
        lines.append("</details>")
        lines.append("")
    lines.append("## Final")
    lines.append("")
    lines.append(trace["final_thought"])
    lines.append("")
    lines.append(f"**Answer:** `{json.dumps(trace['answer'])}`  ")
    lines.append(f"**Stopped:** {trace['stopped']} after {trace['n_calls']} calls")
    return "\n".join(lines)
