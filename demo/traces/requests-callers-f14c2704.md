# requests-callers-f14c2704

**Repository:** requests  
**Chain:** callers  
**Seed:** 0, prior 736169d01b033d9f, floor 7

## Task

`PreparedRequest` is defined at `src/requests/models.py:378` (class).

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N; bindings take effect in source order. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. A class derives from a definition when a base written as a bare name or `module.Name` resolves to it. A call site is `name(...)` where the bare name refers to the module-level binding (not a parameter or local). Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

Starting from the definition of `PreparedRequest` at `src/requests/models.py:378`. Then every real call site of it, which means checking what the name refers to in each file that mentions it.

Next I will search the whole tree for calls of `PreparedRequest`; the search has to be complete before I can call the set final. Probably it fits under the cap. If nothing turns up, that finishes it; if it caps, I follow whatever it opens up.

**Call:** `grep('\\bPreparedRequest\\s*\\(', '.')`

**Response**: outcome `mid`

```
src/requests/models.py:362:        p = PreparedRequest()
src/requests/models.py:378:class PreparedRequest(RequestEncodingMixin, RequestHooksMixin):
src/requests/models.py:457:        p = PreparedRequest()
src/requests/sessions.py:540:        p = PreparedRequest()
tests/test_requests.py:2644:    p = PreparedRequest()
tests/test_requests.py:2681:    prep = PreparedRequest()
tests/test_requests.py:2704:    p = PreparedRequest()
tests/test_requests.py:2732:    p = PreparedRequest()
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
   "desc": "search `.` for calls of `PreparedRequest`"
  }
 ],
 "candidates": [
  {
   "call": "grep('\\\\bPreparedRequest\\\\s*\\\\(', '.')",
   "key": "[\"grep\", [\"\\\\bPreparedRequest\\\\s*\\\\(\", \".\"]]",
   "v1": [
    2035528063,
    1231611160
   ],
   "v2": [
    2035528063,
    1231611160
   ],
   "p_cap": [
    3,
    40
   ],
   "forecast": {
    "zero": [
     1,
     5
    ],
    "mid": [
     29,
     40
    ],
    "cap": [
     3,
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
  "call": "grep('\\\\bPreparedRequest\\\\s*\\\\(', '.')",
  "key": "[\"grep\", [\"\\\\bPreparedRequest\\\\s*\\\\(\", \".\"]]",
  "provenance": "call lines naming `PreparedRequest` under `.` (derived)",
  "v2": [
   2035528063,
   1231611160
  ]
 },
 "forecast": {
  "zero": [
   1,
   5
  ],
  "mid": [
   29,
   40
  ],
  "cap": [
   3,
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
 "adherence": null,
 "facts": [
  {
   "kind": "grep",
   "step": 1,
   "pattern": "\\bPreparedRequest\\s*\\(",
   "scope": ".",
   "hits": [
    [
     "src/requests/models.py",
     362
    ],
    [
     "src/requests/models.py",
     378
    ],
    [
     "src/requests/models.py",
     457
    ],
    [
     "src/requests/sessions.py",
     540
    ],
    [
     "tests/test_requests.py",
     2644
    ],
    [
     "tests/test_requests.py",
     2681
    ],
    [
     "tests/test_requests.py",
     2704
    ],
    [
     "tests/test_requests.py",
     2732
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "phase": "callers",
  "step": 1,
  "of": 1,
  "candidates": [
   "src/requests/models.py",
   "src/requests/sessions.py",
   "tests/test_requests.py"
  ],
  "table": [
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
    "tests/test_requests.py",
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

## Step 2

8 matching lines anywhere for calls of `PreparedRequest`, in `src/requests/models.py`, `src/requests/sessions.py`, `tests/test_requests.py`, and the search was under the cap, so that is the complete set there.

Let me look at `src/requests/sessions.py`'s top-level names for `PreparedRequest`; before counting calls I need to know the name refers to our definition there. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `src/requests/models.py`'s top-level names for `PreparedRequest`.

**Call:** `symbols('src/requests/sessions.py', 'PreparedRequest')`

**Response**: outcome `ok`

```
module src/requests/sessions.py lines=921 dynamic=no all=none
39 from PreparedRequest <- .models PreparedRequest
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
    "PreparedRequest"
   ],
   "desc": "check what `PreparedRequest` means inside `src/requests/models.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/requests/sessions.py",
    "PreparedRequest"
   ],
   "desc": "check what `PreparedRequest` means inside `src/requests/sessions.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_requests.py",
    "PreparedRequest"
   ],
   "desc": "check what `PreparedRequest` means inside `tests/test_requests.py`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/requests/models.py', 'PreparedRequest')",
   "key": "[\"symbols\", [\"src/requests/models.py\", \"PreparedRequest\"]]",
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
     "src/requests/models.py",
     "PreparedRequest"
    ]
   ]
  },
  {
   "call": "symbols('src/requests/sessions.py', 'PreparedRequest')",
   "key": "[\"symbols\", [\"src/requests/sessions.py\", \"PreparedRequest\"]]",
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
     "src/requests/sessions.py",
     "PreparedRequest"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_requests.py', 'PreparedRequest')",
   "key": "[\"symbols\", [\"tests/test_requests.py\", \"PreparedRequest\"]]",
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
     "PreparedRequest"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/requests/sessions.py', 'PreparedRequest')",
  "key": "[\"symbols\", [\"src/requests/sessions.py\", \"PreparedRequest\"]]",
  "provenance": "`src/requests/sessions.py` had a matching line (step 1); its outline names every `PreparedRequest` import exactly",
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
  "ok": "[\"symbols\", [\"src/requests/models.py\", \"PreparedRequest\"]]",
  "cap": "[\"symbols\", [\"src/requests/models.py\", \"PreparedRequest\"]]"
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
   "step": 2,
   "path": "src/requests/sessions.py",
   "filter": "PreparedRequest",
   "header": {
    "lines": 921,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/requests/sessions.py",
     "name": "PreparedRequest",
     "line": 39,
     "kind": "from",
     "src": ".models",
     "src_name": "PreparedRequest",
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
  "step": 1,
  "of": 1,
  "candidates": [
   "src/requests/models.py",
   "src/requests/sessions.py",
   "tests/test_requests.py"
  ],
  "table": [
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
    "tests/test_requests.py",
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

## Step 3

`src/requests/sessions.py` does not define `PreparedRequest` itself; line 39 imports it from `.models`.

Tally: 0 call sites confirmed, 0 ruled out, 3 pending. The search itself is complete; what is left is checking the candidates.

I'll look at `src/requests/models.py`'s top-level names for `PreparedRequest`; that settles what the name means there. Almost certainly it is defined right there. If the name is not bound there or it is re-exported from somewhere else, I will look at `tests/test_requests.py`'s top-level names for `PreparedRequest`.

**Call:** `symbols('src/requests/models.py', 'PreparedRequest')`

**Response**: outcome `def`

```
module src/requests/models.py lines=1185 dynamic=no all=none
378 class PreparedRequest (RequestEncodingMixin,RequestHooksMixin)
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
    "PreparedRequest"
   ],
   "desc": "check what `PreparedRequest` means inside `src/requests/models.py`"
  },
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/requests/models.py",
    "PreparedRequest"
   ],
   "desc": "check the top-level names of `src/requests/models.py` for `PreparedRequest`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_requests.py",
    "PreparedRequest"
   ],
   "desc": "check what `PreparedRequest` means inside `tests/test_requests.py`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/requests/models.py', 'PreparedRequest')",
   "key": "[\"symbols\", [\"src/requests/models.py\", \"PreparedRequest\"]]",
   "v1": [
    1413872689,
    506778650
   ],
   "v2": [
    712004131,
    253389325
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     47,
     50
    ],
    "reexport": [
     1,
     50
    ],
    "star": [
     1,
     100
    ],
    "none": [
     3,
     100
    ]
   },
   "serves": [
    [
     "bindings",
     "src/requests/models.py",
     "PreparedRequest"
    ],
    [
     "outline",
     "src/requests/models.py",
     "PreparedRequest"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_requests.py', 'PreparedRequest')",
   "key": "[\"symbols\", [\"tests/test_requests.py\", \"PreparedRequest\"]]",
   "v1": [
    2300234837,
    506778650
   ],
   "v2": [
    712004131,
    253389325
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
     "PreparedRequest"
    ]
   ]
  },
  {
   "call": "symbols('src/requests/models.py')",
   "key": "[\"symbols\", [\"src/requests/models.py\"]]",
   "v1": [
    414966768739,
    89193042400
   ],
   "v2": [
    85685480981,
    22298260600
   ],
   "p_cap": [
    47,
    352
   ],
   "forecast": {
    "def": [
     2867,
     3520
    ],
    "reexport": [
     61,
     3520
    ],
    "star": [
     61,
     7040
    ],
    "none": [
     183,
     7040
    ],
    "cap": [
     47,
     352
    ]
   },
   "serves": [
    [
     "bindings",
     "src/requests/models.py",
     "PreparedRequest"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/requests/models.py', 'PreparedRequest')",
  "key": "[\"symbols\", [\"src/requests/models.py\", \"PreparedRequest\"]]",
  "provenance": "`src/requests/models.py` had a matching line (task); its outline names every `PreparedRequest` import exactly",
  "v2": [
   712004131,
   253389325
  ]
 },
 "forecast": {
  "def": [
   47,
   50
  ],
  "reexport": [
   1,
   50
  ],
  "star": [
   1,
   100
  ],
  "none": [
   3,
   100
  ]
 },
 "plan": {
  "def": "[\"symbols\", [\"tests/test_requests.py\", \"PreparedRequest\"]]",
  "reexport": "[\"symbols\", [\"tests/test_requests.py\", \"PreparedRequest\"]]",
  "star": "[\"symbols\", [\"tests/test_requests.py\", \"PreparedRequest\"]]",
  "none": "[\"symbols\", [\"tests/test_requests.py\", \"PreparedRequest\"]]"
 },
 "hedges": [
  {
   "outcome": "def",
   "word": "almost certainly",
   "p": [
    47,
    50
   ]
  }
 ],
 "adherence": {
  "planned": "[\"symbols\", [\"src/requests/models.py\", \"PreparedRequest\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 3,
   "path": "src/requests/models.py",
   "filter": "PreparedRequest",
   "header": {
    "lines": 1185,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/requests/models.py",
     "name": "PreparedRequest",
     "line": 378,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "RequestEncodingMixin",
      "RequestHooksMixin"
     ]
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "callers",
  "step": 1,
  "of": 1,
  "candidates": [
   "src/requests/models.py",
   "src/requests/sessions.py",
   "tests/test_requests.py"
  ],
  "table": [
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
    "tests/test_requests.py",
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

## Step 4

`PreparedRequest` is a class defined in `src/requests/models.py` at line 378.

Tally: 0 call sites confirmed, 0 ruled out, 3 pending. The search itself is complete; what is left is checking the candidates.

I'll look at `tests/test_requests.py`'s top-level names for `PreparedRequest`; before counting calls I need to know the name refers to our definition there. Almost certainly the outline shows what I need. If the outline is too long to fit, I will list the call sites of `PreparedRequest` in `src/requests/models.py`.

**Call:** `symbols('tests/test_requests.py', 'PreparedRequest')`

**Response**: outcome `ok`

```
module tests/test_requests.py lines=3095 dynamic=no all=none
53 from PreparedRequest <- requests.models PreparedRequest
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/requests/models.py",
    "PreparedRequest"
   ],
   "desc": "list the call sites of `PreparedRequest` in `src/requests/models.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/requests/sessions.py",
    "PreparedRequest"
   ],
   "desc": "list the call sites of `PreparedRequest` in `src/requests/sessions.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_requests.py",
    "PreparedRequest"
   ],
   "desc": "check what `PreparedRequest` means inside `tests/test_requests.py`"
  }
 ],
 "candidates": [
  {
   "call": "calls('src/requests/models.py', 'PreparedRequest')",
   "key": "[\"calls\", [\"src/requests/models.py\", \"PreparedRequest\"]]",
   "v1": [
    724739,
    191780
   ],
   "v2": [
    3642873,
    958900
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
     "src/requests/models.py",
     "PreparedRequest"
    ]
   ]
  },
  {
   "call": "calls('src/requests/sessions.py', 'PreparedRequest')",
   "key": "[\"calls\", [\"src/requests/sessions.py\", \"PreparedRequest\"]]",
   "v1": [
    724739,
    191780
   ],
   "v2": [
    3642873,
    958900
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
     "src/requests/sessions.py",
     "PreparedRequest"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_requests.py', 'PreparedRequest')",
   "key": "[\"symbols\", [\"tests/test_requests.py\", \"PreparedRequest\"]]",
   "v1": [
    898732,
    239725
   ],
   "v2": [
    3642873,
    958900
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
     "PreparedRequest"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_requests.py', 'PreparedRequest')",
  "key": "[\"symbols\", [\"tests/test_requests.py\", \"PreparedRequest\"]]",
  "provenance": "`tests/test_requests.py` had a matching line (step 1); its outline names every `PreparedRequest` import exactly",
  "v2": [
   3642873,
   958900
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
  "ok": "[\"calls\", [\"src/requests/models.py\", \"PreparedRequest\"]]",
  "cap": "[\"calls\", [\"src/requests/models.py\", \"PreparedRequest\"]]"
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
  "planned": "[\"symbols\", [\"tests/test_requests.py\", \"PreparedRequest\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 4,
   "path": "tests/test_requests.py",
   "filter": "PreparedRequest",
   "header": {
    "lines": 3095,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_requests.py",
     "name": "PreparedRequest",
     "line": 53,
     "kind": "from",
     "src": "requests.models",
     "src_name": "PreparedRequest",
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
  "step": 1,
  "of": 1,
  "candidates": [
   "src/requests/models.py",
   "src/requests/sessions.py",
   "tests/test_requests.py"
  ],
  "table": [
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
    "tests/test_requests.py",
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

The test module `tests/test_requests.py` does not define `PreparedRequest` itself; line 53 imports it from `requests.models`.

Tally: 0 call sites confirmed, 0 ruled out, 3 pending. The search itself is complete; what is left is checking the candidates.

Let me list the call sites of `PreparedRequest` in `src/requests/models.py`; the name is ours there, so each call site counts. Almost certainly the call sites fit. If there are too many call sites, I will list `./` to see what lives there.

**Call:** `calls('src/requests/models.py', 'PreparedRequest')`

**Response**: outcome `ok`

```
calls of PreparedRequest in src/requests/models.py count=2
362:        p = PreparedRequest()
457:        p = PreparedRequest()
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/requests/models.py",
    "PreparedRequest"
   ],
   "desc": "list the call sites of `PreparedRequest` in `src/requests/models.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/requests/sessions.py",
    "PreparedRequest"
   ],
   "desc": "list the call sites of `PreparedRequest` in `src/requests/sessions.py`"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_requests.py",
    "requests.models"
   ],
   "desc": "find where `requests.models` (imported by `tests/test_requests.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "calls('src/requests/models.py', 'PreparedRequest')",
   "key": "[\"calls\", [\"src/requests/models.py\", \"PreparedRequest\"]]",
   "v1": [
    18163,
    4460
   ],
   "v2": [
    52259,
    13380
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
     "src/requests/models.py",
     "PreparedRequest"
    ]
   ]
  },
  {
   "call": "calls('src/requests/sessions.py', 'PreparedRequest')",
   "key": "[\"calls\", [\"src/requests/sessions.py\", \"PreparedRequest\"]]",
   "v1": [
    18163,
    4460
   ],
   "v2": [
    52259,
    13380
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
     "src/requests/sessions.py",
     "PreparedRequest"
    ]
   ]
  },
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    5159,
    1338
   ],
   "v2": [
    52259,
    13380
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
     "requests.models"
    ]
   ]
  },
  {
   "call": "symbols('requests/models.py', 'PreparedRequest')",
   "key": "[\"symbols\", [\"requests/models.py\", \"PreparedRequest\"]]",
   "v1": [
    18797244842848,
    4390165628409
   ],
   "v2": [
    552535851182659,
    131704968852270
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
     "requests.models"
    ]
   ]
  },
  {
   "call": "symbols('requests/models/__init__.py', 'PreparedRequest')",
   "key": "[\"symbols\", [\"requests/models/__init__.py\", \"PreparedRequest\"]]",
   "v1": [
    678799959067,
    135957758481
   ],
   "v2": [
    4385796474721,
    906385056540
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
     "requests.models"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+PreparedRequest\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+PreparedRequest\\\\b\", \".\"]]",
   "v1": [
    1120,
    223
   ],
   "v2": [
    6497,
    1338
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
     "requests.models"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+PreparedRequest\\\\b', 'src')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+PreparedRequest\\\\b\", \"src\"]]",
   "v1": [
    1120,
    223
   ],
   "v2": [
    6497,
    1338
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
     "requests.models"
    ]
   ]
  }
 ],
 "choice": {
  "call": "calls('src/requests/models.py', 'PreparedRequest')",
  "key": "[\"calls\", [\"src/requests/models.py\", \"PreparedRequest\"]]",
  "provenance": "call sites of `PreparedRequest` in `src/requests/models.py` that refer to the module-level binding",
  "v2": [
   52259,
   13380
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
  "ok": "[\"ls\", [\".\"]]",
  "cap": "[\"ls\", [\".\"]]"
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
  "planned": "[\"calls\", [\"src/requests/models.py\", \"PreparedRequest\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "calls",
   "step": 5,
   "path": "src/requests/models.py",
   "name": "PreparedRequest",
   "lines": [
    362,
    457
   ],
   "count": 2,
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "callers",
  "step": 1,
  "of": 1,
  "candidates": [
   "src/requests/models.py",
   "src/requests/sessions.py",
   "tests/test_requests.py"
  ],
  "table": [
   [
    "src/requests/models.py",
    "src/requests/models.py:362",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/requests/models.py",
    "src/requests/models.py:457",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/requests/sessions.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_requests.py",
    null,
    "pending",
    "not yet examined"
   ]
  ],
  "uncovered": {
   "CALL": []
  },
  "n_in": 2,
  "n_out": 0,

```
</details>

## Step 6

`src/requests/models.py` calls `PreparedRequest` at lines 362, 457, and those are real calls of the module-level name, not a shadowed local.

Tally: 2 call sites confirmed, 0 ruled out, 2 pending. The search itself is complete; what is left is checking the candidates.

Next I will list `./` to see what lives there; the listing settles whether the import is a module, a package, or not here at all. Very likely the listing fits. If the listing is too long, I will list the call sites of `PreparedRequest` in `src/requests/sessions.py`.

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
   "kind": "calls",
   "key": [
    "calls",
    "src/requests/sessions.py",
    "PreparedRequest"
   ],
   "desc": "list the call sites of `PreparedRequest` in `src/requests/sessions.py`"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_requests.py",
    "requests.models"
   ],
   "desc": "find where `requests.models` (imported by `tests/test_requests.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "calls('src/requests/sessions.py', 'PreparedRequest')",
   "key": "[\"calls\", [\"src/requests/sessions.py\", \"PreparedRequest\"]]",
   "v1": [
    13703,
    4460
   ],
   "v2": [
    38879,
    13380
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
     "src/requests/sessions.py",
     "PreparedRequest"
    ]
   ]
  },
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    3821,
    1338
   ],
   "v2": [
    38879,
    13380
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
     "requests.models"
    ]
   ]
  },
  {
   "call": "symbols('requests/models.py', 'PreparedRequest')",
   "key": "[\"symbols\", [\"requests/models.py\", \"PreparedRequest\"]]",
   "v1": [
    14407079214439,
    4390165628409
   ],
   "v2": [
    420830882330389,
    131704968852270
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
     "requests.models"
    ]
   ]
  },
  {
   "call": "symbols('requests/models/__init__.py', 'PreparedRequest')",
   "key": "[\"symbols\", [\"requests/models/__init__.py\", \"PreparedRequest\"]]",
   "v1": [
    542842200586,
    135957758481
   ],
   "v2": [
    3479411418181,
    906385056540
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
     "requests.models"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+PreparedRequest\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+PreparedRequest\\\\b\", \".\"]]",
   "v1": [
    897,
    223
   ],
   "v2": [
    5159,
    1338
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
     "requests.models"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+PreparedRequest\\\\b', 'src')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+PreparedRequest\\\\b\", \"src\"]]",
   "v1": [
    897,
    223
   ],
   "v2": [
    5159,
    1338
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
     "requests.models"
    ]
   ]
  }
 ],
 "choice": {
  "call": "ls('.')",
  "key": "[\"ls\", [\".\"]]",
  "provenance": "`requests.models` imported by `tests/test_requests.py` should live under `.`",
  "v2": [
   38879,
   13380
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
  "complete": "[\"calls\", [\"src/requests/sessions.py\", \"PreparedRequest\"]]",
  "cap": "[\"calls\", [\"src/requests/sessions.py\", \"PreparedRequest\"]]"
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
  "phase": "callers",
  "step": 1,
  "of": 1,
  "candidates": [
   "src/requests/models.py",
   "src/requests/sessions.py",
   "tests/test_requests.py"
  ],
  "table": [
   [
    "src/requests/models.py",
    "src/requests/models.py:362",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/requests/models.py",
    "src/requests/models.py:457",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/requests/sessions.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_requests.py",
    null,
    "pending",
    "not yet examined"
   ]
  ],
  "uncovered": {
   "CALL": []
  },
  "n_in": 2,
  "n_out": 0,
  "n_pending": 2
 }
}
```
</details>

## Step 7

`./` has 14 entries: there is no `requests` here.

Next I will list the call sites of `PreparedRequest` in `src/requests/sessions.py`; the name is ours there, so each call site counts. Almost certainly the call sites fit. If there are too many call sites, I will list the call sites of `PreparedRequest` in `tests/test_requests.py`.

**Call:** `calls('src/requests/sessions.py', 'PreparedRequest')`

**Response**: outcome `ok`

```
calls of PreparedRequest in src/requests/sessions.py count=1
540:        p = PreparedRequest()
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/requests/sessions.py",
    "PreparedRequest"
   ],
   "desc": "list the call sites of `PreparedRequest` in `src/requests/sessions.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "tests/test_requests.py",
    "PreparedRequest"
   ],
   "desc": "list the call sites of `PreparedRequest` in `tests/test_requests.py`"
  }
 ],
 "candidates": [
  {
   "call": "calls('src/requests/sessions.py', 'PreparedRequest')",
   "key": "[\"calls\", [\"src/requests/sessions.py\", \"PreparedRequest\"]]",
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
     "src/requests/sessions.py",
     "PreparedRequest"
    ]
   ]
  },
  {
   "call": "calls('tests/test_requests.py', 'PreparedRequest')",
   "key": "[\"calls\", [\"tests/test_requests.py\", \"PreparedRequest\"]]",
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
     "tests/test_requests.py",
     "PreparedRequest"
    ]
   ]
  }
 ],
 "choice": {
  "call": "calls('src/requests/sessions.py', 'PreparedRequest')",
  "key": "[\"calls\", [\"src/requests/sessions.py\", \"PreparedRequest\"]]",
  "provenance": "call sites of `PreparedRequest` in `src/requests/sessions.py` that refer to the module-level binding",
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
  "ok": "[\"calls\", [\"tests/test_requests.py\", \"PreparedRequest\"]]",
  "cap": "[\"calls\", [\"tests/test_requests.py\", \"PreparedRequest\"]]"
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
  "planned": "[\"calls\", [\"src/requests/sessions.py\", \"PreparedRequest\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "calls",
   "step": 7,
   "path": "src/requests/sessions.py",
   "name": "PreparedRequest",
   "lines": [
    540
   ],
   "count": 1,
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "callers",
  "step": 1,
  "of": 1,
  "candidates": [
   "src/requests/models.py",
   "src/requests/sessions.py",
   "tests/test_requests.py"
  ],
  "table": [
   [
    "src/requests/models.py",
    "src/requests/models.py:362",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/requests/models.py",
    "src/requests/models.py:457",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/requests/sessions.py",
    "src/requests/sessions.py:540",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "tests/test_requests.py",
    null,
    "pending",
    "not yet examined"
   ]
  ],
  "uncovered": {
   "CALL": []
  },
  "n_in": 3,
  "n_out": 0,
  "n_pending": 1
 }
}
```
</details>

## Step 8

`src/requests/sessions.py` calls `PreparedRequest` at line 540, and those are real calls of the module-level name, not a shadowed local.

Tally: 3 call sites confirmed, 0 ruled out, 1 pending. The search itself is complete; what is left is checking the candidates.

I'll list the call sites of `PreparedRequest` in `tests/test_requests.py`; the name is ours there, so each call site counts. Almost certainly the call sites fit. If there are too many call sites, I follow whatever it opens up.

**Call:** `calls('tests/test_requests.py', 'PreparedRequest')`

**Response**: outcome `ok`

```
calls of PreparedRequest in tests/test_requests.py count=4
2644:    p = PreparedRequest()
2681:    prep = PreparedRequest()
2704:    p = PreparedRequest()
2732:    p = PreparedRequest()
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "calls",
   "key": [
    "calls",
    "tests/test_requests.py",
    "PreparedRequest"
   ],
   "desc": "list the call sites of `PreparedRequest` in `tests/test_requests.py`"
  }
 ],
 "candidates": [
  {
   "call": "calls('tests/test_requests.py', 'PreparedRequest')",
   "key": "[\"calls\", [\"tests/test_requests.py\", \"PreparedRequest\"]]",
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
     "tests/test_requests.py",
     "PreparedRequest"
    ]
   ]
  }
 ],
 "choice": {
  "call": "calls('tests/test_requests.py', 'PreparedRequest')",
  "key": "[\"calls\", [\"tests/test_requests.py\", \"PreparedRequest\"]]",
  "provenance": "call sites of `PreparedRequest` in `tests/test_requests.py` that refer to the module-level binding",
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
  "planned": "[\"calls\", [\"tests/test_requests.py\", \"PreparedRequest\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "calls",
   "step": 8,
   "path": "tests/test_requests.py",
   "name": "PreparedRequest",
   "lines": [
    2644,
    2681,
    2704,
    2732
   ],
   "count": 4,
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "callers",
  "step": 1,
  "of": 1,
  "candidates": [
   "src/requests/models.py",
   "src/requests/sessions.py",
   "tests/test_requests.py"
  ],
  "table": [
   [
    "src/requests/models.py",
    "src/requests/models.py:362",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/requests/models.py",
    "src/requests/models.py:457",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/requests/sessions.py",
    "src/requests/sessions.py:540",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "tests/test_requests.py",
    "tests/test_requests.py:2644",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "tests/test_requests.py",
    "tests/test_requests.py:2681",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "tests/test_requests.py",
    "tests/test_requests.py:2704",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "tests/test_requests.py",
    "tests/test_requests.py:2732",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ]
  ],
  "uncovered": {
   "CALL": []
  },
  "n_in": 7,
  "n_out": 0,
  "n_pending": 0
 }
}
```
</details>

## Final

7 call sites in 3 modules: `src/requests/models.py:362`, `src/requests/models.py:457`, `src/requests/sessions.py:540`, `tests/test_requests.py:2644`, `tests/test_requests.py:2681`, `tests/test_requests.py:2704`, `tests/test_requests.py:2732`. Looking back, all 8 calls were needed.

**Answer:** `{"final_kind": "callers", "final": ["src/requests/models.py:362", "src/requests/models.py:457", "src/requests/sessions.py:540", "tests/test_requests.py:2644", "tests/test_requests.py:2681", "tests/test_requests.py:2704", "tests/test_requests.py:2732"], "steps": [{"op": "callers", "output": ["src/requests/models.py:362", "src/requests/models.py:457", "src/requests/sessions.py:540", "tests/test_requests.py:2644", "tests/test_requests.py:2681", "tests/test_requests.py:2704", "tests/test_requests.py:2732"]}], "stuck": null}`  
**Stopped:** certificate after 8 calls