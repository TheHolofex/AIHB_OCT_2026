# Module 07 — Build and control a fixed workflow through change

**Serves oracle:** S04, S08, S13, S14, S17, S19  
**Primary objective:** PO-07 — Build and control a fixed workflow  
**Prerequisites:** Source verification, rules kept in code and tested against frozen expectations, failure preservation, and reversible recovery; local n8n readiness; this module's supplied waves, validator, and independent checker
**Consumes:** VERIFY:PREFLIGHT; VERIFY:CASE; VERIFY:BATCH_WORKLOAD; VERIFY:N8N_CONTROLS  
**Produces:** FIXED_BASELINE; EXCEPTION_RULE; DETERMINISTIC_DELTA; CONFIG_ID; RESTORE_ACTION; PO07_RESULT  
**Rough time:** about 3 hours  
**Performance stage:** Adversarial  
**Work surface:** Structured-data/batch work  
**Practical work:** Build a native visual n8n graph from a blank canvas; save and run it on two waves; change only the saved `pending_status` value; prove the complete deterministic effect; restore the original export into a new blank workflow and reproduce both waves.  
**Performance evidence:** Saved graph, ordered branch map, frozen source-based predictions, all-row comparison reports, original export with independent pre-edit SHA-256 record, changed export, verified original-export identity, and both restored receipts.  
**Failure / HOLD:** Missing local runtime or supplied controls, malformed input, altered checker or validator, unexpected route/status/serialization, missing or duplicated rows, manual record repair, lost original digest, import onto a populated canvas, or failed restoration. A green execution alone does not establish a comparison PASS.  
**Scope boundary:** Generated prose is excluded from deterministic acceptance before execution. No programming objective, model-based routing, persistent state, adaptive flow, multi-agent operation, or deployment.  
**Handoff:** Preserve the graph identities, inputs, frozen predictions, complete reports, original and changed exports, and the verified restore path.
**Case family:** [CASE_FAMILY.md](../../CASE_FAMILY.md). The adapter supplies a self-contained case in that family. This module does not consume another module's product.

## Capability added

Before this project, the learner can verify a source claim, keep a decision rule in code and test it against frozen expectations, and recover a reversible change. After it, the learner can compose those controls into a reusable batch process with explicit branch precedence, complete record accounting, and a proven policy-change boundary. Installing n8n and retaining files support that capability; they are not learning objectives.

## Enabling objectives

- Compose validation, first-match branching, exception handling, rejoining, source-order recovery, and terminal serialization into one saved native visual workflow.
- Predict and prove the complete effect of a single policy change across repeated batches, including every unaffected row and the exact serialized representation.
- Recover the original executable graph from an independently identified export and establish repeatability on both waves in a fresh workflow.

## Saved graph contract

Use local n8n 2.41.5 with the full official six-service Docker setup from the platform guide. Keep workflows unpublished and browser access on localhost. Native Windows PowerShell learners use WSL Ubuntu only for the n8n bridge; OMP, Python, Git, credentials, and other course work stay on their selected native path. n8n readiness is separate from OMP readiness.

The learner constructs the router from blank using native nodes: Form Trigger (`wave` file upload) → Extract from File (CSV) → Edit Fields (`Pending rule`, string `pending_status=OPEN`) → supplied batch validator in Code → Switch → four Edit Fields branches → Merge (Append) → Sort → Edit Fields → Convert to File (CSV). Paste the supplied validator unchanged; do not supply a completed router import or write routing code. n8n autosaves the graph; name it distinctly and confirm it persists when reopened. Import the supplied `receipt-checker.json` into a separate new blank workflow.

Retain all input fields through `Pending rule` and the branches. The validator checks the complete batch before routing and preserves source order in `_row`. Enable Always Output Data on CSV extraction so an empty/header-only file reaches validation; keep it off on branch nodes. Invalid inputs HOLD without trimming, coercing, repairing, or inventing records.

The Switch uses first match, case-sensitive exact equality, with Ignore Case OFF and Send data to all matching outputs OFF. Its ordered branches are:

| Condition | Route | Status |
|---|---|---|
| `resource_exception` exactly `RACK_CONFLICT` | `hold` | `RESOURCE_CONFLICT` |
| `permit` exactly `AUTHORIZED` | `pass` | `READY` |
| `permit` exactly `PENDING` | `hold` when `pending_status` is `OPEN`; `reject` when it is `NOT_AUTHORIZED` | saved `pending_status` |
| Fallback: every other permit | `hold` | `OPEN` |

Append the four branches, sort by `_row` ascending, then emit only `lot,route,status` in that order. Keep source strings unchanged. Upload waves through the current workflow's armed Form Trigger Test URL and download receipts from the binary output. Do not use production URLs, terminal routing, host/container file paths, or an AI Assistant.

## Complete comparison and restoration

Before any routing execution, predict the policy effect from each wave's source cells. Freeze one delta CSV per wave with header `lot,before_route,before_status,after_route,after_status`, one row per actual predicted change, no duplicates, and no unchanged rows. State explicitly that every other serialized row stays byte-identical and rack precedence holds. Use a header-only delta for zero predicted changes. Generated explanations cannot amend these predictions or determine routes.

Run both original waves through the saved graph. The supplied checker in `exact` mode must compare their complete receipts: 80 rows each, identical raw bytes, and identical structure. Download and inspect its report; a successful execution can still return HOLD. Retain all receipts and reports in a unique attempt folder without editing or overwriting their bytes.

Before editing the policy, export the original workflow JSON. In the independent checker, use `file-identity` with that export in both upload fields and leave `expected_sha256` empty only for this initial record. Preserve the downloaded `initial_record_only` SHA-256 report separately from the export. Change only the `Pending rule` string from `OPEN` to `NOT_AUTHORIZED`, run both unchanged input waves, and export the changed graph separately.

For each wave, use `predicted-change` against its retained baseline receipt and its frozen delta. Require comparison of every row, all declared changes and all unaffected fields, exact order/count/header, BOM, newlines, quotes, and serialization outside declared changed fields. Counts or selected-row checks alone are insufficient. No human output patch is allowed.

Recheck the preserved original export in `file-identity` mode using the original retained digest as `expected_sha256`; require PASS and `identity_check: matched`. Do not replace that expected digest with a newly calculated value. Import that exact original export into a new blank workflow: n8n import adds nodes to the current canvas. Give baseline, changed, and restored workflows distinct names. Run both waves through the restored graph, then require `exact` PASS against each corresponding retained baseline receipt, all 80 rows and raw bytes equal. Merely changing the visible value back is not restoration proof.

## Supplied-case domain (adapter)

White Rack moves refrigerated reagent kits from Icehouse Depot to Clinic I-6. Each wave contains 80 lots `LW-01`–`LW-80` with columns `lot,permit,gate_window,input_disposition,resource_exception`. Gate windows and input dispositions are provenance only. CANCELLED rows carry `WITHDRAWN` and remain `hold,OPEN`; permit lookalikes use the fallback. Rack conflicts hold before any permit rule. The baseline and second wave have identical permit and exception values, so their original receipts are byte-identical despite provenance changes.

Optional revised-input practice separates two effects: compare revised-wave baseline to wave-two baseline using a separately frozen input-change prediction, then compare revised-wave changed policy to revised-wave baseline using its own frozen policy-change prediction. Never combine membership changes with the policy delta.
