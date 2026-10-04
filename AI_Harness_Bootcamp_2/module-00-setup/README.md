# Module 0 · Set up the harness and direct bounded work

Install and check your tools, then ask Oh My Pi to draft an internal email. Check every important claim against the supplied North Shelf facts. Set the limits, decide what to delegate, and accept the email only for its stated use.

First follow one platform guide. Install what's missing, open a new terminal, and run the OMP readiness check: the model reads a fresh token and writes a real file through the course launcher. Check local Obsidian before Module 2 and local n8n before Module 7; keep their results separate from the checked email.

Allow roughly one to three hours for setup, more if downloads, desktop readiness, or owner approvals take longer. The bounded-work assignment takes about three hours (rough estimates).

## Start here

Choose one platform path and stay in it. A **terminal** is the text window where you enter commands; the **shell** is the program, such as PowerShell or Bash, that runs them.

| Your machine | Use this guide |
|---|---|
| Windows, native OMP with a WSL Ubuntu bridge for n8n | [Windows · PowerShell OMP and local n8n](platforms/windows-powershell.md) |
| Windows with or willing to install WSL 2 | [Windows · WSL 2 with Ubuntu](platforms/windows-wsl.md) |
| Mac | [macOS](platforms/macos.md) |
| Ubuntu desktop | [Ubuntu](platforms/ubuntu.md) |
| Arch Linux desktop | [Arch Linux](platforms/arch-linux.md) |

On Windows, choose WSL if your organization permits it and you can restart the machine. Choose PowerShell to keep OMP, Python, Git, credentials, and course work native to Windows; its WSL Ubuntu bridge is only for n8n. Both routes require approved WSL 2 and Docker Desktop for n8n. If WSL is blocked, keep the native OMP result and record n8n HOLD until the owner resolves it. Don't complete both OMP routes.

## What you will install

- Install Git and get a **checkout**, your local copy of the private course repository.
- Install Python 3.12 or newer.
- Install Oh My Pi (`omp`) pinned at version 18.3.5.
- Before Module 2, install local Obsidian. A **vault** is a folder of linked Markdown notes on your laptop. For a fresh install, use release **1.13.7**; if it's already installed, keep it and record its version.
- Before Module 7, install local n8n **2.41.5** with the full official Docker stack and a working modern `docker compose` plugin. Follow your platform guide's n8n path.

The platform guide keeps **PATH**, the saved list of folders your shell searches for commands. Check it in a new terminal after installation, not just the install window.

Get GitHub read access to `TheHolofex/AIHB_OCT_2026`; the hosted-course password doesn't provide it. Your guide checks approved Git credentials first. Use GitHub CLI (`gh`) for browser login only if that fails; it isn't needed to run the AI.

For the live readiness check, use `shared/run_omp.py` with OpenRouter and the fixed model `openrouter/anthropic/claude-sonnet-4.6`. It bills the account behind your key. Use an account you're authorized to charge and your own [OpenRouter key](shared/CREDENTIALS.md), which you enter in the terminal rather than save in a file. If you lack account or repository access, ask its owner before continuing.

Module 7 uses the local visual workflow editor without a paid model call. You don't need n8n Cloud or an Assistant provider key. Keep Assistant off and workflows unpublished; don't copy the OpenRouter key into n8n.

## Before the first command

- Reserve a restart window and connect to a stable network.
- Keep at least 15 GB free; WSL should have 25 GB.
- Get administrator approval for operating-system packages.
- Get device-owner approval for the full stack's privileged Docker-in-Docker runner, Docker access, and applicable Docker Desktop licensing. If denied, record n8n HOLD.
- Keep existing Docker contexts, containers, volumes, applications, and setup attempts. Resolve an occupied port 5678 or existing `$HOME/n8n-course` with its owner before installation.
- Keep credentials in the approved password manager or secure handoff.
- **Do not paste a key into a command, Markdown file, shell profile, screenshot, ticket, or repository.**
- If policy blocks a step on a managed laptop, stop and save the exact message for device support.

## When a step fails

Save the first error before changing anything. Follow [When setup stops](shared/TROUBLESHOOTING.md), change one thing, and rerun the failed check.

![Save the first error before changing anything, change one thing, and rerun the same check.](shared/figures/m00-recovery-loop.png)

*Save the first error before changing anything, change one thing, and rerun the same check.*

<details markdown="1">
<summary>Figure text</summary>

Keep the first error and do not overwrite the first attempt. Change one thing, run the same check, then compare the result with the saved first error. If the problem remains, use the recovery guidance; if it is resolved, record what changed. Neither outcome starts an automatic retry.

</details>

## Ready means observable

Open a new terminal after the last install. Check these OMP setup results:

![The prerequisite report, live tool write, and two application checks each show something different. One check cannot stand in for another.](shared/figures/m00-readiness-lanes.png)

*The prerequisite report, live tool write, and two application checks each show something different. One check cannot stand in for another.*

<details markdown="1">
<summary>Figure text</summary>

Check each tool on its own. In a new terminal, inspect the prerequisite report. A live OMP call must write a file and produce a receipt; open the file from disk to check it. A setup report marked PASS cannot replace that live check. For Obsidian, check both the files on disk and what you see in the app window. For n8n, check both the running stack and whether the workflow stays saved in the browser. A result for one tool cannot clear another.

</details>

- `origin` reports `https://github.com/TheHolofex/AIHB_OCT_2026.git`, and `git rev-parse HEAD` reports a 40-character id (the setup check prints the first 12). `git status --short` is informational; keep unrelated changes, which don't block setup or QA;
- the platform resolver selects an absolute Python executable reporting 3.12 or higher and saves it as `PY` (`$PY` in PowerShell);
- the setup check prints `omp/18.3.5` and the absolute command path;
- the key check shows `SET` in that terminal without printing the key;
- the tool writes `from-omp.txt` through the course launcher, and you read the file from disk;
- the expected absolute tool path works in that new terminal without repairing PATH; and
- the setup report stays outside the checkout and contains no key, token, or password.

The setup report shows PASS, WARN or FAIL for version, path, repository, and key presence. Run `verify_tool_proof.py` separately on the tool-written file, token, and saved run record; it reports `READINESS CHECK PASS` or `READINESS CHECK HOLD`. A passing setup report cannot replace this live check.

A **receipt** records a run's inputs, tool calls, results, and file effects. Keep receipts and your **work folder**, the editable exercise copy, outside the checkout so corrections don't overwrite supplied inputs or earlier attempts.

Open and read the result file from disk before accepting it. A tool saying “done” doesn't prove the file exists.

## Set up local Obsidian

Follow links, edit local notes, and see changes made outside the app with Obsidian. This check takes roughly 15 to 30 minutes after installation. No provider call is needed. Obsidian stores notes as [local Markdown files and refreshes external changes](https://github.com/obsidianmd/obsidian-help/blob/master/en/Files%20and%20folders/How%20Obsidian%20stores%20data.md).

Complete **Set up local Obsidian** in your existing guide: [native Windows](platforms/windows-powershell.md#set-up-local-obsidian), [WSL Ubuntu](platforms/windows-wsl.md#set-up-local-obsidian), [macOS](platforms/macos.md#set-up-local-obsidian), [Ubuntu](platforms/ubuntu.md#set-up-local-obsidian), or [Arch](platforms/arch-linux.md#set-up-local-obsidian). Follow its install, hash, display, and approval steps before opening the practice vault. The [release and asset table](shared/VERSIONS.md#local-obsidian-for-module-2) identifies the exact fresh downloads. Keep personal vaults, installed versions, and application profiles.

On the WSL route, run Linux Obsidian and the helper in the same Ubuntu Linux home as OMP. WSLg requires [Windows 10 build 19044+ or Windows 11 and WSL 2](https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps). Do not open a WSL UNC path in native Windows Obsidian or copy the vault to `/mnt/c`. On the native PowerShell route, Obsidian and course work stay native to Windows; the separate Ubuntu bridge remains for n8n only.

Keep **Settings → Community plugins → Restricted mode** on in the practice vault. Under **Settings → Core plugins**, turn **Sync** off if it is on. No Obsidian account, community plugin, or MCP service is required. Keep the existing [hidden-input credential procedure](shared/CREDENTIALS.md); never put a key in a note or another secret file.

In your platform guide, create one fresh vault, follow its links, save an edit, watch for a change made to a file outside Obsidian, save again, and close and reopen the same vault. Keep that attempt and note what you saw. Do not create a second practice vault by following another platform's instructions.

Record **Obsidian READY** only after both disk passes and a separate check in the Obsidian window. Note the platform and architecture, app version, practice-vault location, link you followed, first saved edit, changed token shown in the app, second saved edit, and same reply visible after reopening. Record who watched and the date, and keep credentials out of any screenshot. A disk PASS or an `.obsidian` folder alone cannot show what happened in the app. If that window check is missing or fails, record **Obsidian HOLD**; keep the OMP and n8n results and every attempt. Use [Obsidian troubleshooting](shared/TROUBLESHOOTING.md#when-local-obsidian-stops) for the named failure.

## Local n8n readiness for Module 7

Complete your platform guide’s n8n path as an ordinary user. On the native PowerShell route, run only the n8n steps in the selected WSL Ubuntu; keep the earlier OMP environment intact. The fresh destination is `$HOME/n8n-course` in the intended shell, outside the checkout.

Record **n8n READY** only after checking all of the following. Keep these checks separate from the OMP report and live OMP proof:

- The intended new shell passes `docker info` and `docker compose version` against the approved local engine. Modern Compose can report version 5; the older `docker-compose` command on its own isn't enough.
- The running n8n reports exactly `2.41.5`, and the published browser port is exactly `127.0.0.1:5678`.
- All six services appear: `n8n`, `runners`, `sandbox-api`, `sandbox-runner-1`, and `searxng` remain running; the one-shot `sandbox-certs` shows `Exited (0)`. Health checks are healthy where shown.
- At `http://localhost:5678`, the local owner can reopen a named blank, unpublished readiness workflow after reload. Assistant remains off.
- The same workflow survives the course stack’s ordinary `down` then `up -d`, using the same approved engine, directory, recorded project name, and named data volumes. Use the guide’s `course_n8n` helper; keep `.course-project` between restarts. Never use `down -v`.

On a fresh instance with the UI shown, complete **Set up owner account → Next**. If the optional survey appears, continue with **Get started**. Choose **Skip** on the free-license offer and **Set up later in Settings** on the Assistant screen. From **Overview**, select **Build a workflow** on an empty instance. Click the workflow title, enter **Module 7 readiness**, and press **Enter**. The editor saves automatically, so you do not need to see a **Saved** label. Reload and check that the name and blank canvas remain. If an instance already exists, use its local login and never reset its owner. If a workflow with that name already contains work, leave it in place and use a different name.

Run these checks on your device. The n8n app and stack were checked only on Apple Silicon. If the UI differs or any check fails, record **n8n HOLD** and use [When setup stops](shared/TROUBLESHOOTING.md). Keep an OMP pass even if n8n is on HOLD; an OMP pass does not show that n8n is ready.
