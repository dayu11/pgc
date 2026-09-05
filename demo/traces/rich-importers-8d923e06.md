# rich-importers-8d923e06

**Repository:** rich  
**Chain:** resolve → importers  
**Seed:** 0, prior bf534cee5cd76c8c, floor 18

## Task

In `examples/dynamic_progress.py` line 11, `Group` is imported from `rich.console`. Which definition does the module-level name `Group` actually refer to? Give `path:line`. Then list every module-level import statement in the repository that brings in that definition, including through re-exports and star imports, as `path:line`.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N; bindings take effect in source order. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. A class derives from a definition when a base written as a bare name or `module.Name` resolves to it. A call site is `name(...)` where the bare name refers to the module-level binding (not a parameter or local). Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

I need to find what `Group` really is in `examples/dynamic_progress.py`: line 11 imports it from `rich.console`, so the definition is at least one hop away. Then I have to find every module-level import of that definition, which means a complete search, not a sample.

Next I will check `examples/dynamic_progress.py` for any other binding of `Group` besides the import on line 11; almost certainly the import is the only one, and then `rich.console` is the place to follow.

**Call:** `symbols('examples/dynamic_progress.py', 'Group')`

**Response**: outcome `reexport`

```
module examples/dynamic_progress.py lines=118 dynamic=no all=none
11 from Group <- rich.console Group
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "examples/dynamic_progress.py",
    "Group"
   ],
   "desc": "check the top-level names of `examples/dynamic_progress.py` for `Group`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('examples/dynamic_progress.py', 'Group')",
   "key": "[\"symbols\", [\"examples/dynamic_progress.py\", \"Group\"]]",
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
     "examples/dynamic_progress.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('examples/dynamic_progress.py')",
   "key": "[\"symbols\", [\"examples/dynamic_progress.py\"]]",
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
     "examples/dynamic_progress.py",
     "Group"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('examples/dynamic_progress.py', 'Group')",
  "key": "[\"symbols\", [\"examples/dynamic_progress.py\", \"Group\"]]",
  "provenance": "module `examples/dynamic_progress.py` (task), name `Group` (task)",
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
   "path": "examples/dynamic_progress.py",
   "filter": "Group",
   "header": {
    "lines": 118,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "examples/dynamic_progress.py",
     "name": "Group",
     "line": 11,
     "kind": "from",
     "src": "rich.console",
     "src_name": "Group",
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
    "examples/dynamic_progress.py",
    "Group",
    "reexport",
    [
     "rich.console",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 2

`examples/dynamic_progress.py` does not define `Group` itself; line 11 imports it from `rich.console`.

So far: `examples/dynamic_progress.py` takes `Group` from `rich.console`, which I still have to locate.

Let me list `./` to see what lives there; the listing settles whether the import is a module, a package, or not here at all. Very likely the listing fits. If the listing is too long, I will outline `rich/console.py` directly, which both checks that the file exists and shows me `Group`. I could outline `rich/console.py` directly, which both checks that the file exists and shows me `Group` instead, but it costs more calls in expectation.

**Call:** `ls('.')`

**Response** (capped): outcome `cap`

```
.faq/
.github/
.pre-commit-config.yaml
.readthedocs.yml
AI_POLICY.md
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
CONTRIBUTORS.md
FAQ.md
README.cn.md
README.de-ch.md
README.de.md
README.es.md
README.fa.md
README.fr.md
README.hi.md
README.id.md
README.it.md
README.ja.md
README.kr.md
README.md
README.pl.md
README.pt-br.md
README.ru.md
... (15 more lines)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "examples/dynamic_progress.py",
    "rich.console"
   ],
   "desc": "find where `rich.console` (imported by `examples/dynamic_progress.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    2245,
    1311
   ],
   "v2": [
    669175458089,
    383859887544
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
     "examples/dynamic_progress.py",
     "rich.console"
    ]
   ]
  },
  {
   "call": "symbols('rich/console.py', 'Group')",
   "key": "[\"symbols\", [\"rich/console.py\", \"Group\"]]",
   "v1": [
    99095213201,
    42651098616
   ],
   "v2": [
    180026699261,
    85302197232
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     445295,
     1327888
    ],
    "reexport": [
     9657,
     1327888
    ],
    "star": [
     1073,
     1327888
    ],
    "none": [
     11803,
     663944
    ],
    "missing": [
     5693,
     8912
    ]
   },
   "serves": [
    [
     "module_path",
     "examples/dynamic_progress.py",
     "rich.console"
    ]
   ]
  },
  {
   "call": "symbols('rich/console/__init__.py', 'Group')",
   "key": "[\"symbols\", [\"rich/console/__init__.py\", \"Group\"]]",
   "v1": [
    46790532363,
    15484706944
   ],
   "v2": [
    125743483561,
    46454120832
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     3451,
     632752
    ],
    "reexport": [
     23171,
     632752
    ],
    "star": [
     493,
     632752
    ],
    "none": [
     493,
     39547
    ],
    "missing": [
     8419,
     8912
    ]
   },
   "serves": [
    [
     "module_path",
     "examples/dynamic_progress.py",
     "rich.console"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+Group\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+Group\\\\b\", \".\"]]",
   "v1": [
    1331,
    437
   ],
   "v2": [
    3556,
    1311
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
     "examples/dynamic_progress.py",
     "rich.console"
    ]
   ]
  }
 ],
 "choice": {
  "call": "ls('.')",
  "key": "[\"ls\", [\".\"]]",
  "provenance": "`rich.console` imported by `examples/dynamic_progress.py` should live under `.`",
  "v2": [
   669175458089,
   383859887544
  ]
 },
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
 "plan": {
  "complete": "continue",
  "cap": "[\"symbols\", [\"rich/console.py\", \"Group\"]]"
 },
 "hedges": [
  {
   "outcome": "complete",
   "word": "very likely",
   "p": [
    8,
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
    ".faq/",
    ".github/",
    ".pre-commit-config.yaml",
    ".readthedocs.yml",
    "AI_POLICY.md",
    "CHANGELOG.md",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "CONTRIBUTORS.md",
    "FAQ.md",
    "README.cn.md",
    "README.de-ch.md",
    "README.de.md",
    "README.es.md",
    "README.fa.md",
    "README.fr.md",
    "README.hi.md",
    "README.id.md",
    "README.it.md",
    "README.ja.md",
    "README.kr.md",
    "README.md",
    "README.pl.md",
    "README.pt-br.md",
    "README.ru.md",
    "README.sv.md",
    "README.tr.md",
    "README.zh-tw.md",
    "SECURITY.md",
    "assets/",
    "asv.conf.json",
    "benchmarks/",
    "docs/",
    "examples/",
    "faq.yml",
    "pyproject.toml",
    "questions/",
    "rich/",
    "setup.py",
    "tests/"
   ],
   "complete": false
  }
 ],
 "goal_state": {
  "phase": "resolve",
  "step": 1,
  "of": 2,
  "chain": [
   [
    "examples/dynamic_progress.py",
    "Group",
    "reexport",
    [
     "rich.console",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 3

`./` has 40 entries, and the listing is capped so I can't trust absences: `rich/` is there, so `rich.console` is a package.

So far: `examples/dynamic_progress.py` takes `Group` from `rich.console`, which I still have to locate.

I'll outline `rich/console.py` directly, which both checks that the file exists and shows me `Group`; if `rich.console` is a plain module that is where it has to be. Very likely it is defined right there. If the file does not exist, I will list `rich/` to see what lives there; if the name is not bound there, that finishes it. I could list `rich/` to see what lives there instead, but it tends to open more follow-up work.

**Call:** `symbols('rich/console.py', 'Group')`

**Response**: outcome `def`

```
module rich/console.py lines=2699 dynamic=no all=none
450 class Group ()
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "examples/dynamic_progress.py",
    "rich.console"
   ],
   "desc": "find where `rich.console` (imported by `examples/dynamic_progress.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "symbols('rich/console.py', 'Group')",
   "key": "[\"symbols\", [\"rich/console.py\", \"Group\"]]",
   "v1": [
    803368669,
    612583104
   ],
   "v2": [
    25870514795,
    19602659328
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
     "examples/dynamic_progress.py",
     "rich.console"
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
     "examples/dynamic_progress.py",
     "rich.console"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+Group\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+Group\\\\b\", \".\"]]",
   "v1": [
    1331,
    437
   ],
   "v2": [
    1415951773,
    612583104
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
     "examples/dynamic_progress.py",
     "rich.console"
    ]
   ]
  },
  {
   "call": "symbols('rich/console/__init__.py', 'Group')",
   "key": "[\"symbols\", [\"rich/console/__init__.py\", \"Group\"]]",
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
     "examples/dynamic_progress.py",
     "rich.console"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('rich/console.py', 'Group')",
  "key": "[\"symbols\", [\"rich/console.py\", \"Group\"]]",
  "provenance": "`rich.console` would be `rich/console.py` if that file exists; one call both checks and closes it",
  "v2": [
   25870514795,
   19602659328
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
  "missing": "[\"ls\", [\"rich\"]]"
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
  "planned": "[\"symbols\", [\"rich/console.py\", \"Group\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 3,
   "path": "rich/console.py",
   "filter": "Group",
   "header": {
    "lines": 2699,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "rich/console.py",
     "name": "Group",
     "line": 450,
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
    "examples/dynamic_progress.py",
    "Group",
    "reexport",
    [
     "rich.console",
     "rich/console.py"
    ]
   ],
   [
    "rich/console.py",
    "Group",
    "class",
    450
   ]
  ]
 }
}
```
</details>

## Step 4

There it is: `Group` is a class at `rich/console.py:450`. That settles the definition; now the imports of it.

I'll search the whole tree for imports of `Group` and star imports in one go; the search has to be complete before I can call the set final. Probably it fits under the cap. If nothing turns up, that finishes it; if it caps, I follow whatever it opens up.

**Call:** `grep('^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bGroup\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*Group\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$', '.')`

**Response**: outcome `mid`

```
docs/source/group.rst:9:    from rich.console import Group
examples/dynamic_progress.py:11:from rich.console import Group
examples/fullscreen.py:10:from rich.console import Console, Group
examples/group.py:2:from rich.console import Group
rich/__main__.py:7:from rich.console import Console, ConsoleOptions, Group, RenderableType, RenderResult
rich/_inspect.py:5:from .console import Group, RenderableType
rich/align.py:300:    from rich.console import Console, Group
rich/live.py:9:from .console import Console, ConsoleRenderable, Group, RenderableType, RenderHook
rich/progress.py:44:from .console import Console, Group, JustifyMethod, RenderableType
rich/screen.py:14:        Group,
rich/screen.py:34:        from rich.console import Group
rich/spinner.py:120:    from .console import Group
rich/traceback.py:37:    Group,
rich/tree.py:205:    from rich.console import Group
tests/test_live.py:178:    from rich.console import Group
tests/test_text.py:7:from rich.console import Console, Group
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
   "desc": "search `.` for imports of `Group`"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "STAR",
    "."
   ],
   "desc": "search `.` for star imports"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bGroup\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*Group\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bGroup\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*Group\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
   "v1": [
    1789548125,
    1104439714
   ],
   "v2": [
    1789548125,
    1104439714
   ],
   "p_cap": [
    3,
    37
   ],
   "forecast": {
    "zero": [
     13,
     37
    ],
    "mid": [
     21,
     37
    ],
    "cap": [
     3,
     37
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
   "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bGroup\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*Group\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
   "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+.*\\\\bGroup\\\\b|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*Group\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
   "v1": [
    947222553451,
    128503053210
   ],
   "v2": [
    164608867151,
    57983084985
   ],
   "p_cap": [
    1,
    35
   ],
   "forecast": {
    "zero": [
     24,
     35
    ],
    "mid": [
     2,
     7
    ],
    "cap": [
     1,
     35
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
    436376840171,
    128503053210
   ],
   "v2": [
    381010728811,
    128503053210
   ],
   "p_cap": [
    4,
    41
   ],
   "forecast": {
    "zero": [
     15,
     41
    ],
    "mid": [
     22,
     41
    ],
    "cap": [
     4,
     41
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
  "call": "grep('^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bGroup\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*Group\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$', '.')",
  "key": "[\"grep\", [\"^\\\\s*from\\\\s+\\\\S+\\\\s+import\\\\s+(?:.*\\\\bGroup\\\\b|\\\\*)|^\\\\s*(?:\\\\w+(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,\\\\s*)*Group\\\\b(?:\\\\s+as\\\\s+\\\\w+)?\\\\s*,?\\\\s*\\\\)?\\\\s*$\", \".\"]]",
  "provenance": "import and star lines under `.` in one call",
  "v2": [
   1789548125,
   1104439714
  ]
 },
 "forecast": {
  "zero": [
   13,
   37
  ],
  "mid": [
   21,
   37
  ],
  "cap": [
   3,
   37
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
    21,
    37
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
   "pattern": "^\\s*from\\s+\\S+\\s+import\\s+(?:.*\\bGroup\\b|\\*)|^\\s*(?:\\w+(?:\\s+as\\s+\\w+)?\\s*,\\s*)*Group\\b(?:\\s+as\\s+\\w+)?\\s*,?\\s*\\)?\\s*$",
   "scope": ".",
   "hits": [
    [
     "docs/source/group.rst",
     9
    ],
    [
     "examples/dynamic_progress.py",
     11
    ],
    [
     "examples/fullscreen.py",
     10
    ],
    [
     "examples/group.py",
     2
    ],
    [
     "rich/__main__.py",
     7
    ],
    [
     "rich/_inspect.py",
     5
    ],
    [
     "rich/align.py",
     300
    ],
    [
     "rich/live.py",
     9
    ],
    [
     "rich/progress.py",
     44
    ],
    [
     "rich/screen.py",
     14
    ],
    [
     "rich/screen.py",
     34
    ],
    [
     "rich/spinner.py",
     120
    ],
    [
     "rich/traceback.py",
     37
    ],
    [
     "rich/tree.py",
     205
    ],
    [
     "tests/test_live.py",
     178
    ],
    [
     "tests/test_text.py",
     7
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 2,
  "of": 2,
  "candidates": [
   "examples/dynamic_progress.py",
   "examples/fullscreen.py",
   "examples/group.py",
   "rich/__main__.py",
   "rich/_inspect.py",
   "rich/align.py",
   "rich/live.py",
   "rich/progress.py",
   "rich/screen.py",
   "rich/spinner.py",
   "rich/traceback.py",
   "rich/tree.py",
   "tests/test_live.py",
   "tests/test_text.py"
  ],
  "table": [
   [
    "examples/dynamic_progress.py",
    "examples/dynamic_progress.py:11",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "examples/fullscreen.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "examples/group.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "rich/__main__.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "rich/_inspect.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "rich/align.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "rich/live.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "rich/progress.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "rich/screen.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "rich/spinner.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "rich/traceback.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "rich/tree.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_live.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_text.py",
    null,
    "pending",
    "not yet examined"
   ]
  ],
  "uncovered": {
   "IMP
```
</details>

## Step 5

16 matching lines anywhere for imports of `Group` or star imports, in `docs/source/group.rst`, `examples/dynamic_progress.py`, `examples/fullscreen.py`, `examples/group.py` and 11 more files, and the search was under the cap, so that is the complete set there.

Let me look at `rich/_inspect.py`'s top-level names for `Group`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `examples/fullscreen.py`'s top-level names for `Group`.

**Call:** `symbols('rich/_inspect.py', 'Group')`

**Response**: outcome `ok`

```
module rich/_inspect.py lines=273 dynamic=no all=none
5 from Group <- .console Group
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "examples/fullscreen.py",
    "Group"
   ],
   "desc": "look at `examples/fullscreen.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "examples/group.py",
    "Group"
   ],
   "desc": "look at `examples/group.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/__main__.py",
    "Group"
   ],
   "desc": "look at `rich/__main__.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/_inspect.py",
    "Group"
   ],
   "desc": "look at `rich/_inspect.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/align.py",
    "Group"
   ],
   "desc": "look at `rich/align.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/live.py",
    "Group"
   ],
   "desc": "look at `rich/live.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/progress.py",
    "Group"
   ],
   "desc": "look at `rich/progress.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/screen.py",
    "Group"
   ],
   "desc": "look at `rich/screen.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/spinner.py",
    "Group"
   ],
   "desc": "look at `rich/spinner.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/traceback.py",
    "Group"
   ],
   "desc": "look at `rich/traceback.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/tree.py",
    "Group"
   ],
   "desc": "look at `rich/tree.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_live.py",
    "Group"
   ],
   "desc": "look at `tests/test_live.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_text.py",
    "Group"
   ],
   "desc": "look at `tests/test_text.py`'s imports of `Group`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('examples/fullscreen.py', 'Group')",
   "key": "[\"symbols\", [\"examples/fullscreen.py\", \"Group\"]]",
   "v1": [
    20961567,
    895850
   ],
   "v2": [
    10489742,
    447925
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
     "examples/fullscreen.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('examples/group.py', 'Group')",
   "key": "[\"symbols\", [\"examples/group.py\", \"Group\"]]",
   "v1": [
    20961567,
    895850
   ],
   "v2": [
    10489742,
    447925
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
     "examples/group.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/__main__.py', 'Group')",
   "key": "[\"symbols\", [\"rich/__main__.py\", \"Group\"]]",
   "v1": [
    20961567,
    895850
   ],
   "v2": [
    10489742,
    447925
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
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/_inspect.py', 'Group')",
   "key": "[\"symbols\", [\"rich/_inspect.py\", \"Group\"]]",
   "v1": [
    20961567,
    895850
   ],
   "v2": [
    10489742,
    447925
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
     "rich/_inspect.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/align.py', 'Group')",
   "key": "[\"symbols\", [\"rich/align.py\", \"Group\"]]",
   "v1": [
    20961567,
    895850
   ],
   "v2": [
    10489742,
    447925
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
     "rich/align.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/live.py', 'Group')",
   "key": "[\"symbols\", [\"rich/live.py\", \"Group\"]]",
   "v1": [
    20961567,
    895850
   ],
   "v2": [
    10489742,
    447925
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
     "rich/live.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/progress.py', 'Group')",
   "key": "[\"symbols\", [\"rich/progress.py\", \"Group\"]]",
   "v1": [
    20961567,
    895850
   ],
   "v2": [
    10489742,
    447925
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
     "rich/progress.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/screen.py', 'Group')",
   "key": "[\"symbols\", [\"rich/screen.py\", \"Group\"]]",
   "v1": [
    20961567,
    895850
   ],
   "v2": [
    10489742,
    447925
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
     "rich/screen.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/spinner.py', 'Group')",
   "key": "[\"symbols\", [\"rich/spinner.py\", \"Group\"]]",
   "v1": [
    20961567,
    895850
   ],
   "v2": [
    10489742,
    447925
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
     "rich/spinner.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/traceback.py', 'Group')",
   "key": "[\"symbols\", [\"rich/traceback.py\", \
```
</details>

## Step 6

`rich/_inspect.py`: line 5 imports it from `.console`.

Tally: 2 import statements confirmed, 0 ruled out, 12 pending. The search itself is complete; what is left is checking the candidates.

Next I will look at `examples/fullscreen.py`'s top-level names for `Group`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `examples/group.py`'s top-level names for `Group`.

**Call:** `symbols('examples/fullscreen.py', 'Group')`

**Response**: outcome `ok`

```
module examples/fullscreen.py lines=177 dynamic=no all=none
10 from Group <- rich.console Group
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "examples/fullscreen.py",
    "Group"
   ],
   "desc": "look at `examples/fullscreen.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "examples/group.py",
    "Group"
   ],
   "desc": "look at `examples/group.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/__main__.py",
    "Group"
   ],
   "desc": "look at `rich/__main__.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/align.py",
    "Group"
   ],
   "desc": "look at `rich/align.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/live.py",
    "Group"
   ],
   "desc": "look at `rich/live.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/progress.py",
    "Group"
   ],
   "desc": "look at `rich/progress.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/screen.py",
    "Group"
   ],
   "desc": "look at `rich/screen.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/spinner.py",
    "Group"
   ],
   "desc": "look at `rich/spinner.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/traceback.py",
    "Group"
   ],
   "desc": "look at `rich/traceback.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/tree.py",
    "Group"
   ],
   "desc": "look at `rich/tree.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_live.py",
    "Group"
   ],
   "desc": "look at `tests/test_live.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_text.py",
    "Group"
   ],
   "desc": "look at `tests/test_text.py`'s imports of `Group`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('examples/fullscreen.py', 'Group')",
   "key": "[\"symbols\", [\"examples/fullscreen.py\", \"Group\"]]",
   "v1": [
    19350517,
    895850
   ],
   "v2": [
    9684217,
    447925
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
     "examples/fullscreen.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('examples/group.py', 'Group')",
   "key": "[\"symbols\", [\"examples/group.py\", \"Group\"]]",
   "v1": [
    19350517,
    895850
   ],
   "v2": [
    9684217,
    447925
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
     "examples/group.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/__main__.py', 'Group')",
   "key": "[\"symbols\", [\"rich/__main__.py\", \"Group\"]]",
   "v1": [
    19350517,
    895850
   ],
   "v2": [
    9684217,
    447925
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
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/align.py', 'Group')",
   "key": "[\"symbols\", [\"rich/align.py\", \"Group\"]]",
   "v1": [
    19350517,
    895850
   ],
   "v2": [
    9684217,
    447925
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
     "rich/align.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/live.py', 'Group')",
   "key": "[\"symbols\", [\"rich/live.py\", \"Group\"]]",
   "v1": [
    19350517,
    895850
   ],
   "v2": [
    9684217,
    447925
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
     "rich/live.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/progress.py', 'Group')",
   "key": "[\"symbols\", [\"rich/progress.py\", \"Group\"]]",
   "v1": [
    19350517,
    895850
   ],
   "v2": [
    9684217,
    447925
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
     "rich/progress.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/screen.py', 'Group')",
   "key": "[\"symbols\", [\"rich/screen.py\", \"Group\"]]",
   "v1": [
    19350517,
    895850
   ],
   "v2": [
    9684217,
    447925
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
     "rich/screen.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/spinner.py', 'Group')",
   "key": "[\"symbols\", [\"rich/spinner.py\", \"Group\"]]",
   "v1": [
    19350517,
    895850
   ],
   "v2": [
    9684217,
    447925
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
     "rich/spinner.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/traceback.py', 'Group')",
   "key": "[\"symbols\", [\"rich/traceback.py\", \"Group\"]]",
   "v1": [
    19350517,
    895850
   ],
   "v2": [
    9684217,
    447925
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
     "rich/traceback.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/tree.py', 'Group')",
   "key": "[\"symbols\", [\"rich/tree.py\", \"Group\"]]",
   "v1": [
    19350517,
    895850
   ],
   "v2": [
    9684217,
    447925
   ],
   "p_cap": [
    1,
    50
   ],
   "forecast": {
    "ok": [
     49,
     50
 
```
</details>

## Step 7

`examples/fullscreen.py`: line 10 imports it from `rich.console`.

Tally: 3 import statements confirmed, 0 ruled out, 11 pending. The search itself is complete; what is left is checking the candidates.

Next I will look at `examples/group.py`'s top-level names for `Group`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `rich/__main__.py`'s top-level names for `Group`.

**Call:** `symbols('examples/group.py', 'Group')`

**Response**: outcome `ok`

```
module examples/group.py lines=10 dynamic=no all=none
2 from Group <- rich.console Group
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "examples/group.py",
    "Group"
   ],
   "desc": "look at `examples/group.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/__main__.py",
    "Group"
   ],
   "desc": "look at `rich/__main__.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/align.py",
    "Group"
   ],
   "desc": "look at `rich/align.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/live.py",
    "Group"
   ],
   "desc": "look at `rich/live.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/progress.py",
    "Group"
   ],
   "desc": "look at `rich/progress.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/screen.py",
    "Group"
   ],
   "desc": "look at `rich/screen.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/spinner.py",
    "Group"
   ],
   "desc": "look at `rich/spinner.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/traceback.py",
    "Group"
   ],
   "desc": "look at `rich/traceback.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/tree.py",
    "Group"
   ],
   "desc": "look at `rich/tree.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_live.py",
    "Group"
   ],
   "desc": "look at `tests/test_live.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_text.py",
    "Group"
   ],
   "desc": "look at `tests/test_text.py`'s imports of `Group`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('examples/group.py', 'Group')",
   "key": "[\"symbols\", [\"examples/group.py\", \"Group\"]]",
   "v1": [
    17739467,
    895850
   ],
   "v2": [
    8878692,
    447925
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
     "examples/group.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/__main__.py', 'Group')",
   "key": "[\"symbols\", [\"rich/__main__.py\", \"Group\"]]",
   "v1": [
    17739467,
    895850
   ],
   "v2": [
    8878692,
    447925
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
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/align.py', 'Group')",
   "key": "[\"symbols\", [\"rich/align.py\", \"Group\"]]",
   "v1": [
    17739467,
    895850
   ],
   "v2": [
    8878692,
    447925
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
     "rich/align.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/live.py', 'Group')",
   "key": "[\"symbols\", [\"rich/live.py\", \"Group\"]]",
   "v1": [
    17739467,
    895850
   ],
   "v2": [
    8878692,
    447925
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
     "rich/live.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/progress.py', 'Group')",
   "key": "[\"symbols\", [\"rich/progress.py\", \"Group\"]]",
   "v1": [
    17739467,
    895850
   ],
   "v2": [
    8878692,
    447925
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
     "rich/progress.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/screen.py', 'Group')",
   "key": "[\"symbols\", [\"rich/screen.py\", \"Group\"]]",
   "v1": [
    17739467,
    895850
   ],
   "v2": [
    8878692,
    447925
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
     "rich/screen.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/spinner.py', 'Group')",
   "key": "[\"symbols\", [\"rich/spinner.py\", \"Group\"]]",
   "v1": [
    17739467,
    895850
   ],
   "v2": [
    8878692,
    447925
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
     "rich/spinner.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/traceback.py', 'Group')",
   "key": "[\"symbols\", [\"rich/traceback.py\", \"Group\"]]",
   "v1": [
    17739467,
    895850
   ],
   "v2": [
    8878692,
    447925
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
     "rich/traceback.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/tree.py', 'Group')",
   "key": "[\"symbols\", [\"rich/tree.py\", \"Group\"]]",
   "v1": [
    17739467,
    895850
   ],
   "v2": [
    8878692,
    447925
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
     "rich/tree.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_live.py', 'Group')",
   "key": "[\"symbols\", [\"tests/test_live.py\", \"Group\"]]",
   "v1": [
    17739467,
    895850
   ],
   "v2": [
    8878692,
    447925
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
     "tests/test_live.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_text.py', 'Grou
```
</details>

## Step 8

`examples/group.py`: line 2 imports it from `rich.console`.

Tally: 4 import statements confirmed, 0 ruled out, 10 pending. The search itself is complete; what is left is checking the candidates.

Still open: look at `rich/__main__.py`'s imports of `Group`; look at `rich/align.py`'s imports of `Group`; look at `rich/live.py`'s imports of `Group`; and 7 more.

I'll look at `rich/__main__.py`'s top-level names for `Group`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `rich/align.py`'s top-level names for `Group`.

**Call:** `symbols('rich/__main__.py', 'Group')`

**Response**: outcome `ok`

```
module rich/__main__.py lines=246 dynamic=no all=none
7 from Group <- rich.console Group
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
    "Group"
   ],
   "desc": "look at `rich/__main__.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/align.py",
    "Group"
   ],
   "desc": "look at `rich/align.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/live.py",
    "Group"
   ],
   "desc": "look at `rich/live.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/progress.py",
    "Group"
   ],
   "desc": "look at `rich/progress.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/screen.py",
    "Group"
   ],
   "desc": "look at `rich/screen.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/spinner.py",
    "Group"
   ],
   "desc": "look at `rich/spinner.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/traceback.py",
    "Group"
   ],
   "desc": "look at `rich/traceback.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/tree.py",
    "Group"
   ],
   "desc": "look at `rich/tree.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_live.py",
    "Group"
   ],
   "desc": "look at `tests/test_live.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_text.py",
    "Group"
   ],
   "desc": "look at `tests/test_text.py`'s imports of `Group`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('rich/__main__.py', 'Group')",
   "key": "[\"symbols\", [\"rich/__main__.py\", \"Group\"]]",
   "v1": [
    16128417,
    895850
   ],
   "v2": [
    8073167,
    447925
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
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/align.py', 'Group')",
   "key": "[\"symbols\", [\"rich/align.py\", \"Group\"]]",
   "v1": [
    16128417,
    895850
   ],
   "v2": [
    8073167,
    447925
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
     "rich/align.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/live.py', 'Group')",
   "key": "[\"symbols\", [\"rich/live.py\", \"Group\"]]",
   "v1": [
    16128417,
    895850
   ],
   "v2": [
    8073167,
    447925
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
     "rich/live.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/progress.py', 'Group')",
   "key": "[\"symbols\", [\"rich/progress.py\", \"Group\"]]",
   "v1": [
    16128417,
    895850
   ],
   "v2": [
    8073167,
    447925
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
     "rich/progress.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/screen.py', 'Group')",
   "key": "[\"symbols\", [\"rich/screen.py\", \"Group\"]]",
   "v1": [
    16128417,
    895850
   ],
   "v2": [
    8073167,
    447925
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
     "rich/screen.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/spinner.py', 'Group')",
   "key": "[\"symbols\", [\"rich/spinner.py\", \"Group\"]]",
   "v1": [
    16128417,
    895850
   ],
   "v2": [
    8073167,
    447925
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
     "rich/spinner.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/traceback.py', 'Group')",
   "key": "[\"symbols\", [\"rich/traceback.py\", \"Group\"]]",
   "v1": [
    16128417,
    895850
   ],
   "v2": [
    8073167,
    447925
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
     "rich/traceback.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/tree.py', 'Group')",
   "key": "[\"symbols\", [\"rich/tree.py\", \"Group\"]]",
   "v1": [
    16128417,
    895850
   ],
   "v2": [
    8073167,
    447925
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
     "rich/tree.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_live.py', 'Group')",
   "key": "[\"symbols\", [\"tests/test_live.py\", \"Group\"]]",
   "v1": [
    16128417,
    895850
   ],
   "v2": [
    8073167,
    447925
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
     "tests/test_live.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_text.py', 'Group')",
   "key": "[\"symbols\", [\"tests/test_text.py\", \"Group\"]]",
   "v1": [
    16128417,
    895850
   ],
   "v2": [
    8073167,
    447925
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
     "tests/test_text.py",
     "Group"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('rich/__main__.py', 'Group')",
  "key": "[\"symbols\", [\"rich/__main__.py\", \"Group\"]]",
  "provenance": "`rich/__main__.py` had a matching line (step 4); its outline names 
```
</details>

## Step 9

`rich/__main__.py`: line 7 imports it from `rich.console`.

Tally: 5 import statements confirmed, 0 ruled out, 9 pending. The search itself is complete; what is left is checking the candidates.

Let me look at `rich/align.py`'s top-level names for `Group`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `rich/live.py`'s top-level names for `Group`.

**Call:** `symbols('rich/align.py', 'Group')`

**Response**: outcome `ok`

```
module rich/align.py lines=321 dynamic=no all=none
300 from Group <- rich.console Group
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/align.py",
    "Group"
   ],
   "desc": "look at `rich/align.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/live.py",
    "Group"
   ],
   "desc": "look at `rich/live.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/progress.py",
    "Group"
   ],
   "desc": "look at `rich/progress.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/screen.py",
    "Group"
   ],
   "desc": "look at `rich/screen.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/spinner.py",
    "Group"
   ],
   "desc": "look at `rich/spinner.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/traceback.py",
    "Group"
   ],
   "desc": "look at `rich/traceback.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/tree.py",
    "Group"
   ],
   "desc": "look at `rich/tree.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_live.py",
    "Group"
   ],
   "desc": "look at `tests/test_live.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_text.py",
    "Group"
   ],
   "desc": "look at `tests/test_text.py`'s imports of `Group`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('rich/align.py', 'Group')",
   "key": "[\"symbols\", [\"rich/align.py\", \"Group\"]]",
   "v1": [
    14517367,
    895850
   ],
   "v2": [
    7267642,
    447925
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
     "rich/align.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/live.py', 'Group')",
   "key": "[\"symbols\", [\"rich/live.py\", \"Group\"]]",
   "v1": [
    14517367,
    895850
   ],
   "v2": [
    7267642,
    447925
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
     "rich/live.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/progress.py', 'Group')",
   "key": "[\"symbols\", [\"rich/progress.py\", \"Group\"]]",
   "v1": [
    14517367,
    895850
   ],
   "v2": [
    7267642,
    447925
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
     "rich/progress.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/screen.py', 'Group')",
   "key": "[\"symbols\", [\"rich/screen.py\", \"Group\"]]",
   "v1": [
    14517367,
    895850
   ],
   "v2": [
    7267642,
    447925
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
     "rich/screen.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/spinner.py', 'Group')",
   "key": "[\"symbols\", [\"rich/spinner.py\", \"Group\"]]",
   "v1": [
    14517367,
    895850
   ],
   "v2": [
    7267642,
    447925
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
     "rich/spinner.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/traceback.py', 'Group')",
   "key": "[\"symbols\", [\"rich/traceback.py\", \"Group\"]]",
   "v1": [
    14517367,
    895850
   ],
   "v2": [
    7267642,
    447925
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
     "rich/traceback.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/tree.py', 'Group')",
   "key": "[\"symbols\", [\"rich/tree.py\", \"Group\"]]",
   "v1": [
    14517367,
    895850
   ],
   "v2": [
    7267642,
    447925
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
     "rich/tree.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_live.py', 'Group')",
   "key": "[\"symbols\", [\"tests/test_live.py\", \"Group\"]]",
   "v1": [
    14517367,
    895850
   ],
   "v2": [
    7267642,
    447925
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
     "tests/test_live.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_text.py', 'Group')",
   "key": "[\"symbols\", [\"tests/test_text.py\", \"Group\"]]",
   "v1": [
    14517367,
    895850
   ],
   "v2": [
    7267642,
    447925
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
     "tests/test_text.py",
     "Group"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('rich/align.py', 'Group')",
  "key": "[\"symbols\", [\"rich/align.py\", \"Group\"]]",
  "provenance": "`rich/align.py` had a matching line (step 4); its outline names every `Group` import exactly",
  "v2": [
   7267642,
   447925
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
  "ok": "[\"symbols\", [\"rich/live.py\", \"Group\"]]",
  "cap": "[\"symbols\", [\"rich/live.py\", \"Group\"]]"
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
  "planned": "[\"symbols\", [\"rich/align.py\", \"Group\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 9,
   "path": "rich/align.py",
   "filter": "Group",
   "
```
</details>

## Step 10

`rich/align.py`: line 300 imports it from `rich.console`.

Tally: 6 import statements confirmed, 0 ruled out, 8 pending. The search itself is complete; what is left is checking the candidates.

Let me look at `rich/live.py`'s top-level names for `Group`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `rich/progress.py`'s top-level names for `Group`.

**Call:** `symbols('rich/live.py', 'Group')`

**Response**: outcome `ok`

```
module rich/live.py lines=405 dynamic=no all=none
9 from Group <- .console Group
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/live.py",
    "Group"
   ],
   "desc": "look at `rich/live.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/progress.py",
    "Group"
   ],
   "desc": "look at `rich/progress.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/screen.py",
    "Group"
   ],
   "desc": "look at `rich/screen.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/spinner.py",
    "Group"
   ],
   "desc": "look at `rich/spinner.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/traceback.py",
    "Group"
   ],
   "desc": "look at `rich/traceback.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/tree.py",
    "Group"
   ],
   "desc": "look at `rich/tree.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_live.py",
    "Group"
   ],
   "desc": "look at `tests/test_live.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_text.py",
    "Group"
   ],
   "desc": "look at `tests/test_text.py`'s imports of `Group`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('rich/live.py', 'Group')",
   "key": "[\"symbols\", [\"rich/live.py\", \"Group\"]]",
   "v1": [
    12906317,
    895850
   ],
   "v2": [
    6462117,
    447925
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
     "rich/live.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/progress.py', 'Group')",
   "key": "[\"symbols\", [\"rich/progress.py\", \"Group\"]]",
   "v1": [
    12906317,
    895850
   ],
   "v2": [
    6462117,
    447925
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
     "rich/progress.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/screen.py', 'Group')",
   "key": "[\"symbols\", [\"rich/screen.py\", \"Group\"]]",
   "v1": [
    12906317,
    895850
   ],
   "v2": [
    6462117,
    447925
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
     "rich/screen.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/spinner.py', 'Group')",
   "key": "[\"symbols\", [\"rich/spinner.py\", \"Group\"]]",
   "v1": [
    12906317,
    895850
   ],
   "v2": [
    6462117,
    447925
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
     "rich/spinner.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/traceback.py', 'Group')",
   "key": "[\"symbols\", [\"rich/traceback.py\", \"Group\"]]",
   "v1": [
    12906317,
    895850
   ],
   "v2": [
    6462117,
    447925
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
     "rich/traceback.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/tree.py', 'Group')",
   "key": "[\"symbols\", [\"rich/tree.py\", \"Group\"]]",
   "v1": [
    12906317,
    895850
   ],
   "v2": [
    6462117,
    447925
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
     "rich/tree.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_live.py', 'Group')",
   "key": "[\"symbols\", [\"tests/test_live.py\", \"Group\"]]",
   "v1": [
    12906317,
    895850
   ],
   "v2": [
    6462117,
    447925
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
     "tests/test_live.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_text.py', 'Group')",
   "key": "[\"symbols\", [\"tests/test_text.py\", \"Group\"]]",
   "v1": [
    12906317,
    895850
   ],
   "v2": [
    6462117,
    447925
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
     "tests/test_text.py",
     "Group"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('rich/live.py', 'Group')",
  "key": "[\"symbols\", [\"rich/live.py\", \"Group\"]]",
  "provenance": "`rich/live.py` had a matching line (step 4); its outline names every `Group` import exactly",
  "v2": [
   6462117,
   447925
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
  "ok": "[\"symbols\", [\"rich/progress.py\", \"Group\"]]",
  "cap": "[\"symbols\", [\"rich/progress.py\", \"Group\"]]"
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
  "planned": "[\"symbols\", [\"rich/live.py\", \"Group\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 10,
   "path": "rich/live.py",
   "filter": "Group",
   "header": {
    "lines": 405,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "rich/live.py",
     "name": "Group",
     "line": 9,
     "kind": "from",
     "src": ".console",
     "src_name": "Group",
     "conditional": false,
     "col": 0,
     "bases": []
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 2,
  "of": 2,
  "candidates": [
   "examples/dynamic_progress.py",
   "examples/fullscreen.py",
   "examples/group.py",
   "rich/__main__.py",
 
```
</details>

## Step 11

`rich/live.py`: line 9 imports it from `.console`.

Tally: 7 import statements confirmed, 0 ruled out, 7 pending. The search itself is complete; what is left is checking the candidates.

I'll look at `rich/progress.py`'s top-level names for `Group`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `rich/screen.py`'s top-level names for `Group`.

**Call:** `symbols('rich/progress.py', 'Group')`

**Response**: outcome `ok`

```
module rich/progress.py lines=1717 dynamic=no all=none
44 from Group <- .console Group
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/progress.py",
    "Group"
   ],
   "desc": "look at `rich/progress.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/screen.py",
    "Group"
   ],
   "desc": "look at `rich/screen.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/spinner.py",
    "Group"
   ],
   "desc": "look at `rich/spinner.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/traceback.py",
    "Group"
   ],
   "desc": "look at `rich/traceback.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/tree.py",
    "Group"
   ],
   "desc": "look at `rich/tree.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_live.py",
    "Group"
   ],
   "desc": "look at `tests/test_live.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_text.py",
    "Group"
   ],
   "desc": "look at `tests/test_text.py`'s imports of `Group`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('rich/progress.py', 'Group')",
   "key": "[\"symbols\", [\"rich/progress.py\", \"Group\"]]",
   "v1": [
    11295267,
    895850
   ],
   "v2": [
    5656592,
    447925
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
     "rich/progress.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/screen.py', 'Group')",
   "key": "[\"symbols\", [\"rich/screen.py\", \"Group\"]]",
   "v1": [
    11295267,
    895850
   ],
   "v2": [
    5656592,
    447925
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
     "rich/screen.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/spinner.py', 'Group')",
   "key": "[\"symbols\", [\"rich/spinner.py\", \"Group\"]]",
   "v1": [
    11295267,
    895850
   ],
   "v2": [
    5656592,
    447925
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
     "rich/spinner.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/traceback.py', 'Group')",
   "key": "[\"symbols\", [\"rich/traceback.py\", \"Group\"]]",
   "v1": [
    11295267,
    895850
   ],
   "v2": [
    5656592,
    447925
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
     "rich/traceback.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/tree.py', 'Group')",
   "key": "[\"symbols\", [\"rich/tree.py\", \"Group\"]]",
   "v1": [
    11295267,
    895850
   ],
   "v2": [
    5656592,
    447925
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
     "rich/tree.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_live.py', 'Group')",
   "key": "[\"symbols\", [\"tests/test_live.py\", \"Group\"]]",
   "v1": [
    11295267,
    895850
   ],
   "v2": [
    5656592,
    447925
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
     "tests/test_live.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_text.py', 'Group')",
   "key": "[\"symbols\", [\"tests/test_text.py\", \"Group\"]]",
   "v1": [
    11295267,
    895850
   ],
   "v2": [
    5656592,
    447925
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
     "tests/test_text.py",
     "Group"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('rich/progress.py', 'Group')",
  "key": "[\"symbols\", [\"rich/progress.py\", \"Group\"]]",
  "provenance": "`rich/progress.py` had a matching line (step 4); its outline names every `Group` import exactly",
  "v2": [
   5656592,
   447925
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
  "ok": "[\"symbols\", [\"rich/screen.py\", \"Group\"]]",
  "cap": "[\"symbols\", [\"rich/screen.py\", \"Group\"]]"
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
  "planned": "[\"symbols\", [\"rich/progress.py\", \"Group\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 11,
   "path": "rich/progress.py",
   "filter": "Group",
   "header": {
    "lines": 1717,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "rich/progress.py",
     "name": "Group",
     "line": 44,
     "kind": "from",
     "src": ".console",
     "src_name": "Group",
     "conditional": false,
     "col": 0,
     "bases": []
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 2,
  "of": 2,
  "candidates": [
   "examples/dynamic_progress.py",
   "examples/fullscreen.py",
   "examples/group.py",
   "rich/__main__.py",
   "rich/_inspect.py",
   "rich/align.py",
   "rich/live.py",
   "rich/progress.py",
   "rich/screen.py",
   "rich/spinner.py",
   "rich/traceback.py",
   "rich/tree.py",
   "tests/test_live.py",
   "tests/test_text.py"
  ],
  "table": [
   [
    "examples/dynamic_progress.py",
    "examples/dynamic_progress.py:11",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "examples/fullscreen.py",
    "examples/fullscreen.py:10",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "example
```
</details>

## Step 12

`rich/progress.py`: line 44 imports it from `.console`.

Tally: 8 import statements confirmed, 0 ruled out, 6 pending. The search itself is complete; what is left is checking the candidates.

Still open: look at `rich/screen.py`'s imports of `Group`; look at `rich/spinner.py`'s imports of `Group`; look at `rich/traceback.py`'s imports of `Group`; and 3 more.

Next I will look at `rich/screen.py`'s top-level names for `Group`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `rich/spinner.py`'s top-level names for `Group`.

**Call:** `symbols('rich/screen.py', 'Group')`

**Response**: outcome `ok`

```
module rich/screen.py lines=55 dynamic=no all=none
9 from Group <- .console Group
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/screen.py",
    "Group"
   ],
   "desc": "look at `rich/screen.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/spinner.py",
    "Group"
   ],
   "desc": "look at `rich/spinner.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/traceback.py",
    "Group"
   ],
   "desc": "look at `rich/traceback.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/tree.py",
    "Group"
   ],
   "desc": "look at `rich/tree.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_live.py",
    "Group"
   ],
   "desc": "look at `tests/test_live.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_text.py",
    "Group"
   ],
   "desc": "look at `tests/test_text.py`'s imports of `Group`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('rich/screen.py', 'Group')",
   "key": "[\"symbols\", [\"rich/screen.py\", \"Group\"]]",
   "v1": [
    9684217,
    895850
   ],
   "v2": [
    4851067,
    447925
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
     "rich/screen.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/spinner.py', 'Group')",
   "key": "[\"symbols\", [\"rich/spinner.py\", \"Group\"]]",
   "v1": [
    9684217,
    895850
   ],
   "v2": [
    4851067,
    447925
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
     "rich/spinner.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/traceback.py', 'Group')",
   "key": "[\"symbols\", [\"rich/traceback.py\", \"Group\"]]",
   "v1": [
    9684217,
    895850
   ],
   "v2": [
    4851067,
    447925
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
     "rich/traceback.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/tree.py', 'Group')",
   "key": "[\"symbols\", [\"rich/tree.py\", \"Group\"]]",
   "v1": [
    9684217,
    895850
   ],
   "v2": [
    4851067,
    447925
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
     "rich/tree.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_live.py', 'Group')",
   "key": "[\"symbols\", [\"tests/test_live.py\", \"Group\"]]",
   "v1": [
    9684217,
    895850
   ],
   "v2": [
    4851067,
    447925
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
     "tests/test_live.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_text.py', 'Group')",
   "key": "[\"symbols\", [\"tests/test_text.py\", \"Group\"]]",
   "v1": [
    9684217,
    895850
   ],
   "v2": [
    4851067,
    447925
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
     "tests/test_text.py",
     "Group"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('rich/screen.py', 'Group')",
  "key": "[\"symbols\", [\"rich/screen.py\", \"Group\"]]",
  "provenance": "`rich/screen.py` had a matching line (step 4); its outline names every `Group` import exactly",
  "v2": [
   4851067,
   447925
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
  "ok": "[\"symbols\", [\"rich/spinner.py\", \"Group\"]]",
  "cap": "[\"symbols\", [\"rich/spinner.py\", \"Group\"]]"
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
  "planned": "[\"symbols\", [\"rich/screen.py\", \"Group\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 12,
   "path": "rich/screen.py",
   "filter": "Group",
   "header": {
    "lines": 55,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "rich/screen.py",
     "name": "Group",
     "line": 9,
     "kind": "from",
     "src": ".console",
     "src_name": "Group",
     "conditional": false,
     "col": 0,
     "bases": []
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 2,
  "of": 2,
  "candidates": [
   "examples/dynamic_progress.py",
   "examples/fullscreen.py",
   "examples/group.py",
   "rich/__main__.py",
   "rich/_inspect.py",
   "rich/align.py",
   "rich/live.py",
   "rich/progress.py",
   "rich/screen.py",
   "rich/spinner.py",
   "rich/traceback.py",
   "rich/tree.py",
   "tests/test_live.py",
   "tests/test_text.py"
  ],
  "table": [
   [
    "examples/dynamic_progress.py",
    "examples/dynamic_progress.py:11",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "examples/fullscreen.py",
    "examples/fullscreen.py:10",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "examples/group.py",
    "examples/group.py:2",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "rich/__main__.py",
    "rich/__main__.py:7",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "rich/_inspect.py",
    "rich/_inspect.py:5",
    "in",
    "`.console` resolves `Group` to the target"
   ],
   [
    "rich/align.py",
    "rich/align.py:300",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "rich/live.py",
    "rich/live.py:9",
    "in",
    "`.console` resolves `Group` to the target"
   ],
   [
    "rich/prog
```
</details>

## Step 13

`rich/screen.py`: line 9 imports it from `.console`.

Tally: 9 import statements confirmed, 0 ruled out, 5 pending. The search itself is complete; what is left is checking the candidates.

I'll look at `rich/spinner.py`'s top-level names for `Group`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `rich/traceback.py`'s top-level names for `Group`.

**Call:** `symbols('rich/spinner.py', 'Group')`

**Response**: outcome `ok`

```
module rich/spinner.py lines=133 dynamic=no all=none
120 from Group <- .console Group
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/spinner.py",
    "Group"
   ],
   "desc": "look at `rich/spinner.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/traceback.py",
    "Group"
   ],
   "desc": "look at `rich/traceback.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/tree.py",
    "Group"
   ],
   "desc": "look at `rich/tree.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_live.py",
    "Group"
   ],
   "desc": "look at `tests/test_live.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_text.py",
    "Group"
   ],
   "desc": "look at `tests/test_text.py`'s imports of `Group`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('rich/spinner.py', 'Group')",
   "key": "[\"symbols\", [\"rich/spinner.py\", \"Group\"]]",
   "v1": [
    8073167,
    895850
   ],
   "v2": [
    4045542,
    447925
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
     "rich/spinner.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/traceback.py', 'Group')",
   "key": "[\"symbols\", [\"rich/traceback.py\", \"Group\"]]",
   "v1": [
    8073167,
    895850
   ],
   "v2": [
    4045542,
    447925
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
     "rich/traceback.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/tree.py', 'Group')",
   "key": "[\"symbols\", [\"rich/tree.py\", \"Group\"]]",
   "v1": [
    8073167,
    895850
   ],
   "v2": [
    4045542,
    447925
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
     "rich/tree.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_live.py', 'Group')",
   "key": "[\"symbols\", [\"tests/test_live.py\", \"Group\"]]",
   "v1": [
    8073167,
    895850
   ],
   "v2": [
    4045542,
    447925
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
     "tests/test_live.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_text.py', 'Group')",
   "key": "[\"symbols\", [\"tests/test_text.py\", \"Group\"]]",
   "v1": [
    8073167,
    895850
   ],
   "v2": [
    4045542,
    447925
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
     "tests/test_text.py",
     "Group"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('rich/spinner.py', 'Group')",
  "key": "[\"symbols\", [\"rich/spinner.py\", \"Group\"]]",
  "provenance": "`rich/spinner.py` had a matching line (step 4); its outline names every `Group` import exactly",
  "v2": [
   4045542,
   447925
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
  "ok": "[\"symbols\", [\"rich/traceback.py\", \"Group\"]]",
  "cap": "[\"symbols\", [\"rich/traceback.py\", \"Group\"]]"
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
  "planned": "[\"symbols\", [\"rich/spinner.py\", \"Group\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 13,
   "path": "rich/spinner.py",
   "filter": "Group",
   "header": {
    "lines": 133,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "rich/spinner.py",
     "name": "Group",
     "line": 120,
     "kind": "from",
     "src": ".console",
     "src_name": "Group",
     "conditional": false,
     "col": 0,
     "bases": []
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 2,
  "of": 2,
  "candidates": [
   "examples/dynamic_progress.py",
   "examples/fullscreen.py",
   "examples/group.py",
   "rich/__main__.py",
   "rich/_inspect.py",
   "rich/align.py",
   "rich/live.py",
   "rich/progress.py",
   "rich/screen.py",
   "rich/spinner.py",
   "rich/traceback.py",
   "rich/tree.py",
   "tests/test_live.py",
   "tests/test_text.py"
  ],
  "table": [
   [
    "examples/dynamic_progress.py",
    "examples/dynamic_progress.py:11",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "examples/fullscreen.py",
    "examples/fullscreen.py:10",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "examples/group.py",
    "examples/group.py:2",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "rich/__main__.py",
    "rich/__main__.py:7",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "rich/_inspect.py",
    "rich/_inspect.py:5",
    "in",
    "`.console` resolves `Group` to the target"
   ],
   [
    "rich/align.py",
    "rich/align.py:300",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "rich/live.py",
    "rich/live.py:9",
    "in",
    "`.console` resolves `Group` to the target"
   ],
   [
    "rich/progress.py",
    "rich/progress.py:44",
    "in",
    "`.console` resolves `Group` to the target"
   ],
   [
    "rich/screen.py",
    "rich/screen.py:9",
    "in",
    "`.console` resolves `Group` to the target"
   ],
   [
    "rich/spinner.py",
    "rich/spinner.py:120",
    "in",
    "`.console` resolves `Group` to the target"
   ],
   [
    "rich/traceback.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "rich/tree.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_live.py",
    null,
    "pending",
  
```
</details>

## Step 14

`rich/spinner.py`: line 120 imports it from `.console`.

Tally: 10 import statements confirmed, 0 ruled out, 4 pending. The search itself is complete; what is left is checking the candidates.

Next I will look at `rich/traceback.py`'s top-level names for `Group`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `rich/tree.py`'s top-level names for `Group`.

**Call:** `symbols('rich/traceback.py', 'Group')`

**Response**: outcome `ok`

```
module rich/traceback.py lines=925 dynamic=no all=none
32 from Group <- .console Group
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/traceback.py",
    "Group"
   ],
   "desc": "look at `rich/traceback.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/tree.py",
    "Group"
   ],
   "desc": "look at `rich/tree.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_live.py",
    "Group"
   ],
   "desc": "look at `tests/test_live.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_text.py",
    "Group"
   ],
   "desc": "look at `tests/test_text.py`'s imports of `Group`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('rich/traceback.py', 'Group')",
   "key": "[\"symbols\", [\"rich/traceback.py\", \"Group\"]]",
   "v1": [
    6462117,
    895850
   ],
   "v2": [
    3240017,
    447925
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
     "rich/traceback.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('rich/tree.py', 'Group')",
   "key": "[\"symbols\", [\"rich/tree.py\", \"Group\"]]",
   "v1": [
    6462117,
    895850
   ],
   "v2": [
    3240017,
    447925
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
     "rich/tree.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_live.py', 'Group')",
   "key": "[\"symbols\", [\"tests/test_live.py\", \"Group\"]]",
   "v1": [
    6462117,
    895850
   ],
   "v2": [
    3240017,
    447925
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
     "tests/test_live.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_text.py', 'Group')",
   "key": "[\"symbols\", [\"tests/test_text.py\", \"Group\"]]",
   "v1": [
    6462117,
    895850
   ],
   "v2": [
    3240017,
    447925
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
     "tests/test_text.py",
     "Group"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('rich/traceback.py', 'Group')",
  "key": "[\"symbols\", [\"rich/traceback.py\", \"Group\"]]",
  "provenance": "`rich/traceback.py` had a matching line (step 4); its outline names every `Group` import exactly",
  "v2": [
   3240017,
   447925
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
  "ok": "[\"symbols\", [\"rich/tree.py\", \"Group\"]]",
  "cap": "[\"symbols\", [\"rich/tree.py\", \"Group\"]]"
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
  "planned": "[\"symbols\", [\"rich/traceback.py\", \"Group\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 14,
   "path": "rich/traceback.py",
   "filter": "Group",
   "header": {
    "lines": 925,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "rich/traceback.py",
     "name": "Group",
     "line": 32,
     "kind": "from",
     "src": ".console",
     "src_name": "Group",
     "conditional": false,
     "col": 0,
     "bases": []
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 2,
  "of": 2,
  "candidates": [
   "examples/dynamic_progress.py",
   "examples/fullscreen.py",
   "examples/group.py",
   "rich/__main__.py",
   "rich/_inspect.py",
   "rich/align.py",
   "rich/live.py",
   "rich/progress.py",
   "rich/screen.py",
   "rich/spinner.py",
   "rich/traceback.py",
   "rich/tree.py",
   "tests/test_live.py",
   "tests/test_text.py"
  ],
  "table": [
   [
    "examples/dynamic_progress.py",
    "examples/dynamic_progress.py:11",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "examples/fullscreen.py",
    "examples/fullscreen.py:10",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "examples/group.py",
    "examples/group.py:2",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "rich/__main__.py",
    "rich/__main__.py:7",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "rich/_inspect.py",
    "rich/_inspect.py:5",
    "in",
    "`.console` resolves `Group` to the target"
   ],
   [
    "rich/align.py",
    "rich/align.py:300",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "rich/live.py",
    "rich/live.py:9",
    "in",
    "`.console` resolves `Group` to the target"
   ],
   [
    "rich/progress.py",
    "rich/progress.py:44",
    "in",
    "`.console` resolves `Group` to the target"
   ],
   [
    "rich/screen.py",
    "rich/screen.py:9",
    "in",
    "`.console` resolves `Group` to the target"
   ],
   [
    "rich/spinner.py",
    "rich/spinner.py:120",
    "in",
    "`.console` resolves `Group` to the target"
   ],
   [
    "rich/traceback.py",
    "rich/traceback.py:32",
    "in",
    "`.console` resolves `Group` to the target"
   ],
   [
    "rich/tree.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_live.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_text.py",
    null,
    "pending",
    "not yet examined"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  },
  "n_in": 11,
  "n_out": 0,
  "n_pending": 3
 }
}
```
</details>

## Step 15

`rich/traceback.py`: line 32 imports it from `.console`.

Tally: 11 import statements confirmed, 0 ruled out, 3 pending. The search itself is complete; what is left is checking the candidates.

Let me look at `rich/tree.py`'s top-level names for `Group`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `tests/test_live.py`'s top-level names for `Group`.

**Call:** `symbols('rich/tree.py', 'Group')`

**Response**: outcome `ok`

```
module rich/tree.py lines=258 dynamic=no all=none
205 from Group <- rich.console Group
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "rich/tree.py",
    "Group"
   ],
   "desc": "look at `rich/tree.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_live.py",
    "Group"
   ],
   "desc": "look at `tests/test_live.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_text.py",
    "Group"
   ],
   "desc": "look at `tests/test_text.py`'s imports of `Group`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('rich/tree.py', 'Group')",
   "key": "[\"symbols\", [\"rich/tree.py\", \"Group\"]]",
   "v1": [
    4851067,
    895850
   ],
   "v2": [
    2434492,
    447925
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
     "rich/tree.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_live.py', 'Group')",
   "key": "[\"symbols\", [\"tests/test_live.py\", \"Group\"]]",
   "v1": [
    4851067,
    895850
   ],
   "v2": [
    2434492,
    447925
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
     "tests/test_live.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_text.py', 'Group')",
   "key": "[\"symbols\", [\"tests/test_text.py\", \"Group\"]]",
   "v1": [
    4851067,
    895850
   ],
   "v2": [
    2434492,
    447925
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
     "tests/test_text.py",
     "Group"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('rich/tree.py', 'Group')",
  "key": "[\"symbols\", [\"rich/tree.py\", \"Group\"]]",
  "provenance": "`rich/tree.py` had a matching line (step 4); its outline names every `Group` import exactly",
  "v2": [
   2434492,
   447925
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
  "ok": "[\"symbols\", [\"tests/test_live.py\", \"Group\"]]",
  "cap": "[\"symbols\", [\"tests/test_live.py\", \"Group\"]]"
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
  "planned": "[\"symbols\", [\"rich/tree.py\", \"Group\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 15,
   "path": "rich/tree.py",
   "filter": "Group",
   "header": {
    "lines": 258,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "rich/tree.py",
     "name": "Group",
     "line": 205,
     "kind": "from",
     "src": "rich.console",
     "src_name": "Group",
     "conditional": false,
     "col": 0,
     "bases": []
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 2,
  "of": 2,
  "candidates": [
   "examples/dynamic_progress.py",
   "examples/fullscreen.py",
   "examples/group.py",
   "rich/__main__.py",
   "rich/_inspect.py",
   "rich/align.py",
   "rich/live.py",
   "rich/progress.py",
   "rich/screen.py",
   "rich/spinner.py",
   "rich/traceback.py",
   "rich/tree.py",
   "tests/test_live.py",
   "tests/test_text.py"
  ],
  "table": [
   [
    "examples/dynamic_progress.py",
    "examples/dynamic_progress.py:11",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "examples/fullscreen.py",
    "examples/fullscreen.py:10",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "examples/group.py",
    "examples/group.py:2",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "rich/__main__.py",
    "rich/__main__.py:7",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "rich/_inspect.py",
    "rich/_inspect.py:5",
    "in",
    "`.console` resolves `Group` to the target"
   ],
   [
    "rich/align.py",
    "rich/align.py:300",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "rich/live.py",
    "rich/live.py:9",
    "in",
    "`.console` resolves `Group` to the target"
   ],
   [
    "rich/progress.py",
    "rich/progress.py:44",
    "in",
    "`.console` resolves `Group` to the target"
   ],
   [
    "rich/screen.py",
    "rich/screen.py:9",
    "in",
    "`.console` resolves `Group` to the target"
   ],
   [
    "rich/spinner.py",
    "rich/spinner.py:120",
    "in",
    "`.console` resolves `Group` to the target"
   ],
   [
    "rich/traceback.py",
    "rich/traceback.py:32",
    "in",
    "`.console` resolves `Group` to the target"
   ],
   [
    "rich/tree.py",
    "rich/tree.py:205",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "tests/test_live.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_text.py",
    null,
    "pending",
    "not yet examined"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  },
  "n_in": 12,
  "n_out": 0,
  "n_pending": 2
 }
}
```
</details>

## Step 16

`rich/tree.py`: line 205 imports it from `rich.console`.

Tally: 12 import statements confirmed, 0 ruled out, 2 pending. The search itself is complete; what is left is checking the candidates.

I'll look at `tests/test_live.py`'s top-level names for `Group`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `tests/test_text.py`'s top-level names for `Group`.

**Call:** `symbols('tests/test_live.py', 'Group')`

**Response**: outcome `ok`

```
module tests/test_live.py lines=188 dynamic=no all=none
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_live.py",
    "Group"
   ],
   "desc": "look at `tests/test_live.py`'s imports of `Group`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_text.py",
    "Group"
   ],
   "desc": "look at `tests/test_text.py`'s imports of `Group`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/test_live.py', 'Group')",
   "key": "[\"symbols\", [\"tests/test_live.py\", \"Group\"]]",
   "v1": [
    3240017,
    895850
   ],
   "v2": [
    1628967,
    447925
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
     "tests/test_live.py",
     "Group"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_text.py', 'Group')",
   "key": "[\"symbols\", [\"tests/test_text.py\", \"Group\"]]",
   "v1": [
    3240017,
    895850
   ],
   "v2": [
    1628967,
    447925
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
     "tests/test_text.py",
     "Group"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_live.py', 'Group')",
  "key": "[\"symbols\", [\"tests/test_live.py\", \"Group\"]]",
  "provenance": "`tests/test_live.py` had a matching line (step 4); its outline names every `Group` import exactly",
  "v2": [
   1628967,
   447925
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
  "ok": "[\"symbols\", [\"tests/test_text.py\", \"Group\"]]",
  "cap": "[\"symbols\", [\"tests/test_text.py\", \"Group\"]]"
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
  "planned": "[\"symbols\", [\"tests/test_live.py\", \"Group\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 16,
   "path": "tests/test_live.py",
   "filter": "Group",
   "header": {
    "lines": 188,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 2,
  "of": 2,
  "candidates": [
   "examples/dynamic_progress.py",
   "examples/fullscreen.py",
   "examples/group.py",
   "rich/__main__.py",
   "rich/_inspect.py",
   "rich/align.py",
   "rich/live.py",
   "rich/progress.py",
   "rich/screen.py",
   "rich/spinner.py",
   "rich/traceback.py",
   "rich/tree.py",
   "tests/test_live.py",
   "tests/test_text.py"
  ],
  "table": [
   [
    "examples/dynamic_progress.py",
    "examples/dynamic_progress.py:11",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "examples/fullscreen.py",
    "examples/fullscreen.py:10",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "examples/group.py",
    "examples/group.py:2",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "rich/__main__.py",
    "rich/__main__.py:7",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "rich/_inspect.py",
    "rich/_inspect.py:5",
    "in",
    "`.console` resolves `Group` to the target"
   ],
   [
    "rich/align.py",
    "rich/align.py:300",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "rich/live.py",
    "rich/live.py:9",
    "in",
    "`.console` resolves `Group` to the target"
   ],
   [
    "rich/progress.py",
    "rich/progress.py:44",
    "in",
    "`.console` resolves `Group` to the target"
   ],
   [
    "rich/screen.py",
    "rich/screen.py:9",
    "in",
    "`.console` resolves `Group` to the target"
   ],
   [
    "rich/spinner.py",
    "rich/spinner.py:120",
    "in",
    "`.console` resolves `Group` to the target"
   ],
   [
    "rich/traceback.py",
    "rich/traceback.py:32",
    "in",
    "`.console` resolves `Group` to the target"
   ],
   [
    "rich/tree.py",
    "rich/tree.py:205",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "tests/test_live.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
   ],
   [
    "tests/test_text.py",
    null,
    "pending",
    "not yet examined"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  },
  "n_in": 12,
  "n_out": 0,
  "n_pending": 1
 }
}
```
</details>

## Step 17

The test module `tests/test_live.py` matched the search but has no module-level import of `Group`.

Tally: 12 import statements confirmed, 0 ruled out, 1 pending. The search itself is complete; what is left is checking the candidates.

Let me look at `tests/test_text.py`'s top-level names for `Group`; its outline names every import of the symbol exactly, aliases included. Almost certainly the outline shows what I need. If the outline is too long to fit, I follow whatever it opens up.

**Call:** `symbols('tests/test_text.py', 'Group')`

**Response**: outcome `ok`

```
module tests/test_text.py lines=1130 dynamic=no all=none
7 from Group <- rich.console Group
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "tests/test_text.py",
    "Group"
   ],
   "desc": "look at `tests/test_text.py`'s imports of `Group`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/test_text.py', 'Group')",
   "key": "[\"symbols\", [\"tests/test_text.py\", \"Group\"]]",
   "v1": [
    1628967,
    895850
   ],
   "v2": [
    1628967,
    895850
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
     "tests/test_text.py",
     "Group"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_text.py', 'Group')",
  "key": "[\"symbols\", [\"tests/test_text.py\", \"Group\"]]",
  "provenance": "`tests/test_text.py` had a matching line (step 4); its outline names every `Group` import exactly",
  "v2": [
   1628967,
   895850
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
  "planned": "[\"symbols\", [\"tests/test_text.py\", \"Group\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 17,
   "path": "tests/test_text.py",
   "filter": "Group",
   "header": {
    "lines": 1130,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_text.py",
     "name": "Group",
     "line": 7,
     "kind": "from",
     "src": "rich.console",
     "src_name": "Group",
     "conditional": false,
     "col": 0,
     "bases": []
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "importers",
  "step": 2,
  "of": 2,
  "candidates": [
   "examples/dynamic_progress.py",
   "examples/fullscreen.py",
   "examples/group.py",
   "rich/__main__.py",
   "rich/_inspect.py",
   "rich/align.py",
   "rich/live.py",
   "rich/progress.py",
   "rich/screen.py",
   "rich/spinner.py",
   "rich/traceback.py",
   "rich/tree.py",
   "tests/test_live.py",
   "tests/test_text.py"
  ],
  "table": [
   [
    "examples/dynamic_progress.py",
    "examples/dynamic_progress.py:11",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "examples/fullscreen.py",
    "examples/fullscreen.py:10",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "examples/group.py",
    "examples/group.py:2",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "rich/__main__.py",
    "rich/__main__.py:7",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "rich/_inspect.py",
    "rich/_inspect.py:5",
    "in",
    "`.console` resolves `Group` to the target"
   ],
   [
    "rich/align.py",
    "rich/align.py:300",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "rich/live.py",
    "rich/live.py:9",
    "in",
    "`.console` resolves `Group` to the target"
   ],
   [
    "rich/progress.py",
    "rich/progress.py:44",
    "in",
    "`.console` resolves `Group` to the target"
   ],
   [
    "rich/screen.py",
    "rich/screen.py:9",
    "in",
    "`.console` resolves `Group` to the target"
   ],
   [
    "rich/spinner.py",
    "rich/spinner.py:120",
    "in",
    "`.console` resolves `Group` to the target"
   ],
   [
    "rich/traceback.py",
    "rich/traceback.py:32",
    "in",
    "`.console` resolves `Group` to the target"
   ],
   [
    "rich/tree.py",
    "rich/tree.py:205",
    "in",
    "`rich.console` resolves `Group` to the target"
   ],
   [
    "tests/test_live.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
   ],
   [
    "tests/test_text.py",
    "tests/test_text.py:7",
    "in",
    "`rich.console` resolves `Group` to the target"
   ]
  ],
  "uncovered": {
   "IMPORT": [],
   "STAR": []
  },
  "n_in": 13,
  "n_out": 0,
  "n_pending": 0
 }
}
```
</details>

## Final

`Group` is the class at `rich/console.py:450`. 13 module-level import statements bring in this definition: `examples/dynamic_progress.py:11`, `examples/fullscreen.py:10`, `examples/group.py:2`, `rich/__main__.py:7`, `rich/_inspect.py:5`, `rich/align.py:300`, `rich/live.py:9`, `rich/progress.py:44`, `rich/screen.py:9`, `rich/spinner.py:120` and 3 more. Looking back, 1 of 17 calls did not end up mattering (step 2).

**Answer:** `{"final_kind": "importers", "final": ["examples/dynamic_progress.py:11", "examples/fullscreen.py:10", "examples/group.py:2", "rich/__main__.py:7", "rich/_inspect.py:5", "rich/align.py:300", "rich/live.py:9", "rich/progress.py:44", "rich/screen.py:9", "rich/spinner.py:120", "rich/traceback.py:32", "rich/tree.py:205", "tests/test_text.py:7"], "steps": [{"op": "resolve", "output": {"kind": "def", "path": "rich/console.py", "line": 450, "name": "Group", "detail": "class"}}, {"op": "importers", "output": ["examples/dynamic_progress.py:11", "examples/fullscreen.py:10", "examples/group.py:2", "rich/__main__.py:7", "rich/_inspect.py:5", "rich/align.py:300", "rich/live.py:9", "rich/progress.py:44", "rich/screen.py:9", "rich/spinner.py:120", "rich/traceback.py:32", "rich/tree.py:205", "tests/test_text.py:7"]}], "stuck": null}`  
**Stopped:** certificate after 17 calls