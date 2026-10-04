# Module 1 · Verify a logistics mission thread

Decide whether the Cold Lantern brief supports its `GO` recommendation. Open the sources, redo the calculations, and write your supported verdict: accept, revise, reject, or hold. The packet contains every case fact.

Plan for about three hours (a rough estimate).

The case is fictional and class-only. You are not planning or authorizing a real movement.

## Start a work folder

Set the locations of the checkout, this module, your work folder, and Python before the commands. An **absolute path** gives a file's complete location. Keep paths in quotes.

**Terminal: Bash or zsh, ordinary user.**

```bash
export R="$HOME/Documents/AIHB_OCT_2026"
export M="$R/AI_Harness_Bootcamp_2/module-01-mission-thread"
export PY="$(for candidate in python3.12 python3 python; do "$candidate" -c 'import sys; sys.exit(1) if sys.version_info < (3, 12) else print(sys.executable)' 2>/dev/null && break; done)"
[ -n "$PY" ] || echo 'HOLD: Python 3.12 or newer is required.' >&2
RUN="$(date -u +%Y%m%dT%H%M%SZ)-$$"
mkdir -p "$HOME/course-evidence" && printf '%s\n' "$RUN" > "$HOME/course-evidence/module-01-run" && printf 'RUN=%s\n' "$RUN"
export W="$HOME/course-evidence/module-01-$RUN/work"
```

**Terminal: PowerShell, ordinary user.**

```powershell
$env:R = "$HOME\Documents\AIHB_OCT_2026"
$env:M = "$env:R\AI_Harness_Bootcamp_2\module-01-mission-thread"
$env:PY = $(foreach ($candidate in 'python3.12','python3','python') { try { $resolved = & $candidate -c 'import sys; sys.exit(1) if sys.version_info < (3,12) else print(sys.executable)' 2>$null; if ($LASTEXITCODE -eq 0 -and $resolved) { $resolved.Trim(); break } } catch {} })
if (-not $env:PY) { throw 'HOLD: Python 3.12 or newer is required.' }
$RUN = [guid]::NewGuid().ToString('N')
New-Item -ItemType Directory -Force -Path "$HOME\course-evidence" | Out-Null; Set-Content -LiteralPath "$HOME\course-evidence\module-01-run" -Value $RUN; "RUN=$RUN"
$env:W = "$HOME\course-evidence\module-01-$RUN\work"
```

**Expected:** The variables expand to the absolute paths on your machine.

**Stop:** The paths are not absolute or the module directory does not exist.

**Recovery:** Set the variables from a fresh shell that can see your home and the clone; re-export before each group.

Create a fresh work folder outside the repository with the supplied starter. The command uses the absolute module path so it always finds the starter regardless of your current directory.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$M/scripts/start_work.py" "$W"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& "$env:PY" "$env:M\scripts\start_work.py" "$env:W"
```

**Expected:** PASS: created $W (or the equivalent absolute path).

**Stop:** HOLD: destination already exists.

**Recovery:** Keep the existing attempt. Choose a new `RUN` and `W`, then rerun the starter. Do not remove or overwrite an earlier attempt.


Open `desk.md`. Its links point to the files for this attempt.

### If you open a new terminal

A closed terminal forgets these variables. In a new terminal, run this block to reload them for the same attempt instead of preparing another one.

**Terminal: Bash or zsh, ordinary user.**

```bash
export R="$HOME/Documents/AIHB_OCT_2026"
export PY="$(for candidate in python3.12 python3 python; do "$candidate" -c 'import sys; sys.exit(1) if sys.version_info < (3, 12) else print(sys.executable)' 2>/dev/null && break; done)"
[ -n "$PY" ] || echo 'HOLD: Python 3.12 or newer is required.' >&2
RUN="$(cat "$HOME/course-evidence/module-01-run")"
export M="$R/AI_Harness_Bootcamp_2/module-01-mission-thread"
export W="$HOME/course-evidence/module-01-$RUN/work"
printf '%s\n' "RUN=$RUN" "W=$W"
```

**Terminal: PowerShell, ordinary user.**

```powershell
$env:R = "$HOME\Documents\AIHB_OCT_2026"
$env:PY = $(foreach ($candidate in 'python3.12','python3','python') { try { $resolved = & $candidate -c 'import sys; sys.exit(1) if sys.version_info < (3,12) else print(sys.executable)' 2>$null; if ($LASTEXITCODE -eq 0 -and $resolved) { $resolved.Trim(); break } } catch {} })
if (-not $env:PY) { throw 'HOLD: Python 3.12 or newer is required.' }
$RUN = (Get-Content -LiteralPath "$HOME\course-evidence\module-01-run" -Raw).Trim()
$env:M = "$env:R\AI_Harness_Bootcamp_2\module-01-mission-thread"
$env:W = "$HOME\course-evidence\module-01-$RUN\work"
"RUN=$RUN"; "W=$env:W"
```

**Expected:** The terminal prints `RUN=` followed by the identifier, then `W=` followed by the work folder.

**Stop:** The identifier differs from the one you recorded, or the `W=` folder does not exist.

**Recovery:** If the identifier differs, a later attempt overwrote the marker; set `RUN` to the value you recorded and run the block again. If the folder is missing, prepare it with the first block.

## Pacing

Building the thread ledger takes the longest. Hashing the inbox, freezing identity, and recomputing claims each take moderate time. Other steps are short.

## 1. Open and hash the inbox

Record the exact identity of every file. Open:

- `REQUEST.md` in the work folder
- every file under `inbox/`
- [the mission-thread guide](MISSION_THREAD.md)

![A hash identifies the bytes you used; source authority and applicability still require inspection.](figures/m01-byte-identity.png)

*A hash identifies the bytes you used; source authority and applicability still require inspection.*

<details markdown="1">
<summary>Figure text</summary>

The identity check starts with the file bytes and produces a hash that identifies those bytes. The applicability check asks whether the issuer, version and time, exact entity, and allowed use fit the claim. Byte identity and claim fit together make a traceable evidence record. A hash doesn't establish truth or authority.

</details>

Do not inspect the instructor fixture files. The reveal command copies the practice change after the baseline is frozen.

Run the content check to confirm that your checkout is intact. It uses the absolute module path, so you can run it from any folder.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$M/scripts/verify_content.py"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& "$env:PY" "$env:M\scripts\verify_content.py"
```

**Expected:** The JSON shows "state": "PASS" and source_count 9 with no errors.

**Stop:** Errors about missing file or hash mismatch.

**Recovery:** Keep the mismatch and leave the checkout unchanged. Obtain an intact copy in a fresh location, update `R` and `M`, and begin a new work folder. Do not reset or clean existing work.

Calculate a **hash**, a fingerprint of the file bytes, for each inbox file. Save the hashes in `source-register.csv`. Check that each printed filename matches the file you opened. A matching hash identifies the supplied file, but it doesn't tell you whether that file supports a claim.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$M/scripts/hash_inbox.py" "$W"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& "$env:PY" "$env:M\scripts\hash_inbox.py" "$env:W"
```

**Expected:** Nine digest-and-filename lines identify the actual inbox files.

**Stop:** HOLD: expected 9 inbox markdown files.

**Recovery:** Keep this attempt and the mismatch. Run the starter into a new work folder; do not manually add or remove inbox files.

Check the inbox itself:

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$M/scripts/check_work.py" "$W" --phase ingest
```

**Terminal: PowerShell, ordinary user.**

```powershell
& "$env:PY" "$env:M\scripts\check_work.py" "$env:W" --phase ingest
```

**Expected:** PASS: phase ingest (and the nine source hash checks).

**Stop:** FAIL on count or hash.

**Recovery:** Compare the failure with the saved source manifest. If the work copy is incomplete or altered, keep it and prepare a new folder before continuing.

## 2. Freeze exact identity and allowed source use

Open the starter's `source-register.csv` in your editor. Complete one row for every inbox file with the file's hash and the source's identity, version, authority, time, and allowed use. Then run the register check.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$M/scripts/check_work.py" "$W" --phase register
```

**Terminal: PowerShell, ordinary user.**

```powershell
& "$env:PY" "$env:M\scripts\check_work.py" "$env:W" --phase register
```

**Expected:** PASS for the register phase (nine files, hashes match, status values valid).

**Stop:** FAIL on nine inbox or hash or status.

**Recovery:** Correct the register rows against the actual inbox files and rerun.

Before checking the brief, start `baseline-verdict.md` with its heading and the identity values. Add the verdict fields in step 9.

```text
# Baseline verdict

## Identity
Mission:
Decision time:
Vehicle:
Route:
Destination:
Permit:
Cargo lot range:
Time zones present:
```

Near matches are not matches. Write the exact identifier, including revision and time zone.

## 3. Split the AI brief into material claims

Open the 14:05 AI file (name ends desk-ai-go). It is a finished `GO`. Put each decision-changing statement in its own row in `thread-ledger.csv`.

Use this header (the 8 steps and 5 statement types are required):

```csv
step,claim_id,statement_type,exact_entity,entry_condition,claim,source_id,source_version,locator,source_excerpt,warrant,calculation,output_condition,next_handoff,uncertainty,result
```

Label `statement_type` with exactly one of: SOURCE FACT, CALCULATION, INFERENCE, DECISION, UNSUPPORTED.

A compound sentence needs several rows. "All 216 kits are ready" includes a scanned count, a release state, and a decision about readiness. Give each its own support rather than using one citation for all three.

![Give each action-changing claim its own support, dependency, and uncertainty instead of letting one citation carry a compound conclusion.](figures/m01-atomic-ledger.png)

*Give each action-changing claim its own support, dependency, and uncertainty instead of letting one citation carry a compound conclusion.*

<details markdown="1">
<summary>Figure text</summary>

A compound assertion with a count claim, a state claim, and a decision claim needs three separate rows. For each row, record its source, version, and locator; statement kind; warrant; units and calculation; dependency and handoff; and uncertainty. Stop splitting when a row reaches a fact, a calculation, an assumption, a HOLD, or a human decision.

</details>

## 4. Trace all eight thread steps

Trace the cargo through every handoff. Use these step names exactly:

1. `Requirement defined`
2. `Cargo received`
3. `Cargo released`
4. `Vehicle made ready`
5. `Movement authorized`
6. `Route window met`
7. `Cargo delivered`
8. `Usable effect confirmed`

Check the exact identity, authority, and time. Check quantity and condition where they apply. Record what the step depends on, what it hands forward, and what remains uncertain.

If a row depends on an unsupported statement, add a child row. Keep splitting until you reach:

- something read directly from the applicable source;
- a deterministic calculation with supported premises and units;
- a named assumption;
- an unresolved item that causes HOLD; or
- a human DECISION.

Do not mark later events as facts. At 14:05, delivery and clinic receipt have not occurred.

## 5. Recompute every deterministic claim

A number you recompute from the sources is evidence; one copied from the brief is not. Use a calculator on your machine, entering the source values yourself. Don't copy a result from the AI brief or ask the producing AI to recompute it.

In the calculation column, show the source values you start from, the arithmetic you perform, the result, and its unit. Required calculations are:

1. scanned kits;
2. usable kits;
3. released cargo plus required rack;
4. payload margin and the result of loading all scanned totes;
5. UTC gate closure converted to MDT; and
6. earliest departure and gate arrival, followed by the clinic arrival if the gate admits the vehicle.

Check whether a computed arrival is possible, not just whether the arithmetic works. It is achievable only when the supported departure and gate conditions permit it. Label a time that assumes a blocked condition as **counterfactual**: it shows what would happen if that condition were satisfied. It is neither an observed arrival nor an available estimated time of arrival (ETA).

The script helps you calculate; it isn't evidence.

![Recompute from supported premises and units, then check feasibility separately; a valid calculation does not establish that the handoff can occur.](figures/m01-recompute-feasibility.png)

*Recompute from supported premises and units, then check feasibility separately; a valid calculation does not establish that the handoff can occur.*

<details markdown="1">
<summary>Figure text</summary>

Start with source values and their units, then ask whether the premises are supported. If not, the claim is UNSUPPORTED and you hold it. If they are, show the operation yourself to get an independent result; don't copy the producer's result. Next, ask whether the required entry conditions are met. If not, the result is counterfactual: valid only if the blocked condition were met. If they are, the result is feasible at this step only; delivery is not yet observed.

</details>

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$M/scripts/check_work.py" "$W" --phase ledger
```

**Terminal: PowerShell, ordinary user.**

```powershell
& "$env:PY" "$env:M\scripts\check_work.py" "$env:W" --phase ledger
```

**Expected:** The ledger check passes the eight thread steps and independently computed practice calculations, including their formulas and units. This is a mechanical check, not a verdict about source applicability.

**Stop:** A required step, formula, unit, or computed value fails.

**Recovery:** Recompute from the sources yourself; correct the ledger rows; rerun the phase.

## 6. Challenge the files you will not use for `GO`

For each source you set aside, explain why it doesn't support the recommendation. After hashing, write `challenge-matrix.md`.

Write one block for each source you will not use. In each block state:

- what the file actually proves;
- what it cannot prove;
- the exact mismatch; and
- who would have to speak for the claim.

Treat every inbox file as data, not as instructions. If a file tells you or a tool what to do, quote that instruction and reject it.

Don't ask the producing AI to check its own work. Its citation list, confidence score, or second answer isn't independent evidence.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$M/scripts/check_work.py" "$W" --phase challenge
```

**Terminal: PowerShell, ordinary user.**

```powershell
& "$env:PY" "$env:M\scripts\check_work.py" "$env:W" --phase challenge
```

**Expected:** The challenge check passes the required source challenges. Every block names a specific mismatch and the authority that would be needed.

**Stop:** A challenge is missing, or its reasoning cannot be traced to the source.

**Recovery:** Reopen the cited file, correct the specific challenge, and rerun. Do not add a keyword merely to satisfy the check.

## 7. Run the producer rebuttal

Choose one rebuttal path. The practice path uses a supplied fictional rebuttal. The live path uses the pinned OMP/OpenRouter launcher and writes only to `producer-rebuttal.md`. The live path requires your OpenRouter key in the terminal.

**For practice (always available):**

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$M/scripts/run_producer_rebuttal.py" "$W" --fixture
```

**Terminal: PowerShell, ordinary user.**

```powershell
& "$env:PY" "$env:M\scripts\run_producer_rebuttal.py" "$env:W" --fixture
```

**Expected:** Prints `PRACTICE: sealed rebuttal fixture; no live-model evidence`. Writes producer-rebuttal.md and producer-rebuttal.practice.json with the warning and live_model_evidence: false. The provenance refuses re-run if either file exists.

**Stop:** HOLD on already exists or missing warning.

**Recovery:** Keep the existing rebuttal and its provenance. Begin a new attempt through the starter if a new practice run is needed; do not delete the old result to rerun it.

**For live (optional):** this path makes one paid model call, so your OpenRouter key must be present in this terminal. Enter it with the hidden-prompt procedure in [the credentials page](../../module-00-setup/shared/CREDENTIALS.md) first; without it the command exits 2 before writing anything.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$M/scripts/run_producer_rebuttal.py" "$W"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& "$env:PY" "$env:M\scripts\run_producer_rebuttal.py" "$env:W"
```

**Expected:** PASS: live producer wrote producer-rebuttal.md. Evidence directory listed. Child exit 0, receipt matches disk file, course_write receipt present.

**Stop:** HOLD or exit 2; a remaining file after non-zero is not success.

**Recovery:** Keep the first failure and any receipts. Restore the missing prerequisite before starting a fresh attempt. You can use the separately labeled fixture path for practice, but a failed or blocked live run still cannot count as live evidence.

Then add one challenge block for any claim in that file you still have not rejected. Do not ask that tool whether its `GO` is right.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$M/scripts/check_work.py" "$W" --phase rebuttal
```

**Terminal: PowerShell, ordinary user.**

```powershell
& "$env:PY" "$env:M\scripts\check_work.py" "$env:W" --phase rebuttal
```

**Expected:** PASS for rebuttal (file exists, matrix names it).

**Stop:** FAIL on existence or matrix name.

**Recovery:** Complete the challenge block and rerun.

## 8. Write the corrected internal brief

Write `corrected-brief.md` with what is supported, contradicted, unresolved, later events not observed, current blockers, the exact sources and calculations behind them, and the next evidence needed.

Write it so the review page alone shows the decision and its evidence, with nothing left for you to explain in person.

![A defensible verdict names its evidence, blockers, uncertainty, and next evidence; a producer's rebuttal is not independent verification.](figures/m01-supported-verdict.png)

*A defensible verdict names its evidence, blockers, uncertainty, and next evidence; a producer's rebuttal is not independent verification.*

<details markdown="1">
<summary>Figure text</summary>

Sort each claim, including the producer's rebuttal, as supported, contradicted, or unresolved; the rebuttal is another claim to check, not proof. For each finding, point to the exact sources and calculations behind it. Use those findings to state a class-only decision of ACCEPT, REVISE, REJECT, or HOLD, along with the current blockers, the next evidence, and who can supply it. For unresolved claims, name the next evidence and who can supply it directly.

</details>

Keep this brief separate from a movement plan: do not select another route, estimate a permit decision, or claim that the clinic received cargo.

Render the local review page. The command works from any folder because it uses the absolute module path.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$M/scripts/render_review.py" "$W"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& "$env:PY" "$env:M\scripts\render_review.py" "$env:W"
```

**Expected:** The last line reads `PASS: wrote` followed by the path of `review.html` in your work folder.

**Stop:** review.html is missing or the surface omits decision-critical state.

**Recovery:** Fix the file named in the message, then run the renderer again. You can run the command from any folder because it uses the absolute module path.

Open `review.html` and check that blockers and evidence appear. The verdict remains `UNSET` until step 9.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$M/scripts/check_work.py" "$W" --phase packet
```

**Terminal: PowerShell, ordinary user.**

```powershell
& "$env:PY" "$env:M\scripts\check_work.py" "$env:W" --phase packet
```

**Expected:** PASS for the packet phase.

**Stop:** FAIL on review surface or decision target.

**Recovery:** Fix the brief, re-render, re-check.

## 9. Freeze the baseline verdict

Choose your verdict and record its identity before any source changes. Add the verdict fields below the identity block from step 2.

```markdown
# Baseline verdict

## Identity
(the eight identity lines from step 2)

## Verdict
Verdict:
Strongest supported fact:
Strongest contradiction:
Unresolved condition:
Later event not yet observed:
Decision owner:
Reason:
Standing rule:
```

After `Verdict:`, write exactly one of `ACCEPT`, `REVISE`, `REJECT`, or `HOLD`. Choose `ACCEPT` only when every material claim is supported. Choose `REVISE` when evidence supports a decision after bounded corrections. Choose `REJECT` when it contradicts the recommendation. Choose `HOLD` when required evidence, authority, access, or a decision condition is unresolved.

An unsupported material premise blocks `ACCEPT`.

Save the ledger and verdict. Record their hashes:

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" -c "from pathlib import Path; import hashlib,sys; w=Path(sys.argv[1]); [print(hashlib.sha256((w/name).read_bytes()).hexdigest(), name) for name in ('thread-ledger.csv','baseline-verdict.md')]" "$W"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& "$env:PY" -c "from pathlib import Path; import hashlib,sys; w=Path(sys.argv[1]); [print(hashlib.sha256((w/name).read_bytes()).hexdigest(), name) for name in ('thread-ledger.csv','baseline-verdict.md')]" "$env:W"
```

**Expected:** The hashes are recorded before any change is revealed.

**Stop:** Either file is missing or changes while you are recording its identity.

**Recovery:** Complete the verdict and ledger, rerun the hash commands, then proceed only after recording.

Render the review page again so it shows the verdict. Then check that the page alone answers the five questions below, without your notes or the work files.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$M/scripts/render_review.py" "$W"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& "$env:PY" "$env:M\scripts\render_review.py" "$env:W"
```

**Expected:** The last line reads `PASS: wrote` followed by the path of `review.html`, and the page now shows your verdict instead of `UNSET`.

**Stop:** The page still shows `UNSET`, or it omits a blocker you recorded.

**Recovery:** Check the `Verdict:` line holds exactly one of the four words, save the file, and render again.

1. What can proceed?
2. What cannot proceed?
3. What exact condition blocks the decision?
4. Which source and calculation establish that result?
5. What evidence would change it?

If the page can't answer one of them, fix the file that part of the page comes from, render the page again, and record the hashes again before you continue.

## 10. Predict the source-change effect

Before you see a new source, write what it should and should not change. Write `change-prediction.md` before the reveal command.

```markdown
# Source-change prediction

If a new current R-71 bulletin changes only North Gate closure to 21:20Z:

Fields that should change:
Claims that should change:
Thread-step result that should change:
Fields and claims that must not change:
Condition that would still block the overall verdict:
Unexpected change that would cause HOLD:
```

![Predict the update's reach before seeing it, change only dependent claims, and keep unrelated blockers visible.](figures/m01-change-isolation.png)

*Predict the update's reach before seeing it, change only dependent claims, and keep unrelated blockers visible.*

<details markdown="1">
<summary>Figure text</summary>

Freeze the baseline verdict. In change-prediction.md, write what should change and what must not change before you reveal the source update. Then update only the dependent claims and keep unrelated blockers visible. Recompute the verdict either way; new evidence does not produce a GO automatically.

</details>

Your prediction must exist before you reveal the change. Freeze the source register, baseline ledger, challenge matrix, corrected brief, verdict, and prediction.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$M/scripts/freeze_baseline.py" "$W"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& "$env:PY" "$env:M\scripts\freeze_baseline.py" "$env:W"
```

**Expected:** The last line reads `PASS: baseline frozen at` followed by the path of `baseline-freeze.json`, which now holds a fingerprint of each frozen file.

**Stop:** The command refuses because freeze already exists or required files are missing.

**Recovery:** Complete any missing required file before the first freeze. If a freeze already exists, keep it and start a new work attempt rather than deleting the marker.

## 11. Apply the practice change

Release the practice change only after the freeze command passes. Keep the baseline as it is, inspect the new source, and update only claims that depend on it.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$M/scripts/reveal_change.py" "$W"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& "$env:PY" "$env:M\scripts\reveal_change.py" "$env:W"
```

**Expected:** The last line reads `PASS: practice change copied to` followed by the path of `REVEALED_CHANGE.md`. `change-release.json` records that the freeze came first.

**Stop:** The command holds because freeze is missing or change was already released.

**Recovery:** Complete the freeze first, then run the reveal again.

Open `REVEALED_CHANGE.md`. Refer to it as `S10`. Keep the frozen register unchanged. Do not open the staff fixture.

Copy the baseline rows into the untouched `changed-thread-ledger.csv`. Then update only claims that depend on the current gate closure. Record revision, old value, new value, and reason.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" - "$M" "$W" <<'PY'
from pathlib import Path
import sys
m,w = map(Path,sys.argv[1:])
target = w/'changed-thread-ledger.csv'
template = (m/'shared/templates/thread-ledger.csv').read_bytes()
if target.is_symlink() or not target.is_file() or target.read_bytes()!=template:
    raise SystemExit('HOLD: changed ledger is not the untouched starter; preserve it')
target.write_bytes((w/'thread-ledger.csv').read_bytes())
print('CHANGED LEDGER SEEDED: baseline unchanged')
PY
```

**Terminal: PowerShell, ordinary user.**

```powershell
@'
from pathlib import Path
import sys
m,w = map(Path,sys.argv[1:])
target = w/'changed-thread-ledger.csv'
template = (m/'shared/templates/thread-ledger.csv').read_bytes()
if target.is_symlink() or not target.is_file() or target.read_bytes()!=template:
    raise SystemExit('HOLD: changed ledger is not the untouched starter; preserve it')
target.write_bytes((w/'thread-ledger.csv').read_bytes())
print('CHANGED LEDGER SEEDED: baseline unchanged')
'@ | & "$env:PY" - "$env:M" "$env:W"
```

**Expected:** A distinct changed ledger starts with the baseline bytes; the baseline remains unchanged.

**Stop:** The changed ledger is missing, linked, or no longer byte-identical to its untouched starter, or copying fails.

**Recovery:** Keep any changed work you already have. If you seeded this attempt, continue editing that copy instead of running the seed command again. If you cannot confirm its identity, keep the attempt and begin a new one; never overwrite an earlier changed ledger.

In your editor, update the seeded ledger and write `changed-brief.md` (do not overwrite `corrected-brief.md`). Route rows may need revised identity/version details, calculations, entry conditions, and handoffs. For other steps, keep facts, source identities, calculations, and results unchanged. If the new route premise changes a warrant or uncertainty, cite S10 or the changed route claim's ID in your explanation. Do not backdate a later source.

You may quote an old value or an inapplicable identity to explain why you rejected it, but make clear that it is not the current finding. Keep the baseline mission identities. In `changed-verdict.md`, use these additional fields and fill them from your comparison rather than assuming the overall decision must change:

```text
Verdict:
Changed source:
Changed fields, with source revision, old value, new value, and reason:
Unchanged blockers:
Later event not yet observed:
Why the overall verdict changed or stayed:
```

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$M/scripts/check_work.py" "$W" --phase change
```

**Terminal: PowerShell, ordinary user.**

```powershell
& "$env:PY" "$env:M\scripts\check_work.py" "$env:W" --phase change
```

**Expected:** The checker verifies frozen identities, the revised route citation and closure, and which fields were allowed to change. You still need to judge whether each current claim is supported: matching text cannot tell a sound explanation from a wrong one.

**Stop:** A stale value, wrong identity, unrelated change, or unsupported verdict appears in the changed work.

**Recovery:** Compare the separate baseline and changed files. Correct the changed files only where the new source supports a change; never reconstruct the baseline from a digest.

Rerun the review renderer, then run the visible work checker:

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$M/scripts/render_review.py" "$W" &&
"$PY" "$M/scripts/check_work.py" "$W"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& "$env:PY" "$env:M\scripts\render_review.py" "$env:W"
if ($LASTEXITCODE -ne 0) { throw 'Rendering held; preserve the failure.' }
& "$env:PY" "$env:M\scripts\check_work.py" "$env:W"
```

**Expected:** All seven visible practice phases pass. The checker compares both verdict lines with the practice case's known answer. If yours differs, it prints `FAIL: baseline verdict is HOLD` or `FAIL: changed verdict is HOLD`. Recheck your blockers against the sources, but do not change your judgment just to match the checker. Record a verdict you still stand behind in `handoff.md`. The checker's result doesn't replace your reading of the sources or your own judgment.

**Stop:** Stale values or unrelated change errors.

**Recovery:** Correct only the dependent parts and rerun both commands.

## 12. Finish the handoff

Write `handoff.md` so the next reader can find your verdict, evidence, and what to inspect first.

```markdown
# Module 1 handoff

Question reviewed:
Exact entities and as-of time:
Current verdict:
Eight-step thread location:
Material traced claim:
Sources of record:
Rejected sources and reasons:
Baseline-to-change delta:
Current unresolved condition:
Standing rule:
What the next person should inspect first:
```

Write it so the handoff alone is enough to reconstruct the verdict, without you there to explain it.

## Before you stop

Check that:

- all ten work files exist, along with the freeze, reveal, and review records created by the supplied scripts;
- the source manifest passes;
- the source register fixes exact identity, version, time, and allowed use;
- the ledger covers all eight thread steps;
- every material statement is labeled;
- calculations show supported premises and units;
- every inbox file you will not use to support `GO`, and the producer rebuttal, are explicitly rejected;
- the brief works in the review surface;
- the baseline ledger, prediction, and verdict predate the sealed change;
- the changed ledger contains only dependent changes and no stale route value;
- the handoff alone is enough to reconstruct the verdict; and
- the work remains inside the fictional class case.



<details class="rf-stretch" markdown="1">
<summary>Optional stretch: defend changed and unchanged claims</summary>

In `W/dependency-defense.md`, follow every material claim in the baseline and changed briefs from its source and calculation or warrant through the thread output to what depends on it downstream. Mark each claim changed or unchanged and explain why. Include delivery and authority claims even when their state remains unknown.

Choose one unchanged claim supported by a source independent of the new bulletin. Describe a counterfactual observation that would change the claim, name who could supply it, and explain why the revealed bulletin does not supply it. Do not invent that observation or add a second mission.

**Expected:** All and only supported downstream claims change. Unrelated facts retain their original support, and an unknown later event never becomes an observed fact through implication.

**Stop:** You cannot trace a change through its dependency, an unchanged claim has no support beyond habit, or you are treating the counterfactual as evidence that actually arrived.

**Recovery:** Reopen the exact source and both ledger rows. Correct the reasoning in your defense record without changing the frozen baseline files.

</details>

