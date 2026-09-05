# black-expose-363321ff

**Repository:** black  
**Chain:** expose  
**Seed:** 0, prior f2e0b46ccc75305a, floor 2

## Task

`Line` is defined at `src/black/lines.py:44` (class).

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N; bindings take effect in source order. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. A class derives from a definition when a base written as a bare name or `module.Name` resolves to it. A call site is `name(...)` where the bare name refers to the module-level binding (not a parameter or local). Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

Starting from the definition of `Line` at `src/black/lines.py:44`. Then I have to propose the one-line import that exposes it from the package.

Next I will look at `src/black/__init__.py`'s top-level names for `Line`; that settles what the name means there. Probably it is re-exported from somewhere else. If the name is not bound there, I follow whatever it opens up; if it is defined right there, that finishes it. I could outline all of `src/black/__init__.py` instead, but it is more likely to hit the cap.

**Call:** `symbols('src/black/__init__.py', 'Line')`

**Response**: outcome `none`

```
module src/black/__init__.py lines=1723 dynamic=no all=none
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/black/__init__.py",
    "Line"
   ],
   "desc": "check the top-level names of `src/black/__init__.py` for `Line`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/black/__init__.py', 'Line')",
   "key": "[\"symbols\", [\"src/black/__init__.py\", \"Line\"]]",
   "v1": [
    12152,
    5035
   ],
   "v2": [
    12152,
    5035
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     15,
     76
    ],
    "reexport": [
     43,
     76
    ],
    "star": [
     1,
     76
    ],
    "none": [
     17,
     76
    ]
   },
   "serves": [
    [
     "bindings",
     "src/black/__init__.py",
     "Line"
    ]
   ]
  },
  {
   "call": "symbols('src/black/__init__.py')",
   "key": "[\"symbols\", [\"src/black/__init__.py\"]]",
   "v1": [
    667149,
    261820
   ],
   "v2": [
    667149,
    261820
   ],
   "p_cap": [
    7,
    52
   ],
   "forecast": {
    "def": [
     675,
     3952
    ],
    "reexport": [
     1935,
     3952
    ],
    "star": [
     45,
     3952
    ],
    "none": [
     765,
     3952
    ],
    "cap": [
     7,
     52
    ]
   },
   "serves": [
    [
     "bindings",
     "src/black/__init__.py",
     "Line"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/black/__init__.py', 'Line')",
  "key": "[\"symbols\", [\"src/black/__init__.py\", \"Line\"]]",
  "provenance": "module `src/black/__init__.py` (task), name `Line` (task)",
  "v2": [
   12152,
   5035
  ]
 },
 "forecast": {
  "def": [
   15,
   76
  ],
  "reexport": [
   43,
   76
  ],
  "star": [
   1,
   76
  ],
  "none": [
   17,
   76
  ]
 },
 "plan": {
  "def": "done",
  "reexport": "continue",
  "star": "continue",
  "none": "continue"
 },
 "hedges": [
  {
   "outcome": "reexport",
   "word": "probably",
   "p": [
    43,
    76
   ]
  }
 ],
 "adherence": null,
 "facts": [
  {
   "kind": "outline",
   "step": 1,
   "path": "src/black/__init__.py",
   "filter": "Line",
   "header": {
    "lines": 1723,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "expose",
  "step": 1,
  "of": 1,
  "package": "src/black/__init__.py",
  "bound": null,
  "spec": ".lines"
 }
}
```
</details>

## Step 2

The package `src/black` does not bind `Line`; for a package that leaves a submodule called `Line` as the only option.

Let me list `src/black/` to see what lives there; a package that does not bind the name could still have a submodule called that. Almost certainly the listing fits. If the listing is too long, I will outline `src/black/Line.py` directly, which both checks that the file exists and shows me `Line`. I could outline `src/black/Line.py` directly, which both checks that the file exists and shows me `Line` instead, but it tends to open more follow-up work.

**Call:** `ls('src/black')`

**Response**: outcome `complete`

```
__init__.py
__main__.py
_width_table.py
brackets.py
cache.py
comments.py
concurrency.py
const.py
debug.py
files.py
handle_ipynb_magics.py
linegen.py
lines.py
mode.py
nodes.py
numerics.py
output.py
parsing.py
ranges.py
report.py
resources/
rusty.py
schema.py
strings.py
trans.py
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "submodule",
   "key": [
    "submodule",
    "src/black/__init__.py",
    "Line"
   ],
   "desc": "check whether `src/black` has a submodule `Line`"
  }
 ],
 "candidates": [
  {
   "call": "ls('src/black')",
   "key": "[\"ls\", [\"src/black\"]]",
   "v1": [
    185,
    181
   ],
   "v2": [
    54770451113,
    53374837505
   ],
   "p_cap": [
    4,
    181
   ],
   "forecast": {
    "complete": [
     177,
     181
    ],
    "cap": [
     4,
     181
    ]
   },
   "serves": [
    [
     "submodule",
     "src/black/__init__.py",
     "Line"
    ]
   ]
  },
  {
   "call": "symbols('src/black/Line.py', 'Line')",
   "key": "[\"symbols\", [\"src/black/Line.py\", \"Line\"]]",
   "v1": [
    348903402,
    294888605
   ],
   "v2": [
    63316789222,
    53374837505
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     189504,
     234971
    ],
    "reexport": [
     4480,
     234971
    ],
    "star": [
     448,
     234971
    ],
    "none": [
     7616,
     234971
    ],
    "missing": [
     73,
     521
    ]
   },
   "serves": [
    [
     "submodule",
     "src/black/__init__.py",
     "Line"
    ]
   ]
  },
  {
   "call": "symbols('src/black/Line/__init__.py', 'Line')",
   "key": "[\"symbols\", [\"src/black/Line/__init__.py\", \"Line\"]]",
   "v1": [
    5398456,
    2623235
   ],
   "v2": [
    986143256,
    474805535
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     1095,
     39596
    ],
    "reexport": [
     3139,
     39596
    ],
    "star": [
     73,
     39596
    ],
    "none": [
     1241,
     39596
    ],
    "missing": [
     448,
     521
    ]
   },
   "serves": [
    [
     "submodule",
     "src/black/__init__.py",
     "Line"
    ]
   ]
  }
 ],
 "choice": {
  "call": "ls('src/black')",
  "key": "[\"ls\", [\"src/black\"]]",
  "provenance": "package directory of `src/black/__init__.py`",
  "v2": [
   54770451113,
   53374837505
  ]
 },
 "forecast": {
  "complete": [
   177,
   181
  ],
  "cap": [
   4,
   181
  ]
 },
 "plan": {
  "complete": "done",
  "cap": "[\"symbols\", [\"src/black/Line.py\", \"Line\"]]"
 },
 "hedges": [
  {
   "outcome": "complete",
   "word": "almost certainly",
   "p": [
    177,
    181
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
   "dir": "src/black",
   "entries": [
    "__init__.py",
    "__main__.py",
    "_width_table.py",
    "brackets.py",
    "cache.py",
    "comments.py",
    "concurrency.py",
    "const.py",
    "debug.py",
    "files.py",
    "handle_ipynb_magics.py",
    "linegen.py",
    "lines.py",
    "mode.py",
    "nodes.py",
    "numerics.py",
    "output.py",
    "parsing.py",
    "ranges.py",
    "report.py",
    "resources/",
    "rusty.py",
    "schema.py",
    "strings.py",
    "trans.py"
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "expose",
  "step": 1,
  "of": 1,
  "package": "src/black/__init__.py",
  "bound": false,
  "spec": ".lines"
 }
}
```
</details>

## Final

Patch: append `from .lines import Line` to `src/black/__init__.py`. The package does not bind `Line` today and is not dynamic, so after that line `from black import Line` resolves to the definition. Looking back, all 2 calls were needed.

**Answer:** `{"final_kind": "expose", "final": {"patch": {"path": "src/black/__init__.py", "append": "from .lines import Line"}, "claim": "after the patch, `Line` in `src/black/__init__.py` resolves to src/black/lines.py:44"}, "steps": [{"op": "expose", "output": {"patch": {"path": "src/black/__init__.py", "append": "from .lines import Line"}, "claim": "after the patch, `Line` in `src/black/__init__.py` resolves to src/black/lines.py:44"}}], "stuck": null}`  
**Stopped:** certificate after 2 calls