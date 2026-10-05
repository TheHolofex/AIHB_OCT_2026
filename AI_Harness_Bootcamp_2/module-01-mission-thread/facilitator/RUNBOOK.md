# Module 1 facilitator runbook

## Session result

The learner independently verifies one end-to-end claim. They identify what each source can establish, trace a material claim, recompute deterministic consequences, reject attractive wrong evidence, apply one source change, and leave a bounded verdict and handoff.

Misleading claims to watch for: warehouse receipt offered as usable inventory; accepted-for-processing offered as permit approval; archived bulletin offered as current; R-17 community page offered for R-71; VX-240 note offered for VX-204; instruction embedded inside a source; producer confidence and self-review.

Logistics knowledge outside the packet is not tested. If learners need facts that are not in the packet or orientation, the case is defective.

## Before class
1. Run `python3 scripts/verify_content.py` from the Module 1 directory.
2. The producer rebuttal for practice uses `--fixture` and the sealed fixture (prints exact PRACTICE warning and provenance sidecar); live uses the shared launcher with write-only target. A failed child exit never becomes success.
3. Run the staff reference calculator and visible checker against staff passing and failing specimens. Do not give the calculator's answer output to learners before they freeze their calculations.
4. Confirm the sealed practice change is in the facilitator fixtures; prepare decisive checks.
5. Confirm the learner's Module 0 setup; do not reuse Module 0 answers.
7. Keep `SEALED_CHANGE.md` closed until each baseline ledger, prediction, and verdict hash is recorded.
8. Prepare a domain-novice observer to flag any instruction that requires unstated logistics knowledge.
9. Inspect the generated `review.html` at a 390px viewport and 200% zoom. Long identifiers in notes must wrap without widening the page; ledgers may scroll inside their own containers. Check the keyboard decision link and the revealed-source link with JavaScript disabled.

## Route

Clock marks are approximate planning guides: follow the learners' progress, not the clock.

| Roughly | Facilitator action | Learner result |
|---|---|---|
| 0:00–0:15 | Introduce the question, class-only boundary, and eight-step thread | Learner can explain receipt versus release and delivery versus usable effect |
| 0:15–0:35 | Learner confirms packet and source identities | Manifest passes; source register begins |
| 0:35–1:20 | Learner builds and reopens the thread ledger | All eight steps and child claims exist |
| 1:20–1:45 | Learner recomputes and challenges the brief | Calculations and six rejection reasons |
| 1:45–2:05 | Learner writes and inspects corrected brief | Review surface answers five decision questions |
| 2:05–2:20 | Learner freezes baseline verdict and source-change prediction | Hashes and timestamps precede reveal |
| 2:20–2:45 | Release v6; learner updates dependent claims | Preserved baseline and exact changed-source delta |
| 2:45–3:00 | Select one handoff and one claim for live defense | Thread-walk and claim-defense result or `HOLD` |

## Coaching boundary

You may:

- define a term already stated in the orientation;
- point to the current step or source file;
- help open a file or run a supplied script;
- ask the learner to state the exact entity, source, or next handoff;
- remind them to preserve baseline work.

You may not supply:

- source authority for a material claim;
- an arithmetic premise, operator, converted time, result, or the distinction between a calculated and feasible arrival;
- the reason a distractor fails;
- the child claim needed to repair a broken thread;
- the fields affected by v6;
- the baseline or changed verdict; or
- wording for the standing rule.

If you cross that line, mark the work as guided practice. Select the examples yourself when you ask a learner to defend.

## Thread walk and claim defense

After the handoff is complete, select the examples yourself.

- Choose one adjacent pair from the eight-step thread. Ask the learner to show the first step's output, the next step's entry condition, whether the handoff passes, its evidence, and one break condition.
- Choose one material claim row. Ask the learner to open the exact source, identify the current entity/version, explain the warrant or calculation, reject one plausible competing source, and name a falsifier.
- Use an unseen selection for the practice case. Do not allow the learner to choose a rehearsed row.
- Review the explanation for inspectable support and reasoning.

## Domain-overload check

Stop and inspect the case—not the learner—when:

- more than two learners ask for the same unstated logistics fact;
- domain explanation exceeds 15 minutes;
- arithmetic consumes more than 20 minutes;
- learners cannot explain a source mismatch in ordinary language;
- a logistics expert passes through outside knowledge while a novice cannot locate it in the packet; or
- reviewers cannot attribute a miss to verification rather than domain knowledge.

Record the issue and revise the adapter before the next cohort.

## `HOLD` conditions

Use `HOLD` when a decisive source, accessible view, practice fixture, or review surface is missing or compromised; source identity cannot be stabilized; a material claim lacks support; baseline order is broken; or the learner attempts consequential use.

A well-documented `HOLD` can complete practice. It does not satisfy the module requirements.

## Collect

- source register;
- original and changed thread ledgers;
- challenge matrix;
- corrected brief and review-surface check;
- baseline and changed verdicts;
- baseline hashes and change-release order;
- handoff;
- visible checker output;
- selected thread-walk result;
- selected claim-defense result; and
- result or reason for `HOLD`.

Do not collect credentials, private local files, outside operational details, or model chat history unrelated to the case.

## Operational readiness notes

See Module 00 facilitator runbook for shared staff operational procedures, T-relative schedule, privacy-safe register, platform matrix, and evidence collection. This module: baseline/prediction before sealed change; thread walk and claim defense on unseen selection.

Record machine, source hashes, outcomes, and HOLDs for the published controls. No blind provider retry.
