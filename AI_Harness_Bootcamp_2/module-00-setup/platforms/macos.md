# Set up on macOS

Use Git, Python 3.12 or newer, and standalone OMP 18.3.5 to read and write a file through the supplied launcher. Allow 45–90 minutes, plus any system download time. You need a browser, an ordinary text editor, 15 GB free under your home directory, and permission to install the missing tools. Keep work and evidence under your home directory outside the checkout. If device policy blocks an action, stop and use the [support packet](../shared/TROUBLESHOOTING.md).

## Check the machine and existing prerequisites

Open the Terminal app as your ordinary user and check the operating system, native architecture, and running shell. This Homebrew route requires macOS 15 or newer on supported hardware. Apple Silicon is the supported Homebrew configuration; Intel is **Tier 3**, with reduced support and possible source builds, not equivalent support. See [Homebrew requirements](https://docs.brew.sh/Installation).

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

**Expected:** `sw_vers` shows macOS 15+, architecture is `arm64` or native Intel `x86_64`, and the shell is Bash or zsh. Read the available-space column: at least 15 GB must remain. `PREFLIGHT OBSERVED` does not approve a device-policy exception.

**Stop:** The OS, architecture, shell, storage, or permissions do not meet those conditions.

**Recovery:** Preserve the first failure and resolve that condition with the device owner. For Rosetta, close Terminal, clear **Open using Rosetta** in Terminal's Finder **Get Info**, and reopen Terminal through the app before repeating this check.

Find a usable Python by execution, continuing past older candidates. Keep suitable existing Git and Python. Git's Apple system stub can open a developer-tools dialog; cancel if you lack permission, or complete the authorized tools step below.

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

Install Apple's Command Line Tools first if you are using Intel Homebrew, need a source build, or Git/Homebrew reports that developer tools are missing. On Apple Silicon, skip both developer-tools blocks if none of those conditions applies. An existing working tools installation needs no reinstall. [Homebrew documents these requirements](https://docs.brew.sh/Installation).

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same window; approve Apple's GUI only if authorized.**

```bash
if xcode-select -p; then
  printf 'Developer tools path found.\n'
else
  xcode-select --install && printf 'Wait for the Apple installation dialog to finish before continuing.\n'
fi
```

**Expected:** An existing tools path, or an Apple installation dialog. Click **Install**, accept the license if authorized, and wait for installation to finish; returning to the prompt does not mean the download is complete.

**Stop:** Installation fails, authorization is unavailable, or the dialog is still running.

**Recovery:** Preserve the error and ask the device owner to complete the permitted installation. Then confirm the tools are available.

Confirm the selected developer tools after the GUI finishes, or check the existing installation.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same window after the GUI finishes.**

```bash
xcode-select -p && xcrun --find clang
```

**Expected:** Both commands succeed and print developer-tool paths.

**Stop:** Either command fails.

**Recovery:** Keep the failure and have the device owner repair the selected tools installation before continuing.

After installing Apple tools, repeat the existing-prerequisites block: if Git and Python now work, skip Homebrew and package installation. Install Homebrew only if a missing prerequisite needs it and the native prefix has no `brew` executable. The official installer changes the system prefix: `/opt/homebrew` on Apple Silicon or `/usr/local` on Intel. Read its proposed changes and confirmation prompts. It may request an administrator password, which Terminal does not display. Stop if you cannot authorize those changes. Use the full [official installer](https://brew.sh/); never run `sudo brew install`.

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

**Recovery:** Keep the first error and resolve it with the device owner. Do not continue to package installation after a failed installer. A fresh Terminal window will not inherit these shell variables; remain in this window until the explicit reopen step.

Install only missing tools. Recheck Git after any Apple tools installation. Resolve the [versioned Python executable](https://formulae.brew.sh/formula/python@3.12) by running it; an installed formula alone is not a usable interpreter.

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

**Recovery:** Preserve the first error and correct that prerequisite. Do not use `sudo` for formula installation or replace an already suitable tool.

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

**Expected:** Both files exist in the new download directory and both downloads succeed. Their presence alone is not verification.

**Stop:** Either download fails, the destination exists, or a certificate/proxy error appears.

**Recovery:** Retain the failed directory. Resolve the network or path issue before choosing a new `RUN`; never disable certificate checks or execute a partial download.

## Verify before installation or first execution

The following script checks the exact selected filename against its unique SHA-256 entry. It installs only verified bytes. It refuses a symlink or a different existing destination; an identical verified file can be reused without replacement.

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

**Expected:** `SHA256 VERIFIED` names the selected asset and actual digest. Only then is the verified user executable made runnable.

**Stop:** Any checksum, destination, write, or permission check fails.

**Recovery:** Preserve the failure. Do not delete or replace another installation to make this script succeed. Resolve the conflict deliberately or ask for support.

## Keep the verified executable available in a new terminal

Save non-secret command paths for the shell you checked. `PATH` lists directories searched for commands. This preserves existing startup content, appends missing exact lines once, and protects a missing final newline. It refuses linked files and parents. For [Bash](https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html), it uses the first existing login file in `.bash_profile`, `.bash_login`, `.profile` order, plus `.bashrc` for ordinary interactive shells. For [zsh](https://zsh.sourceforge.io/Doc/Release/Files.html), it uses `.zprofile` and `.zshrc` under `ZDOTDIR` or your home directory. Custom startup control that skips these files requires owner review.

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

**Expected:** Two `PROFILE READY` paths for the declared shell. Existing content remains intact; only non-secret Homebrew, Python, and user-bin paths are added.

**Stop:** A file is linked, compiled, unreadable, unwritable, or has startup errors.

**Recovery:** Preserve the file and error; ask its owner to correct the specific startup condition. Do not replace profiles or discard `.profile` settings by creating a higher-priority login file.

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

**Recovery:** Preserve the error and follow authorized [Gatekeeper guidance](https://support.apple.com/en-us/102445) with the device owner. Do not disable Gatekeeper or strip quarantine attributes to bypass the block.

## Confirm private repository access

Check existing Git credentials before installing a login tool or changing a credential helper.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same window.**

```bash
GIT_TERMINAL_PROMPT=0 git ls-remote --exit-code https://github.com/TheHolofex/AIHB_OCT_2026.git HEAD
```

**Expected:** A commit ID followed by `HEAD`, with exit status zero. If this succeeds, skip the entire GitHub CLI fallback below and use the checkout step.

**Stop:** Authentication fails or the repository cannot be read. This is an access prerequisite, not a local-directory permission problem.

**Recovery:** Preserve the error. For missing credentials, use the fallback below. For a network error, correct that connection; for missing access, ask the repository owner to confirm your invitation.

### GitHub CLI fallback — only after the access check fails

Install `gh` only if it is absent. If Homebrew is absent, complete the authorized Homebrew and applicable Apple tools steps above first. If those steps were skipped because Git and Python already worked, `BREW` and `SETUP_SHELL` still come from preflight. After adding Homebrew here, repeat the startup-path saving block so it is available after reopening.

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

**Recovery:** Preserve the error and correct the Homebrew prerequisite; never install the formula with `sudo`.

Sign in with the GitHub account invited to the private repository. The command displays a device code and opens a browser; enter the code at GitHub and authorize that account. GitHub credentials are separate from your course-site password and OpenRouter key. [GitHub CLI prefers the system credential store but may fall back to a plaintext file](https://cli.github.com/manual/gh_auth_login).

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same window; interactive browser login.**

```bash
gh auth login --hostname github.com --git-protocol https --web
```

**Expected:** The browser authorization and CLI login both finish successfully.

**Stop:** Login fails, the wrong account is selected, or policy forbids the requested storage.

**Recovery:** Keep the error privately and ask the device owner to provision approved credentials. Do not use `--insecure-storage`.

Inspect the account and reported storage before configuring Git. Keep this [authentication status](https://cli.github.com/manual/gh_auth_status) output private; do not add `--show-token` or share the output.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same window.**

```bash
gh auth status --hostname github.com
```

**Expected:** Exit zero, the invited account active, and storage approved by your device policy.

**Stop:** Status fails or the reported storage is not approved, including an unapproved plaintext fallback.

**Recovery:** Have the device owner provision approved storage and credentials before proceeding. Login alone does not grant repository access.

Configure the credential helper for [github.com only](https://cli.github.com/manual/gh_auth_setup-git), then repeat the access check with terminal prompting disabled.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same window.**

```bash
gh auth setup-git --hostname github.com &&
GIT_TERMINAL_PROMPT=0 git ls-remote --exit-code https://github.com/TheHolofex/AIHB_OCT_2026.git HEAD
```

**Expected:** The helper succeeds, followed by the repository commit ID and `HEAD`.

**Stop:** Either command fails. Do not clone yet.

**Recovery:** Preserve the error and ask the repository owner to confirm the invited account and required approval. Do not force helper setup or blindly retry login.

## Use the intended checkout without replacing existing work

Use one stable checkout location. Existing related work is not a reason to reset, pull, or clean it.

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

**Recovery:** Preserve that directory and ask the owner to resolve the path conflict. Do not hide a clone failure with `|| true` or discard local changes.

## Reopen independently and check actual tools

Open **Terminal → Shell → New Window** through the Terminal app using the same Bash or zsh profile. Do not launch a child shell from the old prompt. Recreate `R`, `M`, and `PY`: the new window does not inherit your previous shell variables. This check makes no PATH repair and does not enter a key.

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

**Expected:** Actual Git path and version, absolute Python path with version 3.12+, and `$HOME/.local/bin/omp` with exactly `omp/18.3.5`, followed by `FRESH TOOLS READY`. A formula's presence does not prove its executable is on PATH; Python is selected only after execution succeeds. The prerequisite report below also checks command-name resolution.

**Stop:** Any tool fails, the OMP path/version changes, or the checkout files are absent.

**Recovery:** Preserve the failed check, correct the specific non-secret startup setting in the earlier window, then open another independent window. Do not add an export to this check to make it pass.

Observe the key state before entering it. An independent window ordinarily reports `MISSING`; a child of a keyed shell can inherit `SET`. Presence alone proves neither persistence, exposure, nor successful authentication. If `SET` is unexpected, stop and inspect how this window was launched and whether a prior credential configuration exists, without printing its value. Do not save a key in startup files. You can first enter the key now; no earlier entry is required.

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

**Expected:** Only `SET` is printed. This proves presence, not successful authentication or a model call.

**Stop:** The variable is missing or a secret value appears in output.

**Recovery:** Re-enter it through the isolated hidden prompt. Never save the key in a profile, command argument, or evidence file.

## Run a readiness check

Create a fresh readiness-check attempt. Its random token identifies this attempt; it is not a credential. The prompt receives the token only through a file inside the declared work root.

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

**Recovery:** Keep the failed attempt. Correct the reported path or permission problem before creating a new `PROOF_RUN`; never reuse a prior result file as a new result.

Run the paid readiness check only after the fresh-terminal and credential checks pass. The launcher writes receipts under the new evidence directory.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same window.**

```bash
"$PY" "$R/shared/run_omp.py" --workdir "$W" --prompt "$PROOF_RUN/prompt.txt" --evidence "$E" --allow-write from-omp.txt &&
"$PY" "$M/shared/case/verify_tool_proof.py" "$W" "$TOKEN" "$E"
```

**Expected:** A completed paid turn has the pinned identities, a successful `course_write`, exact disk contents, and `READINESS CHECK PASS`. The verifier does not accept the assistant's claim or a manually created file as sufficient evidence.

**Stop:** Missing key gives launcher exit 2 before a provider request. An incomplete turn or failed readiness check holds. A file left behind by a failed child is not success.

**Recovery:** Retain all output and receipts. Restore the missing prerequisite before creating a fresh readiness-check attempt; do not switch provider, enable automatic retries, or reuse a partially written output.

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

**Expected:** The actual absolute file path, `omp works` followed by this attempt's token, and `DISK READBACK PASS`. Together with `READINESS CHECK PASS`, the receipts tie the file to the completed pinned turn.

**Stop:** Disk readback, the prerequisite report, or the readiness check fails. A file alone is not a completed readiness check.

**Recovery:** Preserve the attempt and receipts as `HOLD`. Correct the specific failed prerequisite before creating a new attempt; do not manually write the result file, reuse evidence, change providers, or enable retries. If an operation is unavailable on your device or inaccessible to you, record that limit and leave the readiness check incomplete.

## Save the prerequisite report separately

Save the prerequisite observations in a separate report. The report checks tools and configuration presence; it does not replace the live readiness check or the disk readback.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same window.**

```bash
bash "$M/scripts/verify-setup.sh" "$R" "$PROOF_RUN/setup-report.txt"
```

**Expected:** Exit zero and `SETUP CHECK PASS` with actual observations. A dirty checkout is informational; it is not a demand to discard work. Key or prerequisite failures remain `SETUP CHECK HOLD`.

**Stop:** A required check fails or the report destination already exists.

**Recovery:** Follow its specific next action and preserve the report. Use a new report filename after a real correction. Keep model-call failure, missing prerequisites, and unavailable native/accessible operations as distinct evidence limits.

## Set up local Obsidian

Obsidian lets you edit and link local notes for Module 2. Allow 10–20 minutes for a fresh installation, plus download time. Preserve any existing installation, profile, and vaults. In Finder, inspect **Applications** and your home folder’s **Applications**, and check whether you already launch Obsidian from another location. If it is installed, use that copy and skip the download and install blocks. Record its actual version in the GUI exercise below; do not replace it merely to match 1.13.7.

### Install the verified universal DMG only if Obsidian is absent

The fresh reference is the official universal **1.13.7** DMG for Apple Silicon and Intel. This block downloads to a fresh external folder, verifies the approved SHA-256, and opens the disk image only after a match. It uses `PY` from the earlier Python step. [Official installation instructions](https://github.com/obsidianmd/obsidian-help/blob/master/en/Getting%20started/Download%20and%20install%20Obsidian.md) and [release assets](https://github.com/obsidianmd/obsidian-releases/releases/tag/v1.13.7).

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

**Stop:** Any download/hash/open failure, an existing app, or device policy refuses installation.

**Recovery:** Keep the failed download. Correct the network/path condition and use a fresh download folder; never bypass a hash mismatch, Gatekeeper, or certificate checks. If an app exists elsewhere, use it instead.

**Window: Finder, verified Obsidian disk image.** Drag **Obsidian** to **Applications** only when that destination is absent and installation is authorized. If Finder asks to replace or merge an existing app, cancel. If administrator approval is required, proceed only with the device owner’s approval. Eject the disk image when copying finishes. Open the installed **Obsidian** from Finder’s Applications folder; for an existing installation, open its known location.

**Expected:** The installed app opens. **Stop:** A copy, permission, or security refusal. **Recovery:** Preserve the existing app/profile and ask the device owner to resolve the specific refusal; do not strip quarantine or disable Gatekeeper.

### Open a fresh practice vault and follow its links

This checks that you can follow a note link, save an edit, and see a change made outside Obsidian. Allow 10–15 minutes. A **vault** is a local folder of notes. Use only the fresh practice folder below; keep existing vaults and app profiles intact. No account, community plugin, Sync service, or MCP connection is needed. This exercise makes no provider call and needs no API key.

Keep the same terminal window used above, with `PY` set to the checked Python executable, `R` to your course checkout, and `M` to `$R/AI_Harness_Bootcamp_2/module-00-setup`. The new `OBS_ROOT` is separate from the OMP attempt and the checkout. Run one box at a time; stop after any failure.

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

**Recovery:** Preserve the attempt. If the terminal was closed, restore `PY`, `R`, and `M` using this page’s earlier Python and checkout instructions. For an existing successful initialization, set `OBS_ROOT` to its actual printed parent path and continue with that vault; do not initialize it again. For a failed initialization, correct the named condition and use a fresh attempt. Ask the checkout owner for a missing helper; do not reset or update their checkout.

**Window: Obsidian, ordinary desktop account.**

1. Open Obsidian using the platform launch step above. If another vault opens, leave its files and settings alone. Open the vault switcher, choose **Manage vaults**, then **Open folder as vault → Open**. On a first launch, choose **Open folder as vault → Open** directly.
2. Select exactly the printed `OBS_ROOT/vault` folder. Press **Cmd+Shift+G** in the folder picker and paste the printed absolute path, then open that folder. Do not select the checkout, the parent `OBS_ROOT`, or an existing personal vault.
3. In this practice vault, open **Settings → Community plugins** and leave **Restricted mode** on. If it is off, turn it on for this vault. Under **Settings → Core plugins**, turn **Sync** off if it is on. Do not sign in or install a plugin. Open **Settings → General**, note the actual app version, then close Settings.
4. Open `Start` from the file list. Use Cmd+E to switch to Reading view if needed, then click its **Token** link. Read the token displayed in `Token`; this random text is an exercise identifier, not a credential.
5. Click **Reply** in `Token`. Switch to editing view with Cmd+E if needed. Paste only the token on one line, without a heading, quotation marks, or backticks. Press Cmd+S to save. Obsidian also saves edits automatically; the next command checks the actual saved bytes.

**Expected:** The links open the existing `Token` and `Reply` notes, and `Reply` shows the token you read in the app.

**Stop:** The wrong vault opens, a link creates an empty note, settings cannot remain local and restricted, or you cannot edit/save through the GUI.

**Recovery:** Leave `Start` and `Token` unchanged. Reopen the exact printed vault and follow its existing links. If a policy or display failure prevents GUI use, record `Obsidian HOLD` with the error. A text-editor edit cannot substitute for this observation.

**Terminal: macOS Terminal, Bash or Zsh, ordinary user, same window; no sudo.**

```bash
"$PY" "$M/scripts/obsidian_readiness.py" check --root "$OBS_ROOT"
```

**Expected:** `Token generation 1: initial token; external refresh not yet exercised`, followed by `PASS: Obsidian file round-trip; GUI observation still required`. The command prints the saved disk-observation path.

**Stop:** HOLD or any nonzero exit. A PASS here covers only the initial saved token.

**Recovery:** Read the named failure. For a reply mismatch, return to `Token` in Obsidian, copy its current token into `Reply`, save, and run this check again. Preserve all observations. Do not edit the helper’s `expected` records or repair a reply through the shell.

### Observe an external change, save, and reopen

Keep the practice vault open with `Token` visible. This command changes that note from the terminal while leaving the old reply in place.

**Terminal: macOS Terminal, Bash or Zsh, ordinary user, same window; no sudo.**

```bash
"$PY" "$M/scripts/obsidian_readiness.py" refresh --root "$OBS_ROOT"
```

**Expected:** `Source token rotated outside Obsidian; your saved reply was preserved.`

**Stop:** Any HOLD or error. Do not continue using an old token after a failed refresh.

**Recovery:** Preserve the attempt and the exact error. Resolve the named file or permission condition with support. An interrupted refresh requires a fresh attempt; do not edit expected values or remove a lock to manufacture a pass.

**Window: Obsidian, same practice vault.**

1. Return to `Token` and observe its new text in the already-open app. If needed, select `Start` and follow **Token** again. Confirm that the token differs from the one still saved in `Reply`.
2. Follow **Reply**, replace the old line with the newly observed token, and press Cmd+S. Do not run refresh again.
3. Close the practice vault’s window with its window-close control; leave unrelated vault windows open. Launch Obsidian again using the same platform launch step. If it restores the practice vault, confirm its folder is the exact printed `OBS_ROOT/vault`. Otherwise use the vault switcher’s **Manage vaults → Open folder as vault → Open** to select that exact folder again.
4. Open `Start`, follow **Token**, then **Reply**. Confirm that the new token is still saved after reopening.

**Expected:** You see the external change, save the new reply in Obsidian, and see that reply again after reopening the same folder.

**Stop:** The app does not show the changed token, the edit disappears, or you cannot establish which vault reopened.

**Recovery:** Record `Obsidian HOLD` and the failed GUI action. Preserve the files and observations; do not call a shell-only match GUI success. Check the exact folder and display/session permissions with support before repeating the GUI action.

**Terminal: macOS Terminal, Bash or Zsh, ordinary user, same window; no sudo.**

```bash
"$PY" "$M/scripts/obsidian_readiness.py" check --root "$OBS_ROOT"
```

**Expected:** `Token generation 2: refreshed token; GUI observation still required` and `PASS: Obsidian file round-trip; GUI observation still required`, plus a new disk-observation path. If you deliberately refreshed more than once, the generation is higher; record the actual value.

**Stop:** HOLD, an initial-token generation, or any missing GUI observation.

**Recovery:** Preserve the attempt. For a saved-reply mismatch, correct and save the reply in Obsidian, close/reopen that vault, and check again. Missing GUI evidence leaves Obsidian on HOLD even if disk contents match.

### Record actual Obsidian readiness

In an ordinary text editor, create a new `gui-observation.txt` beside the vault at the actual `OBS_ROOT` path. Record the date, operating system and architecture, actual app version, exact vault path, and both printed disk-observation paths. Describe the link navigation, first edit/save, visible external token change, second edit/save, and close/reopen you actually performed. Record Restricted mode on and Sync off. A screenshot of the practice vault may support this record; exclude credentials and unrelated personal notes.

Write `Obsidian READY` only when both disk checks passed and every listed GUI action was observed. Otherwise write `Obsidian HOLD` and the missing action or exact error. File existence and the `.obsidian` folder do not prove GUI use. Keep this record separate from OMP and n8n readiness; a failure in one does not erase a result in another. Actual reference GUI observation is limited to Obsidian 1.13.7 on Darwin arm64; Intel GUI behavior remains unobserved until you perform and record it.

## Prepare local n8n for Module 7

This gives you a local workflow editor and checks that a saved workflow survives a stop and start. Allow additional download and startup time; the setup estimate above is a planning allowance, not a measured completion time. Complete this n8n check before Module 7. Keep its result separate from both the OMP prerequisite report and the live OMP readiness check above.

### Inspect Docker and preserve existing work

A Docker **context** selects the engine where commands run. Before installing or launching anything, inspect the selected context, existing containers (including stopped ones), volumes, destination, and port. Keep this output private if it contains names or addresses from other work. Do not switch contexts, clear Docker environment variables, or stop an existing application to make room.

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

**Expected:** You can identify the engine and its existing work, or establish that Docker is missing. No listener output from `lsof` (normally exit 1) means none was found; permission errors are not a free-port result. The intended destination is `$HOME/n8n-course`, outside the checkout.

**Stop:** A Docker command fails, the selected engine is remote or unfamiliar, environment overrides exist, port 5678 is occupied, or the destination already exists—even if it is empty or an earlier incomplete attempt.

**Recovery:** Ask the device/work owner to resolve that specific condition. Keep every application, container, volume, directory, and failed attempt. If Docker is already installed but stopped, launch it only after reviewing the effect on existing work. Docker Desktop startup can select `desktop-linux`; record the prior context and have the owner preserve its intended routing. Reuse an approved existing course instance only after checking its actual version and configuration below; skip both installer alternatives and the fresh-file edit. An install elsewhere needs owner review of its actual Compose path before using any lifecycle command. Never silently migrate, repin, reset, uninstall, or upgrade it.

### Install Docker Desktop only if it is missing and approved

Use **Apple menu → About This Mac** to check the macOS release, memory, and **Chip** (Apple Silicon) or **Processor** (Intel). Docker requires at least **4 GB RAM** and supports the current and two preceding major macOS releases; check the current [Mac requirements and downloads](https://docs.docker.com/desktop/setup/install/mac-install/) against your machine. That is Docker's minimum, not a guarantee that this stack plus your other applications fits available memory. The earlier macOS 15+ Homebrew gate does not replace this check. [Intel Homebrew Tier 3](https://docs.brew.sh/Support-Tiers) describes Homebrew support, not Docker's separate Intel support policy.

Have the device owner approve installation, resource use, and the Docker Desktop subscription terms. Education and personal use can qualify for free use; larger commercial organizations and government entities may require a paid subscription. Use the terms on Docker's installation page to determine eligibility before accepting.

1. On that official page, select **Docker Desktop for Mac with Apple silicon** for an Apple chip, or **Docker Desktop for Mac with Intel chip** for an Intel processor. Do not choose based on a Rosetta-translated shell. Rosetta is not strictly required by Docker Desktop; optional tools may need it. Keep the course Terminal native.
2. After saving any open work, close tools that call Docker as the installation page directs. Double-click the downloaded **Docker.dmg**, then drag **Docker** into **Applications**. Keep the installer volume mounted until copying completes. Do not replace an existing Docker.app without owner review.
3. In **Applications**, double-click **Docker.app**. Select **Accept** for the subscription agreement only with owner approval. Follow approved macOS security prompts; do not bypass device controls.
4. Follow the [Docker CLI location options](https://docs.docker.com/desktop/setup/install/mac-permission-requirements/). Current releases default to `$HOME/.docker/bin` and add it to PATH. **Settings → Advanced** allows user or system CLI locations; the system location is `/usr/local/bin` and may require administrator authorization. Releases 4.88.0 and earlier offer **Use recommended settings** or **Use advanced settings** during installation, followed by **Finish**. Choose the owner-approved option. Port 5678 does not require privileged low-port mapping or a default socket symlink.
5. Leave Docker open and wait until its engine is running. A visible application window alone is not readiness. The terminal check below must succeed.

If `docker` is missing in a new terminal, inspect the chosen CLI location. For the user option, add `export PATH="$HOME/.docker/bin:$PATH"` only where needed using your normal text editor: for zsh, the applicable `.zprofile` and `.zshrc` under `ZDOTDIR` or home; for Bash, the first existing login file in `.bash_profile`, `.bash_login`, `.profile` order and `.bashrc`. Preserve their existing contents and the earlier OMP/Python/Homebrew lines. Have the owner review linked, compiled, or managed startup files. Do not create a higher-priority Bash file that masks an existing login file. For system CLI tools, verify `/usr/local/bin` is on PATH without replacing existing PATH entries.

Open **Terminal → Shell → New Window** independently through the app, using the intended Bash or zsh profile. Keep the earlier OMP window for its existing variables; use this new window for all remaining n8n commands. Do not repair PATH inside this check.

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

**Expected:** Docker resolves from the approved CLI location, the approved local engine answers `docker info`, and the Compose plugin runs as `docker compose`. A modern plugin may report version 5; do not require a literal `2.x` version or substitute legacy `docker-compose`. Compare the context and existing work with the earlier observations.

**Stop:** A command fails, the engine/context differs unexpectedly, or startup changed access to existing work.

**Recovery:** Resolve the specific PATH, engine, or context issue with its owner, then open another independent window and repeat. Do not reinstall Docker, reset its data, or run commands against an unapproved engine.

### Generate a fresh course stack without starting it

The [official one-line setup](https://docs.n8n.io/deploy/host-n8n/install-options/one-line-setup) uses Docker Compose. The reviewed [installer source](https://github.com/n8n-io/n8n/blob/master/docker/get-n8n.sh) reports installer **1.4.0**; the command below requests n8n **2.41.5**. The live download can change, so the download-and-review alternative is preferred when you need to inspect exactly what will execute.

Before either route, have the owner approve the full [official stack](https://github.com/n8n-io/n8n/blob/master/docker/get-n8n-compose.yml): `n8n`, `runners`, `sandbox-certs`, `sandbox-api`, `sandbox-runner-1`, and `searxng`. `sandbox-runner-1` runs privileged Docker-in-Docker inside Docker's Linux environment. Its supporting services run even while n8n Assistant is off. If that privilege is disallowed, hold here. Available amd64/arm64 images do not prove native execution on your Mac; only observed local operation can establish readiness.

Repeat the destination and port inspection immediately before installation. Choose **one** route below. Both refuse to reuse `$HOME/n8n-course`; neither should run with `sudo`. Do not set installer source overrides. The `--no-start` option gives you time to restrict the browser port before any service starts.

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

**Expected:** Exit zero and new `compose.yml`, `.env`, and `searxng-settings.yml` under `$HOME/n8n-course`; services have not started. `pipefail` exposes a failed download, but piping can execute bytes before a download finishes. Use the alternative below to avoid that risk.

**Stop:** Any failure, an unexpected installer version, or an “existing install” message. That message proves neither the requested version nor readiness.

**Recovery:** Preserve the partial directory and output. Resolve the failure with the owner before a fresh attempt; do not rerun into or delete that directory.

Alternatively, download to a unique temporary directory. The `&&` chain prevents an unsuccessful or empty download from becoming the reviewable script.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same Docker-verified window; alternative to the pipeline.**

```bash
N8N_REVIEW_DIR="$(mktemp -d "${TMPDIR:-/tmp}/n8n-review.XXXXXX")" &&
curl -fsSL https://get.n8n.io -o "$N8N_REVIEW_DIR/get-n8n.sh.part" &&
[ -s "$N8N_REVIEW_DIR/get-n8n.sh.part" ] &&
mv "$N8N_REVIEW_DIR/get-n8n.sh.part" "$N8N_REVIEW_DIR/get-n8n.sh" &&
printf 'Review this script in your editor: %s/get-n8n.sh\n' "$N8N_REVIEW_DIR"
```

**Expected:** A complete download is saved as `get-n8n.sh`; no script has executed. Open that printed path with **File → Open** in your normal text editor. Review it with the owner, including `SCRIPT_VERSION="1.4.0"`, its source URLs, and its installation actions.

**Stop:** Download failure, a remaining `.part` file, unexpected version, or unapproved actions.

**Recovery:** Keep the failed download and resolve the issue. Never execute the `.part` file. A later successful download needs a new temporary directory and review.

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

**Recovery:** Preserve all files and ask the owner to resolve the specific failure. Do not upgrade or overwrite the attempt.

### Restrict access, start, and inspect

For the fresh install, use **File → Open** in your normal text editor to open `$HOME/n8n-course/compose.yml` (replace `$HOME` with your home-folder path in a file dialog). Under the `n8n` service's `ports`, change only `'5678:5678'` to `'127.0.0.1:5678:5678'`, retaining indentation and quotes. Use **File → Save**. Leave every other service, setting, and volume unchanged. Do not open or display `.env`, paste it into evidence, or run unfiltered `docker compose config`, which can reveal resolved secrets.

**Expected:** The saved file binds n8n only to this Mac's loopback address. No other service publishes a host port.

**Stop:** The expected line is absent, the file differs from the reviewed stack, or this is an existing installation whose settings have not been approved.

**Recovery:** Preserve the file and have the owner review it before starting. Do not replace the whole file with a downloaded template.

### Record the fresh project name

A Compose project name identifies this stack's containers, volumes, and networks. The file path alone does not fix that identity; see [Docker project names](https://docs.docker.com/compose/how-tos/project-name/). For the genuinely fresh configuration, agree on an unused name with the owner before starting. Use lowercase ASCII letters, digits, underscores, and hyphens, beginning with a letter or digit. An existing installation must retain its actual project identity and owner-managed lifecycle; do not register it as a fresh project.

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

**Expected:** all three inspections succeed without finding resources for the approved name, and `.course-project` is created without overwriting a file or symlink. **Stop:** an invalid name, existing resource or record, inspection failure, or failed write. **Recovery:** preserve the resources and files and review the finding with the owner. Do not remove resources or rename an existing installation.

### Use the recorded project and configuration

Define this helper in the same shell. It selects the recorded project, `.env`, and `compose.yml` explicitly. [Exported variables override `.env`](https://docs.docker.com/compose/how-tos/environment-variables/variable-interpolation/), even with an explicit file path. The helper stops if a listed override is exported, including an empty value; it prints only the variable name, never its value.

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

**Expected:** the helper is defined and starts nothing until called. **Stop:** a later call reports HOLD or fails. **Recovery:** have the owner resolve exported overrides in a clean shell, then inspect the approved Docker engine/context and define the helper again. Do not automatically unset variables, rewrite configuration, or recreate a missing project record for an existing installation.

Confirm the engine still matches your approved local context, then start the course stack.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, Docker-verified window.**

```bash
docker context show &&
course_n8n up -d
```

**Expected:** Images download and the course services start. Existing unrelated containers remain unchanged. Wait for startup to settle before the next check.

**Stop:** Pull, resource, privilege, or port errors; an unexpected context; or a failed service.

**Recovery:** Preserve the error and configuration. Have the owner resolve the specific network, memory, policy, or port issue. Do not stop unrelated containers, switch engines, or reinstall the stack.

Inspect actual service state and the running executable, not just the image tag.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same window.**

```bash
course_n8n ps --all &&
course_n8n port n8n 5678 &&
course_n8n exec -T n8n n8n --version
```

**Expected:** All six services are represented. `sandbox-certs` completes with `Exited (0)`; the other services remain running, with `sandbox-api` healthy. The host mapping is exactly `127.0.0.1:5678`, and the running n8n version is exactly `2.41.5`. Images being present, a successful `up -d`, or the installer recognizing a directory is insufficient.

**Stop:** Wrong version, missing/restarting/failed services, or a mapping such as `0.0.0.0:5678` or `[::]:5678`. Leave wrong-version instances on **HOLD** pending owner resolution; do not repin them.

**Recovery:** Preserve the observations. For an unintentionally exposed course stack, stop only this identified stack with the `down` command below, retain its volumes, and resolve its configuration with the owner. For startup delays, wait and repeat the observations; do not hide a persistent failure with repeated installs.

### Save a workflow and prove it persists

1. Open **http://localhost:5678** in your browser. For a genuinely fresh instance, complete **Set up owner account** and select **Next**. These credentials belong to this local n8n instance. If a sign-in screen appears, use the existing local login; do not reset its owner or create another instance.
2. Finish any local onboarding questions. Skip optional offers for a license key or external signup. No n8n Cloud account, external account, or provider API key is required for this readiness check. Leave **n8n Assistant** off, and do not copy your OpenRouter key into n8n.
3. Select **Overview**, then **Build a workflow** on a fresh instance or **Create workflow** when workflows already exist. Click the workflow title, name the blank workflow **Module 7 readiness**, and press **Enter**. The editor saves automatically. Leave the canvas empty and do not select **Publish**. Preserve an existing workflow with that name; choose a distinct readiness name if it contains work.
4. Reload the browser page. Confirm the workflow title and empty canvas remain, and that the workflow is unpublished. This reload checks saved state rather than an unsaved tab.

**Expected:** The local editor opens and the named blank workflow survives reload without an external account or key.

**Stop:** The page remains unavailable after startup, unexpected owner setup appears for an existing instance, login fails, saving fails, or the interface differs enough that you cannot confirm saved/unpublished state.

**Recovery:** Keep the instance and ask for help with the specific state. Do not clear volumes, reset accounts, publish a workflow, or enable Assistant to work around it.

Stop only the identified course stack. Compose `down` removes its containers and network while keeping its named data volumes; never add `-v`.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same approved engine.**

```bash
course_n8n down
```

**Expected:** Course containers stop and are removed; the data volumes remain. Reloading the local page cannot reach the stopped instance.

**Stop:** The command fails, targets unexpected resources, or the browser still reaches another n8n instance.

**Recovery:** Preserve the output and resolve the context/project identity with the owner. Do not remove volumes or other containers.

Start the same stack again using the same directory and engine.

**Terminal: macOS Terminal, Bash or zsh, ordinary user, same approved engine.**

```bash
course_n8n up -d &&
course_n8n ps --all
```

**Expected:** After startup settles, the same service-state expectations apply. Repeat the port/version check above, reload **http://localhost:5678**, sign in if needed, and open **Module 7 readiness** from the workflow list. Its name and empty canvas remain saved and unpublished; no new owner setup is required.

**Stop:** Data is missing, owner setup returns, the version/mapping changes, or services fail.

**Recovery:** Keep both the directory and volumes. Ask the owner to inspect whether the engine or Compose project changed before taking further action. Do not create a replacement workflow to disguise a persistence failure.

Record n8n readiness only after you observe the correct version, local-only mapping, full stack state, saved workflow after reload, and persistence after this stop/start. If any observation is missing, keep n8n readiness on **HOLD** for Module 7. This does not change either OMP readiness result.

In a later shell, inspect the approved Docker engine/context and define `course_n8n` again. Reuse `.course-project`; do not rerun `course_n8n_identify` or create another project for a restart. If Docker Desktop is stopped, obtain owner approval for effects on existing work before launching it.
