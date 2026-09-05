# attrs-resolve-d9bafc19

**Repository:** attrs  
**Chain:** resolve  
**Seed:** 0, prior 0ac2a510ad43644e, floor 2

## Task

In `src/attr/_next_gen.py` line 12, `astuple` is imported from `._funcs` as `_astuple`. Which definition does the module-level name `_astuple` actually refer to? Give `path:line`.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N; bindings take effect in source order. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. A class derives from a definition when a base written as a bare name or `module.Name` resolves to it. A call site is `name(...)` where the bare name refers to the module-level binding (not a parameter or local). Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

I need to find what `_astuple` really is in `src/attr/_next_gen.py`: line 12 imports it from `._funcs`, so the definition is at least one hop away.

Next I will check `src/attr/_next_gen.py` for any other binding of `_astuple` besides the import on line 12; almost certainly the import is the only one, and then `._funcs` is the place to follow.

**Call:** `symbols('src/attr/_next_gen.py', '_astuple')`

**Response**: outcome `reexport`

```
module src/attr/_next_gen.py lines=679 dynamic=no all=none
12 from _astuple <- ._funcs astuple
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/attr/_next_gen.py",
    "_astuple"
   ],
   "desc": "check the top-level names of `src/attr/_next_gen.py` for `_astuple`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/_next_gen.py', '_astuple')",
   "key": "[\"symbols\", [\"src/attr/_next_gen.py\", \"_astuple\"]]",
   "v1": [
    22086579,
    7532750
   ],
   "v2": [
    22086579,
    7532750
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
     "src/attr/_next_gen.py",
     "_astuple"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/_next_gen.py')",
   "key": "[\"symbols\", [\"src/attr/_next_gen.py\"]]",
   "v1": [
    11990227001,
    3909497250
   ],
   "v2": [
    11990227001,
    3909497250
   ],
   "p_cap": [
    70,
    519
   ],
   "forecast": {
    "def": [
     449,
     51900
    ],
    "reexport": [
     13919,
     17300
    ],
    "star": [
     449,
     51900
    ],
    "none": [
     449,
     10380
    ],
    "cap": [
     70,
     519
    ]
   },
   "serves": [
    [
     "bindings",
     "src/attr/_next_gen.py",
     "_astuple"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/attr/_next_gen.py', '_astuple')",
  "key": "[\"symbols\", [\"src/attr/_next_gen.py\", \"_astuple\"]]",
  "provenance": "module `src/attr/_next_gen.py` (task), name `_astuple` (task)",
  "v2": [
   22086579,
   7532750
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
   "path": "src/attr/_next_gen.py",
   "filter": "_astuple",
   "header": {
    "lines": 679,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/attr/_next_gen.py",
     "name": "_astuple",
     "line": 12,
     "kind": "from",
     "src": "._funcs",
     "src_name": "astuple",
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
    "src/attr/_next_gen.py",
    "_astuple",
    "reexport",
    [
     "._funcs",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 2

`src/attr/_next_gen.py` does not define `_astuple` itself; line 12 imports it from `._funcs` under the name `astuple`.

So far: `src/attr/_next_gen.py` takes `_astuple` from `._funcs`, which I still have to locate.

Let me outline `src/attr/_funcs.py` directly, which both checks that the file exists and shows me `astuple`; if `._funcs` is a plain module that is where it has to be. Very likely it is defined right there. If the file does not exist, I will list `src/attr/` to see what lives there; if the name is not bound there, that finishes it. I could list `src/attr/` to see what lives there instead, but it tends to open more follow-up work.

**Call:** `symbols('src/attr/_funcs.py', 'astuple')`

**Response**: outcome `def`

```
module src/attr/_funcs.py lines=496 dynamic=no all=none
230 def astuple
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attr/_next_gen.py",
    "._funcs"
   ],
   "desc": "find where `._funcs` (imported by `src/attr/_next_gen.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/_funcs.py', 'astuple')",
   "key": "[\"symbols\", [\"src/attr/_funcs.py\", \"astuple\"]]",
   "v1": [
    13603250257,
    10976873955
   ],
   "v2": [
    3038575516186,
    2447842891965
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     61864,
     72861
    ],
    "reexport": [
     1628,
     72861
    ],
    "star": [
     148,
     72861
    ],
    "none": [
     2516,
     72861
    ],
    "missing": [
     15,
     163
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attr/_next_gen.py",
     "._funcs"
    ]
   ]
  },
  {
   "call": "ls('src/attr')",
   "key": "[\"ls\", [\"src/attr\"]]",
   "v1": [
    67179,
    32335
   ],
   "v2": [
    5040842963216,
    2447842891965
   ],
   "p_cap": [
    5,
    223
   ],
   "forecast": {
    "complete": [
     218,
     223
    ],
    "cap": [
     5,
     223
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attr/_next_gen.py",
     "._funcs"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+astuple\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+astuple\\\\b\", \".\"]]",
   "v1": [
    5509,
    2610
   ],
   "v2": [
    204044694713,
    98791865595
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
     "src/attr/_next_gen.py",
     "._funcs"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+astuple\\\\b', 'src')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+astuple\\\\b\", \"src\"]]",
   "v1": [
    19363,
    6670
   ],
   "v2": [
    186090070677,
    84156033655
   ],
   "p_cap": [
    1,
    184
   ],
   "forecast": {
    "zero": [
     155,
     184
    ],
    "mid": [
     7,
     46
    ],
    "cap": [
     1,
     184
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attr/_next_gen.py",
     "._funcs"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/_funcs/__init__.py', 'astuple')",
   "key": "[\"symbols\", [\"src/attr/_funcs/__init__.py\", \"astuple\"]]",
   "v1": [
    31637297,
    10588480
   ],
   "v2": [
    1801198508720323,
    801575243689920
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     55,
     2608
    ],
    "reexport": [
     15,
     326
    ],
    "star": [
     5,
     2608
    ],
    "none": [
     15,
     652
    ],
    "missing": [
     148,
     163
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attr/_next_gen.py",
     "._funcs"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/attr/_funcs.py', 'astuple')",
  "key": "[\"symbols\", [\"src/attr/_funcs.py\", \"astuple\"]]",
  "provenance": "`._funcs` would be `src/attr/_funcs.py` if that file exists; one call both checks and closes it",
  "v2": [
   3038575516186,
   2447842891965
  ]
 },
 "forecast": {
  "def": [
   61864,
   72861
  ],
  "reexport": [
   1628,
   72861
  ],
  "star": [
   148,
   72861
  ],
  "none": [
   2516,
   72861
  ],
  "missing": [
   15,
   163
  ]
 },
 "plan": {
  "def": "done",
  "reexport": "continue",
  "star": "continue",
  "none": "done",
  "missing": "[\"ls\", [\"src/attr\"]]"
 },
 "hedges": [
  {
   "outcome": "def",
   "word": "very likely",
   "p": [
    61864,
    72861
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
   "path": "src/attr/_funcs.py",
   "filter": "astuple",
   "header": {
    "lines": 496,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/attr/_funcs.py",
     "name": "astuple",
     "line": 230,
     "kind": "def",
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
    "src/attr/_next_gen.py",
    "_astuple",
    "reexport",
    [
     "._funcs",
     "src/attr/_funcs.py"
    ]
   ],
   [
    "src/attr/_funcs.py",
    "astuple",
    "def",
    230
   ]
  ]
 }
}
```
</details>

## Final

`_astuple` is the def at `src/attr/_funcs.py:230`. Looking back, all 2 calls were needed.

**Answer:** `{"final_kind": "resolve", "final": {"kind": "def", "path": "src/attr/_funcs.py", "line": 230, "name": "astuple", "detail": "def"}, "steps": [{"op": "resolve", "output": {"kind": "def", "path": "src/attr/_funcs.py", "line": 230, "name": "astuple", "detail": "def"}}], "stuck": null}`  
**Stopped:** certificate after 2 calls