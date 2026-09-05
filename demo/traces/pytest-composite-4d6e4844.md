# pytest-composite-4d6e4844

**Repository:** pytest  
**Family:** composite  
**Seed:** 0, prior 0140c5bd99319f8c

## Task

In `src/_pytest/_code/code.py`, line 47 imports `check_ispytest` from `_pytest.deprecated`. Under the declared semantics, which definition does the module-level name `check_ispytest` bound by this statement resolve to? Answer with `path:line`. Then list every module-level import statement in the snapshot that imports that definition (from-imports naming it, directly or with `as`, and star imports of modules that export it), as `path:line` entries.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

Nothing seen yet beyond the task text.

Chain: `src/_pytest/_code/code.py` is not yet closed for `check_ispytest`.

Outstanding: close the namespace of `src/_pytest/_code/code.py` for `check_ispytest`.

Next: outline `src/_pytest/_code/code.py`, because module `src/_pytest/_code/code.py` (task). I expect: a definition there ends the chain (about 85%); a capped outline means filtering by name (about 10%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `src/_pytest/_code/code.py` filtered to `check_ispytest`, is expected to open more follow-up work. Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done; cap: outline `src/_pytest/_code/code.py` filtered to `check_ispytest`.

**Call:** `symbols('src/_pytest/_code/code.py')`

**Response** (capped): outcome `cap`

```
module src/_pytest/_code/code.py lines=1682 dynamic=no all=none
2 from annotations <- __future__ annotations
4 import ast <- ast
5 from Callable <- collections.abc Callable
6 from Iterable <- collections.abc Iterable
7 from Mapping <- collections.abc Mapping
8 from Sequence <- collections.abc Sequence
9 import dataclasses <- dataclasses
10 import inspect <- inspect
11 from StringIO <- io StringIO
12 import os <- os
13 from Path <- pathlib Path
14 import re <- re
15 import sys <- sys
16 from extract_tb <- traceback extract_tb
17 from format_exception <- traceback format_exception
18 from format_exception_only <- traceback format_exception_only
19 from FrameSummary <- traceback FrameSummary
20 from StackSummary <- traceback StackSummary
21 from TracebackException <- traceback TracebackException
22 from CodeType <- types CodeType
23 from FrameType <- types FrameType
24 from TracebackType <- types TracebackType
25 from Any <- typing Any
26 from ClassVar <- typing ClassVar
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
    "src/_pytest/_code/code.py",
    "check_ispytest"
   ],
   "desc": "close the namespace of `src/_pytest/_code/code.py` for `check_ispytest`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/_code/code.py')",
   "key": "[\"symbols\", [\"src/_pytest/_code/code.py\"]]",
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
     "src/_pytest/_code/code.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/_code/code.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/_code/code.py\", \"check_ispytest\"]]",
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
     "src/_pytest/_code/code.py",
     "check_ispytest"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/_pytest/_code/code.py')",
  "key": "[\"symbols\", [\"src/_pytest/_code/code.py\"]]",
  "provenance": "module `src/_pytest/_code/code.py` (task)",
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
  "cap": "[\"symbols\", [\"src/_pytest/_code/code.py\", \"check_ispytest\"]]"
 },
 "adherence": null,
 "facts": [
  {
   "kind": "outline",
   "step": 1,
   "path": "src/_pytest/_code/code.py",
   "filter": null,
   "header": {
    "lines": 1682,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/_pytest/_code/code.py",
     "name": "annotations",
     "line": 2,
     "kind": "from",
     "src": "__future__",
     "src_name": "annotations",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/_code/code.py",
     "name": "ast",
     "line": 4,
     "kind": "import",
     "src": "ast",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/_code/code.py",
     "name": "Callable",
     "line": 5,
     "kind": "from",
     "src": "collections.abc",
     "src_name": "Callable",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/_code/code.py",
     "name": "Iterable",
     "line": 6,
     "kind": "from",
     "src": "collections.abc",
     "src_name": "Iterable",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/_code/code.py",
     "name": "Mapping",
     "line": 7,
     "kind": "from",
     "src": "collections.abc",
     "src_name": "Mapping",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/_code/code.py",
     "name": "Sequence",
     "line": 8,
     "kind": "from",
     "src": "collections.abc",
     "src_name": "Sequence",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/_code/code.py",
     "name": "dataclasses",
     "line": 9,
     "kind": "import",
     "src": "dataclasses",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/_code/code.py",
     "name": "inspect",
     "line": 10,
     "kind": "import",
     "src": "inspect",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/_code/code.py",
     "name": "StringIO",
     "line": 11,
     "kind": "from",
     "src": "io",
     "src_name": "StringIO",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/_code/code.py",
     "name": "os",
     "line": 12,
     "kind": "import",
     "src": "os",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/_code/code.py",
     "name": "Path",
     "line": 13,
     "kind": "from",
     "src": "pathlib",
     "src_name": "Path",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/_code/code.py",
     "name": "re",
     "line": 14,
     "kind": "import",
     "src": "re",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/_code/code.py",
     "name": "sys",
     "line": 15,
     "kind": "import",
     "src": "sys",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/_code/code.py",
     "name": "extract_tb",
     "line": 16,
     "kind": "from",
     "src": "traceback",
     "src_name": "extract_tb",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/_code/code.py",
     "name": "format_exception",
     "line": 17,
     "kind": "from",
     "src": "traceback",
     "src_name": "format_exception",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/_code/code.py",
     "name": "format_exception_only",
     "line": 18,
     "kind": "from",
     "src": "traceback",
     "src_name": "format_exception_only",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/_code/code.py",
     "name": "FrameSummary",
     "line": 19,
     "kind": "from",
     "src": "traceback",
     "src_name": "FrameSummary",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/_code/code.py",
     "name": "StackSummary",
     "line": 20,
     "kin
```
</details>

## Step 2

The outline of `src/_pytest/_code/code.py` has 40 bindings (capped, so this is only the start of the file); no `__all__`; no dynamic namespace tricks.

Chain: `src/_pytest/_code/code.py` is not yet closed for `check_ispytest`.

Still to settle: close the namespace of `src/_pytest/_code/code.py` for `check_ispytest`.

Next: outline `src/_pytest/_code/code.py` filtered to `check_ispytest`, because module `src/_pytest/_code/code.py` (task), name `check_ispytest` (task). I expect: a re-export continues the chain to its source (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a definition there ends the chain (under 5%); no binding but a star import means checking what that source exports (under 5%). Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done.

**Call:** `symbols('src/_pytest/_code/code.py', 'check_ispytest')`

**Response**: outcome `reexport`

```
module src/_pytest/_code/code.py lines=1682 dynamic=no all=none
47 from check_ispytest <- _pytest.deprecated check_ispytest
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/_pytest/_code/code.py",
    "check_ispytest"
   ],
   "desc": "close the namespace of `src/_pytest/_code/code.py` for `check_ispytest`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/_code/code.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/_code/code.py\", \"check_ispytest\"]]",
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
     "src/_pytest/_code/code.py",
     "check_ispytest"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/_pytest/_code/code.py', 'check_ispytest')",
  "key": "[\"symbols\", [\"src/_pytest/_code/code.py\", \"check_ispytest\"]]",
  "provenance": "module `src/_pytest/_code/code.py` (task), name `check_ispytest` (task)",
  "v2": [
   735809,
   250800
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
 "adherence": {
  "planned": "[\"symbols\", [\"src/_pytest/_code/code.py\", \"check_ispytest\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 2,
   "path": "src/_pytest/_code/code.py",
   "filter": "check_ispytest",
   "header": {
    "lines": 1682,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/_pytest/_code/code.py",
     "name": "check_ispytest",
     "line": 47,
     "kind": "from",
     "src": "_pytest.deprecated",
     "src_name": "check_ispytest",
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
    "src/_pytest/_code/code.py",
    "check_ispytest",
    "reexport",
    [
     "_pytest.deprecated",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 3

In `src/_pytest/_code/code.py`, `check_ispytest` has exactly one binding: line 47 imports it as `check_ispytest` from `_pytest.deprecated`. No dynamic namespace tricks, no `__all__`.

Chain: `src/_pytest/_code/code.py` takes `check_ispytest` from `_pytest.deprecated` (module not yet located).

Outstanding: locate the module `_pytest.deprecated` imported by `src/_pytest/_code/code.py`.

Next: grep `def`/`class check_ispytest` statements under `.`, because a `def`/`class check_ispytest` statement would reveal the module file; `check_ispytest` task. I expect: hits under the cap (about 95%); a capped result (about 5%); no hits (about 5%). The alternative, list `.`, is more likely to hit the cap (about 20% against about 5%). Plan by outcome: zero: list `.`; mid: outline each module that appears; cap: list `.`.

**Call:** `grep('^\\s*(?:async\\s+)?(?:def|class)\\s+check_ispytest\\b', '.')`

**Response**: outcome `mid`

```
src/_pytest/deprecated.py:153:def check_ispytest(ispytest: bool) -> None:
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/_pytest/_code/code.py",
    "_pytest.deprecated"
   ],
   "desc": "locate the module `_pytest.deprecated` imported by `src/_pytest/_code/code.py`"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+check_ispytest\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+check_ispytest\\\\b\", \".\"]]",
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
     "src/_pytest/_code/code.py",
     "_pytest.deprecated"
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
     "src/_pytest/_code/code.py",
     "_pytest.deprecated"
    ]
   ]
  },
  {
   "call": "symbols('_pytest/deprecated.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"_pytest/deprecated.py\", \"check_ispytest\"]]",
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
     "src/_pytest/_code/code.py",
     "_pytest.deprecated"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+check_ispytest\\\\b', 'src')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+check_ispytest\\\\b\", \"src\"]]",
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
     "src/_pytest/_code/code.py",
     "_pytest.deprecated"
    ]
   ]
  },
  {
   "call": "symbols('_pytest/deprecated/__init__.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"_pytest/deprecated/__init__.py\", \"check_ispytest\"]]",
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
     "src/_pytest/_code/code.py",
     "_pytest.deprecated"
    ]
   ]
  }
 ],
 "choice": {
  "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+check_ispytest\\\\b', '.')",
  "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+check_ispytest\\\\b\", \".\"]]",
  "provenance": "a `def`/`class check_ispytest` statement would reveal the module file; `check_ispytest` task",
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
   "pattern": "^\\s*(?:async\\s+)?(?:def|class)\\s+check_ispytest\\b",
   "scope": ".",
   "hits": [
    [
     "src/_pytest/deprecated.py",
     153
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "chain": [
   [
    "src/_pytest/_code/code.py",
    "check_ispytest",
    "reexport",
    [
     "_pytest.deprecated",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 4

The grep under `.` returned 1 lines, under the cap, so these are all of them: `src/_pytest/deprecated.py`.

Chain: `src/_pytest/_code/code.py` takes `check_ispytest` from `_pytest.deprecated` (module not yet located).

Outstanding: locate the module `_pytest.deprecated` imported by `src/_pytest/_code/code.py`.

Next: list `.`, because `_pytest.deprecated` imported by `src/_pytest/_code/code.py` should live under `.`. I expect: a complete listing settles which files exist (about 80%); a capped listing settles nothing (about 20%). The alternative, outline `_pytest/deprecated.py` filtered to `check_ispytest`, costs more in expectation. Plan by outcome: complete: outline the module it reveals; cap: outline `_pytest/deprecated.py` filtered to `check_ispytest`.

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
    "src/_pytest/_code/code.py",
    "_pytest.deprecated"
   ],
   "desc": "locate the module `_pytest.deprecated` imported by `src/_pytest/_code/code.py`"
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
     "src/_pytest/_code/code.py",
     "_pytest.deprecated"
    ]
   ]
  },
  {
   "call": "symbols('_pytest/deprecated.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"_pytest/deprecated.py\", \"check_ispytest\"]]",
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
     "src/_pytest/_code/code.py",
     "_pytest.deprecated"
    ]
   ]
  },
  {
   "call": "symbols('_pytest/deprecated/__init__.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"_pytest/deprecated/__init__.py\", \"check_ispytest\"]]",
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
     "src/_pytest/_code/code.py",
     "_pytest.deprecated"
    ]
   ]
  }
 ],
 "choice": {
  "call": "ls('.')",
  "key": "[\"ls\", [\".\"]]",
  "provenance": "`_pytest.deprecated` imported by `src/_pytest/_code/code.py` should live under `.`",
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
  "cap": "[\"symbols\", [\"_pytest/deprecated.py\", \"check_ispytest\"]]"
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
    "src/_pytest/_code/code.py",
    "check_ispytest",
    "reexport",
    [
     "_pytest.deprecated",
     "src/_pytest/deprecated.py"
    ]
   ],
   [
    "src/_pytest/deprecated.py",
    "check_ispytest",
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

Chain: `src/_pytest/_code/code.py` takes `check_ispytest` from `_pytest.deprecated` (`src/_pytest/deprecated.py`); `src/_pytest/deprecated.py` is not yet closed for `check_ispytest`.

Still to settle: close the namespace of `src/_pytest/deprecated.py` for `check_ispytest`.

Next: outline `src/_pytest/deprecated.py` filtered to `check_ispytest`, because module `src/_pytest/deprecated.py` (step 3), name `check_ispytest` (task). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `src/_pytest/deprecated.py`, is more likely to hit the cap (about 10% against under 5%). Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done.

**Call:** `symbols('src/_pytest/deprecated.py', 'check_ispytest')`

**Response**: outcome `def`

```
module src/_pytest/deprecated.py lines=156 dynamic=no all=none
153 def check_ispytest
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/_pytest/deprecated.py",
    "check_ispytest"
   ],
   "desc": "close the namespace of `src/_pytest/deprecated.py` for `check_ispytest`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/deprecated.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/deprecated.py\", \"check_ispytest\"]]",
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
     "src/_pytest/deprecated.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/deprecated.py')",
   "key": "[\"symbols\", [\"src/_pytest/deprecated.py\"]]",
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
     "src/_pytest/deprecated.py",
     "check_ispytest"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/_pytest/deprecated.py', 'check_ispytest')",
  "key": "[\"symbols\", [\"src/_pytest/deprecated.py\", \"check_ispytest\"]]",
  "provenance": "module `src/_pytest/deprecated.py` (step 3), name `check_ispytest` (task)",
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
   "path": "src/_pytest/deprecated.py",
   "filter": "check_ispytest",
   "header": {
    "lines": 156,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/_pytest/deprecated.py",
     "name": "check_ispytest",
     "line": 153,
     "kind": "def",
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
    "src/_pytest/_code/code.py",
    "check_ispytest",
    "reexport",
    [
     "_pytest.deprecated",
     "src/_pytest/deprecated.py"
    ]
   ],
   [
    "src/_pytest/deprecated.py",
    "check_ispytest",
    "def",
    153
   ]
  ]
 }
}
```
</details>

## Step 6

In `src/_pytest/deprecated.py`, `check_ispytest` has exactly one binding: a def at line 153. No dynamic namespace tricks, no `__all__`. This is not the branch I planned for that outcome; the open items changed more than expected.

Candidate modules so far: 0; statements confirmed: 0, ruled out: 0, modules with no such import: 0, pending: 0. import coverage open at `.`; star coverage open at `.`.

Open: cover `.` for import lines; cover `.` for star lines.

Next: grep from-imports naming `check_ispytest` or star imports under `.`, because import and star lines under `.` in one call. I expect: hits under the cap (about 60%); no hits (about 35%); a capped result (about 10%). The alternative, grep from-imports naming `check_ispytest` under `.`, serves fewer of the open items. Plan by outcome: zero: done; mid: outline each module that appears; cap: list the scope and split it.

**Call:** `grep('^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bcheck_ispytest\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*check_ispytest\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$', '.')`

**Response**: outcome `mid`

```
src/_pytest/_code/code.py:47:from _pytest.deprecated import check_ispytest
src/_pytest/cacheprovider.py:28:from _pytest.deprecated import check_ispytest
src/_pytest/capture.py:37:from _pytest.deprecated import check_ispytest
src/_pytest/config/argparsing.py:25:from _pytest.deprecated import check_ispytest
src/_pytest/fixtures.py:58:from _pytest.deprecated import check_ispytest
src/_pytest/legacypath.py:22:from _pytest.deprecated import check_ispytest
src/_pytest/logging.py:37:from _pytest.deprecated import check_ispytest
src/_pytest/mark/structures.py:29:from _pytest.deprecated import check_ispytest
src/_pytest/pytester.py:54:from _pytest.deprecated import check_ispytest
src/_pytest/python.py:59:from _pytest.deprecated import check_ispytest
src/_pytest/recwarn.py:27:from _pytest.deprecated import check_ispytest
src/_pytest/runner.py:29:from _pytest.deprecated import check_ispytest
src/_pytest/subtests.py:29:from _pytest.deprecated import check_ispytest
src/_pytest/tmpdir.py:30:from _pytest.deprecated import check_ispytest
testing/acceptance_test.py:599:            from pytest import *
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
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bcheck_ispytest\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*check_ispytest\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bcheck_ispytest\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*check_ispytest\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
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
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bcheck_ispytest\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*check_ispytest\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bcheck_ispytest\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*check_ispytest\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
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
  "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bcheck_ispytest\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*check_ispytest\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
  "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bcheck_ispytest\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*check_ispytest\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
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
   "step": 6,
   "pattern": "^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bcheck_ispytest\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*check_ispytest\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$",
   "scope": ".",
   "hits": [
    [
     "src/_pytest/_code/code.py",
     47
    ],
    [
     "src/_pytest/cacheprovider.py",
     28
    ],
    [
     "src/_pytest/capture.py",
     37
    ],
    [
     "src/_pytest/config/argparsing.py",
     25
    ],
    [
     "src/_pytest/fixtures.py",
     58
    ],
    [
     "src/_pytest/legacypath.py",
     22
    ],
    [
     "src/_pytest/logging.py",
     37
    ],
    [
     "src/_pytest/mark/structures.py",
     29
    ],
    [
     "src/_pytest/pytester.py",
     54
    ],
    [
     "src/_pytest/python.py",
     59
    ],
    [
     "src/_pytest/recwarn.py",
     27
    ],
    [
     "src/_pytest/runner.py",
     29
    ],
    [
     "src/_pytest/subtests.py",
     29
    ],
    [
     "src/_pytest/tmpdir.py",
     30
    ],
    [
     "testing/acceptance_test.py",
     599
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "src/_pytest/_code/code.py",
    47,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/cacheprovider.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "src/_pytest/capture.py",
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
    "src/_pytest/fixtures.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "src/_pytest/legacypath.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "src/_pytest/logging.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "src/_pytest/mark/structures.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "src/_pytest/pytester.py",
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
    "src/_pytest/recwarn.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "src/_pytest/runner.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "src/_pytest/subtests.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "src/_pytest/tmpdir.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "testing/acceptance_test.py",
    0,
    "pending",
    "outline not yet seen"
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

## Step 7

The grep under `.` returned 15 lines, under the cap, so these are all of them: `src/_pytest/_code/code.py`, `src/_pytest/cacheprovider.py`, `src/_pytest/capture.py`, `src/_pytest/config/argparsing.py` and 11 more files.

Candidate modules so far: 15; statements confirmed: 1, ruled out: 0, modules with no such import: 0, pending: 14. import coverage complete; star coverage complete.

Open: outline `src/_pytest/cacheprovider.py` for its `check_ispytest` imports; outline `src/_pytest/capture.py` for its `check_ispytest` imports; outline `src/_pytest/config/argparsing.py` for its `check_ispytest` imports; outline `src/_pytest/fixtures.py` for its `check_ispytest` imports; and 10 more.

Next: outline `src/_pytest/tmpdir.py` filtered to `check_ispytest`, because `src/_pytest/tmpdir.py` had a matching line (step 6); its outline names every `check_ispytest` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/_pytest/cacheprovider.py` filtered to `check_ispytest`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/_pytest/cacheprovider.py` filtered to `check_ispytest`; cap: outline `src/_pytest/cacheprovider.py` filtered to `check_ispytest`.

**Call:** `symbols('src/_pytest/tmpdir.py', 'check_ispytest')`

**Response**: outcome `ok`

```
module src/_pytest/tmpdir.py lines=347 dynamic=no all=none
30 from check_ispytest <- _pytest.deprecated check_ispytest
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/cacheprovider.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/cacheprovider.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/capture.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/capture.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/argparsing.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/config/argparsing.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/fixtures.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/fixtures.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/legacypath.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/legacypath.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/logging.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/logging.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/mark/structures.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/mark/structures.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/pytester.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/pytester.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/python.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/recwarn.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/recwarn.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/runner.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/runner.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/subtests.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/subtests.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/tmpdir.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/tmpdir.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "check_ispytest"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `check_ispytest` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/cacheprovider.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/cacheprovider.py\", \"check_ispytest\"]]",
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
     "src/_pytest/cacheprovider.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/capture.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/capture.py\", \"check_ispytest\"]]",
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
     "src/_pytest/capture.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/config/argparsing.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/config/argparsing.py\", \"check_ispytest\"]]",
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
     "src/_pytest/config/argparsing.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/fixtures.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/fixtures.py\", \"check_ispytest\"]]",
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
     "src/_pytest/fixtures.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/legacypath.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/legacypath.py\", \"check_ispytest\"]]",
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
     "src/_pytest/legacypath.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/logging.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/logging.py\", \"check_ispytest\"]]",
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
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/mark/structures.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/mark/structures.py\", \"check_ispytest\"]]",
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
    
```
</details>

## Step 8

In `src/_pytest/tmpdir.py`, `check_ispytest` has exactly one binding: line 30 imports it as `check_ispytest` from `_pytest.deprecated`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 15; statements confirmed: 2, ruled out: 0, modules with no such import: 0, pending: 13. import coverage complete; star coverage complete.

Outstanding: outline `src/_pytest/cacheprovider.py` for its `check_ispytest` imports; outline `src/_pytest/capture.py` for its `check_ispytest` imports; outline `src/_pytest/config/argparsing.py` for its `check_ispytest` imports; outline `src/_pytest/fixtures.py` for its `check_ispytest` imports; and 9 more.

Next: outline `src/_pytest/cacheprovider.py` filtered to `check_ispytest`, because `src/_pytest/cacheprovider.py` had a matching line (step 6); its outline names every `check_ispytest` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/_pytest/capture.py` filtered to `check_ispytest`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/_pytest/capture.py` filtered to `check_ispytest`; cap: outline `src/_pytest/capture.py` filtered to `check_ispytest`.

**Call:** `symbols('src/_pytest/cacheprovider.py', 'check_ispytest')`

**Response**: outcome `ok`

```
module src/_pytest/cacheprovider.py lines=661 dynamic=no all=none
28 from check_ispytest <- _pytest.deprecated check_ispytest
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/cacheprovider.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/cacheprovider.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/capture.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/capture.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/argparsing.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/config/argparsing.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/fixtures.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/fixtures.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/legacypath.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/legacypath.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/logging.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/logging.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/mark/structures.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/mark/structures.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/pytester.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/pytester.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/python.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/recwarn.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/recwarn.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/runner.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/runner.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/subtests.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/subtests.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "check_ispytest"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `check_ispytest` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/cacheprovider.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/cacheprovider.py\", \"check_ispytest\"]]",
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
     "src/_pytest/cacheprovider.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/capture.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/capture.py\", \"check_ispytest\"]]",
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
     "src/_pytest/capture.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/config/argparsing.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/config/argparsing.py\", \"check_ispytest\"]]",
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
     "src/_pytest/config/argparsing.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/fixtures.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/fixtures.py\", \"check_ispytest\"]]",
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
     "src/_pytest/fixtures.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/legacypath.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/legacypath.py\", \"check_ispytest\"]]",
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
     "src/_pytest/legacypath.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/logging.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/logging.py\", \"check_ispytest\"]]",
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
     "src/_pytest/logging.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/mark/structures.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/mark/structures.py\", \"check_ispytest\"]]",
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
     "src/_pytest/mark/structures.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/pytester.py', 'check_ispy
```
</details>

## Step 9

In `src/_pytest/cacheprovider.py`, `check_ispytest` has exactly one binding: line 28 imports it as `check_ispytest` from `_pytest.deprecated`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 15; statements confirmed: 3, ruled out: 0, modules with no such import: 0, pending: 12. import coverage complete; star coverage complete.

Still to settle: outline `src/_pytest/capture.py` for its `check_ispytest` imports; outline `src/_pytest/config/argparsing.py` for its `check_ispytest` imports; outline `src/_pytest/fixtures.py` for its `check_ispytest` imports; outline `src/_pytest/legacypath.py` for its `check_ispytest` imports; and 8 more.

Next: outline `src/_pytest/capture.py` filtered to `check_ispytest`, because `src/_pytest/capture.py` had a matching line (step 6); its outline names every `check_ispytest` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/_pytest/config/argparsing.py` filtered to `check_ispytest`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/_pytest/config/argparsing.py` filtered to `check_ispytest`; cap: outline `src/_pytest/config/argparsing.py` filtered to `check_ispytest`.

**Call:** `symbols('src/_pytest/capture.py', 'check_ispytest')`

**Response**: outcome `ok`

```
module src/_pytest/capture.py lines=1158 dynamic=no all=none
37 from check_ispytest <- _pytest.deprecated check_ispytest
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/capture.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/capture.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/config/argparsing.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/config/argparsing.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/fixtures.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/fixtures.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/legacypath.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/legacypath.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/logging.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/logging.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/mark/structures.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/mark/structures.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/pytester.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/pytester.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/python.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/recwarn.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/recwarn.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/runner.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/runner.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/subtests.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/subtests.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "check_ispytest"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `check_ispytest` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/capture.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/capture.py\", \"check_ispytest\"]]",
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
     "src/_pytest/capture.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/config/argparsing.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/config/argparsing.py\", \"check_ispytest\"]]",
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
     "src/_pytest/config/argparsing.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/fixtures.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/fixtures.py\", \"check_ispytest\"]]",
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
     "src/_pytest/fixtures.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/legacypath.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/legacypath.py\", \"check_ispytest\"]]",
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
     "src/_pytest/legacypath.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/logging.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/logging.py\", \"check_ispytest\"]]",
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
     "src/_pytest/logging.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/mark/structures.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/mark/structures.py\", \"check_ispytest\"]]",
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
     "src/_pytest/mark/structures.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/pytester.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/pytester.py\", \"check_ispytest\"]]",
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
     "src/_pytest/pytester.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/python.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/python.py\", \"check_ispytest\"]]",
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
 
```
</details>

## Step 10

In `src/_pytest/capture.py`, `check_ispytest` has exactly one binding: line 37 imports it as `check_ispytest` from `_pytest.deprecated`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 15; statements confirmed: 4, ruled out: 0, modules with no such import: 0, pending: 11. import coverage complete; star coverage complete.

Still to settle: outline `src/_pytest/config/argparsing.py` for its `check_ispytest` imports; outline `src/_pytest/fixtures.py` for its `check_ispytest` imports; outline `src/_pytest/legacypath.py` for its `check_ispytest` imports; outline `src/_pytest/logging.py` for its `check_ispytest` imports; and 7 more.

Next: outline `src/_pytest/config/argparsing.py` filtered to `check_ispytest`, because `src/_pytest/config/argparsing.py` had a matching line (step 6); its outline names every `check_ispytest` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/_pytest/fixtures.py` filtered to `check_ispytest`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/_pytest/fixtures.py` filtered to `check_ispytest`; cap: outline `src/_pytest/fixtures.py` filtered to `check_ispytest`.

**Call:** `symbols('src/_pytest/config/argparsing.py', 'check_ispytest')`

**Response**: outcome `ok`

```
module src/_pytest/config/argparsing.py lines=616 dynamic=no all=none
25 from check_ispytest <- _pytest.deprecated check_ispytest
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
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/config/argparsing.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/fixtures.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/fixtures.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/legacypath.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/legacypath.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/logging.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/logging.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/mark/structures.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/mark/structures.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/pytester.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/pytester.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/python.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/recwarn.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/recwarn.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/runner.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/runner.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/subtests.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/subtests.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "check_ispytest"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `check_ispytest` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/config/argparsing.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/config/argparsing.py\", \"check_ispytest\"]]",
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
     "src/_pytest/config/argparsing.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/fixtures.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/fixtures.py\", \"check_ispytest\"]]",
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
     "src/_pytest/fixtures.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/legacypath.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/legacypath.py\", \"check_ispytest\"]]",
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
     "src/_pytest/legacypath.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/logging.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/logging.py\", \"check_ispytest\"]]",
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
     "src/_pytest/logging.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/mark/structures.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/mark/structures.py\", \"check_ispytest\"]]",
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
     "src/_pytest/mark/structures.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/pytester.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/pytester.py\", \"check_ispytest\"]]",
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
     "src/_pytest/pytester.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/python.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/python.py\", \"check_ispytest\"]]",
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
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/recwarn.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/recwarn.py\", \"check_ispytest\"]]",
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
     "src/_pytest/recwarn.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "sy
```
</details>

## Step 11

In `src/_pytest/config/argparsing.py`, `check_ispytest` has exactly one binding: line 25 imports it as `check_ispytest` from `_pytest.deprecated`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 15; statements confirmed: 5, ruled out: 0, modules with no such import: 0, pending: 10. import coverage complete; star coverage complete.

Outstanding: outline `src/_pytest/fixtures.py` for its `check_ispytest` imports; outline `src/_pytest/legacypath.py` for its `check_ispytest` imports; outline `src/_pytest/logging.py` for its `check_ispytest` imports; outline `src/_pytest/mark/structures.py` for its `check_ispytest` imports; and 6 more.

Next: outline `src/_pytest/fixtures.py` filtered to `check_ispytest`, because `src/_pytest/fixtures.py` had a matching line (step 6); its outline names every `check_ispytest` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/_pytest/legacypath.py` filtered to `check_ispytest`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/_pytest/legacypath.py` filtered to `check_ispytest`; cap: outline `src/_pytest/legacypath.py` filtered to `check_ispytest`.

**Call:** `symbols('src/_pytest/fixtures.py', 'check_ispytest')`

**Response**: outcome `ok`

```
module src/_pytest/fixtures.py lines=2600 dynamic=no all=none
58 from check_ispytest <- _pytest.deprecated check_ispytest
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/fixtures.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/fixtures.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/legacypath.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/legacypath.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/logging.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/logging.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/mark/structures.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/mark/structures.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/pytester.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/pytester.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/python.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/recwarn.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/recwarn.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/runner.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/runner.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/subtests.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/subtests.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "check_ispytest"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `check_ispytest` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/fixtures.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/fixtures.py\", \"check_ispytest\"]]",
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
     "src/_pytest/fixtures.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/legacypath.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/legacypath.py\", \"check_ispytest\"]]",
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
     "src/_pytest/legacypath.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/logging.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/logging.py\", \"check_ispytest\"]]",
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
     "src/_pytest/logging.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/mark/structures.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/mark/structures.py\", \"check_ispytest\"]]",
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
     "src/_pytest/mark/structures.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/pytester.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/pytester.py\", \"check_ispytest\"]]",
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
     "src/_pytest/pytester.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/python.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/python.py\", \"check_ispytest\"]]",
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
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/recwarn.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/recwarn.py\", \"check_ispytest\"]]",
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
     "src/_pytest/recwarn.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/runner.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/runner.py\", \"check_ispytest\"]]",
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
     "src/_pytest/runner.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/subtests.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/subtests.py\", \"check_ispytest\"]]",
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
 
```
</details>

## Step 12

In `src/_pytest/fixtures.py`, `check_ispytest` has exactly one binding: line 58 imports it as `check_ispytest` from `_pytest.deprecated`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 15; statements confirmed: 6, ruled out: 0, modules with no such import: 0, pending: 9. import coverage complete; star coverage complete.

Open: outline `src/_pytest/legacypath.py` for its `check_ispytest` imports; outline `src/_pytest/logging.py` for its `check_ispytest` imports; outline `src/_pytest/mark/structures.py` for its `check_ispytest` imports; outline `src/_pytest/pytester.py` for its `check_ispytest` imports; and 5 more.

Next: outline `src/_pytest/legacypath.py` filtered to `check_ispytest`, because `src/_pytest/legacypath.py` had a matching line (step 6); its outline names every `check_ispytest` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/_pytest/logging.py` filtered to `check_ispytest`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/_pytest/logging.py` filtered to `check_ispytest`; cap: outline `src/_pytest/logging.py` filtered to `check_ispytest`.

**Call:** `symbols('src/_pytest/legacypath.py', 'check_ispytest')`

**Response**: outcome `ok`

```
module src/_pytest/legacypath.py lines=472 dynamic=no all=none
22 from check_ispytest <- _pytest.deprecated check_ispytest
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/legacypath.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/legacypath.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/logging.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/logging.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/mark/structures.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/mark/structures.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/pytester.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/pytester.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/python.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/recwarn.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/recwarn.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/runner.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/runner.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/subtests.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/subtests.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "check_ispytest"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `check_ispytest` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/legacypath.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/legacypath.py\", \"check_ispytest\"]]",
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
     "src/_pytest/legacypath.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/logging.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/logging.py\", \"check_ispytest\"]]",
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
     "src/_pytest/logging.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/mark/structures.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/mark/structures.py\", \"check_ispytest\"]]",
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
     "src/_pytest/mark/structures.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/pytester.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/pytester.py\", \"check_ispytest\"]]",
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
     "src/_pytest/pytester.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/python.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/python.py\", \"check_ispytest\"]]",
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
     "src/_pytest/python.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/recwarn.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/recwarn.py\", \"check_ispytest\"]]",
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
     "src/_pytest/recwarn.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/runner.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/runner.py\", \"check_ispytest\"]]",
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
     "src/_pytest/runner.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/subtests.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/subtests.py\", \"check_ispytest\"]]",
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
     "src/_pytest/subtests.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('testing/acceptance_test.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"check_ispytest\"]]",
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
     "check_ispytest"
    ]
   ]
  }
 ],
 "choice": 
```
</details>

## Step 13

In `src/_pytest/legacypath.py`, `check_ispytest` has exactly one binding: line 22 imports it as `check_ispytest` from `_pytest.deprecated`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 15; statements confirmed: 7, ruled out: 0, modules with no such import: 0, pending: 8. import coverage complete; star coverage complete.

Outstanding: outline `src/_pytest/logging.py` for its `check_ispytest` imports; outline `src/_pytest/mark/structures.py` for its `check_ispytest` imports; outline `src/_pytest/pytester.py` for its `check_ispytest` imports; outline `src/_pytest/python.py` for its `check_ispytest` imports; and 4 more.

Next: outline `src/_pytest/logging.py` filtered to `check_ispytest`, because `src/_pytest/logging.py` had a matching line (step 6); its outline names every `check_ispytest` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/_pytest/mark/structures.py` filtered to `check_ispytest`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/_pytest/mark/structures.py` filtered to `check_ispytest`; cap: outline `src/_pytest/mark/structures.py` filtered to `check_ispytest`.

**Call:** `symbols('src/_pytest/logging.py', 'check_ispytest')`

**Response**: outcome `ok`

```
module src/_pytest/logging.py lines=979 dynamic=no all=none
37 from check_ispytest <- _pytest.deprecated check_ispytest
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
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/logging.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/mark/structures.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/mark/structures.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/pytester.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/pytester.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/python.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/recwarn.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/recwarn.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/runner.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/runner.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/subtests.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/subtests.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "check_ispytest"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `check_ispytest` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/logging.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/logging.py\", \"check_ispytest\"]]",
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
     "src/_pytest/logging.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/mark/structures.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/mark/structures.py\", \"check_ispytest\"]]",
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
     "src/_pytest/mark/structures.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/pytester.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/pytester.py\", \"check_ispytest\"]]",
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
     "src/_pytest/pytester.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/python.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/python.py\", \"check_ispytest\"]]",
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
     "src/_pytest/python.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/recwarn.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/recwarn.py\", \"check_ispytest\"]]",
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
     "src/_pytest/recwarn.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/runner.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/runner.py\", \"check_ispytest\"]]",
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
     "src/_pytest/runner.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/subtests.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/subtests.py\", \"check_ispytest\"]]",
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
     "src/_pytest/subtests.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('testing/acceptance_test.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"check_ispytest\"]]",
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
     "check_ispytest"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/_pytest/logging.py', 'check_ispytest')",
  "key": "[\"symbols\", [\"src/_pytest/logging.py\", \"check_ispytest\"]]",
  "provenance": "`src/_pytest/logging.py` had a matching line (step 6); its outline names every `check_ispytest` import exactly",
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
  "ok": "[\"symbols\", [\"src/_pytest/mark/structures.py\", \"check_ispytest\"]]",
  "cap": "[\"symbols\", [\"src/_pytest/mark/structures.py\", \"check_ispytest\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"src/_pytest/logging.py\", \"check_ispyt
```
</details>

## Step 14

In `src/_pytest/logging.py`, `check_ispytest` has exactly one binding: line 37 imports it as `check_ispytest` from `_pytest.deprecated`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 15; statements confirmed: 8, ruled out: 0, modules with no such import: 0, pending: 7. import coverage complete; star coverage complete.

Open: outline `src/_pytest/mark/structures.py` for its `check_ispytest` imports; outline `src/_pytest/pytester.py` for its `check_ispytest` imports; outline `src/_pytest/python.py` for its `check_ispytest` imports; outline `src/_pytest/recwarn.py` for its `check_ispytest` imports; and 3 more.

Next: outline `src/_pytest/mark/structures.py` filtered to `check_ispytest`, because `src/_pytest/mark/structures.py` had a matching line (step 6); its outline names every `check_ispytest` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/_pytest/pytester.py` filtered to `check_ispytest`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/_pytest/pytester.py` filtered to `check_ispytest`; cap: outline `src/_pytest/pytester.py` filtered to `check_ispytest`.

**Call:** `symbols('src/_pytest/mark/structures.py', 'check_ispytest')`

**Response**: outcome `ok`

```
module src/_pytest/mark/structures.py lines=696 dynamic=no all=none
29 from check_ispytest <- _pytest.deprecated check_ispytest
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/mark/structures.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/mark/structures.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/pytester.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/pytester.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/python.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/recwarn.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/recwarn.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/runner.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/runner.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/subtests.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/subtests.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "check_ispytest"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `check_ispytest` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/mark/structures.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/mark/structures.py\", \"check_ispytest\"]]",
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
     "src/_pytest/mark/structures.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/pytester.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/pytester.py\", \"check_ispytest\"]]",
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
     "src/_pytest/pytester.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/python.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/python.py\", \"check_ispytest\"]]",
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
     "src/_pytest/python.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/recwarn.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/recwarn.py\", \"check_ispytest\"]]",
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
     "src/_pytest/recwarn.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/runner.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/runner.py\", \"check_ispytest\"]]",
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
     "src/_pytest/runner.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/subtests.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/subtests.py\", \"check_ispytest\"]]",
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
     "src/_pytest/subtests.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('testing/acceptance_test.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"check_ispytest\"]]",
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
     "testing/acceptance_test.py",
     "check_ispytest"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/_pytest/mark/structures.py', 'check_ispytest')",
  "key": "[\"symbols\", [\"src/_pytest/mark/structures.py\", \"check_ispytest\"]]",
  "provenance": "`src/_pytest/mark/structures.py` had a matching line (step 6); its outline names every `check_ispytest` import exactly",
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
  "ok": "[\"symbols\", [\"src/_pytest/pytester.py\", \"check_ispytest\"]]",
  "cap": "[\"symbols\", [\"src/_pytest/pytester.py\", \"check_ispytest\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"src/_pytest/mark/structures.py\", \"check_ispytest\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 14,
   "path": "src/_pytest/mark/structures.py",
   "filter": "check_ispytest",
   "header": {
    "lines": 696,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/_pytest/mark/structures.py",
     "name": "check_ispytest",
     "line": 29,
     "kind": "from",
     "src": "_pytest.deprecated",
     "src_name": "check_ispytest",
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
    "src/_pytest/_code/code.py",
```
</details>

## Step 15

In `src/_pytest/mark/structures.py`, `check_ispytest` has exactly one binding: line 29 imports it as `check_ispytest` from `_pytest.deprecated`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 15; statements confirmed: 9, ruled out: 0, modules with no such import: 0, pending: 6. import coverage complete; star coverage complete.

Still to settle: outline `src/_pytest/pytester.py` for its `check_ispytest` imports; outline `src/_pytest/python.py` for its `check_ispytest` imports; outline `src/_pytest/recwarn.py` for its `check_ispytest` imports; outline `src/_pytest/runner.py` for its `check_ispytest` imports; and 2 more.

Next: outline `src/_pytest/pytester.py` filtered to `check_ispytest`, because `src/_pytest/pytester.py` had a matching line (step 6); its outline names every `check_ispytest` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/_pytest/python.py` filtered to `check_ispytest`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/_pytest/python.py` filtered to `check_ispytest`; cap: outline `src/_pytest/python.py` filtered to `check_ispytest`.

**Call:** `symbols('src/_pytest/pytester.py', 'check_ispytest')`

**Response**: outcome `ok`

```
module src/_pytest/pytester.py lines=1816 dynamic=no all=none
54 from check_ispytest <- _pytest.deprecated check_ispytest
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/pytester.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/pytester.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/python.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/recwarn.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/recwarn.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/runner.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/runner.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/subtests.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/subtests.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "check_ispytest"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `check_ispytest` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/pytester.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/pytester.py\", \"check_ispytest\"]]",
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
     "src/_pytest/pytester.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/python.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/python.py\", \"check_ispytest\"]]",
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
     "src/_pytest/python.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/recwarn.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/recwarn.py\", \"check_ispytest\"]]",
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
     "src/_pytest/recwarn.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/runner.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/runner.py\", \"check_ispytest\"]]",
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
     "src/_pytest/runner.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/subtests.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/subtests.py\", \"check_ispytest\"]]",
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
     "src/_pytest/subtests.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('testing/acceptance_test.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"check_ispytest\"]]",
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
     "testing/acceptance_test.py",
     "check_ispytest"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/_pytest/pytester.py', 'check_ispytest')",
  "key": "[\"symbols\", [\"src/_pytest/pytester.py\", \"check_ispytest\"]]",
  "provenance": "`src/_pytest/pytester.py` had a matching line (step 6); its outline names every `check_ispytest` import exactly",
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
  "ok": "[\"symbols\", [\"src/_pytest/python.py\", \"check_ispytest\"]]",
  "cap": "[\"symbols\", [\"src/_pytest/python.py\", \"check_ispytest\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"src/_pytest/pytester.py\", \"check_ispytest\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 15,
   "path": "src/_pytest/pytester.py",
   "filter": "check_ispytest",
   "header": {
    "lines": 1816,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/_pytest/pytester.py",
     "name": "check_ispytest",
     "line": 54,
     "kind": "from",
     "src": "_pytest.deprecated",
     "src_name": "check_ispytest",
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
    "src/_pytest/_code/code.py",
    47,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/cacheprovider.py",
    28,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/capture.py",
    37,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/config/argparsing.py",
    25,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/fixtures.py",
    58,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/legacypath.py",
    22,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "sr
```
</details>

## Step 16

In `src/_pytest/pytester.py`, `check_ispytest` has exactly one binding: line 54 imports it as `check_ispytest` from `_pytest.deprecated`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 15; statements confirmed: 10, ruled out: 0, modules with no such import: 0, pending: 5. import coverage complete; star coverage complete.

Outstanding: outline `src/_pytest/python.py` for its `check_ispytest` imports; outline `src/_pytest/recwarn.py` for its `check_ispytest` imports; outline `src/_pytest/runner.py` for its `check_ispytest` imports; outline `src/_pytest/subtests.py` for its `check_ispytest` imports; and 1 more.

Next: outline `src/_pytest/python.py` filtered to `check_ispytest`, because `src/_pytest/python.py` had a matching line (step 6); its outline names every `check_ispytest` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/_pytest/recwarn.py` filtered to `check_ispytest`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/_pytest/recwarn.py` filtered to `check_ispytest`; cap: outline `src/_pytest/recwarn.py` filtered to `check_ispytest`.

**Call:** `symbols('src/_pytest/python.py', 'check_ispytest')`

**Response**: outcome `ok`

```
module src/_pytest/python.py lines=1843 dynamic=yes all=none
59 from check_ispytest <- _pytest.deprecated check_ispytest
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
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/python.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/recwarn.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/recwarn.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/runner.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/runner.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/subtests.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/subtests.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "check_ispytest"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `check_ispytest` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/python.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/python.py\", \"check_ispytest\"]]",
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
     "src/_pytest/python.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/recwarn.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/recwarn.py\", \"check_ispytest\"]]",
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
     "src/_pytest/recwarn.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/runner.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/runner.py\", \"check_ispytest\"]]",
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
     "src/_pytest/runner.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/subtests.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/subtests.py\", \"check_ispytest\"]]",
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
     "src/_pytest/subtests.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('testing/acceptance_test.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"check_ispytest\"]]",
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
     "testing/acceptance_test.py",
     "check_ispytest"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/_pytest/python.py', 'check_ispytest')",
  "key": "[\"symbols\", [\"src/_pytest/python.py\", \"check_ispytest\"]]",
  "provenance": "`src/_pytest/python.py` had a matching line (step 6); its outline names every `check_ispytest` import exactly",
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
  "ok": "[\"symbols\", [\"src/_pytest/recwarn.py\", \"check_ispytest\"]]",
  "cap": "[\"symbols\", [\"src/_pytest/recwarn.py\", \"check_ispytest\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"src/_pytest/python.py\", \"check_ispytest\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 16,
   "path": "src/_pytest/python.py",
   "filter": "check_ispytest",
   "header": {
    "lines": 1843,
    "dynamic": true,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/_pytest/python.py",
     "name": "check_ispytest",
     "line": 59,
     "kind": "from",
     "src": "_pytest.deprecated",
     "src_name": "check_ispytest",
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
    "src/_pytest/_code/code.py",
    47,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/cacheprovider.py",
    28,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/capture.py",
    37,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/config/argparsing.py",
    25,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/fixtures.py",
    58,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/legacypath.py",
    22,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/logging.py",
    37,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/mark/structures.py",
    29,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/pytester.py",
    54,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/python.py",
    59,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/recwarn.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "src/_pytest/runner.py",
    0,
    "pending",
    "outlin
```
</details>

## Step 17

In `src/_pytest/python.py`, `check_ispytest` has exactly one binding: line 59 imports it as `check_ispytest` from `_pytest.deprecated`. It uses dynamic namespace tricks, no `__all__`.

Candidate modules so far: 15; statements confirmed: 11, ruled out: 0, modules with no such import: 0, pending: 4. import coverage complete; star coverage complete.

Still to settle: outline `src/_pytest/recwarn.py` for its `check_ispytest` imports; outline `src/_pytest/runner.py` for its `check_ispytest` imports; outline `src/_pytest/subtests.py` for its `check_ispytest` imports; outline `testing/acceptance_test.py` for its `check_ispytest` imports.

Next: outline `src/_pytest/recwarn.py` filtered to `check_ispytest`, because `src/_pytest/recwarn.py` had a matching line (step 6); its outline names every `check_ispytest` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/_pytest/runner.py` filtered to `check_ispytest`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/_pytest/runner.py` filtered to `check_ispytest`; cap: outline `src/_pytest/runner.py` filtered to `check_ispytest`.

**Call:** `symbols('src/_pytest/recwarn.py', 'check_ispytest')`

**Response**: outcome `ok`

```
module src/_pytest/recwarn.py lines=379 dynamic=no all=none
27 from check_ispytest <- _pytest.deprecated check_ispytest
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/recwarn.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/recwarn.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/runner.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/runner.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/subtests.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/subtests.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "check_ispytest"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `check_ispytest` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/recwarn.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/recwarn.py\", \"check_ispytest\"]]",
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
     "src/_pytest/recwarn.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/runner.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/runner.py\", \"check_ispytest\"]]",
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
     "src/_pytest/runner.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/subtests.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/subtests.py\", \"check_ispytest\"]]",
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
     "src/_pytest/subtests.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('testing/acceptance_test.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"check_ispytest\"]]",
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
     "testing/acceptance_test.py",
     "check_ispytest"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/_pytest/recwarn.py', 'check_ispytest')",
  "key": "[\"symbols\", [\"src/_pytest/recwarn.py\", \"check_ispytest\"]]",
  "provenance": "`src/_pytest/recwarn.py` had a matching line (step 6); its outline names every `check_ispytest` import exactly",
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
  "ok": "[\"symbols\", [\"src/_pytest/runner.py\", \"check_ispytest\"]]",
  "cap": "[\"symbols\", [\"src/_pytest/runner.py\", \"check_ispytest\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"src/_pytest/recwarn.py\", \"check_ispytest\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 17,
   "path": "src/_pytest/recwarn.py",
   "filter": "check_ispytest",
   "header": {
    "lines": 379,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/_pytest/recwarn.py",
     "name": "check_ispytest",
     "line": 27,
     "kind": "from",
     "src": "_pytest.deprecated",
     "src_name": "check_ispytest",
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
    "src/_pytest/_code/code.py",
    47,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/cacheprovider.py",
    28,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/capture.py",
    37,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/config/argparsing.py",
    25,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/fixtures.py",
    58,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/legacypath.py",
    22,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/logging.py",
    37,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/mark/structures.py",
    29,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/pytester.py",
    54,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/python.py",
    59,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/recwarn.py",
    27,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/runner.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "src/_pytest/subtests.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "src/_pytest/tmpdir.py",
    30,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "testing/acceptance_test.py",
    0,
    "pending",
    "outline not yet seen"
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

## Step 18

In `src/_pytest/recwarn.py`, `check_ispytest` has exactly one binding: line 27 imports it as `check_ispytest` from `_pytest.deprecated`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 15; statements confirmed: 12, ruled out: 0, modules with no such import: 0, pending: 3. import coverage complete; star coverage complete.

Open: outline `src/_pytest/runner.py` for its `check_ispytest` imports; outline `src/_pytest/subtests.py` for its `check_ispytest` imports; outline `testing/acceptance_test.py` for its `check_ispytest` imports.

Next: outline `src/_pytest/runner.py` filtered to `check_ispytest`, because `src/_pytest/runner.py` had a matching line (step 6); its outline names every `check_ispytest` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/_pytest/subtests.py` filtered to `check_ispytest`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/_pytest/subtests.py` filtered to `check_ispytest`; cap: outline `src/_pytest/subtests.py` filtered to `check_ispytest`.

**Call:** `symbols('src/_pytest/runner.py', 'check_ispytest')`

**Response**: outcome `ok`

```
module src/_pytest/runner.py lines=594 dynamic=no all=none
29 from check_ispytest <- _pytest.deprecated check_ispytest
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/runner.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/runner.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/subtests.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/subtests.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "check_ispytest"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `check_ispytest` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/runner.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/runner.py\", \"check_ispytest\"]]",
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
     "src/_pytest/runner.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/subtests.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/subtests.py\", \"check_ispytest\"]]",
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
     "src/_pytest/subtests.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('testing/acceptance_test.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"check_ispytest\"]]",
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
     "testing/acceptance_test.py",
     "check_ispytest"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/_pytest/runner.py', 'check_ispytest')",
  "key": "[\"symbols\", [\"src/_pytest/runner.py\", \"check_ispytest\"]]",
  "provenance": "`src/_pytest/runner.py` had a matching line (step 6); its outline names every `check_ispytest` import exactly",
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
  "ok": "[\"symbols\", [\"src/_pytest/subtests.py\", \"check_ispytest\"]]",
  "cap": "[\"symbols\", [\"src/_pytest/subtests.py\", \"check_ispytest\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"src/_pytest/runner.py\", \"check_ispytest\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 18,
   "path": "src/_pytest/runner.py",
   "filter": "check_ispytest",
   "header": {
    "lines": 594,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/_pytest/runner.py",
     "name": "check_ispytest",
     "line": 29,
     "kind": "from",
     "src": "_pytest.deprecated",
     "src_name": "check_ispytest",
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
    "src/_pytest/_code/code.py",
    47,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/cacheprovider.py",
    28,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/capture.py",
    37,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/config/argparsing.py",
    25,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/fixtures.py",
    58,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/legacypath.py",
    22,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/logging.py",
    37,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/mark/structures.py",
    29,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/pytester.py",
    54,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/python.py",
    59,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/recwarn.py",
    27,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/runner.py",
    29,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/subtests.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "src/_pytest/tmpdir.py",
    30,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "testing/acceptance_test.py",
    0,
    "pending",
    "outline not yet seen"
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

## Step 19

In `src/_pytest/runner.py`, `check_ispytest` has exactly one binding: line 29 imports it as `check_ispytest` from `_pytest.deprecated`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 15; statements confirmed: 13, ruled out: 0, modules with no such import: 0, pending: 2. import coverage complete; star coverage complete.

Outstanding: outline `src/_pytest/subtests.py` for its `check_ispytest` imports; outline `testing/acceptance_test.py` for its `check_ispytest` imports.

Next: outline `src/_pytest/subtests.py` filtered to `check_ispytest`, because `src/_pytest/subtests.py` had a matching line (step 6); its outline names every `check_ispytest` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `testing/acceptance_test.py` filtered to `check_ispytest`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `testing/acceptance_test.py` filtered to `check_ispytest`; cap: outline `testing/acceptance_test.py` filtered to `check_ispytest`.

**Call:** `symbols('src/_pytest/subtests.py', 'check_ispytest')`

**Response**: outcome `ok`

```
module src/_pytest/subtests.py lines=419 dynamic=no all=none
29 from check_ispytest <- _pytest.deprecated check_ispytest
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/subtests.py",
    "check_ispytest"
   ],
   "desc": "outline `src/_pytest/subtests.py` for its `check_ispytest` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "check_ispytest"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `check_ispytest` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/subtests.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"src/_pytest/subtests.py\", \"check_ispytest\"]]",
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
     "src/_pytest/subtests.py",
     "check_ispytest"
    ]
   ]
  },
  {
   "call": "symbols('testing/acceptance_test.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"check_ispytest\"]]",
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
     "testing/acceptance_test.py",
     "check_ispytest"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/_pytest/subtests.py', 'check_ispytest')",
  "key": "[\"symbols\", [\"src/_pytest/subtests.py\", \"check_ispytest\"]]",
  "provenance": "`src/_pytest/subtests.py` had a matching line (step 6); its outline names every `check_ispytest` import exactly",
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
  "ok": "[\"symbols\", [\"testing/acceptance_test.py\", \"check_ispytest\"]]",
  "cap": "[\"symbols\", [\"testing/acceptance_test.py\", \"check_ispytest\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"src/_pytest/subtests.py\", \"check_ispytest\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 19,
   "path": "src/_pytest/subtests.py",
   "filter": "check_ispytest",
   "header": {
    "lines": 419,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/_pytest/subtests.py",
     "name": "check_ispytest",
     "line": 29,
     "kind": "from",
     "src": "_pytest.deprecated",
     "src_name": "check_ispytest",
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
    "src/_pytest/_code/code.py",
    47,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/cacheprovider.py",
    28,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/capture.py",
    37,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/config/argparsing.py",
    25,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/fixtures.py",
    58,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/legacypath.py",
    22,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/logging.py",
    37,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/mark/structures.py",
    29,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/pytester.py",
    54,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/python.py",
    59,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/recwarn.py",
    27,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/runner.py",
    29,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/subtests.py",
    29,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/tmpdir.py",
    30,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "testing/acceptance_test.py",
    0,
    "pending",
    "outline not yet seen"
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

## Step 20

In `src/_pytest/subtests.py`, `check_ispytest` has exactly one binding: line 29 imports it as `check_ispytest` from `_pytest.deprecated`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 15; statements confirmed: 14, ruled out: 0, modules with no such import: 0, pending: 1. import coverage complete; star coverage complete.

Open: outline `testing/acceptance_test.py` for its `check_ispytest` imports.

Next: outline `testing/acceptance_test.py` filtered to `check_ispytest`, because `testing/acceptance_test.py` had a matching line (step 6); its outline names every `check_ispytest` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). Plan by outcome: ok: resolve the sources its import statements name; cap: work the items it opens.

**Call:** `symbols('testing/acceptance_test.py', 'check_ispytest')`

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
    "check_ispytest"
   ],
   "desc": "outline `testing/acceptance_test.py` for its `check_ispytest` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('testing/acceptance_test.py', 'check_ispytest')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"check_ispytest\"]]",
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
     "testing/acceptance_test.py",
     "check_ispytest"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('testing/acceptance_test.py', 'check_ispytest')",
  "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"check_ispytest\"]]",
  "provenance": "`testing/acceptance_test.py` had a matching line (step 6); its outline names every `check_ispytest` import exactly",
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
  "planned": "[\"symbols\", [\"testing/acceptance_test.py\", \"check_ispytest\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 20,
   "path": "testing/acceptance_test.py",
   "filter": "check_ispytest",
   "header": {
    "lines": 1770,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [],
   "complete": true
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "src/_pytest/_code/code.py",
    47,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/cacheprovider.py",
    28,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/capture.py",
    37,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/config/argparsing.py",
    25,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/fixtures.py",
    58,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/legacypath.py",
    22,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/logging.py",
    37,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/mark/structures.py",
    29,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/pytester.py",
    54,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/python.py",
    59,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/recwarn.py",
    27,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/runner.py",
    29,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/subtests.py",
    29,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "src/_pytest/tmpdir.py",
    30,
    "in",
    "`_pytest.deprecated` resolves `check_ispytest` to the target"
   ],
   [
    "testing/acceptance_test.py",
    0,
    "none",
    "no import of the name in this module"
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

Certificate complete. 14 import statements import this definition: `src/_pytest/_code/code.py:47`, `src/_pytest/cacheprovider.py:28`, `src/_pytest/capture.py:37`, `src/_pytest/config/argparsing.py:25`, `src/_pytest/fixtures.py:58`, `src/_pytest/legacypath.py:22`, `src/_pytest/logging.py:37`, `src/_pytest/mark/structures.py:29`, `src/_pytest/pytester.py:54`, `src/_pytest/python.py:59`, `src/_pytest/recwarn.py:27`, `src/_pytest/runner.py:29` and 2 more. In hindsight, 1 of 20 calls were not needed for the certificate: steps 1.

**Answer:** `{"target": {"kind": "def", "path": "src/_pytest/deprecated.py", "line": 153, "name": "check_ispytest", "detail": "def"}, "text": "src/_pytest/deprecated.py:153", "statements": ["src/_pytest/_code/code.py:47", "src/_pytest/cacheprovider.py:28", "src/_pytest/capture.py:37", "src/_pytest/config/argparsing.py:25", "src/_pytest/fixtures.py:58", "src/_pytest/legacypath.py:22", "src/_pytest/logging.py:37", "src/_pytest/mark/structures.py:29", "src/_pytest/pytester.py:54", "src/_pytest/python.py:59", "src/_pytest/recwarn.py:27", "src/_pytest/runner.py:29", "src/_pytest/subtests.py:29", "src/_pytest/tmpdir.py:30"], "count": 14}`  
**Stopped:** certificate after 20 calls