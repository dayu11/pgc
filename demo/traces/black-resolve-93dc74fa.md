# black-resolve-93dc74fa

**Repository:** black  
**Family:** resolve  
**Seed:** 0, prior 55c929686ca1d56a

## Task

In `tests/test_ipynb.py`, line 12 imports `main` from `black`. Under the declared semantics, which definition does the module-level name `main` bound by this statement resolve to? Answer with `path:line`.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

Nothing seen yet beyond the task text.

Chain: `tests/test_ipynb.py` is not yet closed for `main`.

Outstanding: close the namespace of `tests/test_ipynb.py` for `main`.

Next: outline `tests/test_ipynb.py`, because module `tests/test_ipynb.py` (task). I expect: a definition there ends the chain (about 80%); a capped outline means filtering by name (about 15%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `tests/test_ipynb.py` filtered to `main`, is expected to open more follow-up work. Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done; cap: outline `tests/test_ipynb.py` filtered to `main`.

**Call:** `symbols('tests/test_ipynb.py')`

**Response** (capped): outcome `cap`

```
module tests/test_ipynb.py lines=571 dynamic=no all=none
1 import contextlib <- contextlib
2 import pathlib <- pathlib
3 import re <- re
4 from AbstractContextManager <- contextlib AbstractContextManager
5 from does_not_raise <- contextlib ExitStack
6 from replace <- dataclasses replace
8 import pytest <- pytest
9 from CliRunner <- click.testing CliRunner
10 from MonkeyPatch <- pytest MonkeyPatch
12 from Mode <- black Mode
12 from NothingChanged <- black NothingChanged
12 from format_cell <- black format_cell
12 from format_file_contents <- black format_file_contents
12 from format_file_in_place <- black format_file_in_place
12 from main <- black main
20 from Replacement <- black.handle_ipynb_magics Replacement
20 from create_token <- black.handle_ipynb_magics create_token
20 from jupyter_dependencies_are_installed <- black.handle_ipynb_magics jupyter_dependencies_are_installed
20 from unmask_cell <- black.handle_ipynb_magics unmask_cell
26 from DATA_DIR <- tests.util DATA_DIR
26 from get_case_path <- tests.util get_case_path
26 from read_jupyter_notebook <- tests.util read_jupyter_notebook
29 import IPython <- IPython
30 assign pytestmark
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
    "tests/test_ipynb.py",
    "main"
   ],
   "desc": "close the namespace of `tests/test_ipynb.py` for `main`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/test_ipynb.py')",
   "key": "[\"symbols\", [\"tests/test_ipynb.py\"]]",
   "v1": [
    966997049,
    815833332
   ],
   "v2": [
    120339495149,
    81583333200
   ],
   "p_cap": [
    29,
    188
   ],
   "forecast": {
    "def": [
     7579,
     9588
    ],
    "reexport": [
     53,
     4794
    ],
    "star": [
     53,
     28764
    ],
    "none": [
     1219,
     28764
    ],
    "cap": [
     29,
     188
    ]
   },
   "serves": [
    [
     "bindings",
     "tests/test_ipynb.py",
     "main"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_ipynb.py', 'main')",
   "key": "[\"symbols\", [\"tests/test_ipynb.py\", \"main\"]]",
   "v1": [
    8252027,
    2836300
   ],
   "v2": [
    8252027,
    2836300
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
     "tests/test_ipynb.py",
     "main"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_ipynb.py')",
  "key": "[\"symbols\", [\"tests/test_ipynb.py\"]]",
  "provenance": "module `tests/test_ipynb.py` (task)",
  "v2": [
   120339495149,
   81583333200
  ]
 },
 "forecast": {
  "def": [
   7579,
   9588
  ],
  "reexport": [
   53,
   4794
  ],
  "star": [
   53,
   28764
  ],
  "none": [
   1219,
   28764
  ],
  "cap": [
   29,
   188
  ]
 },
 "plan": {
  "def": "done",
  "reexport": "continue",
  "star": "continue",
  "none": "done",
  "cap": "[\"symbols\", [\"tests/test_ipynb.py\", \"main\"]]"
 },
 "adherence": null,
 "facts": [
  {
   "kind": "outline",
   "step": 1,
   "path": "tests/test_ipynb.py",
   "filter": null,
   "header": {
    "lines": 571,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_ipynb.py",
     "name": "contextlib",
     "line": 1,
     "kind": "import",
     "src": "contextlib",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_ipynb.py",
     "name": "pathlib",
     "line": 2,
     "kind": "import",
     "src": "pathlib",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_ipynb.py",
     "name": "re",
     "line": 3,
     "kind": "import",
     "src": "re",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_ipynb.py",
     "name": "AbstractContextManager",
     "line": 4,
     "kind": "from",
     "src": "contextlib",
     "src_name": "AbstractContextManager",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_ipynb.py",
     "name": "does_not_raise",
     "line": 5,
     "kind": "from",
     "src": "contextlib",
     "src_name": "ExitStack",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_ipynb.py",
     "name": "replace",
     "line": 6,
     "kind": "from",
     "src": "dataclasses",
     "src_name": "replace",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_ipynb.py",
     "name": "pytest",
     "line": 8,
     "kind": "import",
     "src": "pytest",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_ipynb.py",
     "name": "CliRunner",
     "line": 9,
     "kind": "from",
     "src": "click.testing",
     "src_name": "CliRunner",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_ipynb.py",
     "name": "MonkeyPatch",
     "line": 10,
     "kind": "from",
     "src": "pytest",
     "src_name": "MonkeyPatch",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_ipynb.py",
     "name": "Mode",
     "line": 12,
     "kind": "from",
     "src": "black",
     "src_name": "Mode",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_ipynb.py",
     "name": "NothingChanged",
     "line": 12,
     "kind": "from",
     "src": "black",
     "src_name": "NothingChanged",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_ipynb.py",
     "name": "format_cell",
     "line": 12,
     "kind": "from",
     "src": "black",
     "src_name": "format_cell",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_ipynb.py",
     "name": "format_file_contents",
     "line": 12,
     "kind": "from",
     "src": "black",
     "src_name": "format_file_contents",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_ipynb.py",
     "name": "format_file_in_place",
     "line": 12,
     "kind": "from",
     "src": "black",
     "src_name": "format_file_in_place",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_ipynb.py",
     "name": "main",
     "line": 12,
     "kind": "from",
     "src": "black",
     "src_name": "main",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_ipynb.py",
     "name": "Replacement",
     "line": 20,
     "kind": "from",
     "src": "black.handle_ipynb_magics",
     "src_name": "Replacement",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_ipynb.py",
     "name": "create_token",
     "line": 20,
     "kind": "from",
     "src": "black.handle_ipynb_magics",
     "src_name": "create_token",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_ipynb.py",
     "name": "jupyter_dependencies_are_installed",
     "line": 20,
     "kind": "from",
     "src": "black.handle_ipynb_magics",
     "src_name": "jupyter_dependencies_are_installed",
     "conditional": false,
     "col": 0
    },
    {

```
</details>

## Step 2

The outline of `tests/test_ipynb.py` has 40 bindings (capped, so this is only the start of the file); no `__all__`; no dynamic namespace tricks.

Chain: `tests/test_ipynb.py` is not yet closed for `main`.

Still to settle: close the namespace of `tests/test_ipynb.py` for `main`.

Next: outline `tests/test_ipynb.py` filtered to `main`, because module `tests/test_ipynb.py` (task), name `main` (task). I expect: a re-export continues the chain to its source (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a definition there ends the chain (under 5%); no binding but a star import means checking what that source exports (under 5%). Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done.

**Call:** `symbols('tests/test_ipynb.py', 'main')`

**Response**: outcome `reexport`

```
module tests/test_ipynb.py lines=571 dynamic=no all=none
12 from main <- black main
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "tests/test_ipynb.py",
    "main"
   ],
   "desc": "close the namespace of `tests/test_ipynb.py` for `main`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/test_ipynb.py', 'main')",
   "key": "[\"symbols\", [\"tests/test_ipynb.py\", \"main\"]]",
   "v1": [
    8252027,
    2836300
   ],
   "v2": [
    8252027,
    2836300
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
     "tests/test_ipynb.py",
     "main"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_ipynb.py', 'main')",
  "key": "[\"symbols\", [\"tests/test_ipynb.py\", \"main\"]]",
  "provenance": "module `tests/test_ipynb.py` (task), name `main` (task)",
  "v2": [
   8252027,
   2836300
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
  "planned": "[\"symbols\", [\"tests/test_ipynb.py\", \"main\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 2,
   "path": "tests/test_ipynb.py",
   "filter": "main",
   "header": {
    "lines": 571,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_ipynb.py",
     "name": "main",
     "line": 12,
     "kind": "from",
     "src": "black",
     "src_name": "main",
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
    "tests/test_ipynb.py",
    "main",
    "reexport",
    [
     "black",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 3

In `tests/test_ipynb.py`, `main` has exactly one binding: line 12 imports it as `main` from `black`. No dynamic namespace tricks, no `__all__`.

Chain: `tests/test_ipynb.py` takes `main` from `black` (module not yet located).

Outstanding: locate the module `black` imported by `tests/test_ipynb.py`.

Next: list `.`, because `black` imported by `tests/test_ipynb.py` should live under `.`. I expect: a complete listing settles which files exist (about 80%); a capped listing settles nothing (about 20%). The alternative, outline `black.py` filtered to `main`, costs more in expectation. Plan by outcome: complete: outline the module it reveals; cap: outline `black.py` filtered to `main`.

**Call:** `ls('.')`

**Response**: outcome `complete`

```
.git_archival.txt
.github/
.pre-commit-config.yaml
.pre-commit-hooks.yaml
.prettierrc.yaml
.readthedocs.yaml
AUTHORS.md
CHANGES.md
CONTRIBUTING.md
README.md
SECURITY.md
action.yml
action/
docs/
profiling/
pyproject.toml
scripts/
src/
tests/
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
    "tests/test_ipynb.py",
    "black"
   ],
   "desc": "locate the module `black` imported by `tests/test_ipynb.py`"
  }
 ],
 "candidates": [
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    4583,
    2034
   ],
   "v2": [
    51467445296935,
    21446895683034
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
     "tests/test_ipynb.py",
     "black"
    ]
   ]
  },
  {
   "call": "symbols('black.py', 'main')",
   "key": "[\"symbols\", [\"black.py\", \"main\"]]",
   "v1": [
    6411482560385,
    2382988409226
   ],
   "v2": [
    6850888850053,
    2382988409226
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     2227940,
     14002917
    ],
    "reexport": [
     31160,
     14002917
    ],
    "star": [
     15580,
     42008751
    ],
    "none": [
     358340,
     42008751
    ],
    "missing": [
     227827,
     274567
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_ipynb.py",
     "black"
    ]
   ]
  },
  {
   "call": "symbols('black/__init__.py', 'main')",
   "key": "[\"symbols\", [\"black/__init__.py\", \"main\"]]",
   "v1": [
    675159768355,
    223635919768
   ],
   "v2": [
    2170952162977,
    670907759304
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     119925,
     37341112
    ],
    "reexport": [
     572975,
     37341112
    ],
    "star": [
     13325,
     37341112
    ],
    "none": [
     199875,
     37341112
    ],
    "missing": [
     535809,
     549134
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_ipynb.py",
     "black"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+main\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+main\\\\b\", \".\"]]",
   "v1": [
    685,
    226
   ],
   "v2": [
    6617,
    2034
   ],
   "p_cap": [
    1,
    39
   ],
   "forecast": {
    "zero": [
     1,
     39
    ],
    "mid": [
     37,
     39
    ],
    "cap": [
     1,
     39
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_ipynb.py",
     "black"
    ]
   ]
  }
 ],
 "choice": {
  "call": "ls('.')",
  "key": "[\"ls\", [\".\"]]",
  "provenance": "`black` imported by `tests/test_ipynb.py` should live under `.`",
  "v2": [
   51467445296935,
   21446895683034
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
  "cap": "[\"symbols\", [\"black.py\", \"main\"]]"
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
    ".git_archival.txt",
    ".github/",
    ".pre-commit-config.yaml",
    ".pre-commit-hooks.yaml",
    ".prettierrc.yaml",
    ".readthedocs.yaml",
    "AUTHORS.md",
    "CHANGES.md",
    "CONTRIBUTING.md",
    "README.md",
    "SECURITY.md",
    "action.yml",
    "action/",
    "docs/",
    "profiling/",
    "pyproject.toml",
    "scripts/",
    "src/",
    "tests/",
    "tox.ini"
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "chain": [
   [
    "tests/test_ipynb.py",
    "main",
    "reexport",
    [
     "black",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 4

`.` lists 20 entries (complete): `.github/`, `action/`, `docs/`, `profiling/`, `scripts/`, `src/` and 1 more.

Chain: `tests/test_ipynb.py` takes `main` from `black` (module not yet located).

Outstanding: locate the module `black` imported by `tests/test_ipynb.py`.

Next: list `src`, because `black` imported by `tests/test_ipynb.py` should live under `src`. I expect: a complete listing settles which files exist (about 90%); a capped listing settles nothing (about 10%). The alternative, outline `src/black.py` filtered to `main`, costs more in expectation. Plan by outcome: complete: outline the module it reveals; cap: outline `src/black.py` filtered to `main`.

**Call:** `ls('src')`

**Response**: outcome `complete`

```
_black_version.pyi
black/
blackd/
blib2to3/
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_ipynb.py",
    "black"
   ],
   "desc": "locate the module `black` imported by `tests/test_ipynb.py`"
  }
 ],
 "candidates": [
  {
   "call": "ls('src')",
   "key": "[\"ls\", [\"src\"]]",
   "v1": [
    1204,
    565
   ],
   "v2": [
    25770627336221,
    11914942046130
   ],
   "p_cap": [
    1,
    10
   ],
   "forecast": {
    "complete": [
     9,
     10
    ],
    "cap": [
     1,
     10
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_ipynb.py",
     "black"
    ]
   ]
  },
  {
   "call": "symbols('src/black.py', 'main')",
   "key": "[\"symbols\", [\"src/black.py\", \"main\"]]",
   "v1": [
    5600190517585,
    2382988409226
   ],
   "v2": [
    14393393343409,
    5957471023065
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     4455880,
     14002917
    ],
    "reexport": [
     62320,
     14002917
    ],
    "star": [
     31160,
     42008751
    ],
    "none": [
     716680,
     42008751
    ],
    "missing": [
     181087,
     274567
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_ipynb.py",
     "black"
    ]
   ]
  },
  {
   "call": "symbols('src/black/__init__.py', 'main')",
   "key": "[\"symbols\", [\"src/black/__init__.py\", \"main\"]]",
   "v1": [
    336242500565,
    111817959884
   ],
   "v2": [
    1734408166317,
    559089799420
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     119925,
     18670556
    ],
    "reexport": [
     572975,
     18670556
    ],
    "star": [
     13325,
     18670556
    ],
    "none": [
     199875,
     18670556
    ],
    "missing": [
     261242,
     274567
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_ipynb.py",
     "black"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+main\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+main\\\\b\", \".\"]]",
   "v1": [
    685,
    226
   ],
   "v2": [
    1769,
    565
   ],
   "p_cap": [
    1,
    39
   ],
   "forecast": {
    "zero": [
     1,
     39
    ],
    "mid": [
     37,
     39
    ],
    "cap": [
     1,
     39
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_ipynb.py",
     "black"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+main\\\\b', 'src')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+main\\\\b\", \"src\"]]",
   "v1": [
    685,
    226
   ],
   "v2": [
    1769,
    565
   ],
   "p_cap": [
    1,
    114
   ],
   "forecast": {
    "zero": [
     47,
     57
    ],
    "mid": [
     1,
     6
    ],
    "cap": [
     1,
     114
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_ipynb.py",
     "black"
    ]
   ]
  }
 ],
 "choice": {
  "call": "ls('src')",
  "key": "[\"ls\", [\"src\"]]",
  "provenance": "`black` imported by `tests/test_ipynb.py` should live under `src`",
  "v2": [
   25770627336221,
   11914942046130
  ]
 },
 "forecast": {
  "complete": [
   9,
   10
  ],
  "cap": [
   1,
   10
  ]
 },
 "plan": {
  "complete": "continue",
  "cap": "[\"symbols\", [\"src/black.py\", \"main\"]]"
 },
 "adherence": {
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "listing",
   "step": 4,
   "dir": "src",
   "entries": [
    "_black_version.pyi",
    "black/",
    "blackd/",
    "blib2to3/"
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "chain": [
   [
    "tests/test_ipynb.py",
    "main",
    "reexport",
    [
     "black",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 5

`src` lists 4 entries (complete): `black/`, `blackd/`, `blib2to3/`.

Chain: `tests/test_ipynb.py` takes `main` from `black` (module not yet located).

Still to settle: locate the module `black` imported by `tests/test_ipynb.py`.

Next: outline `src/black/__init__.py` filtered to `main`, because `black` would be `src/black/__init__.py` if that file exists; one call both checks and closes it. I expect: a re-export continues the chain to its source (about 60%); no binding at all points at a submodule or an unresolved name (about 20%); a definition there ends the chain (about 15%); the file does not exist (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, list `src/black`, is expected to open more follow-up work. Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: check for a submodule of that name; missing: list `src/black`.

**Call:** `symbols('src/black/__init__.py', 'main')`

**Response**: outcome `def`

```
module src/black/__init__.py lines=1723 dynamic=no all=none
554 def main
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_ipynb.py",
    "black"
   ],
   "desc": "locate the module `black` imported by `tests/test_ipynb.py`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/black/__init__.py', 'main')",
   "key": "[\"symbols\", [\"src/black/__init__.py\", \"main\"]]",
   "v1": [
    26247499,
    10181300
   ],
   "v2": [
    4751611823,
    1842815300
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     441,
     3400
    ],
    "reexport": [
     2107,
     3400
    ],
    "star": [
     49,
     3400
    ],
    "none": [
     147,
     680
    ],
    "missing": [
     1,
     50
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_ipynb.py",
     "black"
    ]
   ]
  },
  {
   "call": "ls('src/black')",
   "key": "[\"ls\", [\"src/black\"]]",
   "v1": [
    4946877,
    1390804
   ],
   "v2": [
    6515648721,
    1842815300
   ],
   "p_cap": [
    4,
    181
   ],
   "forecast": {
    "complete": [
     177,
     181
    ],
    "cap": [
     4,
     181
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_ipynb.py",
     "black"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+main\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+main\\\\b\", \".\"]]",
   "v1": [
    34845,
    7684
   ],
   "v2": [
    36428799,
    10181300
   ],
   "p_cap": [
    1,
    39
   ],
   "forecast": {
    "zero": [
     1,
     39
    ],
    "mid": [
     37,
     39
    ],
    "cap": [
     1,
     39
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_ipynb.py",
     "black"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+main\\\\b', 'src')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+main\\\\b\", \"src\"]]",
   "v1": [
    34845,
    7684
   ],
   "v2": [
    36428799,
    10181300
   ],
   "p_cap": [
    1,
    114
   ],
   "forecast": {
    "zero": [
     47,
     57
    ],
    "mid": [
     1,
     6
    ],
    "cap": [
     1,
     114
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_ipynb.py",
     "black"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/black/__init__.py', 'main')",
  "key": "[\"symbols\", [\"src/black/__init__.py\", \"main\"]]",
  "provenance": "`black` would be `src/black/__init__.py` if that file exists; one call both checks and closes it",
  "v2": [
   4751611823,
   1842815300
  ]
 },
 "forecast": {
  "def": [
   441,
   3400
  ],
  "reexport": [
   2107,
   3400
  ],
  "star": [
   49,
   3400
  ],
  "none": [
   147,
   680
  ],
  "missing": [
   1,
   50
  ]
 },
 "plan": {
  "def": "done",
  "reexport": "continue",
  "star": "continue",
  "none": "continue",
  "missing": "[\"ls\", [\"src/black\"]]"
 },
 "adherence": {
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 5,
   "path": "src/black/__init__.py",
   "filter": "main",
   "header": {
    "lines": 1723,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/black/__init__.py",
     "name": "main",
     "line": 554,
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
    "tests/test_ipynb.py",
    "main",
    "reexport",
    [
     "black",
     "src/black/__init__.py"
    ]
   ],
   [
    "src/black/__init__.py",
    "main",
    "def",
    554
   ]
  ]
 }
}
```
</details>

## Final

Certificate complete. The name resolves to `src/black/__init__.py:554`. In hindsight, 1 of 5 calls were not needed for the certificate: steps 1.

**Answer:** `{"target": {"kind": "def", "path": "src/black/__init__.py", "line": 554, "name": "main", "detail": "def"}, "text": "src/black/__init__.py:554"}`  
**Stopped:** certificate after 5 calls