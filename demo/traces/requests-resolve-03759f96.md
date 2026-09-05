# requests-resolve-03759f96

**Repository:** requests  
**Family:** resolve  
**Seed:** 0, prior 89d4e155c6e8b2e4

## Task

In `tests/test_utils.py`, line 16 imports `to_native_string` from `requests.utils`. Under the declared semantics, which definition does the module-level name `to_native_string` bound by this statement resolve to? Answer with `path:line`.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

Nothing seen yet beyond the task text.

Chain: `tests/test_utils.py` is not yet closed for `to_native_string`.

Outstanding: close the namespace of `tests/test_utils.py` for `to_native_string`.

Next: outline `tests/test_utils.py`, because module `tests/test_utils.py` (task). I expect: a definition there ends the chain (about 85%); a capped outline means filtering by name (about 15%); no binding at all points at a submodule or an unresolved name (under 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `tests/test_utils.py` filtered to `to_native_string`, is expected to open more follow-up work. Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done; cap: outline `tests/test_utils.py` filtered to `to_native_string`.

**Call:** `symbols('tests/test_utils.py')`

**Response** (capped): outcome `cap`

```
module tests/test_utils.py lines=1014 dynamic=no all=none
1 import copy <- copy
2 import filecmp <- filecmp
3 import os <- os
4 import tarfile <- tarfile
5 import zipfile <- zipfile
6 from deque <- collections deque
7 from BytesIO <- io BytesIO
8 from mock <- unittest mock
10 import pytest <- pytest
12 from compat <- requests compat
13 from unicode_is_ascii <- requests._internal_utils unicode_is_ascii
14 from RequestsCookieJar <- requests.cookies RequestsCookieJar
15 from CaseInsensitiveDict <- requests.structures CaseInsensitiveDict
16 from _parse_content_type_header <- requests.utils _parse_content_type_header
16 from add_dict_to_cookiejar <- requests.utils add_dict_to_cookiejar
16 from address_in_network <- requests.utils address_in_network
16 from dotted_netmask <- requests.utils dotted_netmask
16 from extract_zipped_paths <- requests.utils extract_zipped_paths
16 from get_auth_from_url <- requests.utils get_auth_from_url
16 from get_encoding_from_headers <- requests.utils get_encoding_from_headers
16 from get_encodings_from_content <- requests.utils get_encodings_from_content
16 from get_environ_proxies <- requests.utils get_environ_proxies
16 from get_netrc_auth <- requests.utils get_netrc_auth
16 from guess_filename <- requests.utils guess_filename
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
    "tests/test_utils.py",
    "to_native_string"
   ],
   "desc": "close the namespace of `tests/test_utils.py` for `to_native_string`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/test_utils.py')",
   "key": "[\"symbols\", [\"tests/test_utils.py\"]]",
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
     "tests/test_utils.py",
     "to_native_string"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_utils.py', 'to_native_string')",
   "key": "[\"symbols\", [\"tests/test_utils.py\", \"to_native_string\"]]",
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
     "tests/test_utils.py",
     "to_native_string"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_utils.py')",
  "key": "[\"symbols\", [\"tests/test_utils.py\"]]",
  "provenance": "module `tests/test_utils.py` (task)",
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
  "cap": "[\"symbols\", [\"tests/test_utils.py\", \"to_native_string\"]]"
 },
 "adherence": null,
 "facts": [
  {
   "kind": "outline",
   "step": 1,
   "path": "tests/test_utils.py",
   "filter": null,
   "header": {
    "lines": 1014,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_utils.py",
     "name": "copy",
     "line": 1,
     "kind": "import",
     "src": "copy",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_utils.py",
     "name": "filecmp",
     "line": 2,
     "kind": "import",
     "src": "filecmp",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_utils.py",
     "name": "os",
     "line": 3,
     "kind": "import",
     "src": "os",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_utils.py",
     "name": "tarfile",
     "line": 4,
     "kind": "import",
     "src": "tarfile",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_utils.py",
     "name": "zipfile",
     "line": 5,
     "kind": "import",
     "src": "zipfile",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_utils.py",
     "name": "deque",
     "line": 6,
     "kind": "from",
     "src": "collections",
     "src_name": "deque",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_utils.py",
     "name": "BytesIO",
     "line": 7,
     "kind": "from",
     "src": "io",
     "src_name": "BytesIO",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_utils.py",
     "name": "mock",
     "line": 8,
     "kind": "from",
     "src": "unittest",
     "src_name": "mock",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_utils.py",
     "name": "pytest",
     "line": 10,
     "kind": "import",
     "src": "pytest",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_utils.py",
     "name": "compat",
     "line": 12,
     "kind": "from",
     "src": "requests",
     "src_name": "compat",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_utils.py",
     "name": "unicode_is_ascii",
     "line": 13,
     "kind": "from",
     "src": "requests._internal_utils",
     "src_name": "unicode_is_ascii",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_utils.py",
     "name": "RequestsCookieJar",
     "line": 14,
     "kind": "from",
     "src": "requests.cookies",
     "src_name": "RequestsCookieJar",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_utils.py",
     "name": "CaseInsensitiveDict",
     "line": 15,
     "kind": "from",
     "src": "requests.structures",
     "src_name": "CaseInsensitiveDict",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_utils.py",
     "name": "_parse_content_type_header",
     "line": 16,
     "kind": "from",
     "src": "requests.utils",
     "src_name": "_parse_content_type_header",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_utils.py",
     "name": "add_dict_to_cookiejar",
     "line": 16,
     "kind": "from",
     "src": "requests.utils",
     "src_name": "add_dict_to_cookiejar",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_utils.py",
     "name": "address_in_network",
     "line": 16,
     "kind": "from",
     "src": "requests.utils",
     "src_name": "address_in_network",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_utils.py",
     "name": "dotted_netmask",
     "line": 16,
     "kind": "from",
     "src": "requests.utils",
     "src_name": "dotted_netmask",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_utils.py",
     "name": "extract_zipped_paths",
     "line": 16,
     "kind": "from",
     "src": "requests.utils",
     "sr
```
</details>

## Step 2

The outline of `tests/test_utils.py` has 40 bindings (capped, so this is only the start of the file); no `__all__`; no dynamic namespace tricks.

Chain: `tests/test_utils.py` is not yet closed for `to_native_string`.

Still to settle: close the namespace of `tests/test_utils.py` for `to_native_string`.

Next: outline `tests/test_utils.py` filtered to `to_native_string`, because module `tests/test_utils.py` (task), name `to_native_string` (task). I expect: a re-export continues the chain to its source (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a definition there ends the chain (under 5%); no binding but a star import means checking what that source exports (under 5%). Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done.

**Call:** `symbols('tests/test_utils.py', 'to_native_string')`

**Response**: outcome `reexport`

```
module tests/test_utils.py lines=1014 dynamic=no all=none
16 from to_native_string <- requests.utils to_native_string
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "tests/test_utils.py",
    "to_native_string"
   ],
   "desc": "close the namespace of `tests/test_utils.py` for `to_native_string`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/test_utils.py', 'to_native_string')",
   "key": "[\"symbols\", [\"tests/test_utils.py\", \"to_native_string\"]]",
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
     "tests/test_utils.py",
     "to_native_string"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_utils.py', 'to_native_string')",
  "key": "[\"symbols\", [\"tests/test_utils.py\", \"to_native_string\"]]",
  "provenance": "module `tests/test_utils.py` (task), name `to_native_string` (task)",
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
  "planned": "[\"symbols\", [\"tests/test_utils.py\", \"to_native_string\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 2,
   "path": "tests/test_utils.py",
   "filter": "to_native_string",
   "header": {
    "lines": 1014,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_utils.py",
     "name": "to_native_string",
     "line": 16,
     "kind": "from",
     "src": "requests.utils",
     "src_name": "to_native_string",
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
    "tests/test_utils.py",
    "to_native_string",
    "reexport",
    [
     "requests.utils",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 3

In `tests/test_utils.py`, `to_native_string` has exactly one binding: line 16 imports it as `to_native_string` from `requests.utils`. No dynamic namespace tricks, no `__all__`.

Chain: `tests/test_utils.py` takes `to_native_string` from `requests.utils` (module not yet located).

Outstanding: locate the module `requests.utils` imported by `tests/test_utils.py`.

Next: grep `def`/`class to_native_string` statements under `.`, because a `def`/`class to_native_string` statement would reveal the module file; `to_native_string` task. I expect: hits under the cap (about 95%); a capped result (about 5%); no hits (about 5%). The alternative, list `.`, is more likely to hit the cap (about 20% against about 5%). Plan by outcome: zero: outline `requests/utils.py` filtered to `to_native_string`; mid: outline each module that appears; cap: outline `requests/utils.py` filtered to `to_native_string`.

**Call:** `grep('^\\s*(?:async\\s+)?(?:def|class)\\s+to_native_string\\b', '.')`

**Response**: outcome `mid`

```
src/requests/_internal_utils.py:26:def to_native_string(string: str | bytes, encoding: str = "ascii") -> str:
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_utils.py",
    "requests.utils"
   ],
   "desc": "locate the module `requests.utils` imported by `tests/test_utils.py`"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+to_native_string\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+to_native_string\\\\b\", \".\"]]",
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
     "tests/test_utils.py",
     "requests.utils"
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
     "tests/test_utils.py",
     "requests.utils"
    ]
   ]
  },
  {
   "call": "symbols('requests/utils.py', 'to_native_string')",
   "key": "[\"symbols\", [\"requests/utils.py\", \"to_native_string\"]]",
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
     "tests/test_utils.py",
     "requests.utils"
    ]
   ]
  },
  {
   "call": "symbols('requests/utils/__init__.py', 'to_native_string')",
   "key": "[\"symbols\", [\"requests/utils/__init__.py\", \"to_native_string\"]]",
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
     "tests/test_utils.py",
     "requests.utils"
    ]
   ]
  }
 ],
 "choice": {
  "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+to_native_string\\\\b', '.')",
  "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+to_native_string\\\\b\", \".\"]]",
  "provenance": "a `def`/`class to_native_string` statement would reveal the module file; `to_native_string` task",
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
  "zero": "[\"symbols\", [\"requests/utils.py\", \"to_native_string\"]]",
  "mid": "continue",
  "cap": "[\"symbols\", [\"requests/utils.py\", \"to_native_string\"]]"
 },
 "adherence": {
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "grep",
   "step": 3,
   "pattern": "^\\s*(?:async\\s+)?(?:def|class)\\s+to_native_string\\b",
   "scope": ".",
   "hits": [
    [
     "src/requests/_internal_utils.py",
     26
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "chain": [
   [
    "tests/test_utils.py",
    "to_native_string",
    "reexport",
    [
     "requests.utils",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 4

The grep under `.` returned 1 lines, under the cap, so these are all of them: `src/requests/_internal_utils.py`.

Chain: `tests/test_utils.py` takes `to_native_string` from `requests.utils` (module not yet located).

Outstanding: locate the module `requests.utils` imported by `tests/test_utils.py`.

Next: list `.`, because `requests.utils` imported by `tests/test_utils.py` should live under `.`. I expect: a complete listing settles which files exist (about 80%); a capped listing settles nothing (about 20%). The alternative, outline `requests/utils.py` filtered to `to_native_string`, costs more in expectation. Plan by outcome: complete: outline the module it reveals; cap: outline `requests/utils.py` filtered to `to_native_string`.

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
    "tests/test_utils.py",
    "requests.utils"
   ],
   "desc": "locate the module `requests.utils` imported by `tests/test_utils.py`"
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
     "tests/test_utils.py",
     "requests.utils"
    ]
   ]
  },
  {
   "call": "symbols('requests/utils.py', 'to_native_string')",
   "key": "[\"symbols\", [\"requests/utils.py\", \"to_native_string\"]]",
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
     "tests/test_utils.py",
     "requests.utils"
    ]
   ]
  },
  {
   "call": "symbols('requests/utils/__init__.py', 'to_native_string')",
   "key": "[\"symbols\", [\"requests/utils/__init__.py\", \"to_native_string\"]]",
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
     "tests/test_utils.py",
     "requests.utils"
    ]
   ]
  }
 ],
 "choice": {
  "call": "ls('.')",
  "key": "[\"ls\", [\".\"]]",
  "provenance": "`requests.utils` imported by `tests/test_utils.py` should live under `.`",
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
  "cap": "[\"symbols\", [\"requests/utils.py\", \"to_native_string\"]]"
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
    "tests/test_utils.py",
    "to_native_string",
    "reexport",
    [
     "requests.utils",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 5

`.` lists 14 entries (complete): `.github/`, `docs/`, `setup.py`, `src/`, `tests/`.

Chain: `tests/test_utils.py` takes `to_native_string` from `requests.utils` (module not yet located).

Still to settle: locate the module `requests.utils` imported by `tests/test_utils.py`.

Next: outline `src/requests/utils.py` filtered to `to_native_string`, because `requests.utils` would be `src/requests/utils.py` if that file exists; one call both checks and closes it. I expect: a definition there ends the chain (about 85%); the file does not exist (about 10%); no binding at all points at a submodule or an unresolved name (under 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, list `src/requests`, is expected to open more follow-up work. Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done; missing: list `src/requests`.

**Call:** `symbols('src/requests/utils.py', 'to_native_string')`

**Response**: outcome `reexport`

```
module src/requests/utils.py lines=1156 dynamic=no all=none
39 from to_native_string <- ._internal_utils to_native_string
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_utils.py",
    "requests.utils"
   ],
   "desc": "locate the module `requests.utils` imported by `tests/test_utils.py`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/requests/utils.py', 'to_native_string')",
   "key": "[\"symbols\", [\"src/requests/utils.py\", \"to_native_string\"]]",
   "v1": [
    71446961347,
    56440411258
   ],
   "v2": [
    35805357479,
    28220205629
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     18160,
     21479
    ],
    "reexport": [
     1816,
     236269
    ],
    "star": [
     454,
     236269
    ],
    "none": [
     5448,
     236269
    ],
    "missing": [
     63,
     517
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_utils.py",
     "requests.utils"
    ]
   ]
  },
  {
   "call": "ls('src/requests')",
   "key": "[\"ls\", [\"src/requests\"]]",
   "v1": [
    4855,
    2373
   ],
   "v2": [
    2403598522013,
    1185248636418
   ],
   "p_cap": [
    1,
    42
   ],
   "forecast": {
    "complete": [
     41,
     42
    ],
    "cap": [
     1,
     42
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_utils.py",
     "requests.utils"
    ]
   ]
  },
  {
   "call": "symbols('src/requests/utils/__init__.py', 'to_native_string')",
   "key": "[\"symbols\", [\"src/requests/utils/__init__.py\", \"to_native_string\"]]",
   "v1": [
    143678473,
    48839956
   ],
   "v2": [
    2525616678124151,
    1108828319574668
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     126,
     5687
    ],
    "reexport": [
     357,
     5687
    ],
    "star": [
     21,
     11374
    ],
    "none": [
     399,
     11374
    ],
    "missing": [
     454,
     517
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_utils.py",
     "requests.utils"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/requests/utils.py', 'to_native_string')",
  "key": "[\"symbols\", [\"src/requests/utils.py\", \"to_native_string\"]]",
  "provenance": "`requests.utils` would be `src/requests/utils.py` if that file exists; one call both checks and closes it",
  "v2": [
   35805357479,
   28220205629
  ]
 },
 "forecast": {
  "def": [
   18160,
   21479
  ],
  "reexport": [
   1816,
   236269
  ],
  "star": [
   454,
   236269
  ],
  "none": [
   5448,
   236269
  ],
  "missing": [
   63,
   517
  ]
 },
 "plan": {
  "def": "done",
  "reexport": "continue",
  "star": "continue",
  "none": "done",
  "missing": "[\"ls\", [\"src/requests\"]]"
 },
 "adherence": {
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 5,
   "path": "src/requests/utils.py",
   "filter": "to_native_string",
   "header": {
    "lines": 1156,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/requests/utils.py",
     "name": "to_native_string",
     "line": 39,
     "kind": "from",
     "src": "._internal_utils",
     "src_name": "to_native_string",
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
    "tests/test_utils.py",
    "to_native_string",
    "reexport",
    [
     "requests.utils",
     "src/requests/utils.py"
    ]
   ],
   [
    "src/requests/utils.py",
    "to_native_string",
    "reexport",
    [
     "._internal_utils",
     "src/requests/_internal_utils.py"
    ]
   ],
   [
    "src/requests/_internal_utils.py",
    "to_native_string",
    "open",
    null
   ]
  ]
 }
}
```
</details>

## Step 6

In `src/requests/utils.py`, `to_native_string` has exactly one binding: line 39 imports it as `to_native_string` from `._internal_utils`. No dynamic namespace tricks, no `__all__`.

Chain: `tests/test_utils.py` takes `to_native_string` from `requests.utils` (`src/requests/utils.py`); `src/requests/utils.py` takes `to_native_string` from `._internal_utils` (`src/requests/_internal_utils.py`); `src/requests/_internal_utils.py` is not yet closed for `to_native_string`.

Open: close the namespace of `src/requests/_internal_utils.py` for `to_native_string`.

Next: outline `src/requests/_internal_utils.py` filtered to `to_native_string`, because module `src/requests/_internal_utils.py` (step 3), name `to_native_string` (task). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `src/requests/_internal_utils.py`, is more likely to hit the cap (about 15% against under 5%). Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done.

**Call:** `symbols('src/requests/_internal_utils.py', 'to_native_string')`

**Response**: outcome `def`

```
module src/requests/_internal_utils.py lines=52 dynamic=no all=none
26 def to_native_string
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/requests/_internal_utils.py",
    "to_native_string"
   ],
   "desc": "close the namespace of `src/requests/_internal_utils.py` for `to_native_string`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/requests/_internal_utils.py', 'to_native_string')",
   "key": "[\"symbols\", [\"src/requests/_internal_utils.py\", \"to_native_string\"]]",
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
     "src/requests/_internal_utils.py",
     "to_native_string"
    ]
   ]
  },
  {
   "call": "symbols('src/requests/_internal_utils.py')",
   "key": "[\"symbols\", [\"src/requests/_internal_utils.py\"]]",
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
     "src/requests/_internal_utils.py",
     "to_native_string"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/requests/_internal_utils.py', 'to_native_string')",
  "key": "[\"symbols\", [\"src/requests/_internal_utils.py\", \"to_native_string\"]]",
  "provenance": "module `src/requests/_internal_utils.py` (step 3), name `to_native_string` (task)",
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
   "step": 6,
   "path": "src/requests/_internal_utils.py",
   "filter": "to_native_string",
   "header": {
    "lines": 52,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/requests/_internal_utils.py",
     "name": "to_native_string",
     "line": 26,
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
    "tests/test_utils.py",
    "to_native_string",
    "reexport",
    [
     "requests.utils",
     "src/requests/utils.py"
    ]
   ],
   [
    "src/requests/utils.py",
    "to_native_string",
    "reexport",
    [
     "._internal_utils",
     "src/requests/_internal_utils.py"
    ]
   ],
   [
    "src/requests/_internal_utils.py",
    "to_native_string",
    "def",
    26
   ]
  ]
 }
}
```
</details>

## Final

Certificate complete. The name resolves to `src/requests/_internal_utils.py:26`. In hindsight, 1 of 6 calls were not needed for the certificate: steps 1.

**Answer:** `{"target": {"kind": "def", "path": "src/requests/_internal_utils.py", "line": 26, "name": "to_native_string", "detail": "def"}, "text": "src/requests/_internal_utils.py:26"}`  
**Stopped:** certificate after 6 calls