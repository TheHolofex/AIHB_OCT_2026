# AI Harness Bootcamp

Learn to operate AI harnesses by doing useful work: draft a document, check a claim, process a batch, and hand off a repeatable workflow. Run the tools yourself, inspect the result, and improve what happens next.

## Put an AI harness to work

An **AI harness** is the working environment around a model: its instructions, source files, tools, permissions, and records of what happened. You control that environment so the model can do a defined job and you can check the result.

You’ll use Oh My Pi to work with files and supplied tools. You’ll save instructions, test changes, diagnose failures, and decide whether an output is supported. No programming experience is required. You will paste supplied commands, edit instructions and settings, and inspect actual files.

## Produce work you can check

- **A source-checked email.** Give the model a request and a fact packet, inspect the draft it writes, and revise it when a fact changes.
- **A defensible brief.** Trace claims to the right sources, reproduce calculations, and separate supported facts from inference and unresolved questions.
- **A repeatable batch workflow.** Process records under a saved rule, handle exceptions, and prove what changes—and what does not—when you change that rule.
- **An operable handoff.** Give another person the inputs, instructions, controls, and checks they need to run, stop, and restore the work without your chat history.

A fluent answer is not enough. Compare the actual output with the request and sources. When a check fails, preserve the failure, correct its cause, and check again. When a required fact or permission is missing, stop and name the gap.

## Four-day schedule

The course runs Monday through Thursday: 28 facilitated hours, which is the time you spend in sessions with an instructor, and 20 of those hours are hands-on practice at your own keyboard. Monday, Tuesday, and Wednesday each hold two three-hour assignments. Thursday holds four assignments in one ten-hour teaching day.

| Day | Assignments, in order | Facilitated time | Practice included |
|---|---|---:|---:|
| Monday | [00 North Shelf](module-00-setup/README.md), then [01 Cold Lantern](module-01-mission-thread/README.md) | 6 hours | 4 hours |
| Tuesday | [02 Ledger Pike](module-02-context-desk/README.md), then [03 Kiln Hold](module-03-release-tools/README.md) | 6 hours | 4 hours |
| Wednesday | [04 Copper Span](module-04-diagnose-review/README.md), then [05 Blue Gauge](module-05-run-corpus/README.md) | 6 hours | 4 hours |
| Thursday | [06 White Rack](module-06-batch-workflow/README.md), then [07 Slope Brief](module-07-change-eval/README.md), then [08 Night Desk](module-08-agent-safeguards/README.md), then [09 Last Count](module-09-capstone/README.md) | 10 hours | 8 hours |

Every assignment includes two hours of practice. Thursday's four assignments take 3 hours, 2 hours 15 minutes, 2 hours 15 minutes, and 2 hours 30 minutes.

### Thursday timetable

Thursday starts at 08:00 and ends at 19:30 local time. Facilitated work adds up to 600 minutes; breaks and meals add another 90.

| Clock time | Work |
|---|---|
| 08:00–09:40 | White Rack, first 100 facilitated minutes |
| 09:40–09:50 | Break |
| 09:50–11:10 | White Rack, remaining 80 facilitated minutes |
| 11:10–11:20 | Break |
| 11:20–13:35 | Slope Brief, 135 facilitated minutes |
| 13:35–14:15 | Lunch |
| 14:15–15:20 | Night Desk, first 65 facilitated minutes |
| 15:20–15:30 | Break |
| 15:30–16:40 | Night Desk, remaining 70 facilitated minutes |
| 16:40–17:00 | Meal break |
| 17:00–19:30 | Last Count, 150 facilitated minutes |

Treat each break as a stopping point. The first White Rack break comes after you have built and saved your workflow, and the Night Desk break comes after the two supplied probes and before the planted-note run. Save your notes and receipts before you step away.

**Last Count's handoff happens outside these hours.** The assignment ends with a package that another person should be able to run, stop, and restore from its saved files, without your chat history. That person's attempt is scheduled separately, so arrange who it will be before Thursday. Running the package yourself in a fresh terminal shows that it restarts from saved files. It doesn't show that someone else can use it, so the course records the two observations separately. If no one is available, record the independent-person attempt as unobserved, not passed.

## Choose your assignment

Start with setup, then work through assignments 00–09. Each supplies its own case and files; bring the operating skills you have already practiced. Keep your work and evidence outside the source checkout.

<div data-course-map></div>

## Fictional cases, actual work

The cases are fictional. The tools you run, files you produce, checks you perform, and handoffs you attempt are real. Use the supplied data, not confidential workplace information. No exercise authorizes a real dispatch, release, or other operational decision.

This bootcamp is ungraded. `PASS` and `HOLD` describe technical checks and work decisions, not learner scores. A successful script run does not prove that another person can operate your handoff; observe that separately.

## Before you start

Choose the [setup path for Windows PowerShell, Windows with WSL 2, macOS, Ubuntu, or Arch Linux](module-00-setup/README.md). You need a browser, a plain-text editor, permission to install the required tools, and GitHub read access to the private course repository. The hosted-course password is separate from repository access.

Setup installs or checks Git, Python 3.12 or newer, and Oh My Pi 18.3.5. Live work uses a [participant-supplied OpenRouter key with a per-key spending ceiling of US$40](module-00-setup/shared/CREDENTIALS.md) and the pinned Sonnet 4.6 model. Set that ceiling before paid work; do not save the key in course files or shell profiles.

Allow 1–3 hours for setup. The 28 facilitated hours run Monday through Thursday, with two hours of practice in every assignment. These are planning allowances, not measured learner-completion guarantees.
