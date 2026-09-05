"""Prose thoughts rendered from the typed state delta. Every number in the prose
rounds from a value in the sidecar; every name is grounded."""
from __future__ import annotations

import hashlib
import random
from fractions import Fraction

from .analysis import DYNAMIC, UNKNOWN
from .prior import pattern
from .snapshot import Call


def pct(x: Fraction) -> str:
    v = int(round(float(x) * 20)) * 5
    if v <= 0:
        return "under 5%"
    if v >= 100:
        return "near certain"
    return f"about {v}%"


def _rng(seed, step):
    return random.Random(int(hashlib.sha256(f"render:{seed}:{step}".encode()).hexdigest(), 16))


def describe_call(call: Call, name: str) -> str:
    if call.tool == "ls":
        return f"list `{call.args[0]}`"
    if call.tool == "symbols":
        if len(call.args) > 1:
            return f"outline `{call.args[0]}` filtered to `{call.args[1]}`"
        return f"outline `{call.args[0]}`"
    if call.tool == "read":
        return f"read `{call.args[0]}` from line {call.args[1]}"
    if call.tool == "grep":
        pat, scope = call.args
        for pc, words in (("DEF", f"`def`/`class {name}` statements"), ("IMPORT", f"from-imports naming `{name}`"),
                          ("STAR", "star imports"), ("IMPORT_OR_STAR", f"from-imports naming `{name}` or star imports")):
            if pattern(pc, name) == pat:
                return f"grep {words} under `{scope}`"
        return f"grep `{pat}` under `{scope}`"
    return str(call)


OUTCOME_WORDS = {
    ("symbols", "def"): "a definition there ends the chain",
    ("symbols", "reexport"): "a re-export continues the chain to its source",
    ("symbols", "star"): "no binding but a star import means checking what that source exports",
    ("symbols", "none"): "no binding at all points at a submodule or an unresolved name",
    ("symbols", "cap"): "a capped outline means filtering by name",
    ("symbols", "ok"): "the outline lists its imports of the name",
    ("symbols", "missing"): "the file does not exist",
    ("ls", "complete"): "a complete listing settles which files exist",
    ("ls", "cap"): "a capped listing settles nothing",
    ("grep", "zero"): "no hits",
    ("grep", "mid"): "hits under the cap",
    ("grep", "cap"): "a capped result",
    ("read", "fits"): "the whole list fits the window",
    ("read", "long"): "the list runs past the window",
}


CONTINUE_WORDS = {
    ("symbols", "reexport"): "locate and outline the source it names",
    ("symbols", "star"): "check what the star source exports",
    ("symbols", "none"): "check for a submodule of that name",
    ("symbols", "ok"): "resolve the sources its import statements name",
    ("grep", "mid"): "outline each module that appears",
    ("grep", "cap"): "list the scope and split it",
    ("ls", "complete"): "outline the module it reveals",
    ("read", "fits"): "resolve through the exported name",
}


def settled_sentences(facts, K, goal_name: str) -> list:
    out = []
    for f in facts:
        d = f.data
        if f.kind == "error":
            if d.get("missing"):
                out.append(f"`{d['missing']}` does not exist, so that path is ruled out.")
            else:
                out.append(f"That call failed ({d['error']}).")
        elif f.kind == "listing":
            n = len(d["entries"])
            py = [e for e in d["entries"] if e.endswith(".py") or e.endswith("/")]
            tail = "complete" if d["complete"] else "capped, so absence proves nothing"
            sample = ", ".join(f"`{e}`" for e in py[:6])
            more = f" and {len(py) - 6} more" if len(py) > 6 else ""
            out.append(f"`{d['dir']}` lists {n} entries ({tail}): {sample}{more}.")
        elif f.kind == "grep":
            n = len(d["hits"])
            files = sorted({p for p, _ in d["hits"]})
            if d["capped"]:
                out.append(f"The grep under `{d['scope']}` hit the cap at {n} lines, so it proves nothing about what else is there.")
            elif n == 0:
                out.append(f"The grep under `{d['scope']}` returned nothing, and it was not capped, so there are no such lines there.")
            else:
                shown = ", ".join(f"`{p}`" for p in files[:4]) + (f" and {len(files) - 4} more files" if len(files) > 4 else "")
                out.append(f"The grep under `{d['scope']}` returned {n} lines, under the cap, so these are all of them: {shown}.")
        elif f.kind == "outline":
            p = d["path"]
            hdr = d["header"]
            filt = d["filter"]
            bs = d["bindings"]
            nonstar = [b for b in bs if b["kind"] != "star"]
            stars = [b for b in bs if b["kind"] == "star"]
            dyn = "it uses dynamic namespace tricks" if hdr["dynamic"] else "no dynamic namespace tricks"
            allw = {"none": "no `__all__`", "dynamic": "a non-literal `__all__`"}.get(hdr["all_status"], f"a literal `__all__` at line {hdr['all_line']}")
            if filt is not None:
                rel = [b for b in nonstar if b["name"] == filt]
                if len(rel) == 1:
                    b = rel[0]
                    if b["kind"] in ("def", "class", "assign"):
                        out.append(f"In `{p}`, `{filt}` has exactly one binding: a {b['kind']} at line {b['line']}. {dyn.capitalize()}, {allw}.")
                    elif b["kind"] == "from":
                        out.append(f"In `{p}`, `{filt}` has exactly one binding: line {b['line']} imports it as `{b['src_name']}` from `{b['src']}`. {dyn.capitalize()}, {allw}.")
                    else:
                        out.append(f"In `{p}`, `{filt}` is bound once, at line {b['line']}, by `import {b['src']}`. {dyn.capitalize()}, {allw}.")
                elif len(rel) == 0:
                    st = f"{len(stars)} star import(s): " + ", ".join(f"`{s['src']}`" for s in stars) if stars else "no star imports"
                    out.append(f"`{p}` binds no `{filt}` at module level; {st}; {allw}; {dyn}.")
                else:
                    out.append(f"`{p}` binds `{filt}` {len(rel)} times (lines {', '.join(str(b['line']) for b in rel)}), which the declared semantics calls ambiguous.")
                imp = [b for b in nonstar if b["name"] != filt and b.get("src_name") == filt]
                if imp:
                    out.append("It also imports it under another name: " + ", ".join(f"`{b['name']}` at line {b['line']}" for b in imp) + ".")
                froms = [b for b in nonstar if b.get("src_name") == filt and b["kind"] == "from"]
                if froms and len(rel) != 1:
                    out.append("Import statements of the name there: " + ", ".join(f"line {b['line']} from `{b['src']}`" for b in froms) + ".")
            else:
                tail = "" if d["complete"] else " (capped, so this is only the start of the file)"
                out.append(f"The outline of `{p}` has {len(bs)} bindings{tail}; {allw}; {dyn}.")
        elif f.kind == "all_names":
            v = d["value"]
            if v == DYNAMIC:
                out.append(f"`__all__` in `{d['path']}` is not a literal list, so its exports are ambiguous.")
            elif v is None:
                out.append(f"`{d['path']}` has no `__all__`.")
            else:
                has = f"and it names `{goal_name}`" if goal_name in v else f"and `{goal_name}` is not among them"
                out.append(f"`__all__` in `{d['path']}` lists {len(v)} names, {has}.")
        elif f.kind == "read":
            stm = K.statements_at(d["path"], d["start"])
            if stm:
                names = ", ".join(f"`{b.name}`" for b in stm[:5])
                out.append(f"The statement at `{d['path']}`:{d['start']} binds {names}.")
    return out


def chain_sentence(goal, K) -> str:
    hops = goal.chain(K)
    parts = []
    for m, n, kind, extra in hops:
        if kind == "reexport":
            spec, mp = extra
            parts.append(f"`{m}` takes `{n}` from `{spec}`" + (f" (`{mp}`)" if mp else " (module not yet located)"))
        elif kind in ("def", "class", "assign"):
            parts.append(f"`{m}` defines it ({kind} at line {extra})")
        elif kind == "star":
            parts.append(f"`{m}` gets it through a star import of `{extra}`")
        elif kind == "open":
            parts.append(f"`{m}` is not yet closed for `{n}`")
        else:
            parts.append(f"`{m}` has no binding for `{n}`")
    return "Chain: " + "; ".join(parts) + "."


def cover_sentence(goal, K) -> str:
    rows = goal.verdict_table(K)
    mods = goal.candidate_modules(K)
    ins = [r for r in rows if r[2] == "in"]
    outs = [r for r in rows if r[2] == "out"]
    none = [r for r in rows if r[2] == "none"]
    pend = [r for r in rows if r[2] == "pending"]
    cov = []
    for pc in goal.CLASSES:
        open_ = goal.uncovered_scopes(K, pc)
        cov.append(f"{pc.lower()} coverage " + ("complete" if not open_ else f"open at {', '.join('`' + s + '`' for _, s in open_[:4])}" + (f" and {len(open_) - 4} more" if len(open_) > 4 else "")))
    s = (f"Candidate modules so far: {len(mods)}; statements confirmed: {len(ins)}, ruled out: {len(outs)}, modules with no such import: {len(none)}, pending: {len(pend)}. "
         + "; ".join(cov) + ".")
    if outs:
        ex = outs[-1]
        s += f" Latest ruled out: `{ex[0]}`:{ex[1]}, {ex[3]}."
    return s


def render_thought(step, K, goal, items, choice, ranked, new_facts, adherence, seed, name, family_phase) -> str:
    rng = _rng(seed, step)
    paras = []
    # settled
    if step == 1:
        paras.append(rng.choice([
            "Nothing seen yet beyond the task text.",
            "Starting from the task alone; nothing in the repository has been read.",
        ]))
    else:
        s = settled_sentences(new_facts, K, name)
        if adherence and adherence.get("status") == "deviated":
            s.append("This is not the branch I planned for that outcome; the open items changed more than expected.")
        elif adherence and adherence.get("status") == "replanned":
            s.append("The call I had planned for this outcome is no longer useful, so I am re-planning.")
        elif adherence and adherence.get("status") == "unplanned":
            s.append("That outcome was not one I had forecast, so there was no branch for it; re-planning from the open items.")
        paras.append(" ".join(s) if s else "The last response settled nothing new.")
    # goal state
    if family_phase == "resolve":
        paras.append(chain_sentence(goal, K))
    else:
        paras.append(cover_sentence(goal, K))
    # ledger
    descs = [it.desc for it in items]
    if len(descs) > 4:
        ledger = "; ".join(descs[:4]) + f"; and {len(descs) - 4} more"
    else:
        ledger = "; ".join(descs)
    paras.append(rng.choice(["Open: ", "Still to settle: ", "Outstanding: "]) + ledger + ".")
    # decision
    if choice is not None:
        fc = choice.forecast()
        top = sorted(fc.items(), key=lambda kv: (-kv[1], kv[0]))
        exp = "; ".join(f"{OUTCOME_WORDS.get((choice.call.tool, l), l)} ({pct(p)})" for l, p in top if p > 0)
        d = f"Next: {describe_call(choice.call, name)}, because {choice.provenance}. I expect: {exp}."
        runner = next((c for c in ranked if c is not choice), None)
        if runner is not None:
            reason = runner_up_reason(choice, runner)
            d += f" The alternative, {describe_call(runner.call, name)}, {reason}."
        plan_bits = []
        for l, nxt in choice.plan.items():
            if nxt == "done":
                plan_bits.append(f"{l}: done")
            elif nxt == "continue":
                plan_bits.append(f"{l}: {CONTINUE_WORDS.get((choice.call.tool, l), 'work the items it opens')}")
            else:
                plan_bits.append(f"{l}: {describe_call(nxt, name)}")
        d += " Plan by outcome: " + "; ".join(plan_bits) + "."
        paras.append(d)
    return "\n\n".join(paras)


def runner_up_reason(choice, runner) -> str:
    if runner.p_cap > choice.p_cap + Fraction(1, 10):
        return f"is more likely to hit the cap ({pct(runner.p_cap)} against {pct(choice.p_cap)})"
    if len(runner.serves) < len(choice.serves):
        return "serves fewer of the open items"
    if runner.spawned > choice.spawned:
        return "is expected to open more follow-up work"
    if runner.v2 == choice.v2:
        return "scores the same; the seed broke the tie"
    return "costs more in expectation"


def render_final(answer, stopped, steps, hindsight, family) -> str:
    if stopped != "certificate":
        return f"Stopping without a certificate: {stopped}. What remains open is listed in the sidecar."
    if family == "resolve" or (family == "composite" and "statements" not in answer):
        s = f"Certificate complete. The name resolves to `{answer['text']}`."
    else:
        s = f"Certificate complete. {answer['count']} import statements import this definition: " + ", ".join(f"`{x}`" for x in answer["statements"][:12])
        if answer["count"] > 12:
            s += f" and {answer['count'] - 12} more"
        s += "."
    unneeded = [i for i, needed in hindsight.items() if not needed]
    if unneeded:
        s += f" In hindsight, {len(unneeded)} of {len(steps)} calls were not needed for the certificate: steps {', '.join(map(str, unneeded))}."
    else:
        s += f" In hindsight every one of the {len(steps)} calls was needed for the certificate."
    return s
