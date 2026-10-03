# Windows WSL 2 with Ubuntu setup

Windows Subsystem for Linux 2 runs Ubuntu on your Windows computer. Keep all course work in the Linux filesystem under your Linux home directory. Plan for roughly 90 to 180 minutes if you need to enable a Windows feature or restart; that is an estimate, not a measured time. Keep the course clone, work directories, evidence directories, and Oh My Pi binary under the Linux `$HOME`. Never use `/mnt/c` for the course checkout or readiness-check work. Use the Linux `omp` binary and Linux configuration. Enter the provider key at the hidden prompt, and if a key appears unexpectedly in a new window, investigate without showing its value.

You need Git, Python 3.12 or newer inside Ubuntu, a browser, an ordinary text editor, Linux Obsidian through WSLg, and Oh My Pi 18.3.5 for Linux. WSLg displays Linux application windows on your Windows desktop. The only provider key is `OPENROUTER_API_KEY`. The course launcher selects `openrouter/anthropic/claude-sonnet-4.6`. Module 7 also requires local n8n 2.41.5 through Docker Desktop, using this same Ubuntu distribution and Linux home. You do not install Node, npm, or another agent.

Keep an existing Ubuntu 24.04 or 26.04 WSL 2 installation. Do not unregister, reset, or replace it. The course checkout belongs at `$HOME/Documents/AIHB_OCT_2026`; work and evidence stay outside that checkout under the same Linux home.

## Check Windows and inspect distributions

Check that your computer runs Windows 10 build 19041 or newer, or Windows 11, and still gets supported security updates under your device policy. Meeting the build number alone does not mean the host is still supported. Get device-owner approval before enabling features, installing software, or converting a distribution. If policy denies a change, keep the message and stop rather than bypassing it. See [Microsoft's WSL installation requirements](https://learn.microsoft.com/en-us/windows/wsl/install).

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

**Expected:** WSL component versions (record the package version separately from each distribution's VERSION), a supported host that meets Microsoft's installation minimum, either a list of installed distributions or a clear message that none are installed, and a successful online list. Record the exact name and VERSION of any existing Ubuntu you plan to use. The name alone won't tell you its Ubuntu release; check that inside Linux below.

**Stop:** unsupported host, an unavailable WSL command, policy denial, an installed-list error other than the explicit no-distributions state, or an online-list failure.

**Recovery:** If no distributions are installed and nothing else failed, use the approved named installation below. Otherwise, keep the output and ask the device owner to fix the specific problem using [Microsoft's installation troubleshooting](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting#installation-issues). Leave manual Windows-feature repair to the owner; don't paste feature-enabling commands from another route.

Meeting Microsoft's simplified-install minimum above does not mean your computer meets Docker Desktop's requirements. Check the stricter Docker requirements at the n8n host check below. If the package version did not print, ask the owner to review it before Docker setup, and keep the existing distributions.

## Install Ubuntu only when a suitable distribution is absent

If you already have a suitable Ubuntu, skip this section. If you don't know an installed Ubuntu's release, select it by its exact name and launch it using the steps below before you decide to install anything. For a new install, first check that the online list includes the exact NAME `Ubuntu-24.04`; don't use the changing `Ubuntu` alias. After the owner approves the install, open PowerShell with **Run as administrator**.

Install the named release. Microsoft's `--install` command creates new distributions as WSL 2. The command `wsl --set-default-version 2` sets the default for **new** distributions only; it won't convert an existing WSL 1 installation.

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

**Recovery:** Keep the message and work through the linked Microsoft troubleshooting with the owner. If Windows asked you to restart, check the installed list again before doing anything else. Don't reinstall a distribution that's already there.

## Select the exact distribution

After any restart, open a regular Windows PowerShell window. At the prompt, enter the exact installed NAME, even if it isn't `Ubuntu-24.04`. That way you keep an existing Ubuntu 26.04 or another valid Ubuntu installation with a different name.

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

**Recovery:** You can launch the named distribution below to check an unknown release, but don't continue to packages until the Linux release check passes. If its VERSION is `1`, use the separate approved conversion below. Setting a default doesn't convert an existing distribution.

### Convert an existing WSL 1 distribution only with approval

If the selected entry already shows VERSION `2`, skip this step. Conversion can take time or fail, so ask the owner to approve it and make a backup you can restore first, using [Microsoft's export and import commands](https://learn.microsoft.com/en-us/windows/wsl/basic-commands#export-a-distribution). The owner picks a new destination with enough space, exports the exact selected distribution, and checks that the backup can be used before conversion. Keep both the original and the backup.

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

Before launching, check that the exact selected NAME shows VERSION `2` in the Windows list. If Ubuntu asks for a Linux username and password on first launch, enter them now. Choose a regular username; no characters appear as you type the password. If this installation already has a user, keep that user.

Launch the selected distribution by name, starting at its Linux home.

**Terminal: Windows PowerShell, ordinary user, same selection window.**

```powershell
if (-not $CourseDistro -or $CourseDistroNames -cnotcontains $CourseDistro) { throw 'STOP: select the installed distribution first.' }
wsl --distribution $CourseDistro --cd ~
if ($LASTEXITCODE -ne 0) { throw 'STOP: the named Ubuntu session returned an error.' }
```

**Expected:** Ubuntu opens as your ordinary Linux user. The PowerShell exit check runs when you leave Ubuntu.

**Stop:** launch fails or first-user setup does not finish.

**Recovery:** keep the error and ask the owner to repair the selected distribution without resetting it.

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

**Expected:** Your regular username, a writable `/home/` path, Ubuntu `24.04` or `26.04`, and `x86_64` or `aarch64`/`arm64`. Use `df` to check available space only: you need at least 25 GB. The mount-point column does not have to start with `/home`.

**Stop:** root user, unsupported release/processor, redirected home, failed command, or less than 25 GB available.

**Recovery:** Choose the correct existing Ubuntu user and distribution, or ask the owner to set up a supported one. If space is low, free space in the Linux filesystem; don't move course work under `/mnt/`.

## Check Git, Python, curl, and certificates

Before installing packages, check what's already in Ubuntu. Its `python3` package provides a supported Python version on [24.04](https://packages.ubuntu.com/noble/python3) and [26.04](https://packages.ubuntu.com/resolute/python3).

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

**Expected:** Git and curl show their versions, followed by the certificate confirmation. Run the Python check below too. Skip package installation only if all these checks pass, including Python 3.12 or newer.

**Stop:** any prerequisite is absent or resolves to Windows.

**Recovery:** After device-owner approval, install any missing packages in the next step. Keep certificate verification on.

Install the prerequisites only if the checks found something missing. At a `sudo` password prompt, enter your Linux password; no characters appear.

**Terminal: Ubuntu Bash, ordinary Linux user invoking sudo for package changes, same window.**

```bash
sudo apt-get update && sudo apt-get install -y git python3 curl ca-certificates
```

**Expected:** both package operations finish successfully. Recheck prerequisites and resolve Python below.

**Stop:** a package has no candidate, a source is unavailable, or permission is denied.

**Recovery:** Keep the apt output and ask the owner to fix the approved Ubuntu package sources. Don't add other sources or upgrade the whole system to pass this check.

## Choose the Python interpreter

Later steps use one Python program at its full path, stored as `PY`. This step tries `python3.12`, `python3`, then `python`, and keeps the first Linux interpreter that reports version 3.12 or newer through `sys.executable`. An older interpreter's version line doesn't pass the check. Find and run the first suitable Linux interpreter.

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

PATH lists the folders this Ubuntu terminal searches when you type a command name. The export in this window lasts only until you close it. A later window will find `omp` only if it reads a startup file with the same line.

A Bash login shell reads the first file it finds in this order: `.bash_profile`, `.bash_login`, `.profile`. An interactive non-login shell reads `.bashrc`. Follow that [Bash startup-file precedence](https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html) rather than creating a new override file. Add the nonsecret PATH line to `.profile`, `.bashrc`, and any existing login override.

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

**Expected:** Each selected startup file prints `PATH_LINE already present` or `PATH_LINE added`. The file's existing bytes stay in place, even if its last line had no newline. Only this Ubuntu setup window gets an immediate PATH export.

**Stop:** a link, non-file, redirected home/bin, or permission error appears.

**Recovery:** Keep the files and ask the device owner to fix the named path. Don't replace a linked profile. After it's fixed, save PATH here and check it in a new Ubuntu window opened separately.

## Download Oh My Pi and verify it before it can run

Download the chosen Linux binary and `SHA256SUMS.txt` from the pinned release into a new directory for this attempt alone. The published file gives a lowercase SHA-256 fingerprint, followed by two spaces and the exact filename. Don't move the binary into place or make it executable unless that line matches the file you downloaded.

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

**Expected:** `SHA256 VERIFIED` names the chosen Linux file before you run it for the first time, followed by `omp/18.3.5`. Keep the download folder as evidence. Only a file that passed this check becomes executable.

**Stop:** A download, checksum, destination, permission, or run check fails. The function returns you to the prompt without leaving the shell set to exit on later errors.

**Recovery:** Keep the failed directory and the existing installation. Fix the reported error before making a new attempt; don't turn off certificate checks, delete evidence, or run a file that hasn't passed verification.

## See the binary in this window

The export above applies only to this Ubuntu window. It doesn't show whether a new window will find `omp`. Check that later in a new terminal window without exporting PATH first. For now, check the selected binary here.

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

Check whether the Git credentials you already have can read the course repository. If this access check fails, check your account or repository access, not folder permissions.

**Terminal: Ubuntu Bash, ordinary Linux user, same Ubuntu window.**

```bash
GIT_TERMINAL_PROMPT=0 git ls-remote --exit-code https://github.com/TheHolofex/AIHB_OCT_2026.git HEAD
```

**Expected:** A commit hash followed by `HEAD`, without a credential prompt. If you see it, skip all GitHub CLI steps below and go to the checkout without changing credential helpers or signing in again.

**Stop:** access fails or no HEAD is returned.

**Recovery:** Keep the error and check your network access and repository invitation. Use the steps below only if you need to set up credentials.

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

**Recovery:** Ask the owner to approve installation from Ubuntu's [Universe gh package](https://packages.ubuntu.com/noble/gh). Universe must already be set up as an approved source. If it isn't available or approved, stop and ask the owner; don't enable it or add another source yourself.

Install the fallback package only after that source approval. Enter your Linux password at the hidden `sudo` prompt if asked.

**Terminal: Ubuntu Bash, ordinary Linux user invoking sudo for package changes, same window.**

```bash
sudo apt-get update && sudo apt-get install -y gh
```

**Expected:** installation succeeds; repeat the gh check above.

**Stop:** no candidate, source failure, or permission denial.

**Recovery:** keep the apt message and have the owner resolve the approved source. Do not add a repository.

Sign in with the GitHub account invited to the repository. The next command shows a device code for browser sign-in. Open the GitHub page it shows, enter the code, and check the account before you authorize access. GitHub credentials are separate from your course-site password and OpenRouter key. [GitHub CLI login](https://cli.github.com/manual/gh_auth_login) prefers an OS credential store but may use a plaintext file instead; don't use `--insecure-storage`. If login asks to configure Git, decline until you've checked storage below.

**Terminal: Ubuntu Bash, ordinary Linux user, same Ubuntu window; interactive login.**

```bash
gh auth login --hostname github.com --git-protocol https --web
```

**Expected:** browser authorization completes for the invited account.

**Stop:** denied authorization, wrong account, or login failure.

**Recovery:** keep the nonsecret error and ask the repository owner to confirm the account/invitation before trying again.

Check the account and credential storage status in this Ubuntu window. Don't share the output or ask to see the token. See [gh auth status](https://cli.github.com/manual/gh_auth_status).

**Terminal: Ubuntu Bash, ordinary Linux user, same Ubuntu window.**

```bash
gh auth status --hostname github.com
```

**Expected:** successful status for the intended account, with storage approved by your device policy.

**Stop:** Status fails, the account is wrong, or your device policy doesn't approve the reported storage. If you can't tell where the credentials are stored, stop and ask the owner to review it.

**Recovery:** Ask the device owner to set up approved storage or credentials. A successful browser login alone isn't enough to continue.

After storage approval, set up the credential helper for github.com only, then repeat the repository check with prompts disabled. [Host-specific setup](https://cli.github.com/manual/gh_auth_setup-git) doesn't give you repository access on its own.

**Terminal: Ubuntu Bash, ordinary Linux user, same Ubuntu window.**

```bash
gh auth setup-git --hostname github.com &&
  GIT_TERMINAL_PROMPT=0 git ls-remote --exit-code https://github.com/TheHolofex/AIHB_OCT_2026.git HEAD
```

**Expected:** a commit hash and `HEAD` after helper setup succeeds.

**Stop:** either command fails.

**Recovery:** Keep the error and ask the repository owner to check your invitation and access. Don't clone until this access check succeeds.

## Use the course checkout, or clone it once

Keep the course checkout at `$HOME/Documents/AIHB_OCT_2026` inside your Linux home. If the course checkout is already there with the right origin, use it as it is. If that path holds a different folder, leave it alone. Check the destination, then use the existing checkout or clone it.

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

**Recovery:** Leave the existing folder in place. If it holds the wrong project, choose a different computer folder only with the person who supports your machine; don't delete, reset, pull, or clean this one. If cloning failed, fix the recorded access or network error first. Keep partial folders and don't retry over them. The command follows GitHub's instructions for [Cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

`$R` and `$M` exist only in this shell. In the new window for the readiness check, set `R`, `M`, and `PY` again. A function defined only in this shell won't be available there either.

## Enter the key without showing it

At the hidden prompt in Ubuntu, type the key and press Enter. The next command only waits for your input; don't put the key in the command, a file, a profile, or a chat. The rules for where a key must not go are in [Connect the course account without leaking a key](../shared/CREDENTIALS.md).

**Terminal: Ubuntu Bash, ordinary Linux user, same Ubuntu window.**

```bash
IFS= read -r -s OPENROUTER_API_KEY
```

**Expected:** the prompt returns, and the key does not appear as readable text.

**Stop:** the key appears in readable text, or you pasted it into the command line instead of the prompt.

**Recovery:** if the key was displayed or pasted into a command, revoke it with the provider, use the replacement, and run only this command again. Do not continue with a key that has been displayed.

## Load the key into this process only

The next command makes the key available to programs started from this Ubuntu terminal and prints only `SET` or `MISSING`. Run it separately after the hidden-read command. A child shell can inherit the key, so `SET` alone doesn't mean the key was saved in a profile or leaked. `MISSING` means this process has no nonempty key variable; it doesn't tell you whether a key exists in a file elsewhere.

After the hidden prompt returns, export the key so programs started from this process can use it.

**Terminal: Ubuntu Bash, ordinary Linux user, same Ubuntu window.**

```bash
export OPENROUTER_API_KEY
if [ -n "${OPENROUTER_API_KEY:-}" ]; then printf 'SET\n'; else printf 'MISSING\n'; fi
```

**Expected:** `SET`.

**Stop:** `MISSING`, or any output that contains the key.

**Recovery:** Run the hidden-read command again in this same shell, then run the export again. Don't print the variable to check the key, and don't save it to `.profile` or any other file.

## Open an independent terminal and read the difference

Open a new Windows PowerShell window from Start, separate from the Ubuntu window that holds the key. Don't type `bash` or start PowerShell inside that Ubuntu process. A child process can inherit its key. A new window opened separately normally prints `MISSING`, though an approved parent environment or startup profile may still provide a value.

In the new Windows PowerShell window, launch the same distribution by its exact name. Enter the name you recorded again, because this window doesn't have variables from the earlier PowerShell session.

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

**Recovery:** keep the error and select the recorded name. Do not use the default distribution as a substitute.

Check the saved OMP path in this Ubuntu window. Don't export PATH or try to repair it in this block.

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

**Recovery:** If the path or version is wrong, don't export PATH in this window; that would hide the problem. Keep every folder under `$HOME/course-evidence`, including download logs. Run the path-miss block below, then open another new Ubuntu window and run this check again. If this separately opened window prints `SET`, check the profile before entering a key. Don't print the variable or upgrade packages.

Fix only the startup file this Bash window reads. Then reopen the named Ubuntu distribution in a separate window.

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

**Expected:** You see `selected omp/18.3.5`, a message telling you whether this window is a login shell, and either `PATH_LINE added` or a STOP line saying the line is already present. Nothing under `$HOME/course-evidence` is deleted.

**Stop:** The selected binary is missing, the startup file is not a regular file, this window is not Bash, or the line is already present and `omp` is still not on this window's own PATH.

**Recovery:** Don't export PATH in this window or delete the download folders. If you just added the line, close this window, run the independent named-distribution launch block again, then check the path again without exporting PATH. If the line was already there, save the printed lines and stop. Don't upgrade Ubuntu or change security settings.

## Set the course paths in this window

The earlier Ubuntu window had `R`, `M`, and `PY`, along with functions that are not available in this new window. Set the paths here before running any readiness-check command. This block does not clone, reset, pull, or clean.

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

**Recovery:** If the lab file is missing, keep the checkout and ask the owner for a complete course checkout. Don't delete or replace the home folder. If Python is missing, return to the package step. Don't call a function from the closed window.

## Investigate unexpected key presence without displaying it

Run this only if the independent terminal printed `SET` before you entered a key. It checks shell profiles for the variable name without printing its value.

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

**Expected:** only the names of profiles containing a reference, or `No profile reference was found.` The reference might be a check, a comment, or an approved use of a parent variable; its presence does not tell you whether a secret was saved or exposed.

**Stop:** the independent window's unexpected `SET` remains unexplained.

**Recovery:** Review the named file privately with the device owner, and check how the parent application passes variables to this window. Don't print profile lines, dump the environment, or share values. If someone unintentionally saved a secret assignment, remove it with the owner's guidance and check whether the secret was exposed; revoke it only if it was exposed or policy requires it. If you understand and have approval for the inherited variable, continue to the hidden-input step. The reference alone does not tell you whether the key persists or authentication works.

## Enter the key again in the new window

Run the readiness check in this independent window only after it has printed the saved `omp` path without another PATH export. The key is usually missing unless a reviewed parent environment passes it in. Enter it through the hidden prompt again, then export it separately. Don't paste the key into the export command instead of using the hidden prompt.

**Terminal: Ubuntu Bash, ordinary Linux user, same Ubuntu window.**

```bash
IFS= read -r -s OPENROUTER_API_KEY
```

**Expected:** the prompt returns, and the key is not readable on screen.

**Stop:** the key is visible as readable text.

**Recovery:** revoke a displayed key, then run this read again.

After the hidden prompt returns, export the key so programs started from this process can use it.

**Terminal: Ubuntu Bash, ordinary Linux user, same Ubuntu window.**

```bash
export OPENROUTER_API_KEY
if [ -n "${OPENROUTER_API_KEY:-}" ]; then printf 'SET\n'; else printf 'MISSING\n'; fi
```

**Expected:** `SET`.

**Stop:** `MISSING`, or any output that contains the key.

**Recovery:** run the hidden read and this export again in this shell. Do not continue to the readiness check on `MISSING`.

## Prepare a fresh readiness check

Keep the work folder outside the course checkout. Before you start, this window must have printed `R`, `M`, and `PY`. Python's secrets module creates the token outside the work folder, then copies it in so the model must read it. At this point, the evidence folder is only a path: don't create it or `from-omp.txt` yourself. Create the new attempt and its input token now.

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

**Recovery:** Keep any partial attempt. Fix the reported path or permission problem, then run the block again with new paths. Don't delete the course checkout or download logs, and don't create the evidence folder or `from-omp.txt` yourself. If the STOP line says `PY` is unset, paste the path-assignment block in this window first.

## Ask for the one permitted write

The launcher runs the pinned Oh My Pi binary and lets it write only `from-omp.txt`. It reads the key from this process. Exit 2 means a prerequisite failed before the evidence folder was created; the `HOLD:` line tells you which one, and a missing key is only one possibility. Exit 1 means the live attempt failed after work began. Keep every failed live attempt as HOLD. Don't rerun the launcher in that attempt, change providers, or use a fallback model. Fix the named problem, then create a new attempt. Run the supplied launcher once against the fresh paths.

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

**Stop:** If you see `launcher exit 2` and a `HOLD:` line, a prerequisite failed. The evidence folder should still be absent; don't make the result file yourself. `launcher exit 1` means the live attempt failed. Stop too if exit 0 appears without an evidence folder.

**Recovery:** Read the `HOLD:` line to find out what failed; exit 2 does not always mean the key is missing. If it says `OPENROUTER_API_KEY unavailable`, enter the key through the hidden prompt and export it separately in this window. Then return to “Prepare a fresh readiness check” for new paths. If it says `omp is not on PATH` or the pinned version did not match, return to the independent-terminal check. Don't export PATH here or enter the key to fix that problem. If a directory is missing, already exists, or overlaps, keep the attempt, fix the named path problem, and prepare a fresh readiness check. If `course_guard.mjs` is missing, the checkout is incomplete; don't reset, pull, or clean it. Exit 1 means the live attempt failed; it is not an authentication prompt. Don't delete `$HOME/course-evidence` or write `from-omp.txt` yourself.

## Check the write against the token and the receipt

The checker uses the work folder, the token file outside it, and the evidence folder. It passes only if `from-omp.txt` contains `omp works`, one space, and this run's token, and the `course_write` receipt agrees with the file on disk. Run it to check the token, receipts, and pinned identities.

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

**Stop:** The last result line is `READINESS CHECK HOLD`, `checker exit` is not 0, or the result file is missing. Creating the file yourself does not count as a pass.

**Recovery:** Keep this failed attempt as HOLD. Fix the specific checker failure before returning to “Prepare a fresh readiness check” with new folders. Don't edit `from-omp.txt` to make the words match. If the STOP line says `PY` or `M` is missing, paste the path-assignment block in this window first.

## Read the actual result file

After `READINESS CHECK PASS`, read the file from disk yourself. This command does not build the expected answer.

**Terminal: Ubuntu Bash, ordinary Linux user, same independent window.**

```bash
cat -- "$proof/from-omp.txt"
```

**Expected:** `omp works`, one space, and this attempt's token, matching the successful checker.

**Stop:** missing/unreadable file or contents differ from the checked result.

**Recovery:** keep the attempt as HOLD and investigate the changed or missing file. Do not write a replacement by hand or retry the live turn in this folder.

## Record prerequisites, not the live turn

This report checks whether Git, Python, Oh My Pi, the checkout, and the key are present in this process. A passing report checks those prerequisites, not the live write; the readiness check you already ran checks the write. Local changes in the checkout are no reason to reset, pull, or clean it. Save the separate prerequisite report now.

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

**Stop:** `SETUP CHECK HOLD` appears, the report exits nonzero, the report path already exists, the report contains the key, or the command says `R` or `M` is missing. A hold here means a prerequisite failed, so editing the result file won't fix it. A pass here also does not replace `READINESS CHECK PASS`.

**Recovery:** Fix the first failed prerequisite named in the report. Once the timestamp changes, run this report command again so it uses a new path, and keep the failed report. Don't reset, pull, or clean the checkout because the report lists local changes. Continue only after both the prerequisite report and the live readiness check pass.


## Set up local Obsidian

Obsidian lets you follow links and edit notes in a **vault**, an ordinary folder of Markdown text files. Allow about 25–40 minutes for Obsidian setup; an approved host repair can take longer. Run Linux Obsidian through WSLg in the same selected Ubuntu distribution and Linux home as OMP, Python, and your checkout. [Obsidian reads local files and refreshes external changes](https://github.com/obsidianmd/obsidian-help/blob/master/en/Files%20and%20folders/How%20Obsidian%20stores%20data.md).

Keep the vault outside the checkout and any synced folder. Don't open a `\\wsl$` or `\\wsl.localhost` vault in native Windows Obsidian, copy it to `/mnt/c`, or create another distribution for this step. Keep existing installations, personal vaults, and profiles.

### Confirm this host can display Linux applications

[Microsoft WSLg requirements](https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps) call for Windows 10 build **19044+** or Windows 11, with your selected distribution running as **WSL 2**. Builds 19041–19043 may meet the earlier command-line OMP requirement, but Obsidian remains at **Obsidian HOLD**. Even if the version and display variables look right, you still need to see an application window open.

Open a separate ordinary PowerShell window from Start. Keep your Ubuntu proof window open. Re-select the exact Ubuntu name you used earlier; this does not change the default distribution.

**Terminal: Windows PowerShell, ordinary user, separate Windows window.**

```powershell
$ErrorActionPreference = 'Stop'
$ObsidianHost = Get-CimInstance -ClassName Win32_OperatingSystem
$ObsidianHost | Select-Object Caption, Version, BuildNumber
if ([int]$ObsidianHost.BuildNumber -lt 19044) { throw 'Obsidian HOLD: WSLg needs Windows build 19044+ or Windows 11.' }
wsl --list --verbose
if ($LASTEXITCODE -ne 0) { throw 'Obsidian HOLD: cannot inspect distributions.' }
$CourseDistroNames = @(wsl --list --quiet)
if ($LASTEXITCODE -ne 0) { throw 'Obsidian HOLD: cannot read distribution names.' }
$CourseDistroNames = @($CourseDistroNames | ForEach-Object { ($_ -replace "`0", '').Trim() } | Where-Object { $_ })
$CourseDistro = Read-Host 'Enter the exact Ubuntu NAME used for your existing OMP proof'
if ($CourseDistroNames -cnotcontains $CourseDistro) { throw 'Obsidian HOLD: exact distribution not installed.' }
$CourseWslVersion = Read-Host 'Enter the VERSION shown for that exact NAME'
if ($CourseWslVersion -ne '2') { throw 'Obsidian HOLD: this distribution must run as WSL 2.' }
wsl --distribution $CourseDistro --exec printenv WSL_DISTRO_NAME HOME
if ($LASTEXITCODE -ne 0) { throw 'Obsidian HOLD: selected distribution did not report its name and home.' }
```

**Expected:** a supported host at the GUI build floor, the exact selected entry at VERSION `2`, then its distribution name and Linux home. **HOLD:** wrong or missing distribution, old host, WSL 1, or command failure. **Recovery:** Keep the current distribution and OMP result. Ask the device owner to resolve host support, display drivers, or WSLg availability. Before any WSL update or restart, save work in all affected distributions and Docker applications, and get approval for the window. Don't reset or unregister the distribution, or use a global `wsl --shutdown` as a quick fix.

Return to the existing Ubuntu proof window. Confirm its name and home match the selected distribution above. If that window was closed, use [the named Ubuntu launch](#launch-and-verify-ubuntu) and [restore the course paths](#set-the-course-paths-in-this-window) there first.

**Terminal: Ubuntu Bash, ordinary Linux user, same selected distribution and proof window.**

```bash
printf 'Distribution: %s\nHome: %s\n' "${WSL_DISTRO_NAME:-missing}" "$HOME"
printf 'Display: %s\nWayland: %s\n' "${DISPLAY:-missing}" "${WAYLAND_DISPLAY:-missing}"
uname -m
if [ ! -d /mnt/wslg ] || { [ -z "${DISPLAY:-}" ] && [ -z "${WAYLAND_DISPLAY:-}" ]; }; then
  printf 'Obsidian HOLD: WSLg display support is unavailable\n'
else
  printf 'WSLg display indicators present; actual Obsidian window still required\n'
fi
```

**Expected:** the same distribution and `/home/` path as before, `x86_64` or `aarch64`, and display indicators present. **HOLD:** any mismatch, missing display support, or another processor. **Recovery:** Stop Obsidian setup and keep the output for the owner. Don't invent display variables or substitute a native Windows app.

### Preserve an existing Linux app, or download the matching asset

Look for an existing **Obsidian** launcher under this Ubuntu distribution in Start, and check the Linux application/AppImage location you already know. In Ubuntu, `command -v obsidian` and `dpkg-query -W obsidian` may find a command or Debian package, but no result does not rule out an AppImage or another package route. If you find an existing Linux app, launch it the usual way as an ordinary user and skip both new-install routes. Later, record the version shown in Obsidian’s Settings. Keep any Windows installation too, but don't use it for this Linux vault. If you're unsure who owns the installation, how to launch it, or whether it is installed, record **Obsidian HOLD** for owner review rather than installing another copy.

Only after confirming Linux Obsidian is absent and obtaining device-owner installation approval, download into a new folder in this Linux home. The exact assets and SHA-256 values are from the [official 1.13.7 release metadata](https://api.github.com/repos/obsidianmd/obsidian-releases/releases/tags/v1.13.7). This block does not install or execute the download.

**Terminal: Ubuntu Bash, ordinary Linux user, same selected distribution and window.**

```bash
course_download_obsidian_wsl() {
  local obsidian_expected
  case "$(uname -m)" in
    x86_64)
      ObsidianAsset='obsidian_1.13.7_amd64.deb'
      obsidian_expected='17dc33b49cb3e785ecc27edd2ea0c79e40207798b554fd2886e36ebee7af9ae0' ;;
    aarch64)
      ObsidianAsset='Obsidian-1.13.7-arm64.AppImage'
      obsidian_expected='e286fd2bb2a5d346a35a577bd764c73fd5537dddec2b99a1a3e5e35974085203' ;;
    *) printf 'Obsidian HOLD: no approved asset for this processor\n'; return 1 ;;
  esac
  case "$HOME" in /home/*) ;; *) printf 'Obsidian HOLD: use the existing Linux home\n'; return 1 ;; esac
  ObsidianDownload="$(mktemp -d "$HOME/obsidian-download.XXXXXXXX")" || return 1
  curl --fail --location --show-error \
    "https://github.com/obsidianmd/obsidian-releases/releases/download/v1.13.7/$ObsidianAsset" \
    --output "$ObsidianDownload/$ObsidianAsset" || return 1
  (cd "$ObsidianDownload" && printf '%s  %s\n' "$obsidian_expected" "$ObsidianAsset" | sha256sum --check -) || {
    printf 'Obsidian HOLD: checksum mismatch; do not execute or install\n'; return 1;
  }
  printf 'Verified download: %s/%s\n' "$ObsidianDownload" "$ObsidianAsset"
}
course_download_obsidian_wsl
```

**Expected:** the selected filename followed by `OK`, then its verified path. Save that path for later launches. **HOLD:** any failed command or mismatch. **Recovery:** Keep this download attempt. Fix the named network or path problem, then run the block again with a new download folder. Don't use a partial file.

### Install and launch the x64 Debian package

Use this route only for `x86_64`. With device-owner approval, install the verified local package using [Ubuntu apt](https://manpages.ubuntu.com/manpages/noble/man8/apt.8.html). Read the proposed changes before accepting, and decline if apt would replace an existing Obsidian installation, remove packages, or make other unapproved changes. The package manager checks downloaded repository dependencies against its usual signed metadata; don't disable those checks.

**Terminal: Ubuntu Bash, ordinary Linux user; sudo only for the approved apt operation.**

```bash
course_install_obsidian_deb() {
  [ "$(uname -m)" = x86_64 ] && [ -n "${ObsidianDownload:-}" ] || {
    printf 'Obsidian HOLD: wrong route or no verified download\n'; return 1;
  }
  if command -v obsidian >/dev/null 2>&1 || dpkg-query -W obsidian >/dev/null 2>&1; then
    printf 'Obsidian HOLD: existing command or package; preserve it\n'; return 1
  fi
  (cd "$ObsidianDownload" &&
    printf '%s  %s\n' '17dc33b49cb3e785ecc27edd2ea0c79e40207798b554fd2886e36ebee7af9ae0' 'obsidian_1.13.7_amd64.deb' | sha256sum --check - &&
    sudo apt install ./obsidian_1.13.7_amd64.deb)
}
course_install_obsidian_deb
```

**Expected:** checksum `OK` and successful package installation. **HOLD:** denial, unexpected transaction, or failed command. **Recovery:** keep the message and installation state for the owner; do not force replacement or attempt unrelated package repairs.

**Terminal: Ubuntu Bash, ordinary Linux user, same window; after successful x64 installation.**

```bash
obsidian &
```

**Expected:** an actual Linux Obsidian window appears on the Windows desktop. **HOLD:** display error, sandbox refusal, or no window. **Recovery:** keep the error for the owner; do not add sandbox flags to this package route or change kernel security settings.

### Prepare and launch the ARM64 AppImage

Use this route only for `aarch64` on the supported Ubuntu 24.04 or 26.04 you checked earlier. An AppImage is a single application file; keep it at the verified download path. It needs the FUSE compatibility library. [AppImage’s FUSE guidance](https://docs.appimage.org/user-guide/troubleshooting/fuse.html) names `libfuse2t64` for Ubuntu 24.04 and explains how the older library can stay alongside FUSE 3. Don't install the obsolete `fuse` package or remove FUSE 3.

Check the library first. If it is missing, the following function asks apt to install only the compatibility library. Obtain device-owner approval before that transaction and review its proposed changes at the prompt. Decline any removal or unapproved change.

**Terminal: Ubuntu Bash, ordinary Linux user; sudo only for the approved apt transaction.**

```bash
course_obsidian_fuse() {
  [ "$(uname -m)" = aarch64 ] || { printf 'Obsidian HOLD: ARM64 route only\n'; return 1; }
  if [ "$(dpkg-query -W -f='${Status}' libfuse2t64 2>/dev/null)" = 'install ok installed' ]; then
    printf 'libfuse2t64 already installed; preserving it\n'
  else
    sudo apt update || return 1
    sudo apt install libfuse2t64 || return 1
  fi
  dpkg-query -W -f='${Package} ${Status}\n' libfuse2t64
}
course_obsidian_fuse
```

**Expected:** `libfuse2t64 install ok installed`. **HOLD:** missing library, denied approval, repository/signature error, or unexpected package changes. **Recovery:** Keep the error and ask the owner to resolve how to install the approved dependency. Don't replace FUSE 3 or try a privileged FUSE repair on your own.

Get **separate device-owner approval** before this launch. The vendor’s [AppImage launch instructions](https://github.com/obsidianmd/obsidian-help/blob/master/en/Getting%20started/Download%20and%20install%20Obsidian.md) include `--no-sandbox`. This flag turns off Chromium’s renderer sandbox for Obsidian, which lowers protection if renderer content is compromised. It does not improve or replace the course tool boundary. Use only the supplied local practice vault, and keep community plugins restricted. Without approval, record **Obsidian HOLD** and do not run this block. Don't change kernel-wide security toggles, make the file world-writable, or add privileged sandbox fixes.

**Terminal: Ubuntu Bash, ordinary Linux user, same window; separately approved ARM64 launch only.**

```bash
course_launch_obsidian_arm64() {
  [ "$(uname -m)" = aarch64 ] && [ -n "${ObsidianDownload:-}" ] || {
    printf 'Obsidian HOLD: wrong route or missing verified path\n'; return 1;
  }
  [ "$(dpkg-query -W -f='${Status}' libfuse2t64 2>/dev/null)" = 'install ok installed' ] || {
    printf 'Obsidian HOLD: libfuse2t64 is missing\n'; return 1;
  }
  (cd "$ObsidianDownload" &&
    printf '%s  %s\n' 'e286fd2bb2a5d346a35a577bd764c73fd5537dddec2b99a1a3e5e35974085203' 'Obsidian-1.13.7-arm64.AppImage' | sha256sum --check - &&
    chmod u+x ./Obsidian-1.13.7-arm64.AppImage &&
    ./Obsidian-1.13.7-arm64.AppImage --no-sandbox) &
}
course_launch_obsidian_arm64
```

**Expected:** checksum `OK`, then a Linux Obsidian window. A background job number alone does not mean the app opened. **HOLD:** checksum, FUSE, display, or security error; absent approval; or no window. **Recovery:** Keep the app and error for owner review. Don't extract it as an unapproved fallback or substitute another architecture.

### Open the exact Linux-home vault and save a linked reply

This creates a fresh practice vault using the existing Linux `$PY` and `$M`. It makes no provider call and needs no key entry. Run it only after an actual Obsidian window is available.

**Terminal: Ubuntu Bash, ordinary Linux user, same selected distribution and proof window.**

```bash
course_initialize_obsidian_wsl() {
  [ -n "${PY:-}" ] && [ -n "${M:-}" ] || {
    printf 'Obsidian HOLD: restore Linux Python and course paths first\n'; return 1;
  }
  ObsidianHelper="$M/scripts/obsidian_readiness.py"
  [ -f "$ObsidianHelper" ] || { printf 'Obsidian HOLD: course helper missing\n'; return 1; }
  ObsidianRoot="$HOME/obsidian-readiness-$("$PY" -c 'import uuid; print(uuid.uuid4().hex)')" || return 1
  "$PY" "$ObsidianHelper" initialize --root "$ObsidianRoot" || return 1
  ObsidianVault="$ObsidianRoot/vault"
  printf 'Attempt root: %s\nVault to open: %s\n' "$ObsidianRoot" "$ObsidianVault"
}
course_initialize_obsidian_wsl
```

**Expected:** `Created practice vault:` and the exact Linux-home vault path. Save the printed root path for this attempt. **HOLD:** any error, redirected path, synced location, or wrong home. **Recovery:** Keep the attempt and restore the page’s Linux paths, or ask the owner for a complete checkout. Don't initialize an existing vault or move it onto `/mnt/c`.

**Window: Linux Obsidian displayed by WSLg, ordinary Linux user.**

1. Use **Open folder as vault → Open** in the vault chooser. From an existing personal vault, use **Open another vault** first and leave its settings as they are. In the Linux folder chooser, press **Ctrl+L** if a location field is needed, enter the exact printed `$ObsidianVault` path, and select it. Do not select the attempt parent or checkout.
2. In this practice vault’s **Settings → Community plugins**, leave **Restricted mode** on; turn it on for this vault if it is off. In **Settings → Core plugins**, turn **Sync** off if it is on. Do not sign in, connect a remote vault, install plugins, or configure MCP. Record the actual version from **Settings → General**, then close Settings.
3. Open **Start** in the file list. Switch to **Reading view** through the note’s view control if necessary, then click **Token**. Read the token and follow **Reply** from Token.
4. Switch Reply to **Editing view** with its view control. Enter only the token you read, on one line. Add no heading, quotes, or explanation. Press **Ctrl+S** and wait for the note to save.

**Expected:** both links open existing notes in the exact vault, and Reply contains the value you saw. **HOLD:** wrong vault, unavailable GUI, missing links, or blocked editing. **Recovery:** Check the exact path and the named failure. Don't enter the reply from Bash or use another editor to stand in for what you saw in Obsidian.

**Terminal: Ubuntu Bash, ordinary Linux user, same window.**

```bash
"$PY" "$ObsidianHelper" check --root "$ObsidianRoot"
```

**Expected:** `Token generation 1: initial token; external refresh not yet exercised`, `PASS: Obsidian file round-trip; GUI observation still required`, and a new disk-record path. **HOLD:** any failed check. **Recovery:** Correct Reply in Obsidian to match the current Token and save, then repeat `check`. Keep every record; never edit Start, Token, or expected-value records to force a pass.

### Observe the outside edit and reopen the same vault

Leave Token visible in Reading view in the open app. Change it from outside Obsidian using this command.

**Terminal: Ubuntu Bash, ordinary Linux user, same window.**

```bash
"$PY" "$ObsidianHelper" refresh --root "$ObsidianRoot"
```

**Expected:** `Source token rotated outside Obsidian; your saved reply was preserved.` **HOLD:** any error. **Recovery:** keep the attempt and named failure for support. Do not reinitialize it or remove its records.

**Window: Linux Obsidian, same practice vault.** Return to Token and watch for its new value while the vault is still open. Follow Reply, replace the old value with the new one in Editing view, and press **Ctrl+S**. Close only this practice-vault window. Reopen it with the same existing Linux launcher, `obsidian &` for the fresh x64 package, or `course_launch_obsidian_arm64` for the separately approved AppImage in the same Ubuntu shell. If needed, use the vault chooser to open the exact `$ObsidianVault` again. Open Reply and check that the new value is still there.

**Expected:** you see the outside change before closing the app, and the second saved reply remains after reopening. **HOLD:** stale Token, wrong reopened vault, failed relaunch, or missing reply. **Recovery:** Record what failed. Reopening to make a stale token appear does not show that Obsidian refreshed while open. Fix the cause, run another `refresh` with the right vault open, then watch the change, edit, save, and reopen again. Keep the same Linux home and all earlier records.

**Terminal: Ubuntu Bash, ordinary Linux user, same window.**

```bash
"$PY" "$ObsidianHelper" check --root "$ObsidianRoot"
```

**Expected:** a refreshed token generation, the qualified PASS line, and a new disk-record path. **HOLD:** any mismatch or helper failure. **Recovery:** inspect the exact vault and saved Reply, keep the record of what failed, and repeat the failed step in Obsidian.

Keep a separate record of what you saw in the Obsidian window directly under the printed `$ObsidianRoot`, outside `vault`. In your usual text editor, create a new `gui-observation.txt` there, but don't replace an existing file. Write down the date, Windows build, exact Ubuntu name and release, WSL VERSION, Linux architecture, Obsidian version you're running, exact vault path, Start → Token → Reply navigation you saw, both edits and saves, the live external refresh, and Reply after reopening. Include the two disk-record paths and any remaining failure. On ARM64, record whether the separate sandbox exception was approved. Screenshots of the practice vault can support your record, but leave out keys and unrelated personal windows.

Record **Obsidian READY** only after you've seen all these actions in the Obsidian window and both checks of the files on disk have passed. Otherwise, record **Obsidian HOLD** and name the action that failed or was unobserved. Files and `.obsidian` settings alone cannot show that Obsidian works in its window. Keep OMP, Obsidian, and n8n results separate; an Obsidian HOLD does not erase an OMP pass. Check WSLg in this distribution on this laptop: results from native Windows or macOS cannot stand in for what happens here.

## Prepare local n8n for Module 7

Open the local visual workflow editor and confirm that a saved workflow remains after you stop and restart it. Keep this result separate from `SETUP CHECK PASS` and the live OMP `READINESS CHECK PASS`. An n8n HOLD does not erase an OMP pass, but Module 7 needs n8n ready. The time needed for installation and image downloads varies with the device and network.

### Check the Windows host and approvals

[Microsoft’s simplified WSL installation](https://learn.microsoft.com/en-us/windows/wsl/install) requires Windows 10 build 19041+ or Windows 11. Docker’s current WSL backend requirements are stricter: WSL package 2.1.5+, Windows 10 22H2 build 19045 or Windows 11 23H2 build 22631+, a supported edition and servicing status, 8 GB RAM, SLAT, hardware virtualization enabled, and the Windows Server service (`LanmanServer`) enabled with Automatic startup. Docker lists Enterprise, Pro, and Education in its requirements and separately discusses Home for Linux containers; have the owner confirm eligibility for the exact host. Windows Server is unsupported. See [Docker’s current Windows requirements](https://docs.docker.com/desktop/setup/install/windows-install/) before downloading. Passing the earlier native-tool or Microsoft WSL floor alone is insufficient.

On Windows Arm, choose the **Arm (Early Access)** download only if the owner approves its Early Access status; Windows containers are unsupported. Published arm64 images do not show that this course stack works on a Windows Arm laptop. Keep n8n on HOLD until this device passes the checks below. An x64 host must pass them too.

Ask the device owner to confirm [Docker Desktop licensing](https://docs.docker.com/subscription-billing/desktop-license/). It's free for personal use, education, non-commercial open source, and qualifying small businesses (fewer than 250 employees AND under $10 million revenue). Professional use outside those limits and use by government entities require a paid subscription. Don't assume a work laptop qualifies because this is a class.

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

**Expected:** you've recorded the host and WSL versions without changing the distributions. You've noted whether Desktop is absent, already running, or installed but stopped, and recorded the Docker inventory from the approved running engine. For a fresh installation, nothing is listening on port 5678. An existing course instance may already use that port.

**Stop:** licensing, privileges, host support, virtualization, or WSL approval is unresolved; Docker points to an unexpected/remote engine; existing applications or port ownership are unclear; any inspection fails.

**Recovery:** work through the specific finding with the owner. Keep all applications, containers, volumes, checkouts, and earlier attempts. Don't kill a process, prune Docker, reset Desktop, or change contexts without knowing their effects. If a WSL/Docker prerequisite is denied, record **n8n HOLD** separately from OMP readiness.

Reuse the exact Ubuntu distribution and ordinary user selected earlier. Keep the existing course checkout at `$HOME/Documents/AIHB_OCT_2026` and its work/evidence paths intact. n8n belongs separately at `$HOME/n8n-course`; do not clone or relocate the course. If conversion or installation is needed, use the owner-approved sections above with their backup and restart steps.

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

**Expected:** Ubuntu has no separately installed Docker Engine/CLI packages and no `dockerd`; the checks can return nonzero when packages or processes are absent. **Stop:** an installed package, daemon, or unclear result may mean Docker is already installed. **Recovery:** ask the owner to check for custom installations too and keep their containers and volumes while resolving the conflict. These checks cannot rule out a daemon installed by hand.

Check `curl --version` and the certificate bundle in the inspection block below. If either is missing, use this package step only after owner approval; skip it when both are present.

**Terminal: Ubuntu Bash, ordinary Linux user, selected distribution; approved missing packages only.**

```bash
sudo apt-get update && sudo apt-get install --no-upgrade curl ca-certificates
```

**Expected:** the missing download prerequisites are installed; existing packages are not upgraded by the install command. **Stop:** policy denial, package failure, or a proposal to remove existing software. **Recovery:** keep the message and resolve it with the owner; do not weaken certificate verification or install a Docker daemon. Then repeat the following inspection.

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

**Expected:** `docker info` works for the approved Docker Desktop Linux engine when you run it as this ordinary user, and `docker compose version` works too. The modern plugin may report version 5; it doesn't have to start with `2.`. The Docker inventory matches the owner's known work, the destination is outside the checkout, and port 5678 is free for a fresh instance in both Windows and Ubuntu.

**Stop:** any command fails, Linux-home identity differs, an engine/context is unexpected, a Docker override is set, an unknown port listener exists, or there isn't enough storage for the full stack.

**Recovery:** review the integration and context with the owner, then try again in the intended Ubuntu shell. Never use `sudo` for the n8n installer, make the Docker socket world-writable, or start a second Ubuntu daemon. Seeing a CLI version doesn't show that you can reach the daemon. Keep an existing destination, even if incomplete, and ask its owner to identify its actual Compose project, data, version, and port. An existing installation must keep that identity and its owner-managed lifecycle; don't create a fresh identity or rename it. If the installation was already created with the recorded identity below, confirm that identity with the owner before reusing the helper. A different version means HOLD until the owner resolves it; it isn't permission to repin or upgrade.

### Create the fresh n8n configuration

Choose one installation method below only if the earlier checks passed and `$HOME/n8n-course` does not exist. The [official one-line setup](https://docs.n8n.io/deploy/host-n8n/install-options/one-line-setup) accepts the course's specified version `2.41.5` and `--no-start`. The [reviewed installer source](https://raw.githubusercontent.com/n8n-io/n8n/master/docker/get-n8n.sh) is version `1.4.0`, but the live URL can change. Prefer downloading and reviewing it so you can check the version before running it. If the installer says “existing install”, that message tells you neither the version nor whether n8n is ready.

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

**Recovery:** keep partial files and messages for owner review. Do not rerun over them, delete them, or use upgrade/uninstall flags. The following alternative downloads completely before execution; use it instead of the one-line option, not afterward.

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

**Expected:** the saved n8n port is exactly `127.0.0.1:5678:5678`; no other service publishes a port. **Stop:** the file differs from the expected stack, already belongs to another installation, or cannot be saved. **Recovery:** keep it and review with the owner before starting; do not replace a preexisting Compose file.

### Record the fresh project name

A Compose project name ties this stack to its containers, volumes, and networks. The Compose file path alone does not set that name; see [Docker project names](https://docs.docker.com/compose/how-tos/project-name/). If you've just created a fresh configuration and bound it to localhost, agree on a name with the owner that isn't in use before starting it for the first time. Use only lowercase ASCII letters, digits, underscores, and hyphens, and start with a letter or digit. Don't use this step for an existing installation.

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

**Expected:** all three Docker inspections succeed without finding resources for the approved name, then `.course-project` is created privately without overwriting a file or symlink. **Stop:** an invalid name, existing resource or record, failed inspection, or failed write. **Recovery:** keep all resources and files. Review the finding with the owner; do not remove resources or rename an existing installation to make the check pass.

### Use the recorded project and configuration

Define this helper in the same Ubuntu shell. It uses the saved name, `.env`, and `compose.yml` each time you run a stack command. Exported variables can take priority over `.env` even when you give its file path; see [Docker interpolation precedence](https://docs.docker.com/compose/how-tos/environment-variables/variable-interpolation/). If any listed override is exported, even with an empty value, the helper stops. It prints the variable name and HOLD, but never its value.

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

**Expected:** the helper is defined but starts nothing until you call it. **Stop:** any later call reports HOLD or fails. **Recovery:** ask the owner to resolve exported overrides in a clean shell. Then check the approved Docker engine/context and define the helper there again. Don't automatically unset variables or rewrite configuration. If the project record is missing, damaged, or unexpected, keep any existing record and the finding for owner review; don't recreate the record for an existing installation.

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

**Expected:** all six services appear. `sandbox-certs` has finished successfully as a one-shot service, `Exited (0)`; the other five are running, with healthy status wherever health checks are shown. The port output is exactly `127.0.0.1:5678`, and n8n reports `2.41.5`. **Stop:** a service is missing, restarting, or unhealthy; the certificate service failed; the port is public; a command failed; or n8n reports another version. **Recovery:** give initialization time to finish, then check again. If the problem persists, keep the result at HOLD. Review errors privately without exposing secrets, and don't change the pinned version, delete volumes, or disable services to force a pass.

### Save a blank workflow and prove it persists

In the Windows browser, open **http://localhost:5678**. For a fresh instance, complete **Set up owner account** with local credentials and select **Next**. This creates the local instance owner, not an n8n Cloud account. If a login page appears for an existing instance, use its existing owner login; do not reset it. Skip optional offers and surveys where offered. No external account, provider key, or paid activation is required. Leave **n8n Assistant** off.

Select **Overview**, then **Build a workflow** on a fresh instance or **Create workflow** when workflows already exist. Click the workflow title, name it **Module 7 Readiness**, and press **Enter**. The editor saves automatically; do not look for a required Save button. Leave the canvas blank and do not select **Publish**. Reload the browser page and confirm the name and blank canvas remain. Keep an existing workflow with that name; choose a distinct readiness name if it contains work.

**Expected:** local owner access, saved blank workflow, Assistant off, and workflow unpublished/inactive. **Stop:** Cloud signup, provider-key/payment request, wrong instance, missing saved workflow, or unavailable editor. **Recovery:** check the address and the inspected port/project with the owner. Keep the existing account and workflows; do not create another instance to hide a failure.

Stop only this confirmed course Compose project. This keeps its named volumes and workflow data.

**Terminal: Ubuntu Bash, ordinary Linux user, same selected distribution.**

```bash
course_n8n down
```

**Expected:** this project’s containers stop and are removed; volumes remain. **Stop:** command failure or evidence this is another owner’s project. **Recovery:** keep the output and confirm project ownership. Never add `-v` or run a volume prune.

**Terminal: Ubuntu Bash, ordinary Linux user, same selected distribution.**

```bash
course_n8n up -d
```

**Expected:** the same project starts again using its saved data. **Stop:** startup failure. **Recovery:** keep files/volumes, resolve the specific error, and repeat the service/version/port inspection above.

Repeat the service, version, and port inspection after restart. Reload **http://localhost:5678**, sign in with the same local owner if needed, and reopen **Module 7 Readiness**. Record **n8n READY** only if the correct version, localhost-only port, six-service state, and saved workflow all survive the restart. Otherwise, record **n8n HOLD** with the failed check, separately from both OMP results. In later sessions, check whether Desktop is running first. If it's stopped, get owner approval for the effects of starting it on existing work before launching it. Open the same Ubuntu distribution as the same ordinary user, inspect the approved Docker engine/context and your access to it, and define `course_n8n` again from the block above. Reuse the saved `.course-project`; never rerun `course_n8n_identify`. Use `course_n8n up -d`, the same helper inspection commands, and `course_n8n down`. Don't reset, uninstall, or upgrade as part of these steps.
