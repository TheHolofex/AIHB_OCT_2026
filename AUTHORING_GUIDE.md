# Core authoring guide

**Serves oracle:** S02, S04, S05, S06, S07, S08, S09, S10, S11, S12, S14, S15, S16, S17, S18, S19, S20, S21, S24, S25, S26

## Scope and responsibility

This guide governs the Reformation core and its runnable modules. Core files own the capability progression. Module sources own scenarios, commands, forms, practice data, and facilitator procedures. The published HTML is the learner surface.

The learner specifies task-specific behavior, configures bounded values in supplied controls, tests, interprets, and decides. The **adapter implements** executable mechanics, dynamic checks, and evidence export, and supplies every module's case. A builder owns general-purpose code, API/MCP, retrieval pipelines, agent runtimes, and deployment.

Adapter-supplied raw state carries a plain-language legend naming each field and state value. The legend labels; it does not interpret the result.

## Module contract

Every module declares once:

- `Serves oracle`
- `Primary objective`
- `Prerequisites`
- `Consumes`
- `Produces`
- `Rough time`
- `Performance stage`
- `Work surface`
- `Practical work`
- `Performance evidence`
- `Failure / HOLD`
- `Scope boundary`
- `Handoff`

Modules have independent supplied cases, not independent learning objectives. Each module assumes earlier capabilities and extends at least one of them. Every entry in `Consumes` is supplied from outside the module and carries the `VERIFY:` prefix: the learner confirms the supplied input or operating boundary before the attempt. `VERIFY:PREFLIGHT` and `VERIFY:CASE` are universal entry conditions.

No module consumes another module's product. Every token in `Produces` is named in that module's `Performance evidence` or `Check the work` section; the module's own result token records the observed behavior and its limits. A mention in `Handoff` alone does not establish that a product exists.

A module has one primary outcome and at most three numbered enabling objectives. It leaves an evidence bundle describing work, observations, decisions, and unresolved limits. The bootcamp is ungraded: do not add exercise scores, learner pass/fail decisions, qualification ledgers, or reassessment requirements. Technical checks may report `PASS` or `HOLD`; those results describe the work, not the learner.

For each mastery claim, complete “Before this project, the learner could ___. After this project, the learner can ___.” A new file, scenario, tool installation, repetition count, or evidence log is not a new capability. Repeated skills are prerequisites or quality bars. Recover a missing prerequisite explicitly without relabeling it as the current objective.

### Module 02 contract

**Title:** Module 2 · Build and control a reusable second brain

**Mastery:** Using verified sources and bounded direction, construct a small source-traceable knowledge vault, load its governing instruction explicitly, and demonstrate useful retrieval from that knowledge in a fresh session without the source-processing chat or raw packet.

Use exactly three enabling objectives:

1. Select and relate source-backed claims while separating evidence from instructions.
2. Admit reviewed knowledge and prove the saved rule and approved content are what a fresh session used.
3. Improve one substantive weakness and demonstrate the result in a new content revision and fresh run.

Before this project, the learner could verify sources and give bounded direction. After this project, the learner can turn those sources into reviewed, linked knowledge governed by an explicitly loaded saved instruction and demonstrate its use in a fresh session. Source checking remains Module 01's inherited quality bar. Saved instructions and load proof are newly taught here. Bounded multi-agent orchestration belongs to Module 05; checking a received local-model package from a fresh copy remains Module 10's.

**Consumes:** `VERIFY:PREFLIGHT`; `VERIFY:CASE`; `VERIFY:SUPPLIED_GUARD`

**Produces:** `CONTEXT_MAP`; `SOURCE_AS_DATA_CONTROL`; `KNOWLEDGE_VAULT`; `RELOAD_RESULT`; `PO02_RESULT`

The independent Ledger Pike case retains all forty DN sources unchanged. Use Obsidian for local Markdown editing, human admission, and useful links. Fresh retrieval reads only a frozen copy of the learner's navigation and admitted Knowledge notes; raw sources, proposed notes, review notes, and the source-processing chat stay outside that read root. Keep the saved governing instruction outside all model read roots and prove its explicit loading. Preserve earlier content revisions and run evidence when improving a substantive weakness. A reviewed content change and an actual read and citation of the focal note establish what was used; the operator judges the improvement. Changed answer wording alone does not establish improvement.

Legacy P4 is an authoring source only. Record adaptation provenance in Module 02's active staff reference; do not create a runtime dependency on the old checkout or change the frozen historical research reference. Keep reuse rationale and curriculum handoffs out of learner prose.

### Module 05 contract

Before this project, the learner could direct and verify one bounded assistant run. After it, the learner can supervise a dependency-aware native OMP agent team, accept its handoffs, and recover a partial failure without discarding valid independent work. Use the three enabling objectives in `LEARNING_OBJECTIVES.md`: decomposition and complete delegation contracts; native fan-out/fan-in with dependent review and source adjudication; selective recovery with dependency invalidation.

The learner owns the work graph, assignment briefs, acceptance, and decision to use the combined result. OMP owns native child execution. The supplied adapter prepares resources, limits the tool surface, preserves native records, and checks evidence; it must not secretly replace delegation with a custom scheduler or prewritten outputs. Use read-only specialists and reviewer, one coordinator-owned output, bounded concurrency and depth, explicit stop conditions, and no implicit retry or model fallback. A task batch is not an ordered dependency graph.

**Consumes:** `VERIFY:PREFLIGHT`; `VERIFY:CASE`; `VERIFY:NATIVE_TASK`; `VERIFY:ORCHESTRATION_CONTROLS`

**Produces:** `WORK_GRAPH`; `AGENT_HANDOFFS`; `PARTIAL_RECOVERY`; `INTEGRATED_BRIEF`; `PO05_RESULT`

Native child completion and artifact presence are not acceptance. Join actual requests, child sessions, results, source identities and permitted effects. A missing input must produce an observed blocked attempt; a selective repair retains that attempt and identifies which prior work remains valid. Review consumes the actual candidate and source evidence after its prerequisites, not merely a request to “review the above.” A source or brief change invalidates its consumers and downstream integration. Keep model proposals, deterministic checks, and human acceptance separate. Historical renderer-repair evidence does not establish this replacement's behavior.


## Single ownership

| Sub-problem | Owner |
|---|---|
| Minimum screen, planned long-document drafting one session per section, separate review sessions with verified findings, targeted revision, bounded internal acceptance | 00 |
| Source verification and output discernment | 01 |
| Human-reviewed knowledge vault, saved instruction and load proof, source-as-data control, fresh-session retrieval | 02 |
| MCP operation, AI classification judgment, limited tool authority proved by probes, revocation | 03 |
| Typed-question decomposition, read-only decision runs, measured confidence gates, code-owned routing | 04 |
| Native OMP team decomposition, evidence-bearing handoffs, dependent review, selective recovery | 05 |
| Observed-run analysis and predicate specification | 06 |
| Model-driven tool use that produces a real structured-data artifact, with observed execution and downloaded-file inspection | 07 |
| Hallucination control with structured claim checks, isolated reviewer agents, correction, re-review and human disposition | 08 |
| Live-agent allow-list, write jail, planted-instruction refuse | 09 |
| Package local-runtime instructions/controls (no undeclared deps) for fresh-terminal structure verification | 10 |

## Responsibility before release

The minimum responsibility screen — source/data authority, sensitive-data boundary, affected audience or person, disclosure need, consequential authority, and human decision owner — is a standing rule applied in every module to its own supplied case. Modules 00–02 can make only bounded internal-acceptance decisions.

Module 03 owns MCP operation, judging an AI's classifications against stated rules, and limiting a tool's authority. A transcript in which the model never attempted a forbidden action does not show that a limit holds; a probe that attempts the action does. Every learner practices both the classification claim and the authority claim. Study a refusal to connect without treating it as evidence that a tool was operated.

## Evidence standard

Every bundle contains:

- work product or operated state;
- strongest independent result;
- learner decision and owner;
- observed result and its limits;
- failure or `HOLD` when applicable;
- substitution record when a named dependency was replaced — what was replaced, the same-state basis, who certified it, and the affected outcome;
- scope boundary; and
- handoff.

Independent evidence checks the producer’s claim against a separately inspectable source, deterministic rule, or observed state. Preserve inputs, check identities, and observed results so another person can inspect the comparison. Public practice files are inspectable. Authored fictional corpora and paired outputs are labeled practice data, not live OpenRouter receipts.

An executed tool claim requires the actual assistant call, execution result, guard decision, and disk effect. A refusal sentence is not a tool denial. Distinguish `DENIED_BY_GUARD`, `DENIED_BY_RUNTIME`, `NOT_ATTEMPTED`, and `VIOLATION`. Missing or incomplete receipts hold the affected claim. The OMP extension limits the tools exposed to the model; it is not an operating-system sandbox or a defense against malicious local processes.

## Nondeveloper and dynamic-check boundary

The learner specifies and configures bounded behavior in **supplied controls**: questions, thresholds, policies, and rules written in the formats those controls read. The adapter implements any new checker, router, or runner and owns its identity. If a needed behavior can't be expressed in a supplied control, record the behavior, implementation dependency, owner, and `HOLD`; do not claim the control was implemented. A model-backed control is pinned to one model and version, and its evidence records the build that answered.

The core includes bounded native OMP multi-agent orchestration and task-bounded automation, not agent-runtime development. Module 05 permits read-only specialists and a reviewer under one coordinator-owned output; learners configure supplied roles and briefs rather than build a scheduler. Module 07 connects one n8n agent to one spreadsheet-writing tool; it does not grant arbitrary file access or make a chat reply proof of an artifact. Module 08 adds a bounded human-started read-only ensemble: reviewers receive isolated inputs, the correction stage sees completed reviews as evidence, and fresh reviewers recheck the entire correction. No model vote grants authority. The core also permits one narrow form of persistent knowledge: a local, human-reviewed Markdown vault with explicit admission and read-only fresh-session retrieval. Autonomous state updates, concurrent agent writes to shared knowledge, unattended or recursively expanding teams, adaptive flow, custom retrieval infrastructure including custom RAG, API/MCP construction, runtime development, and deployment remain advanced. A learner who meets one of those triggers records the simpler alternative, added risk, and escalation owner.

## Deterministic and stochastic evidence

Exact blast-radius claims apply to deterministic outer state: input identity, route, status, field presence, policy version, receipts, and controlled deterministic fields. When probabilistic content materially affects acceptance, the run applies the pre-result variation rule below or routes the item to `HOLD`; one generated sample cannot establish exactness.

An output is **material** when a criterion named in the technical acceptance check depends on its content. Declare that classification before the run and apply the supplied control; the producer does not reclassify after seeing output.

Candidate evaluation declares before results one of:

- a deterministic case whose material result is mechanically fixed;
- repeated paired controls with run count and aggregation rule;
- a hard gate that any single violation defeats; or
- exclusion of the stochastic claim from the decision.

## Transfer practice

Clean-session restartability and fresh-terminal structure check are separate observations. Freeze the declared ten-file bundle (`E/bundle-before.json`) and make a digest-checked copy into the fresh folder `F`. In a new terminal inside `F`, run `scripts/check_package.py shared/PACKAGE.md` and record `PASS: package structure checked`. The structure check reads the package's named fields and confirms every file it names is inside `F`; it does not run the package's commands. Record the check and unresolved limits in `E/close-out.md`.

## Publication check

Publish only when objective/map/module fields agree, every consumed token is supplied and prefixed, the first action can run from verified products alone, failure cannot be mistaken for pass, detailed implementation has not entered core, and every authoritative file names served oracle criteria.

Learner-facing material carries no product token, prefix token, or `PO` identifier. Adapters map them to plain-language records a learner would recognize from ordinary work. `PASS` and `HOLD` are not covered by that ban; see the recorded decision below.

## Recorded decisions

### Maintainer sources and HTML publication

Maintain existing instructional Markdown in its owning module and publish it through `scripts/build_course.py`. Do not add a second learner Markdown navigation path. Only files that learners operate on are raw downloads. `course.json` owns the public allowlist; staff references, historical evidence, and answer keys stay outside `site/`.

Preserve command fence languages, terminal and privilege labels, separate expected output, stop conditions, link destinations, figure descriptions, and text alternatives. Run structural checks against the published HTML. Every procedure gives the purpose, exact action, expected observation, stop condition, and recovery. Use ordinary complete sentences and define each new term at first use. Remove making-of rationale, internal curriculum tokens, section narration, and answer-leading commentary.

The reader sources are `ui/course.css`, `ui/course.js`, and `ui/theme-init.js`. Keep Sirocco vendor files byte-identical; put course-specific changes in the application files. Declare every published UI asset individually in `course.json`; CSS dependencies must resolve inside the same allowlist. Do not copy a public directory recursively or add an external font/script dependency.

The manifest declares each page's `kind`, each module's exact `case_name` and capability `summary`, its learner-facing `outcomes` (`can`: one sentence of at most 320 characters completing "After this assignment you can"; `will`: two to four "You will…" items, free of staff tokens), and one overview and lab route per module. The publisher renders the outcomes and a device-local progress panel on each overview and the course map; do not restate them in the Markdown. The home source contains exactly one `<div data-course-map></div>`; the publisher supplies its ordered links from that manifest.

Lab pages require `guide: {"context_sections": [], "optional_sections": []}` with existing top-level H2 IDs in the appropriate lists. Setup pages use `guide: {}`; other kinds have no guide. A core group runs from its H2 to the next core, context, or optional boundary. Keep preparation commands under their owning heading, and keep each command with its terminal, expected observation, stop condition, and recovery. The publisher turns a `**Terminal: …**` label plus its fence into a command card, pairs a Bash card that is immediately followed by its PowerShell twin into one shell switch, and renders the Expected/Stop/Recovery paragraphs as callouts; quote the exact lines a script prints rather than paraphrasing them. Each numbered step gets a step number and a device-local done control; a non-procedure closing H2 (`before-you-stop`, `class-only-boundary`, `timebox`) belongs in `context_sections` so it is not counted as a step. Every lab that records `RUN` saves it to `$HOME/course-evidence/module-NN-run` and carries an `### If you open a new terminal` subsection that reads it back; every lab that makes a paid call carries the standard `### Enter your key in this terminal` subsection before the first launcher command. Mark the existing outer optional disclosure with `<details class="rf-stretch" markdown="1">`; nested figure-text disclosures are not stretches. An optional top-level H2 belongs in `optional_sections`, not the core sequence. Never renumber or rename existing fragments to make a sequence look regular. New publisher-owned IDs use the reserved `rf-` prefix.

Keep all core/context bodies visible in static HTML. Guided controls, search, copy, appearance, and resume are independent enhancements; their failure must not hide instructions or strand ordinary links. Read full page and printing expose optional work as well as core instructions. A section selection or “Last opened” label never establishes completion or a passed technical check.

Publication uses the existing environment from the repository root: `.venv/bin/python scripts/build_course.py`, then `.venv/bin/python scripts/check_course.py`, then `.venv/bin/python scripts/build_course.py --check`. The gate makes no paid model calls. Compare existing URLs, fragments, command bytes, labeled conditions, the class-only footer, and download/figure bytes when changing the reader. Exercise the actual HTML at root and prefixed mounts; keep visual, keyboard, clipboard, print, and fallback evidence outside the checkout. Do not put browser observations in the live-exercise ledger.


Use `shared/prepare_work.py` for Modules 02–10, Module 01’s starter for its fixed source boundary, and Module 00’s case copy (the request, the style rules, the checker, and six sources). Work and evidence stay outside the checkout. Refuse existing destinations and retain failed attempts. Only the documented restore operation may replace an authorized work-copy control.

Use the supplied OMP launchers rather than direct vendor logins or alternate harness branches. Require Git, Python 3.12+, the latest stable Oh My Pi release, a browser, and a text editor. Setup resolves one official latest release and verifies its binary against the same release's checksums. Record the actual OMP version in each attempt; audit saved identities without imposing a numeric course version. The exact model is `openrouter/anthropic/claude-sonnet-4.6`; the only participant credential is `OPENROUTER_API_KEY`. Node is a maintainer-only figure prerequisite. Module 03 also uses the free Obsidian desktop application to open its supplied vault; it needs no account, Sync, or community plugin, and the module states the requirement itself. Keep hashing, arithmetic, predicates, routing, and comparisons deterministic.

Module 02 also requires Obsidian for local Markdown editing. Do not add community plugins, Sync, a REST API, or an MCP service to its core workflow. Reuse `shared/run_omp.py` and `shared/course_guard.mjs` unchanged.

Record observed exercise outcomes separately from editorial review. Keep live-provider and native-platform observations explicit. Preserve historical evidence without treating an old assessment policy as a current requirement. The 15-minute/eight-term orientation, 120-minute unaided-work limit, and first-result timing remain design targets until measured with people.

### `PASS` and `HOLD` are ordinary English, and they stay

The publication check above once banned any "claim-state word" from learner-facing material, while the frozen Module 0 Reference requires the learner to record `PASS` or `HOLD`, and both words appear throughout the learner surface. Two documents asserting opposite rules is worse than either rule.

Resolved in favour of `PASS` and `HOLD`. A check passes; work goes on hold. Both are words a competent professional already uses at work, and neither reveals anything about how the course is built. The requirement to map internal vocabulary to plain language is satisfied by plain-language forms such as `READY TO SEND / HOLD`.

Two limits hold anyway. A recorded `PASS` is the outcome of a check, never the evidence for it — the verification response the learner sees must portray the observed value, so a learner typing `PASS` into a file cannot stand as proof that anything was verified. And the genuinely internal tokens stay banned in learner-facing material: `PO` identifiers, the `VERIFY:` prefix, product tokens, and served-criterion names.
