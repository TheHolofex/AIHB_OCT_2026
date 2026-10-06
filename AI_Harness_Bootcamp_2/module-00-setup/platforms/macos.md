# Set up on macOS

This setup takes your Mac from a fresh terminal window to a working Oh My Pi (OMP) install that reads and writes a file through the course launcher. Plan for 45 to 90 minutes, plus download time. You'll need the Terminal app, a browser, a plain text editor, 15 GB free in your home folder, and permission to install missing tools. Keep your work under your home folder, outside the course checkout. If device policy blocks a step, stop and use the [support packet](../shared/TROUBLESHOOTING.md).

The work has three parts. Steps 1 to 9 install the tools and run the OMP readiness check. **Set up local Obsidian** prepares the note app for Module 2. **Prepare local n8n for Module 7** prepares the local workflow editor. Paste each box whole into Terminal. Your Mac's default shell is zsh, but the boxes also work in Bash. If a box prints `STOP` or `HOLD`, read its **Recovery** note. For other problems, see [If a step stops](#if-a-step-stops).

## 1. Check this Mac

Open **Terminal** from **Applications → Utilities** while you're signed in to your ordinary account. This box checks your macOS version, chip, shell, and free space, then lists any missing tools. It doesn't install anything or run Apple's `git` or `python3` placeholders, which could open an install dialog.

This setup needs macOS 15 or newer, the same minimum as [Homebrew](https://docs.brew.sh/Installation). Apple silicon is fully supported. Homebrew treats Intel Macs as [Tier 3](https://docs.brew.sh/Support-Tiers), which means they may work but get less support.

**Terminal: macOS Terminal, zsh or Bash, ordinary user, first window.**

```bash
course_find_python() {
  local candidate found
  for candidate in python3.12 python3 python; do
    case "$(command -v "$candidate" 2>/dev/null)" in
      '') continue ;;
      /usr/bin/*) xcode-select -p >/dev/null 2>&1 || continue ;;
    esac
    found="$("$candidate" -c 'import os, sys; sys.exit(1) if sys.version_info < (3, 12) else print(os.path.abspath(sys.executable))' 2>/dev/null)" || continue
    printf '%s\n' "$found"
    return 0
  done
  return 1
}
course_git_works() {
  if xcode-select -p >/dev/null 2>&1 || [ "$(command -v git)" != /usr/bin/git ]; then
    git --version 2>/dev/null
  else
    return 1
  fi
}
course_check_mac() {
  local free_kb todo
  MACOS_VERSION="$(sw_vers -productVersion)" || return 1
  ARCH="$(uname -m)"
  printf 'MACOS %s\nARCH %s\n' "$MACOS_VERSION" "$ARCH"
  if [ "${MACOS_VERSION%%.*}" -lt 15 ]; then
    printf 'STOP: this setup needs macOS 15 or newer\n' >&2
    return 1
  fi
  if [ "$(sysctl -in sysctl.proc_translated 2>/dev/null)" = 1 ]; then
    printf 'STOP: Terminal is running through Rosetta; reopen it natively\n' >&2
    return 1
  fi
  case "$ARCH" in
    arm64) BREW=/opt/homebrew/bin/brew; ASSET=omp-darwin-arm64 ;;
    x86_64) BREW=/usr/local/bin/brew; ASSET=omp-darwin-x64 ;;
    *) printf 'STOP: unsupported architecture\n' >&2; return 1 ;;
  esac
  if [ -n "${ZSH_VERSION:-}" ]; then
    SETUP_SHELL=zsh
  elif [ -n "${BASH_VERSION:-}" ]; then
    SETUP_SHELL=bash
  else
    printf 'STOP: use zsh or Bash\n' >&2
    return 1
  fi
  printf 'SHELL %s\nACCOUNT %s\n' "$SETUP_SHELL" "$(id -un)"
  if [ ! -d "$HOME" ] || [ ! -w "$HOME" ]; then
    printf 'STOP: your home folder is not writable\n' >&2
    return 1
  fi
  free_kb="$(df -Pk "$HOME" | awk 'NR==2 {print $4}')"
  if [ -z "$free_kb" ] || [ "$free_kb" -lt 15728640 ]; then
    printf 'STOP: less than 15 GB is free in your home folder\n' >&2
    return 1
  fi
  printf 'FREE_GB %s\n' "$((free_kb / 1048576))"
  if [ -x "$BREW" ]; then
    eval "$("$BREW" shellenv "$SETUP_SHELL")" || return 1
    printf 'HOMEBREW %s\n' "$BREW"
  else
    printf 'HOMEBREW not installed\n'
  fi
  todo=
  course_git_works || todo="git"
  if PY="$(course_find_python)"; then
    printf 'PYTHON %s\n' "$PY"
  else
    PY=
    todo="${todo:+$todo }python"
  fi
  if [ -n "$todo" ]; then
    printf 'TO INSTALL: %s\n' "$todo"
  else
    printf 'NOTHING TO INSTALL\n'
  fi
}
course_check_mac
```

**Expected:** Lines for `MACOS`, `ARCH`, `SHELL`, `ACCOUNT`, and `FREE_GB`, then a Git version and a `PYTHON` path if those work. The last line is `NOTHING TO INSTALL` or `TO INSTALL:` followed by `git`, `python`, or both.

**Stop:** Any `STOP` line.

**Recovery:** Fix the condition it names, then paste this box again. For Rosetta, an old macOS, or low space, see [Tools and Homebrew](#tools-and-homebrew).

## 2. Install Git and Python

**Git** copies the course files from GitHub to your Mac and records exactly which version you have. Step 4 uses it to make your checkout. On a Mac, Git comes with Apple's Command Line Tools, a free set of developer tools. The [Git project](https://git-scm.com/install/mac) lists these tools and Homebrew as ways to install it, and this step uses both.

If step 1 printed `NOTHING TO INSTALL`, skip the install box and go to [Confirm Git works](#confirm-git-works). Otherwise, this box installs [Homebrew](https://brew.sh/), a package manager for macOS, if needed. If Apple's Command Line Tools are missing, the Homebrew installer adds them, and Git comes with them. The box installs Homebrew's `git` only if Git still doesn't run after that. Then it installs [Python 3.12](https://formulae.brew.sh/formula/python@3.12) if Python is missing.

The Homebrew installer lists what it will change, asks you to press **Return**, and asks for your administrator password. The password won't appear as you type. If an Apple dialog opens, click **Install**, wait for it to finish, then return to Terminal and press a key. The installer needs an administrator account. Never run `sudo brew`.

On an Intel Mac, Homebrew no longer publishes ready-built Python packages, so `python@3.12` compiles from source and can take a long time. Intel users can [install Python from python.org instead](#tools-and-homebrew).

**Terminal: macOS Terminal, zsh or Bash, ordinary user, same window; the installer may ask for administrator approval.**

```bash
course_install_missing() {
  if [ -z "${BREW:-}" ] || [ -z "${SETUP_SHELL:-}" ]; then
    printf 'STOP: paste the step 1 box in this window first\n' >&2
    return 1
  fi
  if [ ! -x "$BREW" ]; then
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" || {
      printf 'STOP: the Homebrew installer did not finish\n' >&2
      return 1
    }
  fi
  if [ ! -x "$BREW" ]; then
    printf 'STOP: Homebrew is not at %s\n' "$BREW" >&2
    return 1
  fi
  eval "$("$BREW" shellenv "$SETUP_SHELL")" || return 1
  "$BREW" --version || return 1
  if ! course_git_works >/dev/null; then
    "$BREW" install git || return 1
  fi
  course_git_works || { printf 'STOP: Git still does not run\n' >&2; return 1; }
  if ! PY="$(course_find_python)"; then
    "$BREW" install python@3.12 || return 1
    PY="$(course_find_python)" || { printf 'STOP: Python 3.12 or newer still does not run\n' >&2; return 1; }
  fi
  "$PY" --version || return 1
  printf 'TOOLS READY %s\n' "$PY"
}
course_install_missing
```

**Expected:** A Homebrew version, a Git version, a Python version of 3.12 or newer, and then `TOOLS READY` with the Python path.

**Stop:** The installer fails or you can't approve it, or any `STOP` line appears.

**Recovery:** Keep the first error and don't install anything else by hand. If you don't have an administrator account, ask the device owner to finish this step; see [Tools and Homebrew](#tools-and-homebrew).

If you installed Homebrew, follow its **Next steps** to add `brew shellenv` to your shell startup file. This keeps Homebrew and its Python available after you restart Terminal.

### Confirm Git works

This box shows which Git your Terminal window finds and asks it for its version. Run it even if you skipped the install box.

**Terminal: macOS Terminal, zsh or Bash, ordinary user, same window.**

```bash
command -v git && git --version
```

**Expected:** a path, usually `/usr/bin/git` for Apple's Git or `/opt/homebrew/bin/git` for Homebrew's (`/usr/local/bin/git` on an Intel Mac), then `git version 2.` followed by more numbers. Apple's Git also shows `(Apple Git-` and a build number.

**Stop:** the box prints nothing, Terminal prints `xcode-select: note: No developer tools were found` instead of a version, or an Apple dialog offers to install the command line developer tools.

**Recovery:** That Apple dialog is Apple's Git installer. If you're allowed to install software, click **Install**, wait for it to finish, and paste this box again. Otherwise, ask the device owner to finish the installation. If no dialog appeared, paste the step 2 box again and keep its first error; see [Tools and Homebrew](#tools-and-homebrew).

## 3. Install Oh My Pi

Run the one-line installer from [omp.sh](https://omp.sh/).

**Terminal: Bash or zsh, ordinary user.**

```bash
curl -fsSL https://omp.sh/install | sh
```

**Restart your terminal after installing OMP so PATH changes take effect.** Follow any PATH instructions the installer prints, complete Step 4 in this window, then close and reopen your terminal as directed in Step 5 before starting OMP or entering your API key.

**Expected:** The installer finishes successfully. In the new terminal, `omp --version` prints the installed version.

**Stop:** The installer reports an error or `omp` is not found.

**Recovery:** Check the installer’s error. For `omp` not found, use [PATH recovery](../shared/TROUBLESHOOTING.md#if-omp-is-not-found-after-restarting), then reopen the terminal and try `omp --version` again.

## 4. Get the course files

This box checks whether your existing Git credentials can read the private course repository. It won't prompt for a login or change your credential settings. If you have access, it clones the repository to `~/Documents/AIHB_OCT_2026`. If the same repository is already there, it keeps that checkout without pulling, resetting, or cleaning it.

**Terminal: macOS Terminal, zsh or Bash, ordinary user, same window.**

```bash
course_get_checkout() {
  R="$HOME/Documents/AIHB_OCT_2026"
  M="$R/AI_Harness_Bootcamp_2/module-00-setup"
  if ! GIT_TERMINAL_PROMPT=0 git ls-remote --exit-code https://github.com/TheHolofex/AIHB_OCT_2026.git HEAD; then
    printf 'ACCESS HOLD: set up GitHub access below, then paste this box again\n' >&2
    return 1
  fi
  if [ -L "$HOME/Documents" ] || [ -L "$R" ]; then
    printf 'STOP: the checkout path is a symlink; nothing was changed\n' >&2
    return 1
  fi
  if [ ! -e "$R" ]; then
    git clone https://github.com/TheHolofex/AIHB_OCT_2026.git "$R" || return 1
  elif [ -d "$R/.git" ] && [ "$(git -C "$R" remote get-url origin 2>/dev/null)" = https://github.com/TheHolofex/AIHB_OCT_2026.git ] && git -C "$R" rev-parse --verify HEAD >/dev/null 2>&1; then
    printf 'KEEP: using the existing checkout without changing it\n'
  else
    printf 'STOP: %s holds other or incomplete work; it was not changed\n' "$R" >&2
    return 1
  fi
  if [ ! -f "$R/shared/run_omp.py" ] || [ ! -f "$M/shared/case/verify_tool_proof.py" ] || [ ! -f "$M/scripts/verify-setup.sh" ]; then
    printf 'STOP: the checkout is missing course files\n' >&2
    return 1
  fi
  printf 'CHECKOUT READY %s\n' "$R"
}
course_get_checkout
```

**Expected:** A commit ID followed by `HEAD`, then clone progress or `KEEP:`, and finally `CHECKOUT READY` with the checkout path.

**Stop:** `ACCESS HOLD`, a clone failure, or any `STOP` line.

**Recovery:** For `ACCESS HOLD`, use the GitHub CLI boxes below. For an occupied path, see [GitHub access and the checkout](#github-access-and-the-checkout).

### If GitHub access fails

Use these three boxes only after `ACCESS HOLD`. The [GitHub CLI](https://cli.github.com/manual/gh_auth_login), `gh`, signs you in through your browser. It lets Git use that sign-in for github.com. Your GitHub account is separate from your course-site password and your OpenRouter key. If Homebrew isn't installed, paste the step 2 box first. It installs Homebrew even when nothing else is missing.

**Terminal: macOS Terminal, zsh or Bash, ordinary user, same window.**

```bash
course_get_gh() {
  if command -v gh >/dev/null 2>&1; then
    gh --version
    return
  fi
  if [ ! -x "${BREW:-}" ]; then
    printf 'STOP: install Homebrew with the step 2 box first\n' >&2
    return 1
  fi
  "$BREW" install gh || return 1
  eval "$("$BREW" shellenv "$SETUP_SHELL")" || return 1
  gh --version
}
course_get_gh
```

**Expected:** A `gh version` line.

**Stop:** The install fails or `gh` still isn't found.

**Recovery:** Correct the Homebrew problem the error names; never install with `sudo`.

Sign in with the GitHub account that was invited to the course repository. The command first asks **Authenticate Git with your GitHub credentials?**; press **Return** to accept. It then shows a one-time code and waits at **Press Enter to open github.com in your browser**. Press **Return**, enter the code in the browser, and approve the sign-in.

**Terminal: macOS Terminal, zsh or Bash, ordinary user, same window; interactive browser login.**

```bash
gh auth login --hostname github.com --git-protocol https --web
```

**Expected:** The browser approval finishes, and the terminal reports that you're logged in.

**Stop:** The login fails, or the wrong account is signed in.

**Recovery:** Keep the error private and ask the device owner for approved credentials. Don't use `--insecure-storage`.

Check the signed-in account, let Git use it for github.com, and test access again. Keep this output private.

**Terminal: macOS Terminal, zsh or Bash, ordinary user, same window.**

```bash
gh auth status --hostname github.com &&
gh auth setup-git --hostname github.com &&
GIT_TERMINAL_PROMPT=0 git ls-remote --exit-code https://github.com/TheHolofex/AIHB_OCT_2026.git HEAD
```

**Expected:** The invited account shows as active, followed by a commit ID and `HEAD`. Now paste the step 4 box again.

**Stop:** Any command fails, or `gh auth status` reports plaintext storage that your device policy doesn't allow.

**Recovery:** Ask the repository owner to confirm your invitation, or ask the device owner to set up approved credential storage. Don't run `--show-token` or share the output.

## 5. Open a new terminal and confirm

A new window shows whether your startup files work on their own. In Terminal, choose **Shell → New Window**. Don't type `zsh` or `bash` in the old window, because a shell started there inherits the old settings. This box sets `R`, `M`, and `PY` again, finds Python, Git, and `omp` by name, and checks that no key is present yet.

**Terminal: macOS Terminal, zsh or Bash, ordinary user, new window opened from the Shell menu.**

```bash
course_confirm_new_terminal() {
  local candidate found omp_path version
  R="$HOME/Documents/AIHB_OCT_2026"
  M="$R/AI_Harness_Bootcamp_2/module-00-setup"
  PY=
  for candidate in python3.12 python3 python; do
    case "$(command -v "$candidate" 2>/dev/null)" in
      '') continue ;;
      /usr/bin/*) xcode-select -p >/dev/null 2>&1 || continue ;;
    esac
    found="$("$candidate" -c 'import os, sys; sys.exit(1) if sys.version_info < (3, 12) else print(os.path.abspath(sys.executable))' 2>/dev/null)" || continue
    PY="$found"
    break
  done
  if [ -z "$PY" ]; then
    printf 'STOP: no Python 3.12 or newer is on PATH in this window\n' >&2
    return 1
  fi
  printf 'PYTHON %s\n' "$PY"
  "$PY" --version || return 1
  printf 'GIT_PATH %s\n' "$(command -v git)"
  git --version || return 1
  omp_path="$(command -v omp)"
  printf 'OMP_PATH %s\n' "${omp_path:-missing}"
  case "$omp_path" in /*) ;; *) printf 'STOP: omp is not on PATH\n' >&2; return 1 ;; esac
  version="$("$omp_path" --version 2>/dev/null)"
  printf 'OMP_VERSION %s\n' "${version:-missing}"
  [[ "$version" =~ ^omp/[0-9]+\.[0-9]+\.[0-9]+$ ]] || { printf 'STOP: installed OMP did not report a version number\n' >&2; return 1; }
  if [ ! -f "$R/shared/run_omp.py" ] || [ ! -f "$M/shared/case/verify_tool_proof.py" ] || [ ! -f "$M/scripts/verify-setup.sh" ]; then
    printf 'STOP: the course checkout is missing or incomplete\n' >&2
    return 1
  fi
  printf 'CHECKOUT %s\n' "$R"
  if [ -n "${OPENROUTER_API_KEY:-}" ]; then
    printf 'SET\n'
    printf 'STOP: this window already has a key; open a new window from the Shell menu\n' >&2
    return 1
  fi
  printf 'MISSING\n'
}
course_confirm_new_terminal
```

**Expected:** `PYTHON` with an absolute path and version 3.12 or newer, a Git path and version, `OMP_PATH` with the installed command path, `OMP_VERSION omp/<semver>`, `CHECKOUT`, and `MISSING` as the last line.

**Stop:** Any `STOP` line, or `SET`.

**Recovery:** Correct the startup setting in your earlier window, then open another new terminal window and paste this box again. Don't add an `export` here to make it pass; see [New terminal and key](#new-terminal-and-key).

## 6. Enter your OpenRouter key

Use the OpenRouter key you were given for this course. The next box reads the key without showing it. Paste the box and press **Return**. Terminal is now waiting for the key, even though nothing seems to happen. Paste the key and press **Return** again. The characters won't appear. The key stays in this window only and isn't saved to a file.

**Terminal: macOS Terminal, zsh or Bash, ordinary user, same new window.**

```bash
IFS= read -r -s OPENROUTER_API_KEY
```

**Expected:** The prompt returns, and the key doesn't appear on screen.

**Stop:** The key appears on screen, or you aren't sure where the typing went.

**Recovery:** Press **Control-C** and follow the [credential handling procedure](../shared/CREDENTIALS.md). Revoke any key that was shown. Don't paste the next box while this one is still waiting.

## 7. Confirm the key is loaded

`export` lets programs started from this window, such as the readiness check, use the key. `SET` shows that the key is present. It doesn't show that the key works.

**Terminal: macOS Terminal, zsh or Bash, ordinary user, same window.**

```bash
export OPENROUTER_API_KEY
if [ -n "${OPENROUTER_API_KEY:-}" ]; then printf 'SET\n'; else printf 'MISSING\n'; fi
```

**Expected:** Only `SET`.

**Stop:** `MISSING`, or the key itself appears on screen.

**Recovery:** Paste the step 6 box again, then this box. Never save the key in a startup file, command, or evidence file.

## 8. Run the readiness check

This box makes a fresh attempt folder under `~/course-evidence`, with a random token and a prompt. The token marks this attempt; it isn't a credential. The box then runs the course launcher. The launcher uses only OpenRouter and `openrouter/anthropic/claude-sonnet-4.6`. It lets the model write only `from-omp.txt`. Last, the checker confirms that the file holds `omp works` plus this attempt's token and that the saved receipts show `course_write` wrote it.

**Terminal: macOS Terminal, zsh or Bash, ordinary user, same window.**

```bash
course_readiness_check() {
  local course_exit
  unset COURSE_PROOF_VERIFIED
  if [ -z "${PY:-}" ] || [ -z "${R:-}" ] || [ -z "${M:-}" ]; then
    printf 'STOP: paste the step 5 box in this window first\n' >&2
    return 1
  fi
  if [ -z "${OPENROUTER_API_KEY:-}" ]; then
    printf 'STOP: the key is MISSING; repeat steps 6 and 7\n' >&2
    return 1
  fi
  if [ -L "$HOME/course-evidence" ]; then
    printf 'STOP: course-evidence is a symlink\n' >&2
    return 1
  fi
  BASE="$HOME/course-evidence/setup-proof-$(date -u +%Y%m%dT%H%M%SZ)-$$"
  EVIDENCE="$BASE/receipts"
  mkdir -p "$HOME/course-evidence" && mkdir "$BASE" && mkdir "$BASE/proof" || {
    printf 'STOP: could not create a fresh attempt folder\n' >&2
    return 1
  }
  "$PY" -c 'import secrets; print(secrets.token_hex(16))' > "$BASE/run-token.txt" || return 1
  cp "$BASE/run-token.txt" "$BASE/proof/run-token.txt" || return 1
  printf '%s\n' 'Read run-token.txt with the course_read tool. Then write only from-omp.txt with the course_write tool. The file contents must be the words omp works, one space, and the exact token text from run-token.txt. Do not write any other file.' > "$BASE/proof/prompt.txt" || return 1
  printf 'READINESS_WORK %s\n' "$BASE/proof"
  "$PY" "$R/shared/run_omp.py" --workdir "$BASE/proof" --prompt "$BASE/proof/prompt.txt" --evidence "$EVIDENCE" --allow-write from-omp.txt
  course_exit="$?"
  printf 'LAUNCH_EXIT %s\n' "$course_exit"
  if [ "$course_exit" -ne 0 ]; then
    printf 'STOP: the launcher did not finish; keep this attempt\n' >&2
    return "$course_exit"
  fi
  "$PY" "$M/shared/case/verify_tool_proof.py" "$BASE/proof" "$BASE/run-token.txt" "$EVIDENCE"
  course_exit="$?"
  printf 'VERIFY_EXIT %s\n' "$course_exit"
  if [ "$course_exit" -eq 0 ]; then COURSE_PROOF_VERIFIED="$BASE"; fi
  return "$course_exit"
}
course_readiness_check
```

**Expected:** `READINESS_WORK` with the attempt path, the launcher's output, `LAUNCH_EXIT 0`, then `READINESS CHECK PASS` and `VERIFY_EXIT 0`.

**Stop:** `LAUNCH_EXIT 2` means a prerequisite such as the key is missing. `LAUNCH_EXIT 1` means the live run failed. `READINESS CHECK HOLD` or a nonzero `VERIFY_EXIT` means the result didn't pass.

**Recovery:** Keep the attempt folder, and don't write `from-omp.txt` yourself. Fix the first reported problem, then paste this box again; it makes a new attempt. See [Readiness check and report](#readiness-check-and-report).

## 9. Save the setup report and read the result

The setup report checks your tools, checkout, and key presence. It saves what it found beside your attempt. The report can't replace the readiness check, so this box reads the result file only after step 8 passed in this window. Changed files in the checkout are reported for your information; don't clean them up.

**Terminal: macOS Terminal, zsh or Bash, ordinary user, same window.**

```bash
course_report_and_read() {
  local course_exit
  if [ -z "${BASE:-}" ] || [ -z "${M:-}" ] || [ -z "${R:-}" ]; then
    printf 'STOP: run step 8 in this window first\n' >&2
    return 1
  fi
  bash "$M/scripts/verify-setup.sh" "$R" "$BASE/setup-report.txt"
  course_exit="$?"
  printf 'REPORT_EXIT %s\n' "$course_exit"
  if [ "${COURSE_PROOF_VERIFIED:-}" != "$BASE" ]; then
    printf 'STOP: this attempt has not passed the readiness check\n' >&2
    return 1
  fi
  if [ ! -f "$BASE/proof/from-omp.txt" ] || [ -L "$BASE/proof/from-omp.txt" ]; then
    printf 'STOP: the result file is missing or linked\n' >&2
    return 1
  fi
  printf 'FILE %s\n' "$BASE/proof/from-omp.txt"
  cat "$BASE/proof/from-omp.txt" || return 1
  printf '\nEND OF FILE\n'
  return "$course_exit"
}
course_report_and_read
```

**Expected:** `SETUP CHECK PASS` with the report path and `REPORT_EXIT 0`, then `FILE`, the line `omp works` followed by this attempt's token, and `END OF FILE`. The report doesn't contain your key.

**Stop:** `SETUP CHECK HOLD`, a nonzero `REPORT_EXIT`, or any `STOP` line.

**Recovery:** Read the first `FAIL` line in the report and correct only that item. If you need another report, run step 8 again so the report goes into a new attempt folder. A passing report doesn't make a failed readiness check pass.

## Set up local Obsidian

Obsidian is the note app you'll use in Module 2. Allow 20 to 35 minutes. You'll install it if needed, then show in the app that you can follow links, save an edit, see a change made outside the app, and reopen the same vault. A **vault** is a folder of notes. This work uses no API key and makes no model call.

If Obsidian is already installed in **Applications** or in your home folder's **Applications**, use that copy, skip the download box, and record its version later. Don't replace it only to match 1.13.7, and leave its existing vaults and settings alone.

### Install Obsidian if it is missing

This box downloads the official universal 1.13.7 disk image for Apple silicon and Intel into a new folder. It checks the image against its published SHA-256 fingerprint and opens it only if the fingerprints match. See the [release assets](https://github.com/obsidianmd/obsidian-releases/releases/tag/v1.13.7) and the [installation instructions](https://github.com/obsidianmd/obsidian-help/blob/master/en/Getting%20started/Download%20and%20install%20Obsidian.md).

**Terminal: macOS Terminal, zsh or Bash, ordinary user, no sudo; only when Obsidian is not installed.**

```bash
course_get_obsidian() {
  local app folder dmg actual
  for app in /Applications/Obsidian.app "$HOME/Applications/Obsidian.app"; do
    if [ -e "$app" ] || [ -L "$app" ]; then
      printf 'STOP: Obsidian is already at %s; use that copy\n' "$app" >&2
      return 1
    fi
  done
  if [ -L "$HOME/course-evidence" ]; then
    printf 'STOP: course-evidence is a symlink\n' >&2
    return 1
  fi
  mkdir -p "$HOME/course-evidence" || return 1
  folder="$HOME/course-evidence/obsidian-download-$(date -u +%Y%m%dT%H%M%SZ)-$$"
  mkdir "$folder" || return 1
  dmg="$folder/Obsidian-1.13.7.dmg"
  curl --fail --location --output "$dmg" 'https://github.com/obsidianmd/obsidian-releases/releases/download/v1.13.7/Obsidian-1.13.7.dmg' || return 1
  actual="$(shasum -a 256 "$dmg" | awk '{ print $1 }')"
  if [ "$actual" != 05daa54f5e1a4458f75da29f8faaa17e8e37ae16998432537f674c626db99bce ]; then
    printf 'STOP: checksum mismatch; the disk image was not opened\n' >&2
    return 1
  fi
  printf 'SHA256 VERIFIED Obsidian-1.13.7.dmg %s\n' "$actual"
  open "$dmg"
}
course_get_obsidian
```

**Expected:** `SHA256 VERIFIED` with the digest, and then a Finder window for the Obsidian disk image.

**Stop:** The download or checksum fails, or Obsidian is already installed.

**Recovery:** Keep the download folder, fix the network problem, then paste the box again. If Obsidian is already installed, use that copy.

**Window: Finder, Obsidian disk image.** Drag **Obsidian** onto **Applications**. If Finder offers to replace an existing app, click **Stop**. When copying finishes, eject the disk image, then open **Obsidian** from **Applications**. If macOS asks whether to open an app downloaded from the internet, click **Open**.

**Expected:** Obsidian opens. **Stop:** The copy is refused or a security setting blocks the app. **Recovery:** Ask the device owner to resolve the specific message; don't disable Gatekeeper or remove quarantine flags.

### Practice in a fresh vault

Use the window from step 9. If you closed it, open a new window and paste the step 5 box first, which sets `PY`, `R`, and `M` again. This box makes a fresh practice vault under `~/course-evidence`, outside the checkout.

**Terminal: macOS Terminal, zsh or Bash, ordinary user, no sudo.**

```bash
course_start_vault() {
  if [ -z "${PY:-}" ] || [ -z "${M:-}" ] || [ ! -f "$M/scripts/obsidian_readiness.py" ]; then
    printf 'STOP: paste the step 5 box in this window first\n' >&2
    return 1
  fi
  OBS_ROOT="$HOME/course-evidence/obsidian-macos-$(date -u +%Y%m%dT%H%M%SZ)-$$"
  "$PY" "$M/scripts/obsidian_readiness.py" initialize --root "$OBS_ROOT" || return 1
  printf 'OPEN EXACT VAULT: %s\n' "$OBS_ROOT/vault"
}
course_start_vault
```

**Expected:** `Created practice vault:` and `OPEN EXACT VAULT:` both name the same folder ending in `/vault`. Keep that path visible.

**Stop:** Any `HOLD`, `STOP`, or error.

**Recovery:** Fix the problem it names, then paste the box again for a fresh vault. If initialization succeeded but you lost the window, see [Obsidian](#obsidian).

**Window: Obsidian.**

1. If another vault opens, leave it alone. Open the vault switcher and choose **Manage vaults**, then **Open folder as vault → Open**. On a first launch, choose **Open folder as vault → Open** directly.
2. In the folder picker, press **Cmd-Shift-G**, paste the printed `OPEN EXACT VAULT` path, and open that folder. Don't choose the checkout, its parent folder, or a personal vault.
3. Open **Settings → Community plugins** and make sure **Restricted mode** is on. Under **Settings → Core plugins**, turn **Sync** off if it is on. Don't sign in or install a plugin. In **Settings → General**, note the app version, then close Settings.
4. Open `Start` from the file list. Press **Cmd-E** for Reading view if needed, then click its **Token** link. The token is an exercise marker, not a credential.
5. Click **Reply** in `Token`. Switch to editing with **Cmd-E** if needed, paste only the token on one line, and press **Cmd-S**.

**Expected:** The links open the existing `Token` and `Reply` notes, and `Reply` shows the token. **Stop:** The wrong vault opens, a link creates an empty note, or you can't edit and save. **Recovery:** Leave `Start` and `Token` unchanged, reopen the exact printed folder, and follow its links again. Editing in another editor doesn't replace doing it in Obsidian.

Keep `Token` open in Obsidian. This box checks your saved reply, then changes `Token` from outside the app while keeping your reply.

**Terminal: macOS Terminal, zsh or Bash, ordinary user, same window; no sudo.**

```bash
"$PY" "$M/scripts/obsidian_readiness.py" check --root "$OBS_ROOT" &&
"$PY" "$M/scripts/obsidian_readiness.py" refresh --root "$OBS_ROOT"
```

**Expected:** `Token generation 1: initial token; external refresh not yet exercised`, then `PASS: Obsidian file round-trip; GUI observation still required` and a record path, then `Source token rotated outside Obsidian; your saved reply was preserved.`

**Stop:** `HOLD` or any error.

**Recovery:** If the check says the reply doesn't match, copy the current token into `Reply` in Obsidian, save, and paste this box again. If the refresh fails, see [Obsidian](#obsidian). Don't edit the helper's records.

**Window: Obsidian, same practice vault.**

1. Look at `Token` again. Its text should change to a new token that differs from the one in `Reply`. If it doesn't update, open `Start` and follow **Token** again.
2. Follow **Reply**, replace the old line with the new token, and press **Cmd-S**. Don't run the refresh again.
3. Close the practice vault's window, then open Obsidian again from **Applications**. If it reopens the practice vault, confirm the folder matches the printed path. Otherwise use **Manage vaults → Open folder as vault → Open** to choose it again.
4. Open `Start`, follow **Token**, then **Reply**, and confirm the new token is still saved.

**Expected:** You see the outside change, save the new reply, and see it again after reopening. **Stop:** The app doesn't show the change, the edit disappears, or you can't tell which vault reopened. **Recovery:** Record `Obsidian HOLD` with the action that failed and ask for help; a match found only by the shell doesn't show that the app worked.

**Terminal: macOS Terminal, zsh or Bash, ordinary user, same window; no sudo.**

```bash
"$PY" "$M/scripts/obsidian_readiness.py" check --root "$OBS_ROOT"
```

**Expected:** `Token generation 2: refreshed token; GUI observation still required` and `PASS: Obsidian file round-trip; GUI observation still required`, plus a second record path.

**Stop:** `HOLD`, or a token that wasn't refreshed.

**Recovery:** Correct `Reply` in Obsidian, save, close and reopen the vault, then paste this box again.

### Record your Obsidian result

In a text editor, create `gui-observation.txt` in the `OBS_ROOT` folder, beside `vault`. Record the date, macOS version, chip, Obsidian version, the exact vault path, and the two record paths the checks printed. Describe how you followed the links, saved the first reply, saw the outside change, saved the second reply, and reopened the vault. Note that Restricted mode was on and Sync was off. Leave out credentials and personal notes.

Write `Obsidian READY` only if both checks passed and you did every action in the Obsidian window. Otherwise write `Obsidian HOLD` and name the missing action or error. This result is separate from your OMP and n8n results. These app steps were checked with Obsidian 1.13.7 on Apple silicon; on Intel, record what you see.

## Prepare local n8n for Module 7

n8n is a workflow editor that you'll run on this Mac for Module 7. It runs in Docker, a tool that runs software in isolated containers. Allow extra time for downloads. You'll check Docker, generate the n8n files without starting them, limit the browser port to this Mac, start n8n, save a blank workflow, and confirm it survives a restart. Keep this result separate from your OMP and Obsidian results.

The [official n8n stack](https://github.com/n8n-io/n8n/blob/master/docker/get-n8n-compose.yml) runs six services: `n8n`, `runners`, `sandbox-certs`, `sandbox-api`, `sandbox-runner-1`, and `searxng`. `sandbox-runner-1` runs privileged Docker-in-Docker inside Docker's Linux virtual machine. Get the device owner's approval for that privilege, and for Docker Desktop itself, before you continue. Without approval, record n8n as `HOLD`.

### 1. Check Docker

A Docker **context** names the engine your `docker` commands reach. This box shows the engine, its existing containers and volumes, the `~/n8n-course` destination, and port 5678. It changes nothing. Keep the output private if it shows other work.

**Terminal: macOS Terminal, zsh or Bash, ordinary user.**

```bash
course_check_docker() {
  local ready=yes
  if [ -d /Applications/Docker.app ]; then printf 'Docker Desktop app found\n'; fi
  if command -v docker >/dev/null 2>&1; then
    printf 'DOCKER_CLI %s\n' "$(command -v docker)"
    docker context show || ready=no
    docker context ls || ready=no
    docker info --format 'ENGINE {{.Name}} {{.OperatingSystem}} {{.ServerVersion}}' || ready=no
    docker compose version || ready=no
    docker ps -a || ready=no
    docker volume ls || ready=no
  else
    printf 'DOCKER_CLI missing\n'
    ready=no
  fi
  if [ -n "${DOCKER_HOST:-}${DOCKER_CONTEXT:-}" ]; then
    printf 'HOLD: DOCKER_HOST or DOCKER_CONTEXT is set in this shell\n'
    ready=no
  fi
  if [ -e "$HOME/n8n-course" ] || [ -L "$HOME/n8n-course" ]; then
    printf 'HOLD: %s already exists; keep it\n' "$HOME/n8n-course"
    ready=no
  fi
  if lsof -nP -iTCP:5678 -sTCP:LISTEN; then
    printf 'HOLD: something is already listening on port 5678\n'
    ready=no
  fi
  if [ "$ready" = yes ]; then
    printf 'DOCKER READY FOR N8N\n'
  else
    printf 'DOCKER NOT READY\n'
    return 1
  fi
}
course_check_docker
```

**Expected:** The context is `desktop-linux` or another local engine you recognize, `ENGINE` names Docker Desktop, `docker compose version` prints a version, and the last line is `DOCKER READY FOR N8N`. Compose version 2 or 5 both work.

**Stop:** `DOCKER_CLI missing`, a failed Docker command, any `HOLD` line, or an engine you don't recognize.

**Recovery:** If Docker is missing, install Docker Desktop as described below. For anything else, see [Docker and n8n](#docker-and-n8n). Don't stop other containers or delete anything to make room.

**Install Docker Desktop only if it is missing.** Check the official [Mac requirements](https://docs.docker.com/desktop/setup/install/mac-install/): at least 4 GB of RAM and one of the three most recent major macOS releases. Confirm license eligibility with the device owner before you accept.

1. On Docker's page, choose **Docker Desktop for Mac with Apple silicon** or **Docker Desktop for Mac with Intel chip** to match the `ARCH` line from step 1 (`arm64` or `x86_64`).
2. Quit apps that use Docker, open `Docker.dmg`, and drag **Docker** onto **Applications**. Keep the disk image open until copying finishes.
3. Open **Docker** from **Applications** and select **Accept** if the device owner approved the license terms. Docker Desktop installs its command-line tools in `~/.docker/bin` and adds that folder to your PATH.
4. Wait until Docker Desktop reports that the engine is running. Then open a new terminal window from the **Shell** menu and paste the box above again.

### Optional: review the installer script before it runs
The installer script is downloaded live from the network and can change. To see exactly what it will do, download it first, read it with less, then let the next box use the reviewed copy.

**Terminal: macOS Terminal, zsh or Bash, ordinary user, Docker-checked window.**

```bash
N8N_REVIEW_DIR="$(mktemp -d "${TMPDIR:-/tmp}/n8n-r.XXXX")" &&
curl -fsSL https://get.n8n.io -o "$N8N_REVIEW_DIR/get-n8n.sh" &&
[ -s "$N8N_REVIEW_DIR/get-n8n.sh" ] &&
less "$N8N_REVIEW_DIR/get-n8n.sh" &&
N8N_REVIEWED_INSTALLER="$N8N_REVIEW_DIR/get-n8n.sh"
```

**Expected:** The script opens in less. It reports SCRIPT_VERSION near the top. After you press q, the variable is set for the generate box.

**Stop:** The download fails or the script contains actions the owner did not approve.

**Recovery:** Keep the directory and show it to the owner. Use a new directory for a later attempt.

### 2. Generate the n8n files and limit the port
This box runs the official one-line setup for n8n 2.41.5 with --no-start. It creates compose.yml, .env, and searxng-settings.yml without starting services. It then changes only the one browser port line in compose.yml from '5678:5678' to '127.0.0.1:5678:5678'. It refuses to run if port 5678 is occupied, the destination already exists, or Docker already has resources for the project name. If you reviewed the installer above, it uses that copy.

**Terminal: macOS Terminal, zsh or Bash, ordinary user, window where the Docker check passed.**

```bash
course_n8n_generate() {
  local dir containers volumes networks count
  dir="$HOME/n8n-course"
  if [ -e "$dir" ] || [ -L "$dir" ]; then printf 'HOLD: %s already exists; keep it\n' "$dir"; return 1; fi
  containers="$(docker ps -aq --filter label=com.docker.compose.project=n8n-course)" || return 1
  volumes="$(docker volume ls -q --filter label=com.docker.compose.project=n8n-course)" || return 1
  networks="$(docker network ls -q --filter label=com.docker.compose.project=n8n-course)" || return 1
  if [ -n "$containers$volumes$networks" ]; then printf 'HOLD: Docker already has resources for project n8n-course\n'; return 1; fi
  if nc -z -w 1 127.0.0.1 5678 2>/dev/null; then printf 'HOLD: something is already listening on port 5678; nothing was generated\n'; return 1; fi
  if [ -n "${N8N_REVIEWED_INSTALLER:-}" ]; then
    N8N_DIR="$dir" sh "$N8N_REVIEWED_INSTALLER" --version 2.41.5 --no-start
  else
    ( set -o pipefail; curl -fsSL https://get.n8n.io | N8N_DIR="$dir" sh -s -- --version 2.41.5 --no-start )
  fi || { printf 'HOLD: the n8n installer failed; keep %s for review\n' "$dir"; return 1; }
  if [ ! -f "$dir/compose.yml" ] || [ ! -f "$dir/.env" ]; then printf 'HOLD: the installer did not create compose.yml and .env\n'; return 1; fi
  count="$(grep -cF -e "- '5678:5678'" "$dir/compose.yml")"
  if [ "$count" != 1 ]; then printf 'HOLD: expected one 5678 port line in compose.yml, found %s\n' "$count"; return 1; fi
  cp "$dir/compose.yml" "$dir/compose.yml.orig" || return 1
  sed "s/- '5678:5678'/- '127.0.0.1:5678:5678'/" "$dir/compose.yml.orig" > "$dir/compose.yml.new" || return 1
  if [ "$(grep -cF -e "- '127.0.0.1:5678:5678'" "$dir/compose.yml.new")" != 1 ] || [ "$(grep -cF -e "- '5678:5678'" "$dir/compose.yml.new")" != 0 ]; then printf 'HOLD: the port change did not apply cleanly; compose.yml is unchanged\n'; return 1; fi
  mv "$dir/compose.yml.new" "$dir/compose.yml" || return 1
  printf 'PORT BOUND 127.0.0.1:5678\n'
  (umask 077; set -o noclobber; printf '%s\n' n8n-course > "$dir/.course-project") || { printf 'HOLD: could not record the project name\n'; return 1; }
  printf 'PROJECT n8n-course\n'
}
course_n8n_generate
```

**Expected:** The installer reports that it created the three configuration files without starting services. Then you see `PORT BOUND 127.0.0.1:5678` and `PROJECT n8n-course`.

**Stop:** Any HOLD line, an installer error, or an "existing install" message.

**Recovery:** Keep `~/n8n-course` and its output. Work with the owner to fix the specific failure. Do not delete the directory or run the installer into it again.

### 3. Start n8n and check it
This box defines two helpers and then starts the stack. `course_n8n` runs Docker Compose with the recorded project name, .env, and compose.yml. It stops if any variable that would override .env is exported in this shell. `course_n8n_check` shows the services, the published port, and the running n8n version.

**Terminal: macOS Terminal, zsh or Bash, ordinary user, window where the n8n generate box ran.**

```bash
course_n8n() {
  local variable
  for variable in N8N_VERSION N8N_SANDBOX_VERSION N8N_RUNNERS_AUTH_TOKEN SEARXNG_SECRET COMPOSE_PROJECT_NAME COMPOSE_FILE COMPOSE_ENV_FILES COMPOSE_DISABLE_ENV_FILE COMPOSE_PROFILES; do
    if printenv "$variable" >/dev/null 2>&1; then printf '%s HOLD\n' "$variable"; return 1; fi
  done
  if [ ! -f "$HOME/n8n-course/.course-project" ] || [ -L "$HOME/n8n-course/.course-project" ] || [ "$(cat "$HOME/n8n-course/.course-project")" != n8n-course ]; then printf 'HOLD: project record\n'; return 1; fi
  docker compose -p n8n-course --env-file "$HOME/n8n-course/.env" -f "$HOME/n8n-course/compose.yml" "$@"
}
course_n8n_check() {
  course_n8n ps --all && course_n8n port n8n 5678 && course_n8n exec -T n8n n8n --version
}
docker context show && course_n8n up -d && course_n8n_check
```

**Expected:** Images download and the services start. The list shows all six services: `sandbox-certs` shows `Exited (0)`, `sandbox-api` becomes healthy, and the rest are running. The port line is exactly `127.0.0.1:5678`, and the version is exactly `2.41.5`.

**Stop:** A service is missing, restarting, or failed; the port shows something other than `127.0.0.1:5678`; or the version differs.

**Recovery:** If a service still shows starting, wait a minute and paste the box again; `up -d` leaves running services alone. If the port is exposed, run `course_n8n down` to stop only this stack, keep its volumes, and ask the owner to review the bind. See [Docker and n8n](#docker-and-n8n).

### 4. Save a blank workflow
1. Open **http://localhost:5678** in your browser. On a fresh instance, complete **Set up owner account** and select **Next**. These credentials belong only to this local n8n instance. If a sign-in screen appears, use the existing local login; do not reset its owner or create another instance.
2. Finish any local onboarding questions. Skip optional offers for a license key or external signup. No n8n Cloud account, external account, or provider API key is required. Leave **n8n Assistant** off, and do not copy your OpenRouter key into n8n.
3. Select **Overview**, then **Build a workflow** on a fresh instance or **Create workflow** when workflows already exist. Click the workflow title, name the blank workflow **Module 7 readiness**, and press **Enter**. The editor saves automatically. Leave the canvas empty and do not select **Publish**. Keep an existing workflow with that name; choose a distinct readiness name if it contains work.
4. Reload the browser page. Confirm the workflow title and empty canvas remain, and that the workflow is unpublished. This reload checks saved state rather than an unsaved tab.

**Expected:** The local editor opens and the named blank workflow survives reload without an external account or key.

**Stop:** The page remains unavailable after startup, unexpected owner setup appears for an existing instance, login fails, saving fails, or the interface differs enough that you cannot confirm saved/unpublished state.

**Recovery:** Keep the instance and ask for help with the specific state. Do not clear volumes, reset accounts, publish a workflow, or enable Assistant to work around it.

### 5. Confirm the workflow survives a restart
Stop only the course stack you identified. Compose `down` removes its containers and network but keeps its named data volumes, so never add `-v`.

If you opened a new terminal window since the n8n start step, paste the box from [### 3. Start n8n and check it](#3-start-n8n-and-check-it) first so the helpers are defined.

**Terminal: macOS Terminal, zsh or Bash, ordinary user, window where the n8n generate box ran.**

```bash
course_n8n down &&
course_n8n up -d &&
course_n8n_check
```

**Expected:** Course containers stop and are removed; the data volumes remain. Then images are already present so start is fast. The check shows the same six services, `127.0.0.1:5678`, and `2.41.5`. Reload **http://localhost:5678**, sign in if needed, and open **Module 7 readiness** from the workflow list. Its name and empty canvas are still saved, it remains unpublished, and you don't need to set up the owner account again.

**Stop:** Data is missing, owner setup returns, the version/mapping changes, or services fail.

**Recovery:** Keep the directory and volumes. Before doing anything else, ask the owner to check whether the engine or Compose project changed. Don't create a replacement workflow to hide a persistence failure.

Record n8n readiness only after you observe the correct version, local-only mapping, the full stack state, the saved workflow after reload, and the workflow still there after this stop/start. If you can't confirm any of these, keep n8n readiness on **HOLD** for Module 7. This does not change either OMP readiness result.

In a later session, start Docker Desktop if it isn't running, open a new Terminal window, and paste the [step 3 box](#3-start-n8n-and-check-it) again. After a restart the stack stays stopped until you start it; the box defines the helpers, starts n8n, and checks it. The data volume keeps your workflow, so sign in with your existing local owner account.

## If a step stops

Keep the first error and attempt folder. See [shared/TROUBLESHOOTING.md](../shared/TROUBLESHOOTING.md) and [shared/CREDENTIALS.md](../shared/CREDENTIALS.md).

### Tools and Homebrew
Rosetta: close Terminal completely. In Finder, go to Applications > Utilities, select Terminal, choose File > Get Info, clear the checkbox **Open using Rosetta**, then reopen Terminal from the app and re-run step 1. Old macOS or <15 GB free: update or free space with the owner, then re-run step 1. No administrator account: ask the owner to run step 2 or provision Homebrew for your account.

**Terminal: macOS Terminal, zsh or Bash, ordinary user; Apple's dialog may ask for administrator approval.**

```bash
xcode-select --install
```

**Expected:** An Apple dialog opens. Click **Install**, accept the license if authorized, wait for completion, then re-run step 1. **Stop:** The dialog reports an error or you cannot authorize it. **Recovery:** Ask the device owner to complete the permitted installation, then re-run step 1.

Intel Python: download the current macOS installer from https://www.python.org/downloads/macos/, open the .pkg, follow the installer, then open a new terminal window and re-run step 1.

### Oh My Pi install
If the installer fails, keep its error and check [omp.sh](https://omp.sh/) for the current installation instructions. If macOS blocks OMP from starting, follow Apple’s Gatekeeper guidance at https://support.apple.com/en-us/102445 with the device owner.

### GitHub access and the checkout
Occupied Documents/AIHB_OCT_2026 that is not a checkout of the course repository: ask its owner to move the work elsewhere; do not overwrite it. gh plaintext storage not approved by device policy: ask the device owner to set up approved credential storage before continuing.

### New terminal and key
Tools not found after reopening: follow the OMP installer’s PATH instructions or Homebrew’s **Next steps**, then open another new window from the Shell menu and repeat step 5. If `SET` appears before key entry, open a fresh window directly from the Shell menu.

### Readiness check and report
LAUNCH_EXIT 2: the key is missing in this window; repeat steps 6 and 7 in this same window, then paste step 8 again. LAUNCH_EXIT 1 or READINESS CHECK HOLD or SETUP CHECK HOLD: keep the attempt folder and all receipts, read the first named failure, correct only that item, then create a new attempt with step 8. Do not edit from-omp.txt by hand or reuse an old result file.

### Obsidian
Lost the exact printed vault path: in the terminal, set `OBS_ROOT` to the printed parent path without the trailing `/vault`. Replace the example folder name with yours:

**Terminal: macOS Terminal, zsh or Bash, ordinary user, the window used for the vault steps.**

```bash
OBS_ROOT="$HOME/course-evidence/obsidian-macos-20261003T120000-1234"
```

**Expected:** The prompt returns with no output.

**Stop:** The folder you named doesn't exist or doesn't contain `vault`.

**Recovery:** Copy the exact path printed by the initialize box, without `/vault`, and paste this box again. If a refresh failed, start a fresh vault with the initialize box and repeat the GUI steps. If the app is blocked or you couldn't complete the link, edit, save, and reopen sequence, record `Obsidian HOLD` with the exact message or missing action.

### Docker and n8n
docker CLI missing after Docker Desktop install: add the export for the user CLI location to your login startup file only. For zsh use `~/.zprofile` (or the file under `ZDOTDIR`); for Bash use the first existing login file among `~/.bash_profile`, `~/.bash_login`, `~/.profile` and also `~/.bashrc`. Add exactly this line in a text editor:

```text
export PATH="$HOME/.docker/bin${PATH:+:$PATH}"
```

Then open a new terminal window from the Shell menu and re-run the Docker check. Wrong context or exported Compose override: ask the owner, then use a clean shell that does not have those variables exported. Existing `~/n8n-course`, port 5678 in use, or project resources for n8n-course: preserve everything; reuse an existing course instance only after the owner confirms its version and settings (skip the generate box). Slow startup: wait for the engine to settle and re-run the check box. Port exposed beyond 127.0.0.1: run `course_n8n down` (this stack only), keep the volumes, and ask the owner to correct the bind in compose.yml before restarting. To review the installer script before execution: use the optional review box that appears before the generate step (it runs `less` on the downloaded file before any execution).

## Local model (capstone) readiness lane

Ask staff for the approved `hf` and `llama-server` paths, then [check local-model readiness](../../module-10-capstone/shared/MODULE_10_LAB.md#check-local-model-readiness-before-downloading) before a download and again before launch. Quoted executable paths support spaces. Missing tools, insufficient capacity, an occupied endpoint, or an unresolved failed rehearsal mean **Local model HOLD**; preserve your other readiness results and contact the device/support owner.
