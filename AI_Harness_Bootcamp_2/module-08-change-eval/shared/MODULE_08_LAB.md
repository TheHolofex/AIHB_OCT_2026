# Module 8 · Evaluate a change with variation controls

Decide whether a proposed change can be adopted without losing a required source check. Freeze the cases, configurations, and decision rule before you look at any outcomes. Compare every candidate with its baseline on the same cases. One hard-gate violation rejects a candidate, even when its other results look better.

The fictional movement carries heater-fuel cans from Ridge Depot to Clinic T-8 on vehicle SB-4. The forty case packets, each with three briefs, are practice data written in advance, not records of OpenRouter calls. Nothing here authorizes a real load sheet or movement.

A **hard gate** is a condition every result must meet. Keep the format check, the mass gate, and the time-zone gate separate: malformed output, an unsourced mass, or a missing time-zone label can each reject a candidate on its own. A **paired comparison** gives the baseline and the candidate the same source packet.

The core comparison checks fixed outputs written in advance, so running that check again tells you nothing about model variation. In the optional live comparison, repeated model calls show how outputs differ under the same conditions, so you can judge whether an apparent improvement holds up across attempts.

Plan for a little over two hours on Thursday (a rough estimate).

## Prepare a separate attempt

Create a new work folder and a separate evidence folder. Use the Python and checkout you verified in [setup](../../module-00-setup/README.md). These commands work from any folder and leave earlier attempts alone. `W` is your work folder; `E` holds your records outside it. Don't open the candidate briefs yet.

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
"$PY" "$R/shared/prepare_work.py" 08 "$W" &&
"$PY" -c "from pathlib import Path; import sys; Path(sys.argv[1]).mkdir(parents=True, exist_ok=False)" "$E"
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
& $PY -c "from pathlib import Path; import sys; Path(sys.argv[1]).mkdir(parents=True, exist_ok=False)" "$E"
```

**Expected:** `RUN=` and this attempt's identifier, then `PASS: created` followed by your work path, then two `Next` commands that display the policy file. The work folder contains `shared/cases`, `shared/controls`, `shared/baseline`, and the two scripts you'll run, `scripts/evaluate_pairs.py` and `scripts/restore_baseline.py`. Your evidence folder is separate.

**Stop:** A command fails, a destination already exists, or Python isn't the verified 3.12-or-newer interpreter.

**Recovery:** Keep the existing attempt. Fix the prerequisite through setup, then repeat this block with a new `RUN`. Don't reset the checkout or delete an old work folder.

### If you open a new terminal

A closed terminal forgets these variables. In a new terminal, run this block to reload them for the same attempt instead of preparing another one.

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

**Expected:** The terminal prints `RUN=` followed by the identifier you saw when you prepared this attempt, then `W=` followed by the existing work folder.

**Stop:** The identifier differs from the one you recorded, or the folder named after `W=` does not exist.

**Recovery:** If the identifier differs, a later attempt overwrote the saved marker: set `RUN` by hand to the value you recorded and run the block again. If the folder is missing, the attempt was never prepared, so prepare it with the first block.

## Freeze your rule and input identities

In your editor, open `W/shared/controls/policy.json` and the three batch manifests next to it. The policy lists the forty case IDs, the three form rows whose values need a source (mass, gate time UTC, gate time MDT), the mass and time-zone gates, no exclusions, and `any_violation_rejects`.

Create `W/decision.md` in your editor. Before you open any candidate, write down what would reject either candidate, what counts as a failed case, and that a faster result can't excuse an unsupported material claim. Don't write an adoption decision yet.

Freeze the file bytes without displaying the candidates. The record covers the policy, manifests, cases, gates, instructions, and restore copies.

![Freeze the rule, cases, and input identities before opening candidates; a manifest identifies supplied files, not a model execution.](figures/m08-freeze-before-results.png)

*Freeze the rule, cases, and input identities before opening candidates; a manifest identifies supplied files, not a model execution.*

<details markdown="1">
<summary>Figure text</summary>

Freeze the rule before opening any candidate.

1. Four inputs go into one frozen record:
   - the rejection rule, `any_violation_rejects`
   - the 40 case IDs
   - the input and configuration hashes
   - the batch manifests. A manifest names a supplied file; it is not proof that a model produced that file.
2. All four go into one frozen record, `pre-result.json`.
3. Then inspect the candidates.

Results cannot change the rule or the record: nothing goes back from the candidates or their results.

</details>

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" -c "import hashlib,json,sys; from pathlib import Path; w=Path(sys.argv[1]); files=sorted(p for p in (w/'shared').rglob('*') if p.is_file() and p.suffix in ('.json','.md','.py')); hashes={p.relative_to(w).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}; f=Path(sys.argv[2]).open('x',encoding='utf-8'); json.dump({'rule':'any_violation_rejects','sha256':hashes},f,indent=2); f.close(); print('FROZEN',len(hashes),'input/control files')" "$W" "$E/pre-result.json"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY -c "import hashlib,json,sys; from pathlib import Path; w=Path(sys.argv[1]); files=sorted(p for p in (w/'shared').rglob('*') if p.is_file() and p.suffix in ('.json','.md','.py')); hashes={p.relative_to(w).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}; f=Path(sys.argv[2]).open('x',encoding='utf-8'); json.dump({'rule':'any_violation_rejects','sha256':hashes},f,indent=2); f.close(); print('FROZEN',len(hashes),'input/control files')" "$W" "$E\pre-result.json"
```

**Expected:** The terminal prints `FROZEN`, a file count, and `input/control files`. `E/pre-result.json` holds the fingerprints of the files, and your decision rule was written before you saw any outcomes.

**Stop:** The record already exists, an input is missing, or you've already picked cases based on their results.

**Recovery:** Keep the first attempt and start a new one. A new filename doesn't turn a rule written after you saw results into one written before.

## Check the baseline, then evaluate every pair

First confirm that all forty baseline briefs pass, then score every baseline, A, and B brief on the same cases. Each case has `sources.json`, a three-row form, and three briefs: baseline, A, and B. A **locator** identifies the exact source record that supports a value. The mass and time-zone gates check each value together with its own locator; the format check records whether the brief follows the required form. A zone word elsewhere can't fix a clock value without its label. Judge a number by whether a source supports it, not by whether you've seen it in an earlier failure.

A malformed source packet, or one for the wrong case, stops the comparison. Don't count it as a candidate failure. A malformed candidate with valid sources stays in the comparison as a format failure.

Run every baseline first. In both shells, the loop remembers a failure even if a later case passes.

![Compare each candidate against its own same-case baseline and check each material value and locator; an average cannot erase a failed gate.](figures/m08-paired-hard-gates.png)

*Compare each candidate against its own same-case baseline and check each material value and locator; an average cannot erase a failed gate.*

<details markdown="1">
<summary>Figure text</summary>

A single violation still counts.

- One case's `sources.json` feeds three briefs: the baseline, candidate A, and candidate B.
- Each brief faces four separate checks:
  - format
  - mass with its `#payload` locator
  - UTC time with its `#gate` locator
  - MDT time with its `#gate` locator
- Each value is checked together with its own locator.
- The baseline must pass every check. If any baseline fails, the comparison is on HOLD: do not evaluate adoption. A baseline failure is not a candidate rejection.
- For candidates A and B, any one failed check rejects that candidate. A failed check is never averaged with other checks or other cases.
- Every result is kept.

</details>

**Terminal: Bash or zsh, ordinary user.**

```bash
baseline_failed=0
for case_dir in "$W"/shared/cases/PC-*; do
  "$PY" "$W/shared/controls/hard_gates.py" "$case_dir/baseline.md" || baseline_failed=1
done
if [ "$baseline_failed" -eq 0 ]; then echo 'BASELINE PASS'; else echo 'HOLD: a baseline failed; do not evaluate adoption.'; fi
```

**Terminal: PowerShell, ordinary user.**

```powershell
$baselineFailed = $false
foreach ($caseDir in Get-ChildItem "$W\shared\cases" -Directory -Filter 'PC-*') {
  & $PY "$W\shared\controls\hard_gates.py" "$($caseDir.FullName)\baseline.md"
  if ($LASTEXITCODE -ne 0) { $baselineFailed = $true }
}
if ($baselineFailed) { throw 'HOLD: a baseline failed; do not evaluate adoption.' } else { 'BASELINE PASS' }
```

**Expected:** Forty `PASS` lines, then `BASELINE PASS`. It says nothing about whether either candidate is good.

**Stop:** Any line starting `HOLD:`, or fewer than forty `PASS` lines.

**Recovery:** Save the failed output. Check the named input against your frozen record; don't fix a brief by hand to force the baseline to pass.

Now run the supplied evaluator from any directory.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$W/scripts/evaluate_pairs.py" "$W/shared/cases" "$W/shared/controls/policy.json" "$W/out/results.csv"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$W\scripts\evaluate_pairs.py" "$W\shared\cases" "$W\shared\controls\policy.json" "$W\out\results.csv"
```

**Expected:** `EVALUATED 120`. It doesn't mean the candidates passed. Open `W/out/results.csv` in your editor or a spreadsheet and look at `format_ok`, `mass_gate`, `zone_gate`, `passed`, `reason`, and the three identity columns.

**Stop:** A case is missing, an identity differs, the evaluator holds, or the output destination already exists.

**Recovery:** Keep the output and the error. Fix the input problem before you start a new attempt. Don't drop the difficult case or replace an earlier result.

## Make the bounded adoption decision

For each failed row, open that brief and the `sources.json` beside it. Trace the material value back to its exact authoritative locator. Record the case, candidate, gate, and source evidence in `decision.md`. Apply your original rule even if most cases pass.

For each candidate, report how many distinct cases would need repair. This **cost proxy** is a count of failed cases. Keep it separate from observed time, tokens, and money. These prewritten outputs tell you nothing about real API cost, and they don't show that one live model is better than another.

Before you accept the comparison, check that your frozen inputs still match.

![State only what the observed comparison supports, and keep the failed-case repair proxy separate from measured time, token usage, and cost estimates.](figures/m08-bounded-decision.png)

*State only what the observed comparison supports, and keep the failed-case repair proxy separate from measured time, token usage, and cost estimates.*

<details markdown="1">
<summary>Figure text</summary>

Keep the claim inside the evidence.

Four things set the limit of the bounded decision: the observed cases, the frozen rule, the named configuration, and the actual repetitions. Anything about unseen cases, including general superiority, is outside that limit: make no unseen-case claim.

Three measurements stay separate:

- The failed-case count is a repair proxy, not repair time.
- Elapsed time, tokens, and the SDK estimate are recorded on their own.
- The provider bill is unobserved unless you check it in your account.

</details>

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" -c "import hashlib,json,sys; from pathlib import Path; w=Path(sys.argv[1]); record=json.loads(Path(sys.argv[2]).read_text()); changed=[name for name,digest in record['sha256'].items() if hashlib.sha256((w/name).read_bytes()).hexdigest()!=digest]; print('FROZEN IDENTITY PASS' if not changed else 'HOLD: '+', '.join(changed)); sys.exit(bool(changed))" "$W" "$E/pre-result.json"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY -c "import hashlib,json,sys; from pathlib import Path; w=Path(sys.argv[1]); record=json.loads(Path(sys.argv[2]).read_text()); changed=[name for name,digest in record['sha256'].items() if hashlib.sha256((w/name).read_bytes()).hexdigest()!=digest]; print('FROZEN IDENTITY PASS' if not changed else 'HOLD: '+', '.join(changed)); sys.exit(bool(changed))" "$W" "$E\pre-result.json"
```

**Expected:** `FROZEN IDENTITY PASS`, which means every file you froze still matches the fingerprint you recorded before results. Your decision cites the actual failures instead of averaging them away.

**Stop:** The identity check fails, or your decision depends on a rule you changed after looking at results.

**Recovery:** Hold the adoption decision and keep the mismatch. Fix the process in a new attempt; don't change the result you've already seen.

## Demonstrate restoration

Swap in the candidate instruction, restore the baseline from its stored fingerprints, and prove the rerun is byte-identical. The block makes the checked instruction the active one (saving a copy of the previous first), then runs the supplied restore. This changes a control on purpose; it doesn't edit a candidate brief.

![Restore the hash-identified baseline, retain candidate attempts, and prove the rerun matches the original result bytes.](figures/m08-restore-baseline.png)

*Restore the hash-identified baseline, retain candidate attempts, and prove the rerun matches the original result bytes.*

<details markdown="1">
<summary>Figure text</summary>

Restore the baseline and confirm the rerun matches.

1. Make the checked instruction active, saving the previous active file first.
2. The stored hashes identify the frozen copies.
3. Restore the baseline control and briefs from those copies. The candidate attempts are kept, not deleted.
4. Rerun the evaluation.
5. Compare the original and restored result bytes.
   - Bytes match: restoration complete.
   - Bytes differ: HOLD.

</details>

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" -c "from pathlib import Path; import sys; w=Path(sys.argv[1]); active=w/'shared/controls/active-instruction.md'; backup=Path(sys.argv[2]).open('xb'); backup.write(active.read_bytes()); backup.close(); active.write_bytes((w/'shared/controls/candidate-checked-instruction.md').read_bytes())" "$W" "$E/active-before-selection.md" &&
"$PY" "$W/scripts/restore_baseline.py" "$W" &&
"$PY" "$W/scripts/evaluate_pairs.py" "$W/shared/cases" "$W/shared/controls/policy.json" "$W/out/restored-results.csv" &&
"$PY" -c "from pathlib import Path; import sys; w=Path(sys.argv[1]); same=(w/'out/results.csv').read_bytes()==(w/'out/restored-results.csv').read_bytes(); print('RESTORED RESULTS MATCH' if same else 'HOLD: results differ'); sys.exit(not same)" "$W"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY -c "from pathlib import Path; import sys; w=Path(sys.argv[1]); active=w/'shared/controls/active-instruction.md'; backup=Path(sys.argv[2]).open('xb'); backup.write(active.read_bytes()); backup.close(); active.write_bytes((w/'shared/controls/candidate-checked-instruction.md').read_bytes())" "$W" "$E\active-before-selection.md"
if ($LASTEXITCODE -ne 0) { throw 'Selection stopped; preserve the attempt.' }
& $PY "$W\scripts\restore_baseline.py" "$W"
if ($LASTEXITCODE -ne 0) { throw 'Restore held; do not continue.' }
& $PY "$W\scripts\evaluate_pairs.py" "$W\shared\cases" "$W\shared\controls\policy.json" "$W\out\restored-results.csv"
if ($LASTEXITCODE -ne 0) { throw 'Restored evaluation held.' }
& $PY -c "from pathlib import Path; import sys; w=Path(sys.argv[1]); same=(w/'out/results.csv').read_bytes()==(w/'out/restored-results.csv').read_bytes(); print('RESTORED RESULTS MATCH' if same else 'HOLD: results differ'); sys.exit(not same)" "$W"
```

**Expected:** Three lines in order: `RESTORE OK`, `EVALUATED 120`, `RESTORED RESULTS MATCH`. The restore checked the active instruction and all forty baseline briefs, the second evaluation matches the first byte for byte, and the candidate attempts are untouched.

**Stop:** The frozen restore source changed, a restore check holds, or the compared bytes differ.

**Recovery:** Keep both results and the control backup. Don't rebuild a baseline from memory or patch a candidate. Record what broke before you prepare a fresh copy.

## Write the handoff

In `W/handoff.md`, name the frozen policy record, the comparison results, your adoption decision, the repair proxy, and the restore evidence. State the limit: comparing fixed, supplied briefs doesn't measure how a live instruction behaves over repeated runs.

Before you stop, check that `handoff.md` names `pre-result.json`, `results.csv`, `restored-results.csv`, your decision, the failed-case counts for A and B, and the stated limit.

<details class="rf-stretch" markdown="1">
<summary>Optional stretch: separate an instruction effect from ordinary variation</summary>

## Preregister and run the live comparison

Compare the supplied baseline and checked instructions on PC-01–PC-06, with three fresh repeats per instruction and case, alternating which goes first. After those 36 calls, restore the baseline and run two fresh controls on PC-01 and PC-02. Don't choose replacements after you see results.

Open both instruction files in your editor. Explain the one check the candidate adds, and predict where it might help, make no difference, or add work. Record that prediction in `decision.md` before you run anything. Keep the model, source/form pair, prompt, and permissions the same within each pair.

This stretch costs money. Use only your OpenRouter key, which you enter in the terminal rather than save in a file, and the pinned Sonnet model from setup. The runner makes one call at a time, never retries a failed call, and never switches provider or model. If your key, credit, or the model isn't available, this stretch is blocked; that's not a reason to use a different provider.

Run this in the same terminal window that holds `PY`, `W`, `E`, and `M`. If you opened a new terminal, run the block under "If you open a new terminal" first.

### Enter your key in this terminal

Enter the key through a hidden prompt in this terminal. Paste the first command by itself and press Enter. Type or paste the key at the prompt (it shows nothing) and press Enter again. Then paste the second block. A new terminal starts without the key.

**Terminal: Bash or zsh, ordinary user.**

```bash
IFS= read -r -s OPENROUTER_API_KEY
```

**Terminal: PowerShell, ordinary user.**

```powershell
$secret = Read-Host 'OpenRouter key' -AsSecureString
```

**Expected:** The terminal waits silently for the key, then returns to its ordinary prompt without showing the value.

**Stop:** Characters appear as you type, or you're not sure which program is reading the input.

**Recovery:** Cancel with Ctrl+C and close that terminal. If the value was shown, revoke the key at OpenRouter and use a replacement.

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

**Expected:** `SET`. That proves the key is present in this terminal; it doesn't prove the key is valid or has credit.

**Stop:** `MISSING`, or any part of the key appears in the output.

**Recovery:** Repeat the hidden prompt in this terminal. Never print the environment to troubleshoot a key, and never save the key in a file or a shell profile.

Before the first call, the runner freezes the schedule and the file identities. Each model attempt gets only `sources.json` and `form.md`, plus permission to create `brief.md`. The launcher, not the batch runner, creates each receipt folder.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$M/scripts/stretch_runner.py" "$W" "$E/live-comparison"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$M\scripts\stretch_runner.py" "$W" "$E\live-comparison"
```

**Expected:** With everything in place, 38 attempts, each checked on its own, produce `comparison.json`, `attempts.csv`, raw receipts, the briefs the tool wrote, and `restore.json`. `COMPLETE` means every planned observation exists, not that the checked instruction won. Without the key, the runner exits 2 before it creates any comparison attempt or contacts a provider.

**Stop:** Any call is incomplete, a frozen identity changes, restoration fails, the provider rejects a request, or the runner stops on its own cost estimate. A content-gate failure is an observation to keep, not a cue to retry until the answer passes.

**Recovery:** Keep the whole comparison, including its first failure. Fix the missing prerequisite before you consider a new preregistered attempt. Don't merge favorable rows from different attempts, leave out failures, or change the runner so it doesn't stop.

## Interpret the paired observations

Open `comparison.json` and `attempts.csv`. For each case, compare the three baseline outcomes with the three checked outcomes. Report every paired disagreement (a baseline attempt and a checked attempt with different outcomes) and any differences among repeats of the same instruction. Keep every preregistered attempt visible. One better answer can't separate an instruction's effect from ordinary variation. Under the frozen rule, a single violation by the checked instruction rejects adoption. You may see no improvement at all.

Report the failed-case repair count separately from elapsed time, raw token usage, and the software library's cost estimate, which the receipts label as an SDK estimate. You don't know what the provider billed unless you check it in your account yourself; don't call an estimate a bill. Check the two restored controls and the hash of the instruction that was actually restored.

In your stretch conclusion, explain what these six cases support, what they don't show, and what's still uncertain. A finished model comparison doesn't certify a human operator, and it doesn't prove one instruction is better in general.

</details>
