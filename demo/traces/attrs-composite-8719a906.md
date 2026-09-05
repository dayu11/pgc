# attrs-composite-8719a906

**Repository:** attrs  
**Family:** composite  
**Seed:** 0, prior df2023878106d754

## Task

In `tests/test_converters.py`, line 15 imports `pipe` from `attr.converters`. Under the declared semantics, which definition does the module-level name `pipe` bound by this statement resolve to? Answer with `path:line`. Then list every module-level import statement in the snapshot that imports that definition (from-imports naming it, directly or with `as`, and star imports of modules that export it), as `path:line` entries.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

Nothing seen yet beyond the task text.

Chain: `tests/test_converters.py` is not yet closed for `pipe`.

Outstanding: close the namespace of `tests/test_converters.py` for `pipe`.

Next: outline `tests/test_converters.py`, because module `tests/test_converters.py` (task). I expect: a definition there ends the chain (about 80%); a capped outline means filtering by name (about 15%); a re-export continues the chain to its source (under 5%); no binding at all points at a submodule or an unresolved name (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `tests/test_converters.py` filtered to `pipe`, is expected to open more follow-up work. Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done; cap: outline `tests/test_converters.py` filtered to `pipe`.

**Call:** `symbols('tests/test_converters.py')`

**Response**: outcome `def`

```
module tests/test_converters.py lines=367 dynamic=no all=none
7 import pickle <- pickle
9 import pytest <- pytest
11 import attr <- attr
13 from Converter <- attr Converter
13 from Factory <- attr Factory
13 from attrib <- attr attrib
14 from _AnnotationExtractor <- attr._compat _AnnotationExtractor
15 from default_if_none <- attr.converters default_if_none
15 from optional <- attr.converters optional
15 from pipe <- attr.converters pipe
15 from to_bool <- attr.converters to_bool
18 class TestConverter
135 class TestOptional
174 class TestDefaultIfNone
230 class TestPipe
302 class TestOptionalPipe
344 class TestToBool
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "tests/test_converters.py",
    "pipe"
   ],
   "desc": "close the namespace of `tests/test_converters.py` for `pipe`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/test_converters.py')",
   "key": "[\"symbols\", [\"tests/test_converters.py\"]]",
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
     "tests/test_converters.py",
     "pipe"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_converters.py', 'pipe')",
   "key": "[\"symbols\", [\"tests/test_converters.py\", \"pipe\"]]",
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
     "tests/test_converters.py",
     "pipe"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_converters.py')",
  "key": "[\"symbols\", [\"tests/test_converters.py\"]]",
  "provenance": "module `tests/test_converters.py` (task)",
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
  "cap": "[\"symbols\", [\"tests/test_converters.py\", \"pipe\"]]"
 },
 "adherence": null,
 "facts": [
  {
   "kind": "outline",
   "step": 1,
   "path": "tests/test_converters.py",
   "filter": null,
   "header": {
    "lines": 367,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_converters.py",
     "name": "pickle",
     "line": 7,
     "kind": "import",
     "src": "pickle",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_converters.py",
     "name": "pytest",
     "line": 9,
     "kind": "import",
     "src": "pytest",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_converters.py",
     "name": "attr",
     "line": 11,
     "kind": "import",
     "src": "attr",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_converters.py",
     "name": "Converter",
     "line": 13,
     "kind": "from",
     "src": "attr",
     "src_name": "Converter",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_converters.py",
     "name": "Factory",
     "line": 13,
     "kind": "from",
     "src": "attr",
     "src_name": "Factory",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_converters.py",
     "name": "attrib",
     "line": 13,
     "kind": "from",
     "src": "attr",
     "src_name": "attrib",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_converters.py",
     "name": "_AnnotationExtractor",
     "line": 14,
     "kind": "from",
     "src": "attr._compat",
     "src_name": "_AnnotationExtractor",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_converters.py",
     "name": "default_if_none",
     "line": 15,
     "kind": "from",
     "src": "attr.converters",
     "src_name": "default_if_none",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_converters.py",
     "name": "optional",
     "line": 15,
     "kind": "from",
     "src": "attr.converters",
     "src_name": "optional",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_converters.py",
     "name": "pipe",
     "line": 15,
     "kind": "from",
     "src": "attr.converters",
     "src_name": "pipe",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_converters.py",
     "name": "to_bool",
     "line": 15,
     "kind": "from",
     "src": "attr.converters",
     "src_name": "to_bool",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_converters.py",
     "name": "TestConverter",
     "line": 18,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_converters.py",
     "name": "TestOptional",
     "line": 135,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_converters.py",
     "name": "TestDefaultIfNone",
     "line": 174,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_converters.py",
     "name": "TestPipe",
     "line": 230,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_converters.py",
     "name": "TestOptionalPipe",
     "line": 302,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_converters.py",
     "name": "TestToBool",
     "line": 344,
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
    "tests/test_converters.py",
    "pipe",
    "reexport",
    [
     "attr.converters",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 2

The outline of `tests/test_converters.py` has 17 bindings; no `__all__`; no dynamic namespace tricks. This is not the branch I planned for that outcome; the open items changed more than expected.

Chain: `tests/test_converters.py` takes `pipe` from `attr.converters` (module not yet located).

Still to settle: locate the module `attr.converters` imported by `tests/test_converters.py`.

Next: grep `def`/`class pipe` statements under `.`, because a `def`/`class pipe` statement would reveal the module file; `pipe` task. I expect: hits under the cap (about 90%); a capped result (about 5%); no hits (about 5%). The alternative, list `.`, is more likely to hit the cap (about 20% against about 5%). Plan by outcome: zero: list `.`; mid: outline each module that appears; cap: list `.`.

**Call:** `grep('^\\s*(?:async\\s+)?(?:def|class)\\s+pipe\\b', '.')`

**Response**: outcome `mid`

```
src/attr/_make.py:3404:def pipe(*converters):
src/attr/converters.pyi:6:def pipe(*validators: _CallableConverterType) -> _CallableConverterType: ...
src/attr/converters.pyi:8:def pipe(*validators: _ConverterType) -> _ConverterType: ...
src/attr/setters.py:11:def pipe(*setters):
src/attr/setters.pyi:11:def pipe(*setters: _OnSetAttrType) -> _OnSetAttrType: ...
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_converters.py",
    "attr.converters"
   ],
   "desc": "locate the module `attr.converters` imported by `tests/test_converters.py`"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+pipe\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+pipe\\\\b\", \".\"]]",
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
     "tests/test_converters.py",
     "attr.converters"
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
     "tests/test_converters.py",
     "attr.converters"
    ]
   ]
  },
  {
   "call": "symbols('attr/converters.py', 'pipe')",
   "key": "[\"symbols\", [\"attr/converters.py\", \"pipe\"]]",
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
     "tests/test_converters.py",
     "attr.converters"
    ]
   ]
  },
  {
   "call": "symbols('attr/converters/__init__.py', 'pipe')",
   "key": "[\"symbols\", [\"attr/converters/__init__.py\", \"pipe\"]]",
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
     "tests/test_converters.py",
     "attr.converters"
    ]
   ]
  }
 ],
 "choice": {
  "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+pipe\\\\b', '.')",
  "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+pipe\\\\b\", \".\"]]",
  "provenance": "a `def`/`class pipe` statement would reveal the module file; `pipe` task",
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
  "planned": "done",
  "status": "deviated"
 },
 "facts": [
  {
   "kind": "grep",
   "step": 2,
   "pattern": "^\\s*(?:async\\s+)?(?:def|class)\\s+pipe\\b",
   "scope": ".",
   "hits": [
    [
     "src/attr/_make.py",
     3404
    ],
    [
     "src/attr/converters.pyi",
     6
    ],
    [
     "src/attr/converters.pyi",
     8
    ],
    [
     "src/attr/setters.py",
     11
    ],
    [
     "src/attr/setters.pyi",
     11
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "chain": [
   [
    "tests/test_converters.py",
    "pipe",
    "reexport",
    [
     "attr.converters",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 3

The grep under `.` returned 5 lines, under the cap, so these are all of them: `src/attr/_make.py`, `src/attr/converters.pyi`, `src/attr/setters.py`, `src/attr/setters.pyi`.

Chain: `tests/test_converters.py` takes `pipe` from `attr.converters` (module not yet located).

Outstanding: locate the module `attr.converters` imported by `tests/test_converters.py`.

Next: list `.`, because `attr.converters` imported by `tests/test_converters.py` should live under `.`. I expect: a complete listing settles which files exist (about 80%); a capped listing settles nothing (about 20%). The alternative, outline `attr/converters.py` filtered to `pipe`, costs more in expectation. Plan by outcome: complete: outline the module it reveals; cap: outline `attr/converters.py` filtered to `pipe`.

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
    "tests/test_converters.py",
    "attr.converters"
   ],
   "desc": "locate the module `attr.converters` imported by `tests/test_converters.py`"
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
     "tests/test_converters.py",
     "attr.converters"
    ]
   ]
  },
  {
   "call": "symbols('attr/converters.py', 'pipe')",
   "key": "[\"symbols\", [\"attr/converters.py\", \"pipe\"]]",
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
     "tests/test_converters.py",
     "attr.converters"
    ]
   ]
  },
  {
   "call": "symbols('attr/converters/__init__.py', 'pipe')",
   "key": "[\"symbols\", [\"attr/converters/__init__.py\", \"pipe\"]]",
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
     "tests/test_converters.py",
     "attr.converters"
    ]
   ]
  }
 ],
 "choice": {
  "call": "ls('.')",
  "key": "[\"ls\", [\".\"]]",
  "provenance": "`attr.converters` imported by `tests/test_converters.py` should live under `.`",
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
  "cap": "[\"symbols\", [\"attr/converters.py\", \"pipe\"]]"
 },
 "adherence": {
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "listing",
   "step": 3,
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
    "tests/test_converters.py",
    "pipe",
    "reexport",
    [
     "attr.converters",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 4

`.` lists 15 entries (complete): `.github/`, `bench/`, `changelog.d/`, `docs/`, `src/`, `tests/` and 1 more.

Chain: `tests/test_converters.py` takes `pipe` from `attr.converters` (module not yet located).

Outstanding: locate the module `attr.converters` imported by `tests/test_converters.py`.

Next: outline `src/attr/converters.py` filtered to `pipe`, because `attr.converters` would be `src/attr/converters.py` if that file exists; one call both checks and closes it. I expect: a definition there ends the chain (about 85%); the file does not exist (about 10%); a re-export continues the chain to its source (under 5%); no binding at all points at a submodule or an unresolved name (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, list `src/attr`, is expected to open more follow-up work. Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done; missing: list `src/attr`.

**Call:** `symbols('src/attr/converters.py', 'pipe')`

**Response**: outcome `reexport`

```
module src/attr/converters.py lines=161 dynamic=no all=static@11
8 from pipe <- ._make pipe
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_converters.py",
    "attr.converters"
   ],
   "desc": "locate the module `attr.converters` imported by `tests/test_converters.py`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/converters.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attr/converters.py\", \"pipe\"]]",
   "v1": [
    36712633883,
    29198892320
   ],
   "v2": [
    8201236043489,
    6511352987360
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
     "tests/test_converters.py",
     "attr.converters"
    ]
   ]
  },
  {
   "call": "ls('src/attr')",
   "key": "[\"ls\", [\"src/attr\"]]",
   "v1": [
    106401,
    51067
   ],
   "v2": [
    2689884647739,
    1302270597472
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
     "tests/test_converters.py",
     "attr.converters"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/converters/__init__.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attr/converters/__init__.py\", \"pipe\"]]",
   "v1": [
    179061797,
    60016320
   ],
   "v2": [
    2160458417195501,
    956555712403200
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
     "tests/test_converters.py",
     "attr.converters"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/attr/converters.py', 'pipe')",
  "key": "[\"symbols\", [\"src/attr/converters.py\", \"pipe\"]]",
  "provenance": "`attr.converters` would be `src/attr/converters.py` if that file exists; one call both checks and closes it",
  "v2": [
   8201236043489,
   6511352987360
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
  "def": "done",
  "reexport": "continue",
  "star": "continue",
  "none": "done",
  "missing": "[\"ls\", [\"src/attr\"]]"
 },
 "adherence": {
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 4,
   "path": "src/attr/converters.py",
   "filter": "pipe",
   "header": {
    "lines": 161,
    "dynamic": false,
    "all_status": "static",
    "all_line": 11
   },
   "bindings": [
    {
     "module": "src/attr/converters.py",
     "name": "pipe",
     "line": 8,
     "kind": "from",
     "src": "._make",
     "src_name": "pipe",
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
    "tests/test_converters.py",
    "pipe",
    "reexport",
    [
     "attr.converters",
     "src/attr/converters.py"
    ]
   ],
   [
    "src/attr/converters.py",
    "pipe",
    "reexport",
    [
     "._make",
     "src/attr/_make.py"
    ]
   ],
   [
    "src/attr/_make.py",
    "pipe",
    "open",
    null
   ]
  ]
 }
}
```
</details>

## Step 5

In `src/attr/converters.py`, `pipe` has exactly one binding: line 8 imports it as `pipe` from `._make`. No dynamic namespace tricks, a literal `__all__` at line 11.

Chain: `tests/test_converters.py` takes `pipe` from `attr.converters` (`src/attr/converters.py`); `src/attr/converters.py` takes `pipe` from `._make` (`src/attr/_make.py`); `src/attr/_make.py` is not yet closed for `pipe`.

Still to settle: close the namespace of `src/attr/_make.py` for `pipe`.

Next: outline `src/attr/_make.py` filtered to `pipe`, because module `src/attr/_make.py` (step 2), name `pipe` (task). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `src/attr/_make.py`, is more likely to hit the cap (about 15% against under 5%). Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done.

**Call:** `symbols('src/attr/_make.py', 'pipe')`

**Response**: outcome `def`

```
module src/attr/_make.py lines=3463 dynamic=no all=none
3404 def pipe
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
    "pipe"
   ],
   "desc": "close the namespace of `src/attr/_make.py` for `pipe`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/_make.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attr/_make.py\", \"pipe\"]]",
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
     "src/attr/_make.py",
     "pipe"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/_make.py')",
   "key": "[\"symbols\", [\"src/attr/_make.py\"]]",
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
     "src/attr/_make.py",
     "pipe"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/attr/_make.py', 'pipe')",
  "key": "[\"symbols\", [\"src/attr/_make.py\", \"pipe\"]]",
  "provenance": "module `src/attr/_make.py` (step 2), name `pipe` (task)",
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
   "path": "src/attr/_make.py",
   "filter": "pipe",
   "header": {
    "lines": 3463,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/attr/_make.py",
     "name": "pipe",
     "line": 3404,
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
    "tests/test_converters.py",
    "pipe",
    "reexport",
    [
     "attr.converters",
     "src/attr/converters.py"
    ]
   ],
   [
    "src/attr/converters.py",
    "pipe",
    "reexport",
    [
     "._make",
     "src/attr/_make.py"
    ]
   ],
   [
    "src/attr/_make.py",
    "pipe",
    "def",
    3404
   ]
  ]
 }
}
```
</details>

## Step 6

In `src/attr/_make.py`, `pipe` has exactly one binding: a def at line 3404. No dynamic namespace tricks, no `__all__`. This is not the branch I planned for that outcome; the open items changed more than expected.

Candidate modules so far: 0; statements confirmed: 0, ruled out: 0, modules with no such import: 0, pending: 0. import coverage open at `.`; star coverage open at `.`.

Open: cover `.` for import lines; cover `.` for star lines.

Next: grep from-imports naming `pipe` or star imports under `.`, because import and star lines under `.` in one call. I expect: hits under the cap (about 45%); no hits (about 45%); a capped result (about 10%). The alternative, grep from-imports naming `pipe` under `.`, serves fewer of the open items. Plan by outcome: zero: done; mid: outline each module that appears; cap: list the scope and split it.

**Call:** `grep('^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bpipe\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*pipe\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$', '.')`

**Response**: outcome `mid`

```
src/attr/converters.py:8:from ._make import NOTHING, Converter, Factory, pipe
src/attrs/converters.py:3:from attr.converters import *  # noqa: F403
src/attrs/exceptions.py:3:from attr.exceptions import *  # noqa: F403
src/attrs/filters.py:3:from attr.filters import *  # noqa: F403
src/attrs/setters.py:3:from attr.setters import *  # noqa: F403
src/attrs/validators.py:3:from attr.validators import *  # noqa: F403
tests/attr_import_star.py:4:from attr import *  # noqa: F403
tests/test_converters.py:15:from attr.converters import default_if_none, optional, pipe, to_bool
tests/test_mypy.yml:1384:            from other import *
tests/test_next_gen.py:567:        from attrs.setters import pipe
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
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bpipe\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*pipe\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bpipe\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*pipe\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
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
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bpipe\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*pipe\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bpipe\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*pipe\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
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
  "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bpipe\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*pipe\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
  "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bpipe\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*pipe\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
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
   "pattern": "^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bpipe\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*pipe\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$",
   "scope": ".",
   "hits": [
    [
     "src/attr/converters.py",
     8
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
     "tests/test_converters.py",
     15
    ],
    [
     "tests/test_mypy.yml",
     1384
    ],
    [
     "tests/test_next_gen.py",
     567
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "src/attr/converters.py",
    8,
    "in",
    "`._make` resolves `pipe` to the target"
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
    "tests/test_converters.py",
    15,
    "in",
    "`attr.converters` resolves `pipe` to the target"
   ],
   [
    "tests/test_next_gen.py",
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

The grep under `.` returned 10 lines, under the cap, so these are all of them: `src/attr/converters.py`, `src/attrs/converters.py`, `src/attrs/exceptions.py`, `src/attrs/filters.py` and 6 more files.

Candidate modules so far: 9; statements confirmed: 2, ruled out: 0, modules with no such import: 0, pending: 7. import coverage complete; star coverage complete.

Open: outline `src/attrs/converters.py` for its `pipe` imports; outline `src/attrs/exceptions.py` for its `pipe` imports; outline `src/attrs/filters.py` for its `pipe` imports; outline `src/attrs/setters.py` for its `pipe` imports; and 3 more.

Next: outline `tests/test_next_gen.py` filtered to `pipe`, because `tests/test_next_gen.py` had a matching line (step 6); its outline names every `pipe` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/attrs/converters.py` filtered to `pipe`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/attrs/converters.py` filtered to `pipe`; cap: outline `src/attrs/converters.py` filtered to `pipe`.

**Call:** `symbols('tests/test_next_gen.py', 'pipe')`

**Response**: outcome `ok`

```
module tests/test_next_gen.py lines=586 dynamic=no all=none
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
    "pipe"
   ],
   "desc": "outline `src/attrs/converters.py` for its `pipe` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/exceptions.py",
    "pipe"
   ],
   "desc": "outline `src/attrs/exceptions.py` for its `pipe` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "pipe"
   ],
   "desc": "outline `src/attrs/filters.py` for its `pipe` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "pipe"
   ],
   "desc": "outline `src/attrs/setters.py` for its `pipe` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "pipe"
   ],
   "desc": "outline `src/attrs/validators.py` for its `pipe` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "pipe"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `pipe` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_next_gen.py",
    "pipe"
   ],
   "desc": "outline `tests/test_next_gen.py` for its `pipe` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attrs/converters.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attrs/converters.py\", \"pipe\"]]",
   "v1": [
    9488741,
    904550
   ],
   "v2": [
    4753416,
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
     "pipe"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/exceptions.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attrs/exceptions.py\", \"pipe\"]]",
   "v1": [
    9488741,
    904550
   ],
   "v2": [
    4753416,
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
     "pipe"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/filters.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"pipe\"]]",
   "v1": [
    9488741,
    904550
   ],
   "v2": [
    4753416,
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
     "pipe"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"pipe\"]]",
   "v1": [
    9488741,
    904550
   ],
   "v2": [
    4753416,
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
     "pipe"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"pipe\"]]",
   "v1": [
    9488741,
    904550
   ],
   "v2": [
    4753416,
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
     "pipe"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'pipe')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"pipe\"]]",
   "v1": [
    9488741,
    904550
   ],
   "v2": [
    4753416,
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
     "pipe"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_next_gen.py', 'pipe')",
   "key": "[\"symbols\", [\"tests/test_next_gen.py\", \"pipe\"]]",
   "v1": [
    9488741,
    904550
   ],
   "v2": [
    4753416,
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
     "tests/test_next_gen.py",
     "pipe"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_next_gen.py', 'pipe')",
  "key": "[\"symbols\", [\"tests/test_next_gen.py\", \"pipe\"]]",
  "provenance": "`tests/test_next_gen.py` had a matching line (step 6); its outline names every `pipe` import exactly",
  "v2": [
   4753416,
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
  "ok": "[\"symbols\", [\"src/attrs/converters.py\", \"pipe\"]]",
  "cap": "[\"symbols\", [\"src/attrs/converters.py\", \"pipe\"]]"
 },
 "adherence": {
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 7,
   "path": "tests/test_next_gen.py",
   "filter": "pipe",
   "header": {
    "lines": 586,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [],
   "complete": true
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "src/attr/converters.py",
    8,
    "in",
    "`._make` resolves `pipe` to the target"
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
    "tests/test_converters.py",
    15,
    "in",
    "`attr.converters` resolves `pipe` to the target"
   ],
   [
    "tests/test_next_gen.py",
    0,
    "none",
    "no
```
</details>

## Step 8

`tests/test_next_gen.py` binds no `pipe` at module level; no star imports; no `__all__`; no dynamic namespace tricks.

Candidate modules so far: 9; statements confirmed: 2, ruled out: 0, modules with no such import: 1, pending: 6. import coverage complete; star coverage complete.

Outstanding: outline `src/attrs/converters.py` for its `pipe` imports; outline `src/attrs/exceptions.py` for its `pipe` imports; outline `src/attrs/filters.py` for its `pipe` imports; outline `src/attrs/setters.py` for its `pipe` imports; and 2 more.

Next: outline `src/attrs/converters.py` filtered to `pipe`, because `src/attrs/converters.py` had a matching line (step 6); its outline names every `pipe` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/attrs/exceptions.py` filtered to `pipe`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/attrs/exceptions.py` filtered to `pipe`; cap: outline `src/attrs/exceptions.py` filtered to `pipe`.

**Call:** `symbols('src/attrs/converters.py', 'pipe')`

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
    "pipe"
   ],
   "desc": "outline `src/attrs/converters.py` for its `pipe` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/exceptions.py",
    "pipe"
   ],
   "desc": "outline `src/attrs/exceptions.py` for its `pipe` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "pipe"
   ],
   "desc": "outline `src/attrs/filters.py` for its `pipe` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "pipe"
   ],
   "desc": "outline `src/attrs/setters.py` for its `pipe` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "pipe"
   ],
   "desc": "outline `src/attrs/validators.py` for its `pipe` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "pipe"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `pipe` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attrs/converters.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attrs/converters.py\", \"pipe\"]]",
   "v1": [
    8135791,
    904550
   ],
   "v2": [
    4076941,
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
     "pipe"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/exceptions.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attrs/exceptions.py\", \"pipe\"]]",
   "v1": [
    8135791,
    904550
   ],
   "v2": [
    4076941,
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
     "pipe"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/filters.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"pipe\"]]",
   "v1": [
    8135791,
    904550
   ],
   "v2": [
    4076941,
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
     "pipe"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"pipe\"]]",
   "v1": [
    8135791,
    904550
   ],
   "v2": [
    4076941,
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
     "pipe"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"pipe\"]]",
   "v1": [
    8135791,
    904550
   ],
   "v2": [
    4076941,
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
     "pipe"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'pipe')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"pipe\"]]",
   "v1": [
    8135791,
    904550
   ],
   "v2": [
    4076941,
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
     "pipe"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/attrs/converters.py', 'pipe')",
  "key": "[\"symbols\", [\"src/attrs/converters.py\", \"pipe\"]]",
  "provenance": "`src/attrs/converters.py` had a matching line (step 6); its outline names every `pipe` import exactly",
  "v2": [
   4076941,
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
  "ok": "[\"symbols\", [\"src/attrs/exceptions.py\", \"pipe\"]]",
  "cap": "[\"symbols\", [\"src/attrs/exceptions.py\", \"pipe\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"src/attrs/converters.py\", \"pipe\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 8,
   "path": "src/attrs/converters.py",
   "filter": "pipe",
   "header": {
    "lines": 4,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/attrs/converters.py",
     "name": "*",
     "line": 3,
     "kind": "star",
     "src": "attr.converters",
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
    "src/attr/converters.py",
    8,
    "in",
    "`._make` resolves `pipe` to the target"
   ],
   [
    "src/attrs/converters.py",
    3,
    "pending",
    ""
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
    "tests/test_converters.py",
    15,
    "in",
    "`attr.converters` resolves `pipe` to the target"
   ],
   [
    "tests/test_next_gen.py",
    0,
    "none",
    "no import of the name in this module"
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

## Step 9

`src/attrs/converters.py` binds no `pipe` at module level; 1 star import(s): `attr.converters`; no `__all__`; no dynamic namespace tricks.

Candidate modules so far: 9; statements confirmed: 2, ruled out: 0, modules with no such import: 1, pending: 6. import coverage complete; star coverage complete.

Still to settle: know what `src/attr/converters.py` exports; outline `src/attrs/exceptions.py` for its `pipe` imports; outline `src/attrs/filters.py` for its `pipe` imports; outline `src/attrs/setters.py` for its `pipe` imports; and 2 more.

Next: outline `src/attrs/exceptions.py` filtered to `pipe`, because `src/attrs/exceptions.py` had a matching line (step 6); its outline names every `pipe` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/attrs/filters.py` filtered to `pipe`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/attrs/filters.py` filtered to `pipe`; cap: outline `src/attrs/filters.py` filtered to `pipe`.

**Call:** `symbols('src/attrs/exceptions.py', 'pipe')`

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
    "src/attrs/exceptions.py",
    "pipe"
   ],
   "desc": "outline `src/attrs/exceptions.py` for its `pipe` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/filters.py",
    "pipe"
   ],
   "desc": "outline `src/attrs/filters.py` for its `pipe` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "pipe"
   ],
   "desc": "outline `src/attrs/setters.py` for its `pipe` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "pipe"
   ],
   "desc": "outline `src/attrs/validators.py` for its `pipe` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "pipe"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `pipe` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attrs/exceptions.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attrs/exceptions.py\", \"pipe\"]]",
   "v1": [
    7687391,
    904550
   ],
   "v2": [
    3852741,
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
     "pipe"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/filters.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"pipe\"]]",
   "v1": [
    7687391,
    904550
   ],
   "v2": [
    3852741,
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
     "pipe"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"pipe\"]]",
   "v1": [
    7687391,
    904550
   ],
   "v2": [
    3852741,
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
     "pipe"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"pipe\"]]",
   "v1": [
    7687391,
    904550
   ],
   "v2": [
    3852741,
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
     "pipe"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'pipe')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"pipe\"]]",
   "v1": [
    7687391,
    904550
   ],
   "v2": [
    3852741,
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
     "pipe"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    4962625,
    578912
   ],
   "v2": [
    124355081,
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
  "call": "symbols('src/attrs/exceptions.py', 'pipe')",
  "key": "[\"symbols\", [\"src/attrs/exceptions.py\", \"pipe\"]]",
  "provenance": "`src/attrs/exceptions.py` had a matching line (step 6); its outline names every `pipe` import exactly",
  "v2": [
   3852741,
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
  "ok": "[\"symbols\", [\"src/attrs/filters.py\", \"pipe\"]]",
  "cap": "[\"symbols\", [\"src/attrs/filters.py\", \"pipe\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"src/attrs/exceptions.py\", \"pipe\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 9,
   "path": "src/attrs/exceptions.py",
   "filter": "pipe",
   "header": {
    "lines": 4,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/attrs/exceptions.py",
     "name": "*",
     "line": 3,
     "kind": "star",
     "src": "attr.exceptions",
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
    "src/attr/converters.py",
    8,
    "in",
    "`._make` resolves `pipe` to the target"
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
    "pending",
    ""
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
    "tests/test_converters.py",
    15,
    "in",
    "`attr.converters` resolves `pipe` to the target"
   ],
   [
    "tests/test_next_gen.py",
    0,
    "none",
    "no import of the name in this module"
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

## Step 10

`src/attrs/exceptions.py` binds no `pipe` at module level; 1 star import(s): `attr.exceptions`; no `__all__`; no dynamic namespace tricks.

Candidate modules so far: 9; statements confirmed: 2, ruled out: 0, modules with no such import: 1, pending: 6. import coverage complete; star coverage complete.

Still to settle: know what `src/attr/converters.py` exports; locate the module `attr.exceptions` imported by `src/attrs/exceptions.py`; outline `src/attrs/filters.py` for its `pipe` imports; outline `src/attrs/setters.py` for its `pipe` imports; and 2 more.

Next: outline `src/attrs/filters.py` filtered to `pipe`, because `src/attrs/filters.py` had a matching line (step 6); its outline names every `pipe` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/attr/exceptions.py` filtered to `pipe`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/attr/exceptions.py` filtered to `pipe`; cap: outline `src/attr/exceptions.py` filtered to `pipe`.

**Call:** `symbols('src/attrs/filters.py', 'pipe')`

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
    "pipe"
   ],
   "desc": "outline `src/attrs/filters.py` for its `pipe` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "pipe"
   ],
   "desc": "outline `src/attrs/setters.py` for its `pipe` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "pipe"
   ],
   "desc": "outline `src/attrs/validators.py` for its `pipe` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "pipe"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `pipe` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/exceptions.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attr/exceptions.py\", \"pipe\"]]",
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
     "src/attrs/exceptions.py",
     "attr.exceptions"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/filters.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attrs/filters.py\", \"pipe\"]]",
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
     "src/attrs/filters.py",
     "pipe"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"pipe\"]]",
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
     "src/attrs/setters.py",
     "pipe"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"pipe\"]]",
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
     "pipe"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'pipe')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"pipe\"]]",
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
     "pipe"
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
     "src/attrs/exceptions.py",
     "attr.exceptions"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/exceptions/__init__.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attr/exceptions/__init__.py\", \"pipe\"]]",
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
     "src/attrs/exceptions.py",
     "attr.exceptions"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/attrs/filters.py', 'pipe')",
  "key": "[\"symbols\", [\"src/attrs/filters.py\", \"pipe\"]]",
  "provenance": "`src/attrs/filters.py` had a matching line (step 6); its outline names every `pipe` import exactly",
  "v2": [
   95269464473913,
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
  "ok": "[\"symbols\", [\"src/attr/exceptions.py\", \"pipe\"]]",
  "cap": "[\"symbols\", [\"src/attr/exceptions.py\", \"pipe\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"src/attrs/filters.py\", \"pipe\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 10,
   "path": "src/attrs/filters.py",
   "filter": "pipe",
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
     "
```
</details>

## Step 11

`src/attrs/filters.py` binds no `pipe` at module level; 1 star import(s): `attr.filters`; no `__all__`; no dynamic namespace tricks.

Candidate modules so far: 9; statements confirmed: 2, ruled out: 0, modules with no such import: 1, pending: 6. import coverage complete; star coverage complete.

Outstanding: know what `src/attr/converters.py` exports; locate the module `attr.exceptions` imported by `src/attrs/exceptions.py`; locate the module `attr.filters` imported by `src/attrs/filters.py`; outline `src/attrs/setters.py` for its `pipe` imports; and 2 more.

Next: outline `src/attr/exceptions.py` filtered to `pipe`, because `attr.exceptions` would be `src/attr/exceptions.py` if that file exists; one call both checks and closes it. I expect: a definition there ends the chain (about 85%); the file does not exist (about 10%); a re-export continues the chain to its source (under 5%); no binding at all points at a submodule or an unresolved name (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `src/attr/filters.py` filtered to `pipe`, scores the same; the seed broke the tie. Plan by outcome: def: outline `src/attr/filters.py` filtered to `pipe`; reexport: outline `src/attr/filters.py` filtered to `pipe`; star: outline `src/attr/filters.py` filtered to `pipe`; none: outline `src/attr/filters.py` filtered to `pipe`; missing: list `src/attr`.

**Call:** `symbols('src/attr/exceptions.py', 'pipe')`

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
    "pipe"
   ],
   "desc": "outline `src/attrs/setters.py` for its `pipe` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "pipe"
   ],
   "desc": "outline `src/attrs/validators.py` for its `pipe` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "pipe"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `pipe` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/exceptions.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attr/exceptions.py\", \"pipe\"]]",
   "v1": [
    20312018337237,
    2306712493280
   ],
   "v2": [
    2136403985357745759,
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
   "call": "symbols('src/attr/filters.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attr/filters.py\", \"pipe\"]]",
   "v1": [
    20312018337237,
    2306712493280
   ],
   "v2": [
    2136403985357745759,
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
   "call": "ls('src/attr')",
   "key": "[\"ls\", [\"src/attr\"]]",
   "v1": [
    34913829,
    4034293
   ],
   "v2": [
    22262559984398029,
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
    ],
    [
     "module_path",
     "src/attrs/filters.py",
     "attr.filters"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/setters.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"pipe\"]]",
   "v1": [
    8710291,
    904550
   ],
   "v2": [
    1749725743,
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
     "pipe"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"pipe\"]]",
   "v1": [
    8710291,
    904550
   ],
   "v2": [
    1749725743,
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
     "pipe"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'pipe')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"pipe\"]]",
   "v1": [
    8710291,
    904550
   ],
   "v2": [
    1749725743,
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
     "pipe"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    5617281,
    578912
   ],
   "v2": [
    1129345407,
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
   "call": "symbols('src/attr/exceptions/__init__.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attr/exceptions/__init__.py\", \"pipe\"]]",
   "v1": [
    49934478443,
    4741289280
   ],
   "v2": [
    161632904094120965843,
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
     "src/attrs/exceptions.py",
     "attr.exceptions"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/filters/__init__.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attr/filters/__init__.py\", \"pipe\"]]",
   "v1": [
    49934478443,
    4741289280
   ],
   "v2": [
    161632904094120965843,
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
  }
 ],
 "choice": {
  "call": "symbols('src/attr/exceptions.py', 'pipe')",
  "key": "[\"symbols\", [\"src/attr/exceptions.py\", \"pipe\"]]"
```
</details>

## Step 12

`src/attr/exceptions.py` binds no `pipe` at module level; no star imports; no `__all__`; no dynamic namespace tricks.

Candidate modules so far: 9; statements confirmed: 2, ruled out: 1, modules with no such import: 1, pending: 5. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/exceptions.py`:3, star import of `attr.exceptions`, which does not export `pipe`.

Open: know what `src/attr/converters.py` exports; locate the module `attr.filters` imported by `src/attrs/filters.py`; outline `src/attrs/setters.py` for its `pipe` imports; outline `src/attrs/validators.py` for its `pipe` imports; and 1 more.

Next: outline `src/attr/filters.py` filtered to `pipe`, because `attr.filters` would be `src/attr/filters.py` if that file exists; one call both checks and closes it. I expect: a definition there ends the chain (about 85%); the file does not exist (about 10%); a re-export continues the chain to its source (under 5%); no binding at all points at a submodule or an unresolved name (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `src/attrs/setters.py` filtered to `pipe`, is expected to open more follow-up work. Plan by outcome: def: outline `src/attrs/setters.py` filtered to `pipe`; reexport: outline `src/attrs/setters.py` filtered to `pipe`; star: outline `src/attrs/setters.py` filtered to `pipe`; none: outline `src/attrs/setters.py` filtered to `pipe`; missing: outline `src/attrs/setters.py` filtered to `pipe`.

**Call:** `symbols('src/attr/filters.py', 'pipe')`

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
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "pipe"
   ],
   "desc": "outline `src/attrs/setters.py` for its `pipe` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "pipe"
   ],
   "desc": "outline `src/attrs/validators.py` for its `pipe` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "pipe"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `pipe` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/filters.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attr/filters.py\", \"pipe\"]]",
   "v1": [
    15557571626197,
    2306712493280
   ],
   "v2": [
    78018529380313,
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
   "call": "symbols('src/attrs/setters.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"pipe\"]]",
   "v1": [
    6845891,
    904550
   ],
   "v2": [
    78018529380313,
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
     "pipe"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"pipe\"]]",
   "v1": [
    6845891,
    904550
   ],
   "v2": [
    78018529380313,
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
     "pipe"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'pipe')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"pipe\"]]",
   "v1": [
    6845891,
    904550
   ],
   "v2": [
    78018529380313,
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
     "pipe"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    4424065,
    578912
   ],
   "v2": [
    7886912961221,
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
    30542443,
    4034293
   ],
   "v2": [
    19475668519263629,
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
   "call": "symbols('src/attr/filters/__init__.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attr/filters/__init__.py\", \"pipe\"]]",
   "v1": [
    40162039403,
    4741289280
   ],
   "v2": [
    2927383628914585759,
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
  "call": "symbols('src/attr/filters.py', 'pipe')",
  "key": "[\"symbols\", [\"src/attr/filters.py\", \"pipe\"]]",
  "provenance": "`attr.filters` would be `src/attr/filters.py` if that file exists; one call both checks and closes it",
  "v2": [
   78018529380313,
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
  "def": "[\"symbols\", [\"src/attrs/setters.py\", \"pipe\"]]",
  "reexport": "[\"symbols\", [\"src/attrs/setters.py\", \"pipe\"]]",
  "star": "[\"symbols\", [\"src/attrs/setters.py\", \"pipe\"]]",
  "none": "[\"symbols\", [\"src/attrs/setters.py\", \"pipe\"]]",
  "missing": "[\"symbols\", [\"src/attrs/setters.py\", \"pipe\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"src/attr/filters.py\", \"pipe\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 12,
   "path": "src/attr/filters.py",
   "filter": "pipe",
   "header": {
    "lines": 73,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [],
   "complete": true
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "src/attr/converters.py",
    8,
    "in",
    "`._make` resolves `pipe` to the target"
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
    "star import of `attr.exceptions`, which does not export `pipe`"
   ],
   [
    "src/attrs/filters.py",
    3,
    "out",
    "star import of `attr.filters`, which does not export `pipe`"
   ],
   [
```
</details>

## Step 13

`src/attr/filters.py` binds no `pipe` at module level; no star imports; no `__all__`; no dynamic namespace tricks.

Candidate modules so far: 9; statements confirmed: 2, ruled out: 2, modules with no such import: 1, pending: 4. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/filters.py`:3, star import of `attr.filters`, which does not export `pipe`.

Outstanding: know what `src/attr/converters.py` exports; outline `src/attrs/setters.py` for its `pipe` imports; outline `src/attrs/validators.py` for its `pipe` imports; outline `tests/attr_import_star.py` for its `pipe` imports.

Next: outline `src/attrs/setters.py` filtered to `pipe`, because `src/attrs/setters.py` had a matching line (step 6); its outline names every `pipe` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/attrs/validators.py` filtered to `pipe`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/attrs/validators.py` filtered to `pipe`; cap: outline `src/attrs/validators.py` filtered to `pipe`.

**Call:** `symbols('src/attrs/setters.py', 'pipe')`

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
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/setters.py",
    "pipe"
   ],
   "desc": "outline `src/attrs/setters.py` for its `pipe` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "pipe"
   ],
   "desc": "outline `src/attrs/validators.py` for its `pipe` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "pipe"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `pipe` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attrs/setters.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attrs/setters.py\", \"pipe\"]]",
   "v1": [
    4981491,
    904550
   ],
   "v2": [
    2499791,
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
     "pipe"
    ]
   ]
  },
  {
   "call": "symbols('src/attrs/validators.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"pipe\"]]",
   "v1": [
    4981491,
    904550
   ],
   "v2": [
    2499791,
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
     "pipe"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'pipe')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"pipe\"]]",
   "v1": [
    4981491,
    904550
   ],
   "v2": [
    2499791,
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
     "pipe"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    3230849,
    578912
   ],
   "v2": [
    81060681,
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
  "call": "symbols('src/attrs/setters.py', 'pipe')",
  "key": "[\"symbols\", [\"src/attrs/setters.py\", \"pipe\"]]",
  "provenance": "`src/attrs/setters.py` had a matching line (step 6); its outline names every `pipe` import exactly",
  "v2": [
   2499791,
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
  "ok": "[\"symbols\", [\"src/attrs/validators.py\", \"pipe\"]]",
  "cap": "[\"symbols\", [\"src/attrs/validators.py\", \"pipe\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"src/attrs/setters.py\", \"pipe\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 13,
   "path": "src/attrs/setters.py",
   "filter": "pipe",
   "header": {
    "lines": 4,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/attrs/setters.py",
     "name": "*",
     "line": 3,
     "kind": "star",
     "src": "attr.setters",
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
    "src/attr/converters.py",
    8,
    "in",
    "`._make` resolves `pipe` to the target"
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
    "star import of `attr.exceptions`, which does not export `pipe`"
   ],
   [
    "src/attrs/filters.py",
    3,
    "out",
    "star import of `attr.filters`, which does not export `pipe`"
   ],
   [
    "src/attrs/setters.py",
    3,
    "pending",
    ""
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
    "tests/test_converters.py",
    15,
    "in",
    "`attr.converters` resolves `pipe` to the target"
   ],
   [
    "tests/test_next_gen.py",
    0,
    "none",
    "no import of the name in this module"
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

## Step 14

`src/attrs/setters.py` binds no `pipe` at module level; 1 star import(s): `attr.setters`; no `__all__`; no dynamic namespace tricks.

Candidate modules so far: 9; statements confirmed: 2, ruled out: 2, modules with no such import: 1, pending: 4. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/filters.py`:3, star import of `attr.filters`, which does not export `pipe`.

Open: know what `src/attr/converters.py` exports; know what `src/attr/setters.py` exports; outline `src/attrs/validators.py` for its `pipe` imports; outline `tests/attr_import_star.py` for its `pipe` imports.

Next: outline `src/attrs/validators.py` filtered to `pipe`, because `src/attrs/validators.py` had a matching line (step 6); its outline names every `pipe` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `tests/attr_import_star.py` filtered to `pipe`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `tests/attr_import_star.py` filtered to `pipe`; cap: outline `tests/attr_import_star.py` filtered to `pipe`.

**Call:** `symbols('src/attrs/validators.py', 'pipe')`

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
   "kind": "all",
   "key": [
    "all",
    "src/attr/setters.py"
   ],
   "desc": "know what `src/attr/setters.py` exports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/attrs/validators.py",
    "pipe"
   ],
   "desc": "outline `src/attrs/validators.py` for its `pipe` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/attr_import_star.py",
    "pipe"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `pipe` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attrs/validators.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attrs/validators.py\", \"pipe\"]]",
   "v1": [
    4533091,
    904550
   ],
   "v2": [
    2275591,
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
     "pipe"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'pipe')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"pipe\"]]",
   "v1": [
    4533091,
    904550
   ],
   "v2": [
    2275591,
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
     "pipe"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/setters.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attr/setters.py\", \"pipe\"]]",
   "v1": [
    4749397349,
    939827450
   ],
   "v2": [
    2384096949,
    469913725
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
     "src/attr/setters.py"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    2943873,
    578912
   ],
   "v2": [
    73886281,
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
  "call": "symbols('src/attrs/validators.py', 'pipe')",
  "key": "[\"symbols\", [\"src/attrs/validators.py\", \"pipe\"]]",
  "provenance": "`src/attrs/validators.py` had a matching line (step 6); its outline names every `pipe` import exactly",
  "v2": [
   2275591,
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
  "ok": "[\"symbols\", [\"tests/attr_import_star.py\", \"pipe\"]]",
  "cap": "[\"symbols\", [\"tests/attr_import_star.py\", \"pipe\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"src/attrs/validators.py\", \"pipe\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 14,
   "path": "src/attrs/validators.py",
   "filter": "pipe",
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
    "src/attr/converters.py",
    8,
    "in",
    "`._make` resolves `pipe` to the target"
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
    "star import of `attr.exceptions`, which does not export `pipe`"
   ],
   [
    "src/attrs/filters.py",
    3,
    "out",
    "star import of `attr.filters`, which does not export `pipe`"
   ],
   [
    "src/attrs/setters.py",
    3,
    "pending",
    ""
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
    "tests/test_converters.py",
    15,
    "in",
    "`attr.converters` resolves `pipe` to the target"
   ],
   [
    "tests/test_next_gen.py",
    0,
    "none",
    "no import of the name in this module"
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

## Step 15

`src/attrs/validators.py` binds no `pipe` at module level; 1 star import(s): `attr.validators`; no `__all__`; no dynamic namespace tricks.

Candidate modules so far: 9; statements confirmed: 2, ruled out: 2, modules with no such import: 1, pending: 4. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/filters.py`:3, star import of `attr.filters`, which does not export `pipe`.

Still to settle: know what `src/attr/converters.py` exports; know what `src/attr/setters.py` exports; locate the module `attr.validators` imported by `src/attrs/validators.py`; outline `tests/attr_import_star.py` for its `pipe` imports.

Next: outline `tests/attr_import_star.py` filtered to `pipe`, because `tests/attr_import_star.py` had a matching line (step 6); its outline names every `pipe` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/attr/validators.py` filtered to `pipe`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/attr/validators.py` filtered to `pipe`; cap: outline `src/attr/validators.py` filtered to `pipe`.

**Call:** `symbols('tests/attr_import_star.py', 'pipe')`

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
    "src/attr/setters.py"
   ],
   "desc": "know what `src/attr/setters.py` exports"
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
    "pipe"
   ],
   "desc": "outline `tests/attr_import_star.py` for its `pipe` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/attr/validators.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attr/validators.py\", \"pipe\"]]",
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
     "src/attrs/validators.py",
     "attr.validators"
    ]
   ]
  },
  {
   "call": "symbols('tests/attr_import_star.py', 'pipe')",
   "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"pipe\"]]",
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
     "tests/attr_import_star.py",
     "pipe"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/setters.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attr/setters.py\", \"pipe\"]]",
   "v1": [
    5280793899,
    939827450
   ],
   "v2": [
    55535159557113,
    11533562466400
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
     "src/attr/setters.py"
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
   "call": "ls('src/attr')",
   "key": "[\"ls\", [\"src/attr\"]]",
   "v1": [
    22508422,
    4034293
   ],
   "v2": [
    14353735897525229,
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
     "src/attrs/validators.py",
     "attr.validators"
    ]
   ]
  },
  {
   "call": "symbols('src/attr/validators/__init__.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attr/validators/__init__.py\", \"pipe\"]]",
   "v1": [
    30720083243,
    4741289280
   ],
   "v2": [
    2174941867981177759,
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
     "src/attrs/validators.py",
     "attr.validators"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/attr_import_star.py', 'pipe')",
  "key": "[\"symbols\", [\"tests/attr_import_star.py\", \"pipe\"]]",
  "provenance": "`tests/attr_import_star.py` had a matching line (step 6); its outline names every `pipe` import exactly",
  "v2": [
   55050221659513,
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
  "ok": "[\"symbols\", [\"src/attr/validators.py\", \"pipe\"]]",
  "cap": "[\"symbols\", [\"src/attr/validators.py\", \"pipe\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"tests/attr_import_star.py\", \"pipe\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 15,
   "path": "tests/attr_import_star.py",
   "filter": "pipe",
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
    "src/attr/converters.py",
    8,
    "in",
    "`._make` resolves `pipe` to the target"
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
    "star import of `attr.exceptions`, which does not export `pipe`"
   ],
   [
    "src/attrs/filters.py",
    3,
    "out",
    "star import of `attr.filters`, which does not export `pipe`"
   ],
   [
    "src/attrs/setters.py",
    3,
    "pending",
    ""
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
    "tests/test_converters.py",
    15,
    "in",
    "`attr.converters` resolves `pipe` to the target"
   ],
   [
    "tests/test_next_gen.py",
    0,
    "none",
    "no import of the name in this module"
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

## Step 16

`tests/attr_import_star.py` binds no `pipe` at module level; 1 star import(s): `attr`; no `__all__`; no dynamic namespace tricks.

Candidate modules so far: 9; statements confirmed: 2, ruled out: 2, modules with no such import: 1, pending: 4. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/filters.py`:3, star import of `attr.filters`, which does not export `pipe`.

Outstanding: know what `src/attr/converters.py` exports; know what `src/attr/setters.py` exports; locate the module `attr.validators` imported by `src/attrs/validators.py`; locate the module `attr` imported by `tests/attr_import_star.py`.

Next: outline `src/attr/validators.py` filtered to `pipe`, because `attr.validators` would be `src/attr/validators.py` if that file exists; one call both checks and closes it. I expect: a definition there ends the chain (about 85%); the file does not exist (about 10%); a re-export continues the chain to its source (under 5%); no binding at all points at a submodule or an unresolved name (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `src/attr.py` filtered to `pipe`, scores the same; the seed broke the tie. Plan by outcome: def: outline `src/attr.py` filtered to `pipe`; reexport: outline `src/attr.py` filtered to `pipe`; star: outline `src/attr.py` filtered to `pipe`; none: outline `src/attr.py` filtered to `pipe`; missing: outline `src/attr.py` filtered to `pipe`.

**Call:** `symbols('src/attr/validators.py', 'pipe')`

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
   "desc": "know what `src/attr/converters.py` exports"
  },
  {
   "kind": "all",
   "key": [
    "all",
    "src/attr/setters.py"
   ],
   "desc": "know what `src/attr/setters.py` exports"
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
   "call": "symbols('src/attr.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attr.py\", \"pipe\"]]",
   "v1": [
    155293288283,
    29198892320
   ],
   "v2": [
    65911526203,
    14599446160
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
   "call": "symbols('src/attr/validators.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attr/validators.py\", \"pipe\"]]",
   "v1": [
    155293288283,
    29198892320
   ],
   "v2": [
    65911526203,
    14599446160
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
   "call": "ls('src/attr')",
   "key": "[\"ls\", [\"src/attr\"]]",
   "v1": [
    313791,
    51067
   ],
   "v2": [
    34776397748709,
    6511352987360
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
   "call": "symbols('src/attr/setters.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attr/setters.py\", \"pipe\"]]",
   "v1": [
    73572031,
    11896550
   ],
   "v2": [
    785524785047,
    145994461600
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
     "src/attr/setters.py"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    45551,
    7328
   ],
   "v2": [
    79015342219,
    14599446160
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
   "call": "ls('src')",
   "key": "[\"ls\", [\"src\"]]",
   "v1": [
    74049,
    11908
   ],
   "v2": [
    158100874083,
    29198892320
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
   "call": "symbols('src/attr/__init__.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attr/__init__.py\", \"pipe\"]]",
   "v1": [
    15697507,
    2473200
   ],
   "v2": [
    21850612948387,
    3941850463200
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
   "call": "symbols('src/attr/validators/__init__.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attr/validators/__init__.py\", \"pipe\"]]",
   "v1": [
    422796197,
    60016320
   ],
   "v2": [
    4592115990359,
    735812086464
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
     "src/attrs/validators.py",
     "attr.validators"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/attr/validators.py', 'pipe')",
  "key": "[\"symbols\", [\"src/attr/validators.py\", \"pipe\"]]",
  "provenance": "`attr.validators` would be `src/attr/validators.py` if that file exists; one call both checks and closes it",
  "v2": [
   65911526203,
   14599446160
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
  "def": "[\"symbols\", [\"src/attr.py\", \"pipe\"]]",
  "reexport": "[\"symbols\", [\"src/attr.py\", \"pipe\"]]",
  "star": "[\"symbols\", [\"src/attr.py\", \"pipe\"]]",
  "none": "[\"symbols\", [\"src/attr.py\", \"pipe\"]]",
  "missing": "[\"symbols\", [\"src/attr.py\", \"pipe\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"src/attr/validators.py\", \"pipe\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 16,
   "path": "src/attr/validators.py",
   "filter": "pipe",
   "header": {
    "lines": 767,
    "dynamic": false,
    "all_status": "static",
    "all_line": 19
   },
   "bindings": [],
   "complete": true
  }
```
</details>

## Step 17

`src/attr/validators.py` binds no `pipe` at module level; no star imports; a literal `__all__` at line 19; no dynamic namespace tricks.

Candidate modules so far: 9; statements confirmed: 2, ruled out: 2, modules with no such import: 1, pending: 4. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/filters.py`:3, star import of `attr.filters`, which does not export `pipe`.

Still to settle: know what `src/attr/converters.py` exports; know what `src/attr/setters.py` exports; know what `src/attr/validators.py` exports; locate the module `attr` imported by `tests/attr_import_star.py`.

Next: outline `src/attr.py` filtered to `pipe`, because `attr` would be `src/attr.py` if that file exists; one call both checks and closes it. I expect: a definition there ends the chain (about 85%); the file does not exist (about 10%); a re-export continues the chain to its source (under 5%); no binding at all points at a submodule or an unresolved name (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `src/attr/setters.py` filtered to `pipe`, is expected to open more follow-up work. Plan by outcome: def: outline `src/attr/setters.py` filtered to `pipe`; reexport: outline `src/attr/setters.py` filtered to `pipe`; star: outline `src/attr/setters.py` filtered to `pipe`; none: outline `src/attr/setters.py` filtered to `pipe`; missing: outline `src/attr/setters.py` filtered to `pipe`.

**Call:** `symbols('src/attr.py', 'pipe')`

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
    "src/attr/setters.py"
   ],
   "desc": "know what `src/attr/setters.py` exports"
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
   "call": "symbols('src/attr.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attr.py\", \"pipe\"]]",
   "v1": [
    124309310843,
    29198892320
   ],
   "v2": [
    630604897847,
    145994461600
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
   "call": "symbols('src/attr/setters.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attr/setters.py\", \"pipe\"]]",
   "v1": [
    60948181,
    11896550
   ],
   "v2": [
    630604897847,
    145994461600
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
     "src/attr/setters.py"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    37775,
    7328
   ],
   "v2": [
    63523353499,
    14599446160
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
    37775,
    7328
   ],
   "v2": [
    63523353499,
    14599446160
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
    61413,
    11908
   ],
   "v2": [
    38991640708979,
    7591712003200
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
   "call": "symbols('src/attr/__init__.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attr/__init__.py\", \"pipe\"]]",
   "v1": [
    13073107,
    2473200
   ],
   "v2": [
    1050628598650841,
    197092523160000
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
  "call": "symbols('src/attr.py', 'pipe')",
  "key": "[\"symbols\", [\"src/attr.py\", \"pipe\"]]",
  "provenance": "`attr` would be `src/attr.py` if that file exists; one call both checks and closes it",
  "v2": [
   630604897847,
   145994461600
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
  "def": "[\"symbols\", [\"src/attr/setters.py\", \"pipe\"]]",
  "reexport": "[\"symbols\", [\"src/attr/setters.py\", \"pipe\"]]",
  "star": "[\"symbols\", [\"src/attr/setters.py\", \"pipe\"]]",
  "none": "[\"symbols\", [\"src/attr/setters.py\", \"pipe\"]]",
  "missing": "[\"symbols\", [\"src/attr/setters.py\", \"pipe\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"src/attr.py\", \"pipe\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "error",
   "step": 17,
   "call": "[\"symbols\", [\"src/attr.py\", \"pipe\"]]",
   "error": "not a python file: src/attr.py",
   "missing": "src/attr.py"
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "src/attr/converters.py",
    8,
    "in",
    "`._make` resolves `pipe` to the target"
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
    "star import of `attr.exceptions`, which does not export `pipe`"
   ],
   [
    "src/attrs/filters.py",
    3,
    "out",
    "star import of `attr.filters`, which does not export `pipe`"
   ],
   [
    "src/attrs/setters.py",
    3,
    "pending",
    ""
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
    "tests/test_converters.py",
    15,
    "in",
    "`attr.converters` resolves `pipe` to the target"
   ],
   [
    "tests/test_next_gen.py",
    0,
    "none",
    "no import of the name in this module"
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

`src/attr.py` does not exist, so that path is ruled out. This is not the branch I planned for that outcome; the open items changed more than expected.

Candidate modules so far: 9; statements confirmed: 2, ruled out: 2, modules with no such import: 1, pending: 4. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/filters.py`:3, star import of `attr.filters`, which does not export `pipe`.

Open: know what `src/attr/converters.py` exports; know what `src/attr/setters.py` exports; know what `src/attr/validators.py` exports; locate the module `attr` imported by `tests/attr_import_star.py`.

Next: outline `src/attr/__init__.py` filtered to `pipe`, because `attr` would be `src/attr/__init__.py` if that file exists; one call both checks and closes it. I expect: a re-export continues the chain to its source (about 40%); no binding at all points at a submodule or an unresolved name (about 40%); a definition there ends the chain (about 20%); the file does not exist (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `src/attr/setters.py` filtered to `pipe`, costs more in expectation. Plan by outcome: def: outline `src/attr/setters.py` filtered to `pipe`; reexport: outline `src/attr/setters.py` filtered to `pipe`; star: outline `src/attr/setters.py` filtered to `pipe`; none: outline `src/attr/setters.py` filtered to `pipe`; missing: list `src/attr`.

**Call:** `symbols('src/attr/__init__.py', 'pipe')`

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
    "src/attr/setters.py"
   ],
   "desc": "know what `src/attr/setters.py` exports"
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
   "call": "symbols('src/attr/__init__.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attr/__init__.py\", \"pipe\"]]",
   "v1": [
    4377581,
    824400
   ],
   "v2": [
    25649311070657,
    4775275170000
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
   "call": "symbols('src/attr/setters.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attr/setters.py\", \"pipe\"]]",
   "v1": [
    1016431081,
    160603425
   ],
   "v2": [
    4601452091,
    856551600
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
     "src/attr/setters.py"
    ]
   ]
  },
  {
   "call": "read('src/attr/converters.py', 11, 30)",
   "key": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
   "v1": [
    1258469,
    197856
   ],
   "v2": [
    8909737,
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
    1258469,
    197856
   ],
   "v2": [
    8909737,
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
    17343215,
    2757618
   ],
   "v2": [
    3626384484413,
    573033020400
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
  "call": "symbols('src/attr/__init__.py', 'pipe')",
  "key": "[\"symbols\", [\"src/attr/__init__.py\", \"pipe\"]]",
  "provenance": "`attr` would be `src/attr/__init__.py` if that file exists; one call both checks and closes it",
  "v2": [
   25649311070657,
   4775275170000
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
  "def": "[\"symbols\", [\"src/attr/setters.py\", \"pipe\"]]",
  "reexport": "[\"symbols\", [\"src/attr/setters.py\", \"pipe\"]]",
  "star": "[\"symbols\", [\"src/attr/setters.py\", \"pipe\"]]",
  "none": "[\"symbols\", [\"src/attr/setters.py\", \"pipe\"]]",
  "missing": "[\"ls\", [\"src/attr\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"src/attr/setters.py\", \"pipe\"]]",
  "status": "deviated"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 18,
   "path": "src/attr/__init__.py",
   "filter": "pipe",
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
    "src/attr/converters.py",
    8,
    "in",
    "`._make` resolves `pipe` to the target"
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
    "star import of `attr.exceptions`, which does not export `pipe`"
   ],
   [
    "src/attrs/filters.py",
    3,
    "out",
    "star import of `attr.filters`, which does not export `pipe`"
   ],
   [
    "src/attrs/setters.py",
    3,
    "pending",
    ""
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
    "tests/test_converters.py",
    15,
    "in",
    "`attr.converters` resolves `pipe` to the target"
   ],
   [
    "tests/test_next_gen.py",
    0,
    "none",
    "no import of the name in this module"
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

## Step 19

`src/attr/__init__.py` binds no `pipe` at module level; no star imports; a literal `__all__` at line 45; it uses dynamic namespace tricks.

Candidate modules so far: 9; statements confirmed: 2, ruled out: 2, modules with no such import: 1, pending: 4. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/filters.py`:3, star import of `attr.filters`, which does not export `pipe`.

Outstanding: know what `src/attr/converters.py` exports; know what `src/attr/setters.py` exports; know what `src/attr/validators.py` exports; know what `src/attr/__init__.py` exports.

Next: outline `src/attr/setters.py` filtered to `pipe`, because module `src/attr/setters.py` (step 2). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, read `src/attr/__init__.py` from line 45, scores the same; the seed broke the tie. Plan by outcome: def: read `src/attr/__init__.py` from line 45; reexport: read `src/attr/__init__.py` from line 45; star: read `src/attr/__init__.py` from line 45; none: read `src/attr/__init__.py` from line 45.

**Call:** `symbols('src/attr/setters.py', 'pipe')`

**Response**: outcome `def`

```
module src/attr/setters.py lines=83 dynamic=no all=none
11 def pipe
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
    "src/attr/setters.py"
   ],
   "desc": "know what `src/attr/setters.py` exports"
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
    131,
    32
   ],
   "v2": [
    791034121,
    190344800
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
    131,
    32
   ],
   "v2": [
    791034121,
    190344800
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
    131,
    32
   ],
   "v2": [
    791034121,
    190344800
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
   "call": "symbols('src/attr/setters.py', 'pipe')",
   "key": "[\"symbols\", [\"src/attr/setters.py\", \"pipe\"]]",
   "v1": [
    48324331,
    11896550
   ],
   "v2": [
    791034121,
    190344800
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
     "src/attr/setters.py"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/attr/setters.py', 'pipe')",
  "key": "[\"symbols\", [\"src/attr/setters.py\", \"pipe\"]]",
  "provenance": "module `src/attr/setters.py` (step 2)",
  "v2": [
   791034121,
   190344800
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
  "def": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]",
  "reexport": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]",
  "star": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]",
  "none": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"src/attr/setters.py\", \"pipe\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 19,
   "path": "src/attr/setters.py",
   "filter": "pipe",
   "header": {
    "lines": 83,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/attr/setters.py",
     "name": "pipe",
     "line": 11,
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
  "verdicts": [
   [
    "src/attr/converters.py",
    8,
    "in",
    "`._make` resolves `pipe` to the target"
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
    "star import of `attr.exceptions`, which does not export `pipe`"
   ],
   [
    "src/attrs/filters.py",
    3,
    "out",
    "star import of `attr.filters`, which does not export `pipe`"
   ],
   [
    "src/attrs/setters.py",
    3,
    "out",
    "star import of `attr.setters` binds `pipe` to src/attr/setters.py:11"
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
    "tests/test_converters.py",
    15,
    "in",
    "`attr.converters` resolves `pipe` to the target"
   ],
   [
    "tests/test_next_gen.py",
    0,
    "none",
    "no import of the name in this module"
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

In `src/attr/setters.py`, `pipe` has exactly one binding: a def at line 11. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 9; statements confirmed: 2, ruled out: 3, modules with no such import: 1, pending: 3. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/setters.py`:3, star import of `attr.setters` binds `pipe` to src/attr/setters.py:11.

Open: know what `src/attr/converters.py` exports; know what `src/attr/validators.py` exports; know what `src/attr/__init__.py` exports.

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
 "adherence": {
  "planned": "[\"read\", [\"src/attr/__init__.py\", 45, 30]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "read",
   "step": 20,
   "path": "src/attr/__init__.py",
   "start": 45,
   "count": 30,
   "n": 30
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "src/attr/converters.py",
    8,
    "in",
    "`._make` resolves `pipe` to the target"
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
    "star import of `attr.exceptions`, which does not export `pipe`"
   ],
   [
    "src/attrs/filters.py",
    3,
    "out",
    "star import of `attr.filters`, which does not export `pipe`"
   ],
   [
    "src/attrs/setters.py",
    3,
    "out",
    "star import of `attr.setters` binds `pipe` to src/attr/setters.py:11"
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
    "tests/test_converters.py",
    15,
    "in",
    "`attr.converters` resolves `pipe` to the target"
   ],
   [
    "tests/test_next_gen.py",
    0,
    "none",
    "no import of the name in this module"
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

The statement at `src/attr/__init__.py`:45 binds `__all__`.

Candidate modules so far: 9; statements confirmed: 2, ruled out: 3, modules with no such import: 1, pending: 3. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/setters.py`:3, star import of `attr.setters` binds `pipe` to src/attr/setters.py:11.

Still to settle: know what `src/attr/converters.py` exports; know what `src/attr/validators.py` exports; know what `src/attr/__init__.py` exports.

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
 "adherence": {
  "planned": "[\"read\", [\"src/attr/converters.py\", 11, 30]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "read",
   "step": 21,
   "path": "src/attr/converters.py",
   "start": 11,
   "count": 30,
   "n": 30
  },
  {
   "kind": "all_names",
   "step": 21,
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
    "src/attr/converters.py",
    8,
    "in",
    "`._make` resolves `pipe` to the target"
   ],
   [
    "src/attrs/converters.py",
    3,
    "in",
    "star import of `attr.converters`, which exports `pipe` from the target"
   ],
   [
    "src/attrs/exceptions.py",
    3,
    "out",
    "star import of `attr.exceptions`, which does not export `pipe`"
   ],
   [
    "src/attrs/filters.py",
    3,
    "out",
    "star import of `attr.filters`, which does not export `pipe`"
   ],
   [
    "src/attrs/setters.py",
    3,
    "out",
    "star import of `attr.setters` binds `pipe` to src/attr/setters.py:11"
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
    "tests/test_converters.py",
    15,
    "in",
    "`attr.converters` resolves `pipe` to the target"
   ],
   [
    "tests/test_next_gen.py",
    0,
    "none",
    "no import of the name in this module"
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

The statement at `src/attr/converters.py`:11 binds `__all__`. `__all__` in `src/attr/converters.py` lists 4 names, and it names `pipe`.

Candidate modules so far: 9; statements confirmed: 3, ruled out: 3, modules with no such import: 1, pending: 2. import coverage complete; star coverage complete. Latest ruled out: `src/attrs/setters.py`:3, star import of `attr.setters` binds `pipe` to src/attr/setters.py:11.

Open: know what `src/attr/validators.py` exports; know what `src/attr/__init__.py` exports.

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
 "adherence": {
  "planned": "[\"read\", [\"src/attr/__init__.py\", 45, 60]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "read",
   "step": 22,
   "path": "src/attr/__init__.py",
   "start": 45,
   "count": 60,
   "n": 60
  },
  {
   "kind": "all_names",
   "step": 22,
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
    "src/attr/converters.py",
    8,
    "in",
    "`._make` resolves `pipe` to the target"
   ],
   [
    "src/attrs/converters.py",
    3,
    "in",
    "star import of `attr.converters`, which exports `pipe` from the target"
   ],
   [
    "src/attrs/exceptions.py",
    3,
    "out",
    "star import of `attr.exceptions`, which does not export `pipe`"
   ],
   [
    "src/attrs/filters.py",
    3,
    "out",
    "star import of `attr.filters`, which does not export `pipe`"
   ],
   [
    "src/attrs/setters.py",
    3,
    "out",
    "star import of `attr.setters` binds `pipe` to src/attr/setters.py:11"
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
    "star import of `attr`, which does not export `pipe`"
   ],
   [
    "tests/test_converters.py",
    15,
    "in",
    "`attr.converters` resolves `pipe` to the target"
   ],
   [
    "tests/test_next_gen.py",
    0,
    "none",
    "no import of the name in this module"
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

The statement at `src/attr/__init__.py`:45 binds `__all__`. `__all__` in `src/attr/__init__.py` lists 34 names, and `pipe` is not among them.

Candidate modules so far: 9; statements confirmed: 3, ruled out: 4, modules with no such import: 1, pending: 1. import coverage complete; star coverage complete. Latest ruled out: `tests/attr_import_star.py`:4, star import of `attr`, which does not export `pipe`.

Outstanding: know what `src/attr/validators.py` exports.

Next: read `src/attr/validators.py` from line 19, because `__all__` of `src/attr/validators.py` starts at line 19 (outline header). I expect: the whole list fits the window (about 90%); the list runs past the window (about 10%). Plan by outcome: fits: done; long: work the items it opens.

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
 "adherence": {
  "planned": "[\"read\", [\"src/attr/validators.py\", 19, 30]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "read",
   "step": 23,
   "path": "src/attr/validators.py",
   "start": 19,
   "count": 30,
   "n": 30
  },
  {
   "kind": "all_names",
   "step": 23,
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
    "src/attr/converters.py",
    8,
    "in",
    "`._make` resolves `pipe` to the target"
   ],
   [
    "src/attrs/converters.py",
    3,
    "in",
    "star import of `attr.converters`, which exports `pipe` from the target"
   ],
   [
    "src/attrs/exceptions.py",
    3,
    "out",
    "star import of `attr.exceptions`, which does not export `pipe`"
   ],
   [
    "src/attrs/filters.py",
    3,
    "out",
    "star import of `attr.filters`, which does not export `pipe`"
   ],
   [
    "src/attrs/setters.py",
    3,
    "out",
    "star import of `attr.setters` binds `pipe` to src/attr/setters.py:11"
   ],
   [
    "src/attrs/validators.py",
    3,
    "out",
    "star import of `attr.validators`, which does not export `pipe`"
   ],
   [
    "tests/attr_import_star.py",
    4,
    "out",
    "star import of `attr`, which does not export `pipe`"
   ],
   [
    "tests/test_converters.py",
    15,
    "in",
    "`attr.converters` resolves `pipe` to the target"
   ],
   [
    "tests/test_next_gen.py",
    0,
    "none",
    "no import of the name in this module"
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

Certificate complete. 3 import statements import this definition: `src/attr/converters.py:8`, `src/attrs/converters.py:3`, `tests/test_converters.py:15`. In hindsight, 1 of 23 calls were not needed for the certificate: steps 20.

**Answer:** `{"target": {"kind": "def", "path": "src/attr/_make.py", "line": 3404, "name": "pipe", "detail": "def"}, "text": "src/attr/_make.py:3404", "statements": ["src/attr/converters.py:8", "src/attrs/converters.py:3", "tests/test_converters.py:15"], "count": 3}`  
**Stopped:** certificate after 23 calls