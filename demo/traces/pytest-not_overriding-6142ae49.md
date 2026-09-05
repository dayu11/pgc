# pytest-not_overriding-6142ae49

**Repository:** pytest  
**Chain:** subclasses → not_overriding  
**Seed:** 0, prior 8e41e8743065d192, floor 21

## Task

`Item` is defined at `src/_pytest/nodes.py:654` (class). Among those subclasses, which do not define `reportinfo` themselves? Same format.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N; bindings take effect in source order. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. A class derives from a definition when a base written as a bare name or `module.Name` resolves to it. A call site is `name(...)` where the bare name refers to the module-level binding (not a parameter or local). Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

Starting from the definition of `Item` at `src/_pytest/nodes.py:654`. Then, among its subclasses, the ones that do not define `reportinfo` themselves.

Next I will search the whole tree for classes deriving from `Item`; the search has to be complete before I can call the set final. Very likely nothing turns up. If it caps or it fits under the cap, I follow whatever it opens up.

**Call:** `grep('^\\s*class\\s+\\w+\\s*\\(.*\\bItem\\b', '.')`

**Response**: outcome `mid`

```
doc/en/deprecations.rst:413:    class CustomItem(pytest.Item):
doc/en/deprecations.rst:422:    class CustomItem(pytest.Item):
doc/en/example/nonpython/conftest.py:22:class YamlItem(pytest.Item):
src/_pytest/doctest.py:252:class DoctestItem(Item):
src/_pytest/python.py:1650:class Function(PyobjMixin, nodes.Item):
testing/acceptance_test.py:308:            class MyItem(pytest.Item):
testing/conftest.py:152:        class YamlItem(pytest.Item):
testing/example_scripts/fixtures/custom_item/conftest.py:7:class CustomItem(pytest.Item):
testing/example_scripts/issue88_initial_file_multinodes/conftest.py:16:class MyItem(pytest.Item):
testing/test_collection.py:571:            class SpecialItem(pytest.Item):
testing/test_collection.py:845:        class Item1(pytest.Item):
testing/test_collection.py:849:        class Item2(pytest.Item):
testing/test_junitxml.py:1072:            class MyItem(pytest.Item):
testing/test_junitxml.py:1526:        class FunItem(pytest.Item):
testing/test_junitxml.py:1529:        class NoFunItem(pytest.Item):
testing/test_nodes.py:43:        class SoWrong(nodes.Item, nodes.File):
testing/test_runner.py:152:            class MyItem(pytest.Item):
testing/test_skipping.py:1376:        class MyItem(pytest.Item):
testing/test_skipping.py:1445:        class MyItem(pytest.Item):
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
   "desc": "search `.` for classes deriving from `Item`"
  }
 ],
 "candidates": [
  {
   "call": "grep('^\\\\s*class\\\\s+\\\\w+\\\\s*\\\\(.*\\\\bItem\\\\b', '.')",
   "key": "[\"grep\", [\"^\\\\s*class\\\\s+\\\\w+\\\\s*\\\\(.*\\\\bItem\\\\b\", \".\"]]",
   "v1": [
    449980794518,
    316748520725
   ],
   "v2": [
    449980794518,
    316748520725
   ],
   "p_cap": [
    1,
    19
   ],
   "forecast": {
    "zero": [
     17,
     19
    ],
    "mid": [
     1,
     19
    ],
    "cap": [
     1,
     19
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
  "call": "grep('^\\\\s*class\\\\s+\\\\w+\\\\s*\\\\(.*\\\\bItem\\\\b', '.')",
  "key": "[\"grep\", [\"^\\\\s*class\\\\s+\\\\w+\\\\s*\\\\(.*\\\\bItem\\\\b\", \".\"]]",
  "provenance": "subclass lines naming `Item` under `.` (derived)",
  "v2": [
   449980794518,
   316748520725
  ]
 },
 "forecast": {
  "zero": [
   17,
   19
  ],
  "mid": [
   1,
   19
  ],
  "cap": [
   1,
   19
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
    17,
    19
   ]
  }
 ],
 "adherence": null,
 "facts": [
  {
   "kind": "grep",
   "step": 1,
   "pattern": "^\\s*class\\s+\\w+\\s*\\(.*\\bItem\\b",
   "scope": ".",
   "hits": [
    [
     "doc/en/deprecations.rst",
     413
    ],
    [
     "doc/en/deprecations.rst",
     422
    ],
    [
     "doc/en/example/nonpython/conftest.py",
     22
    ],
    [
     "src/_pytest/doctest.py",
     252
    ],
    [
     "src/_pytest/python.py",
     1650
    ],
    [
     "testing/acceptance_test.py",
     308
    ],
    [
     "testing/conftest.py",
     152
    ],
    [
     "testing/example_scripts/fixtures/custom_item/conftest.py",
     7
    ],
    [
     "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
     16
    ],
    [
     "testing/test_collection.py",
     571
    ],
    [
     "testing/test_collection.py",
     845
    ],
    [
     "testing/test_collection.py",
     849
    ],
    [
     "testing/test_junitxml.py",
     1072
    ],
    [
     "testing/test_junitxml.py",
     1526
    ],
    [
     "testing/test_junitxml.py",
     1529
    ],
    [
     "testing/test_nodes.py",
     43
    ],
    [
     "testing/test_runner.py",
     152
    ],
    [
     "testing/test_skipping.py",
     1376
    ],
    [
     "testing/test_skipping.py",
     1445
    ]
   ],
   "capped": false
  }
 ],
 "goal_state": {
  "phase": "subclasses",
  "step": 1,
  "of": 2,
  "candidates": [
   "doc/en/example/nonpython/conftest.py",
   "src/_pytest/doctest.py",
   "src/_pytest/python.py",
   "testing/acceptance_test.py",
   "testing/conftest.py",
   "testing/example_scripts/fixtures/custom_item/conftest.py",
   "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
   "testing/test_collection.py",
   "testing/test_junitxml.py",
   "testing/test_nodes.py",
   "testing/test_runner.py",
   "testing/test_skipping.py"
  ],
  "table": [
   [
    "doc/en/example/nonpython/conftest.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/_pytest/doctest.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "src/_pytest/python.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "testing/acceptance_test.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "testing/conftest.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "testing/example_scripts/fixtures/custom_item/conftest.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "testing/test_collection.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "testing/test_junitxml.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "testing/test_nodes.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "testing/test_runner.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "testing/test_skipping.py",
    null,
    "pending",
    "not yet examined"
   ]
  ],
  "uncovered": {
   "SUBCLASS": []
  },
  "n_in": 0,
  "n_out": 0,
  "n_pending": 12
 }
}
```
</details>

## Step 2

Huh: 19 matching lines anywhere for classes deriving from `Item`, in `doc/en/deprecations.rst`, `doc/en/example/nonpython/conftest.py`, `src/_pytest/doctest.py`, `src/_pytest/python.py` and 9 more files, and the search was under the cap, so that is the complete set there.

I'll look at `testing/example_scripts/issue88_initial_file_multinodes/conftest.py`'s top-level names for `Item`; the outline lists each class with its bases. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `doc/en/example/nonpython/conftest.py`'s top-level names for `Item`.

**Call:** `symbols('testing/example_scripts/issue88_initial_file_multinodes/conftest.py', 'Item')`

**Response**: outcome `ok`

```
module testing/example_scripts/issue88_initial_file_multinodes/conftest.py lines=19 dynamic=no all=none
16 class MyItem (pytest.Item)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "doc/en/example/nonpython/conftest.py",
    "Item"
   ],
   "desc": "look at the classes in `doc/en/example/nonpython/conftest.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/doctest.py",
    "Item"
   ],
   "desc": "look at the classes in `src/_pytest/doctest.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "Item"
   ],
   "desc": "look at the classes in `src/_pytest/python.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/acceptance_test.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/conftest.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/conftest.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/example_scripts/fixtures/custom_item/conftest.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/example_scripts/fixtures/custom_item/conftest.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/example_scripts/issue88_initial_file_multinodes/conftest.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_collection.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_collection.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_junitxml.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_junitxml.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_nodes.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_nodes.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_runner.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_runner.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_skipping.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_skipping.py` that derive from `Item`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('doc/en/example/nonpython/conftest.py', 'Item')",
   "key": "[\"symbols\", [\"doc/en/example/nonpython/conftest.py\", \"Item\"]]",
   "v1": [
    7132007,
    393550
   ],
   "v2": [
    3569939,
    196775
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
     "doc/en/example/nonpython/conftest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/doctest.py', 'Item')",
   "key": "[\"symbols\", [\"src/_pytest/doctest.py\", \"Item\"]]",
   "v1": [
    7132007,
    393550
   ],
   "v2": [
    3569939,
    196775
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
     "src/_pytest/doctest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/python.py', 'Item')",
   "key": "[\"symbols\", [\"src/_pytest/python.py\", \"Item\"]]",
   "v1": [
    7132007,
    393550
   ],
   "v2": [
    3569939,
    196775
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
     "src/_pytest/python.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/acceptance_test.py', 'Item')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"Item\"]]",
   "v1": [
    7132007,
    393550
   ],
   "v2": [
    3569939,
    196775
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
     "testing/acceptance_test.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/conftest.py', 'Item')",
   "key": "[\"symbols\", [\"testing/conftest.py\", \"Item\"]]",
   "v1": [
    7132007,
    393550
   ],
   "v2": [
    3569939,
    196775
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
     "testing/conftest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/example_scripts/fixtures/custom_item/conftest.py', 'Item')",
   "key": "[\"symbols\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\", \"Item\"]]",
   "v1": [
    7132007,
    393550
   ],
   "v2": [
    3569939,
    196775
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
     "testing/example_scripts/fixtures/custom_item/conftest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/example_scripts/issue88_initial_file_multinodes/conftest.py', 'Item')",
   "key": "[\"symbols\", [\"testing/example_scripts/issue88_initial_file_multinodes/conftest.py\", \"Item\"]]",
   "v1": [
    7132007,
    393550
   ],
   "v2": [
    3569939,
    196775
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
     "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_collection.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_collection.py\", \"Item\"]]",
   "v1": [
    7132007,
    393550
   ],

```
</details>

## Step 3

The test module `testing/example_scripts/issue88_initial_file_multinodes/conftest.py` has `class MyItem(pytest.Item)` at line 16. Nothing binds `Item` at module level there.

Tally: 0 subclasses confirmed, 0 ruled out, 12 pending. The search itself is complete; what is left is checking the candidates.

I'll look at `doc/en/example/nonpython/conftest.py`'s top-level names for `Item`; the outline lists each class with its bases. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `testing/example_scripts/issue88_initial_file_multinodes/conftest.py`'s top-level names for `pytest`.

**Call:** `symbols('doc/en/example/nonpython/conftest.py', 'Item')`

**Response**: outcome `ok`

```
module doc/en/example/nonpython/conftest.py lines=51 dynamic=no all=none
22 class YamlItem (pytest.Item)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "doc/en/example/nonpython/conftest.py",
    "Item"
   ],
   "desc": "look at the classes in `doc/en/example/nonpython/conftest.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/doctest.py",
    "Item"
   ],
   "desc": "look at the classes in `src/_pytest/doctest.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "Item"
   ],
   "desc": "look at the classes in `src/_pytest/python.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/acceptance_test.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/conftest.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/conftest.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/example_scripts/fixtures/custom_item/conftest.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/example_scripts/fixtures/custom_item/conftest.py` that derive from `Item`"
  },
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
    "pytest"
   ],
   "desc": "check the top-level names of `testing/example_scripts/issue88_initial_file_multinodes/conftest.py` for `pytest`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_collection.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_collection.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_junitxml.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_junitxml.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_nodes.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_nodes.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_runner.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_runner.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_skipping.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_skipping.py` that derive from `Item`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('doc/en/example/nonpython/conftest.py', 'Item')",
   "key": "[\"symbols\", [\"doc/en/example/nonpython/conftest.py\", \"Item\"]]",
   "v1": [
    12837966883,
    658015600
   ],
   "v2": [
    12837966883,
    658015600
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
     "doc/en/example/nonpython/conftest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/doctest.py', 'Item')",
   "key": "[\"symbols\", [\"src/_pytest/doctest.py\", \"Item\"]]",
   "v1": [
    12837966883,
    658015600
   ],
   "v2": [
    12837966883,
    658015600
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
     "src/_pytest/doctest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/python.py', 'Item')",
   "key": "[\"symbols\", [\"src/_pytest/python.py\", \"Item\"]]",
   "v1": [
    12837966883,
    658015600
   ],
   "v2": [
    12837966883,
    658015600
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
     "src/_pytest/python.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/acceptance_test.py', 'Item')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"Item\"]]",
   "v1": [
    12837966883,
    658015600
   ],
   "v2": [
    12837966883,
    658015600
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
     "testing/acceptance_test.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/conftest.py', 'Item')",
   "key": "[\"symbols\", [\"testing/conftest.py\", \"Item\"]]",
   "v1": [
    12837966883,
    658015600
   ],
   "v2": [
    12837966883,
    658015600
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
     "testing/conftest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/example_scripts/fixtures/custom_item/conftest.py', 'Item')",
   "key": "[\"symbols\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\", \"Item\"]]",
   "v1": [
    12837966883,
    658015600
   ],
   "v2": [
    12837966883,
    658015600
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
     "testing/example_scripts/fixtures/custom_item/conftest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/example_scripts/issue88_initial_file_multinodes/conftest.py', 'pytest')",
   "key": "[\"symbols\", [\"testing/example_scripts/issue88_initial_file_multinodes/conftest.py\", \"pytest\"]]",
   "v1": [
    12824806571,
    658015600
   ],
   "v2": [
    12837966883,
    658015600
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     3,
     100
    ],
    "reexport": [
     23,
     25
    ],
    "star": [
     1,
     100
    ],
    "none": [
     1,
     25
    ]
   },
   "serves": [
    [
     "bindings",
     "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
     "pytest"
    ]
 
```
</details>

## Step 4

`doc/en/example/nonpython/conftest.py` has `class YamlItem(pytest.Item)` at line 22. Nothing binds `Item` at module level there.

Tally: 0 subclasses confirmed, 0 ruled out, 12 pending. The search itself is complete; what is left is checking the candidates.

Still open: check the top-level names of `doc/en/example/nonpython/conftest.py` for `pytest`; look at the classes in `src/_pytest/doctest.py` that derive from `Item`; look at the classes in `src/_pytest/python.py` that derive from `Item`; and 9 more.

I'll look at `testing/example_scripts/issue88_initial_file_multinodes/conftest.py`'s top-level names for `pytest`; that settles what the name means there. Almost certainly it is re-exported from somewhere else. If the name is not bound there or it is defined right there, I will look at `doc/en/example/nonpython/conftest.py`'s top-level names for `pytest`.

**Call:** `symbols('testing/example_scripts/issue88_initial_file_multinodes/conftest.py', 'pytest')`

**Response**: outcome `reexport`

```
module testing/example_scripts/issue88_initial_file_multinodes/conftest.py lines=19 dynamic=no all=none
4 import pytest <- pytest
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "doc/en/example/nonpython/conftest.py",
    "pytest"
   ],
   "desc": "check the top-level names of `doc/en/example/nonpython/conftest.py` for `pytest`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/doctest.py",
    "Item"
   ],
   "desc": "look at the classes in `src/_pytest/doctest.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "Item"
   ],
   "desc": "look at the classes in `src/_pytest/python.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/acceptance_test.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/conftest.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/conftest.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/example_scripts/fixtures/custom_item/conftest.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/example_scripts/fixtures/custom_item/conftest.py` that derive from `Item`"
  },
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
    "pytest"
   ],
   "desc": "check the top-level names of `testing/example_scripts/issue88_initial_file_multinodes/conftest.py` for `pytest`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_collection.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_collection.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_junitxml.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_junitxml.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_nodes.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_nodes.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_runner.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_runner.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_skipping.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_skipping.py` that derive from `Item`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('doc/en/example/nonpython/conftest.py', 'pytest')",
   "key": "[\"symbols\", [\"doc/en/example/nonpython/conftest.py\", \"pytest\"]]",
   "v1": [
    274761155,
    13160312
   ],
   "v2": [
    274761155,
    13160312
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     3,
     100
    ],
    "reexport": [
     23,
     25
    ],
    "star": [
     1,
     100
    ],
    "none": [
     1,
     25
    ]
   },
   "serves": [
    [
     "bindings",
     "doc/en/example/nonpython/conftest.py",
     "pytest"
    ]
   ]
  },
  {
   "call": "symbols('testing/example_scripts/issue88_initial_file_multinodes/conftest.py', 'pytest')",
   "key": "[\"symbols\", [\"testing/example_scripts/issue88_initial_file_multinodes/conftest.py\", \"pytest\"]]",
   "v1": [
    274761155,
    13160312
   ],
   "v2": [
    274761155,
    13160312
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     3,
     100
    ],
    "reexport": [
     23,
     25
    ],
    "star": [
     1,
     100
    ],
    "none": [
     1,
     25
    ]
   },
   "serves": [
    [
     "bindings",
     "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
     "pytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/doctest.py', 'Item')",
   "key": "[\"symbols\", [\"src/_pytest/doctest.py\", \"Item\"]]",
   "v1": [
    6875609031,
    329007800
   ],
   "v2": [
    6875609031,
    329007800
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
     "src/_pytest/doctest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/python.py', 'Item')",
   "key": "[\"symbols\", [\"src/_pytest/python.py\", \"Item\"]]",
   "v1": [
    6875609031,
    329007800
   ],
   "v2": [
    6875609031,
    329007800
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
     "src/_pytest/python.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/acceptance_test.py', 'Item')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"Item\"]]",
   "v1": [
    6875609031,
    329007800
   ],
   "v2": [
    6875609031,
    329007800
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
     "testing/acceptance_test.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/conftest.py', 'Item')",
   "key": "[\"symbols\", [\"testing/conftest.py\", \"Item\"]]",
   "v1": [
    6875609031,
    329007800
   ],
   "v2": [
    6875609031,
    329007800
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
     "testing/conftest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/example_scripts/fixtures/custom_item/conftest.py', 'Item')",
   "key": "[\"symbols\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\", \"Item\"]]",
   "v1": [
    6875609031,
    329007800
   ],
   "v2": [
    6875609031,
    329007800
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
     "testing/examp
```
</details>

## Step 5

In the test module `testing/example_scripts/issue88_initial_file_multinodes/conftest.py`, `pytest` is a module import (`import pytest`), not a definition.

Tally: 0 subclasses confirmed, 0 ruled out, 12 pending. The search itself is complete; what is left is checking the candidates.

Let me look at `doc/en/example/nonpython/conftest.py`'s top-level names for `pytest`; that settles what the name means there. Almost certainly it is re-exported from somewhere else. If the name is not bound there or it is defined right there, I will list `./` to see what lives there.

**Call:** `symbols('doc/en/example/nonpython/conftest.py', 'pytest')`

**Response**: outcome `reexport`

```
module doc/en/example/nonpython/conftest.py lines=51 dynamic=no all=none
4 import pytest <- pytest
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "doc/en/example/nonpython/conftest.py",
    "pytest"
   ],
   "desc": "check the top-level names of `doc/en/example/nonpython/conftest.py` for `pytest`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/doctest.py",
    "Item"
   ],
   "desc": "look at the classes in `src/_pytest/doctest.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "Item"
   ],
   "desc": "look at the classes in `src/_pytest/python.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/acceptance_test.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/conftest.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/conftest.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/example_scripts/fixtures/custom_item/conftest.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/example_scripts/fixtures/custom_item/conftest.py` that derive from `Item`"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
    "pytest"
   ],
   "desc": "find where `pytest` (imported by `testing/example_scripts/issue88_initial_file_multinodes/conftest.py`) lives"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_collection.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_collection.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_junitxml.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_junitxml.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_nodes.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_nodes.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_runner.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_runner.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_skipping.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_skipping.py` that derive from `Item`"
  }
 ],
 "candidates": [
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    7838472293,
    394809360
   ],
   "v2": [
    7838472293,
    394809360
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
     "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
     "pytest"
    ]
   ]
  },
  {
   "call": "symbols('doc/en/example/nonpython/conftest.py', 'pytest')",
   "key": "[\"symbols\", [\"doc/en/example/nonpython/conftest.py\", \"pytest\"]]",
   "v1": [
    2634757951,
    131603120
   ],
   "v2": [
    7838472293,
    394809360
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     3,
     100
    ],
    "reexport": [
     23,
     25
    ],
    "star": [
     1,
     100
    ],
    "none": [
     1,
     25
    ]
   },
   "serves": [
    [
     "bindings",
     "doc/en/example/nonpython/conftest.py",
     "pytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/doctest.py', 'Item')",
   "key": "[\"symbols\", [\"src/_pytest/doctest.py\", \"Item\"]]",
   "v1": [
    13186950067,
    658015600
   ],
   "v2": [
    39231842401,
    1974046800
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
     "src/_pytest/doctest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/python.py', 'Item')",
   "key": "[\"symbols\", [\"src/_pytest/python.py\", \"Item\"]]",
   "v1": [
    13186950067,
    658015600
   ],
   "v2": [
    39231842401,
    1974046800
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
     "src/_pytest/python.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/acceptance_test.py', 'Item')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"Item\"]]",
   "v1": [
    13186950067,
    658015600
   ],
   "v2": [
    39231842401,
    1974046800
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
     "testing/acceptance_test.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/conftest.py', 'Item')",
   "key": "[\"symbols\", [\"testing/conftest.py\", \"Item\"]]",
   "v1": [
    13186950067,
    658015600
   ],
   "v2": [
    39231842401,
    1974046800
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
     "testing/conftest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/example_scripts/fixtures/custom_item/conftest.py', 'Item')",
   "key": "[\"symbols\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\", \"Item\"]]",
   "v1": [
    13186950067,
    658015600
   ],
   "v2": [
    39231842401,
    1974046800
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
     "testing/example_scripts/fixtures/custom_item/conftest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_collection.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_collection.py\", \"Item\"]]",
   "
```
</details>

## Step 6

In `doc/en/example/nonpython/conftest.py`, `pytest` is a module import (`import pytest`), not a definition.

Tally: 0 subclasses confirmed, 0 ruled out, 12 pending. The search itself is complete; what is left is checking the candidates.

Next I will list `./` to see what lives there; the listing settles whether the import is a module, a package, or not here at all. Very likely the listing fits. If the listing is too long, I will look at `src/_pytest/doctest.py`'s top-level names for `Item`.

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
    "doc/en/example/nonpython/conftest.py",
    "pytest"
   ],
   "desc": "find where `pytest` (imported by `doc/en/example/nonpython/conftest.py`) lives"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/doctest.py",
    "Item"
   ],
   "desc": "look at the classes in `src/_pytest/doctest.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "Item"
   ],
   "desc": "look at the classes in `src/_pytest/python.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/acceptance_test.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/conftest.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/conftest.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/example_scripts/fixtures/custom_item/conftest.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/example_scripts/fixtures/custom_item/conftest.py` that derive from `Item`"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
    "pytest"
   ],
   "desc": "find where `pytest` (imported by `testing/example_scripts/issue88_initial_file_multinodes/conftest.py`) lives"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_collection.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_collection.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_junitxml.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_junitxml.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_nodes.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_nodes.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_runner.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_runner.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_skipping.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_skipping.py` that derive from `Item`"
  }
 ],
 "candidates": [
  {
   "call": "ls('.')",
   "key": "[\"ls\", [\".\"]]",
   "v1": [
    2105054,
    118065
   ],
   "v2": [
    21074153,
    1180650
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
     "doc/en/example/nonpython/conftest.py",
     "pytest"
    ],
    [
     "module_path",
     "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
     "pytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/doctest.py', 'Item')",
   "key": "[\"symbols\", [\"src/_pytest/doctest.py\", \"Item\"]]",
   "v1": [
    7549451,
    393550
   ],
   "v2": [
    21074153,
    1180650
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
     "src/_pytest/doctest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/python.py', 'Item')",
   "key": "[\"symbols\", [\"src/_pytest/python.py\", \"Item\"]]",
   "v1": [
    7549451,
    393550
   ],
   "v2": [
    21074153,
    1180650
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
     "src/_pytest/python.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/acceptance_test.py', 'Item')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"Item\"]]",
   "v1": [
    7549451,
    393550
   ],
   "v2": [
    21074153,
    1180650
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
     "testing/acceptance_test.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/conftest.py', 'Item')",
   "key": "[\"symbols\", [\"testing/conftest.py\", \"Item\"]]",
   "v1": [
    7549451,
    393550
   ],
   "v2": [
    21074153,
    1180650
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
     "testing/conftest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/example_scripts/fixtures/custom_item/conftest.py', 'Item')",
   "key": "[\"symbols\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\", \"Item\"]]",
   "v1": [
    7549451,
    393550
   ],
   "v2": [
    21074153,
    1180650
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
     "testing/example_scripts/fixtures/custom_item/conftest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_collection.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_collection.py\", \"Item\"]]",
   "v1": [
    7549451,
    393550
   ],
   "v2": [
    21074153,
    1180650
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
     "testing/test_collection.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_junitxml.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_junitxml.py\", \"Item\"]]",
   "v1": [
    7549451,
    393550
   ],
   "v2": [
    21074153,
    1180650
   ],
   "p_cap": [
    1,
    50
   
```
</details>

## Step 7

`./` has 21 entries: there is no `pytest` here. That changes the plan.

Next I will outline `src/pytest.py` directly, which both checks that the file exists and shows me `Item`; if `pytest` is a plain module that is where it has to be. Probably the file is not there, but a miss costs one call and rules that location out; if so, I will list `src/` to see what lives there.

**Call:** `symbols('src/pytest.py', 'Item')`

**Response**: outcome `missing`

```
error: not a python file: src/pytest.py
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "doc/en/example/nonpython/conftest.py",
    "pytest"
   ],
   "desc": "find where `pytest` (imported by `doc/en/example/nonpython/conftest.py`) lives"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/doctest.py",
    "Item"
   ],
   "desc": "look at the classes in `src/_pytest/doctest.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "Item"
   ],
   "desc": "look at the classes in `src/_pytest/python.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/acceptance_test.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/conftest.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/conftest.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/example_scripts/fixtures/custom_item/conftest.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/example_scripts/fixtures/custom_item/conftest.py` that derive from `Item`"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
    "pytest"
   ],
   "desc": "find where `pytest` (imported by `testing/example_scripts/issue88_initial_file_multinodes/conftest.py`) lives"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_collection.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_collection.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_junitxml.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_junitxml.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_nodes.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_nodes.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_runner.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_runner.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_skipping.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_skipping.py` that derive from `Item`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/pytest.py', 'Item')",
   "key": "[\"symbols\", [\"src/pytest.py\", \"Item\"]]",
   "v1": [
    11313090279604459,
    604224403937440
   ],
   "v2": [
    54871472459903399,
    3021122019687200
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
     "doc/en/example/nonpython/conftest.py",
     "pytest"
    ],
    [
     "module_path",
     "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
     "pytest"
    ]
   ]
  },
  {
   "call": "ls('src')",
   "key": "[\"ls\", [\"src\"]]",
   "v1": [
    719433,
    39355
   ],
   "v2": [
    55206662921576007,
    3021122019687200
   ],
   "p_cap": [
    1,
    17
   ],
   "forecast": {
    "complete": [
     16,
     17
    ],
    "cap": [
     1,
     17
    ]
   },
   "serves": [
    [
     "module_path",
     "doc/en/example/nonpython/conftest.py",
     "pytest"
    ],
    [
     "module_path",
     "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
     "pytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/doctest.py', 'Item')",
   "key": "[\"symbols\", [\"src/_pytest/doctest.py\", \"Item\"]]",
   "v1": [
    7549451,
    393550
   ],
   "v2": [
    7202201,
    393550
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
     "src/_pytest/doctest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/python.py', 'Item')",
   "key": "[\"symbols\", [\"src/_pytest/python.py\", \"Item\"]]",
   "v1": [
    7549451,
    393550
   ],
   "v2": [
    7202201,
    393550
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
     "src/_pytest/python.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/acceptance_test.py', 'Item')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"Item\"]]",
   "v1": [
    7549451,
    393550
   ],
   "v2": [
    7202201,
    393550
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
     "testing/acceptance_test.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/conftest.py', 'Item')",
   "key": "[\"symbols\", [\"testing/conftest.py\", \"Item\"]]",
   "v1": [
    7549451,
    393550
   ],
   "v2": [
    7202201,
    393550
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
     "testing/conftest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/example_scripts/fixtures/custom_item/conftest.py', 'Item')",
   "key": "[\"symbols\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\", \"Item\"]]",
   "v1": [
    7549451,
    393550
   ],
   "v2": [
    7202201,
    393550
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
     "tes
```
</details>

## Step 8

There is no `src/pytest.py`, so `pytest` is either a package (`src/pytest/__init__.py`) or not in this repository at all.

Still open: find where `pytest` (imported by `doc/en/example/nonpython/conftest.py`) lives; look at the classes in `src/_pytest/doctest.py` that derive from `Item`; look at the classes in `src/_pytest/python.py` that derive from `Item`; and 9 more.

I'll list `src/` to see what lives there; the listing settles whether the import is a module, a package, or not here at all. Almost certainly the listing fits. If the listing is too long, I will look at `src/_pytest/doctest.py`'s top-level names for `Item`.

**Call:** `ls('src')`

**Response**: outcome `complete`

```
_pytest/
py.py
pytest/
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "doc/en/example/nonpython/conftest.py",
    "pytest"
   ],
   "desc": "find where `pytest` (imported by `doc/en/example/nonpython/conftest.py`) lives"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/doctest.py",
    "Item"
   ],
   "desc": "look at the classes in `src/_pytest/doctest.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "Item"
   ],
   "desc": "look at the classes in `src/_pytest/python.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/acceptance_test.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/conftest.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/conftest.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/example_scripts/fixtures/custom_item/conftest.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/example_scripts/fixtures/custom_item/conftest.py` that derive from `Item`"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
    "pytest"
   ],
   "desc": "find where `pytest` (imported by `testing/example_scripts/issue88_initial_file_multinodes/conftest.py`) lives"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_collection.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_collection.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_junitxml.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_junitxml.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_nodes.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_nodes.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_runner.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_runner.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_skipping.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_skipping.py` that derive from `Item`"
  }
 ],
 "candidates": [
  {
   "call": "ls('src')",
   "key": "[\"ls\", [\"src\"]]",
   "v1": [
    56477951,
    2636785
   ],
   "v2": [
    565306867,
    26367850
   ],
   "p_cap": [
    1,
    17
   ],
   "forecast": {
    "complete": [
     16,
     17
    ],
    "cap": [
     1,
     17
    ]
   },
   "serves": [
    [
     "module_path",
     "doc/en/example/nonpython/conftest.py",
     "pytest"
    ],
    [
     "module_path",
     "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
     "pytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/doctest.py', 'Item')",
   "key": "[\"symbols\", [\"src/_pytest/doctest.py\", \"Item\"]]",
   "v1": [
    588572617,
    26367850
   ],
   "v2": [
    565306867,
    26367850
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
     "src/_pytest/doctest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/python.py', 'Item')",
   "key": "[\"symbols\", [\"src/_pytest/python.py\", \"Item\"]]",
   "v1": [
    588572617,
    26367850
   ],
   "v2": [
    565306867,
    26367850
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
     "src/_pytest/python.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/acceptance_test.py', 'Item')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"Item\"]]",
   "v1": [
    588572617,
    26367850
   ],
   "v2": [
    565306867,
    26367850
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
     "testing/acceptance_test.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/conftest.py', 'Item')",
   "key": "[\"symbols\", [\"testing/conftest.py\", \"Item\"]]",
   "v1": [
    588572617,
    26367850
   ],
   "v2": [
    565306867,
    26367850
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
     "testing/conftest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/example_scripts/fixtures/custom_item/conftest.py', 'Item')",
   "key": "[\"symbols\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\", \"Item\"]]",
   "v1": [
    588572617,
    26367850
   ],
   "v2": [
    565306867,
    26367850
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
     "testing/example_scripts/fixtures/custom_item/conftest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_collection.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_collection.py\", \"Item\"]]",
   "v1": [
    588572617,
    26367850
   ],
   "v2": [
    565306867,
    26367850
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
     "testing/test_collection.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_junitxml.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_junitxml.py\", \"Item\"]]",
   "v1": [
    588572617,
    26367850
   ],
   "v2": [
    5653068
```
</details>

## Step 9

`src/` has 3 entries: `pytest/` is there, so `pytest` is a package. That changes the plan.

Tally: 0 subclasses confirmed, 0 ruled out, 12 pending. The search itself is complete; what is left is checking the candidates.

Let me outline `src/pytest/__init__.py` directly, which both checks that the file exists and shows me `Item`; if `pytest` is a plain module that is where it has to be. Probably it is re-exported from somewhere else. If the name is not bound there or it is defined right there, I will look at `src/_pytest/doctest.py`'s top-level names for `Item`; if the file does not exist, I will list `src/pytest/` to see what lives there. I could look at `src/_pytest/doctest.py`'s top-level names for `Item` instead, but it settles less.

**Call:** `symbols('src/pytest/__init__.py', 'Item')`

**Response**: outcome `reexport`

```
module src/pytest/__init__.py lines=191 dynamic=no all=static@100
49 from Item <- _pytest.nodes Item
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "doc/en/example/nonpython/conftest.py",
    "pytest"
   ],
   "desc": "find where `pytest` (imported by `doc/en/example/nonpython/conftest.py`) lives"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/doctest.py",
    "Item"
   ],
   "desc": "look at the classes in `src/_pytest/doctest.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "Item"
   ],
   "desc": "look at the classes in `src/_pytest/python.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/acceptance_test.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/conftest.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/conftest.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/example_scripts/fixtures/custom_item/conftest.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/example_scripts/fixtures/custom_item/conftest.py` that derive from `Item`"
  },
  {
   "kind": "module_path",
   "key": [
    "module_path",
    "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
    "pytest"
   ],
   "desc": "find where `pytest` (imported by `testing/example_scripts/issue88_initial_file_multinodes/conftest.py`) lives"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_collection.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_collection.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_junitxml.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_junitxml.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_nodes.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_nodes.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_runner.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_runner.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_skipping.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_skipping.py` that derive from `Item`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/pytest/__init__.py', 'Item')",
   "key": "[\"symbols\", [\"src/pytest/__init__.py\", \"Item\"]]",
   "v1": [
    4038192083,
    226763510
   ],
   "v2": [
    31296646257429,
    1757417202500
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     147,
     1675
    ],
    "reexport": [
     1078,
     1675
    ],
    "star": [
     49,
     3350
    ],
    "none": [
     392,
     1675
    ],
    "missing": [
     1,
     50
    ]
   },
   "serves": [
    [
     "module_path",
     "doc/en/example/nonpython/conftest.py",
     "pytest"
    ],
    [
     "module_path",
     "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
     "pytest"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/doctest.py', 'Item')",
   "key": "[\"symbols\", [\"src/_pytest/doctest.py\", \"Item\"]]",
   "v1": [
    588572617,
    26367850
   ],
   "v2": [
    10106818383,
    566908775
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
     "src/_pytest/doctest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/python.py', 'Item')",
   "key": "[\"symbols\", [\"src/_pytest/python.py\", \"Item\"]]",
   "v1": [
    588572617,
    26367850
   ],
   "v2": [
    10106818383,
    566908775
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
     "src/_pytest/python.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/acceptance_test.py', 'Item')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"Item\"]]",
   "v1": [
    588572617,
    26367850
   ],
   "v2": [
    10106818383,
    566908775
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
     "testing/acceptance_test.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/conftest.py', 'Item')",
   "key": "[\"symbols\", [\"testing/conftest.py\", \"Item\"]]",
   "v1": [
    588572617,
    26367850
   ],
   "v2": [
    10106818383,
    566908775
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
     "testing/conftest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/example_scripts/fixtures/custom_item/conftest.py', 'Item')",
   "key": "[\"symbols\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\", \"Item\"]]",
   "v1": [
    588572617,
    26367850
   ],
   "v2": [
    10106818383,
    566908775
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
     "testing/example_scripts/fixtures/custom_item/conftest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_collection.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_collection.py\", \"Item\"]]",
   "v1": [
    588572617,
    26367850
   ],
   "v2": [
    10106818383,
    566908775
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
     "testing/test_collection.py",

```
</details>

## Step 10

The package `src/pytest` does not define `Item` itself; line 49 imports it from `_pytest.nodes`.

Tally: 0 subclasses confirmed, 0 ruled out, 12 pending. The search itself is complete; what is left is checking the candidates.

Let me look at `src/_pytest/doctest.py`'s top-level names for `Item`; the outline lists each class with its bases. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `src/_pytest/nodes.py`'s top-level names for `Item`.

**Call:** `symbols('src/_pytest/doctest.py', 'Item')`

**Response**: outcome `ok`

```
module src/_pytest/doctest.py lines=748 dynamic=no all=none
38 from Item <- _pytest.nodes Item
252 class DoctestItem (Item)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/_pytest/nodes.py",
    "Item"
   ],
   "desc": "check the top-level names of `src/_pytest/nodes.py` for `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/doctest.py",
    "Item"
   ],
   "desc": "look at the classes in `src/_pytest/doctest.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "Item"
   ],
   "desc": "look at the classes in `src/_pytest/python.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/acceptance_test.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/conftest.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/conftest.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/example_scripts/fixtures/custom_item/conftest.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/example_scripts/fixtures/custom_item/conftest.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_collection.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_collection.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_junitxml.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_junitxml.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_nodes.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_nodes.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_runner.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_runner.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_skipping.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_skipping.py` that derive from `Item`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/doctest.py', 'Item')",
   "key": "[\"symbols\", [\"src/_pytest/doctest.py\", \"Item\"]]",
   "v1": [
    1253524465571,
    77645840800
   ],
   "v2": [
    1253524465571,
    77645840800
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
     "src/_pytest/doctest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/nodes.py', 'Item')",
   "key": "[\"symbols\", [\"src/_pytest/nodes.py\", \"Item\"]]",
   "v1": [
    250394309751,
    15529168160
   ],
   "v2": [
    1253524465571,
    77645840800
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     441,
     472
    ],
    "reexport": [
     1,
     59
    ],
    "star": [
     1,
     472
    ],
    "none": [
     11,
     236
    ]
   },
   "serves": [
    [
     "bindings",
     "src/_pytest/nodes.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/python.py', 'Item')",
   "key": "[\"symbols\", [\"src/_pytest/python.py\", \"Item\"]]",
   "v1": [
    1253524465571,
    77645840800
   ],
   "v2": [
    1253524465571,
    77645840800
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
     "src/_pytest/python.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/acceptance_test.py', 'Item')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"Item\"]]",
   "v1": [
    1253524465571,
    77645840800
   ],
   "v2": [
    1253524465571,
    77645840800
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
     "testing/acceptance_test.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/conftest.py', 'Item')",
   "key": "[\"symbols\", [\"testing/conftest.py\", \"Item\"]]",
   "v1": [
    1253524465571,
    77645840800
   ],
   "v2": [
    1253524465571,
    77645840800
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
     "testing/conftest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/example_scripts/fixtures/custom_item/conftest.py', 'Item')",
   "key": "[\"symbols\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\", \"Item\"]]",
   "v1": [
    1253524465571,
    77645840800
   ],
   "v2": [
    1253524465571,
    77645840800
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
     "testing/example_scripts/fixtures/custom_item/conftest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_collection.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_collection.py\", \"Item\"]]",
   "v1": [
    1253524465571,
    77645840800
   ],
   "v2": [
    1253524465571,
    77645840800
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
     "testing/test_collection.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_junitxml.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_junitxml.py\", \"Item\"]]",
   "v1": [
    1253524465571,
    77645840800
   ],
   "v2": [
    1253524465571,
    77645840800
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
     "testing/test_junitxm
```
</details>

## Step 11

`src/_pytest/doctest.py` has `class DoctestItem(Item)` at line 252. It gets `Item` from `_pytest.nodes` (line 38), which is what the base name resolves through.

Tally: 0 subclasses confirmed, 0 ruled out, 12 pending. The search itself is complete; what is left is checking the candidates.

I'll look at `src/_pytest/nodes.py`'s top-level names for `Item`; that settles what the name means there. Almost certainly it is defined right there. If the name is not bound there, I will look at `src/_pytest/python.py`'s top-level names for `Item`.

**Call:** `symbols('src/_pytest/nodes.py', 'Item')`

**Response**: outcome `def`

```
module src/_pytest/nodes.py lines=772 dynamic=no all=none
654 class Item (Node,abc.ABC)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/_pytest/nodes.py",
    "Item"
   ],
   "desc": "check the top-level names of `src/_pytest/nodes.py` for `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "Item"
   ],
   "desc": "look at the classes in `src/_pytest/python.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/acceptance_test.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/conftest.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/conftest.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/example_scripts/fixtures/custom_item/conftest.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/example_scripts/fixtures/custom_item/conftest.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_collection.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_collection.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_junitxml.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_junitxml.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_nodes.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_nodes.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_runner.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_runner.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_skipping.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_skipping.py` that derive from `Item`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/nodes.py', 'Item')",
   "key": "[\"symbols\", [\"src/_pytest/nodes.py\", \"Item\"]]",
   "v1": [
    1134841254067,
    77645840800
   ],
   "v2": [
    1136394170883,
    77645840800
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     441,
     472
    ],
    "reexport": [
     1,
     59
    ],
    "star": [
     1,
     472
    ],
    "none": [
     11,
     236
    ]
   },
   "serves": [
    [
     "bindings",
     "src/_pytest/nodes.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('src/_pytest/python.py', 'Item')",
   "key": "[\"symbols\", [\"src/_pytest/python.py\", \"Item\"]]",
   "v1": [
    1136394170883,
    77645840800
   ],
   "v2": [
    1136394170883,
    77645840800
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
     "src/_pytest/python.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/acceptance_test.py', 'Item')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"Item\"]]",
   "v1": [
    1136394170883,
    77645840800
   ],
   "v2": [
    1136394170883,
    77645840800
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
     "testing/acceptance_test.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/conftest.py', 'Item')",
   "key": "[\"symbols\", [\"testing/conftest.py\", \"Item\"]]",
   "v1": [
    1136394170883,
    77645840800
   ],
   "v2": [
    1136394170883,
    77645840800
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
     "testing/conftest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/example_scripts/fixtures/custom_item/conftest.py', 'Item')",
   "key": "[\"symbols\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\", \"Item\"]]",
   "v1": [
    1136394170883,
    77645840800
   ],
   "v2": [
    1136394170883,
    77645840800
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
     "testing/example_scripts/fixtures/custom_item/conftest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_collection.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_collection.py\", \"Item\"]]",
   "v1": [
    1136394170883,
    77645840800
   ],
   "v2": [
    1136394170883,
    77645840800
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
     "testing/test_collection.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_junitxml.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_junitxml.py\", \"Item\"]]",
   "v1": [
    1136394170883,
    77645840800
   ],
   "v2": [
    1136394170883,
    77645840800
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
     "testing/test_junitxml.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_nodes.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_nodes.py\", \"Item\"]]",
   "v1": [
    1136394170883,
    77645840800
   ],
   "v2": [
    1136394170883,
    77645840800
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
     "testing/test_nodes.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_runner.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_runner.py\", \"Item\"]]",
   "v1": [
    1136394170883,

```
</details>

## Step 12

There it is: `Item` is a class at `src/_pytest/nodes.py:654`.

Tally: 3 subclasses confirmed, 0 ruled out, 9 pending. The search itself is complete; what is left is checking the candidates.

Still open: look at the classes in `src/_pytest/python.py` that derive from `Item`; look at the classes in `testing/acceptance_test.py` that derive from `Item`; look at the classes in `testing/conftest.py` that derive from `Item`; and 6 more.

Next I will look at `src/_pytest/python.py`'s top-level names for `Item`; the outline lists each class with its bases. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `testing/acceptance_test.py`'s top-level names for `Item`.

**Call:** `symbols('src/_pytest/python.py', 'Item')`

**Response**: outcome `ok`

```
module src/_pytest/python.py lines=1843 dynamic=yes all=none
1650 class Function (PyobjMixin,nodes.Item)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "src/_pytest/python.py",
    "Item"
   ],
   "desc": "look at the classes in `src/_pytest/python.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/acceptance_test.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/conftest.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/conftest.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/example_scripts/fixtures/custom_item/conftest.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/example_scripts/fixtures/custom_item/conftest.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_collection.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_collection.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_junitxml.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_junitxml.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_nodes.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_nodes.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_runner.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_runner.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_skipping.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_skipping.py` that derive from `Item`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/_pytest/python.py', 'Item')",
   "key": "[\"symbols\", [\"src/_pytest/python.py\", \"Item\"]]",
   "v1": [
    5350973,
    393550
   ],
   "v2": [
    2679422,
    196775
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
     "src/_pytest/python.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/acceptance_test.py', 'Item')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"Item\"]]",
   "v1": [
    5350973,
    393550
   ],
   "v2": [
    2679422,
    196775
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
     "testing/acceptance_test.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/conftest.py', 'Item')",
   "key": "[\"symbols\", [\"testing/conftest.py\", \"Item\"]]",
   "v1": [
    5350973,
    393550
   ],
   "v2": [
    2679422,
    196775
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
     "testing/conftest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/example_scripts/fixtures/custom_item/conftest.py', 'Item')",
   "key": "[\"symbols\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\", \"Item\"]]",
   "v1": [
    5350973,
    393550
   ],
   "v2": [
    2679422,
    196775
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
     "testing/example_scripts/fixtures/custom_item/conftest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_collection.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_collection.py\", \"Item\"]]",
   "v1": [
    5350973,
    393550
   ],
   "v2": [
    2679422,
    196775
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
     "testing/test_collection.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_junitxml.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_junitxml.py\", \"Item\"]]",
   "v1": [
    5350973,
    393550
   ],
   "v2": [
    2679422,
    196775
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
     "testing/test_junitxml.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_nodes.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_nodes.py\", \"Item\"]]",
   "v1": [
    5350973,
    393550
   ],
   "v2": [
    2679422,
    196775
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
     "testing/test_nodes.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_runner.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_runner.py\", \"Item\"]]",
   "v1": [
    5350973,
    393550
   ],
   "v2": [
    2679422,
    196775
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
     "testing/test_runner.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_skipping.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_skipping.py\", \"Item\"]]",
   "v1": [
    5350973,
    393550
   ],
   "v2": [
    2679422,
    196775
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
     "testing/test_skipping.py",
     "Item"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/_pytest/python.py', 'Item')",
  "key": "[\"symbols\", [\"src/_pytest/python.py\", \"Item\"]]",
  "provenance": "`s
```
</details>

## Step 13

`src/_pytest/python.py` has `class Function(PyobjMixin,nodes.Item)` at line 1650. Nothing binds `Item` at module level there. Careful: this module manipulates its namespace dynamically, so static resolution is not reliable here.

Tally: 3 subclasses confirmed, 1 ruled out, 8 pending. The search itself is complete; what is left is checking the candidates.

I'll look at `testing/acceptance_test.py`'s top-level names for `Item`; the outline lists each class with its bases. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `testing/conftest.py`'s top-level names for `Item`.

**Call:** `symbols('testing/acceptance_test.py', 'Item')`

**Response**: outcome `ok`

```
module testing/acceptance_test.py lines=1770 dynamic=no all=none
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/acceptance_test.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/acceptance_test.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/conftest.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/conftest.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/example_scripts/fixtures/custom_item/conftest.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/example_scripts/fixtures/custom_item/conftest.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_collection.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_collection.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_junitxml.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_junitxml.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_nodes.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_nodes.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_runner.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_runner.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_skipping.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_skipping.py` that derive from `Item`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('testing/acceptance_test.py', 'Item')",
   "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"Item\"]]",
   "v1": [
    951459,
    78710
   ],
   "v2": [
    2382583,
    196775
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
     "testing/acceptance_test.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/conftest.py', 'Item')",
   "key": "[\"symbols\", [\"testing/conftest.py\", \"Item\"]]",
   "v1": [
    951459,
    78710
   ],
   "v2": [
    2382583,
    196775
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
     "testing/conftest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/example_scripts/fixtures/custom_item/conftest.py', 'Item')",
   "key": "[\"symbols\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\", \"Item\"]]",
   "v1": [
    951459,
    78710
   ],
   "v2": [
    2382583,
    196775
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
     "testing/example_scripts/fixtures/custom_item/conftest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_collection.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_collection.py\", \"Item\"]]",
   "v1": [
    951459,
    78710
   ],
   "v2": [
    2382583,
    196775
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
     "testing/test_collection.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_junitxml.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_junitxml.py\", \"Item\"]]",
   "v1": [
    951459,
    78710
   ],
   "v2": [
    2382583,
    196775
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
     "testing/test_junitxml.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_nodes.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_nodes.py\", \"Item\"]]",
   "v1": [
    951459,
    78710
   ],
   "v2": [
    2382583,
    196775
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
     "testing/test_nodes.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_runner.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_runner.py\", \"Item\"]]",
   "v1": [
    951459,
    78710
   ],
   "v2": [
    2382583,
    196775
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
     "testing/test_runner.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_skipping.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_skipping.py\", \"Item\"]]",
   "v1": [
    951459,
    78710
   ],
   "v2": [
    2382583,
    196775
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
     "testing/test_skipping.py",
     "Item"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('testing/acceptance_test.py', 'Item')",
  "key": "[\"symbols\", [\"testing/acceptance_test.py\", \"Item\"]]",
  "provenance": "`testing/acceptance_test.py` had a matching line (step 1); its outline names every `Item` import exactly",
  "v2": [
   2382583,
   196775
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
  "ok": "[\"symbols\", [\"testing/conftest.py\", \"Item\"]]",
  "cap": "[\"symbols\", [\"testing/conftest.py\", \"Item\"]]"
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
  "planned": "[\"symbols\", [\"testing/acceptance_test.py\", \"Item\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "s
```
</details>

## Step 14

The test module `testing/acceptance_test.py` matched the search, but none of its module-level classes actually derive from `Item`; probably a nested class, a comment or a string.

Tally: 3 subclasses confirmed, 1 ruled out, 7 pending. The search itself is complete; what is left is checking the candidates.

Next I will look at `testing/conftest.py`'s top-level names for `Item`; the outline lists each class with its bases. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `testing/example_scripts/fixtures/custom_item/conftest.py`'s top-level names for `Item`.

**Call:** `symbols('testing/conftest.py', 'Item')`

**Response**: outcome `ok`

```
module testing/conftest.py lines=252 dynamic=no all=none
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/conftest.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/conftest.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/example_scripts/fixtures/custom_item/conftest.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/example_scripts/fixtures/custom_item/conftest.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_collection.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_collection.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_junitxml.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_junitxml.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_nodes.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_nodes.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_runner.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_runner.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_skipping.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_skipping.py` that derive from `Item`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('testing/conftest.py', 'Item')",
   "key": "[\"symbols\", [\"testing/conftest.py\", \"Item\"]]",
   "v1": [
    4163617,
    393550
   ],
   "v2": [
    2085744,
    196775
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
     "testing/conftest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/example_scripts/fixtures/custom_item/conftest.py', 'Item')",
   "key": "[\"symbols\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\", \"Item\"]]",
   "v1": [
    4163617,
    393550
   ],
   "v2": [
    2085744,
    196775
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
     "testing/example_scripts/fixtures/custom_item/conftest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_collection.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_collection.py\", \"Item\"]]",
   "v1": [
    4163617,
    393550
   ],
   "v2": [
    2085744,
    196775
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
     "testing/test_collection.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_junitxml.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_junitxml.py\", \"Item\"]]",
   "v1": [
    4163617,
    393550
   ],
   "v2": [
    2085744,
    196775
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
     "testing/test_junitxml.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_nodes.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_nodes.py\", \"Item\"]]",
   "v1": [
    4163617,
    393550
   ],
   "v2": [
    2085744,
    196775
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
     "testing/test_nodes.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_runner.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_runner.py\", \"Item\"]]",
   "v1": [
    4163617,
    393550
   ],
   "v2": [
    2085744,
    196775
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
     "testing/test_runner.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_skipping.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_skipping.py\", \"Item\"]]",
   "v1": [
    4163617,
    393550
   ],
   "v2": [
    2085744,
    196775
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
     "testing/test_skipping.py",
     "Item"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('testing/conftest.py', 'Item')",
  "key": "[\"symbols\", [\"testing/conftest.py\", \"Item\"]]",
  "provenance": "`testing/conftest.py` had a matching line (step 1); its outline names every `Item` import exactly",
  "v2": [
   2085744,
   196775
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
  "ok": "[\"symbols\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\", \"Item\"]]",
  "cap": "[\"symbols\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\", \"Item\"]]"
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
  "planned": "[\"symbols\", [\"testing/conftest.py\", \"Item\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 14,
   "path": "testing/conftest.py",
   "filter": "Item",
   "header": {
    "lines": 252,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "subclasses",
  "step": 1,
  "of": 2,
  "candidates": [
   "doc/en/example/nonpython/conftest.py",
   "src/_pytest/doctest.py",
   "src/_pytest/python.py",
   "testing/acceptance_test.py",
   "testing/conftest.py",
   "testing/example_scripts/fixtures/custom_item/conftest.py",
   "testing/example_scripts/issue88_initial_file_multin
```
</details>

## Step 15

The test module `testing/conftest.py` matched the search, but none of its module-level classes actually derive from `Item`; probably a nested class, a comment or a string.

Tally: 3 subclasses confirmed, 1 ruled out, 6 pending. The search itself is complete; what is left is checking the candidates.

Let me look at `testing/example_scripts/fixtures/custom_item/conftest.py`'s top-level names for `Item`; the outline lists each class with its bases. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `testing/test_collection.py`'s top-level names for `Item`.

**Call:** `symbols('testing/example_scripts/fixtures/custom_item/conftest.py', 'Item')`

**Response**: outcome `ok`

```
module testing/example_scripts/fixtures/custom_item/conftest.py lines=19 dynamic=no all=none
7 class CustomItem (pytest.Item)
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/example_scripts/fixtures/custom_item/conftest.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/example_scripts/fixtures/custom_item/conftest.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_collection.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_collection.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_junitxml.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_junitxml.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_nodes.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_nodes.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_runner.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_runner.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_skipping.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_skipping.py` that derive from `Item`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('testing/example_scripts/fixtures/custom_item/conftest.py', 'Item')",
   "key": "[\"symbols\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\", \"Item\"]]",
   "v1": [
    3569939,
    393550
   ],
   "v2": [
    357781,
    39355
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
     "testing/example_scripts/fixtures/custom_item/conftest.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_collection.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_collection.py\", \"Item\"]]",
   "v1": [
    3569939,
    393550
   ],
   "v2": [
    357781,
    39355
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
     "testing/test_collection.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_junitxml.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_junitxml.py\", \"Item\"]]",
   "v1": [
    3569939,
    393550
   ],
   "v2": [
    357781,
    39355
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
     "testing/test_junitxml.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_nodes.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_nodes.py\", \"Item\"]]",
   "v1": [
    3569939,
    393550
   ],
   "v2": [
    357781,
    39355
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
     "testing/test_nodes.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_runner.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_runner.py\", \"Item\"]]",
   "v1": [
    3569939,
    393550
   ],
   "v2": [
    357781,
    39355
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
     "testing/test_runner.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_skipping.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_skipping.py\", \"Item\"]]",
   "v1": [
    3569939,
    393550
   ],
   "v2": [
    357781,
    39355
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
     "testing/test_skipping.py",
     "Item"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('testing/example_scripts/fixtures/custom_item/conftest.py', 'Item')",
  "key": "[\"symbols\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\", \"Item\"]]",
  "provenance": "`testing/example_scripts/fixtures/custom_item/conftest.py` had a matching line (step 1); its outline names every `Item` import exactly",
  "v2": [
   357781,
   39355
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
  "ok": "[\"symbols\", [\"testing/test_collection.py\", \"Item\"]]",
  "cap": "[\"symbols\", [\"testing/test_collection.py\", \"Item\"]]"
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
  "planned": "[\"symbols\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\", \"Item\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 15,
   "path": "testing/example_scripts/fixtures/custom_item/conftest.py",
   "filter": "Item",
   "header": {
    "lines": 19,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "testing/example_scripts/fixtures/custom_item/conftest.py",
     "name": "CustomItem",
     "line": 7,
     "kind": "class",
     "src": null,
     "src_name": null,
     "conditional": false,
     "col": 0,
     "bases": [
      "pytest.Item"
     ]
    }
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "subclasses",
  "step": 1,
  "of": 2,
  "candidates": [
   "doc/en/example/nonpython/conftest.py",
   "src/_pytest/doctest.py",
   "src/_pytest/python.py",
   "testing/acceptance_test.py",
   "testing/conftest.py",
   "testing/example_scripts/fixtures/custom_item/conftest.py",
   "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
   "testing/test_collection.py",
   "testing/test_junitxml.py",
   "testing/test_nodes.py",
   "testing/test_runner.py",
   "testing/test_skipping.py"
  ],
  "table": [
   [
    "doc/en/example/non
```
</details>

## Step 16

The test module `testing/example_scripts/fixtures/custom_item/conftest.py` has `class CustomItem(pytest.Item)` at line 7. Nothing binds `Item` at module level there.

Tally: 3 subclasses confirmed, 1 ruled out, 6 pending. The search itself is complete; what is left is checking the candidates.

Still open: check the top-level names of `testing/example_scripts/fixtures/custom_item/conftest.py` for `pytest`; look at the classes in `testing/test_collection.py` that derive from `Item`; look at the classes in `testing/test_junitxml.py` that derive from `Item`; and 3 more.

I'll look at `testing/test_collection.py`'s top-level names for `Item`; the outline lists each class with its bases. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `testing/example_scripts/fixtures/custom_item/conftest.py`'s top-level names for `pytest`.

**Call:** `symbols('testing/test_collection.py', 'Item')`

**Response**: outcome `ok`

```
module testing/test_collection.py lines=2800 dynamic=no all=none
20 from Item <- _pytest.nodes Item
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "testing/example_scripts/fixtures/custom_item/conftest.py",
    "pytest"
   ],
   "desc": "check the top-level names of `testing/example_scripts/fixtures/custom_item/conftest.py` for `pytest`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_collection.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_collection.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_junitxml.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_junitxml.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_nodes.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_nodes.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_runner.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_runner.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_skipping.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_skipping.py` that derive from `Item`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('testing/example_scripts/fixtures/custom_item/conftest.py', 'pytest')",
   "key": "[\"symbols\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\", \"pytest\"]]",
   "v1": [
    274761155,
    26320624
   ],
   "v2": [
    6882189187,
    658015600
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     3,
     100
    ],
    "reexport": [
     23,
     25
    ],
    "star": [
     1,
     100
    ],
    "none": [
     1,
     25
    ]
   },
   "serves": [
    [
     "bindings",
     "testing/example_scripts/fixtures/custom_item/conftest.py",
     "pytest"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_collection.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_collection.py\", \"Item\"]]",
   "v1": [
    6882189187,
    658015600
   ],
   "v2": [
    6882189187,
    658015600
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
     "testing/test_collection.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_junitxml.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_junitxml.py\", \"Item\"]]",
   "v1": [
    6882189187,
    658015600
   ],
   "v2": [
    6882189187,
    658015600
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
     "testing/test_junitxml.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_nodes.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_nodes.py\", \"Item\"]]",
   "v1": [
    6882189187,
    658015600
   ],
   "v2": [
    6882189187,
    658015600
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
     "testing/test_nodes.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_runner.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_runner.py\", \"Item\"]]",
   "v1": [
    6882189187,
    658015600
   ],
   "v2": [
    6882189187,
    658015600
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
     "testing/test_runner.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_skipping.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_skipping.py\", \"Item\"]]",
   "v1": [
    6882189187,
    658015600
   ],
   "v2": [
    6882189187,
    658015600
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
     "testing/test_skipping.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/example_scripts/fixtures/custom_item/conftest.py')",
   "key": "[\"symbols\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\"]]",
   "v1": [
    232031306201,
    21977721040
   ],
   "v2": [
    5810468644657,
    549443026000
   ],
   "p_cap": [
    99,
    835
   ],
   "forecast": {
    "def": [
     552,
     20875
    ],
    "reexport": [
     16928,
     20875
    ],
    "star": [
     184,
     20875
    ],
    "none": [
     736,
     20875
    ],
    "cap": [
     99,
     835
    ]
   },
   "serves": [
    [
     "bindings",
     "testing/example_scripts/fixtures/custom_item/conftest.py",
     "pytest"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('testing/test_collection.py', 'Item')",
  "key": "[\"symbols\", [\"testing/test_collection.py\", \"Item\"]]",
  "provenance": "`testing/test_collection.py` had a matching line (step 1); its outline names every `Item` import exactly",
  "v2": [
   6882189187,
   658015600
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
  "ok": "[\"symbols\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\", \"pytest\"]]",
  "cap": "[\"symbols\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\", \"pytest\"]]"
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
  "planned": "[\"symbols\", [\"testing/test_collection.py\", \"Item\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 16,
   "path": "testing/test_collection.py",
   "filter": "Item",
   "header": {
    "lines": 2800,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "testing/test_collection.py",
     "name": "Item",
     "line": 20,
     "kind": "from",
   
```
</details>

## Step 17

The test module `testing/test_collection.py` matched the search, but none of its module-level classes actually derive from `Item`; probably a nested class, a comment or a string. It gets `Item` from `_pytest.nodes` (line 20), which is what the base name resolves through.

Tally: 3 subclasses confirmed, 1 ruled out, 5 pending. The search itself is complete; what is left is checking the candidates.

Let me look at `testing/example_scripts/fixtures/custom_item/conftest.py`'s top-level names for `pytest`; that settles what the name means there. Almost certainly it is re-exported from somewhere else. If the name is not bound there or it is defined right there, I will look at `testing/test_junitxml.py`'s top-level names for `Item`.

**Call:** `symbols('testing/example_scripts/fixtures/custom_item/conftest.py', 'pytest')`

**Response**: outcome `reexport`

```
module testing/example_scripts/fixtures/custom_item/conftest.py lines=19 dynamic=no all=none
4 import pytest <- pytest
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "testing/example_scripts/fixtures/custom_item/conftest.py",
    "pytest"
   ],
   "desc": "check the top-level names of `testing/example_scripts/fixtures/custom_item/conftest.py` for `pytest`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_junitxml.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_junitxml.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_nodes.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_nodes.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_runner.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_runner.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_skipping.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_skipping.py` that derive from `Item`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('testing/example_scripts/fixtures/custom_item/conftest.py', 'pytest')",
   "key": "[\"symbols\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\", \"pytest\"]]",
   "v1": [
    5876399259,
    658015600
   ],
   "v2": [
    5889559571,
    658015600
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     3,
     100
    ],
    "reexport": [
     23,
     25
    ],
    "star": [
     1,
     100
    ],
    "none": [
     1,
     25
    ]
   },
   "serves": [
    [
     "bindings",
     "testing/example_scripts/fixtures/custom_item/conftest.py",
     "pytest"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_junitxml.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_junitxml.py\", \"Item\"]]",
   "v1": [
    5889559571,
    658015600
   ],
   "v2": [
    5889559571,
    658015600
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
     "testing/test_junitxml.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_nodes.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_nodes.py\", \"Item\"]]",
   "v1": [
    5889559571,
    658015600
   ],
   "v2": [
    5889559571,
    658015600
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
     "testing/test_nodes.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_runner.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_runner.py\", \"Item\"]]",
   "v1": [
    5889559571,
    658015600
   ],
   "v2": [
    5889559571,
    658015600
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
     "testing/test_runner.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_skipping.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_skipping.py\", \"Item\"]]",
   "v1": [
    5889559571,
    658015600
   ],
   "v2": [
    5889559571,
    658015600
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
     "testing/test_skipping.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/example_scripts/fixtures/custom_item/conftest.py')",
   "key": "[\"symbols\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\"]]",
   "v1": [
    994387385133,
    109888605200
   ],
   "v2": [
    4981622915297,
    549443026000
   ],
   "p_cap": [
    99,
    835
   ],
   "forecast": {
    "def": [
     552,
     20875
    ],
    "reexport": [
     16928,
     20875
    ],
    "star": [
     184,
     20875
    ],
    "none": [
     736,
     20875
    ],
    "cap": [
     99,
     835
    ]
   },
   "serves": [
    [
     "bindings",
     "testing/example_scripts/fixtures/custom_item/conftest.py",
     "pytest"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('testing/example_scripts/fixtures/custom_item/conftest.py', 'pytest')",
  "key": "[\"symbols\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\", \"pytest\"]]",
  "provenance": "module `testing/example_scripts/fixtures/custom_item/conftest.py` (step 1), name `pytest` (step 4)",
  "v2": [
   5889559571,
   658015600
  ]
 },
 "forecast": {
  "def": [
   3,
   100
  ],
  "reexport": [
   23,
   25
  ],
  "star": [
   1,
   100
  ],
  "none": [
   1,
   25
  ]
 },
 "plan": {
  "def": "[\"symbols\", [\"testing/test_junitxml.py\", \"Item\"]]",
  "reexport": "[\"symbols\", [\"testing/test_junitxml.py\", \"Item\"]]",
  "star": "[\"symbols\", [\"testing/test_junitxml.py\", \"Item\"]]",
  "none": "[\"symbols\", [\"testing/test_junitxml.py\", \"Item\"]]"
 },
 "hedges": [
  {
   "outcome": "reexport",
   "word": "almost certainly",
   "p": [
    23,
    25
   ]
  }
 ],
 "adherence": {
  "planned": "[\"symbols\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\", \"pytest\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 17,
   "path": "testing/example_scripts/fixtures/custom_item/conftest.py",
   "filter": "pytest",
   "header": {
    "lines": 19,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [
    {
     "module": "testing/example_scripts/fixtures/custom_item/conftest.py",
     "name": "pytest",
     "line": 4,
     "kind": "import",
     "src": "pytest",
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
  "phase": "subclasses",
  "step": 1,
  "of": 2,
  "candidates": [
   "doc/en/example/nonpython/conftest.py",
   "src/_pytest/doctest.py",
   "src/_pytest/python.py",
   "testing/acceptance_tes
```
</details>

## Step 18

In the test module `testing/example_scripts/fixtures/custom_item/conftest.py`, `pytest` is a module import (`import pytest`), not a definition.

Tally: 4 subclasses confirmed, 1 ruled out, 4 pending. The search itself is complete; what is left is checking the candidates.

Next I will look at `testing/test_junitxml.py`'s top-level names for `Item`; the outline lists each class with its bases. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `testing/test_nodes.py`'s top-level names for `Item`.

**Call:** `symbols('testing/test_junitxml.py', 'Item')`

**Response**: outcome `ok`

```
module testing/test_junitxml.py lines=1887 dynamic=no all=none
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_junitxml.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_junitxml.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_nodes.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_nodes.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_runner.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_runner.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_skipping.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_skipping.py` that derive from `Item`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('testing/test_junitxml.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_junitxml.py\", \"Item\"]]",
   "v1": [
    2382583,
    393550
   ],
   "v2": [
    1195227,
    196775
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
     "testing/test_junitxml.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_nodes.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_nodes.py\", \"Item\"]]",
   "v1": [
    2382583,
    393550
   ],
   "v2": [
    1195227,
    196775
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
     "testing/test_nodes.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_runner.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_runner.py\", \"Item\"]]",
   "v1": [
    2382583,
    393550
   ],
   "v2": [
    1195227,
    196775
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
     "testing/test_runner.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_skipping.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_skipping.py\", \"Item\"]]",
   "v1": [
    2382583,
    393550
   ],
   "v2": [
    1195227,
    196775
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
     "testing/test_skipping.py",
     "Item"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('testing/test_junitxml.py', 'Item')",
  "key": "[\"symbols\", [\"testing/test_junitxml.py\", \"Item\"]]",
  "provenance": "`testing/test_junitxml.py` had a matching line (step 1); its outline names every `Item` import exactly",
  "v2": [
   1195227,
   196775
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
  "ok": "[\"symbols\", [\"testing/test_nodes.py\", \"Item\"]]",
  "cap": "[\"symbols\", [\"testing/test_nodes.py\", \"Item\"]]"
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
  "planned": "[\"symbols\", [\"testing/test_junitxml.py\", \"Item\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 18,
   "path": "testing/test_junitxml.py",
   "filter": "Item",
   "header": {
    "lines": 1887,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "subclasses",
  "step": 1,
  "of": 2,
  "candidates": [
   "doc/en/example/nonpython/conftest.py",
   "src/_pytest/doctest.py",
   "src/_pytest/python.py",
   "testing/acceptance_test.py",
   "testing/conftest.py",
   "testing/example_scripts/fixtures/custom_item/conftest.py",
   "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
   "testing/test_collection.py",
   "testing/test_junitxml.py",
   "testing/test_nodes.py",
   "testing/test_runner.py",
   "testing/test_skipping.py"
  ],
  "table": [
   [
    "doc/en/example/nonpython/conftest.py",
    "doc/en/example/nonpython/conftest.py:22:YamlItem",
    "in",
    "base `pytest.Item` resolves to the target"
   ],
   [
    "src/_pytest/doctest.py",
    "src/_pytest/doctest.py:252:DoctestItem",
    "in",
    "base `Item` resolves to the target"
   ],
   [
    "src/_pytest/python.py",
    "src/_pytest/python.py:1650:Function",
    "out",
    "base `nodes.Item` resolves to unresolved(`nodes` is not a module)"
   ],
   [
    "testing/acceptance_test.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
   ],
   [
    "testing/conftest.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
   ],
   [
    "testing/example_scripts/fixtures/custom_item/conftest.py",
    "testing/example_scripts/fixtures/custom_item/conftest.py:7:CustomItem",
    "in",
    "base `pytest.Item` resolves to the target"
   ],
   [
    "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
    "testing/example_scripts/issue88_initial_file_multinodes/conftest.py:16:MyItem",
    "in",
    "base `pytest.Item` resolves to the target"
   ],
   [
    "testing/test_collection.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
   ],
   [
    "testing/test_junitxml.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
   ],
   [
    "testing/test_nodes.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "testing/test_runner.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "testing/test_skipping.py",
    null,
    "pending",
    "not yet examined"
   ]
  ],
  "uncovered": {
   "SUBCLASS": []
  },
  "n_in": 4,
  "n_out": 1,
  "n_pending": 3
 }
}
```
</details>

## Step 19

The test module `testing/test_junitxml.py` matched the search, but none of its module-level classes actually derive from `Item`; probably a nested class, a comment or a string.

Tally: 4 subclasses confirmed, 1 ruled out, 3 pending. The search itself is complete; what is left is checking the candidates.

I'll look at `testing/test_nodes.py`'s top-level names for `Item`; the outline lists each class with its bases. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `testing/test_runner.py`'s top-level names for `Item`.

**Call:** `symbols('testing/test_nodes.py', 'Item')`

**Response**: outcome `ok`

```
module testing/test_nodes.py lines=165 dynamic=no all=none
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_nodes.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_nodes.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_runner.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_runner.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_skipping.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_skipping.py` that derive from `Item`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('testing/test_nodes.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_nodes.py\", \"Item\"]]",
   "v1": [
    357781,
    78710
   ],
   "v2": [
    898388,
    196775
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
     "testing/test_nodes.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_runner.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_runner.py\", \"Item\"]]",
   "v1": [
    357781,
    78710
   ],
   "v2": [
    898388,
    196775
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
     "testing/test_runner.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_skipping.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_skipping.py\", \"Item\"]]",
   "v1": [
    357781,
    78710
   ],
   "v2": [
    898388,
    196775
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
     "testing/test_skipping.py",
     "Item"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('testing/test_nodes.py', 'Item')",
  "key": "[\"symbols\", [\"testing/test_nodes.py\", \"Item\"]]",
  "provenance": "`testing/test_nodes.py` had a matching line (step 1); its outline names every `Item` import exactly",
  "v2": [
   898388,
   196775
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
  "ok": "[\"symbols\", [\"testing/test_runner.py\", \"Item\"]]",
  "cap": "[\"symbols\", [\"testing/test_runner.py\", \"Item\"]]"
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
  "planned": "[\"symbols\", [\"testing/test_nodes.py\", \"Item\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 19,
   "path": "testing/test_nodes.py",
   "filter": "Item",
   "header": {
    "lines": 165,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "subclasses",
  "step": 1,
  "of": 2,
  "candidates": [
   "doc/en/example/nonpython/conftest.py",
   "src/_pytest/doctest.py",
   "src/_pytest/python.py",
   "testing/acceptance_test.py",
   "testing/conftest.py",
   "testing/example_scripts/fixtures/custom_item/conftest.py",
   "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
   "testing/test_collection.py",
   "testing/test_junitxml.py",
   "testing/test_nodes.py",
   "testing/test_runner.py",
   "testing/test_skipping.py"
  ],
  "table": [
   [
    "doc/en/example/nonpython/conftest.py",
    "doc/en/example/nonpython/conftest.py:22:YamlItem",
    "in",
    "base `pytest.Item` resolves to the target"
   ],
   [
    "src/_pytest/doctest.py",
    "src/_pytest/doctest.py:252:DoctestItem",
    "in",
    "base `Item` resolves to the target"
   ],
   [
    "src/_pytest/python.py",
    "src/_pytest/python.py:1650:Function",
    "out",
    "base `nodes.Item` resolves to unresolved(`nodes` is not a module)"
   ],
   [
    "testing/acceptance_test.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
   ],
   [
    "testing/conftest.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
   ],
   [
    "testing/example_scripts/fixtures/custom_item/conftest.py",
    "testing/example_scripts/fixtures/custom_item/conftest.py:7:CustomItem",
    "in",
    "base `pytest.Item` resolves to the target"
   ],
   [
    "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
    "testing/example_scripts/issue88_initial_file_multinodes/conftest.py:16:MyItem",
    "in",
    "base `pytest.Item` resolves to the target"
   ],
   [
    "testing/test_collection.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
   ],
   [
    "testing/test_junitxml.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
   ],
   [
    "testing/test_nodes.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
   ],
   [
    "testing/test_runner.py",
    null,
    "pending",
    "not yet examined"
   ],
   [
    "testing/test_skipping.py",
    null,
    "pending",
    "not yet examined"
   ]
  ],
  "uncovered": {
   "SUBCLASS": []
  },
  "n_in": 4,
  "n_out": 1,
  "n_pending": 2
 }
}
```
</details>

## Step 20

The test module `testing/test_nodes.py` matched the search, but none of its module-level classes actually derive from `Item`; probably a nested class, a comment or a string.

Tally: 4 subclasses confirmed, 1 ruled out, 2 pending. The search itself is complete; what is left is checking the candidates.

Next I will look at `testing/test_runner.py`'s top-level names for `Item`; the outline lists each class with its bases. Almost certainly the outline shows what I need. If the outline is too long to fit, I will look at `testing/test_skipping.py`'s top-level names for `Item`.

**Call:** `symbols('testing/test_runner.py', 'Item')`

**Response**: outcome `ok`

```
module testing/test_runner.py lines=1276 dynamic=no all=none
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_runner.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_runner.py` that derive from `Item`"
  },
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_skipping.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_skipping.py` that derive from `Item`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('testing/test_runner.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_runner.py\", \"Item\"]]",
   "v1": [
    1195227,
    393550
   ],
   "v2": [
    601549,
    196775
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
     "testing/test_runner.py",
     "Item"
    ]
   ]
  },
  {
   "call": "symbols('testing/test_skipping.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_skipping.py\", \"Item\"]]",
   "v1": [
    1195227,
    393550
   ],
   "v2": [
    601549,
    196775
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
     "testing/test_skipping.py",
     "Item"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('testing/test_runner.py', 'Item')",
  "key": "[\"symbols\", [\"testing/test_runner.py\", \"Item\"]]",
  "provenance": "`testing/test_runner.py` had a matching line (step 1); its outline names every `Item` import exactly",
  "v2": [
   601549,
   196775
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
  "ok": "[\"symbols\", [\"testing/test_skipping.py\", \"Item\"]]",
  "cap": "[\"symbols\", [\"testing/test_skipping.py\", \"Item\"]]"
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
  "planned": "[\"symbols\", [\"testing/test_runner.py\", \"Item\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 20,
   "path": "testing/test_runner.py",
   "filter": "Item",
   "header": {
    "lines": 1276,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "subclasses",
  "step": 1,
  "of": 2,
  "candidates": [
   "doc/en/example/nonpython/conftest.py",
   "src/_pytest/doctest.py",
   "src/_pytest/python.py",
   "testing/acceptance_test.py",
   "testing/conftest.py",
   "testing/example_scripts/fixtures/custom_item/conftest.py",
   "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
   "testing/test_collection.py",
   "testing/test_junitxml.py",
   "testing/test_nodes.py",
   "testing/test_runner.py",
   "testing/test_skipping.py"
  ],
  "table": [
   [
    "doc/en/example/nonpython/conftest.py",
    "doc/en/example/nonpython/conftest.py:22:YamlItem",
    "in",
    "base `pytest.Item` resolves to the target"
   ],
   [
    "src/_pytest/doctest.py",
    "src/_pytest/doctest.py:252:DoctestItem",
    "in",
    "base `Item` resolves to the target"
   ],
   [
    "src/_pytest/python.py",
    "src/_pytest/python.py:1650:Function",
    "out",
    "base `nodes.Item` resolves to unresolved(`nodes` is not a module)"
   ],
   [
    "testing/acceptance_test.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
   ],
   [
    "testing/conftest.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
   ],
   [
    "testing/example_scripts/fixtures/custom_item/conftest.py",
    "testing/example_scripts/fixtures/custom_item/conftest.py:7:CustomItem",
    "in",
    "base `pytest.Item` resolves to the target"
   ],
   [
    "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
    "testing/example_scripts/issue88_initial_file_multinodes/conftest.py:16:MyItem",
    "in",
    "base `pytest.Item` resolves to the target"
   ],
   [
    "testing/test_collection.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
   ],
   [
    "testing/test_junitxml.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
   ],
   [
    "testing/test_nodes.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
   ],
   [
    "testing/test_runner.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
   ],
   [
    "testing/test_skipping.py",
    null,
    "pending",
    "not yet examined"
   ]
  ],
  "uncovered": {
   "SUBCLASS": []
  },
  "n_in": 4,
  "n_out": 1,
  "n_pending": 1
 }
}
```
</details>

## Step 21

The test module `testing/test_runner.py` matched the search, but none of its module-level classes actually derive from `Item`; probably a nested class, a comment or a string.

Tally: 4 subclasses confirmed, 1 ruled out, 1 pending. The search itself is complete; what is left is checking the candidates.

Let me look at `testing/test_skipping.py`'s top-level names for `Item`; the outline lists each class with its bases. Almost certainly the outline shows what I need. If the outline is too long to fit, I follow whatever it opens up.

**Call:** `symbols('testing/test_skipping.py', 'Item')`

**Response**: outcome `ok`

```
module testing/test_skipping.py lines=1570 dynamic=no all=none
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "outline",
   "key": [
    "outline",
    "testing/test_skipping.py",
    "Item"
   ],
   "desc": "look at the classes in `testing/test_skipping.py` that derive from `Item`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('testing/test_skipping.py', 'Item')",
   "key": "[\"symbols\", [\"testing/test_skipping.py\", \"Item\"]]",
   "v1": [
    601549,
    393550
   ],
   "v2": [
    601549,
    393550
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
     "testing/test_skipping.py",
     "Item"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('testing/test_skipping.py', 'Item')",
  "key": "[\"symbols\", [\"testing/test_skipping.py\", \"Item\"]]",
  "provenance": "`testing/test_skipping.py` had a matching line (step 1); its outline names every `Item` import exactly",
  "v2": [
   601549,
   393550
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
  "planned": "[\"symbols\", [\"testing/test_skipping.py\", \"Item\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "outline",
   "step": 21,
   "path": "testing/test_skipping.py",
   "filter": "Item",
   "header": {
    "lines": 1570,
    "dynamic": false,
    "all_status": "none",
    "all_line": null
   },
   "bindings": [],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "subclasses",
  "step": 1,
  "of": 2,
  "candidates": [
   "doc/en/example/nonpython/conftest.py",
   "src/_pytest/doctest.py",
   "src/_pytest/python.py",
   "testing/acceptance_test.py",
   "testing/conftest.py",
   "testing/example_scripts/fixtures/custom_item/conftest.py",
   "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
   "testing/test_collection.py",
   "testing/test_junitxml.py",
   "testing/test_nodes.py",
   "testing/test_runner.py",
   "testing/test_skipping.py"
  ],
  "table": [
   [
    "doc/en/example/nonpython/conftest.py",
    "doc/en/example/nonpython/conftest.py:22:YamlItem",
    "in",
    "base `pytest.Item` resolves to the target"
   ],
   [
    "src/_pytest/doctest.py",
    "src/_pytest/doctest.py:252:DoctestItem",
    "in",
    "base `Item` resolves to the target"
   ],
   [
    "src/_pytest/python.py",
    "src/_pytest/python.py:1650:Function",
    "out",
    "base `nodes.Item` resolves to unresolved(`nodes` is not a module)"
   ],
   [
    "testing/acceptance_test.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
   ],
   [
    "testing/conftest.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
   ],
   [
    "testing/example_scripts/fixtures/custom_item/conftest.py",
    "testing/example_scripts/fixtures/custom_item/conftest.py:7:CustomItem",
    "in",
    "base `pytest.Item` resolves to the target"
   ],
   [
    "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
    "testing/example_scripts/issue88_initial_file_multinodes/conftest.py:16:MyItem",
    "in",
    "base `pytest.Item` resolves to the target"
   ],
   [
    "testing/test_collection.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
   ],
   [
    "testing/test_junitxml.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
   ],
   [
    "testing/test_nodes.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
   ],
   [
    "testing/test_runner.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
   ],
   [
    "testing/test_skipping.py",
    null,
    "none",
    "matching line but nothing relevant at module level"
   ]
  ],
  "uncovered": {
   "SUBCLASS": []
  },
  "n_in": 4,
  "n_out": 1,
  "n_pending": 0
 }
}
```
</details>

## Step 22

The test module `testing/test_skipping.py` matched the search, but none of its module-level classes actually derive from `Item`; probably a nested class, a comment or a string. That is the full set of subclasses; now which of them lack the method.

Tally: 0 classes without their own method confirmed, 0 ruled out, 4 pending.

Next I will check `MyItem`'s own members in `testing/example_scripts/issue88_initial_file_multinodes/conftest.py`; only its own members tell me whether it overrides. Almost certainly the members fit. If there are too many members, I will check `YamlItem`'s own members in `doc/en/example/nonpython/conftest.py`.

**Call:** `members('testing/example_scripts/issue88_initial_file_multinodes/conftest.py', 'MyItem')`

**Response**: outcome `ok`

```
class MyItem in testing/example_scripts/issue88_initial_file_multinodes/conftest.py definitions=1
17 def runtest
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "members",
   "key": [
    "members",
    "doc/en/example/nonpython/conftest.py",
    "YamlItem"
   ],
   "desc": "look at what `YamlItem` in `doc/en/example/nonpython/conftest.py` defines itself"
  },
  {
   "kind": "members",
   "key": [
    "members",
    "src/_pytest/doctest.py",
    "DoctestItem"
   ],
   "desc": "look at what `DoctestItem` in `src/_pytest/doctest.py` defines itself"
  },
  {
   "kind": "members",
   "key": [
    "members",
    "testing/example_scripts/fixtures/custom_item/conftest.py",
    "CustomItem"
   ],
   "desc": "look at what `CustomItem` in `testing/example_scripts/fixtures/custom_item/conftest.py` defines itself"
  },
  {
   "kind": "members",
   "key": [
    "members",
    "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
    "MyItem"
   ],
   "desc": "look at what `MyItem` in `testing/example_scripts/issue88_initial_file_multinodes/conftest.py` defines itself"
  }
 ],
 "candidates": [
  {
   "call": "members('doc/en/example/nonpython/conftest.py', 'YamlItem')",
   "key": "[\"members\", [\"doc/en/example/nonpython/conftest.py\", \"YamlItem\"]]",
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
     "members",
     "doc/en/example/nonpython/conftest.py",
     "YamlItem"
    ]
   ]
  },
  {
   "call": "members('src/_pytest/doctest.py', 'DoctestItem')",
   "key": "[\"members\", [\"src/_pytest/doctest.py\", \"DoctestItem\"]]",
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
     "members",
     "src/_pytest/doctest.py",
     "DoctestItem"
    ]
   ]
  },
  {
   "call": "members('testing/example_scripts/fixtures/custom_item/conftest.py', 'CustomItem')",
   "key": "[\"members\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\", \"CustomItem\"]]",
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
     "members",
     "testing/example_scripts/fixtures/custom_item/conftest.py",
     "CustomItem"
    ]
   ]
  },
  {
   "call": "members('testing/example_scripts/issue88_initial_file_multinodes/conftest.py', 'MyItem')",
   "key": "[\"members\", [\"testing/example_scripts/issue88_initial_file_multinodes/conftest.py\", \"MyItem\"]]",
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
     "members",
     "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
     "MyItem"
    ]
   ]
  }
 ],
 "choice": {
  "call": "members('testing/example_scripts/issue88_initial_file_multinodes/conftest.py', 'MyItem')",
  "key": "[\"members\", [\"testing/example_scripts/issue88_initial_file_multinodes/conftest.py\", \"MyItem\"]]",
  "provenance": "the members `MyItem` defines itself (step 1)",
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
  "ok": "[\"members\", [\"doc/en/example/nonpython/conftest.py\", \"YamlItem\"]]",
  "cap": "[\"members\", [\"doc/en/example/nonpython/conftest.py\", \"YamlItem\"]]"
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
   "kind": "members",
   "step": 22,
   "path": "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
   "cls": "MyItem",
   "entries": [
    [
     17,
     "def",
     "runtest"
    ]
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "not_overriding",
  "step": 2,
  "of": 2,
  "table": [
   [
    "doc/en/example/nonpython/conftest.py",
    "YamlItem",
    "pending",
    "members not yet seen"
   ],
   [
    "src/_pytest/doctest.py",
    "DoctestItem",
    "pending",
    "members not yet seen"
   ],
   [
    "testing/example_scripts/fixtures/custom_item/conftest.py",
    "CustomItem",
    "pending",
    "members not yet seen"
   ],
   [
    "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
    "MyItem",
    "in",
    "does not define `reportinfo`"
   ]
  ],
  "n_in": 1,
  "n_out": 0,
  "n_pending": 3
 }
}
```
</details>

## Step 23

`MyItem` defines `runtest`, but no `reportinfo`, so it inherits it.

Tally: 1 classes without their own method confirmed, 0 ruled out, 3 pending.

I'll check `YamlItem`'s own members in `doc/en/example/nonpython/conftest.py`; only its own members tell me whether it overrides. Almost certainly the members fit. If there are too many members, I will check `DoctestItem`'s own members in `src/_pytest/doctest.py`.

**Call:** `members('doc/en/example/nonpython/conftest.py', 'YamlItem')`

**Response**: outcome `ok`

```
class YamlItem in doc/en/example/nonpython/conftest.py definitions=1
23 def __init__
27 def runtest
33 def repr_failure
45 def reportinfo
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "members",
   "key": [
    "members",
    "doc/en/example/nonpython/conftest.py",
    "YamlItem"
   ],
   "desc": "look at what `YamlItem` in `doc/en/example/nonpython/conftest.py` defines itself"
  },
  {
   "kind": "members",
   "key": [
    "members",
    "src/_pytest/doctest.py",
    "DoctestItem"
   ],
   "desc": "look at what `DoctestItem` in `src/_pytest/doctest.py` defines itself"
  },
  {
   "kind": "members",
   "key": [
    "members",
    "testing/example_scripts/fixtures/custom_item/conftest.py",
    "CustomItem"
   ],
   "desc": "look at what `CustomItem` in `testing/example_scripts/fixtures/custom_item/conftest.py` defines itself"
  }
 ],
 "candidates": [
  {
   "call": "members('doc/en/example/nonpython/conftest.py', 'YamlItem')",
   "key": "[\"members\", [\"doc/en/example/nonpython/conftest.py\", \"YamlItem\"]]",
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
     "members",
     "doc/en/example/nonpython/conftest.py",
     "YamlItem"
    ]
   ]
  },
  {
   "call": "members('src/_pytest/doctest.py', 'DoctestItem')",
   "key": "[\"members\", [\"src/_pytest/doctest.py\", \"DoctestItem\"]]",
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
     "members",
     "src/_pytest/doctest.py",
     "DoctestItem"
    ]
   ]
  },
  {
   "call": "members('testing/example_scripts/fixtures/custom_item/conftest.py', 'CustomItem')",
   "key": "[\"members\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\", \"CustomItem\"]]",
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
     "members",
     "testing/example_scripts/fixtures/custom_item/conftest.py",
     "CustomItem"
    ]
   ]
  }
 ],
 "choice": {
  "call": "members('doc/en/example/nonpython/conftest.py', 'YamlItem')",
  "key": "[\"members\", [\"doc/en/example/nonpython/conftest.py\", \"YamlItem\"]]",
  "provenance": "the members `YamlItem` defines itself (step 1)",
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
  "ok": "[\"members\", [\"src/_pytest/doctest.py\", \"DoctestItem\"]]",
  "cap": "[\"members\", [\"src/_pytest/doctest.py\", \"DoctestItem\"]]"
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
  "planned": "[\"members\", [\"doc/en/example/nonpython/conftest.py\", \"YamlItem\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "members",
   "step": 23,
   "path": "doc/en/example/nonpython/conftest.py",
   "cls": "YamlItem",
   "entries": [
    [
     23,
     "def",
     "__init__"
    ],
    [
     27,
     "def",
     "runtest"
    ],
    [
     33,
     "def",
     "repr_failure"
    ],
    [
     45,
     "def",
     "reportinfo"
    ]
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "not_overriding",
  "step": 2,
  "of": 2,
  "table": [
   [
    "doc/en/example/nonpython/conftest.py",
    "YamlItem",
    "out",
    "defines `reportinfo` itself"
   ],
   [
    "src/_pytest/doctest.py",
    "DoctestItem",
    "pending",
    "members not yet seen"
   ],
   [
    "testing/example_scripts/fixtures/custom_item/conftest.py",
    "CustomItem",
    "pending",
    "members not yet seen"
   ],
   [
    "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
    "MyItem",
    "in",
    "does not define `reportinfo`"
   ]
  ],
  "n_in": 1,
  "n_out": 1,
  "n_pending": 2
 }
}
```
</details>

## Step 24

`YamlItem` defines `reportinfo` itself (line 45), so it overrides.

Tally: 1 classes without their own method confirmed, 1 ruled out, 2 pending.

Let me check `DoctestItem`'s own members in `src/_pytest/doctest.py`; only its own members tell me whether it overrides. Almost certainly the members fit. If there are too many members, I will check `CustomItem`'s own members in `testing/example_scripts/fixtures/custom_item/conftest.py`.

**Call:** `members('src/_pytest/doctest.py', 'DoctestItem')`

**Response**: outcome `ok`

```
class DoctestItem in src/_pytest/doctest.py definitions=1
253 def __init__
273 def from_parent
285 def _initrequest
289 def setup
296 def runtest
306 def _disable_output_capturing_for_darwin
318 def repr_failure
382 def reportinfo
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "members",
   "key": [
    "members",
    "src/_pytest/doctest.py",
    "DoctestItem"
   ],
   "desc": "look at what `DoctestItem` in `src/_pytest/doctest.py` defines itself"
  },
  {
   "kind": "members",
   "key": [
    "members",
    "testing/example_scripts/fixtures/custom_item/conftest.py",
    "CustomItem"
   ],
   "desc": "look at what `CustomItem` in `testing/example_scripts/fixtures/custom_item/conftest.py` defines itself"
  }
 ],
 "candidates": [
  {
   "call": "members('src/_pytest/doctest.py', 'DoctestItem')",
   "key": "[\"members\", [\"src/_pytest/doctest.py\", \"DoctestItem\"]]",
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
     "members",
     "src/_pytest/doctest.py",
     "DoctestItem"
    ]
   ]
  },
  {
   "call": "members('testing/example_scripts/fixtures/custom_item/conftest.py', 'CustomItem')",
   "key": "[\"members\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\", \"CustomItem\"]]",
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
     "members",
     "testing/example_scripts/fixtures/custom_item/conftest.py",
     "CustomItem"
    ]
   ]
  }
 ],
 "choice": {
  "call": "members('src/_pytest/doctest.py', 'DoctestItem')",
  "key": "[\"members\", [\"src/_pytest/doctest.py\", \"DoctestItem\"]]",
  "provenance": "the members `DoctestItem` defines itself (step 1)",
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
  "ok": "[\"members\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\", \"CustomItem\"]]",
  "cap": "[\"members\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\", \"CustomItem\"]]"
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
  "planned": "[\"members\", [\"src/_pytest/doctest.py\", \"DoctestItem\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "members",
   "step": 24,
   "path": "src/_pytest/doctest.py",
   "cls": "DoctestItem",
   "entries": [
    [
     253,
     "def",
     "__init__"
    ],
    [
     273,
     "def",
     "from_parent"
    ],
    [
     285,
     "def",
     "_initrequest"
    ],
    [
     289,
     "def",
     "setup"
    ],
    [
     296,
     "def",
     "runtest"
    ],
    [
     306,
     "def",
     "_disable_output_capturing_for_darwin"
    ],
    [
     318,
     "def",
     "repr_failure"
    ],
    [
     382,
     "def",
     "reportinfo"
    ]
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "not_overriding",
  "step": 2,
  "of": 2,
  "table": [
   [
    "doc/en/example/nonpython/conftest.py",
    "YamlItem",
    "out",
    "defines `reportinfo` itself"
   ],
   [
    "src/_pytest/doctest.py",
    "DoctestItem",
    "out",
    "defines `reportinfo` itself"
   ],
   [
    "testing/example_scripts/fixtures/custom_item/conftest.py",
    "CustomItem",
    "pending",
    "members not yet seen"
   ],
   [
    "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
    "MyItem",
    "in",
    "does not define `reportinfo`"
   ]
  ],
  "n_in": 1,
  "n_out": 2,
  "n_pending": 1
 }
}
```
</details>

## Step 25

`DoctestItem` defines `reportinfo` itself (line 382), so it overrides.

Tally: 1 classes without their own method confirmed, 2 ruled out, 1 pending.

Let me check `CustomItem`'s own members in `testing/example_scripts/fixtures/custom_item/conftest.py`; only its own members tell me whether it overrides. Almost certainly the members fit. If there are too many members, I follow whatever it opens up.

**Call:** `members('testing/example_scripts/fixtures/custom_item/conftest.py', 'CustomItem')`

**Response**: outcome `ok`

```
class CustomItem in testing/example_scripts/fixtures/custom_item/conftest.py definitions=1
8 def runtest
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "members",
   "key": [
    "members",
    "testing/example_scripts/fixtures/custom_item/conftest.py",
    "CustomItem"
   ],
   "desc": "look at what `CustomItem` in `testing/example_scripts/fixtures/custom_item/conftest.py` defines itself"
  }
 ],
 "candidates": [
  {
   "call": "members('testing/example_scripts/fixtures/custom_item/conftest.py', 'CustomItem')",
   "key": "[\"members\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\", \"CustomItem\"]]",
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
     "members",
     "testing/example_scripts/fixtures/custom_item/conftest.py",
     "CustomItem"
    ]
   ]
  }
 ],
 "choice": {
  "call": "members('testing/example_scripts/fixtures/custom_item/conftest.py', 'CustomItem')",
  "key": "[\"members\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\", \"CustomItem\"]]",
  "provenance": "the members `CustomItem` defines itself (step 1)",
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
  "planned": "[\"members\", [\"testing/example_scripts/fixtures/custom_item/conftest.py\", \"CustomItem\"]]",
  "status": "followed"
 },
 "facts": [
  {
   "kind": "members",
   "step": 25,
   "path": "testing/example_scripts/fixtures/custom_item/conftest.py",
   "cls": "CustomItem",
   "entries": [
    [
     8,
     "def",
     "runtest"
    ]
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "not_overriding",
  "step": 2,
  "of": 2,
  "table": [
   [
    "doc/en/example/nonpython/conftest.py",
    "YamlItem",
    "out",
    "defines `reportinfo` itself"
   ],
   [
    "src/_pytest/doctest.py",
    "DoctestItem",
    "out",
    "defines `reportinfo` itself"
   ],
   [
    "testing/example_scripts/fixtures/custom_item/conftest.py",
    "CustomItem",
    "in",
    "does not define `reportinfo`"
   ],
   [
    "testing/example_scripts/issue88_initial_file_multinodes/conftest.py",
    "MyItem",
    "in",
    "does not define `reportinfo`"
   ]
  ],
  "n_in": 2,
  "n_out": 2,
  "n_pending": 0
 }
}
```
</details>

## Final

4 classes derive from it directly: `YamlItem` (`doc/en/example/nonpython/conftest.py:22`), `DoctestItem` (`src/_pytest/doctest.py:252`), `CustomItem` (`testing/example_scripts/fixtures/custom_item/conftest.py:7`), `MyItem` (`testing/example_scripts/issue88_initial_file_multinodes/conftest.py:16`). 2 of the subclasses do not define `reportinfo` themselves: `CustomItem`, `MyItem`. Ruled out along the way: `src/_pytest/python.py:1650:Function` (base `nodes.Item` resolves to unresolved(`nodes` is not a module)). Looking back, 2 of 25 calls did not end up mattering (steps 7, 8).

**Answer:** `{"final_kind": "not_overriding", "final": ["testing/example_scripts/fixtures/custom_item/conftest.py:7:CustomItem", "testing/example_scripts/issue88_initial_file_multinodes/conftest.py:16:MyItem"], "steps": [{"op": "subclasses", "output": ["doc/en/example/nonpython/conftest.py:22:YamlItem", "src/_pytest/doctest.py:252:DoctestItem", "testing/example_scripts/fixtures/custom_item/conftest.py:7:CustomItem", "testing/example_scripts/issue88_initial_file_multinodes/conftest.py:16:MyItem"]}, {"op": "not_overriding", "output": ["testing/example_scripts/fixtures/custom_item/conftest.py:7:CustomItem", "testing/example_scripts/issue88_initial_file_multinodes/conftest.py:16:MyItem"]}], "stuck": null}`  
**Stopped:** certificate after 25 calls