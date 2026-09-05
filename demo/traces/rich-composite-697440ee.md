# rich-composite-697440ee

**Repository:** rich  
**Family:** composite  
**Seed:** 0, prior 6d694b621dbf13a2

## Task

In `tests/test_syntax.py`, line 14 imports `Color` from `rich.syntax`. Under the declared semantics, which definition does the module-level name `Color` bound by this statement resolve to? Answer with `path:line`. Then list every module-level import statement in the snapshot that imports that definition (from-imports naming it, directly or with `as`, and star imports of modules that export it), as `path:line` entries.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

Nothing seen yet beyond the task text.

Chain: `tests/test_syntax.py` is not yet closed for `Color`.

Outstanding: close the namespace of `tests/test_syntax.py` for `Color`.

Next: outline `tests/test_syntax.py`, because module `tests/test_syntax.py` (task). I expect: a definition there ends the chain (about 80%); a capped outline means filtering by name (about 15%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `tests/test_syntax.py` filtered to `Color`, is expected to open more follow-up work. Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done; cap: outline `tests/test_syntax.py` filtered to `Color`.

**Call:** `symbols('tests/test_syntax.py')`

**Response** (capped): outcome `cap`

```
module tests/test_syntax.py lines=454 dynamic=no all=none
1 import io <- io
2 import os <- os
3 import sys <- sys
4 import tempfile <- tempfile
5 from Distribution <- importlib.metadata Distribution
7 import pytest <- pytest
8 from PythonLexer <- pygments.lexers PythonLexer
10 from Console <- rich.console Console
11 from Measurement <- rich.measure Measurement
12 from Panel <- rich.panel Panel
13 from Style <- rich.style Style
14 from ANSISyntaxTheme <- rich.syntax ANSISyntaxTheme
14 from Color <- rich.syntax Color
14 from PygmentsSyntaxTheme <- rich.syntax PygmentsSyntaxTheme
14 from Syntax <- rich.syntax Syntax
14 from _SyntaxHighlightRange <- rich.syntax _SyntaxHighlightRange
22 from render <- .render render
24 assign PYGMENTS_VERSION
25 assign OLD_PYGMENTS
27 assign CODE
43 def test_blank_lines
56 def test_python_render
75 def test_python_render_simple
90 def test_python_render_simple_passing_lexer_instance
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
    "tests/test_syntax.py",
    "Color"
   ],
   "desc": "close the namespace of `tests/test_syntax.py` for `Color`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/test_syntax.py')",
   "key": "[\"symbols\", [\"tests/test_syntax.py\"]]",
   "v1": [
    11114712068,
    9252541277
   ],
   "v2": [
    1027294644842,
    693940595775
   ],
   "p_cap": [
    131,
    881
   ],
   "forecast": {
    "def": [
     330000,
     413189
    ],
    "reexport": [
     8250,
     413189
    ],
    "star": [
     750,
     413189
    ],
    "none": [
     12750,
     413189
    ],
    "cap": [
     131,
     881
    ]
   },
   "serves": [
    [
     "bindings",
     "tests/test_syntax.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_syntax.py', 'Color')",
   "key": "[\"symbols\", [\"tests/test_syntax.py\", \"Color\"]]",
   "v1": [
    4920253,
    1679475
   ],
   "v2": [
    4920253,
    1679475
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
     "tests/test_syntax.py",
     "Color"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_syntax.py')",
  "key": "[\"symbols\", [\"tests/test_syntax.py\"]]",
  "provenance": "module `tests/test_syntax.py` (task)",
  "v2": [
   1027294644842,
   693940595775
  ]
 },
 "forecast": {
  "def": [
   330000,
   413189
  ],
  "reexport": [
   8250,
   413189
  ],
  "star": [
   750,
   413189
  ],
  "none": [
   12750,
   413189
  ],
  "cap": [
   131,
   881
  ]
 },
 "plan": {
  "def": "done",
  "reexport": "continue",
  "star": "continue",
  "none": "done",
  "cap": "[\"symbols\", [\"tests/test_syntax.py\", \"Color\"]]"
 },
 "adherence": null,
 "facts": [
  {
   "kind": "outline",
   "step": 1,
   "path": "tests/test_syntax.py",
   "filter": null,
   "header": {
    "lines": 454,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_syntax.py",
     "name": "io",
     "line": 1,
     "kind": "import",
     "src": "io",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_syntax.py",
     "name": "os",
     "line": 2,
     "kind": "import",
     "src": "os",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_syntax.py",
     "name": "sys",
     "line": 3,
     "kind": "import",
     "src": "sys",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_syntax.py",
     "name": "tempfile",
     "line": 4,
     "kind": "import",
     "src": "tempfile",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_syntax.py",
     "name": "Distribution",
     "line": 5,
     "kind": "from",
     "src": "importlib.metadata",
     "src_name": "Distribution",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_syntax.py",
     "name": "pytest",
     "line": 7,
     "kind": "import",
     "src": "pytest",
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_syntax.py",
     "name": "PythonLexer",
     "line": 8,
     "kind": "from",
     "src": "pygments.lexers",
     "src_name": "PythonLexer",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_syntax.py",
     "name": "Console",
     "line": 10,
     "kind": "from",
     "src": "rich.console",
     "src_name": "Console",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_syntax.py",
     "name": "Measurement",
     "line": 11,
     "kind": "from",
     "src": "rich.measure",
     "src_name": "Measurement",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_syntax.py",
     "name": "Panel",
     "line": 12,
     "kind": "from",
     "src": "rich.panel",
     "src_name": "Panel",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_syntax.py",
     "name": "Style",
     "line": 13,
     "kind": "from",
     "src": "rich.style",
     "src_name": "Style",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_syntax.py",
     "name": "ANSISyntaxTheme",
     "line": 14,
     "kind": "from",
     "src": "rich.syntax",
     "src_name": "ANSISyntaxTheme",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_syntax.py",
     "name": "Color",
     "line": 14,
     "kind": "from",
     "src": "rich.syntax",
     "src_name": "Color",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_syntax.py",
     "name": "PygmentsSyntaxTheme",
     "line": 14,
     "kind": "from",
     "src": "rich.syntax",
     "src_name": "PygmentsSyntaxTheme",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_syntax.py",
     "name": "Syntax",
     "line": 14,
     "kind": "from",
     "src": "rich.syntax",
     "src_name": "Syntax",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_syntax.py",
     "name": "_SyntaxHighlightRange",
     "line": 14,
     "kind": "from",
     "src": "rich.syntax",
     "src_name": "_SyntaxHighlightRange",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_syntax.py",
     "name": "render",
     "line": 22,
     "kind": "from",
     "src": ".render",
     "src_name": "render",
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_syntax.py",
     "name": "PYGMENTS_VERSION",
     "line": 24,
     "kind": "assign",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0
    },
    {
     "module": "tests/test_syntax.py",
     "name": "OLD_PYG
```
</details>

## Step 2

The outline of `tests/test_syntax.py` has 40 bindings (capped, so this is only the start of the file); no `__all__`; no dynamic namespace tricks.

Chain: `tests/test_syntax.py` is not yet closed for `Color`.

Still to settle: close the namespace of `tests/test_syntax.py` for `Color`.

Next: outline `tests/test_syntax.py` filtered to `Color`, because module `tests/test_syntax.py` (task), name `Color` (task). I expect: a re-export continues the chain to its source (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a definition there ends the chain (under 5%); no binding but a star import means checking what that source exports (under 5%). Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done.

**Call:** `symbols('tests/test_syntax.py', 'Color')`

**Response**: outcome `reexport`

```
module tests/test_syntax.py lines=454 dynamic=no all=none
14 from Color <- rich.syntax Color
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "tests/test_syntax.py",
    "Color"
   ],
   "desc": "close the namespace of `tests/test_syntax.py` for `Color`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/test_syntax.py', 'Color')",
   "key": "[\"symbols\", [\"tests/test_syntax.py\", \"Color\"]]",
   "v1": [
    4920253,
    1679475
   ],
   "v2": [
    4920253,
    1679475
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
     "tests/test_syntax.py",
     "Color"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_syntax.py', 'Color')",
  "key": "[\"symbols\", [\"tests/test_syntax.py\", \"Color\"]]",
  "provenance": "module `tests/test_syntax.py` (task), name `Color` (task)",
  "v2": [
   4920253,
   1679475
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
  "planned": "[\"symbols\", [\"tests/test_syntax.py\", \"Color\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 2,
   "path": "tests/test_syntax.py",
   "filter": "Color",
   "header": {
    "lines": 454,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_syntax.py",
     "name": "Color",
     "line": 14,
     "kind": "from",
     "src": "rich.syntax",
     "src_name": "Color",
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
    "tests/test_syntax.py",
    "Color",
    "reexport",
    [
     "rich.syntax",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 3

In `tests/test_syntax.py`, `Color` has exactly one binding: line 14 imports it as `Color` from `rich.syntax`. No dynamic namespace tricks, no `__all__`.

Chain: `tests/test_syntax.py` takes `Color` from `rich.syntax` (module not yet located).

Outstanding: locate the module `rich.syntax` imported by `tests/test_syntax.py`.

Next: grep `def`/`class Color` statements under `.`, because a `def`/`class Color` statement would reveal the module file; `Color` task. I expect: hits under the cap (about 95%); a capped result (about 5%); no hits (about 5%). The alternative, list `.`, costs more in expectation. Plan by outcome: zero: list `.`; mid: outline each module that appears; cap: list `.`.

**Call:** `grep('^\\s*(?:async\\s+)?(?:def|class)\\s+Color\\b', '.')`

**Response**: outcome `mid`

```
rich/color.py:303:class Color(NamedTuple):
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_syntax.py",
    "rich.syntax"
   ],
   "desc": "locate the module `rich.syntax` imported by `tests/test_syntax.py`"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+Color\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+Color\\\\b\", \".\"]]",
   "v1": [
    17341,
    8226
   ],
   "v2": [
    78263,
    37017
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
     "tests/test_syntax.py",
     "rich.syntax"
    ]
   ]
  },
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    8899,
    4113
   ],
   "v2": [
    160639,
    74034
   ],
   "p_cap": [
    1,
    9
   ],
   "forecast": {
    "complete": [
     8,
     9
    ],
    "cap": [
     1,
     9
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_syntax.py",
     "rich.syntax"
    ]
   ]
  },
  {
   "call": "symbols('rich/syntax.py', 'Color')",
   "key": "[\"symbols\", [\"rich/syntax.py\", \"Color\"]]",
   "v1": [
    21676611139,
    9506097216
   ],
   "v2": [
    264009691951,
    114073166592
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     1165,
     3216
    ],
    "reexport": [
     233,
     25728
    ],
    "star": [
     233,
     283008
    ],
    "none": [
     3961,
     283008
    ],
    "missing": [
     2593,
     4224
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_syntax.py",
     "rich.syntax"
    ]
   ]
  },
  {
   "call": "symbols('rich/syntax/__init__.py', 'Color')",
   "key": "[\"symbols\", [\"rich/syntax/__init__.py\", \"Color\"]]",
   "v1": [
    3032096453,
    1003791360
   ],
   "v2": [
    27764979817,
    9034122240
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     217,
     27456
    ],
    "reexport": [
     1519,
     54912
    ],
    "star": [
     217,
     274560
    ],
    "none": [
     4123,
     274560
    ],
    "missing": [
     4007,
     4224
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_syntax.py",
     "rich.syntax"
    ]
   ]
  }
 ],
 "choice": {
  "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+Color\\\\b', '.')",
  "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+Color\\\\b\", \".\"]]",
  "provenance": "a `def`/`class Color` statement would reveal the module file; `Color` task",
  "v2": [
   78263,
   37017
  ]
 },
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
   "pattern": "^\\s*(?:async\\s+)?(?:def|class)\\s+Color\\b",
   "scope": ".",
   "hits": [
    [
     "rich/color.py",
     303
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "chain": [
   [
    "tests/test_syntax.py",
    "Color",
    "reexport",
    [
     "rich.syntax",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 4

The grep under `.` returned 1 lines, under the cap, so these are all of them: `rich/color.py`.

Chain: `tests/test_syntax.py` takes `Color` from `rich.syntax` (module not yet located).

Outstanding: locate the module `rich.syntax` imported by `tests/test_syntax.py`.

Next: outline `rich/syntax.py` filtered to `Color`, because `rich.syntax` would be `rich/syntax.py` if that file exists; one call both checks and closes it. I expect: a definition there ends the chain (about 85%); the file does not exist (about 10%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, list `rich`, is expected to open more follow-up work. Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done; missing: list `rich`.

**Call:** `symbols('rich/syntax.py', 'Color')`

**Response**: outcome `reexport`

```
module rich/syntax.py lines=989 dynamic=no all=none
50 from Color <- .color Color
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_syntax.py",
    "rich.syntax"
   ],
   "desc": "locate the module `rich.syntax` imported by `tests/test_syntax.py`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('rich/syntax.py', 'Color')",
   "key": "[\"symbols\", [\"rich/syntax.py\", \"Color\"]]",
   "v1": [
    5354257399,
    4158917532
   ],
   "v2": [
    172312952249,
    133085361024
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     1165,
     1407
    ],
    "reexport": [
     233,
     11256
    ],
    "star": [
     233,
     123816
    ],
    "none": [
     3961,
     123816
    ],
    "missing": [
     31,
     264
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_syntax.py",
     "rich.syntax"
    ]
   ]
  },
  {
   "call": "ls('rich')",
   "key": "[\"ls\", [\"rich\"]]",
   "v1": [
    15465,
    7312
   ],
   "v2": [
    137556872251,
    66542680512
   ],
   "p_cap": [
    1,
    16
   ],
   "forecast": {
    "complete": [
     15,
     16
    ],
    "cap": [
     1,
     16
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_syntax.py",
     "rich.syntax"
    ]
   ]
  },
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    8899,
    4113
   ],
   "v2": [
    77803146835,
    37430257788
   ],
   "p_cap": [
    1,
    9
   ],
   "forecast": {
    "complete": [
     8,
     9
    ],
    "cap": [
     1,
     9
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_syntax.py",
     "rich.syntax"
    ]
   ]
  },
  {
   "call": "symbols('rich/syntax/__init__.py', 'Color')",
   "key": "[\"symbols\", [\"rich/syntax/__init__.py\", \"Color\"]]",
   "v1": [
    1308546053,
    439158720
   ],
   "v2": [
    328917263002091,
    142734049698240
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     31,
     1716
    ],
    "reexport": [
     217,
     3432
    ],
    "star": [
     31,
     17160
    ],
    "none": [
     589,
     17160
    ],
    "missing": [
     233,
     264
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_syntax.py",
     "rich.syntax"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('rich/syntax.py', 'Color')",
  "key": "[\"symbols\", [\"rich/syntax.py\", \"Color\"]]",
  "provenance": "`rich.syntax` would be `rich/syntax.py` if that file exists; one call both checks and closes it",
  "v2": [
   172312952249,
   133085361024
  ]
 },
 "forecast": {
  "def": [
   1165,
   1407
  ],
  "reexport": [
   233,
   11256
  ],
  "star": [
   233,
   123816
  ],
  "none": [
   3961,
   123816
  ],
  "missing": [
   31,
   264
  ]
 },
 "plan": {
  "def": "done",
  "reexport": "continue",
  "star": "continue",
  "none": "done",
  "missing": "[\"ls\", [\"rich\"]]"
 },
 "adherence": {
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 4,
   "path": "rich/syntax.py",
   "filter": "Color",
   "header": {
    "lines": 989,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "rich/syntax.py",
     "name": "Color",
     "line": 50,
     "kind": "from",
     "src": ".color",
     "src_name": "Color",
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
    "tests/test_syntax.py",
    "Color",
    "reexport",
    [
     "rich.syntax",
     "rich/syntax.py"
    ]
   ],
   [
    "rich/syntax.py",
    "Color",
    "reexport",
    [
     ".color",
     "rich/color.py"
    ]
   ],
   [
    "rich/color.py",
    "Color",
    "open",
    null
   ]
  ]
 }
}
```
</details>

## Step 5

In `rich/syntax.py`, `Color` has exactly one binding: line 50 imports it as `Color` from `.color`. No dynamic namespace tricks, no `__all__`.

Chain: `tests/test_syntax.py` takes `Color` from `rich.syntax` (`rich/syntax.py`); `rich/syntax.py` takes `Color` from `.color` (`rich/color.py`); `rich/color.py` is not yet closed for `Color`.

Still to settle: close the namespace of `rich/color.py` for `Color`.

Next: outline `rich/color.py` filtered to `Color`, because module `rich/color.py` (step 3), name `Color` (task). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `rich/color.py`, is more likely to hit the cap (about 15% against under 5%). Plan by outcome: def: done; reexport: locate and outline the source it names; star: check what the star source exports; none: done.

**Call:** `symbols('rich/color.py', 'Color')`

**Response**: outcome `def`

```
module rich/color.py lines=622 dynamic=no all=none
303 class Color
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "rich/color.py",
    "Color"
   ],
   "desc": "close the namespace of `rich/color.py` for `Color`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('rich/color.py', 'Color')",
   "key": "[\"symbols\", [\"rich/color.py\", \"Color\"]]",
   "v1": [
    3566693,
    3358950
   ],
   "v2": [
    3566693,
    3358950
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
     "rich/color.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/color.py')",
   "key": "[\"symbols\", [\"rich/color.py\"]]",
   "v1": [
    11114712068,
    9252541277
   ],
   "v2": [
    1669132492777,
    1387881191550
   ],
   "p_cap": [
    131,
    881
   ],
   "forecast": {
    "def": [
     330000,
     413189
    ],
    "reexport": [
     8250,
     413189
    ],
    "star": [
     750,
     413189
    ],
    "none": [
     12750,
     413189
    ],
    "cap": [
     131,
     881
    ]
   },
   "serves": [
    [
     "bindings",
     "rich/color.py",
     "Color"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('rich/color.py', 'Color')",
  "key": "[\"symbols\", [\"rich/color.py\", \"Color\"]]",
  "provenance": "module `rich/color.py` (step 3), name `Color` (task)",
  "v2": [
   3566693,
   3358950
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
   "path": "rich/color.py",
   "filter": "Color",
   "header": {
    "lines": 622,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "rich/color.py",
     "name": "Color",
     "line": 303,
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
    "tests/test_syntax.py",
    "Color",
    "reexport",
    [
     "rich.syntax",
     "rich/syntax.py"
    ]
   ],
   [
    "rich/syntax.py",
    "Color",
    "reexport",
    [
     ".color",
     "rich/color.py"
    ]
   ],
   [
    "rich/color.py",
    "Color",
    "class",
    303
   ]
  ]
 }
}
```
</details>

## Step 6

In `rich/color.py`, `Color` has exactly one binding: a class at line 303. No dynamic namespace tricks, no `__all__`. This is not the branch I planned for that outcome; the open items changed more than expected.

Candidate modules so far: 0; statements confirmed: 0, ruled out: 0, modules with no such import: 0, pending: 0. import coverage open at `.`; star coverage open at `.`.

Open: cover `.` for import lines; cover `.` for star lines.

Next: grep from-imports naming `Color` or star imports under `.`, because import and star lines under `.` in one call. I expect: hits under the cap (about 70%); no hits (about 25%); a capped result (about 10%). The alternative, grep from-imports naming `Color` under `.`, serves fewer of the open items. Plan by outcome: zero: done; mid: outline each module that appears; cap: list the scope and split it.

**Call:** `grep('^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bColor\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*Color\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$', '.')`

**Response**: outcome `mid`

```
benchmarks/benchmarks.py:4:from rich.color import Color, ColorSystem
examples/bars.py:10:from rich.color import Color
rich/__main__.py:6:from rich.color import Color
rich/ansi.py:6:from .color import Color
rich/bar.py:3:from .color import Color
rich/palette.py:21:        from rich.color import Color
rich/palette.py:78:    from rich.color import Color
rich/progress_bar.py:6:from .color import Color, blend_rgb
rich/style.py:10:from .color import Color, ColorParseError, ColorSystem, blend_rgb
rich/syntax.py:50:from .color import Color, blend_rgb
tests/test_color.py:4:    Color,
tests/test_style.py:4:from rich.color import Color, ColorSystem, ColorType
tests/test_syntax.py:16:    Color,
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
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bColor\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*Color\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bColor\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*Color\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
   "v1": [
    395661216193,
    63414176875
   ],
   "v2": [
    395661216193,
    63414176875
   ],
   "p_cap": [
    3,
    35
   ],
   "forecast": {
    "zero": [
     8,
     35
    ],
    "mid": [
     24,
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
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bColor\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*Color\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bColor\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*Color\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
   "v1": [
    17117047510677,
    2168402482400
   ],
   "v2": [
    17117047510677,
    2168402482400
   ],
   "p_cap": [
    1,
    32
   ],
   "forecast": {
    "zero": [
     3,
     4
    ],
    "mid": [
     7,
     32
    ],
    "cap": [
     1,
     32
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
    17117047510677,
    2168402482400
   ],
   "v2": [
    17117047510677,
    2168402482400
   ],
   "p_cap": [
    2,
    33
   ],
   "forecast": {
    "zero": [
     13,
     33
    ],
    "mid": [
     6,
     11
    ],
    "cap": [
     2,
     33
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
  "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bColor\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*Color\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
  "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bColor\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*Color\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
  "provenance": "import and star lines under `.` in one call",
  "v2": [
   395661216193,
   63414176875
  ]
 },
 "forecast": {
  "zero": [
   8,
   35
  ],
  "mid": [
   24,
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
   "pattern": "^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bColor\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*Color\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$",
   "scope": ".",
   "hits": [
    [
     "benchmarks/benchmarks.py",
     4
    ],
    [
     "examples/bars.py",
     10
    ],
    [
     "rich/__main__.py",
     6
    ],
    [
     "rich/ansi.py",
     6
    ],
    [
     "rich/bar.py",
     3
    ],
    [
     "rich/palette.py",
     21
    ],
    [
     "rich/palette.py",
     78
    ],
    [
     "rich/progress_bar.py",
     6
    ],
    [
     "rich/style.py",
     10
    ],
    [
     "rich/syntax.py",
     50
    ],
    [
     "tests/test_color.py",
     4
    ],
    [
     "tests/test_style.py",
     4
    ],
    [
     "tests/test_syntax.py",
     16
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "verdicts": [
   [
    "benchmarks/benchmarks.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "examples/bars.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "rich/__main__.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "rich/ansi.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "rich/bar.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "rich/palette.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "rich/progress_bar.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "rich/style.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "rich/syntax.py",
    50,
    "in",
    "`.color` resolves `Color` to the target"
   ],
   [
    "tests/test_color.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_style.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_syntax.py",
    14,
    "in",
    "`rich.syntax` resolves `Color` to the target"
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

The grep under `.` returned 13 lines, under the cap, so these are all of them: `benchmarks/benchmarks.py`, `examples/bars.py`, `rich/__main__.py`, `rich/ansi.py` and 8 more files.

Candidate modules so far: 12; statements confirmed: 2, ruled out: 0, modules with no such import: 0, pending: 10. import coverage complete; star coverage complete.

Open: outline `benchmarks/benchmarks.py` for its `Color` imports; outline `examples/bars.py` for its `Color` imports; outline `rich/__main__.py` for its `Color` imports; outline `rich/ansi.py` for its `Color` imports; and 6 more.

Next: outline `tests/test_style.py` filtered to `Color`, because `tests/test_style.py` had a matching line (step 6); its outline names every `Color` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `benchmarks/benchmarks.py` filtered to `Color`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `benchmarks/benchmarks.py` filtered to `Color`; cap: outline `benchmarks/benchmarks.py` filtered to `Color`.

**Call:** `symbols('tests/test_style.py', 'Color')`

**Response**: outcome `ok`

```
module tests/test_style.py lines=268 dynamic=no all=none
4 from Color <- rich.color Color
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "benchmarks/benchmarks.py",
    "Color"
   ],
   "desc": "outline `benchmarks/benchmarks.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "examples/bars.py",
    "Color"
   ],
   "desc": "outline `examples/bars.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/__main__.py",
    "Color"
   ],
   "desc": "outline `rich/__main__.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/ansi.py",
    "Color"
   ],
   "desc": "outline `rich/ansi.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/bar.py",
    "Color"
   ],
   "desc": "outline `rich/bar.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/palette.py",
    "Color"
   ],
   "desc": "outline `rich/palette.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/progress_bar.py",
    "Color"
   ],
   "desc": "outline `rich/progress_bar.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/style.py",
    "Color"
   ],
   "desc": "outline `rich/style.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_color.py",
    "Color"
   ],
   "desc": "outline `tests/test_color.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_style.py",
    "Color"
   ],
   "desc": "outline `tests/test_style.py` for its `Color` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('benchmarks/benchmarks.py', 'Color')",
   "key": "[\"symbols\", [\"benchmarks/benchmarks.py\", \"Color\"]]",
   "v1": [
    414681,
    22850
   ],
   "v2": [
    207569,
    11425
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "benchmarks/benchmarks.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('examples/bars.py', 'Color')",
   "key": "[\"symbols\", [\"examples/bars.py\", \"Color\"]]",
   "v1": [
    414681,
    22850
   ],
   "v2": [
    207569,
    11425
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "examples/bars.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/__main__.py', 'Color')",
   "key": "[\"symbols\", [\"rich/__main__.py\", \"Color\"]]",
   "v1": [
    414681,
    22850
   ],
   "v2": [
    207569,
    11425
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/__main__.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/ansi.py', 'Color')",
   "key": "[\"symbols\", [\"rich/ansi.py\", \"Color\"]]",
   "v1": [
    414681,
    22850
   ],
   "v2": [
    207569,
    11425
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/ansi.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/bar.py', 'Color')",
   "key": "[\"symbols\", [\"rich/bar.py\", \"Color\"]]",
   "v1": [
    414681,
    22850
   ],
   "v2": [
    207569,
    11425
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/bar.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/palette.py', 'Color')",
   "key": "[\"symbols\", [\"rich/palette.py\", \"Color\"]]",
   "v1": [
    414681,
    22850
   ],
   "v2": [
    207569,
    11425
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/palette.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/progress_bar.py', 'Color')",
   "key": "[\"symbols\", [\"rich/progress_bar.py\", \"Color\"]]",
   "v1": [
    414681,
    22850
   ],
   "v2": [
    207569,
    11425
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/progress_bar.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/style.py', 'Color')",
   "key": "[\"symbols\", [\"rich/style.py\", \"Color\"]]",
   "v1": [
    414681,
    22850
   ],
   "v2": [
    207569,
    11425
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/style.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_color.py', 'Color')",
   "key": "[\"symbols\", [\"tests/test_color.py\", \"Color\"]]",
   "v1": [
    414681,
    22850
   ],
   "v2": [
    207569,
    11425
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_color.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_style.py', 'Color')",
   "key": "[\"symbols\", [\"tests/test_style.py\", \"Color\"]]",
   "v1": [
    414681,
    22850
   ],
   "v2": [
    207569,
    11425
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_style.py",
     "Color"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_style.py', 'Color')",
  "key": "[\"symbols\", [\"tests/test_style.py\", \"Color\"]]",
  "provenance": "`tests/test
```
</details>

## Step 8

In `tests/test_style.py`, `Color` has exactly one binding: line 4 imports it as `Color` from `rich.color`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 12; statements confirmed: 3, ruled out: 0, modules with no such import: 0, pending: 9. import coverage complete; star coverage complete.

Outstanding: outline `benchmarks/benchmarks.py` for its `Color` imports; outline `examples/bars.py` for its `Color` imports; outline `rich/__main__.py` for its `Color` imports; outline `rich/ansi.py` for its `Color` imports; and 5 more.

Next: outline `benchmarks/benchmarks.py` filtered to `Color`, because `benchmarks/benchmarks.py` had a matching line (step 6); its outline names every `Color` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `examples/bars.py` filtered to `Color`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `examples/bars.py` filtered to `Color`; cap: outline `examples/bars.py` filtered to `Color`.

**Call:** `symbols('benchmarks/benchmarks.py', 'Color')`

**Response**: outcome `ok`

```
module benchmarks/benchmarks.py lines=219 dynamic=no all=none
4 from Color <- rich.color Color
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "benchmarks/benchmarks.py",
    "Color"
   ],
   "desc": "outline `benchmarks/benchmarks.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "examples/bars.py",
    "Color"
   ],
   "desc": "outline `examples/bars.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/__main__.py",
    "Color"
   ],
   "desc": "outline `rich/__main__.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/ansi.py",
    "Color"
   ],
   "desc": "outline `rich/ansi.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/bar.py",
    "Color"
   ],
   "desc": "outline `rich/bar.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/palette.py",
    "Color"
   ],
   "desc": "outline `rich/palette.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/progress_bar.py",
    "Color"
   ],
   "desc": "outline `rich/progress_bar.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/style.py",
    "Color"
   ],
   "desc": "outline `rich/style.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_color.py",
    "Color"
   ],
   "desc": "outline `tests/test_color.py` for its `Color` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('benchmarks/benchmarks.py', 'Color')",
   "key": "[\"symbols\", [\"benchmarks/benchmarks.py\", \"Color\"]]",
   "v1": [
    1866293,
    114250
   ],
   "v2": [
    934289,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "benchmarks/benchmarks.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('examples/bars.py', 'Color')",
   "key": "[\"symbols\", [\"examples/bars.py\", \"Color\"]]",
   "v1": [
    1866293,
    114250
   ],
   "v2": [
    934289,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "examples/bars.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/__main__.py', 'Color')",
   "key": "[\"symbols\", [\"rich/__main__.py\", \"Color\"]]",
   "v1": [
    1866293,
    114250
   ],
   "v2": [
    934289,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/__main__.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/ansi.py', 'Color')",
   "key": "[\"symbols\", [\"rich/ansi.py\", \"Color\"]]",
   "v1": [
    1866293,
    114250
   ],
   "v2": [
    934289,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/ansi.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/bar.py', 'Color')",
   "key": "[\"symbols\", [\"rich/bar.py\", \"Color\"]]",
   "v1": [
    1866293,
    114250
   ],
   "v2": [
    934289,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/bar.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/palette.py', 'Color')",
   "key": "[\"symbols\", [\"rich/palette.py\", \"Color\"]]",
   "v1": [
    1866293,
    114250
   ],
   "v2": [
    934289,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/palette.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/progress_bar.py', 'Color')",
   "key": "[\"symbols\", [\"rich/progress_bar.py\", \"Color\"]]",
   "v1": [
    1866293,
    114250
   ],
   "v2": [
    934289,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/progress_bar.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/style.py', 'Color')",
   "key": "[\"symbols\", [\"rich/style.py\", \"Color\"]]",
   "v1": [
    1866293,
    114250
   ],
   "v2": [
    934289,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/style.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_color.py', 'Color')",
   "key": "[\"symbols\", [\"tests/test_color.py\", \"Color\"]]",
   "v1": [
    1866293,
    114250
   ],
   "v2": [
    934289,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_color.py",
     "Color"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('benchmarks/benchmarks.py', 'Color')",
  "key": "[\"symbols\", [\"benchmarks/benchmarks.py\", \"Color\"]]",
  "provenance": "`benchmarks/benchmarks.py` had a matching line (step 6); its outline names every `Color` import exactly",
  "v2": [
   934289,
   57125
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
  "ok": "[\"symbols\", [\"examples/bars.py\", \"Color\"]]",
  "cap": "[\"symbols\", [\"examples/bars.py\", \"Color\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"benchmarks/benchmarks.py\", \"Color\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 8,
   "path": "benchmarks/benchmarks.py",
   "filter": "Co
```
</details>

## Step 9

In `benchmarks/benchmarks.py`, `Color` has exactly one binding: line 4 imports it as `Color` from `rich.color`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 12; statements confirmed: 4, ruled out: 0, modules with no such import: 0, pending: 8. import coverage complete; star coverage complete.

Still to settle: outline `examples/bars.py` for its `Color` imports; outline `rich/__main__.py` for its `Color` imports; outline `rich/ansi.py` for its `Color` imports; outline `rich/bar.py` for its `Color` imports; and 4 more.

Next: outline `examples/bars.py` filtered to `Color`, because `examples/bars.py` had a matching line (step 6); its outline names every `Color` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `rich/__main__.py` filtered to `Color`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `rich/__main__.py` filtered to `Color`; cap: outline `rich/__main__.py` filtered to `Color`.

**Call:** `symbols('examples/bars.py', 'Color')`

**Response**: outcome `ok`

```
module examples/bars.py lines=22 dynamic=no all=none
10 from Color <- rich.color Color
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "examples/bars.py",
    "Color"
   ],
   "desc": "outline `examples/bars.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/__main__.py",
    "Color"
   ],
   "desc": "outline `rich/__main__.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/ansi.py",
    "Color"
   ],
   "desc": "outline `rich/ansi.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/bar.py",
    "Color"
   ],
   "desc": "outline `rich/bar.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/palette.py",
    "Color"
   ],
   "desc": "outline `rich/palette.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/progress_bar.py",
    "Color"
   ],
   "desc": "outline `rich/progress_bar.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/style.py",
    "Color"
   ],
   "desc": "outline `rich/style.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_color.py",
    "Color"
   ],
   "desc": "outline `tests/test_color.py` for its `Color` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('examples/bars.py', 'Color')",
   "key": "[\"symbols\", [\"examples/bars.py\", \"Color\"]]",
   "v1": [
    1659181,
    114250
   ],
   "v2": [
    830733,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "examples/bars.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/__main__.py', 'Color')",
   "key": "[\"symbols\", [\"rich/__main__.py\", \"Color\"]]",
   "v1": [
    1659181,
    114250
   ],
   "v2": [
    830733,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/__main__.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/ansi.py', 'Color')",
   "key": "[\"symbols\", [\"rich/ansi.py\", \"Color\"]]",
   "v1": [
    1659181,
    114250
   ],
   "v2": [
    830733,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/ansi.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/bar.py', 'Color')",
   "key": "[\"symbols\", [\"rich/bar.py\", \"Color\"]]",
   "v1": [
    1659181,
    114250
   ],
   "v2": [
    830733,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/bar.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/palette.py', 'Color')",
   "key": "[\"symbols\", [\"rich/palette.py\", \"Color\"]]",
   "v1": [
    1659181,
    114250
   ],
   "v2": [
    830733,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/palette.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/progress_bar.py', 'Color')",
   "key": "[\"symbols\", [\"rich/progress_bar.py\", \"Color\"]]",
   "v1": [
    1659181,
    114250
   ],
   "v2": [
    830733,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/progress_bar.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/style.py', 'Color')",
   "key": "[\"symbols\", [\"rich/style.py\", \"Color\"]]",
   "v1": [
    1659181,
    114250
   ],
   "v2": [
    830733,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/style.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_color.py', 'Color')",
   "key": "[\"symbols\", [\"tests/test_color.py\", \"Color\"]]",
   "v1": [
    1659181,
    114250
   ],
   "v2": [
    830733,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_color.py",
     "Color"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('examples/bars.py', 'Color')",
  "key": "[\"symbols\", [\"examples/bars.py\", \"Color\"]]",
  "provenance": "`examples/bars.py` had a matching line (step 6); its outline names every `Color` import exactly",
  "v2": [
   830733,
   57125
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
  "ok": "[\"symbols\", [\"rich/__main__.py\", \"Color\"]]",
  "cap": "[\"symbols\", [\"rich/__main__.py\", \"Color\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"examples/bars.py\", \"Color\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 9,
   "path": "examples/bars.py",
   "filter": "Color",
   "header": {
    "lines": 22,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "examples/bars.py",
     "name": "Color",
     "line": 10,
     "kind": "from",
     "src": "rich.color",
     "src_name": "Color",
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
    "benchmarks/benchmarks.py",
    4,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "examples/bars.py",
    10,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "rich/__main__.py",
    0,
    "pending",
```
</details>

## Step 10

In `examples/bars.py`, `Color` has exactly one binding: line 10 imports it as `Color` from `rich.color`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 12; statements confirmed: 5, ruled out: 0, modules with no such import: 0, pending: 7. import coverage complete; star coverage complete.

Still to settle: outline `rich/__main__.py` for its `Color` imports; outline `rich/ansi.py` for its `Color` imports; outline `rich/bar.py` for its `Color` imports; outline `rich/palette.py` for its `Color` imports; and 3 more.

Next: outline `rich/__main__.py` filtered to `Color`, because `rich/__main__.py` had a matching line (step 6); its outline names every `Color` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `rich/ansi.py` filtered to `Color`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `rich/ansi.py` filtered to `Color`; cap: outline `rich/ansi.py` filtered to `Color`.

**Call:** `symbols('rich/__main__.py', 'Color')`

**Response**: outcome `ok`

```
module rich/__main__.py lines=246 dynamic=no all=none
6 from Color <- rich.color Color
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/__main__.py",
    "Color"
   ],
   "desc": "outline `rich/__main__.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/ansi.py",
    "Color"
   ],
   "desc": "outline `rich/ansi.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/bar.py",
    "Color"
   ],
   "desc": "outline `rich/bar.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/palette.py",
    "Color"
   ],
   "desc": "outline `rich/palette.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/progress_bar.py",
    "Color"
   ],
   "desc": "outline `rich/progress_bar.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/style.py",
    "Color"
   ],
   "desc": "outline `rich/style.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_color.py",
    "Color"
   ],
   "desc": "outline `tests/test_color.py` for its `Color` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('rich/__main__.py', 'Color')",
   "key": "[\"symbols\", [\"rich/__main__.py\", \"Color\"]]",
   "v1": [
    1452069,
    114250
   ],
   "v2": [
    727177,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/__main__.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/ansi.py', 'Color')",
   "key": "[\"symbols\", [\"rich/ansi.py\", \"Color\"]]",
   "v1": [
    1452069,
    114250
   ],
   "v2": [
    727177,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/ansi.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/bar.py', 'Color')",
   "key": "[\"symbols\", [\"rich/bar.py\", \"Color\"]]",
   "v1": [
    1452069,
    114250
   ],
   "v2": [
    727177,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/bar.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/palette.py', 'Color')",
   "key": "[\"symbols\", [\"rich/palette.py\", \"Color\"]]",
   "v1": [
    1452069,
    114250
   ],
   "v2": [
    727177,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/palette.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/progress_bar.py', 'Color')",
   "key": "[\"symbols\", [\"rich/progress_bar.py\", \"Color\"]]",
   "v1": [
    1452069,
    114250
   ],
   "v2": [
    727177,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/progress_bar.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/style.py', 'Color')",
   "key": "[\"symbols\", [\"rich/style.py\", \"Color\"]]",
   "v1": [
    1452069,
    114250
   ],
   "v2": [
    727177,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/style.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_color.py', 'Color')",
   "key": "[\"symbols\", [\"tests/test_color.py\", \"Color\"]]",
   "v1": [
    1452069,
    114250
   ],
   "v2": [
    727177,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_color.py",
     "Color"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('rich/__main__.py', 'Color')",
  "key": "[\"symbols\", [\"rich/__main__.py\", \"Color\"]]",
  "provenance": "`rich/__main__.py` had a matching line (step 6); its outline names every `Color` import exactly",
  "v2": [
   727177,
   57125
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
  "ok": "[\"symbols\", [\"rich/ansi.py\", \"Color\"]]",
  "cap": "[\"symbols\", [\"rich/ansi.py\", \"Color\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"rich/__main__.py\", \"Color\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 10,
   "path": "rich/__main__.py",
   "filter": "Color",
   "header": {
    "lines": 246,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "rich/__main__.py",
     "name": "Color",
     "line": 6,
     "kind": "from",
     "src": "rich.color",
     "src_name": "Color",
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
    "benchmarks/benchmarks.py",
    4,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "examples/bars.py",
    10,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "rich/__main__.py",
    6,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "rich/ansi.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "rich/bar.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "rich/palette.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "rich/progress_bar.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "rich/style.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "rich/syntax.py",
    50,
    "in",
    "`.color` resolves `Color` to the target"
   ],
   [
    "tests/test_color.
```
</details>

## Step 11

In `rich/__main__.py`, `Color` has exactly one binding: line 6 imports it as `Color` from `rich.color`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 12; statements confirmed: 6, ruled out: 0, modules with no such import: 0, pending: 6. import coverage complete; star coverage complete.

Outstanding: outline `rich/ansi.py` for its `Color` imports; outline `rich/bar.py` for its `Color` imports; outline `rich/palette.py` for its `Color` imports; outline `rich/progress_bar.py` for its `Color` imports; and 2 more.

Next: outline `rich/ansi.py` filtered to `Color`, because `rich/ansi.py` had a matching line (step 6); its outline names every `Color` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `rich/bar.py` filtered to `Color`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `rich/bar.py` filtered to `Color`; cap: outline `rich/bar.py` filtered to `Color`.

**Call:** `symbols('rich/ansi.py', 'Color')`

**Response**: outcome `ok`

```
module rich/ansi.py lines=242 dynamic=no all=none
6 from Color <- .color Color
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/ansi.py",
    "Color"
   ],
   "desc": "outline `rich/ansi.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/bar.py",
    "Color"
   ],
   "desc": "outline `rich/bar.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/palette.py",
    "Color"
   ],
   "desc": "outline `rich/palette.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/progress_bar.py",
    "Color"
   ],
   "desc": "outline `rich/progress_bar.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/style.py",
    "Color"
   ],
   "desc": "outline `rich/style.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_color.py",
    "Color"
   ],
   "desc": "outline `tests/test_color.py` for its `Color` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('rich/ansi.py', 'Color')",
   "key": "[\"symbols\", [\"rich/ansi.py\", \"Color\"]]",
   "v1": [
    1244957,
    114250
   ],
   "v2": [
    623621,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/ansi.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/bar.py', 'Color')",
   "key": "[\"symbols\", [\"rich/bar.py\", \"Color\"]]",
   "v1": [
    1244957,
    114250
   ],
   "v2": [
    623621,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/bar.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/palette.py', 'Color')",
   "key": "[\"symbols\", [\"rich/palette.py\", \"Color\"]]",
   "v1": [
    1244957,
    114250
   ],
   "v2": [
    623621,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/palette.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/progress_bar.py', 'Color')",
   "key": "[\"symbols\", [\"rich/progress_bar.py\", \"Color\"]]",
   "v1": [
    1244957,
    114250
   ],
   "v2": [
    623621,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/progress_bar.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/style.py', 'Color')",
   "key": "[\"symbols\", [\"rich/style.py\", \"Color\"]]",
   "v1": [
    1244957,
    114250
   ],
   "v2": [
    623621,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/style.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_color.py', 'Color')",
   "key": "[\"symbols\", [\"tests/test_color.py\", \"Color\"]]",
   "v1": [
    1244957,
    114250
   ],
   "v2": [
    623621,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_color.py",
     "Color"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('rich/ansi.py', 'Color')",
  "key": "[\"symbols\", [\"rich/ansi.py\", \"Color\"]]",
  "provenance": "`rich/ansi.py` had a matching line (step 6); its outline names every `Color` import exactly",
  "v2": [
   623621,
   57125
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
  "ok": "[\"symbols\", [\"rich/bar.py\", \"Color\"]]",
  "cap": "[\"symbols\", [\"rich/bar.py\", \"Color\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"rich/ansi.py\", \"Color\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 11,
   "path": "rich/ansi.py",
   "filter": "Color",
   "header": {
    "lines": 242,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "rich/ansi.py",
     "name": "Color",
     "line": 6,
     "kind": "from",
     "src": ".color",
     "src_name": "Color",
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
    "benchmarks/benchmarks.py",
    4,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "examples/bars.py",
    10,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "rich/__main__.py",
    6,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "rich/ansi.py",
    6,
    "in",
    "`.color` resolves `Color` to the target"
   ],
   [
    "rich/bar.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "rich/palette.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "rich/progress_bar.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "rich/style.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "rich/syntax.py",
    50,
    "in",
    "`.color` resolves `Color` to the target"
   ],
   [
    "tests/test_color.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_style.py",
    4,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "tests/test_syntax.py",
    14,
    "in",
    "`rich.syntax` resolves `Color` to the target"
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

## Step 12

In `rich/ansi.py`, `Color` has exactly one binding: line 6 imports it as `Color` from `.color`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 12; statements confirmed: 7, ruled out: 0, modules with no such import: 0, pending: 5. import coverage complete; star coverage complete.

Open: outline `rich/bar.py` for its `Color` imports; outline `rich/palette.py` for its `Color` imports; outline `rich/progress_bar.py` for its `Color` imports; outline `rich/style.py` for its `Color` imports; and 1 more.

Next: outline `rich/bar.py` filtered to `Color`, because `rich/bar.py` had a matching line (step 6); its outline names every `Color` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `rich/palette.py` filtered to `Color`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `rich/palette.py` filtered to `Color`; cap: outline `rich/palette.py` filtered to `Color`.

**Call:** `symbols('rich/bar.py', 'Color')`

**Response**: outcome `ok`

```
module rich/bar.py lines=94 dynamic=no all=none
3 from Color <- .color Color
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/bar.py",
    "Color"
   ],
   "desc": "outline `rich/bar.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/palette.py",
    "Color"
   ],
   "desc": "outline `rich/palette.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/progress_bar.py",
    "Color"
   ],
   "desc": "outline `rich/progress_bar.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/style.py",
    "Color"
   ],
   "desc": "outline `rich/style.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_color.py",
    "Color"
   ],
   "desc": "outline `tests/test_color.py` for its `Color` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('rich/bar.py', 'Color')",
   "key": "[\"symbols\", [\"rich/bar.py\", \"Color\"]]",
   "v1": [
    207569,
    22850
   ],
   "v2": [
    104013,
    11425
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/bar.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/palette.py', 'Color')",
   "key": "[\"symbols\", [\"rich/palette.py\", \"Color\"]]",
   "v1": [
    207569,
    22850
   ],
   "v2": [
    104013,
    11425
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/palette.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/progress_bar.py', 'Color')",
   "key": "[\"symbols\", [\"rich/progress_bar.py\", \"Color\"]]",
   "v1": [
    207569,
    22850
   ],
   "v2": [
    104013,
    11425
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/progress_bar.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/style.py', 'Color')",
   "key": "[\"symbols\", [\"rich/style.py\", \"Color\"]]",
   "v1": [
    207569,
    22850
   ],
   "v2": [
    104013,
    11425
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/style.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_color.py', 'Color')",
   "key": "[\"symbols\", [\"tests/test_color.py\", \"Color\"]]",
   "v1": [
    207569,
    22850
   ],
   "v2": [
    104013,
    11425
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_color.py",
     "Color"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('rich/bar.py', 'Color')",
  "key": "[\"symbols\", [\"rich/bar.py\", \"Color\"]]",
  "provenance": "`rich/bar.py` had a matching line (step 6); its outline names every `Color` import exactly",
  "v2": [
   104013,
   11425
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
  "ok": "[\"symbols\", [\"rich/palette.py\", \"Color\"]]",
  "cap": "[\"symbols\", [\"rich/palette.py\", \"Color\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"rich/bar.py\", \"Color\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 12,
   "path": "rich/bar.py",
   "filter": "Color",
   "header": {
    "lines": 94,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "rich/bar.py",
     "name": "Color",
     "line": 3,
     "kind": "from",
     "src": ".color",
     "src_name": "Color",
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
    "benchmarks/benchmarks.py",
    4,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "examples/bars.py",
    10,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "rich/__main__.py",
    6,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "rich/ansi.py",
    6,
    "in",
    "`.color` resolves `Color` to the target"
   ],
   [
    "rich/bar.py",
    3,
    "in",
    "`.color` resolves `Color` to the target"
   ],
   [
    "rich/palette.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "rich/progress_bar.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "rich/style.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "rich/syntax.py",
    50,
    "in",
    "`.color` resolves `Color` to the target"
   ],
   [
    "tests/test_color.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_style.py",
    4,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "tests/test_syntax.py",
    14,
    "in",
    "`rich.syntax` resolves `Color` to the target"
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

## Step 13

In `rich/bar.py`, `Color` has exactly one binding: line 3 imports it as `Color` from `.color`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 12; statements confirmed: 8, ruled out: 0, modules with no such import: 0, pending: 4. import coverage complete; star coverage complete.

Outstanding: outline `rich/palette.py` for its `Color` imports; outline `rich/progress_bar.py` for its `Color` imports; outline `rich/style.py` for its `Color` imports; outline `tests/test_color.py` for its `Color` imports.

Next: outline `rich/palette.py` filtered to `Color`, because `rich/palette.py` had a matching line (step 6); its outline names every `Color` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `rich/progress_bar.py` filtered to `Color`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `rich/progress_bar.py` filtered to `Color`; cap: outline `rich/progress_bar.py` filtered to `Color`.

**Call:** `symbols('rich/palette.py', 'Color')`

**Response**: outcome `ok`

```
module rich/palette.py lines=101 dynamic=no all=none
78 from Color <- rich.color Color
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/palette.py",
    "Color"
   ],
   "desc": "outline `rich/palette.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/progress_bar.py",
    "Color"
   ],
   "desc": "outline `rich/progress_bar.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/style.py",
    "Color"
   ],
   "desc": "outline `rich/style.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_color.py",
    "Color"
   ],
   "desc": "outline `tests/test_color.py` for its `Color` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('rich/palette.py', 'Color')",
   "key": "[\"symbols\", [\"rich/palette.py\", \"Color\"]]",
   "v1": [
    830733,
    114250
   ],
   "v2": [
    416509,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/palette.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/progress_bar.py', 'Color')",
   "key": "[\"symbols\", [\"rich/progress_bar.py\", \"Color\"]]",
   "v1": [
    830733,
    114250
   ],
   "v2": [
    416509,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/progress_bar.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/style.py', 'Color')",
   "key": "[\"symbols\", [\"rich/style.py\", \"Color\"]]",
   "v1": [
    830733,
    114250
   ],
   "v2": [
    416509,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/style.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_color.py', 'Color')",
   "key": "[\"symbols\", [\"tests/test_color.py\", \"Color\"]]",
   "v1": [
    830733,
    114250
   ],
   "v2": [
    416509,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_color.py",
     "Color"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('rich/palette.py', 'Color')",
  "key": "[\"symbols\", [\"rich/palette.py\", \"Color\"]]",
  "provenance": "`rich/palette.py` had a matching line (step 6); its outline names every `Color` import exactly",
  "v2": [
   416509,
   57125
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
  "ok": "[\"symbols\", [\"rich/progress_bar.py\", \"Color\"]]",
  "cap": "[\"symbols\", [\"rich/progress_bar.py\", \"Color\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"rich/palette.py\", \"Color\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 13,
   "path": "rich/palette.py",
   "filter": "Color",
   "header": {
    "lines": 101,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "rich/palette.py",
     "name": "Color",
     "line": 78,
     "kind": "from",
     "src": "rich.color",
     "src_name": "Color",
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
    "benchmarks/benchmarks.py",
    4,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "examples/bars.py",
    10,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "rich/__main__.py",
    6,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "rich/ansi.py",
    6,
    "in",
    "`.color` resolves `Color` to the target"
   ],
   [
    "rich/bar.py",
    3,
    "in",
    "`.color` resolves `Color` to the target"
   ],
   [
    "rich/palette.py",
    78,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "rich/progress_bar.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "rich/style.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "rich/syntax.py",
    50,
    "in",
    "`.color` resolves `Color` to the target"
   ],
   [
    "tests/test_color.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_style.py",
    4,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "tests/test_syntax.py",
    14,
    "in",
    "`rich.syntax` resolves `Color` to the target"
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

In `rich/palette.py`, `Color` has exactly one binding: line 78 imports it as `Color` from `rich.color`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 12; statements confirmed: 9, ruled out: 0, modules with no such import: 0, pending: 3. import coverage complete; star coverage complete.

Open: outline `rich/progress_bar.py` for its `Color` imports; outline `rich/style.py` for its `Color` imports; outline `tests/test_color.py` for its `Color` imports.

Next: outline `rich/progress_bar.py` filtered to `Color`, because `rich/progress_bar.py` had a matching line (step 6); its outline names every `Color` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `rich/style.py` filtered to `Color`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `rich/style.py` filtered to `Color`; cap: outline `rich/style.py` filtered to `Color`.

**Call:** `symbols('rich/progress_bar.py', 'Color')`

**Response**: outcome `ok`

```
module rich/progress_bar.py lines=224 dynamic=no all=none
6 from Color <- .color Color
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/progress_bar.py",
    "Color"
   ],
   "desc": "outline `rich/progress_bar.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/style.py",
    "Color"
   ],
   "desc": "outline `rich/style.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_color.py",
    "Color"
   ],
   "desc": "outline `tests/test_color.py` for its `Color` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('rich/progress_bar.py', 'Color')",
   "key": "[\"symbols\", [\"rich/progress_bar.py\", \"Color\"]]",
   "v1": [
    623621,
    114250
   ],
   "v2": [
    312953,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/progress_bar.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('rich/style.py', 'Color')",
   "key": "[\"symbols\", [\"rich/style.py\", \"Color\"]]",
   "v1": [
    623621,
    114250
   ],
   "v2": [
    312953,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/style.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_color.py', 'Color')",
   "key": "[\"symbols\", [\"tests/test_color.py\", \"Color\"]]",
   "v1": [
    623621,
    114250
   ],
   "v2": [
    312953,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_color.py",
     "Color"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('rich/progress_bar.py', 'Color')",
  "key": "[\"symbols\", [\"rich/progress_bar.py\", \"Color\"]]",
  "provenance": "`rich/progress_bar.py` had a matching line (step 6); its outline names every `Color` import exactly",
  "v2": [
   312953,
   57125
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
  "ok": "[\"symbols\", [\"rich/style.py\", \"Color\"]]",
  "cap": "[\"symbols\", [\"rich/style.py\", \"Color\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"rich/progress_bar.py\", \"Color\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 14,
   "path": "rich/progress_bar.py",
   "filter": "Color",
   "header": {
    "lines": 224,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "rich/progress_bar.py",
     "name": "Color",
     "line": 6,
     "kind": "from",
     "src": ".color",
     "src_name": "Color",
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
    "benchmarks/benchmarks.py",
    4,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "examples/bars.py",
    10,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "rich/__main__.py",
    6,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "rich/ansi.py",
    6,
    "in",
    "`.color` resolves `Color` to the target"
   ],
   [
    "rich/bar.py",
    3,
    "in",
    "`.color` resolves `Color` to the target"
   ],
   [
    "rich/palette.py",
    78,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "rich/progress_bar.py",
    6,
    "in",
    "`.color` resolves `Color` to the target"
   ],
   [
    "rich/style.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "rich/syntax.py",
    50,
    "in",
    "`.color` resolves `Color` to the target"
   ],
   [
    "tests/test_color.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_style.py",
    4,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "tests/test_syntax.py",
    14,
    "in",
    "`rich.syntax` resolves `Color` to the target"
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

In `rich/progress_bar.py`, `Color` has exactly one binding: line 6 imports it as `Color` from `.color`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 12; statements confirmed: 10, ruled out: 0, modules with no such import: 0, pending: 2. import coverage complete; star coverage complete.

Still to settle: outline `rich/style.py` for its `Color` imports; outline `tests/test_color.py` for its `Color` imports.

Next: outline `rich/style.py` filtered to `Color`, because `rich/style.py` had a matching line (step 6); its outline names every `Color` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `tests/test_color.py` filtered to `Color`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `tests/test_color.py` filtered to `Color`; cap: outline `tests/test_color.py` filtered to `Color`.

**Call:** `symbols('rich/style.py', 'Color')`

**Response**: outcome `ok`

```
module rich/style.py lines=797 dynamic=no all=none
10 from Color <- .color Color
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/style.py",
    "Color"
   ],
   "desc": "outline `rich/style.py` for its `Color` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_color.py",
    "Color"
   ],
   "desc": "outline `tests/test_color.py` for its `Color` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('rich/style.py', 'Color')",
   "key": "[\"symbols\", [\"rich/style.py\", \"Color\"]]",
   "v1": [
    416509,
    114250
   ],
   "v2": [
    209397,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/style.py",
     "Color"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_color.py', 'Color')",
   "key": "[\"symbols\", [\"tests/test_color.py\", \"Color\"]]",
   "v1": [
    416509,
    114250
   ],
   "v2": [
    209397,
    57125
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_color.py",
     "Color"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('rich/style.py', 'Color')",
  "key": "[\"symbols\", [\"rich/style.py\", \"Color\"]]",
  "provenance": "`rich/style.py` had a matching line (step 6); its outline names every `Color` import exactly",
  "v2": [
   209397,
   57125
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
  "ok": "[\"symbols\", [\"tests/test_color.py\", \"Color\"]]",
  "cap": "[\"symbols\", [\"tests/test_color.py\", \"Color\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"rich/style.py\", \"Color\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 15,
   "path": "rich/style.py",
   "filter": "Color",
   "header": {
    "lines": 797,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "rich/style.py",
     "name": "Color",
     "line": 10,
     "kind": "from",
     "src": ".color",
     "src_name": "Color",
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
    "benchmarks/benchmarks.py",
    4,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "examples/bars.py",
    10,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "rich/__main__.py",
    6,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "rich/ansi.py",
    6,
    "in",
    "`.color` resolves `Color` to the target"
   ],
   [
    "rich/bar.py",
    3,
    "in",
    "`.color` resolves `Color` to the target"
   ],
   [
    "rich/palette.py",
    78,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "rich/progress_bar.py",
    6,
    "in",
    "`.color` resolves `Color` to the target"
   ],
   [
    "rich/style.py",
    10,
    "in",
    "`.color` resolves `Color` to the target"
   ],
   [
    "rich/syntax.py",
    50,
    "in",
    "`.color` resolves `Color` to the target"
   ],
   [
    "tests/test_color.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_style.py",
    4,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "tests/test_syntax.py",
    14,
    "in",
    "`rich.syntax` resolves `Color` to the target"
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

In `rich/style.py`, `Color` has exactly one binding: line 10 imports it as `Color` from `.color`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 12; statements confirmed: 11, ruled out: 0, modules with no such import: 0, pending: 1. import coverage complete; star coverage complete.

Outstanding: outline `tests/test_color.py` for its `Color` imports.

Next: outline `tests/test_color.py` filtered to `Color`, because `tests/test_color.py` had a matching line (step 6); its outline names every `Color` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). Plan by outcome: ok: resolve the sources its import statements name; cap: work the items it opens.

**Call:** `symbols('tests/test_color.py', 'Color')`

**Response**: outcome `ok`

```
module tests/test_color.py lines=188 dynamic=no all=none
1 from Color <- rich.color Color
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_color.py",
    "Color"
   ],
   "desc": "outline `tests/test_color.py` for its `Color` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/test_color.py', 'Color')",
   "key": "[\"symbols\", [\"tests/test_color.py\", \"Color\"]]",
   "v1": [
    209397,
    114250
   ],
   "v2": [
    209397,
    114250
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_color.py",
     "Color"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_color.py', 'Color')",
  "key": "[\"symbols\", [\"tests/test_color.py\", \"Color\"]]",
  "provenance": "`tests/test_color.py` had a matching line (step 6); its outline names every `Color` import exactly",
  "v2": [
   209397,
   114250
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
  "planned": "[\"symbols\", [\"tests/test_color.py\", \"Color\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 16,
   "path": "tests/test_color.py",
   "filter": "Color",
   "header": {
    "lines": 188,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_color.py",
     "name": "Color",
     "line": 1,
     "kind": "from",
     "src": "rich.color",
     "src_name": "Color",
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
    "benchmarks/benchmarks.py",
    4,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "examples/bars.py",
    10,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "rich/__main__.py",
    6,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "rich/ansi.py",
    6,
    "in",
    "`.color` resolves `Color` to the target"
   ],
   [
    "rich/bar.py",
    3,
    "in",
    "`.color` resolves `Color` to the target"
   ],
   [
    "rich/palette.py",
    78,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "rich/progress_bar.py",
    6,
    "in",
    "`.color` resolves `Color` to the target"
   ],
   [
    "rich/style.py",
    10,
    "in",
    "`.color` resolves `Color` to the target"
   ],
   [
    "rich/syntax.py",
    50,
    "in",
    "`.color` resolves `Color` to the target"
   ],
   [
    "tests/test_color.py",
    1,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "tests/test_style.py",
    4,
    "in",
    "`rich.color` resolves `Color` to the target"
   ],
   [
    "tests/test_syntax.py",
    14,
    "in",
    "`rich.syntax` resolves `Color` to the target"
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

Certificate complete. 12 import statements import this definition: `benchmarks/benchmarks.py:4`, `examples/bars.py:10`, `rich/__main__.py:6`, `rich/ansi.py:6`, `rich/bar.py:3`, `rich/palette.py:78`, `rich/progress_bar.py:6`, `rich/style.py:10`, `rich/syntax.py:50`, `tests/test_color.py:1`, `tests/test_style.py:4`, `tests/test_syntax.py:14`. In hindsight, 1 of 16 calls were not needed for the certificate: steps 1.

**Answer:** `{"target": {"kind": "def", "path": "rich/color.py", "line": 303, "name": "Color", "detail": "class"}, "text": "rich/color.py:303", "statements": ["benchmarks/benchmarks.py:4", "examples/bars.py:10", "rich/__main__.py:6", "rich/ansi.py:6", "rich/bar.py:3", "rich/palette.py:78", "rich/progress_bar.py:6", "rich/style.py:10", "rich/syntax.py:50", "tests/test_color.py:1", "tests/test_style.py:4", "tests/test_syntax.py:14"], "count": 12}`  
**Stopped:** certificate after 16 calls