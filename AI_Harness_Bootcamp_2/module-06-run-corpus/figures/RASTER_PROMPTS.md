# Raster figure prompts and provenance — module-06-run-corpus

Staff-only record. Not published (absent from `course.json`).

- Generator: `codex-cli 0.154.0` (`codex exec`, ChatGPT login, built-in `image_gen`).
- Style references attached to every invocation: `ui/images/home-hero.webp` and `ui/images/home-band-custody.webp`, decoded losslessly to PNG with `dwebp`; every figure except `m00-bounded-direction` also received the accepted `m00-bounded-direction` attempt-01 raster as a style-only reference. Label edits additionally attached the image being edited as the first input.
- Post-processing: the generator returns RGBA with a transparent ground. Each accepted raster was alpha-composited onto the specified `#0D0906` ground and saved as opaque lossless RGB PNG at native size. No other pixel changes, no resizing.
- Run evidence (all attempts, logs, rejected rasters, reviews): `~/course-evidence/course-raster-visuals/20261002T233502`
- Module source contract: `module-06-run-corpus/shared/MODULE_06_LAB.md` steps 1–5 and `shared/controls/PREDICATE_SPEC.md`. The authored corpus is practice material, not measured workplace/model reliability. Keep the strings learners must infer out of every image and caption.
- Owning page digests at integration (SHA-256): `shared/MODULE_06_LAB.md` 2bbeb2b27e6f46d2…

## m06-control-boundaries

- Title: `READ THE RESULT, NOT JUST THE EXIT`
- Publication path: `shared/figures/m06-control-boundaries.png`
- Anchor: Lab `## 5. Run the supplied control`, after its expected-results list and before recording results.
- Caption: MATCH and HOLD both exit 1; use the output text to distinguish a matched condition from a run the control could not decide.
- Native size: 1536×1024; published SHA-256: `3ef29b9deeb2f1102afe9c307517b91b190cc9fc151f299cc2860a71116a3446`
- Iteration history:
  - attempt-01: full generation; session `01a10057-80e2-7d82-9a18-906e44da1593`; raw SHA-256 `82824af840339864…`; ACCEPTED
- Final review outcome: accepted attempt-01. FAcc: m06-control-boundaries: ACCEPT_A1 — the monospace strings and the HOLD collector line are visible.

### Final prompt

````text
## 1. Tool/output instruction

$imagegen Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

## 2. Lesson contract

- Owning module/page/H2: Module 06 — Blue Gauge, `module-06-run-corpus/shared/MODULE_06_LAB.md`, H2 `## 5. Run the supplied control`. The figure goes after the expected-results list and before the instruction to copy results into `predicate-results.md`.
- Learning takeaway (caption, not image text): "MATCH and HOLD both exit 1; use the output text to distinguish a matched condition from a run the control could not decide."
- Learner action in unfamiliar work: test a check on known-bad and known-good inputs and on refusal cases (missing input, malformed config). Read the printed result line, not just the exit code, before recording what happened.
- Misconception prevented: that a nonzero exit always means "condition matched", or that a refusal is a decision about the run.

## 3. Composition

- Category: contrast grid of four independent input-to-outcome cards. This is NOT a pipeline: no arrows between cards.
- Canvas: 1536×1024 landscape, 64 px safe margin. Title zone at top. A 2×2 grid of cards fills the rest, with a bottom band.
- Top row, labeled by position as the decided tests:
  - Card 1: input `Known bad`, then result line `MATCH: both literals present`, then exit chip `exit 1`.
  - Card 2: input `Known good`, then result line `PASS: at least one literal absent`, then exit chip `exit 0`.
- Bottom row, the refusal cases, visually distinct (brick-red outline, neutral `#2D3030` fill):
  - Card 3: input `Missing run`, then result line `HOLD: missing input`, then exit chip `exit 1`.
  - Card 4: input `Malformed config`, then result line `HOLD: malformed config`, then exit chip `exit 1`.
- Within each card, a short gold trace runs from input to result line to exit chip.
- Focal relationship: the `exit 1` chips on Card 1 (MATCH) and on the HOLD cards are joined by a gold bracket that spans the grid. The bracket is labeled `HOLD also exits 1`. It shows that the exit code alone cannot separate MATCH from HOLD, so the result line must be read. Place the bracket so it visibly touches the MATCH card's `exit 1` and both HOLD cards' `exit 1`.

## 4. Verbatim label map

Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts.

- Title zone: `READ THE RESULT, NOT JUST THE EXIT`
- Card 1: `Known bad`; `MATCH: both literals present`; `exit 1`
- Card 2: `Known good`; `PASS: at least one literal absent`; `exit 0`
- Card 3: `Missing run`; `HOLD: missing input`; `exit 1`
- Card 4: `Malformed config`; `HOLD: malformed config`; `exit 1`
- Joining bracket: `HOLD also exits 1`

`exit 1` appears exactly three times (Cards 1, 3, 4) because each card requires it. No other duplicates or text. Result lines and exit chips use a clean monospace.

## 5. Visual family

`#0D0906` primary ground; `#17110C` panel fill; `#A58650` primary gold; `#C8A96A` sheen and connector highlights; `#C8B78A` secondary readable text; `#FFF8E7` primary text; `#655337` subdued nonessential rules; `#3A2E1B` faint structural lines; `#4F5634` restrained verified/allowed accents; `#B43A2F` warnings/blocked branches; `#2D3030` neutral mechanisms. Olive and brick red are fills, strokes, or pills only. Text is off-white or sandstone with high contrast. Every status has a text label as well as a color. No bright green, blue, cyan, teal, or purple. Do not use Starzl product names or product-specific color identities.

## 6. Richness and legibility

Subtle warm panel gradients, a thin gold sheen, and precise gold traces. Use restrained emission dots only on meaningful connections (inside each card, and the joining bracket). Modest inner and elevation shadows, sharp corners, and a faint survey-grid texture away from text. The light is warm and restrained, like an operations room. Not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use a clean Inter- or Helvetica-like sans-serif for inputs. Result lines and exit chips use a clean monospace. Title about 60 px. Major labels at least 38 px. All essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density.

## 7. Honesty/exclusions

No scene, people, hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal windows or UI chrome, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Specific to this figure: never show the literal strings, file contents, config JSON, paths, or command lines. Do not color MATCH olive or imply that MATCH or PASS is a release or approval. Do not chain the cards into a pipeline. Do not show oxygen cylinders, yards, or clinics.

## 8. Generation self-check instruction

Must remain obvious: four independent cards. Two are decided tests (MATCH/exit 1, PASS/exit 0). Two are refusals (HOLD/exit 1). One bracket joins the MATCH `exit 1` with both HOLD `exit 1` chips under `HOLD also exits 1`. The result is unusable if any of these happen: any result line deviates from the exact text; an exit code is swapped (especially if PASS shows `exit 1` or any HOLD shows `exit 0`); a card is missing; arrows connect cards; or the bracket omits the MATCH card.
````

## m06-first-failure-notes

- Title: `OBSERVE BEFORE CATEGORIZING`
- Publication path: `shared/figures/m06-first-failure-notes.png`
- Anchor: Lab `## 2. First-failure notes before categories`, after instructions and before Expected.
- Caption: Record each run's earliest supported problem, no failure, or uncertainty before assigning categories.
- Native size: 1536×1024; published SHA-256: `7596413cb55d1eb9427b396617ba8cb591bbaa98eeab357c545d339ecc8755d1`
- Iteration history:
  - attempt-01: full generation; session `01a10058-6cbd-7653-b28d-6ae26f4d296e`; raw SHA-256 `16091885e93bdf29…`; superseded — review: m06-first-failure-notes: enlarge 'Evidence passage' and remove title bloom
  - attempt-02: edit; session `01a1006b-f25b-7cf1-b393-f94f789df1fa`; raw SHA-256 `2528c7745dbffc1f…`; ACCEPTED
- Final review outcome: accepted attempt-02. F06: m06-first-failure-notes: ACCEPT_A2 — Nine labels are verbatim: 'OBSERVE BEFORE CATEGORIZING', 'One note per run', 'Run ID', 'Earliest supported problem', 'Evidence passage', 'No failure found', 'Uncertain', 'All notes first', 'Categories later'. 'Evidence passage' is now enlarged and bright, and the A1 legibility defect is fixed. There are three exclusive branches, the stack is collected by one brace, one arrow passes through the gate, and the bins are unnamed. This matches Lab §2, and the figure is legible at 800 px.

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to EDIT the first attached image and save exactly ONE corrected PNG. Do not use a CLI image fallback or write code/SVG. The other attachments are STYLE references only. Return the absolute saved PNG path and no claim of verification.

LABEL-LEVEL CORRECTIONS (apply exactly; preserve every other relationship and label):
- m06-first-failure-notes: enlarge 'Evidence passage' and remove title bloom
LABEL_EDIT. Transcription: 'OBSERVE BEFORE CATEGORIZING'; 'One note per run'; 'Run ID'; 'Earliest supported problem'; 'Evidence passage'; 'No failure found'; 'Uncertain'; 'All notes first'; 'Categories later'. No missing, misspelled or added words. The bins are unnamed and nothing bypasses the gate. Three sibling branches come from the Run ID field, the stack is gathered by one brace, and a single arrow passes through the 'All notes first' gate to 'Categories later'. This matches Lab §2. Defects: (1) 'Evidence passage' is about 20 px cap-height text in dim sandstone beside the passage glyph. It is below the required 32 px essential-copy minimum and the 'never dim essential words' rule, and it will be unreadable at article width. (2) The title sits on a bright white bloom/haze band (top about 0–150 px), which the style rules exclude. Fix: in the 'Earliest supported problem' panel, re-letter 'Evidence passage' at 32 px or more in #FFF8E7, keeping its position under the passage glyph. In the title zone, keep the text 'OBSERVE BEFORE CATEGORIZING' but remove the white glow/haze so the title sits on the #0D0906 ground. If an edit cannot remove the bloom cleanly, regenerate with the same composition.

The original full generation contract follows and still governs labels and composition:

## 1. Tool/output instruction

$imagegen Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

## 2. Lesson contract

- Owning module/page/H2: Module 06 — Blue Gauge, `module-06-run-corpus/shared/MODULE_06_LAB.md`, H2 `## 2. First-failure notes before categories`. The figure goes after the instructions and before **Expected**.
- Learning takeaway (caption, not image text): "Record each run's earliest supported problem, no failure, or uncertainty before assigning categories."
- Learner action in unfamiliar work: read each record on its own terms and write one note per record. The note names the earliest problem the text supports, with the passage that shows it, or says no failure was found, or keeps the case marked uncertain. Only after every record has a note do you start grouping.
- Misconception prevented: starting from a category name and fitting runs to it, inventing a failure for a clean run, or forcing uncertain runs into a decision.

## 3. Composition

- Category: per-item conditional flow that merges into a completeness gate.
- Canvas: 1536×1024 landscape, 64 px safe margin. Title zone at top. The mechanism fills the rest.
- Left zone (about 45% width): a single exemplar note card, drawn large, labeled `One note per run`. At the top of the card is a field labeled `Run ID`. Three mutually exclusive outcome slots branch from that card, stacked vertically, each its own small pill or panel:
  1. `Earliest supported problem`, with a gold trace to an attached small passage glyph labeled `Evidence passage` (the problem must cite the passage).
  2. `No failure found` (olive accent pill).
  3. `Uncertain` (neutral `#2D3030` pill, kept explicit).
  Behind the exemplar card, a faint stack of identical blank note cards (no text, no numbers) shows that each run gets its own card independently.
- Center: a vertical completeness gate. All note cards collect into one bundle labeled `All notes first`. Draw it as a gate bar. Nothing passes until the bundle is complete.
- Right zone: a panel labeled `Categories later`, reached only through the gate by a single gold arrow. Inside it are a few empty, unlabeled category bins (blank outlines, no names, no counts).
- Focal relationship: notes are written per run, then the full set passes the gate, and only then come categories. No arrow goes from any single note directly to a category bin.
- Reading order: left to right.

## 4. Verbatim label map

Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts.

- Title zone: `OBSERVE BEFORE CATEGORIZING`
- Exemplar card caption: `One note per run`
- Card top field: `Run ID`
- Branch 1: `Earliest supported problem`
- Attached to branch 1: `Evidence passage`
- Branch 2: `No failure found`
- Branch 3: `Uncertain`
- Center gate bundle: `All notes first`
- Right panel: `Categories later`

No other text. Do not write actual run IDs, quotes, or category names.

## 5. Visual family

`#0D0906` primary ground; `#17110C` panel fill; `#A58650` primary gold; `#C8A96A` sheen and connector highlights; `#C8B78A` secondary readable text; `#FFF8E7` primary text; `#655337` subdued nonessential rules; `#3A2E1B` faint structural lines; `#4F5634` restrained verified/allowed accents; `#B43A2F` warnings/blocked branches; `#2D3030` neutral mechanisms. Olive and brick red are fills, strokes, or pills only. Text is off-white or sandstone with high contrast. Every status has a text label as well as a color. No bright green, blue, cyan, teal, or purple. Do not use Starzl product names or product-specific color identities.

## 6. Richness and legibility

Subtle warm panel gradients, a thin gold sheen, and precise gold traces. Use restrained emission dots only on meaningful connections (problem to passage, bundle through gate). Modest inner and elevation shadows, sharp corners, and a faint survey-grid texture away from text. The light is warm and restrained, like an operations room. Not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use a clean Inter- or Helvetica-like sans-serif. Title about 60 px. Major labels at least 38 px. All essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density.

## 7. Honesty/exclusions

No scene, people, hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal or UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document and card glyphs only to show the note structure. Specific to this figure: show no real run identifiers, no quoted run text, no failure category names, no counts or proportions of outcomes, and no stamp words. Do not imply that every run has a failure. `No failure found` and `Uncertain` are legitimate, equal-weight outcomes. Do not show oxygen cylinders, yards, or clinics.

## 8. Generation self-check instruction

Must remain obvious: each run gets one note with exactly one of three outcomes. A supported problem is tied to its evidence passage. Categories are reached only after the complete note set passes the `All notes first` gate. The result is unusable if any of these happen: `No failure found` or `Uncertain` is missing; `Evidence passage` is detached from `Earliest supported problem`; any arrow skips the gate into `Categories later`; or category bins carry names or numbers.
````

## m06-freeze-sample

- Title: `FREEZE ELIGIBILITY BEFORE OUTCOMES`
- Publication path: `shared/figures/m06-freeze-sample.png`
- Anchor: Lab `## 1. Freeze the sample rule first`, before sample-rule commands.
- Caption: Freeze the sample before reading outcomes; if you already saw results, record that exposure rather than claim an outcome-blind attempt.
- Native size: 1536×1024; published SHA-256: `5856963e7ca24777911227313c6d033b2b6f85566ebd882868072a938cc57998`
- Iteration history:
  - attempt-01: full generation; session `01a10059-57f2-7782-b2fb-062e5c5a854f`; raw SHA-256 `e3fd39726b44e52e…`; superseded — review: m06-freeze-sample: stop blocked return path crossing exposure connector
  - attempt-02: full generation; session `01a1006c-df1d-7771-9a6b-03425b2ddd54`; raw SHA-256 `73ff19eb0f05ac53…`; ACCEPTED
- Final review outcome: accepted attempt-02. F06: m06-freeze-sample: ACCEPT_A2 — Seven labels are verbatim: 'FREEZE ELIGIBILITY BEFORE OUTCOMES', 'Save eligibility rule', 'R-001–R-016' (dash confirmed at zoom), 'Keep every eligible run', 'Then open outcomes', 'Do not add or drop by result', 'Record prior exposure'. The flow is rule → locked unmarked 4×4 set → dotted time gate → same tiles with blank outcome bars. The brick-red return path is blocked by a bar and an X and no longer crosses the gold exposure connector, which attaches to the gate. This matches Lab §1, the art is warm gold, and the text is large. The red arrowhead stops just

### Final prompt

````text
## 1. Tool/output instruction

$imagegen Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

## 2. Lesson contract

- Owning module/page/H2: Module 06 — Blue Gauge, `module-06-run-corpus/shared/MODULE_06_LAB.md`, H2 `## 1. Freeze the sample rule first`. The figure goes before the sample-rule commands.
- Learning takeaway (caption, not image text): "Freeze the sample before reading outcomes; if you already saw results, record that exposure rather than claim an outcome-blind attempt."
- Learner action in unfamiliar work: before you look at any results, write down and fix which records are in the sample. Keep every eligible record no matter how it turned out. If you have already seen results, write that down instead of claiming an outcome-blind reading.
- Misconception prevented: that you can pick or drop records after you see whether they passed or failed, or that a fresh folder makes outcomes you already saw unseen.

## 3. Composition

- Category: ordered dependency with a time gate (containment + sequence). This is not a filter funnel.
- Canvas: 1536×1024 landscape, 64 px safe margin. Title zone at top (about 120 px tall). The mechanism fills the rest.
- Left-to-right reading order in one main row:
  1. Left panel: a rule document glyph labeled `Save eligibility rule`.
  2. One gold trace runs from it to a center container. The container is a sealed bracketed set of sixteen identical, unmarked run-file tiles in a 4×4 grid, labeled `R-001–R-016`. The tiles have no outcome marks, no colors that suggest pass or fail, and no numbers on them. The container is closed and locked (thin gold border with a small lock or seal notch). Under it is the label `Keep every eligible run`.
  3. A vertical gate line divides the time sequence. Right of the gate is a panel labeled `Then open outcomes`. Here the same sixteen tiles stay inside the same container outline. Each tile has only a neutral, unreadable outcome glyph (blank small bar). No pass/fail tally, no colors per tile, no counts.
- Focal relationship: membership is fixed BEFORE outcomes are opened. The arrow from the frozen set to `Then open outcomes` means only "later in time". Outcomes flow nowhere back into membership.
- Second row (bottom band, two small panels):
  - Bottom center-right: a crossed-out return path (a brick-red stroke with a blocked bar) from the outcomes panel back toward the set boundary, labeled `Do not add or drop by result`. It shows that outcomes are never admission filters.
  - Bottom left: a separate side note card attached to the time gate by a thin dashed rule, labeled `Record prior exposure`. It is the branch for someone who already saw outcomes. It is a note added to the record, not a reset.
- No decorative connectors. Arrows never mean approval.

## 4. Verbatim label map

Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts.

- Title zone: `FREEZE ELIGIBILITY BEFORE OUTCOMES`
- Left panel: `Save eligibility rule`
- Center sealed set: `R-001–R-016`
- Under center set: `Keep every eligible run`
- Right panel heading: `Then open outcomes`
- Blocked return path (bottom band): `Do not add or drop by result`
- Side note card (bottom left): `Record prior exposure`

No other text. Do not number the tiles or write individual run IDs.

## 5. Visual family

`#0D0906` primary ground; `#17110C` panel fill; `#A58650` primary gold; `#C8A96A` sheen and connector highlights; `#C8B78A` secondary readable text; `#FFF8E7` primary text; `#655337` subdued nonessential rules; `#3A2E1B` faint structural lines; `#4F5634` restrained verified/allowed accents; `#B43A2F` warnings/blocked branches; `#2D3030` neutral mechanisms. Olive and brick red are fills, strokes, or pills only. Text is off-white or sandstone with high contrast. Every status has a text label as well as a color. No bright green, blue, cyan, teal, or purple. Do not use Starzl product names or product-specific color identities.

## 6. Richness and legibility

Subtle warm panel gradients, a thin gold sheen, and precise gold traces. Use restrained emission dots only on meaningful connections (the rule-to-set trace and the time gate). Modest inner and elevation shadows, sharp corners, and a faint survey-grid texture away from text. The light is warm and restrained, like an operations room. Not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use a clean Inter- or Helvetica-like sans-serif. The token `R-001–R-016` may use a clean monospace. Title about 60 px. Major labels at least 38 px. All essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density.

## 7. Honesty/exclusions

No scene, people, hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal or UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document and tile glyphs only to show containment. Specific to this figure: show no outcome for any run, no pass/fail counts or prevalence, and no selection of "clean" or "broken" runs. Do not suggest that outcomes decide membership. Do not suggest that a new attempt erases earlier exposure. Do not show oxygen cylinders, yards, or clinics.

## 8. Generation self-check instruction

Must remain obvious: the saved rule fixes the sixteen-run set first. Outcomes are opened only afterward. The return path from outcomes to membership is visibly blocked. The result is unusable if any of these happen: `R-001–R-016` is missing or altered (for example, to a different range or hyphen-only); the blocked-path label `Do not add or drop by result` is missing or attached to a forward arrow; `Record prior exposure` is missing; tiles show pass/fail colors or counts; or the arrow order puts outcomes before the rule.

## 9. Revision requirements from review of the previous attempt
A previous generation of this figure was rejected. Generate a NEW image from this full contract and fix every defect below. All earlier blocks still govern; labels stay verbatim; add no words. Title text sits directly on the dark ground with no white bloom/haze band.

- m06-freeze-sample: stop blocked return path crossing exposure connector
REGENERATE (minor). Transcription: 'FREEZE ELIGIBILITY BEFORE OUTCOMES'; 'Save eligibility rule'; 'R-001–R-016' (en dash confirmed at zoom); 'Keep every eligible run'; 'Then open outcomes'; 'Do not add or drop by result'; 'Record prior exposure'. No missing, added or misspelled text. The tiles are unnumbered and unmarked, with neutral bars only on the outcomes side. The order runs rule → frozen set → gate → outcomes, and the red return path is blocked by a bar and an X. This matches Lab §1. Defect: the brick-red return path (y≈765) crosses the dashed connector that drops from the time gate (x≈905) to 'Record prior exposure', right beside the blocked bar. The exposure note therefore also reads as attached to the blocked add/drop path, which is the ambiguous crossing that acceptance criterion 4 forbids. Placement under the gate is otherwise acceptable, although the brief asked for bottom-left. Fix: keep the composition, but route the red blocked path under or around the exposure card so it never crosses the dashed gate connector. Alternatively, move 'Record prior exposure' to the bottom left, linked to the gate by a dashed rule that does not touch the red path.
````

## m06-predicate-boundary

- Title: `TEST TEXT, NOT MEANING`
- Publication path: `shared/figures/m06-predicate-boundary.png`
- Anchor: Lab `## 4. Infer two literals and configure the supplied control`, after the case-sensitive substring explanation.
- Caption: Derive two exact literals from your notes; the supplied condition checks their co-occurrence, not the meaning or truth of the run.
- Native size: 1536×1024; published SHA-256: `6507d4d9696ed035260310af4ab469185de766d65048ceeb94f638d09a84a93d`
- Iteration history:
  - attempt-01: full generation; session `01a1005a-5079-71b2-aa65-d187f472305c`; raw SHA-256 `d2add2112b54fd27…`; superseded — review: m06-predicate-boundary: fix 'faillure' and move stamp to Both present
  - attempt-02: full generation; session `01a1006a-ed61-79a0-b6e3-f130cd27fffa`; raw SHA-256 `01269fe0015c0c79…`; superseded
  - attempt-03: edit; session `01a1008a-87fd-7b52-a1de-d3eec971f598`; raw SHA-256 `d4515ccc2c26ab61…`; ACCEPTED
- Final review outcome: accepted attempt-03. Final2: m06-predicate-boundary: ACCEPT_A3 (11 labels verbatim; the four requested labels are enlarged and off-white; the structure is unchanged: two literals reach one file, two probes feed AND all_present, the stamp sits on Both present, and the dashed semantic note has no path to the gate)

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to EDIT the first attached image and save exactly ONE corrected PNG with an OPAQUE #0D0906 background (no transparency). Do not use a CLI image fallback or write code/SVG. The other attachments are STYLE references only. Return the absolute saved PNG path and no claim of verification.

CORRECTIONS (apply exactly; preserve every other relationship, label, position and color):
m06-predicate-boundary: LABEL_EDIT_A2 — enlarge undersized mechanism labels
A2 structure is correct and fixes both A1 defects. A1 misspells 'Your faillure notes' and hangs the stamp from 'Either absent'. A2 transcription: 'TEST TEXT, NOT MEANING'; 'Literal A'; 'Literal B'; 'Case-sensitive substring'; 'One run file'; 'all_present' (monospace); 'Either absent'; 'Both present'; 'Not release authority'; 'Your failure notes'; 'Semantic judgment stays a note'. All are verbatim; there are no Yes/No labels, no real literal or stamp words, and the substring illustration uses blank bars. Two literals go to one file, two probes go to an AND gate, and the gate branches to Either absent and Both present. The red stamp is attached to Both present, and the semantic note is linked by dashes to the notes with no path to the gate. This matches PREDICATE_SPEC lines 5–11. Remaining defect: the decisive rule tag 'Case-sensitive substring' is drawn at about 16 px cap height (about 22 px type) in thin grey, roughly 8 px cap height at 800 px article width. That is the same size class that rejected 'Evidence passage' in m06-first-failure-notes A1. 'Your failure notes', 'One run file' and 'Semantic judgment stays a note' are also about 15–19 px cap in dim sandstone. Edit of attempt-02: (1) In the bracketed tag between the Literal A and Literal B traces (x≈610–815, y≈295–420), redraw 'Case-sensitive substring' on two lines at about 32 px type (cap height ≥ 23 px) in #FFF8E7. Widen the bracket as needed but keep it between the two traces, with the blank token-in-bar illustration below the text. (2) Redraw 'Your failure notes' (under the left note glyph), 'One run file' (above the file glyph) and 'Semantic judgment stays a note' (under the lower note card) at about 32 px in #FFF8E7. Change no other element.

The original full generation contract follows and still governs labels and composition:

## 1. Tool/output instruction

$imagegen Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

## 2. Lesson contract

- Owning module/page/H2: Module 06 — Blue Gauge, `module-06-run-corpus/shared/MODULE_06_LAB.md`, H2 `## 4. Infer two literals and configure the supplied control`. The figure goes after the case-sensitive substring explanation.
- Learning takeaway (caption, not image text): "Derive two exact literals from your notes; the supplied condition checks their co-occurrence, not the meaning or truth of the run."
- Learner action in unfamiliar work: turn a human-observed repeated failure into two exact, distinct, nonempty strings. Configure a mechanical co-occurrence check on a single file. Keep semantic judgment in your notes rather than in the check.
- Misconception prevented: that a text match proves meaning or truth (for example, that something was really released), that matching is case-insensitive or whole-word, or that a match is a release decision.

## 3. Composition

- Category: two-lane boundary diagram. The upper lane is mechanical. The lower lane is human judgment.
- Canvas: 1536×1024 landscape, 64 px safe margin. Title zone at top. Two rows.
- Upper lane (mechanical), left to right:
  - Source panel `Your failure notes` (note-card glyph with blank lines). Two gold traces leave it into two distinct token pills `Literal A` and `Literal B`. The pills are blank-bodied token shapes. Their labels are only the placeholder names; no actual strings.
  - A single document glyph `One run file`. Two presence-check probes, one per literal, scan the same file. Both probe outputs enter a single AND gate housing labeled `all_present`.
  - A small rule tag on the probes: `Case-sensitive substring`. Beside it, a tiny generic illustration: a short placeholder token drawn inside a longer blank word bar (no letters), showing that a literal inside a longer word still matches.
  - The AND gate has two output branches: `Both present` (gold or neutral pill; this is only a text condition) and `Either absent` (neutral pill).
- Lower lane (human), separated by a clear horizontal boundary rule:
  - A retained note card labeled `Semantic judgment stays a note`. A thin dashed link connects it back to `Your failure notes`. There is no arrow into the AND gate.
  - At the lane's right end, a boundary stamp outlined in brick red: `Not release authority`. It is placed against the `Both present` branch so the match is visibly NOT a release decision.
- Focal relationship: two literals, then two checks on the same file, then AND. Meaning stays in the human lane.

## 4. Verbatim label map

Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts.

- Title zone: `TEST TEXT, NOT MEANING`
- Source panel: `Your failure notes`
- Token pills: `Literal A`; `Literal B`
- File glyph: `One run file`
- AND gate: `all_present` (monospace)
- Probe rule tag: `Case-sensitive substring`
- Gate outputs: `Both present`; `Either absent`
- Lower lane note: `Semantic judgment stays a note`
- Boundary stamp: `Not release authority`

No other text. Never write any actual literal string, stamp word, or example word inside the pills, file, or substring illustration. The illustration uses blank bars only.

## 5. Visual family

`#0D0906` primary ground; `#17110C` panel fill; `#A58650` primary gold; `#C8A96A` sheen and connector highlights; `#C8B78A` secondary readable text; `#FFF8E7` primary text; `#655337` subdued nonessential rules; `#3A2E1B` faint structural lines; `#4F5634` restrained verified/allowed accents; `#B43A2F` warnings/blocked branches; `#2D3030` neutral mechanisms. Olive and brick red are fills, strokes, or pills only. Text is off-white or sandstone with high contrast. Every status has a text label as well as a color. No bright green, blue, cyan, teal, or purple. Do not use Starzl product names or product-specific color identities.

## 6. Richness and legibility

Subtle warm panel gradients, a thin gold sheen, and precise gold traces. Use restrained emission dots only on meaningful connections (notes to literals, probes to gate). Modest inner and elevation shadows, sharp corners, and a faint survey-grid texture away from text. The light is warm and restrained, like an operations room. Not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use a clean Inter- or Helvetica-like sans-serif. `all_present` uses a clean monospace. Title about 60 px. Major labels at least 38 px. All essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density.

## 7. Honesty/exclusions

No scene, people, hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal or UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Specific to this figure: NEVER show the actual inferred literal pair, any stamp word, or any example pair such as a word and its negated longer form. Show no JSON text, no regex symbols, no formulas, no false-positive rates, and no corpus results. Do not depict `olive` on `Both present`, which would imply approval. Do not show oxygen cylinders, yards, or clinics.

## 8. Generation self-check instruction

Must remain obvious: two literals from the notes are checked on the same single file and combined by AND. The human semantic note never feeds the gate. A match is marked `Not release authority`. The result is unusable if any of these happen: any real word appears inside `Literal A`, `Literal B`, the file, or the substring illustration; only one probe or two files are shown; `Either absent` or `Both present` is missing; or `Semantic judgment stays a note` has an arrow into the gate.
````

## m06-reconcile-history

- Title: `ACCOUNT FOR EACH RUN ONCE`
- Publication path: `shared/figures/m06-reconcile-history.png`
- Anchor: Lab `## 3. Then tally categories`, after the paragraph requiring retained original notes/revised labels.
- Caption: Reconcile pass, fail, and other to all sixteen runs once, and keep each original first-failure note beside any revised category.
- Native size: 1536×1024; published SHA-256: `429df8b614add3c4527116b5f9e27fdc91c2313d75fdee55a0f2e5f917f31499`
- Iteration history:
  - attempt-01: full generation; session `01a1005b-3fa9-7081-9914-36c296bc1966`; raw SHA-256 `6db35a188543d34c…`; superseded — review: m06-reconcile-history: route each Run ID to one bucket; other gets no ID
  - attempt-02: full generation; session `01a1006b-d716-76d0-9ad3-19b3edd8e4e9`; raw SHA-256 `9cd7f380dda42892…`; superseded
  - attempt-03: full generation; session `01a1008a-87ff-7111-aa5b-39deb5ce97c3`; raw SHA-256 `acda47cdb5406356…`; superseded
  - attempt-04: full generation; session `01a1023e-8644-7351-a22f-6af9c68b8f21`; raw SHA-256 `b942872e054c6225…`; ACCEPTED
- Final review outcome: accepted attempt-04. A4Review: m06-reconcile-history: ACCEPT_A4. All 11 labels are verbatim ('ACCOUNT FOR EACH RUN ONCE' / 'Run IDs' / 'Each run once' / 'pass' / 'fail by category' / 'other' / 'Original note' / 'Revised category' / 'Original notes stay' / 'Total = 16' / 'Counts do not close → HOLD'), with no numerals other than 16. Each of the six chips sends one trace from its own right-edge dot. Traces use nested lanes with no crossings: chips 1–2 go to the two 'other' chips, 3–4 to one chip in each 'fail' sub-bin, and 5–6 to the two 'pass' chips. Each trace ends on a chip dot, not on a header. 'Total = 16' has 

### Final prompt

````text
## 1. Tool/output instruction

$imagegen Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

## 2. Lesson contract

- Owning module/page/H2: Module 06 — Blue Gauge, `module-06-run-corpus/shared/MODULE_06_LAB.md`, H2 `## 3. Then tally categories`. The figure goes after the paragraph requiring that original first-failure notes stay visible next to any revised category label.
- Learning takeaway (caption, not image text): "Reconcile pass, fail, and other to all sixteen runs once, and keep each original first-failure note beside any revised category."
- Learner action in unfamiliar work: place every record ID in exactly one bucket, check that the bucket totals equal the fixed eligible membership, and record HOLD when they do not. When you rename a category, keep the original observation next to the new label.
- Misconception prevented: that category totals are trustworthy without per-ID reconciliation, that a run may be double-counted or dropped, or that relabeling replaces the original evidence.

## 3. Composition

- Category: one-to-one mapping plus a reconciliation check with a HOLD branch.
- Canvas: 1536×1024 landscape, 64 px safe margin. Title zone at top. The mechanism uses two rows.
- Top row, left to right:
  - Left column: a vertical stack of blank run-ID chips (no digits) headed `Run IDs`, with the rule label `Each run once` beside it. Each chip has exactly one gold trace leaving it. No chip has two traces, and no chip has zero.
  - Right: three bucket containers. `pass` (olive accent), `fail by category` (wider, subdivided into a few unlabeled sub-bins), and `other` (neutral `#2D3030`). Buckets contain blank chips only. No counts or numerals anywhere except the fixed total label.
- Inside or directly below `fail by category`: a history pair shown as two side-by-side columns on one record row. The left column is `Original note` and the right column is `Revised category`, joined by a thin gold link. A small anchor label `Original notes stay` sits on the left column to show the original is retained, not overwritten. There is no erasure or strike-through on the original.
- Bottom row: a reconciliation bar. The three buckets feed a single sum bracket labeled `Total = 16`. From the sum bracket, a brick-red side branch leads to a HOLD pill labeled `Counts do not close → HOLD`. This branch shows what happens when a run is missing or double-counted.
- Focal relationship: each ID maps once into a bucket, and the buckets reconcile to the fixed sixteen. A mismatch goes to HOLD.

## 4. Verbatim label map

Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts.

- Title zone: `ACCOUNT FOR EACH RUN ONCE`
- Left column heading: `Run IDs`
- Rule beside left column: `Each run once`
- Buckets: `pass`; `fail by category`; `other` (lowercase exactly as written)
- History pair: `Original note` (left column); `Revised category` (right column)
- Retention label on the original column: `Original notes stay`
- Sum bracket: `Total = 16`
- HOLD branch pill: `Counts do not close → HOLD`

No other text or numerals. Do not label sub-bins with category names. Do not put counts on buckets.

## 5. Visual family

`#0D0906` primary ground; `#17110C` panel fill; `#A58650` primary gold; `#C8A96A` sheen and connector highlights; `#C8B78A` secondary readable text; `#FFF8E7` primary text; `#655337` subdued nonessential rules; `#3A2E1B` faint structural lines; `#4F5634` restrained verified/allowed accents; `#B43A2F` warnings/blocked branches; `#2D3030` neutral mechanisms. Olive and brick red are fills, strokes, or pills only. Text is off-white or sandstone with high contrast. Every status has a text label as well as a color. No bright green, blue, cyan, teal, or purple. Do not use Starzl product names or product-specific color identities.

## 6. Richness and legibility

Subtle warm panel gradients, a thin gold sheen, and precise gold traces. Use restrained emission dots only on meaningful connections (ID-to-bucket traces, bucket-to-total). Modest inner and elevation shadows, sharp corners, and a faint survey-grid texture away from text. The light is warm and restrained, like an operations room. Not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use a clean Inter- or Helvetica-like sans-serif. `Total = 16` may use a clean monospace. Title about 60 px. Major labels at least 38 px. All essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density.

## 7. Honesty/exclusions

No scene, people, hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal or UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Specific to this figure: no per-bucket counts, no category prevalence, no category names, and no indication of how many runs pass or fail. Draw the chips so their distribution across buckets is not readable as a result: show only a few representative chips per bucket, roughly even and unnumbered. No frequency generalization to workplaces or models. Do not show oxygen cylinders, yards, or clinics.

## 8. Generation self-check instruction

Must remain obvious: each run ID leaves exactly one trace into one of three buckets. Buckets sum to `Total = 16`. A mismatch branches to `Counts do not close → HOLD`. The original note stays beside the revised category. The result is unusable if any of these happen: any bucket shows a number; `Total = 16` is altered; the HOLD branch is missing or shown as approval; `Original note` and `Revised category` are not side by side; or the original note is struck out or replaced.

## 9. Revision requirements from review of the previous attempt
A previous generation of this figure was rejected. Generate a NEW image from this full contract and fix every defect below. All earlier blocks still govern; labels stay verbatim; add no words. Title text sits directly on the dark ground with no white bloom/haze band.

- m06-reconcile-history: route each Run ID to one bucket; other gets no ID
REGENERATE. Transcription: 'ACCOUNT FOR EACH RUN ONCE'; 'Run IDs'; 'Each run once'; 'pass'; 'fail by category'; 'other'; 'Original note'; 'Revised category'; 'Original notes stay'; 'Total = 16'; 'Counts do not close → HOLD'. Every label is spelled correctly and has no added text. The arrow sign → and the '=' are correct. Structural defects: (1) four Run ID chips send four traces, two into 'pass' and two into 'fail by category'. 'other' gets no Run ID trace. Its two incoming arrows come from a junction under 'fail by category' (x≈1018, y≈482), which also feeds the history pair. This shows fail runs flowing into 'other' and breaks the one-to-one mapping the figure exists to teach. Bucket chips (2+4+2=8) also outnumber the four IDs. (2) 'Original notes stay' is drawn as small text (about 22 px) inside the Original note body, so it reads as note content rather than a retention anchor. A one-way arrow from Original note to Revised category suggests the note turns into the category. (3) The title has a bright white bloom/haze band behind it, and the prompt's style rules exclude cinematic haze. Fix: regenerate. Draw one trace from each Run ID chip to exactly one bucket, with at least one trace into each of 'pass', 'fail by category' and 'other'. Draw no bucket-to-bucket traces. Feed the history pair from 'fail by category' only, with no link to 'other'. Join Original note and Revised category with a plain non-directional rule. Place 'Original notes stay' (at least 32 px) as a tag outside the Original note column. Remove the title glow.


## 11. Final revision requirements
Render on an OPAQUE #0D0906 background with no transparent pixels. Fix every defect below:

m06-reconcile-history: REGENERATE — run-ID traces still not one-to-one
Both candidates are structurally wrong. A1 has 4 ID chips: two traces go to pass and two to fail. 'other' receives no ID; its two arrows come from a junction under 'fail by category', and two fail sub-bin chips have no source. A2 (transcribed labels: 'ACCOUNT FOR EACH RUN ONCE', 'Run IDs', 'Each run once', 'pass', 'fail by category', 'other', 'Original note', 'Revised category', 'Original notes stay', 'Total = 16', 'Counts do not close → HOLD'; all verbatim) is worse on mapping. Five traces leave from the Run IDs frame edge above or between chips, not from chip dots (y≈122, 148, 178, 205). Chip 6 (y≈462) has a dot but no trace. Pass chip 1 receives two traces (one from the left, one arrow from above). One trace ends on the pass header and one on the fail header. Other chip 2 has an orphan dot. 'Total = 16' has a stray incoming arrow from nowhere at its left edge (x≈690, y≈860). The history pair also feeds Total as a fourth input, which reads as a double count of fail runs. Composition fixes for regeneration: (1) Draw exactly six blank Run ID chips, each with exactly one gold trace starting at that chip's right-edge dot. No trace may start at the column frame. (2) Route chips 1–2 to two separate chips in 'other', chips 3–4 to one chip in each of two different 'fail by category' sub-bins, and chips 5–6 to two separate chips in 'pass'. Use nested lanes (higher lanes drop farther right) so no traces cross. Every bucket chip gets exactly one incoming trace; no arrow ends on a bucket header; no unconnected dots. (3) Feed 'Total = 16' from exactly three traces: the bottoms of pass, fail by category, and other. Draw nothing else into Total. (4) Hang the 'Original note' | 'Revised category' pair below 'fail by category' from one thin connector, joined side by side by a short gold link, with the 'Original notes stay' tag attached under the Original note column. The pair must not connect to Total. (5) Keep one brick-red arrow from Total to the 'Counts do not close → HOLD' pill. Keep all labels verbatim; no numerals except 'Total = 16'.


## 12. Attempt-4 requirements (previous attempt still failed)
OPAQUE #0D0906 background. Fix exactly:
Route fail bucket to Total without passing through the history pair
In m06-reconcile-history A3, the only path from 'fail by category' to 'Total = 16' runs through the history pair. The bucket bottom (x≈915) drops to the Original note / Revised category junction (y≈692). The middle input to Total (x≈830) rises from the 'Original notes stay' tag, which hangs under 'Original note'. Final-revision fix (4) said the pair must not connect to Total, and fix (3) said Total is fed by the three bucket bottoms only. The figure therefore shows the retained note record as part of the count, which is the defect flagged in A2. Also, all six ID traces stop on the bucket header tops (pass x≈450/540, fail x≈835/933, other x≈1270/1366), and separate stubs drop from the header divider to chips at different x positions (450/572, 820/1007, 1258/1381). This breaks fix (2): no trace may end on a bucket header, and each chip gets its own incoming trace.
Draw each connector as its own separate line from its own source to its own target; no shared trunks, T-junctions, merges, or lines ending in empty space. Before returning, trace every connector end to end.
````

