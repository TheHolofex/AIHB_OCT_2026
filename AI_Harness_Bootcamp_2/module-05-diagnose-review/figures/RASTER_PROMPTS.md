# Raster figure prompts and provenance — module-05-diagnose-review

Staff-only record. Not published (absent from `course.json`).

- Generator: `codex-cli 0.154.0` (`codex exec`, ChatGPT login, built-in `image_gen`).
- Style references attached to every invocation: `ui/images/home-hero.webp` and `ui/images/home-band-custody.webp`, decoded losslessly to PNG with `dwebp`; every figure except `m00-bounded-direction` also received the accepted `m00-bounded-direction` attempt-01 raster as a style-only reference. Label edits additionally attached the image being edited as the first input.
- Post-processing: the generator returns RGBA with a transparent ground. Each accepted raster was alpha-composited onto the specified `#0D0906` ground and saved as opaque lossless RGB PNG at native size. No other pixel changes, no resizing.
- Run evidence (all attempts, logs, rejected rasters, reviews): `~/course-evidence/course-raster-visuals/20261002T233502`
- Module source contract: `module-05-diagnose-review/shared/MODULE_05_LAB.md` steps 2–5, `scripts/probe_fields.py::classify_field`, and the restore description. Insert into the published lab, not `modules/core/`. Competing-input cases remain optional stretch.
- Owning page digests at integration (SHA-256): `shared/MODULE_05_LAB.md` 6538d947d8719eb5…

## m05-authorized-correction

- Title: `CORRECT THE ISOLATED CAUSE`
- Publication path: `shared/figures/m05-authorized-correction.png`
- Anchor: Lab `## 4. One authorized replace`.
- Caption: Replace the renderer only when the evidence isolates it; preserve the failed attempt instead of patching the card or relaxing acceptance.
- Native size: 1536×1024; published SHA-256: `32c2c033d7e793b1da212362803d54f197e89dab063fb86e4f3fe3ba8bcad721`
- Iteration history:
  - attempt-01: full generation; session `01a10056-92d9-73d0-934e-e19b0e3e9566`; raw SHA-256 `611e9c17693df85d…`; superseded — review: m05-authorized-correction: HOLD branch leaves the renderer-isolated box; fake window glyph (REGENERATE)
  - attempt-02: full generation; session `01a10067-e8a4-7ca0-bdf6-cfb186265638`; raw SHA-256 `c89f05f25fa64455…`; superseded
  - attempt-03: edit; session `01a10087-4eee-71b1-9f71-c638d85e9362`; raw SHA-256 `ec27f41853660176…`; ACCEPTED
- Final review outcome: accepted attempt-03. Final1: m05-authorized-correction: ACCEPT_A3 — 'Renderer is the failing boundary' is now off-white in two lines with a 22 px cap height, matching 'Sealed diagnosis' (23 px). The HOLD branch still leaves Sealed diagnosis and ends in a stop bar. The preserve branch splits off before the single restore arrow, both bottom tiles remain crossed dead ends, and all nine strings are verbatim.

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to EDIT the first attached image and save exactly ONE corrected PNG with an OPAQUE #0D0906 background (no transparency). Do not use a CLI image fallback or write code/SVG. The other attachments are STYLE references only. Return the absolute saved PNG path and no claim of verification.

CORRECTIONS (apply exactly; preserve every other relationship, label, position and color):
m05-authorized-correction: LABEL_EDIT_A2 — restore legibility of decisive condition label
A2 is structurally correct, and better than A1. All nine strings are exact and appear once: CORRECT THE ISOLATED CAUSE; Sealed diagnosis; Renderer is the failing boundary; Authorized replacement; Preserve failed attempt; Restore clean renderer; Other cause → HOLD; No output hand-patch; Do not weaken requirements. The HOLD branch now leaves the Sealed diagnosis panel instead of the renderer sub-panel, and it ends in a stop bar. Preserve failed attempt sits on its own branch, split off before the single restore arrow. Both bottom tiles are crossed dead ends with no outgoing path. This matches lab §4: preserve first, replace once, never hand-edit or relax requirements. One essential label fails the legibility contract. The sub-panel text 'Renderer is the failing boundary', at about x 280–560, y 405–485, is the only label rendered in dim tan (≈#C8A070). It is about 23 px tall at 1536 px, roughly 12 px at an 800 px article width, which is below the 32 px essential-copy minimum. It is also visibly smaller and dimmer than its neighbours, yet it is the condition that authorizes the replacement. The prompt explicitly says 'Never dim essential words into low-contrast tan.' Image-edit instruction for A2: inside the lower sub-panel of the Sealed diagnosis card, re-render the text 'Renderer is the failing boundary' in #FFF8E7. Use the same weight as 'Sealed diagnosis' and a cap height at least equal to it. Two lines are allowed ('Renderer is the' / 'failing boundary'). Keep the panel, connectors and all other content unchanged. Reject A1: it starts the HOLD connector from the renderer sub-panel, which says 'renderer is failing → HOLD'. It also adds a decorative gear and a faux app-window glyph, which the exclusions forbid as fake UI.

The original full generation contract follows and still governs labels and composition:

## 1. Tool/output instruction

$imagegen Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

## 2. Lesson contract

- Owning module/page/H2: Module 05 — Copper Span; published lab `module-05-diagnose-review/shared/MODULE_05_LAB.md`; H2 `## 4. One authorized replace`.
- Learning takeaway (caption, HTML text only, not in image): "Replace the renderer only when the evidence isolates it; preserve the failed attempt instead of patching the card or relaxing acceptance."
- Intended learner action in unfamiliar work: make exactly one correction, and only after the sealed diagnosis isolates the failing component and the correction is authorized. Keep the failed component and its output as evidence. If the evidence points elsewhere, hold instead of replacing.
- Misconception prevented: "Any change that makes the output look right is a fix." Hand-editing the output or removing a required field from the acceptance requirements hides the failure instead of correcting its cause. Neither is an alternative successful path. Replacing the renderer when the cause lies elsewhere (for example, the source) cannot recover the value.

## 3. Composition

- Category: constrained selection / authorization gate with one permitted path, one preservation branch, one HOLD branch, and two crossed-out boundary dead ends.
- Canvas: 1536×1024 landscape, 64 px safe margin. Title zone across the top (about 120 px). These are inline course images, so do not reserve slide-overlay space.
- Left column (inputs), stacked vertically:
  - `Sealed diagnosis`, a panel with a generic sealed-document glyph (a document with a seal stamp, no characters).
  - Directly under it and joined to it, a sub-panel or attached tag: `Renderer is the failing boundary`.
  - From the diagnosis panel, a brick-red connector branches DOWN-LEFT to a brick-red outlined terminal pill `Other cause → HOLD`. It ends with a hard stop bar and no onward connection. This is the branch for when the diagnosis does not isolate the renderer.
- Center: a single gate node `Authorized replacement`, a sharp-cornered gate panel with a gold outline. The gold trace from `Renderer is the failing boundary` enters this gate. It is the only path into it.
- From the gate, the gold path goes right in two ordered steps:
  1. `Preserve failed attempt`: a panel with document and stacked-files glyphs going into a retained tray. It sits on a separate branch that splits off the main path just before the restore step, showing that the failed renderer and output are kept, not discarded.
  2. `Restore clean renderer`: the single outcome panel at the right of the main path, with a gold outline and an olive (#4F5634) accent strip. One replacement only, so draw a single arrow and no loop.
- Bottom band, visually separated by a thin #3A2E1B rule: two dead-end tiles, each struck through with a brick-red diagonal or X, with a crossed boundary-line motif. Neither has any arrow leading from it to success, and neither connects to `Restore clean renderer`:
  - `No output hand-patch`
  - `Do not weaken requirements`
- Focal relationship: sealed diagnosis isolating the renderer → authorization → one clean replacement, with the failed attempt preserved alongside.
- Arrows mean only "permits / proceeds to". They never mean approval of a result. No decorative connectors.

## 4. Verbatim label map

Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts.

- Title zone: `CORRECT THE ISOLATED CAUSE`
- Left column: `Sealed diagnosis`; `Renderer is the failing boundary`
- HOLD branch terminal: `Other cause → HOLD`
- Center gate: `Authorized replacement`
- Preservation branch: `Preserve failed attempt`
- Outcome: `Restore clean renderer`
- Bottom crossed-out tiles: `No output hand-patch`; `Do not weaken requirements`

No other words. No Yes/No edge labels, because no node ends in `?`. No step numbers.

## 5. Visual family

`#0D0906` primary ground; `#17110C` panel fill; `#A58650` primary gold; `#C8A96A` sheen and connector highlights; `#C8B78A` secondary readable text; `#FFF8E7` primary text; `#655337` subdued nonessential rules; `#3A2E1B` faint structural lines; `#4F5634` restrained verified/allowed accents; `#B43A2F` warnings/blocked branches; `#2D3030` neutral mechanisms. Olive and brick red are fills, strokes, or pills only. Text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities. Brick red marks `Other cause → HOLD` and the strike-throughs on the two bottom tiles. The tile text itself stays #FFF8E7 and fully readable under the strike.

## 6. Richness and legibility

Subtle warm panel gradients, thin gold sheen, precise gold traces, and restrained emission dots only on meaningful connections (diagnosis → gate → preserve → restore). Modest inner/elevation shadows, sharp corners, and faint survey-grid texture away from text. Warm, restrained operational luminance: not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use a clean Inter/Helvetica-like sans-serif. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Strike-through marks must not cover letters so heavily that the words become illegible. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density.

## 7. Honesty/exclusions

No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Specific prohibitions for this figure: no approval stamps, checkmark badges, or signatures implying sign-off of the result. Do not draw a second replacement, a retry loop, or multiple restore arrows. Do not show the hand-patch or weakened-requirements tiles leading anywhere. Do not name which practice fault variant was placed or which field it removed. Do not show `permit_status` as permission to act.

## 8. Generation self-check instruction

The following must stay obvious: only `Sealed diagnosis` + `Renderer is the failing boundary` lead into `Authorized replacement`; the gate leads to exactly one `Restore clean renderer`; `Preserve failed attempt` is kept on its own branch; `Other cause → HOLD` stops; `No output hand-patch` and `Do not weaken requirements` are crossed-out dead ends with no path to success. The result is unusable if any of the eight labels is missing, altered, or duplicated, if either dead end connects to the restore, if the HOLD branch continues onward, if extra words or numbers appear, or if the title differs from `CORRECT THE ISOLATED CAUSE`. This self-check does not replace post-generation inspection.
````

## m05-first-divergence

- Title: `TRACE THE FIRST DIVERGENCE`
- Publication path: `shared/figures/m05-first-divergence.png`
- Anchor: Lab `## 3. Seal the first miss`, after the paragraph introducing the read-only probe and before its command.
- Caption: Compare the selected source and rendered card, preserve the first mismatch, and read the probe's classifications before replacing anything.
- Native size: 1536×1024; published SHA-256: `6b1e3852fb18a5371015c49bb678ea753cce4bbba8605ec40327f0b936c696fa`
- Iteration history:
  - attempt-01: full generation; session `01a10057-98c8-7ab0-afad-8dc380444736`; raw SHA-256 `0e1a66a1349700cf…`; superseded — review: m05-first-divergence: remove title haze and enlarge Yes/No edge words (REGENERATE)
  - attempt-02: full generation; session `01a10067-e8a4-7930-84b4-42ccb772e04c`; raw SHA-256 `74b75afc019caf08…`; ACCEPTED
- Final review outcome: accepted attempt-02. F0405: m05-first-divergence: ACCEPT_A2 — all 13 strings are exact. The Yes/No labels appear only on the four `?` nodes, and each node has both destinations. The cascade and side exits match the probe classes in lab §3. The evidence strip (Expected / observed / command; Seal before changing; Probe exit 0 ≠ complete card) has no prefilled result. Labels are larger and more legible than in A1.

### Final prompt

````text
## 1. Tool/output instruction

$imagegen Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

## 2. Lesson contract

- Owning module/page/H2: Module 05 — Copper Span; published lab `module-05-diagnose-review/shared/MODULE_05_LAB.md`; H2 `## 3. Seal the first miss`. The figure sits after the paragraph introducing the read-only probe and before its command.
- Learning takeaway (caption, HTML text only, not in image): "Compare the selected source and rendered card, preserve the first mismatch, and read the probe's classifications before replacing anything."
- Intended learner action in unfamiliar work: when a required value is missing from an output, check each boundary in order from the source outward and stop at the first one that fails. First: does the selected source supply the value? Is it consistent across rows? Does an output exist? Is the value actually rendered? Write down the expected result, the observed result, and the exact command, and seal that record before changing anything. Read the per-field classification lines, not just the probe's exit status.
- Misconception prevented: "The probe exited 0, so the card is complete," or "the field is missing, so the renderer must be broken." The probe's exit code only says the diagnosis completed. A missing value may come from the source (omission or conflict) or from a missing output, and replacing the renderer cannot recover a value the source never supplied.

## 3. Composition

- Category: four-row conditional cascade (decision tree) with side exits, plus a separate evidence strip.
- Canvas: 1536×1024 landscape, 64 px safe margin. Title zone across the top (about 120 px). These are inline course images, so do not reserve slide-overlay space.
- Left about 68% of the mechanism area holds the cascade, which reads top to bottom:
  - Entry node at the top: `Selected source rows`, a panel with a generic small table glyph (three blank rows, no characters). A gold arrow goes down to Row 1.
  - Row 1 decision node: `Source values present?`. Its `No` edge goes RIGHT to the side-exit terminal `source_omission`. Its `Yes` edge goes DOWN to Row 2.
  - Row 2 decision node: `Consistent values?`. `No` goes RIGHT to the side-exit terminal `source_conflict`. `Yes` goes DOWN to Row 3.
  - Row 3 decision node: `Card exists?`. `No` goes RIGHT to the side-exit terminal `output_absent`. `Yes` goes DOWN to Row 4.
  - Row 4 decision node: `Field rendered?`. This row has two terminal outcomes side by side: `Yes` goes to the terminal `rendered` and `No` goes to the terminal `renderer_omission`. Place `rendered` directly below or right of the node and `renderer_omission` on the other side, each with its own clearly attached edge label.
  - Decision nodes are sharp-cornered diamonds or chamfered decision panels stacked in one vertical column with equal spacing. Side-exit terminals align in a column to their right. All terminals are neutral classification pills (#2D3030 fill, gold outline, monospace text). Mark none of them as "the answer" or highlight any one as the actual result. No terminal is prefilled or checked.
- Right about 32% of the mechanism area holds a separate vertical evidence strip, a framed panel set apart by a thin #3A2E1B rule. From top to bottom:
  - `Expected / observed / command`, a panel with a generic document glyph of three blank lines.
  - Below it, a seal motif (a sharp-cornered wax-seal-like stamp or a closed bracket, no characters) with the label `Seal before changing`.
  - At the bottom of the strip, a brick-red outlined warning pill: `Probe exit 0 ≠ complete card`.
  - A single thin gold trace from the cascade's terminal column into the evidence strip shows that the cascade's classification feeds the sealed record. It is one connector, not one per terminal.
- Focal relationship: the ordered cascade. Each later boundary is checked only after every earlier boundary passes, so the first failing boundary is where the cascade exits.
- Arrows mean only "if this answer, go to". They never mean approval. No decorative connectors.

## 4. Verbatim label map

Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts.

- Title zone: `TRACE THE FIRST DIVERGENCE`
- Cascade entry: `Selected source rows`
- Row 1 decision: `Source values present?`, with side exit `source_omission`
- Row 2 decision: `Consistent values?`, with side exit `source_conflict`
- Row 3 decision: `Card exists?`, with side exit `output_absent`
- Row 4 decision: `Field rendered?`, with outcomes `rendered` and `renderer_omission`
- Evidence strip: `Expected / observed / command`; `Seal before changing`; `Probe exit 0 ≠ complete card`
- Edge words: `Yes` and `No` are the only additional words, used solely on edges leaving the four questions ending in `?`. Each question has exactly one `Yes` edge and one `No` edge, both with explicit destinations: `Source values present?` No→`source_omission`, Yes→`Consistent values?`; `Consistent values?` No→`source_conflict`, Yes→`Card exists?`; `Card exists?` No→`output_absent`, Yes→`Field rendered?`; `Field rendered?` Yes→`rendered`, No→`renderer_omission`.
- Render the classification tokens (`source_omission`, `source_conflict`, `output_absent`, `rendered`, `renderer_omission`) in a clean monospace exactly as written, lowercase, with underscores. No step numbers.

## 5. Visual family

`#0D0906` primary ground; `#17110C` panel fill; `#A58650` primary gold; `#C8A96A` sheen and connector highlights; `#C8B78A` secondary readable text; `#FFF8E7` primary text; `#655337` subdued nonessential rules; `#3A2E1B` faint structural lines; `#4F5634` restrained verified/allowed accents; `#B43A2F` warnings/blocked branches; `#2D3030` neutral mechanisms. Olive and brick red are fills, strokes, or pills only. Text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities. Here the classification terminals are neutral (#2D3030 with gold outline), not color-coded as pass or fail. Brick red is used only for the `Probe exit 0 ≠ complete card` warning pill.

## 6. Richness and legibility

Subtle warm panel gradients, thin gold sheen, precise gold traces, and restrained emission dots only on meaningful connections (the cascade edges and the single trace into the evidence strip). Modest inner/elevation shadows, sharp corners, and faint survey-grid texture away from text. Warm, restrained operational luminance: not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use a clean Inter/Helvetica-like sans-serif, with monospace for the classification tokens. Title about 60 px; major labels at least 38 px; all essential copy, including `Yes`/`No` edge words and the monospace tokens, at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density.

## 7. Honesty/exclusions

No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Specific prohibitions for this figure: do not prefill, highlight, check, or circle any classification as the actual result. Do not show which field name (`permit_status`, `gate_time_mdt`) gets which classification; neither field name appears in this figure. Do not show the practice fault variant, row IDs, source IDs, or probe output lines. Do not depict a `wrong_input_version` outcome or any intended-input comparison; it is not part of this ordinary probe. Do not imply the probe detects wrong-input versions. Do not imply a zero exit means a complete card.

## 8. Generation self-check instruction

The following must stay obvious: the four questions are checked in fixed order, top to bottom (`Source values present?` → `Consistent values?` → `Card exists?` → `Field rendered?`); each `No` on the first three exits sideways to its own classification; only the last question splits into `rendered` vs `renderer_omission`; the evidence strip is separate, and sealing precedes changing. The result is unusable if any question, any of the five classification tokens, or any `Yes`/`No` edge is missing, duplicated, misattached, or reordered. It is also unusable if `Probe exit 0 ≠ complete card` or `Seal before changing` is missing, if any classification is shown as the selected result, or if any extra words or numbers appear. The title must read `TRACE THE FIRST DIVERGENCE`. This self-check does not replace post-generation inspection.

## 9. Revision requirements from review of the previous attempt
A previous generation of this figure was rejected. Generate a NEW image from this full contract and fix every defect below. All earlier blocks still govern; labels stay verbatim; add no words.

Transcription: "TRACE THE FIRST DIVERGENCE"; "Selected source rows"; "Source values present?"; "Consistent values?"; "Card exists?"; "Field rendered?"; "source_omission"; "source_conflict"; "output_absent"; "renderer_omission"; "rendered"; Yes×4; No×4; "Expected / observed / command"; "Seal before changing"; "Probe exit 0 ≠ complete card". All strings, the ≠ sign and the monospace tokens are exact, with no added words. Edge routing matches probe_fields.py lines 104-112: each of the first three No edges exits right to its token, and Field rendered? goes Yes→rendered (down) and No→renderer_omission (right). Defects: (1) The title sits in a blown-out off-white glow at the very top edge, with no 64 px margin. Its off-white letters on a near-white halo are hard to read, and the glow is the cinematic haze the brief prohibits. (2) All eight Yes/No edge words are small (about 22 px) and in dim tan, far below the 32 px minimum for essential copy. At article width they shrink to roughly 11 px. (3) The connector to the evidence strip is a four-stub bracket that joins source_omission through renderer_omission but leaves out rendered. That reads as if only failure classes feed the sealed record, although the lab's sealed record carries every probe classification line, including rendered. (4) A broad radial haze glows behind the cascade. Fix: regenerate with the same layout. Put the title in a solid dark title band 64 px below the top edge, with no glow behind it. Render Yes/No at 32 px or more in #FFF8E7 or #C8B78A. Draw one trace from the whole terminal column, including rendered, into the evidence strip. Remove the center radial glow.
````

## m05-recovery-proofs

- Title: `DIAGNOSIS IS NOT RECOVERY`
- Publication path: `shared/figures/m05-recovery-proofs.png`
- Anchor: Lab `## 5. Prove recovery three ways`.
- Caption: Prove the focused repair, the complete result, and fresh-process recovery without dropping either required field.
- Native size: 1536×1024; published SHA-256: `1a1863089e9b3180506042e2b092c7960058caed9bd95e0c2579a3520e7e9e9f`
- Iteration history:
  - attempt-01: full generation; session `01a10058-a49d-72b3-b27c-4ce4925679e3`; raw SHA-256 `54ee255d1082149a…`; superseded — review: m05-recovery-proofs: field bands skip lane 1; title washed out (REGENERATE)
  - attempt-02: full generation; session `01a10068-e8e4-75e2-8314-25af90b26031`; raw SHA-256 `52ec9a12bf921547…`; ACCEPTED
- Final review outcome: accepted attempt-02. F0405: m05-recovery-proofs: ACCEPT_A2 — all ten strings are exact. Three distinct lanes converge on Same acceptance requirements. permit_status and gate_time_mdt cross all three lanes with junction dots, matching lab §5. In A1 the probe lane has no field junctions, and there is a decorative location pin.

### Final prompt

````text
## 1. Tool/output instruction

$imagegen Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

## 2. Lesson contract

- Owning module/page/H2: Module 05 — Copper Span; published lab `module-05-diagnose-review/shared/MODULE_05_LAB.md`; H2 `## 5. Prove recovery three ways`.
- Learning takeaway (caption, HTML text only, not in image): "Prove the focused repair, the complete result, and fresh-process recovery without dropping either required field."
- Intended learner action in unfamiliar work: after a correction, prove recovery in three independent ways that answer different questions. First, a focused check that the previously missing field is now present. Second, a complete end-to-end result from an explicit input. Third, a fresh-process run in a fresh folder started from an unrelated working directory. Keep every required field in every check, and judge all three against the same, unchanged acceptance requirements.
- Misconception prevented: "I found and fixed the cause, so it's recovered," or "the focused check passed, so we're done." Diagnosis is not recovery. A single check can pass while the full result or a clean environment still fails, and dropping a required field from any check is not acceptance.

## 3. Composition

- Category: evidence linkage. Three parallel proof lanes converge on one unchanged acceptance bar, with two required-field bands spanning all lanes.
- Canvas: 1536×1024 landscape, 64 px safe margin. Title zone across the top (about 120 px). These are inline course images, so do not reserve slide-overlay space.
- Three vertical lanes of equal width, side by side across the middle of the mechanism area, separated by thin #3A2E1B rules. Each lane has a header panel at the top:
  - Lane 1 header: `Focused field probe`. Inside the lane, a generic magnifier-over-document glyph with no characters.
  - Lane 2 header: `Complete render`. Inside the lane, a sub-tag `Explicit ledger` attached to a generic table glyph whose gold trace feeds a full generic document glyph. This shows that the complete card comes from the explicitly named ledger.
  - Lane 3 header: `Fresh-process run`. Inside the lane, two stacked sub-tags: `Fresh folder` (a new, empty folder glyph) and `Unrelated working directory` (a separate folder glyph with a starting-point marker, set apart from the fresh folder).
- Two horizontal bands cross ALL THREE lanes, like rails threading through each lane. Each band is labeled once at its left end, in monospace:
  - Band A: `permit_status`
  - Band B: `gate_time_mdt`
  Where each band crosses each lane, place a small gold node (a junction dot, with no check mark and no text) showing that the field is part of that lane's check. Neither band may stop short of lane 3.
- Bottom: the three lanes each send one gold trace downward to converge on a single wide horizontal bar spanning the lanes: `Same acceptance requirements`. Draw it as a fixed bar with a gold outline and a subtle olive (#4F5634) accent edge. All three traces meet the same bar.
- Focal relationship: three distinct proofs, both required fields threaded through every proof, all judged by one unchanged acceptance bar.
- Arrows/traces mean only "is judged against". They never mean approval. No decorative connectors.

## 4. Verbatim label map

Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts.

- Title zone: `DIAGNOSIS IS NOT RECOVERY`
- Lane 1 header: `Focused field probe`
- Lane 2 header: `Complete render`; lane 2 sub-tag: `Explicit ledger`
- Lane 3 header: `Fresh-process run`; lane 3 sub-tags: `Fresh folder`; `Unrelated working directory`
- Field bands (monospace, each labeled once at the band's left end): `permit_status`; `gate_time_mdt`
- Convergence bar: `Same acceptance requirements`

No other words. No Yes/No edge labels, because no node ends in `?`. No lane numbers or step numbers.

## 5. Visual family

`#0D0906` primary ground; `#17110C` panel fill; `#A58650` primary gold; `#C8A96A` sheen and connector highlights; `#C8B78A` secondary readable text; `#FFF8E7` primary text; `#655337` subdued nonessential rules; `#3A2E1B` faint structural lines; `#4F5634` restrained verified/allowed accents; `#B43A2F` warnings/blocked branches; `#2D3030` neutral mechanisms. Olive and brick red are fills, strokes, or pills only. Text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities. This figure needs no brick red. The two field bands are gold traces (#A58650 with #C8A96A sheen) and must not be color-coded as allowed or blocked.

## 6. Richness and legibility

Subtle warm panel gradients, thin gold sheen, precise gold traces, and restrained emission dots only on meaningful connections (the field-band junctions and the convergence traces). Modest inner/elevation shadows, sharp corners, and faint survey-grid texture away from text. Warm, restrained operational luminance: not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use a clean Inter/Helvetica-like sans-serif, with monospace for `permit_status` and `gate_time_mdt`. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density.

## 7. Honesty/exclusions

No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Specific prohibitions for this figure: no field values, times, permit states, or file paths. No check marks, PASS badges, or green lights claiming the proofs succeeded. Do not depict `permit_status` as permission to move, travel, or proceed: no gates opening, vehicles, or go signals. Do not show which field was the one that went missing, and do not emphasize either field over the other. Do not show any lane dropping a field.

## 8. Generation self-check instruction

The following must stay obvious: there are three separate lanes; both `permit_status` and `gate_time_mdt` cross all three lanes; all three lanes converge on the single `Same acceptance requirements` bar; `Explicit ledger` belongs to `Complete render`; `Fresh folder` and `Unrelated working directory` belong to `Fresh-process run`. The result is unusable if any lane, sub-tag, or field band is missing, misplaced, or duplicated, if either band stops before a lane, if lanes converge on different bars, if extra words, numbers, or success marks appear, or if the title differs from `DIAGNOSIS IS NOT RECOVERY`. This self-check does not replace post-generation inspection.

## 9. Revision requirements from review of the previous attempt
A previous generation of this figure was rejected. Generate a NEW image from this full contract and fix every defect below. All earlier blocks still govern; labels stay verbatim; add no words.

Transcription: "DIAGNOSIS IS NOT RECOVERY"; "Focused field probe"; "Complete render"; "Explicit ledger"; "Fresh-process run"; "Fresh folder"; "Unrelated working directory"; "permit_status"; "gate_time_mdt"; "Same acceptance requirements". All strings are exact and the field names are monospace; there are no extra words, numbers, or check marks. Defects: (1) Both field bands start at the right edge of their label tags, which sit inside lane 1. Lane 1's vertical trace runs behind the tags at x≈280 and has no junction node. So the Focused field probe lane shows no visible junction with either required field, while lanes 2 and 3 each have two. That breaks the core relationship the figure exists to show (lab §5: "Keep both required fields in every acceptance check"; the focused probe must report both fields as rendered), and it violates the brief's rule that neither band may skip a lane. (2) The title is set in a blown-out white glow against the top edge, with no safe margin. The off-white letters on near-white haze are barely legible and form the prohibited cinematic haze. That is the headline takeaway, so it fails the narrow-phone criterion as well. Fix: regenerate. Put the band labels in a gutter left of lane 1, outside every lane, so both bands visibly cross lane 1, and add gold junction nodes where both bands meet each of the three lane traces, six in total. Put the title in a solid dark title band with the 64 px margin and no glow.
````

## m05-restore-precondition

- Title: `PROVE THE RESTORE PATH FIRST`
- Publication path: `shared/figures/m05-restore-precondition.png`
- Anchor: Lab `## 2. Verify restore before any swap`.
- Caption: Confirm the restore reproduces the clean renderer before placing a fault, while preserving the existing attempt and output.
- Native size: 1536×1024; published SHA-256: `158ba6cdc7481a1176d0eda945ac5f1c7ea90f51a61286e3d506d40ef181d9d5`
- Iteration history:
  - attempt-01: full generation; session `01a10059-88ad-7dd1-8680-0c0858e7eb27`; raw SHA-256 `ff6ff2ce40a8e9a7…`; ACCEPTED
- Final review outcome: accepted attempt-01. FAcc: m05-restore-precondition: ACCEPT_A1 — the HOLD branch, the stop bar and the 'Only then place the fault' box are clear.

### Final prompt

````text
## 1. Tool/output instruction

$imagegen Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

## 2. Lesson contract

- Owning module/page/H2: Module 05 — Copper Span; published lab `module-05-diagnose-review/shared/MODULE_05_LAB.md`; H2 `## 2. Verify restore before any swap`.
- Learning takeaway (caption, HTML text only, not in image): "Confirm the restore reproduces the clean renderer before placing a fault, while preserving the existing attempt and output."
- Intended learner action in unfamiliar work: before deliberately changing or breaking any working component, prove that the recovery path actually works. The recovery path checks a trusted baseline fingerprint (digest), keeps the current component and its outputs as a retained attempt, then restores. Only a confirmed restore permits the deliberate change.
- Misconception prevented: "I have a backup, so I can break things first and restore later." An unproven restore path is not a recovery path. A digest mismatch stops the work (HOLD) before anything is replaced. Preserving the current attempt is part of restoring; restore does not overwrite it.

## 3. Composition

- Category: gated conditional flow (precondition gate) with one preservation side branch and one stop branch.
- Canvas: 1536×1024 landscape, 64 px safe margin on all sides. Title zone across the top (about 120 px tall). The rest is the mechanism. These are inline course images, so do not reserve slide-overlay space.
- Nodes and relationships, in reading order left to right along one main horizontal spine through the vertical middle of the mechanism area:
  1. `Clean baseline`: a panel at the far left holding a generic single-document glyph that stands for the trusted baseline renderer file.
  2. A gold trace arrow from `Clean baseline` into `Check digest`, a gate node drawn as a sharp-cornered diamond or a gate bar with a fingerprint-like hash motif and no readable characters.
  3. Stop branch: from `Check digest`, a brick-red stroked connector goes DOWN to a brick-red outlined terminal pill `Mismatch → HOLD`. This branch ends there with no onward arrow, and it visibly terminates before the replacement step. Draw a short hard stop bar at its end.
  4. Pass path: from `Check digest`, the gold spine continues right to `Preserve renderer + output`. Draw this as a panel with two small generic glyphs, a document (renderer) and a small stacked-files glyph (output). A short gold side trace UP from this panel into a small retained-attempt tray, with no label, shows that the existing renderer and output are kept and not overwritten.
  5. The gold spine continues right to `Restore work copy`, a panel whose document glyph now matches the baseline glyph's shape.
  6. The spine continues to `RESTORE OK`, an olive-filled confirmation pill with off-white text.
  7. A final gold arrow leads to `Only then place the fault` at the far right. This is the permitted next action, drawn as a neutral (#2D3030) panel with a gold outline, not as a success or approval badge.
- Focal relationship: the digest gate. Everything downstream (preserve, restore, RESTORE OK, place the fault) is reachable only through the passing side of `Check digest`, and the mismatch exits to HOLD before `Restore work copy`.
- Spatial zones: top = title; middle band = the main left-to-right spine; lower band under the gate = the HOLD stop terminal; upper band above the preserve panel = the small unlabeled retained-attempt tray. Keep generous spacing and prefer large type to crowding. Use two rows if the spine becomes cramped, keeping the order.
- Arrows mean only "proceeds to / gates". They never mean approval or authorization. No decorative connectors.

## 4. Verbatim label map

Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts.

- Title zone: `PROVE THE RESTORE PATH FIRST`
- Leftmost panel: `Clean baseline`
- Gate node: `Check digest`
- Stop terminal below the gate: `Mismatch → HOLD`
- Second spine panel: `Preserve renderer + output`
- Third spine panel: `Restore work copy`
- Confirmation pill: `RESTORE OK`
- Final rightmost panel: `Only then place the fault`

No other words anywhere. No Yes/No edge labels, because no node ends in `?`. No step numbers.

## 5. Visual family

`#0D0906` primary ground; `#17110C` panel fill; `#A58650` primary gold; `#C8A96A` sheen and connector highlights; `#C8B78A` secondary readable text; `#FFF8E7` primary text; `#655337` subdued nonessential rules; `#3A2E1B` faint structural lines; `#4F5634` restrained verified/allowed accents; `#B43A2F` warnings/blocked branches; `#2D3030` neutral mechanisms. Olive and brick red are fills, strokes, or pills only. Text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities. Here `RESTORE OK` uses an olive (#4F5634) fill, and `Mismatch → HOLD` uses a brick-red (#B43A2F) stroke and fill. Both carry #FFF8E7 text.

## 6. Richness and legibility

Subtle warm panel gradients, thin gold sheen, precise gold traces, and restrained emission dots only on meaningful connections (the gold spine and the preservation side trace). Modest inner/elevation shadows, sharp corners, and faint survey-grid texture away from text. Warm, restrained operational luminance: not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use a clean Inter/Helvetica-like sans-serif. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density.

## 7. Honesty/exclusions

No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Specific prohibitions for this figure: do not show hash strings, file paths, attempt-folder names, or numbers. Do not show the fault being placed before `RESTORE OK`. Do not draw any path from `Mismatch → HOLD` onward to replacement or to placing the fault. Do not depict restore as overwriting or discarding the existing renderer or output. Do not name or hint at which practice fault variant exists or which field it affects.

## 8. Generation self-check instruction

The following must stay obvious: `Check digest` gates everything to its right; a mismatch exits to `Mismatch → HOLD` and stops before `Restore work copy`; `Preserve renderer + output` happens before `Restore work copy`; `Only then place the fault` comes only after `RESTORE OK`. The result is unusable if any of these is missing or reordered: `Check digest`, `Mismatch → HOLD`, `Preserve renderer + output`, `Restore work copy`, `RESTORE OK`, `Only then place the fault`. It is also unusable if the HOLD branch connects onward, if extra words or numbers appear, or if the title differs from `PROVE THE RESTORE PATH FIRST`. This self-check does not replace post-generation inspection.
````

