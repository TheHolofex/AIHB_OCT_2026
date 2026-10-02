# Ubuntu setup for Module 0

This takes an ordinary Ubuntu desktop account through a checked Oh My Pi install, a course checkout, and one live proof file. Plan for 45 to 90 minutes. A package install can take longer on a slow connection. Wait for the prompt to return before you paste the next box.

You need Git, Python 3.12 or newer, a web browser, an ordinary text editor, and Oh My Pi 18.3.5. The live proof uses one OpenRouter key and the model `openrouter/anthropic/claude-sonnet-4.6`. This path does not install Node, npm, or a second AI tool, and it does not ask you to log in to a model vendor.

Every command box is one paste. Select every line in the box, paste it once, and press Return. The commands use absolute paths, so your current folder does not matter. A home folder with spaces is fine, because every path is quoted.

## 1. Check the machine

Use Ubuntu 24.04 or 26.04 on x86-64 or ARM64. Check the operating system, shell, home-folder permissions, and free space before downloading anything. Use an ordinary account with device-owner approval for any package installation.

**Terminal: Ubuntu, Bash or Zsh, ordinary user, current window.**

```bash
course_preflight() {
  local ID VERSION_ID machine
  [ -r /etc/os-release ] || { printf 'STOP: cannot read /etc/os-release\n' >&2; return 1; }
  . /etc/os-release || return 1
  machine="$(uname -m)" || return 1
  printf 'OS %s %s\nARCH %s\n' "$ID" "${VERSION_ID:-rolling}" "$machine"
  case "$ID:${VERSION_ID:-rolling}:$machine" in
    ubuntu:24.04:x86_64|ubuntu:24.04:aarch64|ubuntu:24.04:arm64|ubuntu:26.04:x86_64|ubuntu:26.04:aarch64|ubuntu:26.04:arm64) ;;
    *) printf 'STOP: unsupported OS or architecture\n' >&2; return 1 ;;
  esac
  if [ -z "${BASH_VERSION:-}" ] && [ -z "${ZSH_VERSION:-}" ]; then
    printf 'STOP: use Bash or Zsh\n' >&2; return 1
  fi
  if [ "$(id -u)" -eq 0 ] || [ ! -w "$HOME" ] || [ ! -x "$HOME" ]; then
    printf 'STOP: use an ordinary account with a writable home folder\n' >&2; return 1
  fi
  df -h "$HOME" || return 1
}
course_preflight
```

**Expected:** The OS and architecture match the supported combination above. In the disk table, Available is at least 15G.

**Stop:** Any STOP line appears, or Available is below 15G.

**Recovery:** Free space if needed, then repeat this check. For an unsupported OS, shell, architecture, or account permission, ask the device owner for a supported environment. Do not choose a different processor's binary.

## 2. See whether the Ubuntu packages are already installed

Git, curl, Python, and the certificate bundle come from Ubuntu's own packages. This check only looks. It does not install or remove anything.

**Terminal: Ubuntu, Bash or Zsh, ordinary user, same window.**

```bash
course_check_packages() {
  local missing="" package
  for package in git curl python3 ca-certificates; do
    [ "$(dpkg-query -W -f='${Status}' "$package" 2>/dev/null)" = "install ok installed" ] || missing="${missing:+$missing }$package"
  done
  if [ -z "$missing" ]; then
    printf 'PACKAGES present\n'
  else
    printf 'PACKAGES missing: %s\n' "$missing"
  fi
}
course_check_packages
```

**Expected:** The line is `PACKAGES present`, or it names one or more of `git`, `curl`, `python3`, and `ca-certificates`.

**Stop:** The command prints an error instead of one of those lines, or you are not in the Ubuntu Terminal application.

**Recovery:** Open the Ubuntu Terminal application as your ordinary user and paste the box again. If the line names missing packages, continue to the next step. If it says `PACKAGES present`, skip the install step and continue at the Python step. An older `python3` can still be present; the Python step is what rejects a version below 3.12.

## 3. Install missing Ubuntu packages

This package step asks for an administrator password. [Ubuntu 24.04’s `python3` package](https://packages.ubuntu.com/noble/python3) is Python 3.12, and [Ubuntu 26.04’s package](https://packages.ubuntu.com/resolute/python3) is Python 3.14. Both meet the course floor. The install uses that distro package, plus Git, curl, and the certificate bundle. Package names and the `apt-get` command are Ubuntu's, as described in [Ubuntu package management](https://documentation.ubuntu.com/server/how-to/software/package-management/).

Skip this box when the previous step printed `PACKAGES present`.

**Terminal: Ubuntu, Bash or Zsh, same window; sudo elevates package installation.**

```bash
sudo apt-get update && sudo apt-get install -y git python3 ca-certificates curl
```

**Expected:** `apt-get` finishes and returns you to the prompt. It may ask for your password before it installs. Already-installed packages stay in place.

**Stop:** `sudo` is missing, the password is rejected, a device policy refuses the install, or `apt-get` stops with an error. A failed update must not be followed by a separate install command.

**Recovery:** Stop. Do not add a personal package archive, download Python from the web, or use pip to get around the refusal. Save the exact error and use [when setup stops](../shared/TROUBLESHOOTING.md). When the device owner has approved the packages, paste this box again.

## 4. Choose the Python interpreter

The later checks must call one real Python executable, not a name that might point somewhere else. Run each available candidate in order: `python3.12`, `python3`, then `python`. Keep the absolute path of the first interpreter that reports Python 3.12 or newer.

**Terminal: Ubuntu, Bash or Zsh, ordinary user, same window.**

```bash
course_resolve_python() {
  PY="$(for candidate in python3.12 python3 python; do "$candidate" -c 'import os, sys; sys.exit(1) if sys.version_info < (3, 12) else print(os.path.realpath(sys.executable))' 2>/dev/null && break; done)"
  if [ -n "$PY" ]; then
    printf 'PY %s\n' "$PY"
    "$PY" -c 'import sys; sys.exit(sys.version_info < (3, 12))' || return 1
    "$PY" --version || return 1
    return 0
  fi
  printf 'STOP: no real Python executable is version 3.12 or newer\n' >&2
  return 1
}
course_resolve_python
```

**Expected:** A line starting with `PY ` gives an absolute path, and the next line starts with `Python 3.12` or newer.

**Stop:** You see the STOP line, no `PY` line, or a version below 3.12.

**Recovery:** If the package step was skipped and the interpreter is too old, return to the elevated install and run it. If Ubuntu's python3 package is already installed and is still older than 3.12, stop. Do not add another Python repository. Save the version line and ask the device owner.

## 5. Download Oh My Pi into a fresh folder

You are downloading the pinned release file and its official checksum list. Nothing is made executable in this step, and nothing is copied into the command folder. The checksum file also lists musl builds. This path selects only `omp-linux-arm64` for `aarch64` or `arm64`, or `omp-linux-x64` for `x86_64`. The files come from the [v18.3.5 release](https://github.com/can1357/oh-my-pi/releases/tag/v18.3.5). This path does not use the project's installer script.

Each attempt has its own folder under your home directory. A failed download stays there. The next try creates a new folder instead of reusing it.

**Terminal: Ubuntu, Bash or Zsh, ordinary user, same window.**

```bash
course_download_omp() {
  local arch asset attempt download
  unset OMP_ASSET OMP_DOWNLOAD_DIR
  arch="$(uname -m)" || return 1
  case "$arch" in
    aarch64|arm64) asset="omp-linux-arm64" ;;
    x86_64) asset="omp-linux-x64" ;;
    *)
      printf 'STOP: unsupported architecture %s\n' "$arch" >&2
      return 1
      ;;
  esac
  if [ -L "$HOME/course-evidence" ] || [ -L "$HOME/course-evidence/reformation-qa" ]; then
    printf 'STOP: evidence parent is linked; keep work under your home folder\n' >&2; return 1
  fi
  attempt="omp-download-$(date -u +%Y%m%dT%H%M%SZ)-$$"
  download="$HOME/course-evidence/reformation-qa/$attempt"
  if [ -e "$download" ] || [ -L "$download" ]; then
    printf 'STOP: %s already exists and was not reused\n' "$download" >&2
    return 1
  fi
  mkdir -p -- "$download" || return 1
  if ! curl -fL --output "$download/$asset" "https://github.com/can1357/oh-my-pi/releases/download/v18.3.5/$asset"; then
    printf 'STOP: binary download failed; nothing was installed or executed\n' >&2
    return 1
  fi
  if ! curl -fL --output "$download/SHA256SUMS.txt" "https://github.com/can1357/oh-my-pi/releases/download/v18.3.5/SHA256SUMS.txt"; then
    printf 'STOP: checksum download failed; nothing was installed or executed\n' >&2
    return 1
  fi
  OMP_ASSET="$asset"
  OMP_DOWNLOAD_DIR="$download"
  printf 'DOWNLOADED %s\n' "$download/$asset"
}
course_download_omp
```

**Expected:** One line starts with `DOWNLOADED ` and names a new folder under your home directory, ending in `omp-linux-arm64` or `omp-linux-x64`.

**Stop:** You see a STOP line, curl reports an error, or the line names a musl file. Do not continue to the install step after a STOP line.

**Recovery:** Leave the failed folder in place. Do not delete it to retry, and do not disable certificate checks. For a missing certificate bundle, use the approved package step to install `ca-certificates`. For a proxy or a certificate error with that package already installed, ask the device owner to correct the connection. Start a fresh download only after the cause is corrected. Keep the failed folder for [troubleshooting](../shared/TROUBLESHOOTING.md).

## 6. Verify the checksum and install the binary

A checksum is a fingerprint for a file. Here it is a 64-character hexadecimal value from `SHA256SUMS.txt`. The install runs only after exactly one well-formed line names the selected file and the downloaded bytes match that value. A missing line, a second line, or a mismatch stops the function before the file is made executable, copied, or run.

The destination is `"$HOME/.local/bin/omp"`. An existing different file is left untouched. A shortcut at that path is left untouched. A file that already matches the verified download is kept.

**Terminal: Ubuntu, Bash or Zsh, ordinary user, same window.**

```bash
course_install_omp() {
  local asset download sums expected actual dest version
  asset="${OMP_ASSET:-}"
  download="${OMP_DOWNLOAD_DIR:-}"
  case "$asset" in
    omp-linux-arm64|omp-linux-x64) ;;
    *)
      printf 'STOP: no selected Linux asset is recorded in this terminal\n' >&2
      return 1
      ;;
  esac
  if [ -z "$download" ] || [ ! -d "$download" ] || [ -L "$download" ]; then
    printf 'STOP: no fresh download directory is recorded in this terminal\n' >&2
    return 1
  fi
  sums="$download/SHA256SUMS.txt"
  if ! expected="$(awk -v asset="$asset" '
    BEGIN { count = 0; hash = "" }
    {
      gsub(/\r/, "")
      if ($2 == asset) { count++; hash = $1; if (NF != 2) bad = 1 }
    }
    END {
      if (count != 1 || bad) exit 2
      if (hash !~ /^[0-9a-fA-F]{64}$/) exit 3
      print hash
    }
  ' "$sums")"; then
    printf 'STOP: checksum entry for %s is absent, ambiguous, or not a 64-character hex digest\n' "$asset" >&2
    return 1
  fi
  if [ ! -f "$download/$asset" ] || [ -L "$download/$asset" ]; then
    printf 'STOP: downloaded file is missing or is a symlink\n' >&2
    return 1
  fi
  actual="$(sha256sum -- "$download/$asset" | awk '{ print $1 }')" || return 1
  if [ "$actual" != "$expected" ]; then
    printf 'STOP: checksum mismatch; the binary was not installed or executed\n' >&2
    return 1
  fi
  chmod +x -- "$download/$asset" || return 1
  if [ -L "$HOME/.local" ] || [ -L "$HOME/.local/bin" ]; then
    printf 'STOP: %s is a symlink; the binary was not installed there\n' "$HOME/.local/bin" >&2
    return 1
  fi
  mkdir -p -- "$HOME/.local/bin" || return 1
  dest="$HOME/.local/bin/omp"
  if [ -L "$dest" ]; then
    printf 'STOP: %s is a symlink; it was not replaced\n' "$dest" >&2
    return 1
  fi
  if [ -e "$dest" ]; then
    if [ ! -f "$dest" ] || ! cmp -s -- "$download/$asset" "$dest"; then
      printf 'STOP: destination exists and differs; it was not overwritten\n' >&2
      return 1
    fi
    printf 'KEEP: destination already matches the verified download\n'
  else
    cp -- "$download/$asset" "$dest" || return 1
    if [ -L "$dest" ] || ! cmp -s -- "$download/$asset" "$dest"; then
      printf 'STOP: copy does not match the verified download\n' >&2
      return 1
    fi
    printf 'INSTALLED %s\n' "$dest"
  fi
  chmod +x -- "$dest" || return 1
  version="$("$dest" --version 2>/dev/null)" || { printf 'STOP: installed OMP could not run\n' >&2; return 1; }
  printf 'OMP_VERSION %s\n' "${version:-missing}"
  if [ "$version" != "omp/18.3.5" ]; then
    printf 'STOP: installed file did not print omp/18.3.5\n' >&2
    return 1
  fi
}
course_install_omp
```

**Expected:** You see `KEEP:` or `INSTALLED`, and then `OMP_VERSION omp/18.3.5`. The verified download remains in its attempt folder.

**Stop:** Any STOP line appears, including a checksum miss, a shortcut destination, or a different existing file. The version line is anything other than `omp/18.3.5`.

**Recovery:** Leave both the download folder and any existing `"$HOME/.local/bin/omp"` in place. Do not delete the existing file, and do not rename the download onto it. For a checksum or download problem, preserve the failed files and ask the course owner to resolve the source or transfer problem before starting a fresh download attempt. For a different existing file or a shortcut, ask the device owner before anything is replaced. Do not switch to the musl asset to get past this stop.

## 7. Keep the user command folder on PATH

PATH is the list of folders searched for command names. Save the nonsecret user-command path for both interactive and login sessions of your current shell. [Bash](https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html) uses `.bashrc` for interactive sessions and the first existing login file in this order: `.bash_profile`, `.bash_login`, `.profile`. The command preserves that precedence. [Zsh](https://zsh.sourceforge.io/Doc/Release/Files.html) uses `.zshrc` and `.zprofile` under `ZDOTDIR`, or your home folder when `ZDOTDIR` is unset.

Append the exact line only if it is absent. Existing content stays intact, including a last line without a newline. Links and nonregular files stop the operation. No key is written.

**Terminal: Ubuntu, Bash or Zsh, ordinary user, same window.**

```bash
course_persist_path() {
  local startup login_file zdir line
  line='case ":$PATH:" in *":$HOME/.local/bin:"*) ;; *) export PATH="$HOME/.local/bin${PATH:+:$PATH}" ;; esac'
  if [ -L "$HOME/.local" ] || [ -L "$HOME/.local/bin" ]; then
    printf 'STOP: user command directory is a symlink\n' >&2; return 1
  fi
  mkdir -p -- "$HOME/.local/bin" || return 1
  if [ -n "${BASH_VERSION:-}" ]; then
    login_file=""
    for startup in "$HOME/.bash_profile" "$HOME/.bash_login" "$HOME/.profile"; do
      if [ -L "$startup" ] || { [ -e "$startup" ] && [ ! -f "$startup" ]; }; then
        printf 'STOP: %s is not an ordinary startup file\n' "$startup" >&2; return 1
      fi
      if [ -z "$login_file" ] && [ -f "$startup" ]; then login_file="$startup"; fi
    done
    set -- "$HOME/.bashrc" "${login_file:-$HOME/.profile}"
  elif [ -n "${ZSH_VERSION:-}" ]; then
    zdir="${ZDOTDIR-$HOME}"
    if [ ! -d "$zdir" ] || [ -L "$zdir" ]; then
      printf 'STOP: Zsh startup directory is missing or linked\n' >&2; return 1
    fi
    set -- "$zdir/.zshrc" "$zdir/.zprofile"
  else
    printf 'STOP: use Bash or Zsh\n' >&2; return 1
  fi
  for startup in "$@"; do
    if [ -L "$startup" ] || { [ -e "$startup" ] && [ ! -f "$startup" ]; } || { [ -f "$startup" ] && { [ ! -r "$startup" ] || [ ! -w "$startup" ]; }; }; then
      printf 'STOP: %s is not a readable, writable ordinary file\n' "$startup" >&2; return 1
    fi
  done
  for startup in "$@"; do
    if [ -f "$startup" ] && grep -Fqx -- "$line" "$startup"; then
      printf 'PATH_LINE already present in %s\n' "$startup"
    else
      if [ -s "$startup" ] && [ -n "$(tail -c 1 -- "$startup")" ]; then
        printf '\n' >> "$startup" || return 1
      fi
      printf '%s\n' "$line" >> "$startup" || return 1
      printf 'PATH_LINE added to %s\n' "$startup"
    fi
  done
}
course_persist_path
```

**Expected:** Two `PATH_LINE` messages name the interactive and login startup files. Each says `added` or `already present`.

**Stop:** A STOP line or file-write error appears.

**Recovery:** Preserve the files. Ask the device owner to resolve linked files or permissions. After that correction, repeat this step; exact existing entries are kept. Then open a new desktop terminal for the check in step 9. Do not export PATH there to hide a startup failure.

## 8. Use the course checkout

Check private-repository access before cloning. GitHub credentials are separate from your course-site password and OpenRouter key. This first check uses existing credentials without changing login or credential-helper settings.

**Terminal: Ubuntu, Bash or Zsh, ordinary user, same window.**

```bash
GIT_TERMINAL_PROMPT=0 git ls-remote --exit-code https://github.com/TheHolofex/AIHB_OCT_2026.git HEAD
```

**Expected:** A commit hash followed by `HEAD`. Skip all GitHub CLI steps below and continue at “Create or reuse the checkout.”

**Stop:** An authentication, repository-not-found, or network error appears. Do not clone yet. This is an access prerequisite, not a directory-permission problem.

**Recovery:** Keep the error. Resolve a network error with the device owner. For missing GitHub credentials, use the fallback below. If your account lacks access, the repository owner must invite or approve that account; login alone cannot grant access.

### Set up GitHub access only if the first check failed

Check whether the official GitHub CLI, `gh`, is already available.

**Terminal: Ubuntu, Bash or Zsh, ordinary user, same window.**

```bash
if command -v gh >/dev/null 2>&1; then
  gh --version
else
  printf 'GH MISSING\n'
fi
```

**Expected:** A `gh version` line, or `GH MISSING`. Skip the install box if a version is shown.

**Stop:** An existing `gh` fails to run.

**Recovery:** Ask the device owner to repair the existing helper. Install only when it is missing.

The official [Ubuntu `gh` package](https://packages.ubuntu.com/noble/gh) requires **Universe** to be available under device policy. If it is unavailable, stop and ask the device owner; do not edit package sources or add a repository. Install the missing helper using this command.

**Terminal: Ubuntu, Bash or Zsh, same window; sudo elevates package installation.**

```bash
sudo apt-get update && sudo apt-get install -y gh
```

**Expected:** The package operation completes and the prompt returns. Enter your administrator password only at the sudo prompt.

**Stop:** Permission is refused, the package is unavailable, or the package operation fails.

**Recovery:** Keep the error and ask the device owner to provide the approved official package. Do not change sources or use another installer.

Sign in through the browser with [GitHub CLI login](https://cli.github.com/manual/gh_auth_login). The terminal supplies a one-time device code and may ask you to press Return to open the browser. Enter that code on GitHub and authorize the **account invited to this repository**. If asked to configure Git authentication now, choose **No**; inspect credential storage first. GitHub CLI prefers the OS credential store but can fall back to a plaintext file. Do not use `--insecure-storage`.

**Terminal: Ubuntu, Bash or Zsh, ordinary user, same window; interactive login.**

```bash
gh auth login --hostname github.com --git-protocol https --web
```

**Expected:** The browser authorization completes and the terminal confirms login.

**Stop:** Login fails, the browser has the wrong account, or device policy refuses authorization.

**Recovery:** Stop and ask the account or device owner to resolve that specific problem. Do not paste any password or token into a command.

Inspect the active account and credential-storage location with [auth status](https://cli.github.com/manual/gh_auth_status). Keep this output private; do not share it or add `--show-token`.

**Terminal: Ubuntu, Bash or Zsh, ordinary user, same window.**

```bash
gh auth status --hostname github.com
```

**Expected:** Authentication succeeds for the invited account, and the reported storage is approved by device policy.

**Stop:** Authentication fails, the active account is wrong, or the storage location is not approved or is unclear.

**Recovery:** Ask the device owner to provision approved storage or credentials. Do not continue to helper setup until both account and storage are approved.

Configure the [Git credential helper for github.com only](https://cli.github.com/manual/gh_auth_setup-git), then check repository access again. The access check runs only if helper setup succeeds.

**Terminal: Ubuntu, Bash or Zsh, ordinary user, same window.**

```bash
gh auth setup-git --hostname github.com &&
GIT_TERMINAL_PROMPT=0 git ls-remote --exit-code https://github.com/TheHolofex/AIHB_OCT_2026.git HEAD
```

**Expected:** A commit hash followed by `HEAD`.

**Stop:** Either command fails. Do not clone.

**Recovery:** Keep the error and ask the repository owner to confirm the invitation and any organization approval for this account. Repeat the access check only after that correction. Do not force helper setup.

### Create or reuse the checkout

Create or inspect the checkout at `"$HOME/Documents/AIHB_OCT_2026"`. If that folder is absent, this step clones [the course repository](https://github.com/TheHolofex/AIHB_OCT_2026.git). If that folder is already a checkout of that exact origin, it is used as it is. Nothing is reset, pulled, or cleaned.

**Terminal: Ubuntu, Bash or Zsh, ordinary user, same window.**

```bash
course_use_checkout() {
  local origin_url checkout_top helper
  R="$HOME/Documents/AIHB_OCT_2026"
  ORIGIN="https://github.com/TheHolofex/AIHB_OCT_2026.git"
  if [ -L "$HOME/Documents" ] || [ -L "$R" ]; then
    printf 'STOP: %s is a symlink; it was not replaced\n' "$R" >&2
    return 1
  fi
  if [ ! -e "$R" ]; then
    GIT_TERMINAL_PROMPT=0 git ls-remote --exit-code https://github.com/TheHolofex/AIHB_OCT_2026.git HEAD || return 1
    mkdir -p -- "$HOME/Documents" || return 1
    git clone "$ORIGIN" "$R" || {
      printf 'STOP: clone failed; the path was not reused\n' >&2
      return 1
    }
  elif [ ! -d "$R" ]; then
    printf 'STOP: %s exists and is not a directory; it was not replaced\n' "$R" >&2
    return 1
  else
    origin_url="$(git -C "$R" remote get-url origin 2>/dev/null || true)"
    if [ "$origin_url" != "$ORIGIN" ]; then
      printf 'STOP: %s is not the course checkout; it was not changed\n' "$R" >&2
      return 1
    fi
    printf 'USE: existing checkout; no reset, pull, or clean\n'
  fi
  if [ -L "$R/.git" ]; then
    printf 'STOP: checkout metadata is linked\n' >&2; return 1
  fi
  checkout_top="$(git -C "$R" rev-parse --show-toplevel 2>/dev/null)" || return 1
  if [ "$checkout_top" != "$R" ]; then
    printf 'STOP: intended folder is not the checkout root\n' >&2; return 1
  fi
  git -C "$R" rev-parse --verify HEAD >/dev/null || return 1
  M="$R/AI_Harness_Bootcamp_2/module-00-setup"
  if [ ! -f "$R/shared/run_omp.py" ] || [ ! -f "$R/shared/course_guard.mjs" ] || [ ! -f "$M/scripts/verify-setup.sh" ] || [ ! -f "$M/shared/case/verify_tool_proof.py" ]; then
    printf 'STOP: this checkout is missing a course helper; it was not reset or updated\n' >&2
    return 1
  fi
  for helper in "$R/shared/run_omp.py" "$R/shared/course_guard.mjs" "$M/scripts/verify-setup.sh" "$M/shared/case/verify_tool_proof.py"; do
    if [ -L "$helper" ]; then
      printf 'STOP: course helper is linked; checkout was not changed\n' >&2; return 1
    fi
  done
  printf 'R %s\n' "$R"
  printf 'M %s\n' "$M"
}
course_use_checkout
```

**Expected:** You see `USE:` or a completed clone, then one `R` line and one `M` line. Both paths are under your home folder.

**Stop:** Any STOP line appears. The folder exists but is a different project, a file, or a shortcut.

**Recovery:** Do not delete, rename, reset, pull, or clean the existing folder. Leave it as it is and ask the person who owns it. A missing helper is not a reason to update the checkout from this guide. Clone help is in GitHub's [cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) page.

## 9. Open a new terminal and confirm the install

Close this terminal completely. Open a new one from the desktop menu, not by typing `bash`, `sh`, or `su` in the old window. A program started from the old window is a child. A child can inherit exported variables and the old PATH. An independently opened terminal reads its startup files and ordinarily has no key from the old window. A child window can inherit a key; that alone does not prove persistence or exposure.

Do not export PATH in the new window before this check. The check is what shows whether the startup file worked.

**Terminal: Ubuntu, Bash or Zsh, ordinary user, newly opened desktop window.**

```bash
course_confirm_new_terminal() {
  local resolved version candidate origin_url
  R="$HOME/Documents/AIHB_OCT_2026"
  M="$R/AI_Harness_Bootcamp_2/module-00-setup"
  PY="$(for candidate in python3.12 python3 python; do "$candidate" -c 'import sys; from pathlib import Path; sys.exit(1) if sys.version_info < (3, 12) else print(Path(sys.executable).resolve())' 2>/dev/null && break; done)"
  case "$PY" in /*) ;; *) printf 'STOP: no absolute Python 3.12+ executable\n' >&2; return 1 ;; esac
  "$PY" -c 'import sys; print(sys.version); sys.exit(sys.version_info < (3, 12))' || return 1
  resolved="$(command -v git)" || return 1
  case "$resolved" in /*) ;; *) printf 'STOP: Git is not an absolute executable\n' >&2; return 1 ;; esac
  printf 'GIT_PATH %s\n' "$resolved"
  "$resolved" --version || return 1
  if [ -L "$HOME/Documents" ] || [ -L "$R" ] || [ -L "$R/.git" ] || [ ! -d "$R" ]; then
    printf 'STOP: checkout is missing or linked\n' >&2; return 1
  fi
  origin_url="$(git -C "$R" remote get-url origin)" || return 1
  if [ "$origin_url" != 'https://github.com/TheHolofex/AIHB_OCT_2026.git' ] || [ "$(git -C "$R" rev-parse --show-toplevel)" != "$R" ]; then
    printf 'STOP: wrong checkout identity\n' >&2; return 1
  fi
  git -C "$R" rev-parse --verify HEAD >/dev/null || return 1
  printf 'R %s\nM %s\nPY %s\n' "$R" "$M" "$PY"
  resolved="$(command -v omp 2>/dev/null || true)"
  printf 'OMP_PATH %s\n' "${resolved:-missing}"
  if [ "$resolved" != "$HOME/.local/bin/omp" ]; then
    printf 'STOP: omp is not the user binary\n' >&2
    return 1
  fi
  version="$("$HOME/.local/bin/omp" --version 2>/dev/null)" || { printf 'STOP: installed OMP could not run\n' >&2; return 1; }
  printf 'OMP_VERSION %s\n' "${version:-missing}"
  if [ "$version" != "omp/18.3.5" ]; then
    printf 'STOP: version is not omp/18.3.5\n' >&2
    return 1
  fi
  if [ -n "${OPENROUTER_API_KEY:-}" ]; then
    printf 'SET\n'
    printf 'STOP: this window already has the key variable\n' >&2
    return 1
  fi
  printf 'MISSING\n'
}
course_confirm_new_terminal
```

**Expected:** `R` and `M` name the course checkout, `PY` is an absolute executable reporting Python 3.12 or newer, and `GIT_PATH` is followed by a Git version. `OMP_PATH` is your home folder plus `/.local/bin/omp`. `OMP_VERSION` is `omp/18.3.5`. The last line is `MISSING`.

**Stop:** Any command fails, Python is below 3.12, Git cannot run, the checkout identity is wrong, OMP has the wrong path or version, or the key line is `SET`.

**Recovery:** For Python or Git, repair only that prerequisite with the device owner. For the checkout, preserve its files and ask the course owner. For a missing or wrong `omp`, return to the PATH step in a window that can edit the startup file, then open another terminal from the desktop. Do not export PATH in the proof window to hide a miss. For `SET`, do not print the variable and do not treat `SET` as proof that the key was written to a file. Close this window. If you had opened it from the old terminal, open the next one from the desktop menu. If an independently opened window still prints `SET`, stop and follow [credentials](../shared/CREDENTIALS.md).

## 10. Enter the key

Set a **US$40 per-key spending cap in OpenRouter** before the live turn. Confirm the cap is saved for the key you will use, following [credentials](../shared/CREDENTIALS.md). If you cannot confirm it, stop before entering the key.

The next box is only the hidden read. Paste it, press Return, and wait. The terminal is waiting for the key even when it looks idle. Paste or type the key, then press Return. The characters do not appear. This stores the key in this process only. It does not write a profile, a file, or a log.

Do not put the key on the same line as a command. Do not run `echo`, `env`, `set`, or `printenv` to look at it. Read [credentials](../shared/CREDENTIALS.md) before you paste a key that may already have been exposed.

**Terminal: Ubuntu, Bash or Zsh, ordinary user, same window.**

```bash
IFS= read -r -s OPENROUTER_API_KEY
```

**Expected:** Nothing is echoed. After you press Return, the prompt comes back. It may stay on the same line, because hidden input does not print a newline.

**Stop:** Any character of the key appears on screen, or you pasted the key into the command box instead of waiting for the read.

**Recovery:** Treat a displayed key as exposed. Stop, follow [credentials](../shared/CREDENTIALS.md), and use the replacement key in a new window. Do not copy the displayed key into a file.

## 11. Export the key in this process

Export makes the variable available to programs you start from this window, including the proof. It still does not write the key to disk. `SET` means this process has a non-empty variable. It does not prove persistence, exposure, or successful authentication. `MISSING` means this process does not have it.

**Terminal: Ubuntu, Bash or Zsh, ordinary user, same window.**

```bash
export OPENROUTER_API_KEY
if [ -n "${OPENROUTER_API_KEY:-}" ]; then
  printf 'SET\n'
else
  printf 'MISSING\n'
fi
```

**Expected:** The only new line is `SET`.

**Stop:** The line is `MISSING`, or any command prints the key itself.

**Recovery:** Paste the hidden-read box again, then paste this box again. Do not add the key to a startup file to make `SET` survive a new terminal. A new independent terminal is expected to print `MISSING` until you enter the key there.

## 12. Choose Python and the checkout again

Recheck Python and the checkout in this same window before preparing the proof. The checkout box will not clone over an existing course folder, and it will not update one.

**Terminal: Ubuntu, Bash or Zsh, ordinary user, same window.**

```bash
course_resolve_python() {
  PY="$(for candidate in python3.12 python3 python; do "$candidate" -c 'import os, sys; sys.exit(1) if sys.version_info < (3, 12) else print(os.path.realpath(sys.executable))' 2>/dev/null && break; done)"
  if [ -n "$PY" ]; then
    printf 'PY %s\n' "$PY"
    "$PY" -c 'import sys; sys.exit(sys.version_info < (3, 12))' || return 1
    "$PY" --version || return 1
    return 0
  fi
  printf 'STOP: no real Python executable is version 3.12 or newer\n' >&2
  return 1
}
course_resolve_python
```

**Expected:** A `PY` line and a Python version of 3.12 or newer.

**Stop:** The STOP line appears, or the version is below 3.12.

**Recovery:** Return to the package and Python steps in the install window. Do not point `PY` at a copy you downloaded outside Ubuntu's packages.

Confirm the existing checkout without changing its files.

**Terminal: Ubuntu, Bash or Zsh, ordinary user, same window.**

```bash
course_use_checkout() {
  local origin_url checkout_top helper
  R="$HOME/Documents/AIHB_OCT_2026"
  ORIGIN="https://github.com/TheHolofex/AIHB_OCT_2026.git"
  if [ -L "$HOME/Documents" ] || [ -L "$R" ]; then
    printf 'STOP: %s is a symlink; it was not replaced\n' "$R" >&2
    return 1
  fi
  if [ ! -e "$R" ]; then
    GIT_TERMINAL_PROMPT=0 git ls-remote --exit-code https://github.com/TheHolofex/AIHB_OCT_2026.git HEAD || return 1
    mkdir -p -- "$HOME/Documents" || return 1
    git clone "$ORIGIN" "$R" || {
      printf 'STOP: clone failed; the path was not reused\n' >&2
      return 1
    }
  elif [ ! -d "$R" ]; then
    printf 'STOP: %s exists and is not a directory; it was not replaced\n' "$R" >&2
    return 1
  else
    origin_url="$(git -C "$R" remote get-url origin 2>/dev/null || true)"
    if [ "$origin_url" != "$ORIGIN" ]; then
      printf 'STOP: %s is not the course checkout; it was not changed\n' "$R" >&2
      return 1
    fi
    printf 'USE: existing checkout; no reset, pull, or clean\n'
  fi
  if [ -L "$R/.git" ]; then
    printf 'STOP: checkout metadata is linked\n' >&2; return 1
  fi
  checkout_top="$(git -C "$R" rev-parse --show-toplevel 2>/dev/null)" || return 1
  if [ "$checkout_top" != "$R" ]; then
    printf 'STOP: intended folder is not the checkout root\n' >&2; return 1
  fi
  git -C "$R" rev-parse --verify HEAD >/dev/null || return 1
  M="$R/AI_Harness_Bootcamp_2/module-00-setup"
  if [ ! -f "$R/shared/run_omp.py" ] || [ ! -f "$R/shared/course_guard.mjs" ] || [ ! -f "$M/scripts/verify-setup.sh" ] || [ ! -f "$M/shared/case/verify_tool_proof.py" ]; then
    printf 'STOP: this checkout is missing a course helper; it was not reset or updated\n' >&2
    return 1
  fi
  for helper in "$R/shared/run_omp.py" "$R/shared/course_guard.mjs" "$M/scripts/verify-setup.sh" "$M/shared/case/verify_tool_proof.py"; do
    if [ -L "$helper" ]; then
      printf 'STOP: course helper is linked; checkout was not changed\n' >&2; return 1
    fi
  done
  printf 'R %s\n' "$R"
  printf 'M %s\n' "$M"
}
course_use_checkout
```

**Expected:** `USE:` for an existing checkout, then `R` and `M` lines.

**Stop:** Any STOP line appears.

**Recovery:** Do not pull, reset, or clean the checkout to create a missing helper. Stop and ask the person who owns that folder.

## 13. Prepare a fresh proof attempt

The proof folder, the token, and the evidence folder are outside the course checkout. The token is created with Python's `secrets` module and saved as `run-token.txt` beside the proof folder, then copied into it. The evidence child is named but not created. The launcher creates that child. Do not create `from-omp.txt` yourself.

**Terminal: Ubuntu, Bash or Zsh, ordinary user, same window.**

```bash
course_prepare_proof() {
  local attempt token_bytes
  unset COURSE_PROOF_VERIFIED
  if [ -z "${PY:-}" ] || [ ! -x "${PY:-}" ]; then
    printf 'STOP: PY is not set in this terminal\n' >&2
    return 1
  fi
  if [ -L "$HOME/course-evidence" ] || [ -L "$HOME/course-evidence/reformation-qa" ]; then
    printf 'STOP: evidence parent is linked; keep work under your home folder\n' >&2; return 1
  fi
  attempt="module-00-$(date -u +%Y%m%dT%H%M%SZ)-$$"
  BASE="$HOME/course-evidence/reformation-qa/$attempt"
  if [ -e "$BASE" ] || [ -L "$BASE" ]; then
    printf 'STOP: %s already exists and was not reused\n' "$BASE" >&2
    return 1
  fi
  mkdir -p -- "$BASE/proof" || return 1
  mkdir -p -- "$BASE/receipts" || return 1
  EVIDENCE="$BASE/receipts/live-1"
  if [ -e "$EVIDENCE" ] || [ -L "$EVIDENCE" ]; then
    printf 'STOP: evidence path already exists\n' >&2
    return 1
  fi
  "$PY" -c 'import secrets; print(secrets.token_hex(16), end="")' > "$BASE/run-token.txt" || return 1
  token_bytes="$(wc -c < "$BASE/run-token.txt" | tr -d '[:space:]')"
  if [ "$token_bytes" -lt 16 ]; then
    printf 'STOP: token file is empty; nothing was sent to the model\n' >&2
    return 1
  fi
  cp -- "$BASE/run-token.txt" "$BASE/proof/run-token.txt" || return 1
  cat > "$BASE/proof/prompt.txt" << 'COURSE_PROMPT'
Read run-token.txt with the course_read tool. Then write only from-omp.txt with the course_write tool. The file contents must be the words omp works, one space, and the exact token text from run-token.txt. Do not write any other file.
COURSE_PROMPT
  if [ -e "$BASE/proof/from-omp.txt" ] || [ -L "$BASE/proof/from-omp.txt" ]; then
    printf 'STOP: from-omp.txt already exists; start a new attempt\n' >&2
    return 1
  fi
  printf 'PROOF %s\n' "$BASE/proof"
  printf 'TOKEN_OUTSIDE %s\n' "$BASE/run-token.txt"
  printf 'EVIDENCE_NOT_CREATED %s\n' "$EVIDENCE"
}
course_prepare_proof
```

**Expected:** Three lines, starting with `PROOF`, `TOKEN_OUTSIDE`, and `EVIDENCE_NOT_CREATED`. The evidence path is printed, and that folder does not exist yet. The token value is not printed.

**Stop:** A STOP line appears, or `from-omp.txt` already exists.

**Recovery:** Leave the existing attempt in place. Paste this box again. The new paste uses a new attempt folder. Do not copy an old `from-omp.txt` into the new proof folder.

## 14. Ask for one tool write

This command starts the course launcher. The launcher selects OpenRouter and `openrouter/anthropic/claude-sonnet-4.6`. It allows the model to read the proof folder and to write only `from-omp.txt`. The key is read from this process. It is not placed on the command line.

A missing key exits 2 and does not create the evidence folder. A live failure exits 1. Keep that attempt. Do not run the launcher again against the same proof folder after a partial file exists.

**Terminal: Ubuntu, Bash or Zsh, ordinary user, same window.**

```bash
course_run_proof() {
  local course_exit
  if [ -z "${PY:-}" ] || [ -z "${R:-}" ] || [ -z "${BASE:-}" ] || [ -z "${EVIDENCE:-}" ]; then
    printf 'STOP: proof paths are not set in this terminal\n' >&2
    return 1
  fi
  if [ -e "$EVIDENCE" ] || [ -L "$EVIDENCE" ]; then
    printf 'STOP: evidence already exists; start a new attempt\n' >&2
    return 1
  fi
  if [ -e "$BASE/proof/from-omp.txt" ] || [ -L "$BASE/proof/from-omp.txt" ]; then
    printf 'STOP: from-omp.txt already exists; start a new attempt\n' >&2
    return 1
  fi
  "$PY" "$R/shared/run_omp.py" \
    --workdir "$BASE/proof" \
    --prompt "$BASE/proof/prompt.txt" \
    --evidence "$EVIDENCE" \
    --allow-write from-omp.txt
  course_exit="$?"
  printf 'LAUNCH_EXIT %s\n' "$course_exit"
  if [ "$course_exit" -eq 2 ]; then
    printf 'STOP: prerequisite hold; do not reuse this attempt\n' >&2
    return 2
  fi
  if [ "$course_exit" -ne 0 ]; then
    printf 'STOP: live run failed; keep this attempt\n' >&2
    return 1
  fi
  return 0
}
course_run_proof
```

**Expected:** The launcher finishes, and the last line you added is `LAUNCH_EXIT 0`. The evidence folder now exists because the launcher created it.

**Stop:** `LAUNCH_EXIT 2` means a prerequisite hold. A missing key is that hold, and the evidence folder should still be absent. `LAUNCH_EXIT 1` means the live run failed or was incomplete. Any other STOP line means this attempt must not be reused.

**Recovery:** Do not create `from-omp.txt` by hand, and do not delete the attempt to make the same path work. For exit 2, read the prerequisite error. If it names a missing key, repeat the hidden-read and export boxes in this window. For another prerequisite, correct that specific failure with the course owner. Only then prepare a new attempt. For exit 1, keep the attempt, inspect the first failure in its receipts, and correct that cause with the course owner before preparing a new attempt. Do not retry blindly. Do not point the launcher at a second provider or a different model.

## 15. Check the proof

The checker reads the proof folder, the token file outside that folder, and the evidence folder. It audits the saved receipts and pinned provider, model, and OMP identities. It passes only when `from-omp.txt` contains `omp works` and the token from this attempt, and when the evidence records that `course_write` wrote those bytes.

**Terminal: Ubuntu, Bash or Zsh, ordinary user, same window.**

```bash
course_verify_proof() {
  local course_exit
  unset COURSE_PROOF_VERIFIED
  if [ -z "${PY:-}" ] || [ -z "${M:-}" ] || [ -z "${BASE:-}" ] || [ -z "${EVIDENCE:-}" ]; then
    printf 'STOP: proof paths are not set in this terminal\n' >&2
    return 1
  fi
  if [ ! -d "$EVIDENCE" ]; then
    printf 'STOP: evidence was not created; do not invent a proof file\n' >&2
    return 1
  fi
  "$PY" "$M/shared/case/verify_tool_proof.py" "$BASE/proof" "$BASE/run-token.txt" "$EVIDENCE"
  course_exit="$?"
  printf 'VERIFY_EXIT %s\n' "$course_exit"
  if [ "$course_exit" -eq 0 ]; then COURSE_PROOF_VERIFIED="$BASE"; fi
  return "$course_exit"
}
course_verify_proof
```

**Expected:** The checker prints `TOOL PROOF PASS`, and the last line is `VERIFY_EXIT 0`.

**Stop:** You see `TOOL PROOF HOLD`, `VERIFY_EXIT 1`, `VERIFY_EXIT 2`, or a STOP line.

**Recovery:** Do not edit `from-omp.txt`, and do not run the checker against a folder you filled in yourself. Keep this attempt as HOLD. Correct the first reported failure with the course owner before preparing a new attempt. A later prerequisite report cannot replace this check.

## 16. Save the prerequisite report

This report checks the machine, the tools, the checkout, and whether the key variable is present in this process. It does not prove the live write. A checkout with changed or untracked files is not a failure and is not a reason to clean it.

**Terminal: Ubuntu, Bash or Zsh, ordinary user, same window.**

```bash
course_save_report() {
  local course_exit
  if [ -z "${M:-}" ] || [ -z "${R:-}" ] || [ -z "${BASE:-}" ]; then
    printf 'STOP: report paths are not set in this terminal\n' >&2
    return 1
  fi
  if [ -e "$BASE/setup-report.txt" ] || [ -L "$BASE/setup-report.txt" ]; then
    printf 'STOP: report already exists; start a new attempt if you need another report\n' >&2
    return 1
  fi
  bash "$M/scripts/verify-setup.sh" "$R" "$BASE/setup-report.txt"
  course_exit="$?"
  printf 'REPORT_EXIT %s\n' "$course_exit"
  return "$course_exit"
}
course_save_report
```

**Expected:** The command writes the report file it names. A run with no failed prerequisite prints `SETUP CHECK PASS` and `REPORT_EXIT 0`. The report does not contain the key.

**Stop:** The command prints `SETUP CHECK HOLD`, any nonzero `REPORT_EXIT`, or an error. A line in the report tells you to pull, reset, or discard files.

**Recovery:** Read the first FAIL line and correct only that prerequisite. Do not pull, reset, clean, or discard the checkout because a report mentions changed files. Do not paste the key into the report. If the report passed but the proof check did not, the proof remains stopped.

## 17. Read the actual proof file

Read the actual result from disk after `TOOL PROOF PASS`. Keep the prerequisite report separate: its PASS cannot replace the tool proof. This command prints every byte of `from-omp.txt`; the token is a run identifier, not your API key.

**Terminal: Ubuntu, Bash or Zsh, ordinary user, same window.**

```bash
course_read_back_proof() {
  if [ -z "${BASE:-}" ] || [ "${COURSE_PROOF_VERIFIED:-}" != "$BASE" ]; then
    printf 'STOP: this attempt has not passed the tool-proof check\n' >&2; return 1
  fi
  if [ ! -f "$BASE/proof/from-omp.txt" ] || [ -L "$BASE/proof/from-omp.txt" ]; then
    printf 'STOP: proof file is missing or linked\n' >&2; return 1
  fi
  printf 'FILE %s\n' "$BASE/proof/from-omp.txt"
  cat -- "$BASE/proof/from-omp.txt" || return 1
  printf '\nEND OF FILE\n'
}
course_read_back_proof
```

**Expected:** Between the file path and `END OF FILE`, you see `omp works` followed by the token for this attempt. This is the file you just verified, under your home folder outside the checkout.

**Stop:** The file cannot be read, its contents differ from the verified result, or any STOP line appears. A failed proof or prerequisite report remains HOLD.

**Recovery:** Preserve the attempt and its receipts. Ask the course owner to resolve the first failed check before creating a new attempt. Do not edit the proof file or use an assistant message as a substitute for the disk file.
