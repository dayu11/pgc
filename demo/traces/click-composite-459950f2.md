# click-composite-459950f2

**Repository:** click  
**Family:** composite  
**Seed:** 0, prior 93954b294cf7311e

## Task

In `tests/test_termui.py`, line 22 imports `BadParameter` from `click.exceptions`. Under the declared semantics, which definition does the module-level name `BadParameter` bound by this statement resolve to? Answer with `path:line`. Then list every module-level import statement in the snapshot that imports that definition (from-imports naming it, directly or with `as`, and star imports of modules that export it), as `path:line` entries.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

Nothing seen yet beyond the task text.

Chain: `tests/test_termui.py` is not yet closed for `BadParameter`.

Outstanding: close the namespace of `tests/test_termui.py` for `BadParameter`.

Next: outline `tests/test_termui.py`, because module `tests/test_termui.py` (task). I expect: a definition there ends the chain (about 80%); a capped outline means filtering by name (about 15%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (about 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `tests/test_termui.py` filtered to `BadParameter`, is expected to open more follow-up work. Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done; cap: outline `tests/test_termui.py` filtered to `BadParameter`.

**Call:** `symbols('tests/test_termui.py')`

**Response** (capped): outcome `cap`

```
module tests/test_termui.py lines=1985 dynamic=no all=none
1 import contextlib <- contextlib
2 import gc <- gc
3 import io <- io
4 import os <- os
5 import pathlib <- pathlib
6 import platform <- platform
7 import shlex <- shlex
8 import shutil <- shutil
9 import subprocess <- subprocess
10 import sys <- sys
11 import tempfile <- tempfile
12 import time <- time
13 from patch <- unittest.mock patch
15 import pytest <- pytest
17 import click <- click
18 import click <- click
19 from WIN <- click._compat WIN
20 from Editor <- click._termui_impl Editor
21 from UNSET <- click._utils UNSET
22 from BadParameter <- click.exceptions BadParameter
23 from MissingParameter <- click.exceptions MissingParameter
26 class FakeClock
37 def _create_progress
44 def test_progressbar_strip_regression
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
    "tests/test_termui.py",
    "BadParameter"
   ],
   "desc": "close the namespace of `tests/test_termui.py` for `BadParameter`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/test_termui.py')",
   "key": "[\"symbols\", [\"tests/test_termui.py\"]]",
   "v1": [
    113693994699,
    94869955040
   ],
   "v2": [
    3429841440589,
    2371748876000
   ],
   "p_cap": [
    134,
    1015
   ],
   "forecast": {
    "def": [
     353281,
     442540
    ],
    "reexport": [
     11453,
     442540
    ],
    "star": [
     881,
     442540
    ],
    "none": [
     2643,
     63220
    ],
    "cap": [
     134,
     1015
    ]
   },
   "serves": [
    [
     "bindings",
     "tests/test_termui.py",
     "BadParameter"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_termui.py', 'BadParameter')",
   "key": "[\"symbols\", [\"tests/test_termui.py\", \"BadParameter\"]]",
   "v1": [
    63082619,
    21437600
   ],
   "v2": [
    63082619,
    21437600
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
     "tests/test_termui.py",
     "BadParameter"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_termui.py')",
  "key": "[\"symbols\", [\"tests/test_termui.py\"]]",
  "provenance": "module `tests/test_termui.py` (task)",
  "v2": [
   3429841440589,
   2371748876000
  ]
 },
 "forecast": {
  "def": [
   353281,
   442540
  ],
  "reexport": [
   11453,
   442540
  ],
  "star": [
   881,
   442540
  ],
  "none": [
   2643,
   63220
  ],
  "cap": [
   134,
   1015
  ]
 },
 "plan": {
  "def": "done",
  "reexport": "continue",
  "star": "continue",
  "none": "done",
  "cap": "[\"symbols\", [\"tests/test_termui.py\", \"BadParameter\"]]"
 },
 "adherence": null,
 "facts": [
  {
   "kind": "outline",
   "step": 1,
   "path": "tests/test_termui.py",
   "filter": null,
   "header": {
    "lines": 1985,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_termui.py",
     "name": "contextlib",
     "line": 1,
     "kind": "import",
     "src": "contextlib",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_termui.py",
     "name": "gc",
     "line": 2,
     "kind": "import",
     "src": "gc",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_termui.py",
     "name": "io",
     "line": 3,
     "kind": "import",
     "src": "io",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_termui.py",
     "name": "os",
     "line": 4,
     "kind": "import",
     "src": "os",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_termui.py",
     "name": "pathlib",
     "line": 5,
     "kind": "import",
     "src": "pathlib",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_termui.py",
     "name": "platform",
     "line": 6,
     "kind": "import",
     "src": "platform",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_termui.py",
     "name": "shlex",
     "line": 7,
     "kind": "import",
     "src": "shlex",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_termui.py",
     "name": "shutil",
     "line": 8,
     "kind": "import",
     "src": "shutil",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_termui.py",
     "name": "subprocess",
     "line": 9,
     "kind": "import",
     "src": "subprocess",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_termui.py",
     "name": "sys",
     "line": 10,
     "kind": "import",
     "src": "sys",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_termui.py",
     "name": "tempfile",
     "line": 11,
     "kind": "import",
     "src": "tempfile",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_termui.py",
     "name": "time",
     "line": 12,
     "kind": "import",
     "src": "time",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_termui.py",
     "name": "patch",
     "line": 13,
     "kind": "from",
     "src": "unittest.mock",
     "src_name": "patch",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_termui.py",
     "name": "pytest",
     "line": 15,
     "kind": "import",
     "src": "pytest",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_termui.py",
     "name": "click",
     "line": 17,
     "kind": "import",
     "src": "click",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_termui.py",
     "name": "click",
     "line": 18,
     "kind": "import",
     "src": "click",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_termui.py",
     "name": "WIN",
     "line": 19,
     "kind": "from",
     "src": "click._compat",
     "src_name": "WIN",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_termui.py",
     "name": "Editor",
     "line": 20,
     "kind": "from",
     "src": "click._termui_impl",
     "src_name": "Editor",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_termui.py",
     "name": "UNSET",
     "line": 21,
     "kind": "from",
     "src": "click._utils",
     "src_name": "UNSET",
     "conditional": f
```
</details>

## Step 2

The outline of `tests/test_termui.py` has 40 bindings (capped, so this is only the start of the file); no `__all__`; no dynamic namespace tricks.

Chain: `tests/test_termui.py` is not yet closed for `BadParameter`.

Still to settle: close the namespace of `tests/test_termui.py` for `BadParameter`.

Next: outline `tests/test_termui.py` filtered to `BadParameter`, because module `tests/test_termui.py` (task), name `BadParameter` (task). I expect: a re-export continues the chain to its source (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a definition there ends the chain (under 5%); no binding but a star import means checking what that source exports (under 5%). Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done.

**Call:** `symbols('tests/test_termui.py', 'BadParameter')`

**Response**: outcome `reexport`

```
module tests/test_termui.py lines=1985 dynamic=no all=none
22 from BadParameter <- click.exceptions BadParameter
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "tests/test_termui.py",
    "BadParameter"
   ],
   "desc": "close the namespace of `tests/test_termui.py` for `BadParameter`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/test_termui.py', 'BadParameter')",
   "key": "[\"symbols\", [\"tests/test_termui.py\", \"BadParameter\"]]",
   "v1": [
    63082619,
    21437600
   ],
   "v2": [
    63082619,
    21437600
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
     "tests/test_termui.py",
     "BadParameter"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_termui.py', 'BadParameter')",
  "key": "[\"symbols\", [\"tests/test_termui.py\", \"BadParameter\"]]",
  "provenance": "module `tests/test_termui.py` (task), name `BadParameter` (task)",
  "v2": [
   63082619,
   21437600
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
  "planned": "[\"symbols\", [\"tests/test_termui.py\", \"BadParameter\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 2,
   "path": "tests/test_termui.py",
   "filter": "BadParameter",
   "header": {
    "lines": 1985,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_termui.py",
     "name": "BadParameter",
     "line": 22,
     "kind": "from",
     "src": "click.exceptions",
     "src_name": "BadParameter",
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
    "tests/test_termui.py",
    "BadParameter",
    "reexport",
    [
     "click.exceptions",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 3

In `tests/test_termui.py`, `BadParameter` has exactly one binding: line 22 imports it as `BadParameter` from `click.exceptions`. No dynamic namespace tricks, no `__all__`.

Chain: `tests/test_termui.py` takes `BadParameter` from `click.exceptions` (module not yet located).

Outstanding: locate the module `click.exceptions` imported by `tests/test_termui.py`.

Next: grep `def`/`class BadParameter` statements under `.`, because a `def`/`class BadParameter` statement would reveal the module file; `BadParameter` task. I expect: hits under the cap (about 95%); a capped result (under 5%); no hits (under 5%). The alternative, list `.`, is more likely to hit the cap (about 20% against under 5%). Plan by outcome: zero: list `.`; mid: outline each module that appears; cap: list `.`.

**Call:** `grep('^\\s*(?:async\\s+)?(?:def|class)\\s+BadParameter\\b', '.')`

**Response**: outcome `mid`

```
src/click/exceptions.py:114:class BadParameter(UsageError):
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_termui.py",
    "click.exceptions"
   ],
   "desc": "locate the module `click.exceptions` imported by `tests/test_termui.py`"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+BadParameter\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+BadParameter\\\\b\", \".\"]]",
   "v1": [
    9367,
    4431
   ],
   "v2": [
    84725,
    39879
   ],
   "p_cap": [
    1,
    42
   ],
   "forecast": {
    "zero": [
     1,
     42
    ],
    "mid": [
     20,
     21
    ],
    "cap": [
     1,
     42
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_termui.py",
     "click.exceptions"
    ]
   ]
  },
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    4346,
    1899
   ],
   "v2": [
    91688,
    39879
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
     "tests/test_termui.py",
     "click.exceptions"
    ]
   ]
  },
  {
   "call": "symbols('click/exceptions.py', 'BadParameter')",
   "key": "[\"symbols\", [\"click/exceptions.py\", \"BadParameter\"]]",
   "v1": [
    602168889551,
    257971503360
   ],
   "v2": [
    38427253237777,
    16252204711680
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     1215431,
     3610080
    ],
    "reexport": [
     39403,
     3610080
    ],
    "star": [
     3031,
     3610080
    ],
    "none": [
     21217,
     1203360
    ],
    "missing": [
     5249,
     8280
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_termui.py",
     "click.exceptions"
    ]
   ]
  },
  {
   "call": "symbols('click/exceptions/__init__.py', 'BadParameter')",
   "key": "[\"symbols\", [\"click/exceptions/__init__.py\", \"BadParameter\"]]",
   "v1": [
    784335349,
    258567840
   ],
   "v2": [
    16714089853,
    5429924640
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     5467,
     612720
    ],
    "reexport": [
     497,
     13616
    ],
    "star": [
     497,
     612720
    ],
    "none": [
     8449,
     612720
    ],
    "missing": [
     7783,
     8280
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_termui.py",
     "click.exceptions"
    ]
   ]
  }
 ],
 "choice": {
  "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+BadParameter\\\\b', '.')",
  "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+BadParameter\\\\b\", \".\"]]",
  "provenance": "a `def`/`class BadParameter` statement would reveal the module file; `BadParameter` task",
  "v2": [
   84725,
   39879
  ]
 },
 "forecast": {
  "zero": [
   1,
   42
  ],
  "mid": [
   20,
   21
  ],
  "cap": [
   1,
   42
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
   "pattern": "^\\s*(?:async\\s+)?(?:def|class)\\s+BadParameter\\b",
   "scope": ".",
   "hits": [
    [
     "src/click/exceptions.py",
     114
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "chain": [
   [
    "tests/test_termui.py",
    "BadParameter",
    "reexport",
    [
     "click.exceptions",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 4

The grep under `.` returned 1 lines, under the cap, so these are all of them: `src/click/exceptions.py`.

Chain: `tests/test_termui.py` takes `BadParameter` from `click.exceptions` (module not yet located).

Outstanding: locate the module `click.exceptions` imported by `tests/test_termui.py`.

Next: list `.`, because `click.exceptions` imported by `tests/test_termui.py` should live under `.`. I expect: a complete listing settles which files exist (about 80%); a capped listing settles nothing (about 20%). The alternative, outline `click/exceptions.py` filtered to `BadParameter`, costs more in expectation. Plan by outcome: complete: outline the module it reveals; cap: outline `click/exceptions.py` filtered to `BadParameter`.

**Call:** `ls('.')`

**Response**: outcome `complete`

```
.devcontainer/
.github/
.pre-commit-config.yaml
.readthedocs.yaml
CHANGES.md
LICENSE.txt
README.md
docs/
examples/
pyproject.toml
src/
tests/
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_termui.py",
    "click.exceptions"
   ],
   "desc": "locate the module `click.exceptions` imported by `tests/test_termui.py`"
  }
 ],
 "candidates": [
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    4346,
    1899
   ],
   "v2": [
    2725848990671,
    1160871765120
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
     "tests/test_termui.py",
     "click.exceptions"
    ]
   ]
  },
  {
   "call": "symbols('click/exceptions.py', 'BadParameter')",
   "key": "[\"symbols\", [\"click/exceptions.py\", \"BadParameter\"]]",
   "v1": [
    602168889551,
    257971503360
   ],
   "v2": [
    3447957282001,
    1393046118144
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     1215431,
     3610080
    ],
    "reexport": [
     39403,
     3610080
    ],
    "star": [
     3031,
     3610080
    ],
    "none": [
     21217,
     1203360
    ],
    "missing": [
     5249,
     8280
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_termui.py",
     "click.exceptions"
    ]
   ]
  },
  {
   "call": "symbols('click/exceptions/__init__.py', 'BadParameter')",
   "key": "[\"symbols\", [\"click/exceptions/__init__.py\", \"BadParameter\"]]",
   "v1": [
    784335349,
    258567840
   ],
   "v2": [
    7545113189,
    2327110560
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     5467,
     612720
    ],
    "reexport": [
     497,
     13616
    ],
    "star": [
     497,
     612720
    ],
    "none": [
     8449,
     612720
    ],
    "missing": [
     7783,
     8280
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_termui.py",
     "click.exceptions"
    ]
   ]
  }
 ],
 "choice": {
  "call": "ls('.')",
  "key": "[\"ls\", [\".\"]]",
  "provenance": "`click.exceptions` imported by `tests/test_termui.py` should live under `.`",
  "v2": [
   2725848990671,
   1160871765120
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
  "cap": "[\"symbols\", [\"click/exceptions.py\", \"BadParameter\"]]"
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
    ".devcontainer/",
    ".github/",
    ".pre-commit-config.yaml",
    ".readthedocs.yaml",
    "CHANGES.md",
    "LICENSE.txt",
    "README.md",
    "docs/",
    "examples/",
    "pyproject.toml",
    "src/",
    "tests/"
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "chain": [
   [
    "tests/test_termui.py",
    "BadParameter",
    "reexport",
    [
     "click.exceptions",
     "src/click/exceptions.py"
    ]
   ],
   [
    "src/click/exceptions.py",
    "BadParameter",
    "open",
    null
   ]
  ]
 }
}
```
</details>

## Step 5

`.` lists 12 entries (complete): `.devcontainer/`, `.github/`, `docs/`, `examples/`, `src/`, `tests/`.

Chain: `tests/test_termui.py` takes `BadParameter` from `click.exceptions` (`src/click/exceptions.py`); `src/click/exceptions.py` is not yet closed for `BadParameter`.

Still to settle: close the namespace of `src/click/exceptions.py` for `BadParameter`.

Next: outline `src/click/exceptions.py` filtered to `BadParameter`, because module `src/click/exceptions.py` (step 3), name `BadParameter` (task). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `src/click/exceptions.py`, is more likely to hit the cap (about 15% against under 5%). Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done.

**Call:** `symbols('src/click/exceptions.py', 'BadParameter')`

**Response**: outcome `def`

```
module src/click/exceptions.py lines=379 dynamic=no all=none
114 class BadParameter
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/click/exceptions.py",
    "BadParameter"
   ],
   "desc": "close the namespace of `src/click/exceptions.py` for `BadParameter`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/click/exceptions.py', 'BadParameter')",
   "key": "[\"symbols\", [\"src/click/exceptions.py\", \"BadParameter\"]]",
   "v1": [
    22771803,
    21437600
   ],
   "v2": [
    22771803,
    21437600
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
     "src/click/exceptions.py",
     "BadParameter"
    ]
   ]
  },
  {
   "call": "symbols('src/click/exceptions.py')",
   "key": "[\"symbols\", [\"src/click/exceptions.py\"]]",
   "v1": [
    113693994699,
    94869955040
   ],
   "v2": [
    2841061662093,
    2371748876000
   ],
   "p_cap": [
    134,
    1015
   ],
   "forecast": {
    "def": [
     353281,
     442540
    ],
    "reexport": [
     11453,
     442540
    ],
    "star": [
     881,
     442540
    ],
    "none": [
     2643,
     63220
    ],
    "cap": [
     134,
     1015
    ]
   },
   "serves": [
    [
     "bindings",
     "src/click/exceptions.py",
     "BadParameter"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/click/exceptions.py', 'BadParameter')",
  "key": "[\"symbols\", [\"src/click/exceptions.py\", \"BadParameter\"]]",
  "provenance": "module `src/click/exceptions.py` (step 3), name `BadParameter` (task)",
  "v2": [
   22771803,
   21437600
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
   "path": "src/click/exceptions.py",
   "filter": "BadParameter",
   "header": {
    "lines": 379,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/click/exceptions.py",
     "name": "BadParameter",
     "line": 114,
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
    "tests/test_termui.py",
    "BadParameter",
    "reexport",
    [
     "click.exceptions",
     "src/click/exceptions.py"
    ]
   ],
   [
    "src/click/exceptions.py",
    "BadParameter",
    "class",
    114
   ]
  ]
 }
}
```
</details>

## Step 6

In `src/click/exceptions.py`, `BadParameter` has exactly one binding: a class at line 114. No dynamic namespace tricks, no `__all__`. This is not the branch I planned for that outcome; the open items changed more than expected.

Candidate modules so far: 0; statements confirmed: 0, ruled out: 0, modules with no such import: 0, pending: 0. import coverage open at `.`; star coverage open at `.`.

Open: cover `.` for import lines; cover `.` for star lines.

Next: grep from-imports naming `BadParameter` under `.`, because import lines naming `BadParameter` under `.` (derived). I expect: no hits (about 60%); hits under the cap (about 35%); a capped result (about 5%). The alternative, grep star imports under `.`, is expected to open more follow-up work. Plan by outcome: zero: grep star imports under `.`; mid: grep star imports under `.`; cap: grep star imports under `.`.

**Call:** `grep('^\\s*from\\s+\\S+\\s+import\\s+.*\\bBadParameter\\b|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*BadParameter\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$', '.')`

**Response**: outcome `mid`

```
src/click/__init__.py:33:from .exceptions import BadParameter as BadParameter
src/click/core.py:27:from .exceptions import BadParameter
src/click/types.py:17:from .exceptions import BadParameter
tests/test_termui.py:22:from click.exceptions import BadParameter
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
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bBadParameter\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*BadParameter\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bBadParameter\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*BadParameter\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
   "v1": [
    29722001089,
    4698822933
   ],
   "v2": [
    29722001089,
    4698822933
   ],
   "p_cap": [
    1,
    29
   ],
   "forecast": {
    "zero": [
     18,
     29
    ],
    "mid": [
     10,
     29
    ],
    "cap": [
     1,
     29
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
    29722001089,
    4698822933
   ],
   "v2": [
    29722001089,
    4698822933
   ],
   "p_cap": [
    2,
    33
   ],
   "forecast": {
    "zero": [
     16,
     33
    ],
    "mid": [
     5,
     11
    ],
    "cap": [
     2,
     33
    ]
   },
   "serves": [
    [
     "cover",
     "STAR",
     "."
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bBadParameter\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*BadParameter\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bBadParameter\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*BadParameter\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
   "v1": [
    7495554769,
    990173415
   ],
   "v2": [
    7495554769,
    990173415
   ],
   "p_cap": [
    4,
    35
   ],
   "forecast": {
    "zero": [
     8,
     35
    ],
    "mid": [
     23,
     35
    ],
    "cap": [
     4,
     35
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
  }
 ],
 "choice": {
  "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bBadParameter\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*BadParameter\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
  "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bBadParameter\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*BadParameter\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
  "provenance": "import lines naming `BadParameter` under `.` (derived)",
  "v2": [
   29722001089,
   4698822933
  ]
 },
 "forecast": {
  "zero": [
   18,
   29
  ],
  "mid": [
   10,
   29
  ],
  "cap": [
   1,
   29
  ]
 },
 "plan": {
  "zero": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+\\\\*\", \".\"]]",
  "mid": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+\\\\*\", \".\"]]",
  "cap": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+\\\\*\", \".\"]]"
 },
 "adherence": {
  "planned": "done",
  "status": "deviated"
 },
 "facts": [
  {
   "kind": "grep",
   "step": 6,
   "pattern": "^\\s*from\\s+\\S+\\s+import\\s+.*\\bBadParameter\\b|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*BadParameter\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$",
   "scope": ".",
   "hits": [
    [
     "src/click/__init__.py",
     33
    ],
    [
     "src/click/core.py",
     27
    ],
    [
     "src/click/types.py",
     17
    ],
    [
     "tests/test_termui.py",
     22
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "src/click/__init__.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "src/click/core.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "src/click/types.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_termui.py",
    22,
    "in",
    "`click.exceptions` resolves `BadParameter` to the target"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": [
    [
     "grep",
     "."
    ]
   ]
  }
 }
}
```
</details>

## Step 7

The grep under `.` returned 4 lines, under the cap, so these are all of them: `src/click/__init__.py`, `src/click/core.py`, `src/click/types.py`, `tests/test_termui.py`.

Candidate modules so far: 4; statements confirmed: 1, ruled out: 0, modules with no such import: 0, pending: 3. import coverage complete; star coverage open at `.`.

Open: cover `.` for star lines; outline `src/click/__init__.py` for its `BadParameter` imports; outline `src/click/core.py` for its `BadParameter` imports; outline `src/click/types.py` for its `BadParameter` imports.

Next: grep star imports under `.`, because star lines naming `BadParameter` under `.` (derived). I expect: no hits (about 50%); hits under the cap (about 45%); a capped result (about 5%). The alternative, outline `src/click/__init__.py` filtered to `BadParameter`, scores the same; the seed broke the tie. Plan by outcome: zero: outline `src/click/__init__.py` filtered to `BadParameter`; mid: outline `src/click/__init__.py` filtered to `BadParameter`; cap: outline `src/click/__init__.py` filtered to `BadParameter`.

**Call:** `grep('^\\s*from\\s+\\S+\\s+import\\s+\\*', '.')`

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
    "STAR",
    "."
   ],
   "desc": "cover `.` for star lines"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/__init__.py",
    "BadParameter"
   ],
   "desc": "outline `src/click/__init__.py` for its `BadParameter` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/core.py",
    "BadParameter"
   ],
   "desc": "outline `src/click/core.py` for its `BadParameter` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/types.py",
    "BadParameter"
   ],
   "desc": "outline `src/click/types.py` for its `BadParameter` imports"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+\\\\*', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+\\\\*\", \".\"]]",
   "v1": [
    172656094,
    18003153
   ],
   "v2": [
    8650807853,
    900157650
   ],
   "p_cap": [
    2,
    33
   ],
   "forecast": {
    "zero": [
     16,
     33
    ],
    "mid": [
     5,
     11
    ],
    "cap": [
     2,
     33
    ]
   },
   "serves": [
    [
     "cover",
     "STAR",
     "."
    ]
   ]
  },
  {
   "call": "symbols('src/click/__init__.py', 'BadParameter')",
   "key": "[\"symbols\", [\"src/click/__init__.py\", \"BadParameter\"]]",
   "v1": [
    8650807853,
    900157650
   ],
   "v2": [
    8650807853,
    900157650
   ],
   "p_cap": [
    1,
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
     "src/click/__init__.py",
     "BadParameter"
    ]
   ]
  },
  {
   "call": "symbols('src/click/core.py', 'BadParameter')",
   "key": "[\"symbols\", [\"src/click/core.py\", \"BadParameter\"]]",
   "v1": [
    8650807853,
    900157650
   ],
   "v2": [
    8650807853,
    900157650
   ],
   "p_cap": [
    1,
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
     "src/click/core.py",
     "BadParameter"
    ]
   ]
  },
  {
   "call": "symbols('src/click/types.py', 'BadParameter')",
   "key": "[\"symbols\", [\"src/click/types.py\", \"BadParameter\"]]",
   "v1": [
    8650807853,
    900157650
   ],
   "v2": [
    8650807853,
    900157650
   ],
   "p_cap": [
    1,
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
     "src/click/types.py",
     "BadParameter"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bBadParameter\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*BadParameter\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bBadParameter\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*BadParameter\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
   "v1": [
    12512120554,
    990173415
   ],
   "v2": [
    125319240223,
    9901734150
   ],
   "p_cap": [
    4,
    35
   ],
   "forecast": {
    "zero": [
     8,
     35
    ],
    "mid": [
     23,
     35
    ],
    "cap": [
     4,
     35
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
  "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+\\\\*', '.')",
  "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+\\\\*\", \".\"]]",
  "provenance": "star lines naming `BadParameter` under `.` (derived)",
  "v2": [
   8650807853,
   900157650
  ]
 },
 "forecast": {
  "zero": [
   16,
   33
  ],
  "mid": [
   5,
   11
  ],
  "cap": [
   2,
   33
  ]
 },
 "plan": {
  "zero": "[\"symbols\", [\"src/click/__init__.py\", \"BadParameter\"]]",
  "mid": "[\"symbols\", [\"src/click/__init__.py\", \"BadParameter\"]]",
  "cap": "[\"symbols\", [\"src/click/__init__.py\", \"BadParameter\"]]"
 },
 "adherence": {
  "planned": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+\\\\*\", \".\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "grep",
   "step": 7,
   "pattern": "^\\s*from\\s+\\S+\\s+import\\s+\\*",
   "scope": ".",
   "hits": [],
   "capped": false
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "src/click/__init__.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "src/click/core.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "src/click/types.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_termui.py",
    22,
    "in",
    "`click.exceptions` resolves `BadParameter` to the target"
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

## Step 8

The grep under `.` returned nothing, and it was not capped, so there are no such lines there.

Candidate modules so far: 4; statements confirmed: 1, ruled out: 0, modules with no such import: 0, pending: 3. import coverage complete; star coverage complete.

Outstanding: outline `src/click/__init__.py` for its `BadParameter` imports; outline `src/click/core.py` for its `BadParameter` imports; outline `src/click/types.py` for its `BadParameter` imports.

Next: outline `src/click/__init__.py` filtered to `BadParameter`, because `src/click/__init__.py` had a matching line (step 6); its outline names every `BadParameter` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/click/core.py` filtered to `BadParameter`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/click/core.py` filtered to `BadParameter`; cap: outline `src/click/core.py` filtered to `BadParameter`.

**Call:** `symbols('src/click/__init__.py', 'BadParameter')`

**Response**: outcome `ok`

```
module src/click/__init__.py lines=145 dynamic=yes all=none
33 from BadParameter <- .exceptions BadParameter
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/__init__.py",
    "BadParameter"
   ],
   "desc": "outline `src/click/__init__.py` for its `BadParameter` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/core.py",
    "BadParameter"
   ],
   "desc": "outline `src/click/core.py` for its `BadParameter` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/types.py",
    "BadParameter"
   ],
   "desc": "outline `src/click/types.py` for its `BadParameter` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/click/__init__.py', 'BadParameter')",
   "key": "[\"symbols\", [\"src/click/__init__.py\", \"BadParameter\"]]",
   "v1": [
    53661,
    10550
   ],
   "v2": [
    26936,
    5275
   ],
   "p_cap": [
    1,
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
     "src/click/__init__.py",
     "BadParameter"
    ]
   ]
  },
  {
   "call": "symbols('src/click/core.py', 'BadParameter')",
   "key": "[\"symbols\", [\"src/click/core.py\", \"BadParameter\"]]",
   "v1": [
    53661,
    10550
   ],
   "v2": [
    26936,
    5275
   ],
   "p_cap": [
    1,
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
     "src/click/core.py",
     "BadParameter"
    ]
   ]
  },
  {
   "call": "symbols('src/click/types.py', 'BadParameter')",
   "key": "[\"symbols\", [\"src/click/types.py\", \"BadParameter\"]]",
   "v1": [
    53661,
    10550
   ],
   "v2": [
    26936,
    5275
   ],
   "p_cap": [
    1,
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
     "src/click/types.py",
     "BadParameter"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/click/__init__.py', 'BadParameter')",
  "key": "[\"symbols\", [\"src/click/__init__.py\", \"BadParameter\"]]",
  "provenance": "`src/click/__init__.py` had a matching line (step 6); its outline names every `BadParameter` import exactly",
  "v2": [
   26936,
   5275
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
  "ok": "[\"symbols\", [\"src/click/core.py\", \"BadParameter\"]]",
  "cap": "[\"symbols\", [\"src/click/core.py\", \"BadParameter\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"src/click/__init__.py\", \"BadParameter\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 8,
   "path": "src/click/__init__.py",
   "filter": "BadParameter",
   "header": {
    "lines": 145,
    "dynamic": true,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/click/__init__.py",
     "name": "BadParameter",
     "line": 33,
     "kind": "from",
     "src": ".exceptions",
     "src_name": "BadParameter",
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
    "src/click/__init__.py",
    33,
    "in",
    "`.exceptions` resolves `BadParameter` to the target"
   ],
   [
    "src/click/core.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "src/click/types.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_termui.py",
    22,
    "in",
    "`click.exceptions` resolves `BadParameter` to the target"
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

## Step 9

In `src/click/__init__.py`, `BadParameter` has exactly one binding: line 33 imports it as `BadParameter` from `.exceptions`. It uses dynamic namespace tricks, no `__all__`.

Candidate modules so far: 4; statements confirmed: 2, ruled out: 0, modules with no such import: 0, pending: 2. import coverage complete; star coverage complete.

Still to settle: outline `src/click/core.py` for its `BadParameter` imports; outline `src/click/types.py` for its `BadParameter` imports.

Next: outline `src/click/core.py` filtered to `BadParameter`, because `src/click/core.py` had a matching line (step 6); its outline names every `BadParameter` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/click/types.py` filtered to `BadParameter`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/click/types.py` filtered to `BadParameter`; cap: outline `src/click/types.py` filtered to `BadParameter`.

**Call:** `symbols('src/click/core.py', 'BadParameter')`

**Response**: outcome `ok`

```
module src/click/core.py lines=3800 dynamic=yes all=none
27 from BadParameter <- .exceptions BadParameter
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/core.py",
    "BadParameter"
   ],
   "desc": "outline `src/click/core.py` for its `BadParameter` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/types.py",
    "BadParameter"
   ],
   "desc": "outline `src/click/types.py` for its `BadParameter` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/click/core.py', 'BadParameter')",
   "key": "[\"symbols\", [\"src/click/core.py\", \"BadParameter\"]]",
   "v1": [
    107533,
    31650
   ],
   "v2": [
    54083,
    15825
   ],
   "p_cap": [
    1,
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
     "src/click/core.py",
     "BadParameter"
    ]
   ]
  },
  {
   "call": "symbols('src/click/types.py', 'BadParameter')",
   "key": "[\"symbols\", [\"src/click/types.py\", \"BadParameter\"]]",
   "v1": [
    107533,
    31650
   ],
   "v2": [
    54083,
    15825
   ],
   "p_cap": [
    1,
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
     "src/click/types.py",
     "BadParameter"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/click/core.py', 'BadParameter')",
  "key": "[\"symbols\", [\"src/click/core.py\", \"BadParameter\"]]",
  "provenance": "`src/click/core.py` had a matching line (step 6); its outline names every `BadParameter` import exactly",
  "v2": [
   54083,
   15825
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
  "ok": "[\"symbols\", [\"src/click/types.py\", \"BadParameter\"]]",
  "cap": "[\"symbols\", [\"src/click/types.py\", \"BadParameter\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"src/click/core.py\", \"BadParameter\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 9,
   "path": "src/click/core.py",
   "filter": "BadParameter",
   "header": {
    "lines": 3800,
    "dynamic": true,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/click/core.py",
     "name": "BadParameter",
     "line": 27,
     "kind": "from",
     "src": ".exceptions",
     "src_name": "BadParameter",
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
    "src/click/__init__.py",
    33,
    "in",
    "`.exceptions` resolves `BadParameter` to the target"
   ],
   [
    "src/click/core.py",
    27,
    "in",
    "`.exceptions` resolves `BadParameter` to the target"
   ],
   [
    "src/click/types.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_termui.py",
    22,
    "in",
    "`click.exceptions` resolves `BadParameter` to the target"
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

## Step 10

In `src/click/core.py`, `BadParameter` has exactly one binding: line 27 imports it as `BadParameter` from `.exceptions`. It uses dynamic namespace tricks, no `__all__`.

Candidate modules so far: 4; statements confirmed: 3, ruled out: 0, modules with no such import: 0, pending: 1. import coverage complete; star coverage complete.

Still to settle: outline `src/click/types.py` for its `BadParameter` imports.

Next: outline `src/click/types.py` filtered to `BadParameter`, because `src/click/types.py` had a matching line (step 6); its outline names every `BadParameter` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). Plan by outcome: ok: resolve the sources its import statements name; cap: work the items it opens.

**Call:** `symbols('src/click/types.py', 'BadParameter')`

**Response**: outcome `ok`

```
module src/click/types.py lines=1423 dynamic=no all=none
17 from BadParameter <- .exceptions BadParameter
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/types.py",
    "BadParameter"
   ],
   "desc": "outline `src/click/types.py` for its `BadParameter` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/click/types.py', 'BadParameter')",
   "key": "[\"symbols\", [\"src/click/types.py\", \"BadParameter\"]]",
   "v1": [
    54083,
    31650
   ],
   "v2": [
    54083,
    31650
   ],
   "p_cap": [
    1,
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
     "src/click/types.py",
     "BadParameter"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/click/types.py', 'BadParameter')",
  "key": "[\"symbols\", [\"src/click/types.py\", \"BadParameter\"]]",
  "provenance": "`src/click/types.py` had a matching line (step 6); its outline names every `BadParameter` import exactly",
  "v2": [
   54083,
   31650
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
  "planned": "[\"symbols\", [\"src/click/types.py\", \"BadParameter\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 10,
   "path": "src/click/types.py",
   "filter": "BadParameter",
   "header": {
    "lines": 1423,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/click/types.py",
     "name": "BadParameter",
     "line": 17,
     "kind": "from",
     "src": ".exceptions",
     "src_name": "BadParameter",
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
    "src/click/__init__.py",
    33,
    "in",
    "`.exceptions` resolves `BadParameter` to the target"
   ],
   [
    "src/click/core.py",
    27,
    "in",
    "`.exceptions` resolves `BadParameter` to the target"
   ],
   [
    "src/click/types.py",
    17,
    "in",
    "`.exceptions` resolves `BadParameter` to the target"
   ],
   [
    "tests/test_termui.py",
    22,
    "in",
    "`click.exceptions` resolves `BadParameter` to the target"
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

Certificate complete. 4 import statements import this definition: `src/click/__init__.py:33`, `src/click/core.py:27`, `src/click/types.py:17`, `tests/test_termui.py:22`. In hindsight, 1 of 10 calls were not needed for the certificate: steps 1.

**Answer:** `{"target": {"kind": "def", "path": "src/click/exceptions.py", "line": 114, "name": "BadParameter", "detail": "class"}, "text": "src/click/exceptions.py:114", "statements": ["src/click/__init__.py:33", "src/click/core.py:27", "src/click/types.py:17", "tests/test_termui.py:22"], "count": 4}`  
**Stopped:** certificate after 10 calls