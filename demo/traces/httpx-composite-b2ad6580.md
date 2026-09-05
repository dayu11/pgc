# httpx-composite-b2ad6580

**Repository:** httpx  
**Family:** composite  
**Seed:** 0, prior d99074a5d38bc2d8

## Task

In `httpx/_transports/asgi.py`, line 6 imports `AsyncByteStream` from `.._types`. Under the declared semantics, which definition does the module-level name `AsyncByteStream` bound by this statement resolve to? Answer with `path:line`. Then list every module-level import statement in the snapshot that imports that definition (from-imports naming it, directly or with `as`, and star imports of modules that export it), as `path:line` entries.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

Nothing seen yet beyond the task text.

Chain: `httpx/_transports/asgi.py` is not yet closed for `AsyncByteStream`.

Outstanding: close the namespace of `httpx/_transports/asgi.py` for `AsyncByteStream`.

Next: outline `httpx/_transports/asgi.py`, because module `httpx/_transports/asgi.py` (task). I expect: a definition there ends the chain (about 80%); a capped outline means filtering by name (about 15%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `httpx/_transports/asgi.py` filtered to `AsyncByteStream`, is expected to open more follow-up work. Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done; cap: outline `httpx/_transports/asgi.py` filtered to `AsyncByteStream`.

**Call:** `symbols('httpx/_transports/asgi.py')`

**Response**: outcome `def`

```
module httpx/_transports/asgi.py lines=188 dynamic=no all=static@26
1 from annotations <- __future__ annotations
3 import typing <- typing
5 from Request <- .._models Request
5 from Response <- .._models Response
6 from AsyncByteStream <- .._types AsyncByteStream
7 from AsyncBaseTransport <- .base AsyncBaseTransport
10 import asyncio <- asyncio
12 import trio <- trio
14 assign Event
17 assign _Message
18 assign _Receive
19 assign _Send
22 assign _ASGIApp
26 assign __all__
29 def is_running_trio
44 def create_event
55 class ASGIResponseStream
63 class ASGITransport
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "httpx/_transports/asgi.py",
    "AsyncByteStream"
   ],
   "desc": "close the namespace of `httpx/_transports/asgi.py` for `AsyncByteStream`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/_transports/asgi.py')",
   "key": "[\"symbols\", [\"httpx/_transports/asgi.py\"]]",
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
     "httpx/_transports/asgi.py",
     "AsyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/asgi.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/asgi.py\", \"AsyncByteStream\"]]",
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
     "httpx/_transports/asgi.py",
     "AsyncByteStream"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('httpx/_transports/asgi.py')",
  "key": "[\"symbols\", [\"httpx/_transports/asgi.py\"]]",
  "provenance": "module `httpx/_transports/asgi.py` (task)",
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
  "cap": "[\"symbols\", [\"httpx/_transports/asgi.py\", \"AsyncByteStream\"]]"
 },
 "adherence": null,
 "facts": [
  {
   "kind": "outline",
   "step": 1,
   "path": "httpx/_transports/asgi.py",
   "filter": null,
   "header": {
    "lines": 188,
    "dynamic": false,
    "all_status": "static",
    "all_line": 26
   },
   "bindings": [
    {
     "module": "httpx/_transports/asgi.py",
     "name": "annotations",
     "line": 1,
     "kind": "from",
     "src": "__future__",
     "src_name": "annotations",
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_transports/asgi.py",
     "name": "typing",
     "line": 3,
     "kind": "import",
     "src": "typing",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_transports/asgi.py",
     "name": "Request",
     "line": 5,
     "kind": "from",
     "src": ".._models",
     "src_name": "Request",
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_transports/asgi.py",
     "name": "Response",
     "line": 5,
     "kind": "from",
     "src": ".._models",
     "src_name": "Response",
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_transports/asgi.py",
     "name": "AsyncByteStream",
     "line": 6,
     "kind": "from",
     "src": ".._types",
     "src_name": "AsyncByteStream",
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_transports/asgi.py",
     "name": "AsyncBaseTransport",
     "line": 7,
     "kind": "from",
     "src": ".base",
     "src_name": "AsyncBaseTransport",
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_transports/asgi.py",
     "name": "asyncio",
     "line": 10,
     "kind": "import",
     "src": "asyncio",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_transports/asgi.py",
     "name": "trio",
     "line": 12,
     "kind": "import",
     "src": "trio",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_transports/asgi.py",
     "name": "Event",
     "line": 14,
     "kind": "assign",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_transports/asgi.py",
     "name": "_Message",
     "line": 17,
     "kind": "assign",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_transports/asgi.py",
     "name": "_Receive",
     "line": 18,
     "kind": "assign",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_transports/asgi.py",
     "name": "_Send",
     "line": 19,
     "kind": "assign",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_transports/asgi.py",
     "name": "_ASGIApp",
     "line": 22,
     "kind": "assign",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_transports/asgi.py",
     "name": "__all__",
     "line": 26,
     "kind": "assign",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_transports/asgi.py",
     "name": "is_running_trio",
     "line": 29,
     "kind": "def",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_transports/asgi.py",
     "name": "create_event",
     "line": 44,
     "kind": "def",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_transports/asgi.py",
     "name": "ASGIResponseStream",
     "line": 55,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/_transports/asgi.py",
     "name": "ASGITransport",
     "line": 63,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": f
```
</details>

## Step 2

The outline of `httpx/_transports/asgi.py` has 18 bindings; a literal `__all__` at line 26; no dynamic namespace tricks. This is not the branch I planned for that outcome; the open items changed more than expected.

Chain: `httpx/_transports/asgi.py` takes `AsyncByteStream` from `.._types` (module not yet located).

Still to settle: locate the module `.._types` imported by `httpx/_transports/asgi.py`.

Next: outline `httpx/_types.py` filtered to `AsyncByteStream`, because `.._types` would be `httpx/_types.py` if that file exists; one call both checks and closes it. I expect: a definition there ends the chain (about 80%); the file does not exist (about 15%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, grep `def`/`class AsyncByteStream` statements under `.`, is expected to open more follow-up work. Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done; missing: grep `def`/`class AsyncByteStream` statements under `.`.

**Call:** `symbols('httpx/_types.py', 'AsyncByteStream')`

**Response**: outcome `def`

```
module httpx/_types.py lines=115 dynamic=no all=static@89
106 class AsyncByteStream
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/_transports/asgi.py",
    ".._types"
   ],
   "desc": "locate the module `.._types` imported by `httpx/_transports/asgi.py`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/_types.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_types.py\", \"AsyncByteStream\"]]",
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
     "httpx/_transports/asgi.py",
     ".._types"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+AsyncByteStream\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+AsyncByteStream\\\\b\", \".\"]]",
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
     "httpx/_transports/asgi.py",
     ".._types"
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
     "httpx/_transports/asgi.py",
     ".._types"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_types/__init__.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_types/__init__.py\", \"AsyncByteStream\"]]",
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
     "httpx/_transports/asgi.py",
     ".._types"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('httpx/_types.py', 'AsyncByteStream')",
  "key": "[\"symbols\", [\"httpx/_types.py\", \"AsyncByteStream\"]]",
  "provenance": "`.._types` would be `httpx/_types.py` if that file exists; one call both checks and closes it",
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
  "missing": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+AsyncByteStream\\\\b\", \".\"]]"
 },
 "adherence": {
  "planned": "done",
  "status": "deviated"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 2,
   "path": "httpx/_types.py",
   "filter": "AsyncByteStream",
   "header": {
    "lines": 115,
    "dynamic": false,
    "all_status": "static",
    "all_line": 89
   },
   "bindings": [
    {
     "module": "httpx/_types.py",
     "name": "AsyncByteStream",
     "line": 106,
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
    "httpx/_transports/asgi.py",
    "AsyncByteStream",
    "reexport",
    [
     ".._types",
     "httpx/_types.py"
    ]
   ],
   [
    "httpx/_types.py",
    "AsyncByteStream",
    "class",
    106
   ]
  ]
 }
}
```
</details>

## Step 3

In `httpx/_types.py`, `AsyncByteStream` has exactly one binding: a class at line 106. No dynamic namespace tricks, a literal `__all__` at line 89. This is not the branch I planned for that outcome; the open items changed more than expected.

Candidate modules so far: 0; statements confirmed: 0, ruled out: 0, modules with no such import: 0, pending: 0. import coverage open at `.`; star coverage open at `.`.

Outstanding: cover `.` for import lines; cover `.` for star lines.

Next: grep from-imports naming `AsyncByteStream` or star imports under `.`, because import and star lines under `.` in one call. I expect: hits under the cap (about 55%); no hits (about 40%); a capped result (about 10%). The alternative, grep from-imports naming `AsyncByteStream` under `.`, serves fewer of the open items. Plan by outcome: zero: done; mid: outline each module that appears; cap: list the scope and split it.

**Call:** `grep('^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bAsyncByteStream\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*AsyncByteStream\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$', '.')`

**Response** (capped): outcome `cap`

```
httpx/__init__.py:2:from ._api import *
httpx/__init__.py:3:from ._auth import *
httpx/__init__.py:4:from ._client import *
httpx/__init__.py:5:from ._config import *
httpx/__init__.py:6:from ._content import *
httpx/__init__.py:7:from ._exceptions import *
httpx/__init__.py:8:from ._models import *
httpx/__init__.py:9:from ._status_codes import *
httpx/__init__.py:10:from ._transports import *
httpx/__init__.py:11:from ._types import *
httpx/__init__.py:12:from ._urls import *
httpx/_client.py:34:    AsyncByteStream,
httpx/_content.py:19:    AsyncByteStream,
httpx/_models.py:36:    AsyncByteStream,
httpx/_multipart.py:11:    AsyncByteStream,
httpx/_transports/__init__.py:1:from .asgi import *
httpx/_transports/__init__.py:2:from .base import *
httpx/_transports/__init__.py:3:from .default import *
httpx/_transports/__init__.py:4:from .mock import *
httpx/_transports/__init__.py:5:from .wsgi import *
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
   "desc": "cover `.` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "."
   ],
   "desc": "cover `.` for star lines"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bAsyncByteStream\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*AsyncByteStream\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bAsyncByteStream\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*AsyncByteStream\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
   "v1": [
    23223006629,
    6996023307
   ],
   "v2": [
    23223006629,
    6996023307
   ],
   "p_cap": [
    3,
    37
   ],
   "forecast": {
    "zero": [
     14,
     37
    ],
    "mid": [
     20,
     37
    ],
    "cap": [
     3,
     37
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
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bAsyncByteStream\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*AsyncByteStream\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bAsyncByteStream\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*AsyncByteStream\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
   "v1": [
    86126677061,
    18808654410
   ],
   "v2": [
    86126677061,
    18808654410
   ],
   "p_cap": [
    1,
    36
   ],
   "forecast": {
    "zero": [
     19,
     36
    ],
    "mid": [
     4,
     9
    ],
    "cap": [
     1,
     36
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
    86126677061,
    18808654410
   ],
   "v2": [
    86126677061,
    18808654410
   ],
   "p_cap": [
    2,
    35
   ],
   "forecast": {
    "zero": [
     22,
     35
    ],
    "mid": [
     11,
     35
    ],
    "cap": [
     2,
     35
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
  "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bAsyncByteStream\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*AsyncByteStream\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
  "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bAsyncByteStream\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*AsyncByteStream\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
  "provenance": "import and star lines under `.` in one call",
  "v2": [
   23223006629,
   6996023307
  ]
 },
 "forecast": {
  "zero": [
   14,
   37
  ],
  "mid": [
   20,
   37
  ],
  "cap": [
   3,
   37
  ]
 },
 "plan": {
  "zero": "done",
  "mid": "continue",
  "cap": "continue"
 },
 "adherence": {
  "planned": "done",
  "status": "deviated"
 },
 "facts": [
  {
   "kind": "grep",
   "step": 3,
   "pattern": "^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bAsyncByteStream\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*AsyncByteStream\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$",
   "scope": ".",
   "hits": [
    [
     "httpx/__init__.py",
     2
    ],
    [
     "httpx/__init__.py",
     3
    ],
    [
     "httpx/__init__.py",
     4
    ],
    [
     "httpx/__init__.py",
     5
    ],
    [
     "httpx/__init__.py",
     6
    ],
    [
     "httpx/__init__.py",
     7
    ],
    [
     "httpx/__init__.py",
     8
    ],
    [
     "httpx/__init__.py",
     9
    ],
    [
     "httpx/__init__.py",
     10
    ],
    [
     "httpx/__init__.py",
     11
    ],
    [
     "httpx/__init__.py",
     12
    ],
    [
     "httpx/_client.py",
     34
    ],
    [
     "httpx/_content.py",
     19
    ],
    [
     "httpx/_models.py",
     36
    ],
    [
     "httpx/_multipart.py",
     11
    ],
    [
     "httpx/_transports/__init__.py",
     1
    ],
    [
     "httpx/_transports/__init__.py",
     2
    ],
    [
     "httpx/_transports/__init__.py",
     3
    ],
    [
     "httpx/_transports/__init__.py",
     4
    ],
    [
     "httpx/_transports/__init__.py",
     5
    ]
   ],
   "capped": true
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "httpx/__init__.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "httpx/_client.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "httpx/_content.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "httpx/_models.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "httpx/_multipart.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "httpx/_transports/__init__.py",
    0,
    "pending",
    "outline not yet seen"
   ]
  ],
  "uncovered": {
   "IMPORT": [
    [
     "split",
     "."
    ]
   ],
   "STAR": [
    [
     "split",
     "."
    ]
   ]
  }
 }
}
```
</details>

## Step 4

The grep under `.` hit the cap at 20 lines, so it proves nothing about what else is there.

Candidate modules so far: 6; statements confirmed: 0, ruled out: 0, modules with no such import: 0, pending: 6. import coverage open at `.`; star coverage open at `.`.

Outstanding: list `.` to split a capped grep; outline `httpx/__init__.py` for its `AsyncByteStream` imports; outline `httpx/_client.py` for its `AsyncByteStream` imports; outline `httpx/_content.py` for its `AsyncByteStream` imports; and 3 more.

Next: outline `httpx/__init__.py` filtered to `AsyncByteStream`, because `httpx/__init__.py` had a matching line (step 3); its outline names every `AsyncByteStream` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `httpx/_client.py` filtered to `AsyncByteStream`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `httpx/_client.py` filtered to `AsyncByteStream`; cap: outline `httpx/_client.py` filtered to `AsyncByteStream`.

**Call:** `symbols('httpx/__init__.py', 'AsyncByteStream')`

**Response**: outcome `ok`

```
module httpx/__init__.py lines=107 dynamic=no all=static@29
2 star <- ._api
3 star <- ._auth
4 star <- ._client
5 star <- ._config
6 star <- ._content
7 star <- ._exceptions
8 star <- ._models
9 star <- ._status_codes
10 star <- ._transports
11 star <- ._types
12 star <- ._urls
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/__init__.py",
    "AsyncByteStream"
   ],
   "desc": "outline `httpx/__init__.py` for its `AsyncByteStream` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_client.py",
    "AsyncByteStream"
   ],
   "desc": "outline `httpx/_client.py` for its `AsyncByteStream` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_content.py",
    "AsyncByteStream"
   ],
   "desc": "outline `httpx/_content.py` for its `AsyncByteStream` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_models.py",
    "AsyncByteStream"
   ],
   "desc": "outline `httpx/_models.py` for its `AsyncByteStream` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_multipart.py",
    "AsyncByteStream"
   ],
   "desc": "outline `httpx/_multipart.py` for its `AsyncByteStream` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_transports/__init__.py",
    "AsyncByteStream"
   ],
   "desc": "outline `httpx/_transports/__init__.py` for its `AsyncByteStream` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/__init__.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/__init__.py\", \"AsyncByteStream\"]]",
   "v1": [
    26721135607,
    1492750350
   ],
   "v2": [
    13375495307,
    746375175
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
     "httpx/__init__.py",
     "AsyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_client.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_client.py\", \"AsyncByteStream\"]]",
   "v1": [
    26721135607,
    1492750350
   ],
   "v2": [
    13375495307,
    746375175
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
     "AsyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_content.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_content.py\", \"AsyncByteStream\"]]",
   "v1": [
    26721135607,
    1492750350
   ],
   "v2": [
    13375495307,
    746375175
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
     "AsyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_models.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_models.py\", \"AsyncByteStream\"]]",
   "v1": [
    26721135607,
    1492750350
   ],
   "v2": [
    13375495307,
    746375175
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
     "httpx/_models.py",
     "AsyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_multipart.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_multipart.py\", \"AsyncByteStream\"]]",
   "v1": [
    26721135607,
    1492750350
   ],
   "v2": [
    13375495307,
    746375175
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
     "AsyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/__init__.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/__init__.py\", \"AsyncByteStream\"]]",
   "v1": [
    26721135607,
    1492750350
   ],
   "v2": [
    13375495307,
    746375175
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
     "httpx/_transports/__init__.py",
     "AsyncByteStream"
    ]
   ]
  },
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    540460058,
    29855007
   ],
   "v2": [
    27052857907,
    1492750350
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
     "split",
     "."
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('httpx/__init__.py', 'AsyncByteStream')",
  "key": "[\"symbols\", [\"httpx/__init__.py\", \"AsyncByteStream\"]]",
  "provenance": "`httpx/__init__.py` had a matching line (step 3); its outline names every `AsyncByteStream` import exactly",
  "v2": [
   13375495307,
   746375175
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
  "ok": "[\"symbols\", [\"httpx/_client.py\", \"AsyncByteStream\"]]",
  "cap": "[\"symbols\", [\"httpx/_client.py\", \"AsyncByteStream\"]]"
 },
 "adherence": {
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 4,
   "path": "httpx/__init__.py",
   "filter": "AsyncByteStream",
   "header": {
    "lines": 107,
    "dynamic": false,
    "all_status": "static",
    "all_line": 29
   },
   "bindings": [
    {
     "module": "httpx/__init__.py",
     "name": "*",
     "line": 2,
     "kind": "star",
     "src": "._api",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/__init__.py",
     "name": "*",
     "line": 3,
     "kind": "star",
     "src": "._auth",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/__init__.py",
     "name": "*",
     "line": 4,
     "kind": "star",
     "src": "._client",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/__init__.py",
     "name": "*",
     "line": 5,
     "kind": "star",
     "src"
```
</details>

## Step 5

`httpx/__init__.py` binds no `AsyncByteStream` at module level; 11 star import(s): `._api`, `._auth`, `._client`, `._config`, `._content`, `._exceptions`, `._models`, `._status_codes`, `._transports`, `._types`, `._urls`; a literal `__all__` at line 29; no dynamic namespace tricks. The call I had planned for this outcome is no longer useful, so I am re-planning.

Candidate modules so far: 6; statements confirmed: 0, ruled out: 0, modules with no such import: 0, pending: 16. import coverage open at `.`; star coverage open at `.`.

Still to settle: list `.` to split a capped grep; locate the module `._api` imported by `httpx/__init__.py`; locate the module `._auth` imported by `httpx/__init__.py`; know what `httpx/_client.py` exports; and 13 more.

Next: grep `def`/`class AsyncByteStream` statements under `.`, because a `def`/`class AsyncByteStream` statement would reveal the module file; `AsyncByteStream` task. I expect: hits under the cap (about 95%); a capped result (about 5%); no hits (about 5%). The alternative, list `httpx`, costs more in expectation. Plan by outcome: zero: list `httpx`; mid: outline `httpx/_client.py` filtered to `AsyncByteStream`; cap: list `httpx`.

**Call:** `grep('^\\s*(?:async\\s+)?(?:def|class)\\s+AsyncByteStream\\b', '.')`

**Response**: outcome `mid`

```
httpx/_types.py:106:class AsyncByteStream:
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._api"
   ],
   "desc": "locate the module `._api` imported by `httpx/__init__.py`"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._auth"
   ],
   "desc": "locate the module `._auth` imported by `httpx/__init__.py`"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_client.py"
   ],
   "desc": "know what `httpx/_client.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._config"
   ],
   "desc": "locate the module `._config` imported by `httpx/__init__.py`"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_content.py"
   ],
   "desc": "know what `httpx/_content.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._exceptions"
   ],
   "desc": "locate the module `._exceptions` imported by `httpx/__init__.py`"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_models.py"
   ],
   "desc": "know what `httpx/_models.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._status_codes"
   ],
   "desc": "locate the module `._status_codes` imported by `httpx/__init__.py`"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._transports"
   ],
   "desc": "locate the module `._transports` imported by `httpx/__init__.py`"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._urls"
   ],
   "desc": "locate the module `._urls` imported by `httpx/__init__.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_client.py",
    "AsyncByteStream"
   ],
   "desc": "outline `httpx/_client.py` for its `AsyncByteStream` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_content.py",
    "AsyncByteStream"
   ],
   "desc": "outline `httpx/_content.py` for its `AsyncByteStream` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_models.py",
    "AsyncByteStream"
   ],
   "desc": "outline `httpx/_models.py` for its `AsyncByteStream` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_multipart.py",
    "AsyncByteStream"
   ],
   "desc": "outline `httpx/_multipart.py` for its `AsyncByteStream` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_transports/__init__.py",
    "AsyncByteStream"
   ],
   "desc": "outline `httpx/_transports/__init__.py` for its `AsyncByteStream` imports"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+AsyncByteStream\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+AsyncByteStream\\\\b\", \".\"]]",
   "v1": [
    868967405,
    29855007
   ],
   "v2": [
    6927199372,
    248791725
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
     "httpx/__init__.py",
     "._api"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._auth"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._config"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._exceptions"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._status_codes"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._transports"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._urls"
    ]
   ]
  },
  {
   "call": "ls('httpx')",
   "key": "[\"ls\", [\"httpx\"]]",
   "v1": [
    582603407,
    19903338
   ],
   "v2": [
    41632324109,
    1492750350
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
     "httpx/__init__.py",
     "._api"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._auth"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._config"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._exceptions"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._status_codes"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._transports"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._urls"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_client.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_client.py\", \"AsyncByteStream\"]]",
   "v1": [
    25125596957,
    746375175
   ],
   "v2": [
    21007664957,
    746375175
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
     "all",
     "httpx/_client.py"
    ],
    [
     "outline",
     "httpx/_client.py",
     "AsyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_content.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_content.py\", \"AsyncByteStream\"]]",
   "v1": [
    25125596957,
    746375175
   ],
   "v2": [
    21007664957,
    746375175
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
     "all",
     "httpx/_content.py"
    ],
    [
     "outline",
     "httpx/_content.py",
     "AsyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_models.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_models.py\", \"AsyncByteStream\"]]",
   "v1": [
    25125596957,
    746375175
   ]
```
</details>

## Step 6

The grep under `.` returned 1 lines, under the cap, so these are all of them: `httpx/_types.py`.

Candidate modules so far: 6; statements confirmed: 0, ruled out: 0, modules with no such import: 0, pending: 16. import coverage open at `.`; star coverage open at `.`.

Open: list `.` to split a capped grep; locate the module `._api` imported by `httpx/__init__.py`; locate the module `._auth` imported by `httpx/__init__.py`; know what `httpx/_client.py` exports; and 13 more.

Next: outline `httpx/_client.py` filtered to `AsyncByteStream`, because module `httpx/_client.py` (step 3). I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, list `httpx`, is expected to open more follow-up work. Plan by outcome: ok: list `httpx`; cap: list `httpx`.

**Call:** `symbols('httpx/_client.py', 'AsyncByteStream')`

**Response**: outcome `reexport`

```
module httpx/_client.py lines=2020 dynamic=no all=static@54
33 from AsyncByteStream <- ._types AsyncByteStream
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._api"
   ],
   "desc": "locate the module `._api` imported by `httpx/__init__.py`"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._auth"
   ],
   "desc": "locate the module `._auth` imported by `httpx/__init__.py`"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_client.py"
   ],
   "desc": "know what `httpx/_client.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._config"
   ],
   "desc": "locate the module `._config` imported by `httpx/__init__.py`"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_content.py"
   ],
   "desc": "know what `httpx/_content.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._exceptions"
   ],
   "desc": "locate the module `._exceptions` imported by `httpx/__init__.py`"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_models.py"
   ],
   "desc": "know what `httpx/_models.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._status_codes"
   ],
   "desc": "locate the module `._status_codes` imported by `httpx/__init__.py`"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._transports"
   ],
   "desc": "locate the module `._transports` imported by `httpx/__init__.py`"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._urls"
   ],
   "desc": "locate the module `._urls` imported by `httpx/__init__.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_client.py",
    "AsyncByteStream"
   ],
   "desc": "outline `httpx/_client.py` for its `AsyncByteStream` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_content.py",
    "AsyncByteStream"
   ],
   "desc": "outline `httpx/_content.py` for its `AsyncByteStream` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_models.py",
    "AsyncByteStream"
   ],
   "desc": "outline `httpx/_models.py` for its `AsyncByteStream` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_multipart.py",
    "AsyncByteStream"
   ],
   "desc": "outline `httpx/_multipart.py` for its `AsyncByteStream` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_transports/__init__.py",
    "AsyncByteStream"
   ],
   "desc": "outline `httpx/_transports/__init__.py` for its `AsyncByteStream` imports"
  }
 ],
 "candidates": [
  {
   "call": "ls('httpx')",
   "key": "[\"ls\", [\"httpx\"]]",
   "v1": [
    582603407,
    19903338
   ],
   "v2": [
    14087405063,
    497583450
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
     "httpx/__init__.py",
     "._api"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._auth"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._config"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._exceptions"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._status_codes"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._transports"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._urls"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_client.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_client.py\", \"AsyncByteStream\"]]",
   "v1": [
    25125596957,
    746375175
   ],
   "v2": [
    14087405063,
    497583450
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
     "all",
     "httpx/_client.py"
    ],
    [
     "outline",
     "httpx/_client.py",
     "AsyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_content.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_content.py\", \"AsyncByteStream\"]]",
   "v1": [
    25125596957,
    746375175
   ],
   "v2": [
    14087405063,
    497583450
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
     "all",
     "httpx/_content.py"
    ],
    [
     "outline",
     "httpx/_content.py",
     "AsyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_models.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_models.py\", \"AsyncByteStream\"]]",
   "v1": [
    25125596957,
    746375175
   ],
   "v2": [
    14087405063,
    497583450
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
     "all",
     "httpx/_models.py"
    ],
    [
     "outline",
     "httpx/_models.py",
     "AsyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_multipart.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_multipart.py\", \"AsyncByteStream\"]]",
   "v1": [
    51714089257,
    1492750350
   ],
   "v2": [
    7287518422,
    248791725
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
     "AsyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/__init__.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/__init__.py\", \"AsyncByteStream\"]]",
   "v1": [
    51714089257,
    1492750350
   ],
```
</details>

## Step 7

In `httpx/_client.py`, `AsyncByteStream` has exactly one binding: line 33 imports it as `AsyncByteStream` from `._types`. No dynamic namespace tricks, a literal `__all__` at line 54. That outcome was not one I had forecast, so there was no branch for it; re-planning from the open items.

Candidate modules so far: 6; statements confirmed: 1, ruled out: 0, modules with no such import: 0, pending: 15. import coverage open at `.`; star coverage open at `.`.

Open: list `.` to split a capped grep; locate the module `._api` imported by `httpx/__init__.py`; locate the module `._auth` imported by `httpx/__init__.py`; know what `httpx/_client.py` exports; and 12 more.

Next: outline `httpx/_models.py` filtered to `AsyncByteStream`, because module `httpx/_models.py` (step 3). I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, list `httpx`, is expected to open more follow-up work. Plan by outcome: ok: list `httpx`; cap: list `httpx`.

**Call:** `symbols('httpx/_models.py', 'AsyncByteStream')`

**Response**: outcome `reexport`

```
module httpx/_models.py lines=1278 dynamic=no all=static@51
35 from AsyncByteStream <- ._types AsyncByteStream
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._api"
   ],
   "desc": "locate the module `._api` imported by `httpx/__init__.py`"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._auth"
   ],
   "desc": "locate the module `._auth` imported by `httpx/__init__.py`"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_client.py"
   ],
   "desc": "know what `httpx/_client.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._config"
   ],
   "desc": "locate the module `._config` imported by `httpx/__init__.py`"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_content.py"
   ],
   "desc": "know what `httpx/_content.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._exceptions"
   ],
   "desc": "locate the module `._exceptions` imported by `httpx/__init__.py`"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_models.py"
   ],
   "desc": "know what `httpx/_models.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._status_codes"
   ],
   "desc": "locate the module `._status_codes` imported by `httpx/__init__.py`"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._transports"
   ],
   "desc": "locate the module `._transports` imported by `httpx/__init__.py`"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._urls"
   ],
   "desc": "locate the module `._urls` imported by `httpx/__init__.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_content.py",
    "AsyncByteStream"
   ],
   "desc": "outline `httpx/_content.py` for its `AsyncByteStream` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_models.py",
    "AsyncByteStream"
   ],
   "desc": "outline `httpx/_models.py` for its `AsyncByteStream` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_multipart.py",
    "AsyncByteStream"
   ],
   "desc": "outline `httpx/_multipart.py` for its `AsyncByteStream` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_transports/__init__.py",
    "AsyncByteStream"
   ],
   "desc": "outline `httpx/_transports/__init__.py` for its `AsyncByteStream` imports"
  }
 ],
 "candidates": [
  {
   "call": "ls('httpx')",
   "key": "[\"ls\", [\"httpx\"]]",
   "v1": [
    552262481,
    19903338
   ],
   "v2": [
    13328881913,
    497583450
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
     "httpx/__init__.py",
     "._api"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._auth"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._config"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._exceptions"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._status_codes"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._transports"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._urls"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_content.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_content.py\", \"AsyncByteStream\"]]",
   "v1": [
    23987812232,
    746375175
   ],
   "v2": [
    13328881913,
    497583450
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
     "all",
     "httpx/_content.py"
    ],
    [
     "outline",
     "httpx/_content.py",
     "AsyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_models.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_models.py\", \"AsyncByteStream\"]]",
   "v1": [
    23987812232,
    746375175
   ],
   "v2": [
    13328881913,
    497583450
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
     "all",
     "httpx/_models.py"
    ],
    [
     "outline",
     "httpx/_models.py",
     "AsyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_multipart.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_multipart.py\", \"AsyncByteStream\"]]",
   "v1": [
    49438519807,
    1492750350
   ],
   "v2": [
    6908256847,
    248791725
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
     "AsyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/__init__.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/__init__.py\", \"AsyncByteStream\"]]",
   "v1": [
    49438519807,
    1492750350
   ],
   "v2": [
    6908256847,
    248791725
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
     "httpx/_transports/__init__.py",
     "AsyncByteStream"
    ]
   ]
  },
  {
   "call": "read('httpx/_client.py', 54, 30)",
   "key": "[\"read\", [\"httpx/_client.py\", 54, 30]]",
   "v1": [
    4970721487,
    149275035
   ],
   "v2": [
    2781215743,
    99516690
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_client.py"
    ]
   ]
  },
  {
 
```
</details>

## Step 8

In `httpx/_models.py`, `AsyncByteStream` has exactly one binding: line 35 imports it as `AsyncByteStream` from `._types`. No dynamic namespace tricks, a literal `__all__` at line 51. That outcome was not one I had forecast, so there was no branch for it; re-planning from the open items.

Candidate modules so far: 6; statements confirmed: 2, ruled out: 0, modules with no such import: 0, pending: 14. import coverage open at `.`; star coverage open at `.`.

Outstanding: list `.` to split a capped grep; locate the module `._api` imported by `httpx/__init__.py`; locate the module `._auth` imported by `httpx/__init__.py`; know what `httpx/_client.py` exports; and 11 more.

Next: outline `httpx/_content.py` filtered to `AsyncByteStream`, because module `httpx/_content.py` (step 3). I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, list `httpx`, is expected to open more follow-up work. Plan by outcome: ok: list `httpx`; cap: list `httpx`.

**Call:** `symbols('httpx/_content.py', 'AsyncByteStream')`

**Response**: outcome `reexport`

```
module httpx/_content.py lines=241 dynamic=no all=static@28
18 from AsyncByteStream <- ._types AsyncByteStream
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._api"
   ],
   "desc": "locate the module `._api` imported by `httpx/__init__.py`"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._auth"
   ],
   "desc": "locate the module `._auth` imported by `httpx/__init__.py`"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_client.py"
   ],
   "desc": "know what `httpx/_client.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._config"
   ],
   "desc": "locate the module `._config` imported by `httpx/__init__.py`"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_content.py"
   ],
   "desc": "know what `httpx/_content.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._exceptions"
   ],
   "desc": "locate the module `._exceptions` imported by `httpx/__init__.py`"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_models.py"
   ],
   "desc": "know what `httpx/_models.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._status_codes"
   ],
   "desc": "locate the module `._status_codes` imported by `httpx/__init__.py`"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._transports"
   ],
   "desc": "locate the module `._transports` imported by `httpx/__init__.py`"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._urls"
   ],
   "desc": "locate the module `._urls` imported by `httpx/__init__.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_content.py",
    "AsyncByteStream"
   ],
   "desc": "outline `httpx/_content.py` for its `AsyncByteStream` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_multipart.py",
    "AsyncByteStream"
   ],
   "desc": "outline `httpx/_multipart.py` for its `AsyncByteStream` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_transports/__init__.py",
    "AsyncByteStream"
   ],
   "desc": "outline `httpx/_transports/__init__.py` for its `AsyncByteStream` imports"
  }
 ],
 "candidates": [
  {
   "call": "ls('httpx')",
   "key": "[\"ls\", [\"httpx\"]]",
   "v1": [
    17997295,
    686322
   ],
   "v2": [
    433460647,
    17158050
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
     "httpx/__init__.py",
     "._api"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._auth"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._config"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._exceptions"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._status_codes"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._transports"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._urls"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_content.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_content.py\", \"AsyncByteStream\"]]",
   "v1": [
    787931983,
    25737075
   ],
   "v2": [
    433460647,
    17158050
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
     "all",
     "httpx/_content.py"
    ],
    [
     "outline",
     "httpx/_content.py",
     "AsyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_multipart.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_multipart.py\", \"AsyncByteStream\"]]",
   "v1": [
    1626308633,
    51474150
   ],
   "v2": [
    225137768,
    8579025
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
     "AsyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/__init__.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/__init__.py\", \"AsyncByteStream\"]]",
   "v1": [
    1626308633,
    51474150
   ],
   "v2": [
    225137768,
    8579025
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
     "httpx/_transports/__init__.py",
     "AsyncByteStream"
    ]
   ]
  },
  {
   "call": "read('httpx/_client.py', 54, 30)",
   "key": "[\"read\", [\"httpx/_client.py\", 54, 30]]",
   "v1": [
    163557398,
    5147415
   ],
   "v2": [
    90672797,
    3431610
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_client.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_models.py', 51, 30)",
   "key": "[\"read\", [\"httpx/_models.py\", 51, 30]]",
   "v1": [
    163557398,
    5147415
   ],
   "v2": [
    90672797,
    3431610
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_models.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_types.py', 89, 30)",
   "key": "[\"read\", [\"httpx/_types.py\", 89, 30]]",
   "v1": [
    163557398,
    5147415
   ],
   "v2": [
    90672797,
    3431610
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
  
```
</details>

## Step 9

In `httpx/_content.py`, `AsyncByteStream` has exactly one binding: line 18 imports it as `AsyncByteStream` from `._types`. No dynamic namespace tricks, a literal `__all__` at line 28. That outcome was not one I had forecast, so there was no branch for it; re-planning from the open items.

Candidate modules so far: 6; statements confirmed: 3, ruled out: 0, modules with no such import: 0, pending: 13. import coverage open at `.`; star coverage open at `.`.

Still to settle: list `.` to split a capped grep; locate the module `._api` imported by `httpx/__init__.py`; locate the module `._auth` imported by `httpx/__init__.py`; know what `httpx/_client.py` exports; and 10 more.

Next: list `httpx`, because `._api` imported by `httpx/__init__.py` should live under `httpx`. I expect: a complete listing settles which files exist (about 90%); a capped listing settles nothing (about 10%). The alternative, outline `httpx/_multipart.py` filtered to `AsyncByteStream`, serves fewer of the open items. Plan by outcome: complete: outline `httpx/_multipart.py` filtered to `AsyncByteStream`; cap: outline `httpx/_api.py` filtered to `AsyncByteStream`.

**Call:** `ls('httpx')`

**Response**: outcome `complete`

```
__init__.py
__version__.py
_api.py
_auth.py
_client.py
_config.py
_content.py
_decoders.py
_exceptions.py
_main.py
_models.py
_multipart.py
_status_codes.py
_transports/
_types.py
_urlparse.py
_urls.py
_utils.py
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._api"
   ],
   "desc": "locate the module `._api` imported by `httpx/__init__.py`"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._auth"
   ],
   "desc": "locate the module `._auth` imported by `httpx/__init__.py`"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_client.py"
   ],
   "desc": "know what `httpx/_client.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._config"
   ],
   "desc": "locate the module `._config` imported by `httpx/__init__.py`"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_content.py"
   ],
   "desc": "know what `httpx/_content.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._exceptions"
   ],
   "desc": "locate the module `._exceptions` imported by `httpx/__init__.py`"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_models.py"
   ],
   "desc": "know what `httpx/_models.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._status_codes"
   ],
   "desc": "locate the module `._status_codes` imported by `httpx/__init__.py`"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._transports"
   ],
   "desc": "locate the module `._transports` imported by `httpx/__init__.py`"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._urls"
   ],
   "desc": "locate the module `._urls` imported by `httpx/__init__.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_multipart.py",
    "AsyncByteStream"
   ],
   "desc": "outline `httpx/_multipart.py` for its `AsyncByteStream` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_transports/__init__.py",
    "AsyncByteStream"
   ],
   "desc": "outline `httpx/_transports/__init__.py` for its `AsyncByteStream` imports"
  }
 ],
 "candidates": [
  {
   "call": "ls('httpx')",
   "key": "[\"ls\", [\"httpx\"]]",
   "v1": [
    491580629,
    19903338
   ],
   "v2": [
    566442992072411,
    22979245785300
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
     "httpx/__init__.py",
     "._api"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._auth"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._config"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._exceptions"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._status_codes"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._transports"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._urls"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_multipart.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_multipart.py\", \"AsyncByteStream\"]]",
   "v1": [
    44887380907,
    1492750350
   ],
   "v2": [
    6149733697,
    248791725
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
     "AsyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/__init__.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/__init__.py\", \"AsyncByteStream\"]]",
   "v1": [
    44887380907,
    1492750350
   ],
   "v2": [
    6149733697,
    248791725
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
     "httpx/_transports/__init__.py",
     "AsyncByteStream"
    ]
   ]
  },
  {
   "call": "read('httpx/_client.py', 54, 30)",
   "key": "[\"read\", [\"httpx/_client.py\", 54, 30]]",
   "v1": [
    4515607597,
    149275035
   ],
   "v2": [
    2477806483,
    99516690
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_client.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_content.py', 28, 30)",
   "key": "[\"read\", [\"httpx/_content.py\", 28, 30]]",
   "v1": [
    4515607597,
    149275035
   ],
   "v2": [
    2477806483,
    99516690
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_content.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_models.py', 51, 30)",
   "key": "[\"read\", [\"httpx/_models.py\", 51, 30]]",
   "v1": [
    4515607597,
    149275035
   ],
   "v2": [
    2477806483,
    99516690
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_models.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_types.py', 89, 30)",
   "key": "[\"read\", [\"httpx/_types.py\", 89, 30]]",
   "v1": [
    4515607597,
    149275035
   ],
   "v2": [
    2477806483,
    99516690
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_types.py"
    ]
   ]
  },
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    903784964,
    29855007
   ],
   "v2": [
    165334531,
    6634446
   ],
   "p_cap": [
    2,
    9
   ],
   "forecast"
```
</details>

## Step 10

`httpx` lists 18 entries (complete): `__init__.py`, `__version__.py`, `_api.py`, `_auth.py`, `_client.py`, `_config.py` and 12 more.

Candidate modules so far: 6; statements confirmed: 3, ruled out: 0, modules with no such import: 0, pending: 13. import coverage open at `.`; star coverage open at `.`.

Still to settle: list `.` to split a capped grep; know what `httpx/_api.py` exports; know what `httpx/_auth.py` exports; know what `httpx/_client.py` exports; and 10 more.

Next: outline `httpx/_multipart.py` filtered to `AsyncByteStream`, because `httpx/_multipart.py` had a matching line (step 3); its outline names every `AsyncByteStream` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `httpx/_transports/__init__.py` filtered to `AsyncByteStream`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `httpx/_transports/__init__.py` filtered to `AsyncByteStream`; cap: outline `httpx/_transports/__init__.py` filtered to `AsyncByteStream`.

**Call:** `symbols('httpx/_multipart.py', 'AsyncByteStream')`

**Response**: outcome `ok`

```
module httpx/_multipart.py lines=301 dynamic=no all=none
10 from AsyncByteStream <- ._types AsyncByteStream
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_api.py"
   ],
   "desc": "know what `httpx/_api.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_auth.py"
   ],
   "desc": "know what `httpx/_auth.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_client.py"
   ],
   "desc": "know what `httpx/_client.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_config.py"
   ],
   "desc": "know what `httpx/_config.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_content.py"
   ],
   "desc": "know what `httpx/_content.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_exceptions.py"
   ],
   "desc": "know what `httpx/_exceptions.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_models.py"
   ],
   "desc": "know what `httpx/_models.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_status_codes.py"
   ],
   "desc": "know what `httpx/_status_codes.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/__init__.py"
   ],
   "desc": "know what `httpx/_transports/__init__.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_urls.py"
   ],
   "desc": "know what `httpx/_urls.py` exports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_multipart.py",
    "AsyncByteStream"
   ],
   "desc": "outline `httpx/_multipart.py` for its `AsyncByteStream` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_transports/__init__.py",
    "AsyncByteStream"
   ],
   "desc": "outline `httpx/_transports/__init__.py` for its `AsyncByteStream` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/_multipart.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_multipart.py\", \"AsyncByteStream\"]]",
   "v1": [
    34039111657,
    1492750350
   ],
   "v2": [
    32606071321,
    1492750350
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
     "AsyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/__init__.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/__init__.py\", \"AsyncByteStream\"]]",
   "v1": [
    16288108157,
    746375175
   ],
   "v2": [
    32606071321,
    1492750350
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
     "all",
     "httpx/_transports/__init__.py"
    ],
    [
     "outline",
     "httpx/_transports/__init__.py",
     "AsyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_api.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_api.py\", \"AsyncByteStream\"]]",
   "v1": [
    21528534394243,
    943358511186
   ],
   "v2": [
    515572755587611,
    23583962779650
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_api.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_auth.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_auth.py\", \"AsyncByteStream\"]]",
   "v1": [
    21528534394243,
    943358511186
   ],
   "v2": [
    515572755587611,
    23583962779650
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_auth.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_config.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_config.py\", \"AsyncByteStream\"]]",
   "v1": [
    21528534394243,
    943358511186
   ],
   "v2": [
    515572755587611,
    23583962779650
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_config.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_exceptions.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_exceptions.py\", \"AsyncByteStream\"]]",
   "v1": [
    21528534394243,
    943358511186
   ],
   "v2": [
    515572755587611,
    23583962779650
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_exceptions.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_status_codes.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_status_codes.py\", \"AsyncByteStream\"]]",
   "v1": [
    21528534394243,
    943358511186
   ],
   "v2": [
    515572755587611,
    23583962779650
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_status_codes.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_urls.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_urls.py\", \"AsyncByteStream\"]]",
   "v1": [
    21528534394243,
    943358511186
   ],
   "v2": [
    515572755587611,
    23583962779650
   ],
   "p_cap": [
    0,
    1
   ],
   "fore
```
</details>

## Step 11

In `httpx/_multipart.py`, `AsyncByteStream` has exactly one binding: line 10 imports it as `AsyncByteStream` from `._types`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 6; statements confirmed: 4, ruled out: 0, modules with no such import: 0, pending: 12. import coverage open at `.`; star coverage open at `.`.

Outstanding: list `.` to split a capped grep; know what `httpx/_api.py` exports; know what `httpx/_auth.py` exports; know what `httpx/_client.py` exports; and 9 more.

Next: outline `httpx/_transports/__init__.py` filtered to `AsyncByteStream`, because module `httpx/_transports/__init__.py` (step 3). I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `httpx/_api.py` filtered to `AsyncByteStream`, serves fewer of the open items. Plan by outcome: ok: outline `httpx/_api.py` filtered to `AsyncByteStream`; cap: outline `httpx/_api.py` filtered to `AsyncByteStream`.

**Call:** `symbols('httpx/_transports/__init__.py', 'AsyncByteStream')`

**Response**: outcome `star`

```
module httpx/_transports/__init__.py lines=16 dynamic=no all=static@7
1 star <- .asgi
2 star <- .base
3 star <- .default
4 star <- .mock
5 star <- .wsgi
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_api.py"
   ],
   "desc": "know what `httpx/_api.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_auth.py"
   ],
   "desc": "know what `httpx/_auth.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_client.py"
   ],
   "desc": "know what `httpx/_client.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_config.py"
   ],
   "desc": "know what `httpx/_config.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_content.py"
   ],
   "desc": "know what `httpx/_content.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_exceptions.py"
   ],
   "desc": "know what `httpx/_exceptions.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_models.py"
   ],
   "desc": "know what `httpx/_models.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_status_codes.py"
   ],
   "desc": "know what `httpx/_status_codes.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/__init__.py"
   ],
   "desc": "know what `httpx/_transports/__init__.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_urls.py"
   ],
   "desc": "know what `httpx/_urls.py` exports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_transports/__init__.py",
    "AsyncByteStream"
   ],
   "desc": "outline `httpx/_transports/__init__.py` for its `AsyncByteStream` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/_api.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_api.py\", \"AsyncByteStream\"]]",
   "v1": [
    20090465524621,
    943358511186
   ],
   "v2": [
    479621033847061,
    23583962779650
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_api.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_auth.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_auth.py\", \"AsyncByteStream\"]]",
   "v1": [
    20090465524621,
    943358511186
   ],
   "v2": [
    479621033847061,
    23583962779650
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_auth.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_config.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_config.py\", \"AsyncByteStream\"]]",
   "v1": [
    20090465524621,
    943358511186
   ],
   "v2": [
    479621033847061,
    23583962779650
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_config.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_exceptions.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_exceptions.py\", \"AsyncByteStream\"]]",
   "v1": [
    20090465524621,
    943358511186
   ],
   "v2": [
    479621033847061,
    23583962779650
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_exceptions.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_status_codes.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_status_codes.py\", \"AsyncByteStream\"]]",
   "v1": [
    20090465524621,
    943358511186
   ],
   "v2": [
    479621033847061,
    23583962779650
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_status_codes.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/__init__.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/__init__.py\", \"AsyncByteStream\"]]",
   "v1": [
    15150323432,
    746375175
   ],
   "v2": [
    479621033847061,
    23583962779650
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
     "all",
     "httpx/_transports/__init__.py"
    ],
    [
     "outline",
     "httpx/_transports/__init__.py",
     "AsyncByteStream"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_urls.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_urls.py\", \"AsyncByteStream\"]]",
   "v1": [
    20090465524621,
    943358511186
   ],
   "v2": [
    479621033847061,
    23583962779650
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_urls.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_client.py', 54, 30)",
   "key": "[\"read\", [\"httpx/_client.py\", 54, 30]]",
   "v1": [
    3203223727,
    149275035
   ],
   "v2": [
    15299598467,
    746375175
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_client.py"
    ]
   ]
  },
  {
   "cal
```
</details>

## Step 12

`httpx/_transports/__init__.py` binds no `AsyncByteStream` at module level; 5 star import(s): `.asgi`, `.base`, `.default`, `.mock`, `.wsgi`; a literal `__all__` at line 7; no dynamic namespace tricks. That outcome was not one I had forecast, so there was no branch for it; re-planning from the open items.

Candidate modules so far: 6; statements confirmed: 4, ruled out: 0, modules with no such import: 0, pending: 16. import coverage open at `.`; star coverage open at `.`.

Open: list `.` to split a capped grep; know what `httpx/_api.py` exports; know what `httpx/_auth.py` exports; know what `httpx/_client.py` exports; and 13 more.

Next: list `httpx/_transports`, because `.base` imported by `httpx/_transports/__init__.py` should live under `httpx/_transports`. I expect: a complete listing settles which files exist (near certain); a capped listing settles nothing (under 5%). The alternative, outline `httpx/_api.py` filtered to `AsyncByteStream`, serves fewer of the open items. Plan by outcome: complete: outline `httpx/_api.py` filtered to `AsyncByteStream`; cap: outline `httpx/_transports/base.py` filtered to `AsyncByteStream`.

**Call:** `ls('httpx/_transports')`

**Response**: outcome `complete`

```
__init__.py
asgi.py
base.py
default.py
mock.py
wsgi.py
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_api.py"
   ],
   "desc": "know what `httpx/_api.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_auth.py"
   ],
   "desc": "know what `httpx/_auth.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_client.py"
   ],
   "desc": "know what `httpx/_client.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_config.py"
   ],
   "desc": "know what `httpx/_config.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_content.py"
   ],
   "desc": "know what `httpx/_content.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_exceptions.py"
   ],
   "desc": "know what `httpx/_exceptions.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_models.py"
   ],
   "desc": "know what `httpx/_models.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_status_codes.py"
   ],
   "desc": "know what `httpx/_status_codes.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/__init__.py"
   ],
   "desc": "know what `httpx/_transports/__init__.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_urls.py"
   ],
   "desc": "know what `httpx/_urls.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/asgi.py"
   ],
   "desc": "know what `httpx/_transports/asgi.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/_transports/__init__.py",
    ".base"
   ],
   "desc": "locate the module `.base` imported by `httpx/_transports/__init__.py`"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/_transports/__init__.py",
    ".default"
   ],
   "desc": "locate the module `.default` imported by `httpx/_transports/__init__.py`"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/_transports/__init__.py",
    ".mock"
   ],
   "desc": "locate the module `.mock` imported by `httpx/_transports/__init__.py`"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/_transports/__init__.py",
    ".wsgi"
   ],
   "desc": "locate the module `.wsgi` imported by `httpx/_transports/__init__.py`"
  }
 ],
 "candidates": [
  {
   "call": "ls('httpx/_transports')",
   "key": "[\"ls\", [\"httpx/_transports\"]]",
   "v1": [
    24043730279,
    925505217
   ],
   "v2": [
    7223254448064212,
    277819081544277
   ],
   "p_cap": [
    5,
    217
   ],
   "forecast": {
    "complete": [
     212,
     217
    ],
    "cap": [
     5,
     217
    ]
   },
   "serves": [
    [
     "module_path",
     "httpx/_transports/__init__.py",
     ".base"
    ],
    [
     "module_path",
     "httpx/_transports/__init__.py",
     ".default"
    ],
    [
     "module_path",
     "httpx/_transports/__init__.py",
     ".mock"
    ],
    [
     "module_path",
     "httpx/_transports/__init__.py",
     ".wsgi"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_api.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_api.py\", \"AsyncByteStream\"]]",
   "v1": [
    27286716202489,
    943358511186
   ],
   "v2": [
    760851170768821,
    29244113846766
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_api.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_auth.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_auth.py\", \"AsyncByteStream\"]]",
   "v1": [
    27286716202489,
    943358511186
   ],
   "v2": [
    760851170768821,
    29244113846766
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_auth.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_config.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_config.py\", \"AsyncByteStream\"]]",
   "v1": [
    27286716202489,
    943358511186
   ],
   "v2": [
    760851170768821,
    29244113846766
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_config.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_exceptions.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_exceptions.py\", \"AsyncByteStream\"]]",
   "v1": [
    27286716202489,
    943358511186
   ],
   "v2": [
    760851170768821,
    29244113846766
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_exceptions.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_status_codes.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_status_codes.py\", \"AsyncByteStream\"]]",
   "v1": [
    27286716202489,
    943358511186
   ],
   "v2": [
    760851170768821,
    29244113846766
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_status_codes.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_urls.py', 'AsyncByteStre
```
</details>

## Step 13

`httpx/_transports` lists 6 entries (complete): `__init__.py`, `asgi.py`, `base.py`, `default.py`, `mock.py`, `wsgi.py`.

Candidate modules so far: 6; statements confirmed: 4, ruled out: 0, modules with no such import: 0, pending: 16. import coverage open at `.`; star coverage open at `.`.

Outstanding: list `.` to split a capped grep; know what `httpx/_api.py` exports; know what `httpx/_auth.py` exports; know what `httpx/_client.py` exports; and 13 more.

Next: outline `httpx/_api.py` filtered to `AsyncByteStream`, because module `httpx/_api.py` (step 9). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `httpx/_auth.py` filtered to `AsyncByteStream`, scores the same; the seed broke the tie. Plan by outcome: def: outline `httpx/_auth.py` filtered to `AsyncByteStream`; reexport: outline `httpx/_auth.py` filtered to `AsyncByteStream`; star: outline `httpx/_auth.py` filtered to `AsyncByteStream`; none: outline `httpx/_auth.py` filtered to `AsyncByteStream`.

**Call:** `symbols('httpx/_api.py', 'AsyncByteStream')`

**Response**: outcome `none`

```
module httpx/_api.py lines=439 dynamic=no all=static@26
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_api.py"
   ],
   "desc": "know what `httpx/_api.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_auth.py"
   ],
   "desc": "know what `httpx/_auth.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_client.py"
   ],
   "desc": "know what `httpx/_client.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_config.py"
   ],
   "desc": "know what `httpx/_config.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_content.py"
   ],
   "desc": "know what `httpx/_content.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_exceptions.py"
   ],
   "desc": "know what `httpx/_exceptions.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_models.py"
   ],
   "desc": "know what `httpx/_models.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_status_codes.py"
   ],
   "desc": "know what `httpx/_status_codes.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/__init__.py"
   ],
   "desc": "know what `httpx/_transports/__init__.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_urls.py"
   ],
   "desc": "know what `httpx/_urls.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/asgi.py"
   ],
   "desc": "know what `httpx/_transports/asgi.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/base.py"
   ],
   "desc": "know what `httpx/_transports/base.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/default.py"
   ],
   "desc": "know what `httpx/_transports/default.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/mock.py"
   ],
   "desc": "know what `httpx/_transports/mock.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/wsgi.py"
   ],
   "desc": "know what `httpx/_transports/wsgi.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/_api.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_api.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_api.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_auth.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_auth.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_auth.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_config.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_config.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_config.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_exceptions.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_exceptions.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_exceptions.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_status_codes.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_status_codes.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_status_codes.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/base.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/base.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/base.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/default.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/default.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
  
```
</details>

## Step 14

`httpx/_api.py` binds no `AsyncByteStream` at module level; no star imports; a literal `__all__` at line 26; no dynamic namespace tricks.

Candidate modules so far: 6; statements confirmed: 4, ruled out: 0, modules with no such import: 0, pending: 16. import coverage open at `.`; star coverage open at `.`.

Open: list `.` to split a capped grep; know what `httpx/_api.py` exports; know what `httpx/_auth.py` exports; know what `httpx/_client.py` exports; and 13 more.

Next: outline `httpx/_auth.py` filtered to `AsyncByteStream`, because module `httpx/_auth.py` (step 9). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `httpx/_config.py` filtered to `AsyncByteStream`, scores the same; the seed broke the tie. Plan by outcome: def: outline `httpx/_config.py` filtered to `AsyncByteStream`; reexport: outline `httpx/_config.py` filtered to `AsyncByteStream`; star: outline `httpx/_config.py` filtered to `AsyncByteStream`; none: outline `httpx/_config.py` filtered to `AsyncByteStream`.

**Call:** `symbols('httpx/_auth.py', 'AsyncByteStream')`

**Response**: outcome `none`

```
module httpx/_auth.py lines=349 dynamic=no all=static@19
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_api.py"
   ],
   "desc": "know what `httpx/_api.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_auth.py"
   ],
   "desc": "know what `httpx/_auth.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_client.py"
   ],
   "desc": "know what `httpx/_client.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_config.py"
   ],
   "desc": "know what `httpx/_config.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_content.py"
   ],
   "desc": "know what `httpx/_content.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_exceptions.py"
   ],
   "desc": "know what `httpx/_exceptions.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_models.py"
   ],
   "desc": "know what `httpx/_models.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_status_codes.py"
   ],
   "desc": "know what `httpx/_status_codes.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/__init__.py"
   ],
   "desc": "know what `httpx/_transports/__init__.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_urls.py"
   ],
   "desc": "know what `httpx/_urls.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/asgi.py"
   ],
   "desc": "know what `httpx/_transports/asgi.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/base.py"
   ],
   "desc": "know what `httpx/_transports/base.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/default.py"
   ],
   "desc": "know what `httpx/_transports/default.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/mock.py"
   ],
   "desc": "know what `httpx/_transports/mock.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/wsgi.py"
   ],
   "desc": "know what `httpx/_transports/wsgi.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/_auth.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_auth.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_auth.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_config.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_config.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_config.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_exceptions.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_exceptions.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_exceptions.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_status_codes.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_status_codes.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_status_codes.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/base.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/base.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/base.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/default.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/default.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/default.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/mock.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/mock.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
 
```
</details>

## Step 15

`httpx/_auth.py` binds no `AsyncByteStream` at module level; no star imports; a literal `__all__` at line 19; no dynamic namespace tricks.

Candidate modules so far: 6; statements confirmed: 4, ruled out: 0, modules with no such import: 0, pending: 16. import coverage open at `.`; star coverage open at `.`.

Still to settle: list `.` to split a capped grep; know what `httpx/_api.py` exports; know what `httpx/_auth.py` exports; know what `httpx/_client.py` exports; and 13 more.

Next: outline `httpx/_config.py` filtered to `AsyncByteStream`, because module `httpx/_config.py` (step 9). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `httpx/_exceptions.py` filtered to `AsyncByteStream`, scores the same; the seed broke the tie. Plan by outcome: def: outline `httpx/_exceptions.py` filtered to `AsyncByteStream`; reexport: outline `httpx/_exceptions.py` filtered to `AsyncByteStream`; star: outline `httpx/_exceptions.py` filtered to `AsyncByteStream`; none: outline `httpx/_exceptions.py` filtered to `AsyncByteStream`.

**Call:** `symbols('httpx/_config.py', 'AsyncByteStream')`

**Response**: outcome `none`

```
module httpx/_config.py lines=249 dynamic=no all=static@13
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_api.py"
   ],
   "desc": "know what `httpx/_api.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_auth.py"
   ],
   "desc": "know what `httpx/_auth.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_client.py"
   ],
   "desc": "know what `httpx/_client.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_config.py"
   ],
   "desc": "know what `httpx/_config.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_content.py"
   ],
   "desc": "know what `httpx/_content.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_exceptions.py"
   ],
   "desc": "know what `httpx/_exceptions.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_models.py"
   ],
   "desc": "know what `httpx/_models.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_status_codes.py"
   ],
   "desc": "know what `httpx/_status_codes.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/__init__.py"
   ],
   "desc": "know what `httpx/_transports/__init__.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_urls.py"
   ],
   "desc": "know what `httpx/_urls.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/asgi.py"
   ],
   "desc": "know what `httpx/_transports/asgi.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/base.py"
   ],
   "desc": "know what `httpx/_transports/base.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/default.py"
   ],
   "desc": "know what `httpx/_transports/default.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/mock.py"
   ],
   "desc": "know what `httpx/_transports/mock.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/wsgi.py"
   ],
   "desc": "know what `httpx/_transports/wsgi.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/_config.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_config.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_config.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_exceptions.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_exceptions.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_exceptions.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_status_codes.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_status_codes.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_status_codes.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/base.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/base.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/base.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/default.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/default.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/default.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/mock.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/mock.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/mock.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/wsgi.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/wsgi.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reex
```
</details>

## Step 16

`httpx/_config.py` binds no `AsyncByteStream` at module level; no star imports; a literal `__all__` at line 13; no dynamic namespace tricks.

Candidate modules so far: 6; statements confirmed: 4, ruled out: 0, modules with no such import: 0, pending: 16. import coverage open at `.`; star coverage open at `.`.

Outstanding: list `.` to split a capped grep; know what `httpx/_api.py` exports; know what `httpx/_auth.py` exports; know what `httpx/_client.py` exports; and 13 more.

Next: outline `httpx/_exceptions.py` filtered to `AsyncByteStream`, because module `httpx/_exceptions.py` (step 9). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `httpx/_status_codes.py` filtered to `AsyncByteStream`, scores the same; the seed broke the tie. Plan by outcome: def: outline `httpx/_status_codes.py` filtered to `AsyncByteStream`; reexport: outline `httpx/_status_codes.py` filtered to `AsyncByteStream`; star: outline `httpx/_status_codes.py` filtered to `AsyncByteStream`; none: outline `httpx/_status_codes.py` filtered to `AsyncByteStream`.

**Call:** `symbols('httpx/_exceptions.py', 'AsyncByteStream')`

**Response**: outcome `none`

```
module httpx/_exceptions.py lines=378 dynamic=no all=static@42
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_api.py"
   ],
   "desc": "know what `httpx/_api.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_auth.py"
   ],
   "desc": "know what `httpx/_auth.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_client.py"
   ],
   "desc": "know what `httpx/_client.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_config.py"
   ],
   "desc": "know what `httpx/_config.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_content.py"
   ],
   "desc": "know what `httpx/_content.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_exceptions.py"
   ],
   "desc": "know what `httpx/_exceptions.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_models.py"
   ],
   "desc": "know what `httpx/_models.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_status_codes.py"
   ],
   "desc": "know what `httpx/_status_codes.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/__init__.py"
   ],
   "desc": "know what `httpx/_transports/__init__.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_urls.py"
   ],
   "desc": "know what `httpx/_urls.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/asgi.py"
   ],
   "desc": "know what `httpx/_transports/asgi.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/base.py"
   ],
   "desc": "know what `httpx/_transports/base.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/default.py"
   ],
   "desc": "know what `httpx/_transports/default.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/mock.py"
   ],
   "desc": "know what `httpx/_transports/mock.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/wsgi.py"
   ],
   "desc": "know what `httpx/_transports/wsgi.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/_exceptions.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_exceptions.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_exceptions.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_status_codes.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_status_codes.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_status_codes.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/base.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/base.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/base.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/default.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/default.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/default.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/mock.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/mock.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/mock.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/wsgi.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/wsgi.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/wsgi.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_urls.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_urls.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    
```
</details>

## Step 17

`httpx/_exceptions.py` binds no `AsyncByteStream` at module level; no star imports; a literal `__all__` at line 42; no dynamic namespace tricks.

Candidate modules so far: 6; statements confirmed: 4, ruled out: 0, modules with no such import: 0, pending: 16. import coverage open at `.`; star coverage open at `.`.

Still to settle: list `.` to split a capped grep; know what `httpx/_api.py` exports; know what `httpx/_auth.py` exports; know what `httpx/_client.py` exports; and 13 more.

Next: outline `httpx/_status_codes.py` filtered to `AsyncByteStream`, because module `httpx/_status_codes.py` (step 9). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `httpx/_transports/base.py` filtered to `AsyncByteStream`, scores the same; the seed broke the tie. Plan by outcome: def: outline `httpx/_transports/base.py` filtered to `AsyncByteStream`; reexport: outline `httpx/_transports/base.py` filtered to `AsyncByteStream`; star: outline `httpx/_transports/base.py` filtered to `AsyncByteStream`; none: outline `httpx/_transports/base.py` filtered to `AsyncByteStream`.

**Call:** `symbols('httpx/_status_codes.py', 'AsyncByteStream')`

**Response**: outcome `none`

```
module httpx/_status_codes.py lines=163 dynamic=no all=static@5
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_api.py"
   ],
   "desc": "know what `httpx/_api.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_auth.py"
   ],
   "desc": "know what `httpx/_auth.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_client.py"
   ],
   "desc": "know what `httpx/_client.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_config.py"
   ],
   "desc": "know what `httpx/_config.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_content.py"
   ],
   "desc": "know what `httpx/_content.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_exceptions.py"
   ],
   "desc": "know what `httpx/_exceptions.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_models.py"
   ],
   "desc": "know what `httpx/_models.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_status_codes.py"
   ],
   "desc": "know what `httpx/_status_codes.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/__init__.py"
   ],
   "desc": "know what `httpx/_transports/__init__.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_urls.py"
   ],
   "desc": "know what `httpx/_urls.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/asgi.py"
   ],
   "desc": "know what `httpx/_transports/asgi.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/base.py"
   ],
   "desc": "know what `httpx/_transports/base.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/default.py"
   ],
   "desc": "know what `httpx/_transports/default.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/mock.py"
   ],
   "desc": "know what `httpx/_transports/mock.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/wsgi.py"
   ],
   "desc": "know what `httpx/_transports/wsgi.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/_status_codes.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_status_codes.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_status_codes.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/base.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/base.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/base.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/default.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/default.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/default.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/mock.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/mock.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/mock.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/wsgi.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/wsgi.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/wsgi.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_urls.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_urls.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_urls.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_api.py', 26, 30)",
   "key": "[\"read\", [\"httpx/_api.py\", 26, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    117789304565831,
    4716792555930
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [

```
</details>

## Step 18

`httpx/_status_codes.py` binds no `AsyncByteStream` at module level; no star imports; a literal `__all__` at line 5; no dynamic namespace tricks.

Candidate modules so far: 6; statements confirmed: 4, ruled out: 0, modules with no such import: 0, pending: 16. import coverage open at `.`; star coverage open at `.`.

Open: list `.` to split a capped grep; know what `httpx/_api.py` exports; know what `httpx/_auth.py` exports; know what `httpx/_client.py` exports; and 13 more.

Next: outline `httpx/_transports/base.py` filtered to `AsyncByteStream`, because module `httpx/_transports/base.py` (step 12). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `httpx/_transports/default.py` filtered to `AsyncByteStream`, scores the same; the seed broke the tie. Plan by outcome: def: outline `httpx/_transports/default.py` filtered to `AsyncByteStream`; reexport: outline `httpx/_transports/default.py` filtered to `AsyncByteStream`; star: outline `httpx/_transports/default.py` filtered to `AsyncByteStream`; none: outline `httpx/_transports/default.py` filtered to `AsyncByteStream`.

**Call:** `symbols('httpx/_transports/base.py', 'AsyncByteStream')`

**Response**: outcome `none`

```
module httpx/_transports/base.py lines=87 dynamic=no all=static@11
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_api.py"
   ],
   "desc": "know what `httpx/_api.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_auth.py"
   ],
   "desc": "know what `httpx/_auth.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_client.py"
   ],
   "desc": "know what `httpx/_client.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_config.py"
   ],
   "desc": "know what `httpx/_config.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_content.py"
   ],
   "desc": "know what `httpx/_content.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_exceptions.py"
   ],
   "desc": "know what `httpx/_exceptions.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_models.py"
   ],
   "desc": "know what `httpx/_models.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_status_codes.py"
   ],
   "desc": "know what `httpx/_status_codes.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/__init__.py"
   ],
   "desc": "know what `httpx/_transports/__init__.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_urls.py"
   ],
   "desc": "know what `httpx/_urls.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/asgi.py"
   ],
   "desc": "know what `httpx/_transports/asgi.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/base.py"
   ],
   "desc": "know what `httpx/_transports/base.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/default.py"
   ],
   "desc": "know what `httpx/_transports/default.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/mock.py"
   ],
   "desc": "know what `httpx/_transports/mock.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/wsgi.py"
   ],
   "desc": "know what `httpx/_transports/wsgi.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/_transports/base.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/base.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/base.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/default.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/default.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/default.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/mock.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/mock.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/mock.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/wsgi.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/wsgi.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/wsgi.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_urls.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_urls.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_urls.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_api.py', 26, 30)",
   "key": "[\"read\", [\"httpx/_api.py\", 26, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    117789304565831,
    4716792555930
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_api.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_auth.py', 19, 30)",
   "key": "[\"read\", [\"httpx/_auth.py\", 19, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    117789304565831,
    4716792555930
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_auth.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_client.py', 54, 30)",
   "key": "[\"read\", [\"httpx/_client.py\",
```
</details>

## Step 19

`httpx/_transports/base.py` binds no `AsyncByteStream` at module level; no star imports; a literal `__all__` at line 11; no dynamic namespace tricks.

Candidate modules so far: 6; statements confirmed: 4, ruled out: 0, modules with no such import: 0, pending: 16. import coverage open at `.`; star coverage open at `.`.

Outstanding: list `.` to split a capped grep; know what `httpx/_api.py` exports; know what `httpx/_auth.py` exports; know what `httpx/_client.py` exports; and 13 more.

Next: outline `httpx/_transports/default.py` filtered to `AsyncByteStream`, because module `httpx/_transports/default.py` (step 12). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `httpx/_transports/mock.py` filtered to `AsyncByteStream`, scores the same; the seed broke the tie. Plan by outcome: def: outline `httpx/_transports/mock.py` filtered to `AsyncByteStream`; reexport: outline `httpx/_transports/mock.py` filtered to `AsyncByteStream`; star: outline `httpx/_transports/mock.py` filtered to `AsyncByteStream`; none: outline `httpx/_transports/mock.py` filtered to `AsyncByteStream`.

**Call:** `symbols('httpx/_transports/default.py', 'AsyncByteStream')`

**Response**: outcome `reexport`

```
module httpx/_transports/default.py lines=407 dynamic=no all=static@69
56 from AsyncByteStream <- .._types AsyncByteStream
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_api.py"
   ],
   "desc": "know what `httpx/_api.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_auth.py"
   ],
   "desc": "know what `httpx/_auth.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_client.py"
   ],
   "desc": "know what `httpx/_client.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_config.py"
   ],
   "desc": "know what `httpx/_config.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_content.py"
   ],
   "desc": "know what `httpx/_content.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_exceptions.py"
   ],
   "desc": "know what `httpx/_exceptions.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_models.py"
   ],
   "desc": "know what `httpx/_models.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_status_codes.py"
   ],
   "desc": "know what `httpx/_status_codes.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/__init__.py"
   ],
   "desc": "know what `httpx/_transports/__init__.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_urls.py"
   ],
   "desc": "know what `httpx/_urls.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/asgi.py"
   ],
   "desc": "know what `httpx/_transports/asgi.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/base.py"
   ],
   "desc": "know what `httpx/_transports/base.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/default.py"
   ],
   "desc": "know what `httpx/_transports/default.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/mock.py"
   ],
   "desc": "know what `httpx/_transports/mock.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/wsgi.py"
   ],
   "desc": "know what `httpx/_transports/wsgi.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/_transports/default.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/default.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/default.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/mock.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/mock.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/mock.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/wsgi.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/wsgi.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/wsgi.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_urls.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_urls.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_urls.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_api.py', 26, 30)",
   "key": "[\"read\", [\"httpx/_api.py\", 26, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    117789304565831,
    4716792555930
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_api.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_auth.py', 19, 30)",
   "key": "[\"read\", [\"httpx/_auth.py\", 19, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    117789304565831,
    4716792555930
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_auth.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_client.py', 54, 30)",
   "key": "[\"read\", [\"httpx/_client.py\", 54, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    117789304565831,
    4716792555930
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_client.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_config.py', 13, 30)",
   "key": "[\"read\", [\"httpx/_config.py\", 13, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    117789304565831,
    4716792555930
   ],
   "p_cap": [
    0,
    1
   ],
```
</details>

## Step 20

In `httpx/_transports/default.py`, `AsyncByteStream` has exactly one binding: line 56 imports it as `AsyncByteStream` from `.._types`. No dynamic namespace tricks, a literal `__all__` at line 69.

Candidate modules so far: 6; statements confirmed: 4, ruled out: 0, modules with no such import: 0, pending: 16. import coverage open at `.`; star coverage open at `.`.

Open: list `.` to split a capped grep; know what `httpx/_api.py` exports; know what `httpx/_auth.py` exports; know what `httpx/_client.py` exports; and 13 more.

Next: outline `httpx/_transports/mock.py` filtered to `AsyncByteStream`, because module `httpx/_transports/mock.py` (step 12). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `httpx/_transports/wsgi.py` filtered to `AsyncByteStream`, scores the same; the seed broke the tie. Plan by outcome: def: outline `httpx/_transports/wsgi.py` filtered to `AsyncByteStream`; reexport: outline `httpx/_transports/wsgi.py` filtered to `AsyncByteStream`; star: outline `httpx/_transports/wsgi.py` filtered to `AsyncByteStream`; none: outline `httpx/_transports/wsgi.py` filtered to `AsyncByteStream`.

**Call:** `symbols('httpx/_transports/mock.py', 'AsyncByteStream')`

**Response**: outcome `none`

```
module httpx/_transports/mock.py lines=44 dynamic=no all=static@12
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_api.py"
   ],
   "desc": "know what `httpx/_api.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_auth.py"
   ],
   "desc": "know what `httpx/_auth.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_client.py"
   ],
   "desc": "know what `httpx/_client.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_config.py"
   ],
   "desc": "know what `httpx/_config.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_content.py"
   ],
   "desc": "know what `httpx/_content.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_exceptions.py"
   ],
   "desc": "know what `httpx/_exceptions.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_models.py"
   ],
   "desc": "know what `httpx/_models.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_status_codes.py"
   ],
   "desc": "know what `httpx/_status_codes.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/__init__.py"
   ],
   "desc": "know what `httpx/_transports/__init__.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_urls.py"
   ],
   "desc": "know what `httpx/_urls.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/asgi.py"
   ],
   "desc": "know what `httpx/_transports/asgi.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/base.py"
   ],
   "desc": "know what `httpx/_transports/base.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/default.py"
   ],
   "desc": "know what `httpx/_transports/default.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/mock.py"
   ],
   "desc": "know what `httpx/_transports/mock.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/wsgi.py"
   ],
   "desc": "know what `httpx/_transports/wsgi.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/_transports/mock.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/mock.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/mock.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/wsgi.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/wsgi.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/wsgi.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_urls.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_urls.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_urls.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_api.py', 26, 30)",
   "key": "[\"read\", [\"httpx/_api.py\", 26, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    117789304565831,
    4716792555930
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_api.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_auth.py', 19, 30)",
   "key": "[\"read\", [\"httpx/_auth.py\", 19, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    117789304565831,
    4716792555930
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_auth.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_client.py', 54, 30)",
   "key": "[\"read\", [\"httpx/_client.py\", 54, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    117789304565831,
    4716792555930
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_client.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_config.py', 13, 30)",
   "key": "[\"read\", [\"httpx/_config.py\", 13, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    117789304565831,
    4716792555930
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_config.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_content.py', 28, 30)",
   "key": "[\"read\", [\"httpx/_content.py\", 28, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    117789304565831,
    4716792555930
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_content.py"
 
```
</details>

## Step 21

`httpx/_transports/mock.py` binds no `AsyncByteStream` at module level; no star imports; a literal `__all__` at line 12; no dynamic namespace tricks.

Candidate modules so far: 6; statements confirmed: 4, ruled out: 0, modules with no such import: 0, pending: 16. import coverage open at `.`; star coverage open at `.`.

Still to settle: list `.` to split a capped grep; know what `httpx/_api.py` exports; know what `httpx/_auth.py` exports; know what `httpx/_client.py` exports; and 13 more.

Next: outline `httpx/_transports/wsgi.py` filtered to `AsyncByteStream`, because module `httpx/_transports/wsgi.py` (step 12). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `httpx/_urls.py` filtered to `AsyncByteStream`, scores the same; the seed broke the tie. Plan by outcome: def: outline `httpx/_urls.py` filtered to `AsyncByteStream`; reexport: outline `httpx/_urls.py` filtered to `AsyncByteStream`; star: outline `httpx/_urls.py` filtered to `AsyncByteStream`; none: outline `httpx/_urls.py` filtered to `AsyncByteStream`.

**Call:** `symbols('httpx/_transports/wsgi.py', 'AsyncByteStream')`

**Response**: outcome `none`

```
module httpx/_transports/wsgi.py lines=150 dynamic=no all=static@19
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_api.py"
   ],
   "desc": "know what `httpx/_api.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_auth.py"
   ],
   "desc": "know what `httpx/_auth.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_client.py"
   ],
   "desc": "know what `httpx/_client.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_config.py"
   ],
   "desc": "know what `httpx/_config.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_content.py"
   ],
   "desc": "know what `httpx/_content.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_exceptions.py"
   ],
   "desc": "know what `httpx/_exceptions.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_models.py"
   ],
   "desc": "know what `httpx/_models.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_status_codes.py"
   ],
   "desc": "know what `httpx/_status_codes.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/__init__.py"
   ],
   "desc": "know what `httpx/_transports/__init__.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_urls.py"
   ],
   "desc": "know what `httpx/_urls.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/asgi.py"
   ],
   "desc": "know what `httpx/_transports/asgi.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/base.py"
   ],
   "desc": "know what `httpx/_transports/base.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/default.py"
   ],
   "desc": "know what `httpx/_transports/default.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/mock.py"
   ],
   "desc": "know what `httpx/_transports/mock.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/wsgi.py"
   ],
   "desc": "know what `httpx/_transports/wsgi.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/_transports/wsgi.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_transports/wsgi.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/wsgi.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_urls.py', 'AsyncByteStream')",
   "key": "[\"symbols\", [\"httpx/_urls.py\", \"AsyncByteStream\"]]",
   "v1": [
    23369189210929,
    943358511186
   ],
   "v2": [
    11702616886319,
    471679255593
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     403,
     427
    ],
    "reexport": [
     1,
     61
    ],
    "star": [
     1,
     427
    ],
    "none": [
     16,
     427
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_urls.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_api.py', 26, 30)",
   "key": "[\"read\", [\"httpx/_api.py\", 26, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    117789304565831,
    4716792555930
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_api.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_auth.py', 19, 30)",
   "key": "[\"read\", [\"httpx/_auth.py\", 19, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    117789304565831,
    4716792555930
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_auth.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_client.py', 54, 30)",
   "key": "[\"read\", [\"httpx/_client.py\", 54, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    117789304565831,
    4716792555930
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_client.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_config.py', 13, 30)",
   "key": "[\"read\", [\"httpx/_config.py\", 13, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    117789304565831,
    4716792555930
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_config.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_content.py', 28, 30)",
   "key": "[\"read\", [\"httpx/_content.py\", 28, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    117789304565831,
    4716792555930
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_content.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_exceptions.py', 42, 30)",
   "key": "[\"read\", [\"httpx/_exceptions.py\", 42, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    117789304565831,
    4716792555930
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_exceptions.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_models.py', 51, 30)",
   "key": "[\"read\", [\"httpx/_models.py\", 51, 30]]",
   "v1": [
  
```
</details>

## Step 22

`httpx/_transports/wsgi.py` binds no `AsyncByteStream` at module level; no star imports; a literal `__all__` at line 19; no dynamic namespace tricks.

Candidate modules so far: 6; statements confirmed: 4, ruled out: 0, modules with no such import: 0, pending: 16. import coverage open at `.`; star coverage open at `.`.

Open: list `.` to split a capped grep; know what `httpx/_api.py` exports; know what `httpx/_auth.py` exports; know what `httpx/_client.py` exports; and 13 more.

Next: outline `httpx/_urls.py` filtered to `AsyncByteStream`, because module `httpx/_urls.py` (step 9). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, read `httpx/_api.py` from line 26, scores the same; the seed broke the tie. Plan by outcome: def: read `httpx/_api.py` from line 26; reexport: read `httpx/_api.py` from line 26; star: read `httpx/_api.py` from line 26; none: read `httpx/_api.py` from line 26.

**Call:** `symbols('httpx/_urls.py', 'AsyncByteStream')`

**Response**: outcome `none`

```
module httpx/_urls.py lines=642 dynamic=no all=static@12
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_api.py"
   ],
   "desc": "know what `httpx/_api.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_auth.py"
   ],
   "desc": "know what `httpx/_auth.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_client.py"
   ],
   "desc": "know what `httpx/_client.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_config.py"
   ],
   "desc": "know what `httpx/_config.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_content.py"
   ],
   "desc": "know what `httpx/_content.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_exceptions.py"
   ],
   "desc": "know what `httpx/_exceptions.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_models.py"
   ],
   "desc": "know what `httpx/_models.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_status_codes.py"
   ],
   "desc": "know what `httpx/_status_codes.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/__init__.py"
   ],
   "desc": "know what `httpx/_transports/__init__.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_urls.py"
   ],
   "desc": "know what `httpx/_urls.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/asgi.py"
   ],
   "desc": "know what `httpx/_transports/asgi.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/base.py"
   ],
   "desc": "know what `httpx/_transports/base.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/default.py"
   ],
   "desc": "know what `httpx/_transports/default.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/mock.py"
   ],
   "desc": "know what `httpx/_transports/mock.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/wsgi.py"
   ],
   "desc": "know what `httpx/_transports/wsgi.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "read('httpx/_api.py', 26, 30)",
   "key": "[\"read\", [\"httpx/_api.py\", 26, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    117789304565831,
    4716792555930
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_api.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_auth.py', 19, 30)",
   "key": "[\"read\", [\"httpx/_auth.py\", 19, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    117789304565831,
    4716792555930
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_auth.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_client.py', 54, 30)",
   "key": "[\"read\", [\"httpx/_client.py\", 54, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    117789304565831,
    4716792555930
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_client.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_config.py', 13, 30)",
   "key": "[\"read\", [\"httpx/_config.py\", 13, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    117789304565831,
    4716792555930
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_config.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_content.py', 28, 30)",
   "key": "[\"read\", [\"httpx/_content.py\", 28, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    117789304565831,
    4716792555930
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_content.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_exceptions.py', 42, 30)",
   "key": "[\"read\", [\"httpx/_exceptions.py\", 42, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    117789304565831,
    4716792555930
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_exceptions.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_models.py', 51, 30)",
   "key": "[\"read\", [\"httpx/_models.py\", 51, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    117789304565831,
    4716792555930
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_models.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_status_codes.py', 5, 30)",
   "key": "[\"read\", [\"httpx/_status_codes.py\", 5, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    117789304565831,
    4716792555930
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_status_codes.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/__init__.py', 7, 30)",
   "key": "[\"read\", [\"httpx/_transports/__init__.py\", 7, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    117789304565831,
    4716792555930
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "
```
</details>

## Step 23

`httpx/_urls.py` binds no `AsyncByteStream` at module level; no star imports; a literal `__all__` at line 12; no dynamic namespace tricks.

Candidate modules so far: 6; statements confirmed: 4, ruled out: 0, modules with no such import: 0, pending: 16. import coverage open at `.`; star coverage open at `.`.

Outstanding: list `.` to split a capped grep; know what `httpx/_api.py` exports; know what `httpx/_auth.py` exports; know what `httpx/_client.py` exports; and 13 more.

Next: read `httpx/_api.py` from line 26, because `__all__` of `httpx/_api.py` starts at line 26 (outline header). I expect: the whole list fits the window (about 80%); the list runs past the window (about 20%). The alternative, read `httpx/_auth.py` from line 19, scores the same; the seed broke the tie. Plan by outcome: fits: read `httpx/_auth.py` from line 19; long: read `httpx/_auth.py` from line 19.

**Call:** `read('httpx/_api.py', 26, 30)`

**Response**: outcome `fits`

```
26:__all__ = [
27:    "delete",
28:    "get",
29:    "head",
30:    "options",
31:    "patch",
32:    "post",
33:    "put",
34:    "request",
35:    "stream",
36:]
37:
38:
39:def request(
40:    method: str,
41:    url: URL | str,
42:    *,
43:    params: QueryParamTypes | None = None,
44:    content: RequestContent | None = None,
45:    data: RequestData | None = None,
46:    files: RequestFiles | None = None,
47:    json: typing.Any | None = None,
48:    headers: HeaderTypes | None = None,
49:    cookies: CookieTypes | None = None,
50:    auth: AuthTypes | None = None,
... (5 more lines)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_api.py"
   ],
   "desc": "know what `httpx/_api.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_auth.py"
   ],
   "desc": "know what `httpx/_auth.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_client.py"
   ],
   "desc": "know what `httpx/_client.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_config.py"
   ],
   "desc": "know what `httpx/_config.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_content.py"
   ],
   "desc": "know what `httpx/_content.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_exceptions.py"
   ],
   "desc": "know what `httpx/_exceptions.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_models.py"
   ],
   "desc": "know what `httpx/_models.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_status_codes.py"
   ],
   "desc": "know what `httpx/_status_codes.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/__init__.py"
   ],
   "desc": "know what `httpx/_transports/__init__.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_urls.py"
   ],
   "desc": "know what `httpx/_urls.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/asgi.py"
   ],
   "desc": "know what `httpx/_transports/asgi.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/base.py"
   ],
   "desc": "know what `httpx/_transports/base.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/default.py"
   ],
   "desc": "know what `httpx/_transports/default.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/mock.py"
   ],
   "desc": "know what `httpx/_transports/mock.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/wsgi.py"
   ],
   "desc": "know what `httpx/_transports/wsgi.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "read('httpx/_api.py', 26, 30)",
   "key": "[\"read\", [\"httpx/_api.py\", 26, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    3751896964,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_api.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_auth.py', 19, 30)",
   "key": "[\"read\", [\"httpx/_auth.py\", 19, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    3751896964,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_auth.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_client.py', 54, 30)",
   "key": "[\"read\", [\"httpx/_client.py\", 54, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    3751896964,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_client.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_config.py', 13, 30)",
   "key": "[\"read\", [\"httpx/_config.py\", 13, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    3751896964,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_config.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_content.py', 28, 30)",
   "key": "[\"read\", [\"httpx/_content.py\", 28, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    3751896964,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_content.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_exceptions.py', 42, 30)",
   "key": "[\"read\", [\"httpx/_exceptions.py\", 42, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    3751896964,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_exceptions.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_models.py', 51, 30)",
   "key": "[\"read\", [\"httpx/_models.py\", 51, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    3751896964,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_models.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_status_codes.py', 5, 30)",
   "key": "[\"read\", [\"httpx/_status_codes.py\", 5, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    3751896964,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_status_codes.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/__init__.py', 7, 30)",
   "key": "[\"read\", [\"httpx/_transports/__init__.py\", 7, 30]]",
   "v1": [
    3722041957,
    149275035
   ],
   "v2": [
    3751896964,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/__init__.py"
    ]
   ]
  },
```
</details>

## Step 24

The statement at `httpx/_api.py`:26 binds `__all__`. `__all__` in `httpx/_api.py` lists 9 names, and `AsyncByteStream` is not among them.

Candidate modules so far: 6; statements confirmed: 4, ruled out: 1, modules with no such import: 0, pending: 15. import coverage open at `.`; star coverage open at `.`. Latest ruled out: `httpx/__init__.py`:2, star import of `._api`, which does not export `AsyncByteStream`.

Still to settle: list `.` to split a capped grep; know what `httpx/_auth.py` exports; know what `httpx/_client.py` exports; know what `httpx/_config.py` exports; and 12 more.

Next: read `httpx/_auth.py` from line 19, because `__all__` of `httpx/_auth.py` starts at line 19 (outline header). I expect: the whole list fits the window (about 80%); the list runs past the window (about 20%). The alternative, read `httpx/_client.py` from line 54, scores the same; the seed broke the tie. Plan by outcome: fits: read `httpx/_client.py` from line 54; long: read `httpx/_client.py` from line 54.

**Call:** `read('httpx/_auth.py', 19, 30)`

**Response**: outcome `fits`

```
19:__all__ = ["Auth", "BasicAuth", "DigestAuth", "FunctionAuth", "NetRCAuth"]
20:
21:
22:class Auth:
23:    """
24:    Base class for all authentication schemes.
25:
26:    To implement a custom authentication scheme, subclass `Auth` and override
27:    the `.auth_flow()` method.
28:
29:    If the authentication scheme does I/O such as disk access or network calls, or uses
30:    synchronization primitives such as locks, you should override `.sync_auth_flow()`
31:    and/or `.async_auth_flow()` instead of `.auth_flow()` to provide specialized
32:    implementations that will be used by `Client` and `AsyncClient` respectively.
33:    """
34:
35:    requires_request_body = False
36:    requires_response_body = False
37:
38:    def auth_flow(self, request: Request) -> typing.Generator[Request, Response, None]:
39:        """
40:        Execute the authentication flow.
41:
42:        To dispatch a request, `yield` it:
43:
... (5 more lines)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_auth.py"
   ],
   "desc": "know what `httpx/_auth.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_client.py"
   ],
   "desc": "know what `httpx/_client.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_config.py"
   ],
   "desc": "know what `httpx/_config.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_content.py"
   ],
   "desc": "know what `httpx/_content.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_exceptions.py"
   ],
   "desc": "know what `httpx/_exceptions.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_models.py"
   ],
   "desc": "know what `httpx/_models.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_status_codes.py"
   ],
   "desc": "know what `httpx/_status_codes.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/__init__.py"
   ],
   "desc": "know what `httpx/_transports/__init__.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_urls.py"
   ],
   "desc": "know what `httpx/_urls.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/asgi.py"
   ],
   "desc": "know what `httpx/_transports/asgi.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/base.py"
   ],
   "desc": "know what `httpx/_transports/base.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/default.py"
   ],
   "desc": "know what `httpx/_transports/default.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/mock.py"
   ],
   "desc": "know what `httpx/_transports/mock.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/wsgi.py"
   ],
   "desc": "know what `httpx/_transports/wsgi.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "read('httpx/_auth.py', 19, 30)",
   "key": "[\"read\", [\"httpx/_auth.py\", 19, 30]]",
   "v1": [
    3572766922,
    149275035
   ],
   "v2": [
    3602621929,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_auth.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_client.py', 54, 30)",
   "key": "[\"read\", [\"httpx/_client.py\", 54, 30]]",
   "v1": [
    3572766922,
    149275035
   ],
   "v2": [
    3602621929,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_client.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_config.py', 13, 30)",
   "key": "[\"read\", [\"httpx/_config.py\", 13, 30]]",
   "v1": [
    3572766922,
    149275035
   ],
   "v2": [
    3602621929,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_config.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_content.py', 28, 30)",
   "key": "[\"read\", [\"httpx/_content.py\", 28, 30]]",
   "v1": [
    3572766922,
    149275035
   ],
   "v2": [
    3602621929,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_content.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_exceptions.py', 42, 30)",
   "key": "[\"read\", [\"httpx/_exceptions.py\", 42, 30]]",
   "v1": [
    3572766922,
    149275035
   ],
   "v2": [
    3602621929,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_exceptions.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_models.py', 51, 30)",
   "key": "[\"read\", [\"httpx/_models.py\", 51, 30]]",
   "v1": [
    3572766922,
    149275035
   ],
   "v2": [
    3602621929,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_models.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_status_codes.py', 5, 30)",
   "key": "[\"read\", [\"httpx/_status_codes.py\", 5, 30]]",
   "v1": [
    3572766922,
    149275035
   ],
   "v2": [
    3602621929,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_status_codes.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/__init__.py', 7, 30)",
   "key": "[\"read\", [\"httpx/_transports/__init__.py\", 7, 30]]",
   "v1": [
    3572766922,
    149275035
   ],
   "v2": [
    3602621929,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/__init__.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/asgi.py', 26, 30)",
   "key": "[\"read\", [\"httpx/_transports/asgi.py\", 26, 30]]",
   "v1": [
    3572766922,
    149275035
   ],
   "v2": [
    3602621929,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/asgi.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/base.py', 11, 30)",
   "key": "[\"read\", [\"h
```
</details>

## Step 25

The statement at `httpx/_auth.py`:19 binds `__all__`. `__all__` in `httpx/_auth.py` lists 5 names, and `AsyncByteStream` is not among them.

Candidate modules so far: 6; statements confirmed: 4, ruled out: 2, modules with no such import: 0, pending: 14. import coverage open at `.`; star coverage open at `.`. Latest ruled out: `httpx/__init__.py`:3, star import of `._auth`, which does not export `AsyncByteStream`.

Still to settle: list `.` to split a capped grep; know what `httpx/_client.py` exports; know what `httpx/_config.py` exports; know what `httpx/_content.py` exports; and 11 more.

Next: read `httpx/_client.py` from line 54, because `__all__` of `httpx/_client.py` starts at line 54 (outline header). I expect: the whole list fits the window (about 80%); the list runs past the window (about 20%). The alternative, read `httpx/_config.py` from line 13, scores the same; the seed broke the tie. Plan by outcome: fits: read `httpx/_config.py` from line 13; long: read `httpx/_config.py` from line 13.

**Call:** `read('httpx/_client.py', 54, 30)`

**Response**: outcome `fits`

```
54:__all__ = ["USE_CLIENT_DEFAULT", "AsyncClient", "Client"]
55:
56:# The type annotation for @classmethod and context managers here follows PEP 484
57:# https://www.python.org/dev/peps/pep-0484/#annotating-instance-and-class-methods
58:T = typing.TypeVar("T", bound="Client")
59:U = typing.TypeVar("U", bound="AsyncClient")
60:
61:
62:def _is_https_redirect(url: URL, location: URL) -> bool:
63:    """
64:    Return 'True' if 'location' is a HTTPS upgrade of 'url'
65:    """
66:    if url.host != location.host:
67:        return False
68:
69:    return (
70:        url.scheme == "http"
71:        and _port_or_default(url) == 80
72:        and location.scheme == "https"
73:        and _port_or_default(location) == 443
74:    )
75:
76:
77:def _port_or_default(url: URL) -> int | None:
78:    if url.port is not None:
... (5 more lines)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_client.py"
   ],
   "desc": "know what `httpx/_client.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_config.py"
   ],
   "desc": "know what `httpx/_config.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_content.py"
   ],
   "desc": "know what `httpx/_content.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_exceptions.py"
   ],
   "desc": "know what `httpx/_exceptions.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_models.py"
   ],
   "desc": "know what `httpx/_models.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_status_codes.py"
   ],
   "desc": "know what `httpx/_status_codes.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/__init__.py"
   ],
   "desc": "know what `httpx/_transports/__init__.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_urls.py"
   ],
   "desc": "know what `httpx/_urls.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/asgi.py"
   ],
   "desc": "know what `httpx/_transports/asgi.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/base.py"
   ],
   "desc": "know what `httpx/_transports/base.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/default.py"
   ],
   "desc": "know what `httpx/_transports/default.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/mock.py"
   ],
   "desc": "know what `httpx/_transports/mock.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/wsgi.py"
   ],
   "desc": "know what `httpx/_transports/wsgi.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "read('httpx/_client.py', 54, 30)",
   "key": "[\"read\", [\"httpx/_client.py\", 54, 30]]",
   "v1": [
    3423491887,
    149275035
   ],
   "v2": [
    3453346894,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_client.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_config.py', 13, 30)",
   "key": "[\"read\", [\"httpx/_config.py\", 13, 30]]",
   "v1": [
    3423491887,
    149275035
   ],
   "v2": [
    3453346894,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_config.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_content.py', 28, 30)",
   "key": "[\"read\", [\"httpx/_content.py\", 28, 30]]",
   "v1": [
    3423491887,
    149275035
   ],
   "v2": [
    3453346894,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_content.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_exceptions.py', 42, 30)",
   "key": "[\"read\", [\"httpx/_exceptions.py\", 42, 30]]",
   "v1": [
    3423491887,
    149275035
   ],
   "v2": [
    3453346894,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_exceptions.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_models.py', 51, 30)",
   "key": "[\"read\", [\"httpx/_models.py\", 51, 30]]",
   "v1": [
    3423491887,
    149275035
   ],
   "v2": [
    3453346894,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_models.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_status_codes.py', 5, 30)",
   "key": "[\"read\", [\"httpx/_status_codes.py\", 5, 30]]",
   "v1": [
    3423491887,
    149275035
   ],
   "v2": [
    3453346894,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_status_codes.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/__init__.py', 7, 30)",
   "key": "[\"read\", [\"httpx/_transports/__init__.py\", 7, 30]]",
   "v1": [
    3423491887,
    149275035
   ],
   "v2": [
    3453346894,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/__init__.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/asgi.py', 26, 30)",
   "key": "[\"read\", [\"httpx/_transports/asgi.py\", 26, 30]]",
   "v1": [
    3423491887,
    149275035
   ],
   "v2": [
    3453346894,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/asgi.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/base.py', 11, 30)",
   "key": "[\"read\", [\"httpx/_transports/base.py\", 11, 30]]",
   "v1": [
    3423491887,
    149275035
   ],
   "v2": [
    3453346894,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/base.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/default.py', 69, 30)",
   "key": "[\"read\", [\"httpx/_transports/default.py\", 69, 30]]",
   "v1": [
    3423491887,
    149275035
   ],

```
</details>

## Step 26

The statement at `httpx/_client.py`:54 binds `__all__`. `__all__` in `httpx/_client.py` lists 3 names, and `AsyncByteStream` is not among them.

Candidate modules so far: 6; statements confirmed: 4, ruled out: 3, modules with no such import: 0, pending: 13. import coverage open at `.`; star coverage open at `.`. Latest ruled out: `httpx/__init__.py`:4, star import of `._client`, which does not export `AsyncByteStream`.

Outstanding: list `.` to split a capped grep; know what `httpx/_config.py` exports; know what `httpx/_content.py` exports; know what `httpx/_exceptions.py` exports; and 10 more.

Next: read `httpx/_config.py` from line 13, because `__all__` of `httpx/_config.py` starts at line 13 (outline header). I expect: the whole list fits the window (about 80%); the list runs past the window (about 20%). The alternative, read `httpx/_content.py` from line 28, scores the same; the seed broke the tie. Plan by outcome: fits: read `httpx/_content.py` from line 28; long: read `httpx/_content.py` from line 28.

**Call:** `read('httpx/_config.py', 13, 30)`

**Response**: outcome `fits`

```
13:__all__ = ["Limits", "Proxy", "Timeout", "create_ssl_context"]
14:
15:
16:class UnsetType:
17:    pass  # pragma: no cover
18:
19:
20:UNSET = UnsetType()
21:
22:
23:def create_ssl_context(
24:    verify: ssl.SSLContext | str | bool = True,
25:    cert: CertTypes | None = None,
26:    trust_env: bool = True,
27:) -> ssl.SSLContext:
28:    import ssl
29:    import warnings
30:
31:    import certifi
32:
33:    if verify is True:
34:        if trust_env and os.environ.get("SSL_CERT_FILE"):  # pragma: nocover
35:            ctx = ssl.create_default_context(cafile=os.environ["SSL_CERT_FILE"])
36:        elif trust_env and os.environ.get("SSL_CERT_DIR"):  # pragma: nocover
37:            ctx = ssl.create_default_context(capath=os.environ["SSL_CERT_DIR"])
... (5 more lines)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_config.py"
   ],
   "desc": "know what `httpx/_config.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_content.py"
   ],
   "desc": "know what `httpx/_content.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_exceptions.py"
   ],
   "desc": "know what `httpx/_exceptions.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_models.py"
   ],
   "desc": "know what `httpx/_models.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_status_codes.py"
   ],
   "desc": "know what `httpx/_status_codes.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/__init__.py"
   ],
   "desc": "know what `httpx/_transports/__init__.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_urls.py"
   ],
   "desc": "know what `httpx/_urls.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/asgi.py"
   ],
   "desc": "know what `httpx/_transports/asgi.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/base.py"
   ],
   "desc": "know what `httpx/_transports/base.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/default.py"
   ],
   "desc": "know what `httpx/_transports/default.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/mock.py"
   ],
   "desc": "know what `httpx/_transports/mock.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/wsgi.py"
   ],
   "desc": "know what `httpx/_transports/wsgi.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "read('httpx/_config.py', 13, 30)",
   "key": "[\"read\", [\"httpx/_config.py\", 13, 30]]",
   "v1": [
    3274216852,
    149275035
   ],
   "v2": [
    3304071859,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_config.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_content.py', 28, 30)",
   "key": "[\"read\", [\"httpx/_content.py\", 28, 30]]",
   "v1": [
    3274216852,
    149275035
   ],
   "v2": [
    3304071859,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_content.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_exceptions.py', 42, 30)",
   "key": "[\"read\", [\"httpx/_exceptions.py\", 42, 30]]",
   "v1": [
    3274216852,
    149275035
   ],
   "v2": [
    3304071859,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_exceptions.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_models.py', 51, 30)",
   "key": "[\"read\", [\"httpx/_models.py\", 51, 30]]",
   "v1": [
    3274216852,
    149275035
   ],
   "v2": [
    3304071859,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_models.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_status_codes.py', 5, 30)",
   "key": "[\"read\", [\"httpx/_status_codes.py\", 5, 30]]",
   "v1": [
    3274216852,
    149275035
   ],
   "v2": [
    3304071859,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_status_codes.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/__init__.py', 7, 30)",
   "key": "[\"read\", [\"httpx/_transports/__init__.py\", 7, 30]]",
   "v1": [
    3274216852,
    149275035
   ],
   "v2": [
    3304071859,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/__init__.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/asgi.py', 26, 30)",
   "key": "[\"read\", [\"httpx/_transports/asgi.py\", 26, 30]]",
   "v1": [
    3274216852,
    149275035
   ],
   "v2": [
    3304071859,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/asgi.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/base.py', 11, 30)",
   "key": "[\"read\", [\"httpx/_transports/base.py\", 11, 30]]",
   "v1": [
    3274216852,
    149275035
   ],
   "v2": [
    3304071859,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/base.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/default.py', 69, 30)",
   "key": "[\"read\", [\"httpx/_transports/default.py\", 69, 30]]",
   "v1": [
    3274216852,
    149275035
   ],
   "v2": [
    3304071859,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/default.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/mock.py', 12, 30)",
   "key": "[\"read\", [\"httpx/_transports/mock.py\", 12, 30]]",
   "v1": [
    3274216852,
    149275035
   ],
   "v2": [
    3304071859,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
  
```
</details>

## Step 27

The statement at `httpx/_config.py`:13 binds `__all__`. `__all__` in `httpx/_config.py` lists 4 names, and `AsyncByteStream` is not among them.

Candidate modules so far: 6; statements confirmed: 4, ruled out: 4, modules with no such import: 0, pending: 12. import coverage open at `.`; star coverage open at `.`. Latest ruled out: `httpx/__init__.py`:5, star import of `._config`, which does not export `AsyncByteStream`.

Outstanding: list `.` to split a capped grep; know what `httpx/_content.py` exports; know what `httpx/_exceptions.py` exports; know what `httpx/_models.py` exports; and 9 more.

Next: read `httpx/_content.py` from line 28, because `__all__` of `httpx/_content.py` starts at line 28 (outline header). I expect: the whole list fits the window (about 80%); the list runs past the window (about 20%). The alternative, read `httpx/_exceptions.py` from line 42, scores the same; the seed broke the tie. Plan by outcome: fits: read `httpx/_exceptions.py` from line 42; long: read `httpx/_exceptions.py` from line 42.

**Call:** `read('httpx/_content.py', 28, 30)`

**Response**: outcome `fits`

```
28:__all__ = ["ByteStream"]
29:
30:
31:class ByteStream(AsyncByteStream, SyncByteStream):
32:    def __init__(self, stream: bytes) -> None:
33:        self._stream = stream
34:
35:    def __iter__(self) -> Iterator[bytes]:
36:        yield self._stream
37:
38:    async def __aiter__(self) -> AsyncIterator[bytes]:
39:        yield self._stream
40:
41:
42:class IteratorByteStream(SyncByteStream):
43:    CHUNK_SIZE = 65_536
44:
45:    def __init__(self, stream: Iterable[bytes]) -> None:
46:        self._stream = stream
47:        self._is_stream_consumed = False
48:        self._is_generator = inspect.isgenerator(stream)
49:
50:    def __iter__(self) -> Iterator[bytes]:
51:        if self._is_stream_consumed and self._is_generator:
52:            raise StreamConsumed()
... (5 more lines)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_content.py"
   ],
   "desc": "know what `httpx/_content.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_exceptions.py"
   ],
   "desc": "know what `httpx/_exceptions.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_models.py"
   ],
   "desc": "know what `httpx/_models.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_status_codes.py"
   ],
   "desc": "know what `httpx/_status_codes.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/__init__.py"
   ],
   "desc": "know what `httpx/_transports/__init__.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_urls.py"
   ],
   "desc": "know what `httpx/_urls.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/asgi.py"
   ],
   "desc": "know what `httpx/_transports/asgi.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/base.py"
   ],
   "desc": "know what `httpx/_transports/base.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/default.py"
   ],
   "desc": "know what `httpx/_transports/default.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/mock.py"
   ],
   "desc": "know what `httpx/_transports/mock.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/wsgi.py"
   ],
   "desc": "know what `httpx/_transports/wsgi.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "read('httpx/_content.py', 28, 30)",
   "key": "[\"read\", [\"httpx/_content.py\", 28, 30]]",
   "v1": [
    3124941817,
    149275035
   ],
   "v2": [
    3154796824,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_content.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_exceptions.py', 42, 30)",
   "key": "[\"read\", [\"httpx/_exceptions.py\", 42, 30]]",
   "v1": [
    3124941817,
    149275035
   ],
   "v2": [
    3154796824,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_exceptions.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_models.py', 51, 30)",
   "key": "[\"read\", [\"httpx/_models.py\", 51, 30]]",
   "v1": [
    3124941817,
    149275035
   ],
   "v2": [
    3154796824,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_models.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_status_codes.py', 5, 30)",
   "key": "[\"read\", [\"httpx/_status_codes.py\", 5, 30]]",
   "v1": [
    3124941817,
    149275035
   ],
   "v2": [
    3154796824,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_status_codes.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/__init__.py', 7, 30)",
   "key": "[\"read\", [\"httpx/_transports/__init__.py\", 7, 30]]",
   "v1": [
    3124941817,
    149275035
   ],
   "v2": [
    3154796824,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/__init__.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/asgi.py', 26, 30)",
   "key": "[\"read\", [\"httpx/_transports/asgi.py\", 26, 30]]",
   "v1": [
    3124941817,
    149275035
   ],
   "v2": [
    3154796824,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/asgi.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/base.py', 11, 30)",
   "key": "[\"read\", [\"httpx/_transports/base.py\", 11, 30]]",
   "v1": [
    3124941817,
    149275035
   ],
   "v2": [
    3154796824,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/base.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/default.py', 69, 30)",
   "key": "[\"read\", [\"httpx/_transports/default.py\", 69, 30]]",
   "v1": [
    3124941817,
    149275035
   ],
   "v2": [
    3154796824,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/default.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/mock.py', 12, 30)",
   "key": "[\"read\", [\"httpx/_transports/mock.py\", 12, 30]]",
   "v1": [
    3124941817,
    149275035
   ],
   "v2": [
    3154796824,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/mock.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/wsgi.py', 19, 30)",
   "key": "[\"read\", [\"httpx/_transports/wsgi.py\", 19, 30]]",
   "v1": [
    3124941817,
    149275035
   ],
   "v2": [
    3154796824,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "
```
</details>

## Step 28

The statement at `httpx/_content.py`:28 binds `__all__`. `__all__` in `httpx/_content.py` lists 1 names, and `AsyncByteStream` is not among them.

Candidate modules so far: 6; statements confirmed: 4, ruled out: 5, modules with no such import: 0, pending: 11. import coverage open at `.`; star coverage open at `.`. Latest ruled out: `httpx/__init__.py`:6, star import of `._content`, which does not export `AsyncByteStream`.

Open: list `.` to split a capped grep; know what `httpx/_exceptions.py` exports; know what `httpx/_models.py` exports; know what `httpx/_status_codes.py` exports; and 8 more.

Next: read `httpx/_exceptions.py` from line 42, because `__all__` of `httpx/_exceptions.py` starts at line 42 (outline header). I expect: the whole list fits the window (about 80%); the list runs past the window (about 20%). The alternative, read `httpx/_models.py` from line 51, scores the same; the seed broke the tie. Plan by outcome: fits: read `httpx/_models.py` from line 51; long: read `httpx/_models.py` from line 51.

**Call:** `read('httpx/_exceptions.py', 42, 30)`

**Response**: outcome `fits`

```
42:__all__ = [
43:    "CloseError",
44:    "ConnectError",
45:    "ConnectTimeout",
46:    "CookieConflict",
47:    "DecodingError",
48:    "HTTPError",
49:    "HTTPStatusError",
50:    "InvalidURL",
51:    "LocalProtocolError",
52:    "NetworkError",
53:    "PoolTimeout",
54:    "ProtocolError",
55:    "ProxyError",
56:    "ReadError",
57:    "ReadTimeout",
58:    "RemoteProtocolError",
59:    "RequestError",
60:    "RequestNotRead",
61:    "ResponseNotRead",
62:    "StreamClosed",
63:    "StreamConsumed",
64:    "StreamError",
65:    "TimeoutException",
66:    "TooManyRedirects",
... (5 more lines)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_exceptions.py"
   ],
   "desc": "know what `httpx/_exceptions.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_models.py"
   ],
   "desc": "know what `httpx/_models.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_status_codes.py"
   ],
   "desc": "know what `httpx/_status_codes.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/__init__.py"
   ],
   "desc": "know what `httpx/_transports/__init__.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_urls.py"
   ],
   "desc": "know what `httpx/_urls.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/asgi.py"
   ],
   "desc": "know what `httpx/_transports/asgi.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/base.py"
   ],
   "desc": "know what `httpx/_transports/base.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/default.py"
   ],
   "desc": "know what `httpx/_transports/default.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/mock.py"
   ],
   "desc": "know what `httpx/_transports/mock.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/wsgi.py"
   ],
   "desc": "know what `httpx/_transports/wsgi.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "read('httpx/_exceptions.py', 42, 30)",
   "key": "[\"read\", [\"httpx/_exceptions.py\", 42, 30]]",
   "v1": [
    2975666782,
    149275035
   ],
   "v2": [
    3005521789,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_exceptions.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_models.py', 51, 30)",
   "key": "[\"read\", [\"httpx/_models.py\", 51, 30]]",
   "v1": [
    2975666782,
    149275035
   ],
   "v2": [
    3005521789,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_models.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_status_codes.py', 5, 30)",
   "key": "[\"read\", [\"httpx/_status_codes.py\", 5, 30]]",
   "v1": [
    2975666782,
    149275035
   ],
   "v2": [
    3005521789,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_status_codes.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/__init__.py', 7, 30)",
   "key": "[\"read\", [\"httpx/_transports/__init__.py\", 7, 30]]",
   "v1": [
    2975666782,
    149275035
   ],
   "v2": [
    3005521789,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/__init__.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/asgi.py', 26, 30)",
   "key": "[\"read\", [\"httpx/_transports/asgi.py\", 26, 30]]",
   "v1": [
    2975666782,
    149275035
   ],
   "v2": [
    3005521789,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/asgi.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/base.py', 11, 30)",
   "key": "[\"read\", [\"httpx/_transports/base.py\", 11, 30]]",
   "v1": [
    2975666782,
    149275035
   ],
   "v2": [
    3005521789,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/base.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/default.py', 69, 30)",
   "key": "[\"read\", [\"httpx/_transports/default.py\", 69, 30]]",
   "v1": [
    2975666782,
    149275035
   ],
   "v2": [
    3005521789,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/default.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/mock.py', 12, 30)",
   "key": "[\"read\", [\"httpx/_transports/mock.py\", 12, 30]]",
   "v1": [
    2975666782,
    149275035
   ],
   "v2": [
    3005521789,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/mock.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/wsgi.py', 19, 30)",
   "key": "[\"read\", [\"httpx/_transports/wsgi.py\", 19, 30]]",
   "v1": [
    2975666782,
    149275035
   ],
   "v2": [
    3005521789,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/wsgi.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_types.py', 89, 30)",
   "key": "[\"read\", [\"httpx/_types.py\", 89, 30]]",
   "v1": [
    2975666782,
    149275035
   ],
   "v2": [
    3005521789,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_types.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_urls.py', 12, 30)",
   "key": "[\"read\", [\"httpx/_u
```
</details>

## Step 29

The statement at `httpx/_exceptions.py`:42 binds `__all__`. `__all__` in `httpx/_exceptions.py` lists 28 names, and `AsyncByteStream` is not among them.

Candidate modules so far: 6; statements confirmed: 4, ruled out: 6, modules with no such import: 0, pending: 10. import coverage open at `.`; star coverage open at `.`. Latest ruled out: `httpx/__init__.py`:7, star import of `._exceptions`, which does not export `AsyncByteStream`.

Still to settle: list `.` to split a capped grep; know what `httpx/_models.py` exports; know what `httpx/_status_codes.py` exports; know what `httpx/_transports/__init__.py` exports; and 7 more.

Next: read `httpx/_models.py` from line 51, because `__all__` of `httpx/_models.py` starts at line 51 (outline header). I expect: the whole list fits the window (about 80%); the list runs past the window (about 20%). The alternative, read `httpx/_status_codes.py` from line 5, scores the same; the seed broke the tie. Plan by outcome: fits: read `httpx/_status_codes.py` from line 5; long: read `httpx/_status_codes.py` from line 5.

**Call:** `read('httpx/_models.py', 51, 30)`

**Response**: outcome `fits`

```
51:__all__ = ["Cookies", "Headers", "Request", "Response"]
52:
53:SENSITIVE_HEADERS = {"authorization", "proxy-authorization"}
54:
55:
56:def _is_known_encoding(encoding: str) -> bool:
57:    """
58:    Return `True` if `encoding` is a known codec.
59:    """
60:    try:
61:        codecs.lookup(encoding)
62:    except LookupError:
63:        return False
64:    return True
65:
66:
67:def _normalize_header_key(key: str | bytes, encoding: str | None = None) -> bytes:
68:    """
69:    Coerce str/bytes into a strictly byte-wise HTTP header key.
70:    """
71:    return key if isinstance(key, bytes) else key.encode(encoding or "ascii")
72:
73:
74:def _normalize_header_value(value: str | bytes, encoding: str | None = None) -> bytes:
75:    """
... (5 more lines)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_models.py"
   ],
   "desc": "know what `httpx/_models.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_status_codes.py"
   ],
   "desc": "know what `httpx/_status_codes.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/__init__.py"
   ],
   "desc": "know what `httpx/_transports/__init__.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_urls.py"
   ],
   "desc": "know what `httpx/_urls.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/asgi.py"
   ],
   "desc": "know what `httpx/_transports/asgi.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/base.py"
   ],
   "desc": "know what `httpx/_transports/base.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/default.py"
   ],
   "desc": "know what `httpx/_transports/default.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/mock.py"
   ],
   "desc": "know what `httpx/_transports/mock.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/wsgi.py"
   ],
   "desc": "know what `httpx/_transports/wsgi.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "read('httpx/_models.py', 51, 30)",
   "key": "[\"read\", [\"httpx/_models.py\", 51, 30]]",
   "v1": [
    2826391747,
    149275035
   ],
   "v2": [
    2856246754,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_models.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_status_codes.py', 5, 30)",
   "key": "[\"read\", [\"httpx/_status_codes.py\", 5, 30]]",
   "v1": [
    2826391747,
    149275035
   ],
   "v2": [
    2856246754,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_status_codes.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/__init__.py', 7, 30)",
   "key": "[\"read\", [\"httpx/_transports/__init__.py\", 7, 30]]",
   "v1": [
    2826391747,
    149275035
   ],
   "v2": [
    2856246754,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/__init__.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/asgi.py', 26, 30)",
   "key": "[\"read\", [\"httpx/_transports/asgi.py\", 26, 30]]",
   "v1": [
    2826391747,
    149275035
   ],
   "v2": [
    2856246754,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/asgi.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/base.py', 11, 30)",
   "key": "[\"read\", [\"httpx/_transports/base.py\", 11, 30]]",
   "v1": [
    2826391747,
    149275035
   ],
   "v2": [
    2856246754,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/base.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/default.py', 69, 30)",
   "key": "[\"read\", [\"httpx/_transports/default.py\", 69, 30]]",
   "v1": [
    2826391747,
    149275035
   ],
   "v2": [
    2856246754,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/default.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/mock.py', 12, 30)",
   "key": "[\"read\", [\"httpx/_transports/mock.py\", 12, 30]]",
   "v1": [
    2826391747,
    149275035
   ],
   "v2": [
    2856246754,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/mock.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/wsgi.py', 19, 30)",
   "key": "[\"read\", [\"httpx/_transports/wsgi.py\", 19, 30]]",
   "v1": [
    2826391747,
    149275035
   ],
   "v2": [
    2856246754,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/wsgi.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_types.py', 89, 30)",
   "key": "[\"read\", [\"httpx/_types.py\", 89, 30]]",
   "v1": [
    2826391747,
    149275035
   ],
   "v2": [
    2856246754,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_types.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_urls.py', 12, 30)",
   "key": "[\"read\", [\"httpx/_urls.py\", 12, 30]]",
   "v1": [
    2826391747,
    149275035
   ],
   "v2": [
    2856246754,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_urls.py"
    ]
   ]
  },
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    565941794,
    29855007
   ],
   "v2": [
    2859563977,
    149275035
   ],
   "p_cap": [
    2,
    9
   ],
   "forecast": {
    "complete": [
     7,
     9
    ]
```
</details>

## Step 30

The statement at `httpx/_models.py`:51 binds `__all__`. `__all__` in `httpx/_models.py` lists 4 names, and `AsyncByteStream` is not among them.

Candidate modules so far: 6; statements confirmed: 4, ruled out: 7, modules with no such import: 0, pending: 9. import coverage open at `.`; star coverage open at `.`. Latest ruled out: `httpx/__init__.py`:8, star import of `._models`, which does not export `AsyncByteStream`.

Open: list `.` to split a capped grep; know what `httpx/_status_codes.py` exports; know what `httpx/_transports/__init__.py` exports; know what `httpx/_types.py` exports; and 6 more.

Next: read `httpx/_status_codes.py` from line 5, because `__all__` of `httpx/_status_codes.py` starts at line 5 (outline header). I expect: the whole list fits the window (about 80%); the list runs past the window (about 20%). The alternative, read `httpx/_transports/__init__.py` from line 7, scores the same; the seed broke the tie. Plan by outcome: fits: read `httpx/_transports/__init__.py` from line 7; long: read `httpx/_transports/__init__.py` from line 7.

**Call:** `read('httpx/_status_codes.py', 5, 30)`

**Response**: outcome `fits`

```
5:__all__ = ["codes"]
6:
7:
8:class codes(IntEnum):
9:    """HTTP status codes and reason phrases
10:
11:    Status codes from the following RFCs are all observed:
12:
13:        * RFC 7231: Hypertext Transfer Protocol (HTTP/1.1), obsoletes 2616
14:        * RFC 6585: Additional HTTP Status Codes
15:        * RFC 3229: Delta encoding in HTTP
16:        * RFC 4918: HTTP Extensions for WebDAV, obsoletes 2518
17:        * RFC 5842: Binding Extensions to WebDAV
18:        * RFC 7238: Permanent Redirect
19:        * RFC 2295: Transparent Content Negotiation in HTTP
20:        * RFC 2774: An HTTP Extension Framework
21:        * RFC 7540: Hypertext Transfer Protocol Version 2 (HTTP/2)
22:        * RFC 2324: Hyper Text Coffee Pot Control Protocol (HTCPCP/1.0)
23:        * RFC 7725: An HTTP Status Code to Report Legal Obstacles
24:        * RFC 8297: An HTTP Status Code for Indicating Hints
25:        * RFC 8470: Using Early Data in HTTP
26:    """
27:
28:    def __new__(cls, value: int, phrase: str = "") -> codes:
29:        obj = int.__new__(cls, value)
... (5 more lines)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_status_codes.py"
   ],
   "desc": "know what `httpx/_status_codes.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/__init__.py"
   ],
   "desc": "know what `httpx/_transports/__init__.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_urls.py"
   ],
   "desc": "know what `httpx/_urls.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/asgi.py"
   ],
   "desc": "know what `httpx/_transports/asgi.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/base.py"
   ],
   "desc": "know what `httpx/_transports/base.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/default.py"
   ],
   "desc": "know what `httpx/_transports/default.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/mock.py"
   ],
   "desc": "know what `httpx/_transports/mock.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/wsgi.py"
   ],
   "desc": "know what `httpx/_transports/wsgi.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "read('httpx/_status_codes.py', 5, 30)",
   "key": "[\"read\", [\"httpx/_status_codes.py\", 5, 30]]",
   "v1": [
    2677116712,
    149275035
   ],
   "v2": [
    2706971719,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_status_codes.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/__init__.py', 7, 30)",
   "key": "[\"read\", [\"httpx/_transports/__init__.py\", 7, 30]]",
   "v1": [
    2677116712,
    149275035
   ],
   "v2": [
    2706971719,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/__init__.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/asgi.py', 26, 30)",
   "key": "[\"read\", [\"httpx/_transports/asgi.py\", 26, 30]]",
   "v1": [
    2677116712,
    149275035
   ],
   "v2": [
    2706971719,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/asgi.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/base.py', 11, 30)",
   "key": "[\"read\", [\"httpx/_transports/base.py\", 11, 30]]",
   "v1": [
    2677116712,
    149275035
   ],
   "v2": [
    2706971719,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/base.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/default.py', 69, 30)",
   "key": "[\"read\", [\"httpx/_transports/default.py\", 69, 30]]",
   "v1": [
    2677116712,
    149275035
   ],
   "v2": [
    2706971719,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/default.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/mock.py', 12, 30)",
   "key": "[\"read\", [\"httpx/_transports/mock.py\", 12, 30]]",
   "v1": [
    2677116712,
    149275035
   ],
   "v2": [
    2706971719,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/mock.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/wsgi.py', 19, 30)",
   "key": "[\"read\", [\"httpx/_transports/wsgi.py\", 19, 30]]",
   "v1": [
    2677116712,
    149275035
   ],
   "v2": [
    2706971719,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/wsgi.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_types.py', 89, 30)",
   "key": "[\"read\", [\"httpx/_types.py\", 89, 30]]",
   "v1": [
    2677116712,
    149275035
   ],
   "v2": [
    2706971719,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_types.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_urls.py', 12, 30)",
   "key": "[\"read\", [\"httpx/_urls.py\", 12, 30]]",
   "v1": [
    2677116712,
    149275035
   ],
   "v2": [
    2706971719,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_urls.py"
    ]
   ]
  },
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    536086787,
    29855007
   ],
   "v2": [
    2710288942,
    149275035
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
     "split",
     "."
    ]
   ]
  }
 ],
 "choice": {
  "call": "read('httpx/_status_codes.py', 5, 30)",
  "key": "[\"read\", [\"httpx/_status_codes.py\", 5, 30]]",
  "provenance": "`__all__` of `httpx/_status_codes.py` starts at line 5 (outline header)",
  "v2": [
   2706971719,
   149275035
  ]
 },
 "forecast": {
  "fits": [
   4,
   5
  ],
  "long": [
   1,
   5
  ]
 },
 "plan": {
  "fits": "[\"read\", [\"httpx/_transports/__init__.py\", 7, 30]]",
  "long": "
```
</details>

## Step 31

The statement at `httpx/_status_codes.py`:5 binds `__all__`. `__all__` in `httpx/_status_codes.py` lists 1 names, and `AsyncByteStream` is not among them.

Candidate modules so far: 6; statements confirmed: 4, ruled out: 8, modules with no such import: 0, pending: 8. import coverage open at `.`; star coverage open at `.`. Latest ruled out: `httpx/__init__.py`:9, star import of `._status_codes`, which does not export `AsyncByteStream`.

Outstanding: list `.` to split a capped grep; know what `httpx/_transports/__init__.py` exports; know what `httpx/_types.py` exports; know what `httpx/_urls.py` exports; and 5 more.

Next: read `httpx/_transports/__init__.py` from line 7, because `__all__` of `httpx/_transports/__init__.py` starts at line 7 (outline header). I expect: the whole list fits the window (about 80%); the list runs past the window (about 20%). The alternative, read `httpx/_transports/asgi.py` from line 26, scores the same; the seed broke the tie. Plan by outcome: fits: read `httpx/_transports/asgi.py` from line 26; long: read `httpx/_transports/asgi.py` from line 26.

**Call:** `read('httpx/_transports/__init__.py', 7, 30)`

**Response**: outcome `fits`

```
7:__all__ = [
8:    "ASGITransport",
9:    "AsyncBaseTransport",
10:    "BaseTransport",
11:    "AsyncHTTPTransport",
12:    "HTTPTransport",
13:    "MockTransport",
14:    "WSGITransport",
15:]
16:
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/__init__.py"
   ],
   "desc": "know what `httpx/_transports/__init__.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_urls.py"
   ],
   "desc": "know what `httpx/_urls.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/asgi.py"
   ],
   "desc": "know what `httpx/_transports/asgi.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/base.py"
   ],
   "desc": "know what `httpx/_transports/base.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/default.py"
   ],
   "desc": "know what `httpx/_transports/default.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/mock.py"
   ],
   "desc": "know what `httpx/_transports/mock.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/wsgi.py"
   ],
   "desc": "know what `httpx/_transports/wsgi.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "read('httpx/_transports/__init__.py', 7, 30)",
   "key": "[\"read\", [\"httpx/_transports/__init__.py\", 7, 30]]",
   "v1": [
    2527841677,
    149275035
   ],
   "v2": [
    2557696684,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/__init__.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/asgi.py', 26, 30)",
   "key": "[\"read\", [\"httpx/_transports/asgi.py\", 26, 30]]",
   "v1": [
    2527841677,
    149275035
   ],
   "v2": [
    2557696684,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/asgi.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/base.py', 11, 30)",
   "key": "[\"read\", [\"httpx/_transports/base.py\", 11, 30]]",
   "v1": [
    2527841677,
    149275035
   ],
   "v2": [
    2557696684,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/base.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/default.py', 69, 30)",
   "key": "[\"read\", [\"httpx/_transports/default.py\", 69, 30]]",
   "v1": [
    2527841677,
    149275035
   ],
   "v2": [
    2557696684,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/default.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/mock.py', 12, 30)",
   "key": "[\"read\", [\"httpx/_transports/mock.py\", 12, 30]]",
   "v1": [
    2527841677,
    149275035
   ],
   "v2": [
    2557696684,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/mock.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/wsgi.py', 19, 30)",
   "key": "[\"read\", [\"httpx/_transports/wsgi.py\", 19, 30]]",
   "v1": [
    2527841677,
    149275035
   ],
   "v2": [
    2557696684,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/wsgi.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_types.py', 89, 30)",
   "key": "[\"read\", [\"httpx/_types.py\", 89, 30]]",
   "v1": [
    2527841677,
    149275035
   ],
   "v2": [
    2557696684,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_types.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_urls.py', 12, 30)",
   "key": "[\"read\", [\"httpx/_urls.py\", 12, 30]]",
   "v1": [
    2527841677,
    149275035
   ],
   "v2": [
    2557696684,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_urls.py"
    ]
   ]
  },
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    506231780,
    29855007
   ],
   "v2": [
    2561013907,
    149275035
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
     "split",
     "."
    ]
   ]
  }
 ],
 "choice": {
  "call": "read('httpx/_transports/__init__.py', 7, 30)",
  "key": "[\"read\", [\"httpx/_transports/__init__.py\", 7, 30]]",
  "provenance": "`__all__` of `httpx/_transports/__init__.py` starts at line 7 (outline header)",
  "v2": [
   2557696684,
   149275035
  ]
 },
 "forecast": {
  "fits": [
   4,
   5
  ],
  "long": [
   1,
   5
  ]
 },
 "plan": {
  "fits": "[\"read\", [\"httpx/_transports/asgi.py\", 26, 30]]",
  "long": "[\"read\", [\"httpx/_transports/asgi.py\", 26, 30]]"
 },
 "adherence": {
  "planned": "[\"read\", [\"httpx/_transports/__init__.py\", 7, 30]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "read",
   "step": 31,
   "path": "httpx/_transports/__init__.py",
   "start": 7,
   "count": 30,
   "n": 10
  },
  {
   "kind": "all_names",
   "step": 31,
   "path": "httpx/_transports/__init__.py",
   "value": [
    "ASGITransport",
    "AsyncBaseTransport",
    "BaseTransport",
    "AsyncHTTPTransport",
    "HTTPTransport",
    "MockTra
```
</details>

## Step 32

The statement at `httpx/_transports/__init__.py`:7 binds `__all__`. `__all__` in `httpx/_transports/__init__.py` lists 7 names, and `AsyncByteStream` is not among them.

Candidate modules so far: 6; statements confirmed: 4, ruled out: 9, modules with no such import: 0, pending: 7. import coverage open at `.`; star coverage open at `.`. Latest ruled out: `httpx/__init__.py`:10, star import of `._transports`, which does not export `AsyncByteStream`.

Open: list `.` to split a capped grep; know what `httpx/_types.py` exports; know what `httpx/_urls.py` exports; know what `httpx/_transports/asgi.py` exports; and 4 more.

Next: read `httpx/_transports/asgi.py` from line 26, because `__all__` of `httpx/_transports/asgi.py` starts at line 26 (outline header). I expect: the whole list fits the window (about 80%); the list runs past the window (about 20%). The alternative, read `httpx/_transports/base.py` from line 11, scores the same; the seed broke the tie. Plan by outcome: fits: read `httpx/_transports/base.py` from line 11; long: read `httpx/_transports/base.py` from line 11.

**Call:** `read('httpx/_transports/asgi.py', 26, 30)`

**Response**: outcome `fits`

```
26:__all__ = ["ASGITransport"]
27:
28:
29:def is_running_trio() -> bool:
30:    try:
31:        # sniffio is a dependency of trio.
32:
33:        # See https://github.com/python-trio/trio/issues/2802
34:        import sniffio
35:
36:        if sniffio.current_async_library() == "trio":
37:            return True
38:    except ImportError:  # pragma: nocover
39:        pass
40:
41:    return False
42:
43:
44:def create_event() -> Event:
45:    if is_running_trio():
46:        import trio
47:
48:        return trio.Event()
49:
50:    import asyncio
... (5 more lines)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_urls.py"
   ],
   "desc": "know what `httpx/_urls.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/asgi.py"
   ],
   "desc": "know what `httpx/_transports/asgi.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/base.py"
   ],
   "desc": "know what `httpx/_transports/base.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/default.py"
   ],
   "desc": "know what `httpx/_transports/default.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/mock.py"
   ],
   "desc": "know what `httpx/_transports/mock.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/wsgi.py"
   ],
   "desc": "know what `httpx/_transports/wsgi.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "read('httpx/_transports/asgi.py', 26, 30)",
   "key": "[\"read\", [\"httpx/_transports/asgi.py\", 26, 30]]",
   "v1": [
    2378566642,
    149275035
   ],
   "v2": [
    2408421649,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/asgi.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/base.py', 11, 30)",
   "key": "[\"read\", [\"httpx/_transports/base.py\", 11, 30]]",
   "v1": [
    2378566642,
    149275035
   ],
   "v2": [
    2408421649,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/base.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/default.py', 69, 30)",
   "key": "[\"read\", [\"httpx/_transports/default.py\", 69, 30]]",
   "v1": [
    2378566642,
    149275035
   ],
   "v2": [
    2408421649,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/default.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/mock.py', 12, 30)",
   "key": "[\"read\", [\"httpx/_transports/mock.py\", 12, 30]]",
   "v1": [
    2378566642,
    149275035
   ],
   "v2": [
    2408421649,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/mock.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/wsgi.py', 19, 30)",
   "key": "[\"read\", [\"httpx/_transports/wsgi.py\", 19, 30]]",
   "v1": [
    2378566642,
    149275035
   ],
   "v2": [
    2408421649,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/wsgi.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_types.py', 89, 30)",
   "key": "[\"read\", [\"httpx/_types.py\", 89, 30]]",
   "v1": [
    2378566642,
    149275035
   ],
   "v2": [
    2408421649,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_types.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_urls.py', 12, 30)",
   "key": "[\"read\", [\"httpx/_urls.py\", 12, 30]]",
   "v1": [
    2378566642,
    149275035
   ],
   "v2": [
    2408421649,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_urls.py"
    ]
   ]
  },
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    476376773,
    29855007
   ],
   "v2": [
    2411738872,
    149275035
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
     "split",
     "."
    ]
   ]
  }
 ],
 "choice": {
  "call": "read('httpx/_transports/asgi.py', 26, 30)",
  "key": "[\"read\", [\"httpx/_transports/asgi.py\", 26, 30]]",
  "provenance": "`__all__` of `httpx/_transports/asgi.py` starts at line 26 (outline header)",
  "v2": [
   2408421649,
   149275035
  ]
 },
 "forecast": {
  "fits": [
   4,
   5
  ],
  "long": [
   1,
   5
  ]
 },
 "plan": {
  "fits": "[\"read\", [\"httpx/_transports/base.py\", 11, 30]]",
  "long": "[\"read\", [\"httpx/_transports/base.py\", 11, 30]]"
 },
 "adherence": {
  "planned": "[\"read\", [\"httpx/_transports/asgi.py\", 26, 30]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "read",
   "step": 32,
   "path": "httpx/_transports/asgi.py",
   "start": 26,
   "count": 30,
   "n": 30
  },
  {
   "kind": "all_names",
   "step": 32,
   "path": "httpx/_transports/asgi.py",
   "value": [
    "ASGITransport"
   ]
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "httpx/__init__.py",
    2,
    "out",
    "star import of `._api`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    3,
    "out",
    "star import of `._auth`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    4,
    "out",
    "star import of `._client`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    5,
    "out",
    "star import of `._config`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    6,
    "out",
    "star import of `._content`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    7,
    "
```
</details>

## Step 33

The statement at `httpx/_transports/asgi.py`:26 binds `__all__`. `__all__` in `httpx/_transports/asgi.py` lists 1 names, and `AsyncByteStream` is not among them.

Candidate modules so far: 6; statements confirmed: 4, ruled out: 10, modules with no such import: 0, pending: 6. import coverage open at `.`; star coverage open at `.`. Latest ruled out: `httpx/_transports/__init__.py`:1, star import of `.asgi`, which does not export `AsyncByteStream`.

Still to settle: list `.` to split a capped grep; know what `httpx/_types.py` exports; know what `httpx/_urls.py` exports; know what `httpx/_transports/base.py` exports; and 3 more.

Next: read `httpx/_transports/base.py` from line 11, because `__all__` of `httpx/_transports/base.py` starts at line 11 (outline header). I expect: the whole list fits the window (about 80%); the list runs past the window (about 20%). The alternative, read `httpx/_transports/default.py` from line 69, scores the same; the seed broke the tie. Plan by outcome: fits: read `httpx/_transports/default.py` from line 69; long: read `httpx/_transports/default.py` from line 69.

**Call:** `read('httpx/_transports/base.py', 11, 30)`

**Response**: outcome `fits`

```
11:__all__ = ["AsyncBaseTransport", "BaseTransport"]
12:
13:
14:class BaseTransport:
15:    def __enter__(self: T) -> T:
16:        return self
17:
18:    def __exit__(
19:        self,
20:        exc_type: type[BaseException] | None = None,
21:        exc_value: BaseException | None = None,
22:        traceback: TracebackType | None = None,
23:    ) -> None:
24:        self.close()
25:
26:    def handle_request(self, request: Request) -> Response:
27:        """
28:        Send a single HTTP request and return a response.
29:
30:        Developers shouldn't typically ever need to call into this API directly,
31:        since the Client class provides all the higher level user-facing API
32:        niceties.
33:
34:        In order to properly release any network resources, the response
35:        stream should *either* be consumed immediately, with a call to
... (5 more lines)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_urls.py"
   ],
   "desc": "know what `httpx/_urls.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/base.py"
   ],
   "desc": "know what `httpx/_transports/base.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/default.py"
   ],
   "desc": "know what `httpx/_transports/default.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/mock.py"
   ],
   "desc": "know what `httpx/_transports/mock.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/wsgi.py"
   ],
   "desc": "know what `httpx/_transports/wsgi.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "read('httpx/_transports/base.py', 11, 30)",
   "key": "[\"read\", [\"httpx/_transports/base.py\", 11, 30]]",
   "v1": [
    2229291607,
    149275035
   ],
   "v2": [
    2259146614,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/base.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/default.py', 69, 30)",
   "key": "[\"read\", [\"httpx/_transports/default.py\", 69, 30]]",
   "v1": [
    2229291607,
    149275035
   ],
   "v2": [
    2259146614,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/default.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/mock.py', 12, 30)",
   "key": "[\"read\", [\"httpx/_transports/mock.py\", 12, 30]]",
   "v1": [
    2229291607,
    149275035
   ],
   "v2": [
    2259146614,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/mock.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/wsgi.py', 19, 30)",
   "key": "[\"read\", [\"httpx/_transports/wsgi.py\", 19, 30]]",
   "v1": [
    2229291607,
    149275035
   ],
   "v2": [
    2259146614,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/wsgi.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_types.py', 89, 30)",
   "key": "[\"read\", [\"httpx/_types.py\", 89, 30]]",
   "v1": [
    2229291607,
    149275035
   ],
   "v2": [
    2259146614,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_types.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_urls.py', 12, 30)",
   "key": "[\"read\", [\"httpx/_urls.py\", 12, 30]]",
   "v1": [
    2229291607,
    149275035
   ],
   "v2": [
    2259146614,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_urls.py"
    ]
   ]
  },
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    446521766,
    29855007
   ],
   "v2": [
    2262463837,
    149275035
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
     "split",
     "."
    ]
   ]
  }
 ],
 "choice": {
  "call": "read('httpx/_transports/base.py', 11, 30)",
  "key": "[\"read\", [\"httpx/_transports/base.py\", 11, 30]]",
  "provenance": "`__all__` of `httpx/_transports/base.py` starts at line 11 (outline header)",
  "v2": [
   2259146614,
   149275035
  ]
 },
 "forecast": {
  "fits": [
   4,
   5
  ],
  "long": [
   1,
   5
  ]
 },
 "plan": {
  "fits": "[\"read\", [\"httpx/_transports/default.py\", 69, 30]]",
  "long": "[\"read\", [\"httpx/_transports/default.py\", 69, 30]]"
 },
 "adherence": {
  "planned": "[\"read\", [\"httpx/_transports/base.py\", 11, 30]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "read",
   "step": 33,
   "path": "httpx/_transports/base.py",
   "start": 11,
   "count": 30,
   "n": 30
  },
  {
   "kind": "all_names",
   "step": 33,
   "path": "httpx/_transports/base.py",
   "value": [
    "AsyncBaseTransport",
    "BaseTransport"
   ]
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "httpx/__init__.py",
    2,
    "out",
    "star import of `._api`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    3,
    "out",
    "star import of `._auth`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    4,
    "out",
    "star import of `._client`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    5,
    "out",
    "star import of `._config`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    6,
    "out",
    "star import of `._content`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    7,
    "out",
    "star import of `._exceptions`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    8,
    "out",
    "star import of `._models`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    9,
    "out",
    "star import of `._status_codes`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    10,
    "out",
    "star import of `._transports`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    11,
    "pending",
    ""
  
```
</details>

## Step 34

The statement at `httpx/_transports/base.py`:11 binds `__all__`. `__all__` in `httpx/_transports/base.py` lists 2 names, and `AsyncByteStream` is not among them.

Candidate modules so far: 6; statements confirmed: 4, ruled out: 11, modules with no such import: 0, pending: 5. import coverage open at `.`; star coverage open at `.`. Latest ruled out: `httpx/_transports/__init__.py`:2, star import of `.base`, which does not export `AsyncByteStream`.

Outstanding: list `.` to split a capped grep; know what `httpx/_types.py` exports; know what `httpx/_urls.py` exports; know what `httpx/_transports/default.py` exports; and 2 more.

Next: read `httpx/_transports/default.py` from line 69, because `__all__` of `httpx/_transports/default.py` starts at line 69 (outline header). I expect: the whole list fits the window (about 80%); the list runs past the window (about 20%). The alternative, read `httpx/_transports/mock.py` from line 12, scores the same; the seed broke the tie. Plan by outcome: fits: read `httpx/_transports/mock.py` from line 12; long: read `httpx/_transports/mock.py` from line 12.

**Call:** `read('httpx/_transports/default.py', 69, 30)`

**Response**: outcome `fits`

```
69:__all__ = ["AsyncHTTPTransport", "HTTPTransport"]
70:
71:HTTPCORE_EXC_MAP: dict[type[Exception], type[httpx.HTTPError]] = {}
72:
73:
74:def _load_httpcore_exceptions() -> dict[type[Exception], type[httpx.HTTPError]]:
75:    import httpcore
76:
77:    return {
78:        httpcore.TimeoutException: TimeoutException,
79:        httpcore.ConnectTimeout: ConnectTimeout,
80:        httpcore.ReadTimeout: ReadTimeout,
81:        httpcore.WriteTimeout: WriteTimeout,
82:        httpcore.PoolTimeout: PoolTimeout,
83:        httpcore.NetworkError: NetworkError,
84:        httpcore.ConnectError: ConnectError,
85:        httpcore.ReadError: ReadError,
86:        httpcore.WriteError: WriteError,
87:        httpcore.ProxyError: ProxyError,
88:        httpcore.UnsupportedProtocol: UnsupportedProtocol,
89:        httpcore.ProtocolError: ProtocolError,
90:        httpcore.LocalProtocolError: LocalProtocolError,
91:        httpcore.RemoteProtocolError: RemoteProtocolError,
92:    }
93:
... (5 more lines)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_urls.py"
   ],
   "desc": "know what `httpx/_urls.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/default.py"
   ],
   "desc": "know what `httpx/_transports/default.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/mock.py"
   ],
   "desc": "know what `httpx/_transports/mock.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/wsgi.py"
   ],
   "desc": "know what `httpx/_transports/wsgi.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "read('httpx/_transports/default.py', 69, 30)",
   "key": "[\"read\", [\"httpx/_transports/default.py\", 69, 30]]",
   "v1": [
    2080016572,
    149275035
   ],
   "v2": [
    2109871579,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/default.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/mock.py', 12, 30)",
   "key": "[\"read\", [\"httpx/_transports/mock.py\", 12, 30]]",
   "v1": [
    2080016572,
    149275035
   ],
   "v2": [
    2109871579,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/mock.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/wsgi.py', 19, 30)",
   "key": "[\"read\", [\"httpx/_transports/wsgi.py\", 19, 30]]",
   "v1": [
    2080016572,
    149275035
   ],
   "v2": [
    2109871579,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/wsgi.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_types.py', 89, 30)",
   "key": "[\"read\", [\"httpx/_types.py\", 89, 30]]",
   "v1": [
    2080016572,
    149275035
   ],
   "v2": [
    2109871579,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_types.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_urls.py', 12, 30)",
   "key": "[\"read\", [\"httpx/_urls.py\", 12, 30]]",
   "v1": [
    2080016572,
    149275035
   ],
   "v2": [
    2109871579,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_urls.py"
    ]
   ]
  },
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    416666759,
    29855007
   ],
   "v2": [
    2113188802,
    149275035
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
     "split",
     "."
    ]
   ]
  }
 ],
 "choice": {
  "call": "read('httpx/_transports/default.py', 69, 30)",
  "key": "[\"read\", [\"httpx/_transports/default.py\", 69, 30]]",
  "provenance": "`__all__` of `httpx/_transports/default.py` starts at line 69 (outline header)",
  "v2": [
   2109871579,
   149275035
  ]
 },
 "forecast": {
  "fits": [
   4,
   5
  ],
  "long": [
   1,
   5
  ]
 },
 "plan": {
  "fits": "[\"read\", [\"httpx/_transports/mock.py\", 12, 30]]",
  "long": "[\"read\", [\"httpx/_transports/mock.py\", 12, 30]]"
 },
 "adherence": {
  "planned": "[\"read\", [\"httpx/_transports/default.py\", 69, 30]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "read",
   "step": 34,
   "path": "httpx/_transports/default.py",
   "start": 69,
   "count": 30,
   "n": 30
  },
  {
   "kind": "all_names",
   "step": 34,
   "path": "httpx/_transports/default.py",
   "value": [
    "AsyncHTTPTransport",
    "HTTPTransport"
   ]
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "httpx/__init__.py",
    2,
    "out",
    "star import of `._api`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    3,
    "out",
    "star import of `._auth`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    4,
    "out",
    "star import of `._client`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    5,
    "out",
    "star import of `._config`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    6,
    "out",
    "star import of `._content`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    7,
    "out",
    "star import of `._exceptions`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    8,
    "out",
    "star import of `._models`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    9,
    "out",
    "star import of `._status_codes`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    10,
    "out",
    "star import of `._transports`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    11,
    "pending",
    ""
   ],
   [
    "httpx/__init__.py",
    12,
    "pending",
    ""
   ],
   [
    "httpx/_client.py",
    33,
    "in",
    "`._types` resolves `AsyncByteStream` to the target"
   ],
   [
    "httpx/_content.py",
    18,
    "in",
    "`._types` resolves `AsyncByteStream` to the target"
   ],
   [
    "httpx/_models.py",
    35,
    "in",
    "`._types` resolves `AsyncByteStream` to the target"
   ],
   [
    "httpx/_multipart.py",
    10,
    "in",
    "`._types` resolves `AsyncByteStream` to the target"
   ],
   [
    "httpx/_transports/__init__.py",
    1,

```
</details>

## Step 35

The statement at `httpx/_transports/default.py`:69 binds `__all__`. `__all__` in `httpx/_transports/default.py` lists 2 names, and `AsyncByteStream` is not among them.

Candidate modules so far: 6; statements confirmed: 4, ruled out: 12, modules with no such import: 0, pending: 4. import coverage open at `.`; star coverage open at `.`. Latest ruled out: `httpx/_transports/__init__.py`:3, star import of `.default`, which does not export `AsyncByteStream`.

Still to settle: list `.` to split a capped grep; know what `httpx/_types.py` exports; know what `httpx/_urls.py` exports; know what `httpx/_transports/mock.py` exports; and 1 more.

Next: read `httpx/_transports/mock.py` from line 12, because `__all__` of `httpx/_transports/mock.py` starts at line 12 (outline header). I expect: the whole list fits the window (about 80%); the list runs past the window (about 20%). The alternative, read `httpx/_transports/wsgi.py` from line 19, scores the same; the seed broke the tie. Plan by outcome: fits: read `httpx/_transports/wsgi.py` from line 19; long: read `httpx/_transports/wsgi.py` from line 19.

**Call:** `read('httpx/_transports/mock.py', 12, 30)`

**Response**: outcome `fits`

```
12:__all__ = ["MockTransport"]
13:
14:
15:class MockTransport(AsyncBaseTransport, BaseTransport):
16:    def __init__(self, handler: SyncHandler | AsyncHandler) -> None:
17:        self.handler = handler
18:
19:    def handle_request(
20:        self,
21:        request: Request,
22:    ) -> Response:
23:        request.read()
24:        response = self.handler(request)
25:        if not isinstance(response, Response):  # pragma: no cover
26:            raise TypeError("Cannot use an async handler in a sync Client")
27:        return response
28:
29:    async def handle_async_request(
30:        self,
31:        request: Request,
32:    ) -> Response:
33:        await request.aread()
34:        response = self.handler(request)
35:
36:        # Allow handler to *optionally* be an `async` function.
... (5 more lines)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_urls.py"
   ],
   "desc": "know what `httpx/_urls.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/mock.py"
   ],
   "desc": "know what `httpx/_transports/mock.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/wsgi.py"
   ],
   "desc": "know what `httpx/_transports/wsgi.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "read('httpx/_transports/mock.py', 12, 30)",
   "key": "[\"read\", [\"httpx/_transports/mock.py\", 12, 30]]",
   "v1": [
    1930741537,
    149275035
   ],
   "v2": [
    1960596544,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/mock.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_transports/wsgi.py', 19, 30)",
   "key": "[\"read\", [\"httpx/_transports/wsgi.py\", 19, 30]]",
   "v1": [
    1930741537,
    149275035
   ],
   "v2": [
    1960596544,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/wsgi.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_types.py', 89, 30)",
   "key": "[\"read\", [\"httpx/_types.py\", 89, 30]]",
   "v1": [
    1930741537,
    149275035
   ],
   "v2": [
    1960596544,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_types.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_urls.py', 12, 30)",
   "key": "[\"read\", [\"httpx/_urls.py\", 12, 30]]",
   "v1": [
    1930741537,
    149275035
   ],
   "v2": [
    1960596544,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_urls.py"
    ]
   ]
  },
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    386811752,
    29855007
   ],
   "v2": [
    1963913767,
    149275035
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
     "split",
     "."
    ]
   ]
  }
 ],
 "choice": {
  "call": "read('httpx/_transports/mock.py', 12, 30)",
  "key": "[\"read\", [\"httpx/_transports/mock.py\", 12, 30]]",
  "provenance": "`__all__` of `httpx/_transports/mock.py` starts at line 12 (outline header)",
  "v2": [
   1960596544,
   149275035
  ]
 },
 "forecast": {
  "fits": [
   4,
   5
  ],
  "long": [
   1,
   5
  ]
 },
 "plan": {
  "fits": "[\"read\", [\"httpx/_transports/wsgi.py\", 19, 30]]",
  "long": "[\"read\", [\"httpx/_transports/wsgi.py\", 19, 30]]"
 },
 "adherence": {
  "planned": "[\"read\", [\"httpx/_transports/mock.py\", 12, 30]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "read",
   "step": 35,
   "path": "httpx/_transports/mock.py",
   "start": 12,
   "count": 30,
   "n": 30
  },
  {
   "kind": "all_names",
   "step": 35,
   "path": "httpx/_transports/mock.py",
   "value": [
    "MockTransport"
   ]
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "httpx/__init__.py",
    2,
    "out",
    "star import of `._api`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    3,
    "out",
    "star import of `._auth`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    4,
    "out",
    "star import of `._client`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    5,
    "out",
    "star import of `._config`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    6,
    "out",
    "star import of `._content`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    7,
    "out",
    "star import of `._exceptions`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    8,
    "out",
    "star import of `._models`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    9,
    "out",
    "star import of `._status_codes`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    10,
    "out",
    "star import of `._transports`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    11,
    "pending",
    ""
   ],
   [
    "httpx/__init__.py",
    12,
    "pending",
    ""
   ],
   [
    "httpx/_client.py",
    33,
    "in",
    "`._types` resolves `AsyncByteStream` to the target"
   ],
   [
    "httpx/_content.py",
    18,
    "in",
    "`._types` resolves `AsyncByteStream` to the target"
   ],
   [
    "httpx/_models.py",
    35,
    "in",
    "`._types` resolves `AsyncByteStream` to the target"
   ],
   [
    "httpx/_multipart.py",
    10,
    "in",
    "`._types` resolves `AsyncByteStream` to the target"
   ],
   [
    "httpx/_transports/__init__.py",
    1,
    "out",
    "star import of `.asgi`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/_transports/__init__.py",
    2,
    "out",
    "star import of `.base`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/_transports/__init__.py",
    3,
    "out",
    "star import of `.default`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/_transports/__init__.py",
    4,
    "out",
    "star import of `.mock`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/_transports/__init__.py",
    5,
    "pending",
    ""
   ]
  ],
  "uncovered": {
   "IMPORT": [
    [
     "split",
   
```
</details>

## Step 36

The statement at `httpx/_transports/mock.py`:12 binds `__all__`. `__all__` in `httpx/_transports/mock.py` lists 1 names, and `AsyncByteStream` is not among them.

Candidate modules so far: 6; statements confirmed: 4, ruled out: 13, modules with no such import: 0, pending: 3. import coverage open at `.`; star coverage open at `.`. Latest ruled out: `httpx/_transports/__init__.py`:4, star import of `.mock`, which does not export `AsyncByteStream`.

Open: list `.` to split a capped grep; know what `httpx/_types.py` exports; know what `httpx/_urls.py` exports; know what `httpx/_transports/wsgi.py` exports.

Next: read `httpx/_transports/wsgi.py` from line 19, because `__all__` of `httpx/_transports/wsgi.py` starts at line 19 (outline header). I expect: the whole list fits the window (about 80%); the list runs past the window (about 20%). The alternative, read `httpx/_types.py` from line 89, scores the same; the seed broke the tie. Plan by outcome: fits: read `httpx/_types.py` from line 89; long: read `httpx/_types.py` from line 89.

**Call:** `read('httpx/_transports/wsgi.py', 19, 30)`

**Response**: outcome `fits`

```
19:__all__ = ["WSGITransport"]
20:
21:
22:def _skip_leading_empty_chunks(body: typing.Iterable[_T]) -> typing.Iterable[_T]:
23:    body = iter(body)
24:    for chunk in body:
25:        if chunk:
26:            return itertools.chain([chunk], body)
27:    return []
28:
29:
30:class WSGIByteStream(SyncByteStream):
31:    def __init__(self, result: typing.Iterable[bytes]) -> None:
32:        self._close = getattr(result, "close", None)
33:        self._result = _skip_leading_empty_chunks(result)
34:
35:    def __iter__(self) -> typing.Iterator[bytes]:
36:        for part in self._result:
37:            yield part
38:
39:    def close(self) -> None:
40:        if self._close is not None:
41:            self._close()
42:
43:
... (5 more lines)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_urls.py"
   ],
   "desc": "know what `httpx/_urls.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/wsgi.py"
   ],
   "desc": "know what `httpx/_transports/wsgi.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "read('httpx/_transports/wsgi.py', 19, 30)",
   "key": "[\"read\", [\"httpx/_transports/wsgi.py\", 19, 30]]",
   "v1": [
    1781466502,
    149275035
   ],
   "v2": [
    1811321509,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_transports/wsgi.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_types.py', 89, 30)",
   "key": "[\"read\", [\"httpx/_types.py\", 89, 30]]",
   "v1": [
    1781466502,
    149275035
   ],
   "v2": [
    1811321509,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_types.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_urls.py', 12, 30)",
   "key": "[\"read\", [\"httpx/_urls.py\", 12, 30]]",
   "v1": [
    1781466502,
    149275035
   ],
   "v2": [
    1811321509,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_urls.py"
    ]
   ]
  },
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    356956745,
    29855007
   ],
   "v2": [
    1814638732,
    149275035
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
     "split",
     "."
    ]
   ]
  }
 ],
 "choice": {
  "call": "read('httpx/_transports/wsgi.py', 19, 30)",
  "key": "[\"read\", [\"httpx/_transports/wsgi.py\", 19, 30]]",
  "provenance": "`__all__` of `httpx/_transports/wsgi.py` starts at line 19 (outline header)",
  "v2": [
   1811321509,
   149275035
  ]
 },
 "forecast": {
  "fits": [
   4,
   5
  ],
  "long": [
   1,
   5
  ]
 },
 "plan": {
  "fits": "[\"read\", [\"httpx/_types.py\", 89, 30]]",
  "long": "[\"read\", [\"httpx/_types.py\", 89, 30]]"
 },
 "adherence": {
  "planned": "[\"read\", [\"httpx/_transports/wsgi.py\", 19, 30]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "read",
   "step": 36,
   "path": "httpx/_transports/wsgi.py",
   "start": 19,
   "count": 30,
   "n": 30
  },
  {
   "kind": "all_names",
   "step": 36,
   "path": "httpx/_transports/wsgi.py",
   "value": [
    "WSGITransport"
   ]
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "httpx/__init__.py",
    2,
    "out",
    "star import of `._api`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    3,
    "out",
    "star import of `._auth`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    4,
    "out",
    "star import of `._client`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    5,
    "out",
    "star import of `._config`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    6,
    "out",
    "star import of `._content`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    7,
    "out",
    "star import of `._exceptions`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    8,
    "out",
    "star import of `._models`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    9,
    "out",
    "star import of `._status_codes`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    10,
    "out",
    "star import of `._transports`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    11,
    "pending",
    ""
   ],
   [
    "httpx/__init__.py",
    12,
    "pending",
    ""
   ],
   [
    "httpx/_client.py",
    33,
    "in",
    "`._types` resolves `AsyncByteStream` to the target"
   ],
   [
    "httpx/_content.py",
    18,
    "in",
    "`._types` resolves `AsyncByteStream` to the target"
   ],
   [
    "httpx/_models.py",
    35,
    "in",
    "`._types` resolves `AsyncByteStream` to the target"
   ],
   [
    "httpx/_multipart.py",
    10,
    "in",
    "`._types` resolves `AsyncByteStream` to the target"
   ],
   [
    "httpx/_transports/__init__.py",
    1,
    "out",
    "star import of `.asgi`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/_transports/__init__.py",
    2,
    "out",
    "star import of `.base`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/_transports/__init__.py",
    3,
    "out",
    "star import of `.default`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/_transports/__init__.py",
    4,
    "out",
    "star import of `.mock`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/_transports/__init__.py",
    5,
    "out",
    "star import of `.wsgi`, which does not export `AsyncByteStream`"
   ]
  ],
  "uncovered": {
   "IMPORT": [
    [
     "split",
     "."
    ]
   ],
   "STAR": [
    [
     "split",
     "."
    ]
   ]
  }
 }
}
```
</details>

## Step 37

The statement at `httpx/_transports/wsgi.py`:19 binds `__all__`. `__all__` in `httpx/_transports/wsgi.py` lists 1 names, and `AsyncByteStream` is not among them.

Candidate modules so far: 6; statements confirmed: 4, ruled out: 14, modules with no such import: 0, pending: 2. import coverage open at `.`; star coverage open at `.`. Latest ruled out: `httpx/_transports/__init__.py`:5, star import of `.wsgi`, which does not export `AsyncByteStream`.

Outstanding: list `.` to split a capped grep; know what `httpx/_types.py` exports; know what `httpx/_urls.py` exports.

Next: read `httpx/_types.py` from line 89, because `__all__` of `httpx/_types.py` starts at line 89 (outline header). I expect: the whole list fits the window (about 80%); the list runs past the window (about 20%). The alternative, read `httpx/_urls.py` from line 12, scores the same; the seed broke the tie. Plan by outcome: fits: read `httpx/_urls.py` from line 12; long: read `httpx/_urls.py` from line 12.

**Call:** `read('httpx/_types.py', 89, 30)`

**Response**: outcome `fits`

```
89:__all__ = ["AsyncByteStream", "SyncByteStream"]
90:
91:
92:class SyncByteStream:
93:    def __iter__(self) -> Iterator[bytes]:
94:        raise NotImplementedError(
95:            "The '__iter__' method must be implemented."
96:        )  # pragma: no cover
97:        yield b""  # pragma: no cover
98:
99:    def close(self) -> None:
100:        """
101:        Subclasses can override this method to release any network resources
102:        after a request/response cycle is complete.
103:        """
104:
105:
106:class AsyncByteStream:
107:    async def __aiter__(self) -> AsyncIterator[bytes]:
108:        raise NotImplementedError(
109:            "The '__aiter__' method must be implemented."
110:        )  # pragma: no cover
111:        yield b""  # pragma: no cover
112:
113:    async def aclose(self) -> None:
... (2 more lines)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_types.py"
   ],
   "desc": "know what `httpx/_types.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_urls.py"
   ],
   "desc": "know what `httpx/_urls.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "read('httpx/_types.py', 89, 30)",
   "key": "[\"read\", [\"httpx/_types.py\", 89, 30]]",
   "v1": [
    1632191467,
    149275035
   ],
   "v2": [
    1662046474,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_types.py"
    ]
   ]
  },
  {
   "call": "read('httpx/_urls.py', 12, 30)",
   "key": "[\"read\", [\"httpx/_urls.py\", 12, 30]]",
   "v1": [
    1632191467,
    149275035
   ],
   "v2": [
    1662046474,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_urls.py"
    ]
   ]
  },
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    327101738,
    29855007
   ],
   "v2": [
    1665363697,
    149275035
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
     "split",
     "."
    ]
   ]
  }
 ],
 "choice": {
  "call": "read('httpx/_types.py', 89, 30)",
  "key": "[\"read\", [\"httpx/_types.py\", 89, 30]]",
  "provenance": "`__all__` of `httpx/_types.py` starts at line 89 (outline header)",
  "v2": [
   1662046474,
   149275035
  ]
 },
 "forecast": {
  "fits": [
   4,
   5
  ],
  "long": [
   1,
   5
  ]
 },
 "plan": {
  "fits": "[\"read\", [\"httpx/_urls.py\", 12, 30]]",
  "long": "[\"read\", [\"httpx/_urls.py\", 12, 30]]"
 },
 "adherence": {
  "planned": "[\"read\", [\"httpx/_types.py\", 89, 30]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "read",
   "step": 37,
   "path": "httpx/_types.py",
   "start": 89,
   "count": 30,
   "n": 27
  },
  {
   "kind": "all_names",
   "step": 37,
   "path": "httpx/_types.py",
   "value": [
    "AsyncByteStream",
    "SyncByteStream"
   ]
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "httpx/__init__.py",
    2,
    "out",
    "star import of `._api`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    3,
    "out",
    "star import of `._auth`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    4,
    "out",
    "star import of `._client`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    5,
    "out",
    "star import of `._config`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    6,
    "out",
    "star import of `._content`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    7,
    "out",
    "star import of `._exceptions`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    8,
    "out",
    "star import of `._models`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    9,
    "out",
    "star import of `._status_codes`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    10,
    "out",
    "star import of `._transports`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    11,
    "in",
    "star import of `._types`, which exports `AsyncByteStream` from the target"
   ],
   [
    "httpx/__init__.py",
    12,
    "pending",
    ""
   ],
   [
    "httpx/_client.py",
    33,
    "in",
    "`._types` resolves `AsyncByteStream` to the target"
   ],
   [
    "httpx/_content.py",
    18,
    "in",
    "`._types` resolves `AsyncByteStream` to the target"
   ],
   [
    "httpx/_models.py",
    35,
    "in",
    "`._types` resolves `AsyncByteStream` to the target"
   ],
   [
    "httpx/_multipart.py",
    10,
    "in",
    "`._types` resolves `AsyncByteStream` to the target"
   ],
   [
    "httpx/_transports/__init__.py",
    1,
    "out",
    "star import of `.asgi`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/_transports/__init__.py",
    2,
    "out",
    "star import of `.base`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/_transports/__init__.py",
    3,
    "out",
    "star import of `.default`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/_transports/__init__.py",
    4,
    "out",
    "star import of `.mock`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/_transports/__init__.py",
    5,
    "out",
    "star import of `.wsgi`, which does not export `AsyncByteStream`"
   ]
  ],
  "uncovered": {
   "IMPORT": [
    [
     "split",
     "."
    ]
   ],
   "STAR": [
    [
     "split",
     "."
    ]
   ]
  }
 }
}
```
</details>

## Step 38

The statement at `httpx/_types.py`:89 binds `__all__`. `__all__` in `httpx/_types.py` lists 2 names, and it names `AsyncByteStream`.

Candidate modules so far: 6; statements confirmed: 5, ruled out: 14, modules with no such import: 0, pending: 1. import coverage open at `.`; star coverage open at `.`. Latest ruled out: `httpx/_transports/__init__.py`:5, star import of `.wsgi`, which does not export `AsyncByteStream`.

Still to settle: list `.` to split a capped grep; know what `httpx/_urls.py` exports.

Next: read `httpx/_urls.py` from line 12, because `__all__` of `httpx/_urls.py` starts at line 12 (outline header). I expect: the whole list fits the window (about 80%); the list runs past the window (about 20%). The alternative, list `.`, is more likely to hit the cap (about 20% against under 5%). Plan by outcome: fits: list `.`; long: list `.`.

**Call:** `read('httpx/_urls.py', 12, 30)`

**Response**: outcome `fits`

```
12:__all__ = ["URL", "QueryParams"]
13:
14:
15:class URL:
16:    """
17:    url = httpx.URL("HTTPS://jo%40email.com:a%20secret@müller.de:1234/pa%20th?search=ab#anchorlink")
18:
19:    assert url.scheme == "https"
20:    assert url.username == "jo@email.com"
21:    assert url.password == "a secret"
22:    assert url.userinfo == b"jo%40email.com:a%20secret"
23:    assert url.host == "müller.de"
24:    assert url.raw_host == b"xn--mller-kva.de"
25:    assert url.port == 1234
26:    assert url.netloc == b"xn--mller-kva.de:1234"
27:    assert url.path == "/pa th"
28:    assert url.query == b"?search=ab"
29:    assert url.raw_path == b"/pa%20th?search=ab"
30:    assert url.fragment == "anchorlink"
31:
32:    The components of a URL are broken down like this:
33:
34:       https://jo%40email.com:a%20secret@müller.de:1234/pa%20th?search=ab#anchorlink
35:    [scheme]   [  username  ] [password] [ host ][port][ path ] [ query ] [fragment]
36:               [       userinfo        ] [   netloc   ][    raw_path    ]
... (5 more lines)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "httpx/_urls.py"
   ],
   "desc": "know what `httpx/_urls.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    297246731,
    29855007
   ],
   "v2": [
    1516088662,
    149275035
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
     "split",
     "."
    ]
   ]
  },
  {
   "call": "read('httpx/_urls.py', 12, 30)",
   "key": "[\"read\", [\"httpx/_urls.py\", 12, 30]]",
   "v1": [
    1482916432,
    149275035
   ],
   "v2": [
    1516088662,
    149275035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     4,
     5
    ],
    "long": [
     1,
     5
    ]
   },
   "serves": [
    [
     "all",
     "httpx/_urls.py"
    ]
   ]
  }
 ],
 "choice": {
  "call": "read('httpx/_urls.py', 12, 30)",
  "key": "[\"read\", [\"httpx/_urls.py\", 12, 30]]",
  "provenance": "`__all__` of `httpx/_urls.py` starts at line 12 (outline header)",
  "v2": [
   1516088662,
   149275035
  ]
 },
 "forecast": {
  "fits": [
   4,
   5
  ],
  "long": [
   1,
   5
  ]
 },
 "plan": {
  "fits": "[\"ls\", [\".\"]]",
  "long": "[\"ls\", [\".\"]]"
 },
 "adherence": {
  "planned": "[\"read\", [\"httpx/_urls.py\", 12, 30]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "read",
   "step": 38,
   "path": "httpx/_urls.py",
   "start": 12,
   "count": 30,
   "n": 30
  },
  {
   "kind": "all_names",
   "step": 38,
   "path": "httpx/_urls.py",
   "value": [
    "URL",
    "QueryParams"
   ]
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "httpx/__init__.py",
    2,
    "out",
    "star import of `._api`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    3,
    "out",
    "star import of `._auth`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    4,
    "out",
    "star import of `._client`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    5,
    "out",
    "star import of `._config`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    6,
    "out",
    "star import of `._content`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    7,
    "out",
    "star import of `._exceptions`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    8,
    "out",
    "star import of `._models`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    9,
    "out",
    "star import of `._status_codes`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    10,
    "out",
    "star import of `._transports`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    11,
    "in",
    "star import of `._types`, which exports `AsyncByteStream` from the target"
   ],
   [
    "httpx/__init__.py",
    12,
    "out",
    "star import of `._urls`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/_client.py",
    33,
    "in",
    "`._types` resolves `AsyncByteStream` to the target"
   ],
   [
    "httpx/_content.py",
    18,
    "in",
    "`._types` resolves `AsyncByteStream` to the target"
   ],
   [
    "httpx/_models.py",
    35,
    "in",
    "`._types` resolves `AsyncByteStream` to the target"
   ],
   [
    "httpx/_multipart.py",
    10,
    "in",
    "`._types` resolves `AsyncByteStream` to the target"
   ],
   [
    "httpx/_transports/__init__.py",
    1,
    "out",
    "star import of `.asgi`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/_transports/__init__.py",
    2,
    "out",
    "star import of `.base`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/_transports/__init__.py",
    3,
    "out",
    "star import of `.default`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/_transports/__init__.py",
    4,
    "out",
    "star import of `.mock`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/_transports/__init__.py",
    5,
    "out",
    "star import of `.wsgi`, which does not export `AsyncByteStream`"
   ]
  ],
  "uncovered": {
   "IMPORT": [
    [
     "split",
     "."
    ]
   ],
   "STAR": [
    [
     "split",
     "."
    ]
   ]
  }
 }
}
```
</details>

## Step 39

The statement at `httpx/_urls.py`:12 binds `__all__`. `__all__` in `httpx/_urls.py` lists 2 names, and `AsyncByteStream` is not among them.

Candidate modules so far: 6; statements confirmed: 5, ruled out: 15, modules with no such import: 0, pending: 0. import coverage open at `.`; star coverage open at `.`. Latest ruled out: `httpx/_transports/__init__.py`:5, star import of `.wsgi`, which does not export `AsyncByteStream`.

Still to settle: list `.` to split a capped grep.

Next: list `.`, because children of `.` to split the capped grep. I expect: a complete listing settles which files exist (about 80%); a capped listing settles nothing (about 20%). Plan by outcome: complete: outline the module it reveals; cap: work the items it opens.

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
   "kind": "split",
   "key": [
    "split",
    "."
   ],
   "desc": "list `.` to split a capped grep"
  }
 ],
 "candidates": [
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    267391724,
    29855007
   ],
   "v2": [
    267391724,
    29855007
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
     "split",
     "."
    ]
   ]
  }
 ],
 "choice": {
  "call": "ls('.')",
  "key": "[\"ls\", [\".\"]]",
  "provenance": "children of `.` to split the capped grep",
  "v2": [
   267391724,
   29855007
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
  "cap": "continue"
 },
 "adherence": {
  "planned": "[\"ls\", [\".\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "listing",
   "step": 39,
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
  "verdicts": [
   [
    "httpx/__init__.py",
    2,
    "out",
    "star import of `._api`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    3,
    "out",
    "star import of `._auth`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    4,
    "out",
    "star import of `._client`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    5,
    "out",
    "star import of `._config`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    6,
    "out",
    "star import of `._content`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    7,
    "out",
    "star import of `._exceptions`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    8,
    "out",
    "star import of `._models`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    9,
    "out",
    "star import of `._status_codes`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    10,
    "out",
    "star import of `._transports`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/__init__.py",
    11,
    "in",
    "star import of `._types`, which exports `AsyncByteStream` from the target"
   ],
   [
    "httpx/__init__.py",
    12,
    "out",
    "star import of `._urls`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/_client.py",
    33,
    "in",
    "`._types` resolves `AsyncByteStream` to the target"
   ],
   [
    "httpx/_content.py",
    18,
    "in",
    "`._types` resolves `AsyncByteStream` to the target"
   ],
   [
    "httpx/_models.py",
    35,
    "in",
    "`._types` resolves `AsyncByteStream` to the target"
   ],
   [
    "httpx/_multipart.py",
    10,
    "in",
    "`._types` resolves `AsyncByteStream` to the target"
   ],
   [
    "httpx/_transports/__init__.py",
    1,
    "out",
    "star import of `.asgi`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/_transports/__init__.py",
    2,
    "out",
    "star import of `.base`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/_transports/__init__.py",
    3,
    "out",
    "star import of `.default`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/_transports/__init__.py",
    4,
    "out",
    "star import of `.mock`, which does not export `AsyncByteStream`"
   ],
   [
    "httpx/_transports/__init__.py",
    5,
    "out",
    "star import of `.wsgi`, which does not export `AsyncByteStream`"
   ]
  ],
  "uncovered": {
   "IMPORT": [
    [
     "grep",
     ".github"
    ],
    [
     "grep",
     "docs"
    ],
    [
     "grep",
     "httpx"
    ],
    [
     "grep",
     "tests"
    ]
   ],
   "STAR": [
    [
     "grep",
     ".github"
    ],
    [
     "grep",
     "docs"
    ],
    [
     "grep",
     "httpx"
    ],
    [
     "grep",
     "tests"
    ]
   ]
  }
 }
}
```
</details>

## Step 40

`.` lists 10 entries (complete): `.github/`, `docs/`, `httpx/`, `tests/`.

Candidate modules so far: 6; statements confirmed: 5, ruled out: 15, modules with no such import: 0, pending: 0. import coverage open at `.github`, `docs`, `httpx`, `tests`; star coverage open at `.github`, `docs`, `httpx`, `tests`. Latest ruled out: `httpx/_transports/__init__.py`:5, star import of `.wsgi`, which does not export `AsyncByteStream`.

Open: cover `.github` for import lines; cover `docs` for import lines; cover `httpx` for import lines; cover `tests` for import lines; and 4 more.

Next: grep from-imports naming `AsyncByteStream` or star imports under `.github`, because import and star lines under `.github` in one call. I expect: no hits (about 90%); hits under the cap (about 10%); a capped result (under 5%). The alternative, grep from-imports naming `AsyncByteStream` or star imports under `docs`, scores the same; the seed broke the tie. Plan by outcome: zero: grep from-imports naming `AsyncByteStream` or star imports under `docs`; mid: grep from-imports naming `AsyncByteStream` or star imports under `docs`; cap: grep from-imports naming `AsyncByteStream` or star imports under `docs`.

**Call:** `grep('^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bAsyncByteStream\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*AsyncByteStream\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$', '.github')`

**Response**: outcome `zero`

```

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
    ".github"
   ],
   "desc": "cover `.github` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "IMPORT",
    "docs"
   ],
   "desc": "cover `docs` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "IMPORT",
    "httpx"
   ],
   "desc": "cover `httpx` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "IMPORT",
    "tests"
   ],
   "desc": "cover `tests` for import lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    ".github"
   ],
   "desc": "cover `.github` for star lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "docs"
   ],
   "desc": "cover `docs` for star lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "httpx"
   ],
   "desc": "cover `httpx` for star lines"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "tests"
   ],
   "desc": "cover `tests` for star lines"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bAsyncByteStream\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*AsyncByteStream\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.github')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bAsyncByteStream\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*AsyncByteStream\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".github\"]]",
   "v1": [
    2847172160014752127,
    327633968195659125
   ],
   "v2": [
    7385996665207471579,
    982901904586977375
   ],
   "p_cap": [
    2,
    231
   ],
   "forecast": {
    "zero": [
     68,
     77
    ],
    "mid": [
     25,
     231
    ],
    "cap": [
     2,
     231
    ]
   },
   "serves": [
    [
     "cover",
     "IMPORT",
     ".github"
    ],
    [
     "cover",
     "STAR",
     ".github"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bAsyncByteStream\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*AsyncByteStream\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', 'docs')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bAsyncByteStream\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*AsyncByteStream\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \"docs\"]]",
   "v1": [
    2847172160014752127,
    327633968195659125
   ],
   "v2": [
    7385996665207471579,
    982901904586977375
   ],
   "p_cap": [
    2,
    231
   ],
   "forecast": {
    "zero": [
     68,
     77
    ],
    "mid": [
     25,
     231
    ],
    "cap": [
     2,
     231
    ]
   },
   "serves": [
    [
     "cover",
     "IMPORT",
     "docs"
    ],
    [
     "cover",
     "STAR",
     "docs"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bAsyncByteStream\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*AsyncByteStream\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', 'httpx')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bAsyncByteStream\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*AsyncByteStream\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \"httpx\"]]",
   "v1": [
    2847172160014752127,
    327633968195659125
   ],
   "v2": [
    7385996665207471579,
    982901904586977375
   ],
   "p_cap": [
    2,
    231
   ],
   "forecast": {
    "zero": [
     68,
     77
    ],
    "mid": [
     25,
     231
    ],
    "cap": [
     2,
     231
    ]
   },
   "serves": [
    [
     "cover",
     "IMPORT",
     "httpx"
    ],
    [
     "cover",
     "STAR",
     "httpx"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bAsyncByteStream\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*AsyncByteStream\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', 'tests')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bAsyncByteStream\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*AsyncByteStream\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \"tests\"]]",
   "v1": [
    2847172160014752127,
    327633968195659125
   ],
   "v2": [
    7385996665207471579,
    982901904586977375
   ],
   "p_cap": [
    2,
    231
   ],
   "forecast": {
    "zero": [
     68,
     77
    ],
    "mid": [
     25,
     231
    ],
    "cap": [
     2,
     231
    ]
   },
   "serves": [
    [
     "cover",
     "IMPORT",
     "tests"
    ],
    [
     "cover",
     "STAR",
     "tests"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bAsyncByteStream\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*AsyncByteStream\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.github')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bAsyncByteStream\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*AsyncByteStream\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".github\"]]",
   "v1": [
    125935536297156379,
    12764959799830875
   ],
   "v2": [
    2847172160014752127,
    327633968195659125
   ],
   "p_cap": [
    1,
    225
   ],
   "forecast": {
    "zero": [
     214,
     225
    ],
    "mid": [
     2,
     45
    ],
    "cap": [
     1,
     225
    ]
   },
   "serves": [
    [
     "cover",
     "IMPORT",
     ".github"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bAsyncByteStream\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*AsyncByteStream\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', 'docs')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bAsyncByteStream\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\
```
</details>

## Final

Stopping without a certificate: budget. What remains open is listed in the sidecar.

**Answer:** `null`  
**Stopped:** budget after 40 calls