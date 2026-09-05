# black-subclasses-1ffaaa76

**Repository:** black  
**Chain:** subclasses  
**Seed:** 0, prior f2e0b46ccc75305a, floor 5

## Task

`Grammar` is defined at `src/blib2to3/pgen2/grammar.py:31` (class).

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N; bindings take effect in source order. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. A class derives from a definition when a base written as a bare name or `module.Name` resolves to it. A call site is `name(...)` where the bare name refers to the module-level binding (not a parameter or local). Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

Starting from the definition of `Grammar` at `src/blib2to3/pgen2/grammar.py:31`. Then I need every class that derives from it, checking that each base name really points at this definition.

Next I will search the whole tree for classes deriving from `Grammar`; the search has to be complete before I can call the set final. Very likely nothing turns up. If it caps or it fits under the cap, I follow whatever it opens up.

**Call:** `grep('^\\s*class\\s+\\w+\\s*\\(.*\\bGrammar\\b', '.')`

**Response**: outcome `mid`

```
src/blib2to3/pgen2/conv.py:38:class Converter(grammar.Grammar):
src/blib2to3/pgen2/pgen.py:14:class PgenGrammar(grammar.Grammar):
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
   "desc": "search `.` for classes deriving from `Grammar`"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*class\\\\s+\\\\w+\\\\s*\\\\(.*\\\\bGrammar\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*class\\\\s+\\\\w+\\\\s*\\\\(.*\\\\bGrammar\\\\b\", \".\"]]",
   "v1": [
    19392910487,
    13622148540
   ],
   "v2": [
    19392910487,
    13622148540
   ],
   "p_cap": [
    2,
    39
   ],
   "forecast": {
    "zero": [
     35,
     39
    ],
    "mid": [
     2,
     39
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
  "call": "grep('^\\\\s*class\\\\s+\\\\w+\\\\s*\\\\(.*\\\\bGrammar\\\\b', '.')",
  "key": "[\"grep\", [\"^\\\\s*class\\\\s+\\\\w+\\\\s*\\\\(.*\\\\bGrammar\\\\b\", \".\"]]",
  "provenance": "subclass lines naming `Grammar` under `.` (derived)",
  "v2": [
   19392910487,
   13622148540
  ]
 },
 "forecast": {
  "zero": [
   35,
   39
  ],
  "mid": [
   2,
   39
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
    35,
    39
   ]
  }
 ],
 "adherence": null,
 "facts": [
  {
   "kind": "grep",
   "step": 1,
   "pattern": "^\\s*class\\s+\\w+\\s*\\(.*\\bGrammar\\b",
   "scope": ".",
   "hits": [
    [
     "src/blib2to3/pgen2/conv.py",
     38
    ],
    [
     "src/blib2to3/pgen2/pgen.py",
     14
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
   "src/blib2to3/pgen2/conv.py",
   "src/blib2to3/pgen2/pgen.py"
  ],
  "table": [
   [
    "src/blib2to3/pgen2/conv.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/blib2to3/pgen2/pgen.py",
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
  "n_pending": 2
 }
}
```
</details>

## Step 2

Huh: 2 matching lines anywhere for classes deriving from `Grammar`, in `src/blib2to3/pgen2/conv.py`, `src/blib2to3/pgen2/pgen.py`, and the search was under the cap, so that is the complete set there.

I'll look at `src/blib2to3/pgen2/pgen.py`'s top-level names for `Grammar`; the outline lists each class with its bases. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `src/blib2to3/pgen2/conv.py`'s top-level names for `Grammar`.

**Call:** `symbols('src/blib2to3/pgen2/pgen.py', 'Grammar')`

**Response**: outcome `ok`

```
module src/blib2to3/pgen2/pgen.py lines=389 dynamic=no all=none
14 class PgenGrammar (grammar.Grammar)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/blib2to3/pgen2/conv.py",
    "Grammar"
   ],
   "desc": "look at the classes in `src/blib2to3/pgen2/conv.py` that derive from `Grammar`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/blib2to3/pgen2/pgen.py",
    "Grammar"
   ],
   "desc": "look at the classes in `src/blib2to3/pgen2/pgen.py` that derive from `Grammar`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/blib2to3/pgen2/conv.py', 'Grammar')",
   "key": "[\"symbols\", [\"src/blib2to3/pgen2/conv.py\", \"Grammar\"]]",
   "v1": [
    51899,
    15950
   ],
   "v2": [
    26109,
    7975
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
     "src/blib2to3/pgen2/conv.py",
     "Grammar"
    ]
   ]
  },
  {
   "call": "symbols('src/blib2to3/pgen2/pgen.py', 'Grammar')",
   "key": "[\"symbols\", [\"src/blib2to3/pgen2/pgen.py\", \"Grammar\"]]",
   "v1": [
    51899,
    15950
   ],
   "v2": [
    26109,
    7975
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
     "src/blib2to3/pgen2/pgen.py",
     "Grammar"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/blib2to3/pgen2/pgen.py', 'Grammar')",
  "key": "[\"symbols\", [\"src/blib2to3/pgen2/pgen.py\", \"Grammar\"]]",
  "provenance": "`src/blib2to3/pgen2/pgen.py` had a matching line (step 1); its outline names every `Grammar` import exactly",
  "v2": [
   26109,
   7975
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
  "ok": "[\"symbols\", [\"src/blib2to3/pgen2/conv.py\", \"Grammar\"]]",
  "cap": "[\"symbols\", [\"src/blib2to3/pgen2/conv.py\", \"Grammar\"]]"
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
   "path": "src/blib2to3/pgen2/pgen.py",
   "filter": "Grammar",
   "header": {
    "lines": 389,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/blib2to3/pgen2/pgen.py",
     "name": "PgenGrammar",
     "line": 14,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "grammar.Grammar"
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
   "src/blib2to3/pgen2/conv.py",
   "src/blib2to3/pgen2/pgen.py"
  ],
  "table": [
   [
    "src/blib2to3/pgen2/conv.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/blib2to3/pgen2/pgen.py",
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
  "n_pending": 2
 }
}
```
</details>

## Step 3

`src/blib2to3/pgen2/pgen.py` has `class PgenGrammar(grammar.Grammar)` at line 14. Nothing binds `Grammar` at module level there.

Tally: 0 subclasses confirmed, 0 ruled out, 2 pending. The search itself is complete; what is left is checking the candidates.

I'll look at `src/blib2to3/pgen2/conv.py`'s top-level names for `Grammar`; the outline lists each class with its bases. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `src/blib2to3/pgen2/pgen.py`'s top-level names for `grammar`.

**Call:** `symbols('src/blib2to3/pgen2/conv.py', 'Grammar')`

**Response**: outcome `ok`

```
module src/blib2to3/pgen2/conv.py lines=257 dynamic=no all=none
38 class Converter (grammar.Grammar)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/blib2to3/pgen2/conv.py",
    "Grammar"
   ],
   "desc": "look at the classes in `src/blib2to3/pgen2/conv.py` that derive from `Grammar`"
  },
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/blib2to3/pgen2/pgen.py",
    "grammar"
   ],
   "desc": "check the top-level names of `src/blib2to3/pgen2/pgen.py` for `grammar`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/blib2to3/pgen2/conv.py', 'Grammar')",
   "key": "[\"symbols\", [\"src/blib2to3/pgen2/conv.py\", \"Grammar\"]]",
   "v1": [
    727626497,
    160138000
   ],
   "v2": [
    727626497,
    160138000
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
     "src/blib2to3/pgen2/conv.py",
     "Grammar"
    ]
   ]
  },
  {
   "call": "symbols('src/blib2to3/pgen2/pgen.py', 'grammar')",
   "key": "[\"symbols\", [\"src/blib2to3/pgen2/pgen.py\", \"grammar\"]]",
   "v1": [
    724423737,
    160138000
   ],
   "v2": [
    727626497,
    160138000
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     3,
     100
    ],
    "reexport": [
     23,
     25
    ],
    "star": [
     1,
     100
    ],
    "none": [
     1,
     25
    ]
   },
   "serves": [
    [
     "bindings",
     "src/blib2to3/pgen2/pgen.py",
     "grammar"
    ]
   ]
  },
  {
   "call": "symbols('src/blib2to3/pgen2/pgen.py')",
   "key": "[\"symbols\", [\"src/blib2to3/pgen2/pgen.py\"]]",
   "v1": [
    35208916139,
    7526486000
   ],
   "v2": [
    35336225849,
    7526486000
   ],
   "p_cap": [
    29,
    188
   ],
   "forecast": {
    "def": [
     477,
     18800
    ],
    "reexport": [
     3657,
     4700
    ],
    "star": [
     159,
     18800
    ],
    "none": [
     159,
     4700
    ],
    "cap": [
     29,
     188
    ]
   },
   "serves": [
    [
     "bindings",
     "src/blib2to3/pgen2/pgen.py",
     "grammar"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/blib2to3/pgen2/conv.py', 'Grammar')",
  "key": "[\"symbols\", [\"src/blib2to3/pgen2/conv.py\", \"Grammar\"]]",
  "provenance": "`src/blib2to3/pgen2/conv.py` had a matching line (step 1); its outline names every `Grammar` import exactly",
  "v2": [
   727626497,
   160138000
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
  "ok": "[\"symbols\", [\"src/blib2to3/pgen2/pgen.py\", \"grammar\"]]",
  "cap": "[\"symbols\", [\"src/blib2to3/pgen2/pgen.py\", \"grammar\"]]"
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
  "planned": "[\"symbols\", [\"src/blib2to3/pgen2/conv.py\", \"Grammar\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 3,
   "path": "src/blib2to3/pgen2/conv.py",
   "filter": "Grammar",
   "header": {
    "lines": 257,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/blib2to3/pgen2/conv.py",
     "name": "Converter",
     "line": 38,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "grammar.Grammar"
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
   "src/blib2to3/pgen2/conv.py",
   "src/blib2to3/pgen2/pgen.py"
  ],
  "table": [
   [
    "src/blib2to3/pgen2/conv.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/blib2to3/pgen2/pgen.py",
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
  "n_pending": 2
 }
}
```
</details>

## Step 4

`src/blib2to3/pgen2/conv.py` has `class Converter(grammar.Grammar)` at line 38. Nothing binds `Grammar` at module level there.

Tally: 0 subclasses confirmed, 0 ruled out, 2 pending. The search itself is complete; what is left is checking the candidates.

I'll look at `src/blib2to3/pgen2/pgen.py`'s top-level names for `grammar`; that settles what the name means there. Almost certainly it is re-exported from somewhere else. If the name is not bound there or it is defined right there, I will look at `src/blib2to3/pgen2/conv.py`'s top-level names for `grammar`.

**Call:** `symbols('src/blib2to3/pgen2/pgen.py', 'grammar')`

**Response**: outcome `reexport`

```
module src/blib2to3/pgen2/pgen.py lines=389 dynamic=no all=none
8 from grammar <- blib2to3.pgen2 grammar
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/blib2to3/pgen2/conv.py",
    "grammar"
   ],
   "desc": "check the top-level names of `src/blib2to3/pgen2/conv.py` for `grammar`"
  },
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/blib2to3/pgen2/pgen.py",
    "grammar"
   ],
   "desc": "check the top-level names of `src/blib2to3/pgen2/pgen.py` for `grammar`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/blib2to3/pgen2/conv.py', 'grammar')",
   "key": "[\"symbols\", [\"src/blib2to3/pgen2/conv.py\", \"grammar\"]]",
   "v1": [
    1459223,
    251000
   ],
   "v2": [
    1459223,
    251000
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     3,
     100
    ],
    "reexport": [
     23,
     25
    ],
    "star": [
     1,
     100
    ],
    "none": [
     1,
     25
    ]
   },
   "serves": [
    [
     "bindings",
     "src/blib2to3/pgen2/conv.py",
     "grammar"
    ]
   ]
  },
  {
   "call": "symbols('src/blib2to3/pgen2/pgen.py', 'grammar')",
   "key": "[\"symbols\", [\"src/blib2to3/pgen2/pgen.py\", \"grammar\"]]",
   "v1": [
    1459223,
    251000
   ],
   "v2": [
    1459223,
    251000
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     3,
     100
    ],
    "reexport": [
     23,
     25
    ],
    "star": [
     1,
     100
    ],
    "none": [
     1,
     25
    ]
   },
   "serves": [
    [
     "bindings",
     "src/blib2to3/pgen2/pgen.py",
     "grammar"
    ]
   ]
  },
  {
   "call": "symbols('src/blib2to3/pgen2/conv.py')",
   "key": "[\"symbols\", [\"src/blib2to3/pgen2/conv.py\"]]",
   "v1": [
    70403231,
    11797000
   ],
   "v2": [
    70403231,
    11797000
   ],
   "p_cap": [
    29,
    188
   ],
   "forecast": {
    "def": [
     477,
     18800
    ],
    "reexport": [
     3657,
     4700
    ],
    "star": [
     159,
     18800
    ],
    "none": [
     159,
     4700
    ],
    "cap": [
     29,
     188
    ]
   },
   "serves": [
    [
     "bindings",
     "src/blib2to3/pgen2/conv.py",
     "grammar"
    ]
   ]
  },
  {
   "call": "symbols('src/blib2to3/pgen2/pgen.py')",
   "key": "[\"symbols\", [\"src/blib2to3/pgen2/pgen.py\"]]",
   "v1": [
    70403231,
    11797000
   ],
   "v2": [
    70403231,
    11797000
   ],
   "p_cap": [
    29,
    188
   ],
   "forecast": {
    "def": [
     477,
     18800
    ],
    "reexport": [
     3657,
     4700
    ],
    "star": [
     159,
     18800
    ],
    "none": [
     159,
     4700
    ],
    "cap": [
     29,
     188
    ]
   },
   "serves": [
    [
     "bindings",
     "src/blib2to3/pgen2/pgen.py",
     "grammar"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/blib2to3/pgen2/pgen.py', 'grammar')",
  "key": "[\"symbols\", [\"src/blib2to3/pgen2/pgen.py\", \"grammar\"]]",
  "provenance": "module `src/blib2to3/pgen2/pgen.py` (step 1), name `grammar` (derived)",
  "v2": [
   1459223,
   251000
  ]
 },
 "forecast": {
  "def": [
   3,
   100
  ],
  "reexport": [
   23,
   25
  ],
  "star": [
   1,
   100
  ],
  "none": [
   1,
   25
  ]
 },
 "plan": {
  "def": "[\"symbols\", [\"src/blib2to3/pgen2/conv.py\", \"grammar\"]]",
  "reexport": "[\"symbols\", [\"src/blib2to3/pgen2/conv.py\", \"grammar\"]]",
  "star": "[\"symbols\", [\"src/blib2to3/pgen2/conv.py\", \"grammar\"]]",
  "none": "[\"symbols\", [\"src/blib2to3/pgen2/conv.py\", \"grammar\"]]"
 },
 "hedges": [
  {
   "outcome": "reexport",
   "word": "almost certainly",
   "p": [
    23,
    25
   ]
  }
 ],
 "adherence": {
  "planned": "[\"symbols\", [\"src/blib2to3/pgen2/pgen.py\", \"grammar\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 4,
   "path": "src/blib2to3/pgen2/pgen.py",
   "filter": "grammar",
   "header": {
    "lines": 389,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/blib2to3/pgen2/pgen.py",
     "name": "grammar",
     "line": 8,
     "kind": "from",
     "src": "blib2to3.pgen2",
     "src_name": "grammar",
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
  "of": 1,
  "candidates": [
   "src/blib2to3/pgen2/conv.py",
   "src/blib2to3/pgen2/pgen.py"
  ],
  "table": [
   [
    "src/blib2to3/pgen2/conv.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/blib2to3/pgen2/pgen.py",
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
  "n_pending": 2
 }
}
```
</details>

## Step 5

`src/blib2to3/pgen2/pgen.py` does not define `grammar` itself; line 8 imports it from `blib2to3.pgen2`.

Tally: 0 subclasses confirmed, 0 ruled out, 2 pending. The search itself is complete; what is left is checking the candidates.

Let me look at `src/blib2to3/pgen2/conv.py`'s top-level names for `grammar`; that settles what the name means there. Almost certainly it is re-exported from somewhere else. If the name is not bound there or it is defined right there, I will list `./` to see what lives there.

**Call:** `symbols('src/blib2to3/pgen2/conv.py', 'grammar')`

**Response**: outcome `reexport`

```
module src/blib2to3/pgen2/conv.py lines=257 dynamic=no all=none
35 from grammar <- blib2to3.pgen2 grammar
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/blib2to3/pgen2/conv.py",
    "grammar"
   ],
   "desc": "check the top-level names of `src/blib2to3/pgen2/conv.py` for `grammar`"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/blib2to3/pgen2/pgen.py",
    "blib2to3.pgen2"
   ],
   "desc": "find where `blib2to3.pgen2` (imported by `src/blib2to3/pgen2/pgen.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    7213969,
    1506000
   ],
   "v2": [
    7213969,
    1506000
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
     "src/blib2to3/pgen2/pgen.py",
     "blib2to3.pgen2"
    ]
   ]
  },
  {
   "call": "symbols('src/blib2to3/pgen2/conv.py', 'grammar')",
   "key": "[\"symbols\", [\"src/blib2to3/pgen2/conv.py\", \"grammar\"]]",
   "v1": [
    2488323,
    502000
   ],
   "v2": [
    7213969,
    1506000
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     3,
     100
    ],
    "reexport": [
     23,
     25
    ],
    "star": [
     1,
     100
    ],
    "none": [
     1,
     25
    ]
   },
   "serves": [
    [
     "bindings",
     "src/blib2to3/pgen2/conv.py",
     "grammar"
    ]
   ]
  },
  {
   "call": "symbols('src/blib2to3/pgen2/conv.py')",
   "key": "[\"symbols\", [\"src/blib2to3/pgen2/conv.py\"]]",
   "v1": [
    120590681,
    23594000
   ],
   "v2": [
    349975043,
    70782000
   ],
   "p_cap": [
    29,
    188
   ],
   "forecast": {
    "def": [
     477,
     18800
    ],
    "reexport": [
     3657,
     4700
    ],
    "star": [
     159,
     18800
    ],
    "none": [
     159,
     4700
    ],
    "cap": [
     29,
     188
    ]
   },
   "serves": [
    [
     "bindings",
     "src/blib2to3/pgen2/conv.py",
     "grammar"
    ]
   ]
  },
  {
   "call": "symbols('blib2to3/pgen2/__init__.py', 'grammar')",
   "key": "[\"symbols\", [\"blib2to3/pgen2/__init__.py\", \"grammar\"]]",
   "v1": [
    42734092292111,
    7221959246000
   ],
   "v2": [
    41594849978111,
    7221959246000
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     43581,
     27144100
    ],
    "reexport": [
     43581,
     2714410
    ],
    "star": [
     14527,
     13572050
    ],
    "none": [
     188851,
     5428820
    ],
    "missing": [
     256914,
     271441
    ]
   },
   "serves": [
    [
     "module_path",
     "src/blib2to3/pgen2/pgen.py",
     "blib2to3.pgen2"
    ]
   ]
  },
  {
   "call": "symbols('blib2to3/pgen2.py', 'grammar')",
   "key": "[\"symbols\", [\"blib2to3/pgen2.py\", \"grammar\"]]",
   "v1": [
    805288287139,
    136263382000
   ],
   "v2": [
    790036774139,
    136263382000
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     66864,
     6786025
    ],
    "reexport": [
     2050496,
     6786025
    ],
    "star": [
     22288,
     6786025
    ],
    "none": [
     89152,
     6786025
    ],
    "missing": [
     182289,
     271441
    ]
   },
   "serves": [
    [
     "module_path",
     "src/blib2to3/pgen2/pgen.py",
     "blib2to3.pgen2"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/blib2to3/pgen2/conv.py', 'grammar')",
  "key": "[\"symbols\", [\"src/blib2to3/pgen2/conv.py\", \"grammar\"]]",
  "provenance": "module `src/blib2to3/pgen2/conv.py` (step 1), name `grammar` (step 4)",
  "v2": [
   7213969,
   1506000
  ]
 },
 "forecast": {
  "def": [
   3,
   100
  ],
  "reexport": [
   23,
   25
  ],
  "star": [
   1,
   100
  ],
  "none": [
   1,
   25
  ]
 },
 "plan": {
  "def": "[\"ls\", [\".\"]]",
  "reexport": "[\"ls\", [\".\"]]",
  "star": "[\"ls\", [\".\"]]",
  "none": "[\"ls\", [\".\"]]"
 },
 "hedges": [
  {
   "outcome": "reexport",
   "word": "almost certainly",
   "p": [
    23,
    25
   ]
  }
 ],
 "adherence": {
  "planned": "[\"symbols\", [\"src/blib2to3/pgen2/conv.py\", \"grammar\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 5,
   "path": "src/blib2to3/pgen2/conv.py",
   "filter": "grammar",
   "header": {
    "lines": 257,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/blib2to3/pgen2/conv.py",
     "name": "grammar",
     "line": 35,
     "kind": "from",
     "src": "blib2to3.pgen2",
     "src_name": "grammar",
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
  "of": 1,
  "candidates": [
   "src/blib2to3/pgen2/conv.py",
   "src/blib2to3/pgen2/pgen.py"
  ],
  "table": [
   [
    "src/blib2to3/pgen2/conv.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/blib2to3/pgen2/pgen.py",
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
  "n_pending": 2
 }
}
```
</details>

## Step 6

`src/blib2to3/pgen2/conv.py` does not define `grammar` itself; line 35 imports it from `blib2to3.pgen2`.

Tally: 0 subclasses confirmed, 0 ruled out, 2 pending. The search itself is complete; what is left is checking the candidates.

Next I will list `./` to see what lives there; the listing settles whether the import is a module, a package, or not here at all. Very likely the listing fits. If the listing is too long, I will outline `blib2to3/pgen2.py` directly, which both checks that the file exists and shows me `grammar`. I could outline `blib2to3/pgen2.py` directly, which both checks that the file exists and shows me `grammar` instead, but it costs more calls in expectation.

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
    "src/blib2to3/pgen2/conv.py",
    "blib2to3.pgen2"
   ],
   "desc": "find where `blib2to3.pgen2` (imported by `src/blib2to3/pgen2/conv.py`) lives"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/blib2to3/pgen2/pgen.py",
    "blib2to3.pgen2"
   ],
   "desc": "find where `blib2to3.pgen2` (imported by `src/blib2to3/pgen2/pgen.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    83,
    30
   ],
   "v2": [
    144549015533,
    51098768250
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
     "src/blib2to3/pgen2/conv.py",
     "blib2to3.pgen2"
    ],
    [
     "module_path",
     "src/blib2to3/pgen2/pgen.py",
     "blib2to3.pgen2"
    ]
   ]
  },
  {
   "call": "symbols('blib2to3/pgen2.py', 'grammar')",
   "key": "[\"symbols\", [\"blib2to3/pgen2.py\", \"grammar\"]]",
   "v1": [
    74598618337,
    17032922750
   ],
   "v2": [
    59347105337,
    17032922750
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     66864,
     6786025
    ],
    "reexport": [
     2050496,
     6786025
    ],
    "star": [
     22288,
     6786025
    ],
    "none": [
     89152,
     6786025
    ],
    "missing": [
     182289,
     271441
    ]
   },
   "serves": [
    [
     "module_path",
     "src/blib2to3/pgen2/conv.py",
     "blib2to3.pgen2"
    ],
    [
     "module_path",
     "src/blib2to3/pgen2/pgen.py",
     "blib2to3.pgen2"
    ]
   ]
  },
  {
   "call": "symbols('blib2to3/pgen2/__init__.py', 'grammar')",
   "key": "[\"symbols\", [\"blib2to3/pgen2/__init__.py\", \"grammar\"]]",
   "v1": [
    35611400783,
    7193186500
   ],
   "v2": [
    26533772783,
    7193186500
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     43581,
     27144100
    ],
    "reexport": [
     43581,
     2714410
    ],
    "star": [
     14527,
     13572050
    ],
    "none": [
     188851,
     5428820
    ],
    "missing": [
     256914,
     271441
    ]
   },
   "serves": [
    [
     "module_path",
     "src/blib2to3/pgen2/conv.py",
     "blib2to3.pgen2"
    ],
    [
     "module_path",
     "src/blib2to3/pgen2/pgen.py",
     "blib2to3.pgen2"
    ]
   ]
  }
 ],
 "choice": {
  "call": "ls('.')",
  "key": "[\"ls\", [\".\"]]",
  "provenance": "`blib2to3.pgen2` imported by `src/blib2to3/pgen2/conv.py` should live under `.`",
  "v2": [
   144549015533,
   51098768250
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
  "cap": "[\"symbols\", [\"blib2to3/pgen2.py\", \"grammar\"]]"
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
  "phase": "subclasses",
  "step": 1,
  "of": 1,
  "candidates": [
   "src/blib2to3/pgen2/conv.py",
   "src/blib2to3/pgen2/pgen.py"
  ],
  "table": [
   [
    "src/blib2to3/pgen2/conv.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/blib2to3/pgen2/pgen.py",
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
  "n_pending": 2
 }
}
```
</details>

## Step 7

`./` has 20 entries: there is no `blib2to3` here.

Next I will outline `src/blib2to3/pgen2/__init__.py` directly, which both checks that the file exists and shows me `grammar`; if `blib2to3.pgen2` is a plain module that is where it has to be. Probably the name is not bound there. If it is re-exported from somewhere else, I follow whatever it opens up; if it is defined right there, that finishes it.

**Call:** `symbols('src/blib2to3/pgen2/__init__.py', 'grammar')`

**Response**: outcome `none`

```
module src/blib2to3/pgen2/__init__.py lines=5 dynamic=no all=none
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/blib2to3/pgen2/conv.py",
    "blib2to3.pgen2"
   ],
   "desc": "find where `blib2to3.pgen2` (imported by `src/blib2to3/pgen2/conv.py`) lives"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/blib2to3/pgen2/pgen.py",
    "blib2to3.pgen2"
   ],
   "desc": "find where `blib2to3.pgen2` (imported by `src/blib2to3/pgen2/pgen.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/blib2to3/pgen2/__init__.py', 'grammar')",
   "key": "[\"symbols\", [\"src/blib2to3/pgen2/__init__.py\", \"grammar\"]]",
   "v1": [
    3135371,
    1325000
   ],
   "v2": [
    562917651,
    239825000
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     147,
     5000
    ],
    "reexport": [
     147,
     500
    ],
    "star": [
     49,
     2500
    ],
    "none": [
     637,
     1000
    ],
    "missing": [
     1,
     50
    ]
   },
   "serves": [
    [
     "module_path",
     "src/blib2to3/pgen2/conv.py",
     "blib2to3.pgen2"
    ],
    [
     "module_path",
     "src/blib2to3/pgen2/pgen.py",
     "blib2to3.pgen2"
    ]
   ]
  },
  {
   "call": "symbols('src/blib2to3/pgen2.py', 'grammar')",
   "key": "[\"symbols\", [\"src/blib2to3/pgen2.py\", \"grammar\"]]",
   "v1": [
    105078313,
    32692750
   ],
   "v2": [
    514824764233,
    173271575000
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     336,
     13025
    ],
    "reexport": [
     10304,
     13025
    ],
    "star": [
     112,
     13025
    ],
    "none": [
     448,
     13025
    ],
    "missing": [
     73,
     521
    ]
   },
   "serves": [
    [
     "module_path",
     "src/blib2to3/pgen2/conv.py",
     "blib2to3.pgen2"
    ],
    [
     "module_path",
     "src/blib2to3/pgen2/pgen.py",
     "blib2to3.pgen2"
    ]
   ]
  },
  {
   "call": "ls('src/blib2to3')",
   "key": "[\"ls\", [\"src/blib2to3\"]]",
   "v1": [
    5691,
    1810
   ],
   "v2": [
    93108623,
    29978125
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
     "src/blib2to3/pgen2/conv.py",
     "blib2to3.pgen2"
    ],
    [
     "module_path",
     "src/blib2to3/pgen2/pgen.py",
     "blib2to3.pgen2"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/blib2to3/pgen2/__init__.py', 'grammar')",
  "key": "[\"symbols\", [\"src/blib2to3/pgen2/__init__.py\", \"grammar\"]]",
  "provenance": "`blib2to3.pgen2` would be `src/blib2to3/pgen2/__init__.py` if that file exists; one call both checks and closes it",
  "v2": [
   562917651,
   239825000
  ]
 },
 "forecast": {
  "def": [
   147,
   5000
  ],
  "reexport": [
   147,
   500
  ],
  "star": [
   49,
   2500
  ],
  "none": [
   637,
   1000
  ],
  "missing": [
   1,
   50
  ]
 },
 "plan": {
  "def": "done",
  "reexport": "continue",
  "star": "continue",
  "none": "continue",
  "missing": "[\"ls\", [\"src/blib2to3\"]]"
 },
 "hedges": [
  {
   "outcome": "none",
   "word": "probably",
   "p": [
    637,
    1000
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
   "step": 7,
   "path": "src/blib2to3/pgen2/__init__.py",
   "filter": "grammar",
   "header": {
    "lines": 5,
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
  "of": 1,
  "candidates": [
   "src/blib2to3/pgen2/conv.py",
   "src/blib2to3/pgen2/pgen.py"
  ],
  "table": [
   [
    "src/blib2to3/pgen2/conv.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/blib2to3/pgen2/pgen.py",
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
  "n_pending": 2
 }
}
```
</details>

## Step 8

The package `src/blib2to3/pgen2` does not bind `grammar`; for a package that leaves a submodule called `grammar` as the only option.

Tally: 0 subclasses confirmed, 0 ruled out, 2 pending. The search itself is complete; what is left is checking the candidates.

I'll outline `src/blib2to3/pgen2.py` directly, which both checks that the file exists and shows me `grammar`; if `blib2to3.pgen2` is a plain module that is where it has to be. Very likely it is re-exported from somewhere else. If the file does not exist, I will list `src/blib2to3/` to see what lives there; if the name is not bound there or it is defined right there, that finishes it. I could list `src/blib2to3/` to see what lives there instead, but it tends to open more follow-up work.

**Call:** `symbols('src/blib2to3/pgen2.py', 'grammar')`

**Response**: outcome `missing`

```
error: not a python file: src/blib2to3/pgen2.py
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/blib2to3/pgen2/conv.py",
    "blib2to3.pgen2"
   ],
   "desc": "find where `blib2to3.pgen2` (imported by `src/blib2to3/pgen2/conv.py`) lives"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/blib2to3/pgen2/pgen.py",
    "blib2to3.pgen2"
   ],
   "desc": "find where `blib2to3.pgen2` (imported by `src/blib2to3/pgen2/pgen.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/blib2to3/pgen2.py', 'grammar')",
   "key": "[\"symbols\", [\"src/blib2to3/pgen2.py\", \"grammar\"]]",
   "v1": [
    105078313,
    32692750
   ],
   "v2": [
    18226704903,
    5917387750
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     336,
     13025
    ],
    "reexport": [
     10304,
     13025
    ],
    "star": [
     112,
     13025
    ],
    "none": [
     448,
     13025
    ],
    "missing": [
     73,
     521
    ]
   },
   "serves": [
    [
     "module_path",
     "src/blib2to3/pgen2/conv.py",
     "blib2to3.pgen2"
    ],
    [
     "module_path",
     "src/blib2to3/pgen2/pgen.py",
     "blib2to3.pgen2"
    ]
   ]
  },
  {
   "call": "ls('src/blib2to3')",
   "key": "[\"ls\", [\"src/blib2to3\"]]",
   "v1": [
    5691,
    1810
   ],
   "v2": [
    18489596177,
    5917387750
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
     "src/blib2to3/pgen2/conv.py",
     "blib2to3.pgen2"
    ],
    [
     "module_path",
     "src/blib2to3/pgen2/pgen.py",
     "blib2to3.pgen2"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/blib2to3/pgen2.py', 'grammar')",
  "key": "[\"symbols\", [\"src/blib2to3/pgen2.py\", \"grammar\"]]",
  "provenance": "`blib2to3.pgen2` would be `src/blib2to3/pgen2.py` if that file exists; one call both checks and closes it",
  "v2": [
   18226704903,
   5917387750
  ]
 },
 "forecast": {
  "def": [
   336,
   13025
  ],
  "reexport": [
   10304,
   13025
  ],
  "star": [
   112,
   13025
  ],
  "none": [
   448,
   13025
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
  "missing": "[\"ls\", [\"src/blib2to3\"]]"
 },
 "hedges": [
  {
   "outcome": "reexport",
   "word": "very likely",
   "p": [
    10304,
    13025
   ]
  }
 ],
 "adherence": {
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "error",
   "step": 8,
   "call": "[\"symbols\", [\"src/blib2to3/pgen2.py\", \"grammar\"]]",
   "error": "not a python file: src/blib2to3/pgen2.py",
   "missing": "src/blib2to3/pgen2.py"
  }
 ],
 "goal_state": {
  "phase": "subclasses",
  "step": 1,
  "of": 1,
  "candidates": [
   "src/blib2to3/pgen2/conv.py",
   "src/blib2to3/pgen2/pgen.py"
  ],
  "table": [
   [
    "src/blib2to3/pgen2/conv.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/blib2to3/pgen2/pgen.py",
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
  "n_pending": 2
 }
}
```
</details>

## Step 9

There is no `src/blib2to3/pgen2.py`, so `pgen2` is either a package (`src/blib2to3/pgen2/__init__.py`) or not in this repository at all.

Tally: 0 subclasses confirmed, 0 ruled out, 2 pending. The search itself is complete; what is left is checking the candidates.

Let me look at `src/blib2to3/pgen2/grammar.py`'s top-level names for `Grammar`; that settles what the name means there. Almost certainly it is defined right there. If the name is not bound there, that finishes it; if it is re-exported from somewhere else, I follow whatever it opens up. I could outline all of `src/blib2to3/pgen2/grammar.py` instead, but it is more likely to hit the cap.

**Call:** `symbols('src/blib2to3/pgen2/grammar.py', 'Grammar')`

**Response**: outcome `def`

```
module src/blib2to3/pgen2/grammar.py lines=229 dynamic=no all=none
31 class Grammar ()
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/blib2to3/pgen2/grammar.py",
    "Grammar"
   ],
   "desc": "check the top-level names of `src/blib2to3/pgen2/grammar.py` for `Grammar`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/blib2to3/pgen2/grammar.py', 'Grammar')",
   "key": "[\"symbols\", [\"src/blib2to3/pgen2/grammar.py\", \"Grammar\"]]",
   "v1": [
    2377381,
    2264020
   ],
   "v2": [
    2377381,
    2264020
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     423,
     451
    ],
    "reexport": [
     10,
     451
    ],
    "star": [
     1,
     451
    ],
    "none": [
     17,
     451
    ]
   },
   "serves": [
    [
     "bindings",
     "src/blib2to3/pgen2/grammar.py",
     "Grammar"
    ]
   ]
  },
  {
   "call": "symbols('src/blib2to3/pgen2/grammar.py')",
   "key": "[\"symbols\", [\"src/blib2to3/pgen2/grammar.py\"]]",
   "v1": [
    32037763,
    26602235
   ],
   "v2": [
    32037763,
    26602235
   ],
   "p_cap": [
    29,
    188
   ],
   "forecast": {
    "def": [
     1431,
     1804
    ],
    "reexport": [
     795,
     42394
    ],
    "star": [
     159,
     84788
    ],
    "none": [
     2703,
     84788
    ],
    "cap": [
     29,
     188
    ]
   },
   "serves": [
    [
     "bindings",
     "src/blib2to3/pgen2/grammar.py",
     "Grammar"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/blib2to3/pgen2/grammar.py', 'Grammar')",
  "key": "[\"symbols\", [\"src/blib2to3/pgen2/grammar.py\", \"Grammar\"]]",
  "provenance": "module `src/blib2to3/pgen2/grammar.py` (task), name `Grammar` (task)",
  "v2": [
   2377381,
   2264020
  ]
 },
 "forecast": {
  "def": [
   423,
   451
  ],
  "reexport": [
   10,
   451
  ],
  "star": [
   1,
   451
  ],
  "none": [
   17,
   451
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
   "outcome": "def",
   "word": "almost certainly",
   "p": [
    423,
    451
   ]
  }
 ],
 "adherence": {
  "planned": "[\"ls\", [\"src/blib2to3\"]]",
  "status": "replanned"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 9,
   "path": "src/blib2to3/pgen2/grammar.py",
   "filter": "Grammar",
   "header": {
    "lines": 229,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/blib2to3/pgen2/grammar.py",
     "name": "Grammar",
     "line": 31,
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
  "of": 1,
  "candidates": [
   "src/blib2to3/pgen2/conv.py",
   "src/blib2to3/pgen2/pgen.py"
  ],
  "table": [
   [
    "src/blib2to3/pgen2/conv.py",
    "src/blib2to3/pgen2/conv.py:38:Converter",
    "in",
    "base `grammar.Grammar` resolves to the target"
   ],
   [
    "src/blib2to3/pgen2/pgen.py",
    "src/blib2to3/pgen2/pgen.py:14:PgenGrammar",
    "in",
    "base `grammar.Grammar` resolves to the target"
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

2 classes derive from it directly: `Converter` (`src/blib2to3/pgen2/conv.py:38`), `PgenGrammar` (`src/blib2to3/pgen2/pgen.py:14`). Looking back, all 9 calls were needed.

**Answer:** `{"final_kind": "subclasses", "final": ["src/blib2to3/pgen2/conv.py:38:Converter", "src/blib2to3/pgen2/pgen.py:14:PgenGrammar"], "steps": [{"op": "subclasses", "output": ["src/blib2to3/pgen2/conv.py:38:Converter", "src/blib2to3/pgen2/pgen.py:14:PgenGrammar"]}], "stuck": null}`  
**Stopped:** certificate after 9 calls