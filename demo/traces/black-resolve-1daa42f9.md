# black-resolve-1daa42f9

**Repository:** black  
**Family:** resolve  
**Seed:** 0, prior 55c929686ca1d56a

## Task

In `src/black/__init__.py`, line 59 imports `LN` from `black.linegen`. Under the declared semantics, which definition does the module-level name `LN` bound by this statement resolve to? Answer with `path:line`.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

Nothing seen yet beyond the task text.

Chain: `src/black/__init__.py` is not yet closed for `LN`.

Outstanding: close the namespace of `src/black/__init__.py` for `LN`.

Next: outline `src/black/__init__.py`, because module `src/black/__init__.py` (task). I expect: a re-export continues the chain to its source (about 55%); no binding at all points at a submodule or an unresolved name (about 20%); a capped outline means filtering by name (about 15%); a definition there ends the chain (about 10%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `src/black/__init__.py` filtered to `LN`, is expected to open more follow-up work. Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: check for a submodule of that name; cap: outline `src/black/__init__.py` filtered to `LN`.

**Call:** `symbols('src/black/__init__.py')`

**Response** (capped): outcome `cap`

```
module src/black/__init__.py lines=1723 dynamic=no all=none
1 import io <- io
2 import json <- json
3 import platform <- platform
4 import re <- re
5 import sys <- sys
6 import tokenize <- tokenize
7 import traceback <- traceback
8 from Collection <- collections.abc Collection
8 from Generator <- collections.abc Generator
8 from MutableMapping <- collections.abc MutableMapping
8 from Sequence <- collections.abc Sequence
14 from nullcontext <- contextlib nullcontext
15 from replace <- dataclasses replace
16 from datetime <- datetime datetime
16 from timezone <- datetime timezone
17 from Enum <- enum Enum
18 from JSONDecodeError <- json.decoder JSONDecodeError
19 from Path <- pathlib Path
20 from Pattern <- re Pattern
21 from Any <- typing Any
23 import click <- click
24 from ParameterSource <- click.core ParameterSource
25 from mypyc_attr <- mypy_extensions mypyc_attr
26 from GitIgnoreSpec <- pathspec GitIgnoreSpec
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
    "src/black/__init__.py",
    "LN"
   ],
   "desc": "close the namespace of `src/black/__init__.py` for `LN`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/black/__init__.py')",
   "key": "[\"symbols\", [\"src/black/__init__.py\"]]",
   "v1": [
    14147599,
    5294276
   ],
   "v2": [
    289033111,
    105885520
   ],
   "p_cap": [
    7,
    52
   ],
   "forecast": {
    "def": [
     405,
     3536
    ],
    "reexport": [
     1935,
     3536
    ],
    "star": [
     45,
     3536
    ],
    "none": [
     675,
     3536
    ],
    "cap": [
     7,
     52
    ]
   },
   "serves": [
    [
     "bindings",
     "src/black/__init__.py",
     "LN"
    ]
   ]
  },
  {
   "call": "symbols('src/black/__init__.py', 'LN')",
   "key": "[\"symbols\", [\"src/black/__init__.py\", \"LN\"]]",
   "v1": [
    177357,
    59890
   ],
   "v2": [
    177357,
    59890
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
     "src/black/__init__.py",
     "LN"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/black/__init__.py')",
  "key": "[\"symbols\", [\"src/black/__init__.py\"]]",
  "provenance": "module `src/black/__init__.py` (task)",
  "v2": [
   289033111,
   105885520
  ]
 },
 "forecast": {
  "def": [
   405,
   3536
  ],
  "reexport": [
   1935,
   3536
  ],
  "star": [
   45,
   3536
  ],
  "none": [
   675,
   3536
  ],
  "cap": [
   7,
   52
  ]
 },
 "plan": {
  "def": "done",
  "reexport": "continue",
  "star": "continue",
  "none": "continue",
  "cap": "[\"symbols\", [\"src/black/__init__.py\", \"LN\"]]"
 },
 "adherence": null,
 "facts": [
  {
   "kind": "outline",
   "step": 1,
   "path": "src/black/__init__.py",
   "filter": null,
   "header": {
    "lines": 1723,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/black/__init__.py",
     "name": "io",
     "line": 1,
     "kind": "import",
     "src": "io",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/black/__init__.py",
     "name": "json",
     "line": 2,
     "kind": "import",
     "src": "json",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/black/__init__.py",
     "name": "platform",
     "line": 3,
     "kind": "import",
     "src": "platform",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/black/__init__.py",
     "name": "re",
     "line": 4,
     "kind": "import",
     "src": "re",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/black/__init__.py",
     "name": "sys",
     "line": 5,
     "kind": "import",
     "src": "sys",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/black/__init__.py",
     "name": "tokenize",
     "line": 6,
     "kind": "import",
     "src": "tokenize",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/black/__init__.py",
     "name": "traceback",
     "line": 7,
     "kind": "import",
     "src": "traceback",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/black/__init__.py",
     "name": "Collection",
     "line": 8,
     "kind": "from",
     "src": "collections.abc",
     "src_name": "Collection",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/black/__init__.py",
     "name": "Generator",
     "line": 8,
     "kind": "from",
     "src": "collections.abc",
     "src_name": "Generator",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/black/__init__.py",
     "name": "MutableMapping",
     "line": 8,
     "kind": "from",
     "src": "collections.abc",
     "src_name": "MutableMapping",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/black/__init__.py",
     "name": "Sequence",
     "line": 8,
     "kind": "from",
     "src": "collections.abc",
     "src_name": "Sequence",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/black/__init__.py",
     "name": "nullcontext",
     "line": 14,
     "kind": "from",
     "src": "contextlib",
     "src_name": "nullcontext",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/black/__init__.py",
     "name": "replace",
     "line": 15,
     "kind": "from",
     "src": "dataclasses",
     "src_name": "replace",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/black/__init__.py",
     "name": "datetime",
     "line": 16,
     "kind": "from",
     "src": "datetime",
     "src_name": "datetime",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/black/__init__.py",
     "name": "timezone",
     "line": 16,
     "kind": "from",
     "src": "datetime",
     "src_name": "timezone",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/black/__init__.py",
     "name": "Enum",
     "line": 17,
     "kind": "from",
     "src": "enum",
     "src_name": "Enum",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/black/__init__.py",
     "name": "JSONDecodeError",
     "line": 18,
     "kind": "from",
     "src": "json.decoder",
     "src_name": "JSONDecodeError",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/black/__init__.py",
     "name": "Path",
     "line": 19,
     "kind": "from",
     "src": "pathlib",
     "src_name": "Path",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/black/__init__.py",
     "name": "Pattern",
     "line": 20,
     "kind": "from",
     "src": "re",
     "src_name": "Pattern",
     "conditional
```
</details>

## Step 2

The outline of `src/black/__init__.py` has 40 bindings (capped, so this is only the start of the file); no `__all__`; no dynamic namespace tricks.

Chain: `src/black/__init__.py` is not yet closed for `LN`.

Still to settle: close the namespace of `src/black/__init__.py` for `LN`.

Next: outline `src/black/__init__.py` filtered to `LN`, because module `src/black/__init__.py` (task), name `LN` (task). I expect: a re-export continues the chain to its source (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a definition there ends the chain (under 5%); no binding but a star import means checking what that source exports (under 5%). Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: check for a submodule of that name.

**Call:** `symbols('src/black/__init__.py', 'LN')`

**Response**: outcome `reexport`

```
module src/black/__init__.py lines=1723 dynamic=no all=none
59 from LN <- black.linegen LN
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/black/__init__.py",
    "LN"
   ],
   "desc": "close the namespace of `src/black/__init__.py` for `LN`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/black/__init__.py', 'LN')",
   "key": "[\"symbols\", [\"src/black/__init__.py\", \"LN\"]]",
   "v1": [
    177357,
    59890
   ],
   "v2": [
    177357,
    59890
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
     "src/black/__init__.py",
     "LN"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/black/__init__.py', 'LN')",
  "key": "[\"symbols\", [\"src/black/__init__.py\", \"LN\"]]",
  "provenance": "module `src/black/__init__.py` (task), name `LN` (task)",
  "v2": [
   177357,
   59890
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
  "planned": "[\"symbols\", [\"src/black/__init__.py\", \"LN\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 2,
   "path": "src/black/__init__.py",
   "filter": "LN",
   "header": {
    "lines": 1723,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/black/__init__.py",
     "name": "LN",
     "line": 59,
     "kind": "from",
     "src": "black.linegen",
     "src_name": "LN",
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
    "src/black/__init__.py",
    "LN",
    "reexport",
    [
     "black.linegen",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 3

In `src/black/__init__.py`, `LN` has exactly one binding: line 59 imports it as `LN` from `black.linegen`. No dynamic namespace tricks, no `__all__`.

Chain: `src/black/__init__.py` takes `LN` from `black.linegen` (module not yet located).

Outstanding: locate the module `black.linegen` imported by `src/black/__init__.py`.

Next: grep `def`/`class LN` statements under `.`, because a `def`/`class LN` statement would reveal the module file; `LN` task. I expect: hits under the cap (about 95%); a capped result (about 5%); no hits (about 5%). The alternative, list `.`, is more likely to hit the cap (about 20% against about 5%). Plan by outcome: zero: list `.`; mid: outline each module that appears; cap: list `.`.

**Call:** `grep('^\\s*(?:async\\s+)?(?:def|class)\\s+LN\\b', '.')`

**Response**: outcome `zero`

```

```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/black/__init__.py",
    "black.linegen"
   ],
   "desc": "locate the module `black.linegen` imported by `src/black/__init__.py`"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+LN\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+LN\\\\b\", \".\"]]",
   "v1": [
    18353,
    8814
   ],
   "v2": [
    166081,
    79326
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
     "src/black/__init__.py",
     "black.linegen"
    ]
   ]
  },
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    4583,
    2034
   ],
   "v2": [
    179641,
    79326
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
     "src/black/__init__.py",
     "black.linegen"
    ]
   ]
  },
  {
   "call": "symbols('black/linegen.py', 'LN')",
   "key": "[\"symbols\", [\"black/linegen.py\", \"LN\"]]",
   "v1": [
    5600190517585,
    2382988409226
   ],
   "v2": [
    73850255527129,
    30978849319938
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
     "src/black/__init__.py",
     "black.linegen"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+LN\\\\b', 'src')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+LN\\\\b\", \"src\"]]",
   "v1": [
    971,
    339
   ],
   "v2": [
    38434,
    13221
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
     "src/black/__init__.py",
     "black.linegen"
    ]
   ]
  },
  {
   "call": "symbols('black/linegen/__init__.py', 'LN')",
   "key": "[\"symbols\", [\"black/linegen/__init__.py\", \"LN\"]]",
   "v1": [
    336242500565,
    111817959884
   ],
   "v2": [
    13326240176003,
    4360900435476
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
     "src/black/__init__.py",
     "black.linegen"
    ]
   ]
  }
 ],
 "choice": {
  "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+LN\\\\b', '.')",
  "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+LN\\\\b\", \".\"]]",
  "provenance": "a `def`/`class LN` statement would reveal the module file; `LN` task",
  "v2": [
   166081,
   79326
  ]
 },
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
   "pattern": "^\\s*(?:async\\s+)?(?:def|class)\\s+LN\\b",
   "scope": ".",
   "hits": [],
   "capped": false
  }
 ],
 "goal_state": {
  "chain": [
   [
    "src/black/__init__.py",
    "LN",
    "reexport",
    [
     "black.linegen",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 4

The grep under `.` returned nothing, and it was not capped, so there are no such lines there.

Chain: `src/black/__init__.py` takes `LN` from `black.linegen` (module not yet located).

Outstanding: locate the module `black.linegen` imported by `src/black/__init__.py`.

Next: list `.`, because `black.linegen` imported by `src/black/__init__.py` should live under `.`. I expect: a complete listing settles which files exist (about 80%); a capped listing settles nothing (about 20%). The alternative, outline `black/linegen.py` filtered to `LN`, costs more in expectation. Plan by outcome: complete: outline the module it reveals; cap: outline `black/linegen.py` filtered to `LN`.

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
    "src/black/__init__.py",
    "black.linegen"
   ],
   "desc": "locate the module `black.linegen` imported by `src/black/__init__.py`"
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
    49844861211335,
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
     "src/black/__init__.py",
     "black.linegen"
    ]
   ]
  },
  {
   "call": "symbols('black/linegen.py', 'LN')",
   "key": "[\"symbols\", [\"black/linegen.py\", \"LN\"]]",
   "v1": [
    5600190517585,
    2382988409226
   ],
   "v2": [
    1983150039031,
    794329469742
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
     "src/black/__init__.py",
     "black.linegen"
    ]
   ]
  },
  {
   "call": "symbols('black/linegen/__init__.py', 'LN')",
   "key": "[\"symbols\", [\"black/linegen/__init__.py\", \"LN\"]]",
   "v1": [
    336242500565,
    111817959884
   ],
   "v2": [
    3238965159053,
    1006361638956
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
     "src/black/__init__.py",
     "black.linegen"
    ]
   ]
  }
 ],
 "choice": {
  "call": "ls('.')",
  "key": "[\"ls\", [\".\"]]",
  "provenance": "`black.linegen` imported by `src/black/__init__.py` should live under `.`",
  "v2": [
   49844861211335,
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
  "cap": "[\"symbols\", [\"black/linegen.py\", \"LN\"]]"
 },
 "adherence": {
  "planned": "[\"ls\", [\".\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "listing",
   "step": 4,
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
    "src/black/__init__.py",
    "LN",
    "reexport",
    [
     "black.linegen",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 5

`.` lists 20 entries (complete): `.github/`, `action/`, `docs/`, `profiling/`, `scripts/`, `src/` and 1 more.

Chain: `src/black/__init__.py` takes `LN` from `black.linegen` (module not yet located).

Still to settle: locate the module `black.linegen` imported by `src/black/__init__.py`.

Next: outline `src/black/linegen.py` filtered to `LN`, because `black.linegen` would be `src/black/linegen.py` if that file exists; one call both checks and closes it. I expect: a definition there ends the chain (about 80%); the file does not exist (about 10%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, list `src/black`, is expected to open more follow-up work. Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done; missing: list `src/black`.

**Call:** `symbols('src/black/linegen.py', 'LN')`

**Response**: outcome `def`

```
module src/black/linegen.py lines=2339 dynamic=no all=none
101 assign LN
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/black/__init__.py",
    "black.linegen"
   ],
   "desc": "locate the module `black.linegen` imported by `src/black/__init__.py`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/black/linegen.py', 'LN')",
   "key": "[\"symbols\", [\"src/black/linegen.py\", \"LN\"]]",
   "v1": [
    5790410335,
    4521799638
   ],
   "v2": [
    1050320830915,
    818445734478
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     21736,
     26571
    ],
    "reexport": [
     304,
     26571
    ],
    "star": [
     152,
     79713
    ],
    "none": [
     3496,
     79713
    ],
    "missing": [
     65,
     521
    ]
   },
   "serves": [
    [
     "module_path",
     "src/black/__init__.py",
     "black.linegen"
    ]
   ]
  },
  {
   "call": "ls('src/black')",
   "key": "[\"ls\", [\"src/black\"]]",
   "v1": [
    83983,
    40906
   ],
   "v2": [
    1666755777901,
    818445734478
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
     "src/black/__init__.py",
     "black.linegen"
    ]
   ]
  },
  {
   "call": "symbols('src/black/linegen/__init__.py', 'LN')",
   "key": "[\"symbols\", [\"src/black/linegen/__init__.py\", \"LN\"]]",
   "v1": [
    630059125,
    212178292
   ],
   "v2": [
    192508427189741,
    83240302269396
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     585,
     35428
    ],
    "reexport": [
     2795,
     35428
    ],
    "star": [
     65,
     35428
    ],
    "none": [
     975,
     35428
    ],
    "missing": [
     456,
     521
    ]
   },
   "serves": [
    [
     "module_path",
     "src/black/__init__.py",
     "black.linegen"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/black/linegen.py', 'LN')",
  "key": "[\"symbols\", [\"src/black/linegen.py\", \"LN\"]]",
  "provenance": "`black.linegen` would be `src/black/linegen.py` if that file exists; one call both checks and closes it",
  "v2": [
   1050320830915,
   818445734478
  ]
 },
 "forecast": {
  "def": [
   21736,
   26571
  ],
  "reexport": [
   304,
   26571
  ],
  "star": [
   152,
   79713
  ],
  "none": [
   3496,
   79713
  ],
  "missing": [
   65,
   521
  ]
 },
 "plan": {
  "def": "done",
  "reexport": "continue",
  "star": "continue",
  "none": "done",
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
   "path": "src/black/linegen.py",
   "filter": "LN",
   "header": {
    "lines": 2339,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/black/linegen.py",
     "name": "LN",
     "line": 101,
     "kind": "assign",
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
    "src/black/__init__.py",
    "LN",
    "reexport",
    [
     "black.linegen",
     "src/black/linegen.py"
    ]
   ],
   [
    "src/black/linegen.py",
    "LN",
    "assign",
    101
   ]
  ]
 }
}
```
</details>

## Final

Certificate complete. The name resolves to `src/black/linegen.py:101`. In hindsight, 2 of 5 calls were not needed for the certificate: steps 1, 3.

**Answer:** `{"target": {"kind": "def", "path": "src/black/linegen.py", "line": 101, "name": "LN", "detail": "assign"}, "text": "src/black/linegen.py:101"}`  
**Stopped:** certificate after 5 calls