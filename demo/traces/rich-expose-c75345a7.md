# rich-expose-c75345a7

**Repository:** rich  
**Chain:** resolve → expose  
**Seed:** 0, prior bf534cee5cd76c8c, floor 4

## Task

In `rich/progress_bar.py` line 8, `Console` is imported from `.console`. Which definition does the module-level name `Console` actually refer to? Give `path:line`. Then propose the one-line change to `rich/_unicode_data/__init__.py` that makes `from _unicode_data import Console` resolve to this definition; give the exact line to append.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N; bindings take effect in source order. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. A class derives from a definition when a base written as a bare name or `module.Name` resolves to it. A call site is `name(...)` where the bare name refers to the module-level binding (not a parameter or local). Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

I need to find what `Console` really is in `rich/progress_bar.py`: line 8 imports it from `.console`, so the definition is at least one hop away. Then I have to propose the one-line import that exposes it from the package.

Next I will check `rich/progress_bar.py` for any other binding of `Console` besides the import on line 8; almost certainly the import is the only one, and then `.console` is the place to follow.

**Call:** `symbols('rich/progress_bar.py', 'Console')`

**Response**: outcome `reexport`

```
module rich/progress_bar.py lines=224 dynamic=no all=none
8 from Console <- .console Console
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "rich/progress_bar.py",
    "Console"
   ],
   "desc": "check the top-level names of `rich/progress_bar.py` for `Console`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('rich/progress_bar.py', 'Console')",
   "key": "[\"symbols\", [\"rich/progress_bar.py\", \"Console\"]]",
   "v1": [
    938947,
    321195
   ],
   "v2": [
    938947,
    321195
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
     "rich/progress_bar.py",
     "Console"
    ]
   ]
  },
  {
   "call": "symbols('rich/progress_bar.py')",
   "key": "[\"symbols\", [\"rich/progress_bar.py\"]]",
   "v1": [
    869288852,
    282972795
   ],
   "v2": [
    869288852,
    282972795
   ],
   "p_cap": [
    131,
    881
   ],
   "forecast": {
    "def": [
     15,
     1762
    ],
    "reexport": [
     1395,
     1762
    ],
    "star": [
     15,
     1762
    ],
    "none": [
     75,
     1762
    ],
    "cap": [
     131,
     881
    ]
   },
   "serves": [
    [
     "bindings",
     "rich/progress_bar.py",
     "Console"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('rich/progress_bar.py', 'Console')",
  "key": "[\"symbols\", [\"rich/progress_bar.py\", \"Console\"]]",
  "provenance": "module `rich/progress_bar.py` (task), name `Console` (task)",
  "v2": [
   938947,
   321195
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
   "path": "rich/progress_bar.py",
   "filter": "Console",
   "header": {
    "lines": 224,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "rich/progress_bar.py",
     "name": "Console",
     "line": 8,
     "kind": "from",
     "src": ".console",
     "src_name": "Console",
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
    "rich/progress_bar.py",
    "Console",
    "reexport",
    [
     ".console",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 2

`rich/progress_bar.py` does not define `Console` itself; line 8 imports it from `.console`.

So far: `rich/progress_bar.py` takes `Console` from `.console`, which I still have to locate.

Let me outline `rich/console.py` directly, which both checks that the file exists and shows me `Console`; if `.console` is a plain module that is where it has to be. Very likely it is defined right there. If the file does not exist, I will search the whole tree for `class Console`/`def Console`; if the name is not bound there, that finishes it. I could search the whole tree for `class Console`/`def Console` instead, but it tends to open more follow-up work.

**Call:** `symbols('rich/console.py', 'Console')`

**Response**: outcome `def`

```
module rich/console.py lines=2699 dynamic=no all=none
581 class Console ()
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "rich/progress_bar.py",
    ".console"
   ],
   "desc": "find where `.console` (imported by `rich/progress_bar.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "symbols('rich/console.py', 'Console')",
   "key": "[\"symbols\", [\"rich/console.py\", \"Console\"]]",
   "v1": [
    803368669,
    612583104
   ],
   "v2": [
    1111411811,
    842301768
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     15355,
     19072
    ],
    "reexport": [
     333,
     19072
    ],
    "star": [
     37,
     19072
    ],
    "none": [
     407,
     9536
    ],
    "missing": [
     17,
     128
    ]
   },
   "serves": [
    [
     "module_path",
     "rich/progress_bar.py",
     ".console"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+Console\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+Console\\\\b\", \".\"]]",
   "v1": [
    30376,
    14421
   ],
   "v2": [
    20840583517,
    10107621216
   ],
   "p_cap": [
    1,
    33
   ],
   "forecast": {
    "zero": [
     1,
     33
    ],
    "mid": [
     31,
     33
    ],
    "cap": [
     1,
     33
    ]
   },
   "serves": [
    [
     "module_path",
     "rich/progress_bar.py",
     ".console"
    ]
   ]
  },
  {
   "call": "ls('rich')",
   "key": "[\"ls\", [\"rich\"]]",
   "v1": [
    14741,
    6992
   ],
   "v2": [
    20213982493,
    9801329664
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
     "rich/progress_bar.py",
     ".console"
    ]
   ]
  },
  {
   "call": "symbols('rich/console/__init__.py', 'Console')",
   "key": "[\"symbols\", [\"rich/console/__init__.py\", \"Console\"]]",
   "v1": [
    664546247,
    222401536
   ],
   "v2": [
    4363261598335,
    1855718416384
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     119,
     9088
    ],
    "reexport": [
     799,
     9088
    ],
    "star": [
     17,
     9088
    ],
    "none": [
     17,
     568
    ],
    "missing": [
     111,
     128
    ]
   },
   "serves": [
    [
     "module_path",
     "rich/progress_bar.py",
     ".console"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('rich/console.py', 'Console')",
  "key": "[\"symbols\", [\"rich/console.py\", \"Console\"]]",
  "provenance": "`.console` would be `rich/console.py` if that file exists; one call both checks and closes it",
  "v2": [
   1111411811,
   842301768
  ]
 },
 "forecast": {
  "def": [
   15355,
   19072
  ],
  "reexport": [
   333,
   19072
  ],
  "star": [
   37,
   19072
  ],
  "none": [
   407,
   9536
  ],
  "missing": [
   17,
   128
  ]
 },
 "plan": {
  "def": "done",
  "reexport": "continue",
  "star": "continue",
  "none": "done",
  "missing": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+Console\\\\b\", \".\"]]"
 },
 "hedges": [
  {
   "outcome": "def",
   "word": "very likely",
   "p": [
    15355,
    19072
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
   "step": 2,
   "path": "rich/console.py",
   "filter": "Console",
   "header": {
    "lines": 2699,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "rich/console.py",
     "name": "Console",
     "line": 581,
     "kind": "class",
     "src": null,
     "src_name": null,
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
    "rich/progress_bar.py",
    "Console",
    "reexport",
    [
     ".console",
     "rich/console.py"
    ]
   ],
   [
    "rich/console.py",
    "Console",
    "class",
    581
   ]
  ]
 }
}
```
</details>

## Step 3

There it is: `Console` is a class at `rich/console.py:581`. That settles the definition; now the package that should expose it.

I'll look at `rich/_unicode_data/__init__.py`'s top-level names for `Console`; that settles what the name means there. Probably it is re-exported from somewhere else. If the name is not bound there, I follow whatever it opens up; if it is defined right there, that finishes it. I could outline all of `rich/_unicode_data/__init__.py` instead, but it is more likely to hit the cap.

**Call:** `symbols('rich/_unicode_data/__init__.py', 'Console')`

**Response**: outcome `none`

```
module rich/_unicode_data/__init__.py lines=94 dynamic=no all=none
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "rich/_unicode_data/__init__.py",
    "Console"
   ],
   "desc": "check the top-level names of `rich/_unicode_data/__init__.py` for `Console`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('rich/_unicode_data/__init__.py', 'Console')",
   "key": "[\"symbols\", [\"rich/_unicode_data/__init__.py\", \"Console\"]]",
   "v1": [
    4536943,
    1737512
   ],
   "v2": [
    4536943,
    1737512
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     7,
     71
    ],
    "reexport": [
     47,
     71
    ],
    "star": [
     1,
     71
    ],
    "none": [
     16,
     71
    ]
   },
   "serves": [
    [
     "bindings",
     "rich/_unicode_data/__init__.py",
     "Console"
    ]
   ]
  },
  {
   "call": "symbols('rich/_unicode_data/__init__.py')",
   "key": "[\"symbols\", [\"rich/_unicode_data/__init__.py\"]]",
   "v1": [
    265169473,
    95563160
   ],
   "v2": [
    265169473,
    95563160
   ],
   "p_cap": [
    9,
    55
   ],
   "forecast": {
    "def": [
     322,
     3905
    ],
    "reexport": [
     2162,
     3905
    ],
    "star": [
     46,
     3905
    ],
    "none": [
     736,
     3905
    ],
    "cap": [
     9,
     55
    ]
   },
   "serves": [
    [
     "bindings",
     "rich/_unicode_data/__init__.py",
     "Console"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('rich/_unicode_data/__init__.py', 'Console')",
  "key": "[\"symbols\", [\"rich/_unicode_data/__init__.py\", \"Console\"]]",
  "provenance": "module `rich/_unicode_data/__init__.py` (task), name `Console` (task)",
  "v2": [
   4536943,
   1737512
  ]
 },
 "forecast": {
  "def": [
   7,
   71
  ],
  "reexport": [
   47,
   71
  ],
  "star": [
   1,
   71
  ],
  "none": [
   16,
   71
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
    47,
    71
   ]
  }
 ],
 "adherence": {
  "planned": "done",
  "status": "deviated"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 3,
   "path": "rich/_unicode_data/__init__.py",
   "filter": "Console",
   "header": {
    "lines": 94,
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
  "step": 2,
  "of": 2,
  "package": "rich/_unicode_data/__init__.py",
  "bound": null,
  "spec": "..console"
 }
}
```
</details>

## Step 4

The package `rich/_unicode_data` does not bind `Console`; for a package that leaves a submodule called `Console` as the only option.

I'll list `rich/_unicode_data/` to see what lives there; a package that does not bind the name could still have a submodule called that. Almost certainly the listing fits. I could outline `rich/_unicode_data/Console.py` directly, which both checks that the file exists and shows me `Console` instead, but it tends to open more follow-up work.

**Call:** `ls('rich/_unicode_data')`

**Response**: outcome `complete`

```
__init__.py
_versions.py
unicode10-0-0.py
unicode11-0-0.py
unicode12-0-0.py
unicode12-1-0.py
unicode13-0-0.py
unicode14-0-0.py
unicode15-0-0.py
unicode15-1-0.py
unicode16-0-0.py
unicode17-0-0.py
unicode4-1-0.py
unicode5-0-0.py
unicode5-1-0.py
unicode5-2-0.py
unicode6-0-0.py
unicode6-1-0.py
unicode6-2-0.py
unicode6-3-0.py
unicode7-0-0.py
unicode8-0-0.py
unicode9-0-0.py
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "submodule",
   "key": [
    "submodule",
    "rich/_unicode_data/__init__.py",
    "Console"
   ],
   "desc": "check whether `rich/_unicode_data` has a submodule `Console`"
  }
 ],
 "candidates": [
  {
   "call": "ls('rich/_unicode_data')",
   "key": "[\"ls\", [\"rich/_unicode_data\"]]",
   "v1": [
    223,
    219
   ],
   "v2": [
    68514422819,
    67077849888
   ],
   "p_cap": [
    4,
    219
   ],
   "forecast": {
    "complete": [
     215,
     219
    ],
    "cap": [
     4,
     219
    ]
   },
   "serves": [
    [
     "submodule",
     "rich/_unicode_data/__init__.py",
     "Console"
    ]
   ]
  },
  {
   "call": "symbols('rich/_unicode_data/Console.py', 'Console')",
   "key": "[\"symbols\", [\"rich/_unicode_data/Console.py\", \"Console\"]]",
   "v1": [
    1436572931,
    1225166208
   ],
   "v2": [
    105086780479,
    89437133184
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     15355,
     19072
    ],
    "reexport": [
     333,
     19072
    ],
    "star": [
     37,
     19072
    ],
    "none": [
     407,
     9536
    ],
    "missing": [
     17,
     128
    ]
   },
   "serves": [
    [
     "submodule",
     "rich/_unicode_data/__init__.py",
     "Console"
    ]
   ]
  },
  {
   "call": "symbols('rich/_unicode_data/Console/__init__.py', 'Console')",
   "key": "[\"symbols\", [\"rich/_unicode_data/Console/__init__.py\", \"Console\"]]",
   "v1": [
    462855695,
    222401536
   ],
   "v2": [
    34045617511,
    16235312128
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     119,
     9088
    ],
    "reexport": [
     799,
     9088
    ],
    "star": [
     17,
     9088
    ],
    "none": [
     17,
     568
    ],
    "missing": [
     111,
     128
    ]
   },
   "serves": [
    [
     "submodule",
     "rich/_unicode_data/__init__.py",
     "Console"
    ]
   ]
  }
 ],
 "choice": {
  "call": "ls('rich/_unicode_data')",
  "key": "[\"ls\", [\"rich/_unicode_data\"]]",
  "provenance": "package directory of `rich/_unicode_data/__init__.py`",
  "v2": [
   68514422819,
   67077849888
  ]
 },
 "forecast": {
  "complete": [
   215,
   219
  ],
  "cap": [
   4,
   219
  ]
 },
 "plan": {
  "complete": "done",
  "cap": "[\"symbols\", [\"rich/_unicode_data/Console.py\", \"Console\"]]"
 },
 "hedges": [
  {
   "outcome": "complete",
   "word": "almost certainly",
   "p": [
    215,
    219
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
   "step": 4,
   "dir": "rich/_unicode_data",
   "entries": [
    "__init__.py",
    "_versions.py",
    "unicode10-0-0.py",
    "unicode11-0-0.py",
    "unicode12-0-0.py",
    "unicode12-1-0.py",
    "unicode13-0-0.py",
    "unicode14-0-0.py",
    "unicode15-0-0.py",
    "unicode15-1-0.py",
    "unicode16-0-0.py",
    "unicode17-0-0.py",
    "unicode4-1-0.py",
    "unicode5-0-0.py",
    "unicode5-1-0.py",
    "unicode5-2-0.py",
    "unicode6-0-0.py",
    "unicode6-1-0.py",
    "unicode6-2-0.py",
    "unicode6-3-0.py",
    "unicode7-0-0.py",
    "unicode8-0-0.py",
    "unicode9-0-0.py"
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "expose",
  "step": 2,
  "of": 2,
  "package": "rich/_unicode_data/__init__.py",
  "bound": false,
  "spec": "..console"
 }
}
```
</details>

## Final

`Console` is the class at `rich/console.py:581`. Patch: append `from ..console import Console` to `rich/_unicode_data/__init__.py`. The package does not bind `Console` today and is not dynamic, so after that line `from _unicode_data import Console` resolves to the definition. Looking back, all 4 calls were needed.

**Answer:** `{"final_kind": "expose", "final": {"patch": {"path": "rich/_unicode_data/__init__.py", "append": "from ..console import Console"}, "claim": "after the patch, `Console` in `rich/_unicode_data/__init__.py` resolves to rich/console.py:581"}, "steps": [{"op": "resolve", "output": {"kind": "def", "path": "rich/console.py", "line": 581, "name": "Console", "detail": "class"}}, {"op": "expose", "output": {"patch": {"path": "rich/_unicode_data/__init__.py", "append": "from ..console import Console"}, "claim": "after the patch, `Console` in `rich/_unicode_data/__init__.py` resolves to rich/console.py:581"}}], "stuck": null}`  
**Stopped:** certificate after 4 calls