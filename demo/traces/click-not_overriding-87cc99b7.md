# click-not_overriding-87cc99b7

**Repository:** click  
**Chain:** resolve → subclasses → not_overriding  
**Seed:** 0, prior 81b2b7394c71c459, floor 8

## Task

In `tests/test_testing.py` line 11, `ClickException` is imported from `click.exceptions`. Which definition does the module-level name `ClickException` actually refer to? Give `path:line`. Then list every class that derives from it directly, as `path:line:ClassName`, making sure each base name really resolves to this definition. Among those subclasses, which do not define `format_message` themselves? Same format.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N; bindings take effect in source order. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. A class derives from a definition when a base written as a bare name or `module.Name` resolves to it. A call site is `name(...)` where the bare name refers to the module-level binding (not a parameter or local). Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

I need to find what `ClickException` really is in `tests/test_testing.py`: line 11 imports it from `click.exceptions`, so the definition is at least one hop away. Then, among its subclasses, the ones that do not define `format_message` themselves.

Next I will check `tests/test_testing.py` for any other binding of `ClickException` besides the import on line 11; almost certainly the import is the only one, and then `click.exceptions` is the place to follow.

**Call:** `symbols('tests/test_testing.py', 'ClickException')`

**Response**: outcome `reexport`

```
module tests/test_testing.py lines=841 dynamic=no all=none
11 from ClickException <- click.exceptions ClickException
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "tests/test_testing.py",
    "ClickException"
   ],
   "desc": "check the top-level names of `tests/test_testing.py` for `ClickException`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/test_testing.py', 'ClickException')",
   "key": "[\"symbols\", [\"tests/test_testing.py\", \"ClickException\"]]",
   "v1": [
    65626933,
    22453600
   ],
   "v2": [
    65626933,
    22453600
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
     "tests/test_testing.py",
     "ClickException"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_testing.py')",
   "key": "[\"symbols\", [\"tests/test_testing.py\"]]",
   "v1": [
    13924023879,
    4558080800
   ],
   "v2": [
    13924023879,
    4558080800
   ],
   "p_cap": [
    134,
    1015
   ],
   "forecast": {
    "def": [
     881,
     101500
    ],
    "reexport": [
     81933,
     101500
    ],
    "star": [
     881,
     101500
    ],
    "none": [
     881,
     20300
    ],
    "cap": [
     134,
     1015
    ]
   },
   "serves": [
    [
     "bindings",
     "tests/test_testing.py",
     "ClickException"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_testing.py', 'ClickException')",
  "key": "[\"symbols\", [\"tests/test_testing.py\", \"ClickException\"]]",
  "provenance": "module `tests/test_testing.py` (task), name `ClickException` (task)",
  "v2": [
   65626933,
   22453600
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
   "path": "tests/test_testing.py",
   "filter": "ClickException",
   "header": {
    "lines": 841,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_testing.py",
     "name": "ClickException",
     "line": 11,
     "kind": "from",
     "src": "click.exceptions",
     "src_name": "ClickException",
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
  "of": 3,
  "chain": [
   [
    "tests/test_testing.py",
    "ClickException",
    "reexport",
    [
     "click.exceptions",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 2

The test module `tests/test_testing.py` does not define `ClickException` itself; line 11 imports it from `click.exceptions`.

So far: `tests/test_testing.py` takes `ClickException` from `click.exceptions`, which I still have to locate.

Let me list `./` to see what lives there; the listing settles whether the import is a module, a package, or not here at all. Very likely the listing fits. If the listing is too long, I will outline `click/exceptions.py` directly, which both checks that the file exists and shows me `ClickException`. I could outline `click/exceptions.py` directly, which both checks that the file exists and shows me `ClickException` instead, but it costs more calls in expectation.

**Call:** `ls('.')`

**Response**: outcome `complete`

```
.devcontainer/
.github/
.pre-commit-config.yaml
.readthedocs.yaml
CHANGES.md
LICENSE.txt
README.md
docs/
examples/
pyproject.toml
src/
tests/
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_testing.py",
    "click.exceptions"
   ],
   "desc": "find where `click.exceptions` (imported by `tests/test_testing.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    2491,
    1326
   ],
   "v2": [
    59881702565,
    31056023232
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
     "tests/test_testing.py",
     "click.exceptions"
    ]
   ]
  },
  {
   "call": "symbols('click/exceptions.py', 'ClickException')",
   "key": "[\"symbols\", [\"click/exceptions.py\", \"ClickException\"]]",
   "v1": [
    15655364805,
    6901338496
   ],
   "v2": [
    44855693759,
    20704015488
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     95637,
     261256
    ],
    "reexport": [
     4041,
     522512
    ],
    "star": [
     449,
     522512
    ],
    "none": [
     449,
     32657
    ],
    "missing": [
     707,
     1156
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_testing.py",
     "click.exceptions"
    ]
   ]
  },
  {
   "call": "symbols('click/exceptions/__init__.py', 'ClickException')",
   "key": "[\"symbols\", [\"click/exceptions/__init__.py\", \"ClickException\"]]",
   "v1": [
    86086477,
    28613312
   ],
   "v2": [
    244806719,
    85839936
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     23,
     2312
    ],
    "reexport": [
     115,
     3468
    ],
    "star": [
     23,
     27744
    ],
    "none": [
     437,
     27744
    ],
    "missing": [
     1087,
     1156
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_testing.py",
     "click.exceptions"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+ClickException\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+ClickException\\\\b\", \".\"]]",
   "v1": [
    673,
    221
   ],
   "v2": [
    3817,
    1326
   ],
   "p_cap": [
    1,
    39
   ],
   "forecast": {
    "zero": [
     1,
     39
    ],
    "mid": [
     37,
     39
    ],
    "cap": [
     1,
     39
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_testing.py",
     "click.exceptions"
    ]
   ]
  }
 ],
 "choice": {
  "call": "ls('.')",
  "key": "[\"ls\", [\".\"]]",
  "provenance": "`click.exceptions` imported by `tests/test_testing.py` should live under `.`",
  "v2": [
   59881702565,
   31056023232
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
  "cap": "[\"symbols\", [\"click/exceptions.py\", \"ClickException\"]]"
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
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "listing",
   "step": 2,
   "dir": ".",
   "entries": [
    ".devcontainer/",
    ".github/",
    ".pre-commit-config.yaml",
    ".readthedocs.yaml",
    "CHANGES.md",
    "LICENSE.txt",
    "README.md",
    "docs/",
    "examples/",
    "pyproject.toml",
    "src/",
    "tests/"
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "resolve",
  "step": 1,
  "of": 3,
  "chain": [
   [
    "tests/test_testing.py",
    "ClickException",
    "reexport",
    [
     "click.exceptions",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 3

`./` has 12 entries: there is no `click` here.

So far: `tests/test_testing.py` takes `ClickException` from `click.exceptions`, which I still have to locate.

I'll search the whole tree for `class ClickException`/`def ClickException`; that shows where the definition lives and whether the name is reused. Almost certainly it fits under the cap. If it caps or nothing turns up, I will list `src/` to see what lives there. I could list `src/` to see what lives there instead, but it costs more calls in expectation.

**Call:** `grep('^\\s*(?:async\\s+)?(?:def|class)\\s+ClickException\\b', '.')`

**Response**: outcome `mid`

```
src/click/exceptions.py:35:class ClickException(Exception):
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_testing.py",
    "click.exceptions"
   ],
   "desc": "find where `click.exceptions` (imported by `tests/test_testing.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+ClickException\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+ClickException\\\\b\", \".\"]]",
   "v1": [
    1390,
    663
   ],
   "v2": [
    5680,
    2703
   ],
   "p_cap": [
    1,
    39
   ],
   "forecast": {
    "zero": [
     1,
     39
    ],
    "mid": [
     37,
     39
    ],
    "cap": [
     1,
     39
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_testing.py",
     "click.exceptions"
    ]
   ]
  },
  {
   "call": "ls('src')",
   "key": "[\"ls\", [\"src\"]]",
   "v1": [
    25061,
    11713
   ],
   "v2": [
    75353,
    35139
   ],
   "p_cap": [
    5,
    53
   ],
   "forecast": {
    "complete": [
     48,
     53
    ],
    "cap": [
     5,
     53
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_testing.py",
     "click.exceptions"
    ]
   ]
  },
  {
   "call": "symbols('src/click/exceptions.py', 'ClickException')",
   "key": "[\"symbols\", [\"src/click/exceptions.py\", \"ClickException\"]]",
   "v1": [
    15655364805,
    6901338496
   ],
   "v2": [
    47615448463,
    20704015488
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     95637,
     261256
    ],
    "reexport": [
     4041,
     522512
    ],
    "star": [
     449,
     522512
    ],
    "none": [
     449,
     32657
    ],
    "missing": [
     707,
     1156
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_testing.py",
     "click.exceptions"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+ClickException\\\\b', 'src')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+ClickException\\\\b\", \"src\"]]",
   "v1": [
    72061,
    24752
   ],
   "v2": [
    219481,
    74256
   ],
   "p_cap": [
    1,
    224
   ],
   "forecast": {
    "zero": [
     193,
     224
    ],
    "mid": [
     15,
     112
    ],
    "cap": [
     1,
     224
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_testing.py",
     "click.exceptions"
    ]
   ]
  },
  {
   "call": "symbols('src/click/exceptions/__init__.py', 'ClickException')",
   "key": "[\"symbols\", [\"src/click/exceptions/__init__.py\", \"ClickException\"]]",
   "v1": [
    86086477,
    28613312
   ],
   "v2": [
    262398727,
    85839936
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     23,
     2312
    ],
    "reexport": [
     115,
     3468
    ],
    "star": [
     23,
     27744
    ],
    "none": [
     437,
     27744
    ],
    "missing": [
     1087,
     1156
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_testing.py",
     "click.exceptions"
    ]
   ]
  }
 ],
 "choice": {
  "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+ClickException\\\\b', '.')",
  "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+ClickException\\\\b\", \".\"]]",
  "provenance": "a `def`/`class ClickException` statement would reveal the module file; `ClickException` task",
  "v2": [
   5680,
   2703
  ]
 },
 "forecast": {
  "zero": [
   1,
   39
  ],
  "mid": [
   37,
   39
  ],
  "cap": [
   1,
   39
  ]
 },
 "plan": {
  "zero": "[\"ls\", [\"src\"]]",
  "mid": "continue",
  "cap": "[\"ls\", [\"src\"]]"
 },
 "hedges": [
  {
   "outcome": "mid",
   "word": "almost certainly",
   "p": [
    37,
    39
   ]
  }
 ],
 "adherence": {
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "grep",
   "step": 3,
   "pattern": "^\\s*(?:async\\s+)?(?:def|class)\\s+ClickException\\b",
   "scope": ".",
   "hits": [
    [
     "src/click/exceptions.py",
     35
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "phase": "resolve",
  "step": 1,
  "of": 3,
  "chain": [
   [
    "tests/test_testing.py",
    "ClickException",
    "reexport",
    [
     "click.exceptions",
     "src/click/exceptions.py"
    ]
   ],
   [
    "src/click/exceptions.py",
    "ClickException",
    "open",
    null
   ]
  ]
 }
}
```
</details>

## Step 4

There is exactly one `ClickException` definition in the tree, in `src/click/exceptions.py`.

So far: `tests/test_testing.py` takes `ClickException` from `click.exceptions`; `src/click/exceptions.py` is next.

I'll look at `src/click/exceptions.py`'s top-level names for `ClickException`; that settles what the name means there. Almost certainly it is defined right there. If the name is not bound there, that finishes it; if it is re-exported from somewhere else, I follow whatever it opens up. I could outline all of `src/click/exceptions.py` instead, but it is more likely to hit the cap.

**Call:** `symbols('src/click/exceptions.py', 'ClickException')`

**Response**: outcome `def`

```
module src/click/exceptions.py lines=379 dynamic=no all=none
35 class ClickException (Exception)
68 class UsageError (ClickException)
342 class FileError (ClickException)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/click/exceptions.py",
    "ClickException"
   ],
   "desc": "check the top-level names of `src/click/exceptions.py` for `ClickException`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/click/exceptions.py', 'ClickException')",
   "key": "[\"symbols\", [\"src/click/exceptions.py\", \"ClickException\"]]",
   "v1": [
    23836821,
    22453600
   ],
   "v2": [
    23836821,
    22453600
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
     "src/click/exceptions.py",
     "ClickException"
    ]
   ]
  },
  {
   "call": "symbols('src/click/exceptions.py')",
   "key": "[\"symbols\", [\"src/click/exceptions.py\"]]",
   "v1": [
    5440631143,
    4558080800
   ],
   "v2": [
    5440631143,
    4558080800
   ],
   "p_cap": [
    134,
    1015
   ],
   "forecast": {
    "def": [
     41407,
     50750
    ],
    "reexport": [
     881,
     50750
    ],
    "star": [
     881,
     101500
    ],
    "none": [
     2643,
     101500
    ],
    "cap": [
     134,
     1015
    ]
   },
   "serves": [
    [
     "bindings",
     "src/click/exceptions.py",
     "ClickException"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/click/exceptions.py', 'ClickException')",
  "key": "[\"symbols\", [\"src/click/exceptions.py\", \"ClickException\"]]",
  "provenance": "module `src/click/exceptions.py` (step 3), name `ClickException` (task)",
  "v2": [
   23836821,
   22453600
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
    47,
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
   "step": 4,
   "path": "src/click/exceptions.py",
   "filter": "ClickException",
   "header": {
    "lines": 379,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/click/exceptions.py",
     "name": "ClickException",
     "line": 35,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "Exception"
     ]
    },
    {
     "module": "src/click/exceptions.py",
     "name": "UsageError",
     "line": 68,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "ClickException"
     ]
    },
    {
     "module": "src/click/exceptions.py",
     "name": "FileError",
     "line": 342,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "ClickException"
     ]
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "resolve",
  "step": 1,
  "of": 3,
  "chain": [
   [
    "tests/test_testing.py",
    "ClickException",
    "reexport",
    [
     "click.exceptions",
     "src/click/exceptions.py"
    ]
   ],
   [
    "src/click/exceptions.py",
    "ClickException",
    "class",
    35
   ]
  ]
 }
}
```
</details>

## Step 5

There it is: `ClickException` is a class at `src/click/exceptions.py:35`. That settles the definition; now its subclasses.

Let me search the whole tree for classes deriving from `ClickException`; the search has to be complete before I can call the set final. Very likely nothing turns up. If it fits under the cap or it caps, I follow whatever it opens up.

**Call:** `grep('^\\s*class\\s+\\w+\\s*\\(.*\\bClickException\\b', '.')`

**Response**: outcome `mid`

```
src/click/exceptions.py:68:class UsageError(ClickException):
src/click/exceptions.py:342:class FileError(ClickException):
tests/test_testing.py:230:    class CLIError(ClickException):
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
   "desc": "search `.` for classes deriving from `ClickException`"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*class\\\\s+\\\\w+\\\\s*\\\\(.*\\\\bClickException\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*class\\\\s+\\\\w+\\\\s*\\\\(.*\\\\bClickException\\\\b\", \".\"]]",
   "v1": [
    614758073,
    419499990
   ],
   "v2": [
    614758073,
    419499990
   ],
   "p_cap": [
    1,
    18
   ],
   "forecast": {
    "zero": [
     31,
     36
    ],
    "mid": [
     1,
     12
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
  "call": "grep('^\\\\s*class\\\\s+\\\\w+\\\\s*\\\\(.*\\\\bClickException\\\\b', '.')",
  "key": "[\"grep\", [\"^\\\\s*class\\\\s+\\\\w+\\\\s*\\\\(.*\\\\bClickException\\\\b\", \".\"]]",
  "provenance": "subclass lines naming `ClickException` under `.` (derived)",
  "v2": [
   614758073,
   419499990
  ]
 },
 "forecast": {
  "zero": [
   31,
   36
  ],
  "mid": [
   1,
   12
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
    31,
    36
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
   "step": 5,
   "pattern": "^\\s*class\\s+\\w+\\s*\\(.*\\bClickException\\b",
   "scope": ".",
   "hits": [
    [
     "src/click/exceptions.py",
     68
    ],
    [
     "src/click/exceptions.py",
     342
    ],
    [
     "tests/test_testing.py",
     230
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "phase": "subclasses",
  "step": 2,
  "of": 3,
  "candidates": [
   "src/click/exceptions.py",
   "tests/test_testing.py"
  ],
  "table": [
   [
    "src/click/exceptions.py",
    "src/click/exceptions.py:68:UsageError",
    "in",
    "base `ClickException` resolves to the target"
   ],
   [
    "src/click/exceptions.py",
    "src/click/exceptions.py:342:FileError",
    "in",
    "base `ClickException` resolves to the target"
   ],
   [
    "tests/test_testing.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
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

## Step 6

Not what I expected: 3 matching lines anywhere for classes deriving from `ClickException`, in `src/click/exceptions.py`, `tests/test_testing.py`, and the search was under the cap, so that is the complete set there. That is the full set of subclasses; now which of them lack the method.

Tally: 0 classes without their own method confirmed, 0 ruled out, 2 pending.

Let me check `FileError`'s own members in `src/click/exceptions.py`; only its own members tell me whether it overrides. Almost certainly the members fit. If there are too many members, I will check `UsageError`'s own members in `src/click/exceptions.py`.

**Call:** `members('src/click/exceptions.py', 'FileError')`

**Response**: outcome `ok`

```
class FileError in src/click/exceptions.py definitions=1
345 assign ui_filename
346 assign filename
348 def __init__
356 def format_message
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "members",
   "key": [
    "members",
    "src/click/exceptions.py",
    "UsageError"
   ],
   "desc": "look at what `UsageError` in `src/click/exceptions.py` defines itself"
  },
  {
   "kind": "members",
   "key": [
    "members",
    "src/click/exceptions.py",
    "FileError"
   ],
   "desc": "look at what `FileError` in `src/click/exceptions.py` defines itself"
  }
 ],
 "candidates": [
  {
   "call": "members('src/click/exceptions.py', 'FileError')",
   "key": "[\"members\", [\"src/click/exceptions.py\", \"FileError\"]]",
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
     "src/click/exceptions.py",
     "FileError"
    ]
   ]
  },
  {
   "call": "members('src/click/exceptions.py', 'UsageError')",
   "key": "[\"members\", [\"src/click/exceptions.py\", \"UsageError\"]]",
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
     "src/click/exceptions.py",
     "UsageError"
    ]
   ]
  }
 ],
 "choice": {
  "call": "members('src/click/exceptions.py', 'FileError')",
  "key": "[\"members\", [\"src/click/exceptions.py\", \"FileError\"]]",
  "provenance": "the members `FileError` defines itself (step 3)",
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
  "ok": "[\"members\", [\"src/click/exceptions.py\", \"UsageError\"]]",
  "cap": "[\"members\", [\"src/click/exceptions.py\", \"UsageError\"]]"
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
   "step": 6,
   "path": "src/click/exceptions.py",
   "cls": "FileError",
   "entries": [
    [
     345,
     "assign",
     "ui_filename"
    ],
    [
     346,
     "assign",
     "filename"
    ],
    [
     348,
     "def",
     "__init__"
    ],
    [
     356,
     "def",
     "format_message"
    ]
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "not_overriding",
  "step": 3,
  "of": 3,
  "table": [
   [
    "src/click/exceptions.py",
    "UsageError",
    "pending",
    "members not yet seen"
   ],
   [
    "src/click/exceptions.py",
    "FileError",
    "out",
    "defines `format_message` itself"
   ]
  ],
  "n_in": 0,
  "n_out": 1,
  "n_pending": 1
 }
}
```
</details>

## Step 7

`FileError` defines `format_message` itself (line 356), so it overrides.

Tally: 0 classes without their own method confirmed, 1 ruled out, 1 pending.

Next I will check `UsageError`'s own members in `src/click/exceptions.py`; only its own members tell me whether it overrides. Almost certainly the members fit. If there are too many members, I follow whatever it opens up.

**Call:** `members('src/click/exceptions.py', 'UsageError')`

**Response**: outcome `ok`

```
class UsageError in src/click/exceptions.py definitions=1
77 assign exit_code
79 assign ctx
80 assign cmd
82 def __init__
87 def show
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "members",
   "key": [
    "members",
    "src/click/exceptions.py",
    "UsageError"
   ],
   "desc": "look at what `UsageError` in `src/click/exceptions.py` defines itself"
  }
 ],
 "candidates": [
  {
   "call": "members('src/click/exceptions.py', 'UsageError')",
   "key": "[\"members\", [\"src/click/exceptions.py\", \"UsageError\"]]",
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
     "src/click/exceptions.py",
     "UsageError"
    ]
   ]
  }
 ],
 "choice": {
  "call": "members('src/click/exceptions.py', 'UsageError')",
  "key": "[\"members\", [\"src/click/exceptions.py\", \"UsageError\"]]",
  "provenance": "the members `UsageError` defines itself (step 3)",
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
  "planned": "[\"members\", [\"src/click/exceptions.py\", \"UsageError\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "members",
   "step": 7,
   "path": "src/click/exceptions.py",
   "cls": "UsageError",
   "entries": [
    [
     77,
     "assign",
     "exit_code"
    ],
    [
     79,
     "assign",
     "ctx"
    ],
    [
     80,
     "assign",
     "cmd"
    ],
    [
     82,
     "def",
     "__init__"
    ],
    [
     87,
     "def",
     "show"
    ]
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "not_overriding",
  "step": 3,
  "of": 3,
  "table": [
   [
    "src/click/exceptions.py",
    "UsageError",
    "in",
    "does not define `format_message`"
   ],
   [
    "src/click/exceptions.py",
    "FileError",
    "out",
    "defines `format_message` itself"
   ]
  ],
  "n_in": 1,
  "n_out": 1,
  "n_pending": 0
 }
}
```
</details>

## Final

`ClickException` is the class at `src/click/exceptions.py:35`. 2 classes derive from it directly: `UsageError` (`src/click/exceptions.py:68`), `FileError` (`src/click/exceptions.py:342`). 1 of the subclasses do not define `format_message` themselves: `UsageError`. Looking back, all 7 calls were needed.

**Answer:** `{"final_kind": "not_overriding", "final": ["src/click/exceptions.py:68:UsageError"], "steps": [{"op": "resolve", "output": {"kind": "def", "path": "src/click/exceptions.py", "line": 35, "name": "ClickException", "detail": "class"}}, {"op": "subclasses", "output": ["src/click/exceptions.py:68:UsageError", "src/click/exceptions.py:342:FileError"]}, {"op": "not_overriding", "output": ["src/click/exceptions.py:68:UsageError"]}], "stuck": null}`  
**Stopped:** certificate after 7 calls