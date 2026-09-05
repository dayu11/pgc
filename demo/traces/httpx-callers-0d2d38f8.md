# httpx-callers-0d2d38f8

**Repository:** httpx  
**Chain:** resolve → callers  
**Seed:** 0, prior 708591d2904e1ac3, floor 8

## Task

In `tests/test_utils.py` line 9, `URLPattern` is imported from `httpx._utils`. Which definition does the module-level name `URLPattern` actually refer to? Give `path:line`. Then list every call site of it: bare-name calls whose module-level binding resolves to this definition, as `path:line`.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N; bindings take effect in source order. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. A class derives from a definition when a base written as a bare name or `module.Name` resolves to it. A call site is `name(...)` where the bare name refers to the module-level binding (not a parameter or local). Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

I need to find what `URLPattern` really is in `tests/test_utils.py`: line 9 imports it from `httpx._utils`, so the definition is at least one hop away. Then every real call site of it, which means checking what the name refers to in each file that mentions it.

Next I will check `tests/test_utils.py` for any other binding of `URLPattern` besides the import on line 9; almost certainly the import is the only one, and then `httpx._utils` is the place to follow.

**Call:** `symbols('tests/test_utils.py', 'URLPattern')`

**Response**: outcome `reexport`

```
module tests/test_utils.py lines=151 dynamic=no all=none
9 from URLPattern <- httpx._utils URLPattern
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "tests/test_utils.py",
    "URLPattern"
   ],
   "desc": "check the top-level names of `tests/test_utils.py` for `URLPattern`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/test_utils.py', 'URLPattern')",
   "key": "[\"symbols\", [\"tests/test_utils.py\", \"URLPattern\"]]",
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
     "tests/test_utils.py",
     "URLPattern"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_utils.py')",
   "key": "[\"symbols\", [\"tests/test_utils.py\"]]",
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
     "tests/test_utils.py",
     "URLPattern"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_utils.py', 'URLPattern')",
  "key": "[\"symbols\", [\"tests/test_utils.py\", \"URLPattern\"]]",
  "provenance": "module `tests/test_utils.py` (task), name `URLPattern` (task)",
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
   "path": "tests/test_utils.py",
   "filter": "URLPattern",
   "header": {
    "lines": 151,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_utils.py",
     "name": "URLPattern",
     "line": 9,
     "kind": "from",
     "src": "httpx._utils",
     "src_name": "URLPattern",
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
    "tests/test_utils.py",
    "URLPattern",
    "reexport",
    [
     "httpx._utils",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 2

The test module `tests/test_utils.py` does not define `URLPattern` itself; line 9 imports it from `httpx._utils`.

So far: `tests/test_utils.py` takes `URLPattern` from `httpx._utils`, which I still have to locate.

Let me list `./` to see what lives there; the listing settles whether the import is a module, a package, or not here at all. Very likely the listing fits. If the listing is too long, I will outline `httpx/_utils.py` directly, which both checks that the file exists and shows me `URLPattern`. I could outline `httpx/_utils.py` directly, which both checks that the file exists and shows me `URLPattern` instead, but it costs more calls in expectation.

**Call:** `ls('.')`

**Response**: outcome `complete`

```
.github/
CHANGELOG.md
LICENSE.md
README.md
docs/
httpx/
mkdocs.yml
pyproject.toml
requirements.txt
tests/
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_utils.py",
    "httpx._utils"
   ],
   "desc": "find where `httpx._utils` (imported by `tests/test_utils.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    4699,
    2478
   ],
   "v2": [
    1072615937,
    550070157
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
     "tests/test_utils.py",
     "httpx._utils"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_utils.py', 'URLPattern')",
   "key": "[\"symbols\", [\"httpx/_utils.py\", \"URLPattern\"]]",
   "v1": [
    1690175115,
    733426876
   ],
   "v2": [
    53271711887,
    24203086908
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     92825,
     263978
    ],
    "reexport": [
     1410,
     131989
    ],
    "star": [
     235,
     263978
    ],
    "none": [
     2115,
     131989
    ],
    "missing": [
     1154,
     1859
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_utils.py",
     "httpx._utils"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_utils/__init__.py', 'URLPattern')",
   "key": "[\"symbols\", [\"httpx/_utils/__init__.py\", \"URLPattern\"]]",
   "v1": [
    2217347855,
    734753019
   ],
   "v2": [
    4208222617,
    1469506038
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     140,
     12441
    ],
    "reexport": [
     6860,
     161733
    ],
    "star": [
     140,
     161733
    ],
    "none": [
     1120,
     53911
    ],
    "missing": [
     1719,
     1859
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_utils.py",
     "httpx._utils"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+URLPattern\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+URLPattern\\\\b\", \".\"]]",
   "v1": [
    1265,
    413
   ],
   "v2": [
    7177,
    2478
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
     "tests/test_utils.py",
     "httpx._utils"
    ]
   ]
  }
 ],
 "choice": {
  "call": "ls('.')",
  "key": "[\"ls\", [\".\"]]",
  "provenance": "`httpx._utils` imported by `tests/test_utils.py` should live under `.`",
  "v2": [
   1072615937,
   550070157
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
  "cap": "[\"symbols\", [\"httpx/_utils.py\", \"URLPattern\"]]"
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
    ".github/",
    "CHANGELOG.md",
    "LICENSE.md",
    "README.md",
    "docs/",
    "httpx/",
    "mkdocs.yml",
    "pyproject.toml",
    "requirements.txt",
    "tests/"
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
    "tests/test_utils.py",
    "URLPattern",
    "reexport",
    [
     "httpx._utils",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 3

`./` has 10 entries: `httpx/` is there, so `httpx._utils` is a package.

So far: `tests/test_utils.py` takes `URLPattern` from `httpx._utils`, which I still have to locate.

I'll outline `httpx/_utils.py` directly, which both checks that the file exists and shows me `URLPattern`; if `httpx._utils` is a plain module that is where it has to be. Very likely it is defined right there. If the file does not exist, I will search the whole tree for `class URLPattern`/`def URLPattern`; if the name is not bound there, that finishes it. I could search the whole tree for `class URLPattern`/`def URLPattern` instead, but it tends to open more follow-up work.

**Call:** `symbols('httpx/_utils.py', 'URLPattern')`

**Response**: outcome `def`

```
module httpx/_utils.py lines=243 dynamic=no all=none
120 class URLPattern ()
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_utils.py",
    "httpx._utils"
   ],
   "desc": "find where `httpx._utils` (imported by `tests/test_utils.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/_utils.py', 'URLPattern')",
   "key": "[\"symbols\", [\"httpx/_utils.py\", \"URLPattern\"]]",
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
     "tests/test_utils.py",
     "httpx._utils"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+URLPattern\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+URLPattern\\\\b\", \".\"]]",
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
     "tests/test_utils.py",
     "httpx._utils"
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
     "tests/test_utils.py",
     "httpx._utils"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_utils/__init__.py', 'URLPattern')",
   "key": "[\"symbols\", [\"httpx/_utils/__init__.py\", \"URLPattern\"]]",
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
     "tests/test_utils.py",
     "httpx._utils"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('httpx/_utils.py', 'URLPattern')",
  "key": "[\"symbols\", [\"httpx/_utils.py\", \"URLPattern\"]]",
  "provenance": "`httpx._utils` would be `httpx/_utils.py` if that file exists; one call both checks and closes it",
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
  "missing": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+URLPattern\\\\b\", \".\"]]"
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
   "step": 3,
   "path": "httpx/_utils.py",
   "filter": "URLPattern",
   "header": {
    "lines": 243,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "httpx/_utils.py",
     "name": "URLPattern",
     "line": 120,
     "kind": "class",
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
    "tests/test_utils.py",
    "URLPattern",
    "reexport",
    [
     "httpx._utils",
     "httpx/_utils.py"
    ]
   ],
   [
    "httpx/_utils.py",
    "URLPattern",
    "class",
    120
   ]
  ]
 }
}
```
</details>

## Step 4

There it is: `URLPattern` is a class at `httpx/_utils.py:120`. That settles the definition; now its call sites.

I'll search the whole tree for calls of `URLPattern`; the search has to be complete before I can call the set final. Probably it fits under the cap. If nothing turns up, that finishes it; if it caps, I follow whatever it opens up.

**Call:** `grep('\\bURLPattern\\s*\\(', '.')`

**Response**: outcome `mid`

```
httpx/_client.py:698:            URLPattern(key): None
httpx/_client.py:713:                {URLPattern(key): transport for key, transport in mounts.items()}
httpx/_client.py:1413:            URLPattern(key): None
httpx/_client.py:1428:                {URLPattern(key): transport for key, transport in mounts.items()}
httpx/_utils.py:125:    >>> pattern = URLPattern("all://")
httpx/_utils.py:130:    >>> pattern = URLPattern("https://")
httpx/_utils.py:137:    >>> pattern = URLPattern("https://example.com")
httpx/_utils.py:146:    >>> pattern = URLPattern("all://example.com")
httpx/_utils.py:155:    >>> pattern = URLPattern("https://example.com:1234")
tests/test_utils.py:133:    pattern = URLPattern(pattern)
tests/test_utils.py:139:        URLPattern("all://"),
tests/test_utils.py:140:        URLPattern("http://"),
tests/test_utils.py:141:        URLPattern("http://example.com"),
tests/test_utils.py:142:        URLPattern("http://example.com:123"),
tests/test_utils.py:146:        URLPattern("http://example.com:123"),
tests/test_utils.py:147:        URLPattern("http://example.com"),
tests/test_utils.py:148:        URLPattern("http://"),
tests/test_utils.py:149:        URLPattern("all://"),
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
   "desc": "search `.` for calls of `URLPattern`"
  }
 ],
 "candidates": [
  {
   "call": "grep('\\\\bURLPattern\\\\s*\\\\(', '.')",
   "key": "[\"grep\", [\"\\\\bURLPattern\\\\s*\\\\(\", \".\"]]",
   "v1": [
    283567664673,
    232106594720
   ],
   "v2": [
    283567664673,
    232106594720
   ],
   "p_cap": [
    1,
    40
   ],
   "forecast": {
    "zero": [
     1,
     4
    ],
    "mid": [
     29,
     40
    ],
    "cap": [
     1,
     40
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
  "call": "grep('\\\\bURLPattern\\\\s*\\\\(', '.')",
  "key": "[\"grep\", [\"\\\\bURLPattern\\\\s*\\\\(\", \".\"]]",
  "provenance": "call lines naming `URLPattern` under `.` (derived)",
  "v2": [
   283567664673,
   232106594720
  ]
 },
 "forecast": {
  "zero": [
   1,
   4
  ],
  "mid": [
   29,
   40
  ],
  "cap": [
   1,
   40
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
    29,
    40
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
   "pattern": "\\bURLPattern\\s*\\(",
   "scope": ".",
   "hits": [
    [
     "httpx/_client.py",
     698
    ],
    [
     "httpx/_client.py",
     713
    ],
    [
     "httpx/_client.py",
     1413
    ],
    [
     "httpx/_client.py",
     1428
    ],
    [
     "httpx/_utils.py",
     125
    ],
    [
     "httpx/_utils.py",
     130
    ],
    [
     "httpx/_utils.py",
     137
    ],
    [
     "httpx/_utils.py",
     146
    ],
    [
     "httpx/_utils.py",
     155
    ],
    [
     "tests/test_utils.py",
     133
    ],
    [
     "tests/test_utils.py",
     139
    ],
    [
     "tests/test_utils.py",
     140
    ],
    [
     "tests/test_utils.py",
     141
    ],
    [
     "tests/test_utils.py",
     142
    ],
    [
     "tests/test_utils.py",
     146
    ],
    [
     "tests/test_utils.py",
     147
    ],
    [
     "tests/test_utils.py",
     148
    ],
    [
     "tests/test_utils.py",
     149
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
   "httpx/_client.py",
   "httpx/_utils.py",
   "tests/test_utils.py"
  ],
  "table": [
   [
    "httpx/_client.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "httpx/_utils.py",
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
   "CALL": []
  },
  "n_in": 0,
  "n_out": 0,
  "n_pending": 3
 }
}
```
</details>

## Step 5

18 matching lines anywhere for calls of `URLPattern`, in `httpx/_client.py`, `httpx/_utils.py`, `tests/test_utils.py`, and the search was under the cap, so that is the complete set there.

Let me list the call sites of `URLPattern` in `httpx/_utils.py`; the name is ours there, so each call site counts. Almost certainly the call sites fit. If there are too many call sites, I will look at `httpx/_client.py`'s top-level names for `URLPattern`.

**Call:** `calls('httpx/_utils.py', 'URLPattern')`

**Response**: outcome `ok`

```
calls of URLPattern in httpx/_utils.py count=0
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_client.py",
    "URLPattern"
   ],
   "desc": "check what `URLPattern` means inside `httpx/_client.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "httpx/_utils.py",
    "URLPattern"
   ],
   "desc": "list the call sites of `URLPattern` in `httpx/_utils.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "tests/test_utils.py",
    "URLPattern"
   ],
   "desc": "list the call sites of `URLPattern` in `tests/test_utils.py`"
  }
 ],
 "candidates": [
  {
   "call": "calls('httpx/_utils.py', 'URLPattern')",
   "key": "[\"calls\", [\"httpx/_utils.py\", \"URLPattern\"]]",
   "v1": [
    9621287,
    2634940
   ],
   "v2": [
    48369929,
    13174700
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
     "httpx/_utils.py",
     "URLPattern"
    ]
   ]
  },
  {
   "call": "calls('tests/test_utils.py', 'URLPattern')",
   "key": "[\"calls\", [\"tests/test_utils.py\", \"URLPattern\"]]",
   "v1": [
    9621287,
    2634940
   ],
   "v2": [
    48369929,
    13174700
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
     "tests/test_utils.py",
     "URLPattern"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_client.py', 'URLPattern')",
   "key": "[\"symbols\", [\"httpx/_client.py\", \"URLPattern\"]]",
   "v1": [
    23855597,
    6587350
   ],
   "v2": [
    48369929,
    13174700
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
     "httpx/_client.py",
     "URLPattern"
    ]
   ]
  }
 ],
 "choice": {
  "call": "calls('httpx/_utils.py', 'URLPattern')",
  "key": "[\"calls\", [\"httpx/_utils.py\", \"URLPattern\"]]",
  "provenance": "call sites of `URLPattern` in `httpx/_utils.py` that refer to the module-level binding",
  "v2": [
   48369929,
   13174700
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
  "ok": "[\"symbols\", [\"httpx/_client.py\", \"URLPattern\"]]",
  "cap": "[\"symbols\", [\"httpx/_client.py\", \"URLPattern\"]]"
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
   "path": "httpx/_utils.py",
   "name": "URLPattern",
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
   "httpx/_client.py",
   "httpx/_utils.py",
   "tests/test_utils.py"
  ],
  "table": [
   [
    "httpx/_client.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "httpx/_utils.py",
    "httpx/_utils.py",
    "out",
    "the module binds the name but never calls it by bare name"
   ],
   [
    "tests/test_utils.py",
    null,
    "pending",
    "not yet examined"
   ]
  ],
  "uncovered": {
   "CALL": []
  },
  "n_in": 0,
  "n_out": 1,
  "n_pending": 2
 }
}
```
</details>

## Step 6

`httpx/_utils.py` binds `URLPattern` but never actually calls it by that name.

Tally: 0 call sites confirmed, 1 ruled out, 2 pending. The search itself is complete; what is left is checking the candidates.

Next I will look at `httpx/_client.py`'s top-level names for `URLPattern`; before counting calls I need to know the name refers to our definition there. Almost certainly the outline shows what I need. If the outline is too long to fit, I will list the call sites of `URLPattern` in `tests/test_utils.py`.

**Call:** `symbols('httpx/_client.py', 'URLPattern')`

**Response**: outcome `ok`

```
module httpx/_client.py lines=2020 dynamic=no all=static@54
49 from URLPattern <- ._utils URLPattern
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_client.py",
    "URLPattern"
   ],
   "desc": "check what `URLPattern` means inside `httpx/_client.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "tests/test_utils.py",
    "URLPattern"
   ],
   "desc": "list the call sites of `URLPattern` in `tests/test_utils.py`"
  }
 ],
 "candidates": [
  {
   "call": "calls('tests/test_utils.py', 'URLPattern')",
   "key": "[\"calls\", [\"tests/test_utils.py\", \"URLPattern\"]]",
   "v1": [
    6986347,
    2634940
   ],
   "v2": [
    35195229,
    13174700
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
     "tests/test_utils.py",
     "URLPattern"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_client.py', 'URLPattern')",
   "key": "[\"symbols\", [\"httpx/_client.py\", \"URLPattern\"]]",
   "v1": [
    17268247,
    6587350
   ],
   "v2": [
    35195229,
    13174700
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
     "httpx/_client.py",
     "URLPattern"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('httpx/_client.py', 'URLPattern')",
  "key": "[\"symbols\", [\"httpx/_client.py\", \"URLPattern\"]]",
  "provenance": "`httpx/_client.py` had a matching line (step 4); its outline names every `URLPattern` import exactly",
  "v2": [
   35195229,
   13174700
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
  "ok": "[\"calls\", [\"tests/test_utils.py\", \"URLPattern\"]]",
  "cap": "[\"calls\", [\"tests/test_utils.py\", \"URLPattern\"]]"
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
  "planned": "[\"symbols\", [\"httpx/_client.py\", \"URLPattern\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 6,
   "path": "httpx/_client.py",
   "filter": "URLPattern",
   "header": {
    "lines": 2020,
    "dynamic": false,
    "all_status": "static",
    "all_line": 54
   },
   "bindings": [
    {
     "module": "httpx/_client.py",
     "name": "URLPattern",
     "line": 49,
     "kind": "from",
     "src": "._utils",
     "src_name": "URLPattern",
     "conditional": false,
     "col": 0,
     "bases": []
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "callers",
  "step": 2,
  "of": 2,
  "candidates": [
   "httpx/_client.py",
   "httpx/_utils.py",
   "tests/test_utils.py"
  ],
  "table": [
   [
    "httpx/_client.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "httpx/_utils.py",
    "httpx/_utils.py",
    "out",
    "the module binds the name but never calls it by bare name"
   ],
   [
    "tests/test_utils.py",
    null,
    "pending",
    "not yet examined"
   ]
  ],
  "uncovered": {
   "CALL": []
  },
  "n_in": 0,
  "n_out": 1,
  "n_pending": 2
 }
}
```
</details>

## Step 7

`httpx/_client.py` does not define `URLPattern` itself; line 49 imports it from `._utils`.

Tally: 0 call sites confirmed, 1 ruled out, 2 pending. The search itself is complete; what is left is checking the candidates.

Next I will list the call sites of `URLPattern` in `tests/test_utils.py`; the name is ours there, so each call site counts. Almost certainly the call sites fit. If there are too many call sites, I will list the call sites of `URLPattern` in `httpx/_client.py`.

**Call:** `calls('tests/test_utils.py', 'URLPattern')`

**Response**: outcome `ok`

```
calls of URLPattern in tests/test_utils.py count=9
133:    pattern = URLPattern(pattern)
139:        URLPattern("all://"),
140:        URLPattern("http://"),
141:        URLPattern("http://example.com"),
142:        URLPattern("http://example.com:123"),
146:        URLPattern("http://example.com:123"),
147:        URLPattern("http://example.com"),
148:        URLPattern("http://"),
149:        URLPattern("all://"),
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "calls",
   "key": [
    "calls",
    "httpx/_client.py",
    "URLPattern"
   ],
   "desc": "list the call sites of `URLPattern` in `httpx/_client.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "tests/test_utils.py",
    "URLPattern"
   ],
   "desc": "list the call sites of `URLPattern` in `tests/test_utils.py`"
  }
 ],
 "candidates": [
  {
   "call": "calls('httpx/_client.py', 'URLPattern')",
   "key": "[\"calls\", [\"httpx/_client.py\", \"URLPattern\"]]",
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
     "httpx/_client.py",
     "URLPattern"
    ]
   ]
  },
  {
   "call": "calls('tests/test_utils.py', 'URLPattern')",
   "key": "[\"calls\", [\"tests/test_utils.py\", \"URLPattern\"]]",
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
     "tests/test_utils.py",
     "URLPattern"
    ]
   ]
  }
 ],
 "choice": {
  "call": "calls('tests/test_utils.py', 'URLPattern')",
  "key": "[\"calls\", [\"tests/test_utils.py\", \"URLPattern\"]]",
  "provenance": "call sites of `URLPattern` in `tests/test_utils.py` that refer to the module-level binding",
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
  "ok": "[\"calls\", [\"httpx/_client.py\", \"URLPattern\"]]",
  "cap": "[\"calls\", [\"httpx/_client.py\", \"URLPattern\"]]"
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
  "planned": "[\"calls\", [\"tests/test_utils.py\", \"URLPattern\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "calls",
   "step": 7,
   "path": "tests/test_utils.py",
   "name": "URLPattern",
   "lines": [
    133,
    139,
    140,
    141,
    142,
    146,
    147,
    148,
    149
   ],
   "count": 9,
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "callers",
  "step": 2,
  "of": 2,
  "candidates": [
   "httpx/_client.py",
   "httpx/_utils.py",
   "tests/test_utils.py"
  ],
  "table": [
   [
    "httpx/_client.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "httpx/_utils.py",
    "httpx/_utils.py",
    "out",
    "the module binds the name but never calls it by bare name"
   ],
   [
    "tests/test_utils.py",
    "tests/test_utils.py:133",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "tests/test_utils.py",
    "tests/test_utils.py:139",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "tests/test_utils.py",
    "tests/test_utils.py:140",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "tests/test_utils.py",
    "tests/test_utils.py:141",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "tests/test_utils.py",
    "tests/test_utils.py:142",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "tests/test_utils.py",
    "tests/test_utils.py:146",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "tests/test_utils.py",
    "tests/test_utils.py:147",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "tests/test_utils.py",
    "tests/test_utils.py:148",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "tests/test_utils.py",
    "tests/test_utils.py:149",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ]
  ],
  "uncovered": {
   "CALL": []
  },
  "n_in": 9,
  "n_out": 1,
  "n_pending": 1
 }
}
```
</details>

## Step 8

`tests/test_utils.py` calls `URLPattern` at lines 133, 139, 140, 141, 142, 146 and 3 more, and those are real calls of the module-level name, not a shadowed local.

Tally: 9 call sites confirmed, 1 ruled out, 1 pending. The search itself is complete; what is left is checking the candidates.

I'll list the call sites of `URLPattern` in `httpx/_client.py`; the name is ours there, so each call site counts. Almost certainly the call sites fit. If there are too many call sites, I follow whatever it opens up.

**Call:** `calls('httpx/_client.py', 'URLPattern')`

**Response**: outcome `ok`

```
calls of URLPattern in httpx/_client.py count=4
698:            URLPattern(key): None
713:                {URLPattern(key): transport for key, transport in mounts.items()}
1413:            URLPattern(key): None
1428:                {URLPattern(key): transport for key, transport in mounts.items()}
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "calls",
   "key": [
    "calls",
    "httpx/_client.py",
    "URLPattern"
   ],
   "desc": "list the call sites of `URLPattern` in `httpx/_client.py`"
  }
 ],
 "candidates": [
  {
   "call": "calls('httpx/_client.py', 'URLPattern')",
   "key": "[\"calls\", [\"httpx/_client.py\", \"URLPattern\"]]",
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
     "httpx/_client.py",
     "URLPattern"
    ]
   ]
  }
 ],
 "choice": {
  "call": "calls('httpx/_client.py', 'URLPattern')",
  "key": "[\"calls\", [\"httpx/_client.py\", \"URLPattern\"]]",
  "provenance": "call sites of `URLPattern` in `httpx/_client.py` that refer to the module-level binding",
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
  "planned": "[\"calls\", [\"httpx/_client.py\", \"URLPattern\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "calls",
   "step": 8,
   "path": "httpx/_client.py",
   "name": "URLPattern",
   "lines": [
    698,
    713,
    1413,
    1428
   ],
   "count": 4,
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "callers",
  "step": 2,
  "of": 2,
  "candidates": [
   "httpx/_client.py",
   "httpx/_utils.py",
   "tests/test_utils.py"
  ],
  "table": [
   [
    "httpx/_client.py",
    "httpx/_client.py:698",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "httpx/_client.py",
    "httpx/_client.py:713",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "httpx/_client.py",
    "httpx/_client.py:1413",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "httpx/_client.py",
    "httpx/_client.py:1428",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "httpx/_utils.py",
    "httpx/_utils.py",
    "out",
    "the module binds the name but never calls it by bare name"
   ],
   [
    "tests/test_utils.py",
    "tests/test_utils.py:133",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "tests/test_utils.py",
    "tests/test_utils.py:139",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "tests/test_utils.py",
    "tests/test_utils.py:140",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "tests/test_utils.py",
    "tests/test_utils.py:141",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "tests/test_utils.py",
    "tests/test_utils.py:142",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "tests/test_utils.py",
    "tests/test_utils.py:146",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "tests/test_utils.py",
    "tests/test_utils.py:147",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "tests/test_utils.py",
    "tests/test_utils.py:148",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "tests/test_utils.py",
    "tests/test_utils.py:149",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ]
  ],
  "uncovered": {
   "CALL": []
  },
  "n_in": 13,
  "n_out": 1,
  "n_pending": 0
 }
}
```
</details>

## Final

`URLPattern` is the class at `httpx/_utils.py:120`. 13 call sites in 2 modules: `httpx/_client.py:698`, `httpx/_client.py:713`, `httpx/_client.py:1413`, `httpx/_client.py:1428`, `tests/test_utils.py:133`, `tests/test_utils.py:139`, `tests/test_utils.py:140`, `tests/test_utils.py:141`, `tests/test_utils.py:142`, `tests/test_utils.py:146` and 3 more. Ruled out along the way: `httpx/_utils.py` (the module binds the name but never calls it by bare name). Looking back, 1 of 8 calls did not end up mattering (step 2).

**Answer:** `{"final_kind": "callers", "final": ["httpx/_client.py:698", "httpx/_client.py:713", "httpx/_client.py:1413", "httpx/_client.py:1428", "tests/test_utils.py:133", "tests/test_utils.py:139", "tests/test_utils.py:140", "tests/test_utils.py:141", "tests/test_utils.py:142", "tests/test_utils.py:146", "tests/test_utils.py:147", "tests/test_utils.py:148", "tests/test_utils.py:149"], "steps": [{"op": "resolve", "output": {"kind": "def", "path": "httpx/_utils.py", "line": 120, "name": "URLPattern", "detail": "class"}}, {"op": "callers", "output": ["httpx/_client.py:698", "httpx/_client.py:713", "httpx/_client.py:1413", "httpx/_client.py:1428", "tests/test_utils.py:133", "tests/test_utils.py:139", "tests/test_utils.py:140", "tests/test_utils.py:141", "tests/test_utils.py:142", "tests/test_utils.py:146", "tests/test_utils.py:147", "tests/test_utils.py:148", "tests/test_utils.py:149"]}], "stuck": null}`  
**Stopped:** certificate after 8 calls