# Module 6 · Use Jev inside Oh My Pi

You put four decision-model patterns to work inside the native Oh My Pi harness on the Blue Gauge airlift desk. You tell the harness what to change through ordinary prompts, run the native operations, inspect the actual calls and routes, change one setting, and compare the observed effect. All work stays inside the OMP TUI. Plan for about three hours.

## Blue Gauge: the last resupply flight

It is 05:00 UTC+02 on 15 October 2026 at Aster Airhead. Flight BG-F17 is planned to Forward Support Base Kestrel. The cargo list closes at 05:30 and the aircraft departs at 06:00. The next flight is **not supplied**. The desk handles messages about generator spares, medical-equipment battery kits, and water-system repair parts.

Read the [desk rules](case/DESK_RULES.md). Stock release and exact-flight acceptance are separate records. `PASS` sends a message to ordinary desk processing. `RETURN` asks for source correction. `REVIEW` brings the message to the duty logistics officer. The cargo release officer owns stock release. The air movement controller owns acceptance for this flight and dispatch. The duty logistics officer owns the review queue and handoff.

The eighty messages and sixteen requests are fictional. Their text goes through OpenRouter to Jev for typed judgments; the OMP chat model remains conversational. Keep real operational and personal data out of the case. A message, model answer, confidence value, priority score, or handler result cannot release stock, accept cargo for BG-F17, or dispatch the aircraft.

## Start Oh My Pi

Start from the Python and OMP installation checked in [setup](../../module-00-setup/README.md). The launcher prepares a fresh work folder outside the checkout and opens the interactive OMP TUI. If no OpenRouter key is available, the terminal requests it without echo. The launcher never writes the key to a file or transcript.

**Terminal: Bash or zsh, ordinary user.**

```bash
cd "$HOME/Documents/AIHB_OCT_2026/AI_Harness_Bootcamp_2/module-06-decision-model"
python3 scripts/blue_gauge.py start
```

**Terminal: PowerShell, ordinary user.**

```powershell
Set-Location "$HOME\Documents\AIHB_OCT_2026\AI_Harness_Bootcamp_2\module-06-decision-model"
python scripts/blue_gauge.py start
```

**Expected:** The terminal prints the work folder, the evidence folder, the actual OMP version, the conversational model pin, and the judge pin. Then the native OMP TUI opens. Inside OMP the only active tools are `blue_gauge` and `eval`.

**Stop:** Stop if the command prints `HOLD`, if OMP is not the verified classroom version, or if the key prompt appears in a noninteractive context.

**Recovery:** Return to setup if Python or OMP is missing or the interpreter is older than Python 3.12. To continue an existing attempt, use `resume` and select its exact attempt and native session IDs.

To resume an existing attempt:

**Terminal: Bash or zsh, ordinary user.**

```bash
cd "$HOME/Documents/AIHB_OCT_2026/AI_Harness_Bootcamp_2/module-06-decision-model"
python3 scripts/blue_gauge.py resume
```

**Terminal: PowerShell, ordinary user.**

```powershell
Set-Location "$HOME\Documents\AIHB_OCT_2026\AI_Harness_Bootcamp_2\module-06-decision-model"
python scripts/blue_gauge.py resume
```

**Expected:** The terminal lists existing attempts and requests an exact attempt ID, then an exact saved native session ID. The selected work opens with the same model pins and saved results; resume starts no paid operation.

**Stop:** Stop if either ID is unknown or the runtime or protected controls changed.

**Recovery:** Keep the existing evidence. Select the IDs printed for that attempt; never guess a global latest run or prepare over an existing folder.

Inside the OMP session the conversational model is `openrouter/anthropic/claude-sonnet-4.6`. The native judge is `openrouter/typesafe/jev-1.13`. Both use the same OpenRouter key. Jev returns typed answers and probabilities; it does not write conversational prose.


Ask OMP to inspect controls, sources, and saved runs through `blue_gauge`. For each pattern, inspect the controls, configure one setting, run the helper-issued operation, and source-check one actual item. OMP runs the exact issued `eval` cell once per prepared operation; you do not write executable code. A replay uses saved answers: zero additional Jev requests and zero handler executions. The conversational model can still incur chat usage while explaining a replay.

## 1. Ask once, then use what matters

Speculative fan-out asks several questions about the same state in one model request. Some answers may not be needed for the route. You see which ones the router actually used.

**In OMP:**

```text
Screen the 20 practice messages for the Blue Gauge airlift desk. Ask a Jev follow-up question only when the desk needs it. Show the questions asked, message routes, elapsed time, and reported cost. Keep the cargo sources unchanged.
```

The serial run shows a waterfall of the dependent calls that actually ran. After the change below, the comparison adds one six-question block per eligible message, with used and ignored answer tiles and the observed route agreement.

**In OMP:**

```text
Now ask all six questions together for each message. Use the same messages and question wording. Compare the timelines, cost, and routes. Highlight answers the desk ignored, and explain why an ignored answer cannot change the route.
```

**Source and behavior check:** Use `inspect` on `BG-006` (instruction branch) and `BG-004` (supported records). Confirm that a high-probability answer the router did not use cannot change the route. Confirm source-settled identity cases made no Jev call.

**Expected:** Two cold runs with the same twenty messages and question definitions. The fan-out arm contains six questions in each eligible request. Ignored answers are marked. Preserve any route disagreement; a lower request count does not prove better answers.

**Stop:** Stop if the prepare step is refused, if the eval cell is altered, or if a second paid operation is attempted on the same plan.

**Recovery:** Ask OMP to inspect the active revision and saved failure. Do not repeat a consumed cell or automatically start a new paid operation.

## 2. Make uncertain notes wait

Confidence-gated routing sends a message to review when the model's confidence on the selected answer falls below a gate. You compare gates on the same saved answers without new Jev calls.

**In OMP:**

```text
Use the saved Jev answers to compare confidence gates of 0.4, 0.6, and 0.8 for messages entering the normal desk queue. Keep the return-confidence gate at 0.4. Show review load and automatic routes that disagree with the practice labels. Don't call Jev again.
```

The native panel shows one dot per judged message on a 0–1 ruler with the chosen gate marked. Separate lanes for `PASS`, `RETURN`, and `REVIEW`. Symbols distinguish label agreement. Code-settled messages sit outside the ruler and say "confidence not used". Stock release and current BG-F17 acceptance appear as separate source fields.

**In OMP:**

Choose the pass-confidence gate from the practice comparisons; it must be stricter than the return-confidence gate. State your choice in OMP before freezing. For example:

```text
Keep pass confidence at 0.8 and return confidence at 0.4, with a review ceiling of 40%. Freeze these settings, questions, sources and build. Check the 60 unseen messages once. Show actual errors and review load. Keep a completed HOLD; do not retune or repeat the unseen measurement.
```

**Source and behavior check:** Inspect `BG-008`. Confirm that high model confidence on a release claim does not create a missing flight acceptance. Confirm the frozen settings, questions, mission clock, stock records, and flight records are recorded before the unseen run.

**Expected:** Three replay comparisons with zero additional Jev requests. One frozen unseen run of the 60 notes. Code-only rows remain explicit. A `HOLD` from review share or a critical miss is valid evidence; do not retune on unseen labels.

**Stop:** Stop if a replay is misdescribed as new Jev work, if the freeze is attempted after the unseen run, or if unseen labels are read before the frozen measurement completes.

**Recovery:** Use `replay` on the prior run ID with the new revision. Use `verify` to confirm the freeze preceded the measurement. Keep the incomplete or held result.

## 3. Change priorities without asking Jev again

Composite scoring combines normalized scores from separate dimensions with weights you control. Changing the weights re-ranks attention using the same saved answers.

**In OMP:**

```text
Score all 80 Blue Gauge messages for urgency, stated mission impact and handoff risk. Rank desk attention at weights 50%, 30%, 20%, showing contributions. Reuse compatible saved urgency answers. Compare 20%, 60%, 20% using the same answers without another Jev call. Inspect BG-012 beside BG-014. This is not cargo allocation or clearance.
```

Code divides each score by its maximum level: urgency by 2, mission impact by 3, and handoff risk by 4. It sums the weighted contributions. The native panel shows the top ten, labeled contribution bars, and before/after rank slopes. Ask OMP to inspect the saved raw dimensions, confidences and source records; all eighty IDs remain available.

**In OMP:**

Choose a third nonnegative weight set totaling 100%, and predict a message that will move. State both choices yourself. For example:

```text
Use weights 10% urgency, 20% mission impact and 70% handoff risk. I predict BG-006 will move up. Replay the saved scores without another Jev call. Compare its actual rank and contributions with the first policy, even if my prediction is wrong.
```

**Source and behavior check:** Inspect `BG-012` (urgent spare-charger) beside `BG-014` (shared generator). Confirm that the observed scores produce the recorded rank order or reversal. Confirm zero new Jev requests on the replay. Confirm source stock and flight facts are unchanged.

**Expected:** All 80 messages receive urgency, mission-impact, and handoff-risk scores. Missing dimensions are `UNSCORED`. Two weight policies compared by replay only. A learner-chosen third set also by replay. The priority is always labeled provisional desk attention.

**Stop:** Stop if a replay makes new Jev calls, if weights are negative or do not sum to 1, or if a high rank is treated as authority. A zero weight for one dimension is valid.

**Recovery:** Use `replay` with the prior run and the new revision. Inspect the raw scores and the arithmetic in the panel. Report the actual movement observed.

## 4. Use the right kind of help

Intent routing uses Jev's typed intent and complexity answers to select real work. A **handler** is supplied code that carries out the selected task: look up one record, compare records, or save an item for the duty officer. Record comparison selects applicable records for the exact cargo, BG-F17 and snapshot time; it is not an assistant explanation, clearance, or human approval.

Judge the work being requested, not how serious the cargo's status sounds. Comparing available records can be bounded work; deciding whether to waive a missing approval is officer work. Drafts, approvals, uncertain requests, and missing or multiple identities go to the officer.

**In OMP:**

```text
Use Jev to classify all 16 Blue Gauge requests. Route status lookups to record lookup, record questions to deterministic comparison, and drafts, approvals, or uncertain requests to my officer queue. Execute the routed handlers and show what actually ran. Inspect a result against its source records.
```

The native panel traces `Jev → selected handler → actual result` for `record_lookup`, `record_comparison`, and `human_review`. A path labeled `HANDLER NOT RUN` is not execution. Inspect the typed choices, gate decisions, saved results, and source references. OMP can explain those results, but its prose is not an execution receipt.

**In OMP:**

```text
Raise the intent-confidence gate to 0.9. Preview which requests would now come to me using saved Jev answers. Do not execute handlers or create queue entries. Compare this preview with the original executed paths.
```

**Source and behavior check:** Inspect `BGR-001`'s lookup result, the selected handlers for `BGR-005` and `BGR-006`, and an authorization request's officer queue entry. Check any executed comparison against the exact-flight records. If a comparison was deferred, inspect its intent confidence, complexity score, and complexity confidence against their separate gates. For `BGR-005`, stock is `RELEASED` while flight acceptance is `PENDING`; for `BGR-006`, a newer BG-F71 record does not supersede the applicable BG-F17 record. Neither a comparison nor a queue entry approves cargo. A replay must say "preview — handlers not executed".

**Expected:** The routed run classifies all sixteen requests and records actual lookup, comparison, and human-review execution where the saved choices and safety gates permit. Each executed handler saves its result; an officer queue item is not approval. A stricter-gate replay changes only the route preview, with zero Jev requests and zero handler executions. Main chat usage remains distinct from Jev usage.

**Stop:** Stop if a replay executes a handler, if an authorization request is sent to a non-human handler, or if source facts are altered.

**Recovery:** Keep failed or incomplete judgment and handler records. Never call a queue entry approval or invent missing cost or served identity. Request a new paid operation only explicitly; a preview must not dispatch it.

## 5. Inspect and hand off

Request a final review packet through OMP. It must contain:

- A four-row pattern comparison: configuration change, observed effect, limitation, actual run ID.
- One concrete inspected cargo or message example per pattern with its source references.
- Leading unresolved messages with their source facts and the human owner who must act.

**In OMP:**

```text
Prepare the airlift-desk handoff. Include four pattern rows: change, observed effect, limitation and run ID. Name one inspected cargo or message per pattern with source references. List leading unresolved messages, source facts and human owners. Use the verifier's actual counts and HOLD reasons. Label it "review packet — not a manifest or movement order".
```

**Source and behavior check:** Every row cites a real run ID and a real cargo or message ID that appears in the saved evidence. No row claims cargo clearance, flight acceptance, or dispatch.

**Expected:** The verifier supplies the counts. You supply the attention-policy explanation. The packet names concrete owners for the remaining work. Previous results remain byte-identical after resume and replay.

**Stop:** Stop if the packet is labeled a manifest or movement order, if a replay is claimed to have executed new work, or if held-out answers appear before the frozen measurement completes.

**Recovery:** Use `show` and `inspect` on the saved runs to pull the exact numbers and IDs. Correct the packet and request a fresh view.

