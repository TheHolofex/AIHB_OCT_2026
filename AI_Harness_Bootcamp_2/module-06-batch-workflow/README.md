# Module 6 · Operate a fixed workflow through change

Apply one saved routing rule consistently to White Rack's refrigerated reagent kits from Icehouse Depot to Clinic I-6. Predict the full effect of one rule change across two batches of 80 lots, then compare every changed and unchanged output row. Restore the original rule from its separate saved copy and verify that both batches reproduce their original results.

Plan for one three-hour facilitated session, including two hours of practice. This is a planning allowance, not a measured completion guarantee.

`PENDING` is part of the routing decision. It is not a quality release. `RACK_CONFLICT` is evaluated first and produces `hold,RESOURCE_CONFLICT`.

## Start here

1. [Run and compare both batches](shared/MODULE_06_LAB.md) under the original and changed rule.

## The one-rule change

The baseline, or original rule, is `pending_status: OPEN`. AUTHORIZED lots are `pass,READY`; PENDING lots are `hold,OPEN`; every other permit state and cancelled lots are `hold,OPEN`.

With `pending_status: NOT_AUTHORIZED`, PENDING lots become `reject,NOT_AUTHORIZED`; everything else stays as baseline. Rack conflicts remain held first.

For each batch, keep the workflow and input file fixed. Only the one line in `RULE.md` changes. Compare complete serialized rows: the exact text saved in the output file, including separators and line endings. Exclude generated prose from this deterministic acceptance check, which requires the same bytes for the same inputs and rule.

## Class-only boundary

All lots, permits, windows, and notes are fictional course fixtures. Do not use this packet to plan, authorize, dispatch, or describe a real movement. A module result permits only class review.
