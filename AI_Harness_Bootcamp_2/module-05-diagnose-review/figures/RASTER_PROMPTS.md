# Figure prompts and provenance — module-05-diagnose-review

Staff-only record. Not published (absent from `course.json`).

- Generator: `codex-cli 0.154.0` (`codex exec`, built-in `image_gen`). No reference images attached.
- Style: flat light instructional diagram (warm off-white ground, white boxes, thin neutral borders, one ochre accent, muted red only for stop/HOLD, muted green only for allowed). Sentence-case titles and plain-language labels.
- Post-processing: composited onto the opaque `#FAF7F0` ground and saved as lossless RGB PNG at native size; no other pixel changes.
- Run evidence (all attempts, prompts, logs): `~/course-evidence/image-remake-20261003T204449`
- These figures replace an earlier set that used dark, glowing styling and slogan-style labels.

## m05-authorized-correction

- Title: When to replace the renderer
- Native size: 1536×1024; published SHA-256: `c7b65df94dcb63a3d54711f960ecc4822123c35ba90c511772126efb15f9534d`
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

TITLE (top-left): "When to replace the renderer"

TEXT ELEMENTS (each exactly once unless the layout says a token repeats; verbatim):
- "Sealed diagnosis"
- "Is the renderer the first failing boundary (renderer_omission)?"
- "Yes"
- "No"
- "HOLD: do not replace the renderer"
- "One authorized replacement: run restore once"
- "Save the failed renderer and output as a retained attempt"
- "Restore the clean renderer"
- "Not allowed, and not recovery:"
- "Hand-editing the output card"
- "Removing a required field from the acceptance requirements"

LAYOUT AND RELATIONSHIPS:
Left to right: 'Sealed diagnosis' → decision diamond 'Is the renderer the first failing boundary (renderer_omission)?' (renderer_omission in monospace). The No edge drops down to a muted-red end box 'HOLD: do not replace the renderer', with no onward arrow. The Yes edge goes right into a grouping frame headed 'One authorized replacement: run restore once'. Inside the frame, two boxes in sequence joined by an arrow meaning 'then': 'Save the failed renderer and output as a retained attempt' → 'Restore the clean renderer'. There is no loop and no second replacement. Below a divider, a plain panel headed 'Not allowed, and not recovery:' lists the two forbidden actions as bullets. They have no connectors and no glowing X strokes; at most a small muted 'not allowed' marker. No seal dot, no stripe, no ornaments.

REVISION REQUIREMENTS (a previous attempt was rejected; fix all of these):
- In attempt-01 the diamond's four-line label ends with '(renderer_omission)?', which runs nearly into the diamond's left and right edges at its widest line, so the label looks cramped. The spec also requires renderer_omission in monospace, but it is set in the proportional sans. Fix: make the diamond wider than it is tall (about 1.6:1), or shorten the line breaks to 'Is the renderer the first / failing boundary / (renderer_omission)?', so every line keeps at least 24 px clearance from the outline. Set renderer_omission in monospace. Keep all other elements and strings unchanged.

Before returning, check every text element is present, spelled exactly, and nothing else was added.
````

## m05-first-divergence

- Title: Find where the field first goes missing
- Native size: 1536×1024; published SHA-256: `24801dae5ff568fc4db4a2de0ac8fdc25753aac01d27d8ed3b8b3dc2a1ef2105`
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

TITLE (top-left): "Find where the field first goes missing"

TEXT ELEMENTS (each exactly once unless the layout says a token repeats; verbatim):
- "Selected source rows, one required field at a time"
- "Is the source value present?"
- "Do the selected rows agree?"
- "Does the card exist?"
- "Is the field on the card?"
- "Yes"
- "No"
- "source_omission"
- "source_conflict"
- "output_absent"
- "renderer_omission"
- "rendered"
- "Stop at the first failing check."
- "Before changing anything, seal: expected, observed, exact command."
- "Probe exit 0 means it ran, not that the card is complete."

LAYOUT AND RELATIONSHIPS:
Left two-thirds: a vertical chain that starts with the entry box 'Selected source rows, one required field at a time', followed by four decision diamonds in order: Is the source value present? → Do the selected rows agree? → Does the card exist? → Is the field on the card?. On the first three diamonds, Yes goes down to the next diamond and No goes right to a neutral monospace result chip: source_omission, source_conflict, output_absent. On the fourth diamond, Yes goes down to 'rendered' and No goes right to 'renderer_omission'. Every diamond has exactly one Yes and one No label. All result chips are neutral; none is highlighted as the actual result. 'Stop at the first failing check.' sits under the chip column. Right third, set off by a thin rule: a plain record panel with the seal sentence. One thin connector from the chip column into this panel means 'record the result'. Under the panel is a neutral note box (no ≠, no corner brackets) with the exit-status sentence. No field names, row IDs or wrong_input_version.

Before returning, check every text element is present, spelled exactly, and nothing else was added.
````

## m05-recovery-proofs

- Title: Three proofs of recovery
- Native size: 1536×1024; published SHA-256: `703e0347fe45f33ff636d05343c51e680881562aae79f1055051ad26c148502d`
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

TITLE (top-left): "Three proofs of recovery"

TEXT ELEMENTS (each exactly once unless the layout says a token repeats; verbatim):
- "1. Focused field probe"
- "Probe a newly rendered card"
- "2. Complete render"
- "Render from the explicit ledger"
- "3. Fresh-process run"
- "Fresh folder, started from an unrelated working directory"
- "Each proof must show both required fields"
- "permit_status"
- "gate_time_mdt"
- "All three proofs use the same acceptance requirements."
- "No proof drops or relaxes a field."

LAYOUT AND RELATIONSHIPS:
A simple grid of three equal numbered columns in order 1→2→3. Each column has its header and a one-line description beneath it. Below the headers, a row caption spanning the full width reads 'Each proof must show both required fields'. Two field rows follow, each labelled once at the left in monospace (permit_status, gate_time_mdt). Each row runs across all three columns, with a small neutral dot (not a checkmark and not a PASS mark) where it crosses each column. Neither field is emphasised over the other. Footer row spanning all columns: the two acceptance sentences. No empty corner cell (the field-label column header is left out or merged), no icons, no glow.

REVISION REQUIREMENTS (a previous attempt was rejected; fix all of these):
- In attempt-01 the field grid has four columns: a wide label column, then three dot columns. Those three columns do not line up with the three proof headers above them. The proof-1 dots (x≈649) sit under the left half of header 2, the proof-2 dots (x≈990) fall on the boundary between headers 2 and 3, and only the proof-3 dots sit under their own header. A reader cannot tell which proof each dot belongs to, which breaks the figure's one relationship (each proof shows both fields). Header 3's description ('Fresh folder, started from an unrelated working directory') is also set at about half the size of the other two descriptions, so it is hard to read at 800 px. Fix: regenerate as one grid. Put a narrow left gutter (about 22% of width) for the monospace field labels, and make the three header columns start at the gutter's right edge with exactly the same widths and x-positions as the three dot columns below. Leave the gutter's header cell empty or merge it into the caption row. Set all three descriptions at one size; let column 3's description wrap to two lines. Keep every string as it is.

Before returning, check every text element is present, spelled exactly, and nothing else was added.
````

## m05-restore-precondition

- Title: Confirm the restore works before placing the fault
- Native size: 1536×1024; published SHA-256: `5cb7a8b357e2583938441025d38bfa7a1934a88e43c6c88776400183e7906265`
- Accepted attempt: 03 of 3
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

TITLE (top-left): "Confirm the restore works before placing the fault"

TEXT ELEMENTS (each exactly once unless the layout says a token repeats; verbatim):
- "Clean baseline renderer"
- "Does the baseline digest match?"
- "No"
- "Yes"
- "HOLD: stop before replacing anything"
- "Save the current renderer and output as a retained attempt"
- "Copy the baseline over the work renderer"
- "RESTORE OK"
- "Now place the practice fault"

LAYOUT AND RELATIONSHIPS:
Left to right: 'Clean baseline renderer' → decision diamond 'Does the baseline digest match?'. The No edge drops down to a muted-red end box 'HOLD: stop before replacing anything', with no onward arrow and no T-bar glyph. The Yes edge continues right: 'Save the current renderer and output as a retained attempt' → 'Copy the baseline over the work renderer' → 'RESTORE OK' (plain box with a thin green outline, styled like the others) → 'Now place the practice fault'. Arrows mean 'then'. HOLD and RESTORE OK are in monospace. No frame, grid, glow, file icons, paths or hash strings.

REVISION REQUIREMENTS (previous attempts were rejected; fix all of these):
- FIX. Not one of the three layout requirements in fix.txt is met. (1) Node text is still about 22 px, not the required 26–28 px; it is visibly smaller than the sibling m05-authorized-correction. (2) The flow starts about 100 px below the title, not ~60 px. (3) The composition still does not fill the canvas: the band below y≈750 (about 27% of the height) is empty, and the whole lower-right quadrant under the Save/Copy/RESTORE OK/Now place nodes is blank. The relationships are correct: the No edge goes to HOLD with no onward arrow, and the Yes chain runs in page order. Separately, the whole HOLD label 'HOLD: stop before replacing anything' is set in monospace. The paired figure m05-authorized-correction sets 'HOLD: do not replace the renderer' in sans, so the two HOLD boxes are inconsistent. Regeneration: keep all strings, arrows and colours. Set node text at 27 px and let boxes grow to three- or four-line labels so the row height is about 220 px. Place the row about 60 px below the title. Hang HOLD under the diamond so its bottom sits near y≈850. Set only the token 'HOLD' (and 'RESTORE OK') in monospace; set ': stop before replacing anything' in the regular sans.

Before returning, check every text element is present, spelled exactly, and nothing else was added.
````

