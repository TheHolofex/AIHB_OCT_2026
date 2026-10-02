# Staff reference: Module 2 · Build and control a reusable second brain

This active staff reference defines the source-to-vault-to-cold workflow and its semantic review. Keep it outside learner downloads, search, prompts, model read roots, and prepared work copies. Historical evidence and reviews remain unchanged; they describe earlier exercises and do not prove this workflow.

## Capability and boundary

Using verified sources and bounded direction, the learner constructs a small source-traceable knowledge vault, explicitly loads its governing instruction, and demonstrates useful retrieval in a fresh session without raw sources or the processing chat. The three enabling objectives are source-backed selection/relationships with evidence separated from instructions; human admission with saved-rule/content-use proof; and one substantive improvement demonstrated in reviewed content and a fresh run.

Source verification and bounded direction are earlier capabilities. Saved instruction files and proof of their load are newly taught here. Do not turn this into hidden-fault diagnosis, person-to-person transfer, code writing, plugin setup, autonomous state maintenance, or a scored qualification exercise.

The supplied forty DN notes, file screen, shared launcher, and shared tool guard remain unchanged. Runtime assets belong to this repository. The original P4 checkout is an authoring source only, never a learner dependency.

## P4 reuse provenance

The following originals were read during authoring under `/Users/ravistarzl/Documents/GitHub/AI_Harness_Bootcamp/`. These paths document provenance; the new module must run without that checkout.

| Original | Retained idea | Adaptation and exclusions |
|---|---|---|
| `mission_flesh/p4/vault_seed/templates/NOTE_TEMPLATE.md` | Note identity, source identity, exact support, uncertainty, linked body | KB filename is identity; H1 is title; four ordered Markdown sections replace frontmatter. The helper derives locators/hashes. Remove route legs, modes, threat taxonomy, confidence labels, absent source URLs/publisher fields, and manual JSON/YAML. All shipped slots are blank. |
| `mission_flesh/p4/vault_seed/MOC.md` | A navigable entry point into knowledge | One learner-authored title and Knowledge-link list, with every admitted note reachable. Remove prescribed logistics hubs, Mission_Brief, and prebuilt answer paths. |
| `mission_flesh/p4/vault_seed/Notes/Route/Spine.md` | Relationships that make a sequence interpretable | Learners link claims, qualifications, competing sources, and consequential sequence among existing Knowledge files. No supplied route spine, answer graph, six-hub requirement, or eight-note quota. |
| `site/blocks/p4.html`, Stage 05 before line 418 | Candidate admission with rejected items and reasons | A human reviews in Obsidian, prepares Knowledge bytes, and records short reasons before helper admission. The model does not write admitted content; no director, worker dispatch, MCP receipts, or automatic merge. |
| `site/blocks/p4.html:418–529`, Stages 06–08 | Brain-only cold query, human audit, applied repair, fresh repair proof | Freeze only MOC and reviewed Knowledge; retrieve with course_read in a fresh process. Audit names a focal note, weakness, before/after, expected and observed effects. Review all changed notes and freeze a new revision. Audit itself is outside the cold read root. Do not copy tank/logistics questions, grading, OpenCode configuration, MCP write steps, or dependencies on another project's artifacts. |
| `mission_flesh/p4/vault_seed/tools/verify_baseline.py`, `manifest_files`, `manifest_fingerprint`, `check_manifest` | Sorted file identities; detect added, changed, missing content | Module-owned helper uses explicit cold membership, path/byte-size/digest entries and canonical-JSON fingerprint, external identity records, no-overwrite publication, and link rejection. The old implementation skipped links and fingerprinted path/hash lines; neither behavior is retained. No legacy internal-manifest mode. |
| `mission_flesh/p4/vault_seed/tools/verify_brain.py`, `validate_note`, `validate_source`, `resolve_wikilink`, `validate_wikilinks` | Source-bound metadata and resolvable relationships | Fixed plain-Markdown sections and exact quote matching; case-sensitive Knowledge paths; only unique DN source IDs get short-name resolution. Do not transplant optional PyYAML, permissive nested-key handling, general basename fallback, logistics validation, volume quotas, or artifact-presence-as-proof. |

## Fixed working contract

The editable Obsidian root is `W/vault`. The source-processing read root is `W/vault/Sources`; a cold read root is `W/cold/<revision>`. `W/shared/controls/SAVED_INSTRUCTION.md` stays outside both roots and is injected explicitly by the launcher. `E` is a fresh sibling of W outside the checkout.

Initialize records the original source and rule identities and seeds only forty source notes, blank templates, and blank navigation. Ingest reads forty distinct sources once, audits actual receipts, and stages independent valid proposals under Drafts. Three to five notes is a workload guide, never a checker quota. Per-proposal invalidity produces an entry in `W/reviews/ingest-report.json`, not a Draft file; independently valid proposals still stage. That report is the unstaged proposal's machine defect record, so no rejection command is needed for it. Top-level malformed JSON fails before staging and before report creation. Use the terminal HOLD, preserved `E/ingest/response.md`, and runtime evidence to distinguish it from runtime-proof failure. After runtime proof passed, the learner may repair or author replacement Knowledge from blank Markdown without another paid ingestion. Runtime-proof failure means stop.

A preflight exit 2 without an evidence directory preserves a preflight record and releases only that invocation's reservation. Any created evidence, unexpected exception, or other result consumes the ingest. No automatic retry, provider fallback, model substitution, or evidence overwrite is permitted.

A human copies promising Draft text or the blank template into Knowledge, checks exact source excerpts, populates target notes before links, completes the MOC, and records reasons under vault/Reviews. Review does not copy or rewrite Knowledge. It records note identity, decision, source identity, and the reason text/hash externally. Rejection requires an existing staged Draft file but does not require valid citations; edited or malformed Draft text can still receive a rejection record. Never direct rejection at an invalid proposal that did not stage. Human-authored notes use the same admission route.

The note contract is filename `KB-NNN.md`, nonempty H1 title, and exactly one ordered Claim, Limits and conflicts, Evidence, Related H2. Replace the blank template's bare first-line `#` with `# ` followed by a chosen title. Evidence uses source-link H3s and exact blockquotes. Remove one presentation quote marker and optional space per line; preserve literal source characters, with only CRLF normalization. Knowledge links use exact vault-relative `Knowledge/KB-NNN` paths. Source links accept unique `DN-NNN` or `Sources/DN-NNN` identities. Source mode is essential when copying meaningful Markdown bytes. Do not teach learners to edit hashes, locators, JSON, YAML, or captured responses.

Teach MOC with `# ` followed by a title on its first line, then one `- [[Knowledge/KB-NNN|label]]` entry per nonblank line. No surrounding answer prose, subheading, numbered bullet, or trailing text is allowed. The learner supplies the title, existing note IDs, and navigation labels; no completed graph is provided.

Freeze requires matching admissions for every Knowledge file, including an accidentally created empty one, plus coherent links and navigation. Missing admissions name every affected note with fully quoted Bash/zsh and PowerShell review commands. Their reason-file paths must be created and filled or replaced with actual reason paths under `vault/Reviews` before execution. A v2 revision verifies v1 independently of live bytes, requires new/changed Knowledge with fresh matching reviews, forbids deletion of earlier Knowledge, and binds a changed/new focus note. MOC and reciprocal links may change. Frozen content is exactly MOC plus admitted Knowledge. Reviews, Templates, Drafts, Sources, `.obsidian`, chat, staff material, and identity records are excluded.

The manifest is external, schema version 1, with sorted `{path, bytes, sha256}` entries, root fingerprint, source/rule identities, review-receipt hashes, previous-manifest hash, and focal note (null for v1). Check compares frozen bytes and immutable source/review identities, not later live Knowledge or editable reason notes. Identity is not truth, authority, authorship proof, or tamper-proof custody.

## Runtime proof and judgment

For each paid phase require the shared audit, `policy.profile == 'read'`, `policy.tools == ['course_read']`, exact canonical phase root, actual prompt hash, and non-null saved-rule identity matching initialize and the cold manifest. Instruction-loaded evidence precedes provider contact and matches the rule's loaded text. Require unchanged inputs and empty output hashes. The shared launcher and guard are reused, not reimplemented.

Ingest needs forty distinct executed DN file reads; 39 plus a duplicate is insufficient. Retrieval needs an actual MOC read and actual reads of every cited frozen KB. Successful file reads must be frozen members. A listing is not an evidence read. A later revision must read and cite its focal note. No raw packet, Draft, chat, audit, or staff answer is successfully read.

Call classifications remain observational: EXECUTED; ALLOWED_ABSENT for allowed in-root missing paths with no executed read; DENIED when the guard refuses the call or the runtime rejects an unavailable tool before the guard runs; and NOT_ATTEMPTED when no relevant call exists. A pre-hook denial has a runtime rejection but no guard decision row, and the shared audit must still pass. Raw-source observations inspect path references in all string argument values, including nested objects and arrays; they do not prove a read. An ALLOWED_ABSENT observation alone is not raw access or a helper failure. Preserve errors and any shared-audit failure. Do not claim a live denial without an actual denied call. Existing offline guard tests establish containment; this module does not require a live adversarial probe.

Cold response is exactly three unique Q1/Q2/Q3 entries under `answers`, each with status, answer, and citations. Supported entries require citations. Each citation's frozen, actually read KB must contain the DN identity and exact Evidence excerpt (an exact contiguous subexcerpt is permitted). Unsupported answers may cite partial evidence but must state the missing support. The helper checks structure and provenance; the operator judges completeness, uncertainty, and semantic honesty.

Missing saved instruction is prerequisite exit 2 before provider contact or evidence creation. Rename only the work-copy rule; restore identical bytes, then use cold-v2 as the restored positive. Never count the synthetic oracle as an observed provider or human run.

## Staff semantic checks — never seed into learner assets

Check against the actual unchanged DN text, not only a fluent answer:

| Question | Material support and limits |
|---|---|
| Q1: current height, competing record, authority | DN-014 gives C-44 inner height **0.92 m at 10:48 MDT**, explicitly not quality release or QP-17 assignment. Its quoted instruction is not an order to obey. DN-037's **0.80 m** card dated 2 October is marked stale and must not supersede the current bench measurement. |
| Q2: separate states at 12:15 | DN-028 records a **blank quality line at 11:50**, no quality signature, and **QP-17 unassigned**. Do not turn that observation into a fabricated later release. DN-005 records a **received, unapproved permit** with blank approval line. DN-040 records **no crate stamp at 12:15**. Receipt, quality release, vehicle assignment, permit approval, and stamping are distinct. |
| Q3: sequence and missing authority | DN-003's **11:40 paper arrival** is paper receipt only. DN-006 says the gate **closed at 11:55**, before the **12:15 decision**, and an open road does not reopen the gate. Paper arrival establishes neither release nor movement authority. Preserve the separate absent authorities rather than inventing dispatch permission. |

For every material statement, check a cited KB actually read and its underlying DN/excerpt. Human source inspection may follow original links outside the cold runtime. A truthful unsupported v1 answer is an audit target, not a runtime failure. Check collective coverage before v1, but never force fabricated coverage. All three final answers require source-backed support; a remaining gap requires another substantive reviewed revision and fresh run.

The audit must name one changed/new focal note, substantive weakness, before/after, expected effect, and observed effect. Useful qualifications or counter-sources are valid if v1 was already correct. Cosmetic edits and MOC-only changes do not satisfy the human check. Answer wording need not change; report unchanged correct wording honestly. The helper establishes reviewed byte changes and focal-note read/citation, not semantic improvement.

## Delivery and evidence

Use 180 facilitated minutes: 15 orientation, 15 walkthrough, 120 practice (10 setup/open, 15 source pass, 35 review/link/admit, 15 first cold, 30 audit/improve/retest, 15 missing-rule/identity/close), 30 discussion. These are planning allocations, not observed timing.

Retain meaningful file-screen behavior and helper mutation/oracle checks. The live prose digest gate and reference sidecar are removed rather than repinned. Historical records naming an earlier digest remain historical. Independent review must inspect actual files and observed evidence. Staff answers, completed vaults, local receipts, and screenshots must not enter publication or model roots.

Actual Obsidian observation includes link following, externally staged Draft refresh, an edit saved to disk, and close/reopen. A file checker or automation pilot does not prove a human learner acted. Keep observed GUI/platform scope, runtime completion, provenance, semantic judgment, and human observation separate. No qualification or score is inferred.
