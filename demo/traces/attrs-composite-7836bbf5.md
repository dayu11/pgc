# attrs-composite-7836bbf5

**Repository:** attrs  
**Family:** composite  
**Seed:** 0, prior df2023878106d754

## Task

In `tests/test_dunders.py`, line 27 imports `instance_of` from `attr.validators`. Under the declared semantics, which definition does the module-level name `instance_of` bound by this statement resolve to? Answer with `path:line`. Then list every module-level import statement in the snapshot that imports that definition (from-imports naming it, directly or with `as`, and star imports of modules that export it), as `path:line` entries.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

Nothing seen yet beyond the task text.

Chain: `tests/test_dunders.py` is not yet closed for `instance_of`.

Outstanding: close the namespace of `tests/test_dunders.py` for `instance_of`.

Next: outline `tests/test_dunders.py`, because module `tests/test_dunders.py` (task). I expect: a definition there ends the chain (about 80%); a capped outline means filtering by name (about 15%); a re-export continues the chain to its source (under 5%); no binding at all points at a submodule or an unresolved name (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `tests/test_dunders.py` filtered to `instance_of`, is expected to open more follow-up work. Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done; cap: outline `tests/test_dunders.py` filtered to `instance_of`.

**Call:** `symbols('tests/test_dunders.py')`

**Response** (capped): outcome `cap`

```
module tests/test_dunders.py lines=1062 dynamic=no all=none
7 import copy <- copy
8 import inspect <- inspect
9 import pickle <- pickle
11 import pytest <- pytest
13 from given <- hypothesis given
14 from booleans <- hypothesis.strategies booleans
16 import attr <- attr
18 from Factory <- attr._make Factory
18 from NOTHING <- attr._make NOTHING
18 from _add_repr <- attr._make _add_repr
18 from _compile_and_eval <- attr._make _compile_and_eval
18 from _make_init_script <- attr._make _make_init_script
18 from fields <- attr._make fields
18 from make_class <- attr._make make_class
27 from instance_of <- attr.validators instance_of
29 from simple_attr <- .utils simple_attr
29 from simple_class <- .utils simple_class
32 assign EqC
33 assign EqCSlots
34 assign OrderC
35 assign OrderCSlots
36 assign ReprC
37 assign ReprCSlots
41 class EqCallableC
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
    "tests/test_dunders.py",
    "instance_of"
   ],
   "desc": "close the namespace of `tests/test_dunders.py` for `instance_of`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/test_dunders.py')",
   "key": "[\"symbols\", [\"tests/test_dunders.py\"]]",
   "v1": [
    11618714673,
    9714246868
   ],
   "v2": [
    14077374709,
    9714246868
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
     "tests/test_dunders.py",
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_dunders.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/test_dunders.py\", \"instance_of\"]]",
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
     "tests/test_dunders.py",
     "instance_of"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_dunders.py')",
  "key": "[\"symbols\", [\"tests/test_dunders.py\"]]",
  "provenance": "module `tests/test_dunders.py` (task)",
  "v2": [
   14077374709,
   9714246868
  ]
 },
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
 "plan": {
  "def": "done",
  "reexport": "continue",
  "star": "continue",
  "none": "done",
  "cap": "[\"symbols\", [\"tests/test_dunders.py\", \"instance_of\"]]"
 },
 "adherence": null,
 "facts": [
  {
   "kind": "outline",
   "step": 1,
   "path": "tests/test_dunders.py",
   "filter": null,
   "header": {
    "lines": 1062,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_dunders.py",
     "name": "copy",
     "line": 7,
     "kind": "import",
     "src": "copy",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_dunders.py",
     "name": "inspect",
     "line": 8,
     "kind": "import",
     "src": "inspect",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_dunders.py",
     "name": "pickle",
     "line": 9,
     "kind": "import",
     "src": "pickle",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_dunders.py",
     "name": "pytest",
     "line": 11,
     "kind": "import",
     "src": "pytest",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_dunders.py",
     "name": "given",
     "line": 13,
     "kind": "from",
     "src": "hypothesis",
     "src_name": "given",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_dunders.py",
     "name": "booleans",
     "line": 14,
     "kind": "from",
     "src": "hypothesis.strategies",
     "src_name": "booleans",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_dunders.py",
     "name": "attr",
     "line": 16,
     "kind": "import",
     "src": "attr",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_dunders.py",
     "name": "Factory",
     "line": 18,
     "kind": "from",
     "src": "attr._make",
     "src_name": "Factory",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_dunders.py",
     "name": "NOTHING",
     "line": 18,
     "kind": "from",
     "src": "attr._make",
     "src_name": "NOTHING",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_dunders.py",
     "name": "_add_repr",
     "line": 18,
     "kind": "from",
     "src": "attr._make",
     "src_name": "_add_repr",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_dunders.py",
     "name": "_compile_and_eval",
     "line": 18,
     "kind": "from",
     "src": "attr._make",
     "src_name": "_compile_and_eval",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_dunders.py",
     "name": "_make_init_script",
     "line": 18,
     "kind": "from",
     "src": "attr._make",
     "src_name": "_make_init_script",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_dunders.py",
     "name": "fields",
     "line": 18,
     "kind": "from",
     "src": "attr._make",
     "src_name": "fields",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_dunders.py",
     "name": "make_class",
     "line": 18,
     "kind": "from",
     "src": "attr._make",
     "src_name": "make_class",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_dunders.py",
     "name": "instance_of",
     "line": 27,
     "kind": "from",
     "src": "attr.validators",
     "src_name": "instance_of",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_dunders.py",
     "name": "simple_attr",
     "line": 29,
     "kind": "from",
     "src": ".utils",
     "src_name": "simple_attr",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_dunders.py",
     "name": "simple_class",
     "line": 29,
     "kind": "from",
     "src": ".utils",
     "src_name": "simple_class",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_dunders.py",
     "name": "EqC",
     "line": 32,
     "kind": "assign",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "t
```
</details>

## Step 2

The outline of `tests/test_dunders.py` has 40 bindings (capped, so this is only the start of the file); no `__all__`; no dynamic namespace tricks.

Chain: `tests/test_dunders.py` is not yet closed for `instance_of`.

Still to settle: close the namespace of `tests/test_dunders.py` for `instance_of`.

Next: outline `tests/test_dunders.py` filtered to `instance_of`, because module `tests/test_dunders.py` (task), name `instance_of` (task). I expect: a re-export continues the chain to its source (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a definition there ends the chain (under 5%); no binding but a star import means checking what that source exports (under 5%). Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done.

**Call:** `symbols('tests/test_dunders.py', 'instance_of')`

**Response**: outcome `reexport`

```
module tests/test_dunders.py lines=1062 dynamic=no all=none
27 from instance_of <- attr.validators instance_of
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "tests/test_dunders.py",
    "instance_of"
   ],
   "desc": "close the namespace of `tests/test_dunders.py` for `instance_of`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/test_dunders.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/test_dunders.py\", \"instance_of\"]]",
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
     "tests/test_dunders.py",
     "instance_of"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_dunders.py', 'instance_of')",
  "key": "[\"symbols\", [\"tests/test_dunders.py\", \"instance_of\"]]",
  "provenance": "module `tests/test_dunders.py` (task), name `instance_of` (task)",
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
  "planned": "[\"symbols\", [\"tests/test_dunders.py\", \"instance_of\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 2,
   "path": "tests/test_dunders.py",
   "filter": "instance_of",
   "header": {
    "lines": 1062,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_dunders.py",
     "name": "instance_of",
     "line": 27,
     "kind": "from",
     "src": "attr.validators",
     "src_name": "instance_of",
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
    "tests/test_dunders.py",
    "instance_of",
    "reexport",
    [
     "attr.validators",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 3

In `tests/test_dunders.py`, `instance_of` has exactly one binding: line 27 imports it as `instance_of` from `attr.validators`. No dynamic namespace tricks, no `__all__`.

Chain: `tests/test_dunders.py` takes `instance_of` from `attr.validators` (module not yet located).

Outstanding: locate the module `attr.validators` imported by `tests/test_dunders.py`.

Next: grep `def`/`class instance_of` statements under `.`, because a `def`/`class instance_of` statement would reveal the module file; `instance_of` task. I expect: hits under the cap (about 90%); a capped result (about 5%); no hits (about 5%). The alternative, list `.`, is more likely to hit the cap (about 20% against about 5%). Plan by outcome: zero: list `.`; mid: outline each module that appears; cap: list `.`.

**Call:** `grep('^\\s*(?:async\\s+)?(?:def|class)\\s+instance_of\\b', '.')`

**Response**: outcome `mid`

```
src/attr/validators.py:114:def instance_of(type):
src/attr/validators.pyi:38:def instance_of(type: type[_T]) -> _ValidatorType[_T]: ...
src/attr/validators.pyi:40:def instance_of(type: tuple[type[_T]]) -> _ValidatorType[_T]: ...
src/attr/validators.pyi:42:def instance_of(
src/attr/validators.pyi:46:def instance_of(
src/attr/validators.pyi:50:def instance_of(type: tuple[type, ...]) -> _ValidatorType[Any]: ...
src/attr/validators.pyi:52:def instance_of(type: UnionType) -> _ValidatorType[Any]: ...
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_dunders.py",
    "attr.validators"
   ],
   "desc": "locate the module `attr.validators` imported by `tests/test_dunders.py`"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+instance_of\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+instance_of\\\\b\", \".\"]]",
   "v1": [
    5893,
    2748
   ],
   "v2": [
    53495,
    24732
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
     12
    ],
    "cap": [
     1,
     24
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_dunders.py",
     "attr.validators"
    ]
   ]
  },
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    4706,
    2061
   ],
   "v2": [
    28465,
    12366
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
     "tests/test_dunders.py",
     "attr.validators"
    ]
   ]
  },
  {
   "call": "symbols('attr/validators.py', 'instance_of')",
   "key": "[\"symbols\", [\"attr/validators.py\", \"instance_of\"]]",
   "v1": [
    157529507203,
    68666886600
   ],
   "v2": [
    18583517483,
    7923102300
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     13132,
     36075
    ],
    "reexport": [
     469,
     44400
    ],
    "star": [
     469,
     577200
    ],
    "none": [
     469,
     57720
    ],
    "missing": [
     44479,
     72150
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_dunders.py",
     "attr.validators"
    ]
   ]
  },
  {
   "call": "symbols('attr/validators/__init__.py', 'instance_of')",
   "key": "[\"symbols\", [\"attr/validators/__init__.py\", \"instance_of\"]]",
   "v1": [
    25216162903,
    8327264400
   ],
   "v2": [
    25881161041,
    8327264400
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     1003,
     129870
    ],
    "reexport": [
     11033,
     649350
    ],
    "star": [
     1003,
     1298700
    ],
    "none": [
     7021,
     432900
    ],
    "missing": [
     23047,
     24050
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_dunders.py",
     "attr.validators"
    ]
   ]
  }
 ],
 "choice": {
  "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+instance_of\\\\b', '.')",
  "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+instance_of\\\\b\", \".\"]]",
  "provenance": "a `def`/`class instance_of` statement would reveal the module file; `instance_of` task",
  "v2": [
   53495,
   24732
  ]
 },
 "forecast": {
  "zero": [
   1,
   24
  ],
  "mid": [
   11,
   12
  ],
  "cap": [
   1,
   24
  ]
 },
 "plan": {
  "zero": "[\"ls\", [\".\"]]",
  "mid": "continue",
  "cap": "[\"ls\", [\".\"]]"
 },
 "adherence": {
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "grep",
   "step": 3,
   "pattern": "^\\s*(?:async\\s+)?(?:def|class)\\s+instance_of\\b",
   "scope": ".",
   "hits": [
    [
     "src/attr/validators.py",
     114
    ],
    [
     "src/attr/validators.pyi",
     38
    ],
    [
     "src/attr/validators.pyi",
     40
    ],
    [
     "src/attr/validators.pyi",
     42
    ],
    [
     "src/attr/validators.pyi",
     46
    ],
    [
     "src/attr/validators.pyi",
     50
    ],
    [
     "src/attr/validators.pyi",
     52
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "chain": [
   [
    "tests/test_dunders.py",
    "instance_of",
    "reexport",
    [
     "attr.validators",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 4

The grep under `.` returned 7 lines, under the cap, so these are all of them: `src/attr/validators.py`, `src/attr/validators.pyi`.

Chain: `tests/test_dunders.py` takes `instance_of` from `attr.validators` (module not yet located).

Outstanding: locate the module `attr.validators` imported by `tests/test_dunders.py`.

Next: list `.`, because `attr.validators` imported by `tests/test_dunders.py` should live under `.`. I expect: a complete listing settles which files exist (about 80%); a capped listing settles nothing (about 20%). The alternative, outline `attr/validators.py` filtered to `instance_of`, costs more in expectation. Plan by outcome: complete: outline the module it reveals; cap: outline `attr/validators.py` filtered to `instance_of`.

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
    "tests/test_dunders.py",
    "attr.validators"
   ],
   "desc": "locate the module `attr.validators` imported by `tests/test_dunders.py`"
  }
 ],
 "candidates": [
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    4706,
    2061
   ],
   "v2": [
    721557514603,
    309000989700
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
     "tests/test_dunders.py",
     "attr.validators"
    ]
   ]
  },
  {
   "call": "symbols('attr/validators.py', 'instance_of')",
   "key": "[\"symbols\", [\"attr/validators.py\", \"instance_of\"]]",
   "v1": [
    157529507203,
    68666886600
   ],
   "v2": [
    1502429028419,
    618001979400
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     13132,
     36075
    ],
    "reexport": [
     469,
     44400
    ],
    "star": [
     469,
     577200
    ],
    "none": [
     469,
     57720
    ],
    "missing": [
     44479,
     72150
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_dunders.py",
     "attr.validators"
    ]
   ]
  },
  {
   "call": "symbols('attr/validators/__init__.py', 'instance_of')",
   "key": "[\"symbols\", [\"attr/validators/__init__.py\", \"instance_of\"]]",
   "v1": [
    25216162903,
    8327264400
   ],
   "v2": [
    26989491271,
    8327264400
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     1003,
     129870
    ],
    "reexport": [
     11033,
     649350
    ],
    "star": [
     1003,
     1298700
    ],
    "none": [
     7021,
     432900
    ],
    "missing": [
     23047,
     24050
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_dunders.py",
     "attr.validators"
    ]
   ]
  }
 ],
 "choice": {
  "call": "ls('.')",
  "key": "[\"ls\", [\".\"]]",
  "provenance": "`attr.validators` imported by `tests/test_dunders.py` should live under `.`",
  "v2": [
   721557514603,
   309000989700
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
  "cap": "[\"symbols\", [\"attr/validators.py\", \"instance_of\"]]"
 },
 "adherence": {
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "listing",
   "step": 4,
   "dir": ".",
   "entries": [
    ".git_archival.txt",
    ".github/",
    ".pre-commit-config.yaml",
    ".readthedocs.yaml",
    "CHANGELOG.md",
    "README.md",
    "bench/",
    "changelog.d/",
    "codspeed.yml",
    "docs/",
    "pyproject.toml",
    "src/",
    "tests/",
    "tox.ini",
    "typing_tests/"
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "chain": [
   [
    "tests/test_dunders.py",
    "instance_of",
    "reexport",
    [
     "attr.validators",
     "src/attr/validators.py"
    ]
   ],
   [
    "src/attr/validators.py",
    "instance_of",
    "open",
    null
   ]
  ]
 }
}
```
</details>

## Step 5

`.` lists 15 entries (complete): `.github/`, `bench/`, `changelog.d/`, `docs/`, `src/`, `tests/` and 1 more.

Chain: `tests/test_dunders.py` takes `instance_of` from `attr.validators` (`src/attr/validators.py`); `src/attr/validators.py` is not yet closed for `instance_of`.

Still to settle: close the namespace of `src/attr/validators.py` for `instance_of`.

Next: outline `src/attr/validators.py` filtered to `instance_of`, because module `src/attr/validators.py` (step 3), name `instance_of` (task). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `src/attr/validators.py`, is more likely to hit the cap (about 15% against under 5%). Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done.

**Call:** `symbols('src/attr/validators.py', 'instance_of')`

**Response**: outcome `def`

```
module src/attr/validators.py lines=767 dynamic=no all=static@19
114 def instance_of
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/attr/validators.py",
    "instance_of"
   ],
   "desc": "close the namespace of `src/attr/validators.py` for `instance_of`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/validators.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attr/validators.py\", \"instance_of\"]]",
   "v1": [
    12634681,
    11896550
   ],
   "v2": [
    12634681,
    11896550
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
     "src/attr/validators.py",
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/validators.py')",
   "key": "[\"symbols\", [\"src/attr/validators.py\"]]",
   "v1": [
    11618714673,
    9714246868
   ],
   "v2": [
    174298612907,
    145713703020
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
     "src/attr/validators.py",
     "instance_of"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/attr/validators.py', 'instance_of')",
  "key": "[\"symbols\", [\"src/attr/validators.py\", \"instance_of\"]]",
  "provenance": "module `src/attr/validators.py` (step 3), name `instance_of` (task)",
  "v2": [
   12634681,
   11896550
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
 "adherence": {
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 5,
   "path": "src/attr/validators.py",
   "filter": "instance_of",
   "header": {
    "lines": 767,
    "dynamic": false,
    "all_status": "static",
    "all_line": 19
   },
   "bindings": [
    {
     "module": "src/attr/validators.py",
     "name": "instance_of",
     "line": 114,
     "kind": "def",
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
    "tests/test_dunders.py",
    "instance_of",
    "reexport",
    [
     "attr.validators",
     "src/attr/validators.py"
    ]
   ],
   [
    "src/attr/validators.py",
    "instance_of",
    "def",
    114
   ]
  ]
 }
}
```
</details>

## Step 6

In `src/attr/validators.py`, `instance_of` has exactly one binding: a def at line 114. No dynamic namespace tricks, a literal `__all__` at line 19. This is not the branch I planned for that outcome; the open items changed more than expected.

Candidate modules so far: 0; statements confirmed: 0, ruled out: 0, modules with no such import: 0, pending: 0. import coverage open at `.`; star coverage open at `.`.

Open: cover `.` for import lines; cover `.` for star lines.

Next: grep from-imports naming `instance_of` or star imports under `.`, because import and star lines under `.` in one call. I expect: hits under the cap (about 45%); no hits (about 45%); a capped result (about 10%). The alternative, grep from-imports naming `instance_of` under `.`, serves fewer of the open items. Plan by outcome: zero: done; mid: outline each module that appears; cap: list the scope and split it.

**Call:** `grep('^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\binstance_of\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*instance_of\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$', '.')`

**Response**: outcome `mid`

```
src/attrs/converters.py:3:from attr.converters import *  # noqa: F403
src/attrs/exceptions.py:3:from attr.exceptions import *  # noqa: F403
src/attrs/filters.py:3:from attr.filters import *  # noqa: F403
src/attrs/setters.py:3:from attr.setters import *  # noqa: F403
src/attrs/validators.py:3:from attr.validators import *  # noqa: F403
tests/attr_import_star.py:4:from attr import *  # noqa: F403
tests/test_dunders.py:27:from attr.validators import instance_of
tests/test_funcs.py:22:from attr.validators import instance_of
tests/test_mypy.yml:1384:            from other import *
tests/test_setattr.py:12:from attr.validators import instance_of, matches_re
tests/test_validators.py:24:    instance_of,
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
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\binstance_of\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*instance_of\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\binstance_of\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*instance_of\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
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
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\binstance_of\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*instance_of\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\binstance_of\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*instance_of\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
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
  "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\binstance_of\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*instance_of\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
  "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\binstance_of\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*instance_of\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
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
 "adherence": {
  "planned": "done",
  "status": "deviated"
 },
 "facts": [
  {
   "kind": "grep",
   "step": 6,
   "pattern": "^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\binstance_of\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*instance_of\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$",
   "scope": ".",
   "hits": [
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
     27
    ],
    [
     "tests/test_funcs.py",
     22
    ],
    [
     "tests/test_mypy.yml",
     1384
    ],
    [
     "tests/test_setattr.py",
     12
    ],
    [
     "tests/test_validators.py",
     24
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "verdicts": [
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
    "tests/test_dunders.py",
    27,
    "in",
    "`attr.validators` resolves `instance_of` to the target"
   ],
   [
    "tests/test_funcs.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_setattr.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_validators.py",
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

## Step 7

The grep under `.` returned 11 lines, under the cap, so these are all of them: `src/attrs/converters.py`, `src/attrs/exceptions.py`, `src/attrs/filters.py`, `src/attrs/setters.py` and 7 more files.

Candidate modules so far: 10; statements confirmed: 1, ruled out: 0, modules with no such import: 0, pending: 9. import coverage complete; star coverage complete.

Open: outline `src/attrs/converters.py` for its `instance_of` imports; outline `src/attrs/exceptions.py` for its `instance_of` imports; outline `src/attrs/filters.py` for its `instance_of` imports; outline `src/attrs/setters.py` for its `instance_of` imports; and 5 more.

Next: outline `tests/test_validators.py` filtered to `instance_of`, because `tests/test_validators.py` had a matching line (step 6); its outline names every `instance_of` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/attrs/converters.py` filtered to `instance_of`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/attrs/converters.py` filtered to `instance_of`; cap: outline `src/attrs/converters.py` filtered to `instance_of`.

**Call:** `symbols('tests/test_validators.py', 'instance_of')`

**Response**: outcome `ok`

```
module tests/test_validators.py lines=1405 dynamic=no all=none
16 from instance_of <- attr.validators instance_of
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
    "instance_of"
   ],
   "desc": "outline `src/attrs/converters.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/exceptions.py",
    "instance_of"
   ],
   "desc": "outline `src/attrs/exceptions.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "instance_of"
   ],
   "desc": "outline `src/attrs/filters.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "instance_of"
   ],
   "desc": "outline `src/attrs/setters.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "instance_of"
   ],
   "desc": "outline `src/attrs/validators.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "instance_of"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "instance_of"
   ],
   "desc": "outline `tests/test_funcs.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_setattr.py",
    "instance_of"
   ],
   "desc": "outline `tests/test_setattr.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_validators.py",
    "instance_of"
   ],
   "desc": "outline `tests/test_validators.py` for its `instance_of` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attrs/converters.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attrs/converters.py\", \"instance_of\"]]",
   "v1": [
    12194641,
    904550
   ],
   "v2": [
    6106366,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/exceptions.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attrs/exceptions.py\", \"instance_of\"]]",
   "v1": [
    12194641,
    904550
   ],
   "v2": [
    6106366,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/filters.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"instance_of\"]]",
   "v1": [
    12194641,
    904550
   ],
   "v2": [
    6106366,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"instance_of\"]]",
   "v1": [
    12194641,
    904550
   ],
   "v2": [
    6106366,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"instance_of\"]]",
   "v1": [
    12194641,
    904550
   ],
   "v2": [
    6106366,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"instance_of\"]]",
   "v1": [
    12194641,
    904550
   ],
   "v2": [
    6106366,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_funcs.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/test_funcs.py\", \"instance_of\"]]",
   "v1": [
    12194641,
    904550
   ],
   "v2": [
    6106366,
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
     "tests/test_funcs.py",
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_setattr.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/test_setattr.py\", \"instance_of\"]]",
   "v1": [
    12194641,
    904550
   ],
   "v2": [
    6106366,
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
     "tests/test_setattr.py",
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_validators.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/test_validators.py\", \"instance_of\"]]",
   "v1": [
    12194641,
    904550
   ],
   "v2": [
    6106366,
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
     "tests/test_validators.py",
     "instance_of"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_validators.py', 'instance_of')",
  "key": "[\"symbols\", [\"tests/test_validators.py\", \"instance_of\"]]",
  "provenance": "`tests/
```
</details>

## Step 8

In `tests/test_validators.py`, `instance_of` has exactly one binding: line 16 imports it as `instance_of` from `attr.validators`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 10; statements confirmed: 2, ruled out: 0, modules with no such import: 0, pending: 8. import coverage complete; star coverage complete.

Outstanding: outline `src/attrs/converters.py` for its `instance_of` imports; outline `src/attrs/exceptions.py` for its `instance_of` imports; outline `src/attrs/filters.py` for its `instance_of` imports; outline `src/attrs/setters.py` for its `instance_of` imports; and 4 more.

Next: outline `src/attrs/converters.py` filtered to `instance_of`, because `src/attrs/converters.py` had a matching line (step 6); its outline names every `instance_of` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/attrs/exceptions.py` filtered to `instance_of`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/attrs/exceptions.py` filtered to `instance_of`; cap: outline `src/attrs/exceptions.py` filtered to `instance_of`.

**Call:** `symbols('src/attrs/converters.py', 'instance_of')`

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
    "instance_of"
   ],
   "desc": "outline `src/attrs/converters.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/exceptions.py",
    "instance_of"
   ],
   "desc": "outline `src/attrs/exceptions.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "instance_of"
   ],
   "desc": "outline `src/attrs/filters.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "instance_of"
   ],
   "desc": "outline `src/attrs/setters.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "instance_of"
   ],
   "desc": "outline `src/attrs/validators.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "instance_of"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "instance_of"
   ],
   "desc": "outline `tests/test_funcs.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_setattr.py",
    "instance_of"
   ],
   "desc": "outline `tests/test_setattr.py` for its `instance_of` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attrs/converters.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attrs/converters.py\", \"instance_of\"]]",
   "v1": [
    10841691,
    904550
   ],
   "v2": [
    5429891,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/exceptions.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attrs/exceptions.py\", \"instance_of\"]]",
   "v1": [
    10841691,
    904550
   ],
   "v2": [
    5429891,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/filters.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"instance_of\"]]",
   "v1": [
    10841691,
    904550
   ],
   "v2": [
    5429891,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"instance_of\"]]",
   "v1": [
    10841691,
    904550
   ],
   "v2": [
    5429891,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"instance_of\"]]",
   "v1": [
    10841691,
    904550
   ],
   "v2": [
    5429891,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"instance_of\"]]",
   "v1": [
    10841691,
    904550
   ],
   "v2": [
    5429891,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_funcs.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/test_funcs.py\", \"instance_of\"]]",
   "v1": [
    10841691,
    904550
   ],
   "v2": [
    5429891,
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
     "tests/test_funcs.py",
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_setattr.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/test_setattr.py\", \"instance_of\"]]",
   "v1": [
    10841691,
    904550
   ],
   "v2": [
    5429891,
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
     "tests/test_setattr.py",
     "instance_of"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/attrs/converters.py', 'instance_of')",
  "key": "[\"symbols\", [\"src/attrs/converters.py\", \"instance_of\"]]",
  "provenance": "`src/attrs/converters.py` had a matching line (step 6); its outline names every `instance_of` import exactly",
  "v2": [
   5429891,
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
  "ok": "[\"symbols\", [\"src/attrs/exceptions.py\", \"instance_of\"]]",
  "cap": "[\"symbols\", [\"src/attrs/exceptions.py\", \"instance_of\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"src/attrs/converters.py\", \"instance_of\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 8,
   "path": "src/attrs/converters.py",
   "filter": "instance_of",
   "header": {
    "lines": 4,
    "d
```
</details>

## Step 9

`src/attrs/converters.py` binds no `instance_of` at module level; 1 star import(s): `attr.converters`; no `__all__`; no dynamic namespace tricks.

Candidate modules so far: 10; statements confirmed: 2, ruled out: 0, modules with no such import: 0, pending: 8. import coverage complete; star coverage complete.

Still to settle: locate the module `attr.converters` imported by `src/attrs/converters.py`; outline `src/attrs/exceptions.py` for its `instance_of` imports; outline `src/attrs/filters.py` for its `instance_of` imports; outline `src/attrs/setters.py` for its `instance_of` imports; and 4 more.

Next: outline `src/attrs/exceptions.py` filtered to `instance_of`, because `src/attrs/exceptions.py` had a matching line (step 6); its outline names every `instance_of` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/attr/converters.py` filtered to `instance_of`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/attr/converters.py` filtered to `instance_of`; cap: outline `src/attr/converters.py` filtered to `instance_of`.

**Call:** `symbols('src/attrs/exceptions.py', 'instance_of')`

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
    "instance_of"
   ],
   "desc": "outline `src/attrs/exceptions.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "instance_of"
   ],
   "desc": "outline `src/attrs/filters.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "instance_of"
   ],
   "desc": "outline `src/attrs/setters.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "instance_of"
   ],
   "desc": "outline `src/attrs/validators.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "instance_of"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "instance_of"
   ],
   "desc": "outline `tests/test_funcs.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_setattr.py",
    "instance_of"
   ],
   "desc": "outline `tests/test_setattr.py` for its `instance_of` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/converters.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attr/converters.py\", \"instance_of\"]]",
   "v1": [
    27051607207797,
    2306712493280
   ],
   "v2": [
    135488707288313,
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
   "call": "symbols('src/attrs/exceptions.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attrs/exceptions.py\", \"instance_of\"]]",
   "v1": [
    11353141,
    904550
   ],
   "v2": [
    135488707288313,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/filters.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"instance_of\"]]",
   "v1": [
    11353141,
    904550
   ],
   "v2": [
    135488707288313,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"instance_of\"]]",
   "v1": [
    11353141,
    904550
   ],
   "v2": [
    135488707288313,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"instance_of\"]]",
   "v1": [
    11353141,
    904550
   ],
   "v2": [
    135488707288313,
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
     "src/attrs/validators.py",
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"instance_of\"]]",
   "v1": [
    11353141,
    904550
   ],
   "v2": [
    135488707288313,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_funcs.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/test_funcs.py\", \"instance_of\"]]",
   "v1": [
    11353141,
    904550
   ],
   "v2": [
    135488707288313,
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
     "tests/test_funcs.py",
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_setattr.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/test_setattr.py\", \"instance_of\"]]",
   "v1": [
    11353141,
    904550
   ],
   "v2": [
    135488707288313,
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
     "tests/test_setattr.py",
     "instance_of"
    ]
   ]
  },
  {
   "call": "ls('src/attr')",
   "key": "[\"ls\", [\"src/attr\"]]",
   "v1": [
    50644778,
    4034293
   ],
   "v2": [
    32291518192747629,
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
     "src/attrs/converters.py",
     "attr.converters"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/converters/__init__.py', 'instance_of')",
   "key": "[\"symbols
```
</details>

## Step 10

`src/attrs/exceptions.py` binds no `instance_of` at module level; 1 star import(s): `attr.exceptions`; no `__all__`; no dynamic namespace tricks.

Candidate modules so far: 10; statements confirmed: 2, ruled out: 0, modules with no such import: 0, pending: 8. import coverage complete; star coverage complete.

Still to settle: locate the module `attr.converters` imported by `src/attrs/converters.py`; locate the module `attr.exceptions` imported by `src/attrs/exceptions.py`; outline `src/attrs/filters.py` for its `instance_of` imports; outline `src/attrs/setters.py` for its `instance_of` imports; and 4 more.

Next: outline `src/attr/converters.py` filtered to `instance_of`, because `attr.converters` would be `src/attr/converters.py` if that file exists; one call both checks and closes it. I expect: a definition there ends the chain (about 85%); the file does not exist (about 10%); a re-export continues the chain to its source (under 5%); no binding at all points at a submodule or an unresolved name (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `src/attr/exceptions.py` filtered to `instance_of`, scores the same; the seed broke the tie. Plan by outcome: def: outline `src/attr/exceptions.py` filtered to `instance_of`; reexport: outline `src/attr/exceptions.py` filtered to `instance_of`; star: outline `src/attr/exceptions.py` filtered to `instance_of`; none: outline `src/attr/exceptions.py` filtered to `instance_of`; missing: list `src/attr`.

**Call:** `symbols('src/attr/converters.py', 'instance_of')`

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
    "instance_of"
   ],
   "desc": "outline `src/attrs/filters.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "instance_of"
   ],
   "desc": "outline `src/attrs/setters.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "instance_of"
   ],
   "desc": "outline `src/attrs/validators.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "instance_of"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "instance_of"
   ],
   "desc": "outline `tests/test_funcs.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_setattr.py",
    "instance_of"
   ],
   "desc": "outline `tests/test_setattr.py` for its `instance_of` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/converters.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attr/converters.py\", \"instance_of\"]]",
   "v1": [
    28355866900117,
    2306712493280
   ],
   "v2": [
    3069168664709310559,
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
   "call": "symbols('src/attr/exceptions.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attr/exceptions.py\", \"instance_of\"]]",
   "v1": [
    28355866900117,
    2306712493280
   ],
   "v2": [
    3069168664709310559,
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
    48982007,
    4034293
   ],
   "v2": [
    31231451132009229,
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
   "call": "symbols('src/attrs/filters.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"instance_of\"]]",
   "v1": [
    11864591,
    904550
   ],
   "v2": [
    2453134643,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"instance_of\"]]",
   "v1": [
    11864591,
    904550
   ],
   "v2": [
    2453134643,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"instance_of\"]]",
   "v1": [
    11864591,
    904550
   ],
   "v2": [
    2453134643,
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
     "src/attrs/validators.py",
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"instance_of\"]]",
   "v1": [
    11864591,
    904550
   ],
   "v2": [
    2453134643,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_funcs.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/test_funcs.py\", \"instance_of\"]]",
   "v1": [
    11864591,
    904550
   ],
   "v2": [
    2453134643,
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
     "tests/test_funcs.py",
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_setattr.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/test_setattr.py\", \"instance_of\"]]",
   "v1": [
    11864591,
    904550
   ],
   "v2": [
    2453134643,
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
 
```
</details>

## Step 11

`src/attr/converters.py` binds no `instance_of` at module level; no star imports; a literal `__all__` at line 11; no dynamic namespace tricks.

Candidate modules so far: 10; statements confirmed: 2, ruled out: 0, modules with no such import: 0, pending: 8. import coverage complete; star coverage complete.

Outstanding: know what `src/attr/converters.py` exports; locate the module `attr.exceptions` imported by `src/attrs/exceptions.py`; outline `src/attrs/filters.py` for its `instance_of` imports; outline `src/attrs/setters.py` for its `instance_of` imports; and 4 more.

Next: outline `src/attr/exceptions.py` filtered to `instance_of`, because `attr.exceptions` would be `src/attr/exceptions.py` if that file exists; one call both checks and closes it. I expect: a definition there ends the chain (about 85%); the file does not exist (about 10%); a re-export continues the chain to its source (under 5%); no binding at all points at a submodule or an unresolved name (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `src/attrs/filters.py` filtered to `instance_of`, is expected to open more follow-up work. Plan by outcome: def: outline `src/attrs/filters.py` filtered to `instance_of`; reexport: outline `src/attrs/filters.py` filtered to `instance_of`; star: outline `src/attrs/filters.py` filtered to `instance_of`; none: outline `src/attrs/filters.py` filtered to `instance_of`; missing: outline `src/attrs/filters.py` filtered to `instance_of`.

**Call:** `symbols('src/attr/exceptions.py', 'instance_of')`

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
    "instance_of"
   ],
   "desc": "outline `src/attrs/filters.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "instance_of"
   ],
   "desc": "outline `src/attrs/setters.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "instance_of"
   ],
   "desc": "outline `src/attrs/validators.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "instance_of"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "instance_of"
   ],
   "desc": "outline `tests/test_funcs.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_setattr.py",
    "instance_of"
   ],
   "desc": "outline `tests/test_setattr.py` for its `instance_of` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/exceptions.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attr/exceptions.py\", \"instance_of\"]]",
   "v1": [
    25908132682357,
    2306712493280
   ],
   "v2": [
    129771334661113,
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
   "call": "symbols('src/attrs/filters.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"instance_of\"]]",
   "v1": [
    10904741,
    904550
   ],
   "v2": [
    129771334661113,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"instance_of\"]]",
   "v1": [
    10904741,
    904550
   ],
   "v2": [
    129771334661113,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"instance_of\"]]",
   "v1": [
    10904741,
    904550
   ],
   "v2": [
    129771334661113,
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
     "src/attrs/validators.py",
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"instance_of\"]]",
   "v1": [
    10904741,
    904550
   ],
   "v2": [
    129771334661113,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_funcs.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/test_funcs.py\", \"instance_of\"]]",
   "v1": [
    10904741,
    904550
   ],
   "v2": [
    129771334661113,
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
     "tests/test_funcs.py",
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_setattr.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/test_setattr.py\", \"instance_of\"]]",
   "v1": [
    10904741,
    904550
   ],
   "v2": [
    129771334661113,
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
     "tests/test_setattr.py",
     "instance_of"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    7021729,
    578912
   ],
   "v2": [
    13062193489301,
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
   "call": "ls('src/attr')",
   "key": "[\"ls\", [\"src/attr\"]]",
   "v1": [
    48644914,
    4034293
   ],
   "v2": [
    31016544096882029,
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
     "src/attrs/exceptions.py",
     "attr.exceptions"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/exceptions/__init__.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attr/exceptions/__init__.py\", \"instance_of\"]]",
   "v1": [
    61436907563,
    47412
```
</details>

## Step 12

`src/attr/exceptions.py` binds no `instance_of` at module level; no star imports; no `__all__`; no dynamic namespace tricks.

Candidate modules so far: 10; statements confirmed: 2, ruled out: 1, modules with no such import: 0, pending: 7. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/exceptions.py`:3, star import of `attr.exceptions`, which does not export `instance_of`.

Open: know what `src/attr/converters.py` exports; outline `src/attrs/filters.py` for its `instance_of` imports; outline `src/attrs/setters.py` for its `instance_of` imports; outline `src/attrs/validators.py` for its `instance_of` imports; and 3 more.

Next: outline `src/attrs/filters.py` filtered to `instance_of`, because `src/attrs/filters.py` had a matching line (step 6); its outline names every `instance_of` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/attrs/setters.py` filtered to `instance_of`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/attrs/setters.py` filtered to `instance_of`; cap: outline `src/attrs/setters.py` filtered to `instance_of`.

**Call:** `symbols('src/attrs/filters.py', 'instance_of')`

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
    "instance_of"
   ],
   "desc": "outline `src/attrs/filters.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "instance_of"
   ],
   "desc": "outline `src/attrs/setters.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "instance_of"
   ],
   "desc": "outline `src/attrs/validators.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "instance_of"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "instance_of"
   ],
   "desc": "outline `tests/test_funcs.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_setattr.py",
    "instance_of"
   ],
   "desc": "outline `tests/test_setattr.py` for its `instance_of` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attrs/filters.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"instance_of\"]]",
   "v1": [
    9040341,
    904550
   ],
   "v2": [
    4529216,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"instance_of\"]]",
   "v1": [
    9040341,
    904550
   ],
   "v2": [
    4529216,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"instance_of\"]]",
   "v1": [
    9040341,
    904550
   ],
   "v2": [
    4529216,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"instance_of\"]]",
   "v1": [
    9040341,
    904550
   ],
   "v2": [
    4529216,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_funcs.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/test_funcs.py\", \"instance_of\"]]",
   "v1": [
    9040341,
    904550
   ],
   "v2": [
    4529216,
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
     "tests/test_funcs.py",
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_setattr.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/test_setattr.py\", \"instance_of\"]]",
   "v1": [
    9040341,
    904550
   ],
   "v2": [
    4529216,
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
     "tests/test_setattr.py",
     "instance_of"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    5828513,
    578912
   ],
   "v2": [
    146002281,
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
  }
 ],
 "choice": {
  "call": "symbols('src/attrs/filters.py', 'instance_of')",
  "key": "[\"symbols\", [\"src/attrs/filters.py\", \"instance_of\"]]",
  "provenance": "`src/attrs/filters.py` had a matching line (step 6); its outline names every `instance_of` import exactly",
  "v2": [
   4529216,
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
  "ok": "[\"symbols\", [\"src/attrs/setters.py\", \"instance_of\"]]",
  "cap": "[\"symbols\", [\"src/attrs/setters.py\", \"instance_of\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"src/attrs/filters.py\", \"instance_of\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 12,
   "path": "src/attrs/filters.py",
   "filter": "instance_of",
   "header": {
    "lines": 4,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/attrs/filters.py",
     "name": "*",
     "line": 3,
     "kind": "star",
     "src": "attr.filters",
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
    "src/attrs/converters.py",
    3,
    "pending",
    ""
   ],
   [
    "src/attrs/exceptions.py",
    3,
    "out",
    "star import of `attr.exceptions`, which does not export `instance_of`"
   ],
   [
    "src/attrs/filters.py",
    3,
    "pending",
    ""
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
    "pendi
```
</details>

## Step 13

`src/attrs/filters.py` binds no `instance_of` at module level; 1 star import(s): `attr.filters`; no `__all__`; no dynamic namespace tricks.

Candidate modules so far: 10; statements confirmed: 2, ruled out: 1, modules with no such import: 0, pending: 7. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/exceptions.py`:3, star import of `attr.exceptions`, which does not export `instance_of`.

Outstanding: know what `src/attr/converters.py` exports; locate the module `attr.filters` imported by `src/attrs/filters.py`; outline `src/attrs/setters.py` for its `instance_of` imports; outline `src/attrs/validators.py` for its `instance_of` imports; and 3 more.

Next: outline `src/attrs/setters.py` filtered to `instance_of`, because `src/attrs/setters.py` had a matching line (step 6); its outline names every `instance_of` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/attr/filters.py` filtered to `instance_of`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/attr/filters.py` filtered to `instance_of`; cap: outline `src/attr/filters.py` filtered to `instance_of`.

**Call:** `symbols('src/attrs/setters.py', 'instance_of')`

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
    "instance_of"
   ],
   "desc": "outline `src/attrs/setters.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "instance_of"
   ],
   "desc": "outline `src/attrs/validators.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "instance_of"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "instance_of"
   ],
   "desc": "outline `tests/test_funcs.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_setattr.py",
    "instance_of"
   ],
   "desc": "outline `tests/test_setattr.py` for its `instance_of` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/filters.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attr/filters.py\", \"instance_of\"]]",
   "v1": [
    22457945663637,
    2306712493280
   ],
   "v2": [
    112520399567513,
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
   "call": "symbols('src/attrs/setters.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"instance_of\"]]",
   "v1": [
    9551791,
    904550
   ],
   "v2": [
    112520399567513,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"instance_of\"]]",
   "v1": [
    9551791,
    904550
   ],
   "v2": [
    112520399567513,
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
     "src/attrs/validators.py",
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"instance_of\"]]",
   "v1": [
    9551791,
    904550
   ],
   "v2": [
    112520399567513,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_funcs.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/test_funcs.py\", \"instance_of\"]]",
   "v1": [
    9551791,
    904550
   ],
   "v2": [
    112520399567513,
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
     "tests/test_funcs.py",
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_setattr.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/test_setattr.py\", \"instance_of\"]]",
   "v1": [
    9551791,
    904550
   ],
   "v2": [
    112520399567513,
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
     "tests/test_setattr.py",
     "instance_of"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    6155841,
    578912
   ],
   "v2": [
    11337099979941,
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
   "call": "ls('src/attr')",
   "key": "[\"ls\", [\"src/attr\"]]",
   "v1": [
    42610757,
    4034293
   ],
   "v2": [
    27169585571009229,
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
     "src/attrs/filters.py",
     "attr.filters"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/filters/__init__.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attr/filters/__init__.py\", \"instance_of\"]]",
   "v1": [
    54345284843,
    4741289280
   ],
   "v2": [
    4057664896247257759,
    377839506399264000
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     17,
     936
    ],
    "reexport": [
     187,
     4680
    ],
    "star": [
     17,
     9360
    ],
    "none": [
     119,
     3120
    ],
    "missing": [
     469,
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
  }
 ],
 "choice": {
  "call": "symbols('src/attrs/setters.py', 'instance_of')",
  "key": "[\"symbols\", [\"src/attrs/setters.py\", \"instance_of\"]]",
  "provenance": "`src/attrs/setters.py` had a matching line (step 6); its outline names every `ins
```
</details>

## Step 14

`src/attrs/setters.py` binds no `instance_of` at module level; 1 star import(s): `attr.setters`; no `__all__`; no dynamic namespace tricks.

Candidate modules so far: 10; statements confirmed: 2, ruled out: 1, modules with no such import: 0, pending: 7. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/exceptions.py`:3, star import of `attr.exceptions`, which does not export `instance_of`.

Open: know what `src/attr/converters.py` exports; locate the module `attr.filters` imported by `src/attrs/filters.py`; locate the module `attr.setters` imported by `src/attrs/setters.py`; outline `src/attrs/validators.py` for its `instance_of` imports; and 3 more.

Next: outline `src/attr/filters.py` filtered to `instance_of`, because `attr.filters` would be `src/attr/filters.py` if that file exists; one call both checks and closes it. I expect: a definition there ends the chain (about 85%); the file does not exist (about 10%); a re-export continues the chain to its source (under 5%); no binding at all points at a submodule or an unresolved name (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `src/attr/setters.py` filtered to `instance_of`, scores the same; the seed broke the tie. Plan by outcome: def: outline `src/attr/setters.py` filtered to `instance_of`; reexport: outline `src/attr/setters.py` filtered to `instance_of`; star: outline `src/attr/setters.py` filtered to `instance_of`; none: outline `src/attr/setters.py` filtered to `instance_of`; missing: list `src/attr`.

**Call:** `symbols('src/attr/filters.py', 'instance_of')`

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
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "instance_of"
   ],
   "desc": "outline `src/attrs/validators.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "instance_of"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "instance_of"
   ],
   "desc": "outline `tests/test_funcs.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_setattr.py",
    "instance_of"
   ],
   "desc": "outline `tests/test_setattr.py` for its `instance_of` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/filters.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attr/filters.py\", \"instance_of\"]]",
   "v1": [
    23762205355957,
    2306712493280
   ],
   "v2": [
    2536487672048516959,
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
   "call": "symbols('src/attr/setters.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attr/setters.py\", \"instance_of\"]]",
   "v1": [
    23762205355957,
    2306712493280
   ],
   "v2": [
    2536487672048516959,
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
    40947986,
    4034293
   ],
   "v2": [
    26109518510270829,
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
   "call": "symbols('src/attrs/validators.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"instance_of\"]]",
   "v1": [
    10063241,
    904550
   ],
   "v2": [
    2051433593,
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
     "src/attrs/validators.py",
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"instance_of\"]]",
   "v1": [
    10063241,
    904550
   ],
   "v2": [
    2051433593,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_funcs.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/test_funcs.py\", \"instance_of\"]]",
   "v1": [
    10063241,
    904550
   ],
   "v2": [
    2051433593,
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
     "tests/test_funcs.py",
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_setattr.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/test_setattr.py\", \"instance_of\"]]",
   "v1": [
    10063241,
    904550
   ],
   "v2": [
    2051433593,
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
     "tests/test_setattr.py",
     "instance_of"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    6483169,
    578912
   ],
   "v2": [
    1322438431,
    129097376
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
   "call": "symbols('src/attr/filters/__init__.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attr/filters/__init__.py\", \"instance_of\"]]",
   "v1": [
    57026101163,
    4741289280
   ],
   "v2": [
    186838176355639551443,
    16851641985407174400
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     17,
     936
    ],
    "reexport": [
     187,
     4680
    ],
    "star": [
     17,
     9360
    ],
    "none": [
     119,
     3120
    ],
    "missing": [
     469,
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
   "call"
```
</details>

## Step 15

`src/attr/filters.py` binds no `instance_of` at module level; no star imports; no `__all__`; no dynamic namespace tricks.

Candidate modules so far: 10; statements confirmed: 2, ruled out: 2, modules with no such import: 0, pending: 6. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/filters.py`:3, star import of `attr.filters`, which does not export `instance_of`.

Still to settle: know what `src/attr/converters.py` exports; locate the module `attr.setters` imported by `src/attrs/setters.py`; outline `src/attrs/validators.py` for its `instance_of` imports; outline `tests/attr_import_star.py` for its `instance_of` imports; and 2 more.

Next: outline `src/attr/setters.py` filtered to `instance_of`, because `attr.setters` would be `src/attr/setters.py` if that file exists; one call both checks and closes it. I expect: a definition there ends the chain (about 85%); the file does not exist (about 10%); a re-export continues the chain to its source (under 5%); no binding at all points at a submodule or an unresolved name (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `src/attrs/validators.py` filtered to `instance_of`, is expected to open more follow-up work. Plan by outcome: def: outline `src/attrs/validators.py` filtered to `instance_of`; reexport: outline `src/attrs/validators.py` filtered to `instance_of`; star: outline `src/attrs/validators.py` filtered to `instance_of`; none: outline `src/attrs/validators.py` filtered to `instance_of`; missing: outline `src/attrs/validators.py` filtered to `instance_of`.

**Call:** `symbols('src/attr/setters.py', 'instance_of')`

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
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "instance_of"
   ],
   "desc": "outline `src/attrs/validators.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "instance_of"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "instance_of"
   ],
   "desc": "outline `tests/test_funcs.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_setattr.py",
    "instance_of"
   ],
   "desc": "outline `tests/test_setattr.py` for its `instance_of` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/setters.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attr/setters.py\", \"instance_of\"]]",
   "v1": [
    19007758644917,
    2306712493280
   ],
   "v2": [
    95269464473913,
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
   "call": "symbols('src/attrs/validators.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"instance_of\"]]",
   "v1": [
    8198841,
    904550
   ],
   "v2": [
    95269464473913,
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
     "src/attrs/validators.py",
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"instance_of\"]]",
   "v1": [
    8198841,
    904550
   ],
   "v2": [
    95269464473913,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_funcs.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/test_funcs.py\", \"instance_of\"]]",
   "v1": [
    8198841,
    904550
   ],
   "v2": [
    95269464473913,
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
     "tests/test_funcs.py",
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_setattr.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/test_setattr.py\", \"instance_of\"]]",
   "v1": [
    8198841,
    904550
   ],
   "v2": [
    95269464473913,
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
     "tests/test_setattr.py",
     "instance_of"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    5289953,
    578912
   ],
   "v2": [
    9612006470581,
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
   "call": "ls('src/attr')",
   "key": "[\"ls\", [\"src/attr\"]]",
   "v1": [
    36576600,
    4034293
   ],
   "v2": [
    23322627045136429,
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
   "call": "symbols('src/attr/setters/__init__.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attr/setters/__init__.py\", \"instance_of\"]]",
   "v1": [
    47253662123,
    4741289280
   ],
   "v2": [
    3492524262580921759,
    377839506399264000
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     17,
     936
    ],
    "reexport": [
     187,
     4680
    ],
    "star": [
     17,
     9360
    ],
    "none": [
     119,
     3120
    ],
    "missing": [
     469,
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
  }
 ],
 "choice": {
  "call": "symbols('src/attr/setters.py', 'instance_of')",
  "key": "[\"symbols\", [\"src/attr/setters.py\", \"instance_of\"]]",
  "provenance": "`attr.setters` would be `src/attr/setters.py` if that file exists; one call both checks and closes it",
  "v2": [
   95269464473913,
   11533562466400
  ]
 },
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
 "plan": {
  "def": "[\"symbols\", [\"src/attrs/validators.py\", \"instance_of\"]]",
  "reexport": "[\"symbols\", [\"src/attrs/validators.py\", \"instance_of\"]]",
  "star": "[\"symbols\", [\"src/attrs/validators.py\", \"instance_of\"]]",
  "none": "[\"symbols\", [\"src/attrs/validators.py\", \"instance_of\"]]",
  "missing": "[\"symbols\", [\"src/attrs/validators.py\", \"instance_of\
```
</details>

## Step 16

`src/attr/setters.py` binds no `instance_of` at module level; no star imports; no `__all__`; no dynamic namespace tricks.

Candidate modules so far: 10; statements confirmed: 2, ruled out: 3, modules with no such import: 0, pending: 5. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/setters.py`:3, star import of `attr.setters`, which does not export `instance_of`.

Outstanding: know what `src/attr/converters.py` exports; outline `src/attrs/validators.py` for its `instance_of` imports; outline `tests/attr_import_star.py` for its `instance_of` imports; outline `tests/test_funcs.py` for its `instance_of` imports; and 1 more.

Next: outline `src/attrs/validators.py` filtered to `instance_of`, because `src/attrs/validators.py` had a matching line (step 6); its outline names every `instance_of` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `tests/attr_import_star.py` filtered to `instance_of`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `tests/attr_import_star.py` filtered to `instance_of`; cap: outline `tests/attr_import_star.py` filtered to `instance_of`.

**Call:** `symbols('src/attrs/validators.py', 'instance_of')`

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
   "desc": "know what `src/attr/converters.py` exports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "instance_of"
   ],
   "desc": "outline `src/attrs/validators.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "instance_of"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "instance_of"
   ],
   "desc": "outline `tests/test_funcs.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_setattr.py",
    "instance_of"
   ],
   "desc": "outline `tests/test_setattr.py` for its `instance_of` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attrs/validators.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"instance_of\"]]",
   "v1": [
    6334441,
    904550
   ],
   "v2": [
    3176266,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"instance_of\"]]",
   "v1": [
    6334441,
    904550
   ],
   "v2": [
    3176266,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_funcs.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/test_funcs.py\", \"instance_of\"]]",
   "v1": [
    6334441,
    904550
   ],
   "v2": [
    3176266,
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
     "tests/test_funcs.py",
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_setattr.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/test_setattr.py\", \"instance_of\"]]",
   "v1": [
    6334441,
    904550
   ],
   "v2": [
    3176266,
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
     "tests/test_setattr.py",
     "instance_of"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    4096737,
    578912
   ],
   "v2": [
    102707881,
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
  }
 ],
 "choice": {
  "call": "symbols('src/attrs/validators.py', 'instance_of')",
  "key": "[\"symbols\", [\"src/attrs/validators.py\", \"instance_of\"]]",
  "provenance": "`src/attrs/validators.py` had a matching line (step 6); its outline names every `instance_of` import exactly",
  "v2": [
   3176266,
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
  "ok": "[\"symbols\", [\"tests/attr_import_star.py\", \"instance_of\"]]",
  "cap": "[\"symbols\", [\"tests/attr_import_star.py\", \"instance_of\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"src/attrs/validators.py\", \"instance_of\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 16,
   "path": "src/attrs/validators.py",
   "filter": "instance_of",
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
     "kind": "star",
     "src": "attr.validators",
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
    "src/attrs/converters.py",
    3,
    "pending",
    ""
   ],
   [
    "src/attrs/exceptions.py",
    3,
    "out",
    "star import of `attr.exceptions`, which does not export `instance_of`"
   ],
   [
    "src/attrs/filters.py",
    3,
    "out",
    "star import of `attr.filters`, which does not export `instance_of`"
   ],
   [
    "src/attrs/setters.py",
    3,
    "out",
    "star import of `attr.setters`, which does not export `instance_of`"
   ],
   [
    "src/attrs/validators.py",
    3,
    "pending",
    ""
   ],
   [
    "tests/attr_import_star.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_dunders.py",
    27,
    "in",
    "`attr.validators` resolves `instance_of` to the target"
   ],
   [
    "tests/test_funcs.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_setattr.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_validators.py",
    16,
    "in",
    "`attr.validators` resolves `instance_of` to the target"
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

## Step 17

`src/attrs/validators.py` binds no `instance_of` at module level; 1 star import(s): `attr.validators`; no `__all__`; no dynamic namespace tricks.

Candidate modules so far: 10; statements confirmed: 2, ruled out: 3, modules with no such import: 0, pending: 5. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/setters.py`:3, star import of `attr.setters`, which does not export `instance_of`.

Still to settle: know what `src/attr/converters.py` exports; know what `src/attr/validators.py` exports; outline `tests/attr_import_star.py` for its `instance_of` imports; outline `tests/test_funcs.py` for its `instance_of` imports; and 1 more.

Next: outline `tests/attr_import_star.py` filtered to `instance_of`, because `tests/attr_import_star.py` had a matching line (step 6); its outline names every `instance_of` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `tests/test_funcs.py` filtered to `instance_of`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `tests/test_funcs.py` filtered to `instance_of`; cap: outline `tests/test_funcs.py` filtered to `instance_of`.

**Call:** `symbols('tests/attr_import_star.py', 'instance_of')`

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
    "instance_of"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "instance_of"
   ],
   "desc": "outline `tests/test_funcs.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_setattr.py",
    "instance_of"
   ],
   "desc": "outline `tests/test_setattr.py` for its `instance_of` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/attr_import_star.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"instance_of\"]]",
   "v1": [
    5886041,
    904550
   ],
   "v2": [
    2952066,
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
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_funcs.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/test_funcs.py\", \"instance_of\"]]",
   "v1": [
    5886041,
    904550
   ],
   "v2": [
    2952066,
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
     "tests/test_funcs.py",
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_setattr.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/test_setattr.py\", \"instance_of\"]]",
   "v1": [
    5886041,
    904550
   ],
   "v2": [
    2952066,
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
     "tests/test_setattr.py",
     "instance_of"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    3809761,
    578912
   ],
   "v2": [
    95533481,
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
    3809761,
    578912
   ],
   "v2": [
    95533481,
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
  "call": "symbols('tests/attr_import_star.py', 'instance_of')",
  "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"instance_of\"]]",
  "provenance": "`tests/attr_import_star.py` had a matching line (step 6); its outline names every `instance_of` import exactly",
  "v2": [
   2952066,
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
  "ok": "[\"symbols\", [\"tests/test_funcs.py\", \"instance_of\"]]",
  "cap": "[\"symbols\", [\"tests/test_funcs.py\", \"instance_of\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"tests/attr_import_star.py\", \"instance_of\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 17,
   "path": "tests/attr_import_star.py",
   "filter": "instance_of",
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
    "src/attrs/converters.py",
    3,
    "pending",
    ""
   ],
   [
    "src/attrs/exceptions.py",
    3,
    "out",
    "star import of `attr.exceptions`, which does not export `instance_of`"
   ],
   [
    "src/attrs/filters.py",
    3,
    "out",
    "star import of `attr.filters`, which does not export `instance_of`"
   ],
   [
    "src/attrs/setters.py",
    3,
    "out",
    "star import of `attr.setters`, which does not export `instance_of`"
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
    "tests/test_dunders.py",
    27,
    "in",
    "`attr.validators` resolves `instance_of` to the target"
   ],
   [
    "tests/test_funcs.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_setattr.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_validators.py",
    16,
    "in",
    "`attr.validators` resolves `instance_of` to the target"
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

## Step 18

`tests/attr_import_star.py` binds no `instance_of` at module level; 1 star import(s): `attr`; no `__all__`; no dynamic namespace tricks.

Candidate modules so far: 10; statements confirmed: 2, ruled out: 3, modules with no such import: 0, pending: 5. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/setters.py`:3, star import of `attr.setters`, which does not export `instance_of`.

Open: know what `src/attr/converters.py` exports; know what `src/attr/validators.py` exports; locate the module `attr` imported by `tests/attr_import_star.py`; outline `tests/test_funcs.py` for its `instance_of` imports; and 1 more.

Next: outline `tests/test_funcs.py` filtered to `instance_of`, because `tests/test_funcs.py` had a matching line (step 6); its outline names every `instance_of` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/attr.py` filtered to `instance_of`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/attr.py` filtered to `instance_of`; cap: outline `src/attr.py` filtered to `instance_of`.

**Call:** `symbols('tests/test_funcs.py', 'instance_of')`

**Response**: outcome `ok`

```
module tests/test_funcs.py lines=851 dynamic=no all=none
22 from instance_of <- attr.validators instance_of
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
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/attr_import_star.py",
    "attr"
   ],
   "desc": "locate the module `attr` imported by `tests/attr_import_star.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_funcs.py",
    "instance_of"
   ],
   "desc": "outline `tests/test_funcs.py` for its `instance_of` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_setattr.py",
    "instance_of"
   ],
   "desc": "outline `tests/test_setattr.py` for its `instance_of` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attr.py\", \"instance_of\"]]",
   "v1": [
    14414097100757,
    2306712493280
   ],
   "v2": [
    72301156753113,
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
     "tests/attr_import_star.py",
     "attr"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_funcs.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/test_funcs.py\", \"instance_of\"]]",
   "v1": [
    6397491,
    904550
   ],
   "v2": [
    72301156753113,
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
     "tests/test_funcs.py",
     "instance_of"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_setattr.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/test_setattr.py\", \"instance_of\"]]",
   "v1": [
    6397491,
    904550
   ],
   "v2": [
    72301156753113,
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
     "tests/test_setattr.py",
     "instance_of"
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
    7315175698501,
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
    4137089,
    578912
   ],
   "v2": [
    7315175698501,
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
   "call": "ls('src')",
   "key": "[\"ls\", [\"src\"]]",
   "v1": [
    6725031,
    940732
   ],
   "v2": [
    4251899536303741,
    599745248252800
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
     "tests/attr_import_star.py",
     "attr"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/__init__.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attr/__init__.py\", \"instance_of\"]]",
   "v1": [
    1421867053,
    195382800
   ],
   "v2": [
    113365301877971639,
    15570309329640000
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     49,
     270
    ],
    "reexport": [
     539,
     1350
    ],
    "star": [
     49,
     2700
    ],
    "none": [
     343,
     900
    ],
    "missing": [
     1,
     50
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/attr_import_star.py",
     "attr"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_funcs.py', 'instance_of')",
  "key": "[\"symbols\", [\"tests/test_funcs.py\", \"instance_of\"]]",
  "provenance": "`tests/test_funcs.py` had a matching line (step 6); its outline names every `instance_of` import exactly",
  "v2": [
   72301156753113,
   11533562466400
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
  "ok": "[\"symbols\", [\"src/attr.py\", \"instance_of\"]]",
  "cap": "[\"symbols\", [\"src/attr.py\", \"instance_of\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"tests/test_funcs.py\", \"instance_of\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 18,
   "path": "tests/test_funcs.py",
   "filter": "instance_of",
   "header": {
    "lines": 851,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_funcs.py",
     "name": "instance_of",
     "line": 22,
     "kind": "from",
     "src": "attr.validators",
     "src_name": "instance_of",
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
    "src/attrs/converters.py",
    3,
    "pending",
    ""
   ],
   [
    "src/attrs/exceptions.py",
    3,
    "out",
    "star import of `attr.exceptions`, which does not export `instance_of`"
   ],
   [
    "src/attrs/filters.py",
    3,
    "out",
    "star import of `attr.filters`, which does not export `instance_of`"
   ],
   [
    "src/attrs/setters.py",
    3,
    "out",
    "star import of `attr.setters`, which does not export `instance_of`"
   ],
   [
    "src/attrs/validators.py",
    3,
    "pending",
    ""
   ],
   [
    "tests/attr_impo
```
</details>

## Step 19

In `tests/test_funcs.py`, `instance_of` has exactly one binding: line 22 imports it as `instance_of` from `attr.validators`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 10; statements confirmed: 3, ruled out: 3, modules with no such import: 0, pending: 4. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/setters.py`:3, star import of `attr.setters`, which does not export `instance_of`.

Outstanding: know what `src/attr/converters.py` exports; know what `src/attr/validators.py` exports; locate the module `attr` imported by `tests/attr_import_star.py`; outline `tests/test_setattr.py` for its `instance_of` imports.

Next: outline `src/attr.py` filtered to `instance_of`, because `attr` would be `src/attr.py` if that file exists; one call both checks and closes it. I expect: a definition there ends the chain (about 85%); the file does not exist (about 10%); a re-export continues the chain to its source (under 5%); no binding at all points at a submodule or an unresolved name (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `tests/test_setattr.py` filtered to `instance_of`, is expected to open more follow-up work. Plan by outcome: def: outline `tests/test_setattr.py` filtered to `instance_of`; reexport: outline `tests/test_setattr.py` filtered to `instance_of`; star: outline `tests/test_setattr.py` filtered to `instance_of`; none: outline `tests/test_setattr.py` filtered to `instance_of`; missing: outline `tests/test_setattr.py` filtered to `instance_of`.

**Call:** `symbols('src/attr.py', 'instance_of')`

**Response**: outcome `missing`

```
error: not a python file: src/attr.py
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
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/attr_import_star.py",
    "attr"
   ],
   "desc": "locate the module `attr` imported by `tests/attr_import_star.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_setattr.py",
    "instance_of"
   ],
   "desc": "outline `tests/test_setattr.py` for its `instance_of` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attr.py\", \"instance_of\"]]",
   "v1": [
    10963910082037,
    2306712493280
   ],
   "v2": [
    55050221659513,
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
     "tests/attr_import_star.py",
     "attr"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_setattr.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/test_setattr.py\", \"instance_of\"]]",
   "v1": [
    5044541,
    904550
   ],
   "v2": [
    55050221659513,
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
     "tests/test_setattr.py",
     "instance_of"
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
    5590082189141,
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
    3271201,
    578912
   ],
   "v2": [
    5590082189141,
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
   "call": "ls('src')",
   "key": "[\"ls\", [\"src\"]]",
   "v1": [
    5317963,
    940732
   ],
   "v2": [
    3354850911436541,
    599745248252800
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
     "tests/attr_import_star.py",
     "attr"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/__init__.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attr/__init__.py\", \"instance_of\"]]",
   "v1": [
    1129629853,
    195382800
   ],
   "v2": [
    90076539501611639,
    15570309329640000
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     49,
     270
    ],
    "reexport": [
     539,
     1350
    ],
    "star": [
     49,
     2700
    ],
    "none": [
     343,
     900
    ],
    "missing": [
     1,
     50
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/attr_import_star.py",
     "attr"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/attr.py', 'instance_of')",
  "key": "[\"symbols\", [\"src/attr.py\", \"instance_of\"]]",
  "provenance": "`attr` would be `src/attr.py` if that file exists; one call both checks and closes it",
  "v2": [
   55050221659513,
   11533562466400
  ]
 },
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
 "plan": {
  "def": "[\"symbols\", [\"tests/test_setattr.py\", \"instance_of\"]]",
  "reexport": "[\"symbols\", [\"tests/test_setattr.py\", \"instance_of\"]]",
  "star": "[\"symbols\", [\"tests/test_setattr.py\", \"instance_of\"]]",
  "none": "[\"symbols\", [\"tests/test_setattr.py\", \"instance_of\"]]",
  "missing": "[\"symbols\", [\"tests/test_setattr.py\", \"instance_of\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"src/attr.py\", \"instance_of\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "error",
   "step": 19,
   "call": "[\"symbols\", [\"src/attr.py\", \"instance_of\"]]",
   "error": "not a python file: src/attr.py",
   "missing": "src/attr.py"
  }
 ],
 "goal_state": {
  "verdicts": [
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
    "star import of `attr.exceptions`, which does not export `instance_of`"
   ],
   [
    "src/attrs/filters.py",
    3,
    "out",
    "star import of `attr.filters`, which does not export `instance_of`"
   ],
   [
    "src/attrs/setters.py",
    3,
    "out",
    "star import of `attr.setters`, which does not export `instance_of`"
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
    "tests/test_dunders.py",
    27,
    "in",
    "`attr.validators` resolves `instance_of` to the target"
   ],
   [
    "tests/test_funcs.py",
    22,
    "in",
    "`attr.validators` resolves `instance_of` to the target"
   ],
   [
    "tests/test_setattr.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_validators.py",
    16,
    "in",
    "`attr.validators` resolves `instance_of` to the target"
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

## Step 20

`src/attr.py` does not exist, so that path is ruled out.

Candidate modules so far: 10; statements confirmed: 3, ruled out: 3, modules with no such import: 0, pending: 4. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/setters.py`:3, star import of `attr.setters`, which does not export `instance_of`.

Open: know what `src/attr/converters.py` exports; know what `src/attr/validators.py` exports; locate the module `attr` imported by `tests/attr_import_star.py`; outline `tests/test_setattr.py` for its `instance_of` imports.

Next: outline `tests/test_setattr.py` filtered to `instance_of`, because `tests/test_setattr.py` had a matching line (step 6); its outline names every `instance_of` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/attr/__init__.py` filtered to `instance_of`, is expected to open more follow-up work. Plan by outcome: ok: outline `src/attr/__init__.py` filtered to `instance_of`; cap: outline `src/attr/__init__.py` filtered to `instance_of`.

**Call:** `symbols('tests/test_setattr.py', 'instance_of')`

**Response**: outcome `ok`

```
module tests/test_setattr.py lines=648 dynamic=no all=none
12 from instance_of <- attr.validators instance_of
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
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/attr_import_star.py",
    "attr"
   ],
   "desc": "locate the module `attr` imported by `tests/attr_import_star.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_setattr.py",
    "instance_of"
   ],
   "desc": "outline `tests/test_setattr.py` for its `instance_of` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/__init__.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attr/__init__.py\", \"instance_of\"]]",
   "v1": [
    378113699,
    65127600
   ],
   "v2": [
    379416251,
    65127600
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     49,
     270
    ],
    "reexport": [
     539,
     1350
    ],
    "star": [
     49,
     2700
    ],
    "none": [
     343,
     900
    ],
    "missing": [
     1,
     50
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/attr_import_star.py",
     "attr"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_setattr.py', 'instance_of')",
   "key": "[\"symbols\", [\"tests/test_setattr.py\", \"instance_of\"]]",
   "v1": [
    82823941,
    12211425
   ],
   "v2": [
    379416251,
    65127600
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_setattr.py",
     "instance_of"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    107167403,
    15630624
   ],
   "v2": [
    768438823,
    130255200
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
    107167403,
    15630624
   ],
   "v2": [
    768438823,
    130255200
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
    1478106641,
    217851822
   ],
   "v2": [
    295538525693,
    43570364400
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
     "tests/attr_import_star.py",
     "attr"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_setattr.py', 'instance_of')",
  "key": "[\"symbols\", [\"tests/test_setattr.py\", \"instance_of\"]]",
  "provenance": "`tests/test_setattr.py` had a matching line (step 6); its outline names every `instance_of` import exactly",
  "v2": [
   379416251,
   65127600
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
  "ok": "[\"symbols\", [\"src/attr/__init__.py\", \"instance_of\"]]",
  "cap": "[\"symbols\", [\"src/attr/__init__.py\", \"instance_of\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"tests/test_setattr.py\", \"instance_of\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 20,
   "path": "tests/test_setattr.py",
   "filter": "instance_of",
   "header": {
    "lines": 648,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_setattr.py",
     "name": "instance_of",
     "line": 12,
     "kind": "from",
     "src": "attr.validators",
     "src_name": "instance_of",
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
    "src/attrs/converters.py",
    3,
    "pending",
    ""
   ],
   [
    "src/attrs/exceptions.py",
    3,
    "out",
    "star import of `attr.exceptions`, which does not export `instance_of`"
   ],
   [
    "src/attrs/filters.py",
    3,
    "out",
    "star import of `attr.filters`, which does not export `instance_of`"
   ],
   [
    "src/attrs/setters.py",
    3,
    "out",
    "star import of `attr.setters`, which does not export `instance_of`"
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
    "tests/test_dunders.py",
    27,
    "in",
    "`attr.validators` resolves `instance_of` to the target"
   ],
   [
    "tests/test_funcs.py",
    22,
    "in",
    "`attr.validators` resolves `instance_of` to the target"
   ],
   [
    "tests/test_setattr.py",
    12,
    "in",
    "`attr.validators` resolves `instance_of` to the target"
   ],
   [
    "tests/test_validators.py",
    16,
    "in",
    "`attr.validators` resolves `instance_of` to the target"
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

## Step 21

In `tests/test_setattr.py`, `instance_of` has exactly one binding: line 12 imports it as `instance_of` from `attr.validators`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 10; statements confirmed: 4, ruled out: 3, modules with no such import: 0, pending: 3. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/setters.py`:3, star import of `attr.setters`, which does not export `instance_of`.

Still to settle: know what `src/attr/converters.py` exports; know what `src/attr/validators.py` exports; locate the module `attr` imported by `tests/attr_import_star.py`.

Next: outline `src/attr/__init__.py` filtered to `instance_of`, because `attr` would be `src/attr/__init__.py` if that file exists; one call both checks and closes it. I expect: a re-export continues the chain to its source (about 40%); no binding at all points at a submodule or an unresolved name (about 40%); a definition there ends the chain (about 20%); the file does not exist (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, read `src/attr/converters.py` from line 11, costs more in expectation. Plan by outcome: def: read `src/attr/converters.py` from line 11; reexport: read `src/attr/converters.py` from line 11; star: read `src/attr/converters.py` from line 11; none: read `src/attr/converters.py` from line 11; missing: list `src/attr`.

**Call:** `symbols('src/attr/__init__.py', 'instance_of')`

**Response**: outcome `none`

```
module src/attr/__init__.py lines=121 dynamic=yes all=static@45
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
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/attr_import_star.py",
    "attr"
   ],
   "desc": "locate the module `attr` imported by `tests/attr_import_star.py`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/__init__.py', 'instance_of')",
   "key": "[\"symbols\", [\"src/attr/__init__.py\", \"instance_of\"]]",
   "v1": [
    3553181,
    824400
   ],
   "v2": [
    3237328853,
    735364800
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     49,
     270
    ],
    "reexport": [
     539,
     1350
    ],
    "star": [
     49,
     2700
    ],
    "none": [
     343,
     900
    ],
    "missing": [
     1,
     50
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/attr_import_star.py",
     "attr"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    1060613,
    197856
   ],
   "v2": [
    7260937,
    1648800
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
    1060613,
    197856
   ],
   "v2": [
    7260937,
    1648800
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
    14585597,
    2757618
   ],
   "v2": [
    147791707,
    27576180
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
     "tests/attr_import_star.py",
     "attr"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/attr/__init__.py', 'instance_of')",
  "key": "[\"symbols\", [\"src/attr/__init__.py\", \"instance_of\"]]",
  "provenance": "`attr` would be `src/attr/__init__.py` if that file exists; one call both checks and closes it",
  "v2": [
   3237328853,
   735364800
  ]
 },
 "forecast": {
  "def": [
   49,
   270
  ],
  "reexport": [
   539,
   1350
  ],
  "star": [
   49,
   2700
  ],
  "none": [
   343,
   900
  ],
  "missing": [
   1,
   50
  ]
 },
 "plan": {
  "def": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
  "reexport": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
  "star": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
  "none": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
  "missing": "[\"ls\", [\"src/attr\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"src/attr/__init__.py\", \"instance_of\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 21,
   "path": "src/attr/__init__.py",
   "filter": "instance_of",
   "header": {
    "lines": 121,
    "dynamic": true,
    "all_status": "static",
    "all_line": 45
   },
   "bindings": [],
   "complete": true
  }
 ],
 "goal_state": {
  "verdicts": [
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
    "star import of `attr.exceptions`, which does not export `instance_of`"
   ],
   [
    "src/attrs/filters.py",
    3,
    "out",
    "star import of `attr.filters`, which does not export `instance_of`"
   ],
   [
    "src/attrs/setters.py",
    3,
    "out",
    "star import of `attr.setters`, which does not export `instance_of`"
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
    "tests/test_dunders.py",
    27,
    "in",
    "`attr.validators` resolves `instance_of` to the target"
   ],
   [
    "tests/test_funcs.py",
    22,
    "in",
    "`attr.validators` resolves `instance_of` to the target"
   ],
   [
    "tests/test_setattr.py",
    12,
    "in",
    "`attr.validators` resolves `instance_of` to the target"
   ],
   [
    "tests/test_validators.py",
    16,
    "in",
    "`attr.validators` resolves `instance_of` to the target"
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

`src/attr/__init__.py` binds no `instance_of` at module level; no star imports; a literal `__all__` at line 45; it uses dynamic namespace tricks.

Candidate modules so far: 10; statements confirmed: 4, ruled out: 3, modules with no such import: 0, pending: 3. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/setters.py`:3, star import of `attr.setters`, which does not export `instance_of`.

Open: know what `src/attr/converters.py` exports; know what `src/attr/validators.py` exports; know what `src/attr/__init__.py` exports.

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
  "fits": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]",
  "long": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]"
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
    "src/attrs/converters.py",
    3,
    "out",
    "star import of `attr.converters`, which does not export `instance_of`"
   ],
   [
    "src/attrs/exceptions.py",
    3,
    "out",
    "star import of `attr.exceptions`, which does not export `instance_of`"
   ],
   [
    "src/attrs/filters.py",
    3,
    "out",
    "star import of `attr.filters`, which does not export `instance_of`"
   ],
   [
    "src/attrs/setters.py",
    3,
    "out",
    "star import of `attr.setters`, which does not export `instance_of`"
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
    "tests/test_dunders.py",
    27,
    "in",
    "`attr.validators` resolves `instance_of` to the target"
   ],
   [
    "tests/test_funcs.py",
    22,
    "in",
    "`attr.validators` resolves `instance_of` to the target"
   ],
   [
    "tests/test_setattr.py",
    12,
    "in",
    "`attr.validators` resolves `instance_of` to the target"
   ],
   [
    "tests/test_validators.py",
    16,
    "in",
    "`attr.validators` resolves `instance_of` to the target"
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

The statement at `src/attr/converters.py`:11 binds `__all__`. `__all__` in `src/attr/converters.py` lists 4 names, and `instance_of` is not among them.

Candidate modules so far: 10; statements confirmed: 4, ruled out: 4, modules with no such import: 0, pending: 2. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/setters.py`:3, star import of `attr.setters`, which does not export `instance_of`.

Outstanding: know what `src/attr/validators.py` exports; know what `src/attr/__init__.py` exports.

Next: read `src/attr/__init__.py` from line 45, because `__all__` of `src/attr/__init__.py` starts at line 45 (outline header). I expect: the whole list fits the window (about 90%); the list runs past the window (about 10%). The alternative, read `src/attr/validators.py` from line 19, scores the same; the seed broke the tie. Plan by outcome: fits: read `src/attr/validators.py` from line 19; long: read `src/attr/validators.py` from line 19.

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
  }
 ],
 "candidates": [
  {
   "call": "read('src/attr/__init__.py', 45, 30)",
   "key": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]",
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
  "call": "read('src/attr/__init__.py', 45, 30)",
  "key": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]",
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
 "adherence": {
  "planned": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "read",
   "step": 23,
   "path": "src/attr/__init__.py",
   "start": 45,
   "count": 30,
   "n": 30
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "src/attrs/converters.py",
    3,
    "out",
    "star import of `attr.converters`, which does not export `instance_of`"
   ],
   [
    "src/attrs/exceptions.py",
    3,
    "out",
    "star import of `attr.exceptions`, which does not export `instance_of`"
   ],
   [
    "src/attrs/filters.py",
    3,
    "out",
    "star import of `attr.filters`, which does not export `instance_of`"
   ],
   [
    "src/attrs/setters.py",
    3,
    "out",
    "star import of `attr.setters`, which does not export `instance_of`"
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
    "tests/test_dunders.py",
    27,
    "in",
    "`attr.validators` resolves `instance_of` to the target"
   ],
   [
    "tests/test_funcs.py",
    22,
    "in",
    "`attr.validators` resolves `instance_of` to the target"
   ],
   [
    "tests/test_setattr.py",
    12,
    "in",
    "`attr.validators` resolves `instance_of` to the target"
   ],
   [
    "tests/test_validators.py",
    16,
    "in",
    "`attr.validators` resolves `instance_of` to the target"
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

The statement at `src/attr/__init__.py`:45 binds `__all__`.

Candidate modules so far: 10; statements confirmed: 4, ruled out: 4, modules with no such import: 0, pending: 2. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/setters.py`:3, star import of `attr.setters`, which does not export `instance_of`.

Still to settle: know what `src/attr/validators.py` exports; know what `src/attr/__init__.py` exports.

Next: read `src/attr/validators.py` from line 19, because `__all__` of `src/attr/validators.py` starts at line 19 (outline header). I expect: the whole list fits the window (about 90%); the list runs past the window (about 10%). The alternative, read `src/attr/__init__.py` from line 45, scores the same; the seed broke the tie. Plan by outcome: fits: read `src/attr/__init__.py` from line 45; long: read `src/attr/__init__.py` from line 45.

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
   "kind": "all",
   "key": [
    "all",
    "src/attr/__init__.py"
   ],
   "desc": "know what `src/attr/__init__.py` exports"
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
  "call": "read('src/attr/validators.py', 19, 30)",
  "key": "[\"read\", [\"src/attr/validators.py\", 19, 30]]",
  "provenance": "`__all__` of `src/attr/validators.py` starts at line 19 (outline header)",
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
  "fits": "[\"read\", [\"src/attr/__init__.py\", 45, 60]]",
  "long": "[\"read\", [\"src/attr/__init__.py\", 45, 60]]"
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
    "src/attrs/converters.py",
    3,
    "out",
    "star import of `attr.converters`, which does not export `instance_of`"
   ],
   [
    "src/attrs/exceptions.py",
    3,
    "out",
    "star import of `attr.exceptions`, which does not export `instance_of`"
   ],
   [
    "src/attrs/filters.py",
    3,
    "out",
    "star import of `attr.filters`, which does not export `instance_of`"
   ],
   [
    "src/attrs/setters.py",
    3,
    "out",
    "star import of `attr.setters`, which does not export `instance_of`"
   ],
   [
    "src/attrs/validators.py",
    3,
    "in",
    "star import of `attr.validators`, which exports `instance_of` from the target"
   ],
   [
    "tests/attr_import_star.py",
    4,
    "pending",
    ""
   ],
   [
    "tests/test_dunders.py",
    27,
    "in",
    "`attr.validators` resolves `instance_of` to the target"
   ],
   [
    "tests/test_funcs.py",
    22,
    "in",
    "`attr.validators` resolves `instance_of` to the target"
   ],
   [
    "tests/test_setattr.py",
    12,
    "in",
    "`attr.validators` resolves `instance_of` to the target"
   ],
   [
    "tests/test_validators.py",
    16,
    "in",
    "`attr.validators` resolves `instance_of` to the target"
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

The statement at `src/attr/validators.py`:19 binds `__all__`. `__all__` in `src/attr/validators.py` lists 20 names, and it names `instance_of`.

Candidate modules so far: 10; statements confirmed: 5, ruled out: 4, modules with no such import: 0, pending: 1. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/setters.py`:3, star import of `attr.setters`, which does not export `instance_of`.

Still to settle: know what `src/attr/__init__.py` exports.

Next: read `src/attr/__init__.py` from line 45, because `__all__` of `src/attr/__init__.py` starts at line 45 (outline header). I expect: the whole list fits the window (about 90%); the list runs past the window (about 10%). Plan by outcome: fits: done; long: work the items it opens.

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
    "src/attr/__init__.py"
   ],
   "desc": "know what `src/attr/__init__.py` exports"
  }
 ],
 "candidates": [
  {
   "call": "read('src/attr/__init__.py', 45, 60)",
   "key": "[\"read\", [\"src/attr/__init__.py\", 45, 60]]",
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
     "src/attr/__init__.py"
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
 "adherence": {
  "planned": "[\"read\", [\"src/attr/__init__.py\", 45, 60]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "read",
   "step": 25,
   "path": "src/attr/__init__.py",
   "start": 45,
   "count": 60,
   "n": 60
  },
  {
   "kind": "all_names",
   "step": 25,
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
    "src/attrs/converters.py",
    3,
    "out",
    "star import of `attr.converters`, which does not export `instance_of`"
   ],
   [
    "src/attrs/exceptions.py",
    3,
    "out",
    "star import of `attr.exceptions`, which does not export `instance_of`"
   ],
   [
    "src/attrs/filters.py",
    3,
    "out",
    "star import of `attr.filters`, which does not export `instance_of`"
   ],
   [
    "src/attrs/setters.py",
    3,
    "out",
    "star import of `attr.setters`, which does not export `instance_of`"
   ],
   [
    "src/attrs/validators.py",
    3,
    "in",
    "star import of `attr.validators`, which exports `instance_of` from the target"
   ],
   [
    "tests/attr_import_star.py",
    4,
    "out",
    "star import of `attr`, which does not export `instance_of`"
   ],
   [
    "tests/test_dunders.py",
    27,
    "in",
    "`attr.validators` resolves `instance_of` to the target"
   ],
   [
    "tests/test_funcs.py",
    22,
    "in",
    "`attr.validators` resolves `instance_of` to the target"
   ],
   [
    "tests/test_setattr.py",
    12,
    "in",
    "`attr.validators` resolves `instance_of` to the target"
   ],
   [
    "tests/test_validators.py",
    16,
    "in",
    "`attr.validators` resolves `instance_of` to the target"
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

Certificate complete. 5 import statements import this definition: `src/attrs/validators.py:3`, `tests/test_dunders.py:27`, `tests/test_funcs.py:22`, `tests/test_setattr.py:12`, `tests/test_validators.py:16`. In hindsight, 2 of 25 calls were not needed for the certificate: steps 1, 23.

**Answer:** `{"target": {"kind": "def", "path": "src/attr/validators.py", "line": 114, "name": "instance_of", "detail": "def"}, "text": "src/attr/validators.py:114", "statements": ["src/attrs/validators.py:3", "tests/test_dunders.py:27", "tests/test_funcs.py:22", "tests/test_setattr.py:12", "tests/test_validators.py:16"], "count": 5}`  
**Stopped:** certificate after 25 calls