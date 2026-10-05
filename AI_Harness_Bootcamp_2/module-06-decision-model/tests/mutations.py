#!/usr/bin/env python3
"""Mutation corpus: each item must make test_module_06.py FAIL its named check."""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Callable


@dataclass(frozen=True)
class Mutation:
    cid: str
    what: str
    apply: Callable[[Path], None]


def sub(rel: str, pattern: str, repl: str) -> Callable[[Path], None]:
    def go(root: Path) -> None:
        path = root / rel
        text = path.read_text(encoding="utf-8")
        new, count = re.subn(pattern, repl, text, count=1, flags=re.M)
        if count == 0:
            raise AssertionError(f"mutation anchor {pattern!r} not found in {rel}")
        path.write_text(new, encoding="utf-8")
    return go


def edit_json(rel: str, change: Callable[[dict], None]) -> Callable[[Path], None]:
    def go(root: Path) -> None:
        path = root / rel
        data = json.loads(path.read_text(encoding="utf-8"))
        change(data)
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return go


def remove(rel: str) -> Callable[[Path], None]:
    return lambda root: (root / rel).unlink()


SCRIPT = "scripts/blue_gauge.py"
MUTATIONS = [
    Mutation("M6-REF", "the frozen reference changes after its digest", sub("reference/REFERENCE.md", r"\Z", "\nAn unfrozen line.\n")),
    Mutation("M6-CASE", "a held-out note disappears", remove("shared/case/notes/held-out/BG-080.json")),
    Mutation("M6-STATE", "the scan record leaks into the model's state", edit_json("shared/case/notes/tuning/BG-002.json", lambda data: data["state"].update(scan="RECEIVED"))),
    Mutation("M6-QUESTIONS", "the checker stops comparing the twin's option order", sub(SCRIPT, r"if list\(reverse\) != list\(reversed\(list\(status\)\)\) or ", "if ")),
    Mutation("M6-ROUTE", "the instruction check stops taking precedence", sub(SCRIPT, r'if answers\["instructs_reader"\]\["bool"\] >= t\["instruction_review"\]:', "if False:")),
    Mutation("M6-PREP", "the selection form is not supplied", remove("shared/controls/SELECTION.template.md")),
    Mutation("M6-FREEZE", "a freeze no longer compares the tuning run's questions", sub(SCRIPT, r'if digest\(evidence / args\.tuning_run / "questions\.json"\) != digest\(work / "QUESTIONS\.json"\):', "if False:")),
    Mutation("M6-MEASURE", "a held-out run that started before the freeze is measured anyway", sub(SCRIPT, r'if result\["started_at"\] <= freeze\["created_at"\]:', "if False:")),
    Mutation("M6-VERIFY", "first-miss notes are no longer compared with the misses", sub(SCRIPT, r'problems = \[f"first-misses\.md does not mention \{key\}" for key in missed if key not in notes\]', "problems = []")),
    Mutation("M6-LEARNER", "staff wording reaches the lab", sub("shared/MODULE_06_LAB.md", r"\Z", "\nThe answer key is in WORKED_QUESTIONS.\n")),
]
