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
- `Facilitated time`
- `Practice time`
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

## Single ownership

| Sub-problem | Owner |
|---|---|
| Delegation, first-use limits, minimum screen, direction, bounded internal acceptance | 00 |
| Source verification and output discernment | 01 |
| Context, reusable instruction, source-as-data control | 02 |
| MCP operation, AI classification judgment, limited tool authority proved by probes, revocation | 03 |
| Hidden-fault diagnosis and recovery | 04 |
| Observed-run analysis and predicate specification | 05 |
| Fixed workflow and deterministic outer-state change | 06 |
| Variation-aware candidate comparison and rollback | 07 |
| Live-agent allow-list, write jail, planted-instruction refuse | 08 |
| Restartability and person-to-person transfer | 09 |

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

The learner can specify a mechanically decidable predicate and configure it in a **supplied deterministic control**. The adapter implements any new checker and owns its identity. If the observed failure is an arbitrary semantic condition that cannot be represented in supplied controls, record the predicate, implementation dependency, owner, and `HOLD`; do not claim the control was implemented.

The fixed workflow is the highest common-core machinery. Persistent state, adaptive flow, multi-agent operation, custom RAG, API/MCP construction, runtime development, and deployment are advanced. A learner who meets a trigger for one of them records the trigger, the simpler alternative, the added risk, and the escalation owner.

## Deterministic and stochastic evidence

Exact blast-radius claims apply to deterministic outer state: input identity, route, status, field presence, policy version, receipts, and controlled deterministic fields. When probabilistic content materially affects acceptance, the run applies the pre-result variation rule below or routes the item to `HOLD`; one generated sample cannot establish exactness.

An output is **material** when a criterion named in the technical acceptance check depends on its content. Declare that classification before the run and apply the supplied control; the producer does not reclassify after seeing output.

Candidate evaluation declares before results one of:

- a deterministic case whose material result is mechanically fixed;
- repeated paired controls with run count and aggregation rule;
- a hard gate that any single violation defeats; or
- exclusion of the stochastic claim from the decision.

## Transfer practice

Clean-session and person-to-person transfer are separate observations. The recipient receives the saved package, operating access, and supplied task. Record what they do, what they ask, and any help they need; use that feedback to improve the package rather than score the attempt.

Preserve technical failures and later attempts separately. A missing recipient is an unobserved transfer attempt, not a learner grade. Do not require a new recipient or unseen task as a condition for trying again.

## Publication check

Publish only when objective/map/module fields agree, every consumed token is supplied and prefixed, the first action can run from verified products alone, failure cannot be mistaken for pass, detailed implementation has not entered core, and every authoritative file names served oracle criteria.

Learner-facing material carries no product token, prefix token, or `PO` identifier. Adapters map them to plain-language records a learner would recognize from ordinary work. `PASS` and `HOLD` are not covered by that ban; see the recorded decision below.

## Recorded decisions

### Maintainer sources and HTML publication

Maintain existing instructional Markdown in its owning module and publish it through `scripts/build_course.py`. Do not add a second learner Markdown navigation path. Only files that learners operate on are raw downloads. `course.json` owns the public allowlist; staff references, historical evidence, and answer keys stay outside `site/`.

Preserve command fence languages, terminal and privilege labels, separate expected output, stop conditions, link destinations, figure descriptions, and text alternatives. Run structural checks against the published HTML. Every procedure gives the purpose, exact action, expected observation, stop condition, and recovery. Use ordinary complete sentences and define each new term at first use. Remove making-of rationale, internal curriculum tokens, section narration, and answer-leading commentary.

The reader sources are `ui/course.css`, `ui/course.js`, and `ui/theme-init.js`. Keep Sirocco vendor files byte-identical; put course-specific changes in the application files. Declare every published UI asset individually in `course.json`; CSS dependencies must resolve inside the same allowlist. Do not copy a public directory recursively or add an external font/script dependency.

The manifest declares each page's `kind`, each module's exact `case_name` and capability `summary`, and one overview and lab route per module. The home source contains exactly one `<div data-course-map></div>`; the publisher supplies its ordered links from that manifest.

Lab pages require `guide: {"context_sections": [], "optional_sections": []}` with existing top-level H2 IDs in the appropriate lists. Setup pages use `guide: {}`; other kinds have no guide. A core group runs from its H2 to the next core, context, or optional boundary. Keep preparation commands under their owning heading, and keep each command with its terminal, expected observation, stop condition, and recovery. Mark the existing outer optional disclosure with `<details class="rf-stretch" markdown="1">`; nested figure-text disclosures are not stretches. An optional top-level H2 belongs in `optional_sections`, not the core sequence. Never renumber or rename existing fragments to make a sequence look regular. New publisher-owned IDs use the reserved `rf-` prefix.

Keep all core/context bodies visible in static HTML. Guided controls, search, copy, appearance, and resume are independent enhancements; their failure must not hide instructions or strand ordinary links. Read full page and printing expose optional work as well as core instructions. A section selection or “Last opened” label never establishes completion or a passed technical check.

Publication uses the existing environment from the repository root: `.venv/bin/python scripts/build_course.py`, then `.venv/bin/python scripts/check_course.py`, then `.venv/bin/python scripts/build_course.py --check`. The gate makes no paid model calls. Compare existing URLs, fragments, command bytes, labeled conditions, the class-only footer, and download/figure bytes when changing the reader. Exercise the actual HTML at root and prefixed mounts; keep visual, keyboard, clipboard, print, and fallback evidence outside the checkout. Do not put browser observations in the live-exercise ledger.


Use `shared/prepare_work.py` for Modules 02–09, Module 01’s starter for its fixed source boundary, and Module 00’s four-file case copy. Work and evidence stay outside the checkout. Refuse existing destinations and retain failed attempts. Only the documented restore operation may replace an authorized work-copy control.

Use the pinned shared OMP launcher rather than direct vendor logins or alternate harness branches. Require Git, Python 3.12+, Oh My Pi 18.3.5, a browser, and a text editor. The exact model is `openrouter/anthropic/claude-sonnet-4.6`; the only participant credential is `OPENROUTER_API_KEY`. Node is a maintainer-only figure prerequisite. Module 03 also uses the free Obsidian desktop application to open its supplied vault; it needs no account, Sync, or community plugin, and the module states the requirement itself. Keep hashing, arithmetic, predicates, routing, and comparisons deterministic.

Record observed exercise outcomes separately from editorial review. Keep live-provider, native-platform, peer-review, and person-to-person transfer observations explicit. Preserve historical evidence without treating an old assessment policy as a current requirement. The 15-minute/eight-term orientation, 120-minute unaided-work limit, and first-result timing remain design targets until measured with people.

### `PASS` and `HOLD` are ordinary English, and they stay

The publication check above once banned any "claim-state word" from learner-facing material, while the frozen Module 0 Reference requires the learner to record `PASS` or `HOLD`, and both words appear throughout the learner surface. Two documents asserting opposite rules is worse than either rule.

Resolved in favour of `PASS` and `HOLD`. A check passes; work goes on hold. Both are words a competent professional already uses at work, and neither reveals anything about how the course is built. The requirement to map internal vocabulary to plain language is satisfied by plain-language forms such as `PASS FOR CLASS REVIEW / HOLD`.

Two limits hold anyway. A recorded `PASS` is the outcome of a check, never the evidence for it — the verification response the learner sees must portray the observed value, so a learner typing `PASS` into a file cannot stand as proof that anything was verified. And the genuinely internal tokens stay banned in learner-facing material: `PO` identifiers, the `VERIFY:` prefix, product tokens, and served-criterion names.
