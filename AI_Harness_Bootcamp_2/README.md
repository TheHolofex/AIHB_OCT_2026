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

The course runs Monday through Thursday, and all of it is hands-on: you work alongside an instructor, run the tools yourself, and check your own results. Most assignments take about three hours. Chalk Line takes about two and a half, and Slope Brief and Night Desk a little over two. These are rough estimates, not measured times, and your pace will vary with the group and the machine.

| Day | Assignments, in order | Roughly |
|---|---|---:|
| Monday | [00 North Shelf](module-00-setup/README.md), then [01 Cold Lantern](module-01-mission-thread/README.md) | 6 hours |
| Tuesday | [02 Ledger Pike](module-02-context-desk/README.md), then [03 Kiln Hold](module-03-mcp-research/README.md), then [04 Chalk Line](module-04-typed-decisions/README.md) | 8 to 9 hours |
| Wednesday | [05 Copper Span](module-05-diagnose-review/README.md), then [06 Blue Gauge](module-06-run-corpus/README.md), then [07 White Rack](module-07-batch-workflow/README.md) | 9 hours |
| Thursday | [08 Slope Brief](module-08-change-eval/README.md), then [09 Night Desk](module-09-agent-safeguards/README.md), then [10 Cold Foundry](module-10-capstone/README.md) | 7.5 hours |

The hours in this table don't include breaks or meals.

### Tuesday timetable

| Roughly | Work |
|---|---|
| 08:00–11:10 | Ledger Pike |
| 11:10–11:50 | Lunch |
| 11:50–15:00 | Kiln Hold |
| 15:00–15:20 | Meal break |
| 15:20–18:00 | Chalk Line |

### Wednesday timetable

| Roughly | Work |
|---|---|
| 08:00–11:10 | Copper Span |
| 11:10–11:50 | Lunch |
| 11:50–15:00 | Blue Gauge |
| 15:00–15:20 | Meal break |
| 15:20–18:30 | White Rack |

### Thursday timetable

| Roughly | Work |
|---|---|
| 08:00–10:15 | Slope Brief |
| 10:15–10:25 | Break |
| 10:25–12:50 | Night Desk |
| 12:50–13:30 | Lunch |
| 13:30–16:30 | Cold Foundry |

Some assignments also have a break partway through, at these points:

- **Ledger Pike:** after you run the file screen.
- **Kiln Hold:** after you probe the bounded connection.
- **Chalk Line:** after the comparison prints and before you adjudicate the disagreements.
- **Copper Span:** after you seal the first miss.
- **Blue Gauge:** after you write your sixteen first-failure notes.
- **White Rack:** after you've built and saved your workflow.
- **Night Desk:** after the two supplied probes and before the planted-note run.

Before any break, save your notes and receipts.

**Cold Foundry's handoff happens outside class hours.** The assignment ends with a kit that another person should be able to start, stop, and restore from its saved files, without your chat history. The coordinator arranges that person with you by three days before the first teaching day; their attempt is scheduled separately from Thursday's 13:30–16:30 block. Running the kit yourself in a fresh terminal shows that it restarts from its saved files, but not that someone else can use it, so you record the two results separately. If no one is available, record the other person's attempt as unobserved, not passed.

<div data-photo-band="route"></div>

## Choose your assignment

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

Cold Foundry has a separate **Local model** readiness check. Staff prepare missing tools with the device owner's approval, then you check the intended machine before any model download or launch. A passing OMP, Obsidian or n8n check doesn't establish local-model capacity. Use [Cold Foundry's readiness requirements](module-10-capstone/README.md) and report any missing tool, capacity limit or occupied service port to the support owner.

Allow roughly one to three hours for setup on top of the daily schedule, and longer if downloads are slow, the Obsidian or n8n checks take extra work, or you're waiting on the device owner's approval. That's a rough estimate, not a measured time.

### Arrange access and report blockers

Let **T** be the first teaching day confirmed by the coordinator.

| When | What you need |
|---|---|
| T−7 days | The coordinator sends setup instructions and access requirements. Confirm the GitHub invitation belongs to the account you'll use and obtain the device owner's installation approval. |
| T−3 days | Return your operating system/version, architecture, device owner, separate readiness results, evidence locations and blockers. Confirm authorized OpenRouter access and the provisional US$40 learner allowance with the account owner; that allowance isn't an automatically enforced cap. Confirm access and any usage conditions for the pinned Hugging Face repository with its account owner. |
| By T−1 day | Work with the support owner to resolve blockers. Staff complete the capstone download and full exact-model rehearsal on the intended machine. Keep unresolved checks on HOLD; don't infer readiness from a missed deadline. |

Send private names, contact details and account evidence through the coordinator's approved private channel. Never include a token in a readiness record. Only the account owner can authorize paid use or accept repository conditions; only the device owner can approve installations, Docker access and applicable licensing.
