# Design as built

This note maps the merged design onto the code. It supersedes the task-family
description in the brainstorm; the four properties (grounded, reproducible,
checkable, read-only capped tools) and the truth boundary are unchanged.

## Six components

1. **Adapter with declared semantics** (`analysis.py`). Python `ast` and `symtable`
   give module-level bindings with class bases, class members, and scope-exact call
   sites. The semantics is written in the module docstring and repeated in every task.
   Anything dynamic (module `__getattr__`, `globals()`, `sys.modules` writes, non-literal
   `__all__`, external star imports) makes a name ambiguous and the setter never asks
   about it. Claims are syntactic: a subclass is a class statement whose base resolves to
   the definition; a call site is a `name(...)` whose bare name refers to the module-level
   binding.

2. **Obligation solver shared with the oracle** (`analysis.resolve_name`,
   `obligations.py`). One resolver serves the setter (full index), the checker (full
   index) and the agent (partial knowledge). Where knowledge is missing it returns a
   `Need`; the agent's obligations turn needs into calls. The agent has no reasoning code
   path of its own beyond parsing tool output into typed facts, so it cannot over-conclude.

3. **Acquisition planner with held-out priors** (`policy.py`, `prior.py`). Candidate calls
   come from a grounded grammar (only names seen in the task or in responses, plus paths
   constructed from seen module specs and roots). Each candidate has an outcome
   distribution over a coarse partition (definition / re-export / star / none / missing /
   cap, or zero / hits / cap) from priors fit on the other repositories. A depth-2 search
   over the abstract state of open items picks the call, names a plan per outcome, and
   keeps the previous plan when scores tie. Item costs and outcome effects use the same
   conditional distribution, so every outcome nets exactly the call's cost and discovering
   work is never penalised relative to learning nothing.

4. **Setter with floors and quotas** (`setter.py`). Operations compose under types:
   resolve → target; target → importers, subclasses, callers, expose; subclasses →
   not_overriding. Each chain carries the oracle answer per step, a skeleton cell
   (hops, decoys, aliases, star imports, importer counts, false-positive modules, and so
   on), and an omniscient floor. Selection is one task per cell with family quotas,
   decided before any run. Private names, dynamic modules, capped-listing coverage and
   floors above the budget are excluded.

5. **Checker with five properties** (`verify.py`). Bit-identical replay of every typed
   output and every thought; world checks of every fact against the snapshot and index;
   every statable resolution, module path and export compared with the oracle; every
   verdict of a universal claim compared with oracle membership; the final answer compared
   with the oracle (a proposed patch is applied to an in-memory copy and the snapshot
   re-indexed); plan adherence; hedge words checked against their probability bands;
   calibration pooled over all steps.

6. **Renderer for world and decision claims** (`render.py`). Observation, status, intent.
   Names come from the task or responses; internals never appear; probabilities appear as
   hedge words whose bands are recorded in the sidecar; branches of the plan that lead to
   the same call are merged; a probe the policy expects to miss says why it is still worth
   a call; the hindsight sentence uses a grounding cascade so a read is not credited while
   the outline that made it possible is dropped.

## What the run showed

Forty-eight tasks over eight repositories, six operations, all certified and verified.
Search at depth 2 and greedy at depth 1 mostly agree, so the value here is in the
outcome model and the obligation structure rather than lookahead depth. The largest
gaps to the omniscient floor come from star-import-heavy packages, where the declared
semantics requires checking each star source's exports; that is the semantics being
honest, not the policy being slow.

## Not done

A second language through a language server; call chains and reverse reachability as
operations; a language-model proposer for calls outside the grammar; distillation of the
search into a learned policy.
