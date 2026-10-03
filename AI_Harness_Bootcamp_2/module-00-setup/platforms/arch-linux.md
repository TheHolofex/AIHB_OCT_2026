# Arch Linux setup for Module 0

With an ordinary Arch Linux desktop account, you'll install and verify Oh My Pi, get the course checkout, and run a live readiness check that writes a file. Plan for roughly 45 to 90 minutes. Arch's package step may take longer than a single-package install because it updates the whole system, so wait for the prompt to return before you paste the next box.

You need Git, Python 3.12 or newer, a web browser, an ordinary text editor, and Oh My Pi 18.3.5. The readiness check uses one OpenRouter key and the model `openrouter/anthropic/claude-sonnet-4.6`. This path does not install Node, npm, or a second AI tool, and it does not ask you to log in to a model vendor.

Every command box is one paste. Select every line in the box, paste it once, and press Return. The commands use absolute paths, so your current folder does not matter. A home folder with spaces is fine, because every path is quoted.

## 1. Check the machine

Use official [Arch Linux](https://archlinux.org/about/) on x86-64 only. Arch Linux ARM is a different distribution and is not a supported route here. Check the operating system, shell, home-folder permissions, and free space before downloading anything. Use an ordinary account with device-owner approval for any package installation.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, current window.**

```bash
course_preflight() {
  local ID VERSION_ID machine
  [ -r /etc/os-release ] || { printf 'STOP: cannot read /etc/os-release\n' >&2; return 1; }
  . /etc/os-release || return 1
  machine="$(uname -m)" || return 1
  printf 'OS %s %s\nARCH %s\n' "$ID" "${VERSION_ID:-rolling}" "$machine"
  case "$ID:${VERSION_ID:-rolling}:$machine" in
    arch:*:x86_64) ;;
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

## 2. See whether the Arch packages are already installed

Git, curl, Python, the certificate bundle, and Obsidian come from Arch's official packages. Before installing packages, look in your application menu and known app locations for Obsidian. Keep its profile and vaults. If Obsidian was installed outside pacman, stop and ask the device owner to review it before you install a second copy or replace it. The Python package is `python`, and its command may be `python` rather than `python3`. This check only looks; it does not install, remove, or upgrade anything.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window.**

```bash
course_check_packages() {
  local missing="" package
  for package in git curl python ca-certificates obsidian; do
    pacman -Q "$package" >/dev/null 2>&1 || missing="${missing:+$missing }$package"
  done
  if [ -z "$missing" ]; then
    printf 'PACKAGES present\n'
  else
    printf 'PACKAGES missing: %s\n' "$missing"
  fi
}
course_check_packages
```

**Expected:** The line is `PACKAGES present`, or it names one or more of `git`, `curl`, `python`, `ca-certificates`, and `obsidian`.

**Stop:** The command prints an error instead of one of those lines, or you are not in a Bash or Zsh terminal on Arch.

**Recovery:** Open your desktop terminal as your ordinary user and paste the box again. If the line names missing packages, continue to the next step. If it says `PACKAGES present`, skip the install step and continue at the Python step. An older interpreter can still be present; the Python step is what rejects a version below 3.12.

## 3. Install missing Arch packages

This package step asks for an administrator password. Arch does not support a partial upgrade, so the command syncs the package databases and upgrades the system before installing `git`, `python`, `curl`, `ca-certificates`, and the signed Extra `obsidian` package. Existing packaged apps are part of that approved system upgrade; keep any separate Obsidian installation in place. This follows the [pacman](https://wiki.archlinux.org/title/Pacman) rule; [Arch's Python page](https://wiki.archlinux.org/title/Python) names the Python package. Do not run `pacman -Sy` without the upgrade.

Skip this box when the previous step printed `PACKAGES present` and the next Python step accepts the interpreter. If that step says Python is older than 3.12, come back and run this box. Do not install an older interpreter from the AUR to match a version number.

**Terminal: Arch Linux, Bash or Zsh, same window; sudo elevates package installation.**

```bash
sudo pacman -Syu --needed git python curl ca-certificates obsidian
```

**Expected:** Pacman shows the transaction and asks whether to proceed. This is a full-system upgrade: many unrelated packages may appear, as well as any missing course packages. Read the entire transaction. Type `y` and press Return only when the device owner has approved that transaction; otherwise type `n` and stop. When it finishes, the prompt returns. Already-current packages are not reinstalled.

**Stop:** `sudo` is missing, the password is rejected, a device policy refuses the transaction, pacman stops with a conflict, or the package list includes an unapproved replacement. Type `n` at the confirmation prompt in that last case.

**Recovery:** Stop. Do not use the AUR, an installer script, npm, or pip to get around the refusal. Do not sync the databases without upgrading. Save the exact error and use [when setup stops](../shared/TROUBLESHOOTING.md). When the device owner has approved a full upgrade, paste this box again.

## 4. Choose the Python interpreter

Later checks need the path to a specific Python executable, rather than a command name that could lead elsewhere. Arch’s `python` package provides `python` and may also provide `python3`. Try the available commands in this order: `python3.12`, `python3`, then `python`. Keep the absolute path of the first one that reports Python 3.12 or newer.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window.**

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

**Expected:** A line starting with `PY ` gives an absolute path, and the next line starts with `Python 3.12` or newer. On Arch that path is often the real file behind the `python` command.

**Stop:** You see the STOP line, no `PY` line, or a version below 3.12.

**Recovery:** Return to the elevated pacman step and run the full upgrade. If the official python package is installed and the real interpreter is still older than 3.12, stop. Do not install a versioned interpreter from the AUR. Save the version line and ask the device owner.

## 5. Download Oh My Pi into a fresh folder

Download the pinned release file and its official checksum list. This step does not make anything executable or copy anything into the command folder. The checksum file also lists musl builds, but the command selects only `omp-linux-x64` for `x86_64`. The files come from the [v18.3.5 release](https://github.com/can1357/oh-my-pi/releases/tag/v18.3.5). Do not use the project's installer script.

Each attempt has its own folder under your home directory. A failed download stays there. The next try creates a new folder instead of reusing it.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window.**

```bash
course_download_omp() {
  local arch asset attempt download
  unset OMP_ASSET OMP_DOWNLOAD_DIR
  arch="$(uname -m)" || return 1
  case "$arch" in
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

**Expected:** One line starts with `DOWNLOADED ` and names a new folder under your home directory, ending in `omp-linux-x64`.

**Stop:** You see a STOP line, curl reports an error, or the line names a musl file. Do not continue to the install step after a STOP line.

**Recovery:** Leave the failed folder in place. Do not delete it to retry, and do not disable certificate checks. For a missing certificate bundle, use the approved package step to install `ca-certificates`. For a proxy or a certificate error with that package already installed, ask the device owner to correct the connection. Start a fresh download only after the cause is corrected. Keep the failed folder for [troubleshooting](../shared/TROUBLESHOOTING.md).

## 6. Verify the checksum and install the binary

A checksum is a fingerprint for a file. Here, it is a 64-character hexadecimal value in `SHA256SUMS.txt`. The install proceeds only if exactly one correctly formatted line names the chosen file and the downloaded bytes match that value. If that line is missing, a second line names the file, or the bytes don't match, the function stops before making the file executable, copying it, or running it.

The install goes to `"$HOME/.local/bin/omp"`. If a different file or a shortcut is already there, the command leaves it alone. If the file there already matches the checked download, the command keeps it.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window.**

```bash
course_install_omp() {
  local asset download sums expected actual dest version
  asset="${OMP_ASSET:-}"
  download="${OMP_DOWNLOAD_DIR:-}"
  case "$asset" in
    omp-linux-x64) ;;
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

**Recovery:** Leave both the download folder and any existing `"$HOME/.local/bin/omp"` in place; don't delete the existing file or rename the download onto it. For a checksum or download problem, keep the failed files and ask the course owner to resolve the source or transfer problem before starting a fresh download attempt. For a different existing file or a shortcut, ask the device owner before replacing anything. Don't switch to the musl asset to get past this stop.

## 7. Keep the user command folder on PATH

PATH is the list of folders your shell searches when you type a command name. Save the nonsecret user-command path for both interactive and login sessions of your current shell. [Bash](https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html) reads `.bashrc` for interactive sessions and the first existing login file in this order: `.bash_profile`, `.bash_login`, `.profile`. The command keeps that order. [Zsh](https://zsh.sourceforge.io/Doc/Release/Files.html) reads `.zshrc` and `.zprofile` under `ZDOTDIR`, or in your home folder when `ZDOTDIR` is unset.

The command adds the exact line only if it isn't already there. It keeps the rest of each file, even if its last line has no newline, and stops if it finds a link or a file that isn't a regular file. It does not write a key.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window.**

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

**Recovery:** Leave the files in place and ask the device owner to fix any links or permissions. After that, repeat this step; the command keeps exact entries that are already there. Then open a new desktop terminal for the check in step 9. Don't export PATH in that window to cover up a startup failure.

## 8. Use the course checkout

Check private-repository access before cloning. GitHub credentials are separate from your course-site password and OpenRouter key. This first check uses existing credentials without changing login or credential-helper settings.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window.**

```bash
GIT_TERMINAL_PROMPT=0 git ls-remote --exit-code https://github.com/TheHolofex/AIHB_OCT_2026.git HEAD
```

**Expected:** A commit hash followed by `HEAD`. Skip all GitHub CLI steps below and continue at “Create or reuse the checkout.”

**Stop:** If you see an authentication, repository-not-found, or network error, don't clone yet. Fix access first; this error is not about permission to use the folder.

**Recovery:** Keep the error. Resolve a network error with the device owner. For missing GitHub credentials, use the fallback below. If your account lacks access, the repository owner must invite or approve that account; login alone cannot grant access.

### Set up GitHub access only if the first check failed

Check whether the official GitHub CLI, `gh`, is already available.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window.**

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

Use Arch's official [`github-cli` package](https://archlinux.org/packages/extra/x86_64/github-cli/) to install the missing helper. The command upgrades the whole system, so many unrelated packages may appear. Proceed only if the device owner has approved the entire transaction; type `n` and stop if there are conflicts or unapproved replacements. Do not use the AUR, do a partial upgrade, or replace system Python.

**Terminal: Arch Linux, Bash or Zsh, same window; sudo elevates package installation.**

```bash
sudo pacman -Syu --needed github-cli
```

**Expected:** The package operation completes and the prompt returns. Enter your administrator password only at the sudo prompt.

**Stop:** Permission is refused, the package is unavailable, or the package operation fails.

**Recovery:** Keep the error and ask the device owner to provide the approved official package. Do not change sources or use another installer.

Sign in through your browser using [GitHub CLI login](https://cli.github.com/manual/gh_auth_login). The terminal gives you a one-time device code and may ask you to press Return to open the browser. Enter the code on GitHub and authorize the **account invited to this repository**. If you're asked to configure Git authentication now, choose **No** so you can check where credentials will be stored first. GitHub CLI prefers the OS credential store but can fall back to a plaintext file. Don't use `--insecure-storage`.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window; interactive login.**

```bash
gh auth login --hostname github.com --git-protocol https --web
```

**Expected:** The browser authorization completes and the terminal confirms login.

**Stop:** Login fails, the browser has the wrong account, or device policy refuses authorization.

**Recovery:** Stop and ask the account or device owner to resolve that specific problem. Do not paste any password or token into a command.

Inspect the active account and credential-storage location with [auth status](https://cli.github.com/manual/gh_auth_status). Keep this output private; do not share it or add `--show-token`.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window.**

```bash
gh auth status --hostname github.com
```

**Expected:** Authentication succeeds for the invited account, and the reported storage is approved by device policy.

**Stop:** Authentication fails, the active account is wrong, or the storage location is not approved or is unclear.

**Recovery:** Ask the device owner to provision approved storage or credentials. Do not continue to helper setup until both account and storage are approved.

Set up the [Git credential helper for github.com only](https://cli.github.com/manual/gh_auth_setup-git), then check repository access again. The access check runs only if the helper setup succeeds.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window.**

```bash
gh auth setup-git --hostname github.com &&
GIT_TERMINAL_PROMPT=0 git ls-remote --exit-code https://github.com/TheHolofex/AIHB_OCT_2026.git HEAD
```

**Expected:** A commit hash followed by `HEAD`.

**Stop:** Either command fails. Do not clone.

**Recovery:** Keep the error and ask the repository owner to confirm the invitation and any organization approval for this account. Repeat the access check only after that correction. Do not force helper setup.

### Create or reuse the checkout

Use the checkout at `"$HOME/Documents/AIHB_OCT_2026"`. If the folder isn't there, this step clones [the course repository](https://github.com/TheHolofex/AIHB_OCT_2026.git). If it's already a checkout of that exact origin, the command leaves it as it is. It does not reset, pull, or clean anything.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window.**

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

Close this terminal completely, then open a new terminal window from the desktop menu. Don't type `bash`, `sh`, or `su` in the old window: a program started there is a child that can inherit exported variables and the old PATH. A new terminal window opened from the desktop menu reads its startup files and normally has no key from the old window. If a child window has the key, that alone doesn't show whether the key was saved or exposed.

Do not export PATH in the new window before this check. The check is what shows whether the startup file worked.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, newly opened desktop window.**

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

**Recovery:** If Python or Git is the problem, work with the device owner to fix only that prerequisite. If the checkout is the problem, leave its files in place and ask the course owner. If `omp` is missing or wrong, return to the PATH step in a window where you can edit the startup file, then open another terminal from the desktop. Don't export PATH in the new window to cover up a missing startup setting. Arch won't add the user bin folder unless that startup file has the line. If you see `SET`, don't print the variable or assume the key was written to a file. Close this window. If you opened it from the old terminal, open the next one from the desktop menu. If a new terminal window opened from the desktop menu still prints `SET`, stop and follow [credentials](../shared/CREDENTIALS.md).

## 10. Enter the key

The next box reads the key without showing it. Paste the box, press Return, and wait; the terminal is ready for the key even if it looks idle. Paste or type the key, then press Return. You won't see the characters. The key stays in this process only; this step does not write it to a profile, file, or log.

Do not put the key on the same line as a command. Do not run `echo`, `env`, `set`, or `printenv` to look at it. Read [credentials](../shared/CREDENTIALS.md) before you paste a key that may already have been exposed.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window.**

```bash
IFS= read -r -s OPENROUTER_API_KEY
```

**Expected:** Nothing is echoed. After you press Return, the prompt comes back. It may stay on the same line, because hidden input does not print a newline.

**Stop:** Any character of the key appears on screen, or you pasted the key into the command box instead of waiting for the read.

**Recovery:** Treat a displayed key as exposed. Stop, follow [credentials](../shared/CREDENTIALS.md), and use the replacement key in a new window. Do not copy the displayed key into a file.

## 11. Export the key in this process

Export lets programs started from this window use the variable, including the readiness check. It still doesn't write the key to disk. `SET` means this process has a non-empty variable, but it doesn't tell you whether the key was saved, exposed, or accepted for authentication. `MISSING` means this process doesn't have the variable.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window.**

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

**Recovery:** Paste the hidden-read box again, then paste this box again. Don't put the key in a startup file to keep `SET` when you open a new terminal window. A new independent terminal window is expected to print `MISSING` until you enter the key there.

## 12. Choose Python and the checkout again

In this same window, check Python and the checkout again before preparing the readiness check. The checkout box won't clone over or update an existing course folder. The Python box still accepts `python` when that command points to the real Arch interpreter.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window.**

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

**Recovery:** Return to the pacman step and run the full upgrade. Do not point `PY` at an AUR interpreter or a copy you downloaded outside Arch's packages.

Confirm the existing checkout without changing its files.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window.**

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

## 13. Prepare a fresh readiness check

Keep the work folder, token, and evidence folder outside the course checkout. Python creates the token with its `secrets` module, saves it as `run-token.txt` beside the work folder, then copies it into the work folder. This step names the evidence folder but doesn't create it; the launcher creates it. Don't create `from-omp.txt` yourself.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window.**

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
  printf 'READINESS_WORK %s\n' "$BASE/proof"
  printf 'TOKEN_OUTSIDE %s\n' "$BASE/run-token.txt"
  printf 'EVIDENCE_NOT_CREATED %s\n' "$EVIDENCE"
}
course_prepare_proof
```

**Expected:** Three lines, starting with `READINESS_WORK`, `TOKEN_OUTSIDE`, and `EVIDENCE_NOT_CREATED`. You'll see the path to the evidence folder, which doesn't exist yet, but not the token value.

**Stop:** A STOP line appears, or `from-omp.txt` already exists.

**Recovery:** Keep the existing attempt. Paste this box again to use a new attempt folder, but don't copy an old `from-omp.txt` into the new work folder.

## 14. Ask for one tool write

This command starts the course launcher, which selects OpenRouter and `openrouter/anthropic/claude-sonnet-4.6`. It lets the model read the work folder and write only `from-omp.txt`. The key comes from the variable in this process, not from the command line.

If the key is missing, the launcher exits 2 without creating the evidence folder. If the live run fails, it exits 1. Keep that attempt, and don't run the launcher again against the same work folder after a partial file exists.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window.**

```bash
course_run_proof() {
  local course_exit
  if [ -z "${PY:-}" ] || [ -z "${R:-}" ] || [ -z "${BASE:-}" ] || [ -z "${EVIDENCE:-}" ]; then
    printf 'STOP: readiness-check paths are not set in this terminal\n' >&2
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

**Stop:** `LAUNCH_EXIT 2` means a prerequisite is on hold. A missing key causes this hold, and the evidence folder should still be absent. `LAUNCH_EXIT 1` means the live run failed or didn't finish. If you see any other STOP line, don't reuse this attempt.

**Recovery:** Don't create `from-omp.txt` by hand or delete the attempt to reuse the same path. For exit 2, read the prerequisite error. If it names a missing key, repeat the hidden-read and export boxes in this window. For another prerequisite, work with the course owner to correct that specific failure. Only then prepare a new attempt. For exit 1, keep the attempt and look at the first failure in its receipts. Work with the course owner to correct the cause before preparing a new attempt. Don't retry without finding the cause, and don't point the launcher at a second provider or a different model.

## 15. Verify the readiness result

The checker reads the work folder, the token file outside it, and the evidence folder. It checks the saved receipts and the pinned provider, model, and OMP identities. It passes only if `from-omp.txt` contains `omp works` and the token from this attempt, and the evidence shows that `course_write` wrote those bytes.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window.**

```bash
course_verify_proof() {
  local course_exit
  unset COURSE_PROOF_VERIFIED
  if [ -z "${PY:-}" ] || [ -z "${M:-}" ] || [ -z "${BASE:-}" ] || [ -z "${EVIDENCE:-}" ]; then
    printf 'STOP: readiness-check paths are not set in this terminal\n' >&2
    return 1
  fi
  if [ ! -d "$EVIDENCE" ]; then
    printf 'STOP: evidence was not created; do not invent a result file\n' >&2
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

**Expected:** The checker prints `READINESS CHECK PASS`, and the last line is `VERIFY_EXIT 0`.

**Stop:** You see `READINESS CHECK HOLD`, `VERIFY_EXIT 1`, `VERIFY_EXIT 2`, or a STOP line.

**Recovery:** Don't edit `from-omp.txt` or run the checker against a folder you filled in yourself. Keep this attempt as HOLD, and work with the course owner to correct the first reported failure before preparing a new attempt. A later prerequisite report cannot replace this check.

## 16. Save the prerequisite report

This report checks the machine, the tools, the checkout, and whether the key variable is present in this process. It can't tell you whether the live write succeeded. Changed or untracked files in the checkout aren't a failure, so don't clean the checkout because of them.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window.**

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

**Recovery:** Read the first FAIL line and correct only that prerequisite. Don't pull, reset, clean, or discard the checkout because the report mentions changed files, and don't paste the key into the report. If the report passed but the readiness check didn't, the readiness check remains stopped.

## 17. Read the actual result file

After `READINESS CHECK PASS`, read the result file from disk. Keep the prerequisite report separate: its PASS cannot replace the live readiness check. This command prints every byte of `from-omp.txt`; the token identifies this run and isn't your API key.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window.**

```bash
course_read_back_proof() {
  if [ -z "${BASE:-}" ] || [ "${COURSE_PROOF_VERIFIED:-}" != "$BASE" ]; then
    printf 'STOP: this attempt has not passed the readiness check\n' >&2; return 1
  fi
  if [ ! -f "$BASE/proof/from-omp.txt" ] || [ -L "$BASE/proof/from-omp.txt" ]; then
    printf 'STOP: result file is missing or linked\n' >&2; return 1
  fi
  printf 'FILE %s\n' "$BASE/proof/from-omp.txt"
  cat -- "$BASE/proof/from-omp.txt" || return 1
  printf '\nEND OF FILE\n'
}
course_read_back_proof
```

**Expected:** Between the file path and `END OF FILE`, you see `omp works` followed by the token for this attempt. This is the file you just verified, under your home folder outside the checkout.

**Stop:** The file cannot be read, its contents differ from the verified result, or any STOP line appears. A failed readiness check or prerequisite report remains HOLD.

**Recovery:** Keep the attempt and its receipts. Ask the course owner to resolve the first failed check before creating a new attempt. Don't edit the result file or use an assistant message in place of the file on disk.


## Set up local Obsidian

Obsidian lets you edit and link local notes for Module 2. Allow roughly 10 to 15 minutes for this practice, plus any earlier package download time. Use the signed **Extra** `obsidian` package installed by the full `pacman -Syu` transaction on this page. It is an [Arch-maintained x86-64 package](https://archlinux.org/packages/extra/x86_64/obsidian/), not an AUR package or an Obsidian-vendor binary. Pacman checks package integrity and signatures before installation, so never turn off signature checks to get past a failure. Keep existing app profiles and vaults.

If the package was missing and you skipped the earlier approved full-upgrade transaction, go back and run it. Do not perform a partial upgrade, install through the AUR, or downgrade to match the version named here. Arch listed package version 1.13.7-2; record the version installed on your machine.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window; no sudo.**

```bash
pacman -Q obsidian
```

**Expected:** `obsidian` followed by the installed package version. **Stop:** The package is missing or the command fails. **Recovery:** Keep the error and return to the owner-approved full-upgrade transaction. If you have an Obsidian installation outside the package manager, keep it and ask the device owner to resolve the package-route conflict before you proceed; do not overwrite it.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window; no sudo.**

```bash
obsidian &
```

**Expected:** The Obsidian GUI opens in your desktop session, and you can still use the terminal. **Stop:** A launch error, missing display, or sandbox refusal. **Recovery:** Record Obsidian HOLD and the exact error. Do not add `--no-sandbox`, run as root, or change system security controls to get past the failure.

### Open a fresh practice vault and follow its links

Use Obsidian to follow a note link, save an edit, and see a change made outside the app. Allow roughly 10 to 15 minutes. A **vault** is a local folder of notes. Use only the fresh practice folder, and leave existing vaults and app profiles intact. You don't need an account, community plugin, Sync service, or MCP connection. This work makes no provider call and needs no API key.

Stay in the terminal window used above, with `PY` set to the checked Python executable, `R` to your course checkout, and `M` to `$R/AI_Harness_Bootcamp_2/module-00-setup`. The new `OBS_ROOT` sits outside both the OMP attempt and the checkout. Run one box at a time and stop if any box fails.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window; no sudo.**

```bash
course_initialize_obsidian() {
  [ -n "${PY:-}" ] && [ -n "${R:-}" ] && [ -n "${M:-}" ] || {
    printf 'HOLD: restore this page’s Python and checkout variables first.\n' >&2; return 1;
  }
  [ "$M" = "$R/AI_Harness_Bootcamp_2/module-00-setup" ] || return 1
  [ -f "$M/scripts/obsidian_readiness.py" ] && [ ! -L "$M/scripts/obsidian_readiness.py" ] || {
    printf 'HOLD: course readiness helper is missing or linked.\n' >&2; return 1;
  }
  OBS_ROOT="$HOME/course-evidence/obsidian-arch-linux-$(date -u +%Y%m%dT%H%M%SZ)-$$"
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
2. Select exactly the printed `OBS_ROOT/vault` folder. Press **Ctrl+L** in the folder picker and paste the printed absolute path, then open that folder. Do not select the checkout, the parent `OBS_ROOT`, or an existing personal vault.
3. In this practice vault, open **Settings → Community plugins** and leave **Restricted mode** on. If it is off, turn it on for this vault. Under **Settings → Core plugins**, turn **Sync** off if it is on. Do not sign in or install a plugin. Open **Settings → General**, note the actual app version, then close Settings.
4. Open `Start` from the file list. Use Ctrl+E to switch to Reading view if needed, then click its **Token** link. Read the token displayed in `Token`; this random text is an exercise identifier, not a credential.
5. Click **Reply** in `Token`. Switch to editing view with Ctrl+E if needed. Paste only the token on one line, without a heading, quotation marks, or backticks. Press Ctrl+S to save. Obsidian also saves edits automatically; the next command checks the actual saved bytes.

**Expected:** The links open the existing `Token` and `Reply` notes, and `Reply` shows the token you read in the app.

**Stop:** The wrong vault opens, a link creates an empty note, settings cannot remain local and restricted, or you cannot edit/save through the GUI.

**Recovery:** Leave `Start` and `Token` unchanged. Reopen the vault at the printed path and follow its existing links. If a policy or display failure stops you from using the Obsidian window, record `Obsidian HOLD` with the error. Editing in a text editor doesn't replace seeing and editing the note in Obsidian.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window; no sudo.**

```bash
"$PY" "$M/scripts/obsidian_readiness.py" check --root "$OBS_ROOT"
```

**Expected:** `Token generation 1: initial token; external refresh not yet exercised`, followed by `PASS: Obsidian file round-trip; GUI observation still required`. The command prints the path to the saved record of what it read from disk.

**Stop:** HOLD or any nonzero exit. A PASS here covers only the initial saved token.

**Recovery:** Read the named failure. If the reply doesn't match, return to `Token` in Obsidian, copy its current token into `Reply`, save, and run this check again. Keep all the records from each check. Don't edit the helper's `expected` records or fix a reply through the shell.

### Observe an external change, save, and reopen

Keep the practice vault open with `Token` visible. This command changes that note from the terminal while leaving the old reply in place.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window; no sudo.**

```bash
"$PY" "$M/scripts/obsidian_readiness.py" refresh --root "$OBS_ROOT"
```

**Expected:** `Source token rotated outside Obsidian; your saved reply was preserved.`

**Stop:** Any HOLD or error. Do not continue using an old token after a failed refresh.

**Recovery:** Keep the attempt and the exact error. Work with support to fix the named file or permission problem. If the refresh was interrupted, use a fresh attempt; don't edit expected values or remove a lock to force a pass.

**Window: Obsidian, same practice vault.**

1. Return to `Token` in the app, which is still open, and look for its new text. If needed, select `Start` and follow **Token** again. Confirm that the token differs from the one still saved in `Reply`.
2. Follow **Reply**, replace the old line with the new token you just saw, and press Ctrl+S. Do not run refresh again.
3. Close the practice vault’s window with its window-close control; leave unrelated vault windows open. Launch Obsidian again using the same platform launch step. If it restores the practice vault, confirm its folder is the exact printed `OBS_ROOT/vault`. Otherwise use the vault switcher’s **Manage vaults → Open folder as vault → Open** to select that exact folder again.
4. Open `Start`, follow **Token**, then **Reply**. Confirm that the new token is still saved after reopening.

**Expected:** You see the external change, save the new reply in Obsidian, and see that reply again after reopening the same folder.

**Stop:** The app doesn't show the changed token, the edit disappears, or you can't tell which vault reopened.

**Recovery:** Record `Obsidian HOLD` and the action that failed in the Obsidian window. Keep the files and the records from each check; a match found only in the shell doesn't show that the app worked. Check the exact folder and display/session permissions with support before trying that action again.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window; no sudo.**

```bash
"$PY" "$M/scripts/obsidian_readiness.py" check --root "$OBS_ROOT"
```

**Expected:** `Token generation 2: refreshed token; GUI observation still required` and `PASS: Obsidian file round-trip; GUI observation still required`, plus a new path to the saved record of what the command read from disk. If you refreshed more than once on purpose, the generation is higher; record the value you see.

**Stop:** HOLD, a token that has not been refreshed, or a GUI action you could not see in the Obsidian window.

**Recovery:** Keep the attempt. If the saved reply does not match, correct it in Obsidian, save it, close and reopen that vault, then check again. Obsidian stays on HOLD if you could not see the GUI actions, even when the files on disk match.

### Record actual Obsidian readiness

Use an ordinary text editor to create `gui-observation.txt` beside the vault at the `OBS_ROOT` path you used. Record the date, operating system and architecture, app version, exact vault path, and the two disk-record paths the checks printed. Describe how you followed the links, made and saved the first edit, saw the token change made outside Obsidian, made and saved the second edit, then closed and reopened the vault. Record that Restricted mode was on and Sync was off. You may include a screenshot of the practice vault, but leave out credentials and unrelated personal notes.

Write `Obsidian READY` only if both disk checks passed and you saw every listed GUI action in the Obsidian window. Otherwise write `Obsidian HOLD` and name the missing action or exact error. A file or `.obsidian` folder alone cannot show that you used the app. Keep this record separate from OMP and n8n readiness; a failure in one does not cancel a result in another. These Obsidian GUI actions have not been checked on Arch; record what happens on your machine.

## 18. Inspect Docker before setting up local n8n

You need local n8n for Module 7. Keep its readiness result separate from the OMP prerequisite report and live write above; none of these results replaces another. Leave extra time for image downloads and owner approvals; the setup time is only an estimate, not a measured time.

Use your ordinary account, and leave existing applications, Docker contexts, containers, volumes, and setup attempts in place. The destination is `$HOME/n8n-course`, outside the course checkout; you will open `http://localhost:5678` in your browser. If the destination already exists or the port is in use, mark HOLD until its owner identifies it. Do not delete it, stop another application, or run the installer over it.

The [official n8n stack](https://raw.githubusercontent.com/n8n-io/n8n/master/docker/get-n8n-compose.yml) includes `n8n`, `runners`, `sandbox-certs`, `sandbox-api`, `sandbox-runner-1`, and `searxng`. The sandbox runner uses privileged Docker-in-Docker. Obtain device-owner approval for that privilege and the software's applicable license terms before installation or startup. Assistant stays off even though its support services run. If an existing Docker Desktop is used, its owner must also confirm [Docker Desktop license eligibility](https://docs.docker.com/subscription/desktop-license/). Denial is HOLD.

Check the services before contacting the daemon, because a Docker command can activate a socket that is already listening.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, new window.**

```bash
id -un
systemctl show docker.service docker.socket containerd.service --property=Id,LoadState,ActiveState,UnitFileState
systemctl --user show docker.service docker.socket --property=Id,LoadState,ActiveState,UnitFileState
ss -ltn 'sport = :5678'
if [ -e "$HOME/n8n-course" ] || [ -L "$HOME/n8n-course" ]; then
  printf 'HOLD: n8n-course already exists; preserve it\n'
else
  printf 'DESTINATION absent: %s/n8n-course\n' "$HOME"
fi
if command -v docker >/dev/null 2>&1; then
  docker --version
  docker context ls
  docker context show
else
  printf 'DOCKER missing\n'
fi
printf 'DOCKER_HOST %s\nDOCKER_CONTEXT %s\n' "${DOCKER_HOST:-unset}" "${DOCKER_CONTEXT:-unset}"
```

**Expected:** You can identify the state of each service and socket, which context is selected, and whether an environment variable overrides it. For a fresh install, the destination is absent and the port table has no listener rows. Before Docker is installed, missing units are normal.

**Stop:** A remote or unfamiliar context, root account, unknown listener, existing destination, masked/failed service, or denied service inspection is HOLD.

**Recovery:** Ask the device owner to identify existing work and approve contact with the intended local daemon, including any socket activation. Do not switch contexts, unset overrides, unmask units, or start another daemon to get past a conflict. Continue with an existing course instance only if its owner confirms the directory, actual project identity, stack, version, and permission to stop or restart it. Keep its owner-managed lifecycle and actual identity; do not reinstall it, silently change its pinned version, or give it a new project identity.

Once the owner approves contact with that daemon, inspect existing work. Skip this box only when Docker is missing.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window.**

```bash
docker info && docker compose version && docker ps -a && docker volume ls && docker compose ls --all
```

**Expected:** Docker responds and lists existing work. `docker compose version` works through the modern plugin interface; a version such as 5.x is acceptable. The old `docker-compose` command on its own is not enough.

**Stop:** Permission denial, failed daemon contact, missing Compose, or unidentified work is HOLD for n8n.

**Recovery:** Follow only the missing-prerequisite steps that apply. Keep a compatible engine and Compose plugin. Do not prune containers or volumes, replace a working engine, or use sudo for n8n commands.

## 19. Install only approved missing Arch Docker prerequisites

Use official Arch Linux on x86-64 only, as you checked in step 1. The official packages are [docker](https://archlinux.org/packages/extra/x86_64/docker/) and [docker-compose](https://archlinux.org/packages/extra/x86_64/docker-compose/); the latter provides the modern `docker compose` interface. Keep a compatible engine and plugin that are already installed.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window.**

```bash
for package in docker docker-compose containerd runc podman-docker; do
  pacman -Q "$package" 2>/dev/null || printf '%s absent\n' "$package"
done
```

**Expected:** Each package is identified as installed or absent.

**Stop:** An alternative provider, package conflict, or unexplained runtime installation is HOLD before changes.

**Recovery:** Ask the owner to identify the existing installation and any work that depends on it. Do not replace providers or use an AUR package to get past a conflict. If Docker and Compose already work, skip installation.

If a prerequisite is missing, get approval for the full system transaction. Arch [does not support partial upgrades](https://wiki.archlinux.org/title/System_maintenance#Partial_upgrades_are_unsupported): `-Syu` updates the system, while `--needed` avoids reinstalling packages that are already current. Follow any current [Arch news](https://archlinux.org/news/) that calls for manual steps with the owner before you continue.

**Terminal: Arch Linux, Bash or Zsh, same window; sudo elevates the approved full-system transaction.**

```bash
sudo pacman -Syu --needed docker docker-compose
```

**Expected:** Read the whole proposed transaction. Type `y` only if the owner approved it; otherwise type `n`. Pacman finishes without errors.

**Stop:** A conflict, unapproved replacement, denied full upgrade, or failed transaction is HOLD.

**Recovery:** Keep the error for the owner. Do not replace the full upgrade with a partial sync such as `pacman -Sy`, ignore dependencies, or force an overwrite. Complete any reboot the owner requires, then check service and socket state again using step 18. An installed package alone does not tell you whether the daemon is running.

## 20. Confirm approved ordinary-account Docker access

For the system Docker Engine, follow the [Linux post-install instructions](https://docs.docker.com/engine/install/linux-postinstall/). The `docker` group gives its members root-equivalent control of this machine, so get explicit device-owner approval before adding your account. If approval is denied, mark HOLD; do not run the n8n installer as root or make the Docker socket world-writable. If your account already works with an approved daemon, keep that access and skip the group change.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window; sudo changes approved group membership only.**

```bash
course_docker_access() {
  [ "$(id -u)" -ne 0 ] || { printf 'HOLD: use your ordinary account\n' >&2; return 1; }
  getent group docker >/dev/null || { sudo groupadd docker || return 1; }
  sudo usermod -aG docker "$(id -un)"
}
course_docker_access
```

**Expected:** Your approved account is added without errors. Sign out of the desktop completely and sign back in; opening another terminal alone will not refresh your desktop group membership.

**Stop:** Any denied group change or unfamiliar account is HOLD.

**Recovery:** Ask the owner to resolve access. Never use `sudo sh` for the installer, `sudo docker` for this path, or socket permission changes as a workaround.

If the system Docker service is already active, skip the start box. If it is inactive, start it only after the owner approves `docker.service` and its dependencies, including containerd and any Docker socket activation. Do not change whether it starts at boot or alter an existing user/rootless/Desktop service. [Arch's Docker guidance](https://wiki.archlinux.org/title/Docker) describes how the service starts, but the existing unit policy still takes precedence.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, fresh login; sudo starts the approved system service.**

```bash
sudo systemctl start docker.service
```

**Expected:** The approved service starts without errors.

**Stop:** A masked/failed unit, dependency error, or refused startup is HOLD.

**Recovery:** Keep the error and ask the owner. Do not unmask, restart unrelated services, or enable a socket to bypass the refusal.

In the terminal you opened after signing back in, check the context and existing work again, even if they looked right in another shell earlier. Use this terminal for n8n.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, fresh login.**

```bash
id -un && id -nG && docker context show && docker info && docker compose version && docker ps -a && docker volume ls && docker compose ls --all
```

**Expected:** The approved local daemon responds without sudo, the modern Compose interface works, and all existing work is accounted for.

**Stop:** Either `docker info` or `docker compose version` fails, the context differs, or work is unidentified: HOLD.

**Recovery:** Work through the first failure with the device owner. Do not reinstall a working engine to fix account access. Continue only after this same shell passes the checks.

## 21. Generate a fresh n8n configuration without starting it

Use n8n **2.41.5**. The [official installer source](https://raw.githubusercontent.com/n8n-io/n8n/master/docker/get-n8n.sh) checked for this setup was **1.4.0**. Because the download URL points to a live script that can change, choose the download-and-review method if you need to inspect the script before running it. The [official one-line setup](https://docs.n8n.io/deploy/host-n8n/install-options/one-line-setup) accepts a version and `--no-start`, so you can generate the configuration without starting the containers.

Choose only one method. Both refuse a destination that already exists, even if it is a symlink. An installer message saying “existing install” does not tell you its version or whether it is ready. Keep any partial attempt in place and ask the owner to resolve it; do not reset, uninstall, or upgrade it here.

### Selected one-line method

The subshell turns on `pipefail`, so it reports a failed download even if the shell on the right succeeds. But a pipeline may run part of the script before the download is complete. Choose the review method below if you want to avoid that.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same verified window.**

```bash
(
  set -o pipefail
  [ "$(id -u)" -ne 0 ] || { printf 'HOLD: use an ordinary account\n' >&2; exit 1; }
  if [ -e "$HOME/n8n-course" ] || [ -L "$HOME/n8n-course" ]; then
    printf 'HOLD: existing destination preserved\n' >&2; exit 1
  fi
  curl -fsSL https://get.n8n.io | N8N_DIR="$HOME/n8n-course" sh -s -- --version 2.41.5 --no-start
)
```

**Expected:** Configuration is generated under `$HOME/n8n-course`; containers have not started.

**Stop:** Any curl/installer error, existing-install message, unexpected destination, or unexpected startup is HOLD.

**Recovery:** Keep the destination and error. Do not rerun over the attempt or change its version. Ask the owner to resolve it before continuing.

### Alternative: download and review before execution

This method makes a new download folder and marks the download successful only after curl finishes. It never chooses an incomplete file to run.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same verified window.**

```bash
course_download_n8n() {
  local attempt
  unset N8N_REVIEW_SCRIPT
  attempt="$(mktemp -d "$HOME/n8n-installer-review.XXXXXX")" || return 1
  curl -fsSL https://get.n8n.io -o "$attempt/get-n8n.sh" || { printf 'HOLD: incomplete download preserved; do not execute\n' >&2; return 1; }
  [ -s "$attempt/get-n8n.sh" ] || { printf 'HOLD: empty download\n' >&2; return 1; }
  N8N_REVIEW_SCRIPT="$attempt/get-n8n.sh"
  printf 'REVIEW %s\n' "$N8N_REVIEW_SCRIPT"
}
course_download_n8n
```

**Expected:** `REVIEW` shows the path to the completed script. Use **File > Open** in your ordinary text editor to open that file. Read it before running it, including the parts that download files and generate configuration. Check for `SCRIPT_VERSION="1.4.0"`; ask the owner to review the installer if it has changed.

**Stop:** A failed download, changed script version, or unapproved behavior is HOLD. Do not execute a file from a failed attempt.

**Recovery:** Keep the download for review. Correct the cause with the owner and create another download attempt only when approved.

After the review is approved, run this box instead of the one-line method.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same verified window.**

```bash
course_run_reviewed_n8n() {
  [ "$(id -u)" -ne 0 ] || { printf 'HOLD: use an ordinary account\n' >&2; return 1; }
  [ -n "${N8N_REVIEW_SCRIPT:-}" ] && [ -s "$N8N_REVIEW_SCRIPT" ] && [ ! -L "$N8N_REVIEW_SCRIPT" ] || { printf 'HOLD: no completed script selected\n' >&2; return 1; }
  if [ -e "$HOME/n8n-course" ] || [ -L "$HOME/n8n-course" ]; then
    printf 'HOLD: existing destination preserved\n' >&2; return 1
  fi
  N8N_DIR="$HOME/n8n-course" sh "$N8N_REVIEW_SCRIPT" --version 2.41.5 --no-start
}
course_run_reviewed_n8n
```

**Expected:** Configuration is generated in the fresh destination without starting containers.

**Stop:** Any installer failure or existing-install message is HOLD.

**Recovery:** Keep all files. Ask the owner to resolve this attempt; do not switch to the pipeline to get past the failure.

## 22. Bind the browser port to this laptop and start n8n

In your ordinary text editor, choose **File > Open** and open `compose.yml` inside your home folder's `n8n-course` directory. In the `n8n` service's `ports` entry, change only `'5678:5678'` to `'127.0.0.1:5678:5678'`, then choose **File > Save**. Keep every other service and setting intact. Do this before the first start. If the expected entry is missing or differs, HOLD for owner review.

Do not display or share `.env`, and do not run a resolved `docker compose config` dump: those can reveal generated secrets.

For a freshly generated directory that has never been started, ask the device owner to approve a project name that is unused on the selected Docker engine. A [Compose project name](https://docs.docker.com/compose/how-tos/project-name/) groups its containers, volumes, and networks. The name must start with a letter or digit and contain only lowercase ASCII letters, digits, `_`, or `-`. The check below looks at stopped containers and retained volumes and networks too. If any check fails, mark HOLD.

Keep an existing installation's actual project identity and let its owner manage its lifecycle. Do not create a fresh identity for it or choose a new name to get around existing resources. If it already has a `.course-project` file from this setup that its owner has confirmed, reuse it. Otherwise ask its owner; do not guess its identity to create a replacement record.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same verified window.**

```bash
course_n8n_identify() {
  local project containers volumes networks
  local LC_ALL=C
  if [ ! -d "$HOME/n8n-course" ] || [ -L "$HOME/n8n-course" ]; then
    printf 'HOLD: expected an ordinary fresh n8n-course directory\n' >&2; return 1
  fi
  if [ -e "$HOME/n8n-course/.course-project" ] || [ -L "$HOME/n8n-course/.course-project" ]; then
    printf 'HOLD: existing project record preserved\n' >&2; return 1
  fi
  printf 'Enter the owner-approved unused project name: '
  IFS= read -r project || { printf 'HOLD: project name was not read\n' >&2; return 1; }
  case "$project" in
    ''|[!a-z0-9]*|*[!a-z0-9_-]*)
      printf 'HOLD: invalid project name\n' >&2; return 1 ;;
  esac
  containers="$(docker ps -aq --filter "label=com.docker.compose.project=$project")" || {
    printf 'HOLD: container inspection failed\n' >&2; return 1;
  }
  volumes="$(docker volume ls -q --filter "label=com.docker.compose.project=$project")" || {
    printf 'HOLD: volume inspection failed\n' >&2; return 1;
  }
  networks="$(docker network ls -q --filter "label=com.docker.compose.project=$project")" || {
    printf 'HOLD: network inspection failed\n' >&2; return 1;
  }
  if [ -n "$containers" ] || [ -n "$volumes" ] || [ -n "$networks" ]; then
    printf 'HOLD: project name already has Docker resources; preserve them\n' >&2; return 1
  fi
  (
    umask 077
    set -o noclobber
    printf '%s\n' "$project" > "$HOME/n8n-course/.course-project"
  ) || { printf 'HOLD: project record could not be saved; preserve any existing file\n' >&2; return 1; }
  printf 'PROJECT recorded: %s\n' "$project"
}
course_n8n_identify
```

**Expected:** `PROJECT recorded:` names the approved project. Keep `.course-project` in place for every later start, inspection, and stop.

**Stop:** An existing record, invalid name, existing Docker resource, failed inspection, or failed write is HOLD.

**Recovery:** Keep all files and resources. Ask the owner to resolve the failure. Do not delete a record or resource to retry, and do not automatically rename an installation.

Define `course_n8n` so every call uses the recorded project, the generated `.env`, and the saved `compose.yml`. [Exported shell variables override values from `--env-file`](https://docs.docker.com/compose/how-tos/environment-variables/variable-interpolation/), so the helper checks for conflicts without showing their values. It also catches variables exported with empty values.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same verified window.**

```bash
course_n8n() {
  local variable conflict=0 project
  local LC_ALL=C
  for variable in N8N_VERSION N8N_SANDBOX_VERSION N8N_RUNNERS_AUTH_TOKEN SEARXNG_SECRET COMPOSE_PROJECT_NAME COMPOSE_FILE COMPOSE_ENV_FILES COMPOSE_DISABLE_ENV_FILE COMPOSE_PROFILES; do
    if printenv "$variable" >/dev/null 2>&1; then
      printf 'HOLD: %s\n' "$variable" >&2
      conflict=1
    fi
  done
  [ "$conflict" -eq 0 ] || return 1
  if [ -L "$HOME/n8n-course" ] || [ -L "$HOME/n8n-course/.course-project" ] || [ ! -f "$HOME/n8n-course/.course-project" ]; then
    printf 'HOLD: project record is missing or linked\n' >&2; return 1
  fi
  project="$(cat "$HOME/n8n-course/.course-project")" || {
    printf 'HOLD: project record could not be read\n' >&2; return 1;
  }
  case "$project" in
    ''|[!a-z0-9]*|*[!a-z0-9_-]*)
      printf 'HOLD: invalid recorded project name\n' >&2; return 1 ;;
  esac
  docker compose -p "$project" --env-file "$HOME/n8n-course/.env" -f "$HOME/n8n-course/compose.yml" "$@"
}
```

**Expected:** The prompt returns without output. Use `course_n8n` for every stack command below.

**Stop:** Any helper call prints HOLD or returns an error.

**Recovery:** If the helper names an exported variable, ask the owner to trace its source in a clean shell. Do not print secret values, automatically unset variables, or change configuration to get past the check. If the project record is missing or invalid, keep the directory and ask the owner; do not create a new identity.

When you open a fresh shell later, check the service and socket, then the approved engine and context, using steps 18 and 20 before you contact Docker. Paste only the `course_n8n` definition again and use the recorded file. Never rerun `course_n8n_identify` for an existing installation. Keep using the same engine and context the owner approved; the record does not select a Docker engine.

Recheck the port before startup.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same verified window.**

```bash
ss -ltn 'sport = :5678'
```

**Expected:** No listener rows for a fresh instance. An owner-approved existing course instance may already own the port.

**Stop:** An unidentified listener is HOLD.

**Recovery:** Ask its owner to resolve the conflict. Do not kill a process or change another application's port.

Start only the approved course stack after confirming the saved loopback mapping and privileged-runner approval.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same verified window.**

```bash
course_n8n up -d
```

**Expected:** Images download and the stack starts. The first download can take several minutes.

**Stop:** A port, pull, permission, or startup error is HOLD.

**Recovery:** Keep the files and volumes. Ask the owner to resolve the exact failure; do not prune, reset, or upgrade.

Inspect state and version without printing secrets.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same verified window.**

```bash
course_n8n ps --all &&
course_n8n port n8n 5678 &&
course_n8n exec -T n8n n8n --version
```

**Expected:** All six services are represented. `sandbox-certs` is a one-shot service and should show `Exited (0)`. The other services run; `sandbox-api` becomes healthy. The port command prints `127.0.0.1:5678`, and n8n prints `2.41.5`.

**Stop:** A missing service, nonzero certificate exit, persistent failure/restart, non-loopback publication, or another n8n version is HOLD.

**Recovery:** Let the first startup finish, then check again. If the problem remains, leave the state as it is for owner review. If the version is wrong, keep the existing install for the owner to resolve; do not silently change its pin. If the port is exposed beyond loopback, use the course-only stop command in step 24 and fix the configuration before restarting.

## 23. Save a blank readiness workflow

Open `http://localhost:5678` in your browser. For a fresh instance only, complete **Set up owner account** with your name, email, and a local password, then select **Next**. These credentials belong to this local instance. For an existing instance, use its existing login; do not create a replacement owner. No n8n Cloud account, external account, or API key is required. Skip optional registration or license offers. Keep n8n Assistant off and do not enter the OpenRouter key here.

Select **Overview**, then **Build a workflow** on a fresh instance or **Create workflow** when workflows already exist. Click the workflow title, name it **Module 7 readiness**, and press **Enter**. The editor saves automatically. Keep the canvas blank and do not select **Publish**. Reload the page and confirm the same name and empty canvas remain. If that name already exists, open it rather than overwriting it; if it contains work, keep it and choose a distinct readiness name.

**Expected:** You can reopen the named blank workflow after reload, and it remains unpublished.

**Stop:** A Cloud login, external-key requirement, missing saved workflow, unexpected owner setup on an existing instance, or different UI that prevents these actions is HOLD.

**Recovery:** Check the URL and version. Keep the instance in place and ask the course owner to resolve the mismatch. Do not reset the owner account or treat an assistant response as proof that the workflow was saved.

## 24. Confirm the workflow survives a stop and start

Stop only this approved course stack. Compose keeps the named data volume when `down` is used without `-v`.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same verified window.**

```bash
course_n8n down
```

**Expected:** The course containers and network stop; the data volume remains. The local browser page becomes unavailable after reload.

**Stop:** An unexpected project or stop error is HOLD.

**Recovery:** Keep the output for the owner. Never use `down -v`, remove volumes, or uninstall to recover.

Start the same stack again.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same verified window.**

```bash
course_n8n up -d
```

**Expected:** Repeat the state/port/version inspection from step 22. Reload `http://localhost:5678`, use the existing login if prompted, and reopen your readiness workflow. Its name and blank canvas persist, and it is still unpublished.

**Stop:** Missing data, a new owner-setup screen, wrong version, wrong port mapping, or failed services is HOLD.

**Recovery:** Keep the directory and volumes intact and ask the owner to check the project and data volume. Do not create another account or workflow to hide a failure to keep the saved data. Module 7 n8n readiness passes only if the saved workflow survives this restart; the earlier OMP checks must keep their own passing results.
