# requests-importers-8ad279df

**Repository:** requests  
**Chain:** resolve → importers  
**Seed:** 0, prior 736169d01b033d9f, floor 12

## Task

In `src/requests/_types.py` line 67, `CaseInsensitiveDict` is imported from `.structures`. Which definition does the module-level name `CaseInsensitiveDict` actually refer to? Give `path:line`. Then list every module-level import statement in the repository that brings in that definition, including through re-exports and star imports, as `path:line`.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N; bindings take effect in source order. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. A class derives from a definition when a base written as a bare name or `module.Name` resolves to it. A call site is `name(...)` where the bare name refers to the module-level binding (not a parameter or local). Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

I need to find what `CaseInsensitiveDict` really is in `src/requests/_types.py`: line 67 imports it from `.structures`, so the definition is at least one hop away. Then I have to find every module-level import of that definition, which means a complete search, not a sample.

Next I will check `src/requests/_types.py` for any other binding of `CaseInsensitiveDict` besides the import on line 67; almost certainly the import is the only one, and then `.structures` is the place to follow.

**Call:** `symbols('src/requests/_types.py', 'CaseInsensitiveDict')`

**Response**: outcome `reexport`

```
module src/requests/_types.py lines=189 dynamic=no all=none
67 from CaseInsensitiveDict <- .structures CaseInsensitiveDict
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/requests/_types.py",
    "CaseInsensitiveDict"
   ],
   "desc": "check the top-level names of `src/requests/_types.py` for `CaseInsensitiveDict`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/requests/_types.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"src/requests/_types.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    68387133,
    23571100
   ],
   "v2": [
    68387133,
    23571100
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
     "src/requests/_types.py",
     "CaseInsensitiveDict"
    ]
   ]
  },
  {
   "call": "symbols('src/requests/_types.py')",
   "key": "[\"symbols\", [\"src/requests/_types.py\"]]",
   "v1": [
    6295028129,
    2074256800
   ],
   "v2": [
    6295028129,
    2074256800
   ],
   "p_cap": [
    47,
    352
   ],
   "forecast": {
    "def": [
     61,
     7040
    ],
    "reexport": [
     5673,
     7040
    ],
    "star": [
     61,
     7040
    ],
    "none": [
     61,
     1408
    ],
    "cap": [
     47,
     352
    ]
   },
   "serves": [
    [
     "bindings",
     "src/requests/_types.py",
     "CaseInsensitiveDict"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/requests/_types.py', 'CaseInsensitiveDict')",
  "key": "[\"symbols\", [\"src/requests/_types.py\", \"CaseInsensitiveDict\"]]",
  "provenance": "module `src/requests/_types.py` (task), name `CaseInsensitiveDict` (task)",
  "v2": [
   68387133,
   23571100
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
   "path": "src/requests/_types.py",
   "filter": "CaseInsensitiveDict",
   "header": {
    "lines": 189,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/requests/_types.py",
     "name": "CaseInsensitiveDict",
     "line": 67,
     "kind": "from",
     "src": ".structures",
     "src_name": "CaseInsensitiveDict",
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
    "src/requests/_types.py",
    "CaseInsensitiveDict",
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

`src/requests/_types.py` does not define `CaseInsensitiveDict` itself; line 67 imports it from `.structures`.

So far: `src/requests/_types.py` takes `CaseInsensitiveDict` from `.structures`, which I still have to locate.

Let me outline `src/requests/structures.py` directly, which both checks that the file exists and shows me `CaseInsensitiveDict`; if `.structures` is a plain module that is where it has to be. Very likely it is defined right there. If the file does not exist, I will list `src/requests/` to see what lives there; if the name is not bound there, that finishes it. I could list `src/requests/` to see what lives there instead, but it tends to open more follow-up work.

**Call:** `symbols('src/requests/structures.py', 'CaseInsensitiveDict')`

**Response**: outcome `def`

```
module src/requests/structures.py lines=131 dynamic=no all=none
20 class CaseInsensitiveDict (?,?)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/requests/_types.py",
    ".structures"
   ],
   "desc": "find where `.structures` (imported by `src/requests/_types.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/requests/structures.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"src/requests/structures.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    10215370598,
    7881805437
   ],
   "v2": [
    430123808249,
    331035828354
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     191744,
     234069
    ],
    "reexport": [
     1792,
     234069
    ],
    "star": [
     448,
     234069
    ],
    "none": [
     2688,
     78023
    ],
    "missing": [
     71,
     519
    ]
   },
   "serves": [
    [
     "module_path",
     "src/requests/_types.py",
     ".structures"
    ]
   ]
  },
  {
   "call": "ls('src/requests')",
   "key": "[\"ls\", [\"src/requests\"]]",
   "v1": [
    19165,
    9366
   ],
   "v2": [
    47975059126,
    23645416311
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
     "src/requests/_types.py",
     ".structures"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+CaseInsensitiveDict\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+CaseInsensitiveDict\\\\b\", \".\"]]",
   "v1": [
    16231,
    7805
   ],
   "v2": [
    80317905721,
    39409027185
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
     "src/requests/_types.py",
     ".structures"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+CaseInsensitiveDict\\\\b', 'src')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+CaseInsensitiveDict\\\\b\", \"src\"]]",
   "v1": [
    77991,
    27206
   ],
   "v2": [
    1083437729008,
    480790131657
   ],
   "p_cap": [
    1,
    244
   ],
   "forecast": {
    "zero": [
     205,
     244
    ],
    "mid": [
     19,
     122
    ],
    "cap": [
     1,
     244
    ]
   },
   "serves": [
    [
     "module_path",
     "src/requests/_types.py",
     ".structures"
    ]
   ]
  },
  {
   "call": "symbols('src/requests/structures/__init__.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"src/requests/structures/__init__.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    720848747,
    244089333
   ],
   "v2": [
    2229872500297369,
    958577295442503
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     213,
     12802
    ],
    "reexport": [
     1065,
     12802
    ],
    "star": [
     71,
     38406
    ],
    "none": [
     1349,
     38406
    ],
    "missing": [
     448,
     519
    ]
   },
   "serves": [
    [
     "module_path",
     "src/requests/_types.py",
     ".structures"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/requests/structures.py', 'CaseInsensitiveDict')",
  "key": "[\"symbols\", [\"src/requests/structures.py\", \"CaseInsensitiveDict\"]]",
  "provenance": "`.structures` would be `src/requests/structures.py` if that file exists; one call both checks and closes it",
  "v2": [
   430123808249,
   331035828354
  ]
 },
 "forecast": {
  "def": [
   191744,
   234069
  ],
  "reexport": [
   1792,
   234069
  ],
  "star": [
   448,
   234069
  ],
  "none": [
   2688,
   78023
  ],
  "missing": [
   71,
   519
  ]
 },
 "plan": {
  "def": "done",
  "reexport": "continue",
  "star": "continue",
  "none": "done",
  "missing": "[\"ls\", [\"src/requests\"]]"
 },
 "hedges": [
  {
   "outcome": "def",
   "word": "very likely",
   "p": [
    191744,
    234069
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
   "path": "src/requests/structures.py",
   "filter": "CaseInsensitiveDict",
   "header": {
    "lines": 131,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/requests/structures.py",
     "name": "CaseInsensitiveDict",
     "line": 20,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "?",
      "?"
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
    "src/requests/_types.py",
    "CaseInsensitiveDict",
    "reexport",
    [
     ".structures",
     "src/requests/structures.py"
    ]
   ],
   [
    "src/requests/structures.py",
    "CaseInsensitiveDict",
    "class",
    20
   ]
  ]
 }
}
```
</details>

## Step 3

There it is: `CaseInsensitiveDict` is a class at `src/requests/structures.py:20`. That settles the definition; now the imports of it.

I'll search the whole tree for imports of `CaseInsensitiveDict` and star imports in one go; the search has to be complete before I can call the set final. Probably it fits under the cap. If nothing turns up, that finishes it; if it caps, I follow whatever it opens up.

**Call:** `grep('^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bCaseInsensitiveDict\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*CaseInsensitiveDict\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$', '.')`

**Response**: outcome `mid`

```
src/requests/_types.py:67:    from .structures import CaseInsensitiveDict
src/requests/adapters.py:52:from .structures import CaseInsensitiveDict
src/requests/models.py:71:from .structures import CaseInsensitiveDict
src/requests/sessions.py:47:from .structures import CaseInsensitiveDict
src/requests/utils.py:69:from .structures import CaseInsensitiveDict
tests/test_requests.py:55:from requests.structures import CaseInsensitiveDict
tests/test_structures.py:3:from requests.structures import CaseInsensitiveDict, LookupDict
tests/test_utils.py:15:from requests.structures import CaseInsensitiveDict
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
   "desc": "search `.` for imports of `CaseInsensitiveDict`"
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
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bCaseInsensitiveDict\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*CaseInsensitiveDict\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bCaseInsensitiveDict\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*CaseInsensitiveDict\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
   "v1": [
    1973947505,
    1170030602
   ],
   "v2": [
    1973947505,
    1170030602
   ],
   "p_cap": [
    3,
    38
   ],
   "forecast": {
    "zero": [
     13,
     38
    ],
    "mid": [
     11,
     19
    ],
    "cap": [
     3,
     38
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
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bCaseInsensitiveDict\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*CaseInsensitiveDict\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bCaseInsensitiveDict\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*CaseInsensitiveDict\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
   "v1": [
    314647331571,
    44184050365
   ],
   "v2": [
    9247860091,
    3150082390
   ],
   "p_cap": [
    1,
    35
   ],
   "forecast": {
    "zero": [
     24,
     35
    ],
    "mid": [
     2,
     7
    ],
    "cap": [
     1,
     35
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
    198327408362,
    56808064755
   ],
   "v2": [
    136871087211,
    44184050365
   ],
   "p_cap": [
    4,
    41
   ],
   "forecast": {
    "zero": [
     15,
     41
    ],
    "mid": [
     22,
     41
    ],
    "cap": [
     4,
     41
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
  "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bCaseInsensitiveDict\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*CaseInsensitiveDict\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
  "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bCaseInsensitiveDict\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*CaseInsensitiveDict\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
  "provenance": "import and star lines under `.` in one call",
  "v2": [
   1973947505,
   1170030602
  ]
 },
 "forecast": {
  "zero": [
   13,
   38
  ],
  "mid": [
   11,
   19
  ],
  "cap": [
   3,
   38
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
    11,
    19
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
   "pattern": "^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bCaseInsensitiveDict\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*CaseInsensitiveDict\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$",
   "scope": ".",
   "hits": [
    [
     "src/requests/_types.py",
     67
    ],
    [
     "src/requests/adapters.py",
     52
    ],
    [
     "src/requests/models.py",
     71
    ],
    [
     "src/requests/sessions.py",
     47
    ],
    [
     "src/requests/utils.py",
     69
    ],
    [
     "tests/test_requests.py",
     55
    ],
    [
     "tests/test_structures.py",
     3
    ],
    [
     "tests/test_utils.py",
     15
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
   "src/requests/_types.py",
   "src/requests/adapters.py",
   "src/requests/models.py",
   "src/requests/sessions.py",
   "src/requests/utils.py",
   "tests/test_requests.py",
   "tests/test_structures.py",
   "tests/test_utils.py"
  ],
  "table": [
   [
    "src/requests/_types.py",
    "src/requests/_types.py:67",
    "in",
    "`.structures` resolves `CaseInsensitiveDict` to the target"
   ],
   [
    "src/requests/adapters.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/requests/models.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/requests/sessions.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/requests/utils.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_requests.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_structures.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_utils.py",
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
  "n_pending": 7
 }
}
```
</details>

## Step 4

8 matching lines anywhere for imports of `CaseInsensitiveDict` or star imports, in `src/requests/_types.py`, `src/requests/adapters.py`, `src/requests/models.py`, `src/requests/sessions.py` and 4 more files, and the search was under the cap, so that is the complete set there.

Still open: look at `src/requests/adapters.py`'s imports of `CaseInsensitiveDict`; look at `src/requests/models.py`'s imports of `CaseInsensitiveDict`; look at `src/requests/sessions.py`'s imports of `CaseInsensitiveDict`; and 4 more.

I'll look at `src/requests/adapters.py`'s top-level names for `CaseInsensitiveDict`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `src/requests/models.py`'s top-level names for `CaseInsensitiveDict`.

**Call:** `symbols('src/requests/adapters.py', 'CaseInsensitiveDict')`

**Response**: outcome `ok`

```
module src/requests/adapters.py lines=749 dynamic=no all=none
52 from CaseInsensitiveDict <- .structures CaseInsensitiveDict
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/requests/adapters.py",
    "CaseInsensitiveDict"
   ],
   "desc": "look at `src/requests/adapters.py`'s imports of `CaseInsensitiveDict`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/requests/models.py",
    "CaseInsensitiveDict"
   ],
   "desc": "look at `src/requests/models.py`'s imports of `CaseInsensitiveDict`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/requests/sessions.py",
    "CaseInsensitiveDict"
   ],
   "desc": "look at `src/requests/sessions.py`'s imports of `CaseInsensitiveDict`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/requests/utils.py",
    "CaseInsensitiveDict"
   ],
   "desc": "look at `src/requests/utils.py`'s imports of `CaseInsensitiveDict`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_requests.py",
    "CaseInsensitiveDict"
   ],
   "desc": "look at `tests/test_requests.py`'s imports of `CaseInsensitiveDict`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_structures.py",
    "CaseInsensitiveDict"
   ],
   "desc": "look at `tests/test_structures.py`'s imports of `CaseInsensitiveDict`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_utils.py",
    "CaseInsensitiveDict"
   ],
   "desc": "look at `tests/test_utils.py`'s imports of `CaseInsensitiveDict`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/requests/adapters.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"src/requests/adapters.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    2906207,
    239725
   ],
   "v2": [
    5822003,
    479450
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
     "src/requests/adapters.py",
     "CaseInsensitiveDict"
    ]
   ]
  },
  {
   "call": "symbols('src/requests/models.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"src/requests/models.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    2906207,
    239725
   ],
   "v2": [
    5822003,
    479450
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
     "src/requests/models.py",
     "CaseInsensitiveDict"
    ]
   ]
  },
  {
   "call": "symbols('src/requests/sessions.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"src/requests/sessions.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    2906207,
    239725
   ],
   "v2": [
    5822003,
    479450
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
     "src/requests/sessions.py",
     "CaseInsensitiveDict"
    ]
   ]
  },
  {
   "call": "symbols('src/requests/utils.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"src/requests/utils.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    2906207,
    239725
   ],
   "v2": [
    5822003,
    479450
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
     "src/requests/utils.py",
     "CaseInsensitiveDict"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_requests.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"tests/test_requests.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    2906207,
    239725
   ],
   "v2": [
    5822003,
    479450
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
     "tests/test_requests.py",
     "CaseInsensitiveDict"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_structures.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"tests/test_structures.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    2906207,
    239725
   ],
   "v2": [
    5822003,
    479450
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
     "tests/test_structures.py",
     "CaseInsensitiveDict"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_utils.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"tests/test_utils.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    2906207,
    239725
   ],
   "v2": [
    5822003,
    479450
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
     "tests/test_utils.py",
     "CaseInsensitiveDict"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/requests/adapters.py', 'CaseInsensitiveDict')",
  "key": "[\"symbols\", [\"src/requests/adapters.py\", \"CaseInsensitiveDict\"]]",
  "provenance": "`src/requests/adapters.py` had a matching line (step 3); its outline names every `CaseInsensitiveDict` import exactly",
  "v2": [
   5822003,
   479450
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
  "ok": "[\"symbols\", [\"src/requests/models.py\", \"CaseInsensitiveDict\"]]",
  "cap": "[\"symbols\", [\"src/requests/models.py\", \"CaseInsensitiveDict\"]]"
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
   "path": "src/requests/adapters.py",
   "filter": "CaseInsensitiveDict",
   "header": {
    "lines": 749,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/requests/adapters.py",
     "name": "CaseInsensitiveDict",
     "line": 52,
     "kind": "from",
     "src": ".structures",
     "src_name": "CaseInsens
```
</details>

## Step 5

`src/requests/adapters.py`: line 52 imports it from `.structures`.

Tally: 2 import statements confirmed, 0 ruled out, 6 pending. The search itself is complete; what is left is checking the candidates.

Let me look at `src/requests/models.py`'s top-level names for `CaseInsensitiveDict`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `src/requests/sessions.py`'s top-level names for `CaseInsensitiveDict`.

**Call:** `symbols('src/requests/models.py', 'CaseInsensitiveDict')`

**Response**: outcome `ok`

```
module src/requests/models.py lines=1185 dynamic=no all=none
71 from CaseInsensitiveDict <- .structures CaseInsensitiveDict
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/requests/models.py",
    "CaseInsensitiveDict"
   ],
   "desc": "look at `src/requests/models.py`'s imports of `CaseInsensitiveDict`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/requests/sessions.py",
    "CaseInsensitiveDict"
   ],
   "desc": "look at `src/requests/sessions.py`'s imports of `CaseInsensitiveDict`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/requests/utils.py",
    "CaseInsensitiveDict"
   ],
   "desc": "look at `src/requests/utils.py`'s imports of `CaseInsensitiveDict`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_requests.py",
    "CaseInsensitiveDict"
   ],
   "desc": "look at `tests/test_requests.py`'s imports of `CaseInsensitiveDict`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_structures.py",
    "CaseInsensitiveDict"
   ],
   "desc": "look at `tests/test_structures.py`'s imports of `CaseInsensitiveDict`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_utils.py",
    "CaseInsensitiveDict"
   ],
   "desc": "look at `tests/test_utils.py`'s imports of `CaseInsensitiveDict`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/requests/models.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"src/requests/models.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    4983439,
    479450
   ],
   "v2": [
    2496514,
    239725
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
     "src/requests/models.py",
     "CaseInsensitiveDict"
    ]
   ]
  },
  {
   "call": "symbols('src/requests/sessions.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"src/requests/sessions.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    4983439,
    479450
   ],
   "v2": [
    2496514,
    239725
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
     "src/requests/sessions.py",
     "CaseInsensitiveDict"
    ]
   ]
  },
  {
   "call": "symbols('src/requests/utils.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"src/requests/utils.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    4983439,
    479450
   ],
   "v2": [
    2496514,
    239725
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
     "src/requests/utils.py",
     "CaseInsensitiveDict"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_requests.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"tests/test_requests.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    4983439,
    479450
   ],
   "v2": [
    2496514,
    239725
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
     "tests/test_requests.py",
     "CaseInsensitiveDict"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_structures.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"tests/test_structures.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    4983439,
    479450
   ],
   "v2": [
    2496514,
    239725
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
     "tests/test_structures.py",
     "CaseInsensitiveDict"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_utils.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"tests/test_utils.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    4983439,
    479450
   ],
   "v2": [
    2496514,
    239725
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
     "tests/test_utils.py",
     "CaseInsensitiveDict"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/requests/models.py', 'CaseInsensitiveDict')",
  "key": "[\"symbols\", [\"src/requests/models.py\", \"CaseInsensitiveDict\"]]",
  "provenance": "`src/requests/models.py` had a matching line (step 3); its outline names every `CaseInsensitiveDict` import exactly",
  "v2": [
   2496514,
   239725
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
  "ok": "[\"symbols\", [\"src/requests/sessions.py\", \"CaseInsensitiveDict\"]]",
  "cap": "[\"symbols\", [\"src/requests/sessions.py\", \"CaseInsensitiveDict\"]]"
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
  "planned": "[\"symbols\", [\"src/requests/models.py\", \"CaseInsensitiveDict\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 5,
   "path": "src/requests/models.py",
   "filter": "CaseInsensitiveDict",
   "header": {
    "lines": 1185,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/requests/models.py",
     "name": "CaseInsensitiveDict",
     "line": 71,
     "kind": "from",
     "src": ".structures",
     "src_name": "CaseInsensitiveDict",
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
   "src/requests/_types.py",
   "src/requests/adapters.py",
   "src/requests/models.py",
   "src/requests/sessions.py",
   "src/requests/utils.py",
   "tests/test_requests.py",
   "tests/test_structures.py",
   "tests/test_utils.py"
  ],
  "table": [
   [
    "src/requests/_types.py",
    "src/requests/_types.py:67",
    "in",
    "`.structures` resolves `CaseInsensitiveDict` to the target"
   ],
   [
    "src/requests/adapters.py",
    "
```
</details>

## Step 6

`src/requests/models.py`: line 71 imports it from `.structures`.

Tally: 3 import statements confirmed, 0 ruled out, 5 pending. The search itself is complete; what is left is checking the candidates.

Next I will look at `src/requests/sessions.py`'s top-level names for `CaseInsensitiveDict`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `src/requests/utils.py`'s top-level names for `CaseInsensitiveDict`.

**Call:** `symbols('src/requests/sessions.py', 'CaseInsensitiveDict')`

**Response**: outcome `ok`

```
module src/requests/sessions.py lines=921 dynamic=no all=none
47 from CaseInsensitiveDict <- .structures CaseInsensitiveDict
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/requests/sessions.py",
    "CaseInsensitiveDict"
   ],
   "desc": "look at `src/requests/sessions.py`'s imports of `CaseInsensitiveDict`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/requests/utils.py",
    "CaseInsensitiveDict"
   ],
   "desc": "look at `src/requests/utils.py`'s imports of `CaseInsensitiveDict`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_requests.py",
    "CaseInsensitiveDict"
   ],
   "desc": "look at `tests/test_requests.py`'s imports of `CaseInsensitiveDict`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_structures.py",
    "CaseInsensitiveDict"
   ],
   "desc": "look at `tests/test_structures.py`'s imports of `CaseInsensitiveDict`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_utils.py",
    "CaseInsensitiveDict"
   ],
   "desc": "look at `tests/test_utils.py`'s imports of `CaseInsensitiveDict`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/requests/sessions.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"src/requests/sessions.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    2077232,
    239725
   ],
   "v2": [
    4164053,
    479450
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
     "src/requests/sessions.py",
     "CaseInsensitiveDict"
    ]
   ]
  },
  {
   "call": "symbols('src/requests/utils.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"src/requests/utils.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    2077232,
    239725
   ],
   "v2": [
    4164053,
    479450
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
     "src/requests/utils.py",
     "CaseInsensitiveDict"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_requests.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"tests/test_requests.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    2077232,
    239725
   ],
   "v2": [
    4164053,
    479450
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
     "tests/test_requests.py",
     "CaseInsensitiveDict"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_structures.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"tests/test_structures.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    2077232,
    239725
   ],
   "v2": [
    4164053,
    479450
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
     "tests/test_structures.py",
     "CaseInsensitiveDict"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_utils.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"tests/test_utils.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    2077232,
    239725
   ],
   "v2": [
    4164053,
    479450
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
     "tests/test_utils.py",
     "CaseInsensitiveDict"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/requests/sessions.py', 'CaseInsensitiveDict')",
  "key": "[\"symbols\", [\"src/requests/sessions.py\", \"CaseInsensitiveDict\"]]",
  "provenance": "`src/requests/sessions.py` had a matching line (step 3); its outline names every `CaseInsensitiveDict` import exactly",
  "v2": [
   4164053,
   479450
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
  "ok": "[\"symbols\", [\"src/requests/utils.py\", \"CaseInsensitiveDict\"]]",
  "cap": "[\"symbols\", [\"src/requests/utils.py\", \"CaseInsensitiveDict\"]]"
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
  "planned": "[\"symbols\", [\"src/requests/sessions.py\", \"CaseInsensitiveDict\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 6,
   "path": "src/requests/sessions.py",
   "filter": "CaseInsensitiveDict",
   "header": {
    "lines": 921,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/requests/sessions.py",
     "name": "CaseInsensitiveDict",
     "line": 47,
     "kind": "from",
     "src": ".structures",
     "src_name": "CaseInsensitiveDict",
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
   "src/requests/_types.py",
   "src/requests/adapters.py",
   "src/requests/models.py",
   "src/requests/sessions.py",
   "src/requests/utils.py",
   "tests/test_requests.py",
   "tests/test_structures.py",
   "tests/test_utils.py"
  ],
  "table": [
   [
    "src/requests/_types.py",
    "src/requests/_types.py:67",
    "in",
    "`.structures` resolves `CaseInsensitiveDict` to the target"
   ],
   [
    "src/requests/adapters.py",
    "src/requests/adapters.py:52",
    "in",
    "`.structures` resolves `CaseInsensitiveDict` to the target"
   ],
   [
    "src/requests/models.py",
    "src/requests/models.py:71",
    "in",
    "`.structures` resolves `CaseInsensitiveDict` to the target"
   ],
   [
    "src/requests/sessions.py",
    "src/requests/sessions.py:47",
    "in",
    "`.structures` resolves `CaseInsensitiveDict` to the target"
   ],
   [
    "src/requests/utils.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_requests.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_structures.py",
    null,
    "pending",
    "not yet examined"
```
</details>

## Step 7

`src/requests/sessions.py`: line 47 imports it from `.structures`.

Tally: 4 import statements confirmed, 0 ruled out, 4 pending. The search itself is complete; what is left is checking the candidates.

Next I will look at `src/requests/utils.py`'s top-level names for `CaseInsensitiveDict`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `tests/test_requests.py`'s top-level names for `CaseInsensitiveDict`.

**Call:** `symbols('src/requests/utils.py', 'CaseInsensitiveDict')`

**Response**: outcome `ok`

```
module src/requests/utils.py lines=1156 dynamic=no all=none
69 from CaseInsensitiveDict <- .structures CaseInsensitiveDict
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/requests/utils.py",
    "CaseInsensitiveDict"
   ],
   "desc": "look at `src/requests/utils.py`'s imports of `CaseInsensitiveDict`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_requests.py",
    "CaseInsensitiveDict"
   ],
   "desc": "look at `tests/test_requests.py`'s imports of `CaseInsensitiveDict`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_structures.py",
    "CaseInsensitiveDict"
   ],
   "desc": "look at `tests/test_structures.py`'s imports of `CaseInsensitiveDict`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_utils.py",
    "CaseInsensitiveDict"
   ],
   "desc": "look at `tests/test_utils.py`'s imports of `CaseInsensitiveDict`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/requests/utils.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"src/requests/utils.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    3325489,
    479450
   ],
   "v2": [
    1667539,
    239725
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
     "src/requests/utils.py",
     "CaseInsensitiveDict"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_requests.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"tests/test_requests.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    3325489,
    479450
   ],
   "v2": [
    1667539,
    239725
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
     "tests/test_requests.py",
     "CaseInsensitiveDict"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_structures.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"tests/test_structures.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    3325489,
    479450
   ],
   "v2": [
    1667539,
    239725
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
     "tests/test_structures.py",
     "CaseInsensitiveDict"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_utils.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"tests/test_utils.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    3325489,
    479450
   ],
   "v2": [
    1667539,
    239725
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
     "tests/test_utils.py",
     "CaseInsensitiveDict"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/requests/utils.py', 'CaseInsensitiveDict')",
  "key": "[\"symbols\", [\"src/requests/utils.py\", \"CaseInsensitiveDict\"]]",
  "provenance": "`src/requests/utils.py` had a matching line (step 3); its outline names every `CaseInsensitiveDict` import exactly",
  "v2": [
   1667539,
   239725
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
  "ok": "[\"symbols\", [\"tests/test_requests.py\", \"CaseInsensitiveDict\"]]",
  "cap": "[\"symbols\", [\"tests/test_requests.py\", \"CaseInsensitiveDict\"]]"
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
  "planned": "[\"symbols\", [\"src/requests/utils.py\", \"CaseInsensitiveDict\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 7,
   "path": "src/requests/utils.py",
   "filter": "CaseInsensitiveDict",
   "header": {
    "lines": 1156,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/requests/utils.py",
     "name": "CaseInsensitiveDict",
     "line": 69,
     "kind": "from",
     "src": ".structures",
     "src_name": "CaseInsensitiveDict",
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
   "src/requests/_types.py",
   "src/requests/adapters.py",
   "src/requests/models.py",
   "src/requests/sessions.py",
   "src/requests/utils.py",
   "tests/test_requests.py",
   "tests/test_structures.py",
   "tests/test_utils.py"
  ],
  "table": [
   [
    "src/requests/_types.py",
    "src/requests/_types.py:67",
    "in",
    "`.structures` resolves `CaseInsensitiveDict` to the target"
   ],
   [
    "src/requests/adapters.py",
    "src/requests/adapters.py:52",
    "in",
    "`.structures` resolves `CaseInsensitiveDict` to the target"
   ],
   [
    "src/requests/models.py",
    "src/requests/models.py:71",
    "in",
    "`.structures` resolves `CaseInsensitiveDict` to the target"
   ],
   [
    "src/requests/sessions.py",
    "src/requests/sessions.py:47",
    "in",
    "`.structures` resolves `CaseInsensitiveDict` to the target"
   ],
   [
    "src/requests/utils.py",
    "src/requests/utils.py:69",
    "in",
    "`.structures` resolves `CaseInsensitiveDict` to the target"
   ],
   [
    "tests/test_requests.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_structures.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_utils.py",
    null,
    "pending",
    "not yet examined"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  },
  "n_in": 5,
  "n_out": 0,
  "n_pending": 3
 }
}
```
</details>

## Step 8

`src/requests/utils.py`: line 69 imports it from `.structures`.

Tally: 5 import statements confirmed, 0 ruled out, 3 pending. The search itself is complete; what is left is checking the candidates.

I'll look at `tests/test_requests.py`'s top-level names for `CaseInsensitiveDict`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `tests/test_structures.py`'s top-level names for `CaseInsensitiveDict`.

**Call:** `symbols('tests/test_requests.py', 'CaseInsensitiveDict')`

**Response**: outcome `ok`

```
module tests/test_requests.py lines=3095 dynamic=no all=none
55 from CaseInsensitiveDict <- requests.structures CaseInsensitiveDict
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_requests.py",
    "CaseInsensitiveDict"
   ],
   "desc": "look at `tests/test_requests.py`'s imports of `CaseInsensitiveDict`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_structures.py",
    "CaseInsensitiveDict"
   ],
   "desc": "look at `tests/test_structures.py`'s imports of `CaseInsensitiveDict`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_utils.py",
    "CaseInsensitiveDict"
   ],
   "desc": "look at `tests/test_utils.py`'s imports of `CaseInsensitiveDict`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/test_requests.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"tests/test_requests.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    1248257,
    239725
   ],
   "v2": [
    2506103,
    479450
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
     "tests/test_requests.py",
     "CaseInsensitiveDict"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_structures.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"tests/test_structures.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    1248257,
    239725
   ],
   "v2": [
    2506103,
    479450
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
     "tests/test_structures.py",
     "CaseInsensitiveDict"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_utils.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"tests/test_utils.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    1248257,
    239725
   ],
   "v2": [
    2506103,
    479450
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
     "tests/test_utils.py",
     "CaseInsensitiveDict"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_requests.py', 'CaseInsensitiveDict')",
  "key": "[\"symbols\", [\"tests/test_requests.py\", \"CaseInsensitiveDict\"]]",
  "provenance": "`tests/test_requests.py` had a matching line (step 3); its outline names every `CaseInsensitiveDict` import exactly",
  "v2": [
   2506103,
   479450
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
  "ok": "[\"symbols\", [\"tests/test_structures.py\", \"CaseInsensitiveDict\"]]",
  "cap": "[\"symbols\", [\"tests/test_structures.py\", \"CaseInsensitiveDict\"]]"
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
  "planned": "[\"symbols\", [\"tests/test_requests.py\", \"CaseInsensitiveDict\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 8,
   "path": "tests/test_requests.py",
   "filter": "CaseInsensitiveDict",
   "header": {
    "lines": 3095,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_requests.py",
     "name": "CaseInsensitiveDict",
     "line": 55,
     "kind": "from",
     "src": "requests.structures",
     "src_name": "CaseInsensitiveDict",
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
   "src/requests/_types.py",
   "src/requests/adapters.py",
   "src/requests/models.py",
   "src/requests/sessions.py",
   "src/requests/utils.py",
   "tests/test_requests.py",
   "tests/test_structures.py",
   "tests/test_utils.py"
  ],
  "table": [
   [
    "src/requests/_types.py",
    "src/requests/_types.py:67",
    "in",
    "`.structures` resolves `CaseInsensitiveDict` to the target"
   ],
   [
    "src/requests/adapters.py",
    "src/requests/adapters.py:52",
    "in",
    "`.structures` resolves `CaseInsensitiveDict` to the target"
   ],
   [
    "src/requests/models.py",
    "src/requests/models.py:71",
    "in",
    "`.structures` resolves `CaseInsensitiveDict` to the target"
   ],
   [
    "src/requests/sessions.py",
    "src/requests/sessions.py:47",
    "in",
    "`.structures` resolves `CaseInsensitiveDict` to the target"
   ],
   [
    "src/requests/utils.py",
    "src/requests/utils.py:69",
    "in",
    "`.structures` resolves `CaseInsensitiveDict` to the target"
   ],
   [
    "tests/test_requests.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_structures.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_utils.py",
    null,
    "pending",
    "not yet examined"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  },
  "n_in": 5,
  "n_out": 0,
  "n_pending": 3
 }
}
```
</details>

## Step 9

The test module `tests/test_requests.py`: line 55 imports it from `requests.structures`.

Tally: 5 import statements confirmed, 0 ruled out, 3 pending. The search itself is complete; what is left is checking the candidates.

Let me look at `tests/test_structures.py`'s top-level names for `CaseInsensitiveDict`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will list `./` to see what lives there.

**Call:** `symbols('tests/test_structures.py', 'CaseInsensitiveDict')`

**Response**: outcome `ok`

```
module tests/test_structures.py lines=92 dynamic=no all=none
3 from CaseInsensitiveDict <- requests.structures CaseInsensitiveDict
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_requests.py",
    "requests.structures"
   ],
   "desc": "find where `requests.structures` (imported by `tests/test_requests.py`) lives"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_structures.py",
    "CaseInsensitiveDict"
   ],
   "desc": "look at `tests/test_structures.py`'s imports of `CaseInsensitiveDict`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_utils.py",
    "CaseInsensitiveDict"
   ],
   "desc": "look at `tests/test_utils.py`'s imports of `CaseInsensitiveDict`"
  }
 ],
 "candidates": [
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    305723,
    57534
   ],
   "v2": [
    3835921,
    719175
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
     "tests/test_requests.py",
     "requests.structures"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_structures.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"tests/test_structures.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    2637189,
    479450
   ],
   "v2": [
    3835921,
    719175
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
     "tests/test_structures.py",
     "CaseInsensitiveDict"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_utils.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"tests/test_utils.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    2637189,
    479450
   ],
   "v2": [
    3835921,
    719175
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
     "tests/test_utils.py",
     "CaseInsensitiveDict"
    ]
   ]
  },
  {
   "call": "symbols('requests/structures.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"requests/structures.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    1083523257618187,
    188777122021587
   ],
   "v2": [
    159766826466538199,
    28316568303238050
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     45826816,
     130376433
    ],
    "reexport": [
     428288,
     130376433
    ],
    "star": [
     107072,
     130376433
    ],
    "none": [
     642432,
     43458811
    ],
    "missing": [
     182011,
     289083
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_requests.py",
     "requests.structures"
    ]
   ]
  },
  {
   "call": "symbols('requests/structures/__init__.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"requests/structures/__init__.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    37712279052988,
    5846183614683
   ],
   "v2": [
    613366217502073,
    97436393578050
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     50907,
     7130714
    ],
    "reexport": [
     254535,
     7130714
    ],
    "star": [
     16969,
     21392142
    ],
    "none": [
     322411,
     21392142
    ],
    "missing": [
     272114,
     289083
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_requests.py",
     "requests.structures"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+CaseInsensitiveDict\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+CaseInsensitiveDict\\\\b\", \".\"]]",
   "v1": [
    62141,
    9589
   ],
   "v2": [
    363257,
    57534
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
     "tests/test_requests.py",
     "requests.structures"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+CaseInsensitiveDict\\\\b', 'src')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+CaseInsensitiveDict\\\\b\", \"src\"]]",
   "v1": [
    62141,
    9589
   ],
   "v2": [
    363257,
    57534
   ],
   "p_cap": [
    1,
    244
   ],
   "forecast": {
    "zero": [
     205,
     244
    ],
    "mid": [
     19,
     122
    ],
    "cap": [
     1,
     244
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_requests.py",
     "requests.structures"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_structures.py', 'CaseInsensitiveDict')",
  "key": "[\"symbols\", [\"tests/test_structures.py\", \"CaseInsensitiveDict\"]]",
  "provenance": "`tests/test_structures.py` had a matching line (step 3); its outline names every `CaseInsensitiveDict` import exactly",
  "v2": [
   3835921,
   719175
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
  "planned": "[\"symbols\", [\"tests/test_structures.py\", \"CaseInsensitiveDict\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 9,
   "path": "tests/test_structures.py",
   "filter": "CaseInsensitiveDict",
   "header": {
    "lines": 92,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_structures.py",
     "name": "CaseInsensitiveDict",
     "line": 3,
     "kind": "from",
     "src": "requests.structures",
     "src_name": "CaseInsensitiveDict",
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
   "src/requests/_types.py",
   "src/requests/adapters.py",
   "src/requests/models.py",
   "src/requests/sessions.py",
   "sr
```
</details>

## Step 10

The test module `tests/test_structures.py`: line 3 imports it from `requests.structures`.

Tally: 5 import statements confirmed, 0 ruled out, 3 pending. The search itself is complete; what is left is checking the candidates.

Let me list `./` to see what lives there; the listing settles whether the import is a module, a package, or not here at all. Very likely the listing fits. If the listing is too long, I will outline `requests/structures.py` directly, which both checks that the file exists and shows me `CaseInsensitiveDict`. I could outline `requests/structures.py` directly, which both checks that the file exists and shows me `CaseInsensitiveDict` instead, but it costs more calls in expectation.

**Call:** `ls('.')`

**Response**: outcome `complete`

```
.github/
.pre-commit-config.yaml
.readthedocs.yaml
AUTHORS.rst
HISTORY.md
MANIFEST.in
README.md
docs/
pyproject.toml
requirements-dev.txt
setup.py
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
    "tests/test_requests.py",
    "requests.structures"
   ],
   "desc": "find where `requests.structures` (imported by `tests/test_requests.py`) lives"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_structures.py",
    "requests.structures"
   ],
   "desc": "find where `requests.structures` (imported by `tests/test_structures.py`) lives"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_utils.py",
    "CaseInsensitiveDict"
   ],
   "desc": "look at `tests/test_utils.py`'s imports of `CaseInsensitiveDict`"
  }
 ],
 "candidates": [
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    255481,
    57534
   ],
   "v2": [
    184647853651152667,
    42474852454857075
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
     "tests/test_requests.py",
     "requests.structures"
    ],
    [
     "module_path",
     "tests/test_structures.py",
     "requests.structures"
    ]
   ]
  },
  {
   "call": "symbols('requests/structures.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"requests/structures.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    1995008097088723,
    377554244043174
   ],
   "v2": [
    126063985466373049,
    28316568303238050
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     45826816,
     130376433
    ],
    "reexport": [
     428288,
     130376433
    ],
    "star": [
     107072,
     130376433
    ],
    "none": [
     642432,
     43458811
    ],
    "missing": [
     182011,
     289083
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_requests.py",
     "requests.structures"
    ],
    [
     "module_path",
     "tests/test_structures.py",
     "requests.structures"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_utils.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"tests/test_utils.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    1388932,
    239725
   ],
   "v2": [
    3207896,
    719175
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
     "tests/test_utils.py",
     "CaseInsensitiveDict"
    ]
   ]
  },
  {
   "call": "symbols('requests/structures/__init__.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"requests/structures/__init__.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    77467146554339,
    11692367229366
   ],
   "v2": [
    785077045114322,
    146154590367075
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     50907,
     7130714
    ],
    "reexport": [
     254535,
     7130714
    ],
    "star": [
     16969,
     21392142
    ],
    "none": [
     322411,
     21392142
    ],
    "missing": [
     272114,
     289083
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_requests.py",
     "requests.structures"
    ],
    [
     "module_path",
     "tests/test_structures.py",
     "requests.structures"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+CaseInsensitiveDict\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+CaseInsensitiveDict\\\\b\", \".\"]]",
   "v1": [
    129909,
    19178
   ],
   "v2": [
    313015,
    57534
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
     "tests/test_requests.py",
     "requests.structures"
    ],
    [
     "module_path",
     "tests/test_structures.py",
     "requests.structures"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+CaseInsensitiveDict\\\\b', 'src')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+CaseInsensitiveDict\\\\b\", \"src\"]]",
   "v1": [
    129909,
    19178
   ],
   "v2": [
    313015,
    57534
   ],
   "p_cap": [
    1,
    244
   ],
   "forecast": {
    "zero": [
     205,
     244
    ],
    "mid": [
     19,
     122
    ],
    "cap": [
     1,
     244
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_requests.py",
     "requests.structures"
    ],
    [
     "module_path",
     "tests/test_structures.py",
     "requests.structures"
    ]
   ]
  }
 ],
 "choice": {
  "call": "ls('.')",
  "key": "[\"ls\", [\".\"]]",
  "provenance": "`requests.structures` imported by `tests/test_requests.py` should live under `.`",
  "v2": [
   184647853651152667,
   42474852454857075
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
  "complete": "[\"symbols\", [\"tests/test_utils.py\", \"CaseInsensitiveDict\"]]",
  "cap": "[\"symbols\", [\"requests/structures.py\", \"CaseInsensitiveDict\"]]"
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
   "step": 10,
   "dir": ".",
   "entries": [
    ".github/",
    ".pre-commit-config.yaml",
    ".readthedocs.yaml",
    "AUTHORS.rst",
    "HISTORY.md",
    "MANIFEST.in",
    "README.md",
    "docs/",
    "pyproject.toml",
    "requirements-dev.txt",
    "setup.py",
    "src/",
    "tests/",
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
   "src/requests/_types.py",
   "src/requests/adapters.py",
   "src/requests/models.py",
   "src/requests/sessions.py",
   "src/requests/utils.py",
   "tests/test_requests.py",
   "tests/test_structures.py",
   "tests/test_utils.py"
  ],
  "table": [
   [
    "src/requests/_types.py",
    "src/requests/_types.py:67",
    "in",

```
</details>

## Step 11

`./` has 14 entries: there is no `requests` here.

I'll look at `tests/test_utils.py`'s top-level names for `CaseInsensitiveDict`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I follow whatever it opens up.

**Call:** `symbols('tests/test_utils.py', 'CaseInsensitiveDict')`

**Response**: outcome `ok`

```
module tests/test_utils.py lines=1014 dynamic=no all=none
15 from CaseInsensitiveDict <- requests.structures CaseInsensitiveDict
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_utils.py",
    "CaseInsensitiveDict"
   ],
   "desc": "look at `tests/test_utils.py`'s imports of `CaseInsensitiveDict`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/test_utils.py', 'CaseInsensitiveDict')",
   "key": "[\"symbols\", [\"tests/test_utils.py\", \"CaseInsensitiveDict\"]]",
   "v1": [
    419282,
    239725
   ],
   "v2": [
    419282,
    239725
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
     "tests/test_utils.py",
     "CaseInsensitiveDict"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_utils.py', 'CaseInsensitiveDict')",
  "key": "[\"symbols\", [\"tests/test_utils.py\", \"CaseInsensitiveDict\"]]",
  "provenance": "`tests/test_utils.py` had a matching line (step 3); its outline names every `CaseInsensitiveDict` import exactly",
  "v2": [
   419282,
   239725
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
  "planned": "[\"symbols\", [\"tests/test_utils.py\", \"CaseInsensitiveDict\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 11,
   "path": "tests/test_utils.py",
   "filter": "CaseInsensitiveDict",
   "header": {
    "lines": 1014,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_utils.py",
     "name": "CaseInsensitiveDict",
     "line": 15,
     "kind": "from",
     "src": "requests.structures",
     "src_name": "CaseInsensitiveDict",
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
   "src/requests/_types.py",
   "src/requests/adapters.py",
   "src/requests/models.py",
   "src/requests/sessions.py",
   "src/requests/utils.py",
   "tests/test_requests.py",
   "tests/test_structures.py",
   "tests/test_utils.py"
  ],
  "table": [
   [
    "src/requests/_types.py",
    "src/requests/_types.py:67",
    "in",
    "`.structures` resolves `CaseInsensitiveDict` to the target"
   ],
   [
    "src/requests/adapters.py",
    "src/requests/adapters.py:52",
    "in",
    "`.structures` resolves `CaseInsensitiveDict` to the target"
   ],
   [
    "src/requests/models.py",
    "src/requests/models.py:71",
    "in",
    "`.structures` resolves `CaseInsensitiveDict` to the target"
   ],
   [
    "src/requests/sessions.py",
    "src/requests/sessions.py:47",
    "in",
    "`.structures` resolves `CaseInsensitiveDict` to the target"
   ],
   [
    "src/requests/utils.py",
    "src/requests/utils.py:69",
    "in",
    "`.structures` resolves `CaseInsensitiveDict` to the target"
   ],
   [
    "tests/test_requests.py",
    "tests/test_requests.py:55",
    "in",
    "`requests.structures` resolves `CaseInsensitiveDict` to the target"
   ],
   [
    "tests/test_structures.py",
    "tests/test_structures.py:3",
    "in",
    "`requests.structures` resolves `CaseInsensitiveDict` to the target"
   ],
   [
    "tests/test_utils.py",
    "tests/test_utils.py:15",
    "in",
    "`requests.structures` resolves `CaseInsensitiveDict` to the target"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  },
  "n_in": 8,
  "n_out": 0,
  "n_pending": 0
 }
}
```
</details>

## Final

`CaseInsensitiveDict` is the class at `src/requests/structures.py:20`. 8 module-level import statements bring in this definition: `src/requests/_types.py:67`, `src/requests/adapters.py:52`, `src/requests/models.py:71`, `src/requests/sessions.py:47`, `src/requests/utils.py:69`, `tests/test_requests.py:55`, `tests/test_structures.py:3`, `tests/test_utils.py:15`. Looking back, all 11 calls were needed.

**Answer:** `{"final_kind": "importers", "final": ["src/requests/_types.py:67", "src/requests/adapters.py:52", "src/requests/models.py:71", "src/requests/sessions.py:47", "src/requests/utils.py:69", "tests/test_requests.py:55", "tests/test_structures.py:3", "tests/test_utils.py:15"], "steps": [{"op": "resolve", "output": {"kind": "def", "path": "src/requests/structures.py", "line": 20, "name": "CaseInsensitiveDict", "detail": "class"}}, {"op": "importers", "output": ["src/requests/_types.py:67", "src/requests/adapters.py:52", "src/requests/models.py:71", "src/requests/sessions.py:47", "src/requests/utils.py:69", "tests/test_requests.py:55", "tests/test_structures.py:3", "tests/test_utils.py:15"]}], "stuck": null}`  
**Stopped:** certificate after 11 calls