# pytest-callers-5bdeb4fd

**Repository:** pytest  
**Chain:** resolve → callers  
**Seed:** 0, prior 8e41e8743065d192, floor 7

## Task

In `src/_pytest/deprecated.py` line 17, `PytestRemovedIn10Warning` is imported from `_pytest.warning_types`. Which definition does the module-level name `PytestRemovedIn10Warning` actually refer to? Give `path:line`. Then list every call site of it: bare-name calls whose module-level binding resolves to this definition, as `path:line`.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N; bindings take effect in source order. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. A class derives from a definition when a base written as a bare name or `module.Name` resolves to it. A call site is `name(...)` where the bare name refers to the module-level binding (not a parameter or local). Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

I need to find what `PytestRemovedIn10Warning` really is in `src/_pytest/deprecated.py`: line 17 imports it from `_pytest.warning_types`, so the definition is at least one hop away. Then every real call site of it, which means checking what the name refers to in each file that mentions it.

Next I will check `src/_pytest/deprecated.py` for any other binding of `PytestRemovedIn10Warning` besides the import on line 17; almost certainly the import is the only one, and then `_pytest.warning_types` is the place to follow.

**Call:** `symbols('src/_pytest/deprecated.py', 'PytestRemovedIn10Warning')`

**Response**: outcome `reexport`

```
module src/_pytest/deprecated.py lines=156 dynamic=no all=none
17 from PytestRemovedIn10Warning <- _pytest.warning_types PytestRemovedIn10Warning
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/_pytest/deprecated.py",
    "PytestRemovedIn10Warning"
   ],
   "desc": "check the top-level names of `src/_pytest/deprecated.py` for `PytestRemovedIn10Warning`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/deprecated.py', 'PytestRemovedIn10Warning')",
   "key": "[\"symbols\", [\"src/_pytest/deprecated.py\", \"PytestRemovedIn10Warning\"]]",
   "v1": [
    112899819,
    38706800
   ],
   "v2": [
    112899819,
    38706800
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
     "src/_pytest/deprecated.py",
     "PytestRemovedIn10Warning"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/deprecated.py')",
   "key": "[\"symbols\", [\"src/_pytest/deprecated.py\"]]",
   "v1": [
    19620664413,
    6464035600
   ],
   "v2": [
    19620664413,
    6464035600
   ],
   "p_cap": [
    99,
    835
   ],
   "forecast": {
    "def": [
     184,
     20875
    ],
    "reexport": [
     17112,
     20875
    ],
    "star": [
     184,
     20875
    ],
    "none": [
     184,
     4175
    ],
    "cap": [
     99,
     835
    ]
   },
   "serves": [
    [
     "bindings",
     "src/_pytest/deprecated.py",
     "PytestRemovedIn10Warning"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/_pytest/deprecated.py', 'PytestRemovedIn10Warning')",
  "key": "[\"symbols\", [\"src/_pytest/deprecated.py\", \"PytestRemovedIn10Warning\"]]",
  "provenance": "module `src/_pytest/deprecated.py` (task), name `PytestRemovedIn10Warning` (task)",
  "v2": [
   112899819,
   38706800
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
   "path": "src/_pytest/deprecated.py",
   "filter": "PytestRemovedIn10Warning",
   "header": {
    "lines": 156,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/_pytest/deprecated.py",
     "name": "PytestRemovedIn10Warning",
     "line": 17,
     "kind": "from",
     "src": "_pytest.warning_types",
     "src_name": "PytestRemovedIn10Warning",
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
  "of": 2,
  "chain": [
   [
    "src/_pytest/deprecated.py",
    "PytestRemovedIn10Warning",
    "reexport",
    [
     "_pytest.warning_types",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 2

`src/_pytest/deprecated.py` does not define `PytestRemovedIn10Warning` itself; line 17 imports it from `_pytest.warning_types`.

So far: `src/_pytest/deprecated.py` takes `PytestRemovedIn10Warning` from `_pytest.warning_types`, which I still have to locate.

Let me list `./` to see what lives there; the listing settles whether the import is a module, a package, or not here at all. Very likely the listing fits. If the listing is too long, I will outline `_pytest/warning_types.py` directly, which both checks that the file exists and shows me `PytestRemovedIn10Warning`. I could outline `_pytest/warning_types.py` directly, which both checks that the file exists and shows me `PytestRemovedIn10Warning` instead, but it costs more calls in expectation.

**Call:** `ls('.')`

**Response**: outcome `complete`

```
.github/
.pre-commit-config.yaml
.readthedocs.yaml
CHANGELOG.rst
CODE_OF_CONDUCT.md
CONTRIBUTING.rst
OPENCOLLECTIVE.rst
README.rst
RELEASING.rst
SECURITY.md
TIDELIFT.rst
bench/
changelog/
codecov.yml
doc/
extra/
pyproject.toml
scripts/
src/
testing/
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
    "src/_pytest/deprecated.py",
    "_pytest.warning_types"
   ],
   "desc": "find where `_pytest.warning_types` (imported by `src/_pytest/deprecated.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    5201,
    2778
   ],
   "v2": [
    61929950320999,
    31988350796688
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
     "src/_pytest/deprecated.py",
     "_pytest.warning_types"
    ]
   ]
  },
  {
   "call": "symbols('_pytest/warning_types.py', 'PytestRemovedIn10Warning')",
   "key": "[\"symbols\", [\"_pytest/warning_types.py\", \"PytestRemovedIn10Warning\"]]",
   "v1": [
    16534434977535,
    7108522399264
   ],
   "v2": [
    47315949810685,
    21325567197792
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     6116229,
     18365048
    ],
    "reexport": [
     13869,
     2295631
    ],
    "star": [
     13869,
     18365048
    ],
    "none": [
     152559,
     9182524
    ],
    "missing": [
     25040,
     38909
    ]
   },
   "serves": [
    [
     "module_path",
     "src/_pytest/deprecated.py",
     "_pytest.warning_types"
    ]
   ]
  },
  {
   "call": "symbols('_pytest/warning_types/__init__.py', 'PytestRemovedIn10Warning')",
   "key": "[\"symbols\", [\"_pytest/warning_types/__init__.py\", \"PytestRemovedIn10Warning\"]]",
   "v1": [
    1096473894549,
    363305822789
   ],
   "v2": [
    6233209091449,
    2179834936734
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     79488,
     18248321
    ],
    "reexport": [
     582912,
     18248321
    ],
    "star": [
     13248,
     18248321
    ],
    "none": [
     211968,
     18248321
    ],
    "missing": [
     259115,
     272363
    ]
   },
   "serves": [
    [
     "module_path",
     "src/_pytest/deprecated.py",
     "_pytest.warning_types"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+PytestRemovedIn10Warning\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+PytestRemovedIn10Warning\\\\b\", \".\"]]",
   "v1": [
    1407,
    463
   ],
   "v2": [
    7979,
    2778
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
     "src/_pytest/deprecated.py",
     "_pytest.warning_types"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+PytestRemovedIn10Warning\\\\b', 'src')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+PytestRemovedIn10Warning\\\\b\", \"src\"]]",
   "v1": [
    1407,
    463
   ],
   "v2": [
    7979,
    2778
   ],
   "p_cap": [
    1,
    252
   ],
   "forecast": {
    "zero": [
     107,
     126
    ],
    "mid": [
     37,
     252
    ],
    "cap": [
     1,
     252
    ]
   },
   "serves": [
    [
     "module_path",
     "src/_pytest/deprecated.py",
     "_pytest.warning_types"
    ]
   ]
  }
 ],
 "choice": {
  "call": "ls('.')",
  "key": "[\"ls\", [\".\"]]",
  "provenance": "`_pytest.warning_types` imported by `src/_pytest/deprecated.py` should live under `.`",
  "v2": [
   61929950320999,
   31988350796688
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
  "cap": "[\"symbols\", [\"_pytest/warning_types.py\", \"PytestRemovedIn10Warning\"]]"
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
    ".github/",
    ".pre-commit-config.yaml",
    ".readthedocs.yaml",
    "CHANGELOG.rst",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.rst",
    "OPENCOLLECTIVE.rst",
    "README.rst",
    "RELEASING.rst",
    "SECURITY.md",
    "TIDELIFT.rst",
    "bench/",
    "changelog/",
    "codecov.yml",
    "doc/",
    "extra/",
    "pyproject.toml",
    "scripts/",
    "src/",
    "testing/",
    "tox.ini"
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "resolve",
  "step": 1,
  "of": 2,
  "chain": [
   [
    "src/_pytest/deprecated.py",
    "PytestRemovedIn10Warning",
    "reexport",
    [
     "_pytest.warning_types",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 3

`./` has 21 entries: there is no `_pytest` here.

So far: `src/_pytest/deprecated.py` takes `PytestRemovedIn10Warning` from `_pytest.warning_types`, which I still have to locate.

I'll outline `src/_pytest/warning_types.py` directly, which both checks that the file exists and shows me `PytestRemovedIn10Warning`; if `_pytest.warning_types` is a plain module that is where it has to be. Very likely it is defined right there. If the file does not exist, I will list `src/_pytest/` to see what lives there; if the name is not bound there, that finishes it. I could list `src/_pytest/` to see what lives there instead, but it tends to open more follow-up work.

**Call:** `symbols('src/_pytest/warning_types.py', 'PytestRemovedIn10Warning')`

**Response**: outcome `def`

```
module src/_pytest/warning_types.py lines=167 dynamic=no all=none
53 class PytestRemovedIn10Warning (PytestDeprecationWarning)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "src/_pytest/deprecated.py",
    "_pytest.warning_types"
   ],
   "desc": "find where `_pytest.warning_types` (imported by `src/_pytest/deprecated.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/warning_types.py', 'PytestRemovedIn10Warning')",
   "key": "[\"symbols\", [\"src/_pytest/warning_types.py\", \"PytestRemovedIn10Warning\"]]",
   "v1": [
    124552395191,
    97377019168
   ],
   "v2": [
    19340698905037,
    15093437971040
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     206829,
     251576
    ],
    "reexport": [
     469,
     31447
    ],
    "star": [
     469,
     251576
    ],
    "none": [
     5159,
     125788
    ],
    "missing": [
     64,
     533
    ]
   },
   "serves": [
    [
     "module_path",
     "src/_pytest/deprecated.py",
     "_pytest.warning_types"
    ]
   ]
  },
  {
   "call": "ls('src/_pytest')",
   "key": "[\"ls\", [\"src/_pytest\"]]",
   "v1": [
    147709,
    71765
   ],
   "v2": [
    6168766169729,
    3018687594208
   ],
   "p_cap": [
    3,
    155
   ],
   "forecast": {
    "complete": [
     152,
     155
    ],
    "cap": [
     3,
     155
    ]
   },
   "serves": [
    [
     "module_path",
     "src/_pytest/deprecated.py",
     "_pytest.warning_types"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+PytestRemovedIn10Warning\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+PytestRemovedIn10Warning\\\\b\", \".\"]]",
   "v1": [
    33966,
    16205
   ],
   "v2": [
    699567071019,
    340819567088
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
     "src/_pytest/deprecated.py",
     "_pytest.warning_types"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+PytestRemovedIn10Warning\\\\b', 'src')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+PytestRemovedIn10Warning\\\\b\", \"src\"]]",
   "v1": [
    337433,
    116676
   ],
   "v2": [
    55060794984593,
    24539008830336
   ],
   "p_cap": [
    1,
    252
   ],
   "forecast": {
    "zero": [
     107,
     126
    ],
    "mid": [
     37,
     252
    ],
    "cap": [
     1,
     252
    ]
   },
   "serves": [
    [
     "module_path",
     "src/_pytest/deprecated.py",
     "_pytest.warning_types"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/warning_types/__init__.py', 'PytestRemovedIn10Warning')",
   "key": "[\"symbols\", [\"src/_pytest/warning_types/__init__.py\", \"PytestRemovedIn10Warning\"]]",
   "v1": [
    2123991915,
    710970299
   ],
   "v2": [
    346741840706566563,
    149529521454863264
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     384,
     35711
    ],
    "reexport": [
     2816,
     35711
    ],
    "star": [
     64,
     35711
    ],
    "none": [
     1024,
     35711
    ],
    "missing": [
     469,
     533
    ]
   },
   "serves": [
    [
     "module_path",
     "src/_pytest/deprecated.py",
     "_pytest.warning_types"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/_pytest/warning_types.py', 'PytestRemovedIn10Warning')",
  "key": "[\"symbols\", [\"src/_pytest/warning_types.py\", \"PytestRemovedIn10Warning\"]]",
  "provenance": "`_pytest.warning_types` would be `src/_pytest/warning_types.py` if that file exists; one call both checks and closes it",
  "v2": [
   19340698905037,
   15093437971040
  ]
 },
 "forecast": {
  "def": [
   206829,
   251576
  ],
  "reexport": [
   469,
   31447
  ],
  "star": [
   469,
   251576
  ],
  "none": [
   5159,
   125788
  ],
  "missing": [
   64,
   533
  ]
 },
 "plan": {
  "def": "done",
  "reexport": "continue",
  "star": "continue",
  "none": "done",
  "missing": "[\"ls\", [\"src/_pytest\"]]"
 },
 "hedges": [
  {
   "outcome": "def",
   "word": "very likely",
   "p": [
    206829,
    251576
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
   "step": 3,
   "path": "src/_pytest/warning_types.py",
   "filter": "PytestRemovedIn10Warning",
   "header": {
    "lines": 167,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/_pytest/warning_types.py",
     "name": "PytestRemovedIn10Warning",
     "line": 53,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "PytestDeprecationWarning"
     ]
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "resolve",
  "step": 1,
  "of": 2,
  "chain": [
   [
    "src/_pytest/deprecated.py",
    "PytestRemovedIn10Warning",
    "reexport",
    [
     "_pytest.warning_types",
     "src/_pytest/warning_types.py"
    ]
   ],
   [
    "src/_pytest/warning_types.py",
    "PytestRemovedIn10Warning",
    "class",
    53
   ]
  ]
 }
}
```
</details>

## Step 4

There it is: `PytestRemovedIn10Warning` is a class at `src/_pytest/warning_types.py:53`. That settles the definition; now its call sites.

I'll search the whole tree for calls of `PytestRemovedIn10Warning`; the search has to be complete before I can call the set final. Probably it fits under the cap. If nothing turns up, that finishes it; if it caps, I follow whatever it opens up.

**Call:** `grep('\\bPytestRemovedIn10Warning\\s*\\(', '.')`

**Response**: outcome `mid`

```
src/_pytest/deprecated.py:32:YIELD_FIXTURE = PytestRemovedIn10Warning(
src/_pytest/deprecated.py:59:MONKEYPATCH_LEGACY_NAMESPACE_PACKAGES = PytestRemovedIn10Warning(
src/_pytest/deprecated.py:74:CONSOLE_MAIN = PytestRemovedIn10Warning(
src/_pytest/deprecated.py:80:CONFIG_INICFG = PytestRemovedIn10Warning(
src/_pytest/deprecated.py:93:PASTEBIN = PytestRemovedIn10Warning(
src/_pytest/deprecated.py:99:INI_STRING_TYPE_NON_STR_VALUE = PytestRemovedIn10Warning(
src/_pytest/deprecated.py:126:FIXTURE_BASEID_DEPRECATED = PytestRemovedIn10Warning(
src/_pytest/deprecated.py:130:FIXTURE_NODEID_DEPRECATED = PytestRemovedIn10Warning(
src/_pytest/deprecated.py:135:FIXTUREDEF_HAS_LOCATION_DEPRECATED = PytestRemovedIn10Warning(
src/_pytest/deprecated.py:140:PARSEFACTORIES_NODEID_DEPRECATED = PytestRemovedIn10Warning(
src/_pytest/deprecated.py:145:CALLSPEC2_RENAMED = PytestRemovedIn10Warning(
src/_pytest/warning_types.py:53:class PytestRemovedIn10Warning(PytestDeprecationWarning):
testing/test_warnings.py:578:            warnings.warn(pytest.PytestRemovedIn10Warning("some warning"))
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "cover",
   "key": [
    "cover",
    "CALL",
    "."
   ],
   "desc": "search `.` for calls of `PytestRemovedIn10Warning`"
  }
 ],
 "candidates": [
  {
   "call": "grep('\\\\bPytestRemovedIn10Warning\\\\s*\\\\(', '.')",
   "key": "[\"grep\", [\"\\\\bPytestRemovedIn10Warning\\\\s*\\\\(\", \".\"]]",
   "v1": [
    516664693618,
    383432419825
   ],
   "v2": [
    516664693618,
    383432419825
   ],
   "p_cap": [
    1,
    23
   ],
   "forecast": {
    "zero": [
     11,
     46
    ],
    "mid": [
     33,
     46
    ],
    "cap": [
     1,
     23
    ]
   },
   "serves": [
    [
     "cover",
     "CALL",
     "."
    ]
   ]
  }
 ],
 "choice": {
  "call": "grep('\\\\bPytestRemovedIn10Warning\\\\s*\\\\(', '.')",
  "key": "[\"grep\", [\"\\\\bPytestRemovedIn10Warning\\\\s*\\\\(\", \".\"]]",
  "provenance": "call lines naming `PytestRemovedIn10Warning` under `.` (derived)",
  "v2": [
   516664693618,
   383432419825
  ]
 },
 "forecast": {
  "zero": [
   11,
   46
  ],
  "mid": [
   33,
   46
  ],
  "cap": [
   1,
   23
  ]
 },
 "plan": {
  "zero": "done",
  "mid": "continue",
  "cap": "continue"
 },
 "hedges": [
  {
   "outcome": "mid",
   "word": "probably",
   "p": [
    33,
    46
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
   "step": 4,
   "pattern": "\\bPytestRemovedIn10Warning\\s*\\(",
   "scope": ".",
   "hits": [
    [
     "src/_pytest/deprecated.py",
     32
    ],
    [
     "src/_pytest/deprecated.py",
     59
    ],
    [
     "src/_pytest/deprecated.py",
     74
    ],
    [
     "src/_pytest/deprecated.py",
     80
    ],
    [
     "src/_pytest/deprecated.py",
     93
    ],
    [
     "src/_pytest/deprecated.py",
     99
    ],
    [
     "src/_pytest/deprecated.py",
     126
    ],
    [
     "src/_pytest/deprecated.py",
     130
    ],
    [
     "src/_pytest/deprecated.py",
     135
    ],
    [
     "src/_pytest/deprecated.py",
     140
    ],
    [
     "src/_pytest/deprecated.py",
     145
    ],
    [
     "src/_pytest/warning_types.py",
     53
    ],
    [
     "testing/test_warnings.py",
     578
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "phase": "callers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/_pytest/deprecated.py",
   "src/_pytest/warning_types.py",
   "testing/test_warnings.py"
  ],
  "table": [
   [
    "src/_pytest/deprecated.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/_pytest/warning_types.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "testing/test_warnings.py",
    null,
    "pending",
    "not yet examined"
   ]
  ],
  "uncovered": {
   "CALL": []
  },
  "n_in": 0,
  "n_out": 0,
  "n_pending": 3
 }
}
```
</details>

## Step 5

13 matching lines anywhere for calls of `PytestRemovedIn10Warning`, in `src/_pytest/deprecated.py`, `src/_pytest/warning_types.py`, `testing/test_warnings.py`, and the search was under the cap, so that is the complete set there.

Let me list the call sites of `PytestRemovedIn10Warning` in `src/_pytest/deprecated.py`; the name is ours there, so each call site counts. Almost certainly the call sites fit. If there are too many call sites, I will look at `testing/test_warnings.py`'s top-level names for `PytestRemovedIn10Warning`.

**Call:** `calls('src/_pytest/deprecated.py', 'PytestRemovedIn10Warning')`

**Response**: outcome `ok`

```
calls of PytestRemovedIn10Warning in src/_pytest/deprecated.py count=11
32:YIELD_FIXTURE = PytestRemovedIn10Warning(
59:MONKEYPATCH_LEGACY_NAMESPACE_PACKAGES = PytestRemovedIn10Warning(
74:CONSOLE_MAIN = PytestRemovedIn10Warning(
80:CONFIG_INICFG = PytestRemovedIn10Warning(
93:PASTEBIN = PytestRemovedIn10Warning(
99:INI_STRING_TYPE_NON_STR_VALUE = PytestRemovedIn10Warning(
126:FIXTURE_BASEID_DEPRECATED = PytestRemovedIn10Warning(
130:FIXTURE_NODEID_DEPRECATED = PytestRemovedIn10Warning(
135:FIXTUREDEF_HAS_LOCATION_DEPRECATED = PytestRemovedIn10Warning(
140:PARSEFACTORIES_NODEID_DEPRECATED = PytestRemovedIn10Warning(
145:CALLSPEC2_RENAMED = PytestRemovedIn10Warning(
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/_pytest/deprecated.py",
    "PytestRemovedIn10Warning"
   ],
   "desc": "list the call sites of `PytestRemovedIn10Warning` in `src/_pytest/deprecated.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/_pytest/warning_types.py",
    "PytestRemovedIn10Warning"
   ],
   "desc": "list the call sites of `PytestRemovedIn10Warning` in `src/_pytest/warning_types.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_warnings.py",
    "PytestRemovedIn10Warning"
   ],
   "desc": "check what `PytestRemovedIn10Warning` means inside `testing/test_warnings.py`"
  }
 ],
 "candidates": [
  {
   "call": "calls('src/_pytest/deprecated.py', 'PytestRemovedIn10Warning')",
   "key": "[\"calls\", [\"src/_pytest/deprecated.py\", \"PytestRemovedIn10Warning\"]]",
   "v1": [
    2800911,
    787100
   ],
   "v2": [
    2816653,
    787100
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
     "calls",
     "src/_pytest/deprecated.py",
     "PytestRemovedIn10Warning"
    ]
   ]
  },
  {
   "call": "calls('src/_pytest/warning_types.py', 'PytestRemovedIn10Warning')",
   "key": "[\"calls\", [\"src/_pytest/warning_types.py\", \"PytestRemovedIn10Warning\"]]",
   "v1": [
    2800911,
    787100
   ],
   "v2": [
    2816653,
    787100
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
     "calls",
     "src/_pytest/warning_types.py",
     "PytestRemovedIn10Warning"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_warnings.py', 'PytestRemovedIn10Warning')",
   "key": "[\"symbols\", [\"testing/test_warnings.py\", \"PytestRemovedIn10Warning\"]]",
   "v1": [
    1388649,
    393550
   ],
   "v2": [
    2816653,
    787100
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "testing/test_warnings.py",
     "PytestRemovedIn10Warning"
    ]
   ]
  }
 ],
 "choice": {
  "call": "calls('src/_pytest/deprecated.py', 'PytestRemovedIn10Warning')",
  "key": "[\"calls\", [\"src/_pytest/deprecated.py\", \"PytestRemovedIn10Warning\"]]",
  "provenance": "call sites of `PytestRemovedIn10Warning` in `src/_pytest/deprecated.py` that refer to the module-level binding",
  "v2": [
   2816653,
   787100
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
  "ok": "[\"symbols\", [\"testing/test_warnings.py\", \"PytestRemovedIn10Warning\"]]",
  "cap": "[\"symbols\", [\"testing/test_warnings.py\", \"PytestRemovedIn10Warning\"]]"
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
   "kind": "calls",
   "step": 5,
   "path": "src/_pytest/deprecated.py",
   "name": "PytestRemovedIn10Warning",
   "lines": [
    32,
    59,
    74,
    80,
    93,
    99,
    126,
    130,
    135,
    140,
    145
   ],
   "count": 11,
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "callers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/_pytest/deprecated.py",
   "src/_pytest/warning_types.py",
   "testing/test_warnings.py"
  ],
  "table": [
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:32",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:59",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:74",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:80",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:93",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:99",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:126",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:130",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:135",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:140",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:145",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/warning_types.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "testing/test_warnings.py",
    null,
    "pending",
    "not yet examined"
   ]
  ],
  "uncovered": {
   "CALL": []
  },
  "n_in": 11,
  "n_out": 0,
  "n_pending": 2
 }
}
```
</details>

## Step 6

`src/_pytest/deprecated.py` calls `PytestRemovedIn10Warning` at lines 32, 59, 74, 80, 93, 99 and 5 more, and those are real calls of the module-level name, not a shadowed local.

Tally: 11 call sites confirmed, 0 ruled out, 2 pending. The search itself is complete; what is left is checking the candidates.

Next I will look at `testing/test_warnings.py`'s top-level names for `PytestRemovedIn10Warning`; before counting calls I need to know the name refers to our definition there. Almost certainly the outline shows what I need. If the outline is too long to fit, I will list the call sites of `PytestRemovedIn10Warning` in `src/_pytest/warning_types.py`.

**Call:** `symbols('testing/test_warnings.py', 'PytestRemovedIn10Warning')`

**Response**: outcome `ok`

```
module testing/test_warnings.py lines=1156 dynamic=no all=none
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/_pytest/warning_types.py",
    "PytestRemovedIn10Warning"
   ],
   "desc": "list the call sites of `PytestRemovedIn10Warning` in `src/_pytest/warning_types.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_warnings.py",
    "PytestRemovedIn10Warning"
   ],
   "desc": "check what `PytestRemovedIn10Warning` means inside `testing/test_warnings.py`"
  }
 ],
 "candidates": [
  {
   "call": "calls('src/_pytest/warning_types.py', 'PytestRemovedIn10Warning')",
   "key": "[\"calls\", [\"src/_pytest/warning_types.py\", \"PytestRemovedIn10Warning\"]]",
   "v1": [
    2013811,
    787100
   ],
   "v2": [
    2029553,
    787100
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
     "calls",
     "src/_pytest/warning_types.py",
     "PytestRemovedIn10Warning"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_warnings.py', 'PytestRemovedIn10Warning')",
   "key": "[\"symbols\", [\"testing/test_warnings.py\", \"PytestRemovedIn10Warning\"]]",
   "v1": [
    995099,
    393550
   ],
   "v2": [
    2029553,
    787100
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "testing/test_warnings.py",
     "PytestRemovedIn10Warning"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('testing/test_warnings.py', 'PytestRemovedIn10Warning')",
  "key": "[\"symbols\", [\"testing/test_warnings.py\", \"PytestRemovedIn10Warning\"]]",
  "provenance": "`testing/test_warnings.py` had a matching line (step 4); its outline names every `PytestRemovedIn10Warning` import exactly",
  "v2": [
   2029553,
   787100
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
  "ok": "[\"calls\", [\"src/_pytest/warning_types.py\", \"PytestRemovedIn10Warning\"]]",
  "cap": "[\"calls\", [\"src/_pytest/warning_types.py\", \"PytestRemovedIn10Warning\"]]"
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
  "planned": "[\"symbols\", [\"testing/test_warnings.py\", \"PytestRemovedIn10Warning\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 6,
   "path": "testing/test_warnings.py",
   "filter": "PytestRemovedIn10Warning",
   "header": {
    "lines": 1156,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "callers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/_pytest/deprecated.py",
   "src/_pytest/warning_types.py",
   "testing/test_warnings.py"
  ],
  "table": [
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:32",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:59",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:74",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:80",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:93",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:99",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:126",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:130",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:135",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:140",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:145",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/warning_types.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "testing/test_warnings.py",
    "testing/test_warnings.py",
    "out",
    "the name is not bound at module level here"
   ]
  ],
  "uncovered": {
   "CALL": []
  },
  "n_in": 11,
  "n_out": 1,
  "n_pending": 1
 }
}
```
</details>

## Step 7

The test module `testing/test_warnings.py` does not bind `PytestRemovedIn10Warning` at module level at all, so its matches were false positives.

Tally: 11 call sites confirmed, 1 ruled out, 1 pending. The search itself is complete; what is left is checking the candidates.

Next I will list the call sites of `PytestRemovedIn10Warning` in `src/_pytest/warning_types.py`; the name is ours there, so each call site counts. Almost certainly the call sites fit. If there are too many call sites, I follow whatever it opens up.

**Call:** `calls('src/_pytest/warning_types.py', 'PytestRemovedIn10Warning')`

**Response**: outcome `ok`

```
calls of PytestRemovedIn10Warning in src/_pytest/warning_types.py count=0
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/_pytest/warning_types.py",
    "PytestRemovedIn10Warning"
   ],
   "desc": "list the call sites of `PytestRemovedIn10Warning` in `src/_pytest/warning_types.py`"
  }
 ],
 "candidates": [
  {
   "call": "calls('src/_pytest/warning_types.py', 'PytestRemovedIn10Warning')",
   "key": "[\"calls\", [\"src/_pytest/warning_types.py\", \"PytestRemovedIn10Warning\"]]",
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
     "calls",
     "src/_pytest/warning_types.py",
     "PytestRemovedIn10Warning"
    ]
   ]
  }
 ],
 "choice": {
  "call": "calls('src/_pytest/warning_types.py', 'PytestRemovedIn10Warning')",
  "key": "[\"calls\", [\"src/_pytest/warning_types.py\", \"PytestRemovedIn10Warning\"]]",
  "provenance": "call sites of `PytestRemovedIn10Warning` in `src/_pytest/warning_types.py` that refer to the module-level binding",
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
  "planned": "[\"calls\", [\"src/_pytest/warning_types.py\", \"PytestRemovedIn10Warning\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "calls",
   "step": 7,
   "path": "src/_pytest/warning_types.py",
   "name": "PytestRemovedIn10Warning",
   "lines": [],
   "count": 0,
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "callers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/_pytest/deprecated.py",
   "src/_pytest/warning_types.py",
   "testing/test_warnings.py"
  ],
  "table": [
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:32",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:59",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:74",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:80",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:93",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:99",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:126",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:130",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:135",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:140",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/deprecated.py",
    "src/_pytest/deprecated.py:145",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/_pytest/warning_types.py",
    "src/_pytest/warning_types.py",
    "out",
    "the module binds the name but never calls it by bare name"
   ],
   [
    "testing/test_warnings.py",
    "testing/test_warnings.py",
    "out",
    "the name is not bound at module level here"
   ]
  ],
  "uncovered": {
   "CALL": []
  },
  "n_in": 11,
  "n_out": 2,
  "n_pending": 0
 }
}
```
</details>

## Final

`PytestRemovedIn10Warning` is the class at `src/_pytest/warning_types.py:53`. 11 call sites in 1 modules: `src/_pytest/deprecated.py:32`, `src/_pytest/deprecated.py:59`, `src/_pytest/deprecated.py:74`, `src/_pytest/deprecated.py:80`, `src/_pytest/deprecated.py:93`, `src/_pytest/deprecated.py:99`, `src/_pytest/deprecated.py:126`, `src/_pytest/deprecated.py:130`, `src/_pytest/deprecated.py:135`, `src/_pytest/deprecated.py:140` and 1 more. Ruled out along the way: `src/_pytest/warning_types.py` (the module binds the name but never calls it by bare name); `testing/test_warnings.py` (the name is not bound at module level here). Looking back, all 7 calls were needed.

**Answer:** `{"final_kind": "callers", "final": ["src/_pytest/deprecated.py:32", "src/_pytest/deprecated.py:59", "src/_pytest/deprecated.py:74", "src/_pytest/deprecated.py:80", "src/_pytest/deprecated.py:93", "src/_pytest/deprecated.py:99", "src/_pytest/deprecated.py:126", "src/_pytest/deprecated.py:130", "src/_pytest/deprecated.py:135", "src/_pytest/deprecated.py:140", "src/_pytest/deprecated.py:145"], "steps": [{"op": "resolve", "output": {"kind": "def", "path": "src/_pytest/warning_types.py", "line": 53, "name": "PytestRemovedIn10Warning", "detail": "class"}}, {"op": "callers", "output": ["src/_pytest/deprecated.py:32", "src/_pytest/deprecated.py:59", "src/_pytest/deprecated.py:74", "src/_pytest/deprecated.py:80", "src/_pytest/deprecated.py:93", "src/_pytest/deprecated.py:99", "src/_pytest/deprecated.py:126", "src/_pytest/deprecated.py:130", "src/_pytest/deprecated.py:135", "src/_pytest/deprecated.py:140", "src/_pytest/deprecated.py:145"]}], "stuck": null}`  
**Stopped:** certificate after 7 calls