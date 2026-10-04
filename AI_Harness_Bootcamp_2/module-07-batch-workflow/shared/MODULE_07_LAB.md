# Module 7 · Build a workflow, predict a change, and prove the result

Build a local n8n workflow that routes White Rack's refrigerated reagent kits from Icehouse Depot to Clinic I-6. Predict what one policy change will do to two source batches, run both batches, and compare every receipt row. Save a copy of the original workflow, change one saved value, then restore the original into a new blank workflow and reproduce both original receipts.

Plan for about three hours on Wednesday. That's a rough estimate, not a measured time. All lots and movements are fictional. A receipt doesn't authorize a real movement, and it isn't a quality release.

You'll use three named workflows: your router, the supplied checker, and a restored router. Keep all three unpublished, and work only in the local browser editor and its test forms. A **receipt** is a downloaded CSV with the columns `lot,route,status`. An **exact comparison** checks the whole file, including column order, quotes, separators, and line endings. A green workflow run alone doesn't prove the files match.

## Prepare your files

Complete [local n8n readiness](../../module-00-setup/README.md) first: n8n **2.41.5**, the approved full official local stack, and the editor at `http://localhost:5678`. Keep Assistant off. You don't need a cloud account, provider key, published workflow, or production URL. Bring your source-checking and evidence habits from earlier modules.

In Finder or File Explorer, create a new folder such as `module-07-attempt-2026-10-01-a`. Give each attempt its own name. Inside it, create `inputs`, `predictions`, `exports`, `receipts`, and `reports`, and use your plain-text editor to create an empty text file named `observations.md`. Whenever a step says to record something, write it there. Download these exercise files into `inputs`:

- [wave1.csv](batch/wave1.csv)
- [wave2.csv](batch/wave2.csv)
- [validate-batch.js](controls/validate-batch.js)
- [receipt-checker.json](controls/receipt-checker.json)

Right-click each link and choose **Save link as** (**Download Linked File As** in Safari). On macOS, Control-click also opens the link menu. Keep the filename and extension shown above. If you click a link instead of saving it, the browser may just show the file as text.

Don't change the source CSVs. View them in a plain text editor, and don't save them from a spreadsheet. Copy each browser download into the right folder, under the name the step gives. Renaming a file is fine, but opening and resaving it can change its bytes. Keep the original download too. Never replace a receipt, export, or report you've kept. If a name is already taken, add a new attempt suffix and record the name you actually used.

**Expected:** You can open both CSVs and see the header `lot,permit,gate_window,input_disposition,resource_exception`, in that order. Each wave has 80 lots. **Stop:** A file is missing, the local editor isn't ready, or a source was changed. **Recovery:** Finish setup, or download a fresh copy of the source into a new attempt folder, before you go on.

## Freeze predictions before any routing run

Read the `permit` and `resource_exception` cells in both waves. The router checks these conditions in order:

| First matching condition | Receipt under `OPEN` | Receipt under `NOT_AUTHORIZED` |
| --- | --- | --- |
| `resource_exception` exactly `RACK_CONFLICT` | `hold,RESOURCE_CONFLICT` | `hold,RESOURCE_CONFLICT` |
| Otherwise, `permit` exactly `AUTHORIZED` | `pass,READY` | `pass,READY` |
| Otherwise, `permit` exactly `PENDING` | `hold,OPEN` | `reject,NOT_AUTHORIZED` |
| Otherwise | `hold,OPEN` | `hold,OPEN` |

Matches are case-sensitive. A shortened, lowercase, or space-padded permit is a different string and goes to the fallback. `gate_window` and `input_disposition` describe the input, but they don't choose a route. Cancelled lots carry `WITHDRAWN`, which goes to the fallback unless the rack rule catches the lot first. Never trim or fix a source value to force a match.

In your plain text editor, create `predictions/prediction.md`. For each wave, record the source filename, the cells each expected decision rests on, and the rack claimants that must stay held. Then write this sentence: “Every other serialized row stays byte-identical, and rack precedence holds.” A serialized row is the exact text saved in the CSV, not just what a spreadsheet shows.

Create `predictions/wave1-delta.csv` and `predictions/wave2-delta.csv`. Start each with this exact header:

```csv
lot,before_route,before_status,after_route,after_status
```

Add one row for each lot you predict will actually change when `OPEN` becomes `NOT_AUTHORIZED`. Use that lot's source ID and its predicted before and after values. Don't include unchanged lots or repeat an ID. If you predict no changes, keep just the header. Save all three prediction files before you run the router, and record the date and time in the note. Once results arrive, write your observations in a separate file; don't replace your original prediction or quietly fix its delta CSV.

**Expected:** You can trace each predicted change to source cells, and each wave has its own frozen delta. **Stop:** A routing run has already shown you results, or you can't explain a predicted row from its cells. **Recovery:** Keep the attempt and record what you saw. Check the sources again and start a new, clearly named attempt; don't present a prediction made after a run as one made before it.

## Build the router from a blank canvas

Build the fixed workflow node by node, so every routing rule is visible on the canvas and nothing depends on a hidden setting.

To add each node, click the **+** on the previous node's output, search for the node type shown in bold, and select it. n8n connects it to the previous node for you. Click the node title, type the exact name shown, and press Enter. Go back to the canvas once you've set its fields. To connect nodes that already exist, drag from the source's right output connector to the destination's left input connector. Check that the wire is there instead of assuming it was added.

For Edit Fields nodes, use **Manual Mapping** and **Add Field**, and set each field's type to **String**. Use **Fixed** for literal values. For values inside `{{ }}`, switch the value control to **Expression** and paste the whole expression. Don't paste an expression as fixed text. Leave any setting not mentioned here at its default. Leave **Settings → On Error** at **Stop Workflow**; don't turn on retries, error continuation, or pinned test data.

### 1. Create and name the blank router

Open **Overview → Build a workflow** on a fresh installation, or **Overview → Create workflow** when workflows already exist. Click the workflow title, enter `White Rack — attempt a — router` (use your attempt identifier in place of `a`), and press Enter. n8n saves automatically, so there's no Save or Saved indicator to wait for. Leave the workflow unpublished.

![Blank n8n canvas named White Rack — attempt a — router, with no nodes](figures/m07-n8n-01-blank-router.png)

**Expected:** The named canvas has no nodes. **Stop:** An existing graph is visible. **Recovery:** Return to Overview and create a new workflow; don't clear someone else's canvas.

### 2. Add the upload form

Click **Add first step**, search **n8n Form**, and choose **On new n8n Form event**. Rename it `Upload wave`. Set **Form Title** to `White Rack — upload one wave` and **Form Description** to `Use the test form. Upload one unchanged source CSV.` Under **Form Elements**, select **Add Form Element**. Set **Field Label** to `wave` and **Element Type** to `File`. Use **Add Attributes** to show **Multiple Files**, **Accepted File Types**, and **Required Field**. Turn Multiple Files off, enter `.csv` for Accepted File Types, and turn Required Field on. Keep authentication at **None** for this local test form. Don't execute it yet.

![Upload wave form settings show required single CSV file field named wave](figures/m07-n8n-02-upload-field.png)

**Expected:** There is exactly one upload field named `wave`. **Stop:** The field allows multiple files or uses a different label. **Recovery:** Fix the field before you add more nodes; later nodes use its label as the key to find the uploaded file.

### 3. Extract the CSV without dropping empty cells

From Upload wave, add **Extract from File** and rename it `Read CSV`. Select **Extract From CSV**. Set **Input Binary Field** to `wave`. Under **Options**, use **Add option** to show **Header Row**, **Include Empty Cells**, and **Skip Records with Errors**. Turn Header Row and Include Empty Cells on. Keep Skip Records with Errors → **Enabled** off. Open **Settings** and turn **Always Output Data** on. Go back to Parameters and check that the input field is still `wave`.

![Read CSV uses wave with Header Row and Include Empty Cells on and Skip Records with Errors disabled](figures/m07-n8n-03-read-csv.png)

![Read CSV has Always Output Data on so a header-only extraction reaches validation](figures/m07-n8n-03-empty-batch-setting.png)

**Expected:** Upload wave connects to Read CSV. An empty or header-only file still reaches validation instead of the run quietly stopping there. **Stop:** Errors are skipped or empty cells are dropped. **Recovery:** Fix these settings; don't work around them by changing the source file.

### 4. Add the single saved policy value

From Read CSV, add **Edit Fields (Set)** and rename it `Pending rule`. Select **Manual Mapping**. Add one String field named `pending_status`, with Fixed value `OPEN`. Turn **Include Other Input Fields** on so every input field passes through.

![Pending rule adds the String pending_status set to OPEN while retaining input fields](figures/m07-n8n-04-pending-rule.png)

**Expected:** This node adds one value without replacing the source columns. **Stop:** Include Other Input Fields is off or the value is an expression. **Recovery:** Turn the setting back on and set the value to the fixed text `OPEN`.

### 5. Install the supplied batch validation

From Pending rule, add **Code** and rename it `Check batch`. Choose **JavaScript** and **Run Once for All Items**. Open the downloaded `validate-batch.js` in your plain text editor, select everything, and copy it. In the node, select all the placeholder code and paste the supplied code over it without changes.

The validator reads `Read CSV`'s original output as well as the rows with the policy value added, so keep that node's name exactly. It checks that the source has exactly the five source columns, in order, that source values and row order are unchanged, and that every value is a string. Lot IDs must be unique and nonblank, with no commas, quotes, or ASCII control characters. Dispositions and exceptions must be valid, a cancelled lot must carry `WITHDRAWN`, and every row must have the same saved policy value. A `pending_status` column in the source is invalid even though Pending rule would overwrite it. The validator adds `_row`, each row's position in the source, without changing any source text. Invalid input stops before routing. Unknown permit strings are still valid input; they go to the fallback.

![Check batch is JavaScript in Run Once for All Items mode with the supplied validator body](figures/m07-n8n-05-check-batch.png)

**Expected:** The wire is Pending rule → Check batch, and no placeholder code remains. **Stop:** The code was shortened, rewritten, or put in per-item mode. **Recovery:** Paste the whole supplied file in again and set the mode back to Run Once for All Items. Don't add routing code here.

### 6. Set ordered, case-sensitive routing

From Check batch, add **Switch** and rename it `Route lots`. Select **Rules** mode. Add exactly three routing rules in this order. Each uses **String → is equal to**, an Expression on the left, and a Fixed value on the right:

| Output | Left expression | Right fixed value |
| --- | --- | --- |
| 0, first rule | `{{$json.resource_exception}}` | `RACK_CONFLICT` |
| 1, second rule | `{{$json.permit}}` | `AUTHORIZED` |
| 2, third rule | `{{$json.permit}}` | `PENDING` |

Under **Options**, use **Add option** to show **Fallback Output**, **Ignore Case**, and **Send data to all matching outputs**. Set Fallback Output to **Extra Output**, Ignore Case off, and Send data to all matching outputs off. Leave **Convert types where required** off. Keep one condition per rule. The first matching rule wins, so rack conflicts can't also enter the permit branches.

![Route lots places exact rack matching before exact AUTHORIZED matching](figures/m07-n8n-06-switch-rules.png)

![The third rule matches exact PENDING; fallback is Extra Output and case folding and all-match routing are off](figures/m07-n8n-06-switch-options.png)

**Expected:** Four output connectors appear: three rules and the fallback. **Stop:** Rules use contains, ignore case, or send to all matches. **Recovery:** Set the rules back to exact equality and the options back to the values above before you wire the branches.

### 7. Wire the rack hold branch

Click the **+** on Route lots output **0**, the first rule. Add **Edit Fields (Set)** and rename it `Rack hold`. Use Manual Mapping. Add String fields `route` = Fixed `hold` and `status` = Fixed `RESOURCE_CONFLICT`. Turn **Include Other Input Fields** on. Leave **Settings → Always Output Data** off.

![Rack hold sets hold and RESOURCE_CONFLICT and connects to the first Switch output](figures/m07-n8n-07-rack-hold.png)

**Expected:** Only the first Switch output feeds Rack hold, and `_row` passes through. **Stop:** The node hangs off another branch, or it drops input fields. **Recovery:** Delete the wrong wire and connect output 0 straight to Rack hold.

### 8. Wire the authorized branch

From Route lots output **1**, add **Edit Fields (Set)** named `Ready`. Use Manual Mapping with String fields `route` = Fixed `pass` and `status` = Fixed `READY`. Turn **Include Other Input Fields** on. Leave **Always Output Data** off.

![Ready maps pass and READY from the second Switch output with source fields retained](figures/m07-n8n-08-ready.png)

**Expected:** Output 1 feeds Ready directly. **Stop:** Ready receives rack or pending output. **Recovery:** Reconnect the correct Switch output; don't change the branch values to hide a wiring error.

### 9. Wire the pending branch

From Route lots output **2**, add **Edit Fields (Set)** named `Pending decision`. Use Manual Mapping. Add String `route` in Expression mode with `{{$json.pending_status === 'NOT_AUTHORIZED' ? 'reject' : 'hold'}}`. Add String `status` in Expression mode with `{{$json.pending_status}}`. Turn **Include Other Input Fields** on. Leave **Always Output Data** off.

![Pending decision uses expressions for route and status and retains other input fields](figures/m07-n8n-09-pending-decision.png)

**Expected:** Both values are expressions and output 2 feeds this node. **Stop:** An expression shows up as plain text, or status is fixed to OPEN. **Recovery:** Select Expression mode and paste the exact expressions.

### 10. Wire the fallback

From Route lots' **Fallback** output, add **Edit Fields (Set)** named `Other permit`. Use Manual Mapping with String fields `route` = Fixed `hold` and `status` = Fixed `OPEN`. Turn **Include Other Input Fields** on. Leave **Always Output Data** off.

![Other permit is connected to fallback and sets hold and OPEN](figures/m07-n8n-10-fallback.png)

**Expected:** All unmatched permit strings have a path to a receipt. **Stop:** The fallback is unconnected or points to Pending decision. **Recovery:** Connect it to Other permit and keep the fixed values.

### 11. Collect all four branches

From Rack hold, add **Merge** named `Collect routes`. Set **Mode** to **Append** and **Number of Inputs** to `4`. Connect the branches to its inputs in this order: Rack hold → **Input 1** (index 0); Ready → **Input 2** (index 1); Pending decision → **Input 3** (index 2); Other permit → **Input 4** (index 3). Drag the remaining three wires on the canvas. Check that each branch has exactly one connection to its own Merge input.

![Collect routes is configured for Append with four inputs](figures/m07-n8n-11-collect-routes.png)

![Four distinct branch wires enter Collect routes before Original order restores source order](figures/m07-n8n-11-branch-wires.png)

**Expected:** Four distinct branch wires enter Merge. **Stop:** Mode is Combine, an input is missing, or a branch has Always Output Data on. **Recovery:** Set Mode back to Append and fix the four wires. Turn off Always Output Data on the branches so an empty branch can't add made-up rows.

### 12. Restore source order

From Collect routes, add **Sort** named `Original order`. Select **Simple** sorting. Add a sort field named `_row` with **Ascending** order. `_row` must still be present here: Merge groups the rows by branch, and this sort puts them back in source order.

![Original order sorts the retained numeric _row field ascending](figures/m07-n8n-12-original-order.png)

**Expected:** Collect routes connects to Original order, which sorts only on `_row`. **Stop:** The sort uses lot, route, or status. **Recovery:** Replace that sort field with `_row`; don't reorder the input file.

### 13. Keep only the receipt columns

From Original order, add **Edit Fields (Set)** named `Receipt fields`. Use Manual Mapping. Add these String fields in this exact order, each in Expression mode: `lot` = `{{$json.lot}}`, `route` = `{{$json.route}}`, `status` = `{{$json.status}}`. Turn **Include Other Input Fields** off. This is the first node that drops `_row` and the source-only fields.

![Receipt fields contains only lot, route, and status expressions in that order with other fields excluded](figures/m07-n8n-13-receipt-fields.png)

**Expected:** Exactly three fields remain, in the order above. **Stop:** A source field or pending_status is included. **Recovery:** Turn off Include Other Input Fields and remove any extra fields.

### 14. Make a downloadable CSV

From Receipt fields, add **Convert to File** named `Make receipt`. Choose **Convert to CSV**. Set **Put Output File in Field** to `data`. Under **Options**, turn **Header Row** on and set **File Name** in Expression mode to `white-rack-{{$execution.id}}.csv`. Keep the remaining CSV options at their defaults. Go back to the canvas and follow the whole path from Upload wave through all four branches to Make receipt.

![Make receipt converts the three fields to a CSV with headers and an execution-specific filename](figures/m07-n8n-14-make-receipt.png)

![The complete 13-node router validates before routing and sorts after all four branches rejoin](figures/m07-n8n-complete-canvas.png)

**Expected:** The graph has 13 nodes, with validation before Switch and Sort after Merge. **Stop:** There is an extra path around validation, a missing branch, or a disconnected final node. **Recovery:** Fix the wires before you run anything. Don't import a finished router instead of building it.

## Preserve the baseline and prepare the independent checker

Save the untouched router as a file you can restore from, and set up a separate checker that compares receipts without trusting the router.

### 15. Export the original router

Return to Overview, reopen your named router, and inspect Pending rule: `pending_status` must still be Fixed `OPEN`. Return to the canvas. Open the **three-dot menu beside the workflow name** and choose **Export JSON**. Copy the download into `exports/router-baseline.json`. Record the router's name and browser URL in `observations.md`. Keep this file exactly as it is; later exports get different names.

![Router menu offers Export JSON while the original graph is still unchanged](figures/m07-n8n-15-baseline-export.png)

**Expected:** A nonempty baseline JSON export exists before you edit the policy. **Stop:** The policy has already changed, or the file would replace an earlier export. **Recovery:** Keep what exists and start a separate baseline attempt; don't relabel a changed export as the original.

### 16. Import the checker into a new blank workflow

Choose **Overview → Create workflow**. Confirm there are no nodes. Open the **three-dot menu beside the workflow name**, choose **Import → From file**, and select `receipt-checker.json`. Import adds nodes to the open canvas, so never do this on your router. Rename this workflow `White Rack — attempt a — checker` and press Enter. Keep it unpublished.

Check the supplied graph: Upload comparison feeds input 1 of Keep files and hashes directly, Hash baseline feeds input 2, and Hash actual feeds input 3. Both hash nodes take their input straight from Upload comparison. Keep files and hashes combines its inputs by position, then feeds Compare complete files → Download report. Don't change this graph. The parallel paths keep the uploaded files intact while the Crypto nodes compute the hashes.

![Separate checker canvas contains the upload, two parallel hash paths, file merge, comparison, and report download](figures/m07-n8n-16-checker-import.png)

**Expected:** Six nodes appear, with no router nodes. **Stop:** The import mixed in other nodes, or the hash nodes are chained one after the other. **Recovery:** Leave that workflow unused and import the supplied checker into another new blank workflow.

### 17. Record the original export's digest separately

Open **Upload comparison** and copy its **Test URL**. Return to the canvas and click **Execute workflow**. Wait until the form is listening, then open that Test URL in another browser tab. In `baseline`, choose `exports/router-baseline.json`; in `actual`, choose the same file. Set `mode` to `file-identity`. Leave `delta` and `expected_sha256` empty. Click **Submit** once.

Return to the checker editor. Open **Compare complete files → Output → Schema** or **JSON**. Check for `result: PASS`, `raw_byte_equal: true`, and `identity_check: initial_record_only`. Double-click the **Download report** node. In the right-hand **OUTPUT** panel, select the **Binary** tab and click **Download** under the file card. Copy it to `reports/baseline-original-identity.json`. This report stores the original SHA256 digest, a fingerprint of the file's bytes. Keep it separate from the export, and record its path in `observations.md`.

![Initial file-identity report shows PASS and initial_record_only for the original router export](figures/m07-n8n-17-original-hash.png)

**Expected:** The saved report shows the same SHA256 value for baseline and actual. **Stop:** The report says HOLD, the files differ, or you entered an expected digest on this first record. **Recovery:** Keep the report, select the original export in both fields, and run it again under a new report name. This first record sets the reference; it doesn't prove restoration yet.

## Run and compare the two baseline waves

Make the two reference receipts under the unchanged policy, and prove they match each other before you change anything.

Before every form run, re-arm the workflow the form belongs to with **Execute workflow**, wait for it to start listening, and use the **Test URL from that workflow**. Don't reuse a form tab from another workflow or from an earlier restored copy. If the form says it isn't listening, go back to the right editor, re-arm it, and reopen its Test URL. Submit once per execution, and use the current execution's output, not an older node preview.

### 18. Run and download wave 1 under OPEN

Open your router from Overview. Confirm Pending rule is `OPEN` and your predictions are already saved. Open Upload wave and copy its Test URL. Return to the canvas, click **Execute workflow**, wait for the listener, then open the Test URL. Click **Choose file**, select the unchanged `inputs/wave1.csv`, and click **Submit** once. Return to the editor. Check the outputs of Check batch and Receipt fields: each must contain 80 items. Double-click the **Make receipt** node. In the right-hand **OUTPUT** panel, select the **Binary** tab. Under the `data` file card, click **Download**. Copy the downloaded file to `receipts/wave1-baseline.csv`. Record the execution ID, the source filename, and the name you saved the receipt under.

![Wave 1 baseline execution reaches Make receipt with a CSV available in Binary output](figures/m07-n8n-18-wave1-baseline.png)

**Expected:** All 80 source lots reach the three-column receipt. **Stop:** Validation stops with HOLD, a node fails, or the count differs. **Recovery:** Keep the execution error and compare the first failing node's settings with the build steps. Don't trim inputs, bypass validation, or make up a receipt.

### 19. Run and download wave 2 under OPEN

On the same unchanged router, click **Execute workflow** again. Open its current Test URL, choose `inputs/wave2.csv`, and Submit once. Check that Check batch and Receipt fields show 80 items. Download Make receipt's Binary file the same way and save it as `receipts/wave2-baseline.csv`. Record this execution separately. Check both baseline receipts against the decisions in your frozen note, without resaving either file.

![Wave 2 baseline execution shows 80 receipt items and its separate downloadable CSV](figures/m07-n8n-19-wave2-baseline.png)

**Expected:** Both receipts follow the OPEN policy and rack precedence. **Stop:** A baseline decision doesn't match the source, or wave 1 was uploaded again. **Recovery:** Keep the mistaken run and work out whether the source selection or the graph is wrong; repeat under a new filename. A byte match alone can't prove you built the routing rule correctly.

### 20. Prove the two baseline files match exactly

Open the checker, click **Execute workflow**, and open its Test URL once it's listening. Choose `wave1-baseline.csv` for `baseline` and `wave2-baseline.csv` for `actual`. Select `mode` = `exact`. Leave `delta` and `expected_sha256` empty. Submit once. Inspect Compare complete files, then download the report from Download report's Binary output to `reports/baseline-waves-exact.json`.

![Exact baseline comparison reports PASS, raw byte equality, and all 80 rows unchanged](figures/m07-n8n-20-baseline-exact.png)

**Expected:** `result` is `PASS`, `raw_byte_equal` is `true`, both row counts and `row_count_checked` are `80`, `changed_count` is `0`, and `unchanged_count` is `80`. **Stop:** Any field disagrees, even if the workflow is green. **Recovery:** Keep the HOLD report and both receipts. Check the uploaded filenames, branch wires, sorting, and receipt columns before a new run. Don't clean up the files to make them match.

## Change one saved value and prove both deltas

Change the single policy value, rerun both waves, and prove the checker sees exactly your predicted changes and nothing else.

### 21. Save only the intended policy change

Return to your router. Check that you still have the original export, the original identity report, both baselines, the baseline exact report, and the frozen predictions. Open Pending rule. Change only its Fixed String value from `OPEN` to `NOT_AUTHORIZED`. Return to Overview and reopen the same router to confirm the new value was saved. Leave the workflow name, every other setting, every wire, and every input unchanged. Record the node, field, old value, and new value in `observations.md`.

![Pending rule retains the same field and input setting with only its value changed to NOT_AUTHORIZED](figures/m07-n8n-21-one-saved-change.png)

**Expected:** One saved parameter changed: Pending rule's `pending_status`. **Stop:** Another parameter, expression, wire, or input changed. **Recovery:** Keep the attempt and its exports. If you can't show that only that one value changed, start a new baseline attempt; don't rewrite evidence to hide extra edits.

### 22. Run and retain both changed receipts

Click Execute workflow on the changed router, wait, open its Test URL, upload `wave1.csv`, and Submit once. Check for 80 receipt items and download the Binary CSV as `receipts/wave1-changed.csv`. Re-arm the same router and repeat with `wave2.csv`, saving the receipt as `receipts/wave2-changed.csv`. Record both execution IDs and filenames. Don't change the policy between runs.

![Make receipt offers the changed run's CSV for download](figures/m07-n8n-22-changed-runs.png)

**Expected:** Each run produces 80 receipt rows under the same changed policy. **Stop:** A run fails, a count differs, or you're not sure which source was uploaded. **Recovery:** Keep the failed run and look at the first error or the file you uploaded. Fix the cause, then repeat using new filenames.

### 23. Prove wave 1's predicted change

Re-arm the checker and open its Test URL. Set `baseline` to `wave1-baseline.csv`, `actual` to `wave1-changed.csv`, `delta` to the frozen `wave1-delta.csv`, and `mode` to `predicted-change`. Leave `expected_sha256` empty. Submit, inspect Compare complete files, and download the report as `reports/wave1-predicted-change.json`.

The checker compares every row. Each change you declared must happen, with exactly the before and after values you gave, and every row you didn't declare must stay byte-identical. It also checks the row count, order, header, byte-order mark, quotes, and line endings. It doesn't work out your prediction from the output.

![Wave 1 predicted-change report shows its selected files, result, checked row count, and changed and unchanged counts](figures/m07-n8n-23-wave1-delta.png)

**Expected:** `PASS`, both row counts and `row_count_checked` equal `80`, and the changed and unchanged counts add up to `80`. `changed_ids` matches your frozen wave 1 list exactly, and no rack claimant appears in it. **Stop:** A prediction is missing, extra, or wrong, or any undeclared bytes differ. **Recovery:** Keep the HOLD report and the original prediction. Explain the mismatch in your observations; don't revise the prediction after seeing the output and call that the original proof.

### 24. Prove wave 2's predicted change

Re-arm the checker. Upload `wave2-baseline.csv`, `wave2-changed.csv`, and the frozen `wave2-delta.csv` in their matching fields. Select `predicted-change`, leave expected_sha256 empty, and Submit. Download the report as `reports/wave2-predicted-change.json`.

![Wave 2 predicted-change report identifies wave 2 files and accounts for all 80 rows](figures/m07-n8n-24-wave2-delta.png)

**Expected:** `PASS`, 80 baseline rows, 80 actual rows, and 80 rows checked. The changed IDs match wave 2's frozen prediction exactly, and every other row is byte-identical. **Stop:** The report used wave 1 files, a rack claimant changed, or the result is HOLD. **Recovery:** Keep the report and check the exact filenames and source cells. If you correct the file selection, save under a new report name; keep any mistaken prediction exactly as you wrote it.

### 25. Export the changed workflow separately

Open the changed router's **three-dot menu beside the workflow name** and choose **Export JSON**. Save the download as `exports/router-changed.json`. Don't touch the baseline export or the original digest report. Record the changed router's name, URL, export path, and the two changed execution IDs in `observations.md`.

![Changed router Export JSON action preserves a separate changed workflow before restoration](figures/m07-n8n-25-changed-export.png)

**Expected:** The baseline and changed exports are separate files. **Stop:** Saving would replace router-baseline.json. **Recovery:** Cancel the replacement and use the changed filename. If the original was overwritten, stop; a new hash can't recover the old reference.

## Restore the preserved baseline and prove both reruns

Put the original router back from the saved export, then prove the restored copy produces the baseline receipts byte for byte.

### 26. Recheck the original export against its retained digest

Open `reports/baseline-original-identity.json` read-only and copy its original `baseline_sha256` value. Re-arm the checker. Upload the preserved `router-baseline.json` in both file fields, select `file-identity`, leave delta empty, and paste the original value into `expected_sha256`. Submit and download `reports/baseline-identity-recheck.json`.

![File-identity recheck reports PASS and matched against the original retained expected SHA256](figures/m07-n8n-26-digest-recheck.png)

**Expected:** `PASS`, `identity_check: matched`, `raw_byte_equal: true`, and expected_sha256 equals the digest in the original report. **Stop:** The result is mismatch or initial_record_only, or the original report is missing. **Recovery:** Keep the failed report and find the original file and report. Never calculate a new expected digest from the file you're trying to verify.

### 27. Restore into a NEW BLANK workflow

Choose **Overview → Create workflow**. Confirm the canvas is completely empty. Only then open the **three-dot menu beside the workflow name**, choose **Import → From file**, and select the exact `router-baseline.json` that passed the digest recheck. Import adds nodes; it doesn't replace what's already on the canvas. Rename the new workflow `White Rack — attempt a — restored` and press Enter. Keep it unpublished. Open Pending rule and confirm `OPEN`. Follow the 13-node graph and check all four Merge inputs. Leave the changed router intact.

![An empty new workflow has Import → From file open before the baseline is selected](figures/m07-n8n-27-blank-restore.png)

![The imported baseline retains Pending rule's fixed OPEN value](figures/m07-n8n-27-restored-rule.png)

**Expected:** A separate restored workflow holds one router graph, set to OPEN. **Stop:** There are duplicate nodes or checker nodes, or the value is still NOT_AUTHORIZED. **Recovery:** Leave that mixed workflow unused. Create another new blank workflow and import the verified original export. Don't change the value back by hand and call that an import restore.

### 28. Run restored wave 1

Open Upload wave in the restored workflow and copy its own Test URL. Click Execute workflow, wait until it's listening, open that URL, upload unchanged `wave1.csv`, and Submit once. Check for 80 receipt items. Download the new Binary CSV as `receipts/wave1-restored.csv`. Record the restored workflow URL and execution ID.

![Restored workflow's wave 1 execution offers its receipt for download](figures/m07-n8n-28-wave1-restored.png)

**Expected:** The execution belongs to the restored workflow, not the old router. **Stop:** An old form tab submitted to the changed workflow, or a row count differs. **Recovery:** Keep the mistaken run, copy the restored workflow's own Test URL, and repeat, saving to a new receipt name.

### 29. Prove restored wave 1 is exact

Re-arm the checker. Upload `wave1-baseline.csv` as baseline and `wave1-restored.csv` as actual. Select `exact`; leave delta and expected_sha256 empty. Submit and download `reports/wave1-restored-exact.json`.

![Wave 1 restored exact report shows PASS, raw byte equality, and 80 unchanged rows](figures/m07-n8n-29-wave1-restored-exact.png)

**Expected:** `PASS`, raw byte equality true, both row counts and checked count `80`, changed count `0`, unchanged count `80`. **Stop:** Any byte differs or the report checks different files. **Recovery:** Keep the report. Check which workflow ran, the imported export's digest, and which files you uploaded; don't edit the receipt's bytes.

### 30. Run restored wave 2

Re-arm the restored router, open its own Test URL, upload unchanged `wave2.csv`, and Submit once. Check that there are 80 receipt items, then download `receipts/wave2-restored.csv`. Record the execution ID and source filename.

![Restored workflow's separate wave 2 execution produces its downloadable receipt](figures/m07-n8n-30-wave2-restored.png)

**Expected:** The restored graph, still set to OPEN, produces the second restored receipt. **Stop:** The workflow, policy, source, or item count is wrong. **Recovery:** Keep the execution and fix the specific mismatch before you download a new attempt.

### 31. Prove restored wave 2 is exact

Re-arm the checker. Upload `wave2-baseline.csv` as baseline and `wave2-restored.csv` as actual. Select `exact`, leave delta and expected_sha256 empty, and Submit. Download `reports/wave2-restored-exact.json`.

![Wave 2 restored exact report shows PASS, raw byte equality, and all 80 rows unchanged](figures/m07-n8n-31-wave2-restored-exact.png)

**Expected:** `PASS`, raw byte equality true, 80 rows on both sides and checked, zero changed, and 80 unchanged. **Stop:** The report says HOLD, or only wave 1 has a restored proof. **Recovery:** Keep the evidence and sort out wave 2 on its own. One matching wave doesn't prove the other.

## Keep a usable operating record

In `observations.md`, record the attempt path; all three workflow names and URLs; the input filenames; the execution IDs; the baseline and changed export paths; the original and rechecked digest reports; the six receipt paths; and the five receipt comparison reports. State the one saved change and whether each comparison passed or held. Keep the original frozen predictions in their own files. The reports contain receipt sizes and hashes; quote the values from your saved reports, not a digest copied from a screenshot.

Explain any mismatch from the source cells, node settings, or files you selected. State that input disposition never chose a route and that rack precedence held. Screenshots show settings and which execution ran; the downloaded checker reports are what prove how the files compare. Leave a held attempt as it is, and label any later attempt separately.

<details class="rf-stretch" markdown="1">
<summary>Optional stretch: separate an input revision from the policy change</summary>

Download [wave2-revised.csv](batch/wave2-revised.csv) into `inputs`. Before you run it, compare its source cells with wave2.csv. Freeze two new delta CSVs that start with the same header as your wave delta files, `lot,before_route,before_status,after_route,after_status`. In `revised-input-delta.csv`, predict the changes from the wave 2 baseline to the revised wave's baseline, with OPEN held fixed. In `revised-policy-delta.csv`, predict the changes from the revised wave's baseline to its changed run, with the revised input held fixed. In a separate note, name each source cell that changed, state that every other row must stay unchanged, and state that rack precedence holds. If you predict no output changes, use a delta with just the header. Don't explain either effect with a comparison that changes the input and the policy at once.

**Expected:** Both predictions exist before either revised run. **Stop:** A prediction relies on results you've already seen. **Recovery:** Keep the observation, and label any new attempt as one made after you'd seen results.

### 32. Produce the revised baseline with policy fixed

Open the restored router and confirm OPEN. Re-arm it, open its Test URL, upload wave2-revised.csv, and Submit. Check for 80 receipt items and download `receipts/wave2-revised-baseline.csv`. Keep the restored policy unchanged.

![Restored OPEN router processes the revised input and offers the revised baseline receipt](figures/m07-n8n-32-revised-baseline.png)

**Expected:** The only difference from the wave 2 baseline run is the input file. **Stop:** The policy is NOT_AUTHORIZED, or the wrong input was uploaded. **Recovery:** Keep that run and repeat on the correct restored graph with a new filename.

### 33. Prove the input-only effect

Re-arm the checker. Upload `wave2-baseline.csv` as baseline, `wave2-revised-baseline.csv` as actual, and frozen `revised-input-delta.csv` as delta. Select predicted-change, leave expected_sha256 empty, and Submit. Download `reports/revised-input-delta.json`.

![Input-only comparison pairs the original and revised OPEN receipts with the frozen input delta](figures/m07-n8n-33-input-only-proof.png)

**Expected:** PASS, with all 80 rows checked and exactly the input changes you froze. **Stop:** Any other row differs, or a rack hold changes unexpectedly. **Recovery:** Keep the report and check the two source files and the original prediction; don't rewrite the delta to fit the result.

### 34. Produce the revised changed receipt on the retained changed router

Open the original changed router, not the restored one. Confirm Pending rule is still NOT_AUTHORIZED. Re-arm it, open its own Test URL, upload the same wave2-revised.csv, and Submit. Check for 80 receipt items and download `receipts/wave2-revised-changed.csv`. You don't need to edit the policy again.

![Retained changed router processes the same revised input under NOT_AUTHORIZED](figures/m07-n8n-34-revised-changed.png)

**Expected:** Both revised runs use the same revised input; only the saved policy differs. **Stop:** A source file or another setting changed. **Recovery:** Keep the run, then repeat it on the changed workflow you kept, with the unchanged revised input.

### 35. Prove the policy-only effect

Re-arm the checker. Choose `wave2-revised-baseline.csv` for baseline, `wave2-revised-changed.csv` for actual, and frozen `revised-policy-delta.csv` for delta. Select predicted-change, leave expected_sha256 empty, and Submit. Download `reports/revised-policy-delta.json`. In your observations, record the input effect and the policy effect separately, without changing either frozen prediction.

![Policy-only comparison pairs the two revised-input receipts and accounts for all rows against its own frozen delta](figures/m07-n8n-35-policy-only-proof.png)

**Expected:** PASS, with 80 rows checked, only the policy changes you predicted, and every other serialized row byte-identical. **Stop:** The comparison mixes the original input with the revised input, or returns HOLD. **Recovery:** Keep the report, and fix a mistaken file selection in a separately named run. A prediction that didn't match stays on record. Leave the restored workflow at OPEN and the changed workflow at NOT_AUTHORIZED.

</details>
