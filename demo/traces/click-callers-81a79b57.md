# click-callers-81a79b57

**Repository:** click  
**Chain:** resolve → callers  
**Seed:** 0, prior 81b2b7394c71c459, floor 18

## Task

In `tests/test_compat.py` line 11, `term_len` is imported from `click._compat`. Which definition does the module-level name `term_len` actually refer to? Give `path:line`. Then list every call site of it: bare-name calls whose module-level binding resolves to this definition, as `path:line`.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N; bindings take effect in source order. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. A class derives from a definition when a base written as a bare name or `module.Name` resolves to it. A call site is `name(...)` where the bare name refers to the module-level binding (not a parameter or local). Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

I need to find what `term_len` really is in `tests/test_compat.py`: line 11 imports it from `click._compat`, so the definition is at least one hop away. Then every real call site of it, which means checking what the name refers to in each file that mentions it.

Next I will check `tests/test_compat.py` for any other binding of `term_len` besides the import on line 11; almost certainly the import is the only one, and then `click._compat` is the place to follow.

**Call:** `symbols('tests/test_compat.py', 'term_len')`

**Response**: outcome `reexport`

```
module tests/test_compat.py lines=271 dynamic=no all=none
11 from term_len <- click._compat term_len
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "tests/test_compat.py",
    "term_len"
   ],
   "desc": "check the top-level names of `tests/test_compat.py` for `term_len`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('tests/test_compat.py', 'term_len')",
   "key": "[\"symbols\", [\"tests/test_compat.py\", \"term_len\"]]",
   "v1": [
    65626933,
    22453600
   ],
   "v2": [
    65626933,
    22453600
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
     "tests/test_compat.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "symbols('tests/test_compat.py')",
   "key": "[\"symbols\", [\"tests/test_compat.py\"]]",
   "v1": [
    13924023879,
    4558080800
   ],
   "v2": [
    13924023879,
    4558080800
   ],
   "p_cap": [
    134,
    1015
   ],
   "forecast": {
    "def": [
     881,
     101500
    ],
    "reexport": [
     81933,
     101500
    ],
    "star": [
     881,
     101500
    ],
    "none": [
     881,
     20300
    ],
    "cap": [
     134,
     1015
    ]
   },
   "serves": [
    [
     "bindings",
     "tests/test_compat.py",
     "term_len"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('tests/test_compat.py', 'term_len')",
  "key": "[\"symbols\", [\"tests/test_compat.py\", \"term_len\"]]",
  "provenance": "module `tests/test_compat.py` (task), name `term_len` (task)",
  "v2": [
   65626933,
   22453600
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
   "path": "tests/test_compat.py",
   "filter": "term_len",
   "header": {
    "lines": 271,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "tests/test_compat.py",
     "name": "term_len",
     "line": 11,
     "kind": "from",
     "src": "click._compat",
     "src_name": "term_len",
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
    "tests/test_compat.py",
    "term_len",
    "reexport",
    [
     "click._compat",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 2

The test module `tests/test_compat.py` does not define `term_len` itself; line 11 imports it from `click._compat`.

So far: `tests/test_compat.py` takes `term_len` from `click._compat`, which I still have to locate.

Let me list `./` to see what lives there; the listing settles whether the import is a module, a package, or not here at all. Very likely the listing fits. If the listing is too long, I will outline `click/_compat.py` directly, which both checks that the file exists and shows me `term_len`. I could outline `click/_compat.py` directly, which both checks that the file exists and shows me `term_len` instead, but it costs more calls in expectation.

**Call:** `ls('.')`

**Response**: outcome `complete`

```
.devcontainer/
.github/
.pre-commit-config.yaml
.readthedocs.yaml
CHANGES.md
LICENSE.txt
README.md
docs/
examples/
pyproject.toml
src/
tests/
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_compat.py",
    "click._compat"
   ],
   "desc": "find where `click._compat` (imported by `tests/test_compat.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    2491,
    1326
   ],
   "v2": [
    59881702565,
    31056023232
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
     "tests/test_compat.py",
     "click._compat"
    ]
   ]
  },
  {
   "call": "symbols('click/_compat.py', 'term_len')",
   "key": "[\"symbols\", [\"click/_compat.py\", \"term_len\"]]",
   "v1": [
    15655364805,
    6901338496
   ],
   "v2": [
    44855693759,
    20704015488
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     95637,
     261256
    ],
    "reexport": [
     4041,
     522512
    ],
    "star": [
     449,
     522512
    ],
    "none": [
     449,
     32657
    ],
    "missing": [
     707,
     1156
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_compat.py",
     "click._compat"
    ]
   ]
  },
  {
   "call": "symbols('click/_compat/__init__.py', 'term_len')",
   "key": "[\"symbols\", [\"click/_compat/__init__.py\", \"term_len\"]]",
   "v1": [
    86086477,
    28613312
   ],
   "v2": [
    244806719,
    85839936
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     23,
     2312
    ],
    "reexport": [
     115,
     3468
    ],
    "star": [
     23,
     27744
    ],
    "none": [
     437,
     27744
    ],
    "missing": [
     1087,
     1156
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_compat.py",
     "click._compat"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+term_len\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+term_len\\\\b\", \".\"]]",
   "v1": [
    673,
    221
   ],
   "v2": [
    3817,
    1326
   ],
   "p_cap": [
    1,
    39
   ],
   "forecast": {
    "zero": [
     1,
     39
    ],
    "mid": [
     37,
     39
    ],
    "cap": [
     1,
     39
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_compat.py",
     "click._compat"
    ]
   ]
  }
 ],
 "choice": {
  "call": "ls('.')",
  "key": "[\"ls\", [\".\"]]",
  "provenance": "`click._compat` imported by `tests/test_compat.py` should live under `.`",
  "v2": [
   59881702565,
   31056023232
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
  "cap": "[\"symbols\", [\"click/_compat.py\", \"term_len\"]]"
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
    ".devcontainer/",
    ".github/",
    ".pre-commit-config.yaml",
    ".readthedocs.yaml",
    "CHANGES.md",
    "LICENSE.txt",
    "README.md",
    "docs/",
    "examples/",
    "pyproject.toml",
    "src/",
    "tests/"
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
    "tests/test_compat.py",
    "term_len",
    "reexport",
    [
     "click._compat",
     null
    ]
   ]
  ]
 }
}
```
</details>

## Step 3

`./` has 12 entries: there is no `click` here.

So far: `tests/test_compat.py` takes `term_len` from `click._compat`, which I still have to locate.

I'll search the whole tree for `class term_len`/`def term_len`; that shows where the definition lives and whether the name is reused. Almost certainly it fits under the cap. If it caps or nothing turns up, I will list `src/` to see what lives there. I could list `src/` to see what lives there instead, but it costs more calls in expectation.

**Call:** `grep('^\\s*(?:async\\s+)?(?:def|class)\\s+term_len\\b', '.')`

**Response**: outcome `mid`

```
src/click/_compat.py:536:def term_len(x: str) -> int:
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "tests/test_compat.py",
    "click._compat"
   ],
   "desc": "find where `click._compat` (imported by `tests/test_compat.py`) lives"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+term_len\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+term_len\\\\b\", \".\"]]",
   "v1": [
    1390,
    663
   ],
   "v2": [
    5680,
    2703
   ],
   "p_cap": [
    1,
    39
   ],
   "forecast": {
    "zero": [
     1,
     39
    ],
    "mid": [
     37,
     39
    ],
    "cap": [
     1,
     39
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_compat.py",
     "click._compat"
    ]
   ]
  },
  {
   "call": "ls('src')",
   "key": "[\"ls\", [\"src\"]]",
   "v1": [
    25061,
    11713
   ],
   "v2": [
    75353,
    35139
   ],
   "p_cap": [
    5,
    53
   ],
   "forecast": {
    "complete": [
     48,
     53
    ],
    "cap": [
     5,
     53
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_compat.py",
     "click._compat"
    ]
   ]
  },
  {
   "call": "symbols('src/click/_compat.py', 'term_len')",
   "key": "[\"symbols\", [\"src/click/_compat.py\", \"term_len\"]]",
   "v1": [
    15655364805,
    6901338496
   ],
   "v2": [
    47615448463,
    20704015488
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     95637,
     261256
    ],
    "reexport": [
     4041,
     522512
    ],
    "star": [
     449,
     522512
    ],
    "none": [
     449,
     32657
    ],
    "missing": [
     707,
     1156
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_compat.py",
     "click._compat"
    ]
   ]
  },
  {
   "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+term_len\\\\b', 'src')",
   "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+term_len\\\\b\", \"src\"]]",
   "v1": [
    72061,
    24752
   ],
   "v2": [
    219481,
    74256
   ],
   "p_cap": [
    1,
    224
   ],
   "forecast": {
    "zero": [
     193,
     224
    ],
    "mid": [
     15,
     112
    ],
    "cap": [
     1,
     224
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_compat.py",
     "click._compat"
    ]
   ]
  },
  {
   "call": "symbols('src/click/_compat/__init__.py', 'term_len')",
   "key": "[\"symbols\", [\"src/click/_compat/__init__.py\", \"term_len\"]]",
   "v1": [
    86086477,
    28613312
   ],
   "v2": [
    262398727,
    85839936
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     23,
     2312
    ],
    "reexport": [
     115,
     3468
    ],
    "star": [
     23,
     27744
    ],
    "none": [
     437,
     27744
    ],
    "missing": [
     1087,
     1156
    ]
   },
   "serves": [
    [
     "module_path",
     "tests/test_compat.py",
     "click._compat"
    ]
   ]
  }
 ],
 "choice": {
  "call": "grep('^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+term_len\\\\b', '.')",
  "key": "[\"grep\", [\"^\\\\s*(?:async\\\\s+)?(?:def|class)\\\\s+term_len\\\\b\", \".\"]]",
  "provenance": "a `def`/`class term_len` statement would reveal the module file; `term_len` task",
  "v2": [
   5680,
   2703
  ]
 },
 "forecast": {
  "zero": [
   1,
   39
  ],
  "mid": [
   37,
   39
  ],
  "cap": [
   1,
   39
  ]
 },
 "plan": {
  "zero": "[\"ls\", [\"src\"]]",
  "mid": "continue",
  "cap": "[\"ls\", [\"src\"]]"
 },
 "hedges": [
  {
   "outcome": "mid",
   "word": "almost certainly",
   "p": [
    37,
    39
   ]
  }
 ],
 "adherence": {
  "planned": "continue",
  "status": "open-ended"
 },
 "facts": [
  {
   "kind": "grep",
   "step": 3,
   "pattern": "^\\s*(?:async\\s+)?(?:def|class)\\s+term_len\\b",
   "scope": ".",
   "hits": [
    [
     "src/click/_compat.py",
     536
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "phase": "resolve",
  "step": 1,
  "of": 2,
  "chain": [
   [
    "tests/test_compat.py",
    "term_len",
    "reexport",
    [
     "click._compat",
     "src/click/_compat.py"
    ]
   ],
   [
    "src/click/_compat.py",
    "term_len",
    "open",
    null
   ]
  ]
 }
}
```
</details>

## Step 4

There is exactly one `term_len` definition in the tree, in `src/click/_compat.py`.

So far: `tests/test_compat.py` takes `term_len` from `click._compat`; `src/click/_compat.py` is next.

I'll look at `src/click/_compat.py`'s top-level names for `term_len`; that settles what the name means there. Almost certainly it is defined right there. If the name is not bound there, that finishes it; if it is re-exported from somewhere else, I follow whatever it opens up. I could outline all of `src/click/_compat.py` instead, but it is more likely to hit the cap.

**Call:** `symbols('src/click/_compat.py', 'term_len')`

**Response**: outcome `def`

```
module src/click/_compat.py lines=591 dynamic=no all=none
536 def term_len
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/click/_compat.py",
    "term_len"
   ],
   "desc": "check the top-level names of `src/click/_compat.py` for `term_len`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/click/_compat.py', 'term_len')",
   "key": "[\"symbols\", [\"src/click/_compat.py\", \"term_len\"]]",
   "v1": [
    23836821,
    22453600
   ],
   "v2": [
    23836821,
    22453600
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
     "src/click/_compat.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "symbols('src/click/_compat.py')",
   "key": "[\"symbols\", [\"src/click/_compat.py\"]]",
   "v1": [
    5440631143,
    4558080800
   ],
   "v2": [
    5440631143,
    4558080800
   ],
   "p_cap": [
    134,
    1015
   ],
   "forecast": {
    "def": [
     41407,
     50750
    ],
    "reexport": [
     881,
     50750
    ],
    "star": [
     881,
     101500
    ],
    "none": [
     2643,
     101500
    ],
    "cap": [
     134,
     1015
    ]
   },
   "serves": [
    [
     "bindings",
     "src/click/_compat.py",
     "term_len"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/click/_compat.py', 'term_len')",
  "key": "[\"symbols\", [\"src/click/_compat.py\", \"term_len\"]]",
  "provenance": "module `src/click/_compat.py` (step 3), name `term_len` (task)",
  "v2": [
   23836821,
   22453600
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
 "hedges": [
  {
   "outcome": "def",
   "word": "almost certainly",
   "p": [
    47,
    50
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
   "step": 4,
   "path": "src/click/_compat.py",
   "filter": "term_len",
   "header": {
    "lines": 591,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/click/_compat.py",
     "name": "term_len",
     "line": 536,
     "kind": "def",
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
    "tests/test_compat.py",
    "term_len",
    "reexport",
    [
     "click._compat",
     "src/click/_compat.py"
    ]
   ],
   [
    "src/click/_compat.py",
    "term_len",
    "def",
    536
   ]
  ]
 }
}
```
</details>

## Step 5

There it is: `term_len` is a function at `src/click/_compat.py:536`. That settles the definition; now its call sites.

Let me search the whole tree for calls of `term_len`; the search has to be complete before I can call the set final. Probably it fits under the cap. If nothing turns up, that finishes it; if it caps, I follow whatever it opens up.

**Call:** `grep('\\bterm_len\\s*\\(', '.')`

**Response** (capped): outcome `cap`

```
src/click/_compat.py:536:def term_len(x: str) -> int:
src/click/_termui_impl.py:268:            clutter_length = term_len(self.format_progress_line())
src/click/_termui_impl.py:282:        line_len = term_len(line)
src/click/_textwrap.py:89:            if term_len(indent) + term_len(self.placeholder.lstrip()) > self.width:
src/click/_textwrap.py:103:            width = self.width - term_len(indent)
src/click/_textwrap.py:109:                n = term_len(chunks[-1])
src/click/_textwrap.py:118:            if chunks and term_len(chunks[-1]) > width:
src/click/_textwrap.py:123:                cur_len -= term_len(cur_line[-1])
src/click/_textwrap.py:143:                            and cur_len + term_len(self.placeholder) <= width
src/click/_textwrap.py:148:                        cur_len -= term_len(cur_line[-1])
src/click/_textwrap.py:154:                                term_len(prev_line) + term_len(self.placeholder)
src/click/formatting.py:19:            widths[idx] = max(widths.get(idx, 0), term_len(col))
src/click/formatting.py:93:                orig_len = term_len(line)
src/click/formatting.py:95:                indent = orig_len - term_len(line)
src/click/formatting.py:180:        if text_width >= (term_len(usage_prefix) + 20):
src/click/formatting.py:182:            indent = " " * term_len(usage_prefix)
src/click/formatting.py:195:            indent = " " * (max(self.current_indent, term_len(prefix)) + 4)
src/click/formatting.py:255:            if term_len(first) <= first_col - col_spacing:
src/click/formatting.py:256:                self.write(" " * (first_col - term_len(first)))
tests/test_compat.py:129:    assert term_len(f"a{seq}b") == 2
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
   "desc": "search `.` for calls of `term_len`"
  }
 ],
 "candidates": [
  {
   "call": "grep('\\\\bterm_len\\\\s*\\\\(', '.')",
   "key": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \".\"]]",
   "v1": [
    684674738,
    489416655
   ],
   "v2": [
    684674738,
    489416655
   ],
   "p_cap": [
    1,
    21
   ],
   "forecast": {
    "zero": [
     3,
     14
    ],
    "mid": [
     31,
     42
    ],
    "cap": [
     1,
     21
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
  "call": "grep('\\\\bterm_len\\\\s*\\\\(', '.')",
  "key": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \".\"]]",
  "provenance": "call lines naming `term_len` under `.` (derived)",
  "v2": [
   684674738,
   489416655
  ]
 },
 "forecast": {
  "zero": [
   3,
   14
  ],
  "mid": [
   31,
   42
  ],
  "cap": [
   1,
   21
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
    31,
    42
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
   "step": 5,
   "pattern": "\\bterm_len\\s*\\(",
   "scope": ".",
   "hits": [
    [
     "src/click/_compat.py",
     536
    ],
    [
     "src/click/_termui_impl.py",
     268
    ],
    [
     "src/click/_termui_impl.py",
     282
    ],
    [
     "src/click/_textwrap.py",
     89
    ],
    [
     "src/click/_textwrap.py",
     103
    ],
    [
     "src/click/_textwrap.py",
     109
    ],
    [
     "src/click/_textwrap.py",
     118
    ],
    [
     "src/click/_textwrap.py",
     123
    ],
    [
     "src/click/_textwrap.py",
     143
    ],
    [
     "src/click/_textwrap.py",
     148
    ],
    [
     "src/click/_textwrap.py",
     154
    ],
    [
     "src/click/formatting.py",
     19
    ],
    [
     "src/click/formatting.py",
     93
    ],
    [
     "src/click/formatting.py",
     95
    ],
    [
     "src/click/formatting.py",
     180
    ],
    [
     "src/click/formatting.py",
     182
    ],
    [
     "src/click/formatting.py",
     195
    ],
    [
     "src/click/formatting.py",
     255
    ],
    [
     "src/click/formatting.py",
     256
    ],
    [
     "tests/test_compat.py",
     129
    ]
   ],
   "capped": true
  }
 ],
 "goal_state": {
  "phase": "callers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/click/_compat.py",
   "src/click/_termui_impl.py",
   "src/click/_textwrap.py",
   "src/click/formatting.py",
   "tests/test_compat.py"
  ],
  "table": [
   [
    "src/click/_compat.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/click/_termui_impl.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/click/_textwrap.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/click/formatting.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_compat.py",
    null,
    "pending",
    "not yet examined"
   ]
  ],
  "uncovered": {
   "CALL": [
    [
     "grep",
     ".devcontainer"
    ],
    [
     "grep",
     ".github"
    ],
    [
     "grep",
     "docs"
    ],
    [
     "grep",
     "examples"
    ],
    [
     "grep",
     "src"
    ],
    [
     "grep",
     "tests"
    ]
   ]
  },
  "n_in": 0,
  "n_out": 0,
  "n_pending": 5
 }
}
```
</details>

## Step 6

The search for calls of `term_len` anywhere hit the cap at 20 lines, so it only shows part of the picture.

Tally: 0 call sites confirmed, 0 ruled out, 5 pending. The search still has 6 scopes to cover.

Next I will search `.devcontainer` for calls of `term_len`; the search has to be complete before I can call the set final.

**Call:** `grep('\\bterm_len\\s*\\(', '.devcontainer')`

**Response**: outcome `zero`

```

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
    ".devcontainer"
   ],
   "desc": "search `.devcontainer` for calls of `term_len`"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "CALL",
    ".github"
   ],
   "desc": "search `.github` for calls of `term_len`"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "CALL",
    "docs"
   ],
   "desc": "search `docs` for calls of `term_len`"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "CALL",
    "examples"
   ],
   "desc": "search `examples` for calls of `term_len`"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "CALL",
    "src"
   ],
   "desc": "search `src` for calls of `term_len`"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "CALL",
    "tests"
   ],
   "desc": "search `tests` for calls of `term_len`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/click/_compat.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `src/click/_compat.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/_termui_impl.py",
    "term_len"
   ],
   "desc": "check what `term_len` means inside `src/click/_termui_impl.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/_textwrap.py",
    "term_len"
   ],
   "desc": "check what `term_len` means inside `src/click/_textwrap.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/formatting.py",
    "term_len"
   ],
   "desc": "check what `term_len` means inside `src/click/formatting.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "tests/test_compat.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `tests/test_compat.py`"
  }
 ],
 "candidates": [
  {
   "call": "grep('\\\\bterm_len\\\\s*\\\\(', '.devcontainer')",
   "key": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \".devcontainer\"]]",
   "v1": [
    35587899002547893,
    2635242731476992
   ],
   "v2": [
    245709636859854493,
    18446699120338944
   ],
   "p_cap": [
    1,
    13356
   ],
   "forecast": {
    "zero": [
     13325,
     13356
    ],
    "mid": [
     5,
     2226
    ],
    "cap": [
     1,
     13356
    ]
   },
   "serves": [
    [
     "cover",
     "CALL",
     ".devcontainer"
    ]
   ]
  },
  {
   "call": "grep('\\\\bterm_len\\\\s*\\\\(', '.github')",
   "key": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \".github\"]]",
   "v1": [
    35587899002547893,
    2635242731476992
   ],
   "v2": [
    245709636859854493,
    18446699120338944
   ],
   "p_cap": [
    1,
    13356
   ],
   "forecast": {
    "zero": [
     13325,
     13356
    ],
    "mid": [
     5,
     2226
    ],
    "cap": [
     1,
     13356
    ]
   },
   "serves": [
    [
     "cover",
     "CALL",
     ".github"
    ]
   ]
  },
  {
   "call": "grep('\\\\bterm_len\\\\s*\\\\(', 'docs')",
   "key": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \"docs\"]]",
   "v1": [
    827345687667614459,
    61256963116597248
   ],
   "v2": [
    43249925962578952919,
    3246619045179654144
   ],
   "p_cap": [
    5,
    22176
   ],
   "forecast": {
    "zero": [
     22021,
     22176
    ],
    "mid": [
     25,
     3696
    ],
    "cap": [
     5,
     22176
    ]
   },
   "serves": [
    [
     "cover",
     "CALL",
     "docs"
    ]
   ]
  },
  {
   "call": "grep('\\\\bterm_len\\\\s*\\\\(', 'examples')",
   "key": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \"examples\"]]",
   "v1": [
    89513519029300721,
    6612967609178112
   ],
   "v2": [
    519945449061255979,
    38943031476271104
   ],
   "p_cap": [
    5,
    1596
   ],
   "forecast": {
    "zero": [
     1441,
     1596
    ],
    "mid": [
     25,
     266
    ],
    "cap": [
     5,
     1596
    ]
   },
   "serves": [
    [
     "cover",
     "CALL",
     "examples"
    ]
   ]
  },
  {
   "call": "grep('\\\\bterm_len\\\\s*\\\\(', 'tests')",
   "key": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \"tests\"]]",
   "v1": [
    4128670123973230583,
    304892611875790848
   ],
   "v2": [
    30833737396598582413,
    2308472632773844992
   ],
   "p_cap": [
    403,
    110376
   ],
   "forecast": {
    "zero": [
     97883,
     110376
    ],
    "mid": [
     2015,
     18396
    ],
    "cap": [
     403,
     110376
    ]
   },
   "serves": [
    [
     "cover",
     "CALL",
     "tests"
    ]
   ]
  },
  {
   "call": "grep('\\\\bterm_len\\\\s*\\\\(', 'src')",
   "key": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \"src\"]]",
   "v1": [
    32991764747751115,
    2436356487591936
   ],
   "v2": [
    1724723938524943789,
    129126893842372608
   ],
   "p_cap": [
    187,
    51156
   ],
   "forecast": {
    "zero": [
     45359,
     51156
    ],
    "mid": [
     935,
     8526
    ],
    "cap": [
     187,
     51156
    ]
   },
   "serves": [
    [
     "cover",
     "CALL",
     "src"
    ]
   ]
  },
  {
   "call": "symbols('src/click/_termui_impl.py', 'term_len')",
   "key": "[\"symbols\", [\"src/click/_termui_impl.py\", \"term_len\"]]",
   "v1": [
    3058658480384891,
    223109568460800
   ],
   "v2": [
    891015096429435821,
    65881068286924800
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
     "src/click/_termui_impl.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "symbols('src/click/_textwrap.py', 'term_len')",
   "key": "[\"symbols\", [\"src/click/_textwrap.py\", \"term_len\"]]",
   "v1": [
    3058658480384891,
    223109568460800
   ],
   "v2": [
    891015096429435821,
    65881068286924800
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
     "src/click/_textwrap.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "symbols('src/click/formatting.py', 'term_len')",
   "key": "[\"symbols\", [\"src/click/formatting.py\", \"term_len\"]]",

```
</details>

## Step 7

Nothing under `.devcontainer` for calls of `term_len`, and the search was not capped, so that part of the tree is clear.

Next I will search `.github` for calls of `term_len`; the search has to be complete before I can call the set final.

**Call:** `grep('\\bterm_len\\s*\\(', '.github')`

**Response**: outcome `zero`

```

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
    ".github"
   ],
   "desc": "search `.github` for calls of `term_len`"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "CALL",
    "docs"
   ],
   "desc": "search `docs` for calls of `term_len`"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "CALL",
    "examples"
   ],
   "desc": "search `examples` for calls of `term_len`"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "CALL",
    "src"
   ],
   "desc": "search `src` for calls of `term_len`"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "CALL",
    "tests"
   ],
   "desc": "search `tests` for calls of `term_len`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/click/_compat.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `src/click/_compat.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/_termui_impl.py",
    "term_len"
   ],
   "desc": "check what `term_len` means inside `src/click/_termui_impl.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/_textwrap.py",
    "term_len"
   ],
   "desc": "check what `term_len` means inside `src/click/_textwrap.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/formatting.py",
    "term_len"
   ],
   "desc": "check what `term_len` means inside `src/click/formatting.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "tests/test_compat.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `tests/test_compat.py`"
  }
 ],
 "candidates": [
  {
   "call": "grep('\\\\bterm_len\\\\s*\\\\(', '.github')",
   "key": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \".github\"]]",
   "v1": [
    151499152701589345,
    12297799413559296
   ],
   "v2": [
    39401410704659535823,
    3246619045179654144
   ],
   "p_cap": [
    1,
    13356
   ],
   "forecast": {
    "zero": [
     13325,
     13356
    ],
    "mid": [
     5,
     2226
    ],
    "cap": [
     1,
     13356
    ]
   },
   "serves": [
    [
     "cover",
     "CALL",
     ".github"
    ]
   ]
  },
  {
   "call": "grep('\\\\bterm_len\\\\s*\\\\(', 'docs')",
   "key": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \"docs\"]]",
   "v1": [
    2114095776569111,
    171588131979264
   ],
   "v2": [
    39401410704659535823,
    3246619045179654144
   ],
   "p_cap": [
    5,
    22176
   ],
   "forecast": {
    "zero": [
     22021,
     22176
    ],
    "mid": [
     25,
     3696
    ],
    "cap": [
     5,
     22176
    ]
   },
   "serves": [
    [
     "cover",
     "CALL",
     "docs"
    ]
   ]
  },
  {
   "call": "grep('\\\\bterm_len\\\\s*\\\\(', 'examples')",
   "key": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \"examples\"]]",
   "v1": [
    23335589181721643,
    1889419316908032
   ],
   "v2": [
    8528088652415460749,
    700974566572879872
   ],
   "p_cap": [
    5,
    1596
   ],
   "forecast": {
    "zero": [
     1441,
     1596
    ],
    "mid": [
     25,
     266
    ],
    "cap": [
     5,
     1596
    ]
   },
   "serves": [
    [
     "cover",
     "CALL",
     "examples"
    ]
   ]
  },
  {
   "call": "grep('\\\\bterm_len\\\\s*\\\\(', 'tests')",
   "key": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \"tests\"]]",
   "v1": [
    3767252953525395101,
    304892611875790848
   ],
   "v2": [
    196681051742454796345,
    16159308429416914944
   ],
   "p_cap": [
    403,
    110376
   ],
   "forecast": {
    "zero": [
     97883,
     110376
    ],
    "mid": [
     2015,
     18396
    ],
    "cap": [
     403,
     110376
    ]
   },
   "serves": [
    [
     "cover",
     "CALL",
     "tests"
    ]
   ]
  },
  {
   "call": "grep('\\\\bterm_len\\\\s*\\\\(', 'src')",
   "key": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \"src\"]]",
   "v1": [
    247767308622199,
    20052316770304
   ],
   "v2": [
    3143315981533570309,
    258253787684745216
   ],
   "p_cap": [
    187,
    51156
   ],
   "forecast": {
    "zero": [
     45359,
     51156
    ],
    "mid": [
     935,
     8526
    ],
    "cap": [
     187,
     51156
    ]
   },
   "serves": [
    [
     "cover",
     "CALL",
     "src"
    ]
   ]
  },
  {
   "call": "symbols('src/click/_termui_impl.py', 'term_len')",
   "key": "[\"symbols\", [\"src/click/_termui_impl.py\", \"term_len\"]]",
   "v1": [
    217946527540350523,
    17402546339942400
   ],
   "v2": [
    3793627717246513273,
    307444985338982400
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
     "src/click/_termui_impl.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "symbols('src/click/_textwrap.py', 'term_len')",
   "key": "[\"symbols\", [\"src/click/_textwrap.py\", \"term_len\"]]",
   "v1": [
    217946527540350523,
    17402546339942400
   ],
   "v2": [
    3793627717246513273,
    307444985338982400
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
     "src/click/_textwrap.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "symbols('src/click/formatting.py', 'term_len')",
   "key": "[\"symbols\", [\"src/click/formatting.py\", \"term_len\"]]",
   "v1": [
    217946527540350523,
    17402546339942400
   ],
   "v2": [
    3793627717246513273,
    307444985338982400
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
     "src/click/formatting.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "calls('src/click/_compat.py', 'term_len')",
   "key": "[\"calls\", [\"src/click/_compat.py\", \"term_len\"]]",
   "v1": [
    43693720786109759,
    3480509267988480
   ],
   "v2": [
    760570213361336549,
    61488997067796480
   ],
   "p_cap": [
    1,
    20
   ],
   "forecast": {
    "ok": [
```
</details>

## Step 8

Nothing under `.github` for calls of `term_len`, and the search was not capped, so that part of the tree is clear.

Still open: search `docs` for calls of `term_len`; search `examples` for calls of `term_len`; search `src` for calls of `term_len`; and 6 more.

I'll search `docs` for calls of `term_len`; the search has to be complete before I can call the set final. Almost certainly nothing turns up.

**Call:** `grep('\\bterm_len\\s*\\(', 'docs')`

**Response**: outcome `zero`

```

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
    "docs"
   ],
   "desc": "search `docs` for calls of `term_len`"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "CALL",
    "examples"
   ],
   "desc": "search `examples` for calls of `term_len`"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "CALL",
    "src"
   ],
   "desc": "search `src` for calls of `term_len`"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "CALL",
    "tests"
   ],
   "desc": "search `tests` for calls of `term_len`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/click/_compat.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `src/click/_compat.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/_termui_impl.py",
    "term_len"
   ],
   "desc": "check what `term_len` means inside `src/click/_termui_impl.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/_textwrap.py",
    "term_len"
   ],
   "desc": "check what `term_len` means inside `src/click/_textwrap.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/formatting.py",
    "term_len"
   ],
   "desc": "check what `term_len` means inside `src/click/formatting.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "tests/test_compat.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `tests/test_compat.py`"
  }
 ],
 "candidates": [
  {
   "call": "grep('\\\\bterm_len\\\\s*\\\\(', 'docs')",
   "key": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \"docs\"]]",
   "v1": [
    682118696802730795,
    61256963116597248
   ],
   "v2": [
    12781992059278081169,
    1163882299215347712
   ],
   "p_cap": [
    5,
    22176
   ],
   "forecast": {
    "zero": [
     22021,
     22176
    ],
    "mid": [
     25,
     3696
    ],
    "cap": [
     5,
     22176
    ]
   },
   "serves": [
    [
     "cover",
     "CALL",
     "docs"
    ]
   ]
  },
  {
   "call": "grep('\\\\bterm_len\\\\s*\\\\(', 'examples')",
   "key": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \"examples\"]]",
   "v1": [
    157768387270835,
    14130272669184
   ],
   "v2": [
    12781992059278081169,
    1163882299215347712
   ],
   "p_cap": [
    5,
    1596
   ],
   "forecast": {
    "zero": [
     1441,
     1596
    ],
    "mid": [
     25,
     266
    ],
    "cap": [
     5,
     1596
    ]
   },
   "serves": [
    [
     "cover",
     "CALL",
     "examples"
    ]
   ]
  },
  {
   "call": "grep('\\\\bterm_len\\\\s*\\\\(', 'tests')",
   "key": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \"tests\"]]",
   "v1": [
    200343281357503507,
    17934859522105344
   ],
   "v2": [
    147400810903060713325,
    13415274922534797312
   ],
   "p_cap": [
    403,
    110376
   ],
   "forecast": {
    "zero": [
     97883,
     110376
    ],
    "mid": [
     2015,
     18396
    ],
    "cap": [
     403,
     110376
    ]
   },
   "serves": [
    [
     "cover",
     "CALL",
     "tests"
    ]
   ]
  },
  {
   "call": "grep('\\\\bterm_len\\\\s*\\\\(', 'src')",
   "key": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \"src\"]]",
   "v1": [
    13607845623721621,
    1218178243795968
   ],
   "v2": [
    523495615715367301,
    47644304646242304
   ],
   "p_cap": [
    187,
    51156
   ],
   "forecast": {
    "zero": [
     45359,
     51156
    ],
    "mid": [
     935,
     8526
    ],
    "cap": [
     187,
     51156
    ]
   },
   "serves": [
    [
     "cover",
     "CALL",
     "src"
    ]
   ]
  },
  {
   "call": "symbols('src/click/_termui_impl.py', 'term_len')",
   "key": "[\"symbols\", [\"src/click/_termui_impl.py\", \"term_len\"]]",
   "v1": [
    49329423402669887,
    4350636584985600
   ],
   "v2": [
    17083595901626568499,
    1531424077914931200
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
     "src/click/_termui_impl.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "symbols('src/click/_textwrap.py', 'term_len')",
   "key": "[\"symbols\", [\"src/click/_textwrap.py\", \"term_len\"]]",
   "v1": [
    49329423402669887,
    4350636584985600
   ],
   "v2": [
    17083595901626568499,
    1531424077914931200
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
     "src/click/_textwrap.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "symbols('src/click/formatting.py', 'term_len')",
   "key": "[\"symbols\", [\"src/click/formatting.py\", \"term_len\"]]",
   "v1": [
    49329423402669887,
    4350636584985600
   ],
   "v2": [
    17083595901626568499,
    1531424077914931200
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
     "src/click/formatting.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "calls('src/click/_compat.py', 'term_len')",
   "key": "[\"calls\", [\"src/click/_compat.py\", \"term_len\"]]",
   "v1": [
    9891988500043891,
    870127316997120
   ],
   "v2": [
    3425907724792803287,
    306284815582986240
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
     "src/click/_compat.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "calls('tests/test_compat.py', 'term_len')",
   "key": "[\"calls\", [\"tests/test_compat.py\", \"term_len\"]]",
   "v1": [
    9891988500043891,
    870127316997120
   ],
   "v2": [
    3425907724792803287,
    306284815582986240
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
     "tests/test_compat.py",
     "term_len"
    ]
   ]
  }
 ],
 "choice": {
  "ca
```
</details>

## Step 9

Nothing under `docs` for calls of `term_len`, and the search was not capped, so that part of the tree is clear.

Tally: 0 call sites confirmed, 0 ruled out, 5 pending. The search still has 3 scopes to cover.

Let me search `examples` for calls of `term_len`; the search has to be complete before I can call the set final. Almost certainly nothing turns up. If it fits under the cap, I will search `tests` for calls of `term_len`.

**Call:** `grep('\\bterm_len\\s*\\(', 'examples')`

**Response**: outcome `zero`

```

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
    "examples"
   ],
   "desc": "search `examples` for calls of `term_len`"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "CALL",
    "src"
   ],
   "desc": "search `src` for calls of `term_len`"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "CALL",
    "tests"
   ],
   "desc": "search `tests` for calls of `term_len`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/click/_compat.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `src/click/_compat.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/_termui_impl.py",
    "term_len"
   ],
   "desc": "check what `term_len` means inside `src/click/_termui_impl.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/_textwrap.py",
    "term_len"
   ],
   "desc": "check what `term_len` means inside `src/click/_textwrap.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/formatting.py",
    "term_len"
   ],
   "desc": "check what `term_len` means inside `src/click/formatting.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "tests/test_compat.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `tests/test_compat.py`"
  }
 ],
 "candidates": [
  {
   "call": "grep('\\\\bterm_len\\\\s*\\\\(', 'examples')",
   "key": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \"examples\"]]",
   "v1": [
    1007582417549249,
    100961337544704
   ],
   "v2": [
    56956689176004234467,
    5792959625640026112
   ],
   "p_cap": [
    5,
    1596
   ],
   "forecast": {
    "zero": [
     1441,
     1596
    ],
    "mid": [
     25,
     266
    ],
    "cap": [
     5,
     1596
    ]
   },
   "serves": [
    [
     "cover",
     "CALL",
     "examples"
    ]
   ]
  },
  {
   "call": "grep('\\\\bterm_len\\\\s*\\\\(', 'tests')",
   "key": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \"tests\"]]",
   "v1": [
    3044418612629724137,
    304892611875790848
   ],
   "v2": [
    56956689176004234467,
    5792959625640026112
   ],
   "p_cap": [
    403,
    110376
   ],
   "forecast": {
    "zero": [
     97883,
     110376
    ],
    "mid": [
     2015,
     18396
    ],
    "cap": [
     403,
     110376
    ]
   },
   "serves": [
    [
     "cover",
     "CALL",
     "tests"
    ]
   ]
  },
  {
   "call": "grep('\\\\bterm_len\\\\s*\\\\(', 'src')",
   "key": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \"src\"]]",
   "v1": [
    3742716076506047,
    374824075014144
   ],
   "v2": [
    17848447945436455,
    1815324441735168
   ],
   "p_cap": [
    187,
    51156
   ],
   "forecast": {
    "zero": [
     45359,
     51156
    ],
    "mid": [
     935,
     8526
    ],
    "cap": [
     187,
     51156
    ]
   },
   "serves": [
    [
     "cover",
     "CALL",
     "src"
    ]
   ]
  },
  {
   "call": "symbols('src/click/_termui_impl.py', 'term_len')",
   "key": "[\"symbols\", [\"src/click/_termui_impl.py\", \"term_len\"]]",
   "v1": [
    58896286560336191,
    5800848779980800
   ],
   "v2": [
    25240041107503577,
    2524033438617600
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
     "src/click/_termui_impl.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "symbols('src/click/_textwrap.py', 'term_len')",
   "key": "[\"symbols\", [\"src/click/_textwrap.py\", \"term_len\"]]",
   "v1": [
    58896286560336191,
    5800848779980800
   ],
   "v2": [
    25240041107503577,
    2524033438617600
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
     "src/click/_textwrap.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "symbols('src/click/formatting.py', 'term_len')",
   "key": "[\"symbols\", [\"src/click/formatting.py\", \"term_len\"]]",
   "v1": [
    58896286560336191,
    5800848779980800
   ],
   "v2": [
    25240041107503577,
    2524033438617600
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
     "src/click/formatting.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "calls('src/click/_compat.py', 'term_len')",
   "key": "[\"calls\", [\"src/click/_compat.py\", \"term_len\"]]",
   "v1": [
    11814062404747123,
    1160169755996160
   ],
   "v2": [
    5063152422132421,
    504806687723520
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
     "src/click/_compat.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "calls('tests/test_compat.py', 'term_len')",
   "key": "[\"calls\", [\"tests/test_compat.py\", \"term_len\"]]",
   "v1": [
    11814062404747123,
    1160169755996160
   ],
   "v2": [
    5063152422132421,
    504806687723520
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
     "tests/test_compat.py",
     "term_len"
    ]
   ]
  }
 ],
 "choice": {
  "call": "grep('\\\\bterm_len\\\\s*\\\\(', 'examples')",
  "key": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \"examples\"]]",
  "provenance": "call lines naming `term_len` under `examples` (step 2)",
  "v2": [
   56956689176004234467,
   5792959625640026112
  ]
 },
 "forecast": {
  "zero": [
   1441,
   1596
  ],
  "mid": [
   25,
   266
  ],
  "cap": [
   5,
   1596
  ]
 },
 "plan": {
  "zero": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \"tests\"]]",
  "mid": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \"tests\"]]",
  "cap": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \"tests\"]]"
 },
 "hedges": [
  {
   "outcome": "zero",
   "word": "almost certainly",
   "p": [
    144
```
</details>

## Step 10

Nothing under `examples` for calls of `term_len`, and the search was not capped, so that part of the tree is clear.

Let me search `tests` for calls of `term_len`; the search has to be complete before I can call the set final. Very likely nothing turns up. If it fits under the cap, I will search `src` for calls of `term_len`.

**Call:** `grep('\\bterm_len\\s*\\(', 'tests')`

**Response**: outcome `mid`

```
tests/test_compat.py:129:    assert term_len(f"a{seq}b") == 2
tests/test_compat.py:172:    assert term_len(text) == len(expected)
tests/test_compat.py:199:    assert term_len(text) == len(text)
tests/test_compat.py:239:    assert term_len(text) == visible
tests/test_compat.py:270:    assert term_len(out) <= max(n, 0)
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
    "src"
   ],
   "desc": "search `src` for calls of `term_len`"
  },
  {
   "kind": "cover",
   "key": [
    "cover",
    "CALL",
    "tests"
   ],
   "desc": "search `tests` for calls of `term_len`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/click/_compat.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `src/click/_compat.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/_termui_impl.py",
    "term_len"
   ],
   "desc": "check what `term_len` means inside `src/click/_termui_impl.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/_textwrap.py",
    "term_len"
   ],
   "desc": "check what `term_len` means inside `src/click/_textwrap.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/formatting.py",
    "term_len"
   ],
   "desc": "check what `term_len` means inside `src/click/formatting.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "tests/test_compat.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `tests/test_compat.py`"
  }
 ],
 "candidates": [
  {
   "call": "grep('\\\\bterm_len\\\\s*\\\\(', 'src')",
   "key": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \"src\"]]",
   "v1": [
    7146539249045123,
    812118829197312
   ],
   "v2": [
    18465598649282371529,
    2134248283130535936
   ],
   "p_cap": [
    187,
    51156
   ],
   "forecast": {
    "zero": [
     45359,
     51156
    ],
    "mid": [
     935,
     8526
    ],
    "cap": [
     187,
     51156
    ]
   },
   "serves": [
    [
     "cover",
     "CALL",
     "src"
    ]
   ]
  },
  {
   "call": "grep('\\\\bterm_len\\\\s*\\\\(', 'tests')",
   "key": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \"tests\"]]",
   "v1": [
    2683001442181888655,
    304892611875790848
   ],
   "v2": [
    18465598649282371529,
    2134248283130535936
   ],
   "p_cap": [
    403,
    110376
   ],
   "forecast": {
    "zero": [
     97883,
     110376
    ],
    "mid": [
     2015,
     18396
    ],
    "cap": [
     403,
     110376
    ]
   },
   "serves": [
    [
     "cover",
     "CALL",
     "tests"
    ]
   ]
  },
  {
   "call": "symbols('src/click/_termui_impl.py', 'term_len')",
   "key": "[\"symbols\", [\"src/click/_termui_impl.py\", \"term_len\"]]",
   "v1": [
    78030012875668799,
    8701273169971200
   ],
   "v2": [
    67227482360485111799,
    7622315296894771200
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
     "src/click/_termui_impl.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "symbols('src/click/_textwrap.py', 'term_len')",
   "key": "[\"symbols\", [\"src/click/_textwrap.py\", \"term_len\"]]",
   "v1": [
    78030012875668799,
    8701273169971200
   ],
   "v2": [
    67227482360485111799,
    7622315296894771200
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
     "src/click/_textwrap.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "symbols('src/click/formatting.py', 'term_len')",
   "key": "[\"symbols\", [\"src/click/formatting.py\", \"term_len\"]]",
   "v1": [
    78030012875668799,
    8701273169971200
   ],
   "v2": [
    67227482360485111799,
    7622315296894771200
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
     "src/click/formatting.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "calls('src/click/_compat.py', 'term_len')",
   "key": "[\"calls\", [\"src/click/_compat.py\", \"term_len\"]]",
   "v1": [
    15658210214153587,
    1740254633994240
   ],
   "v2": [
    13491230363878390987,
    1524463059378954240
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
     "src/click/_compat.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "calls('tests/test_compat.py', 'term_len')",
   "key": "[\"calls\", [\"tests/test_compat.py\", \"term_len\"]]",
   "v1": [
    15658210214153587,
    1740254633994240
   ],
   "v2": [
    13491230363878390987,
    1524463059378954240
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
     "tests/test_compat.py",
     "term_len"
    ]
   ]
  }
 ],
 "choice": {
  "call": "grep('\\\\bterm_len\\\\s*\\\\(', 'tests')",
  "key": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \"tests\"]]",
  "provenance": "call lines naming `term_len` under `tests` (task)",
  "v2": [
   18465598649282371529,
   2134248283130535936
  ]
 },
 "forecast": {
  "zero": [
   97883,
   110376
  ],
  "mid": [
   2015,
   18396
  ],
  "cap": [
   403,
   110376
  ]
 },
 "plan": {
  "zero": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \"src\"]]",
  "mid": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \"src\"]]",
  "cap": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \"src\"]]"
 },
 "hedges": [
  {
   "outcome": "zero",
   "word": "very likely",
   "p": [
    97883,
    110376
   ]
  }
 ],
 "adherence": {
  "planned": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \"tests\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "grep",
   "step": 10,
   "pattern": "\\bterm_len\\s*\\(",
   "scope": "tests",
   "hits": [
    [
     "tests/test_compat.py",
     129
    ],
    [
     "tests/test_compat.py",
     172
    ],
    [
     "tests/test_compat.py",
     199
    ],
    [
     "tests/test_compat.py",
     239
    ],
    [
     "tests/test_compat.py",
     270
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
```
</details>

## Step 11

5 matching lines under `tests` for calls of `term_len`, in `tests/test_compat.py`, and the search was under the cap, so that is the complete set there.

I'll search `src` for calls of `term_len`; the search has to be complete before I can call the set final. Very likely nothing turns up. If it fits under the cap, I will look at `src/click/_termui_impl.py`'s top-level names for `term_len`.

**Call:** `grep('\\bterm_len\\s*\\(', 'src')`

**Response**: outcome `mid`

```
src/click/_compat.py:536:def term_len(x: str) -> int:
src/click/_termui_impl.py:268:            clutter_length = term_len(self.format_progress_line())
src/click/_termui_impl.py:282:        line_len = term_len(line)
src/click/_textwrap.py:89:            if term_len(indent) + term_len(self.placeholder.lstrip()) > self.width:
src/click/_textwrap.py:103:            width = self.width - term_len(indent)
src/click/_textwrap.py:109:                n = term_len(chunks[-1])
src/click/_textwrap.py:118:            if chunks and term_len(chunks[-1]) > width:
src/click/_textwrap.py:123:                cur_len -= term_len(cur_line[-1])
src/click/_textwrap.py:143:                            and cur_len + term_len(self.placeholder) <= width
src/click/_textwrap.py:148:                        cur_len -= term_len(cur_line[-1])
src/click/_textwrap.py:154:                                term_len(prev_line) + term_len(self.placeholder)
src/click/formatting.py:19:            widths[idx] = max(widths.get(idx, 0), term_len(col))
src/click/formatting.py:93:                orig_len = term_len(line)
src/click/formatting.py:95:                indent = orig_len - term_len(line)
src/click/formatting.py:180:        if text_width >= (term_len(usage_prefix) + 20):
src/click/formatting.py:182:            indent = " " * term_len(usage_prefix)
src/click/formatting.py:195:            indent = " " * (max(self.current_indent, term_len(prefix)) + 4)
src/click/formatting.py:255:            if term_len(first) <= first_col - col_spacing:
src/click/formatting.py:256:                self.write(" " * (first_col - term_len(first)))
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
    "src"
   ],
   "desc": "search `src` for calls of `term_len`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/click/_compat.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `src/click/_compat.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/_termui_impl.py",
    "term_len"
   ],
   "desc": "check what `term_len` means inside `src/click/_termui_impl.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/_textwrap.py",
    "term_len"
   ],
   "desc": "check what `term_len` means inside `src/click/_textwrap.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/formatting.py",
    "term_len"
   ],
   "desc": "check what `term_len` means inside `src/click/formatting.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "tests/test_compat.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `tests/test_compat.py`"
  }
 ],
 "candidates": [
  {
   "call": "grep('\\\\bterm_len\\\\s*\\\\(', 'src')",
   "key": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \"src\"]]",
   "v1": [
    2182538940821345,
    286630175010816
   ],
   "v2": [
    54706788608039033,
    7165754375270400
   ],
   "p_cap": [
    187,
    51156
   ],
   "forecast": {
    "zero": [
     45359,
     51156
    ],
    "mid": [
     935,
     8526
    ],
    "cap": [
     187,
     51156
    ]
   },
   "serves": [
    [
     "cover",
     "CALL",
     "src"
    ]
   ]
  },
  {
   "call": "symbols('src/click/_termui_impl.py', 'term_len')",
   "key": "[\"symbols\", [\"src/click/_termui_impl.py\", \"term_len\"]]",
   "v1": [
    135431191821666623,
    17402546339942400
   ],
   "v2": [
    54706788608039033,
    7165754375270400
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
     "src/click/_termui_impl.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "symbols('src/click/_textwrap.py', 'term_len')",
   "key": "[\"symbols\", [\"src/click/_textwrap.py\", \"term_len\"]]",
   "v1": [
    135431191821666623,
    17402546339942400
   ],
   "v2": [
    54706788608039033,
    7165754375270400
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
     "src/click/_textwrap.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "symbols('src/click/formatting.py', 'term_len')",
   "key": "[\"symbols\", [\"src/click/formatting.py\", \"term_len\"]]",
   "v1": [
    135431191821666623,
    17402546339942400
   ],
   "v2": [
    54706788608039033,
    7165754375270400
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
     "src/click/formatting.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "calls('src/click/_compat.py', 'term_len')",
   "key": "[\"calls\", [\"src/click/_compat.py\", \"term_len\"]]",
   "v1": [
    27190653642372979,
    3480509267988480
   ],
   "v2": [
    10984352247859429,
    1433150875054080
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
     "src/click/_compat.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "calls('tests/test_compat.py', 'term_len')",
   "key": "[\"calls\", [\"tests/test_compat.py\", \"term_len\"]]",
   "v1": [
    27190653642372979,
    3480509267988480
   ],
   "v2": [
    10984352247859429,
    1433150875054080
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
     "tests/test_compat.py",
     "term_len"
    ]
   ]
  }
 ],
 "choice": {
  "call": "grep('\\\\bterm_len\\\\s*\\\\(', 'src')",
  "key": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \"src\"]]",
  "provenance": "call lines naming `term_len` under `src` (step 2)",
  "v2": [
   54706788608039033,
   7165754375270400
  ]
 },
 "forecast": {
  "zero": [
   45359,
   51156
  ],
  "mid": [
   935,
   8526
  ],
  "cap": [
   187,
   51156
  ]
 },
 "plan": {
  "zero": "[\"symbols\", [\"src/click/_termui_impl.py\", \"term_len\"]]",
  "mid": "[\"symbols\", [\"src/click/_termui_impl.py\", \"term_len\"]]",
  "cap": "[\"symbols\", [\"src/click/_termui_impl.py\", \"term_len\"]]"
 },
 "hedges": [
  {
   "outcome": "zero",
   "word": "very likely",
   "p": [
    45359,
    51156
   ]
  }
 ],
 "adherence": {
  "planned": "[\"grep\", [\"\\\\bterm_len\\\\s*\\\\(\", \"src\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "grep",
   "step": 11,
   "pattern": "\\bterm_len\\s*\\(",
   "scope": "src",
   "hits": [
    [
     "src/click/_compat.py",
     536
    ],
    [
     "src/click/_termui_impl.py",
     268
    ],
    [
     "src/click/_termui_impl.py",
     282
    ],
    [
     "src/click/_textwrap.py",
     89
    ],
    [
     "src/click/_textwrap.py",
     103
    ],
    [
     "src/click/_textwrap.py",
     109
    ],
    [
     "src/click/_textwrap.py",
     118
    ],
    [
     "src/click/_textwrap.py",
     123
    ],
    [
     "src/click/_textwrap.py",
     143
    ],
    [
     "src/click/_textwrap.py",
     148
    ],
    [
     "src/click/_textwrap.py",
     154
    ],
    [
     "src/click/formatting.py",
     19
    ],
    [
     "src/click/formatting.py",
     93
    ],
    [
     "src/click/formatting.py",
     95
    ],
    [
     "src/click/formatting.py",
     180
    ],
    [
     "src/click/formatting.py",
     182
    ],
    [
     "src/click/formatting.py",
     195
    ],
    [
     "src/click/formatting.py",
     255
    ],
    [
     "src/click/formatting.py",
     256
    ]
   ],
   "capped": false
  }
 ],
 "goa
```
</details>

## Step 12

19 matching lines under `src` for calls of `term_len`, in `src/click/_compat.py`, `src/click/_termui_impl.py`, `src/click/_textwrap.py`, `src/click/formatting.py`, and the search was under the cap, so that is the complete set there.

Tally: 0 call sites confirmed, 0 ruled out, 5 pending. The search itself is complete; what is left is checking the candidates.

Still open: list the call sites of `term_len` in `src/click/_compat.py`; check what `term_len` means inside `src/click/_termui_impl.py`; check what `term_len` means inside `src/click/_textwrap.py`; and 2 more.

Next I will look at `src/click/_termui_impl.py`'s top-level names for `term_len`; before counting calls I need to know the name refers to our definition there. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `src/click/_textwrap.py`'s top-level names for `term_len`.

**Call:** `symbols('src/click/_termui_impl.py', 'term_len')`

**Response**: outcome `ok`

```
module src/click/_termui_impl.py lines=973 dynamic=no all=none
27 from term_len <- ._compat term_len
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/click/_compat.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `src/click/_compat.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/_termui_impl.py",
    "term_len"
   ],
   "desc": "check what `term_len` means inside `src/click/_termui_impl.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/_textwrap.py",
    "term_len"
   ],
   "desc": "check what `term_len` means inside `src/click/_textwrap.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/formatting.py",
    "term_len"
   ],
   "desc": "check what `term_len` means inside `src/click/formatting.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "tests/test_compat.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `tests/test_compat.py`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/click/_termui_impl.py', 'term_len')",
   "key": "[\"symbols\", [\"src/click/_termui_impl.py\", \"term_len\"]]",
   "v1": [
    9549301,
    1447550
   ],
   "v2": [
    4789126,
    723775
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
     "src/click/_termui_impl.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "symbols('src/click/_textwrap.py', 'term_len')",
   "key": "[\"symbols\", [\"src/click/_textwrap.py\", \"term_len\"]]",
   "v1": [
    9549301,
    1447550
   ],
   "v2": [
    4789126,
    723775
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
     "src/click/_textwrap.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "symbols('src/click/formatting.py', 'term_len')",
   "key": "[\"symbols\", [\"src/click/formatting.py\", \"term_len\"]]",
   "v1": [
    9549301,
    1447550
   ],
   "v2": [
    4789126,
    723775
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
     "src/click/formatting.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "calls('src/click/_compat.py', 'term_len')",
   "key": "[\"calls\", [\"src/click/_compat.py\", \"term_len\"]]",
   "v1": [
    3837091,
    579020
   ],
   "v2": [
    19243357,
    2895100
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
     "src/click/_compat.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "calls('tests/test_compat.py', 'term_len')",
   "key": "[\"calls\", [\"tests/test_compat.py\", \"term_len\"]]",
   "v1": [
    3837091,
    579020
   ],
   "v2": [
    19243357,
    2895100
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
     "tests/test_compat.py",
     "term_len"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/click/_termui_impl.py', 'term_len')",
  "key": "[\"symbols\", [\"src/click/_termui_impl.py\", \"term_len\"]]",
  "provenance": "`src/click/_termui_impl.py` had a matching line (step 5); its outline names every `term_len` import exactly",
  "v2": [
   4789126,
   723775
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
  "ok": "[\"symbols\", [\"src/click/_textwrap.py\", \"term_len\"]]",
  "cap": "[\"symbols\", [\"src/click/_textwrap.py\", \"term_len\"]]"
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
  "planned": "[\"symbols\", [\"src/click/_termui_impl.py\", \"term_len\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 12,
   "path": "src/click/_termui_impl.py",
   "filter": "term_len",
   "header": {
    "lines": 973,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/click/_termui_impl.py",
     "name": "term_len",
     "line": 27,
     "kind": "from",
     "src": "._compat",
     "src_name": "term_len",
     "conditional": false,
     "col": 0,
     "bases": []
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "callers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/click/_compat.py",
   "src/click/_termui_impl.py",
   "src/click/_textwrap.py",
   "src/click/formatting.py",
   "tests/test_compat.py"
  ],
  "table": [
   [
    "src/click/_compat.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/click/_termui_impl.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/click/_textwrap.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/click/formatting.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_compat.py",
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
  "n_pending": 5
 }
}
```
</details>

## Step 13

`src/click/_termui_impl.py` does not define `term_len` itself; line 27 imports it from `._compat`.

Tally: 0 call sites confirmed, 0 ruled out, 5 pending. The search itself is complete; what is left is checking the candidates.

I'll look at `src/click/_textwrap.py`'s top-level names for `term_len`; before counting calls I need to know the name refers to our definition there. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `src/click/formatting.py`'s top-level names for `term_len`.

**Call:** `symbols('src/click/_textwrap.py', 'term_len')`

**Response**: outcome `ok`

```
module src/click/_textwrap.py lines=189 dynamic=no all=none
8 from term_len <- ._compat term_len
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/click/_compat.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `src/click/_compat.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/click/_termui_impl.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `src/click/_termui_impl.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/_textwrap.py",
    "term_len"
   ],
   "desc": "check what `term_len` means inside `src/click/_textwrap.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/formatting.py",
    "term_len"
   ],
   "desc": "check what `term_len` means inside `src/click/formatting.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "tests/test_compat.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `tests/test_compat.py`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/click/_textwrap.py', 'term_len')",
   "key": "[\"symbols\", [\"src/click/_textwrap.py\", \"term_len\"]]",
   "v1": [
    26365303,
    4342650
   ],
   "v2": [
    13226078,
    2171325
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
     "src/click/_textwrap.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "symbols('src/click/formatting.py', 'term_len')",
   "key": "[\"symbols\", [\"src/click/formatting.py\", \"term_len\"]]",
   "v1": [
    26365303,
    4342650
   ],
   "v2": [
    13226078,
    2171325
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
     "src/click/formatting.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "calls('src/click/_compat.py', 'term_len')",
   "key": "[\"calls\", [\"src/click/_compat.py\", \"term_len\"]]",
   "v1": [
    10598233,
    1737060
   ],
   "v2": [
    53164871,
    8685300
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
     "src/click/_compat.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "calls('src/click/_termui_impl.py', 'term_len')",
   "key": "[\"calls\", [\"src/click/_termui_impl.py\", \"term_len\"]]",
   "v1": [
    10598233,
    1737060
   ],
   "v2": [
    53164871,
    8685300
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
     "src/click/_termui_impl.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "calls('tests/test_compat.py', 'term_len')",
   "key": "[\"calls\", [\"tests/test_compat.py\", \"term_len\"]]",
   "v1": [
    10598233,
    1737060
   ],
   "v2": [
    53164871,
    8685300
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
     "tests/test_compat.py",
     "term_len"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/click/_textwrap.py', 'term_len')",
  "key": "[\"symbols\", [\"src/click/_textwrap.py\", \"term_len\"]]",
  "provenance": "`src/click/_textwrap.py` had a matching line (step 5); its outline names every `term_len` import exactly",
  "v2": [
   13226078,
   2171325
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
  "ok": "[\"symbols\", [\"src/click/formatting.py\", \"term_len\"]]",
  "cap": "[\"symbols\", [\"src/click/formatting.py\", \"term_len\"]]"
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
  "planned": "[\"symbols\", [\"src/click/_textwrap.py\", \"term_len\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 13,
   "path": "src/click/_textwrap.py",
   "filter": "term_len",
   "header": {
    "lines": 189,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/click/_textwrap.py",
     "name": "term_len",
     "line": 8,
     "kind": "from",
     "src": "._compat",
     "src_name": "term_len",
     "conditional": false,
     "col": 0,
     "bases": []
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "callers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/click/_compat.py",
   "src/click/_termui_impl.py",
   "src/click/_textwrap.py",
   "src/click/formatting.py",
   "tests/test_compat.py"
  ],
  "table": [
   [
    "src/click/_compat.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/click/_termui_impl.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/click/_textwrap.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/click/formatting.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_compat.py",
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
  "n_pending": 5
 }
}
```
</details>

## Step 14

`src/click/_textwrap.py` does not define `term_len` itself; line 8 imports it from `._compat`.

Tally: 0 call sites confirmed, 0 ruled out, 5 pending. The search itself is complete; what is left is checking the candidates.

Next I will look at `src/click/formatting.py`'s top-level names for `term_len`; before counting calls I need to know the name refers to our definition there. Almost certainly the outline shows what I need. If the outline is too long to fit, I will list the call sites of `term_len` in `src/click/_compat.py`.

**Call:** `symbols('src/click/formatting.py', 'term_len')`

**Response**: outcome `ok`

```
module src/click/formatting.py lines=321 dynamic=no all=none
7 from term_len <- ._compat term_len
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/click/_compat.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `src/click/_compat.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/click/_termui_impl.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `src/click/_termui_impl.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/click/_textwrap.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `src/click/_textwrap.py`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/click/formatting.py",
    "term_len"
   ],
   "desc": "check what `term_len` means inside `src/click/formatting.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "tests/test_compat.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `tests/test_compat.py`"
  }
 ],
 "candidates": [
  {
   "call": "calls('src/click/_compat.py', 'term_len')",
   "key": "[\"calls\", [\"src/click/_compat.py\", \"term_len\"]]",
   "v1": [
    9685193,
    1737060
   ],
   "v2": [
    48599671,
    8685300
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
     "src/click/_compat.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "calls('src/click/_termui_impl.py', 'term_len')",
   "key": "[\"calls\", [\"src/click/_termui_impl.py\", \"term_len\"]]",
   "v1": [
    9685193,
    1737060
   ],
   "v2": [
    48599671,
    8685300
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
     "src/click/_termui_impl.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "calls('src/click/_textwrap.py', 'term_len')",
   "key": "[\"calls\", [\"src/click/_textwrap.py\", \"term_len\"]]",
   "v1": [
    9685193,
    1737060
   ],
   "v2": [
    48599671,
    8685300
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
     "src/click/_textwrap.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "calls('tests/test_compat.py', 'term_len')",
   "key": "[\"calls\", [\"tests/test_compat.py\", \"term_len\"]]",
   "v1": [
    9685193,
    1737060
   ],
   "v2": [
    48599671,
    8685300
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
     "tests/test_compat.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "symbols('src/click/formatting.py', 'term_len')",
   "key": "[\"symbols\", [\"src/click/formatting.py\", \"term_len\"]]",
   "v1": [
    24082703,
    4342650
   ],
   "v2": [
    48599671,
    8685300
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
     "src/click/formatting.py",
     "term_len"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/click/formatting.py', 'term_len')",
  "key": "[\"symbols\", [\"src/click/formatting.py\", \"term_len\"]]",
  "provenance": "`src/click/formatting.py` had a matching line (step 5); its outline names every `term_len` import exactly",
  "v2": [
   48599671,
   8685300
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
  "ok": "[\"calls\", [\"src/click/_compat.py\", \"term_len\"]]",
  "cap": "[\"calls\", [\"src/click/_compat.py\", \"term_len\"]]"
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
  "planned": "[\"symbols\", [\"src/click/formatting.py\", \"term_len\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 14,
   "path": "src/click/formatting.py",
   "filter": "term_len",
   "header": {
    "lines": 321,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "src/click/formatting.py",
     "name": "term_len",
     "line": 7,
     "kind": "from",
     "src": "._compat",
     "src_name": "term_len",
     "conditional": false,
     "col": 0,
     "bases": []
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "callers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/click/_compat.py",
   "src/click/_termui_impl.py",
   "src/click/_textwrap.py",
   "src/click/formatting.py",
   "tests/test_compat.py"
  ],
  "table": [
   [
    "src/click/_compat.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/click/_termui_impl.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/click/_textwrap.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/click/formatting.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_compat.py",
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
  "n_pending": 5
 }
}
```
</details>

## Step 15

`src/click/formatting.py` does not define `term_len` itself; line 7 imports it from `._compat`.

Tally: 0 call sites confirmed, 0 ruled out, 5 pending. The search itself is complete; what is left is checking the candidates.

Let me list the call sites of `term_len` in `src/click/_compat.py`; the name is ours there, so each call site counts. Almost certainly the call sites fit. If there are too many call sites, I will list the call sites of `term_len` in `src/click/_termui_impl.py`.

**Call:** `calls('src/click/_compat.py', 'term_len')`

**Response**: outcome `ok`

```
calls of term_len in src/click/_compat.py count=0
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/click/_compat.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `src/click/_compat.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/click/_termui_impl.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `src/click/_termui_impl.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/click/_textwrap.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `src/click/_textwrap.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/click/formatting.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `src/click/formatting.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "tests/test_compat.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `tests/test_compat.py`"
  }
 ],
 "candidates": [
  {
   "call": "calls('src/click/_compat.py', 'term_len')",
   "key": "[\"calls\", [\"src/click/_compat.py\", \"term_len\"]]",
   "v1": [
    101,
    20
   ],
   "v2": [
    51,
    10
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
     "src/click/_compat.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "calls('src/click/_termui_impl.py', 'term_len')",
   "key": "[\"calls\", [\"src/click/_termui_impl.py\", \"term_len\"]]",
   "v1": [
    101,
    20
   ],
   "v2": [
    51,
    10
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
     "src/click/_termui_impl.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "calls('src/click/_textwrap.py', 'term_len')",
   "key": "[\"calls\", [\"src/click/_textwrap.py\", \"term_len\"]]",
   "v1": [
    101,
    20
   ],
   "v2": [
    51,
    10
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
     "src/click/_textwrap.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "calls('src/click/formatting.py', 'term_len')",
   "key": "[\"calls\", [\"src/click/formatting.py\", \"term_len\"]]",
   "v1": [
    101,
    20
   ],
   "v2": [
    51,
    10
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
     "src/click/formatting.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "calls('tests/test_compat.py', 'term_len')",
   "key": "[\"calls\", [\"tests/test_compat.py\", \"term_len\"]]",
   "v1": [
    101,
    20
   ],
   "v2": [
    51,
    10
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
     "tests/test_compat.py",
     "term_len"
    ]
   ]
  }
 ],
 "choice": {
  "call": "calls('src/click/_compat.py', 'term_len')",
  "key": "[\"calls\", [\"src/click/_compat.py\", \"term_len\"]]",
  "provenance": "call sites of `term_len` in `src/click/_compat.py` that refer to the module-level binding",
  "v2": [
   51,
   10
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
  "ok": "[\"calls\", [\"src/click/_termui_impl.py\", \"term_len\"]]",
  "cap": "[\"calls\", [\"src/click/_termui_impl.py\", \"term_len\"]]"
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
  "planned": "[\"calls\", [\"src/click/_compat.py\", \"term_len\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "calls",
   "step": 15,
   "path": "src/click/_compat.py",
   "name": "term_len",
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
   "src/click/_compat.py",
   "src/click/_termui_impl.py",
   "src/click/_textwrap.py",
   "src/click/formatting.py",
   "tests/test_compat.py"
  ],
  "table": [
   [
    "src/click/_compat.py",
    "src/click/_compat.py",
    "out",
    "the module binds the name but never calls it by bare name"
   ],
   [
    "src/click/_termui_impl.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/click/_textwrap.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/click/formatting.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_compat.py",
    null,
    "pending",
    "not yet examined"
   ]
  ],
  "uncovered": {
   "CALL": []
  },
  "n_in": 0,
  "n_out": 1,
  "n_pending": 4
 }
}
```
</details>

## Step 16

`src/click/_compat.py` binds `term_len` but never actually calls it by that name.

Tally: 0 call sites confirmed, 1 ruled out, 4 pending. The search itself is complete; what is left is checking the candidates.

I'll list the call sites of `term_len` in `src/click/_termui_impl.py`; the name is ours there, so each call site counts. Almost certainly the call sites fit. If there are too many call sites, I will list the call sites of `term_len` in `src/click/_textwrap.py`.

**Call:** `calls('src/click/_termui_impl.py', 'term_len')`

**Response**: outcome `ok`

```
calls of term_len in src/click/_termui_impl.py count=2
268:            clutter_length = term_len(self.format_progress_line())
282:        line_len = term_len(line)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/click/_termui_impl.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `src/click/_termui_impl.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/click/_textwrap.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `src/click/_textwrap.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/click/formatting.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `src/click/formatting.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "tests/test_compat.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `tests/test_compat.py`"
  }
 ],
 "candidates": [
  {
   "call": "calls('src/click/_termui_impl.py', 'term_len')",
   "key": "[\"calls\", [\"src/click/_termui_impl.py\", \"term_len\"]]",
   "v1": [
    81,
    20
   ],
   "v2": [
    41,
    10
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
     "src/click/_termui_impl.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "calls('src/click/_textwrap.py', 'term_len')",
   "key": "[\"calls\", [\"src/click/_textwrap.py\", \"term_len\"]]",
   "v1": [
    81,
    20
   ],
   "v2": [
    41,
    10
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
     "src/click/_textwrap.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "calls('src/click/formatting.py', 'term_len')",
   "key": "[\"calls\", [\"src/click/formatting.py\", \"term_len\"]]",
   "v1": [
    81,
    20
   ],
   "v2": [
    41,
    10
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
     "src/click/formatting.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "calls('tests/test_compat.py', 'term_len')",
   "key": "[\"calls\", [\"tests/test_compat.py\", \"term_len\"]]",
   "v1": [
    81,
    20
   ],
   "v2": [
    41,
    10
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
     "tests/test_compat.py",
     "term_len"
    ]
   ]
  }
 ],
 "choice": {
  "call": "calls('src/click/_termui_impl.py', 'term_len')",
  "key": "[\"calls\", [\"src/click/_termui_impl.py\", \"term_len\"]]",
  "provenance": "call sites of `term_len` in `src/click/_termui_impl.py` that refer to the module-level binding",
  "v2": [
   41,
   10
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
  "ok": "[\"calls\", [\"src/click/_textwrap.py\", \"term_len\"]]",
  "cap": "[\"calls\", [\"src/click/_textwrap.py\", \"term_len\"]]"
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
  "planned": "[\"calls\", [\"src/click/_termui_impl.py\", \"term_len\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "calls",
   "step": 16,
   "path": "src/click/_termui_impl.py",
   "name": "term_len",
   "lines": [
    268,
    282
   ],
   "count": 2,
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "callers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/click/_compat.py",
   "src/click/_termui_impl.py",
   "src/click/_textwrap.py",
   "src/click/formatting.py",
   "tests/test_compat.py"
  ],
  "table": [
   [
    "src/click/_compat.py",
    "src/click/_compat.py",
    "out",
    "the module binds the name but never calls it by bare name"
   ],
   [
    "src/click/_termui_impl.py",
    "src/click/_termui_impl.py:268",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/_termui_impl.py",
    "src/click/_termui_impl.py:282",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/_textwrap.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/click/formatting.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_compat.py",
    null,
    "pending",
    "not yet examined"
   ]
  ],
  "uncovered": {
   "CALL": []
  },
  "n_in": 2,
  "n_out": 1,
  "n_pending": 3
 }
}
```
</details>

## Step 17

`src/click/_termui_impl.py` calls `term_len` at lines 268, 282, and those are real calls of the module-level name, not a shadowed local.

Tally: 2 call sites confirmed, 1 ruled out, 3 pending. The search itself is complete; what is left is checking the candidates.

Let me list the call sites of `term_len` in `src/click/_textwrap.py`; the name is ours there, so each call site counts. Almost certainly the call sites fit. If there are too many call sites, I will list the call sites of `term_len` in `src/click/formatting.py`.

**Call:** `calls('src/click/_textwrap.py', 'term_len')`

**Response**: outcome `ok`

```
calls of term_len in src/click/_textwrap.py count=8
89:            if term_len(indent) + term_len(self.placeholder.lstrip()) > self.width:
103:            width = self.width - term_len(indent)
109:                n = term_len(chunks[-1])
118:            if chunks and term_len(chunks[-1]) > width:
123:                cur_len -= term_len(cur_line[-1])
143:                            and cur_len + term_len(self.placeholder) <= width
148:                        cur_len -= term_len(cur_line[-1])
154:                                term_len(prev_line) + term_len(self.placeholder)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/click/_textwrap.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `src/click/_textwrap.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/click/formatting.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `src/click/formatting.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "tests/test_compat.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `tests/test_compat.py`"
  }
 ],
 "candidates": [
  {
   "call": "calls('src/click/_textwrap.py', 'term_len')",
   "key": "[\"calls\", [\"src/click/_textwrap.py\", \"term_len\"]]",
   "v1": [
    61,
    20
   ],
   "v2": [
    31,
    10
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
     "src/click/_textwrap.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "calls('src/click/formatting.py', 'term_len')",
   "key": "[\"calls\", [\"src/click/formatting.py\", \"term_len\"]]",
   "v1": [
    61,
    20
   ],
   "v2": [
    31,
    10
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
     "src/click/formatting.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "calls('tests/test_compat.py', 'term_len')",
   "key": "[\"calls\", [\"tests/test_compat.py\", \"term_len\"]]",
   "v1": [
    61,
    20
   ],
   "v2": [
    31,
    10
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
     "tests/test_compat.py",
     "term_len"
    ]
   ]
  }
 ],
 "choice": {
  "call": "calls('src/click/_textwrap.py', 'term_len')",
  "key": "[\"calls\", [\"src/click/_textwrap.py\", \"term_len\"]]",
  "provenance": "call sites of `term_len` in `src/click/_textwrap.py` that refer to the module-level binding",
  "v2": [
   31,
   10
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
  "ok": "[\"calls\", [\"src/click/formatting.py\", \"term_len\"]]",
  "cap": "[\"calls\", [\"src/click/formatting.py\", \"term_len\"]]"
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
  "planned": "[\"calls\", [\"src/click/_textwrap.py\", \"term_len\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "calls",
   "step": 17,
   "path": "src/click/_textwrap.py",
   "name": "term_len",
   "lines": [
    89,
    103,
    109,
    118,
    123,
    143,
    148,
    154
   ],
   "count": 8,
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "callers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/click/_compat.py",
   "src/click/_termui_impl.py",
   "src/click/_textwrap.py",
   "src/click/formatting.py",
   "tests/test_compat.py"
  ],
  "table": [
   [
    "src/click/_compat.py",
    "src/click/_compat.py",
    "out",
    "the module binds the name but never calls it by bare name"
   ],
   [
    "src/click/_termui_impl.py",
    "src/click/_termui_impl.py:268",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/_termui_impl.py",
    "src/click/_termui_impl.py:282",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/_textwrap.py",
    "src/click/_textwrap.py:89",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/_textwrap.py",
    "src/click/_textwrap.py:103",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/_textwrap.py",
    "src/click/_textwrap.py:109",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/_textwrap.py",
    "src/click/_textwrap.py:118",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/_textwrap.py",
    "src/click/_textwrap.py:123",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/_textwrap.py",
    "src/click/_textwrap.py:143",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/_textwrap.py",
    "src/click/_textwrap.py:148",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/_textwrap.py",
    "src/click/_textwrap.py:154",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/formatting.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "tests/test_compat.py",
    null,
    "pending",
    "not yet examined"
   ]
  ],
  "uncovered": {
   "CALL": []
  },
  "n_in": 10,
  "n_out": 1,
  "n_pending": 2
 }
}
```
</details>

## Step 18

`src/click/_textwrap.py` calls `term_len` at lines 89, 103, 109, 118, 123, 143 and 2 more, and those are real calls of the module-level name, not a shadowed local.

Tally: 10 call sites confirmed, 1 ruled out, 2 pending. The search itself is complete; what is left is checking the candidates.

Next I will list the call sites of `term_len` in `src/click/formatting.py`; the name is ours there, so each call site counts. Almost certainly the call sites fit. If there are too many call sites, I will list the call sites of `term_len` in `tests/test_compat.py`.

**Call:** `calls('src/click/formatting.py', 'term_len')`

**Response**: outcome `ok`

```
calls of term_len in src/click/formatting.py count=8
19:            widths[idx] = max(widths.get(idx, 0), term_len(col))
93:                orig_len = term_len(line)
95:                indent = orig_len - term_len(line)
180:        if text_width >= (term_len(usage_prefix) + 20):
182:            indent = " " * term_len(usage_prefix)
195:            indent = " " * (max(self.current_indent, term_len(prefix)) + 4)
255:            if term_len(first) <= first_col - col_spacing:
256:                self.write(" " * (first_col - term_len(first)))
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "calls",
   "key": [
    "calls",
    "src/click/formatting.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `src/click/formatting.py`"
  },
  {
   "kind": "calls",
   "key": [
    "calls",
    "tests/test_compat.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `tests/test_compat.py`"
  }
 ],
 "candidates": [
  {
   "call": "calls('src/click/formatting.py', 'term_len')",
   "key": "[\"calls\", [\"src/click/formatting.py\", \"term_len\"]]",
   "v1": [
    41,
    20
   ],
   "v2": [
    21,
    10
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
     "src/click/formatting.py",
     "term_len"
    ]
   ]
  },
  {
   "call": "calls('tests/test_compat.py', 'term_len')",
   "key": "[\"calls\", [\"tests/test_compat.py\", \"term_len\"]]",
   "v1": [
    41,
    20
   ],
   "v2": [
    21,
    10
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
     "tests/test_compat.py",
     "term_len"
    ]
   ]
  }
 ],
 "choice": {
  "call": "calls('src/click/formatting.py', 'term_len')",
  "key": "[\"calls\", [\"src/click/formatting.py\", \"term_len\"]]",
  "provenance": "call sites of `term_len` in `src/click/formatting.py` that refer to the module-level binding",
  "v2": [
   21,
   10
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
  "ok": "[\"calls\", [\"tests/test_compat.py\", \"term_len\"]]",
  "cap": "[\"calls\", [\"tests/test_compat.py\", \"term_len\"]]"
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
  "planned": "[\"calls\", [\"src/click/formatting.py\", \"term_len\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "calls",
   "step": 18,
   "path": "src/click/formatting.py",
   "name": "term_len",
   "lines": [
    19,
    93,
    95,
    180,
    182,
    195,
    255,
    256
   ],
   "count": 8,
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "callers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/click/_compat.py",
   "src/click/_termui_impl.py",
   "src/click/_textwrap.py",
   "src/click/formatting.py",
   "tests/test_compat.py"
  ],
  "table": [
   [
    "src/click/_compat.py",
    "src/click/_compat.py",
    "out",
    "the module binds the name but never calls it by bare name"
   ],
   [
    "src/click/_termui_impl.py",
    "src/click/_termui_impl.py:268",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/_termui_impl.py",
    "src/click/_termui_impl.py:282",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/_textwrap.py",
    "src/click/_textwrap.py:89",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/_textwrap.py",
    "src/click/_textwrap.py:103",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/_textwrap.py",
    "src/click/_textwrap.py:109",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/_textwrap.py",
    "src/click/_textwrap.py:118",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/_textwrap.py",
    "src/click/_textwrap.py:123",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/_textwrap.py",
    "src/click/_textwrap.py:143",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/_textwrap.py",
    "src/click/_textwrap.py:148",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/_textwrap.py",
    "src/click/_textwrap.py:154",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/formatting.py",
    "src/click/formatting.py:19",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/formatting.py",
    "src/click/formatting.py:93",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/formatting.py",
    "src/click/formatting.py:95",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/formatting.py",
    "src/click/formatting.py:180",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/formatting.py",
    "src/click/formatting.py:182",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/formatting.py",
    "src/click/formatting.py:195",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/formatting.py",
    "src/click/formatting.py:255",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/formatting.py",
    "src/click/formatting.py:256",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "tests/test_compat.py",
    null,
    "pending",
    "not yet examined"
   ]
  ],
  "uncovered": {
   "CALL": []
  },
  "n_in": 18,
  "n_out": 1,
  "n_pending": 1
 }
}
```
</details>

## Step 19

`src/click/formatting.py` calls `term_len` at lines 19, 93, 95, 180, 182, 195 and 2 more, and those are real calls of the module-level name, not a shadowed local.

Tally: 18 call sites confirmed, 1 ruled out, 1 pending. The search itself is complete; what is left is checking the candidates.

I'll list the call sites of `term_len` in `tests/test_compat.py`; the name is ours there, so each call site counts. Almost certainly the call sites fit. If there are too many call sites, I follow whatever it opens up.

**Call:** `calls('tests/test_compat.py', 'term_len')`

**Response**: outcome `ok`

```
calls of term_len in tests/test_compat.py count=5
129:    assert term_len(f"a{seq}b") == 2
172:    assert term_len(text) == len(expected)
199:    assert term_len(text) == len(text)
239:    assert term_len(text) == visible
270:    assert term_len(out) <= max(n, 0)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "calls",
   "key": [
    "calls",
    "tests/test_compat.py",
    "term_len"
   ],
   "desc": "list the call sites of `term_len` in `tests/test_compat.py`"
  }
 ],
 "candidates": [
  {
   "call": "calls('tests/test_compat.py', 'term_len')",
   "key": "[\"calls\", [\"tests/test_compat.py\", \"term_len\"]]",
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
     "tests/test_compat.py",
     "term_len"
    ]
   ]
  }
 ],
 "choice": {
  "call": "calls('tests/test_compat.py', 'term_len')",
  "key": "[\"calls\", [\"tests/test_compat.py\", \"term_len\"]]",
  "provenance": "call sites of `term_len` in `tests/test_compat.py` that refer to the module-level binding",
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
  "planned": "[\"calls\", [\"tests/test_compat.py\", \"term_len\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "calls",
   "step": 19,
   "path": "tests/test_compat.py",
   "name": "term_len",
   "lines": [
    129,
    172,
    199,
    239,
    270
   ],
   "count": 5,
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "callers",
  "step": 2,
  "of": 2,
  "candidates": [
   "src/click/_compat.py",
   "src/click/_termui_impl.py",
   "src/click/_textwrap.py",
   "src/click/formatting.py",
   "tests/test_compat.py"
  ],
  "table": [
   [
    "src/click/_compat.py",
    "src/click/_compat.py",
    "out",
    "the module binds the name but never calls it by bare name"
   ],
   [
    "src/click/_termui_impl.py",
    "src/click/_termui_impl.py:268",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/_termui_impl.py",
    "src/click/_termui_impl.py:282",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/_textwrap.py",
    "src/click/_textwrap.py:89",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/_textwrap.py",
    "src/click/_textwrap.py:103",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/_textwrap.py",
    "src/click/_textwrap.py:109",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/_textwrap.py",
    "src/click/_textwrap.py:118",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/_textwrap.py",
    "src/click/_textwrap.py:123",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/_textwrap.py",
    "src/click/_textwrap.py:143",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/_textwrap.py",
    "src/click/_textwrap.py:148",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/_textwrap.py",
    "src/click/_textwrap.py:154",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/formatting.py",
    "src/click/formatting.py:19",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/formatting.py",
    "src/click/formatting.py:93",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/formatting.py",
    "src/click/formatting.py:95",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/formatting.py",
    "src/click/formatting.py:180",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/formatting.py",
    "src/click/formatting.py:182",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/formatting.py",
    "src/click/formatting.py:195",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/formatting.py",
    "src/click/formatting.py:255",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "src/click/formatting.py",
    "src/click/formatting.py:256",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "tests/test_compat.py",
    "tests/test_compat.py:129",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "tests/test_compat.py",
    "tests/test_compat.py:172",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "tests/test_compat.py",
    "tests/test_compat.py:199",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "tests/test_compat.py",
    "tests/test_compat.py:239",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ],
   [
    "tests/test_compat.py",
    "tests/test_compat.py:270",
    "in",
    "bare-name call of the module-level binding, which resolves to the target"
   ]
  ],
  "uncovered": {
   "CALL": []
  },
  "n_in": 23,
  "n_out": 1,
  "n_pending": 0
 }
}
```
</details>

## Final

`term_len` is the def at `src/click/_compat.py:536`. 23 call sites in 4 modules: `src/click/_termui_impl.py:268`, `src/click/_termui_impl.py:282`, `src/click/_textwrap.py:89`, `src/click/_textwrap.py:103`, `src/click/_textwrap.py:109`, `src/click/_textwrap.py:118`, `src/click/_textwrap.py:123`, `src/click/_textwrap.py:143`, `src/click/_textwrap.py:148`, `src/click/_textwrap.py:154` and 13 more. Ruled out along the way: `src/click/_compat.py` (the module binds the name but never calls it by bare name). Looking back, all 19 calls were needed.

**Answer:** `{"final_kind": "callers", "final": ["src/click/_termui_impl.py:268", "src/click/_termui_impl.py:282", "src/click/_textwrap.py:89", "src/click/_textwrap.py:103", "src/click/_textwrap.py:109", "src/click/_textwrap.py:118", "src/click/_textwrap.py:123", "src/click/_textwrap.py:143", "src/click/_textwrap.py:148", "src/click/_textwrap.py:154", "src/click/formatting.py:19", "src/click/formatting.py:93", "src/click/formatting.py:95", "src/click/formatting.py:180", "src/click/formatting.py:182", "src/click/formatting.py:195", "src/click/formatting.py:255", "src/click/formatting.py:256", "tests/test_compat.py:129", "tests/test_compat.py:172", "tests/test_compat.py:199", "tests/test_compat.py:239", "tests/test_compat.py:270"], "steps": [{"op": "resolve", "output": {"kind": "def", "path": "src/click/_compat.py", "line": 536, "name": "term_len", "detail": "def"}}, {"op": "callers", "output": ["src/click/_termui_impl.py:268", "src/click/_termui_impl.py:282", "src/click/_textwrap.py:89", "src/click/_textwrap.py:103", "src/click/_textwrap.py:109", "src/click/_textwrap.py:118", "src/click/_textwrap.py:123", "src/click/_textwrap.py:143", "src/click/_textwrap.py:148", "src/click/_textwrap.py:154", "src/click/formatting.py:19", "src/click/formatting.py:93", "src/click/formatting.py:95", "src/click/formatting.py:180", "src/click/formatting.py:182", "src/click/formatting.py:195", "src/click/formatting.py:255", "src/click/formatting.py:256", "tests/test_compat.py:129", "tests/test_compat.py:172", `  
**Stopped:** certificate after 19 calls