# Reference: Module 5 — Orchestrate an OMP agent team

Staff-only contract and verification record. Revision: 2026-10-04, native orchestration cutover. The publication keeps the existing module directory/URLs, but retires the renderer-fault exercise.

## Capability and authority

Before Copper Span, the learner can direct and verify one bounded assistant run. After it, the learner can supervise a dependency-aware native OMP team: assign independent work, accept attributable handoffs, gate dependent integration/review, and recover only invalidated work without erasing valid evidence.

Source verification, typed answers and basic tool boundaries are prerequisites. A graph, log or installed tool is evidence, not the objective. Course authority is `modules/core/05-diagnose-recover.md`, `LEARNING_OBJECTIVES.md`, `AUTHORING_GUIDE.md`, `MISSION_THREAD_SCENARIOS.md` and the pinned native sources below.

## 2026-10-04 amendment — no graded cases

The owner's direction is that no classmate or instructor grades a learner's work. There are no protected grading cases, learner scores, qualification decisions or exercise-grading instructions. Technical checks and work decisions may return PASS/HOLD. The orchestration rewrite preserves that direction from the concurrent staff amendment; the obsolete renderer/protected-case instructions are not retained as current practice.

## Supplied case and controlling answer

All records are fictional. CS-2 carries IV fluid cases from Basin Depot to Clinic F-9. Decision time is `2026-10-16T12:15:00-06:00`.

- `INV-CS2`, revision 2 superseding 1: 72 scanned, 68 usable, 4 quarantined.
- `REL-CS2`, revision 2 superseding 1: HOLD; QC inspection remains open. The superseded RELEASED record has a later archive receipt timestamp. Explicit authority/revision/supersession, not receipt order or agent agreement, determines the current fact.
- `TIME-CS2`, revision 2 superseding 1: not before `2026-10-16T18:00:00-06:00`.
- Correct candidate: decision HOLD, reasons AUTHORITY_HOLD and TIMING_NOT_OPEN, with the three original producing attempt/child identities and source identities/hashes.

The learner writes an ownership/dependency plan and revises Inventory's target/acceptance before dispatch. Timing initially names the genuinely absent `shared/case/timing-pending.json`. Repair changes that Input line to `shared/case/timing.json`, not the evidence or the other briefs. Learners do not implement a scheduler or write executable exercise code.

## Runtime contract

`shared/prepare_work.py 05 W` copies the case, roles, briefs, guard and both Python controls into a new external work root. `scripts/orchestrate.py` exposes only `inspect`, `run` and `check`.

- **Inspect:** offline graph, assignments, required version/model and fingerprints. Not proof of installation, credentials or execution.
- **Fanout:** one native `task` call with Inventory, Authority and Timing. Three read-only child sessions. The first expected technical result is HOLD/exit 1, with two accepted and Timing blocked after a real ENOENT read.
- **Repair:** verified `--prior` required; only blocked or fingerprint-invalid specialists are dispatched. Reused reports retain their original attempt_id and child_id. Expected PASS/exit 0 with only Timing dispatched.
- **Integrate:** accepted, current specialist evidence required. The coordinator reads accepted-handoffs and all three sources before one write to `out/status-brief.json`. No child. Expected PASS/exit 0; candidate snapshot retained.
- **Review:** accepted current integration required. One read-only Review child reads the actual candidate, accepted handoffs and sources. Its native payload is accepted/hold with candidate_sha256 and issues. Expected CLI PASS/exit 0 only when its recorded work is accepted.
- **Human use decision:** separate note outside sealed evidence, identifying candidate, checked evidence, use/revise/hold decision and remaining owner. No real movement authorization.

Each stage creates exactly its new evidence directory; existing destinations are refused. Run preflight failures return HOLD on stderr and exit 2 before provider dispatch. Runtime failures, incomplete records and failed acceptance remain held. `check` makes no provider call and returns exit 1 for invalid or stale evidence. A malformed chain may yield only status/issues, rather than a reconstructed stage summary.

The pin is OMP 18.3.5 and `openrouter/anthropic/claude-sonnet-4.6`. Native `task` owns child execution; there is no alternate provider client or Python child scheduler. The isolated runtime has a fresh HOME/cwd, explicit requested roles, no personal profile, disabled runtime retry/model fallback, synchronous result collection, concurrency 3, recursion depth 1, 12 provider requests per session and a 300-second run deadline with shutdown allowance.

The re-bound extension validates actual `ctx.agent` identity, exact task/spawn contracts, model/role/control identity, assigned read attempts and terminal yield. Child initial/active tools are course_read/yield. course_write is registered only for coordinator-only integration. Exact input bindings do not grant directory-wide access. Missing input produces a real filesystem error; no synthetic blocked receipt is inserted.

Evidence includes policy/config, frozen inputs and controls, guard events, native parent/child sessions and structured artifacts, stdout.jsonl, stderr.txt, process.json, before/after work snapshots, derived reports/result and seal.json. Dependent stages retain accepted-handoffs.json and candidate.json. Integration preserves an existing candidate before an authorized replacement. The validator joins native calls/results to independently recorded read/write effects, source truth, producing identity and current fingerprints; a parent summary alone cannot pass.

Changed specialist inputs invalidate their consumers. Changed integration instructions invalidate integration and review; changed reviewer instructions/role invalidate review without discarding unchanged specialists. Prior seals and exact locations remain part of the local evidence chain. Files and hashes are ordinary audit records, not tamper-proof attestation; tool policies are not an OS sandbox.

## Measured native proof — Apple Silicon macOS, 2026-10-04

Retained private evidence: `~/course-evidence/copper-span-native-20261004/`, with work, fanout, repair, integrate and review siblings. Provider credential was passed privately in the process environment, not published. Inventory's target and acceptance were rewritten before this fanout.

The separately downloaded official darwin-arm64 18.3.5 binary reported `omp/18.3.5`; its official checksum matched `3ad34e91a474ea239674b593a5ff1544727a22f7afd3c8a8729260128a5febd1`. A newer global binary was not substituted.

| Stage | Producing run ID | Observed run/check result |
|---|---|---|
| Fanout | `6a9d81d0-2760-4016-9739-c71542ed2b69` | HOLD/1; Inventory and Authority accepted; Timing blocked on the exact absent input. |
| Repair | `74b2de92-7d80-49cb-bea7-59e9ec45c8d0` | PASS/0; only Timing dispatched; Inventory/Authority retain fanout attribution. |
| Integrate | `e7df4ab6-450d-402a-bb20-a340deb17c93` | PASS/0; no child; source-backed candidate written. |
| Review | `e8b33b6c-ad67-488c-90f0-5410cbe3c247` | PASS/0; only Review dispatched; native accepted payload, no issues, matching candidate hash. |

Candidate SHA-256: `89c46ce52611ff5a63a835fbee2420763a8fcaf02d83a290870b8ef885c9ab6a`. Its facts match the controlling answer above; movement remains HOLD despite technical acceptance.

An actual check of this review returned HOLD/1 after the integration brief was changed. Restoring the original brief restored PASS/0 without altering the saved evidence. An earlier complete native run also rejected premature integration from the blocked first wave with preflight HOLD/2.

Final control identities used by this run:

| Control | SHA-256 |
|---|---|
| scripts/orchestrate.py | `48db9dd817769dab8ee49f7459a0e518e28a6a2dc827d4b707c2e46a44582771` |
| scripts/orchestration_evidence.py | `12bfaa29b5177ea0dd29ad41563781ad7e5667ea958af7b0642e002c3019a77d` |
| shared/controls/orchestration_guard.mjs | `12a0816c73b8495bde70fda73fd1c8322c74f391aad5a0c4a0fe20dbf25bb44d` |

Earlier failed attempts were kept, not rewritten: native cwd alias mismatch, returned-assignment whitespace normalization, and child initial-tool registration led to specific corrections. The final run uses canonical cwd comparison, native trim normalization and no child writer registration.

## Offline and publication proof

On the isolated feature branch before integration with concurrent main changes:

- 11 deterministic Python behavior tests and 8 Node guard boundary tests passed. Synthetic native-record fixtures are explicitly labeled and are not live proof. The new consumer-instruction regression failed before its fix and passed afterward.
- All 65 root unit tests passed.
- All 29 `scripts/check_course.py` gates passed, including module figure checks and the byte-for-byte publication check.
- Publisher output: 35 instructional pages, 713 raw downloads, 40 UI/generated assets. Counts describe that checkout, not a promise about subsequent concurrent course edits.
- All 18 lab shell blocks parsed: 9 Bash blocks in both Bash and zsh, plus 9 PowerShell blocks in the available PowerShell parser, 27 checks total. This is not native Windows PowerShell 5.1 execution evidence.
- Isolated Chromium exercised overview-to-lab and home navigation, the new home/module wording, shell switching, actual page-clipboard command bytes, full reading, narrow 390-pixel layout, Sand/Dark presentation, both loaded figures, full-size dialog and Escape, published controls/roles, and staff/obsolete-script 404 boundaries. No horizontal document overflow was observed. With JavaScript disabled, all required stages and all 18 command blocks remained available.
- Browser screenshots are retained under the private evidence root. The default shared browser's screenshots/input stalled; a separately launched Chromium instance completed the observed interaction and visual checks. That tool failure is not a passed browser lane.

## Integration with concurrent main changes

The merge retains main's spreadsheet-agent and structured hallucination-control work, along with its revised local-model scope. After integration, the 11 orchestration tests, 8 guard tests and all 65 root unit tests passed. A fresh Module 05 preparation/inspect succeeded, and the merged launcher independently accepted the retained real review. The rebuilt publication passed exact checking and figure-link validation: 35 instructional pages, 423 raw downloads and 40 UI/generated assets. Chromium confirmed the combined homepage and the orchestration overview.

Current main already records a separate Module 07 core-contract mismatch: the course map produces AGENT_SHEET while `modules/core/07-fixed-workflow.md` still names retired fixed-workflow products. `module-08-change-eval/evidence/REVIEW_VERDICT.md` records that inherited `test_core_standard.py` HOLD. This integration does not claim a green combined full-course gate or rewrite that unrelated Module 07 contract.

## Limits and historical boundary

The 90–150 minute allocation is a planning estimate, not a measured learner duration. No representative learner study, human panel, native Windows/WSL/Linux execution, Intel macOS run or screen-reader operation is claimed. Interactive Agent Hub/steering is explained from the pinned native sources; the headless smoke does not prove an interactive supervision session. Child outputs and timestamps are nondeterministic; contracts and checked identities determine acceptance.

Historical `evidence/`, `reviews/` and the repository's earlier exercise-run registry describe the retired renderer/probe/restore contract. Keep them unchanged and do not use their outcomes as orchestration proof. Current learner publication, runtime, tests and review challenge contain no compatibility path back to that exercise.

## Pinned primary sources

- [Native task arguments and execution](https://github.com/can1357/oh-my-pi/blob/v18.3.5/docs/tools/task.md)
- [Role discovery and frontmatter](https://github.com/can1357/oh-my-pi/blob/v18.3.5/docs/task-agent-discovery.md)
- [Settings](https://github.com/can1357/oh-my-pi/blob/v18.3.5/docs/settings.md)
- [Extensions and child context](https://github.com/can1357/oh-my-pi/blob/v18.3.5/docs/extensions.md)
- [Task executor and native artifacts](https://github.com/can1357/oh-my-pi/blob/v18.3.5/packages/coding-agent/src/task/executor.ts)

`REFERENCE.sha256` records this staff source. Runtime/control hashes above bind the measured native run; the prose digest is not a substitute for those records.
