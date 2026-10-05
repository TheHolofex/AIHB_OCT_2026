# AIHB_OCT_2026 — Reformation

**Serves oracle:** S02, S05, S06, S07, S09, S12, S13, S19, S20, S21, S24, S26

This course is in its own repository: <https://github.com/TheHolofex/AIHB_OCT_2026>. The standard checkout is `~/Documents/AIHB_OCT_2026`. You'll find the course sources, publishing tools, and required reference files here; you don't need a parent checkout.

## Course identity

Reformation is an **ungraded bootcamp** for a **professional domain user** doing accountable AI-assisted work without more operating complexity than the work needs. It builds professional AI-user and **harness operator** skills, not builder or software-engineering skills. Exercises produce work and observations, not learner scores or qualification decisions.

A harness is everything around a model that shapes and records its work: direction, context, sources, tools, permissions, working artifacts, saved controls, feedback, checks, and traces. The learner sets limits on the model's behavior, configures supplied controls, inspects evidence, and owns consequential decisions. An **adapter** builds and protects the executable mechanics and supplies each module's case. A builder owns APIs, MCP, retrieval pipelines, agent runtimes, and deployment.

The core targets a **nondeveloper** who can use workplace files and applications and inspect plain-language configuration. A ready accessible environment, checked in advance, supplies the mechanics.

The learner course is published under [`site/`](site/). Existing Markdown in [`AI_Harness_Bootcamp_2/`](AI_Harness_Bootcamp_2/) is maintainer source, not a second learner reading path. [`MISSION_THREAD_SCENARIOS.md`](MISSION_THREAD_SCENARIOS.md) holds the independent case specifications. [`evidence/exercise-runs.json`](evidence/exercise-runs.json) records observed exercise outcomes and explicit unverified lanes; design budgets are not pilot evidence.

## Core promise

The first-result target is about an hour to a frozen plan and a first AI-drafted section checked against its sources. It's a design target, not a measured promise about how long learners take. Before releasing anything consequential, the learner applies a minimum responsibility screen. Across the core, the learner gets a long document they can trust from AI, verifies sources, controls context, operates MCP tools under limited authority, decides with typed questions, orchestrates a bounded OMP agent team, designs a workflow for a decision model, has an agent write a spreadsheet, controls hallucinations through structured checks and independent agent review, and transfers the method.

The core runs on **four teaching days, Monday through Thursday, instructor-led and hands-on throughout**. Most modules take about three hours, including Cold Foundry. Chalk Line takes about two and a half hours; Slope Brief and Night Desk take a little over two hours each. These are rough estimates, not measured times. Each module has one outcome and its own supplied case, and produces **one evidence bundle per module**.

The day order, with each module's case, is:

| Day | Cases, in order |
|---|---|
| Monday | North Shelf (00), Cold Lantern (01) |
| Tuesday | Ledger Pike (02), Kiln Hold (03), Chalk Line (04) |
| Wednesday | Copper Span (05), Blue Gauge (06), White Rack (07) |
| Thursday | Slope Brief (08), Night Desk (09), Cold Foundry (10) |

The clocks and break points are in [COURSE_MAP.md](COURSE_MAP.md).

## Target sequence

| ID | Case | Module | Primary capability |
|---:|---|---|---|
| 00 | North Shelf | Get a long document you can trust from AI | Screen responsibility, plan and test a long document before any prose, have AI draft it one section at a time from six sources, check it against references outside it, revise only what's flagged, and decide whether to send it. |
| 01 | Cold Lantern | Verify sources and outputs | Produce and challenge research/source work with independent evidence. |
| 02 | Ledger Pike | Build and control a reusable second brain | Construct source-traceable knowledge in Obsidian, explicitly load its governing instruction, and retrieve from reviewed knowledge in a fresh session. |
| 03 | Kiln Hold | Operate MCP tools under limited authority | Connect a supplied MCP server, research a folder of notes, check the assistant's markings against the written rules, prove each limit including actions the model never tries, and remove the connection with proof. |
| 04 | Chalk Line | Decide with typed questions | Decompose a desk decision into atomic typed questions, run a model once as a read-only decision function, validate and measure its answers against frozen labels, and route in code with gates set from the measurement. |
| 05 | Copper Span | Orchestrate an OMP agent team | Decompose independent work and dependent joins, accept source-bearing native child results, and recover partial failure without discarding valid work. |
| 06 | Blue Gauge | Design a workflow for a decision model | Select and pin Jev (`openrouter/typesafe/jev-1.13`) as the harness judge, design questions and a code split around its weak spots, set thresholds from its probabilities on tuning notes, and measure the frozen screen on held-out notes. |
| 07 | White Rack | Automate a spreadsheet with an agent | Connect a local n8n AI Agent to OpenRouter with the learner's key, have it write a spreadsheet from the supplied batch, download that file, and check it against the source lots. |
| 08 | Slope Brief | Control hallucinations | Run structured source checks and independent agent reviews, correct only what the evidence supports, and keep unknowns visible in the human decision. |
| 09 | Night Desk | Constrain agent behavior | Enforce a live agent's declared tool boundary and distinguish observed denial from a prohibited call never attempted. |
| 10 | Cold Foundry | Stand up and package a local uncensored AI | Stand up the pinned uncensored model on the learner's own laptop under OMP, prove a live loopback-only interaction, stop and restore it, package the supporting kit of instructions and controls (weights excluded) so a fresh-terminal structure check passes, and close out by separating live runtime proof from structure-only evidence. Thursday's session is individual work. |

Cases and evidence bundles are **independent**: no gate relies on a product from an earlier module. Skills build on one another, but earlier skills are assumed rather than retaught as new objectives. The authoritative sequence and supplied inputs are in [COURSE_MAP.md](COURSE_MAP.md). Outcomes are in [LEARNING_OBJECTIVES.md](LEARNING_OBJECTIVES.md). [AUTHORING_GUIDE.md](AUTHORING_GUIDE.md) defines the module contract.

### Module 02 mastery

Using verified sources and bounded direction, construct a small source-traceable knowledge vault, load its governing instruction explicitly, and demonstrate useful retrieval from that knowledge in a fresh session without the source-processing chat or raw packet.

The three enabling objectives are:

1. Select and relate source-backed claims while separating evidence from instructions.
2. Admit reviewed knowledge and prove the saved rule and approved content are what a fresh session used.
3. Improve one substantive weakness and demonstrate the result in a new content revision and fresh run.

Module 01 already established source checking as a quality bar, and bounded direction is also an earlier skill. Module 02 adds saved instructions and proof that they were loaded. Its separate Ledger Pike case keeps all forty DN sources. The learner reviews and links local Markdown notes in Obsidian, admits knowledge, and checks retrieval from a frozen copy that contains only navigation and admitted knowledge. Bounded multi-agent orchestration belongs to Module 05; checking a local-model package from a fresh copy remains Module 10's.

## Core and advanced boundary

The core includes bounded native OMP multi-agent orchestration and task-bounded automation. Module 05 uses read-only specialists and a reviewer with one coordinator-owned output, explicit dependencies, and bounded recovery. Module 07 uses one n8n agent and one spreadsheet-writing tool. Module 08 adds a bounded, human-started, read-only review ensemble: agents work in isolated sessions, and a person starts each fixed stage and owns acceptance. The core permits one narrow form of persistent knowledge: a local, human-reviewed Markdown vault with explicit admission and read-only fresh-session retrieval. Autonomous state updates, concurrent agent writes to shared knowledge, unattended or recursively expanding teams, adaptive flow, and custom retrieval infrastructure remain advanced work. Core learners recognize the trigger, simpler alternative, added risk, and escalation owner.

The core requires zero programming objectives. Dynamic checker implementation, API/MCP construction, custom RAG, agent-runtime development, and deployment remain adapter or builder work.

## Evidence and operating limits

- A person owns consequential acceptance, release, refusal, authority expansion, and residual risk.
- A material acceptance uses independent evidence from a source, deterministic check, or observed state. Public practice files are inspectable.
- Keep input and check identities the same across a comparison. Authored practice data, hashes, model authorship, and agent role-play don't prove how a person performed.
- Every learner makes decisions and operates the tools. A supported `no-use`, `no-release`, or `no-tool` decision is professional performance: record and study it, but don't treat it as proof of operation.
- Keep evidence of a material failure before repairing it. Finding the fault alone is held, not completed recovery.
- A file's presence or a written refusal doesn't prove execution. Keep actual tool calls, execution results, guard records, and disk snapshots. A technical replay proves only the behavior it exercised.
- `PASS` and `HOLD` describe technical checks and work decisions, not grades. Keep the failed attempt, fix its cause, and keep later attempts separate.
- A clean-session check proves only the behavior exercised. Module 10's fresh-terminal structure check confirms named fields and files inside the fresh copy; it does not execute package commands or show that another person can operate the kit.
- Each module bundle contains the artifact/state, decisive evidence, decision, claim result, failure or `HOLD`, scope boundary, and handoff.

## Authoritative files

- [Course map](COURSE_MAP.md)
- [Learning objectives](LEARNING_OBJECTIVES.md)
- [Authoring guide](AUTHORING_GUIDE.md)
- [`modules/core/`](modules/core/)
- [Mission-thread scenario memory](MISSION_THREAD_SCENARIOS.md) — staff specs for session projects; not a lab

Detailed scenarios, commands, forms, answer keys, fixtures, and platform procedures remain outside the core skeleton. Only allowlisted public pages and exercise files enter `site/`; staff references, historical reviews, and answer keys stay outside publication.

## Reader UI and manifest

The current manifest publishes 35 instructional pages. They share the local Sirocco reader. Edit `ui/course.css` for composition, `ui/course.js` for progressive enhancement, and `ui/theme-init.js` for the before-paint appearance preference. `ui/vendor/sirocco/` contains the byte-identical selected reference assets and their font licenses; course overrides belong outside that vendor directory. No JavaScript bundler, package installation, CDN, or external font service is required. `course.json` declares 39 UI assets; the publisher also emits `assets/search-index.json`.

`course.json` remains the single publication registry:

- Each page has a `kind`: `home`, `overview`, `lab`, `setup`, or `reference`. Each module declares `case_name`, `summary`, `nav_summary`, `outcomes`, and exactly one overview and lab page. `summary` describes the work on the homepage card; `nav_summary` concisely names the main tool or skills beneath the case name in the desktop rail, mobile Course menu, and no-JavaScript navigation. `outcomes.can` is one learner-language sentence (at most 320 characters) completing "After this assignment you can"; `outcomes.will` lists two to four "You will…" items. The publisher rejects staff tokens in either. Keep these labels grounded in the module's distinct learning objectives; they wrap naturally rather than truncating.
- Lab `guide` objects list `context_sections` and `optional_sections` by existing H2 ID. Platform setup pages use `guide: {}`. Other page kinds omit `guide`.
- `ui_assets` explicitly maps each UI source to its published destination. Local CSS dependencies must also be declared. The publisher rejects missing dependencies, external CSS resources, unsafe paths, and unexpected output files.
- Figure entries accept SVGs and PNGs. PNGs use standard-library IHDR validation for intrinsic dimensions and the same full-size dialog as SVGs. Instructional PNGs live under the owning module's `shared/figures/`; their complete generation prompts and provenance stay unpublished in that module's `figures/RASTER_PROMPTS.md`, which is never listed in `course.json`. Keep authentic n8n captures under the owning module's `shared/figures/` as well. Do not feed screenshots or instructional PNGs into the SVG renderer.
- The homepage hero is the first `.webp` in `ui_assets` and must be exactly 1672×941. Optional photo bands map an id to a declared 1672×716 `.webp` under the top-level `home_bands` key, and each id appears exactly once on the home page as an empty `<div data-photo-band="ID"></div>`. An unknown, repeated, unused, non-empty, or non-home placeholder fails the build. Bands render as decorative, lazy-loaded figures outside search, the outline, and the figure dialog. The publisher reads WebP dimensions from the file header. Course-owned photographs live in `ui/images/`, not in the vendored Sirocco directory; `ui/images/ART_DIRECTION.md` holds their style contract, exact prompts, encode budgets, and provenance.
- The generated `assets/search-index.json` contains instructional prose and heading targets, not fenced commands, raw exercise contents, staff sources, or evidence. Search loads it only when opened.

Do not publish standalone accessibility/equivalent-inspection pages or callouts, scoring rubrics, or exercise-grading guidance. Keep keyboard navigation, figure text, and technical checks.

Every module overview and lab has an **Overview / Lab** switch immediately below its title. Both links come from the module's manifest routes; `aria-current="page"` marks the active page. Keep the switch visible on overview pages as well as labs, at narrow and wide widths, and without JavaScript.

Guided reading keeps commands and their expected, stop, and recovery conditions together. The publisher renders each labeled fence as a command card with a copy control, pairs adjacent Bash and PowerShell cards into one shell switch (the chosen shell is remembered; print shows both), and renders Expected/Stop/Recovery as callouts. Numbered steps carry step numbers and a "Mark done" control; the rail stepper mirrors them. Read full page exposes all procedure bodies and optional/transcript disclosures. Without JavaScript, core instructions, both shells, outcomes, and the static stepper remain visible, and navigation uses ordinary links and native disclosures. Existing heading fragments remain valid.

Appearance, reading mode, shell choice, explicitly selected reading positions, and step completion use only `reformation-ui:v1:{course-root-pathname}` in local storage (state version 2; version 1 preferences migrate). Progress is per device and per module: the overview panel, the header bar, and the home course map count done steps out of the lab and setup steps. "Reset progress on this device" clears positions and completion but keeps appearance, reading mode, and shell choice. These preferences store no work, credentials, or check results, and a done mark never establishes a passed technical check. Root and prefixed publications use separate keys.


## Runtime and publication

Participants need Git, Python 3.12+, the **latest stable Oh My Pi release**, a browser, and an ordinary text editor. Setup resolves [the official latest release](https://github.com/can1357/oh-my-pi/releases/latest) once and verifies the binary against that release's checksum list. Each run records the actual `omp --version` output; there is no course-specific OMP version number. Live cloud-model OMP runs still select **`openrouter/anthropic/claude-sonnet-4.6`** as the main chat model, with `OPENROUTER_API_KEY` supplied to the current process. Module 05 uses its native-task orchestration launcher; other OMP exercises use `shared/run_omp.py`. The launchers create fresh runtime state, bound the model's tools, disable retries and model fallback, and keep evidence separate from work. These are OMP tool boundaries, not operating-system sandboxes.

Resolve latest when installing or updating, not while auditing saved evidence. Checks compare each attempt's recorded runtime identities, so a later OMP release does not relabel an earlier run. Complete a dependent Module 05 chain with the same verified runtime; after an upgrade, start a fresh chain. Provider and model pins remain unchanged.

Module 02 also uses Obsidian to edit the local Markdown vault. It requires no community plugin, Sync account, REST API, or MCP service.

Module 06 also sets OMP's judge role to **`openrouter/typesafe/jev-1.13`**, TypeSafe's Jev decision model, through the same key and launcher. The course chat model makes exactly one `eval` call with a launcher-written cell; the guard refuses any other code. The launcher checks every saved judgment, the dated build that answered, the cost, and the work folder. A moving alias, the router, or a chat model as judge holds before any call.

Modules 02–10 use `shared/prepare_work.py`; Module 01 keeps its nine-source starter and Module 00 copies its request, style rules, checker, and six sources. Helpers refuse existing work/output attempts. A missing key or unavailable pinned provider/model holds the live lane without replacing it with a different model or unlabeled fixture.

Module 05 runs native `task` children rather than a second scheduler. Its three read-only specialists feed a coordinator-owned brief and a dependent read-only review. The first missing-input attempt remains on record; selective repair can reuse only still-valid independent results. The module checker joins requested assignments to native child records, source identities and permitted effects. A parent summary, finished task, or fixture transcript cannot substitute for accepted live handoffs.

Module 7 uses local **n8n 2.41.5** on the full approved official Docker stack. The learner connects an AI Agent to OpenRouter with their own key and downloads the spreadsheet that agent creates. The key must not appear in an export, prompt, or note. Run `python3 AI_Harness_Bootcamp_2/module-07-batch-workflow/tests/test_sheet.py` and `node --test AI_Harness_Bootcamp_2/module-07-batch-workflow/tests/test_controls.mjs`.

The child working directory is inside its redirected, fresh HOME. The historical OMP 18.3.5 replay showed that `--no-rules` did not disable [ancestor context-file discovery](https://github.com/can1357/oh-my-pi/blob/v18.3.5/packages/coding-agent/src/discovery/helpers.ts): placing cwd beside HOME allowed an outside ancestor's instructions to load. That offline replay observed the leak before the placement fix and its absence afterward, with zero provider requests. The isolated HOME/cwd boundary remains in place.

`.gitattributes` keeps text checkouts at LF so frozen source/control digests survive Git's automatic line-ending conversion. Native Windows setup also disables `core.autocrlf` for the clone command only. Do not renormalize or reset an existing dirty checkout to repair a hash failure; keep the mismatch and use an intact fresh copy.

Native OMP can exit 0 after an extension preparation error. The launcher still holds an attempt without exactly one completed terminal turn, the expected model identity, complete guard lifecycle, and matching tool/disk receipts. An offline host-invoked guard smoke verifies extension APIs and allow/deny behavior; it is not a model tool call or provider evidence. Runtime evidence files are local audit records, not cryptographic proof against an operator who can rewrite the whole evidence directory.

The saved-evidence audit joins each successful call to its authorization, independent execution check, tool/path identity, and filesystem effect. It also binds `response.md` to the final assistant event; changing only the extracted answer cannot change the recorded model response.

The MCP cutover retires the `hash_tool` policy field. Historical receipts containing that field require the launcher revision that produced them; the current auditor rejects the obsolete schema. Keep those receipts unchanged rather than removing fields to make an old run pass a new auditor.

Maintainers need Python 3.12+ and Node.js 22 to publish the course and run the offline checks. From the repository root, create the Python environment once if it does not already exist:

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

Reuse that environment for publication and checks. `node scripts/render_figures.mjs --check` verifies every local image link in the module pages. No module currently has a spec-owned SVG figure; the script renders a `figures/spec.json` only if one is added. Instructional PNGs are not rendered by that script. A reader UI change does not require regenerating figures.

```bash
.venv/bin/python scripts/build_course.py
.venv/bin/python scripts/check_course.py
.venv/bin/python scripts/build_course.py --check
.venv/bin/python -m http.server 8766 --bind 127.0.0.1 --directory site
```

On native Windows, use `.venv\Scripts\python.exe` for the virtual-environment interpreter. Reuse the environment during correction loops. `check_course.py` never starts paid model calls; live verification is explicit and separately recorded. Serve only `site`, not the repository or staff source tree.

The publisher reports instructional pages, raw downloads, and UI/generated assets separately. `--check` is read-only and compares exact bytes, including search and styles. After a UI change, exercise the built pages in a real browser in Dark and Sand, on narrow and wide viewports, with keyboard navigation, full reading, no JavaScript, print, and a prefixed mount. Keep screenshots and first-failure records outside the checkout. Browser proof is not native-platform, assistive-technology, provider, or learner-performance evidence.

`site/` is generated output and is not committed. On a fresh clone, install the pinned build dependency and run the publication commands above before serving or deploying. Publish the contents of `site/` as a static site; do not point a host at the repository root. The generated site needs no application server or provider credentials.

The GitHub repository is private. Give participants repository read access before they use the clone instructions; access to a hosted course page does not grant access to the source repository. Each setup route checks existing HTTPS access first. Only failed access enters the official `gh` browser-login fallback. `gh` is a conditional repository-access helper, not a harness or model credential. Its preferred OS credential store can fall back to plaintext; device policy must permit the reported storage before configuring the Git helper for `github.com`.

## Setup maintenance and verification

The five owning procedures are under `AI_Harness_Bootcamp_2/module-00-setup/platforms/`. Keep their commands aligned with the shared credential, version, troubleshooting, and source pages. The supported routes are native Windows PowerShell 5.1; Windows plus WSL 2 Ubuntu 24.04/26.04; macOS 15+ on Apple Silicon or Intel; Ubuntu 24.04/26.04 on x86-64/ARM64; and official Arch x86-64. Intel Homebrew is Tier 3, not equivalent support. Arch package installation is a full upgrade, never a partial `pacman -Sy`.

Keep the setup boundaries: install only missing prerequisites; verify the exact OMP checksum before execution; keep conflicting installs, profiles, and dirty checkouts; check saved PATH in an independent terminal without repairing it inside the check; and keep the prerequisite report separate from the live readiness check and actual disk readback. Both report helpers execute Python candidates until a usable 3.12+ interpreter is found. The native helper also tries the Python launcher's version selectors and rejects Store aliases/reparse paths.

Call the setup activity a **readiness check**. Its verifier reports `READINESS CHECK PASS` or `READINESS CHECK HOLD`; the executable remains `verify_tool_proof.py`. The name does not change the token, receipt, identity, or disk-content acceptance checks.

Windows execution policy is not a blanket setup prerequisite. Leave an already permitted policy unchanged. Managed restrictions, signing requirements, and intentional local restrictions require the device owner's approved route. The optional unmanaged-default recovery is explicitly consented, Process-only `RemoteSigned`; closing that PowerShell process ends it.

The hands-on language/setup revision passed all 28 offline gates and publication checks for 32 instructional pages, 663 raw downloads, and 38 UI/generated assets. Actual OMP 18.3.5 installation/checksum and no-key launcher boundaries were exercised in a disposable Apple Silicon home and an Ubuntu 24.04 x86-64 container, including Bash/zsh interactive and login startup. The Ubuntu route also exercised the official prerequisite and `gh` packages. PowerShell 7 parsing and controlled command-boundary checks are not Windows PowerShell 5.1 evidence.

Release evidence remains incomplete: native Windows/WSL, Intel macOS, the other Ubuntu combinations, independent desktop-terminal transitions, GitHub browser authentication, and authorized paid readiness checks remain unobserved for the revised routes. The emulated Arch container could not initialize pacman's syscall sandbox; no sandbox bypass was used to claim an upgrade. A representative nondeveloper's homepage/setup attempt is also unobserved. Browser navigation, clipboard, saved place, keyboard, search, no-script reading, print, and prefixed publication were exercised; narrow DOM checks passed, but narrow screen capture failed in the browser tooling. Keep those limits separate from passed checks. Preserve transcripts and visual evidence outside the checkout; do not describe the five routes as natively verified or the revision as unqualified “S-tier.”

The native Module 7 cutover passed all 27 current scoped gates: 32 instructional pages, 692 raw downloads, and 38 UI/generated assets. n8n 2.41.5 ran in the approved isolated six-service stack on Apple Silicon Docker Desktop. Native form submissions produced both 80-row baselines, the predicted three-lot policy change, and byte-identical restored receipts; independent downloaded checker reports also cover revised inputs, malformed batches, empty routes, and tampered evidence. See `AI_Harness_Bootcamp_2/module-07-batch-workflow/evidence/REVIEW_VERDICT.md` for execution IDs and limits. Bash/zsh and PowerShell parsing plus controlled shell-boundary checks cover all five authored setup routes; they are not native Windows/WSL/Linux runs.

Those page, download, and asset counts are the records of the checks named above. They are not the current publication size. The current manifest declares 35 instructional pages and 39 UI assets. `scripts/check_course.py` now runs 31 scoped gates; that count is the manifest plus the shared publication, runtime, and figure checks, not a new claim that every live lane was rerun.

### Rolling latest OMP verification — 2026-10-05 UTC

The official latest-release lookup selected `v18.6.1` for this verification, not as a new course pin. The authored macOS installer downloaded and verified that release in a disposable home; a separate login zsh resolved it from the saved profile. All 280 setup syntax, release-selection and failure-boundary checks passed, including optimized Python metadata validation and preservation of conflicting installed bytes.

The real latest binary passed the setup report, token-and-write readiness check, one bounded MCP read, a bool/choice/score Jev batch, and Copper Span's four native stages. Fanout produced the expected missing-Timing HOLD; selective repair dispatched only Timing; integration and review passed their independent saved-evidence checks. Existing provider/model pins did not change. Private records are under `~/course-evidence/omp-latest-20261004/`; the affected module references record run IDs and scope. These checks do not establish native Windows/WSL/Linux installs, GUI-terminal transitions, full MCP/Blue Gauge lab outcomes, or learner performance.

The generated setup pages were exercised in an isolated Chromium browser at desktop and 390-pixel widths. macOS and Windows copy controls returned the authored installer commands, and the version table showed the rolling latest requirement. Screenshots and clipboard observations are retained with the private evidence. The automation browser required explicit clipboard read/write permissions after a clipboard read left subsequent writes denied; no course code was changed to bypass that browser state.

All manifest module gates, the additional Module 01 content check, shared launcher/guard tests, publication/build tests, and figure check passed individually. Module 02's eight-mutation adequacy run required an extended deadline: its first run hit 600 seconds, and the isolated rerun passed in 823 seconds. The combined course gate is not claimed green: its 600-second per-command limit is unchanged, and the previously documented Module 07 core-contract HOLD was neither rerun nor changed.

## Netlify deployment

The hosted course is at [reformation-aihb-oct-2026.netlify.app](https://reformation-aihb-oct-2026.netlify.app). Native Netlify builds use the existing GitHub App connection to the private repository and publish successful pushes to `main`.

Root `netlify.toml` selects Python 3.12 and Node.js 22, installs `requirements-dev.txt`, runs the publisher and all course gates, and publishes only `site/`. A failed command blocks publication. Pretty URLs are disabled to keep the generated `.html` routes.

Manage the shared password in [the Netlify project](https://app.netlify.com/projects/reformation-aihb-oct-2026) under **Project configuration → General → Visitor access → Project visibility**. Keep **Password** selected with **Production and previews** scope. This protects pages, assets, downloads, and immutable deploy URLs. Keep credentials out of Git and build environment variables; the local `NETLIFY_PAT` stays in ignored `.env`.

To reconnect GitHub, open **Project configuration → Developer settings → Continuous deployment → Repository → Manage repository → Link to a different repository** and select `TheHolofex/AIHB_OCT_2026` through the existing Netlify GitHub App. Keep existing App repository grants. After relinking, confirm `main`, the `netlify.toml` build settings, private deploy logs, and all-deploy password protection. Push a deployment-owned change and confirm the published production deploy's commit matches that push; a successful clone or a build started by relinking does not prove push notifications work.

In the native deploy log, confirm `build.command from netlify.toml`, `PASS: all 31 scoped gates`, and the byte-for-byte publication check. Then check the live password gate and an authenticated download; a ready deploy alone does not verify access protection.

If a private-repository push appears missing, check **Deploys** for **Pending Review** before relinking. Netlify can hold an unrecognized Git author as `unverified-committer`, and the ordinary deploy-list API can omit that request; the site's builds API still lists it. For an author who is already a team member, use **Start approval process → Further action required → Approve and match with existing team member**, select that person, and confirm the match. Do not enable team-wide auto-approval to resolve one author's identity.
