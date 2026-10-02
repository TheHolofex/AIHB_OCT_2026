#!/usr/bin/env python3
"""Deterministic launcher regressions. Synthetic receipts never count as live proof."""
from __future__ import annotations
import copy
import importlib.util
import json
import os
import subprocess
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
LAUNCHER = ROOT / "shared/run_omp.py"
SPEC = importlib.util.spec_from_file_location("run_omp", LAUNCHER)
runtime = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runtime)


class LauncherBehavior(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="course-launch-test-")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.work = self.base / "work"
        self.work.mkdir()
        (self.work / "source.txt").write_text("input", encoding="utf-8")
        self.prompt = self.base / "prompt.md"
        self.prompt.write_text("Read source.txt without changing it.", encoding="utf-8")
        self.evidence = self.base / "evidence"

    def cli(self, extra=(), key=""):
        environment = dict(os.environ, OPENROUTER_API_KEY=key)
        return subprocess.run([sys.executable, str(LAUNCHER), "--workdir", str(self.work), "--prompt", str(self.prompt), "--evidence", str(self.evidence), *extra], capture_output=True, text=True, env=environment, cwd=self.base, timeout=20)

    def test_missing_key_stops_without_runtime_outputs_or_work_mutation(self):
        before = runtime.work_snapshot(self.work)
        result = self.cli()
        self.assertEqual(result.returncode, 2)
        self.assertIn("OPENROUTER_API_KEY unavailable", result.stderr)
        self.assertFalse(self.evidence.exists())
        self.assertEqual(runtime.work_snapshot(self.work), before)

    def test_missing_empty_instruction_and_permission_conflicts_are_prerequisites(self):
        empty = self.base / "empty.md"
        empty.write_text(" \n", encoding="utf-8")
        for args in (("--instruction", str(self.base / "missing")), ("--instruction", str(empty)), ("--allow-write", "../escape"), ("--allow-write", "source.txt"), ("--mcp-config", "missing.json"), ("--authority", "missing.md"), ("--mcp-config", "missing.json", "--authority", "missing.md", "--allow-write", "new.txt")):
            with self.subTest(args=args):
                result = self.cli(args)
                self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
                self.assertFalse(self.evidence.exists())

    def test_declared_policy_exact_schema_and_unknown_keys(self):
        declaration = self.work / "AGENT_POLICY.md"
        declaration.write_text("# Policy\n\n```json\n" + json.dumps(runtime.DECLARATION) + "\n```\n", encoding="utf-8")
        self.assertEqual(runtime.parse_declaration(declaration), runtime.DECLARATION)
        for update in ({"extra": True}, {"write_root": "."}, {"tools": ["course_read"]}, {"yolo": True}):
            changed = {**runtime.DECLARATION, **update}
            declaration.write_text("```json\n" + json.dumps(changed) + "\n```\n", encoding="utf-8")
            with self.subTest(update=update), self.assertRaises(ValueError):
                runtime.parse_declaration(declaration)
        with self.assertRaisesRegex(ValueError, "duplicate"):
            runtime.strict_json('{"enabled":true,"enabled":false}')

    def test_isolation_removes_author_state_and_keeps_only_course_credential(self):
        isolated = self.base / "runtime"
        isolated.mkdir()
        poison = {"PI_CODING_AGENT_DIR": "/author", "OMP_PROFILE": "author", "ANTHROPIC_API_KEY": "direct", "OPENAI_API_KEY": "direct", "OPENROUTER_BASE_URL": "bad", "COURSE_GUARD_POLICY": "bad", "HOME": "/author", "APPDATA": "/author", "LANG": "C", "HTTPS_PROXY": "http://proxy.invalid"}
        with patch.dict(os.environ, poison):
            environment = runtime.isolated_env(isolated, self.evidence / "policy.json", "synthetic-key")
        self.assertFalse(set(poison).intersection(environment) - {"HOME", "APPDATA", "LANG", "HTTPS_PROXY", "COURSE_GUARD_POLICY"})
        self.assertEqual(environment["OPENROUTER_API_KEY"], "synthetic-key")
        self.assertEqual(environment["COURSE_GUARD_POLICY"], str(self.evidence / "policy.json"))
        for name in ("HOME", "USERPROFILE", "APPDATA", "LOCALAPPDATA", "XDG_CONFIG_HOME", "XDG_STATE_HOME"):
            self.assertTrue(Path(environment[name]).is_relative_to(isolated))

    def receipt(self):
        policy = dict.fromkeys(runtime.POLICY_KEYS)
        policy.update(schema_version=1, run_id="synthetic", work_root=str(self.work), profile="read", tools=["course_read"], write_files=[], write_root=None, provider=runtime.PROVIDER, model=runtime.MODEL, omp_version=runtime.OMP_VERSION)
        assistant = {"role": "assistant", "provider": runtime.PROVIDER, "model": runtime.MODEL, "stopReason": "stop", "content": [{"type": "text", "text": "Source describes custody only."}]}
        events = [{"type": "agent_start"}, {"type": "message_end", "message": assistant}, {"type": "agent_end", "isTerminal": True, "messages": [assistant]}]
        guard = [{"type": "guard_ready", "run_id": "synthetic", "provider": runtime.PROVIDER, "model": runtime.MODEL, "active_tools": ["course_read"]}, {"type": "provider_request", "run_id": "synthetic", "provider": runtime.PROVIDER, "model": runtime.MODEL}, {"type": "guard_end", "run_id": "synthetic", "ready": True, "failed": False, "provider_requests": 1}]
        before = runtime.snapshot(self.work, [self.base / "outside.txt"])
        return policy, events, guard, {"before": before, "after": copy.deepcopy(before)}

    def test_incomplete_error_duplicate_or_drift_receipts_hold(self):
        policy, events, guard, snapshots = self.receipt()
        self.assertEqual(runtime.validate_run(policy, events, guard, snapshots, 0), [])
        for reason in ("no-terminal", "duplicate-terminal", "truncated", "model-drift", "missing-guard", "retry", "guard-failed", "request-count", "offline-cutoff"):
            p, e, g, s = copy.deepcopy((policy, events, guard, snapshots))
            if reason == "no-terminal": e[-1]["isTerminal"] = False
            elif reason == "duplicate-terminal": e.append(e[-1])
            elif reason == "truncated": e[1]["message"]["stopReason"] = "length"
            elif reason == "model-drift": e[1]["message"]["model"] = "other"
            elif reason == "missing-guard": g.pop()
            elif reason == "retry": e.insert(1, {"type": "auto_retry_start"})
            elif reason == "guard-failed": g[-1]["failed"] = True
            elif reason == "request-count": g[-1]["provider_requests"] = 2
            elif reason == "offline-cutoff": e = [{"type": "session"}]; g.pop(1); g[-1]["provider_requests"] = 0
            with self.subTest(reason=reason):
                self.assertTrue(runtime.validate_run(p, e, g, s, 0))

    def test_session_completion_timestamp_does_not_mask_terminal_drift(self):
        policy, events, guard, snapshots = self.receipt()
        events[1]["message"] = copy.deepcopy(events[1]["message"])
        events[1]["message"]["completedAt"] = 1790808511557
        self.assertEqual(runtime.validate_run(policy, events, guard, snapshots, 0), [])
        for field, value in (
            ("content", [{"type": "text", "text": "Changed answer"}]),
            ("model", "other"),
            ("stopReason", "error"),
            ("usage", {"cost": {"total": 999}}),
            ("timestamp", 123),
            ("completedAt", 1790808511558),
        ):
            changed = copy.deepcopy(events)
            changed[-1]["messages"][-1][field] = value
            with self.subTest(field=field):
                self.assertIn("terminal and streamed assistant records disagree", runtime.validate_run(policy, changed, guard, snapshots, 0))

    def test_unpaired_calls_and_forbidden_effects_hold(self):
        policy, events, guard, snapshots = self.receipt()
        events[1]["message"]["content"].append({"type": "toolCall", "id": "unpaired", "name": "course_read", "arguments": {"path": "source.txt"}})
        self.assertIn("unmatched assistant calls, executions, or results", runtime.validate_run(policy, events, guard, snapshots, 0))
        policy, events, guard, snapshots = self.receipt()
        snapshots["after"]["work"]["source.txt"]["sha256"] = "changed"
        snapshots["after"]["work"]["release.txt"] = {"type": "file", "sha256": "unreceipted"}
        snapshots["after"]["watch"][str(self.base / "outside.txt")] = {"type": "file", "sha256": "forbidden"}
        errors = runtime.validate_run(policy, events, guard, snapshots, 0)
        self.assertIn("watched target changed", errors)
        self.assertTrue(any("existing input/control" in error for error in errors))
        self.assertTrue(any("unreceipted output" in error for error in errors))

    def test_successful_tool_receipts_bind_execution_identity_path_and_order(self):
        policy, events, guard, snapshots = self.receipt()
        call = {"type": "toolCall", "id": "read-1", "name": "course_read", "arguments": {"path": "source.txt"}}
        assistant = {"role": "assistant", "provider": runtime.PROVIDER, "model": runtime.MODEL, "stopReason": "toolUse", "content": [call]}
        content = [{"type": "text", "text": "input"}]
        events[1:1] = [
            {"type": "message_end", "message": assistant},
            {"type": "tool_execution_start", "toolCallId": "read-1", "toolName": "course_read", "args": call["arguments"]},
            {"type": "tool_execution_end", "toolCallId": "read-1", "toolName": "course_read", "result": {"content": content}, "isError": False},
            {"type": "message_end", "message": {"role": "toolResult", "toolCallId": "read-1", "toolName": "course_read", "content": content, "isError": False}},
        ]
        decision = {"run_id": "synthetic", "type": "decision", "call_id": "read-1", "tool": "course_read", "arguments": call["arguments"], "allow": True, "resolved_path": str(self.work / "source.txt")}
        guard[-1:-1] = [decision, {**decision, "type": "execution_check"}, {"run_id": "synthetic", "type": "executed", "call_id": "read-1", "tool": "course_read", "resolved_path": str(self.work / "source.txt"), "output_sha256": None}]
        self.assertEqual(runtime.validate_run(policy, events, guard, snapshots, 0), [])
        for defect in ("wrong-tool", "wrong-path", "execution-before-authorization", "authorized-outside-read"):
            changed = copy.deepcopy(guard)
            if defect == "wrong-tool": changed[-2]["tool"] = "course_write"
            elif defect == "wrong-path": changed[-2]["resolved_path"] = str(self.base / "outside.txt")
            elif defect == "execution-before-authorization": changed[2:5] = [changed[4], changed[2], changed[3]]
            else:
                for row in changed[2:5]:
                    row["resolved_path"] = str(self.base / "outside.txt")
            with self.subTest(defect=defect):
                self.assertTrue(runtime.validate_run(policy, events, changed, snapshots, 0))

    def test_saved_evidence_rejects_altered_result_hashes_and_later_forbidden_effects(self):
        policy, events, guard, snapshots = self.receipt()
        self.evidence.mkdir()
        overlay = {"retry": {"enabled": False, "modelFallback": False}, "providers": {"cacheWarming": "off"}, "tools": {"approval": {"course_read": "allow"}, "intentTracing": False}}
        (self.evidence / "runtime-config.yml").write_bytes(runtime.json_bytes(overlay))
        policy["runtime_config_sha256"] = runtime.file_hash(self.evidence / "runtime-config.yml")
        (self.evidence / "policy.json").write_bytes(runtime.json_bytes(policy))
        policy_hash = runtime.file_hash(self.evidence / "policy.json")
        for row in guard:
            if row["type"] in {"guard_ready", "guard_end"}:
                row["policy_sha256"] = policy_hash
        for name, rows in (("events", events), ("guard", guard)):
            (self.evidence / f"{name}.jsonl").write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")
        (self.evidence / "snapshots.json").write_bytes(runtime.json_bytes(snapshots))
        result = {"run_id": "synthetic", "provider": runtime.PROVIDER, "model": runtime.MODEL, "omp_version": runtime.OMP_VERSION, "status": "PASS", "exit_code": 0, "policy_sha256": policy_hash, "guard_sha256": runtime.file_hash(self.evidence / "guard.jsonl"), "instruction_sha256": None, "declared_policy_sha256": None, "input_sha256": {"source.txt": runtime.file_hash(self.work / "source.txt")}, "output_sha256": {}}
        (self.evidence / "result.json").write_bytes(runtime.json_bytes(result))
        (self.evidence / "response.md").write_text("Source describes custody only.", encoding="utf-8")
        self.assertEqual(runtime.audit_evidence(self.evidence), [])
        (self.evidence / "response.md").write_text("A substituted answer.", encoding="utf-8")
        self.assertIn("saved response differs from final assistant event", runtime.audit_evidence(self.evidence))
        (self.evidence / "response.md").write_text("Source describes custody only.", encoding="utf-8")
        altered = {**result, "input_sha256": {}}
        (self.evidence / "result.json").write_bytes(runtime.json_bytes(altered))
        self.assertIn("input_sha256 differs", runtime.audit_evidence(self.evidence))
        (self.evidence / "result.json").write_bytes(runtime.json_bytes(result))
        (self.base / "outside.txt").write_text("forbidden later effect")
        self.assertTrue(any("watched target changed after" in error for error in runtime.audit_evidence(self.evidence)))

    def test_jsonl_rejects_partial_or_non_event_records(self):
        target = self.base / "stream.jsonl"
        for raw in (b'{"type":"agent_end"}', b'{"type":', b'{}\n', b'\n'):
            target.write_bytes(raw)
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                runtime.read_jsonl(target)

    def mcp_receipt(self):
        """A synthetic MCP run: one allowed read, one server refusal, one runtime refusal, one new draft."""
        known = [f"mcp__vault_{name}" for name in ("list_directory", "read_note", "read_multiple_notes", "search_notes", "get_frontmatter", "get_vault_stats", "write_note", "patch_note", "update_frontmatter", "manage_tags", "move_note", "delete_note")]
        allow = ["mcp__vault_read_note", "mcp__vault_write_note"]
        flags = {"read_only": False, "read_prefixes": ["Sources/"], "write_prefixes": ["Drafts/"], "no_overwrite": True, "max_results": 20}
        offered = [name.removeprefix("mcp__vault_") for name in known]
        policy = dict.fromkeys(runtime.POLICY_KEYS)
        policy.update(schema_version=1, run_id="synthetic", work_root=str(self.work), profile="mcp", tools=[], write_files=[], write_root=None, provider=runtime.PROVIDER, model=runtime.MODEL, omp_version=runtime.OMP_VERSION)
        policy["mcp"] = {"server": "vault", "script": {"path": "vault_mcp.py", "sha256": "script"}, "phase": "research", "allow_tools": ["read_note", "write_note"], "allow_names": allow, "known_names": known,
                         "read_scope": ["Sources/"], "write_scope": ["Drafts/"], "create_only": True, "flags": flags, "tools_offered": offered}
        policy["snapshot_exclude"] = ["vault/.obsidian"]
        shutil.rmtree(self.work / "vault", ignore_errors=True)
        (self.work / "vault/Sources").mkdir(parents=True)
        (self.work / "vault/Drafts").mkdir()
        (self.work / "vault/Sources/KH-001.md").write_text("source", encoding="utf-8")
        draft = "# finding\n"
        digest = runtime.sha256(draft.encode())
        calls = [("read-1", "mcp__vault_read_note", {"path": "Sources/KH-001.md"}), ("deny-1", "mcp__vault_write_note", {"path": "Sources/KH-001.md", "content": "x", "mode": "overwrite"}),
                 ("gone-1", "mcp__vault_patch_note", {"path": "Sources/KH-001.md", "oldString": "s", "newString": "t"}), ("write-1", "mcp__vault_write_note", {"path": "Drafts/finding.md", "content": draft, "mode": "create"})]
        blocks = [{"type": "toolCall", "id": identifier, "name": name, "arguments": arguments} for identifier, name, arguments in calls]
        assistant = {"role": "assistant", "provider": runtime.PROVIDER, "model": runtime.MODEL, "stopReason": "toolUse", "content": blocks}
        final = {"role": "assistant", "provider": runtime.PROVIDER, "model": runtime.MODEL, "stopReason": "stop", "content": [{"type": "text", "text": "done"}]}
        events = [{"type": "agent_start"}, {"type": "message_end", "message": assistant}]
        failed = {"deny-1": "DENIED: OUTSIDE_WRITE_SCOPE refused", "gone-1": "Tool mcp__vault_patch_note not found"}
        for identifier, name, arguments in calls:
            text = failed.get(identifier, "ok")
            content = [{"type": "text", "text": text}]
            events += [{"type": "tool_execution_start", "toolCallId": identifier, "toolName": name, "args": arguments},
                       {"type": "tool_execution_end", "toolCallId": identifier, "toolName": name, "result": {"content": content}, "isError": identifier in failed},
                       {"type": "message_end", "message": {"role": "toolResult", "toolCallId": identifier, "toolName": name, "content": content, "isError": identifier in failed, "details": {"mcpToolName": name.removeprefix("mcp__vault_")}}}]
        events += [{"type": "message_end", "message": final}, {"type": "agent_end", "isTerminal": True, "messages": [assistant, final]}]
        decisions = [{"run_id": "synthetic", "type": "decision", "call_id": identifier, "tool": name, "arguments": arguments, "allow": True} for identifier, name, arguments in calls if identifier != "gone-1"]
        guard = [{"type": "guard_ready", "run_id": "synthetic", "provider": runtime.PROVIDER, "model": runtime.MODEL, "active_tools": sorted(allow)}, *decisions,
                 {"type": "provider_request", "run_id": "synthetic", "provider": runtime.PROVIDER, "model": runtime.MODEL, "tools": sorted(allow)},
                 {"type": "guard_end", "run_id": "synthetic", "ready": True, "failed": False, "provider_requests": 1}]
        redact = runtime.redact_arguments
        audit = [{"seq": 1, "type": "server_start", "flags": flags, "script_sha256": "script", "tools_offered": offered},
                 {"seq": 2, "type": "tool_call", "tool": "read_note", "arguments": {"path": "Sources/KH-001.md"}, "allowed": True, "is_error": False, "reads": ["Sources/KH-001.md"], "effect": None},
                 {"seq": 3, "type": "tool_call", "tool": "write_note", "arguments": redact(calls[1][2]), "allowed": False, "is_error": True, "reads": [], "effect": None},
                 {"seq": 4, "type": "tool_call", "tool": "write_note", "arguments": redact(calls[3][2]), "allowed": True, "is_error": False, "reads": [], "effect": {"op": "create", "path": "Drafts/finding.md", "sha256_before": None, "sha256_after": digest}}]
        before = runtime.snapshot(self.work, [], ("vault/.obsidian",))
        (self.work / "vault/Drafts/finding.md").write_text(draft, encoding="utf-8")
        after = runtime.snapshot(self.work, [], ("vault/.obsidian",))
        return policy, events, guard, {"before": before, "after": after}, audit

    def test_mcp_receipts_join_each_call_to_the_servers_own_audit_and_the_disk(self):
        policy, events, guard, snapshots, audit = self.mcp_receipt()
        self.assertEqual(runtime.validate_run(policy, events, guard, snapshots, 0, audit), [])
        calls = {block["id"]: block for row in events if row.get("type") == "message_end" for block in row["message"].get("content", []) if block.get("type") == "toolCall"}
        results = {row["message"]["toolCallId"]: row["message"] for row in events if row.get("type") == "message_end" and row["message"].get("role") == "toolResult"}
        ends = {row["toolCallId"]: row for row in events if row.get("type") == "tool_execution_end"}
        decisions = {row["call_id"]: row for row in guard if row["type"] == "decision"}
        records, errors = runtime.join_mcp(policy, calls, results, ends, decisions, audit)
        self.assertEqual(errors, [])
        self.assertEqual([record["classification"] for record in records], ["EXECUTED", "DENIED_BY_SERVER", "DENIED_BY_RUNTIME", "EXECUTED"])
        self.assertEqual(records[3]["effect"]["path"], "Drafts/finding.md")

    def test_mcp_receipts_hold_on_missing_extra_or_contradicting_server_records(self):
        defects = {
            "a successful call with no audit row": ("no matching server audit row", lambda p, e, g, s, a: a.pop(1)),
            "an audit call the harness never made": ("never made", lambda p, e, g, s, a: a.append({"seq": 5, "type": "tool_call", "tool": "read_note", "arguments": {"path": "Sources/KH-002.md"}, "allowed": True, "is_error": False, "reads": [], "effect": None})),
            "a read outside the declared scope": ("outside read_scope", lambda p, e, g, s, a: a[1].update(reads=["Estimate/Calibration.md"])),
            "a server that started with other limits": ("limits that differ", lambda p, e, g, s, a: a[0].update(flags={**a[0]["flags"], "no_overwrite": False})),
            "a server that offered other tools": ("different tool set", lambda p, e, g, s, a: a[0].update(tools_offered=["read_note"])),
            "an overwrite although create_only is declared": ("create_only is declared", lambda p, e, g, s, a: a[3]["effect"].update(op="overwrite")),
            "a write outside the declared folder": ("outside write_scope", lambda p, e, g, s, a: a[3]["effect"].update(path="Estimate/finding.md")),
            "a change to a source note": ("unreceipted vault change", lambda p, e, g, s, a: s["after"]["work"].__setitem__("vault/Sources/KH-001.md", {"type": "file", "sha256": "changed"})),
            "a file nobody receipted": ("unreceipted vault change", lambda p, e, g, s, a: s["after"]["work"].__setitem__("vault/Drafts/stray.md", {"type": "file", "sha256": "stray"})),
            "a provider request that offered an undeclared tool": ("outside the declaration", lambda p, e, g, s, a: g[-2].update(tools=["mcp__vault_read_note", "mcp__vault_write_note", "mcp__vault_delete_note"])),
            "a declared tool that was not active": ("active tools differ", lambda p, e, g, s, a: g[0].update(active_tools=["mcp__vault_read_note"])),
        }
        for label, (fragment, defect) in defects.items():
            policy, events, guard, snapshots, audit = self.mcp_receipt()
            defect(policy, events, guard, snapshots, audit)
            with self.subTest(label):
                errors = runtime.validate_run(policy, events, guard, snapshots, 0, audit)
                self.assertTrue(any(fragment in error for error in errors), f"{label}: {errors}")

    def test_a_revoked_phase_holds_when_any_call_reaches_a_server(self):
        policy, events, guard, snapshots, audit = self.mcp_receipt()
        policy["mcp"].update(phase="revoked", allow_names=[], allow_tools=[], read_scope=[], write_scope=[], create_only=False, server=None, flags=None, script=None, tools_offered=[])
        guard[0]["active_tools"] = []
        guard[-2]["tools"] = []
        self.assertTrue(any("revoked phase executed or reached a tool" in error for error in runtime.validate_run(policy, events, guard, snapshots, 0, audit)))

    def test_a_connection_that_differs_from_its_declaration_is_refused_before_any_model_call(self):
        work = self.base / "mcp-work"
        script = work / "shared/mcp/vault_mcp.py"
        script.parent.mkdir(parents=True)
        script.write_bytes((ROOT / "AI_Harness_Bootcamp_2/module-03-mcp-research/shared/mcp/vault_mcp.py").read_bytes())
        (work / "vault").mkdir()
        declaration = {"schema_version": 1, "phase": "research", "allow_tools": ["read_note", "write_note"], "read_scope": ["Sources/"], "write_scope": ["Drafts/research/"], "create_only": True}
        entry = lambda *flags: {"mcpServers": {"vault": {"type": "stdio", "command": "python", "args": [str(script), "--root", str(work / "vault"), *flags]}}}
        matching = ["--read-prefix", "Sources/", "--write-prefix", "Drafts/research/", "--no-overwrite"]

        def prepare(config, declared=declaration):
            (work / "mcp.json").write_text(json.dumps(config), encoding="utf-8")
            (work / "AUTHORITY.md").write_text("```json\n" + json.dumps(declared) + "\n```\n", encoding="utf-8")
            return runtime.prepare_mcp({"path": str(work / "mcp.json")}, {"path": str(work / "AUTHORITY.md")}, work.resolve())

        self.assertEqual(prepare(entry(*matching))["parsed"]["write_prefixes"], ["Drafts/research/"])
        for label, flags in (("no create-only flag", matching[:-1]), ("a wider read folder", ["--read-prefix", "Sources/", "--read-prefix", "Estimate/", *matching[2:]]), ("no write folder", ["--read-prefix", "Sources/", "--no-overwrite"])):
            with self.subTest(label), self.assertRaisesRegex(ValueError, "limits differ|create_only|read-only"):
                prepare(entry(*flags))
        with self.assertRaisesRegex(ValueError, "program|Python|supplied"):
            prepare({"mcpServers": {"vault": {"type": "stdio", "command": "/bin/sh", "args": [str(script), "--root", str(work / "vault"), *matching]}}})
        with self.assertRaisesRegex(ValueError, "exactly one server"):
            prepare({"mcpServers": {}})
        script.write_text("# edited\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "differs from the course"):
            prepare(entry(*matching))


if __name__ == "__main__":
    unittest.main()
