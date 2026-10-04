# Module 08 — Control hallucinations

**Serves oracle:** S04, S14, S17, S19, S25  
**Primary objective:** PO-08 — Control hallucinations  
**Prerequisites:** Source verification, atomic typed questions, exact checks kept in code beside decision-model judgments, bounded agent handoffs, and bounded model-and-tool operation; preflighted environment and this module's supplied claims, source packets, and controls  
**Consumes:** VERIFY:PREFLIGHT; VERIFY:CASE; VERIFY:CLAIMS  
**Produces:** FROZEN_CLAIMS; BEFORE_REVIEWS; CORRECTION; AFTER_REVIEWS; REPORT; HUMAN_DISPOSITION; PO08_RESULT  
**Rough time:** a little over 2 hours (design budget, unmeasured)  
**Performance stage:** Adversarial  
**Work surface:** Supplied structured claim checks and a fixed, human-started, read-only review ensemble  
**Practical work:** Apply exact checks to seven registered claims on three source packets; obtain blind source and skeptical reviews; have a fresh agent correct only the registered claims against the original evidence; re-review the entire correction in fresh sessions; resolve disagreements and regressions by evidence, retaining unknown authority.  
**Performance evidence:** FROZEN_CLAIMS binds the original claims, sources, controls, and initial checks; BEFORE_REVIEWS preserves two isolated typed reviews and their actual receipts; CORRECTION preserves the full revised set and its receipt; AFTER_REVIEWS preserves two fresh full-set reviews and receipts; REPORT exposes every before/after finding, deterministic check, disagreement, and regression; HUMAN_DISPOSITION records per-claim USE, KEEP_UNKNOWN, or HOLD with reasons and an overall internal-summary decision; PO08_RESULT states the observed outcome and unresolved limits.  
**Failure / HOLD:** Incomplete or malformed coverage; invented or wrong-case citations; changed inputs or controls; missing source-read or execution evidence; reviewer exposure to other verdicts; a correction that fails an exact check or damages a supported claim; unresolved material disagreement; or model agreement treated as release authority. Preserve the failed attempt.  
**Scope boundary:** Five distinct sessions of the same pinned model are not independent model families. This case establishes neither calibrated confidence nor a general hallucination rate. Technical completion, source support, and human permission remain separate. Operational dispatch stays HOLD.  
**Handoff:** Preserve the original failure, five audited runs, complete before/after findings, individual human decision, and the evidence and owner needed to resolve each remaining gap.  
**Case family:** [CASE_FAMILY.md](../../CASE_FAMILY.md). The independent Slope Brief case uses Ridge Depot, Clinic T-8, and vehicle SB-4. No earlier module's product is required.

## Capability delta

Before this project, the learner could verify a source, obtain typed judgments, keep exact checks in code beside a decision model's judgments, supervise a bounded agent team, and have an agent produce a structured-data artifact. After this project, the learner can control the admission of model-generated claims through a source-bound review-and-correction loop, including failures introduced or endorsed by its reviewers. Giving each claim an exact check, a support judgment, or a held authority applies the Module 06 split as a quality bar; it is not a new objective.

## Enabling objectives

1. Direct blind review and source-constrained correction without allowing reviewer consensus to override evidence or lose claim coverage.
2. Adjudicate reviewer disagreements and correction regressions against the original sources, accepting a bounded summary with explicit unknowns or retaining the hold.

## Check the work

Inspect all seven claims, including the initially supported controls. Verify that each before reviewer received only the original claims and sources, and each after reviewer received only the corrected claims and original sources. Require separate audited executions, complete claim identities, real per-case locators, and exact quotations. A genuine quotation still needs a human judgment about whether it supports the asserted conclusion.

Inspect every deterministic contradiction even when both reviewers approve it. Confirm that correction did not invent, omit, or change the identity of a claim, and that a missing fact is not converted into a positive assertion. The report distinguishes technical completion from content holds. An explicit unknown can remain in an accepted internal source summary; it cannot authorize dispatch. Record that result and its limits in PO08_RESULT. No classmate or instructor grades the work.

## Supplied-case boundary

Three unchanged source packets, PC-01 through PC-03, support an authored seven-claim draft with an invented mass, two time/zone defects, a misleading shipment citation, two supported controls, and absent dispatch authority. Jev's state-plus-typed-question pattern informs the checks; the actual five live turns use the pinned course model through the existing launcher. The learner operates supplied controls, not a new agent runtime. Autonomous collaboration and multi-agent writes remain advanced. Prior paired-comparison evidence is historical only.
