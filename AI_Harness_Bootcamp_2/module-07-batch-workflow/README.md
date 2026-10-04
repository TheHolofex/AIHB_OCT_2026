# Module 7 · Operate a fixed workflow through change

Build a local visual n8n workflow that routes White Rack's fictional shipment of refrigerated reagent kits from Icehouse Depot to Clinic I-6. Predict the effect of one saved policy change across two batches of 80 lots. Compare every receipt row, changed or not, then restore the saved original workflow into a new blank canvas and reproduce both original files exactly.

Plan for about three hours on Wednesday. That's a rough estimate, not a measured time.

## Before you begin

Complete [local n8n readiness](../module-00-setup/README.md): n8n 2.41.5 on the approved full official local stack, with the editor available on localhost. Bring the habits you already have: inspect sources, freeze predictions before running anything, validate with bounded controls like Blue Gauge's predicate, and keep every piece of evidence. Have a plain text editor ready, and know where your browser saves downloads. Keep Assistant off and workflows unpublished. You'll use test forms only, with no model calls or provider credentials.

[Build, run, compare, and restore the workflow](shared/MODULE_07_LAB.md). You start from a blank router canvas and download the two input waves, the supplied validator, and the separate receipt checker from the lab. Save your predictions before you run the router.

## The saved change

The router checks exact, case-sensitive values. `RACK_CONFLICT` takes priority and produces `hold,RESOURCE_CONFLICT`. Otherwise, `AUTHORIZED` produces `pass,READY`. Exact `PENDING` uses the saved `pending_status` value: `OPEN` produces `hold,OPEN`; `NOT_AUTHORIZED` produces `reject,NOT_AUTHORIZED`. Other permit strings, including `WITHDRAWN`, fall back to `hold,OPEN`. Gate-window text and input disposition don't affect the route. A pending decision is not a quality release.

Change only Pending rule's String value, from `OPEN` to `NOT_AUTHORIZED`. Leave every other node setting, wire, and input as it is. Before you edit, keep the original JSON export and the separately downloaded SHA256 report for it. Keep the changed export as a separate file.

Importing JSON adds nodes to whatever n8n canvas is open, so import the checker into its own new blank workflow. To restore, recheck the original export against its saved digest, then import it into another new blank workflow. Don't restore by changing the policy value back by hand.

## Retain the evidence

Keep the frozen delta CSV for each wave, the baseline and changed exports, the original and rechecked identity reports, the six receipts, the baseline exact comparison, the two predicted-change reports, and the two restored exact reports. Record each workflow's name and URL and every execution ID. A successful execution isn't a comparison result: read the checker's `PASS` or `HOLD` report and its full row counts. Keep every held attempt, and never edit a receipt by hand.

The optional revised-wave stretch first changes the input with the policy held fixed, then changes the policy with the revised input held fixed. Each comparison needs its own frozen prediction and downloaded report.

## Class-only boundary

All lots, permits, windows, and notes are fictional practice data. Don't use this packet to plan, authorize, dispatch, or describe a real movement. A module result is for class review only.
