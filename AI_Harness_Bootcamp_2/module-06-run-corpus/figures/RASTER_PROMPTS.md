# Figure prompts and provenance — module-06-run-corpus

Staff-only record. Not published (absent from `course.json`).

- Generator: `codex-cli 0.154.0` (`codex exec`, built-in `image_gen`). No reference images attached.
- Style: flat light instructional diagram (warm off-white ground, white boxes, thin neutral borders, one ochre accent, muted red only for stop/HOLD, muted green only for allowed). Sentence-case titles and plain-language labels.
- Post-processing: composited onto the opaque `#FAF7F0` ground and saved as lossless RGB PNG at native size; no other pixel changes.
- Run evidence (all attempts, prompts, logs): `~/course-evidence/image-remake-20261003T204449`
- These figures replace an earlier set that used dark, glowing styling and slogan-style labels.

## m06-control-boundaries

- Title: Control outputs and their exit codes
- Native size: 1536×1024; published SHA-256: `4ed2e9aa583c98671a6a11013957c4c5ce0caa19c20bc3a3e64827c870ce5ba5`
- Accepted attempt: 01 of 1

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to generate exactly ONE PNG instructional diagram. Do not write code or SVG. Return the absolute saved PNG path.

VISUAL STYLE (strict):
- Flat, clean technical diagram like a figure in a professional training manual or consulting report (think McKinsey/Stripe documentation). 1536x1024 landscape.
- Opaque solid warm off-white background #FAF7F0. No texture, no grid, no vignette, no gradients, no glow, no shadows, no 3D, no shine, no decorative icons, no illustrations.
- Boxes: white fill #FFFFFF, 1.5px solid border #C9C1B0, small 6px corner radius. Header strips or emphasis: deep ink #2B2A27 text; one accent colour, muted ochre #9A7B3C, for arrows and key borders; muted red #A23B2C only for stop/blocked items; muted green #4E6B3A only for allowed items. Arrows thin (2px), solid, simple arrowheads.
- Typography: one clean sans-serif (Inter or Helvetica style), sentence case everywhere (no ALL CAPS except code tokens and status words like HELD/BREACHED), title 44px semibold at top-left, labels 26-30px regular, generous padding, consistent spacing, aligned grid.
- Render every text string exactly as given, once, spelled correctly. Add no other words, numbers, logos or captions.

TITLE (top-left): "Control outputs and their exit codes"

TEXT ELEMENTS (each exactly once unless the layout says a token repeats; verbatim):
- "Output line"
- "Exit code"
- "Known bad"
- "MATCH: both literals present"
- "exit 1"
- "Known good"
- "PASS: at least one literal absent"
- "exit 0"
- "Missing run"
- "HOLD: missing input"
- "exit 1"
- "Malformed config"
- "HOLD: malformed config"
- "exit 1"
- "Three cases exit 1; only the output line separates MATCH from HOLD"

LAYOUT AND RELATIONSHIPS:
A four-row table on a light ground, with no arrows between rows. Columns: an unlabelled case column, 'Output line' and 'Exit code'. Rows in this order: Known bad / MATCH: both literals present / exit 1; Known good / PASS: at least one literal absent / exit 0; Missing run / HOLD: missing input / exit 1; Malformed config / HOLD: malformed config / exit 1. Monospace only for the output lines and the exit codes; case names in sans-serif. Leave a slightly larger gap between row 2 and row 3, so the two decided results (MATCH, PASS) read as one group and the two refusals (HOLD) as another. Give the HOLD rows a light grey fill; the word HOLD itself states their status, so colour is never the only signal. On the right, a single bracket spans the three 'exit 1' cells (rows 1, 3 and 4, skipping row 2) and carries the note 'Three cases exit 1; only the output line separates MATCH from HOLD'. MATCH is not coloured green or as an approval.

Before returning, check every text element is present, spelled exactly, and nothing else was added.
````

## m06-first-failure-notes

- Title: Note every run before assigning categories
- Native size: 1536×1024; published SHA-256: `102b06d9d2a0d50829e7e1e8663fd8dc9033e4e3a61650080f4fbeb37b70229e`
- Accepted attempt: 01 of 1

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to generate exactly ONE PNG instructional diagram. Do not write code or SVG. Return the absolute saved PNG path.

VISUAL STYLE (strict):
- Flat, clean technical diagram like a figure in a professional training manual or consulting report (think McKinsey/Stripe documentation). 1536x1024 landscape.
- Opaque solid warm off-white background #FAF7F0. No texture, no grid, no vignette, no gradients, no glow, no shadows, no 3D, no shine, no decorative icons, no illustrations.
- Boxes: white fill #FFFFFF, 1.5px solid border #C9C1B0, small 6px corner radius. Header strips or emphasis: deep ink #2B2A27 text; one accent colour, muted ochre #9A7B3C, for arrows and key borders; muted red #A23B2C only for stop/blocked items; muted green #4E6B3A only for allowed items. Arrows thin (2px), solid, simple arrowheads.
- Typography: one clean sans-serif (Inter or Helvetica style), sentence case everywhere (no ALL CAPS except code tokens and status words like HELD/BREACHED), title 44px semibold at top-left, labels 26-30px regular, generous padding, consistent spacing, aligned grid.
- Render every text string exactly as given, once, spelled correctly. Add no other words, numbers, logos or captions.

TITLE (top-left): "Note every run before assigning categories"

TEXT ELEMENTS (each exactly once unless the layout says a token repeats; verbatim):
- "One note per run (first-failures.md)"
- "Run ID"
- "Record exactly one of:"
- "Earliest supported problem"
- "Evidence passage that shows it"
- "No failure found"
- "Uncertain"
- "All 16 notes complete"
- "Then group the notes into categories"

LAYOUT AND RELATIONSHIPS:
Left (about 45% width): one flat note template, a single card with no stacked or offset copies. Its top line reads 'One note per run (first-failures.md)', and the first field is 'Run ID'. Under it is the prompt 'Record exactly one of:', followed by three equal-weight option rows, each with an empty radio circle so that only one can be chosen: 'Earliest supported problem', 'No failure found', 'Uncertain'. A short bracket ties a small indented sub-box, 'Evidence passage that shows it', to the 'Earliest supported problem' row only. Centre: a plain vertical checkpoint bar labelled 'All 16 notes complete'. One arrow runs from the note card to the checkpoint, and one arrow from the checkpoint to the right panel; no line bypasses the checkpoint. Right: a panel headed 'Then group the notes into categories' containing three or four empty, unlabelled category boxes with no names and no counts. Read left to right. All three options get the same visual weight; do not emphasise the problem option.

Before returning, check every text element is present, spelled exactly, and nothing else was added.
````

## m06-freeze-sample

- Title: Freeze the sample before reading outcomes
- Native size: 1536×1024; published SHA-256: `d07b4de508763262ec27b5a14cc17e381a2c4b58e09311ffd294c0615ada6691`
- Accepted attempt: 02 of 2
- Earlier attempts were rejected in review for relationship or layout defects; the last revision requirements are included at the end of the prompt.

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to generate exactly ONE PNG instructional diagram. Do not write code or SVG. Return the absolute saved PNG path.

VISUAL STYLE (strict):
- Flat, clean technical diagram like a figure in a professional training manual or consulting report (think McKinsey/Stripe documentation). 1536x1024 landscape.
- Opaque solid warm off-white background #FAF7F0. No texture, no grid, no vignette, no gradients, no glow, no shadows, no 3D, no shine, no decorative icons, no illustrations.
- Boxes: white fill #FFFFFF, 1.5px solid border #C9C1B0, small 6px corner radius. Header strips or emphasis: deep ink #2B2A27 text; one accent colour, muted ochre #9A7B3C, for arrows and key borders; muted red #A23B2C only for stop/blocked items; muted green #4E6B3A only for allowed items. Arrows thin (2px), solid, simple arrowheads.
- Typography: one clean sans-serif (Inter or Helvetica style), sentence case everywhere (no ALL CAPS except code tokens and status words like HELD/BREACHED), title 44px semibold at top-left, labels 26-30px regular, generous padding, consistent spacing, aligned grid.
- Render every text string exactly as given, once, spelled correctly. Add no other words, numbers, logos or captions.

TITLE (top-left): "Freeze the sample before reading outcomes"

TEXT ELEMENTS (each exactly once unless the layout says a token repeats; verbatim):
- "Save the eligibility rule (sample-rule.md) and record its fingerprint"
- "Sample fixed: R-001 to R-016 (16 runs)"
- "Keep every eligible run"
- "Membership is fixed before any outcome is read"
- "Then open the outcomes"
- "Do not add or remove a run because of its result"
- "Saw outcomes before saving the rule?"
- "Record that exposure; do not claim an outcome-blind attempt"

LAYOUT AND RELATIONSHIPS:
Light ground, flat strokes, no padlocks and no glow. Main row, read left to right. (1) A plain document box: 'Save the eligibility rule (sample-rule.md) and record its fingerprint'. A solid arrow (meaning 'then') goes to (2) a bordered container holding a 4×4 grid of 16 identical blank tiles. The tiles carry no IDs, no colours and no marks. The container caption above it is 'Sample fixed: R-001 to R-016 (16 runs)', and the note under it is 'Keep every eligible run'. A vertical dashed time line follows, labelled along its length 'Membership is fixed before any outcome is read'. A solid arrow crosses that line to (3) the same 4×4 container outline headed 'Then open the outcomes'. Its 16 tiles each show one small neutral grey bar: no pass/fail colours, no counts, no symbols. Below the main row, one return arrow runs from container (3) back toward container (2). It is drawn grey and crossed out with a single X where it meets container (2). The label beside it is 'Do not add or remove a run because of its result'. Bottom-left, a separate exception box with a thin outline, attached by one dotted line to the time line only (it must not touch the crossed-out return arrow): the heading 'Saw outcomes before saving the rule?' and the body line 'Record that exposure; do not claim an outcome-blind attempt'.

REVISION REQUIREMENTS (a previous attempt was rejected; fix all of these):
- The dashed time line runs down to y≈720, the grey crossed-out return arrow from 'Then open the outcomes' to the sample container runs at y≈725 on the same x (≈993), and the dotted exposure connector resumes below the label 'Do not add or remove a run because of its result' at the same x before turning left to 'Saw outcomes before saving the rule?'. Read at normal size, this is one dotted line passing through the return arrow and its label. That is the crossing the spec forbids ('it must not touch the crossed-out return arrow'); the same defect rejected the previous attempt. Fix for full regeneration: route the crossed-out return arrow over the top of the two containers (from the top edge of the outcomes container back to the top edge of the sample container, X near the sample container, label above it). Keep the dashed time line running uninterrupted from the top of the main row to the bottom, then attach the exception box bottom-left by one dotted elbow from the time line's lower end. No other line may sit on the time line's x below the containers. All labels unchanged.

Before returning, check every text element is present, spelled exactly, and nothing else was added.
````

## m06-predicate-boundary

- Title: What the supplied control checks
- Native size: 1536×1024; published SHA-256: `8d5bf682e8dd2d4dc8dd352ba91eae751c3622127b3669ea348a228eee9e78b1`
- Accepted attempt: 01 of 1

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to generate exactly ONE PNG instructional diagram. Do not write code or SVG. Return the absolute saved PNG path.

VISUAL STYLE (strict):
- Flat, clean technical diagram like a figure in a professional training manual or consulting report (think McKinsey/Stripe documentation). 1536x1024 landscape.
- Opaque solid warm off-white background #FAF7F0. No texture, no grid, no vignette, no gradients, no glow, no shadows, no 3D, no shine, no decorative icons, no illustrations.
- Boxes: white fill #FFFFFF, 1.5px solid border #C9C1B0, small 6px corner radius. Header strips or emphasis: deep ink #2B2A27 text; one accent colour, muted ochre #9A7B3C, for arrows and key borders; muted red #A23B2C only for stop/blocked items; muted green #4E6B3A only for allowed items. Arrows thin (2px), solid, simple arrowheads.
- Typography: one clean sans-serif (Inter or Helvetica style), sentence case everywhere (no ALL CAPS except code tokens and status words like HELD/BREACHED), title 44px semibold at top-left, labels 26-30px regular, generous padding, consistent spacing, aligned grid.
- Render every text string exactly as given, once, spelled correctly. Add no other words, numbers, logos or captions.

TITLE (top-left): "What the supplied control checks"

TEXT ELEMENTS (each exactly once unless the layout says a token repeats; verbatim):
- "Your failure notes"
- "Literal A"
- "Literal B"
- "Two different exact strings"
- "One run file"
- "Case-sensitive substring search: a literal inside a longer word still matches"
- "all_present"
- "Both literals present: MATCH"
- "At least one literal absent: PASS"
- "A match is not permission to release"
- "Meaning and truth stay in your notes; the check never reads them"

LAYOUT AND RELATIONSHIPS:
Upper band (the mechanical check), read left to right. A note card 'Your failure notes' sends two arrows to two token pills, 'Literal A' and 'Literal B', with a brace under the pair labelled 'Two different exact strings'. The pills are blank-bodied and contain no real words. Both pills point at a single document 'One run file': one search arrow per literal, and both land on the same file. Beside the search arrows is a small note, 'Case-sensitive substring search: a literal inside a longer word still matches'. It carries a tiny abstract illustration: a short solid bar drawn inside a longer outlined bar, with no letters. Both search results feed one gate box, 'all_present' (monospace). The gate has two exits: 'Both literals present: MATCH' and 'At least one literal absent: PASS'. Both exits are neutral grey; neither is green or approval-coloured. Directly under the MATCH exit is a red-outlined note: 'A match is not permission to release'. Lower band, separated by a full-width thin rule: one note box, 'Meaning and truth stay in your notes; the check never reads them', joined by a dotted line up to 'Your failure notes' only. Nothing in the lower band connects to the gate or to the file. Spread the elements evenly across both bands.

Before returning, check every text element is present, spelled exactly, and nothing else was added.
````

## m06-reconcile-history

- Title: Count each run exactly once
- Native size: 1536×1024; published SHA-256: `afdcf47abac2cab27283e82fc3ff00f70855028c5de8262d1c5f9e4ab67ff511`
- Accepted attempt: 04 of 4
- Earlier attempts were rejected in review for relationship or layout defects; the last revision requirements are included at the end of the prompt.

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to generate exactly ONE PNG instructional diagram. Do not write code or SVG. Return the absolute saved PNG path.

VISUAL STYLE (strict):
- Flat, clean technical diagram like a figure in a professional training manual or consulting report (think McKinsey/Stripe documentation). 1536x1024 landscape.
- Opaque solid warm off-white background #FAF7F0. No texture, no grid, no vignette, no gradients, no glow, no shadows, no 3D, no shine, no decorative icons, no illustrations.
- Boxes: white fill #FFFFFF, 1.5px solid border #C9C1B0, small 6px corner radius. Header strips or emphasis: deep ink #2B2A27 text; one accent colour, muted ochre #9A7B3C, for arrows and key borders; muted red #A23B2C only for stop/blocked items; muted green #4E6B3A only for allowed items. Arrows thin (2px), solid, simple arrowheads.
- Typography: one clean sans-serif (Inter or Helvetica style), sentence case everywhere (no ALL CAPS except code tokens and status words like HELD/BREACHED), title 44px semibold at top-left, labels 26-30px regular, generous padding, consistent spacing, aligned grid.
- Render every text string exactly as given, once, spelled correctly. Add no other words, numbers, logos or captions.

TITLE (top-left): "Count each run exactly once"

TEXT ELEMENTS (each exactly once unless the layout says a token repeats; verbatim):
- "Run IDs: R-001 to R-016"
- "Each run goes into exactly one group"
- "pass"
- "fail by category"
- "other"
- "Original first-failure note"
- "Revised category"
- "Keep the original note beside any revised category"
- "Total = 16"
- "Not 16, or a run missing or counted twice: HOLD"

LAYOUT AND RELATIONSHIPS:
Three side-by-side group panels headed 'pass', 'fail by category', 'other'. Show membership by CONTAINMENT, not connectors: each panel contains exactly two small blank run chips placed inside it (six chips total, no IDs written on chips). Above the panels, one line of text 'Run IDs: R-001 to R-016' and the note 'Each run goes into exactly one group'. Inside the 'fail by category' panel, below its two chips, one row with two side-by-side boxes 'Original first-failure note' and 'Revised category' joined by a short plain line (no arrowhead), and under them the note 'Keep the original note beside any revised category'. Below the three panels, one plain arrow from each panel bottom joins into a single box 'Total = 16'. From 'Total = 16' one arrow to the right into a red-outlined box with the HOLD text. No other connectors anywhere; no line crosses any panel.

Before returning, check every text element is present, spelled exactly, and nothing else was added.
````

