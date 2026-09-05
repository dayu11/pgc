# Demo report: smart policies for programmatic thoughts

Corpus: 8 real repositories, pinned by commit (see manifest below). Tasks set by static analysis with full access; priors fit leave-one-out (each repository's prior is fit on the other 7). Seed 0, budget 40 calls.

## Headline numbers

| Metric | Value |
|---|---|
| Tasks | 48 |
| Finished with a certificate (search policy) | 48/48 |
| Finished with a certificate (greedy baseline) | 48/48 |
| Final answer equals the oracle | 48/48 |
| Traces that replay bit-identically | 48/48 |
| Traces whose every world claim verifies | 48/48 (2176 checks) |
| Calls: omniscient floor / search / greedy | 402 / 403 / 402 |
| Steps by plan adherence | deviated 33, first 48, followed 205, open-ended 113, replanned 4 |

## Reading the numbers

- The omniscient floor counts one call per module that has to be closed, one per class or call list that has to be read, and the searches and listings a complete coverage needs. Calls above it are the price of honest uncertainty: a probe of a module file that turns out to be a package or external, a listing before a probe, a star-import source that had to be checked.
- Search (depth 2) and the greedy baseline (depth 1) mostly agree; where they differ the gap is one or two calls. The gains over a naive policy come from the cap-aware outcome model and from the obligation structure, not from lookahead depth.
- Calibration is measured on every step of every trace, unfiltered, so it also reflects the setter's task distribution (a task about subclasses is more likely to find some than a random name would be).
- `unplanned` steps are outcomes outside the forecast classes (an error response); `replanned` steps follow an outcome that opened new items, so the previous plan named a call that no longer applied; `deviated` steps chose differently with the same items open.

## By family

| Family | Tasks | Certificates | Floor | Search calls | Greedy calls |
|---|---|---|---|---|---|
| callers | 12 | 12 | 113 | 115 | 115 |
| expose | 7 | 7 | 25 | 32 | 32 |
| importers | 8 | 8 | 117 | 119 | 119 |
| not_overriding | 6 | 6 | 90 | 80 | 79 |
| resolve | 7 | 7 | 16 | 24 | 24 |
| subclasses | 8 | 8 | 41 | 33 | 33 |

## Calibration of forecasts (search policy)

Each step forecasts a distribution over outcome classes before its call. Rows pool (step, class) pairs by forecast probability.

| Forecast bin | Pairs | Mean forecast | Realized frequency |
|---|---|---|---|
| 0.0-0.2 | 685 | 0.04 | 0.07 |
| 0.2-0.4 | 58 | 0.24 | 0.16 |
| 0.4-0.6 | 19 | 0.51 | 0.47 |
| 0.6-0.8 | 50 | 0.74 | 0.84 |
| 0.8-1.0 | 338 | 0.94 | 0.87 |

## Diversity

| Repository | Pool by final operation | Skeleton cells in pool | Chosen | Prior hash |
|---|---|---|---|---|
| attrs | callers 36, expose 18, importers 55, resolve 98 | 45 | 6 | 0ac2a510ad43644e |
| black | callers 202, expose 430, resolve 363, subclasses 8 | 52 | 6 | f2e0b46ccc75305a |
| click | callers 33, importers 38, not_overriding 6, resolve 61, subclasses 6 | 36 | 6 | 81b2b7394c71c459 |
| flask | callers 52, expose 205, importers 95, not_overriding 1, resolve 180, subclasses 9 | 61 | 6 | 4ad7c2823d0ab783 |
| httpx | callers 59, expose 205, not_overriding 27, resolve 187, subclasses 34 | 39 | 6 | 708591d2904e1ac3 |
| pytest | callers 397, expose 978, importers 510, not_overriding 39, resolve 867, subclasses 99 | 107 | 6 | 8e41e8743065d192 |
| requests | callers 143, expose 181, importers 93, resolve 204, subclasses 13 | 62 | 6 | 736169d01b033d9f |
| rich | callers 302, expose 1031, importers 280, not_overriding 4, resolve 947, subclasses 8 | 87 | 6 | bf534cee5cd76c8c |

Distinct skeleton cells among chosen tasks: 43 of 48 tasks.

## Tasks

| Task | Chain | Floor | Search | Greedy | Stopped | Replay | World | Cell |
|---|---|---|---|---|---|---|---|---|
| [attrs-callers-139c336d](traces/attrs-callers-139c336d.md) | resolve→callers | 10 | 11 | 11 | certificate | ok | ok | alias=False|call_sites=5-12|caller_modules=2-3|chain=resolve→callers|decoys=0|false_positive_modules=3+|hops=2|relative=False|star=False |
| [attrs-callers-8516d5f7](traces/attrs-callers-8516d5f7.md) | resolve→callers | 8 | 7 | 7 | certificate | ok | ok | alias=False|call_sites=13+|caller_modules=2-3|chain=resolve→callers|decoys=0|false_positive_modules=1-2|hops=2|relative=True|star=False |
| [attrs-importers-b2c2ecb5](traces/attrs-importers-b2c2ecb5.md) | importers | 25 | 29 | 29 | certificate | ok | ok | chain=importers|decoy_sources=2+|importers=5|star=False |
| [attrs-importers-fc1b6d66](traces/attrs-importers-fc1b6d66.md) | resolve→importers | 23 | 24 | 24 | certificate | ok | ok | alias=False|chain=resolve→importers|decoy_sources=2+|decoys=0|hops=3|importers=5|relative=False|star=True |
| [attrs-resolve-4f2016a5](traces/attrs-resolve-4f2016a5.md) | resolve | 3 | 5 | 5 | certificate | ok | ok | alias=False|chain=resolve|decoys=1|hops=3|relative=False|star=False |
| [attrs-resolve-d9bafc19](traces/attrs-resolve-d9bafc19.md) | resolve | 2 | 2 | 2 | certificate | ok | ok | alias=True|chain=resolve|decoys=1|hops=2|relative=True|star=False |
| [black-callers-2595670c](traces/black-callers-2595670c.md) | callers | 6 | 8 | 8 | certificate | ok | ok | call_sites=5-12|caller_modules=2-3|chain=callers|false_positive_modules=1-2 |
| [black-callers-622092b7](traces/black-callers-622092b7.md) | resolve→callers | 6 | 6 | 6 | certificate | ok | ok | alias=False|call_sites=5-12|caller_modules=1|chain=resolve→callers|decoys=0|false_positive_modules=1-2|hops=2|relative=False|star=False |
| [black-expose-363321ff](traces/black-expose-363321ff.md) | expose | 2 | 2 | 2 | certificate | ok | ok | chain=expose|package_depth=2|star_sources=0 |
| [black-expose-3f3627c9](traces/black-expose-3f3627c9.md) | resolve→expose | 4 | 5 | 5 | certificate | ok | ok | alias=False|chain=resolve→expose|decoys=1|hops=2|package_depth=2|relative=False|star=False|star_sources=0 |
| [black-resolve-7179dc2f](traces/black-resolve-7179dc2f.md) | resolve | 3 | 5 | 5 | certificate | ok | ok | alias=False|chain=resolve|decoys=0|hops=3|relative=False|star=False |
| [black-subclasses-1ffaaa76](traces/black-subclasses-1ffaaa76.md) | subclasses | 5 | 9 | 9 | certificate | ok | ok | chain=subclasses|decoy_classes=0|subclasses=3 |
| [click-callers-81a79b57](traces/click-callers-81a79b57.md) | resolve→callers | 18 | 19 | 19 | certificate | ok | ok | alias=False|call_sites=13+|caller_modules=4+|chain=resolve→callers|decoys=0|false_positive_modules=1-2|hops=2|relative=False|star=False |
| [click-importers-0cd70ca7](traces/click-importers-0cd70ca7.md) | resolve→importers | 8 | 8 | 8 | certificate | ok | ok | alias=False|chain=resolve→importers|decoy_sources=0|decoys=0|hops=2|importers=5|relative=False|star=False |
| [click-importers-4d466025](traces/click-importers-4d466025.md) | resolve→importers | 12 | 11 | 11 | certificate | ok | ok | alias=False|chain=resolve→importers|decoy_sources=0|decoys=0|hops=2|importers=6-12|relative=True|star=False |
| [click-not_overriding-87cc99b7](traces/click-not_overriding-87cc99b7.md) | resolve→subclasses→not_overriding | 8 | 7 | 7 | certificate | ok | ok | alias=False|chain=resolve→subclasses→not_overriding|decoy_classes=0|decoys=0|hops=2|overriders=1|relative=False|star=False|subclasses=3 |
| [click-subclasses-1c5ae2a6](traces/click-subclasses-1c5ae2a6.md) | resolve→subclasses | 6 | 5 | 5 | certificate | ok | ok | alias=False|chain=resolve→subclasses|decoy_classes=0|decoys=0|hops=2|relative=False|star=False|subclasses=4-8 |
| [click-subclasses-7ada152a](traces/click-subclasses-7ada152a.md) | resolve→subclasses | 5 | 3 | 3 | certificate | ok | ok | alias=False|chain=resolve→subclasses|decoy_classes=0|decoys=0|hops=2|relative=True|star=False|subclasses=4-8 |
| [flask-callers-aad1e92e](traces/flask-callers-aad1e92e.md) | resolve→callers | 7 | 7 | 7 | certificate | ok | ok | alias=False|call_sites=5-12|caller_modules=2-3|chain=resolve→callers|decoys=0|false_positive_modules=0|hops=2|relative=True|star=False |
| [flask-expose-4411289d](traces/flask-expose-4411289d.md) | resolve→expose | 4 | 5 | 5 | certificate | ok | ok | alias=False|chain=resolve→expose|decoys=2+|hops=2|package_depth=3+|relative=True|star=False|star_sources=0 |
| [flask-importers-4322d92d](traces/flask-importers-4322d92d.md) | resolve→importers | 11 | 11 | 11 | certificate | ok | ok | alias=False|chain=resolve→importers|decoy_sources=0|decoys=0|hops=2|importers=6-12|relative=False|star=False |
| [flask-not_overriding-1895faee](traces/flask-not_overriding-1895faee.md) | resolve→subclasses→not_overriding | 14 | 13 | 13 | certificate | ok | ok | alias=False|chain=resolve→subclasses→not_overriding|decoy_classes=0|decoys=0|hops=2|overriders=4+|relative=False|star=False|subclasses=4-8 |
| [flask-resolve-b12c910a](traces/flask-resolve-b12c910a.md) | resolve | 2 | 2 | 2 | certificate | ok | ok | alias=False|chain=resolve|decoys=1|hops=2|relative=True|star=False |
| [flask-subclasses-d6d1d981](traces/flask-subclasses-d6d1d981.md) | resolve→subclasses | 7 | 5 | 5 | certificate | ok | ok | alias=False|chain=resolve→subclasses|decoy_classes=0|decoys=0|hops=2|relative=True|star=False|subclasses=3 |
| [httpx-callers-0d2d38f8](traces/httpx-callers-0d2d38f8.md) | resolve→callers | 8 | 8 | 8 | certificate | ok | ok | alias=False|call_sites=13+|caller_modules=2-3|chain=resolve→callers|decoys=0|false_positive_modules=1-2|hops=2|relative=False|star=False |
| [httpx-callers-a475b389](traces/httpx-callers-a475b389.md) | resolve→callers | 11 | 9 | 9 | certificate | ok | ok | alias=False|call_sites=5-12|caller_modules=2-3|chain=resolve→callers|decoys=0|false_positive_modules=1-2|hops=2|relative=True|star=False |
| [httpx-not_overriding-e47ffae3](traces/httpx-not_overriding-e47ffae3.md) | subclasses→not_overriding | 19 | 15 | 15 | certificate | ok | ok | chain=subclasses→not_overriding|decoy_classes=0|overriders=2-3|subclasses=4-8 |
| [httpx-not_overriding-f3ad6f92](traces/httpx-not_overriding-f3ad6f92.md) | subclasses→not_overriding | 11 | 9 | 9 | certificate | ok | ok | chain=subclasses→not_overriding|decoy_classes=0|overriders=1|subclasses=3 |
| [httpx-resolve-f733f017](traces/httpx-resolve-f733f017.md) | resolve | 2 | 2 | 2 | certificate | ok | ok | alias=False|chain=resolve|decoys=0|hops=2|relative=True|star=False |
| [httpx-subclasses-ce1b6953](traces/httpx-subclasses-ce1b6953.md) | subclasses | 3 | 2 | 2 | certificate | ok | ok | chain=subclasses|decoy_classes=0|subclasses=3 |
| [pytest-callers-5bdeb4fd](traces/pytest-callers-5bdeb4fd.md) | resolve→callers | 7 | 7 | 7 | certificate | ok | ok | alias=False|call_sites=5-12|caller_modules=1|chain=resolve→callers|decoys=0|false_positive_modules=1-2|hops=2|relative=False|star=False |
| [pytest-expose-c2e38ec1](traces/pytest-expose-c2e38ec1.md) | resolve→expose | 5 | 9 | 9 | certificate | ok | ok | alias=False|chain=resolve→expose|decoys=0|hops=3|package_depth=2|relative=False|star=False|star_sources=0 |
| [pytest-importers-dd54ab7d](traces/pytest-importers-dd54ab7d.md) | resolve→importers | 8 | 8 | 8 | certificate | ok | ok | alias=False|chain=resolve→importers|decoy_sources=0|decoys=0|hops=2|importers=5|relative=True|star=False |
| [pytest-not_overriding-6142ae49](traces/pytest-not_overriding-6142ae49.md) | subclasses→not_overriding | 21 | 25 | 24 | certificate | ok | ok | chain=subclasses→not_overriding|decoy_classes=1|overriders=2-3|subclasses=4-8 |
| [pytest-resolve-8d655d35](traces/pytest-resolve-8d655d35.md) | resolve | 2 | 4 | 4 | certificate | ok | ok | alias=True|chain=resolve|decoys=1|hops=2|relative=False|star=False |
| [pytest-subclasses-7309d690](traces/pytest-subclasses-7309d690.md) | subclasses | 3 | 2 | 2 | certificate | ok | ok | chain=subclasses|decoy_classes=0|subclasses=4-8 |
| [requests-callers-ca8381db](traces/requests-callers-ca8381db.md) | resolve→callers | 14 | 14 | 14 | certificate | ok | ok | alias=False|call_sites=13+|caller_modules=2-3|chain=resolve→callers|decoys=0|false_positive_modules=1-2|hops=2|relative=True|star=False |
| [requests-callers-f14c2704](traces/requests-callers-f14c2704.md) | callers | 7 | 8 | 8 | certificate | ok | ok | call_sites=5-12|caller_modules=2-3|chain=callers|false_positive_modules=0 |
| [requests-expose-92e3294d](traces/requests-expose-92e3294d.md) | expose | 2 | 2 | 2 | certificate | ok | ok | chain=expose|package_depth=2|star_sources=0 |
| [requests-expose-f79ae652](traces/requests-expose-f79ae652.md) | resolve→expose | 4 | 5 | 5 | certificate | ok | ok | alias=False|chain=resolve→expose|decoys=0|hops=2|package_depth=2|relative=False|star=False|star_sources=0 |
| [requests-importers-8ad279df](traces/requests-importers-8ad279df.md) | resolve→importers | 12 | 11 | 11 | certificate | ok | ok | alias=False|chain=resolve→importers|decoy_sources=0|decoys=0|hops=2|importers=6-12|relative=True|star=False |
| [requests-subclasses-0433d150](traces/requests-subclasses-0433d150.md) | resolve→subclasses | 5 | 3 | 3 | certificate | ok | ok | alias=False|chain=resolve→subclasses|decoy_classes=0|decoys=0|hops=2|relative=True|star=False|subclasses=9+ |
| [rich-callers-e62f0078](traces/rich-callers-e62f0078.md) | callers | 11 | 11 | 11 | certificate | ok | ok | call_sites=5-12|caller_modules=4+|chain=callers|false_positive_modules=0 |
| [rich-expose-c75345a7](traces/rich-expose-c75345a7.md) | resolve→expose | 4 | 4 | 4 | certificate | ok | ok | alias=False|chain=resolve→expose|decoys=0|hops=2|package_depth=2|relative=True|star=False|star_sources=0 |
| [rich-importers-8d923e06](traces/rich-importers-8d923e06.md) | resolve→importers | 18 | 17 | 17 | certificate | ok | ok | alias=False|chain=resolve→importers|decoy_sources=0|decoys=0|hops=2|importers=13+|relative=False|star=False |
| [rich-not_overriding-dad6cd7e](traces/rich-not_overriding-dad6cd7e.md) | resolve→subclasses→not_overriding | 17 | 11 | 11 | certificate | ok | ok | alias=False|chain=resolve→subclasses→not_overriding|decoy_classes=0|decoys=0|hops=2|overriders=1|relative=True|star=False|subclasses=4-8 |
| [rich-resolve-380ccb11](traces/rich-resolve-380ccb11.md) | resolve | 2 | 4 | 4 | certificate | ok | ok | alias=False|chain=resolve|decoys=1|hops=2|relative=False|star=False |
| [rich-subclasses-5ddce5e1](traces/rich-subclasses-5ddce5e1.md) | resolve→subclasses | 7 | 4 | 4 | certificate | ok | ok | alias=False|chain=resolve→subclasses|decoy_classes=0|decoys=0|hops=2|relative=False|star=False|subclasses=3 |

## Sample thought

From `attrs-importers-b2c2ecb5`, step 1:

> Starting from the definition of `fields` at `src/attr/_make.py:1924`. Then I have to find every module-level import of that definition, which means a complete search, not a sample.
>
> Next I will search the whole tree for imports of `fields` and star imports in one go; the search has to be complete before I can call the set final. Maybe nothing turns up. If it fits under the cap or it caps, I follow whatever it opens up.

From `attrs-importers-b2c2ecb5`, step 2:

> 20 matching lines anywhere for imports of `fields` or star imports, in `src/attr/__init__.py`, `src/attr/_funcs.py`, `src/attrs/__init__.py`, `src/attrs/__init__.pyi` and 13 more files, and the search was under the cap, so that is the complete set there.
>
> Let me look at `tests/test_validators.py`'s top-level names for `fields`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `src/attr/__init__.py`'s top-level names for `fields`.

From `attrs-importers-b2c2ecb5`, step 3:

> The test module `tests/test_validators.py`: line 14 imports it from `attr`.
>
> Tally: 0 import statements confirmed, 0 ruled out, 15 pending. The search itself is complete; what is left is checking the candidates.
>
> I'll look at `src/attr/__init__.py`'s top-level names for `fields`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will list `./` to see what lives there.

Final thought:

> 4 module-level import statements bring in this definition: `src/attr/__init__.py:16`, `src/attr/_funcs.py:5`, `tests/test_dunders.py:18`, `tests/test_make.py:29`. Ruled out along the way: `src/attrs/__init__.py:3` (`attr` resolves `fields` to ambiguous(dynamic module)); `src/attrs/converters.py:3` (star import of `attr.converters`, which does not export `fields`). Looking back, 1 of 29 calls did not end up mattering (step 26).

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
