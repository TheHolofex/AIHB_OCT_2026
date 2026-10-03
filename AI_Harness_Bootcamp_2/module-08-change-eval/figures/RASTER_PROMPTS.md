# Raster figure prompts and provenance — module-08-change-eval

Staff-only record. Not published (absent from `course.json`).

- Generator: `codex-cli 0.154.0` (`codex exec`, ChatGPT login, built-in `image_gen`).
- Style references attached to every invocation: `ui/images/home-hero.webp` and `ui/images/home-band-custody.webp`, decoded losslessly to PNG with `dwebp`; every figure except `m00-bounded-direction` also received the accepted `m00-bounded-direction` attempt-01 raster as a style-only reference. Label edits additionally attached the image being edited as the first input.
- Post-processing: the generator returns RGBA with a transparent ground. Each accepted raster was alpha-composited onto the specified `#0D0906` ground and saved as opaque lossless RGB PNG at native size. No other pixel changes, no resizing.
- Run evidence (all attempts, logs, rejected rasters, reviews): `~/course-evidence/course-raster-visuals/20261002T233502`
- Module source contract: `module-08-change-eval/shared/MODULE_08_LAB.md` §§Freeze your rule and input identities, Check the baseline, Make the bounded adoption decision, Demonstrate restoration, and the optional live-comparison disclosure; `shared/controls/policy.json` and `hard_gates.py`. Supplied-file evaluation and optional paid live observation are separate evidence lanes.
- Owning page digests at integration (SHA-256): `README.md` e6971fccd74be6d0…; `shared/MODULE_08_LAB.md` 48f974930e455e61…

## m08-bounded-decision

- Title: `KEEP THE CLAIM INSIDE THE EVIDENCE`
- Publication path: `shared/figures/m08-bounded-decision.png`
- Anchor: Lab `## Make the bounded adoption decision`.
- Caption: State only what the observed comparison supports, and keep the failed-case repair proxy separate from measured time, token usage, and cost estimates.
- Native size: 1536×1024; published SHA-256: `14f50a29c4af4cf7e8a2564b0697d67c04f2c1ac12a56b03841e65096efa79a8`
- Iteration history:
  - attempt-01: full generation; session `01a1005a-796d-7351-9aba-664684923fe3`; raw SHA-256 `6fc327ef1f980274…`; superseded — review: m08-bounded-decision: raise size and contrast of the repair-proxy sub-label
  - attempt-02: full generation; session `01a1006f-32d9-70e2-81ac-d2c227d0a6cf`; raw SHA-256 `36afa4b06863c159…`; ACCEPTED
- Final review outcome: accepted attempt-02. F08: m08-bounded-decision: ACCEPT_A2 — all 10 labels exact; boundary built from the four evidence labels; `No unseen-case claim` outside; three separate cells; repair-proxy sub-label now about 42 px and bright; provider-bill cell dashed.

### Final prompt

````text
## 1. Tool/output instruction

$imagegen Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

## 2. Lesson contract

- Owning module/page/H2: Module 08 — Slope Brief; page `AI_Harness_Bootcamp_2/module-08-change-eval/shared/MODULE_08_LAB.md`; H2 `## Make the bounded adoption decision`.
- Learning takeaway (caption, HTML text only): "State only what the observed comparison supports, and keep the failed-case repair proxy separate from measured time, token usage, and cost estimates."
- Learner action in unfamiliar work: write an adoption decision scoped to the cases actually observed, the rule frozen beforehand, the named configuration, and the repetitions actually run; report the count of failed cases as a repair proxy and keep it in a separate column from elapsed time, token counts, and SDK cost estimates, treating the provider bill as unknown unless independently checked.
- Misconception prevented: that passing observed cases licenses a claim about unseen cases or general superiority, that a failed-case count is a measured repair time, or that an SDK cost estimate is the provider bill.

## 3. Composition

- Category: containment (claim boundary) plus a separated measurement strip.
- Canvas: 1536×1024 landscape, 64 px safe margin. Title zone across the top. Upper mechanism area (about 60% of remaining height) for the boundary; lower area for the measurement strip, clearly separated by a gap and thin `#3A2E1B` rule.
- Upper area: a large gold-edged boundary enclosure. Its four sides (or four corner anchors) are labeled by the evidence that forms it: `Observed cases`, `Frozen rule`, `Named configuration`, `Actual repetitions`. Inside the enclosure, centered: the decision block `Bounded decision`. Outside the enclosure, to the right, with no trace entering the boundary: a faded/neutral region labeled `No unseen-case claim` (outside the line, separated; may use a `#B43A2F` thin stroke to mark it as excluded).
- Lower measurement strip, separate cells side by side with visible gaps (not one merged bar): cell 1 `Failed-case count` with a sub-label directly under it `Repair proxy, not repair time`; cell 2 `Elapsed time / tokens / SDK estimate`; cell 3 `Provider bill: unobserved unless checked` (neutral/dashed border to show not observed). No connector merges these cells, and no connector from the strip into `Bounded decision` adds them together.
- Reading order: title → the four boundary-forming labels → `Bounded decision` → outside `No unseen-case claim` → measurement strip left to right.
- Focal relationship: the decision sits inside the boundary built from observed evidence; the unseen-case claim stays outside.
- No arrows implying approval. No decorative connectors. Inline course image; no slide-overlay space.

## 4. Verbatim label map

Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts.

- Title zone: `KEEP THE CLAIM INSIDE THE EVIDENCE`
- Boundary sides/anchors: `Observed cases`; `Frozen rule`; `Named configuration`; `Actual repetitions`
- Inside boundary: `Bounded decision`
- Outside boundary: `No unseen-case claim`
- Measurement strip cell 1: `Failed-case count`
- Measurement strip cell 1 sub-label: `Repair proxy, not repair time`
- Measurement strip cell 2: `Elapsed time / tokens / SDK estimate`
- Measurement strip cell 3: `Provider bill: unobserved unless checked`

No other text: no counts, durations, token numbers, currency, case IDs, Yes/No, or step numbers.

## 5. Visual family

`#0D0906` primary ground; `#17110C` panel fill; `#A58650` primary gold; `#C8A96A` sheen and connector highlights; `#C8B78A` secondary readable text; `#FFF8E7` primary text; `#655337` subdued nonessential rules; `#3A2E1B` faint structural lines; `#4F5634` restrained verified/allowed accents; `#B43A2F` warnings/blocked branches; `#2D3030` neutral mechanisms. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities. Here: boundary in gold `#A58650` with `#C8A96A` sheen; `Bounded decision` in a deep panel with olive `#4F5634` inner accent; `No unseen-case claim` region with a `#B43A2F` thin stroke and off-white text (text must stay fully legible, not faded); measurement cells neutral `#2D3030`; provider-bill cell with dashed `#655337` border.

## 6. Richness and legibility

Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use clean Inter/Helvetica-like sans-serif; exact filenames/tokens may use a clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density.

## 7. Honesty/exclusions

No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Module-specific: do not show an adopt/reject outcome, a winning candidate, a chart, gauges, clocks with times, coin/dollar stacks, invoices, token counts, or any number; do not imply the SDK estimate equals a bill; do not connect the measurement cells into a single sum.

## 8. Generation self-check

Must remain obvious: `Bounded decision` sits inside a boundary formed by `Observed cases`, `Frozen rule`, `Named configuration`, `Actual repetitions`; `No unseen-case claim` sits outside; the three measurement cells are separate, with `Failed-case count` marked `Repair proxy, not repair time`. Unusable if: any of the ten labels is missing or altered; `No unseen-case claim` is placed inside the boundary; the measurement cells merge or feed the decision as a total; the provider-bill cell looks observed; any number or currency appears.

## 9. Revision requirements from review of the previous attempt
A previous generation of this figure was rejected. Generate a NEW image from this full contract and fix every defect below. All earlier blocks still govern; labels stay verbatim; add no words. Title text sits directly on the dark ground with no white bloom/haze band.

- m08-bounded-decision: raise size and contrast of the repair-proxy sub-label
Transcription: KEEP THE CLAIM INSIDE THE EVIDENCE / Observed cases / Frozen rule / Named configuration / Actual repetitions / Bounded decision / No unseen-case claim (broken over lines at its own hyphen, which is acceptable) / Failed-case count / Repair proxy, not repair time / Elapsed time / tokens / SDK estimate / Provider bill: unobserved unless checked. All 10 labels are exact, with no numbers, currency, or outcome. The four labelled corners form the boundary around `Bounded decision`. `No unseen-case claim` sits outside it in a brick-red stroked panel with no trace entering. The three measurement cells are separate, and the provider-bill cell is dashed. This matches the lab: the bounded adoption decision, failed-case repair count kept separate from elapsed time, tokens, and the SDK estimate, and the provider bill unknown unless observed. One defect: `Repair proxy, not repair time` is the decisive distinction for that cell, but it renders at about 26 px in dim tan. That is below the 32 px minimum and breaks the 'never dim essential words into low-contrast tan' rule, so it fades at article width. Verdict: LABEL_EDIT. Fix: in measurement cell 1, re-render `Repair proxy, not repair time` at 32 px or larger in #C8B78A or brighter, keeping it directly under `Failed-case count`. Change nothing else.
````

## m08-evidence-lanes

- Title: `SEPARATE CHANGE FROM VARIATION`
- Publication path: `shared/figures/m08-evidence-lanes.png`
- Anchor: Overview `## The hard gates`; replace `m08-variation.svg`.
- Caption: Supplied-file checks do not measure model variation; repeated live pairs separate observed between-instruction disagreements from within-instruction variation.
- Native size: 1536×1024; published SHA-256: `94f5076ff0c19b9270ac7d0aa222a5e45ee3df444ba6719f4de9a091175c2e01`
- Iteration history:
  - attempt-01: full generation; session `01a1005b-588e-7491-90fb-d8991d4e5099`; raw SHA-256 `dac07d2f6e0de092…`; superseded — review: m08-evidence-lanes: stop pooling both lanes into one reject band
  - attempt-02: full generation; session `01a1006c-f7ac-7231-99f0-3caebc6f1d7e`; raw SHA-256 `5b5bfcb964e3f8fc…`; superseded
  - attempt-03: edit; session `01a1008b-770d-7e33-a9f0-7a542b5dbee3`; raw SHA-256 `6190ce5352f14993…`; superseded
  - attempt-04: edit; session `01a1023e-8471-7823-891a-ee37e2391049`; raw SHA-256 `2ee8afb7862d762c…`; ACCEPTED
- Final review outcome: accepted attempt-04. A4Review: m08-evidence-lanes: ACCEPT_A4. The edit is confined to the callouts. '3 repeats per instruction' now has no connector. 'Same-case pairs' has its own leader from the dot on the row-1 horizontal join (x≈1040, y≈263) up to y≈216, right, and into the pill's top-left edge. The leader crosses the row-1 top horizontal join, which is also a same-case join, so the meaning holds. 'Within-instruction variation' still points at the vertical join. All 11 labels are verbatim, and the rest of the image matches A3 apart from re-encoding noise.

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to EDIT the first attached image and save exactly ONE corrected PNG with an OPAQUE #0D0906 background. Do not use a CLI image fallback or write code/SVG. Other attachments are STYLE references only. Return the absolute saved PNG path and no claim of verification.

CORRECTION (callout wiring only; preserve every other element, label, size and position):
- The `3 repeats per instruction` tag must have NO leader line to any join; it sits as a header above both column groups with no connector.
- The `Same-case pairs` pill gets its OWN single thin leader line from the pill's left edge to the dot on the row-1 HORIZONTAL join between the baseline group and the checked group. Remove the spur that currently ends before the pill and the link from that dot up to the `3 repeats per instruction` tag.
- Keep `Within-instruction variation` and its leader to the VERTICAL join exactly as is.

Reviewer finding being fixed:
Reconnect Same-case pairs callout; leader now hangs from 3 repeats tag
In m08-evidence-lanes A3, the row-1 middle horizontal join now carries the dot at x≈1040, y≈263 as requested. But its leader rises and joins the stub under the '3 repeats per instruction' tag (x≈1070, y≈205–214). A short spur runs right to x≈1203 and ends before the 'Same-case pairs' pill (x≈1265–1485, y≈232–283), which has no leader of its own. So the figure points 'Same-case pairs' at nothing and points '3 repeats per instruction' at a horizontal join. That reverses the focal teaching: repeats are the vertical joins, and same-case pairs are the horizontal ones. The label enlargement and the Within-instruction dot fix (x≈1170, y≈458 on the row-3 checked vertical join) are correct. A2 is not a fallback because its dot sat on a slot and its callouts were undersized.

Original contract (still governs):

## 1. Tool/output instruction

$imagegen Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

## 2. Lesson contract

- Owning module/page/H2: Module 08 — Slope Brief; page `AI_Harness_Bootcamp_2/module-08-change-eval/README.md`; H2 `## The hard gates` (replaces `shared/figures/m08-variation.svg`).
- Learning takeaway (caption, HTML text only): "Supplied-file checks do not measure model variation; repeated live pairs separate observed between-instruction disagreements from within-instruction variation."
- Learner action in unfamiliar work: keep a deterministic check of fixed outputs and a repeated live comparison as two separate evidence lanes; in the live lane, read same-case baseline/checked pairs across, and repeats of one instruction down, before claiming an instruction changed anything; apply the hard-gate rule in each lane without pooling.
- Misconception prevented: that re-running a deterministic file check measures model variation, or that results from the two lanes can be blended into one score; also that one better live answer shows an instruction effect.
- Preregistered live sequence the figure must stay consistent with (do not render as text): alternating order; model, source/form pair, prompt, and permissions fixed within each pair; 36 comparison calls plus two restored-baseline controls. These are planned observations, not accomplished results or proof of superiority.

## 3. Composition

- Category: contrast of two evidence lanes with a pairing/repeat grid (evidence linkage).
- Canvas: 1536×1024 landscape, 64 px safe margin. Title zone across the top. Below it, two side-by-side lanes separated by a clear vertical divider gap (no connector crosses it), and a full-width rule band at the bottom.
- Left lane (about 40% width), header `SUPPLIED FILES`: one panel `40 cases: baseline / A / B` showing three thin parallel columns of small neutral generic file slots (baseline, A, B) on the same rows, then a short downward gold trace into a neutral mechanism block `Deterministic checks`. The slots are empty/neutral; no pass/fail marks.
- Right lane (about 60% width), header `OPTIONAL LIVE COMPARISON` with a visibly optional treatment (dashed outer border). Inside: tag `6 cases` and tag `3 repeats per instruction`. Main element: a grid of six case rows; each row has two column groups (baseline instruction, checked instruction), each group with three empty neutral slots stacked vertically or in a short column (three repeats). Do not label rows or columns with extra words or numbers.
  - Horizontal gold joins link a baseline slot to its same-row checked slot; callout label `Same-case pairs` points to these horizontal joins.
  - Vertical thinner sandstone joins link the three slots within one instruction group; callout label `Within-instruction variation` points to these vertical joins.
  - Under the grid: label `Retain every attempt` attached to the whole grid by a bracket.
- Bottom band, full width: `One violation rejects`, with two separate short traces rising to each lane individually (one to the left lane, one to the right lane). The two lanes never merge into one pooled total; no arrow joins the lanes to each other.
- Reading order: title → left lane top to bottom → right lane header, tags, grid, joins → bottom rule band.
- Focal relationship: horizontal joins (between instructions, same case) are visually distinct from vertical joins (within one instruction); the two lanes stay separate.
- Arrows/joins mean only "same case compared" or "same instruction repeated"; the bottom traces mean "rule applies to"; never approval. No decorative connectors. Inline course image; no slide-overlay space.

## 4. Verbatim label map

Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts.

- Title zone: `SEPARATE CHANGE FROM VARIATION`
- Left lane header: `SUPPLIED FILES`
- Left lane panel: `40 cases: baseline / A / B`
- Left lane mechanism block: `Deterministic checks`
- Right lane header: `OPTIONAL LIVE COMPARISON`
- Right lane tag: `6 cases`
- Right lane tag: `3 repeats per instruction`
- Right lane callout on horizontal joins: `Same-case pairs`
- Right lane callout on vertical joins: `Within-instruction variation`
- Right lane bracket under grid: `Retain every attempt`
- Bottom band: `One violation rejects`

No other text: no case IDs, no counts beyond those in labels, no call totals, no Yes/No, no step numbers.

## 5. Visual family

`#0D0906` primary ground; `#17110C` panel fill; `#A58650` primary gold; `#C8A96A` sheen and connector highlights; `#C8B78A` secondary readable text; `#FFF8E7` primary text; `#655337` subdued nonessential rules; `#3A2E1B` faint structural lines; `#4F5634` restrained verified/allowed accents; `#B43A2F` warnings/blocked branches; `#2D3030` neutral mechanisms. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities. Here: all slots are neutral `#2D3030` (empty, no outcome color); horizontal same-case joins in gold `#C8A96A`; vertical within-instruction joins in sandstone `#C8B78A` thinner strokes; `One violation rejects` band uses a `#B43A2F` stroke or pill with off-white text.

## 6. Richness and legibility

Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use clean Inter/Helvetica-like sans-serif; exact filenames/tokens may use a clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density. Keep slots large enough that horizontal versus vertical joins are distinguishable at article width; prefer fewer, larger slots over tiny ones while keeping six rows × two groups × three repeats.

## 7. Honesty/exclusions

No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Module-specific: slots stay empty—no pass/fail marks, check marks, crosses, colors implying outcomes, or a winning instruction; no chart, axis, or average; no element pooling both lanes into one result; do not imply the live lane has been run or that it proves superiority; no provider or model logos.

## 8. Generation self-check

Must remain obvious: two separate lanes; in the live lane, horizontal joins = same-case pairs between instructions, vertical joins = repeats within one instruction; `One violation rejects` applies to each lane separately. Unusable if: any of the eleven labels is missing or altered; the live lane is not visibly optional; horizontal and vertical joins look identical or their callouts are swapped; slots show outcomes; a connector merges the two lanes; extra numbers, IDs, or words appear.
````

## m08-freeze-before-results

- Title: `FIX THE RULE BEFORE SEEING RESULTS`
- Publication path: `shared/figures/m08-freeze-before-results.png`
- Anchor: Lab `## Freeze your rule and input identities`.
- Caption: Freeze the rule, cases, and input identities before opening candidates; a manifest identifies supplied files, not a model execution.
- Native size: 1536×1024; published SHA-256: `6657aa71c84150e5f3890c4b1e0da1af11397e73080ec59254c4ef3902974077`
- Iteration history:
  - attempt-01: full generation; session `01a1005c-4b7f-7a93-99db-db7fbf52f1bd`; raw SHA-256 `9b2f0e1f64d10457…`; superseded — review: m08-freeze-before-results: enlarge the any_violation_rejects token
  - attempt-02: full generation; session `01a1006f-29b7-7080-bda9-38a6e265aae5`; raw SHA-256 `4b745e3f57e3d722…`; ACCEPTED
- Final review outcome: accepted attempt-02. F08: m08-freeze-before-results: ACCEPT_A2 — all 9 labels exact incl. `≠`; any_violation_rejects now about 32 px; four inputs feed one sealed Freeze; one forward arrow to the closed candidates; no back arrow. Matches the lab's Freeze section.

### Final prompt

````text
## 1. Tool/output instruction

$imagegen Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

## 2. Lesson contract

- Owning module/page/H2: Module 08 — Slope Brief; page `AI_Harness_Bootcamp_2/module-08-change-eval/shared/MODULE_08_LAB.md`; H2 `## Freeze your rule and input identities`.
- Learning takeaway (caption, HTML text only, not in image): "Freeze the rule, cases, and input identities before opening candidates; a manifest identifies supplied files, not a model execution."
- Learner action in unfamiliar work: before looking at any outcome of a proposed change, write down the rejection rule, the fixed case set, and content hashes of every input and configuration file in one record; only then open the candidate outputs.
- Misconception prevented: that the decision rule can be chosen or adjusted after seeing results, and that a batch manifest proves a model actually produced the briefs it names.

## 3. Composition

- Category: containment / sequence-gate diagram (constrained ordering).
- Canvas: 1536×1024 landscape, 64 px safe margin. Title zone across the top (about 120 px tall). Mechanism occupies the rest.
- Left zone (inputs, stacked vertically as three or four equal dark panels): `Rejection rule` panel containing the monospace token `any_violation_rejects`; `40 case IDs` panel; `Input + configuration hashes` panel; `Batch manifests` panel. Each panel shows one small generic glyph only to explain its content type (rule card, short list, fingerprint/hash strip, document stack).
- Center zone (focal): one heavy, sealed record block labeled `Freeze`. Thin gold traces run from each left-panel into this single block; each trace ends at the block edge. The block reads as closed/sealed (a gold seal edge or clasp), not a lock icon with extra text.
- Right zone: a closed container representing candidate contents, labeled `Then inspect candidates`. A single gold arrow runs from `Freeze` to this container. The container stays visibly closed on its left side up to that arrow, showing it opens only after the freeze record exists.
- Lower strip under the `Batch manifests` panel (or a small bracket attached to it): a distinct neutral note pill `Manifest ≠ model call`, attached by a short thin rule to the manifests panel only.
- Reading order: top title → left inputs top to bottom → center `Freeze` → right `Then inspect candidates` → manifest note.
- Focal relationship: everything enters `Freeze` before the candidates are opened. There is NO arrow from the candidates/results back to the rule or to `Freeze`; no loop, no feedback path.
- Arrows mean only "recorded into" (left→center) and "comes after" (center→right). They never mean approval. No decorative connectors.
- Inline course image: do not reserve slide-overlay space.

## 4. Verbatim label map

Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts.

- Title zone: `FIX THE RULE BEFORE SEEING RESULTS`
- Left zone, panel 1 heading: `Rejection rule`
- Left zone, panel 1 token (monospace): `any_violation_rejects`
- Left zone, panel 2: `40 case IDs`
- Left zone, panel 3: `Input + configuration hashes`
- Left zone, panel 4: `Batch manifests`
- Center block: `Freeze`
- Right container: `Then inspect candidates`
- Note pill attached to panel 4: `Manifest ≠ model call`

No other text. No case IDs listed, no hash strings, no filenames, no step numbers, no Yes/No.

## 5. Visual family

`#0D0906` primary ground; `#17110C` panel fill; `#A58650` primary gold; `#C8A96A` sheen and connector highlights; `#C8B78A` secondary readable text; `#FFF8E7` primary text; `#655337` subdued nonessential rules; `#3A2E1B` faint structural lines; `#4F5634` restrained verified/allowed accents; `#B43A2F` warnings/blocked branches; `#2D3030` neutral mechanisms. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities. Here: `Freeze` block uses a deep panel with a gold `#A58650` seal edge; the closed candidate container uses neutral `#2D3030`; the `Manifest ≠ model call` pill uses a neutral `#2D3030` fill with a thin `#655337` stroke (it is a caution about meaning, not a failure).

## 6. Richness and legibility

Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use clean Inter/Helvetica-like sans-serif; exact filenames/tokens (`any_violation_rejects`) may use a clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density.

## 7. Honesty/exclusions

No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Module-specific: do not show any candidate brief contents, pass/fail marks, result tables, or a winning candidate; do not show a model, robot, chip, or AI icon near the manifests (a manifest is not a model execution); no arrow or loop from results back to the rule; no readable hash values or case IDs.

## 8. Generation self-check

Must remain obvious: all four inputs (rule, 40 case IDs, hashes, manifests) feed one sealed `Freeze` record, and `Then inspect candidates` follows it in one direction only. Unusable if: any of the nine labels is missing or altered (especially `any_violation_rejects` and `Manifest ≠ model call`); the `≠` sign is replaced with `=` or a word; a back arrow from candidates to rule/freeze appears; the candidate container appears open before `Freeze`; any invented text, numbers, hashes, or check marks appear.

## 9. Revision requirements from review of the previous attempt
A previous generation of this figure was rejected. Generate a NEW image from this full contract and fix every defect below. All earlier blocks still govern; labels stay verbatim; add no words. Title text sits directly on the dark ground with no white bloom/haze band.

- m08-freeze-before-results: enlarge the any_violation_rejects token
Transcription: FIX THE RULE BEFORE SEEING RESULTS / Rejection rule / any_violation_rejects / 40 case IDs / Input + configuration hashes / Batch manifests / Freeze / Then inspect candidates / Manifest ≠ model call. All 9 labels are exact, with `≠` intact and no added text, hashes, or IDs. All four inputs feed one sealed `Freeze` block, and a single forward arrow goes to a closed candidate chest with no back arrow. That is consistent with the lab's Freeze section: the policy, `any_violation_rejects`, forty case IDs, manifests, and the sha256 record. Style and composition are good. One defect: the monospace `any_violation_rejects` token renders at about 22–24 px, below the 32 px minimum. At article width (~760 px) it shrinks to roughly 11 px and becomes unreadable, yet the prompt's self-check names it as essential. Verdict: LABEL_EDIT. Fix: in the `Rejection rule` panel, re-render `any_violation_rejects` in monospace at 32 px or larger in off-white #FFF8E7. If needed, shrink the rule-card glyph or move it right to make room. Change nothing else.
````

## m08-paired-hard-gates

- Title: `A SINGLE VIOLATION STILL COUNTS`
- Publication path: `shared/figures/m08-paired-hard-gates.png`
- Anchor: Lab `## Check the baseline, then evaluate every pair`.
- Caption: Compare each candidate against its own same-case baseline and check each material value and locator; an average cannot erase a failed gate.
- Native size: 1536×1024; published SHA-256: `60457468e1a35e771a8d8082f0592b9330cc1b0601689ce095f53d244f5ab3ec`
- Iteration history:
  - attempt-01: full generation; session `01a1005d-52c6-7521-898a-5d90a1ff687b`; raw SHA-256 `5533b038902f548b…`; superseded — review: m08-paired-hard-gates: give each cell its own exit; don't chain columns
  - attempt-02: full generation; session `01a1006e-0c3f-7df0-a6ac-d24ea8f01623`; raw SHA-256 `040c01d500dafc58…`; superseded
  - attempt-03: full generation; session `01a1008b-e34f-7011-b331-045b9e2c2c71`; raw SHA-256 `946c35bfc10bef0d…`; superseded
  - attempt-04: full generation; session `01a1023f-d12d-78d0-b80d-7294e8f02f8b`; raw SHA-256 `46c8c9ad660ce8f7…`; superseded
  - attempt-05: edit; session `01a10244-cd27-7843-abd4-7834f8df5033`; raw SHA-256 `0c3d89ff1b58ed18…`; ACCEPTED
- Final review outcome: accepted attempt-05. Orchestrator: labels verbatim (12); three separate source arrows; Baseline must pass enlarged on one line; eight independent candidate exits into reject bar; baseline cells have no exit (HOLD precedence preserved).

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to EDIT the first attached image and save exactly ONE corrected PNG with an OPAQUE #0D0906 background. Do not use a CLI image fallback or write code/SVG. Other attachments are STYLE references only. Return the absolute saved PNG path and no claim of verification.

CORRECTIONS (preserve every other element, label, trace and position exactly, especially the eight independent candidate exit traces into `Any one violation rejects` and the absence of any baseline exit):
1. Re-letter `Baseline must pass` on ONE line at the same type size as the `Format` and `Baseline` labels (at least 32 px), widening the olive pill to about 300 px; keep it centred in the gutter between the Baseline and Candidate A columns, between the column headers and the first row.
2. From `Same sources.json`, draw three SEPARATE gold arrows, one each to `Baseline`, `Candidate A`, `Candidate B`, with no shared segment, tee or junction. Remove the existing shared lines.
Add no words.

Original contract (still governs labels):

## 1. Tool/output instruction

$imagegen Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

## 2. Lesson contract

- Owning module/page/H2: Module 08 — Slope Brief; page `AI_Harness_Bootcamp_2/module-08-change-eval/shared/MODULE_08_LAB.md`; H2 `## Check the baseline, then evaluate every pair`.
- Learning takeaway (caption, HTML text only): "Compare each candidate against its own same-case baseline and check each material value and locator; an average cannot erase a failed gate."
- Learner action in unfamiliar work: feed the same source packet to the baseline and every candidate for a case, require the baseline to pass first, then check each material value against its own source locator as an independent hard gate; any single failure rejects, and every result is kept.
- Misconception prevented: that strong performance on most cells or cases averages out one failed required value, or that a zone label or source elsewhere in the brief repairs a missing one.

## 3. Composition

- Category: dependency / fan-out with independent gate cells (hard-gate matrix).
- Canvas: 1536×1024 landscape, 64 px safe margin. Title zone across the top. Mechanism below in two rows if needed for legibility.
- Left: one source packet block `Same sources.json` (generic document glyph, monospace filename). Three gold traces fan out from it to three brief columns: `Baseline`, `Candidate A`, `Candidate B`. The `Baseline` column carries a gate tag `Baseline must pass` placed before the candidate columns are evaluated (e.g., a gate bar on the baseline trace).
- Center: a grid where each brief column faces the same four independent gate cells (one column of cells per brief, rows aligned): row 1 `Format`; row 2 `Mass + #payload locator`; row 3 `UTC time + #gate locator`; row 4 `MDT time + #gate locator`. Render the row labels once at the left edge of the grid, aligned to the rows (do not repeat them per column). Cells are empty neutral squares with visible separation—no connector between cells within a column, and no summing bar or average under any column. In rows 2–4, each cell is drawn as a value slot visibly paired with its own small locator slot (two halves of one cell), showing each value is checked against its own locator.
- Right: a single exit bar `Any one violation rejects`; each individual gate cell has its own thin trace that could reach this bar (one cell is enough). Do not draw any total, mean, or score aggregate.
- Bottom: a full-width retention strip `Keep every result` under all three columns.
- Reading order: title → `Same sources.json` → three briefs → `Baseline must pass` → gate rows → `Any one violation rejects` → `Keep every result`.
- Focal relationship: one same-case source feeds all three briefs; each gate cell exits independently to rejection; nothing averages cells.
- Arrows mean only "same input supplied to" and "a failed cell routes to"; never approval. No decorative connectors. Inline course image; no slide-overlay space.

## 4. Verbatim label map

Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts.

- Title zone: `A SINGLE VIOLATION STILL COUNTS`
- Source block (monospace filename allowed): `Same sources.json`
- Brief column headers: `Baseline`; `Candidate A`; `Candidate B`
- Gate tag on baseline column/trace: `Baseline must pass`
- Gate row labels (once each, left edge of grid): `Format`; `Mass + #payload locator`; `UTC time + #gate locator`; `MDT time + #gate locator`
- Exit bar: `Any one violation rejects`
- Bottom strip: `Keep every result`

No other text: no mass values, no clock times, no zone words besides those in labels, no case IDs, no Yes/No, no step numbers.

## 5. Visual family

`#0D0906` primary ground; `#17110C` panel fill; `#A58650` primary gold; `#C8A96A` sheen and connector highlights; `#C8B78A` secondary readable text; `#FFF8E7` primary text; `#655337` subdued nonessential rules; `#3A2E1B` faint structural lines; `#4F5634` restrained verified/allowed accents; `#B43A2F` warnings/blocked branches; `#2D3030` neutral mechanisms. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities. Here: gate cells are neutral `#2D3030` (no outcome); fan-out traces gold; `Baseline must pass` tag with an olive `#4F5634` stroke; `Any one violation rejects` exit bar with a `#B43A2F` fill/stroke and off-white text; `Keep every result` strip in neutral panel fill with gold edge.

## 6. Richness and legibility

Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use clean Inter/Helvetica-like sans-serif; exact filenames/tokens (`sources.json`, `#payload`, `#gate`) may use a clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density.

## 7. Honesty/exclusions

No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Module-specific: do not show any candidate failing or passing, any filled cell, check mark, cross, real or invented mass or time value, average, total, percentage, or a preferred candidate; do not show different source packets per brief.

## 8. Generation self-check

Must remain obvious: one `Same sources.json` feeds `Baseline`, `Candidate A`, `Candidate B`; each of the four gate rows is checked separately per brief, rows 2–4 pairing a value with its own locator; any single cell can exit to `Any one violation rejects`; no averaging. Unusable if: any of the eleven labels is missing or altered (especially `#payload` and `#gate`); row labels are repeated per column or missing; an aggregate/average element appears; cells show outcomes; UTC and MDT are merged into one row; the baseline gate is absent.
````

## m08-restore-baseline

- Title: `RESTORE IDENTITY, THEN REPEAT`
- Publication path: `shared/figures/m08-restore-baseline.png`
- Anchor: Lab `## Demonstrate restoration`.
- Caption: Restore the hash-identified baseline, retain candidate attempts, and prove the rerun matches the original result bytes.
- Native size: 1536×1024; published SHA-256: `98eafcb6f5240242ae28d47884f58c2dd4a4837760b99cb657ca25877e463aa3`
- Iteration history:
  - attempt-01: full generation; session `01a1005e-45a0-7162-9681-2bfb2fe51841`; raw SHA-256 `00ae1729044ae522…`; superseded — review: m08-restore-baseline: remove title bloom and dangling stub below HOLD
  - attempt-02: full generation; session `01a1006e-0f66-7e10-9fb3-f278cc7d9064`; raw SHA-256 `2e9d5ff335a6e996…`; superseded
  - attempt-03: edit; session `01a1008c-7b52-78d1-b78b-bb8e25180817`; raw SHA-256 `8df7a47775827f42…`; ACCEPTED
- Final review outcome: accepted attempt-03. Final2: m08-restore-baseline: ACCEPT_A3 (8 labels verbatim, with → intact; Compare original and restored bytes, Match required and Retain candidate attempts are enlarged; the flow matches MODULE_08_LAB Demonstrate restoration, nothing else changed, and there is no success badge)

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to EDIT the first attached image and save exactly ONE corrected PNG with an OPAQUE #0D0906 background (no transparency). Do not use a CLI image fallback or write code/SVG. The other attachments are STYLE references only. Return the absolute saved PNG path and no claim of verification.

CORRECTIONS (apply exactly; preserve every other relationship, label, position and color):
m08-restore-baseline: LABEL_EDIT_A2 — enlarge comparison and condition-tag labels
A2 structure matches the lab's Demonstrate restoration flow. A hash dot-grid `Stored hashes` feeds frozen copies into `Restore baseline control + briefs`, which leads to `Rerun evaluation`, then to `Compare original and restored bytes` (two file glyphs and a neutral `=` operator, no badge). The forward edge carries `Match required` to a plain terminal dot, and a red downward branch goes to the terminal `Mismatch → HOLD`. The dangling stub below HOLD is gone. `Retain candidate attempts` is a side shelf joined by a plain unarrowed rule. The 8 labels are exact, with `→` intact, no step numbers and no readouts. Measured on flattened.png, the remaining defect is size: `Compare original and restored bytes` is about 28 px. The prior review required ≥32 px for this label, and it was not fixed. `Match required`, the decisive condition tag, is about 24 px (about 12 px at 800 px article width). `Retain candidate attempts` is about 27 px. Edit of A2: re-render `Compare original and restored bytes` at ≥32 px in the same two-line layout inside the compare block. Widen the `Match required` pill and re-render its text at ≥32 px, keeping the arrow into it and the arrow on to the plain terminal dot. Re-render `Retain candidate attempts` at ≥32 px in its box header. Change nothing else.

The original full generation contract follows and still governs labels and composition:

## 1. Tool/output instruction

$imagegen Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

## 2. Lesson contract

- Owning module/page/H2: Module 08 — Slope Brief; page `AI_Harness_Bootcamp_2/module-08-change-eval/shared/MODULE_08_LAB.md`; H2 `## Demonstrate restoration`.
- Learning takeaway (caption, HTML text only): "Restore the hash-identified baseline, retain candidate attempts, and prove the rerun matches the original result bytes."
- Learner action in unfamiliar work: after changing a control, restore the baseline only from frozen copies whose stored hashes match, keep the candidate attempts untouched, rerun the same evaluation, and byte-compare the new result with the original; any difference holds the work.
- Misconception prevented: that a restore succeeded because the command ran, that a baseline may be reconstructed from memory, or that restoring means deleting the candidate attempts.

## 3. Composition

- Category: genuine conditional flow (sequence with a gate and one comparison branch).
- Canvas: 1536×1024 landscape, 64 px safe margin. Title zone across the top. Main flow left to right across the upper/middle band; a side retention branch below.
- Step 1 (left): `Stored hashes` — a fingerprint/hash strip glyph block acting as a gate.
- Step 2: gold trace from `Stored hashes` into `Restore baseline control + briefs` (generic frozen-copy document glyphs entering the block, showing restoration from frozen copies gated by the hashes).
- Parallel lower branch, starting beside step 2 and NOT on the restore path: `Retain candidate attempts` — a separate shelf/container that stays intact, linked only by a thin neutral rule showing it is preserved, not overwritten.
- Step 3: gold trace to `Rerun evaluation`.
- Step 4: gold trace to `Compare original and restored bytes` — two side-by-side generic result-file glyphs (original, restored) feeding one comparison block.
- Exit from the comparison: a pass-through condition tag `Match required` on the forward edge (the forward edge ends at the frame edge or a plain terminal node without any success badge, check mark, or extra text), and a separate downward branch to a red-stroked terminal `Mismatch → HOLD`.
- Reading order: title → `Stored hashes` → restore → rerun → compare → `Match required` / `Mismatch → HOLD`, with `Retain candidate attempts` read as a side branch.
- Focal relationship: the byte comparison decides; nothing shows success before it.
- Arrows mean only "next step" or "on mismatch"; never approval. No decorative connectors. Inline course image; no slide-overlay space.

## 4. Verbatim label map

Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts.

- Title zone: `RESTORE IDENTITY, THEN REPEAT`
- Step 1 block: `Stored hashes`
- Step 2 block: `Restore baseline control + briefs`
- Side branch container: `Retain candidate attempts`
- Step 3 block: `Rerun evaluation`
- Step 4 block: `Compare original and restored bytes`
- Forward-edge condition tag: `Match required`
- Mismatch terminal: `Mismatch → HOLD`

No other text: no filenames, hash strings, `RESTORE OK`/`MATCH` readouts, counts, Yes/No, or step numbers (do not number the steps).

## 5. Visual family

`#0D0906` primary ground; `#17110C` panel fill; `#A58650` primary gold; `#C8A96A` sheen and connector highlights; `#C8B78A` secondary readable text; `#FFF8E7` primary text; `#655337` subdued nonessential rules; `#3A2E1B` faint structural lines; `#4F5634` restrained verified/allowed accents; `#B43A2F` warnings/blocked branches; `#2D3030` neutral mechanisms. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities. Here: flow blocks neutral `#2D3030` with gold traces; `Stored hashes` with gold `#A58650` edge; `Retain candidate attempts` in panel fill with `#655337` stroke; `Match required` pill with olive `#4F5634` stroke (a requirement, not a success badge); `Mismatch → HOLD` with `#B43A2F` fill/stroke and off-white text.

## 6. Richness and legibility

Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use clean Inter/Helvetica-like sans-serif; exact filenames/tokens may use a clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density. If five blocks in one row get cramped, use two rows (hashes → restore → rerun on top; compare and its two exits below) rather than shrinking type.

## 7. Honesty/exclusions

No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Module-specific: no success badge, check mark, trophy, or green light anywhere before or after the comparison; no trash can, deletion, or overwriting of candidate attempts; no undo/rewind icon suggesting reconstruction from memory; no readable hash values or result contents.

## 8. Generation self-check

Must remain obvious: `Stored hashes` gate the restore; candidate attempts are retained on a side branch; the rerun result is byte-compared with the original; `Match required` on the forward edge and `Mismatch → HOLD` as the other exit. Unusable if: any of the eight labels is missing or altered (especially the `→` in `Mismatch → HOLD`); a success badge appears; the candidate attempts are shown deleted or inside the restore path; the comparison has only one exit; extra text, numbers, or step numbers appear.
````

