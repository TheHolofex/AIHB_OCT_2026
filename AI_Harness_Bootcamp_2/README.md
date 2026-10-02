# AI Harness Bootcamp

Learn to operate AI harnesses by doing useful work: draft a document, check a claim, process a batch, and hand off a repeatable workflow. Run the tools yourself, inspect the result, and improve what happens next.

## Put an AI harness to work

An **AI harness** is the working environment around a model: its instructions, source files, tools, permissions, and records of what happened. You control that environment so the model can do a defined job and you can check the result.

You’ll use Oh My Pi to work with files and supplied tools, and local n8n to build visual workflows in Module 6. You’ll save instructions, test changes, diagnose failures, and decide whether an output is supported. No programming experience is required. You will paste supplied commands, edit instructions and settings, and inspect actual files.

<div data-photo-band="custody"></div>

## Produce work you can check

- **A source-checked email.** Give the model a request and a fact packet, inspect the draft it writes, and revise it when a fact changes.
- **A defensible brief.** Trace claims to the right sources, reproduce calculations, and separate supported facts from inference and unresolved questions.
- **A repeatable batch workflow.** Build and save a visual n8n workflow that validates records, routes exceptions, and produces ordered receipts. Predict one policy change, compare every output row across two batches, and restore the original workflow to reproduce both results.
- **An operable handoff.** Give another person the inputs, instructions, controls, and checks they need to run, stop, and restore the work without your chat history.

Keep the original workflow export and its separately recorded SHA-256 fingerprint before changing the policy. Save the changed export separately. Restore the verified original into a new blank workflow and compare both reruns byte-for-byte with their original receipts. Generated prose stays outside these deterministic checks, and outputs are never patched by hand.

A fluent answer is not enough. Compare the actual output with the request and sources. When a check fails, preserve the failure, correct its cause, and check again. When a required fact or permission is missing, stop and name the gap.

## Four-day schedule

The course runs Monday through Thursday: 30½ facilitated hours, which is the time you spend in sessions with an instructor, and 22 of those hours are hands-on practice at your own keyboard. Monday holds two three-hour assignments. Tuesday holds two three-hour assignments and a third of 2½ hours. Wednesday holds three three-hour assignments. Thursday holds three assignments that take seven hours together.

| Day | Assignments, in order | Facilitated time | Practice included |
|---|---|---:|---:|
| Monday | [00 North Shelf](module-00-setup/README.md), then [01 Cold Lantern](module-01-mission-thread/README.md) | 6 hours | 4 hours |
| Tuesday | [02 Ledger Pike](module-02-context-desk/README.md), then [03 Kiln Hold](module-03-mcp-research/README.md), then [10 Chalk Line](module-10-typed-decisions/README.md) | 8½ hours | 6 hours |
| Wednesday | [04 Copper Span](module-04-diagnose-review/README.md), then [05 Blue Gauge](module-05-run-corpus/README.md), then [06 White Rack](module-06-batch-workflow/README.md) | 9 hours | 6 hours |
| Thursday | [07 Slope Brief](module-07-change-eval/README.md), then [08 Night Desk](module-08-agent-safeguards/README.md), then [09 Last Count](module-09-capstone/README.md) | 7 hours | 6 hours |

Every assignment includes two hours of practice. Tuesday's third assignment takes 2 hours 30 minutes. Thursday's three assignments take 2 hours 15 minutes, 2 hours 15 minutes, and 2 hours 30 minutes.

### Tuesday timetable

Tuesday starts at 08:00 and ends at 18:00 local time. Facilitated work adds up to 510 minutes; breaks and meals add another 90.

| Clock time | Work |
|---|---|
| 08:00–09:20 | Ledger Pike, first 80 facilitated minutes |
| 09:20–09:30 | Break |
| 09:30–11:10 | Ledger Pike, remaining 100 facilitated minutes |
| 11:10–11:50 | Lunch |
| 11:50–13:05 | Kiln Hold, first 75 facilitated minutes |
| 13:05–13:15 | Break |
| 13:15–15:00 | Kiln Hold, remaining 105 facilitated minutes |
| 15:00–15:20 | Meal break |
| 15:20–16:40 | Chalk Line, first 80 facilitated minutes |
| 16:40–16:50 | Break |
| 16:50–18:00 | Chalk Line, remaining 70 facilitated minutes |

### Wednesday timetable

Wednesday starts at 08:00 and ends at 18:30 local time. Facilitated work adds up to 540 minutes; breaks and meals add another 90.

| Clock time | Work |
|---|---|
| 08:00–09:20 | Copper Span, first 80 facilitated minutes |
| 09:20–09:30 | Break |
| 09:30–11:10 | Copper Span, remaining 100 facilitated minutes |
| 11:10–11:50 | Lunch |
| 11:50–13:05 | Blue Gauge, first 75 facilitated minutes |
| 13:05–13:15 | Break |
| 13:15–15:00 | Blue Gauge, remaining 105 facilitated minutes |
| 15:00–15:20 | Meal break |
| 15:20–17:00 | White Rack, first 100 facilitated minutes |
| 17:00–17:10 | Break |
| 17:10–18:30 | White Rack, remaining 80 facilitated minutes |

### Thursday timetable

Thursday starts at 08:00 and ends at 16:00 local time. Facilitated work adds up to 420 minutes; breaks and meals add another 60.

| Clock time | Work |
|---|---|
| 08:00–10:15 | Slope Brief, 135 facilitated minutes |
| 10:15–10:25 | Break |
| 10:25–11:30 | Night Desk, first 65 facilitated minutes |
| 11:30–11:40 | Break |
| 11:40–12:50 | Night Desk, remaining 70 facilitated minutes |
| 12:50–13:30 | Lunch |
| 13:30–16:00 | Last Count, 150 facilitated minutes |

Treat each break as a stopping point. Inside an assignment, the Ledger Pike break comes after the screen runs, the Kiln Hold break comes after the bounded probe, the Chalk Line break comes after the comparison has been printed and before you adjudicate it, the Copper Span break comes after you seal the first miss, the Blue Gauge break comes after you write your sixteen first-failure notes, and the White Rack break comes after you have built and saved your workflow. On Thursday, the Night Desk break comes after the two supplied probes and before the planted-note run. Save your notes and receipts before you step away.

**Last Count's handoff happens outside these hours.** The assignment ends with a package that another person should be able to run, stop, and restore from its saved files, without your chat history. That person's attempt is scheduled separately, so arrange who it will be before Thursday. Running the package yourself in a fresh terminal shows that it restarts from saved files. It doesn't show that someone else can use it, so the course records the two observations separately. If no one is available, record the independent-person attempt as unobserved, not passed.

<div data-photo-band="route"></div>

## Choose your assignment

Start with setup, then work through the assignments in the order shown, which is the teaching order; each number is that assignment's permanent ID. Each supplies its own case and files; bring the operating skills you have already practiced. Keep your work and evidence outside the source checkout.

<div data-course-map></div>

<div data-photo-band="clinic"></div>

## Fictional cases, actual work

The cases are fictional. The tools you run, files you produce, checks you perform, and handoffs you attempt are real. Use the supplied data, not confidential workplace information. No exercise authorizes a real dispatch, release, or other operational decision.

`PASS` and `HOLD` describe technical checks and work decisions. A successful execution does not prove that another person can operate your handoff; observe that separately.

## Before you start

Choose the [setup path for Windows PowerShell, Windows with WSL 2, macOS, Ubuntu, or Arch Linux](module-00-setup/README.md). You need a browser, a plain-text editor, permission to install the required tools, and GitHub read access to the private course repository. The hosted-course password is separate from repository access.

Setup installs or checks Git, Python 3.12 or newer, Oh My Pi 18.3.5, and local n8n 2.41.5 with its full official Docker stack. Live OMP work uses a [participant-supplied OpenRouter key with a per-key spending ceiling of US$40](module-00-setup/shared/CREDENTIALS.md) and the pinned Sonnet 4.6 model. Set that ceiling before paid work; do not save the key in course files or shell profiles.

Module 6 requires a separate n8n readiness check: local editor access and a saved workflow that survives a stop and start. It needs no n8n Cloud signup, Assistant key, or paid model call. Keep Assistant off, workflows unpublished, and browser access on localhost. The device owner must approve the privileged Docker-in-Docker runner and applicable Docker Desktop licensing. On the native Windows PowerShell path, only n8n uses a WSL Ubuntu bridge. OMP, Python, Git, credentials, and other course work stay native to Windows. A blocked WSL or Docker prerequisite leaves n8n on HOLD even if OMP passes.

Allow 1–3 hours for setup, with additional time as needed for Docker downloads and owner approvals. The 28 facilitated hours run Monday through Thursday, with two hours of practice in every assignment. These are planning allowances, not measured learner-completion guarantees.
