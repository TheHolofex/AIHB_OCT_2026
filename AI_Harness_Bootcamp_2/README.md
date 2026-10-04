# AI Harness Bootcamp

Learn to operate AI harnesses by doing useful work: draft a document, check a claim, process a batch, and hand off a repeatable workflow. You run the tools yourself, check what they produce, and use what you find to improve the next run.

## Put an AI harness to work

An **AI harness** is the working environment around a model: its instructions, source files, tools, permissions, and records of what happened. You control that environment so the model can do a defined job and you can check the result.

You'll use Oh My Pi to work with files and supplied tools, Obsidian to review and link notes, and a local copy of n8n to build visual workflows in Module 7. You'll save instructions, test changes, diagnose failures, and decide whether an output holds up against its sources. You don't need any programming experience: you'll paste supplied commands, edit instructions and settings, and open the files yourself to see what they contain.

<div data-photo-band="custody"></div>

## Produce work you can check

- **A source-checked email.** Give the model a request and a fact packet, inspect the draft it writes, and revise it when a fact changes.
- **A defensible brief.** Trace claims to the right sources, reproduce calculations, and separate supported facts from inference and unresolved questions.
- **A reusable knowledge vault.** Review source-backed notes in Obsidian, link the useful claims, and prove that a fresh model session uses your saved instruction and only the notes you approved. Then fix one weakness that matters and show the difference in another fresh run.
- **A repeatable batch workflow.** Build and save a visual n8n workflow that validates records, routes exceptions, and produces ordered receipts. Predict which rows one policy change will alter, compare every output row in both batches, then restore the original workflow and reproduce its results exactly.
- **A handoff someone else can run.** Give another person the inputs, instructions, controls, and checks they need to run, stop, and restore the work without you or your chat history.

In the batch workflow, before you change the policy, you save the original workflow export along with a separate record of its SHA-256 fingerprint. The changed export goes in its own file. To restore, you check the original against its fingerprint, import it into a new, blank workflow, and compare both reruns byte for byte with their original receipts. No model-written text goes into these checks, and you never edit an output by hand to make it match.

An answer can read well and still be wrong, so compare what the tool actually produced with the request and the sources. If a check fails, save the failed result, fix the cause, and check again. If you're missing a fact or permission you need, stop and say exactly what's missing.

## Four-day schedule

| Day | AM (with a break) | Lunch | PM (with a break) |
|---|---|---|---|
| Monday | [North Shelf](module-00-setup/README.md) | Lunch break | [Cold Lantern](module-01-mission-thread/README.md) |
| Tuesday | [Ledger Pike](module-02-context-desk/README.md) | Lunch break | [Kiln Hold](module-03-mcp-research/README.md), [Chalk Line](module-04-typed-decisions/README.md) |
| Wednesday | [Copper Span](module-05-diagnose-review/README.md) | Lunch break | [Blue Gauge](module-06-run-corpus/README.md), [White Rack](module-07-batch-workflow/README.md) |
| Thursday | [Slope Brief](module-08-change-eval/README.md), [Night Desk](module-09-agent-safeguards/README.md) | Lunch break | [Cold Foundry](module-10-capstone/README.md) |

<div data-photo-band="route"></div>

## Work through the assignments

Start with setup, then work through the assignments in order. Each one comes with its own case and files and expects you to bring the skills you practiced in the earlier ones. Keep your work and evidence outside your checkout, the local copy of the course repository.

<div data-course-map></div>

<div data-photo-band="clinic"></div>

## Fictional cases, actual work

Ten of the eleven assignments use fictional cases. Cold Foundry doesn't: you run a real, uncensored model on your own laptop under its own usage rules. Either way, the tools, files, checks, and handoffs are real. Use the supplied data, not confidential information from your workplace. No exercise authorizes a real dispatch, release, or other operational decision, and none publishes a model or makes one reachable from outside your own machine.

`PASS` and `HOLD` report the result of a technical check or a work decision: a check passes, or the work goes on hold until the problem is resolved.

## Before you start

Choose the [setup path for Windows PowerShell, Windows with WSL 2, macOS, Ubuntu, or Arch Linux](module-00-setup/README.md). You need a browser, a plain-text editor, permission to install the required tools, and GitHub read access to the private course repository. The password for this course site doesn't give you repository access; you need both.

Setup installs or checks Git, Python 3.12 or newer, Oh My Pi (OMP) 18.3.5, Obsidian, and n8n 2.41.5 with its full official Docker stack, all on your own machine. For live work, OMP uses [your own OpenRouter key](module-00-setup/shared/CREDENTIALS.md) and one fixed model, Claude Sonnet 4.6. Don't save the key in course files or shell profiles.

Module 2 needs Obsidian installed on your machine, with community plugins in Restricted mode and Sync turned off. If you already have Obsidian and it passes the readiness check, keep that installation; for a fresh install, use the release your platform guide names. The check has you open the practice vault, follow its links, save a reply, watch Obsidian pick up a change made outside the app, and then close and reopen the vault. Record what you saw in the Obsidian window separately from the disk check and from the OMP and n8n readiness results. On the WSL route, you run the Linux version of Obsidian through WSLg, on the same Linux home files that OMP uses, rather than pointing the Windows app at a network path.

Module 7 has its own n8n readiness check: you open the local editor and confirm that a saved workflow survives stopping and restarting n8n. You don't need an n8n Cloud account, an Assistant key, or any paid model calls. Keep the Assistant off, leave workflows unpublished, and open n8n only at localhost in your browser. The device owner must approve the privileged Docker-in-Docker runner and any Docker Desktop licensing that applies. On the native Windows PowerShell route, n8n is the only part that runs through a WSL Ubuntu bridge; OMP, Python, Git, your credentials, and the rest of the course work stay native to Windows. If WSL or Docker is blocked, n8n stays on HOLD even when OMP passes.

Allow roughly one to three hours for setup on top of the daily schedule, and longer if downloads are slow, the Obsidian or n8n checks take extra work, or you're waiting on the device owner's approval. That's a rough estimate, not a measured time.
