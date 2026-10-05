# Module 0 · Set up the harness and direct bounded work

Install and check your tools, then ask Oh My Pi to draft an internal email. Check every important claim against the supplied North Shelf facts. Set the limits, choose what to delegate, and decide whether you'd send the email.

Start with one platform guide. Install what's missing, open a new terminal, and run the OMP readiness check. In that check, the model reads a fresh token and writes a real file through the course launcher. Check local Obsidian before Module 2 and local n8n before Module 7; keep those results separate from the checked email.

Plan for about one to three hours for setup (a rough estimate). Downloads, desktop readiness, or owner approvals may take longer. Plan for about three hours for the bounded-work assignment (a rough estimate).

## Start here

Choose one platform path and stay in it. A **terminal** is the text window where you enter commands; the **shell** is the program, such as PowerShell or Bash, that runs them.

| Your machine | Use this guide |
|---|---|
| Windows, native OMP with a WSL Ubuntu bridge for n8n | [Windows · PowerShell OMP and local n8n](platforms/windows-powershell.md) |
| Windows with or willing to install WSL 2 | [Windows · WSL 2 with Ubuntu](platforms/windows-wsl.md) |
| Mac | [macOS](platforms/macos.md) |
| Ubuntu desktop | [Ubuntu](platforms/ubuntu.md) |
| Arch Linux desktop | [Arch Linux](platforms/arch-linux.md) |

On Windows, choose WSL if your organization permits it and you can restart the machine. Choose PowerShell if you want to keep OMP, Python, Git, credentials, and course work native to Windows; its WSL Ubuntu bridge is only for n8n. Both routes require approved WSL 2 and Docker Desktop for n8n. If WSL is blocked, keep the native OMP result and record n8n HOLD until the owner resolves it. Don't complete both OMP routes.

## What you will install

- Install Git and get a **checkout**, your local copy of the private course repository.
- Install Python 3.12 or newer.
- Install Oh My Pi (`omp`) from the latest stable release (the setup prints the observed `omp/<semver>`).
- Before Module 2, install local Obsidian. A **vault** is a folder of linked Markdown notes on your laptop. For a fresh install, use release **1.13.7**; if it's already installed, keep it and record its version.
- Before Module 7, install local n8n **2.41.5** with the full official Docker stack and a working modern `docker compose` plugin. Follow your platform guide's n8n path.

The platform guide keeps **PATH**, the saved list of folders your shell searches for commands. Check it in a new terminal after installation, not just the install window.

Get GitHub read access to `TheHolofex/AIHB_OCT_2026`; the hosted-course password doesn't grant it. Your guide checks approved Git credentials first. Use GitHub CLI (`gh`) for browser login only if that fails; you don't need it to run the AI.

For the live readiness check, use `shared/run_omp.py` with OpenRouter and the fixed model `openrouter/anthropic/claude-sonnet-4.6`. Use your own [OpenRouter key](shared/CREDENTIALS.md), which you enter in the terminal rather than save in a file. If you lack account or repository access, ask its owner before continuing.

Module 7 uses the local visual workflow editor. You don't need n8n Cloud. Keep Assistant off and keep workflows unpublished during setup. In Module 7 you put your OpenRouter key into an n8n credential for the agent. Don't put that key in a file, a workflow export, a prompt, or your notes.

## Before the first command

- Keep at least 15 GB free; WSL should have 25 GB.
- Get administrator approval for operating-system packages.


## When a step fails

Copy and paste the error into the harness. Describe what you were doing when the error appeared and what you are trying to accomplish, then ask it to fix the issue:

```text
I'm trying to: [describe the outcome you want].
I was doing this when the error appeared: [describe the command or action].
Here is the error:
[paste the error message]

Fix this issue.
```

Review and apply the fix, then rerun the failed check. If it still fails, paste the new error into the same conversation and explain what you tried. If the harness itself cannot start, use [When setup stops](shared/TROUBLESHOOTING.md).

![Give the harness the error, what you were doing, and your goal. Ask it to fix the issue, then check the result.](shared/figures/m00-recovery-loop.png)

*Give the harness the error, what you were doing, and your goal. Ask it to fix the issue, then check the result.*

<details markdown="1">
<summary>Figure text</summary>

Copy and paste the error into the harness, describe what you were doing and what you are trying to accomplish, and ask “Fix this issue.” Review and apply the fix, then run the same check again. If it still fails, return to the harness with the new error and what you tried. If it succeeds, record the result.

</details>

## Ready means observable

Open a new terminal after the last install. Check these OMP setup results:

![The prerequisite report, live tool write, and two application checks each show something different. One check cannot stand in for another.](shared/figures/m00-readiness-lanes.png)

*The prerequisite report, live tool write, and two application checks each show something different. One check cannot stand in for another.*

<details markdown="1">
<summary>Figure text</summary>

Check each tool on its own. In a new terminal, inspect the prerequisite report. A live OMP call must write a file and produce a receipt; open the file from disk to check it. A setup report marked PASS cannot replace that live check. For Obsidian, check both the files on disk and what you see in the app window. For n8n, check both the running stack and whether the workflow stays saved in the browser. A result for one tool cannot clear another.

</details>

- `origin` reports `https://github.com/TheHolofex/AIHB_OCT_2026.git`, and `git rev-parse HEAD` reports a 40-character id (the setup check prints the first 12). `git status --short` is informational; keep unrelated changes. They don't block setup or QA;
- the platform resolver selects an absolute Python executable reporting 3.12 or higher and saves it as `PY` (`$PY` in PowerShell);
- the setup check prints the observed `OMP_VERSION omp/<semver>` and the absolute command path;
- the key check shows `SET` in that terminal without printing the key;
- the tool writes `from-omp.txt` through the course launcher, and you read the file from disk;
- the expected absolute tool path works in that new terminal without repairing PATH; and
- the setup report stays outside the checkout and contains no key, token, or password.

The setup report shows PASS, WARN or FAIL for version, path, repository, and key presence. Run `verify_tool_proof.py` separately on the tool-written file, token, and saved run record; it reports `READINESS CHECK PASS` or `READINESS CHECK HOLD`. Even a passing setup report cannot replace the live check.

A **receipt** records a run's inputs, tool calls, results, and file effects. Keep receipts and your **work folder** (the editable exercise copy) outside the checkout. That way, corrections won't overwrite supplied inputs or earlier attempts.

Open and read the result file from disk before accepting it. A tool saying “done” doesn't prove the file exists.

## Set up local Obsidian

Obsidian is the note app for Module 2. A **vault** is a folder of notes on your laptop. Do this before Module 2, in the platform guide you already chose. You don't sign in to Obsidian, and you don't use your key here.

Open **Set up local Obsidian** in that guide and follow only those steps:

- [Windows PowerShell](platforms/windows-powershell.md#set-up-local-obsidian)
- [Windows with WSL](platforms/windows-wsl.md#set-up-local-obsidian)
- [Mac](platforms/macos.md#set-up-local-obsidian)
- [Ubuntu](platforms/ubuntu.md#set-up-local-obsidian)
- [Arch Linux](platforms/arch-linux.md#set-up-local-obsidian)

The guide installs the app if you don't have it, then has you practice in one new vault. If Obsidian is already installed, keep that copy and your existing notes. Don't mix steps from another platform.

You're done when the guide's checks pass and you saw the practice in the Obsidian window. Write **Obsidian READY** or **Obsidian HOLD** as the guide tells you. That result stays separate from your Oh My Pi and n8n results. If a step stops, use [Obsidian troubleshooting](shared/TROUBLESHOOTING.md#when-local-obsidian-stops).

## Local n8n readiness for Module 7

Complete your platform guide's n8n path as an ordinary user. On the native PowerShell route, run only the n8n steps in the selected WSL Ubuntu; keep the earlier OMP environment intact. The fresh destination is `$HOME/n8n-course` in the intended shell, outside the checkout.

Record **n8n READY** only after checking all of the following. Keep these checks separate from the OMP report and live OMP proof:

- The intended new shell passes `docker info` and `docker compose version` against the approved local engine. Modern Compose can report version 5; the older `docker-compose` command on its own isn't enough.
- The running n8n reports exactly `2.41.5`, and the published browser port is exactly `127.0.0.1:5678`.
- All six services appear: `n8n`, `runners`, `sandbox-api`, `sandbox-runner-1`, and `searxng` remain running; the one-shot `sandbox-certs` shows `Exited (0)`. Health checks are healthy where shown.
- At `http://localhost:5678`, the local owner can reopen a named blank, unpublished readiness workflow after reload. Assistant remains off.
- The same workflow survives the course stack's ordinary `down` then `up -d`, using the same approved engine, directory, recorded project name, and named data volumes. Use the guide's `course_n8n` helper; keep `.course-project` between restarts. Never use `down -v`.

On a fresh instance with the UI shown, complete **Set up owner account → Next**. If the optional survey appears, continue with **Get started**. Choose **Skip** on the free-license offer and **Set up later in Settings** on the Assistant screen. From **Overview**, select **Build a workflow** on an empty instance. Click the workflow title, enter **Module 7 readiness**, and press **Enter**. The editor saves automatically, so you do not need to see a **Saved** label. Reload and check that the name and blank canvas remain. If an instance already exists, use its local login and never reset its owner. If a workflow with that name already contains work, leave it in place and use a different name.

Run these checks on your device. The n8n app and stack were checked only on Apple Silicon. If the UI differs or any check fails, record **n8n HOLD** and use [When setup stops](shared/TROUBLESHOOTING.md). Keep an OMP pass even if n8n is on HOLD; an OMP pass does not show that n8n is ready.
