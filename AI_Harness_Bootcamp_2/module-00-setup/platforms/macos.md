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

Set the provider-side per-key spending ceiling to US$40 before any live turn, then use your participant-supplied OpenRouter key. The supplied `shared/run_omp.py` uses only `openrouter/anthropic/claude-sonnet-4.6`. Do not use a vendor login or another model. Paste this one command, press Enter, then enter the key without echo and press Enter again.

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

