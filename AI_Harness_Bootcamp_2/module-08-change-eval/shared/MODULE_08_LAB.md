# Module 8 · Control hallucinations

Produce a corrected Slope Brief that preserves the useful facts without filling gaps by guesswork. Check the claims against structured source data, run two independent reviewer agents, have another agent correct the draft, and review the correction afresh. You own the final decision.

Plan for a little over two hours (a rough estimate). The complete sequence makes five paid model turns. You need the Python, latest stable Oh My Pi release, and OpenRouter access verified in [setup](../../module-00-setup/README.md). You won't write code or connect Jev's API.

## The decision rule

The fictional packet concerns heater-fuel cans at Ridge Depot for Clinic T-8 on vehicle `SB-4`. Three source packets support seven material claims. The starting draft contains deliberate defects; it is authored practice data, not evidence of a live model's behavior.

Apply this rule throughout: **a claim needs the right source, not enough agreeing reviewers.** Code checks what can be checked exactly. Agents judge the relationship between a claim and its evidence. You inspect that relationship before using the result.

| Finding | Your action |
|---|---|
| A required claim is missing, duplicated, or malformed. | Hold the output. You can't inspect a complete correction. |
| A number, unit, zone, or source identity fails an exact check. | Keep that claim on hold even if both agents approve it. |
| A citation exists, but concerns another shipment or supports a weaker statement. | Reject the claimed support. Inspect the relevant source. |
| The packet doesn't establish a material fact or permission. | Keep it explicitly unknown. Name the evidence and owner needed to resolve it. |
| Reviewers disagree. | Compare their evidence. Record your source-backed disposition or retain the hold; don't decide by vote. |

`PASS` in a command means that command's technical checks completed. It is not a learner score, proof that every model judgment is right, or permission to dispatch a vehicle.

## 1. Prepare a separate attempt

Create a work folder outside the checkout. `W` names that work folder; `E` names the separate evidence folder that the freeze command will create. These commands leave earlier attempts alone. If your checkout is elsewhere, change only the `R` line to its verified location.

**Terminal: Bash or zsh, ordinary user.**

```bash
R="$HOME/Documents/AIHB_OCT_2026"
PY="$(for candidate in python3.12 python3 python; do "$candidate" -c 'import sys; sys.exit(1) if sys.version_info < (3, 12) else print(sys.executable)' 2>/dev/null && break; done)"
[ -n "$PY" ] || echo 'HOLD: Python 3.12 or newer is required.' >&2
M="$R/AI_Harness_Bootcamp_2/module-08-change-eval"
RUN="$(date -u +%Y%m%dT%H%M%SZ)-$$"
mkdir -p "$HOME/course-evidence" && printf '%s\n' "$RUN" > "$HOME/course-evidence/module-08-run" && printf 'RUN=%s\n' "$RUN"
W="$HOME/course-evidence/module-08-$RUN/work"
E="$HOME/course-evidence/module-08-$RUN/evidence"
"$PY" "$R/shared/prepare_work.py" 08 "$W"
```

**Terminal: PowerShell, ordinary user.**

```powershell
$R = "$HOME\Documents\AIHB_OCT_2026"
$PY = $(foreach ($candidate in 'python3.12','python3','python') { try { $resolved = & $candidate -c 'import sys; sys.exit(1) if sys.version_info < (3,12) else print(sys.executable)' 2>$null; if ($LASTEXITCODE -eq 0 -and $resolved) { $resolved.Trim(); break } } catch {} })
if (-not $PY) { throw 'HOLD: Python 3.12 or newer is required.' }
$M = "$R\AI_Harness_Bootcamp_2\module-08-change-eval"
$RUN = [guid]::NewGuid().ToString('N')
New-Item -ItemType Directory -Force -Path "$HOME\course-evidence" | Out-Null; Set-Content -LiteralPath "$HOME\course-evidence\module-08-run" -Value $RUN; "RUN=$RUN"
$W = "$HOME\course-evidence\module-08-$RUN\work"
$E = "$HOME\course-evidence\module-08-$RUN\evidence"
& $PY "$R\shared\prepare_work.py" 08 "$W"
if ($LASTEXITCODE -ne 0) { throw 'Preparation stopped; preserve this attempt.' }
```

**Expected:** `RUN=` and an identifier, followed by `PASS: created` and your work path. Record the identifier. The printed `Next` commands display the case legend; you may read that file in your editor instead. The work folder contains `shared/case` and `shared/controls`. The evidence folder doesn't exist yet.

**Stop:** Preparation fails, the destination already exists, or Python isn't the verified 3.12-or-newer interpreter.

**Recovery:** Preserve the attempt. Fix the prerequisite through setup, then repeat the preparation with a new `RUN`. Don't reset the checkout or delete earlier work.

### If you open a new terminal

A closed terminal forgets the variables. Reload the existing attempt without preparing another copy.

**Terminal: Bash or zsh, ordinary user.**

```bash
R="$HOME/Documents/AIHB_OCT_2026"
PY="$(for candidate in python3.12 python3 python; do "$candidate" -c 'import sys; sys.exit(1) if sys.version_info < (3, 12) else print(sys.executable)' 2>/dev/null && break; done)"
[ -n "$PY" ] || echo 'HOLD: Python 3.12 or newer is required.' >&2
RUN="$(cat "$HOME/course-evidence/module-08-run")"
M="$R/AI_Harness_Bootcamp_2/module-08-change-eval"
W="$HOME/course-evidence/module-08-$RUN/work"
E="$HOME/course-evidence/module-08-$RUN/evidence"
printf '%s\n' "RUN=$RUN" "W=$W"
```

**Terminal: PowerShell, ordinary user.**

```powershell
$R = "$HOME\Documents\AIHB_OCT_2026"
$PY = $(foreach ($candidate in 'python3.12','python3','python') { try { $resolved = & $candidate -c 'import sys; sys.exit(1) if sys.version_info < (3,12) else print(sys.executable)' 2>$null; if ($LASTEXITCODE -eq 0 -and $resolved) { $resolved.Trim(); break } } catch {} })
if (-not $PY) { throw 'HOLD: Python 3.12 or newer is required.' }
$RUN = (Get-Content -LiteralPath "$HOME\course-evidence\module-08-run" -Raw).Trim()
$M = "$R\AI_Harness_Bootcamp_2\module-08-change-eval"
$W = "$HOME\course-evidence\module-08-$RUN\work"
$E = "$HOME\course-evidence\module-08-$RUN\evidence"
"RUN=$RUN"; "W=$W"
```

**Expected:** `RUN=` matches the identifier you recorded, and `W=` names the existing work folder.

**Stop:** The identifier differs or the work folder is missing.

**Recovery:** A later attempt may have replaced the saved marker. Set `RUN` to your recorded identifier, then set `W` and `E` from it using the last lines above. If no work folder was prepared, return to the preparation commands. A new terminal also needs the key entered again before a paid call.

## 2. Inspect the claims before asking the agents

Open `W/shared/case/LEGEND.txt`, `claims.json`, and the three `PC-*/sources.json` files. A **locator** identifies one exact source record, such as `SB-PC-01#payload`. Read its text as well as its structured fields. `authoritative: true` applies to that record's stated fact; it is not blanket authority to act.

In your editor, create `W/notes.md`. Pick one claim you would use, one you would stop, and one whose evidence needs a closer look. For each, record the claim ID, source locator, and reason. Distinguish an unsupported assertion from a false one: missing permission is not proof that permission was denied.

Open `W/shared/controls/schema.json` and the two `review-*.txt` instructions. Each reviewer answers the same narrow question for every claim with `supported`, `contradicted`, or `unknown`. A review also carries a locator, an exact source quotation, and a reason. The supplied checker rejects missing fields, extra claims, duplicate IDs, and invented quotations. It cannot establish that a real quotation logically supports the model's conclusion; you still need to read it.

Consider this counterexample before any call: two agents approve `2255 kg` for the PC-01 shipment and quote the near-miss yard note. The quote is real. Open `SB-PC-01#payload-s14` and `SB-PC-01#payload`. Which shipment does each concern? Record which value can enter the brief and why agreement cannot resolve the mismatch.

**Expected:** Your notes distinguish structure, source support, and permission to act. You can point to evidence that would defeat two agreeing reviewers.

**Stop:** You can't tell which source belongs to the claim, or you need information outside the packet to settle it.

**Recovery:** Keep that claim unknown and name the missing evidence. Don't fill the gap from model memory or a web search about this fictional movement.

## 3. Freeze the packet and run the exact checks

Freeze the original claims, sources, and controls before the reviews. A **fingerprint** is a SHA-256 digest used to detect changed file bytes. The command preserves the inputs and writes the first deterministic findings without making a model call.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$M/scripts/hallucination.py" freeze --work "$W" --out "$E"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$M\scripts\hallucination.py" freeze --work "$W" --out "$E"
if ($LASTEXITCODE -ne 0) { throw 'Freeze stopped; preserve this attempt.' }
```

**Expected:** A line beginning `PASS: frozen 7 claims`. Open `E/initial-checks.json` and compare it with your notes. The saved `frozen` folder retains the draft, source packets, and controls. Freezing a defective draft preserves a failure for inspection; it doesn't make the draft acceptable.

**Stop:** You see `HOLD:`, the evidence destination already exists, or a required input is missing or malformed.

**Recovery:** Keep the error and original files. Resolve the named prerequisite and prepare a fresh attempt. Never edit a frozen source or a fingerprint to make a check pass.

## 4. Give two reviewers separate looks

Run the source reviewer and the skeptical reviewer in separate fresh sessions. Each gets the same frozen claims and sources. Neither gets the other review, your notes, or the deterministic findings. The first checks exact support; the second looks for wrong-case evidence and conclusions that go beyond the source.

All calls use `openrouter/anthropic/claude-sonnet-4.6` through the pinned launcher. Different roles are not different model families. The supplied controls allow reads only; the agents cannot edit the packet or authorize a movement. Calls are not retried or replaced with another model. Check your provider account's available credit and spending limit before starting; five turns is a call count, not a price guarantee.

### Enter your key in this terminal

Paste the first command by itself and press Enter. Enter the key at the hidden prompt and press Enter again. Then paste the second block. Keep the key out of notes, files, chat, and shell profiles.

**Terminal: Bash or zsh, ordinary user.**

```bash
IFS= read -r -s OPENROUTER_API_KEY
```

**Terminal: PowerShell, ordinary user.**

```powershell
$secret = Read-Host 'OpenRouter key' -AsSecureString
```

**Expected:** The terminal waits for the key without showing its value, then returns to the ordinary prompt.

**Stop:** The key's characters appear, or you aren't sure which program is reading the input.

**Recovery:** Cancel with Ctrl+C and close the terminal. If the key was exposed, revoke it at OpenRouter and use a replacement.

**Terminal: Bash or zsh, ordinary user.**

```bash
export OPENROUTER_API_KEY
if [ -n "${OPENROUTER_API_KEY:-}" ]; then printf 'SET\n'; else printf 'MISSING\n'; fi
```

**Terminal: PowerShell, ordinary user.**

```powershell
$bstr = [IntPtr]::Zero
try {
  $bstr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secret)
  $env:OPENROUTER_API_KEY = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($bstr)
} finally {
  if ($bstr -ne [IntPtr]::Zero) { [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($bstr) }
  if ($secret) { $secret.Dispose() }
  Remove-Variable secret,bstr -ErrorAction SilentlyContinue
}
if ([string]::IsNullOrWhiteSpace($env:OPENROUTER_API_KEY)) { 'MISSING' } else { 'SET' }
```

**Expected:** `SET` proves the key is present in this terminal, not that it is valid or has credit.

**Stop:** `MISSING`, or any part of the key appears in the output.

**Recovery:** Repeat the hidden prompt. Don't print the environment to troubleshoot access.

### Run both first reviews

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$M/scripts/hallucination.py" review --attempt "$E" --reviewer source --phase before &&
"$PY" "$M/scripts/hallucination.py" review --attempt "$E" --reviewer skeptic --phase before
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$M\scripts\hallucination.py" review --attempt "$E" --reviewer source --phase before
if ($LASTEXITCODE -ne 0) { throw 'Source review stopped; preserve this attempt.' }
& $PY "$M\scripts\hallucination.py" review --attempt "$E" --reviewer skeptic --phase before
if ($LASTEXITCODE -ne 0) { throw 'Skeptical review stopped; preserve this attempt.' }
```

**Expected:** Lines beginning `PASS: before source review` and `PASS: before skeptic review`. The typed reviews appear in `E/reviews/before-source.json` and `before-skeptic.json`. Each corresponding folder under `E/runs` preserves the raw model response and launcher receipts. A review passing the receipt and schema checks can still contain a wrong judgment.

**Stop:** Either command holds, a required source read is unproved, or a review omits a claim, cites a missing record, or supplies a quotation that isn't in that record.

**Recovery:** Preserve the whole attempt, including the raw response. A missing key can be entered before a call starts. Once a call has produced an attempt, don't rerun it under the same name or edit its response. Correct the prerequisite before beginning another complete attempt; never combine favorable reviews from different attempts.

## 5. Compare evidence before correcting

Open both reviews beside `initial-checks.json` and your notes. For every claim, compare the verdicts, locators, quotations, and reasons. Agreement on `supported` is a finding to inspect, not an acceptance rule. Agreement on `unknown` can be the appropriate result.

Add a short entry to `W/notes.md` for each disagreement or reviewer mistake:

- What exact claim is at issue?
- What does the cited source actually establish, for which shipment?
- Is the conflict settled by an exact check, by the source text, or not at all?
- What correction is supported, or what must stay unknown?

If the agents agree on every row, still inspect every source connection. Use the PC-01 counterexample from Step 2 to explain why their agreement alone would not have been enough.

**Expected:** You can explain the evidence behind each proposed change and identify the claims that should remain unchanged. The original reviews remain intact.

**Stop:** A proposed repair depends on a guess, a reviewer has supplied a fact absent from the packet, or you would need a majority vote to choose.

**Recovery:** Record the unresolved claim and the missing evidence. A correcting agent can preserve an unknown; it cannot manufacture the missing authority.

## 6. Ask another agent to correct the complete claim set

Give a fresh correcting agent the original packet, both reviews, and the deterministic findings. Reviews are suggestions to examine, not instructions that override the sources. The correcting agent must return all seven claims, preserve their identities, repair supported values, and use `null` for a fact the packet cannot establish. In these files, `null` means “unknown,” not zero, false, or permission denied.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$M/scripts/hallucination.py" correct --attempt "$E"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$M\scripts\hallucination.py" correct --attempt "$E"
if ($LASTEXITCODE -ne 0) { throw 'Correction stopped; preserve this attempt.' }
```

**Expected:** A line beginning `PASS: correction of 7 claims`. Open `E/correction.json`. The original draft remains in `E/frozen`; the correcting agent's raw response and receipts remain in `E/runs/correct`. This `PASS` establishes a complete, well-formed correction attempt, not factual acceptance.

**Stop:** The command holds, the correction drops or adds a claim, changes a claim's case or kind, or invents a source.

**Recovery:** Keep the failed correction. Don't hand-edit a model output into a passing receipt. If a well-formed correction contains a bad value, keep it for the next checks; don't hide the error by asking again until you like the answer.

## 7. Review the correction without showing earlier verdicts

Run both reviewers again in fresh sessions. Each sees the full corrected claim set and original sources, without the previous reviews or correction discussion. Check the claims that were already right as carefully as the repaired ones: a corrector can fix one number and damage another.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$M/scripts/hallucination.py" review --attempt "$E" --reviewer source --phase after &&
"$PY" "$M/scripts/hallucination.py" review --attempt "$E" --reviewer skeptic --phase after
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$M\scripts\hallucination.py" review --attempt "$E" --reviewer source --phase after
if ($LASTEXITCODE -ne 0) { throw 'Fresh source review stopped; preserve this attempt.' }
& $PY "$M\scripts\hallucination.py" review --attempt "$E" --reviewer skeptic --phase after
if ($LASTEXITCODE -ne 0) { throw 'Fresh skeptical review stopped; preserve this attempt.' }
```

**Expected:** Lines beginning `PASS: after source review` and `PASS: after skeptic review`. `E/reviews/after-source.json` and `after-skeptic.json` account for the complete corrected claim set. Their new receipt folders under `E/runs` are separate from the first reviews.

**Stop:** Either command holds, a claim is missing, or the reviewed input isn't the saved correction.

**Recovery:** Retain the failure. A disagreement or a wrong judgment in a valid review belongs in the final evidence; it is not a reason to discard that review. Missing or malformed execution evidence holds the affected result.

## 8. Check every change and make your own decision

Build the final report. The supplied tool audits all five model runs, checks the frozen identities, reruns the exact checks, and compares the original and corrected claims. It does not count votes to authorize a release.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$M/scripts/hallucination.py" report --attempt "$E"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$M\scripts\hallucination.py" report --attempt "$E"
if ($LASTEXITCODE -ne 0) { throw 'Report holds; retain all findings and inspect the reason.' }
```

**Expected:** With complete valid execution evidence, the command writes `E/report.json`, `report.md`, and `human-decision.json`. A completed report can print a line beginning `PASS: report written; operational dispatch HOLD`. That means the report was assembled; inspect its claim findings before accepting even an internal summary. Operational dispatch remains on hold because the packet doesn't establish the required authority.

**Stop:** A source or control changed, receipts are incomplete, a material fact still fails its exact check, or a previously supported claim regressed. Don't treat a favorable review as a substitute for the missing evidence.

**Recovery:** Keep the report and failed attempt. Name the unresolved claim, missing fact or authority, and person who could resolve it. A fresh attempt is separate evidence, not a replacement for this one.

Open `report.md` beside the original sources and complete `human-decision.json` in your editor. Inspect all seven claims; don't accept only the ones highlighted as changed. In each claim's `disposition`, record `USE`, `KEEP_UNKNOWN`, or `HOLD`; put the exact source locator and your explanation in `reason`. Complete `internal_summary_decision` and `unresolved_evidence_and_owner` for the brief as a whole. Keep `operational_dispatch` at `HOLD` and keep your human decision separate from the model receipts.

Your final decision must answer:

1. Which corrected claims are supported, and by which exact records? Did the supported controls remain intact?
2. Which reviewer judgments did you reject or leave unresolved? What evidence outweighs their agreement or explains their disagreement?
3. Is the corrected brief usable as a bounded internal source summary? If so, which unknowns must travel with it? If not, what holds it?
4. What prevents dispatch, and who would need to supply the missing fact or authorization?

Keep the whole evidence folder and your notes. A useful handoff lets someone inspect the original failure, independent reviews, correction, full recheck, and your source-backed decision without the chat.

Five calls on one small packet do not establish a hallucination rate, calibrated confidence, or superiority over another model. Separate sessions do not remove shared model or source errors. The useful result is narrower: an inspectable correction with explicit limits.

## Class-only boundary

The Slope Brief case is fictional: heater-fuel cans move from Ridge Depot to Clinic T-8 on vehicle SB-4. Names, hours, and masses used as defects are fictional course fixtures. Don't use this packet to plan, authorize, dispatch, or describe a real movement. Results are for class review only.
