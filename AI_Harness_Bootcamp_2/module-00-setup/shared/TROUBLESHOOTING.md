# When setup stops

Start with the first action that failed. Save its exact error and the last thing you saw work before changing anything. Don't reinstall every tool or discard an existing checkout.

## Choose the next action from the observed failure

| What you see | What to do next |
|---|---|
| Git or Python is missing | Return to the named platform's prerequisite step. On a managed device, stop when policy blocks installation and send the support packet below. |
| A download fails | Keep the HTTP, proxy, or certificate error. Use the official release URLs. Do not disable TLS verification or execute an incomplete download. |
| The checksum fails or the selected asset has no unique checksum entry | Do not install or execute the binary. Keep the failed download separate. Check the filename, release, and source before downloading into a new directory. |
| `omp` is not found | Check the resolved command path below. Add only the user-bin directory named by your platform guide, then check again in the intended terminal. |
| `omp` reports a different version | Note the path and version you found. Do not silently overwrite a different installation. Use the verified course binary and confirm that PATH resolves to it. |
| A course directory already exists | Confirm that it is the intended checkout. Use it without reset, pull, or clean when it is valid; otherwise leave it untouched and resolve the path conflict. |
| Git cannot read the private course repository | A website password is not GitHub access. Follow the platform's read check with prompts disabled, then use the browser-login steps if needed. Even after you log in to GitHub, you need permission to read the repository. Ask the repository owner about the invitation or organization approval, and keep any existing checkout. |
| GitHub CLI reports unapproved credential storage | Stop before configuring the Git helper or cloning. Ask the device owner to set up approved credential storage or approved Git credentials. Do not request plaintext storage or share authentication output. |
| The conditional GitHub CLI package is unavailable | Use only the named platform's official package route. Ubuntu's `gh` requires Universe; ask the owner to approve that component if unavailable. Do not silently add sources. Arch's `github-cli` installation uses a full upgrade, not a partial upgrade. |
| The new terminal has tools but the key is `MISSING` | That's expected in a terminal you opened fresh, not from an earlier window. Enter the key through the hidden-input step in that terminal. Never put the key in a shell profile. |
| A new process reports an unexpected `SET` | Check whether the new process inherited its environment from a parent process. `SET` alone does not tell you whether the key was saved or exposed. Do not include an environment dump in the evidence. |
| The launcher exits 2 | Read its prerequisite message. Missing key, wrong OMP version, missing input, conflicting permissions, or an existing attempt can stop before a provider request. No live success has occurred. |
| The launcher exits 1 | Keep the entire attempted run. Check `result.json` and the raw receipts. A file left behind does not make an incomplete turn successful. |
| The provider returns 401 or 403 | Confirm the participant key and model access in OpenRouter without printing the key. Do not try a direct-provider login or silently switch models. |
| The provider returns 402 or 429 | Stop paid work. Keep the response and sort out credit or rate availability before starting a new attempt on purpose. Do not loop retries. |
| The assistant claims it wrote a file, but the file or receipt is absent | Record `HOLD`. Check the declared work root and authorized filename. Do not create the file yourself or use chat text in place of a tool-write receipt. |
| A write or evidence destination already exists | Keep that attempt. After you record the cause, start with new work/output and receipt paths. Changing only E does not make an existing output new. |
| A Windows script is blocked by execution policy or signing requirements | Check the effective policy and every scope. Leave organizational and intentionally configured restrictions as they are, and ask the device owner for an approved route. Temporary Process-scope `RemoteSigned` applies only to the native setup when the unmanaged default is explicitly authorized; it does not change CurrentUser or LocalMachine. |
| A new Windows tab cannot find an installed tool | Close all relevant terminal windows and reopen Windows PowerShell from Start. A new tab can inherit the old terminal application's PATH. Check which Git, Python, and OMP commands the reopened terminal finds before proceeding. |
| WSL paths point under `/mnt/c` | Use the selected Ubuntu distribution's Linux home and Linux OMP asset. Do not mix Windows executable/configuration paths with the WSL attempt. `df` reports filesystem space; its mount name need not begin with `/home`. |
| The chosen WSL distribution shows VERSION 1 | Setting the default version affects new distributions only. Keep the existing distribution and get the owner's approval for backup and conversion before proceeding. Do not unregister or reset it. |
| A fresh macOS terminal cannot find Homebrew or Python | Check the saved `brew shellenv` and versioned Python PATH settings for the shell you use, then open another independent terminal. Do not repair PATH inside the verification block. |

## When local Obsidian stops

Save the first error, app version, platform, attempt folder, and the last action you saw in the Obsidian window before changing anything. Keep **Obsidian READY/HOLD** separate from OMP and n8n. Module 2 needs local Obsidian READY; another editor or a disk PASS cannot replace a record of what you actually saw in Obsidian. Use your existing guide's **Set up local Obsidian** section: [native Windows](../platforms/windows-powershell.md#set-up-local-obsidian), [WSL Ubuntu](../platforms/windows-wsl.md#set-up-local-obsidian), [macOS](../platforms/macos.md#set-up-local-obsidian), [Ubuntu](../platforms/ubuntu.md#set-up-local-obsidian), or [Arch](../platforms/arch-linux.md#set-up-local-obsidian).

| What you see | What to do next |
|---|---|
| Obsidian is absent or installation is blocked | Use the guide's approved official route and [reference asset table](VERSIONS.md#local-obsidian-for-module-2). Record Obsidian HOLD if device policy or install approval blocks it. Keep the OMP and n8n results; do not disable Gatekeeper, antivirus, or package-signature checks. |
| Obsidian already exists, possibly at another version | Keep its binary, profile, and personal vaults. Record the version you have and use a new local practice vault. Complete the same steps in the app without forcing an upgrade, downgrade, profile reset, or replacement. |
| Asset SHA-256 differs from the reference value | Do not execute it. Keep the filename, source URL, expected hash, hash you got, and failed download. Resolve the release or architecture mismatch before downloading to a new location. Use the [official release metadata](https://api.github.com/repos/obsidianmd/obsidian-releases/releases/tags/v1.13.7); renaming a file does not verify it. |
| Arch package version differs from the reference 1.13.7-2 | Record the signed Extra version you have and check whether Obsidian is ready. Use only the guide's approved full-upgrade route; never downgrade or run a partial upgrade to match the reference version. See [Arch maintenance](https://wiki.archlinux.org/title/System_maintenance#Partial_upgrades_are_unsupported). |
| WSL command-line tools work but Obsidian has no window | Record Obsidian HOLD. Check the [WSLg requirement](https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps): build 19044+ or Windows 11, WSL 2, and GUI support in the selected Ubuntu. Builds 19041–19043 cannot use this windowed-app route. Keep the distribution and ask for an approved time to update and restart. Do not shut down active Docker or another distribution without approval. |
| WSL vault is a UNC path or lies under `/mnt/c` | Stop this attempt and keep it. Use Linux Obsidian and a fresh readiness root in the same Ubuntu Linux home as OMP. Do not use native Windows Obsidian on the WSL vault, relocate earlier work, or create a synchronized duplicate. |
| Linux reports a missing display or cannot open the window | Confirm that you are in the intended graphical desktop or WSLg session, not a headless/remote-only shell. Keep the exact display error and use the owner's approved way to open the app window. A CLI launch without a usable window is HOLD. |
| Ubuntu ARM64 AppImage reports missing FUSE | Use the guide's owner-approved apt step for `libfuse2t64` on Ubuntu 24.04/26.04. Keep FUSE 3; do not replace it with obsolete `fuse`. See [AppImage's FUSE guidance](https://docs.appimage.org/user-guide/troubleshooting/fuse.html). If the approved package is unavailable, stay on HOLD. |
| ARM64 AppImage renderer sandbox prevents launch, or exception approval is absent | The vendor's [AppImage route](https://github.com/obsidianmd/obsidian-help/blob/master/en/Getting%20started/Download%20and%20install%20Obsidian.md) uses `--no-sandbox`, which disables Chromium's renderer sandbox for this app. Get separate approval from the device owner through the platform step or keep Obsidian HOLD. Do not change kernel-wide security, make binaries world-writable, or improvise privileged sandbox fixes. |
| `initialize` reports an existing, linked, or overlapping root | Keep that root, even if the attempt is incomplete. Choose a fresh local child outside every checkout and outside synced folders. On WSL, use its Linux home. Never remove an existing root to make the command pass. |
| `Start` or `Token` links are absent, or a link creates an empty note | Confirm that Obsidian opened this attempt's `vault` child, not its parent or the checkout. Use Reading view to follow `Start` → `Token` → `Reply`. Keep any supplied notes that were altered and the failed attempt. If the notes' content changed, initialize a fresh root. |
| `check` reports that the saved reply does not match | In the same vault's Obsidian window, follow `Token` and replace `Reply` with only its current token on one line. Save with Cmd+S on macOS or Ctrl+S on Windows/Linux, then rerun `check` against the same root. Keep the failed check record. Do not edit the external expected record. |
| `refresh` succeeds but Obsidian still shows the old token | Confirm the open vault and helper root match. Return to `Token` and watch for the change in Obsidian. If the old token remains, keep a record of what you saw and record HOLD. Do not keep rotating the token, copy it from the terminal, or use another editor to show that Obsidian refreshed. You still need to see Obsidian's [external-refresh behavior](https://github.com/obsidianmd/obsidian-help/blob/master/en/Files%20and%20folders/How%20Obsidian%20stores%20data.md) work on your device. |
| The reply changes or disappears after closing/reopening | Confirm the reopened vault is the same local folder and that Sync remains off. Keep a record of the failure. Fix the save or path issue you found, then repeat the affected edit, save, and reopen steps in Obsidian and check the file on disk. If you never saw the external refresh in Obsidian, that part remains HOLD. |
| Helper reports changed expected identity, changed source, or an interrupted operation | Keep the whole attempt, including any `.readiness-operation` directory. Do not hand-edit records or remove locks to obtain PASS. Resolve the cause and use a fresh root for a complete new sequence. |
| Helper prints its qualified PASS but no one watched the GUI actions in Obsidian | The disk record shows what happened on disk, not what happened in Obsidian. Follow the link/edit/save/refresh/reopen steps in your [platform guide](../README.md#set-up-local-obsidian) and record what you see in the Obsidian window before recording Obsidian READY. Never change `gui_observed: false` in the helper's receipt. |

Run the helper in a terminal as an ordinary user, and make edits in the Obsidian window. Keep Restricted community plugins on and Sync off. An account, plugin, MCP service, or provider call cannot repair this readiness check. Follow the [hidden-input credential procedure](CREDENTIALS.md), and never store a provider key in notes, a shell profile, or another secret file. When you report Obsidian HOLD, keep the earlier OMP and n8n results and every failed attempt.

## When local n8n stops

Keep **n8n READY/HOLD** separate from the OMP setup report and the live OMP readiness result. Module 7 requires n8n READY, but checking n8n needs no paid model call, n8n Cloud signup, or Assistant key. Once you have fixed the first failure, use the complete n8n section in your chosen platform guide.

| What you see | What to do next |
|---|---|
| Docker is installed but `docker info` cannot reach the daemon | Check that Docker points to the intended local context and whether Desktop or the approved Linux service is stopped. Ask the owner to approve starting it and any effect on existing work, then repeat the check in the intended new shell. A CLI version alone does not show that the daemon is reachable. Do not reinstall or switch contexts without checking. |
| `docker compose version` fails | Install only the approved missing modern Compose plugin through the platform route. Legacy `docker-compose` alone will not do. If the modern plugin works and reports 5.x, keep it; do not downgrade it to get a 2.x label. |
| Linux Docker access is denied | Ask the owner to approve access from your ordinary account. Docker-group membership gives root-equivalent control and requires you to log in again. Do not use root for the n8n installer or make the socket world-writable. |
| Docker Desktop cannot reach the selected WSL Ubuntu | Check **Settings → General → Use WSL 2 based engine** and **Settings → Resources → WSL Integration** for the exact selected distro. Save affected work before an approved Apply/restart. If Ubuntu already has its own independent daemon, resolve that with its owner; do not install a second one. Repeat `docker info` and `docker compose version` in that Ubuntu shell. |
| WSL, virtualization, privileged Docker-in-Docker, or Desktop licensing is blocked or unresolved | Record n8n HOLD and send the exact policy, license, or approval issue to the device owner. Do not bypass it. If you use native PowerShell, keep native OMP, Python, Git, credentials, and earlier readiness results. Use WSL Ubuntu only as the bridge to n8n. |
| Port 5678 is occupied or startup reports “address already in use” | Identify the application and engine with the owner. On Windows, inspect both Windows and Ubuntu listeners. Do not kill another application, change its port, or silently select another n8n address. |
| `$HOME/n8n-course` already exists, including an empty directory, symlink, or partial attempt | Leave it in place, and do not run either installer over it. Ask the owner to identify its Compose project, version, data, and port. An “existing install” message does not tell you its version or whether it is ready. Use commands that manage its lifecycle only after you confirm the intended course instance and actual Compose path. |
| Project-name inspection finds containers, volumes, networks, or an existing `.course-project` | Keep everything. If an installation already exists, confirm which installation it is with the owner. Do not register it as fresh, remove resources, or choose a new name to disguise a restart. |
| `course_n8n` reports a variable name followed by HOLD, or cannot read its project record | Stop before starting or stopping containers. With the owner's approval, sort out the exported overrides in a clean shell and confirm the existing project record and engine. Do not print secret values, automatically unset variables, or recreate a missing record for an existing installation. |
| An image registry pull fails | Keep the registry/image name and first network, proxy, TLS, authentication, rate-limit, or architecture error. Resolve it with the owner before repeating the course start. Do not disable TLS, change image tags, prune volumes, or replace the full stack. |
| Running n8n reports anything except `2.41.5` | Record n8n HOLD and keep the version and instance you found. The owner must resolve the mismatch. Do not repin, upgrade, migrate, or replace it on your own. |
| `sandbox-certs` shows `Exited (0)` | That service has finished its one-time job successfully. The other five services should stay running, with healthy health checks where shown. A nonzero certificate exit, missing service, persistent restart, or unhealthy service is HOLD. Let the initial startup settle and check again. Keep a record of failures that continue. |
| The published port is `0.0.0.0:5678` or `[::]:5678` | Use the guide's ordinary `down` to stop only the course stack you identified. Correct the Compose mapping to `127.0.0.1:5678:5678` before restarting, and keep its volumes and other services. |
| The browser asks for Cloud signup, payment, or a provider key | Confirm `http://localhost:5678` and the inspected course instance. A fresh local owner uses **Next**; the optional survey uses **Get started**. Select **Skip** on the free-license offer and **Set up later in Settings** for Assistant. Do not enter the OpenRouter key. |
| Local login fails, or an existing instance unexpectedly shows owner setup | Leave the instance as it is. Confirm the engine, project, port, and existing local login with its owner. Do not reset the account or register a replacement owner. |
| The empty instance has no “Create Workflow” button or mandatory “Saved” label | On the Apple Silicon Mac where these steps were checked, the empty instance offers **Overview → Build a workflow**. Click the title, enter the readiness name, and press **Enter**; saving is automatic. Reload and confirm the name and blank canvas. Do not publish. If your screens don't allow this, keep the instance as it is and ask for help. |
| The workflow disappears after reload or after `down` / `up -d` | Record n8n HOLD. Keep the directory and volumes. With the owner, confirm you are using the same engine, Compose path/project, and named data volume. Ordinary `down` keeps named data. Never use `down -v`, prune volumes, or create a replacement workflow to hide failed persistence. |

What the UI showed and how n8n ran were checked only on Apple Silicon. You still need successful checks on your own device. Share only errors with private details removed and a description of the system state you saw; never include `.env`, resolved Compose configuration, local passwords, or provider keys.

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

**Recovery:** Fix only the installation or PATH issue shown in the output. Keep other installations and repeat the check before a paid turn.

**PATH** is the ordered list of directories your terminal searches for a command. Changing PATH does not install a program, and a terminal you already have open does not automatically pick up settings saved later. The key works differently: keep it in the current terminal process only, even if you save a non-secret PATH setting.

## Distinguish slow work from a stopped process

Keep the original terminal visible. In Activity Monitor on macOS, Task Manager on Windows, or your Linux system monitor, find the named download or package-manager process and check its current CPU, disk, and network activity. A single check showing no activity does not mean the process has hung.

If an installation was interrupted, follow the package manager's recovery instructions instead of killing or restarting a transaction without checking. For a provider turn, the launcher times out after a set limit and records an incomplete attempt. Wait for it to report the failure instead of starting a second paid process to see whether that one is faster.

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

Make one targeted correction, then repeat the failed check. If you cannot explain a correction, a rollback fails, or device policy blocks the action, record `HOLD` and contact the responsible owner. Do not disable certificate checks, Gatekeeper, antivirus, or protected filesystem permissions to force progress.
