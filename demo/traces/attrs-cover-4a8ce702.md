# attrs-cover-4a8ce702

**Repository:** attrs  
**Family:** cover  
**Seed:** 0, prior df2023878106d754

## Task

`make_class` is defined at `src/attr/_make.py:3261` (def). List every module-level import statement in the snapshot that imports this definition: `from ... import` statements naming it (directly or with `as`), and star imports of modules that export it. Answer as `path:line` entries.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

Nothing seen yet beyond the task text.

Candidate modules so far: 0; statements confirmed: 0, ruled out: 0, modules with no such import: 0, pending: 0. import coverage open at `.`; star coverage open at `.`.

Outstanding: cover `.` for import lines; cover `.` for star lines.

Next: grep from-imports naming `make_class` or star imports under `.`, because import and star lines under `.` in one call. I expect: hits under the cap (about 45%); no hits (about 45%); a capped result (about 10%). The alternative, grep from-imports naming `make_class` under `.`, serves fewer of the open items. Plan by outcome: zero: done; mid: outline each module that appears; cap: list the scope and split it.

**Call:** `grep('^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bmake_class\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*make_class\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$', '.')`

**Response**: outcome `mid`

```
src/attr/__init__.py:27:    make_class,
src/attrs/__init__.py:20:    make_class,
src/attrs/__init__.pyi:37:from attr import make_class as make_class
src/attrs/converters.py:3:from attr.converters import *  # noqa: F403
src/attrs/exceptions.py:3:from attr.exceptions import *  # noqa: F403
src/attrs/filters.py:3:from attr.filters import *  # noqa: F403
src/attrs/setters.py:3:from attr.setters import *  # noqa: F403
src/attrs/validators.py:3:from attr.validators import *  # noqa: F403
tests/attr_import_star.py:4:from attr import *  # noqa: F403
tests/strategies.py:17:from .utils import make_class
tests/test_dunders.py:25:    make_class,
tests/test_make.py:44:    make_class,
tests/test_mypy.yml:1384:            from other import *
tests/utils.py:8:from attr._make import NOTHING, _default_init_alias_for, make_class
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
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bmake_class\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*make_class\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bmake_class\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*make_class\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
   "v1": [
    604593608543,
    141991736250
   ],
   "v2": [
    604593608543,
    141991736250
   ],
   "p_cap": [
    3,
    25
   ],
   "forecast": {
    "zero": [
     11,
     25
    ],
    "mid": [
     11,
     25
    ],
    "cap": [
     3,
     25
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
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bmake_class\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*make_class\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bmake_class\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*make_class\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
   "v1": [
    25081236912073,
    4049604317850
   ],
   "v2": [
    28439144459521,
    4898714900625
   ],
   "p_cap": [
    1,
    23
   ],
   "forecast": {
    "zero": [
     16,
     23
    ],
    "mid": [
     6,
     23
    ],
    "cap": [
     1,
     23
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
    25081236912073,
    4049604317850
   ],
   "v2": [
    25081236912073,
    4049604317850
   ],
   "p_cap": [
    4,
    31
   ],
   "forecast": {
    "zero": [
     17,
     31
    ],
    "mid": [
     10,
     31
    ],
    "cap": [
     4,
     31
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
  "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bmake_class\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*make_class\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
  "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bmake_class\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*make_class\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
  "provenance": "import and star lines under `.` in one call",
  "v2": [
   604593608543,
   141991736250
  ]
 },
 "forecast": {
  "zero": [
   11,
   25
  ],
  "mid": [
   11,
   25
  ],
  "cap": [
   3,
   25
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
   "pattern": "^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bmake_class\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*make_class\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$",
   "scope": ".",
   "hits": [
    [
     "src/attr/__init__.py",
     27
    ],
    [
     "src/attrs/__init__.py",
     20
    ],
    [
     "src/attrs/__init__.pyi",
     37
    ],
    [
     "src/attrs/converters.py",
     3
    ],
    [
     "src/attrs/exceptions.py",
     3
    ],
    [
     "src/attrs/filters.py",
     3
    ],
    [
     "src/attrs/setters.py",
     3
    ],
    [
     "src/attrs/validators.py",
     3
    ],
    [
     "tests/attr_import_star.py",
     4
    ],
    [
     "tests/strategies.py",
     17
    ],
    [
     "tests/test_dunders.py",
     25
    ],
    [
     "tests/test_make.py",
     44
    ],
    [
     "tests/test_mypy.yml",
     1384
    ],
    [
     "tests/utils.py",
     8
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "src/attr/__init__.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "src/attrs/__init__.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "src/attrs/converters.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "src/attrs/exceptions.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "src/attrs/filters.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "src/attrs/setters.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "src/attrs/validators.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/attr_import_star.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/strategies.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_dunders.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_make.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/utils.py",
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

The grep under `.` returned 14 lines, under the cap, so these are all of them: `src/attr/__init__.py`, `src/attrs/__init__.py`, `src/attrs/__init__.pyi`, `src/attrs/converters.py` and 10 more files.

Candidate modules so far: 12; statements confirmed: 0, ruled out: 0, modules with no such import: 0, pending: 12. import coverage complete; star coverage complete.

Still to settle: outline `src/attr/__init__.py` for its `make_class` imports; outline `src/attrs/__init__.py` for its `make_class` imports; outline `src/attrs/converters.py` for its `make_class` imports; outline `src/attrs/exceptions.py` for its `make_class` imports; and 8 more.

Next: outline `src/attrs/validators.py` filtered to `make_class`, because `src/attrs/validators.py` had a matching line (step 1); its outline names every `make_class` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/attr/__init__.py` filtered to `make_class`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/attr/__init__.py` filtered to `make_class`; cap: outline `src/attr/__init__.py` filtered to `make_class`.

**Call:** `symbols('src/attrs/validators.py', 'make_class')`

**Response**: outcome `ok`

```
module src/attrs/validators.py lines=4 dynamic=no all=none
3 star <- attr.validators
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attr/__init__.py",
    "make_class"
   ],
   "desc": "outline `src/attr/__init__.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/__init__.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/__init__.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/converters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/converters.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/exceptions.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/exceptions.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/filters.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/setters.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/validators.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "make_class"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/strategies.py",
    "make_class"
   ],
   "desc": "outline `tests/strategies.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "make_class"
   ],
   "desc": "outline `tests/test_dunders.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "make_class"
   ],
   "desc": "outline `tests/test_make.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/utils.py",
    "make_class"
   ],
   "desc": "outline `tests/utils.py` for its `make_class` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/__init__.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attr/__init__.py\", \"make_class\"]]",
   "v1": [
    16253491,
    904550
   ],
   "v2": [
    8135791,
    452275
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
     "src/attr/__init__.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/__init__.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/__init__.py\", \"make_class\"]]",
   "v1": [
    16253491,
    904550
   ],
   "v2": [
    8135791,
    452275
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
     "src/attrs/__init__.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/converters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/converters.py\", \"make_class\"]]",
   "v1": [
    16253491,
    904550
   ],
   "v2": [
    8135791,
    452275
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
     "src/attrs/converters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/exceptions.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/exceptions.py\", \"make_class\"]]",
   "v1": [
    16253491,
    904550
   ],
   "v2": [
    8135791,
    452275
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
     "src/attrs/exceptions.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/filters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"make_class\"]]",
   "v1": [
    16253491,
    904550
   ],
   "v2": [
    8135791,
    452275
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
     "src/attrs/filters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"make_class\"]]",
   "v1": [
    16253491,
    904550
   ],
   "v2": [
    8135791,
    452275
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
     "src/attrs/setters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"make_class\"]]",
   "v1": [
    16253491,
    904550
   ],
   "v2": [
    8135791,
    452275
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
     "src/attrs/validators.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"make_class\"]]",
   "v1": [
    16253491,
    904550
   ],
   "v2": [
    8135791,
    452275
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
     "tests/attr_import_star.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/strategies.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/strategies.py\", \"make_class\"]]",
   "v1": [
    1625349
```
</details>

## Step 3

`src/attrs/validators.py` binds no `make_class` at module level; 1 star import(s): `attr.validators`; no `__all__`; no dynamic namespace tricks.

Candidate modules so far: 12; statements confirmed: 0, ruled out: 0, modules with no such import: 0, pending: 12. import coverage complete; star coverage complete.

Outstanding: outline `src/attr/__init__.py` for its `make_class` imports; outline `src/attrs/__init__.py` for its `make_class` imports; outline `src/attrs/converters.py` for its `make_class` imports; outline `src/attrs/exceptions.py` for its `make_class` imports; and 8 more.

Next: outline `src/attr/__init__.py` filtered to `make_class`, because `src/attr/__init__.py` had a matching line (step 1); its outline names every `make_class` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/attrs/__init__.py` filtered to `make_class`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/attrs/__init__.py` filtered to `make_class`; cap: outline `src/attrs/__init__.py` filtered to `make_class`.

**Call:** `symbols('src/attr/__init__.py', 'make_class')`

**Response**: outcome `ok`

```
module src/attr/__init__.py lines=121 dynamic=yes all=static@45
16 from make_class <- ._make make_class
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attr/__init__.py",
    "make_class"
   ],
   "desc": "outline `src/attr/__init__.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/__init__.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/__init__.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/converters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/converters.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/exceptions.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/exceptions.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/filters.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/setters.py` for its `make_class` imports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/validators.py",
    "attr.validators"
   ],
   "desc": "locate the module `attr.validators` imported by `src/attrs/validators.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "make_class"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/strategies.py",
    "make_class"
   ],
   "desc": "outline `tests/strategies.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "make_class"
   ],
   "desc": "outline `tests/test_dunders.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "make_class"
   ],
   "desc": "outline `tests/test_make.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/utils.py",
    "make_class"
   ],
   "desc": "outline `tests/utils.py` for its `make_class` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/__init__.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attr/__init__.py\", \"make_class\"]]",
   "v1": [
    16764941,
    904550
   ],
   "v2": [
    8391516,
    452275
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
     "src/attr/__init__.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/__init__.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/__init__.py\", \"make_class\"]]",
   "v1": [
    16764941,
    904550
   ],
   "v2": [
    8391516,
    452275
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
     "src/attrs/__init__.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/converters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/converters.py\", \"make_class\"]]",
   "v1": [
    16764941,
    904550
   ],
   "v2": [
    8391516,
    452275
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
     "src/attrs/converters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/exceptions.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/exceptions.py\", \"make_class\"]]",
   "v1": [
    16764941,
    904550
   ],
   "v2": [
    8391516,
    452275
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
     "src/attrs/exceptions.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/filters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"make_class\"]]",
   "v1": [
    16764941,
    904550
   ],
   "v2": [
    8391516,
    452275
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
     "src/attrs/filters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"make_class\"]]",
   "v1": [
    16764941,
    904550
   ],
   "v2": [
    8391516,
    452275
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
     "src/attrs/setters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"make_class\"]]",
   "v1": [
    16764941,
    904550
   ],
   "v2": [
    8391516,
    452275
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
     "tests/attr_import_star.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/strategies.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/strategies.py\", \"make_class\"]]",
   "v1": [
    16764941,
    904550
   ],
   "v2": [
    8391516,
    452275
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
     "tests/strategies.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_dunders.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/test_dunders.py\", \"make_class\"]]",
   "v1
```
</details>

## Step 4

In `src/attr/__init__.py`, `make_class` has exactly one binding: line 16 imports it as `make_class` from `._make`. It uses dynamic namespace tricks, a literal `__all__` at line 45.

Candidate modules so far: 12; statements confirmed: 0, ruled out: 0, modules with no such import: 0, pending: 12. import coverage complete; star coverage complete.

Outstanding: close the namespace of `src/attr/_make.py` for `make_class`; outline `src/attrs/__init__.py` for its `make_class` imports; outline `src/attrs/converters.py` for its `make_class` imports; outline `src/attrs/exceptions.py` for its `make_class` imports; and 8 more.

Next: outline `src/attrs/__init__.py` filtered to `make_class`, because `src/attrs/__init__.py` had a matching line (step 1); its outline names every `make_class` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/attr/_make.py` filtered to `make_class`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/attr/_make.py` filtered to `make_class`; cap: outline `src/attr/_make.py` filtered to `make_class`.

**Call:** `symbols('src/attrs/__init__.py', 'make_class')`

**Response**: outcome `ok`

```
module src/attrs/__init__.py lines=77 dynamic=yes all=static@31
3 from make_class <- attr make_class
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/attr/_make.py",
    "make_class"
   ],
   "desc": "close the namespace of `src/attr/_make.py` for `make_class`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/__init__.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/__init__.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/converters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/converters.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/exceptions.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/exceptions.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/filters.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/setters.py` for its `make_class` imports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/validators.py",
    "attr.validators"
   ],
   "desc": "locate the module `attr.validators` imported by `src/attrs/validators.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "make_class"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/strategies.py",
    "make_class"
   ],
   "desc": "outline `tests/strategies.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "make_class"
   ],
   "desc": "outline `tests/test_dunders.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "make_class"
   ],
   "desc": "outline `tests/test_make.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/utils.py",
    "make_class"
   ],
   "desc": "outline `tests/utils.py` for its `make_class` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/_make.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attr/_make.py\", \"make_class\"]]",
   "v1": [
    80200297301,
    4435985564
   ],
   "v2": [
    2007225425307,
    110899639100
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     56,
     59
    ],
    "reexport": [
     13,
     472
    ],
    "star": [
     1,
     472
    ],
    "none": [
     5,
     236
    ]
   },
   "serves": [
    [
     "bindings",
     "src/attr/_make.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/__init__.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/__init__.py\", \"make_class\"]]",
   "v1": [
    16371841,
    904550
   ],
   "v2": [
    2007225425307,
    110899639100
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
     "src/attrs/__init__.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/converters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/converters.py\", \"make_class\"]]",
   "v1": [
    16371841,
    904550
   ],
   "v2": [
    2007225425307,
    110899639100
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
     "src/attrs/converters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/exceptions.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/exceptions.py\", \"make_class\"]]",
   "v1": [
    16371841,
    904550
   ],
   "v2": [
    2007225425307,
    110899639100
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
     "src/attrs/exceptions.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/filters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"make_class\"]]",
   "v1": [
    16371841,
    904550
   ],
   "v2": [
    2007225425307,
    110899639100
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
     "src/attrs/filters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"make_class\"]]",
   "v1": [
    16371841,
    904550
   ],
   "v2": [
    2007225425307,
    110899639100
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
     "src/attrs/setters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"make_class\"]]",
   "v1": [
    16371841,
    904550
   ],
   "v2": [
    2007225425307,
    110899639100
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
     "tests/attr_import_star.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/strategies.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/strategies.py\", \"make_class\"]]",
   "v1": [
    16371841,
    904550
   ],
   "v2": [
    2007225425307,
    110899639100
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
     "tests/strategies.py",

```
</details>

## Step 5

In `src/attrs/__init__.py`, `make_class` has exactly one binding: line 3 imports it as `make_class` from `attr`. It uses dynamic namespace tricks, a literal `__all__` at line 31.

Candidate modules so far: 12; statements confirmed: 0, ruled out: 0, modules with no such import: 0, pending: 12. import coverage complete; star coverage complete.

Still to settle: close the namespace of `src/attr/_make.py` for `make_class`; locate the module `attr` imported by `src/attrs/__init__.py`; outline `src/attrs/converters.py` for its `make_class` imports; outline `src/attrs/exceptions.py` for its `make_class` imports; and 8 more.

Next: outline `src/attr/_make.py` filtered to `make_class`, because module `src/attr/_make.py` (task), name `make_class` (task). I expect: a definition there ends the chain (about 95%); a re-export continues the chain to its source (about 5%); no binding at all points at a submodule or an unresolved name (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, list `.`, is more likely to hit the cap (about 20% against under 5%). Plan by outcome: def: list `.`; reexport: list `.`; star: list `.`; none: list `.`.

**Call:** `symbols('src/attr/_make.py', 'make_class')`

**Response**: outcome `def`

```
module src/attr/_make.py lines=3463 dynamic=no all=none
3261 def make_class
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/attr/_make.py",
    "make_class"
   ],
   "desc": "close the namespace of `src/attr/_make.py` for `make_class`"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/__init__.py",
    "attr"
   ],
   "desc": "locate the module `attr` imported by `src/attrs/__init__.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/converters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/converters.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/exceptions.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/exceptions.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/filters.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/setters.py` for its `make_class` imports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/validators.py",
    "attr.validators"
   ],
   "desc": "locate the module `attr.validators` imported by `src/attrs/validators.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "make_class"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/strategies.py",
    "make_class"
   ],
   "desc": "outline `tests/strategies.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "make_class"
   ],
   "desc": "outline `tests/test_dunders.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "make_class"
   ],
   "desc": "outline `tests/test_make.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/utils.py",
    "make_class"
   ],
   "desc": "outline `tests/utils.py` for its `make_class` imports"
  }
 ],
 "candidates": [
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    2945281,
    162819
   ],
   "v2": [
    722196473333,
    39923870076
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
     "src/attrs/__init__.py",
     "attr"
    ],
    [
     "module_path",
     "src/attrs/validators.py",
     "attr.validators"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/_make.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attr/_make.py\", \"make_class\"]]",
   "v1": [
    82708489017,
    4435985564
   ],
   "v2": [
    722196473333,
    39923870076
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     56,
     59
    ],
    "reexport": [
     13,
     472
    ],
    "star": [
     1,
     472
    ],
    "none": [
     5,
     236
    ]
   },
   "serves": [
    [
     "bindings",
     "src/attr/_make.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/converters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/converters.py\", \"make_class\"]]",
   "v1": [
    16883291,
    904550
   ],
   "v2": [
    147426869,
    8140950
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
     "src/attrs/converters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/exceptions.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/exceptions.py\", \"make_class\"]]",
   "v1": [
    16883291,
    904550
   ],
   "v2": [
    147426869,
    8140950
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
     "src/attrs/exceptions.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/filters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"make_class\"]]",
   "v1": [
    16883291,
    904550
   ],
   "v2": [
    147426869,
    8140950
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
     "src/attrs/filters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"make_class\"]]",
   "v1": [
    16883291,
    904550
   ],
   "v2": [
    147426869,
    8140950
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
     "src/attrs/setters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"make_class\"]]",
   "v1": [
    16883291,
    904550
   ],
   "v2": [
    147426869,
    8140950
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
     "tests/attr_import_star.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/strategies.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/strategies.py\", \"make_class\"]]",
   "v1": [
    16883291,
    904550
   ],
   "v2": [
    147426869,
    8140950
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
     "tests/strategies.py",
     "make_class"
    ]
   ]
  },
  {
   "call": 
```
</details>

## Step 6

In `src/attr/_make.py`, `make_class` has exactly one binding: a def at line 3261. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 12; statements confirmed: 1, ruled out: 0, modules with no such import: 0, pending: 11. import coverage complete; star coverage complete.

Open: locate the module `attr` imported by `src/attrs/__init__.py`; outline `src/attrs/converters.py` for its `make_class` imports; outline `src/attrs/exceptions.py` for its `make_class` imports; outline `src/attrs/filters.py` for its `make_class` imports; and 7 more.

Next: list `.`, because `attr` imported by `src/attrs/__init__.py` should live under `.`. I expect: a complete listing settles which files exist (about 80%); a capped listing settles nothing (about 20%). The alternative, outline `src/attrs/converters.py` filtered to `make_class`, serves fewer of the open items. Plan by outcome: complete: outline `src/attrs/converters.py` filtered to `make_class`; cap: outline `src/attrs/converters.py` filtered to `make_class`.

**Call:** `ls('.')`

**Response**: outcome `complete`

```
.git_archival.txt
.github/
.pre-commit-config.yaml
.readthedocs.yaml
CHANGELOG.md
README.md
bench/
changelog.d/
codspeed.yml
docs/
pyproject.toml
src/
tests/
tox.ini
typing_tests/
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/__init__.py",
    "attr"
   ],
   "desc": "locate the module `attr` imported by `src/attrs/__init__.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/converters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/converters.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/exceptions.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/exceptions.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/filters.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/setters.py` for its `make_class` imports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/validators.py",
    "attr.validators"
   ],
   "desc": "locate the module `attr.validators` imported by `src/attrs/validators.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "make_class"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/strategies.py",
    "make_class"
   ],
   "desc": "outline `tests/strategies.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "make_class"
   ],
   "desc": "outline `tests/test_dunders.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "make_class"
   ],
   "desc": "outline `tests/test_make.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/utils.py",
    "make_class"
   ],
   "desc": "outline `tests/utils.py` for its `make_class` imports"
  }
 ],
 "candidates": [
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    2772508,
    162819
   ],
   "v2": [
    138788219,
    8140950
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
     "src/attrs/__init__.py",
     "attr"
    ],
    [
     "module_path",
     "src/attrs/validators.py",
     "attr.validators"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/converters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/converters.py\", \"make_class\"]]",
   "v1": [
    15923441,
    904550
   ],
   "v2": [
    138788219,
    8140950
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
     "src/attrs/converters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/exceptions.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/exceptions.py\", \"make_class\"]]",
   "v1": [
    15923441,
    904550
   ],
   "v2": [
    138788219,
    8140950
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
     "src/attrs/exceptions.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/filters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"make_class\"]]",
   "v1": [
    15923441,
    904550
   ],
   "v2": [
    138788219,
    8140950
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
     "src/attrs/filters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"make_class\"]]",
   "v1": [
    15923441,
    904550
   ],
   "v2": [
    138788219,
    8140950
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
     "src/attrs/setters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"make_class\"]]",
   "v1": [
    15923441,
    904550
   ],
   "v2": [
    138788219,
    8140950
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
     "tests/attr_import_star.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/strategies.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/strategies.py\", \"make_class\"]]",
   "v1": [
    15923441,
    904550
   ],
   "v2": [
    138788219,
    8140950
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
     "tests/strategies.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_dunders.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/test_dunders.py\", \"make_class\"]]",
   "v1": [
    15923441,
    904550
   ],
   "v2": [
    138788219,
    8140950
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
     "tests/test_dunders.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"make_class\"]]",
   "v1": [
    15923441,
    904550
   ],
   "v2": [
    138788219,
    8140950
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,

```
</details>

## Step 7

`.` lists 15 entries (complete): `.github/`, `bench/`, `changelog.d/`, `docs/`, `src/`, `tests/` and 1 more. This is not the branch I planned for that outcome; the open items changed more than expected.

Candidate modules so far: 12; statements confirmed: 1, ruled out: 0, modules with no such import: 0, pending: 11. import coverage complete; star coverage complete.

Open: locate the module `attr` imported by `src/attrs/__init__.py`; outline `src/attrs/converters.py` for its `make_class` imports; outline `src/attrs/exceptions.py` for its `make_class` imports; outline `src/attrs/filters.py` for its `make_class` imports; and 7 more.

Next: outline `src/attr.py` filtered to `make_class`, because `attr` would be `src/attr.py` if that file exists; one call both checks and closes it. I expect: a definition there ends the chain (about 85%); the file does not exist (about 10%); a re-export continues the chain to its source (under 5%); no binding at all points at a submodule or an unresolved name (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `src/attr/validators.py` filtered to `make_class`, scores the same; the seed broke the tie. Plan by outcome: def: outline `src/attr/validators.py` filtered to `make_class`; reexport: outline `src/attr/validators.py` filtered to `make_class`; star: outline `src/attr/validators.py` filtered to `make_class`; none: outline `src/attr/validators.py` filtered to `make_class`; missing: outline `src/attr/validators.py` filtered to `make_class`.

**Call:** `symbols('src/attr.py', 'make_class')`

**Response**: outcome `missing`

```
error: not a python file: src/attr.py
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/__init__.py",
    "attr"
   ],
   "desc": "locate the module `attr` imported by `src/attrs/__init__.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/converters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/converters.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/exceptions.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/exceptions.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/filters.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/setters.py` for its `make_class` imports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/validators.py",
    "attr.validators"
   ],
   "desc": "locate the module `attr.validators` imported by `src/attrs/validators.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "make_class"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/strategies.py",
    "make_class"
   ],
   "desc": "outline `tests/strategies.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "make_class"
   ],
   "desc": "outline `tests/test_dunders.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "make_class"
   ],
   "desc": "outline `tests/test_make.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/utils.py",
    "make_class"
   ],
   "desc": "outline `tests/utils.py` for its `make_class` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attr.py\", \"make_class\"]]",
   "v1": [
    38706427956277,
    2306712493280
   ],
   "v2": [
    18426139660997,
    1153356246640
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     3283,
     3835
    ],
    "reexport": [
     469,
     18880
    ],
    "star": [
     469,
     245440
    ],
    "none": [
     469,
     24544
    ],
    "missing": [
     51,
     520
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attrs/__init__.py",
     "attr"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/validators.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attr/validators.py\", \"make_class\"]]",
   "v1": [
    38706427956277,
    2306712493280
   ],
   "v2": [
    18426139660997,
    1153356246640
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     3283,
     3835
    ],
    "reexport": [
     469,
     18880
    ],
    "star": [
     469,
     245440
    ],
    "none": [
     469,
     24544
    ],
    "missing": [
     51,
     520
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attrs/validators.py",
     "attr.validators"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/converters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/converters.py\", \"make_class\"]]",
   "v1": [
    15923441,
    904550
   ],
   "v2": [
    193762811030713,
    11533562466400
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
     "src/attrs/converters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/exceptions.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/exceptions.py\", \"make_class\"]]",
   "v1": [
    15923441,
    904550
   ],
   "v2": [
    193762811030713,
    11533562466400
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
     "src/attrs/exceptions.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/filters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"make_class\"]]",
   "v1": [
    15923441,
    904550
   ],
   "v2": [
    193762811030713,
    11533562466400
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
     "src/attrs/filters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"make_class\"]]",
   "v1": [
    15923441,
    904550
   ],
   "v2": [
    193762811030713,
    11533562466400
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
     "src/attrs/setters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"make_class\"]]",
   "v1": [
    15923441,
    904550
   ],
   "v2": [
    193762811030713,
    11533562466400
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
     "tests/attr_import_star.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/strategies.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/strategies.py\", \"make_class\"]]",
   "v1": [
    15923441,
    904550
   ],
   "v2": [
    193762811030713,
    11533562466400
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
  
```
</details>

## Step 8

`src/attr.py` does not exist, so that path is ruled out.

Candidate modules so far: 12; statements confirmed: 1, ruled out: 1, modules with no such import: 0, pending: 10. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/__init__.py`:3, `attr` resolves `make_class` to ambiguous(dynamic module).

Outstanding: outline `src/attrs/converters.py` for its `make_class` imports; outline `src/attrs/exceptions.py` for its `make_class` imports; outline `src/attrs/filters.py` for its `make_class` imports; outline `src/attrs/setters.py` for its `make_class` imports; and 6 more.

Next: outline `src/attr/validators.py` filtered to `make_class`, because `attr.validators` would be `src/attr/validators.py` if that file exists; one call both checks and closes it. I expect: a definition there ends the chain (about 85%); the file does not exist (about 10%); a re-export continues the chain to its source (under 5%); no binding at all points at a submodule or an unresolved name (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `src/attrs/converters.py` filtered to `make_class`, is expected to open more follow-up work. Plan by outcome: def: outline `src/attrs/converters.py` filtered to `make_class`; reexport: outline `src/attrs/converters.py` filtered to `make_class`; star: outline `src/attrs/converters.py` filtered to `make_class`; none: outline `src/attrs/converters.py` filtered to `make_class`; missing: outline `src/attrs/converters.py` filtered to `make_class`.

**Call:** `symbols('src/attr/validators.py', 'make_class')`

**Response**: outcome `none`

```
module src/attr/validators.py lines=767 dynamic=no all=static@19
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/converters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/converters.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/exceptions.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/exceptions.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/filters.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/setters.py` for its `make_class` imports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/validators.py",
    "attr.validators"
   ],
   "desc": "locate the module `attr.validators` imported by `src/attrs/validators.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "make_class"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/strategies.py",
    "make_class"
   ],
   "desc": "outline `tests/strategies.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "make_class"
   ],
   "desc": "outline `tests/test_dunders.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "make_class"
   ],
   "desc": "outline `tests/test_make.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/utils.py",
    "make_class"
   ],
   "desc": "outline `tests/utils.py` for its `make_class` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/validators.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attr/validators.py\", \"make_class\"]]",
   "v1": [
    33951981245237,
    2306712493280
   ],
   "v2": [
    169990577475513,
    11533562466400
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     3283,
     3835
    ],
    "reexport": [
     469,
     18880
    ],
    "star": [
     469,
     245440
    ],
    "none": [
     469,
     24544
    ],
    "missing": [
     51,
     520
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attrs/validators.py",
     "attr.validators"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/converters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/converters.py\", \"make_class\"]]",
   "v1": [
    14059041,
    904550
   ],
   "v2": [
    169990577475513,
    11533562466400
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
     "src/attrs/converters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/exceptions.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/exceptions.py\", \"make_class\"]]",
   "v1": [
    14059041,
    904550
   ],
   "v2": [
    169990577475513,
    11533562466400
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
     "src/attrs/exceptions.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/filters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"make_class\"]]",
   "v1": [
    14059041,
    904550
   ],
   "v2": [
    169990577475513,
    11533562466400
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
     "src/attrs/filters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"make_class\"]]",
   "v1": [
    14059041,
    904550
   ],
   "v2": [
    169990577475513,
    11533562466400
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
     "src/attrs/setters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"make_class\"]]",
   "v1": [
    14059041,
    904550
   ],
   "v2": [
    169990577475513,
    11533562466400
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
     "tests/attr_import_star.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/strategies.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/strategies.py\", \"make_class\"]]",
   "v1": [
    14059041,
    904550
   ],
   "v2": [
    169990577475513,
    11533562466400
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
     "tests/strategies.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_dunders.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/test_dunders.py\", \"make_class\"]]",
   "v1": [
    14059041,
    904550
   ],
   "v2": [
    169990577475513,
    11533562466400
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
     "tests/test_dunders.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"make_class\"]]",
   "v1": [
    14059041,
    904550
   ],
   "v2": [
    169990577475513,
    11
```
</details>

## Step 9

`src/attr/validators.py` binds no `make_class` at module level; no star imports; a literal `__all__` at line 19; no dynamic namespace tricks.

Candidate modules so far: 12; statements confirmed: 1, ruled out: 1, modules with no such import: 0, pending: 10. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/__init__.py`:3, `attr` resolves `make_class` to ambiguous(dynamic module).

Still to settle: outline `src/attrs/converters.py` for its `make_class` imports; outline `src/attrs/exceptions.py` for its `make_class` imports; outline `src/attrs/filters.py` for its `make_class` imports; outline `src/attrs/setters.py` for its `make_class` imports; and 6 more.

Next: outline `src/attrs/converters.py` filtered to `make_class`, because `src/attrs/converters.py` had a matching line (step 1); its outline names every `make_class` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/attrs/exceptions.py` filtered to `make_class`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/attrs/exceptions.py` filtered to `make_class`; cap: outline `src/attrs/exceptions.py` filtered to `make_class`.

**Call:** `symbols('src/attrs/converters.py', 'make_class')`

**Response**: outcome `ok`

```
module src/attrs/converters.py lines=4 dynamic=no all=none
3 star <- attr.converters
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/converters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/converters.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/exceptions.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/exceptions.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/filters.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/setters.py` for its `make_class` imports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/validators.py"
   ],
   "desc": "know what `src/attr/validators.py` exports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "make_class"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/strategies.py",
    "make_class"
   ],
   "desc": "outline `tests/strategies.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "make_class"
   ],
   "desc": "outline `tests/test_dunders.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "make_class"
   ],
   "desc": "outline `tests/test_make.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/utils.py",
    "make_class"
   ],
   "desc": "outline `tests/utils.py` for its `make_class` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attrs/converters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/converters.py\", \"make_class\"]]",
   "v1": [
    13099191,
    904550
   ],
   "v2": [
    6558641,
    452275
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
     "src/attrs/converters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/exceptions.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/exceptions.py\", \"make_class\"]]",
   "v1": [
    13099191,
    904550
   ],
   "v2": [
    6558641,
    452275
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
     "src/attrs/exceptions.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/filters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"make_class\"]]",
   "v1": [
    13099191,
    904550
   ],
   "v2": [
    6558641,
    452275
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
     "src/attrs/filters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"make_class\"]]",
   "v1": [
    13099191,
    904550
   ],
   "v2": [
    6558641,
    452275
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
     "src/attrs/setters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"make_class\"]]",
   "v1": [
    13099191,
    904550
   ],
   "v2": [
    6558641,
    452275
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
     "tests/attr_import_star.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/strategies.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/strategies.py\", \"make_class\"]]",
   "v1": [
    13099191,
    904550
   ],
   "v2": [
    6558641,
    452275
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
     "tests/strategies.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_dunders.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/test_dunders.py\", \"make_class\"]]",
   "v1": [
    13099191,
    904550
   ],
   "v2": [
    6558641,
    452275
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
     "tests/test_dunders.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"make_class\"]]",
   "v1": [
    13099191,
    904550
   ],
   "v2": [
    6558641,
    452275
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
     "tests/test_make.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/utils.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/utils.py\", \"make_class\"]]",
   "v1": [
    13099191,
    904550
   ],
   "v2": [
    6558641,
    452275
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
     "tests/utils.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "read('src/attr/validators.py', 19, 30)",
   "key": "[\"read\", [\"src/attr/validators.py\", 19, 30]]",
   "v1": [
    8426177,
    578912
   ]
```
</details>

## Step 10

`src/attrs/converters.py` binds no `make_class` at module level; 1 star import(s): `attr.converters`; no `__all__`; no dynamic namespace tricks.

Candidate modules so far: 12; statements confirmed: 1, ruled out: 1, modules with no such import: 0, pending: 10. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/__init__.py`:3, `attr` resolves `make_class` to ambiguous(dynamic module).

Still to settle: locate the module `attr.converters` imported by `src/attrs/converters.py`; outline `src/attrs/exceptions.py` for its `make_class` imports; outline `src/attrs/filters.py` for its `make_class` imports; outline `src/attrs/setters.py` for its `make_class` imports; and 6 more.

Next: outline `src/attrs/exceptions.py` filtered to `make_class`, because `src/attrs/exceptions.py` had a matching line (step 1); its outline names every `make_class` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/attr/converters.py` filtered to `make_class`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/attr/converters.py` filtered to `make_class`; cap: outline `src/attr/converters.py` filtered to `make_class`.

**Call:** `symbols('src/attrs/exceptions.py', 'make_class')`

**Response**: outcome `ok`

```
module src/attrs/exceptions.py lines=4 dynamic=no all=none
3 star <- attr.exceptions
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/converters.py",
    "attr.converters"
   ],
   "desc": "locate the module `attr.converters` imported by `src/attrs/converters.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/exceptions.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/exceptions.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/filters.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/setters.py` for its `make_class` imports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/validators.py"
   ],
   "desc": "know what `src/attr/validators.py` exports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "make_class"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/strategies.py",
    "make_class"
   ],
   "desc": "outline `tests/strategies.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "make_class"
   ],
   "desc": "outline `tests/test_dunders.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "make_class"
   ],
   "desc": "outline `tests/test_make.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/utils.py",
    "make_class"
   ],
   "desc": "outline `tests/utils.py` for its `make_class` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/converters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attr/converters.py\", \"make_class\"]]",
   "v1": [
    32808506719797,
    2306712493280
   ],
   "v2": [
    164273204848313,
    11533562466400
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     3283,
     3835
    ],
    "reexport": [
     469,
     18880
    ],
    "star": [
     469,
     245440
    ],
    "none": [
     469,
     24544
    ],
    "missing": [
     51,
     520
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attrs/converters.py",
     "attr.converters"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/exceptions.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/exceptions.py\", \"make_class\"]]",
   "v1": [
    13610641,
    904550
   ],
   "v2": [
    164273204848313,
    11533562466400
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
     "src/attrs/exceptions.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/filters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"make_class\"]]",
   "v1": [
    13610641,
    904550
   ],
   "v2": [
    164273204848313,
    11533562466400
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
     "src/attrs/filters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"make_class\"]]",
   "v1": [
    13610641,
    904550
   ],
   "v2": [
    164273204848313,
    11533562466400
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
     "src/attrs/setters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"make_class\"]]",
   "v1": [
    13610641,
    904550
   ],
   "v2": [
    164273204848313,
    11533562466400
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
     "tests/attr_import_star.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/strategies.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/strategies.py\", \"make_class\"]]",
   "v1": [
    13610641,
    904550
   ],
   "v2": [
    164273204848313,
    11533562466400
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
     "tests/strategies.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_dunders.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/test_dunders.py\", \"make_class\"]]",
   "v1": [
    13610641,
    904550
   ],
   "v2": [
    164273204848313,
    11533562466400
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
     "tests/test_dunders.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"make_class\"]]",
   "v1": [
    13610641,
    904550
   ],
   "v2": [
    164273204848313,
    11533562466400
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
     "tests/test_make.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/utils.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/utils.py\", \"make_class\"]]",
   "v1": [
    13610641,
    904550
   ],
   "v2": [
    164273204848313,
    11533562466400
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {

```
</details>

## Step 11

`src/attrs/exceptions.py` binds no `make_class` at module level; 1 star import(s): `attr.exceptions`; no `__all__`; no dynamic namespace tricks.

Candidate modules so far: 12; statements confirmed: 1, ruled out: 1, modules with no such import: 0, pending: 10. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/__init__.py`:3, `attr` resolves `make_class` to ambiguous(dynamic module).

Outstanding: locate the module `attr.converters` imported by `src/attrs/converters.py`; locate the module `attr.exceptions` imported by `src/attrs/exceptions.py`; outline `src/attrs/filters.py` for its `make_class` imports; outline `src/attrs/setters.py` for its `make_class` imports; and 6 more.

Next: outline `src/attr/converters.py` filtered to `make_class`, because `attr.converters` would be `src/attr/converters.py` if that file exists; one call both checks and closes it. I expect: a definition there ends the chain (about 85%); the file does not exist (about 10%); a re-export continues the chain to its source (under 5%); no binding at all points at a submodule or an unresolved name (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `src/attr/exceptions.py` filtered to `make_class`, scores the same; the seed broke the tie. Plan by outcome: def: outline `src/attr/exceptions.py` filtered to `make_class`; reexport: outline `src/attr/exceptions.py` filtered to `make_class`; star: outline `src/attr/exceptions.py` filtered to `make_class`; none: outline `src/attr/exceptions.py` filtered to `make_class`; missing: list `src/attr`.

**Call:** `symbols('src/attr/converters.py', 'make_class')`

**Response**: outcome `none`

```
module src/attr/converters.py lines=161 dynamic=no all=static@11
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/converters.py",
    "attr.converters"
   ],
   "desc": "locate the module `attr.converters` imported by `src/attrs/converters.py`"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/exceptions.py",
    "attr.exceptions"
   ],
   "desc": "locate the module `attr.exceptions` imported by `src/attrs/exceptions.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/filters.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/setters.py` for its `make_class` imports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/validators.py"
   ],
   "desc": "know what `src/attr/validators.py` exports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "make_class"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/strategies.py",
    "make_class"
   ],
   "desc": "outline `tests/strategies.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "make_class"
   ],
   "desc": "outline `tests/test_dunders.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "make_class"
   ],
   "desc": "outline `tests/test_make.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/utils.py",
    "make_class"
   ],
   "desc": "outline `tests/utils.py` for its `make_class` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/converters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attr/converters.py\", \"make_class\"]]",
   "v1": [
    34112766412117,
    2306712493280
   ],
   "v2": [
    3736738732120830559,
    267486380720748800
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     3283,
     3835
    ],
    "reexport": [
     469,
     18880
    ],
    "star": [
     469,
     245440
    ],
    "none": [
     469,
     24544
    ],
    "missing": [
     51,
     520
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attrs/converters.py",
     "attr.converters"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/exceptions.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attr/exceptions.py\", \"make_class\"]]",
   "v1": [
    34112766412117,
    2306712493280
   ],
   "v2": [
    3736738732120830559,
    267486380720748800
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     3283,
     3835
    ],
    "reexport": [
     469,
     18880
    ],
    "star": [
     469,
     245440
    ],
    "none": [
     469,
     24544
    ],
    "missing": [
     51,
     520
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attrs/exceptions.py",
     "attr.exceptions"
    ]
   ]
  },
  {
   "call": "ls('src/attr')",
   "key": "[\"ls\", [\"src/attr\"]]",
   "v1": [
    59050457,
    4034293
   ],
   "v2": [
    8858093189,
    605143950
   ],
   "p_cap": [
    5,
    223
   ],
   "forecast": {
    "complete": [
     218,
     223
    ],
    "cap": [
     5,
     223
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attrs/converters.py",
     "attr.converters"
    ],
    [
     "module_path",
     "src/attrs/exceptions.py",
     "attr.exceptions"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/filters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"make_class\"]]",
   "v1": [
    14122091,
    904550
   ],
   "v2": [
    2956557143,
    201714650
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
     "src/attrs/filters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"make_class\"]]",
   "v1": [
    14122091,
    904550
   ],
   "v2": [
    2956557143,
    201714650
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
     "src/attrs/setters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"make_class\"]]",
   "v1": [
    14122091,
    904550
   ],
   "v2": [
    2956557143,
    201714650
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
     "tests/attr_import_star.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/strategies.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/strategies.py\", \"make_class\"]]",
   "v1": [
    14122091,
    904550
   ],
   "v2": [
    2956557143,
    201714650
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
     "tests/strategies.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_dunders.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/test_dunders.py\", \"make_class\"]]",
   "v1": [
    14122091,
    904550
   ],
   "v2": [
    2956557143,
    201714650
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
     "tests/test_dunders.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'make_class')",
   "key": "[\"sym
```
</details>

## Step 12

`src/attr/converters.py` binds no `make_class` at module level; no star imports; a literal `__all__` at line 11; no dynamic namespace tricks.

Candidate modules so far: 12; statements confirmed: 1, ruled out: 1, modules with no such import: 0, pending: 10. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/__init__.py`:3, `attr` resolves `make_class` to ambiguous(dynamic module).

Open: know what `src/attr/converters.py` exports; locate the module `attr.exceptions` imported by `src/attrs/exceptions.py`; outline `src/attrs/filters.py` for its `make_class` imports; outline `src/attrs/setters.py` for its `make_class` imports; and 6 more.

Next: outline `src/attr/exceptions.py` filtered to `make_class`, because `attr.exceptions` would be `src/attr/exceptions.py` if that file exists; one call both checks and closes it. I expect: a definition there ends the chain (about 85%); the file does not exist (about 10%); a re-export continues the chain to its source (under 5%); no binding at all points at a submodule or an unresolved name (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `src/attrs/filters.py` filtered to `make_class`, is expected to open more follow-up work. Plan by outcome: def: outline `src/attrs/filters.py` filtered to `make_class`; reexport: outline `src/attrs/filters.py` filtered to `make_class`; star: outline `src/attrs/filters.py` filtered to `make_class`; none: outline `src/attrs/filters.py` filtered to `make_class`; missing: outline `src/attrs/filters.py` filtered to `make_class`.

**Call:** `symbols('src/attr/exceptions.py', 'make_class')`

**Response**: outcome `none`

```
module src/attr/exceptions.py lines=96 dynamic=no all=none
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/converters.py"
   ],
   "desc": "know what `src/attr/converters.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/exceptions.py",
    "attr.exceptions"
   ],
   "desc": "locate the module `attr.exceptions` imported by `src/attrs/exceptions.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/filters.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/setters.py` for its `make_class` imports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/validators.py"
   ],
   "desc": "know what `src/attr/validators.py` exports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "make_class"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/strategies.py",
    "make_class"
   ],
   "desc": "outline `tests/strategies.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "make_class"
   ],
   "desc": "outline `tests/test_dunders.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "make_class"
   ],
   "desc": "outline `tests/test_make.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/utils.py",
    "make_class"
   ],
   "desc": "outline `tests/utils.py` for its `make_class` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/exceptions.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attr/exceptions.py\", \"make_class\"]]",
   "v1": [
    31665032194357,
    2306712493280
   ],
   "v2": [
    158555832221113,
    11533562466400
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     3283,
     3835
    ],
    "reexport": [
     469,
     18880
    ],
    "star": [
     469,
     245440
    ],
    "none": [
     469,
     24544
    ],
    "missing": [
     51,
     520
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attrs/exceptions.py",
     "attr.exceptions"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/filters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"make_class\"]]",
   "v1": [
    13162241,
    904550
   ],
   "v2": [
    158555832221113,
    11533562466400
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
     "src/attrs/filters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"make_class\"]]",
   "v1": [
    13162241,
    904550
   ],
   "v2": [
    158555832221113,
    11533562466400
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
     "src/attrs/setters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"make_class\"]]",
   "v1": [
    13162241,
    904550
   ],
   "v2": [
    158555832221113,
    11533562466400
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
     "tests/attr_import_star.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/strategies.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/strategies.py\", \"make_class\"]]",
   "v1": [
    13162241,
    904550
   ],
   "v2": [
    158555832221113,
    11533562466400
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
     "tests/strategies.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_dunders.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/test_dunders.py\", \"make_class\"]]",
   "v1": [
    13162241,
    904550
   ],
   "v2": [
    158555832221113,
    11533562466400
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
     "tests/test_dunders.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"make_class\"]]",
   "v1": [
    13162241,
    904550
   ],
   "v2": [
    158555832221113,
    11533562466400
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
     "tests/test_make.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/utils.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/utils.py\", \"make_class\"]]",
   "v1": [
    13162241,
    904550
   ],
   "v2": [
    158555832221113,
    11533562466400
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
     "tests/utils.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    8466529,
    578912
   ],
   "v2": [
    15940643245301,
    1153356246640
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
  
```
</details>

## Step 13

`src/attr/exceptions.py` binds no `make_class` at module level; no star imports; no `__all__`; no dynamic namespace tricks.

Candidate modules so far: 12; statements confirmed: 1, ruled out: 2, modules with no such import: 0, pending: 9. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/exceptions.py`:3, star import of `attr.exceptions`, which does not export `make_class`.

Outstanding: know what `src/attr/converters.py` exports; outline `src/attrs/filters.py` for its `make_class` imports; outline `src/attrs/setters.py` for its `make_class` imports; know what `src/attr/validators.py` exports; and 5 more.

Next: outline `src/attrs/filters.py` filtered to `make_class`, because `src/attrs/filters.py` had a matching line (step 1); its outline names every `make_class` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/attrs/setters.py` filtered to `make_class`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/attrs/setters.py` filtered to `make_class`; cap: outline `src/attrs/setters.py` filtered to `make_class`.

**Call:** `symbols('src/attrs/filters.py', 'make_class')`

**Response**: outcome `ok`

```
module src/attrs/filters.py lines=4 dynamic=no all=none
3 star <- attr.filters
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/converters.py"
   ],
   "desc": "know what `src/attr/converters.py` exports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/filters.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/setters.py` for its `make_class` imports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/validators.py"
   ],
   "desc": "know what `src/attr/validators.py` exports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "make_class"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/strategies.py",
    "make_class"
   ],
   "desc": "outline `tests/strategies.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "make_class"
   ],
   "desc": "outline `tests/test_dunders.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "make_class"
   ],
   "desc": "outline `tests/test_make.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/utils.py",
    "make_class"
   ],
   "desc": "outline `tests/utils.py` for its `make_class` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attrs/filters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"make_class\"]]",
   "v1": [
    11297841,
    904550
   ],
   "v2": [
    5657966,
    452275
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
     "src/attrs/filters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"make_class\"]]",
   "v1": [
    11297841,
    904550
   ],
   "v2": [
    5657966,
    452275
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
     "src/attrs/setters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"make_class\"]]",
   "v1": [
    11297841,
    904550
   ],
   "v2": [
    5657966,
    452275
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
     "tests/attr_import_star.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/strategies.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/strategies.py\", \"make_class\"]]",
   "v1": [
    11297841,
    904550
   ],
   "v2": [
    5657966,
    452275
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
     "tests/strategies.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_dunders.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/test_dunders.py\", \"make_class\"]]",
   "v1": [
    11297841,
    904550
   ],
   "v2": [
    5657966,
    452275
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
     "tests/test_dunders.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"make_class\"]]",
   "v1": [
    11297841,
    904550
   ],
   "v2": [
    5657966,
    452275
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
     "tests/test_make.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/utils.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/utils.py\", \"make_class\"]]",
   "v1": [
    11297841,
    904550
   ],
   "v2": [
    5657966,
    452275
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
     "tests/utils.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    7273313,
    578912
   ],
   "v2": [
    182122281,
    14472800
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/converters.py"
    ]
   ]
  },
  {
   "call": "read('src/attr/validators.py', 19, 30)",
   "key": "[\"read\", [\"src/attr/validators.py\", 19, 30]]",
   "v1": [
    7273313,
    578912
   ],
   "v2": [
    182122281,
    14472800
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/validators.py"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/attrs/filters.py', 'make_class')",
  "key": "[\"symbols\", [\"src/attrs/filters.py\", \"make_class\"]]",
  "provenance": "`src/attrs/filters.py` had a matching line (step 1); its outline names every `make_class` import exactly",
  "v2": [
   5657966,
   452275
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
  "ok": "[\"symbols\", [\"src/attrs/setters.py\", \"make_class\"]]",
  "cap": "[\
```
</details>

## Step 14

`src/attrs/filters.py` binds no `make_class` at module level; 1 star import(s): `attr.filters`; no `__all__`; no dynamic namespace tricks.

Candidate modules so far: 12; statements confirmed: 1, ruled out: 2, modules with no such import: 0, pending: 9. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/exceptions.py`:3, star import of `attr.exceptions`, which does not export `make_class`.

Open: know what `src/attr/converters.py` exports; locate the module `attr.filters` imported by `src/attrs/filters.py`; outline `src/attrs/setters.py` for its `make_class` imports; know what `src/attr/validators.py` exports; and 5 more.

Next: outline `src/attrs/setters.py` filtered to `make_class`, because `src/attrs/setters.py` had a matching line (step 1); its outline names every `make_class` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/attr/filters.py` filtered to `make_class`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/attr/filters.py` filtered to `make_class`; cap: outline `src/attr/filters.py` filtered to `make_class`.

**Call:** `symbols('src/attrs/setters.py', 'make_class')`

**Response**: outcome `ok`

```
module src/attrs/setters.py lines=4 dynamic=no all=none
3 star <- attr.setters
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/converters.py"
   ],
   "desc": "know what `src/attr/converters.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/filters.py",
    "attr.filters"
   ],
   "desc": "locate the module `attr.filters` imported by `src/attrs/filters.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "make_class"
   ],
   "desc": "outline `src/attrs/setters.py` for its `make_class` imports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/validators.py"
   ],
   "desc": "know what `src/attr/validators.py` exports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "make_class"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/strategies.py",
    "make_class"
   ],
   "desc": "outline `tests/strategies.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "make_class"
   ],
   "desc": "outline `tests/test_dunders.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "make_class"
   ],
   "desc": "outline `tests/test_make.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/utils.py",
    "make_class"
   ],
   "desc": "outline `tests/utils.py` for its `make_class` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/filters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attr/filters.py\", \"make_class\"]]",
   "v1": [
    28214845175637,
    2306712493280
   ],
   "v2": [
    141304897127513,
    11533562466400
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     3283,
     3835
    ],
    "reexport": [
     469,
     18880
    ],
    "star": [
     469,
     245440
    ],
    "none": [
     469,
     24544
    ],
    "missing": [
     51,
     520
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attrs/filters.py",
     "attr.filters"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"make_class\"]]",
   "v1": [
    11809291,
    904550
   ],
   "v2": [
    141304897127513,
    11533562466400
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
     "src/attrs/setters.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"make_class\"]]",
   "v1": [
    11809291,
    904550
   ],
   "v2": [
    141304897127513,
    11533562466400
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
     "tests/attr_import_star.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/strategies.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/strategies.py\", \"make_class\"]]",
   "v1": [
    11809291,
    904550
   ],
   "v2": [
    141304897127513,
    11533562466400
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
     "tests/strategies.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_dunders.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/test_dunders.py\", \"make_class\"]]",
   "v1": [
    11809291,
    904550
   ],
   "v2": [
    141304897127513,
    11533562466400
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
     "tests/test_dunders.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"make_class\"]]",
   "v1": [
    11809291,
    904550
   ],
   "v2": [
    141304897127513,
    11533562466400
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
     "tests/test_make.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/utils.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/utils.py\", \"make_class\"]]",
   "v1": [
    11809291,
    904550
   ],
   "v2": [
    141304897127513,
    11533562466400
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
     "tests/utils.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    7600641,
    578912
   ],
   "v2": [
    14215549735941,
    1153356246640
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/converters.py"
    ]
   ]
  },
  {
   "call": "read('src/attr/validators.py', 19, 30)",
   "key": "[\"read\", [\"src/attr/validators.py\", 19, 30]]",
   "v1": [
    7600641,
    578912
   ],
   "v2": [
    14215549735941,
    1153356246640
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/validators.py"
    ]
   ]
  },
  {
   "call": "ls('src/attr')",
   "key": "[\"ls\", [\"src/attr\"]]",
   "v1": [
    52679207,
    4034293
   ],
   "v2": [
    33588528526889229,
    257198443000720
```
</details>

## Step 15

`src/attrs/setters.py` binds no `make_class` at module level; 1 star import(s): `attr.setters`; no `__all__`; no dynamic namespace tricks.

Candidate modules so far: 12; statements confirmed: 1, ruled out: 2, modules with no such import: 0, pending: 9. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/exceptions.py`:3, star import of `attr.exceptions`, which does not export `make_class`.

Still to settle: know what `src/attr/converters.py` exports; locate the module `attr.filters` imported by `src/attrs/filters.py`; locate the module `attr.setters` imported by `src/attrs/setters.py`; know what `src/attr/validators.py` exports; and 5 more.

Next: outline `src/attr/filters.py` filtered to `make_class`, because `attr.filters` would be `src/attr/filters.py` if that file exists; one call both checks and closes it. I expect: a definition there ends the chain (about 85%); the file does not exist (about 10%); a re-export continues the chain to its source (under 5%); no binding at all points at a submodule or an unresolved name (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `src/attr/setters.py` filtered to `make_class`, scores the same; the seed broke the tie. Plan by outcome: def: outline `src/attr/setters.py` filtered to `make_class`; reexport: outline `src/attr/setters.py` filtered to `make_class`; star: outline `src/attr/setters.py` filtered to `make_class`; none: outline `src/attr/setters.py` filtered to `make_class`; missing: list `src/attr`.

**Call:** `symbols('src/attr/filters.py', 'make_class')`

**Response**: outcome `none`

```
module src/attr/filters.py lines=73 dynamic=no all=none
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/converters.py"
   ],
   "desc": "know what `src/attr/converters.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/filters.py",
    "attr.filters"
   ],
   "desc": "locate the module `attr.filters` imported by `src/attrs/filters.py`"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/setters.py",
    "attr.setters"
   ],
   "desc": "locate the module `attr.setters` imported by `src/attrs/setters.py`"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/validators.py"
   ],
   "desc": "know what `src/attr/validators.py` exports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "make_class"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/strategies.py",
    "make_class"
   ],
   "desc": "outline `tests/strategies.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "make_class"
   ],
   "desc": "outline `tests/test_dunders.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "make_class"
   ],
   "desc": "outline `tests/test_make.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/utils.py",
    "make_class"
   ],
   "desc": "outline `tests/utils.py` for its `make_class` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/filters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attr/filters.py\", \"make_class\"]]",
   "v1": [
    29519104867957,
    2306712493280
   ],
   "v2": [
    3204057739460036959,
    267486380720748800
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     3283,
     3835
    ],
    "reexport": [
     469,
     18880
    ],
    "star": [
     469,
     245440
    ],
    "none": [
     469,
     24544
    ],
    "missing": [
     51,
     520
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attrs/filters.py",
     "attr.filters"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/setters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attr/setters.py\", \"make_class\"]]",
   "v1": [
    29519104867957,
    2306712493280
   ],
   "v2": [
    3204057739460036959,
    267486380720748800
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     3283,
     3835
    ],
    "reexport": [
     469,
     18880
    ],
    "star": [
     469,
     245440
    ],
    "none": [
     469,
     24544
    ],
    "missing": [
     51,
     520
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attrs/setters.py",
     "attr.setters"
    ]
   ]
  },
  {
   "call": "ls('src/attr')",
   "key": "[\"ls\", [\"src/attr\"]]",
   "v1": [
    51016436,
    4034293
   ],
   "v2": [
    7652990039,
    605143950
   ],
   "p_cap": [
    5,
    223
   ],
   "forecast": {
    "complete": [
     218,
     223
    ],
    "cap": [
     5,
     223
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attrs/filters.py",
     "attr.filters"
    ],
    [
     "module_path",
     "src/attrs/setters.py",
     "attr.setters"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"make_class\"]]",
   "v1": [
    12320741,
    904550
   ],
   "v2": [
    2554856093,
    201714650
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
     "tests/attr_import_star.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/strategies.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/strategies.py\", \"make_class\"]]",
   "v1": [
    12320741,
    904550
   ],
   "v2": [
    2554856093,
    201714650
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
     "tests/strategies.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_dunders.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/test_dunders.py\", \"make_class\"]]",
   "v1": [
    12320741,
    904550
   ],
   "v2": [
    2554856093,
    201714650
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
     "tests/test_dunders.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"make_class\"]]",
   "v1": [
    12320741,
    904550
   ],
   "v2": [
    2554856093,
    201714650
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
     "tests/test_make.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/utils.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/utils.py\", \"make_class\"]]",
   "v1": [
    12320741,
    904550
   ],
   "v2": [
    2554856093,
    201714650
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
     "tests/utils.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+make_class\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+make_class\\\\b\", \".\"]]",
   "v1": [
    1385863,
    108546
   ],
   "v2": [
    10252150991,
    806858600
   ],
   "p_cap": [
    1,
    24
   ],
   "forecast": {
    "zero": [
     1,
     24
    ],
    "mid": [
     11,
  
```
</details>

## Step 16

`src/attr/filters.py` binds no `make_class` at module level; no star imports; no `__all__`; no dynamic namespace tricks.

Candidate modules so far: 12; statements confirmed: 1, ruled out: 3, modules with no such import: 0, pending: 8. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/filters.py`:3, star import of `attr.filters`, which does not export `make_class`.

Outstanding: know what `src/attr/converters.py` exports; locate the module `attr.setters` imported by `src/attrs/setters.py`; know what `src/attr/validators.py` exports; outline `tests/attr_import_star.py` for its `make_class` imports; and 4 more.

Next: outline `src/attr/setters.py` filtered to `make_class`, because `attr.setters` would be `src/attr/setters.py` if that file exists; one call both checks and closes it. I expect: a definition there ends the chain (about 85%); the file does not exist (about 10%); a re-export continues the chain to its source (under 5%); no binding at all points at a submodule or an unresolved name (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `tests/attr_import_star.py` filtered to `make_class`, is expected to open more follow-up work. Plan by outcome: def: outline `tests/attr_import_star.py` filtered to `make_class`; reexport: outline `tests/attr_import_star.py` filtered to `make_class`; star: outline `tests/attr_import_star.py` filtered to `make_class`; none: outline `tests/attr_import_star.py` filtered to `make_class`; missing: outline `tests/attr_import_star.py` filtered to `make_class`.

**Call:** `symbols('src/attr/setters.py', 'make_class')`

**Response**: outcome `none`

```
module src/attr/setters.py lines=83 dynamic=no all=none
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/converters.py"
   ],
   "desc": "know what `src/attr/converters.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/setters.py",
    "attr.setters"
   ],
   "desc": "locate the module `attr.setters` imported by `src/attrs/setters.py`"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/validators.py"
   ],
   "desc": "know what `src/attr/validators.py` exports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "make_class"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/strategies.py",
    "make_class"
   ],
   "desc": "outline `tests/strategies.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "make_class"
   ],
   "desc": "outline `tests/test_dunders.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "make_class"
   ],
   "desc": "outline `tests/test_make.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/utils.py",
    "make_class"
   ],
   "desc": "outline `tests/utils.py` for its `make_class` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/setters.py', 'make_class')",
   "key": "[\"symbols\", [\"src/attr/setters.py\", \"make_class\"]]",
   "v1": [
    24764658156917,
    2306712493280
   ],
   "v2": [
    124053962033913,
    11533562466400
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     3283,
     3835
    ],
    "reexport": [
     469,
     18880
    ],
    "star": [
     469,
     245440
    ],
    "none": [
     469,
     24544
    ],
    "missing": [
     51,
     520
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attrs/setters.py",
     "attr.setters"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"make_class\"]]",
   "v1": [
    10456341,
    904550
   ],
   "v2": [
    124053962033913,
    11533562466400
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
     "tests/attr_import_star.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/strategies.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/strategies.py\", \"make_class\"]]",
   "v1": [
    10456341,
    904550
   ],
   "v2": [
    124053962033913,
    11533562466400
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
     "tests/strategies.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_dunders.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/test_dunders.py\", \"make_class\"]]",
   "v1": [
    10456341,
    904550
   ],
   "v2": [
    124053962033913,
    11533562466400
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
     "tests/test_dunders.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"make_class\"]]",
   "v1": [
    10456341,
    904550
   ],
   "v2": [
    124053962033913,
    11533562466400
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
     "tests/test_make.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/utils.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/utils.py\", \"make_class\"]]",
   "v1": [
    10456341,
    904550
   ],
   "v2": [
    124053962033913,
    11533562466400
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
     "tests/utils.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    6734753,
    578912
   ],
   "v2": [
    12490456226581,
    1153356246640
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/converters.py"
    ]
   ]
  },
  {
   "call": "read('src/attr/validators.py', 19, 30)",
   "key": "[\"read\", [\"src/attr/validators.py\", 19, 30]]",
   "v1": [
    6734753,
    578912
   ],
   "v2": [
    12490456226581,
    1153356246640
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/validators.py"
    ]
   ]
  },
  {
   "call": "ls('src/attr')",
   "key": "[\"ls\", [\"src/attr\"]]",
   "v1": [
    46645050,
    4034293
   ],
   "v2": [
    29741570001016429,
    2571984430007200
   ],
   "p_cap": [
    5,
    223
   ],
   "forecast": {
    "complete": [
     218,
     223
    ],
    "cap": [
     5,
     223
    ]
   },
   "serves": [
    [
     "module_path",
     "src/attrs/setters.py",
     "attr.setters"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+make_class\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+make_class\\\\b\", \".\"]]",
   "v1": [
    2523271,
    217092
   ],
   "v2": [
    1601928610509593,
    138402749596800
   ],
   "p_cap": [
    1,
    24
   ],
   "forecast": {
    "zero": [
     1,
     24
    ],
    "mid": [
     1
```
</details>

## Step 17

`src/attr/setters.py` binds no `make_class` at module level; no star imports; no `__all__`; no dynamic namespace tricks.

Candidate modules so far: 12; statements confirmed: 1, ruled out: 4, modules with no such import: 0, pending: 7. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/setters.py`:3, star import of `attr.setters`, which does not export `make_class`.

Still to settle: know what `src/attr/converters.py` exports; know what `src/attr/validators.py` exports; outline `tests/attr_import_star.py` for its `make_class` imports; outline `tests/strategies.py` for its `make_class` imports; and 3 more.

Next: outline `tests/attr_import_star.py` filtered to `make_class`, because `tests/attr_import_star.py` had a matching line (step 1); its outline names every `make_class` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `tests/strategies.py` filtered to `make_class`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `tests/strategies.py` filtered to `make_class`; cap: outline `tests/strategies.py` filtered to `make_class`.

**Call:** `symbols('tests/attr_import_star.py', 'make_class')`

**Response**: outcome `ok`

```
module tests/attr_import_star.py lines=10 dynamic=no all=none
4 star <- attr
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/converters.py"
   ],
   "desc": "know what `src/attr/converters.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/validators.py"
   ],
   "desc": "know what `src/attr/validators.py` exports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "make_class"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/strategies.py",
    "make_class"
   ],
   "desc": "outline `tests/strategies.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "make_class"
   ],
   "desc": "outline `tests/test_dunders.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "make_class"
   ],
   "desc": "outline `tests/test_make.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/utils.py",
    "make_class"
   ],
   "desc": "outline `tests/utils.py` for its `make_class` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/attr_import_star.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"make_class\"]]",
   "v1": [
    8591941,
    904550
   ],
   "v2": [
    4305016,
    452275
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
     "tests/attr_import_star.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/strategies.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/strategies.py\", \"make_class\"]]",
   "v1": [
    8591941,
    904550
   ],
   "v2": [
    4305016,
    452275
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
     "tests/strategies.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_dunders.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/test_dunders.py\", \"make_class\"]]",
   "v1": [
    8591941,
    904550
   ],
   "v2": [
    4305016,
    452275
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
     "tests/test_dunders.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"make_class\"]]",
   "v1": [
    8591941,
    904550
   ],
   "v2": [
    4305016,
    452275
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
     "tests/test_make.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/utils.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/utils.py\", \"make_class\"]]",
   "v1": [
    8591941,
    904550
   ],
   "v2": [
    4305016,
    452275
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
     "tests/utils.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    5541537,
    578912
   ],
   "v2": [
    138827881,
    14472800
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/converters.py"
    ]
   ]
  },
  {
   "call": "read('src/attr/validators.py', 19, 30)",
   "key": "[\"read\", [\"src/attr/validators.py\", 19, 30]]",
   "v1": [
    5541537,
    578912
   ],
   "v2": [
    138827881,
    14472800
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/validators.py"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/attr_import_star.py', 'make_class')",
  "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"make_class\"]]",
  "provenance": "`tests/attr_import_star.py` had a matching line (step 1); its outline names every `make_class` import exactly",
  "v2": [
   4305016,
   452275
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
  "ok": "[\"symbols\", [\"tests/strategies.py\", \"make_class\"]]",
  "cap": "[\"symbols\", [\"tests/strategies.py\", \"make_class\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"tests/attr_import_star.py\", \"make_class\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 17,
   "path": "tests/attr_import_star.py",
   "filter": "make_class",
   "header": {
    "lines": 10,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/attr_import_star.py",
     "name": "*",
     "line": 4,
     "kind": "star",
     "src": "attr",
     "src_name": null,
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
    "src/attr/__init__.py",
    16,
    "in",
    "`._make` resolves `make_class` to the target"
   ],
   [
    "src/attrs/__init__.py",
    3,
    "out",
    "`attr` resolves `make_class` to ambiguous(dynamic module)"
   ],
   [
    "src/attrs/converters.py",
    3,
    "pending",
    ""
   ],
   [
    "src/attrs/exceptions.py",
    3,
    "out",
    "star import of `attr.exceptions`, which does not export `make_class`"
   ],
   [
    "src/attrs/filters.py",
    3,
    "out",
    "star import of `attr.filters`, which does not export `make_class`"

```
</details>

## Step 18

`tests/attr_import_star.py` binds no `make_class` at module level; 1 star import(s): `attr`; no `__all__`; no dynamic namespace tricks.

Candidate modules so far: 12; statements confirmed: 1, ruled out: 4, modules with no such import: 0, pending: 7. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/setters.py`:3, star import of `attr.setters`, which does not export `make_class`.

Open: know what `src/attr/converters.py` exports; know what `src/attr/validators.py` exports; know what `src/attr/__init__.py` exports; outline `tests/strategies.py` for its `make_class` imports; and 3 more.

Next: outline `tests/strategies.py` filtered to `make_class`, because `tests/strategies.py` had a matching line (step 1); its outline names every `make_class` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `tests/test_dunders.py` filtered to `make_class`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `tests/test_dunders.py` filtered to `make_class`; cap: outline `tests/test_dunders.py` filtered to `make_class`.

**Call:** `symbols('tests/strategies.py', 'make_class')`

**Response**: outcome `ok`

```
module tests/strategies.py lines=219 dynamic=no all=none
17 from make_class <- .utils make_class
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/converters.py"
   ],
   "desc": "know what `src/attr/converters.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/validators.py"
   ],
   "desc": "know what `src/attr/validators.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/__init__.py"
   ],
   "desc": "know what `src/attr/__init__.py` exports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/strategies.py",
    "make_class"
   ],
   "desc": "outline `tests/strategies.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "make_class"
   ],
   "desc": "outline `tests/test_dunders.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "make_class"
   ],
   "desc": "outline `tests/test_make.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/utils.py",
    "make_class"
   ],
   "desc": "outline `tests/utils.py` for its `make_class` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/strategies.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/strategies.py\", \"make_class\"]]",
   "v1": [
    8143541,
    904550
   ],
   "v2": [
    4080816,
    452275
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
     "tests/strategies.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_dunders.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/test_dunders.py\", \"make_class\"]]",
   "v1": [
    8143541,
    904550
   ],
   "v2": [
    4080816,
    452275
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
     "tests/test_dunders.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"make_class\"]]",
   "v1": [
    8143541,
    904550
   ],
   "v2": [
    4080816,
    452275
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
     "tests/test_make.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/utils.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/utils.py\", \"make_class\"]]",
   "v1": [
    8143541,
    904550
   ],
   "v2": [
    4080816,
    452275
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
     "tests/utils.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "read('src/attr/__init__.py', 45, 30)",
   "key": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]",
   "v1": [
    5254561,
    578912
   ],
   "v2": [
    131653481,
    14472800
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/__init__.py"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    5254561,
    578912
   ],
   "v2": [
    131653481,
    14472800
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/converters.py"
    ]
   ]
  },
  {
   "call": "read('src/attr/validators.py', 19, 30)",
   "key": "[\"read\", [\"src/attr/validators.py\", 19, 30]]",
   "v1": [
    5254561,
    578912
   ],
   "v2": [
    131653481,
    14472800
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/validators.py"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/strategies.py', 'make_class')",
  "key": "[\"symbols\", [\"tests/strategies.py\", \"make_class\"]]",
  "provenance": "`tests/strategies.py` had a matching line (step 1); its outline names every `make_class` import exactly",
  "v2": [
   4080816,
   452275
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
  "ok": "[\"symbols\", [\"tests/test_dunders.py\", \"make_class\"]]",
  "cap": "[\"symbols\", [\"tests/test_dunders.py\", \"make_class\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"tests/strategies.py\", \"make_class\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 18,
   "path": "tests/strategies.py",
   "filter": "make_class",
   "header": {
    "lines": 219,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/strategies.py",
     "name": "make_class",
     "line": 17,
     "kind": "from",
     "src": ".utils",
     "src_name": "make_class",
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
    "src/attr/__init__.py",
    16,
    "in",
    "`._make` resolves `make_class` to the target"
   ],
   [
    "src/attrs/__init__.py",
    3,
    "out",
    "`attr` resolves `make_class` to ambiguous(dynamic module)"
   ],
   [
    "src/attrs/converters.py",
    3,
    "pending",
    ""
   ],
   [
    "src/attrs/exceptions.py",
    3,
    "out",
    "star import of `attr.exceptions`, which does not export `make_class`"
   ],
   [
    "src/attrs/filters.py",
    3,
    "out",
    "star import of `attr.filters`, which does not export `make_class`"
   ],
   [
    "src/attrs/setters.py",
    3,
    "out",
    "star import of `attr.setters`, which does not export `ma
```
</details>

## Step 19

In `tests/strategies.py`, `make_class` has exactly one binding: line 17 imports it as `make_class` from `.utils`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 12; statements confirmed: 1, ruled out: 4, modules with no such import: 0, pending: 7. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/setters.py`:3, star import of `attr.setters`, which does not export `make_class`.

Outstanding: know what `src/attr/converters.py` exports; know what `src/attr/validators.py` exports; know what `src/attr/__init__.py` exports; close the namespace of `tests/utils.py` for `make_class`; and 3 more.

Next: outline `tests/test_dunders.py` filtered to `make_class`, because `tests/test_dunders.py` had a matching line (step 1); its outline names every `make_class` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `tests/test_make.py` filtered to `make_class`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `tests/test_make.py` filtered to `make_class`; cap: outline `tests/test_make.py` filtered to `make_class`.

**Call:** `symbols('tests/test_dunders.py', 'make_class')`

**Response**: outcome `ok`

```
module tests/test_dunders.py lines=1062 dynamic=no all=none
18 from make_class <- attr._make make_class
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/converters.py"
   ],
   "desc": "know what `src/attr/converters.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/validators.py"
   ],
   "desc": "know what `src/attr/validators.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/__init__.py"
   ],
   "desc": "know what `src/attr/__init__.py` exports"
  },
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "tests/utils.py",
    "make_class"
   ],
   "desc": "close the namespace of `tests/utils.py` for `make_class`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "make_class"
   ],
   "desc": "outline `tests/test_dunders.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "make_class"
   ],
   "desc": "outline `tests/test_make.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/utils.py",
    "make_class"
   ],
   "desc": "outline `tests/utils.py` for its `make_class` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/test_dunders.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/test_dunders.py\", \"make_class\"]]",
   "v1": [
    7750441,
    904550
   ],
   "v2": [
    3884266,
    452275
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
     "tests/test_dunders.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"make_class\"]]",
   "v1": [
    7750441,
    904550
   ],
   "v2": [
    3884266,
    452275
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
     "tests/test_make.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "read('src/attr/__init__.py', 45, 30)",
   "key": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]",
   "v1": [
    5002977,
    578912
   ],
   "v2": [
    125363881,
    14472800
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/__init__.py"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    5002977,
    578912
   ],
   "v2": [
    125363881,
    14472800
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/converters.py"
    ]
   ]
  },
  {
   "call": "read('src/attr/validators.py', 19, 30)",
   "key": "[\"read\", [\"src/attr/validators.py\", 19, 30]]",
   "v1": [
    5002977,
    578912
   ],
   "v2": [
    125363881,
    14472800
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/validators.py"
    ]
   ]
  },
  {
   "call": "symbols('tests/utils.py')",
   "key": "[\"symbols\", [\"tests/utils.py\"]]",
   "v1": [
    6663707010567,
    767425502572
   ],
   "v2": [
    166976388015461,
    19185637564300
   ],
   "p_cap": [
    70,
    519
   ],
   "forecast": {
    "def": [
     25144,
     30621
    ],
    "reexport": [
     5837,
     244968
    ],
    "star": [
     449,
     244968
    ],
    "none": [
     2245,
     122484
    ],
    "cap": [
     70,
     519
    ]
   },
   "serves": [
    [
     "bindings",
     "tests/utils.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/utils.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/utils.py\", \"make_class\"]]",
   "v1": [
    1678364761,
    187965490
   ],
   "v2": [
    4205310177,
    469913725
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
     "tests/utils.py",
     "make_class"
    ],
    [
     "outline",
     "tests/utils.py",
     "make_class"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_dunders.py', 'make_class')",
  "key": "[\"symbols\", [\"tests/test_dunders.py\", \"make_class\"]]",
  "provenance": "`tests/test_dunders.py` had a matching line (step 1); its outline names every `make_class` import exactly",
  "v2": [
   3884266,
   452275
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
  "ok": "[\"symbols\", [\"tests/test_make.py\", \"make_class\"]]",
  "cap": "[\"symbols\", [\"tests/test_make.py\", \"make_class\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"tests/test_dunders.py\", \"make_class\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 19,
   "path": "tests/test_dunders.py",
   "filter": "make_class",
   "header": {
    "lines": 1062,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_dunders.py",
     "name": "make_class",
     "line": 18,
     "kind": "from",
     "src": "attr._make",
     "src_name": "make_class",
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
    "src/attr/__init__.py",
    16,
    "in",
    "`._make` resolves `make_class` to the target"
   ],
   [
    "src/attrs/__init__.py",
    3,
    "out",
    "`attr` resolves `make_class` to ambiguous(dynamic module)"
   ],
   [
    "src/attrs/converters.py",
    3,
    "pending",
    ""
   ],
   [
    "src/attrs/exceptions.py",
    3,
    "out",
    "star import of `
```
</details>

## Step 20

In `tests/test_dunders.py`, `make_class` has exactly one binding: line 18 imports it as `make_class` from `attr._make`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 12; statements confirmed: 2, ruled out: 4, modules with no such import: 0, pending: 6. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/setters.py`:3, star import of `attr.setters`, which does not export `make_class`.

Open: know what `src/attr/converters.py` exports; know what `src/attr/validators.py` exports; know what `src/attr/__init__.py` exports; close the namespace of `tests/utils.py` for `make_class`; and 2 more.

Next: outline `tests/test_make.py` filtered to `make_class`, because `tests/test_make.py` had a matching line (step 1); its outline names every `make_class` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, read `src/attr/__init__.py` from line 45, scores the same; the seed broke the tie. Plan by outcome: ok: read `src/attr/__init__.py` from line 45; cap: read `src/attr/__init__.py` from line 45.

**Call:** `symbols('tests/test_make.py', 'make_class')`

**Response**: outcome `ok`

```
module tests/test_make.py lines=3213 dynamic=no all=none
29 from make_class <- attr._make make_class
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/converters.py"
   ],
   "desc": "know what `src/attr/converters.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/validators.py"
   ],
   "desc": "know what `src/attr/validators.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/__init__.py"
   ],
   "desc": "know what `src/attr/__init__.py` exports"
  },
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "tests/utils.py",
    "make_class"
   ],
   "desc": "close the namespace of `tests/utils.py` for `make_class`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "make_class"
   ],
   "desc": "outline `tests/test_make.py` for its `make_class` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/utils.py",
    "make_class"
   ],
   "desc": "outline `tests/utils.py` for its `make_class` imports"
  }
 ],
 "candidates": [
  {
   "call": "read('src/attr/__init__.py', 45, 30)",
   "key": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]",
   "v1": [
    4137089,
    578912
   ],
   "v2": [
    103716681,
    14472800
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/__init__.py"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    4137089,
    578912
   ],
   "v2": [
    103716681,
    14472800
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/converters.py"
    ]
   ]
  },
  {
   "call": "read('src/attr/validators.py', 19, 30)",
   "key": "[\"read\", [\"src/attr/validators.py\", 19, 30]]",
   "v1": [
    4137089,
    578912
   ],
   "v2": [
    103716681,
    14472800
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/validators.py"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"make_class\"]]",
   "v1": [
    6397491,
    904550
   ],
   "v2": [
    103716681,
    14472800
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
     "tests/test_make.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/utils.py')",
   "key": "[\"symbols\", [\"tests/utils.py\"]]",
   "v1": [
    5515856329339,
    767425502572
   ],
   "v2": [
    138280120984761,
    19185637564300
   ],
   "p_cap": [
    70,
    519
   ],
   "forecast": {
    "def": [
     25144,
     30621
    ],
    "reexport": [
     5837,
     244968
    ],
    "star": [
     449,
     244968
    ],
    "none": [
     2245,
     122484
    ],
    "cap": [
     70,
     519
    ]
   },
   "serves": [
    [
     "bindings",
     "tests/utils.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/utils.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/utils.py\", \"make_class\"]]",
   "v1": [
    1397221751,
    187965490
   ],
   "v2": [
    3502452652,
    469913725
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
     "tests/utils.py",
     "make_class"
    ],
    [
     "outline",
     "tests/utils.py",
     "make_class"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_make.py', 'make_class')",
  "key": "[\"symbols\", [\"tests/test_make.py\", \"make_class\"]]",
  "provenance": "`tests/test_make.py` had a matching line (step 1); its outline names every `make_class` import exactly",
  "v2": [
   103716681,
   14472800
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
  "ok": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]",
  "cap": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"tests/test_make.py\", \"make_class\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 20,
   "path": "tests/test_make.py",
   "filter": "make_class",
   "header": {
    "lines": 3213,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_make.py",
     "name": "make_class",
     "line": 29,
     "kind": "from",
     "src": "attr._make",
     "src_name": "make_class",
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
    "src/attr/__init__.py",
    16,
    "in",
    "`._make` resolves `make_class` to the target"
   ],
   [
    "src/attrs/__init__.py",
    3,
    "out",
    "`attr` resolves `make_class` to ambiguous(dynamic module)"
   ],
   [
    "src/attrs/converters.py",
    3,
    "pending",
    ""
   ],
   [
    "src/attrs/exceptions.py",
    3,
    "out",
    "star import of `attr.exceptions`, which does not export `make_class`"
   ],
   [
    "src/attrs/filters.py",
    3,
    "out",
    "star import of `attr.filters`, which does not export `make_class`"
   ],
   [
    "src/attrs/setters.py",
    3,
    "out",
    "star import of `attr.setters`, which does not export `make_class`"
   ],
   [
    "src/attrs/validators.py",
    3,
    "pending",
    ""
   ],
   [
    "tests/attr_import_star.py",
    4,
    "pending",
    ""
   ],
   [
    "tests/strategies.py",
    17,
    "pending",
    ""
   ],
   [
    "tests/test_dunders.py",
    18,
    "in",
    "`attr._make` resolves `make_class` to the target"
   ],
   [
    "tests/t
```
</details>

## Step 21

In `tests/test_make.py`, `make_class` has exactly one binding: line 29 imports it as `make_class` from `attr._make`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 12; statements confirmed: 3, ruled out: 4, modules with no such import: 0, pending: 5. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/setters.py`:3, star import of `attr.setters`, which does not export `make_class`.

Still to settle: know what `src/attr/converters.py` exports; know what `src/attr/validators.py` exports; know what `src/attr/__init__.py` exports; close the namespace of `tests/utils.py` for `make_class`; and 1 more.

Next: read `src/attr/__init__.py` from line 45, because `__all__` of `src/attr/__init__.py` starts at line 45 (outline header). I expect: the whole list fits the window (about 90%); the list runs past the window (about 10%). The alternative, read `src/attr/converters.py` from line 11, scores the same; the seed broke the tie. Plan by outcome: fits: read `src/attr/converters.py` from line 11; long: read `src/attr/converters.py` from line 11.

**Call:** `read('src/attr/__init__.py', 45, 30)`

**Response**: outcome `long`

```
45:__all__ = [
46:    "NOTHING",
47:    "Attribute",
48:    "AttrsInstance",
49:    "Converter",
50:    "Factory",
51:    "NothingType",
52:    "asdict",
53:    "assoc",
54:    "astuple",
55:    "attr",
56:    "attrib",
57:    "attributes",
58:    "attrs",
59:    "cmp_using",
60:    "converters",
61:    "define",
62:    "evolve",
63:    "exceptions",
64:    "field",
65:    "fields",
66:    "fields_dict",
67:    "filters",
68:    "frozen",
69:    "get_run_validators",
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
    "src/attr/converters.py"
   ],
   "desc": "know what `src/attr/converters.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/validators.py"
   ],
   "desc": "know what `src/attr/validators.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/__init__.py"
   ],
   "desc": "know what `src/attr/__init__.py` exports"
  },
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "tests/utils.py",
    "make_class"
   ],
   "desc": "close the namespace of `tests/utils.py` for `make_class`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/utils.py",
    "make_class"
   ],
   "desc": "outline `tests/utils.py` for its `make_class` imports"
  }
 ],
 "candidates": [
  {
   "call": "read('src/attr/__init__.py', 45, 30)",
   "key": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]",
   "v1": [
    3271201,
    578912
   ],
   "v2": [
    1662737,
    289456
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/__init__.py"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    3271201,
    578912
   ],
   "v2": [
    1662737,
    289456
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/converters.py"
    ]
   ]
  },
  {
   "call": "read('src/attr/validators.py', 19, 30)",
   "key": "[\"read\", [\"src/attr/validators.py\", 19, 30]]",
   "v1": [
    3271201,
    578912
   ],
   "v2": [
    1662737,
    289456
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/validators.py"
    ]
   ]
  },
  {
   "call": "symbols('tests/utils.py')",
   "key": "[\"symbols\", [\"tests/utils.py\"]]",
   "v1": [
    4368005648111,
    767425502572
   ],
   "v2": [
    35519614311817,
    6139404020576
   ],
   "p_cap": [
    70,
    519
   ],
   "forecast": {
    "def": [
     25144,
     30621
    ],
    "reexport": [
     5837,
     244968
    ],
    "star": [
     449,
     244968
    ],
    "none": [
     2245,
     122484
    ],
    "cap": [
     70,
     519
    ]
   },
   "serves": [
    [
     "bindings",
     "tests/utils.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/utils.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/utils.py\", \"make_class\"]]",
   "v1": [
    14127579,
    2379310
   ],
   "v2": [
    229610229,
    38068960
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
     "tests/utils.py",
     "make_class"
    ],
    [
     "outline",
     "tests/utils.py",
     "make_class"
    ]
   ]
  }
 ],
 "choice": {
  "call": "read('src/attr/__init__.py', 45, 30)",
  "key": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]",
  "provenance": "`__all__` of `src/attr/__init__.py` starts at line 45 (outline header)",
  "v2": [
   1662737,
   289456
  ]
 },
 "forecast": {
  "fits": [
   29,
   32
  ],
  "long": [
   3,
   32
  ]
 },
 "plan": {
  "fits": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
  "long": "[\"read\", [\"src/attr/converters.py\", 11, 30]]"
 },
 "adherence": {
  "planned": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "read",
   "step": 21,
   "path": "src/attr/__init__.py",
   "start": 45,
   "count": 30,
   "n": 30
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "src/attr/__init__.py",
    16,
    "in",
    "`._make` resolves `make_class` to the target"
   ],
   [
    "src/attrs/__init__.py",
    3,
    "out",
    "`attr` resolves `make_class` to ambiguous(dynamic module)"
   ],
   [
    "src/attrs/converters.py",
    3,
    "pending",
    ""
   ],
   [
    "src/attrs/exceptions.py",
    3,
    "out",
    "star import of `attr.exceptions`, which does not export `make_class`"
   ],
   [
    "src/attrs/filters.py",
    3,
    "out",
    "star import of `attr.filters`, which does not export `make_class`"
   ],
   [
    "src/attrs/setters.py",
    3,
    "out",
    "star import of `attr.setters`, which does not export `make_class`"
   ],
   [
    "src/attrs/validators.py",
    3,
    "pending",
    ""
   ],
   [
    "tests/attr_import_star.py",
    4,
    "pending",
    ""
   ],
   [
    "tests/strategies.py",
    17,
    "pending",
    ""
   ],
   [
    "tests/test_dunders.py",
    18,
    "in",
    "`attr._make` resolves `make_class` to the target"
   ],
   [
    "tests/test_make.py",
    29,
    "in",
    "`attr._make` resolves `make_class` to the target"
   ],
   [
    "tests/utils.py",
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

## Step 22

The statement at `src/attr/__init__.py`:45 binds `__all__`.

Candidate modules so far: 12; statements confirmed: 3, ruled out: 4, modules with no such import: 0, pending: 5. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/setters.py`:3, star import of `attr.setters`, which does not export `make_class`.

Open: know what `src/attr/converters.py` exports; know what `src/attr/validators.py` exports; know what `src/attr/__init__.py` exports; close the namespace of `tests/utils.py` for `make_class`; and 1 more.

Next: read `src/attr/converters.py` from line 11, because `__all__` of `src/attr/converters.py` starts at line 11 (outline header). I expect: the whole list fits the window (about 90%); the list runs past the window (about 10%). The alternative, read `src/attr/__init__.py` from line 45, scores the same; the seed broke the tie. Plan by outcome: fits: read `src/attr/__init__.py` from line 45; long: read `src/attr/__init__.py` from line 45.

**Call:** `read('src/attr/converters.py', 11, 30)`

**Response**: outcome `fits`

```
11:__all__ = [
12:    "default_if_none",
13:    "optional",
14:    "pipe",
15:    "to_bool",
16:]
17:
18:
19:def optional(converter):
20:    """
21:    A converter that allows an attribute to be optional. An optional attribute
22:    is one which can be set to `None`.
23:
24:    Type annotations will be inferred from the wrapped converter's, if it has
25:    any.
26:
27:    Args:
28:        converter (typing.Callable):
29:            the converter that is used for non-`None` values.
30:
31:    .. versionadded:: 17.1.0
32:    """
33:
34:    if isinstance(converter, Converter):
35:
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
    "src/attr/converters.py"
   ],
   "desc": "know what `src/attr/converters.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/validators.py"
   ],
   "desc": "know what `src/attr/validators.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/__init__.py"
   ],
   "desc": "know what `src/attr/__init__.py` exports"
  },
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "tests/utils.py",
    "make_class"
   ],
   "desc": "close the namespace of `tests/utils.py` for `make_class`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/utils.py",
    "make_class"
   ],
   "desc": "outline `tests/utils.py` for its `make_class` imports"
  }
 ],
 "candidates": [
  {
   "call": "read('src/attr/__init__.py', 45, 60)",
   "key": "[\"read\", [\"src/attr/__init__.py\", 45, 60]]",
   "v1": [
    3271201,
    578912
   ],
   "v2": [
    1662737,
    289456
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/__init__.py"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    3271201,
    578912
   ],
   "v2": [
    1662737,
    289456
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/converters.py"
    ]
   ]
  },
  {
   "call": "read('src/attr/validators.py', 19, 30)",
   "key": "[\"read\", [\"src/attr/validators.py\", 19, 30]]",
   "v1": [
    3271201,
    578912
   ],
   "v2": [
    1662737,
    289456
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/validators.py"
    ]
   ]
  },
  {
   "call": "symbols('tests/utils.py')",
   "key": "[\"symbols\", [\"tests/utils.py\"]]",
   "v1": [
    4368005648111,
    767425502572
   ],
   "v2": [
    35519614311817,
    6139404020576
   ],
   "p_cap": [
    70,
    519
   ],
   "forecast": {
    "def": [
     25144,
     30621
    ],
    "reexport": [
     5837,
     244968
    ],
    "star": [
     449,
     244968
    ],
    "none": [
     2245,
     122484
    ],
    "cap": [
     70,
     519
    ]
   },
   "serves": [
    [
     "bindings",
     "tests/utils.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/utils.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/utils.py\", \"make_class\"]]",
   "v1": [
    14127579,
    2379310
   ],
   "v2": [
    229610229,
    38068960
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
     "tests/utils.py",
     "make_class"
    ],
    [
     "outline",
     "tests/utils.py",
     "make_class"
    ]
   ]
  }
 ],
 "choice": {
  "call": "read('src/attr/converters.py', 11, 30)",
  "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
  "provenance": "`__all__` of `src/attr/converters.py` starts at line 11 (outline header)",
  "v2": [
   1662737,
   289456
  ]
 },
 "forecast": {
  "fits": [
   29,
   32
  ],
  "long": [
   3,
   32
  ]
 },
 "plan": {
  "fits": "[\"read\", [\"src/attr/__init__.py\", 45, 60]]",
  "long": "[\"read\", [\"src/attr/__init__.py\", 45, 60]]"
 },
 "adherence": {
  "planned": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "read",
   "step": 22,
   "path": "src/attr/converters.py",
   "start": 11,
   "count": 30,
   "n": 30
  },
  {
   "kind": "all_names",
   "step": 22,
   "path": "src/attr/converters.py",
   "value": [
    "default_if_none",
    "optional",
    "pipe",
    "to_bool"
   ]
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "src/attr/__init__.py",
    16,
    "in",
    "`._make` resolves `make_class` to the target"
   ],
   [
    "src/attrs/__init__.py",
    3,
    "out",
    "`attr` resolves `make_class` to ambiguous(dynamic module)"
   ],
   [
    "src/attrs/converters.py",
    3,
    "out",
    "star import of `attr.converters`, which does not export `make_class`"
   ],
   [
    "src/attrs/exceptions.py",
    3,
    "out",
    "star import of `attr.exceptions`, which does not export `make_class`"
   ],
   [
    "src/attrs/filters.py",
    3,
    "out",
    "star import of `attr.filters`, which does not export `make_class`"
   ],
   [
    "src/attrs/setters.py",
    3,
    "out",
    "star import of `attr.setters`, which does not export `make_class`"
   ],
   [
    "src/attrs/validators.py",
    3,
    "pending",
    ""
   ],
   [
    "tests/attr_import_star.py",
    4,
    "pending",
    ""
   ],
   [
    "tests/strategies.py",
    17,
    "pending",
    ""
   ],
   [
    "tests/test_dunders.py",
    18,
    "in",
    "`attr._make` resolves `make_class` to the target"
   ],
   [
    "tests/test_make.py",
    29,
    "in",
    "`attr._make` resolves `make_class` to the target"
   ],
   [
    "tests/utils.py",
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

## Step 23

The statement at `src/attr/converters.py`:11 binds `__all__`. `__all__` in `src/attr/converters.py` lists 4 names, and `make_class` is not among them.

Candidate modules so far: 12; statements confirmed: 3, ruled out: 5, modules with no such import: 0, pending: 4. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/setters.py`:3, star import of `attr.setters`, which does not export `make_class`.

Outstanding: know what `src/attr/validators.py` exports; know what `src/attr/__init__.py` exports; close the namespace of `tests/utils.py` for `make_class`; outline `tests/utils.py` for its `make_class` imports.

Next: read `src/attr/__init__.py` from line 45, because `__all__` of `src/attr/__init__.py` starts at line 45 (outline header). I expect: the whole list fits the window (about 90%); the list runs past the window (about 10%). The alternative, read `src/attr/validators.py` from line 19, scores the same; the seed broke the tie. Plan by outcome: fits: read `src/attr/validators.py` from line 19; long: read `src/attr/validators.py` from line 19.

**Call:** `read('src/attr/__init__.py', 45, 60)`

**Response**: outcome `fits`

```
45:__all__ = [
46:    "NOTHING",
47:    "Attribute",
48:    "AttrsInstance",
49:    "Converter",
50:    "Factory",
51:    "NothingType",
52:    "asdict",
53:    "assoc",
54:    "astuple",
55:    "attr",
56:    "attrib",
57:    "attributes",
58:    "attrs",
59:    "cmp_using",
60:    "converters",
61:    "define",
62:    "evolve",
63:    "exceptions",
64:    "field",
65:    "fields",
66:    "fields_dict",
67:    "filters",
68:    "frozen",
69:    "get_run_validators",
... (35 more lines)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/validators.py"
   ],
   "desc": "know what `src/attr/validators.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/__init__.py"
   ],
   "desc": "know what `src/attr/__init__.py` exports"
  },
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "tests/utils.py",
    "make_class"
   ],
   "desc": "close the namespace of `tests/utils.py` for `make_class`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/utils.py",
    "make_class"
   ],
   "desc": "outline `tests/utils.py` for its `make_class` imports"
  }
 ],
 "candidates": [
  {
   "call": "read('src/attr/__init__.py', 45, 60)",
   "key": "[\"read\", [\"src/attr/__init__.py\", 45, 60]]",
   "v1": [
    2692289,
    578912
   ],
   "v2": [
    1373281,
    289456
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/__init__.py"
    ]
   ]
  },
  {
   "call": "read('src/attr/validators.py', 19, 30)",
   "key": "[\"read\", [\"src/attr/validators.py\", 19, 30]]",
   "v1": [
    2692289,
    578912
   ],
   "v2": [
    1373281,
    289456
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/validators.py"
    ]
   ]
  },
  {
   "call": "symbols('tests/utils.py')",
   "key": "[\"symbols\", [\"tests/utils.py\"]]",
   "v1": [
    3600580145539,
    767425502572
   ],
   "v2": [
    29380210291241,
    6139404020576
   ],
   "p_cap": [
    70,
    519
   ],
   "forecast": {
    "def": [
     25144,
     30621
    ],
    "reexport": [
     5837,
     244968
    ],
    "star": [
     449,
     244968
    ],
    "none": [
     2245,
     122484
    ],
    "cap": [
     70,
     519
    ]
   },
   "serves": [
    [
     "bindings",
     "tests/utils.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/utils.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/utils.py\", \"make_class\"]]",
   "v1": [
    11748269,
    2379310
   ],
   "v2": [
    191541269,
    38068960
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
     "tests/utils.py",
     "make_class"
    ],
    [
     "outline",
     "tests/utils.py",
     "make_class"
    ]
   ]
  }
 ],
 "choice": {
  "call": "read('src/attr/__init__.py', 45, 60)",
  "key": "[\"read\", [\"src/attr/__init__.py\", 45, 60]]",
  "provenance": "`__all__` of `src/attr/__init__.py` starts at line 45 (outline header)",
  "v2": [
   1373281,
   289456
  ]
 },
 "forecast": {
  "fits": [
   29,
   32
  ],
  "long": [
   3,
   32
  ]
 },
 "plan": {
  "fits": "[\"read\", [\"src/attr/validators.py\", 19, 30]]",
  "long": "[\"read\", [\"src/attr/validators.py\", 19, 30]]"
 },
 "adherence": {
  "planned": "[\"read\", [\"src/attr/__init__.py\", 45, 60]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "read",
   "step": 23,
   "path": "src/attr/__init__.py",
   "start": 45,
   "count": 60,
   "n": 60
  },
  {
   "kind": "all_names",
   "step": 23,
   "path": "src/attr/__init__.py",
   "value": [
    "NOTHING",
    "Attribute",
    "AttrsInstance",
    "Converter",
    "Factory",
    "NothingType",
    "asdict",
    "assoc",
    "astuple",
    "attr",
    "attrib",
    "attributes",
    "attrs",
    "cmp_using",
    "converters",
    "define",
    "evolve",
    "exceptions",
    "field",
    "fields",
    "fields_dict",
    "filters",
    "frozen",
    "get_run_validators",
    "has",
    "ib",
    "make_class",
    "mutable",
    "resolve_types",
    "s",
    "set_run_validators",
    "setters",
    "validate",
    "validators"
   ]
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "src/attr/__init__.py",
    16,
    "in",
    "`._make` resolves `make_class` to the target"
   ],
   [
    "src/attrs/__init__.py",
    3,
    "out",
    "`attr` resolves `make_class` to ambiguous(dynamic module)"
   ],
   [
    "src/attrs/converters.py",
    3,
    "out",
    "star import of `attr.converters`, which does not export `make_class`"
   ],
   [
    "src/attrs/exceptions.py",
    3,
    "out",
    "star import of `attr.exceptions`, which does not export `make_class`"
   ],
   [
    "src/attrs/filters.py",
    3,
    "out",
    "star import of `attr.filters`, which does not export `make_class`"
   ],
   [
    "src/attrs/setters.py",
    3,
    "out",
    "star import of `attr.setters`, which does not export `make_class`"
   ],
   [
    "src/attrs/validators.py",
    3,
    "pending",
    ""
   ],
   [
    "tests/attr_import_star.py",
    4,
    "out",
    "star import of `attr` binds `make_class` to ambiguous(dynamic module)"
   ],
   [
    "tests/strategies.py",
    17,
    "pending",
    ""
   ],
   [
    "tests/test_dunders.py",
    18,
    "in",
    "`attr._make` resolves `make_class` to the target"
   ],
   [
    "tests/test_make.py",
    29,
    "in",
    "`attr._make` resolves `make_class` to the target"
   ],
   [
    "tests/utils.py",
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

## Step 24

The statement at `src/attr/__init__.py`:45 binds `__all__`. `__all__` in `src/attr/__init__.py` lists 34 names, and it names `make_class`.

Candidate modules so far: 12; statements confirmed: 3, ruled out: 6, modules with no such import: 0, pending: 3. import coverage complete; star coverage complete. Latest ruled out: `tests/attr_import_star.py`:4, star import of `attr` binds `make_class` to ambiguous(dynamic module).

Still to settle: know what `src/attr/validators.py` exports; close the namespace of `tests/utils.py` for `make_class`; outline `tests/utils.py` for its `make_class` imports.

Next: read `src/attr/validators.py` from line 19, because `__all__` of `src/attr/validators.py` starts at line 19 (outline header). I expect: the whole list fits the window (about 90%); the list runs past the window (about 10%). The alternative, outline `tests/utils.py`, is more likely to hit the cap (about 15% against under 5%). Plan by outcome: fits: outline `tests/utils.py`; long: outline `tests/utils.py`.

**Call:** `read('src/attr/validators.py', 19, 30)`

**Response**: outcome `fits`

```
19:__all__ = [
20:    "and_",
21:    "deep_iterable",
22:    "deep_mapping",
23:    "disabled",
24:    "ge",
25:    "get_disabled",
26:    "gt",
27:    "in_",
28:    "instance_of",
29:    "is_callable",
30:    "le",
31:    "lt",
32:    "matches_re",
33:    "max_len",
34:    "min_len",
35:    "ne",
36:    "not_",
37:    "optional",
38:    "or_",
39:    "set_disabled",
40:]
41:
42:
43:def set_disabled(disabled):
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
    "src/attr/validators.py"
   ],
   "desc": "know what `src/attr/validators.py` exports"
  },
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "tests/utils.py",
    "make_class"
   ],
   "desc": "close the namespace of `tests/utils.py` for `make_class`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/utils.py",
    "make_class"
   ],
   "desc": "outline `tests/utils.py` for its `make_class` imports"
  }
 ],
 "candidates": [
  {
   "call": "read('src/attr/validators.py', 19, 30)",
   "key": "[\"read\", [\"src/attr/validators.py\", 19, 30]]",
   "v1": [
    2113377,
    578912
   ],
   "v2": [
    23240806270665,
    6139404020576
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "fits": [
     29,
     32
    ],
    "long": [
     3,
     32
    ]
   },
   "serves": [
    [
     "all",
     "src/attr/validators.py"
    ]
   ]
  },
  {
   "call": "symbols('tests/utils.py')",
   "key": "[\"symbols\", [\"tests/utils.py\"]]",
   "v1": [
    2833154642967,
    767425502572
   ],
   "v2": [
    23240806270665,
    6139404020576
   ],
   "p_cap": [
    70,
    519
   ],
   "forecast": {
    "def": [
     25144,
     30621
    ],
    "reexport": [
     5837,
     244968
    ],
    "star": [
     449,
     244968
    ],
    "none": [
     2245,
     122484
    ],
    "cap": [
     70,
     519
    ]
   },
   "serves": [
    [
     "bindings",
     "tests/utils.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/utils.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/utils.py\", \"make_class\"]]",
   "v1": [
    9368959,
    2379310
   ],
   "v2": [
    153472309,
    38068960
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
     "tests/utils.py",
     "make_class"
    ],
    [
     "outline",
     "tests/utils.py",
     "make_class"
    ]
   ]
  }
 ],
 "choice": {
  "call": "read('src/attr/validators.py', 19, 30)",
  "key": "[\"read\", [\"src/attr/validators.py\", 19, 30]]",
  "provenance": "`__all__` of `src/attr/validators.py` starts at line 19 (outline header)",
  "v2": [
   23240806270665,
   6139404020576
  ]
 },
 "forecast": {
  "fits": [
   29,
   32
  ],
  "long": [
   3,
   32
  ]
 },
 "plan": {
  "fits": "[\"symbols\", [\"tests/utils.py\"]]",
  "long": "[\"symbols\", [\"tests/utils.py\"]]"
 },
 "adherence": {
  "planned": "[\"read\", [\"src/attr/validators.py\", 19, 30]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "read",
   "step": 24,
   "path": "src/attr/validators.py",
   "start": 19,
   "count": 30,
   "n": 30
  },
  {
   "kind": "all_names",
   "step": 24,
   "path": "src/attr/validators.py",
   "value": [
    "and_",
    "deep_iterable",
    "deep_mapping",
    "disabled",
    "ge",
    "get_disabled",
    "gt",
    "in_",
    "instance_of",
    "is_callable",
    "le",
    "lt",
    "matches_re",
    "max_len",
    "min_len",
    "ne",
    "not_",
    "optional",
    "or_",
    "set_disabled"
   ]
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "src/attr/__init__.py",
    16,
    "in",
    "`._make` resolves `make_class` to the target"
   ],
   [
    "src/attrs/__init__.py",
    3,
    "out",
    "`attr` resolves `make_class` to ambiguous(dynamic module)"
   ],
   [
    "src/attrs/converters.py",
    3,
    "out",
    "star import of `attr.converters`, which does not export `make_class`"
   ],
   [
    "src/attrs/exceptions.py",
    3,
    "out",
    "star import of `attr.exceptions`, which does not export `make_class`"
   ],
   [
    "src/attrs/filters.py",
    3,
    "out",
    "star import of `attr.filters`, which does not export `make_class`"
   ],
   [
    "src/attrs/setters.py",
    3,
    "out",
    "star import of `attr.setters`, which does not export `make_class`"
   ],
   [
    "src/attrs/validators.py",
    3,
    "out",
    "star import of `attr.validators`, which does not export `make_class`"
   ],
   [
    "tests/attr_import_star.py",
    4,
    "out",
    "star import of `attr` binds `make_class` to ambiguous(dynamic module)"
   ],
   [
    "tests/strategies.py",
    17,
    "pending",
    ""
   ],
   [
    "tests/test_dunders.py",
    18,
    "in",
    "`attr._make` resolves `make_class` to the target"
   ],
   [
    "tests/test_make.py",
    29,
    "in",
    "`attr._make` resolves `make_class` to the target"
   ],
   [
    "tests/utils.py",
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

## Step 25

The statement at `src/attr/validators.py`:19 binds `__all__`. `__all__` in `src/attr/validators.py` lists 20 names, and `make_class` is not among them. This is not the branch I planned for that outcome; the open items changed more than expected.

Candidate modules so far: 12; statements confirmed: 3, ruled out: 7, modules with no such import: 0, pending: 2. import coverage complete; star coverage complete. Latest ruled out: `tests/attr_import_star.py`:4, star import of `attr` binds `make_class` to ambiguous(dynamic module).

Still to settle: close the namespace of `tests/utils.py` for `make_class`; outline `tests/utils.py` for its `make_class` imports.

Next: outline `tests/utils.py` filtered to `make_class`, because module `tests/utils.py` (step 1), name `make_class` (task). I expect: a re-export continues the chain to its source (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a definition there ends the chain (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `tests/utils.py`, is more likely to hit the cap (about 15% against under 5%). Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done.

**Call:** `symbols('tests/utils.py', 'make_class')`

**Response**: outcome `reexport`

```
module tests/utils.py lines=70 dynamic=no all=none
8 from make_class <- attr._make make_class
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "tests/utils.py",
    "make_class"
   ],
   "desc": "close the namespace of `tests/utils.py` for `make_class`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/utils.py",
    "make_class"
   ],
   "desc": "outline `tests/utils.py` for its `make_class` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/utils.py', 'make_class')",
   "key": "[\"symbols\", [\"tests/utils.py\", \"make_class\"]]",
   "v1": [
    6989649,
    2379310
   ],
   "v2": [
    6989649,
    2379310
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
     "tests/utils.py",
     "make_class"
    ],
    [
     "outline",
     "tests/utils.py",
     "make_class"
    ]
   ]
  },
  {
   "call": "symbols('tests/utils.py')",
   "key": "[\"symbols\", [\"tests/utils.py\"]]",
   "v1": [
    2065729140395,
    767425502572
   ],
   "v2": [
    193828734651,
    48571234340
   ],
   "p_cap": [
    70,
    519
   ],
   "forecast": {
    "def": [
     25144,
     30621
    ],
    "reexport": [
     5837,
     244968
    ],
    "star": [
     449,
     244968
    ],
    "none": [
     2245,
     122484
    ],
    "cap": [
     70,
     519
    ]
   },
   "serves": [
    [
     "bindings",
     "tests/utils.py",
     "make_class"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/utils.py', 'make_class')",
  "key": "[\"symbols\", [\"tests/utils.py\", \"make_class\"]]",
  "provenance": "module `tests/utils.py` (step 1), name `make_class` (task)",
  "v2": [
   6989649,
   2379310
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
  "planned": "[\"symbols\", [\"tests/utils.py\"]]",
  "status": "deviated"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 25,
   "path": "tests/utils.py",
   "filter": "make_class",
   "header": {
    "lines": 70,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/utils.py",
     "name": "make_class",
     "line": 8,
     "kind": "from",
     "src": "attr._make",
     "src_name": "make_class",
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
    "src/attr/__init__.py",
    16,
    "in",
    "`._make` resolves `make_class` to the target"
   ],
   [
    "src/attrs/__init__.py",
    3,
    "out",
    "`attr` resolves `make_class` to ambiguous(dynamic module)"
   ],
   [
    "src/attrs/converters.py",
    3,
    "out",
    "star import of `attr.converters`, which does not export `make_class`"
   ],
   [
    "src/attrs/exceptions.py",
    3,
    "out",
    "star import of `attr.exceptions`, which does not export `make_class`"
   ],
   [
    "src/attrs/filters.py",
    3,
    "out",
    "star import of `attr.filters`, which does not export `make_class`"
   ],
   [
    "src/attrs/setters.py",
    3,
    "out",
    "star import of `attr.setters`, which does not export `make_class`"
   ],
   [
    "src/attrs/validators.py",
    3,
    "out",
    "star import of `attr.validators`, which does not export `make_class`"
   ],
   [
    "tests/attr_import_star.py",
    4,
    "out",
    "star import of `attr` binds `make_class` to ambiguous(dynamic module)"
   ],
   [
    "tests/strategies.py",
    17,
    "in",
    "`.utils` resolves `make_class` to the target"
   ],
   [
    "tests/test_dunders.py",
    18,
    "in",
    "`attr._make` resolves `make_class` to the target"
   ],
   [
    "tests/test_make.py",
    29,
    "in",
    "`attr._make` resolves `make_class` to the target"
   ],
   [
    "tests/utils.py",
    8,
    "in",
    "`attr._make` resolves `make_class` to the target"
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

Certificate complete. 5 import statements import this definition: `src/attr/__init__.py:16`, `tests/strategies.py:17`, `tests/test_dunders.py:18`, `tests/test_make.py:29`, `tests/utils.py:8`. In hindsight, 1 of 25 calls were not needed for the certificate: steps 21.

**Answer:** `{"statements": ["src/attr/__init__.py:16", "tests/strategies.py:17", "tests/test_dunders.py:18", "tests/test_make.py:29", "tests/utils.py:8"], "count": 5}`  
**Stopped:** certificate after 25 calls