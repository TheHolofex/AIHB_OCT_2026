# AI Harness Bootcamp

Learn to operate AI harnesses by doing useful work: draft a document, check a claim, process a batch, and hand off a repeatable workflow. Run the tools yourself, inspect the result, and improve what happens next.

## Put an AI harness to work

An **AI harness** is the working environment around a model: its instructions, source files, tools, permissions, and records of what happened. You control that environment so the model can do a defined job and you can check the result.

You’ll use Oh My Pi to work with files and supplied tools, Obsidian to review linked knowledge, and local n8n to build visual workflows in Module 6. You’ll save instructions, test changes, diagnose failures, and decide whether an output is supported. No programming experience is required. You will paste supplied commands, edit instructions and settings, and inspect actual files.

## Produce work you can check

- **A source-checked email.** Give the model a request and a fact packet, inspect the draft it writes, and revise it when a fact changes.
- **A defensible brief.** Trace claims to the right sources, reproduce calculations, and separate supported facts from inference and unresolved questions.
- **A reusable knowledge vault.** Review source-backed notes in Obsidian, connect useful claims, and prove that a fresh model session uses the admitted knowledge and its saved instruction. Improve a substantive weakness and compare a fresh run.
- **A repeatable batch workflow.** Build and save a visual n8n workflow that validates records, routes exceptions, and produces ordered receipts. Predict one policy change, compare every output row across two batches, and restore the original workflow to reproduce both results.
- **An operable handoff.** Give another person the inputs, instructions, controls, and checks they need to run, stop, and restore the work without your chat history.

Keep the original workflow export and its separately recorded SHA-256 fingerprint before changing the policy. Save the changed export separately. Restore the verified original into a new blank workflow and compare both reruns byte-for-byte with their original receipts. Generated prose stays outside these deterministic checks, and outputs are never patched by hand.

A fluent answer is not enough. Compare the actual output with the request and sources. When a check fails, preserve the failure, correct its cause, and check again. When a required fact or permission is missing, stop and name the gap.

## Choose your assignment

Start with setup, then work through assignments 00–09. Each supplies its own case and files; bring the operating skills you have already practiced. Keep your work and evidence outside the source checkout.

<div data-course-map></div>

## Fictional cases, actual work

The cases are fictional. The tools you run, files you produce, checks you perform, and handoffs you attempt are real. Use the supplied data, not confidential workplace information. No exercise authorizes a real dispatch, release, or other operational decision.

`PASS` and `HOLD` describe technical checks and work decisions. A successful execution does not prove that another person can operate your handoff; observe that separately.

## Before you start

Choose the [setup path for Windows PowerShell, Windows with WSL 2, macOS, Ubuntu, or Arch Linux](module-00-setup/README.md). You need a browser, a plain-text editor, permission to install the required tools, and GitHub read access to the private course repository. The hosted-course password is separate from repository access.

Setup installs or checks Git, Python 3.12 or newer, Oh My Pi 18.3.5, local Obsidian, and local n8n 2.41.5 with its full official Docker stack. Live OMP work uses a [participant-supplied OpenRouter key with a per-key spending ceiling of US$40](module-00-setup/shared/CREDENTIALS.md) and the pinned Sonnet 4.6 model. Set that ceiling before paid work; do not save the key in course files or shell profiles.

Module 2 requires local Obsidian with community plugins restricted and Sync off. Preserve an existing installation that passes readiness; fresh installs use the reference release in your platform guide. Open the practice vault, follow its links, save a reply, observe an external change, then close and reopen it. Keep the actual GUI observation separate from the disk check and from OMP and n8n readiness. The WSL route runs Linux Obsidian through WSLg against the same Linux-home files, not a native Windows app watching a network path.

Module 6 requires a separate n8n readiness check: local editor access and a saved workflow that survives a stop and start. It needs no n8n Cloud signup, Assistant key, or paid model call. Keep Assistant off, workflows unpublished, and browser access on localhost. The device owner must approve the privileged Docker-in-Docker runner and applicable Docker Desktop licensing. On the native Windows PowerShell path, only n8n uses a WSL Ubuntu bridge. OMP, Python, Git, credentials, and other course work stay native to Windows. A blocked WSL or Docker prerequisite leaves n8n on HOLD even if OMP passes.

Allow 1–3 hours for setup, with additional time as needed for downloads, desktop readiness, and owner approvals. The ten facilitated sessions are three hours each, including two hours of practice. These are planning allowances, not measured learner-completion guarantees.
