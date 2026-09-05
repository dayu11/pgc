# black-callers-622092b7

**Repository:** black  
**Chain:** resolve → callers  
**Seed:** 0, prior f2e0b46ccc75305a, floor 6

## Task

In `src/black/linegen.py` line 38, `is_rpar_token` is imported from `black.nodes`. Which definition does the module-level name `is_rpar_token` actually refer to? Give `path:line`. Then list every call site of it: bare-name calls whose module-level binding resolves to this definition, as `path:line`.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N; bindings take effect in source order. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. A class derives from a definition when a base written as a bare name or `module.Name` resolves to it. A call site is `name(...)` where the bare name refers to the module-level binding (not a parameter or local). Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

I need to find what `is_rpar_token` really is in `src/black/linegen.py`: line 38 imports it from `black.nodes`, so the definition is at least one hop away. Then every real call site of it, which means checking what the name refers to in each file that mentions it.

Next I will check `src/black/linegen.py` for any other binding of `is_rpar_token` besides the import on line 38; almost certainly the import is the only one, and then `black.nodes` is the place to follow.

**Call:** `symbols('src/black/linegen.py', 'is_rpar_token')`

**Response**: outcome `reexport`

```
module src/black/linegen.py lines=2339 dynamic=no all=none
38 from is_rpar_token <- black.nodes is_rpar_token
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/black/linegen.py",
    "is_rpar_token"
   ],
   "desc": "check the top-level names of `src/black/linegen.py` for `is_rpar_token`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/black/linegen.py', 'is_rpar_token')",
   "key": "[\"symbols\", [\"src/black/linegen.py\", \"is_rpar_token\"]]",
   "v1": [
    734757,
    251000
   ],
   "v2": [
    734757,
    251000
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
     "src/black/linegen.py",
     "is_rpar_token"
    ]
   ]
  },
  {
   "call": "symbols('src/black/linegen.py')",
   "key": "[\"symbols\", [\"src/black/linegen.py\"]]",
   "v1": [
    36353329,
    11797000
   ],
   "v2": [
    36353329,
    11797000
   ],
   "p_cap": [
    29,
    188
   ],
   "forecast": {
    "def": [
     159,
     18800
    ],
    "reexport": [
     14787,
     18800
    ],
    "star": [
     159,
     18800
    ],
    "none": [
     159,
     3760
    ],
    "cap": [
     29,
     188
    ]
   },
   "serves": [
    [
     "bindings",
     "src/black/linegen.py",
     "is_rpar_token"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/black/linegen.py', 'is_rpar_token')",
  "key": "[\"symbols\", [\"src/black/linegen.py\", \"is_rpar_token\"]]",
  "provenance": "module `src/black/linegen.py` (task), name `is_rpar_token` (task)",
  "v2": [
   734757,
   251000
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
   "path": "src/black/linegen.py",
   "filter": "is_rpar_token",
   "header": {
    "lines": 2339,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/black/linegen.py",
     "name": "is_rpar_token",
     "line": 38,
     "kind": "from",
     "src": "black.nodes",
     "src_name": "is_rpar_token",
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
    "src/black/linegen.py",
    "is_rpar_token",
    "reexport",
    [
     "black.nodes",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 2

`src/black/linegen.py` does not define `is_rpar_token` itself; line 38 imports it from `black.nodes`.

So far: `src/black/linegen.py` takes `is_rpar_token` from `black.nodes`, which I still have to locate.

Let me list `./` to see what lives there; the listing settles whether the import is a module, a package, or not here at all. Very likely the listing fits. If the listing is too long, I will outline `black/nodes.py` directly, which both checks that the file exists and shows me `is_rpar_token`. I could outline `black/nodes.py` directly, which both checks that the file exists and shows me `is_rpar_token` instead, but it costs more calls in expectation.

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
    "src/black/linegen.py",
    "black.nodes"
   ],
   "desc": "find where `black.nodes` (imported by `src/black/linegen.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    113,
    60
   ],
   "v2": [
    1204260299491,
    614547852820
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
     "src/black/linegen.py",
     "black.nodes"
    ]
   ]
  },
  {
   "call": "symbols('black/nodes.py', 'is_rpar_token')",
   "key": "[\"symbols\", [\"black/nodes.py\", \"is_rpar_token\"]]",
   "v1": [
    1470701393341,
    614547852820
   ],
   "v2": [
    1401917069711,
    614547852820
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     37711296,
     122419891
    ],
    "reexport": [
     891520,
     122419891
    ],
    "star": [
     89152,
     122419891
    ],
    "none": [
     1515584,
     122419891
    ],
    "missing": [
     182289,
     271441
    ]
   },
   "serves": [
    [
     "module_path",
     "src/black/linegen.py",
     "black.nodes"
    ]
   ]
  },
  {
   "call": "symbols('black/nodes/__init__.py', 'is_rpar_token')",
   "key": "[\"symbols\", [\"black/nodes/__init__.py\", \"is_rpar_token\"]]",
   "v1": [
    8243792347,
    2733410870
   ],
   "v2": [
    7812605017,
    2733410870
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     217905,
     20629516
    ],
    "reexport": [
     624661,
     20629516
    ],
    "star": [
     14527,
     20629516
    ],
    "none": [
     246959,
     20629516
    ],
    "missing": [
     256914,
     271441
    ]
   },
   "serves": [
    [
     "module_path",
     "src/black/linegen.py",
     "black.nodes"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+is_rpar_token\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+is_rpar_token\\\\b\", \".\"]]",
   "v1": [
    61,
    20
   ],
   "v2": [
    173,
    60
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
     "src/black/linegen.py",
     "black.nodes"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+is_rpar_token\\\\b', 'src')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+is_rpar_token\\\\b\", \"src\"]]",
   "v1": [
    61,
    20
   ],
   "v2": [
    173,
    60
   ],
   "p_cap": [
    1,
    265
   ],
   "forecast": {
    "zero": [
     218,
     265
    ],
    "mid": [
     46,
     265
    ],
    "cap": [
     1,
     265
    ]
   },
   "serves": [
    [
     "module_path",
     "src/black/linegen.py",
     "black.nodes"
    ]
   ]
  }
 ],
 "choice": {
  "call": "ls('.')",
  "key": "[\"ls\", [\".\"]]",
  "provenance": "`black.nodes` imported by `src/black/linegen.py` should live under `.`",
  "v2": [
   1204260299491,
   614547852820
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
  "cap": "[\"symbols\", [\"black/nodes.py\", \"is_rpar_token\"]]"
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
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "listing",
   "step": 2,
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
  "phase": "resolve",
  "step": 1,
  "of": 2,
  "chain": [
   [
    "src/black/linegen.py",
    "is_rpar_token",
    "reexport",
    [
     "black.nodes",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 3

`./` has 20 entries: there is no `black` here.

So far: `src/black/linegen.py` takes `is_rpar_token` from `black.nodes`, which I still have to locate.

I'll outline `src/black/nodes.py` directly, which both checks that the file exists and shows me `is_rpar_token`; if `black.nodes` is a plain module that is where it has to be. Very likely it is defined right there. If the file does not exist, I will list `src/black/` to see what lives there; if the name is not bound there, that finishes it. I could list `src/black/` to see what lives there instead, but it tends to open more follow-up work.

**Call:** `symbols('src/black/nodes.py', 'is_rpar_token')`

**Response**: outcome `def`

```
module src/black/nodes.py lines=1145 dynamic=no all=none
1075 def is_rpar_token
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/black/linegen.py",
    "black.nodes"
   ],
   "desc": "find where `black.nodes` (imported by `src/black/linegen.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/black/nodes.py', 'is_rpar_token')",
   "key": "[\"symbols\", [\"src/black/nodes.py\", \"is_rpar_token\"]]",
   "v1": [
    1569150741,
    1179554420
   ],
   "v2": [
    284677377961,
    213499350020
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     189504,
     234971
    ],
    "reexport": [
     4480,
     234971
    ],
    "star": [
     448,
     234971
    ],
    "none": [
     7616,
     234971
    ],
    "missing": [
     73,
     521
    ]
   },
   "serves": [
    [
     "module_path",
     "src/black/linegen.py",
     "black.nodes"
    ]
   ]
  },
  {
   "call": "ls('src/black')",
   "key": "[\"ls\", [\"src/black\"]]",
   "v1": [
    7501,
    3620
   ],
   "v2": [
    438996141941,
    213499350020
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
     "src/black/linegen.py",
     "black.nodes"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+is_rpar_token\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+is_rpar_token\\\\b\", \".\"]]",
   "v1": [
    32,
    15
   ],
   "v2": [
    2445638111,
    1179554420
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
     "src/black/linegen.py",
     "black.nodes"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+is_rpar_token\\\\b', 'src')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+is_rpar_token\\\\b\", \"src\"]]",
   "v1": [
    3049,
    1060
   ],
   "v2": [
    142639682413,
    62516384260
   ],
   "p_cap": [
    1,
    265
   ],
   "forecast": {
    "zero": [
     218,
     265
    ],
    "mid": [
     46,
     265
    ],
    "cap": [
     1,
     265
    ]
   },
   "serves": [
    [
     "module_path",
     "src/black/linegen.py",
     "black.nodes"
    ]
   ]
  },
  {
   "call": "symbols('src/black/nodes/__init__.py', 'is_rpar_token')",
   "key": "[\"symbols\", [\"src/black/nodes/__init__.py\", \"is_rpar_token\"]]",
   "v1": [
    1553384,
    524647
   ],
   "v2": [
    72465772653288,
    30942484389487
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     1095,
     39596
    ],
    "reexport": [
     3139,
     39596
    ],
    "star": [
     73,
     39596
    ],
    "none": [
     1241,
     39596
    ],
    "missing": [
     448,
     521
    ]
   },
   "serves": [
    [
     "module_path",
     "src/black/linegen.py",
     "black.nodes"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/black/nodes.py', 'is_rpar_token')",
  "key": "[\"symbols\", [\"src/black/nodes.py\", \"is_rpar_token\"]]",
  "provenance": "`black.nodes` would be `src/black/nodes.py` if that file exists; one call both checks and closes it",
  "v2": [
   284677377961,
   213499350020
  ]
 },
 "forecast": {
  "def": [
   189504,
   234971
  ],
  "reexport": [
   4480,
   234971
  ],
  "star": [
   448,
   234971
  ],
  "none": [
   7616,
   234971
  ],
  "missing": [
   73,
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
 "hedges": [
  {
   "outcome": "def",
   "word": "very likely",
   "p": [
    189504,
    234971
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
   "step": 3,
   "path": "src/black/nodes.py",
   "filter": "is_rpar_token",
   "header": {
    "lines": 1145,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/black/nodes.py",
     "name": "is_rpar_token",
     "line": 1075,
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
  "of": 2,
  "chain": [
   [
    "src/black/linegen.py",
    "is_rpar_token",
    "reexport",
    [
     "black.nodes",
     "src/black/nodes.py"
    ]
   ],
   [
    "src/black/nodes.py",
    "is_rpar_token",
    "def",
    1075
   ]
  ]
 }
}
```
</details>

## Step 4

There it is: `is_rpar_token` is a function at `src/black/nodes.py:1075`. That settles the definition; now its call sites.

I'll search the whole tree for calls of `is_rpar_token`; the search has to be complete before I can call the set final. Probably it fits under the cap. If nothing turns up, that finishes it; if it caps, I follow whatever it opens up.

**Call:** `grep('\\bis_rpar_token\\s*\\(', '.')`

**Response**: outcome `mid`

```
src/black/linegen.py:387:                    and is_rpar_token(child.children[2])
src/black/linegen.py:1638:        and is_rpar_token(node.children[-1])
src/black/linegen.py:1653:        or not is_rpar_token(node.children[-1])
src/black/linegen.py:1784:                    if is_lpar_token(opening) and is_rpar_token(closing):
src/black/linegen.py:1846:        assert is_rpar_token(parent.children[-1])
src/black/linegen.py:2117:    if is_lpar_token(first) and is_rpar_token(last):
src/black/nodes.py:1075:def is_rpar_token(nl: NL) -> TypeGuard[Leaf]:
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "cover",
   "key": [
    "cover",
    "CALL",
    "."
   ],
   "desc": "search `.` for calls of `is_rpar_token`"
  }
 ],
 "candidates": [
  {
   "call": "grep('\\\\bis_rpar_token\\\\s*\\\\(', '.')",
   "key": "[\"grep\", [\"\\\\bis_rpar_token\\\\s*\\\\(\", \".\"]]",
   "v1": [
    30919343867,
    25148581920
   ],
   "v2": [
    30919343867,
    25148581920
   ],
   "p_cap": [
    1,
    36
   ],
   "forecast": {
    "zero": [
     1,
     4
    ],
    "mid": [
     13,
     18
    ],
    "cap": [
     1,
     36
    ]
   },
   "serves": [
    [
     "cover",
     "CALL",
     "."
    ]
   ]
  }
 ],
 "choice": {
  "call": "grep('\\\\bis_rpar_token\\\\s*\\\\(', '.')",
  "key": "[\"grep\", [\"\\\\bis_rpar_token\\\\s*\\\\(\", \".\"]]",
  "provenance": "call lines naming `is_rpar_token` under `.` (derived)",
  "v2": [
   30919343867,
   25148581920
  ]
 },
 "forecast": {
  "zero": [
   1,
   4
  ],
  "mid": [
   13,
   18
  ],
  "cap": [
   1,
   36
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
    13,
    18
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
   "step": 4,
   "pattern": "\\bis_rpar_token\\s*\\(",
   "scope": ".",
   "hits": [
    [
     "src/black/linegen.py",
     387
    ],
    [
     "src/black/linegen.py",
     1638
    ],
    [
     "src/black/linegen.py",
     1653
    ],
    [
     "src/black/linegen.py",
     1784
    ],
    [
     "src/black/linegen.py",
     1846
    ],
    [
     "src/black/linegen.py",
     2117
    ],
    [
     "src/black/nodes.py",
     1075
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "phase": "callers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/black/linegen.py",
   "src/black/nodes.py"
  ],
  "table": [
   [
    "src/black/linegen.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/black/nodes.py",
    null,
    "pending",
    "not yet examined"
   ]
  ],
  "uncovered": {
   "CALL": []
  },
  "n_in": 0,
  "n_out": 0,
  "n_pending": 2
 }
}
```
</details>

## Step 5

7 matching lines anywhere for calls of `is_rpar_token`, in `src/black/linegen.py`, `src/black/nodes.py`, and the search was under the cap, so that is the complete set there.

Let me list the call sites of `is_rpar_token` in `src/black/linegen.py`; the name is ours there, so each call site counts. Almost certainly the call sites fit. If there are too many call sites, I will list the call sites of `is_rpar_token` in `src/black/nodes.py`.

**Call:** `calls('src/black/linegen.py', 'is_rpar_token')`

**Response**: outcome `ok`

```
calls of is_rpar_token in src/black/linegen.py count=6
387:                    and is_rpar_token(child.children[2])
1638:        and is_rpar_token(node.children[-1])
1653:        or not is_rpar_token(node.children[-1])
1784:                    if is_lpar_token(opening) and is_rpar_token(closing):
1846:        assert is_rpar_token(parent.children[-1])
2117:    if is_lpar_token(first) and is_rpar_token(last):
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/black/linegen.py",
    "is_rpar_token"
   ],
   "desc": "list the call sites of `is_rpar_token` in `src/black/linegen.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/black/nodes.py",
    "is_rpar_token"
   ],
   "desc": "list the call sites of `is_rpar_token` in `src/black/nodes.py`"
  }
 ],
 "candidates": [
  {
   "call": "calls('src/black/linegen.py', 'is_rpar_token')",
   "key": "[\"calls\", [\"src/black/linegen.py\", \"is_rpar_token\"]]",
   "v1": [
    41,
    20
   ],
   "v2": [
    21,
    10
   ],
   "p_cap": [
    1,
    20
   ],
   "forecast": {
    "ok": [
     19,
     20
    ],
    "cap": [
     1,
     20
    ]
   },
   "serves": [
    [
     "calls",
     "src/black/linegen.py",
     "is_rpar_token"
    ]
   ]
  },
  {
   "call": "calls('src/black/nodes.py', 'is_rpar_token')",
   "key": "[\"calls\", [\"src/black/nodes.py\", \"is_rpar_token\"]]",
   "v1": [
    41,
    20
   ],
   "v2": [
    21,
    10
   ],
   "p_cap": [
    1,
    20
   ],
   "forecast": {
    "ok": [
     19,
     20
    ],
    "cap": [
     1,
     20
    ]
   },
   "serves": [
    [
     "calls",
     "src/black/nodes.py",
     "is_rpar_token"
    ]
   ]
  }
 ],
 "choice": {
  "call": "calls('src/black/linegen.py', 'is_rpar_token')",
  "key": "[\"calls\", [\"src/black/linegen.py\", \"is_rpar_token\"]]",
  "provenance": "call sites of `is_rpar_token` in `src/black/linegen.py` that refer to the module-level binding",
  "v2": [
   21,
   10
  ]
 },
 "forecast": {
  "ok": [
   19,
   20
  ],
  "cap": [
   1,
   20
  ]
 },
 "plan": {
  "ok": "[\"calls\", [\"src/black/nodes.py\", \"is_rpar_token\"]]",
  "cap": "[\"calls\", [\"src/black/nodes.py\", \"is_rpar_token\"]]"
 },
 "hedges": [
  {
   "outcome": "ok",
   "word": "almost certainly",
   "p": [
    19,
    20
   ]
  }
 ],
 "adherence": {
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "calls",
   "step": 5,
   "path": "src/black/linegen.py",
   "name": "is_rpar_token",
   "lines": [
    387,
    1638,
    1653,
    1784,
    1846,
    2117
   ],
   "count": 6,
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "callers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/black/linegen.py",
   "src/black/nodes.py"
  ],
  "table": [
   [
    "src/black/linegen.py",
    "src/black/linegen.py:387",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/black/linegen.py",
    "src/black/linegen.py:1638",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/black/linegen.py",
    "src/black/linegen.py:1653",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/black/linegen.py",
    "src/black/linegen.py:1784",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/black/linegen.py",
    "src/black/linegen.py:1846",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/black/linegen.py",
    "src/black/linegen.py:2117",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/black/nodes.py",
    null,
    "pending",
    "not yet examined"
   ]
  ],
  "uncovered": {
   "CALL": []
  },
  "n_in": 6,
  "n_out": 0,
  "n_pending": 1
 }
}
```
</details>

## Step 6

`src/black/linegen.py` calls `is_rpar_token` at lines 387, 1638, 1653, 1784, 1846, 2117, and those are real calls of the module-level name, not a shadowed local.

Tally: 6 call sites confirmed, 0 ruled out, 1 pending. The search itself is complete; what is left is checking the candidates.

Next I will list the call sites of `is_rpar_token` in `src/black/nodes.py`; the name is ours there, so each call site counts. Almost certainly the call sites fit. If there are too many call sites, I follow whatever it opens up.

**Call:** `calls('src/black/nodes.py', 'is_rpar_token')`

**Response**: outcome `ok`

```
calls of is_rpar_token in src/black/nodes.py count=0
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/black/nodes.py",
    "is_rpar_token"
   ],
   "desc": "list the call sites of `is_rpar_token` in `src/black/nodes.py`"
  }
 ],
 "candidates": [
  {
   "call": "calls('src/black/nodes.py', 'is_rpar_token')",
   "key": "[\"calls\", [\"src/black/nodes.py\", \"is_rpar_token\"]]",
   "v1": [
    21,
    20
   ],
   "v2": [
    21,
    20
   ],
   "p_cap": [
    1,
    20
   ],
   "forecast": {
    "ok": [
     19,
     20
    ],
    "cap": [
     1,
     20
    ]
   },
   "serves": [
    [
     "calls",
     "src/black/nodes.py",
     "is_rpar_token"
    ]
   ]
  }
 ],
 "choice": {
  "call": "calls('src/black/nodes.py', 'is_rpar_token')",
  "key": "[\"calls\", [\"src/black/nodes.py\", \"is_rpar_token\"]]",
  "provenance": "call sites of `is_rpar_token` in `src/black/nodes.py` that refer to the module-level binding",
  "v2": [
   21,
   20
  ]
 },
 "forecast": {
  "ok": [
   19,
   20
  ],
  "cap": [
   1,
   20
  ]
 },
 "plan": {
  "ok": "done",
  "cap": "continue"
 },
 "hedges": [
  {
   "outcome": "ok",
   "word": "almost certainly",
   "p": [
    19,
    20
   ]
  }
 ],
 "adherence": {
  "planned": "[\"calls\", [\"src/black/nodes.py\", \"is_rpar_token\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "calls",
   "step": 6,
   "path": "src/black/nodes.py",
   "name": "is_rpar_token",
   "lines": [],
   "count": 0,
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "callers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/black/linegen.py",
   "src/black/nodes.py"
  ],
  "table": [
   [
    "src/black/linegen.py",
    "src/black/linegen.py:387",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/black/linegen.py",
    "src/black/linegen.py:1638",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/black/linegen.py",
    "src/black/linegen.py:1653",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/black/linegen.py",
    "src/black/linegen.py:1784",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/black/linegen.py",
    "src/black/linegen.py:1846",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/black/linegen.py",
    "src/black/linegen.py:2117",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/black/nodes.py",
    "src/black/nodes.py",
    "out",
    "the module binds the name but never calls it by bare name"
   ]
  ],
  "uncovered": {
   "CALL": []
  },
  "n_in": 6,
  "n_out": 1,
  "n_pending": 0
 }
}
```
</details>

## Final

`is_rpar_token` is the def at `src/black/nodes.py:1075`. 6 call sites in 1 modules: `src/black/linegen.py:387`, `src/black/linegen.py:1638`, `src/black/linegen.py:1653`, `src/black/linegen.py:1784`, `src/black/linegen.py:1846`, `src/black/linegen.py:2117`. Ruled out along the way: `src/black/nodes.py` (the module binds the name but never calls it by bare name). Looking back, all 6 calls were needed.

**Answer:** `{"final_kind": "callers", "final": ["src/black/linegen.py:387", "src/black/linegen.py:1638", "src/black/linegen.py:1653", "src/black/linegen.py:1784", "src/black/linegen.py:1846", "src/black/linegen.py:2117"], "steps": [{"op": "resolve", "output": {"kind": "def", "path": "src/black/nodes.py", "line": 1075, "name": "is_rpar_token", "detail": "def"}}, {"op": "callers", "output": ["src/black/linegen.py:387", "src/black/linegen.py:1638", "src/black/linegen.py:1653", "src/black/linegen.py:1784", "src/black/linegen.py:1846", "src/black/linegen.py:2117"]}], "stuck": null}`  
**Stopped:** certificate after 6 calls