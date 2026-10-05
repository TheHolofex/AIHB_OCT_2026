# Module 0 facilitator runbook

## What this session must prove

Each learner can give AI a clear, limited job, check a material claim at the source, prove their own check is capable of failing, keep the draft inside the class, handle one changed fact, and leave a handoff with the exact paths and files so the work is locatable from the handoff alone.

Setup is an entry condition, not the lesson, and it is not part of the PO-00 result. A learner whose machine is not ready records `HOLD` on setup and moves to a loaner machine or a paired observation path. Observation keeps the learner in the room but does not pass the operating task.

The supplied Harbor Depot desk note to Field Clinic S-3 is public practice. Its checker is inspectable. Do not invent a second case or describe a public file as secret.

## Before learners arrive

1. Run the relevant setup path on the actual classroom images, including local Obsidian before Module 2 and its full local n8n path before Module 7.
2. Record each platform, architecture, installed versions, and date.
3. Confirm the intended repository is reachable and its frozen inputs are intact. Preserve unrelated local changes; do not reset or clean it.
4. Confirm the latest stable Oh My Pi (the observed `omp/<semver>` is recorded in receipts), the exact `openrouter/anthropic/claude-sonnet-4.6` selector, and a participant-supplied process-local `OPENROUTER_API_KEY`. There is no direct-provider login, model fallback, or automatic retry.
5. Choose fresh readiness-check work directories and preserve every prior attempt.
6. Confirm a same-state path for every control a learner must operate. Record any unverified operation explicitly.
7. Prepare a support owner for managed-machine and account problems.
8. Put a visible clock where learners can observe the 60-minute first-result design target. Record actual timing and assistance; this target has not been validated with learners.
9. Confirm T (first teaching day). At T-7 the coordinator sends setup instructions and access requirements. At T-3 each participant returns readiness status, evidence, and blockers via the register below. By T-1 device/support owners resolve blockers and staff complete capstone rehearsals/downloads on intended machines. Missing deadlines produce named HOLD records.
10. Maintain one privacy-safe readiness register (participant alias only, no real names/contact; route/platform, OS/architecture, device owner, required check, due date, status, evidence locator + date + redacted hash, support owner, disposition). Private details stay outside the repo and public site. Use actual cohort intake; do not assume availability of people or machines.
11. Record separately: GitHub account/invitation acceptance and repository read probe; participant-authorized OpenRouter access/key readiness and funded-credit readiness; HF access/conditions; device-owner installation approval; local n8n runtime/access and Local model tool/storage/RAM/port status. Exact local paths and private approvals belong in the external register, not this source. The US$25 staff verification admission remains separate from learner instructions.
12. Freeze the platform rehearsal matrix from the actual cohort inventory plus the mandatory changed-path routes (host macOS/Apple Silicon, native Windows PowerShell 5.1, clean Arch). At least one clean owner-approved machine per required combination completes the checks. Missing required machines hold release; unrepresented advertised routes remain explicitly runtime-unobserved.
13. Exercise the published commands for each required live lane on actual machines and preserve failures. Confirm class-work authorization and funded-credit readiness with the participant's account owner. Staff verification campaigns use their separately authorized [campaign ledger](../../../evidence/exercise-runs.json); its additional admission controls do not change the learner contract.

## Keep four readiness lanes separate

Record **OMP**, **Obsidian**, **n8n**, and **Local model** separately. The OMP lane retains both its prerequisite report and live `READINESS CHECK PASS/HOLD`; a passing report never replaces the live tool-write proof. Record **Obsidian READY/HOLD** from its two disk checks plus separate actual GUI observation, and **n8n READY/HOLD** from runtime, browser, and persistence checks. Record **Local model READY/HOLD** from approved tool identities, actual destination/cache volumes, installed and available RAM, a free `127.0.0.1:8080` before launch, and the complete exact-model lifecycle in Module 10. A preflight alone cannot make the Local model lane READY. No lane establishes another lane's result.

## Set up local Obsidian

Allow 15–30 minutes after installation to observe the practice workflow; record actual time rather than treating that allowance as measured. Use the existing platform's **Set up local Obsidian** section: [native Windows](../platforms/windows-powershell.md#set-up-local-obsidian), [WSL Ubuntu](../platforms/windows-wsl.md#set-up-local-obsidian), [macOS](../platforms/macos.md#set-up-local-obsidian), [Ubuntu](../platforms/ubuntu.md#set-up-local-obsidian), or [Arch](../platforms/arch-linux.md#set-up-local-obsidian). Require local vault storage, Restricted community plugins, and Sync off. No account, community plugin, or MCP service is needed.

Preserve the installed app, profile, and personal vaults. Fresh vendor installs use [1.13.7 and the exact asset hashes](../shared/VERSIONS.md#local-obsidian-for-module-2); an existing version may remain when its actual version and successful workflow are recorded. Arch uses its signed Extra package in the approved full-upgrade transaction, without a downgrade or partial upgrade. On WSL, require Linux Obsidian through WSLg in the same Ubuntu Linux home as OMP. The [Microsoft GUI floor](https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps) is build 19044+ or Windows 11 with WSL 2. Do not reset a distribution, use a native app on a WSL UNC vault, or move it to `/mnt/c`; coordinate any restart with owners of active distributions and Docker workloads.

On Ubuntu/WSLg ARM64, require the approved `libfuse2t64` transaction while retaining FUSE 3, as described in the [AppImage FUSE guidance](https://docs.appimage.org/user-guide/troubleshooting/fuse.html). Separately obtain device-owner approval for the vendor's [AppImage `--no-sandbox` launch](https://github.com/obsidianmd/obsidian-help/blob/master/en/Getting%20started/Download%20and%20install%20Obsidian.md). Explain that it disables Chromium's renderer sandbox for Obsidian and does not replace the course tool guard. Missing approval or display support remains Obsidian HOLD; no kernel-wide toggles, world-writable binaries, or privileged sandbox repairs.

Follow **Set up local Obsidian** in the learner's [platform guide](../README.md#set-up-local-obsidian) as an ordinary user with the platform-resolved Python 3.12+ executable. The overview links to the five routes; perform only the selected route's practice. The helper interface is `obsidian_readiness.py initialize|refresh|check --root PATH`; PATH must be a fresh external attempt directory. Open only its `vault` child. Observe this order:

1. `initialize --root PATH` creates linked `Start.md`, `Token.md`, blank `Reply.md`, and external `expected`/`observations` directories without overwriting an attempt.
2. In Obsidian, the learner opens `Start`, follows `Token`, follows `Reply`, enters the token on one line, and saves.
3. `check --root PATH` records the first disk result. Require `PASS: Obsidian file round-trip; GUI observation still required` for generation 1.
4. With the vault still open, `refresh --root PATH` rotates the token from outside Obsidian and preserves the old reply and observation.
5. The learner observes the changed token in Obsidian, follows `Reply`, edits and saves the new token, closes the vault window, reopens the same vault, and inspects the saved reply.
6. `check --root PATH` records the second disk result. Require the same qualified PASS for generation 2 and keep both check records and the refresh record.

Record actual platform, architecture, app version, date, observer, attempt location, and the GUI actions seen separately from helper output. The helper deliberately records `gui_observed: false`; never edit that field to manufacture desktop evidence. A token copied by a script, a matching disk file, or `.obsidian` presence does not prove GUI operation. Capture only credential-free practice-window evidence. Preserve every HOLD and use [Obsidian troubleshooting](../shared/TROUBLESHOOTING.md#when-local-obsidian-stops).

The observed reference GUI is **1.13.7 on Darwin arm64**. Native Windows, WSLg, Intel macOS, Ubuntu, and Arch GUI lanes remain unobserved in this record. Do not infer their success from the Mac observation or from shell parsing. Keep the learner's process-local hidden key entry, no-secret-files procedure, fixed provider/model, and no automatic retries unchanged; a maintainer credential exception grants no learner exception.

## Local n8n readiness

Before starting n8n, confirm device-owner approval for the full official six-service stack, privileged `sandbox-runner-1` Docker-in-Docker, ordinary-account Docker access, and applicable Docker Desktop licensing. Preserve existing contexts, containers, volumes, applications, destinations, and attempts. On native PowerShell, keep OMP, Git, Python, keys, checkout, and receipts native; the selected WSL Ubuntu is only the n8n bridge. If policy blocks WSL/Docker, preserve HOLD and arrange an approved operating machine.

The platform guide must establish all of the following on the learner’s actual device:

- `docker info` and modern `docker compose version` succeed in the intended new shell; Compose 5 is acceptable.
- The fresh install uses the reviewed official installer 1.4.0 contract, explicit n8n 2.41.5, and `--no-start`, with a completed-download review alternative. A live installer URL can change. An existing destination is preserved for owner review, not reinstalled.
- A fresh installation has an unused owner-approved project name recorded in `.course-project`; lifecycle commands use `course_n8n` with explicit project and configuration files and no exported overrides. Reuse the same identity and engine. Existing installations retain their owner-managed identity; stopped Docker Desktop requires startup approval because existing work may resume.
- The n8n browser port is `127.0.0.1:5678`, with no other host ports added. The running version is exactly `2.41.5`; a mismatch remains HOLD pending owner resolution.
- `n8n`, `runners`, `sandbox-api`, `sandbox-runner-1`, and `searxng` stay running, with health checks healthy where shown. `sandbox-certs` is the sixth service and correctly finishes at `Exited (0)`.
- A named blank, unpublished workflow survives browser reload and ordinary course `down` / `up -d` against the same project and named volumes. Never use `down -v`. Assistant remains off. Module 7 requires no Cloud signup, Assistant key, or model call.

For the observed fresh-instance UI, use **Set up owner account → Next**, optional survey **Get started**, free-license offer **Skip**, then Assistant **Set up later in Settings**. On an empty instance, **Overview → Build a workflow** opens the canvas. Click the title, enter the readiness name, and press **Enter**. Saving is automatic; require the name and blank canvas to persist after reload, not a mandatory **Saved** label. An existing instance uses its existing local login. Preserve a preexisting workflow; choose a distinct readiness name if needed.

The integration owner observed these runtime/UI/persistence results on Apple Silicon only. Do not report Windows, Intel macOS, Ubuntu, or Arch as exercised on that basis. Image availability is not execution proof. Record each actual platform and any unexercised operation. Use [shared n8n troubleshooting](../shared/TROUBLESHOOTING.md#when-local-n8n-stops) for blocked prerequisites, login, pulls, version, port, and persistence failures.

## Session shape

Plan about three hours. The clock marks below are approximate planning guides, not measured completion times: follow the learners' progress, not the clock. You are with the room throughout. The first table lists the moments when you address everyone; the second lists what learners work on and the evidence to look for. Preserve a HOLD rather than rushing a blocked action into a claimed pass.

### When you address the room

| Segment | Roughly | What you do |
|---|---|---|
| Opening | 0:00–0:20 | Record setup state and route blocked learners. Name the fictional case and sharing limit. Explain the inspectable practice checker and start the visible clock. |
| Checkpoint | 1:15–1:35 | Record first-draft state and actual elapsed time. Confirm direction and responsibility records preceded the run. Preserve failures and stop after the stated correction limit; do not read drafts aloud. |
| Close | 2:40–3:00 | Preserve original drafts, source/control identities and first failures. Name unresolved dependencies. |

### What learners work on

| Roughly | Learner work | Evidence you should see |
|---|---|---|
| 0:20–0:30 | Work folder created; email requirements written | `email-requirements.md` lists what the request asks for and two things the checker can't judge |
| 0:30–0:40 | Case and practice checker read | The learner can name two things the checker cannot judge |
| 0:40–0:50 | Delegation decision and responsibility screen | Both files saved, both before any AI run |
| 0:50–1:00 | Direction brief frozen | What a correct email must show, the falsifier, stop condition, and correction limit are all written |
| 1:00–1:15 | First draft produced and practice check run | A file on disk and a check output, within about the first hour |
| 1:35–1:50 | Material claim checked against the source | Exact source text quoted by the learner, not by the model |
| 1:50–2:00 | Falsifier run against a deliberately wrong copy | `falsifier-probe.md` plus the observed failure copied verbatim |
| 2:00–2:10 | Capability-limit statement written | Model output, product surface, harness control, and human decision separated; one capability and one limitation from this run |
| 2:10–2:15 | Send-or-hold decision | `READY TO SEND` or `HOLD`, with the evidence behind it |
| 2:15–2:35 | Changed input predicted, applied, and compared | Prediction timestamped before the second run; `artifact.md` untouched |
| 2:35–2:40 | Handoff written | Handoff names the exact paths and files so the work is locatable without asking the author |

## Coaching limits

You may:

- point to the current step;
- define a term in plain language;
- help recover the machine or open a supplied file;
- ask what source supports a claim;
- remind the learner of the correction limit.

You may not:

- supply the delegation decision;
- fill in the responsibility screen;
- rewrite the direction brief;
- identify the material source line;
- disclose any genuinely protected deciding control;
- tell the learner which statements the changed input should move;
- tell the learner what to break in the falsifier probe;
- accept a narrated action in place of an operation.

If coaching crosses one of those lines, mark that part of the attempt as guided practice in the evidence record.

## Setup triage

| State | Action |
|---|---|
| Command missing in every new terminal | Return to the PATH step; do not reinstall all tools |
| Key missing in a new terminal | Expected; repeat hidden entry |
| Repository dirty before learner work | Inspect and preserve it; frozen-input integrity matters, not a clean working tree |
| Provider or participant key unavailable | Preserve the blocked live lane; no provider/model substitute or invented artifact |
| Platform operation unavailable | Record exactly what was not exercised; parsing or another OS is not native proof |
| Managed policy | Capture the exact message and route it to the IT owner |
| Learner exceeds two draft corrections | Preserve the attempts and record the practice result as `HOLD` |

The shared receipt auditor accounts for OMP 18.3.5's stream-only `completedAt`
timestamp. It still requires every other final assistant field to match the
terminal record, plus the tool/guard/filesystem joins. If an older auditor holds
an otherwise completed readiness check on that timestamp, retain its original HOLD and
receipts. After updating the supplied helper, use a fresh work root and token;
do not rewrite the earlier result or reuse its output for the new readiness check.

## End-of-session collection

Collect or verify:

- OMP setup report path and separate live readiness result;
- Obsidian READY/HOLD, both disk-check paths, refresh record, actual version/platform, and separate GUI observations;
- separate n8n READY/HOLD, observed platform/version/port/service state, workflow name, reload and stop/start persistence observations, and unresolved owner approvals;
- separate Local model readiness status, preflight report, intended machine, and complete exact-model rehearsal evidence or the missing prerequisite;
- readiness-register entries with evidence locators and platform-matrix status;
- actual pilot observations, facilitator rehearsal records with source hashes and machines, and human peer-review records where observed;
- the relevant staff-verification ledger entry for campaign work, kept separate from class-work authorization;
- `email-requirements.md`;
- first-checked-draft timestamp;
- delegation and responsibility records, created before the run;
- original brief, draft, first check output, source check, and decision;
- `falsifier-probe.md` and the recorded observed failure;
- capability-limit statement;
- changed-input prediction and the unchanged original;
- handoff;
- reason for any `HOLD`;
- support packet for any blocked dependency.

Do not collect API keys, environment dumps, account screenshots, or the learner's full home path.

## Pre-release operational evidence requirements

These procedures are exercised on actual cohort machines and participants. Record actual observations only; do not fabricate participants, approvals, or results. Report missing people, machines, authorizations, and any unresolved staff-campaign admission prerequisite.

**Readiness register and schedule:** Use the privacy-safe register defined above. Collect from actual intake. T-7 / T-3 / T-1 deadlines govern; missing items produce named HOLDs. Staff-verification spending and its additional admission controls belong in the separate campaign ledger.

**Platform matrix:** Mandatory: host macOS/Apple Silicon, native Windows PowerShell 5.1, clean Arch. Plus every OS/version/arch in the confirmed cohort. One clean owner-approved machine per required combo must complete install + fresh-terminal + repo auth + OMP + Obsidian GUI + n8n + capstone where assigned. WSL2 Ubuntu, native Ubuntu, Intel macOS added where present in cohort. Unrepresented routes: explicitly unobserved.

**Three nondeveloper pilots (Modules 00-02):** Recruit three representative nondevelopers. Exercise Modules 00, 01, 02 in order on the candidate generated site served locally. Observe setup, source verification, Obsidian workflow, navigation/search, elapsed time, questions, interventions, friction, outcomes. Record failures and assistance. Fix instruction/UI defects and re-observe affected path. No scores or qualification decisions.

**Current Module 00-10 facilitator controls (rehearsals):** Facilitators perform each current lab using its owning runbook. Record source/config hashes, operator alias, actual machine/date, outputs, assistance, HOLDs. Particular controls:
- 00: separate OMP/Obsidian/n8n/Local model lanes + register.
- 01: baseline/prediction before sealed change; thread walk and claim defense.
- 02: real Obsidian GUI + cold retrieval + admission.
- 03: human contract inspection, six human-first calibration decisions (model does not supply baseline), unbounded then bounded probes in order, forty-note handling, narrowed partner, final revoked.
- 04: labels before model answers/adjudication; ten-message sample limits stated.
- 05: restore before fault/sealed first miss/authorized correction/three recovery runs.
- 06: sample before categories/held-out labels after prediction; first-failure notes.
- 07: blank-canvas build, frozen deltas, both waves, restored reports; three-hour block preserved.
- 08: pre-result policy, 120 authored rows, six designated failures, restoration; 38-call stretch only after mandatory lanes and budget gate.
- 09: three core probes + strict planted-question verifier; human peer review of policy/probe/measurement evidence.
- 10: individual in-session exact-model lifecycle (weights, 127.0.0.1:8080, 32768, health after listening, OMP reply, stop/unreachable, digest restore, frozen copy and fresh-terminal structure check); no recipient or after-hours attempt.

**Module 09 human peer review:** Obtain real human peer review of current Module 09 policy/probe/measurement evidence and handoff from someone able to inspect the mechanisms. Technical peer critique is distinct from novice pilot. Current evidence is ungraded observation.


**Billing and evidence integrity:** Record every paid staff-verification attempt in its campaign ledger, including facilitator, pilot, and platform work. Preserve receipts, planned/attempted/completed/held counts, and actual billing when observable. No synthetic evidence. Retired evidence stays in the archived prior report.
