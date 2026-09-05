"""Self-contained checks on a synthetic mini-repository (no corpus needed).
Run: python tests/test_basic.py"""
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pgc.analysis import Index, Target, parse_module
from pgc.knowledge import parse_all_list, parse_line
from pgc.prior import Prior, fit_prior
from pgc.runner import LiveSource, run
from pgc.snapshot import Call, Snapshot
from pgc.verify import check_patch, replay, world_check

FILES = {
    "src/pkg/__init__.py": "from .core import Widget\nfrom ._util import *\n__all__ = ['Widget', 'helper']\n",
    "src/pkg/core.py": "class Base:\n    def run(self):\n        return 0\n\nclass Widget(Base):\n    '''doc'''\n    def run(self):\n        return 1\n\nclass Panel(Base):\n    pass\n",
    "src/pkg/_util.py": "__all__ = ['helper']\n\ndef helper():\n    return 2\n\ndef _private():\n    return 3\n",
    "src/pkg/ui.py": "from pkg import Widget as W\nfrom .core import (\n    Base,\n    Widget,\n)\nimport pkg.core\n\nclass Dialog(Base):\n    def run(self):\n        return 2\n\nclass Frame(pkg.core.Base):\n    pass\n\ndef make():\n    return Widget()\n\ndef shadow(Widget):\n    return Widget()\n",
    "src/pkg/sub/__init__.py": "",
    "tests/fixtures.py": "class Widget:\n    pass\n\nclass Base:\n    pass\n\nclass FakeThing(Base):\n    pass\n",
    "tests/test_widget.py": "from pkg import Widget\nfrom .fixtures import Widget as Fake\nfrom pkg import helper\n\ndef test():\n    w = Widget()\n    return helper(), Fake()\n",
    "tests/__init__.py": "",
    "docs/guide.md": "Use `from pkg import Widget`.\n",
}


def make_repo(tmp):
    for rel, text in FILES.items():
        p = os.path.join(tmp, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w") as f:
            f.write(text)
    return Snapshot(tmp, "mini")


class TestParsing(unittest.TestCase):
    def test_parse_line(self):
        bs, inc = parse_line("f.py", 1, "from .models import Response, Request as R  # c")
        self.assertEqual([(b.name, b.src_name) for b in bs], [("Response", "Response"), ("R", "Request")])
        self.assertIsNone(inc)
        bs, inc = parse_line("f.py", 2, "from x import (")
        self.assertIsNotNone(inc)
        self.assertEqual(parse_all_list(["__all__ = [", " 'a',", "]"]), ["a"])

    def test_scope_exact_calls(self):
        src = "import f\ndef g(f):\n    return f(1)\ndef h():\n    return f(2)\nclass C:\n    y = f(3)\nlam = lambda: f(4)\n[f(5) for _ in range(2)]\ndef k():\n    f = 1\n    return [f(6) for _ in range(2)]\n"
        mi = parse_module("m.py", src)
        self.assertEqual(mi.calls["f"], [5, 7, 8, 9])
        self.assertFalse(mi.calls_unsure)


class TestAnalysis(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.snap = make_repo(self.tmp)
        self.ix = Index(self.snap)

    def test_resolution_chain_and_star(self):
        self.assertEqual(str(self.ix.resolve("tests/test_widget.py", "Widget")), "src/pkg/core.py:5")
        self.assertEqual(str(self.ix.resolve("tests/test_widget.py", "Fake")), "tests/fixtures.py:1")
        self.assertEqual(str(self.ix.resolve("src/pkg/ui.py", "W")), "src/pkg/core.py:5")
        self.assertEqual(str(self.ix.resolve("tests/test_widget.py", "helper")), "src/pkg/_util.py:3")

    def test_importers_subclasses_callers(self):
        tgt = self.ix.resolve("src/pkg/core.py", "Widget")
        self.assertEqual(sorted((p, l) for p, l, _, _ in self.ix.importers_of(tgt)), [("src/pkg/__init__.py", 1), ("src/pkg/ui.py", 1), ("src/pkg/ui.py", 2), ("tests/test_widget.py", 1)])
        base = self.ix.resolve("src/pkg/core.py", "Base")
        subs = self.ix.subclasses_of(base)
        self.assertEqual(sorted(c for _, _, c in subs), ["Dialog", "Frame", "Panel", "Widget"])  # FakeThing derives from the fixture Base
        # callers of Widget: ui.make (module-level binding), test_widget.test; not shadow's parameter
        self.assertEqual(self.ix.callers_of(tgt), [("src/pkg/ui.py", 16), ("tests/test_widget.py", 6)])

    def test_tools(self):
        sym = self.snap.call(Call("symbols", ("src/pkg/ui.py", "Base")))
        self.assertIn("8 class Dialog (Base)", sym.lines)
        self.assertIn("12 class Frame (pkg.core.Base)", sym.lines)
        mem = self.snap.call(Call("members", ("src/pkg/core.py", "Panel")))
        self.assertEqual(mem.lines[1:], ())
        calls = self.snap.call(Call("calls", ("src/pkg/ui.py", "Widget")))
        self.assertEqual([l.split(":")[0] for l in calls.lines[1:]], ["16"])


class TestEndToEnd(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.snap = make_repo(self.tmp)
        self.ix = Index(self.snap)
        repos = {"mini": (self.snap, self.ix), "mini2": (self.snap, self.ix)}
        self.prior = Prior(fit_prior(repos, exclude="mini", samples_per_repo=5))

    def _task(self, chain, given, tid):
        return {"id": tid, "repo": "mini", "family": chain[-1]["op"], "text": "x", "semantics": "v0", "chain": chain, "given": given}

    def check(self, tr):
        self.assertEqual(tr["stopped"], "certificate", tr.get("open_at_stop"))
        self.assertTrue(replay(tr, self.prior)["ok"])
        wc = world_check(tr, self.snap, self.ix)
        self.assertTrue(wc["ok"], wc["failures"])
        for st in tr["steps"]:  # no lowercased identifiers leaking from sentence casing
            self.assertNotIn("`widget`", st["thought"])

    def test_resolve_importers(self):
        task = self._task([{"op": "resolve", "module": "tests/test_widget.py", "line": 1, "name": "Widget", "spec": "pkg", "src_name": "Widget"}, {"op": "importers"}],
                          {"module": "tests/test_widget.py", "line": 1, "name": "Widget", "spec": "pkg", "src_name": "Widget"}, "t1")
        tr = run(task, LiveSource(self.snap), self.prior, seed=3, budget=30)
        self.check(tr)
        self.assertEqual(tr["answer"]["steps"][0]["output"]["line"], 5)
        self.assertEqual(tr["answer"]["final"], ["src/pkg/__init__.py:1", "src/pkg/ui.py:1", "src/pkg/ui.py:2", "tests/test_widget.py:1"])
        outs = [r for r in tr["certificate"][1]["counterexamples"]]
        self.assertTrue(any("fixtures" in r[3] or "fixtures" in r[0] for r in outs), outs)

    def test_subclasses_not_overriding(self):
        given = {"def_path": "src/pkg/core.py", "def_line": 1, "name": "Base", "def_kind": "class", "method": "run"}
        task = self._task([{"op": "subclasses", "def_path": "src/pkg/core.py", "def_line": 1, "name": "Base", "def_kind": "class"}, {"op": "not_overriding", "method": "run"}], given, "t2")
        tr = run(task, LiveSource(self.snap), self.prior, seed=1, budget=30)
        self.check(tr)
        self.assertEqual(tr["answer"]["steps"][0]["output"], ["src/pkg/core.py:5:Widget", "src/pkg/core.py:10:Panel", "src/pkg/ui.py:8:Dialog", "src/pkg/ui.py:12:Frame"])
        self.assertEqual(tr["answer"]["final"], ["src/pkg/core.py:10:Panel", "src/pkg/ui.py:12:Frame"])

    def test_callers(self):
        given = {"def_path": "src/pkg/core.py", "def_line": 5, "name": "Widget", "def_kind": "class"}
        task = self._task([{"op": "callers", **given}], given, "t3")
        tr = run(task, LiveSource(self.snap), self.prior, seed=2, budget=30)
        self.check(tr)
        self.assertEqual(tr["answer"]["final"], ["src/pkg/ui.py:16", "tests/test_widget.py:6"])

    def test_expose_patch(self):
        given = {"def_path": "src/pkg/_util.py", "def_line": 3, "name": "helper", "def_kind": "def", "package": "src/pkg/sub/__init__.py"}
        task = self._task([{"op": "expose", **given}], given, "t4")
        tr = run(task, LiveSource(self.snap), self.prior, seed=2, budget=30)
        self.check(tr)
        patch = tr["answer"]["final"]["patch"]
        self.assertEqual(patch["append"], "from .._util import helper")
        ok, detail = check_patch(self.snap, self.ix, "src/pkg/sub/__init__.py", "helper", {"kind": "def", "path": "src/pkg/_util.py", "line": 3, "name": "helper", "detail": "def"}, patch)
        self.assertTrue(ok, detail)


if __name__ == "__main__":
    unittest.main()
