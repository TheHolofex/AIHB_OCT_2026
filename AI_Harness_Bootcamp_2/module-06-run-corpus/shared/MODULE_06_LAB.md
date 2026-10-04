# Module 6 · Improve from observed failures

Find a repeated failure in Blue Gauge's practice records. Turn it into a check that flags the same text in another run. Use your failure notes to define a **predicate**: a yes-or-no condition. Configure the supplied control with two exact pieces of text, test it on known-bad, known-good, and missing input, and record what it catches and misses.

The eighty records are fictional practice runs about oxygen cylinders moving from East Yard to Clinic O-2. They aren't real workplace observations and don't measure model reliability. Don't use this packet to plan, authorize, dispatch, or describe a real movement. A module result is for class review only.

Plan for about three hours (a rough estimate).

## Copy a work folder

Use the checkout and Python you verified in setup. The block below sets variables for this attempt. `R` points to the checkout at `$HOME/Documents/AIHB_OCT_2026`, `PY` to the full path of Python 3.12 or newer, `M` to the module sources, `RUN` to a unique name, `W` to the work folder, and `E` to the evidence folder, both outside the checkout. Use the command blocks for your terminal throughout.

**Terminal: Bash or zsh, ordinary user.**

```bash
R="$HOME/Documents/AIHB_OCT_2026"
PY="$(for candidate in python3.12 python3 python; do "$candidate" -c 'import sys; sys.exit(1) if sys.version_info < (3, 12) else print(sys.executable)' 2>/dev/null && break; done)"
[ -n "$PY" ] || echo 'HOLD: Python 3.12 or newer is required.' >&2
M="$R/AI_Harness_Bootcamp_2/module-06-run-corpus"
RUN="$(date -u +%Y%m%dT%H%M%SZ)-$$"
mkdir -p "$HOME/course-evidence" && printf '%s\n' "$RUN" > "$HOME/course-evidence/module-06-run" && printf 'RUN=%s\n' "$RUN"
W="$HOME/course-evidence/module-06-$RUN/work"
E="$HOME/course-evidence/module-06-$RUN/evidence"
```

**Expected:** The terminal prints `RUN=` followed by this attempt's identifier. Note it. `R` points to the checkout, `PY` to Python 3.12 or newer, `W` and `E` to new paths.

**Stop:** PY is empty or doesn't point to Python 3.12 or newer.

**Recovery:** Follow the setup instructions to fix Python, then run the block again in a new terminal.

**Terminal: PowerShell, ordinary user.**

```powershell
$R = "$HOME\Documents\AIHB_OCT_2026"
$PY = $null
foreach ($candidate in @('python3.12', 'python3', 'python')) {
  $cmd = Get-Command $candidate -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
  if ($cmd) {
    $ver = & $cmd.Source -c "import sys; print(1 if sys.version_info >= (3, 12) else 0)" 2>$null
    if ($ver -eq '1') {
      $PY = & $cmd.Source -c "import sys; print(sys.executable)"
      break
    }
  }
}
if (-not $PY) { throw 'Python 3.12 or newer not found on PATH.' }

$M = "$R\AI_Harness_Bootcamp_2\module-06-run-corpus"
$RUN = [guid]::NewGuid().ToString('N')
New-Item -ItemType Directory -Force -Path "$HOME\course-evidence" | Out-Null; Set-Content -LiteralPath "$HOME\course-evidence\module-06-run" -Value $RUN; "RUN=$RUN"
$W = "$HOME\course-evidence\module-06-$RUN\work"
$E = "$HOME\course-evidence\module-06-$RUN\evidence"
```

**Terminal: Bash or zsh, ordinary user.**

```bash
mkdir -p "$E"
```

**Expected:** The evidence folder `E` exists.

**Stop:** `mkdir` fails with a permission error.

**Recovery:** Use a writable path under $HOME/course-evidence and run `mkdir` again with the full path.

**Terminal: PowerShell, ordinary user.**

```powershell
New-Item -ItemType Directory -Force -Path "$E" | Out-Null
```

**Expected:** The evidence folder `E` exists.

**Stop:** The command fails with a permission error.

**Recovery:** Use a writable path under $HOME/course-evidence and run `New-Item` again with the full path.

Run the shared prepare script by its full path under R. It creates the work folder (W) outside the checkout. Prepare each attempt only once.

**Terminal: Bash or zsh, ordinary user.**

```bash
cd "$R" && "$PY" "$R/shared/prepare_work.py" 06 "$W"
```

**Terminal: PowerShell, ordinary user.**

```powershell
Set-Location -LiteralPath "$R"; & $PY "$R\shared\prepare_work.py" 06 "$W"
```

**Expected:** `PASS: created` followed by the full work path, then two suggested next commands. Don't run them yet: freeze the sample rule first. The work folder contains `shared/controls/`, `shared/corpus/` with the eighty runs, and `shared/checks/`.

**Stop:** Prepare refuses with HOLD because the destination already exists.

**Recovery:** Open a new terminal, paste the variable block from the start of this lab to create a new `RUN` and `W`, then run the prepare command again.

Create the output folder under W. You only need to do this once:

**Terminal: Bash or zsh, ordinary user.**

```bash
mkdir -p "$W/out"
```

**Terminal: PowerShell, ordinary user.**

```powershell
New-Item -ItemType Directory -Force -Path "$W\out" | Out-Null
```

**Expected:** No output. The folder `W/out` now exists.

**Stop:** A permission error.

**Recovery:** Use a writable path under `$HOME/course-evidence` and run the command again with the full path.

Every later command uses full paths under `W`, so you never need to change folders. Don't copy any other checker into the work folder.

### If you open a new terminal

A closed terminal forgets these variables. In a new terminal, run this block to reload them for the same attempt instead of preparing another one.

**Terminal: Bash or zsh, ordinary user.**

```bash
R="$HOME/Documents/AIHB_OCT_2026"
PY="$(for candidate in python3.12 python3 python; do "$candidate" -c 'import sys; sys.exit(1) if sys.version_info < (3, 12) else print(sys.executable)' 2>/dev/null && break; done)"
[ -n "$PY" ] || echo 'HOLD: Python 3.12 or newer is required.' >&2
RUN="$(cat "$HOME/course-evidence/module-06-run")"
M="$R/AI_Harness_Bootcamp_2/module-06-run-corpus"
W="$HOME/course-evidence/module-06-$RUN/work"
E="$HOME/course-evidence/module-06-$RUN/evidence"
printf '%s\n' "RUN=$RUN" "W=$W"
```

**Terminal: PowerShell, ordinary user.**

```powershell
$R = "$HOME\Documents\AIHB_OCT_2026"
$PY = $(foreach ($candidate in 'python3.12','python3','python') { try { $resolved = & $candidate -c 'import sys; sys.exit(1) if sys.version_info < (3,12) else print(sys.executable)' 2>$null; if ($LASTEXITCODE -eq 0 -and $resolved) { $resolved.Trim(); break } } catch {} })
if (-not $PY) { throw 'HOLD: Python 3.12 or newer is required.' }
$RUN = (Get-Content -LiteralPath "$HOME\course-evidence\module-06-run" -Raw).Trim()
$M = "$R\AI_Harness_Bootcamp_2\module-06-run-corpus"
$W = "$HOME\course-evidence\module-06-$RUN\work"
$E = "$HOME\course-evidence\module-06-$RUN\evidence"
"RUN=$RUN"; "W=$W"
```

**Expected:** The terminal prints `RUN=` followed by the identifier you saw when you prepared this attempt, then `W=` followed by the existing work folder.

**Stop:** The identifier differs from the one you recorded, or the folder named after `W=` does not exist.

**Recovery:** A different identifier means a later attempt overwrote the saved marker; set `RUN` by hand to the value you recorded and run the block again. A missing folder means the attempt was never prepared, so run the prepare steps above.

## Pacing

Most of the session is hands-on work. Reading the sample runs and writing first-failure notes takes the longest. Freezing the config copy and running the three checks come next. Reconciling the counts and choosing the two literals take less time. Freezing the sample rule and writing the handoff are quick. Your own pace may differ.

## 1. Freeze the sample rule first

Write `sample-rule.md` before you open any run that shows an outcome or a stamp result.

This keeps the sample **outcome-blind**: you decide which runs belong without choosing any because they passed or failed. Use the declaration below only if you haven't opened the run files. If you've already seen outcomes, record that instead of claiming an outcome-blind attempt.

![Freeze the sample before reading outcomes; if you already saw results, record that exposure rather than claim an outcome-blind attempt.](figures/m06-freeze-sample.png)

*Freeze the sample before reading outcomes; if you already saw results, record that exposure rather than claim an outcome-blind attempt.*

<details markdown="1">
<summary>Figure text</summary>

Freeze eligibility before outcomes.

1. Save eligibility rule: a written rule comes first.
2. The rule fixes the sample as R-001–R-016, sixteen runs, locked in place. Keep every eligible run.
3. Then open outcomes: the same sixteen runs, now with their results visible. Membership stays locked.

Exceptions:

- Do not add or drop by result. Nothing seen in an outcome may change which runs are in the sample.
- If outcomes were seen before the rule was saved, Record prior exposure instead of claiming an outcome-blind attempt.

</details>

**Terminal: Bash or zsh, ordinary user.**

```bash
cat > "$W/sample-rule.md" << 'EOF'
# Sample rule

## Eligible set
The eligible set is R-001.md through R-016.md. I will read all sixteen. I will not add or drop a file.

## Reading rule
I have not opened a run file yet. I will not choose a run because it looks clean or broken.

## Outcome rule
I will not use a stamp result to decide which runs belong in the sample.
EOF
```

**Expected:** `sample-rule.md` exists and has the three headings.

**Stop:** `cat` fails or the file isn't created.

**Recovery:** Check permissions and run the `cat` command again with the full path.

**Terminal: PowerShell, ordinary user.**

```powershell
@"
# Sample rule

## Eligible set
The eligible set is R-001.md through R-016.md. I will read all sixteen. I will not add or drop a file.

## Reading rule
I have not opened a run file yet. I will not choose a run because it looks clean or broken.

## Outcome rule
I will not use a stamp result to decide which runs belong in the sample.
"@ | Out-File -FilePath "$W\sample-rule.md" -Encoding utf8
```

**Expected:** `sample-rule.md` exists and has the three headings.

**Stop:** The command fails or the file isn't created.

**Recovery:** Check permissions and run the `Out-File` command again with the full path.

Record the rule's fingerprint in `E` so you can show that your reading came after the rule.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" -c "import hashlib,sys; from pathlib import Path; src, dst = map(Path, sys.argv[1:]); digest = hashlib.sha256(src.read_bytes()).hexdigest(); handle = dst.open('x', encoding='utf-8'); handle.write(digest + '\n'); handle.close(); print(digest)" "$W/sample-rule.md" "$E/sample-rule.sha256"
```

**Expected:** The terminal prints a 64-character digest and writes it to a new file, `E/sample-rule.sha256`. The command exits 0.

**Stop:** The sample-rule file is missing, the digest file already exists, or you've already opened a run and seen a stamp.

**Recovery:** Leave the attempt and files in place. If you saw no outcomes: open a new terminal, repeat the prepare block, and write the rule before you open any run. If you've seen outcomes, record that and don't claim an outcome-blind attempt.

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY -c "import hashlib,sys; from pathlib import Path; src, dst = map(Path, sys.argv[1:]); digest = hashlib.sha256(src.read_bytes()).hexdigest(); handle = dst.open('x', encoding='utf-8'); handle.write(digest + '\n'); handle.close(); print(digest)" "$W\sample-rule.md" "$E\sample-rule.sha256"
Write-Output "exit $LASTEXITCODE"
```

**Expected:** The terminal prints a 64-character digest and writes it to a new file, `E\sample-rule.sha256`. The command exits 0.

**Stop:** The sample-rule file is missing, the digest file already exists, or you've already opened a run and seen a stamp.

**Recovery:** Leave the attempt and files in place. If you saw no outcomes: open a new terminal, repeat the prepare block, and write the rule before you open any run. If you've seen outcomes, record that and don't claim an outcome-blind attempt.

### If you must start a new attempt

Open a new terminal and paste the variable block from the start of this lab to create a new `RUN`. Then run:

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$R/shared/prepare_work.py" 06 "$W" &&
"$PY" -c "from pathlib import Path; import sys; Path(sys.argv[1]).mkdir(parents=True); (Path(sys.argv[2])/'out').mkdir(exist_ok=True)" "$E" "$W"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$R\shared\prepare_work.py" 06 "$W"
if ($LASTEXITCODE -ne 0) { throw 'Preparation held; preserve this attempt.' }
& $PY -c "from pathlib import Path; import sys; Path(sys.argv[1]).mkdir(parents=True); (Path(sys.argv[2])/'out').mkdir(exist_ok=True)" "$E" "$W"
```

**Expected:** The preparer creates a new work folder at the new path, and `W/out` and the new evidence folder `E` both exist before you record the digest.

**Stop:** Prepare holds because the destination already exists.

**Recovery:** Use a path that doesn't exist yet (paste the variable block into a new terminal to get a new RUN), then run the prepare command again.

If you haven't opened any outcomes, write `sample-rule.md` again and repeat the digest step with the new W and E. If you have, note it in the attempt record and don't reuse the outcome-blind declaration. A rerun can still check the control but can't give an outcome-blind first reading.

## 2. First-failure notes before categories


Open the sixteen sample files under `shared/corpus/`. For each run, write one first-failure note in `$E/first-failures.md` before any category tally.

Name the earliest concrete problem the run text supports and point to the line or passage that shows it. Don't start with a category name. If you find no failure, write that instead of inventing one. If you're unsure, say so.

![Record each run's earliest supported problem, no failure, or uncertainty before assigning categories.](figures/m06-first-failure-notes.png)

*Record each run's earliest supported problem, no failure, or uncertainty before assigning categories.*

<details markdown="1">
<summary>Figure text</summary>

Observe before categorizing.

One note per run. Each note starts with the Run ID, then records exactly one of three outcomes:

- Earliest supported problem, tied to its Evidence passage from the run text.
- No failure found.
- Uncertain.

Every run's note feeds a single gate: All notes first. Only after the complete set of notes exists does work move on to Categories later, where the notes are grouped.

</details>

**Expected:** `first-failures.md` has sixteen entries, one per sample run. Each starts with the run ID and records the earliest supported problem, an observation you couldn't resolve, or that you found no failure.

**Stop:** You wrote a category count before every run had its note. Those counts aren't evidence.

**Recovery:** Keep the notes you have, add the missing ones, and only then write or revise the counts file.

## 3. Then tally categories

Once all sixteen notes exist, group the failures you observed by what went wrong and write `$E/counts.md`. List the run IDs under each category so another reader can check the counts against the notes. Use the pass, fail, and other lines below so that every run is counted exactly once.

```markdown
# Counts

pass (run IDs):
fail by category:
  <category>: <run IDs>
other (run IDs):
total: 16
revisions to category names:
```

The total must be 16. Each category's count must match the runs listed under it. Pass, fail, and other must add up to the total. If they don't, record `HOLD` and find the run that's missing or counted twice. Then state one conclusion that the failure categories in this sample support. Don't treat how often a failure appeared here as a rate for real work or current models.

If you revise a category label, keep the original first-failure notes visible next to it.

![Reconcile pass, fail, and other to all sixteen runs once, and keep each original first-failure note beside any revised category.](figures/m06-reconcile-history.png)

*Reconcile pass, fail, and other to all sixteen runs once, and keep each original first-failure note beside any revised category.*

<details markdown="1">
<summary>Figure text</summary>

Account for each run once.

1. Run IDs: each run ID connects to exactly one bucket. Each run once.
2. The three buckets are pass, fail by category, and other.
3. Inside fail by category, each Original note sits beside its Revised category. Original notes stay; revising a category never replaces the note.
4. All three buckets add into Total = 16.
5. Exception: Counts do not close → HOLD. If the buckets do not add to sixteen, or a run is missing or counted twice, record HOLD.

</details>

**Expected:** The totals in the counts file add up to 16, and the first-failure notes are still the source of truth.

**Stop:** The totals add up to anything other than 16.

**Recovery:** Compare the counts with `first-failures.md` to find the run that's missing or counted twice. Correct the counts and keep the earlier version.

## 4. Infer two literals and configure the supplied control

Choose two exact text strings that mark your repeated failure, then freeze them. Start by reading `shared/controls/PREDICATE_SPEC.md`.

The control takes one run file and a configuration file:

`predicate.py <run-file> --config <predicate.json>`

The configuration is a JSON object with exactly one key, `all_present`. Its value is a list of exactly two different nonempty strings. Those two strings are the literals.

A **literal** is an exact piece of text. Choose two literals from your first-failure notes that together identify one repeated failure category. The predicate matches only when both appear in the same file; either one can also appear alone in a passing run. It's a case-sensitive substring search, so text inside a longer word also matches. The control doesn't interpret meaning, calculate values, or use pattern rules (regular expressions).

`RELEASED` occurs inside `UNRELEASED`, so a config that uses `RELEASED` also matches a hold stamp written as `UNRELEASED` when the other literal is present. Measure this limit of a pure text check.

![Derive two exact literals from your notes; the supplied condition checks their co-occurrence, not the meaning or truth of the run.](figures/m06-predicate-boundary.png)

*Derive two exact literals from your notes; the supplied condition checks their co-occurrence, not the meaning or truth of the run.*

<details markdown="1">
<summary>Figure text</summary>

Test text, not meaning.

1. Your failure notes supply two different exact strings: Literal A and Literal B.
2. Each literal is searched in One run file as a Case-sensitive substring, so a literal inside a longer word still counts as present and can cause a false positive.
3. The two presence checks meet at all_present, which requires both.
4. Two outcomes: Either absent, or Both present.
5. Both present is Not release authority.

Separately, Semantic judgment stays a note: what the run means, and whether its claims are true, stays in your retained failure notes and never enters the check.

</details>

Start from the template:

**Terminal: Bash or zsh, ordinary user.**

```bash
cp "$W/shared/controls/predicate.template.json" "$W/out/predicate.json"
```

**Terminal: PowerShell, ordinary user.**

```powershell
Copy-Item "$W\shared\controls\predicate.template.json" -Destination "$W\out\predicate.json"
```


**Expected:** $W/out/predicate.json exists and matches the template.

**Stop:** The copy fails or the file isn't there.

**Recovery:** Check the path and permissions. Make sure W points to your work folder and that shared/controls/predicate.template.json exists in it, then run the copy command again.

Edit `$W/out/predicate.json` so that `all_present` holds your two strings. The finished file must look like `{"all_present": ["first text", "second text"]}` with your own two strings.

Then freeze a copy. The checks use this frozen copy, not the file you edit:

**Terminal: Bash or zsh, ordinary user.**

```bash
CFG="$W/out/predicate-frozen.json"
"$PY" - "$W/out/predicate.json" "$CFG" <<'PY'
from pathlib import Path
import hashlib, sys
source, target = map(Path, sys.argv[1:])
try:
    raw = source.read_bytes()
    with target.open('xb') as handle:
        handle.write(raw)
except OSError as exc:
    raise SystemExit('HOLD: ' + str(exc))
print('FROZEN', target.name, hashlib.sha256(raw).hexdigest())
PY
```

**Terminal: PowerShell, ordinary user.**

```powershell
$CFG = "$W\out\predicate-frozen.json"
@'
from pathlib import Path
import hashlib, sys
source, target = map(Path, sys.argv[1:])
try:
    raw = source.read_bytes()
    with target.open('xb') as handle:
        handle.write(raw)
except OSError as exc:
    raise SystemExit('HOLD: ' + str(exc))
print('FROZEN', target.name, hashlib.sha256(raw).hexdigest())
'@ | & $PY - "$W\out\predicate.json" "$CFG"
if ($LASTEXITCODE -ne 0) { throw 'Freeze held; preserve the attempt.' }
```

**Expected:** One line: `FROZEN predicate-frozen.json` followed by a 64-character digest. Step 5 checks the content.

**Stop:** A line starting `HOLD:`. Either the frozen file already exists, or a file can't be read or written.

**Recovery:** Keep the earlier frozen file and its results. To change the literals, use the copy, edit, and freeze recovery in step 5; never overwrite a frozen file. `CFG` names the frozen configuration that the checks and the stretch use.


## 5. Run the supplied control

Confirm the control refuses a malformed config using the unedited template. Then check your frozen configuration on a known-bad run, a known-good run, and a missing file.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$W/shared/controls/predicate.py" "$W/shared/checks/known-bad.txt" --config "$W/shared/controls/predicate.template.json"
echo "exit $?"
```


**Expected:** The control prints `HOLD: malformed config` to standard error, and the exit line is `exit 1`.

**Stop:** The exit isn't 1, or the output contains `MATCH` or `PASS`.

**Recovery:** Check that the command points at the unedited template and that the paths are quoted. If you edited a copy, give it a new name.

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$W\shared\controls\predicate.py" "$W\shared\checks\known-bad.txt" --config "$W\shared\controls\predicate.template.json"
Write-Output "exit $LASTEXITCODE"
```



**Expected:** The control prints `HOLD: malformed config` to standard error, and the exit line is `exit 1`.

**Stop:** The exit isn't 1, or the output contains `MATCH` or `PASS`.

**Recovery:** Check that the command points at the unedited template and that the paths are quoted. If you edited a copy, give it a new name.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$W/shared/controls/predicate.py" "$W/shared/checks/known-bad.txt" --config "$CFG"; echo "exit $?"
"$PY" "$W/shared/controls/predicate.py" "$W/shared/checks/known-good.txt" --config "$CFG"; echo "exit $?"
"$PY" "$W/shared/controls/predicate.py" "$W/out/not-created.txt" --config "$CFG"; echo "exit $?"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$W\shared\controls\predicate.py" "$W\shared\checks\known-bad.txt" --config "$CFG"; Write-Output "exit $LASTEXITCODE"
& $PY "$W\shared\controls\predicate.py" "$W\shared\checks\known-good.txt" --config "$CFG"; Write-Output "exit $LASTEXITCODE"
& $PY "$W\shared\controls\predicate.py" "$W\out\not-created.txt" --config "$CFG"; Write-Output "exit $LASTEXITCODE"
```

**Expected:**

- The known-bad check prints `MATCH: both literals present`, then `exit 1`.
- The known-good check prints `PASS: at least one literal absent`, then `exit 0`.
- The missing path prints `HOLD: missing input`, then `exit 1`.

The exit lines read `exit 1`, `exit 0`, `exit 1` in that order.

![MATCH and HOLD both exit 1; use the output text to distinguish a matched condition from a run the control could not decide.](figures/m06-control-boundaries.png)

*MATCH and HOLD both exit 1; use the output text to distinguish a matched condition from a run the control could not decide.*

<details markdown="1">
<summary>Figure text</summary>

Read the result, not just the exit. Four separate cases, each an input with its output and exit code:

- Known bad: `MATCH: both literals present`, `exit 1`.
- Known good: `PASS: at least one literal absent`, `exit 0`.
- Missing run: `HOLD: missing input`, `exit 1`.
- Malformed config: `HOLD: malformed config`, `exit 1`.

The three `exit 1` cases share one exit code: HOLD also exits 1. The exit code alone cannot tell a match from a refusal; read the output line.

</details>

Copy the three command lines and their output into `$E/predicate-results.md`.

**Stop:** Known-bad exits 0 or known-good exits 1. Your literals don't separate the cases you chose.

**Recovery:** Keep the frozen configuration and the results. Make a new working copy with the command below; it doesn't run the predicate.

**Terminal: Bash or zsh, ordinary user.**

```bash
PF="$W/out/predicate-revised-$(date -u +%Y%m%dT%H%M%SZ)-$$"
P="$PF.json"
"$PY" - "$W/out/predicate-frozen.json" "$P" <<'PY'
from pathlib import Path
import sys
source, target = map(Path, sys.argv[1:])
try:
    with target.open('xb') as handle:
        handle.write(source.read_bytes())
except OSError as exc:
    raise SystemExit('HOLD: ' + str(exc))
print('EDIT THIS WORKING COPY:', target)
PY
```

**Terminal: PowerShell, ordinary user.**

```powershell
$PF = "$W\out\predicate-revised-$([guid]::NewGuid().ToString('N'))"
$P = "$PF.json"
@'
from pathlib import Path
import sys
source, target = map(Path, sys.argv[1:])
try:
    with target.open('xb') as handle:
        handle.write(source.read_bytes())
except OSError as exc:
    raise SystemExit('HOLD: ' + str(exc))
print('EDIT THIS WORKING COPY:', target)
'@ | & $PY - "$W\out\predicate-frozen.json" "$P"
if ($LASTEXITCODE -ne 0) { throw 'Revised copy held; preserve the attempt.' }
```

**Expected:** The terminal prints `EDIT THIS WORKING COPY:` and the new copy's path. The original frozen file is unchanged.

**Stop:** The copy fails, or it would replace an existing file.

**Recovery:** Keep that attempt and choose a new working filename. Don't remove the original.

Open the printed `P` file. Change the two literals based on the sample and the failed check, then save it. Keep this terminal open while you edit. Then freeze the revised copy:

**Terminal: Bash or zsh, ordinary user.**

```bash
CFG="$PF-frozen.json"
"$PY" - "$P" "$CFG" <<'PY'
from pathlib import Path
import hashlib, sys
source, target = map(Path, sys.argv[1:])
try:
    raw = source.read_bytes()
    with target.open('xb') as handle:
        handle.write(raw)
except OSError as exc:
    raise SystemExit('HOLD: ' + str(exc))
print('FROZEN', target.name, hashlib.sha256(raw).hexdigest())
PY
```

**Terminal: PowerShell, ordinary user.**

```powershell
$CFG = "$PF-frozen.json"
@'
from pathlib import Path
import hashlib, sys
source, target = map(Path, sys.argv[1:])
try:
    raw = source.read_bytes()
    with target.open('xb') as handle:
        handle.write(raw)
except OSError as exc:
    raise SystemExit('HOLD: ' + str(exc))
print('FROZEN', target.name, hashlib.sha256(raw).hexdigest())
'@ | & $PY - "$P" "$CFG"
if ($LASTEXITCODE -ne 0) { throw 'Revised freeze held; preserve the attempt.' }
```

**Expected:** The terminal prints the new frozen file's name and digest. `CFG` now points to this revision, and the earlier attempt is unchanged.

**Stop:** Freezing fails, one of the earlier files changes, or the two literals aren't the revision you intended.

**Recovery:** Keep the failure and start another separate working copy.

If you froze a revised config, rerun the three checks above with the new `CFG`. Continue only when known-bad matches, known-good passes, and missing input holds. Don't edit `predicate.py` itself.

## 6. Finish the handoff

Decide whether to add this control to the workflow. Base the decision only on the sixteen runs and the three checks. Then write `$E/handoff.md`:

```markdown
# Module 6 handoff

Sample rule:
Count total:
Two literals chosen:
Known-bad result:
Known-good result:
Missing result:
Scope of the control:
Decision (adopt, revise, or hold) and the sampled evidence that bounds it:
What the next person should read first in the full corpus:
```

A classmate who didn't watch you work should be able to rebuild your result and understand the control's limits without help from you.

In the handoff, say which observed failures the predicate targets and which it misses. A **false positive** is a match on a run that doesn't have the failure; a **false negative** is a run that has the failure but doesn't match. List any you found in the runs you checked, with their run IDs and how many runs you checked. If you haven't measured a limit, don't report it as a zero error rate.

## Stretch: two preregistered configurations on the held-out runs

<details class="rf-stretch" markdown="1">
<summary>Optional stretch: measure the tradeoff on R-017 through R-080</summary>

Once you have a frozen config that works on the sample, make two working copies of it in $W/out/:

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" - "$CFG" "$W/out" <<'PY'
from pathlib import Path
import sys
source, out = map(Path, sys.argv[1:])
targets = [out/'stretch-a.json', out/'stretch-b.json']
try:
    if any(p.exists() or p.is_symlink() for p in targets):
        raise SystemExit('HOLD: stretch working copies already exist; preserve them')
    raw = source.read_bytes()
    for target in targets:
        with target.open('xb') as handle:
            handle.write(raw)
except OSError as exc:
    raise SystemExit('HOLD: ' + str(exc))
print('STRETCH WORKING COPIES READY')
PY
```

**Terminal: PowerShell, ordinary user.**

```powershell
@'
from pathlib import Path
import sys
source, out = map(Path, sys.argv[1:])
targets = [out/'stretch-a.json', out/'stretch-b.json']
try:
    if any(p.exists() or p.is_symlink() for p in targets):
        raise SystemExit('HOLD: stretch working copies already exist; preserve them')
    raw = source.read_bytes()
    for target in targets:
        with target.open('xb') as handle:
            handle.write(raw)
except OSError as exc:
    raise SystemExit('HOLD: ' + str(exc))
print('STRETCH WORKING COPIES READY')
'@ | & $PY - "$CFG" "$W\out"
if ($LASTEXITCODE -ne 0) { throw 'Stretch working copies held; preserve the attempt.' }
```


**Expected:** The terminal prints `STRETCH WORKING COPIES READY`, and both stretch files are copies of the frozen config.

**Stop:** A copy doesn't contain the exact two literals from your frozen config.

**Recovery:** Keep any existing stretch work. Make the copies again from the frozen configuration in `CFG` that passed the checks. Give a new attempt new output names instead of overwriting.

Edit $W/out/stretch-a.json and $W/out/stretch-b.json so they use two different pairs of literals. Then freeze both, and don't edit them afterward.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" - "$W/out" <<'PY'
from pathlib import Path
import hashlib, sys
out = Path(sys.argv[1])
pairs = [(out/f'stretch-{name}.json', out/f'stretch-{name}-frozen.json') for name in ('a', 'b')]
try:
    if any(target.exists() or target.is_symlink() for _, target in pairs):
        raise SystemExit('HOLD: frozen stretch configuration exists; preserve it')
    contents = [source.read_bytes() for source, _ in pairs]
    for (_, target), raw in zip(pairs, contents):
        with target.open('xb') as handle:
            handle.write(raw)
        print('FROZEN', target.name, hashlib.sha256(raw).hexdigest())
except OSError as exc:
    raise SystemExit('HOLD: ' + str(exc))
PY
```

**Expected:** Two lines, `FROZEN stretch-a-frozen.json` and `FROZEN stretch-b-frozen.json`, each followed by a 64-character digest.

**Stop:** The copy fails, or the files aren't two different two-literal configs.

**Recovery:** Keep any partial or earlier freeze. For a new pair, choose new frozen filenames and use them in that pair's commands; never overwrite a preregistered configuration.

**Terminal: PowerShell, ordinary user.**

```powershell
@'
from pathlib import Path
import hashlib, sys
out = Path(sys.argv[1])
pairs = [(out/f'stretch-{name}.json', out/f'stretch-{name}-frozen.json') for name in ('a', 'b')]
try:
    if any(target.exists() or target.is_symlink() for _, target in pairs):
        raise SystemExit('HOLD: frozen stretch configuration exists; preserve it')
    contents = [source.read_bytes() for source, _ in pairs]
    for (_, target), raw in zip(pairs, contents):
        with target.open('xb') as handle:
            handle.write(raw)
        print('FROZEN', target.name, hashlib.sha256(raw).hexdigest())
except OSError as exc:
    raise SystemExit('HOLD: ' + str(exc))
'@ | & $PY - "$W\out"
if ($LASTEXITCODE -ne 0) { throw 'Stretch freeze held; preserve the attempt.' }
```

**Expected:** Two lines, `FROZEN stretch-a-frozen.json` and `FROZEN stretch-b-frozen.json`, each followed by a 64-character digest.

**Stop:** The copy fails, or the files aren't two different two-literal configs.

**Recovery:** Keep any partial or earlier freeze. For a new pair, choose new frozen filenames and use them in that pair's commands; never overwrite a preregistered configuration.

The **held-out runs**, R-017 through R-080, weren't used to choose the original literals. Read those 64 runs and write your predictions in $W/out/stretch-prediction.md before you run either configuration or open the public labels. For each run, predict whether `promotion_failure` is true (a receipt was treated as a release) and whether each configuration will return MATCH or PASS.

Create the prediction skeleton below and fill in every value from your reading of the runs. Use `true` or `false` for `promotion_failure` and `MATCH` or `PASS` for each configuration. Keep exactly one row per run, in ID order. The command won't overwrite an existing file, but nothing stops later edits; the freeze step that follows records the finished file before you open any results or labels.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" -c '
from pathlib import Path
import sys
p = Path(sys.argv[1]) / "out" / "stretch-prediction.md"
lines = []
for n in range(17, 81):
    rid = f"R-{n:03d}"
    lines.append(f"{rid} promotion_failure=? a=? b=?")
with p.open("x", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")
print("wrote", len(lines))
' "$W"
```

**Terminal: PowerShell, ordinary user.**

```powershell
@'
from pathlib import Path
import sys
p = Path(sys.argv[1]) / "out" / "stretch-prediction.md"
lines = []
for n in range(17, 81):
    rid = f"R-{n:03d}"
    lines.append(f"{rid} promotion_failure=? a=? b=?")
with p.open("x", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")
print("wrote", len(lines))
'@ | & $PY - "$W"
if ($LASTEXITCODE -ne 0) { throw 'Prediction file creation held; preserve the attempt.' }
```

**Expected:** `wrote 64`.

**Stop:** `FileExistsError`: the file already exists.

**Recovery:** Keep the existing file and fill in its values instead of creating another.

Check all sixty-four completed predictions and freeze their hash. Counting rows isn't enough, because a row that still holds a placeholder counts too.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" - "$W/out/stretch-prediction.md" <<'PY'
from pathlib import Path
import hashlib, re, sys
p = Path(sys.argv[1])
try:
    raw = p.read_bytes()
    lines = raw.decode('utf-8').splitlines()
    rows = [re.fullmatch(r'R-(\d{3}) promotion_failure=(true|false) a=(MATCH|PASS) b=(MATCH|PASS)', line) for line in lines]
    if any(row is None for row in rows) or [int(row[1]) for row in rows] != list(range(17, 81)):
        raise ValueError('complete every prediction exactly once, in R-017 through R-080 order')
    digest = hashlib.sha256(raw).hexdigest()
    with p.with_suffix('.sha256').open('x', encoding='ascii') as frozen:
        frozen.write(digest + '\n')
except (OSError, UnicodeError, ValueError) as exc:
    raise SystemExit('HOLD: ' + str(exc))
print('PREDICTIONS 64 FROZEN', digest)
PY
```

**Terminal: PowerShell, ordinary user.**

```powershell
@'
from pathlib import Path
import hashlib, re, sys
p = Path(sys.argv[1])
try:
    raw = p.read_bytes()
    lines = raw.decode('utf-8').splitlines()
    rows = [re.fullmatch(r'R-(\d{3}) promotion_failure=(true|false) a=(MATCH|PASS) b=(MATCH|PASS)', line) for line in lines]
    if any(row is None for row in rows) or [int(row[1]) for row in rows] != list(range(17, 81)):
        raise ValueError('complete every prediction exactly once, in R-017 through R-080 order')
    digest = hashlib.sha256(raw).hexdigest()
    with p.with_suffix('.sha256').open('x', encoding='ascii') as frozen:
        frozen.write(digest + '\n')
except (OSError, UnicodeError, ValueError) as exc:
    raise SystemExit('HOLD: ' + str(exc))
print('PREDICTIONS 64 FROZEN', digest)
'@ | & $PY - "$W\out\stretch-prediction.md"
if ($LASTEXITCODE -ne 0) { throw 'Prediction freeze held; preserve the attempt.' }
```

**Expected:** `PREDICTIONS 64 FROZEN` and a SHA-256 value appear, and a new file, `stretch-prediction.sha256`, sits beside the completed prediction.

**Stop:** A row is still a placeholder, duplicated, missing, or malformed; the hash file already exists; or you've opened results or labels.

**Recovery:** Before the first freeze, fill in the missing predictions from the run texts and run the check again. If a freeze already exists, keep it. Once you've opened results or labels, mark any new prediction as post-result analysis instead of replacing the original.

Then run each frozen configuration on every held-out run, first stretch-a-frozen.json and then stretch-b-frozen.json:

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" - "$W" <<'PY'
from pathlib import Path
import hashlib, json, subprocess, sys, uuid
w = Path(sys.argv[1])
prediction = w / "out/stretch-prediction.md"
prediction_hash = hashlib.sha256(prediction.read_bytes()).hexdigest()
if prediction_hash != prediction.with_suffix(".sha256").read_text(encoding="ascii").strip():
    raise SystemExit("HOLD: predictions differ from their pre-result freeze")
attempt = uuid.uuid4().hex
for label in ("a", "b"):
    config = w / f"out/stretch-{label}-frozen.json"
    config_hash = hashlib.sha256(config.read_bytes()).hexdigest()
    output = w / f"out/stretch-{label}-results-{attempt}.jsonl"
    with output.open("x", encoding="utf-8") as evidence:
        for number in range(17, 81):
            run_id = f"R-{number:03d}"
            source = w / f"shared/corpus/{run_id}.md"
            result = subprocess.run(
                [sys.executable, str(w / "shared/controls/predicate.py"),
                 str(source), "--config", str(config)],
                capture_output=True, text=True)
            row = {"run_id": run_id, "config_sha256": config_hash, "prediction_sha256": prediction_hash,
                   "exit_code": result.returncode,
                   "stdout": result.stdout, "stderr": result.stderr}
            evidence.write(json.dumps(row, sort_keys=True) + "\n")
            evidence.flush()
            valid = ((result.returncode == 1 and result.stdout.strip() == "MATCH: both literals present")
                     or (result.returncode == 0 and result.stdout.strip() == "PASS: at least one literal absent"))
            if not valid or result.stderr or hashlib.sha256(config.read_bytes()).hexdigest() != config_hash:
                raise SystemExit(f"HOLD: {run_id} did not produce a valid classification under the frozen config; inspect the retained row")
    print(f"COMPLETE: configuration {label}; R-017 through R-080; {output}")
PY
```

**Terminal: PowerShell, ordinary user.**

```powershell
@'
from pathlib import Path
import hashlib, json, subprocess, sys, uuid
w = Path(sys.argv[1])
prediction = w / "out/stretch-prediction.md"
prediction_hash = hashlib.sha256(prediction.read_bytes()).hexdigest()
if prediction_hash != prediction.with_suffix(".sha256").read_text(encoding="ascii").strip():
    raise SystemExit("HOLD: predictions differ from their pre-result freeze")
attempt = uuid.uuid4().hex
for label in ("a", "b"):
    config = w / f"out/stretch-{label}-frozen.json"
    config_hash = hashlib.sha256(config.read_bytes()).hexdigest()
    output = w / f"out/stretch-{label}-results-{attempt}.jsonl"
    with output.open("x", encoding="utf-8") as evidence:
        for number in range(17, 81):
            run_id = f"R-{number:03d}"
            source = w / f"shared/corpus/{run_id}.md"
            result = subprocess.run(
                [sys.executable, str(w / "shared/controls/predicate.py"),
                 str(source), "--config", str(config)],
                capture_output=True, text=True)
            row = {"run_id": run_id, "config_sha256": config_hash, "prediction_sha256": prediction_hash,
                   "exit_code": result.returncode,
                   "stdout": result.stdout, "stderr": result.stderr}
            evidence.write(json.dumps(row, sort_keys=True) + "\n")
            evidence.flush()
            valid = ((result.returncode == 1 and result.stdout.strip() == "MATCH: both literals present")
                     or (result.returncode == 0 and result.stdout.strip() == "PASS: at least one literal absent"))
            if not valid or result.stderr or hashlib.sha256(config.read_bytes()).hexdigest() != config_hash:
                raise SystemExit(f"HOLD: {run_id} did not produce a valid classification under the frozen config; inspect the retained row")
    print(f"COMPLETE: configuration {label}; R-017 through R-080; {output}")
'@ | & $PY - $W
if ($LASTEXITCODE -ne 0) { throw 'Held-out comparison stopped; keep the partial evidence.' }
```

**Expected:** Two new JSONL files each hold one row for each of the 64 runs, R-017 through R-080, with the frozen configuration's hash, the exit status, stdout, and stderr. Both `COMPLETE` lines show their output paths, and the command exits 0. Each time you run the command, its two result files get a new shared suffix.

**Stop:** A result file already exists, a configuration changes, or any run produces HOLD or another error instead of MATCH or PASS. A missing input doesn't count as a match, and a partial result file isn't a finished comparison.

**Recovery:** Keep all partial results and the first failure. Fix only the path or input problem you diagnosed, then run the command again; it creates new result filenames and leaves the earlier attempt in place. If you change a configuration, preregister new predictions and keep the earlier comparison separate.

After the runs, open the public practice labels:

**Terminal: Bash or zsh, ordinary user.**

```bash
cat "$W/shared/checks/held-out-truth.json"
```

**Terminal: PowerShell, ordinary user.**

```powershell
Get-Content "$W\shared\checks\held-out-truth.json"
```

**Expected:** The JSON lists each held-out run, R-017 through R-080, with `promotion_failure` set to true or false and a short note.

**Stop:** The file is missing or unreadable.

**Recovery:** Check the path under the work copy and run the command again.

For each frozen configuration, compare its matches and misses with the public labels and report its false positives and false negatives out of all 64 runs. Compare the two configurations' errors, and don't drop a run because it's inconvenient. Explain what `RELEASED` matching inside `UNRELEASED` shows about the limits of a pure text check.

Don't resample runs to improve the numbers. The public labels are practice data only.

</details>

## Before you stop

Check that:

- the sample rule existed before you read any outcome text;
- you wrote first-failure notes for all sixteen sample runs before any counts;
- the counts add up to sixteen;
- the frozen config contains exactly two distinct nonempty strings;
- known-bad exits 1 with MATCH, known-good exits 0 with PASS, and missing input prints `HOLD: missing input`;
- you didn't write a second checker;
- the work stayed inside the fictional class case;
- if you did the stretch, you froze your predictions before you opened the held-out labels.
