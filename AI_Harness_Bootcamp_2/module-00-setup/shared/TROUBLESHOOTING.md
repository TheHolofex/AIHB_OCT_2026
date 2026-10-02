# When setup stops

Start with the first failed action. Save its exact error and the last known-good observation before changing anything. Do not reinstall every tool or discard an existing checkout.

## Choose the next action from the observed failure

| Observation | Next action |
|---|---|
| Git or Python is missing | Return to the named platform's prerequisite step. On a managed device, stop when policy blocks installation and send the support packet below. |
| A download fails | Keep the HTTP, proxy, or certificate error. Use the official release URLs. Do not disable TLS verification or execute an incomplete download. |
| The checksum fails or the selected asset has no unique checksum entry | Do not install or execute the binary. Retain the failed download separately and investigate the filename, release, and source before downloading into a new directory. |
| `omp` is not found | Check the resolved command path below. Add only the user-bin directory named by your platform guide, then check again in the intended terminal. |
| `omp` reports a different version | Keep the observed path and version. Do not overwrite a different installation silently. Use the verified course binary and confirm that PATH resolves to it. |
| A course directory already exists | Confirm that it is the intended checkout. Use it without reset, pull, or clean when it is valid; otherwise leave it untouched and resolve the path conflict. |
| Git cannot read the private course repository | A website password is not GitHub access. Follow the platform's disabled-prompt read check and conditional browser-login steps. A successful GitHub login still needs repository read permission; ask the repository owner about the invitation or organization approval. Preserve any existing checkout. |
| GitHub CLI reports unapproved credential storage | Stop before configuring the Git helper or cloning. Have the device owner provision approved credential storage or approved Git credentials. Do not request plaintext storage or share authentication output. |
| The conditional GitHub CLI package is unavailable | Use only the named platform's official package route. Ubuntu's `gh` requires Universe; ask the owner to approve that component if unavailable. Do not silently add sources. Arch's `github-cli` installation uses a full upgrade, not a partial upgrade. |
| The new terminal has tools but the key is `MISSING` | This is expected for independently opened terminals. Enter the key through the hidden-input step in that terminal. Never put the key in a shell profile. |
| A new process reports an unexpected `SET` | Determine whether it inherited the environment from a parent. `SET` alone does not prove persistence or exposure. Do not dump the environment into evidence. |
| The launcher exits 2 | Read its prerequisite message. Missing key, wrong OMP version, missing input, conflicting permissions, or an existing attempt can stop before a provider request. No live success has occurred. |
| The launcher exits 1 | Retain the entire attempted run. Inspect `result.json` and the raw receipts; an incomplete turn is not rescued by a file left behind. |
| The provider returns 401 or 403 | Confirm the participant key and model access in OpenRouter without printing the key. Do not try a direct-provider login or silently switch models. |
| The provider returns 402 or 429 | Stop paid work. Preserve the response and resolve credit or rate availability before an explicit new attempt. Do not loop retries. |
| The assistant claims it wrote a file, but the file or receipt is absent | Record `HOLD`. Check the declared work root and authorized filename. Do not manufacture the file or substitute chat text as a tool-write receipt. |
| A write or evidence destination already exists | Preserve that attempt. Start with new work/output and receipt paths after documenting the cause; changing only E does not make an existing output new. |
| A Windows script is blocked by execution policy or signing requirements | Inspect the effective policy and all scopes. Keep organizational and intentionally configured restrictions unchanged. Ask the device owner for an approved route. Only the native setup's explicitly authorized, unmanaged-default case uses temporary Process-scope `RemoteSigned`; it does not change CurrentUser or LocalMachine. |
| A new Windows tab cannot find an installed tool | Close all relevant terminal windows and reopen Windows PowerShell from Start. A new tab can inherit the old terminal application's PATH. Re-resolve Git, Python, and OMP before proceeding. |
| WSL paths point under `/mnt/c` | Use the selected Ubuntu distribution's Linux home and Linux OMP asset. Do not mix Windows executable/configuration paths with the WSL attempt. `df` reports filesystem space; its mount name need not begin with `/home`. |
| The chosen WSL distribution shows VERSION 1 | Setting the default version affects new distributions only. Preserve the existing distribution and obtain owner-approved backup and conversion before proceeding. Do not unregister or reset it. |
| A fresh macOS terminal cannot find Homebrew or Python | Check the saved `brew shellenv` and versioned Python PATH settings for the actual shell, then open another independent terminal. Do not repair PATH inside the verification block. |

## When local n8n stops

Keep **n8n READY/HOLD** separate from the OMP setup report and live OMP readiness result. Module 6 requires n8n READY; its checks need no paid model call, n8n Cloud signup, or Assistant key. Use the complete n8n section in your chosen platform guide after resolving the first failure.

| Observation | Next action |
|---|---|
| Docker is installed but `docker info` cannot reach the daemon | Confirm the intended local context and whether Desktop or the approved Linux service is stopped. Have the owner approve startup and its effect on existing work, then repeat in the intended new shell. A CLI version alone is insufficient. Do not reinstall or switch contexts blindly. |
| `docker compose version` fails | Install only the approved missing modern Compose plugin through the platform route. Legacy `docker-compose` alone is insufficient. A working modern plugin reporting 5.x is acceptable; do not downgrade it to obtain a 2.x label. |
| Linux Docker access is denied | Ask the owner to approve ordinary-account access. Docker-group membership grants root-equivalent control and requires a fresh login. Do not use root for the n8n installer or make the socket world-writable. |
| Docker Desktop cannot reach the selected WSL Ubuntu | Check **Settings → General → Use WSL 2 based engine** and **Settings → Resources → WSL Integration** for the exact selected distro. Save affected work before an approved Apply/restart. Resolve an existing independent Ubuntu daemon with its owner; do not install a second one. Repeat `docker info` and `docker compose version` in that Ubuntu shell. |
| WSL, virtualization, privileged Docker-in-Docker, or Desktop licensing is blocked or unresolved | Record n8n HOLD and send the exact policy/license/approval issue to the device owner. Do not bypass it. On the native PowerShell route, preserve native OMP, Python, Git, credentials, and earlier readiness results; WSL Ubuntu is the n8n bridge only. |
| Port 5678 is occupied or startup reports “address already in use” | Identify the application and engine with the owner. On Windows, inspect both Windows and Ubuntu listeners. Do not kill another application, change its port, or silently select another n8n address. |
| `$HOME/n8n-course` already exists, including an empty directory, symlink, or partial attempt | Preserve it. Do not run either installer over it. Have the owner identify its Compose project, version, data, and port. An “existing install” message proves neither version nor readiness. Use lifecycle commands only after confirming the intended course instance and actual Compose path. |
| Project-name inspection finds containers, volumes, networks, or an existing `.course-project` | Preserve everything. For an existing installation, confirm its actual identity with the owner. Do not register it as fresh, remove resources, or choose a new name to disguise a restart. |
| `course_n8n` reports a variable name followed by HOLD, or cannot read its project record | Stop before starting or stopping containers. Resolve exported overrides in an owner-approved clean shell and confirm the existing project record and engine. Do not print secret values, automatically unset variables, or recreate a missing record for an existing installation. |
| An image registry pull fails | Keep the registry/image name and first network, proxy, TLS, authentication, rate-limit, or architecture error. Resolve it with the owner before repeating the course start. Do not disable TLS, change image tags, prune volumes, or replace the full stack. |
| Running n8n reports anything except `2.41.5` | Record n8n HOLD, preserving the observed version and instance. Owner resolution is required; do not silently repin, upgrade, migrate, or replace it. |
| `sandbox-certs` shows `Exited (0)` | This is successful one-shot completion. The other five services should remain running, with health checks healthy where shown. A nonzero certificate exit, missing service, persistent restart, or unhealthy service is HOLD. Allow initial startup to settle and inspect again; preserve persistent failures. |
| The published port is `0.0.0.0:5678` or `[::]:5678` | Stop only the identified course stack using its guide’s ordinary `down`. Resolve the Compose mapping to `127.0.0.1:5678:5678` before restarting. Preserve its volumes and other services. |
| The browser asks for Cloud signup, payment, or a provider key | Confirm `http://localhost:5678` and the inspected course instance. A fresh local owner uses **Next**; the optional survey uses **Get started**. Select **Skip** on the free-license offer and **Set up later in Settings** for Assistant. Do not enter the OpenRouter key. |
| Local login fails, or an existing instance unexpectedly shows owner setup | Preserve the instance. Confirm the engine, project, port, and existing local login with its owner. Do not reset the account or register a replacement owner. |
| The empty instance has no “Create Workflow” button or mandatory “Saved” label | The observed Apple Silicon UI uses **Overview → Build a workflow**. Click the title, enter the readiness name, and press **Enter**; saving is automatic. Reload and confirm the name and blank canvas. Do not publish. If the observed UI prevents this, preserve the state and ask for help. |
| The workflow disappears after reload or after `down` / `up -d` | Record n8n HOLD. Keep the directory and volumes; confirm the same engine, Compose path/project, and named data volume with the owner. Ordinary `down` preserves named data. Never use `down -v`, prune volumes, or create a replacement workflow to hide failed persistence. |

The UI and runtime observations above were made on Apple Silicon only. Each device still needs its own successful checks. Share only redacted errors and state observations; never include `.env`, resolved Compose configuration, local passwords, or provider keys.

## Confirm the command you are actually running

These checks make no provider call and print no credential. Run the block in the same terminal that failed.

**Terminal: Bash or zsh, ordinary user.**

```bash
command -v omp && omp --version
```

**Terminal: PowerShell, ordinary user.**

```powershell
$ompCommand = Get-Command omp -CommandType Application -ErrorAction Stop
$ompCommand.Source
& $ompCommand.Source --version
if ($LASTEXITCODE -ne 0) { throw 'HOLD: the selected OMP executable failed its version check.' }
```

**Expected:** The path is the installation you verified, and the version is exactly `omp/18.3.5`.

**Stop:** The command is missing, resolves to an unexpected installation, fails to run, or reports another version.

**Recovery:** Correct only the installation or PATH issue identified by the output. Preserve other installations and repeat the check before a paid turn.

**PATH** is the ordered list of directories searched for a command name. Changing it does not install a program, and an already open terminal does not automatically receive later configuration changes. Credential variables have a different lifecycle: keep the key process-local even if you save a non-secret PATH setting.

## Distinguish slow work from a stopped process

Keep the original terminal visible. Use Activity Monitor on macOS, Task Manager on Windows, or your Linux system monitor to inspect the named download or package-manager process and its current CPU, disk, and network activity. No activity in one observation is not proof of a hang.

Follow the package manager's own recovery instructions if installation was interrupted; do not kill or restart a transaction blindly. For a provider turn, the launcher has a bounded timeout and records an incomplete attempt. Let that boundary report the failure rather than launch a second paid process to see whether it is faster.

## Capture a support packet

```text
Platform, version, and architecture:
Terminal and privilege level:
Step title:
Command or UI action, with no key value:
Resolved tool path and version:
First error and exit code:
Expected observation:
Last known-good observation:
What changed immediately before the failure:
External attempt/report location:
Whether any output or forbidden effect appeared:
```

Redact personal paths, account IDs, internal hosts, and credentials from the copy you share. Keep command names, versions, exit codes, and the first error. An exposed key must be revoked; deleting it from a screenshot does not revoke access.

Make one targeted correction and repeat the failed check. If a correction cannot be explained, a rollback fails, or device policy blocks the action, record `HOLD` and contact the responsible owner. Do not disable certificate checks, Gatekeeper, antivirus, or protected filesystem permissions to force progress.
