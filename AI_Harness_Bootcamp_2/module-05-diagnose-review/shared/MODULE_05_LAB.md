# Module 5 · Diagnose and recover

A required field drops off a Copper Span duty card. Find where it disappeared before you change anything. Keep the failed card. The probe tells you whether the source never had the field, or the program that writes the card left it out. Then make one correction you can undo, and show the card meets the same rules as before.

Plan for about three hours (a rough estimate).

The case is fictional and for class only. Nothing here plans or authorizes a real movement.

## Prepare a separate attempt

Open an ordinary terminal and run this block. It uses the Python and checkout from setup, creates a new work folder `W` and a records folder `E`, and leaves earlier attempts alone. The preparer prints a suggested next command. Don't run it.

**Terminal: Bash or zsh, ordinary user.**

```bash
R="$HOME/Documents/AIHB_OCT_2026"
PY="$(for candidate in python3.12 python3 python; do "$candidate" -c 'import sys; sys.exit(1) if sys.version_info < (3, 12) else print(sys.executable)' 2>/dev/null && break; done)"
[ -n "$PY" ] || echo 'HOLD: Python 3.12 or newer is required.' >&2
M="$R/AI_Harness_Bootcamp_2/module-05-diagnose-review"
RUN="$(date -u +%Y%m%dT%H%M%SZ)-$$"
mkdir -p "$HOME/course-evidence" && printf '%s\n' "$RUN" > "$HOME/course-evidence/module-05-run" && printf 'RUN=%s\n' "$RUN"
W="$HOME/course-evidence/module-05-$RUN/work"
E="$HOME/course-evidence/module-05-$RUN/evidence"
"$PY" "$R/shared/prepare_work.py" 05 "$W" &&
"$PY" -c "from pathlib import Path; import sys; Path(sys.argv[1]).mkdir(parents=True, exist_ok=False)" "$E"
```

**Terminal: PowerShell, ordinary user.**

```powershell
$R = "$HOME\Documents\AIHB_OCT_2026"
$PY = $(foreach ($candidate in 'python3.12','python3','python') { try { $resolved = & $candidate -c 'import sys; sys.exit(1) if sys.version_info < (3,12) else print(sys.executable)' 2>$null; if ($LASTEXITCODE -eq 0 -and $resolved) { $resolved.Trim(); break } } catch {} })
if (-not $PY) { throw 'No Python >= 3.12 found' }
$M = "$R\AI_Harness_Bootcamp_2\module-05-diagnose-review"
$RUN = [guid]::NewGuid().ToString('N')
New-Item -ItemType Directory -Force -Path "$HOME\course-evidence" | Out-Null; Set-Content -LiteralPath "$HOME\course-evidence\module-05-run" -Value $RUN; "RUN=$RUN"
$W = "$HOME\course-evidence\module-05-$RUN\work"
$E = "$HOME\course-evidence\module-05-$RUN\evidence"
& $PY "$R\shared\prepare_work.py" 05 "$W"
if ($LASTEXITCODE -ne 0) { throw 'Preparation stopped; preserve this attempt.' }
& $PY -c "from pathlib import Path; import sys; Path(sys.argv[1]).mkdir(parents=True, exist_ok=False)" "$E"
```

**Expected:** The preparer prints `PASS: created`, then the full work path. `W` contains `scripts/render_review.py`, `scripts/restore.py`, `baseline/`, `shared/case/ledger.json` (and the stretch ledgers), and an empty `out/` directory. `E` is the records folder next to it.

**Stop:** A command fails, the destination already exists, Python isn't the 3.12-or-newer interpreter you checked in setup, or you already ran the suggested command and created a review.

**Recovery:** Keep this attempt. Fix the missing setup piece, then run this block again with a new `RUN`. Don't reset the checkout or delete an old work folder.

### If you open a new terminal

A closed terminal forgets these variables. In a new terminal, run this block to load them again for the same attempt. Don't prepare another one.

**Terminal: Bash or zsh, ordinary user.**

```bash
R="$HOME/Documents/AIHB_OCT_2026"
PY="$(for candidate in python3.12 python3 python; do "$candidate" -c 'import sys; sys.exit(1) if sys.version_info < (3, 12) else print(sys.executable)' 2>/dev/null && break; done)"
[ -n "$PY" ] || echo 'HOLD: Python 3.12 or newer is required.' >&2
RUN="$(cat "$HOME/course-evidence/module-05-run")"
M="$R/AI_Harness_Bootcamp_2/module-05-diagnose-review"
W="$HOME/course-evidence/module-05-$RUN/work"
E="$HOME/course-evidence/module-05-$RUN/evidence"
printf '%s\n' "RUN=$RUN" "W=$W"
```

**Terminal: PowerShell, ordinary user.**

```powershell
$R = "$HOME\Documents\AIHB_OCT_2026"
$PY = $(foreach ($candidate in 'python3.12','python3','python') { try { $resolved = & $candidate -c 'import sys; sys.exit(1) if sys.version_info < (3,12) else print(sys.executable)' 2>$null; if ($LASTEXITCODE -eq 0 -and $resolved) { $resolved.Trim(); break } } catch {} })
if (-not $PY) { throw 'HOLD: Python 3.12 or newer is required.' }
$RUN = (Get-Content -LiteralPath "$HOME\course-evidence\module-05-run" -Raw).Trim()
$M = "$R\AI_Harness_Bootcamp_2\module-05-diagnose-review"
$W = "$HOME\course-evidence\module-05-$RUN\work"
$E = "$HOME\course-evidence\module-05-$RUN\evidence"
"RUN=$RUN"; "W=$W"
```

**Expected:** The terminal prints `RUN=` followed by the identifier you saw when you prepared this attempt, then `W=` followed by the existing work folder.

**Stop:** The identifier differs from the one you wrote down, or the folder named after `W=` does not exist.

**Recovery:** If the identifier differs, a later attempt overwrote the saved marker. Set `RUN` to the value you wrote down and run the block again. If the folder is missing, this attempt was never prepared. Run the first block.

## 1. Confirm the clean render

Write the card with the clean **renderer**, the supplied program that turns ledger rows into a duty card. Keep this output. It's the known-good card you'll compare against later.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$W/scripts/render_review.py" "$W/shared/case/ledger.json" "$W/out/baseline.md"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$W\scripts\render_review.py" "$W\shared\case\ledger.json" "$W\out\baseline.md"
```

**Expected:** The terminal prints the full path of `baseline.md`.

**Stop:** The command prints a line starting `HOLD:`.

**Recovery:** Check the variables and that `ledger.json` is under `W`. Keep any output already written and rerun with a new output filename.

Open the card and check that both required fields are there.

**Terminal: Bash or zsh, ordinary user.**

```bash
cat "$W/out/baseline.md"
```

**Terminal: PowerShell, ordinary user.**

```powershell
Get-Content "$W\out\baseline.md"
```

**Expected:** The card shows `current_rows:`, `near_miss_rows:`, `near_miss_ids:`, and `scanned_quantity:` lines, then a `permit_status:` line and a `gate_time_mdt:` line, each with a value, then `class_only: true`.

**Stop:** Either `permit_status:` or `gate_time_mdt:` is missing from the card.

**Recovery:** Check the variables and that `ledger.json` is under `W`, then render again to a new output filename. Keep the earlier output.

Then read the rules for this card in [shared/case/DUTY_CARD.md](case/DUTY_CARD.md).

## 2. Verify restore before any swap

Test restore before you place the fault. The restore command checks the clean baseline's **digest**, a fingerprint of its file bytes. The command saves your current renderer and `out/` files under `attempts/`, then copies the baseline over the work renderer.

![Check that restore puts the clean renderer back before you place a fault, and keep the current attempt and output.](figures/m05-restore-precondition.png)

*Check that restore puts the clean renderer back before you place a fault, and keep the current attempt and output.*

<details markdown="1">
<summary>Figure text</summary>

Start with the clean baseline renderer and check its digest. If the fingerprint does not match, stop at `HOLD` before you replace anything. If it matches, save the current renderer and output as a kept attempt, then copy the baseline over the work renderer. Confirm `RESTORE OK` before you place the practice fault.

</details>

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$W/scripts/restore.py" "$W"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$W\scripts\restore.py" "$W"
```

**Expected:** `RESTORE OK` is printed, and the `scripts/render_review.py` bytes now match the baseline.

**Stop:** `RESTORE OK` is not printed, or the files differ.

**Recovery:** Do not continue. Record the error and start with a new prepare_work destination.

## 3. Seal the first miss

When your instructor says so, place the practice fault. It breaks only the renderer in your work copy. The clean baseline stays untouched. Don't fix anything until you've written down where the field first disappears.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$M/scripts/place_practice_fault.py" "$W" --variant A
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$M\scripts\place_practice_fault.py" "$W" --variant A
```

**Expected:** `FAULT PLACED A`.

**Stop:** A line starting `HOLD:`, for example `HOLD: work copy is not the clean baseline` or `HOLD: output already exists`.

**Recovery:** Run the restore from step 2 again, confirm `RESTORE OK`, then place the fault again. If the hold names an existing output, you have already placed the fault in this attempt. Continue.

Write the card again with the faulty renderer:

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$W/scripts/render_review.py" "$W/shared/case/ledger.json" "$W/out/miss.md"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$W\scripts\render_review.py" "$W\shared\case\ledger.json" "$W\out\miss.md"
```

**Expected:** The terminal prints the full path of `miss.md`. The render succeeds. The fault drops a field instead of crashing the renderer.

**Stop:** A line starting `HOLD:`.

**Recovery:** Keep the output. Check that the ledger path is the one under `W`, then repeat with a new output filename.

Before you run the probe, write down how you would tell whether a field is missing from the source or lost while the card is written. The read-only **probe** compares the required fields in the selected source rows with the rendered card. The command runs it from the checkout, not your work copy, so the fault can't turn it off:

![Compare the selected source and the written card, keep the first mismatch, and read what the probe calls it before you replace anything.](figures/m05-first-divergence.png)

*Compare the selected source and the written card, keep the first mismatch, and read what the probe calls it before you replace anything.*

<details markdown="1">
<summary>Figure text</summary>

Check the selected source rows for each required field, in order. If a source value is missing, the ordinary probe reports `source_omission`. If it is present, check whether the selected rows agree. Conflicting values produce `source_conflict`. When the values agree, check for a written card. If there is no card, the result is `output_absent`. If the card exists, the probe reports `rendered` when it contains the field and `renderer_omission` when it does not. Stop at the first failing check. Write down what you expected, what you saw, and the exact command, then save that record before you change anything. A probe exit status of 0 means the check ran. It does not mean the card is complete. The ordinary probe does not catch a wrong input version. That takes the optional `--intended` comparison, which reports `wrong_input_version` outside these core outcomes.

</details>

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$M/scripts/probe_fields.py" "$W/shared/case/ledger.json" --review "$W/out/miss.md"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$M\scripts\probe_fields.py" "$W\shared\case\ledger.json" --review "$W\out\miss.md"
```

**Expected:** The probe prints four lines: `selected_source_ids` followed by the current row IDs, `review_present yes`, one field line ending `renderer_omission`, and the other ending `rendered`. The field marked `renderer_omission` is the first one missing from the card.

**Stop:** You can't name the earliest missing field from the probe output, or more than one field is missing.

**Recovery:** Record `HOLD`. Wait to replace the renderer until the probe shows the field in the selected source but not on the card. If the source is missing it, replacing the renderer cannot bring that information back.

Now write `$E/sealed-first-miss.md` from the probe output. Do this before you replace anything, and don't change the file afterwards. Record the last place the field is still present, and the first place it's missing:

```markdown
# Sealed first miss

Command:
Observed output (first 20 lines):
Probe output:
  selected_source_ids ...
  review_present yes
  permit_status ...
  gate_time_mdt ...
First missing field:
Still present:
```

## 4. One authorized replace

Replace the renderer only if the probe names it as the first failing place (`renderer_omission`). Make that one allowed replacement by running restore. The command first saves the failed renderer and `out/` under `attempts/`, then copies the clean baseline back. Don't edit the card by hand, and don't drop a required field from the rules the card has to meet.

![Replace the renderer only when the evidence points to it. Keep the failed attempt. Don't patch the card or drop a required field.](figures/m05-authorized-correction.png)

*Replace the renderer only when the evidence points to it. Keep the failed attempt. Don't patch the card or drop a required field.*

<details markdown="1">
<summary>Figure text</summary>

Start from the saved diagnosis. If it shows that the renderer is the first failing place (`renderer_omission`), make one allowed replacement: run restore once. Before the clean renderer comes back, the failed attempt (the failed renderer and its output) is saved and kept. Then restore the clean renderer. If the diagnosis points to any other cause, stop at `HOLD` and do not replace the renderer. Two actions are not allowed, and they are not recovery: editing the output card by hand, and removing a required field from the rules the card has to meet.

</details>

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$W/scripts/restore.py" "$W"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$W\scripts\restore.py" "$W"
```

**Expected:** `RESTORE OK`, and the work copy now matches the baseline bytes.

**Stop:** You made more than one change, or you replaced the renderer before saving the miss.

**Recovery:** Record the error. Start over with a fresh prepare_work destination.

Then write `$E/replace-record.md` with the command, the `RESTORE OK` line, and why replacing the renderer fixes the cause you found.

## 5. Prove recovery three ways

Finding the cause isn't enough. Show the repair with three checks, in this order. Each one must show both required fields.

![Show the field check, the complete card, and a new run in a fresh folder, without dropping either required field.](figures/m05-recovery-proofs.png)

*Show the field check, the complete card, and a new run in a fresh folder, without dropping either required field.*

<details markdown="1">
<summary>Figure text</summary>

Recovery needs three separate proofs. First, a field probe of a newly written card. Second, a complete card from the named ledger. Third, a new run in a fresh folder, started from a working directory that is not the work copy. Each proof must show both required fields, `permit_status` and `gate_time_mdt`. All three proofs use the same rules. No proof drops a field or makes the rules easier.

</details>

First, the field check: write a new card and use the probe to check its required fields.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$W/scripts/render_review.py" "$W/shared/case/ledger.json" "$W/out/focused.md" &&
"$PY" "$M/scripts/probe_fields.py" "$W/shared/case/ledger.json" --review "$W/out/focused.md"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$W\scripts\render_review.py" "$W\shared\case\ledger.json" "$W\out\focused.md"
if ($LASTEXITCODE -ne 0) { throw 'Focused render held.' }
& $PY "$M\scripts\probe_fields.py" "$W\shared\case\ledger.json" --review "$W\out\focused.md"
```

Second, the full check: write the complete card from the work-copy ledger. Then open `complete.md` and check both fields.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$W/scripts/render_review.py" "$W/shared/case/ledger.json" "$W/out/complete.md"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$W\scripts\render_review.py" "$W\shared\case\ledger.json" "$W\out\complete.md"
```

Third, the clean-condition check: copy the renderer and ledger to a fresh folder. Then run them in a new process from your home folder, a working directory that is not the work copy.

**Terminal: Bash or zsh, ordinary user.**

```bash
FRESH="$HOME/course-evidence/module-05-$RUN/fresh"
"$PY" -c "
from pathlib import Path
import sys
p = Path(sys.argv[1])
if p.exists() or p.is_symlink(): sys.exit(1)
p.mkdir(parents=True)
" "$FRESH" &&
cp "$W/scripts/render_review.py" "$FRESH/" &&
cp "$W/shared/case/ledger.json" "$FRESH/" &&
cd "$HOME" &&
"$PY" "$FRESH/render_review.py" "$FRESH/ledger.json" "$FRESH/review.md"
```

**Terminal: PowerShell, ordinary user.**

```powershell
$FRESH = "$HOME\course-evidence\module-05-$RUN\fresh"
& $PY -c "
from pathlib import Path
import sys
p = Path(sys.argv[1])
if p.exists() or p.is_symlink(): sys.exit(1)
p.mkdir(parents=True)
" "$FRESH"
if ($LASTEXITCODE -ne 0) { throw 'Fresh dir exists.' }
Copy-Item "$W\scripts\render_review.py" "$FRESH\"
Copy-Item "$W\shared\case\ledger.json" "$FRESH\"
Set-Location "$HOME"
& $PY "$FRESH\render_review.py" "$FRESH\ledger.json" "$FRESH\review.md"
```

**Expected:** The focused probe reports both fields as `rendered`, and the complete and fresh review files both contain `permit_status` and `gate_time_mdt`. The fresh run used a new folder and started from your home folder. A probe exit code of 0 only means the probe ran; read its field lines.

**Stop:** Any of the three outputs lacks `permit_status:` or `gate_time_mdt:`, or the focused probe reports anything other than `rendered`.

**Recovery:** Keep the failed output. Fix the path problem you found, then use unused output names for another proof. If you need to replace the renderer again, start a fresh attempt. Don't erase the first correction.

Keep the three outputs, the focused probe result, and the saved miss for your handoff.

Finally, check that the commands still work when the work path contains a space. This block prepares a separate attempt and writes a baseline card, because restore needs an output to save. Then it restores the renderer and probes a new card. Your main attempt stays untouched.

**Terminal: Bash or zsh, ordinary user.**

```bash
SPACE_WORK="$HOME/course-evidence/module-05-$RUN/work with space"
"$PY" "$R/shared/prepare_work.py" 05 "$SPACE_WORK" &&
"$PY" "$SPACE_WORK/scripts/render_review.py" "$SPACE_WORK/shared/case/ledger.json" "$SPACE_WORK/out/baseline.md" &&
"$PY" "$SPACE_WORK/scripts/restore.py" "$SPACE_WORK" &&
"$PY" "$SPACE_WORK/scripts/render_review.py" "$SPACE_WORK/shared/case/ledger.json" "$SPACE_WORK/out/focused.md" &&
"$PY" "$M/scripts/probe_fields.py" "$SPACE_WORK/shared/case/ledger.json" --review "$SPACE_WORK/out/focused.md"
```

**Terminal: PowerShell, ordinary user.**

```powershell
$SPACE_WORK = "$HOME\course-evidence\module-05-$RUN\work with space"
& $PY "$R\shared\prepare_work.py" 05 "$SPACE_WORK"
if ($LASTEXITCODE -ne 0) { throw 'Spaced work preparation held.' }
& $PY "$SPACE_WORK\scripts\render_review.py" "$SPACE_WORK\shared\case\ledger.json" "$SPACE_WORK\out\baseline.md"
if ($LASTEXITCODE -ne 0) { throw 'Baseline render held.' }
& $PY "$SPACE_WORK\scripts\restore.py" "$SPACE_WORK"
if ($LASTEXITCODE -ne 0) { throw 'Restore held.' }
& $PY "$SPACE_WORK\scripts\render_review.py" "$SPACE_WORK\shared\case\ledger.json" "$SPACE_WORK\out\focused.md"
if ($LASTEXITCODE -ne 0) { throw 'Focused render held.' }
& $PY "$M\scripts\probe_fields.py" "$SPACE_WORK\shared\case\ledger.json" --review "$SPACE_WORK\out\focused.md"
```

**Expected:** Preparation and both renders succeed, restore prints `RESTORE OK`, and the probe reports both fields as `rendered`.

**Stop:** Any command holds or either field is absent.

**Recovery:** Keep this directory. Fix the named problem, then choose a new spaced destination instead of reusing an existing output.

## 6. Finish the handoff

Write `$E/handoff.md` so the next person can repeat your result and check it without asking you:

```markdown
# Module 5 handoff

First missing field:
Probe output that showed it:
  (include selected_source_ids, review_present, and the cause line)
Replace command:
Previous renderer and outputs preserved in: (the attempts folder under W)
Focused probe result:
Complete render file:
Fresh-process rerun file:
What the next person should inspect first:
```

## Stretch: competing causes on a second case

<details class="rf-stretch" markdown="1">
<summary>Optional stretch: distinguish source omission, wrong input version, and renderer omission</summary>

Three different causes can make a field go missing: the source never had it, you used the wrong version of the input, or the renderer dropped a field the source supplies. Before you start, write in `E/stretch-prediction.md` which cause you expect in each case, and what you would see that tells them apart. Leave the core evidence unchanged.

### Inspect missing source evidence

Write a card from the second ledger with the clean renderer. The renderer should refuse it, and the command then runs the probe on the source rows. Don't fill a source gap by changing code.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$W/scripts/render_review.py" "$W/shared/case/ledger-stretch.json" "$W/out/source-omission.md"
SOURCE_EXIT=$?
if [ "$SOURCE_EXIT" -eq 1 ]; then
  "$PY" "$M/scripts/probe_fields.py" "$W/shared/case/ledger-stretch.json"
else
  printf '%s\n' 'HOLD: expected a malformed-source refusal; inspect the actual result.'
  false
fi
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$W\scripts\render_review.py" "$W\shared\case\ledger-stretch.json" "$W\out\source-omission.md"
if ($LASTEXITCODE -ne 1) { throw 'Expected a malformed-source refusal; inspect the actual result.' }
& $PY "$M\scripts\probe_fields.py" "$W\shared\case\ledger-stretch.json"
```

**Expected:** The renderer prints `HOLD: malformed input (permit_status)`. The probe then prints `permit_status source_omission BK-202` and `gate_time_mdt source_omission BK-203`.

**Stop:** The renderer accepts the incomplete source, or you cannot find the missing values in the named rows.

**Recovery:** Keep the refusal and the probe output. Get the missing source from its owner. Putting the renderer back cannot create that information.

### Compare the intended input

Probe the stale ledger against the supplied intended ledger. Look at both the source IDs and their revisions. Matching IDs don't mean matching versions.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$M/scripts/probe_fields.py" "$W/shared/case/ledger-stale.json" --intended "$W/shared/case/ledger-intended.json"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$M\scripts\probe_fields.py" "$W\shared\case\ledger-stale.json" --intended "$W\shared\case\ledger-intended.json"
```

**Expected:** The probe reports `wrong_input_version` and prints both selections and their revisions.

**Stop:** You cannot explain which intended source replaces the stale selection.

**Recovery:** Write down the input-selection error and name the correct snapshot. Don't replace a working renderer to hide a wrong input.

### Localize the other renderer omission

The main ledger has both fields. Place variant B, write the card to a new name, and use the result to find the first missing field before you allow a replacement.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$M/scripts/place_practice_fault.py" "$W" --variant B &&
"$PY" "$W/scripts/render_review.py" "$W/shared/case/ledger.json" "$W/out/stretch-miss.md" &&
"$PY" "$M/scripts/probe_fields.py" "$W/shared/case/ledger.json" --review "$W/out/stretch-miss.md"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$M\scripts\place_practice_fault.py" "$W" --variant B
if ($LASTEXITCODE -ne 0) { throw 'Fault placement held.' }
& $PY "$W\scripts\render_review.py" "$W\shared\case\ledger.json" "$W\out\stretch-miss.md"
if ($LASTEXITCODE -ne 0) { throw 'Stretch render held.' }
& $PY "$M\scripts\probe_fields.py" "$W\shared\case\ledger.json" --review "$W\out\stretch-miss.md"
```

**Expected:** One field is `renderer_omission`; the other is `rendered`. Seal this miss and the source support in `E/sealed-stretch-miss.md` before continuing.

**Stop:** More than one field is missing, or the selected source does not supply the omitted value.

**Recovery:** Keep what you saw and find the earlier cause. Don't replace anything until the evidence points to this renderer.

### Prove the second recovery without overwriting the first

Allow one baseline replacement for the saved variant-B miss. Use new output names and a new fresh-process folder for its three proofs.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$W/scripts/restore.py" "$W" &&
"$PY" "$W/scripts/render_review.py" "$W/shared/case/ledger.json" "$W/out/stretch-focused.md" &&
"$PY" "$M/scripts/probe_fields.py" "$W/shared/case/ledger.json" --review "$W/out/stretch-focused.md" &&
"$PY" "$W/scripts/render_review.py" "$W/shared/case/ledger.json" "$W/out/stretch-complete.md"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$W\scripts\restore.py" "$W"
if ($LASTEXITCODE -ne 0) { throw 'Stretch restore held.' }
& $PY "$W\scripts\render_review.py" "$W\shared\case\ledger.json" "$W\out\stretch-focused.md"
if ($LASTEXITCODE -ne 0) { throw 'Stretch focused render held.' }
& $PY "$M\scripts\probe_fields.py" "$W\shared\case\ledger.json" --review "$W\out\stretch-focused.md"
if ($LASTEXITCODE -ne 0) { throw 'Stretch probe held.' }
& $PY "$W\scripts\render_review.py" "$W\shared\case\ledger.json" "$W\out\stretch-complete.md"
```

**Expected:** Restore succeeds, the focused probe reports both fields as `rendered`, and the complete output contains both values.

**Stop:** Any command holds or either field is absent.

**Recovery:** Keep the failed proof and choose unused names for a justified new attempt. Never overwrite the core proof files.

**Terminal: Bash or zsh, ordinary user.**

```bash
FRESH="$HOME/course-evidence/module-05-$RUN/fresh-stretch"
"$PY" -c "from pathlib import Path; import sys; Path(sys.argv[1]).mkdir(parents=True, exist_ok=False)" "$FRESH" &&
cp "$W/scripts/render_review.py" "$FRESH/" &&
cp "$W/shared/case/ledger.json" "$FRESH/" &&
cd "$HOME" &&
"$PY" "$FRESH/render_review.py" "$FRESH/ledger.json" "$FRESH/review.md"
```

**Terminal: PowerShell, ordinary user.**

```powershell
$FRESH = "$HOME\course-evidence\module-05-$RUN\fresh-stretch"
& $PY -c 'from pathlib import Path; import sys; Path(sys.argv[1]).mkdir(parents=True, exist_ok=False)' "$FRESH"
if ($LASTEXITCODE -ne 0) { throw 'Fresh stretch destination already exists.' }
Copy-Item "$W\scripts\render_review.py" "$FRESH\" -ErrorAction Stop
Copy-Item "$W\shared\case\ledger.json" "$FRESH\" -ErrorAction Stop
Set-Location -LiteralPath $HOME -ErrorAction Stop
& $PY "$FRESH\render_review.py" "$FRESH\ledger.json" "$FRESH\review.md"
```

**Expected:** The new process produces a review with both fields while using only the copied renderer and ledger, from a working directory that is not the work copy.

**Stop:** The destination exists or the copied run fails.

**Recovery:** Keep the failed directory. After you correct the cause you found, use a new destination. Write down which source or renderer change each of the three cases actually justified. A successful renderer replacement in one case won't fix all three.

</details>

## Before you stop

Check that:

- restore printed `RESTORE OK` before the first swap;
- the saved miss names exactly one earliest field, based on the probe output for the selected rows;
- you made only one allowed replacement;
- the focused probe confirmed both fields on the work-copy card, and the complete card and the fresh-folder output also show both fields (the fresh run started from your home folder);
- the work stayed inside the fictional class case.

Keep the saved misses, the source selections, each replacement record, and all three recovery proofs. The next person should be able to tell a source gap from a wrong version, or from a field the renderer dropped, without asking you.
