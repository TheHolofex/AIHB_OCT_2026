# Module 7 facilitator runbook

## What the harness changes

The supplied evaluate_pairs and restore now operate on the 40 paired cases with per-cell authoritative locators and hashed baseline restore instead of the two-pair historical thin lab.

## Session result
The learner freezes the policy, confirms all baselines pass, records the six designated one-violation failures on the two candidates (three each), runs the 120-row evaluator, and restores work copies that pass. The learner does not average.

## Before class
1. Confirm the policy file names hard gate and any single violation.
2. Run hard_gates.py on a few baselines (exit 0) and the six designated failing briefs (exit 1 with the expected reason).
3. Run evaluate_pairs.py on the case directory and confirm 120 rows with the six designated failures only.
4. Run restore_baseline.py on a test work copy and confirm baselines pass again.
5. Confirm the case pairs and the evaluator script are ready for the technical checks.

The checked live instruction keeps the two clock values separate: UTC in `Gate time in source`, MDT in `Gate time for desk`. An older instruction ambiguously asked both cells to include both labels. Preserve that version and its results if a batch has started; do not replace a frozen instruction or repair its briefs. The clarified instruction needs a fresh preregistered comparison. A rejection of the old wording is not evidence that the revision passes or improves outcomes.

## Coaching boundary
You may point to a file or help run a supplied command. You may not supply the defect names, rewrite the policy after results, average the pairs, or tell the learner which rows to mark failed. If you cross that line, mark the work as guided practice.

## `HOLD` conditions
Use `HOLD` when the policy changes after results, a baseline fails, a non-designated candidate passes its gate, the evaluator does not produce 120 rows or the hashes do not match, restore fails or does not restore a passing baseline, or the learner handoff requires coaching to be understood.

## Staff-only local campaign stop

The learner command still requires the provider-side US$40 per-key ceiling. An
explicitly authorized staff campaign may keep its existing provider limit and
instead supply both local-stop flags:

```bash
"$PY" "$M/scripts/stretch_runner.py" "$W" "$E/live-comparison" \
  --local-budget-usd "$REMAINING_USD" --usage-baseline-usd "$Upre"
```

Immediately before launch, obtain `Upre = usage + byok_usage` from the authenticated
OpenRouter `GET /api/v1/key` response. `REMAINING_USD` is the campaign's remaining
allowance, greater than zero and no more than US$40. Subtract the maximum of the
campaign's cumulative key-usage delta, known SDK estimate subtotal, and previous
admission high-water charge from its approved allowance. Do not round upward,
reset the campaign baseline, or exclude failed calls. Keep all other paid
processes stopped while the comparison runs. Pass the API key through the
environment, never through command arguments or evidence files.

The runner queries key usage before and after each attempted launcher call,
including the two restored controls. It admits a call only while the maximum of
usage since the supplied baseline and known SDK estimates remains below the
remaining allowance. Missing estimates stay explicitly incomplete; invalid or
decreasing metadata stops further admissions. A failed child retains its output,
exit status, receipts, and post-call accounting without a retry.

This is a soft stop, not a hard spending cap. One in-flight turn can make several
provider requests; delayed accounting or other activity on the key can cause an
overshoot. The final observation can leave a complete 38-attempt comparison
`COMPLETE` with a recorded overshoot, but no more paid work may be admitted.
Inspect `comparison.json.local_budget` and the campaign ledger before any later
paid operation. Aggregate key usage is not exact per-generation billing.

Local mode records a null provider-ceiling prerequisite and leaves
`provider_ceiling_verified_by_adapter` false. It does not change the provider
limit, establish available account credit, or waive learner prerequisites.
