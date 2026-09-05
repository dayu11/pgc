# pytest-resolve-09b34f57

**Repository:** pytest  
**Family:** resolve  
**Seed:** 0, prior 0140c5bd99319f8c

## Task

In `src/pytest/__init__.py`, line 25 imports `pytestPDB` from `_pytest.debugging` as `__pytestPDB`. Under the declared semantics, which definition does the module-level name `__pytestPDB` bound by this statement resolve to? Answer with `path:line`.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

Nothing seen yet beyond the task text.

Chain: `src/pytest/__init__.py` is not yet closed for `__pytestPDB`.

Outstanding: close the namespace of `src/pytest/__init__.py` for `__pytestPDB`.

Next: outline `src/pytest/__init__.py`, because module `src/pytest/__init__.py` (task). I expect: a re-export continues the chain to its source (about 50%); no binding at all points at a submodule or an unresolved name (about 25%); a capped outline means filtering by name (about 15%); a definition there ends the chain (about 10%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `src/pytest/__init__.py` filtered to `__pytestPDB`, is expected to open more follow-up work. Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: check for a submodule of that name; cap: outline `src/pytest/__init__.py` filtered to `__pytestPDB`.

**Call:** `symbols('src/pytest/__init__.py')`

**Response** (capped): outcome `cap`

```
module src/pytest/__init__.py lines=191 dynamic=no all=static@100
4 from annotations <- __future__ annotations
6 from __version__ <- _pytest __version__
7 from version_tuple <- _pytest version_tuple
8 from ExceptionInfo <- _pytest._code ExceptionInfo
9 from Approx <- _pytest.approx Approx
10 from approx <- _pytest.approx approx
11 from register_assert_rewrite <- _pytest.assertion register_assert_rewrite
12 from Cache <- _pytest.cacheprovider Cache
13 from CaptureFixture <- _pytest.capture CaptureFixture
14 from cmdline <- _pytest.config cmdline
15 from Config <- _pytest.config Config
16 from console_main <- _pytest.config console_main
17 from ExitCode <- _pytest.config ExitCode
18 from hookimpl <- _pytest.config hookimpl
19 from hookspec <- _pytest.config hookspec
20 from main <- _pytest.config main
21 from PytestPluginManager <- _pytest.config PytestPluginManager
22 from UsageError <- _pytest.config UsageError
23 from OptionGroup <- _pytest.config.argparsing OptionGroup
24 from Parser <- _pytest.config.argparsing Parser
25 from __pytestPDB <- _pytest.debugging pytestPDB
26 from DoctestItem <- _pytest.doctest DoctestItem
27 from fixture <- _pytest.fixtures fixture
28 from FixtureDef <- _pytest.fixtures FixtureDef
... (16 more lines)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/pytest/__init__.py",
    "__pytestPDB"
   ],
   "desc": "close the namespace of `src/pytest/__init__.py` for `__pytestPDB`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/pytest/__init__.py')",
   "key": "[\"symbols\", [\"src/pytest/__init__.py\"]]",
   "v1": [
    1491533,
    549024
   ],
   "v2": [
    133349473,
    48039600
   ],
   "p_cap": [
    1,
    7
   ],
   "forecast": {
    "def": [
     15,
     196
    ],
    "reexport": [
     51,
     98
    ],
    "star": [
     3,
     196
    ],
    "none": [
     12,
     49
    ],
    "cap": [
     1,
     7
    ]
   },
   "serves": [
    [
     "bindings",
     "src/pytest/__init__.py",
     "__pytestPDB"
    ]
   ]
  },
  {
   "call": "symbols('src/pytest/__init__.py', '__pytestPDB')",
   "key": "[\"symbols\", [\"src/pytest/__init__.py\", \"__pytestPDB\"]]",
   "v1": [
    1463357,
    490200
   ],
   "v2": [
    1463357,
    490200
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
     "src/pytest/__init__.py",
     "__pytestPDB"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/pytest/__init__.py')",
  "key": "[\"symbols\", [\"src/pytest/__init__.py\"]]",
  "provenance": "module `src/pytest/__init__.py` (task)",
  "v2": [
   133349473,
   48039600
  ]
 },
 "forecast": {
  "def": [
   15,
   196
  ],
  "reexport": [
   51,
   98
  ],
  "star": [
   3,
   196
  ],
  "none": [
   12,
   49
  ],
  "cap": [
   1,
   7
  ]
 },
 "plan": {
  "def": "done",
  "reexport": "continue",
  "star": "continue",
  "none": "continue",
  "cap": "[\"symbols\", [\"src/pytest/__init__.py\", \"__pytestPDB\"]]"
 },
 "adherence": null,
 "facts": [
  {
   "kind": "outline",
   "step": 1,
   "path": "src/pytest/__init__.py",
   "filter": null,
   "header": {
    "lines": 191,
    "dynamic": false,
    "all_status": "static",
    "all_line": 100
   },
   "bindings": [
    {
     "module": "src/pytest/__init__.py",
     "name": "annotations",
     "line": 4,
     "kind": "from",
     "src": "__future__",
     "src_name": "annotations",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/pytest/__init__.py",
     "name": "__version__",
     "line": 6,
     "kind": "from",
     "src": "_pytest",
     "src_name": "__version__",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/pytest/__init__.py",
     "name": "version_tuple",
     "line": 7,
     "kind": "from",
     "src": "_pytest",
     "src_name": "version_tuple",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/pytest/__init__.py",
     "name": "ExceptionInfo",
     "line": 8,
     "kind": "from",
     "src": "_pytest._code",
     "src_name": "ExceptionInfo",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/pytest/__init__.py",
     "name": "Approx",
     "line": 9,
     "kind": "from",
     "src": "_pytest.approx",
     "src_name": "Approx",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/pytest/__init__.py",
     "name": "approx",
     "line": 10,
     "kind": "from",
     "src": "_pytest.approx",
     "src_name": "approx",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/pytest/__init__.py",
     "name": "register_assert_rewrite",
     "line": 11,
     "kind": "from",
     "src": "_pytest.assertion",
     "src_name": "register_assert_rewrite",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/pytest/__init__.py",
     "name": "Cache",
     "line": 12,
     "kind": "from",
     "src": "_pytest.cacheprovider",
     "src_name": "Cache",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/pytest/__init__.py",
     "name": "CaptureFixture",
     "line": 13,
     "kind": "from",
     "src": "_pytest.capture",
     "src_name": "CaptureFixture",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/pytest/__init__.py",
     "name": "cmdline",
     "line": 14,
     "kind": "from",
     "src": "_pytest.config",
     "src_name": "cmdline",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/pytest/__init__.py",
     "name": "Config",
     "line": 15,
     "kind": "from",
     "src": "_pytest.config",
     "src_name": "Config",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/pytest/__init__.py",
     "name": "console_main",
     "line": 16,
     "kind": "from",
     "src": "_pytest.config",
     "src_name": "console_main",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/pytest/__init__.py",
     "name": "ExitCode",
     "line": 17,
     "kind": "from",
     "src": "_pytest.config",
     "src_name": "ExitCode",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/pytest/__init__.py",
     "name": "hookimpl",
     "line": 18,
     "kind": "from",
     "src": "_pytest.config",
     "src_name": "hookimpl",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/pytest/__init__.py",
     "name": "hookspec",
     "line": 19,
     "kind": "from",
     "src": "_pytest.config",
     "src_name": "hookspec",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/pytest/__init__.py",
     "name": "main",
     "line": 20,
     "kind": "from",
     "src": "_pytest.config",
     "src_name": "main",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/pytest/__init__.py",
     "name": "PytestPluginManager",
     "line": 21,
     "kind": "from",
     "src": "_pytest.config",
     "src_name": "PytestPluginManager",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/pytest/__init__.py",
     "name": "UsageError",
     "line": 22,
     "kind": "from",
     "src
```
</details>

## Step 2

The outline of `src/pytest/__init__.py` has 40 bindings (capped, so this is only the start of the file); a literal `__all__` at line 100; no dynamic namespace tricks.

Chain: `src/pytest/__init__.py` is not yet closed for `__pytestPDB`.

Still to settle: close the namespace of `src/pytest/__init__.py` for `__pytestPDB`.

Next: outline `src/pytest/__init__.py` filtered to `__pytestPDB`, because module `src/pytest/__init__.py` (task), name `__pytestPDB` (task). I expect: a re-export continues the chain to its source (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a definition there ends the chain (under 5%); no binding but a star import means checking what that source exports (under 5%). Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: check for a submodule of that name.

**Call:** `symbols('src/pytest/__init__.py', '__pytestPDB')`

**Response**: outcome `reexport`

```
module src/pytest/__init__.py lines=191 dynamic=no all=static@100
25 from __pytestPDB <- _pytest.debugging pytestPDB
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/pytest/__init__.py",
    "__pytestPDB"
   ],
   "desc": "close the namespace of `src/pytest/__init__.py` for `__pytestPDB`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/pytest/__init__.py', '__pytestPDB')",
   "key": "[\"symbols\", [\"src/pytest/__init__.py\", \"__pytestPDB\"]]",
   "v1": [
    1463357,
    490200
   ],
   "v2": [
    1463357,
    490200
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
     "src/pytest/__init__.py",
     "__pytestPDB"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/pytest/__init__.py', '__pytestPDB')",
  "key": "[\"symbols\", [\"src/pytest/__init__.py\", \"__pytestPDB\"]]",
  "provenance": "module `src/pytest/__init__.py` (task), name `__pytestPDB` (task)",
  "v2": [
   1463357,
   490200
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
  "none": "continue"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"src/pytest/__init__.py\", \"__pytestPDB\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 2,
   "path": "src/pytest/__init__.py",
   "filter": "__pytestPDB",
   "header": {
    "lines": 191,
    "dynamic": false,
    "all_status": "static",
    "all_line": 100
   },
   "bindings": [
    {
     "module": "src/pytest/__init__.py",
     "name": "__pytestPDB",
     "line": 25,
     "kind": "from",
     "src": "_pytest.debugging",
     "src_name": "pytestPDB",
     "conditional": false,
     "col": 0
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "chain": [
   [
    "src/pytest/__init__.py",
    "__pytestPDB",
    "reexport",
    [
     "_pytest.debugging",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 3

In `src/pytest/__init__.py`, `__pytestPDB` has exactly one binding: line 25 imports it as `pytestPDB` from `_pytest.debugging`. No dynamic namespace tricks, a literal `__all__` at line 100.

Chain: `src/pytest/__init__.py` takes `__pytestPDB` from `_pytest.debugging` (module not yet located).

Outstanding: locate the module `_pytest.debugging` imported by `src/pytest/__init__.py`.

Next: grep `^\s*(?:async\s+)?(?:def|class)\s+pytestPDB\b` under `.`, because a `def`/`class pytestPDB` statement would reveal the module file; `pytestPDB` task. I expect: hits under the cap (about 95%); a capped result (about 5%); no hits (about 5%). The alternative, list `.`, is more likely to hit the cap (about 20% against about 5%). Plan by outcome: zero: list `.`; mid: outline each module that appears; cap: list `.`.

**Call:** `grep('^\\s*(?:async\\s+)?(?:def|class)\\s+pytestPDB\\b', '.')`

**Response**: outcome `mid`

```
src/_pytest/debugging.py:92:class pytestPDB:
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/pytest/__init__.py",
    "_pytest.debugging"
   ],
   "desc": "locate the module `_pytest.debugging` imported by `src/pytest/__init__.py`"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+pytestPDB\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+pytestPDB\\\\b\", \".\"]]",
   "v1": [
    17809,
    8436
   ],
   "v2": [
    53731,
    25308
   ],
   "p_cap": [
    1,
    37
   ],
   "forecast": {
    "zero": [
     1,
     37
    ],
    "mid": [
     35,
     37
    ],
    "cap": [
     1,
     37
    ]
   },
   "serves": [
    [
     "module_path",
     "src/pytest/__init__.py",
     "_pytest.debugging"
    ]
   ]
  },
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    1559,
    684
   ],
   "v2": [
    6443,
    2812
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
     "src/pytest/__init__.py",
     "_pytest.debugging"
    ]
   ]
  },
  {
   "call": "symbols('_pytest/debugging.py', 'pytestPDB')",
   "key": "[\"symbols\", [\"_pytest/debugging.py\", \"pytestPDB\"]]",
   "v1": [
    2940841487,
    1245174766
   ],
   "v2": [
    331307345249,
    138214399026
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     20494214,
     62556627
    ],
    "reexport": [
     185468,
     20852209
    ],
    "star": [
     46367,
     62556627
    ],
    "none": [
     92734,
     8936661
    ],
    "missing": [
     87016,
     133383
    ]
   },
   "serves": [
    [
     "module_path",
     "src/pytest/__init__.py",
     "_pytest.debugging"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+pytestPDB\\\\b', 'src')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+pytestPDB\\\\b\", \"src\"]]",
   "v1": [
    21769,
    7410
   ],
   "v2": [
    31481,
    10545
   ],
   "p_cap": [
    1,
    130
   ],
   "forecast": {
    "zero": [
     227,
     260
    ],
    "mid": [
     31,
     260
    ],
    "cap": [
     1,
     130
    ]
   },
   "serves": [
    [
     "module_path",
     "src/pytest/__init__.py",
     "_pytest.debugging"
    ]
   ]
  },
  {
   "call": "symbols('_pytest/debugging/__init__.py', 'pytestPDB')",
   "key": "[\"symbols\", [\"_pytest/debugging/__init__.py\", \"pytestPDB\"]]",
   "v1": [
    49437577923,
    16273437376
   ],
   "v2": [
    5581351402957,
    1806351548736
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     52735,
     14938896
    ],
    "reexport": [
     179299,
     7469448
    ],
    "star": [
     10547,
     14938896
    ],
    "none": [
     10547,
     933681
    ],
    "missing": [
     256219,
     266766
    ]
   },
   "serves": [
    [
     "module_path",
     "src/pytest/__init__.py",
     "_pytest.debugging"
    ]
   ]
  }
 ],
 "choice": {
  "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+pytestPDB\\\\b', '.')",
  "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+pytestPDB\\\\b\", \".\"]]",
  "provenance": "a `def`/`class pytestPDB` statement would reveal the module file; `pytestPDB` task",
  "v2": [
   53731,
   25308
  ]
 },
 "forecast": {
  "zero": [
   1,
   37
  ],
  "mid": [
   35,
   37
  ],
  "cap": [
   1,
   37
  ]
 },
 "plan": {
  "zero": "[\"ls\", [\".\"]]",
  "mid": "continue",
  "cap": "[\"ls\", [\".\"]]"
 },
 "adherence": {
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "grep",
   "step": 3,
   "pattern": "^\\s*(?:async\\s+)?(?:def|class)\\s+pytestPDB\\b",
   "scope": ".",
   "hits": [
    [
     "src/_pytest/debugging.py",
     92
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "chain": [
   [
    "src/pytest/__init__.py",
    "__pytestPDB",
    "reexport",
    [
     "_pytest.debugging",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 4

The grep under `.` returned 1 lines, under the cap, so these are all of them: `src/_pytest/debugging.py`.

Chain: `src/pytest/__init__.py` takes `__pytestPDB` from `_pytest.debugging` (module not yet located).

Outstanding: locate the module `_pytest.debugging` imported by `src/pytest/__init__.py`.

Next: list `.`, because `_pytest.debugging` imported by `src/pytest/__init__.py` should live under `.`. I expect: a complete listing settles which files exist (about 80%); a capped listing settles nothing (about 20%). The alternative, outline `_pytest/debugging.py` filtered to `pytestPDB`, costs more in expectation. Plan by outcome: complete: outline the module it reveals; cap: outline `_pytest/debugging.py` filtered to `pytestPDB`.

**Call:** `ls('.')`

**Response**: outcome `complete`

```
.github/
.pre-commit-config.yaml
.readthedocs.yaml
CHANGELOG.rst
CODE_OF_CONDUCT.md
CONTRIBUTING.rst
OPENCOLLECTIVE.rst
README.rst
RELEASING.rst
SECURITY.md
TIDELIFT.rst
bench/
changelog/
codecov.yml
doc/
extra/
pyproject.toml
scripts/
src/
testing/
tox.ini
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/pytest/__init__.py",
    "_pytest.debugging"
   ],
   "desc": "locate the module `_pytest.debugging` imported by `src/pytest/__init__.py`"
  }
 ],
 "candidates": [
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    1559,
    684
   ],
   "v2": [
    157808741267,
    67239437364
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
     "src/pytest/__init__.py",
     "_pytest.debugging"
    ]
   ]
  },
  {
   "call": "symbols('_pytest/debugging.py', 'pytestPDB')",
   "key": "[\"symbols\", [\"_pytest/debugging.py\", \"pytestPDB\"]]",
   "v1": [
    2940841487,
    1245174766
   ],
   "v2": [
    84276660341,
    33619718682
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     20494214,
     62556627
    ],
    "reexport": [
     185468,
     20852209
    ],
    "star": [
     46367,
     62556627
    ],
    "none": [
     92734,
     8936661
    ],
    "missing": [
     87016,
     133383
    ]
   },
   "serves": [
    [
     "module_path",
     "src/pytest/__init__.py",
     "_pytest.debugging"
    ]
   ]
  },
  {
   "call": "symbols('_pytest/debugging/__init__.py', 'pytestPDB')",
   "key": "[\"symbols\", [\"_pytest/debugging/__init__.py\", \"pytestPDB\"]]",
   "v1": [
    49437577923,
    16273437376
   ],
   "v2": [
    1428594857425,
    439382809152
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     52735,
     14938896
    ],
    "reexport": [
     179299,
     7469448
    ],
    "star": [
     10547,
     14938896
    ],
    "none": [
     10547,
     933681
    ],
    "missing": [
     256219,
     266766
    ]
   },
   "serves": [
    [
     "module_path",
     "src/pytest/__init__.py",
     "_pytest.debugging"
    ]
   ]
  }
 ],
 "choice": {
  "call": "ls('.')",
  "key": "[\"ls\", [\".\"]]",
  "provenance": "`_pytest.debugging` imported by `src/pytest/__init__.py` should live under `.`",
  "v2": [
   157808741267,
   67239437364
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
  "cap": "[\"symbols\", [\"_pytest/debugging.py\", \"pytestPDB\"]]"
 },
 "adherence": {
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "listing",
   "step": 4,
   "dir": ".",
   "entries": [
    ".github/",
    ".pre-commit-config.yaml",
    ".readthedocs.yaml",
    "CHANGELOG.rst",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.rst",
    "OPENCOLLECTIVE.rst",
    "README.rst",
    "RELEASING.rst",
    "SECURITY.md",
    "TIDELIFT.rst",
    "bench/",
    "changelog/",
    "codecov.yml",
    "doc/",
    "extra/",
    "pyproject.toml",
    "scripts/",
    "src/",
    "testing/",
    "tox.ini"
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "chain": [
   [
    "src/pytest/__init__.py",
    "__pytestPDB",
    "reexport",
    [
     "_pytest.debugging",
     "src/_pytest/debugging.py"
    ]
   ],
   [
    "src/_pytest/debugging.py",
    "pytestPDB",
    "open",
    null
   ]
  ]
 }
}
```
</details>

## Step 5

`.` lists 21 entries (complete): `.github/`, `bench/`, `changelog/`, `doc/`, `extra/`, `scripts/` and 2 more.

Chain: `src/pytest/__init__.py` takes `__pytestPDB` from `_pytest.debugging` (`src/_pytest/debugging.py`); `src/_pytest/debugging.py` is not yet closed for `pytestPDB`.

Still to settle: close the namespace of `src/_pytest/debugging.py` for `pytestPDB`.

Next: outline `src/_pytest/debugging.py` filtered to `pytestPDB`, because module `src/_pytest/debugging.py` (step 3), name `pytestPDB` (task). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `src/_pytest/debugging.py`, is more likely to hit the cap (about 10% against under 5%). Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done.

**Call:** `symbols('src/_pytest/debugging.py', 'pytestPDB')`

**Response**: outcome `def`

```
module src/_pytest/debugging.py lines=405 dynamic=no all=none
92 class pytestPDB
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/_pytest/debugging.py",
    "pytestPDB"
   ],
   "desc": "close the namespace of `src/_pytest/debugging.py` for `pytestPDB`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/debugging.py', 'pytestPDB')",
   "key": "[\"symbols\", [\"src/_pytest/debugging.py\", \"pytestPDB\"]]",
   "v1": [
    4439,
    4180
   ],
   "v2": [
    4439,
    4180
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
     "src/_pytest/debugging.py",
     "pytestPDB"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/debugging.py')",
   "key": "[\"symbols\", [\"src/_pytest/debugging.py\"]]",
   "v1": [
    164952383,
    140310060
   ],
   "v2": [
    825173161,
    701550300
   ],
   "p_cap": [
    99,
    835
   ],
   "forecast": {
    "def": [
     325312,
     391615
    ],
    "reexport": [
     8832,
     391615
    ],
    "star": [
     736,
     391615
    ],
    "none": [
     1472,
     55945
    ],
    "cap": [
     99,
     835
    ]
   },
   "serves": [
    [
     "bindings",
     "src/_pytest/debugging.py",
     "pytestPDB"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/_pytest/debugging.py', 'pytestPDB')",
  "key": "[\"symbols\", [\"src/_pytest/debugging.py\", \"pytestPDB\"]]",
  "provenance": "module `src/_pytest/debugging.py` (step 3), name `pytestPDB` (task)",
  "v2": [
   4439,
   4180
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
 "adherence": {
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 5,
   "path": "src/_pytest/debugging.py",
   "filter": "pytestPDB",
   "header": {
    "lines": 405,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/_pytest/debugging.py",
     "name": "pytestPDB",
     "line": 92,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "chain": [
   [
    "src/pytest/__init__.py",
    "__pytestPDB",
    "reexport",
    [
     "_pytest.debugging",
     "src/_pytest/debugging.py"
    ]
   ],
   [
    "src/_pytest/debugging.py",
    "pytestPDB",
    "class",
    92
   ]
  ]
 }
}
```
</details>

## Final

Certificate complete. The name resolves to `src/_pytest/debugging.py:92`. In hindsight, 1 of 5 calls were not needed for the certificate: steps 1.

**Answer:** `{"target": {"kind": "def", "path": "src/_pytest/debugging.py", "line": 92, "name": "pytestPDB", "detail": "class"}, "text": "src/_pytest/debugging.py:92"}`  
**Stopped:** certificate after 5 calls