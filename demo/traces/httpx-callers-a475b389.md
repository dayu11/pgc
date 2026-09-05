# httpx-callers-a475b389

**Repository:** httpx  
**Chain:** resolve → callers  
**Seed:** 0, prior 708591d2904e1ac3, floor 11

## Task

In `httpx/_auth.py` line 12, `Cookies` is imported from `._models`. Which definition does the module-level name `Cookies` actually refer to? Give `path:line`. Then list every call site of it: bare-name calls whose module-level binding resolves to this definition, as `path:line`.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N; bindings take effect in source order. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. A class derives from a definition when a base written as a bare name or `module.Name` resolves to it. A call site is `name(...)` where the bare name refers to the module-level binding (not a parameter or local). Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

I need to find what `Cookies` really is in `httpx/_auth.py`: line 12 imports it from `._models`, so the definition is at least one hop away. Then every real call site of it, which means checking what the name refers to in each file that mentions it.

Next I will check `httpx/_auth.py` for any other binding of `Cookies` besides the import on line 12; almost certainly the import is the only one, and then `._models` is the place to follow.

**Call:** `symbols('httpx/_auth.py', 'Cookies')`

**Response**: outcome `reexport`

```
module httpx/_auth.py lines=349 dynamic=no all=static@19
12 from Cookies <- ._models Cookies
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "httpx/_auth.py",
    "Cookies"
   ],
   "desc": "check the top-level names of `httpx/_auth.py` for `Cookies`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/_auth.py', 'Cookies')",
   "key": "[\"symbols\", [\"httpx/_auth.py\", \"Cookies\"]]",
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
     "httpx/_auth.py",
     "Cookies"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_auth.py')",
   "key": "[\"symbols\", [\"httpx/_auth.py\"]]",
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
     "httpx/_auth.py",
     "Cookies"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('httpx/_auth.py', 'Cookies')",
  "key": "[\"symbols\", [\"httpx/_auth.py\", \"Cookies\"]]",
  "provenance": "module `httpx/_auth.py` (task), name `Cookies` (task)",
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
   "path": "httpx/_auth.py",
   "filter": "Cookies",
   "header": {
    "lines": 349,
    "dynamic": false,
    "all_status": "static",
    "all_line": 19
   },
   "bindings": [
    {
     "module": "httpx/_auth.py",
     "name": "Cookies",
     "line": 12,
     "kind": "from",
     "src": "._models",
     "src_name": "Cookies",
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
    "httpx/_auth.py",
    "Cookies",
    "reexport",
    [
     "._models",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 2

`httpx/_auth.py` does not define `Cookies` itself; line 12 imports it from `._models`.

So far: `httpx/_auth.py` takes `Cookies` from `._models`, which I still have to locate.

Let me outline `httpx/_models.py` directly, which both checks that the file exists and shows me `Cookies`; if `._models` is a plain module that is where it has to be. Very likely it is defined right there. If the file does not exist, I will search the whole tree for `class Cookies`/`def Cookies`; if the name is not bound there, that finishes it. I could search the whole tree for `class Cookies`/`def Cookies` instead, but it tends to open more follow-up work.

**Call:** `symbols('httpx/_models.py', 'Cookies')`

**Response**: outcome `def`

```
module httpx/_models.py lines=1278 dynamic=no all=static@51
1079 class Cookies (?)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/_auth.py",
    "._models"
   ],
   "desc": "find where `._models` (imported by `httpx/_auth.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/_models.py', 'Cookies')",
   "key": "[\"symbols\", [\"httpx/_models.py\", \"Cookies\"]]",
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
     "httpx/_auth.py",
     "._models"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+Cookies\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+Cookies\\\\b\", \".\"]]",
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
     "httpx/_auth.py",
     "._models"
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
     "httpx/_auth.py",
     "._models"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_models/__init__.py', 'Cookies')",
   "key": "[\"symbols\", [\"httpx/_models/__init__.py\", \"Cookies\"]]",
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
     "httpx/_auth.py",
     "._models"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('httpx/_models.py', 'Cookies')",
  "key": "[\"symbols\", [\"httpx/_models.py\", \"Cookies\"]]",
  "provenance": "`._models` would be `httpx/_models.py` if that file exists; one call both checks and closes it",
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
  "missing": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+Cookies\\\\b\", \".\"]]"
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
   "path": "httpx/_models.py",
   "filter": "Cookies",
   "header": {
    "lines": 1278,
    "dynamic": false,
    "all_status": "static",
    "all_line": 51
   },
   "bindings": [
    {
     "module": "httpx/_models.py",
     "name": "Cookies",
     "line": 1079,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
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
    "httpx/_auth.py",
    "Cookies",
    "reexport",
    [
     "._models",
     "httpx/_models.py"
    ]
   ],
   [
    "httpx/_models.py",
    "Cookies",
    "class",
    1079
   ]
  ]
 }
}
```
</details>

## Step 3

There it is: `Cookies` is a class at `httpx/_models.py:1079`. That settles the definition; now its call sites.

I'll search the whole tree for calls of `Cookies`; the search has to be complete before I can call the set final. Probably it fits under the cap. If nothing turns up, that finishes it; if it caps, I follow whatever it opens up.

**Call:** `grep('\\bCookies\\s*\\(', '.')`

**Response**: outcome `mid`

```
docs/api.md:149:>>> cookies = Cookies()
docs/quickstart.md:410:>>> cookies = httpx.Cookies()
httpx/_auth.py:221:            Cookies(response.cookies).set_cookie_header(request=request)
httpx/_client.py:211:        self._cookies = Cookies(cookies)
httpx/_client.py:327:        self._cookies = Cookies(cookies)
httpx/_client.py:419:            merged_cookies = Cookies(self.cookies)
httpx/_client.py:484:        cookies = Cookies(self.cookies)
httpx/_models.py:404:            Cookies(cookies).set_cookie_header(self)
httpx/_models.py:837:            self._cookies = Cookies()
httpx/_models.py:1079:class Cookies(typing.MutableMapping[str, str]):
httpx/_models.py:1206:        cookies = Cookies(cookies)
tests/client/test_cookies.py:129:    cookies = httpx.Cookies()
tests/models/test_cookies.py:9:    cookies = httpx.Cookies({"name": "value"})
tests/models/test_cookies.py:24:    cookies = httpx.Cookies()
tests/models/test_cookies.py:25:    more_cookies = httpx.Cookies()
tests/models/test_cookies.py:34:    cookies = httpx.Cookies()
tests/models/test_cookies.py:46:    cookies = httpx.Cookies()
tests/models/test_cookies.py:74:    cookies = httpx.Cookies(jar)
tests/models/test_cookies.py:83:    cookies = httpx.Cookies(cookies_val)
tests/models/test_cookies.py:91:    cookies = httpx.Cookies()
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
   "desc": "search `.` for calls of `Cookies`"
  }
 ],
 "candidates": [
  {
   "call": "grep('\\\\bCookies\\\\s*\\\\(', '.')",
   "key": "[\"grep\", [\"\\\\bCookies\\\\s*\\\\(\", \".\"]]",
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
  "call": "grep('\\\\bCookies\\\\s*\\\\(', '.')",
  "key": "[\"grep\", [\"\\\\bCookies\\\\s*\\\\(\", \".\"]]",
  "provenance": "call lines naming `Cookies` under `.` (derived)",
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
   "step": 3,
   "pattern": "\\bCookies\\s*\\(",
   "scope": ".",
   "hits": [
    [
     "docs/api.md",
     149
    ],
    [
     "docs/quickstart.md",
     410
    ],
    [
     "httpx/_auth.py",
     221
    ],
    [
     "httpx/_client.py",
     211
    ],
    [
     "httpx/_client.py",
     327
    ],
    [
     "httpx/_client.py",
     419
    ],
    [
     "httpx/_client.py",
     484
    ],
    [
     "httpx/_models.py",
     404
    ],
    [
     "httpx/_models.py",
     837
    ],
    [
     "httpx/_models.py",
     1079
    ],
    [
     "httpx/_models.py",
     1206
    ],
    [
     "tests/client/test_cookies.py",
     129
    ],
    [
     "tests/models/test_cookies.py",
     9
    ],
    [
     "tests/models/test_cookies.py",
     24
    ],
    [
     "tests/models/test_cookies.py",
     25
    ],
    [
     "tests/models/test_cookies.py",
     34
    ],
    [
     "tests/models/test_cookies.py",
     46
    ],
    [
     "tests/models/test_cookies.py",
     74
    ],
    [
     "tests/models/test_cookies.py",
     83
    ],
    [
     "tests/models/test_cookies.py",
     91
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
   "httpx/_auth.py",
   "httpx/_client.py",
   "httpx/_models.py",
   "tests/client/test_cookies.py",
   "tests/models/test_cookies.py"
  ],
  "table": [
   [
    "httpx/_auth.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "httpx/_client.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "httpx/_models.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/client/test_cookies.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/models/test_cookies.py",
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
  "n_pending": 5
 }
}
```
</details>

## Step 4

20 matching lines anywhere for calls of `Cookies`, in `docs/api.md`, `docs/quickstart.md`, `httpx/_auth.py`, `httpx/_client.py` and 3 more files, and the search was under the cap, so that is the complete set there.

Still open: list the call sites of `Cookies` in `httpx/_auth.py`; check what `Cookies` means inside `httpx/_client.py`; list the call sites of `Cookies` in `httpx/_models.py`; and 2 more.

I'll look at `httpx/_client.py`'s top-level names for `Cookies`; before counting calls I need to know the name refers to our definition there. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `tests/client/test_cookies.py`'s top-level names for `Cookies`.

**Call:** `symbols('httpx/_client.py', 'Cookies')`

**Response**: outcome `ok`

```
module httpx/_client.py lines=2020 dynamic=no all=static@54
29 from Cookies <- ._models Cookies
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "calls",
   "key": [
    "calls",
    "httpx/_auth.py",
    "Cookies"
   ],
   "desc": "list the call sites of `Cookies` in `httpx/_auth.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_client.py",
    "Cookies"
   ],
   "desc": "check what `Cookies` means inside `httpx/_client.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "httpx/_models.py",
    "Cookies"
   ],
   "desc": "list the call sites of `Cookies` in `httpx/_models.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/client/test_cookies.py",
    "Cookies"
   ],
   "desc": "check what `Cookies` means inside `tests/client/test_cookies.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/models/test_cookies.py",
    "Cookies"
   ],
   "desc": "check what `Cookies` means inside `tests/models/test_cookies.py`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/_client.py', 'Cookies')",
   "key": "[\"symbols\", [\"httpx/_client.py\", \"Cookies\"]]",
   "v1": [
    44953897,
    6587350
   ],
   "v2": [
    22542822,
    3293675
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
     "Cookies"
    ]
   ]
  },
  {
   "call": "symbols('tests/client/test_cookies.py', 'Cookies')",
   "key": "[\"symbols\", [\"tests/client/test_cookies.py\", \"Cookies\"]]",
   "v1": [
    44953897,
    6587350
   ],
   "v2": [
    22542822,
    3293675
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
     "tests/client/test_cookies.py",
     "Cookies"
    ]
   ]
  },
  {
   "call": "symbols('tests/models/test_cookies.py', 'Cookies')",
   "key": "[\"symbols\", [\"tests/models/test_cookies.py\", \"Cookies\"]]",
   "v1": [
    44953897,
    6587350
   ],
   "v2": [
    22542822,
    3293675
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
     "tests/models/test_cookies.py",
     "Cookies"
    ]
   ]
  },
  {
   "call": "calls('httpx/_auth.py', 'Cookies')",
   "key": "[\"calls\", [\"httpx/_auth.py\", \"Cookies\"]]",
   "v1": [
    18060607,
    2634940
   ],
   "v2": [
    90566529,
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
     "httpx/_auth.py",
     "Cookies"
    ]
   ]
  },
  {
   "call": "calls('httpx/_models.py', 'Cookies')",
   "key": "[\"calls\", [\"httpx/_models.py\", \"Cookies\"]]",
   "v1": [
    18060607,
    2634940
   ],
   "v2": [
    90566529,
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
     "httpx/_models.py",
     "Cookies"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('httpx/_client.py', 'Cookies')",
  "key": "[\"symbols\", [\"httpx/_client.py\", \"Cookies\"]]",
  "provenance": "`httpx/_client.py` had a matching line (step 3); its outline names every `Cookies` import exactly",
  "v2": [
   22542822,
   3293675
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
  "ok": "[\"symbols\", [\"tests/client/test_cookies.py\", \"Cookies\"]]",
  "cap": "[\"symbols\", [\"tests/client/test_cookies.py\", \"Cookies\"]]"
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
   "path": "httpx/_client.py",
   "filter": "Cookies",
   "header": {
    "lines": 2020,
    "dynamic": false,
    "all_status": "static",
    "all_line": 54
   },
   "bindings": [
    {
     "module": "httpx/_client.py",
     "name": "Cookies",
     "line": 29,
     "kind": "from",
     "src": "._models",
     "src_name": "Cookies",
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
   "httpx/_auth.py",
   "httpx/_client.py",
   "httpx/_models.py",
   "tests/client/test_cookies.py",
   "tests/models/test_cookies.py"
  ],
  "table": [
   [
    "httpx/_auth.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "httpx/_client.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "httpx/_models.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/client/test_cookies.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/models/test_cookies.py",
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
  "n_pending": 5
 }
}
```
</details>

## Step 5

`httpx/_client.py` does not define `Cookies` itself; line 29 imports it from `._models`.

Tally: 0 call sites confirmed, 0 ruled out, 5 pending. The search itself is complete; what is left is checking the candidates.

Let me look at `tests/client/test_cookies.py`'s top-level names for `Cookies`; before counting calls I need to know the name refers to our definition there. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `tests/models/test_cookies.py`'s top-level names for `Cookies`.

**Call:** `symbols('tests/client/test_cookies.py', 'Cookies')`

**Response**: outcome `ok`

```
module tests/client/test_cookies.py lines=169 dynamic=no all=none
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "calls",
   "key": [
    "calls",
    "httpx/_auth.py",
    "Cookies"
   ],
   "desc": "list the call sites of `Cookies` in `httpx/_auth.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "httpx/_client.py",
    "Cookies"
   ],
   "desc": "list the call sites of `Cookies` in `httpx/_client.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "httpx/_models.py",
    "Cookies"
   ],
   "desc": "list the call sites of `Cookies` in `httpx/_models.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/client/test_cookies.py",
    "Cookies"
   ],
   "desc": "check what `Cookies` means inside `tests/client/test_cookies.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/models/test_cookies.py",
    "Cookies"
   ],
   "desc": "check what `Cookies` means inside `tests/models/test_cookies.py`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/client/test_cookies.py', 'Cookies')",
   "key": "[\"symbols\", [\"tests/client/test_cookies.py\", \"Cookies\"]]",
   "v1": [
    40992097,
    6587350
   ],
   "v2": [
    20561922,
    3293675
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
     "tests/client/test_cookies.py",
     "Cookies"
    ]
   ]
  },
  {
   "call": "symbols('tests/models/test_cookies.py', 'Cookies')",
   "key": "[\"symbols\", [\"tests/models/test_cookies.py\", \"Cookies\"]]",
   "v1": [
    40992097,
    6587350
   ],
   "v2": [
    20561922,
    3293675
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
     "tests/models/test_cookies.py",
     "Cookies"
    ]
   ]
  },
  {
   "call": "calls('httpx/_auth.py', 'Cookies')",
   "key": "[\"calls\", [\"httpx/_auth.py\", \"Cookies\"]]",
   "v1": [
    16475887,
    2634940
   ],
   "v2": [
    82642929,
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
     "httpx/_auth.py",
     "Cookies"
    ]
   ]
  },
  {
   "call": "calls('httpx/_client.py', 'Cookies')",
   "key": "[\"calls\", [\"httpx/_client.py\", \"Cookies\"]]",
   "v1": [
    16475887,
    2634940
   ],
   "v2": [
    82642929,
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
     "httpx/_client.py",
     "Cookies"
    ]
   ]
  },
  {
   "call": "calls('httpx/_models.py', 'Cookies')",
   "key": "[\"calls\", [\"httpx/_models.py\", \"Cookies\"]]",
   "v1": [
    16475887,
    2634940
   ],
   "v2": [
    82642929,
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
     "httpx/_models.py",
     "Cookies"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/client/test_cookies.py', 'Cookies')",
  "key": "[\"symbols\", [\"tests/client/test_cookies.py\", \"Cookies\"]]",
  "provenance": "`tests/client/test_cookies.py` had a matching line (step 3); its outline names every `Cookies` import exactly",
  "v2": [
   20561922,
   3293675
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
  "ok": "[\"symbols\", [\"tests/models/test_cookies.py\", \"Cookies\"]]",
  "cap": "[\"symbols\", [\"tests/models/test_cookies.py\", \"Cookies\"]]"
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
  "planned": "[\"symbols\", [\"tests/client/test_cookies.py\", \"Cookies\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 5,
   "path": "tests/client/test_cookies.py",
   "filter": "Cookies",
   "header": {
    "lines": 169,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "callers",
  "step": 2,
  "of": 2,
  "candidates": [
   "httpx/_auth.py",
   "httpx/_client.py",
   "httpx/_models.py",
   "tests/client/test_cookies.py",
   "tests/models/test_cookies.py"
  ],
  "table": [
   [
    "httpx/_auth.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "httpx/_client.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "httpx/_models.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/client/test_cookies.py",
    "tests/client/test_cookies.py",
    "out",
    "the name is not bound at module level here"
   ],
   [
    "tests/models/test_cookies.py",
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
  "n_pending": 4
 }
}
```
</details>

## Step 6

The test module `tests/client/test_cookies.py` does not bind `Cookies` at module level at all, so its matches were false positives.

Tally: 0 call sites confirmed, 1 ruled out, 4 pending. The search itself is complete; what is left is checking the candidates.

Next I will look at `tests/models/test_cookies.py`'s top-level names for `Cookies`; before counting calls I need to know the name refers to our definition there. Almost certainly the outline shows what I need. If the outline is too long to fit, I will list the call sites of `Cookies` in `httpx/_auth.py`.

**Call:** `symbols('tests/models/test_cookies.py', 'Cookies')`

**Response**: outcome `ok`

```
module tests/models/test_cookies.py lines=99 dynamic=no all=none
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "calls",
   "key": [
    "calls",
    "httpx/_auth.py",
    "Cookies"
   ],
   "desc": "list the call sites of `Cookies` in `httpx/_auth.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "httpx/_client.py",
    "Cookies"
   ],
   "desc": "list the call sites of `Cookies` in `httpx/_client.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "httpx/_models.py",
    "Cookies"
   ],
   "desc": "list the call sites of `Cookies` in `httpx/_models.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/models/test_cookies.py",
    "Cookies"
   ],
   "desc": "check what `Cookies` means inside `tests/models/test_cookies.py`"
  }
 ],
 "candidates": [
  {
   "call": "calls('httpx/_auth.py', 'Cookies')",
   "key": "[\"calls\", [\"httpx/_auth.py\", \"Cookies\"]]",
   "v1": [
    12256227,
    2634940
   ],
   "v2": [
    61544629,
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
     "httpx/_auth.py",
     "Cookies"
    ]
   ]
  },
  {
   "call": "calls('httpx/_client.py', 'Cookies')",
   "key": "[\"calls\", [\"httpx/_client.py\", \"Cookies\"]]",
   "v1": [
    12256227,
    2634940
   ],
   "v2": [
    61544629,
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
     "httpx/_client.py",
     "Cookies"
    ]
   ]
  },
  {
   "call": "calls('httpx/_models.py', 'Cookies')",
   "key": "[\"calls\", [\"httpx/_models.py\", \"Cookies\"]]",
   "v1": [
    12256227,
    2634940
   ],
   "v2": [
    61544629,
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
     "httpx/_models.py",
     "Cookies"
    ]
   ]
  },
  {
   "call": "symbols('tests/models/test_cookies.py', 'Cookies')",
   "key": "[\"symbols\", [\"tests/models/test_cookies.py\", \"Cookies\"]]",
   "v1": [
    30442947,
    6587350
   ],
   "v2": [
    61544629,
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
     "tests/models/test_cookies.py",
     "Cookies"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/models/test_cookies.py', 'Cookies')",
  "key": "[\"symbols\", [\"tests/models/test_cookies.py\", \"Cookies\"]]",
  "provenance": "`tests/models/test_cookies.py` had a matching line (step 3); its outline names every `Cookies` import exactly",
  "v2": [
   61544629,
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
  "ok": "[\"calls\", [\"httpx/_auth.py\", \"Cookies\"]]",
  "cap": "[\"calls\", [\"httpx/_auth.py\", \"Cookies\"]]"
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
  "planned": "[\"symbols\", [\"tests/models/test_cookies.py\", \"Cookies\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 6,
   "path": "tests/models/test_cookies.py",
   "filter": "Cookies",
   "header": {
    "lines": 99,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "callers",
  "step": 2,
  "of": 2,
  "candidates": [
   "httpx/_auth.py",
   "httpx/_client.py",
   "httpx/_models.py",
   "tests/client/test_cookies.py",
   "tests/models/test_cookies.py"
  ],
  "table": [
   [
    "httpx/_auth.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "httpx/_client.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "httpx/_models.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/client/test_cookies.py",
    "tests/client/test_cookies.py",
    "out",
    "the name is not bound at module level here"
   ],
   [
    "tests/models/test_cookies.py",
    "tests/models/test_cookies.py",
    "out",
    "the name is not bound at module level here"
   ]
  ],
  "uncovered": {
   "CALL": []
  },
  "n_in": 0,
  "n_out": 2,
  "n_pending": 3
 }
}
```
</details>

## Step 7

The test module `tests/models/test_cookies.py` does not bind `Cookies` at module level at all, so its matches were false positives.

Tally: 0 call sites confirmed, 2 ruled out, 3 pending. The search itself is complete; what is left is checking the candidates.

Next I will list the call sites of `Cookies` in `httpx/_auth.py`; the name is ours there, so each call site counts. Almost certainly the call sites fit. If there are too many call sites, I will list the call sites of `Cookies` in `httpx/_client.py`.

**Call:** `calls('httpx/_auth.py', 'Cookies')`

**Response**: outcome `ok`

```
calls of Cookies in httpx/_auth.py count=1
221:            Cookies(response.cookies).set_cookie_header(request=request)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "calls",
   "key": [
    "calls",
    "httpx/_auth.py",
    "Cookies"
   ],
   "desc": "list the call sites of `Cookies` in `httpx/_auth.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "httpx/_client.py",
    "Cookies"
   ],
   "desc": "list the call sites of `Cookies` in `httpx/_client.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "httpx/_models.py",
    "Cookies"
   ],
   "desc": "list the call sites of `Cookies` in `httpx/_models.py`"
  }
 ],
 "candidates": [
  {
   "call": "calls('httpx/_auth.py', 'Cookies')",
   "key": "[\"calls\", [\"httpx/_auth.py\", \"Cookies\"]]",
   "v1": [
    61,
    20
   ],
   "v2": [
    31,
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
     "httpx/_auth.py",
     "Cookies"
    ]
   ]
  },
  {
   "call": "calls('httpx/_client.py', 'Cookies')",
   "key": "[\"calls\", [\"httpx/_client.py\", \"Cookies\"]]",
   "v1": [
    61,
    20
   ],
   "v2": [
    31,
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
     "Cookies"
    ]
   ]
  },
  {
   "call": "calls('httpx/_models.py', 'Cookies')",
   "key": "[\"calls\", [\"httpx/_models.py\", \"Cookies\"]]",
   "v1": [
    61,
    20
   ],
   "v2": [
    31,
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
     "httpx/_models.py",
     "Cookies"
    ]
   ]
  }
 ],
 "choice": {
  "call": "calls('httpx/_auth.py', 'Cookies')",
  "key": "[\"calls\", [\"httpx/_auth.py\", \"Cookies\"]]",
  "provenance": "call sites of `Cookies` in `httpx/_auth.py` that refer to the module-level binding",
  "v2": [
   31,
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
  "ok": "[\"calls\", [\"httpx/_client.py\", \"Cookies\"]]",
  "cap": "[\"calls\", [\"httpx/_client.py\", \"Cookies\"]]"
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
  "planned": "[\"calls\", [\"httpx/_auth.py\", \"Cookies\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "calls",
   "step": 7,
   "path": "httpx/_auth.py",
   "name": "Cookies",
   "lines": [
    221
   ],
   "count": 1,
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "callers",
  "step": 2,
  "of": 2,
  "candidates": [
   "httpx/_auth.py",
   "httpx/_client.py",
   "httpx/_models.py",
   "tests/client/test_cookies.py",
   "tests/models/test_cookies.py"
  ],
  "table": [
   [
    "httpx/_auth.py",
    "httpx/_auth.py:221",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "httpx/_client.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "httpx/_models.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/client/test_cookies.py",
    "tests/client/test_cookies.py",
    "out",
    "the name is not bound at module level here"
   ],
   [
    "tests/models/test_cookies.py",
    "tests/models/test_cookies.py",
    "out",
    "the name is not bound at module level here"
   ]
  ],
  "uncovered": {
   "CALL": []
  },
  "n_in": 1,
  "n_out": 2,
  "n_pending": 2
 }
}
```
</details>

## Step 8

`httpx/_auth.py` calls `Cookies` at line 221, and those are real calls of the module-level name, not a shadowed local.

Tally: 1 call sites confirmed, 2 ruled out, 2 pending. The search itself is complete; what is left is checking the candidates.

I'll list the call sites of `Cookies` in `httpx/_client.py`; the name is ours there, so each call site counts. Almost certainly the call sites fit. If there are too many call sites, I will list the call sites of `Cookies` in `httpx/_models.py`.

**Call:** `calls('httpx/_client.py', 'Cookies')`

**Response**: outcome `ok`

```
calls of Cookies in httpx/_client.py count=4
211:        self._cookies = Cookies(cookies)
327:        self._cookies = Cookies(cookies)
419:            merged_cookies = Cookies(self.cookies)
484:        cookies = Cookies(self.cookies)
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
    "Cookies"
   ],
   "desc": "list the call sites of `Cookies` in `httpx/_client.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "httpx/_models.py",
    "Cookies"
   ],
   "desc": "list the call sites of `Cookies` in `httpx/_models.py`"
  }
 ],
 "candidates": [
  {
   "call": "calls('httpx/_client.py', 'Cookies')",
   "key": "[\"calls\", [\"httpx/_client.py\", \"Cookies\"]]",
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
     "Cookies"
    ]
   ]
  },
  {
   "call": "calls('httpx/_models.py', 'Cookies')",
   "key": "[\"calls\", [\"httpx/_models.py\", \"Cookies\"]]",
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
     "httpx/_models.py",
     "Cookies"
    ]
   ]
  }
 ],
 "choice": {
  "call": "calls('httpx/_client.py', 'Cookies')",
  "key": "[\"calls\", [\"httpx/_client.py\", \"Cookies\"]]",
  "provenance": "call sites of `Cookies` in `httpx/_client.py` that refer to the module-level binding",
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
  "ok": "[\"calls\", [\"httpx/_models.py\", \"Cookies\"]]",
  "cap": "[\"calls\", [\"httpx/_models.py\", \"Cookies\"]]"
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
  "planned": "[\"calls\", [\"httpx/_client.py\", \"Cookies\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "calls",
   "step": 8,
   "path": "httpx/_client.py",
   "name": "Cookies",
   "lines": [
    211,
    327,
    419,
    484
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
   "httpx/_auth.py",
   "httpx/_client.py",
   "httpx/_models.py",
   "tests/client/test_cookies.py",
   "tests/models/test_cookies.py"
  ],
  "table": [
   [
    "httpx/_auth.py",
    "httpx/_auth.py:221",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "httpx/_client.py",
    "httpx/_client.py:211",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "httpx/_client.py",
    "httpx/_client.py:327",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "httpx/_client.py",
    "httpx/_client.py:419",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "httpx/_client.py",
    "httpx/_client.py:484",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "httpx/_models.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/client/test_cookies.py",
    "tests/client/test_cookies.py",
    "out",
    "the name is not bound at module level here"
   ],
   [
    "tests/models/test_cookies.py",
    "tests/models/test_cookies.py",
    "out",
    "the name is not bound at module level here"
   ]
  ],
  "uncovered": {
   "CALL": []
  },
  "n_in": 5,
  "n_out": 2,
  "n_pending": 1
 }
}
```
</details>

## Step 9

`httpx/_client.py` calls `Cookies` at lines 211, 327, 419, 484, and those are real calls of the module-level name, not a shadowed local.

Tally: 5 call sites confirmed, 2 ruled out, 1 pending. The search itself is complete; what is left is checking the candidates.

Let me list the call sites of `Cookies` in `httpx/_models.py`; the name is ours there, so each call site counts. Almost certainly the call sites fit. If there are too many call sites, I follow whatever it opens up.

**Call:** `calls('httpx/_models.py', 'Cookies')`

**Response**: outcome `ok`

```
calls of Cookies in httpx/_models.py count=3
404:            Cookies(cookies).set_cookie_header(self)
837:            self._cookies = Cookies()
1206:        cookies = Cookies(cookies)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "calls",
   "key": [
    "calls",
    "httpx/_models.py",
    "Cookies"
   ],
   "desc": "list the call sites of `Cookies` in `httpx/_models.py`"
  }
 ],
 "candidates": [
  {
   "call": "calls('httpx/_models.py', 'Cookies')",
   "key": "[\"calls\", [\"httpx/_models.py\", \"Cookies\"]]",
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
     "httpx/_models.py",
     "Cookies"
    ]
   ]
  }
 ],
 "choice": {
  "call": "calls('httpx/_models.py', 'Cookies')",
  "key": "[\"calls\", [\"httpx/_models.py\", \"Cookies\"]]",
  "provenance": "call sites of `Cookies` in `httpx/_models.py` that refer to the module-level binding",
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
  "planned": "[\"calls\", [\"httpx/_models.py\", \"Cookies\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "calls",
   "step": 9,
   "path": "httpx/_models.py",
   "name": "Cookies",
   "lines": [
    404,
    837,
    1206
   ],
   "count": 3,
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "callers",
  "step": 2,
  "of": 2,
  "candidates": [
   "httpx/_auth.py",
   "httpx/_client.py",
   "httpx/_models.py",
   "tests/client/test_cookies.py",
   "tests/models/test_cookies.py"
  ],
  "table": [
   [
    "httpx/_auth.py",
    "httpx/_auth.py:221",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "httpx/_client.py",
    "httpx/_client.py:211",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "httpx/_client.py",
    "httpx/_client.py:327",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "httpx/_client.py",
    "httpx/_client.py:419",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "httpx/_client.py",
    "httpx/_client.py:484",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "httpx/_models.py",
    "httpx/_models.py:404",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "httpx/_models.py",
    "httpx/_models.py:837",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "httpx/_models.py",
    "httpx/_models.py:1206",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "tests/client/test_cookies.py",
    "tests/client/test_cookies.py",
    "out",
    "the name is not bound at module level here"
   ],
   [
    "tests/models/test_cookies.py",
    "tests/models/test_cookies.py",
    "out",
    "the name is not bound at module level here"
   ]
  ],
  "uncovered": {
   "CALL": []
  },
  "n_in": 8,
  "n_out": 2,
  "n_pending": 0
 }
}
```
</details>

## Final

`Cookies` is the class at `httpx/_models.py:1079`. 8 call sites in 3 modules: `httpx/_auth.py:221`, `httpx/_client.py:211`, `httpx/_client.py:327`, `httpx/_client.py:419`, `httpx/_client.py:484`, `httpx/_models.py:404`, `httpx/_models.py:837`, `httpx/_models.py:1206`. Ruled out along the way: `tests/client/test_cookies.py` (the name is not bound at module level here); `tests/models/test_cookies.py` (the name is not bound at module level here). Looking back, all 9 calls were needed.

**Answer:** `{"final_kind": "callers", "final": ["httpx/_auth.py:221", "httpx/_client.py:211", "httpx/_client.py:327", "httpx/_client.py:419", "httpx/_client.py:484", "httpx/_models.py:404", "httpx/_models.py:837", "httpx/_models.py:1206"], "steps": [{"op": "resolve", "output": {"kind": "def", "path": "httpx/_models.py", "line": 1079, "name": "Cookies", "detail": "class"}}, {"op": "callers", "output": ["httpx/_auth.py:221", "httpx/_client.py:211", "httpx/_client.py:327", "httpx/_client.py:419", "httpx/_client.py:484", "httpx/_models.py:404", "httpx/_models.py:837", "httpx/_models.py:1206"]}], "stuck": null}`  
**Stopped:** certificate after 9 calls