# httpx-not_overriding-e47ffae3

**Repository:** httpx  
**Chain:** subclasses → not_overriding  
**Seed:** 0, prior 708591d2904e1ac3, floor 19

## Task

`SyncByteStream` is defined at `httpx/_types.py:92` (class). Among those subclasses, which do not define `close` themselves? Same format.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N; bindings take effect in source order. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. A class derives from a definition when a base written as a bare name or `module.Name` resolves to it. A call site is `name(...)` where the bare name refers to the module-level binding (not a parameter or local). Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

Starting from the definition of `SyncByteStream` at `httpx/_types.py:92`. Then, among its subclasses, the ones that do not define `close` themselves.

Next I will search the whole tree for classes deriving from `SyncByteStream`; the search has to be complete before I can call the set final. Very likely nothing turns up. If it caps or it fits under the cap, I follow whatever it opens up.

**Call:** `grep('^\\s*class\\s+\\w+\\s*\\(.*\\bSyncByteStream\\b', '.')`

**Response**: outcome `mid`

```
httpx/_client.py:139:class BoundSyncStream(SyncByteStream):
httpx/_content.py:31:class ByteStream(AsyncByteStream, SyncByteStream):
httpx/_content.py:42:class IteratorByteStream(SyncByteStream):
httpx/_content.py:92:class UnattachedStream(AsyncByteStream, SyncByteStream):
httpx/_multipart.py:224:class MultipartStream(SyncByteStream, AsyncByteStream):
httpx/_transports/default.py:121:class ResponseStream(SyncByteStream):
httpx/_transports/wsgi.py:30:class WSGIByteStream(SyncByteStream):
tests/test_api.py:34:    class Data(httpx.SyncByteStream):
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
   "desc": "search `.` for classes deriving from `SyncByteStream`"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*class\\\\s+\\\\w+\\\\s*\\\\(.*\\\\bSyncByteStream\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*class\\\\s+\\\\w+\\\\s*\\\\(.*\\\\bSyncByteStream\\\\b\", \".\"]]",
   "v1": [
    155909037577,
    104447967624
   ],
   "v2": [
    155909037577,
    104447967624
   ],
   "p_cap": [
    1,
    18
   ],
   "forecast": {
    "zero": [
     8,
     9
    ],
    "mid": [
     1,
     18
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
  "call": "grep('^\\\\s*class\\\\s+\\\\w+\\\\s*\\\\(.*\\\\bSyncByteStream\\\\b', '.')",
  "key": "[\"grep\", [\"^\\\\s*class\\\\s+\\\\w+\\\\s*\\\\(.*\\\\bSyncByteStream\\\\b\", \".\"]]",
  "provenance": "subclass lines naming `SyncByteStream` under `.` (derived)",
  "v2": [
   155909037577,
   104447967624
  ]
 },
 "forecast": {
  "zero": [
   8,
   9
  ],
  "mid": [
   1,
   18
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
    8,
    9
   ]
  }
 ],
 "adherence": null,
 "facts": [
  {
   "kind": "grep",
   "step": 1,
   "pattern": "^\\s*class\\s+\\w+\\s*\\(.*\\bSyncByteStream\\b",
   "scope": ".",
   "hits": [
    [
     "httpx/_client.py",
     139
    ],
    [
     "httpx/_content.py",
     31
    ],
    [
     "httpx/_content.py",
     42
    ],
    [
     "httpx/_content.py",
     92
    ],
    [
     "httpx/_multipart.py",
     224
    ],
    [
     "httpx/_transports/default.py",
     121
    ],
    [
     "httpx/_transports/wsgi.py",
     30
    ],
    [
     "tests/test_api.py",
     34
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "phase": "subclasses",
  "step": 1,
  "of": 2,
  "candidates": [
   "httpx/_client.py",
   "httpx/_content.py",
   "httpx/_multipart.py",
   "httpx/_transports/default.py",
   "httpx/_transports/wsgi.py",
   "tests/test_api.py"
  ],
  "table": [
   [
    "httpx/_client.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "httpx/_content.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "httpx/_multipart.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "httpx/_transports/default.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "httpx/_transports/wsgi.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_api.py",
    null,
    "pending",
    "not yet examined"
   ]
  ],
  "uncovered": {
   "SUBCLASS": []
  },
  "n_in": 0,
  "n_out": 0,
  "n_pending": 6
 }
}
```
</details>

## Step 2

Huh: 8 matching lines anywhere for classes deriving from `SyncByteStream`, in `httpx/_client.py`, `httpx/_content.py`, `httpx/_multipart.py`, `httpx/_transports/default.py` and 2 more files, and the search was under the cap, so that is the complete set there.

I'll look at `httpx/_transports/default.py`'s top-level names for `SyncByteStream`; the outline lists each class with its bases. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `httpx/_client.py`'s top-level names for `SyncByteStream`.

**Call:** `symbols('httpx/_transports/default.py', 'SyncByteStream')`

**Response**: outcome `ok`

```
module httpx/_transports/default.py lines=407 dynamic=no all=static@69
56 from SyncByteStream <- .._types SyncByteStream
121 class ResponseStream (SyncByteStream)
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
    "SyncByteStream"
   ],
   "desc": "look at the classes in `httpx/_client.py` that derive from `SyncByteStream`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_content.py",
    "SyncByteStream"
   ],
   "desc": "look at the classes in `httpx/_content.py` that derive from `SyncByteStream`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_multipart.py",
    "SyncByteStream"
   ],
   "desc": "look at the classes in `httpx/_multipart.py` that derive from `SyncByteStream`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_transports/default.py",
    "SyncByteStream"
   ],
   "desc": "look at the classes in `httpx/_transports/default.py` that derive from `SyncByteStream`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_transports/wsgi.py",
    "SyncByteStream"
   ],
   "desc": "look at the classes in `httpx/_transports/wsgi.py` that derive from `SyncByteStream`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_api.py",
    "SyncByteStream"
   ],
   "desc": "look at the classes in `tests/test_api.py` that derive from `SyncByteStream`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/_client.py', 'SyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_client.py\", \"SyncByteStream\"]]",
   "v1": [
    63426647,
    6587350
   ],
   "v2": [
    31779197,
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
     "SyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_content.py', 'SyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_content.py\", \"SyncByteStream\"]]",
   "v1": [
    63426647,
    6587350
   ],
   "v2": [
    31779197,
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
     "httpx/_content.py",
     "SyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_multipart.py', 'SyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_multipart.py\", \"SyncByteStream\"]]",
   "v1": [
    63426647,
    6587350
   ],
   "v2": [
    31779197,
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
     "httpx/_multipart.py",
     "SyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/default.py', 'SyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/default.py\", \"SyncByteStream\"]]",
   "v1": [
    63426647,
    6587350
   ],
   "v2": [
    31779197,
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
     "httpx/_transports/default.py",
     "SyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/wsgi.py', 'SyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/wsgi.py\", \"SyncByteStream\"]]",
   "v1": [
    63426647,
    6587350
   ],
   "v2": [
    31779197,
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
     "httpx/_transports/wsgi.py",
     "SyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_api.py', 'SyncByteStream')",
   "key": "[\"symbols\", [\"tests/test_api.py\", \"SyncByteStream\"]]",
   "v1": [
    63426647,
    6587350
   ],
   "v2": [
    31779197,
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
     "tests/test_api.py",
     "SyncByteStream"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('httpx/_transports/default.py', 'SyncByteStream')",
  "key": "[\"symbols\", [\"httpx/_transports/default.py\", \"SyncByteStream\"]]",
  "provenance": "`httpx/_transports/default.py` had a matching line (step 1); its outline names every `SyncByteStream` import exactly",
  "v2": [
   31779197,
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
  "ok": "[\"symbols\", [\"httpx/_client.py\", \"SyncByteStream\"]]",
  "cap": "[\"symbols\", [\"httpx/_client.py\", \"SyncByteStream\"]]"
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
   "path": "httpx/_transports/default.py",
   "filter": "SyncByteStream",
   "header": {
    "lines": 407,
    "dynamic": false,
    "all_status": "static",
    "all_line": 69
   },
   "bindings": [
    {
     "module": "httpx/_transports/default.py",
     "name": "SyncByteStream",
     "line": 56,
     "kind": "from",
     "src": ".._types",
     "src_name": "SyncByteStream",
     "conditional": false,
     "col": 0,
     "bases": []
    },
    {
     "module": "httpx/_transports/default.py",
     "name": "ResponseStream",
     "line": 121,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "SyncByteStream"
     ]
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "subclasses",
  "step": 1,
  "of": 2,
  "candidates": [
   "httpx/_client.py",
   "httpx/_content.py",
   "httpx/_multipart.py",
   "httpx/_transports/default.py",
   "httpx/_transports/wsgi.py",
   "tests/test_api.py"
  ],
  "table": [
   [
    "httpx/_client.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "httpx/_content.py",
    null,
    "pending",
    "not y
```
</details>

## Step 3

`httpx/_transports/default.py` has `class ResponseStream(SyncByteStream)` at line 121. It gets `SyncByteStream` from `.._types` (line 56), which is what the base name resolves through.

Tally: 0 subclasses confirmed, 0 ruled out, 6 pending. The search itself is complete; what is left is checking the candidates.

I'll look at `httpx/_client.py`'s top-level names for `SyncByteStream`; the outline lists each class with its bases. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `httpx/_types.py`'s top-level names for `SyncByteStream`.

**Call:** `symbols('httpx/_client.py', 'SyncByteStream')`

**Response**: outcome `ok`

```
module httpx/_client.py lines=2020 dynamic=no all=static@54
33 from SyncByteStream <- ._types SyncByteStream
139 class BoundSyncStream (SyncByteStream)
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
    "SyncByteStream"
   ],
   "desc": "look at the classes in `httpx/_client.py` that derive from `SyncByteStream`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_content.py",
    "SyncByteStream"
   ],
   "desc": "look at the classes in `httpx/_content.py` that derive from `SyncByteStream`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_multipart.py",
    "SyncByteStream"
   ],
   "desc": "look at the classes in `httpx/_multipart.py` that derive from `SyncByteStream`"
  },
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "httpx/_types.py",
    "SyncByteStream"
   ],
   "desc": "check the top-level names of `httpx/_types.py` for `SyncByteStream`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_transports/wsgi.py",
    "SyncByteStream"
   ],
   "desc": "look at the classes in `httpx/_transports/wsgi.py` that derive from `SyncByteStream`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_api.py",
    "SyncByteStream"
   ],
   "desc": "look at the classes in `tests/test_api.py` that derive from `SyncByteStream`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/_client.py', 'SyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_client.py\", \"SyncByteStream\"]]",
   "v1": [
    943823772439,
    103829810700
   ],
   "v2": [
    943823772439,
    103829810700
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
     "SyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_content.py', 'SyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_content.py\", \"SyncByteStream\"]]",
   "v1": [
    943823772439,
    103829810700
   ],
   "v2": [
    943823772439,
    103829810700
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
     "httpx/_content.py",
     "SyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_multipart.py', 'SyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_multipart.py\", \"SyncByteStream\"]]",
   "v1": [
    943823772439,
    103829810700
   ],
   "v2": [
    943823772439,
    103829810700
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
     "httpx/_multipart.py",
     "SyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/wsgi.py', 'SyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/wsgi.py\", \"SyncByteStream\"]]",
   "v1": [
    943823772439,
    103829810700
   ],
   "v2": [
    943823772439,
    103829810700
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
     "httpx/_transports/wsgi.py",
     "SyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_types.py', 'SyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_types.py\", \"SyncByteStream\"]]",
   "v1": [
    37669887049,
    4153192428
   ],
   "v2": [
    943823772439,
    103829810700
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     395,
     426
    ],
    "reexport": [
     2,
     71
    ],
    "star": [
     1,
     426
    ],
    "none": [
     3,
     71
    ]
   },
   "serves": [
    [
     "bindings",
     "httpx/_types.py",
     "SyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_api.py', 'SyncByteStream')",
   "key": "[\"symbols\", [\"tests/test_api.py\", \"SyncByteStream\"]]",
   "v1": [
    943823772439,
    103829810700
   ],
   "v2": [
    943823772439,
    103829810700
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
     "tests/test_api.py",
     "SyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_types.py')",
   "key": "[\"symbols\", [\"httpx/_types.py\"]]",
   "v1": [
    2637985335709,
    286570277532
   ],
   "v2": [
    66073536966827,
    7164256938300
   ],
   "p_cap": [
    28,
    207
   ],
   "forecast": {
    "def": [
     70705,
     88182
    ],
    "reexport": [
     358,
     14697
    ],
    "star": [
     179,
     88182
    ],
    "none": [
     179,
     4899
    ],
    "cap": [
     28,
     207
    ]
   },
   "serves": [
    [
     "bindings",
     "httpx/_types.py",
     "SyncByteStream"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('httpx/_client.py', 'SyncByteStream')",
  "key": "[\"symbols\", [\"httpx/_client.py\", \"SyncByteStream\"]]",
  "provenance": "`httpx/_client.py` had a matching line (step 1); its outline names every `SyncByteStream` import exactly",
  "v2": [
   943823772439,
   103829810700
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
  "ok": "[\"symbols\", [\"httpx/_types.py\", \"SyncByteStream\"]]",
  "cap": "[\"symbols\", [\"httpx/_types.py\", \"SyncByteStream\"]]"
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
  "planned": "[\"symbols\", [\"httpx/_client.py\", \"SyncByteStream\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 3,
   "path": "httpx/_client.py",
   "filter": "SyncByteStream",
   "header": {
    "lines": 2020,
    "dynamic": false,
    "all_status": "static",
    "all_line": 54
   },
   "bindings": [
    {
     "module": "httpx/_client.py",
     "name": "SyncByteStream",
     "line": 33,
     "kind": "from",
     "src": "._types",
     "src_name": "SyncByteStream",
     "conditional": false,
     "col": 0,
     "bases": []
    },
    {
     "module": "h
```
</details>

## Step 4

`httpx/_client.py` has `class BoundSyncStream(SyncByteStream)` at line 139. It gets `SyncByteStream` from `._types` (line 33), which is what the base name resolves through.

Tally: 0 subclasses confirmed, 0 ruled out, 6 pending. The search itself is complete; what is left is checking the candidates.

Still open: check the top-level names of `httpx/_types.py` for `SyncByteStream`; look at the classes in `httpx/_content.py` that derive from `SyncByteStream`; look at the classes in `httpx/_multipart.py` that derive from `SyncByteStream`; and 2 more.

I'll look at `httpx/_types.py`'s top-level names for `SyncByteStream`; that settles what the name means there. Almost certainly it is defined right there. If the name is not bound there or it is re-exported from somewhere else, I will look at `httpx/_content.py`'s top-level names for `SyncByteStream`.

**Call:** `symbols('httpx/_types.py', 'SyncByteStream')`

**Response**: outcome `def`

```
module httpx/_types.py lines=115 dynamic=no all=static@89
92 class SyncByteStream ()
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "httpx/_types.py",
    "SyncByteStream"
   ],
   "desc": "check the top-level names of `httpx/_types.py` for `SyncByteStream`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_content.py",
    "SyncByteStream"
   ],
   "desc": "look at the classes in `httpx/_content.py` that derive from `SyncByteStream`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_multipart.py",
    "SyncByteStream"
   ],
   "desc": "look at the classes in `httpx/_multipart.py` that derive from `SyncByteStream`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_transports/wsgi.py",
    "SyncByteStream"
   ],
   "desc": "look at the classes in `httpx/_transports/wsgi.py` that derive from `SyncByteStream`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_api.py",
    "SyncByteStream"
   ],
   "desc": "look at the classes in `tests/test_api.py` that derive from `SyncByteStream`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/_content.py', 'SyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_content.py\", \"SyncByteStream\"]]",
   "v1": [
    777548070139,
    103829810700
   ],
   "v2": [
    777548070139,
    103829810700
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
     "httpx/_content.py",
     "SyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_multipart.py', 'SyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_multipart.py\", \"SyncByteStream\"]]",
   "v1": [
    777548070139,
    103829810700
   ],
   "v2": [
    777548070139,
    103829810700
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
     "httpx/_multipart.py",
     "SyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/wsgi.py', 'SyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/wsgi.py\", \"SyncByteStream\"]]",
   "v1": [
    777548070139,
    103829810700
   ],
   "v2": [
    777548070139,
    103829810700
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
     "httpx/_transports/wsgi.py",
     "SyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_types.py', 'SyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_types.py\", \"SyncByteStream\"]]",
   "v1": [
    31018858957,
    4153192428
   ],
   "v2": [
    777548070139,
    103829810700
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     395,
     426
    ],
    "reexport": [
     2,
     71
    ],
    "star": [
     1,
     426
    ],
    "none": [
     3,
     71
    ]
   },
   "serves": [
    [
     "bindings",
     "httpx/_types.py",
     "SyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_api.py', 'SyncByteStream')",
   "key": "[\"symbols\", [\"tests/test_api.py\", \"SyncByteStream\"]]",
   "v1": [
    777548070139,
    103829810700
   ],
   "v2": [
    777548070139,
    103829810700
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
     "tests/test_api.py",
     "SyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_types.py')",
   "key": "[\"symbols\", [\"httpx/_types.py\"]]",
   "v1": [
    2179064397361,
    286570277532
   ],
   "v2": [
    54600513508127,
    7164256938300
   ],
   "p_cap": [
    28,
    207
   ],
   "forecast": {
    "def": [
     70705,
     88182
    ],
    "reexport": [
     358,
     14697
    ],
    "star": [
     179,
     88182
    ],
    "none": [
     179,
     4899
    ],
    "cap": [
     28,
     207
    ]
   },
   "serves": [
    [
     "bindings",
     "httpx/_types.py",
     "SyncByteStream"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('httpx/_types.py', 'SyncByteStream')",
  "key": "[\"symbols\", [\"httpx/_types.py\", \"SyncByteStream\"]]",
  "provenance": "module `httpx/_types.py` (task), name `SyncByteStream` (task)",
  "v2": [
   777548070139,
   103829810700
  ]
 },
 "forecast": {
  "def": [
   395,
   426
  ],
  "reexport": [
   2,
   71
  ],
  "star": [
   1,
   426
  ],
  "none": [
   3,
   71
  ]
 },
 "plan": {
  "def": "[\"symbols\", [\"httpx/_content.py\", \"SyncByteStream\"]]",
  "reexport": "[\"symbols\", [\"httpx/_content.py\", \"SyncByteStream\"]]",
  "star": "[\"symbols\", [\"httpx/_content.py\", \"SyncByteStream\"]]",
  "none": "[\"symbols\", [\"httpx/_content.py\", \"SyncByteStream\"]]"
 },
 "hedges": [
  {
   "outcome": "def",
   "word": "almost certainly",
   "p": [
    395,
    426
   ]
  }
 ],
 "adherence": {
  "planned": "[\"symbols\", [\"httpx/_types.py\", \"SyncByteStream\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 4,
   "path": "httpx/_types.py",
   "filter": "SyncByteStream",
   "header": {
    "lines": 115,
    "dynamic": false,
    "all_status": "static",
    "all_line": 89
   },
   "bindings": [
    {
     "module": "httpx/_types.py",
     "name": "SyncByteStream",
     "line": 92,
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
  "phase": "subclasses",
  "step": 1,
  "of": 2,
  "candidates": [
   "httpx/_client.py",
   "httpx/_content.py",
   "httpx/_multipart.py",
   "httpx/_transports/default.py",
   "httpx/_transports/wsgi.py",
   "tests/test_api.py"
  ],
  "table": [
   [
    "httpx/_client.py",
    "httpx/_client.py:139:BoundSyncStream",
    "in",
    "base `SyncByteStream` resolves to the target"
   ],
   [
    "httpx/_content.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
  
```
</details>

## Step 5

There it is: `SyncByteStream` is a class at `httpx/_types.py:92`.

Tally: 2 subclasses confirmed, 0 ruled out, 4 pending. The search itself is complete; what is left is checking the candidates.

Let me look at `httpx/_content.py`'s top-level names for `SyncByteStream`; the outline lists each class with its bases. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `httpx/_multipart.py`'s top-level names for `SyncByteStream`.

**Call:** `symbols('httpx/_content.py', 'SyncByteStream')`

**Response**: outcome `ok`

```
module httpx/_content.py lines=241 dynamic=no all=static@28
18 from SyncByteStream <- ._types SyncByteStream
31 class ByteStream (AsyncByteStream,SyncByteStream)
42 class IteratorByteStream (SyncByteStream)
92 class UnattachedStream (AsyncByteStream,SyncByteStream)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_content.py",
    "SyncByteStream"
   ],
   "desc": "look at the classes in `httpx/_content.py` that derive from `SyncByteStream`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_multipart.py",
    "SyncByteStream"
   ],
   "desc": "look at the classes in `httpx/_multipart.py` that derive from `SyncByteStream`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_transports/wsgi.py",
    "SyncByteStream"
   ],
   "desc": "look at the classes in `httpx/_transports/wsgi.py` that derive from `SyncByteStream`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_api.py",
    "SyncByteStream"
   ],
   "desc": "look at the classes in `tests/test_api.py` that derive from `SyncByteStream`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/_content.py', 'SyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_content.py\", \"SyncByteStream\"]]",
   "v1": [
    42328347,
    6587350
   ],
   "v2": [
    21230047,
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
     "httpx/_content.py",
     "SyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_multipart.py', 'SyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_multipart.py\", \"SyncByteStream\"]]",
   "v1": [
    42328347,
    6587350
   ],
   "v2": [
    21230047,
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
     "httpx/_multipart.py",
     "SyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/wsgi.py', 'SyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/wsgi.py\", \"SyncByteStream\"]]",
   "v1": [
    42328347,
    6587350
   ],
   "v2": [
    21230047,
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
     "httpx/_transports/wsgi.py",
     "SyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_api.py', 'SyncByteStream')",
   "key": "[\"symbols\", [\"tests/test_api.py\", \"SyncByteStream\"]]",
   "v1": [
    42328347,
    6587350
   ],
   "v2": [
    21230047,
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
     "tests/test_api.py",
     "SyncByteStream"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('httpx/_content.py', 'SyncByteStream')",
  "key": "[\"symbols\", [\"httpx/_content.py\", \"SyncByteStream\"]]",
  "provenance": "`httpx/_content.py` had a matching line (step 1); its outline names every `SyncByteStream` import exactly",
  "v2": [
   21230047,
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
  "ok": "[\"symbols\", [\"httpx/_multipart.py\", \"SyncByteStream\"]]",
  "cap": "[\"symbols\", [\"httpx/_multipart.py\", \"SyncByteStream\"]]"
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
  "planned": "[\"symbols\", [\"httpx/_content.py\", \"SyncByteStream\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 5,
   "path": "httpx/_content.py",
   "filter": "SyncByteStream",
   "header": {
    "lines": 241,
    "dynamic": false,
    "all_status": "static",
    "all_line": 28
   },
   "bindings": [
    {
     "module": "httpx/_content.py",
     "name": "SyncByteStream",
     "line": 18,
     "kind": "from",
     "src": "._types",
     "src_name": "SyncByteStream",
     "conditional": false,
     "col": 0,
     "bases": []
    },
    {
     "module": "httpx/_content.py",
     "name": "ByteStream",
     "line": 31,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "AsyncByteStream",
      "SyncByteStream"
     ]
    },
    {
     "module": "httpx/_content.py",
     "name": "IteratorByteStream",
     "line": 42,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "SyncByteStream"
     ]
    },
    {
     "module": "httpx/_content.py",
     "name": "UnattachedStream",
     "line": 92,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "AsyncByteStream",
      "SyncByteStream"
     ]
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "subclasses",
  "step": 1,
  "of": 2,
  "candidates": [
   "httpx/_client.py",
   "httpx/_content.py",
   "httpx/_multipart.py",
   "httpx/_transports/default.py",
   "httpx/_transports/wsgi.py",
   "tests/test_api.py"
  ],
  "table": [
   [
    "httpx/_client.py",
    "httpx/_client.py:139:BoundSyncStream",
    "in",
    "base `SyncByteStream` resolves to the target"
   ],
   [
    "httpx/_content.py",
    "httpx/_content.py:31:ByteStream",
    "in",
    "base `SyncByteStream` resolves to the target"
   ],
   [
    "httpx/_content.py",
    "httpx/_content.py:42:IteratorByteStream",
    "in",
    "base `SyncByteStream` resolves to the target"
   ],
   [
    "httpx/_content.py",
    "httpx/_content.py:92:UnattachedStream",
    "in",
    "base `SyncByteStream` resolves to the target"
   ],
   [
    "httpx/_multipart.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "httpx/_transports/default.py",
    "httpx/_transports/default.py:121:ResponseStream",
    "in",
    "base `SyncByteStream` resolves to the target"
   ],
   [
    "httpx/_transports/wsgi.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_api.py",
    null,
    "pending",
    "not y
```
</details>

## Step 6

`httpx/_content.py` has `class ByteStream(AsyncByteStream,SyncByteStream)` at line 31; `class IteratorByteStream(SyncByteStream)` at line 42; `class UnattachedStream(AsyncByteStream,SyncByteStream)` at line 92. It gets `SyncByteStream` from `._types` (line 18), which is what the base name resolves through.

Tally: 5 subclasses confirmed, 0 ruled out, 3 pending. The search itself is complete; what is left is checking the candidates.

Next I will look at `httpx/_multipart.py`'s top-level names for `SyncByteStream`; the outline lists each class with its bases. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `httpx/_transports/wsgi.py`'s top-level names for `SyncByteStream`.

**Call:** `symbols('httpx/_multipart.py', 'SyncByteStream')`

**Response**: outcome `ok`

```
module httpx/_multipart.py lines=301 dynamic=no all=none
10 from SyncByteStream <- ._types SyncByteStream
224 class MultipartStream (SyncByteStream,AsyncByteStream)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_multipart.py",
    "SyncByteStream"
   ],
   "desc": "look at the classes in `httpx/_multipart.py` that derive from `SyncByteStream`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_transports/wsgi.py",
    "SyncByteStream"
   ],
   "desc": "look at the classes in `httpx/_transports/wsgi.py` that derive from `SyncByteStream`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_api.py",
    "SyncByteStream"
   ],
   "desc": "look at the classes in `tests/test_api.py` that derive from `SyncByteStream`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/_multipart.py', 'SyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_multipart.py\", \"SyncByteStream\"]]",
   "v1": [
    31779197,
    6587350
   ],
   "v2": [
    15955472,
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
     "httpx/_multipart.py",
     "SyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/wsgi.py', 'SyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/wsgi.py\", \"SyncByteStream\"]]",
   "v1": [
    31779197,
    6587350
   ],
   "v2": [
    15955472,
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
     "httpx/_transports/wsgi.py",
     "SyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_api.py', 'SyncByteStream')",
   "key": "[\"symbols\", [\"tests/test_api.py\", \"SyncByteStream\"]]",
   "v1": [
    31779197,
    6587350
   ],
   "v2": [
    15955472,
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
     "tests/test_api.py",
     "SyncByteStream"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('httpx/_multipart.py', 'SyncByteStream')",
  "key": "[\"symbols\", [\"httpx/_multipart.py\", \"SyncByteStream\"]]",
  "provenance": "`httpx/_multipart.py` had a matching line (step 1); its outline names every `SyncByteStream` import exactly",
  "v2": [
   15955472,
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
  "ok": "[\"symbols\", [\"httpx/_transports/wsgi.py\", \"SyncByteStream\"]]",
  "cap": "[\"symbols\", [\"httpx/_transports/wsgi.py\", \"SyncByteStream\"]]"
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
  "planned": "[\"symbols\", [\"httpx/_multipart.py\", \"SyncByteStream\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 6,
   "path": "httpx/_multipart.py",
   "filter": "SyncByteStream",
   "header": {
    "lines": 301,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "httpx/_multipart.py",
     "name": "SyncByteStream",
     "line": 10,
     "kind": "from",
     "src": "._types",
     "src_name": "SyncByteStream",
     "conditional": false,
     "col": 0,
     "bases": []
    },
    {
     "module": "httpx/_multipart.py",
     "name": "MultipartStream",
     "line": 224,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "SyncByteStream",
      "AsyncByteStream"
     ]
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "subclasses",
  "step": 1,
  "of": 2,
  "candidates": [
   "httpx/_client.py",
   "httpx/_content.py",
   "httpx/_multipart.py",
   "httpx/_transports/default.py",
   "httpx/_transports/wsgi.py",
   "tests/test_api.py"
  ],
  "table": [
   [
    "httpx/_client.py",
    "httpx/_client.py:139:BoundSyncStream",
    "in",
    "base `SyncByteStream` resolves to the target"
   ],
   [
    "httpx/_content.py",
    "httpx/_content.py:31:ByteStream",
    "in",
    "base `SyncByteStream` resolves to the target"
   ],
   [
    "httpx/_content.py",
    "httpx/_content.py:42:IteratorByteStream",
    "in",
    "base `SyncByteStream` resolves to the target"
   ],
   [
    "httpx/_content.py",
    "httpx/_content.py:92:UnattachedStream",
    "in",
    "base `SyncByteStream` resolves to the target"
   ],
   [
    "httpx/_multipart.py",
    "httpx/_multipart.py:224:MultipartStream",
    "in",
    "base `SyncByteStream` resolves to the target"
   ],
   [
    "httpx/_transports/default.py",
    "httpx/_transports/default.py:121:ResponseStream",
    "in",
    "base `SyncByteStream` resolves to the target"
   ],
   [
    "httpx/_transports/wsgi.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_api.py",
    null,
    "pending",
    "not yet examined"
   ]
  ],
  "uncovered": {
   "SUBCLASS": []
  },
  "n_in": 6,
  "n_out": 0,
  "n_pending": 2
 }
}
```
</details>

## Step 7

`httpx/_multipart.py` has `class MultipartStream(SyncByteStream,AsyncByteStream)` at line 224. It gets `SyncByteStream` from `._types` (line 10), which is what the base name resolves through.

Tally: 6 subclasses confirmed, 0 ruled out, 2 pending. The search itself is complete; what is left is checking the candidates.

Next I will look at `httpx/_transports/wsgi.py`'s top-level names for `SyncByteStream`; the outline lists each class with its bases. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `tests/test_api.py`'s top-level names for `SyncByteStream`.

**Call:** `symbols('httpx/_transports/wsgi.py', 'SyncByteStream')`

**Response**: outcome `ok`

```
module httpx/_transports/wsgi.py lines=150 dynamic=no all=static@19
9 from SyncByteStream <- .._types SyncByteStream
30 class WSGIByteStream (SyncByteStream)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_transports/wsgi.py",
    "SyncByteStream"
   ],
   "desc": "look at the classes in `httpx/_transports/wsgi.py` that derive from `SyncByteStream`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_api.py",
    "SyncByteStream"
   ],
   "desc": "look at the classes in `tests/test_api.py` that derive from `SyncByteStream`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/_transports/wsgi.py', 'SyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/wsgi.py\", \"SyncByteStream\"]]",
   "v1": [
    21230047,
    6587350
   ],
   "v2": [
    10680897,
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
     "httpx/_transports/wsgi.py",
     "SyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_api.py', 'SyncByteStream')",
   "key": "[\"symbols\", [\"tests/test_api.py\", \"SyncByteStream\"]]",
   "v1": [
    21230047,
    6587350
   ],
   "v2": [
    10680897,
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
     "tests/test_api.py",
     "SyncByteStream"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('httpx/_transports/wsgi.py', 'SyncByteStream')",
  "key": "[\"symbols\", [\"httpx/_transports/wsgi.py\", \"SyncByteStream\"]]",
  "provenance": "`httpx/_transports/wsgi.py` had a matching line (step 1); its outline names every `SyncByteStream` import exactly",
  "v2": [
   10680897,
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
  "ok": "[\"symbols\", [\"tests/test_api.py\", \"SyncByteStream\"]]",
  "cap": "[\"symbols\", [\"tests/test_api.py\", \"SyncByteStream\"]]"
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
  "planned": "[\"symbols\", [\"httpx/_transports/wsgi.py\", \"SyncByteStream\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 7,
   "path": "httpx/_transports/wsgi.py",
   "filter": "SyncByteStream",
   "header": {
    "lines": 150,
    "dynamic": false,
    "all_status": "static",
    "all_line": 19
   },
   "bindings": [
    {
     "module": "httpx/_transports/wsgi.py",
     "name": "SyncByteStream",
     "line": 9,
     "kind": "from",
     "src": ".._types",
     "src_name": "SyncByteStream",
     "conditional": false,
     "col": 0,
     "bases": []
    },
    {
     "module": "httpx/_transports/wsgi.py",
     "name": "WSGIByteStream",
     "line": 30,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "SyncByteStream"
     ]
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "subclasses",
  "step": 1,
  "of": 2,
  "candidates": [
   "httpx/_client.py",
   "httpx/_content.py",
   "httpx/_multipart.py",
   "httpx/_transports/default.py",
   "httpx/_transports/wsgi.py",
   "tests/test_api.py"
  ],
  "table": [
   [
    "httpx/_client.py",
    "httpx/_client.py:139:BoundSyncStream",
    "in",
    "base `SyncByteStream` resolves to the target"
   ],
   [
    "httpx/_content.py",
    "httpx/_content.py:31:ByteStream",
    "in",
    "base `SyncByteStream` resolves to the target"
   ],
   [
    "httpx/_content.py",
    "httpx/_content.py:42:IteratorByteStream",
    "in",
    "base `SyncByteStream` resolves to the target"
   ],
   [
    "httpx/_content.py",
    "httpx/_content.py:92:UnattachedStream",
    "in",
    "base `SyncByteStream` resolves to the target"
   ],
   [
    "httpx/_multipart.py",
    "httpx/_multipart.py:224:MultipartStream",
    "in",
    "base `SyncByteStream` resolves to the target"
   ],
   [
    "httpx/_transports/default.py",
    "httpx/_transports/default.py:121:ResponseStream",
    "in",
    "base `SyncByteStream` resolves to the target"
   ],
   [
    "httpx/_transports/wsgi.py",
    "httpx/_transports/wsgi.py:30:WSGIByteStream",
    "in",
    "base `SyncByteStream` resolves to the target"
   ],
   [
    "tests/test_api.py",
    null,
    "pending",
    "not yet examined"
   ]
  ],
  "uncovered": {
   "SUBCLASS": []
  },
  "n_in": 7,
  "n_out": 0,
  "n_pending": 1
 }
}
```
</details>

## Step 8

`httpx/_transports/wsgi.py` has `class WSGIByteStream(SyncByteStream)` at line 30. It gets `SyncByteStream` from `.._types` (line 9), which is what the base name resolves through.

Tally: 7 subclasses confirmed, 0 ruled out, 1 pending. The search itself is complete; what is left is checking the candidates.

I'll look at `tests/test_api.py`'s top-level names for `SyncByteStream`; the outline lists each class with its bases. Almost certainly the outline shows what I need. If the outline is too long to fit, I follow whatever it opens up.

**Call:** `symbols('tests/test_api.py', 'SyncByteStream')`

**Response**: outcome `ok`

```
module tests/test_api.py lines=103 dynamic=no all=none
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_api.py",
    "SyncByteStream"
   ],
   "desc": "look at the classes in `tests/test_api.py` that derive from `SyncByteStream`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/test_api.py', 'SyncByteStream')",
   "key": "[\"symbols\", [\"tests/test_api.py\", \"SyncByteStream\"]]",
   "v1": [
    10680897,
    6587350
   ],
   "v2": [
    10680897,
    6587350
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
     "tests/test_api.py",
     "SyncByteStream"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_api.py', 'SyncByteStream')",
  "key": "[\"symbols\", [\"tests/test_api.py\", \"SyncByteStream\"]]",
  "provenance": "`tests/test_api.py` had a matching line (step 1); its outline names every `SyncByteStream` import exactly",
  "v2": [
   10680897,
   6587350
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
  "planned": "[\"symbols\", [\"tests/test_api.py\", \"SyncByteStream\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 8,
   "path": "tests/test_api.py",
   "filter": "SyncByteStream",
   "header": {
    "lines": 103,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "subclasses",
  "step": 1,
  "of": 2,
  "candidates": [
   "httpx/_client.py",
   "httpx/_content.py",
   "httpx/_multipart.py",
   "httpx/_transports/default.py",
   "httpx/_transports/wsgi.py",
   "tests/test_api.py"
  ],
  "table": [
   [
    "httpx/_client.py",
    "httpx/_client.py:139:BoundSyncStream",
    "in",
    "base `SyncByteStream` resolves to the target"
   ],
   [
    "httpx/_content.py",
    "httpx/_content.py:31:ByteStream",
    "in",
    "base `SyncByteStream` resolves to the target"
   ],
   [
    "httpx/_content.py",
    "httpx/_content.py:42:IteratorByteStream",
    "in",
    "base `SyncByteStream` resolves to the target"
   ],
   [
    "httpx/_content.py",
    "httpx/_content.py:92:UnattachedStream",
    "in",
    "base `SyncByteStream` resolves to the target"
   ],
   [
    "httpx/_multipart.py",
    "httpx/_multipart.py:224:MultipartStream",
    "in",
    "base `SyncByteStream` resolves to the target"
   ],
   [
    "httpx/_transports/default.py",
    "httpx/_transports/default.py:121:ResponseStream",
    "in",
    "base `SyncByteStream` resolves to the target"
   ],
   [
    "httpx/_transports/wsgi.py",
    "httpx/_transports/wsgi.py:30:WSGIByteStream",
    "in",
    "base `SyncByteStream` resolves to the target"
   ],
   [
    "tests/test_api.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
   ]
  ],
  "uncovered": {
   "SUBCLASS": []
  },
  "n_in": 7,
  "n_out": 0,
  "n_pending": 0
 }
}
```
</details>

## Step 9

The test module `tests/test_api.py` matched the search, but none of its module-level classes actually derive from `SyncByteStream`; probably a nested class, a comment or a string. That is the full set of subclasses; now which of them lack the method.

Tally: 0 classes without their own method confirmed, 0 ruled out, 7 pending.

Let me check `WSGIByteStream`'s own members in `httpx/_transports/wsgi.py`; only its own members tell me whether it overrides. Almost certainly the members fit. If there are too many members, I will check `BoundSyncStream`'s own members in `httpx/_client.py`.

**Call:** `members('httpx/_transports/wsgi.py', 'WSGIByteStream')`

**Response**: outcome `ok`

```
class WSGIByteStream in httpx/_transports/wsgi.py definitions=1
31 def __init__
35 def __iter__
39 def close
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "members",
   "key": [
    "members",
    "httpx/_client.py",
    "BoundSyncStream"
   ],
   "desc": "look at what `BoundSyncStream` in `httpx/_client.py` defines itself"
  },
  {
   "kind": "members",
   "key": [
    "members",
    "httpx/_content.py",
    "ByteStream"
   ],
   "desc": "look at what `ByteStream` in `httpx/_content.py` defines itself"
  },
  {
   "kind": "members",
   "key": [
    "members",
    "httpx/_content.py",
    "IteratorByteStream"
   ],
   "desc": "look at what `IteratorByteStream` in `httpx/_content.py` defines itself"
  },
  {
   "kind": "members",
   "key": [
    "members",
    "httpx/_content.py",
    "UnattachedStream"
   ],
   "desc": "look at what `UnattachedStream` in `httpx/_content.py` defines itself"
  },
  {
   "kind": "members",
   "key": [
    "members",
    "httpx/_multipart.py",
    "MultipartStream"
   ],
   "desc": "look at what `MultipartStream` in `httpx/_multipart.py` defines itself"
  },
  {
   "kind": "members",
   "key": [
    "members",
    "httpx/_transports/default.py",
    "ResponseStream"
   ],
   "desc": "look at what `ResponseStream` in `httpx/_transports/default.py` defines itself"
  },
  {
   "kind": "members",
   "key": [
    "members",
    "httpx/_transports/wsgi.py",
    "WSGIByteStream"
   ],
   "desc": "look at what `WSGIByteStream` in `httpx/_transports/wsgi.py` defines itself"
  }
 ],
 "candidates": [
  {
   "call": "members('httpx/_client.py', 'BoundSyncStream')",
   "key": "[\"members\", [\"httpx/_client.py\", \"BoundSyncStream\"]]",
   "v1": [
    141,
    20
   ],
   "v2": [
    71,
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
     "members",
     "httpx/_client.py",
     "BoundSyncStream"
    ]
   ]
  },
  {
   "call": "members('httpx/_content.py', 'ByteStream')",
   "key": "[\"members\", [\"httpx/_content.py\", \"ByteStream\"]]",
   "v1": [
    141,
    20
   ],
   "v2": [
    71,
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
     "members",
     "httpx/_content.py",
     "ByteStream"
    ]
   ]
  },
  {
   "call": "members('httpx/_content.py', 'IteratorByteStream')",
   "key": "[\"members\", [\"httpx/_content.py\", \"IteratorByteStream\"]]",
   "v1": [
    141,
    20
   ],
   "v2": [
    71,
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
     "members",
     "httpx/_content.py",
     "IteratorByteStream"
    ]
   ]
  },
  {
   "call": "members('httpx/_content.py', 'UnattachedStream')",
   "key": "[\"members\", [\"httpx/_content.py\", \"UnattachedStream\"]]",
   "v1": [
    141,
    20
   ],
   "v2": [
    71,
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
     "members",
     "httpx/_content.py",
     "UnattachedStream"
    ]
   ]
  },
  {
   "call": "members('httpx/_multipart.py', 'MultipartStream')",
   "key": "[\"members\", [\"httpx/_multipart.py\", \"MultipartStream\"]]",
   "v1": [
    141,
    20
   ],
   "v2": [
    71,
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
     "members",
     "httpx/_multipart.py",
     "MultipartStream"
    ]
   ]
  },
  {
   "call": "members('httpx/_transports/default.py', 'ResponseStream')",
   "key": "[\"members\", [\"httpx/_transports/default.py\", \"ResponseStream\"]]",
   "v1": [
    141,
    20
   ],
   "v2": [
    71,
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
     "members",
     "httpx/_transports/default.py",
     "ResponseStream"
    ]
   ]
  },
  {
   "call": "members('httpx/_transports/wsgi.py', 'WSGIByteStream')",
   "key": "[\"members\", [\"httpx/_transports/wsgi.py\", \"WSGIByteStream\"]]",
   "v1": [
    141,
    20
   ],
   "v2": [
    71,
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
     "members",
     "httpx/_transports/wsgi.py",
     "WSGIByteStream"
    ]
   ]
  }
 ],
 "choice": {
  "call": "members('httpx/_transports/wsgi.py', 'WSGIByteStream')",
  "key": "[\"members\", [\"httpx/_transports/wsgi.py\", \"WSGIByteStream\"]]",
  "provenance": "the members `WSGIByteStream` defines itself (step 1)",
  "v2": [
   71,
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
  "ok": "[\"members\", [\"httpx/_client.py\", \"BoundSyncStream\"]]",
  "cap": "[\"members\", [\"httpx/_client.py\", \"BoundSyncStream\"]]"
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
   "kind": "members",
   "step": 9,
   "path": "httpx/_transports/wsgi.py",
   "cls": "WSGIByteStream",
   "entries": [
    [
     31,
     "def",
     "__init__"
    ],
    [
     35,
     "def",
     "__iter__"
    ],
    [
     39,
     "def",
     "close"
    ]
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "not_overriding",
  "step": 2,
  "of": 2,
  "table": [
   [
    "httpx/_client.py",
    "BoundSyncStream",
    "pending",
    "members not yet seen"
   ],
   [
    "httpx/_content.py",
    "ByteStream",
    "pending",
    "members not yet seen"
   ],
   [
    "httpx/_content.py",
    "IteratorByteStream",
    "pending",
    "members not yet seen"
   ],
   [
    "httpx/_content.py",
    "UnattachedStream",
    "pending",
    "members not yet seen"
   ],
   [
    "httpx/_mul
```
</details>

## Step 10

`WSGIByteStream` defines `close` itself (line 39), so it overrides.

Tally: 0 classes without their own method confirmed, 1 ruled out, 6 pending.

Let me check `BoundSyncStream`'s own members in `httpx/_client.py`; only its own members tell me whether it overrides. Almost certainly the members fit. If there are too many members, I will check `ByteStream`'s own members in `httpx/_content.py`.

**Call:** `members('httpx/_client.py', 'BoundSyncStream')`

**Response**: outcome `ok`

```
class BoundSyncStream in httpx/_client.py definitions=1
145 def __init__
152 def __iter__
156 def close
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "members",
   "key": [
    "members",
    "httpx/_client.py",
    "BoundSyncStream"
   ],
   "desc": "look at what `BoundSyncStream` in `httpx/_client.py` defines itself"
  },
  {
   "kind": "members",
   "key": [
    "members",
    "httpx/_content.py",
    "ByteStream"
   ],
   "desc": "look at what `ByteStream` in `httpx/_content.py` defines itself"
  },
  {
   "kind": "members",
   "key": [
    "members",
    "httpx/_content.py",
    "IteratorByteStream"
   ],
   "desc": "look at what `IteratorByteStream` in `httpx/_content.py` defines itself"
  },
  {
   "kind": "members",
   "key": [
    "members",
    "httpx/_content.py",
    "UnattachedStream"
   ],
   "desc": "look at what `UnattachedStream` in `httpx/_content.py` defines itself"
  },
  {
   "kind": "members",
   "key": [
    "members",
    "httpx/_multipart.py",
    "MultipartStream"
   ],
   "desc": "look at what `MultipartStream` in `httpx/_multipart.py` defines itself"
  },
  {
   "kind": "members",
   "key": [
    "members",
    "httpx/_transports/default.py",
    "ResponseStream"
   ],
   "desc": "look at what `ResponseStream` in `httpx/_transports/default.py` defines itself"
  }
 ],
 "candidates": [
  {
   "call": "members('httpx/_client.py', 'BoundSyncStream')",
   "key": "[\"members\", [\"httpx/_client.py\", \"BoundSyncStream\"]]",
   "v1": [
    121,
    20
   ],
   "v2": [
    61,
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
     "members",
     "httpx/_client.py",
     "BoundSyncStream"
    ]
   ]
  },
  {
   "call": "members('httpx/_content.py', 'ByteStream')",
   "key": "[\"members\", [\"httpx/_content.py\", \"ByteStream\"]]",
   "v1": [
    121,
    20
   ],
   "v2": [
    61,
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
     "members",
     "httpx/_content.py",
     "ByteStream"
    ]
   ]
  },
  {
   "call": "members('httpx/_content.py', 'IteratorByteStream')",
   "key": "[\"members\", [\"httpx/_content.py\", \"IteratorByteStream\"]]",
   "v1": [
    121,
    20
   ],
   "v2": [
    61,
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
     "members",
     "httpx/_content.py",
     "IteratorByteStream"
    ]
   ]
  },
  {
   "call": "members('httpx/_content.py', 'UnattachedStream')",
   "key": "[\"members\", [\"httpx/_content.py\", \"UnattachedStream\"]]",
   "v1": [
    121,
    20
   ],
   "v2": [
    61,
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
     "members",
     "httpx/_content.py",
     "UnattachedStream"
    ]
   ]
  },
  {
   "call": "members('httpx/_multipart.py', 'MultipartStream')",
   "key": "[\"members\", [\"httpx/_multipart.py\", \"MultipartStream\"]]",
   "v1": [
    121,
    20
   ],
   "v2": [
    61,
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
     "members",
     "httpx/_multipart.py",
     "MultipartStream"
    ]
   ]
  },
  {
   "call": "members('httpx/_transports/default.py', 'ResponseStream')",
   "key": "[\"members\", [\"httpx/_transports/default.py\", \"ResponseStream\"]]",
   "v1": [
    121,
    20
   ],
   "v2": [
    61,
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
     "members",
     "httpx/_transports/default.py",
     "ResponseStream"
    ]
   ]
  }
 ],
 "choice": {
  "call": "members('httpx/_client.py', 'BoundSyncStream')",
  "key": "[\"members\", [\"httpx/_client.py\", \"BoundSyncStream\"]]",
  "provenance": "the members `BoundSyncStream` defines itself (step 1)",
  "v2": [
   61,
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
  "ok": "[\"members\", [\"httpx/_content.py\", \"ByteStream\"]]",
  "cap": "[\"members\", [\"httpx/_content.py\", \"ByteStream\"]]"
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
  "planned": "[\"members\", [\"httpx/_client.py\", \"BoundSyncStream\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "members",
   "step": 10,
   "path": "httpx/_client.py",
   "cls": "BoundSyncStream",
   "entries": [
    [
     145,
     "def",
     "__init__"
    ],
    [
     152,
     "def",
     "__iter__"
    ],
    [
     156,
     "def",
     "close"
    ]
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "not_overriding",
  "step": 2,
  "of": 2,
  "table": [
   [
    "httpx/_client.py",
    "BoundSyncStream",
    "out",
    "defines `close` itself"
   ],
   [
    "httpx/_content.py",
    "ByteStream",
    "pending",
    "members not yet seen"
   ],
   [
    "httpx/_content.py",
    "IteratorByteStream",
    "pending",
    "members not yet seen"
   ],
   [
    "httpx/_content.py",
    "UnattachedStream",
    "pending",
    "members not yet seen"
   ],
   [
    "httpx/_multipart.py",
    "MultipartStream",
    "pending",
    "members not yet seen"
   ],
   [
    "httpx/_transports/default.py",
    "ResponseStream",
    "pending",
    "members not yet seen"
   ],
   [
    "httpx/_transports/wsgi.py",
    "WSGIByteStream",
    "out",
    "defines `close` itself"
   ]
  ],
  "n_in": 0,
  "n_out": 2,
  "n_pending": 5
 }
}
```
</details>

## Step 11

`BoundSyncStream` defines `close` itself (line 156), so it overrides.

Tally: 0 classes without their own method confirmed, 2 ruled out, 5 pending.

I'll check `ByteStream`'s own members in `httpx/_content.py`; only its own members tell me whether it overrides. Almost certainly the members fit. If there are too many members, I will check `IteratorByteStream`'s own members in `httpx/_content.py`.

**Call:** `members('httpx/_content.py', 'ByteStream')`

**Response**: outcome `ok`

```
class ByteStream in httpx/_content.py definitions=1
32 def __init__
35 def __iter__
38 def __aiter__
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "members",
   "key": [
    "members",
    "httpx/_content.py",
    "ByteStream"
   ],
   "desc": "look at what `ByteStream` in `httpx/_content.py` defines itself"
  },
  {
   "kind": "members",
   "key": [
    "members",
    "httpx/_content.py",
    "IteratorByteStream"
   ],
   "desc": "look at what `IteratorByteStream` in `httpx/_content.py` defines itself"
  },
  {
   "kind": "members",
   "key": [
    "members",
    "httpx/_content.py",
    "UnattachedStream"
   ],
   "desc": "look at what `UnattachedStream` in `httpx/_content.py` defines itself"
  },
  {
   "kind": "members",
   "key": [
    "members",
    "httpx/_multipart.py",
    "MultipartStream"
   ],
   "desc": "look at what `MultipartStream` in `httpx/_multipart.py` defines itself"
  },
  {
   "kind": "members",
   "key": [
    "members",
    "httpx/_transports/default.py",
    "ResponseStream"
   ],
   "desc": "look at what `ResponseStream` in `httpx/_transports/default.py` defines itself"
  }
 ],
 "candidates": [
  {
   "call": "members('httpx/_content.py', 'ByteStream')",
   "key": "[\"members\", [\"httpx/_content.py\", \"ByteStream\"]]",
   "v1": [
    101,
    20
   ],
   "v2": [
    51,
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
     "members",
     "httpx/_content.py",
     "ByteStream"
    ]
   ]
  },
  {
   "call": "members('httpx/_content.py', 'IteratorByteStream')",
   "key": "[\"members\", [\"httpx/_content.py\", \"IteratorByteStream\"]]",
   "v1": [
    101,
    20
   ],
   "v2": [
    51,
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
     "members",
     "httpx/_content.py",
     "IteratorByteStream"
    ]
   ]
  },
  {
   "call": "members('httpx/_content.py', 'UnattachedStream')",
   "key": "[\"members\", [\"httpx/_content.py\", \"UnattachedStream\"]]",
   "v1": [
    101,
    20
   ],
   "v2": [
    51,
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
     "members",
     "httpx/_content.py",
     "UnattachedStream"
    ]
   ]
  },
  {
   "call": "members('httpx/_multipart.py', 'MultipartStream')",
   "key": "[\"members\", [\"httpx/_multipart.py\", \"MultipartStream\"]]",
   "v1": [
    101,
    20
   ],
   "v2": [
    51,
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
     "members",
     "httpx/_multipart.py",
     "MultipartStream"
    ]
   ]
  },
  {
   "call": "members('httpx/_transports/default.py', 'ResponseStream')",
   "key": "[\"members\", [\"httpx/_transports/default.py\", \"ResponseStream\"]]",
   "v1": [
    101,
    20
   ],
   "v2": [
    51,
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
     "members",
     "httpx/_transports/default.py",
     "ResponseStream"
    ]
   ]
  }
 ],
 "choice": {
  "call": "members('httpx/_content.py', 'ByteStream')",
  "key": "[\"members\", [\"httpx/_content.py\", \"ByteStream\"]]",
  "provenance": "the members `ByteStream` defines itself (step 1)",
  "v2": [
   51,
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
  "ok": "[\"members\", [\"httpx/_content.py\", \"IteratorByteStream\"]]",
  "cap": "[\"members\", [\"httpx/_content.py\", \"IteratorByteStream\"]]"
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
  "planned": "[\"members\", [\"httpx/_content.py\", \"ByteStream\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "members",
   "step": 11,
   "path": "httpx/_content.py",
   "cls": "ByteStream",
   "entries": [
    [
     32,
     "def",
     "__init__"
    ],
    [
     35,
     "def",
     "__iter__"
    ],
    [
     38,
     "def",
     "__aiter__"
    ]
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "not_overriding",
  "step": 2,
  "of": 2,
  "table": [
   [
    "httpx/_client.py",
    "BoundSyncStream",
    "out",
    "defines `close` itself"
   ],
   [
    "httpx/_content.py",
    "ByteStream",
    "in",
    "does not define `close`"
   ],
   [
    "httpx/_content.py",
    "IteratorByteStream",
    "pending",
    "members not yet seen"
   ],
   [
    "httpx/_content.py",
    "UnattachedStream",
    "pending",
    "members not yet seen"
   ],
   [
    "httpx/_multipart.py",
    "MultipartStream",
    "pending",
    "members not yet seen"
   ],
   [
    "httpx/_transports/default.py",
    "ResponseStream",
    "pending",
    "members not yet seen"
   ],
   [
    "httpx/_transports/wsgi.py",
    "WSGIByteStream",
    "out",
    "defines `close` itself"
   ]
  ],
  "n_in": 1,
  "n_out": 2,
  "n_pending": 4
 }
}
```
</details>

## Step 12

`ByteStream` defines `__init__`, `__iter__`, `__aiter__`, but no `close`, so it inherits it.

Tally: 1 classes without their own method confirmed, 2 ruled out, 4 pending.

Next I will check `IteratorByteStream`'s own members in `httpx/_content.py`; only its own members tell me whether it overrides. Almost certainly the members fit. If there are too many members, I will check `UnattachedStream`'s own members in `httpx/_content.py`.

**Call:** `members('httpx/_content.py', 'IteratorByteStream')`

**Response**: outcome `ok`

```
class IteratorByteStream in httpx/_content.py definitions=1
43 assign CHUNK_SIZE
45 def __init__
50 def __iter__
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "members",
   "key": [
    "members",
    "httpx/_content.py",
    "IteratorByteStream"
   ],
   "desc": "look at what `IteratorByteStream` in `httpx/_content.py` defines itself"
  },
  {
   "kind": "members",
   "key": [
    "members",
    "httpx/_content.py",
    "UnattachedStream"
   ],
   "desc": "look at what `UnattachedStream` in `httpx/_content.py` defines itself"
  },
  {
   "kind": "members",
   "key": [
    "members",
    "httpx/_multipart.py",
    "MultipartStream"
   ],
   "desc": "look at what `MultipartStream` in `httpx/_multipart.py` defines itself"
  },
  {
   "kind": "members",
   "key": [
    "members",
    "httpx/_transports/default.py",
    "ResponseStream"
   ],
   "desc": "look at what `ResponseStream` in `httpx/_transports/default.py` defines itself"
  }
 ],
 "candidates": [
  {
   "call": "members('httpx/_content.py', 'IteratorByteStream')",
   "key": "[\"members\", [\"httpx/_content.py\", \"IteratorByteStream\"]]",
   "v1": [
    81,
    20
   ],
   "v2": [
    41,
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
     "members",
     "httpx/_content.py",
     "IteratorByteStream"
    ]
   ]
  },
  {
   "call": "members('httpx/_content.py', 'UnattachedStream')",
   "key": "[\"members\", [\"httpx/_content.py\", \"UnattachedStream\"]]",
   "v1": [
    81,
    20
   ],
   "v2": [
    41,
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
     "members",
     "httpx/_content.py",
     "UnattachedStream"
    ]
   ]
  },
  {
   "call": "members('httpx/_multipart.py', 'MultipartStream')",
   "key": "[\"members\", [\"httpx/_multipart.py\", \"MultipartStream\"]]",
   "v1": [
    81,
    20
   ],
   "v2": [
    41,
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
     "members",
     "httpx/_multipart.py",
     "MultipartStream"
    ]
   ]
  },
  {
   "call": "members('httpx/_transports/default.py', 'ResponseStream')",
   "key": "[\"members\", [\"httpx/_transports/default.py\", \"ResponseStream\"]]",
   "v1": [
    81,
    20
   ],
   "v2": [
    41,
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
     "members",
     "httpx/_transports/default.py",
     "ResponseStream"
    ]
   ]
  }
 ],
 "choice": {
  "call": "members('httpx/_content.py', 'IteratorByteStream')",
  "key": "[\"members\", [\"httpx/_content.py\", \"IteratorByteStream\"]]",
  "provenance": "the members `IteratorByteStream` defines itself (step 1)",
  "v2": [
   41,
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
  "ok": "[\"members\", [\"httpx/_content.py\", \"UnattachedStream\"]]",
  "cap": "[\"members\", [\"httpx/_content.py\", \"UnattachedStream\"]]"
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
  "planned": "[\"members\", [\"httpx/_content.py\", \"IteratorByteStream\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "members",
   "step": 12,
   "path": "httpx/_content.py",
   "cls": "IteratorByteStream",
   "entries": [
    [
     43,
     "assign",
     "CHUNK_SIZE"
    ],
    [
     45,
     "def",
     "__init__"
    ],
    [
     50,
     "def",
     "__iter__"
    ]
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "not_overriding",
  "step": 2,
  "of": 2,
  "table": [
   [
    "httpx/_client.py",
    "BoundSyncStream",
    "out",
    "defines `close` itself"
   ],
   [
    "httpx/_content.py",
    "ByteStream",
    "in",
    "does not define `close`"
   ],
   [
    "httpx/_content.py",
    "IteratorByteStream",
    "in",
    "does not define `close`"
   ],
   [
    "httpx/_content.py",
    "UnattachedStream",
    "pending",
    "members not yet seen"
   ],
   [
    "httpx/_multipart.py",
    "MultipartStream",
    "pending",
    "members not yet seen"
   ],
   [
    "httpx/_transports/default.py",
    "ResponseStream",
    "pending",
    "members not yet seen"
   ],
   [
    "httpx/_transports/wsgi.py",
    "WSGIByteStream",
    "out",
    "defines `close` itself"
   ]
  ],
  "n_in": 2,
  "n_out": 2,
  "n_pending": 3
 }
}
```
</details>

## Step 13

`IteratorByteStream` defines `__init__`, `__iter__`, but no `close`, so it inherits it.

Tally: 2 classes without their own method confirmed, 2 ruled out, 3 pending.

I'll check `UnattachedStream`'s own members in `httpx/_content.py`; only its own members tell me whether it overrides. Almost certainly the members fit. If there are too many members, I will check `MultipartStream`'s own members in `httpx/_multipart.py`.

**Call:** `members('httpx/_content.py', 'UnattachedStream')`

**Response**: outcome `ok`

```
class UnattachedStream in httpx/_content.py definitions=1
99 def __iter__
102 def __aiter__
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "members",
   "key": [
    "members",
    "httpx/_content.py",
    "UnattachedStream"
   ],
   "desc": "look at what `UnattachedStream` in `httpx/_content.py` defines itself"
  },
  {
   "kind": "members",
   "key": [
    "members",
    "httpx/_multipart.py",
    "MultipartStream"
   ],
   "desc": "look at what `MultipartStream` in `httpx/_multipart.py` defines itself"
  },
  {
   "kind": "members",
   "key": [
    "members",
    "httpx/_transports/default.py",
    "ResponseStream"
   ],
   "desc": "look at what `ResponseStream` in `httpx/_transports/default.py` defines itself"
  }
 ],
 "candidates": [
  {
   "call": "members('httpx/_content.py', 'UnattachedStream')",
   "key": "[\"members\", [\"httpx/_content.py\", \"UnattachedStream\"]]",
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
     "members",
     "httpx/_content.py",
     "UnattachedStream"
    ]
   ]
  },
  {
   "call": "members('httpx/_multipart.py', 'MultipartStream')",
   "key": "[\"members\", [\"httpx/_multipart.py\", \"MultipartStream\"]]",
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
     "members",
     "httpx/_multipart.py",
     "MultipartStream"
    ]
   ]
  },
  {
   "call": "members('httpx/_transports/default.py', 'ResponseStream')",
   "key": "[\"members\", [\"httpx/_transports/default.py\", \"ResponseStream\"]]",
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
     "members",
     "httpx/_transports/default.py",
     "ResponseStream"
    ]
   ]
  }
 ],
 "choice": {
  "call": "members('httpx/_content.py', 'UnattachedStream')",
  "key": "[\"members\", [\"httpx/_content.py\", \"UnattachedStream\"]]",
  "provenance": "the members `UnattachedStream` defines itself (step 1)",
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
  "ok": "[\"members\", [\"httpx/_multipart.py\", \"MultipartStream\"]]",
  "cap": "[\"members\", [\"httpx/_multipart.py\", \"MultipartStream\"]]"
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
  "planned": "[\"members\", [\"httpx/_content.py\", \"UnattachedStream\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "members",
   "step": 13,
   "path": "httpx/_content.py",
   "cls": "UnattachedStream",
   "entries": [
    [
     99,
     "def",
     "__iter__"
    ],
    [
     102,
     "def",
     "__aiter__"
    ]
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "not_overriding",
  "step": 2,
  "of": 2,
  "table": [
   [
    "httpx/_client.py",
    "BoundSyncStream",
    "out",
    "defines `close` itself"
   ],
   [
    "httpx/_content.py",
    "ByteStream",
    "in",
    "does not define `close`"
   ],
   [
    "httpx/_content.py",
    "IteratorByteStream",
    "in",
    "does not define `close`"
   ],
   [
    "httpx/_content.py",
    "UnattachedStream",
    "in",
    "does not define `close`"
   ],
   [
    "httpx/_multipart.py",
    "MultipartStream",
    "pending",
    "members not yet seen"
   ],
   [
    "httpx/_transports/default.py",
    "ResponseStream",
    "pending",
    "members not yet seen"
   ],
   [
    "httpx/_transports/wsgi.py",
    "WSGIByteStream",
    "out",
    "defines `close` itself"
   ]
  ],
  "n_in": 3,
  "n_out": 2,
  "n_pending": 2
 }
}
```
</details>

## Step 14

`UnattachedStream` defines `__iter__`, `__aiter__`, but no `close`, so it inherits it.

Tally: 3 classes without their own method confirmed, 2 ruled out, 2 pending.

Next I will check `MultipartStream`'s own members in `httpx/_multipart.py`; only its own members tell me whether it overrides. Almost certainly the members fit. If there are too many members, I will check `ResponseStream`'s own members in `httpx/_transports/default.py`.

**Call:** `members('httpx/_multipart.py', 'MultipartStream')`

**Response**: outcome `ok`

```
class MultipartStream in httpx/_multipart.py definitions=1
229 def __init__
244 def _iter_fields
258 def iter_chunks
265 def get_content_length
287 def get_headers
294 def __iter__
298 def __aiter__
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "members",
   "key": [
    "members",
    "httpx/_multipart.py",
    "MultipartStream"
   ],
   "desc": "look at what `MultipartStream` in `httpx/_multipart.py` defines itself"
  },
  {
   "kind": "members",
   "key": [
    "members",
    "httpx/_transports/default.py",
    "ResponseStream"
   ],
   "desc": "look at what `ResponseStream` in `httpx/_transports/default.py` defines itself"
  }
 ],
 "candidates": [
  {
   "call": "members('httpx/_multipart.py', 'MultipartStream')",
   "key": "[\"members\", [\"httpx/_multipart.py\", \"MultipartStream\"]]",
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
     "members",
     "httpx/_multipart.py",
     "MultipartStream"
    ]
   ]
  },
  {
   "call": "members('httpx/_transports/default.py', 'ResponseStream')",
   "key": "[\"members\", [\"httpx/_transports/default.py\", \"ResponseStream\"]]",
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
     "members",
     "httpx/_transports/default.py",
     "ResponseStream"
    ]
   ]
  }
 ],
 "choice": {
  "call": "members('httpx/_multipart.py', 'MultipartStream')",
  "key": "[\"members\", [\"httpx/_multipart.py\", \"MultipartStream\"]]",
  "provenance": "the members `MultipartStream` defines itself (step 1)",
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
  "ok": "[\"members\", [\"httpx/_transports/default.py\", \"ResponseStream\"]]",
  "cap": "[\"members\", [\"httpx/_transports/default.py\", \"ResponseStream\"]]"
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
  "planned": "[\"members\", [\"httpx/_multipart.py\", \"MultipartStream\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "members",
   "step": 14,
   "path": "httpx/_multipart.py",
   "cls": "MultipartStream",
   "entries": [
    [
     229,
     "def",
     "__init__"
    ],
    [
     244,
     "def",
     "_iter_fields"
    ],
    [
     258,
     "def",
     "iter_chunks"
    ],
    [
     265,
     "def",
     "get_content_length"
    ],
    [
     287,
     "def",
     "get_headers"
    ],
    [
     294,
     "def",
     "__iter__"
    ],
    [
     298,
     "def",
     "__aiter__"
    ]
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "not_overriding",
  "step": 2,
  "of": 2,
  "table": [
   [
    "httpx/_client.py",
    "BoundSyncStream",
    "out",
    "defines `close` itself"
   ],
   [
    "httpx/_content.py",
    "ByteStream",
    "in",
    "does not define `close`"
   ],
   [
    "httpx/_content.py",
    "IteratorByteStream",
    "in",
    "does not define `close`"
   ],
   [
    "httpx/_content.py",
    "UnattachedStream",
    "in",
    "does not define `close`"
   ],
   [
    "httpx/_multipart.py",
    "MultipartStream",
    "in",
    "does not define `close`"
   ],
   [
    "httpx/_transports/default.py",
    "ResponseStream",
    "pending",
    "members not yet seen"
   ],
   [
    "httpx/_transports/wsgi.py",
    "WSGIByteStream",
    "out",
    "defines `close` itself"
   ]
  ],
  "n_in": 4,
  "n_out": 2,
  "n_pending": 1
 }
}
```
</details>

## Step 15

`MultipartStream` defines `__init__`, `_iter_fields`, `iter_chunks`, `get_content_length` and more, but no `close`, so it inherits it.

Tally: 4 classes without their own method confirmed, 2 ruled out, 1 pending.

Let me check `ResponseStream`'s own members in `httpx/_transports/default.py`; only its own members tell me whether it overrides. Almost certainly the members fit. If there are too many members, I follow whatever it opens up.

**Call:** `members('httpx/_transports/default.py', 'ResponseStream')`

**Response**: outcome `ok`

```
class ResponseStream in httpx/_transports/default.py definitions=1
122 def __init__
125 def __iter__
130 def close
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "members",
   "key": [
    "members",
    "httpx/_transports/default.py",
    "ResponseStream"
   ],
   "desc": "look at what `ResponseStream` in `httpx/_transports/default.py` defines itself"
  }
 ],
 "candidates": [
  {
   "call": "members('httpx/_transports/default.py', 'ResponseStream')",
   "key": "[\"members\", [\"httpx/_transports/default.py\", \"ResponseStream\"]]",
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
     "members",
     "httpx/_transports/default.py",
     "ResponseStream"
    ]
   ]
  }
 ],
 "choice": {
  "call": "members('httpx/_transports/default.py', 'ResponseStream')",
  "key": "[\"members\", [\"httpx/_transports/default.py\", \"ResponseStream\"]]",
  "provenance": "the members `ResponseStream` defines itself (step 1)",
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
  "planned": "[\"members\", [\"httpx/_transports/default.py\", \"ResponseStream\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "members",
   "step": 15,
   "path": "httpx/_transports/default.py",
   "cls": "ResponseStream",
   "entries": [
    [
     122,
     "def",
     "__init__"
    ],
    [
     125,
     "def",
     "__iter__"
    ],
    [
     130,
     "def",
     "close"
    ]
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "not_overriding",
  "step": 2,
  "of": 2,
  "table": [
   [
    "httpx/_client.py",
    "BoundSyncStream",
    "out",
    "defines `close` itself"
   ],
   [
    "httpx/_content.py",
    "ByteStream",
    "in",
    "does not define `close`"
   ],
   [
    "httpx/_content.py",
    "IteratorByteStream",
    "in",
    "does not define `close`"
   ],
   [
    "httpx/_content.py",
    "UnattachedStream",
    "in",
    "does not define `close`"
   ],
   [
    "httpx/_multipart.py",
    "MultipartStream",
    "in",
    "does not define `close`"
   ],
   [
    "httpx/_transports/default.py",
    "ResponseStream",
    "out",
    "defines `close` itself"
   ],
   [
    "httpx/_transports/wsgi.py",
    "WSGIByteStream",
    "out",
    "defines `close` itself"
   ]
  ],
  "n_in": 4,
  "n_out": 3,
  "n_pending": 0
 }
}
```
</details>

## Final

7 classes derive from it directly: `BoundSyncStream` (`httpx/_client.py:139`), `ByteStream` (`httpx/_content.py:31`), `IteratorByteStream` (`httpx/_content.py:42`), `UnattachedStream` (`httpx/_content.py:92`), `MultipartStream` (`httpx/_multipart.py:224`), `ResponseStream` (`httpx/_transports/default.py:121`), `WSGIByteStream` (`httpx/_transports/wsgi.py:30`). 4 of the subclasses do not define `close` themselves: `ByteStream`, `IteratorByteStream`, `UnattachedStream`, `MultipartStream`. Looking back, all 15 calls were needed.

**Answer:** `{"final_kind": "not_overriding", "final": ["httpx/_content.py:31:ByteStream", "httpx/_content.py:42:IteratorByteStream", "httpx/_content.py:92:UnattachedStream", "httpx/_multipart.py:224:MultipartStream"], "steps": [{"op": "subclasses", "output": ["httpx/_client.py:139:BoundSyncStream", "httpx/_content.py:31:ByteStream", "httpx/_content.py:42:IteratorByteStream", "httpx/_content.py:92:UnattachedStream", "httpx/_multipart.py:224:MultipartStream", "httpx/_transports/default.py:121:ResponseStream", "httpx/_transports/wsgi.py:30:WSGIByteStream"]}, {"op": "not_overriding", "output": ["httpx/_content.py:31:ByteStream", "httpx/_content.py:42:IteratorByteStream", "httpx/_content.py:92:UnattachedStream", "httpx/_multipart.py:224:MultipartStream"]}], "stuck": null}`  
**Stopped:** certificate after 15 calls