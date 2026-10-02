# Module 6 facilitator runbook

Help learners build a repeatable routing graph, predict one saved policy change, and distinguish execution from proof. The operating result is two complete predicted-change comparisons and two restored exact comparisons, supported by preserved inputs, exports, predictions, and reports. The fictional receipts never authorize real movement or product release.

## Prepare the room

Allow three hours on Wednesday, including two hours of practice; the Wednesday delivery route below allocates the minutes. Treat this as a planning allowance, not a measured completion claim. The remaining hour covers prerequisite recovery, short visual demonstrations, and discussion of observed results. If construction takes longer than its window, preserve the current state, record the unfinished lane as `HOLD`, and start the next independent block on schedule; do not replace the learner's graph with a completed router export to meet the clock.

Confirm each learner has completed the local n8n setup: version 2.41.5, the approved full official six-service stack, localhost-only browser access, and the platform-specific readiness observations. Keep Assistant off and workflows unpublished. Do not treat an OMP pass as n8n readiness. Resolve blocked setup using the existing setup guide, without substituting a cloud instance, production webhook, shell router, or container host-path upload.

Have the unchanged wave CSVs, supplied validate-batch.js, and receipt-checker.json available through the lab downloads. Learners need an ordinary text editor and browser uploads/downloads. Earlier source inspection, bounded-control validation, prediction, and evidence habits are prerequisites; recover a missing prerequisite directly where needed.

Before facilitating, complete the published click-by-click path on a separate staff attempt. Build the router from blank, run both waves, check their baseline byte identity, compare each changed wave against its own frozen prediction, export both policy conditions, verify the preserved baseline digest, restore into a new blank workflow, and obtain both restored exact reports. Check the revised-wave practice separately if using it. Preserve actual outcomes; don't describe an unrun path as verified. Keep completed router exports and row-level answer sets out of learner downloads and demonstrations before prediction.

## Wednesday delivery route

Module 6 is the third Wednesday block: 180 facilitated minutes, with 60 minutes of facilitation and 120 minutes of practice. Count elapsed minutes from the start of this block; breaks do not count. The block's break falls at minute 100, after initial graph construction. The day's clock is in `COURSE_MAP.md` and on the public homepage.

Before Wednesday, confirm the prerequisites this module already requires: local n8n readiness (version 2.41.5 on the approved full official stack, editor on localhost, a saved workflow that survives a stop and start) and the supplied wave CSVs, `validate-batch.js`, and `receipt-checker.json` from the lab downloads. This verifies existing prerequisites. It adds no homework.

| Elapsed minutes | Mode | Action and result |
|---|---|---|
| 0–15 | Facilitation | Case-specific boundary, readiness confirmation, and the new graph-composition capability. Remind learners of their source, predicate, and recovery skills rather than reteaching them. |
| 15–35 | Practice | Learners inspect both 80-row waves and freeze two source-derived predictions before any router execution. |
| 35–55 | Facilitation | Demonstrate native-node wiring, Fixed versus Expression, preserved source fields, and independent checker use, without giving a completed router or a predicted answer set. |
| 55–100 | Practice | Learners build and save the native router from a blank canvas. |
| 100–110 | Facilitation | Inspect branch precedence, complete record accounting, and the original-export and pre-edit digest sequence. |
| 110–130 | Practice | Learners preserve the original export and its separate initial identity report, run both baselines and their exact comparison, and inspect the source-supported routing. |
| 130–145 | Practice | Learners make the one saved policy edit, run both waves, save the changed export, and obtain both complete predicted-change reports. |
| 145–165 | Practice | Learners recheck the original digest, import it into a new blank workflow, rerun both waves, and obtain both restored exact reports. |
| 165–180 | Facilitation | Inspect the observed results, explain any `HOLD` and its recovery need, and establish the retained operating record. |

The rows total 60 facilitation minutes and 120 practice minutes.

Every native-n8n requirement in this runbook stays in force. The 13-node learner-built graph, the two 80-row waves, six receipts, five receipt-comparison reports, the original and changed exports, and the separately recorded pre-edit digest with its later matched recheck are all mandatory. Do not substitute a completed router, a one-wave shortcut, a manual output patch, or a manual reversal of the visible value as a restore. The optional revised-wave practice stays in the lab, unscheduled; claim it only if it was run.

Hold the clock without cutting the work:

- Save time by shortening repeated plenaries, using the lab's existing prerequisite reminders, and coaching while learners build and operate. Do not remove a lab explanation or supply a completed router, changed IDs, counts, or a prediction table to meet the clock.
- If a learner cannot finish a required operation in its window, preserve the first failure and the current state, record the unfinished lane as `HOLD`, and start the next independent block on schedule. Do not add a teaching day, move normal required practice into homework, or label an incomplete technical claim complete.

## Facilitate construction and prediction

Ask learners to explain a decision from the exact permit and exception cells before they execute the graph. They write their own per-wave delta CSVs and a note stating that every other serialized row stays byte-identical and rack precedence holds. Predictions must precede the first routing run and remain frozen before the edit. Do not supply changed IDs, counts, or a completed prediction table. If results were already exposed, retain that fact and label a later attempt honestly.

Demonstrate adding a node, selecting Fixed versus Expression, and dragging a wire using the lab settings. Let learners construct the actual router. Point to a source cell or node setting when helping; don't repair receipts or rewrite predictions to fit results. An explanation or a green execution cannot replace the downloaded comparison report.

Use the learner lab's numbered steps and images for the exact UI settings. The complete graph has 13 nodes. The key construction checks are:

- Upload wave has one required File field named wave, accepts .csv, and does not allow multiple files.
- Read CSV extracts binary wave, retains the header and empty cells, does not skip records with errors, and has Always Output Data on so empty extraction reaches validation.
- Pending rule adds the String pending_status while retaining inputs. Check batch reads the exactly named Read CSV node's original five-column rows, rejects a source-supplied policy column or any source-value replacement, and validates the entire policy-augmented batch before routing.
- Route lots uses ordered String equality rules: RACK_CONFLICT, AUTHORIZED, PENDING, then an extra fallback output. Ignore Case, Send data to all matching outputs, and Convert types where required are off.
- All four branch Edit Fields nodes retain inputs and leave Always Output Data off. Rack hold, Ready, Pending decision, and Other permit enter four distinct Merge inputs in that order.
- Merge uses Append. Original order sorts numeric _row ascending. Receipt fields removes everything except lot, route, status in that order. Make receipt creates CSV with headers and an execution-specific filename.

Keep the source strings intact. Unknown permit strings go to fallback; they are not an invitation to trim, coerce, or repair data. Gate-window and disposition values describe provenance. CANCELLED requires WITHDRAWN in validation but does not itself choose the route. Rack precedence remains first under both policy conditions.

## Watch the evidence sequence

The original router export must exist before the policy edit. The separate checker imports into a new blank workflow. Its initial file-identity run uploads the original export in both fields, leaves expected_sha256 empty, and produces a retained initial_record_only report. That report records the original digest; it is not restoration proof.

The two baseline receipts must each have 80 rows. The baseline exact report compares wave 1 baseline with wave 2 baseline: PASS, raw_byte_equal true, both row counts and row_count_checked 80, changed_count 0, unchanged_count 80. Also have learners inspect baseline decisions against source cells. Equal wrong outputs do not establish correct routing.

The only saved edit is Pending rule's String value OPEN → NOT_AUTHORIZED. The changed router retains its name, other settings, wires, and inputs. Learners reopen it to confirm persistence, run both waves, and compare each pair with that wave's frozen delta CSV. Each predicted-change report must return PASS, account for 80 rows, identify precisely the predicted changes, and retain all undeclared bytes. Counts alone do not establish a correct delta. Retain the changed export under a different filename before restoration.

For restoration, the checker must recheck the preserved original export using expected_sha256 copied from the original report, not recalculated from the current file. Require PASS and identity_check matched. Import that exact export into a NEW BLANK workflow: import adds nodes to the current canvas. Leave the changed workflow intact. Confirm OPEN, run each unchanged wave using the restored workflow's own Test URL, and compare each new receipt against its corresponding retained baseline in exact mode. Both reports must independently show PASS, raw byte equality, 80 checked rows, zero changed, and 80 unchanged.

The checker is a separate supplied graph. Its upload fans out to the direct file-preserving Merge input and two parallel Crypto hash nodes. Crypto drops binaries; chaining the hashes loses required uploads. Merge combines the three paths by position, then comparison produces the report and Convert to File makes it downloadable. Preserve this graph unchanged. Comparison HOLD can arrive in a successful green execution; read result and reason.

## Recover from concrete stops

| Observation | Stop and preserve | Recovery |
| --- | --- | --- |
| Editor unavailable or wrong n8n version | Record n8n HOLD and setup observations. | Use the platform setup recovery; retain earlier readiness results separately. |
| Form says not listening | Keep the intended workflow identity and any execution record. | Re-arm that workflow with Execute workflow, wait, then open its own current Test URL. Submit once. |
| Form uses an old workflow | Preserve the mistaken execution and download. | Copy the Test URL from the intended router, checker, or restored workflow and rerun to new filenames. |
| CSV extraction errors or Check batch throws HOLD | Retain the first error and source file. | Check extraction settings, supplied code body, and input selection. Do not skip errors, trim source strings, or bypass validation. |
| Empty/header-only input silently stops | Do not call it a successful validated batch. | Turn Read CSV Always Output Data on; keep error continuation off. Validation must receive the empty result and stop before routing. |
| Rows disappear or duplicate | Retain receipt and execution counts. | Inspect Switch first-match/fallback options, all four wires, Merge Append inputs, and branch Always Output Data off. |
| Receipt order or columns differ | Preserve both files and HOLD report. | Check _row retention, ascending Sort, and final three-field mapping. Never sort or resave a receipt externally. |
| Literal braces appear in output | Retain the failed receipt. | Use Expression mode for the specified values, then create a new baseline attempt if the baseline graph changes. |
| Predicted-change returns HOLD | Keep the original prediction, both receipts, and reason. | Diagnose source-cell reasoning, file selection, and graph settings. Append observations; do not change the frozen prediction after seeing output. |
| More than one saved parameter changed | Preserve both exports and observations. | Start a separate controlled attempt if the single change cannot be established. Do not claim a one-change proof. |
| Export digest mismatches or original report is missing | Retain the suspect export and report. | Locate the preserved original and its original digest report. If unavailable, start a new attempt; never replace the expected digest. |
| Import creates duplicate/mixed nodes | Leave that workflow unused and note its identity. | Create a NEW BLANK workflow and import the exact verified file there. |
| Restored exact check holds | Preserve all conditions and the report. | Check export identity, restored workflow URL, source selection, and receipt filenames. Do not manually reverse a value as a substitute for restore. |
| Browser adds a download suffix | Keep all downloads. | Copy each into the attempt folder under a unique stage name and record the actual path without editing bytes. |

If learners correct graph construction after baseline collection, treat that as a new graph condition. Preserve the old attempt and rebuild the baseline evidence under a new attempt identifier. Do not mix receipts from different graph conditions to assemble an apparent pass.

## Retained operating record

Look for a traceable record, not a score: attempt folder, frozen predictions, source filenames, workflow names and URLs, execution IDs, baseline and changed exports, original identity and digest recheck reports, six core receipts, and five core receipt comparisons. Observations should explain any HOLD without deleting it. A screenshot documents a UI state; downloaded reports document the comparison and file hashes. Keep secrets, account details, and completed prediction sets out of demonstration captures before prediction.

For optional revised-wave work, freeze two predictions first. Compare wave2-baseline against wave2-revised-baseline under OPEN to isolate input effects. Compare wave2-revised-baseline against wave2-revised-changed to isolate policy effects with the input fixed. Use the retained restored and changed workflows without another policy edit. Require a separate predicted-change report for each comparison and preserve all unchanged bytes. Leave unrun optional work unclaimed.
