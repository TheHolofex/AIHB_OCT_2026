# Module 8 facilitator runbook

The learner runs five sessions on the Slope Brief. The brief says the shipment is released. The sources do not. PC-01 has a real quote for a different shipment, so two reviewers can agree and still be wrong. The learner decides from the sources. Dispatch stays HOLD.

## Capability and prerequisites

The new capability is operating an evidence-bound review-and-correction loop, including mistakes introduced or endorsed by its reviewers. Source verification, typed questions, the split between exact checks, model judgments, and decisions reserved for a person, bounded agent handoffs, and bounded model-and-tool operation are inherited skills; giving each claim its exact check, support judgment, or held authority applies that split. Repair a missing prerequisite explicitly; do not count it as new mastery here.

The independent case has three source packets and seven authored claims. Five audited child calls use the same pinned model: before-source, before-skeptic, correct, after-source, after-skeptic. Fresh sessions prevent answer sharing, not correlated model errors. Jev supplies the state-plus-typed-question design reference, not a new account or runtime dependency. Learners drive every step by copying natural-language prompts into the ordinary OMP conversation (the coordinator). The coordinator executes the helper and shows evidence; the five audited children are the isolated runs launched for the recorded tests.

## Before class

Follow the actual learner procedure from the published lab (copying the In Oh My Pi prompts) in a fresh external work folder. Use Python 3.12+, the verified latest stable OMP release, and `openrouter/anthropic/claude-sonnet-4.6` through the shared launcher. Retain the actual OMP version in each run's evidence. Do not replace a missing model or credential with a fixture.

Rehearse the sequence the prompts will cause:

1. Copy the prepare/resume prompt; confirm the helper creates W (with case and controls) and names a separate unused E. No audited child/provider-test call yet. Verify credential availability check without secrets printed and link back to Module 00 on missing setup.
2. Copy the read-the-claims prompt; confirm W/notes.md receives only the learner's confirmed observations: one claim to use, one to stop, and which PC-01 record belongs to SB-4. No child launched.
3. Copy the freeze prompt; run the helper's freeze --work W --out E (or observe the coordinator doing it). Check the frozen sources and controls, manifest, and initial findings exist. `PASS: frozen 7 claims` describes preservation and checking, not a correct original draft.
4. Copy the first-review prompts; observe the coordinator launch before-source and before-skeptic as two separate child calls. Parsed answers belong in `reviews/`; actual execution receipts belong in `runs/`. Inspect actual source-read proof, blind input identities, and distinct run IDs. Confirm neither child received W/notes.md, initial checks, or the other review.
5. Copy the compare prompt; confirm learner notes are appended and both review files remain untouched.
6. Copy the correct prompt; observe the coordinator invoke correct --attempt E exactly once. Check every original/corrected claim and the two supported controls.
7. Copy the after-review prompts; observe two new child calls (after-source, after-skeptic) with the corrected claims and original sources only. Five distinct audited executions are required for technical completion.
8. Copy the report prompt; if the report files exist, the prompt must cause inspection rather than overwrite. Confirm the report distinguishes technical_complete from content_holds. The generated human-decision.json is a template only.
9. Copy the human-disposition prompt; observe the coordinator interview the learner for each C01–C07 disposition (USE / KEEP_UNKNOWN / HOLD + reason), show proposed entries for confirmation, and fill only the existing human-decision.json schema with operational_dispatch remaining HOLD. Do not let it edit report, provider results, or receipts.
10. Confirm that an existing output is refused rather than overwritten. The no-key path must stop before creating a model attempt. Preserve failed runs and use a new attempt after repairing a prerequisite.

Check the published Overview and Lab routes for the prompt contract (In Oh My Pi / Expected / Stop / Recovery sections), the resume prompt near the top, and explicit coordinator vs. child language. Any observed verification applies only to the exercised host, model, and case; representative learner timing remains unmeasured.

Only explicit live execution calls the provider. The five audited child calls are the core sequence, not a price cap. Use the approved account budget and preserve failures; do not add retries, model fallback, or an autonomous campaign.

## Thursday pacing

The first Thursday block has a little over two hours. This approximately 130-minute allocation is a design budget, not a measured learner time. Follow progress and retain unfinished work honestly.

| Minutes | Work and observation |
|---|---|
| 0–15 | Learners copy the read-the-claims prompt. They read the claims and packets in W, name one claim to use and one to stop, and say which PC-01 record belongs to SB-4. Confirm W/notes.md contains only their confirmed observations. |
| 15–30 | Learners copy the freeze prompt. The coordinator runs freeze; compare exact findings with the initial human reading. |
| 30–55 | Learners copy the two first-review prompts. The coordinator launches two isolated child calls. Compare every verdict, source, quotation, and reason from the returned before reviews. Record disagreements and mistakes before correction. Verify blind inputs and separate run folders. |
| 55–75 | Learners copy the correct prompt. The coordinator invokes correct once. Inspect complete claim coverage and explicit unknowns. |
| 75–95 | Learners copy the two after-review prompts. The coordinator launches two fresh child calls on the corrected claims and original sources, without prior verdicts. Inspect unchanged controls as well as repaired claims. Confirm no leakage of earlier verdicts. |
| 95–120 | Learners copy the report prompt (or inspect if already present). The report audits all five child runs. Resolve disagreements by source evidence or retain a hold. Learners copy the human-disposition prompt; the coordinator interviews and writes only after confirmation. Complete each human disposition and the overall internal-summary decision. |
| 120–130 | Preserve the original failure, all five child receipts, complete findings, notes, decision, and the missing evidence and responsible owner. State why dispatch remains on hold. |

Do not move required work into homework or describe an unexecuted lane as completed. If a provider or environment prerequisite blocks execution, retain the unaffected source-check evidence and name the live lane as unobserved. That is an honest operating limit, not learner failure.

## Coaching

Help learners identify the active folder, read a field, or interpret an error. When a source settles a disagreement, have the learner name the exact record and explain the relationship to the claim. Teach the distinction between a contradicted assertion and an unestablished one. A missing authorization does not establish a denial.

Watch that the coordinator never sends conversation, notes, or earlier verdicts into a child; each child must receive only its prescribed frozen inputs. Confirm the learner, not the coordinator, supplies the final dispositions after inspecting evidence.

Do not overwrite model findings, hide the first failed attempt, or present a facilitator's explanation as a model execution. No classmate or instructor grades the work, and no peer sign-off is required. The handoff must be inspectable in itself.

## Work decisions and failure handling

- A malformed review or correction stops the affected stage. Retain the raw response and receipts.
- A well-formed but wrong correction is re-reviewed and exposed in the report. Do not retry it until it looks favorable.
- Reviewer disagreement remains visible. Agreement cannot defeat an exact source check.
- A real quote can still be irrelevant or insufficient. The person judges its relationship to the claim.
- A supported claim changed unnecessarily is a regression to inspect, even when the other defects were repaired.
- `technical_complete` means the report audited all five child runs. `content_holds` separately records unresolved exact failures, reviewer conflicts, and regressions.
- A withdrawn unsupported assertion represented by `null` can remain in a usable internal summary. Its authority remains unknown; operational dispatch stays `HOLD`.

The human template uses per-claim `USE`, `KEEP_UNKNOWN`, or `HOLD`, with a source-backed `reason`. `internal_summary_decision` and `unresolved_evidence_and_owner` record the overall boundary. The tool does not automatically verify those human judgments.

## Evidence limits

Authored defects are exercise inputs, not observed hallucinations from the provider. Model-produced reviews and correction are live observations only when their receipts pass the audit. One five-audited-child-call sequence establishes no general hallucination rate, calibration, or model superiority. Previous paired-comparison and restore evidence belongs to the retired module revision and does not verify this workflow.

## Operational readiness notes

See Module 00 facilitator runbook for shared staff operational procedures, T-relative schedule, privacy-safe register, platform matrix, and evidence collection. This module: five audited child calls; human decision on holds.

Record machine, source hashes, outcomes, and HOLDs for the published controls. No blind provider retry.
