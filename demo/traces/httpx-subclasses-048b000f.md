# httpx-subclasses-048b000f

**Repository:** httpx  
**Chain:** subclasses  
**Seed:** 0, prior 708591d2904e1ac3, floor 3

## Task

`ProtocolError` is defined at `httpx/_exceptions.py:216` (class). List every class that derives from it directly, as `path:line:ClassName`, making sure each base name really resolves to this definition.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N; bindings take effect in source order. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. A class derives from a definition when a base written as a bare name or `module.Name` resolves to it. A call site is `name(...)` where the bare name refers to the module-level binding (not a parameter or local). Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

Starting from the definition of `ProtocolError` at `httpx/_exceptions.py:216`. Then I need every class that derives from it, checking that each base name really points at this definition.

Next I will search the whole tree for classes deriving from `ProtocolError`; the search has to be complete before I can call the set final. Very likely nothing turns up. If it caps or it fits under the cap, I follow whatever it opens up.

**Call:** `grep('^\\s*class\\s+\\w+\\s*\\(.*\\bProtocolError\\b', '.')`

**Response**: outcome `mid`

```
httpx/_exceptions.py:222:class LocalProtocolError(ProtocolError):
httpx/_exceptions.py:232:class RemoteProtocolError(ProtocolError):
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
   "desc": "search `.` for classes deriving from `ProtocolError`"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*class\\\\s+\\\\w+\\\\s*\\\\(.*\\\\bProtocolError\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*class\\\\s+\\\\w+\\\\s*\\\\(.*\\\\bProtocolError\\\\b\", \".\"]]",
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
  "call": "grep('^\\\\s*class\\\\s+\\\\w+\\\\s*\\\\(.*\\\\bProtocolError\\\\b', '.')",
  "key": "[\"grep\", [\"^\\\\s*class\\\\s+\\\\w+\\\\s*\\\\(.*\\\\bProtocolError\\\\b\", \".\"]]",
  "provenance": "subclass lines naming `ProtocolError` under `.` (derived)",
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
   "pattern": "^\\s*class\\s+\\w+\\s*\\(.*\\bProtocolError\\b",
   "scope": ".",
   "hits": [
    [
     "httpx/_exceptions.py",
     222
    ],
    [
     "httpx/_exceptions.py",
     232
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "phase": "subclasses",
  "step": 1,
  "of": 1,
  "candidates": [
   "httpx/_exceptions.py"
  ],
  "table": [
   [
    "httpx/_exceptions.py",
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
  "n_pending": 1
 }
}
```
</details>

## Step 2

Huh: 2 matching lines anywhere for classes deriving from `ProtocolError`, in `httpx/_exceptions.py`, and the search was under the cap, so that is the complete set there.

I'll look at `httpx/_exceptions.py`'s top-level names for `ProtocolError`; the outline lists each class with its bases. Almost certainly the outline shows what I need. If the outline is too long to fit, I follow whatever it opens up.

**Call:** `symbols('httpx/_exceptions.py', 'ProtocolError')`

**Response**: outcome `ok`

```
module httpx/_exceptions.py lines=378 dynamic=no all=static@42
216 class ProtocolError (TransportError)
222 class LocalProtocolError (ProtocolError)
232 class RemoteProtocolError (ProtocolError)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "httpx/_exceptions.py",
    "ProtocolError"
   ],
   "desc": "look at the classes in `httpx/_exceptions.py` that derive from `ProtocolError`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('httpx/_exceptions.py', 'ProtocolError')",
   "key": "[\"symbols\", [\"httpx/_exceptions.py\", \"ProtocolError\"]]",
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
     "httpx/_exceptions.py",
     "ProtocolError"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('httpx/_exceptions.py', 'ProtocolError')",
  "key": "[\"symbols\", [\"httpx/_exceptions.py\", \"ProtocolError\"]]",
  "provenance": "`httpx/_exceptions.py` had a matching line (task); its outline names every `ProtocolError` import exactly",
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
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 2,
   "path": "httpx/_exceptions.py",
   "filter": "ProtocolError",
   "header": {
    "lines": 378,
    "dynamic": false,
    "all_status": "static",
    "all_line": 42
   },
   "bindings": [
    {
     "module": "httpx/_exceptions.py",
     "name": "ProtocolError",
     "line": 216,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "TransportError"
     ]
    },
    {
     "module": "httpx/_exceptions.py",
     "name": "LocalProtocolError",
     "line": 222,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "ProtocolError"
     ]
    },
    {
     "module": "httpx/_exceptions.py",
     "name": "RemoteProtocolError",
     "line": 232,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "ProtocolError"
     ]
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "subclasses",
  "step": 1,
  "of": 1,
  "candidates": [
   "httpx/_exceptions.py"
  ],
  "table": [
   [
    "httpx/_exceptions.py",
    "httpx/_exceptions.py:222:LocalProtocolError",
    "in",
    "base `ProtocolError` resolves to the target"
   ],
   [
    "httpx/_exceptions.py",
    "httpx/_exceptions.py:232:RemoteProtocolError",
    "in",
    "base `ProtocolError` resolves to the target"
   ]
  ],
  "uncovered": {
   "SUBCLASS": []
  },
  "n_in": 2,
  "n_out": 0,
  "n_pending": 0
 }
}
```
</details>

## Final

2 classes derive from it directly: `LocalProtocolError` (`httpx/_exceptions.py:222`), `RemoteProtocolError` (`httpx/_exceptions.py:232`). Looking back, all 2 calls were needed.

**Answer:** `{"final_kind": "subclasses", "final": ["httpx/_exceptions.py:222:LocalProtocolError", "httpx/_exceptions.py:232:RemoteProtocolError"], "steps": [{"op": "subclasses", "output": ["httpx/_exceptions.py:222:LocalProtocolError", "httpx/_exceptions.py:232:RemoteProtocolError"]}], "stuck": null}`  
**Stopped:** certificate after 2 calls