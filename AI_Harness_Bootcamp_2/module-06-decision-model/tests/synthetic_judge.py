#!/usr/bin/env python3
"""Build launcher-shaped judge evidence that the shared auditor accepts. Offline tests only; never live proof."""
from __future__ import annotations

import json
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace

MODULE = Path(__file__).resolve().parents[1]
REPO = MODULE.parents[1]
sys.path.insert(0, str(REPO / "shared"))
import run_omp as runtime  # noqa: E402

BUILD = "openrouter/typesafe/jev-1.13-20260917"
OPTIONS = ["released_for_issue", "inspected", "received", "held", "not_stated"]


def answers_for(label: dict, *, claim: float | None = None, status: str | None = None, reversed_status: str | None = None,
                instruct: float | None = None, confidence: float = 0.95) -> dict:
    """Answers a careful judge would give for one desk label, with any field overridden."""
    status = status or label["note_status"]
    reversed_status = reversed_status or status

    def choice(selected: str, order: list[str]) -> dict:
        spread = round((1 - confidence) / (len(order) - 1), 4)
        return {"type": "choice", "choice": selected, "probabilities": {option: confidence if option == selected else spread for option in order}, "confidence": confidence}
    return {
        "claims_release": {"type": "bool", "bool": claim if claim is not None else (0.95 if label["note_status"] == "released_for_issue" else 0.03)},
        "note_status": choice(status, OPTIONS),
        "note_status_reversed": choice(reversed_status, list(reversed(OPTIONS))),
        "instructs_reader": {"type": "bool", "bool": instruct if instruct is not None else (0.95 if label["instructs"] else 0.04)},
        "urgency": {"type": "score", "score": 0.2, "legend": {"0": "Routine", "1": "Today", "2": "Immediate"}, "probabilities": {"0": 0.8, "1": 0.2, "2": 0.0}, "confidence": 0.7},
    }


def judge_run(work: Path, evidence_root: Path, name: str, split: str, answers: dict, *, model: str = BUILD, cost: float = 0.0008) -> dict:
    """Write one complete judge run: frozen inputs, outputs in the work folder, events, guard log, snapshots, and result."""
    evidence = evidence_root / name
    evidence.mkdir(parents=True)
    args = SimpleNamespace(judge_config=str(work / "JUDGE.yml"), judge_questions=str(work / "QUESTIONS.json"), judge_states=str(work / "shared/case/notes" / split), judge_output=f"out/{name}")
    prompt_text, judge = runtime.judge_launch_files(runtime.prepare_judge(args, work), work, evidence)
    (evidence / "prompt.md").write_text(prompt_text, encoding="utf-8")
    overlay = {"retry": {"enabled": False, "modelFallback": False}, "providers": {"cacheWarming": "off"}, "tools": {"approval": {"eval": "allow"}, "intentTracing": False}, "modelRoles": {"judge": runtime.JUDGE_SELECTOR}}
    (evidence / "runtime-config.yml").write_bytes(runtime.json_bytes(overlay))
    run_id = str(uuid.uuid4())
    policy = {"schema_version": 1, "run_id": run_id, "work_root": str(work), "profile": "judge", "tools": ["eval"], "write_files": [], "write_root": None,
              "provider": runtime.PROVIDER, "model": runtime.MODEL, "omp_version": runtime.OMP_VERSION, "prompt_sha256": runtime.file_hash(evidence / "prompt.md"),
              "instruction": None, "declaration": None, "python": sys.executable, "guard_source_sha256": runtime.file_hash(runtime.GUARD),
              "runtime_config_sha256": runtime.file_hash(evidence / "runtime-config.yml"), "guard_log": str(evidence / "guard.jsonl"), "watch_paths": [], "judge": judge}
    (evidence / "policy.json").write_bytes(runtime.json_bytes(policy))
    policy_hash = runtime.file_hash(evidence / "policy.json")
    started = datetime.now(timezone.utc).isoformat()
    before = runtime.snapshot(work, [])
    folder = work / "out" / name
    folder.mkdir()
    rows = [{"key": key, "answers": answers[key], "error": None, "model": model} for key in judge["states"]]
    (folder / "judgments.jsonl").write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")
    status = {"id": f"jdgb-{name}", "intent": f"Judging {len(rows)} states", "total": len(rows), "done": len(rows), "failed": 0, "cost": cost, "running": False, "model": model, "elapsedS": 2.0}
    (folder / "batch-status.json").write_text(json.dumps(status) + "\n", encoding="utf-8")
    after = runtime.snapshot(work, [])
    call_args = {"language": "js", "code": judge["cell_code"], "title": "Judge runner", "timeout": 120}
    text = f"judged {len(rows)}/{len(rows)}; failed 0; model {model}; cost {cost}"
    usage = {"cost": {"total": 0.03}}
    call = {"type": "toolCall", "id": "judge-1", "name": "eval", "arguments": call_args}
    assistant = {"role": "assistant", "provider": runtime.PROVIDER, "model": runtime.MODEL, "stopReason": "toolUse", "content": [call], "usage": usage}
    final = {"role": "assistant", "provider": runtime.PROVIDER, "model": runtime.MODEL, "stopReason": "stop", "content": [{"type": "text", "text": text}], "usage": usage}
    content = [{"type": "text", "text": text}]
    events = [{"type": "agent_start"}, {"type": "message_end", "message": assistant},
              {"type": "tool_execution_start", "toolCallId": "judge-1", "toolName": "eval", "args": call_args},
              {"type": "tool_execution_end", "toolCallId": "judge-1", "toolName": "eval", "result": {"content": content}, "isError": False},
              {"type": "message_end", "message": {"role": "toolResult", "toolCallId": "judge-1", "toolName": "eval", "content": content, "isError": False}},
              {"type": "message_end", "message": final}, {"type": "agent_end", "isTerminal": True, "messages": [assistant, final]}]
    request = {"type": "provider_request", "run_id": run_id, "provider": runtime.PROVIDER, "model": runtime.MODEL, "tools": ["eval"]}
    guard = [{"type": "guard_ready", "run_id": run_id, "provider": runtime.PROVIDER, "model": runtime.MODEL, "active_tools": ["eval"], "policy_sha256": policy_hash}, request,
             {"run_id": run_id, "type": "decision", "call_id": "judge-1", "tool": "eval", "arguments": call_args, "allow": True, "reason": "frozen judge cell"}, request,
             {"type": "guard_end", "run_id": run_id, "ready": True, "failed": False, "provider_requests": 2, "policy_sha256": policy_hash}]
    (evidence / "events.jsonl").write_text("".join(json.dumps(row) + "\n" for row in events), encoding="utf-8")
    (evidence / "guard.jsonl").write_text("".join(json.dumps(row) + "\n" for row in guard), encoding="utf-8")
    snapshots = {"before": before, "after": after}
    (evidence / "snapshots.json").write_bytes(runtime.json_bytes(snapshots))
    (evidence / "response.md").write_text(text, encoding="utf-8")
    (evidence / "stderr.txt").write_text("", encoding="utf-8")
    errors = runtime.validate_run(policy, events, guard, snapshots, 0)
    if errors:
        raise AssertionError(f"synthetic run is not launcher-shaped: {errors}")
    result = {"run_id": run_id, "provider": runtime.PROVIDER, "model": runtime.MODEL, "omp_version": runtime.OMP_VERSION, "started_at": started,
              "finished_at": datetime.now(timezone.utc).isoformat(), "exit_code": 0, "policy_sha256": policy_hash, "guard_sha256": runtime.file_hash(evidence / "guard.jsonl"),
              "declared_policy_sha256": None, "instruction_sha256": None,
              "input_sha256": {relative: value["sha256"] for relative, value in before["work"].items() if value["type"] == "file"},
              "output_sha256": {relative: value.get("sha256") for relative, value in after["work"].items() if value["type"] == "file" and value != before["work"].get(relative)},
              "status": "PASS", "reason": "complete guarded OMP turn; module content still requires its own check", "judge": runtime.judge_output_errors(policy)[1]}
    (evidence / "result.json").write_bytes(runtime.json_bytes(result))
    return result


def candidates(evidence_root: Path) -> None:
    folder = evidence_root / "judge-candidates"
    folder.mkdir(parents=True)
    (folder / "candidates.json").write_text(json.dumps({"models": [{"selector": runtime.JUDGE_SELECTOR}, {"selector": "openrouter/~typesafe/jev-latest"}]}), encoding="utf-8")
    (folder / "result.json").write_text(json.dumps({"omp_version": runtime.OMP_VERSION, "candidates": 2, "pinned": runtime.JUDGE_SELECTOR, "pinned_offered": True}), encoding="utf-8")
