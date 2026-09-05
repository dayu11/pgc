# rich-cover-ad4aa569

**Repository:** rich  
**Family:** cover  
**Seed:** 0, prior 6d694b621dbf13a2

## Task

`ColorSystem` is defined at `rich/color.py:21` (class). List every module-level import statement in the snapshot that imports this definition: `from ... import` statements naming it (directly or with `as`), and star imports of modules that export it. Answer as `path:line` entries.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

Nothing seen yet beyond the task text.

Candidate modules so far: 0; statements confirmed: 0, ruled out: 0, modules with no such import: 0, pending: 0. import coverage open at `.`; star coverage open at `.`.

Outstanding: cover `.` for import lines; cover `.` for star lines.

Next: grep from-imports naming `ColorSystem` or star imports under `.`, because import and star lines under `.` in one call. I expect: hits under the cap (about 70%); no hits (about 25%); a capped result (about 10%). The alternative, grep from-imports naming `ColorSystem` under `.`, serves fewer of the open items. Plan by outcome: zero: done; mid: outline each module that appears; cap: list the scope and split it.

**Call:** `grep('^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bColorSystem\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*ColorSystem\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$', '.')`

**Response**: outcome `mid`

```
benchmarks/benchmarks.py:4:from rich.color import Color, ColorSystem
rich/_win32_console.py:20:from rich.color import ColorSystem
rich/console.py:42:from .color import ColorSystem, blend_rgb
rich/style.py:10:from .color import Color, ColorParseError, ColorSystem, blend_rgb
tests/test_color.py:6:    ColorSystem,
tests/test_console.py:14:from rich.color import ColorSystem
tests/test_style.py:4:from rich.color import Color, ColorSystem, ColorType
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
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bColorSystem\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*ColorSystem\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bColorSystem\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*ColorSystem\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
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
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bColorSystem\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*ColorSystem\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bColorSystem\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*ColorSystem\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
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
  "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bColorSystem\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*ColorSystem\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
  "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bColorSystem\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*ColorSystem\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
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
 "adherence": null,
 "facts": [
  {
   "kind": "grep",
   "step": 1,
   "pattern": "^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bColorSystem\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*ColorSystem\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$",
   "scope": ".",
   "hits": [
    [
     "benchmarks/benchmarks.py",
     4
    ],
    [
     "rich/_win32_console.py",
     20
    ],
    [
     "rich/console.py",
     42
    ],
    [
     "rich/style.py",
     10
    ],
    [
     "tests/test_color.py",
     6
    ],
    [
     "tests/test_console.py",
     14
    ],
    [
     "tests/test_style.py",
     4
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
    "rich/_win32_console.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "rich/console.py",
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
    "tests/test_color.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_console.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_style.py",
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

The grep under `.` returned 7 lines, under the cap, so these are all of them: `benchmarks/benchmarks.py`, `rich/_win32_console.py`, `rich/console.py`, `rich/style.py` and 3 more files.

Candidate modules so far: 7; statements confirmed: 0, ruled out: 0, modules with no such import: 0, pending: 7. import coverage complete; star coverage complete.

Still to settle: outline `benchmarks/benchmarks.py` for its `ColorSystem` imports; outline `rich/_win32_console.py` for its `ColorSystem` imports; outline `rich/console.py` for its `ColorSystem` imports; outline `rich/style.py` for its `ColorSystem` imports; and 3 more.

Next: outline `tests/test_style.py` filtered to `ColorSystem`, because `tests/test_style.py` had a matching line (step 1); its outline names every `ColorSystem` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `benchmarks/benchmarks.py` filtered to `ColorSystem`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `benchmarks/benchmarks.py` filtered to `ColorSystem`; cap: outline `benchmarks/benchmarks.py` filtered to `ColorSystem`.

**Call:** `symbols('tests/test_style.py', 'ColorSystem')`

**Response**: outcome `ok`

```
module tests/test_style.py lines=268 dynamic=no all=none
4 from ColorSystem <- rich.color ColorSystem
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
    "ColorSystem"
   ],
   "desc": "outline `benchmarks/benchmarks.py` for its `ColorSystem` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/_win32_console.py",
    "ColorSystem"
   ],
   "desc": "outline `rich/_win32_console.py` for its `ColorSystem` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/console.py",
    "ColorSystem"
   ],
   "desc": "outline `rich/console.py` for its `ColorSystem` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/style.py",
    "ColorSystem"
   ],
   "desc": "outline `rich/style.py` for its `ColorSystem` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_color.py",
    "ColorSystem"
   ],
   "desc": "outline `tests/test_color.py` for its `ColorSystem` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_console.py",
    "ColorSystem"
   ],
   "desc": "outline `tests/test_console.py` for its `ColorSystem` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_style.py",
    "ColorSystem"
   ],
   "desc": "outline `tests/test_style.py` for its `ColorSystem` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('benchmarks/benchmarks.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"benchmarks/benchmarks.py\", \"ColorSystem\"]]",
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
     "benchmarks/benchmarks.py",
     "ColorSystem"
    ]
   ]
  },
  {
   "call": "symbols('rich/_win32_console.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"rich/_win32_console.py\", \"ColorSystem\"]]",
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
     "rich/_win32_console.py",
     "ColorSystem"
    ]
   ]
  },
  {
   "call": "symbols('rich/console.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"rich/console.py\", \"ColorSystem\"]]",
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
     "rich/console.py",
     "ColorSystem"
    ]
   ]
  },
  {
   "call": "symbols('rich/style.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"rich/style.py\", \"ColorSystem\"]]",
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
     "ColorSystem"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_color.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"tests/test_color.py\", \"ColorSystem\"]]",
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
     "ColorSystem"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_console.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"tests/test_console.py\", \"ColorSystem\"]]",
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
     "tests/test_console.py",
     "ColorSystem"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_style.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"tests/test_style.py\", \"ColorSystem\"]]",
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
     "tests/test_style.py",
     "ColorSystem"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_style.py', 'ColorSystem')",
  "key": "[\"symbols\", [\"tests/test_style.py\", \"ColorSystem\"]]",
  "provenance": "`tests/test_style.py` had a matching line (step 1); its outline names every `ColorSystem` import exactly",
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
  "ok": "[\"symbols\", [\"benchmarks/benchmarks.py\", \"ColorSystem\"]]",
  "cap": "[\"symbols\", [\"benchmarks/benchmarks.py\", \"ColorSystem\"]]"
 },
 "adherence": {
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 2,
   "path": "tests/test_style.py",
   "filter": "ColorSystem",
   "header": {
    "lines": 268,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_style.py",
     "name": "ColorSystem",
     "line": 4,
     "kind": "from",
     "src": "rich.color",
     "src_name": "ColorSystem",
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
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "rich/_win32_console.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "rich/console.py",
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
    "tests/test_color.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_con
```
</details>

## Step 3

In `tests/test_style.py`, `ColorSystem` has exactly one binding: line 4 imports it as `ColorSystem` from `rich.color`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 7; statements confirmed: 0, ruled out: 0, modules with no such import: 0, pending: 7. import coverage complete; star coverage complete.

Outstanding: outline `benchmarks/benchmarks.py` for its `ColorSystem` imports; outline `rich/_win32_console.py` for its `ColorSystem` imports; outline `rich/console.py` for its `ColorSystem` imports; outline `rich/style.py` for its `ColorSystem` imports; and 3 more.

Next: outline `benchmarks/benchmarks.py` filtered to `ColorSystem`, because `benchmarks/benchmarks.py` had a matching line (step 1); its outline names every `ColorSystem` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `rich/_win32_console.py` filtered to `ColorSystem`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `rich/color.py` filtered to `ColorSystem`; cap: outline `rich/color.py` filtered to `ColorSystem`.

**Call:** `symbols('benchmarks/benchmarks.py', 'ColorSystem')`

**Response**: outcome `ok`

```
module benchmarks/benchmarks.py lines=219 dynamic=no all=none
4 from ColorSystem <- rich.color ColorSystem
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
    "ColorSystem"
   ],
   "desc": "outline `benchmarks/benchmarks.py` for its `ColorSystem` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/_win32_console.py",
    "ColorSystem"
   ],
   "desc": "outline `rich/_win32_console.py` for its `ColorSystem` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/console.py",
    "ColorSystem"
   ],
   "desc": "outline `rich/console.py` for its `ColorSystem` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/style.py",
    "ColorSystem"
   ],
   "desc": "outline `rich/style.py` for its `ColorSystem` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_color.py",
    "ColorSystem"
   ],
   "desc": "outline `tests/test_color.py` for its `ColorSystem` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_console.py",
    "ColorSystem"
   ],
   "desc": "outline `tests/test_console.py` for its `ColorSystem` imports"
  },
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "rich/color.py",
    "ColorSystem"
   ],
   "desc": "close the namespace of `rich/color.py` for `ColorSystem`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('benchmarks/benchmarks.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"benchmarks/benchmarks.py\", \"ColorSystem\"]]",
   "v1": [
    1365207,
    114250
   ],
   "v2": [
    94121923201,
    7876737750
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
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
     "ColorSystem"
    ]
   ]
  },
  {
   "call": "symbols('rich/_win32_console.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"rich/_win32_console.py\", \"ColorSystem\"]]",
   "v1": [
    1365207,
    114250
   ],
   "v2": [
    94121923201,
    7876737750
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/_win32_console.py",
     "ColorSystem"
    ]
   ]
  },
  {
   "call": "symbols('rich/color.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"rich/color.py\", \"ColorSystem\"]]",
   "v1": [
    46982194223,
    3938368875
   ],
   "v2": [
    94121923201,
    7876737750
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     440,
     469
    ],
    "reexport": [
     11,
     469
    ],
    "star": [
     1,
     469
    ],
    "none": [
     17,
     469
    ]
   },
   "serves": [
    [
     "bindings",
     "rich/color.py",
     "ColorSystem"
    ]
   ]
  },
  {
   "call": "symbols('rich/console.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"rich/console.py\", \"ColorSystem\"]]",
   "v1": [
    1365207,
    114250
   ],
   "v2": [
    94121923201,
    7876737750
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/console.py",
     "ColorSystem"
    ]
   ]
  },
  {
   "call": "symbols('rich/style.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"rich/style.py\", \"ColorSystem\"]]",
   "v1": [
    1365207,
    114250
   ],
   "v2": [
    94121923201,
    7876737750
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
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
     "ColorSystem"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_color.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"tests/test_color.py\", \"ColorSystem\"]]",
   "v1": [
    1365207,
    114250
   ],
   "v2": [
    94121923201,
    7876737750
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
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
     "ColorSystem"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_console.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"tests/test_console.py\", \"ColorSystem\"]]",
   "v1": [
    1365207,
    114250
   ],
   "v2": [
    94121923201,
    7876737750
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_console.py",
     "ColorSystem"
    ]
   ]
  },
  {
   "call": "symbols('rich/color.py')",
   "key": "[\"symbols\", [\"rich/color.py\"]]",
   "v1": [
    13969069833196,
    1156567659625
   ],
   "v2": [
    41966314966213,
    3469702978875
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
     "ColorSystem"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('benchmarks/benchmarks.py', 'ColorSystem')",
  "key": "[\"symbols\", [\"benchmarks/benchmarks.py\", \"ColorSystem\"]]",
  "provenance": "`benchmarks/benchmarks.py` had a matching line (step 1); its outline names every `ColorSystem` import exactly",
  "v2": [
   94121923201,
   7876737750
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
  "ok": "[\"symbols\", [\"rich/color.py\", \"ColorSystem\"]]",
  "cap": "[\"symbols\", [\"rich/color.py\", \"ColorSystem\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"benchmarks/benchmarks.py\", \"ColorSystem\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 3,
   "path": "benchmarks/benchmarks.py",
   "filter": "ColorSystem",
   "header": {
    "lines": 219,
    "dynamic": false,
    "all_status": "none",
    "al
```
</details>

## Step 4

In `benchmarks/benchmarks.py`, `ColorSystem` has exactly one binding: line 4 imports it as `ColorSystem` from `rich.color`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 7; statements confirmed: 0, ruled out: 0, modules with no such import: 0, pending: 7. import coverage complete; star coverage complete.

Outstanding: close the namespace of `rich/color.py` for `ColorSystem`; outline `rich/_win32_console.py` for its `ColorSystem` imports; outline `rich/console.py` for its `ColorSystem` imports; outline `rich/style.py` for its `ColorSystem` imports; and 2 more.

Next: outline `rich/color.py` filtered to `ColorSystem`, because module `rich/color.py` (task), name `ColorSystem` (task). I expect: a definition there ends the chain (about 95%); no binding at all points at a submodule or an unresolved name (about 5%); a re-export continues the chain to its source (under 5%); no binding but a star import means checking what that source exports (under 5%). The alternative, outline `rich/_win32_console.py` filtered to `ColorSystem`, is expected to open more follow-up work. Plan by outcome: def: outline `rich/_win32_console.py` filtered to `ColorSystem`; reexport: outline `rich/_win32_console.py` filtered to `ColorSystem`; star: outline `rich/_win32_console.py` filtered to `ColorSystem`; none: outline `rich/_win32_console.py` filtered to `ColorSystem`.

**Call:** `symbols('rich/color.py', 'ColorSystem')`

**Response**: outcome `def`

```
module rich/color.py lines=622 dynamic=no all=none
21 class ColorSystem
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
    "ColorSystem"
   ],
   "desc": "close the namespace of `rich/color.py` for `ColorSystem`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/_win32_console.py",
    "ColorSystem"
   ],
   "desc": "outline `rich/_win32_console.py` for its `ColorSystem` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/console.py",
    "ColorSystem"
   ],
   "desc": "outline `rich/console.py` for its `ColorSystem` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/style.py",
    "ColorSystem"
   ],
   "desc": "outline `rich/style.py` for its `ColorSystem` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_color.py",
    "ColorSystem"
   ],
   "desc": "outline `tests/test_color.py` for its `ColorSystem` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_console.py",
    "ColorSystem"
   ],
   "desc": "outline `tests/test_console.py` for its `ColorSystem` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('rich/_win32_console.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"rich/_win32_console.py\", \"ColorSystem\"]]",
   "v1": [
    231619,
    22850
   ],
   "v2": [
    15968600117,
    1575347550
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/_win32_console.py",
     "ColorSystem"
    ]
   ]
  },
  {
   "call": "symbols('rich/color.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"rich/color.py\", \"ColorSystem\"]]",
   "v1": [
    7968546583,
    787673775
   ],
   "v2": [
    15968600117,
    1575347550
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     440,
     469
    ],
    "reexport": [
     11,
     469
    ],
    "star": [
     1,
     469
    ],
    "none": [
     17,
     469
    ]
   },
   "serves": [
    [
     "bindings",
     "rich/color.py",
     "ColorSystem"
    ]
   ]
  },
  {
   "call": "symbols('rich/console.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"rich/console.py\", \"ColorSystem\"]]",
   "v1": [
    231619,
    22850
   ],
   "v2": [
    15968600117,
    1575347550
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "rich/console.py",
     "ColorSystem"
    ]
   ]
  },
  {
   "call": "symbols('rich/style.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"rich/style.py\", \"ColorSystem\"]]",
   "v1": [
    231619,
    22850
   ],
   "v2": [
    15968600117,
    1575347550
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
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
     "ColorSystem"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_color.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"tests/test_color.py\", \"ColorSystem\"]]",
   "v1": [
    231619,
    22850
   ],
   "v2": [
    15968600117,
    1575347550
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
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
     "ColorSystem"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_console.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"tests/test_console.py\", \"ColorSystem\"]]",
   "v1": [
    231619,
    22850
   ],
   "v2": [
    15968600117,
    1575347550
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
    ],
    "cap": [
     1,
     50
    ]
   },
   "serves": [
    [
     "outline",
     "tests/test_console.py",
     "ColorSystem"
    ]
   ]
  },
  {
   "call": "symbols('rich/color.py')",
   "key": "[\"symbols\", [\"rich/color.py\"]]",
   "v1": [
    2374489605816,
    231313531925
   ],
   "v2": [
    7135289910773,
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
     "rich/color.py",
     "ColorSystem"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('rich/color.py', 'ColorSystem')",
  "key": "[\"symbols\", [\"rich/color.py\", \"ColorSystem\"]]",
  "provenance": "module `rich/color.py` (task), name `ColorSystem` (task)",
  "v2": [
   15968600117,
   1575347550
  ]
 },
 "forecast": {
  "def": [
   440,
   469
  ],
  "reexport": [
   11,
   469
  ],
  "star": [
   1,
   469
  ],
  "none": [
   17,
   469
  ]
 },
 "plan": {
  "def": "[\"symbols\", [\"rich/_win32_console.py\", \"ColorSystem\"]]",
  "reexport": "[\"symbols\", [\"rich/_win32_console.py\", \"ColorSystem\"]]",
  "star": "[\"symbols\", [\"rich/_win32_console.py\", \"ColorSystem\"]]",
  "none": "[\"symbols\", [\"rich/_win32_console.py\", \"ColorSystem\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"rich/color.py\", \"ColorSystem\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 4,
   "path": "rich/color.py",
   "filter": "ColorSystem",
   "header": {
    "lines": 622,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "rich/color.py",
     "name": "ColorSystem",
     "line": 21,
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
  "verdicts": [
   [
    "benchmarks/benchmarks.py",
    4,
    "in",
    "`rich.color` resolves `ColorSystem` to the target"
   ],
   [
    "rich/_win32_console.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "rich/console.py",
```
</details>

## Step 5

In `rich/color.py`, `ColorSystem` has exactly one binding: a class at line 21. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 7; statements confirmed: 2, ruled out: 0, modules with no such import: 0, pending: 5. import coverage complete; star coverage complete.

Still to settle: outline `rich/_win32_console.py` for its `ColorSystem` imports; outline `rich/console.py` for its `ColorSystem` imports; outline `rich/style.py` for its `ColorSystem` imports; outline `tests/test_color.py` for its `ColorSystem` imports; and 1 more.

Next: outline `rich/_win32_console.py` filtered to `ColorSystem`, because `rich/_win32_console.py` had a matching line (step 1); its outline names every `ColorSystem` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `rich/console.py` filtered to `ColorSystem`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `rich/console.py` filtered to `ColorSystem`; cap: outline `rich/console.py` filtered to `ColorSystem`.

**Call:** `symbols('rich/_win32_console.py', 'ColorSystem')`

**Response**: outcome `ok`

```
module rich/_win32_console.py lines=662 dynamic=no all=none
20 from ColorSystem <- rich.color ColorSystem
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/_win32_console.py",
    "ColorSystem"
   ],
   "desc": "outline `rich/_win32_console.py` for its `ColorSystem` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/console.py",
    "ColorSystem"
   ],
   "desc": "outline `rich/console.py` for its `ColorSystem` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/style.py",
    "ColorSystem"
   ],
   "desc": "outline `rich/style.py` for its `ColorSystem` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_color.py",
    "ColorSystem"
   ],
   "desc": "outline `tests/test_color.py` for its `ColorSystem` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_console.py",
    "ColorSystem"
   ],
   "desc": "outline `tests/test_console.py` for its `ColorSystem` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('rich/_win32_console.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"rich/_win32_console.py\", \"ColorSystem\"]]",
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
     "rich/_win32_console.py",
     "ColorSystem"
    ]
   ]
  },
  {
   "call": "symbols('rich/console.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"rich/console.py\", \"ColorSystem\"]]",
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
     "rich/console.py",
     "ColorSystem"
    ]
   ]
  },
  {
   "call": "symbols('rich/style.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"rich/style.py\", \"ColorSystem\"]]",
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
     "ColorSystem"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_color.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"tests/test_color.py\", \"ColorSystem\"]]",
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
     "ColorSystem"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_console.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"tests/test_console.py\", \"ColorSystem\"]]",
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
     "tests/test_console.py",
     "ColorSystem"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('rich/_win32_console.py', 'ColorSystem')",
  "key": "[\"symbols\", [\"rich/_win32_console.py\", \"ColorSystem\"]]",
  "provenance": "`rich/_win32_console.py` had a matching line (step 1); its outline names every `ColorSystem` import exactly",
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
  "ok": "[\"symbols\", [\"rich/console.py\", \"ColorSystem\"]]",
  "cap": "[\"symbols\", [\"rich/console.py\", \"ColorSystem\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"rich/_win32_console.py\", \"ColorSystem\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 5,
   "path": "rich/_win32_console.py",
   "filter": "ColorSystem",
   "header": {
    "lines": 662,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "rich/_win32_console.py",
     "name": "ColorSystem",
     "line": 20,
     "kind": "from",
     "src": "rich.color",
     "src_name": "ColorSystem",
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
    "`rich.color` resolves `ColorSystem` to the target"
   ],
   [
    "rich/_win32_console.py",
    20,
    "in",
    "`rich.color` resolves `ColorSystem` to the target"
   ],
   [
    "rich/console.py",
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
    "tests/test_color.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_console.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_style.py",
    4,
    "in",
    "`rich.color` resolves `ColorSystem` to the target"
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

## Step 6

In `rich/_win32_console.py`, `ColorSystem` has exactly one binding: line 20 imports it as `ColorSystem` from `rich.color`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 7; statements confirmed: 3, ruled out: 0, modules with no such import: 0, pending: 4. import coverage complete; star coverage complete.

Open: outline `rich/console.py` for its `ColorSystem` imports; outline `rich/style.py` for its `ColorSystem` imports; outline `tests/test_color.py` for its `ColorSystem` imports; outline `tests/test_console.py` for its `ColorSystem` imports.

Next: outline `rich/console.py` filtered to `ColorSystem`, because `rich/console.py` had a matching line (step 1); its outline names every `ColorSystem` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `rich/style.py` filtered to `ColorSystem`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `rich/style.py` filtered to `ColorSystem`; cap: outline `rich/style.py` filtered to `ColorSystem`.

**Call:** `symbols('rich/console.py', 'ColorSystem')`

**Response**: outcome `ok`

```
module rich/console.py lines=2699 dynamic=no all=none
42 from ColorSystem <- .color ColorSystem
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/console.py",
    "ColorSystem"
   ],
   "desc": "outline `rich/console.py` for its `ColorSystem` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/style.py",
    "ColorSystem"
   ],
   "desc": "outline `rich/style.py` for its `ColorSystem` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_color.py",
    "ColorSystem"
   ],
   "desc": "outline `tests/test_color.py` for its `ColorSystem` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_console.py",
    "ColorSystem"
   ],
   "desc": "outline `tests/test_console.py` for its `ColorSystem` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('rich/console.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"rich/console.py\", \"ColorSystem\"]]",
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
     "rich/console.py",
     "ColorSystem"
    ]
   ]
  },
  {
   "call": "symbols('rich/style.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"rich/style.py\", \"ColorSystem\"]]",
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
     "ColorSystem"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_color.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"tests/test_color.py\", \"ColorSystem\"]]",
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
     "ColorSystem"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_console.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"tests/test_console.py\", \"ColorSystem\"]]",
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
     "tests/test_console.py",
     "ColorSystem"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('rich/console.py', 'ColorSystem')",
  "key": "[\"symbols\", [\"rich/console.py\", \"ColorSystem\"]]",
  "provenance": "`rich/console.py` had a matching line (step 1); its outline names every `ColorSystem` import exactly",
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
  "ok": "[\"symbols\", [\"rich/style.py\", \"ColorSystem\"]]",
  "cap": "[\"symbols\", [\"rich/style.py\", \"ColorSystem\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"rich/console.py\", \"ColorSystem\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 6,
   "path": "rich/console.py",
   "filter": "ColorSystem",
   "header": {
    "lines": 2699,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "rich/console.py",
     "name": "ColorSystem",
     "line": 42,
     "kind": "from",
     "src": ".color",
     "src_name": "ColorSystem",
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
    "`rich.color` resolves `ColorSystem` to the target"
   ],
   [
    "rich/_win32_console.py",
    20,
    "in",
    "`rich.color` resolves `ColorSystem` to the target"
   ],
   [
    "rich/console.py",
    42,
    "in",
    "`.color` resolves `ColorSystem` to the target"
   ],
   [
    "rich/style.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_color.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_console.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_style.py",
    4,
    "in",
    "`rich.color` resolves `ColorSystem` to the target"
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

In `rich/console.py`, `ColorSystem` has exactly one binding: line 42 imports it as `ColorSystem` from `.color`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 7; statements confirmed: 4, ruled out: 0, modules with no such import: 0, pending: 3. import coverage complete; star coverage complete.

Open: outline `rich/style.py` for its `ColorSystem` imports; outline `tests/test_color.py` for its `ColorSystem` imports; outline `tests/test_console.py` for its `ColorSystem` imports.

Next: outline `rich/style.py` filtered to `ColorSystem`, because `rich/style.py` had a matching line (step 1); its outline names every `ColorSystem` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `tests/test_color.py` filtered to `ColorSystem`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `tests/test_color.py` filtered to `ColorSystem`; cap: outline `tests/test_color.py` filtered to `ColorSystem`.

**Call:** `symbols('rich/style.py', 'ColorSystem')`

**Response**: outcome `ok`

```
module rich/style.py lines=797 dynamic=no all=none
10 from ColorSystem <- .color ColorSystem
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
    "ColorSystem"
   ],
   "desc": "outline `rich/style.py` for its `ColorSystem` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_color.py",
    "ColorSystem"
   ],
   "desc": "outline `tests/test_color.py` for its `ColorSystem` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_console.py",
    "ColorSystem"
   ],
   "desc": "outline `tests/test_console.py` for its `ColorSystem` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('rich/style.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"rich/style.py\", \"ColorSystem\"]]",
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
     "ColorSystem"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_color.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"tests/test_color.py\", \"ColorSystem\"]]",
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
     "ColorSystem"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_console.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"tests/test_console.py\", \"ColorSystem\"]]",
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
     "tests/test_console.py",
     "ColorSystem"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('rich/style.py', 'ColorSystem')",
  "key": "[\"symbols\", [\"rich/style.py\", \"ColorSystem\"]]",
  "provenance": "`rich/style.py` had a matching line (step 1); its outline names every `ColorSystem` import exactly",
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
  "ok": "[\"symbols\", [\"tests/test_color.py\", \"ColorSystem\"]]",
  "cap": "[\"symbols\", [\"tests/test_color.py\", \"ColorSystem\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"rich/style.py\", \"ColorSystem\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 7,
   "path": "rich/style.py",
   "filter": "ColorSystem",
   "header": {
    "lines": 797,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "rich/style.py",
     "name": "ColorSystem",
     "line": 10,
     "kind": "from",
     "src": ".color",
     "src_name": "ColorSystem",
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
    "`rich.color` resolves `ColorSystem` to the target"
   ],
   [
    "rich/_win32_console.py",
    20,
    "in",
    "`rich.color` resolves `ColorSystem` to the target"
   ],
   [
    "rich/console.py",
    42,
    "in",
    "`.color` resolves `ColorSystem` to the target"
   ],
   [
    "rich/style.py",
    10,
    "in",
    "`.color` resolves `ColorSystem` to the target"
   ],
   [
    "tests/test_color.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_console.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_style.py",
    4,
    "in",
    "`rich.color` resolves `ColorSystem` to the target"
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

In `rich/style.py`, `ColorSystem` has exactly one binding: line 10 imports it as `ColorSystem` from `.color`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 7; statements confirmed: 5, ruled out: 0, modules with no such import: 0, pending: 2. import coverage complete; star coverage complete.

Outstanding: outline `tests/test_color.py` for its `ColorSystem` imports; outline `tests/test_console.py` for its `ColorSystem` imports.

Next: outline `tests/test_color.py` filtered to `ColorSystem`, because `tests/test_color.py` had a matching line (step 1); its outline names every `ColorSystem` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). The alternative, outline `tests/test_console.py` filtered to `ColorSystem`, scores the same; the seed broke the tie. Plan by outcome: ok: outline `tests/test_console.py` filtered to `ColorSystem`; cap: outline `tests/test_console.py` filtered to `ColorSystem`.

**Call:** `symbols('tests/test_color.py', 'ColorSystem')`

**Response**: outcome `ok`

```
module tests/test_color.py lines=188 dynamic=no all=none
1 from ColorSystem <- rich.color ColorSystem
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
    "ColorSystem"
   ],
   "desc": "outline `tests/test_color.py` for its `ColorSystem` imports"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_console.py",
    "ColorSystem"
   ],
   "desc": "outline `tests/test_console.py` for its `ColorSystem` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/test_color.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"tests/test_color.py\", \"ColorSystem\"]]",
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
     "ColorSystem"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_console.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"tests/test_console.py\", \"ColorSystem\"]]",
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
     "tests/test_console.py",
     "ColorSystem"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_color.py', 'ColorSystem')",
  "key": "[\"symbols\", [\"tests/test_color.py\", \"ColorSystem\"]]",
  "provenance": "`tests/test_color.py` had a matching line (step 1); its outline names every `ColorSystem` import exactly",
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
  "ok": "[\"symbols\", [\"tests/test_console.py\", \"ColorSystem\"]]",
  "cap": "[\"symbols\", [\"tests/test_console.py\", \"ColorSystem\"]]"
 },
 "adherence": {
  "planned": "[\"symbols\", [\"tests/test_color.py\", \"ColorSystem\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 8,
   "path": "tests/test_color.py",
   "filter": "ColorSystem",
   "header": {
    "lines": 188,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_color.py",
     "name": "ColorSystem",
     "line": 1,
     "kind": "from",
     "src": "rich.color",
     "src_name": "ColorSystem",
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
    "`rich.color` resolves `ColorSystem` to the target"
   ],
   [
    "rich/_win32_console.py",
    20,
    "in",
    "`rich.color` resolves `ColorSystem` to the target"
   ],
   [
    "rich/console.py",
    42,
    "in",
    "`.color` resolves `ColorSystem` to the target"
   ],
   [
    "rich/style.py",
    10,
    "in",
    "`.color` resolves `ColorSystem` to the target"
   ],
   [
    "tests/test_color.py",
    1,
    "in",
    "`rich.color` resolves `ColorSystem` to the target"
   ],
   [
    "tests/test_console.py",
    0,
    "pending",
    "outline not yet seen"
   ],
   [
    "tests/test_style.py",
    4,
    "in",
    "`rich.color` resolves `ColorSystem` to the target"
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

In `tests/test_color.py`, `ColorSystem` has exactly one binding: line 1 imports it as `ColorSystem` from `rich.color`. No dynamic namespace tricks, no `__all__`.

Candidate modules so far: 7; statements confirmed: 6, ruled out: 0, modules with no such import: 0, pending: 1. import coverage complete; star coverage complete.

Still to settle: outline `tests/test_console.py` for its `ColorSystem` imports.

Next: outline `tests/test_console.py` filtered to `ColorSystem`, because `tests/test_console.py` had a matching line (step 1); its outline names every `ColorSystem` import exactly. I expect: the outline lists its imports of the name (near certain); a capped outline means filtering by name (under 5%). Plan by outcome: ok: resolve the sources its import statements name; cap: work the items it opens.

**Call:** `symbols('tests/test_console.py', 'ColorSystem')`

**Response**: outcome `ok`

```
module tests/test_console.py lines=1136 dynamic=no all=none
14 from ColorSystem <- rich.color ColorSystem
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_console.py",
    "ColorSystem"
   ],
   "desc": "outline `tests/test_console.py` for its `ColorSystem` imports"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/test_console.py', 'ColorSystem')",
   "key": "[\"symbols\", [\"tests/test_console.py\", \"ColorSystem\"]]",
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
     "tests/test_console.py",
     "ColorSystem"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_console.py', 'ColorSystem')",
  "key": "[\"symbols\", [\"tests/test_console.py\", \"ColorSystem\"]]",
  "provenance": "`tests/test_console.py` had a matching line (step 1); its outline names every `ColorSystem` import exactly",
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
  "planned": "[\"symbols\", [\"tests/test_console.py\", \"ColorSystem\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 9,
   "path": "tests/test_console.py",
   "filter": "ColorSystem",
   "header": {
    "lines": 1136,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_console.py",
     "name": "ColorSystem",
     "line": 14,
     "kind": "from",
     "src": "rich.color",
     "src_name": "ColorSystem",
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
    "`rich.color` resolves `ColorSystem` to the target"
   ],
   [
    "rich/_win32_console.py",
    20,
    "in",
    "`rich.color` resolves `ColorSystem` to the target"
   ],
   [
    "rich/console.py",
    42,
    "in",
    "`.color` resolves `ColorSystem` to the target"
   ],
   [
    "rich/style.py",
    10,
    "in",
    "`.color` resolves `ColorSystem` to the target"
   ],
   [
    "tests/test_color.py",
    1,
    "in",
    "`rich.color` resolves `ColorSystem` to the target"
   ],
   [
    "tests/test_console.py",
    14,
    "in",
    "`rich.color` resolves `ColorSystem` to the target"
   ],
   [
    "tests/test_style.py",
    4,
    "in",
    "`rich.color` resolves `ColorSystem` to the target"
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

Certificate complete. 7 import statements import this definition: `benchmarks/benchmarks.py:4`, `rich/_win32_console.py:20`, `rich/console.py:42`, `rich/style.py:10`, `tests/test_color.py:1`, `tests/test_console.py:14`, `tests/test_style.py:4`. In hindsight every one of the 9 calls was needed for the certificate.

**Answer:** `{"statements": ["benchmarks/benchmarks.py:4", "rich/_win32_console.py:20", "rich/console.py:42", "rich/style.py:10", "tests/test_color.py:1", "tests/test_console.py:14", "tests/test_style.py:4"], "count": 7}`  
**Stopped:** certificate after 9 calls