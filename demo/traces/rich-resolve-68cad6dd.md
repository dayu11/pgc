# rich-resolve-68cad6dd

**Repository:** rich  
**Family:** resolve  
**Seed:** 0, prior 6d694b621dbf13a2

## Task

In `rich/_unicode_data/__init__.py`, line 18 imports `CellTable` from `rich.cells`. Under the declared semantics, which definition does the module-level name `CellTable` bound by this statement resolve to? Answer with `path:line`.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

Nothing seen yet beyond the task text.

Chain: `rich/_unicode_data/__init__.py` is not yet closed for `CellTable`.

Outstanding: close the namespace of `rich/_unicode_data/__init__.py` for `CellTable`.

Next: outline `rich/_unicode_data/__init__.py`, because module `rich/_unicode_data/__init__.py` (task). I expect: a re-export continues the chain to its source (about 45%); no binding at all points at a submodule or an unresolved name (about 25%); a capped outline means filtering by name (about 15%); a definition there ends the chain (about 15%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `rich/_unicode_data/__init__.py` filtered to `CellTable`, is expected to open more follow-up work. Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: check for a submodule of that name; cap: outline `rich/_unicode_data/__init__.py` filtered to `CellTable`.

**Call:** `symbols('rich/_unicode_data/__init__.py')`

**Response**: outcome `def`

```
module rich/_unicode_data/__init__.py lines=94 dynamic=no all=none
1 from annotations <- __future__ annotations
3 import bisect <- bisect
4 import os <- os
5 import sys <- sys
8 from cache <- functools cache
10 from cache <- functools lru_cache
12 from import_module <- importlib import_module
13 from TYPE_CHECKING <- typing TYPE_CHECKING
13 from cast <- typing cast
15 from VERSIONS <- rich._unicode_data._versions VERSIONS
18 from CellTable <- rich.cells CellTable
20 assign VERSION_ORDER
28 assign VERSION_SET
31 def _parse_version
59 def load
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "rich/_unicode_data/__init__.py",
    "CellTable"
   ],
   "desc": "close the namespace of `rich/_unicode_data/__init__.py` for `CellTable`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('rich/_unicode_data/__init__.py')",
   "key": "[\"symbols\", [\"rich/_unicode_data/__init__.py\"]]",
   "v1": [
    118721521,
    45745700
   ],
   "v2": [
    4914217183,
    1829828000
   ],
   "p_cap": [
    9,
    55
   ],
   "forecast": {
    "def": [
     92,
     715
    ],
    "reexport": [
     322,
     715
    ],
    "star": [
     46,
     3575
    ],
    "none": [
     874,
     3575
    ],
    "cap": [
     9,
     55
    ]
   },
   "serves": [
    [
     "bindings",
     "rich/_unicode_data/__init__.py",
     "CellTable"
    ]
   ]
  },
  {
   "call": "symbols('rich/_unicode_data/__init__.py', 'CellTable')",
   "key": "[\"symbols\", [\"rich/_unicode_data/__init__.py\", \"CellTable\"]]",
   "v1": [
    7629819,
    2559200
   ],
   "v2": [
    7629819,
    2559200
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
     "rich/_unicode_data/__init__.py",
     "CellTable"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('rich/_unicode_data/__init__.py')",
  "key": "[\"symbols\", [\"rich/_unicode_data/__init__.py\"]]",
  "provenance": "module `rich/_unicode_data/__init__.py` (task)",
  "v2": [
   4914217183,
   1829828000
  ]
 },
 "forecast": {
  "def": [
   92,
   715
  ],
  "reexport": [
   322,
   715
  ],
  "star": [
   46,
   3575
  ],
  "none": [
   874,
   3575
  ],
  "cap": [
   9,
   55
  ]
 },
 "plan": {
  "def": "done",
  "reexport": "continue",
  "star": "continue",
  "none": "continue",
  "cap": "[\"symbols\", [\"rich/_unicode_data/__init__.py\", \"CellTable\"]]"
 },
 "adherence": null,
 "facts": [
  {
   "kind": "outline",
   "step": 1,
   "path": "rich/_unicode_data/__init__.py",
   "filter": null,
   "header": {
    "lines": 94,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "rich/_unicode_data/__init__.py",
     "name": "annotations",
     "line": 1,
     "kind": "from",
     "src": "__future__",
     "src_name": "annotations",
     "conditional": false,
     "col": 0
    },
    {
     "module": "rich/_unicode_data/__init__.py",
     "name": "bisect",
     "line": 3,
     "kind": "import",
     "src": "bisect",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "rich/_unicode_data/__init__.py",
     "name": "os",
     "line": 4,
     "kind": "import",
     "src": "os",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "rich/_unicode_data/__init__.py",
     "name": "sys",
     "line": 5,
     "kind": "import",
     "src": "sys",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "rich/_unicode_data/__init__.py",
     "name": "cache",
     "line": 8,
     "kind": "from",
     "src": "functools",
     "src_name": "cache",
     "conditional": false,
     "col": 0
    },
    {
     "module": "rich/_unicode_data/__init__.py",
     "name": "cache",
     "line": 10,
     "kind": "from",
     "src": "functools",
     "src_name": "lru_cache",
     "conditional": false,
     "col": 0
    },
    {
     "module": "rich/_unicode_data/__init__.py",
     "name": "import_module",
     "line": 12,
     "kind": "from",
     "src": "importlib",
     "src_name": "import_module",
     "conditional": false,
     "col": 0
    },
    {
     "module": "rich/_unicode_data/__init__.py",
     "name": "TYPE_CHECKING",
     "line": 13,
     "kind": "from",
     "src": "typing",
     "src_name": "TYPE_CHECKING",
     "conditional": false,
     "col": 0
    },
    {
     "module": "rich/_unicode_data/__init__.py",
     "name": "cast",
     "line": 13,
     "kind": "from",
     "src": "typing",
     "src_name": "cast",
     "conditional": false,
     "col": 0
    },
    {
     "module": "rich/_unicode_data/__init__.py",
     "name": "VERSIONS",
     "line": 15,
     "kind": "from",
     "src": "rich._unicode_data._versions",
     "src_name": "VERSIONS",
     "conditional": false,
     "col": 0
    },
    {
     "module": "rich/_unicode_data/__init__.py",
     "name": "CellTable",
     "line": 18,
     "kind": "from",
     "src": "rich.cells",
     "src_name": "CellTable",
     "conditional": false,
     "col": 0
    },
    {
     "module": "rich/_unicode_data/__init__.py",
     "name": "VERSION_ORDER",
     "line": 20,
     "kind": "assign",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "rich/_unicode_data/__init__.py",
     "name": "VERSION_SET",
     "line": 28,
     "kind": "assign",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "rich/_unicode_data/__init__.py",
     "name": "_parse_version",
     "line": 31,
     "kind": "def",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "rich/_unicode_data/__init__.py",
     "name": "load",
     "line": 59,
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
    "rich/_unicode_data/__init__.py",
    "CellTable",
    "reexport",
    [
     "rich.cells",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 2

The outline of `rich/_unicode_data/__init__.py` has 15 bindings; no `__all__`; no dynamic namespace tricks. This is not the branch I planned for that outcome; the open items changed more than expected.

Chain: `rich/_unicode_data/__init__.py` takes `CellTable` from `rich.cells` (module not yet located).

Still to settle: locate the module `rich.cells` imported by `rich/_unicode_data/__init__.py`.

Next: outline `rich/cells.py` filtered to `CellTable`, because `rich.cells` would be `rich/cells.py` if that file exists; one call both checks and closes it. I expect: a definition there ends the chain (about 85%); the file does not exist (about 10%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, grep `def`/`class CellTable` statements under `.`, is expected to open more follow-up work. Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done; missing: grep `def`/`class CellTable` statements under `.`.

**Call:** `symbols('rich/cells.py', 'CellTable')`

**Response**: outcome `def`

```
module rich/cells.py lines=353 dynamic=no all=none
38 class CellTable
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "rich/_unicode_data/__init__.py",
    "rich.cells"
   ],
   "desc": "locate the module `rich.cells` imported by `rich/_unicode_data/__init__.py`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('rich/cells.py', 'CellTable')",
   "key": "[\"symbols\", [\"rich/cells.py\", \"CellTable\"]]",
   "v1": [
    5354257399,
    4158917532
   ],
   "v2": [
    64576660615,
    49907010384
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     1165,
     1407
    ],
    "reexport": [
     233,
     11256
    ],
    "star": [
     233,
     123816
    ],
    "none": [
     3961,
     123816
    ],
    "missing": [
     31,
     264
    ]
   },
   "serves": [
    [
     "module_path",
     "rich/_unicode_data/__init__.py",
     "rich.cells"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+CellTable\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+CellTable\\\\b\", \".\"]]",
   "v1": [
    17341,
    8226
   ],
   "v2": [
    154629365227,
    74860515576
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
     "rich/_unicode_data/__init__.py",
     "rich.cells"
    ]
   ]
  },
  {
   "call": "ls('rich')",
   "key": "[\"ls\", [\"rich\"]]",
   "v1": [
    15465,
    7312
   ],
   "v2": [
    137556872251,
    66542680512
   ],
   "p_cap": [
    1,
    16
   ],
   "forecast": {
    "complete": [
     15,
     16
    ],
    "cap": [
     1,
     16
    ]
   },
   "serves": [
    [
     "module_path",
     "rich/_unicode_data/__init__.py",
     "rich.cells"
    ]
   ]
  },
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    8899,
    4113
   ],
   "v2": [
    77803146835,
    37430257788
   ],
   "p_cap": [
    1,
    9
   ],
   "forecast": {
    "complete": [
     8,
     9
    ],
    "cap": [
     1,
     9
    ]
   },
   "serves": [
    [
     "module_path",
     "rich/_unicode_data/__init__.py",
     "rich.cells"
    ]
   ]
  },
  {
   "call": "symbols('rich/cells/__init__.py', 'CellTable')",
   "key": "[\"symbols\", [\"rich/cells/__init__.py\", \"CellTable\"]]",
   "v1": [
    1308546053,
    439158720
   ],
   "v2": [
    328917263002091,
    142734049698240
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     31,
     1716
    ],
    "reexport": [
     217,
     3432
    ],
    "star": [
     31,
     17160
    ],
    "none": [
     589,
     17160
    ],
    "missing": [
     233,
     264
    ]
   },
   "serves": [
    [
     "module_path",
     "rich/_unicode_data/__init__.py",
     "rich.cells"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('rich/cells.py', 'CellTable')",
  "key": "[\"symbols\", [\"rich/cells.py\", \"CellTable\"]]",
  "provenance": "`rich.cells` would be `rich/cells.py` if that file exists; one call both checks and closes it",
  "v2": [
   64576660615,
   49907010384
  ]
 },
 "forecast": {
  "def": [
   1165,
   1407
  ],
  "reexport": [
   233,
   11256
  ],
  "star": [
   233,
   123816
  ],
  "none": [
   3961,
   123816
  ],
  "missing": [
   31,
   264
  ]
 },
 "plan": {
  "def": "done",
  "reexport": "continue",
  "star": "continue",
  "none": "done",
  "missing": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+CellTable\\\\b\", \".\"]]"
 },
 "adherence": {
  "planned": "done",
  "status": "deviated"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 2,
   "path": "rich/cells.py",
   "filter": "CellTable",
   "header": {
    "lines": 353,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "rich/cells.py",
     "name": "CellTable",
     "line": 38,
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
    "rich/_unicode_data/__init__.py",
    "CellTable",
    "reexport",
    [
     "rich.cells",
     "rich/cells.py"
    ]
   ],
   [
    "rich/cells.py",
    "CellTable",
    "class",
    38
   ]
  ]
 }
}
```
</details>

## Final

Certificate complete. The name resolves to `rich/cells.py:38`. In hindsight every one of the 2 calls was needed for the certificate.

**Answer:** `{"target": {"kind": "def", "path": "rich/cells.py", "line": 38, "name": "CellTable", "detail": "class"}, "text": "rich/cells.py:38"}`  
**Stopped:** certificate after 2 calls