# click-subclasses-7ada152a

**Repository:** click  
**Chain:** resolve → subclasses  
**Seed:** 0, prior 81b2b7394c71c459, floor 5

## Task

In `src/click/termui.py` line 19, `UsageError` is imported from `.exceptions`. Which definition does the module-level name `UsageError` actually refer to? Give `path:line`. Then list every class that derives from it directly, as `path:line:ClassName`, making sure each base name really resolves to this definition.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N; bindings take effect in source order. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. A class derives from a definition when a base written as a bare name or `module.Name` resolves to it. A call site is `name(...)` where the bare name refers to the module-level binding (not a parameter or local). Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

I need to find what `UsageError` really is in `src/click/termui.py`: line 19 imports it from `.exceptions`, so the definition is at least one hop away. Then I need every class that derives from it, checking that each base name really points at this definition.

Next I will check `src/click/termui.py` for any other binding of `UsageError` besides the import on line 19; almost certainly the import is the only one, and then `.exceptions` is the place to follow.

**Call:** `symbols('src/click/termui.py', 'UsageError')`

**Response**: outcome `reexport`

```
module src/click/termui.py lines=1015 dynamic=no all=none
19 from UsageError <- .exceptions UsageError
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/click/termui.py",
    "UsageError"
   ],
   "desc": "check the top-level names of `src/click/termui.py` for `UsageError`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/click/termui.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/click/termui.py\", \"UsageError\"]]",
   "v1": [
    65626933,
    22453600
   ],
   "v2": [
    65626933,
    22453600
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
     "src/click/termui.py",
     "UsageError"
    ]
   ]
  },
  {
   "call": "symbols('src/click/termui.py')",
   "key": "[\"symbols\", [\"src/click/termui.py\"]]",
   "v1": [
    13924023879,
    4558080800
   ],
   "v2": [
    13924023879,
    4558080800
   ],
   "p_cap": [
    134,
    1015
   ],
   "forecast": {
    "def": [
     881,
     101500
    ],
    "reexport": [
     81933,
     101500
    ],
    "star": [
     881,
     101500
    ],
    "none": [
     881,
     20300
    ],
    "cap": [
     134,
     1015
    ]
   },
   "serves": [
    [
     "bindings",
     "src/click/termui.py",
     "UsageError"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/click/termui.py', 'UsageError')",
  "key": "[\"symbols\", [\"src/click/termui.py\", \"UsageError\"]]",
  "provenance": "module `src/click/termui.py` (task), name `UsageError` (task)",
  "v2": [
   65626933,
   22453600
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
   "path": "src/click/termui.py",
   "filter": "UsageError",
   "header": {
    "lines": 1015,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/click/termui.py",
     "name": "UsageError",
     "line": 19,
     "kind": "from",
     "src": ".exceptions",
     "src_name": "UsageError",
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
  "of": 2,
  "chain": [
   [
    "src/click/termui.py",
    "UsageError",
    "reexport",
    [
     ".exceptions",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 2

`src/click/termui.py` does not define `UsageError` itself; line 19 imports it from `.exceptions`.

So far: `src/click/termui.py` takes `UsageError` from `.exceptions`, which I still have to locate.

Let me outline `src/click/exceptions.py` directly, which both checks that the file exists and shows me `UsageError`; if `.exceptions` is a plain module that is where it has to be. Very likely it is defined right there. If the file does not exist, I will list `src/click/` to see what lives there; if the name is not bound there, that finishes it. I could list `src/click/` to see what lives there instead, but it tends to open more follow-up work.

**Call:** `symbols('src/click/exceptions.py', 'UsageError')`

**Response**: outcome `def`

```
module src/click/exceptions.py lines=379 dynamic=no all=none
68 class UsageError (ClickException)
114 class BadParameter (UsageError)
232 class NoSuchOption (UsageError)
268 class NoSuchCommand (UsageError)
304 class BadOptionUsage (UsageError)
323 class BadArgumentUsage (UsageError)
332 class NoArgsIsHelpError (UsageError)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/click/termui.py",
    ".exceptions"
   ],
   "desc": "find where `.exceptions` (imported by `src/click/termui.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/click/exceptions.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/click/exceptions.py\", \"UsageError\"]]",
   "v1": [
    68958920917,
    52571960896
   ],
   "v2": [
    483879584547,
    368003726272
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     95637,
     117068
    ],
    "reexport": [
     4041,
     234136
    ],
    "star": [
     449,
     234136
    ],
    "none": [
     898,
     29267
    ],
    "missing": [
     69,
     518
    ]
   },
   "serves": [
    [
     "module_path",
     "src/click/termui.py",
     ".exceptions"
    ]
   ]
  },
  {
   "call": "ls('src/click')",
   "key": "[\"ls\", [\"src/click\"]]",
   "v1": [
    19205,
    9282
   ],
   "v2": [
    4529963367445,
    2208022357632
   ],
   "p_cap": [
    1,
    42
   ],
   "forecast": {
    "complete": [
     41,
     42
    ],
    "cap": [
     1,
     42
    ]
   },
   "serves": [
    [
     "module_path",
     "src/click/termui.py",
     ".exceptions"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+UsageError\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+UsageError\\\\b\", \".\"]]",
   "v1": [
    1390,
    663
   ],
   "v2": [
    162361664425,
    78857941344
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
     "src/click/termui.py",
     ".exceptions"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+UsageError\\\\b', 'src')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+UsageError\\\\b\", \"src\"]]",
   "v1": [
    72061,
    24752
   ],
   "v2": [
    13401336689141,
    5888059620352
   ],
   "p_cap": [
    1,
    224
   ],
   "forecast": {
    "zero": [
     193,
     224
    ],
    "mid": [
     15,
     112
    ],
    "cap": [
     1,
     224
    ]
   },
   "serves": [
    [
     "module_path",
     "src/click/termui.py",
     ".exceptions"
    ]
   ]
  },
  {
   "call": "symbols('src/click/exceptions/__init__.py', 'UsageError')",
   "key": "[\"symbols\", [\"src/click/exceptions/__init__.py\", \"UsageError\"]]",
   "v1": [
    37996589,
    12821536
   ],
   "v2": [
    63387622850257,
    27232275744128
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     23,
     1036
    ],
    "reexport": [
     115,
     1554
    ],
    "star": [
     23,
     12432
    ],
    "none": [
     437,
     12432
    ],
    "missing": [
     449,
     518
    ]
   },
   "serves": [
    [
     "module_path",
     "src/click/termui.py",
     ".exceptions"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/click/exceptions.py', 'UsageError')",
  "key": "[\"symbols\", [\"src/click/exceptions.py\", \"UsageError\"]]",
  "provenance": "`.exceptions` would be `src/click/exceptions.py` if that file exists; one call both checks and closes it",
  "v2": [
   483879584547,
   368003726272
  ]
 },
 "forecast": {
  "def": [
   95637,
   117068
  ],
  "reexport": [
   4041,
   234136
  ],
  "star": [
   449,
   234136
  ],
  "none": [
   898,
   29267
  ],
  "missing": [
   69,
   518
  ]
 },
 "plan": {
  "def": "done",
  "reexport": "continue",
  "star": "continue",
  "none": "done",
  "missing": "[\"ls\", [\"src/click\"]]"
 },
 "hedges": [
  {
   "outcome": "def",
   "word": "very likely",
   "p": [
    95637,
    117068
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
   "path": "src/click/exceptions.py",
   "filter": "UsageError",
   "header": {
    "lines": 379,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/click/exceptions.py",
     "name": "UsageError",
     "line": 68,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "ClickException"
     ]
    },
    {
     "module": "src/click/exceptions.py",
     "name": "BadParameter",
     "line": 114,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "UsageError"
     ]
    },
    {
     "module": "src/click/exceptions.py",
     "name": "NoSuchOption",
     "line": 232,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "UsageError"
     ]
    },
    {
     "module": "src/click/exceptions.py",
     "name": "NoSuchCommand",
     "line": 268,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "UsageError"
     ]
    },
    {
     "module": "src/click/exceptions.py",
     "name": "BadOptionUsage",
     "line": 304,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "UsageError"
     ]
    },
    {
     "module": "src/click/exceptions.py",
     "name": "BadArgumentUsage",
     "line": 323,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "UsageError"
     ]
    },
    {
     "module": "src/click/exceptions.py",
     "name": "NoArgsIsHelpError",
     "line": 332,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "UsageError"
     ]
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "resolve",
  "step": 1,
  "of": 2,
  "chain": [
   [
    "src/click/termui.py",
    "UsageError",
    "reexport",
    [
```
</details>

## Step 3

There it is: `UsageError` is a class at `src/click/exceptions.py:68`. That settles the definition; now its subclasses.

I'll search the whole tree for classes deriving from `UsageError`; the search has to be complete before I can call the set final. Very likely nothing turns up. If it fits under the cap or it caps, I follow whatever it opens up.

**Call:** `grep('^\\s*class\\s+\\w+\\s*\\(.*\\bUsageError\\b', '.')`

**Response**: outcome `mid`

```
src/click/exceptions.py:114:class BadParameter(UsageError):
src/click/exceptions.py:232:class NoSuchOption(UsageError):
src/click/exceptions.py:268:class NoSuchCommand(UsageError):
src/click/exceptions.py:304:class BadOptionUsage(UsageError):
src/click/exceptions.py:323:class BadArgumentUsage(UsageError):
src/click/exceptions.py:332:class NoArgsIsHelpError(UsageError):
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "cover",
   "key": [
    "cover",
    "SUBCLASS",
    "."
   ],
   "desc": "search `.` for classes deriving from `UsageError`"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*class\\\\s+\\\\w+\\\\s*\\\\(.*\\\\bUsageError\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*class\\\\s+\\\\w+\\\\s*\\\\(.*\\\\bUsageError\\\\b\", \".\"]]",
   "v1": [
    614758073,
    419499990
   ],
   "v2": [
    614758073,
    419499990
   ],
   "p_cap": [
    1,
    18
   ],
   "forecast": {
    "zero": [
     31,
     36
    ],
    "mid": [
     1,
     12
    ],
    "cap": [
     1,
     18
    ]
   },
   "serves": [
    [
     "cover",
     "SUBCLASS",
     "."
    ]
   ]
  }
 ],
 "choice": {
  "call": "grep('^\\\\s*class\\\\s+\\\\w+\\\\s*\\\\(.*\\\\bUsageError\\\\b', '.')",
  "key": "[\"grep\", [\"^\\\\s*class\\\\s+\\\\w+\\\\s*\\\\(.*\\\\bUsageError\\\\b\", \".\"]]",
  "provenance": "subclass lines naming `UsageError` under `.` (derived)",
  "v2": [
   614758073,
   419499990
  ]
 },
 "forecast": {
  "zero": [
   31,
   36
  ],
  "mid": [
   1,
   12
  ],
  "cap": [
   1,
   18
  ]
 },
 "plan": {
  "zero": "done",
  "mid": "continue",
  "cap": "continue"
 },
 "hedges": [
  {
   "outcome": "zero",
   "word": "very likely",
   "p": [
    31,
    36
   ]
  }
 ],
 "adherence": {
  "planned": "done",
  "status": "deviated"
 },
 "facts": [
  {
   "kind": "grep",
   "step": 3,
   "pattern": "^\\s*class\\s+\\w+\\s*\\(.*\\bUsageError\\b",
   "scope": ".",
   "hits": [
    [
     "src/click/exceptions.py",
     114
    ],
    [
     "src/click/exceptions.py",
     232
    ],
    [
     "src/click/exceptions.py",
     268
    ],
    [
     "src/click/exceptions.py",
     304
    ],
    [
     "src/click/exceptions.py",
     323
    ],
    [
     "src/click/exceptions.py",
     332
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "phase": "subclasses",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/click/exceptions.py"
  ],
  "table": [
   [
    "src/click/exceptions.py",
    "src/click/exceptions.py:114:BadParameter",
    "in",
    "base `UsageError` resolves to the target"
   ],
   [
    "src/click/exceptions.py",
    "src/click/exceptions.py:232:NoSuchOption",
    "in",
    "base `UsageError` resolves to the target"
   ],
   [
    "src/click/exceptions.py",
    "src/click/exceptions.py:268:NoSuchCommand",
    "in",
    "base `UsageError` resolves to the target"
   ],
   [
    "src/click/exceptions.py",
    "src/click/exceptions.py:304:BadOptionUsage",
    "in",
    "base `UsageError` resolves to the target"
   ],
   [
    "src/click/exceptions.py",
    "src/click/exceptions.py:323:BadArgumentUsage",
    "in",
    "base `UsageError` resolves to the target"
   ],
   [
    "src/click/exceptions.py",
    "src/click/exceptions.py:332:NoArgsIsHelpError",
    "in",
    "base `UsageError` resolves to the target"
   ]
  ],
  "uncovered": {
   "SUBCLASS": []
  },
  "n_in": 6,
  "n_out": 0,
  "n_pending": 0
 }
}
```
</details>

## Final

`UsageError` is the class at `src/click/exceptions.py:68`. 6 classes derive from it directly: `BadParameter` (`src/click/exceptions.py:114`), `NoSuchOption` (`src/click/exceptions.py:232`), `NoSuchCommand` (`src/click/exceptions.py:268`), `BadOptionUsage` (`src/click/exceptions.py:304`), `BadArgumentUsage` (`src/click/exceptions.py:323`), `NoArgsIsHelpError` (`src/click/exceptions.py:332`). Looking back, all 3 calls were needed.

**Answer:** `{"final_kind": "subclasses", "final": ["src/click/exceptions.py:114:BadParameter", "src/click/exceptions.py:232:NoSuchOption", "src/click/exceptions.py:268:NoSuchCommand", "src/click/exceptions.py:304:BadOptionUsage", "src/click/exceptions.py:323:BadArgumentUsage", "src/click/exceptions.py:332:NoArgsIsHelpError"], "steps": [{"op": "resolve", "output": {"kind": "def", "path": "src/click/exceptions.py", "line": 68, "name": "UsageError", "detail": "class"}}, {"op": "subclasses", "output": ["src/click/exceptions.py:114:BadParameter", "src/click/exceptions.py:232:NoSuchOption", "src/click/exceptions.py:268:NoSuchCommand", "src/click/exceptions.py:304:BadOptionUsage", "src/click/exceptions.py:323:BadArgumentUsage", "src/click/exceptions.py:332:NoArgsIsHelpError"]}], "stuck": null}`  
**Stopped:** certificate after 3 calls