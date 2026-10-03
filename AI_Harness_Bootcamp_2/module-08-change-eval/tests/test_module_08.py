#!/usr/bin/env python3
"""Behavior and integrity checks; synthetic failures never count as live calls."""
from __future__ import annotations

import contextlib
import csv
import hashlib
import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
FAILURES = []


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def command(script, *args):
    return subprocess.run([sys.executable, str(script), *map(str, args)], capture_output=True, text=True, env={**os.environ, "OPENROUTER_API_KEY": ""}, timeout=30)


def copied_work(base):
    work = base / "work with spaces"
    for name in ("cases", "controls", "baseline"):
        shutil.copytree(ROOT / "shared" / name, work / "shared" / name)
    (work / "scripts").mkdir()
    for name in ("restore_baseline.py", "evaluate_pairs.py"):
        shutil.copyfile(ROOT / "scripts" / name, work / "scripts" / name)
    return work


def reference():
    expected = (ROOT / "reference/REFERENCE.sha256").read_text().split()[0]
    assert digest(ROOT / "reference/REFERENCE.md") == expected


def evaluated_pairs():
    with tempfile.TemporaryDirectory() as temp:
        out = Path(temp) / "results.csv"
        result = command(ROOT / "scripts/evaluate_pairs.py", ROOT / "shared/cases", ROOT / "shared/controls/policy.json", out)
        assert result.returncode == 0, result.stderr
        with out.open(newline="") as stream:
            rows = list(csv.DictReader(stream))
        expected = {(f"PC-{number:02d}", variant) for number in range(1, 41) for variant in ("baseline", "candidate-a", "candidate-b")}
        assert len(rows) == len(expected) and {(row["case_id"], row["variant"]) for row in rows} == expected
        failures = {variant: set() for variant in ("baseline", "candidate-a", "candidate-b")}
        for row in rows:
            case = ROOT / "shared/cases" / row["case_id"]
            assert row["source_sha256"] == digest(case / "sources.json")
            assert row["brief_sha256"] == digest(case / f"{row['variant']}.md")
            assert row["config_sha256"] == digest(ROOT / "shared/controls" / f"{row['variant']}.json")
            if row["passed"] == "false":
                failures[row["variant"]].add(row["case_id"])
                assert row["reason"] == ("sourced_mass" if row["variant"] == "candidate-a" else "labeled_gate_time")
        assert failures == {"baseline": set(), "candidate-a": {"PC-03", "PC-11", "PC-27"}, "candidate-b": {"PC-02", "PC-14", "PC-35"}}
        before = out.read_bytes()
        again = command(ROOT / "scripts/evaluate_pairs.py", ROOT / "shared/cases", ROOT / "shared/controls/policy.json", out)
        assert again.returncode == 1 and out.read_bytes() == before


def malformed_and_cell_boundaries():
    with tempfile.TemporaryDirectory() as temp:
        case = Path(temp)
        shutil.copyfile(ROOT / "shared/cases/PC-01/sources.json", case / "sources.json")
        original = (ROOT / "shared/cases/PC-01/baseline.md").read_text()
        source = json.loads((case / "sources.json").read_text())
        examples = [
            original.replace(" | SB-PC-01#payload", ""),
            original.replace("2211 kg |", "2211 kg | extra |"),
            original + "This is released for dispatch.\n",
            original.replace("13:05 MDT", "13:05"),
            original.replace("19:05 UTC", "19:05 UTC / 13:05 MDT").replace("| 13:05 MDT |", "| 19:05 UTC / 13:05 MDT |"),
            original.replace("SB-PC-01#payload", "SB-PC-01#payload-s14"),
            original.replace("# Slope Brief — PC-01", "# Slope Brief — PC-010"),
        ]
        # The title spelling is not the contract; change the actual ID wherever it appears.
        examples[-1] = original.replace("PC-01", "PC-010")
        for text in examples:
            (case / "brief.md").write_text(text)
            result = command(ROOT / "shared/controls/hard_gates.py", case / "brief.md")
            assert result.returncode == 1 and "HOLD" in result.stdout + result.stderr and "Traceback" not in result.stderr
        (case / "brief.md").write_text(original)
        source["sources"]["SB-PC-01#payload"]["text"] = "The stated mass is 12211 kg."
        (case / "sources.json").write_text(json.dumps(source))
        result = command(ROOT / "shared/controls/hard_gates.py", case / "brief.md")
        assert result.returncode == 1 and "sourced_mass" in result.stdout


def frozen_identity_refusal():
    with tempfile.TemporaryDirectory() as temp:
        work = copied_work(Path(temp))
        policy = work / "shared/controls/policy.json"
        value = json.loads(policy.read_text())
        value["config_sha256"]["baseline"] = "0" * 64
        policy.write_text(json.dumps(value))
        output = work / "out/bad.csv"
        result = command(work / "scripts/evaluate_pairs.py", work / "shared/cases", policy, output)
        assert result.returncode == 1 and not output.exists()


def source_errors_are_not_candidate_failures():
    for condition in ("malformed_source", "wrong_case", "malformed_candidate"):
        with tempfile.TemporaryDirectory() as temp:
            work = copied_work(Path(temp))
            case = work / "shared/cases/PC-01"
            if condition == "malformed_source":
                source = json.loads((case / "sources.json").read_text())
                source["sources"]["SB-PC-01#payload"]["authoritative"] = "true"
                (case / "sources.json").write_text(json.dumps(source))
            elif condition == "wrong_case":
                (case / "sources.json").write_bytes((work / "shared/cases/PC-02/sources.json").read_bytes())
            else:
                (case / "candidate-a.md").write_text("The candidate omitted the required table.\n")
            output = work / "out/results.csv"
            result = command(work / "scripts/evaluate_pairs.py", work / "shared/cases", work / "shared/controls/policy.json", output)
            if condition != "malformed_candidate":
                assert result.returncode == 1 and "HOLD:" in result.stderr and not output.exists(), result.stdout + result.stderr
                assert "Traceback" not in result.stderr
            else:
                assert result.returncode == 0, result.stderr
                with output.open(newline="") as stream:
                    rows = list(csv.DictReader(stream))
                failed = next(row for row in rows if row["case_id"] == "PC-01" and row["variant"] == "candidate-a")
                baseline = next(row for row in rows if row["case_id"] == "PC-01" and row["variant"] == "baseline")
                assert failed["format_ok"] == "false" and failed["reason"] == "format"
                assert baseline["passed"] == "true"


def restore_boundaries():
    with tempfile.TemporaryDirectory() as temp:
        work = copied_work(Path(temp))
        active = work / "shared/controls/active-instruction.md"
        baseline = work / "shared/cases/PC-01/baseline.md"
        candidate = work / "shared/cases/PC-03/candidate-a.md"
        candidate_before = candidate.read_bytes()
        active.write_text("changed instruction")
        baseline.write_text("changed baseline")
        result = command(work / "scripts/restore_baseline.py", work)
        assert result.returncode == 0, result.stderr
        hashes = json.loads((work / "shared/baseline/hashes.json").read_text())["files"]
        for name, expected in hashes.items():
            target = active if name == "active-instruction.md" else work / "shared/cases" / Path(name).stem / "baseline.md"
            assert digest(target) == expected
        assert candidate.read_bytes() == candidate_before
        frozen = work / "shared/baseline/active-instruction.md"
        frozen.write_text("tampered restore authority")
        before = active.read_bytes()
        result = command(work / "scripts/restore_baseline.py", work)
        assert result.returncode == 1 and active.read_bytes() == before and "HOLD" in result.stderr


def paid_batch_fail_closed():
    spec = importlib.util.spec_from_file_location("slope_test_batch", ROOT / "scripts/stretch_runner.py")
    runner = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(runner)
    with tempfile.TemporaryDirectory() as temp:
        base = Path(temp)
        work = copied_work(base)
        destination = base / "comparison"
        result = command(ROOT / "scripts/stretch_runner.py", work, destination)
        assert result.returncode == 2 and "OPENROUTER_API_KEY unavailable" in result.stderr and not destination.exists()
        calls = []
        def failed_child(argv, **kwargs):
            calls.append(argv)
            child_work = Path(argv[argv.index("--workdir") + 1])
            (child_work / "brief.md").write_text("Incomplete file left by a failed child.")
            return subprocess.CompletedProcess(argv, 1, "HOLD: synthetic provider failure", "")
        with patch.dict(os.environ, {"OPENROUTER_API_KEY": "synthetic-test-only"}), patch.object(runner.subprocess, "run", side_effect=failed_child), contextlib.redirect_stdout(io.StringIO()):
            status = runner.main([str(work), str(destination)])
        report = json.loads((destination / "comparison.json").read_text())
        assert status == 1 and report["status"] == "HOLD" and report["recorded_attempts"] == 1 and len(calls) == 1
        assert (destination / "attempt-01/work/brief.md").read_text() == "Incomplete file left by a failed child."
        assert not (destination / "attempt-01/receipts").exists()
        assert report["checked_instruction_decision"] == "HOLD"

    # All following provider/launcher boundaries are synthetic, never live proof.
    for flags in (
        ["--local-budget-usd", "1"], ["--usage-baseline-usd", "0"],
        ["--local-budget-usd", "nan", "--usage-baseline-usd", "0"],
        ["--local-budget-usd", "inf", "--usage-baseline-usd", "0"],
        ["--local-budget-usd", "0", "--usage-baseline-usd", "0"],
        ["--local-budget-usd", "40.01", "--usage-baseline-usd", "0"],
        ["--local-budget-usd", "invalid", "--usage-baseline-usd", "0"],
        ["--local-budget-usd", "1", "--usage-baseline-usd", "-1"],
        ["--local-budget-usd", "1", "--usage-baseline-usd", "nan"],
        ["--local-budget-usd", "1", "--usage-baseline-usd", "inf"],
    ):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / "comparison"
            result = command(ROOT / "scripts/stretch_runner.py", Path(temp) / "work", destination, *flags)
            assert result.returncode == 2 and not destination.exists()

    token = "synthetic-private-value"
    valid_usage = {"usage": 10, "byok_usage": 2}

    class Response(io.BytesIO):
        status = 200

    class Opener:
        def __init__(self, body=None, error=None, redirect=False):
            self.body, self.error, self.redirect = body, error, redirect

        def open(self, request, timeout):
            assert request.full_url == "https://openrouter.ai/api/v1/key" and timeout == 15
            if self.error:
                raise self.error
            if self.redirect:
                # Exercise the real rejecting handler supplied to build_opener.
                handler.redirect_request(request, None, 302, "redirect", {}, "https://example.invalid/" + token)
            return Response(self.body)

    def opener_factory(opener):
        def build(value):
            nonlocal handler
            handler = value
            return opener
        return build

    handler = None
    bad_payloads = [b"x" * 65537, b"not JSON", b"{}", b'{"data":null}']
    for field in ("usage", "byok_usage"):
        for invalid in (True, -1, float("nan"), float("inf"), "12"):
            bad_payloads.append(json.dumps({"data": {**valid_usage, field: invalid}}).encode())
    bad_payloads.append(json.dumps({"data": {**valid_usage, "usage": None}}).encode())
    for opener in [*(Opener(body=body) for body in bad_payloads),
                   Opener(error=runner.urllib.error.URLError(token)),
                   Opener(error=runner.urllib.error.HTTPError("https://openrouter.ai/" + token, 401, token, {}, None)),
                   Opener(redirect=True)]:
        with patch.object(runner.urllib.request, "build_opener", side_effect=opener_factory(opener)):
            try:
                runner._read_key_usage(token)
                raise AssertionError("invalid metadata accepted")
            except ValueError as error:
                assert token not in str(error) and "key metadata" in str(error)
    with patch.object(runner.urllib.request, "build_opener", return_value=Opener(body=json.dumps({"data": {**valid_usage, "label": token}}).encode())):
        assert runner._read_key_usage(token) == valid_usage

    def observation(total):
        return {"usage": total, "byok_usage": 0}

    real_run = subprocess.run

    def batch(metadata, *, limit=1, baseline=10, failed=False, costs=(0.01,), rejected=False):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            work = copied_work(base)
            destination = base / "comparison"
            calls = []

            def child(argv, **kwargs):
                if "--workdir" not in argv:
                    return real_run(argv, **kwargs)  # Real supplied baseline restore.
                calls.append(argv)
                child_work = Path(argv[argv.index("--workdir") + 1])
                evidence = Path(argv[argv.index("--evidence") + 1])
                evidence.mkdir()
                (child_work / "brief.md").write_text("Retained synthetic partial output" if failed else "Synthetic budget-boundary observation")
                events = [{"type": "message_end", "message": {"role": "assistant", "usage": {"cost": {"total": cost}} if cost is not None else None}} for cost in costs]
                (evidence / "events.jsonl").write_text("".join(json.dumps(event) + "\n" for event in events))
                return subprocess.CompletedProcess(argv, 1 if failed else 0, "synthetic stdout", "synthetic stderr")

            def inspected(runtime, gates, child_work, evidence, frozen, attempt, instruction):
                passed = not (rejected and attempt["variant"] == "checked")
                return {"passed": passed, "format_ok": True, "mass_gate": passed, "zone_gate": True, "reason": "PASS" if passed else "sourced_mass", **runner.usage_summary(runtime.read_jsonl(evidence / "events.jsonl"))}

            with patch.dict(os.environ, {"OPENROUTER_API_KEY": token}), patch.object(runner, "_read_key_usage", side_effect=metadata), patch.object(runner.subprocess, "run", side_effect=child), patch.object(runner, "inspect_attempt", side_effect=inspected), contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                status = runner.main([str(work), str(destination), "--local-budget-usd", str(limit), "--usage-baseline-usd", str(baseline)])
            if not destination.exists():
                assert not calls
                return status, None, None
            report = json.loads((destination / "comparison.json").read_text())
            preregistration = json.loads((destination / "preregistration.json").read_text())
            assert report["recorded_attempts"] == len(calls)
            assert report["provider_billed_usd"] is None
            for index in range(1, len(calls) + 1):
                assert (destination / f"attempt-{index:02d}/work/brief.md").exists()
                launcher = json.loads((destination / f"attempt-{index:02d}/launcher.json").read_text())
                assert launcher["stdout"] == "synthetic stdout" and launcher["stderr"] == "synthetic stderr"
            assert not (destination / f"attempt-{len(calls) + 1:02d}").exists()
            return status, report, preregistration

    for metadata in ([ValueError("key metadata transport failure")], [observation(11)], [observation(9)]):
        status, report, _ = batch(metadata)
        assert status == 2 and report is None
    # Delayed usage since the caller's baseline consumes the allowance.
    status, report, _ = batch([observation(10.4), observation(10.4), observation(11), observation(11)])
    assert status == 1 and report["recorded_attempts"] == 1 and report["local_budget"]["admission_high_water_usd"] == 1
    # Partial SDK estimates still stop admission; the subtotal is not called complete.
    status, report, _ = batch([observation(10)] * 4, costs=(1, None))
    assert status == 1 and report["recorded_attempts"] == 1
    assert report["local_budget"]["known_sdk_estimated_usd"] == 1 and report["local_budget"]["sdk_estimate_complete"] is False
    # Failed children get post-call accounting and retain their original result.
    status, report, _ = batch([observation(10), observation(10), observation(10.2)], failed=True)
    assert status == 1 and report["recorded_attempts"] == 1 and report["attempts"][0]["launcher_exit_code"] == 1
    assert report["local_budget"]["observations"][-1]["stage"] == "after"
    for after in (observation(9), ValueError("key metadata transport failure")):
        status, report, _ = batch([observation(10), observation(10), after])
        assert status == 1 and report["recorded_attempts"] == 1 and report["local_budget"]["stop_reason"]
    # A content rejection is an outcome, never an early stop or retry.
    status, report, preregistration = batch([observation(10)] * 77, rejected=True)
    assert status == 0 and report["recorded_attempts"] == 38 and report["checked_instruction_decision"] == "REJECT"
    assert report["restore"]["exit_code"] == 0 and len(preregistration["schedule"]) == 38
    # Both restored controls have admission checks; equality refuses the next call.
    status, report, _ = batch([observation(10)] * 74 + [observation(11), observation(11)])
    assert status == 1 and report["recorded_attempts"] == 37 and report["restore"]["exit_code"] == 0
    # The final in-flight turn may overshoot without erasing complete observations.
    status, report, _ = batch([observation(10)] * 76 + [observation(11.25)])
    assert status == 0 and report["status"] == "COMPLETE" and report["recorded_attempts"] == 38
    assert report["local_budget"]["overshoot_usd"] == 0.25 and report["local_budget"]["stop_reason"]


def no_answer_leakage():
    paths = [ROOT / "README.md", *list((ROOT / "shared").rglob("*.md"))]
    text = "\n".join(path.read_text() for path in paths)
    assert not any(value in text for value in ("246 kg", "1,404 kg", "3 minutes late", "S07_VENDOR_VX-240", "VERIFY:", "CUSTODY:"))


def main():
    tests = {"M8-REF": reference, "M8-EVAL": evaluated_pairs, "M8-GATE": malformed_and_cell_boundaries, "M8-FREEZE": frozen_identity_refusal, "M8-SOURCE": source_errors_are_not_candidate_failures, "M8-RESTORE": restore_boundaries, "M8-LIVE-HOLD": paid_batch_fail_closed, "M8-LEAK": no_answer_leakage}
    for identifier, test in tests.items():
        try:
            test()
        except Exception as error:
            FAILURES.append(identifier)
            print(f"FAIL {identifier}: {type(error).__name__}: {error}")
        else:
            print(f"PASS {identifier}: {test.__name__}")
    return bool(FAILURES)


if __name__ == "__main__":
    raise SystemExit(main())
