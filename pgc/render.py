"""Prose thoughts in an engineer's voice, rendered from the typed state delta.

Rules: every name comes from the task or a response; every hedge word maps to a
probability band and is recorded next to the exact probability so the checker
can verify the wording; internals (needs, items, outcome classes) never appear.
"""
from __future__ import annotations

import hashlib
import random
from fractions import Fraction

from .analysis import DYNAMIC, UNKNOWN
from .policy import pattern_class
from .snapshot import Call

HEDGE_BANDS = [  # (min, max, word)
    (Fraction(9, 10), Fraction(1), "almost certainly"),
    (Fraction(3, 4), Fraction(9, 10), "very likely"),
    (Fraction(11, 20), Fraction(3, 4), "probably"),
    (Fraction(7, 20), Fraction(11, 20), "maybe"),
    (Fraction(3, 20), Fraction(7, 20), "possibly"),
    (Fraction(0), Fraction(3, 20), "unlikely"),
]


def hedge(p: Fraction) -> str:
    """Bands are closed at the top: p in (lo, hi]; the lowest band includes 0."""
    for lo, hi, w in HEDGE_BANDS:
        if (lo < p <= hi) or (p == 0 and lo == 0):
            return w
    return "unlikely"


def hedge_band(word: str):
    for lo, hi, w in HEDGE_BANDS:
        if w == word:
            return lo, hi
    return None


def _rng(seed, step):
    return random.Random(int(hashlib.sha256(f"render:{seed}:{step}".encode()).hexdigest(), 16))


def short(p: str) -> str:
    return f"`{p}`"


def module_word(p: str) -> str:
    if p.endswith("/__init__.py"):
        return f"the package `{p.rsplit('/', 1)[0]}`"
    if p.endswith("__init__.py"):
        return "the top-level package"
    if "/tests/" in "/" + p or p.startswith(("tests/", "testing/")):
        return f"the test module `{p}`"
    return f"`{p}`"


KIND_WORD = {"class": "a class", "def": "a function", "assign": "a module-level assignment", "import": "an `import`", "from": "a `from ... import`"}


# ---------------------------------------------------------------------------
# Observations: what the last response taught me
# ---------------------------------------------------------------------------

def observe(facts, K, name, phase, rng, prev_call, served=()):
    out = []
    for f in facts:
        d = f.data
        k = f.kind
        if k == "error":
            if d.get("missing"):
                path = d["missing"]
                if path.endswith("/__init__.py"):
                    out.append(f"No `{path}` either, so that import must come from outside the snapshot.")
                elif path.endswith(".py"):
                    stem = path[:-3]
                    out.append(f"There is no `{path}`, so `{stem.rsplit('/', 1)[-1]}` is either a package (`{stem}/__init__.py`) or not in this repository at all.")
                else:
                    out.append(f"`{path}` does not exist.")
            else:
                out.append(f"That call failed ({d['error']}).")
        elif k == "listing":
            entries = d["entries"]
            py = [e for e in entries if e.endswith(".py") or e.endswith("/")]
            tail = "" if d["complete"] else ", and the listing is capped so I can't trust absences"
            purpose = []
            for it in served:
                if it.kind in ("module_path", "submodule") and it.need is not None:
                    if it.kind == "submodule":
                        want = it.need.arg
                    else:
                        parts = it.need.arg.lstrip(".").split(".")
                        # a root-level listing settles the top package; a deeper one settles the last component
                        want = parts[0] if (d["dir"] in (".", "src", "lib") and not it.need.arg.startswith(".") and len(parts) > 1) else parts[-1]
                    if want + ".py" in entries:
                        purpose.append(f"`{want}.py` is there, so `{it.need.arg}` is a plain module")
                    elif want + "/" in entries:
                        purpose.append(f"`{want}/` is there, so `{it.need.arg}` is a package")
                    elif d["complete"]:
                        purpose.append(f"there is no `{want}` here" + (", so nothing shadows the real one" if it.kind == "submodule" else ""))
                elif it.kind == "split":
                    purpose.append(f"{len(py)} parts to search separately")
            purpose = list(dict.fromkeys(purpose))
            if purpose:
                out.append(f"`{d['dir']}/` has {len(entries)} entries{tail}: " + "; ".join(purpose) + ".")
            else:
                shown = ", ".join(f"`{e}`" for e in py[:6])
                more = f" and {len(py) - 6} more" if len(py) > 6 else ""
                out.append(f"`{d['dir']}/` has {len(entries)} entries{tail}: {shown}{more}.")
        elif k == "grep":
            pc = pattern_class(d["pattern"])
            name = pattern_symbol(d["pattern"], name)
            n = len(d["hits"])
            files = sorted({p for p, _ in d["hits"]})
            what = {"DEF": f"`class {name}`/`def {name}`", "IMPORT": f"imports of `{name}`", "STAR": "star imports",
                    "IMPORT_OR_STAR": f"imports of `{name}` or star imports", "SUBCLASS": f"classes deriving from `{name}`", "CALL": f"calls of `{name}`"}[pc]
            where = "anywhere" if d["scope"] == "." else f"under `{d['scope']}`"
            if d["capped"]:
                out.append(f"The search for {what} {where} hit the cap at {n} lines, so it only shows part of the picture.")
            elif n == 0:
                if pc == "DEF":
                    out.append(f"No `class {name}` or `def {name}` {where}, so the name must be bound by assignment or come from outside.")
                else:
                    out.append(f"Nothing {where} for {what}, and the search was not capped, so that part of the tree is clear.")
            else:
                fl = ", ".join(f"`{p}`" for p in files[:4]) + (f" and {len(files) - 4} more files" if len(files) > 4 else "")
                if pc == "DEF":
                    if n == 1:
                        out.append(f"There is exactly one `{name}` definition in the tree, in {fl}.")
                    else:
                        out.append(f"`{name}` is defined {n} times: {fl}. Only one of them can be the one this import means, so the import chain decides.")
                else:
                    out.append(f"{n} matching lines {where} for {what}, in {fl}, and the search was under the cap, so that is the complete set there.")
        elif k == "outline":
            kinds = {it.kind for it in served}
            eff_phase = phase if ("outline" in kinds or not kinds) else "resolve"
            out.extend(observe_outline(d, K, name, eff_phase))
        elif k == "all_names":
            v = d["value"]
            if v == DYNAMIC:
                out.append(f"`__all__` in `{d['path']}` is computed rather than written out, so I can't tell statically what it exports.")
            elif v is None:
                out.append(f"`{d['path']}` has no `__all__`.")
            elif name in v:
                out.append(f"`__all__` in `{d['path']}` lists {len(v)} names and `{name}` is one of them, so its star import does carry the name.")
            else:
                out.append(f"`__all__` in `{d['path']}` lists {len(v)} names and `{name}` is not among them, so that star import does not carry it.")
        elif k == "members":
            defs = [n for _, kind, n in d["entries"] if kind == "def"]
            if not d["complete"]:
                out.append(f"`{d['cls']}` has more members than fit in one view.")
            elif name in defs:
                out.append(f"`{d['cls']}` defines `{name}` itself (line {[ln for ln, kind, n in d['entries'] if n == name][0]}), so it overrides.")
            else:
                sample = ", ".join(f"`{x}`" for x in defs[:4]) + (" and more" if len(defs) > 4 else "")
                out.append(f"`{d['cls']}` defines {sample if defs else 'no methods of its own'}, but no `{name}`, so it inherits it.")
        elif k == "calls":
            n = len(d["lines"])
            if not d["complete"]:
                out.append(f"`{d['path']}` calls `{name}` {d['count']} times, more than fit in one view.")
            elif n == 0:
                out.append(f"`{d['path']}` binds `{name}` but never actually calls it by that name.")
            else:
                ls = ", ".join(str(x) for x in d["lines"][:6]) + (f" and {n - 6} more" if n > 6 else "")
                out.append(f"`{d['path']}` calls `{name}` at line{'s' if n > 1 else ''} {ls}, and those are real calls of the module-level name, not a shadowed local.")
    return out


def observe_outline(d, K, name, phase):
    p = d["path"]
    hdr = d["header"]
    filt = d["filter"]
    bs = d["bindings"]
    nonstar = [b for b in bs if b["kind"] != "star"]
    stars = [b for b in bs if b["kind"] == "star"]
    out = []
    dyn = " Careful: this module manipulates its namespace dynamically, so static resolution is not reliable here." if hdr["dynamic"] else ""
    if filt is None:
        head = f"The outline of `{p}` shows {len(bs)} top-level bindings{'' if d['complete'] else ' (cut off by the cap)'}."
        mine = [b for b in nonstar if b["name"] == name]
        if len(mine) == 1 and mine[0]["kind"] == "from":
            head += f" `{name}` there is imported from `{mine[0]['src']}` (line {mine[0]['line']})."
        elif len(mine) == 1 and mine[0]["kind"] == "import":
            head += f" `{name}` there is `import {mine[0]['src']}` (line {mine[0]['line']})."
        elif len(mine) == 1:
            head += f" `{name}` is {KIND_WORD.get(mine[0]['kind'], 'defined')} there at line {mine[0]['line']}."
        elif not mine and d["complete"]:
            head += f" Nothing binds `{name}` at module level."
        out.append(head + dyn)
        return out
    mine = [b for b in nonstar if b["name"] == filt]
    imports_of = [b for b in nonstar if b["kind"] == "from" and b.get("src_name") == filt]
    classes = [b for b in nonstar if b["kind"] == "class" and any(x.split(".")[-1] == filt for x in b.get("bases", []))]
    who = module_word(p)
    if phase == "subclasses":
        if classes:
            cl = "; ".join(f"`class {b['name']}({','.join(b['bases'])})` at line {b['line']}" for b in classes[:4])
            out.append(f"{who[0].upper() + who[1:]} has {cl}.")
        else:
            out.append(f"{who[0].upper() + who[1:]} matched the search, but none of its module-level classes actually derive from `{filt}`; probably a nested class, a comment or a string.")
        if imports_of:
            b = imports_of[0]
            out.append(f"It gets `{filt}` from `{b['src']}` (line {b['line']}), which is what the base name resolves through.")
        elif mine and mine[0]["kind"] in ("class", "def", "assign"):
            out.append(f"It also defines its own `{filt}` at line {mine[0]['line']}, so the base is that local one, not ours.")
        elif not mine and classes:
            out.append(f"Nothing binds `{filt}` at module level there{', but there are star imports to check' if stars else ''}.")
        return out + ([dyn.strip()] if dyn else [])
    if phase in ("importers",):
        if imports_of:
            parts = [f"line {b['line']} imports it from `{b['src']}`" + (f" as `{b['name']}`" if b["name"] != filt else "") for b in imports_of[:4]]
            out.append(f"{who[0].upper() + who[1:]}: " + "; ".join(parts) + ".")
        else:
            out.append(f"{who[0].upper() + who[1:]} matched the search but has no module-level import of `{filt}`.")
        if stars:
            out.append("It also star-imports " + ", ".join(f"`{s['src']}`" for s in stars[:4]) + (", each of which could carry the name, so those need checking." if len(stars) > 1 else ", which could carry the name, so that needs checking."))
        return out + ([dyn.strip()] if dyn else [])
    # resolve / callers / expose / default
    if len(mine) == 1:
        b = mine[0]
        if b["kind"] in ("class", "def", "assign"):
            what = {"class": "a class", "def": "a function", "assign": "an assignment"}[b["kind"]]
            out.append(f"`{filt}` is {what} defined in {who} at line {b['line']}." if phase != "resolve" else f"There it is: `{filt}` is {what} at `{p}:{b['line']}`.")
        elif b["kind"] == "from":
            out.append(f"{who[0].upper() + who[1:]} does not define `{filt}` itself; line {b['line']} imports it from `{b['src']}`" + (f" under the name `{b['src_name']}`" if b["src_name"] != filt else "") + ".")
        else:
            out.append(f"In {who}, `{filt}` is a module import (`import {b['src']}`), not a definition.")
    elif len(mine) == 0:
        if stars:
            out.append(f"{who[0].upper() + who[1:]} has no `{filt}` at module level, but it star-imports " + ", ".join(f"`{s['src']}`" for s in stars[:4]) + ", so the name may come through one of those.")
        elif p.endswith("__init__.py") and phase == "expose":
            out.append(f"{who[0].upper() + who[1:]} does not bind `{filt}`, so there is nothing to conflict with; I still need to be sure there is no submodule of that name.")
        elif p.endswith("__init__.py"):
            out.append(f"{who[0].upper() + who[1:]} does not bind `{filt}`; for a package that leaves a submodule called `{filt}` as the only option.")
        else:
            out.append(f"{who[0].upper() + who[1:]} does not bind `{filt}` at module level at all" + (", so its matches were false positives." if phase == "callers" else "."))
    else:
        out.append(f"{who[0].upper() + who[1:]} binds `{filt}` {len(mine)} times (lines {', '.join(str(b['line']) for b in mine)}), which makes it ambiguous under the rules I am working with.")
    if imports_of and not mine:
        out.append("It imports the name under another alias: " + ", ".join(f"`{b['name']}` at line {b['line']}" for b in imports_of[:3]) + ".")
    if dyn:
        out.append(dyn.strip())
    return out


# ---------------------------------------------------------------------------
# Status: where the goal stands
# ---------------------------------------------------------------------------

def status(chain, state, K, name, step, items, rng):
    phase = state["phase"]
    of = state["of"]
    prefix = ""
    if phase == "resolve":
        hops = state["chain"]
        parts = []
        for m, n, kind, extra in hops:
            if kind == "reexport":
                spec, mp = extra
                parts.append(f"`{m}` takes `{n}` from `{spec}`" + ("" if mp else ", which I still have to locate"))
            elif kind in ("class", "def", "assign"):
                parts.append(f"`{m}` defines it at line {extra}")
            elif kind == "star":
                parts.append(f"`{m}` gets it through a star import of `{extra}`")
            elif kind == "open":
                parts.append(f"I have not looked at `{m}` yet" if len(hops) == 1 else f"`{m}` is next")
        if len(parts) <= 1 and step == 1:
            return ""
        return prefix + "So far: " + "; ".join(parts) + "."
    if phase in ("importers", "subclasses", "callers", "not_overriding"):
        n_in, n_out, n_pend = state["n_in"], state["n_out"], state["n_pending"]
        unit = {"importers": "import statements", "subclasses": "subclasses", "callers": "call sites", "not_overriding": "classes without their own method"}[phase]
        cov = ""
        if phase != "not_overriding":
            open_ = [s for pc in state["uncovered"] for _, s in state["uncovered"][pc]]
            if not open_:
                cov = " The search itself is complete; what is left is checking the candidates."
            elif len(state["candidates"]) > 0:
                cov = f" The search still has {len(open_)} scope{'s' if len(open_) != 1 else ''} to cover."
        tally = f"Tally: {n_in} {unit} confirmed, {n_out} ruled out, {n_pend} pending."
        if n_in + n_out + n_pend == 0:
            return ""
        return prefix + tally + cov
    if phase == "expose":
        if state.get("bound") is False:
            return prefix + f"The package does not bind `{name}` yet, so a one-line import will do the job."
        return ""
    return ""


# ---------------------------------------------------------------------------
# Intent: what I will do next and why
# ---------------------------------------------------------------------------

OUTCOME_PHRASE = {
    ("symbols", "def"): "it is defined right there",
    ("symbols", "reexport"): "it is re-exported from somewhere else",
    ("symbols", "star"): "it comes in through a star import",
    ("symbols", "none"): "the name is not bound there",
    ("symbols", "missing"): "the file does not exist",
    ("symbols", "cap"): "the outline is too long to fit",
    ("symbols", "ok"): "the outline shows what I need",
    ("ls", "complete"): "the listing fits",
    ("ls", "cap"): "the listing is too long",
    ("grep", "zero"): "nothing turns up",
    ("grep", "mid"): "it fits under the cap",
    ("grep", "cap"): "it caps",
    ("read", "fits"): "the list fits in one read",
    ("read", "long"): "the list runs past the window",
    ("members", "ok"): "the members fit",
    ("members", "cap"): "there are too many members",
    ("calls", "ok"): "the call sites fit",
    ("calls", "cap"): "there are too many call sites",
}


def pattern_symbol(pat: str, default: str) -> str:
    import re as _re
    m = _re.search(r"\\s\+(\w+)\\b", pat) or _re.search(r"\\b(\w+)\\s\*\\\(", pat) or _re.search(r"\\b(\w+)\\b", pat)
    return m.group(1) if m else default


def describe_call(call: Call, name: str, K, items_by_key, serves) -> str:
    kinds = {items_by_key[k].kind for k in serves if k in items_by_key}
    if call.tool == "symbols":
        M = call.args[0]
        n = call.args[1] if len(call.args) > 1 else None
        unknown = M not in K.files and M not in K.header
        if unknown:
            return f"outline `{M}` directly, which both checks that the file exists and shows me `{n}`"
        if "outline" in kinds:
            return f"look at `{M}`'s top-level names for `{n}`"
        if n is None:
            return f"outline all of `{M}`"
        return f"look at `{M}`'s top-level names for `{n}`"
    if call.tool == "ls":
        d = call.args[0]
        if "split" in kinds:
            return f"list `{d}/` so I can search its parts one at a time"
        return f"list `{d}/` to see what lives there"
    if call.tool == "grep":
        pat, scope = call.args
        pc = pattern_class(pat)
        name = pattern_symbol(pat, name)
        where = "the whole tree" if scope == "." else f"`{scope}`"
        return {"DEF": f"search {where} for `class {name}`/`def {name}`",
                "IMPORT": f"search {where} for imports of `{name}`",
                "STAR": f"search {where} for star imports",
                "IMPORT_OR_STAR": f"search {where} for imports of `{name}` and star imports in one go",
                "SUBCLASS": f"search {where} for classes deriving from `{name}`",
                "CALL": f"search {where} for calls of `{name}`"}[pc]
    if call.tool == "read":
        return f"read `__all__` in `{call.args[0]}`"
    if call.tool == "members":
        return f"check `{call.args[1]}`'s own members in `{call.args[0]}`"
    if call.tool == "calls":
        return f"list the call sites of `{call.args[1]}` in `{call.args[0]}`"
    return str(call)


def why(choice, K, items_by_key, phase, name) -> str:
    kinds = {items_by_key[k].kind for k in choice.serves if k in items_by_key}
    call = choice.call
    if call.tool == "symbols" and "module_path" in kinds:
        spec = next((items_by_key[k].need.arg for k in choice.serves if k in items_by_key and items_by_key[k].kind == "module_path"), None)
        return f"if `{spec}` is a plain module that is where it has to be" if spec else "that is where the module should be"
    if call.tool == "symbols" and "bindings" in kinds:
        return "that settles what the name means there"
    if call.tool == "symbols" and "outline" in kinds:
        return {"importers": "its outline names every import of the symbol exactly, aliases included",
                "subclasses": "the outline lists each class with its bases",
                "callers": "before counting calls I need to know the name refers to our definition there"}.get(phase, "the outline is exact")
    if call.tool == "ls" and "split" in kinds:
        return "a capped search cannot be trusted, and the listing lets me split it" + (" (it also tells me where the imported package lives)" if "module_path" in kinds else "")
    if call.tool == "ls" and "module_path" in kinds:
        return "the listing settles whether the import is a module, a package, or not here at all"
    if call.tool == "ls" and "submodule" in kinds:
        return "a package that does not bind the name could still have a submodule called that"
    if call.tool == "ls":
        return "a capped search cannot be trusted, and the listing lets me split it"
    if call.tool == "grep":
        pc = pattern_class(call.args[0])
        if pc == "DEF":
            return "that shows where the definition lives and whether the name is reused"
        return "the search has to be complete before I can call the set final"
    if call.tool == "read":
        return f"whether `{name}` is in it decides if the star import carries the name"
    if call.tool == "members":
        return "only its own members tell me whether it overrides"
    if call.tool == "calls":
        return "the name is ours there, so each call site counts"
    return choice.provenance


def intent(choice, ranked, K, items, name, phase, rng, hedges_out):
    items_by_key = {it.key: it for it in items}
    call = choice.call
    fc = sorted(choice.forecast().items(), key=lambda kv: (-kv[1], kv[0]))
    top_label, top_p = fc[0]
    verb = rng.choice(["Next I will", "Let me", "I'll"])
    # a filtered outline of a module whose import line the task already gave: say what it is for
    given_from = None
    if call.tool == "symbols" and len(call.args) > 1:
        for ln, bs in K.stmts.get(call.args[0], {}).items():
            for b in bs:
                if b.name == call.args[1] and b.kind == "from" and K.first_seen.get(call.args[0]) == "task":
                    given_from = (ln, b.src)
    if given_from is not None:
        w = hedge(top_p)
        hedges_out.append({"outcome": top_label, "word": w, "p": [top_p.numerator, top_p.denominator]})
        s = (f"{verb} check `{call.args[0]}` for any other binding of `{call.args[1]}` besides the import on line {given_from[0]}; "
             f"{w} the import is the only one, and then `{given_from[1]}` is the place to follow.")
        runner = next((c for c in ranked if c is not choice), None)
        return s
    s = f"{verb} {describe_call(call, name, K, items_by_key, choice.serves)}; {why(choice, K, items_by_key, phase, name)}."
    if call.tool == "symbols" and top_label == "missing":
        # a probe the policy itself expects to miss: say why it is still worth a call
        w = hedge(top_p)
        hedges_out.append({"outcome": top_label, "word": w, "p": [top_p.numerator, top_p.denominator]})
        nxt = choice.plan.get("missing")
        follow = f"; if so, I will {describe_call(nxt, name, K, items_by_key, set())}" if nxt not in (None, "done", "continue") else ""
        s += f" {w[0].upper() + w[1:]} the file is not there, but a miss costs one call and rules that location out{follow}."
        return s
    # expectation for the most likely outcome, hedged
    phrase = OUTCOME_PHRASE.get((call.tool, top_label))
    if phrase and top_p < Fraction(199, 200):
        w = hedge(top_p)
        hedges_out.append({"outcome": top_label, "word": w, "p": [top_p.numerator, top_p.denominator]})
        s += f" {w[0].upper() + w[1:]} {phrase}."
    # contingencies for the other outcomes; branches that lead to the same call are merged
    groups = {}
    order = []
    for label, p in fc[1:]:
        if p < Fraction(1, 50):
            continue
        nxt = choice.plan.get(label)
        key = nxt if isinstance(nxt, str) or nxt is None else nxt.key()
        if key not in groups:
            groups[key] = (nxt, [])
            order.append(key)
        groups[key][1].append(OUTCOME_PHRASE.get((call.tool, label), label))
    conts = []
    for key in order[:2]:
        nxt, phrases = groups[key]
        ph = " or ".join(phrases[:2])
        if nxt == "done":
            conts.append(f"if {ph}, that finishes it")
        elif nxt == "continue" or nxt is None:
            conts.append(f"if {ph}, I follow whatever it opens up")
        else:
            conts.append(f"if {ph}, I will {describe_call(nxt, name, K, items_by_key, set())}")
    if conts:
        joined = "; ".join(conts)
        s += " " + joined[0].upper() + joined[1:] + "."
    # alternative: only when it is close but not a coin flip, or of a different kind
    runner = next((c for c in ranked if c is not choice), None)
    if runner is not None and runner.v2 is not None and choice.v2 is not None:
        close = runner.v2 <= choice.v2 * Fraction(23, 20) and runner.v2 != choice.v2
        if close or (runner.call.tool != call.tool and runner.v2 != choice.v2):
            reason = runner_reason(choice, runner)
            s += f" I could {describe_call(runner.call, name, K, items_by_key, runner.serves)} instead, but {reason}."
    return s


def runner_reason(choice, runner) -> str:
    if runner.p_cap > choice.p_cap + Fraction(1, 10):
        return "it is more likely to hit the cap"
    if len(runner.serves) < len(choice.serves):
        return "it settles less"
    if runner.spawned > choice.spawned:
        return "it tends to open more follow-up work"
    if runner.v2 == choice.v2:
        return "it is a coin flip and I am keeping to the plan"
    return "it costs more calls in expectation"


# ---------------------------------------------------------------------------
# Assembly
# ---------------------------------------------------------------------------

def opening(task, chain, K, rng) -> str:
    g = task["given"]
    first = task["chain"][0]["op"]
    last = task["chain"][-1]["op"]
    if first == "resolve":
        s = f"I need to find what `{g['name']}` really is in `{g['module']}`: line {g['line']} imports it from `{g['spec']}`, so the definition is at least one hop away."
    else:
        s = f"Starting from the definition of `{g['name']}` at `{g['def_path']}:{g['def_line']}`."
    goal = {"resolve": "", "importers": " Then I have to find every module-level import of that definition, which means a complete search, not a sample.",
            "subclasses": " Then I need every class that derives from it, checking that each base name really points at this definition.",
            "callers": " Then every real call site of it, which means checking what the name refers to in each file that mentions it.",
            "not_overriding": f" Then, among its subclasses, the ones that do not define `{task['chain'][-1].get('method', 'the method')}` themselves.",
            "expose": " Then I have to propose the one-line import that exposes it from the package."}[last]
    return s + goal


PHASE_TRANSITION = {
    "importers": "That settles the definition; now the imports of it.",
    "subclasses": "That settles the definition; now its subclasses.",
    "callers": "That settles the definition; now its call sites.",
    "not_overriding": "That is the full set of subclasses; now which of them lack the method.",
    "expose": "That settles the definition; now the package that should expose it.",
}


def render_thought(step, K, chain, items, choice, ranked, new_facts, adherence, seed, name, task, prev_call, surprise,
                   prev_phase=None, prev_name=None, prev_served=()):
    rng = _rng(seed, step)
    state = chain.state(K)
    phase = state["phase"]
    hedges = []
    paras = []
    if step == 1:
        paras.append(opening(task, chain, K, rng))
    else:
        obs = observe(new_facts, K, prev_name or name, prev_phase or phase, rng, prev_call, prev_served)
        realized_cap = bool(new_facts) and any(f.kind in ("grep", "outline", "listing") and (f.data.get("capped") or f.data.get("complete") is False) for f in new_facts)
        if surprise is not None and surprise < Fraction(1, 10) and obs and not realized_cap:
            obs[0] = rng.choice(["Not what I expected: ", "Huh: ", "Interesting: "]) + obs[0][0].lower() + obs[0][1:]
        if prev_phase is not None and phase != prev_phase:
            obs.append(PHASE_TRANSITION.get(phase, ""))
        elif adherence and adherence.get("status") == "deviated":
            obs.append("That changes the plan.")
        paras.append(" ".join(o for o in obs if o) if obs else "That did not tell me anything new.")
    st = status(chain, state, K, name, step, items, rng)
    if st and (step == 1 or step % 3 == 0 or phase == "resolve" or (new_facts and new_facts[-1].kind in ("outline", "members", "calls"))):
        paras.append(st)
    if len(items) > 4 and step % 4 == 0:
        descs = [it.desc for it in items[:3]]
        paras.append("Still open: " + "; ".join(descs) + f"; and {len(items) - 3} more.")
    if choice is not None:
        paras.append(intent(choice, ranked, K, items, name, phase, rng, hedges))
    return "\n\n".join(paras), hedges


def render_final(task, answer, stopped, steps, hindsight, chain, K) -> str:
    if stopped != "certificate":
        return f"I have to stop here without a complete answer: {stopped}. What is still open is listed in the sidecar."
    if answer.get("stuck"):
        return f"This chain cannot continue: {answer['stuck']}."
    parts = []
    for st in answer["steps"]:
        op, out = st["op"], st["output"]
        if op == "resolve":
            parts.append(f"`{task['given']['name']}` is the {out.get('detail') or 'definition'} at `{out['path']}:{out['line']}`.")
        elif op == "importers":
            parts.append(f"{len(out)} module-level import statements bring in this definition: " + ", ".join(f"`{x}`" for x in out[:10]) + (f" and {len(out) - 10} more" if len(out) > 10 else "") + ".")
        elif op == "subclasses":
            parts.append(f"{len(out)} classes derive from it directly: " + ", ".join(f"`{x.split(':')[-1]}` (`{':'.join(x.split(':')[:2])}`)" for x in out[:8]) + (f" and {len(out) - 8} more" if len(out) > 8 else "") + ".")
        elif op == "callers":
            mods = sorted({x.split(":")[0] for x in out})
            parts.append(f"{len(out)} call sites in {len(mods)} modules: " + ", ".join(f"`{x}`" for x in out[:10]) + (f" and {len(out) - 10} more" if len(out) > 10 else "") + ".")
        elif op == "not_overriding":
            parts.append(f"{len(out)} of the subclasses do not define `{task['chain'][-1]['method']}` themselves: " + ", ".join(f"`{x.split(':')[-1]}`" for x in out) + "." if out else f"Every subclass defines `{task['chain'][-1]['method']}` itself.")
        elif op == "expose":
            if out.get("patch"):
                pkg = out["patch"]["path"].rsplit("/", 1)[0].split("/")[-1]
                nm = out["patch"]["append"].rsplit(" ", 1)[-1]
                parts.append(f"Patch: append `{out['patch']['append']}` to `{out['patch']['path']}`. The package does not bind `{nm}` today and is not dynamic, so after that line `from {pkg} import {nm}` resolves to the definition.")
            else:
                parts.append(f"No safe patch: {out.get('reason')}.")
    # counterexamples worth a word
    cert = chain.certificate(K)
    for c in cert:
        if c.get("kind") == "forall" and c.get("counterexamples"):
            ex = c["counterexamples"][:2]
            parts.append("Ruled out along the way: " + "; ".join(f"`{r[1] or r[0]}` ({r[3]})" for r in ex) + ".")
            break
    unneeded = [i for i, needed in hindsight.items() if not needed]
    if unneeded:
        parts.append(f"Looking back, {len(unneeded)} of {len(steps)} calls did not end up mattering (step{'s' if len(unneeded) > 1 else ''} {', '.join(map(str, unneeded))}).")
    else:
        parts.append(f"Looking back, all {len(steps)} calls were needed.")
    return " ".join(parts)
