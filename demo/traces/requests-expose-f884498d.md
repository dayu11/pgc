# requests-expose-f884498d

**Repository:** requests  
**Chain:** expose  
**Seed:** 0, prior 736169d01b033d9f, floor 2

## Task

`InvalidProxyURL` is defined at `src/requests/exceptions.py:126` (class). Propose the one-line change to `src/requests/__init__.py` that makes `from requests import InvalidProxyURL` resolve to this definition; give the exact line to append.

*Declared semantics:* A module is a .py file; source roots are the repository root and, if present, src/ and lib/. `from M import N` binds N to M's single module-level binding of N, else to the submodule M/N, else to the single star-import source of M that exports N; bindings take effect in source order. A module exports N if its literal __all__ lists N or, without __all__, if N is public and bound in it. A class derives from a definition when a base written as a bare name or `module.Name` resolves to it. A call site is `name(...)` where the bare name refers to the module-level binding (not a parameter or local). Multiple bindings, non-literal __all__, external star imports and dynamic namespace code make a name ambiguous; tasks never ask about ambiguous names.

## Step 1

Starting from the definition of `InvalidProxyURL` at `src/requests/exceptions.py:126`. Then I have to propose the one-line import that exposes it from the package.

Next I will look at `src/requests/__init__.py`'s top-level names for `InvalidProxyURL`; that settles what the name means there. Probably it is re-exported from somewhere else. If the name is not bound there, I follow whatever it opens up; if it is defined right there, that finishes it. I could outline all of `src/requests/__init__.py` instead, but it is more likely to hit the cap.

**Call:** `symbols('src/requests/__init__.py', 'InvalidProxyURL')`

**Response**: outcome `none`

```
module src/requests/__init__.py lines=220 dynamic=no all=static@188
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "bindings",
   "key": [
    "bindings",
    "src/requests/__init__.py",
    "InvalidProxyURL"
   ],
   "desc": "check the top-level names of `src/requests/__init__.py` for `InvalidProxyURL`"
  }
 ],
 "candidates": [
  {
   "call": "symbols('src/requests/__init__.py', 'InvalidProxyURL')",
   "key": "[\"symbols\", [\"src/requests/__init__.py\", \"InvalidProxyURL\"]]",
   "v1": [
    1183549,
    470307
   ],
   "v2": [
    1183549,
    470307
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     9,
     74
    ],
    "reexport": [
     45,
     74
    ],
    "star": [
     1,
     74
    ],
    "none": [
     19,
     74
    ]
   },
   "serves": [
    [
     "bindings",
     "src/requests/__init__.py",
     "InvalidProxyURL"
    ]
   ]
  },
  {
   "call": "symbols('src/requests/__init__.py')",
   "key": "[\"symbols\", [\"src/requests/__init__.py\"]]",
   "v1": [
    8755150,
    3292149
   ],
   "v2": [
    8755150,
    3292149
   ],
   "p_cap": [
    1,
    7
   ],
   "forecast": {
    "def": [
     27,
     259
    ],
    "reexport": [
     135,
     259
    ],
    "star": [
     3,
     259
    ],
    "none": [
     57,
     259
    ],
    "cap": [
     1,
     7
    ]
   },
   "serves": [
    [
     "bindings",
     "src/requests/__init__.py",
     "InvalidProxyURL"
    ]
   ]
  }
 ],
 "choice": {
  "call": "symbols('src/requests/__init__.py', 'InvalidProxyURL')",
  "key": "[\"symbols\", [\"src/requests/__init__.py\", \"InvalidProxyURL\"]]",
  "provenance": "module `src/requests/__init__.py` (task), name `InvalidProxyURL` (task)",
  "v2": [
   1183549,
   470307
  ]
 },
 "forecast": {
  "def": [
   9,
   74
  ],
  "reexport": [
   45,
   74
  ],
  "star": [
   1,
   74
  ],
  "none": [
   19,
   74
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
    45,
    74
   ]
  }
 ],
 "adherence": null,
 "facts": [
  {
   "kind": "outline",
   "step": 1,
   "path": "src/requests/__init__.py",
   "filter": "InvalidProxyURL",
   "header": {
    "lines": 220,
    "dynamic": false,
    "all_status": "static",
    "all_line": 188
   },
   "bindings": [],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "expose",
  "step": 1,
  "of": 1,
  "package": "src/requests/__init__.py",
  "bound": null,
  "spec": ".exceptions"
 }
}
```
</details>

## Step 2

The package `src/requests` does not bind `InvalidProxyURL`; for a package that leaves a submodule called `InvalidProxyURL` as the only option.

Let me list `src/requests/` to see what lives there; a package that does not bind the name could still have a submodule called that. Almost certainly the listing fits. If the listing is too long, I will outline `src/requests/InvalidProxyURL.py` directly, which both checks that the file exists and shows me `InvalidProxyURL`. I could outline `src/requests/InvalidProxyURL.py` directly, which both checks that the file exists and shows me `InvalidProxyURL` instead, but it tends to open more follow-up work.

**Call:** `ls('src/requests')`

**Response**: outcome `complete`

```
__init__.py
__version__.py
_internal_utils.py
_types.py
adapters.py
api.py
auth.py
certs.py
compat.py
cookies.py
exceptions.py
help.py
hooks.py
models.py
packages.py
sessions.py
status_codes.py
structures.py
utils.py
```

<details><summary>sidecar</summary>

```json
{
 "items": [
  {
   "kind": "submodule",
   "key": [
    "submodule",
    "src/requests/__init__.py",
    "InvalidProxyURL"
   ],
   "desc": "check whether `src/requests` has a submodule `InvalidProxyURL`"
  }
 ],
 "candidates": [
  {
   "call": "ls('src/requests')",
   "key": "[\"ls\", [\"src/requests\"]]",
   "v1": [
    43,
    42
   ],
   "v2": [
    24296341426,
    23645416311
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
     "submodule",
     "src/requests/__init__.py",
     "InvalidProxyURL"
    ]
   ]
  },
  {
   "call": "symbols('src/requests/InvalidProxyURL.py', 'InvalidProxyURL')",
   "key": "[\"symbols\", [\"src/requests/InvalidProxyURL.py\", \"InvalidProxyURL\"]]",
   "v1": [
    9112951610,
    7881805437
   ],
   "v2": [
    383822210753,
    331035828354
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     191744,
     234069
    ],
    "reexport": [
     1792,
     234069
    ],
    "star": [
     448,
     234069
    ],
    "none": [
     2688,
     78023
    ],
    "missing": [
     71,
     519
    ]
   },
   "serves": [
    [
     "submodule",
     "src/requests/__init__.py",
     "InvalidProxyURL"
    ]
   ]
  },
  {
   "call": "symbols('src/requests/InvalidProxyURL/__init__.py', 'InvalidProxyURL')",
   "key": "[\"symbols\", [\"src/requests/InvalidProxyURL/__init__.py\", \"InvalidProxyURL\"]]",
   "v1": [
    505427051,
    244089333
   ],
   "v2": [
    510443659,
    244089333
   ],
   "p_cap": [
    0,
    1
   ],
   "forecast": {
    "def": [
     213,
     12802
    ],
    "reexport": [
     1065,
     12802
    ],
    "star": [
     71,
     38406
    ],
    "none": [
     1349,
     38406
    ],
    "missing": [
     448,
     519
    ]
   },
   "serves": [
    [
     "submodule",
     "src/requests/__init__.py",
     "InvalidProxyURL"
    ]
   ]
  }
 ],
 "choice": {
  "call": "ls('src/requests')",
  "key": "[\"ls\", [\"src/requests\"]]",
  "provenance": "package directory of `src/requests/__init__.py`",
  "v2": [
   24296341426,
   23645416311
  ]
 },
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
 "plan": {
  "complete": "done",
  "cap": "[\"symbols\", [\"src/requests/InvalidProxyURL.py\", \"InvalidProxyURL\"]]"
 },
 "hedges": [
  {
   "outcome": "complete",
   "word": "almost certainly",
   "p": [
    41,
    42
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
   "dir": "src/requests",
   "entries": [
    "__init__.py",
    "__version__.py",
    "_internal_utils.py",
    "_types.py",
    "adapters.py",
    "api.py",
    "auth.py",
    "certs.py",
    "compat.py",
    "cookies.py",
    "exceptions.py",
    "help.py",
    "hooks.py",
    "models.py",
    "packages.py",
    "sessions.py",
    "status_codes.py",
    "structures.py",
    "utils.py"
   ],
   "complete": true
  }
 ],
 "goal_state": {
  "phase": "expose",
  "step": 1,
  "of": 1,
  "package": "src/requests/__init__.py",
  "bound": false,
  "spec": ".exceptions"
 }
}
```
</details>

## Final

Patch: append `from .exceptions import InvalidProxyURL` to `src/requests/__init__.py`. The package does not bind `InvalidProxyURL` today and is not dynamic, so after that line `from requests import InvalidProxyURL` resolves to the definition. Looking back, all 2 calls were needed.

**Answer:** `{"final_kind": "expose", "final": {"patch": {"path": "src/requests/__init__.py", "append": "from .exceptions import InvalidProxyURL"}, "claim": "after the patch, `InvalidProxyURL` in `src/requests/__init__.py` resolves to src/requests/exceptions.py:126"}, "steps": [{"op": "expose", "output": {"patch": {"path": "src/requests/__init__.py", "append": "from .exceptions import InvalidProxyURL"}, "claim": "after the patch, `InvalidProxyURL` in `src/requests/__init__.py` resolves to src/requests/exceptions.py:126"}}], "stuck": null}`  
**Stopped:** certificate after 2 calls