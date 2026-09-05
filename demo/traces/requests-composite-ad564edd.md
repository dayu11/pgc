# requests-composite-ad564edd

**Repository:** requests  
**Family:** composite  
**Seed:** 0, prior 89d4e155c6e8b2e4

## Task

In `tests/test_requests.py`, line 33 imports `ChunkedEncodingError` from `requests.exceptions`. Under the declared semantics, which definition does the module-level name `ChunkedEncodingError` bound by this statement resolve to? Answer with `path:line`. Then list every module-level import statement in the snapshot that imports that definition (from-imports naming it, directly or with `as`, and star imports of modules that export it), as `path:line` entries.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

Nothing seen yet beyond the task text.

Chain: `tests/test_requests.py` is not yet closed for `ChunkedEncodingError`.

Outstanding: close the namespace of `tests/test_requests.py` for `ChunkedEncodingError`.

Next: outline `tests/test_requests.py`, because module `tests/test_requests.py` (task). I expect: a definition there ends the chain (about 85%); a capped outline means filtering by name (about 15%); no binding at all points at a submodule or an unresolved name (under 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `tests/test_requests.py` filtered to `ChunkedEncodingError`, is expected to open more follow-up work. Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done; cap: outline `tests/test_requests.py` filtered to `ChunkedEncodingError`.

**Call:** `symbols('tests/test_requests.py')`

**Response** (capped): outcome `cap`

```
module tests/test_requests.py lines=3095 dynamic=no all=none
3 import collections <- collections
4 import contextlib <- contextlib
5 import io <- io
6 import json <- json
7 import os <- os
8 import pickle <- pickle
9 import re <- re
10 import tempfile <- tempfile
11 import threading <- threading
12 import warnings <- warnings
13 from mock <- unittest mock
15 import pytest <- pytest
16 import urllib3 <- urllib3
17 from Urllib3Timeout <- urllib3.util Timeout
19 import requests <- requests
20 from HTTPAdapter <- requests.adapters HTTPAdapter
21 from HTTPDigestAuth <- requests.auth HTTPDigestAuth
21 from _basic_auth_str <- requests.auth _basic_auth_str
22 from JSONDecodeError <- requests.compat JSONDecodeError
22 from Morsel <- requests.compat Morsel
22 from MutableMapping <- requests.compat MutableMapping
22 from builtin_str <- requests.compat builtin_str
22 from cookielib <- requests.compat cookielib
22 from getproxies <- requests.compat getproxies
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
    "tests/test_requests.py",
    "ChunkedEncodingError"
   ],
   "desc": "close the namespace of `tests/test_requests.py` for `ChunkedEncodingError`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/test_requests.py')",
   "key": "[\"symbols\", [\"tests/test_requests.py\"]]",
   "v1": [
    693911719,
    600429907
   ],
   "v2": [
    1351273299181,
    960687851200
   ],
   "p_cap": [
    47,
    352
   ],
   "forecast": {
    "def": [
     1525,
     1828
    ],
    "reexport": [
     305,
     40216
    ],
    "star": [
     305,
     160864
    ],
    "none": [
     915,
     40216
    ],
    "cap": [
     47,
     352
    ]
   },
   "serves": [
    [
     "bindings",
     "tests/test_requests.py",
     "ChunkedEncodingError"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_requests.py', 'ChunkedEncodingError')",
   "key": "[\"symbols\", [\"tests/test_requests.py\", \"ChunkedEncodingError\"]]",
   "v1": [
    8662557,
    2986025
   ],
   "v2": [
    8662557,
    2986025
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
     "tests/test_requests.py",
     "ChunkedEncodingError"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_requests.py')",
  "key": "[\"symbols\", [\"tests/test_requests.py\"]]",
  "provenance": "module `tests/test_requests.py` (task)",
  "v2": [
   1351273299181,
   960687851200
  ]
 },
 "forecast": {
  "def": [
   1525,
   1828
  ],
  "reexport": [
   305,
   40216
  ],
  "star": [
   305,
   160864
  ],
  "none": [
   915,
   40216
  ],
  "cap": [
   47,
   352
  ]
 },
 "plan": {
  "def": "done",
  "reexport": "continue",
  "star": "continue",
  "none": "done",
  "cap": "[\"symbols\", [\"tests/test_requests.py\", \"ChunkedEncodingError\"]]"
 },
 "adherence": null,
 "facts": [
  {
   "kind": "outline",
   "step": 1,
   "path": "tests/test_requests.py",
   "filter": null,
   "header": {
    "lines": 3095,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_requests.py",
     "name": "collections",
     "line": 3,
     "kind": "import",
     "src": "collections",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_requests.py",
     "name": "contextlib",
     "line": 4,
     "kind": "import",
     "src": "contextlib",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_requests.py",
     "name": "io",
     "line": 5,
     "kind": "import",
     "src": "io",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_requests.py",
     "name": "json",
     "line": 6,
     "kind": "import",
     "src": "json",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_requests.py",
     "name": "os",
     "line": 7,
     "kind": "import",
     "src": "os",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_requests.py",
     "name": "pickle",
     "line": 8,
     "kind": "import",
     "src": "pickle",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_requests.py",
     "name": "re",
     "line": 9,
     "kind": "import",
     "src": "re",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_requests.py",
     "name": "tempfile",
     "line": 10,
     "kind": "import",
     "src": "tempfile",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_requests.py",
     "name": "threading",
     "line": 11,
     "kind": "import",
     "src": "threading",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_requests.py",
     "name": "warnings",
     "line": 12,
     "kind": "import",
     "src": "warnings",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_requests.py",
     "name": "mock",
     "line": 13,
     "kind": "from",
     "src": "unittest",
     "src_name": "mock",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_requests.py",
     "name": "pytest",
     "line": 15,
     "kind": "import",
     "src": "pytest",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_requests.py",
     "name": "urllib3",
     "line": 16,
     "kind": "import",
     "src": "urllib3",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_requests.py",
     "name": "Urllib3Timeout",
     "line": 17,
     "kind": "from",
     "src": "urllib3.util",
     "src_name": "Timeout",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_requests.py",
     "name": "requests",
     "line": 19,
     "kind": "import",
     "src": "requests",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_requests.py",
     "name": "HTTPAdapter",
     "line": 20,
     "kind": "from",
     "src": "requests.adapters",
     "src_name": "HTTPAdapter",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_requests.py",
     "name": "HTTPDigestAuth",
     "line": 21,
     "kind": "from",
     "src": "requests.auth",
     "src_name": "HTTPDigestAuth",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_requests.py",
     "name": "_basic_auth_str",
     "line": 21,
     "kind": "from",
     "src": "requests.auth",
     "src_name": "_basic_auth_str",
     "conditional": false,
     "col": 0
    },
 
```
</details>

## Step 2

The outline of `tests/test_requests.py` has 40 bindings (capped, so this is only the start of the file); no `__all__`; no dynamic namespace tricks.

Chain: `tests/test_requests.py` is not yet closed for `ChunkedEncodingError`.

Still to settle: close the namespace of `tests/test_requests.py` for `ChunkedEncodingError`.

Next: outline `tests/test_requests.py` filtered to `ChunkedEncodingError`, because module `tests/test_requests.py` (task), name `ChunkedEncodingError` (task). I expect: a re-export continues the chain to its source (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a definition there ends the chain (under 5%); no binding but a star import means checking what that source exports (under 5%). Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done.

**Call:** `symbols('tests/test_requests.py', 'ChunkedEncodingError')`

**Response**: outcome `reexport`

```
module tests/test_requests.py lines=3095 dynamic=no all=none
33 from ChunkedEncodingError <- requests.exceptions ChunkedEncodingError
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "tests/test_requests.py",
    "ChunkedEncodingError"
   ],
   "desc": "close the namespace of `tests/test_requests.py` for `ChunkedEncodingError`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/test_requests.py', 'ChunkedEncodingError')",
   "key": "[\"symbols\", [\"tests/test_requests.py\", \"ChunkedEncodingError\"]]",
   "v1": [
    8662557,
    2986025
   ],
   "v2": [
    8662557,
    2986025
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
     "tests/test_requests.py",
     "ChunkedEncodingError"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_requests.py', 'ChunkedEncodingError')",
  "key": "[\"symbols\", [\"tests/test_requests.py\", \"ChunkedEncodingError\"]]",
  "provenance": "module `tests/test_requests.py` (task), name `ChunkedEncodingError` (task)",
  "v2": [
   8662557,
   2986025
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
  "planned": "[\"symbols\", [\"tests/test_requests.py\", \"ChunkedEncodingError\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 2,
   "path": "tests/test_requests.py",
   "filter": "ChunkedEncodingError",
   "header": {
    "lines": 3095,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_requests.py",
     "name": "ChunkedEncodingError",
     "line": 33,
     "kind": "from",
     "src": "requests.exceptions",
     "src_name": "ChunkedEncodingError",
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
    "tests/test_requests.py",
    "ChunkedEncodingError",
    "reexport",
    [
     "requests.exceptions",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 3

In `tests/test_requests.py`, `ChunkedEncodingError` has exactly one binding: line 33 imports it as `ChunkedEncodingError` from `requests.exceptions`. No dynamic namespace tricks, no `__all__`.

Chain: `tests/test_requests.py` takes `ChunkedEncodingError` from `requests.exceptions` (module not yet located).

Outstanding: locate the module `requests.exceptions` imported by `tests/test_requests.py`.

Next: grep `def`/`class ChunkedEncodingError` statements under `.`, because a `def`/`class ChunkedEncodingError` statement would reveal the module file; `ChunkedEncodingError` task. I expect: hits under the cap (about 95%); a capped result (about 5%); no hits (about 5%). The alternative, list `.`, is more likely to hit the cap (about 20% against about 5%). Plan by outcome: zero: outline `requests/exceptions.py` filtered to `ChunkedEncodingError`; mid: outline each module that appears; cap: outline `requests/exceptions.py` filtered to `ChunkedEncodingError`.

**Call:** `grep('^\\s*(?:async\\s+)?(?:def|class)\\s+ChunkedEncodingError\\b', '.')`

**Response**: outcome `mid`

```
src/requests/exceptions.py:130:class ChunkedEncodingError(RequestException):
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_requests.py",
    "requests.exceptions"
   ],
   "desc": "locate the module `requests.exceptions` imported by `tests/test_requests.py`"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+ChunkedEncodingError\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+ChunkedEncodingError\\\\b\", \".\"]]",
   "v1": [
    16447,
    7910
   ],
   "v2": [
    478321993351457,
    228752986828674
   ],
   "p_cap": [
    1,
    35
   ],
   "forecast": {
    "zero": [
     1,
     35
    ],
    "mid": [
     33,
     35
    ],
    "cap": [
     1,
     35
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_requests.py",
     "requests.exceptions"
    ]
   ]
  },
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    4565,
    2034
   ],
   "v2": [
    160679,
    71190
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
     "tests/test_requests.py",
     "requests.exceptions"
    ]
   ]
  },
  {
   "call": "symbols('requests/exceptions.py', 'ChunkedEncodingError')",
   "key": "[\"symbols\", [\"requests/exceptions.py\", \"ChunkedEncodingError\"]]",
   "v1": [
    72789767067077,
    32678998118382
   ],
   "v2": [
    73915113073033,
    32678998118382
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     4757920,
     12436341
    ],
    "reexport": [
     475792,
     136799751
    ],
    "star": [
     118948,
     136799751
    ],
    "none": [
     475792,
     45599917
    ],
    "missing": [
     180395,
     299343
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_requests.py",
     "requests.exceptions"
    ]
   ]
  },
  {
   "call": "symbols('requests/exceptions/__init__.py', 'ChunkedEncodingError')",
   "key": "[\"symbols\", [\"requests/exceptions/__init__.py\", \"ChunkedEncodingError\"]]",
   "v1": [
    21108271523,
    7069583631
   ],
   "v2": [
    752149026163,
    247435427085
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     11004,
     1097591
    ],
    "reexport": [
     31178,
     1097591
    ],
    "star": [
     917,
     1097591
    ],
    "none": [
     17423,
     1097591
    ],
    "missing": [
     94279,
     99781
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_requests.py",
     "requests.exceptions"
    ]
   ]
  }
 ],
 "choice": {
  "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+ChunkedEncodingError\\\\b', '.')",
  "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+ChunkedEncodingError\\\\b\", \".\"]]",
  "provenance": "a `def`/`class ChunkedEncodingError` statement would reveal the module file; `ChunkedEncodingError` task",
  "v2": [
   478321993351457,
   228752986828674
  ]
 },
 "forecast": {
  "zero": [
   1,
   35
  ],
  "mid": [
   33,
   35
  ],
  "cap": [
   1,
   35
  ]
 },
 "plan": {
  "zero": "[\"symbols\", [\"requests/exceptions.py\", \"ChunkedEncodingError\"]]",
  "mid": "continue",
  "cap": "[\"symbols\", [\"requests/exceptions.py\", \"ChunkedEncodingError\"]]"
 },
 "adherence": {
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "grep",
   "step": 3,
   "pattern": "^\\s*(?:async\\s+)?(?:def|class)\\s+ChunkedEncodingError\\b",
   "scope": ".",
   "hits": [
    [
     "src/requests/exceptions.py",
     130
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "chain": [
   [
    "tests/test_requests.py",
    "ChunkedEncodingError",
    "reexport",
    [
     "requests.exceptions",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 4

The grep under `.` returned 1 lines, under the cap, so these are all of them: `src/requests/exceptions.py`.

Chain: `tests/test_requests.py` takes `ChunkedEncodingError` from `requests.exceptions` (module not yet located).

Outstanding: locate the module `requests.exceptions` imported by `tests/test_requests.py`.

Next: list `.`, because `requests.exceptions` imported by `tests/test_requests.py` should live under `.`. I expect: a complete listing settles which files exist (about 80%); a capped listing settles nothing (about 20%). The alternative, outline `requests/exceptions.py` filtered to `ChunkedEncodingError`, costs more in expectation. Plan by outcome: complete: outline the module it reveals; cap: outline `requests/exceptions.py` filtered to `ChunkedEncodingError`.

**Call:** `ls('.')`

**Response**: outcome `complete`

```
.github/
.pre-commit-config.yaml
.readthedocs.yaml
AUTHORS.rst
HISTORY.md
MANIFEST.in
README.md
docs/
pyproject.toml
requirements-dev.txt
setup.py
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
    "tests/test_requests.py",
    "requests.exceptions"
   ],
   "desc": "locate the module `requests.exceptions` imported by `tests/test_requests.py`"
  }
 ],
 "candidates": [
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    4565,
    2034
   ],
   "v2": [
    673504410816511,
    294110983065438
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
     "tests/test_requests.py",
     "requests.exceptions"
    ]
   ]
  },
  {
   "call": "symbols('requests/exceptions.py', 'ChunkedEncodingError')",
   "key": "[\"symbols\", [\"requests/exceptions.py\", \"ChunkedEncodingError\"]]",
   "v1": [
    72789767067077,
    32678998118382
   ],
   "v2": [
    694495013812153,
    294110983065438
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     4757920,
     12436341
    ],
    "reexport": [
     475792,
     136799751
    ],
    "star": [
     118948,
     136799751
    ],
    "none": [
     475792,
     45599917
    ],
    "missing": [
     180395,
     299343
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_requests.py",
     "requests.exceptions"
    ]
   ]
  },
  {
   "call": "symbols('requests/exceptions/__init__.py', 'ChunkedEncodingError')",
   "key": "[\"symbols\", [\"requests/exceptions/__init__.py\", \"ChunkedEncodingError\"]]",
   "v1": [
    21108271523,
    7069583631
   ],
   "v2": [
    98499630324243474356,
    30977059556877606249
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     11004,
     1097591
    ],
    "reexport": [
     31178,
     1097591
    ],
    "star": [
     917,
     1097591
    ],
    "none": [
     17423,
     1097591
    ],
    "missing": [
     94279,
     99781
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_requests.py",
     "requests.exceptions"
    ]
   ]
  }
 ],
 "choice": {
  "call": "ls('.')",
  "key": "[\"ls\", [\".\"]]",
  "provenance": "`requests.exceptions` imported by `tests/test_requests.py` should live under `.`",
  "v2": [
   673504410816511,
   294110983065438
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
  "cap": "[\"symbols\", [\"requests/exceptions.py\", \"ChunkedEncodingError\"]]"
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
    ".github/",
    ".pre-commit-config.yaml",
    ".readthedocs.yaml",
    "AUTHORS.rst",
    "HISTORY.md",
    "MANIFEST.in",
    "README.md",
    "docs/",
    "pyproject.toml",
    "requirements-dev.txt",
    "setup.py",
    "src/",
    "tests/",
    "tox.ini"
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "chain": [
   [
    "tests/test_requests.py",
    "ChunkedEncodingError",
    "reexport",
    [
     "requests.exceptions",
     "src/requests/exceptions.py"
    ]
   ],
   [
    "src/requests/exceptions.py",
    "ChunkedEncodingError",
    "open",
    null
   ]
  ]
 }
}
```
</details>

## Step 5

`.` lists 14 entries (complete): `.github/`, `docs/`, `setup.py`, `src/`, `tests/`.

Chain: `tests/test_requests.py` takes `ChunkedEncodingError` from `requests.exceptions` (`src/requests/exceptions.py`); `src/requests/exceptions.py` is not yet closed for `ChunkedEncodingError`.

Still to settle: close the namespace of `src/requests/exceptions.py` for `ChunkedEncodingError`.

Next: outline `src/requests/exceptions.py` filtered to `ChunkedEncodingError`, because module `src/requests/exceptions.py` (step 3), name `ChunkedEncodingError` (task). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `src/requests/exceptions.py`, is more likely to hit the cap (about 15% against under 5%). Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done.

**Call:** `symbols('src/requests/exceptions.py', 'ChunkedEncodingError')`

**Response**: outcome `def`

```
module src/requests/exceptions.py lines=163 dynamic=no all=none
130 class ChunkedEncodingError
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/requests/exceptions.py",
    "ChunkedEncodingError"
   ],
   "desc": "close the namespace of `src/requests/exceptions.py` for `ChunkedEncodingError`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/requests/exceptions.py', 'ChunkedEncodingError')",
   "key": "[\"symbols\", [\"src/requests/exceptions.py\", \"ChunkedEncodingError\"]]",
   "v1": [
    25342997,
    23888200
   ],
   "v2": [
    25342997,
    23888200
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
     "src/requests/exceptions.py",
     "ChunkedEncodingError"
    ]
   ]
  },
  {
   "call": "symbols('src/requests/exceptions.py')",
   "key": "[\"symbols\", [\"src/requests/exceptions.py\"]]",
   "v1": [
    693911719,
    600429907
   ],
   "v2": [
    4460930934863,
    3842751404800
   ],
   "p_cap": [
    47,
    352
   ],
   "forecast": {
    "def": [
     1525,
     1828
    ],
    "reexport": [
     305,
     40216
    ],
    "star": [
     305,
     160864
    ],
    "none": [
     915,
     40216
    ],
    "cap": [
     47,
     352
    ]
   },
   "serves": [
    [
     "bindings",
     "src/requests/exceptions.py",
     "ChunkedEncodingError"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/requests/exceptions.py', 'ChunkedEncodingError')",
  "key": "[\"symbols\", [\"src/requests/exceptions.py\", \"ChunkedEncodingError\"]]",
  "provenance": "module `src/requests/exceptions.py` (step 3), name `ChunkedEncodingError` (task)",
  "v2": [
   25342997,
   23888200
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
   "path": "src/requests/exceptions.py",
   "filter": "ChunkedEncodingError",
   "header": {
    "lines": 163,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/requests/exceptions.py",
     "name": "ChunkedEncodingError",
     "line": 130,
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
    "tests/test_requests.py",
    "ChunkedEncodingError",
    "reexport",
    [
     "requests.exceptions",
     "src/requests/exceptions.py"
    ]
   ],
   [
    "src/requests/exceptions.py",
    "ChunkedEncodingError",
    "class",
    130
   ]
  ]
 }
}
```
</details>

## Step 6

In `src/requests/exceptions.py`, `ChunkedEncodingError` has exactly one binding: a class at line 130. No dynamic namespace tricks, no `__all__`. This is not the branch I planned for that outcome; the open items changed more than expected.

Candidate modules so far: 0; statements confirmed: 0, ruled out: 0, modules with no such import: 0, pending: 0. import coverage open at `.`; star coverage open at `.`.

Open: cover `.` for import lines; cover `.` for star lines.

Next: grep from-imports naming `ChunkedEncodingError` or star imports under `.`, because import and star lines under `.` in one call. I expect: hits under the cap (about 65%); no hits (about 30%); a capped result (about 10%). The alternative, grep from-imports naming `ChunkedEncodingError` under `.`, serves fewer of the open items. Plan by outcome: zero: done; mid: outline each module that appears; cap: list the scope and split it.

**Call:** `grep('^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bChunkedEncodingError\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*ChunkedEncodingError\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$', '.')`

**Response**: outcome `mid`

```
src/requests/models.py:58:    ChunkedEncodingError,
src/requests/sessions.py:31:    ChunkedEncodingError,
tests/test_requests.py:34:    ChunkedEncodingError,
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
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bChunkedEncodingError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*ChunkedEncodingError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bChunkedEncodingError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*ChunkedEncodingError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
   "v1": [
    14597935207,
    2752553440
   ],
   "v2": [
    14597935207,
    2752553440
   ],
   "p_cap": [
    3,
    35
   ],
   "forecast": {
    "zero": [
     2,
     7
    ],
    "mid": [
     22,
     35
    ],
    "cap": [
     3,
     35
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
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bChunkedEncodingError\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*ChunkedEncodingError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bChunkedEncodingError\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*ChunkedEncodingError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
   "v1": [
    10231155043481,
    1509803649120
   ],
   "v2": [
    10231155043481,
    1509803649120
   ],
   "p_cap": [
    1,
    31
   ],
   "forecast": {
    "zero": [
     24,
     31
    ],
    "mid": [
     6,
     31
    ],
    "cap": [
     1,
     31
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
    10231155043481,
    1509803649120
   ],
   "v2": [
    10231155043481,
    1509803649120
   ],
   "p_cap": [
    1,
    17
   ],
   "forecast": {
    "zero": [
     7,
     17
    ],
    "mid": [
     9,
     17
    ],
    "cap": [
     1,
     17
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
  "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bChunkedEncodingError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*ChunkedEncodingError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
  "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bChunkedEncodingError\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*ChunkedEncodingError\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
  "provenance": "import and star lines under `.` in one call",
  "v2": [
   14597935207,
   2752553440
  ]
 },
 "forecast": {
  "zero": [
   2,
   7
  ],
  "mid": [
   22,
   35
  ],
  "cap": [
   3,
   35
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
   "pattern": "^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bChunkedEncodingError\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*ChunkedEncodingError\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$",
   "scope": ".",
   "hits": [
    [
     "src/requests/models.py",
     58
    ],
    [
     "src/requests/sessions.py",
     31
    ],
    [
     "tests/test_requests.py",
     34
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "src/requests/models.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "src/requests/sessions.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_requests.py",
    33,
    "in",
    "`requests.exceptions` resolves `ChunkedEncodingError` to the target"
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

The grep under `.` returned 3 lines, under the cap, so these are all of them: `src/requests/models.py`, `src/requests/sessions.py`, `tests/test_requests.py`.

Candidate modules so far: 3; statements confirmed: 1, ruled out: 0, modules with no such import: 0, pending: 2. import coverage complete; star coverage complete.

Open: outline `src/requests/models.py` for its `ChunkedEncodingError` imports; outline `src/requests/sessions.py` for its `ChunkedEncodingError` imports.

Next: outline `src/requests/models.py` filtered to `ChunkedEncodingError`, because `src/requests/models.py` had a matching line (step 6); its outline names every `ChunkedEncodingError` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `src/requests/sessions.py` filtered to `ChunkedEncodingError`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `src/requests/sessions.py` filtered to `ChunkedEncodingError`; cap: outline `src/requests/sessions.py` filtered to `ChunkedEncodingError`.

**Call:** `symbols('src/requests/models.py', 'ChunkedEncodingError')`

**Response**: outcome `ok`

```
module src/requests/models.py lines=1185 dynamic=no all=none
57 from ChunkedEncodingError <- .exceptions ChunkedEncodingError
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/requests/models.py",
    "ChunkedEncodingError"
   ],
   "desc": "outline `src/requests/models.py` for its `ChunkedEncodingError` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/requests/sessions.py",
    "ChunkedEncodingError"
   ],
   "desc": "outline `src/requests/sessions.py` for its `ChunkedEncodingError` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/requests/models.py', 'ChunkedEncodingError')",
   "key": "[\"symbols\", [\"src/requests/models.py\", \"ChunkedEncodingError\"]]",
   "v1": [
    901999,
    271200
   ],
   "v2": [
    907423,
    271200
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "src/requests/models.py",
     "ChunkedEncodingError"
    ]
   ]
  },
  {
   "call": "symbols('src/requests/sessions.py', 'ChunkedEncodingError')",
   "key": "[\"symbols\", [\"src/requests/sessions.py\", \"ChunkedEncodingError\"]]",
   "v1": [
    901999,
    271200
   ],
   "v2": [
    907423,
    271200
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "src/requests/sessions.py",
     "ChunkedEncodingError"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/requests/models.py', 'ChunkedEncodingError')",
  "key": "[\"symbols\", [\"src/requests/models.py\", \"ChunkedEncodingError\"]]",
  "provenance": "`src/requests/models.py` had a matching line (step 6); its outline names every `ChunkedEncodingError` import exactly",
  "v2": [
   907423,
   271200
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
  "ok": "[\"symbols\", [\"src/requests/sessions.py\", \"ChunkedEncodingError\"]]",
  "cap": "[\"symbols\", [\"src/requests/sessions.py\", \"ChunkedEncodingError\"]]"
 },
 "adherence": {
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 7,
   "path": "src/requests/models.py",
   "filter": "ChunkedEncodingError",
   "header": {
    "lines": 1185,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/requests/models.py",
     "name": "ChunkedEncodingError",
     "line": 57,
     "kind": "from",
     "src": ".exceptions",
     "src_name": "ChunkedEncodingError",
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
    "src/requests/models.py",
    57,
    "in",
    "`.exceptions` resolves `ChunkedEncodingError` to the target"
   ],
   [
    "src/requests/sessions.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_requests.py",
    33,
    "in",
    "`requests.exceptions` resolves `ChunkedEncodingError` to the target"
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

## Step 8

In `src/requests/models.py`, `ChunkedEncodingError` has exactly one binding: line 57 imports it as `ChunkedEncodingError` from `.exceptions`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 3; statements confirmed: 2, ruled out: 0, modules with no such import: 0, pending: 1. import coverage complete; star coverage complete.

Outstanding: outline `src/requests/sessions.py` for its `ChunkedEncodingError` imports.

Next: outline `src/requests/sessions.py` filtered to `ChunkedEncodingError`, because `src/requests/sessions.py` had a matching line (step 6); its outline names every `ChunkedEncodingError` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). Plan by outcome: ok: resolve the sources its import statements name; cap: work the items it opens.

**Call:** `symbols('src/requests/sessions.py', 'ChunkedEncodingError')`

**Response**: outcome `ok`

```
module src/requests/sessions.py lines=921 dynamic=no all=none
30 from ChunkedEncodingError <- .exceptions ChunkedEncodingError
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/requests/sessions.py",
    "ChunkedEncodingError"
   ],
   "desc": "outline `src/requests/sessions.py` for its `ChunkedEncodingError` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/requests/sessions.py', 'ChunkedEncodingError')",
   "key": "[\"symbols\", [\"src/requests/sessions.py\", \"ChunkedEncodingError\"]]",
   "v1": [
    907423,
    542400
   ],
   "v2": [
    907423,
    542400
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "src/requests/sessions.py",
     "ChunkedEncodingError"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/requests/sessions.py', 'ChunkedEncodingError')",
  "key": "[\"symbols\", [\"src/requests/sessions.py\", \"ChunkedEncodingError\"]]",
  "provenance": "`src/requests/sessions.py` had a matching line (step 6); its outline names every `ChunkedEncodingError` import exactly",
  "v2": [
   907423,
   542400
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
 "adherence": {
  "planned": "[\"symbols\", [\"src/requests/sessions.py\", \"ChunkedEncodingError\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 8,
   "path": "src/requests/sessions.py",
   "filter": "ChunkedEncodingError",
   "header": {
    "lines": 921,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/requests/sessions.py",
     "name": "ChunkedEncodingError",
     "line": 30,
     "kind": "from",
     "src": ".exceptions",
     "src_name": "ChunkedEncodingError",
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
    "src/requests/models.py",
    57,
    "in",
    "`.exceptions` resolves `ChunkedEncodingError` to the target"
   ],
   [
    "src/requests/sessions.py",
    30,
    "in",
    "`.exceptions` resolves `ChunkedEncodingError` to the target"
   ],
   [
    "tests/test_requests.py",
    33,
    "in",
    "`requests.exceptions` resolves `ChunkedEncodingError` to the target"
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

Certificate complete. 3 import statements import this definition: `src/requests/models.py:57`, `src/requests/sessions.py:30`, `tests/test_requests.py:33`. In hindsight, 1 of 8 calls were not needed for the certificate: steps 1.

**Answer:** `{"target": {"kind": "def", "path": "src/requests/exceptions.py", "line": 130, "name": "ChunkedEncodingError", "detail": "class"}, "text": "src/requests/exceptions.py:130", "statements": ["src/requests/models.py:57", "src/requests/sessions.py:30", "tests/test_requests.py:33"], "count": 3}`  
**Stopped:** certificate after 8 calls