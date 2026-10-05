# Module 06 — Design a workflow for a decision model

**Serves oracle:** S04, S12, S14, S17, S19
**Primary objective:** PO-06 — Design a workflow for a decision model
**Prerequisites:** Bounded direction, source verification, and typed questions with labels frozen before a run; a preflighted accessible environment, the course launcher on the latest stable OMP release with its judge profile, and this module's supplied case and controls
**Consumes:** VERIFY:PREFLIGHT; VERIFY:CASE; VERIFY:JUDGE_ROUTE; VERIFY:DESK_LABELS
**Produces:** JUDGE_SELECTION; DECISION_QUESTIONS; RISK_THRESHOLDS; HELD_OUT_MEASURE; PO06_RESULT
**Rough time:** about 3 hours
**Performance stage:** Adversarial
**Work surface:** Decision-model screen for AI-drafted notes
**Practical work:** List the judge models the course key reaches and record a selection; pin `openrouter/typesafe/jev-1.13` as OMP's judge role; repair a starter question set against the router contract and the model's documented weak spots; run twenty tuning notes through the launcher's judge profile; record first misses before revising; set four thresholds from the tuning answers; freeze questions, thresholds, served build, and review ceiling; judge sixty held-out notes once; measure and hand off.
**Performance evidence:** Saved judge candidate list and selection record; two-line judge setting; question set passing the router check; every tuning run with launcher receipts, served build, and cost; first-miss notes covering every note the first run missed; frozen thresholds and review ceiling recorded before the held-out run; held-out measurement with error counts, review share, served build, and cost per 1,000 notes; handoff; the verifier's joined result.
**Failure / HOLD:** Hold when the pinned judge is unavailable or another selector is set; a judgment is missing, malformed, or from another build; the questions changed after the tuning run a freeze names; the held-out run started before the freeze; a saved judgment or measurement is edited; or the held-out measurement shows a missed overstatement, an unreviewed instruction, an unreviewed note about another cylinder, a changed build, or a review share above the frozen ceiling.
**Scope boundary:** Proves one frozen screen on sixty practice notes judged by one served build. It does not establish the model's accuracy beyond the sample, calibrate its probabilities in general, authorize a release or a load, or require programming: the learner writes questions, thresholds, and records in supplied formats, and the launcher, guard, runner, and router are supplied.
**Handoff:** Give the duty officer the frozen questions and thresholds, the held-out errors and review share, the served build and cost, the limits, and the owners of the review queue and every release.
**Case family:** [CASE_FAMILY.md](../../CASE_FAMILY.md). The adapter supplies a self-contained case in that family. This module's gate does not consume another module's product.

## Capability added

Before this project, the learner can shape an AI judgment as typed questions, freeze labels before a run, and route the chat model's answers in code with gates set from measurement. After it, the learner can select, pin, and operate a dedicated decision model in their own harness, design the question set and code split around that model's documented weak spots, set thresholds from its probabilities by the cost of each error, and prove the frozen screen on held-out data with the served build and cost on record. Typed questions and frozen labels are prerequisites, not new objectives.

## Enabling objectives

1. Select and pin a decision model as the harness judge from the candidates a key reaches, and state the decision point, the data boundary, and the weak spots the design must answer.
2. Design questions and a code split for that model class: rules settled in code, minimal state, one condition per question, explicit ways out, and option order checked by asking twice.
3. Set thresholds from tuning answers by error cost, freeze them with a review ceiling, and measure the frozen screen once on held-out notes.

## Check the work

Recheck every judge run with the shared auditor: one frozen cell, every answer shaped by the frozen questions, one served `jev-1.13` build, a finished batch with cost, and no work-folder change beyond the declared output. Confirm the first-miss notes name every note the first tuning run missed, and that a revised run followed. Confirm the freeze names a tuning run with the current questions and predates the held-out run, measure the saved held-out answers again, and compare with the saved measurement. Read the selection record and handoff. Record the result in PO06_RESULT.

## Supplied-case domain (adapter)

Blue Gauge screens AI-drafted handoff notes for oxygen cylinders moving from East Yard to Clinic O-2 against the yard's scan record. Eighty notes `BG-001`–`BG-080`: twenty tuning notes with visible desk labels and sixty held-out notes whose labels the learner opens only through the measurement after the freeze. The state sent to the model is the note text alone; the cylinder ID, cited order, and scan rank stay in code. Traps include release claims without the word released, negated and conditional releases, cautions that keep a control in place, embedded instructions, a cited order the scan record lacks, other-cylinder notes, and a vendor tag that reads like a release.
