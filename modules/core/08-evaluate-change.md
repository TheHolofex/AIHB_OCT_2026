# Module 08 — Evaluate a change with variation controls

**Serves oracle:** S04, S14, S17, S19, S25  
**Primary objective:** PO-08 — Evaluate a change with variation controls  
**Prerequisites:** Preflighted accessible environment, this module's supplied baseline configuration, and supplied candidate briefs on frozen paired cases  
**Consumes:** VERIFY:PREFLIGHT; VERIFY:CASE; VERIFY:BASELINE_CONFIG; VERIFY:CANDIDATE  
**Produces:** PRE_RESULT_POLICY; CHANGE_DECISION; COST_PROXY; RESTORED_BASELINE; PO08_RESULT  
**Rough time:** a little over 2 hours  
**Performance stage:** Adversarial  
**Work surface:** Frozen paired cases  
**Practical work:** Confirm the supplied baseline configuration and candidates, declare the variation rule and hard gates before any result, compare the candidates against the preserved baselines on 40 frozen paired cases using per-cell authoritative locator gates, make a narrow decision, and restore the baseline copies from stored hashes.  
**Performance evidence:** Independent protected PRE_RESULT_POLICY, 120-row evaluation with validated hashes, raw output pairs and receipts, hard-gate dispositions on the designated misses only, COST_PROXY, bounded CHANGE_DECISION, and RESTORED_BASELINE control result.  
**Failure / HOLD:** Hold for rule changes made after results, a single unqualified stochastic sample, incomparable authority or opportunity, an opened case reused as confirmation, missing raw evidence, or unproved rollback.  
**Scope boundary:** Supports a decision only for the named behavior, cases, repetition rule, environment, and served configuration; it does not establish general model superiority or authorize implementation.  
**Handoff:** Give the next owner the frozen criteria, the paired evidence, the decision and its exact boundary, the rollback trigger, and the restored home state.
**Case family:** [CASE_FAMILY.md](../../CASE_FAMILY.md). The adapter supplies a self-contained case in that family. This module’s gate does not consume another module’s product.

## Why
A new model or method cannot be separated from ordinary run-to-run variation by comparing one convenient output. How repetition, aggregation, hard gates, or exclusion will be handled has to be settled before anyone sees a result, or the goalposts move by themselves.

## Enabling objectives
1. Freeze the behavior claim, eligible cases, hard gates, cost proxy, and adoption or rollback rule.
2. Declare before results a deterministic case set, an any-single-violation gate, and an aggregation rule that does not average.
3. Make a bounded decision and prove the baseline can be restored from its frozen hash record.

## Check the work
Inspect the pre-result variation rule and the 120-row evaluation, accounting for every pair without averaging away hard-gate violations. Compare designated misses with the observed case results and retain raw pairs and receipts. Keep CHANGE_DECISION no broader than that evidence, and exercise RESTORED_BASELINE with candidate influence removed. Record the comparison and restore observation in PO08_RESULT. An opened case that informed a repair becomes diagnostic and cannot serve as confirmation.

## Supplied-case domain (adapter)
Baseline vs two candidates on 40 paired Ridge Depot cases. Authoritative locators in sources.json. Hard gates: mass must be the exact number from the authoritative #payload record with that locator in the Source cell; gate times must carry both the UTC label from the source and the MDT label from the source with the authoritative #gate locator. Restore baseline using the distinct hashed copies. Class-only. No real movement.
