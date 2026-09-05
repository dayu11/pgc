# Smart policies for programmatic thoughts

A brainstorm, written from the handoff brief alone. It proposes a
formulation, a boundary for how the truth may be used, a menu of policy
mechanisms with their verification, a worked step, a map of tasks and
corpora, a definition of "smart", and a first experiment.

Everything here keeps the four properties from the brief: thoughts are
grounded, reproducible and checkable, and the tools are read-only,
deterministic, capped, over a fixed snapshot.

## 0. Where this lands

Six positions. Each is argued in the sections that follow.

1. **A read-only task is identification under a belief.** It is a POMDP
   whose hidden state is the snapshot itself, and that state never
   changes. The agent's state is a version space over answers (named
   candidates plus an explicit "somewhere unseen" remainder) and a prior
   over the unseen parts, fit on other repositories. Actions come from a
   grounded grammar, so the action set is finite and every candidate call
   carries its own provenance.

2. **The decision half becomes a shallow contingency search.** Outcomes
   partition coarsely (hit, miss, capped), grounded actions number in the
   tens, horizons are short. A depth-2 or depth-3 search over the belief is
   cheap, and it produces exactly the objects a strong engineer narrates:
   the alternatives weighed, the forecast, the plan for each outcome, the
   surprise when the plan's branch is not the expected one.

3. **The truth boundary.** The snapshot may enter the trace through four
   channels only: logged responses, the setter who designs the task, the
   verifier who checks it, and priors fit on held-out repositories. It may
   never enter the choice of the next call. Rollouts against the target
   snapshot are leakage. The same rollouts against held-out snapshots are
   learning.

4. **Thoughts gain a second layer of claims.** World claims (what the
   snapshot contains) are checked against the snapshot, as before. Policy
   claims (belief, forecast, comparison, plan) are checked by replaying the
   seeded policy, by adherence (did the next call follow the plan), and at
   dataset scale by calibration (did the things called 70% likely happen
   about 70% of the time). Uncertainty words in prose stop being
   unverifiable.

5. **"Smart" means Bayes-optimal under a declared prior with a cost of
   being wrong, subject to explicability.** The cost of being wrong is what
   makes a confirming read rational. Explicability means the move must be
   justified by a handful of typed claims that the thought renders.
   Fewest calls in hindsight is a diagnostic (regret), not the objective.

6. **The setter chooses tasks where decisions matter.** Greedy is
   provably near-optimal for plain identification with unit costs, so the
   setter should pick the regimes where it is not: heterogeneous costs,
   calls that only become available after other calls, censored
   observations (caps), hard budgets. Definition-finding under truncating
   greps, caller-covering with completeness certificates, informed bisect
   over git history, and effective-config resolution are the natural first
   tasks.

## 1. Formulation

### 1.1 World, observation, state

- **World** `w`: the pinned snapshot (tree, contents, and optionally
  history). Fixed and hidden from the agent.
- **Observation** `o = T(a, w)`: the capped response to call `a`.
  Deterministic in `(a, w)`.
- **Agent state** `s_t`: the task text, the transcript
  `⟨(a_1, o_1), …, (a_t, o_t)⟩`, and three derived objects:
  - `F_t`, typed facts entailed by the transcript (the derivation half,
    as in the previous line of work);
  - `C_t`, the version space: hypotheses about the answer consistent with
    the transcript;
  - `B_t`, the belief: a distribution over `C_t` and over the unseen parts
    of `w` that matter for the remaining decisions.

The version space needs one device to be honest. Before a path has been
seen it cannot be a named candidate, yet the answer may lie there. So
`C_t` is `{named candidates} ∪ {remainder}`, where the remainder is the
hypothesis "the answer is somewhere I have not seen". Its mass comes from
the prior and shrinks as listings and uncapped greps cover the tree. It
is the thing that stands in for the parts of the repository the agent has
not seen, and the thought can name it plainly: "or somewhere not yet
listed, about one chance in five".

### 1.2 Actions: a grounded grammar

The action space is enormous (any path, any regex) and must be generated
rather than enumerated. A small grammar does it:

| Tool | Argument sources |
|---|---|
| `ls(dir)` | `dir` is the root, or a directory named in a response, or a proper prefix of a path named in a response |
| `read(path, start, count)` | `path` named in a response; `start` anchored to a line number seen in a response, or 1 |
| `grep(pattern, scope)` | `pattern = P(sym)` for a symbol from the task or a response and `P` from a fixed set of transformations; `scope` as for `ls` |
| `git log/show/grep(rev, …)` | `rev` named in a response, or a range endpoint |

Transformations `P` are a fixed list: the bare identifier, `\bclass S\b`,
`\bdef S\b`, import or class statements naming `S`, assignment to `S`,
call `S(`, attribute `.S`, case variants, and so on. Each candidate call
therefore carries its provenance ("pattern from the task's symbol, scope
from the listing at step 1"), which is both the grounding proof and the
first sentence of its justification. The candidate set is typically ten
to a hundred calls.

The grammar is also the place where a skilled engineer's cleverness gets
encoded: a pattern that matches "import or class statements only" is
what turns a grep that would cap into one that will not. New
transformations widen the policy without touching its verification.

### 1.3 Observation model under the belief

Given hypothesis `h ∈ C_t` and call `a`, the response is partly
determined by `h` (if `h` says the definition is at path `p`, then
`grep('\bclass S\b', root)` lists `p` among its hits, and `read(p)` shows
the statement) and partly by the rest of the repository (how many other
lines match). The model factors:

- an **outcome partition** per call, coarse on purpose: for a grep,
  `{no hit, target among ≤ cap hits, capped}`; for `ls`, `{contains a
  name of interest, does not, capped}`; for `read`, `{shows the expected
  statement, does not}`;
- a **count prior** for the part `h` does not determine: the number of
  matching lines given the pattern's specificity, the scope's estimated
  size (from listings so far) and corpus statistics of the identifier.
  The probability of a cap is the tail of that count distribution.

Caps are therefore not an edge case in the model. They are the third
outcome of every search call, and the reason a broader pattern is not
always the better one.

### 1.4 Cost and the price of being wrong

Cost per call is one unit, or the bytes returned (which rewards skimming
over reading whole files), or a mix. A terminal penalty `λ` for a wrong
final answer is added. With `λ` the stopping rule is decision-theoretic:
stop when the expected cost of one more call exceeds the expected
reduction in `λ × P(wrong)`. This is what makes a confirming read at 95%
belief rational, and what makes it irrational at 99.9% under a tight
budget. A strong engineer behaves this way, and the number that says so
is now typed.

### 1.5 Goal and certificate

A task is done when the solver can produce a **certificate** that the
oracle checks against the snapshot:

- identification: a singleton version space, plus the witness lines that
  entail it (the grep line that shows the statement, the `__init__` line
  that re-exports the name);
- covering: a set of uncapped observations whose scopes cover the
  required region, plus the matched lines;
- resolution (effective value, symbol binding): the chain of witnesses
  in precedence order.

The certificate is the typed form of the answer. A trace that stops
without one is a trace that gave up, and says so.

### 1.6 Why planning is cheap here

The world is static, observations are deterministic, the outcome
partition is coarse, the grounded action set is small, and horizons are
five to fifteen calls. A belief-space tree of depth 2 over 30 actions and
3 outcomes has a few thousand leaves. Deeper lookahead is available by
sampling. None of it touches the snapshot.

## 2. The truth boundary

The harness can execute any candidate call and see the true response.
The temptation is to let a planner look, then choose. The rule proposed
here:

> The policy is a function of the task, the transcript, a seed, and
> parameters `θ` fit with the target snapshot held out. Nothing else.

Four channels through which the truth legitimately reaches the trace:

1. **Responses.** Once a call is made, its response is seen and may be
   used for everything.
2. **The setter.** Whoever designs the task has full access and uses it
   to pick the target, the caps, the budget, and to reject tasks that are
   trivial or hopeless. Hints may not pass into the task text beyond what
   the task declares as given.
3. **The verifier.** Checks world claims against the snapshot after the
   fact.
4. **Held-out priors.** `θ` is fit on other snapshots. A leave-one-out
   manifest (hash of the training set per target) is part of the trace's
   metadata, so leakage is checkable.

Why the alternative poisons the data: a planner that chooses on the truth
produces a trace whose stated reasons are not its real reasons. Its
thoughts either cite unseen information (breaking groundedness) or
rationalize after the fact (breaking the link between reason and choice).
A model trained on it learns that the first grep always lands, not how
one figures out what to grep for. Filtering traces on success is the
milder version of the same disease: it skews stated confidences away from
the frequencies a reader would experience. Do not filter on outcome;
filter on the setter's difficulty criteria, which are decided before the
run.

Three uses of the truth that look like leakage but are not:

- **Hindsight reflection at the end of a trace.** A closing thought that
  says "call 3 was unnecessary: response 2 already ruled out its target"
  is grounded (everything is seen by then), reproducible (a function of
  the full transcript) and checkable. It teaches self-critique.
- **Offline counterfactual annotation.** After the trace is generated,
  the harness may execute the unchosen alternatives and record what they
  would have returned, in metadata only. This is supervision for learned
  value functions and a diagnostic for the comparison claims. It never
  enters a thought.
- **Regret measurement.** An omniscient policy's call count is a lower
  bound used to score traces, never to steer them.

Two subtleties:

- **Tie-breaking** between equally scored calls must be seeded, not
  truth-informed. It is the easiest place for leakage to hide.
- **Rollout machinery** is neutral. Monte Carlo rollouts against the
  target snapshot are leakage; identical rollouts against held-out
  snapshots, used to fit `θ`, are learning.

## 3. Policy mechanisms

A menu. Each entry gives the idea, what it narrates, how the narration is
verified, and where it shines. They compose.

### A. Version space with expected information gain, cap-aware

The greedy baseline done properly. Maintain `C_t`; for each grounded call
compute the expected reduction in entropy of `C_t` under the observation
model of 1.3, divided by cost; choose the best. The cap-aware count prior
is what separates this from a naive "grep the symbol" heuristic: it knows
that grepping a common name will truncate and settle nothing.

- Narrates: the candidate set with masses, the top two or three calls
  with their expected gain and cap probability, the winner.
- Verified: replay (`C_t`, gains and the argmax are bit-identical on
  re-run); world checks on the eliminations' witnesses.
- Shines: as the baseline every other mechanism is compared against, and
  as the leaf evaluation for the searches below.

### B. Contingency search (the recommended core)

Before each call, search the belief tree to depth 2 or 3 over the coarse
outcome partition and choose the call whose subtree has the lowest
expected cost-to-certificate. Publish the first level of the subtree as a
**plan**: for each outcome class, the next call.

- Narrates: "grep X first; one hit, confirm it; several, resolve the
  import instead of guessing; none, list the root; capped, split by
  directory". Exactly the shape of an engineer's stated intent.
- Verified: replay of the search (seeded, `θ`-parameterized); **plan
  adherence**, where the verifier checks that the actual next call is the
  branch prescribed for the actual outcome, or that a deviation is
  narrated with a typed reason; calibration of the outcome forecasts
  across the dataset.
- Shines: multi-hop tasks (the plan's branches are the hops), and any
  task with cap risk, where the search trades pattern breadth against
  truncation.

Plans make the trace honest in a strong sense: the agent commits, in
writing, before it looks. Surprise becomes a first-class, checkable
event: the outcome landed in a branch the forecast gave low mass.

### C. A* over proof obligations (for covering and certificates)

Reframe the goal as a set of open obligations. For "all call sites of
`f`": one obligation per uncovered scope, "show every match under this
scope with an uncapped grep". A capped grep leaves the obligation open
but records "at least `cap` matches here"; an `ls` splits an obligation
into children. The heuristic `h(state)` sums, over open obligations, the
estimated number of uncapped greps needed, from the count prior. A*
picks the call minimizing `g + h`.

- Narrates: "three scopes open: `src/` (estimated 35 matches, would cap,
  needs splitting), `tests/` (about 8, one grep), `docs/` (about 1, one
  grep). Listing `src/` first". Then, at the end, the certificate: the
  list of (scope, pattern, uncapped) observations that cover the tree.
- Verified: replay of `h` and the choice; the oracle checks the
  certificate for coverage and the match set for completeness.
- Shines: covering tasks, where completeness under caps is the whole
  difficulty and greedy tends to fire a capped grep at the root and
  learn little.

### D. Belief-space sampling with particle repositories

For deeper lookahead, replace the coarse outcome partition with sampled
completions of the unseen repository ("particles") and run candidate
calls against them for real. Particles come from the corpus (other repos
reweighted by how well they match the seen tree) or from a structural
completion model (typical contents of a `tests/` directory given the
`src/` listing). The chosen call is the one with the best average
cost-to-certificate over particles.

- Narrates: the same objects as B, with forecasts from particles.
- Verified: replay with the seed; the particle set is a deterministic
  function of the transcript and `θ`.
- Shines: long-horizon tasks (dependency-graph walks, multi-file
  resolution) where the coarse partition loses information.
- Caveat: particles that are whole real repositories rarely agree with
  the seen part. The structural completion model is the practical route,
  and it is a research item.

### E. Corpus-fit priors as typed forecasts

The count prior of 1.3 and the placement prior ("a top-level class named
`S` is defined in a module named like `S`, under the package that exports
it") are small models fit on held-out repositories. They are policy
parameters `θ`, versioned and hashed into the trace.

- Narrates: "expect two to five matches; one chance in ten of a cap". The
  prose carries coarse numbers; the sidecar carries exact ones; the
  checker verifies the prose rounds from the sidecar.
- Verified: replay of the forecast from `θ`; calibration audits over the
  unfiltered pool of traces; the leave-one-out manifest.
- Shines: everywhere. It is what gives the searches something to be
  smart about. It also gives an out-of-distribution detector for free:
  a repository where forecasts keep missing is one the prior does not
  understand, and the trace should say so.

### F. Two-policy contrast as narration

Run the greedy baseline (A) alongside the search (B or C). When they
disagree, the thought says so: "the direct move is to read `X`; under
the current candidates a grep for `Y` settles two of them at once and
costs the same. Taking the grep." Both policies are deterministic, so
both moves are reproducible.

- Verified: replay of both.
- Shines: as training signal. It teaches *why* the smart move is smart,
  at exactly the steps where it matters, and it costs nothing extra.

### G. Cap-splitting planner

A dedicated sub-policy for the moment after a truncation. The problem is
to choose a partition of the capped scope (by directory, by extension,
by pattern refinement) that covers it in the fewest expected calls, given
the seen tree and the count prior. It is a small set-cover with
estimated weights.

- Narrates: "50 matches, capped. Splitting by top-level directory:
  `src/` about 30, `tests/` about 15, `docs/` about 5; two or three calls
  should cover it. A narrower pattern (class statements only) would cover
  it in one but might miss definitions by assignment."
- Verified: replay; the oracle checks coverage of the resulting
  observations.
- Shines: every task, because caps are normal.

### H. Hindsight post-mortem

The closing thought, computed from the full transcript: which calls
contributed to the certificate, which were confirmations by design, which
were wasted, and what a two-call-shorter run would have looked like.

- Verified: for each call `i`, the verifier recomputes whether the
  certificate is entailed by the transcript without response `i`.
- Shines: as the one place regret-flavored reflection is honest.

### I. Legal non-determinism: a proposer and a chooser

If a language model is involved, keep it out of the justification. Let it
**propose** candidate calls (checked for groundedness and grammar
membership, logged verbatim) or **forecast** outcomes (logged, audited
for calibration like any prior). The programmatic solver chooses among
proposals and renders the reasons.

- Verified: legality of each proposal (grounded, well-formed); the choice
  and its reasons replay exactly given the logged proposals.
- Shines: widening the action grammar beyond fixed transformations
  without giving up verification. The grammar becomes a floor, not a
  ceiling.

### J. Distilling the search into a learned policy

Once traces exist, fit a fast policy on the search's decisions and the
counterfactual annotations from section 2. It is a new `θ`. Its outputs
are typed and seeded, so the same replay verifies it, and calibration
audits catch drift. This is expert iteration with a fully verifiable
expert, and it is the route to volume.

### K. Adversarial and curricular setting

The setter runs omniscient, greedy and search policies on candidate
tasks and keeps the tasks where search beats greedy by at least `k` calls
and the omniscient floor is at least `m`. Beyond that, an adversarial
setter chooses targets to maximize greedy's regret. Both are legitimate
uses of the truth (section 2) and both produce a curriculum in which the
decision half visibly matters. The selection statistics are logged per
task so that nobody mistakes the curriculum for the base rate.

## 4. What a smart step reads like

A worked fragment. Percentages are illustrative outputs of a prior, not
measurements.

**Task.** `app/main.py` contains `from ui import Widget`. Report the path
and line of the `class` statement that this name resolves to.

**Tools.** `ls(dir)` returns up to 40 entries. `grep(regex, dir)` returns
up to 20 lines as `path:line:text`. `read(path, start, count)` returns up
to 60 lines.

### Step 1

> Nothing seen yet beyond the task: the importing file `app/main.py`, the
> module name `ui`, the symbol `Widget`. No candidate file is named; the
> remainder is the whole tree. Two ways in. Resolving the import needs a
> listing first, since no `ui` path has been seen. Searching for the class
> statement directly can settle most of it in one call: I expect a single
> hit (about 55%), a few hits if fixtures or examples reuse the name
> (30%), none if the class is made some other way (10%), a cap only if
> `Widget` is a family name in a UI framework (5%). Listing the root
> settles nothing by itself. Grepping first. Plan: one hit, confirm it by
> reading around the line; several, resolve the import rather than guess;
> none, list the root and grep the bare name; capped, list the root and
> split by directory.

Sidecar (abridged):

```
seen:        task → {app/main.py, ui, Widget}
candidates:  named ∅ ; remainder 1.00
alternatives:
  grep('\bclass Widget\b', '.')   forecast {0: .10, 1: .55, 2..19: .30, cap: .05}   E[cost-to-certificate] 2.3
  ls('.')                          forecast —                                        E[cost-to-certificate] 3.4
choice:      grep('\bclass Widget\b', '.')      provenance: pattern ← task:Widget ; scope ← root
plan:        {1 → read(hit.path, hit.line-5, 15) ; 2..19 → resolve-import ;
              0 → ls('.') then grep('Widget', '.') ; cap → ls('.') then split}
```

Checks: groundedness (every name is in `seen`); replay (forecast,
expectations, choice, plan reproduce bit-identically). No world claims
yet.

**Response 1** (3 lines, under the cap):

```
docs/examples/custom.py:12:class Widget(ui.Widget):
src/ui/widget.py:41:class Widget(Component):
tests/fixtures/fake_widget.py:7:class Widget:
```

### Step 2

> Three `class Widget` statements in the tree, and the result is under the
> cap, so these are all of them. The outcome fell in the bucket I gave
> 30%. The docs example subclasses `ui.Widget`, so it uses the name rather
> than sourcing it; it stays a candidate only through the remote chance
> that `ui` re-exports it (2%). The fixture sits under `tests/`, outside
> any plausible `ui` package (8%). The strong candidate is
> `src/ui/widget.py:41` (85%), with 5% left for a `ui` module that binds
> `Widget` some other way. Per the plan, resolve the import. `src/ui` is
> now a seen directory, and `from ui import Widget` binds the attribute
> `Widget` of the package `ui`, so its `__init__` decides. Three ways to
> look. List `src/ui` and then read its `__init__.py`: two calls, certain.
> Grep the bare name under `src/ui`: one call if it stays under the cap,
> but a UI package uses `Widget` everywhere; I put the cap risk at 40%.
> Grep only import and class statements naming `Widget` under `src/ui`:
> cap risk 5%, and it shows the re-export and the definition at once.
> Taking the third. Plan: a `from .widget import Widget` line in
> `src/ui/__init__.py` confirms the chain, then read around line 41; no
> `__init__.py` among the hits, list `src/ui`; capped, fall back to the
> two-call route.

Sidecar (abridged):

```
facts:
  F1  all_class_statements('Widget', '.') = {docs/examples/custom.py:12, src/ui/widget.py:41,
      tests/fixtures/fake_widget.py:7}          witness: response 1, uncapped (3 < 20)      [world]
candidates:  src/ui/widget.py:41 .85 ; tests/fixtures/fake_widget.py:7 .08 ;
             docs/examples/custom.py:12 .02 ; remainder .05
surprise:    outcome bucket '2..19' had forecast .30      (log-loss 1.20 nats)
alternatives:
  ls('src/ui') → read('src/ui/__init__.py')                      E[cost] 2.0   P(cap) —
  grep('\bWidget\b', 'src/ui')                                    E[cost] 1.8   P(cap) .40
  grep('^(from|import) .*\bWidget\b|^class Widget\b', 'src/ui')   E[cost] 1.1   P(cap) .05
choice:      third   provenance: pattern ← P_import_or_class(task:Widget) ; scope ← prefix of response1:src/ui/widget.py
plan:        {re-export line in src/ui/__init__.py → read(src/ui/widget.py, 36, 15) ;
              no __init__.py among hits → ls('src/ui') ; cap → ls('src/ui') then read}
adherence:   step 2 follows plan(step 1)['2..19']   ✓
```

Checks: F1 against the snapshot (the oracle greps the whole tree and
compares); candidate masses, surprise, expectations and choice by replay;
adherence to the previous plan.

**Response 2** (3 lines, under the cap):

```
src/ui/__init__.py:3:from .widget import Widget
src/ui/panel.py:2:from .widget import Widget
src/ui/widget.py:41:class Widget(Component):
```

### Step 3

> Under the cap again: within `src/ui`, the only import or class
> statements naming `Widget` are the re-export at `src/ui/__init__.py:3`,
> a sibling import in `panel.py`, and the class at `widget.py:41`. So the
> `ui` package re-exports `Widget` from `.widget`, which defines it at
> line 41. This is the plan's re-export branch. Still open: whether
> `src/ui` is the package that `app/main.py` reaches, which needs `src` to
> be a source root. Every `class Widget` statement in the tree is
> accounted for, so any other `ui` package would have to bind the name by
> assignment or alias; the prior puts that at 3%. A read of the
> definition costs one call and rules out a match inside a string or a
> nested scope. Under the cost of being wrong, that check pays. Reading
> `src/ui/widget.py` lines 36 to 50.

Sidecar: fact F2 (the import-or-class statements under `src/ui`, witness
response 2 uncapped) and F3 (`ui` re-exports `Widget` from `.widget`,
derived from F2 by the import rule), both world claims; candidates
collapse to `src/ui/widget.py:41` at .97 with remainder .03; the stopping
computation shows one more call is worth it at the declared `λ`;
adherence to plan(step 2) holds.

**Response 3**: lines 36 to 50, with `class Widget(Component):` at line
41, column 0, followed by a docstring.

### Step 4 (final)

> Confirmed: line 41 of `src/ui/widget.py` opens `class
> Widget(Component):` at column 0, a top-level statement. Answer:
> `src/ui/widget.py:41`. Residual: 3% that `ui` resolves elsewhere; a
> source-root check would cost two or more calls, and the budget does not
> reward it. In hindsight: three calls against a floor of two. The read
> was a confirmation by design, not waste.

Sidecar: the certificate (`F1`, `F3`, and the read's witness line); the
post-mortem table (call 1 necessary, call 2 necessary, call 3
confirmation); the omniscient floor as metadata.

What to notice. Every uncertainty word has a number behind it. Every
comparison of moves is a replayable computation. The plan is written
before the look, and the verifier checks that the agent kept its word.
The two world claims that carry the answer (F1 and F3) are what the
oracle checks against the snapshot. Nothing in the thoughts required
seeing anything unseen.

## 5. Tasks, corpora, games

### 5.1 Where search beats greedy, and where it cannot

For plain identification with unit costs and uncensored observations,
greedy by information gain is within a logarithmic factor of optimal
(adaptive submodularity). Search buys little there, and a "smart" policy
would look no different from a greedy one. Search matters where the
assumptions break:

- **Heterogeneous costs.** Reading a 2000-line file versus a one-line
  grep; bytes as cost.
- **Enabling constraints.** A call becomes available only after another
  call names its argument (grounding). Multi-hop tasks are made of these.
- **Censored observations.** Caps turn "how broad a pattern" into a real
  trade-off with lookahead consequences.
- **Budgets.** A hard call budget below what greedy needs forces planning
  and makes budget pressure narratable.

Degenerate for this session's purpose: one-call tasks (read this file);
open-ended tasks with no version space (explain this module); tasks where
every call is equally informative; tasks where the only strategy is
enumeration.

### 5.2 A map

| Corpus | Task | Certificate | Why search is natural | Setter's game |
|---|---|---|---|---|
| Source tree | Which `class`/`def` does this name resolve to | Witness chain through imports | Multi-hop, cap risk on common names | Pick symbols whose bare name truncates but whose anchored pattern does not |
| Source tree | All call sites of `f` | Uncapped greps covering the tree | Covering under caps, heterogeneous scope sizes | Pick `f` with call density that caps at the root and splits unevenly |
| Source tree | Which tests exercise `f` | Chain of call witnesses | Indirection through helpers | Pick `f` reached only via fixtures |
| Git history | Which commit first introduced line `L` in `f` | Presence at `c`, absence at `parent(c)` | Bisect with informed probe choice from messages and touched paths | Choose lines that moved across renames; exclude pickaxe from the tool set |
| Git history | When was `f` renamed, and from what | Rename witness in a commit's tree diff | Interval search with priors from messages | Choose files with multi-step renames |
| Configuration | Effective value of setting `S` in environment `E` | Precedence chain of witnesses | Read highest precedence first; includes make hops | Layer defaults, env files, overrides; place the override where the prior least expects |
| Dependency lock | Which top-level dependency pulls in `p@v` | Edge chain | Graph walk with pruning | Choose deep transitive edges |
| Build/CI logs plus source | Which source line does the first failure point at | Log line plus source witness | Two corpora, caps on huge logs, windowed reads | Bury the failure past the first screen |
| Documentation plus source | Does the doc's default for flag `x` match the code | Two witnesses and a comparison | Two searches, one comparison | Choose flags whose defaults are set indirectly |

### 5.3 The bisect game, in one paragraph

An interval `[absent, present]` over the commit sequence. A naive bisect
probes the midpoint and needs `log2(N)` calls. An informed policy reads
the capped log for the interval, scores commits by a prior over message
tokens and touched paths ("add Widget class", touches `ui/widget.py`),
and probes the most likely commit and its parent first. The interval
claims are world claims (checked against history), the probe choice
replays, and the payoff over naive bisect is measurable per task. It is
the cleanest demonstration that a computed decision half is worth having.

### 5.4 Modified snapshots

The setter may plant a target in a real repository before pinning it (an
override in a config layer, a renamed file in history). The agent still
sees a read-only fixed snapshot, so the properties hold. The risk is
unrealistic artifacts; the mitigation is to prefer found targets over
planted ones and to log which is which.

## 6. What "smart" means, and how to measure it

Three candidate definitions from the brief, and a position.

- **Fewest calls in hindsight.** Unattainable without leakage. Keep it as
  regret, a diagnostic.
- **Fewest calls in expectation under honest uncertainty.** Principled and
  computable. On its own it can prefer gambles that no engineer would
  take, and it says nothing about whether the move can be explained.
- **The choices a skilled reader would make and could explain.** The real
  training target, but not by itself a computation.

Position: **smart = Bayes-optimal under a declared, held-out prior, with
a cost of being wrong, subject to an explicability budget.** The
explicability budget caps how many typed claims the justification may
need (say, five: the candidates, the forecast, the top alternative, the
reason it loses, the plan). A move whose justification does not fit is
not made, even if the search prefers it. That is a constraint a strong
engineer also lives under: they take moves they can explain.

Metrics, all computable from traces and their metadata:

| Metric | What it measures | Source |
|---|---|---|
| Expected calls under prior | The policy's own view of its efficiency | Replay |
| Realized calls, and regret versus the omniscient floor | Hindsight efficiency | Omniscient run in metadata |
| Calls versus greedy | Whether the search earned its keep | Two-policy run |
| Forecast calibration (expected calibration error, log-loss) | Whether stated uncertainty is honest | Unfiltered pool of traces |
| Plan adherence rate, and narrated deviations | Whether the agent keeps its word | Verifier |
| Certificate completeness, wrong-answer rate | Whether it finishes and finishes right | Oracle |
| Justification size | Explicability | Sidecar |
| Regret variance across repositories | Prior misspecification | Corpus |

A separate, non-verifiable side metric is worth keeping on a sample:
agreement of a strong engineer (human or model judge) with the chosen
move, as a check that the formal objective has not drifted from the
behavioral one.

## 7. Risks and how to handle them

- **Numbers in prose.** Thoughts full of "0.73 bits" read like logs.
  Render ordinal comparisons in prose ("more informative", "settles two
  at once", "cheaper"), put exact numbers in the sidecar, and have the
  checker verify the prose against the numbers.
- **Narrating the algorithm instead of the decision.** "I expanded 4,000
  nodes" is not a thought. Render the conclusions of the search: the
  alternatives, the choice, the plan.
- **Prior leakage.** Fit `θ` with the target held out and record the
  manifest. Watch for priors that memorize corpus-specific paths.
- **Outcome filtering.** Never filter traces on success. Audit
  calibration on the unfiltered pool even if a curated subset is
  published.
- **Confident and wrong.** A misspecified prior produces confident
  mistakes. The cost of being wrong forces confirmations; the
  out-of-distribution signal from repeated surprises should be narrated
  ("this repository does not follow the conventions I assumed").
- **A grammar too narrow to hold the clever move.** The fixed
  transformation set will miss things an engineer would try. Widen it
  over time, and consider the proposer (I) as the escape hatch.
- **Planted targets that look planted.** Prefer found targets; log
  provenance.

## 8. A first experiment

Scope small enough to run in a week, large enough to answer whether the
decision half can be computed.

1. **Corpus.** A few hundred Python repositories, pinned. Three tools
   (`ls`, `grep`, `read`) with caps of 40 entries, 20 lines, 60 lines.
2. **Tasks.** Definition resolution (as in section 4) and caller
   covering. Targets found by the setter with full access; the setter
   keeps tasks whose omniscient floor is at least 2 and whose grounded
   depth is at least 2 hops.
3. **Priors.** A count prior for grep matches (features: pattern
   transformation, scope size from listings, identifier frequency in the
   held-out corpus) and a placement prior for definitions. Leave-one-out
   by repository.
4. **Policies.** Greedy EIG (A), depth-2 contingency search (B) with the
   cap-splitting planner (G), A* over obligations (C) for covering.
   Omniscient in metadata. Seeded tie-breaking.
5. **Rendering.** Five-slot thoughts: settled, ruled out (with witness),
   open, expect, next (and why not the runner-up). Sidecar per step.
6. **Verification.** Replay for policy claims, oracle for world claims,
   adherence for plans, calibration over the pool, post-mortem check.
7. **Questions to answer.** Does B beat A by at least one call on the
   setter's tasks, and by how much on the unfiltered pool? Are forecasts
   calibrated? How often does the plan get followed? Do the traces read
   as the reasoning of a careful engineer on a blind sample?

Expected result, stated so it can be wrong: search beats greedy mainly
through cap avoidance (choosing anchored patterns and scoped greps) and
through hop ordering, by one to two calls on the curated tasks, and by
much less on the pool. If that is what the numbers say, the setter's
curriculum is where the value lives.

## 9. Open questions

- How rich should the grammar be before a proposer is worth its
  non-determinism?
- What is the right cost: calls, bytes, or a mix, and does the choice
  change the traces' character?
- How should the remainder's mass be estimated for trees only partly
  listed, and how should that estimate be narrated without false
  precision?
- Can particle completion (D) be made deterministic and cheap enough to
  replace the coarse outcome partition for long tasks?
- Should traces include deliberately budget-starved runs, where the agent
  must stop with an honest, typed statement of residual uncertainty?
- How do several sub-goals in one task (find the definition, then all
  callers) share a belief and a budget, and what does the hand-off
  between them look like in a thought?
