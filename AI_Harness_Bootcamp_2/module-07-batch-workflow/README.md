# Module 7 · Operate a fixed workflow through change

Build a local visual n8n workflow to route White Rack's fictional shipment of refrigerated reagent kits from Icehouse Depot to Clinic I-6. Predict how one saved policy change will affect two batches of 80 lots. Compare every receipt row, whether it changed or not. Then restore the saved original workflow into a new blank canvas and use it to reproduce both original files exactly.

Plan for about three hours on Wednesday (a rough estimate).

## Before you begin

Complete [local n8n readiness](../module-00-setup/README.md), then open [Build, run, compare, and restore the workflow](shared/MODULE_07_LAB.md). Start with a blank router canvas. Download the two input waves, validator, and separate receipt checker from the lab. Save your prediction files before running the router.

Use n8n 2.41.5 on the approved full official local stack, with the editor on localhost. Check the sources, freeze your predictions before runs, validate with bounded controls like Blue Gauge's predicate, and keep all your evidence, as you did earlier. Have a plain text editor ready and know where your browser saves downloads. Keep Assistant off and workflows unpublished. Use test forms only, without model calls or provider credentials.

## The saved change

The router checks exact, case-sensitive values. `RACK_CONFLICT` takes priority and produces `hold,RESOURCE_CONFLICT`. Otherwise, `AUTHORIZED` produces `pass,READY`. Exact `PENDING` uses the saved `pending_status`: `OPEN` produces `hold,OPEN`; `NOT_AUTHORIZED` produces `reject,NOT_AUTHORIZED`. Other permit strings, including `WITHDRAWN`, fall back to `hold,OPEN`. Gate-window text and input disposition don't choose a route. A pending decision isn't a quality release.

Change only the Pending rule's String value from `OPEN` to `NOT_AUTHORIZED`. Keep every other node setting, wire, and input unchanged. Before editing, save the original JSON export and its separately downloaded SHA256 report. Save the changed export as a separate file.

Import the checker into its own new blank workflow; importing JSON adds nodes to the open canvas. To restore the original, check its export against the saved digest again, then import it into another new blank workflow. Don't change the policy back by hand.

## Retain the evidence

Keep each wave's frozen delta CSV, the baseline and changed exports, the original and rechecked identity reports, six receipts, the baseline exact comparison, two predicted-change reports, and two restored exact reports. Record each workflow's name and URL and every execution ID. Read the checker's `PASS` or `HOLD` report and full row counts; a successful execution doesn't tell you whether the files match. Keep every held attempt. Never edit a receipt by hand.

For the optional revised-wave stretch, first change the input with the policy fixed. Then change the policy with the revised input fixed. Freeze a separate prediction and download a report for each comparison.

## Class-only boundary

All lots, permits, windows, and notes are fictional practice data. Don't use this packet to plan, authorize, dispatch, or describe a real movement. A module result is for class use only.
