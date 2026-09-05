# pytest-importers-dd54ab7d

**Repository:** pytest  
**Chain:** resolve → importers  
**Seed:** 0, prior 8e41e8743065d192, floor 8

## Task

In `src/_pytest/mark/__init__.py` line 22, `ParameterSet` is imported from `.structures`. Which definition does the module-level name `ParameterSet` actually refer to? Give `path:line`. Then list every module-level import statement in the repository that brings in that definition, including through re-exports and star imports, as `path:line`.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N; bindings take effect in source order. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. A class derives from a definition when a base written as a bare name or `module.Name` resolves to it. A call site is `name(...)` where the bare name refers to the module-level binding (not a parameter or local). Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

I need to find what `ParameterSet` really is in `src/_pytest/mark/__init__.py`: line 22 imports it from `.structures`, so the definition is at least one hop away. Then I have to find every module-level import of that definition, which means a complete search, not a sample.

Next I will check `src/_pytest/mark/__init__.py` for any other binding of `ParameterSet` besides the import on line 22; almost certainly the import is the only one, and then `.structures` is the place to follow.

**Call:** `symbols('src/_pytest/mark/__init__.py', 'ParameterSet')`

**Response**: outcome `reexport`

```
module src/_pytest/mark/__init__.py lines=324 dynamic=no all=static@36
22 from ParameterSet <- .structures ParameterSet
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
    "ParameterSet"
   ],
   "desc": "check the top-level names of `src/_pytest/mark/__init__.py` for `ParameterSet`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/mark/__init__.py', 'ParameterSet')",
   "key": "[\"symbols\", [\"src/_pytest/mark/__init__.py\", \"ParameterSet\"]]",
   "v1": [
    2954667,
    995450
   ],
   "v2": [
    2954667,
    995450
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
     "ParameterSet"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/mark/__init__.py')",
   "key": "[\"symbols\", [\"src/_pytest/mark/__init__.py\"]]",
   "v1": [
    21678119,
    6968150
   ],
   "v2": [
    21678119,
    6968150
   ],
   "p_cap": [
    1,
    7
   ],
   "forecast": {
    "def": [
     3,
     350
    ],
    "reexport": [
     279,
     350
    ],
    "star": [
     3,
     350
    ],
    "none": [
     3,
     70
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
     "ParameterSet"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/_pytest/mark/__init__.py', 'ParameterSet')",
  "key": "[\"symbols\", [\"src/_pytest/mark/__init__.py\", \"ParameterSet\"]]",
  "provenance": "module `src/_pytest/mark/__init__.py` (task), name `ParameterSet` (task)",
  "v2": [
   2954667,
   995450
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
   "path": "src/_pytest/mark/__init__.py",
   "filter": "ParameterSet",
   "header": {
    "lines": 324,
    "dynamic": false,
    "all_status": "static",
    "all_line": 36
   },
   "bindings": [
    {
     "module": "src/_pytest/mark/__init__.py",
     "name": "ParameterSet",
     "line": 22,
     "kind": "from",
     "src": ".structures",
     "src_name": "ParameterSet",
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
    "src/_pytest/mark/__init__.py",
    "ParameterSet",
    "reexport",
    [
     ".structures",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 2

The package `src/_pytest/mark` does not define `ParameterSet` itself; line 22 imports it from `.structures`.

So far: `src/_pytest/mark/__init__.py` takes `ParameterSet` from `.structures`, which I still have to locate.

Let me outline `src/_pytest/mark/structures.py` directly, which both checks that the file exists and shows me `ParameterSet`; if `.structures` is a plain module that is where it has to be. Very likely it is defined right there. If the file does not exist, I will list `src/_pytest/mark/` to see what lives there; if the name is not bound there, that finishes it. I could list `src/_pytest/mark/` to see what lives there instead, but it tends to open more follow-up work.

**Call:** `symbols('src/_pytest/mark/structures.py', 'ParameterSet')`

**Response**: outcome `def`

```
module src/_pytest/mark/structures.py lines=696 dynamic=no all=none
83 class ParameterSet (NamedTuple)
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
   "desc": "find where `.structures` (imported by `src/_pytest/mark/__init__.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/mark/structures.py', 'ParameterSet')",
   "key": "[\"symbols\", [\"src/_pytest/mark/structures.py\", \"ParameterSet\"]]",
   "v1": [
    124552395191,
    97377019168
   ],
   "v2": [
    19340698905037,
    15093437971040
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     206829,
     251576
    ],
    "reexport": [
     469,
     31447
    ],
    "star": [
     469,
     251576
    ],
    "none": [
     5159,
     125788
    ],
    "missing": [
     64,
     533
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
    147709,
    71765
   ],
   "v2": [
    6168766169729,
    3018687594208
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
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+ParameterSet\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+ParameterSet\\\\b\", \".\"]]",
   "v1": [
    33966,
    16205
   ],
   "v2": [
    699567071019,
    340819567088
   ],
   "p_cap": [
    1,
    35
   ],
   "forecast": {
    "zero": [
     1,
     35
    ],
    "mid": [
     33,
     35
    ],
    "cap": [
     1,
     35
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
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+ParameterSet\\\\b', 'src')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+ParameterSet\\\\b\", \"src\"]]",
   "v1": [
    337433,
    116676
   ],
   "v2": [
    55060794984593,
    24539008830336
   ],
   "p_cap": [
    1,
    252
   ],
   "forecast": {
    "zero": [
     107,
     126
    ],
    "mid": [
     37,
     252
    ],
    "cap": [
     1,
     252
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
   "call": "symbols('src/_pytest/mark/structures/__init__.py', 'ParameterSet')",
   "key": "[\"symbols\", [\"src/_pytest/mark/structures/__init__.py\", \"ParameterSet\"]]",
   "v1": [
    2123991915,
    710970299
   ],
   "v2": [
    346741840706566563,
    149529521454863264
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     384,
     35711
    ],
    "reexport": [
     2816,
     35711
    ],
    "star": [
     64,
     35711
    ],
    "none": [
     1024,
     35711
    ],
    "missing": [
     469,
     533
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
  "call": "symbols('src/_pytest/mark/structures.py', 'ParameterSet')",
  "key": "[\"symbols\", [\"src/_pytest/mark/structures.py\", \"ParameterSet\"]]",
  "provenance": "`.structures` would be `src/_pytest/mark/structures.py` if that file exists; one call both checks and closes it",
  "v2": [
   19340698905037,
   15093437971040
  ]
 },
 "forecast": {
  "def": [
   206829,
   251576
  ],
  "reexport": [
   469,
   31447
  ],
  "star": [
   469,
   251576
  ],
  "none": [
   5159,
   125788
  ],
  "missing": [
   64,
   533
  ]
 },
 "plan": {
  "def": "done",
  "reexport": "continue",
  "star": "continue",
  "none": "done",
  "missing": "[\"ls\", [\"src/_pytest/mark\"]]"
 },
 "hedges": [
  {
   "outcome": "def",
   "word": "very likely",
   "p": [
    206829,
    251576
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
   "path": "src/_pytest/mark/structures.py",
   "filter": "ParameterSet",
   "header": {
    "lines": 696,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/_pytest/mark/structures.py",
     "name": "ParameterSet",
     "line": 83,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "NamedTuple"
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
    "src/_pytest/mark/__init__.py",
    "ParameterSet",
    "reexport",
    [
     ".structures",
     "src/_pytest/mark/structures.py"
    ]
   ],
   [
    "src/_pytest/mark/structures.py",
    "ParameterSet",
    "class",
    83
   ]
  ]
 }
}
```
</details>

## Step 3

There it is: `ParameterSet` is a class at `src/_pytest/mark/structures.py:83`. That settles the definition; now the imports of it.

I'll search the whole tree for imports of `ParameterSet` and star imports in one go; the search has to be complete before I can call the set final. Probably it fits under the cap. If nothing turns up, that finishes it; if it caps, I follow whatever it opens up.

**Call:** `grep('^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bParameterSet\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*ParameterSet\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$', '.')`

**Response**: outcome `mid`

```
src/_pytest/fixtures.py:68:from _pytest.mark import ParameterSet
src/_pytest/mark/__init__.py:22:from .structures import ParameterSet
src/_pytest/python.py:67:from _pytest.mark import ParameterSet
testing/acceptance_test.py:599:            from pytest import *
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
   "desc": "search `.` for imports of `ParameterSet`"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "."
   ],
   "desc": "search `.` for star imports"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bParameterSet\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*ParameterSet\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bParameterSet\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*ParameterSet\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
   "v1": [
    966509963729,
    566813142350
   ],
   "v2": [
    966509963729,
    566813142350
   ],
   "p_cap": [
    3,
    34
   ],
   "forecast": {
    "zero": [
     6,
     17
    ],
    "mid": [
     19,
     34
    ],
    "cap": [
     3,
     34
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
  },
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bParameterSet\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*ParameterSet\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bParameterSet\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*ParameterSet\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
   "v1": [
    88055542063897,
    16337555279500
   ],
   "v2": [
    49862073878297,
    16337555279500
   ],
   "p_cap": [
    1,
    20
   ],
   "forecast": {
    "zero": [
     7,
     10
    ],
    "mid": [
     1,
     4
    ],
    "cap": [
     1,
     20
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
    484067544634433,
    147037997515500
   ],
   "v2": [
    49862073878297,
    16337555279500
   ],
   "p_cap": [
    4,
    49
   ],
   "forecast": {
    "zero": [
     25,
     49
    ],
    "mid": [
     20,
     49
    ],
    "cap": [
     4,
     49
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
  "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bParameterSet\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*ParameterSet\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
  "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bParameterSet\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*ParameterSet\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
  "provenance": "import and star lines under `.` in one call",
  "v2": [
   966509963729,
   566813142350
  ]
 },
 "forecast": {
  "zero": [
   6,
   17
  ],
  "mid": [
   19,
   34
  ],
  "cap": [
   3,
   34
  ]
 },
 "plan": {
  "zero": "done",
  "mid": "continue",
  "cap": "continue"
 },
 "hedges": [
  {
   "outcome": "mid",
   "word": "probably",
   "p": [
    19,
    34
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
   "pattern": "^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bParameterSet\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*ParameterSet\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$",
   "scope": ".",
   "hits": [
    [
     "src/_pytest/fixtures.py",
     68
    ],
    [
     "src/_pytest/mark/__init__.py",
     22
    ],
    [
     "src/_pytest/python.py",
     67
    ],
    [
     "testing/acceptance_test.py",
     599
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/_pytest/fixtures.py",
   "src/_pytest/mark/__init__.py",
   "src/_pytest/python.py",
   "testing/acceptance_test.py"
  ],
  "table": [
   [
    "src/_pytest/fixtures.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/_pytest/mark/__init__.py",
    "src/_pytest/mark/__init__.py:22",
    "in",
    "`.structures` resolves `ParameterSet` to the target"
   ],
   [
    "src/_pytest/python.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "testing/acceptance_test.py",
    null,
    "pending",
    "not yet examined"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  },
  "n_in": 1,
  "n_out": 0,
  "n_pending": 3
 }
}
```
</details>

## Step 4

4 matching lines anywhere for imports of `ParameterSet` or star imports, in `src/_pytest/fixtures.py`, `src/_pytest/mark/__init__.py`, `src/_pytest/python.py`, `testing/acceptance_test.py`, and the search was under the cap, so that is the complete set there.

I'll look at `src/_pytest/fixtures.py`'s top-level names for `ParameterSet`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `src/_pytest/python.py`'s top-level names for `ParameterSet`.

**Call:** `symbols('src/_pytest/fixtures.py', 'ParameterSet')`

**Response**: outcome `ok`

```
module src/_pytest/fixtures.py lines=2600 dynamic=no all=none
68 from ParameterSet <- _pytest.mark ParameterSet
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/fixtures.py",
    "ParameterSet"
   ],
   "desc": "look at `src/_pytest/fixtures.py`'s imports of `ParameterSet`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "ParameterSet"
   ],
   "desc": "look at `src/_pytest/python.py`'s imports of `ParameterSet`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "ParameterSet"
   ],
   "desc": "look at `testing/acceptance_test.py`'s imports of `ParameterSet`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/fixtures.py', 'ParameterSet')",
   "key": "[\"symbols\", [\"src/_pytest/fixtures.py\", \"ParameterSet\"]]",
   "v1": [
    357781,
    78710
   ],
   "v2": [
    898388,
    196775
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
     "src/_pytest/fixtures.py",
     "ParameterSet"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/python.py', 'ParameterSet')",
   "key": "[\"symbols\", [\"src/_pytest/python.py\", \"ParameterSet\"]]",
   "v1": [
    357781,
    78710
   ],
   "v2": [
    898388,
    196775
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
     "src/_pytest/python.py",
     "ParameterSet"
    ]
   ]
  },
  {
   "call": "symbols('testing/acceptance_test.py', 'ParameterSet')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"ParameterSet\"]]",
   "v1": [
    357781,
    78710
   ],
   "v2": [
    898388,
    196775
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
     "testing/acceptance_test.py",
     "ParameterSet"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/_pytest/fixtures.py', 'ParameterSet')",
  "key": "[\"symbols\", [\"src/_pytest/fixtures.py\", \"ParameterSet\"]]",
  "provenance": "`src/_pytest/fixtures.py` had a matching line (step 3); its outline names every `ParameterSet` import exactly",
  "v2": [
   898388,
   196775
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
  "ok": "[\"symbols\", [\"src/_pytest/python.py\", \"ParameterSet\"]]",
  "cap": "[\"symbols\", [\"src/_pytest/python.py\", \"ParameterSet\"]]"
 },
 "hedges": [
  {
   "outcome": "ok",
   "word": "almost certainly",
   "p": [
    49,
    50
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
   "step": 4,
   "path": "src/_pytest/fixtures.py",
   "filter": "ParameterSet",
   "header": {
    "lines": 2600,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/_pytest/fixtures.py",
     "name": "ParameterSet",
     "line": 68,
     "kind": "from",
     "src": "_pytest.mark",
     "src_name": "ParameterSet",
     "conditional": false,
     "col": 0,
     "bases": []
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/_pytest/fixtures.py",
   "src/_pytest/mark/__init__.py",
   "src/_pytest/python.py",
   "testing/acceptance_test.py"
  ],
  "table": [
   [
    "src/_pytest/fixtures.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/_pytest/mark/__init__.py",
    "src/_pytest/mark/__init__.py:22",
    "in",
    "`.structures` resolves `ParameterSet` to the target"
   ],
   [
    "src/_pytest/python.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "testing/acceptance_test.py",
    null,
    "pending",
    "not yet examined"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  },
  "n_in": 1,
  "n_out": 0,
  "n_pending": 3
 }
}
```
</details>

## Step 5

`src/_pytest/fixtures.py`: line 68 imports it from `_pytest.mark`.

Tally: 1 import statements confirmed, 0 ruled out, 3 pending. The search itself is complete; what is left is checking the candidates.

Let me look at `src/_pytest/python.py`'s top-level names for `ParameterSet`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will list `./` to see what lives there.

**Call:** `symbols('src/_pytest/python.py', 'ParameterSet')`

**Response**: outcome `ok`

```
module src/_pytest/python.py lines=1843 dynamic=yes all=none
67 from ParameterSet <- _pytest.mark ParameterSet
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/_pytest/fixtures.py",
    "_pytest.mark"
   ],
   "desc": "find where `_pytest.mark` (imported by `src/_pytest/fixtures.py`) lives"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "ParameterSet"
   ],
   "desc": "look at `src/_pytest/python.py`'s imports of `ParameterSet`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "ParameterSet"
   ],
   "desc": "look at `testing/acceptance_test.py`'s imports of `ParameterSet`"
  }
 ],
 "candidates": [
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    5772493,
    1180650
   ],
   "v2": [
    2898053,
    590325
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
     "src/_pytest/fixtures.py",
     "_pytest.mark"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/python.py', 'ParameterSet')",
   "key": "[\"symbols\", [\"src/_pytest/python.py\", \"ParameterSet\"]]",
   "v1": [
    1997627,
    393550
   ],
   "v2": [
    2898053,
    590325
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
     "src/_pytest/python.py",
     "ParameterSet"
    ]
   ]
  },
  {
   "call": "symbols('testing/acceptance_test.py', 'ParameterSet')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"ParameterSet\"]]",
   "v1": [
    1997627,
    393550
   ],
   "v2": [
    2898053,
    590325
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
     "testing/acceptance_test.py",
     "ParameterSet"
    ]
   ]
  },
  {
   "call": "symbols('_pytest/mark.py', 'ParameterSet')",
   "key": "[\"symbols\", [\"_pytest/mark.py\", \"ParameterSet\"]]",
   "v1": [
    16141980137483159,
    3021122019687200
   ],
   "v2": [
    47518426695596789,
    9063366059061600
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     6116229,
     18365048
    ],
    "reexport": [
     13869,
     2295631
    ],
    "star": [
     13869,
     18365048
    ],
    "none": [
     152559,
     9182524
    ],
    "missing": [
     25040,
     38909
    ]
   },
   "serves": [
    [
     "module_path",
     "src/_pytest/fixtures.py",
     "_pytest.mark"
    ]
   ]
  },
  {
   "call": "symbols('_pytest/mark/__init__.py', 'ParameterSet')",
   "key": "[\"symbols\", [\"_pytest/mark/__init__.py\", \"ParameterSet\"]]",
   "v1": [
    931847353912759,
    154404974685325
   ],
   "v2": [
    5445090805136573,
    926429848111950
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     79488,
     18248321
    ],
    "reexport": [
     582912,
     18248321
    ],
    "star": [
     13248,
     18248321
    ],
    "none": [
     211968,
     18248321
    ],
    "missing": [
     259115,
     272363
    ]
   },
   "serves": [
    [
     "module_path",
     "src/_pytest/fixtures.py",
     "_pytest.mark"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+ParameterSet\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+ParameterSet\\\\b\", \".\"]]",
   "v1": [
    1191653,
    196775
   ],
   "v2": [
    6953143,
    1180650
   ],
   "p_cap": [
    1,
    35
   ],
   "forecast": {
    "zero": [
     1,
     35
    ],
    "mid": [
     33,
     35
    ],
    "cap": [
     1,
     35
    ]
   },
   "serves": [
    [
     "module_path",
     "src/_pytest/fixtures.py",
     "_pytest.mark"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+ParameterSet\\\\b', 'src')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+ParameterSet\\\\b\", \"src\"]]",
   "v1": [
    1191653,
    196775
   ],
   "v2": [
    6953143,
    1180650
   ],
   "p_cap": [
    1,
    252
   ],
   "forecast": {
    "zero": [
     107,
     126
    ],
    "mid": [
     37,
     252
    ],
    "cap": [
     1,
     252
    ]
   },
   "serves": [
    [
     "module_path",
     "src/_pytest/fixtures.py",
     "_pytest.mark"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/_pytest/python.py', 'ParameterSet')",
  "key": "[\"symbols\", [\"src/_pytest/python.py\", \"ParameterSet\"]]",
  "provenance": "`src/_pytest/python.py` had a matching line (step 3); its outline names every `ParameterSet` import exactly",
  "v2": [
   2898053,
   590325
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
  "ok": "[\"ls\", [\".\"]]",
  "cap": "[\"ls\", [\".\"]]"
 },
 "hedges": [
  {
   "outcome": "ok",
   "word": "almost certainly",
   "p": [
    49,
    50
   ]
  }
 ],
 "adherence": {
  "planned": "[\"symbols\", [\"src/_pytest/python.py\", \"ParameterSet\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 5,
   "path": "src/_pytest/python.py",
   "filter": "ParameterSet",
   "header": {
    "lines": 1843,
    "dynamic": true,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/_pytest/python.py",
     "name": "ParameterSet",
     "line": 67,
     "kind": "from",
     "src": "_pytest.mark",
     "src_name": "ParameterSet",
     "conditional": false,
     "col": 0,
     "bases": []
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/_pytest/fixtures.py",
   "src/_pytest/mark/__init__.py",
   "src/_pytest/python.py",
   "testing/acceptance_test.py"
  ],
  "table": [
   [
    "src/_pytest/fixtures.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/_pytest/mark/__init__.py",
    "src/_pytest/mark/__init__.py:22",
    "in",
    "`.structures` resolves `Paramete
```
</details>

## Step 6

`src/_pytest/python.py`: line 67 imports it from `_pytest.mark`. Careful: this module manipulates its namespace dynamically, so static resolution is not reliable here.

Tally: 1 import statements confirmed, 0 ruled out, 3 pending. The search itself is complete; what is left is checking the candidates.

Next I will list `./` to see what lives there; the listing settles whether the import is a module, a package, or not here at all. Very likely the listing fits. If the listing is too long, I will outline `_pytest/mark.py` directly, which both checks that the file exists and shows me `ParameterSet`. I could look at `testing/acceptance_test.py`'s top-level names for `ParameterSet` instead, but it settles less.

**Call:** `ls('.')`

**Response**: outcome `complete`

```
.github/
.pre-commit-config.yaml
.readthedocs.yaml
CHANGELOG.rst
CODE_OF_CONDUCT.md
CONTRIBUTING.rst
OPENCOLLECTIVE.rst
README.rst
RELEASING.rst
SECURITY.md
TIDELIFT.rst
bench/
changelog/
codecov.yml
doc/
extra/
pyproject.toml
scripts/
src/
testing/
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
    "src/_pytest/fixtures.py",
    "_pytest.mark"
   ],
   "desc": "find where `_pytest.mark` (imported by `src/_pytest/fixtures.py`) lives"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/_pytest/python.py",
    "_pytest.mark"
   ],
   "desc": "find where `_pytest.mark` (imported by `src/_pytest/python.py`) lives"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "ParameterSet"
   ],
   "desc": "look at `testing/acceptance_test.py`'s imports of `ParameterSet`"
  }
 ],
 "candidates": [
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    2510617,
    590325
   ],
   "v2": [
    56702244394667743,
    13595049088592400
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
     "src/_pytest/fixtures.py",
     "_pytest.mark"
    ],
    [
     "module_path",
     "src/_pytest/python.py",
     "_pytest.mark"
    ]
   ]
  },
  {
   "call": "symbols('testing/acceptance_test.py', 'ParameterSet')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"ParameterSet\"]]",
   "v1": [
    2206349,
    393550
   ],
   "v2": [
    5044847,
    1180650
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
     "testing/acceptance_test.py",
     "ParameterSet"
    ]
   ]
  },
  {
   "call": "symbols('_pytest/mark.py', 'ParameterSet')",
   "key": "[\"symbols\", [\"_pytest/mark.py\", \"ParameterSet\"]]",
   "v1": [
    15548647673883767,
    3021122019687200
   ],
   "v2": [
    38933547817086613,
    9063366059061600
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     6116229,
     18365048
    ],
    "reexport": [
     13869,
     2295631
    ],
    "star": [
     13869,
     18365048
    ],
    "none": [
     152559,
     9182524
    ],
    "missing": [
     25040,
     38909
    ]
   },
   "serves": [
    [
     "module_path",
     "src/_pytest/fixtures.py",
     "_pytest.mark"
    ],
    [
     "module_path",
     "src/_pytest/python.py",
     "_pytest.mark"
    ]
   ]
  },
  {
   "call": "symbols('_pytest/mark/__init__.py', 'ParameterSet')",
   "key": "[\"symbols\", [\"_pytest/mark/__init__.py\", \"ParameterSet\"]]",
   "v1": [
    142632045418006,
    22057853526475
   ],
   "v2": [
    344020758469814,
    66173560579425
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     79488,
     18248321
    ],
    "reexport": [
     582912,
     18248321
    ],
    "star": [
     13248,
     18248321
    ],
    "none": [
     211968,
     18248321
    ],
    "missing": [
     259115,
     272363
    ]
   },
   "serves": [
    [
     "module_path",
     "src/_pytest/fixtures.py",
     "_pytest.mark"
    ],
    [
     "module_path",
     "src/_pytest/python.py",
     "_pytest.mark"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+ParameterSet\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+ParameterSet\\\\b\", \".\"]]",
   "v1": [
    1296014,
    196775
   ],
   "v2": [
    3100942,
    590325
   ],
   "p_cap": [
    1,
    35
   ],
   "forecast": {
    "zero": [
     1,
     35
    ],
    "mid": [
     33,
     35
    ],
    "cap": [
     1,
     35
    ]
   },
   "serves": [
    [
     "module_path",
     "src/_pytest/fixtures.py",
     "_pytest.mark"
    ],
    [
     "module_path",
     "src/_pytest/python.py",
     "_pytest.mark"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+ParameterSet\\\\b', 'src')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+ParameterSet\\\\b\", \"src\"]]",
   "v1": [
    1296014,
    196775
   ],
   "v2": [
    3100942,
    590325
   ],
   "p_cap": [
    1,
    252
   ],
   "forecast": {
    "zero": [
     107,
     126
    ],
    "mid": [
     37,
     252
    ],
    "cap": [
     1,
     252
    ]
   },
   "serves": [
    [
     "module_path",
     "src/_pytest/fixtures.py",
     "_pytest.mark"
    ],
    [
     "module_path",
     "src/_pytest/python.py",
     "_pytest.mark"
    ]
   ]
  }
 ],
 "choice": {
  "call": "ls('.')",
  "key": "[\"ls\", [\".\"]]",
  "provenance": "`_pytest.mark` imported by `src/_pytest/fixtures.py` should live under `.`",
  "v2": [
   56702244394667743,
   13595049088592400
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
  "complete": "[\"symbols\", [\"testing/acceptance_test.py\", \"ParameterSet\"]]",
  "cap": "[\"symbols\", [\"_pytest/mark.py\", \"ParameterSet\"]]"
 },
 "hedges": [
  {
   "outcome": "complete",
   "word": "very likely",
   "p": [
    7,
    9
   ]
  }
 ],
 "adherence": {
  "planned": "[\"ls\", [\".\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "listing",
   "step": 6,
   "dir": ".",
   "entries": [
    ".github/",
    ".pre-commit-config.yaml",
    ".readthedocs.yaml",
    "CHANGELOG.rst",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.rst",
    "OPENCOLLECTIVE.rst",
    "README.rst",
    "RELEASING.rst",
    "SECURITY.md",
    "TIDELIFT.rst",
    "bench/",
    "changelog/",
    "codecov.yml",
    "doc/",
    "extra/",
    "pyproject.toml",
    "scripts/",
    "src/",
    "testing/",
    "tox.ini"
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/_pytest/fixtures.py",
   "src/_pytest/mark/__init__.py",
   "src/_pytest/python.py",
   "testing/acceptance_test.py"
  ],
  "table": [
   [
    "src/_pytest/fixtures.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/_pytest/mark/__init__.py",
    "src/_pytest/mark/__init__.py:22",
    "in",
    "`.structures` resolves `ParameterSet` to the target"
   ],
   [
    "src/_pyt
```
</details>

## Step 7

`./` has 21 entries: there is no `_pytest` here. That changes the plan.

Next I will outline `src/_pytest/mark.py` directly, which both checks that the file exists and shows me `ParameterSet`; if `_pytest.mark` is a plain module that is where it has to be. Very likely it is defined right there. If the file does not exist, I will list `src/_pytest/` to see what lives there; if the name is not bound there, I will look at `testing/acceptance_test.py`'s top-level names for `ParameterSet`. I could look at `testing/acceptance_test.py`'s top-level names for `ParameterSet` instead, but it settles less.

**Call:** `symbols('src/_pytest/mark.py', 'ParameterSet')`

**Response**: outcome `missing`

```
error: not a python file: src/_pytest/mark.py
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/_pytest/fixtures.py",
    "_pytest.mark"
   ],
   "desc": "find where `_pytest.mark` (imported by `src/_pytest/fixtures.py`) lives"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/_pytest/python.py",
    "_pytest.mark"
   ],
   "desc": "find where `_pytest.mark` (imported by `src/_pytest/python.py`) lives"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "ParameterSet"
   ],
   "desc": "look at `testing/acceptance_test.py`'s imports of `ParameterSet`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/mark.py', 'ParameterSet')",
   "key": "[\"symbols\", [\"src/_pytest/mark.py\", \"ParameterSet\"]]",
   "v1": [
    125497074890479,
    41385233146400
   ],
   "v2": [
    3764901031618913,
    1282942227538400
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     206829,
     251576
    ],
    "reexport": [
     469,
     31447
    ],
    "star": [
     469,
     251576
    ],
    "none": [
     5159,
     125788
    ],
    "missing": [
     64,
     533
    ]
   },
   "serves": [
    [
     "module_path",
     "src/_pytest/fixtures.py",
     "_pytest.mark"
    ],
    [
     "module_path",
     "src/_pytest/python.py",
     "_pytest.mark"
    ]
   ]
  },
  {
   "call": "symbols('testing/acceptance_test.py', 'ParameterSet')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"ParameterSet\"]]",
   "v1": [
    2206349,
    393550
   ],
   "v2": [
    126324779553407,
    41385233146400
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
     "testing/acceptance_test.py",
     "ParameterSet"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+ParameterSet\\\\b', 'src')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+ParameterSet\\\\b\", \"src\"]]",
   "v1": [
    156017089,
    24793650
   ],
   "v2": [
    42933069478379369,
    10429078752892800
   ],
   "p_cap": [
    1,
    252
   ],
   "forecast": {
    "zero": [
     107,
     126
    ],
    "mid": [
     37,
     252
    ],
    "cap": [
     1,
     252
    ]
   },
   "serves": [
    [
     "module_path",
     "src/_pytest/fixtures.py",
     "_pytest.mark"
    ],
    [
     "module_path",
     "src/_pytest/python.py",
     "_pytest.mark"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+ParameterSet\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+ParameterSet\\\\b\", \".\"]]",
   "v1": [
    6474668,
    1377425
   ],
   "v2": [
    3312305514318807,
    724241580062000
   ],
   "p_cap": [
    1,
    35
   ],
   "forecast": {
    "zero": [
     1,
     35
    ],
    "mid": [
     33,
     35
    ],
    "cap": [
     1,
     35
    ]
   },
   "serves": [
    [
     "module_path",
     "src/_pytest/fixtures.py",
     "_pytest.mark"
    ],
    [
     "module_path",
     "src/_pytest/python.py",
     "_pytest.mark"
    ]
   ]
  },
  {
   "call": "ls('src/_pytest')",
   "key": "[\"ls\", [\"src/_pytest\"]]",
   "v1": [
    28212514,
    6100025
   ],
   "v2": [
    29476666763798701,
    6414711137692000
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
     "src/_pytest/fixtures.py",
     "_pytest.mark"
    ],
    [
     "module_path",
     "src/_pytest/python.py",
     "_pytest.mark"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/_pytest/mark.py', 'ParameterSet')",
  "key": "[\"symbols\", [\"src/_pytest/mark.py\", \"ParameterSet\"]]",
  "provenance": "`_pytest.mark` would be `src/_pytest/mark.py` if that file exists; one call both checks and closes it",
  "v2": [
   3764901031618913,
   1282942227538400
  ]
 },
 "forecast": {
  "def": [
   206829,
   251576
  ],
  "reexport": [
   469,
   31447
  ],
  "star": [
   469,
   251576
  ],
  "none": [
   5159,
   125788
  ],
  "missing": [
   64,
   533
  ]
 },
 "plan": {
  "def": "[\"symbols\", [\"testing/acceptance_test.py\", \"ParameterSet\"]]",
  "reexport": "[\"symbols\", [\"testing/acceptance_test.py\", \"ParameterSet\"]]",
  "star": "[\"symbols\", [\"testing/acceptance_test.py\", \"ParameterSet\"]]",
  "none": "[\"symbols\", [\"testing/acceptance_test.py\", \"ParameterSet\"]]",
  "missing": "[\"ls\", [\"src/_pytest\"]]"
 },
 "hedges": [
  {
   "outcome": "def",
   "word": "very likely",
   "p": [
    206829,
    251576
   ]
  }
 ],
 "adherence": {
  "planned": "[\"symbols\", [\"testing/acceptance_test.py\", \"ParameterSet\"]]",
  "status": "deviated"
 },
 "facts": [
  {
   "kind": "error",
   "step": 7,
   "call": "[\"symbols\", [\"src/_pytest/mark.py\", \"ParameterSet\"]]",
   "error": "not a python file: src/_pytest/mark.py",
   "missing": "src/_pytest/mark.py"
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/_pytest/fixtures.py",
   "src/_pytest/mark/__init__.py",
   "src/_pytest/python.py",
   "testing/acceptance_test.py"
  ],
  "table": [
   [
    "src/_pytest/fixtures.py",
    "src/_pytest/fixtures.py:68",
    "in",
    "`_pytest.mark` resolves `ParameterSet` to the target"
   ],
   [
    "src/_pytest/mark/__init__.py",
    "src/_pytest/mark/__init__.py:22",
    "in",
    "`.structures` resolves `ParameterSet` to the target"
   ],
   [
    "src/_pytest/python.py",
    "src/_pytest/python.py:67",
    "in",
    "`_pytest.mark` resolves `ParameterSet` to the target"
   ],
   [
    "testing/acceptance_test.py",
    null,
    "pending",
    "not yet examined"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  },
  "n_in": 3,
  "n_out": 0,
  "n_pending": 1
 }
}
```
</details>

## Step 8

There is no `src/_pytest/mark.py`, so `mark` is either a package (`src/_pytest/mark/__init__.py`) or not in this repository at all.

I'll look at `testing/acceptance_test.py`'s top-level names for `ParameterSet`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I follow whatever it opens up.

**Call:** `symbols('testing/acceptance_test.py', 'ParameterSet')`

**Response**: outcome `ok`

```
module testing/acceptance_test.py lines=1770 dynamic=no all=none
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "ParameterSet"
   ],
   "desc": "look at `testing/acceptance_test.py`'s imports of `ParameterSet`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('testing/acceptance_test.py', 'ParameterSet')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"ParameterSet\"]]",
   "v1": [
    601549,
    393550
   ],
   "v2": [
    601549,
    393550
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
     "testing/acceptance_test.py",
     "ParameterSet"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('testing/acceptance_test.py', 'ParameterSet')",
  "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"ParameterSet\"]]",
  "provenance": "`testing/acceptance_test.py` had a matching line (step 3); its outline names every `ParameterSet` import exactly",
  "v2": [
   601549,
   393550
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
 "hedges": [
  {
   "outcome": "ok",
   "word": "almost certainly",
   "p": [
    49,
    50
   ]
  }
 ],
 "adherence": {
  "planned": "[\"ls\", [\"src/_pytest\"]]",
  "status": "replanned"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 8,
   "path": "testing/acceptance_test.py",
   "filter": "ParameterSet",
   "header": {
    "lines": 1770,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/_pytest/fixtures.py",
   "src/_pytest/mark/__init__.py",
   "src/_pytest/python.py",
   "testing/acceptance_test.py"
  ],
  "table": [
   [
    "src/_pytest/fixtures.py",
    "src/_pytest/fixtures.py:68",
    "in",
    "`_pytest.mark` resolves `ParameterSet` to the target"
   ],
   [
    "src/_pytest/mark/__init__.py",
    "src/_pytest/mark/__init__.py:22",
    "in",
    "`.structures` resolves `ParameterSet` to the target"
   ],
   [
    "src/_pytest/python.py",
    "src/_pytest/python.py:67",
    "in",
    "`_pytest.mark` resolves `ParameterSet` to the target"
   ],
   [
    "testing/acceptance_test.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  },
  "n_in": 3,
  "n_out": 0,
  "n_pending": 0
 }
}
```
</details>

## Final

`ParameterSet` is the class at `src/_pytest/mark/structures.py:83`. 3 module-level import statements bring in this definition: `src/_pytest/fixtures.py:68`, `src/_pytest/mark/__init__.py:22`, `src/_pytest/python.py:67`. Looking back, all 8 calls were needed.

**Answer:** `{"final_kind": "importers", "final": ["src/_pytest/fixtures.py:68", "src/_pytest/mark/__init__.py:22", "src/_pytest/python.py:67"], "steps": [{"op": "resolve", "output": {"kind": "def", "path": "src/_pytest/mark/structures.py", "line": 83, "name": "ParameterSet", "detail": "class"}}, {"op": "importers", "output": ["src/_pytest/fixtures.py:68", "src/_pytest/mark/__init__.py:22", "src/_pytest/python.py:67"]}], "stuck": null}`  
**Stopped:** certificate after 8 calls