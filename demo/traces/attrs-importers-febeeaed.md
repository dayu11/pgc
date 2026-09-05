# attrs-importers-febeeaed

**Repository:** attrs  
**Chain:** importers  
**Seed:** 0, prior 0ac2a510ad43644e, floor 25

## Task

`fields` is defined at `src/attr/_make.py:1924` (def). List every module-level import statement in the repository that brings in that definition, including through re-exports and star imports, as `path:line`.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N; bindings take effect in source order. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. A class derives from a definition when a base written as a bare name or `module.Name` resolves to it. A call site is `name(...)` where the bare name refers to the module-level binding (not a parameter or local). Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

Starting from the definition of `fields` at `src/attr/_make.py:1924`. Then I have to find every module-level import of that definition, which means a complete search, not a sample.

Next I will search the whole tree for imports of `fields` and star imports in one go; the search has to be complete before I can call the set final. Maybe nothing turns up. If it fits under the cap or it caps, I follow whatever it opens up.

**Call:** `grep('^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bfields\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*fields\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$', '.')`

**Response**: outcome `mid`

```
src/attr/__init__.py:25:    fields,
src/attr/_funcs.py:5:from ._make import _OBJ_SETATTR, NOTHING, fields
src/attrs/__init__.py:16:    fields,
src/attrs/__init__.pyi:33:from attr import fields as fields
src/attrs/converters.py:3:from attr.converters import *  # noqa: F403
src/attrs/exceptions.py:3:from attr.exceptions import *  # noqa: F403
src/attrs/filters.py:3:from attr.filters import *  # noqa: F403
src/attrs/setters.py:3:from attr.setters import *  # noqa: F403
src/attrs/validators.py:3:from attr.validators import *  # noqa: F403
tests/attr_import_star.py:4:from attr import *  # noqa: F403
tests/test_dunders.py:24:    fields,
tests/test_filters.py:11:from attr import fields
tests/test_forward_references.py:5:from attrs import define, fields, resolve_types
tests/test_funcs.py:19:from attr import asdict, assoc, astuple, evolve, fields, has
tests/test_make.py:42:    fields,
tests/test_mypy.yml:1384:            from other import *
tests/test_mypy.yml:1439:    from attrs import define, fields
tests/test_mypy.yml:1450:    from attrs import define, fields
tests/test_mypy.yml:1462:    from attrs import fields
tests/test_validators.py:14:from attr import _config, fields, has
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
   "desc": "search `.` for imports of `fields`"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "."
   ],
   "desc": "search `.` for star imports"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bfields\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*fields\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bfields\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*fields\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
   "v1": [
    23209880717,
    10098421760
   ],
   "v2": [
    23209880717,
    10098421760
   ],
   "p_cap": [
    5,
    32
   ],
   "forecast": {
    "zero": [
     17,
     32
    ],
    "mid": [
     5,
     16
    ],
    "cap": [
     5,
     32
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
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bfields\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*fields\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bfields\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*fields\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
   "v1": [
    1819974069461,
    388158086400
   ],
   "v2": [
    344724955207,
    129386028800
   ],
   "p_cap": [
    1,
    41
   ],
   "forecast": {
    "zero": [
     31,
     41
    ],
    "mid": [
     9,
     41
    ],
    "cap": [
     1,
     41
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
    389070645127,
    129386028800
   ],
   "v2": [
    344724955207,
    129386028800
   ],
   "p_cap": [
    1,
    18
   ],
   "forecast": {
    "zero": [
     13,
     18
    ],
    "mid": [
     2,
     9
    ],
    "cap": [
     1,
     18
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
  "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bfields\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*fields\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
  "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bfields\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*fields\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
  "provenance": "import and star lines under `.` in one call",
  "v2": [
   23209880717,
   10098421760
  ]
 },
 "forecast": {
  "zero": [
   17,
   32
  ],
  "mid": [
   5,
   16
  ],
  "cap": [
   5,
   32
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
   "word": "maybe",
   "p": [
    17,
    32
   ]
  }
 ],
 "adherence": null,
 "facts": [
  {
   "kind": "grep",
   "step": 1,
   "pattern": "^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bfields\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*fields\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$",
   "scope": ".",
   "hits": [
    [
     "src/attr/__init__.py",
     25
    ],
    [
     "src/attr/_funcs.py",
     5
    ],
    [
     "src/attrs/__init__.py",
     16
    ],
    [
     "src/attrs/__init__.pyi",
     33
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
     "tests/test_dunders.py",
     24
    ],
    [
     "tests/test_filters.py",
     11
    ],
    [
     "tests/test_forward_references.py",
     5
    ],
    [
     "tests/test_funcs.py",
     19
    ],
    [
     "tests/test_make.py",
     42
    ],
    [
     "tests/test_mypy.yml",
     1384
    ],
    [
     "tests/test_mypy.yml",
     1439
    ],
    [
     "tests/test_mypy.yml",
     1450
    ],
    [
     "tests/test_mypy.yml",
     1462
    ],
    [
     "tests/test_validators.py",
     14
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 1,
  "of": 1,
  "candidates": [
   "src/attr/__init__.py",
   "src/attr/_funcs.py",
   "src/attrs/__init__.py",
   "src/attrs/converters.py",
   "src/attrs/exceptions.py",
   "src/attrs/filters.py",
   "src/attrs/setters.py",
   "src/attrs/validators.py",
   "tests/attr_import_star.py",
   "tests/test_dunders.py",
   "tests/test_filters.py",
   "tests/test_forward_references.py",
   "tests/test_funcs.py",
   "tests/test_make.py",
   "tests/test_validators.py"
  ],
  "table": [
   [
    "src/attr/__init__.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/attr/_funcs.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/attrs/__init__.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/attrs/converters.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/attrs/exceptions.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/attrs/filters.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/attrs/setters.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/attrs/validators.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/attr_import_star.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_dunders.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests
```
</details>

## Step 2

20 matching lines anywhere for imports of `fields` or star imports, in `src/attr/__init__.py`, `src/attr/_funcs.py`, `src/attrs/__init__.py`, `src/attrs/__init__.pyi` and 13 more files, and the search was under the cap, so that is the complete set there.

Let me look at `tests/test_validators.py`'s top-level names for `fields`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `src/attr/__init__.py`'s top-level names for `fields`.

**Call:** `symbols('tests/test_validators.py', 'fields')`

**Response**: outcome `ok`

```
module tests/test_validators.py lines=1405 dynamic=no all=none
14 from fields <- attr fields
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
    "fields"
   ],
   "desc": "look at `src/attr/__init__.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attr/_funcs.py",
    "fields"
   ],
   "desc": "look at `src/attr/_funcs.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/__init__.py",
    "fields"
   ],
   "desc": "look at `src/attrs/__init__.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/converters.py",
    "fields"
   ],
   "desc": "look at `src/attrs/converters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/exceptions.py",
    "fields"
   ],
   "desc": "look at `src/attrs/exceptions.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "fields"
   ],
   "desc": "look at `src/attrs/filters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "fields"
   ],
   "desc": "look at `src/attrs/setters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "fields"
   ],
   "desc": "look at `src/attrs/validators.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "fields"
   ],
   "desc": "look at `tests/attr_import_star.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "fields"
   ],
   "desc": "look at `tests/test_dunders.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_filters.py",
    "fields"
   ],
   "desc": "look at `tests/test_filters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_forward_references.py",
    "fields"
   ],
   "desc": "look at `tests/test_forward_references.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "fields"
   ],
   "desc": "look at `tests/test_funcs.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "fields"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_validators.py",
    "fields"
   ],
   "desc": "look at `tests/test_validators.py`'s imports of `fields`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/__init__.py', 'fields')",
   "key": "[\"symbols\", [\"src/attr/__init__.py\", \"fields\"]]",
   "v1": [
    12519013,
    503150
   ],
   "v2": [
    6264538,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/_funcs.py', 'fields')",
   "key": "[\"symbols\", [\"src/attr/_funcs.py\", \"fields\"]]",
   "v1": [
    12519013,
    503150
   ],
   "v2": [
    6264538,
    251575
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
     "src/attr/_funcs.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/__init__.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/__init__.py\", \"fields\"]]",
   "v1": [
    12519013,
    503150
   ],
   "v2": [
    6264538,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/converters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/converters.py\", \"fields\"]]",
   "v1": [
    12519013,
    503150
   ],
   "v2": [
    6264538,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/exceptions.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/exceptions.py\", \"fields\"]]",
   "v1": [
    12519013,
    503150
   ],
   "v2": [
    6264538,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/filters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"fields\"]]",
   "v1": [
    12519013,
    503150
   ],
   "v2": [
    6264538,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"fields\"]]",
   "v1": [
    12519013,
    503150
   ],
   "v2": [
    6264538,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"fields\"]]",
   "v1": [
    12519013,
    503150
   ],
   "v2": [
    6264538,
    251575
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

## Step 3

The test module `tests/test_validators.py`: line 14 imports it from `attr`.

Tally: 0 import statements confirmed, 0 ruled out, 15 pending. The search itself is complete; what is left is checking the candidates.

I'll look at `src/attr/__init__.py`'s top-level names for `fields`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will list `./` to see what lives there.

**Call:** `symbols('src/attr/__init__.py', 'fields')`

**Response**: outcome `ok`

```
module src/attr/__init__.py lines=121 dynamic=yes all=static@45
16 from fields <- ._make fields
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
    "fields"
   ],
   "desc": "look at `src/attr/__init__.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attr/_funcs.py",
    "fields"
   ],
   "desc": "look at `src/attr/_funcs.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/__init__.py",
    "fields"
   ],
   "desc": "look at `src/attrs/__init__.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/converters.py",
    "fields"
   ],
   "desc": "look at `src/attrs/converters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/exceptions.py",
    "fields"
   ],
   "desc": "look at `src/attrs/exceptions.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "fields"
   ],
   "desc": "look at `src/attrs/filters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "fields"
   ],
   "desc": "look at `src/attrs/setters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "fields"
   ],
   "desc": "look at `src/attrs/validators.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "fields"
   ],
   "desc": "look at `tests/attr_import_star.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "fields"
   ],
   "desc": "look at `tests/test_dunders.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_filters.py",
    "fields"
   ],
   "desc": "look at `tests/test_filters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_forward_references.py",
    "fields"
   ],
   "desc": "look at `tests/test_forward_references.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "fields"
   ],
   "desc": "look at `tests/test_funcs.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "fields"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `fields`"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_validators.py",
    "attr"
   ],
   "desc": "find where `attr` (imported by `tests/test_validators.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    7575133,
    301890
   ],
   "v2": [
    18952927,
    754725
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
     "tests/test_validators.py",
     "attr"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/__init__.py', 'fields')",
   "key": "[\"symbols\", [\"src/attr/__init__.py\", \"fields\"]]",
   "v1": [
    12719143,
    503150
   ],
   "v2": [
    18952927,
    754725
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/_funcs.py', 'fields')",
   "key": "[\"symbols\", [\"src/attr/_funcs.py\", \"fields\"]]",
   "v1": [
    12719143,
    503150
   ],
   "v2": [
    18952927,
    754725
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
     "src/attr/_funcs.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/__init__.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/__init__.py\", \"fields\"]]",
   "v1": [
    12719143,
    503150
   ],
   "v2": [
    18952927,
    754725
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/converters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/converters.py\", \"fields\"]]",
   "v1": [
    12719143,
    503150
   ],
   "v2": [
    18952927,
    754725
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/exceptions.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/exceptions.py\", \"fields\"]]",
   "v1": [
    12719143,
    503150
   ],
   "v2": [
    18952927,
    754725
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/filters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"fields\"]]",
   "v1": [
    12719143,
    503150
   ],
   "v2": [
    18952927,
    754725
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"fields\"]]",
   "v1": [
    12719143,
    503150
   ],
   "v2": [
    18952927,
    754725
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

## Step 4

The package `src/attr`: line 16 imports it from `._make`. Careful: this module manipulates its namespace dynamically, so static resolution is not reliable here.

Tally: 0 import statements confirmed, 0 ruled out, 15 pending. The search itself is complete; what is left is checking the candidates.

Still open: check the top-level names of `src/attr/_make.py` for `fields`; look at `src/attr/_funcs.py`'s imports of `fields`; look at `src/attrs/__init__.py`'s imports of `fields`; and 12 more.

I'll list `./` to see what lives there; the listing settles whether the import is a module, a package, or not here at all. Very likely the listing fits. If the listing is too long, I will look at `src/attr/_make.py`'s top-level names for `fields`.

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
   "kind": "bindings",
   "key": [
    "bindings",
    "src/attr/_make.py",
    "fields"
   ],
   "desc": "check the top-level names of `src/attr/_make.py` for `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attr/_funcs.py",
    "fields"
   ],
   "desc": "look at `src/attr/_funcs.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/__init__.py",
    "fields"
   ],
   "desc": "look at `src/attrs/__init__.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/converters.py",
    "fields"
   ],
   "desc": "look at `src/attrs/converters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/exceptions.py",
    "fields"
   ],
   "desc": "look at `src/attrs/exceptions.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "fields"
   ],
   "desc": "look at `src/attrs/filters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "fields"
   ],
   "desc": "look at `src/attrs/setters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "fields"
   ],
   "desc": "look at `src/attrs/validators.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "fields"
   ],
   "desc": "look at `tests/attr_import_star.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "fields"
   ],
   "desc": "look at `tests/test_dunders.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_filters.py",
    "fields"
   ],
   "desc": "look at `tests/test_filters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_forward_references.py",
    "fields"
   ],
   "desc": "look at `tests/test_forward_references.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "fields"
   ],
   "desc": "look at `tests/test_funcs.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "fields"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `fields`"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_validators.py",
    "attr"
   ],
   "desc": "find where `attr` (imported by `tests/test_validators.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    381523210397,
    15578630930
   ],
   "v2": [
    381523210397,
    15578630930
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
     "tests/test_validators.py",
     "attr"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/_make.py', 'fields')",
   "key": "[\"symbols\", [\"src/attr/_make.py\", \"fields\"]]",
   "v1": [
    576179473328,
    23367946395
   ],
   "v2": [
    381523210397,
    15578630930
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     418,
     447
    ],
    "reexport": [
     11,
     447
    ],
    "star": [
     1,
     447
    ],
    "none": [
     17,
     447
    ]
   },
   "serves": [
    [
     "bindings",
     "src/attr/_make.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/_funcs.py', 'fields')",
   "key": "[\"symbols\", [\"src/attr/_funcs.py\", \"fields\"]]",
   "v1": [
    5766468322559,
    233679463950
   ],
   "v2": [
    954586957539,
    38946577325
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
     "src/attr/_funcs.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/__init__.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/__init__.py\", \"fields\"]]",
   "v1": [
    5766468322559,
    233679463950
   ],
   "v2": [
    954586957539,
    38946577325
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/converters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/converters.py\", \"fields\"]]",
   "v1": [
    5766468322559,
    233679463950
   ],
   "v2": [
    954586957539,
    38946577325
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/exceptions.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/exceptions.py\", \"fields\"]]",
   "v1": [
    5766468322559,
    233679463950
   ],
   "v2": [
    954586957539,
    38946577325
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/filters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"fields\"]]",
   "v1": [
    5766468322559,
    233679463950
   ],
   "v2": [
    954586957539,
    38946577325
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\",
```
</details>

## Step 5

`./` has 15 entries: there is no `attr` here.

Let me look at `src/attr/_make.py`'s top-level names for `fields`; that settles what the name means there. Almost certainly it is defined right there. If the name is not bound there or it is re-exported from somewhere else, I will outline `src/attr.py` directly, which both checks that the file exists and shows me `_config`.

**Call:** `symbols('src/attr/_make.py', 'fields')`

**Response**: outcome `def`

```
module src/attr/_make.py lines=3463 dynamic=no all=none
1924 def fields
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
    "fields"
   ],
   "desc": "check the top-level names of `src/attr/_make.py` for `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attr/_funcs.py",
    "fields"
   ],
   "desc": "look at `src/attr/_funcs.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/__init__.py",
    "fields"
   ],
   "desc": "look at `src/attrs/__init__.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/converters.py",
    "fields"
   ],
   "desc": "look at `src/attrs/converters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/exceptions.py",
    "fields"
   ],
   "desc": "look at `src/attrs/exceptions.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "fields"
   ],
   "desc": "look at `src/attrs/filters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "fields"
   ],
   "desc": "look at `src/attrs/setters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "fields"
   ],
   "desc": "look at `src/attrs/validators.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "fields"
   ],
   "desc": "look at `tests/attr_import_star.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "fields"
   ],
   "desc": "look at `tests/test_dunders.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_filters.py",
    "fields"
   ],
   "desc": "look at `tests/test_filters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_forward_references.py",
    "fields"
   ],
   "desc": "look at `tests/test_forward_references.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "fields"
   ],
   "desc": "look at `tests/test_funcs.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "fields"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `fields`"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_validators.py",
    "attr"
   ],
   "desc": "find where `attr` (imported by `tests/test_validators.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr.py', '_config')",
   "key": "[\"symbols\", [\"src/attr.py\", \"_config\"]]",
   "v1": [
    90809481107569,
    3808975262385
   ],
   "v2": [
    90809481107569,
    3808975262385
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     61864,
     72861
    ],
    "reexport": [
     1628,
     72861
    ],
    "star": [
     148,
     72861
    ],
    "none": [
     2516,
     72861
    ],
    "missing": [
     15,
     163
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_validators.py",
     "attr"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/_make.py', 'fields')",
   "key": "[\"symbols\", [\"src/attr/_make.py\", \"fields\"]]",
   "v1": [
    576179473328,
    23367946395
   ],
   "v2": [
    90809481107569,
    3808975262385
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     418,
     447
    ],
    "reexport": [
     11,
     447
    ],
    "star": [
     1,
     447
    ],
    "none": [
     17,
     447
    ]
   },
   "serves": [
    [
     "bindings",
     "src/attr/_make.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/_funcs.py', 'fields')",
   "key": "[\"symbols\", [\"src/attr/_funcs.py\", \"fields\"]]",
   "v1": [
    5766468322559,
    233679463950
   ],
   "v2": [
    908856606128167,
    38089752623850
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
     "src/attr/_funcs.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/__init__.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/__init__.py\", \"fields\"]]",
   "v1": [
    5766468322559,
    233679463950
   ],
   "v2": [
    908856606128167,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/converters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/converters.py\", \"fields\"]]",
   "v1": [
    5766468322559,
    233679463950
   ],
   "v2": [
    908856606128167,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/exceptions.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/exceptions.py\", \"fields\"]]",
   "v1": [
    5766468322559,
    233679463950
   ],
   "v2": [
    908856606128167,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/filters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"fields\"]]",
   "v1": [
    5766468322559,
    233679463950
   ],
   "v2": [
    908856606128167,
    38089752623850
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
    "cap":
```
</details>

## Step 6

There it is: `fields` is a function at `src/attr/_make.py:1924`.

Tally: 1 import statements confirmed, 0 ruled out, 14 pending. The search itself is complete; what is left is checking the candidates.

Next I will outline `src/attr.py` directly, which both checks that the file exists and shows me `_config`; if `attr` is a plain module that is where it has to be. Very likely it is defined right there. If the file does not exist or the name is not bound there, I will look at `src/attr/_funcs.py`'s top-level names for `fields`.

**Call:** `symbols('src/attr.py', '_config')`

**Response**: outcome `missing`

```
error: not a python file: src/attr.py
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attr/_funcs.py",
    "fields"
   ],
   "desc": "look at `src/attr/_funcs.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/__init__.py",
    "fields"
   ],
   "desc": "look at `src/attrs/__init__.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/converters.py",
    "fields"
   ],
   "desc": "look at `src/attrs/converters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/exceptions.py",
    "fields"
   ],
   "desc": "look at `src/attrs/exceptions.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "fields"
   ],
   "desc": "look at `src/attrs/filters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "fields"
   ],
   "desc": "look at `src/attrs/setters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "fields"
   ],
   "desc": "look at `src/attrs/validators.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "fields"
   ],
   "desc": "look at `tests/attr_import_star.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "fields"
   ],
   "desc": "look at `tests/test_dunders.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_filters.py",
    "fields"
   ],
   "desc": "look at `tests/test_filters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_forward_references.py",
    "fields"
   ],
   "desc": "look at `tests/test_forward_references.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "fields"
   ],
   "desc": "look at `tests/test_funcs.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "fields"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `fields`"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_validators.py",
    "attr"
   ],
   "desc": "find where `attr` (imported by `tests/test_validators.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr.py', '_config')",
   "key": "[\"symbols\", [\"src/attr.py\", \"_config\"]]",
   "v1": [
    17358035011258,
    761795052477
   ],
   "v2": [
    868663545615377,
    38089752623850
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     61864,
     72861
    ],
    "reexport": [
     1628,
     72861
    ],
    "star": [
     148,
     72861
    ],
    "none": [
     2516,
     72861
    ],
    "missing": [
     15,
     163
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_validators.py",
     "attr"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/_funcs.py', 'fields')",
   "key": "[\"symbols\", [\"src/attr/_funcs.py\", \"fields\"]]",
   "v1": [
    11885213,
    503150
   ],
   "v2": [
    868663545615377,
    38089752623850
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
     "src/attr/_funcs.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/__init__.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/__init__.py\", \"fields\"]]",
   "v1": [
    11885213,
    503150
   ],
   "v2": [
    868663545615377,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/converters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/converters.py\", \"fields\"]]",
   "v1": [
    11885213,
    503150
   ],
   "v2": [
    868663545615377,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/exceptions.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/exceptions.py\", \"fields\"]]",
   "v1": [
    11885213,
    503150
   ],
   "v2": [
    868663545615377,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/filters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"fields\"]]",
   "v1": [
    11885213,
    503150
   ],
   "v2": [
    868663545615377,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"fields\"]]",
   "v1": [
    11885213,
    503150
   ],
   "v2": [
    868663545615377,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"fields\"]]",
   "v1": [
    11885213,
    503150
   ],
   "v2": [
    8
```
</details>

## Step 7

Not what I expected: there is no `src/attr.py`, so `attr` is either a package (`src/attr/__init__.py`) or not in this repository at all.

Next I will look at `src/attr/_funcs.py`'s top-level names for `fields`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `src/attrs/__init__.py`'s top-level names for `fields`.

**Call:** `symbols('src/attr/_funcs.py', 'fields')`

**Response**: outcome `ok`

```
module src/attr/_funcs.py lines=496 dynamic=no all=none
5 from fields <- ._make fields
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attr/_funcs.py",
    "fields"
   ],
   "desc": "look at `src/attr/_funcs.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/__init__.py",
    "fields"
   ],
   "desc": "look at `src/attrs/__init__.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/converters.py",
    "fields"
   ],
   "desc": "look at `src/attrs/converters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/exceptions.py",
    "fields"
   ],
   "desc": "look at `src/attrs/exceptions.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "fields"
   ],
   "desc": "look at `src/attrs/filters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "fields"
   ],
   "desc": "look at `src/attrs/setters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "fields"
   ],
   "desc": "look at `src/attrs/validators.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "fields"
   ],
   "desc": "look at `tests/attr_import_star.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "fields"
   ],
   "desc": "look at `tests/test_dunders.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_filters.py",
    "fields"
   ],
   "desc": "look at `tests/test_filters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_forward_references.py",
    "fields"
   ],
   "desc": "look at `tests/test_forward_references.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "fields"
   ],
   "desc": "look at `tests/test_funcs.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "fields"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `fields`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/_funcs.py', 'fields')",
   "key": "[\"symbols\", [\"src/attr/_funcs.py\", \"fields\"]]",
   "v1": [
    10851153,
    503150
   ],
   "v2": [
    5430608,
    251575
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
     "src/attr/_funcs.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/__init__.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/__init__.py\", \"fields\"]]",
   "v1": [
    10851153,
    503150
   ],
   "v2": [
    5430608,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/converters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/converters.py\", \"fields\"]]",
   "v1": [
    10851153,
    503150
   ],
   "v2": [
    5430608,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/exceptions.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/exceptions.py\", \"fields\"]]",
   "v1": [
    10851153,
    503150
   ],
   "v2": [
    5430608,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/filters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"fields\"]]",
   "v1": [
    10851153,
    503150
   ],
   "v2": [
    5430608,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"fields\"]]",
   "v1": [
    10851153,
    503150
   ],
   "v2": [
    5430608,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"fields\"]]",
   "v1": [
    10851153,
    503150
   ],
   "v2": [
    5430608,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'fields')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"fields\"]]",
   "v1": [
    10851153,
    503150
   ],
   "v2": [
    5430608,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_dunders.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_dunders.py\", \"fields\"]]",
   "v1": [
    10851153,
    503150
   ],
   "v2": [
  
```
</details>

## Step 8

`src/attr/_funcs.py`: line 5 imports it from `._make`.

Tally: 2 import statements confirmed, 1 ruled out, 12 pending. The search itself is complete; what is left is checking the candidates.

Still open: look at `src/attrs/__init__.py`'s imports of `fields`; look at `src/attrs/converters.py`'s imports of `fields`; look at `src/attrs/exceptions.py`'s imports of `fields`; and 9 more.

I'll look at `src/attrs/__init__.py`'s top-level names for `fields`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `src/attrs/converters.py`'s top-level names for `fields`.

**Call:** `symbols('src/attrs/__init__.py', 'fields')`

**Response**: outcome `ok`

```
module src/attrs/__init__.py lines=77 dynamic=yes all=static@31
3 from fields <- attr fields
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/__init__.py",
    "fields"
   ],
   "desc": "look at `src/attrs/__init__.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/converters.py",
    "fields"
   ],
   "desc": "look at `src/attrs/converters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/exceptions.py",
    "fields"
   ],
   "desc": "look at `src/attrs/exceptions.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "fields"
   ],
   "desc": "look at `src/attrs/filters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "fields"
   ],
   "desc": "look at `src/attrs/setters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "fields"
   ],
   "desc": "look at `src/attrs/validators.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "fields"
   ],
   "desc": "look at `tests/attr_import_star.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "fields"
   ],
   "desc": "look at `tests/test_dunders.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_filters.py",
    "fields"
   ],
   "desc": "look at `tests/test_filters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_forward_references.py",
    "fields"
   ],
   "desc": "look at `tests/test_forward_references.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "fields"
   ],
   "desc": "look at `tests/test_funcs.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "fields"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `fields`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attrs/__init__.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/__init__.py\", \"fields\"]]",
   "v1": [
    10017223,
    503150
   ],
   "v2": [
    5013643,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/converters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/converters.py\", \"fields\"]]",
   "v1": [
    10017223,
    503150
   ],
   "v2": [
    5013643,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/exceptions.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/exceptions.py\", \"fields\"]]",
   "v1": [
    10017223,
    503150
   ],
   "v2": [
    5013643,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/filters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"fields\"]]",
   "v1": [
    10017223,
    503150
   ],
   "v2": [
    5013643,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"fields\"]]",
   "v1": [
    10017223,
    503150
   ],
   "v2": [
    5013643,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"fields\"]]",
   "v1": [
    10017223,
    503150
   ],
   "v2": [
    5013643,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'fields')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"fields\"]]",
   "v1": [
    10017223,
    503150
   ],
   "v2": [
    5013643,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_dunders.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_dunders.py\", \"fields\"]]",
   "v1": [
    10017223,
    503150
   ],
   "v2": [
    5013643,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_filters.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_filters.py\", \"fields\"]]",
   "v1": [
    10017223,
    503150
   ],
   "v2": [
    5013643,
    251575
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
  
```
</details>

## Step 9

The package `src/attrs`: line 3 imports it from `attr`. Careful: this module manipulates its namespace dynamically, so static resolution is not reliable here.

Tally: 2 import statements confirmed, 2 ruled out, 11 pending. The search itself is complete; what is left is checking the candidates.

Let me look at `src/attrs/converters.py`'s top-level names for `fields`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `src/attrs/exceptions.py`'s top-level names for `fields`.

**Call:** `symbols('src/attrs/converters.py', 'fields')`

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
    "fields"
   ],
   "desc": "look at `src/attrs/converters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/exceptions.py",
    "fields"
   ],
   "desc": "look at `src/attrs/exceptions.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "fields"
   ],
   "desc": "look at `src/attrs/filters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "fields"
   ],
   "desc": "look at `src/attrs/setters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "fields"
   ],
   "desc": "look at `src/attrs/validators.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "fields"
   ],
   "desc": "look at `tests/attr_import_star.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "fields"
   ],
   "desc": "look at `tests/test_dunders.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_filters.py",
    "fields"
   ],
   "desc": "look at `tests/test_filters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_forward_references.py",
    "fields"
   ],
   "desc": "look at `tests/test_forward_references.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "fields"
   ],
   "desc": "look at `tests/test_funcs.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "fields"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `fields`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attrs/converters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/converters.py\", \"fields\"]]",
   "v1": [
    9183293,
    503150
   ],
   "v2": [
    4596678,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/exceptions.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/exceptions.py\", \"fields\"]]",
   "v1": [
    9183293,
    503150
   ],
   "v2": [
    4596678,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/filters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"fields\"]]",
   "v1": [
    9183293,
    503150
   ],
   "v2": [
    4596678,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"fields\"]]",
   "v1": [
    9183293,
    503150
   ],
   "v2": [
    4596678,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"fields\"]]",
   "v1": [
    9183293,
    503150
   ],
   "v2": [
    4596678,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'fields')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"fields\"]]",
   "v1": [
    9183293,
    503150
   ],
   "v2": [
    4596678,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_dunders.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_dunders.py\", \"fields\"]]",
   "v1": [
    9183293,
    503150
   ],
   "v2": [
    4596678,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_filters.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_filters.py\", \"fields\"]]",
   "v1": [
    9183293,
    503150
   ],
   "v2": [
    4596678,
    251575
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
     "tests/test_filters.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_forward_references.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_forward_references.py\", \"fields\"]]",
   "v1": [
    9183293,
    503150
   ],
   "v2": [
    4596678,
    251575
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
     "tests/test_forward_references.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_funcs.py', 'fields
```
</details>

## Step 10

`src/attrs/converters.py` matched the search but has no module-level import of `fields`. It also star-imports `attr.converters`, which could carry the name, so that needs checking.

Tally: 2 import statements confirmed, 2 ruled out, 11 pending. The search itself is complete; what is left is checking the candidates.

Let me look at `src/attrs/exceptions.py`'s top-level names for `fields`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will outline `src/attr/converters.py` directly, which both checks that the file exists and shows me `fields`.

**Call:** `symbols('src/attrs/exceptions.py', 'fields')`

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
   "desc": "find where `attr.converters` (imported by `src/attrs/converters.py`) lives"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/exceptions.py",
    "fields"
   ],
   "desc": "look at `src/attrs/exceptions.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "fields"
   ],
   "desc": "look at `src/attrs/filters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "fields"
   ],
   "desc": "look at `src/attrs/setters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "fields"
   ],
   "desc": "look at `src/attrs/validators.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "fields"
   ],
   "desc": "look at `tests/attr_import_star.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "fields"
   ],
   "desc": "look at `tests/test_dunders.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_filters.py",
    "fields"
   ],
   "desc": "look at `tests/test_filters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_forward_references.py",
    "fields"
   ],
   "desc": "look at `tests/test_forward_references.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "fields"
   ],
   "desc": "look at `tests/test_funcs.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "fields"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `fields`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/converters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attr/converters.py\", \"fields\"]]",
   "v1": [
    67850979544649,
    3808975262385
   ],
   "v2": [
    679271590498967,
    38089752623850
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     61864,
     72861
    ],
    "reexport": [
     1628,
     72861
    ],
    "star": [
     148,
     72861
    ],
    "none": [
     2516,
     72861
    ],
    "missing": [
     15,
     163
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
   "call": "symbols('src/attrs/exceptions.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/exceptions.py\", \"fields\"]]",
   "v1": [
    9383423,
    503150
   ],
   "v2": [
    679271590498967,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/filters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"fields\"]]",
   "v1": [
    9383423,
    503150
   ],
   "v2": [
    679271590498967,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"fields\"]]",
   "v1": [
    9383423,
    503150
   ],
   "v2": [
    679271590498967,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"fields\"]]",
   "v1": [
    9383423,
    503150
   ],
   "v2": [
    679271590498967,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'fields')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"fields\"]]",
   "v1": [
    9383423,
    503150
   ],
   "v2": [
    679271590498967,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_dunders.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_dunders.py\", \"fields\"]]",
   "v1": [
    9383423,
    503150
   ],
   "v2": [
    679271590498967,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_filters.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_filters.py\", \"fields\"]]",
   "v1": [
    9383423,
    503150
   ],
   "v2": [
    679271590498967,
    38089752623850
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
     "tests/test_filters.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_forward_references.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_forward_references.py\", \"fields\"]]",
   "v1": [
    9383423,
    503150
   ]
```
</details>

## Step 11

`src/attrs/exceptions.py` matched the search but has no module-level import of `fields`. It also star-imports `attr.exceptions`, which could carry the name, so that needs checking.

Tally: 2 import statements confirmed, 2 ruled out, 11 pending. The search itself is complete; what is left is checking the candidates.

I'll outline `src/attr/converters.py` directly, which both checks that the file exists and shows me `fields`; if `attr.converters` is a plain module that is where it has to be. Very likely it is defined right there. If the file does not exist, I will list `src/attr/` to see what lives there; if the name is not bound there or it is re-exported from somewhere else, I will outline `src/attr/exceptions.py` directly, which both checks that the file exists and shows me `fields`.

**Call:** `symbols('src/attr/converters.py', 'fields')`

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
   "desc": "find where `attr.converters` (imported by `src/attrs/converters.py`) lives"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/exceptions.py",
    "attr.exceptions"
   ],
   "desc": "find where `attr.exceptions` (imported by `src/attrs/exceptions.py`) lives"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "fields"
   ],
   "desc": "look at `src/attrs/filters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "fields"
   ],
   "desc": "look at `src/attrs/setters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "fields"
   ],
   "desc": "look at `src/attrs/validators.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "fields"
   ],
   "desc": "look at `tests/attr_import_star.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "fields"
   ],
   "desc": "look at `tests/test_dunders.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_filters.py",
    "fields"
   ],
   "desc": "look at `tests/test_filters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_forward_references.py",
    "fields"
   ],
   "desc": "look at `tests/test_forward_references.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "fields"
   ],
   "desc": "look at `tests/test_funcs.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "fields"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `fields`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/converters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attr/converters.py\", \"fields\"]]",
   "v1": [
    69366015258176,
    3808975262385
   ],
   "v2": [
    2406646671082404769,
    138452441812432365
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     61864,
     72861
    ],
    "reexport": [
     1628,
     72861
    ],
    "star": [
     148,
     72861
    ],
    "none": [
     2516,
     72861
    ],
    "missing": [
     15,
     163
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
   "call": "symbols('src/attr/exceptions.py', 'fields')",
   "key": "[\"symbols\", [\"src/attr/exceptions.py\", \"fields\"]]",
   "v1": [
    69366015258176,
    3808975262385
   ],
   "v2": [
    2406646671082404769,
    138452441812432365
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     61864,
     72861
    ],
    "reexport": [
     1628,
     72861
    ],
    "star": [
     148,
     72861
    ],
    "none": [
     2516,
     72861
    ],
    "missing": [
     15,
     163
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
    202771732,
    11220245
   ],
   "v2": [
    9124536743,
    504911025
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
   "call": "symbols('src/attrs/filters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"fields\"]]",
   "v1": [
    9583553,
    503150
   ],
   "v2": [
    2029961369,
    112202450
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"fields\"]]",
   "v1": [
    9583553,
    503150
   ],
   "v2": [
    2029961369,
    112202450
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"fields\"]]",
   "v1": [
    9583553,
    503150
   ],
   "v2": [
    2029961369,
    112202450
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'fields')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"fields\"]]",
   "v1": [
    9583553,
    503150
   ],
   "v2": [
    2029961369,
    112202450
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_dunders.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_dunders.py\", \"fields\"]]",
   "v1": [
    9583553,
    503150
   ],
   "v2": [
    2029961369,
    112202450
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

```
</details>

## Step 12

Not what I expected: `src/attr/converters.py` does not bind `fields` at module level at all.

Tally: 2 import statements confirmed, 2 ruled out, 11 pending. The search itself is complete; what is left is checking the candidates.

Still open: read what `src/attr/converters.py` exports; find where `attr.exceptions` (imported by `src/attrs/exceptions.py`) lives; look at `src/attrs/filters.py`'s imports of `fields`; and 8 more.

Next I will outline `src/attr/exceptions.py` directly, which both checks that the file exists and shows me `fields`; if `attr.exceptions` is a plain module that is where it has to be. Very likely it is defined right there. If the file does not exist or the name is not bound there, I will look at `src/attrs/filters.py`'s top-level names for `fields`.

**Call:** `symbols('src/attr/exceptions.py', 'fields')`

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
   "desc": "read what `src/attr/converters.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/exceptions.py",
    "attr.exceptions"
   ],
   "desc": "find where `attr.exceptions` (imported by `src/attrs/exceptions.py`) lives"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "fields"
   ],
   "desc": "look at `src/attrs/filters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "fields"
   ],
   "desc": "look at `src/attrs/setters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "fields"
   ],
   "desc": "look at `src/attrs/validators.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "fields"
   ],
   "desc": "look at `tests/attr_import_star.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "fields"
   ],
   "desc": "look at `tests/test_dunders.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_filters.py",
    "fields"
   ],
   "desc": "look at `tests/test_filters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_forward_references.py",
    "fields"
   ],
   "desc": "look at `tests/test_forward_references.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "fields"
   ],
   "desc": "look at `tests/test_funcs.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "fields"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `fields`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/exceptions.py', 'fields')",
   "key": "[\"symbols\", [\"src/attr/exceptions.py\", \"fields\"]]",
   "v1": [
    65346889636487,
    3808975262385
   ],
   "v2": [
    654230691417347,
    38089752623850
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     61864,
     72861
    ],
    "reexport": [
     1628,
     72861
    ],
    "star": [
     148,
     72861
    ],
    "none": [
     2516,
     72861
    ],
    "missing": [
     15,
     163
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
   "call": "symbols('src/attrs/filters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"fields\"]]",
   "v1": [
    9052643,
    503150
   ],
   "v2": [
    654230691417347,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"fields\"]]",
   "v1": [
    9052643,
    503150
   ],
   "v2": [
    654230691417347,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"fields\"]]",
   "v1": [
    9052643,
    503150
   ],
   "v2": [
    654230691417347,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'fields')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"fields\"]]",
   "v1": [
    9052643,
    503150
   ],
   "v2": [
    654230691417347,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_dunders.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_dunders.py\", \"fields\"]]",
   "v1": [
    9052643,
    503150
   ],
   "v2": [
    654230691417347,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_filters.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_filters.py\", \"fields\"]]",
   "v1": [
    9052643,
    503150
   ],
   "v2": [
    654230691417347,
    38089752623850
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
     "tests/test_filters.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_forward_references.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_forward_references.py\", \"fields\"]]",
   "v1": [
    9052643,
    503150
   ],
   "v2": [
    654230691417347,
    38089752623850
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
     "tests/test_forward_references.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_funcs.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_funcs.py\", \"fields\"]]",
   "v1": [
    9052643,
    503150
   ],
   "v2": [
    654230691417347,
 
```
</details>

## Step 13

Interesting: `src/attr/exceptions.py` does not bind `fields` at module level at all.

Tally: 2 import statements confirmed, 3 ruled out, 10 pending. The search itself is complete; what is left is checking the candidates.

Let me look at `src/attrs/filters.py`'s top-level names for `fields`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `src/attrs/setters.py`'s top-level names for `fields`.

**Call:** `symbols('src/attrs/filters.py', 'fields')`

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
   "desc": "read what `src/attr/converters.py` exports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "fields"
   ],
   "desc": "look at `src/attrs/filters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "fields"
   ],
   "desc": "look at `src/attrs/setters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "fields"
   ],
   "desc": "look at `src/attrs/validators.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "fields"
   ],
   "desc": "look at `tests/attr_import_star.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "fields"
   ],
   "desc": "look at `tests/test_dunders.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_filters.py",
    "fields"
   ],
   "desc": "look at `tests/test_filters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_forward_references.py",
    "fields"
   ],
   "desc": "look at `tests/test_forward_references.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "fields"
   ],
   "desc": "look at `tests/test_funcs.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "fields"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `fields`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attrs/filters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"fields\"]]",
   "v1": [
    8018583,
    503150
   ],
   "v2": [
    4014323,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"fields\"]]",
   "v1": [
    8018583,
    503150
   ],
   "v2": [
    4014323,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"fields\"]]",
   "v1": [
    8018583,
    503150
   ],
   "v2": [
    4014323,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'fields')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"fields\"]]",
   "v1": [
    8018583,
    503150
   ],
   "v2": [
    4014323,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_dunders.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_dunders.py\", \"fields\"]]",
   "v1": [
    8018583,
    503150
   ],
   "v2": [
    4014323,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_filters.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_filters.py\", \"fields\"]]",
   "v1": [
    8018583,
    503150
   ],
   "v2": [
    4014323,
    251575
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
     "tests/test_filters.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_forward_references.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_forward_references.py\", \"fields\"]]",
   "v1": [
    8018583,
    503150
   ],
   "v2": [
    4014323,
    251575
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
     "tests/test_forward_references.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_funcs.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_funcs.py\", \"fields\"]]",
   "v1": [
    8018583,
    503150
   ],
   "v2": [
    4014323,
    251575
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
     "tests/test_funcs.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"fields\"]]",
   "v1": [
    8018583,
    503150
   ],
   "v2": [
    4014323,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    25778209,
    1610080
   ],
   "v2": [
    129052053,
    8050400
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

```
</details>

## Step 14

`src/attrs/filters.py` matched the search but has no module-level import of `fields`. It also star-imports `attr.filters`, which could carry the name, so that needs checking.

Tally: 2 import statements confirmed, 3 ruled out, 10 pending. The search itself is complete; what is left is checking the candidates.

Next I will look at `src/attrs/setters.py`'s top-level names for `fields`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will outline `src/attr/filters.py` directly, which both checks that the file exists and shows me `fields`.

**Call:** `symbols('src/attrs/setters.py', 'fields')`

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
   "desc": "read what `src/attr/converters.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/filters.py",
    "attr.filters"
   ],
   "desc": "find where `attr.filters` (imported by `src/attrs/filters.py`) lives"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "fields"
   ],
   "desc": "look at `src/attrs/setters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "fields"
   ],
   "desc": "look at `src/attrs/validators.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "fields"
   ],
   "desc": "look at `tests/attr_import_star.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "fields"
   ],
   "desc": "look at `tests/test_dunders.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_filters.py",
    "fields"
   ],
   "desc": "look at `tests/test_filters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_forward_references.py",
    "fields"
   ],
   "desc": "look at `tests/test_forward_references.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "fields"
   ],
   "desc": "look at `tests/test_funcs.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "fields"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `fields`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/filters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attr/filters.py\", \"fields\"]]",
   "v1": [
    11806764893188,
    761795052477
   ],
   "v2": [
    591100039711877,
    38089752623850
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     61864,
     72861
    ],
    "reexport": [
     1628,
     72861
    ],
    "star": [
     148,
     72861
    ],
    "none": [
     2516,
     72861
    ],
    "missing": [
     15,
     163
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
   "call": "symbols('src/attrs/setters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"fields\"]]",
   "v1": [
    8218713,
    503150
   ],
   "v2": [
    591100039711877,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"fields\"]]",
   "v1": [
    8218713,
    503150
   ],
   "v2": [
    591100039711877,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'fields')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"fields\"]]",
   "v1": [
    8218713,
    503150
   ],
   "v2": [
    591100039711877,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_dunders.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_dunders.py\", \"fields\"]]",
   "v1": [
    8218713,
    503150
   ],
   "v2": [
    591100039711877,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_filters.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_filters.py\", \"fields\"]]",
   "v1": [
    8218713,
    503150
   ],
   "v2": [
    591100039711877,
    38089752623850
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
     "tests/test_filters.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_forward_references.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_forward_references.py\", \"fields\"]]",
   "v1": [
    8218713,
    503150
   ],
   "v2": [
    591100039711877,
    38089752623850
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
     "tests/test_forward_references.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_funcs.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_funcs.py\", \"fields\"]]",
   "v1": [
    8218713,
    503150
   ],
   "v2": [
    591100039711877,
    38089752623850
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
     "tests/test_funcs.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"fields\"]]",
   "v1": [
    8218713,
    503150
   ],
   "v2": [
    591100039711877,
    38089752623850
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
     "tests/
```
</details>

## Step 15

`src/attrs/setters.py` matched the search but has no module-level import of `fields`. It also star-imports `attr.setters`, which could carry the name, so that needs checking.

Tally: 2 import statements confirmed, 3 ruled out, 10 pending. The search itself is complete; what is left is checking the candidates.

Let me outline `src/attr/filters.py` directly, which both checks that the file exists and shows me `fields`; if `attr.filters` is a plain module that is where it has to be. Very likely it is defined right there. If the file does not exist, I will list `src/attr/` to see what lives there; if the name is not bound there or it is re-exported from somewhere else, I will outline `src/attr/setters.py` directly, which both checks that the file exists and shows me `fields`.

**Call:** `symbols('src/attr/filters.py', 'fields')`

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
   "desc": "read what `src/attr/converters.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/filters.py",
    "attr.filters"
   ],
   "desc": "find where `attr.filters` (imported by `src/attrs/filters.py`) lives"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/setters.py",
    "attr.setters"
   ],
   "desc": "find where `attr.setters` (imported by `src/attrs/setters.py`) lives"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "fields"
   ],
   "desc": "look at `src/attrs/validators.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "fields"
   ],
   "desc": "look at `tests/attr_import_star.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "fields"
   ],
   "desc": "look at `tests/test_dunders.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_filters.py",
    "fields"
   ],
   "desc": "look at `tests/test_filters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_forward_references.py",
    "fields"
   ],
   "desc": "look at `tests/test_forward_references.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "fields"
   ],
   "desc": "look at `tests/test_funcs.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "fields"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `fields`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/filters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attr/filters.py\", \"fields\"]]",
   "v1": [
    60548860179467,
    3808975262385
   ],
   "v2": [
    2086151901126411328,
    138452441812432365
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     61864,
     72861
    ],
    "reexport": [
     1628,
     72861
    ],
    "star": [
     148,
     72861
    ],
    "none": [
     2516,
     72861
    ],
    "missing": [
     15,
     163
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
   "call": "symbols('src/attr/setters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attr/setters.py\", \"fields\"]]",
   "v1": [
    60548860179467,
    3808975262385
   ],
   "v2": [
    2086151901126411328,
    138452441812432365
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     61864,
     72861
    ],
    "reexport": [
     1628,
     72861
    ],
    "star": [
     148,
     72861
    ],
    "none": [
     2516,
     72861
    ],
    "missing": [
     15,
     163
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
    176798699,
    11220245
   ],
   "v2": [
    7955750258,
    504911025
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
   "call": "symbols('src/attrs/validators.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"fields\"]]",
   "v1": [
    8418843,
    503150
   ],
   "v2": [
    1770231039,
    112202450
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'fields')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"fields\"]]",
   "v1": [
    8418843,
    503150
   ],
   "v2": [
    1770231039,
    112202450
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_dunders.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_dunders.py\", \"fields\"]]",
   "v1": [
    8418843,
    503150
   ],
   "v2": [
    1770231039,
    112202450
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_filters.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_filters.py\", \"fields\"]]",
   "v1": [
    8418843,
    503150
   ],
   "v2": [
    1770231039,
    112202450
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
     "tests/test_filters.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_forward_references.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_forward_references.py\", \"fields\"]]",
   "v1": [
    8418843,
    503150
   ],
   "v2": [
    1770231039,
    112202450
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
     "tests/test_forward_references.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_funcs.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_funcs.py\", \"fields\"]]",
   "v1": [
    8418843,
    503150
   ],
   "v2": [
    1770231039,
```
</details>

## Step 16

Interesting: `src/attr/filters.py` does not bind `fields` at module level at all.

Tally: 2 import statements confirmed, 4 ruled out, 9 pending. The search itself is complete; what is left is checking the candidates.

Still open: read what `src/attr/converters.py` exports; find where `attr.setters` (imported by `src/attrs/setters.py`) lives; look at `src/attrs/validators.py`'s imports of `fields`; and 6 more.

I'll outline `src/attr/setters.py` directly, which both checks that the file exists and shows me `fields`; if `attr.setters` is a plain module that is where it has to be. Very likely it is defined right there. If the file does not exist or the name is not bound there, I will look at `src/attrs/validators.py`'s top-level names for `fields`.

**Call:** `symbols('src/attr/setters.py', 'fields')`

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
   "desc": "read what `src/attr/converters.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/setters.py",
    "attr.setters"
   ],
   "desc": "find where `attr.setters` (imported by `src/attrs/setters.py`) lives"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "fields"
   ],
   "desc": "look at `src/attrs/validators.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "fields"
   ],
   "desc": "look at `tests/attr_import_star.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "fields"
   ],
   "desc": "look at `tests/test_dunders.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_filters.py",
    "fields"
   ],
   "desc": "look at `tests/test_filters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_forward_references.py",
    "fields"
   ],
   "desc": "look at `tests/test_forward_references.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "fields"
   ],
   "desc": "look at `tests/test_funcs.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "fields"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `fields`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/setters.py', 'fields')",
   "key": "[\"symbols\", [\"src/attr/setters.py\", \"fields\"]]",
   "v1": [
    52720759295393,
    3808975262385
   ],
   "v2": [
    527969388006407,
    38089752623850
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     61864,
     72861
    ],
    "reexport": [
     1628,
     72861
    ],
    "star": [
     148,
     72861
    ],
    "none": [
     2516,
     72861
    ],
    "missing": [
     15,
     163
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
   "call": "symbols('src/attrs/validators.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"fields\"]]",
   "v1": [
    7384783,
    503150
   ],
   "v2": [
    527969388006407,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'fields')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"fields\"]]",
   "v1": [
    7384783,
    503150
   ],
   "v2": [
    527969388006407,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_dunders.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_dunders.py\", \"fields\"]]",
   "v1": [
    7384783,
    503150
   ],
   "v2": [
    527969388006407,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_filters.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_filters.py\", \"fields\"]]",
   "v1": [
    7384783,
    503150
   ],
   "v2": [
    527969388006407,
    38089752623850
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
     "tests/test_filters.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_forward_references.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_forward_references.py\", \"fields\"]]",
   "v1": [
    7384783,
    503150
   ],
   "v2": [
    527969388006407,
    38089752623850
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
     "tests/test_forward_references.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_funcs.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_funcs.py\", \"fields\"]]",
   "v1": [
    7384783,
    503150
   ],
   "v2": [
    527969388006407,
    38089752623850
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
     "tests/test_funcs.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"fields\"]]",
   "v1": [
    7384783,
    503150
   ],
   "v2": [
    527969388006407,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    23750049,
    1610080
   ],
   "v2": [
    1698491223239731,
    121887208396320
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
   "call": "ls('src/attr')",
   "key": "[\"ls\", [\"src/attr\"]]",
   "v1": [
    164707831,
    11220245
   ],
   "v2": [
    6234937927557
```
</details>

## Step 17

Huh: `src/attr/setters.py` does not bind `fields` at module level at all.

Tally: 2 import statements confirmed, 5 ruled out, 8 pending. The search itself is complete; what is left is checking the candidates.

I'll look at `src/attrs/validators.py`'s top-level names for `fields`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `tests/attr_import_star.py`'s top-level names for `fields`.

**Call:** `symbols('src/attrs/validators.py', 'fields')`

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
   "kind": "all",
   "key": [
    "all",
    "src/attr/converters.py"
   ],
   "desc": "read what `src/attr/converters.py` exports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "fields"
   ],
   "desc": "look at `src/attrs/validators.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "fields"
   ],
   "desc": "look at `tests/attr_import_star.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "fields"
   ],
   "desc": "look at `tests/test_dunders.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_filters.py",
    "fields"
   ],
   "desc": "look at `tests/test_filters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_forward_references.py",
    "fields"
   ],
   "desc": "look at `tests/test_forward_references.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "fields"
   ],
   "desc": "look at `tests/test_funcs.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "fields"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `fields`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attrs/validators.py', 'fields')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"fields\"]]",
   "v1": [
    6350723,
    503150
   ],
   "v2": [
    3180393,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'fields')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"fields\"]]",
   "v1": [
    6350723,
    503150
   ],
   "v2": [
    3180393,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_dunders.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_dunders.py\", \"fields\"]]",
   "v1": [
    6350723,
    503150
   ],
   "v2": [
    3180393,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_filters.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_filters.py\", \"fields\"]]",
   "v1": [
    6350723,
    503150
   ],
   "v2": [
    3180393,
    251575
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
     "tests/test_filters.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_forward_references.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_forward_references.py\", \"fields\"]]",
   "v1": [
    6350723,
    503150
   ],
   "v2": [
    3180393,
    251575
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
     "tests/test_forward_references.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_funcs.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_funcs.py\", \"fields\"]]",
   "v1": [
    6350723,
    503150
   ],
   "v2": [
    3180393,
    251575
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
     "tests/test_funcs.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"fields\"]]",
   "v1": [
    6350723,
    503150
   ],
   "v2": [
    3180393,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    20441057,
    1610080
   ],
   "v2": [
    102366293,
    8050400
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
  }
 ],
 "choice": {
  "call": "symbols('src/attrs/validators.py', 'fields')",
  "key": "[\"symbols\", [\"src/attrs/validators.py\", \"fields\"]]",
  "provenance": "`src/attrs/validators.py` had a matching line (step 1); its outline names every `fields` import exactly",
  "v2": [
   3180393,
   251575
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
  "ok": "[\"symbols\", [\"tests/attr_import_star.py\", \"fields\"]]",
  "cap": "[\"symbols\", [\"tests/attr_import_star.py\", \"fields\"]]"
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
  "planned": "[\"symbols\", [\"src/attrs/validators.py\", \"fields\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 17,
   "path": "src/attrs/validators.py",
   "filter": "fields",
   "header": {
    "lines": 4,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/attrs/validators.py",
     "name": "*",
     "line": 3,
     "kind"
```
</details>

## Step 18

`src/attrs/validators.py` matched the search but has no module-level import of `fields`. It also star-imports `attr.validators`, which could carry the name, so that needs checking.

Tally: 2 import statements confirmed, 5 ruled out, 8 pending. The search itself is complete; what is left is checking the candidates.

Next I will look at `tests/attr_import_star.py`'s top-level names for `fields`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will outline `src/attr/validators.py` directly, which both checks that the file exists and shows me `fields`.

**Call:** `symbols('tests/attr_import_star.py', 'fields')`

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
   "desc": "read what `src/attr/converters.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/validators.py",
    "attr.validators"
   ],
   "desc": "find where `attr.validators` (imported by `src/attrs/validators.py`) lives"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "fields"
   ],
   "desc": "look at `tests/attr_import_star.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "fields"
   ],
   "desc": "look at `tests/test_dunders.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_filters.py",
    "fields"
   ],
   "desc": "look at `tests/test_filters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_forward_references.py",
    "fields"
   ],
   "desc": "look at `tests/test_forward_references.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "fields"
   ],
   "desc": "look at `tests/test_funcs.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "fields"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `fields`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/validators.py', 'fields')",
   "key": "[\"symbols\", [\"src/attr/validators.py\", \"fields\"]]",
   "v1": [
    46407694124846,
    3808975262385
   ],
   "v2": [
    464838736300937,
    38089752623850
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     61864,
     72861
    ],
    "reexport": [
     1628,
     72861
    ],
    "star": [
     148,
     72861
    ],
    "none": [
     2516,
     72861
    ],
    "missing": [
     15,
     163
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
   "call": "symbols('tests/attr_import_star.py', 'fields')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"fields\"]]",
   "v1": [
    6550853,
    503150
   ],
   "v2": [
    464838736300937,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_dunders.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_dunders.py\", \"fields\"]]",
   "v1": [
    6550853,
    503150
   ],
   "v2": [
    464838736300937,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_filters.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_filters.py\", \"fields\"]]",
   "v1": [
    6550853,
    503150
   ],
   "v2": [
    464838736300937,
    38089752623850
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
     "tests/test_filters.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_forward_references.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_forward_references.py\", \"fields\"]]",
   "v1": [
    6550853,
    503150
   ],
   "v2": [
    464838736300937,
    38089752623850
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
     "tests/test_forward_references.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_funcs.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_funcs.py\", \"fields\"]]",
   "v1": [
    6550853,
    503150
   ],
   "v2": [
    464838736300937,
    38089752623850
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
     "tests/test_funcs.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"fields\"]]",
   "v1": [
    6550853,
    503150
   ],
   "v2": [
    464838736300937,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    21081473,
    1610080
   ],
   "v2": [
    1496473137782227,
    121887208396320
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
   "call": "ls('src/attr')",
   "key": "[\"ls\", [\"src/attr\"]]",
   "v1": [
    146111192,
    11220245
   ],
   "v2": [
    55310311610418458,
    4247007417559275
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
     "src/attrs/validators.py",
     "attr.validators"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+fields\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+fields\\\\b\", \".\"]]",
   "v1": [
    11823737,
    905670
   ],
   "v2": [
    8932746628620389,
    685615547229300
   ],
   "p_cap": [
    1,
    36
   ],
   "forecast": {
```
</details>

## Step 19

The test module `tests/attr_import_star.py` matched the search but has no module-level import of `fields`. It also star-imports `attr`, which could carry the name, so that needs checking.

Tally: 2 import statements confirmed, 5 ruled out, 8 pending. The search itself is complete; what is left is checking the candidates.

I'll outline `src/attr/validators.py` directly, which both checks that the file exists and shows me `fields`; if `attr.validators` is a plain module that is where it has to be. Very likely it is defined right there. If the file does not exist or the name is not bound there, I will look at `tests/test_dunders.py`'s top-level names for `fields`.

**Call:** `symbols('src/attr/validators.py', 'fields')`

**Response**: outcome `none`

```
module src/attr/validators.py lines=767 dynamic=no all=static@19
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
   "desc": "read what `src/attr/converters.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/attrs/validators.py",
    "attr.validators"
   ],
   "desc": "find where `attr.validators` (imported by `src/attrs/validators.py`) lives"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/__init__.py"
   ],
   "desc": "read what `src/attr/__init__.py` exports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "fields"
   ],
   "desc": "look at `tests/test_dunders.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_filters.py",
    "fields"
   ],
   "desc": "look at `tests/test_filters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_forward_references.py",
    "fields"
   ],
   "desc": "look at `tests/test_forward_references.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "fields"
   ],
   "desc": "look at `tests/test_funcs.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "fields"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `fields`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/validators.py', 'fields')",
   "key": "[\"symbols\", [\"src/attr/validators.py\", \"fields\"]]",
   "v1": [
    43903604216684,
    3808975262385
   ],
   "v2": [
    439797837219317,
    38089752623850
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     61864,
     72861
    ],
    "reexport": [
     1628,
     72861
    ],
    "star": [
     148,
     72861
    ],
    "none": [
     2516,
     72861
    ],
    "missing": [
     15,
     163
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
   "call": "symbols('tests/test_dunders.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_dunders.py\", \"fields\"]]",
   "v1": [
    6220073,
    503150
   ],
   "v2": [
    439797837219317,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_filters.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_filters.py\", \"fields\"]]",
   "v1": [
    6220073,
    503150
   ],
   "v2": [
    439797837219317,
    38089752623850
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
     "tests/test_filters.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_forward_references.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_forward_references.py\", \"fields\"]]",
   "v1": [
    6220073,
    503150
   ],
   "v2": [
    439797837219317,
    38089752623850
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
     "tests/test_forward_references.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_funcs.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_funcs.py\", \"fields\"]]",
   "v1": [
    6220073,
    503150
   ],
   "v2": [
    439797837219317,
    38089752623850
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
     "tests/test_funcs.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"fields\"]]",
   "v1": [
    6220073,
    503150
   ],
   "v2": [
    439797837219317,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "read('src/attr/__init__.py', 45, 30)",
   "key": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]",
   "v1": [
    20022977,
    1610080
   ],
   "v2": [
    1416342260721043,
    121887208396320
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
    20022977,
    1610080
   ],
   "v2": [
    1416342260721043,
    121887208396320
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
   "call": "ls('src/attr')",
   "key": "[\"ls\", [\"src/attr\"]]",
   "v1": [
    138734798,
    11220245
   ],
   "v2": [
    52518251362817828,
    4247007417559275
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
     "src/attrs/validators.py",
     "attr.validators"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+fields\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+fields\\\\b\", \".\"]]",
   "v1": [
    11228333,
    905670
   ],
   "v2": [
    8482010445151229,
    685615547229300
   ],
   "p_cap": [
    1,
    36
   ],
   "forecast": {
    "zero": [
     1,
     36
    ],
    "mid": [
     17,
     18
    ],
    "cap"
```
</details>

## Step 20

Not what I expected: `src/attr/validators.py` does not bind `fields` at module level at all.

Tally: 2 import statements confirmed, 5 ruled out, 8 pending. The search itself is complete; what is left is checking the candidates.

Still open: read what `src/attr/converters.py` exports; read what `src/attr/validators.py` exports; read what `src/attr/__init__.py` exports; and 5 more.

Let me look at `tests/test_dunders.py`'s top-level names for `fields`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `tests/test_filters.py`'s top-level names for `fields`.

**Call:** `symbols('tests/test_dunders.py', 'fields')`

**Response**: outcome `ok`

```
module tests/test_dunders.py lines=1062 dynamic=no all=none
18 from fields <- attr._make fields
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
   "desc": "read what `src/attr/converters.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/validators.py"
   ],
   "desc": "read what `src/attr/validators.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/__init__.py"
   ],
   "desc": "read what `src/attr/__init__.py` exports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_dunders.py",
    "fields"
   ],
   "desc": "look at `tests/test_dunders.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_filters.py",
    "fields"
   ],
   "desc": "look at `tests/test_filters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_forward_references.py",
    "fields"
   ],
   "desc": "look at `tests/test_forward_references.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "fields"
   ],
   "desc": "look at `tests/test_funcs.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "fields"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `fields`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/test_dunders.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_dunders.py\", \"fields\"]]",
   "v1": [
    5689163,
    503150
   ],
   "v2": [
    2849613,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_filters.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_filters.py\", \"fields\"]]",
   "v1": [
    5689163,
    503150
   ],
   "v2": [
    2849613,
    251575
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
     "tests/test_filters.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_forward_references.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_forward_references.py\", \"fields\"]]",
   "v1": [
    5689163,
    503150
   ],
   "v2": [
    2849613,
    251575
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
     "tests/test_forward_references.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_funcs.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_funcs.py\", \"fields\"]]",
   "v1": [
    5689163,
    503150
   ],
   "v2": [
    2849613,
    251575
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
     "tests/test_funcs.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"fields\"]]",
   "v1": [
    5689163,
    503150
   ],
   "v2": [
    2849613,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "read('src/attr/__init__.py', 45, 30)",
   "key": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]",
   "v1": [
    3664813,
    322016
   ],
   "v2": [
    91781333,
    8050400
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
    3664813,
    322016
   ],
   "v2": [
    91781333,
    8050400
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
    3664813,
    322016
   ],
   "v2": [
    91781333,
    8050400
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
  "call": "symbols('tests/test_dunders.py', 'fields')",
  "key": "[\"symbols\", [\"tests/test_dunders.py\", \"fields\"]]",
  "provenance": "`tests/test_dunders.py` had a matching line (step 1); its outline names every `fields` import exactly",
  "v2": [
   2849613,
   251575
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
  "ok": "[\"symbols\", [\"tests/test_filters.py\", \"fields\"]]",
  "cap": "[\"symbols\", [\"tests/test_filters.py\", \"fields\"]]"
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
  "planned": "[\"symbols\", [\"tests/test_dunders.py\", \"fields\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 20,
   "path": "tests/test_dunders.py",
   "filter": "fields",
   "header": {
    "lines": 1062,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_dunders.py",
     "name": "fields",
     "line": 18,
     "kind": "from",
     "src": "attr._make",
     "src_name": "fields",
     "conditional": false,
     "col": 0,
     "bases": []
    }
   ],
   "complete": true
  }
 ],
 "go
```
</details>

## Step 21

The test module `tests/test_dunders.py`: line 18 imports it from `attr._make`.

Tally: 3 import statements confirmed, 5 ruled out, 7 pending. The search itself is complete; what is left is checking the candidates.

Let me look at `tests/test_filters.py`'s top-level names for `fields`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `tests/test_forward_references.py`'s top-level names for `fields`.

**Call:** `symbols('tests/test_filters.py', 'fields')`

**Response**: outcome `ok`

```
module tests/test_filters.py lines=127 dynamic=no all=none
11 from fields <- attr fields
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
   "desc": "read what `src/attr/converters.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/validators.py"
   ],
   "desc": "read what `src/attr/validators.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/__init__.py"
   ],
   "desc": "read what `src/attr/__init__.py` exports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_filters.py",
    "fields"
   ],
   "desc": "look at `tests/test_filters.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_forward_references.py",
    "fields"
   ],
   "desc": "look at `tests/test_forward_references.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "fields"
   ],
   "desc": "look at `tests/test_funcs.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "fields"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `fields`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/test_filters.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_filters.py\", \"fields\"]]",
   "v1": [
    4855233,
    503150
   ],
   "v2": [
    2432648,
    251575
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
     "tests/test_filters.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_forward_references.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_forward_references.py\", \"fields\"]]",
   "v1": [
    4855233,
    503150
   ],
   "v2": [
    2432648,
    251575
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
     "tests/test_forward_references.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_funcs.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_funcs.py\", \"fields\"]]",
   "v1": [
    4855233,
    503150
   ],
   "v2": [
    2432648,
    251575
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
     "tests/test_funcs.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"fields\"]]",
   "v1": [
    4855233,
    503150
   ],
   "v2": [
    2432648,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "read('src/attr/__init__.py', 45, 30)",
   "key": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]",
   "v1": [
    15655489,
    1610080
   ],
   "v2": [
    78438453,
    8050400
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
    15655489,
    1610080
   ],
   "v2": [
    78438453,
    8050400
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
    15655489,
    1610080
   ],
   "v2": [
    78438453,
    8050400
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
  "call": "symbols('tests/test_filters.py', 'fields')",
  "key": "[\"symbols\", [\"tests/test_filters.py\", \"fields\"]]",
  "provenance": "`tests/test_filters.py` had a matching line (step 1); its outline names every `fields` import exactly",
  "v2": [
   2432648,
   251575
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
  "ok": "[\"symbols\", [\"tests/test_forward_references.py\", \"fields\"]]",
  "cap": "[\"symbols\", [\"tests/test_forward_references.py\", \"fields\"]]"
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
  "planned": "[\"symbols\", [\"tests/test_filters.py\", \"fields\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 21,
   "path": "tests/test_filters.py",
   "filter": "fields",
   "header": {
    "lines": 127,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_filters.py",
     "name": "fields",
     "line": 11,
     "kind": "from",
     "src": "attr",
     "src_name": "fields",
     "conditional": false,
     "col": 0,
     "bases": []
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 1,
  "of": 1,
  "candidates": [
   "src/attr/__init__.py",
   "src/attr/_funcs.py",
   "src/attrs/__init__.py",
   "src/attrs/converters.py",
   "src/attrs/exceptions.py",
   "src/attrs/filters.py",
   "src/attrs/setters.py",
   "src/attrs/validators.py",
   "tests/attr_import_star.py",
   "tests/test_dunders.py",
   "tests/test_filters.py",
   "tests/test_forward_references.py",
   "tests/test_funcs.py",
   "tests/test_make.py",
   "tests/test_validators.py"
  ],
  "table": [
   [
    "src/attr/__init__.py",
    "src/attr/__init__.py:
```
</details>

## Step 22

The test module `tests/test_filters.py`: line 11 imports it from `attr`.

Tally: 3 import statements confirmed, 6 ruled out, 6 pending. The search itself is complete; what is left is checking the candidates.

Next I will look at `tests/test_forward_references.py`'s top-level names for `fields`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `tests/test_funcs.py`'s top-level names for `fields`.

**Call:** `symbols('tests/test_forward_references.py', 'fields')`

**Response**: outcome `ok`

```
module tests/test_forward_references.py lines=23 dynamic=no all=none
5 from fields <- attrs fields
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
   "desc": "read what `src/attr/converters.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/validators.py"
   ],
   "desc": "read what `src/attr/validators.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/__init__.py"
   ],
   "desc": "read what `src/attr/__init__.py` exports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_forward_references.py",
    "fields"
   ],
   "desc": "look at `tests/test_forward_references.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "fields"
   ],
   "desc": "look at `tests/test_funcs.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "fields"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `fields`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/test_forward_references.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_forward_references.py\", \"fields\"]]",
   "v1": [
    4021303,
    503150
   ],
   "v2": [
    2015683,
    251575
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
     "tests/test_forward_references.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_funcs.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_funcs.py\", \"fields\"]]",
   "v1": [
    4021303,
    503150
   ],
   "v2": [
    2015683,
    251575
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
     "tests/test_funcs.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"fields\"]]",
   "v1": [
    4021303,
    503150
   ],
   "v2": [
    2015683,
    251575
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
     "fields"
    ]
   ]
  },
  {
   "call": "read('src/attr/__init__.py', 45, 30)",
   "key": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]",
   "v1": [
    12986913,
    1610080
   ],
   "v2": [
    65095573,
    8050400
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
    12986913,
    1610080
   ],
   "v2": [
    65095573,
    8050400
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
    12986913,
    1610080
   ],
   "v2": [
    65095573,
    8050400
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
  "call": "symbols('tests/test_forward_references.py', 'fields')",
  "key": "[\"symbols\", [\"tests/test_forward_references.py\", \"fields\"]]",
  "provenance": "`tests/test_forward_references.py` had a matching line (step 1); its outline names every `fields` import exactly",
  "v2": [
   2015683,
   251575
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
  "ok": "[\"symbols\", [\"tests/test_funcs.py\", \"fields\"]]",
  "cap": "[\"symbols\", [\"tests/test_funcs.py\", \"fields\"]]"
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
  "planned": "[\"symbols\", [\"tests/test_forward_references.py\", \"fields\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 22,
   "path": "tests/test_forward_references.py",
   "filter": "fields",
   "header": {
    "lines": 23,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_forward_references.py",
     "name": "fields",
     "line": 5,
     "kind": "from",
     "src": "attrs",
     "src_name": "fields",
     "conditional": false,
     "col": 0,
     "bases": []
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 1,
  "of": 1,
  "candidates": [
   "src/attr/__init__.py",
   "src/attr/_funcs.py",
   "src/attrs/__init__.py",
   "src/attrs/converters.py",
   "src/attrs/exceptions.py",
   "src/attrs/filters.py",
   "src/attrs/setters.py",
   "src/attrs/validators.py",
   "tests/attr_import_star.py",
   "tests/test_dunders.py",
   "tests/test_filters.py",
   "tests/test_forward_references.py",
   "tests/test_funcs.py",
   "tests/test_make.py",
   "tests/test_validators.py"
  ],
  "table": [
   [
    "src/attr/__init__.py",
    "src/attr/__init__.py:16",
    "in",
    "`._make` resolves `fields` to the target"
   ],
   [
    "src/attr/_funcs.py",
    "src/attr/_funcs.py:5",
    "in",
    "`._make` resolves `fields` to the target"
   ],
   [
    "src/attrs/__init__.py",
    "src/attrs/__init__.py:3",
    "out",
    "`attr` resolves `fields` to ambiguous(dynamic module)"
   ],
   [
    "src/attrs/converters.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/attrs/exceptions.py",
    "src/attrs/exceptions.py:3",
    "out",
    "star import of `attr.exceptions`, which does not export `fields
```
</details>

## Step 23

The test module `tests/test_forward_references.py`: line 5 imports it from `attrs`.

Tally: 3 import statements confirmed, 6 ruled out, 6 pending. The search itself is complete; what is left is checking the candidates.

I'll look at `tests/test_funcs.py`'s top-level names for `fields`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will outline `src/attrs.py` directly, which both checks that the file exists and shows me `define`.

**Call:** `symbols('tests/test_funcs.py', 'fields')`

**Response**: outcome `ok`

```
module tests/test_funcs.py lines=851 dynamic=no all=none
19 from fields <- attr fields
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
   "desc": "read what `src/attr/converters.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/validators.py"
   ],
   "desc": "read what `src/attr/validators.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/__init__.py"
   ],
   "desc": "read what `src/attr/__init__.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_forward_references.py",
    "attrs"
   ],
   "desc": "find where `attrs` (imported by `tests/test_forward_references.py`) lives"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "fields"
   ],
   "desc": "look at `tests/test_funcs.py`'s imports of `fields`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "fields"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `fields`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attrs.py', 'define')",
   "key": "[\"symbols\", [\"src/attrs.py\", \"define\"]]",
   "v1": [
    28773383967428,
    3808975262385
   ],
   "v2": [
    288495634726757,
    38089752623850
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     61864,
     72861
    ],
    "reexport": [
     1628,
     72861
    ],
    "star": [
     148,
     72861
    ],
    "none": [
     2516,
     72861
    ],
    "missing": [
     15,
     163
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_forward_references.py",
     "attrs"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_funcs.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_funcs.py\", \"fields\"]]",
   "v1": [
    4221433,
    503150
   ],
   "v2": [
    288495634726757,
    38089752623850
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
     "tests/test_funcs.py",
     "fields"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"fields\"]]",
   "v1": [
    4221433,
    503150
   ],
   "v2": [
    288495634726757,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "read('src/attr/__init__.py', 45, 30)",
   "key": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]",
   "v1": [
    13627329,
    1610080
   ],
   "v2": [
    932175212744851,
    121887208396320
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
    13627329,
    1610080
   ],
   "v2": [
    932175212744851,
    121887208396320
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
    13627329,
    1610080
   ],
   "v2": [
    932175212744851,
    121887208396320
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
   "call": "ls('src')",
   "key": "[\"ls\", [\"src\"]]",
   "v1": [
    22150699,
    2616380
   ],
   "v2": [
    16649066124748879,
    1980667136440200
   ],
   "p_cap": [
    5,
    52
   ],
   "forecast": {
    "complete": [
     47,
     52
    ],
    "cap": [
     5,
     52
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_forward_references.py",
     "attrs"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+define\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+define\\\\b\", \".\"]]",
   "v1": [
    471452,
    50315
   ],
   "v2": [
    32582359229813,
    3808975262385
   ],
   "p_cap": [
    1,
    36
   ],
   "forecast": {
    "zero": [
     1,
     36
    ],
    "mid": [
     17,
     18
    ],
    "cap": [
     1,
     36
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_forward_references.py",
     "attrs"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+define\\\\b', 'src')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+define\\\\b\", \"src\"]]",
   "v1": [
    471452,
    50315
   ],
   "v2": [
    32582359229813,
    3808975262385
   ],
   "p_cap": [
    1,
    184
   ],
   "forecast": {
    "zero": [
     155,
     184
    ],
    "mid": [
     7,
     46
    ],
    "cap": [
     1,
     184
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_forward_references.py",
     "attrs"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_funcs.py', 'fields')",
  "key": "[\"symbols\", [\"tests/test_funcs.py\", \"fields\"]]",
  "provenance": "`tests/test_funcs.py` had a matching line (step 1); its outline names every `fields` import exactly",
  "v2": [
   288495634726757,
   38089752623850
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
  "ok": "[\"symbols\", [\"src/attrs.py\", \"define\"]]",
  "cap": "[\"symbols\", [\"src/attrs.py\", \"define\"]]"
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
  "planned": "[\"symbols\", [\"tests/test_funcs.py\", \"fields\"]]",
  "sta
```
</details>

## Step 24

The test module `tests/test_funcs.py`: line 19 imports it from `attr`.

Tally: 3 import statements confirmed, 7 ruled out, 5 pending. The search itself is complete; what is left is checking the candidates.

Still open: read what `src/attr/converters.py` exports; read what `src/attr/validators.py` exports; read what `src/attr/__init__.py` exports; and 2 more.

Let me outline `src/attrs.py` directly, which both checks that the file exists and shows me `define`; if `attrs` is a plain module that is where it has to be. Very likely it is defined right there. If the file does not exist or the name is not bound there, I will look at `tests/test_make.py`'s top-level names for `fields`.

**Call:** `symbols('src/attrs.py', 'define')`

**Response**: outcome `missing`

```
error: not a python file: src/attrs.py
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
   "desc": "read what `src/attr/converters.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/validators.py"
   ],
   "desc": "read what `src/attr/validators.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/__init__.py"
   ],
   "desc": "read what `src/attr/__init__.py` exports"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_forward_references.py",
    "attrs"
   ],
   "desc": "find where `attrs` (imported by `tests/test_forward_references.py`) lives"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "fields"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `fields`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attrs.py', 'define')",
   "key": "[\"symbols\", [\"src/attrs.py\", \"define\"]]",
   "v1": [
    22460318796881,
    3808975262385
   ],
   "v2": [
    225364983021287,
    38089752623850
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     61864,
     72861
    ],
    "reexport": [
     1628,
     72861
    ],
    "star": [
     148,
     72861
    ],
    "none": [
     2516,
     72861
    ],
    "missing": [
     15,
     163
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_forward_references.py",
     "attrs"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_make.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"fields\"]]",
   "v1": [
    3387503,
    503150
   ],
   "v2": [
    225364983021287,
    38089752623850
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
     "fields"
    ]
   ]
  },
  {
   "call": "read('src/attr/__init__.py', 45, 30)",
   "key": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]",
   "v1": [
    10958753,
    1610080
   ],
   "v2": [
    730157127287347,
    121887208396320
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
    10958753,
    1610080
   ],
   "v2": [
    730157127287347,
    121887208396320
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
    10958753,
    1610080
   ],
   "v2": [
    730157127287347,
    121887208396320
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
   "call": "ls('src')",
   "key": "[\"ls\", [\"src\"]]",
   "v1": [
    17814263,
    2616380
   ],
   "v2": [
    13366272236064439,
    1980667136440200
   ],
   "p_cap": [
    5,
    52
   ],
   "forecast": {
    "complete": [
     47,
     52
    ],
    "cap": [
     5,
     52
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_forward_references.py",
     "attrs"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+define\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+define\\\\b\", \".\"]]",
   "v1": [
    388059,
    50315
   ],
   "v2": [
    26269294059266,
    3808975262385
   ],
   "p_cap": [
    1,
    36
   ],
   "forecast": {
    "zero": [
     1,
     36
    ],
    "mid": [
     17,
     18
    ],
    "cap": [
     1,
     36
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_forward_references.py",
     "attrs"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+define\\\\b', 'src')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+define\\\\b\", \"src\"]]",
   "v1": [
    388059,
    50315
   ],
   "v2": [
    26269294059266,
    3808975262385
   ],
   "p_cap": [
    1,
    184
   ],
   "forecast": {
    "zero": [
     155,
     184
    ],
    "mid": [
     7,
     46
    ],
    "cap": [
     1,
     184
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_forward_references.py",
     "attrs"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/attrs.py', 'define')",
  "key": "[\"symbols\", [\"src/attrs.py\", \"define\"]]",
  "provenance": "`attrs` would be `src/attrs.py` if that file exists; one call both checks and closes it",
  "v2": [
   225364983021287,
   38089752623850
  ]
 },
 "forecast": {
  "def": [
   61864,
   72861
  ],
  "reexport": [
   1628,
   72861
  ],
  "star": [
   148,
   72861
  ],
  "none": [
   2516,
   72861
  ],
  "missing": [
   15,
   163
  ]
 },
 "plan": {
  "def": "[\"symbols\", [\"tests/test_make.py\", \"fields\"]]",
  "reexport": "[\"symbols\", [\"tests/test_make.py\", \"fields\"]]",
  "star": "[\"symbols\", [\"tests/test_make.py\", \"fields\"]]",
  "none": "[\"symbols\", [\"tests/test_make.py\", \"fields\"]]",
  "missing": "[\"symbols\", [\"tests/test_make.py\", \"fields\"]]"
 },
 "hedges": [
  {
   "outcome": "def",
   "word": "very likely",
   "p": [
    61864,
    72861
   ]
  }
 ],
 "adherence": {
  "planned": "[\"symbols\", [\"src/attrs.py\", \"define\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "error",
   "step": 24,
   "call": "[\"symbols\", [\"src/attrs.py\", \"define\"]]",
   "error": "not a python file: src/attrs.py",
   "missing": "src/attrs.py"
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 1,
  "of": 1,
  "candidates": [
   "src/at
```
</details>

## Step 25

Huh: there is no `src/attrs.py`, so `attrs` is either a package (`src/attrs/__init__.py`) or not in this repository at all.

I'll look at `tests/test_make.py`'s top-level names for `fields`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will read `__all__` in `src/attr/__init__.py`.

**Call:** `symbols('tests/test_make.py', 'fields')`

**Response**: outcome `ok`

```
module tests/test_make.py lines=3213 dynamic=no all=none
29 from fields <- attr._make fields
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
   "desc": "read what `src/attr/converters.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/validators.py"
   ],
   "desc": "read what `src/attr/validators.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/__init__.py"
   ],
   "desc": "read what `src/attr/__init__.py` exports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_make.py",
    "fields"
   ],
   "desc": "look at `tests/test_make.py`'s imports of `fields`"
  }
 ],
 "candidates": [
  {
   "call": "read('src/attr/__init__.py', 45, 30)",
   "key": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]",
   "v1": [
    7649761,
    1610080
   ],
   "v2": [
    38409813,
    8050400
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
    7649761,
    1610080
   ],
   "v2": [
    38409813,
    8050400
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
    7649761,
    1610080
   ],
   "v2": [
    38409813,
    8050400
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
   "call": "symbols('tests/test_make.py', 'fields')",
   "key": "[\"symbols\", [\"tests/test_make.py\", \"fields\"]]",
   "v1": [
    2353443,
    503150
   ],
   "v2": [
    38409813,
    8050400
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
     "fields"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_make.py', 'fields')",
  "key": "[\"symbols\", [\"tests/test_make.py\", \"fields\"]]",
  "provenance": "`tests/test_make.py` had a matching line (step 1); its outline names every `fields` import exactly",
  "v2": [
   38409813,
   8050400
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
  "planned": "[\"symbols\", [\"tests/test_make.py\", \"fields\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 25,
   "path": "tests/test_make.py",
   "filter": "fields",
   "header": {
    "lines": 3213,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_make.py",
     "name": "fields",
     "line": 29,
     "kind": "from",
     "src": "attr._make",
     "src_name": "fields",
     "conditional": false,
     "col": 0,
     "bases": []
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 1,
  "of": 1,
  "candidates": [
   "src/attr/__init__.py",
   "src/attr/_funcs.py",
   "src/attrs/__init__.py",
   "src/attrs/converters.py",
   "src/attrs/exceptions.py",
   "src/attrs/filters.py",
   "src/attrs/setters.py",
   "src/attrs/validators.py",
   "tests/attr_import_star.py",
   "tests/test_dunders.py",
   "tests/test_filters.py",
   "tests/test_forward_references.py",
   "tests/test_funcs.py",
   "tests/test_make.py",
   "tests/test_validators.py"
  ],
  "table": [
   [
    "src/attr/__init__.py",
    "src/attr/__init__.py:16",
    "in",
    "`._make` resolves `fields` to the target"
   ],
   [
    "src/attr/_funcs.py",
    "src/attr/_funcs.py:5",
    "in",
    "`._make` resolves `fields` to the target"
   ],
   [
    "src/attrs/__init__.py",
    "src/attrs/__init__.py:3",
    "out",
    "`attr` resolves `fields` to ambiguous(dynamic module)"
   ],
   [
    "src/attrs/converters.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/attrs/exceptions.py",
    "src/attrs/exceptions.py:3",
    "out",
    "star import of `attr.exceptions`, which does not export `fields`"
   ],
   [
    "src/attrs/filters.py",
    "src/attrs/filters.py:3",
    "out",
    "star import of `attr.filters`, which does not export `fields`"
   ],
   [
    "src/attrs/setters.py",
    "src/attrs/setters.py:3",
    "out",
    "star import of `attr.setters`, which does not export `fields`"
   ],
   [
    "src/attrs/validators.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/attr_import_star.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_dunders.py",
    "tests/test_dunders.py:18",
    "in",
    "`attr._make` resolves `fields` to the target"
   ],
   [
    "tests/test_filters.py",
    "tests/test_filters.py:11",
    "out",
    "`attr` resolves `fields` to ambiguous(dynamic module)"
   ],
   [
    "tests/test_forward_references.py",
    "tests/test_forward_references.py:5",
    "out",
    "`attrs` resolves `fields` to ambiguous(dynamic module)"
   ],
   [
    "tests/test_funcs.py",
    "tests/test_funcs.py:19",
    "out",
    "`attr` resolves `fields` to ambiguous(dynamic module)"
   ],
   [
    "tests/test_make.py",
    "tests/test_make.py:29",
    "in",
    "`attr._make` resolves `fields` to the target"
   ],
   [
    "tests/test_validators.py",
    "tests/test_validators.py:14",
    "out",
    "`attr` resolves `fields` to ambiguous(dynamic module)"
   ]
  ],
  "
```
</details>

## Step 26

The test module `tests/test_make.py`: line 29 imports it from `attr._make`.

Tally: 4 import statements confirmed, 8 ruled out, 3 pending. The search itself is complete; what is left is checking the candidates.

I'll read `__all__` in `src/attr/__init__.py`; whether `fields` is in it decides if the star import carries the name. Almost certainly the list fits in one read. If the list runs past the window, I will read `__all__` in `src/attr/converters.py`.

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
   "desc": "read what `src/attr/converters.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/validators.py"
   ],
   "desc": "read what `src/attr/validators.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/__init__.py"
   ],
   "desc": "read what `src/attr/__init__.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "read('src/attr/__init__.py', 45, 30)",
   "key": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]",
   "v1": [
    99,
    32
   ],
   "v2": [
    51,
    16
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
    99,
    32
   ],
   "v2": [
    51,
    16
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
    99,
    32
   ],
   "v2": [
    51,
    16
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
  "call": "read('src/attr/__init__.py', 45, 30)",
  "key": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]",
  "provenance": "`__all__` of `src/attr/__init__.py` starts at line 45 (outline header)",
  "v2": [
   51,
   16
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
 "hedges": [
  {
   "outcome": "fits",
   "word": "almost certainly",
   "p": [
    29,
    32
   ]
  }
 ],
 "adherence": {
  "planned": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "read",
   "step": 26,
   "path": "src/attr/__init__.py",
   "start": 45,
   "count": 30,
   "n": 30
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 1,
  "of": 1,
  "candidates": [
   "src/attr/__init__.py",
   "src/attr/_funcs.py",
   "src/attrs/__init__.py",
   "src/attrs/converters.py",
   "src/attrs/exceptions.py",
   "src/attrs/filters.py",
   "src/attrs/setters.py",
   "src/attrs/validators.py",
   "tests/attr_import_star.py",
   "tests/test_dunders.py",
   "tests/test_filters.py",
   "tests/test_forward_references.py",
   "tests/test_funcs.py",
   "tests/test_make.py",
   "tests/test_validators.py"
  ],
  "table": [
   [
    "src/attr/__init__.py",
    "src/attr/__init__.py:16",
    "in",
    "`._make` resolves `fields` to the target"
   ],
   [
    "src/attr/_funcs.py",
    "src/attr/_funcs.py:5",
    "in",
    "`._make` resolves `fields` to the target"
   ],
   [
    "src/attrs/__init__.py",
    "src/attrs/__init__.py:3",
    "out",
    "`attr` resolves `fields` to ambiguous(dynamic module)"
   ],
   [
    "src/attrs/converters.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/attrs/exceptions.py",
    "src/attrs/exceptions.py:3",
    "out",
    "star import of `attr.exceptions`, which does not export `fields`"
   ],
   [
    "src/attrs/filters.py",
    "src/attrs/filters.py:3",
    "out",
    "star import of `attr.filters`, which does not export `fields`"
   ],
   [
    "src/attrs/setters.py",
    "src/attrs/setters.py:3",
    "out",
    "star import of `attr.setters`, which does not export `fields`"
   ],
   [
    "src/attrs/validators.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/attr_import_star.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_dunders.py",
    "tests/test_dunders.py:18",
    "in",
    "`attr._make` resolves `fields` to the target"
   ],
   [
    "tests/test_filters.py",
    "tests/test_filters.py:11",
    "out",
    "`attr` resolves `fields` to ambiguous(dynamic module)"
   ],
   [
    "tests/test_forward_references.py",
    "tests/test_forward_references.py:5",
    "out",
    "`attrs` resolves `fields` to ambiguous(dynamic module)"
   ],
   [
    "tests/test_funcs.py",
    "tests/test_funcs.py:19",
    "out",
    "`attr` resolves `fields` to ambiguous(dynamic module)"
   ],
   [
    "tests/test_make.py",
    "tests/test_make.py:29",
    "in",
    "`attr._make` resolves `fields` to the target"
   ],
   [
    "tests/test_validators.py",
    "tests/test_validators.py:14",
    "out",
    "`attr` resolves `fields` to ambiguous(dynamic module)"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  },
  "n_in": 4,
  "n_out": 8,
  "n_pending": 3
 }
}
```
</details>

## Step 27

That did not tell me anything new.

Tally: 4 import statements confirmed, 8 ruled out, 3 pending. The search itself is complete; what is left is checking the candidates.

I'll read `__all__` in `src/attr/converters.py`; whether `fields` is in it decides if the star import carries the name. Almost certainly the list fits in one read. If the list runs past the window, I will read `__all__` in `src/attr/__init__.py`.

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
   "desc": "read what `src/attr/converters.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/validators.py"
   ],
   "desc": "read what `src/attr/validators.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/__init__.py"
   ],
   "desc": "read what `src/attr/__init__.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "read('src/attr/__init__.py', 45, 60)",
   "key": "[\"read\", [\"src/attr/__init__.py\", 45, 60]]",
   "v1": [
    99,
    32
   ],
   "v2": [
    51,
    16
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
    99,
    32
   ],
   "v2": [
    51,
    16
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
    99,
    32
   ],
   "v2": [
    51,
    16
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
  "call": "read('src/attr/converters.py', 11, 30)",
  "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
  "provenance": "`__all__` of `src/attr/converters.py` starts at line 11 (outline header)",
  "v2": [
   51,
   16
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
 "hedges": [
  {
   "outcome": "fits",
   "word": "almost certainly",
   "p": [
    29,
    32
   ]
  }
 ],
 "adherence": {
  "planned": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "read",
   "step": 27,
   "path": "src/attr/converters.py",
   "start": 11,
   "count": 30,
   "n": 30
  },
  {
   "kind": "all_names",
   "step": 27,
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
  "phase": "importers",
  "step": 1,
  "of": 1,
  "candidates": [
   "src/attr/__init__.py",
   "src/attr/_funcs.py",
   "src/attrs/__init__.py",
   "src/attrs/converters.py",
   "src/attrs/exceptions.py",
   "src/attrs/filters.py",
   "src/attrs/setters.py",
   "src/attrs/validators.py",
   "tests/attr_import_star.py",
   "tests/test_dunders.py",
   "tests/test_filters.py",
   "tests/test_forward_references.py",
   "tests/test_funcs.py",
   "tests/test_make.py",
   "tests/test_validators.py"
  ],
  "table": [
   [
    "src/attr/__init__.py",
    "src/attr/__init__.py:16",
    "in",
    "`._make` resolves `fields` to the target"
   ],
   [
    "src/attr/_funcs.py",
    "src/attr/_funcs.py:5",
    "in",
    "`._make` resolves `fields` to the target"
   ],
   [
    "src/attrs/__init__.py",
    "src/attrs/__init__.py:3",
    "out",
    "`attr` resolves `fields` to ambiguous(dynamic module)"
   ],
   [
    "src/attrs/converters.py",
    "src/attrs/converters.py:3",
    "out",
    "star import of `attr.converters`, which does not export `fields`"
   ],
   [
    "src/attrs/exceptions.py",
    "src/attrs/exceptions.py:3",
    "out",
    "star import of `attr.exceptions`, which does not export `fields`"
   ],
   [
    "src/attrs/filters.py",
    "src/attrs/filters.py:3",
    "out",
    "star import of `attr.filters`, which does not export `fields`"
   ],
   [
    "src/attrs/setters.py",
    "src/attrs/setters.py:3",
    "out",
    "star import of `attr.setters`, which does not export `fields`"
   ],
   [
    "src/attrs/validators.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/attr_import_star.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_dunders.py",
    "tests/test_dunders.py:18",
    "in",
    "`attr._make` resolves `fields` to the target"
   ],
   [
    "tests/test_filters.py",
    "tests/test_filters.py:11",
    "out",
    "`attr` resolves `fields` to ambiguous(dynamic module)"
   ],
   [
    "tests/test_forward_references.py",
    "tests/test_forward_references.py:5",
    "out",
    "`attrs` resolves `fields` to ambiguous(dynamic module)"
   ],
   [
    "tests/test_funcs.py",
    "tests/test_funcs.py:19",
    "out",
    "`attr` resolves `fields` to ambiguous(dynamic module)"
   ],
   [
    "tests/test_make.py",
    "tests/test_make.py:29",
    "in",
    "`attr._make` resolves `fields` to the target"
   ],
   [
    "tests/test_validators.py",
    "tests/test_validators.py:14",
    "out",
    "`attr` resolves `fields` to ambiguous(dynamic module)"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  },
  "n_in": 4,
  "n_out": 9,
  "n_pending": 2
 }
}
```
</details>

## Step 28

`__all__` in `src/attr/converters.py` lists 4 names and `fields` is not among them, so that star import does not carry it.

Next I will read `__all__` in `src/attr/__init__.py`; whether `fields` is in it decides if the star import carries the name. Almost certainly the list fits in one read. If the list runs past the window, I will read `__all__` in `src/attr/validators.py`.

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
   "desc": "read what `src/attr/validators.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/__init__.py"
   ],
   "desc": "read what `src/attr/__init__.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "read('src/attr/__init__.py', 45, 60)",
   "key": "[\"read\", [\"src/attr/__init__.py\", 45, 60]]",
   "v1": [
    67,
    32
   ],
   "v2": [
    35,
    16
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
    67,
    32
   ],
   "v2": [
    35,
    16
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
  "call": "read('src/attr/__init__.py', 45, 60)",
  "key": "[\"read\", [\"src/attr/__init__.py\", 45, 60]]",
  "provenance": "`__all__` of `src/attr/__init__.py` starts at line 45 (outline header)",
  "v2": [
   35,
   16
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
 "hedges": [
  {
   "outcome": "fits",
   "word": "almost certainly",
   "p": [
    29,
    32
   ]
  }
 ],
 "adherence": {
  "planned": "[\"read\", [\"src/attr/__init__.py\", 45, 60]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "read",
   "step": 28,
   "path": "src/attr/__init__.py",
   "start": 45,
   "count": 60,
   "n": 60
  },
  {
   "kind": "all_names",
   "step": 28,
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
  "phase": "importers",
  "step": 1,
  "of": 1,
  "candidates": [
   "src/attr/__init__.py",
   "src/attr/_funcs.py",
   "src/attrs/__init__.py",
   "src/attrs/converters.py",
   "src/attrs/exceptions.py",
   "src/attrs/filters.py",
   "src/attrs/setters.py",
   "src/attrs/validators.py",
   "tests/attr_import_star.py",
   "tests/test_dunders.py",
   "tests/test_filters.py",
   "tests/test_forward_references.py",
   "tests/test_funcs.py",
   "tests/test_make.py",
   "tests/test_validators.py"
  ],
  "table": [
   [
    "src/attr/__init__.py",
    "src/attr/__init__.py:16",
    "in",
    "`._make` resolves `fields` to the target"
   ],
   [
    "src/attr/_funcs.py",
    "src/attr/_funcs.py:5",
    "in",
    "`._make` resolves `fields` to the target"
   ],
   [
    "src/attrs/__init__.py",
    "src/attrs/__init__.py:3",
    "out",
    "`attr` resolves `fields` to ambiguous(dynamic module)"
   ],
   [
    "src/attrs/converters.py",
    "src/attrs/converters.py:3",
    "out",
    "star import of `attr.converters`, which does not export `fields`"
   ],
   [
    "src/attrs/exceptions.py",
    "src/attrs/exceptions.py:3",
    "out",
    "star import of `attr.exceptions`, which does not export `fields`"
   ],
   [
    "src/attrs/filters.py",
    "src/attrs/filters.py:3",
    "out",
    "star import of `attr.filters`, which does not export `fields`"
   ],
   [
    "src/attrs/setters.py",
    "src/attrs/setters.py:3",
    "out",
    "star import of `attr.setters`, which does not export `fields`"
   ],
   [
    "src/attrs/validators.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/attr_import_star.py",
    "tests/attr_import_star.py:4",
    "out",
    "star import of `attr` binds `fields` to ambiguous(dynamic module)"
   ],
   [
    "tests/test_dunders.py",
    "tests/test_dunders.py:18",
    "in",
    "`attr._make` resolves `fields` to the target"
   ],
   [
    "tests/test_filters.py",
    "tests/test_filters.py:11",
    "out",
    "`attr` resolves `fields` to ambiguous(dynamic module)"
   ],
   [
    "tests/test_forward_references.py",
    "tests/test_forward_references.py:5",
    "out",
    "`attrs` resolves `fields` to ambiguous(dynamic module)"
   ],
   [
    "tests/test_funcs.py",
    "tests/test_funcs.py:19",
    "out",
    "`attr` resolves `fields` to ambiguous(dynamic module)"
   ],
   [
    "tests/test_make.py",
    "tests/test_make.py:29",
    "in",
    "`attr._make` resolves `fields` to the target"
   ],
   [
    "tests/test_validators.py",
    "tests/test_validators.py:14",
    "out",
    "`attr` resolves `fields` to ambiguous(dynamic module)"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  },
  "n_in": 4,
  "n_out": 10,
  "n_pending": 1
 }
}
```
</details>

## Step 29

`__all__` in `src/attr/__init__.py` lists 34 names and `fields` is one of them, so its star import does carry the name.

Let me read `__all__` in `src/attr/validators.py`; whether `fields` is in it decides if the star import carries the name. Almost certainly the list fits in one read. If the list runs past the window, I follow whatever it opens up.

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
   "desc": "read what `src/attr/validators.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "read('src/attr/validators.py', 19, 30)",
   "key": "[\"read\", [\"src/attr/validators.py\", 19, 30]]",
   "v1": [
    35,
    32
   ],
   "v2": [
    35,
    32
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
  "call": "read('src/attr/validators.py', 19, 30)",
  "key": "[\"read\", [\"src/attr/validators.py\", 19, 30]]",
  "provenance": "`__all__` of `src/attr/validators.py` starts at line 19 (outline header)",
  "v2": [
   35,
   32
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
  "fits": "done",
  "long": "continue"
 },
 "hedges": [
  {
   "outcome": "fits",
   "word": "almost certainly",
   "p": [
    29,
    32
   ]
  }
 ],
 "adherence": {
  "planned": "[\"read\", [\"src/attr/validators.py\", 19, 30]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "read",
   "step": 29,
   "path": "src/attr/validators.py",
   "start": 19,
   "count": 30,
   "n": 30
  },
  {
   "kind": "all_names",
   "step": 29,
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
  "phase": "importers",
  "step": 1,
  "of": 1,
  "candidates": [
   "src/attr/__init__.py",
   "src/attr/_funcs.py",
   "src/attrs/__init__.py",
   "src/attrs/converters.py",
   "src/attrs/exceptions.py",
   "src/attrs/filters.py",
   "src/attrs/setters.py",
   "src/attrs/validators.py",
   "tests/attr_import_star.py",
   "tests/test_dunders.py",
   "tests/test_filters.py",
   "tests/test_forward_references.py",
   "tests/test_funcs.py",
   "tests/test_make.py",
   "tests/test_validators.py"
  ],
  "table": [
   [
    "src/attr/__init__.py",
    "src/attr/__init__.py:16",
    "in",
    "`._make` resolves `fields` to the target"
   ],
   [
    "src/attr/_funcs.py",
    "src/attr/_funcs.py:5",
    "in",
    "`._make` resolves `fields` to the target"
   ],
   [
    "src/attrs/__init__.py",
    "src/attrs/__init__.py:3",
    "out",
    "`attr` resolves `fields` to ambiguous(dynamic module)"
   ],
   [
    "src/attrs/converters.py",
    "src/attrs/converters.py:3",
    "out",
    "star import of `attr.converters`, which does not export `fields`"
   ],
   [
    "src/attrs/exceptions.py",
    "src/attrs/exceptions.py:3",
    "out",
    "star import of `attr.exceptions`, which does not export `fields`"
   ],
   [
    "src/attrs/filters.py",
    "src/attrs/filters.py:3",
    "out",
    "star import of `attr.filters`, which does not export `fields`"
   ],
   [
    "src/attrs/setters.py",
    "src/attrs/setters.py:3",
    "out",
    "star import of `attr.setters`, which does not export `fields`"
   ],
   [
    "src/attrs/validators.py",
    "src/attrs/validators.py:3",
    "out",
    "star import of `attr.validators`, which does not export `fields`"
   ],
   [
    "tests/attr_import_star.py",
    "tests/attr_import_star.py:4",
    "out",
    "star import of `attr` binds `fields` to ambiguous(dynamic module)"
   ],
   [
    "tests/test_dunders.py",
    "tests/test_dunders.py:18",
    "in",
    "`attr._make` resolves `fields` to the target"
   ],
   [
    "tests/test_filters.py",
    "tests/test_filters.py:11",
    "out",
    "`attr` resolves `fields` to ambiguous(dynamic module)"
   ],
   [
    "tests/test_forward_references.py",
    "tests/test_forward_references.py:5",
    "out",
    "`attrs` resolves `fields` to ambiguous(dynamic module)"
   ],
   [
    "tests/test_funcs.py",
    "tests/test_funcs.py:19",
    "out",
    "`attr` resolves `fields` to ambiguous(dynamic module)"
   ],
   [
    "tests/test_make.py",
    "tests/test_make.py:29",
    "in",
    "`attr._make` resolves `fields` to the target"
   ],
   [
    "tests/test_validators.py",
    "tests/test_validators.py:14",
    "out",
    "`attr` resolves `fields` to ambiguous(dynamic module)"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  },
  "n_in": 4,
  "n_out": 11,
  "n_pending": 0
 }
}
```
</details>

## Final

4 module-level import statements bring in this definition: `src/attr/__init__.py:16`, `src/attr/_funcs.py:5`, `tests/test_dunders.py:18`, `tests/test_make.py:29`. Ruled out along the way: `src/attrs/__init__.py:3` (`attr` resolves `fields` to ambiguous(dynamic module)); `src/attrs/converters.py:3` (star import of `attr.converters`, which does not export `fields`). Looking back, 1 of 29 calls did not end up mattering (step 26).

**Answer:** `{"final_kind": "importers", "final": ["src/attr/__init__.py:16", "src/attr/_funcs.py:5", "tests/test_dunders.py:18", "tests/test_make.py:29"], "steps": [{"op": "importers", "output": ["src/attr/__init__.py:16", "src/attr/_funcs.py:5", "tests/test_dunders.py:18", "tests/test_make.py:29"]}], "stuck": null}`  
**Stopped:** certificate after 29 calls