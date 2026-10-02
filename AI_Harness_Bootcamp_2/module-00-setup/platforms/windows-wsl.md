# Windows WSL 2 with Ubuntu setup

This path uses Windows Subsystem for Linux 2 with the Ubuntu distribution so that all course work happens inside the Linux filesystem under your Linux home directory. Plan for 90 to 180 minutes if any Windows feature enable or reboot is needed; this is a planning estimate, not a measured completion time. All course clone, work directories, evidence directories, and the Oh My Pi binary stay under the Linux `$HOME`. Never use `/mnt/c` for the course checkout or readiness-check work. Use the Linux `omp` binary and Linux configuration. Enter the provider key through the hidden prompt; investigate unexpected inherited key presence without displaying its value.

You need Git, Python 3.12 or newer inside Ubuntu, a browser, an ordinary text editor, and Oh My Pi 18.3.5 for Linux. The only provider key is `OPENROUTER_API_KEY`. The course launcher selects `openrouter/anthropic/claude-sonnet-4.6`. Module 6 also requires local n8n 2.41.5 through Docker Desktop, using this same Ubuntu distribution and Linux home. You do not install Node, npm, Obsidian, or another agent.

Keep an existing Ubuntu 24.04 or 26.04 WSL 2 installation. Do not unregister, reset, or replace it. The course checkout belongs at `$HOME/Documents/AIHB_OCT_2026`; work and evidence stay outside that checkout under the same Linux home.

## Check Windows and inspect distributions

Confirm the host is Windows 10 build 19041 or newer, or Windows 11, and still receives supported security updates under your device policy. The build floor alone does not establish current host support. Obtain device-owner approval before enabling features, installing software, or converting a distribution. Keep any policy-denial message and stop; do not bypass it. See [Microsoft's WSL installation requirements](https://learn.microsoft.com/en-us/windows/wsl/install).

Read the host build and both distribution lists before making changes.

**Terminal: Windows PowerShell, ordinary user, newly opened from Start.**

```powershell
Get-ComputerInfo -ErrorAction Stop | Select-Object WindowsProductName, WindowsVersion, OsBuildNumber
wsl --version
Write-Output ('WSL package-version exit: ' + $LASTEXITCODE)
wsl --list --verbose
Write-Output ('Installed-list exit: ' + $LASTEXITCODE)
wsl --list --online
if ($LASTEXITCODE -ne 0) { throw 'STOP: save the online-list error before any installation.' }
```

**Expected:** WSL component versions (record the package version separately from each distribution’s VERSION), a supported host meeting the Microsoft installation floor, either an installed-distribution list or an explicit message that no distributions are installed, and a successful online list. Record the exact name and VERSION of any existing Ubuntu you intend to use. A name alone does not establish its Ubuntu release; the Linux check below does that.

**Stop:** unsupported host, an unavailable WSL command, policy denial, an installed-list error other than the explicit no-distributions state, or an online-list failure.

**Recovery:** If the only finding is that no distributions are installed, use the approved named installation below. For a different failure, preserve the output and ask the device owner to resolve that specific prerequisite using [Microsoft's installation troubleshooting](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting#installation-issues). Manual Windows-feature recovery belongs with the owner; do not paste feature-enabling commands from another route.

The Microsoft simplified-install floor above does not establish Docker Desktop eligibility. The separate n8n host check below applies Docker’s stricter requirements. Missing package-version output needs owner review before Docker setup; keep the existing distributions.

## Install Ubuntu only when a suitable distribution is absent

Skip this section for an existing suitable Ubuntu. If an installed Ubuntu release is unknown, use the exact selection and named launch below to inspect it before deciding to install anything. For a new install, first confirm that the online list contains the exact NAME `Ubuntu-24.04`. Do not substitute the moving `Ubuntu` alias. Open PowerShell with **Run as administrator** after the owner approves the install.

Install that named release. Microsoft's `--install` route creates new distributions as WSL 2. Setting a default with `wsl --set-default-version 2` affects **new** distributions only; it does not convert an existing WSL 1 installation.

**Terminal: Windows PowerShell, elevated, newly opened for the approved installation.**

```powershell
wsl --list --online
if ($LASTEXITCODE -ne 0) { throw 'STOP: online list failed.' }
$CourseInstallName = Read-Host 'Type Ubuntu-24.04 only if that exact NAME appears in the online list'
if ($CourseInstallName -cne 'Ubuntu-24.04') { throw 'STOP: the exact pinned distribution was not confirmed.' }
wsl --install -d Ubuntu-24.04
if ($LASTEXITCODE -ne 0) { throw 'STOP: preserve the install message; complete any requested restart before rechecking.' }
```

**Expected:** Ubuntu-24.04 installs, or Windows requests a restart. Save open work and restart Windows when requested. Do not paste Linux commands into PowerShell. If installation opens Ubuntu and asks for a username, create an ordinary Linux username and password there; password characters are invisible. Wait until that setup finishes before continuing.

**Stop:** the exact release is unavailable, help text appears instead of installation, or installation fails.

**Recovery:** keep the message and use the linked Microsoft troubleshooting with the owner. After a requested restart, inspect the installed list again before doing anything else. Do not reinstall an existing distribution.

## Select the exact distribution

Open ordinary PowerShell after any restart. Enter the exact installed NAME at the prompt, even if it differs from `Ubuntu-24.04`. This preserves an existing Ubuntu 26.04 or a differently named valid Ubuntu installation.

**Terminal: Windows PowerShell, ordinary user, newly opened from Start.**

```powershell
wsl --list --verbose
if ($LASTEXITCODE -ne 0) { throw 'STOP: could not inspect installed distributions.' }
$CourseDistroNames = @(wsl --list --quiet)
if ($LASTEXITCODE -ne 0) { throw 'STOP: could not read distribution names.' }
$CourseDistroNames = @($CourseDistroNames | ForEach-Object { ($_ -replace "`0", '').Trim() } | Where-Object { $_ })
$CourseDistro = Read-Host 'Enter the exact installed Ubuntu NAME you intend to use'
if ($CourseDistroNames -cnotcontains $CourseDistro) { throw 'STOP: that exact name is not installed.' }
$CourseWslVersion = Read-Host 'Enter the VERSION shown for that exact NAME in the verbose list'
if ($CourseWslVersion -notin @('1', '2')) { throw 'STOP: inspect the VERSION column again.' }
```

**Expected:** the name matches an installed entry, and its VERSION is `2`.

**Stop:** the selected name is absent, its release is unknown, or its VERSION is `1`.

**Recovery:** an unknown release can be inspected with the named launch below, but do not continue to packages until the Linux release check passes. A VERSION `1` entry requires the separate approved conversion below. Do not assume setting the default converted it.

### Convert an existing WSL 1 distribution only with approval

Skip this step when the selected entry already shows VERSION `2`. Conversion can take time and can fail. Ask the owner to approve it and make a recoverable backup first using [Microsoft's export and import commands](https://learn.microsoft.com/en-us/windows/wsl/basic-commands#export-a-distribution). The owner chooses a new backup destination with enough space, exports the exact selected distribution, and confirms the backup is usable before conversion. Preserve the original and the backup.

Convert only the name validated in the preceding block, after backup confirmation.

**Terminal: Windows PowerShell, ordinary user, same selection window; owner-approved conversion only.**

```powershell
if (-not $CourseDistro -or $CourseDistroNames -cnotcontains $CourseDistro -or $CourseWslVersion -ne '1') { throw 'STOP: select and validate the WSL 1 entry first.' }
$CourseConversion = Read-Host 'Type BACKUP READY only after the owner approves conversion and confirms a recoverable backup'
if ($CourseConversion -cne 'BACKUP READY') { throw 'STOP: conversion is not approved and backed up.' }
wsl --set-version $CourseDistro 2
if ($LASTEXITCODE -ne 0) { throw 'STOP: preserve the conversion error and backup.' }
wsl --list --verbose
if ($LASTEXITCODE -ne 0) { throw 'STOP: could not verify the converted distribution.' }
```

**Expected:** the exact selected NAME now shows VERSION `2`.

**Stop:** conversion fails or the entry still shows `1`.

**Recovery:** keep the distribution and backup intact and ask the owner to resolve the reported failure. Never unregister or reset as a repair.

## Launch and verify Ubuntu

Confirm the exact selected NAME shows VERSION `2` in the Windows list before launching. If a first launch asks for a Linux username and password, complete those prompts now. Choose an ordinary username; the password entry shows no characters. Existing installations should retain their existing user.

Launch the selected distribution by name, starting at its Linux home.

**Terminal: Windows PowerShell, ordinary user, same selection window.**

```powershell
if (-not $CourseDistro -or $CourseDistroNames -cnotcontains $CourseDistro) { throw 'STOP: select the installed distribution first.' }
wsl --distribution $CourseDistro --cd ~
if ($LASTEXITCODE -ne 0) { throw 'STOP: the named Ubuntu session returned an error.' }
```

**Expected:** Ubuntu opens as your ordinary Linux user. The PowerShell exit check runs when you leave Ubuntu.

**Stop:** launch fails or first-user setup does not finish.

**Recovery:** preserve the error and ask the owner to repair the selected distribution without resetting it.

Check the user, home, release, shell, and processor inside that Ubuntu window.

**Terminal: Ubuntu Bash, ordinary Linux user, newly launched named distribution.**

```bash
course_check_wsl_host() {
  [ -n "${BASH_VERSION:-}" ] && [ "$(id -u)" -ne 0 ] || { printf 'STOP: use Bash as your ordinary Linux user\n'; return 1; }
  whoami && cd "$HOME" && pwd -P || return 1
  case "$(pwd -P)" in /home/*) ;; *) printf 'STOP: home must be under Linux /home\n'; return 1 ;; esac
  [ "$HOME" = "$(pwd -P)" ] && [ -w "$HOME" ] || { printf 'STOP: home is redirected or not writable\n'; return 1; }
  cat /etc/os-release || return 1
  . /etc/os-release
  case "$ID:$VERSION_ID" in ubuntu:24.04|ubuntu:26.04) ;; *) printf 'STOP: use supported Ubuntu 24.04 or 26.04\n'; return 1 ;; esac
  case "$(uname -m)" in x86_64|aarch64|arm64) uname -m ;; *) printf 'STOP: unsupported processor\n'; return 1 ;; esac
  df -h "$HOME"
}
course_check_wsl_host
```

**Expected:** your ordinary username, a writable `/home/` path, Ubuntu `24.04` or `26.04`, and `x86_64` or `aarch64`/`arm64`. Read `df` only for available space: you need at least 25 GB. Its mount-point column need not start with `/home`.

**Stop:** root user, unsupported release/processor, redirected home, failed command, or less than 25 GB available.

**Recovery:** select the correct existing Ubuntu/user or ask the owner to provision a supported one. Free space in the Linux filesystem if needed; do not move course work under `/mnt/`.

## Check Git, Python, curl, and certificates

Check existing prerequisites before installing packages. Ubuntu's `python3` package supplies a supported interpreter on [24.04](https://packages.ubuntu.com/noble/python3) and [26.04](https://packages.ubuntu.com/resolute/python3).

**Terminal: Ubuntu Bash, ordinary Linux user, same Ubuntu window.**

```bash
course_check_wsl_packages() {
  local tool resolved
  for tool in git curl; do
    resolved="$(type -P "$tool")" || return 1
    resolved="$(readlink -f -- "$resolved")" || return 1
    case "$resolved" in /mnt/*|*.exe) printf 'STOP: Windows tool rejected\n'; return 1 ;; /*) ;; *) return 1 ;; esac
    "$resolved" --version || return 1
  done
  [ "$(dpkg-query -W -f='${Status}' ca-certificates 2>/dev/null)" = 'install ok installed' ] &&
    [ -s /etc/ssl/certs/ca-certificates.crt ] || { printf 'STOP: certificate package or trust bundle missing\n'; return 1; }
  printf 'Git, curl, and certificates present; check Python next\n'
}
course_check_wsl_packages
```

**Expected:** Git and curl versions, then the certificate confirmation. Also run the Python check below. Skip package installation only when all these checks pass, including Python 3.12 or newer.

**Stop:** any prerequisite is absent or resolves to Windows.

**Recovery:** install the missing prerequisites with the following package step after device-owner approval. Do not bypass certificate verification.

Install the prerequisites only if the checks found something missing. At a `sudo` password prompt, enter your Linux password; no characters appear.

**Terminal: Ubuntu Bash, ordinary Linux user invoking sudo for package changes, same window.**

```bash
sudo apt-get update && sudo apt-get install -y git python3 curl ca-certificates
```

**Expected:** both package operations finish successfully. Recheck prerequisites and resolve Python below.

**Stop:** a package has no candidate, a source is unavailable, or permission is denied.

**Recovery:** keep the apt output and ask the owner to repair the approved Ubuntu sources. Do not add sources or upgrade the whole system to get past this check.

## Choose the Python interpreter

Later steps call one real Python executable by its absolute path. That path is `PY`. This step keeps the first of `python3.12`, `python3`, or `python` that reports version 3.12 or newer through `sys.executable`. A version line from an older interpreter is not a pass. Resolve and execute the first suitable Linux interpreter.

**Terminal: Ubuntu Bash, ordinary Linux user, same Ubuntu window.**

```bash
course_resolve_python() {
  PY="$(for candidate in python3.12 python3 python; do
    candidate_path="$(type -P "$candidate")" || continue
    candidate_path="$(readlink -f -- "$candidate_path")" || continue
    case "$candidate_path" in /mnt/*|*.exe) continue ;; /*) ;; *) continue ;; esac
    "$candidate_path" -c 'import os, pathlib, sys; p=pathlib.Path(sys.executable).resolve(); sys.exit(1) if sys.platform != "linux" or sys.version_info < (3,12) or str(p).startswith("/mnt/") or str(p).lower().endswith(".exe") or not os.access(p,os.X_OK) else print(p)' 2>/dev/null && break
  done)"
  if [ -n "$PY" ] && [ -x "$PY" ]; then
    printf 'PY %s\n' "$PY"
    "$PY" --version || return 1
    return 0
  fi
  printf 'STOP: no real Python executable is version 3.12 or newer\n' >&2
  return 1
}
course_resolve_python
```

**Expected:** A line starting with `PY ` gives an absolute path on the Linux filesystem, and the next line starts with `Python 3.12` or newer.

**Stop:** You see the STOP line, no `PY` line, a version below 3.12, or a path that starts with `/mnt/` or ends in `.exe`.

**Recovery:** Return to the package step if no supported Linux Python was found. Do not point `PY` at a Windows Python under `/mnt/c`. Do not upgrade the whole system to get past this stop.

## Put the user bin on PATH inside Ubuntu

PATH is the list of folders this terminal searches when you type a command name. The export in this window lasts only until you close it. A later window finds `omp` only if a startup file that window actually reads contains the same line.

Bash login shells read the first available file in this order: `.bash_profile`, `.bash_login`, `.profile`. Interactive non-login shells read `.bashrc`. Preserve that [Bash startup-file precedence](https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html); do not create a new override file. Add the nonsecret PATH line to `.profile`, `.bashrc`, and an existing login override, if present.

Save the PATH line without replacing existing contents or following profile links.

**Terminal: Ubuntu Bash, ordinary Linux user, same Ubuntu window.**

```bash
course_persist_wsl_path() {
  "$PY" - <<'PY'
from pathlib import Path
home = Path.home()
if home.resolve() != home or not str(home).startswith('/home/'):
    raise SystemExit('STOP: use an unredirected Linux home')
for folder in (home/'.local', home/'.local/bin'):
    if folder.is_symlink() or (folder.exists() and not folder.is_dir()):
        raise SystemExit('STOP: preserve redirected or non-directory user bin')
files = [home/'.profile', home/'.bashrc']
for name in ('.bash_profile', '.bash_login'):
    candidate = home/name
    if candidate.exists() or candidate.is_symlink():
        files.append(candidate)
        break
for file in files:
    if file.is_symlink() or (file.exists() and not file.is_file()):
        raise SystemExit('STOP: startup file is not an ordinary file: ' + str(file))
line = b'export PATH="$HOME/.local/bin:$PATH"'
(home/'.local/bin').mkdir(parents=True, exist_ok=True)
for file in files:
    raw = file.read_bytes() if file.exists() else b''
    if line in raw.split(b'\n'):
        print('PATH_LINE already present in', file)
        continue
    with file.open('ab') as output:
        output.write((b'\n' if raw and not raw.endswith(b'\n') else b'') + line + b'\n')
    print('PATH_LINE added to', file)
PY
  local course_exit=$?
  [ "$course_exit" -eq 0 ] || return "$course_exit"
  export PATH="$HOME/.local/bin:$PATH"
}
course_persist_wsl_path
```

**Expected:** each selected startup file prints `PATH_LINE already present` or `PATH_LINE added`. Existing bytes remain intact, including a last line that lacked a newline. Only this setup window receives an immediate PATH export.

**Stop:** a link, non-file, redirected home/bin, or permission error appears.

**Recovery:** preserve the files and ask the device owner to resolve the named path. Do not replace a linked profile. After correction, save PATH here and prove it in a separate new Ubuntu window.

## Download Oh My Pi and verify it before it can run

You download the selected Linux binary and `SHA256SUMS.txt` from the pinned release into a new directory that belongs only to this attempt. The published file lists a lowercase SHA-256 fingerprint, two spaces, then the exact filename. Nothing is moved into place and nothing is made executable unless that exact line matches the downloaded file.

Download and verify the matching asset from [Oh My Pi v18.3.5](https://github.com/can1357/oh-my-pi/releases/tag/v18.3.5).

**Terminal: Ubuntu Bash, ordinary Linux user, same Ubuntu window.**

```bash
course_install_wsl_omp() {
  arch="$(uname -m)" || return 1
  case "$arch" in
    x86_64) asset=omp-linux-x64 ;;
    aarch64|arm64) asset=omp-linux-arm64 ;;
    *) printf 'HOLD: unsupported Linux architecture.\n' >&2; return 1 ;;
  esac
  download="$HOME/course-evidence/wsl-omp-$(date -u +%Y%m%dT%H%M%SZ)-$$/download"
  dest="$HOME/.local/bin/omp"
  "$PY" - "$download" "$dest" <<'PY'
from pathlib import Path
import sys
home = Path.home()
for value in sys.argv[1:]:
    path = Path(value)
    if not str(home).startswith('/home/') or home.resolve() != home or path.resolve() != path or not path.is_relative_to(home):
        raise SystemExit('HOLD: path is redirected or outside Linux home')
Path(sys.argv[1]).mkdir(parents=True, exist_ok=False)
PY
  local course_exit=$?
  [ "$course_exit" -eq 0 ] || return "$course_exit"
  base=https://github.com/can1357/oh-my-pi/releases/download/v18.3.5
  curl --fail --location --output "$download/$asset" "$base/$asset" || return 1
  curl --fail --location --output "$download/SHA256SUMS.txt" "$base/SHA256SUMS.txt" || return 1
  "$PY" - "$download" "$asset" "$dest" <<'PY'
from pathlib import Path
import hashlib, re, sys
folder, asset, target = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3])
entries = [line.split() for line in (folder/'SHA256SUMS.txt').read_text().splitlines()]
selected = [row for row in entries if len(row) >= 2 and row[1].removeprefix('*') == asset]
if len(selected) != 1 or len(selected[0]) != 2 or not re.fullmatch(r'[0-9a-fA-F]{64}', selected[0][0]):
    raise SystemExit('HOLD: no unique valid checksum for selected asset')
expected = selected[0][0]
raw = (folder/asset).read_bytes()
digest = hashlib.sha256(raw).hexdigest()
if digest != expected.lower():
    raise SystemExit('HOLD: checksum mismatch; do not execute')
if target.is_symlink() or (target.exists() and (not target.is_file() or hashlib.sha256(target.read_bytes()).hexdigest()!=digest)):
    raise SystemExit('HOLD: preserve the different existing destination')
target.parent.mkdir(parents=True,exist_ok=True)
if not target.exists():
    with target.open('xb') as output:
        output.write(raw)
target.chmod(target.stat().st_mode | 0o100)
print('SHA256 VERIFIED',asset,digest)
PY
  course_exit=$?
  if [ "$course_exit" -ne 0 ]; then return "$course_exit"; fi
  version="$("$dest" --version)" || return 1
  printf '%s\n' "$version"
  [ "$version" = 'omp/18.3.5' ] || { printf 'HOLD: wrong pinned version\n'; return 1; }
}
course_install_wsl_omp
```

**Expected:** `SHA256 VERIFIED` identifies the selected Linux asset before first execution, followed by `omp/18.3.5`. The download folder remains as evidence. Only verified bytes become executable.

**Stop:** A download, checksum, destination, permission, or execution check fails. The function returns to your prompt without enabling persistent shell error-exit behavior.

**Recovery:** Keep the failed directory and existing installation. Resolve the specific error before using a new attempt; do not disable certificate checks, delete evidence, or run an unverified file.

## See the binary in this window

The export above is only for this window. It does not establish that a new window will find `omp`. Check that in the independent terminal later, without exporting PATH first. Check the selected binary here.

**Terminal: Ubuntu Bash, ordinary Linux user, same Ubuntu window.**

```bash
command -v omp &&
  [ "$(command -v omp)" = "$HOME/.local/bin/omp" ] &&
  "$HOME/.local/bin/omp" --version
```

**Expected:** `command -v` prints `$HOME/.local/bin/omp`, and the version line is `omp/18.3.5`.

**Stop:** `command -v` does not print that path, or the version is not `omp/18.3.5`.

**Recovery:** If `$HOME/.local/bin/omp` is missing, return to the download step. A new attempt keeps the old download folder. If a different `omp` is found earlier on PATH, do not overwrite it.

## Confirm private GitHub access

Check whether your existing Git credentials can read the course repository. A failed access check is an account or repository-access prerequisite, not a folder-permission problem.

**Terminal: Ubuntu Bash, ordinary Linux user, same Ubuntu window.**

```bash
GIT_TERMINAL_PROMPT=0 git ls-remote --exit-code https://github.com/TheHolofex/AIHB_OCT_2026.git HEAD
```

**Expected:** a commit hash followed by `HEAD`, with no credential prompt. If it succeeds, skip all GitHub CLI steps below and proceed to the checkout without changing helpers or login.

**Stop:** access fails or no HEAD is returned.

**Recovery:** preserve the error. Confirm network access and your repository invitation. Use the fallback below only if credentials need setup.

### Use GitHub CLI only for the access fallback

Check for an existing Linux GitHub CLI before installing it.

**Terminal: Ubuntu Bash, ordinary Linux user, same Ubuntu window.**

```bash
course_check_wsl_gh() {
  local resolved
  resolved="$(type -P gh)" && resolved="$(readlink -f -- "$resolved")" || return 1
  case "$resolved" in /mnt/*|*.exe) printf 'STOP: Windows gh rejected\n'; return 1 ;; /*) ;; *) return 1 ;; esac
  "$resolved" --version
}
course_check_wsl_gh
```

**Expected:** a Linux `gh` version. Skip the install block when it works.

**Stop:** gh is absent or resolves to Windows.

**Recovery:** ask the owner to approve installation from Ubuntu's [Universe gh package](https://packages.ubuntu.com/noble/gh). Universe must already be an approved configured source. If it is unavailable or unapproved, stop for the owner; do not silently enable it or add another source.

Install the fallback package only after that source approval. Enter your Linux password at the hidden `sudo` prompt if asked.

**Terminal: Ubuntu Bash, ordinary Linux user invoking sudo for package changes, same window.**

```bash
sudo apt-get update && sudo apt-get install -y gh
```

**Expected:** installation succeeds; repeat the gh check above.

**Stop:** no candidate, source failure, or permission denial.

**Recovery:** keep the apt message and have the owner resolve the approved source. Do not add a repository.

Sign in with the invited GitHub account. The next command presents a device code and browser authorization. Open the displayed GitHub page, enter that code, and verify the account before authorizing. GitHub credentials are separate from your course-site password and OpenRouter key. [GitHub CLI login](https://cli.github.com/manual/gh_auth_login) prefers an OS credential store but can fall back to a plaintext file; do not use `--insecure-storage`. If asked to configure Git during login, decline that change until storage has been reviewed below.

**Terminal: Ubuntu Bash, ordinary Linux user, same Ubuntu window; interactive login.**

```bash
gh auth login --hostname github.com --git-protocol https --web
```

**Expected:** browser authorization completes for the invited account.

**Stop:** denied authorization, wrong account, or login failure.

**Recovery:** preserve the nonsecret error and ask the repository owner to confirm the account/invitation before trying again.

Inspect account and storage status locally; do not share this output or request token display. See [gh auth status](https://cli.github.com/manual/gh_auth_status).

**Terminal: Ubuntu Bash, ordinary Linux user, same Ubuntu window.**

```bash
gh auth status --hostname github.com
```

**Expected:** successful status for the intended account, with storage approved by your device policy.

**Stop:** status fails, the account is wrong, or reported storage is not approved. If the storage location is unclear, stop for owner review.

**Recovery:** have the device owner provision approved storage or credentials. Do not continue merely because browser login succeeded.

Configure the credential helper for only github.com after storage approval, then repeat the disabled-prompt repository check. [Host-specific setup](https://cli.github.com/manual/gh_auth_setup-git) does not grant repository access.

**Terminal: Ubuntu Bash, ordinary Linux user, same Ubuntu window.**

```bash
gh auth setup-git --hostname github.com &&
  GIT_TERMINAL_PROMPT=0 git ls-remote --exit-code https://github.com/TheHolofex/AIHB_OCT_2026.git HEAD
```

**Expected:** a commit hash and `HEAD` after helper setup succeeds.

**Stop:** either command fails.

**Recovery:** preserve the error and ask the repository owner to confirm your invitation and access. Do not clone until this exact access check succeeds.

## Use the course checkout, or clone it once

The course lives at `$HOME/Documents/AIHB_OCT_2026`. An existing checkout of the course origin is used as it is. A different folder at that path is left alone. All paths stay inside the Linux home. Validate the destination and reuse or clone the course checkout.

**Terminal: Ubuntu Bash, ordinary Linux user, same Ubuntu window.**

```bash
course_checkout_wsl() {
R="$HOME/Documents/AIHB_OCT_2026"
origin=https://github.com/TheHolofex/AIHB_OCT_2026.git
"$PY" - "$R" <<'PY'
from pathlib import Path
import sys
home, target = Path.home(), Path(sys.argv[1])
if not str(home).startswith('/home/') or home.resolve() != home or target.resolve() != target or not target.is_relative_to(home):
    raise SystemExit('STOP: checkout path is redirected or outside Linux home')
if target.is_symlink() or (target.exists() and not target.is_dir()):
    raise SystemExit('STOP: preserve the existing checkout-path object')
PY
[ $? -eq 0 ] || return 1
if [ -d "$R" ]; then
  if [ ! -d "$R/.git" ] || [ -L "$R/.git" ] || ! git -C "$R" rev-parse --verify HEAD >/dev/null 2>&1; then
    echo "STOP: the home folder already has AIHB_OCT_2026, and it is not a Git checkout. It was not replaced."
    return 1
  fi
  remote=$(git -C "$R" remote get-url origin 2>/dev/null || true)
  if [ "$remote" != "$origin" ]; then
    echo "STOP: that checkout has a different origin. It was not replaced, reset, pulled, or cleaned."
    return 1
  fi
  echo "Using the existing course checkout."
else
  mkdir -p -- "$HOME/Documents" || return 1
  GIT_TERMINAL_PROMPT=0 git -c core.autocrlf=false clone "$origin" "$R"
  if [ $? -ne 0 ]; then
    echo "STOP: clone failed. No partial folder was cleaned up by this step."
    return 1
  fi
  echo "Cloned the course checkout."
fi
M="$R/AI_Harness_Bootcamp_2/module-00-setup"
lab="$M/shared/MODULE_00_LAB.md"
if [ ! -f "$lab" ]; then
  echo "STOP: this checkout does not contain the Module 0 lab. It was not reset, pulled, or cleaned."
  return 1
fi
"$PY" - "$R" "$M" <<'PY'
from pathlib import Path
import sys
root, module = map(Path, sys.argv[1:])
required = [root/'shared/run_omp.py', root/'shared/course_guard.mjs', module/'shared/MODULE_00_LAB.md', module/'shared/VERSIONS.md', module/'shared/case/verify_tool_proof.py', module/'scripts/verify-setup.sh']
for file in required:
    if file.resolve() != file or not file.is_file():
        raise SystemExit('STOP: required course file is missing or redirected; preserve checkout')
    if b'\r\n' in file.read_bytes():
        raise SystemExit('STOP: required course file has CRLF; preserve checkout without renormalizing')
print('Required course files present with LF line endings')
PY
[ $? -eq 0 ] || return 1
echo "$R"
echo "$M"
}
course_checkout_wsl
```

**Expected:** either `Using the existing course checkout.` or `Cloned the course checkout.`, `Required course files present with LF line endings`, then the absolute course path and the Module 0 path.

**Stop:** the folder exists but is not the course origin, Git cannot read the origin, the clone fails, or any required course file is missing, redirected, or has CRLF line endings.

**Recovery:** leave the existing folder in place. If it is the wrong project, choose a different computer folder only with the person who supports your machine; do not delete, reset, pull, or clean this one. For a clone failure, resolve the recorded access or network error first. Preserve partial folders; do not retry over them. The command follows GitHub’s instructions for [Cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

`$R` and `$M` belong to this shell. The new window used for the readiness check sets `R`, `M`, and `PY` again. It cannot use a function that existed only here.

## Enter the key without showing it

Enter the key at the hidden prompt. The next command does nothing except wait for the key. Type the key at that hidden prompt and press Enter. Do not paste the key into the command, a file, a profile, or a chat. The rules for where a key must not go are in [Connect the course account without leaking a key](../shared/CREDENTIALS.md).

**Terminal: Ubuntu Bash, ordinary Linux user, same Ubuntu window.**

```bash
IFS= read -r -s OPENROUTER_API_KEY
```

**Expected:** the prompt returns, and the key does not appear as readable text.

**Stop:** the key appears in readable text, or you pasted it into the command line instead of the prompt.

**Recovery:** if the key was displayed or pasted into a command, revoke it with the provider, use the replacement, and run only this command again. Do not continue with a key that has been displayed.

## Load the key into this process only

This second command exports the variable for the current process and prints only `SET` or `MISSING`. The export happens in a separate command from the read. A child shell may inherit an exported variable, but `SET` alone never proves the key was persisted to a profile or leaked. `MISSING` means only that this process has no nonempty key variable; it does not prove that no file elsewhere contains a key.

Export the entered key for this process after the hidden prompt returns.

**Terminal: Ubuntu Bash, ordinary Linux user, same Ubuntu window.**

```bash
export OPENROUTER_API_KEY
if [ -n "${OPENROUTER_API_KEY:-}" ]; then printf 'SET\n'; else printf 'MISSING\n'; fi
```

**Expected:** `SET`.

**Stop:** `MISSING`, or any output that contains the key.

**Recovery:** run the hidden-read command again in this same shell, then run this export again. Do not check the key by printing the variable. Do not save it to `.profile` or any other file.

## Open an independent terminal and read the difference

Open a new Windows PowerShell window from Start, independently of the Ubuntu window that held the key. Do not type `bash` or launch PowerShell inside that Ubuntu process. A child may inherit its key; an independent window ordinarily prints `MISSING`, but an approved parent environment or a startup profile can still supply a value.

Launch the same selected distribution explicitly. Enter its recorded exact name again; this window has no variables from the previous PowerShell session.

**Terminal: Windows PowerShell, ordinary user, newly opened independently from Start.**

```powershell
wsl --list --verbose
if ($LASTEXITCODE -ne 0) { throw 'STOP: cannot inspect distributions.' }
$CourseDistroNames = @(wsl --list --quiet)
if ($LASTEXITCODE -ne 0) { throw 'STOP: cannot read names.' }
$CourseDistroNames = @($CourseDistroNames | ForEach-Object { ($_ -replace "`0", '').Trim() } | Where-Object { $_ })
$CourseDistro = Read-Host 'Enter the exact Ubuntu NAME you verified earlier; confirm its VERSION is 2'
if ($CourseDistroNames -cnotcontains $CourseDistro) { throw 'STOP: exact name not installed.' }
wsl --distribution $CourseDistro --cd ~
if ($LASTEXITCODE -ne 0) { throw 'STOP: named Ubuntu session returned an error.' }
```

**Expected:** the same verified Ubuntu opens at your Linux home.

**Stop:** the name/version differs or launch fails.

**Recovery:** preserve the error and select the recorded name. Do not use the default distribution as a substitute.

Check the saved OMP path without exporting or repairing PATH in this block.

**Terminal: Ubuntu Bash, ordinary Linux user, newly opened independent window.**

```bash
course_confirm_wsl_terminal() {
  local resolved version course_exit
  resolved="$(command -v omp || true)"
  printf 'OMP_PATH %s\n' "${resolved:-missing}"
  if [ "$resolved" != "$HOME/.local/bin/omp" ]; then
    printf 'STOP: this window did not find the user binary on its own PATH\n' >&2
    return 1
  fi
  version="$("$resolved" --version)"
  course_exit=$?
  printf '%s\n' "${version:-missing}"
  printf 'omp exit %s\n' "$course_exit"
  if [ "$course_exit" -ne 0 ]; then
    return "$course_exit"
  fi
  if [ "$version" != "omp/18.3.5" ]; then
    printf 'STOP: version is not omp/18.3.5\n' >&2
    return 1
  fi
  if [ -n "${OPENROUTER_API_KEY:-}" ]; then
    printf 'key in this window: SET — investigate\n'
    return 1
  fi
  printf 'key in this window: MISSING — expected\n'
}
course_confirm_wsl_terminal
```

**Expected:** `OMP_PATH` is your Linux home plus `/.local/bin/omp`. The next line is `omp/18.3.5`, then `omp exit 0`, then `key in this window: MISSING — expected`. This window did not export PATH before the check.

**Stop:** `OMP_PATH` is `missing` or any other path, the version is not `omp/18.3.5`, `omp exit` is not 0, or the key line is `SET`.

**Recovery:** If the path or version is wrong, do not export PATH in this window. That would hide the miss. Leave every folder under `$HOME/course-evidence` in place, including download logs. Run the path-miss block below, then open another new Ubuntu window and paste this check again. If this independent window prints `SET`, run the profile check before you enter a key. Do not print the variable. Do not upgrade packages.

Repair only the startup file that this Bash window reads, then reopen the named distribution independently.

**Terminal: Ubuntu Bash, ordinary Linux user, same independent window, recovery only after the path check stopped.**

```bash
course_note_wsl_path_miss() {
  local line file
  line='export PATH="$HOME/.local/bin:$PATH"'
  if [ -z "${BASH_VERSION:-}" ]; then
    printf 'STOP: this window is not Bash; no startup file was changed and no log was removed\n' >&2
    return 1
  fi
  if [ -x "$HOME/.local/bin/omp" ]; then
    printf 'selected '
    "$HOME/.local/bin/omp" --version || return 1
  else
    printf 'STOP: %s is missing or not executable; logs under %s were not removed\n' "$HOME/.local/bin/omp" "$HOME/course-evidence" >&2
    return 1
  fi
  if shopt -q login_shell; then
    file="$HOME/.profile"
    if [ -e "$HOME/.bash_profile" ] || [ -L "$HOME/.bash_profile" ]; then
      file="$HOME/.bash_profile"
    elif [ -e "$HOME/.bash_login" ] || [ -L "$HOME/.bash_login" ]; then
      file="$HOME/.bash_login"
    fi
    printf 'this window is a login shell\n'
  else
    file="$HOME/.bashrc"
    printf 'this window is not a login shell\n'
  fi
  if [ -L "$file" ] || { [ -e "$file" ] && [ ! -f "$file" ]; }; then
    printf 'STOP: %s is not a regular file; it was not changed and no log was removed\n' "$file" >&2
    return 1
  fi
  if [ -f "$file" ] && grep -F -x -q -- "$line" "$file"; then
    printf 'PATH_LINE already present in %s\n' "$file"
    printf 'STOP: the line is present, but this window still did not resolve omp from its own PATH. Do not export PATH here. No log was removed.\n' >&2
    return 1
  fi
  if [ -s "$file" ] && [ "$(tail -c 1 -- "$file" | wc -l)" -eq 0 ]; then
    printf '\n' >> "$file" || return 1
  fi
  printf '%s\n' "$line" >> "$file" || return 1
  printf 'PATH_LINE added to %s\n' "$file"
  printf 'logs kept under %s\n' "$HOME/course-evidence"
}
course_note_wsl_path_miss
```

**Expected:** You see `selected omp/18.3.5`, whether this window is a login shell, and either `PATH_LINE added` or a STOP line that says the line is already present. Nothing under `$HOME/course-evidence` is deleted.

**Stop:** The selected binary is missing, the startup file is not a regular file, this window is not Bash, or the line is already present and `omp` is still not on this window's own PATH.

**Recovery:** Do not export PATH in this window, and do not delete download folders. If the line was just added, close this window, use the independent named-distribution launch block again, and run the path check again with no PATH export. If the line was already present, save the printed lines and stop. Do not upgrade Ubuntu and do not change security settings.

## Set the course paths in this window

The earlier Ubuntu window kept `R`, `M`, and `PY`. This window does not have those variables, and it does not have the functions from the earlier window. Set them here before any readiness-check command. This block does not clone, reset, pull, or clean.

**Terminal: Ubuntu Bash, ordinary Linux user, newly opened independent window.**

```bash
course_assign_wsl_paths() {
  R="$HOME/Documents/AIHB_OCT_2026"
  M="$R/AI_Harness_Bootcamp_2/module-00-setup"
  if [ ! -f "$M/shared/MODULE_00_LAB.md" ]; then
    printf 'STOP: this window cannot see the Module 0 lab at %s. The checkout was not reset, pulled, or cleaned.\n' "$M" >&2
    return 1
  fi
  PY="$(for candidate in python3.12 python3 python; do
    candidate_path="$(type -P "$candidate")" || continue
    candidate_path="$(readlink -f -- "$candidate_path")" || continue
    case "$candidate_path" in /mnt/*|*.exe) continue ;; /*) ;; *) continue ;; esac
    "$candidate_path" -c 'import os, pathlib, sys; p=pathlib.Path(sys.executable).resolve(); sys.exit(1) if sys.platform != "linux" or sys.version_info < (3,12) or str(p).startswith("/mnt/") or str(p).lower().endswith(".exe") or not os.access(p,os.X_OK) else print(p)' 2>/dev/null && break
  done)"
  if [ -z "$PY" ] || [ ! -x "$PY" ]; then
    printf 'STOP: no real Python executable is version 3.12 or newer\n' >&2
    return 1
  fi
  "$PY" - "$R" "$M" "$HOME/course-evidence" "$HOME/.local/bin/omp" <<'PY'
from pathlib import Path
import sys
home = Path.home()
if not str(home).startswith('/home/') or home.resolve() != home:
    raise SystemExit('STOP: invalid Linux home')
for value in sys.argv[1:]:
    path = Path(value)
    if path.resolve() != path or not path.is_relative_to(home):
        raise SystemExit('STOP: redirected path or path outside Linux home')
PY
  [ $? -eq 0 ] || return 1
  git_path="$(type -P git)" && git_path="$(readlink -f -- "$git_path")" || return 1
  case "$git_path" in /mnt/*|*.exe) printf 'STOP: Windows Git rejected\n'; return 1 ;; /*) ;; *) return 1 ;; esac
  "$git_path" --version || return 1
  printf 'R %s\n' "$R"
  printf 'M %s\n' "$M"
  printf 'PY %s\n' "$PY"
  "$PY" --version
}
course_assign_wsl_paths
```

**Expected:** An `R` line, an `M` line, and a `PY` line with absolute paths, then a Python version of 3.12 or newer. `R` is under your Linux home, not under `/mnt/c`.

**Stop:** A STOP line appears, a path starts with `/mnt/` or ends in `.exe`, or the Python version is below 3.12.

**Recovery:** If the lab file is missing, preserve the checkout and ask the owner to supply a complete course checkout. Do not delete or replace the home folder. If Python is missing, return to the package step. Do not call a function that existed only in the closed window.

## Investigate unexpected key presence without displaying it

Run this only when the independent terminal printed `SET` before you typed a key. It looks for the variable name in shell profiles and does not print a value.

**Terminal: Ubuntu Bash, ordinary Linux user, same Ubuntu window.**

```bash
found=0
for f in "$HOME/.profile" "$HOME/.bashrc" "$HOME/.bash_profile" "$HOME/.bash_login" "$HOME/.zshrc"; do
  if [ -f "$f" ] && grep -q 'OPENROUTER_API_KEY' "$f"; then
    printf 'REFERENCE in %s; contents not printed\n' "$f"
    found=1
  fi
done
if [ "$found" -eq 0 ]; then
  echo "No profile reference was found."
fi
```

**Expected:** only profile names containing a reference, or `No profile reference was found.` A reference can be a check, comment, or approved parent-variable use; it does not establish a saved secret or exposure.

**Stop:** the independent window's unexpected `SET` remains unexplained.

**Recovery:** review the named file privately with the device owner and check how the parent application supplies variables. Do not print profile lines, dump the environment, or share values. If an actual secret assignment was saved unintentionally, remove it with owner guidance and assess exposure; revoke only when exposed or required by policy. If inheritance is approved and understood, proceed to the hidden-input step. Presence alone proves neither persistence nor successful authentication.

## Enter the key again in the new window

The readiness check runs in this independent window, after that window has printed the persisted `omp` path without an extra PATH export. The key is ordinarily missing unless a reviewed parent environment supplies it. Repeat the hidden read, then the separate export. Do not skip the read and paste the key into the export command.

**Terminal: Ubuntu Bash, ordinary Linux user, same Ubuntu window.**

```bash
IFS= read -r -s OPENROUTER_API_KEY
```

**Expected:** the prompt returns, and the key is not readable on screen.

**Stop:** the key is visible as readable text.

**Recovery:** revoke a displayed key, then run this read again.

Export the entered key for this process after the hidden prompt returns.

**Terminal: Ubuntu Bash, ordinary Linux user, same Ubuntu window.**

```bash
export OPENROUTER_API_KEY
if [ -n "${OPENROUTER_API_KEY:-}" ]; then printf 'SET\n'; else printf 'MISSING\n'; fi
```

**Expected:** `SET`.

**Stop:** `MISSING`, or any output that contains the key.

**Recovery:** run the hidden read and this export again in this shell. Do not continue to the readiness check on `MISSING`.

## Prepare a fresh readiness check

The work folder is outside the course checkout. This window must already have printed `R`, `M`, and `PY`. The token is created by Python's secrets module and stored outside the work folder, then copied in so the model has to read it. The evidence folder is only a path at this point. You do not create it. You also do not create `from-omp.txt`. Create the new attempt and its input token now.

**Terminal: Ubuntu Bash, ordinary Linux user, same Ubuntu window.**

```bash
course_prepare_wsl_proof() {
  local course_exit
  if [ -z "${PY:-}" ] || [ ! -x "$PY" ]; then
    printf 'STOP: PY is not an executable path in this window\n' >&2
    return 1
  fi
  run="$HOME/course-evidence/setup-wsl-proof-$(date -u +%Y%m%dT%H%M%SZ)-$$"
  attempt="$run/module-00"
  proof="$attempt/proof"
  token_file="$attempt/run-token.txt"
  evidence="$attempt/receipts"
  prompt_file="$attempt/prompt.txt"
  "$PY" - "$attempt" <<'PY'
from pathlib import Path
import secrets, sys
attempt = Path(sys.argv[1])
home = Path.home()
checkout = home/'Documents/AIHB_OCT_2026'
if not str(home).startswith('/home/') or home.resolve() != home or attempt.resolve() != attempt or not attempt.is_relative_to(home) or attempt.is_relative_to(checkout):
    raise SystemExit('STOP: attempt must be unredirected, under Linux home, outside checkout')
attempt.mkdir(parents=True,exist_ok=False)
proof = attempt/'proof'
proof.mkdir()
token = secrets.token_hex(16) + '\n'
(attempt/'run-token.txt').write_text(token,encoding='utf-8')
(proof/'run-token.txt').write_text(token,encoding='utf-8')
(attempt/'prompt.txt').write_text('Read run-token.txt with course_read. Use course_write to create only from-omp.txt containing omp works, one space, and the exact token. Do not write another file.\n',encoding='utf-8')
print('FRESH READINESS WORK',proof)
print('EVIDENCE NOT PRECREATED',attempt/'receipts')
PY
  course_exit=$?
  printf 'prepare exit %s\n' "$course_exit"
  return "$course_exit"
}
course_prepare_wsl_proof
```

**Expected:** `FRESH READINESS WORK` names the new work folder, `EVIDENCE NOT PRECREATED` names its absent receipt path, and the last line is `prepare exit 0`. The token value is not printed.

**Stop:** `PY` is unset, Python is missing, a path already exists, a file cannot be written, or `prepare exit` is not 0.

**Recovery:** Leave any partial attempt in place. Correct the reported path or permission failure, then run the block again with new paths. Do not delete the course checkout or the download logs, and do not create the evidence folder or `from-omp.txt` by hand. If the STOP line says `PY` is unset, paste the path-assignment block in this window first.

## Ask for the one permitted write

The launcher runs the pinned Oh My Pi binary with permission to write only `from-omp.txt`. It reads the key from this process. Exit 2 means a prerequisite failed before the evidence folder was created. The `HOLD:` line names which prerequisite. A missing key is only one of those holds. Exit 1 means the live attempt failed after work began. Keep every failed live attempt as HOLD. Do not retry the launcher in that attempt, switch providers, or use a fallback model. After a targeted correction, create a new attempt. Run the supplied launcher once against the fresh paths.

**Terminal: Ubuntu Bash, ordinary Linux user, same Ubuntu window.**

```bash
course_run_wsl_proof() {
  local course_exit
  if [ -z "${PY:-}" ] || [ ! -x "$PY" ] || [ -z "${R:-}" ] || [ -z "${proof:-}" ] || [ -z "${prompt_file:-}" ] || [ -z "${evidence:-}" ]; then
    printf 'STOP: this window is missing PY, R, or the readiness-check paths\n' >&2
    return 1
  fi
  "$PY" "$R/shared/run_omp.py" --workdir "$proof" --prompt "$prompt_file" --evidence "$evidence" --allow-write from-omp.txt
  course_exit=$?
  printf 'launcher exit %s\n' "$course_exit"
  return "$course_exit"
}
course_run_wsl_proof
```

**Expected:** The launcher's own output appears, and the last line is `launcher exit 0`. The evidence folder now exists because the launcher created it. That status does not yet complete the readiness check.

**Stop:** `launcher exit 2` with a `HOLD:` line means a prerequisite failed. The evidence folder should still be absent, and you must not invent the result file. `launcher exit 1` means the live attempt failed. Exit 0 with no evidence folder is also a stop.

**Recovery:** Read the `HOLD:` line. Do not treat every exit 2 as a missing key. If that line says `OPENROUTER_API_KEY unavailable`, repeat the hidden read and the separate export in this window, then return to “Prepare a fresh readiness check” so the paths are new. If it says `omp is not on PATH`, or that the pinned version did not match, return to the independent-terminal check. Do not export PATH here, and do not enter the key as that fix. If it says a directory is missing, already exists, or overlaps, keep the attempt, correct the named path problem, and prepare a fresh readiness check. If it says `course_guard.mjs` is missing, the checkout is incomplete; do not reset, pull, or clean it. Exit 1 is a failed live attempt, not an authentication prompt. Do not delete `$HOME/course-evidence`, and do not write `from-omp.txt` yourself.

## Check the write against the token and the receipt

The checker takes the work folder, the token file outside that folder, and the evidence folder. It passes only when `from-omp.txt` contains the words `omp works`, one space, and this run's token, and a `course_write` receipt matches the file on disk. Run the checker to verify the token, receipts, and pinned identities.

**Terminal: Ubuntu Bash, ordinary Linux user, same Ubuntu window.**

```bash
course_check_wsl_proof() {
  local course_exit
  if [ -z "${PY:-}" ] || [ ! -x "$PY" ] || [ -z "${M:-}" ] || [ -z "${proof:-}" ] || [ -z "${token_file:-}" ] || [ -z "${evidence:-}" ]; then
    printf 'STOP: this window is missing PY, M, or the readiness-check paths\n' >&2
    return 1
  fi
  checker="$M/shared/case/verify_tool_proof.py"
  "$PY" "$checker" "$proof" "$token_file" "$evidence"
  course_exit=$?
  printf 'checker exit %s\n' "$course_exit"
  return "$course_exit"
}
course_check_wsl_proof
```

**Expected:** the checker's last result line is `READINESS CHECK PASS`, and the last line is `checker exit 0`.

**Stop:** the last result line is `READINESS CHECK HOLD`, `checker exit` is not 0, or the result file is missing. A file you create by hand is not a pass.

**Recovery:** keep this failed attempt as HOLD. Correct the specific checker failure before returning to “Prepare a fresh readiness check” with new folders. Do not edit `from-omp.txt` to make the words match. If the STOP line says `PY` or `M` is missing, paste the path-assignment block in this window first.

## Read the actual result file

Read the file on disk separately after `READINESS CHECK PASS`; this command does not construct the expected answer.

**Terminal: Ubuntu Bash, ordinary Linux user, same independent window.**

```bash
cat -- "$proof/from-omp.txt"
```

**Expected:** `omp works`, one space, and this attempt's token, matching the successful checker.

**Stop:** missing/unreadable file or contents differ from the checked result.

**Recovery:** keep the attempt as HOLD and investigate the changed or missing file. Do not write a replacement by hand or retry the live turn in this folder.

## Record prerequisites, not the live turn

This report checks that Git, Python, Oh My Pi, the checkout, and the key are present in this process. A passing report does not prove the live write. A dirty checkout is not a reason to reset, pull, or clean. The readiness check you already ran checks the live write. Save the separate prerequisite report now.

**Terminal: Ubuntu Bash, ordinary Linux user, same Ubuntu window.**

```bash
course_report_wsl_setup() {
  local course_exit
  if [ -z "${R:-}" ] || [ -z "${M:-}" ] || [ -z "${attempt:-}" ]; then
    printf 'STOP: this window is missing R, M, or the attempt path\n' >&2
    return 1
  fi
  report="$attempt/setup-report-$(date -u +%Y%m%dT%H%M%SZ)-$$.txt"
  bash "$M/scripts/verify-setup.sh" "$R" "$report"
  course_exit=$?
  printf 'report exit %s\n' "$course_exit"
  return "$course_exit"
}
course_report_wsl_setup
```

**Expected:** a report file path, a last report line beginning `SETUP CHECK PASS`, and `report exit 0`. The report does not contain the key. The shell stays open.

**Stop:** `SETUP CHECK HOLD`, any nonzero report exit, the report path already exists, the report contains the key, or the command says `R` or `M` is missing. A hold in this report is a prerequisite hold. It is not repaired by editing the result file, and a pass in this report does not replace `READINESS CHECK PASS`.

**Recovery:** fix the first failed prerequisite named in the report, then run this report command again after the timestamp changes so the report path is new. Keep the failed report. Do not reset, pull, or clean the checkout because the report mentions local changes. Proceed only when both the prerequisite report and the live readiness check pass.


## Prepare local n8n for Module 6

This check opens the local visual workflow editor and proves that a saved workflow survives a stop and start. Keep its result separate from `SETUP CHECK PASS` and the live OMP `READINESS CHECK PASS`. An n8n HOLD does not erase an OMP pass, but Module 6 needs n8n ready. Installation and image-download time depends on the device and network.

### Check the Windows host and approvals

[Microsoft’s simplified WSL installation](https://learn.microsoft.com/en-us/windows/wsl/install) requires Windows 10 build 19041+ or Windows 11. Docker’s current WSL backend requirements are stricter: WSL package 2.1.5+, Windows 10 22H2 build 19045 or Windows 11 23H2 build 22631+, a supported edition and servicing status, 8 GB RAM, SLAT, hardware virtualization enabled, and the Windows Server service (`LanmanServer`) enabled with Automatic startup. Docker lists Enterprise, Pro, and Education in its requirements and separately discusses Home for Linux containers; have the owner confirm eligibility for the exact host. Windows Server is unsupported. See [Docker’s current Windows requirements](https://docs.docker.com/desktop/setup/install/windows-install/) before downloading. Passing the earlier native-tool or Microsoft WSL floor alone is insufficient.

On Windows Arm, select the **Arm (Early Access)** download only with owner approval for that status; Windows containers are unsupported. Published arm64 images do not prove this course stack works on a Windows Arm laptop. Keep n8n on HOLD until this device completes the checks below. An x64 host also needs those checks.

Have the device owner confirm [Docker Desktop licensing](https://docs.docker.com/subscription-billing/desktop-license/). Personal use, education, non-commercial open source, and qualifying small businesses (fewer than 250 employees AND under $10 million revenue) are free; professional use outside those limits and government entities require a paid subscription. Do not assume a work laptop qualifies because this is a class.

The [official stack](https://raw.githubusercontent.com/n8n-io/n8n/master/docker/get-n8n-compose.yml) includes `n8n`, `runners`, `sandbox-certs`, `sandbox-api`, `sandbox-runner-1`, and `searxng`. The sandbox runner uses privileged Docker-in-Docker. Obtain owner approval for that privilege and ordinary-user Docker access before starting it. Keep Assistant off; do not enter a provider key into n8n.

Inspect existing Docker work and the Windows port before changing settings. Check **Settings → Apps → Installed apps** for Docker Desktop and **Task Manager** for running Docker Desktop processes without launching it. If Desktop and its engine are already running, inspect **Containers** in the existing window. If Desktop is installed but stopped, or its engine state is unclear, keep it stopped until the owner reviews and approves startup effects on existing work. Starting the daemon can restart containers with an `always` restart policy, including manually stopped containers; see [Docker restart policies](https://docs.docker.com/engine/containers/start-containers-automatically/). Do not stop existing applications to make room. The CLI probes below do not start Desktop; a failed connection is HOLD, not an instruction to launch it.

**Terminal: Windows PowerShell, ordinary user, new inspection window.**

```powershell
Get-ComputerInfo -ErrorAction Stop | Select-Object WindowsProductName, WindowsVersion, OsBuildNumber, CsTotalPhysicalMemory
Get-Service -Name LanmanServer -ErrorAction Stop | Select-Object Name, Status, StartType
wsl --version
Write-Output ('WSL version exit: ' + $LASTEXITCODE)
wsl --list --verbose
Write-Output ('Distribution list exit: ' + $LASTEXITCODE)
if (Get-Command docker -CommandType Application -ErrorAction SilentlyContinue) {
  docker context ls
  docker info
  docker compose version
  docker ps --all
  docker volume ls
} else { Write-Output 'Docker CLI absent; inspect installed apps before installing.' }
Get-NetTCPConnection -State Listen -ErrorAction Stop | Where-Object LocalPort -eq 5678 | Select-Object LocalAddress, LocalPort, OwningProcess
```

**Expected:** recorded host and WSL versions, distributions preserved, Desktop recorded as absent, already running, or installed but stopped, Docker inventory from the approved running engine, and no listener on 5678 for a fresh installation. An existing course instance may already own that port.

**Stop:** licensing, privileges, host support, virtualization, or WSL approval is unresolved; Docker points to an unexpected/remote engine; existing applications or port ownership are unclear; any inspection fails.

**Recovery:** resolve the specific finding with the owner. Keep all applications, containers, volumes, checkouts, and earlier attempts. Do not kill a process, prune Docker, reset Desktop, or change contexts blindly. A denied WSL/Docker prerequisite is **n8n HOLD**, separate from OMP readiness.

Reuse the exact Ubuntu distribution and ordinary user selected earlier. Keep the existing course checkout at `$HOME/Documents/AIHB_OCT_2026` and its work/evidence paths intact. n8n belongs separately at `$HOME/n8n-course`; do not clone or relocate the course. If conversion or installation is needed, use the owner-approved sections above with their backup and restart boundaries.

### Update WSL only if Docker requires it

Skip this step when the recorded WSL package version meets the Docker requirement. A distribution’s VERSION `2` is not the WSL package version. For an old inbox WSL with no version output, or a package below 2.1.5, obtain owner approval for the update. Save work in every WSL distribution and Docker application; updates or restarts can interrupt them. Do not use a blanket WSL shutdown while other work is running.

**Terminal: Windows PowerShell, elevated only for the owner-approved WSL update.**

```powershell
wsl --update
if ($LASTEXITCODE -ne 0) { throw 'STOP: preserve the WSL update message.' }
wsl --version
if ($LASTEXITCODE -ne 0) { throw 'STOP: WSL package version is still unavailable.' }
wsl --list --verbose
if ($LASTEXITCODE -ne 0) { throw 'STOP: could not recheck distributions.' }
```

**Expected:** WSL package 2.1.5 or newer and the selected Ubuntu still present as VERSION `2`.

**Stop:** update denied, failed, or requests a restart; the selected distribution changed or the version is still too old.

**Recovery:** save the output and complete any owner-approved restart before rechecking in a fresh ordinary PowerShell window. Re-select the exact distribution name afterward. Never unregister, reset, or reinstall an existing distribution to repair a version check. See [Microsoft’s WSL commands](https://learn.microsoft.com/en-us/windows/wsl/basic-commands).

### Connect Docker Desktop to the selected Ubuntu

First run the Ubuntu package/process inspection below and resolve any independent Docker installation with its owner. Then install only a missing, approved **Docker Desktop for Windows**, from the official Windows download page above, matching the host processor. In the installer select **Use WSL 2 instead of Hyper-V** when offered. Follow the owner’s installation mode and elevation policy, select **Close** when complete, and save work before any required Windows restart. Existing Desktop installations stay in place.

Before enabling integration, run the Ubuntu package/process inspection below and resolve any existing independent daemon. If Desktop is stopped, obtain owner approval for the effects of daemon startup on existing work before opening **Start → Docker Desktop**. If it is already running, use its existing window. Review the agreement and select **Accept** only after licensing approval. Under **Settings → General**, select **Use WSL 2 based engine** if shown (it can be enabled automatically). Under **Settings → Resources → WSL Integration**, enable the exact Ubuntu NAME you recorded; do not rely on the default-distribution checkbox. Select **Apply** (or **Apply & restart**, if that is the displayed button) after saving affected work. If WSL Integration is missing, use the Docker taskbar menu’s **Switch to Linux containers** with owner approval; switching can interrupt existing work. Expected state: Desktop’s engine is running, using Linux containers, with integration enabled for that exact distro. See [Docker WSL integration](https://docs.docker.com/desktop/features/wsl/).

Do not install Docker Engine inside Ubuntu. If Ubuntu already has its own Docker Engine/CLI, stop and have its owner inventory and back up that work and resolve the conflict before enabling Desktop integration. Docker warns against running both installations. Do not uninstall or migrate the existing daemon as an automatic repair. If the installer later suggests `get.docker.com`, do not follow that suggestion on this route.

Open the selected Ubuntu by its exact NAME using the named launch procedure above. Use the same ordinary Linux user and Linux `$HOME` each time. Before enabling integration, inspect that Ubuntu’s installed packages and processes with the owner to identify any existing independent Docker daemon. Do not start or remove one.

**Terminal: Ubuntu Bash, ordinary Linux user, selected distribution; before installing Desktop or enabling integration.**

```bash
dpkg-query -W -f='${binary:Package} ${Status}\n' docker-ce docker-ce-cli docker.io containerd.io 2>/dev/null
pgrep -a dockerd
```

**Expected:** no independently installed Docker Engine/CLI packages and no Ubuntu `dockerd`; absent packages/processes can return nonzero here. **Stop:** any installed package, daemon, or unclear result suggests an existing installation. **Recovery:** have the owner inspect custom installations too and preserve their containers/volumes before resolving the conflict. These probes alone do not prove absence of a manually installed daemon.

Check `curl --version` and the certificate bundle in the inspection block below. If either is missing, use this package step only after owner approval; skip it when both are present.

**Terminal: Ubuntu Bash, ordinary Linux user, selected distribution; approved missing packages only.**

```bash
sudo apt-get update && sudo apt-get install --no-upgrade curl ca-certificates
```

**Expected:** the missing download prerequisites are installed; existing packages are not upgraded by the install command. **Stop:** policy denial, package failure, or a proposal to remove existing software. **Recovery:** preserve the message and resolve it with the owner; do not weaken certificate verification or install a Docker daemon. Then repeat the following inspection.

**Terminal: Ubuntu Bash, ordinary Linux user, selected WSL 2 distribution.**

```bash
course_n8n_inspect() {
  [ -n "${BASH_VERSION:-}" ] && [ "$(id -u)" -ne 0 ] || return 1
  cd "$HOME" || return 1
  case "$HOME" in /home/*) ;; *) printf 'HOLD: use your Linux home\n'; return 1 ;; esac
  [ "$(pwd -P)" = "$HOME" ] || return 1
  curl --version || return 1
  [ -s /etc/ssl/certs/ca-certificates.crt ] || return 1
  if [ -n "${DOCKER_HOST:-}" ] || [ -n "${DOCKER_CONTEXT:-}" ]; then
    printf 'HOLD: Docker override is set; review privately with owner\n'; return 1
  fi
  docker context ls || return 1
  docker info || return 1
  docker compose version || return 1
  docker ps --all || return 1
  docker volume ls || return 1
  ss -ltn 'sport = :5678' || return 1
  df -h "$HOME" || return 1
  printf 'Intended destination: %s/n8n-course\n' "$HOME"
  if [ -e "$HOME/n8n-course" ] || [ -L "$HOME/n8n-course" ]; then
    printf 'EXISTING destination: preserve it; do not run installer\n'
  else
    printf 'FRESH destination: absent\n'
  fi
}
course_n8n_inspect
```

**Expected:** `docker info` succeeds for the approved Docker Desktop Linux engine as this ordinary user, and `docker compose version` succeeds. The modern plugin may report version 5; it need not start with `2.`. Inventory matches the owner’s known work, the destination is outside the checkout, and port 5678 is free for a fresh instance in both Windows and Ubuntu.

**Stop:** any command fails, Linux-home identity differs, an engine/context is unexpected, a Docker override is set, an unknown port listener exists, or storage is insufficient for the full stack.

**Recovery:** review integration and context with the owner, then repeat in the intended Ubuntu shell. Never use `sudo` for the n8n installer, make the Docker socket world-writable, or start a second Ubuntu daemon. A CLI version alone does not prove daemon access. Preserve an existing destination even if incomplete. Have its owner identify its actual Compose project, data, version, and port. An existing installation must retain that identity and its owner-managed lifecycle; do not run fresh identity creation or rename it. For an installation already created with the recorded identity below, confirm that identity with the owner before reusing the helper. A different version is HOLD pending owner resolution, not permission to repin or upgrade.

### Create the fresh n8n configuration

Choose one installation method below, only after the preceding checks pass and `$HOME/n8n-course` is absent. The [official one-line setup](https://docs.n8n.io/deploy/host-n8n/install-options/one-line-setup) accepts the course’s explicit `2.41.5` version and `--no-start`. Its [reviewed installer source](https://raw.githubusercontent.com/n8n-io/n8n/master/docker/get-n8n.sh) is version `1.4.0`; the live URL can change. Prefer download-and-review to check that version before execution. The installer’s “existing install” message proves neither version nor readiness.

**Terminal: Ubuntu Bash, ordinary Linux user, same selected distribution; one-line option.**

```bash
(
  set -o pipefail
  if [ -e "$HOME/n8n-course" ] || [ -L "$HOME/n8n-course" ]; then
    printf 'HOLD: destination exists; preserved\n' >&2; exit 1
  fi
  curl -fsSL https://get.n8n.io | N8N_DIR="$HOME/n8n-course" sh -s -- --version 2.41.5 --no-start
)
```

**Expected:** successful completion creates configuration under Linux `$HOME/n8n-course` without starting containers. Bash `pipefail` reports a failed download even if the shell side exits successfully.

**Stop:** any download/installer failure, changed installer version, missing configuration, or existing-install notice. A streamed script can partially execute before a download failure.

**Recovery:** preserve partial files and messages for owner review. Do not rerun over them, delete them, or use upgrade/uninstall flags. The following alternative downloads completely before execution; use it instead of the one-line option, not afterward.

**Terminal: Ubuntu Bash, ordinary Linux user, same selected distribution; download-and-review alternative.**

```bash
course_n8n_review_install() {
  local review_dir approved
  if [ -e "$HOME/n8n-course" ] || [ -L "$HOME/n8n-course" ]; then
    printf 'HOLD: destination exists; preserved\n'; return 1
  fi
  review_dir="$(mktemp -d "$HOME/n8n-installer-review.XXXXXX")" || return 1
  curl -fsSL https://get.n8n.io -o "$review_dir/get-n8n.sh" || {
    printf 'HOLD: incomplete download kept at %s; do not execute it\n' "$review_dir"; return 1;
  }
  [ -s "$review_dir/get-n8n.sh" ] || return 1
  grep -qx 'SCRIPT_VERSION="1.4.0"' "$review_dir/get-n8n.sh" || {
    printf 'HOLD: installer version changed; owner review needed\n'; return 1;
  }
  less "$review_dir/get-n8n.sh" || return 1
  read -r -p 'After reviewing, type INSTALL to create the fresh configuration: ' approved
  [ "$approved" = INSTALL ] || return 1
  N8N_DIR="$HOME/n8n-course" sh "$review_dir/get-n8n.sh" --version 2.41.5 --no-start
}
course_n8n_review_install
```

**Expected:** a completed download, installer version `1.4.0`, review in `less` (press **q** to leave), then fresh configuration after confirmation; no containers start.

**Stop:** failed or empty download, changed script version, denied review, installer failure, or an existing destination.

**Recovery:** keep the review folder and partial setup. Resolve the specific failure with the owner. Do not execute a partial download or overwrite an existing installation.

### Bind the editor to this laptop before starting

In your normal text editor, use **File → Open** to open the selected distro’s Linux `$HOME/n8n-course/compose.yml` (Windows editors can reach it through `\\wsl.localhost\<exact-distro-name>\home\<linux-user>\n8n-course\compose.yml`). Under the `n8n` service’s `ports`, change only `'5678:5678'` to `'127.0.0.1:5678:5678'`, then **File → Save**. Keep all six services. Do not open/share `.env`, paste it into chat, or run a resolved `docker compose config` dump; it contains secrets. No course checkout file or provider key belongs in this n8n configuration.

**Expected:** the saved n8n port is exactly `127.0.0.1:5678:5678`; no other service publishes a port. **Stop:** the file differs from the expected stack, already belongs to another installation, or cannot be saved. **Recovery:** preserve it and review with the owner before starting; do not replace a preexisting Compose file.

### Record the fresh project name

A Compose project name identifies this stack’s containers, volumes, and networks. The Compose file path alone does not fix that identity; see [Docker project names](https://docs.docker.com/compose/how-tos/project-name/). For the genuinely fresh configuration you just generated and bound to localhost, agree on an unused name with the owner before the first start. Use only lowercase ASCII letters, digits, underscores, and hyphens, beginning with a letter or digit. Do not use this step for an existing installation.

**Terminal: Ubuntu Bash, ordinary Linux user, same selected distribution; fresh configuration only.**

```bash
course_n8n_identify() {
  local project containers volumes networks
  local LC_ALL=C
  if [ -e "$HOME/n8n-course/.course-project" ] || [ -L "$HOME/n8n-course/.course-project" ]; then
    printf 'HOLD: project record exists; preserve it\n'; return 1
  fi
  printf 'Enter the owner-approved unused project name: '
  IFS= read -r project || return 1
  case "$project" in
    ''|[!a-z0-9]*|*[!a-z0-9_-]*) printf 'HOLD: invalid project name\n'; return 1 ;;
  esac
  containers="$(docker ps -aq --filter "label=com.docker.compose.project=$project")" || {
    printf 'HOLD: container inspection failed\n'; return 1;
  }
  volumes="$(docker volume ls -q --filter "label=com.docker.compose.project=$project")" || {
    printf 'HOLD: volume inspection failed\n'; return 1;
  }
  networks="$(docker network ls -q --filter "label=com.docker.compose.project=$project")" || {
    printf 'HOLD: network inspection failed\n'; return 1;
  }
  if [ -n "$containers" ] || [ -n "$volumes" ] || [ -n "$networks" ]; then
    printf 'HOLD: project name already has Docker resources\n'; return 1
  fi
  (umask 077; set -o noclobber; printf '%s\n' "$project" > "$HOME/n8n-course/.course-project") || {
    printf 'HOLD: could not create project record; preserve existing files\n'; return 1;
  }
  printf 'Project name recorded\n'
}
course_n8n_identify
```

**Expected:** all three Docker inspections succeed without finding resources for the approved name, then `.course-project` is created privately without overwriting a file or symlink. **Stop:** an invalid name, existing resource or record, failed inspection, or failed write. **Recovery:** preserve all resources and files. Review the finding with the owner; do not remove resources or rename an existing installation to make the check pass.

### Use the recorded project and configuration

Define this helper in the same Ubuntu shell. It uses the recorded name, `.env`, and `compose.yml` for every stack command. Exported variables can override `.env` even with an explicit file path; see [Docker interpolation precedence](https://docs.docker.com/compose/how-tos/environment-variables/variable-interpolation/). The helper stops if any listed override is exported, including an empty value. It prints only the variable name and HOLD, never its value.

**Terminal: Ubuntu Bash, ordinary Linux user, same selected distribution.**

```bash
course_n8n() {
  local variable project
  local LC_ALL=C
  for variable in N8N_VERSION N8N_SANDBOX_VERSION N8N_RUNNERS_AUTH_TOKEN SEARXNG_SECRET COMPOSE_PROJECT_NAME COMPOSE_FILE COMPOSE_ENV_FILES COMPOSE_DISABLE_ENV_FILE COMPOSE_PROFILES; do
    if printenv "$variable" >/dev/null 2>&1; then
      printf '%s HOLD\n' "$variable"; return 1
    fi
  done
  if [ ! -f "$HOME/n8n-course/.course-project" ] || [ -L "$HOME/n8n-course/.course-project" ]; then
    printf 'HOLD: project record missing or not a regular file\n'; return 1
  fi
  project="$(cat "$HOME/n8n-course/.course-project")" || {
    printf 'HOLD: could not read project record\n'; return 1;
  }
  case "$project" in
    ''|[!a-z0-9]*|*[!a-z0-9_-]*) printf 'HOLD: invalid project record\n'; return 1 ;;
  esac
  docker compose -p "$project" --env-file "$HOME/n8n-course/.env" -f "$HOME/n8n-course/compose.yml" "$@"
}
```

**Expected:** the helper is defined; it starts nothing until called. **Stop:** any later call reports HOLD or fails. **Recovery:** have the owner resolve exported overrides in a clean shell, then inspect the approved Docker engine/context and define the helper there again. Do not automatically unset variables or rewrite configuration. Preserve a missing, damaged, or unexpected project record for owner review; do not recreate it for an existing installation.

Start the confirmed project only after identity creation succeeds.

**Terminal: Ubuntu Bash, ordinary Linux user, same selected distribution.**

```bash
course_n8n up -d
```

**Expected:** the full stack starts; initial image pulls can take several minutes. **Stop:** a pull, privilege, port, or startup error. **Recovery:** keep configuration and volumes, resolve the named problem with the owner, and retry only this start after correction. Do not reset or reinstall.

**Terminal: Ubuntu Bash, ordinary Linux user, same selected distribution.**

```bash
course_n8n ps --all
course_n8n port n8n 5678
course_n8n exec n8n n8n --version
```

**Expected:** all six services are present. `sandbox-certs` is a successful one-shot, `Exited (0)`; the other five services are running, with health checks healthy where shown. The port output is exactly `127.0.0.1:5678` and n8n reports `2.41.5`. **Stop:** missing/restarting/unhealthy services, failed certificate exit, a public binding, failed command, or another n8n version. **Recovery:** allow initialization to finish and repeat inspection; persistent failures stay HOLD. Review errors privately without exposing secrets. Do not change the pin, delete volumes, or disable services to force a pass.

### Save a blank workflow and prove it persists

In the Windows browser, open **http://localhost:5678**. For a fresh instance, complete **Set up owner account** with local credentials and select **Next**. This creates the local instance owner, not an n8n Cloud account. If a login page appears for an existing instance, use its existing owner login; do not reset it. Skip optional offers and surveys where offered. No external account, provider key, or paid activation is required. Leave **n8n Assistant** off.

Select **Overview**, then **Build a workflow** on a fresh instance or **Create workflow** when workflows already exist. Click the workflow title, name it **Module 6 Readiness**, and press **Enter**. The editor saves automatically; do not look for a required Save button. Leave the canvas blank and do not select **Publish**. Reload the browser page and confirm the name and blank canvas remain. Preserve an existing workflow with that name; choose a distinct readiness name if it contains work.

**Expected:** local owner access, saved blank workflow, Assistant off, and workflow unpublished/inactive. **Stop:** Cloud signup, provider-key/payment request, wrong instance, missing saved workflow, or unavailable editor. **Recovery:** check the address and the inspected port/project with the owner. Preserve the existing account and workflows; do not create another instance to hide a failure.

Stop only this confirmed course Compose project. This retains its named volumes and workflow data.

**Terminal: Ubuntu Bash, ordinary Linux user, same selected distribution.**

```bash
course_n8n down
```

**Expected:** this project’s containers stop and are removed; volumes remain. **Stop:** command failure or evidence this is another owner’s project. **Recovery:** preserve the output and confirm project ownership. Never add `-v` or run a volume prune.

**Terminal: Ubuntu Bash, ordinary Linux user, same selected distribution.**

```bash
course_n8n up -d
```

**Expected:** the same project starts again using its saved data. **Stop:** startup failure. **Recovery:** preserve files/volumes, resolve the specific error, and repeat the service/version/port inspection above.

Repeat that inspection after restart. Reload **http://localhost:5678**, sign in with the same local owner if needed, and reopen **Module 6 Readiness**. Record **n8n READY** only when the correct version, localhost-only port, six-service state, and saved workflow all survive the restart. Otherwise record **n8n HOLD** with the failed check, separately from both OMP results. For later sessions, inspect Desktop’s running state first. If it is stopped, obtain owner approval for startup effects on existing work before launching it. Open the same Ubuntu distribution as the same ordinary user, inspect the approved Docker engine/context and access, and define `course_n8n` again from the block above. Reuse the recorded `.course-project`; never rerun `course_n8n_identify`. Use `course_n8n up -d`, the same helper inspection commands, and `course_n8n down`. No reset, uninstall, or upgrade is part of this path.
