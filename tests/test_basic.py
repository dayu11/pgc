"""Self-contained checks on a synthetic mini-repository (no corpus needed).
Run: python -m pytest -q tests  (or python tests/test_basic.py)"""
import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pgc.analysis import Index, Target
from pgc.knowledge import parse_line, parse_all_list
from pgc.prior import Prior, fit_prior
from pgc.runner import LiveSource, run
from pgc.snapshot import Call, Snapshot
from pgc.verify import replay, world_check

FILES = {
    "src/pkg/__init__.py": "from .core import Widget\nfrom ._util import *\n__all__ = ['Widget', 'helper']\n",
    "src/pkg/core.py": "class Base:\n    pass\n\nclass Widget(Base):\n    '''doc'''\n    def run(self):\n        return 1\n",
    "src/pkg/_util.py": "__all__ = ['helper']\n\ndef helper():\n    return 2\n\ndef _private():\n    return 3\n",
    "src/pkg/ui.py": "from pkg import Widget as W\nfrom .core import (\n    Base,\n    Widget,\n)\n",
    "tests/fixtures.py": "class Widget:\n    pass\n",
    "tests/test_widget.py": "from pkg import Widget\nfrom .fixtures import Widget as Fake\nfrom pkg import helper\n",
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


class TestAnalysis(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.snap = make_repo(self.tmp)
        self.ix = Index(self.snap)

    def test_resolution_chain_and_star(self):
        self.assertEqual(str(self.ix.resolve("tests/test_widget.py", "Widget")), "src/pkg/core.py:4")
        self.assertEqual(str(self.ix.resolve("tests/test_widget.py", "Fake")), "tests/fixtures.py:1")
        self.assertEqual(str(self.ix.resolve("src/pkg/ui.py", "W")), "src/pkg/core.py:4")
        # helper reaches _util through the star import of pkg/__init__
        self.assertEqual(str(self.ix.resolve("tests/test_widget.py", "helper")), "src/pkg/_util.py:3")

    def test_importers(self):
        tgt = self.ix.resolve("src/pkg/core.py", "Widget")
        imps = self.ix.importers_of(tgt)
        self.assertEqual(sorted((p, l) for p, l, _, _ in imps), [("src/pkg/__init__.py", 1), ("src/pkg/ui.py", 1), ("src/pkg/ui.py", 2), ("tests/test_widget.py", 1)])

    def test_tools_deterministic_and_capped(self):
        r1 = self.snap.call(Call("grep", (r"Widget", ".")))
        r2 = self.snap.call(Call("grep", (r"Widget", ".")))
        self.assertEqual(r1, r2)
        self.assertFalse(r1.capped)
        sym = self.snap.call(Call("symbols", ("src/pkg/__init__.py", "Widget")))
        self.assertTrue(sym.lines[0].startswith("module src/pkg/__init__.py"))
        self.assertIn("1 from Widget <- .core Widget", sym.lines)


class TestEndToEnd(unittest.TestCase):
    def test_run_replay_verify(self):
        tmp = tempfile.mkdtemp()
        snap = make_repo(tmp)
        ix = Index(snap)
        repos = {"mini": (snap, ix), "mini2": (snap, ix)}
        prior = Prior(fit_prior(repos, exclude="mini", samples_per_repo=5))
        task = {"id": "t", "repo": "mini", "family": "composite", "text": "x", "semantics": "v0",
                "given": {"module": "tests/test_widget.py", "line": 1, "name": "Widget", "spec": "pkg", "src_name": "Widget"}}
        tr = run(task, LiveSource(snap), prior, seed=3, budget=30)
        self.assertEqual(tr["stopped"], "certificate")
        self.assertEqual(tr["answer"]["text"], "src/pkg/core.py:4")
        self.assertEqual(tr["answer"]["statements"], ["src/pkg/__init__.py:1", "src/pkg/ui.py:1", "src/pkg/ui.py:2", "tests/test_widget.py:1"])
        self.assertTrue(replay(tr, prior)["ok"])
        wc = world_check(tr, snap, ix)
        self.assertTrue(wc["ok"], wc["failures"])
        # the decoy in tests/fixtures.py must have been ruled out with a reason, not ignored
        verdicts = tr["steps"][-1]["goal_state"]["verdicts"]
        outs = [v for v in verdicts if v[2] == "out"]
        self.assertTrue(any("fixtures" in v[3] for v in outs), verdicts)
        # grounded: every path named in a call was seen before the call
        seen = set(str(v) for v in task["given"].values())
        for st in tr["steps"]:
            for a in st["call"]["args"]:
                if isinstance(a, str) and "/" in a and not a.startswith("^"):
                    self.assertTrue(any(a == s or a.startswith(s.rsplit("/", 1)[0]) for s in seen) or a in seen, a)
            for line in st["response"]["lines"]:
                seen.add(line.split(":", 1)[0])
                for tok in line.replace(":", " ").split():
                    seen.add(tok)


if __name__ == "__main__":
    unittest.main()
