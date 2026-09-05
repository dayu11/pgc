# Demo report: smart policies for programmatic thoughts

Corpus: 8 real repositories, pinned by commit (see manifest below). Tasks set by static analysis with full access; priors fit leave-one-out (each repository's prior is fit on the other 7). Seed 0, budget 40 calls.

## Headline numbers

| Metric | Value |
|---|---|
| Tasks | 30 |
| Finished with a certificate (search policy) | 29/30 |
| Finished with a certificate (greedy baseline) | 29/30 |
| Final answer equals the oracle | 29/30 |
| Traces that replay bit-identically | 30/30 |
| Traces whose every world claim verifies | 30/30 (1991 checks) |
| Calls: omniscient floor / search / greedy | 308 / 417 / 419 |
| Steps by plan adherence | deviated 27, first 30, followed 273, open-ended 71, replanned 7, unplanned 9 |

## Reading the numbers

- Search (depth 2) and the greedy baseline (depth 1) choose the same call at almost every step here; where they differ the gap is one call. On these families the gains over a naive policy come from the cap-aware outcome model and the item structure, not from lookahead depth.
- The omniscient floor counts one outline per module that must be closed plus the greps and listings needed for coverage; it ignores nothing the agent could have skipped, so calls above it are the price of honest uncertainty (probing a module that turns out external, listing a directory before probing).
- Calibration is measured on every step of every trace, unfiltered. The top bin is over-confident: outline forecasts of about 0.95 realized less often, mostly because probed module files were missing or names were unbound more often than the prior expected.
- `unplanned` steps are outcomes outside the forecast classes (an error response); `replanned` steps follow an outcome that opened new items, so the previous plan named a call that no longer applied.

## By family

| Family | Tasks | Certificates | Floor | Search calls | Greedy calls |
|---|---|---|---|---|---|
| composite | 13 | 12 | 206 | 266 | 267 |
| cover | 6 | 6 | 78 | 109 | 109 |
| resolve | 11 | 11 | 24 | 42 | 43 |

## Calibration of forecasts (search policy)

Each step forecasts a distribution over outcome classes before its call. Rows pool (step, class) pairs by forecast probability.

| Forecast bin | Pairs | Mean forecast | Realized frequency |
|---|---|---|---|
| 0.0-0.2 | 687 | 0.04 | 0.12 |
| 0.2-0.4 | 106 | 0.24 | 0.07 |
| 0.4-0.6 | 26 | 0.49 | 0.50 |
| 0.6-0.8 | 38 | 0.74 | 0.76 |
| 0.8-1.0 | 355 | 0.92 | 0.78 |

## Diversity

| Repository | Pool (resolve/cover/composite) | Skeleton cells in pool | Chosen | Prior hash |
|---|---|---|---|---|
| attrs | 98/13/33 | 18 | 4 | df2023878106d754 |
| black | 363/14/88 | 10 | 2 | 55c929686ca1d56a |
| click | 61/7/18 | 5 | 4 | 93954b294cf7311e |
| flask | 180/16/97 | 33 | 4 | b7977e45b67266d2 |
| httpx | 187/11/55 | 8 | 4 | d99074a5d38bc2d8 |
| pytest | 867/69/586 | 46 | 4 | 0140c5bd99319f8c |
| requests | 204/18/72 | 18 | 4 | 89d4e155c6e8b2e4 |
| rich | 947/55/529 | 22 | 4 | 6d694b621dbf13a2 |

Distinct skeleton cells among chosen tasks: 27 of 30 tasks.

## Tasks

| Task | Family | Floor | Search | Greedy | Stopped | Replay | World | Cell |
|---|---|---|---|---|---|---|---|---|
| [attrs-composite-7836bbf5](traces/attrs-composite-7836bbf5.md) | composite | 19 | 25 | 25 | certificate | ok | ok | alias=False|decoys=0|family=composite|from_init=False|hops=2|importers=5|relative=False|root_caps=False|star=False |
| [attrs-composite-8719a906](traces/attrs-composite-8719a906.md) | composite | 19 | 23 | 23 | certificate | ok | ok | alias=False|decoys=1|family=composite|from_init=False|hops=3|importers=5|relative=False|root_caps=False|star=False |
| [attrs-cover-4a8ce702](traces/attrs-cover-4a8ce702.md) | cover | 19 | 25 | 25 | certificate | ok | ok | decoy_sources=2+|family=cover|importers=5|root_caps=False|sources=2-3|star=False |
| [attrs-resolve-b134577c](traces/attrs-resolve-b134577c.md) | resolve | 2 | 2 | 2 | certificate | ok | ok | alias=False|decoys=1|family=resolve|from_init=False|hops=2|relative=True|star=False |
| [black-resolve-1daa42f9](traces/black-resolve-1daa42f9.md) | resolve | 2 | 5 | 5 | certificate | ok | ok | alias=False|decoys=2+|family=resolve|from_init=True|hops=2|relative=False|star=False |
| [black-resolve-93dc74fa](traces/black-resolve-93dc74fa.md) | resolve | 2 | 5 | 5 | certificate | ok | ok | alias=False|decoys=2+|family=resolve|from_init=False|hops=2|relative=False|star=False |
| [click-composite-459950f2](traces/click-composite-459950f2.md) | composite | 8 | 10 | 10 | certificate | ok | ok | alias=False|decoys=0|family=composite|from_init=False|hops=2|importers=5|relative=False|root_caps=False|star=False |
| [click-composite-ca81075c](traces/click-composite-ca81075c.md) | composite | 8 | 10 | 10 | certificate | ok | ok | alias=False|decoys=0|family=composite|from_init=False|hops=2|importers=5|relative=True|root_caps=False|star=False |
| [click-cover-1ae0c26a](traces/click-cover-1ae0c26a.md) | cover | 6 | 9 | 9 | certificate | ok | ok | decoy_sources=0|family=cover|importers=5|root_caps=False|sources=1|star=False |
| [click-resolve-4cf9b346](traces/click-resolve-4cf9b346.md) | resolve | 2 | 5 | 5 | certificate | ok | ok | alias=False|decoys=0|family=resolve|from_init=False|hops=2|relative=False|star=False |
| [flask-composite-6d6303d9](traces/flask-composite-6d6303d9.md) | composite | 16 | 15 | 15 | certificate | ok | ok | alias=False|decoys=1|family=composite|from_init=True|hops=3|importers=6-12|relative=False|root_caps=False|star=False |
| [flask-composite-9bc1d97c](traces/flask-composite-9bc1d97c.md) | composite | 20 | 18 | 18 | certificate | ok | ok | alias=False|decoys=0|family=composite|from_init=False|hops=3|importers=6-12|relative=False|root_caps=True|star=False |
| [flask-resolve-069472a0](traces/flask-resolve-069472a0.md) | resolve | 2 | 2 | 2 | certificate | ok | ok | alias=False|decoys=1|family=resolve|from_init=True|hops=2|relative=True|star=False |
| [flask-resolve-f8d5cd59](traces/flask-resolve-f8d5cd59.md) | resolve | 3 | 5 | 5 | certificate | ok | ok | alias=False|decoys=1|family=resolve|from_init=False|hops=3|relative=False|star=False |
| [httpx-composite-3652b9a2](traces/httpx-composite-3652b9a2.md) | composite | 20 | 38 | 38 | certificate | ok | ok | alias=False|decoys=0|family=composite|from_init=False|hops=2|importers=6-12|relative=True|root_caps=False|star=False |
| [httpx-composite-b2ad6580](traces/httpx-composite-b2ad6580.md) | composite | 22 | 40 | 40 | budget | ok | ok | alias=False|decoys=0|family=composite|from_init=False|hops=2|importers=6-12|relative=True|root_caps=True|star=False |
| [httpx-cover-48c28c46](traces/httpx-cover-48c28c46.md) | cover | 18 | 37 | 37 | certificate | ok | ok | decoy_sources=2+|family=cover|importers=5|root_caps=False|sources=1|star=True |
| [httpx-resolve-81b1af7d](traces/httpx-resolve-81b1af7d.md) | resolve | 2 | 3 | 3 | certificate | ok | ok | alias=False|decoys=0|family=resolve|from_init=False|hops=2|relative=True|star=False |
| [pytest-composite-4d6e4844](traces/pytest-composite-4d6e4844.md) | composite | 19 | 20 | 20 | certificate | ok | ok | alias=False|decoys=0|family=composite|from_init=False|hops=2|importers=13+|relative=False|root_caps=False|star=False |
| [pytest-composite-984fcea8](traces/pytest-composite-984fcea8.md) | composite | 24 | 32 | 32 | certificate | ok | ok | alias=False|decoys=0|family=composite|from_init=False|hops=2|importers=13+|relative=False|root_caps=True|star=False |
| [pytest-resolve-09b34f57](traces/pytest-resolve-09b34f57.md) | resolve | 2 | 5 | 5 | certificate | ok | ok | alias=True|decoys=0|family=resolve|from_init=True|hops=2|relative=False|star=False |
| [pytest-resolve-426f0f0a](traces/pytest-resolve-426f0f0a.md) | resolve | 2 | 2 | 2 | certificate | ok | ok | alias=False|decoys=0|family=resolve|from_init=True|hops=2|relative=True|star=False |
| [requests-composite-a66a6553](traces/requests-composite-a66a6553.md) | composite | 7 | 11 | 11 | certificate | ok | ok | alias=True|decoys=0|family=composite|from_init=False|hops=2|importers=5|relative=False|root_caps=False|star=False |
| [requests-composite-ad564edd](traces/requests-composite-ad564edd.md) | composite | 7 | 8 | 9 | certificate | ok | ok | alias=False|decoys=0|family=composite|from_init=False|hops=2|importers=5|relative=False|root_caps=False|star=False |
| [requests-cover-dcdf02a7](traces/requests-cover-dcdf02a7.md) | cover | 10 | 13 | 13 | certificate | ok | ok | decoy_sources=0|family=cover|importers=6-12|root_caps=False|sources=1|star=False |
| [requests-resolve-03759f96](traces/requests-resolve-03759f96.md) | resolve | 3 | 6 | 7 | certificate | ok | ok | alias=False|decoys=0|family=resolve|from_init=False|hops=3|relative=False|star=False |
| [rich-composite-697440ee](traces/rich-composite-697440ee.md) | composite | 17 | 16 | 16 | certificate | ok | ok | alias=False|decoys=0|family=composite|from_init=False|hops=3|importers=6-12|relative=False|root_caps=False|star=False |
| [rich-cover-331b66a2](traces/rich-cover-331b66a2.md) | cover | 16 | 16 | 16 | certificate | ok | ok | decoy_sources=0|family=cover|importers=13+|root_caps=False|sources=1|star=False |
| [rich-cover-ad4aa569](traces/rich-cover-ad4aa569.md) | cover | 9 | 9 | 9 | certificate | ok | ok | decoy_sources=0|family=cover|importers=6-12|root_caps=False|sources=1|star=False |
| [rich-resolve-68cad6dd](traces/rich-resolve-68cad6dd.md) | resolve | 2 | 2 | 2 | certificate | ok | ok | alias=False|decoys=0|family=resolve|from_init=True|hops=2|relative=False|star=False |

## Sample thought

From `httpx-composite-b2ad6580`, step 2:

> The outline of `httpx/_transports/asgi.py` has 18 bindings; a literal `__all__` at line 26; no dynamic namespace tricks. This is not the branch I planned for that outcome; the open items changed more than expected.
>
> Chain: `httpx/_transports/asgi.py` takes `AsyncByteStream` from `.._types` (module not yet located).
>
> Still to settle: locate the module `.._types` imported by `httpx/_transports/asgi.py`.
>
> Next: outline `httpx/_types.py` filtered to `AsyncByteStream`, because `.._types` would be `httpx/_types.py` if that file exists; one call both checks and closes it. I expect: a definition there ends the chain (about 80%); the file does not exist (about 15%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, grep `def`/`class AsyncByteStream` statements under `.`, is expected to open more follow-up work. Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done; missing: grep `def`/`class AsyncByteStream` statements under `.`.

## Corpus manifest

| Repository | Commit | Python files | Text files |
|---|---|---|---|
| attrs | 8f767776326f | 56 | 113 |
| black | 20622e1259c2 | 345 | 438 |
| click | 36baa15ff831 | 79 | 144 |
| flask | d318b6834711 | 83 | 193 |
| httpx | b5addb64f016 | 60 | 98 |
| pytest | 51e9a9f148cd | 272 | 649 |
| requests | dae7ef63b4df | 37 | 83 |
| rich | 9d8f9a372cc5 | 213 | 517 |
