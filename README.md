# pgc: programmatic, verifiable coding traces with a computed decision policy

A demo of the idea in [docs/smart-policies-brainstorm.md](docs/smart-policies-brainstorm.md):
generate agentic coding traces (thought, read-only tool call, response, repeated) over real
repositories, where every thought is rendered from a solver's typed state and every claim is
machine-checked, and where the choice of the next call is **computed** (a cap-aware
contingency search over open sub-goals) rather than hard-coded.

The oracle is static analysis, not commit history. The setter, the checker and the agent share
one resolver with a declared semantics (see the docstring of `pgc/analysis.py`); the agent runs it
over partial knowledge and gets back *needs* instead of guesses, so it can never conclude more
than the oracle would.

## What the demo shows

`demo/report.md` summarises one run over 8 real repositories (pinned commits in
`scripts/fetch_corpus.sh`), 30 tasks set by the analyzer, priors fit leave-one-out:

- every trace replays bit-identically from its logged responses;
- every world claim in every trace verifies against the snapshot (about 2000 checks);
- 29 of 30 tasks end with a certificate that equals the oracle's answer (one hits the budget);
- forecasts, plans, plan adherence and hindsight are all typed and checked.

Each trace in `demo/traces/*.md` shows, per step: the prose thought, the call, the response, and a
sidecar with the open items, every candidate call with its score and forecast, the plan per
outcome, the facts extracted, and adherence to the previous plan.

## Task families

- **resolve**: which definition does the name bound by this import resolve to (re-export chains,
  star imports with `__all__`, decoys of the same name).
- **cover**: every module-level import statement that imports a given definition, with a
  completeness proof under the grep cap (splitting capped scopes by directory).
- **composite**: resolve, then cover the result (20 to 40 calls).

## Layout

| Module | Role |
|---|---|
| `pgc/snapshot.py` | pinned snapshot; deterministic capped tools `ls`, `grep`, `read`, `symbols` |
| `pgc/analysis.py` | the declared semantics; index and resolver shared by setter, checker and agent |
| `pgc/knowledge.py` | what the agent has seen, as typed facts; partial-knowledge `Knowledge` |
| `pgc/goals.py` | goal state machines: open needs, certificates, answers |
| `pgc/prior.py` | priors fit on held-out repositories, stored as exact rationals |
| `pgc/policy.py` | grounded candidates, outcome model, depth-2 contingency search |
| `pgc/render.py` | prose from the typed delta |
| `pgc/runner.py` | the loop, live or replay; trace format; hindsight table |
| `pgc/verify.py` | replay, world checks, adherence, calibration |
| `pgc/setter.py` | task generation with full access; skeletons, quotas, floors |
| `pgc/cli.py` | `python -m pgc.cli demo ...` |

## Run

```
scripts/fetch_corpus.sh corpus
python -m pgc.cli demo --corpus corpus --out demo --per-repo 4 --seed 0 --budget 40
python tests/test_basic.py
```

Standard library only (Python 3.11).
