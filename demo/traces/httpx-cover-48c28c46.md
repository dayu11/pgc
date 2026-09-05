# httpx-cover-48c28c46

**Repository:** httpx  
**Family:** cover  
**Seed:** 0, prior d99074a5d38bc2d8

## Task

`RemoteProtocolError` is defined at `httpx/_exceptions.py:232` (class). List every module-level import statement in the snapshot that imports this definition: `from ... import` statements naming it (directly or with `as`), and star imports of modules that export it. Answer as `path:line` entries.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

Nothing seen yet beyond the task text.

Candidate modules so far: 0; statements confirmed: 0, ruled out: 0, modules with no such import: 0, pending: 0. import coverage open at `.`; star coverage open at `.`.

Outstanding: cover `.` for import lines; cover `.` for star lines.

Next: grep from-imports naming `RemoteProtocolError` or star imports under `.`, because import and star lines under `.` in one call. I expect: hits under the cap (about 55%); no hits (about 40%); a capped result (about 10%). The alternative, grep from-imports naming `RemoteProtocolError` under `.`, serves fewer of the open items. Plan by outcome: zero: done; mid: outline each module that appears; cap: list the scope and split it.

**Call:** `grep('^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bRemoteProtocolError\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*RemoteProtocolError\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$', '.')`

**Response**: outcome `mid`

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
httpx/_client.py:25:    RemoteProtocolError,
httpx/_transports/__init__.py:1:from .asgi import *
httpx/_transports/__init__.py:2:from .base import *
httpx/_transports/__init__.py:3:from .default import *
httpx/_transports/__init__.py:4:from .mock import *
httpx/_transports/__init__.py:5:from .wsgi import *
httpx/_transports/default.py:49:    RemoteProtocolError,
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
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bRemoteProtocolError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*RemoteProtocolError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bRemoteProtocolError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*RemoteProtocolError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
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
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bRemoteProtocolError\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*RemoteProtocolError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bRemoteProtocolError\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*RemoteProtocolError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
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
  "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bRemoteProtocolError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*RemoteProtocolError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
  "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bRemoteProtocolError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*RemoteProtocolError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
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
 "adherence": null,
 "facts": [
  {
   "kind": "grep",
   "step": 1,
   "pattern": "^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bRemoteProtocolError\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*RemoteProtocolError\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$",
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
     25
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
    ],
    [
     "httpx/_transports/default.py",
     49
    ]
   ],
   "capped": false
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
    "httpx/_transports/__init__.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "httpx/_transports/default.py",
    0,
    "pending",
    "outline not yet seen"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  }
 }
}
```
</details>

## Step 2

The grep under `.` returned 18 lines, under the cap, so these are all of them: `httpx/__init__.py`, `httpx/_client.py`, `httpx/_transports/__init__.py`, `httpx/_transports/default.py`.

Candidate modules so far: 4; statements confirmed: 0, ruled out: 0, modules with no such import: 0, pending: 4. import coverage complete; star coverage complete.

Still to settle: outline `httpx/__init__.py` for its `RemoteProtocolError` imports; outline `httpx/_client.py` for its `RemoteProtocolError` imports; outline `httpx/_transports/__init__.py` for its `RemoteProtocolError` imports; outline `httpx/_transports/default.py` for its `RemoteProtocolError` imports.

Next: outline `httpx/_transports/default.py` filtered to `RemoteProtocolError`, because `httpx/_transports/default.py` had a matching line (step 1); its outline names every `RemoteProtocolError` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `httpx/__init__.py` filtered to `RemoteProtocolError`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `httpx/__init__.py` filtered to `RemoteProtocolError`; cap: outline `httpx/__init__.py` filtered to `RemoteProtocolError`.

**Call:** `symbols('httpx/_transports/default.py', 'RemoteProtocolError')`

**Response**: outcome `ok`

```
module httpx/_transports/default.py lines=407 dynamic=no all=static@69
39 from RemoteProtocolError <- .._exceptions RemoteProtocolError
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/__init__.py",
    "RemoteProtocolError"
   ],
   "desc": "outline `httpx/__init__.py` for its `RemoteProtocolError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_client.py",
    "RemoteProtocolError"
   ],
   "desc": "outline `httpx/_client.py` for its `RemoteProtocolError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_transports/__init__.py",
    "RemoteProtocolError"
   ],
   "desc": "outline `httpx/_transports/__init__.py` for its `RemoteProtocolError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_transports/default.py",
    "RemoteProtocolError"
   ],
   "desc": "outline `httpx/_transports/default.py` for its `RemoteProtocolError` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/__init__.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/__init__.py\", \"RemoteProtocolError\"]]",
   "v1": [
    48318163,
    7898150
   ],
   "v2": [
    24238063,
    3949075
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
     "RemoteProtocolError"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_client.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_client.py\", \"RemoteProtocolError\"]]",
   "v1": [
    48318163,
    7898150
   ],
   "v2": [
    24238063,
    3949075
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
     "RemoteProtocolError"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/__init__.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/__init__.py\", \"RemoteProtocolError\"]]",
   "v1": [
    48318163,
    7898150
   ],
   "v2": [
    24238063,
    3949075
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
     "RemoteProtocolError"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/default.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/default.py\", \"RemoteProtocolError\"]]",
   "v1": [
    48318163,
    7898150
   ],
   "v2": [
    24238063,
    3949075
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
     "RemoteProtocolError"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('httpx/_transports/default.py', 'RemoteProtocolError')",
  "key": "[\"symbols\", [\"httpx/_transports/default.py\", \"RemoteProtocolError\"]]",
  "provenance": "`httpx/_transports/default.py` had a matching line (step 1); its outline names every `RemoteProtocolError` import exactly",
  "v2": [
   24238063,
   3949075
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
  "ok": "[\"symbols\", [\"httpx/__init__.py\", \"RemoteProtocolError\"]]",
  "cap": "[\"symbols\", [\"httpx/__init__.py\", \"RemoteProtocolError\"]]"
 },
 "adherence": {
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 2,
   "path": "httpx/_transports/default.py",
   "filter": "RemoteProtocolError",
   "header": {
    "lines": 407,
    "dynamic": false,
    "all_status": "static",
    "all_line": 69
   },
   "bindings": [
    {
     "module": "httpx/_transports/default.py",
     "name": "RemoteProtocolError",
     "line": 39,
     "kind": "from",
     "src": ".._exceptions",
     "src_name": "RemoteProtocolError",
     "conditional": false,
     "col": 0
    }
   ],
   "complete": true
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
    "httpx/_transports/__init__.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "httpx/_transports/default.py",
    39,
    "pending",
    ""
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  }
 }
}
```
</details>

## Step 3

In `httpx/_transports/default.py`, `RemoteProtocolError` has exactly one binding: line 39 imports it as `RemoteProtocolError` from `.._exceptions`. No dynamic namespace tricks, a literal `__all__` at line 69.

Candidate modules so far: 4; statements confirmed: 0, ruled out: 0, modules with no such import: 0, pending: 4. import coverage complete; star coverage complete.

Outstanding: outline `httpx/__init__.py` for its `RemoteProtocolError` imports; outline `httpx/_client.py` for its `RemoteProtocolError` imports; outline `httpx/_transports/__init__.py` for its `RemoteProtocolError` imports; close the namespace of `httpx/_exceptions.py` for `RemoteProtocolError`.

Next: outline `httpx/__init__.py` filtered to `RemoteProtocolError`, because `httpx/__init__.py` had a matching line (step 1); its outline names every `RemoteProtocolError` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `httpx/_client.py` filtered to `RemoteProtocolError`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `httpx/_exceptions.py` filtered to `RemoteProtocolError`; cap: outline `httpx/_exceptions.py` filtered to `RemoteProtocolError`.

**Call:** `symbols('httpx/__init__.py', 'RemoteProtocolError')`

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
   "kind": "outline",
   "key": [
    "outline",
    "httpx/__init__.py",
    "RemoteProtocolError"
   ],
   "desc": "outline `httpx/__init__.py` for its `RemoteProtocolError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_client.py",
    "RemoteProtocolError"
   ],
   "desc": "outline `httpx/_client.py` for its `RemoteProtocolError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_transports/__init__.py",
    "RemoteProtocolError"
   ],
   "desc": "outline `httpx/_transports/__init__.py` for its `RemoteProtocolError` imports"
  },
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "httpx/_exceptions.py",
    "RemoteProtocolError"
   ],
   "desc": "close the namespace of `httpx/_exceptions.py` for `RemoteProtocolError`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/__init__.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/__init__.py\", \"RemoteProtocolError\"]]",
   "v1": [
    44477863,
    7898150
   ],
   "v2": [
    2459480024067,
    436740051475
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
     "RemoteProtocolError"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_client.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_client.py\", \"RemoteProtocolError\"]]",
   "v1": [
    44477863,
    7898150
   ],
   "v2": [
    2459480024067,
    436740051475
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
     "RemoteProtocolError"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_exceptions.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_exceptions.py\", \"RemoteProtocolError\"]]",
   "v1": [
    196059617843,
    34939204118
   ],
   "v2": [
    2459480024067,
    436740051475
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
     "bindings",
     "httpx/_exceptions.py",
     "RemoteProtocolError"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/__init__.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/__init__.py\", \"RemoteProtocolError\"]]",
   "v1": [
    44477863,
    7898150
   ],
   "v2": [
    2459480024067,
    436740051475
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
     "RemoteProtocolError"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_exceptions.py')",
   "key": "[\"symbols\", [\"httpx/_exceptions.py\"]]",
   "v1": [
    13854205497995,
    2410805084142
   ],
   "v2": [
    521096511994343,
    90405190655325
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
     "httpx/_exceptions.py",
     "RemoteProtocolError"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('httpx/__init__.py', 'RemoteProtocolError')",
  "key": "[\"symbols\", [\"httpx/__init__.py\", \"RemoteProtocolError\"]]",
  "provenance": "`httpx/__init__.py` had a matching line (step 1); its outline names every `RemoteProtocolError` import exactly",
  "v2": [
   2459480024067,
   436740051475
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
  "ok": "[\"symbols\", [\"httpx/_exceptions.py\", \"RemoteProtocolError\"]]",
  "cap": "[\"symbols\", [\"httpx/_exceptions.py\", \"RemoteProtocolError\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"httpx/__init__.py\", \"RemoteProtocolError\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 3,
   "path": "httpx/__init__.py",
   "filter": "RemoteProtocolError",
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
     "src": "._config",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/__init__.py",
     "name": "*",
     "line": 6,
     "kind": "star",
     "src": "._content",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/__init__.py",
     "name": "*",
     "line": 7,
     "kind": "star",
     "src": "._exceptions",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/__init__.py",
     "name": "*",
     "line": 8,
     "kind": "star",
     "src": "._models",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "httpx/__init__.py",
     "name": "*",
     "line": 9,
     "kind": "star",
     "src": "._status_codes",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "h
```
</details>

## Step 4

`httpx/__init__.py` binds no `RemoteProtocolError` at module level; 11 star import(s): `._api`, `._auth`, `._client`, `._config`, `._content`, `._exceptions`, `._models`, `._status_codes`, `._transports`, `._types`, `._urls`; a literal `__all__` at line 29; no dynamic namespace tricks. The call I had planned for this outcome is no longer useful, so I am re-planning.

Candidate modules so far: 4; statements confirmed: 0, ruled out: 0, modules with no such import: 0, pending: 14. import coverage complete; star coverage complete.

Outstanding: locate the module `._api` imported by `httpx/__init__.py`; locate the module `._auth` imported by `httpx/__init__.py`; know what `httpx/_client.py` exports; locate the module `._config` imported by `httpx/__init__.py`; and 10 more.

Next: grep `def`/`class RemoteProtocolError` statements under `.`, because a `def`/`class RemoteProtocolError` statement would reveal the module file; `RemoteProtocolError` task. I expect: hits under the cap (about 95%); a capped result (about 5%); no hits (about 5%). The alternative, list `httpx`, costs more in expectation. Plan by outcome: zero: list `httpx`; mid: outline `httpx/_exceptions.py` filtered to `RemoteProtocolError`; cap: list `httpx`.

**Call:** `grep('^\\s*(?:async\\s+)?(?:def|class)\\s+RemoteProtocolError\\b', '.')`

**Response**: outcome `mid`

```
httpx/_exceptions.py:232:class RemoteProtocolError(ProtocolError):
```

<details><summary>sidecar</summary>

```json
{
 "items": [
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
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._content"
   ],
   "desc": "locate the module `._content` imported by `httpx/__init__.py`"
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
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._models"
   ],
   "desc": "locate the module `._models` imported by `httpx/__init__.py`"
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
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._types"
   ],
   "desc": "locate the module `._types` imported by `httpx/__init__.py`"
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
    "RemoteProtocolError"
   ],
   "desc": "outline `httpx/_client.py` for its `RemoteProtocolError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_transports/__init__.py",
    "RemoteProtocolError"
   ],
   "desc": "outline `httpx/_transports/__init__.py` for its `RemoteProtocolError` imports"
  },
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "httpx/_exceptions.py",
    "RemoteProtocolError"
   ],
   "desc": "close the namespace of `httpx/_exceptions.py` for `RemoteProtocolError`"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+RemoteProtocolError\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+RemoteProtocolError\\\\b\", \".\"]]",
   "v1": [
    2693487,
    157963
   ],
   "v2": [
    1637891835173,
    104817612354
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
     "._content"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._models"
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
     "._types"
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
    16362461,
    947778
   ],
   "v2": [
    603494025223,
    38504429028
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
     "._content"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._models"
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
     "._types"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._urls"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_exceptions.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_exceptions.py\", \"RemoteProtocolError\"]]",
   "v1": [
    818650431667,
    34939204118
   ],
   "v2": [
    560823201279,
    34939204118
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
    ],
    [
     "bindings",
     "httpx/_exceptions.py",
     "RemoteProtocolError"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_client.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_client.py\", \"RemoteProtocolError\"]]",
   "v1": [
    92687513,
    3949075
   ],
   "v2": [
    63546063,
    3949075
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
     "RemoteProtocolError"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/__init__.py', 'RemoteProtocolError')",
   "key": "[\"symbols
```
</details>

## Step 5

The grep under `.` returned 1 lines, under the cap, so these are all of them: `httpx/_exceptions.py`.

Candidate modules so far: 4; statements confirmed: 0, ruled out: 0, modules with no such import: 0, pending: 14. import coverage complete; star coverage complete.

Still to settle: locate the module `._api` imported by `httpx/__init__.py`; locate the module `._auth` imported by `httpx/__init__.py`; know what `httpx/_client.py` exports; locate the module `._config` imported by `httpx/__init__.py`; and 10 more.

Next: outline `httpx/_exceptions.py` filtered to `RemoteProtocolError`, because module `httpx/_exceptions.py` (task). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, list `httpx`, is expected to open more follow-up work. Plan by outcome: def: list `httpx`; reexport: list `httpx`; star: list `httpx`; none: list `httpx`.

**Call:** `symbols('httpx/_exceptions.py', 'RemoteProtocolError')`

**Response**: outcome `def`

```
module httpx/_exceptions.py lines=378 dynamic=no all=static@42
232 class RemoteProtocolError
```

<details><summary>sidecar</summary>

```json
{
 "items": [
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
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._content"
   ],
   "desc": "locate the module `._content` imported by `httpx/__init__.py`"
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
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._models"
   ],
   "desc": "locate the module `._models` imported by `httpx/__init__.py`"
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
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._types"
   ],
   "desc": "locate the module `._types` imported by `httpx/__init__.py`"
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
    "RemoteProtocolError"
   ],
   "desc": "outline `httpx/_client.py` for its `RemoteProtocolError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_transports/__init__.py",
    "RemoteProtocolError"
   ],
   "desc": "outline `httpx/_transports/__init__.py` for its `RemoteProtocolError` imports"
  },
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "httpx/_exceptions.py",
    "RemoteProtocolError"
   ],
   "desc": "close the namespace of `httpx/_exceptions.py` for `RemoteProtocolError`"
  }
 ],
 "candidates": [
  {
   "call": "ls('httpx')",
   "key": "[\"ls\", [\"httpx\"]]",
   "v1": [
    16362461,
    947778
   ],
   "v2": [
    399806254541,
    24547450200
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
     "._content"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._models"
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
     "._types"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._urls"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_exceptions.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_exceptions.py\", \"RemoteProtocolError\"]]",
   "v1": [
    191909882547,
    8182483400
   ],
   "v2": [
    399806254541,
    24547450200
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
     "all",
     "httpx/_exceptions.py"
    ],
    [
     "bindings",
     "httpx/_exceptions.py",
     "RemoteProtocolError"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_client.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_client.py\", \"RemoteProtocolError\"]]",
   "v1": [
    92687513,
    3949075
   ],
   "v2": [
    386314853,
    23694450
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
     "RemoteProtocolError"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/__init__.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/__init__.py\", \"RemoteProtocolError\"]]",
   "v1": [
    193115213,
    7898150
   ],
   "v2": [
    204767707,
    11847225
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
     "RemoteProtocolError"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_exceptions.py')",
   "key": "[\"symbols\", [\"httpx/_exceptions.py\"]]",
   "v1": [
    59223776735993,
    2410805084142
   ],
   "v2": [
    6991056716607,
    401800847357
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
     "httpx/_exceptions.py",
     "RemoteProtocolError"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_api.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_api.py\", \"RemoteProtocolError\"]]",
   "v1": [
    7871245125634,
  
```
</details>

## Step 6

In `httpx/_exceptions.py`, `RemoteProtocolError` has exactly one binding: a class at line 232. No dynamic namespace tricks, a literal `__all__` at line 42.

Candidate modules so far: 4; statements confirmed: 1, ruled out: 0, modules with no such import: 0, pending: 13. import coverage complete; star coverage complete.

Open: locate the module `._api` imported by `httpx/__init__.py`; locate the module `._auth` imported by `httpx/__init__.py`; know what `httpx/_client.py` exports; locate the module `._config` imported by `httpx/__init__.py`; and 9 more.

Next: list `httpx`, because `._api` imported by `httpx/__init__.py` should live under `httpx`. I expect: a complete listing settles which files exist (about 90%); a capped listing settles nothing (about 10%). The alternative, outline `httpx/_client.py` filtered to `RemoteProtocolError`, serves fewer of the open items. Plan by outcome: complete: outline `httpx/_client.py` filtered to `RemoteProtocolError`; cap: outline `httpx/_client.py` filtered to `RemoteProtocolError`.

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
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._content"
   ],
   "desc": "locate the module `._content` imported by `httpx/__init__.py`"
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
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._models"
   ],
   "desc": "locate the module `._models` imported by `httpx/__init__.py`"
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
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/__init__.py",
    "._types"
   ],
   "desc": "locate the module `._types` imported by `httpx/__init__.py`"
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
    "RemoteProtocolError"
   ],
   "desc": "outline `httpx/_client.py` for its `RemoteProtocolError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_transports/__init__.py",
    "RemoteProtocolError"
   ],
   "desc": "outline `httpx/_transports/__init__.py` for its `RemoteProtocolError` imports"
  }
 ],
 "candidates": [
  {
   "call": "ls('httpx')",
   "key": "[\"ls\", [\"httpx\"]]",
   "v1": [
    15378491,
    947778
   ],
   "v2": [
    361715603,
    23694450
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
     "._content"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._models"
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
     "._types"
    ],
    [
     "module_path",
     "httpx/__init__.py",
     "._urls"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_client.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_client.py\", \"RemoteProtocolError\"]]",
   "v1": [
    88587638,
    3949075
   ],
   "v2": [
    361715603,
    23694450
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
     "RemoteProtocolError"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/__init__.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/__init__.py\", \"RemoteProtocolError\"]]",
   "v1": [
    184915463,
    7898150
   ],
   "v2": [
    192468082,
    11847225
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
     "RemoteProtocolError"
    ]
   ]
  },
  {
   "call": "read('httpx/_exceptions.py', 42, 30)",
   "key": "[\"read\", [\"httpx/_exceptions.py\", 42, 30]]",
   "v1": [
    18633713,
    789815
   ],
   "v2": [
    77840233,
    4738890
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
   "call": "symbols('httpx/_api.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_api.py\", \"RemoteProtocolError\"]]",
   "v1": [
    7526647843969,
    331922439121
   ],
   "v2": [
    306437173154843,
    17923811712534
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
     "httpx/__init__.py",
     "._api"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_auth.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_auth.py\", \"RemoteProtocolError\"]]",
   "v1": [
    7526647843969,
    331922439121
   ],
   "v2": [
    306437173154843,
    17923811712534
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
     "httpx/__init
```
</details>

## Step 7

`httpx` lists 18 entries (complete): `__init__.py`, `__version__.py`, `_api.py`, `_auth.py`, `_client.py`, `_config.py` and 12 more.

Candidate modules so far: 4; statements confirmed: 1, ruled out: 0, modules with no such import: 0, pending: 13. import coverage complete; star coverage complete.

Open: know what `httpx/_api.py` exports; know what `httpx/_auth.py` exports; know what `httpx/_client.py` exports; know what `httpx/_config.py` exports; and 9 more.

Next: outline `httpx/_client.py` filtered to `RemoteProtocolError`, because module `httpx/_client.py` (step 1). I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `httpx/_transports/__init__.py` filtered to `RemoteProtocolError`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `httpx/_transports/__init__.py` filtered to `RemoteProtocolError`; cap: outline `httpx/_transports/__init__.py` filtered to `RemoteProtocolError`.

**Call:** `symbols('httpx/_client.py', 'RemoteProtocolError')`

**Response**: outcome `reexport`

```
module httpx/_client.py lines=2020 dynamic=no all=static@54
23 from RemoteProtocolError <- ._exceptions RemoteProtocolError
```

<details><summary>sidecar</summary>

```json
{
 "items": [
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
    "httpx/_client.py",
    "RemoteProtocolError"
   ],
   "desc": "outline `httpx/_client.py` for its `RemoteProtocolError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_transports/__init__.py",
    "RemoteProtocolError"
   ],
   "desc": "outline `httpx/_transports/__init__.py` for its `RemoteProtocolError` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/_client.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_client.py\", \"RemoteProtocolError\"]]",
   "v1": [
    51688763,
    3949075
   ],
   "v2": [
    47897651,
    3949075
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
     "RemoteProtocolError"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/__init__.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/__init__.py\", \"RemoteProtocolError\"]]",
   "v1": [
    51688763,
    3949075
   ],
   "v2": [
    47897651,
    3949075
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
     "RemoteProtocolError"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_api.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_api.py\", \"RemoteProtocolError\"]]",
   "v1": [
    492189849037,
    34939204118
   ],
   "v2": [
    11466205327093,
    873480102950
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
   "call": "symbols('httpx/_auth.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_auth.py\", \"RemoteProtocolError\"]]",
   "v1": [
    492189849037,
    34939204118
   ],
   "v2": [
    11466205327093,
    873480102950
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
   "call": "symbols('httpx/_config.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_config.py\", \"RemoteProtocolError\"]]",
   "v1": [
    492189849037,
    34939204118
   ],
   "v2": [
    11466205327093,
    873480102950
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
   "call": "symbols('httpx/_content.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_content.py\", \"RemoteProtocolError\"]]",
   "v1": [
    492189849037,
    34939204118
   ],
   "v2": [
    11466205327093,
    873480102950
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
     "httpx/_content.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_models.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_models.py\", \"RemoteProtocolError\"]]",
   "v1": [
    492189849037,
    34939204118
   ],
   "v2": [
    11466205327093,
    873480102950
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
     "httpx/_models.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_status_codes.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_status_codes.py\", \"RemoteProtocolError\"]]",
   "v1": [
    492189849037,
    34939204118
   ],
   "v2": [
    11466205327093,
    873480102950
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
    "reexport
```
</details>

## Step 8

In `httpx/_client.py`, `RemoteProtocolError` has exactly one binding: line 23 imports it as `RemoteProtocolError` from `._exceptions`. No dynamic namespace tricks, a literal `__all__` at line 54. That outcome was not one I had forecast, so there was no branch for it; re-planning from the open items.

Candidate modules so far: 4; statements confirmed: 2, ruled out: 0, modules with no such import: 0, pending: 12. import coverage complete; star coverage complete.

Outstanding: know what `httpx/_api.py` exports; know what `httpx/_auth.py` exports; know what `httpx/_client.py` exports; know what `httpx/_config.py` exports; and 8 more.

Next: outline `httpx/_status_codes.py` filtered to `RemoteProtocolError`, because module `httpx/_status_codes.py` (step 6). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `httpx/_api.py` filtered to `RemoteProtocolError`, scores the same; the seed broke the tie. Plan by outcome: def: outline `httpx/_transports/__init__.py` filtered to `RemoteProtocolError`; reexport: outline `httpx/_transports/__init__.py` filtered to `RemoteProtocolError`; star: outline `httpx/_transports/__init__.py` filtered to `RemoteProtocolError`; none: outline `httpx/_transports/__init__.py` filtered to `RemoteProtocolError`.

**Call:** `symbols('httpx/_status_codes.py', 'RemoteProtocolError')`

**Response**: outcome `none`

```
module httpx/_status_codes.py lines=163 dynamic=no all=static@5
```

<details><summary>sidecar</summary>

```json
{
 "items": [
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
    "RemoteProtocolError"
   ],
   "desc": "outline `httpx/_transports/__init__.py` for its `RemoteProtocolError` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/_api.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_api.py\", \"RemoteProtocolError\"]]",
   "v1": [
    438928039051,
    34939204118
   ],
   "v2": [
    10134660077443,
    873480102950
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
   "call": "symbols('httpx/_auth.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_auth.py\", \"RemoteProtocolError\"]]",
   "v1": [
    438928039051,
    34939204118
   ],
   "v2": [
    10134660077443,
    873480102950
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
   "call": "symbols('httpx/_config.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_config.py\", \"RemoteProtocolError\"]]",
   "v1": [
    438928039051,
    34939204118
   ],
   "v2": [
    10134660077443,
    873480102950
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
   "call": "symbols('httpx/_content.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_content.py\", \"RemoteProtocolError\"]]",
   "v1": [
    438928039051,
    34939204118
   ],
   "v2": [
    10134660077443,
    873480102950
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
     "httpx/_content.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_models.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_models.py\", \"RemoteProtocolError\"]]",
   "v1": [
    438928039051,
    34939204118
   ],
   "v2": [
    10134660077443,
    873480102950
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
     "httpx/_models.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_status_codes.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_status_codes.py\", \"RemoteProtocolError\"]]",
   "v1": [
    438928039051,
    34939204118
   ],
   "v2": [
    10134660077443,
    873480102950
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
   "call": "symbols('httpx/_transports/__init__.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/__init__.py\", \"RemoteProtocolError\"]]",
   "v1": [
    45668738,
    3949075
   ],
   "v2": [
    10134660077443,
    873480102950
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
     "RemoteProtocolError"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_types.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_types.py\", \"RemoteProtocolError\"]]",
   "v1": [
    438928039051,
    34939204118
   ],
   "v2": [
    10134660077443,
    873480102950
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
     "httpx/
```
</details>

## Step 9

`httpx/_status_codes.py` binds no `RemoteProtocolError` at module level; no star imports; a literal `__all__` at line 5; no dynamic namespace tricks.

Candidate modules so far: 4; statements confirmed: 2, ruled out: 0, modules with no such import: 0, pending: 12. import coverage complete; star coverage complete.

Still to settle: know what `httpx/_api.py` exports; know what `httpx/_auth.py` exports; know what `httpx/_client.py` exports; know what `httpx/_config.py` exports; and 8 more.

Next: outline `httpx/_transports/__init__.py` filtered to `RemoteProtocolError`, because module `httpx/_transports/__init__.py` (step 1). I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `httpx/_api.py` filtered to `RemoteProtocolError`, serves fewer of the open items. Plan by outcome: ok: outline `httpx/_api.py` filtered to `RemoteProtocolError`; cap: outline `httpx/_api.py` filtered to `RemoteProtocolError`.

**Call:** `symbols('httpx/_transports/__init__.py', 'RemoteProtocolError')`

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
    "RemoteProtocolError"
   ],
   "desc": "outline `httpx/_transports/__init__.py` for its `RemoteProtocolError` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/_api.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_api.py\", \"RemoteProtocolError\"]]",
   "v1": [
    438928039051,
    34939204118
   ],
   "v2": [
    10134660077443,
    873480102950
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
   "call": "symbols('httpx/_auth.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_auth.py\", \"RemoteProtocolError\"]]",
   "v1": [
    438928039051,
    34939204118
   ],
   "v2": [
    10134660077443,
    873480102950
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
   "call": "symbols('httpx/_config.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_config.py\", \"RemoteProtocolError\"]]",
   "v1": [
    438928039051,
    34939204118
   ],
   "v2": [
    10134660077443,
    873480102950
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
   "call": "symbols('httpx/_content.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_content.py\", \"RemoteProtocolError\"]]",
   "v1": [
    438928039051,
    34939204118
   ],
   "v2": [
    10134660077443,
    873480102950
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
     "httpx/_content.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_models.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_models.py\", \"RemoteProtocolError\"]]",
   "v1": [
    438928039051,
    34939204118
   ],
   "v2": [
    10134660077443,
    873480102950
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
     "httpx/_models.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/__init__.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/__init__.py\", \"RemoteProtocolError\"]]",
   "v1": [
    45668738,
    3949075
   ],
   "v2": [
    10134660077443,
    873480102950
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
     "RemoteProtocolError"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_types.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_types.py\", \"RemoteProtocolError\"]]",
   "v1": [
    438928039051,
    34939204118
   ],
   "v2": [
    10134660077443,
    873480102950
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
     "httpx/_types.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_urls.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_urls.py\", \"RemoteProtocolError\"]]",
   "v1": [
    438928039051,
    34939204118
   ],
   "v2": [
    10134660077443,
    873480102950
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
  
```
</details>

## Step 10

`httpx/_transports/__init__.py` binds no `RemoteProtocolError` at module level; 5 star import(s): `.asgi`, `.base`, `.default`, `.mock`, `.wsgi`; a literal `__all__` at line 7; no dynamic namespace tricks. That outcome was not one I had forecast, so there was no branch for it; re-planning from the open items.

Candidate modules so far: 4; statements confirmed: 2, ruled out: 0, modules with no such import: 0, pending: 16. import coverage complete; star coverage complete.

Still to settle: know what `httpx/_api.py` exports; know what `httpx/_auth.py` exports; know what `httpx/_client.py` exports; know what `httpx/_config.py` exports; and 12 more.

Next: list `httpx/_transports`, because `.asgi` imported by `httpx/_transports/__init__.py` should live under `httpx/_transports`. I expect: a complete listing settles which files exist (near certain); a capped listing settles nothing (under 5%). The alternative, outline `httpx/_api.py` filtered to `RemoteProtocolError`, serves fewer of the open items. Plan by outcome: complete: outline `httpx/_api.py` filtered to `RemoteProtocolError`; cap: outline `httpx/_transports/asgi.py` filtered to `RemoteProtocolError`.

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
   "kind": "module_path",
   "key": [
    "module_path",
    "httpx/_transports/__init__.py",
    ".asgi"
   ],
   "desc": "locate the module `.asgi` imported by `httpx/_transports/__init__.py`"
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
   "kind": "all",
   "key": [
    "all",
    "httpx/_transports/default.py"
   ],
   "desc": "know what `httpx/_transports/default.py` exports"
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
    1567959,
    90923
   ],
   "v2": [
    6126115777238,
    354813641819
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
     ".asgi"
    ],
    [
     "module_path",
     "httpx/_transports/__init__.py",
     ".base"
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
   "call": "symbols('httpx/_api.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_api.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1871235655,
    92676934
   ],
   "v2": [
    49654141683,
    2872984954
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
   "call": "symbols('httpx/_auth.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_auth.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1871235655,
    92676934
   ],
   "v2": [
    49654141683,
    2872984954
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
   "call": "symbols('httpx/_config.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_config.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1871235655,
    92676934
   ],
   "v2": [
    49654141683,
    2872984954
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
   "call": "symbols('httpx/_content.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_content.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1871235655,
    92676934
   ],
   "v2": [
    49654141683,
    2872984954
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
     "httpx/_content.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_models.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_models.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1871235655,
    92676934
   ],
   "v2": [
    49654141683,
    2872984954
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
     "httpx/_models.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_types.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_types.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1871235655,
    92676934
   ],
   "v2": [
    49654141683,
    2872984954
   ],
   "p_cap": [
 
```
</details>

## Step 11

`httpx/_transports` lists 6 entries (complete): `__init__.py`, `asgi.py`, `base.py`, `default.py`, `mock.py`, `wsgi.py`.

Candidate modules so far: 4; statements confirmed: 2, ruled out: 0, modules with no such import: 0, pending: 16. import coverage complete; star coverage complete.

Outstanding: know what `httpx/_api.py` exports; know what `httpx/_auth.py` exports; know what `httpx/_client.py` exports; know what `httpx/_config.py` exports; and 12 more.

Next: outline `httpx/_api.py` filtered to `RemoteProtocolError`, because module `httpx/_api.py` (step 6). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `httpx/_auth.py` filtered to `RemoteProtocolError`, scores the same; the seed broke the tie. Plan by outcome: def: outline `httpx/_auth.py` filtered to `RemoteProtocolError`; reexport: outline `httpx/_auth.py` filtered to `RemoteProtocolError`; star: outline `httpx/_auth.py` filtered to `RemoteProtocolError`; none: outline `httpx/_auth.py` filtered to `RemoteProtocolError`.

**Call:** `symbols('httpx/_api.py', 'RemoteProtocolError')`

**Response**: outcome `none`

```
module httpx/_api.py lines=439 dynamic=no all=static@26
```

<details><summary>sidecar</summary>

```json
{
 "items": [
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
   "call": "symbols('httpx/_api.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_api.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
   "call": "symbols('httpx/_auth.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_auth.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
   "call": "symbols('httpx/_config.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_config.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
   "call": "symbols('httpx/_content.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_content.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
     "httpx/_content.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_models.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_models.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
     "httpx/_models.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/asgi.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/asgi.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
     "httpx/_transports/asgi.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/base.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/base.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
   "call": "symbols('httpx/_transports/mock.py', 'RemoteProtocolError')",
   "key
```
</details>

## Step 12

`httpx/_api.py` binds no `RemoteProtocolError` at module level; no star imports; a literal `__all__` at line 26; no dynamic namespace tricks.

Candidate modules so far: 4; statements confirmed: 2, ruled out: 0, modules with no such import: 0, pending: 16. import coverage complete; star coverage complete.

Open: know what `httpx/_api.py` exports; know what `httpx/_auth.py` exports; know what `httpx/_client.py` exports; know what `httpx/_config.py` exports; and 12 more.

Next: outline `httpx/_auth.py` filtered to `RemoteProtocolError`, because module `httpx/_auth.py` (step 6). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `httpx/_config.py` filtered to `RemoteProtocolError`, scores the same; the seed broke the tie. Plan by outcome: def: outline `httpx/_config.py` filtered to `RemoteProtocolError`; reexport: outline `httpx/_config.py` filtered to `RemoteProtocolError`; star: outline `httpx/_config.py` filtered to `RemoteProtocolError`; none: outline `httpx/_config.py` filtered to `RemoteProtocolError`.

**Call:** `symbols('httpx/_auth.py', 'RemoteProtocolError')`

**Response**: outcome `none`

```
module httpx/_auth.py lines=349 dynamic=no all=static@19
```

<details><summary>sidecar</summary>

```json
{
 "items": [
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
   "call": "symbols('httpx/_auth.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_auth.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
   "call": "symbols('httpx/_config.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_config.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
   "call": "symbols('httpx/_content.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_content.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
     "httpx/_content.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_models.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_models.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
     "httpx/_models.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/asgi.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/asgi.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
     "httpx/_transports/asgi.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/base.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/base.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
   "call": "symbols('httpx/_transports/mock.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/mock.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
   "call": "symbols('httpx/_transports/wsgi.p
```
</details>

## Step 13

`httpx/_auth.py` binds no `RemoteProtocolError` at module level; no star imports; a literal `__all__` at line 19; no dynamic namespace tricks.

Candidate modules so far: 4; statements confirmed: 2, ruled out: 0, modules with no such import: 0, pending: 16. import coverage complete; star coverage complete.

Outstanding: know what `httpx/_api.py` exports; know what `httpx/_auth.py` exports; know what `httpx/_client.py` exports; know what `httpx/_config.py` exports; and 12 more.

Next: outline `httpx/_config.py` filtered to `RemoteProtocolError`, because module `httpx/_config.py` (step 6). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `httpx/_content.py` filtered to `RemoteProtocolError`, scores the same; the seed broke the tie. Plan by outcome: def: outline `httpx/_content.py` filtered to `RemoteProtocolError`; reexport: outline `httpx/_content.py` filtered to `RemoteProtocolError`; star: outline `httpx/_content.py` filtered to `RemoteProtocolError`; none: outline `httpx/_content.py` filtered to `RemoteProtocolError`.

**Call:** `symbols('httpx/_config.py', 'RemoteProtocolError')`

**Response**: outcome `none`

```
module httpx/_config.py lines=249 dynamic=no all=static@13
```

<details><summary>sidecar</summary>

```json
{
 "items": [
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
   "call": "symbols('httpx/_config.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_config.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
   "call": "symbols('httpx/_content.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_content.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
     "httpx/_content.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_models.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_models.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
     "httpx/_models.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/asgi.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/asgi.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
     "httpx/_transports/asgi.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/base.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/base.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
   "call": "symbols('httpx/_transports/mock.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/mock.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
   "call": "symbols('httpx/_transports/wsgi.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/wsgi.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
   "call": "
```
</details>

## Step 14

`httpx/_config.py` binds no `RemoteProtocolError` at module level; no star imports; a literal `__all__` at line 13; no dynamic namespace tricks.

Candidate modules so far: 4; statements confirmed: 2, ruled out: 0, modules with no such import: 0, pending: 16. import coverage complete; star coverage complete.

Open: know what `httpx/_api.py` exports; know what `httpx/_auth.py` exports; know what `httpx/_client.py` exports; know what `httpx/_config.py` exports; and 12 more.

Next: outline `httpx/_content.py` filtered to `RemoteProtocolError`, because module `httpx/_content.py` (step 6). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `httpx/_models.py` filtered to `RemoteProtocolError`, scores the same; the seed broke the tie. Plan by outcome: def: outline `httpx/_models.py` filtered to `RemoteProtocolError`; reexport: outline `httpx/_models.py` filtered to `RemoteProtocolError`; star: outline `httpx/_models.py` filtered to `RemoteProtocolError`; none: outline `httpx/_models.py` filtered to `RemoteProtocolError`.

**Call:** `symbols('httpx/_content.py', 'RemoteProtocolError')`

**Response**: outcome `none`

```
module httpx/_content.py lines=241 dynamic=no all=static@28
```

<details><summary>sidecar</summary>

```json
{
 "items": [
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
   "call": "symbols('httpx/_content.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_content.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
     "httpx/_content.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_models.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_models.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
     "httpx/_models.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/asgi.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/asgi.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
     "httpx/_transports/asgi.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/base.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/base.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
   "call": "symbols('httpx/_transports/mock.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/mock.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
   "call": "symbols('httpx/_transports/wsgi.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/wsgi.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
   "call": "symbols('httpx/_types.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_types.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
     "httpx/_types.py"
    ]
   ]
  },
  {
   "call": "sym
```
</details>

## Step 15

`httpx/_content.py` binds no `RemoteProtocolError` at module level; no star imports; a literal `__all__` at line 28; no dynamic namespace tricks.

Candidate modules so far: 4; statements confirmed: 2, ruled out: 0, modules with no such import: 0, pending: 16. import coverage complete; star coverage complete.

Still to settle: know what `httpx/_api.py` exports; know what `httpx/_auth.py` exports; know what `httpx/_client.py` exports; know what `httpx/_config.py` exports; and 12 more.

Next: outline `httpx/_models.py` filtered to `RemoteProtocolError`, because module `httpx/_models.py` (step 6). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `httpx/_transports/asgi.py` filtered to `RemoteProtocolError`, scores the same; the seed broke the tie. Plan by outcome: def: outline `httpx/_transports/asgi.py` filtered to `RemoteProtocolError`; reexport: outline `httpx/_transports/asgi.py` filtered to `RemoteProtocolError`; star: outline `httpx/_transports/asgi.py` filtered to `RemoteProtocolError`; none: outline `httpx/_transports/asgi.py` filtered to `RemoteProtocolError`.

**Call:** `symbols('httpx/_models.py', 'RemoteProtocolError')`

**Response**: outcome `none`

```
module httpx/_models.py lines=1278 dynamic=no all=static@51
```

<details><summary>sidecar</summary>

```json
{
 "items": [
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
   "call": "symbols('httpx/_models.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_models.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
     "httpx/_models.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/asgi.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/asgi.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
     "httpx/_transports/asgi.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/base.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/base.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
   "call": "symbols('httpx/_transports/mock.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/mock.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
   "call": "symbols('httpx/_transports/wsgi.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/wsgi.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
   "call": "symbols('httpx/_types.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_types.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
     "httpx/_types.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_urls.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_urls.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
   "call": "read('httpx/
```
</details>

## Step 16

`httpx/_models.py` binds no `RemoteProtocolError` at module level; no star imports; a literal `__all__` at line 51; no dynamic namespace tricks.

Candidate modules so far: 4; statements confirmed: 2, ruled out: 0, modules with no such import: 0, pending: 16. import coverage complete; star coverage complete.

Outstanding: know what `httpx/_api.py` exports; know what `httpx/_auth.py` exports; know what `httpx/_client.py` exports; know what `httpx/_config.py` exports; and 12 more.

Next: outline `httpx/_transports/asgi.py` filtered to `RemoteProtocolError`, because module `httpx/_transports/asgi.py` (step 10). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `httpx/_transports/base.py` filtered to `RemoteProtocolError`, scores the same; the seed broke the tie. Plan by outcome: def: outline `httpx/_transports/base.py` filtered to `RemoteProtocolError`; reexport: outline `httpx/_transports/base.py` filtered to `RemoteProtocolError`; star: outline `httpx/_transports/base.py` filtered to `RemoteProtocolError`; none: outline `httpx/_transports/base.py` filtered to `RemoteProtocolError`.

**Call:** `symbols('httpx/_transports/asgi.py', 'RemoteProtocolError')`

**Response**: outcome `none`

```
module httpx/_transports/asgi.py lines=188 dynamic=no all=static@26
```

<details><summary>sidecar</summary>

```json
{
 "items": [
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
   "call": "symbols('httpx/_transports/asgi.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/asgi.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
     "httpx/_transports/asgi.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_transports/base.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/base.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
   "call": "symbols('httpx/_transports/mock.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/mock.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
   "call": "symbols('httpx/_transports/wsgi.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/wsgi.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
   "call": "symbols('httpx/_types.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_types.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
     "httpx/_types.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_urls.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_urls.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
    81,
    5
   ],
   "v2": [
    7524537009,
    463384670
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
    81,
    5
   ],
   "v2": [
    7524537009,
    46338467
```
</details>

## Step 17

`httpx/_transports/asgi.py` binds no `RemoteProtocolError` at module level; no star imports; a literal `__all__` at line 26; no dynamic namespace tricks.

Candidate modules so far: 4; statements confirmed: 2, ruled out: 0, modules with no such import: 0, pending: 16. import coverage complete; star coverage complete.

Still to settle: know what `httpx/_api.py` exports; know what `httpx/_auth.py` exports; know what `httpx/_client.py` exports; know what `httpx/_config.py` exports; and 12 more.

Next: outline `httpx/_transports/base.py` filtered to `RemoteProtocolError`, because module `httpx/_transports/base.py` (step 10). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `httpx/_transports/mock.py` filtered to `RemoteProtocolError`, scores the same; the seed broke the tie. Plan by outcome: def: outline `httpx/_transports/mock.py` filtered to `RemoteProtocolError`; reexport: outline `httpx/_transports/mock.py` filtered to `RemoteProtocolError`; star: outline `httpx/_transports/mock.py` filtered to `RemoteProtocolError`; none: outline `httpx/_transports/mock.py` filtered to `RemoteProtocolError`.

**Call:** `symbols('httpx/_transports/base.py', 'RemoteProtocolError')`

**Response**: outcome `none`

```
module httpx/_transports/base.py lines=87 dynamic=no all=static@11
```

<details><summary>sidecar</summary>

```json
{
 "items": [
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
   "call": "symbols('httpx/_transports/base.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/base.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
   "call": "symbols('httpx/_transports/mock.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/mock.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
   "call": "symbols('httpx/_transports/wsgi.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/wsgi.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
   "call": "symbols('httpx/_types.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_types.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
     "httpx/_types.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_urls.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_urls.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
    81,
    5
   ],
   "v2": [
    7524537009,
    463384670
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
    81,
    5
   ],
   "v2": [
    7524537009,
    463384670
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
    81,
    5
   ],
   "v2": [
    7524537009,
    463384670
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
     "all
```
</details>

## Step 18

`httpx/_transports/base.py` binds no `RemoteProtocolError` at module level; no star imports; a literal `__all__` at line 11; no dynamic namespace tricks.

Candidate modules so far: 4; statements confirmed: 2, ruled out: 0, modules with no such import: 0, pending: 16. import coverage complete; star coverage complete.

Open: know what `httpx/_api.py` exports; know what `httpx/_auth.py` exports; know what `httpx/_client.py` exports; know what `httpx/_config.py` exports; and 12 more.

Next: outline `httpx/_transports/mock.py` filtered to `RemoteProtocolError`, because module `httpx/_transports/mock.py` (step 10). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `httpx/_transports/wsgi.py` filtered to `RemoteProtocolError`, scores the same; the seed broke the tie. Plan by outcome: def: outline `httpx/_transports/wsgi.py` filtered to `RemoteProtocolError`; reexport: outline `httpx/_transports/wsgi.py` filtered to `RemoteProtocolError`; star: outline `httpx/_transports/wsgi.py` filtered to `RemoteProtocolError`; none: outline `httpx/_transports/wsgi.py` filtered to `RemoteProtocolError`.

**Call:** `symbols('httpx/_transports/mock.py', 'RemoteProtocolError')`

**Response**: outcome `none`

```
module httpx/_transports/mock.py lines=44 dynamic=no all=static@12
```

<details><summary>sidecar</summary>

```json
{
 "items": [
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
   "call": "symbols('httpx/_transports/mock.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/mock.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
   "call": "symbols('httpx/_transports/wsgi.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/wsgi.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
   "call": "symbols('httpx/_types.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_types.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
     "httpx/_types.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_urls.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_urls.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
    81,
    5
   ],
   "v2": [
    7524537009,
    463384670
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
    81,
    5
   ],
   "v2": [
    7524537009,
    463384670
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
    81,
    5
   ],
   "v2": [
    7524537009,
    463384670
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
    81,
    5
   ],
   "v2": [
    7524537009,
    463384670
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

```
</details>

## Step 19

`httpx/_transports/mock.py` binds no `RemoteProtocolError` at module level; no star imports; a literal `__all__` at line 12; no dynamic namespace tricks.

Candidate modules so far: 4; statements confirmed: 2, ruled out: 0, modules with no such import: 0, pending: 16. import coverage complete; star coverage complete.

Outstanding: know what `httpx/_api.py` exports; know what `httpx/_auth.py` exports; know what `httpx/_client.py` exports; know what `httpx/_config.py` exports; and 12 more.

Next: outline `httpx/_transports/wsgi.py` filtered to `RemoteProtocolError`, because module `httpx/_transports/wsgi.py` (step 10). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `httpx/_types.py` filtered to `RemoteProtocolError`, scores the same; the seed broke the tie. Plan by outcome: def: outline `httpx/_types.py` filtered to `RemoteProtocolError`; reexport: outline `httpx/_types.py` filtered to `RemoteProtocolError`; star: outline `httpx/_types.py` filtered to `RemoteProtocolError`; none: outline `httpx/_types.py` filtered to `RemoteProtocolError`.

**Call:** `symbols('httpx/_transports/wsgi.py', 'RemoteProtocolError')`

**Response**: outcome `none`

```
module httpx/_transports/wsgi.py lines=150 dynamic=no all=static@19
```

<details><summary>sidecar</summary>

```json
{
 "items": [
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
   "call": "symbols('httpx/_transports/wsgi.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_transports/wsgi.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
   "call": "symbols('httpx/_types.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_types.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
     "httpx/_types.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_urls.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_urls.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
    81,
    5
   ],
   "v2": [
    7524537009,
    463384670
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
    81,
    5
   ],
   "v2": [
    7524537009,
    463384670
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
    81,
    5
   ],
   "v2": [
    7524537009,
    463384670
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
    81,
    5
   ],
   "v2": [
    7524537009,
    463384670
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
    81,
    5
   ],
   "v2": [
    7524537009,
    463384670
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
    81,
    5
   ],
   "v2": [
    7524537009,
    463384670
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
 
```
</details>

## Step 20

`httpx/_transports/wsgi.py` binds no `RemoteProtocolError` at module level; no star imports; a literal `__all__` at line 19; no dynamic namespace tricks.

Candidate modules so far: 4; statements confirmed: 2, ruled out: 0, modules with no such import: 0, pending: 16. import coverage complete; star coverage complete.

Open: know what `httpx/_api.py` exports; know what `httpx/_auth.py` exports; know what `httpx/_client.py` exports; know what `httpx/_config.py` exports; and 12 more.

Next: outline `httpx/_types.py` filtered to `RemoteProtocolError`, because module `httpx/_types.py` (step 6). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `httpx/_urls.py` filtered to `RemoteProtocolError`, scores the same; the seed broke the tie. Plan by outcome: def: outline `httpx/_urls.py` filtered to `RemoteProtocolError`; reexport: outline `httpx/_urls.py` filtered to `RemoteProtocolError`; star: outline `httpx/_urls.py` filtered to `RemoteProtocolError`; none: outline `httpx/_urls.py` filtered to `RemoteProtocolError`.

**Call:** `symbols('httpx/_types.py', 'RemoteProtocolError')`

**Response**: outcome `none`

```
module httpx/_types.py lines=115 dynamic=no all=static@89
```

<details><summary>sidecar</summary>

```json
{
 "items": [
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
   "call": "symbols('httpx/_types.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_types.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
     "httpx/_types.py"
    ]
   ]
  },
  {
   "call": "symbols('httpx/_urls.py', 'RemoteProtocolError')",
   "key": "[\"symbols\", [\"httpx/_urls.py\", \"RemoteProtocolError\"]]",
   "v1": [
    1486372015,
    92676934
   ],
   "v2": [
    744956543,
    46338467
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
    81,
    5
   ],
   "v2": [
    7524537009,
    463384670
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
    81,
    5
   ],
   "v2": [
    7524537009,
    463384670
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
    81,
    5
   ],
   "v2": [
    7524537009,
    463384670
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
    81,
    5
   ],
   "v2": [
    7524537009,
    463384670
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
    81,
    5
   ],
   "v2": [
    7524537009,
    463384670
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
    81,
    5
   ],
   "v2": [
    7524537009,
    463384670
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
    81,
    5
   ],
   "v2": [
    7524537009,
    463384670
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
   "call": "read('httpx/_status_codes.py',
```
</details>

## Step 21

`httpx/_types.py` binds no `RemoteProtocolError` at module level; no star imports; a literal `__all__` at line 89; no dynamic namespace tricks.

Candidate modules so far: 4; statements confirmed: 2, ruled out: 0, modules with no such import: 0, pending: 16. import coverage complete; star coverage complete.

Still to settle: know what `httpx/_api.py` exports; know what `httpx/_auth.py` exports; know what `httpx/_client.py` exports; know what `httpx/_config.py` exports; and 12 more.

Next: outline `httpx/_urls.py` filtered to `RemoteProtocolError`, because module `httpx/_urls.py` (step 6). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, read `httpx/_api.py` from line 26, scores the same; the seed broke the tie. Plan by outcome: def: read `httpx/_api.py` from line 26; reexport: read `httpx/_api.py` from line 26; star: read `httpx/_api.py` from line 26; none: read `httpx/_api.py` from line 26.

**Call:** `symbols('httpx/_urls.py', 'RemoteProtocolError')`

**Response**: outcome `none`

```
module httpx/_urls.py lines=642 dynamic=no all=static@12
```

<details><summary>sidecar</summary>

```json
{
 "items": [
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
    81,
    5
   ],
   "v2": [
    7524537009,
    463384670
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
    81,
    5
   ],
   "v2": [
    7524537009,
    463384670
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
    81,
    5
   ],
   "v2": [
    7524537009,
    463384670
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
    81,
    5
   ],
   "v2": [
    7524537009,
    463384670
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
    81,
    5
   ],
   "v2": [
    7524537009,
    463384670
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
    81,
    5
   ],
   "v2": [
    7524537009,
    463384670
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
    81,
    5
   ],
   "v2": [
    7524537009,
    463384670
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
    81,
    5
   ],
   "v2": [
    7524537009,
    463384670
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
    81,
    5
   ],
   "v2": [
    7524537009,
    463384670
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
    81,
    5
   ],
   "v2": [
    7524537009,
    463384670
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
   
```
</details>

## Step 22

`httpx/_urls.py` binds no `RemoteProtocolError` at module level; no star imports; a literal `__all__` at line 12; no dynamic namespace tricks.

Candidate modules so far: 4; statements confirmed: 2, ruled out: 0, modules with no such import: 0, pending: 16. import coverage complete; star coverage complete.

Open: know what `httpx/_api.py` exports; know what `httpx/_auth.py` exports; know what `httpx/_client.py` exports; know what `httpx/_config.py` exports; and 12 more.

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
    81,
    5
   ],
   "v2": [
    82,
    5
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
    81,
    5
   ],
   "v2": [
    82,
    5
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
    81,
    5
   ],
   "v2": [
    82,
    5
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
    81,
    5
   ],
   "v2": [
    82,
    5
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
    81,
    5
   ],
   "v2": [
    82,
    5
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
    81,
    5
   ],
   "v2": [
    82,
    5
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
    81,
    5
   ],
   "v2": [
    82,
    5
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
    81,
    5
   ],
   "v2": [
    82,
    5
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
    81,
    5
   ],
   "v2": [
    82,
    5
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
    81,
    5
   ],
   "v2": [
    82,
    5
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

```
</details>

## Step 23

The statement at `httpx/_api.py`:26 binds `__all__`. `__all__` in `httpx/_api.py` lists 9 names, and `RemoteProtocolError` is not among them.

Candidate modules so far: 4; statements confirmed: 2, ruled out: 1, modules with no such import: 0, pending: 15. import coverage complete; star coverage complete. Latest ruled out: `httpx/__init__.py`:2, star import of `._api`, which does not export `RemoteProtocolError`.

Outstanding: know what `httpx/_auth.py` exports; know what `httpx/_client.py` exports; know what `httpx/_config.py` exports; know what `httpx/_content.py` exports; and 11 more.

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
    76,
    5
   ],
   "v2": [
    77,
    5
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
    76,
    5
   ],
   "v2": [
    77,
    5
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
    76,
    5
   ],
   "v2": [
    77,
    5
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
    76,
    5
   ],
   "v2": [
    77,
    5
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
    76,
    5
   ],
   "v2": [
    77,
    5
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
    76,
    5
   ],
   "v2": [
    77,
    5
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
    76,
    5
   ],
   "v2": [
    77,
    5
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
    76,
    5
   ],
   "v2": [
    77,
    5
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
    76,
    5
   ],
   "v2": [
    77,
    5
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
    76,
    5
   ],
   "v2": [
    77,
    5
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
   "key": "[\"read\", [\"htt
```
</details>

## Step 24

The statement at `httpx/_auth.py`:19 binds `__all__`. `__all__` in `httpx/_auth.py` lists 5 names, and `RemoteProtocolError` is not among them.

Candidate modules so far: 4; statements confirmed: 2, ruled out: 2, modules with no such import: 0, pending: 14. import coverage complete; star coverage complete. Latest ruled out: `httpx/__init__.py`:3, star import of `._auth`, which does not export `RemoteProtocolError`.

Still to settle: know what `httpx/_client.py` exports; know what `httpx/_config.py` exports; know what `httpx/_content.py` exports; know what `httpx/_exceptions.py` exports; and 10 more.

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
    71,
    5
   ],
   "v2": [
    72,
    5
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
    71,
    5
   ],
   "v2": [
    72,
    5
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
    71,
    5
   ],
   "v2": [
    72,
    5
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
    71,
    5
   ],
   "v2": [
    72,
    5
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
    71,
    5
   ],
   "v2": [
    72,
    5
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
    71,
    5
   ],
   "v2": [
    72,
    5
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
    71,
    5
   ],
   "v2": [
    72,
    5
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
    71,
    5
   ],
   "v2": [
    72,
    5
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
    71,
    5
   ],
   "v2": [
    72,
    5
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
    71,
    5
   ],
   "v2": [
    72,
    5
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
    71,
    5
   ],
   "v2": [
    72,
```
</details>

## Step 25

The statement at `httpx/_client.py`:54 binds `__all__`. `__all__` in `httpx/_client.py` lists 3 names, and `RemoteProtocolError` is not among them.

Candidate modules so far: 4; statements confirmed: 2, ruled out: 3, modules with no such import: 0, pending: 13. import coverage complete; star coverage complete. Latest ruled out: `httpx/__init__.py`:4, star import of `._client`, which does not export `RemoteProtocolError`.

Still to settle: know what `httpx/_config.py` exports; know what `httpx/_content.py` exports; know what `httpx/_exceptions.py` exports; know what `httpx/_models.py` exports; and 9 more.

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
    66,
    5
   ],
   "v2": [
    67,
    5
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
    66,
    5
   ],
   "v2": [
    67,
    5
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
    66,
    5
   ],
   "v2": [
    67,
    5
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
    66,
    5
   ],
   "v2": [
    67,
    5
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
    66,
    5
   ],
   "v2": [
    67,
    5
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
    66,
    5
   ],
   "v2": [
    67,
    5
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
    66,
    5
   ],
   "v2": [
    67,
    5
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
    66,
    5
   ],
   "v2": [
    67,
    5
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
    66,
    5
   ],
   "v2": [
    67,
    5
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
    66,
    5
   ],
   "v2": [
    67,
    5
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
    66,
    5
   ],
   "v2": [
    67,
    5
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
   
```
</details>

## Step 26

The statement at `httpx/_config.py`:13 binds `__all__`. `__all__` in `httpx/_config.py` lists 4 names, and `RemoteProtocolError` is not among them.

Candidate modules so far: 4; statements confirmed: 2, ruled out: 4, modules with no such import: 0, pending: 12. import coverage complete; star coverage complete. Latest ruled out: `httpx/__init__.py`:5, star import of `._config`, which does not export `RemoteProtocolError`.

Outstanding: know what `httpx/_content.py` exports; know what `httpx/_exceptions.py` exports; know what `httpx/_models.py` exports; know what `httpx/_status_codes.py` exports; and 8 more.

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
    61,
    5
   ],
   "v2": [
    62,
    5
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
    61,
    5
   ],
   "v2": [
    62,
    5
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
    61,
    5
   ],
   "v2": [
    62,
    5
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
    61,
    5
   ],
   "v2": [
    62,
    5
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
    61,
    5
   ],
   "v2": [
    62,
    5
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
    61,
    5
   ],
   "v2": [
    62,
    5
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
    61,
    5
   ],
   "v2": [
    62,
    5
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
    61,
    5
   ],
   "v2": [
    62,
    5
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
    61,
    5
   ],
   "v2": [
    62,
    5
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
    61,
    5
   ],
   "v2": [
    62,
    5
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
    61,
    5
   ],
   "v2": [
    62,
    5
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
   "call
```
</details>

## Step 27

The statement at `httpx/_content.py`:28 binds `__all__`. `__all__` in `httpx/_content.py` lists 1 names, and `RemoteProtocolError` is not among them.

Candidate modules so far: 4; statements confirmed: 2, ruled out: 5, modules with no such import: 0, pending: 11. import coverage complete; star coverage complete. Latest ruled out: `httpx/__init__.py`:6, star import of `._content`, which does not export `RemoteProtocolError`.

Outstanding: know what `httpx/_exceptions.py` exports; know what `httpx/_models.py` exports; know what `httpx/_status_codes.py` exports; know what `httpx/_transports/__init__.py` exports; and 7 more.

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
    56,
    5
   ],
   "v2": [
    57,
    5
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
    56,
    5
   ],
   "v2": [
    57,
    5
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
    56,
    5
   ],
   "v2": [
    57,
    5
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
    56,
    5
   ],
   "v2": [
    57,
    5
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
    56,
    5
   ],
   "v2": [
    57,
    5
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
    56,
    5
   ],
   "v2": [
    57,
    5
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
    56,
    5
   ],
   "v2": [
    57,
    5
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
    56,
    5
   ],
   "v2": [
    57,
    5
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
    56,
    5
   ],
   "v2": [
    57,
    5
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
    56,
    5
   ],
   "v2": [
    57,
    5
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
    56,
    5
   ],
   "v2": [
    57,
    5
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
  "call": "read('httpx/_exceptions.py', 42, 30)",
  "key": "[\"read\", [\"httpx/_exceptions.py\", 42, 30]]",
  "provenance": "`__all__` 
```
</details>

## Step 28

The statement at `httpx/_exceptions.py`:42 binds `__all__`. `__all__` in `httpx/_exceptions.py` lists 28 names, and it names `RemoteProtocolError`.

Candidate modules so far: 4; statements confirmed: 3, ruled out: 5, modules with no such import: 0, pending: 10. import coverage complete; star coverage complete. Latest ruled out: `httpx/__init__.py`:6, star import of `._content`, which does not export `RemoteProtocolError`.

Open: know what `httpx/_models.py` exports; know what `httpx/_status_codes.py` exports; know what `httpx/_transports/__init__.py` exports; know what `httpx/_types.py` exports; and 6 more.

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
    51,
    5
   ],
   "v2": [
    52,
    5
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
    51,
    5
   ],
   "v2": [
    52,
    5
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
    51,
    5
   ],
   "v2": [
    52,
    5
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
    51,
    5
   ],
   "v2": [
    52,
    5
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
    51,
    5
   ],
   "v2": [
    52,
    5
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
    51,
    5
   ],
   "v2": [
    52,
    5
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
    51,
    5
   ],
   "v2": [
    52,
    5
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
    51,
    5
   ],
   "v2": [
    52,
    5
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
    51,
    5
   ],
   "v2": [
    52,
    5
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
    51,
    5
   ],
   "v2": [
    52,
    5
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
  "call": "read('httpx/_models.py', 51, 30)",
  "key": "[\"read\", [\"httpx/_models.py\", 51, 30]]",
  "provenance": "`__all__` of `httpx/_models.py` starts at line 51 (outline header)",
  "v2": [
   52,
   5
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
  "fits": "[\"read\", [\"httpx/_status_codes.py\", 5, 30]]",
  "long": "[\"read\", [\"httpx/_status_codes.py\", 5, 30]]"
 },
 "adherence": {
  "planned": "[\"read\", [\"httpx/_models.py\", 51, 30]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "read",
   "step": 28,
   "path": "httpx/_models.py",
   "start": 51,
   "count": 30,
   "n": 30
 
```
</details>

## Step 29

The statement at `httpx/_models.py`:51 binds `__all__`. `__all__` in `httpx/_models.py` lists 4 names, and `RemoteProtocolError` is not among them.

Candidate modules so far: 4; statements confirmed: 3, ruled out: 6, modules with no such import: 0, pending: 9. import coverage complete; star coverage complete. Latest ruled out: `httpx/__init__.py`:8, star import of `._models`, which does not export `RemoteProtocolError`.

Still to settle: know what `httpx/_status_codes.py` exports; know what `httpx/_transports/__init__.py` exports; know what `httpx/_types.py` exports; know what `httpx/_urls.py` exports; and 5 more.

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
    46,
    5
   ],
   "v2": [
    47,
    5
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
    46,
    5
   ],
   "v2": [
    47,
    5
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
    46,
    5
   ],
   "v2": [
    47,
    5
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
    46,
    5
   ],
   "v2": [
    47,
    5
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
    46,
    5
   ],
   "v2": [
    47,
    5
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
    46,
    5
   ],
   "v2": [
    47,
    5
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
    46,
    5
   ],
   "v2": [
    47,
    5
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
    46,
    5
   ],
   "v2": [
    47,
    5
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
    46,
    5
   ],
   "v2": [
    47,
    5
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
  "call": "read('httpx/_status_codes.py', 5, 30)",
  "key": "[\"read\", [\"httpx/_status_codes.py\", 5, 30]]",
  "provenance": "`__all__` of `httpx/_status_codes.py` starts at line 5 (outline header)",
  "v2": [
   47,
   5
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
  "long": "[\"read\", [\"httpx/_transports/__init__.py\", 7, 30]]"
 },
 "adherence": {
  "planned": "[\"read\", [\"httpx/_status_codes.py\", 5, 30]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "read",
   "step": 29,
   "path": "httpx/_status_codes.py",
   "start": 5,
   "count": 30,
   "n": 30
  },
  {
   "kind": "all_names",
   "step": 29,
   "path": "httpx/_status_codes.py",
   "value": [
    "codes"
   ]
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "httpx/__init__.py",
    2,
    "out",
    "star import of `._api`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    3,
    "out",
    "star import of `._auth`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    4,
    "out"
```
</details>

## Step 30

The statement at `httpx/_status_codes.py`:5 binds `__all__`. `__all__` in `httpx/_status_codes.py` lists 1 names, and `RemoteProtocolError` is not among them.

Candidate modules so far: 4; statements confirmed: 3, ruled out: 7, modules with no such import: 0, pending: 8. import coverage complete; star coverage complete. Latest ruled out: `httpx/__init__.py`:9, star import of `._status_codes`, which does not export `RemoteProtocolError`.

Open: know what `httpx/_transports/__init__.py` exports; know what `httpx/_types.py` exports; know what `httpx/_urls.py` exports; know what `httpx/_transports/asgi.py` exports; and 4 more.

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
    41,
    5
   ],
   "v2": [
    42,
    5
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
    41,
    5
   ],
   "v2": [
    42,
    5
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
    41,
    5
   ],
   "v2": [
    42,
    5
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
    41,
    5
   ],
   "v2": [
    42,
    5
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
    41,
    5
   ],
   "v2": [
    42,
    5
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
    41,
    5
   ],
   "v2": [
    42,
    5
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
    41,
    5
   ],
   "v2": [
    42,
    5
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
    41,
    5
   ],
   "v2": [
    42,
    5
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
  "call": "read('httpx/_transports/__init__.py', 7, 30)",
  "key": "[\"read\", [\"httpx/_transports/__init__.py\", 7, 30]]",
  "provenance": "`__all__` of `httpx/_transports/__init__.py` starts at line 7 (outline header)",
  "v2": [
   42,
   5
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
   "step": 30,
   "path": "httpx/_transports/__init__.py",
   "start": 7,
   "count": 30,
   "n": 10
  },
  {
   "kind": "all_names",
   "step": 30,
   "path": "httpx/_transports/__init__.py",
   "value": [
    "ASGITransport",
    "AsyncBaseTransport",
    "BaseTransport",
    "AsyncHTTPTransport",
    "HTTPTransport",
    "MockTransport",
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
    "star import of `._api`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    3,
    "out",
    "star import of `._auth`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    4,
    "out",
    "star import of `._client`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    5,
    "out",
    "star import of `._config`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    6,
    "out",
    "star import of `._content`, which does not export `RemoteProtocolError`"
   ]
```
</details>

## Step 31

The statement at `httpx/_transports/__init__.py`:7 binds `__all__`. `__all__` in `httpx/_transports/__init__.py` lists 7 names, and `RemoteProtocolError` is not among them.

Candidate modules so far: 4; statements confirmed: 3, ruled out: 8, modules with no such import: 0, pending: 7. import coverage complete; star coverage complete. Latest ruled out: `httpx/__init__.py`:10, star import of `._transports`, which does not export `RemoteProtocolError`.

Outstanding: know what `httpx/_types.py` exports; know what `httpx/_urls.py` exports; know what `httpx/_transports/asgi.py` exports; know what `httpx/_transports/base.py` exports; and 3 more.

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
    36,
    5
   ],
   "v2": [
    37,
    5
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
    36,
    5
   ],
   "v2": [
    37,
    5
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
    36,
    5
   ],
   "v2": [
    37,
    5
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
    36,
    5
   ],
   "v2": [
    37,
    5
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
    36,
    5
   ],
   "v2": [
    37,
    5
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
    36,
    5
   ],
   "v2": [
    37,
    5
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
    36,
    5
   ],
   "v2": [
    37,
    5
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
  "call": "read('httpx/_transports/asgi.py', 26, 30)",
  "key": "[\"read\", [\"httpx/_transports/asgi.py\", 26, 30]]",
  "provenance": "`__all__` of `httpx/_transports/asgi.py` starts at line 26 (outline header)",
  "v2": [
   37,
   5
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
   "step": 31,
   "path": "httpx/_transports/asgi.py",
   "start": 26,
   "count": 30,
   "n": 30
  },
  {
   "kind": "all_names",
   "step": 31,
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
    "star import of `._api`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    3,
    "out",
    "star import of `._auth`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    4,
    "out",
    "star import of `._client`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    5,
    "out",
    "star import of `._config`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    6,
    "out",
    "star import of `._content`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    7,
    "in",
    "star import of `._exceptions`, which exports `RemoteProtocolError` from the target"
   ],
   [
    "httpx/__init__.py",
    8,
    "out",
    "star import of `._models`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    9,
    "out",
    "star import of `._status_codes`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    10,
    "out",
    "star import of `._transports`, which does not export `RemoteProtocolError`"
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
    23,
```
</details>

## Step 32

The statement at `httpx/_transports/asgi.py`:26 binds `__all__`. `__all__` in `httpx/_transports/asgi.py` lists 1 names, and `RemoteProtocolError` is not among them.

Candidate modules so far: 4; statements confirmed: 3, ruled out: 9, modules with no such import: 0, pending: 6. import coverage complete; star coverage complete. Latest ruled out: `httpx/_transports/__init__.py`:1, star import of `.asgi`, which does not export `RemoteProtocolError`.

Open: know what `httpx/_types.py` exports; know what `httpx/_urls.py` exports; know what `httpx/_transports/base.py` exports; know what `httpx/_transports/default.py` exports; and 2 more.

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
    31,
    5
   ],
   "v2": [
    32,
    5
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
    31,
    5
   ],
   "v2": [
    32,
    5
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
    31,
    5
   ],
   "v2": [
    32,
    5
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
    31,
    5
   ],
   "v2": [
    32,
    5
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
    31,
    5
   ],
   "v2": [
    32,
    5
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
    31,
    5
   ],
   "v2": [
    32,
    5
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
  "call": "read('httpx/_transports/base.py', 11, 30)",
  "key": "[\"read\", [\"httpx/_transports/base.py\", 11, 30]]",
  "provenance": "`__all__` of `httpx/_transports/base.py` starts at line 11 (outline header)",
  "v2": [
   32,
   5
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
   "step": 32,
   "path": "httpx/_transports/base.py",
   "start": 11,
   "count": 30,
   "n": 30
  },
  {
   "kind": "all_names",
   "step": 32,
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
    "star import of `._api`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    3,
    "out",
    "star import of `._auth`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    4,
    "out",
    "star import of `._client`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    5,
    "out",
    "star import of `._config`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    6,
    "out",
    "star import of `._content`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    7,
    "in",
    "star import of `._exceptions`, which exports `RemoteProtocolError` from the target"
   ],
   [
    "httpx/__init__.py",
    8,
    "out",
    "star import of `._models`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    9,
    "out",
    "star import of `._status_codes`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    10,
    "out",
    "star import of `._transports`, which does not export `RemoteProtocolError`"
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
    23,
    "in",
    "`._exceptions` resolves `RemoteProtocolError` to the target"
   ],
   [
    "httpx/_transports/__init__.py",
    1,
    "out",
    "star import of `.asgi`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/_transports/__init__.py",
    2,
    "out",
    "star import of `.base`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/_transports/__init__.py",
    3,
    "pending",
    ""
   ],
   [
    "httpx/_transports/__init__.py",
    4,
    "pending",
    ""

```
</details>

## Step 33

The statement at `httpx/_transports/base.py`:11 binds `__all__`. `__all__` in `httpx/_transports/base.py` lists 2 names, and `RemoteProtocolError` is not among them.

Candidate modules so far: 4; statements confirmed: 3, ruled out: 10, modules with no such import: 0, pending: 5. import coverage complete; star coverage complete. Latest ruled out: `httpx/_transports/__init__.py`:2, star import of `.base`, which does not export `RemoteProtocolError`.

Still to settle: know what `httpx/_types.py` exports; know what `httpx/_urls.py` exports; know what `httpx/_transports/default.py` exports; know what `httpx/_transports/mock.py` exports; and 1 more.

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
    26,
    5
   ],
   "v2": [
    27,
    5
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
    26,
    5
   ],
   "v2": [
    27,
    5
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
    26,
    5
   ],
   "v2": [
    27,
    5
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
    26,
    5
   ],
   "v2": [
    27,
    5
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
    26,
    5
   ],
   "v2": [
    27,
    5
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
  "call": "read('httpx/_transports/default.py', 69, 30)",
  "key": "[\"read\", [\"httpx/_transports/default.py\", 69, 30]]",
  "provenance": "`__all__` of `httpx/_transports/default.py` starts at line 69 (outline header)",
  "v2": [
   27,
   5
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
   "step": 33,
   "path": "httpx/_transports/default.py",
   "start": 69,
   "count": 30,
   "n": 30
  },
  {
   "kind": "all_names",
   "step": 33,
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
    "star import of `._api`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    3,
    "out",
    "star import of `._auth`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    4,
    "out",
    "star import of `._client`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    5,
    "out",
    "star import of `._config`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    6,
    "out",
    "star import of `._content`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    7,
    "in",
    "star import of `._exceptions`, which exports `RemoteProtocolError` from the target"
   ],
   [
    "httpx/__init__.py",
    8,
    "out",
    "star import of `._models`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    9,
    "out",
    "star import of `._status_codes`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    10,
    "out",
    "star import of `._transports`, which does not export `RemoteProtocolError`"
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
    23,
    "in",
    "`._exceptions` resolves `RemoteProtocolError` to the target"
   ],
   [
    "httpx/_transports/__init__.py",
    1,
    "out",
    "star import of `.asgi`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/_transports/__init__.py",
    2,
    "out",
    "star import of `.base`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/_transports/__init__.py",
    3,
    "out",
    "star import of `.default`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/_transports/__init__.py",
    4,
    "pending",
    ""
   ],
   [
    "httpx/_transports/__init__.py",
    5,
    "pending",
    ""
   ],
   [
    "httpx/_transports/default.py",
    39,
    "in",
    "`.._exceptions` resolves `RemoteProtocolError` to the target"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  }
 }
}
```
</details>

## Step 34

The statement at `httpx/_transports/default.py`:69 binds `__all__`. `__all__` in `httpx/_transports/default.py` lists 2 names, and `RemoteProtocolError` is not among them.

Candidate modules so far: 4; statements confirmed: 3, ruled out: 11, modules with no such import: 0, pending: 4. import coverage complete; star coverage complete. Latest ruled out: `httpx/_transports/__init__.py`:3, star import of `.default`, which does not export `RemoteProtocolError`.

Outstanding: know what `httpx/_types.py` exports; know what `httpx/_urls.py` exports; know what `httpx/_transports/mock.py` exports; know what `httpx/_transports/wsgi.py` exports.

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
    21,
    5
   ],
   "v2": [
    22,
    5
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
    21,
    5
   ],
   "v2": [
    22,
    5
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
    21,
    5
   ],
   "v2": [
    22,
    5
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
    21,
    5
   ],
   "v2": [
    22,
    5
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
  "call": "read('httpx/_transports/mock.py', 12, 30)",
  "key": "[\"read\", [\"httpx/_transports/mock.py\", 12, 30]]",
  "provenance": "`__all__` of `httpx/_transports/mock.py` starts at line 12 (outline header)",
  "v2": [
   22,
   5
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
   "step": 34,
   "path": "httpx/_transports/mock.py",
   "start": 12,
   "count": 30,
   "n": 30
  },
  {
   "kind": "all_names",
   "step": 34,
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
    "star import of `._api`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    3,
    "out",
    "star import of `._auth`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    4,
    "out",
    "star import of `._client`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    5,
    "out",
    "star import of `._config`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    6,
    "out",
    "star import of `._content`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    7,
    "in",
    "star import of `._exceptions`, which exports `RemoteProtocolError` from the target"
   ],
   [
    "httpx/__init__.py",
    8,
    "out",
    "star import of `._models`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    9,
    "out",
    "star import of `._status_codes`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    10,
    "out",
    "star import of `._transports`, which does not export `RemoteProtocolError`"
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
    23,
    "in",
    "`._exceptions` resolves `RemoteProtocolError` to the target"
   ],
   [
    "httpx/_transports/__init__.py",
    1,
    "out",
    "star import of `.asgi`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/_transports/__init__.py",
    2,
    "out",
    "star import of `.base`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/_transports/__init__.py",
    3,
    "out",
    "star import of `.default`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/_transports/__init__.py",
    4,
    "out",
    "star import of `.mock`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/_transports/__init__.py",
    5,
    "pending",
    ""
   ],
   [
    "httpx/_transports/default.py",
    39,
    "in",
    "`.._exceptions` resolves `RemoteProtocolError` to the target"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  }
 }
}
```
</details>

## Step 35

The statement at `httpx/_transports/mock.py`:12 binds `__all__`. `__all__` in `httpx/_transports/mock.py` lists 1 names, and `RemoteProtocolError` is not among them.

Candidate modules so far: 4; statements confirmed: 3, ruled out: 12, modules with no such import: 0, pending: 3. import coverage complete; star coverage complete. Latest ruled out: `httpx/_transports/__init__.py`:4, star import of `.mock`, which does not export `RemoteProtocolError`.

Still to settle: know what `httpx/_types.py` exports; know what `httpx/_urls.py` exports; know what `httpx/_transports/wsgi.py` exports.

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
    16,
    5
   ],
   "v2": [
    17,
    5
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
    16,
    5
   ],
   "v2": [
    17,
    5
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
    16,
    5
   ],
   "v2": [
    17,
    5
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
  "call": "read('httpx/_transports/wsgi.py', 19, 30)",
  "key": "[\"read\", [\"httpx/_transports/wsgi.py\", 19, 30]]",
  "provenance": "`__all__` of `httpx/_transports/wsgi.py` starts at line 19 (outline header)",
  "v2": [
   17,
   5
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
   "step": 35,
   "path": "httpx/_transports/wsgi.py",
   "start": 19,
   "count": 30,
   "n": 30
  },
  {
   "kind": "all_names",
   "step": 35,
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
    "star import of `._api`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    3,
    "out",
    "star import of `._auth`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    4,
    "out",
    "star import of `._client`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    5,
    "out",
    "star import of `._config`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    6,
    "out",
    "star import of `._content`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    7,
    "in",
    "star import of `._exceptions`, which exports `RemoteProtocolError` from the target"
   ],
   [
    "httpx/__init__.py",
    8,
    "out",
    "star import of `._models`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    9,
    "out",
    "star import of `._status_codes`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    10,
    "out",
    "star import of `._transports`, which does not export `RemoteProtocolError`"
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
    23,
    "in",
    "`._exceptions` resolves `RemoteProtocolError` to the target"
   ],
   [
    "httpx/_transports/__init__.py",
    1,
    "out",
    "star import of `.asgi`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/_transports/__init__.py",
    2,
    "out",
    "star import of `.base`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/_transports/__init__.py",
    3,
    "out",
    "star import of `.default`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/_transports/__init__.py",
    4,
    "out",
    "star import of `.mock`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/_transports/__init__.py",
    5,
    "out",
    "star import of `.wsgi`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/_transports/default.py",
    39,
    "in",
    "`.._exceptions` resolves `RemoteProtocolError` to the target"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  }
 }
}
```
</details>

## Step 36

The statement at `httpx/_transports/wsgi.py`:19 binds `__all__`. `__all__` in `httpx/_transports/wsgi.py` lists 1 names, and `RemoteProtocolError` is not among them.

Candidate modules so far: 4; statements confirmed: 3, ruled out: 13, modules with no such import: 0, pending: 2. import coverage complete; star coverage complete. Latest ruled out: `httpx/_transports/__init__.py`:5, star import of `.wsgi`, which does not export `RemoteProtocolError`.

Open: know what `httpx/_types.py` exports; know what `httpx/_urls.py` exports.

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
    11,
    5
   ],
   "v2": [
    12,
    5
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
    11,
    5
   ],
   "v2": [
    12,
    5
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
  "call": "read('httpx/_types.py', 89, 30)",
  "key": "[\"read\", [\"httpx/_types.py\", 89, 30]]",
  "provenance": "`__all__` of `httpx/_types.py` starts at line 89 (outline header)",
  "v2": [
   12,
   5
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
   "step": 36,
   "path": "httpx/_types.py",
   "start": 89,
   "count": 30,
   "n": 27
  },
  {
   "kind": "all_names",
   "step": 36,
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
    "star import of `._api`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    3,
    "out",
    "star import of `._auth`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    4,
    "out",
    "star import of `._client`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    5,
    "out",
    "star import of `._config`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    6,
    "out",
    "star import of `._content`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    7,
    "in",
    "star import of `._exceptions`, which exports `RemoteProtocolError` from the target"
   ],
   [
    "httpx/__init__.py",
    8,
    "out",
    "star import of `._models`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    9,
    "out",
    "star import of `._status_codes`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    10,
    "out",
    "star import of `._transports`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    11,
    "out",
    "star import of `._types`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    12,
    "pending",
    ""
   ],
   [
    "httpx/_client.py",
    23,
    "in",
    "`._exceptions` resolves `RemoteProtocolError` to the target"
   ],
   [
    "httpx/_transports/__init__.py",
    1,
    "out",
    "star import of `.asgi`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/_transports/__init__.py",
    2,
    "out",
    "star import of `.base`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/_transports/__init__.py",
    3,
    "out",
    "star import of `.default`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/_transports/__init__.py",
    4,
    "out",
    "star import of `.mock`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/_transports/__init__.py",
    5,
    "out",
    "star import of `.wsgi`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/_transports/default.py",
    39,
    "in",
    "`.._exceptions` resolves `RemoteProtocolError` to the target"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  }
 }
}
```
</details>

## Step 37

The statement at `httpx/_types.py`:89 binds `__all__`. `__all__` in `httpx/_types.py` lists 2 names, and `RemoteProtocolError` is not among them.

Candidate modules so far: 4; statements confirmed: 3, ruled out: 14, modules with no such import: 0, pending: 1. import coverage complete; star coverage complete. Latest ruled out: `httpx/_transports/__init__.py`:5, star import of `.wsgi`, which does not export `RemoteProtocolError`.

Outstanding: know what `httpx/_urls.py` exports.

Next: read `httpx/_urls.py` from line 12, because `__all__` of `httpx/_urls.py` starts at line 12 (outline header). I expect: the whole list fits the window (about 80%); the list runs past the window (about 20%). Plan by outcome: fits: done; long: work the items it opens.

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
   "call": "read('httpx/_urls.py', 12, 30)",
   "key": "[\"read\", [\"httpx/_urls.py\", 12, 30]]",
   "v1": [
    6,
    5
   ],
   "v2": [
    6,
    5
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
   6,
   5
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
  "fits": "done",
  "long": "continue"
 },
 "adherence": {
  "planned": "[\"read\", [\"httpx/_urls.py\", 12, 30]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "read",
   "step": 37,
   "path": "httpx/_urls.py",
   "start": 12,
   "count": 30,
   "n": 30
  },
  {
   "kind": "all_names",
   "step": 37,
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
    "star import of `._api`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    3,
    "out",
    "star import of `._auth`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    4,
    "out",
    "star import of `._client`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    5,
    "out",
    "star import of `._config`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    6,
    "out",
    "star import of `._content`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    7,
    "in",
    "star import of `._exceptions`, which exports `RemoteProtocolError` from the target"
   ],
   [
    "httpx/__init__.py",
    8,
    "out",
    "star import of `._models`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    9,
    "out",
    "star import of `._status_codes`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    10,
    "out",
    "star import of `._transports`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    11,
    "out",
    "star import of `._types`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/__init__.py",
    12,
    "out",
    "star import of `._urls`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/_client.py",
    23,
    "in",
    "`._exceptions` resolves `RemoteProtocolError` to the target"
   ],
   [
    "httpx/_transports/__init__.py",
    1,
    "out",
    "star import of `.asgi`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/_transports/__init__.py",
    2,
    "out",
    "star import of `.base`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/_transports/__init__.py",
    3,
    "out",
    "star import of `.default`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/_transports/__init__.py",
    4,
    "out",
    "star import of `.mock`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/_transports/__init__.py",
    5,
    "out",
    "star import of `.wsgi`, which does not export `RemoteProtocolError`"
   ],
   [
    "httpx/_transports/default.py",
    39,
    "in",
    "`.._exceptions` resolves `RemoteProtocolError` to the target"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  }
 }
}
```
</details>

## Final

Certificate complete. 3 import statements import this definition: `httpx/__init__.py:7`, `httpx/_client.py:23`, `httpx/_transports/default.py:39`. In hindsight, 1 of 37 calls were not needed for the certificate: steps 4.

**Answer:** `{"statements": ["httpx/__init__.py:7", "httpx/_client.py:23", "httpx/_transports/default.py:39"], "count": 3}`  
**Stopped:** certificate after 37 calls