# pgc: programmatic, verifiable coding traces with a computed decision policy

Generates agentic coding traces (thought, read-only tool call, response, repeated) over real
repositories, where every thought is rendered from a solver's typed state, every claim is
machine-checked, and the choice of the next call is **computed** by a cap-aware contingency
search over open obligations rather than hard-coded.

Two documents explain the thinking: [docs/smart-policies-brainstorm.md](docs/smart-policies-brainstorm.md)
(the original brainstorm) and [docs/design.md](docs/design.md) (the design as built, after merging a
second proposal based on an obligation algebra).

## What the demo shows

`demo/report.md` summarises one run over 8 real repositories (pinned commits in
`scripts/fetch_corpus.sh`), 48 tasks composed by the setter from six operations, priors fit
leave-one-out. In that run every trace replays bit-identically from its logged responses, every
world claim verifies against the snapshot (about 2300 checks), every certificate equals the
oracle's answer, and the hedge words in the prose match the probabilities they stand for.

Each trace in `demo/traces/*.md` shows per step the thought, the call, the response, and a sidecar
with the open obligations, every candidate call with its score and forecast, the plan per outcome,
the facts extracted, the hedges used, and adherence to the previous plan.

## The obligation algebra

Tasks are chains of typed operations; each step's output is the next step's input.

| Operation | Output | Certificate |
|---|---|---|
| `resolve(module, name)` | definition | witness chain through re-exports and star imports |
| `importers(definition)` | module-level import statements | coverage of the tree under the grep cap, one verdict with a reason per candidate |
| `subclasses(definition)` | classes | coverage plus resolution of every base name, dotted bases included |
| `callers(definition)` | call sites | coverage plus, per module, what the bare name refers to; call sites are scope-exact |
| `not_overriding(classes, method)` | classes | one members lookup per class |
| `expose(definition, package)` | one-line patch | precondition facts; the patch is verified by re-indexing an in-memory copy |

Universal claims are discharged by coverage plus a verdict for every candidate (the failing ones are
the counterexamples); existential claims by witnesses. The setter, the checker and the agent share one
resolver with a declared semantics (`pgc/analysis.py`); the agent runs it over partial knowledge and
gets back *needs* instead of guesses, so it cannot conclude more than the oracle would.

## Tools available to the agent

`ls`, `grep`, `read`, `symbols(path[, name])` (module-level outline with class bases), `members(path,
class)`, `calls(path, name)` (call sites of the module-level binding, scope-exact). All deterministic,
all capped, over a pinned snapshot.

## Layout

| Module | Role |
|---|---|
| `pgc/snapshot.py` | pinned snapshot; deterministic capped tools |
| `pgc/analysis.py` | declared semantics; index and resolver shared by setter, checker and agent |
| `pgc/knowledge.py` | what the agent has seen, as typed facts with provenance; partial-knowledge resolver |
| `pgc/obligations.py` | the algebra: Resolve, Importers, Subclasses, Callers, NotOverriding, Expose, Chain |
| `pgc/prior.py` | priors fit on held-out repositories, stored as exact rationals |
| `pgc/policy.py` | grounded candidates, cap-aware outcome model, depth-2 contingency search |
| `pgc/render.py` | thoughts in an engineer's voice; hedge words recorded with their probabilities |
| `pgc/runner.py` | the loop, live or replay; trace format; hindsight with a grounding cascade |
| `pgc/verify.py` | replay, world checks, verdict checks, patch re-indexing, hedge bands, calibration |
| `pgc/setter.py` | composition of operations into tasks; skeleton cells, quotas, omniscient floors |
| `pgc/cli.py` | `python -m pgc.cli demo ...` |

## Run

```
scripts/fetch_corpus.sh corpus
python -m pgc.cli demo --corpus corpus --out demo --per-repo 6 --seed 0 --budget 40
python tests/test_basic.py
```

Standard library only (Python 3.11).
