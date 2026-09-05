# attrs-resolve-4f2016a5

**Repository:** attrs  
**Chain:** resolve  
**Seed:** 0, prior 0ac2a510ad43644e, floor 3

## Task

In `tests/test_converters.py` line 15, `pipe` is imported from `attr.converters`. Which definition does the module-level name `pipe` actually refer to? Give `path:line`.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N; bindings take effect in source order. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. A class derives from a definition when a base written as a bare name or `module.Name` resolves to it. A call site is `name(...)` where the bare name refers to the module-level binding (not a parameter or local). Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

I need to find what `pipe` really is in `tests/test_converters.py`: line 15 imports it from `attr.converters`, so the definition is at least one hop away.

Next I will check `tests/test_converters.py` for any other binding of `pipe` besides the import on line 15; almost certainly the import is the only one, and then `attr.converters` is the place to follow.

**Call:** `symbols('tests/test_converters.py', 'pipe')`

**Response**: outcome `reexport`

```
module tests/test_converters.py lines=367 dynamic=no all=none
15 from pipe <- attr.converters pipe
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "tests/test_converters.py",
    "pipe"
   ],
   "desc": "check the top-level names of `tests/test_converters.py` for `pipe`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/test_converters.py', 'pipe')",
   "key": "[\"symbols\", [\"tests/test_converters.py\", \"pipe\"]]",
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
     "tests/test_converters.py",
     "pipe"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_converters.py')",
   "key": "[\"symbols\", [\"tests/test_converters.py\"]]",
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
     "tests/test_converters.py",
     "pipe"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_converters.py', 'pipe')",
  "key": "[\"symbols\", [\"tests/test_converters.py\", \"pipe\"]]",
  "provenance": "module `tests/test_converters.py` (task), name `pipe` (task)",
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
   "path": "tests/test_converters.py",
   "filter": "pipe",
   "header": {
    "lines": 367,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_converters.py",
     "name": "pipe",
     "line": 15,
     "kind": "from",
     "src": "attr.converters",
     "src_name": "pipe",
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
  "of": 1,
  "chain": [
   [
    "tests/test_converters.py",
    "pipe",
    "reexport",
    [
     "attr.converters",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 2

The test module `tests/test_converters.py` does not define `pipe` itself; line 15 imports it from `attr.converters`.

So far: `tests/test_converters.py` takes `pipe` from `attr.converters`, which I still have to locate.

Let me list `./` to see what lives there; the listing settles whether the import is a module, a package, or not here at all. Very likely the listing fits. If the listing is too long, I will outline `attr/converters.py` directly, which both checks that the file exists and shows me `pipe`. I could outline `attr/converters.py` directly, which both checks that the file exists and shows me `pipe` instead, but it costs more calls in expectation.

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
    "tests/test_converters.py",
    "attr.converters"
   ],
   "desc": "find where `attr.converters` (imported by `tests/test_converters.py`) lives"
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
     "tests/test_converters.py",
     "attr.converters"
    ]
   ]
  },
  {
   "call": "symbols('attr/converters.py', 'pipe')",
   "key": "[\"symbols\", [\"attr/converters.py\", \"pipe\"]]",
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
     "tests/test_converters.py",
     "attr.converters"
    ]
   ]
  },
  {
   "call": "symbols('attr/converters/__init__.py', 'pipe')",
   "key": "[\"symbols\", [\"attr/converters/__init__.py\", \"pipe\"]]",
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
     "tests/test_converters.py",
     "attr.converters"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+pipe\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+pipe\\\\b\", \".\"]]",
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
     "tests/test_converters.py",
     "attr.converters"
    ]
   ]
  }
 ],
 "choice": {
  "call": "ls('.')",
  "key": "[\"ls\", [\".\"]]",
  "provenance": "`attr.converters` imported by `tests/test_converters.py` should live under `.`",
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
  "cap": "[\"symbols\", [\"attr/converters.py\", \"pipe\"]]"
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
  "of": 1,
  "chain": [
   [
    "tests/test_converters.py",
    "pipe",
    "reexport",
    [
     "attr.converters",
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

So far: `tests/test_converters.py` takes `pipe` from `attr.converters`, which I still have to locate.

I'll search the whole tree for `class pipe`/`def pipe`; that shows where the definition lives and whether the name is reused. Almost certainly it fits under the cap. If it caps or nothing turns up, I will list `src/` to see what lives there. I could list `src/` to see what lives there instead, but it costs more calls in expectation.

**Call:** `grep('^\\s*(?:async\\s+)?(?:def|class)\\s+pipe\\b', '.')`

**Response**: outcome `mid`

```
src/attr/_make.py:3404:def pipe(*converters):
src/attr/converters.pyi:6:def pipe(*validators: _CallableConverterType) -> _CallableConverterType: ...
src/attr/converters.pyi:8:def pipe(*validators: _ConverterType) -> _ConverterType: ...
src/attr/setters.py:11:def pipe(*setters):
src/attr/setters.pyi:11:def pipe(*setters: _OnSetAttrType) -> _OnSetAttrType: ...
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_converters.py",
    "attr.converters"
   ],
   "desc": "find where `attr.converters` (imported by `tests/test_converters.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+pipe\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+pipe\\\\b\", \".\"]]",
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
     "tests/test_converters.py",
     "attr.converters"
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
     "tests/test_converters.py",
     "attr.converters"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/converters.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attr/converters.py\", \"pipe\"]]",
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
     "tests/test_converters.py",
     "attr.converters"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+pipe\\\\b', 'src')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+pipe\\\\b\", \"src\"]]",
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
     "tests/test_converters.py",
     "attr.converters"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/converters/__init__.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attr/converters/__init__.py\", \"pipe\"]]",
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
     "tests/test_converters.py",
     "attr.converters"
    ]
   ]
  }
 ],
 "choice": {
  "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+pipe\\\\b', '.')",
  "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+pipe\\\\b\", \".\"]]",
  "provenance": "a `def`/`class pipe` statement would reveal the module file; `pipe` task",
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
   "pattern": "^\\s*(?:async\\s+)?(?:def|class)\\s+pipe\\b",
   "scope": ".",
   "hits": [
    [
     "src/attr/_make.py",
     3404
    ],
    [
     "src/attr/converters.pyi",
     6
    ],
    [
     "src/attr/converters.pyi",
     8
    ],
    [
     "src/attr/setters.py",
     11
    ],
    [
     "src/attr/setters.pyi",
     11
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "phase": "resolve",
  "step": 1,
  "of": 1,
  "chain": [
   [
    "tests/test_converters.py",
    "pipe",
    "reexport",
    [
     "attr.converters",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 4

`pipe` is defined 5 times: `src/attr/_make.py`, `src/attr/converters.pyi`, `src/attr/setters.py`, `src/attr/setters.pyi`. Only one of them can be the one this import means, so the import chain decides.

So far: `tests/test_converters.py` takes `pipe` from `attr.converters`, which I still have to locate.

I'll outline `src/attr/converters.py` directly, which both checks that the file exists and shows me `pipe`; if `attr.converters` is a plain module that is where it has to be. Very likely it is defined right there. If the file does not exist, I will list `src/attr/` to see what lives there; if the name is not bound there, that finishes it. I could list `src/attr/` to see what lives there instead, but it tends to open more follow-up work.

**Call:** `symbols('src/attr/converters.py', 'pipe')`

**Response**: outcome `reexport`

```
module src/attr/converters.py lines=161 dynamic=no all=static@11
8 from pipe <- ._make pipe
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_converters.py",
    "attr.converters"
   ],
   "desc": "find where `attr.converters` (imported by `tests/test_converters.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/converters.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attr/converters.py\", \"pipe\"]]",
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
     "tests/test_converters.py",
     "attr.converters"
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
     "tests/test_converters.py",
     "attr.converters"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/converters/__init__.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attr/converters/__init__.py\", \"pipe\"]]",
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
     "tests/test_converters.py",
     "attr.converters"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/attr/converters.py', 'pipe')",
  "key": "[\"symbols\", [\"src/attr/converters.py\", \"pipe\"]]",
  "provenance": "`attr.converters` would be `src/attr/converters.py` if that file exists; one call both checks and closes it",
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
   "path": "src/attr/converters.py",
   "filter": "pipe",
   "header": {
    "lines": 161,
    "dynamic": false,
    "all_status": "static",
    "all_line": 11
   },
   "bindings": [
    {
     "module": "src/attr/converters.py",
     "name": "pipe",
     "line": 8,
     "kind": "from",
     "src": "._make",
     "src_name": "pipe",
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
  "of": 1,
  "chain": [
   [
    "tests/test_converters.py",
    "pipe",
    "reexport",
    [
     "attr.converters",
     "src/attr/converters.py"
    ]
   ],
   [
    "src/attr/converters.py",
    "pipe",
    "reexport",
    [
     "._make",
     "src/attr/_make.py"
    ]
   ],
   [
    "src/attr/_make.py",
    "pipe",
    "open",
    null
   ]
  ]
 }
}
```
</details>

## Step 5

Huh: `src/attr/converters.py` does not define `pipe` itself; line 8 imports it from `._make`.

So far: `tests/test_converters.py` takes `pipe` from `attr.converters`; `src/attr/converters.py` takes `pipe` from `._make`; `src/attr/_make.py` is next.

I'll look at `src/attr/_make.py`'s top-level names for `pipe`; that settles what the name means there. Almost certainly it is defined right there. If the name is not bound there, that finishes it; if it is re-exported from somewhere else, I follow whatever it opens up. I could outline all of `src/attr/_make.py` instead, but it is more likely to hit the cap.

**Call:** `symbols('src/attr/_make.py', 'pipe')`

**Response**: outcome `def`

```
module src/attr/_make.py lines=3463 dynamic=no all=none
3404 def pipe
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
    "pipe"
   ],
   "desc": "check the top-level names of `src/attr/_make.py` for `pipe`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/_make.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attr/_make.py\", \"pipe\"]]",
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
     "pipe"
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
     "pipe"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/attr/_make.py', 'pipe')",
  "key": "[\"symbols\", [\"src/attr/_make.py\", \"pipe\"]]",
  "provenance": "module `src/attr/_make.py` (step 3), name `pipe` (task)",
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
   "filter": "pipe",
   "header": {
    "lines": 3463,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/attr/_make.py",
     "name": "pipe",
     "line": 3404,
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
  "of": 1,
  "chain": [
   [
    "tests/test_converters.py",
    "pipe",
    "reexport",
    [
     "attr.converters",
     "src/attr/converters.py"
    ]
   ],
   [
    "src/attr/converters.py",
    "pipe",
    "reexport",
    [
     "._make",
     "src/attr/_make.py"
    ]
   ],
   [
    "src/attr/_make.py",
    "pipe",
    "def",
    3404
   ]
  ]
 }
}
```
</details>

## Final

`pipe` is the def at `src/attr/_make.py:3404`. Looking back, all 5 calls were needed.

**Answer:** `{"final_kind": "resolve", "final": {"kind": "def", "path": "src/attr/_make.py", "line": 3404, "name": "pipe", "detail": "def"}, "steps": [{"op": "resolve", "output": {"kind": "def", "path": "src/attr/_make.py", "line": 3404, "name": "pipe", "detail": "def"}}], "stuck": null}`  
**Stopped:** certificate after 5 calls