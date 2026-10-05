# Figure prompts and provenance — module-00-setup

Staff-only record. Not published (absent from `course.json`).

- Generator: `codex-cli 0.154.0` (`codex exec`, built-in `image_gen`). No reference images attached.
- Style: flat light instructional diagram (warm off-white ground, white boxes, thin neutral borders, one ochre accent, muted red only for stop/HOLD, muted green only for allowed). Sentence-case titles and plain-language labels.
- Post-processing: composited onto the opaque `#FAF7F0` ground and saved as lossless RGB PNG at native size; no other pixel changes.
- Run evidence (all attempts, prompts, logs): `~/course-evidence/image-remake-20261003T204449`; `m00-bounded-direction` and `m00-responsibility-screen` were regenerated on 2026-10-04 with concrete decision labels, evidence in `~/course-evidence/image-remake-20261004T161818Z-north-shelf`.
- These figures replace an earlier set that used dark, glowing styling and slogan-style labels.

## m00-bounded-direction

- Title: Write a testable direction before the run
- Native size: 1536×1024; published SHA-256: `70d9208f16b4f30c50a91a8ea85cbebc2aa3e7148eda7fc423415aa85505694c`
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

TITLE (top-left): "Write a testable direction before the run"

TEXT ELEMENTS (each exactly once unless the layout says a token repeats; verbatim):
- "AI: drafts from the supplied facts"
- "You: check the facts and make the send-or-hold call"
- "Refused: real sending, release or any outside action"
- "direction-brief.md"
- "Outcome and audience"
- "Allowed sources and constraints"
- "Precedence: which source governs a conflict"
- "What a correct email must show"
- "Falsifier: an observation that would prove the email wrong"
- "Stop condition"
- "Who decides it goes out: you"
- "Freeze the direction before the first run"

LAYOUT AND RELATIONSHIPS:
Top row: three equal, separate boxes side by side in neutral fill. Left to right: 'AI: drafts from the supplied facts', 'You: check the facts and make the send-or-hold call', 'Refused: real sending, release or any outside action' (only this box may carry the red blocked accent). From each, one short vertical line drops into the top edge of one large bordered frame below. The lines mean 'is written into'. The frame is headed 'direction-brief.md' and holds seven equal cells in two rows. Row 1: Outcome and audience | Allowed sources and constraints | Precedence: which source governs a conflict. Row 2: What a correct email must show | Falsifier: an observation that would prove the email wrong | Stop condition | Who decides it goes out: you. No cell is highlighted. The frame footer reads 'Freeze the direction before the first run'. No arrow leaves the frame, so nothing implies approval.

Before returning, check every text element is present, spelled exactly, and nothing else was added.
````

## m00-change-isolation

- Title: Change only what depends on the new fact
- Native size: 1536×1024; published SHA-256: `b2da7482aa248ba56c227527d1eb0cfae3ef8429ea19316a1ed6f740cda94078`
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

TITLE (top-left): "Change only what depends on the new fact"

TEXT ELEMENTS (each exactly once unless the layout says a token repeats; verbatim):
- "Keep the original draft"
- "Write down what must change and what must not"
- "Apply the one changed fact"
- "Update the statements that depend on it"
- "Keep authority, audience and other facts unchanged"
- "Compare both drafts"
- "Changed draft: artifact-changed.md"
- "The original checker still expects the old count"
- "So the changed draft fails that check"
- "Do not edit the checker to hide the failure"

LAYOUT AND RELATIONSHIPS:
Top row, left to right, 'then' arrows: 'Keep the original draft' → 'Write down what must change and what must not' → 'Apply the one changed fact'. From the third box, a fork with two orthogonal branches: upper 'Update the statements that depend on it', lower 'Keep authority, audience and other facts unchanged'. The two branches stay apart and rejoin only at 'Compare both drafts' on the right. Below, a separate branch drawn in the warning colour starts at 'Changed draft: artifact-changed.md' (a box placed after the fork, fed by the upper branch). It runs to 'The original checker still expects the old count' → 'So the changed draft fails that check' → 'Do not edit the checker to hide the failure'. No arrow points into the checker box from an edit action. Centred text in every box; no icons, badges or document glyphs; no counts.

REVISION REQUIREMENTS (a previous attempt was rejected; fix all of these):
- The red warning connector leaves from the left edge of 'Update the statements that depend on it' (x≈855, y≈345), right beside the incoming gold fork arrow. It then drops vertically and crosses the gold connector into 'Keep authority, audience and other facts unchanged' at about (855, 565). The crossing makes the warning branch look as if it comes off the fork or cuts through the 'keep unchanged' branch. The spec requires the two branches to stay apart, with the changed-draft box fed only by the upper branch. Regenerate with the red connector leaving from the top or right side of the update box, or from a point after it. Route it above the fork, or around the right of the 'Compare both drafts' column, down to 'Changed draft: artifact-changed.md', with no crossing of any gold connector. Alternatively, place the changed-draft box directly after the update box on the upper branch. Keep all text unchanged.

Before returning, check every text element is present, spelled exactly, and nothing else was added.
````

## m00-claim-check

- Title: Trace each claim to its source
- Native size: 1536×1024; published SHA-256: `f91738908ac89da930ff06ad89a6fffd22d705be4a52d18a84e10e291571ca06`
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

TITLE (top-left): "Trace each claim to its source"

TEXT ELEMENTS (each exactly once unless the layout says a token repeats; verbatim):
- "Material claim"
- "Source and locator (line or paragraph)"
- "Quoted support"
- "What the quote establishes"
- "What it does not establish"
- "An action a reader might infer"
- "Not supported"
- "Mechanical checks"
- "Human interpretation"

LAYOUT AND RELATIONSHIPS:
Top chain, left to right, 'then' arrows: 'Material claim' → 'Source and locator (line or paragraph)' → 'Quoted support'. From 'Quoted support', an orthogonal fork down to two side-by-side boxes: 'What the quote establishes' (left) and 'What it does not establish' (right). From 'What it does not establish', a dashed red connector ending in a perpendicular stop bar, with the small label 'Not supported' at the bar, leads toward 'An action a reader might infer' at far right. This is a blocked link, not an arrow. Both fork boxes feed down by straight arrows into 'Human interpretation' (bottom centre). A separate lower-left box, 'Mechanical checks', has one straight arrow into 'Human interpretation' only, and no connection to the inferred-action box. Even spacing; no S-bends.

Before returning, check every text element is present, spelled exactly, and nothing else was added.
````

## m00-falsifier

- Title: Test the checker on a copy
- Native size: 1536×1024; published SHA-256: `f5adfea450274ea6ac019c61bd2b7dbc4c03b97a63e07d37e4e83807e0c76569`
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

TITLE (top-left): "Test the checker on a copy"

TEXT ELEMENTS (each exactly once unless the layout says a token repeats; verbatim):
- "Original: artifact.md"
- "Keep the original unchanged"
- "Record its hash"
- "Later, confirm the hash is unchanged"
- "Test copy: falsifier-probe.md"
- "Make a separate copy"
- "Add one deliberate error"
- "Run the same checker"
- "Expected result: the checker rejects the copy"
- "A rejection shows the check catches this error"
- "It does not show the original is correct"

LAYOUT AND RELATIONSHIPS:
Two columns separated by a full-height vertical rule, with no connector crossing it. Left column headed 'Original: artifact.md', three boxes top to bottom with downward 'then' arrows: 'Keep the original unchanged' → 'Record its hash' → 'Later, confirm the hash is unchanged'. Right column headed 'Test copy: falsifier-probe.md', four boxes top to bottom with downward arrows: 'Make a separate copy' → 'Add one deliberate error' → 'Run the same checker' → 'Expected result: the checker rejects the copy'. A two-line plain-sentence footer spans both columns below the rule: 'A rejection shows the check catches this error' / 'It does not show the original is correct'. No arrow from the rejection toward the left column or toward any 'correct' endpoint. No icons, gears or byte glyphs; show no hash value and no count.

REVISION REQUIREMENTS (a previous attempt was rejected; fix all of these):
- The two left-column arrows carry the word 'then' (beside the arrows at y≈388 and y≈608). 'then' is not a spec label, and the right column's identical 'then' arrows carry no label, so the two columns look inconsistent. The spec gives 'then' as the meaning of the arrows, not as visible text. Regenerate with no text on any arrow; leave the plain downward arrows in both columns. Keep every other label, the vertical rule and the two-line footer unchanged.

Before returning, check every text element is present, spelled exactly, and nothing else was added.
````

## m00-readiness-lanes

- Title: Check each tool separately
- Native size: 1536×1024; published SHA-256: `446f4d4f9e806beb162ab65de14aceb7af8798fa25508b80d6bdd8262f4eb1bb`
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

TITLE (top-left): "Check each tool separately"

TEXT ELEMENTS (each exactly once unless the layout says a token repeats; verbatim):
- "OMP prerequisites"
- "Read the prerequisite report in a new terminal"
- "Live OMP check"
- "A live call writes from-omp.txt"
- "Read the file from disk"
- "verify_tool_proof.py checks the file and its receipt"
- "Obsidian"
- "Check the files on disk"
- "Check the same changes in the app window"
- "n8n"
- "Check the running stack"
- "Check the workflow survives reload and restart"
- "A passing prerequisite report does not replace the live check"
- "A result for one tool does not clear another"

LAYOUT AND RELATIONSHIPS:
Four equal-width vertical lanes side by side, each with a heading at the top: 'OMP prerequisites', 'Live OMP check', 'Obsidian', 'n8n'. Lane 1: one box, 'Read the prerequisite report in a new terminal'. Lane 2: three boxes top to bottom joined by downward 'then' arrows: 'A live call writes from-omp.txt' → 'Read the file from disk' → 'verify_tool_proof.py checks the file and its receipt'. Lane 3: two boxes stacked with no arrow between them (both checks are required, neither replaces the other): 'Check the files on disk', 'Check the same changes in the app window'. Lane 4: two boxes stacked the same way: 'Check the running stack', 'Check the workflow survives reload and restart'. Thin vertical rules separate the lanes. No line crosses between lanes and no lane feeds a shared all-clear box. A plain two-line footer spans the width: 'A passing prerequisite report does not replace the live check' (placed under lanes 1–2) and 'A result for one tool does not clear another'. No red banner, no tail dots.

Before returning, check every text element is present, spelled exactly, and nothing else was added.
````

## m00-recovery-loop

- Title: Recover from a failed step
- Native size: 1536×1024; published SHA-256: `fab611f950c431908f7f8c613f4b1f55bb4e0fcb01476315cc8ab696c87df29d`
- Accepted replacement: 01 of 1, generated with Codex CLI 0.154.0 through its built-in `image_gen` tool.
- Reference image: the prior `m00-recovery-loop.png` at commit `c87f7d9`, SHA-256 `fc46cc117a748cabf0422e40d4b4c1057e722ce22ef4edf89931d011e467f999`.
- Review: all thirteen labels are present and correctly spelled. The Yes branch returns new evidence to the harness; the No branch records the result. The existing light course-figure style is retained.

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to generate exactly ONE PNG instructional flow diagram. Do not write code or SVG. Save the finished PNG as /tmp/aihb-m00-recovery.VPoavF/recovery-loop.png and return that absolute path. Do not edit repository sources. Do not run tests, builds, linters, or formatters.

This is a revision of the attached course diagram, not a new visual identity. Preserve the existing course figure's light, clean style. The subject is a learner using an AI harness to solve a setup error. Teach the work itself: no curriculum rationale, making-of commentary, grades, scores, or qualification claims.

VISUAL STYLE:
- 1536x1024 landscape, opaque warm off-white background #FAF7F0.
- Match the attached figure: white panels #FFFFFF, thin border #C9C1B0, small corner radius, deep ink text #2B2A27, muted ochre #9A7B3C arrows and key borders. No new style, scene, photographic effects, decorative icons, gradients, texture, glow, shadows, 3D, logos, or invented data.
- One clean sans-serif; sentence case; title 44px semibold at top-left; labels 26-30px, generous padding, aligned layout. Make every label legible.
- Render every label below exactly once, except that Yes and No label their respective decision edges. Do not invent, abbreviate, or add any labels.

TITLE:
"Recover from a failed step"

LABEL SET:
Main instruction panel:
"Ask the harness"
"Copy and paste the error"
"Describe what you were doing"
"Describe what you are trying to accomplish"
"Fix this issue."
Other flow nodes:
"Review and apply the fix"
"Run the same check again"
"Still failing?"
"Paste the new error and describe what you tried"
"Record the result"
Decision edges:
"Yes"
"No"

LAYOUT AND RELATIONSHIPS:
The dominant panel occupies the upper-left half. Its heading is Ask the harness; the next three lines are equally readable supporting instructions; Fix this issue. is the final emphasized line inside that same panel. Do not draw arrows between the lines: they are parts of one request, not separate actions.
A single right-pointing arrow leaves this panel to Review and apply the fix in the upper-right. A down arrow leads to Run the same check again, then another down arrow to the diamond Still failing?. The Yes edge leaves the LEFT vertex of the diamond for a lower-left box reading Paste the new error and describe what you tried; a clear return arrow from that box goes back to the main Ask the harness panel. This is the learner returning with new evidence. The No edge leaves a DIFFERENT vertex for Record the result, at the lower-right, with no return arrow from success. Place Yes and No on their own distinct edges. Keep connectors outside boxes, uncrossed, and away from text. Use the available canvas evenly with generous margins.

Do not retain any old labels such as Change one thing, Use the recovery guidance, or Neither outcome starts an automatic retry. The revised diagram must visibly include the full error + action + goal + explicit fix request, not just generic troubleshooting advice.

Before returning, inspect all labels and arrows. Every stated label must appear, spelled exactly. The two decision edges must be unambiguous. Do not report an image as completed without actually generating it.
````

## m00-responsibility-screen

- Title: Screen the job before you delegate it
- Native size: 1536×1024; published SHA-256: `e9983055f034c1edcbef4c934c2bb6c4d1caefa55108b998c0ed5a9555de54d4`
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

TITLE (top-left): "Screen the job before you delegate it"

TEXT ELEMENTS (each exactly once unless the layout says a token repeats; verbatim):
- "Source and data authority"
- "Who decides whether this email goes out"
- "Both resolved?"
- "Yes"
- "No"
- "Draft the email"
- "HOLD"
- "Resolve it before drafting"
- "Also answer from what you inspected"
- "Sensitive data present"
- "Affected audience or person"
- "Disclosure needed"
- "Consequential action this draft cannot authorize"

LAYOUT AND RELATIONSHIPS:
Left: two stacked gate boxes, 'Source and data authority' above 'Who decides whether this email goes out'. Each has an arrow into one decision diamond 'Both resolved?' to their right. The 'Yes' edge goes right to an olive-outlined box 'Draft the email'. The 'No' edge goes down to a red HOLD token, then by arrow to 'Resolve it before drafting'. No arrow leads from that box back to drafting. Right side: a plain bordered panel headed 'Also answer from what you inspected', listing four lines (Sensitive data present; Affected audience or person; Disclosure needed; Consequential action this draft cannot authorize). The panel has no arrows to or from the gates or the outcomes: these questions are answers to record, not permissions. Flat fills, no halo, title centred.

Before returning, check every text element is present, spelled exactly, and nothing else was added.
````

## m00-tool-layers

- Title: What each layer of the tool shows
- Native size: 1536×1024; published SHA-256: `e17c92f9c131167a1c787858a62ef33666712f5b353e8b420f50f4873448b17e`
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

TITLE (top-left): "What each layer of the tool shows"

TEXT ELEMENTS (each exactly once unless the layout says a token repeats; verbatim):
- "Layer"
- "What it gives you as evidence"
- "Model"
- "Text it generated"
- "Interface"
- "File written to disk"
- "Harness"
- "Enforced permissions and run receipts"
- "Person"
- "Interpretation and the decision to use the result"
- "Generated text is not a verified fact"
- "A receipt shows what ran, not that the result is right"
- "Record one observed capability"
- "Record one observed limit"

LAYOUT AND RELATIONSHIPS:
Two-column table, four equal-height rows read top to bottom, with column headers 'Layer' and 'What it gives you as evidence'. Rows: Model | Text it generated; Interface | File written to disk; Harness | Enforced permissions and run receipts; Person | Interpretation and the decision to use the result. No arrows between rows, so no row passes its result to the next. Two small italic notes sit in the right margin at row boundaries, each with a short tick to its boundary: 'Generated text is not a verified fact' on the Model/Interface boundary; 'A receipt shows what ran, not that the result is right' on the Harness/Person boundary. Below the table, one neutral bracket spans all four rows and splits into two equal side-by-side outcome boxes: 'Record one observed capability' and 'Record one observed limit'. Meaning: evidence from any row can support either record. Draw no stub above the first row and no joint dots.

Before returning, check every text element is present, spelled exactly, and nothing else was added.
````

