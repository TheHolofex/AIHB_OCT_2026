# Set up on macOS

Use Git, Python 3.12 or newer, and standalone OMP 18.3.5 with the supplied launcher to read and write a file. Plan for roughly 45 to 90 minutes, plus any system download time. You need a browser, an ordinary text editor, 15 GB free under your home directory, and permission to install any missing tools. Keep your work and evidence under your home directory, outside the checkout. If device policy blocks a step, stop and use the [support packet](../shared/TROUBLESHOOTING.md).

## Check the machine and existing prerequisites

Open the Terminal app while signed in to your ordinary user account, and check your macOS version, native architecture, and current shell. This Homebrew route needs macOS 15 or newer on supported hardware. Apple Silicon is the supported Homebrew setup; Intel is **Tier 3**, which means reduced support and possible source builds, not the same level of support. See [Homebrew requirements](https://docs.brew.sh/Installation).

**Terminal: macOS Terminal app, Bash or zsh, ordinary user, initial window.**

```bash
mac_preflight() {
  sw_vers || return
  MACOS_VERSION="$(sw_vers -productVersion)" || return
  [ "${MACOS_VERSION%%.*}" -ge 15 ] || { printf 'HOLD: this route requires macOS 15+.\n'; return 1; }
  ARCH="$(uname -m)" || return
  if [ "$(sysctl -in sysctl.proc_translated 2>/dev/null)" = 1 ]; then
    printf 'HOLD: Terminal is running through Rosetta; reopen it natively.\n'
    return 1
  fi
  case "$ARCH" in
    arm64) BREW=/opt/homebrew/bin/brew ;;
    x86_64) BREW=/usr/local/bin/brew ;;
    *) printf 'HOLD: unsupported architecture.\n'; return 1 ;;
  esac
  if [ -n "${ZSH_VERSION-}" ]; then
    SETUP_SHELL=zsh
  elif [ -n "${BASH_VERSION-}" ]; then
    SETUP_SHELL=bash
  else
    printf 'HOLD: use Bash or zsh.\n'; return 1
  fi
  printf 'ARCH %s; SHELL %s; BREW %s\n' "$ARCH" "$SETUP_SHELL" "$BREW"
  df -h "$HOME" || return
  [ -w "$HOME" ] || { printf 'HOLD: home directory is not writable.\n'; return 1; }
  printf 'PREFLIGHT OBSERVED\n'
}
mac_preflight
```

**Expected:** `sw_vers` shows macOS 15+, your architecture is `arm64` or native Intel `x86_64`, and your shell is Bash or zsh. Check the available-space column: at least 15 GB must remain. `PREFLIGHT OBSERVED` does not mean a device-policy exception has been approved.

**Stop:** The OS, architecture, shell, storage, or permissions do not meet those conditions.

**Recovery:** Keep the first failure and work with the device owner to resolve it. If Terminal is running through Rosetta, close Terminal, clear **Open using Rosetta** in Terminal's Finder **Get Info**, then reopen Terminal through the app before running this check again.

Run Python candidates until one meets the version requirement, continuing past older ones. Keep existing Git and Python if they work. Apple's Git stub may open a developer-tools dialog; cancel it if you lack permission, or complete the authorized tools step below.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same window.**

```bash
resolve_python() {
  for candidate in python3.12 python3 python; do
    "$candidate" -c 'import os, sys; sys.exit(1) if sys.version_info < (3, 12) else print(os.path.abspath(sys.executable))' 2>/dev/null && return 0
  done
  if [ -x "$BREW" ]; then
    PY_PREFIX="$("$BREW" --prefix python@3.12)" || return
    "$PY_PREFIX/bin/python3.12" -c 'import os, sys; sys.exit(1) if sys.version_info < (3, 12) else print(os.path.abspath(sys.executable))'
    return
  fi
  return 1
}
NEED_GIT=yes
if git --version; then NEED_GIT=no; fi
PY=
if PY="$(resolve_python)"; then
  "$PY" --version
else
  PY=
  printf 'MISSING: usable Python 3.12+.\n'
fi
printf 'Git installation needed: %s\n' "$NEED_GIT"
```

**Expected:** Git prints its version if usable; Python prints 3.12 or newer if usable. `PY` holds its absolute executable path.

**Stop:** An unexpected permission or policy prompt appears.

**Recovery:** Keep the error. Install only the missing prerequisite below; if both work, skip installation and go to the OMP download.

## Install missing Git or Python only when needed

Install Apple's Command Line Tools first if you use Intel Homebrew, need a source build, or Git/Homebrew says developer tools are missing. On Apple Silicon, skip both developer-tools blocks if none of these applies. If your tools already work, leave them in place. [Homebrew documents these requirements](https://docs.brew.sh/Installation).

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same window; approve Apple's GUI only if authorized.**

```bash
if xcode-select -p; then
  printf 'Developer tools path found.\n'
else
  xcode-select --install && printf 'Wait for the Apple installation dialog to finish before continuing.\n'
fi
```

**Expected:** You see an existing tools path or an Apple installation dialog. If the dialog opens, click **Install**, accept the license if authorized, and wait until installation finishes. A return to the prompt does not mean the download has finished.

**Stop:** Installation fails, authorization is unavailable, or the dialog is still running.

**Recovery:** Keep the error and ask the device owner to complete the permitted installation. Then confirm the tools are available.

Confirm the selected developer tools after the GUI finishes, or check the existing installation.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same window after the GUI finishes.**

```bash
xcode-select -p && xcrun --find clang
```

**Expected:** Both commands succeed and print developer-tool paths.

**Stop:** Either command fails.

**Recovery:** Keep the failure and have the device owner repair the selected tools installation before continuing.

After installing Apple tools, run the existing-prerequisites block again. If Git and Python now work, skip Homebrew and package installation. Install Homebrew only if a missing tool needs it and the native prefix has no `brew` executable. The official installer changes the system prefix: `/opt/homebrew` on Apple Silicon or `/usr/local` on Intel. Read its proposed changes and confirmation prompts. It may ask for an administrator password, which Terminal will not display. Stop if you cannot authorize the changes. Use the full [official installer](https://brew.sh/); never run `sudo brew install`.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same window; installer may request authorized administrator approval.**

```bash
ensure_brew() {
  if [ ! -x "$BREW" ]; then
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" || return
  fi
  [ -x "$BREW" ] || { printf 'HOLD: expected native Homebrew executable is absent.\n'; return 1; }
  BREW_ENV="$("$BREW" shellenv "$SETUP_SHELL")" || return
  eval "$BREW_ENV" || return
  "$BREW" --version
}
ensure_brew
```

**Expected:** The installer exits successfully and the expected native Homebrew executable prints its version. `shellenv` makes that installation available in this window.

**Stop:** The installer, `shellenv`, or version check fails, or policy prevents approval.

**Recovery:** Keep the first error and work with the device owner to resolve it. Do not install packages after the installer fails. Stay in this window until the step that tells you to reopen Terminal, because a fresh Terminal window will not inherit these shell variables.

Install only the tools you are missing, and check Git again after installing any Apple tools. Find a usable [versioned Python executable](https://formulae.brew.sh/formula/python@3.12) by running it; having the formula installed is not enough.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same window.**

```bash
install_missing_tools() {
  if ! git --version; then
    "$BREW" install git || return
  fi
  if ! PY="$(resolve_python)"; then
    "$BREW" install python@3.12 || return
    PY="$(resolve_python)" || return
  fi
  git --version || return
  "$PY" --version || return
  printf 'PREREQUISITES READY: %s\n' "$PY"
}
install_missing_tools
```

**Expected:** `PREREQUISITES READY` follows successful Git and Python 3.12+ execution.

**Stop:** Either installation or version check fails. Intel source builds may need additional owner support.

**Recovery:** Keep the first error and fix the tool that failed. Do not use `sudo` to install a formula or replace a tool that already meets the requirements.

## Download the exact OMP release into a new directory

Select the native macOS asset. Keep its checksum file beside it. The download block does not execute the downloaded program.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same window.**

```bash
RUN="$(date -u +%Y%m%dT%H%M%SZ)-$$"
DOWNLOAD="$HOME/course-evidence/setup-macos-$RUN/download"
DEST="$HOME/.local/bin/omp"
case "$(uname -m)" in
  arm64) ASSET=omp-darwin-arm64 ;;
  x86_64) ASSET=omp-darwin-x64 ;;
  *) ASSET= ;;
esac
if [ -n "$ASSET" ]; then
  "$PY" - "$DOWNLOAD" <<'PY'
from pathlib import Path
import sys
folder = Path(sys.argv[1])
if folder.is_symlink() or any(parent.is_symlink() for parent in folder.parents):
    raise SystemExit('HOLD: linked download path; preserve it and resolve the path.')
folder.mkdir(parents=True, exist_ok=False)
PY
  if [ "$?" -ne 0 ]; then
    false
  else
  curl --fail --location --output "$DOWNLOAD/$ASSET" "https://github.com/can1357/oh-my-pi/releases/download/v18.3.5/$ASSET" &&
  curl --fail --location --output "$DOWNLOAD/SHA256SUMS.txt" "https://github.com/can1357/oh-my-pi/releases/download/v18.3.5/SHA256SUMS.txt"
  fi
else
  printf 'HOLD: unsupported macOS architecture.\n' >&2
  false
fi
```

**Expected:** Both downloads succeed, and both files are in the new download directory. Finding the files there does not mean they have passed the checksum check.

**Stop:** Either download fails, the destination exists, or a certificate/proxy error appears.

**Recovery:** Keep the failed directory. Fix the network or path issue before choosing a new `RUN`. Never disable certificate checks or run a partial download.

## Verify before installation or first execution

This script checks the exact selected filename against its unique SHA-256 entry and installs only verified bytes. It refuses a symlink or anything different already at the destination, but it can reuse an identical verified file without replacing it.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same window.**

```bash
"$PY" - "$DOWNLOAD" "$ASSET" "$DEST" <<'PY'
from pathlib import Path
import hashlib, re, sys
folder, asset, target = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3])
entries = [line.split() for line in (folder / 'SHA256SUMS.txt').read_text().splitlines()]
expected = [parts[0] for parts in entries if len(parts) == 2 and parts[1] in (asset, '*' + asset)]
if len(expected) != 1 or not re.fullmatch(r'[0-9a-fA-F]{64}', expected[0]):
    raise SystemExit('HOLD: selected asset has no unique valid checksum entry.')
raw = (folder / asset).read_bytes()
actual = hashlib.sha256(raw).hexdigest()
if actual != expected[0].lower():
    raise SystemExit('HOLD: checksum mismatch; do not install or execute this file.')
if target.is_symlink() or (target.exists() and (not target.is_file() or hashlib.sha256(target.read_bytes()).hexdigest() != actual)):
    raise SystemExit('HOLD: a different destination exists; preserve it and resolve the installation conflict.')
if any(parent.is_symlink() for parent in target.parents):
    raise SystemExit('HOLD: destination parent is a symlink; preserve it and resolve the path.')
target.parent.mkdir(parents=True, exist_ok=True)
if not target.exists():
    with target.open('xb') as output:
        output.write(raw)
target.chmod(target.stat().st_mode | 0o100)
print('SHA256 VERIFIED', asset, actual)
print('USER EXECUTABLE', target)
PY
```

**Expected:** `SHA256 VERIFIED` names the selected asset and actual digest. Only then does the script make the verified executable runnable.

**Stop:** Any checksum, destination, write, or permission check fails.

**Recovery:** Keep the failure. Do not delete or replace another installation to make this script succeed. Resolve the conflict deliberately or ask for support.

## Keep the verified executable available in a new terminal

Save non-secret command paths for the shell you checked. `PATH` lists the directories your shell searches for commands. This step keeps what is already in your startup files, adds each missing line once, and handles a file with no final newline. It refuses linked files or linked parent directories. For [Bash](https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html), it uses the first existing login file in `.bash_profile`, `.bash_login`, `.profile` order, plus `.bashrc` for regular interactive shells. For [zsh](https://zsh.sourceforge.io/Doc/Release/Files.html), it uses `.zprofile` and `.zshrc` under `ZDOTDIR` or your home directory. Ask the owner to review any custom startup setup that skips these files.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same window.**

```bash
"$PY" - "$SETUP_SHELL" "$BREW" "${ZDOTDIR:-$HOME}" <<'PY'
from pathlib import Path
import shlex, sys
shell, brew_name, zdotdir = sys.argv[1:]
home = Path.home()
brew = Path(brew_name)
if shell == 'zsh':
    base = Path(zdotdir)
    if not base.is_absolute() or not base.is_dir():
        raise SystemExit('HOLD: inspect ZDOTDIR before editing startup files.')
    profiles = [base / '.zprofile', base / '.zshrc']
elif shell == 'bash':
    choices = [home / name for name in ('.bash_profile', '.bash_login', '.profile')]
    login = next((path for path in choices if path.exists() or path.is_symlink()), choices[0])
    profiles = [login, home / '.bashrc']
else:
    raise SystemExit('HOLD: use Bash or zsh.')
lines = []
if brew.is_file():
    lines.append(f'eval "$({shlex.quote(str(brew))} shellenv {shell})"')
python_bin = str(Path(sys.executable).absolute().parent)
lines.append(f'case ":$PATH:" in *:{shlex.quote(python_bin)}:*) ;; *) export PATH={shlex.quote(python_bin)}"${{PATH:+:$PATH}}" ;; esac')
lines.append('case "$PATH" in "$HOME/.local/bin"|"$HOME/.local/bin:"*) ;; *) export PATH="$HOME/.local/bin${PATH:+:$PATH}" ;; esac')
updates = []
for profile in profiles:
    if profile.is_symlink() or any(parent.is_symlink() for parent in profile.parents):
        raise SystemExit(f'HOLD: linked startup path; preserve {profile}')
    if profile.exists() and not profile.is_file():
        raise SystemExit(f'HOLD: startup path is not a file: {profile}')
    if Path(str(profile) + '.zwc').exists():
        raise SystemExit(f'HOLD: compiled zsh startup file needs owner review: {profile}')
    existing = profile.read_bytes() if profile.exists() else b''
    missing = [line.encode() for line in lines if line.encode() not in existing.splitlines()]
    updates.append((profile, existing, missing))
for profile, existing, missing in updates:
    if missing:
        with profile.open('ab') as stream:
            stream.write((b'\n' if existing and not existing.endswith(b'\n') else b'') + b'\n'.join(missing) + b'\n')
    print('PROFILE READY', profile)
PY
```

**Expected:** You see two `PROFILE READY` paths for the shell checked in preflight. Your existing file content stays in place; only non-secret Homebrew, Python, and user-bin paths are added.

**Stop:** A file is linked, compiled, unreadable, unwritable, or has startup errors.

**Recovery:** Keep the file and the error, and ask its owner to fix the startup problem shown. Do not replace profiles or create a higher-priority login file that would skip settings in `.profile`.

Check the verified executable directly before reopening.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same window.**

```bash
OMP_VERSION="$("$HOME/.local/bin/omp" --version)" &&
if [ "$OMP_VERSION" = omp/18.3.5 ]; then
  printf '%s\n%s\n' "$HOME/.local/bin/omp" "$OMP_VERSION"
else
  printf 'HOLD: unexpected OMP version: %s\n' "$OMP_VERSION" >&2
  false
fi
```

**Expected:** The absolute user executable prints exactly `omp/18.3.5`.

**Stop:** The version differs, execution fails, or macOS blocks it.

**Recovery:** Keep the error and follow authorized [Gatekeeper guidance](https://support.apple.com/en-us/102445) with the device owner. Do not disable Gatekeeper or strip quarantine attributes to bypass the block.

## Confirm private repository access

Check existing Git credentials before installing a login tool or changing a credential helper.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same window.**

```bash
GIT_TERMINAL_PROMPT=0 git ls-remote --exit-code https://github.com/TheHolofex/AIHB_OCT_2026.git HEAD
```

**Expected:** A commit ID followed by `HEAD`, with exit status zero. If this succeeds, skip the entire GitHub CLI fallback below and use the checkout step.

**Stop:** Authentication fails or you cannot read the repository. You need access to the repository; changing local-directory permissions will not fix this.

**Recovery:** Keep the error. If credentials are missing, use the GitHub fallback. If the network failed, fix that connection; if access is missing, ask the repository owner to confirm your invitation.

### GitHub CLI fallback — only after the access check fails

Install `gh` only if it is missing. If Homebrew is missing too, complete the authorized Homebrew and applicable Apple tools steps above first. If you skipped those steps because Git and Python already worked, preflight still set `BREW` and `SETUP_SHELL`. After installing Homebrew here, repeat the startup-path saving block so you can use it after reopening Terminal.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same window.**

```bash
if command -v gh >/dev/null 2>&1; then
  gh --version
elif [ -x "$BREW" ]; then
  BREW_ENV="$("$BREW" shellenv "$SETUP_SHELL")" &&
  eval "$BREW_ENV" &&
  "$BREW" install gh && gh --version
else
  printf 'HOLD: complete the authorized Homebrew installation first.\n' >&2
  false
fi
```

**Expected:** Existing `gh` prints its version, or Homebrew installs the official [GitHub CLI formula](https://formulae.brew.sh/formula/gh) successfully. The earlier Homebrew `shellenv` step must have succeeded in this window.

**Stop:** Installation fails or `gh` remains unavailable.

**Recovery:** Keep the error and correct the Homebrew prerequisite; never install the formula with `sudo`.

Sign in with the GitHub account invited to the private repository. The command displays a device code and opens a browser; enter the code at GitHub and authorize that account. GitHub credentials are separate from your course-site password and OpenRouter key. [GitHub CLI prefers the system credential store but may fall back to a plaintext file](https://cli.github.com/manual/gh_auth_login).

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same window; interactive browser login.**

```bash
gh auth login --hostname github.com --git-protocol https --web
```

**Expected:** The browser authorization and CLI login both finish successfully.

**Stop:** Login fails, the wrong account is selected, or policy forbids the requested storage.

**Recovery:** Keep the error privately and ask the device owner to provision approved credentials. Do not use `--insecure-storage`.

Check the account and reported credential storage before setting up Git. Keep the [authentication status](https://cli.github.com/manual/gh_auth_status) output private; do not add `--show-token` or share the output.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same window.**

```bash
gh auth status --hostname github.com
```

**Expected:** Exit zero, the invited account active, and storage approved by your device policy.

**Stop:** Status fails or the reported storage is not approved, including an unapproved plaintext fallback.

**Recovery:** Ask the device owner to set up approved credential storage and credentials before you continue. Signing in does not by itself give you access to the repository.

Configure the credential helper for [github.com only](https://cli.github.com/manual/gh_auth_setup-git), then repeat the access check with terminal prompting disabled.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same window.**

```bash
gh auth setup-git --hostname github.com &&
GIT_TERMINAL_PROMPT=0 git ls-remote --exit-code https://github.com/TheHolofex/AIHB_OCT_2026.git HEAD
```

**Expected:** The helper succeeds, followed by the repository commit ID and `HEAD`.

**Stop:** Either command fails. Do not clone yet.

**Recovery:** Keep the error and ask the repository owner to confirm your invited account and any required approval. Do not force helper setup or retry login without finding the cause.

## Use the intended checkout without replacing existing work

Use one checkout location that you can keep using. Even if you have related work, do not reset, pull, or clean it.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same window.**

```bash
R="$HOME/Documents/AIHB_OCT_2026"
"$PY" - "$R" <<'PY'
from pathlib import Path
import sys
root = Path(sys.argv[1])
if root.is_symlink() or any(parent.is_symlink() for parent in root.parents):
    raise SystemExit('HOLD: linked checkout path; preserve it and resolve the path.')
PY
if [ "$?" -ne 0 ]; then
  false
elif [ ! -e "$R" ] && [ ! -L "$R" ]; then
  git clone https://github.com/TheHolofex/AIHB_OCT_2026.git "$R"
elif [ -d "$R/.git" ] && [ ! -L "$R/.git" ] &&
  git -C "$R" rev-parse --verify HEAD >/dev/null 2>&1 &&
  [ "$(git -C "$R" rev-parse --show-toplevel)" = "$R" ] &&
  [ "$(git -C "$R" remote get-url origin)" = https://github.com/TheHolofex/AIHB_OCT_2026.git ]; then
  printf 'Using the existing course checkout without changing it.\n'
else
  printf 'HOLD: the checkout path is occupied by unrelated or incomplete work.\n' >&2
  false
fi &&
M="$R/AI_Harness_Bootcamp_2/module-00-setup" &&
[ -f "$R/shared/run_omp.py" ] &&
[ -f "$M/shared/case/verify_tool_proof.py" ] &&
[ -f "$M/scripts/verify-setup.sh" ] &&
printf 'CHECKOUT READY %s\n' "$R"
```

**Expected:** `CHECKOUT READY` names the intended checkout at `R`, with the required launcher and Module 0 files under `M`.

**Stop:** Cloning fails or the existing path is unrelated/incomplete.

**Recovery:** Keep that directory and ask the owner to resolve the path conflict. Do not hide a clone failure with `|| true` or discard local changes.

## Reopen independently and check actual tools

In the Terminal app, open **Terminal → Shell → New Window** with the same Bash or zsh profile. Do not start a child shell at the old prompt. Set `R`, `M`, and `PY` again because the new window does not inherit your earlier shell variables. This check does not fix PATH or enter a key.

**Terminal: macOS Terminal app, same declared Bash or zsh, ordinary user, independently opened window.**

```bash
fresh_tools() {
  R="$HOME/Documents/AIHB_OCT_2026"
  M="$R/AI_Harness_Bootcamp_2/module-00-setup"
  case "$(uname -m)" in
    arm64) BREW=/opt/homebrew/bin/brew ;;
    x86_64) BREW=/usr/local/bin/brew ;;
    *) printf 'HOLD: unsupported architecture.\n'; return 1 ;;
  esac
  PY=
  for candidate in python3.12 python3 python; do
    if PY="$("$candidate" -c 'import os, sys; sys.exit(1) if sys.version_info < (3, 12) else print(os.path.abspath(sys.executable))' 2>/dev/null)"; then
      break
    fi
    PY=
  done
  if [ -z "$PY" ] && [ -x "$BREW" ]; then
    PY_PREFIX="$("$BREW" --prefix python@3.12)" || return
    PY="$("$PY_PREFIX/bin/python3.12" -c 'import os, sys; sys.exit(1) if sys.version_info < (3, 12) else print(os.path.abspath(sys.executable))')" || return
  fi
  [ -n "$PY" ] || { printf 'HOLD: Python 3.12+ is unavailable.\n'; return 1; }
  command -v git || return
  git --version || return
  printf 'PYTHON %s\n' "$PY"
  "$PY" -c 'import sys; print(sys.version); sys.exit(0 if sys.version_info >= (3, 12) else 1)' || return
  [ "$(command -v omp)" = "$HOME/.local/bin/omp" ] || { printf 'HOLD: OMP PATH differs.\n'; return 1; }
  OMP_VERSION="$("$HOME/.local/bin/omp" --version)" || return
  [ "$OMP_VERSION" = omp/18.3.5 ] || { printf 'HOLD: OMP version differs: %s\n' "$OMP_VERSION"; return 1; }
  printf 'OMP %s %s\n' "$HOME/.local/bin/omp" "$OMP_VERSION"
  [ -f "$R/shared/run_omp.py" ] && [ -f "$M/shared/case/verify_tool_proof.py" ] || return
  if [ -n "${OPENROUTER_API_KEY:-}" ]; then printf 'SET\n'; else printf 'MISSING\n'; fi
  printf 'FRESH TOOLS READY\n'
}
fresh_tools
```

**Expected:** You see the Git path and version, an absolute Python path with version 3.12+, and `$HOME/.local/bin/omp` with exactly `omp/18.3.5`, followed by `FRESH TOOLS READY`. An installed formula may not put its executable on PATH; Python is chosen only after it runs successfully. The prerequisite report below also checks whether commands can be found by name.

**Stop:** Any tool fails, the OMP path/version changes, or the checkout files are absent.

**Recovery:** Keep the failed check, fix the non-secret startup setting that caused it in the earlier window, then open another Terminal window from the app, not from a shell in the earlier window. Do not add an export to this check to make it pass.

Check whether the key is set before entering it. A Terminal window opened from the app normally reports `MISSING`, but a shell started from a window that already has the key can inherit `SET`. Seeing `SET` doesn't tell you whether the key persists, has been exposed, or works for authentication. If `SET` surprises you, stop and check how you opened this window and whether credentials were configured earlier, without printing the key. Do not save a key in startup files. You can enter it for the first time now; you didn't need to enter it earlier.

## Enter the key only after the hidden prompt is ready

Use your participant-supplied OpenRouter key. The supplied `shared/run_omp.py` uses only `openrouter/anthropic/claude-sonnet-4.6`. Do not use a vendor login or another model. Paste this one command, press Enter, then enter the key without echo and press Enter again.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same window.**

```bash
IFS= read -r -s OPENROUTER_API_KEY
```

**Expected:** The prompt returns without displaying the key.

**Stop:** The key appears, focus is uncertain, or hidden entry is inaccessible.

**Recovery:** Cancel and use the [credential handling procedure](../shared/CREDENTIALS.md). Revoke any exposed key. Do not paste the next block while the hidden read is waiting.

Export the value only after the hidden prompt has returned, and check presence without printing it.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same fresh window.**

```bash
export OPENROUTER_API_KEY
if [ -n "${OPENROUTER_API_KEY:-}" ]; then printf 'SET\n'; else printf 'MISSING\n'; fi
```

**Expected:** Only `SET` is printed. This check shows the key is present, not whether authentication or a model call works.

**Stop:** The variable is missing or a secret value appears in output.

**Recovery:** Re-enter it through the isolated hidden prompt. Never save the key in a profile, command argument, or evidence file.

## Run a readiness check

Create a fresh readiness-check attempt. The random token marks this attempt; it is not a credential. The prompt gets the token only from a file inside the work root you set.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same window.**

```bash
PROOF_RUN="$HOME/course-evidence/setup-proof-$(date -u +%Y%m%dT%H%M%SZ)-$$"
W="$PROOF_RUN/proof"
E="$PROOF_RUN/receipts"
TOKEN="$PROOF_RUN/run-token.txt"
"$PY" - "$PROOF_RUN" <<'PY'
from pathlib import Path
import secrets, sys
run = Path(sys.argv[1])
if run.is_symlink() or any(parent.is_symlink() for parent in run.parents):
    raise SystemExit('HOLD: linked readiness-check path; preserve it and resolve the path.')
run.mkdir(parents=True, exist_ok=False)
work = run / 'proof'
work.mkdir()
token = secrets.token_hex(16)
(run / 'run-token.txt').write_text(token + '\n', encoding='utf-8')
(work / 'run-token.txt').write_text(token + '\n', encoding='utf-8')
(run / 'prompt.txt').write_text('Read run-token.txt with course_read. Use course_write to create from-omp.txt containing only omp works followed by one space and the exact token. Do not write another file.\n', encoding='utf-8')
print('FRESH READINESS WORK', work)
PY
```

**Expected:** `FRESH READINESS WORK` names the new work folder. Its token and prompt exist. `E` does not exist yet.

**Stop:** The attempt already exists or preparation fails.

**Recovery:** Keep the failed attempt. Fix the reported path or permission problem before creating a new `PROOF_RUN`, and never reuse an old result file as a new result.

Run the paid readiness check only after the checks in the new terminal window and the credential checks pass. The launcher writes receipts in the new evidence directory.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same window.**

```bash
"$PY" "$R/shared/run_omp.py" --workdir "$W" --prompt "$PROOF_RUN/prompt.txt" --evidence "$E" --allow-write from-omp.txt &&
"$PY" "$M/shared/case/verify_tool_proof.py" "$W" "$TOKEN" "$E"
```

**Expected:** A completed paid turn shows the pinned identities, a successful `course_write`, the exact required file contents on disk, and `READINESS CHECK PASS`. The verifier also checks the receipts, so the assistant saying it worked or a file you made by hand is not enough.

**Stop:** If the key is missing, the launcher exits with status 2 before contacting the provider. An incomplete turn or a failed readiness check remains on hold. A file left behind by a failed child does not mean the check passed.

**Recovery:** Keep all output and receipts. Fix the missing prerequisite before creating a fresh readiness-check attempt. Do not switch providers, turn on automatic retries, or reuse a partly written output.

Read the actual output file from disk in a separate command and compare it with this attempt's token.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same fresh window.**

```bash
"$PY" - "$W/from-omp.txt" "$TOKEN" <<'PY'
from pathlib import Path
import sys
output, token_file = map(Path, sys.argv[1:])
if output.is_symlink() or not output.is_file():
    raise SystemExit('HOLD: readiness-check output is missing or linked.')
raw = output.read_bytes()
token = token_file.read_text(encoding='utf-8').strip()
expected = ('omp works ' + token).encode('utf-8')
if raw not in (expected, expected + b'\n'):
    raise SystemExit('HOLD: actual disk bytes differ from this attempt token.')
print('DISK FILE', output.resolve())
print(raw.decode('utf-8'), end='' if raw.endswith(b'\n') else '\n')
print('DISK READBACK PASS')
PY
```

**Expected:** You see the absolute path of the file, `omp works` followed by this attempt's token, and `DISK READBACK PASS`. Along with `READINESS CHECK PASS`, the receipts link that file to the completed pinned turn.

**Stop:** Reading the file from disk, the prerequisite report, or the readiness check fails. Finding a file alone does not mean the readiness check was completed.

**Recovery:** Keep the attempt and receipts as `HOLD`. Fix the failed prerequisite before creating a new attempt; do not write the result file yourself, reuse evidence, change providers, or turn on retries. If you cannot use an operation on your device or cannot access it, record that limit and leave the readiness check incomplete.

## Save the prerequisite report separately

Save what you saw in the prerequisite checks in a separate report. That report checks your tools and whether configuration is present; it does not replace the live readiness check or reading the file from disk.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same window.**

```bash
bash "$M/scripts/verify-setup.sh" "$R" "$PROOF_RUN/setup-report.txt"
```

**Expected:** The command exits with status zero and shows `SETUP CHECK PASS` with what it found. A dirty checkout is information, not a request to discard your work. Key or prerequisite failures still show `SETUP CHECK HOLD`.

**Stop:** A required check fails or the report destination already exists.

**Recovery:** Follow the action given for the failure and keep the report. After fixing the problem, use a new report filename. Keep a failed model call, missing prerequisites, and unavailable native or accessible operations as separate limits in your evidence.

## Set up local Obsidian

Obsidian lets you edit and link local notes for Module 2. Plan for roughly 10 to 20 minutes for a fresh installation, plus download time. Keep any existing installation, profile, and vaults. In Finder, check **Applications** and your home folder's **Applications**, and see whether you already open Obsidian from another location. If it is installed, use that copy and skip the download and install blocks. Record the version it shows when you do the Obsidian check below; don't replace it only to match 1.13.7.

### Install the verified universal DMG only if Obsidian is absent

If Obsidian is not installed, use the official universal **1.13.7** DMG for Apple Silicon and Intel. This block downloads it to a new folder outside the checkout, checks its approved SHA-256, and opens the disk image only if the hash matches. It uses `PY` from the earlier Python step. See the [official installation instructions](https://github.com/obsidianmd/obsidian-help/blob/master/en/Getting%20started/Download%20and%20install%20Obsidian.md) and [release assets](https://github.com/obsidianmd/obsidian-releases/releases/tag/v1.13.7).

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same window; no sudo. Run only if no existing installation was found.**

```bash
course_download_obsidian() {
  [ -n "${PY:-}" ] || { printf 'HOLD: restore PY first.\n'; return 1; }
  for app in /Applications/Obsidian.app "$HOME/Applications/Obsidian.app"; do
    if [ -e "$app" ] || [ -L "$app" ]; then
      printf 'HOLD: preserve and use existing %s\n' "$app"; return 1
    fi
  done
  OBS_DOWNLOAD="$HOME/course-evidence/obsidian-download-$(date -u +%Y%m%dT%H%M%SZ)-$$"
  "$PY" - "$OBS_DOWNLOAD" <<'PYOBS'
from pathlib import Path
import sys
folder = Path(sys.argv[1])
if folder.is_symlink() or any(p.is_symlink() for p in folder.parents):
    raise SystemExit('HOLD: linked download path; preserve it.')
folder.mkdir(parents=True, exist_ok=False)
PYOBS
  [ "$?" -eq 0 ] || return 1
  curl --fail --location --output "$OBS_DOWNLOAD/Obsidian-1.13.7.dmg" 'https://github.com/obsidianmd/obsidian-releases/releases/download/v1.13.7/Obsidian-1.13.7.dmg' || return 1
  "$PY" - "$OBS_DOWNLOAD/Obsidian-1.13.7.dmg" <<'PYOBS'
from pathlib import Path
import hashlib, sys
asset = Path(sys.argv[1])
expected = '05daa54f5e1a4458f75da29f8faaa17e8e37ae16998432537f674c626db99bce'
if asset.is_symlink() or hashlib.sha256(asset.read_bytes()).hexdigest() != expected:
    raise SystemExit('HOLD: DMG checksum mismatch; do not open or install it.')
print('SHA256 VERIFIED', asset.name, expected)
PYOBS
  [ "$?" -eq 0 ] || return 1
  open "$OBS_DOWNLOAD/Obsidian-1.13.7.dmg"
}
course_download_obsidian
```

**Expected:** `SHA256 VERIFIED` prints the exact DMG digest, then Finder opens the disk image.

**Stop:** the download, hash check, or disk-image opening fails; an app already exists; or device policy refuses installation.

**Recovery:** Keep the failed download. Fix the network or path problem, then use a new download folder. Never bypass a hash mismatch, Gatekeeper, or certificate checks. If an app exists elsewhere, use it instead.

**Window: Finder, verified Obsidian disk image.** Drag **Obsidian** to **Applications** only when that destination is absent and installation is authorized. If Finder asks to replace or merge an existing app, cancel. If administrator approval is required, proceed only with the device owner’s approval. Eject the disk image when copying finishes. Open the installed **Obsidian** from Finder’s Applications folder; for an existing installation, open its known location.

**Expected:** The installed app opens. **Stop:** Copying is refused, or a permission or security setting blocks it. **Recovery:** Keep the existing app and profile, and ask the device owner to resolve the specific refusal. Do not strip quarantine or disable Gatekeeper.

### Open a fresh practice vault and follow its links

Use Obsidian to follow a note link, save an edit, and see a change made outside the app. Allow roughly 10 to 15 minutes. A **vault** is a local folder of notes. Use only the fresh practice folder, and leave existing vaults and app profiles intact. You don't need an account, community plugin, Sync service, or MCP connection. This work makes no provider call and needs no API key.

Stay in the terminal window used above, with `PY` set to the checked Python executable, `R` to your course checkout, and `M` to `$R/AI_Harness_Bootcamp_2/module-00-setup`. The new `OBS_ROOT` sits outside both the OMP attempt and the checkout. Run one box at a time and stop if any box fails.

**Terminal: macOS Terminal, Bash or Zsh, ordinary user, same window; no sudo.**

```bash
course_initialize_obsidian() {
  [ -n "${PY:-}" ] && [ -n "${R:-}" ] && [ -n "${M:-}" ] || {
    printf 'HOLD: restore this page’s Python and checkout variables first.\n' >&2; return 1;
  }
  [ "$M" = "$R/AI_Harness_Bootcamp_2/module-00-setup" ] || return 1
  [ -f "$M/scripts/obsidian_readiness.py" ] && [ ! -L "$M/scripts/obsidian_readiness.py" ] || {
    printf 'HOLD: course readiness helper is missing or linked.\n' >&2; return 1;
  }
  OBS_ROOT="$HOME/course-evidence/obsidian-macos-$(date -u +%Y%m%dT%H%M%SZ)-$$"
  "$PY" "$M/scripts/obsidian_readiness.py" initialize --root "$OBS_ROOT" || return 1
  printf 'OPEN EXACT VAULT: %s\n' "$OBS_ROOT/vault"
}
course_initialize_obsidian
```

**Expected:** `Created practice vault:` and `OPEN EXACT VAULT:` name the same absolute folder ending in `/vault`. Keep that path visible.

**Stop:** Any HOLD or error, an existing destination, or a missing variable.

**Recovery:** Keep the attempt. If you closed the terminal, restore `PY`, `R`, and `M` using the earlier Python and checkout instructions. If initialization succeeded, set `OBS_ROOT` to the parent path that was printed and continue with that vault; don't initialize it again. If initialization failed, correct the named problem and use a fresh attempt. If a helper is missing, ask the checkout owner to resolve it; don't reset or update their checkout.

**Window: Obsidian, ordinary desktop account.**

1. Open Obsidian using the platform launch step above. If another vault opens, leave its files and settings alone. Open the vault switcher, choose **Manage vaults**, then **Open folder as vault → Open**. On a first launch, choose **Open folder as vault → Open** directly.
2. Select exactly the printed `OBS_ROOT/vault` folder. Press **Cmd+Shift+G** in the folder picker and paste the printed absolute path, then open that folder. Do not select the checkout, the parent `OBS_ROOT`, or an existing personal vault.
3. In this practice vault, open **Settings → Community plugins** and leave **Restricted mode** on. If it is off, turn it on for this vault. Under **Settings → Core plugins**, turn **Sync** off if it is on. Do not sign in or install a plugin. Open **Settings → General**, note the actual app version, then close Settings.
4. Open `Start` from the file list. Use Cmd+E to switch to Reading view if needed, then click its **Token** link. Read the token displayed in `Token`; this random text is an exercise identifier, not a credential.
5. Click **Reply** in `Token`. Switch to editing view with Cmd+E if needed. Paste only the token on one line, without a heading, quotation marks, or backticks. Press Cmd+S to save. Obsidian also saves edits automatically; the next command checks the actual saved bytes.

**Expected:** The links open the existing `Token` and `Reply` notes, and `Reply` shows the token you read in the app.

**Stop:** The wrong vault opens, a link creates an empty note, settings cannot remain local and restricted, or you cannot edit/save through the GUI.

**Recovery:** Leave `Start` and `Token` unchanged. Reopen the vault at the printed path and follow its existing links. If a policy or display failure stops you from using the Obsidian window, record `Obsidian HOLD` with the error. Editing in a text editor doesn't replace seeing and editing the note in Obsidian.

**Terminal: macOS Terminal, Bash or Zsh, ordinary user, same window; no sudo.**

```bash
"$PY" "$M/scripts/obsidian_readiness.py" check --root "$OBS_ROOT"
```

**Expected:** `Token generation 1: initial token; external refresh not yet exercised`, followed by `PASS: Obsidian file round-trip; GUI observation still required`. The command prints the path to the saved record of what it read from disk.

**Stop:** HOLD or any nonzero exit. A PASS here covers only the initial saved token.

**Recovery:** Read the named failure. If the reply doesn't match, return to `Token` in Obsidian, copy its current token into `Reply`, save, and run this check again. Keep all the records from each check. Don't edit the helper's `expected` records or fix a reply through the shell.

### Observe an external change, save, and reopen

Keep the practice vault open with `Token` visible. This command changes that note from the terminal while leaving the old reply in place.

**Terminal: macOS Terminal, Bash or Zsh, ordinary user, same window; no sudo.**

```bash
"$PY" "$M/scripts/obsidian_readiness.py" refresh --root "$OBS_ROOT"
```

**Expected:** `Source token rotated outside Obsidian; your saved reply was preserved.`

**Stop:** Any HOLD or error. Do not continue using an old token after a failed refresh.

**Recovery:** Keep the attempt and the exact error. Work with support to fix the named file or permission problem. If the refresh was interrupted, use a fresh attempt; don't edit expected values or remove a lock to force a pass.

**Window: Obsidian, same practice vault.**

1. Return to `Token` in the app, which is still open, and look for its new text. If needed, select `Start` and follow **Token** again. Confirm that the token differs from the one still saved in `Reply`.
2. Follow **Reply**, replace the old line with the new token you just saw, and press Cmd+S. Do not run refresh again.
3. Close the practice vault’s window with its window-close control; leave unrelated vault windows open. Launch Obsidian again using the same platform launch step. If it restores the practice vault, confirm its folder is the exact printed `OBS_ROOT/vault`. Otherwise use the vault switcher’s **Manage vaults → Open folder as vault → Open** to select that exact folder again.
4. Open `Start`, follow **Token**, then **Reply**. Confirm that the new token is still saved after reopening.

**Expected:** You see the external change, save the new reply in Obsidian, and see that reply again after reopening the same folder.

**Stop:** The app doesn't show the changed token, the edit disappears, or you can't tell which vault reopened.

**Recovery:** Record `Obsidian HOLD` and the action that failed in the Obsidian window. Keep the files and the records from each check; a match found only in the shell doesn't show that the app worked. Check the exact folder and display/session permissions with support before trying that action again.

**Terminal: macOS Terminal, Bash or Zsh, ordinary user, same window; no sudo.**

```bash
"$PY" "$M/scripts/obsidian_readiness.py" check --root "$OBS_ROOT"
```

**Expected:** `Token generation 2: refreshed token; GUI observation still required` and `PASS: Obsidian file round-trip; GUI observation still required`, plus a new path to the saved record of what the command read from disk. If you refreshed more than once on purpose, the generation is higher; record the value you see.

**Stop:** HOLD, a token that has not been refreshed, or a GUI action you could not see in the Obsidian window.

**Recovery:** Keep the attempt. If the saved reply does not match, correct it in Obsidian, save it, close and reopen that vault, then check again. Obsidian stays on HOLD if you could not see the GUI actions, even when the files on disk match.

### Record actual Obsidian readiness

Use an ordinary text editor to create `gui-observation.txt` beside the vault at the `OBS_ROOT` path you used. Record the date, operating system and architecture, app version, exact vault path, and the two disk-record paths the checks printed. Describe how you followed the links, made and saved the first edit, saw the token change made outside Obsidian, made and saved the second edit, then closed and reopened the vault. Record that Restricted mode was on and Sync was off. You may include a screenshot of the practice vault, but leave out credentials and unrelated personal notes.

Write `Obsidian READY` only if both disk checks passed and you saw every listed GUI action in the Obsidian window. Otherwise write `Obsidian HOLD` and name the missing action or exact error. A file or `.obsidian` folder alone cannot show that you used the app. Keep this record separate from OMP and n8n readiness; a failure in one does not cancel a result in another. These Obsidian GUI actions were checked only with Obsidian 1.13.7 on Darwin arm64. If you use Intel, perform the actions and record what happens on your machine.

## Prepare local n8n for Module 7

You'll use a local workflow editor and check whether a saved workflow survives a stop and start. Allow extra time for downloads and startup; the setup estimate above is rough, not measured. Finish this n8n readiness check before Module 7, and keep its result separate from both the OMP prerequisite report and the live OMP readiness check above.

### Inspect Docker and preserve existing work

A Docker **context** tells Docker which engine receives your commands. Before you install or launch anything, check the selected context, containers (including stopped ones), volumes, destination, and port. Keep the output private if it shows names or addresses from other work. Don't switch contexts, clear Docker environment variables, or stop an existing application to make room.

**Terminal: macOS Terminal, Bash or zsh, ordinary user.**

```bash
if [ -d /Applications/Docker.app ]; then
  printf 'Docker Desktop is already installed.\n'
fi
if command -v docker >/dev/null 2>&1; then
  command -v docker
  docker context show
  docker context ls
  docker info
  docker compose version
  docker ps -a
  docker volume ls
else
  printf 'Docker CLI is not on PATH; inspect installed applications before installing.\n'
fi
if [ -n "${DOCKER_HOST:-}${DOCKER_CONTEXT:-}" ]; then
  printf 'HOLD: Docker environment overrides exist; have their owner inspect the destination.\n'
fi
if [ -e "$HOME/n8n-course" ] || [ -L "$HOME/n8n-course" ]; then
  printf 'HOLD: preserve the existing n8n-course destination.\n'
else
  printf 'Proposed fresh destination: %s/n8n-course\n' "$HOME"
fi
lsof -nP -iTCP:5678 -sTCP:LISTEN
```

**Expected:** You can identify the engine and its existing work, or tell that Docker is missing. If `lsof` shows no listener (normally exit 1), none was found; a permission error does not mean the port is free. The destination is `$HOME/n8n-course`, outside the checkout.

**Stop:** A Docker command fails, the selected engine is remote or unfamiliar, environment overrides exist, port 5678 is occupied, or the destination already exists—even if it is empty or an earlier incomplete attempt.

**Recovery:** Ask the device/work owner to resolve the specific condition, and keep every application, container, volume, directory, and failed attempt. If Docker is installed but stopped, review with the owner how starting it will affect existing work before you launch it. Starting Docker Desktop can select `desktop-linux`, so record the previous context and have the owner keep its intended routing. Reuse an approved existing course instance only after you check its version and configuration below; skip both installer alternatives and the fresh-file edit. If the installation is elsewhere, have the owner review its Compose path before you use any lifecycle command. Never silently migrate, repin, reset, uninstall, or upgrade it.

### Install Docker Desktop only if it is missing and approved

Use **Apple menu → About This Mac** to check the macOS release, memory, and **Chip** (Apple Silicon) or **Processor** (Intel). Docker requires at least **4 GB RAM** and supports the current and two preceding major macOS releases; check the current [Mac requirements and downloads](https://docs.docker.com/desktop/setup/install/mac-install/) against your machine. That is Docker's minimum, not a guarantee that this stack plus your other applications fits available memory. The earlier macOS 15+ Homebrew gate does not replace this check. [Intel Homebrew Tier 3](https://docs.brew.sh/Support-Tiers) describes Homebrew support, not Docker's separate Intel support policy.

Have the device owner approve installation, resource use, and the Docker Desktop subscription terms. Education and personal use can qualify for free use; larger commercial organizations and government entities may require a paid subscription. Use the terms on Docker's installation page to determine eligibility before accepting.

1. On that official page, select **Docker Desktop for Mac with Apple silicon** for an Apple chip, or **Docker Desktop for Mac with Intel chip** for an Intel processor. Do not choose based on a Rosetta-translated shell. Rosetta is not strictly required by Docker Desktop; optional tools may need it. Keep the course Terminal native.
2. After saving any open work, close tools that call Docker as the installation page directs. Double-click the downloaded **Docker.dmg**, then drag **Docker** into **Applications**. Keep the installer volume mounted until copying completes. Do not replace an existing Docker.app without owner review.
3. In **Applications**, double-click **Docker.app**. Select **Accept** for the subscription agreement only with owner approval. Follow approved macOS security prompts; do not bypass device controls.
4. Follow the [Docker CLI location options](https://docs.docker.com/desktop/setup/install/mac-permission-requirements/). Current releases default to `$HOME/.docker/bin` and add it to PATH. **Settings → Advanced** allows user or system CLI locations; the system location is `/usr/local/bin` and may require administrator authorization. Releases 4.88.0 and earlier offer **Use recommended settings** or **Use advanced settings** during installation, followed by **Finish**. Choose the owner-approved option. Port 5678 does not require privileged low-port mapping or a default socket symlink.
5. Leave Docker open and wait until its engine is running. A visible application window alone is not readiness. The terminal check below must succeed.

If `docker` is missing in a new terminal, check the chosen CLI location. For the user option, use your normal text editor to add `export PATH="$HOME/.docker/bin:$PATH"` only where needed: for zsh, the applicable `.zprofile` and `.zshrc` under `ZDOTDIR` or home; for Bash, the first existing login file in `.bash_profile`, `.bash_login`, `.profile` order and `.bashrc`. Keep their existing contents and the earlier OMP/Python/Homebrew lines. Have the owner review startup files that are linked, compiled, or managed. Don't create a higher-priority Bash file that hides an existing login file. For system CLI tools, check that `/usr/local/bin` is on PATH without replacing existing PATH entries.

Open **Terminal → Shell → New Window** through the app, using the intended Bash or zsh profile. Keep the earlier OMP window and its variables; use the new terminal window for all remaining n8n commands. Don't fix PATH inside this check.

**Terminal: macOS Terminal app, Bash or zsh, ordinary user, independently opened window.**

```bash
command -v docker &&
docker context show &&
docker context ls &&
docker info &&
docker compose version &&
docker ps -a &&
docker volume ls
```

**Expected:** Docker is found at the approved CLI location, the approved local engine answers `docker info`, and the Compose plugin runs as `docker compose`. A newer plugin may report version 5, so don't insist on a literal `2.x` version or use legacy `docker-compose` instead. Compare the context and existing work with what you saw earlier.

**Stop:** A command fails, the engine/context differs unexpectedly, or startup changed access to existing work.

**Recovery:** Work with the owner to fix the specific PATH, engine, or context issue. Then open another new terminal window and repeat the check. Don't reinstall Docker, reset its data, or run commands against an unapproved engine.

### Generate a fresh course stack without starting it

The [official one-line setup](https://docs.n8n.io/deploy/host-n8n/install-options/one-line-setup) uses Docker Compose. The [installer source](https://github.com/n8n-io/n8n/blob/master/docker/get-n8n.sh) reviewed here reports installer **1.4.0**, and the command below requests n8n **2.41.5**. The live download can change, so use the download-and-review alternative if you need to see precisely what will run.

Before you use either route, have the owner approve the full [official stack](https://github.com/n8n-io/n8n/blob/master/docker/get-n8n-compose.yml): `n8n`, `runners`, `sandbox-certs`, `sandbox-api`, `sandbox-runner-1`, and `searxng`. `sandbox-runner-1` runs privileged Docker-in-Docker inside Docker's Linux environment. Its supporting services run even when n8n Assistant is off. If that privilege is not allowed, hold here. Having amd64/arm64 images does not show that they run natively on your Mac; only seeing the stack work on your Mac shows that it's ready.

Check the destination and port again immediately before installing. Choose **one** route below. Both refuse to reuse `$HOME/n8n-course`, and neither should run with `sudo`. Don't set installer source overrides. The `--no-start` option lets you restrict the browser port before any service starts.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, new Docker-verified window.**

```bash
(
  set -o pipefail
  if [ -e "$HOME/n8n-course" ] || [ -L "$HOME/n8n-course" ]; then
    printf 'HOLD: destination exists; preserve it.\n' >&2
    exit 1
  fi
  curl -fsSL https://get.n8n.io | N8N_DIR="$HOME/n8n-course" sh -s -- --version 2.41.5 --no-start
)
```

**Expected:** The command exits with zero and creates `compose.yml`, `.env`, and `searxng-settings.yml` under `$HOME/n8n-course` without starting services. `pipefail` catches a failed download, but piping may run some bytes before the download finishes. Use the alternative below to avoid that risk.

**Stop:** any failure, an unexpected installer version, or an “existing install” message. That message does not confirm the requested version or readiness.

**Recovery:** Keep the partial directory and output. Work with the owner to fix the failure before a fresh attempt; don't rerun into or delete that directory.

Alternatively, download the installer into a new temporary directory. The `&&` chain stops an unsuccessful or empty download from becoming the script you review.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same Docker-verified window; alternative to the pipeline.**

```bash
N8N_REVIEW_DIR="$(mktemp -d "${TMPDIR:-/tmp}/n8n-review.XXXXXX")" &&
curl -fsSL https://get.n8n.io -o "$N8N_REVIEW_DIR/get-n8n.sh.part" &&
[ -s "$N8N_REVIEW_DIR/get-n8n.sh.part" ] &&
mv "$N8N_REVIEW_DIR/get-n8n.sh.part" "$N8N_REVIEW_DIR/get-n8n.sh" &&
printf 'Review this script in your editor: %s/get-n8n.sh\n' "$N8N_REVIEW_DIR"
```

**Expected:** The full download is saved as `get-n8n.sh`, but no script has run. Use **File → Open** in your normal text editor to open the printed path. Review the script with the owner, including `SCRIPT_VERSION="1.4.0"`, its source URLs, and what it will do during installation.

**Stop:** Download failure, a remaining `.part` file, unexpected version, or unapproved actions.

**Recovery:** Keep the failed download and fix the problem. Never run the `.part` file. For a later successful download, use a new temporary directory and review the new file.

After review and approval, run the downloaded file.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same window as the alternative download.**

```bash
if [ -e "$HOME/n8n-course" ] || [ -L "$HOME/n8n-course" ]; then
  printf 'HOLD: destination exists; preserve it.\n' >&2
  false
elif [ -n "${N8N_REVIEW_DIR:-}" ] && [ -s "$N8N_REVIEW_DIR/get-n8n.sh" ]; then
  N8N_DIR="$HOME/n8n-course" sh "$N8N_REVIEW_DIR/get-n8n.sh" --version 2.41.5 --no-start
else
  printf 'HOLD: complete and review the download first.\n' >&2
  false
fi
```

**Expected:** The same three configuration files are generated without starting services.

**Stop:** Any failure or existing-install message.

**Recovery:** Keep all files and ask the owner to resolve the specific failure. Don't upgrade or overwrite this attempt.

### Restrict access, start, and inspect

For a fresh install, use **File → Open** in your normal text editor to open `$HOME/n8n-course/compose.yml` (replace `$HOME` with your home-folder path in the file dialog). Under the `n8n` service's `ports`, change only `'5678:5678'` to `'127.0.0.1:5678:5678'`. Keep the indentation and quotes, then use **File → Save**. Leave all other services, settings, and volumes unchanged. Don't open or display `.env`, paste it into evidence, or run unfiltered `docker compose config`, which can reveal resolved secrets.

**Expected:** The saved file binds n8n only to this Mac's loopback address. No other service publishes a host port.

**Stop:** The expected line is absent, the file differs from the reviewed stack, or this is an existing installation whose settings have not been approved.

**Recovery:** Keep the file and have the owner review it before starting. Do not replace the whole file with a downloaded template.

### Record the fresh project name

A Compose project name tells Docker which containers, volumes, and networks belong to this stack. The file path alone doesn't set that name; see [Docker project names](https://docs.docker.com/compose/how-tos/project-name/). For a genuinely fresh configuration, agree on an unused name with the owner before starting. Use lowercase ASCII letters, digits, underscores, and hyphens, beginning with a letter or digit. If an installation already exists, keep its actual project identity and leave its lifecycle with the owner; don't register it as a fresh project.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same approved engine; fresh configuration only.**

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

**Expected:** all three inspections succeed without finding resources for the approved name, and `.course-project` is created without overwriting a file or symlink. **Stop:** an invalid name, existing resource or record, inspection failure, or failed write. **Recovery:** keep the resources and files and review the finding with the owner. Do not remove resources or rename an existing installation.

### Use the recorded project and configuration

Define this helper in the same shell. It explicitly selects the recorded project, `.env`, and `compose.yml`. [Exported variables override `.env`](https://docs.docker.com/compose/how-tos/environment-variables/variable-interpolation/), even when you give the file path. If any listed override is exported, even with an empty value, the helper stops and prints only its name, not its value.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same approved engine.**

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

**Expected:** the helper is defined but starts nothing until you call it. **Stop:** a later call reports HOLD or fails. **Recovery:** ask the owner to resolve exported overrides in a clean shell. Then check the approved Docker engine/context and define the helper again. Don't automatically unset variables, rewrite configuration, or recreate a missing project record for an existing installation.

Confirm the engine still matches your approved local context, then start the course stack.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, Docker-verified window.**

```bash
docker context show &&
course_n8n up -d
```

**Expected:** Images download and the course services start. Existing unrelated containers remain unchanged. Wait for startup to settle before the next check.

**Stop:** Pull, resource, privilege, or port errors; an unexpected context; or a failed service.

**Recovery:** Keep the error and configuration, and have the owner resolve the specific network, memory, policy, or port problem. Don't stop unrelated containers, switch engines, or reinstall the stack.

Check which services are running and which n8n executable is running; the image tag alone isn't enough.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same window.**

```bash
course_n8n ps --all &&
course_n8n port n8n 5678 &&
course_n8n exec -T n8n n8n --version
```

**Expected:** You can see all six services. `sandbox-certs` finishes with `Exited (0)`; the others keep running, and `sandbox-api` is healthy. The host mapping is exactly `127.0.0.1:5678`, and the running n8n version is exactly `2.41.5`. Images on disk, a successful `up -d`, or an installer that recognizes the directory do not confirm these results.

**Stop:** Wrong version, missing/restarting/failed services, or a mapping such as `0.0.0.0:5678` or `[::]:5678`. Leave wrong-version instances on **HOLD** pending owner resolution; do not repin them.

**Recovery:** Keep a record of what you saw. If the course stack is exposed unintentionally, stop only this identified stack with the `down` command below, keep its volumes, and work with the owner to fix its configuration. If startup is slow, wait and check again; don't hide a failure that persists by installing repeatedly.

### Save a workflow and prove it persists

1. Open **http://localhost:5678** in your browser. For a genuinely fresh instance, complete **Set up owner account** and select **Next**. These credentials belong to this local n8n instance. If a sign-in screen appears, use the existing local login; do not reset its owner or create another instance.
2. Finish any local onboarding questions. Skip optional offers for a license key or external signup. No n8n Cloud account, external account, or provider API key is required for this readiness check. Leave **n8n Assistant** off, and do not copy your OpenRouter key into n8n.
3. Select **Overview**, then **Build a workflow** on a fresh instance or **Create workflow** when workflows already exist. Click the workflow title, name the blank workflow **Module 7 readiness**, and press **Enter**. The editor saves automatically. Leave the canvas empty and do not select **Publish**. Keep an existing workflow with that name; choose a distinct readiness name if it contains work.
4. Reload the browser page. Confirm the workflow title and empty canvas remain, and that the workflow is unpublished. This reload checks saved state rather than an unsaved tab.

**Expected:** The local editor opens and the named blank workflow survives reload without an external account or key.

**Stop:** The page remains unavailable after startup, unexpected owner setup appears for an existing instance, login fails, saving fails, or the interface differs enough that you cannot confirm saved/unpublished state.

**Recovery:** Keep the instance and ask for help with the specific state. Do not clear volumes, reset accounts, publish a workflow, or enable Assistant to work around it.

Stop only the course stack you identified. Compose `down` removes its containers and network but keeps its named data volumes, so never add `-v`.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same approved engine.**

```bash
course_n8n down
```

**Expected:** Course containers stop and are removed; the data volumes remain. Reloading the local page cannot reach the stopped instance.

**Stop:** The command fails, targets unexpected resources, or the browser still reaches another n8n instance.

**Recovery:** Keep the output and resolve the context/project identity with the owner. Do not remove volumes or other containers.

Start the same stack again using the same directory and engine.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same approved engine.**

```bash
course_n8n up -d &&
course_n8n ps --all
```

**Expected:** Once startup settles, check the same service states again. Repeat the port/version check above, reload **http://localhost:5678**, sign in if needed, and open **Module 7 readiness** from the workflow list. Its name and empty canvas are still saved, it remains unpublished, and you don't need to set up the owner account again.

**Stop:** Data is missing, owner setup returns, the version/mapping changes, or services fail.

**Recovery:** Keep the directory and volumes. Before doing anything else, ask the owner to check whether the engine or Compose project changed. Don't create a replacement workflow to hide a persistence failure.

Record n8n readiness only after you observe the correct version, local-only mapping, the full stack state, the saved workflow after reload, and the workflow still there after this stop/start. If you can't confirm any of these, keep n8n readiness on **HOLD** for Module 7. This does not change either OMP readiness result.

In a later shell, check the approved Docker engine/context and define `course_n8n` again. Reuse `.course-project`; don't rerun `course_n8n_identify` or create another project for a restart. If Docker Desktop is stopped, get the owner's approval for any effects on existing work before starting it.
