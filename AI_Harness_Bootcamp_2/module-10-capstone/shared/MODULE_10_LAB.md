# Module 10 · Stand up a local uncensored AI and hand it off

A complete kit lets another person bring the pinned uncensored model up as a loopback-only service, prove one live interaction, stop it, and restore it without your chat history. Assemble the smallest sufficient set of files and instructions, freeze it, move only the declared bundle to a fresh location, and operate it from a new terminal. Keep your own rerun separate from observing another person use the kit.

The pinned model is `orcarouter/OrcaSAQ-2-Cyber-27B-Uncensored-GGUF`, one 15.7 GB weight file. Its refusal direction was removed: it will answer bluntly and apply no judgment of its own. The service binds `127.0.0.1` only, the weights stay on this laptop, and prompts are recorded by the harness.

Plan for 3 hours on Thursday. This is a planning allowance, not a measured completion guarantee. The recipient's attempt takes place outside the facilitated hours.

## Prepare separate work and transfer locations

Use the verified checkout and Python from [setup](../../module-00-setup/README.md). `W` is the authoring work copy, `E` is the separate evidence directory, and `F` is the future received package. The commands work from any directory. Do not create `F` until the transfer step.

**Terminal: Bash or zsh, ordinary user.**

```bash
R="$HOME/Documents/AIHB_OCT_2026"
PY="$(for candidate in python3.12 python3 python; do "$candidate" -c 'import sys; sys.exit(1) if sys.version_info < (3, 12) else print(sys.executable)' 2>/dev/null && break; done)"
[ -n "$PY" ] || echo 'HOLD: Python 3.12 or newer is required.' >&2
M="$R/AI_Harness_Bootcamp_2/module-10-capstone"
RUN="$(date -u +%Y%m%dT%H%M%SZ)-$$"
mkdir -p "$HOME/course-evidence" && printf '%s\n' "$RUN" > "$HOME/course-evidence/module-10-run" && printf 'RUN=%s\n' "$RUN"
BASE="$HOME/course-evidence/module-10-$RUN"
W="$BASE/work"
E="$BASE/evidence"
F="$BASE/received package"
"$PY" "$R/shared/prepare_work.py" 10 "$W" &&
"$PY" -c "from pathlib import Path; import sys; e,f=map(Path,sys.argv[1:]); (f.exists() or f.is_symlink()) and sys.exit('HOLD: received destination exists'); e.mkdir(); print('EVIDENCE',e); print('FRESH DESTINATION',f)" "$E" "$F"
```

**Terminal: PowerShell, ordinary user.**

```powershell
$R = "$HOME\Documents\AIHB_OCT_2026"
$PY = $(foreach ($candidate in 'python3.12','python3','python') { try { $resolved = & $candidate -c 'import sys; sys.exit(1) if sys.version_info < (3,12) else print(sys.executable)' 2>$null; if ($LASTEXITCODE -eq 0 -and $resolved) { $resolved.Trim(); break } } catch {} })
if (-not $PY) { throw 'HOLD: Python 3.12 or newer is required.' }
$M = "$R/AI_Harness_Bootcamp_2/module-10-capstone"
$RUN = [guid]::NewGuid().ToString('N')
New-Item -ItemType Directory -Force -Path "$HOME/course-evidence" | Out-Null; Set-Content -LiteralPath "$HOME/course-evidence/module-10-run" -Value $RUN; "RUN=$RUN"
$BASE = "$HOME/course-evidence/module-10-$RUN"
$W = "$BASE/work"
$E = "$BASE/evidence"
$F = "$BASE/received package"
& $PY "$R/shared/prepare_work.py" 10 "$W"
if ($LASTEXITCODE -ne 0) { throw 'Preparation held; preserve this attempt.' }
& $PY -c "from pathlib import Path; import sys; e,f=map(Path,sys.argv[1:]); (f.exists() or f.is_symlink()) and sys.exit('HOLD: received destination exists'); e.mkdir(); print('EVIDENCE',e); print('FRESH DESTINATION',f)" "$E" "$F"
```

**Expected:** `RUN=` and this attempt's identifier, then `PASS: created` followed by the work path; ignore the printed `Next` suggestion, because this lab gives the next command. `W` holds nested case, control, baseline, package, and scripts. `E` exists beside it, and the printed received-folder destination does not exist yet.

**Stop:** A destination exists, a prerequisite is missing, or preparation fails.

**Recovery:** Keep the first attempt, correct the prerequisite, and use a new `RUN`. Do not reset the checkout or reuse a partially prepared received folder.

### If you open a new terminal

Every command on this page uses the variables from the block above, and a terminal forgets them when it closes. Run this block in any new terminal to return to the same attempt instead of preparing a second one. It reads the attempt identifier that the first block saved.

**Terminal: Bash or zsh, ordinary user.**

```bash
R="$HOME/Documents/AIHB_OCT_2026"
PY="$(for candidate in python3.12 python3 python; do "$candidate" -c 'import sys; sys.exit(1) if sys.version_info < (3, 12) else print(sys.executable)' 2>/dev/null && break; done)"
[ -n "$PY" ] || echo 'HOLD: Python 3.12 or newer is required.' >&2
RUN="$(cat "$HOME/course-evidence/module-10-run")"
M="$R/AI_Harness_Bootcamp_2/module-10-capstone"
BASE="$HOME/course-evidence/module-10-$RUN"
W="$BASE/work"
E="$BASE/evidence"
F="$BASE/received package"
printf '%s\n' "RUN=$RUN" "W=$W"
```

**Terminal: PowerShell, ordinary user.**

```powershell
$R = "$HOME\Documents\AIHB_OCT_2026"
$PY = $(foreach ($candidate in 'python3.12','python3','python') { try { $resolved = & $candidate -c 'import sys; sys.exit(1) if sys.version_info < (3,12) else print(sys.executable)' 2>$null; if ($LASTEXITCODE -eq 0 -and $resolved) { $resolved.Trim(); break } } catch {} })
if (-not $PY) { throw 'HOLD: Python 3.12 or newer is required.' }
$RUN = (Get-Content -LiteralPath "$HOME/course-evidence/module-10-run" -Raw).Trim()
$M = "$R/AI_Harness_Bootcamp_2/module-10-capstone"
$BASE = "$HOME/course-evidence/module-10-$RUN"
$W = "$BASE/work"
$E = "$BASE/evidence"
$F = "$BASE/received package"
"RUN=$RUN"; "W=$W"
```

**Expected:** The terminal prints `RUN=` followed by the identifier you saw when you prepared this attempt, then `W=` followed by the existing work folder.

**Stop:** The identifier differs from the one you recorded, or the folder named after `W=` does not exist.

**Recovery:** A different identifier means a later attempt overwrote the saved marker; set `RUN` by hand to the value you recorded and run the block again. A missing folder means the attempt was never prepared, so prepare it with the first block.

## Read the boundary before the first launch

Open these files in your editor:

- `W/shared/case/SERVICE_RULES.md`
- `W/shared/case/model-card.json`
- `W/shared/case/task.json`
- `W/shared/case/hostile-note.md`
- `W/shared/PACKAGE.md`

In `E/pre-run.md`, record the pinned model identity, the byte size, the license, the base model, and the loopback bind. Explain what the identity check proves and what it does not. Quote the community note's two suggestions — the `0.0.0.0` bind and the skipped digest check — and state why each supplies no authority here. Name what the uncensored model will not do for you: refuse, warn, or apply judgment.

![Loopback limits network reach, and the identity check identifies the checked weight file; neither establishes the model's safety, accuracy, or fitness for publication.](figures/m10-operator-boundary.png)

*Loopback limits network reach, and the identity check identifies the checked weight file; neither establishes the model's safety, accuracy, or fitness for publication.*

<details markdown="1">
<summary>Figure text</summary>

The service boundary is `127.0.0.1` only. Inside it, one operator exchanges requests and replies with the local weights, and prompts and replies are recorded. Output from the local weights goes to the operator, who reviews it; it does not go straight to publishing. Two things are blocked at the boundary: no shared endpoint, and no traffic for other people. A separate note attached to the local weights reads: identity ≠ safety or accuracy. The identity check is a limited check of the weight file, not a safety guarantee around the service.

</details>

**Expected:** Every material statement has a file and line behind it. The loopback bind and the pinned identity are the only operating truth.

**Stop:** A rule is unclear, the note is being treated as guidance, or the boundary feels optional.

**Recovery:** Reopen `SERVICE_RULES.md` and the note. The boundary is not negotiable by anyone, including you.

## Gain account access and download the pinned weights

The repository is access-gated. Log in to Hugging Face, open the pinned repository page, and accept its conditions. The download is 15.7 GB and resumable.

**Terminal: Bash or zsh, ordinary user.**

```bash
hf auth login
hf download orcarouter/OrcaSAQ-2-Cyber-27B-Uncensored-GGUF --include "OrcaSAQ-2-27B-Uncensored.gguf" --local-dir "$W/weights"
```

**Terminal: PowerShell, ordinary user.**

```powershell
hf auth login
hf download orcarouter/OrcaSAQ-2-Cyber-27B-Uncensored-GGUF --include "OrcaSAQ-2-27B-Uncensored.gguf" --local-dir "$W/weights"
```

**Expected:** One file, `OrcaSAQ-2-27B-Uncensored.gguf`, at exactly 15,676,553,472 bytes when complete. Record the account name in `E/pre-run.md`; never record a token.

**Stop:** The conditions are not accepted, the download is interrupted, or the byte size differs.

**Recovery:** `hf download` resumes. Never accept a wrong-size file and never continue without the conditions accepted.

## Verify the pinned identity

**Terminal: Bash or zsh, ordinary user.**

```bash
cd "$W" && "$PY" scripts/local_ai.py verify --model weights/OrcaSAQ-2-27B-Uncensored.gguf --control shared/controls/run.json
```

**Terminal: PowerShell, ordinary user.**

```powershell
Set-Location -LiteralPath $W
& $PY scripts/local_ai.py verify --model weights/OrcaSAQ-2-27B-Uncensored.gguf --control shared/controls/run.json
```

**Expected:** `PASS: pinned weight identity verified` with the identity card: model id, weight file, exact size, digest, license, and base model.

**Stop:** The adapter reports a size or digest mismatch by name.

**Recovery:** Re-download and re-verify. Never edit `model-card.json` or force a pass. Return to the repository root with `cd "$BASE"` after this step.

## Wire OMP to the loopback service

**Terminal: Bash or zsh, ordinary user.**

```bash
cd "$W" && "$PY" scripts/local_ai.py wire --port 8080 --control shared/controls/run.json --work-dir . && cd "$BASE"
```

**Terminal: PowerShell, ordinary user.**

```powershell
Set-Location -LiteralPath $W
& $PY scripts/local_ai.py wire --port 8080 --control shared/controls/run.json --work-dir .
Set-Location -LiteralPath $BASE
```

**Expected:** `WIRED loopback service at 127.0.0.1:8080` and the two outputs `omp-local.yml` and `omp-launch.json`. The overlay names no address other than `127.0.0.1`. Read `omp-launch.json`: it records the exact OMP argv for the live interaction.

**Stop:** The adapter refuses the port, the outputs exist, or the control is disabled.

**Recovery:** The refusal names the reason. Preserve the outputs; never overwrite them.

## Bring the service up under OMP orchestration

OMP drafts the launch line and drives bring-up; you approve and observe each step. Open OMP in `W` and give it the orchestration brief below, then run the line it proposes after checking it against the pinned boundary.

![OMP drafts the launch line, but you check it against the pinned boundary and start the server; reachability is a separate probe.](figures/m10-launch-approval.png)

*OMP drafts the launch line, but you check it against the pinned boundary and start the server; reachability is a separate probe.*

<details markdown="1">
<summary>Figure text</summary>

1. Checked weights and the wired loopback config both feed into: OMP drafts launch line.
2. Check the drafted line: `127.0.0.1` + context `32768`.
3. If the bind is wrong, reject the line and go back to OMP for a new draft. A rejected line is never launched.
4. If the check passes, the operator starts the server.
5. A health probe then checks whether the service is reachable. A drafted line is not a running service.
6. If the probe finds the service unreachable, the result is HOLD.

</details>

```text
Read shared/case/SERVICE_RULES.md, shared/case/model-card.json, and shared/case/task.json.
Draft the exact llama-server launch line for the pinned weight file: loopback bind on port 8080, context 32768, no other flags that widen the boundary. Print the line and each flag's purpose. Do not run it yourself; I approve and run it.
```

Check the proposed line against `SERVICE_RULES.md`: the host must be `127.0.0.1`, the context must be 32768, and nothing else may widen the boundary. Run the approved line in a terminal reserved for the server:


**Terminal: Bash or zsh, ordinary user.**

```bash
llama-server -m "$W/weights/OrcaSAQ-2-27B-Uncensored.gguf" --host 127.0.0.1 --port 8080 -c 32768
```


**Terminal: PowerShell, ordinary user.**
```powershell
llama-server -m "$W\weights\OrcaSAQ-2-27B-Uncensored.gguf" --host 127.0.0.1 --port 8080 -c 32768
```

Load takes minutes on most laptops. When the server reports loading complete, prove reachability from a second terminal:


**Terminal: Bash or zsh, ordinary user.**

```bash
cd "$W" && "$PY" scripts/local_ai.py probe --port 8080 --control shared/controls/run.json && cd "$BASE"
```


**Terminal: PowerShell, ordinary user.**
```powershell
Set-Location -LiteralPath $W
& $PY scripts/local_ai.py probe --port 8080 --control shared/controls/run.json
Set-Location -LiteralPath $BASE
```

**Expected:** The probe prints `PASS: local service reachable on loopback`. Record the load time and the probe result in `E/pre-run.md`.

**Stop:** The proposed line binds anything except `127.0.0.1`, loading fails, or the probe reports unreachable.

**Recovery:** Reject the drafted line and ask again if the bind is wrong; free memory and re-probe if loading failed. Do not change the bind address or the context.

## Prove one live interaction

![Each check supports a narrow claim; neither a health probe nor a package-structure pass proves model quality or another person's operation.](figures/m10-evidence-boundaries.png)

*Each check supports a narrow claim; neither a health probe nor a package-structure pass proves model quality or another person's operation.*

<details markdown="1">
<summary>Figure text</summary>

Each kind of evidence supports one narrow claim. None ranks above the others:

- Size + digest → weight identity.
- Health probe → reachable at probe time.
- Live transcript → recorded interaction.
- Structure check → named fields + local paths.

None of these checks establishes any of the following: not safety, not model quality, not production readiness, and not independent transfer.

</details>

Run the exact argv from `omp-launch.json`:

**Terminal: Bash or zsh, ordinary user.**

```bash
cd "$W" && omp --model llama.cpp/OrcaSAQ-2-27B-Uncensored --config omp-local.yml --no-session --no-title --no-skills --no-rules --no-extensions --no-lsp --no-prewalk --mode json -p "Answer in one sentence: what are you?" > "$E/live-interaction.jsonl"; cd "$BASE"
```

**Terminal: PowerShell, ordinary user.**

```powershell
Set-Location -LiteralPath $W
omp --model llama.cpp/OrcaSAQ-2-27B-Uncensored --config omp-local.yml --no-session --no-title --no-skills --no-rules --no-extensions --no-lsp --no-prewalk --mode json -p "Answer in one sentence: what are you?" > "$E/live-interaction.jsonl"
Set-Location -LiteralPath $BASE
```

**Expected:** The saved stream contains a real assistant reply, names `llama.cpp` as the provider, and reports zero cost. A refusal to answer would be surprising from this model; a connection failure is the failure mode to watch.

**Stop:** A context-size refusal or connection failure appears.

**Recovery:** Re-probe, then retry once. If the context is exceeded, the server context stays at the pinned value; do not widen it.

## Observe the uncensored behaviour

Ask the model for one deliberately blunt answer, for example a sentence a safety-tuned model would soften. Save the exchange to `E/observations.md`. The model will not refuse and will not warn; that is the capability you chose, and the guardrail is you. Record what you would not put your name on and why you would not send it anywhere.

**Expected:** A recorded exchange showing the model answering without refusal, and your named boundary for using its output.

**Stop:** The exchange is not saved, or the observation reads like an endorsement of unlimited use.

**Recovery:** Save the transcript first, then write the boundary.

## Stop the service and prove the stopped state

Interrupt the server process in its terminal with Ctrl+C. Then prove the stopped state and record it:


**Terminal: Bash or zsh, ordinary user.**

```bash
cd "$W" && "$PY" scripts/local_ai.py probe --port 8080 --control shared/controls/run.json && cd "$BASE"
```


**Terminal: PowerShell, ordinary user.**
```powershell
Set-Location -LiteralPath $W
& $PY scripts/local_ai.py probe --port 8080 --control shared/controls/run.json
Set-Location -LiteralPath $BASE
```

**Expected:** The probe exits 1 with `HOLD: service is not reachable`; the service is down.

Write the stop receipt in `W` naming the port and the action:


**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" -c "import json; print(json.dumps({'action':'stop','port':8080,'stopped_by':'operator Ctrl+C at the server terminal'}))" > "$W/stop-receipt.json" && cat "$W/stop-receipt.json"
```


**Terminal: PowerShell, ordinary user.**
```powershell
"$PY" -c "import json; print(json.dumps({'action':'stop','port':8080,'stopped_by':'operator Ctrl+C at the server terminal'}))" > "$W/stop-receipt.json"; Get-Content "$W/stop-receipt.json"
```

Then confirm it:


**Terminal: Bash or zsh, ordinary user.**

```bash
cd "$W" && "$PY" scripts/local_ai.py stop --port 8080 --control shared/controls/run.json --receipt stop-receipt.json && cd "$BASE"
```


**Terminal: PowerShell, ordinary user.**
```powershell
Set-Location -LiteralPath $W
& $PY scripts/local_ai.py stop --port 8080 --control shared/controls/run.json --receipt stop-receipt.json
Set-Location -LiteralPath $BASE
```

**Expected:** `PASS: service is stopped and unreachable on loopback`. Copy the receipt to `E/`.

**Stop:** The probe still reports the service reachable, or the receipt does not name this port.

**Recovery:** Terminate the server and re-probe. Never record a stop that did not happen.

## Disable the control and prove the refusal

Disable the active control, attempt each adapter command, and restore from the validated baseline:

![The operator stops the process; the adapter verifies the stopped state. Restoring an enabled control does not itself restart the service.](figures/m10-stop-restore.png)

*The operator stops the process; the adapter verifies the stopped state. Restoring an enabled control does not itself restart the service.*

<details markdown="1">
<summary>Figure text</summary>

Stopping the service and the control are separate.

Stopping, from the step before: the operator stops the process → the probe reports unreachable → stop receipt → the adapter verifies the stopped state. The operator ends the process; the adapter only verifies that it stopped.

Control: control disabled → every adapter command returns `HOLD: control disabled`. The disabled-control check runs before anything else, so this refusal is not a health observation and cannot prove the service stopped. Only the stop evidence shows that. Separately: validate the baseline digest → restore the control from that baseline.

Restoring the control does not restart the service automatically, and a restored control is not evidence of a running service. To claim the service is running again, launch it and probe it again.

</details>


**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" -c "from pathlib import Path; import json; Path('$W/shared/controls/run.json').write_text(json.dumps({'enabled': False})+'\n')" && cd "$W" && "$PY" scripts/local_ai.py probe --port 8080 --control shared/controls/run.json; cd "$BASE"
```


**Terminal: PowerShell, ordinary user.**
```powershell
& $PY -c "from pathlib import Path; import json; Path('$W/shared/controls/run.json').write_text(json.dumps({'enabled': False})+'\n')"
Set-Location -LiteralPath $W
& $PY scripts/local_ai.py probe --port 8080 --control shared/controls/run.json
Set-Location -LiteralPath $BASE
```

**Expected:** `HOLD: control disabled` and exit 1 for every adapter command; no command acts while the control is off.

Restore from the baseline by rerunning the package's own restore commands, then confirm the wire outputs are unchanged before proceeding.

**Stop:** Any adapter command acts while the control is disabled, or the baseline digest fails.

**Recovery:** Preserve the refusal as evidence. Restore only through the validated baseline.

## Freeze the declared bundle before copying

Keep only the eleven files the package declares. Do not add the weights, the evidence folder, the repository, private material, or conversation history. Freeze the identities outside `W`:

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" - "$W" "$E" <<'PY'
from pathlib import Path
import hashlib, json, sys
w,e = map(Path,sys.argv[1:])
names = ['shared/PACKAGE.md','scripts/local_ai.py','scripts/check_package.py','shared/case/model-card.json','shared/case/SERVICE_RULES.md','shared/case/task.json','shared/case/hostile-note.md','shared/controls/run.json','shared/baseline/run.json','shared/baseline/run.json.sha256']
files = {name:hashlib.sha256((w/name).read_bytes()).hexdigest() for name in names}
record = {'files':files,'stop_receipt_sha256':hashlib.sha256((w/'stop-receipt.json').read_bytes()).hexdigest()}
with (e/'bundle-before.json').open('x',encoding='utf-8') as output:
    json.dump(record,output,indent=2,sort_keys=True)
print('FROZEN BUNDLE',len(files),'files')
PY
```

**Terminal: PowerShell, ordinary user.**

```powershell
@'
from pathlib import Path
import hashlib, json, sys
w,e = map(Path,sys.argv[1:])
names = ['shared/PACKAGE.md','scripts/local_ai.py','scripts/check_package.py','shared/case/model-card.json','shared/case/SERVICE_RULES.md','shared/case/task.json','shared/case/hostile-note.md','shared/controls/run.json','shared/baseline/run.json','shared/baseline/run.json.sha256']
files = {name:hashlib.sha256((w/name).read_bytes()).hexdigest() for name in names}
record = {'files':files,'stop_receipt_sha256':hashlib.sha256((w/'stop-receipt.json').read_bytes()).hexdigest()}
with (e/'bundle-before.json').open('x',encoding='utf-8') as output:
    json.dump(record,output,indent=2,sort_keys=True)
print('FROZEN BUNDLE',len(files),'files')
'@ | & $PY - "$W" "$E"
```

**Expected:** A new record with ten path/digest pairs and the stop-receipt digest.

**Stop:** A file is missing, a record already exists, or the set differs from the package's declared inputs.

**Recovery:** Correct the bundle and freeze again into a new record; never overwrite the old one.

## Copy only the frozen members

The weights stay out: the colleague downloads them under their own account against the pinned identity. Copy with digest validation exactly as the package's freeze step prescribes:


**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" - "$W" "$F" "$E/bundle-before.json" <<'PY'
from pathlib import Path
import hashlib, json, shutil, sys
w,f,record_path = map(Path,sys.argv[1:])
w = w.resolve()
record = json.loads(record_path.read_text())
if f.exists() or f.is_symlink() or f.resolve().is_relative_to(w):
    raise SystemExit('HOLD: received destination exists or overlaps work')
for name,digest in record['files'].items():
    source = w/Path(name)
    if not source.resolve().is_relative_to(w):
        raise SystemExit('HOLD: escaping bundle path: '+name)
    if hashlib.sha256(source.read_bytes()).hexdigest()!=digest:
        raise SystemExit('HOLD: frozen source changed: '+name)
f.mkdir(parents=True,exist_ok=False)
for name,digest in record['files'].items():
    target = f/name
    target.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(w/name,target)
    if hashlib.sha256(target.read_bytes()).hexdigest()!=digest:
        raise SystemExit('HOLD: copied bytes differ: '+name)
print('FRESH PACKAGE',f.resolve())
print('NO WEIGHTS COPIED')
PY
```

**Terminal: PowerShell, ordinary user.**

```powershell
@'
from pathlib import Path
import hashlib, json, shutil, sys
w,f,record_path = map(Path,sys.argv[1:])
w = w.resolve()
record = json.loads(record_path.read_text())
if f.exists() or f.is_symlink() or f.resolve().is_relative_to(w):
    raise SystemExit('HOLD: received destination exists or overlaps work')
for name,digest in record['files'].items():
    source = w/Path(name)
    if not source.resolve().is_relative_to(w):
        raise SystemExit('HOLD: escaping bundle path: '+name)
    if hashlib.sha256(source.read_bytes()).hexdigest()!=digest:
        raise SystemExit('HOLD: frozen source changed: '+name)
f.mkdir(parents=True,exist_ok=False)
for name,digest in record['files'].items():
    target = f/name
    target.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(w/name,target)
    if hashlib.sha256(target.read_bytes()).hexdigest()!=digest:
        raise SystemExit('HOLD: copied bytes differ: '+name)
print('FRESH PACKAGE',f.resolve())
print('NO WEIGHTS COPIED')
'@ | & $PY - "$W" "$F" "$E/bundle-before.json"
```

**Expected:** The printed destination contains only the declared bundle. The weights are absent by design.

**Stop:** The destination exists, a frozen source changed, or the weights were copied.

**Recovery:** Keep the failed folder; use a fresh destination for a corrected transfer.

## Hand the package to another person

The colleague receives the fresh folder, the pinned identity, and the boundary. Let them run it from the package alone: account access, download, verify, wire, serve, probe, interact, stop, restore. Record their questions, commands, observed outcomes, and any help in `E/transfer-status.md`. A technical replay, including an agent replay, is not an observation of another person's operation. If no person is available, retain the technical results and record independent-person operation as **unobserved**, with the missing prerequisite. It is not a pass.

If the colleague needs help, record what they did before and after; do not relabel an assisted attempt as independent. Use their questions to improve a new package version while preserving the observed attempt.

![Keep technical replay separate from another person's attempt, record every intervention, and mark human transfer unobserved when no recipient has operated the kit.](figures/m10-independent-transfer.png)

*Keep technical replay separate from another person's attempt, record every intervention, and mark human transfer unobserved when no recipient has operated the kit.*

<details markdown="1">
<summary>Figure text</summary>

Three separate kinds of evidence:

- Author rerun.
- Fresh-session technical replay. It is not passed by substitution: it does not count as another person's operation.
- Different person → package alone → questions / actions / outcomes → record any help → assisted stays assisted.

If there is no recipient, the different person's operation is UNOBSERVED. No agent or checker result counts as a different person's operation.

</details>

## Close the session

In `E/close-out.md`, record the verified identity, the live interaction, the stop receipt, the restore comparison, and the transfer status. State plainly which parts ran and which did not. Then shut the service down if it is still running, and keep the evidence bundle for staff review.
