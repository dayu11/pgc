# httpx-resolve-81b1af7d

**Repository:** httpx  
**Family:** resolve  
**Seed:** 0, prior d99074a5d38bc2d8

## Task

In `httpx/_models.py`, line 34 imports `codes` from `._status_codes`. Under the declared semantics, which definition does the module-level name `codes` bound by this statement resolve to? Answer with `path:line`.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

Nothing seen yet beyond the task text.

Chain: `httpx/_models.py` is not yet closed for `codes`.

Outstanding: close the namespace of `httpx/_models.py` for `codes`.

Next: outline `httpx/_models.py`, because module `httpx/_models.py` (task). I expect: a definition there ends the chain (about 80%); a capped outline means filtering by name (about 15%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `httpx/_models.py` filtered to `codes`, is expected to open more follow-up work. Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done; cap: outline `httpx/_models.py` filtered to `codes`.

**Call:** `symbols('httpx/_models.py')`

**Response** (capped): outcome `cap`

```
module httpx/_models.py lines=1278 dynamic=no all=static@51
1 from annotations <- __future__ annotations
3 import codecs <- codecs
4 import datetime <- datetime
5 import email <- email
6 import jsonlib <- json
7 import re <- re
8 import typing <- typing
9 import urllib <- urllib
10 from Mapping <- collections.abc Mapping
11 from Cookie <- http.cookiejar Cookie
11 from CookieJar <- http.cookiejar CookieJar
13 from ByteStream <- ._content ByteStream
13 from UnattachedStream <- ._content UnattachedStream
13 from encode_request <- ._content encode_request
13 from encode_response <- ._content encode_response
14 from ByteChunker <- ._decoders ByteChunker
14 from ContentDecoder <- ._decoders ContentDecoder
14 from IdentityDecoder <- ._decoders IdentityDecoder
14 from LineDecoder <- ._decoders LineDecoder
14 from MultiDecoder <- ._decoders MultiDecoder
14 from SUPPORTED_DECODERS <- ._decoders SUPPORTED_DECODERS
14 from TextChunker <- ._decoders TextChunker
14 from TextDecoder <- ._decoders TextDecoder
24 from CookieConflict <- ._exceptions CookieConflict
... (16 more lines)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "httpx/_models.py",
    "codes"
   ],
   "desc": "close the namespace of `httpx/_models.py` for `codes`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/_models.py')",
   "key": "[\"symbols\", [\"httpx/_models.py\"]]",
   "v1": [
    7504007509,
    6394708446
   ],
   "v2": [
    38034501849,
    26644618525
   ],
   "p_cap": [
    28,
    207
   ],
   "forecast": {
    "def": [
     72137,
     88389
    ],
    "reexport": [
     179,
     12627
    ],
    "star": [
     179,
     88389
    ],
    "none": [
     2864,
     88389
    ],
    "cap": [
     28,
     207
    ]
   },
   "serves": [
    [
     "bindings",
     "httpx/_models.py",
     "codes"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_models.py', 'codes')",
   "key": "[\"symbols\", [\"httpx/_models.py\", \"codes\"]]",
   "v1": [
    63289263,
    21704200
   ],
   "v2": [
    63289263,
    21704200
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
     "httpx/_models.py",
     "codes"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('httpx/_models.py')",
  "key": "[\"symbols\", [\"httpx/_models.py\"]]",
  "provenance": "module `httpx/_models.py` (task)",
  "v2": [
   38034501849,
   26644618525
  ]
 },
 "forecast": {
  "def": [
   72137,
   88389
  ],
  "reexport": [
   179,
   12627
  ],
  "star": [
   179,
   88389
  ],
  "none": [
   2864,
   88389
  ],
  "cap": [
   28,
   207
  ]
 },
 "plan": {
  "def": "done",
  "reexport": "continue",
  "star": "continue",
  "none": "done",
  "cap": "[\"symbols\", [\"httpx/_models.py\", \"codes\"]]"
 },
 "adherence": null,
 "facts": [
  {
   "kind": "outline",
   "step": 1,
   "path": "httpx/_models.py",
   "filter": null,
   "header": {
    "lines": 1278,
    "dynamic": false,
    "all_status": "static",
    "all_line": 51
   },
   "bindings": [
    {
     "module": "httpx/_models.py",
     "name": "annotations",
     "line": 1,
     "kind": "from",
     "src": "__future__",
     "src_name": "annotations",
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_models.py",
     "name": "codecs",
     "line": 3,
     "kind": "import",
     "src": "codecs",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_models.py",
     "name": "datetime",
     "line": 4,
     "kind": "import",
     "src": "datetime",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_models.py",
     "name": "email",
     "line": 5,
     "kind": "import",
     "src": "email",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_models.py",
     "name": "jsonlib",
     "line": 6,
     "kind": "import",
     "src": "json",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_models.py",
     "name": "re",
     "line": 7,
     "kind": "import",
     "src": "re",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_models.py",
     "name": "typing",
     "line": 8,
     "kind": "import",
     "src": "typing",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_models.py",
     "name": "urllib",
     "line": 9,
     "kind": "import",
     "src": "urllib",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_models.py",
     "name": "Mapping",
     "line": 10,
     "kind": "from",
     "src": "collections.abc",
     "src_name": "Mapping",
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_models.py",
     "name": "Cookie",
     "line": 11,
     "kind": "from",
     "src": "http.cookiejar",
     "src_name": "Cookie",
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_models.py",
     "name": "CookieJar",
     "line": 11,
     "kind": "from",
     "src": "http.cookiejar",
     "src_name": "CookieJar",
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_models.py",
     "name": "ByteStream",
     "line": 13,
     "kind": "from",
     "src": "._content",
     "src_name": "ByteStream",
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_models.py",
     "name": "UnattachedStream",
     "line": 13,
     "kind": "from",
     "src": "._content",
     "src_name": "UnattachedStream",
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_models.py",
     "name": "encode_request",
     "line": 13,
     "kind": "from",
     "src": "._content",
     "src_name": "encode_request",
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_models.py",
     "name": "encode_response",
     "line": 13,
     "kind": "from",
     "src": "._content",
     "src_name": "encode_response",
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_models.py",
     "name": "ByteChunker",
     "line": 14,
     "kind": "from",
     "src": "._decoders",
     "src_name": "ByteChunker",
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_models.py",
     "name": "ContentDecoder",
     "line": 14,
     "kind": "from",
     "src": "._decoders",
     "src_name": "ContentDecoder",
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_models.py",
     "name": "IdentityDecoder",
     "line": 14,
     "kind": "from",
     "src": "._decoders",
     "src_name": "IdentityDecoder",
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_models.py",
     "name": "LineDecoder",
     "line": 14,
     "kind": "from",
     "src": "._decoders",
     "src_name": "LineDecoder",
     "conditional": false,
     "c
```
</details>

## Step 2

The outline of `httpx/_models.py` has 40 bindings (capped, so this is only the start of the file); a literal `__all__` at line 51; no dynamic namespace tricks.

Chain: `httpx/_models.py` is not yet closed for `codes`.

Still to settle: close the namespace of `httpx/_models.py` for `codes`.

Next: outline `httpx/_models.py` filtered to `codes`, because module `httpx/_models.py` (task), name `codes` (task). I expect: a re-export continues the chain to its source (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a definition there ends the chain (under 5%); no binding but a star import means checking what that source exports (under 5%). Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done.

**Call:** `symbols('httpx/_models.py', 'codes')`

**Response**: outcome `reexport`

```
module httpx/_models.py lines=1278 dynamic=no all=static@51
34 from codes <- ._status_codes codes
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "httpx/_models.py",
    "codes"
   ],
   "desc": "close the namespace of `httpx/_models.py` for `codes`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/_models.py', 'codes')",
   "key": "[\"symbols\", [\"httpx/_models.py\", \"codes\"]]",
   "v1": [
    63289263,
    21704200
   ],
   "v2": [
    63289263,
    21704200
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
     "httpx/_models.py",
     "codes"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('httpx/_models.py', 'codes')",
  "key": "[\"symbols\", [\"httpx/_models.py\", \"codes\"]]",
  "provenance": "module `httpx/_models.py` (task), name `codes` (task)",
  "v2": [
   63289263,
   21704200
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
 "adherence": {
  "planned": "[\"symbols\", [\"httpx/_models.py\", \"codes\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 2,
   "path": "httpx/_models.py",
   "filter": "codes",
   "header": {
    "lines": 1278,
    "dynamic": false,
    "all_status": "static",
    "all_line": 51
   },
   "bindings": [
    {
     "module": "httpx/_models.py",
     "name": "codes",
     "line": 34,
     "kind": "from",
     "src": "._status_codes",
     "src_name": "codes",
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
    "httpx/_models.py",
    "codes",
    "reexport",
    [
     "._status_codes",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 3

In `httpx/_models.py`, `codes` has exactly one binding: line 34 imports it as `codes` from `._status_codes`. No dynamic namespace tricks, a literal `__all__` at line 51.

Chain: `httpx/_models.py` takes `codes` from `._status_codes` (module not yet located).

Outstanding: locate the module `._status_codes` imported by `httpx/_models.py`.

Next: outline `httpx/_status_codes.py` filtered to `codes`, because `._status_codes` would be `httpx/_status_codes.py` if that file exists; one call both checks and closes it. I expect: a definition there ends the chain (about 80%); the file does not exist (about 15%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, grep `def`/`class codes` statements under `.`, is expected to open more follow-up work. Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done; missing: grep `def`/`class codes` statements under `.`.

**Call:** `symbols('httpx/_status_codes.py', 'codes')`

**Response**: outcome `def`

```
module httpx/_status_codes.py lines=163 dynamic=no all=static@5
8 class codes
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/_models.py",
    "._status_codes"
   ],
   "desc": "locate the module `._status_codes` imported by `httpx/_models.py`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/_status_codes.py', 'codes')",
   "key": "[\"symbols\", [\"httpx/_status_codes.py\", \"codes\"]]",
   "v1": [
    15126579645,
    11445601349
   ],
   "v2": [
    441914502395,
    331922439121
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     6572,
     8113
    ],
    "reexport": [
     212,
     15067
    ],
    "star": [
     212,
     105469
    ],
    "none": [
     3392,
     105469
    ],
    "missing": [
     35,
     247
    ]
   },
   "serves": [
    [
     "module_path",
     "httpx/_models.py",
     "._status_codes"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+codes\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+codes\\\\b\", \".\"]]",
   "v1": [
    25604,
    12151
   ],
   "v2": [
    683007550306,
    331922439121
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
     "httpx/_models.py",
     "._status_codes"
    ]
   ]
  },
  {
   "call": "ls('httpx')",
   "key": "[\"ls\", [\"httpx\"]]",
   "v1": [
    48211,
    22626
   ],
   "v2": [
    212657658406,
    103010412141
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
     "httpx/_models.py",
     "._status_codes"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_status_codes/__init__.py', 'codes')",
   "key": "[\"symbols\", [\"httpx/_status_codes/__init__.py\", \"codes\"]]",
   "v1": [
    245545073,
    83104879
   ],
   "v2": [
    5311202547632379,
    2270132017162009
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     350,
     18031
    ],
    "reexport": [
     1400,
     18031
    ],
    "star": [
     35,
     18031
    ],
    "none": [
     770,
     18031
    ],
    "missing": [
     212,
     247
    ]
   },
   "serves": [
    [
     "module_path",
     "httpx/_models.py",
     "._status_codes"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('httpx/_status_codes.py', 'codes')",
  "key": "[\"symbols\", [\"httpx/_status_codes.py\", \"codes\"]]",
  "provenance": "`._status_codes` would be `httpx/_status_codes.py` if that file exists; one call both checks and closes it",
  "v2": [
   441914502395,
   331922439121
  ]
 },
 "forecast": {
  "def": [
   6572,
   8113
  ],
  "reexport": [
   212,
   15067
  ],
  "star": [
   212,
   105469
  ],
  "none": [
   3392,
   105469
  ],
  "missing": [
   35,
   247
  ]
 },
 "plan": {
  "def": "done",
  "reexport": "continue",
  "star": "continue",
  "none": "done",
  "missing": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+codes\\\\b\", \".\"]]"
 },
 "adherence": {
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 3,
   "path": "httpx/_status_codes.py",
   "filter": "codes",
   "header": {
    "lines": 163,
    "dynamic": false,
    "all_status": "static",
    "all_line": 5
   },
   "bindings": [
    {
     "module": "httpx/_status_codes.py",
     "name": "codes",
     "line": 8,
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
    "httpx/_models.py",
    "codes",
    "reexport",
    [
     "._status_codes",
     "httpx/_status_codes.py"
    ]
   ],
   [
    "httpx/_status_codes.py",
    "codes",
    "class",
    8
   ]
  ]
 }
}
```
</details>

## Final

Certificate complete. The name resolves to `httpx/_status_codes.py:8`. In hindsight, 1 of 3 calls were not needed for the certificate: steps 1.

**Answer:** `{"target": {"kind": "def", "path": "httpx/_status_codes.py", "line": 8, "name": "codes", "detail": "class"}, "text": "httpx/_status_codes.py:8"}`  
**Stopped:** certificate after 3 calls