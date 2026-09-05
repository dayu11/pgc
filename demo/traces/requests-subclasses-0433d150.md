# requests-subclasses-0433d150

**Repository:** requests  
**Chain:** resolve → subclasses  
**Seed:** 0, prior 736169d01b033d9f, floor 5

## Task

In `src/requests/__init__.py` line 172, `RequestException` is imported from `.exceptions`. Which definition does the module-level name `RequestException` actually refer to? Give `path:line`. Then list every class that derives from it directly, as `path:line:ClassName`, making sure each base name really resolves to this definition.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N; bindings take effect in source order. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. A class derives from a definition when a base written as a bare name or `module.Name` resolves to it. A call site is `name(...)` where the bare name refers to the module-level binding (not a parameter or local). Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

I need to find what `RequestException` really is in `src/requests/__init__.py`: line 172 imports it from `.exceptions`, so the definition is at least one hop away. Then I need every class that derives from it, checking that each base name really points at this definition.

Next I will check `src/requests/__init__.py` for any other binding of `RequestException` besides the import on line 172; almost certainly the import is the only one, and then `.exceptions` is the place to follow.

**Call:** `symbols('src/requests/__init__.py', 'RequestException')`

**Response**: outcome `reexport`

```
module src/requests/__init__.py lines=220 dynamic=no all=static@188
172 from RequestException <- .exceptions RequestException
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/requests/__init__.py",
    "RequestException"
   ],
   "desc": "check the top-level names of `src/requests/__init__.py` for `RequestException`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/requests/__init__.py', 'RequestException')",
   "key": "[\"symbols\", [\"src/requests/__init__.py\", \"RequestException\"]]",
   "v1": [
    1876783,
    635550
   ],
   "v2": [
    1876783,
    635550
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
     "src/requests/__init__.py",
     "RequestException"
    ]
   ]
  },
  {
   "call": "symbols('src/requests/__init__.py')",
   "key": "[\"symbols\", [\"src/requests/__init__.py\"]]",
   "v1": [
    13773031,
    4448850
   ],
   "v2": [
    13773031,
    4448850
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
     "src/requests/__init__.py",
     "RequestException"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/requests/__init__.py', 'RequestException')",
  "key": "[\"symbols\", [\"src/requests/__init__.py\", \"RequestException\"]]",
  "provenance": "module `src/requests/__init__.py` (task), name `RequestException` (task)",
  "v2": [
   1876783,
   635550
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
   "path": "src/requests/__init__.py",
   "filter": "RequestException",
   "header": {
    "lines": 220,
    "dynamic": false,
    "all_status": "static",
    "all_line": 188
   },
   "bindings": [
    {
     "module": "src/requests/__init__.py",
     "name": "RequestException",
     "line": 172,
     "kind": "from",
     "src": ".exceptions",
     "src_name": "RequestException",
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
    "src/requests/__init__.py",
    "RequestException",
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

The package `src/requests` does not define `RequestException` itself; line 172 imports it from `.exceptions`.

So far: `src/requests/__init__.py` takes `RequestException` from `.exceptions`, which I still have to locate.

Let me outline `src/requests/exceptions.py` directly, which both checks that the file exists and shows me `RequestException`; if `.exceptions` is a plain module that is where it has to be. Very likely it is defined right there. If the file does not exist, I will list `src/requests/` to see what lives there; if the name is not bound there, that finishes it. I could list `src/requests/` to see what lives there instead, but it tends to open more follow-up work.

**Call:** `symbols('src/requests/exceptions.py', 'RequestException')`

**Response**: outcome `def`

```
module src/requests/exceptions.py lines=163 dynamic=no all=none
20 class RequestException (IOError)
38 class InvalidJSONError (RequestException)
66 class HTTPError (RequestException)
70 class ConnectionError (RequestException)
82 class Timeout (RequestException)
102 class URLRequired (RequestException)
106 class TooManyRedirects (RequestException)
110 class MissingSchema (RequestException,ValueError)
114 class InvalidSchema (RequestException,ValueError)
118 class InvalidURL (RequestException,ValueError)
122 class InvalidHeader (RequestException,ValueError)
130 class ChunkedEncodingError (RequestException)
134 class ContentDecodingError (RequestException,BaseHTTPError)
138 class StreamConsumedError (RequestException,TypeError)
142 class RetryError (RequestException)
146 class UnrewindableBodyError (RequestException)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/requests/__init__.py",
    ".exceptions"
   ],
   "desc": "find where `.exceptions` (imported by `src/requests/__init__.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/requests/exceptions.py', 'RequestException')",
   "key": "[\"symbols\", [\"src/requests/exceptions.py\", \"RequestException\"]]",
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
     "src/requests/__init__.py",
     ".exceptions"
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
     "src/requests/__init__.py",
     ".exceptions"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+RequestException\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+RequestException\\\\b\", \".\"]]",
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
     "src/requests/__init__.py",
     ".exceptions"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+RequestException\\\\b', 'src')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+RequestException\\\\b\", \"src\"]]",
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
     "src/requests/__init__.py",
     ".exceptions"
    ]
   ]
  },
  {
   "call": "symbols('src/requests/exceptions/__init__.py', 'RequestException')",
   "key": "[\"symbols\", [\"src/requests/exceptions/__init__.py\", \"RequestException\"]]",
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
     "src/requests/__init__.py",
     ".exceptions"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/requests/exceptions.py', 'RequestException')",
  "key": "[\"symbols\", [\"src/requests/exceptions.py\", \"RequestException\"]]",
  "provenance": "`.exceptions` would be `src/requests/exceptions.py` if that file exists; one call both checks and closes it",
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
   "path": "src/requests/exceptions.py",
   "filter": "RequestException",
   "header": {
    "lines": 163,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/requests/exceptions.py",
     "name": "RequestException",
     "line": 20,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "IOError"
     ]
    },
    {
     "module": "src/requests/exceptions.py",
     "name": "InvalidJSONError",
     "line": 38,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "RequestException"
     ]
    },
    {
     "module": "src/requests/exceptions.py",
     "name": "HTTPError",
     "line": 66,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "RequestException"
     ]
    },
    {
     "module": "src/requests/exceptions.py",
     "name": "ConnectionError",
     "line": 70,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "RequestException"
     ]
    },
    {
     "module": "src/requests/exceptions.py",
     "name": "Timeout",
     "line": 82,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "RequestException"
     ]
    },
    {
     "module": "src/requests/exceptions.py",
     "name": "URLRequired",
     "line": 102,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "RequestException"
     ]
    },
    {
     "module": "src/requests/exceptions.py",
     "name": "TooManyRedirects",
     "line": 106,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "RequestException"
     ]
  
```
</details>

## Step 3

There it is: `RequestException` is a class at `src/requests/exceptions.py:20`. That settles the definition; now its subclasses.

I'll search the whole tree for classes deriving from `RequestException`; the search has to be complete before I can call the set final. Very likely nothing turns up. If it fits under the cap or it caps, I follow whatever it opens up.

**Call:** `grep('^\\s*class\\s+\\w+\\s*\\(.*\\bRequestException\\b', '.')`

**Response**: outcome `mid`

```
src/requests/exceptions.py:38:class InvalidJSONError(RequestException):
src/requests/exceptions.py:66:class HTTPError(RequestException):
src/requests/exceptions.py:70:class ConnectionError(RequestException):
src/requests/exceptions.py:82:class Timeout(RequestException):
src/requests/exceptions.py:102:class URLRequired(RequestException):
src/requests/exceptions.py:106:class TooManyRedirects(RequestException):
src/requests/exceptions.py:110:class MissingSchema(RequestException, ValueError):
src/requests/exceptions.py:114:class InvalidSchema(RequestException, ValueError):
src/requests/exceptions.py:118:class InvalidURL(RequestException, ValueError):
src/requests/exceptions.py:122:class InvalidHeader(RequestException, ValueError):
src/requests/exceptions.py:130:class ChunkedEncodingError(RequestException):
src/requests/exceptions.py:134:class ContentDecodingError(RequestException, BaseHTTPError):
src/requests/exceptions.py:138:class StreamConsumedError(RequestException, TypeError):
src/requests/exceptions.py:142:class RetryError(RequestException):
src/requests/exceptions.py:146:class UnrewindableBodyError(RequestException):
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
   "desc": "search `.` for classes deriving from `RequestException`"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*class\\\\s+\\\\w+\\\\s*\\\\(.*\\\\bRequestException\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*class\\\\s+\\\\w+\\\\s*\\\\(.*\\\\bRequestException\\\\b\", \".\"]]",
   "v1": [
    1736765483,
    1200820881
   ],
   "v2": [
    1736765483,
    1200820881
   ],
   "p_cap": [
    2,
    39
   ],
   "forecast": {
    "zero": [
     34,
     39
    ],
    "mid": [
     1,
     13
    ],
    "cap": [
     2,
     39
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
  "call": "grep('^\\\\s*class\\\\s+\\\\w+\\\\s*\\\\(.*\\\\bRequestException\\\\b', '.')",
  "key": "[\"grep\", [\"^\\\\s*class\\\\s+\\\\w+\\\\s*\\\\(.*\\\\bRequestException\\\\b\", \".\"]]",
  "provenance": "subclass lines naming `RequestException` under `.` (derived)",
  "v2": [
   1736765483,
   1200820881
  ]
 },
 "forecast": {
  "zero": [
   34,
   39
  ],
  "mid": [
   1,
   13
  ],
  "cap": [
   2,
   39
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
    34,
    39
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
   "pattern": "^\\s*class\\s+\\w+\\s*\\(.*\\bRequestException\\b",
   "scope": ".",
   "hits": [
    [
     "src/requests/exceptions.py",
     38
    ],
    [
     "src/requests/exceptions.py",
     66
    ],
    [
     "src/requests/exceptions.py",
     70
    ],
    [
     "src/requests/exceptions.py",
     82
    ],
    [
     "src/requests/exceptions.py",
     102
    ],
    [
     "src/requests/exceptions.py",
     106
    ],
    [
     "src/requests/exceptions.py",
     110
    ],
    [
     "src/requests/exceptions.py",
     114
    ],
    [
     "src/requests/exceptions.py",
     118
    ],
    [
     "src/requests/exceptions.py",
     122
    ],
    [
     "src/requests/exceptions.py",
     130
    ],
    [
     "src/requests/exceptions.py",
     134
    ],
    [
     "src/requests/exceptions.py",
     138
    ],
    [
     "src/requests/exceptions.py",
     142
    ],
    [
     "src/requests/exceptions.py",
     146
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
   "src/requests/exceptions.py"
  ],
  "table": [
   [
    "src/requests/exceptions.py",
    "src/requests/exceptions.py:38:InvalidJSONError",
    "in",
    "base `RequestException` resolves to the target"
   ],
   [
    "src/requests/exceptions.py",
    "src/requests/exceptions.py:66:HTTPError",
    "in",
    "base `RequestException` resolves to the target"
   ],
   [
    "src/requests/exceptions.py",
    "src/requests/exceptions.py:70:ConnectionError",
    "in",
    "base `RequestException` resolves to the target"
   ],
   [
    "src/requests/exceptions.py",
    "src/requests/exceptions.py:82:Timeout",
    "in",
    "base `RequestException` resolves to the target"
   ],
   [
    "src/requests/exceptions.py",
    "src/requests/exceptions.py:102:URLRequired",
    "in",
    "base `RequestException` resolves to the target"
   ],
   [
    "src/requests/exceptions.py",
    "src/requests/exceptions.py:106:TooManyRedirects",
    "in",
    "base `RequestException` resolves to the target"
   ],
   [
    "src/requests/exceptions.py",
    "src/requests/exceptions.py:110:MissingSchema",
    "in",
    "base `RequestException` resolves to the target"
   ],
   [
    "src/requests/exceptions.py",
    "src/requests/exceptions.py:114:InvalidSchema",
    "in",
    "base `RequestException` resolves to the target"
   ],
   [
    "src/requests/exceptions.py",
    "src/requests/exceptions.py:118:InvalidURL",
    "in",
    "base `RequestException` resolves to the target"
   ],
   [
    "src/requests/exceptions.py",
    "src/requests/exceptions.py:122:InvalidHeader",
    "in",
    "base `RequestException` resolves to the target"
   ],
   [
    "src/requests/exceptions.py",
    "src/requests/exceptions.py:130:ChunkedEncodingError",
    "in",
    "base `RequestException` resolves to the target"
   ],
   [
    "src/requests/exceptions.py",
    "src/requests/exceptions.py:134:ContentDecodingError",
    "in",
    "base `RequestException` resolves to the target"
   ],
   [
    "src/requests/exceptions.py",
    "src/requests/exceptions.py:138:StreamConsumedError",
    "in",
    "base `RequestException` resolves to the target"
   ],
   [
    "src/requests/exceptions.py",
    "src/requests/exceptions.py:142:RetryError",
    "in",
    "base `RequestException` resolves to the target"
   ],
   [
    "src/requests/exceptions.py",
    "src/requests/exceptions.py:146:UnrewindableBodyError",
    "in",
    "base `RequestException` resolves to the target"
   ]
  ],
  "uncovered": {
   "SUBCLASS": []
  },
  "n_in": 15,
  "n_out": 0,
  "n_pending": 0
 }
}
```
</details>

## Final

`RequestException` is the class at `src/requests/exceptions.py:20`. 15 classes derive from it directly: `InvalidJSONError` (`src/requests/exceptions.py:38`), `HTTPError` (`src/requests/exceptions.py:66`), `ConnectionError` (`src/requests/exceptions.py:70`), `Timeout` (`src/requests/exceptions.py:82`), `URLRequired` (`src/requests/exceptions.py:102`), `TooManyRedirects` (`src/requests/exceptions.py:106`), `MissingSchema` (`src/requests/exceptions.py:110`), `InvalidSchema` (`src/requests/exceptions.py:114`) and 7 more. Looking back, all 3 calls were needed.

**Answer:** `{"final_kind": "subclasses", "final": ["src/requests/exceptions.py:38:InvalidJSONError", "src/requests/exceptions.py:66:HTTPError", "src/requests/exceptions.py:70:ConnectionError", "src/requests/exceptions.py:82:Timeout", "src/requests/exceptions.py:102:URLRequired", "src/requests/exceptions.py:106:TooManyRedirects", "src/requests/exceptions.py:110:MissingSchema", "src/requests/exceptions.py:114:InvalidSchema", "src/requests/exceptions.py:118:InvalidURL", "src/requests/exceptions.py:122:InvalidHeader", "src/requests/exceptions.py:130:ChunkedEncodingError", "src/requests/exceptions.py:134:ContentDecodingError", "src/requests/exceptions.py:138:StreamConsumedError", "src/requests/exceptions.py:142:RetryError", "src/requests/exceptions.py:146:UnrewindableBodyError"], "steps": [{"op": "resolve", "output": {"kind": "def", "path": "src/requests/exceptions.py", "line": 20, "name": "RequestException", "detail": "class"}}, {"op": "subclasses", "output": ["src/requests/exceptions.py:38:InvalidJSONError", "src/requests/exceptions.py:66:HTTPError", "src/requests/exceptions.py:70:ConnectionError", "src/requests/exceptions.py:82:Timeout", "src/requests/exceptions.py:102:URLRequired", "src/requests/exceptions.py:106:TooManyRedirects", "src/requests/exceptions.py:110:MissingSchema", "src/requests/exceptions.py:114:InvalidSchema", "src/requests/exceptions.py:118:InvalidURL", "src/requests/exceptions.py:122:InvalidHeader", "src/requests/exceptions.py:130:ChunkedEncodingError", "src/requests/exc`  
**Stopped:** certificate after 3 calls