# Arch Linux setup for Module 0

With an ordinary Arch Linux desktop account, you'll install and check Oh My Pi, get the course checkout, and run a live readiness check that writes a file. Plan for roughly 45 to 90 minutes. Arch's package step upgrades the whole system. Wait for your terminal prompt to return before pasting the next box.

You'll need Git, Python 3.12 or newer, a web browser, an ordinary text editor, and the latest stable Oh My Pi release. The readiness check uses one OpenRouter key and the model `openrouter/anthropic/claude-sonnet-4.6`. You won't install Node, npm, or a second AI tool, and you won't need to log in to a model vendor.

Paste every line of each box at once, then press Return. The commands use absolute paths, so your current folder does not matter. A home folder with spaces is fine because every path is quoted.

## 1. Check this computer

Use official Arch Linux on x86-64, not Arch Linux ARM, which is a different distribution. Before downloading anything, check your operating system, architecture, shell, account, free space, packages, and Python version. Use an ordinary account; get the device owner's approval before installing packages.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, current window.**

```bash
course_check_computer() {
  local ID VERSION_ID machine missing package py
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
  missing=""
  for package in git curl python ca-certificates diffutils less obsidian; do
    pacman -Q "$package" >/dev/null 2>&1 || missing="${missing:+$missing }$package"
  done
  if [ -z "$missing" ]; then
    printf 'PACKAGES present\n'
  else
    printf 'PACKAGES missing: %s\n' "$missing"
  fi
  py="$(for candidate in python3.12 python3 python; do "$candidate" -c 'import os, sys; sys.exit(1) if sys.version_info < (3, 12) else print(os.path.realpath(sys.executable))' 2>/dev/null && break; done)"
  if [ -n "$py" ]; then
    printf 'PY %s\n' "$py"
    "$py" --version || return 1
  else
    printf 'PY missing: step 2 installs or upgrades python\n'
  fi
}
course_check_computer
```

**Expected:** The OS line shows `arch`, and ARCH shows `x86_64`. Available space is at least 15G. The package line is `PACKAGES present` or names some of `git curl python ca-certificates less obsidian`. The last lines show a `PY` path with `Python 3.12` or newer, or `PY missing: step 2 installs or upgrades python`.

**Stop:** Any STOP line appears, or Available is below 15G.

**Recovery:** Free space if needed, then paste this box again. For an unsupported OS, shell, architecture, or account, ask the device owner for a supported environment. A missing package or `PY missing` is not a stop; step 2 handles it.

## 2. Install missing packages

Skip this box if step 1 printed both `PACKAGES present` and a `PY` path. Arch does not support partial upgrades. This command upgrades the whole system with `-Syu` and installs the listed packages in the same transaction. Read the entire transaction. Type `y` only if the device owner has approved every package listed; otherwise type `n` and stop. The `python` package from core provides Python, and `obsidian` is the signed package from extra.

If step 1 lists `obsidian` as missing, check your application menu first. If Obsidian is already installed outside pacman (Flatpak, an AppImage, or a vendor package), stop and ask the device owner before installing a second copy. Remove `obsidian` from the command only with their approval.

**Terminal: Arch Linux, Bash or Zsh, same window; sudo elevates the approved full upgrade.**

```bash
sudo pacman -Syu --needed git python curl ca-certificates diffutils less obsidian
```

**Expected:** Pacman shows the full transaction including any system updates and the missing course packages. Prompt returns after completion. Already-current packages are not reinstalled.

**Stop:** sudo missing, password rejected, policy refusal, conflict, or unapproved replacement in the list.

**Recovery:** Stop. Do not use AUR, partial `-Sy`, or other workarounds. When the owner approves the full transaction, paste again. Use [when setup stops](../shared/TROUBLESHOOTING.md) for the exact error.

## 3. Install Oh My Pi

Download the latest stable release's x86_64 binary and `SHA256SUMS.txt` into a fresh folder. The commands save the selected release's details in `release.json`, verify the binary's checksum, and install it at `~/.local/bin/omp`. A different existing `omp` is left unchanged. The startup files gain a PATH entry so new terminals find the verified binary. Never run an unverified download.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window.**

```bash
course_install_omp() {
  local arch asset attempt download sums expected actual dest version line startup login_file zdir tag base py candidate
  unset OMP_ASSET OMP_DOWNLOAD_DIR
  arch="$(uname -m)" || return 1
  case "$arch" in x86_64) asset="omp-linux-x64" ;; *) printf 'STOP: unsupported architecture\n' >&2; return 1 ;; esac
  if [ -L "$HOME/course-evidence" ] || [ -L "$HOME/course-evidence/reformation-qa" ]; then
    printf 'STOP: evidence parent is linked\n' >&2; return 1
  fi
  attempt="omp-download-$(date -u +%Y%m%dT%H%M%SZ)-$$"
  download="$HOME/course-evidence/reformation-qa/$attempt"
  if [ -e "$download" ] || [ -L "$download" ]; then printf 'STOP: download dir already exists\n' >&2; return 1; fi
  mkdir -p -- "$download" || return 1
  py="$(for candidate in python3.12 python3 python; do "$candidate" -c 'import sys; from pathlib import Path; sys.exit(1) if sys.version_info < (3, 12) else print(Path(sys.executable).resolve())' 2>/dev/null && break; done)"
  case "$py" in /*) ;; *) printf 'STOP: Python 3.12+ is required to read release metadata\n' >&2; return 1 ;; esac
  curl -fL --output "$download/release.json" 'https://api.github.com/repos/can1357/oh-my-pi/releases/latest' ||
    { printf 'STOP: latest release metadata unavailable\n' >&2; return 1; }
  tag="$("$py" - "$download/release.json" "$asset" <<'PYRELEASE'
import json, re, sys
from pathlib import Path
try:
    release = json.loads(Path(sys.argv[1]).read_text())
    tag = release["tag_name"]
    if not isinstance(tag, str) or not re.fullmatch(r"v[0-9]+\.[0-9]+\.[0-9]+", tag):
        raise ValueError("invalid release tag")
    if release.get("draft") is not False or release.get("prerelease") is not False:
        raise ValueError("release is not stable")
    base = "https://github.com/can1357/oh-my-pi/releases/download/%s/" % tag
    for name in (sys.argv[2], "SHA256SUMS.txt"):
        matches = [item for item in release.get("assets", []) if item.get("name") == name]
        if len(matches) != 1 or matches[0].get("browser_download_url") != base + name:
            raise ValueError("required release asset is missing or inconsistent")
    print(tag)
except (AttributeError, KeyError, TypeError, ValueError):
    sys.exit("STOP: latest release metadata or required assets are invalid")
PYRELEASE
  )" || return 1
  base="https://github.com/can1357/oh-my-pi/releases/download/$tag"
  printf 'RELEASE %s (%s)\n' "$tag" "$download/release.json"
  curl -fL --output "$download/$asset" "$base/$asset" || { printf 'STOP: binary download failed\n' >&2; return 1; }
  curl -fL --output "$download/SHA256SUMS.txt" "$base/SHA256SUMS.txt" || { printf 'STOP: checksum download failed\n' >&2; return 1; }
  sums="$download/SHA256SUMS.txt"
  expected="$(awk -v asset="$asset" '
    BEGIN { count=0; hash="" }
    { gsub(/\r/,""); if ($2==asset) { count++; hash=$1; if (NF!=2) bad=1 } }
    END { if (count!=1 || bad) exit 2; if (hash !~ /^[0-9a-fA-F]{64}$/) exit 3; print hash }
  ' "$sums")" || { printf 'STOP: checksum entry absent or ambiguous\n' >&2; return 1; }
  [ -f "$download/$asset" ] && [ ! -L "$download/$asset" ] || { printf 'STOP: downloaded file missing or link\n' >&2; return 1; }
  actual="$(sha256sum -- "$download/$asset" | awk '{print $1}')" || return 1
  [ "$actual" = "$expected" ] || { printf 'STOP: checksum mismatch\n' >&2; return 1; }
  chmod +x -- "$download/$asset" || return 1
  if [ -L "$HOME/.local" ] || [ -L "$HOME/.local/bin" ]; then printf 'STOP: .local is a link\n' >&2; return 1; fi
  mkdir -p -- "$HOME/.local/bin" || return 1
  dest="$HOME/.local/bin/omp"
  if [ -L "$dest" ]; then printf 'STOP: destination is a link\n' >&2; return 1; fi
  if [ -e "$dest" ]; then
    if [ ! -f "$dest" ] || ! cmp -s -- "$download/$asset" "$dest"; then printf 'STOP: destination differs\n' >&2; return 1; fi
    printf 'KEEP: destination already matches\n'
  else
    cp -- "$download/$asset" "$dest" || return 1
    cmp -s -- "$download/$asset" "$dest" || { printf 'STOP: copy mismatch\n' >&2; return 1; }
    printf 'INSTALLED %s\n' "$dest"
  fi
  chmod +x -- "$dest" || return 1
  version="$("$dest" --version 2>/dev/null)" || { printf 'STOP: installed OMP would not run\n' >&2; return 1; }
  printf 'OMP_VERSION %s\n' "${version:-missing}"
  [ "$version" = "omp/${tag#v}" ] || { printf 'STOP: installed version differs from selected %s\n' "$tag" >&2; return 1; }
  # persist PATH for Bash and Zsh
  line='case ":$PATH:" in *":$HOME/.local/bin:"*) ;; *) export PATH="$HOME/.local/bin${PATH:+:$PATH}" ;; esac'
  if [ -L "$HOME/.local" ] || [ -L "$HOME/.local/bin" ]; then printf 'STOP: user bin is link\n' >&2; return 1; fi
  mkdir -p -- "$HOME/.local/bin" || return 1
  if [ -n "${BASH_VERSION:-}" ]; then
    login_file=""
    for startup in "$HOME/.bash_profile" "$HOME/.bash_login" "$HOME/.profile"; do
      if [ -L "$startup" ] || { [ -e "$startup" ] && [ ! -f "$startup" ]; }; then printf 'STOP: bad startup file\n' >&2; return 1; fi
      if [ -z "$login_file" ] && [ -f "$startup" ]; then login_file="$startup"; fi
    done
    set -- "$HOME/.bashrc" "${login_file:-$HOME/.profile}"
  elif [ -n "${ZSH_VERSION:-}" ]; then
    zdir="${ZDOTDIR-$HOME}"
    [ -d "$zdir" ] && [ ! -L "$zdir" ] || { printf 'STOP: bad ZDOTDIR\n' >&2; return 1; }
    set -- "$zdir/.zshrc" "$zdir/.zprofile"
  else
    printf 'STOP: use Bash or Zsh\n' >&2; return 1
  fi
  for startup in "$@"; do
    if [ -L "$startup" ] || { [ -e "$startup" ] && [ ! -f "$startup" ]; } || { [ -f "$startup" ] && { [ ! -r "$startup" ] || [ ! -w "$startup" ]; }; }; then
      printf 'STOP: bad startup file\n' >&2; return 1
    fi
  done
  for startup in "$@"; do
    if [ -f "$startup" ] && grep -Fqx -- "$line" "$startup"; then
      printf 'PATH_LINE already present in %s\n' "$startup"
    else
      if [ -s "$startup" ] && [ -n "$(tail -c 1 -- "$startup")" ]; then printf '\n' >> "$startup" || return 1; fi
      printf '%s\n' "$line" >> "$startup" || return 1
      printf 'PATH_LINE added to %s\n' "$startup"
    fi
  done
}
course_install_omp
```

**Expected:** `RELEASE <tag>`, `KEEP:` or `INSTALLED`, `OMP_VERSION omp/<semver>` (observed from resolved release), and `PATH_LINE` messages for the startup files (added or already present).

**Stop:** Any STOP, checksum mismatch, unavailable/malformed release metadata or assets, wrong version vs selected tag, or write error.

**Recovery:** Keep the download folder and any existing `omp` in place. For a checksum or download error, keep the attempt and ask the owner. If the destination conflicts, ask the owner before you change anything. Do not switch assets or disable checks.

## 4. Get the course files

This command checks access to the private repository, then clones the course into the checkout at `"$HOME/Documents/AIHB_OCT_2026"`. If that folder is already a checkout of the course origin, the command leaves it unchanged and does not reset, pull, or clean it. GitHub credentials are separate from your course-site password and OpenRouter key.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window.**

```bash
course_use_checkout() {
  local origin_url checkout_top helper
  R="$HOME/Documents/AIHB_OCT_2026"
  ORIGIN="https://github.com/TheHolofex/AIHB_OCT_2026.git"
  if [ -L "$HOME/Documents" ] || [ -L "$R" ]; then printf 'STOP: Documents or checkout is a link\n' >&2; return 1; fi
  if [ ! -e "$R" ]; then
    GIT_TERMINAL_PROMPT=0 git ls-remote --exit-code "$ORIGIN" HEAD || return 1
    mkdir -p -- "$HOME/Documents" || return 1
    git clone "$ORIGIN" "$R" || { printf 'STOP: clone failed\n' >&2; return 1; }
  elif [ ! -d "$R" ]; then
    printf 'STOP: exists but not a directory\n' >&2; return 1
  else
    origin_url="$(git -C "$R" remote get-url origin 2>/dev/null || true)"
    if [ "$origin_url" != "$ORIGIN" ]; then printf 'STOP: not the course checkout\n' >&2; return 1; fi
    printf 'USE: existing checkout; no reset, pull, or clean\n'
  fi
  if [ -L "$R/.git" ]; then printf 'STOP: .git is a link\n' >&2; return 1; fi
  checkout_top="$(git -C "$R" rev-parse --show-toplevel 2>/dev/null)" || return 1
  [ "$checkout_top" = "$R" ] || { printf 'STOP: not the checkout root\n' >&2; return 1; }
  git -C "$R" rev-parse --verify HEAD >/dev/null || return 1
  M="$R/AI_Harness_Bootcamp_2/module-00-setup"
  if [ ! -f "$R/shared/run_omp.py" ] || [ ! -f "$R/shared/course_guard.mjs" ] || [ ! -f "$M/scripts/verify-setup.sh" ] || [ ! -f "$M/shared/case/verify_tool_proof.py" ]; then
    printf 'STOP: checkout missing a course helper\n' >&2; return 1
  fi
  for helper in "$R/shared/run_omp.py" "$R/shared/course_guard.mjs" "$M/scripts/verify-setup.sh" "$M/shared/case/verify_tool_proof.py"; do
    [ ! -L "$helper" ] || { printf 'STOP: helper is a link\n' >&2; return 1; }
  done
  printf 'R %s\nM %s\n' "$R" "$M"
}
course_use_checkout
```

**Expected:** For a new clone, a commit hash followed by `HEAD`, then Git's `Cloning into` progress. For an existing checkout, `USE: existing checkout; no reset, pull, or clean`. Either way, the last lines are the `R` and `M` paths under your home folder.

**Stop:** Authentication, network, or not-found error on ls-remote; any STOP from the function.

**Recovery:** Keep the error. For a network problem ask the owner. For missing credentials use the subsection below. If the account lacks access, the repository owner must invite it.

### If GitHub access fails

Check whether `gh` is present.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window.**

```bash
if command -v gh >/dev/null 2>&1; then gh --version; else printf 'GH MISSING\n'; fi
```

**Expected:** A `gh version` line or `GH MISSING`. Skip the install command when a version is shown.

**Stop:** Existing gh fails to run.

**Recovery:** Ask owner to repair existing gh. Install only when missing.

Install only with owner approval for the full upgrade. Use the official package.

**Terminal: Arch Linux, Bash or Zsh, same window; sudo elevates.**

```bash
sudo pacman -Syu --needed github-cli
```

**Expected:** Transaction completes.

**Stop:** Refused, unavailable, or conflict.

**Recovery:** Keep error; ask owner for the official package. No AUR or partial sync.

Sign in through your browser. The terminal shows a one-time code and may ask you to press Return to open the browser. Enter the code on GitHub and authorize the account invited to this repository. If the terminal asks whether to authenticate Git with your GitHub credentials, choose **No**; the next two boxes check where credentials are stored before Git uses them. Don't add `--insecure-storage`.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window; interactive login.**

```bash
gh auth login --hostname github.com --git-protocol https --web
```

**Expected:** Browser completes and the terminal confirms login for the invited account.

**Stop:** Login fails or wrong account.

**Recovery:** Stop; ask owner or account owner to resolve. Never paste a password or token.

Check status. The storage location must be approved by device policy.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window.**

```bash
gh auth status --hostname github.com
```

**Expected:** Success for invited account and approved storage.

**Stop:** Fails, wrong account, or unclear storage.

**Recovery:** Ask owner for approved credentials/storage.

Set up the helper and recheck access.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window.**

```bash
gh auth setup-git --hostname github.com &&
GIT_TERMINAL_PROMPT=0 git ls-remote --exit-code https://github.com/TheHolofex/AIHB_OCT_2026.git HEAD
```

**Expected:** A commit hash followed by `HEAD`. Now paste the step 4 box again to clone the course.

**Stop:** Either command fails. Do not clone.

**Recovery:** Keep the error. The repository owner must confirm the invitation and any organization approval for this account. After that, paste this box again, then the step 4 box.

## 5. Open a new terminal and confirm

Close the current terminal completely. Open a fresh one from the desktop menu. Do not export PATH or run commands in the old window. The new window must read the startup files and show `MISSING` for the key.

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
  if [ "$resolved" != "$HOME/.local/bin/omp" ]; then printf 'STOP: omp is not the user binary\n' >&2; return 1; fi
  version="$("$HOME/.local/bin/omp" --version 2>/dev/null)" || { printf 'STOP: installed OMP could not run\n' >&2; return 1; }
  printf 'OMP_VERSION %s\n' "${version:-missing}"
  [[ "$version" =~ ^omp/[0-9]+\.[0-9]+\.[0-9]+$ ]] || { printf 'STOP: installed OMP did not report a version number\n' >&2; return 1; }
  if [ -n "${OPENROUTER_API_KEY:-}" ]; then printf 'SET\nSTOP: this window already has the key\n' >&2; return 1; fi
  printf 'MISSING\n'
}
course_confirm_new_terminal
```

**Expected:** `R`, `M`, `PY`, `GIT_PATH`, `OMP_PATH`, `OMP_VERSION omp/<semver>`, and final line `MISSING`.

**Stop:** Any failure, wrong paths/versions, or `SET` for the key.

**Recovery:** If Python/Git/omp/ checkout problem, fix the prerequisite with the owner and repeat from the affected step, then open another fresh desktop terminal. If `SET` appears, close the window and open the next from the desktop menu without printing the key.

## 6. Enter your OpenRouter key

The launcher reads your OpenRouter key only from this terminal's environment. This box reads the key without showing it; step 7 makes it available to the commands you run here. Paste the box by itself and press Return. Then type or paste the key and press Return again; nothing appears while you do. The key exists only in this terminal process.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window.**

```bash
IFS= read -r -s OPENROUTER_API_KEY
```

**Expected:** Nothing echoed. Prompt returns after Return (may stay on same line).

**Stop:** Any character of the key appears, or you paste the key into the box.

**Recovery:** Treat displayed key as exposed. Follow [credentials](../shared/CREDENTIALS.md). Use a replacement key in a new terminal.

## 7. Confirm the key is loaded

Export makes the variable visible to programs started from this terminal. `SET` confirms a non-empty value in this process only. A closed terminal forgets the key.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window.**

```bash
export OPENROUTER_API_KEY
if [ -n "${OPENROUTER_API_KEY:-}" ]; then printf 'SET\n'; else printf 'MISSING\n'; fi
```

**Expected:** The only new line is `SET`.

**Stop:** `MISSING`, or any command prints the key value.

**Recovery:** Paste the read box again, then this box again. Never write the key to a file to keep `SET` across terminals.

## 8. Run the readiness check

Prepare a fresh attempt outside the checkout. The launcher runs the model with the key from the environment and writes only the result file. The verifier checks the token match and the write provenance. All three steps run in one paste; keep the attempt on any failure.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window.**

```bash
course_run_readiness() {
  local attempt course_exit
  unset COURSE_PROOF_VERIFIED
  if [ -z "${PY:-}" ] || [ -z "${R:-}" ]; then printf 'STOP: PY and R not set\n' >&2; return 1; fi
  if [ -L "$HOME/course-evidence" ] || [ -L "$HOME/course-evidence/reformation-qa" ]; then printf 'STOP: evidence parent linked\n' >&2; return 1; fi
  attempt="module-00-$(date -u +%Y%m%dT%H%M%SZ)-$$"
  BASE="$HOME/course-evidence/reformation-qa/$attempt"
  if [ -e "$BASE" ] || [ -L "$BASE" ]; then printf 'STOP: attempt exists\n' >&2; return 1; fi
  mkdir -p -- "$BASE/proof" "$BASE/receipts" || return 1
  EVIDENCE="$BASE/receipts/live-1"
  if [ -e "$EVIDENCE" ] || [ -L "$EVIDENCE" ]; then printf 'STOP: evidence exists\n' >&2; return 1; fi
  "$PY" -c 'import secrets; print(secrets.token_hex(16), end="")' > "$BASE/run-token.txt" || return 1
  [ "$(wc -c < "$BASE/run-token.txt" | tr -d '[:space:]')" -ge 16 ] || { printf 'STOP: token too short\n' >&2; return 1; }
  cp -- "$BASE/run-token.txt" "$BASE/proof/run-token.txt" || return 1
  cat > "$BASE/proof/prompt.txt" << 'COURSE_PROMPT'
Read run-token.txt with the course_read tool. Then write only from-omp.txt with the course_write tool. The file contents must be the words omp works, one space, and the exact token text from run-token.txt. Do not write any other file.
COURSE_PROMPT
  if [ -e "$BASE/proof/from-omp.txt" ] || [ -L "$BASE/proof/from-omp.txt" ]; then printf 'STOP: from-omp.txt exists\n' >&2; return 1; fi
  printf 'READINESS_WORK %s\nTOKEN_OUTSIDE %s\nEVIDENCE_NOT_CREATED %s\n' "$BASE/proof" "$BASE/run-token.txt" "$EVIDENCE"
  "$PY" "$R/shared/run_omp.py" --workdir "$BASE/proof" --prompt "$BASE/proof/prompt.txt" --evidence "$EVIDENCE" --allow-write from-omp.txt
  course_exit="$?"
  printf 'LAUNCH_EXIT %s\n' "$course_exit"
  if [ "$course_exit" -eq 2 ]; then printf 'STOP: prerequisite hold\n' >&2; return 2; fi
  if [ "$course_exit" -ne 0 ]; then printf 'STOP: live run failed\n' >&2; return 1; fi
  if [ ! -d "$EVIDENCE" ]; then printf 'STOP: evidence not created\n' >&2; return 1; fi
  "$PY" "$M/shared/case/verify_tool_proof.py" "$BASE/proof" "$BASE/run-token.txt" "$EVIDENCE"
  course_exit="$?"
  printf 'VERIFY_EXIT %s\n' "$course_exit"
  if [ "$course_exit" -eq 0 ]; then COURSE_PROOF_VERIFIED="$BASE"; fi
  return "$course_exit"
}
course_run_readiness
```

**Expected:** `READINESS_WORK`, `TOKEN_OUTSIDE`, `EVIDENCE_NOT_CREATED`, `LAUNCH_EXIT 0`, `READINESS CHECK PASS`, `VERIFY_EXIT 0`.

**Stop:** `LAUNCH_EXIT 2`, nonzero launch or verify exit, or STOP line.

**Recovery:** Keep the attempt. For key hold, re-enter and export in this window. For other prerequisite or failure, ask the owner with the first error from receipts. Do not edit files or reuse the attempt.

## 9. Save the setup report and read the result

The report checks prerequisites. It cannot replace the live readiness result. After the readiness passed, read the actual `from-omp.txt` bytes.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window.**

```bash
course_save_and_read() {
  if [ -z "${M:-}" ] || [ -z "${R:-}" ] || [ -z "${BASE:-}" ] || [ "${COURSE_PROOF_VERIFIED:-}" != "$BASE" ]; then
    printf 'STOP: readiness not passed in this terminal\n' >&2; return 1
  fi
  if [ -e "$BASE/setup-report.txt" ] || [ -L "$BASE/setup-report.txt" ]; then printf 'STOP: report exists\n' >&2; return 1; fi
  bash "$M/scripts/verify-setup.sh" "$R" "$BASE/setup-report.txt"
  local course_exit="$?"
  printf 'REPORT_EXIT %s\n' "$course_exit"
  [ "$course_exit" -eq 0 ] || return "$course_exit"
  if [ ! -f "$BASE/proof/from-omp.txt" ] || [ -L "$BASE/proof/from-omp.txt" ]; then printf 'STOP: result file missing or link\n' >&2; return 1; fi
  printf 'FILE %s\n' "$BASE/proof/from-omp.txt"
  cat -- "$BASE/proof/from-omp.txt" || return 1
  printf '\nEND OF FILE\n'
}
course_save_and_read
```

**Expected:** `SETUP CHECK PASS`, `REPORT_EXIT 0`, then the file path, `omp works <token>`, and `END OF FILE`.

**Stop:** Nonzero report exit, or STOP.

**Recovery:** Read the first FAIL in the report and correct only that. Keep the attempt for owner review. The readiness check remains the live proof.

## Set up local Obsidian

Obsidian lets you edit and link local notes for Module 2. Allow roughly 10 to 15 minutes. Use the signed Extra `obsidian` package from the approved full `pacman -Syu` transaction. It's the [Arch-maintained x86-64 package](https://archlinux.org/packages/extra/x86_64/obsidian/), not an AUR or vendor binary. Pacman checks signatures when it installs the package. Keep any existing profile and vaults.

If you skipped the package step even though Obsidian was missing, go back and run the approved full upgrade. Record the version pacman reports.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window; no sudo.**

```bash
pacman -Q obsidian
```

**Expected:** `obsidian` followed by the installed version (for example 1.13.7-2). **Stop:** Package missing or command fails. **Recovery:** Return to the owner-approved full-upgrade transaction.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window; no sudo.**

```bash
obsidian &
```

**Expected:** The Obsidian GUI opens in your desktop session. **Stop:** Launch error, missing display, or sandbox refusal. **Recovery:** Record `Obsidian HOLD` with the exact error. Do not add flags or change security controls.

### Open a fresh practice vault and follow its links

Use Obsidian to follow a note link, save an edit, and see a change made outside the app. Allow roughly 10 to 15 minutes. A **vault** is a local folder of notes. Use only the fresh practice folder; leave existing vaults and app profiles alone. You don't need an account, plugin, Sync, or MCP. This work makes no provider call.

Stay in the terminal where you set `PY`, `R`, and `M`. `OBS_ROOT` is outside the OMP attempt and checkout.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window; no sudo.**

```bash
course_initialize_obsidian() {
  [ -n "${PY:-}" ] && [ -n "${R:-}" ] && [ -n "${M:-}" ] || { printf 'HOLD: restore PY, R, M first.\n' >&2; return 1; }
  [ "$M" = "$R/AI_Harness_Bootcamp_2/module-00-setup" ] || return 1
  [ -f "$M/scripts/obsidian_readiness.py" ] && [ ! -L "$M/scripts/obsidian_readiness.py" ] || { printf 'HOLD: helper missing or linked.\n' >&2; return 1; }
  OBS_ROOT="$HOME/course-evidence/obsidian-arch-linux-$(date -u +%Y%m%dT%H%M%SZ)-$$"
  "$PY" "$M/scripts/obsidian_readiness.py" initialize --root "$OBS_ROOT" || return 1
  printf 'OPEN EXACT VAULT: %s\n' "$OBS_ROOT/vault"
}
course_initialize_obsidian
```

**Expected:** `Created practice vault:` and `OPEN EXACT VAULT:` name the same absolute folder ending in `/vault`.

**Stop:** HOLD, error, existing destination, or missing variable.

**Recovery:** Keep the attempt. If the terminal closed, open a new one, paste the step 5 box to restore `PY`, `R`, and `M`, then set `OBS_ROOT` to the printed path without the final `/vault` (for example `OBS_ROOT="$HOME/course-evidence/obsidian-arch-linux-..."`). Do not initialize again. Ask the checkout owner for a missing helper.

**Window: Obsidian, ordinary desktop account.**

1. Open Obsidian (from the launch step above). If another vault opens, leave it alone. Open the vault switcher, choose **Manage vaults**, then **Open folder as vault → Open**. On a first launch, choose **Open folder as vault → Open** directly.
2. Select exactly the printed `OBS_ROOT/vault` folder. Use Ctrl+L and paste the absolute path. Do not select the checkout or an existing personal vault.
3. In Settings → Community plugins keep **Restricted mode** on. Under Core plugins turn **Sync** off. Note the app version in General, then close Settings.
4. Open `Start`. Use Ctrl+E for Reading view if needed. Click its **Token** link. Read the token shown.
5. Click **Reply**. Switch to editing view with Ctrl+E if needed. Paste only the token on one line. Press Ctrl+S.

**Expected:** Links open the notes; `Reply` shows the token you read.

**Stop:** Wrong vault, empty note created, settings not local/restricted, or cannot edit/save through GUI.

**Recovery:** Leave `Start` and `Token` unchanged. Reopen the exact printed vault and follow its existing links. Record `Obsidian HOLD` for policy or display failures. A text editor edit does not count.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window; no sudo.**

```bash
"$PY" "$M/scripts/obsidian_readiness.py" check --root "$OBS_ROOT"
```

**Expected:** `Token generation 1: ...` followed by `PASS: Obsidian file round-trip; GUI observation still required`.

**Stop:** HOLD or nonzero exit.

**Recovery:** If reply does not match, correct it in Obsidian and rerun. Keep all records.

### Observe an external change, save, and reopen

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window; no sudo.**

```bash
"$PY" "$M/scripts/obsidian_readiness.py" refresh --root "$OBS_ROOT"
```

**Expected:** `Source token rotated outside Obsidian; your saved reply was preserved.`

**Stop:** HOLD or error.

**Recovery:** Keep the attempt and error; ask owner for file/permission issues.

**Window: Obsidian, same practice vault.**

1. Return to `Token` (still open or reopen via link). Confirm the token changed from the one in `Reply`.
2. Follow **Reply**, replace the old line with the new token, press Ctrl+S. Do not run refresh again.
3. Close the vault window with its close control. Launch Obsidian again from the platform step. Reopen the exact `OBS_ROOT/vault` via Manage vaults if needed.
4. Open `Start`, follow **Token**, then **Reply**. Confirm the new token is still saved.

**Expected:** External change visible, new reply saved in Obsidian, same after reopen.

**Stop:** App does not show the change, edit lost, or wrong vault reopens.

**Recovery:** Record `Obsidian HOLD` with the exact action that failed. Shell match alone does not prove the GUI steps.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window; no sudo.**

```bash
"$PY" "$M/scripts/obsidian_readiness.py" check --root "$OBS_ROOT"
```

**Expected:** `Token generation 2: ...` and `PASS: ...`, plus record path.

**Stop:** HOLD, unrefrshed token, or GUI action not seen in the window.

**Recovery:** Correct the reply in Obsidian, save, close/reopen the vault, then check again.

### Record actual Obsidian readiness

Use an ordinary text editor to create `gui-observation.txt` beside the vault at the printed `OBS_ROOT`. Record date, OS/arch, app version, exact vault path, and the two disk-record paths. Describe following the links, first edit+save, seeing the external change, second edit+save, close and reopen. Note Restricted mode on and Sync off. You may add a screenshot of the vault but omit credentials.

Write `Obsidian READY` only if both disk checks passed **and** you saw every GUI action in the Obsidian window. Otherwise write `Obsidian HOLD` and name the missing action or error. A file or `.obsidian` folder alone does not prove use of the app. Keep this record separate from OMP and n8n results.

## 10. Check Docker and the n8n destination

You need local n8n for Module 7. Keep its result separate from OMP and Obsidian. Leave time for downloads and approvals.

Use your ordinary account. Leave existing apps, contexts, containers, volumes, and attempts in place. Destination `$HOME/n8n-course` outside the checkout; you will open `http://localhost:5678`. If it exists or port 5678 is in use, mark HOLD and ask the owner. Do not delete or run over it.

The stack uses privileged Docker-in-Docker for the sandbox runner. Obtain explicit owner approval for the privilege and the software license before proceeding. If using Docker Desktop, its owner must also confirm eligibility.

Check state before contacting the daemon.

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

**Expected:** Clear state for each unit, context, overrides, destination, and listener table. Fresh machine: destination absent, no listener on 5678.

**Stop:** Remote/unfamiliar context, root account, unknown listener, existing destination, masked/failed unit, or denied inspection: HOLD.

**Recovery:** Ask owner to identify existing work and approve contact with the intended local daemon. Do not switch contexts or start unrelated services. Continue only with an existing course instance whose owner confirms its identity, stack, and version.

Inspect existing work when Docker is present.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window.**

```bash
if command -v docker >/dev/null 2>&1; then
  docker info && docker compose version && docker ps -a && docker volume ls && docker compose ls --all
else
  printf 'DOCKER missing\n'
fi
```

**Expected:** Responses and listed work. Modern `docker compose` works (5.x acceptable).

**Stop:** Permission denial, daemon failure, missing compose, or unidentified work: HOLD.

**Recovery:** Follow only the missing steps that apply. Keep compatible engine and plugin. Do not prune or replace a working engine.

## 11. Install Docker

Use official Arch packages only: `docker` and `docker-compose` from extra. The latter supplies the modern `docker compose` plugin. Check first; keep anything already working.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window.**

```bash
for package in docker docker-compose containerd runc podman-docker; do
  pacman -Q "$package" 2>/dev/null || printf '%s absent\n' "$package"
done
```

**Expected:** Each package reported as installed or absent.

**Stop:** Alternative provider, unexplained runtime install, or conflict: HOLD.

**Recovery:** Ask owner to identify the installation and dependent work. Do not replace providers or use AUR.

If anything is missing, obtain owner approval for the full `-Syu` transaction. Follow any current [Arch news](https://archlinux.org/news/) that requires manual steps.

**Terminal: Arch Linux, Bash or Zsh, same window; sudo elevates the approved full transaction.**

```bash
sudo pacman -Syu --needed docker docker-compose
```

**Expected:** Full transaction completes after you type `y` (only if approved).

**Stop:** Conflict, unapproved replacement, denial, or failure: HOLD.

**Recovery:** Keep the error. Do not use partial sync. Complete any required reboot, then recheck with step 10.

## 12. Give your account Docker access

The `docker` group grants root-equivalent control. Obtain explicit owner approval before adding your account. If denied, record HOLD; do not run as root or make the socket world-writable. If you already work with an approved daemon, keep it and skip the group step.

After the group change, sign out of the desktop completely and sign back in (new terminal alone does not refresh groups).

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same window; sudo changes approved group only.**

```bash
course_docker_access() {
  [ "$(id -u)" -ne 0 ] || { printf 'HOLD: use ordinary account\n' >&2; return 1; }
  getent group docker >/dev/null || { sudo groupadd docker || return 1; }
  sudo usermod -aG docker "$(id -un)"
}
course_docker_access
```

**Expected:** Account added without error.

**Stop:** Denied group change or unfamiliar account: HOLD.

**Recovery:** Ask owner. Never use `sudo sh`, `sudo docker`, or socket permission changes.

If the system service is inactive, start it only after owner approval of `docker.service` and dependencies. Do not alter boot or existing user services.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, fresh login; sudo starts the approved service.**

```bash
sudo systemctl start docker.service
```

**Expected:** Service starts.

**Stop:** Masked/failed unit or refusal: HOLD.

**Recovery:** Keep error; ask owner. Do not unmask or enable sockets to bypass.

In the post-login terminal, re-verify context and work.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, fresh login.**

```bash
id -un && id -nG && docker context show && docker info && docker compose version && docker ps -a && docker volume ls && docker compose ls --all
```

**Expected:** Local daemon responds without sudo, modern compose works, all work accounted for.

**Stop:** `docker info` or compose fails, wrong context, or unidentified work: HOLD.

**Recovery:** Work the first failure with the owner. Do not reinstall a working engine.

## 13. Generate the n8n configuration

Use n8n 2.41.5. The installer source checked was 1.4.0. The live URL can change, so use the review path. Download the script, page it with less, inspect it, then run only the reviewed file. The destination must be absent, even as a symlink or empty directory. The project name is fixed as `n8n-course`. The check below verifies the name is unused on this engine before recording it.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same verified window.**

```bash
course_download_n8n() {
  local attempt
  unset N8N_REVIEW_SCRIPT
  attempt="$(mktemp -d "$HOME/n8n-installer-review.XXXXXX")" || return 1
  curl -fsSL https://get.n8n.io -o "$attempt/get-n8n.sh" || { printf 'HOLD: incomplete download preserved\n' >&2; return 1; }
  [ -s "$attempt/get-n8n.sh" ] || { printf 'HOLD: empty download\n' >&2; return 1; }
  N8N_REVIEW_SCRIPT="$attempt/get-n8n.sh"
  printf 'REVIEW %s\n' "$N8N_REVIEW_SCRIPT"
}
course_download_n8n
```

**Expected:** `REVIEW` path to the completed script.

**Stop:** Failed or empty download, or changed behavior: HOLD.

**Recovery:** Keep the download. Correct with owner; create new attempt only when approved.

Page the script before executing it. Look for the line `SCRIPT_VERSION="1.4.0"`. If the version differs or the line is absent, record HOLD and ask the owner; do not run the script.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same verified window.**

```bash
less "$N8N_REVIEW_SCRIPT"
```

**Expected:** Script content visible in the pager. Press `q` to return.

**Stop:** Pager error or file changed since download.

**Recovery:** Keep the attempt; ask owner.

After review, run the reviewed script.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same verified window.**

```bash
course_run_reviewed_n8n() {
  [ "$(id -u)" -ne 0 ] || { printf 'HOLD: use ordinary account\n' >&2; return 1; }
  [ -n "${N8N_REVIEW_SCRIPT:-}" ] && [ -s "$N8N_REVIEW_SCRIPT" ] && [ ! -L "$N8N_REVIEW_SCRIPT" ] || { printf 'HOLD: no completed script\n' >&2; return 1; }
  if [ -e "$HOME/n8n-course" ] || [ -L "$HOME/n8n-course" ]; then printf 'HOLD: existing destination preserved\n' >&2; return 1; fi
  grep -qx 'SCRIPT_VERSION="1.4.0"' "$N8N_REVIEW_SCRIPT" || { printf 'HOLD: installer version changed\n' >&2; return 1; }
  N8N_DIR="$HOME/n8n-course" sh "$N8N_REVIEW_SCRIPT" --version 2.41.5 --no-start
}
course_run_reviewed_n8n
```

**Expected:** Configuration generated in fresh `$HOME/n8n-course`; containers not started.

**Stop:** Installer failure or existing-install message: HOLD.

**Recovery:** Keep all files; ask owner. Do not switch methods to bypass.

## 14. Start n8n on this computer only

Edit the generated `compose.yml` with a scripted substitution that changes exactly one occurrence of the port mapping. Verify the result. Record the fixed project name `n8n-course` only after confirming it is unused. Define the helper that enforces the record and no exported overrides. Start only after the port and project checks.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same verified window.**

```bash
course_bind_loopback() {
  local yml="$HOME/n8n-course/compose.yml"
  [ -f "$yml" ] && [ ! -L "$yml" ] || { printf 'HOLD: no ordinary compose.yml\n' >&2; return 1; }
  local count_orig
  count_orig=$(grep -oF -- "- '5678:5678'" "$yml" | wc -l | tr -d '[:space:]')
  if [ "$count_orig" -ne 1 ]; then
    printf 'HOLD: expected exactly one 5678:5678, saw %s\n' "$count_orig" >&2; return 1
  fi
  sed -i "s/'5678:5678'/'127.0.0.1:5678:5678'/" "$yml" || return 1
  local count_old count_new
  count_old=$(grep -oF -- "- '5678:5678'" "$yml" | wc -l | tr -d '[:space:]')
  count_new=$(grep -oF -- "- '127.0.0.1:5678:5678'" "$yml" | wc -l | tr -d '[:space:]')
  if [ "$count_old" -ne 0 ] || [ "$count_new" -ne 1 ]; then
    printf 'HOLD: substitution did not produce exactly one loopback binding\n' >&2; return 1
  fi
  printf 'PORT_BOUND 127.0.0.1:5678:5678\n'
}
course_bind_loopback
```

**Expected:** `PORT_BOUND 127.0.0.1:5678:5678`

**Stop:** Any count other than exactly one original, or substitution not producing exactly one new binding: HOLD.

**Recovery:** Keep the directory and ask the owner. Do not edit by hand or rerun the installer to bypass the check.

Record the fixed project name after verifying it is unused on this engine and has no resources.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same verified window.**

```bash
course_n8n_identify() {
  local project="n8n-course" containers volumes networks
  local LC_ALL=C
  if [ ! -d "$HOME/n8n-course" ] || [ -L "$HOME/n8n-course" ]; then printf 'HOLD: expected ordinary fresh n8n-course\n' >&2; return 1; fi
  if [ -e "$HOME/n8n-course/.course-project" ] || [ -L "$HOME/n8n-course/.course-project" ]; then printf 'HOLD: existing project record preserved\n' >&2; return 1; fi
  containers=$(docker ps -aq --filter "label=com.docker.compose.project=$project")
  [ $? -eq 0 ] || { printf 'HOLD: container inspection failed\n' >&2; return 1; }
  volumes=$(docker volume ls -q --filter "label=com.docker.compose.project=$project")
  [ $? -eq 0 ] || { printf 'HOLD: volume inspection failed\n' >&2; return 1; }
  networks=$(docker network ls -q --filter "label=com.docker.compose.project=$project")
  [ $? -eq 0 ] || { printf 'HOLD: network inspection failed\n' >&2; return 1; }
  if [ -n "$containers" ] || [ -n "$volumes" ] || [ -n "$networks" ]; then
    printf 'HOLD: project name already has Docker resources\n' >&2; return 1
  fi
  (
    umask 077
    set -o noclobber
    printf '%s\n' "$project" > "$HOME/n8n-course/.course-project"
  ) || { printf 'HOLD: project record could not be saved\n' >&2; return 1; }
  printf 'PROJECT recorded: %s\n' "$project"
}
course_n8n_identify
```

**Expected:** `PROJECT recorded: n8n-course`

**Stop:** Existing record, resources under the name, or write failure: HOLD.

**Recovery:** Keep everything; ask owner. Do not delete to retry.

Define the helper (paste once per shell).

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same verified window.**

```bash
course_n8n() {
  local variable conflict=0 project
  local LC_ALL=C
  for variable in N8N_VERSION N8N_SANDBOX_VERSION N8N_RUNNERS_AUTH_TOKEN SEARXNG_SECRET COMPOSE_PROJECT_NAME COMPOSE_FILE COMPOSE_ENV_FILES COMPOSE_DISABLE_ENV_FILE COMPOSE_PROFILES; do
    if printenv "$variable" >/dev/null 2>&1; then printf 'HOLD: %s\n' "$variable" >&2; conflict=1; fi
  done
  [ "$conflict" -eq 0 ] || return 1
  if [ -L "$HOME/n8n-course" ] || [ -L "$HOME/n8n-course/.course-project" ] || [ ! -f "$HOME/n8n-course/.course-project" ]; then
    printf 'HOLD: project record missing or linked\n' >&2; return 1
  fi
  project="$(cat "$HOME/n8n-course/.course-project")" || { printf 'HOLD: could not read project record\n' >&2; return 1; }
  case "$project" in ''|[!a-z0-9]*|*[!a-z0-9_-]*) printf 'HOLD: invalid recorded project name\n' >&2; return 1 ;; esac
  docker compose -p "$project" --env-file "$HOME/n8n-course/.env" -f "$HOME/n8n-course/compose.yml" "$@"
}
```

**Expected:** Prompt returns with no output.

**Stop:** HOLD or error from the definition.

**Recovery:** Trace exported variables in a clean shell with the owner. Keep the directory; do not create a new identity.

Recheck the port (fresh instance must have none).

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same verified window.**

```bash
ss -ltn 'sport = :5678'
```

**Expected:** No listener rows.

**Stop:** Unidentified listener: HOLD.

**Recovery:** Ask its owner; do not kill or change another app's port.

Start the stack.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same verified window.**

```bash
course_n8n up -d
```

**Expected:** Images download and stack starts (first pull can take minutes).

**Stop:** Port, pull, permission, or startup error: HOLD.

**Recovery:** Keep files and volumes; ask owner for the exact cause. Do not prune or upgrade.

Inspect state.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same verified window.**

```bash
course_n8n ps --all &&
course_n8n port n8n 5678 &&
course_n8n exec -T n8n n8n --version
```

**Expected:** All six services. `sandbox-certs` Exited (0). Others running; `sandbox-api` healthy. Port `127.0.0.1:5678`. n8n `2.41.5`.

**Stop:** Missing service, nonzero cert exit, restart loop, non-loopback port, or wrong version: HOLD.

**Recovery:** Let initialization settle and check again. Leave state for owner. Do not silently change pin or port.

## 15. Save a blank workflow and confirm it persists

Open `http://localhost:5678`. If this is a fresh instance, complete the owner setup with a local name, email, and password. For an existing instance, use its login. Keep Assistant off and do not enter any OpenRouter key.

Select Overview → Build a workflow (or Create workflow). Name it **Module 7 readiness**. Keep the canvas blank. Do not Publish. Reload the page and confirm that the name and empty canvas remain.

**Expected:** Named blank workflow reopens after reload and is unpublished.

**Stop:** Cloud login, external key, missing workflow, unexpected owner screen, or different UI: HOLD.

**Recovery:** Check URL and version. Keep instance; ask owner. Do not reset owner account.

Stop only this stack (data volume stays).

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same verified window.**

```bash
course_n8n down
```

**Expected:** Containers and network stop; data volume remains. Browser page unavailable after reload.

**Stop:** Unexpected project or error: HOLD.

**Recovery:** Keep output; never use `-v`.

Start the stack again and inspect it.

**Terminal: Arch Linux, Bash or Zsh, ordinary user, same verified window.**

```bash
course_n8n up -d &&
course_n8n ps --all &&
course_n8n port n8n 5678 &&
course_n8n exec -T n8n n8n --version
```

**Expected:** Same state, port, version as before. Reload browser, use existing login if prompted, reopen the readiness workflow: name and blank canvas persist, still unpublished.

**Stop:** Missing data, new owner screen, wrong version/port, or failed services: HOLD.

**Recovery:** Keep directory and volumes; ask owner. Do not create another account or workflow to hide a failure. The n8n result is independent of OMP.

## Later sessions

After a restart, Docker and the n8n stack stay stopped, and a new terminal doesn't know the `course_n8n` helper. Before Module 7, open a new terminal and paste these boxes again, in order: `sudo systemctl start docker.service` from [step 12](#12-give-your-account-docker-access), then the `course_n8n` helper box, the `course_n8n up -d` box, and the inspect box from [step 14](#14-start-n8n-on-this-computer-only). The data volume keeps your workflow, so sign in with your existing local owner account.

## If a step stops

The list below is organized by the step that produced the first error. Keep the exact error, attempt folder, and last observed state. Ask the device or course owner with that evidence. Never delete, rename, or overwrite an existing attempt, checkout, vault, or n8n directory to "start fresh."

- Computer check or Python below 3.12: free space or ask owner for a supported Arch x86_64 desktop with ordinary account and current python package.
- Package transaction refused or conflicting: keep the exact pacman output; only the owner can approve the full `-Syu`.
- OMP checksum or install stop: keep the download folder; ask owner to resolve source or transfer. Do not replace or switch assets.
- GitHub ls-remote or clone stop: keep the error. Network: owner. Credentials: use the gh subsection exactly once per failure mode. Invitation must come from the repository owner.
- New terminal shows `SET` or wrong paths: close it and open the next from the desktop menu. Never export in the diagnostic window.
- Key read or export fails to produce `SET`: re-paste the read box, then export. Treat any visible key as exposed per CREDENTIALS.md.
- Readiness launch or verify fails: keep the attempt folder and its receipts. The first printed failure is the one to correct. Do not edit `from-omp.txt` or reuse the folder.
- Report or read-back fails: the readiness check is still the live proof. Correct only the named prerequisite; do not clean the checkout.
- Obsidian package or launch: return to the approved pacman transaction or record HOLD with the GUI error. Never add `--no-sandbox` or overwrite an existing install.
- Obsidian GUI steps cannot be performed or observed: record `Obsidian HOLD` with the exact missing action. The disk checks alone are not sufficient.
- Docker preflight, install, or access: keep existing work. Only the owner approves group membership or service start. Re-login after group change.
- n8n destination or port occupied: ask owner to identify the owner of `$HOME/n8n-course` or listener. Do not delete or kill.
- n8n generate or bind substitution fails the exactly-one check: keep the directory; the verification is strict. Ask owner.
- n8n start or workflow does not persist: keep the directory, volumes, and `.course-project`. Use only `course_n8n` for lifecycle. The saved blank workflow after down/up is required for Module 7.


## Local model (capstone) readiness lane

Ask staff for the approved `hf` and `llama-server` paths, then [check local-model readiness](../../module-10-capstone/shared/MODULE_10_LAB.md#check-local-model-readiness-before-downloading) before a download and again before launch. Quoted executable paths support spaces. Missing tools, insufficient capacity, an occupied endpoint, or an unresolved failed rehearsal mean **Local model HOLD**; preserve your other readiness results and contact the device/support owner.

See also [shared/TROUBLESHOOTING.md](../shared/TROUBLESHOOTING.md) and [shared/CREDENTIALS.md](../shared/CREDENTIALS.md) for cross-platform cases. Record every HOLD with the concrete symptom and the attempt path; a later prerequisite report cannot replace an earlier live check.