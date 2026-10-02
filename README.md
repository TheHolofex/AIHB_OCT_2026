# AIHB_OCT_2026 — Reformation

**Serves oracle:** S02, S05, S06, S07, S09, S12, S13, S19, S20, S21, S24, S26

Standalone course repository: <https://github.com/TheHolofex/AIHB_OCT_2026>. The standard checkout is `~/Documents/AIHB_OCT_2026`. Course sources, publishing tools, and required reference files live in this repository; no parent checkout is needed.

## Course identity

Reformation is an **ungraded bootcamp** for a **professional domain user** doing accountable AI-assisted work at the smallest sufficient operating complexity. It develops professional AI-user and **harness operator** skills, not builder or software-engineering skills. Exercises produce work and observations, not learner scores or qualification decisions.

A harness is the environment around a model: direction, context, sources, tools, permissions, working artifacts, saved controls, feedback, checks, and traces. The learner specifies bounded behavior, configures supplied controls, inspects evidence, and owns consequential decisions. An **adapter** implements and protects executable mechanics and supplies each module's case. A builder owns APIs, MCP, retrieval pipelines, agent runtimes, and deployment.

The core is designed for a **nondeveloper** who can use workplace files and applications and inspect plain-language configuration. A preflighted accessible environment supplies the mechanics.

The learner course is published under [`site/`](site/). Existing Markdown in [`AI_Harness_Bootcamp_2/`](AI_Harness_Bootcamp_2/) is maintainer source, not a second learner reading path. [`MISSION_THREAD_SCENARIOS.md`](MISSION_THREAD_SCENARIOS.md) owns the independent case specifications. [`evidence/exercise-runs.json`](evidence/exercise-runs.json) records observed exercise outcomes and explicit unverified lanes; design budgets are not pilot evidence.

## Core promise

The first-result design target is 60 minutes for producing and checking a useful bounded artifact; it is not a measured learner-completion promise. Before any consequential release, the learner applies a minimum responsibility screen. Across the core, the learner directs work, verifies sources, controls context, operates MCP tools under limited authority, diagnoses failure, improves from observed runs, operates one fixed workflow, evaluates change with explicit treatment of model variation, and transfers the method.

The core runs as **four teaching days, Monday through Thursday: 28 facilitated hours, including 20 practice hours**. Monday through Wednesday hold seven three-hour blocks; Thursday holds three blocks totaling seven facilitated hours. Every module keeps two hours of practice, owns one outcome, receives its own supplied case, and leaves **one evidence bundle per module**. The independent-person attempt remains separately scheduled outside those hours.

## Target sequence

| ID | Module | Primary capability |
|---:|---|---|
| 00 | Select, screen, and direct bounded work | Delegate appropriately, check one useful result, screen responsibility, and turn a request into accepted direction with a communication artifact. |
| 01 | Verify sources and outputs | Produce and challenge research/source work with independent evidence. |
| 02 | Control context and reusable instructions | Place information and rules where loading, precedence, survival, and bypass are observable. |
| 03 | Operate MCP tools under limited authority | Connect an MCP server, research through it, judge AI handling classifications against stated rules, and limit the connection so forbidden actions cannot happen, with proof and removal. |
| 04 | Diagnose and recover | Localize a hidden fault, make an authorized reversible correction, and prove clean-condition recovery. |
| 05 | Improve from observed failures | Specify a mechanically decidable predicate and configure and validate it in a supplied deterministic control. |
| 06 | Build and control a fixed workflow | Compose native visual batch controls, prove a single policy change completely, and restore the independently identified original graph. |
| 07 | Evaluate a change with variation controls | Use repeated controls or a justified deterministic case to separate change from ordinary variation. |
| 08 | Constrain agent behavior | Enforce a live agent’s declared tool boundary and distinguish observed denial from a prohibited call never attempted. |
| 09 | Transfer a runnable package | Assemble the smallest sufficient method, pass clean-session restart and stop/restore, and enable an independent person to operate the package. |

Cases and evidence bundles are **independent**: no gate consumes an earlier module’s product. Capabilities are cumulative: earlier skills are assumed, not retaught as new objectives. Authoritative sequence and supplied inputs are in [COURSE_MAP.md](COURSE_MAP.md). Outcomes are in [LEARNING_OBJECTIVES.md](LEARNING_OBJECTIVES.md). [AUTHORING_GUIDE.md](AUTHORING_GUIDE.md) owns the module contract.

## Core and advanced boundary

A fixed workflow is the highest machinery every core learner operates. Persistent state operation, adaptive flow operation, and multi-agent operation are advanced work. Core learners recognize the trigger, simpler alternative, added risk, and escalation owner.

The core requires zero programming objectives. Dynamic checker implementation, API/MCP construction, custom RAG, agent-runtime development, and deployment remain adapter or builder work.

## Evidence and operating limits

- A person owns consequential acceptance, release, refusal, authority expansion, and residual risk.
- A material acceptance uses independent evidence from a source, deterministic check, or observed state. Public practice files are inspectable.
- Preserve the identity of inputs and checks across a comparison. Authored practice data, hashes, model authorship, and agent role-play do not establish a person's observed performance.
- Every learner both decides and operates. A supported `no-use`, `no-release`, or `no-tool` decision is professional performance and is recorded and studied; it does not satisfy or replace the operation claim.
- A material failure is preserved before repair. Localization-only is held, not recovery completion.
- File presence and refusal prose do not prove execution. Keep actual tool calls, execution results, guard records, and disk snapshots. A technical replay establishes only the behavior it exercised.
- `PASS` and `HOLD` describe technical checks and work decisions, not grades. Preserve a failed attempt, repair its cause, and keep later attempts separate.
- Clean-session restartability and independent-person transfer are separate; neither can substitute for the other.
- Each module bundle contains the artifact/state, decisive evidence, decision, claim result, failure or `HOLD`, scope boundary, and handoff.

## Authoritative files

- [Course map](COURSE_MAP.md)
- [Learning objectives](LEARNING_OBJECTIVES.md)
- [Authoring guide](AUTHORING_GUIDE.md)
- [`modules/core/`](modules/core/)
- [Mission-thread scenario memory](MISSION_THREAD_SCENARIOS.md) — staff specs for session projects; not a lab

Detailed scenarios, commands, forms, answer keys, fixtures, and platform procedures remain outside the core skeleton. Only allowlisted public pages and exercise files enter `site/`; staff references, historical reviews, and answer keys stay outside publication.

## Reader UI and manifest

The 32 instructional destinations share the local Sirocco reader. Edit `ui/course.css` for composition, `ui/course.js` for progressive enhancement, and `ui/theme-init.js` for the before-paint appearance preference. `ui/vendor/sirocco/` contains the byte-identical selected reference assets and their font licenses; course overrides belong outside that vendor directory. No JavaScript bundler, package installation, CDN, or external font service is required.

`course.json` remains the single publication registry:

- Each page has a `kind`: `home`, `overview`, `lab`, `setup`, or `reference`. Each module declares `case_name`, `summary`, and `nav_summary`, and exactly one overview and lab page. `summary` describes the work on the homepage card; `nav_summary` concisely names the main tool or skills beneath the case name in the desktop rail, mobile Course menu, and no-JavaScript navigation. Keep these labels grounded in the module's distinct learning objectives; they wrap naturally rather than truncating.
- Lab `guide` objects list `context_sections` and `optional_sections` by existing H2 ID. Platform setup pages use `guide: {}`. Other page kinds omit `guide`.
- `ui_assets` explicitly maps each UI source to its published destination. Local CSS dependencies must also be declared. The publisher rejects missing dependencies, external CSS resources, unsafe paths, and unexpected output files.
- Figure entries accept SVGs and PNGs. PNGs use standard-library IHDR validation for intrinsic dimensions and the same full-size dialog as SVGs; keep authentic n8n captures under the owning module's `shared/figures/`. Do not feed screenshots into the SVG renderer.
- The homepage hero is the first `.webp` in `ui_assets` and must be exactly 1672×941. Optional photo bands map an id to a declared 1672×716 `.webp` under the top-level `home_bands` key, and each id appears exactly once on the home page as an empty `<div data-photo-band="ID"></div>`. An unknown, repeated, unused, non-empty, or non-home placeholder fails the build. Bands render as decorative, lazy-loaded figures outside search, the outline, and the figure dialog. The publisher reads WebP dimensions from the file header. Course-owned photographs live in `ui/images/`, not in the vendored Sirocco directory; `ui/images/ART_DIRECTION.md` holds their style contract, exact prompts, encode budgets, and provenance.
- The generated `assets/search-index.json` contains instructional prose and heading targets, not fenced commands, raw exercise contents, staff sources, or evidence. Search loads it only when opened.

Do not publish standalone accessibility/equivalent-inspection pages or callouts, scoring rubrics, or exercise-grading guidance. Retain keyboard navigation, figure text, and technical checks.

Every module overview and lab has an **Overview / Lab** switch immediately below its title. Both links come from the module's manifest routes; `aria-current="page"` marks the active page. Keep the switch visible on overview pages as well as labs, at narrow and wide widths, and without JavaScript.

Guided reading keeps commands and their expected, stop, and recovery conditions together. Read full page exposes all procedure bodies and optional/transcript disclosures. Without JavaScript, core instructions remain visible and navigation uses ordinary links and native disclosures. Existing heading fragments remain valid.

Appearance, reading mode, and explicitly selected reading positions use only `reformation-ui:v1:{course-root-pathname}` in local storage. Reset saved place retains appearance and reading mode. These preferences are local navigation conveniences: they store no work, credentials, check results, or completion. Root and prefixed publications use separate keys.


## Pinned execution and publication

Participants need Git, Python 3.12+, Oh My Pi **18.3.5**, a browser, and an ordinary text editor. The only provider credential is `OPENROUTER_API_KEY`, supplied to the current process. Every live exercise selects **`openrouter/anthropic/claude-sonnet-4.6`** through `shared/run_omp.py`. The launcher creates fresh runtime state, exposes only course tools, disables retries and model fallback, and preserves evidence separately from work. The guard is an OMP tool boundary, not an operating-system sandbox.

Modules 02–09 use `shared/prepare_work.py`; Module 01 retains its nine-source starter and Module 00 retains its four-file copy. Helpers refuse existing work/output attempts. A missing key or unavailable pinned provider/model holds the live lane without replacing it with a different model or unlabeled fixture.

Module 6 instead uses local **n8n 2.41.5** on the full approved official Docker stack. The learner builds the router from blank in the browser; no OMP or paid model call participates in routing or comparison. Its preparation path copies only three unchanged wave CSVs, `validate-batch.js`, and `receipt-checker.json`. Original/changed router exports, staff predictions, and native evidence remain private. Run its control regressions with `node --test AI_Harness_Bootcamp_2/module-06-batch-workflow/tests/test_controls.mjs`; native graph and byte-level evidence live under that module's `evidence/native/`.

The child working directory is inside its redirected, fresh HOME. In pinned OMP, `--no-rules` does not disable [ancestor context-file discovery](https://github.com/can1357/oh-my-pi/blob/v18.3.5/packages/coding-agent/src/discovery/helpers.ts); placing cwd beside HOME allowed an outside ancestor's instructions to load. An actual offline OMP replay observed the leak before this placement fix and its absence afterward, with zero provider requests.

`.gitattributes` keeps text checkouts at LF so frozen source/control digests survive Git's automatic line-ending conversion. Native Windows setup also disables `core.autocrlf` for the clone command only. Do not renormalize or reset an existing dirty checkout to repair a hash failure; retain the mismatch and use an intact fresh copy.

Native OMP can exit 0 after an extension preparation error. The launcher still holds an attempt without exactly one completed terminal turn, the expected model identity, complete guard lifecycle, and matching tool/disk receipts. An offline host-invoked guard smoke verifies extension APIs and allow/deny behavior; it is not a model tool call or provider evidence. Runtime evidence files are local audit records, not cryptographic proof against an operator who can rewrite the whole evidence directory.

The saved-evidence audit joins each successful call to its authorization, independent execution check, tool/path identity, and filesystem effect. It also binds `response.md` to the final assistant event; changing only the extracted answer cannot change the recorded model response.

Maintainers need Python 3.12+ and Node.js 22 to publish the course and run the offline checks. From the repository root, create the Python environment once if it does not already exist:

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

Reuse that environment for publication and checks. Run `node scripts/render_figures.mjs` only when figure sources change; a reader UI change does not require regenerating figures.

```bash
.venv/bin/python scripts/build_course.py
.venv/bin/python scripts/check_course.py
.venv/bin/python scripts/build_course.py --check
.venv/bin/python -m http.server 8766 --bind 127.0.0.1 --directory site
```

On native Windows, use `.venv\Scripts\python.exe` for the virtual-environment interpreter. Reuse the environment during correction loops. `check_course.py` never starts paid model calls; live verification is explicit and separately recorded. Serve only `site`, not the repository or staff source tree.

The publisher reports instructional pages, raw downloads, and UI/generated assets separately. `--check` is read-only and compares exact bytes, including search and styles. After a UI change, exercise the built pages in a real browser in Dark and Sand, on narrow and wide viewports, with keyboard navigation, full reading, no JavaScript, print, and a prefixed mount. Preserve screenshots and first-failure records outside the checkout. Browser proof is not native-platform, assistive-technology, provider, or learner-performance evidence.

`site/` is generated output and is not committed. On a fresh clone, install the pinned build dependency and run the publication commands above before serving or deploying. Publish the contents of `site/` as a static site; do not point a host at the repository root. The generated site needs no application server or provider credentials.

The GitHub repository is private. Give participants repository read access before they use the clone instructions; access to a hosted course page does not grant access to the source repository. Each setup route checks existing HTTPS access first. Only failed access enters the official `gh` browser-login fallback. `gh` is a conditional repository-access helper, not a harness or model credential. Its preferred OS credential store can fall back to plaintext; device policy must permit the reported storage before configuring the Git helper for `github.com`.

## Setup maintenance and verification

The five owning procedures are under `AI_Harness_Bootcamp_2/module-00-setup/platforms/`. Keep their commands aligned with the shared credential, version, troubleshooting, and source pages. The supported routes are native Windows PowerShell 5.1; Windows plus WSL 2 Ubuntu 24.04/26.04; macOS 15+ on Apple Silicon or Intel; Ubuntu 24.04/26.04 on x86-64/ARM64; and official Arch x86-64. Intel Homebrew is Tier 3, not equivalent support. Arch package installation is a full upgrade, never a partial `pacman -Sy`.

Preserve the setup boundaries: install only missing prerequisites; verify the exact OMP checksum before execution; preserve conflicting installs, profiles, and dirty checkouts; check saved PATH in an independent terminal without repairing it inside the check; and keep the prerequisite report separate from the live readiness check and actual disk readback. Both report helpers execute Python candidates until a usable 3.12+ interpreter is found. The native helper also tries the Python launcher's version selectors and rejects Store aliases/reparse paths.

Call the setup activity a **readiness check**. Its verifier reports `READINESS CHECK PASS` or `READINESS CHECK HOLD`; the executable remains `verify_tool_proof.py`. The name does not change the token, receipt, identity, or disk-content acceptance checks.

Windows execution policy is not a blanket setup prerequisite. Leave an already permitted policy unchanged. Managed restrictions, signing requirements, and intentional local restrictions require the device owner's approved route. The optional unmanaged-default recovery is explicitly consented, Process-only `RemoteSigned`; closing that PowerShell process ends it.

The hands-on language/setup revision passed all 28 offline gates and publication checks for 32 instructional pages, 663 raw downloads, and 38 UI/generated assets. Actual OMP 18.3.5 installation/checksum and no-key launcher boundaries were exercised in a disposable Apple Silicon home and an Ubuntu 24.04 x86-64 container, including Bash/zsh interactive and login startup. The Ubuntu route also exercised the official prerequisite and `gh` packages. PowerShell 7 parsing and controlled command-boundary checks are not Windows PowerShell 5.1 evidence.

Release evidence remains incomplete: native Windows/WSL, Intel macOS, the other Ubuntu combinations, independent desktop-terminal transitions, GitHub browser authentication, and authorized paid readiness checks remain unobserved for the revised routes. The emulated Arch container could not initialize pacman's syscall sandbox; no sandbox bypass was used to claim an upgrade. A representative nondeveloper's homepage/setup attempt is also unobserved. Browser navigation, clipboard, saved place, keyboard, search, no-script reading, print, and prefixed publication were exercised; narrow DOM checks passed, but narrow screen capture failed in the browser tooling. Keep those limits separate from passed checks. Preserve transcripts and visual evidence outside the checkout; do not describe the five routes as natively verified or the revision as unqualified “S-tier.”

The native Module 6 cutover passed all 27 current scoped gates: 32 instructional pages, 692 raw downloads, and 38 UI/generated assets. n8n 2.41.5 ran in the approved isolated six-service stack on Apple Silicon Docker Desktop. Native form submissions produced both 80-row baselines, the predicted three-lot policy change, and byte-identical restored receipts; independent downloaded checker reports also cover revised inputs, malformed batches, empty routes, and tampered evidence. See `AI_Harness_Bootcamp_2/module-06-batch-workflow/evidence/REVIEW_VERDICT.md` for execution IDs and limits. Bash/zsh and PowerShell parsing plus controlled shell-boundary checks cover all five authored setup routes; they are not native Windows/WSL/Linux runs.

## Netlify deployment

The hosted course is at [reformation-aihb-oct-2026.netlify.app](https://reformation-aihb-oct-2026.netlify.app). Native Netlify builds use the existing GitHub App connection to the private repository and publish successful pushes to `main`.

Root `netlify.toml` selects Python 3.12 and Node.js 22, installs `requirements-dev.txt`, runs the publisher and all course gates, and publishes only `site/`. A failed command blocks publication. Pretty URLs are disabled to preserve the generated `.html` routes.

Manage the shared password in [the Netlify project](https://app.netlify.com/projects/reformation-aihb-oct-2026) under **Project configuration → General → Visitor access → Project visibility**. Keep **Password** selected with **Production and previews** scope. This protects pages, assets, downloads, and immutable deploy URLs. Keep credentials out of Git and build environment variables; the local `NETLIFY_PAT` stays in ignored `.env`.

To reconnect GitHub, open **Project configuration → Developer settings → Continuous deployment → Repository → Manage repository → Link to a different repository** and select `TheHolofex/AIHB_OCT_2026` through the existing Netlify GitHub App. Preserve existing App repository grants. After relinking, confirm `main`, the `netlify.toml` build settings, private deploy logs, and all-deploy password protection. Push a deployment-owned change and confirm the published production deploy's commit matches that push; a successful clone or a build started by relinking does not prove push notifications work.

In the native deploy log, confirm `build.command from netlify.toml`, `PASS: all 27 scoped gates`, and the byte-for-byte publication check. Then check the live password gate and an authenticated download; a ready deploy alone does not verify access protection.

If a private-repository push appears missing, check **Deploys** for **Pending Review** before relinking. Netlify can hold an unrecognized Git author as `unverified-committer`, and the ordinary deploy-list API can omit that request; the site's builds API still lists it. For an author who is already a team member, use **Start approval process → Further action required → Approve and match with existing team member**, select that person, and confirm the match. Do not enable team-wide auto-approval to resolve one author's identity.
