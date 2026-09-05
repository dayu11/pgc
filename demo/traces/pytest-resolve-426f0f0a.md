# pytest-resolve-426f0f0a

**Repository:** pytest  
**Family:** resolve  
**Seed:** 0, prior 0140c5bd99319f8c

## Task

In `src/_pytest/mark/__init__.py`, line 20 imports `MarkDecorator` from `.structures`. Under the declared semantics, which definition does the module-level name `MarkDecorator` bound by this statement resolve to? Answer with `path:line`.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

Nothing seen yet beyond the task text.

Chain: `src/_pytest/mark/__init__.py` is not yet closed for `MarkDecorator`.

Outstanding: close the namespace of `src/_pytest/mark/__init__.py` for `MarkDecorator`.

Next: outline `src/_pytest/mark/__init__.py`, because module `src/_pytest/mark/__init__.py` (task). I expect: a re-export continues the chain to its source (about 50%); no binding at all points at a submodule or an unresolved name (about 25%); a capped outline means filtering by name (about 15%); a definition there ends the chain (about 10%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `src/_pytest/mark/__init__.py` filtered to `MarkDecorator`, is expected to open more follow-up work. Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: check for a submodule of that name; cap: outline `src/_pytest/mark/__init__.py` filtered to `MarkDecorator`.

**Call:** `symbols('src/_pytest/mark/__init__.py')`

**Response**: outcome `def`

```
module src/_pytest/mark/__init__.py lines=324 dynamic=no all=static@36
3 from annotations <- __future__ annotations
5 import collections <- collections
6 from Collection <- collections.abc Collection
7 from Iterable <- collections.abc Iterable
8 from AbstractSet <- collections.abc Set
9 import dataclasses <- dataclasses
10 from TYPE_CHECKING <- typing TYPE_CHECKING
12 from Expression <- .expression Expression
13 from _EmptyParameterSetMark <- .structures _EmptyParameterSetMark
14 from _HiddenParam <- .structures _HiddenParam
15 from EMPTY_PARAMETERSET_OPTION <- .structures EMPTY_PARAMETERSET_OPTION
16 from get_empty_parameterset_mark <- .structures get_empty_parameterset_mark
17 from HIDDEN_PARAM <- .structures HIDDEN_PARAM
18 from Mark <- .structures Mark
19 from MARK_GEN <- .structures MARK_GEN
20 from MarkDecorator <- .structures MarkDecorator
21 from MarkGenerator <- .structures MarkGenerator
22 from ParameterSet <- .structures ParameterSet
23 from NOTSET <- _pytest.compat NOTSET
24 from Config <- _pytest.config Config
25 from ExitCode <- _pytest.config ExitCode
26 from hookimpl <- _pytest.config hookimpl
27 from UsageError <- _pytest.config UsageError
28 from Parser <- _pytest.config.argparsing Parser
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
    "src/_pytest/mark/__init__.py",
    "MarkDecorator"
   ],
   "desc": "close the namespace of `src/_pytest/mark/__init__.py` for `MarkDecorator`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/mark/__init__.py')",
   "key": "[\"symbols\", [\"src/_pytest/mark/__init__.py\"]]",
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
     "src/_pytest/mark/__init__.py",
     "MarkDecorator"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/mark/__init__.py', 'MarkDecorator')",
   "key": "[\"symbols\", [\"src/_pytest/mark/__init__.py\", \"MarkDecorator\"]]",
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
     "src/_pytest/mark/__init__.py",
     "MarkDecorator"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/_pytest/mark/__init__.py')",
  "key": "[\"symbols\", [\"src/_pytest/mark/__init__.py\"]]",
  "provenance": "module `src/_pytest/mark/__init__.py` (task)",
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
  "cap": "[\"symbols\", [\"src/_pytest/mark/__init__.py\", \"MarkDecorator\"]]"
 },
 "adherence": null,
 "facts": [
  {
   "kind": "outline",
   "step": 1,
   "path": "src/_pytest/mark/__init__.py",
   "filter": null,
   "header": {
    "lines": 324,
    "dynamic": false,
    "all_status": "static",
    "all_line": 36
   },
   "bindings": [
    {
     "module": "src/_pytest/mark/__init__.py",
     "name": "annotations",
     "line": 3,
     "kind": "from",
     "src": "__future__",
     "src_name": "annotations",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/mark/__init__.py",
     "name": "collections",
     "line": 5,
     "kind": "import",
     "src": "collections",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/mark/__init__.py",
     "name": "Collection",
     "line": 6,
     "kind": "from",
     "src": "collections.abc",
     "src_name": "Collection",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/mark/__init__.py",
     "name": "Iterable",
     "line": 7,
     "kind": "from",
     "src": "collections.abc",
     "src_name": "Iterable",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/mark/__init__.py",
     "name": "AbstractSet",
     "line": 8,
     "kind": "from",
     "src": "collections.abc",
     "src_name": "Set",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/mark/__init__.py",
     "name": "dataclasses",
     "line": 9,
     "kind": "import",
     "src": "dataclasses",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/mark/__init__.py",
     "name": "TYPE_CHECKING",
     "line": 10,
     "kind": "from",
     "src": "typing",
     "src_name": "TYPE_CHECKING",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/mark/__init__.py",
     "name": "Expression",
     "line": 12,
     "kind": "from",
     "src": ".expression",
     "src_name": "Expression",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/mark/__init__.py",
     "name": "_EmptyParameterSetMark",
     "line": 13,
     "kind": "from",
     "src": ".structures",
     "src_name": "_EmptyParameterSetMark",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/mark/__init__.py",
     "name": "_HiddenParam",
     "line": 14,
     "kind": "from",
     "src": ".structures",
     "src_name": "_HiddenParam",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/mark/__init__.py",
     "name": "EMPTY_PARAMETERSET_OPTION",
     "line": 15,
     "kind": "from",
     "src": ".structures",
     "src_name": "EMPTY_PARAMETERSET_OPTION",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/mark/__init__.py",
     "name": "get_empty_parameterset_mark",
     "line": 16,
     "kind": "from",
     "src": ".structures",
     "src_name": "get_empty_parameterset_mark",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/mark/__init__.py",
     "name": "HIDDEN_PARAM",
     "line": 17,
     "kind": "from",
     "src": ".structures",
     "src_name": "HIDDEN_PARAM",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/mark/__init__.py",
     "name": "Mark",
     "line": 18,
     "kind": "from",
     "src": ".structures",
     "src_name": "Mark",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/mark/__init__.py",
     "name": "MARK_GEN",
     "line": 19,
     "kind": "from",
     "src": ".structures",
     "src_name": "MARK_GEN",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/mark/__init__.py",
     "name": "MarkDecorator",
     "line": 20,
     "kind": "from",
     "src": ".structures",
     "src_name": "MarkDecorator",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/_pytest/mark/__init__.py",
     "name": "MarkGenerator",
     "line": 21,
     "kind": "from",
   
```
</details>

## Step 2

The outline of `src/_pytest/mark/__init__.py` has 40 bindings; a literal `__all__` at line 36; no dynamic namespace tricks. This is not the branch I planned for that outcome; the open items changed more than expected.

Chain: `src/_pytest/mark/__init__.py` takes `MarkDecorator` from `.structures` (module not yet located).

Still to settle: locate the module `.structures` imported by `src/_pytest/mark/__init__.py`.

Next: outline `src/_pytest/mark/structures.py` filtered to `MarkDecorator`, because `.structures` would be `src/_pytest/mark/structures.py` if that file exists; one call both checks and closes it. I expect: a definition there ends the chain (about 85%); the file does not exist (about 10%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, list `src/_pytest/mark`, is expected to open more follow-up work. Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done; missing: list `src/_pytest/mark`.

**Call:** `symbols('src/_pytest/mark/structures.py', 'MarkDecorator')`

**Response**: outcome `def`

```
module src/_pytest/mark/structures.py lines=696 dynamic=no all=none
325 class MarkDecorator
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/_pytest/mark/__init__.py",
    ".structures"
   ],
   "desc": "locate the module `.structures` imported by `src/_pytest/mark/__init__.py`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/mark/structures.py', 'MarkDecorator')",
   "key": "[\"symbols\", [\"src/_pytest/mark/structures.py\", \"MarkDecorator\"]]",
   "v1": [
    12222137,
    9690076
   ],
   "v2": [
    1897399871,
    1501961780
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
     "src/_pytest/mark/__init__.py",
     ".structures"
    ]
   ]
  },
  {
   "call": "ls('src/_pytest/mark')",
   "key": "[\"ls\", [\"src/_pytest/mark\"]]",
   "v1": [
    73379,
    35340
   ],
   "v2": [
    59912911,
    29070228
   ],
   "p_cap": [
    3,
    155
   ],
   "forecast": {
    "complete": [
     152,
     155
    ],
    "cap": [
     3,
     155
    ]
   },
   "serves": [
    [
     "module_path",
     "src/_pytest/mark/__init__.py",
     ".structures"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+MarkDecorator\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+MarkDecorator\\\\b\", \".\"]]",
   "v1": [
    17809,
    8436
   ],
   "v2": [
    2224402193,
    1075598436
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
     "src/_pytest/mark/__init__.py",
     ".structures"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+MarkDecorator\\\\b', 'src')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+MarkDecorator\\\\b\", \"src\"]]",
   "v1": [
    21769,
    7410
   ],
   "v2": [
    1690742737,
    755825928
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
     "src/_pytest/mark/__init__.py",
     ".structures"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/mark/structures/__init__.py', 'MarkDecorator')",
   "key": "[\"symbols\", [\"src/_pytest/mark/structures/__init__.py\", \"MarkDecorator\"]]",
   "v1": [
    95225517,
    31660384
   ],
   "v2": [
    83315568871729,
    36330575583456
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     265,
     29064
    ],
    "reexport": [
     901,
     14532
    ],
    "star": [
     53,
     29064
    ],
    "none": [
     106,
     3633
    ],
    "missing": [
     466,
     519
    ]
   },
   "serves": [
    [
     "module_path",
     "src/_pytest/mark/__init__.py",
     ".structures"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/_pytest/mark/structures.py', 'MarkDecorator')",
  "key": "[\"symbols\", [\"src/_pytest/mark/structures.py\", \"MarkDecorator\"]]",
  "provenance": "`.structures` would be `src/_pytest/mark/structures.py` if that file exists; one call both checks and closes it",
  "v2": [
   1897399871,
   1501961780
  ]
 },
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
 "plan": {
  "def": "done",
  "reexport": "continue",
  "star": "continue",
  "none": "done",
  "missing": "[\"ls\", [\"src/_pytest/mark\"]]"
 },
 "adherence": {
  "planned": "done",
  "status": "deviated"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 2,
   "path": "src/_pytest/mark/structures.py",
   "filter": "MarkDecorator",
   "header": {
    "lines": 696,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/_pytest/mark/structures.py",
     "name": "MarkDecorator",
     "line": 325,
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
    "src/_pytest/mark/__init__.py",
    "MarkDecorator",
    "reexport",
    [
     ".structures",
     "src/_pytest/mark/structures.py"
    ]
   ],
   [
    "src/_pytest/mark/structures.py",
    "MarkDecorator",
    "class",
    325
   ]
  ]
 }
}
```
</details>

## Final

Certificate complete. The name resolves to `src/_pytest/mark/structures.py:325`. In hindsight every one of the 2 calls was needed for the certificate.

**Answer:** `{"target": {"kind": "def", "path": "src/_pytest/mark/structures.py", "line": 325, "name": "MarkDecorator", "detail": "class"}, "text": "src/_pytest/mark/structures.py:325"}`  
**Stopped:** certificate after 2 calls