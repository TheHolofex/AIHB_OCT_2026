# Runnable local AI service package

## Purpose

Bring the named uncensored model up on this laptop, where only this laptop can reach it. Get one real reply, stop it, and bring it back. Then save the ten files and check a fresh copy from a new terminal on this same machine. You keep this. You are not handing it to someone else.

## Bounds

One person at a time, and that person is you. The server listens on `127.0.0.1` only. The model file stays on this machine. Don't upload it again, don't share the address, and don't let anyone else send requests to it. Prompts and replies are recorded in the evidence folder. The model is uncensored. Every limit in this section is yours to hold, not the model's.

## Inputs

The fresh copy carries only these ten files. The model file is not one of them:

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

The 15.7 GB model file stays where you downloaded it. The final check uses only `scripts/check_package.py` and the other copied files. It does not need a second download, and it does not need the server to be running.

## Controls / config identity

`shared/controls/run.json` is the on/off switch. It accepts only a true or false `enabled` field, and every check command looks at it before acting. `shared/baseline/run.json` plus `shared/baseline/run.json.sha256` is the copy you restore from. Check the fingerprint before you restore. The wire step writes `omp-local.yml` and `omp-launch.json` fresh in the work folder, and you compare those bytes after any rerun. A fingerprint shows that a file changed against the record you kept. It does not prove who wrote the file.

## Run

Find a Python 3.12 or newer program, sign in to Hugging Face, accept the model's conditions, then download the model file and check it.

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

**Recovery:** The download resumes. Never accept a wrong-size or wrong-fingerprint file, and never edit `model-card.json` to force a pass.

Start the server on this laptop with the named context, wait for it to load, then confirm it answers. The start line is the one the wire step and your notes assemble. `omp-launch.json` records the exact OMP command.

```bash
llama-server -m weights/OrcaSAQ-2-27B-Uncensored.gguf --host 127.0.0.1 --port 8080 -c 32768
"$PY" scripts/local_ai.py probe --port 8080 --control shared/controls/run.json
```

```powershell
llama-server -m weights/OrcaSAQ-2-27B-Uncensored.gguf --host 127.0.0.1 --port 8080 -c 32768
& $PY scripts/local_ai.py probe --port 8080 --control shared/controls/run.json
```

**Expected:** The server reports loading complete. The check prints `PASS: local service reachable on loopback`.

**Stop:** Loading fails, or the check says the server cannot be reached.

**Recovery:** Free some memory, keep the context at the named value, and check again. Do not change the address.

One live reply through OMP:

```bash
omp --model llama.cpp/OrcaSAQ-2-27B-Uncensored --config omp-local.yml --no-session --no-title --no-skills --no-rules --no-extensions --no-lsp --no-prewalk --mode json -p "Answer in one sentence: what are you?"
```

```powershell
omp --model llama.cpp/OrcaSAQ-2-27B-Uncensored --config omp-local.yml --no-session --no-title --no-skills --no-rules --no-extensions --no-lsp --no-prewalk --mode json -p "Answer in one sentence: what are you?"
```

**Expected:** A real reply from the local model. The event stream names `llama.cpp` as provider and reports zero cost. Keep the transcript.

**Stop:** A context-size refusal or a connection failure.

**Recovery:** Check that the server answers before you try again. Do not edit the settings to widen the context.

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

**Recovery:** Keep the first failure. The structure check does not run the commands. It tells you the named sections and files are present. It does not start the server, and it does not mean someone else can run this. You run it. The final fresh-copy check, after you freeze the files, runs only `check_package.py` from the new terminal on the copied files. It does not download anything, and it does not start the server.

## Stop

Interrupt the server process, then prove it stopped.

```bash
"$PY" scripts/local_ai.py probe --port 8080 --control shared/controls/run.json
```

```powershell
& $PY scripts/local_ai.py probe --port 8080 --control shared/controls/run.json
```

**Expected:** The check exits 1 with `HOLD: service is not reachable`. Write the stop receipt naming the port, then confirm it:

```bash
"$PY" scripts/local_ai.py stop --port 8080 --control shared/controls/run.json --receipt stop-receipt.json
```

```powershell
& $PY scripts/local_ai.py stop --port 8080 --control shared/controls/run.json --receipt stop-receipt.json
```

**Expected:** `PASS: service is stopped and unreachable on loopback`. If you do not have that line, you do not have a stopped server.

**Stop:** The check still says the server can be reached.

**Recovery:** Stop the server process and check again. Do not record a stop that did not happen.

## Restore

Check the saved baseline, put the on/off switch back if you turned it off, start the server again, and prove both that it answers and that the wiring is unchanged:

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

**Expected:** `RESTORE OK`, the check passes, and the wire files are byte-identical.

**Stop:** The baseline fingerprint fails, the check fails, or the wire bytes differ.

**Recovery:** Keep every file from the failed attempt. Do not run the next command after a failed restore.

## Strongest evidence

The identity card from the verify step, the live reply that names `llama.cpp` as the provider at zero cost, the stop receipt, and the restore comparison that matches byte for byte. Together these show the named model file, a server only this laptop can reach, and a stopped state you can reach again after you restore from the saved baseline.

## Limitations

The model is uncensored. It will not refuse on its own, and it will not edit itself. What you ask, what you filter, and what you publish are your decisions. The file is a compressed copy, not a perfect copy of the full model. This kit shows a local service you can stop and start again. It does not show that the service is ready for other people, that a safety stack is complete, or that the model's answers are good. A laptop that cannot hold the 15.7 GB file in memory runs it slowly, or not at all.

## Next owner

You keep the kit and the evidence on your laptop. You are the owner. Finish the live run, the stop and restore proof, and the fresh-copy check in this session. If a required step cannot finish, write the reason for `HOLD` and close the attempt before the session ends.
