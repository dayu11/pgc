# httpx-resolve-f733f017

**Repository:** httpx  
**Chain:** resolve  
**Seed:** 0, prior 708591d2904e1ac3, floor 2

## Task

In `httpx/_utils.py` line 9, `PrimitiveData` is imported from `._types`. Which definition does the module-level name `PrimitiveData` actually refer to? Give `path:line`.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N; bindings take effect in source order. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. A class derives from a definition when a base written as a bare name or `module.Name` resolves to it. A call site is `name(...)` where the bare name refers to the module-level binding (not a parameter or local). Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

I need to find what `PrimitiveData` really is in `httpx/_utils.py`: line 9 imports it from `._types`, so the definition is at least one hop away.

Next I will check `httpx/_utils.py` for any other binding of `PrimitiveData` besides the import on line 9; almost certainly the import is the only one, and then `._types` is the place to follow.

**Call:** `symbols('httpx/_utils.py', 'PrimitiveData')`

**Response**: outcome `reexport`

```
module httpx/_utils.py lines=243 dynamic=no all=none
9 from PrimitiveData <- ._types PrimitiveData
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "httpx/_utils.py",
    "PrimitiveData"
   ],
   "desc": "check the top-level names of `httpx/_utils.py` for `PrimitiveData`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/_utils.py', 'PrimitiveData')",
   "key": "[\"symbols\", [\"httpx/_utils.py\", \"PrimitiveData\"]]",
   "v1": [
    8983007,
    3056200
   ],
   "v2": [
    8983007,
    3056200
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
     "httpx/_utils.py",
     "PrimitiveData"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_utils.py')",
   "key": "[\"symbols\", [\"httpx/_utils.py\"]]",
   "v1": [
    1945056049,
    632633400
   ],
   "v2": [
    1945056049,
    632633400
   ],
   "p_cap": [
    28,
    207
   ],
   "forecast": {
    "def": [
     179,
     20700
    ],
    "reexport": [
     5549,
     6900
    ],
    "star": [
     179,
     20700
    ],
    "none": [
     179,
     4140
    ],
    "cap": [
     28,
     207
    ]
   },
   "serves": [
    [
     "bindings",
     "httpx/_utils.py",
     "PrimitiveData"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('httpx/_utils.py', 'PrimitiveData')",
  "key": "[\"symbols\", [\"httpx/_utils.py\", \"PrimitiveData\"]]",
  "provenance": "module `httpx/_utils.py` (task), name `PrimitiveData` (task)",
  "v2": [
   8983007,
   3056200
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
   "path": "httpx/_utils.py",
   "filter": "PrimitiveData",
   "header": {
    "lines": 243,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "httpx/_utils.py",
     "name": "PrimitiveData",
     "line": 9,
     "kind": "from",
     "src": "._types",
     "src_name": "PrimitiveData",
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
    "httpx/_utils.py",
    "PrimitiveData",
    "reexport",
    [
     "._types",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 2

`httpx/_utils.py` does not define `PrimitiveData` itself; line 9 imports it from `._types`.

So far: `httpx/_utils.py` takes `PrimitiveData` from `._types`, which I still have to locate.

Let me outline `httpx/_types.py` directly, which both checks that the file exists and shows me `PrimitiveData`; if `._types` is a plain module that is where it has to be. Very likely it is defined right there. If the file does not exist, I will search the whole tree for `class PrimitiveData`/`def PrimitiveData`; if the name is not bound there, that finishes it. I could search the whole tree for `class PrimitiveData`/`def PrimitiveData` instead, but it tends to open more follow-up work.

**Call:** `symbols('httpx/_types.py', 'PrimitiveData')`

**Response**: outcome `def`

```
module httpx/_types.py lines=115 dynamic=no all=static@89
31 assign PrimitiveData
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/_utils.py",
    "._types"
   ],
   "desc": "find where `._types` (imported by `httpx/_utils.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/_types.py', 'PrimitiveData')",
   "key": "[\"symbols\", [\"httpx/_types.py\", \"PrimitiveData\"]]",
   "v1": [
    1022641917,
    733426876
   ],
   "v2": [
    29899644617,
    21269379404
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     18565,
     23998
    ],
    "reexport": [
     282,
     11999
    ],
    "star": [
     47,
     23998
    ],
    "none": [
     423,
     11999
    ],
    "missing": [
     28,
     169
    ]
   },
   "serves": [
    [
     "module_path",
     "httpx/_utils.py",
     "._types"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+PrimitiveData\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+PrimitiveData\\\\b\", \".\"]]",
   "v1": [
    25534,
    11977
   ],
   "v2": [
    22181918497,
    10634689702
   ],
   "p_cap": [
    1,
    29
   ],
   "forecast": {
    "zero": [
     1,
     29
    ],
    "mid": [
     27,
     29
    ],
    "cap": [
     1,
     29
    ]
   },
   "serves": [
    [
     "module_path",
     "httpx/_utils.py",
     "._types"
    ]
   ]
  },
  {
   "call": "ls('httpx')",
   "key": "[\"ls\", [\"httpx\"]]",
   "v1": [
    48073,
    22302
   ],
   "v2": [
    82918613261,
    39605051304
   ],
   "p_cap": [
    5,
    54
   ],
   "forecast": {
    "complete": [
     49,
     54
    ],
    "cap": [
     5,
     54
    ]
   },
   "serves": [
    [
     "module_path",
     "httpx/_utils.py",
     "._types"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_types/__init__.py', 'PrimitiveData')",
   "key": "[\"symbols\", [\"httpx/_types/__init__.py\", \"PrimitiveData\"]]",
   "v1": [
    197958877,
    66795729
   ],
   "v2": [
    285374723584385,
    118619328936108
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     28,
     1131
    ],
    "reexport": [
     1372,
     14703
    ],
    "star": [
     28,
     14703
    ],
    "none": [
     224,
     4901
    ],
    "missing": [
     141,
     169
    ]
   },
   "serves": [
    [
     "module_path",
     "httpx/_utils.py",
     "._types"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('httpx/_types.py', 'PrimitiveData')",
  "key": "[\"symbols\", [\"httpx/_types.py\", \"PrimitiveData\"]]",
  "provenance": "`._types` would be `httpx/_types.py` if that file exists; one call both checks and closes it",
  "v2": [
   29899644617,
   21269379404
  ]
 },
 "forecast": {
  "def": [
   18565,
   23998
  ],
  "reexport": [
   282,
   11999
  ],
  "star": [
   47,
   23998
  ],
  "none": [
   423,
   11999
  ],
  "missing": [
   28,
   169
  ]
 },
 "plan": {
  "def": "done",
  "reexport": "continue",
  "star": "continue",
  "none": "done",
  "missing": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+PrimitiveData\\\\b\", \".\"]]"
 },
 "hedges": [
  {
   "outcome": "def",
   "word": "very likely",
   "p": [
    18565,
    23998
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
   "step": 2,
   "path": "httpx/_types.py",
   "filter": "PrimitiveData",
   "header": {
    "lines": 115,
    "dynamic": false,
    "all_status": "static",
    "all_line": 89
   },
   "bindings": [
    {
     "module": "httpx/_types.py",
     "name": "PrimitiveData",
     "line": 31,
     "kind": "assign",
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
    "httpx/_utils.py",
    "PrimitiveData",
    "reexport",
    [
     "._types",
     "httpx/_types.py"
    ]
   ],
   [
    "httpx/_types.py",
    "PrimitiveData",
    "assign",
    31
   ]
  ]
 }
}
```
</details>

## Final

`PrimitiveData` is the assign at `httpx/_types.py:31`. Looking back, all 2 calls were needed.

**Answer:** `{"final_kind": "resolve", "final": {"kind": "def", "path": "httpx/_types.py", "line": 31, "name": "PrimitiveData", "detail": "assign"}, "steps": [{"op": "resolve", "output": {"kind": "def", "path": "httpx/_types.py", "line": 31, "name": "PrimitiveData", "detail": "assign"}}], "stuck": null}`  
**Stopped:** certificate after 2 calls