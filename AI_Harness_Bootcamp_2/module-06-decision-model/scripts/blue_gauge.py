#!/usr/bin/env python3
"""Blue Gauge: check the question set, route judged notes, set and freeze thresholds, measure, and verify.

Code answers what the scan record settles. The decision model answers narrow questions about each
note. The router combines both with thresholds you set, and the duty officer gets what neither settles.
No command here calls a model; judgments come from the launcher's judge runs.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

OPTIONS = ["released_for_issue", "inspected", "received", "held", "not_stated"]
STATUS_RANK = {"not_stated": 0, "held": 0, "received": 1, "inspected": 2, "released_for_issue": 3}
SCAN_RANK = {"HELD": 0, "RECEIVED": 1, "INSPECTED": 2, "RELEASED": 3}
CONTRACT = {"claims_release": "bool", "instructs_reader": "bool", "note_status": "choice", "note_status_reversed": "choice", "urgency": "score"}
THRESHOLDS = ("instruction_review", "return_at", "pass_below", "status_confidence")
CYLINDER = re.compile(r"\bOC-\d{4}\b")
ORDER = re.compile(r"\bRA-\d{4}\b")
PATH = re.compile(r"`([^`]+)`")
PINNED = "openrouter/typesafe/jev-1.13"
CRITICAL = ("missed overstatement", "instruction not reviewed", "other cylinder not reviewed")
SELECTION_HEADINGS = ("Decision point", "Why a decision model", "Candidate chosen", "Weak spots and how this workflow answers each", "Data boundary")
HANDOFF_HEADINGS = ("What the screen decides", "Settings in force", "Held-out result", "Limits", "Owner")


class Hold(Exception):
    """A check that cannot pass; the message names the reason."""


def strict_json(text: str):
    def pairs(items):
        seen = {}
        for key, value in items:
            if key in seen:
                raise Hold(f"duplicate JSON key: {key}")
            seen[key] = value
        return seen
    try:
        return json.loads(text, object_pairs_hook=pairs)
    except json.JSONDecodeError as error:
        raise Hold(f"not valid JSON: {error.msg} at line {error.lineno}") from None


def load(path: Path):
    if not path.is_file():
        raise Hold(f"missing file: {path}")
    content = path.read_text(encoding="utf-8")
    if content.startswith("\ufeff"):
        raise Hold(f"{path.name} starts with a byte-order mark; save it as UTF-8 without one")
    return strict_json(content)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def usd(value) -> str:
    return f"{value:.6f}" if isinstance(value, (int, float)) and not isinstance(value, bool) else "unknown"


def text(value) -> bool:
    return isinstance(value, str) and bool(value.strip())


def question_problems(path: Path) -> list[str]:
    """Every reason the question set cannot drive the router; an empty list means it can."""
    data = load(path)
    if not isinstance(data, dict) or set(data) != {"schema_version", "questions"} or data.get("schema_version") != 1:
        return ['the file must be {"schema_version": 1, "questions": {...}}']
    questions = data["questions"]
    if not isinstance(questions, dict):
        return ["questions must be an object keyed by question id"]
    problems = []
    for qid, kind in CONTRACT.items():
        if qid not in questions:
            problems.append(f"{qid}: missing; the router reads a {kind} answer under this id")
    for qid, question in questions.items():
        where = qid
        if qid not in CONTRACT and not qid.startswith("extra_"):
            problems.append(f"{where}: the router never reads this answer; delete it, or rename it extra_{qid} if you want it asked anyway")
        if not re.fullmatch(r"[a-z][a-z0-9_]{0,63}", qid):
            problems.append(f"{where}: ids use lowercase letters, digits, and underscores")
        if not isinstance(question, dict) or set(question) - {"type", "instructions", "criteria"}:
            problems.append(f"{where}: a question has only type, instructions, and criteria")
            continue
        kind, instructions, criteria = question.get("type"), question.get("instructions"), question.get("criteria")
        if qid in CONTRACT and kind != CONTRACT[qid]:
            problems.append(f"{where}: must be a {CONTRACT[qid]} question, not {kind}")
        if kind not in {"bool", "choice", "score"}:
            problems.append(f"{where}: type must be bool, choice, or score")
            continue
        if not text(instructions):
            problems.append(f"{where}: instructions must be text")
            continue
        paths = PATH.findall(instructions)
        if "note" not in paths:
            problems.append(f"{where}: name the part of the state it judges, in backticks: `note`")
        if any(found != "note" for found in paths):
            problems.append(f"{where}: the state holds only `note`; other backticked names point at nothing")
        if kind == "bool" and criteria is not None and (not isinstance(criteria, dict) or not criteria or set(criteria) - {"true", "false"} or not all(text(v) for v in criteria.values())):
            problems.append(f"{where}: yes/no criteria are an object with text under true and false")
        if kind == "choice" and (not isinstance(criteria, dict) or len(criteria) < 2 or not all(text(v) for v in criteria.values())):
            problems.append(f"{where}: a choice needs at least two options, each described in text")
        if kind == "score" and (not isinstance(criteria, list) or len(criteria) < 2 or not all(text(v) for v in criteria)):
            problems.append(f"{where}: a score needs at least two levels, each described in text, lowest first")
    status = questions.get("note_status", {}).get("criteria") if isinstance(questions.get("note_status"), dict) else None
    reverse = questions.get("note_status_reversed", {}).get("criteria") if isinstance(questions.get("note_status_reversed"), dict) else None
    if isinstance(status, dict) and set(status) != set(OPTIONS):
        missing, extra = sorted(set(OPTIONS) - set(status)), sorted(set(status) - set(OPTIONS))
        problems.append(f"note_status: options must be exactly {', '.join(OPTIONS)}" + (f"; missing {', '.join(missing)}" if missing else "") + (f"; unknown {', '.join(extra)}" if extra else ""))
    if isinstance(status, dict) and isinstance(reverse, dict):
        if list(reverse) != list(reversed(list(status))) or any(reverse.get(label) != status.get(label) for label in status):
            problems.append("note_status_reversed: same options and descriptions as note_status, listed in reverse order")
        if questions["note_status_reversed"].get("instructions") != questions["note_status"].get("instructions"):
            problems.append("note_status_reversed: same instructions as note_status")
    urgency = questions.get("urgency", {}).get("criteria") if isinstance(questions.get("urgency"), dict) else None
    if isinstance(urgency, list) and len(urgency) != 3:
        problems.append("urgency: three levels, lowest first: routine, needed today, needed immediately")
    return problems


def read_thresholds(path: Path) -> dict:
    data = load(path)
    if not isinstance(data, dict) or set(data) != {"schema_version", *THRESHOLDS} or data.get("schema_version") != 1:
        raise Hold(f"{path.name} must hold schema_version 1 and exactly {', '.join(THRESHOLDS)}")
    if not all(isinstance(data[key], (int, float)) and not isinstance(data[key], bool) and 0 <= data[key] <= 1 for key in THRESHOLDS):
        raise Hold("every threshold is a number from 0 to 1")
    if data["pass_below"] > data["return_at"]:
        raise Hold("pass_below cannot be above return_at")
    return data


def route(note: str, scan: dict, answers: dict | None, t: dict) -> tuple[str, str]:
    """Code checks first, then the instruction check, then the release and status checks."""
    if not answers:
        return "REVIEW", "no judgment; a missing answer never passes"
    cylinders = set(CYLINDER.findall(note))
    if cylinders != {scan["cylinder"]}:
        return "REVIEW", "names another cylinder" if cylinders else "names no cylinder"
    if set(ORDER.findall(note)) - {scan["release_order"]}:
        return "RETURN", "cites a release order the scan record does not hold"
    if answers["instructs_reader"]["bool"] >= t["instruction_review"]:
        return "REVIEW", "carries an instruction"
    if scan["status"] == "RELEASED":
        return "PASS", "the scan record holds a release order"
    first, second = answers["note_status"], answers["note_status_reversed"]
    agree = first["choice"] == second["choice"]
    settled = agree and min(first["confidence"], second["confidence"]) >= t["status_confidence"]
    above = settled and STATUS_RANK[first["choice"]] > SCAN_RANK[scan["status"]]
    if answers["claims_release"]["bool"] >= t["return_at"] or above:
        return "RETURN", "claims more than the scan record"
    if not settled:
        return "REVIEW", "status answer changed with option order" if not agree else "status answer not settled"
    if answers["claims_release"]["bool"] <= t["pass_below"]:
        return "PASS", "matches the scan record"
    return "REVIEW", "release claim not settled"


def outcome(route_name: str, label: dict) -> str:
    if label["other_cylinder"] and route_name != "REVIEW":
        return "other cylinder not reviewed"
    if label["instructs"] and route_name != "REVIEW":
        return "instruction not reviewed"
    if label["overstates"] and route_name == "PASS":
        return "missed overstatement"
    if not label["overstates"] and route_name == "RETURN":
        return "wrong return"
    return "reviewed" if route_name == "REVIEW" else "ok"


def question_misses(answers: dict | None, label: dict) -> list[str]:
    """Threshold-free disagreements between the model's answers and the desk label."""
    if not answers:
        return ["no judgment"]
    misses = []
    if (answers["claims_release"]["bool"] >= 0.5) != (label["note_status"] == "released_for_issue"):
        misses.append(f"claims_release {answers['claims_release']['bool']:.2f}")
    if answers["note_status"]["choice"] != label["note_status"]:
        misses.append(f"note_status {answers['note_status']['choice']} (desk: {label['note_status']})")
    if answers["note_status_reversed"]["choice"] != label["note_status"]:
        misses.append(f"note_status_reversed {answers['note_status_reversed']['choice']}")
    if (answers["instructs_reader"]["bool"] >= 0.5) != label["instructs"]:
        misses.append(f"instructs_reader {answers['instructs_reader']['bool']:.2f}")
    return misses


class Run:
    """One judge run's saved judgments, joined to the case notes, scan records, and desk labels."""

    def __init__(self, work: Path, name: str):
        self.work, self.name = work, name
        folder = work / "out" / name
        rows = [strict_json(line) for line in (folder / "judgments.jsonl").read_text(encoding="utf-8").splitlines()] if (folder / "judgments.jsonl").is_file() else None
        if rows is None:
            raise Hold(f"no judgments at {folder / 'judgments.jsonl'}; run the judge first")
        self.rows = {row["key"]: row for row in rows}
        self.status = load(folder / "batch-status.json")
        self.scans = load(work / "shared/case/scans.json")
        keys = set(self.rows)
        tuning = load(work / "shared/case/labels/tuning-labels.json")["labels"]
        if keys <= set(tuning):
            self.split, self.labels = "tuning", tuning
        else:
            held_out = load(work / "shared/case/labels/held-out-labels.json")["labels"]
            if not keys <= set(held_out):
                raise Hold(f"{name} mixes tuning and held-out notes")
            self.split, self.labels = "held-out", held_out
        self.notes = {key: load(work / "shared/case/notes" / self.split / f"{key}.json")["state"]["note"] for key in sorted(keys)}
        for key, row in self.rows.items():
            if row.get("error") is not None or not isinstance(row.get("answers"), dict) or set(CONTRACT) - set(row["answers"]):
                raise Hold(f"{key}: the saved judgment lacks the answers the router reads")

    def routed(self, t: dict) -> dict:
        return {key: route(self.notes[key], self.scans[key], self.rows[key]["answers"], t) for key in self.notes}

    def score(self, t: dict) -> dict:
        routes = self.routed(t)
        outcomes = {key: outcome(routes[key][0], self.labels[key]) for key in routes}
        counts = {name: sum(value == name for value in outcomes.values()) for name in (*CRITICAL, "wrong return", "reviewed", "ok")}
        return {"routes": routes, "outcomes": outcomes, "counts": counts, "total": len(routes),
                "review_share": round(sum(route_name == "REVIEW" for route_name, _ in routes.values()) / len(routes), 4)}


def print_table(run: Run, t: dict) -> dict:
    result = run.score(t)
    print(f"{'note':7} {'scan':9} {'claim':>5} {'status (both orders)':34} {'instr':>5} {'urg':>4}  route   reason / desk outcome")
    for key in run.notes:
        answers = run.rows[key]["answers"]
        first, second = answers["note_status"], answers["note_status_reversed"]
        status = f"{first['choice']} {first['confidence']:.2f}" + ("" if first["choice"] == second["choice"] else f" / {second['choice']}") + f" | {second['confidence']:.2f}"
        route_name, reason = result["routes"][key]
        flag = result["outcomes"][key]
        marker = "  <<" if flag in CRITICAL or flag == "wrong return" else ""
        print(f"{key:7} {run.scans[key]['status']:9} {answers['claims_release']['bool']:5.2f} {status:34} {answers['instructs_reader']['bool']:5.2f} {answers['urgency']['score']:4.1f}  {route_name:7} {reason}; {flag}{marker}")
    counts = result["counts"]
    print(f"SUMMARY {run.split} {result['total']} notes: missed overstatements {counts['missed overstatement']}, instructions not reviewed {counts['instruction not reviewed']}, "
          f"other cylinders not reviewed {counts['other cylinder not reviewed']}, wrong returns {counts['wrong return']}, reviewed {counts['reviewed']} ({result['review_share']:.0%})")
    return result


def command_check(args) -> int:
    problems = question_problems(Path(args.questions))
    if problems:
        for problem in problems:
            print(f"HOLD: {problem}")
        return 1
    questions = load(Path(args.questions))["questions"]
    for qid, question in questions.items():
        shape = question["type"] if question["type"] == "bool" else f"{question['type']} {list(question['criteria']) if question['type'] == 'choice' else len(question['criteria'])}"
        print(f"{qid:24} {shape}{'   (router ignores)' if qid.startswith('extra_') else ''}")
    print(f"PASS: {len(questions)} questions fit the router; every question judges `note`")
    return 0


def command_report(args) -> int:
    work = Path(args.work)
    run = Run(work, args.run)
    t = read_thresholds(work / "THRESHOLDS.json")
    print(f"RUN {args.run}: {run.split}, served by {run.status.get('model')}, cost USD {usd(run.status.get('cost'))}")
    print(f"THRESHOLDS {json.dumps({key: t[key] for key in THRESHOLDS})}")
    print_table(run, t)
    if run.split == "tuning":
        misses = {key: question_misses(run.rows[key]["answers"], run.labels[key]) for key in run.notes}
        print("QUESTION MISSES (no thresholds; claim and instruction read at 0.50):")
        for key, found in misses.items():
            if found:
                print(f"  {key}: {'; '.join(found)} | note: {run.notes[key]}")
        if not any(misses.values()):
            print("  none")
    return 0


def command_spread(args) -> int:
    """Show each signal's tuning values split by the desk label, so thresholds go in the gaps."""
    work = Path(args.work)
    run = Run(work, args.run)
    if run.split != "tuning":
        raise Hold("set thresholds on tuning notes only; held-out notes are for the final check")
    answers = {key: run.rows[key]["answers"] for key in run.notes}
    show = lambda values: "  ".join(f"{value:.2f} {key}" for value, key in values) or "none"

    def undecided(key):
        scan, note = run.scans[key], run.notes[key]
        return scan["status"] != "RELEASED" and set(CYLINDER.findall(note)) == {scan["cylinder"]} and not set(ORDER.findall(note)) - {scan["release_order"]}

    instructions = sorted((answers[key]["instructs_reader"]["bool"], key) for key in run.notes if run.labels[key]["instructs"])
    plain = sorted(((answers[key]["instructs_reader"]["bool"], key) for key in run.notes if not run.labels[key]["instructs"]), reverse=True)
    print("INSTRUCTION  instructs_reader yes-probability on every tuning note")
    print(f"  desk: instruction, lowest first     {show(instructions)}")
    print(f"  desk: no instruction, highest first  {show(plain[:8])}")
    open_notes = [key for key in run.notes if undecided(key)]
    claims = sorted((answers[key]["claims_release"]["bool"], key) for key in open_notes if run.labels[key]["note_status"] == "released_for_issue")
    no_claims = sorted(((answers[key]["claims_release"]["bool"], key) for key in open_notes if run.labels[key]["note_status"] != "released_for_issue"), reverse=True)
    print("RELEASE CLAIM  claims_release yes-probability on notes the scan record and the code checks leave open")
    print(f"  desk: claims a release, lowest first     {show(claims)}")
    print(f"  desk: no release claim, highest first    {show(no_claims[:8])}")
    matches, differs = [], []
    for key in open_notes:
        first, second = answers[key]["note_status"], answers[key]["note_status_reversed"]
        confidence = min(first["confidence"], second["confidence"])
        agree = first["choice"] == second["choice"] == run.labels[key]["note_status"]
        (matches if agree else differs).append((confidence, key if agree else f"{key} ({first['choice']}/{second['choice']}; desk {run.labels[key]['note_status']})"))
    print("STATUS  lower confidence of the two option orders, same notes")
    print(f"  both orders match the desk, lowest first  {show(sorted(matches)[:8])}")
    print(f"  an order differs from the desk            {show(sorted(differs))}")
    print("Put pass_below under the lowest release claim and instruction_review under the lowest instruction, with room to spare.")
    print("Missing either is the error the desk cannot accept; a value set lower sends more notes to review, which costs minutes.")
    return 0


def run_result(evidence: Path, name: str) -> dict:
    result = load(evidence / name / "result.json")
    if result.get("status") != "PASS" or not result.get("judge"):
        raise Hold(f"{name}: the launcher did not record a complete judge run")
    return result


def command_freeze(args) -> int:
    work, evidence = Path(args.work), Path(args.evidence)
    target = evidence / "freeze.json"
    if target.exists():
        raise Hold(f"{target} already exists; a freeze is recorded once")
    if question_problems(work / "QUESTIONS.json"):
        raise Hold("the question set does not pass check-questions")
    t = read_thresholds(work / "THRESHOLDS.json")
    tuning = run_result(evidence, args.tuning_run)
    if digest(evidence / args.tuning_run / "questions.json") != digest(work / "QUESTIONS.json"):
        raise Hold(f"QUESTIONS.json changed after {args.tuning_run}; tune on judgments from the questions you freeze")
    if not 0 <= args.review_ceiling <= 1:
        raise Hold("--review-ceiling is a share from 0 to 1")
    record = {"created_at": datetime.now(timezone.utc).isoformat(), "questions_sha256": digest(work / "QUESTIONS.json"), "thresholds_sha256": digest(work / "THRESHOLDS.json"),
              "judge_config_sha256": digest(work / "JUDGE.yml"), "thresholds": {key: t[key] for key in THRESHOLDS}, "tuning_run": args.tuning_run,
              "tuning_served_model": tuning["judge"]["served_model"], "review_ceiling": args.review_ceiling,
              "rule": "Adopt for bounded internal screening only if the held-out run has no missed overstatement, no unreviewed instruction, no unreviewed other-cylinder note, the tuning run's served build, and a review share at or below the ceiling."}
    with target.open("x", encoding="utf-8") as handle:
        handle.write(json.dumps(record, indent=2) + "\n")
    print(f"PASS: froze questions {record['questions_sha256'][:12]}, thresholds {record['thresholds_sha256'][:12]}, build {record['tuning_served_model']}, review ceiling {args.review_ceiling:.0%}")
    return 0


def courier_cost(evidence: Path) -> float:
    total = 0.0
    for line in (evidence / "events.jsonl").read_text(encoding="utf-8").splitlines():
        row = json.loads(line)
        message = row.get("message", {}) if row.get("type") == "message_end" else {}
        if message.get("role") == "assistant":
            total += float((message.get("usage") or {}).get("cost", {}).get("total", 0) or 0)
    return round(total, 6)


def measurement(work: Path, evidence: Path, name: str) -> dict:
    freeze = load(evidence / "freeze.json")
    result = run_result(evidence, name)
    if digest(evidence / name / "questions.json") != freeze["questions_sha256"]:
        raise Hold(f"{name} did not use the frozen question set")
    if digest(work / "THRESHOLDS.json") != freeze["thresholds_sha256"]:
        raise Hold("THRESHOLDS.json changed after the freeze")
    if result["started_at"] <= freeze["created_at"]:
        raise Hold(f"{name} started before the freeze was recorded")
    run = Run(work, name)
    if run.split != "held-out":
        raise Hold(f"{name} is not the held-out run")
    scored = run.score(read_thresholds(work / "THRESHOLDS.json"))
    counts, items, cost = scored["counts"], result["judge"]["items"], result["judge"]["cost_usd"]
    reasons = [f"{counts[name_]} {name_}" for name_ in CRITICAL if counts[name_]]
    if result["judge"]["served_model"] != freeze["tuning_served_model"]:
        reasons.append(f"served build {result['judge']['served_model']} differs from the tuning build {freeze['tuning_served_model']}")
    if scored["review_share"] > freeze["review_ceiling"]:
        reasons.append(f"review share {scored['review_share']:.0%} is above the frozen ceiling {freeze['review_ceiling']:.0%}")
    return {"run": name, "notes": scored["total"], "counts": counts, "review_share": scored["review_share"], "served_model": result["judge"]["served_model"],
            "judge_cost_usd": cost, "judge_cost_per_1000_notes_usd": round(cost / items * 1000, 6) if items else None, "courier_cost_usd": courier_cost(evidence / name),
            "routes": {key: list(value) for key, value in scored["routes"].items()}, "decision": "HOLD" if reasons else "ADOPT for bounded internal screening", "reasons": reasons}


def command_measure(args) -> int:
    work, evidence = Path(args.work), Path(args.evidence)
    target = evidence / f"{args.run}-measure.json"
    if target.exists():
        raise Hold(f"{target} already exists; measure the held-out run once")
    record = measurement(work, evidence, args.run)
    with target.open("x", encoding="utf-8") as handle:
        handle.write(json.dumps(record, indent=2) + "\n")
    counts = record["counts"]
    print(f"HELD-OUT {record['notes']} notes: missed overstatements {counts['missed overstatement']}, instructions not reviewed {counts['instruction not reviewed']}, other cylinders not reviewed {counts['other cylinder not reviewed']}, "
          f"wrong returns {counts['wrong return']}, reviewed {counts['reviewed']} ({record['review_share']:.0%})")
    print(f"COST decision model USD {usd(record['judge_cost_usd'])} for {record['notes']} notes (USD {usd(record['judge_cost_per_1000_notes_usd'])} per 1,000 notes); courier turn USD {usd(record['courier_cost_usd'])}")
    print(f"DECISION: {record['decision']}" + (f" ({'; '.join(record['reasons'])})" if record["reasons"] else ""))
    return 0


def sections(path: Path, headings: tuple[str, ...], template: Path | None = None) -> list[str]:
    if not path.is_file():
        return [f"missing {path.name}"]
    content = path.read_text(encoding="utf-8")
    parts = {match.group(1).strip(): body.strip() for match, body in zip(re.finditer(r"^## (.+)$", content, re.M), re.split(r"^## .+$", content, flags=re.M)[1:])}
    original = {}
    if template and template.is_file():
        source = template.read_text(encoding="utf-8")
        original = {match.group(1).strip(): body.strip() for match, body in zip(re.finditer(r"^## (.+)$", source, re.M), re.split(r"^## .+$", source, flags=re.M)[1:])}
    problems = []
    for heading in headings:
        body = parts.get(heading, "")
        if len(body.split()) < 12 or body == original.get(heading):
            problems.append(f"{path.name}: write at least a few sentences of your own under '## {heading}'")
    return problems


def launcher(path: str):
    spec = importlib.util.spec_from_file_location("course_run_omp", path)
    if not spec or not spec.loader:
        raise Hold(f"cannot load the launcher at {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def command_verify(args) -> int:
    work, evidence = Path(args.work), Path(args.evidence)
    runtime = launcher(args.launcher)
    checks: list[tuple[str, list[str]]] = []
    def check(label, function):
        try:
            checks.append((label, function() or []))
        except Hold as error:
            checks.append((label, [str(error)]))
        except (OSError, ValueError, KeyError, TypeError) as error:
            checks.append((label, [f"malformed record: {error}"]))

    check("candidates", lambda: [] if load(evidence / "judge-candidates/result.json").get("pinned_offered") is True else ["the saved candidate list does not offer the pinned judge"])
    check("selection", lambda: sections(work / "SELECTION.md", SELECTION_HEADINGS, work / "shared/controls/SELECTION.template.md") + ([] if PINNED in (work / "SELECTION.md").read_text(encoding="utf-8") else [f"SELECTION.md does not name {PINNED}"]))
    check("judge setting", lambda: [] if runtime.parse_judge_config(work / "JUDGE.yml") == PINNED else ["JUDGE.yml is not pinned"])
    check("questions", lambda: question_problems(work / "QUESTIONS.json"))
    every_run = sorted((path.name for path in evidence.glob("tuning-*") if path.is_dir() and re.fullmatch(r"tuning-\d+", path.name)), key=lambda name: int(name.split("-")[1]))

    def completed(name: str) -> bool:
        try:
            return load(evidence / name / "result.json").get("status") == "PASS"
        except Hold:
            return False
    tuning_runs = [name for name in every_run if completed(name)]
    held_runs = [name for name in every_run if name not in tuning_runs]

    def judge_runs(names, split):
        problems = []
        for name in names:
            problems += [f"{name}: {problem}" for problem in runtime.audit_evidence(evidence / name)]
            policy = load(evidence / name / "policy.json")
            if policy.get("judge", {}).get("states_dir") != f"shared/case/notes/{split}":
                problems.append(f"{name}: judged {policy.get('judge', {}).get('states_dir')}, not shared/case/notes/{split}")
        return problems or ([] if names else [f"no {split} judge run under {evidence}"])
    check("tuning runs", lambda: judge_runs(tuning_runs, "tuning"))

    def first_misses():
        # The first run with saved judgments sets the misses to note, whatever its recorded status.
        first = None
        for name in every_run:
            try:
                first = (name, Run(work, name))
                break
            except Hold:
                continue
        if first is None:
            return ["no tuning run with saved judgments to compare against"]
        name, run = first
        missed = [key for key in run.notes if question_misses(run.rows[key]["answers"], run.labels[key])]
        notes = (evidence / "first-misses.md").read_text(encoding="utf-8") if (evidence / "first-misses.md").is_file() else None
        if notes is None:
            return ["missing first-misses.md"]
        problems = [f"first-misses.md does not mention {key}" for key in missed if key not in notes]
        asked = digest(evidence / name / "questions.json")
        revised = [later for later in tuning_runs if int(later.split("-")[1]) > int(name.split("-")[1]) and digest(evidence / later / "questions.json") != asked]
        if missed and not revised:
            problems.append(f"{name} had question misses; a revised tuning run must follow")
        return problems
    check("first misses", first_misses)

    def frozen():
        freeze = load(evidence / "freeze.json")
        problems = [] if freeze.get("tuning_run") in tuning_runs else [f"the freeze names {freeze.get('tuning_run')}, which is not a saved tuning run"]
        if digest(work / "QUESTIONS.json") != freeze["questions_sha256"] or digest(work / "THRESHOLDS.json") != freeze["thresholds_sha256"]:
            problems.append("QUESTIONS.json or THRESHOLDS.json changed after the freeze")
        return problems
    check("freeze", frozen)
    check("held-out run", lambda: judge_runs(["held-out"], "held-out"))

    def measured():
        saved = load(evidence / "held-out-measure.json")
        again = measurement(work, evidence, "held-out")
        return [] if saved == again else ["held-out-measure.json differs from a fresh measurement of the saved judgments"]
    check("held-out measurement", measured)
    check("handoff", lambda: sections(evidence / "HANDOFF.md", HANDOFF_HEADINGS))
    failed = 0
    for label, problems in checks:
        if problems:
            failed += 1
            for problem in problems:
                print(f"HOLD {label}: {problem}")
        else:
            print(f"PASS {label}")
    if held_runs:
        print(f"NOTE kept held tuning runs, not audited as complete: {', '.join(held_runs)}")
    if failed:
        print(f"HOLD: {failed} of {len(checks)} checks need attention")
        return 1
    decision = load(evidence / "held-out-measure.json")["decision"]
    print(f"PASS: every record joins; the held-out decision on record is {decision}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    check = commands.add_parser("check-questions", help="check that the question set fits the router")
    check.add_argument("questions")
    for name, helptext in (("report", "route one judge run and show each note"), ("spread", "show each signal's tuning values split by the desk label")):
        sub = commands.add_parser(name, help=helptext)
        sub.add_argument("--work", required=True)
        sub.add_argument("--run", required=True)
    freeze = commands.add_parser("freeze", help="record the questions and thresholds before the held-out run")
    freeze.add_argument("--work", required=True)
    freeze.add_argument("--evidence", required=True)
    freeze.add_argument("--tuning-run", required=True)
    freeze.add_argument("--review-ceiling", required=True, type=float)
    measure = commands.add_parser("measure", help="score the held-out run against the frozen rule")
    measure.add_argument("--work", required=True)
    measure.add_argument("--evidence", required=True)
    measure.add_argument("--run", default="held-out")
    verify = commands.add_parser("verify", help="join every record and recheck the launcher evidence")
    verify.add_argument("--work", required=True)
    verify.add_argument("--evidence", required=True)
    verify.add_argument("--launcher", required=True)
    args = parser.parse_args(argv)
    handler = {"check-questions": command_check, "report": command_report, "spread": command_spread, "freeze": command_freeze, "measure": command_measure, "verify": command_verify}[args.command]
    try:
        return handler(args)
    except Hold as error:
        print(f"HOLD: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
