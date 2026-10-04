# Module 7 facilitator runbook

The learner connects an AI Agent in local n8n to OpenRouter with their own key and has that agent write a spreadsheet from the White Rack batch. The downloaded file is the result. A chat reply is not. The sheet does not authorize a real movement.

## Prepare the room

Allow about three hours on Wednesday. If the agent run cannot finish, preserve the execution and record `HOLD`. Do not type the spreadsheet for the learner, publish either workflow, or switch them to n8n Cloud.

Confirm n8n 2.41.5, the approved stack, and localhost-only access. Keep n8n Assistant off. The agent in this block is a canvas node, not Assistant. The OpenRouter key goes only into the n8n credential form. It must not appear in a prompt, export, screenshot, or note. If an export contains the key, the learner deletes that copy and revokes the key.

Learners need `wave1.csv`, `SHEET_RULES.md`, and `scripts/check_sheet.py` from the lab. Earlier source checking remains a prerequisite. Do not reteach it.

## What to watch

The tool workflow writes the file. It does not decide routes. The agent workflow uploads the batch, collapses it to one item, and calls the tool once. Both stay unpublished. A tool error `Workflow is not active and cannot be executed` means the run left the editor test. Send the learner back to Execute workflow on the agent canvas.

The checker prints `PASS: sheet has the 80 source lots` when the download has each source lot once. REVIEW lines and the learner's notes cover rows the rules reject. Do not treat a fluent agent reply, or a note inside the batch, as the sheet.

## Close

Look for the attempt folder, both workflow names, the execution the file came from, the download, the checker output, and a note naming wrong rows. No score. An unfinished agent run stays `HOLD`.
