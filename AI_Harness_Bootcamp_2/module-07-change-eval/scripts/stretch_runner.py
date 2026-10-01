#!/usr/bin/env python3
"""Run the preregistered 36 paired calls and two restored-baseline controls.

Usage: stretch_runner.py <prepared-workdir> <new-comparison-dir>
Configure the OpenRouter key's $40 ceiling unless staff explicitly supplies both
local-budget flags. Local admission is a soft stop, not a provider spending cap.
Calls are sequential, never retried or substituted.
"""
from __future__ import annotations

import argparse
import csv
import http.client
import importlib.util
import json
import math
import os
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1]
REFORMATION = MODULE.parents[1]
CASES = tuple(f"PC-{number:02d}" for number in range(1, 7))
VARIANTS = ("baseline", "checked")
PERMISSIONS = {"profile": "write_files", "tools": ["course_read", "course_write"], "write_files": ["brief.md"], "write_root": None}


def _read_key_usage(api_key: str) -> dict:
    """Read selected cumulative USD fields without redirects or secret errors."""
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, req, fp, code, msg, headers, newurl):
            raise ValueError("key metadata redirect refused")

    request = urllib.request.Request(
        "https://openrouter.ai/api/v1/key",
        headers={"Authorization": f"Bearer {api_key}", "Accept": "application/json"},
    )
    try:
        with urllib.request.build_opener(NoRedirect()).open(request, timeout=15) as response:
            if response.status != 200:
                raise ValueError("key metadata unexpected status")
            raw = response.read(65537)
        if len(raw) > 65536:
            raise ValueError("key metadata response too large")
        data = json.loads(raw)["data"]
        selected = {name: data[name] for name in ("usage", "byok_usage", "limit", "limit_remaining")}
        for name, value in selected.items():
            if value is None and name in {"limit", "limit_remaining"}:
                continue
            if type(value) not in (int, float) or not math.isfinite(value) or value < 0:
                raise ValueError("key metadata invalid numeric field")
        if not math.isfinite(selected["usage"] + selected["byok_usage"]):
            raise ValueError("key metadata invalid cumulative usage")
        return selected
    except urllib.error.HTTPError as error:
        raise ValueError(f"key metadata HTTP {error.code}") from None
    except (OSError, http.client.HTTPException):
        raise ValueError("key metadata transport failure") from None
    except (ValueError, KeyError, TypeError, OverflowError):
        raise ValueError("key metadata invalid response or redirect") from None


def _observe_budget(budget: dict, api_key: str, stage: str, attempt: int, *, admit: bool) -> None:
    try:
        usage = _read_key_usage(api_key)
        total = usage["usage"] + usage["byok_usage"]
        previous = budget["observations"][-1] if budget["observations"] else None
        if previous and any(usage[name] < previous[name] for name in ("usage", "byok_usage")):
            raise ValueError("key cumulative usage decreased")
        if total < budget["usage_baseline_usd"]:
            raise ValueError("usage baseline exceeds observed key usage")
        charge = max(total - budget["usage_baseline_usd"], budget["known_sdk_estimated_usd"], budget["admission_high_water_usd"])
        budget["admission_high_water_usd"] = charge
        budget["observations"].append({"stage": stage, "attempt": attempt, **usage, "key_usage_delta_usd": total - budget["usage_baseline_usd"], "known_sdk_estimated_usd": budget["known_sdk_estimated_usd"], "admission_charge_usd": charge})
        budget["overshoot_usd"] = max(0, charge - budget["limit_usd"])
        if charge >= budget["limit_usd"]:
            budget["stop_reason"] = "local budget reached; no further paid admissions"
            if admit:
                raise ValueError(budget["stop_reason"])
    except ValueError as error:
        budget["stop_reason"] = str(error)
        raise

def load_module(name: str, path: Path):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise ValueError(f"cannot load supplied adapter: {path.name}")
    module = importlib.util.module_from_spec(specification)
    sys.modules[name] = module
    specification.loader.exec_module(module)
    return module


def schedule() -> list[dict]:
    attempts = []
    for case_index, case_id in enumerate(CASES):
        for repeat in range(1, 4):
            order = VARIANTS if (case_index + repeat) % 2 else tuple(reversed(VARIANTS))
            for variant in order:
                attempts.append({"case_id": case_id, "repeat": repeat, "variant": variant, "kind": "paired"})
    attempts.extend({"case_id": case_id, "repeat": 1, "variant": "baseline", "kind": "restored-control"} for case_id in CASES[:2])
    return attempts


def frozen_paths(work: Path) -> dict[str, Path]:
    paths = {
        "instruction/baseline": work / "shared/controls/baseline-instruction.md",
        "instruction/checked": work / "shared/controls/candidate-checked-instruction.md",
        "gate": work / "shared/controls/hard_gates.py",
        "prompt": MODULE / "shared/controls/stretch-prompt.md",
        "restore": work / "scripts/restore_baseline.py",
        "baseline/hashes.json": work / "shared/baseline/hashes.json",
        "baseline/active-instruction.md": work / "shared/baseline/active-instruction.md",
    }
    for case_id in CASES:
        for name in ("sources.json", "form.md"):
            paths[f"{case_id}/{name}"] = work / "shared/cases" / case_id / name
    for number in range(1, 41):
        name = f"briefs/PC-{number:02d}.md"
        paths[f"baseline/{name}"] = work / "shared/baseline" / name
    return paths


def usage_summary(events: list[dict]) -> dict:
    usage = [row["message"].get("usage") for row in events if row.get("type") == "message_end" and row.get("message", {}).get("role") == "assistant"]
    estimates = [(item.get("cost") or {}).get("total") if isinstance(item, dict) else None for item in usage]
    valid = [value for value in estimates if type(value) in (int, float) and math.isfinite(value) and value >= 0]
    known = bool(estimates) and len(valid) == len(estimates)
    subtotal = sum(valid)
    if not math.isfinite(subtotal):
        raise ValueError("nonfinite SDK cost subtotal")
    return {"usage_records": usage, "sdk_estimated_usd": subtotal if known else None, "known_sdk_estimated_usd": subtotal, "sdk_estimate_complete": known, "missing_sdk_estimates": len(estimates) - len(valid) if estimates else 1, "provider_billed_usd": None}


def inspect_attempt(runtime, gates, work: Path, evidence: Path, frozen: dict, attempt: dict, instruction_path: Path) -> dict:
    errors = runtime.audit_evidence(evidence)
    if errors:
        raise ValueError("receipt audit: " + "; ".join(errors))
    policy = runtime.strict_json((evidence / "policy.json").read_text(encoding="utf-8"))
    result = runtime.strict_json((evidence / "result.json").read_text(encoding="utf-8"))
    expected_inputs = {name: frozen[f"{attempt['case_id']}/{name}"] for name in ("sources.json", "form.md")}
    if result["input_sha256"] != expected_inputs or any(runtime.file_hash(work / name) != digest for name, digest in expected_inputs.items()):
        raise ValueError("attempt inputs differ from the frozen source/form pair")
    if policy["work_root"] != str(work.resolve()) or {key: policy[key] for key in PERMISSIONS} != PERMISSIONS:
        raise ValueError("work root or normalized permissions changed")
    if policy["prompt_sha256"] != frozen["prompt"]:
        raise ValueError("prompt changed")
    descriptor = policy["instruction"]
    if descriptor != {"path": str(instruction_path.resolve()), "sha256": frozen[f"instruction/{attempt['variant']}"]}:
        raise ValueError("loaded instruction differs from preregistration")
    if (policy["provider"], policy["model"], policy["omp_version"]) != (runtime.PROVIDER, runtime.MODEL, runtime.OMP_VERSION):
        raise ValueError("provider/model/version drift")
    brief = work / "brief.md"
    if not brief.is_file() or result["output_sha256"] != {"brief.md": runtime.file_hash(brief)}:
        raise ValueError("missing or unreceipted tool-written brief")
    judged = gates.judge_brief(brief)
    return {**judged, "brief_sha256": runtime.file_hash(brief), "policy_sha256": result["policy_sha256"], **usage_summary(runtime.read_jsonl(evidence / "events.jsonl"))}


def summarize(rows: list[dict], restore: dict | None, status: str, reason: str) -> dict:
    paired = [row for row in rows if row["kind"] == "paired" and "passed" in row]
    per_case = []
    for case_id in CASES:
        selected = [row for row in paired if row["case_id"] == case_id]
        lookup = {(row["repeat"], row["variant"]): row for row in selected}
        disagreements = sum(lookup[(repeat, "baseline")]["passed"] != lookup[(repeat, "checked")]["passed"] for repeat in range(1, 4) if all((repeat, variant) in lookup for variant in VARIANTS))
        per_case.append({"case_id": case_id, "baseline_passes": sum(row["passed"] for row in selected if row["variant"] == "baseline"), "checked_passes": sum(row["passed"] for row in selected if row["variant"] == "checked"), "paired_disagreements": disagreements})
    failed_cases = {variant: sorted({row["case_id"] for row in paired if row["variant"] == variant and not row["passed"]}) for variant in VARIANTS}
    costs = [row.get("sdk_estimated_usd") for row in rows]
    complete_cost = bool(costs) and all(value is not None for value in costs)
    return {"status": status, "reason": reason, "planned_attempts": 38, "recorded_attempts": len(rows), "attempts": rows, "per_case": per_case, "failed_case_count": {variant: len(cases) for variant, cases in failed_cases.items()}, "failed_cases": failed_cases, "checked_instruction_decision": "REJECT" if failed_cases["checked"] else ("NO_OBSERVED_HARD_GATE_VIOLATION" if status == "COMPLETE" else "HOLD"), "restore": restore, "sdk_estimated_usd": sum(costs) if complete_cost else None, "provider_billed_usd": None, "limits": "Six paired cases and three repeats do not establish general superiority. SDK estimates are not provider billing."}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workdir", type=Path)
    parser.add_argument("comparison_dir", type=Path)
    parser.add_argument("--local-budget-usd", type=float)
    parser.add_argument("--usage-baseline-usd", type=float)
    args = parser.parse_args(argv)
    budget = None
    try:
        if (args.local_budget_usd is None) != (args.usage_baseline_usd is None):
            raise ValueError("supply both --local-budget-usd and --usage-baseline-usd")
        if args.local_budget_usd is not None:
            if not math.isfinite(args.local_budget_usd) or not 0 < args.local_budget_usd <= 40:
                raise ValueError("local budget must be finite and greater than zero, at most $40")
            if not math.isfinite(args.usage_baseline_usd) or args.usage_baseline_usd < 0:
                raise ValueError("usage baseline must be finite and nonnegative")
            budget = {"limit_usd": args.local_budget_usd, "usage_baseline_usd": args.usage_baseline_usd, "metric": "max(key_usage_delta,known_sdk_estimate)", "hard_cap": False, "observations": [], "known_sdk_estimated_usd": 0, "sdk_estimate_complete": True, "missing_sdk_estimates": 0, "admission_high_water_usd": 0, "overshoot_usd": 0, "stop_reason": None}
        work = args.workdir.expanduser().resolve()
        destination_input = args.comparison_dir.expanduser().absolute()
        if destination_input.exists() or destination_input.is_symlink():
            raise ValueError("comparison attempt already exists; preserve it and use a new directory")
        destination = destination_input.resolve()
        if work == destination or work.is_relative_to(destination) or destination.is_relative_to(work):
            raise ValueError("comparison and prepared work must be separate, non-overlapping directories")
        if not work.is_dir() or work.is_relative_to(REFORMATION):
            raise ValueError("use an existing external prepared Module 07 workdir")
        if not os.environ.get("OPENROUTER_API_KEY"):
            raise ValueError("OPENROUTER_API_KEY unavailable; no calls or attempt outputs were created")
        runtime = load_module("slope_course_runtime", REFORMATION / "shared/run_omp.py")
        paths = frozen_paths(work)
        if any(not path.is_file() or path.is_symlink() for path in paths.values()):
            raise ValueError("a supplied source, form, instruction, gate, or frozen baseline is missing/linked")
        frozen = {name: runtime.file_hash(path) for name, path in paths.items()}
        if frozen["instruction/baseline"] != frozen["baseline/active-instruction.md"]:
            raise ValueError("baseline instruction differs from the frozen restore copy")
        if frozen["instruction/baseline"] == frozen["instruction/checked"]:
            raise ValueError("comparison instructions are identical")
        gates = load_module("slope_live_hard_gates", paths["gate"])
        for case_id in CASES:
            packet = gates.load_sources(paths[f"{case_id}/sources.json"])
            if packet["case_id"] != case_id:
                raise ValueError("case identity differs from its directory")
        if budget is not None:
            _observe_budget(budget, os.environ["OPENROUTER_API_KEY"], "preflight", 0, admit=True)
            budget["provider_limit_usd"] = budget["observations"][0]["limit"]
    except (OSError, ValueError, ImportError) as error:
        print(f"HOLD: {error}", file=sys.stderr)
        return 2

    destination.mkdir(parents=True, exist_ok=False)
    configuration = destination / "frozen"
    configuration.mkdir()
    for variant in VARIANTS:
        shutil.copyfile(paths[f"instruction/{variant}"], configuration / f"{variant}.md")
    shutil.copyfile(paths["prompt"], configuration / "prompt.md")
    policy = {"schema_version": 1, "case_ids": list(CASES), "repeats": 3, "schedule": schedule(), "provider": runtime.PROVIDER, "model": runtime.MODEL, "omp_version": runtime.OMP_VERSION, "frozen_sha256": frozen, "permissions": PERMISSIONS, "hard_gates": ["sourced_mass", "labeled_gate_time"], "aggregation": "any_violation_rejects", "exclusions": [], "cost_proxy": "failed_case_count", "provider_key_spend_ceiling_usd_prerequisite": 40, "provider_ceiling_verified_by_adapter": False, "max_simultaneous_paid_calls": 1}
    if budget is not None:
        policy["provider_key_spend_ceiling_usd_prerequisite"] = None
        policy["local_budget"] = {name: budget[name] for name in ("limit_usd", "usage_baseline_usd", "provider_limit_usd", "metric", "hard_cap")}
    policy_path = destination / "preregistration.json"
    policy_path.write_bytes(runtime.json_bytes(policy))
    policy_hash = runtime.file_hash(policy_path)
    rows, restoration = [], None
    status, reason = "HOLD", "comparison did not complete"
    try:
        for index, attempt in enumerate(policy["schedule"], 1):
            if runtime.file_hash(policy_path) != policy_hash or any(runtime.file_hash(path) != frozen[name] for name, path in paths.items()):
                raise ValueError("preregistered policy, input, instruction, gate, or baseline changed")
            if budget is not None:
                _observe_budget(budget, os.environ["OPENROUTER_API_KEY"], "before", index, admit=True)
            if index == 37:
                active = work / "shared/controls/active-instruction.md"
                if active.is_symlink() or not active.resolve().is_relative_to(work):
                    raise ValueError("active instruction is linked/outside work")
                # Select the checked condition, then use the actual supplied restore.
                before = active.read_bytes()
                (destination / "active-before-restore-selection.md").write_bytes(before)
                active.write_bytes((configuration / "checked.md").read_bytes())
                restored = subprocess.run([sys.executable, str(paths["restore"]), str(work)], capture_output=True, text=True, timeout=30)
                restoration = {"exit_code": restored.returncode, "stdout": restored.stdout, "stderr": restored.stderr, "selected_sha256": frozen["instruction/checked"], "restored_sha256": runtime.file_hash(active)}
                (destination / "restore.json").write_bytes(runtime.json_bytes(restoration))
                if restored.returncode or runtime.file_hash(active) != frozen["instruction/baseline"]:
                    raise ValueError("baseline restore failed; restored controls were not run")
            attempt_root = destination / f"attempt-{index:02d}"
            attempt_work = attempt_root / "work"
            attempt_work.mkdir(parents=True, exist_ok=False)
            evidence = attempt_root / "receipts"  # Only the launcher creates E.
            for name in ("sources.json", "form.md"):
                shutil.copyfile(paths[f"{attempt['case_id']}/{name}"], attempt_work / name)
            instruction = configuration / f"{attempt['variant']}.md"
            if attempt["kind"] == "restored-control":
                instruction = attempt_root / "restored-instruction.md"
                shutil.copyfile(work / "shared/controls/active-instruction.md", instruction)
            if runtime.file_hash(instruction) != frozen[f"instruction/{attempt['variant']}"] or runtime.file_hash(configuration / "prompt.md") != frozen["prompt"]:
                raise ValueError("attempt instruction or prompt changed before launch")
            command = [sys.executable, str(REFORMATION / "shared/run_omp.py"), "--workdir", str(attempt_work), "--prompt", str(configuration / "prompt.md"), "--evidence", str(evidence), "--instruction", str(instruction), "--allow-write", "brief.md"]
            started = time.monotonic()
            launch_error = None
            try:
                completed = subprocess.run(command, capture_output=True, text=True, timeout=370)
                exit_code, stdout, stderr = completed.returncode, completed.stdout, completed.stderr
            except (OSError, subprocess.TimeoutExpired) as error:
                launch_error = f"attempt {index} launcher {type(error).__name__}; retained first failure, no retry"
                exit_code = None
                stdout, stderr = getattr(error, "stdout", None) or "", getattr(error, "stderr", None) or ""
                stdout = stdout.decode("utf-8", errors="replace") if isinstance(stdout, bytes) else stdout
                stderr = stderr.decode("utf-8", errors="replace") if isinstance(stderr, bytes) else stderr
            row = {"attempt": index, **attempt, "wall_seconds": round(time.monotonic() - started, 6), "launcher_exit_code": exit_code, "evidence": str(evidence.relative_to(destination))}
            rows.append(row)
            (attempt_root / "launcher.json").write_bytes(runtime.json_bytes({"command": command, "exit_code": exit_code, "stdout": stdout, "stderr": stderr, "error": launch_error}))
            if budget is not None:
                try:
                    costs = usage_summary(runtime.read_jsonl(evidence / "events.jsonl"))
                except (OSError, ValueError, KeyError, TypeError):
                    costs = usage_summary([])
                row.update(costs)
                budget["known_sdk_estimated_usd"] += costs["known_sdk_estimated_usd"]
                budget["sdk_estimate_complete"] &= costs["sdk_estimate_complete"]
                budget["missing_sdk_estimates"] += costs["missing_sdk_estimates"]
                _observe_budget(budget, os.environ["OPENROUTER_API_KEY"], "after", index, admit=False)
            if launch_error or exit_code:
                raise ValueError(launch_error or f"attempt {index} did not complete; retained first failure, no retry")
            row.update(inspect_attempt(runtime, gates, attempt_work, evidence, frozen, attempt, instruction))
            if runtime.file_hash(policy_path) != policy_hash or any(runtime.file_hash(path) != frozen[name] for name, path in paths.items()):
                raise ValueError("frozen comparison identity changed during an attempt")
            print(f"RECORDED {index}/38: {attempt['case_id']} {attempt['variant']} {row['reason']}", flush=True)
            estimates = [item.get("sdk_estimated_usd") for item in rows]
            if budget is None and index < 38 and all(value is not None for value in estimates) and sum(estimates) >= 40:
                raise ValueError("SDK estimated cost reached $40; stop and inspect actual provider billing/cap")
        status, reason = "COMPLETE", "38 independently receipted and classified attempts; no missing pairs or restore controls"
    except (OSError, ValueError, KeyError, TypeError, subprocess.TimeoutExpired) as error:
        reason = str(error)
    report = summarize(rows, restoration, status, reason)
    report["preregistration_sha256"] = policy_hash
    if budget is not None:
        report["local_budget"] = budget
    (destination / "comparison.json").write_bytes(runtime.json_bytes(report))
    columns = ("attempt", "case_id", "repeat", "variant", "kind", "passed", "format_ok", "mass_gate", "zone_gate", "reason", "wall_seconds", "sdk_estimated_usd", "provider_billed_usd", "evidence")
    with (destination / "attempts.csv").open("x", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(f"{status}: {reason}")
    return 0 if status == "COMPLETE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
