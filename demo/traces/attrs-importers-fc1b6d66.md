# attrs-importers-fc1b6d66

**Repository:** attrs  
**Chain:** resolve → importers  
**Seed:** 0, prior 0ac2a510ad43644e, floor 23

## Task

In `tests/test_validators.py` line 16, `and_` is imported from `attr.validators`. Which definition does the module-level name `and_` actually refer to? Give `path:line`. Then list every module-level import statement in the repository that brings in that definition, including through re-exports and star imports, as `path:line`.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N; bindings take effect in source order. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. A class derives from a definition when a base written as a bare name or `module.Name` resolves to it. A call site is `name(...)` where the bare name refers to the module-level binding (not a parameter or local). Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

I need to find what `and_` really is in `tests/test_validators.py`: line 16 imports it from `attr.validators`, so the definition is at least one hop away. Then I have to find every module-level import of that definition, which means a complete search, not a sample.

Next I will check `tests/test_validators.py` for any other binding of `and_` besides the import on line 16; almost certainly the import is the only one, and then `attr.validators` is the place to follow.

**Call:** `symbols('tests/test_validators.py', 'and_')`

**Response**: outcome `reexport`

```
module tests/test_validators.py lines=1405 dynamic=no all=none
16 from and_ <- attr.validators and_
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "tests/test_validators.py",
    "and_"
   ],
   "desc": "check the top-level names of `tests/test_validators.py` for `and_`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/test_validators.py', 'and_')",
   "key": "[\"symbols\", [\"tests/test_validators.py\", \"and_\"]]",
   "v1": [
    22086579,
    7532750
   ],
   "v2": [
    22086579,
    7532750
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     1,
     100
    ],
    "reexport": [
     93,
     100
    ],
    "star": [
     1,
     100
    ],
    "none": [
     1,
     20
    ]
   },
   "serves": [
    [
     "bindings",
     "tests/test_validators.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_validators.py')",
   "key": "[\"symbols\", [\"tests/test_validators.py\"]]",
   "v1": [
    11990227001,
    3909497250
   ],
   "v2": [
    11990227001,
    3909497250
   ],
   "p_cap": [
    70,
    519
   ],
   "forecast": {
    "def": [
     449,
     51900
    ],
    "reexport": [
     13919,
     17300
    ],
    "star": [
     449,
     51900
    ],
    "none": [
     449,
     10380
    ],
    "cap": [
     70,
     519
    ]
   },
   "serves": [
    [
     "bindings",
     "tests/test_validators.py",
     "and_"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_validators.py', 'and_')",
  "key": "[\"symbols\", [\"tests/test_validators.py\", \"and_\"]]",
  "provenance": "module `tests/test_validators.py` (task), name `and_` (task)",
  "v2": [
   22086579,
   7532750
  ]
 },
 "forecast": {
  "def": [
   1,
   100
  ],
  "reexport": [
   93,
   100
  ],
  "star": [
   1,
   100
  ],
  "none": [
   1,
   20
  ]
 },
 "plan": {
  "def": "done",
  "reexport": "continue",
  "star": "continue",
  "none": "done"
 },
 "hedges": [
  {
   "outcome": "reexport",
   "word": "almost certainly",
   "p": [
    93,
    100
   ]
  }
 ],
 "adherence": null,
 "facts": [
  {
   "kind": "outline",
   "step": 1,
   "path": "tests/test_validators.py",
   "filter": "and_",
   "header": {
    "lines": 1405,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_validators.py",
     "name": "and_",
     "line": 16,
     "kind": "from",
     "src": "attr.validators",
     "src_name": "and_",
     "conditional": false,
     "col": 0,
     "bases": []
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "resolve",
  "step": 1,
  "of": 2,
  "chain": [
   [
    "tests/test_validators.py",
    "and_",
    "reexport",
    [
     "attr.validators",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 2

The test module `tests/test_validators.py` does not define `and_` itself; line 16 imports it from `attr.validators`.

So far: `tests/test_validators.py` takes `and_` from `attr.validators`, which I still have to locate.

Let me list `./` to see what lives there; the listing settles whether the import is a module, a package, or not here at all. Very likely the listing fits. If the listing is too long, I will outline `attr/validators.py` directly, which both checks that the file exists and shows me `and_`. I could outline `attr/validators.py` directly, which both checks that the file exists and shows me `and_` instead, but it costs more calls in expectation.

**Call:** `ls('.')`

**Response**: outcome `complete`

```
.git_archival.txt
.github/
.pre-commit-config.yaml
.readthedocs.yaml
CHANGELOG.md
README.md
bench/
changelog.d/
codspeed.yml
docs/
pyproject.toml
src/
tests/
tox.ini
typing_tests/
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_validators.py",
    "attr.validators"
   ],
   "desc": "find where `attr.validators` (imported by `tests/test_validators.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    1643,
    870
   ],
   "v2": [
    22017490622407,
    11262272677830
   ],
   "p_cap": [
    2,
    9
   ],
   "forecast": {
    "complete": [
     7,
     9
    ],
    "cap": [
     2,
     9
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_validators.py",
     "attr.validators"
    ]
   ]
  },
  {
   "call": "symbols('attr/validators.py', 'and_')",
   "key": "[\"symbols\", [\"attr/validators.py\", \"and_\"]]",
   "v1": [
    1473039993049,
    625681815435
   ],
   "v2": [
    2810608750273,
    1251363630870
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     71632,
     218583
    ],
    "reexport": [
     35816,
     4153077
    ],
    "star": [
     3256,
     4153077
    ],
    "none": [
     55352,
     4153077
    ],
    "missing": [
     6035,
     9291
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_validators.py",
     "attr.validators"
    ]
   ]
  },
  {
   "call": "symbols('attr/validators/__init__.py', 'and_')",
   "key": "[\"symbols\", [\"attr/validators/__init__.py\", \"and_\"]]",
   "v1": [
    304709609,
    100590560
   ],
   "v2": [
    865619947,
    301771680
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     605,
     74328
    ],
    "reexport": [
     55,
     3097
    ],
    "star": [
     55,
     74328
    ],
    "none": [
     55,
     6194
    ],
    "missing": [
     2987,
     3097
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_validators.py",
     "attr.validators"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+and_\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+and_\\\\b\", \".\"]]",
   "v1": [
    443,
    145
   ],
   "v2": [
    2513,
    870
   ],
   "p_cap": [
    1,
    36
   ],
   "forecast": {
    "zero": [
     1,
     36
    ],
    "mid": [
     17,
     18
    ],
    "cap": [
     1,
     36
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_validators.py",
     "attr.validators"
    ]
   ]
  }
 ],
 "choice": {
  "call": "ls('.')",
  "key": "[\"ls\", [\".\"]]",
  "provenance": "`attr.validators` imported by `tests/test_validators.py` should live under `.`",
  "v2": [
   22017490622407,
   11262272677830
  ]
 },
 "forecast": {
  "complete": [
   7,
   9
  ],
  "cap": [
   2,
   9
  ]
 },
 "plan": {
  "complete": "continue",
  "cap": "[\"symbols\", [\"attr/validators.py\", \"and_\"]]"
 },
 "hedges": [
  {
   "outcome": "complete",
   "word": "very likely",
   "p": [
    7,
    9
   ]
  }
 ],
 "adherence": {
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "listing",
   "step": 2,
   "dir": ".",
   "entries": [
    ".git_archival.txt",
    ".github/",
    ".pre-commit-config.yaml",
    ".readthedocs.yaml",
    "CHANGELOG.md",
    "README.md",
    "bench/",
    "changelog.d/",
    "codspeed.yml",
    "docs/",
    "pyproject.toml",
    "src/",
    "tests/",
    "tox.ini",
    "typing_tests/"
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "resolve",
  "step": 1,
  "of": 2,
  "chain": [
   [
    "tests/test_validators.py",
    "and_",
    "reexport",
    [
     "attr.validators",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 3

`./` has 15 entries: there is no `attr` here.

So far: `tests/test_validators.py` takes `and_` from `attr.validators`, which I still have to locate.

I'll search the whole tree for `class and_`/`def and_`; that shows where the definition lives and whether the name is reused. Almost certainly it fits under the cap. If it caps or nothing turns up, I will list `src/` to see what lives there. I could list `src/` to see what lives there instead, but it costs more calls in expectation.

**Call:** `grep('^\\s*(?:async\\s+)?(?:def|class)\\s+and_\\b', '.')`

**Response**: outcome `mid`

```
src/attr/_make.py:3381:def and_(*validators):
src/attr/validators.pyi:61:def and_(*validators: _ValidatorType[_T]) -> _ValidatorType[_T]: ...
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_validators.py",
    "attr.validators"
   ],
   "desc": "find where `attr.validators` (imported by `tests/test_validators.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+and_\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+and_\\\\b\", \".\"]]",
   "v1": [
    5509,
    2610
   ],
   "v2": [
    95731,
    45240
   ],
   "p_cap": [
    1,
    36
   ],
   "forecast": {
    "zero": [
     1,
     36
    ],
    "mid": [
     17,
     18
    ],
    "cap": [
     1,
     36
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_validators.py",
     "attr.validators"
    ]
   ]
  },
  {
   "call": "ls('src')",
   "key": "[\"ls\", [\"src\"]]",
   "v1": [
    16221,
    7540
   ],
   "v2": [
    292703,
    135720
   ],
   "p_cap": [
    5,
    52
   ],
   "forecast": {
    "complete": [
     47,
     52
    ],
    "cap": [
     5,
     52
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_validators.py",
     "attr.validators"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/validators.py', 'and_')",
   "key": "[\"symbols\", [\"src/attr/validators.py\", \"and_\"]]",
   "v1": [
    1473039993049,
    625681815435
   ],
   "v2": [
    8973711194119,
    3754090892610
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     71632,
     218583
    ],
    "reexport": [
     35816,
     4153077
    ],
    "star": [
     3256,
     4153077
    ],
    "none": [
     55352,
     4153077
    ],
    "missing": [
     6035,
     9291
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_validators.py",
     "attr.validators"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+and_\\\\b', 'src')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+and_\\\\b\", \"src\"]]",
   "v1": [
    19363,
    6670
   ],
   "v2": [
    118063,
    40020
   ],
   "p_cap": [
    1,
    184
   ],
   "forecast": {
    "zero": [
     155,
     184
    ],
    "mid": [
     7,
     46
    ],
    "cap": [
     1,
     184
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_validators.py",
     "attr.validators"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/validators/__init__.py', 'and_')",
   "key": "[\"symbols\", [\"src/attr/validators/__init__.py\", \"and_\"]]",
   "v1": [
    304709609,
    100590560
   ],
   "v2": [
    2790895361,
    905315040
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     605,
     74328
    ],
    "reexport": [
     55,
     3097
    ],
    "star": [
     55,
     74328
    ],
    "none": [
     55,
     6194
    ],
    "missing": [
     2987,
     3097
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_validators.py",
     "attr.validators"
    ]
   ]
  }
 ],
 "choice": {
  "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+and_\\\\b', '.')",
  "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+and_\\\\b\", \".\"]]",
  "provenance": "a `def`/`class and_` statement would reveal the module file; `and_` task",
  "v2": [
   95731,
   45240
  ]
 },
 "forecast": {
  "zero": [
   1,
   36
  ],
  "mid": [
   17,
   18
  ],
  "cap": [
   1,
   36
  ]
 },
 "plan": {
  "zero": "[\"ls\", [\"src\"]]",
  "mid": "continue",
  "cap": "[\"ls\", [\"src\"]]"
 },
 "hedges": [
  {
   "outcome": "mid",
   "word": "almost certainly",
   "p": [
    17,
    18
   ]
  }
 ],
 "adherence": {
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "grep",
   "step": 3,
   "pattern": "^\\s*(?:async\\s+)?(?:def|class)\\s+and_\\b",
   "scope": ".",
   "hits": [
    [
     "src/attr/_make.py",
     3381
    ],
    [
     "src/attr/validators.pyi",
     61
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "phase": "resolve",
  "step": 1,
  "of": 2,
  "chain": [
   [
    "tests/test_validators.py",
    "and_",
    "reexport",
    [
     "attr.validators",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 4

`and_` is defined 2 times: `src/attr/_make.py`, `src/attr/validators.pyi`. Only one of them can be the one this import means, so the import chain decides.

So far: `tests/test_validators.py` takes `and_` from `attr.validators`, which I still have to locate.

I'll outline `src/attr/validators.py` directly, which both checks that the file exists and shows me `and_`; if `attr.validators` is a plain module that is where it has to be. Very likely it is defined right there. If the file does not exist, I will list `src/attr/` to see what lives there; if the name is not bound there, that finishes it. I could list `src/attr/` to see what lives there instead, but it tends to open more follow-up work.

**Call:** `symbols('src/attr/validators.py', 'and_')`

**Response**: outcome `reexport`

```
module src/attr/validators.py lines=767 dynamic=no all=static@19
14 from and_ <- ._make and_
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_validators.py",
    "attr.validators"
   ],
   "desc": "find where `attr.validators` (imported by `tests/test_validators.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/validators.py', 'and_')",
   "key": "[\"symbols\", [\"src/attr/validators.py\", \"and_\"]]",
   "v1": [
    13603250257,
    10976873955
   ],
   "v2": [
    3038575516186,
    2447842891965
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     61864,
     72861
    ],
    "reexport": [
     1628,
     72861
    ],
    "star": [
     148,
     72861
    ],
    "none": [
     2516,
     72861
    ],
    "missing": [
     15,
     163
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_validators.py",
     "attr.validators"
    ]
   ]
  },
  {
   "call": "ls('src/attr')",
   "key": "[\"ls\", [\"src/attr\"]]",
   "v1": [
    67179,
    32335
   ],
   "v2": [
    5040842963216,
    2447842891965
   ],
   "p_cap": [
    5,
    223
   ],
   "forecast": {
    "complete": [
     218,
     223
    ],
    "cap": [
     5,
     223
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_validators.py",
     "attr.validators"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/validators/__init__.py', 'and_')",
   "key": "[\"symbols\", [\"src/attr/validators/__init__.py\", \"and_\"]]",
   "v1": [
    31637297,
    10588480
   ],
   "v2": [
    1801198508720323,
    801575243689920
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     55,
     2608
    ],
    "reexport": [
     15,
     326
    ],
    "star": [
     5,
     2608
    ],
    "none": [
     15,
     652
    ],
    "missing": [
     148,
     163
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_validators.py",
     "attr.validators"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/attr/validators.py', 'and_')",
  "key": "[\"symbols\", [\"src/attr/validators.py\", \"and_\"]]",
  "provenance": "`attr.validators` would be `src/attr/validators.py` if that file exists; one call both checks and closes it",
  "v2": [
   3038575516186,
   2447842891965
  ]
 },
 "forecast": {
  "def": [
   61864,
   72861
  ],
  "reexport": [
   1628,
   72861
  ],
  "star": [
   148,
   72861
  ],
  "none": [
   2516,
   72861
  ],
  "missing": [
   15,
   163
  ]
 },
 "plan": {
  "def": "done",
  "reexport": "continue",
  "star": "continue",
  "none": "done",
  "missing": "[\"ls\", [\"src/attr\"]]"
 },
 "hedges": [
  {
   "outcome": "def",
   "word": "very likely",
   "p": [
    61864,
    72861
   ]
  }
 ],
 "adherence": {
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 4,
   "path": "src/attr/validators.py",
   "filter": "and_",
   "header": {
    "lines": 767,
    "dynamic": false,
    "all_status": "static",
    "all_line": 19
   },
   "bindings": [
    {
     "module": "src/attr/validators.py",
     "name": "and_",
     "line": 14,
     "kind": "from",
     "src": "._make",
     "src_name": "and_",
     "conditional": false,
     "col": 0,
     "bases": []
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "resolve",
  "step": 1,
  "of": 2,
  "chain": [
   [
    "tests/test_validators.py",
    "and_",
    "reexport",
    [
     "attr.validators",
     "src/attr/validators.py"
    ]
   ],
   [
    "src/attr/validators.py",
    "and_",
    "reexport",
    [
     "._make",
     "src/attr/_make.py"
    ]
   ],
   [
    "src/attr/_make.py",
    "and_",
    "open",
    null
   ]
  ]
 }
}
```
</details>

## Step 5

Huh: `src/attr/validators.py` does not define `and_` itself; line 14 imports it from `._make`.

So far: `tests/test_validators.py` takes `and_` from `attr.validators`; `src/attr/validators.py` takes `and_` from `._make`; `src/attr/_make.py` is next.

I'll look at `src/attr/_make.py`'s top-level names for `and_`; that settles what the name means there. Almost certainly it is defined right there. If the name is not bound there, that finishes it; if it is re-exported from somewhere else, I follow whatever it opens up. I could outline all of `src/attr/_make.py` instead, but it is more likely to hit the cap.

**Call:** `symbols('src/attr/_make.py', 'and_')`

**Response**: outcome `def`

```
module src/attr/_make.py lines=3463 dynamic=no all=none
3381 def and_
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/attr/_make.py",
    "and_"
   ],
   "desc": "check the top-level names of `src/attr/_make.py` for `and_`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/_make.py', 'and_')",
   "key": "[\"symbols\", [\"src/attr/_make.py\", \"and_\"]]",
   "v1": [
    3999389,
    3766375
   ],
   "v2": [
    3999389,
    3766375
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     47,
     50
    ],
    "reexport": [
     1,
     50
    ],
    "star": [
     1,
     100
    ],
    "none": [
     3,
     100
    ]
   },
   "serves": [
    [
     "bindings",
     "src/attr/_make.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/_make.py')",
   "key": "[\"symbols\", [\"src/attr/_make.py\"]]",
   "v1": [
    2339329141,
    1954748625
   ],
   "v2": [
    2339329141,
    1954748625
   ],
   "p_cap": [
    70,
    519
   ],
   "forecast": {
    "def": [
     21103,
     25950
    ],
    "reexport": [
     449,
     25950
    ],
    "star": [
     449,
     51900
    ],
    "none": [
     449,
     17300
    ],
    "cap": [
     70,
     519
    ]
   },
   "serves": [
    [
     "bindings",
     "src/attr/_make.py",
     "and_"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/attr/_make.py', 'and_')",
  "key": "[\"symbols\", [\"src/attr/_make.py\", \"and_\"]]",
  "provenance": "module `src/attr/_make.py` (step 3), name `and_` (task)",
  "v2": [
   3999389,
   3766375
  ]
 },
 "forecast": {
  "def": [
   47,
   50
  ],
  "reexport": [
   1,
   50
  ],
  "star": [
   1,
   100
  ],
  "none": [
   3,
   100
  ]
 },
 "plan": {
  "def": "done",
  "reexport": "continue",
  "star": "continue",
  "none": "done"
 },
 "hedges": [
  {
   "outcome": "def",
   "word": "almost certainly",
   "p": [
    47,
    50
   ]
  }
 ],
 "adherence": {
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 5,
   "path": "src/attr/_make.py",
   "filter": "and_",
   "header": {
    "lines": 3463,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/attr/_make.py",
     "name": "and_",
     "line": 3381,
     "kind": "def",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": []
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "resolve",
  "step": 1,
  "of": 2,
  "chain": [
   [
    "tests/test_validators.py",
    "and_",
    "reexport",
    [
     "attr.validators",
     "src/attr/validators.py"
    ]
   ],
   [
    "src/attr/validators.py",
    "and_",
    "reexport",
    [
     "._make",
     "src/attr/_make.py"
    ]
   ],
   [
    "src/attr/_make.py",
    "and_",
    "def",
    3381
   ]
  ]
 }
}
```
</details>

## Step 6

There it is: `and_` is a function at `src/attr/_make.py:3381`. That settles the definition; now the imports of it.

Next I will search the whole tree for imports of `and_` and star imports in one go; the search has to be complete before I can call the set final. Maybe nothing turns up. If it fits under the cap or it caps, I follow whatever it opens up.

**Call:** `grep('^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\band_\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*and_\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$', '.')`

**Response**: outcome `mid`

```
src/attr/validators.py:14:from ._make import _AndValidator, and_, attrib, attrs
src/attrs/converters.py:3:from attr.converters import *  # noqa: F403
src/attrs/exceptions.py:3:from attr.exceptions import *  # noqa: F403
src/attrs/filters.py:3:from attr.filters import *  # noqa: F403
src/attrs/setters.py:3:from attr.setters import *  # noqa: F403
src/attrs/validators.py:3:from attr.validators import *  # noqa: F403
tests/attr_import_star.py:4:from attr import *  # noqa: F403
tests/test_make.py:41:    and_,
tests/test_mypy.yml:1384:            from other import *
tests/test_next_gen.py:575:        from attrs.validators import and_
tests/test_validators.py:18:    and_,
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "cover",
   "key": [
    "cover",
    "IMPORT",
    "."
   ],
   "desc": "search `.` for imports of `and_`"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "."
   ],
   "desc": "search `.` for star imports"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\band_\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*and_\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\band_\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*and_\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
   "v1": [
    23209880717,
    10098421760
   ],
   "v2": [
    23209880717,
    10098421760
   ],
   "p_cap": [
    5,
    32
   ],
   "forecast": {
    "zero": [
     17,
     32
    ],
    "mid": [
     5,
     16
    ],
    "cap": [
     5,
     32
    ]
   },
   "serves": [
    [
     "cover",
     "IMPORT",
     "."
    ],
    [
     "cover",
     "STAR",
     "."
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\band_\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*and_\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\band_\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*and_\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
   "v1": [
    1819974069461,
    388158086400
   ],
   "v2": [
    344724955207,
    129386028800
   ],
   "p_cap": [
    1,
    41
   ],
   "forecast": {
    "zero": [
     31,
     41
    ],
    "mid": [
     9,
     41
    ],
    "cap": [
     1,
     41
    ]
   },
   "serves": [
    [
     "cover",
     "IMPORT",
     "."
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+\\\\*', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+\\\\*\", \".\"]]",
   "v1": [
    389070645127,
    129386028800
   ],
   "v2": [
    344724955207,
    129386028800
   ],
   "p_cap": [
    1,
    18
   ],
   "forecast": {
    "zero": [
     13,
     18
    ],
    "mid": [
     2,
     9
    ],
    "cap": [
     1,
     18
    ]
   },
   "serves": [
    [
     "cover",
     "STAR",
     "."
    ]
   ]
  }
 ],
 "choice": {
  "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\band_\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*and_\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
  "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\band_\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*and_\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
  "provenance": "import and star lines under `.` in one call",
  "v2": [
   23209880717,
   10098421760
  ]
 },
 "forecast": {
  "zero": [
   17,
   32
  ],
  "mid": [
   5,
   16
  ],
  "cap": [
   5,
   32
  ]
 },
 "plan": {
  "zero": "done",
  "mid": "continue",
  "cap": "continue"
 },
 "hedges": [
  {
   "outcome": "zero",
   "word": "maybe",
   "p": [
    17,
    32
   ]
  }
 ],
 "adherence": {
  "planned": "done",
  "status": "deviated"
 },
 "facts": [
  {
   "kind": "grep",
   "step": 6,
   "pattern": "^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\band_\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*and_\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$",
   "scope": ".",
   "hits": [
    [
     "src/attr/validators.py",
     14
    ],
    [
     "src/attrs/converters.py",
     3
    ],
    [
     "src/attrs/exceptions.py",
     3
    ],
    [
     "src/attrs/filters.py",
     3
    ],
    [
     "src/attrs/setters.py",
     3
    ],
    [
     "src/attrs/validators.py",
     3
    ],
    [
     "tests/attr_import_star.py",
     4
    ],
    [
     "tests/test_make.py",
     41
    ],
    [
     "tests/test_mypy.yml",
     1384
    ],
    [
     "tests/test_next_gen.py",
     575
    ],
    [
     "tests/test_validators.py",
     18
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/attr/validators.py",
   "src/attrs/converters.py",
   "src/attrs/exceptions.py",
   "src/attrs/filters.py",
   "src/attrs/setters.py",
   "src/attrs/validators.py",
   "tests/attr_import_star.py",
   "tests/test_make.py",
   "tests/test_next_gen.py",
   "tests/test_validators.py"
  ],
  "table": [
   [
    "src/attr/validators.py",
    "src/attr/validators.py:14",
    "in",
    "`._make` resolves `and_` to the target"
   ],
   [
    "src/attrs/converters.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/attrs/exceptions.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/attrs/filters.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/attrs/setters.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/attrs/validators.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/attr_import_star.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_make.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_next_gen.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_validators.py",
    "tests/test_validators.py:16",
    "in",
    "`attr.validators` resolves `and_` to the target"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  },
  "n_in": 2,
  "n_out": 0,
  "n_pending": 8
 }
}
```
</details>

## Step 7

11 matching lines anywhere for imports of `and_` or star imports, in `src/attr/validators.py`, `src/attrs/converters.py`, `src/attrs/exceptions.py`, `src/attrs/filters.py` and 7 more files, and the search was under the cap, so that is the complete set there.

Next I will look at `src/attrs/exceptions.py`'s top-level names for `and_`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `src/attrs/converters.py`'s top-level names for `and_`.

**Call:** `symbols('src/attrs/exceptions.py', 'and_')`

**Response**: outcome `ok`

```
module src/attrs/exceptions.py lines=4 dynamic=no all=none
3 star <- attr.exceptions
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/converters.py",
    "and_"
   ],
   "desc": "look at `src/attrs/converters.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/exceptions.py",
    "and_"
   ],
   "desc": "look at `src/attrs/exceptions.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "and_"
   ],
   "desc": "look at `src/attrs/filters.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "and_"
   ],
   "desc": "look at `src/attrs/setters.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "and_"
   ],
   "desc": "look at `src/attrs/validators.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "and_"
   ],
   "desc": "look at `tests/attr_import_star.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "and_"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_next_gen.py",
    "and_"
   ],
   "desc": "look at `tests/test_next_gen.py`'s imports of `and_`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attrs/converters.py', 'and_')",
   "key": "[\"symbols\", [\"src/attrs/converters.py\", \"and_\"]]",
   "v1": [
    6681503,
    503150
   ],
   "v2": [
    3345783,
    251575
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "src/attrs/converters.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/exceptions.py', 'and_')",
   "key": "[\"symbols\", [\"src/attrs/exceptions.py\", \"and_\"]]",
   "v1": [
    6681503,
    503150
   ],
   "v2": [
    3345783,
    251575
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "src/attrs/exceptions.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/filters.py', 'and_')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"and_\"]]",
   "v1": [
    6681503,
    503150
   ],
   "v2": [
    3345783,
    251575
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "src/attrs/filters.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'and_')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"and_\"]]",
   "v1": [
    6681503,
    503150
   ],
   "v2": [
    3345783,
    251575
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "src/attrs/setters.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'and_')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"and_\"]]",
   "v1": [
    6681503,
    503150
   ],
   "v2": [
    3345783,
    251575
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "src/attrs/validators.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'and_')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"and_\"]]",
   "v1": [
    6681503,
    503150
   ],
   "v2": [
    3345783,
    251575
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/attr_import_star.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'and_')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"and_\"]]",
   "v1": [
    6681503,
    503150
   ],
   "v2": [
    3345783,
    251575
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_make.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_next_gen.py', 'and_')",
   "key": "[\"symbols\", [\"tests/test_next_gen.py\", \"and_\"]]",
   "v1": [
    6681503,
    503150
   ],
   "v2": [
    3345783,
    251575
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_next_gen.py",
     "and_"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/attrs/exceptions.py', 'and_')",
  "key": "[\"symbols\", [\"src/attrs/exceptions.py\", \"and_\"]]",
  "provenance": "`src/attrs/exceptions.py` had a matching line (step 6); its outline names every `and_` import exactly",
  "v2": [
   3345783,
   251575
  ]
 },
 "forecast": {
  "ok": [
   49,
   50
  ],
  "cap": [
   1,
   50
  ]
 },
 "plan": {
  "ok": "[\"symbols\", [\"src/attrs/converters.py\", \"and_\"]]",
  "cap": "[\"symbols\", [\"src/attrs/converters.py\", \"and_\"]]"
 },
 "hedges": [
  {
   "outcome": "ok",
   "word": "almost certainly",
   "p": [
    49,
    50
   ]
  }
 ],
 "adherence": {
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 7,
   "path": "src/attrs/exceptions.py",
   "filter": "and_",
   "header": {
    "lines": 4,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/attrs/exceptions.py",
     "name": "*",
     "line": 3,
     "kind": "star",
     "src": "attr.exceptions",
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": 
```
</details>

## Step 8

`src/attrs/exceptions.py` matched the search but has no module-level import of `and_`. It also star-imports `attr.exceptions`, which could carry the name, so that needs checking.

Tally: 2 import statements confirmed, 0 ruled out, 8 pending. The search itself is complete; what is left is checking the candidates.

Still open: look at `src/attrs/converters.py`'s imports of `and_`; find where `attr.exceptions` (imported by `src/attrs/exceptions.py`) lives; look at `src/attrs/filters.py`'s imports of `and_`; and 5 more.

I'll look at `src/attrs/converters.py`'s top-level names for `and_`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will outline `src/attr/exceptions.py` directly, which both checks that the file exists and shows me `and_`.

**Call:** `symbols('src/attrs/converters.py', 'and_')`

**Response**: outcome `ok`

```
module src/attrs/converters.py lines=4 dynamic=no all=none
3 star <- attr.converters
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/converters.py",
    "and_"
   ],
   "desc": "look at `src/attrs/converters.py`'s imports of `and_`"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/exceptions.py",
    "attr.exceptions"
   ],
   "desc": "find where `attr.exceptions` (imported by `src/attrs/exceptions.py`) lives"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "and_"
   ],
   "desc": "look at `src/attrs/filters.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "and_"
   ],
   "desc": "look at `src/attrs/setters.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "and_"
   ],
   "desc": "look at `src/attrs/validators.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "and_"
   ],
   "desc": "look at `tests/attr_import_star.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "and_"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_next_gen.py",
    "and_"
   ],
   "desc": "look at `tests/test_next_gen.py`'s imports of `and_`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/exceptions.py', 'and_')",
   "key": "[\"symbols\", [\"src/attr/exceptions.py\", \"and_\"]]",
   "v1": [
    48911784033008,
    3808975262385
   ],
   "v2": [
    489879635382557,
    38089752623850
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     61864,
     72861
    ],
    "reexport": [
     1628,
     72861
    ],
    "star": [
     148,
     72861
    ],
    "none": [
     2516,
     72861
    ],
    "missing": [
     15,
     163
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attrs/exceptions.py",
     "attr.exceptions"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/converters.py', 'and_')",
   "key": "[\"symbols\", [\"src/attrs/converters.py\", \"and_\"]]",
   "v1": [
    6881633,
    503150
   ],
   "v2": [
    489879635382557,
    38089752623850
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "src/attrs/converters.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/filters.py', 'and_')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"and_\"]]",
   "v1": [
    6881633,
    503150
   ],
   "v2": [
    489879635382557,
    38089752623850
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "src/attrs/filters.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'and_')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"and_\"]]",
   "v1": [
    6881633,
    503150
   ],
   "v2": [
    489879635382557,
    38089752623850
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "src/attrs/setters.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'and_')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"and_\"]]",
   "v1": [
    6881633,
    503150
   ],
   "v2": [
    489879635382557,
    38089752623850
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "src/attrs/validators.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'and_')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"and_\"]]",
   "v1": [
    6881633,
    503150
   ],
   "v2": [
    489879635382557,
    38089752623850
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/attr_import_star.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'and_')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"and_\"]]",
   "v1": [
    6881633,
    503150
   ],
   "v2": [
    489879635382557,
    38089752623850
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_make.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_next_gen.py', 'and_')",
   "key": "[\"symbols\", [\"tests/test_next_gen.py\", \"and_\"]]",
   "v1": [
    6881633,
    503150
   ],
   "v2": [
    489879635382557,
    38089752623850
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_next_gen.py",
     "and_"
    ]
   ]
  },
  {
   "call": "ls('src/attr')",
   "key": "[\"ls\", [\"src/attr\"]]",
   "v1": [
    153487586,
    11220245
   ],
   "v2": [
    58102371858019088,
    4247007417559275
   ],
   "p_cap": [
    5,
    223
   ],
   "forecast": {
    "complete": [
     218,
     223
    ],
    "cap": [
     5,
     223
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attrs/exceptions.py",
     "attr.exceptions"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/exceptions/__init__.py', 'and_')",
   "key": "[\"symbols\", [\"src/attr/exceptions/__init__.py\", \"and_\"]]",
   "v1": [
    53605975083,
    3674202560
   ],
   "v2": [
    3852564705899385521,
    278146609560402240
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     55,
     2608
    ],
    "reexport": [
     15,
   
```
</details>

## Step 9

`src/attrs/converters.py` matched the search but has no module-level import of `and_`. It also star-imports `attr.converters`, which could carry the name, so that needs checking.

Tally: 2 import statements confirmed, 0 ruled out, 8 pending. The search itself is complete; what is left is checking the candidates.

Let me outline `src/attr/exceptions.py` directly, which both checks that the file exists and shows me `and_`; if `attr.exceptions` is a plain module that is where it has to be. Very likely it is defined right there. If the file does not exist, I will list `src/attr/` to see what lives there; if the name is not bound there or it is re-exported from somewhere else, I will outline `src/attr/converters.py` directly, which both checks that the file exists and shows me `and_`.

**Call:** `symbols('src/attr/exceptions.py', 'and_')`

**Response**: outcome `none`

```
module src/attr/exceptions.py lines=96 dynamic=no all=none
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/converters.py",
    "attr.converters"
   ],
   "desc": "find where `attr.converters` (imported by `src/attrs/converters.py`) lives"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/exceptions.py",
    "attr.exceptions"
   ],
   "desc": "find where `attr.exceptions` (imported by `src/attrs/exceptions.py`) lives"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "and_"
   ],
   "desc": "look at `src/attrs/filters.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "and_"
   ],
   "desc": "look at `src/attrs/setters.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "and_"
   ],
   "desc": "look at `src/attrs/validators.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "and_"
   ],
   "desc": "look at `tests/attr_import_star.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "and_"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_next_gen.py",
    "and_"
   ],
   "desc": "look at `tests/test_next_gen.py`'s imports of `and_`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/converters.py', 'and_')",
   "key": "[\"symbols\", [\"src/attr/converters.py\", \"and_\"]]",
   "v1": [
    10085363949307,
    761795052477
   ],
   "v2": [
    343645170685953212,
    27690488362486473
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     61864,
     72861
    ],
    "reexport": [
     1628,
     72861
    ],
    "star": [
     148,
     72861
    ],
    "none": [
     2516,
     72861
    ],
    "missing": [
     15,
     163
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attrs/converters.py",
     "attr.converters"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/exceptions.py', 'and_')",
   "key": "[\"symbols\", [\"src/attr/exceptions.py\", \"and_\"]]",
   "v1": [
    10085363949307,
    761795052477
   ],
   "v2": [
    343645170685953212,
    27690488362486473
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     61864,
     72861
    ],
    "reexport": [
     1628,
     72861
    ],
    "star": [
     148,
     72861
    ],
    "none": [
     2516,
     72861
    ],
    "missing": [
     15,
     163
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attrs/exceptions.py",
     "attr.exceptions"
    ]
   ]
  },
  {
   "call": "ls('src/attr')",
   "key": "[\"ls\", [\"src/attr\"]]",
   "v1": [
    29396363,
    2244049
   ],
   "v2": [
    55639853642602043,
    4247007417559275
   ],
   "p_cap": [
    5,
    223
   ],
   "forecast": {
    "complete": [
     218,
     223
    ],
    "cap": [
     5,
     223
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attrs/converters.py",
     "attr.converters"
    ],
    [
     "module_path",
     "src/attrs/exceptions.py",
     "attr.exceptions"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/filters.py', 'and_')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"and_\"]]",
   "v1": [
    7081763,
    503150
   ],
   "v2": [
    1472062199,
    112202450
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "src/attrs/filters.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'and_')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"and_\"]]",
   "v1": [
    7081763,
    503150
   ],
   "v2": [
    1472062199,
    112202450
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "src/attrs/setters.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'and_')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"and_\"]]",
   "v1": [
    7081763,
    503150
   ],
   "v2": [
    1472062199,
    112202450
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "src/attrs/validators.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'and_')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"and_\"]]",
   "v1": [
    7081763,
    503150
   ],
   "v2": [
    1472062199,
    112202450
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/attr_import_star.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'and_')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"and_\"]]",
   "v1": [
    7081763,
    503150
   ],
   "v2": [
    1472062199,
    112202450
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_make.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_next_gen.py', 'and_')",
   "key": "[\"symbols\", [\"tests/test_next_gen.py\", \"and_\"]]",
   "v1": [
    7081763,
    503150
   ],
   "v2": [
    1472062199,
    112202450
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_next_gen.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/converters/__init__.py', 'and_')",
   "key": "[\"symbols\", [\"src/attr/converters/__init__.py\",
```
</details>

## Step 10

Huh: `src/attr/exceptions.py` does not bind `and_` at module level at all.

Tally: 2 import statements confirmed, 1 ruled out, 7 pending. The search itself is complete; what is left is checking the candidates.

I'll outline `src/attr/converters.py` directly, which both checks that the file exists and shows me `and_`; if `attr.converters` is a plain module that is where it has to be. Very likely it is defined right there. If the file does not exist or the name is not bound there, I will look at `src/attrs/filters.py`'s top-level names for `and_`.

**Call:** `symbols('src/attr/converters.py', 'and_')`

**Response**: outcome `none`

```
module src/attr/converters.py lines=161 dynamic=no all=static@11
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/converters.py",
    "attr.converters"
   ],
   "desc": "find where `attr.converters` (imported by `src/attrs/converters.py`) lives"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "and_"
   ],
   "desc": "look at `src/attrs/filters.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "and_"
   ],
   "desc": "look at `src/attrs/setters.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "and_"
   ],
   "desc": "look at `src/attrs/validators.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "and_"
   ],
   "desc": "look at `tests/attr_import_star.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "and_"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_next_gen.py",
    "and_"
   ],
   "desc": "look at `tests/test_next_gen.py`'s imports of `and_`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/converters.py', 'and_')",
   "key": "[\"symbols\", [\"src/attr/converters.py\", \"and_\"]]",
   "v1": [
    42598718862461,
    3808975262385
   ],
   "v2": [
    426748983677087,
    38089752623850
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     61864,
     72861
    ],
    "reexport": [
     1628,
     72861
    ],
    "star": [
     148,
     72861
    ],
    "none": [
     2516,
     72861
    ],
    "missing": [
     15,
     163
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attrs/converters.py",
     "attr.converters"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/filters.py', 'and_')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"and_\"]]",
   "v1": [
    6047703,
    503150
   ],
   "v2": [
    426748983677087,
    38089752623850
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "src/attrs/filters.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'and_')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"and_\"]]",
   "v1": [
    6047703,
    503150
   ],
   "v2": [
    426748983677087,
    38089752623850
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "src/attrs/setters.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'and_')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"and_\"]]",
   "v1": [
    6047703,
    503150
   ],
   "v2": [
    426748983677087,
    38089752623850
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "src/attrs/validators.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'and_')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"and_\"]]",
   "v1": [
    6047703,
    503150
   ],
   "v2": [
    426748983677087,
    38089752623850
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/attr_import_star.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'and_')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"and_\"]]",
   "v1": [
    6047703,
    503150
   ],
   "v2": [
    426748983677087,
    38089752623850
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_make.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_next_gen.py', 'and_')",
   "key": "[\"symbols\", [\"tests/test_next_gen.py\", \"and_\"]]",
   "v1": [
    6047703,
    503150
   ],
   "v2": [
    426748983677087,
    38089752623850
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_next_gen.py",
     "and_"
    ]
   ]
  },
  {
   "call": "ls('src/attr')",
   "key": "[\"ls\", [\"src/attr\"]]",
   "v1": [
    134890947,
    11220245
   ],
   "v2": [
    51063304192859183,
    4247007417559275
   ],
   "p_cap": [
    5,
    223
   ],
   "forecast": {
    "complete": [
     218,
     223
    ],
    "cap": [
     5,
     223
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attrs/converters.py",
     "attr.converters"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/converters/__init__.py', 'and_')",
   "key": "[\"symbols\", [\"src/attr/converters/__init__.py\", \"and_\"]]",
   "v1": [
    47516284651,
    3674202560
   ],
   "v2": [
    3391559434885361393,
    278146609560402240
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     55,
     2608
    ],
    "reexport": [
     15,
     326
    ],
    "star": [
     5,
     2608
    ],
    "none": [
     15,
     652
    ],
    "missing": [
     148,
     163
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attrs/converters.py",
     "attr.converters"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/attr/converters.py', 'and_')",
  "key": "[\"symbols\", [\"src/attr/converters.py\", \"and_\"]]",
  "provenance": "`attr.converters` would be `src/attr/converters.py` if that file exists; one call both checks and closes it",
  "v2": [
   426748983677087,
   38089752623850
  ]
 },
 "forecast": {
  "def": [
   61864,
   72861
  ],
  "r
```
</details>

## Step 11

Interesting: `src/attr/converters.py` does not bind `and_` at module level at all.

Tally: 2 import statements confirmed, 1 ruled out, 7 pending. The search itself is complete; what is left is checking the candidates.

I'll look at `src/attrs/filters.py`'s top-level names for `and_`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `src/attrs/setters.py`'s top-level names for `and_`.

**Call:** `symbols('src/attrs/filters.py', 'and_')`

**Response**: outcome `ok`

```
module src/attrs/filters.py lines=4 dynamic=no all=none
3 star <- attr.filters
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/converters.py"
   ],
   "desc": "read what `src/attr/converters.py` exports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "and_"
   ],
   "desc": "look at `src/attrs/filters.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "and_"
   ],
   "desc": "look at `src/attrs/setters.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "and_"
   ],
   "desc": "look at `src/attrs/validators.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "and_"
   ],
   "desc": "look at `tests/attr_import_star.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "and_"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_next_gen.py",
    "and_"
   ],
   "desc": "look at `tests/test_next_gen.py`'s imports of `and_`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attrs/filters.py', 'and_')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"and_\"]]",
   "v1": [
    5516793,
    503150
   ],
   "v2": [
    2763428,
    251575
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "src/attrs/filters.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'and_')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"and_\"]]",
   "v1": [
    5516793,
    503150
   ],
   "v2": [
    2763428,
    251575
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "src/attrs/setters.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'and_')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"and_\"]]",
   "v1": [
    5516793,
    503150
   ],
   "v2": [
    2763428,
    251575
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "src/attrs/validators.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'and_')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"and_\"]]",
   "v1": [
    5516793,
    503150
   ],
   "v2": [
    2763428,
    251575
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/attr_import_star.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'and_')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"and_\"]]",
   "v1": [
    5516793,
    503150
   ],
   "v2": [
    2763428,
    251575
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_make.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_next_gen.py', 'and_')",
   "key": "[\"symbols\", [\"tests/test_next_gen.py\", \"and_\"]]",
   "v1": [
    5516793,
    503150
   ],
   "v2": [
    2763428,
    251575
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_next_gen.py",
     "and_"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    17772481,
    1610080
   ],
   "v2": [
    89023413,
    8050400
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/converters.py"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/attrs/filters.py', 'and_')",
  "key": "[\"symbols\", [\"src/attrs/filters.py\", \"and_\"]]",
  "provenance": "`src/attrs/filters.py` had a matching line (step 6); its outline names every `and_` import exactly",
  "v2": [
   2763428,
   251575
  ]
 },
 "forecast": {
  "ok": [
   49,
   50
  ],
  "cap": [
   1,
   50
  ]
 },
 "plan": {
  "ok": "[\"symbols\", [\"src/attrs/setters.py\", \"and_\"]]",
  "cap": "[\"symbols\", [\"src/attrs/setters.py\", \"and_\"]]"
 },
 "hedges": [
  {
   "outcome": "ok",
   "word": "almost certainly",
   "p": [
    49,
    50
   ]
  }
 ],
 "adherence": {
  "planned": "[\"symbols\", [\"src/attrs/filters.py\", \"and_\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 11,
   "path": "src/attrs/filters.py",
   "filter": "and_",
   "header": {
    "lines": 4,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/attrs/filters.py",
     "name": "*",
     "line": 3,
     "kind": "star",
     "src": "attr.filters",
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": []
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/attr/validators.py",
   "src/attrs/converters.py",
   "src/attrs/exceptions.py",
   "src/attrs/filters.py",
   "src/attrs/setters.py",
   "src/attrs/validators.py",
   "tests/attr_import_star.py",
   "tests/test_make.py",
   "tests/test_next_gen.py",
   "tests/test_validators.py"
  ],
  "table": [
   [
    "src/attr/validators.py",
    "src/attr/validators.py:14",
    "in",
    "`._make` resolves `and_` to the target"
   ],
   [
    "src/attrs/converters.py",
    null,
    "pending",
    "not yet examined"
```
</details>

## Step 12

`src/attrs/filters.py` matched the search but has no module-level import of `and_`. It also star-imports `attr.filters`, which could carry the name, so that needs checking.

Tally: 2 import statements confirmed, 1 ruled out, 7 pending. The search itself is complete; what is left is checking the candidates.

Still open: read what `src/attr/converters.py` exports; find where `attr.filters` (imported by `src/attrs/filters.py`) lives; look at `src/attrs/setters.py`'s imports of `and_`; and 4 more.

Next I will look at `src/attrs/setters.py`'s top-level names for `and_`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will outline `src/attr/filters.py` directly, which both checks that the file exists and shows me `and_`.

**Call:** `symbols('src/attrs/setters.py', 'and_')`

**Response**: outcome `ok`

```
module src/attrs/setters.py lines=4 dynamic=no all=none
3 star <- attr.setters
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/converters.py"
   ],
   "desc": "read what `src/attr/converters.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/filters.py",
    "attr.filters"
   ],
   "desc": "find where `attr.filters` (imported by `src/attrs/filters.py`) lives"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "and_"
   ],
   "desc": "look at `src/attrs/setters.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "and_"
   ],
   "desc": "look at `src/attrs/validators.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "and_"
   ],
   "desc": "look at `tests/attr_import_star.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "and_"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_next_gen.py",
    "and_"
   ],
   "desc": "look at `tests/test_next_gen.py`'s imports of `and_`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/filters.py', 'and_')",
   "key": "[\"symbols\", [\"src/attr/filters.py\", \"and_\"]]",
   "v1": [
    40094628954299,
    3808975262385
   ],
   "v2": [
    401708084595467,
    38089752623850
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     61864,
     72861
    ],
    "reexport": [
     1628,
     72861
    ],
    "star": [
     148,
     72861
    ],
    "none": [
     2516,
     72861
    ],
    "missing": [
     15,
     163
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attrs/filters.py",
     "attr.filters"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'and_')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"and_\"]]",
   "v1": [
    5716923,
    503150
   ],
   "v2": [
    401708084595467,
    38089752623850
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "src/attrs/setters.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'and_')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"and_\"]]",
   "v1": [
    5716923,
    503150
   ],
   "v2": [
    401708084595467,
    38089752623850
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "src/attrs/validators.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'and_')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"and_\"]]",
   "v1": [
    5716923,
    503150
   ],
   "v2": [
    401708084595467,
    38089752623850
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/attr_import_star.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'and_')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"and_\"]]",
   "v1": [
    5716923,
    503150
   ],
   "v2": [
    401708084595467,
    38089752623850
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_make.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_next_gen.py', 'and_')",
   "key": "[\"symbols\", [\"tests/test_next_gen.py\", \"and_\"]]",
   "v1": [
    5716923,
    503150
   ],
   "v2": [
    401708084595467,
    38089752623850
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_next_gen.py",
     "and_"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    18412897,
    1610080
   ],
   "v2": [
    1294455052324723,
    121887208396320
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/converters.py"
    ]
   ]
  },
  {
   "call": "ls('src/attr')",
   "key": "[\"ls\", [\"src/attr\"]]",
   "v1": [
    127514553,
    11220245
   ],
   "v2": [
    48271243945258553,
    4247007417559275
   ],
   "p_cap": [
    5,
    223
   ],
   "forecast": {
    "complete": [
     218,
     223
    ],
    "cap": [
     5,
     223
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attrs/filters.py",
     "attr.filters"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/filters/__init__.py', 'and_')",
   "key": "[\"symbols\", [\"src/attr/filters/__init__.py\", \"and_\"]]",
   "v1": [
    45100796779,
    3674202560
   ],
   "v2": [
    641740154686347901,
    55629321912080448
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     55,
     2608
    ],
    "reexport": [
     15,
     326
    ],
    "star": [
     5,
     2608
    ],
    "none": [
     15,
     652
    ],
    "missing": [
     148,
     163
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attrs/filters.py",
     "attr.filters"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/attrs/setters.py', 'and_')",
  "key": "[\"symbols\", [\"src/attrs/setters.py\", \"and_\"]]",
  "provenance": "`src/attrs/setters.py` had a matching line (step 6); its outline names every `and_` import exactly",
  "v2": [
   401708084595467,
   38089752623850
  ]
 },
 "forecast": {
  "ok": [
   49,
   50
  ],
  "cap": [
   1,
   50
  ]
 },
 "plan": {
  "ok": "[\"symbols\", [\"src/attr/filters.py\", \"and_\"]]",
  "
```
</details>

## Step 13

`src/attrs/setters.py` matched the search but has no module-level import of `and_`. It also star-imports `attr.setters`, which could carry the name, so that needs checking.

Tally: 2 import statements confirmed, 1 ruled out, 7 pending. The search itself is complete; what is left is checking the candidates.

I'll outline `src/attr/filters.py` directly, which both checks that the file exists and shows me `and_`; if `attr.filters` is a plain module that is where it has to be. Very likely it is defined right there. If the file does not exist, I will list `src/attr/` to see what lives there; if the name is not bound there or it is re-exported from somewhere else, I will outline `src/attr/setters.py` directly, which both checks that the file exists and shows me `and_`.

**Call:** `symbols('src/attr/filters.py', 'and_')`

**Response**: outcome `none`

```
module src/attr/filters.py lines=73 dynamic=no all=none
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/converters.py"
   ],
   "desc": "read what `src/attr/converters.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/filters.py",
    "attr.filters"
   ],
   "desc": "find where `attr.filters` (imported by `src/attrs/filters.py`) lives"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/setters.py",
    "attr.setters"
   ],
   "desc": "find where `attr.setters` (imported by `src/attrs/setters.py`) lives"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "and_"
   ],
   "desc": "look at `src/attrs/validators.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "and_"
   ],
   "desc": "look at `tests/attr_import_star.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "and_"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_next_gen.py",
    "and_"
   ],
   "desc": "look at `tests/test_next_gen.py`'s imports of `and_`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/filters.py', 'and_')",
   "key": "[\"symbols\", [\"src/attr/filters.py\", \"and_\"]]",
   "v1": [
    41609664667826,
    3808975262385
   ],
   "v2": [
    1397731083473772619,
    138452441812432365
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     61864,
     72861
    ],
    "reexport": [
     1628,
     72861
    ],
    "star": [
     148,
     72861
    ],
    "none": [
     2516,
     72861
    ],
    "missing": [
     15,
     163
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attrs/filters.py",
     "attr.filters"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/setters.py', 'and_')",
   "key": "[\"symbols\", [\"src/attr/setters.py\", \"and_\"]]",
   "v1": [
    41609664667826,
    3808975262385
   ],
   "v2": [
    1397731083473772619,
    138452441812432365
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     61864,
     72861
    ],
    "reexport": [
     1628,
     72861
    ],
    "star": [
     148,
     72861
    ],
    "none": [
     2516,
     72861
    ],
    "missing": [
     15,
     163
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attrs/setters.py",
     "attr.setters"
    ]
   ]
  },
  {
   "call": "ls('src/attr')",
   "key": "[\"ls\", [\"src/attr\"]]",
   "v1": [
    121008782,
    11220245
   ],
   "v2": [
    45808725729841508,
    4247007417559275
   ],
   "p_cap": [
    5,
    223
   ],
   "forecast": {
    "complete": [
     218,
     223
    ],
    "cap": [
     5,
     223
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attrs/filters.py",
     "attr.filters"
    ],
    [
     "module_path",
     "src/attrs/setters.py",
     "attr.setters"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'and_')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"and_\"]]",
   "v1": [
    5917053,
    503150
   ],
   "v2": [
    1212331869,
    112202450
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "src/attrs/validators.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'and_')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"and_\"]]",
   "v1": [
    5917053,
    503150
   ],
   "v2": [
    1212331869,
    112202450
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/attr_import_star.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'and_')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"and_\"]]",
   "v1": [
    5917053,
    503150
   ],
   "v2": [
    1212331869,
    112202450
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_make.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_next_gen.py', 'and_')",
   "key": "[\"symbols\", [\"tests/test_next_gen.py\", \"and_\"]]",
   "v1": [
    5917053,
    503150
   ],
   "v2": [
    1212331869,
    112202450
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_next_gen.py",
     "and_"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    19053313,
    1610080
   ],
   "v2": [
    3905941759,
    359047840
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/converters.py"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/filters/__init__.py', 'and_')",
   "key": "[\"symbols\", [\"src/attr/filters/__init__.py\", \"and_\"]]",
   "v1": [
    46562226091,
    3674202560
   ],
   "v2": [
    242532658737868914309,
    20675564643989899840
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     55,
     2608
    ],
    "reexport": [
     15,
     326
    ],
    "star": [
     5,
     2608
    ],
    "none": [
     15,
     652
    ],
    "missing": [
     148,
     163
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attrs/filters.py",
     "attr.filters"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/setters/__init__.py', 'and_')",
   "key": "[\"symbols\", [\"src/attr/setters/__init__.py\", \"and_\"]]",
   "v1": [
    46562226091,
    3674202560
   ],
   "v2": [
    
```
</details>

## Step 14

Not what I expected: `src/attr/filters.py` does not bind `and_` at module level at all.

Tally: 2 import statements confirmed, 2 ruled out, 6 pending. The search itself is complete; what is left is checking the candidates.

Next I will outline `src/attr/setters.py` directly, which both checks that the file exists and shows me `and_`; if `attr.setters` is a plain module that is where it has to be. Very likely it is defined right there. If the file does not exist or the name is not bound there, I will look at `src/attrs/validators.py`'s top-level names for `and_`.

**Call:** `symbols('src/attr/setters.py', 'and_')`

**Response**: outcome `none`

```
module src/attr/setters.py lines=83 dynamic=no all=none
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/converters.py"
   ],
   "desc": "read what `src/attr/converters.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/setters.py",
    "attr.setters"
   ],
   "desc": "find where `attr.setters` (imported by `src/attrs/setters.py`) lives"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "and_"
   ],
   "desc": "look at `src/attrs/validators.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "and_"
   ],
   "desc": "look at `tests/attr_import_star.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "and_"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_next_gen.py",
    "and_"
   ],
   "desc": "look at `tests/test_next_gen.py`'s imports of `and_`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/setters.py', 'and_')",
   "key": "[\"symbols\", [\"src/attr/setters.py\", \"and_\"]]",
   "v1": [
    33781563783752,
    3808975262385
   ],
   "v2": [
    338577432889997,
    38089752623850
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     61864,
     72861
    ],
    "reexport": [
     1628,
     72861
    ],
    "star": [
     148,
     72861
    ],
    "none": [
     2516,
     72861
    ],
    "missing": [
     15,
     163
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attrs/setters.py",
     "attr.setters"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'and_')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"and_\"]]",
   "v1": [
    4882993,
    503150
   ],
   "v2": [
    338577432889997,
    38089752623850
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "src/attrs/validators.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'and_')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"and_\"]]",
   "v1": [
    4882993,
    503150
   ],
   "v2": [
    338577432889997,
    38089752623850
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/attr_import_star.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'and_')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"and_\"]]",
   "v1": [
    4882993,
    503150
   ],
   "v2": [
    338577432889997,
    38089752623850
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_make.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_next_gen.py', 'and_')",
   "key": "[\"symbols\", [\"tests/test_next_gen.py\", \"and_\"]]",
   "v1": [
    4882993,
    503150
   ],
   "v2": [
    338577432889997,
    38089752623850
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_next_gen.py",
     "and_"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    15744321,
    1610080
   ],
   "v2": [
    1092436966867219,
    121887208396320
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/converters.py"
    ]
   ]
  },
  {
   "call": "ls('src/attr')",
   "key": "[\"ls\", [\"src/attr\"]]",
   "v1": [
    108917914,
    11220245
   ],
   "v2": [
    41232176280098648,
    4247007417559275
   ],
   "p_cap": [
    5,
    223
   ],
   "forecast": {
    "complete": [
     218,
     223
    ],
    "cap": [
     5,
     223
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attrs/setters.py",
     "attr.setters"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/setters/__init__.py', 'and_')",
   "key": "[\"symbols\", [\"src/attr/setters/__init__.py\", \"and_\"]]",
   "v1": [
    39011106347,
    3674202560
   ],
   "v2": [
    2747695502417715377,
    278146609560402240
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     55,
     2608
    ],
    "reexport": [
     15,
     326
    ],
    "star": [
     5,
     2608
    ],
    "none": [
     15,
     652
    ],
    "missing": [
     148,
     163
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attrs/setters.py",
     "attr.setters"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/attr/setters.py', 'and_')",
  "key": "[\"symbols\", [\"src/attr/setters.py\", \"and_\"]]",
  "provenance": "`attr.setters` would be `src/attr/setters.py` if that file exists; one call both checks and closes it",
  "v2": [
   338577432889997,
   38089752623850
  ]
 },
 "forecast": {
  "def": [
   61864,
   72861
  ],
  "reexport": [
   1628,
   72861
  ],
  "star": [
   148,
   72861
  ],
  "none": [
   2516,
   72861
  ],
  "missing": [
   15,
   163
  ]
 },
 "plan": {
  "def": "[\"symbols\", [\"src/attrs/validators.py\", \"and_\"]]",
  "reexport": "[\"symbols\", [\"src/attrs/validators.py\", \"and_\"]]",
  "star": "[\"symbols\", [\"src/attrs/validators.py\", \"and_\"]]",
  "none": "[\"symbols\", [\"src/attrs/validators.py\", \"and_\"]]",
  "missing": "[\"symbols\", [\"src/attrs/validators.py\", \"and_\"]]"
 },
 "hedges": [
  {
   "outcome": "def",
   "word": "very likely",
   "p": [
    61864,
    72861
   ]
  }
 ],
 "adherence": {
  "planned": "[\"symbols\", [\"src/attr/setters.py\", \"and_\"]]",
  "status":
```
</details>

## Step 15

Huh: `src/attr/setters.py` does not bind `and_` at module level at all.

Tally: 2 import statements confirmed, 3 ruled out, 5 pending. The search itself is complete; what is left is checking the candidates.

Next I will look at `src/attrs/validators.py`'s top-level names for `and_`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `tests/attr_import_star.py`'s top-level names for `and_`.

**Call:** `symbols('src/attrs/validators.py', 'and_')`

**Response**: outcome `ok`

```
module src/attrs/validators.py lines=4 dynamic=no all=none
3 star <- attr.validators
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/converters.py"
   ],
   "desc": "read what `src/attr/converters.py` exports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "and_"
   ],
   "desc": "look at `src/attrs/validators.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "and_"
   ],
   "desc": "look at `tests/attr_import_star.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "and_"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_next_gen.py",
    "and_"
   ],
   "desc": "look at `tests/test_next_gen.py`'s imports of `and_`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attrs/validators.py', 'and_')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"and_\"]]",
   "v1": [
    3848933,
    503150
   ],
   "v2": [
    1929498,
    251575
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "src/attrs/validators.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'and_')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"and_\"]]",
   "v1": [
    3848933,
    503150
   ],
   "v2": [
    1929498,
    251575
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/attr_import_star.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'and_')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"and_\"]]",
   "v1": [
    3848933,
    503150
   ],
   "v2": [
    1929498,
    251575
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_make.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_next_gen.py', 'and_')",
   "key": "[\"symbols\", [\"tests/test_next_gen.py\", \"and_\"]]",
   "v1": [
    3848933,
    503150
   ],
   "v2": [
    1929498,
    251575
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_next_gen.py",
     "and_"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    12435329,
    1610080
   ],
   "v2": [
    62337653,
    8050400
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/converters.py"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/attrs/validators.py', 'and_')",
  "key": "[\"symbols\", [\"src/attrs/validators.py\", \"and_\"]]",
  "provenance": "`src/attrs/validators.py` had a matching line (step 6); its outline names every `and_` import exactly",
  "v2": [
   1929498,
   251575
  ]
 },
 "forecast": {
  "ok": [
   49,
   50
  ],
  "cap": [
   1,
   50
  ]
 },
 "plan": {
  "ok": "[\"symbols\", [\"tests/attr_import_star.py\", \"and_\"]]",
  "cap": "[\"symbols\", [\"tests/attr_import_star.py\", \"and_\"]]"
 },
 "hedges": [
  {
   "outcome": "ok",
   "word": "almost certainly",
   "p": [
    49,
    50
   ]
  }
 ],
 "adherence": {
  "planned": "[\"symbols\", [\"src/attrs/validators.py\", \"and_\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 15,
   "path": "src/attrs/validators.py",
   "filter": "and_",
   "header": {
    "lines": 4,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/attrs/validators.py",
     "name": "*",
     "line": 3,
     "kind": "star",
     "src": "attr.validators",
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": []
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/attr/validators.py",
   "src/attrs/converters.py",
   "src/attrs/exceptions.py",
   "src/attrs/filters.py",
   "src/attrs/setters.py",
   "src/attrs/validators.py",
   "tests/attr_import_star.py",
   "tests/test_make.py",
   "tests/test_next_gen.py",
   "tests/test_validators.py"
  ],
  "table": [
   [
    "src/attr/validators.py",
    "src/attr/validators.py:14",
    "in",
    "`._make` resolves `and_` to the target"
   ],
   [
    "src/attrs/converters.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/attrs/exceptions.py",
    "src/attrs/exceptions.py:3",
    "out",
    "star import of `attr.exceptions`, which does not export `and_`"
   ],
   [
    "src/attrs/filters.py",
    "src/attrs/filters.py:3",
    "out",
    "star import of `attr.filters`, which does not export `and_`"
   ],
   [
    "src/attrs/setters.py",
    "src/attrs/setters.py:3",
    "out",
    "star import of `attr.setters`, which does not export `and_`"
   ],
   [
    "src/attrs/validators.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/attr_import_star.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_make.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_next_gen.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_validators.py",
    "tests/test_validators.py:16",
    "in",
    "`attr.validators` resolves `and_` to the target"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  },
  "n_in": 2,
  "n_out": 3,
  "n_pending": 5
 }
}
```
</details>

## Step 16

`src/attrs/validators.py` matched the search but has no module-level import of `and_`. It also star-imports `attr.validators`, which could carry the name, so that needs checking.

Tally: 2 import statements confirmed, 3 ruled out, 5 pending. The search itself is complete; what is left is checking the candidates.

Still open: read what `src/attr/converters.py` exports; read what `src/attr/validators.py` exports; look at `tests/attr_import_star.py`'s imports of `and_`; and 2 more.

I'll look at `tests/attr_import_star.py`'s top-level names for `and_`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `tests/test_make.py`'s top-level names for `and_`.

**Call:** `symbols('tests/attr_import_star.py', 'and_')`

**Response**: outcome `ok`

```
module tests/attr_import_star.py lines=10 dynamic=no all=none
4 star <- attr
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/converters.py"
   ],
   "desc": "read what `src/attr/converters.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/validators.py"
   ],
   "desc": "read what `src/attr/validators.py` exports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "and_"
   ],
   "desc": "look at `tests/attr_import_star.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "and_"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_next_gen.py",
    "and_"
   ],
   "desc": "look at `tests/test_next_gen.py`'s imports of `and_`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/attr_import_star.py', 'and_')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"and_\"]]",
   "v1": [
    3518153,
    503150
   ],
   "v2": [
    1764108,
    251575
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/attr_import_star.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'and_')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"and_\"]]",
   "v1": [
    3518153,
    503150
   ],
   "v2": [
    1764108,
    251575
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_make.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_next_gen.py', 'and_')",
   "key": "[\"symbols\", [\"tests/test_next_gen.py\", \"and_\"]]",
   "v1": [
    3518153,
    503150
   ],
   "v2": [
    1764108,
    251575
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_next_gen.py",
     "and_"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    11376833,
    1610080
   ],
   "v2": [
    57045173,
    8050400
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/converters.py"
    ]
   ]
  },
  {
   "call": "read('src/attr/validators.py', 19, 30)",
   "key": "[\"read\", [\"src/attr/validators.py\", 19, 30]]",
   "v1": [
    11376833,
    1610080
   ],
   "v2": [
    57045173,
    8050400
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/validators.py"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/attr_import_star.py', 'and_')",
  "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"and_\"]]",
  "provenance": "`tests/attr_import_star.py` had a matching line (step 6); its outline names every `and_` import exactly",
  "v2": [
   1764108,
   251575
  ]
 },
 "forecast": {
  "ok": [
   49,
   50
  ],
  "cap": [
   1,
   50
  ]
 },
 "plan": {
  "ok": "[\"symbols\", [\"tests/test_make.py\", \"and_\"]]",
  "cap": "[\"symbols\", [\"tests/test_make.py\", \"and_\"]]"
 },
 "hedges": [
  {
   "outcome": "ok",
   "word": "almost certainly",
   "p": [
    49,
    50
   ]
  }
 ],
 "adherence": {
  "planned": "[\"symbols\", [\"tests/attr_import_star.py\", \"and_\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 16,
   "path": "tests/attr_import_star.py",
   "filter": "and_",
   "header": {
    "lines": 10,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/attr_import_star.py",
     "name": "*",
     "line": 4,
     "kind": "star",
     "src": "attr",
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": []
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/attr/validators.py",
   "src/attrs/converters.py",
   "src/attrs/exceptions.py",
   "src/attrs/filters.py",
   "src/attrs/setters.py",
   "src/attrs/validators.py",
   "tests/attr_import_star.py",
   "tests/test_make.py",
   "tests/test_next_gen.py",
   "tests/test_validators.py"
  ],
  "table": [
   [
    "src/attr/validators.py",
    "src/attr/validators.py:14",
    "in",
    "`._make` resolves `and_` to the target"
   ],
   [
    "src/attrs/converters.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/attrs/exceptions.py",
    "src/attrs/exceptions.py:3",
    "out",
    "star import of `attr.exceptions`, which does not export `and_`"
   ],
   [
    "src/attrs/filters.py",
    "src/attrs/filters.py:3",
    "out",
    "star import of `attr.filters`, which does not export `and_`"
   ],
   [
    "src/attrs/setters.py",
    "src/attrs/setters.py:3",
    "out",
    "star import of `attr.setters`, which does not export `and_`"
   ],
   [
    "src/attrs/validators.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/attr_import_star.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_make.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_next_gen.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_validators.py",
    "tests/test_validators.py:16",
    "in",
    "`attr.validators` resolves `and_` to the target"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  },
  "n_in": 2,
  "n_out": 3,
  "n_pending": 5
 }
}
```
</details>

## Step 17

The test module `tests/attr_import_star.py` matched the search but has no module-level import of `and_`. It also star-imports `attr`, which could carry the name, so that needs checking.

Tally: 2 import statements confirmed, 3 ruled out, 5 pending. The search itself is complete; what is left is checking the candidates.

Let me look at `tests/test_make.py`'s top-level names for `and_`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will outline `src/attr.py` directly, which both checks that the file exists and shows me `and_`.

**Call:** `symbols('tests/test_make.py', 'and_')`

**Response**: outcome `ok`

```
module tests/test_make.py lines=3213 dynamic=no all=none
29 from and_ <- attr._make and_
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/converters.py"
   ],
   "desc": "read what `src/attr/converters.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/validators.py"
   ],
   "desc": "read what `src/attr/validators.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/attr_import_star.py",
    "attr"
   ],
   "desc": "find where `attr` (imported by `tests/attr_import_star.py`) lives"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "and_"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `and_`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_next_gen.py",
    "and_"
   ],
   "desc": "look at `tests/test_next_gen.py`'s imports of `and_`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr.py', 'and_')",
   "key": "[\"symbols\", [\"src/attr.py\", \"and_\"]]",
   "v1": [
    24964408705043,
    3808975262385
   ],
   "v2": [
    250405882102907,
    38089752623850
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     61864,
     72861
    ],
    "reexport": [
     1628,
     72861
    ],
    "star": [
     148,
     72861
    ],
    "none": [
     2516,
     72861
    ],
    "missing": [
     15,
     163
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/attr_import_star.py",
     "attr"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'and_')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"and_\"]]",
   "v1": [
    3718283,
    503150
   ],
   "v2": [
    250405882102907,
    38089752623850
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_make.py",
     "and_"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_next_gen.py', 'and_')",
   "key": "[\"symbols\", [\"tests/test_next_gen.py\", \"and_\"]]",
   "v1": [
    3718283,
    503150
   ],
   "v2": [
    250405882102907,
    38089752623850
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_next_gen.py",
     "and_"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    12017249,
    1610080
   ],
   "v2": [
    810288004348531,
    121887208396320
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/converters.py"
    ]
   ]
  },
  {
   "call": "read('src/attr/validators.py', 19, 30)",
   "key": "[\"read\", [\"src/attr/validators.py\", 19, 30]]",
   "v1": [
    12017249,
    1610080
   ],
   "v2": [
    810288004348531,
    121887208396320
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/validators.py"
    ]
   ]
  },
  {
   "call": "ls('src')",
   "key": "[\"ls\", [\"src\"]]",
   "v1": [
    19534319,
    2616380
   ],
   "v2": [
    14668398988308679,
    1980667136440200
   ],
   "p_cap": [
    5,
    52
   ],
   "forecast": {
    "complete": [
     47,
     52
    ],
    "cap": [
     5,
     52
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/attr_import_star.py",
     "attr"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/__init__.py', 'and_')",
   "key": "[\"symbols\", [\"src/attr/__init__.py\", \"and_\"]]",
   "v1": [
    1232287619,
    161008000
   ],
   "v2": [
    466636761408264541,
    60943604198160000
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     539,
     2400
    ],
    "reexport": [
     49,
     100
    ],
    "star": [
     49,
     2400
    ],
    "none": [
     49,
     200
    ],
    "missing": [
     1,
     50
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/attr_import_star.py",
     "attr"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_make.py', 'and_')",
  "key": "[\"symbols\", [\"tests/test_make.py\", \"and_\"]]",
  "provenance": "`tests/test_make.py` had a matching line (step 6); its outline names every `and_` import exactly",
  "v2": [
   250405882102907,
   38089752623850
  ]
 },
 "forecast": {
  "ok": [
   49,
   50
  ],
  "cap": [
   1,
   50
  ]
 },
 "plan": {
  "ok": "[\"symbols\", [\"src/attr.py\", \"and_\"]]",
  "cap": "[\"symbols\", [\"src/attr.py\", \"and_\"]]"
 },
 "hedges": [
  {
   "outcome": "ok",
   "word": "almost certainly",
   "p": [
    49,
    50
   ]
  }
 ],
 "adherence": {
  "planned": "[\"symbols\", [\"tests/test_make.py\", \"and_\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 17,
   "path": "tests/test_make.py",
   "filter": "and_",
   "header": {
    "lines": 3213,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_make.py",
     "name": "and_",
     "line": 29,
     "kind": "from",
     "src": "attr._make",
     "src_name": "and_",
     "conditional": false,
     "col": 0,
     "bases": []
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/attr/validators.py",
   "src/attrs/converters.py",
   "src/attrs/exceptions.py",
   "src/attrs/filters.py",
   "src/attrs/setters.py",
   "src/attrs/validators.py",
   "tests/attr_import_star.py",
   "tests/test_make.py",
   "tests/test_next_gen.py",
   "tests/test_validators.py"
  ],
  "table": [
   [
    "src/attr/validators.py",
    "src/attr/validators.py:14",
    "in",
    "`._make` resolves `and_` to the target"
   ],
   [
    "src/attrs/converters.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/att
```
</details>

## Step 18

The test module `tests/test_make.py`: line 29 imports it from `attr._make`.

Tally: 3 import statements confirmed, 3 ruled out, 4 pending. The search itself is complete; what is left is checking the candidates.

Next I will outline `src/attr.py` directly, which both checks that the file exists and shows me `and_`; if `attr` is a plain module that is where it has to be. Very likely it is defined right there. If the file does not exist or the name is not bound there, I will look at `tests/test_next_gen.py`'s top-level names for `and_`.

**Call:** `symbols('src/attr.py', 'and_')`

**Response**: outcome `missing`

```
error: not a python file: src/attr.py
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/converters.py"
   ],
   "desc": "read what `src/attr/converters.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/validators.py"
   ],
   "desc": "read what `src/attr/validators.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/attr_import_star.py",
    "attr"
   ],
   "desc": "find where `attr` (imported by `tests/attr_import_star.py`) lives"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_next_gen.py",
    "and_"
   ],
   "desc": "look at `tests/test_next_gen.py`'s imports of `and_`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr.py', 'and_')",
   "key": "[\"symbols\", [\"src/attr.py\", \"and_\"]]",
   "v1": [
    18651343534496,
    3808975262385
   ],
   "v2": [
    187275230397437,
    38089752623850
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     61864,
     72861
    ],
    "reexport": [
     1628,
     72861
    ],
    "star": [
     148,
     72861
    ],
    "none": [
     2516,
     72861
    ],
    "missing": [
     15,
     163
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/attr_import_star.py",
     "attr"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_next_gen.py', 'and_')",
   "key": "[\"symbols\", [\"tests/test_next_gen.py\", \"and_\"]]",
   "v1": [
    2884353,
    503150
   ],
   "v2": [
    187275230397437,
    38089752623850
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_next_gen.py",
     "and_"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    9348673,
    1610080
   ],
   "v2": [
    608269918891027,
    121887208396320
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/converters.py"
    ]
   ]
  },
  {
   "call": "read('src/attr/validators.py', 19, 30)",
   "key": "[\"read\", [\"src/attr/validators.py\", 19, 30]]",
   "v1": [
    9348673,
    1610080
   ],
   "v2": [
    608269918891027,
    121887208396320
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/validators.py"
    ]
   ]
  },
  {
   "call": "ls('src')",
   "key": "[\"ls\", [\"src\"]]",
   "v1": [
    15197883,
    2616380
   ],
   "v2": [
    11385605099624239,
    1980667136440200
   ],
   "p_cap": [
    5,
    52
   ],
   "forecast": {
    "complete": [
     47,
     52
    ],
    "cap": [
     5,
     52
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/attr_import_star.py",
     "attr"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/__init__.py', 'and_')",
   "key": "[\"symbols\", [\"src/attr/__init__.py\", \"and_\"]]",
   "v1": [
    965430019,
    161008000
   ],
   "v2": [
    365627718679512541,
    60943604198160000
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     539,
     2400
    ],
    "reexport": [
     49,
     100
    ],
    "star": [
     49,
     2400
    ],
    "none": [
     49,
     200
    ],
    "missing": [
     1,
     50
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/attr_import_star.py",
     "attr"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/attr.py', 'and_')",
  "key": "[\"symbols\", [\"src/attr.py\", \"and_\"]]",
  "provenance": "`attr` would be `src/attr.py` if that file exists; one call both checks and closes it",
  "v2": [
   187275230397437,
   38089752623850
  ]
 },
 "forecast": {
  "def": [
   61864,
   72861
  ],
  "reexport": [
   1628,
   72861
  ],
  "star": [
   148,
   72861
  ],
  "none": [
   2516,
   72861
  ],
  "missing": [
   15,
   163
  ]
 },
 "plan": {
  "def": "[\"symbols\", [\"tests/test_next_gen.py\", \"and_\"]]",
  "reexport": "[\"symbols\", [\"tests/test_next_gen.py\", \"and_\"]]",
  "star": "[\"symbols\", [\"tests/test_next_gen.py\", \"and_\"]]",
  "none": "[\"symbols\", [\"tests/test_next_gen.py\", \"and_\"]]",
  "missing": "[\"symbols\", [\"tests/test_next_gen.py\", \"and_\"]]"
 },
 "hedges": [
  {
   "outcome": "def",
   "word": "very likely",
   "p": [
    61864,
    72861
   ]
  }
 ],
 "adherence": {
  "planned": "[\"symbols\", [\"src/attr.py\", \"and_\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "error",
   "step": 18,
   "call": "[\"symbols\", [\"src/attr.py\", \"and_\"]]",
   "error": "not a python file: src/attr.py",
   "missing": "src/attr.py"
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/attr/validators.py",
   "src/attrs/converters.py",
   "src/attrs/exceptions.py",
   "src/attrs/filters.py",
   "src/attrs/setters.py",
   "src/attrs/validators.py",
   "tests/attr_import_star.py",
   "tests/test_make.py",
   "tests/test_next_gen.py",
   "tests/test_validators.py"
  ],
  "table": [
   [
    "src/attr/validators.py",
    "src/attr/validators.py:14",
    "in",
    "`._make` resolves `and_` to the target"
   ],
   [
    "src/attrs/converters.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/attrs/exceptions.py",
    "src/attrs/exceptions.py:3",
    "out",
    "star import of `attr.exceptions`, which does not export `and_`"
   ],
   [
    "src/attrs/filters.py",
    "src/attrs/filters.py:3",
    "out",
    "star import of `attr.filters`, which does not export `and_`"
   ],
   [
    "src/attrs/setters.py",
    "src/attrs/setters.py:3",
    "out",
    "star import of `attr.setters`, which does not export `and_`"
   ],
   [
    "src/attrs/validators.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/attr_import_star.py",
    null,
    "pe
```
</details>

## Step 19

Interesting: there is no `src/attr.py`, so `attr` is either a package (`src/attr/__init__.py`) or not in this repository at all.

I'll look at `tests/test_next_gen.py`'s top-level names for `and_`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will outline `src/attr/__init__.py` directly, which both checks that the file exists and shows me `and_`.

**Call:** `symbols('tests/test_next_gen.py', 'and_')`

**Response**: outcome `ok`

```
module tests/test_next_gen.py lines=586 dynamic=no all=none
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/converters.py"
   ],
   "desc": "read what `src/attr/converters.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/validators.py"
   ],
   "desc": "read what `src/attr/validators.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/attr_import_star.py",
    "attr"
   ],
   "desc": "find where `attr` (imported by `tests/attr_import_star.py`) lives"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_next_gen.py",
    "and_"
   ],
   "desc": "look at `tests/test_next_gen.py`'s imports of `and_`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/__init__.py', 'and_')",
   "key": "[\"symbols\", [\"src/attr/__init__.py\", \"and_\"]]",
   "v1": [
    581702557,
    96604800
   ],
   "v2": [
    583634653,
    96604800
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     539,
     2400
    ],
    "reexport": [
     49,
     100
    ],
    "star": [
     49,
     2400
    ],
    "none": [
     49,
     200
    ],
    "missing": [
     1,
     50
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/attr_import_star.py",
     "attr"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_next_gen.py', 'and_')",
   "key": "[\"symbols\", [\"tests/test_next_gen.py\", \"and_\"]]",
   "v1": [
    42251441,
    6037800
   ],
   "v2": [
    583634653,
    96604800
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_next_gen.py",
     "and_"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    34157383,
    4830240
   ],
   "v2": [
    590759257,
    96604800
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/converters.py"
    ]
   ]
  },
  {
   "call": "read('src/attr/validators.py', 19, 30)",
   "key": "[\"read\", [\"src/attr/validators.py\", 19, 30]]",
   "v1": [
    34157383,
    4830240
   ],
   "v2": [
    590759257,
    96604800
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/validators.py"
    ]
   ]
  },
  {
   "call": "ls('src/attr')",
   "key": "[\"ls\", [\"src/attr\"]]",
   "v1": [
    1885066351,
    269285880
   ],
   "v2": [
    50254854331,
    7180956800
   ],
   "p_cap": [
    5,
    223
   ],
   "forecast": {
    "complete": [
     218,
     223
    ],
    "cap": [
     5,
     223
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/attr_import_star.py",
     "attr"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_next_gen.py', 'and_')",
  "key": "[\"symbols\", [\"tests/test_next_gen.py\", \"and_\"]]",
  "provenance": "`tests/test_next_gen.py` had a matching line (step 6); its outline names every `and_` import exactly",
  "v2": [
   583634653,
   96604800
  ]
 },
 "forecast": {
  "ok": [
   49,
   50
  ],
  "cap": [
   1,
   50
  ]
 },
 "plan": {
  "ok": "[\"symbols\", [\"src/attr/__init__.py\", \"and_\"]]",
  "cap": "[\"symbols\", [\"src/attr/__init__.py\", \"and_\"]]"
 },
 "hedges": [
  {
   "outcome": "ok",
   "word": "almost certainly",
   "p": [
    49,
    50
   ]
  }
 ],
 "adherence": {
  "planned": "[\"symbols\", [\"tests/test_next_gen.py\", \"and_\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 19,
   "path": "tests/test_next_gen.py",
   "filter": "and_",
   "header": {
    "lines": 586,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/attr/validators.py",
   "src/attrs/converters.py",
   "src/attrs/exceptions.py",
   "src/attrs/filters.py",
   "src/attrs/setters.py",
   "src/attrs/validators.py",
   "tests/attr_import_star.py",
   "tests/test_make.py",
   "tests/test_next_gen.py",
   "tests/test_validators.py"
  ],
  "table": [
   [
    "src/attr/validators.py",
    "src/attr/validators.py:14",
    "in",
    "`._make` resolves `and_` to the target"
   ],
   [
    "src/attrs/converters.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/attrs/exceptions.py",
    "src/attrs/exceptions.py:3",
    "out",
    "star import of `attr.exceptions`, which does not export `and_`"
   ],
   [
    "src/attrs/filters.py",
    "src/attrs/filters.py:3",
    "out",
    "star import of `attr.filters`, which does not export `and_`"
   ],
   [
    "src/attrs/setters.py",
    "src/attrs/setters.py:3",
    "out",
    "star import of `attr.setters`, which does not export `and_`"
   ],
   [
    "src/attrs/validators.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/attr_import_star.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_make.py",
    "tests/test_make.py:29",
    "in",
    "`attr._make` resolves `and_` to the target"
   ],
   [
    "tests/test_next_gen.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
   ],
   [
    "tests/test_validators.py",
    "tests/test_validators.py:16",
    "in",
    "`attr.validators` resolves `and_` to the target"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  },
  "n_in": 3,
  "n_out": 3,
  "n_pending": 3
 }
}
```
</details>

## Step 20

The test module `tests/test_next_gen.py` matched the search but has no module-level import of `and_`.

Tally: 3 import statements confirmed, 3 ruled out, 3 pending. The search itself is complete; what is left is checking the candidates.

Next I will outline `src/attr/__init__.py` directly, which both checks that the file exists and shows me `and_`; if `attr` is a plain module that is where it has to be. Maybe it is re-exported from somewhere else. If the name is not bound there or it is defined right there, I will read `__all__` in `src/attr/converters.py`; if the file does not exist, I will list `src/attr/` to see what lives there. I could read `__all__` in `src/attr/converters.py` instead, but it costs more calls in expectation.

**Call:** `symbols('src/attr/__init__.py', 'and_')`

**Response**: outcome `none`

```
module src/attr/__init__.py lines=121 dynamic=yes all=static@45
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/converters.py"
   ],
   "desc": "read what `src/attr/converters.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/validators.py"
   ],
   "desc": "read what `src/attr/validators.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/attr_import_star.py",
    "attr"
   ],
   "desc": "find where `attr` (imported by `tests/attr_import_star.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/__init__.py', 'and_')",
   "key": "[\"symbols\", [\"src/attr/__init__.py\", \"and_\"]]",
   "v1": [
    1214951,
    278400
   ],
   "v2": [
    276665807,
    62083200
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     539,
     2400
    ],
    "reexport": [
     49,
     100
    ],
    "star": [
     49,
     2400
    ],
    "none": [
     49,
     200
    ],
    "missing": [
     1,
     50
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/attr_import_star.py",
     "attr"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    15073,
    2784
   ],
   "v2": [
    1241051,
    278400
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/converters.py"
    ]
   ]
  },
  {
   "call": "read('src/attr/validators.py', 19, 30)",
   "key": "[\"read\", [\"src/attr/validators.py\", 19, 30]]",
   "v1": [
    15073,
    2784
   ],
   "v2": [
    1241051,
    278400
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/validators.py"
    ]
   ]
  },
  {
   "call": "ls('src/attr')",
   "key": "[\"ls\", [\"src/attr\"]]",
   "v1": [
    829249,
    155208
   ],
   "v2": [
    22403877,
    4138880
   ],
   "p_cap": [
    5,
    223
   ],
   "forecast": {
    "complete": [
     218,
     223
    ],
    "cap": [
     5,
     223
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/attr_import_star.py",
     "attr"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/attr/__init__.py', 'and_')",
  "key": "[\"symbols\", [\"src/attr/__init__.py\", \"and_\"]]",
  "provenance": "`attr` would be `src/attr/__init__.py` if that file exists; one call both checks and closes it",
  "v2": [
   276665807,
   62083200
  ]
 },
 "forecast": {
  "def": [
   539,
   2400
  ],
  "reexport": [
   49,
   100
  ],
  "star": [
   49,
   2400
  ],
  "none": [
   49,
   200
  ],
  "missing": [
   1,
   50
  ]
 },
 "plan": {
  "def": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
  "reexport": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
  "star": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
  "none": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
  "missing": "[\"ls\", [\"src/attr\"]]"
 },
 "hedges": [
  {
   "outcome": "reexport",
   "word": "maybe",
   "p": [
    49,
    100
   ]
  }
 ],
 "adherence": {
  "planned": "[\"symbols\", [\"src/attr/__init__.py\", \"and_\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 20,
   "path": "src/attr/__init__.py",
   "filter": "and_",
   "header": {
    "lines": 121,
    "dynamic": true,
    "all_status": "static",
    "all_line": 45
   },
   "bindings": [],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/attr/validators.py",
   "src/attrs/converters.py",
   "src/attrs/exceptions.py",
   "src/attrs/filters.py",
   "src/attrs/setters.py",
   "src/attrs/validators.py",
   "tests/attr_import_star.py",
   "tests/test_make.py",
   "tests/test_next_gen.py",
   "tests/test_validators.py"
  ],
  "table": [
   [
    "src/attr/validators.py",
    "src/attr/validators.py:14",
    "in",
    "`._make` resolves `and_` to the target"
   ],
   [
    "src/attrs/converters.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/attrs/exceptions.py",
    "src/attrs/exceptions.py:3",
    "out",
    "star import of `attr.exceptions`, which does not export `and_`"
   ],
   [
    "src/attrs/filters.py",
    "src/attrs/filters.py:3",
    "out",
    "star import of `attr.filters`, which does not export `and_`"
   ],
   [
    "src/attrs/setters.py",
    "src/attrs/setters.py:3",
    "out",
    "star import of `attr.setters`, which does not export `and_`"
   ],
   [
    "src/attrs/validators.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/attr_import_star.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_make.py",
    "tests/test_make.py:29",
    "in",
    "`attr._make` resolves `and_` to the target"
   ],
   [
    "tests/test_next_gen.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
   ],
   [
    "tests/test_validators.py",
    "tests/test_validators.py:16",
    "in",
    "`attr.validators` resolves `and_` to the target"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  },
  "n_in": 3,
  "n_out": 3,
  "n_pending": 3
 }
}
```
</details>

## Step 21

The package `src/attr` does not bind `and_`; for a package that leaves a submodule called `and_` as the only option. Careful: this module manipulates its namespace dynamically, so static resolution is not reliable here.

Tally: 3 import statements confirmed, 3 ruled out, 3 pending. The search itself is complete; what is left is checking the candidates.

Let me read `__all__` in `src/attr/converters.py`; whether `and_` is in it decides if the star import carries the name. Almost certainly the list fits in one read. If the list runs past the window, I will read `__all__` in `src/attr/__init__.py`.

**Call:** `read('src/attr/converters.py', 11, 30)`

**Response**: outcome `fits`

```
11:__all__ = [
12:    "default_if_none",
13:    "optional",
14:    "pipe",
15:    "to_bool",
16:]
17:
18:
19:def optional(converter):
20:    """
21:    A converter that allows an attribute to be optional. An optional attribute
22:    is one which can be set to `None`.
23:
24:    Type annotations will be inferred from the wrapped converter's, if it has
25:    any.
26:
27:    Args:
28:        converter (typing.Callable):
29:            the converter that is used for non-`None` values.
30:
31:    .. versionadded:: 17.1.0
32:    """
33:
34:    if isinstance(converter, Converter):
35:
... (5 more lines)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/converters.py"
   ],
   "desc": "read what `src/attr/converters.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/validators.py"
   ],
   "desc": "read what `src/attr/validators.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/__init__.py"
   ],
   "desc": "read what `src/attr/__init__.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "read('src/attr/__init__.py', 45, 30)",
   "key": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]",
   "v1": [
    99,
    32
   ],
   "v2": [
    51,
    16
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/__init__.py"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    99,
    32
   ],
   "v2": [
    51,
    16
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/converters.py"
    ]
   ]
  },
  {
   "call": "read('src/attr/validators.py', 19, 30)",
   "key": "[\"read\", [\"src/attr/validators.py\", 19, 30]]",
   "v1": [
    99,
    32
   ],
   "v2": [
    51,
    16
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/validators.py"
    ]
   ]
  }
 ],
 "choice": {
  "call": "read('src/attr/converters.py', 11, 30)",
  "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
  "provenance": "`__all__` of `src/attr/converters.py` starts at line 11 (outline header)",
  "v2": [
   51,
   16
  ]
 },
 "forecast": {
  "fits": [
   29,
   32
  ],
  "long": [
   3,
   32
  ]
 },
 "plan": {
  "fits": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]",
  "long": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]"
 },
 "hedges": [
  {
   "outcome": "fits",
   "word": "almost certainly",
   "p": [
    29,
    32
   ]
  }
 ],
 "adherence": {
  "planned": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "read",
   "step": 21,
   "path": "src/attr/converters.py",
   "start": 11,
   "count": 30,
   "n": 30
  },
  {
   "kind": "all_names",
   "step": 21,
   "path": "src/attr/converters.py",
   "value": [
    "default_if_none",
    "optional",
    "pipe",
    "to_bool"
   ]
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/attr/validators.py",
   "src/attrs/converters.py",
   "src/attrs/exceptions.py",
   "src/attrs/filters.py",
   "src/attrs/setters.py",
   "src/attrs/validators.py",
   "tests/attr_import_star.py",
   "tests/test_make.py",
   "tests/test_next_gen.py",
   "tests/test_validators.py"
  ],
  "table": [
   [
    "src/attr/validators.py",
    "src/attr/validators.py:14",
    "in",
    "`._make` resolves `and_` to the target"
   ],
   [
    "src/attrs/converters.py",
    "src/attrs/converters.py:3",
    "out",
    "star import of `attr.converters`, which does not export `and_`"
   ],
   [
    "src/attrs/exceptions.py",
    "src/attrs/exceptions.py:3",
    "out",
    "star import of `attr.exceptions`, which does not export `and_`"
   ],
   [
    "src/attrs/filters.py",
    "src/attrs/filters.py:3",
    "out",
    "star import of `attr.filters`, which does not export `and_`"
   ],
   [
    "src/attrs/setters.py",
    "src/attrs/setters.py:3",
    "out",
    "star import of `attr.setters`, which does not export `and_`"
   ],
   [
    "src/attrs/validators.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/attr_import_star.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_make.py",
    "tests/test_make.py:29",
    "in",
    "`attr._make` resolves `and_` to the target"
   ],
   [
    "tests/test_next_gen.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
   ],
   [
    "tests/test_validators.py",
    "tests/test_validators.py:16",
    "in",
    "`attr.validators` resolves `and_` to the target"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  },
  "n_in": 3,
  "n_out": 4,
  "n_pending": 2
 }
}
```
</details>

## Step 22

`__all__` in `src/attr/converters.py` lists 4 names and `and_` is not among them, so that star import does not carry it.

Next I will read `__all__` in `src/attr/__init__.py`; whether `and_` is in it decides if the star import carries the name. Almost certainly the list fits in one read. If the list runs past the window, I will read `__all__` in `src/attr/validators.py`.

**Call:** `read('src/attr/__init__.py', 45, 30)`

**Response**: outcome `long`

```
45:__all__ = [
46:    "NOTHING",
47:    "Attribute",
48:    "AttrsInstance",
49:    "Converter",
50:    "Factory",
51:    "NothingType",
52:    "asdict",
53:    "assoc",
54:    "astuple",
55:    "attr",
56:    "attrib",
57:    "attributes",
58:    "attrs",
59:    "cmp_using",
60:    "converters",
61:    "define",
62:    "evolve",
63:    "exceptions",
64:    "field",
65:    "fields",
66:    "fields_dict",
67:    "filters",
68:    "frozen",
69:    "get_run_validators",
... (5 more lines)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/validators.py"
   ],
   "desc": "read what `src/attr/validators.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/__init__.py"
   ],
   "desc": "read what `src/attr/__init__.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "read('src/attr/__init__.py', 45, 30)",
   "key": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]",
   "v1": [
    67,
    32
   ],
   "v2": [
    35,
    16
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/__init__.py"
    ]
   ]
  },
  {
   "call": "read('src/attr/validators.py', 19, 30)",
   "key": "[\"read\", [\"src/attr/validators.py\", 19, 30]]",
   "v1": [
    67,
    32
   ],
   "v2": [
    35,
    16
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/validators.py"
    ]
   ]
  }
 ],
 "choice": {
  "call": "read('src/attr/__init__.py', 45, 30)",
  "key": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]",
  "provenance": "`__all__` of `src/attr/__init__.py` starts at line 45 (outline header)",
  "v2": [
   35,
   16
  ]
 },
 "forecast": {
  "fits": [
   29,
   32
  ],
  "long": [
   3,
   32
  ]
 },
 "plan": {
  "fits": "[\"read\", [\"src/attr/validators.py\", 19, 30]]",
  "long": "[\"read\", [\"src/attr/validators.py\", 19, 30]]"
 },
 "hedges": [
  {
   "outcome": "fits",
   "word": "almost certainly",
   "p": [
    29,
    32
   ]
  }
 ],
 "adherence": {
  "planned": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "read",
   "step": 22,
   "path": "src/attr/__init__.py",
   "start": 45,
   "count": 30,
   "n": 30
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/attr/validators.py",
   "src/attrs/converters.py",
   "src/attrs/exceptions.py",
   "src/attrs/filters.py",
   "src/attrs/setters.py",
   "src/attrs/validators.py",
   "tests/attr_import_star.py",
   "tests/test_make.py",
   "tests/test_next_gen.py",
   "tests/test_validators.py"
  ],
  "table": [
   [
    "src/attr/validators.py",
    "src/attr/validators.py:14",
    "in",
    "`._make` resolves `and_` to the target"
   ],
   [
    "src/attrs/converters.py",
    "src/attrs/converters.py:3",
    "out",
    "star import of `attr.converters`, which does not export `and_`"
   ],
   [
    "src/attrs/exceptions.py",
    "src/attrs/exceptions.py:3",
    "out",
    "star import of `attr.exceptions`, which does not export `and_`"
   ],
   [
    "src/attrs/filters.py",
    "src/attrs/filters.py:3",
    "out",
    "star import of `attr.filters`, which does not export `and_`"
   ],
   [
    "src/attrs/setters.py",
    "src/attrs/setters.py:3",
    "out",
    "star import of `attr.setters`, which does not export `and_`"
   ],
   [
    "src/attrs/validators.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/attr_import_star.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_make.py",
    "tests/test_make.py:29",
    "in",
    "`attr._make` resolves `and_` to the target"
   ],
   [
    "tests/test_next_gen.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
   ],
   [
    "tests/test_validators.py",
    "tests/test_validators.py:16",
    "in",
    "`attr.validators` resolves `and_` to the target"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  },
  "n_in": 3,
  "n_out": 4,
  "n_pending": 2
 }
}
```
</details>

## Step 23

That did not tell me anything new.

I'll read `__all__` in `src/attr/validators.py`; whether `and_` is in it decides if the star import carries the name. Almost certainly the list fits in one read. If the list runs past the window, I will read `__all__` in `src/attr/__init__.py`.

**Call:** `read('src/attr/validators.py', 19, 30)`

**Response**: outcome `fits`

```
19:__all__ = [
20:    "and_",
21:    "deep_iterable",
22:    "deep_mapping",
23:    "disabled",
24:    "ge",
25:    "get_disabled",
26:    "gt",
27:    "in_",
28:    "instance_of",
29:    "is_callable",
30:    "le",
31:    "lt",
32:    "matches_re",
33:    "max_len",
34:    "min_len",
35:    "ne",
36:    "not_",
37:    "optional",
38:    "or_",
39:    "set_disabled",
40:]
41:
42:
43:def set_disabled(disabled):
... (5 more lines)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/validators.py"
   ],
   "desc": "read what `src/attr/validators.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/__init__.py"
   ],
   "desc": "read what `src/attr/__init__.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "read('src/attr/__init__.py', 45, 60)",
   "key": "[\"read\", [\"src/attr/__init__.py\", 45, 60]]",
   "v1": [
    67,
    32
   ],
   "v2": [
    35,
    16
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/__init__.py"
    ]
   ]
  },
  {
   "call": "read('src/attr/validators.py', 19, 30)",
   "key": "[\"read\", [\"src/attr/validators.py\", 19, 30]]",
   "v1": [
    67,
    32
   ],
   "v2": [
    35,
    16
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/validators.py"
    ]
   ]
  }
 ],
 "choice": {
  "call": "read('src/attr/validators.py', 19, 30)",
  "key": "[\"read\", [\"src/attr/validators.py\", 19, 30]]",
  "provenance": "`__all__` of `src/attr/validators.py` starts at line 19 (outline header)",
  "v2": [
   35,
   16
  ]
 },
 "forecast": {
  "fits": [
   29,
   32
  ],
  "long": [
   3,
   32
  ]
 },
 "plan": {
  "fits": "[\"read\", [\"src/attr/__init__.py\", 45, 60]]",
  "long": "[\"read\", [\"src/attr/__init__.py\", 45, 60]]"
 },
 "hedges": [
  {
   "outcome": "fits",
   "word": "almost certainly",
   "p": [
    29,
    32
   ]
  }
 ],
 "adherence": {
  "planned": "[\"read\", [\"src/attr/validators.py\", 19, 30]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "read",
   "step": 23,
   "path": "src/attr/validators.py",
   "start": 19,
   "count": 30,
   "n": 30
  },
  {
   "kind": "all_names",
   "step": 23,
   "path": "src/attr/validators.py",
   "value": [
    "and_",
    "deep_iterable",
    "deep_mapping",
    "disabled",
    "ge",
    "get_disabled",
    "gt",
    "in_",
    "instance_of",
    "is_callable",
    "le",
    "lt",
    "matches_re",
    "max_len",
    "min_len",
    "ne",
    "not_",
    "optional",
    "or_",
    "set_disabled"
   ]
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/attr/validators.py",
   "src/attrs/converters.py",
   "src/attrs/exceptions.py",
   "src/attrs/filters.py",
   "src/attrs/setters.py",
   "src/attrs/validators.py",
   "tests/attr_import_star.py",
   "tests/test_make.py",
   "tests/test_next_gen.py",
   "tests/test_validators.py"
  ],
  "table": [
   [
    "src/attr/validators.py",
    "src/attr/validators.py:14",
    "in",
    "`._make` resolves `and_` to the target"
   ],
   [
    "src/attrs/converters.py",
    "src/attrs/converters.py:3",
    "out",
    "star import of `attr.converters`, which does not export `and_`"
   ],
   [
    "src/attrs/exceptions.py",
    "src/attrs/exceptions.py:3",
    "out",
    "star import of `attr.exceptions`, which does not export `and_`"
   ],
   [
    "src/attrs/filters.py",
    "src/attrs/filters.py:3",
    "out",
    "star import of `attr.filters`, which does not export `and_`"
   ],
   [
    "src/attrs/setters.py",
    "src/attrs/setters.py:3",
    "out",
    "star import of `attr.setters`, which does not export `and_`"
   ],
   [
    "src/attrs/validators.py",
    "src/attrs/validators.py:3",
    "in",
    "star import of `attr.validators`, which exports `and_` from the target"
   ],
   [
    "tests/attr_import_star.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_make.py",
    "tests/test_make.py:29",
    "in",
    "`attr._make` resolves `and_` to the target"
   ],
   [
    "tests/test_next_gen.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
   ],
   [
    "tests/test_validators.py",
    "tests/test_validators.py:16",
    "in",
    "`attr.validators` resolves `and_` to the target"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  },
  "n_in": 4,
  "n_out": 4,
  "n_pending": 1
 }
}
```
</details>

## Step 24

`__all__` in `src/attr/validators.py` lists 20 names and `and_` is one of them, so its star import does carry the name.

Tally: 4 import statements confirmed, 4 ruled out, 1 pending. The search itself is complete; what is left is checking the candidates.

Let me read `__all__` in `src/attr/__init__.py`; whether `and_` is in it decides if the star import carries the name. Almost certainly the list fits in one read. If the list runs past the window, I follow whatever it opens up.

**Call:** `read('src/attr/__init__.py', 45, 60)`

**Response**: outcome `fits`

```
45:__all__ = [
46:    "NOTHING",
47:    "Attribute",
48:    "AttrsInstance",
49:    "Converter",
50:    "Factory",
51:    "NothingType",
52:    "asdict",
53:    "assoc",
54:    "astuple",
55:    "attr",
56:    "attrib",
57:    "attributes",
58:    "attrs",
59:    "cmp_using",
60:    "converters",
61:    "define",
62:    "evolve",
63:    "exceptions",
64:    "field",
65:    "fields",
66:    "fields_dict",
67:    "filters",
68:    "frozen",
69:    "get_run_validators",
... (35 more lines)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/__init__.py"
   ],
   "desc": "read what `src/attr/__init__.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "read('src/attr/__init__.py', 45, 60)",
   "key": "[\"read\", [\"src/attr/__init__.py\", 45, 60]]",
   "v1": [
    35,
    32
   ],
   "v2": [
    35,
    32
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/__init__.py"
    ]
   ]
  }
 ],
 "choice": {
  "call": "read('src/attr/__init__.py', 45, 60)",
  "key": "[\"read\", [\"src/attr/__init__.py\", 45, 60]]",
  "provenance": "`__all__` of `src/attr/__init__.py` starts at line 45 (outline header)",
  "v2": [
   35,
   32
  ]
 },
 "forecast": {
  "fits": [
   29,
   32
  ],
  "long": [
   3,
   32
  ]
 },
 "plan": {
  "fits": "done",
  "long": "continue"
 },
 "hedges": [
  {
   "outcome": "fits",
   "word": "almost certainly",
   "p": [
    29,
    32
   ]
  }
 ],
 "adherence": {
  "planned": "[\"read\", [\"src/attr/__init__.py\", 45, 60]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "read",
   "step": 24,
   "path": "src/attr/__init__.py",
   "start": 45,
   "count": 60,
   "n": 60
  },
  {
   "kind": "all_names",
   "step": 24,
   "path": "src/attr/__init__.py",
   "value": [
    "NOTHING",
    "Attribute",
    "AttrsInstance",
    "Converter",
    "Factory",
    "NothingType",
    "asdict",
    "assoc",
    "astuple",
    "attr",
    "attrib",
    "attributes",
    "attrs",
    "cmp_using",
    "converters",
    "define",
    "evolve",
    "exceptions",
    "field",
    "fields",
    "fields_dict",
    "filters",
    "frozen",
    "get_run_validators",
    "has",
    "ib",
    "make_class",
    "mutable",
    "resolve_types",
    "s",
    "set_run_validators",
    "setters",
    "validate",
    "validators"
   ]
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/attr/validators.py",
   "src/attrs/converters.py",
   "src/attrs/exceptions.py",
   "src/attrs/filters.py",
   "src/attrs/setters.py",
   "src/attrs/validators.py",
   "tests/attr_import_star.py",
   "tests/test_make.py",
   "tests/test_next_gen.py",
   "tests/test_validators.py"
  ],
  "table": [
   [
    "src/attr/validators.py",
    "src/attr/validators.py:14",
    "in",
    "`._make` resolves `and_` to the target"
   ],
   [
    "src/attrs/converters.py",
    "src/attrs/converters.py:3",
    "out",
    "star import of `attr.converters`, which does not export `and_`"
   ],
   [
    "src/attrs/exceptions.py",
    "src/attrs/exceptions.py:3",
    "out",
    "star import of `attr.exceptions`, which does not export `and_`"
   ],
   [
    "src/attrs/filters.py",
    "src/attrs/filters.py:3",
    "out",
    "star import of `attr.filters`, which does not export `and_`"
   ],
   [
    "src/attrs/setters.py",
    "src/attrs/setters.py:3",
    "out",
    "star import of `attr.setters`, which does not export `and_`"
   ],
   [
    "src/attrs/validators.py",
    "src/attrs/validators.py:3",
    "in",
    "star import of `attr.validators`, which exports `and_` from the target"
   ],
   [
    "tests/attr_import_star.py",
    "tests/attr_import_star.py:4",
    "out",
    "star import of `attr`, which does not export `and_`"
   ],
   [
    "tests/test_make.py",
    "tests/test_make.py:29",
    "in",
    "`attr._make` resolves `and_` to the target"
   ],
   [
    "tests/test_next_gen.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
   ],
   [
    "tests/test_validators.py",
    "tests/test_validators.py:16",
    "in",
    "`attr.validators` resolves `and_` to the target"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  },
  "n_in": 4,
  "n_out": 5,
  "n_pending": 0
 }
}
```
</details>

## Final

`and_` is the def at `src/attr/_make.py:3381`. 4 module-level import statements bring in this definition: `src/attr/validators.py:14`, `src/attrs/validators.py:3`, `tests/test_make.py:29`, `tests/test_validators.py:16`. Ruled out along the way: `src/attrs/converters.py:3` (star import of `attr.converters`, which does not export `and_`); `src/attrs/exceptions.py:3` (star import of `attr.exceptions`, which does not export `and_`). Looking back, 1 of 24 calls did not end up mattering (step 22).

**Answer:** `{"final_kind": "importers", "final": ["src/attr/validators.py:14", "src/attrs/validators.py:3", "tests/test_make.py:29", "tests/test_validators.py:16"], "steps": [{"op": "resolve", "output": {"kind": "def", "path": "src/attr/_make.py", "line": 3381, "name": "and_", "detail": "def"}}, {"op": "importers", "output": ["src/attr/validators.py:14", "src/attrs/validators.py:3", "tests/test_make.py:29", "tests/test_validators.py:16"]}], "stuck": null}`  
**Stopped:** certificate after 24 calls