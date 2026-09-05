# attrs-resolve-b134577c

**Repository:** attrs  
**Family:** resolve  
**Seed:** 0, prior df2023878106d754

## Task

In `src/attr/_version_info.py`, line 6 imports `astuple` from `._funcs`. Under the declared semantics, which definition does the module-level name `astuple` bound by this statement resolve to? Answer with `path:line`.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

Nothing seen yet beyond the task text.

Chain: `src/attr/_version_info.py` is not yet closed for `astuple`.

Outstanding: close the namespace of `src/attr/_version_info.py` for `astuple`.

Next: outline `src/attr/_version_info.py`, because module `src/attr/_version_info.py` (task). I expect: a definition there ends the chain (about 80%); a capped outline means filtering by name (about 15%); a re-export continues the chain to its source (under 5%); no binding at all points at a submodule or an unresolved name (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `src/attr/_version_info.py` filtered to `astuple`, is expected to open more follow-up work. Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done; cap: outline `src/attr/_version_info.py` filtered to `astuple`.

**Call:** `symbols('src/attr/_version_info.py')`

**Response**: outcome `def`

```
module src/attr/_version_info.py lines=90 dynamic=no all=none
4 from total_ordering <- functools total_ordering
6 from astuple <- ._funcs astuple
7 from attrib <- ._make attrib
7 from attrs <- ._make attrs
12 class VersionInfo
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/attr/_version_info.py",
    "astuple"
   ],
   "desc": "close the namespace of `src/attr/_version_info.py` for `astuple`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/_version_info.py')",
   "key": "[\"symbols\", [\"src/attr/_version_info.py\"]]",
   "v1": [
    11618714673,
    9714246868
   ],
   "v2": [
    14077374709,
    9714246868
   ],
   "p_cap": [
    70,
    519
   ],
   "forecast": {
    "def": [
     25144,
     30621
    ],
    "reexport": [
     5837,
     244968
    ],
    "star": [
     449,
     244968
    ],
    "none": [
     2245,
     122484
    ],
    "cap": [
     70,
     519
    ]
   },
   "serves": [
    [
     "bindings",
     "src/attr/_version_info.py",
     "astuple"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/_version_info.py', 'astuple')",
   "key": "[\"symbols\", [\"src/attr/_version_info.py\", \"astuple\"]]",
   "v1": [
    6989649,
    2379310
   ],
   "v2": [
    6989649,
    2379310
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
     "src/attr/_version_info.py",
     "astuple"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/attr/_version_info.py')",
  "key": "[\"symbols\", [\"src/attr/_version_info.py\"]]",
  "provenance": "module `src/attr/_version_info.py` (task)",
  "v2": [
   14077374709,
   9714246868
  ]
 },
 "forecast": {
  "def": [
   25144,
   30621
  ],
  "reexport": [
   5837,
   244968
  ],
  "star": [
   449,
   244968
  ],
  "none": [
   2245,
   122484
  ],
  "cap": [
   70,
   519
  ]
 },
 "plan": {
  "def": "done",
  "reexport": "continue",
  "star": "continue",
  "none": "done",
  "cap": "[\"symbols\", [\"src/attr/_version_info.py\", \"astuple\"]]"
 },
 "adherence": null,
 "facts": [
  {
   "kind": "outline",
   "step": 1,
   "path": "src/attr/_version_info.py",
   "filter": null,
   "header": {
    "lines": 90,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/attr/_version_info.py",
     "name": "total_ordering",
     "line": 4,
     "kind": "from",
     "src": "functools",
     "src_name": "total_ordering",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/attr/_version_info.py",
     "name": "astuple",
     "line": 6,
     "kind": "from",
     "src": "._funcs",
     "src_name": "astuple",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/attr/_version_info.py",
     "name": "attrib",
     "line": 7,
     "kind": "from",
     "src": "._make",
     "src_name": "attrib",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/attr/_version_info.py",
     "name": "attrs",
     "line": 7,
     "kind": "from",
     "src": "._make",
     "src_name": "attrs",
     "conditional": false,
     "col": 0
    },
    {
     "module": "src/attr/_version_info.py",
     "name": "VersionInfo",
     "line": 12,
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
    "src/attr/_version_info.py",
    "astuple",
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

The outline of `src/attr/_version_info.py` has 5 bindings; no `__all__`; no dynamic namespace tricks. This is not the branch I planned for that outcome; the open items changed more than expected.

Chain: `src/attr/_version_info.py` takes `astuple` from `._funcs` (module not yet located).

Still to settle: locate the module `._funcs` imported by `src/attr/_version_info.py`.

Next: outline `src/attr/_funcs.py` filtered to `astuple`, because `._funcs` would be `src/attr/_funcs.py` if that file exists; one call both checks and closes it. I expect: a definition there ends the chain (about 85%); the file does not exist (about 10%); a re-export continues the chain to its source (under 5%); no binding at all points at a submodule or an unresolved name (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, list `src/attr`, is expected to open more follow-up work. Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done; missing: list `src/attr`.

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
    "src/attr/_version_info.py",
    "._funcs"
   ],
   "desc": "locate the module `._funcs` imported by `src/attr/_version_info.py`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/_funcs.py', 'astuple')",
   "key": "[\"symbols\", [\"src/attr/_funcs.py\", \"astuple\"]]",
   "v1": [
    36712633883,
    29198892320
   ],
   "v2": [
    8201236043489,
    6511352987360
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     3283,
     3835
    ],
    "reexport": [
     469,
     18880
    ],
    "star": [
     469,
     245440
    ],
    "none": [
     469,
     24544
    ],
    "missing": [
     51,
     520
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attr/_version_info.py",
     "._funcs"
    ]
   ]
  },
  {
   "call": "ls('src/attr')",
   "key": "[\"ls\", [\"src/attr\"]]",
   "v1": [
    106401,
    51067
   ],
   "v2": [
    2689884647739,
    1302270597472
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
     "src/attr/_version_info.py",
     "._funcs"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+astuple\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+astuple\\\\b\", \".\"]]",
   "v1": [
    5893,
    2748
   ],
   "v2": [
    727923093563,
    350386707840
   ],
   "p_cap": [
    1,
    24
   ],
   "forecast": {
    "zero": [
     1,
     24
    ],
    "mid": [
     11,
     12
    ],
    "cap": [
     1,
     24
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attr/_version_info.py",
     "._funcs"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+astuple\\\\b', 'src')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+astuple\\\\b\", \"src\"]]",
   "v1": [
    47252,
    16259
   ],
   "v2": [
    230835156977,
    103656067736
   ],
   "p_cap": [
    2,
    213
   ],
   "forecast": {
    "zero": [
     178,
     213
    ],
    "mid": [
     11,
     71
    ],
    "cap": [
     2,
     213
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attr/_version_info.py",
     "._funcs"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/_funcs/__init__.py', 'astuple')",
   "key": "[\"symbols\", [\"src/attr/_funcs/__init__.py\", \"astuple\"]]",
   "v1": [
    179061797,
    60016320
   ],
   "v2": [
    2160458417195501,
    956555712403200
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     17,
     936
    ],
    "reexport": [
     187,
     4680
    ],
    "star": [
     17,
     9360
    ],
    "none": [
     119,
     3120
    ],
    "missing": [
     469,
     520
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attr/_version_info.py",
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
   8201236043489,
   6511352987360
  ]
 },
 "forecast": {
  "def": [
   3283,
   3835
  ],
  "reexport": [
   469,
   18880
  ],
  "star": [
   469,
   245440
  ],
  "none": [
   469,
   24544
  ],
  "missing": [
   51,
   520
  ]
 },
 "plan": {
  "def": "done",
  "reexport": "continue",
  "star": "continue",
  "none": "done",
  "missing": "[\"ls\", [\"src/attr\"]]"
 },
 "adherence": {
  "planned": "done",
  "status": "deviated"
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
     "col": 0
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "chain": [
   [
    "src/attr/_version_info.py",
    "astuple",
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

Certificate complete. The name resolves to `src/attr/_funcs.py:230`. In hindsight every one of the 2 calls was needed for the certificate.

**Answer:** `{"target": {"kind": "def", "path": "src/attr/_funcs.py", "line": 230, "name": "astuple", "detail": "def"}, "text": "src/attr/_funcs.py:230"}`  
**Stopped:** certificate after 2 calls