# Module 6 · Improve from observed failures

Turn a repeated failure in Blue Gauge's practice records into a check that can flag the same text condition in another run. Use your source checks and preserved failure evidence to derive a **predicate**: a yes-or-no condition the supplied control can decide mechanically. Configure it with two exact pieces of text, then check known-bad, known-good, and missing input and record its limits.

The eighty records are authored practice runs about oxygen cylinders moving from East Yard to Clinic O-2. They are not workplace observations or measurements of current model reliability. Your work stays inside the fictional class case and authorizes no real movement.

Plan for 3 facilitated hours, including 2 hours of practice. This is a planning allowance, not a measured completion guarantee.

## Copy a work folder

Use the verified checkout and Python from setup. The commands name the checkout at `$HOME/Documents/AIHB_OCT_2026` as `R` and select the full path to Python 3.12 or newer as `PY`. `M` names the module sources. `RUN` gives this attempt a unique name; `W` holds its work files and `E` its evidence outside the checkout. Use the command blocks for your terminal throughout.

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

**Expected:** The variables are defined with R as the checkout root, PY as the absolute path to a Python >= 3.12 interpreter, and W/E under a fresh RUN.

**Stop:** PY is empty or does not point to a 3.12 or newer interpreter.

**Recovery:** Correct the Python selection in a new terminal following the setup instructions and repeat the assignments.

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

**Expected:** The E directory exists.

**Stop:** The mkdir fails due to permissions.

**Recovery:** Use a writable path under $HOME/course-evidence and repeat the mkdir with absolute path.

**Terminal: PowerShell, ordinary user.**

```powershell
New-Item -ItemType Directory -Force -Path "$E" | Out-Null
```

**Expected:** The E directory exists.

**Stop:** The command fails due to permissions.

**Recovery:** Use a writable path under $HOME/course-evidence and repeat the New-Item with absolute path.

Use the shared prepare script with its absolute path under R so the work folder (W) is outside the checkout and does not overwrite anything. Prepare exactly once per attempt.

**Terminal: Bash or zsh, ordinary user.**

```bash
cd "$R" && "$PY" "$R/shared/prepare_work.py" 06 "$W"
```

**Terminal: PowerShell, ordinary user.**

```powershell
Set-Location -LiteralPath "$R"; & $PY "$R\shared\prepare_work.py" 06 "$W"
```

**Expected:** `PASS: created` followed by the full work path, then two suggested next commands, one for each shell. Do not run them yet: they list the corpus, and you freeze the sample rule first. The folder contains `shared/controls/`, `shared/corpus/` with the eighty runs, and `shared/checks/`.

**Stop:** If the destination already exists, prepare refuses with HOLD.

**Recovery:** Open a new terminal and paste the variable block from the start of this lab, which creates a new `RUN` and so a new `W`; then repeat the prepare command.

After the prepare step, create the output directory once under the absolute W:

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

**Recovery:** Use a writable path under `$HOME/course-evidence` and repeat the command with the absolute path.

Every later command uses absolute paths under `W`, so you never need to change directory. Do not copy any extra checker into the work folder.

### If you open a new terminal

Every command on this page uses the variables from the block above, and a terminal forgets them when it closes. Run this block in any new terminal to return to the same attempt instead of preparing a second one. It reads the attempt identifier that the first block saved.

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

**Recovery:** A different identifier means a later attempt overwrote the saved marker; set `RUN` by hand to the value you recorded and run the block again. A missing folder means the attempt was never prepared, so prepare it with the first block.

## Timebox

| Work | Time |
|---|---:|
| Freeze the sample rule | 15 minutes |
| Read the sample runs and write first-failure notes | 45 minutes |
| Reconcile counts to the sample size | 20 minutes |
| Infer the two literals and write the config | 20 minutes |
| Freeze the config copy and run the three controls | 25 minutes |
| Handoff | 15 minutes |

The table allocates 140 minutes within the three-hour session, including at least two hours of your own practice. Use the remaining time for preparation and facilitated discussion; the allocations do not predict how quickly you will finish.

## 1. Freeze the sample rule first

Write `sample-rule.md` before you open any run that shows an outcome or a stamp result.

This makes the sample **outcome-blind**: you fix membership without choosing records because they passed or failed. Use the declaration below only if you have not opened the run files. If you have already seen outcomes, preserve that fact; a fresh folder cannot make them unseen. Record the earlier exposure rather than claim an outcome-blind attempt.

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

**Expected:** The file `sample-rule.md` is created with the three headings.

**Stop:** The cat fails or the file is not created.

**Recovery:** Check permissions and repeat the cat with absolute path.

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

**Expected:** The file `sample-rule.md` is created with the three headings.

**Stop:** The command fails or the file is not created.

**Recovery:** Check permissions and repeat the Out-File with absolute path.

Record the rule's fingerprint beside it, so the reading that follows can be shown to have come after the rule.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" -c "import hashlib,sys; from pathlib import Path; src, dst = map(Path, sys.argv[1:]); digest = hashlib.sha256(src.read_bytes()).hexdigest(); handle = dst.open('x', encoding='utf-8'); handle.write(digest + '\n'); handle.close(); print(digest)" "$W/sample-rule.md" "$E/sample-rule.sha256"
```

**Expected:** A 64-character digest, written to a new file `E/sample-rule.sha256`. The command exits 0.

**Stop:** The sample-rule file is missing, the digest file already exists, or you have already opened a run and seen a stamp.

**Recovery:** Leave this attempt in place. Do not delete the digest or the run files. If the failure occurred before you saw outcomes, open a new terminal, repeat the prepare block, and write the rule before opening any run. If you already saw outcomes, record that exposure and do not claim that another attempt is outcome-blind.

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY -c "import hashlib,sys; from pathlib import Path; src, dst = map(Path, sys.argv[1:]); digest = hashlib.sha256(src.read_bytes()).hexdigest(); handle = dst.open('x', encoding='utf-8'); handle.write(digest + '\n'); handle.close(); print(digest)" "$W\sample-rule.md" "$E\sample-rule.sha256"
Write-Output "exit $LASTEXITCODE"
```

**Expected:** A 64-character digest, written to a new file `E\sample-rule.sha256`. The command exits 0.

**Stop:** The sample-rule file is missing, the digest file already exists, or you have already opened a run and seen a stamp.

**Recovery:** Leave this attempt in place. Do not delete the digest or the run files. If the failure occurred before you saw outcomes, open a new terminal, repeat the prepare block, and write the rule before opening any run. If you already saw outcomes, record that exposure and do not claim that another attempt is outcome-blind.

### If you must start a new attempt

Open a new terminal and paste the variable block from the start of this lab, which creates a new `RUN`. Then run:

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

**Expected:** The preparer creates a fresh work folder at the new path. Both `W/out` and the new sibling evidence directory `E` exist before you record the digest.

**Stop:** The prepare holds if the chosen destination already exists.

**Recovery:** Select a path that does not exist yet (use a new terminal with new RUN) and repeat the prepare command.

If no outcomes were opened, recreate `sample-rule.md` and repeat the digest step with the new W and E. If outcomes were opened, retain that exposure in the attempt record and do not reuse the declaration that you have not seen them. A rerun can check the control, but cannot establish an outcome-blind first reading.

## 2. First-failure notes before categories


Open the sixteen sample files under `shared/corpus/`. For each run, write one first-failure note in `$E/first-failures.md` before you write any category tally.

Name the earliest concrete problem you can support from that run's text, with the line or passage that shows it. Do not start with a category name. If you find no failure, record that observation instead of inventing one. Keep uncertain cases explicit.

**Expected:** The file `first-failures.md` contains sixteen entries, one per sample run. Each begins with the run identifier and records the earliest supported problem, an unresolved observation, or that no failure was found.

**Stop:** If you wrote a category count before every run has its note, the counts are not evidence.

**Recovery:** Keep the notes you have, add the missing ones, and only then write or revise the counts file.

## 3. Then tally categories

After all sixteen notes exist, group the observed failures by what went wrong and write `$E/counts.md`. Keep each run identifier attached to its category so another reader can reconcile the counts with the notes. Use the pass, fail, and other totals below to account for every run once.

```markdown
# Counts

pass (run IDs):
fail by category:
  <category>: <run IDs>
other (run IDs):
total: 16
revisions to category names:
```

The total must be 16. Each category count must agree with its listed runs, and pass, fail, and other must add to the total. If they do not, record `HOLD` and identify the missing or double-counted run. State one conclusion supported by the failure categories in this sample; do not generalize its frequency to workplace use or current models.

Keep the original first-failure notes visible next to any revised category label.

**Expected:** The counts file shows totals that add to 16, and the first-failure notes remain the source of truth.

**Stop:** The totals add to any number other than 16.

**Recovery:** Find the run that is missing or counted twice by comparing with `first-failures.md`, correct the counts, and keep the earlier version.

## 4. Infer two literals and configure the supplied control

Choose the two exact text strings that mark your repeated failure, and lock them so the checks run against a fixed version. Read `shared/controls/PREDICATE_SPEC.md`.

The control takes one run file and a configuration file:

`predicate.py <run-file> --config <predicate.json>`

The configuration is a JSON object with exactly one key, `all_present`. Its value is a list of exactly two different nonempty strings. Those two strings are the literals.

Choose the literals from your first-failure notes to identify one repeated failure category. A **literal** is an exact piece of text. The predicate matches only when both literals occur in the same file; either one may also occur alone in a passing run. This is a substring search, so text inside a longer word also matches. Capital letters and lowercase letters are different. The control does not interpret meaning, calculate values, or use pattern rules called regular expressions.

The characters `RELEASED` occur inside `UNRELEASED`. A config that uses `RELEASED` therefore matches a hold stamp written as `UNRELEASED` when the other literal is also present. This is a limit of a pure text check. Measure that limit honestly.

Start from the template:

**Terminal: Bash or zsh, ordinary user.**

```bash
cp "$W/shared/controls/predicate.template.json" "$W/out/predicate.json"
```

**Terminal: PowerShell, ordinary user.**

```powershell
Copy-Item "$W\shared\controls\predicate.template.json" -Destination "$W\out\predicate.json"
```


**Expected:** $W/out/predicate.json exists with the template content.

**Stop:** If the copy fails or the file is not present, check the path and permissions.

**Recovery:** Ensure you are in the work folder (W) and that shared/controls/predicate.template.json exists in the copied tree, then repeat the copy command with absolute paths.

Edit `$W/out/predicate.json` so that `all_present` holds your two strings. The finished file looks like `{"all_present": ["first text", "second text"]}` with your own two texts and nothing else.

Then copy the file you will actually use:

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

**Expected:** One line: `FROZEN predicate-frozen.json` and a 64-character digest. The freeze checks nothing about the content; step 5 tests it.

**Stop:** A line starting `HOLD:`: the frozen file already exists, or a file cannot be read or written.

**Recovery:** Keep the rejected frozen file and its results. Use the separate copy, edit, and freeze recovery below; never overwrite a frozen attempt. `CFG` names the frozen configuration used by the checks and the stretch.


## 5. Run the supplied control

First confirm that the control refuses a malformed configuration: the unedited template has no literals, so it must hold. Then check your frozen configuration on a known-bad run, a known-good run, and a missing file.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$W/shared/controls/predicate.py" "$W/shared/checks/known-bad.txt" --config "$W/shared/controls/predicate.template.json"
echo "exit $?"
```


**Expected:** Standard error prints `HOLD: malformed config`. The echoed exit is 1.

**Stop:** The exit is not 1, or the output contains `MATCH` or `PASS`.

**Recovery:** Confirm the unedited template copy and the quoted paths; use a new name for any edited copy.

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$W\shared\controls\predicate.py" "$W\shared\checks\known-bad.txt" --config "$W\shared\controls\predicate.template.json"
Write-Output "exit $LASTEXITCODE"
```



**Expected:** Standard error prints `HOLD: malformed config`. The exit line is `exit 1`.

**Stop:** The exit is not 1, or the output contains `MATCH` or `PASS`.

**Recovery:** Confirm the unedited template copy and the quoted paths; use a new name for any edited copy.

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

Copy the three command lines and their output into `$E/predicate-results.md`.

**Stop:** If known-bad exits 0 or known-good exits 1, the literals do not separate the cases you chose.

**Recovery:** Preserve the frozen configuration and its failed separation. Create a new working copy; this command does not run the predicate.

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

**Expected:** A new working configuration is printed; the original frozen file is unchanged.

**Stop:** Copying fails or an existing destination would be replaced.

**Recovery:** Retain that attempt and choose a fresh working filename. Do not remove the original.

Open the printed `P` file in your editor, change the two literals using the sample and the failed control, and save it. Keep this terminal open while you edit. Then freeze the revised copy:

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

**Expected:** The new frozen file and digest are printed. `CFG` now selects that revision without changing the earlier attempt.

**Stop:** Freezing fails, either prior file changes, or the two literals are not the intended revision.

**Recovery:** Preserve the failure and start another separate working copy. Repeat the three controls above with the new `CFG`; continue only when known-bad matches, known-good passes, and missing input holds.

Do not edit the predicate.py itself.

## 6. Finish the handoff

Decide whether this control should be added to the workflow. Base the decision only on the sixteen runs and the three checks. Then write `$E/handoff.md`:

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

A classmate who did not watch you work should be able to reconstruct the result and the limits of the control without coaching.

State which observed failures the predicate targets and which it cannot catch. A **false positive** is a match on a run without that failure; a **false negative** is a missed run that has it. Report any such cases in the records you checked, with their run IDs and the number checked. Do not describe an unmeasured limitation as a zero error rate.

## Stretch: two preregistered configurations on the held-out runs

<details class="rf-stretch" markdown="1">
<summary>Optional stretch: measure the tradeoff on R-017 through R-080</summary>

After you have a working frozen config for the sample, write two new configuration files in $W/out/ :

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


**Expected:** Both stretch files exist as copies of the frozen config.

**Stop:** If the copy does not preserve the exact two literals from your frozen config, start the stretch copies again from the frozen file.

**Recovery:** Preserve any existing stretch work. Use the successfully checked frozen configuration named by `CFG`, including a separately frozen repair when needed. A new attempt needs fresh output names, not overwritten copies.

Edit $W/out/stretch-a.json and $W/out/stretch-b.json to use two different pairs of literals. Freeze both (do not edit after).

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

**Stop:** The copy fails or the files are not distinct two-literal configs.

**Recovery:** Preserve any partial or earlier freeze. Choose fresh frozen filenames for a new pair and use those names in its commands; never overwrite a preregistered configuration.

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

**Stop:** The copy fails or the files are not distinct two-literal configs.

**Recovery:** Preserve any partial or earlier freeze. Choose fresh frozen filenames for a new pair and use those names in its commands; never overwrite a preregistered configuration.

The **held-out runs**, R-017 through R-080, were not used to choose the original literals. Read those 64 run texts and write predictions in $W/out/stretch-prediction.md before running either configuration or opening the public labels. For each run, predict whether `promotion_failure` is true, meaning a receipt was treated as a release, and whether each configuration will return MATCH or PASS.

Create the prediction skeleton below, then fill every value from your reading of the run files. Use `true` or `false` for `promotion_failure` and `MATCH` or `PASS` for each configuration. Keep exactly one row per run, in ID order. Creating the file exclusively prevents an accidental replacement; it does not prevent later edits. The following freeze records the completed bytes before any results or labels are opened.

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

**Recovery:** Keep the existing file; fill in its values rather than create another.

Validate all sixty-four completed predictions and freeze their hash. A count alone cannot distinguish predictions from unanswered placeholders.

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

**Expected:** `PREDICTIONS 64 FROZEN` and a SHA-256 value appear. `stretch-prediction.sha256` is a new file beside the completed prediction.

**Stop:** A placeholder, duplicate, missing or malformed row remains; the hash file already exists; or you have opened results or labels.

**Recovery:** Before the first freeze, complete the missing judgments from the run texts and repeat the check. Preserve an existing commitment. Once results or labels are open, mark any new prediction as post-result analysis rather than replacing the original.

Then run the configuration in stretch-a-frozen.json on every held-out file, then run the configuration in stretch-b-frozen.json on every held-out file:

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

**Expected:** Two new JSONL files each contain the 64 run IDs R-017 through R-080, their frozen configuration hash, exit status, stdout, and stderr. Both `COMPLETE` lines print their output paths; the command exits 0. Each invocation chooses a new shared suffix for its two result files.

**Stop:** A result file already exists, a configuration changes, or any invocation produces HOLD or another error instead of MATCH/PASS. A missing input is not a positive classification. A partial result file is not a completed comparison.

**Recovery:** Keep all partial results and the first failure. Repair only the diagnosed path or input problem, then repeat the command: it creates fresh result filenames without replacing the retained attempt. If you change a configuration, preregister new predictions and preserve the previous comparison separately.

After the runs, open the public practice labels:

**Terminal: Bash or zsh, ordinary user.**

```bash
cat "$W/shared/checks/held-out-truth.json"
```

**Terminal: PowerShell, ordinary user.**

```powershell
Get-Content "$W\shared\checks\held-out-truth.json"
```

**Stop:** The file is missing or unreadable.

**Recovery:** Confirm the path under the work copy and repeat the Get-Content.

**Expected:** The json shows promotion_failure true or false for each R-0NN without revealing your literals.

For each frozen configuration, report matches and misses against the public labels, including false positives and false negatives out of all 64 runs. Compare the two configurations' errors without dropping an inconvenient run. Explain what the UNRELEASED / RELEASED substring collision shows about the limit of a pure text check.

Do not resample runs to improve the numbers. The public labels are practice data only.

</details>

## Before you stop

Check that:

- the sample rule exists before any outcome text was read;
- first-failure notes exist for all sixteen sample runs before any counts;
- counts reconcile to sixteen;
- the frozen config contains exactly two distinct nonempty strings;
- known-bad exits 1 with MATCH, known-good exits 0 with PASS, and missing input prints `HOLD: missing input`;
- no second checker was written;
- the work remains inside the fictional class case;
- the two stretch predictions were written before the held-out labels were opened (if you did the stretch).
