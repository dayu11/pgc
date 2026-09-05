# rich-subclasses-5ddce5e1

**Repository:** rich  
**Chain:** resolve → subclasses  
**Seed:** 0, prior bf534cee5cd76c8c, floor 7

## Task

In `examples/rainbow.py` line 10, `Highlighter` is imported from `rich.highlighter`. Which definition does the module-level name `Highlighter` actually refer to? Give `path:line`. Then list every class that derives from it directly, as `path:line:ClassName`, making sure each base name really resolves to this definition.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N; bindings take effect in source order. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. A class derives from a definition when a base written as a bare name or `module.Name` resolves to it. A call site is `name(...)` where the bare name refers to the module-level binding (not a parameter or local). Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

I need to find what `Highlighter` really is in `examples/rainbow.py`: line 10 imports it from `rich.highlighter`, so the definition is at least one hop away. Then I need every class that derives from it, checking that each base name really points at this definition.

Next I will check `examples/rainbow.py` for any other binding of `Highlighter` besides the import on line 10; almost certainly the import is the only one, and then `rich.highlighter` is the place to follow.

**Call:** `symbols('examples/rainbow.py', 'Highlighter')`

**Response**: outcome `reexport`

```
module examples/rainbow.py lines=21 dynamic=no all=none
10 from Highlighter <- rich.highlighter Highlighter
13 class RainbowHighlighter (Highlighter)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "examples/rainbow.py",
    "Highlighter"
   ],
   "desc": "check the top-level names of `examples/rainbow.py` for `Highlighter`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('examples/rainbow.py', 'Highlighter')",
   "key": "[\"symbols\", [\"examples/rainbow.py\", \"Highlighter\"]]",
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
     "examples/rainbow.py",
     "Highlighter"
    ]
   ]
  },
  {
   "call": "symbols('examples/rainbow.py')",
   "key": "[\"symbols\", [\"examples/rainbow.py\"]]",
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
     "examples/rainbow.py",
     "Highlighter"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('examples/rainbow.py', 'Highlighter')",
  "key": "[\"symbols\", [\"examples/rainbow.py\", \"Highlighter\"]]",
  "provenance": "module `examples/rainbow.py` (task), name `Highlighter` (task)",
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
   "path": "examples/rainbow.py",
   "filter": "Highlighter",
   "header": {
    "lines": 21,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "examples/rainbow.py",
     "name": "Highlighter",
     "line": 10,
     "kind": "from",
     "src": "rich.highlighter",
     "src_name": "Highlighter",
     "conditional": false,
     "col": 0,
     "bases": []
    },
    {
     "module": "examples/rainbow.py",
     "name": "RainbowHighlighter",
     "line": 13,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "Highlighter"
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
    "examples/rainbow.py",
    "Highlighter",
    "reexport",
    [
     "rich.highlighter",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 2

`examples/rainbow.py` does not define `Highlighter` itself; line 10 imports it from `rich.highlighter`.

So far: `examples/rainbow.py` takes `Highlighter` from `rich.highlighter`, which I still have to locate.

Let me list `./` to see what lives there; the listing settles whether the import is a module, a package, or not here at all. Very likely the listing fits. If the listing is too long, I will outline `rich/highlighter.py` directly, which both checks that the file exists and shows me `Highlighter`. I could outline `rich/highlighter.py` directly, which both checks that the file exists and shows me `Highlighter` instead, but it costs more calls in expectation.

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
    "examples/rainbow.py",
    "rich.highlighter"
   ],
   "desc": "find where `rich.highlighter` (imported by `examples/rainbow.py`) lives"
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
     "examples/rainbow.py",
     "rich.highlighter"
    ]
   ]
  },
  {
   "call": "symbols('rich/highlighter.py', 'Highlighter')",
   "key": "[\"symbols\", [\"rich/highlighter.py\", \"Highlighter\"]]",
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
     "examples/rainbow.py",
     "rich.highlighter"
    ]
   ]
  },
  {
   "call": "symbols('rich/highlighter/__init__.py', 'Highlighter')",
   "key": "[\"symbols\", [\"rich/highlighter/__init__.py\", \"Highlighter\"]]",
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
     "examples/rainbow.py",
     "rich.highlighter"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+Highlighter\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+Highlighter\\\\b\", \".\"]]",
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
     "examples/rainbow.py",
     "rich.highlighter"
    ]
   ]
  }
 ],
 "choice": {
  "call": "ls('.')",
  "key": "[\"ls\", [\".\"]]",
  "provenance": "`rich.highlighter` imported by `examples/rainbow.py` should live under `.`",
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
  "cap": "[\"symbols\", [\"rich/highlighter.py\", \"Highlighter\"]]"
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
    "examples/rainbow.py",
    "Highlighter",
    "reexport",
    [
     "rich.highlighter",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 3

`./` has 40 entries, and the listing is capped so I can't trust absences: `rich/` is there, so `rich.highlighter` is a package.

So far: `examples/rainbow.py` takes `Highlighter` from `rich.highlighter`, which I still have to locate.

I'll outline `rich/highlighter.py` directly, which both checks that the file exists and shows me `Highlighter`; if `rich.highlighter` is a plain module that is where it has to be. Very likely it is defined right there. If the file does not exist, I will list `rich/` to see what lives there; if the name is not bound there, that finishes it. I could list `rich/` to see what lives there instead, but it tends to open more follow-up work.

**Call:** `symbols('rich/highlighter.py', 'Highlighter')`

**Response**: outcome `def`

```
module rich/highlighter.py lines=233 dynamic=no all=none
17 class Highlighter (ABC)
50 class NullHighlighter (Highlighter)
61 class RegexHighlighter (Highlighter)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "examples/rainbow.py",
    "rich.highlighter"
   ],
   "desc": "find where `rich.highlighter` (imported by `examples/rainbow.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "symbols('rich/highlighter.py', 'Highlighter')",
   "key": "[\"symbols\", [\"rich/highlighter.py\", \"Highlighter\"]]",
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
     "examples/rainbow.py",
     "rich.highlighter"
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
     "examples/rainbow.py",
     "rich.highlighter"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+Highlighter\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+Highlighter\\\\b\", \".\"]]",
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
     "examples/rainbow.py",
     "rich.highlighter"
    ]
   ]
  },
  {
   "call": "symbols('rich/highlighter/__init__.py', 'Highlighter')",
   "key": "[\"symbols\", [\"rich/highlighter/__init__.py\", \"Highlighter\"]]",
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
     "examples/rainbow.py",
     "rich.highlighter"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('rich/highlighter.py', 'Highlighter')",
  "key": "[\"symbols\", [\"rich/highlighter.py\", \"Highlighter\"]]",
  "provenance": "`rich.highlighter` would be `rich/highlighter.py` if that file exists; one call both checks and closes it",
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
  "planned": "[\"symbols\", [\"rich/highlighter.py\", \"Highlighter\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 3,
   "path": "rich/highlighter.py",
   "filter": "Highlighter",
   "header": {
    "lines": 233,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "rich/highlighter.py",
     "name": "Highlighter",
     "line": 17,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "ABC"
     ]
    },
    {
     "module": "rich/highlighter.py",
     "name": "NullHighlighter",
     "line": 50,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "Highlighter"
     ]
    },
    {
     "module": "rich/highlighter.py",
     "name": "RegexHighlighter",
     "line": 61,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "Highlighter"
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
    "examples/rainbow.py",
    "Highlighter",
    "reexport",
    [
     "rich.highlighter",
     "rich/highlighter.py"
    ]
   ],
   [
    "rich/highlighter.py",
    "Highlighter",
    "class",
    17
   ]
  ]
 }
}
```
</details>

## Step 4

There it is: `Highlighter` is a class at `rich/highlighter.py:17`. That settles the definition; now its subclasses.

I'll search the whole tree for classes deriving from `Highlighter`; the search has to be complete before I can call the set final. Very likely nothing turns up. If it fits under the cap or it caps, I follow whatever it opens up.

**Call:** `grep('^\\s*class\\s+\\w+\\s*\\(.*\\bHighlighter\\b', '.')`

**Response**: outcome `mid`

```
docs/source/highlighting.rst:53:    class RainbowHighlighter(Highlighter):
examples/rainbow.py:13:class RainbowHighlighter(Highlighter):
rich/highlighter.py:50:class NullHighlighter(Highlighter):
rich/highlighter.py:61:class RegexHighlighter(Highlighter):
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "cover",
   "key": [
    "cover",
    "SUBCLASS",
    "."
   ],
   "desc": "search `.` for classes deriving from `Highlighter`"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*class\\\\s+\\\\w+\\\\s*\\\\(.*\\\\bHighlighter\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*class\\\\s+\\\\w+\\\\s*\\\\(.*\\\\bHighlighter\\\\b\", \".\"]]",
   "v1": [
    2162669650,
    1477561239
   ],
   "v2": [
    2162669650,
    1477561239
   ],
   "p_cap": [
    2,
    33
   ],
   "forecast": {
    "zero": [
     28,
     33
    ],
    "mid": [
     1,
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
     "SUBCLASS",
     "."
    ]
   ]
  }
 ],
 "choice": {
  "call": "grep('^\\\\s*class\\\\s+\\\\w+\\\\s*\\\\(.*\\\\bHighlighter\\\\b', '.')",
  "key": "[\"grep\", [\"^\\\\s*class\\\\s+\\\\w+\\\\s*\\\\(.*\\\\bHighlighter\\\\b\", \".\"]]",
  "provenance": "subclass lines naming `Highlighter` under `.` (derived)",
  "v2": [
   2162669650,
   1477561239
  ]
 },
 "forecast": {
  "zero": [
   28,
   33
  ],
  "mid": [
   1,
   11
  ],
  "cap": [
   2,
   33
  ]
 },
 "plan": {
  "zero": "done",
  "mid": "continue",
  "cap": "continue"
 },
 "hedges": [
  {
   "outcome": "zero",
   "word": "very likely",
   "p": [
    28,
    33
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
   "pattern": "^\\s*class\\s+\\w+\\s*\\(.*\\bHighlighter\\b",
   "scope": ".",
   "hits": [
    [
     "docs/source/highlighting.rst",
     53
    ],
    [
     "examples/rainbow.py",
     13
    ],
    [
     "rich/highlighter.py",
     50
    ],
    [
     "rich/highlighter.py",
     61
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "phase": "subclasses",
  "step": 2,
  "of": 2,
  "candidates": [
   "examples/rainbow.py",
   "rich/highlighter.py"
  ],
  "table": [
   [
    "examples/rainbow.py",
    "examples/rainbow.py:13:RainbowHighlighter",
    "in",
    "base `Highlighter` resolves to the target"
   ],
   [
    "rich/highlighter.py",
    "rich/highlighter.py:50:NullHighlighter",
    "in",
    "base `Highlighter` resolves to the target"
   ],
   [
    "rich/highlighter.py",
    "rich/highlighter.py:61:RegexHighlighter",
    "in",
    "base `Highlighter` resolves to the target"
   ]
  ],
  "uncovered": {
   "SUBCLASS": []
  },
  "n_in": 3,
  "n_out": 0,
  "n_pending": 0
 }
}
```
</details>

## Final

`Highlighter` is the class at `rich/highlighter.py:17`. 3 classes derive from it directly: `RainbowHighlighter` (`examples/rainbow.py:13`), `NullHighlighter` (`rich/highlighter.py:50`), `RegexHighlighter` (`rich/highlighter.py:61`). Looking back, 1 of 4 calls did not end up mattering (step 2).

**Answer:** `{"final_kind": "subclasses", "final": ["examples/rainbow.py:13:RainbowHighlighter", "rich/highlighter.py:50:NullHighlighter", "rich/highlighter.py:61:RegexHighlighter"], "steps": [{"op": "resolve", "output": {"kind": "def", "path": "rich/highlighter.py", "line": 17, "name": "Highlighter", "detail": "class"}}, {"op": "subclasses", "output": ["examples/rainbow.py:13:RainbowHighlighter", "rich/highlighter.py:50:NullHighlighter", "rich/highlighter.py:61:RegexHighlighter"]}], "stuck": null}`  
**Stopped:** certificate after 4 calls