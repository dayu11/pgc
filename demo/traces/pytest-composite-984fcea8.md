# pytest-composite-984fcea8

**Repository:** pytest  
**Family:** composite  
**Seed:** 0, prior 0140c5bd99319f8c

## Task

In `src/_pytest/debugging.py`, line 24 imports `UsageError` from `_pytest.config.exceptions`. Under the declared semantics, which definition does the module-level name `UsageError` bound by this statement resolve to? Answer with `path:line`. Then list every module-level import statement in the snapshot that imports that definition (from-imports naming it, directly or with `as`, and star imports of modules that export it), as `path:line` entries.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

Nothing seen yet beyond the task text.

Chain: `src/_pytest/debugging.py` is not yet closed for `UsageError`.

Outstanding: close the namespace of `src/_pytest/debugging.py` for `UsageError`.

Next: outline `src/_pytest/debugging.py`, because module `src/_pytest/debugging.py` (task). I expect: a definition there ends the chain (about 85%); a capped outline means filtering by name (about 10%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `src/_pytest/debugging.py` filtered to `UsageError`, is expected to open more follow-up work. Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done; cap: outline `src/_pytest/debugging.py` filtered to `UsageError`.

**Call:** `symbols('src/_pytest/debugging.py')`

**Response**: outcome `def`

```
module src/_pytest/debugging.py lines=405 dynamic=no all=none
5 from annotations <- __future__ annotations
7 import argparse <- argparse
8 from Callable <- collections.abc Callable
9 from Generator <- collections.abc Generator
10 import functools <- functools
11 import importlib <- importlib
12 import sys <- sys
13 import types <- types
14 from Any <- typing Any
16 from outcomes <- _pytest outcomes
17 from ExceptionInfo <- _pytest._code ExceptionInfo
18 from CaptureManager <- _pytest.capture CaptureManager
19 from Config <- _pytest.config Config
20 from ConftestImportFailure <- _pytest.config ConftestImportFailure
21 from hookimpl <- _pytest.config hookimpl
22 from PytestPluginManager <- _pytest.config PytestPluginManager
23 from Parser <- _pytest.config.argparsing Parser
24 from UsageError <- _pytest.config.exceptions UsageError
25 from Node <- _pytest.nodes Node
26 from BaseReport <- _pytest.reports BaseReport
27 from CallInfo <- _pytest.runner CallInfo
30 def _validate_usepdb_cls
41 def pytest_addoption
65 def pytest_configure
... (8 more lines)
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
    "UsageError"
   ],
   "desc": "close the namespace of `src/_pytest/debugging.py` for `UsageError`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/debugging.py')",
   "key": "[\"symbols\", [\"src/_pytest/debugging.py\"]]",
   "v1": [
    164952383,
    140310060
   ],
   "v2": [
    19617451097,
    14031006000
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
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/debugging.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/debugging.py\", \"UsageError\"]]",
   "v1": [
    735809,
    250800
   ],
   "v2": [
    735809,
    250800
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
     "src/_pytest/debugging.py",
     "UsageError"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/_pytest/debugging.py')",
  "key": "[\"symbols\", [\"src/_pytest/debugging.py\"]]",
  "provenance": "module `src/_pytest/debugging.py` (task)",
  "v2": [
   19617451097,
   14031006000
  ]
 },
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
 "plan": {
  "def": "done",
  "reexport": "continue",
  "star": "continue",
  "none": "done",
  "cap": "[\"symbols\", [\"src/_pytest/debugging.py\", \"UsageError\"]]"
 },
 "adherence": null,
 "facts": [
  {
   "kind": "outline",
   "step": 1,
   "path": "src/_pytest/debugging.py",
   "filter": null,
   "header": {
    "lines": 405,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/_pytest/debugging.py",
     "name": "annotations",
     "line": 5,
     "kind": "from",
     "src": "__future__",
     "src_name": "annotations",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/debugging.py",
     "name": "argparse",
     "line": 7,
     "kind": "import",
     "src": "argparse",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/debugging.py",
     "name": "Callable",
     "line": 8,
     "kind": "from",
     "src": "collections.abc",
     "src_name": "Callable",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/debugging.py",
     "name": "Generator",
     "line": 9,
     "kind": "from",
     "src": "collections.abc",
     "src_name": "Generator",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/debugging.py",
     "name": "functools",
     "line": 10,
     "kind": "import",
     "src": "functools",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/debugging.py",
     "name": "importlib",
     "line": 11,
     "kind": "import",
     "src": "importlib",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/debugging.py",
     "name": "sys",
     "line": 12,
     "kind": "import",
     "src": "sys",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/debugging.py",
     "name": "types",
     "line": 13,
     "kind": "import",
     "src": "types",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/debugging.py",
     "name": "Any",
     "line": 14,
     "kind": "from",
     "src": "typing",
     "src_name": "Any",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/debugging.py",
     "name": "outcomes",
     "line": 16,
     "kind": "from",
     "src": "_pytest",
     "src_name": "outcomes",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/debugging.py",
     "name": "ExceptionInfo",
     "line": 17,
     "kind": "from",
     "src": "_pytest._code",
     "src_name": "ExceptionInfo",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/debugging.py",
     "name": "CaptureManager",
     "line": 18,
     "kind": "from",
     "src": "_pytest.capture",
     "src_name": "CaptureManager",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/debugging.py",
     "name": "Config",
     "line": 19,
     "kind": "from",
     "src": "_pytest.config",
     "src_name": "Config",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/debugging.py",
     "name": "ConftestImportFailure",
     "line": 20,
     "kind": "from",
     "src": "_pytest.config",
     "src_name": "ConftestImportFailure",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/debugging.py",
     "name": "hookimpl",
     "line": 21,
     "kind": "from",
     "src": "_pytest.config",
     "src_name": "hookimpl",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/debugging.py",
     "name": "PytestPluginManager",
     "line": 22,
     "kind": "from",
     "src": "_pytest.config",
     "src_name": "PytestPluginManager",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/debugging.py",
     "name": "Parser",
     "line": 23,
     "kind": "from",
     "src": "_pytest.config.argparsing",
     "src_name": "Parser",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/debugging.py",
     "name": "UsageError",
    
```
</details>

## Step 2

The outline of `src/_pytest/debugging.py` has 32 bindings; no `__all__`; no dynamic namespace tricks. This is not the branch I planned for that outcome; the open items changed more than expected.

Chain: `src/_pytest/debugging.py` takes `UsageError` from `_pytest.config.exceptions` (module not yet located).

Still to settle: locate the module `_pytest.config.exceptions` imported by `src/_pytest/debugging.py`.

Next: grep `def`/`class UsageError` statements under `.`, because a `def`/`class UsageError` statement would reveal the module file; `UsageError` task. I expect: hits under the cap (about 95%); a capped result (about 5%); no hits (about 5%). The alternative, list `.`, is more likely to hit the cap (about 20% against about 5%). Plan by outcome: zero: list `.`; mid: outline each module that appears; cap: list `.`.

**Call:** `grep('^\\s*(?:async\\s+)?(?:def|class)\\s+UsageError\\b', '.')`

**Response**: outcome `mid`

```
src/_pytest/config/exceptions.py:7:class UsageError(Exception):
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/_pytest/debugging.py",
    "_pytest.config.exceptions"
   ],
   "desc": "locate the module `_pytest.config.exceptions` imported by `src/_pytest/debugging.py`"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+UsageError\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+UsageError\\\\b\", \".\"]]",
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
     "src/_pytest/debugging.py",
     "_pytest.config.exceptions"
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
     "src/_pytest/debugging.py",
     "_pytest.config.exceptions"
    ]
   ]
  },
  {
   "call": "symbols('_pytest/config/exceptions.py', 'UsageError')",
   "key": "[\"symbols\", [\"_pytest/config/exceptions.py\", \"UsageError\"]]",
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
     "src/_pytest/debugging.py",
     "_pytest.config.exceptions"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+UsageError\\\\b', 'src')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+UsageError\\\\b\", \"src\"]]",
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
     "src/_pytest/debugging.py",
     "_pytest.config.exceptions"
    ]
   ]
  },
  {
   "call": "symbols('_pytest/config/exceptions/__init__.py', 'UsageError')",
   "key": "[\"symbols\", [\"_pytest/config/exceptions/__init__.py\", \"UsageError\"]]",
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
     "src/_pytest/debugging.py",
     "_pytest.config.exceptions"
    ]
   ]
  }
 ],
 "choice": {
  "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+UsageError\\\\b', '.')",
  "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+UsageError\\\\b\", \".\"]]",
  "provenance": "a `def`/`class UsageError` statement would reveal the module file; `UsageError` task",
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
  "planned": "done",
  "status": "deviated"
 },
 "facts": [
  {
   "kind": "grep",
   "step": 2,
   "pattern": "^\\s*(?:async\\s+)?(?:def|class)\\s+UsageError\\b",
   "scope": ".",
   "hits": [
    [
     "src/_pytest/config/exceptions.py",
     7
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "chain": [
   [
    "src/_pytest/debugging.py",
    "UsageError",
    "reexport",
    [
     "_pytest.config.exceptions",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 3

The grep under `.` returned 1 lines, under the cap, so these are all of them: `src/_pytest/config/exceptions.py`.

Chain: `src/_pytest/debugging.py` takes `UsageError` from `_pytest.config.exceptions` (module not yet located).

Outstanding: locate the module `_pytest.config.exceptions` imported by `src/_pytest/debugging.py`.

Next: list `.`, because `_pytest.config.exceptions` imported by `src/_pytest/debugging.py` should live under `.`. I expect: a complete listing settles which files exist (about 80%); a capped listing settles nothing (about 20%). The alternative, outline `_pytest/config/exceptions.py` filtered to `UsageError`, costs more in expectation. Plan by outcome: complete: outline the module it reveals; cap: outline `_pytest/config/exceptions.py` filtered to `UsageError`.

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
    "src/_pytest/debugging.py",
    "_pytest.config.exceptions"
   ],
   "desc": "locate the module `_pytest.config.exceptions` imported by `src/_pytest/debugging.py`"
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
     "src/_pytest/debugging.py",
     "_pytest.config.exceptions"
    ]
   ]
  },
  {
   "call": "symbols('_pytest/config/exceptions.py', 'UsageError')",
   "key": "[\"symbols\", [\"_pytest/config/exceptions.py\", \"UsageError\"]]",
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
     "src/_pytest/debugging.py",
     "_pytest.config.exceptions"
    ]
   ]
  },
  {
   "call": "symbols('_pytest/config/exceptions/__init__.py', 'UsageError')",
   "key": "[\"symbols\", [\"_pytest/config/exceptions/__init__.py\", \"UsageError\"]]",
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
     "src/_pytest/debugging.py",
     "_pytest.config.exceptions"
    ]
   ]
  }
 ],
 "choice": {
  "call": "ls('.')",
  "key": "[\"ls\", [\".\"]]",
  "provenance": "`_pytest.config.exceptions` imported by `src/_pytest/debugging.py` should live under `.`",
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
  "cap": "[\"symbols\", [\"_pytest/config/exceptions.py\", \"UsageError\"]]"
 },
 "adherence": {
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "listing",
   "step": 3,
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
    "src/_pytest/debugging.py",
    "UsageError",
    "reexport",
    [
     "_pytest.config.exceptions",
     "src/_pytest/config/exceptions.py"
    ]
   ],
   [
    "src/_pytest/config/exceptions.py",
    "UsageError",
    "open",
    null
   ]
  ]
 }
}
```
</details>

## Step 4

`.` lists 21 entries (complete): `.github/`, `bench/`, `changelog/`, `doc/`, `extra/`, `scripts/` and 2 more.

Chain: `src/_pytest/debugging.py` takes `UsageError` from `_pytest.config.exceptions` (`src/_pytest/config/exceptions.py`); `src/_pytest/config/exceptions.py` is not yet closed for `UsageError`.

Outstanding: close the namespace of `src/_pytest/config/exceptions.py` for `UsageError`.

Next: outline `src/_pytest/config/exceptions.py` filtered to `UsageError`, because module `src/_pytest/config/exceptions.py` (step 2), name `UsageError` (task). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `src/_pytest/config/exceptions.py`, is more likely to hit the cap (about 10% against under 5%). Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done.

**Call:** `symbols('src/_pytest/config/exceptions.py', 'UsageError')`

**Response**: outcome `def`

```
module src/_pytest/config/exceptions.py lines=16 dynamic=no all=none
7 class UsageError
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/_pytest/config/exceptions.py",
    "UsageError"
   ],
   "desc": "close the namespace of `src/_pytest/config/exceptions.py` for `UsageError`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/config/exceptions.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/config/exceptions.py\", \"UsageError\"]]",
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
     "src/_pytest/config/exceptions.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/config/exceptions.py')",
   "key": "[\"symbols\", [\"src/_pytest/config/exceptions.py\"]]",
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
     "src/_pytest/config/exceptions.py",
     "UsageError"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/_pytest/config/exceptions.py', 'UsageError')",
  "key": "[\"symbols\", [\"src/_pytest/config/exceptions.py\", \"UsageError\"]]",
  "provenance": "module `src/_pytest/config/exceptions.py` (step 2), name `UsageError` (task)",
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
   "step": 4,
   "path": "src/_pytest/config/exceptions.py",
   "filter": "UsageError",
   "header": {
    "lines": 16,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/_pytest/config/exceptions.py",
     "name": "UsageError",
     "line": 7,
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
    "src/_pytest/debugging.py",
    "UsageError",
    "reexport",
    [
     "_pytest.config.exceptions",
     "src/_pytest/config/exceptions.py"
    ]
   ],
   [
    "src/_pytest/config/exceptions.py",
    "UsageError",
    "class",
    7
   ]
  ]
 }
}
```
</details>

## Step 5

In `src/_pytest/config/exceptions.py`, `UsageError` has exactly one binding: a class at line 7. No dynamic namespace tricks, no `__all__`. This is not the branch I planned for that outcome; the open items changed more than expected.

Candidate modules so far: 0; statements confirmed: 0, ruled out: 0, modules with no such import: 0, pending: 0. import coverage open at `.`; star coverage open at `.`.

Still to settle: cover `.` for import lines; cover `.` for star lines.

Next: grep from-imports naming `UsageError` or star imports under `.`, because import and star lines under `.` in one call. I expect: hits under the cap (about 60%); no hits (about 35%); a capped result (about 10%). The alternative, grep from-imports naming `UsageError` under `.`, serves fewer of the open items. Plan by outcome: zero: done; mid: outline each module that appears; cap: list the scope and split it.

**Call:** `grep('^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bUsageError\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*UsageError\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$', '.')`

**Response** (capped): outcome `cap`

```
src/_pytest/_io/terminalwriter.py:217:        from _pytest.config.exceptions import UsageError
src/_pytest/config/__init__.py:51:from .exceptions import UsageError as UsageError
src/_pytest/config/argparsing.py:22:from .exceptions import UsageError
src/_pytest/config/findpaths.py:16:from .exceptions import UsageError
src/_pytest/debugging.py:24:from _pytest.config.exceptions import UsageError
src/_pytest/logging.py:35:from _pytest.config import UsageError
src/_pytest/main.py:34:from _pytest.config import UsageError
src/_pytest/mark/__init__.py:27:from _pytest.config import UsageError
src/_pytest/python.py:56:from _pytest.config import UsageError
src/pytest/__init__.py:22:from _pytest.config import UsageError
testing/acceptance_test.py:599:            from pytest import *
testing/python/collect.py:11:from _pytest.config.exceptions import UsageError
testing/test_config.py:28:from _pytest.config.exceptions import UsageError
testing/test_config.py:1354:            UsageError,
testing/test_findpaths.py:8:from _pytest.config import UsageError
testing/test_main.py:10:from _pytest.config import UsageError
testing/test_main.py:271:            UsageError,
testing/test_mark.py:13:from _pytest.config import UsageError
testing/test_parseopt.py:13:from _pytest.config.exceptions import UsageError
testing/test_pluginmanager.py:16:from _pytest.config.exceptions import UsageError
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
   "desc": "cover `.` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "."
   ],
   "desc": "cover `.` for star lines"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bUsageError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bUsageError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
   "v1": [
    158305706749,
    30174993849
   ],
   "v2": [
    158305706749,
    30174993849
   ],
   "p_cap": [
    1,
    13
   ],
   "forecast": {
    "zero": [
     1,
     3
    ],
    "mid": [
     23,
     39
    ],
    "cap": [
     1,
     13
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
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bUsageError\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bUsageError\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
   "v1": [
    1282037986608,
    216088325915
   ],
   "v2": [
    1282037986608,
    216088325915
   ],
   "p_cap": [
    1,
    33
   ],
   "forecast": {
    "zero": [
     26,
     33
    ],
    "mid": [
     2,
     11
    ],
    "cap": [
     1,
     33
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
    1282037986608,
    216088325915
   ],
   "v2": [
    1282037986608,
    216088325915
   ],
   "p_cap": [
    1,
    23
   ],
   "forecast": {
    "zero": [
     13,
     23
    ],
    "mid": [
     9,
     23
    ],
    "cap": [
     1,
     23
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
  "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bUsageError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
  "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bUsageError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
  "provenance": "import and star lines under `.` in one call",
  "v2": [
   158305706749,
   30174993849
  ]
 },
 "forecast": {
  "zero": [
   1,
   3
  ],
  "mid": [
   23,
   39
  ],
  "cap": [
   1,
   13
  ]
 },
 "plan": {
  "zero": "done",
  "mid": "continue",
  "cap": "continue"
 },
 "adherence": {
  "planned": "done",
  "status": "deviated"
 },
 "facts": [
  {
   "kind": "grep",
   "step": 5,
   "pattern": "^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bUsageError\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*UsageError\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$",
   "scope": ".",
   "hits": [
    [
     "src/_pytest/_io/terminalwriter.py",
     217
    ],
    [
     "src/_pytest/config/__init__.py",
     51
    ],
    [
     "src/_pytest/config/argparsing.py",
     22
    ],
    [
     "src/_pytest/config/findpaths.py",
     16
    ],
    [
     "src/_pytest/debugging.py",
     24
    ],
    [
     "src/_pytest/logging.py",
     35
    ],
    [
     "src/_pytest/main.py",
     34
    ],
    [
     "src/_pytest/mark/__init__.py",
     27
    ],
    [
     "src/_pytest/python.py",
     56
    ],
    [
     "src/pytest/__init__.py",
     22
    ],
    [
     "testing/acceptance_test.py",
     599
    ],
    [
     "testing/python/collect.py",
     11
    ],
    [
     "testing/test_config.py",
     28
    ],
    [
     "testing/test_config.py",
     1354
    ],
    [
     "testing/test_findpaths.py",
     8
    ],
    [
     "testing/test_main.py",
     10
    ],
    [
     "testing/test_main.py",
     271
    ],
    [
     "testing/test_mark.py",
     13
    ],
    [
     "testing/test_parseopt.py",
     13
    ],
    [
     "testing/test_pluginmanager.py",
     16
    ]
   ],
   "capped": true
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "src/_pytest/_io/terminalwriter.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "src/_pytest/config/__init__.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "src/_pytest/config/argparsing.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "src/_pytest/config/findpaths.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "src/_pytest/debugging.py",
    24,
    "in",
    "`_pytest.config.exceptions` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/logging.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "src/_pytest/main.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "src/_pytest/mark/__init__.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "src/_pytest/python.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "src/pytest/__init__.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "testing/acceptance_test.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "testing/python/collect.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "testing/test_config.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "testing/test_findpaths.py",
    0,
    "pending",
    "outline
```
</details>

## Step 6

The grep under `.` hit the cap at 20 lines, so it proves nothing about what else is there.

Candidate modules so far: 18; statements confirmed: 1, ruled out: 0, modules with no such import: 0, pending: 17. import coverage open at `.github`, `bench`, `changelog`, `doc` and 4 more; star coverage open at `.github`, `bench`, `changelog`, `doc` and 4 more.

Open: cover `.github` for import lines; cover `bench` for import lines; cover `changelog` for import lines; cover `doc` for import lines; and 29 more.

Next: grep from-imports naming `UsageError` or star imports under `.github`, because import and star lines under `.github` in one call. I expect: no hits (about 85%); hits under the cap (about 10%); a capped result (under 5%). The alternative, grep from-imports naming `UsageError` or star imports under `bench`, scores the same; the seed broke the tie. Plan by outcome: zero: grep from-imports naming `UsageError` or star imports under `bench`; mid: grep from-imports naming `UsageError` or star imports under `bench`; cap: grep from-imports naming `UsageError` or star imports under `bench`.

**Call:** `grep('^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bUsageError\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*UsageError\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$', '.github')`

**Response**: outcome `zero`

```

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
    ".github"
   ],
   "desc": "cover `.github` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "IMPORT",
    "bench"
   ],
   "desc": "cover `bench` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "IMPORT",
    "changelog"
   ],
   "desc": "cover `changelog` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "IMPORT",
    "doc"
   ],
   "desc": "cover `doc` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "IMPORT",
    "extra"
   ],
   "desc": "cover `extra` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "IMPORT",
    "scripts"
   ],
   "desc": "cover `scripts` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "IMPORT",
    "src"
   ],
   "desc": "cover `src` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "IMPORT",
    "testing"
   ],
   "desc": "cover `testing` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    ".github"
   ],
   "desc": "cover `.github` for star lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "bench"
   ],
   "desc": "cover `bench` for star lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "changelog"
   ],
   "desc": "cover `changelog` for star lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "doc"
   ],
   "desc": "cover `doc` for star lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "extra"
   ],
   "desc": "cover `extra` for star lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "scripts"
   ],
   "desc": "cover `scripts` for star lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "src"
   ],
   "desc": "cover `src` for star lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "testing"
   ],
   "desc": "cover `testing` for star lines"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/_io/terminalwriter.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/_io/terminalwriter.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/argparsing.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/argparsing.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/findpaths.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/logging.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/logging.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/main.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/mark/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/mark/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/python.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/pytest/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/pytest/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "UsageError"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/python/collect.py",
    "UsageError"
   ],
   "desc": "outline `testing/python/collect.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_config.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_config.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_findpaths.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_main.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_mark.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_mark.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_parseopt.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_parseopt.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_pluginmanager.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_pluginmanager.py` for its `UsageError` imports"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bUsageError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.github')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bUsageError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".github\"]]",
   "v1": [
    52680080286193030961,
    1031915837513991360
   ],
   "v2": [
    3670325876605748851,
    73708274108142240
   ],
   "p_cap": [

```
</details>

## Step 7

The grep under `.github` returned nothing, and it was not capped, so there are no such lines there.

Candidate modules so far: 18; statements confirmed: 1, ruled out: 0, modules with no such import: 0, pending: 17. import coverage open at `bench`, `changelog`, `doc`, `extra` and 3 more; star coverage open at `bench`, `changelog`, `doc`, `extra` and 3 more.

Open: cover `bench` for import lines; cover `changelog` for import lines; cover `doc` for import lines; cover `extra` for import lines; and 27 more.

Next: grep from-imports naming `UsageError` or star imports under `bench`, because import and star lines under `bench` in one call. I expect: no hits (about 85%); hits under the cap (about 10%); a capped result (under 5%). The alternative, grep from-imports naming `UsageError` or star imports under `changelog`, scores the same; the seed broke the tie. Plan by outcome: zero: grep from-imports naming `UsageError` or star imports under `changelog`; mid: grep from-imports naming `UsageError` or star imports under `changelog`; cap: grep from-imports naming `UsageError` or star imports under `changelog`.

**Call:** `grep('^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bUsageError\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*UsageError\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$', 'bench')`

**Response**: outcome `zero`

```

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
    "bench"
   ],
   "desc": "cover `bench` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "IMPORT",
    "changelog"
   ],
   "desc": "cover `changelog` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "IMPORT",
    "doc"
   ],
   "desc": "cover `doc` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "IMPORT",
    "extra"
   ],
   "desc": "cover `extra` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "IMPORT",
    "scripts"
   ],
   "desc": "cover `scripts` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "IMPORT",
    "src"
   ],
   "desc": "cover `src` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "IMPORT",
    "testing"
   ],
   "desc": "cover `testing` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "bench"
   ],
   "desc": "cover `bench` for star lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "changelog"
   ],
   "desc": "cover `changelog` for star lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "doc"
   ],
   "desc": "cover `doc` for star lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "extra"
   ],
   "desc": "cover `extra` for star lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "scripts"
   ],
   "desc": "cover `scripts` for star lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "src"
   ],
   "desc": "cover `src` for star lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "testing"
   ],
   "desc": "cover `testing` for star lines"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/_io/terminalwriter.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/_io/terminalwriter.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/argparsing.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/argparsing.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/findpaths.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/logging.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/logging.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/main.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/mark/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/mark/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/python.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/pytest/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/pytest/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "UsageError"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/python/collect.py",
    "UsageError"
   ],
   "desc": "outline `testing/python/collect.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_config.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_config.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_findpaths.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_main.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_mark.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_mark.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_parseopt.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_parseopt.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_pluginmanager.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_pluginmanager.py` for its `UsageError` imports"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bUsageError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', 'bench')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bUsageError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \"bench\"]]",
   "v1": [
    4971442736137818317,
    103191583751399136
   ],
   "v2": [
    48418909347665636123,
    1031915837513991360
   ],
   "p_cap": [
    2,
    239
   ],
   "forecast": {
    "zero": [
     208,
     239
    ],
    "mid": [
     29,
     239
    ],
    "cap": [
     2,
     239
    ]
   },
   "serves": [
    [
     "cover",
     "IMPORT",
     "bench"
    ],
    [
     "cover",
     "STAR",
     "
```
</details>

## Step 8

The grep under `bench` returned nothing, and it was not capped, so there are no such lines there.

Candidate modules so far: 18; statements confirmed: 1, ruled out: 0, modules with no such import: 0, pending: 17. import coverage open at `changelog`, `doc`, `extra`, `scripts` and 2 more; star coverage open at `changelog`, `doc`, `extra`, `scripts` and 2 more.

Outstanding: cover `changelog` for import lines; cover `doc` for import lines; cover `extra` for import lines; cover `scripts` for import lines; and 25 more.

Next: grep from-imports naming `UsageError` or star imports under `changelog`, because import and star lines under `changelog` in one call. I expect: no hits (about 85%); hits under the cap (about 10%); a capped result (under 5%). The alternative, grep from-imports naming `UsageError` or star imports under `doc`, scores the same; the seed broke the tie. Plan by outcome: zero: grep from-imports naming `UsageError` or star imports under `doc`; mid: grep from-imports naming `UsageError` or star imports under `doc`; cap: grep from-imports naming `UsageError` or star imports under `doc`.

**Call:** `grep('^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bUsageError\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*UsageError\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$', 'changelog')`

**Response**: outcome `zero`

```

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
    "changelog"
   ],
   "desc": "cover `changelog` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "IMPORT",
    "doc"
   ],
   "desc": "cover `doc` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "IMPORT",
    "extra"
   ],
   "desc": "cover `extra` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "IMPORT",
    "scripts"
   ],
   "desc": "cover `scripts` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "IMPORT",
    "src"
   ],
   "desc": "cover `src` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "IMPORT",
    "testing"
   ],
   "desc": "cover `testing` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "changelog"
   ],
   "desc": "cover `changelog` for star lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "doc"
   ],
   "desc": "cover `doc` for star lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "extra"
   ],
   "desc": "cover `extra` for star lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "scripts"
   ],
   "desc": "cover `scripts` for star lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "src"
   ],
   "desc": "cover `src` for star lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "testing"
   ],
   "desc": "cover `testing` for star lines"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/_io/terminalwriter.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/_io/terminalwriter.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/argparsing.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/argparsing.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/findpaths.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/logging.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/logging.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/main.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/mark/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/mark/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/python.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/pytest/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/pytest/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "UsageError"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/python/collect.py",
    "UsageError"
   ],
   "desc": "outline `testing/python/collect.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_config.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_config.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_findpaths.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_main.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_mark.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_mark.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_parseopt.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_parseopt.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_pluginmanager.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_pluginmanager.py` for its `UsageError` imports"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bUsageError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', 'changelog')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bUsageError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \"changelog\"]]",
   "v1": [
    46748774436563335379,
    1031915837513991360
   ],
   "v2": [
    11363314105712697083,
    257978959378497840
   ],
   "p_cap": [
    2,
    239
   ],
   "forecast": {
    "zero": [
     208,
     239
    ],
    "mid": [
     29,
     239
    ],
    "cap": [
     2,
     239
    ]
   },
   "serves": [
    [
     "cover",
     "IMPORT",
     "changelog"
    ],
    [
     "cover",
     "STAR",
     "changelog"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bUsageError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\
```
</details>

## Step 9

The grep under `changelog` returned nothing, and it was not capped, so there are no such lines there.

Candidate modules so far: 18; statements confirmed: 1, ruled out: 0, modules with no such import: 0, pending: 17. import coverage open at `doc`, `extra`, `scripts`, `src` and 1 more; star coverage open at `doc`, `extra`, `scripts`, `src` and 1 more.

Still to settle: cover `doc` for import lines; cover `extra` for import lines; cover `scripts` for import lines; cover `src` for import lines; and 23 more.

Next: grep from-imports naming `UsageError` or star imports under `doc`, because import and star lines under `doc` in one call. I expect: no hits (about 85%); hits under the cap (about 10%); a capped result (under 5%). The alternative, grep from-imports naming `UsageError` or star imports under `extra`, scores the same; the seed broke the tie. Plan by outcome: zero: grep from-imports naming `UsageError` or star imports under `extra`; mid: grep from-imports naming `UsageError` or star imports under `extra`; cap: grep from-imports naming `UsageError` or star imports under `extra`.

**Call:** `grep('^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bUsageError\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*UsageError\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$', 'doc')`

**Response**: outcome `zero`

```

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
    "doc"
   ],
   "desc": "cover `doc` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "IMPORT",
    "extra"
   ],
   "desc": "cover `extra` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "IMPORT",
    "scripts"
   ],
   "desc": "cover `scripts` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "IMPORT",
    "src"
   ],
   "desc": "cover `src` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "IMPORT",
    "testing"
   ],
   "desc": "cover `testing` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "doc"
   ],
   "desc": "cover `doc` for star lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "extra"
   ],
   "desc": "cover `extra` for star lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "scripts"
   ],
   "desc": "cover `scripts` for star lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "src"
   ],
   "desc": "cover `src` for star lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "testing"
   ],
   "desc": "cover `testing` for star lines"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/_io/terminalwriter.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/_io/terminalwriter.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/argparsing.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/argparsing.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/findpaths.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/logging.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/logging.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/main.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/mark/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/mark/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/python.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/pytest/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/pytest/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "UsageError"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/python/collect.py",
    "UsageError"
   ],
   "desc": "outline `testing/python/collect.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_config.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_config.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_findpaths.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_main.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_mark.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_mark.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_parseopt.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_parseopt.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_pluginmanager.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_pluginmanager.py` for its `UsageError` imports"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bUsageError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', 'doc')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bUsageError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \"doc\"]]",
   "v1": [
    10945780377937121897,
    257978959378497840
   ],
   "v2": [
    42487603498035940541,
    1031915837513991360
   ],
   "p_cap": [
    2,
    239
   ],
   "forecast": {
    "zero": [
     208,
     239
    ],
    "mid": [
     29,
     239
    ],
    "cap": [
     2,
     239
    ]
   },
   "serves": [
    [
     "cover",
     "IMPORT",
     "doc"
    ],
    [
     "cover",
     "STAR",
     "doc"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bUsageError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', 'extra')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bUsageError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \"extra\"]]",
   "v1": [
    10945780377937121897,
  
```
</details>

## Step 10

The grep under `doc` returned nothing, and it was not capped, so there are no such lines there.

Candidate modules so far: 18; statements confirmed: 1, ruled out: 0, modules with no such import: 0, pending: 17. import coverage open at `extra`, `scripts`, `src`, `testing`; star coverage open at `extra`, `scripts`, `src`, `testing`.

Still to settle: cover `extra` for import lines; cover `scripts` for import lines; cover `src` for import lines; cover `testing` for import lines; and 21 more.

Next: grep from-imports naming `UsageError` or star imports under `extra`, because import and star lines under `extra` in one call. I expect: no hits (about 85%); hits under the cap (about 10%); a capped result (under 5%). The alternative, grep from-imports naming `UsageError` or star imports under `scripts`, scores the same; the seed broke the tie. Plan by outcome: zero: grep from-imports naming `UsageError` or star imports under `scripts`; mid: grep from-imports naming `UsageError` or star imports under `scripts`; cap: grep from-imports naming `UsageError` or star imports under `scripts`.

**Call:** `grep('^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bUsageError\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*UsageError\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$', 'extra')`

**Response**: outcome `zero`

```

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
    "extra"
   ],
   "desc": "cover `extra` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "IMPORT",
    "scripts"
   ],
   "desc": "cover `scripts` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "IMPORT",
    "src"
   ],
   "desc": "cover `src` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "IMPORT",
    "testing"
   ],
   "desc": "cover `testing` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "extra"
   ],
   "desc": "cover `extra` for star lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "scripts"
   ],
   "desc": "cover `scripts` for star lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "src"
   ],
   "desc": "cover `src` for star lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "testing"
   ],
   "desc": "cover `testing` for star lines"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/_io/terminalwriter.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/_io/terminalwriter.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/argparsing.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/argparsing.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/findpaths.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/logging.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/logging.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/main.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/mark/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/mark/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/python.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/pytest/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/pytest/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "UsageError"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/python/collect.py",
    "UsageError"
   ],
   "desc": "outline `testing/python/collect.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_config.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_config.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_findpaths.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_main.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_mark.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_mark.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_parseopt.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_parseopt.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_pluginmanager.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_pluginmanager.py` for its `UsageError` imports"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bUsageError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', 'extra')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bUsageError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \"extra\"]]",
   "v1": [
    5831066940990519971,
    147416548216284480
   ],
   "v2": [
    3952195057322109275,
    103191583751399136
   ],
   "p_cap": [
    2,
    239
   ],
   "forecast": {
    "zero": [
     208,
     239
    ],
    "mid": [
     29,
     239
    ],
    "cap": [
     2,
     239
    ]
   },
   "serves": [
    [
     "cover",
     "IMPORT",
     "extra"
    ],
    [
     "cover",
     "STAR",
     "extra"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bUsageError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', 'scripts')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bUsageError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \"scripts\"]]",
   "v1": [
    5831066940990519971,
    147416548216284480
   ],
   "v2": [
    3952195057322109275,
    103191583751399136
   ],
   "p_cap": [
    2,
    239
   ],
   "forecast": {
    "zero": [
     208,
     239
    ],
    "mid": [
     29,
     239
    ],
    "cap": [
     
```
</details>

## Step 11

The grep under `extra` returned nothing, and it was not capped, so there are no such lines there.

Candidate modules so far: 18; statements confirmed: 1, ruled out: 0, modules with no such import: 0, pending: 17. import coverage open at `scripts`, `src`, `testing`; star coverage open at `scripts`, `src`, `testing`.

Outstanding: cover `scripts` for import lines; cover `src` for import lines; cover `testing` for import lines; cover `scripts` for star lines; and 19 more.

Next: grep from-imports naming `UsageError` or star imports under `scripts`, because import and star lines under `scripts` in one call. I expect: no hits (about 85%); hits under the cap (about 10%); a capped result (under 5%). The alternative, grep from-imports naming `UsageError` or star imports under `src`, scores the same; the seed broke the tie. Plan by outcome: zero: grep from-imports naming `UsageError` or star imports under `src`; mid: grep from-imports naming `UsageError` or star imports under `src`; cap: grep from-imports naming `UsageError` or star imports under `src`.

**Call:** `grep('^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bUsageError\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*UsageError\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$', 'scripts')`

**Response**: outcome `zero`

```

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
    "scripts"
   ],
   "desc": "cover `scripts` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "IMPORT",
    "src"
   ],
   "desc": "cover `src` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "IMPORT",
    "testing"
   ],
   "desc": "cover `testing` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "scripts"
   ],
   "desc": "cover `scripts` for star lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "src"
   ],
   "desc": "cover `src` for star lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "testing"
   ],
   "desc": "cover `testing` for star lines"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/_io/terminalwriter.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/_io/terminalwriter.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/argparsing.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/argparsing.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/findpaths.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/logging.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/logging.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/main.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/mark/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/mark/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/python.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/pytest/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/pytest/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "UsageError"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/python/collect.py",
    "UsageError"
   ],
   "desc": "outline `testing/python/collect.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_config.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_config.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_findpaths.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_main.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_mark.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_mark.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_parseopt.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_parseopt.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_pluginmanager.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_pluginmanager.py` for its `UsageError` imports"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bUsageError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', 'scripts')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bUsageError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \"scripts\"]]",
   "v1": [
    18925907831059396003,
    515957918756995680
   ],
   "v2": [
    36556297648406244959,
    1031915837513991360
   ],
   "p_cap": [
    2,
    239
   ],
   "forecast": {
    "zero": [
     208,
     239
    ],
    "mid": [
     29,
     239
    ],
    "cap": [
     2,
     239
    ]
   },
   "serves": [
    [
     "cover",
     "IMPORT",
     "scripts"
    ],
    [
     "cover",
     "STAR",
     "scripts"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bUsageError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', 'src')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bUsageError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \"src\"]]",
   "v1": [
    18925907831059396003,
    515957918756995680
   ],
   "v2": [
    36556297648406244959,
    1031915837513991360
   ],
   "p_cap": [
    2,
    239
   ],
   "forecast": {
    "zero": [
     208,
     239
    ],
    "mid": [
     29,
     239
    ],
    "cap": [
     2,
     239
    ]
   },
   "serves": [
    [
     "cover",
     "IMPORT",
     "src"
    ],
    [
     "cover",
     "STAR",
     "src"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bUsageError\\\\b|\\\\*)|^\
```
</details>

## Step 12

The grep under `scripts` returned nothing, and it was not capped, so there are no such lines there.

Candidate modules so far: 18; statements confirmed: 1, ruled out: 0, modules with no such import: 0, pending: 17. import coverage open at `src`, `testing`; star coverage open at `src`, `testing`.

Open: cover `src` for import lines; cover `testing` for import lines; cover `src` for star lines; cover `testing` for star lines; and 17 more.

Next: grep from-imports naming `UsageError` or star imports under `src`, because import and star lines under `src` in one call. I expect: no hits (about 85%); hits under the cap (about 10%); a capped result (under 5%). The alternative, grep from-imports naming `UsageError` or star imports under `testing`, scores the same; the seed broke the tie. Plan by outcome: zero: grep from-imports naming `UsageError` or star imports under `testing`; mid: grep from-imports naming `UsageError` or star imports under `testing`; cap: grep from-imports naming `UsageError` or star imports under `testing`.

**Call:** `grep('^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bUsageError\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*UsageError\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$', 'src')`

**Response**: outcome `mid`

```
src/_pytest/_io/terminalwriter.py:217:        from _pytest.config.exceptions import UsageError
src/_pytest/config/__init__.py:51:from .exceptions import UsageError as UsageError
src/_pytest/config/argparsing.py:22:from .exceptions import UsageError
src/_pytest/config/findpaths.py:16:from .exceptions import UsageError
src/_pytest/debugging.py:24:from _pytest.config.exceptions import UsageError
src/_pytest/logging.py:35:from _pytest.config import UsageError
src/_pytest/main.py:34:from _pytest.config import UsageError
src/_pytest/mark/__init__.py:27:from _pytest.config import UsageError
src/_pytest/python.py:56:from _pytest.config import UsageError
src/pytest/__init__.py:22:from _pytest.config import UsageError
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
    "src"
   ],
   "desc": "cover `src` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "IMPORT",
    "testing"
   ],
   "desc": "cover `testing` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "src"
   ],
   "desc": "cover `src` for star lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "testing"
   ],
   "desc": "cover `testing` for star lines"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/_io/terminalwriter.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/_io/terminalwriter.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/argparsing.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/argparsing.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/findpaths.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/logging.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/logging.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/main.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/mark/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/mark/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/python.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/pytest/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/pytest/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "UsageError"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/python/collect.py",
    "UsageError"
   ],
   "desc": "outline `testing/python/collect.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_config.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_config.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_findpaths.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_main.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_mark.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_mark.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_parseopt.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_parseopt.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_pluginmanager.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_pluginmanager.py` for its `UsageError` imports"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bUsageError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', 'src')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bUsageError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \"src\"]]",
   "v1": [
    6977232547460788843,
    206383167502798272
   ],
   "v2": [
    834834251267,
    25646387340
   ],
   "p_cap": [
    2,
    239
   ],
   "forecast": {
    "zero": [
     208,
     239
    ],
    "mid": [
     29,
     239
    ],
    "cap": [
     2,
     239
    ]
   },
   "serves": [
    [
     "cover",
     "IMPORT",
     "src"
    ],
    [
     "cover",
     "STAR",
     "src"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bUsageError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', 'testing')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bUsageError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \"testing\"]]",
   "v1": [
    6977232547460788843,
    206383167502798272
   ],
   "v2": [
    834834251267,
    25646387340
   ],
   "p_cap": [
    2,
    239
   ],
   "forecast": {
    "zero": [
     208,
     239
    ],
    "mid": [
     29,
     239
    ],
    "cap": [
     2,
     239
    ]
   },
   "serves": [
    [
     "cover",
     "IMPORT",
     "testing"
    ],
    [
     "cover",
     "STAR",
     "testing"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bUsageError\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', 'src')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bUsageError\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\
```
</details>

## Step 13

The grep under `src` returned 10 lines, under the cap, so these are all of them: `src/_pytest/_io/terminalwriter.py`, `src/_pytest/config/__init__.py`, `src/_pytest/config/argparsing.py`, `src/_pytest/config/findpaths.py` and 6 more files.

Candidate modules so far: 18; statements confirmed: 1, ruled out: 0, modules with no such import: 0, pending: 17. import coverage open at `testing`; star coverage open at `testing`.

Outstanding: cover `testing` for import lines; cover `testing` for star lines; outline `src/_pytest/_io/terminalwriter.py` for its `UsageError` imports; outline `src/_pytest/config/__init__.py` for its `UsageError` imports; and 15 more.

Next: grep from-imports naming `UsageError` or star imports under `testing`, because import and star lines under `testing` in one call. I expect: no hits (about 85%); hits under the cap (about 10%); a capped result (under 5%). The alternative, outline `src/_pytest/_io/terminalwriter.py` filtered to `UsageError`, serves fewer of the open items. Plan by outcome: zero: outline `src/_pytest/_io/terminalwriter.py` filtered to `UsageError`; mid: outline `src/_pytest/_io/terminalwriter.py` filtered to `UsageError`; cap: outline `src/_pytest/_io/terminalwriter.py` filtered to `UsageError`.

**Call:** `grep('^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bUsageError\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*UsageError\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$', 'testing')`

**Response**: outcome `mid`

```
testing/acceptance_test.py:599:            from pytest import *
testing/python/collect.py:11:from _pytest.config.exceptions import UsageError
testing/test_config.py:28:from _pytest.config.exceptions import UsageError
testing/test_config.py:1354:            UsageError,
testing/test_findpaths.py:8:from _pytest.config import UsageError
testing/test_main.py:10:from _pytest.config import UsageError
testing/test_main.py:271:            UsageError,
testing/test_mark.py:13:from _pytest.config import UsageError
testing/test_parseopt.py:13:from _pytest.config.exceptions import UsageError
testing/test_pluginmanager.py:16:from _pytest.config.exceptions import UsageError
testing/test_session.py:5:from _pytest.config.exceptions import UsageError
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
    "testing"
   ],
   "desc": "cover `testing` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "testing"
   ],
   "desc": "cover `testing` for star lines"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/_io/terminalwriter.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/_io/terminalwriter.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/argparsing.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/argparsing.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/findpaths.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/logging.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/logging.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/main.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/mark/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/mark/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/python.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/pytest/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/pytest/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "UsageError"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/python/collect.py",
    "UsageError"
   ],
   "desc": "outline `testing/python/collect.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_config.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_config.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_findpaths.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_main.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_mark.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_mark.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_parseopt.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_parseopt.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_pluginmanager.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_pluginmanager.py` for its `UsageError` imports"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bUsageError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', 'testing')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bUsageError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*UsageError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \"testing\"]]",
   "v1": [
    68226043919791,
    2205589311240
   ],
   "v2": [
    341350778530079,
    11027946556200
   ],
   "p_cap": [
    2,
    239
   ],
   "forecast": {
    "zero": [
     208,
     239
    ],
    "mid": [
     29,
     239
    ],
    "cap": [
     2,
     239
    ]
   },
   "serves": [
    [
     "cover",
     "IMPORT",
     "testing"
    ],
    [
     "cover",
     "STAR",
     "testing"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/_io/terminalwriter.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/_io/terminalwriter.py\", \"UsageError\"]]",
   "v1": [
    40901631975082357,
    1269893966913600
   ],
   "v2": [
    341350778530079,
    11027946556200
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
     "src/_pytest/_io/terminalwriter.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/config/__init__.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/config/__init__.py\", \"UsageError\"]]",
   "v1": [
    40901631975082357,
    1269893966913600
   ],
   "v2": [
    341350778530079,
    11027946556200
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
     "src/_pytest/config/__init__.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/config/argparsing.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/config/argparsing.py\", \"UsageError\"]]",
   "v1": [
    40901631975082357,
    1269893966913600
   ],
   "v2": [
    341350778530079,
    11027946556200
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
     "src/_pytest/config/argparsing.py",
     "UsageError"
 
```
</details>

## Step 14

The grep under `testing` returned 11 lines, under the cap, so these are all of them: `testing/acceptance_test.py`, `testing/python/collect.py`, `testing/test_config.py`, `testing/test_findpaths.py` and 5 more files.

Candidate modules so far: 19; statements confirmed: 1, ruled out: 0, modules with no such import: 0, pending: 18. import coverage complete; star coverage complete.

Open: outline `src/_pytest/_io/terminalwriter.py` for its `UsageError` imports; outline `src/_pytest/config/__init__.py` for its `UsageError` imports; outline `src/_pytest/config/argparsing.py` for its `UsageError` imports; outline `src/_pytest/config/findpaths.py` for its `UsageError` imports; and 14 more.

Next: outline `src/_pytest/_io/terminalwriter.py` filtered to `UsageError`, because `src/_pytest/_io/terminalwriter.py` had a matching line (step 5); its outline names every `UsageError` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/_pytest/config/__init__.py` filtered to `UsageError`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/_pytest/config/__init__.py` filtered to `UsageError`; cap: outline `src/_pytest/config/__init__.py` filtered to `UsageError`.

**Call:** `symbols('src/_pytest/_io/terminalwriter.py', 'UsageError')`

**Response**: outcome `ok`

```
module src/_pytest/_io/terminalwriter.py lines=259 dynamic=no all=none
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/_io/terminalwriter.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/_io/terminalwriter.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/argparsing.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/argparsing.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/findpaths.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/logging.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/logging.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/main.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/mark/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/mark/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/python.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/pytest/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/pytest/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "UsageError"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/python/collect.py",
    "UsageError"
   ],
   "desc": "outline `testing/python/collect.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_config.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_config.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_findpaths.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_main.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_mark.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_mark.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_parseopt.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_parseopt.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_pluginmanager.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_pluginmanager.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_session.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_session.py` for its `UsageError` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/_io/terminalwriter.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/_io/terminalwriter.py\", \"UsageError\"]]",
   "v1": [
    1268767,
    40850
   ],
   "v2": [
    634792,
    20425
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
     "src/_pytest/_io/terminalwriter.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/config/__init__.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/config/__init__.py\", \"UsageError\"]]",
   "v1": [
    1268767,
    40850
   ],
   "v2": [
    634792,
    20425
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
     "src/_pytest/config/__init__.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/config/argparsing.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/config/argparsing.py\", \"UsageError\"]]",
   "v1": [
    1268767,
    40850
   ],
   "v2": [
    634792,
    20425
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
     "src/_pytest/config/argparsing.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/config/findpaths.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/config/findpaths.py\", \"UsageError\"]]",
   "v1": [
    1268767,
    40850
   ],
   "v2": [
    634792,
    20425
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
     "src/_pytest/config/findpaths.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/logging.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/logging.py\", \"UsageError\"]]",
   "v1": [
    1268767,
    40850
   ],
   "v2": [
    634792,
    20425
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
     "src/_pytest/logging.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/main.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/main.py\", \"UsageError\"]]",
   "v1": [
    1268
```
</details>

## Step 15

`src/_pytest/_io/terminalwriter.py` binds no `UsageError` at module level; no star imports; no `__all__`; no dynamic namespace tricks.

Candidate modules so far: 19; statements confirmed: 1, ruled out: 0, modules with no such import: 1, pending: 17. import coverage complete; star coverage complete.

Still to settle: outline `src/_pytest/config/__init__.py` for its `UsageError` imports; outline `src/_pytest/config/argparsing.py` for its `UsageError` imports; outline `src/_pytest/config/findpaths.py` for its `UsageError` imports; outline `src/_pytest/logging.py` for its `UsageError` imports; and 13 more.

Next: outline `src/_pytest/config/__init__.py` filtered to `UsageError`, because `src/_pytest/config/__init__.py` had a matching line (step 5); its outline names every `UsageError` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/_pytest/config/argparsing.py` filtered to `UsageError`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/_pytest/config/argparsing.py` filtered to `UsageError`; cap: outline `src/_pytest/config/argparsing.py` filtered to `UsageError`.

**Call:** `symbols('src/_pytest/config/__init__.py', 'UsageError')`

**Response**: outcome `ok`

```
module src/_pytest/config/__init__.py lines=2454 dynamic=no all=none
51 from UsageError <- .exceptions UsageError
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/argparsing.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/argparsing.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/findpaths.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/logging.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/logging.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/main.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/mark/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/mark/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/python.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/pytest/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/pytest/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "UsageError"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/python/collect.py",
    "UsageError"
   ],
   "desc": "outline `testing/python/collect.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_config.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_config.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_findpaths.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_main.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_mark.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_mark.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_parseopt.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_parseopt.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_pluginmanager.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_pluginmanager.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_session.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_session.py` for its `UsageError` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/config/__init__.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/config/__init__.py\", \"UsageError\"]]",
   "v1": [
    1797488,
    61275
   ],
   "v2": [
    3597427,
    122550
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
     "src/_pytest/config/__init__.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/config/argparsing.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/config/argparsing.py\", \"UsageError\"]]",
   "v1": [
    1797488,
    61275
   ],
   "v2": [
    3597427,
    122550
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
     "src/_pytest/config/argparsing.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/config/findpaths.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/config/findpaths.py\", \"UsageError\"]]",
   "v1": [
    1797488,
    61275
   ],
   "v2": [
    3597427,
    122550
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
     "src/_pytest/config/findpaths.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/logging.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/logging.py\", \"UsageError\"]]",
   "v1": [
    1797488,
    61275
   ],
   "v2": [
    3597427,
    122550
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
     "src/_pytest/logging.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/main.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/main.py\", \"UsageError\"]]",
   "v1": [
    1797488,
    61275
   ],
   "v2": [
    3597427,
    122550
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
     "src/_pytest/main.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/mark/__init__.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/mark/__init__.py\", \"UsageError\"]]",
   "v1": [
    1797488,
    61275
   ],
   "v2": [
    3597427,
    122550
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
     "outli
```
</details>

## Step 16

In `src/_pytest/config/__init__.py`, `UsageError` has exactly one binding: line 51 imports it as `UsageError` from `.exceptions`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 19; statements confirmed: 2, ruled out: 0, modules with no such import: 1, pending: 16. import coverage complete; star coverage complete.

Outstanding: outline `src/_pytest/config/argparsing.py` for its `UsageError` imports; outline `src/_pytest/config/findpaths.py` for its `UsageError` imports; outline `src/_pytest/logging.py` for its `UsageError` imports; outline `src/_pytest/main.py` for its `UsageError` imports; and 12 more.

Next: outline `src/_pytest/config/argparsing.py` filtered to `UsageError`, because `src/_pytest/config/argparsing.py` had a matching line (step 5); its outline names every `UsageError` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/_pytest/config/findpaths.py` filtered to `UsageError`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/_pytest/config/findpaths.py` filtered to `UsageError`; cap: outline `src/_pytest/config/findpaths.py` filtered to `UsageError`.

**Call:** `symbols('src/_pytest/config/argparsing.py', 'UsageError')`

**Response**: outcome `ok`

```
module src/_pytest/config/argparsing.py lines=616 dynamic=no all=none
22 from UsageError <- .exceptions UsageError
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/argparsing.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/argparsing.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/findpaths.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/logging.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/logging.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/main.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/mark/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/mark/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/python.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/pytest/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/pytest/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "UsageError"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/python/collect.py",
    "UsageError"
   ],
   "desc": "outline `testing/python/collect.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_config.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_config.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_findpaths.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_main.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_mark.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_mark.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_parseopt.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_parseopt.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_pluginmanager.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_pluginmanager.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_session.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_session.py` for its `UsageError` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/config/argparsing.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/config/argparsing.py\", \"UsageError\"]]",
   "v1": [
    3383651,
    122550
   ],
   "v2": [
    1693051,
    61275
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
     "src/_pytest/config/argparsing.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/config/findpaths.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/config/findpaths.py\", \"UsageError\"]]",
   "v1": [
    3383651,
    122550
   ],
   "v2": [
    1693051,
    61275
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
     "src/_pytest/config/findpaths.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/logging.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/logging.py\", \"UsageError\"]]",
   "v1": [
    3383651,
    122550
   ],
   "v2": [
    1693051,
    61275
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
     "src/_pytest/logging.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/main.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/main.py\", \"UsageError\"]]",
   "v1": [
    3383651,
    122550
   ],
   "v2": [
    1693051,
    61275
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
     "src/_pytest/main.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/mark/__init__.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/mark/__init__.py\", \"UsageError\"]]",
   "v1": [
    3383651,
    122550
   ],
   "v2": [
    1693051,
    61275
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
     "src/_pytest/mark/__init__.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/python.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/python.py\", \"UsageError\"]]",
   "v1": [
    3383651,
    122550
   ],
   "v2": [
    1693051,
    61275
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
     "src/_pytest/python.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/pytest/__init__.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/pytest/__init__.py\", \"UsageError\"]]",
   "v1": [
   
```
</details>

## Step 17

In `src/_pytest/config/argparsing.py`, `UsageError` has exactly one binding: line 22 imports it as `UsageError` from `.exceptions`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 19; statements confirmed: 3, ruled out: 0, modules with no such import: 1, pending: 15. import coverage complete; star coverage complete.

Still to settle: outline `src/_pytest/config/findpaths.py` for its `UsageError` imports; outline `src/_pytest/logging.py` for its `UsageError` imports; outline `src/_pytest/main.py` for its `UsageError` imports; outline `src/_pytest/mark/__init__.py` for its `UsageError` imports; and 11 more.

Next: outline `src/_pytest/config/findpaths.py` filtered to `UsageError`, because `src/_pytest/config/findpaths.py` had a matching line (step 5); its outline names every `UsageError` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/_pytest/logging.py` filtered to `UsageError`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/_pytest/logging.py` filtered to `UsageError`; cap: outline `src/_pytest/logging.py` filtered to `UsageError`.

**Call:** `symbols('src/_pytest/config/findpaths.py', 'UsageError')`

**Response**: outcome `ok`

```
module src/_pytest/config/findpaths.py lines=508 dynamic=no all=none
16 from UsageError <- .exceptions UsageError
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/findpaths.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/config/findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/logging.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/logging.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/main.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/mark/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/mark/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/python.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/pytest/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/pytest/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "UsageError"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/python/collect.py",
    "UsageError"
   ],
   "desc": "outline `testing/python/collect.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_config.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_config.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_findpaths.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_main.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_mark.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_mark.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_parseopt.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_parseopt.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_pluginmanager.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_pluginmanager.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_session.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_session.py` for its `UsageError` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/config/findpaths.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/config/findpaths.py\", \"UsageError\"]]",
   "v1": [
    528721,
    20425
   ],
   "v2": [
    1058259,
    40850
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
     "src/_pytest/config/findpaths.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/logging.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/logging.py\", \"UsageError\"]]",
   "v1": [
    528721,
    20425
   ],
   "v2": [
    1058259,
    40850
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
     "src/_pytest/logging.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/main.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/main.py\", \"UsageError\"]]",
   "v1": [
    528721,
    20425
   ],
   "v2": [
    1058259,
    40850
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
     "src/_pytest/main.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/mark/__init__.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/mark/__init__.py\", \"UsageError\"]]",
   "v1": [
    528721,
    20425
   ],
   "v2": [
    1058259,
    40850
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
     "src/_pytest/mark/__init__.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/python.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/python.py\", \"UsageError\"]]",
   "v1": [
    528721,
    20425
   ],
   "v2": [
    1058259,
    40850
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
     "src/_pytest/python.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/pytest/__init__.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/pytest/__init__.py\", \"UsageError\"]]",
   "v1": [
    528721,
    20425
   ],
   "v2": [
    1058259,
    40850
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
     "src/pytest/__init__.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/acceptance_test.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"UsageError\"]]",
   "v1": [
    528721,
    20425
   ],
   "v2": [
    1058259,
    40850
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
     "test
```
</details>

## Step 18

In `src/_pytest/config/findpaths.py`, `UsageError` has exactly one binding: line 16 imports it as `UsageError` from `.exceptions`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 19; statements confirmed: 4, ruled out: 0, modules with no such import: 1, pending: 14. import coverage complete; star coverage complete.

Open: outline `src/_pytest/logging.py` for its `UsageError` imports; outline `src/_pytest/main.py` for its `UsageError` imports; outline `src/_pytest/mark/__init__.py` for its `UsageError` imports; outline `src/_pytest/python.py` for its `UsageError` imports; and 10 more.

Next: outline `src/_pytest/logging.py` filtered to `UsageError`, because `src/_pytest/logging.py` had a matching line (step 5); its outline names every `UsageError` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/_pytest/main.py` filtered to `UsageError`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/_pytest/main.py` filtered to `UsageError`; cap: outline `src/_pytest/main.py` filtered to `UsageError`.

**Call:** `symbols('src/_pytest/logging.py', 'UsageError')`

**Response**: outcome `ok`

```
module src/_pytest/logging.py lines=979 dynamic=no all=none
35 from UsageError <- _pytest.config UsageError
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/logging.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/logging.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/main.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/mark/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/mark/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/python.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/pytest/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/pytest/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "UsageError"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/python/collect.py",
    "UsageError"
   ],
   "desc": "outline `testing/python/collect.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_config.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_config.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_findpaths.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_main.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_mark.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_mark.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_parseopt.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_parseopt.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_pluginmanager.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_pluginmanager.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_session.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_session.py` for its `UsageError` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/logging.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/logging.py\", \"UsageError\"]]",
   "v1": [
    2961001,
    122550
   ],
   "v2": [
    1481726,
    61275
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
     "src/_pytest/logging.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/main.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/main.py\", \"UsageError\"]]",
   "v1": [
    2961001,
    122550
   ],
   "v2": [
    1481726,
    61275
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
     "src/_pytest/main.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/mark/__init__.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/mark/__init__.py\", \"UsageError\"]]",
   "v1": [
    2961001,
    122550
   ],
   "v2": [
    1481726,
    61275
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
     "src/_pytest/mark/__init__.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/python.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/python.py\", \"UsageError\"]]",
   "v1": [
    2961001,
    122550
   ],
   "v2": [
    1481726,
    61275
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
     "src/_pytest/python.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/pytest/__init__.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/pytest/__init__.py\", \"UsageError\"]]",
   "v1": [
    2961001,
    122550
   ],
   "v2": [
    1481726,
    61275
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
     "src/pytest/__init__.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/acceptance_test.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"UsageError\"]]",
   "v1": [
    2961001,
    122550
   ],
   "v2": [
    1481726,
    61275
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
     "testing/acceptance_test.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/python/collect.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/python/collect.py\", \"UsageError\"]]",
   "v1": [
    2961001,
    122550
   ],
   "v2": [
    1481726,
    61275
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
     "testing/python/collect.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_config.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_config.py\", \"UsageError\"]]",
   "v1": [
```
</details>

## Step 19

In `src/_pytest/logging.py`, `UsageError` has exactly one binding: line 35 imports it as `UsageError` from `_pytest.config`. No dynamic namespace tricks, no `__all__`. The call I had planned for this outcome is no longer useful, so I am re-planning.

Candidate modules so far: 19; statements confirmed: 4, ruled out: 0, modules with no such import: 1, pending: 14. import coverage complete; star coverage complete.

Outstanding: locate the module `_pytest.config` imported by `src/_pytest/logging.py`; outline `src/_pytest/main.py` for its `UsageError` imports; outline `src/_pytest/mark/__init__.py` for its `UsageError` imports; outline `src/_pytest/python.py` for its `UsageError` imports; and 10 more.

Next: outline `src/_pytest/config.py` filtered to `UsageError`, because `_pytest.config` would be `src/_pytest/config.py` if that file exists; one call both checks and closes it. I expect: a definition there ends the chain (about 85%); the file does not exist (about 10%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `src/_pytest/main.py` filtered to `UsageError`, is expected to open more follow-up work. Plan by outcome: def: outline `src/_pytest/main.py` filtered to `UsageError`; reexport: outline `src/_pytest/main.py` filtered to `UsageError`; star: outline `src/_pytest/main.py` filtered to `UsageError`; none: outline `src/_pytest/main.py` filtered to `UsageError`; missing: list `src/_pytest`.

**Call:** `symbols('src/_pytest/config.py', 'UsageError')`

**Response**: outcome `missing`

```
error: not a python file: src/_pytest/config.py
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/_pytest/logging.py",
    "_pytest.config"
   ],
   "desc": "locate the module `_pytest.config` imported by `src/_pytest/logging.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/main.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/mark/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/mark/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/python.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/pytest/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/pytest/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "UsageError"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/python/collect.py",
    "UsageError"
   ],
   "desc": "outline `testing/python/collect.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_config.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_config.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_findpaths.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_main.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_mark.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_mark.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_parseopt.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_parseopt.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_pluginmanager.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_pluginmanager.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_session.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_session.py` for its `UsageError` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/config.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/config.py\", \"UsageError\"]]",
   "v1": [
    29598570451,
    1250019804
   ],
   "v2": [
    22958203580813,
    968765348100
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     205972,
     243411
    ],
    "reexport": [
     1864,
     81137
    ],
    "star": [
     466,
     243411
    ],
    "none": [
     932,
     34773
    ],
    "missing": [
     53,
     519
    ]
   },
   "serves": [
    [
     "module_path",
     "src/_pytest/logging.py",
     "_pytest.config"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/main.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/main.py\", \"UsageError\"]]",
   "v1": [
    6003527,
    245100
   ],
   "v2": [
    740589271177,
    31250495100
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
     "src/_pytest/main.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/mark/__init__.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/mark/__init__.py\", \"UsageError\"]]",
   "v1": [
    6003527,
    245100
   ],
   "v2": [
    740589271177,
    31250495100
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
     "src/_pytest/mark/__init__.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/python.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/python.py\", \"UsageError\"]]",
   "v1": [
    6003527,
    245100
   ],
   "v2": [
    740589271177,
    31250495100
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
     "src/_pytest/python.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/pytest/__init__.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/pytest/__init__.py\", \"UsageError\"]]",
   "v1": [
    6003527,
    245100
   ],
   "v2": [
    740589271177,
    31250495100
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
     "src/pytest/__init__.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/acceptance_test.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"UsageError\"]]",
   "v1": [
    6003527,
    245100
   ],
   "v2": [
    740589271177,
    31250495100
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
     "testing/acceptance_test.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/python/collect.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/python/collect.py\", \"UsageError\"]]",
   "v1": [
    6003527,
    245100
   ],
   "v2": [
    740589271177,
    31250495100
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
    
```
</details>

## Step 20

`src/_pytest/config.py` does not exist, so that path is ruled out. The call I had planned for this outcome is no longer useful, so I am re-planning.

Candidate modules so far: 19; statements confirmed: 5, ruled out: 0, modules with no such import: 1, pending: 13. import coverage complete; star coverage complete.

Open: outline `src/_pytest/main.py` for its `UsageError` imports; outline `src/_pytest/mark/__init__.py` for its `UsageError` imports; outline `src/_pytest/python.py` for its `UsageError` imports; outline `src/pytest/__init__.py` for its `UsageError` imports; and 9 more.

Next: outline `testing/test_session.py` filtered to `UsageError`, because `testing/test_session.py` had a matching line (step 13); its outline names every `UsageError` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/_pytest/main.py` filtered to `UsageError`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/_pytest/main.py` filtered to `UsageError`; cap: outline `src/_pytest/main.py` filtered to `UsageError`.

**Call:** `symbols('testing/test_session.py', 'UsageError')`

**Response**: outcome `ok`

```
module testing/test_session.py lines=486 dynamic=no all=none
5 from UsageError <- _pytest.config.exceptions UsageError
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/main.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/mark/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/mark/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/python.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/pytest/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/pytest/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "UsageError"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/python/collect.py",
    "UsageError"
   ],
   "desc": "outline `testing/python/collect.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_config.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_config.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_findpaths.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_main.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_mark.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_mark.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_parseopt.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_parseopt.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_pluginmanager.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_pluginmanager.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_session.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_session.py` for its `UsageError` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/main.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/main.py\", \"UsageError\"]]",
   "v1": [
    1374838,
    61275
   ],
   "v2": [
    2752127,
    122550
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
     "src/_pytest/main.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/mark/__init__.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/mark/__init__.py\", \"UsageError\"]]",
   "v1": [
    1374838,
    61275
   ],
   "v2": [
    2752127,
    122550
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
     "src/_pytest/mark/__init__.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/python.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/python.py\", \"UsageError\"]]",
   "v1": [
    1374838,
    61275
   ],
   "v2": [
    2752127,
    122550
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
     "src/_pytest/python.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/pytest/__init__.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/pytest/__init__.py\", \"UsageError\"]]",
   "v1": [
    1374838,
    61275
   ],
   "v2": [
    2752127,
    122550
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
     "src/pytest/__init__.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/acceptance_test.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"UsageError\"]]",
   "v1": [
    1374838,
    61275
   ],
   "v2": [
    2752127,
    122550
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
     "testing/acceptance_test.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/python/collect.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/python/collect.py\", \"UsageError\"]]",
   "v1": [
    1374838,
    61275
   ],
   "v2": [
    2752127,
    122550
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
     "testing/python/collect.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_config.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_config.py\", \"UsageError\"]]",
   "v1": [
    1374838,
    61275
   ],
   "v2": [
    2752127,
    122550
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
     "testing/test_config.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_findpaths.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_findpaths.py\", \"UsageError\"]]",
   "v1": [
    1374838,
    61275
   ],
   "v2": [
    2752127,
    122550
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
 
```
</details>

## Step 21

In `testing/test_session.py`, `UsageError` has exactly one binding: line 5 imports it as `UsageError` from `_pytest.config.exceptions`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 19; statements confirmed: 6, ruled out: 0, modules with no such import: 1, pending: 12. import coverage complete; star coverage complete.

Still to settle: outline `src/_pytest/main.py` for its `UsageError` imports; outline `src/_pytest/mark/__init__.py` for its `UsageError` imports; outline `src/_pytest/python.py` for its `UsageError` imports; outline `src/pytest/__init__.py` for its `UsageError` imports; and 8 more.

Next: outline `src/_pytest/main.py` filtered to `UsageError`, because `src/_pytest/main.py` had a matching line (step 5); its outline names every `UsageError` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/_pytest/mark/__init__.py` filtered to `UsageError`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/_pytest/mark/__init__.py` filtered to `UsageError`; cap: outline `src/_pytest/mark/__init__.py` filtered to `UsageError`.

**Call:** `symbols('src/_pytest/main.py', 'UsageError')`

**Response**: outcome `ok`

```
module src/_pytest/main.py lines=1240 dynamic=no all=none
34 from UsageError <- _pytest.config UsageError
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/main.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/mark/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/mark/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/python.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/pytest/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/pytest/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "UsageError"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/python/collect.py",
    "UsageError"
   ],
   "desc": "outline `testing/python/collect.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_config.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_config.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_findpaths.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_main.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_mark.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_mark.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_parseopt.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_parseopt.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_pluginmanager.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_pluginmanager.py` for its `UsageError` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/main.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/main.py\", \"UsageError\"]]",
   "v1": [
    846117,
    40850
   ],
   "v2": [
    423467,
    20425
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
     "src/_pytest/main.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/mark/__init__.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/mark/__init__.py\", \"UsageError\"]]",
   "v1": [
    846117,
    40850
   ],
   "v2": [
    423467,
    20425
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
     "src/_pytest/mark/__init__.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/python.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/python.py\", \"UsageError\"]]",
   "v1": [
    846117,
    40850
   ],
   "v2": [
    423467,
    20425
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
     "src/_pytest/python.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/pytest/__init__.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/pytest/__init__.py\", \"UsageError\"]]",
   "v1": [
    846117,
    40850
   ],
   "v2": [
    423467,
    20425
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
     "src/pytest/__init__.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/acceptance_test.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"UsageError\"]]",
   "v1": [
    846117,
    40850
   ],
   "v2": [
    423467,
    20425
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
     "testing/acceptance_test.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/python/collect.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/python/collect.py\", \"UsageError\"]]",
   "v1": [
    846117,
    40850
   ],
   "v2": [
    423467,
    20425
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
     "testing/python/collect.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_config.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_config.py\", \"UsageError\"]]",
   "v1": [
    846117,
    40850
   ],
   "v2": [
    423467,
    20425
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
     "testing/test_config.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_findpaths.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_findpaths.py\", \"UsageError\"]]",
   "v1": [
    846117,
    40850
   ],
   "v2": [
    423467,
    20425
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
     "testing/test_findpaths.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_main.py', 'UsageError')",
   "key": "[\"symbols\",
```
</details>

## Step 22

In `src/_pytest/main.py`, `UsageError` has exactly one binding: line 34 imports it as `UsageError` from `_pytest.config`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 19; statements confirmed: 7, ruled out: 0, modules with no such import: 1, pending: 11. import coverage complete; star coverage complete.

Open: outline `src/_pytest/mark/__init__.py` for its `UsageError` imports; outline `src/_pytest/python.py` for its `UsageError` imports; outline `src/pytest/__init__.py` for its `UsageError` imports; outline `testing/acceptance_test.py` for its `UsageError` imports; and 7 more.

Next: outline `src/_pytest/mark/__init__.py` filtered to `UsageError`, because `src/_pytest/mark/__init__.py` had a matching line (step 5); its outline names every `UsageError` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/_pytest/python.py` filtered to `UsageError`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/_pytest/python.py` filtered to `UsageError`; cap: outline `src/_pytest/python.py` filtered to `UsageError`.

**Call:** `symbols('src/_pytest/mark/__init__.py', 'UsageError')`

**Response**: outcome `ok`

```
module src/_pytest/mark/__init__.py lines=324 dynamic=no all=static@36
27 from UsageError <- _pytest.config UsageError
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/mark/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/mark/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/python.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/pytest/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/pytest/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "UsageError"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/python/collect.py",
    "UsageError"
   ],
   "desc": "outline `testing/python/collect.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_config.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_config.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_findpaths.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_main.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_mark.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_mark.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_parseopt.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_parseopt.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_pluginmanager.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_pluginmanager.py` for its `UsageError` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/mark/__init__.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/mark/__init__.py\", \"UsageError\"]]",
   "v1": [
    1163513,
    61275
   ],
   "v2": [
    2329477,
    122550
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
     "src/_pytest/mark/__init__.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/python.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/python.py\", \"UsageError\"]]",
   "v1": [
    1163513,
    61275
   ],
   "v2": [
    2329477,
    122550
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
     "src/_pytest/python.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/pytest/__init__.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/pytest/__init__.py\", \"UsageError\"]]",
   "v1": [
    1163513,
    61275
   ],
   "v2": [
    2329477,
    122550
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
     "src/pytest/__init__.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/acceptance_test.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"UsageError\"]]",
   "v1": [
    1163513,
    61275
   ],
   "v2": [
    2329477,
    122550
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
     "testing/acceptance_test.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/python/collect.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/python/collect.py\", \"UsageError\"]]",
   "v1": [
    1163513,
    61275
   ],
   "v2": [
    2329477,
    122550
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
     "testing/python/collect.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_config.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_config.py\", \"UsageError\"]]",
   "v1": [
    1163513,
    61275
   ],
   "v2": [
    2329477,
    122550
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
     "testing/test_config.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_findpaths.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_findpaths.py\", \"UsageError\"]]",
   "v1": [
    1163513,
    61275
   ],
   "v2": [
    2329477,
    122550
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
     "testing/test_findpaths.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_main.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_main.py\", \"UsageError\"]]",
   "v1": [
    1163513,
    61275
   ],
   "v2": [
    2329477,
    122550
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
     "testing/test_main.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_mark.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_mark.py\", \"UsageError\"]]",
   "v1": [
    1163513,
    61275
   ],
   "v2": [
    2329477,
    122550
   ],
   "p_cap": [
    1,
    
```
</details>

## Step 23

In `src/_pytest/mark/__init__.py`, `UsageError` has exactly one binding: line 27 imports it as `UsageError` from `_pytest.config`. No dynamic namespace tricks, a literal `__all__` at line 36.

Candidate modules so far: 19; statements confirmed: 8, ruled out: 0, modules with no such import: 1, pending: 10. import coverage complete; star coverage complete.

Outstanding: outline `src/_pytest/python.py` for its `UsageError` imports; outline `src/pytest/__init__.py` for its `UsageError` imports; outline `testing/acceptance_test.py` for its `UsageError` imports; outline `testing/python/collect.py` for its `UsageError` imports; and 6 more.

Next: outline `src/_pytest/python.py` filtered to `UsageError`, because `src/_pytest/python.py` had a matching line (step 5); its outline names every `UsageError` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/pytest/__init__.py` filtered to `UsageError`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/pytest/__init__.py` filtered to `UsageError`; cap: outline `src/pytest/__init__.py` filtered to `UsageError`.

**Call:** `symbols('src/_pytest/python.py', 'UsageError')`

**Response**: outcome `ok`

```
module src/_pytest/python.py lines=1843 dynamic=yes all=none
56 from UsageError <- _pytest.config UsageError
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "UsageError"
   ],
   "desc": "outline `src/_pytest/python.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/pytest/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/pytest/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "UsageError"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/python/collect.py",
    "UsageError"
   ],
   "desc": "outline `testing/python/collect.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_config.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_config.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_findpaths.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_main.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_mark.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_mark.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_parseopt.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_parseopt.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_pluginmanager.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_pluginmanager.py` for its `UsageError` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/python.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/_pytest/python.py\", \"UsageError\"]]",
   "v1": [
    2115701,
    122550
   ],
   "v2": [
    1059076,
    61275
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
     "src/_pytest/python.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/pytest/__init__.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/pytest/__init__.py\", \"UsageError\"]]",
   "v1": [
    2115701,
    122550
   ],
   "v2": [
    1059076,
    61275
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
     "src/pytest/__init__.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/acceptance_test.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"UsageError\"]]",
   "v1": [
    2115701,
    122550
   ],
   "v2": [
    1059076,
    61275
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
     "testing/acceptance_test.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/python/collect.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/python/collect.py\", \"UsageError\"]]",
   "v1": [
    2115701,
    122550
   ],
   "v2": [
    1059076,
    61275
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
     "testing/python/collect.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_config.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_config.py\", \"UsageError\"]]",
   "v1": [
    2115701,
    122550
   ],
   "v2": [
    1059076,
    61275
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
     "testing/test_config.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_findpaths.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_findpaths.py\", \"UsageError\"]]",
   "v1": [
    2115701,
    122550
   ],
   "v2": [
    1059076,
    61275
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
     "testing/test_findpaths.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_main.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_main.py\", \"UsageError\"]]",
   "v1": [
    2115701,
    122550
   ],
   "v2": [
    1059076,
    61275
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
     "testing/test_main.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_mark.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_mark.py\", \"UsageError\"]]",
   "v1": [
    2115701,
    122550
   ],
   "v2": [
    1059076,
    61275
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
     "testing/test_mark.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_parseopt.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_parseopt.py\", \"UsageError\"]]",
   "v1": [
    2115701,
    122550
   ],
   "v2": [
    1059076,
    61275
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
     "testing/test_parseopt.py",
     "UsageError"
    ]
   ]
  },
  {
   
```
</details>

## Step 24

In `src/_pytest/python.py`, `UsageError` has exactly one binding: line 56 imports it as `UsageError` from `_pytest.config`. It uses dynamic namespace tricks, no `__all__`.

Candidate modules so far: 19; statements confirmed: 9, ruled out: 0, modules with no such import: 1, pending: 9. import coverage complete; star coverage complete.

Still to settle: outline `src/pytest/__init__.py` for its `UsageError` imports; outline `testing/acceptance_test.py` for its `UsageError` imports; outline `testing/python/collect.py` for its `UsageError` imports; outline `testing/test_config.py` for its `UsageError` imports; and 5 more.

Next: outline `src/pytest/__init__.py` filtered to `UsageError`, because `src/pytest/__init__.py` had a matching line (step 5); its outline names every `UsageError` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `testing/acceptance_test.py` filtered to `UsageError`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `testing/acceptance_test.py` filtered to `UsageError`; cap: outline `testing/acceptance_test.py` filtered to `UsageError`.

**Call:** `symbols('src/pytest/__init__.py', 'UsageError')`

**Response**: outcome `ok`

```
module src/pytest/__init__.py lines=191 dynamic=no all=static@100
22 from UsageError <- _pytest.config UsageError
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/pytest/__init__.py",
    "UsageError"
   ],
   "desc": "outline `src/pytest/__init__.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "UsageError"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/python/collect.py",
    "UsageError"
   ],
   "desc": "outline `testing/python/collect.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_config.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_config.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_findpaths.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_main.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_mark.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_mark.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_parseopt.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_parseopt.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_pluginmanager.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_pluginmanager.py` for its `UsageError` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/pytest/__init__.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/pytest/__init__.py\", \"UsageError\"]]",
   "v1": [
    317396,
    20425
   ],
   "v2": [
    635609,
    40850
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
     "src/pytest/__init__.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/acceptance_test.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"UsageError\"]]",
   "v1": [
    317396,
    20425
   ],
   "v2": [
    635609,
    40850
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
     "testing/acceptance_test.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/python/collect.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/python/collect.py\", \"UsageError\"]]",
   "v1": [
    317396,
    20425
   ],
   "v2": [
    635609,
    40850
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
     "testing/python/collect.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_config.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_config.py\", \"UsageError\"]]",
   "v1": [
    317396,
    20425
   ],
   "v2": [
    635609,
    40850
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
     "testing/test_config.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_findpaths.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_findpaths.py\", \"UsageError\"]]",
   "v1": [
    317396,
    20425
   ],
   "v2": [
    635609,
    40850
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
     "testing/test_findpaths.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_main.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_main.py\", \"UsageError\"]]",
   "v1": [
    317396,
    20425
   ],
   "v2": [
    635609,
    40850
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
     "testing/test_main.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_mark.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_mark.py\", \"UsageError\"]]",
   "v1": [
    317396,
    20425
   ],
   "v2": [
    635609,
    40850
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
     "testing/test_mark.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_parseopt.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_parseopt.py\", \"UsageError\"]]",
   "v1": [
    317396,
    20425
   ],
   "v2": [
    635609,
    40850
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
     "testing/test_parseopt.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_pluginmanager.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_pluginmanager.py\", \"UsageError\"]]",
   "v1": [
    317396,
    20425
   ],
   "v2": [
    635609,
    40850
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
     "testing/test_pluginmanager.py",
     "UsageError"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/pytest/__init__.py', 'UsageError')",
  "key": "[\"symbols\", [\"src/pytest/__init__.py\", \"UsageError\"]]",
  "provenance": "`src/pytest/__init__.py` had
```
</details>

## Step 25

In `src/pytest/__init__.py`, `UsageError` has exactly one binding: line 22 imports it as `UsageError` from `_pytest.config`. No dynamic namespace tricks, a literal `__all__` at line 100.

Candidate modules so far: 19; statements confirmed: 10, ruled out: 0, modules with no such import: 1, pending: 8. import coverage complete; star coverage complete.

Still to settle: outline `testing/acceptance_test.py` for its `UsageError` imports; outline `testing/python/collect.py` for its `UsageError` imports; outline `testing/test_config.py` for its `UsageError` imports; outline `testing/test_findpaths.py` for its `UsageError` imports; and 4 more.

Next: outline `testing/acceptance_test.py` filtered to `UsageError`, because `testing/acceptance_test.py` had a matching line (step 5); its outline names every `UsageError` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `testing/python/collect.py` filtered to `UsageError`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `testing/python/collect.py` filtered to `UsageError`; cap: outline `testing/python/collect.py` filtered to `UsageError`.

**Call:** `symbols('testing/acceptance_test.py', 'UsageError')`

**Response**: outcome `ok`

```
module testing/acceptance_test.py lines=1770 dynamic=no all=none
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "UsageError"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/python/collect.py",
    "UsageError"
   ],
   "desc": "outline `testing/python/collect.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_config.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_config.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_findpaths.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_main.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_mark.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_mark.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_parseopt.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_parseopt.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_pluginmanager.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_pluginmanager.py` for its `UsageError` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('testing/acceptance_test.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"UsageError\"]]",
   "v1": [
    1693051,
    122550
   ],
   "v2": [
    847751,
    61275
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
     "testing/acceptance_test.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/python/collect.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/python/collect.py\", \"UsageError\"]]",
   "v1": [
    1693051,
    122550
   ],
   "v2": [
    847751,
    61275
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
     "testing/python/collect.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_config.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_config.py\", \"UsageError\"]]",
   "v1": [
    1693051,
    122550
   ],
   "v2": [
    847751,
    61275
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
     "testing/test_config.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_findpaths.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_findpaths.py\", \"UsageError\"]]",
   "v1": [
    1693051,
    122550
   ],
   "v2": [
    847751,
    61275
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
     "testing/test_findpaths.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_main.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_main.py\", \"UsageError\"]]",
   "v1": [
    1693051,
    122550
   ],
   "v2": [
    847751,
    61275
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
     "testing/test_main.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_mark.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_mark.py\", \"UsageError\"]]",
   "v1": [
    1693051,
    122550
   ],
   "v2": [
    847751,
    61275
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
     "testing/test_mark.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_parseopt.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_parseopt.py\", \"UsageError\"]]",
   "v1": [
    1693051,
    122550
   ],
   "v2": [
    847751,
    61275
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
     "testing/test_parseopt.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_pluginmanager.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_pluginmanager.py\", \"UsageError\"]]",
   "v1": [
    1693051,
    122550
   ],
   "v2": [
    847751,
    61275
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
     "testing/test_pluginmanager.py",
     "UsageError"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('testing/acceptance_test.py', 'UsageError')",
  "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"UsageError\"]]",
  "provenance": "`testing/acceptance_test.py` had a matching line (step 5); its outline names every `UsageError` import exactly",
  "v2": [
   847751,
   61275
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
  "ok": "[\"symbols\", [\"testing/python/collect.py\", \"UsageError\"]]",
  "cap": "[\"symbols\", [\"testing/python/collect.py\", \"UsageError\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"testing/acceptance_test.py\", \"UsageError\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 25,
   "path": "testing/acceptance_test.py",
   "filter": "UsageError",
   "h
```
</details>

## Step 26

`testing/acceptance_test.py` binds no `UsageError` at module level; no star imports; no `__all__`; no dynamic namespace tricks.

Candidate modules so far: 19; statements confirmed: 10, ruled out: 0, modules with no such import: 2, pending: 7. import coverage complete; star coverage complete.

Outstanding: outline `testing/python/collect.py` for its `UsageError` imports; outline `testing/test_config.py` for its `UsageError` imports; outline `testing/test_findpaths.py` for its `UsageError` imports; outline `testing/test_main.py` for its `UsageError` imports; and 3 more.

Next: outline `testing/python/collect.py` filtered to `UsageError`, because `testing/python/collect.py` had a matching line (step 5); its outline names every `UsageError` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `testing/test_config.py` filtered to `UsageError`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `testing/test_config.py` filtered to `UsageError`; cap: outline `testing/test_config.py` filtered to `UsageError`.

**Call:** `symbols('testing/python/collect.py', 'UsageError')`

**Response**: outcome `ok`

```
module testing/python/collect.py lines=1752 dynamic=no all=none
11 from UsageError <- _pytest.config.exceptions UsageError
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/python/collect.py",
    "UsageError"
   ],
   "desc": "outline `testing/python/collect.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_config.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_config.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_findpaths.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_main.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_mark.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_mark.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_parseopt.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_parseopt.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_pluginmanager.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_pluginmanager.py` for its `UsageError` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('testing/python/collect.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/python/collect.py\", \"UsageError\"]]",
   "v1": [
    740863,
    61275
   ],
   "v2": [
    1484177,
    122550
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
     "testing/python/collect.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_config.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_config.py\", \"UsageError\"]]",
   "v1": [
    740863,
    61275
   ],
   "v2": [
    1484177,
    122550
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
     "testing/test_config.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_findpaths.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_findpaths.py\", \"UsageError\"]]",
   "v1": [
    740863,
    61275
   ],
   "v2": [
    1484177,
    122550
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
     "testing/test_findpaths.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_main.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_main.py\", \"UsageError\"]]",
   "v1": [
    740863,
    61275
   ],
   "v2": [
    1484177,
    122550
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
     "testing/test_main.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_mark.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_mark.py\", \"UsageError\"]]",
   "v1": [
    740863,
    61275
   ],
   "v2": [
    1484177,
    122550
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
     "testing/test_mark.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_parseopt.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_parseopt.py\", \"UsageError\"]]",
   "v1": [
    740863,
    61275
   ],
   "v2": [
    1484177,
    122550
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
     "testing/test_parseopt.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_pluginmanager.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_pluginmanager.py\", \"UsageError\"]]",
   "v1": [
    740863,
    61275
   ],
   "v2": [
    1484177,
    122550
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
     "testing/test_pluginmanager.py",
     "UsageError"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('testing/python/collect.py', 'UsageError')",
  "key": "[\"symbols\", [\"testing/python/collect.py\", \"UsageError\"]]",
  "provenance": "`testing/python/collect.py` had a matching line (step 5); its outline names every `UsageError` import exactly",
  "v2": [
   1484177,
   122550
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
  "ok": "[\"symbols\", [\"testing/test_config.py\", \"UsageError\"]]",
  "cap": "[\"symbols\", [\"testing/test_config.py\", \"UsageError\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"testing/python/collect.py\", \"UsageError\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 26,
   "path": "testing/python/collect.py",
   "filter": "UsageError",
   "header": {
    "lines": 1752,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "testing/python/collect.py",
     "name": "UsageError",
     "line": 11,
     "kind": "from",
     "src": "_pytest.config.exceptions",
     "src_name": "UsageError",
     "conditional": false,
     "col": 0
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "src/_pytest/_io/terminalwriter.py",
    0,
    "none",
    "no import of the name in this module"
   ],
   [
    "src/_pytest/config/__init__.py",
    51,
    "in",
    "`.exceptions` resolves `UsageError` to the target"
   ],
   [

```
</details>

## Step 27

In `testing/python/collect.py`, `UsageError` has exactly one binding: line 11 imports it as `UsageError` from `_pytest.config.exceptions`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 19; statements confirmed: 11, ruled out: 0, modules with no such import: 2, pending: 6. import coverage complete; star coverage complete.

Outstanding: outline `testing/test_config.py` for its `UsageError` imports; outline `testing/test_findpaths.py` for its `UsageError` imports; outline `testing/test_main.py` for its `UsageError` imports; outline `testing/test_mark.py` for its `UsageError` imports; and 2 more.

Next: outline `testing/test_config.py` filtered to `UsageError`, because `testing/test_config.py` had a matching line (step 5); its outline names every `UsageError` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `testing/test_findpaths.py` filtered to `UsageError`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `testing/test_findpaths.py` filtered to `UsageError`; cap: outline `testing/test_findpaths.py` filtered to `UsageError`.

**Call:** `symbols('testing/test_config.py', 'UsageError')`

**Response**: outcome `ok`

```
module testing/test_config.py lines=3509 dynamic=no all=none
28 from UsageError <- _pytest.config.exceptions UsageError
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_config.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_config.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_findpaths.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_main.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_mark.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_mark.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_parseopt.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_parseopt.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_pluginmanager.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_pluginmanager.py` for its `UsageError` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('testing/test_config.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_config.py\", \"UsageError\"]]",
   "v1": [
    423467,
    40850
   ],
   "v2": [
    212142,
    20425
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
     "testing/test_config.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_findpaths.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_findpaths.py\", \"UsageError\"]]",
   "v1": [
    423467,
    40850
   ],
   "v2": [
    212142,
    20425
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
     "testing/test_findpaths.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_main.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_main.py\", \"UsageError\"]]",
   "v1": [
    423467,
    40850
   ],
   "v2": [
    212142,
    20425
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
     "testing/test_main.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_mark.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_mark.py\", \"UsageError\"]]",
   "v1": [
    423467,
    40850
   ],
   "v2": [
    212142,
    20425
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
     "testing/test_mark.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_parseopt.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_parseopt.py\", \"UsageError\"]]",
   "v1": [
    423467,
    40850
   ],
   "v2": [
    212142,
    20425
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
     "testing/test_parseopt.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_pluginmanager.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_pluginmanager.py\", \"UsageError\"]]",
   "v1": [
    423467,
    40850
   ],
   "v2": [
    212142,
    20425
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
     "testing/test_pluginmanager.py",
     "UsageError"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('testing/test_config.py', 'UsageError')",
  "key": "[\"symbols\", [\"testing/test_config.py\", \"UsageError\"]]",
  "provenance": "`testing/test_config.py` had a matching line (step 5); its outline names every `UsageError` import exactly",
  "v2": [
   212142,
   20425
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
  "ok": "[\"symbols\", [\"testing/test_findpaths.py\", \"UsageError\"]]",
  "cap": "[\"symbols\", [\"testing/test_findpaths.py\", \"UsageError\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"testing/test_config.py\", \"UsageError\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 27,
   "path": "testing/test_config.py",
   "filter": "UsageError",
   "header": {
    "lines": 3509,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "testing/test_config.py",
     "name": "UsageError",
     "line": 28,
     "kind": "from",
     "src": "_pytest.config.exceptions",
     "src_name": "UsageError",
     "conditional": false,
     "col": 0
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "src/_pytest/_io/terminalwriter.py",
    0,
    "none",
    "no import of the name in this module"
   ],
   [
    "src/_pytest/config/__init__.py",
    51,
    "in",
    "`.exceptions` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/config/argparsing.py",
    22,
    "in",
    "`.exceptions` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/config/findpaths.py",
    16,
    "in",
    "`.exceptions` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/debugging.py",
    24,
    "in",
    "`_pytest.config.exceptions` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/logging.py",
    35,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/main.py",
    34,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/mark/__init__.py",
    27,
    "in",
    "`_py
```
</details>

## Step 28

In `testing/test_config.py`, `UsageError` has exactly one binding: line 28 imports it as `UsageError` from `_pytest.config.exceptions`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 19; statements confirmed: 12, ruled out: 0, modules with no such import: 2, pending: 5. import coverage complete; star coverage complete.

Open: outline `testing/test_findpaths.py` for its `UsageError` imports; outline `testing/test_main.py` for its `UsageError` imports; outline `testing/test_mark.py` for its `UsageError` imports; outline `testing/test_parseopt.py` for its `UsageError` imports; and 1 more.

Next: outline `testing/test_findpaths.py` filtered to `UsageError`, because `testing/test_findpaths.py` had a matching line (step 5); its outline names every `UsageError` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `testing/test_main.py` filtered to `UsageError`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `testing/test_main.py` filtered to `UsageError`; cap: outline `testing/test_main.py` filtered to `UsageError`.

**Call:** `symbols('testing/test_findpaths.py', 'UsageError')`

**Response**: outcome `ok`

```
module testing/test_findpaths.py lines=267 dynamic=no all=none
8 from UsageError <- _pytest.config UsageError
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_findpaths.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_findpaths.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_main.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_mark.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_mark.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_parseopt.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_parseopt.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_pluginmanager.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_pluginmanager.py` for its `UsageError` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('testing/test_findpaths.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_findpaths.py\", \"UsageError\"]]",
   "v1": [
    529538,
    61275
   ],
   "v2": [
    1061527,
    122550
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
     "testing/test_findpaths.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_main.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_main.py\", \"UsageError\"]]",
   "v1": [
    529538,
    61275
   ],
   "v2": [
    1061527,
    122550
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
     "testing/test_main.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_mark.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_mark.py\", \"UsageError\"]]",
   "v1": [
    529538,
    61275
   ],
   "v2": [
    1061527,
    122550
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
     "testing/test_mark.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_parseopt.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_parseopt.py\", \"UsageError\"]]",
   "v1": [
    529538,
    61275
   ],
   "v2": [
    1061527,
    122550
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
     "testing/test_parseopt.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_pluginmanager.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_pluginmanager.py\", \"UsageError\"]]",
   "v1": [
    529538,
    61275
   ],
   "v2": [
    1061527,
    122550
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
     "testing/test_pluginmanager.py",
     "UsageError"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('testing/test_findpaths.py', 'UsageError')",
  "key": "[\"symbols\", [\"testing/test_findpaths.py\", \"UsageError\"]]",
  "provenance": "`testing/test_findpaths.py` had a matching line (step 5); its outline names every `UsageError` import exactly",
  "v2": [
   1061527,
   122550
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
  "ok": "[\"symbols\", [\"testing/test_main.py\", \"UsageError\"]]",
  "cap": "[\"symbols\", [\"testing/test_main.py\", \"UsageError\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"testing/test_findpaths.py\", \"UsageError\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 28,
   "path": "testing/test_findpaths.py",
   "filter": "UsageError",
   "header": {
    "lines": 267,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "testing/test_findpaths.py",
     "name": "UsageError",
     "line": 8,
     "kind": "from",
     "src": "_pytest.config",
     "src_name": "UsageError",
     "conditional": false,
     "col": 0
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "src/_pytest/_io/terminalwriter.py",
    0,
    "none",
    "no import of the name in this module"
   ],
   [
    "src/_pytest/config/__init__.py",
    51,
    "in",
    "`.exceptions` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/config/argparsing.py",
    22,
    "in",
    "`.exceptions` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/config/findpaths.py",
    16,
    "in",
    "`.exceptions` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/debugging.py",
    24,
    "in",
    "`_pytest.config.exceptions` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/logging.py",
    35,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/main.py",
    34,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/mark/__init__.py",
    27,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/python.py",
    56,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "src/pytest/__init__.py",
    22,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "testing/acceptance_test.py",
    0,
    "none",
    "no import of the name in this module"
   ],
   [
    "testing/python/collect.py",
    11,
    "in",
    "`_pytest.config.exceptions` resolves `UsageError` to the target"
   ],
   [
    "testing/test_config.py",
    28,
    "in",
    "`_pytest.config.exceptions` resolves `
```
</details>

## Step 29

In `testing/test_findpaths.py`, `UsageError` has exactly one binding: line 8 imports it as `UsageError` from `_pytest.config`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 19; statements confirmed: 13, ruled out: 0, modules with no such import: 2, pending: 4. import coverage complete; star coverage complete.

Still to settle: outline `testing/test_main.py` for its `UsageError` imports; outline `testing/test_mark.py` for its `UsageError` imports; outline `testing/test_parseopt.py` for its `UsageError` imports; outline `testing/test_pluginmanager.py` for its `UsageError` imports.

Next: outline `testing/test_main.py` filtered to `UsageError`, because `testing/test_main.py` had a matching line (step 5); its outline names every `UsageError` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `testing/test_mark.py` filtered to `UsageError`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `testing/test_mark.py` filtered to `UsageError`; cap: outline `testing/test_mark.py` filtered to `UsageError`.

**Call:** `symbols('testing/test_main.py', 'UsageError')`

**Response**: outcome `ok`

```
module testing/test_main.py lines=373 dynamic=no all=none
10 from UsageError <- _pytest.config UsageError
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_main.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_main.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_mark.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_mark.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_parseopt.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_parseopt.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_pluginmanager.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_pluginmanager.py` for its `UsageError` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('testing/test_main.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_main.py\", \"UsageError\"]]",
   "v1": [
    847751,
    122550
   ],
   "v2": [
    425101,
    61275
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
     "testing/test_main.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_mark.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_mark.py\", \"UsageError\"]]",
   "v1": [
    847751,
    122550
   ],
   "v2": [
    425101,
    61275
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
     "testing/test_mark.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_parseopt.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_parseopt.py\", \"UsageError\"]]",
   "v1": [
    847751,
    122550
   ],
   "v2": [
    425101,
    61275
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
     "testing/test_parseopt.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_pluginmanager.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_pluginmanager.py\", \"UsageError\"]]",
   "v1": [
    847751,
    122550
   ],
   "v2": [
    425101,
    61275
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
     "testing/test_pluginmanager.py",
     "UsageError"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('testing/test_main.py', 'UsageError')",
  "key": "[\"symbols\", [\"testing/test_main.py\", \"UsageError\"]]",
  "provenance": "`testing/test_main.py` had a matching line (step 5); its outline names every `UsageError` import exactly",
  "v2": [
   425101,
   61275
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
  "ok": "[\"symbols\", [\"testing/test_mark.py\", \"UsageError\"]]",
  "cap": "[\"symbols\", [\"testing/test_mark.py\", \"UsageError\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"testing/test_main.py\", \"UsageError\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 29,
   "path": "testing/test_main.py",
   "filter": "UsageError",
   "header": {
    "lines": 373,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "testing/test_main.py",
     "name": "UsageError",
     "line": 10,
     "kind": "from",
     "src": "_pytest.config",
     "src_name": "UsageError",
     "conditional": false,
     "col": 0
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "src/_pytest/_io/terminalwriter.py",
    0,
    "none",
    "no import of the name in this module"
   ],
   [
    "src/_pytest/config/__init__.py",
    51,
    "in",
    "`.exceptions` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/config/argparsing.py",
    22,
    "in",
    "`.exceptions` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/config/findpaths.py",
    16,
    "in",
    "`.exceptions` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/debugging.py",
    24,
    "in",
    "`_pytest.config.exceptions` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/logging.py",
    35,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/main.py",
    34,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/mark/__init__.py",
    27,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/python.py",
    56,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "src/pytest/__init__.py",
    22,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "testing/acceptance_test.py",
    0,
    "none",
    "no import of the name in this module"
   ],
   [
    "testing/python/collect.py",
    11,
    "in",
    "`_pytest.config.exceptions` resolves `UsageError` to the target"
   ],
   [
    "testing/test_config.py",
    28,
    "in",
    "`_pytest.config.exceptions` resolves `UsageError` to the target"
   ],
   [
    "testing/test_findpaths.py",
    8,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "testing/test_main.py",
    10,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "testing/test_mark.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "testing/test_parseopt.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "testing/test_pluginmanager.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "testing/test_session.py",
    5,
    "in",
    "`_pytest.config.exceptions` resolves `UsageError` to the target"
   ]
  ],
  "unc
```
</details>

## Step 30

In `testing/test_main.py`, `UsageError` has exactly one binding: line 10 imports it as `UsageError` from `_pytest.config`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 19; statements confirmed: 14, ruled out: 0, modules with no such import: 2, pending: 3. import coverage complete; star coverage complete.

Open: outline `testing/test_mark.py` for its `UsageError` imports; outline `testing/test_parseopt.py` for its `UsageError` imports; outline `testing/test_pluginmanager.py` for its `UsageError` imports.

Next: outline `testing/test_mark.py` filtered to `UsageError`, because `testing/test_mark.py` had a matching line (step 5); its outline names every `UsageError` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `testing/test_parseopt.py` filtered to `UsageError`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `testing/test_parseopt.py` filtered to `UsageError`; cap: outline `testing/test_parseopt.py` filtered to `UsageError`.

**Call:** `symbols('testing/test_mark.py', 'UsageError')`

**Response**: outcome `ok`

```
module testing/test_mark.py lines=1520 dynamic=no all=none
13 from UsageError <- _pytest.config UsageError
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_mark.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_mark.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_parseopt.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_parseopt.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_pluginmanager.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_pluginmanager.py` for its `UsageError` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('testing/test_mark.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_mark.py\", \"UsageError\"]]",
   "v1": [
    106071,
    20425
   ],
   "v2": [
    212959,
    40850
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
     "testing/test_mark.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_parseopt.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_parseopt.py\", \"UsageError\"]]",
   "v1": [
    106071,
    20425
   ],
   "v2": [
    212959,
    40850
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
     "testing/test_parseopt.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_pluginmanager.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_pluginmanager.py\", \"UsageError\"]]",
   "v1": [
    106071,
    20425
   ],
   "v2": [
    212959,
    40850
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
     "testing/test_pluginmanager.py",
     "UsageError"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('testing/test_mark.py', 'UsageError')",
  "key": "[\"symbols\", [\"testing/test_mark.py\", \"UsageError\"]]",
  "provenance": "`testing/test_mark.py` had a matching line (step 5); its outline names every `UsageError` import exactly",
  "v2": [
   212959,
   40850
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
  "ok": "[\"symbols\", [\"testing/test_parseopt.py\", \"UsageError\"]]",
  "cap": "[\"symbols\", [\"testing/test_parseopt.py\", \"UsageError\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"testing/test_mark.py\", \"UsageError\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 30,
   "path": "testing/test_mark.py",
   "filter": "UsageError",
   "header": {
    "lines": 1520,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "testing/test_mark.py",
     "name": "UsageError",
     "line": 13,
     "kind": "from",
     "src": "_pytest.config",
     "src_name": "UsageError",
     "conditional": false,
     "col": 0
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "src/_pytest/_io/terminalwriter.py",
    0,
    "none",
    "no import of the name in this module"
   ],
   [
    "src/_pytest/config/__init__.py",
    51,
    "in",
    "`.exceptions` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/config/argparsing.py",
    22,
    "in",
    "`.exceptions` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/config/findpaths.py",
    16,
    "in",
    "`.exceptions` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/debugging.py",
    24,
    "in",
    "`_pytest.config.exceptions` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/logging.py",
    35,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/main.py",
    34,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/mark/__init__.py",
    27,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/python.py",
    56,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "src/pytest/__init__.py",
    22,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "testing/acceptance_test.py",
    0,
    "none",
    "no import of the name in this module"
   ],
   [
    "testing/python/collect.py",
    11,
    "in",
    "`_pytest.config.exceptions` resolves `UsageError` to the target"
   ],
   [
    "testing/test_config.py",
    28,
    "in",
    "`_pytest.config.exceptions` resolves `UsageError` to the target"
   ],
   [
    "testing/test_findpaths.py",
    8,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "testing/test_main.py",
    10,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "testing/test_mark.py",
    13,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "testing/test_parseopt.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "testing/test_pluginmanager.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "testing/test_session.py",
    5,
    "in",
    "`_pytest.config.exceptions` resolves `UsageError` to the target"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  }
 }
}
```
</details>

## Step 31

In `testing/test_mark.py`, `UsageError` has exactly one binding: line 13 imports it as `UsageError` from `_pytest.config`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 19; statements confirmed: 15, ruled out: 0, modules with no such import: 2, pending: 2. import coverage complete; star coverage complete.

Outstanding: outline `testing/test_parseopt.py` for its `UsageError` imports; outline `testing/test_pluginmanager.py` for its `UsageError` imports.

Next: outline `testing/test_parseopt.py` filtered to `UsageError`, because `testing/test_parseopt.py` had a matching line (step 5); its outline names every `UsageError` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `testing/test_pluginmanager.py` filtered to `UsageError`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `testing/test_pluginmanager.py` filtered to `UsageError`; cap: outline `testing/test_pluginmanager.py` filtered to `UsageError`.

**Call:** `symbols('testing/test_parseopt.py', 'UsageError')`

**Response**: outcome `ok`

```
module testing/test_parseopt.py lines=397 dynamic=no all=none
13 from UsageError <- _pytest.config.exceptions UsageError
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_parseopt.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_parseopt.py` for its `UsageError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_pluginmanager.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_pluginmanager.py` for its `UsageError` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('testing/test_parseopt.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_parseopt.py\", \"UsageError\"]]",
   "v1": [
    425101,
    122550
   ],
   "v2": [
    213776,
    61275
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
     "testing/test_parseopt.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_pluginmanager.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_pluginmanager.py\", \"UsageError\"]]",
   "v1": [
    425101,
    122550
   ],
   "v2": [
    213776,
    61275
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
     "testing/test_pluginmanager.py",
     "UsageError"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('testing/test_parseopt.py', 'UsageError')",
  "key": "[\"symbols\", [\"testing/test_parseopt.py\", \"UsageError\"]]",
  "provenance": "`testing/test_parseopt.py` had a matching line (step 5); its outline names every `UsageError` import exactly",
  "v2": [
   213776,
   61275
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
  "ok": "[\"symbols\", [\"testing/test_pluginmanager.py\", \"UsageError\"]]",
  "cap": "[\"symbols\", [\"testing/test_pluginmanager.py\", \"UsageError\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"testing/test_parseopt.py\", \"UsageError\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 31,
   "path": "testing/test_parseopt.py",
   "filter": "UsageError",
   "header": {
    "lines": 397,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "testing/test_parseopt.py",
     "name": "UsageError",
     "line": 13,
     "kind": "from",
     "src": "_pytest.config.exceptions",
     "src_name": "UsageError",
     "conditional": false,
     "col": 0
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "src/_pytest/_io/terminalwriter.py",
    0,
    "none",
    "no import of the name in this module"
   ],
   [
    "src/_pytest/config/__init__.py",
    51,
    "in",
    "`.exceptions` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/config/argparsing.py",
    22,
    "in",
    "`.exceptions` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/config/findpaths.py",
    16,
    "in",
    "`.exceptions` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/debugging.py",
    24,
    "in",
    "`_pytest.config.exceptions` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/logging.py",
    35,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/main.py",
    34,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/mark/__init__.py",
    27,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/python.py",
    56,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "src/pytest/__init__.py",
    22,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "testing/acceptance_test.py",
    0,
    "none",
    "no import of the name in this module"
   ],
   [
    "testing/python/collect.py",
    11,
    "in",
    "`_pytest.config.exceptions` resolves `UsageError` to the target"
   ],
   [
    "testing/test_config.py",
    28,
    "in",
    "`_pytest.config.exceptions` resolves `UsageError` to the target"
   ],
   [
    "testing/test_findpaths.py",
    8,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "testing/test_main.py",
    10,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "testing/test_mark.py",
    13,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "testing/test_parseopt.py",
    13,
    "in",
    "`_pytest.config.exceptions` resolves `UsageError` to the target"
   ],
   [
    "testing/test_pluginmanager.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "testing/test_session.py",
    5,
    "in",
    "`_pytest.config.exceptions` resolves `UsageError` to the target"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  }
 }
}
```
</details>

## Step 32

In `testing/test_parseopt.py`, `UsageError` has exactly one binding: line 13 imports it as `UsageError` from `_pytest.config.exceptions`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 19; statements confirmed: 16, ruled out: 0, modules with no such import: 2, pending: 1. import coverage complete; star coverage complete.

Open: outline `testing/test_pluginmanager.py` for its `UsageError` imports.

Next: outline `testing/test_pluginmanager.py` filtered to `UsageError`, because `testing/test_pluginmanager.py` had a matching line (step 5); its outline names every `UsageError` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). Plan by outcome: ok: resolve the sources its import statements name; cap: work the items it opens.

**Call:** `symbols('testing/test_pluginmanager.py', 'UsageError')`

**Response**: outcome `ok`

```
module testing/test_pluginmanager.py lines=581 dynamic=no all=none
16 from UsageError <- _pytest.config.exceptions UsageError
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_pluginmanager.py",
    "UsageError"
   ],
   "desc": "outline `testing/test_pluginmanager.py` for its `UsageError` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('testing/test_pluginmanager.py', 'UsageError')",
   "key": "[\"symbols\", [\"testing/test_pluginmanager.py\", \"UsageError\"]]",
   "v1": [
    106888,
    61275
   ],
   "v2": [
    106888,
    61275
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
     "testing/test_pluginmanager.py",
     "UsageError"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('testing/test_pluginmanager.py', 'UsageError')",
  "key": "[\"symbols\", [\"testing/test_pluginmanager.py\", \"UsageError\"]]",
  "provenance": "`testing/test_pluginmanager.py` had a matching line (step 5); its outline names every `UsageError` import exactly",
  "v2": [
   106888,
   61275
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
  "ok": "continue",
  "cap": "continue"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"testing/test_pluginmanager.py\", \"UsageError\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 32,
   "path": "testing/test_pluginmanager.py",
   "filter": "UsageError",
   "header": {
    "lines": 581,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "testing/test_pluginmanager.py",
     "name": "UsageError",
     "line": 16,
     "kind": "from",
     "src": "_pytest.config.exceptions",
     "src_name": "UsageError",
     "conditional": false,
     "col": 0
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "src/_pytest/_io/terminalwriter.py",
    0,
    "none",
    "no import of the name in this module"
   ],
   [
    "src/_pytest/config/__init__.py",
    51,
    "in",
    "`.exceptions` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/config/argparsing.py",
    22,
    "in",
    "`.exceptions` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/config/findpaths.py",
    16,
    "in",
    "`.exceptions` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/debugging.py",
    24,
    "in",
    "`_pytest.config.exceptions` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/logging.py",
    35,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/main.py",
    34,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/mark/__init__.py",
    27,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "src/_pytest/python.py",
    56,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "src/pytest/__init__.py",
    22,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "testing/acceptance_test.py",
    0,
    "none",
    "no import of the name in this module"
   ],
   [
    "testing/python/collect.py",
    11,
    "in",
    "`_pytest.config.exceptions` resolves `UsageError` to the target"
   ],
   [
    "testing/test_config.py",
    28,
    "in",
    "`_pytest.config.exceptions` resolves `UsageError` to the target"
   ],
   [
    "testing/test_findpaths.py",
    8,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "testing/test_main.py",
    10,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "testing/test_mark.py",
    13,
    "in",
    "`_pytest.config` resolves `UsageError` to the target"
   ],
   [
    "testing/test_parseopt.py",
    13,
    "in",
    "`_pytest.config.exceptions` resolves `UsageError` to the target"
   ],
   [
    "testing/test_pluginmanager.py",
    16,
    "in",
    "`_pytest.config.exceptions` resolves `UsageError` to the target"
   ],
   [
    "testing/test_session.py",
    5,
    "in",
    "`_pytest.config.exceptions` resolves `UsageError` to the target"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  }
 }
}
```
</details>

## Final

Certificate complete. 17 import statements import this definition: `src/_pytest/config/__init__.py:51`, `src/_pytest/config/argparsing.py:22`, `src/_pytest/config/findpaths.py:16`, `src/_pytest/debugging.py:24`, `src/_pytest/logging.py:35`, `src/_pytest/main.py:34`, `src/_pytest/mark/__init__.py:27`, `src/_pytest/python.py:56`, `src/pytest/__init__.py:22`, `testing/python/collect.py:11`, `testing/test_config.py:28`, `testing/test_findpaths.py:8` and 5 more. In hindsight every one of the 32 calls was needed for the certificate.

**Answer:** `{"target": {"kind": "def", "path": "src/_pytest/config/exceptions.py", "line": 7, "name": "UsageError", "detail": "class"}, "text": "src/_pytest/config/exceptions.py:7", "statements": ["src/_pytest/config/__init__.py:51", "src/_pytest/config/argparsing.py:22", "src/_pytest/config/findpaths.py:16", "src/_pytest/debugging.py:24", "src/_pytest/logging.py:35", "src/_pytest/main.py:34", "src/_pytest/mark/__init__.py:27", "src/_pytest/python.py:56", "src/pytest/__init__.py:22", "testing/python/collect.py:11", "testing/test_config.py:28", "testing/test_findpaths.py:8", "testing/test_main.py:10", "testing/test_mark.py:13", "testing/test_parseopt.py:13", "testing/test_pluginmanager.py:16", "testing/test_session.py:5"], "count": 17}`  
**Stopped:** certificate after 32 calls