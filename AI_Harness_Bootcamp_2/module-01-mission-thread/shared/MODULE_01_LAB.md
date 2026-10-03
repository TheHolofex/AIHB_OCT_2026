# Module 1 · Verify a logistics mission thread

Decide whether the polished Cold Lantern brief supports its `GO` recommendation. Open the applicable sources, redo the calculations, and write your own supported verdict: accept, revise, reject, or hold for internal class review. Use the bounded direction and source checks you already know to see whether the claims hold together across the movement. The supplied packet contains every case fact you need.

Plan for about three hours. That is a rough estimate, not a measured time.

The case is fictional. Your work stays inside the class. You are not planning or authorizing a real movement.

## Start a work folder

Before running the commands, set the locations of the course checkout, this module, your new work folder, and Python. An **absolute path** gives a file's complete location, regardless of your current folder. Keep the paths in quotes so spaces in folder names don't split them.

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

Open `desk.md` in the new work folder. Its links point to the working files for this attempt.

The visible checker catches missing fields, known practice values, arithmetic, and stale values. It does not judge whether a source applies or whether the verdict is sound.

### If you open a new terminal

The commands on this page use the variables you set above, but a terminal forgets them when it closes. In a new terminal, run this block to return to the same attempt without preparing another one. It reads the attempt identifier saved by the first block.

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

**Expected:** The terminal prints `RUN=` followed by the identifier you saw when you prepared this attempt, then `W=` followed by the existing work folder.

**Stop:** The identifier differs from the one you recorded, or the folder named after `W=` does not exist.

**Recovery:** If the identifier differs, a later attempt overwrote the saved marker; set `RUN` by hand to the value you recorded and run the block again. If the folder is missing, the attempt was never prepared; prepare it with the first block.

## Pacing

Most of the session is your own inspection, calculation, writing, and decision. Building the thread ledger takes the longest. Opening and hashing the inbox, freezing identity and source use, and recomputing the calculated claims take a moderate amount of time each. The other steps are short.

## 1. Open and hash the inbox

Record the exact identity of every file you judge. That way, if someone later swaps a source, the change will show. Open:

- `REQUEST.md` in the work folder
- every file under `inbox/`
- [the mission-thread guide](MISSION_THREAD.md)

![A hash identifies the bytes you used; source authority and applicability still require inspection.](figures/m01-byte-identity.png)

*A hash identifies the bytes you used; source authority and applicability still require inspection.*

<details markdown="1">
<summary>Figure text</summary>

The identity check starts with the file bytes and produces a hash that identifies those bytes. The applicability check asks whether the issuer, version and time, exact entity, and allowed use fit the claim. Byte identity and claim fit together make a traceable evidence record. A hash doesn't establish truth or authority.

</details>

Do not inspect your instructor's fixture files. The supplied reveal command will copy the practice change into your work folder after the baseline is frozen.

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

Then calculate a **hash**, a fingerprint of the file bytes, for each work-inbox file. Save the hashes in `source-register.csv`, and check that each printed filename matches the file you opened. A matching hash identifies the supplied file, but it doesn't tell you whether that file supports a claim.

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

Before using any source, record what it is, how current it is, and what it may be used for. Open the starter's `source-register.csv` in your editor. Complete one row for every inbox file with the file's hash and the source's identity, version, authority, time, and allowed use. Then run the register check.

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

Before checking the brief sentence by sentence, start `baseline-verdict.md` with its heading and the identity values. Add the verdict fields below them in step 9.

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

Near matches are not matches. Write the exact identifier you read, including revision and time zone.

## 3. Split the AI brief into material claims

To test the polished recommendation, take its decision-changing claims one at a time. Open the 14:05 AI file in the inbox, the one whose name ends desk-ai-go. It is a finished `GO` that you did not write. Put each statement that could change the decision in its own row in `thread-ledger.csv`.

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

Follow the cargo through every handoff from origin to clinic, so any gap in the thread appears as a gap in the ledger. Use these step names exactly:

1. `Requirement defined`
2. `Cargo received`
3. `Cargo released`
4. `Vehicle made ready`
5. `Movement authorized`
6. `Route window met`
7. `Cargo delivered`
8. `Usable effect confirmed`

First check the exact identity, the source's authority, and the relevant time. Check quantity and condition where they apply. Then record what the step depends on, what it hands forward, and what remains uncertain. Some entries need only one word; use more when the reasoning calls for it.

If a row depends on another unsupported statement, add a child row and inspect that statement too. Keep splitting until you reach:

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

The script helps you calculate; it isn't evidence. The source rows establish the premises, and your ledger shows whether each premise belongs in the calculation.

![Recompute from supported premises and units, then check feasibility separately; a valid calculation does not establish that the handoff can occur.](figures/m01-recompute-feasibility.png)

*Recompute from supported premises and units, then check feasibility separately; a valid calculation does not establish that the handoff can occur.*

<details markdown="1">
<summary>Figure text</summary>

Start with source values and their units, then ask whether the premises are supported. If not, the claim is UNSUPPORTED and leads to HOLD. If they are, show the operation that produces an independent result; don't copy the producer's result. Next, ask whether the required entry conditions are met. If not, the result is counterfactual, not observed. If they are, the result is feasible at this boundary only; delivery has not been observed.

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

For each source you set aside, explain why it doesn't support the recommendation. Your verdict should account for the sources you didn't use, not just those you did. After opening every inbox file and running the hash command, write `challenge-matrix.md` yourself.

Write one block for each source you will not use to support `GO`. In each block, state:

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

Choose one rebuttal path. Both give you claims to inspect, but neither makes the producer an independent verifier. The practice path uses a supplied fictional rebuttal and records that no live model ran. The live path uses the pinned OMP/OpenRouter launcher and allows only `producer-rebuttal.md` to be written. A failed child is not a success, even if a file remains. Without a key, the live path exits 2 before producing an artifact.

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

Write `corrected-brief.md` so another class member can decide what needs attention next without having watched you work. Include what is supported, what is contradicted, what remains unresolved, which later events have not occurred, the current blockers, the exact sources and calculations behind those blockers, and the next evidence needed.

A classmate who did not watch you work must be able to understand the decision and its evidence from the review page. An AI agent's inspection supplies technical observations only; it does not replace the classmate's review.

![A defensible verdict names its evidence, blockers, uncertainty, and next evidence; a producer's rebuttal is not independent verification.](figures/m01-supported-verdict.png)

*A defensible verdict names its evidence, blockers, uncertainty, and next evidence; a producer's rebuttal is not independent verification.*

<details markdown="1">
<summary>Figure text</summary>

Treat a producer rebuttal as another claim and sort it as supported, contradicted, or unresolved. For each claim, point to the exact sources and calculations behind that finding. Use those findings to state a class-only decision of ACCEPT, REVISE, REJECT, or HOLD, along with the current blockers, the next evidence, and who can supply it. For unresolved claims, name the next evidence and its owner directly.

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

Open `review.html` in your browser and check that your blockers and evidence appear. The verdict remains `UNSET` until step 9; ask your classmate to review the page after that step. The packet check below confirms that the page includes the decision-critical state.

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

Choose your verdict and record its identity before any source changes. That gives you a fixed baseline for judging a later change. Add the verdict fields below the identity block you wrote in step 2, so the file reads:

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

After `Verdict:`, write exactly one of `ACCEPT`, `REVISE`, `REJECT`, or `HOLD`. Choose `ACCEPT` only when every material claim needed for this class-only decision is supported. Choose `REVISE` when the evidence supports a decision after bounded corrections to the brief, or `REJECT` when it contradicts the recommendation. Choose `HOLD` when required evidence, authority, access, or a decision condition is unresolved.

Even if most of the brief is right, an unsupported material premise blocks `ACCEPT`.

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

Render the review page again so it shows the verdict, then ask a classmate who did not watch you work to answer the five questions from that page alone. Use three minutes as a review target, not a measured guarantee.

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

Before you revise anything, record your classmate's first answers and questions. If no eligible person is available, mark the classmate review blocked and continue with technical inspection only. Neither an agent nor your own rereading can supply the missing human observation.

## 10. Predict the source-change effect

Before you see a new source, write down what it should and should not change. That lets you check your revision against your prediction rather than explaining it after the fact. Write `change-prediction.md` before running the reveal command:

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

Start with the frozen baseline. Predict what may change and what must not change before you reveal the source update. Then update the claims that depend on the new source and keep unrelated blockers visible. Recompute the verdict either way; new evidence does not automatically produce a GO.

</details>

Your prediction must exist before you reveal the change. Freeze the source register, baseline ledger, challenge matrix, corrected brief, verdict, and prediction:

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

Now open `REVEALED_CHANGE.md` in your work folder. Refer to this revealed source as `S10`; keep the frozen nine-source register unchanged. Do not open the staff fixture directly.

Copy the baseline rows into the starter's untouched `changed-thread-ledger.csv`. The command refuses to run if the changed ledger already contains work. Keep the baseline unchanged. Then update only claims that depend on the current gate closure, recording the source revision, old value, new value, and reason for every change.

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

In your editor, update the seeded ledger and write `changed-brief.md`; do not overwrite `corrected-brief.md`. Change downstream language only where the new source supports it. Route rows may need revised identity/version details, calculations, entry conditions, and handoffs. For other steps, keep facts, source identities, calculations, and results unchanged. If the new route premise changes a warrant or uncertainty, cite S10 or the changed route claim's ID in your explanation. Do not backdate a later-issued source into the original decision.

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

**Expected:** All seven visible practice phases pass. The checker compares both verdict lines with the practice case's known answer. If yours differs, it prints `FAIL: baseline verdict is HOLD` or `FAIL: changed verdict is HOLD`. Recheck your blockers against the sources, but do not change your judgment just to match the checker. Record a verdict you still stand behind in `handoff.md`. Your reading of the sources, your classmate's review, and your own judgment remain separate evidence requirements.

**Stop:** Stale values or unrelated change errors.

**Recovery:** Correct only the dependent parts and rerun both commands.

## 12. Finish the handoff

Write `handoff.md` so the next reader can find your verdict, its evidence, and what to inspect first:

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

A classmate who did not watch you work should be able to reconstruct the verdict without coaching.

## 13. Defend the thread, not the form

Your instructor or a classmate will choose one handoff between adjacent thread steps and one material claim row. You do not choose the easiest examples.

For the **thread walk**, use the review page and explain:

1. what the first step produced;
2. what the next step required;
3. whether the output met that requirement;
4. which source or calculation established the result; and
5. what would break the handoff.

For the **claim defense**, open the cited source and show:

1. the exact entity and current version;
2. the passage or row you used;
3. your calculation or warrant;
4. why an attractive competing source does not establish the claim; and
5. what observation would falsify your row.

Use your saved work to show the evidence. If the selected handoff or claim lacks a supportable explanation, keep that work decision on `HOLD` and record what remains unresolved. A completed ledger alone does not establish support.

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
- the handoff supports reconstruction without coaching; and
- the work remains inside the fictional class case.



<details class="rf-stretch" markdown="1">
<summary>Optional stretch: defend changed and unchanged claims</summary>

In `W/dependency-defense.md`, follow every material claim in the baseline and changed briefs from its source and calculation or warrant through the thread output to what depends on it downstream. Mark each claim changed or unchanged and explain why. Include delivery and authority claims even when their state remains unknown.

Choose one unchanged claim supported by a source independent of the new bulletin. Describe a counterfactual observation that would change the claim, name who could supply it, and explain why the revealed bulletin does not supply it. Do not invent that observation or add a second mission.

**Expected:** All and only supported downstream claims change. Unrelated facts retain their original support, and an unknown later event never becomes an observed fact through implication.

**Stop:** You cannot trace a change through its dependency, an unchanged claim has no support beyond habit, or you are treating the counterfactual as evidence that actually arrived.

**Recovery:** Reopen the exact source and both ledger rows. Correct the reasoning in your defense record without changing the frozen baseline files. If no independent reviewer is available, keep the technical record and leave the human defense unmeasured.

</details>

