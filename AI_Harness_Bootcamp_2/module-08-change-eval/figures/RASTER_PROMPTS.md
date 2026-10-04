# Figure prompts and provenance — module-08-change-eval

Staff-only record. Not published (absent from `course.json`).

- Generator: `codex-cli 0.154.0` (`codex exec`, built-in `image_gen`). No reference images attached.
- Style: flat light instructional diagram (warm off-white ground, white boxes, thin neutral borders, one ochre accent, muted red only for stop/HOLD, muted green only for allowed). Sentence-case titles and plain-language labels.
- Post-processing: composited onto the opaque `#FAF7F0` ground and saved as lossless RGB PNG at native size; no other pixel changes.
- Run evidence (all attempts, prompts, logs): `~/course-evidence/image-remake-20261003T204449`
- These figures replace an earlier set that used dark, glowing styling and slogan-style labels.

## m08-bounded-decision

- Title: Limit the decision to what you observed
- Native size: 1536×1024; published SHA-256: `907012316c5ac76061f931974c3990614988c28acc558d8fbb5277ab2cb9fb1d`
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

TITLE (top-left): "Limit the decision to what you observed"

TEXT ELEMENTS (each exactly once unless the layout says a token repeats; verbatim):
- "Observed cases"
- "Frozen rule"
- "Named configuration"
- "Actual repetitions"
- "Bounded adoption decision"
- "Outside the evidence: unseen cases and general superiority"
- "Recorded separately"
- "Failed-case count: a repair proxy, not repair time"
- "Elapsed time, tokens and SDK cost estimate"
- "Provider bill: unobserved unless you check your account"

LAYOUT AND RELATIONSHIPS:
Upper area: one plain rectangle with plain corners (no selection handles). Its four edges are labelled 'Observed cases' (top), 'Frozen rule' (right), 'Named configuration' (bottom) and 'Actual repetitions' (left). Centred inside is the box 'Bounded adoption decision', which shows no adopt/reject outcome. To the right, outside the rectangle and with no line crossing into it, a lightly shaded area with a thin red outline: 'Outside the evidence: unseen cases and general superiority'. Lower area, separated by a gap and a thin rule: the heading 'Recorded separately' over three cards side by side with visible gaps and no arrows between them or into the decision: 'Failed-case count: a repair proxy, not repair time'; 'Elapsed time, tokens and SDK cost estimate'; and 'Provider bill: unobserved unless you check your account', the last with a dashed border to show it is not observed. No numbers, currency, clocks or charts.

Before returning, check every text element is present, spelled exactly, and nothing else was added.
````

## m08-evidence-lanes

- Title: Keep supplied-file checks and live comparison separate
- Native size: 1536×1024; published SHA-256: `4a841ff42a52f8db62696763a245e088318a60bbd891cda9d8615bbdfb67a391`
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

TITLE (top-left): "Keep supplied-file checks and live comparison separate"

TEXT ELEMENTS (each exactly once unless the layout says a token repeats; verbatim):
- "Supplied files"
- "40 cases: baseline, A and B briefs"
- "Deterministic checks: same files, same answer; no model variation measured"
- "One violation rejects a candidate"
- "Optional live comparison (planned)"
- "6 cases, 3 repeats per instruction"
- "Baseline"
- "Checked"
- "Across: same-case pairs"
- "Down: within-instruction variation"
- "Keep every attempt"
- "One violation by the checked instruction rejects adoption"
- "Results are never pooled"

LAYOUT AND RELATIONSHIPS:
Two side-by-side lanes separated by a solid vertical divider labelled 'Results are never pooled'; no line crosses the divider. Left lane (about 40% width), headed 'Supplied files': a compact block '40 cases: baseline, A and B briefs', drawn as three short stacked columns of file outlines (not 40 rows). An arrow goes down to 'Deterministic checks: same files, same answer; no model variation measured', and an arrow from it to the lane's own result box 'One violation rejects a candidate'. Right lane (about 60% width), with a dashed outer border to show it is optional, headed 'Optional live comparison (planned)', with the tag '6 cases, 3 repeats per instruction'. The main element is a small grid for one case: two columns headed 'Baseline' and 'Checked', three rows of empty neutral slots (no outcome marks). A horizontal arrow across a row is labelled 'Across: same-case pairs'; a vertical arrow down one column is labelled 'Down: within-instruction variation'. Make the two arrows visibly different, for example solid versus dotted. A bracket under the grid reads 'Keep every attempt', and an arrow from it goes to the lane's own result box 'One violation by the checked instruction rejects adoption'. The two result boxes are never joined.

Before returning, check every text element is present, spelled exactly, and nothing else was added.
````

## m08-freeze-before-results

- Title: Freeze the rule before opening any candidate
- Native size: 1536×1024; published SHA-256: `42bd88ea53b405781b409c16fca66907e2a4eb7e5666df83878927a7c396533b`
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

TITLE (top-left): "Freeze the rule before opening any candidate"

TEXT ELEMENTS (each exactly once unless the layout says a token repeats; verbatim):
- "Rejection rule: any_violation_rejects"
- "40 case IDs"
- "Input and configuration hashes"
- "Batch manifests"
- "Names a supplied file; not proof that a model wrote it"
- "Frozen record (pre-result.json)"
- "Then inspect the candidates"
- "Results cannot change the rule or the record"

LAYOUT AND RELATIONSHIPS:
Left: four flat input boxes stacked vertically, top to bottom: 'Rejection rule: any_violation_rejects' (the token in monospace), '40 case IDs', 'Input and configuration hashes', 'Batch manifests'. A small footnote callout, 'Names a supplied file; not proof that a model wrote it', attaches by a short line to the 'Batch manifests' box only. Four separate arrows (meaning 'recorded into') run from the inputs into one plain box in the centre, 'Frozen record (pre-result.json)'. One forward arrow (meaning 'then') runs from the record to a closed box on the right, 'Then inspect the candidates'. Under them, one return arrow runs from the candidates box back toward the frozen record. It is drawn grey and crossed out with an X before it reaches the record, and labelled 'Results cannot change the rule or the record'. Flat icons or none: no book, chest, wax seal, fingerprint, model or robot glyphs, and no readable hashes or case IDs.

Before returning, check every text element is present, spelled exactly, and nothing else was added.
````

## m08-paired-hard-gates

- Title: One failed check rejects a candidate
- Native size: 1536×1024; published SHA-256: `df3ccfdfe4bc6ae86b73e5a0a46231736c35e5315afca248dc5d380479662550`
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

TITLE (top-left): "One failed check rejects a candidate"

TEXT ELEMENTS (each exactly once unless the layout says a token repeats; verbatim):
- "sources.json (same case)"
- "Baseline"
- "Candidate A"
- "Candidate B"
- "Format"
- "Mass with #payload locator"
- "UTC time with #gate locator"
- "MDT time with #gate locator"
- "Baseline must pass every check first"
- "Any baseline failure: HOLD; adoption is not evaluated"
- "Any one failed check rejects that candidate"
- "Never averaged across checks or cases"
- "Every result is kept"

LAYOUT AND RELATIONSHIPS:
Left: one document box 'sources.json (same case)' sends three separate arrows (meaning 'same input supplied to'), with no shared segment, to three column headers: 'Baseline', 'Candidate A', 'Candidate B'. Below the headers is a grid with four rows. The row labels appear once, at the left edge: 'Format', 'Mass with #payload locator', 'UTC time with #gate locator', 'MDT time with #gate locator' (#payload and #gate in monospace). Each cell is an empty neutral box. In rows 2–4, each cell is split into a value half and a smaller locator half. The cells show no pass or fail marks, ticks, crosses or colours, and there is no total or average bar under any column. The Baseline column has a heavier outline and the tag 'Baseline must pass every check first' above it. Below the Baseline column, one red-outlined exit: 'Any baseline failure: HOLD; adoption is not evaluated'. To the right of the candidate columns, each candidate cell has its own thin line into one bar, 'Any one failed check rejects that candidate'; no baseline cell connects to this bar. Under that bar, a small note: 'Never averaged across checks or cases'. A full-width footer band under all three columns reads 'Every result is kept'.

REVISION REQUIREMENTS (previous attempts were rejected; fix all of these):
- FIX. (1) A label is missing: the source box reads only 'sources.json'. The spec label is 'sources.json (same case)', and the page Figure text says one case's sources.json feeds all three briefs. (2) The Candidate A and Candidate B arrows leave the same point on the box's right edge (y≈133) and run together before they split, which is the shared segment fix.txt forbids. The Baseline arrow also passes through the 'Baseline must pass every check first' tag, so the tag looks like a step between the source and the baseline. (3) The Candidate A row 2 line (Mass with #payload locator) ends at the left edge of Candidate B's cell, with a tick at x≈955. It never reaches 'Any one failed check rejects that candidate', so the figure still says A's mass result flows into B, which is the defect that rejected attempt 1. (4) The candidate-to-bar lines are S-curves, while every other figure uses orthogonal connectors. Regeneration: render 'sources.json (same case)' verbatim. Draw three separate orthogonal arrows that leave three distinct points on the box's bottom edge and drop to the Baseline, Candidate A and Candidate B headers. Put the 'Baseline must pass every check first' tag directly above the Baseline column, to one side of its arrow and not in the arrow path. Give all eight candidate cells their own orthogonal line to the reject bar. Route Candidate A's four lines in the gutter between columns A and B, then under each B cell, and never into a B cell. Keep the empty cells, the baseline HOLD exit, the plain-line note and the footer band unchanged.

Before returning, check every text element is present, spelled exactly, and nothing else was added.
````

## m08-restore-baseline

- Title: Restore the baseline and confirm the rerun matches
- Native size: 1536×1024; published SHA-256: `91e73e25a90ccc7f09922193e2a695b1e95f2b16942de55a1c30518346611f2f`
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

TITLE (top-left): "Restore the baseline and confirm the rerun matches"

TEXT ELEMENTS (each exactly once unless the layout says a token repeats; verbatim):
- "Make the checked instruction active (previous file saved first)"
- "Stored hashes identify the frozen copies"
- "Restore the baseline control and briefs from those copies"
- "Candidate attempts are kept, not deleted"
- "Rerun the evaluation"
- "Compare original and restored result bytes"
- "Bytes match: restoration complete"
- "Bytes differ: HOLD"

LAYOUT AND RELATIONSHIPS:
A left-to-right flow with no step numbers; use two rows if needed for type size. Lead-in box with a grey outline: 'Make the checked instruction active (previous file saved first)'. An arrow leads to 'Stored hashes identify the frozen copies', and an arrow from that to 'Restore the baseline control and briefs from those copies'. A side archive box, 'Candidate attempts are kept, not deleted', hangs below the restore box on a plain line with no arrowhead. It is not on the main path and has no outgoing arrow. Main path continues: arrow to 'Rerun the evaluation', arrow to 'Compare original and restored result bytes', which shows two plain file outlines side by side. From the comparison, two labelled exits end in terminal boxes: right to 'Bytes match: restoration complete' (neutral outline, no tick or badge), and down to 'Bytes differ: HOLD' (red outline). No dot matrix, no 3D paper, no node left unconnected.

Before returning, check every text element is present, spelled exactly, and nothing else was added.
````

