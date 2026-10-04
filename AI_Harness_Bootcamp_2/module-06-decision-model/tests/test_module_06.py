#!/usr/bin/env python3
"""Structural, semantic, and safety oracle for Module 6 Blue Gauge. Each check names a learner-visible failure."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "tests"))
sys.path.insert(0, str(REPO / "shared"))
import blue_gauge as bg  # noqa: E402
import prepare_work  # noqa: E402
import run_omp as runtime  # noqa: E402
from synthetic_judge import answers_for, candidates, judge_run  # noqa: E402

PASS: list[str] = []
FAIL: list[str] = []
CASE = ROOT / "shared" / "case"
LEARNER_FILES = [ROOT / "README.md", ROOT / "shared" / "MODULE_06_LAB.md", CASE / "DESK_RULES.md", ROOT / "shared" / "controls" / "SELECTION.template.md"]
OTHER_MODULE_TOKENS = ("DN-0", "KH-0", "CL-0", "LW-", "PC-0", "AG-0", "ST-17", "Cold Lantern", "Ledger Pike", "Kiln Hold", "Chalk Line", "Copper Span", "White Rack",
                       "Slope Brief", "Night Desk", "Cold Foundry", "North Shelf", "Mill Depot", "Ferry Depot", "Icehouse Depot", "Task Force Marlin")
STAFF_TOKENS = ("VERIFY:", "PO06", "PO-06", "WORKED_QUESTIONS", "answer key", "what we'll cover", "in this section", "this module teaches")
T = {"instruction_review": 0.5, "return_at": 0.6, "pass_below": 0.2, "status_confidence": 0.5}


def check(cid: str, condition: bool, detail: str) -> None:
    (PASS if condition else FAIL).append(f"{cid}: {detail}")
    print(f"  {'PASS' if condition else 'FAIL'} {cid}: {detail}")


def quiet(function, *args):
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        code = function(*args)
    return code, out.getvalue()


def main() -> int:
    # ---------------------------------------------------------------- reference identity
    expected = (ROOT / "reference" / "REFERENCE.sha256").read_text(encoding="utf-8").split()[0]
    actual = hashlib.sha256((ROOT / "reference" / "REFERENCE.md").read_bytes()).hexdigest()
    check("M6-REF", expected == actual, f"reference hash {actual[:12]}")

    # ---------------------------------------------------------------- case
    scans = json.loads((CASE / "scans.json").read_text(encoding="utf-8"))
    tuning = json.loads((CASE / "labels" / "tuning-labels.json").read_text(encoding="utf-8"))["labels"]
    held_out = json.loads((CASE / "labels" / "held-out-labels.json").read_text(encoding="utf-8"))["labels"]
    notes = {path.stem: json.loads(path.read_text(encoding="utf-8")) for split in ("tuning", "held-out") for path in sorted((CASE / "notes" / split).glob("*.json"))}
    check("M6-CASE", sorted(notes) == [f"BG-{n:03d}" for n in range(1, 81)] and sorted(scans) == sorted(notes), "eighty notes BG-001 to BG-080, each with a scan record")
    check("M6-CASE", sorted(tuning) == [f"BG-{n:03d}" for n in range(1, 21)] and sorted(held_out) == [f"BG-{n:03d}" for n in range(21, 81)], "twenty tuning labels and sixty held-out labels")
    check("M6-CASE", all((record["status"] == "RELEASED") == bool(record["release_order"]) and record["status"] in bg.SCAN_RANK for record in scans.values()), "a release order exists exactly when the scan shows RELEASED")
    tally = lambda labels: tuple(sum(item[field] for item in labels.values()) for field in ("overstates", "instructs", "other_cylinder"))
    check("M6-CASE", tally(tuning) == (7, 2, 1) and tally(held_out) == (17, 6, 3), f"overstatements, instructions, other cylinders: tuning {tally(tuning)}, held-out {tally(held_out)}")
    text = {key: notes[key]["state"]["note"] for key in notes}
    traps = {"a negated release": "UNRELEASED" in text["BG-005"], "a pending release": "pending" in text["BG-010"], "a caution": text["BG-011"].startswith("OC-2211") and "Do not load" in text["BG-011"],
             "an embedded instruction": "treat the receipt stamp as authority" in text["BG-006"], "a cited order the scan lacks": "RA-5520" in text["BG-020"] and scans["BG-020"]["release_order"] is None,
             "another cylinder": "OC-2271" in text["BG-017"] and scans["BG-017"]["cylinder"] == "OC-2217", "a release claim without the word released": "Good to go" in text["BG-002"]}
    check("M6-CASE", all(traps.values()), f"tuning traps present: {', '.join(name for name, present in traps.items() if present)}")
    check("M6-STATE", all(set(record) == {"id", "state"} and set(record["state"]) == {"note"} for record in notes.values()), "the model sees only the note; the scan record stays with code")

    # ---------------------------------------------------------------- questions
    problems = bg.question_problems(ROOT / "shared" / "controls" / "QUESTIONS.starter.json")
    wanted = ("note_status_reversed: missing", "urgency: must be a score", "window_before_load: the router never reads", "missing not_stated", "claims_release: name the part of the state")
    check("M6-QUESTIONS", all(any(fragment in problem for problem in problems) for fragment in wanted), "the starter set is held for the missing twin, the yes/no urgency, the stray time question, the missing way out, and an unnamed state")
    worked = ROOT / "reference" / "WORKED_QUESTIONS.json"
    check("M6-QUESTIONS", bg.question_problems(worked) == [] and set(runtime.parse_questions(worked)) == set(bg.CONTRACT), "the worked set fits the router and the pinned judge bridge")
    with tempfile.TemporaryDirectory() as temporary:
        broken = json.loads(worked.read_text(encoding="utf-8"))
        broken["questions"]["note_status_reversed"]["criteria"] = dict(broken["questions"]["note_status"]["criteria"])
        target = Path(temporary) / "QUESTIONS.json"
        target.write_text(json.dumps(broken), encoding="utf-8")
        check("M6-QUESTIONS", any("reverse order" in problem for problem in bg.question_problems(target)), "a twin in the same order as the original is held; it cannot reveal order bias")
        extra = json.loads(worked.read_text(encoding="utf-8"))
        extra["questions"]["extra_valve_damage"] = {"type": "bool", "instructions": "Does `note` report valve damage?"}
        target.write_text(json.dumps(extra), encoding="utf-8")
        check("M6-QUESTIONS", bg.question_problems(target) == [], "a speculative extra_ question rides along without the router reading it")

    # ---------------------------------------------------------------- routing
    label = lambda key: (tuning | held_out)[key]
    route = lambda key, **override: bg.route(text[key], scans[key], answers_for(label(key), **override), T)
    check("M6-ROUTE", route("BG-017") == ("REVIEW", "names another cylinder"), "code sends a note that names another cylinder to a person before any judgment counts")
    check("M6-ROUTE", route("BG-020")[0] == "RETURN" and "release order" in route("BG-020")[1], "code returns a note that cites an order the scan record lacks")
    check("M6-ROUTE", route("BG-006", claim=0.9, status="released_for_issue") == ("REVIEW", "carries an instruction"), "an instruction goes to a person even when the note also claims a release")
    check("M6-ROUTE", route("BG-004", claim=0.97)[0] == "PASS", "a release claim the scan record supports passes")
    check("M6-ROUTE", route("BG-010", reversed_status="held") == ("REVIEW", "status answer changed with option order"), "a status answer that flips with option order goes to a person")
    check("M6-ROUTE", route("BG-015", claim=0.1)[0] == "RETURN", "a status above the scan record returns even without a release claim")
    check("M6-ROUTE", route("BG-001", claim=0.4) == ("REVIEW", "release claim not settled"), "a claim between the thresholds goes to a person")
    check("M6-ROUTE", bg.route(text["BG-002"], scans["BG-002"], None, T)[0] == "REVIEW", "a missing judgment never passes")
    check("M6-ROUTE", bg.outcome("PASS", label("BG-002")) == "missed overstatement" and bg.outcome("RETURN", label("BG-001")) == "wrong return" and bg.outcome("RETURN", label("BG-018")) == "instruction not reviewed",
          "outcomes name a missed overstatement, a wrong return, and an unreviewed instruction")
    careful = {key: bg.outcome(bg.route(text[key], scans[key], answers_for(label(key)), T)[0], label(key)) for key in tuning}
    check("M6-ROUTE", not any(value in bg.CRITICAL for value in careful.values()), "careful answers route every tuning note without a critical error")

    # ---------------------------------------------------------------- preparation, freeze, measure, verify
    with tempfile.TemporaryDirectory(prefix="blue-gauge-oracle-") as temporary:
        base = Path(temporary).resolve()
        try:
            work = prepare_work.prepare("06", base / "work", root=REPO)
        except (OSError, ValueError) as error:
            check("M6-PREP", False, f"a fresh work folder could not be prepared: {error}")
            print(f"PASS {len(PASS)}")
            print(f"FAIL {len(FAIL)}")
            return 1
        check("M6-PREP", all((work / name).is_file() for name in ("QUESTIONS.json", "THRESHOLDS.json", "SELECTION.md", "scripts/blue_gauge.py", "shared/case/scans.json"))
              and not (work / "reference").exists() and not (work / "tests").exists() and not (work / "shared/controls/WORKED_QUESTIONS.json").exists(),
              "preparation places the starter, thresholds, and selection form at the root and leaves staff files behind")
        evidence = base / "evidence"
        shutil.copyfile(worked, work / "QUESTIONS.json")
        (work / "JUDGE.yml").write_text("modelRoles:\n  judge: openrouter/typesafe/jev-1.13\n", encoding="utf-8")
        selection = "# Judge selection\n\n" + "".join(f"## {heading}\n\nThe desk asks the decision model only what the note says; code reads the scan record and the duty officer keeps every release with openrouter/typesafe/jev-1.13 pinned.\n\n" for heading in bg.SELECTION_HEADINGS)
        (work / "SELECTION.md").write_text(selection, encoding="utf-8")
        candidates(evidence)
        first = {key: answers_for(label(key)) for key in tuning}
        first["BG-002"] = answers_for(label("BG-002"), instruct=0.76)
        first["BG-011"] = answers_for(label("BG-011"), status="held")
        judge_run(work, evidence, "tuning-1", "tuning", first)
        revised = json.loads((work / "QUESTIONS.json").read_text(encoding="utf-8"))
        revised["questions"]["instructs_reader"]["criteria"]["false"] += " A release claim alone is not an instruction."
        (work / "QUESTIONS.json").write_text(json.dumps(revised, indent=2), encoding="utf-8")
        code, out = quiet(bg.main, ["freeze", "--work", str(work), "--evidence", str(evidence), "--tuning-run", "tuning-1", "--review-ceiling", "0.4"])
        check("M6-FREEZE", code == 1 and "changed after tuning-1" in out, "a freeze is refused when the questions changed after the tuning run it names")
        judge_run(work, evidence, "tuning-2", "tuning", {key: answers_for(label(key)) for key in tuning})
        (work / "THRESHOLDS.json").write_text(json.dumps({"schema_version": 1, **T}), encoding="utf-8")
        code, out = quiet(bg.main, ["freeze", "--work", str(work), "--evidence", str(evidence), "--tuning-run", "tuning-2", "--review-ceiling", "0.4"])
        check("M6-FREEZE", code == 0 and (evidence / "freeze.json").is_file(), "questions, thresholds, build, and review ceiling freeze before the held-out run")
        code, out = quiet(bg.main, ["freeze", "--work", str(work), "--evidence", str(evidence), "--tuning-run", "tuning-2", "--review-ceiling", "0.4"])
        check("M6-FREEZE", code == 1 and "already exists" in out, "a second freeze is refused")
        judge_run(work, evidence, "held-out", "held-out", {key: answers_for(label(key)) for key in held_out})
        code, out = quiet(bg.main, ["measure", "--work", str(work), "--evidence", str(evidence)])
        measured = json.loads((evidence / "held-out-measure.json").read_text(encoding="utf-8"))
        check("M6-MEASURE", code == 0 and measured["decision"] == "ADOPT for bounded internal screening" and measured["judge_cost_per_1000_notes_usd"] is not None, "careful held-out answers inside the frozen ceiling are adopted for bounded internal screening, with cost per 1,000 notes")
        (evidence / "HANDOFF.md").write_text("# Handoff\n\n" + "".join(f"## {heading}\n\nThe screen routes notes against the scan record; the duty officer owns every review and the Release Authority owns every release decision here.\n\n" for heading in bg.HANDOFF_HEADINGS), encoding="utf-8")
        (evidence / "first-misses.md").write_text("BG-002 read a release claim as an instruction.\nBG-011 read a caution as a hold.\n", encoding="utf-8")
        verify = lambda: quiet(bg.main, ["verify", "--work", str(work), "--evidence", str(evidence), "--launcher", str(REPO / "shared" / "run_omp.py")])
        code, out = verify()
        check("M6-VERIFY", code == 0 and out.count("PASS ") >= 10, "a consistent attempt passes every joined check")

        def defect(label_text, fragment, change, undo):
            change()
            code, out = verify()
            undo()
            check("M6-VERIFY", code == 1 and fragment in out, label_text)
        notes_file = evidence / "first-misses.md"
        original = notes_file.read_text(encoding="utf-8")
        defect("first-miss notes that skip a missed note are held", "does not mention BG-011", lambda: notes_file.write_text("BG-002 only.\n", encoding="utf-8"), lambda: notes_file.write_text(original, encoding="utf-8"))
        thresholds = (work / "THRESHOLDS.json").read_text(encoding="utf-8")
        defect("thresholds changed after the freeze are held", "changed after the freeze", lambda: (work / "THRESHOLDS.json").write_text(json.dumps({"schema_version": 1, **T, "pass_below": 0.3}), encoding="utf-8"), lambda: (work / "THRESHOLDS.json").write_text(thresholds, encoding="utf-8"))
        handoff = (evidence / "HANDOFF.md").read_text(encoding="utf-8")
        defect("a handoff without limits is held", "'## Limits'", lambda: (evidence / "HANDOFF.md").write_text(handoff.replace("## Limits", "## Notes"), encoding="utf-8"), lambda: (evidence / "HANDOFF.md").write_text(handoff, encoding="utf-8"))
        defect("an unfilled selection form is held", "SELECTION.md", lambda: shutil.copyfile(work / "shared/controls/SELECTION.template.md", work / "SELECTION.md"), lambda: (work / "SELECTION.md").write_text(selection, encoding="utf-8"))
        saved = (evidence / "held-out-measure.json").read_text(encoding="utf-8")
        defect("an edited measurement is held", "differs from a fresh measurement", lambda: (evidence / "held-out-measure.json").write_text(saved.replace('"ADOPT for bounded internal screening"', '"HOLD"'), encoding="utf-8"), lambda: (evidence / "held-out-measure.json").write_text(saved, encoding="utf-8"))
        response = (evidence / "tuning-2" / "response.md").read_text(encoding="utf-8")
        defect("a tuning receipt the shared auditor rejects is held", "saved response differs", lambda: (evidence / "tuning-2" / "response.md").write_text("judged everything perfectly", encoding="utf-8"), lambda: (evidence / "tuning-2" / "response.md").write_text(response, encoding="utf-8"))
        moved = base / "parked-tuning-2"
        defect("misses in the first tuning run with no revised run are held", "a revised tuning run must follow", lambda: (evidence / "tuning-2").rename(moved), lambda: moved.rename(evidence / "tuning-2"))

        late = base / "late"
        late_work = prepare_work.prepare("06", late / "work", root=REPO)
        shutil.copyfile(worked, late_work / "QUESTIONS.json")
        (late_work / "JUDGE.yml").write_text("modelRoles:\n  judge: openrouter/typesafe/jev-1.13\n", encoding="utf-8")
        (late_work / "THRESHOLDS.json").write_text(json.dumps({"schema_version": 1, **T}), encoding="utf-8")
        judge_run(late_work, late / "evidence", "tuning-1", "tuning", {key: answers_for(label(key)) for key in tuning})
        judge_run(late_work, late / "evidence", "held-out", "held-out", {key: answers_for(label(key)) for key in held_out})
        quiet(bg.main, ["freeze", "--work", str(late_work), "--evidence", str(late / "evidence"), "--tuning-run", "tuning-1", "--review-ceiling", "0.4"])
        code, out = quiet(bg.main, ["measure", "--work", str(late_work), "--evidence", str(late / "evidence")])
        check("M6-MEASURE", code == 1 and "started before the freeze" in out, "a held-out run that started before the freeze is not measured")

        drift = base / "drift"
        drift_work = prepare_work.prepare("06", drift / "work", root=REPO)
        shutil.copyfile(worked, drift_work / "QUESTIONS.json")
        (drift_work / "JUDGE.yml").write_text("modelRoles:\n  judge: openrouter/typesafe/jev-1.13\n", encoding="utf-8")
        (drift_work / "THRESHOLDS.json").write_text(json.dumps({"schema_version": 1, **T}), encoding="utf-8")
        judge_run(drift_work, drift / "evidence", "tuning-1", "tuning", {key: answers_for(label(key)) for key in tuning})
        quiet(bg.main, ["freeze", "--work", str(drift_work), "--evidence", str(drift / "evidence"), "--tuning-run", "tuning-1", "--review-ceiling", "0.4"])
        missed = {key: answers_for(label(key)) for key in held_out}
        missed["BG-053"] = answers_for(label("BG-053"), claim=0.05, status="received")
        judge_run(drift_work, drift / "evidence", "held-out", "held-out", missed, model="openrouter/typesafe/jev-1.13-20261101")
        quiet(bg.main, ["measure", "--work", str(drift_work), "--evidence", str(drift / "evidence")])
        drifted = json.loads((drift / "evidence" / "held-out-measure.json").read_text(encoding="utf-8"))
        check("M6-MEASURE", drifted["decision"] == "HOLD" and any("1 missed overstatement" in reason for reason in drifted["reasons"]) and any("differs from the tuning build" in reason for reason in drifted["reasons"]),
              "a held-out miss and a changed served build both hold the decision")

    # ---------------------------------------------------------------- learner pages
    learner = "\n".join(path.read_text(encoding="utf-8") for path in LEARNER_FILES)
    found = [token for token in OTHER_MODULE_TOKENS + STAFF_TOKENS if token in learner]
    check("M6-LEARNER", not found, f"learner pages carry no other module's case or staff wording{': ' + ', '.join(found) if found else ''}")
    lab = (ROOT / "shared" / "MODULE_06_LAB.md").read_text(encoding="utf-8")
    used = set(re.findall(r"blue_gauge\.py[\"']? ([a-z-]+)", lab))
    check("M6-LEARNER", used == {"check-questions", "report", "spread", "freeze", "measure", "verify"}, f"the lab runs every Blue Gauge command and no other: {sorted(used)}")
    launcher_args = [line.split("run_omp.py", 1)[1].split("&&")[0] for line in lab.splitlines() if "run_omp.py" in line]
    flags = set(re.findall(r"(--[a-z][a-z-]+)", "\n".join(launcher_args)))
    known = set(re.findall(r'add_argument\("(--[a-z][a-z-]+)"', (REPO / "shared" / "run_omp.py").read_text(encoding="utf-8")))
    check("M6-LEARNER", bool(flags) and flags <= known and {"--list-judges", "--judge-config"} <= flags, f"every launcher flag the lab uses exists: {sorted(flags)}")
    check("M6-LEARNER", "openrouter/typesafe/jev-1.13" in lab and "~typesafe/jev-latest" in lab, "the lab names the pinned judge and the moving alias it refuses")

    print(f"PASS {len(PASS)}")
    print(f"FAIL {len(FAIL)}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
