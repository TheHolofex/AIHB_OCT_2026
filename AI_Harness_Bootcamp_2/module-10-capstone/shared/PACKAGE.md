# Runnable local AI service package

## Purpose

Bring the pinned uncensored model up as a loopback-only service on this laptop, prove one live interaction through it, stop it, restore it, then freeze a ten-file kit and check a fresh copy from a new terminal on the same machine.

## Bounds

One operator at a time. The service binds `127.0.0.1` only. The weights stay on this machine: no re-upload, no sharing the endpoint, no serving another person's traffic. Prompts and replies are recorded in the evidence directory. The model is uncensored; every boundary in this section is the operator's responsibility, not the model's.

## Inputs

The fresh copy carries only these ten files; the weights are excluded:

- `shared/PACKAGE.md`
- `scripts/local_ai.py`
- `scripts/check_package.py`
- `shared/case/model-card.json`
- `shared/case/SERVICE_RULES.md`
- `shared/case/task.json`
- `shared/case/hostile-note.md`
- `shared/controls/run.json`
- `shared/baseline/run.json`
- `shared/baseline/run.json.sha256`

The 15.7 GB weights stay at the original work location. The final fresh-copy structure check uses only `scripts/check_package.py` and the other copied files. It requires neither a second download nor a running service.

## Controls / config identity

`shared/controls/run.json` is the active control; only a Boolean `enabled` field is accepted, and every adapter command rechecks it before acting. `shared/baseline/run.json` plus `shared/baseline/run.json.sha256` is the restore source; validate the digest before restoring. The wire outputs `omp-local.yml` and `omp-launch.json` are generated fresh by the adapter in the work directory and compared byte for byte after any rerun. A digest detects a change against the retained record; it is not proof of authorship.

## Run

Resolve a Python 3.12-or-newer executable, log in to Hugging Face, accept the pinned repository's conditions, then download and verify the weights.

**Terminal: Bash or zsh, ordinary user.**

```bash
PY="$(for candidate in python3.12 python3 python; do "$candidate" -c 'import sys; sys.exit(1) if sys.version_info < (3, 12) else print(sys.executable)' 2>/dev/null && break; done)"
hf auth login
hf download orcarouter/OrcaSAQ-2-Cyber-27B-Uncensored-GGUF --include "OrcaSAQ-2-27B-Uncensored.gguf" --local-dir weights
"$PY" scripts/local_ai.py verify --model weights/OrcaSAQ-2-27B-Uncensored.gguf --control shared/controls/run.json
"$PY" scripts/local_ai.py wire --port 8080 --control shared/controls/run.json --work-dir .
```

**Terminal: PowerShell, ordinary user.**

```powershell
$PY = $(foreach ($candidate in 'python3.12','python3','python') { try { $resolved = & $candidate -c 'import sys; sys.exit(1) if sys.version_info < (3,12) else print(sys.executable)' 2>$null; if ($LASTEXITCODE -eq 0 -and $resolved) { $resolved.Trim(); break } } catch {} })
hf auth login
hf download orcarouter/OrcaSAQ-2-Cyber-27B-Uncensored-GGUF --include "OrcaSAQ-2-27B-Uncensored.gguf" --local-dir weights
& $PY scripts/local_ai.py verify --model weights/OrcaSAQ-2-27B-Uncensored.gguf --control shared/controls/run.json
& $PY scripts/local_ai.py wire --port 8080 --control shared/controls/run.json --work-dir .
```

**Expected:** `PASS: pinned weight identity verified` with the identity card, then `WIRED loopback service at 127.0.0.1:8080`. The wire output names no address other than `127.0.0.1`.

**Stop:** The repository conditions are not accepted, the download is interrupted, the byte size differs, or the digest does not match.

**Recovery:** The download resumes; never accept a wrong-size or wrong-digest file, and never edit `model-card.json` to force a pass.

Start the service on loopback with the pinned context, wait for load, then confirm reachability. The launch line is the one the wire step and the orchestration notes assemble; `omp-launch.json` records the exact OMP argv.

```bash
llama-server -m weights/OrcaSAQ-2-27B-Uncensored.gguf --host 127.0.0.1 --port 8080 -c 32768
"$PY" scripts/local_ai.py probe --port 8080 --control shared/controls/run.json
```

```powershell
llama-server -m weights/OrcaSAQ-2-27B-Uncensored.gguf --host 127.0.0.1 --port 8080 -c 32768
& $PY scripts/local_ai.py probe --port 8080 --control shared/controls/run.json
```

**Expected:** The server reports loading complete; the probe prints `PASS: local service reachable on loopback`.

**Stop:** Loading fails, or the probe reports the service unreachable.

**Recovery:** Free memory, keep the context at the pinned value, and re-probe. Do not change the bind address.

One live interaction through OMP:

```bash
omp --model llama.cpp/OrcaSAQ-2-27B-Uncensored --config omp-local.yml --no-session --no-title --no-skills --no-rules --no-extensions --no-lsp --no-prewalk --mode json -p "Answer in one sentence: what are you?"
```

```powershell
omp --model llama.cpp/OrcaSAQ-2-27B-Uncensored --config omp-local.yml --no-session --no-title --no-skills --no-rules --no-extensions --no-lsp --no-prewalk --mode json -p "Answer in one sentence: what are you?"
```

**Expected:** A real reply from the local model; the event stream names `llama.cpp` as provider and reports zero cost. Keep the transcript.

**Stop:** A context-size refusal or a connection failure.

**Recovery:** Re-probe; the service must be reachable before any interaction. Do not edit the overlay to widen the context.

## Check

```bash
"$PY" scripts/local_ai.py verify --model weights/OrcaSAQ-2-27B-Uncensored.gguf --control shared/controls/run.json
"$PY" scripts/local_ai.py probe --port 8080 --control shared/controls/run.json
"$PY" scripts/check_package.py shared/PACKAGE.md
```

```powershell
& $PY scripts/local_ai.py verify --model weights/OrcaSAQ-2-27B-Uncensored.gguf --control shared/controls/run.json
& $PY scripts/local_ai.py probe --port 8080 --control shared/controls/run.json
& $PY scripts/check_package.py shared/PACKAGE.md
```

**Expected:** `PASS: pinned weight identity verified`, `PASS: local service reachable on loopback`, and `PASS: package structure checked`.

**Stop:** Any check holds.

**Recovery:** Preserve the first failure. The structural check does not execute commands and does not show that another person can operate the kit. The final fresh-copy check (after freeze) runs only `check_package.py` from the new terminal on the copied files; it performs no download and no server launch.

## Stop

Interrupt the server process, then prove the stopped state.

```bash
"$PY" scripts/local_ai.py probe --port 8080 --control shared/controls/run.json
```

```powershell
& $PY scripts/local_ai.py probe --port 8080 --control shared/controls/run.json
```

**Expected:** The probe exits 1 with `HOLD: service is not reachable`. Write the stop receipt naming the port, then confirm it:

```bash
"$PY" scripts/local_ai.py stop --port 8080 --control shared/controls/run.json --receipt stop-receipt.json
```

```powershell
& $PY scripts/local_ai.py stop --port 8080 --control shared/controls/run.json --receipt stop-receipt.json
```

**Expected:** `PASS: service is stopped and unreachable on loopback`. No stopped-state proof, no handoff.

**Stop:** The probe still reports the service reachable.

**Recovery:** Terminate the server process and re-probe. Do not record a stop that did not happen.

## Restore

Validate the frozen baseline, restore the enabled control if it was disabled, relaunch the service, and prove both reachability and unchanged wiring:

```bash
"$PY" - <<'PY'
from pathlib import Path
import hashlib, json
root = Path.cwd().resolve()
source = root/'shared/baseline/run.json'
target = root/'shared/controls/run.json'
raw = source.read_bytes()
listed = (root/'shared/baseline/run.json.sha256').read_text().split()[0]
if hashlib.sha256(raw).hexdigest() != listed:
    raise SystemExit('HOLD: baseline digest invalid')
target.write_bytes(raw)
print('RESTORE OK')
PY
```

```powershell
@'
from pathlib import Path
import hashlib
root = Path.cwd().resolve()
source = root/'shared/baseline/run.json'
target = root/'shared/controls/run.json'
raw = source.read_bytes()
listed = (root/'shared/baseline/run.json.sha256').read_text().split()[0]
if hashlib.sha256(raw).hexdigest() != listed:
    raise SystemExit('HOLD: baseline digest invalid')
target.write_bytes(raw)
print('RESTORE OK')
'@ | & $PY -
```

```bash
"$PY" scripts/local_ai.py probe --port 8080 --control shared/controls/run.json
```

```powershell
"& $PY scripts/local_ai.py probe --port 8080 --control shared/controls/run.json"
```

**Expected:** `RESTORE OK`, the probe passes, and the wire outputs are byte-identical.

**Stop:** The baseline digest fails, the probe fails, or the wire bytes differ.

**Recovery:** Preserve every artifact. Do not run the next command after a failed restore.

## Strongest evidence

The verify identity card, the live interaction transcript naming `llama.cpp` as provider at zero cost, the stop receipt, and the byte-identical restore comparison. Together these show the pinned weights, a loopback-only service, and a stopped state that you can reach again after restore from the frozen baseline.

## Limitations

The model is uncensored; it carries no refusal behaviour of its own and applies no editorial judgment. Guardrails, filtering, and what to publish from replies are the operator's. The quantization is not lossless. This kit proves a bounded local service and a cold restart; it does not establish production serving, safety-stack completeness, or model quality. A laptop that cannot hold the 15.7 GB file in memory runs it slowly or not at all.

## Next owner

You retain the kit and its evidence on your laptop. Complete the live run, stop/restore proof, and fresh-copy check within the session. If a required step cannot finish, record the reason for `HOLD` and close the attempt before the session ends.
