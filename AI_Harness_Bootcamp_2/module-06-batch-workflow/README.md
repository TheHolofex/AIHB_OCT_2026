# Module 6 · Operate a fixed workflow through change

Build a local visual n8n workflow for White Rack's fictional refrigerated reagent kits from Icehouse Depot to Clinic I-6. Predict the effect of one saved policy change across two batches of 80 lots. Compare all changed and unchanged receipt rows, then restore the preserved workflow into a new blank canvas and reproduce both original files exactly.

Plan for 3 facilitated hours on Wednesday, including 2 hours of practice. This is a planning allowance, not a measured completion guarantee.

## Before you begin

Complete [local n8n readiness](../module-00-setup/README.md): n8n 2.41.5 on the approved full official local stack, with the editor available on localhost. Use your established source inspection, frozen prediction, bounded-control validation, and evidence-preservation habits. Have a plain text editor and a browser download folder you can locate. Keep Assistant off and workflows unpublished. This work uses test forms without model calls or provider credentials.

[Build, run, compare, and restore the workflow](shared/MODULE_06_LAB.md). Start from a blank router canvas. Download the two input waves, supplied validator, and separate receipt checker from that lab. Save predictions before any routing execution.

## The saved change

The router checks exact, case-sensitive values. `RACK_CONFLICT` wins first and produces `hold,RESOURCE_CONFLICT`. Otherwise, `AUTHORIZED` produces `pass,READY`. Exact `PENDING` uses the saved `pending_status` value: `OPEN` produces `hold,OPEN`; `NOT_AUTHORIZED` produces `reject,NOT_AUTHORIZED`. Other permit strings, including `WITHDRAWN`, fall back to `hold,OPEN`. Gate-window text and input disposition do not choose a route. A pending decision is not a quality release.

Change only Pending rule's String value from `OPEN` to `NOT_AUTHORIZED`. Keep every other node setting, wire, and input fixed. Preserve the original JSON export and its separately downloaded original SHA256 report before editing. Retain the changed export separately.

Importing JSON adds nodes to the open n8n canvas. Import the checker into its own new blank workflow. Later, recheck the original export against its retained digest and import it into another new blank workflow for restoration. Do not restore by manually reversing the policy value.

## Retain the evidence

Keep the frozen per-wave delta CSVs, baseline and changed exports, original and rechecked identity reports, six receipts, the baseline exact comparison, two predicted-change reports, and two restored exact reports. Record workflow identities and execution IDs. A successful execution is not a comparison result: read the checker's `PASS` or `HOLD` report and its complete row counts. Preserve every held attempt and never hand-edit a receipt.

The optional revised-wave practice compares input changes with policy fixed, then policy changes with the revised input fixed. Each comparison needs its own frozen prediction and downloaded report.

## Class-only boundary

All lots, permits, windows, and notes are fictional practice data. Do not use this packet to plan, authorize, dispatch, or describe a real movement. A module result permits only class review.
