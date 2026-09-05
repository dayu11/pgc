# click-resolve-4cf9b346

**Repository:** click  
**Family:** resolve  
**Seed:** 0, prior 93954b294cf7311e

## Task

In `tests/test_testing.py`, line 12 imports `CliRunner` from `click.testing`. Under the declared semantics, which definition does the module-level name `CliRunner` bound by this statement resolve to? Answer with `path:line`.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

Nothing seen yet beyond the task text.

Chain: `tests/test_testing.py` is not yet closed for `CliRunner`.

Outstanding: close the namespace of `tests/test_testing.py` for `CliRunner`.

Next: outline `tests/test_testing.py`, because module `tests/test_testing.py` (task). I expect: a definition there ends the chain (about 80%); a capped outline means filtering by name (about 15%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (about 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `tests/test_testing.py` filtered to `CliRunner`, is expected to open more follow-up work. Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done; cap: outline `tests/test_testing.py` filtered to `CliRunner`.

**Call:** `symbols('tests/test_testing.py')`

**Response** (capped): outcome `cap`

```
module tests/test_testing.py lines=841 dynamic=no all=none
1 import faulthandler <- faulthandler
2 import io <- io
3 import os <- os
4 import pdb <- pdb
5 import sys <- sys
6 from BytesIO <- io BytesIO
8 import pytest <- pytest
10 import click <- click
11 from ClickException <- click.exceptions ClickException
12 from CliRunner <- click.testing CliRunner
13 from _get_binary_stream <- click.utils _get_binary_stream
16 def test_runner
34 def test_echo_stdin_stream
52 def test_echo_stdin_prompts
92 def test_runner_with_stream
115 def test_prompts
137 def test_getchar
167 def test_catch_exceptions
191 def test_catch_exceptions_cli_runner
213 def test_with_color
229 def test_with_color_errors
249 def test_with_color_but_pause_not_blocking
260 def test_with_echo_via_pager
271 def test_exit_code_and_output_from_sys_exit
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
    "tests/test_testing.py",
    "CliRunner"
   ],
   "desc": "close the namespace of `tests/test_testing.py` for `CliRunner`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/test_testing.py')",
   "key": "[\"symbols\", [\"tests/test_testing.py\"]]",
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
     "tests/test_testing.py",
     "CliRunner"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_testing.py', 'CliRunner')",
   "key": "[\"symbols\", [\"tests/test_testing.py\", \"CliRunner\"]]",
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
     "tests/test_testing.py",
     "CliRunner"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_testing.py')",
  "key": "[\"symbols\", [\"tests/test_testing.py\"]]",
  "provenance": "module `tests/test_testing.py` (task)",
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
  "cap": "[\"symbols\", [\"tests/test_testing.py\", \"CliRunner\"]]"
 },
 "adherence": null,
 "facts": [
  {
   "kind": "outline",
   "step": 1,
   "path": "tests/test_testing.py",
   "filter": null,
   "header": {
    "lines": 841,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_testing.py",
     "name": "faulthandler",
     "line": 1,
     "kind": "import",
     "src": "faulthandler",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_testing.py",
     "name": "io",
     "line": 2,
     "kind": "import",
     "src": "io",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_testing.py",
     "name": "os",
     "line": 3,
     "kind": "import",
     "src": "os",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_testing.py",
     "name": "pdb",
     "line": 4,
     "kind": "import",
     "src": "pdb",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_testing.py",
     "name": "sys",
     "line": 5,
     "kind": "import",
     "src": "sys",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_testing.py",
     "name": "BytesIO",
     "line": 6,
     "kind": "from",
     "src": "io",
     "src_name": "BytesIO",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_testing.py",
     "name": "pytest",
     "line": 8,
     "kind": "import",
     "src": "pytest",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_testing.py",
     "name": "click",
     "line": 10,
     "kind": "import",
     "src": "click",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_testing.py",
     "name": "ClickException",
     "line": 11,
     "kind": "from",
     "src": "click.exceptions",
     "src_name": "ClickException",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_testing.py",
     "name": "CliRunner",
     "line": 12,
     "kind": "from",
     "src": "click.testing",
     "src_name": "CliRunner",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_testing.py",
     "name": "_get_binary_stream",
     "line": 13,
     "kind": "from",
     "src": "click.utils",
     "src_name": "_get_binary_stream",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_testing.py",
     "name": "test_runner",
     "line": 16,
     "kind": "def",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_testing.py",
     "name": "test_echo_stdin_stream",
     "line": 34,
     "kind": "def",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_testing.py",
     "name": "test_echo_stdin_prompts",
     "line": 52,
     "kind": "def",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_testing.py",
     "name": "test_runner_with_stream",
     "line": 92,
     "kind": "def",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_testing.py",
     "name": "test_prompts",
     "line": 115,
     "kind": "def",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_testing.py",
     "name": "test_getchar",
     "line": 137,
     "kind": "def",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_testing.py",
     "name": "test_catch_exceptions",
     "line": 167,
     "kind": "def",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_testing.py",
     "name": "test_catch_exceptions_cli_r
```
</details>

## Step 2

The outline of `tests/test_testing.py` has 40 bindings (capped, so this is only the start of the file); no `__all__`; no dynamic namespace tricks.

Chain: `tests/test_testing.py` is not yet closed for `CliRunner`.

Still to settle: close the namespace of `tests/test_testing.py` for `CliRunner`.

Next: outline `tests/test_testing.py` filtered to `CliRunner`, because module `tests/test_testing.py` (task), name `CliRunner` (task). I expect: a re-export continues the chain to its source (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a definition there ends the chain (under 5%); no binding but a star import means checking what that source exports (under 5%). Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done.

**Call:** `symbols('tests/test_testing.py', 'CliRunner')`

**Response**: outcome `reexport`

```
module tests/test_testing.py lines=841 dynamic=no all=none
12 from CliRunner <- click.testing CliRunner
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "tests/test_testing.py",
    "CliRunner"
   ],
   "desc": "close the namespace of `tests/test_testing.py` for `CliRunner`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/test_testing.py', 'CliRunner')",
   "key": "[\"symbols\", [\"tests/test_testing.py\", \"CliRunner\"]]",
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
     "tests/test_testing.py",
     "CliRunner"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_testing.py', 'CliRunner')",
  "key": "[\"symbols\", [\"tests/test_testing.py\", \"CliRunner\"]]",
  "provenance": "module `tests/test_testing.py` (task), name `CliRunner` (task)",
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
  "planned": "[\"symbols\", [\"tests/test_testing.py\", \"CliRunner\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 2,
   "path": "tests/test_testing.py",
   "filter": "CliRunner",
   "header": {
    "lines": 841,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_testing.py",
     "name": "CliRunner",
     "line": 12,
     "kind": "from",
     "src": "click.testing",
     "src_name": "CliRunner",
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
    "tests/test_testing.py",
    "CliRunner",
    "reexport",
    [
     "click.testing",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 3

In `tests/test_testing.py`, `CliRunner` has exactly one binding: line 12 imports it as `CliRunner` from `click.testing`. No dynamic namespace tricks, no `__all__`.

Chain: `tests/test_testing.py` takes `CliRunner` from `click.testing` (module not yet located).

Outstanding: locate the module `click.testing` imported by `tests/test_testing.py`.

Next: grep `def`/`class CliRunner` statements under `.`, because a `def`/`class CliRunner` statement would reveal the module file; `CliRunner` task. I expect: hits under the cap (about 95%); a capped result (under 5%); no hits (under 5%). The alternative, list `.`, is more likely to hit the cap (about 20% against under 5%). Plan by outcome: zero: list `.`; mid: outline each module that appears; cap: list `.`.

**Call:** `grep('^\\s*(?:async\\s+)?(?:def|class)\\s+CliRunner\\b', '.')`

**Response**: outcome `mid`

```
src/click/testing.py:317:class CliRunner:
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_testing.py",
    "click.testing"
   ],
   "desc": "locate the module `click.testing` imported by `tests/test_testing.py`"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+CliRunner\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+CliRunner\\\\b\", \".\"]]",
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
     "tests/test_testing.py",
     "click.testing"
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
     "tests/test_testing.py",
     "click.testing"
    ]
   ]
  },
  {
   "call": "symbols('click/testing.py', 'CliRunner')",
   "key": "[\"symbols\", [\"click/testing.py\", \"CliRunner\"]]",
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
     "tests/test_testing.py",
     "click.testing"
    ]
   ]
  },
  {
   "call": "symbols('click/testing/__init__.py', 'CliRunner')",
   "key": "[\"symbols\", [\"click/testing/__init__.py\", \"CliRunner\"]]",
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
     "tests/test_testing.py",
     "click.testing"
    ]
   ]
  }
 ],
 "choice": {
  "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+CliRunner\\\\b', '.')",
  "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+CliRunner\\\\b\", \".\"]]",
  "provenance": "a `def`/`class CliRunner` statement would reveal the module file; `CliRunner` task",
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
   "pattern": "^\\s*(?:async\\s+)?(?:def|class)\\s+CliRunner\\b",
   "scope": ".",
   "hits": [
    [
     "src/click/testing.py",
     317
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "chain": [
   [
    "tests/test_testing.py",
    "CliRunner",
    "reexport",
    [
     "click.testing",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 4

The grep under `.` returned 1 lines, under the cap, so these are all of them: `src/click/testing.py`.

Chain: `tests/test_testing.py` takes `CliRunner` from `click.testing` (module not yet located).

Outstanding: locate the module `click.testing` imported by `tests/test_testing.py`.

Next: list `.`, because `click.testing` imported by `tests/test_testing.py` should live under `.`. I expect: a complete listing settles which files exist (about 80%); a capped listing settles nothing (about 20%). The alternative, outline `click/testing.py` filtered to `CliRunner`, costs more in expectation. Plan by outcome: complete: outline the module it reveals; cap: outline `click/testing.py` filtered to `CliRunner`.

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
    "tests/test_testing.py",
    "click.testing"
   ],
   "desc": "locate the module `click.testing` imported by `tests/test_testing.py`"
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
     "tests/test_testing.py",
     "click.testing"
    ]
   ]
  },
  {
   "call": "symbols('click/testing.py', 'CliRunner')",
   "key": "[\"symbols\", [\"click/testing.py\", \"CliRunner\"]]",
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
     "tests/test_testing.py",
     "click.testing"
    ]
   ]
  },
  {
   "call": "symbols('click/testing/__init__.py', 'CliRunner')",
   "key": "[\"symbols\", [\"click/testing/__init__.py\", \"CliRunner\"]]",
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
     "tests/test_testing.py",
     "click.testing"
    ]
   ]
  }
 ],
 "choice": {
  "call": "ls('.')",
  "key": "[\"ls\", [\".\"]]",
  "provenance": "`click.testing` imported by `tests/test_testing.py` should live under `.`",
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
  "cap": "[\"symbols\", [\"click/testing.py\", \"CliRunner\"]]"
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
    "tests/test_testing.py",
    "CliRunner",
    "reexport",
    [
     "click.testing",
     "src/click/testing.py"
    ]
   ],
   [
    "src/click/testing.py",
    "CliRunner",
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

Chain: `tests/test_testing.py` takes `CliRunner` from `click.testing` (`src/click/testing.py`); `src/click/testing.py` is not yet closed for `CliRunner`.

Still to settle: close the namespace of `src/click/testing.py` for `CliRunner`.

Next: outline `src/click/testing.py` filtered to `CliRunner`, because module `src/click/testing.py` (step 3), name `CliRunner` (task). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `src/click/testing.py`, is more likely to hit the cap (about 15% against under 5%). Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done.

**Call:** `symbols('src/click/testing.py', 'CliRunner')`

**Response**: outcome `def`

```
module src/click/testing.py lines=799 dynamic=no all=none
317 class CliRunner
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/click/testing.py",
    "CliRunner"
   ],
   "desc": "close the namespace of `src/click/testing.py` for `CliRunner`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/click/testing.py', 'CliRunner')",
   "key": "[\"symbols\", [\"src/click/testing.py\", \"CliRunner\"]]",
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
     "src/click/testing.py",
     "CliRunner"
    ]
   ]
  },
  {
   "call": "symbols('src/click/testing.py')",
   "key": "[\"symbols\", [\"src/click/testing.py\"]]",
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
     "src/click/testing.py",
     "CliRunner"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/click/testing.py', 'CliRunner')",
  "key": "[\"symbols\", [\"src/click/testing.py\", \"CliRunner\"]]",
  "provenance": "module `src/click/testing.py` (step 3), name `CliRunner` (task)",
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
   "path": "src/click/testing.py",
   "filter": "CliRunner",
   "header": {
    "lines": 799,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/click/testing.py",
     "name": "CliRunner",
     "line": 317,
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
    "tests/test_testing.py",
    "CliRunner",
    "reexport",
    [
     "click.testing",
     "src/click/testing.py"
    ]
   ],
   [
    "src/click/testing.py",
    "CliRunner",
    "class",
    317
   ]
  ]
 }
}
```
</details>

## Final

Certificate complete. The name resolves to `src/click/testing.py:317`. In hindsight, 1 of 5 calls were not needed for the certificate: steps 1.

**Answer:** `{"target": {"kind": "def", "path": "src/click/testing.py", "line": 317, "name": "CliRunner", "detail": "class"}, "text": "src/click/testing.py:317"}`  
**Stopped:** certificate after 5 calls