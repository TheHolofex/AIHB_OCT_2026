# Figure prompts and provenance — module-10-capstone

Staff-only record. Not published (absent from `course.json`).

- Generator: `codex-cli 0.154.0` (`codex exec`, built-in `image_gen`). No reference images attached.
- Style: flat light instructional diagram (warm off-white ground, white boxes, thin neutral borders, one ochre accent, muted red only for stop/HOLD, muted green only for allowed). Sentence-case titles and plain-language labels.
- Post-processing: composited onto the opaque `#FAF7F0` ground and saved as lossless RGB PNG at native size; no other pixel changes.
- Run evidence (all attempts, prompts, logs): `~/course-evidence/image-remake-20261003T204449`
- These figures replace an earlier set that used dark, glowing styling and slogan-style labels.

## m10-evidence-boundaries

- Title: What each check supports
- Native size: 1536×1024; published SHA-256: `196a278794e2c3ca812b02c4d7b5aac4271663d1962785b9ef555f76ddb733e2`
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

TITLE (top-left): "What each check supports"

TEXT ELEMENTS (each exactly once unless the layout says a token repeats; verbatim):
- "Evidence"
- "Supports"
- "Size and digest"
- "Identity of the weight file"
- "Health probe"
- "Service reachable at the time of the probe"
- "Live transcript"
- "One recorded interaction"
- "Structure check"
- "Named fields and local paths present"
- "None of these checks establishes:"
- "Safety, model quality, production readiness or independent transfer"

LAYOUT AND RELATIONSHIPS:
A two-column table with the headers 'Evidence' and 'Supports'. Four equal rows, unnumbered and unranked: Size and digest / Identity of the weight file; Health probe / Service reachable at the time of the probe; Live transcript / One recorded interaction; Structure check / Named fields and local paths present. Use a plain thin arrow or just a column rule between the cells; no icons, or one minimal flat glyph per evidence cell. Below the table, separated by a rule, a single footer box with a thin red outline: the heading 'None of these checks establishes:' over the line 'Safety, model quality, production readiness or independent transfer'. No arrow or line from any row reaches the footer. No checkmarks or PASS stamps.

Before returning, check every text element is present, spelled exactly, and nothing else was added.
````

## m10-independent-transfer

- Title: Three kinds of transfer evidence
- Native size: 1536×1024; published SHA-256: `1d3f2dbfb67ec4cee206690c147acdef3c15a6533ab9e175e33d9f204589640b`
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

TITLE (top-left): "Three kinds of transfer evidence"

TEXT ELEMENTS (each exactly once unless the layout says a token repeats; verbatim):
- "Your own rerun"
- "Fresh-session technical replay, including an agent replay"
- "Technical evidence only; neither counts as another person operating the kit"
- "Another person"
- "Runs the kit from the package alone"
- "Records: questions, commands, observed outcomes"
- "Any help you gave is recorded"
- "An assisted attempt stays labelled assisted, not independent"
- "No recipient available"
- "Record independent operation as unobserved, with the missing prerequisite"

LAYOUT AND RELATIONSHIPS:
Three stacked horizontal lanes in separate bordered panels with gaps between them. Lane 1 (short): 'Your own rerun'. Lane 2 (short): 'Fresh-session technical replay, including an agent replay'. A single bracket on the right spans lanes 1 and 2 with the note 'Technical evidence only; neither counts as another person operating the kit'. No line runs from lanes 1 or 2 into lane 3. Lane 3, outlined more heavily, read left to right: 'Another person' (a text label only, no avatar or silhouette) → 'Runs the kit from the package alone' → 'Records: questions, commands, observed outcomes' → 'Any help you gave is recorded' → 'An assisted attempt stays labelled assisted, not independent'. A side branch drops from 'Another person' at the start of lane 3 to the condition box 'No recipient available', then an arrow to 'Record independent operation as unobserved, with the missing prerequisite'. Neutral palette; no checkmarks or success marks.

REVISION REQUIREMENTS (a previous attempt was rejected; fix all of these):
- An unlabelled arrow drops from the 'Another person' box to 'No recipient available'. Read as a flow, this says 'another person → no recipient available', which contradicts itself. The no-recipient case is the alternative to having another person, not a step after it. The spec asked for this and the problem slipped through. Fix for full regeneration: start lane 3 with a short entry stub at its left edge that splits into two paths. Upper path: 'Another person' → 'Runs the kit from the package alone' → 'Records: questions, commands, observed outcomes' → 'Any help you gave is recorded' → 'An assisted attempt stays labelled assisted, not independent'. Lower path: 'No recipient available' → 'Record independent operation as unobserved, with the missing prerequisite'. Draw no line from the 'Another person' box to the lower path. Keep lanes 1–2, the bracket note and all labels unchanged.

Before returning, check every text element is present, spelled exactly, and nothing else was added.
````

## m10-launch-approval

- Title: You approve and start the launch
- Native size: 1536×1024; published SHA-256: `6ad21637cb16f1214d835e184c020757518db2a7972e3b33a8727b884884ecbc`
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

TITLE (top-left): "You approve and start the launch"

TEXT ELEMENTS (each exactly once unless the layout says a token repeats; verbatim):
- "Checked weight file"
- "Loopback configuration"
- "OMP drafts the launch line"
- "Your check: 127.0.0.1, context 32768, nothing that widens the boundary"
- "Wrong: reject the line and ask OMP for a new draft"
- "Passes: you start the server"
- "Health probe: is the service reachable?"
- "Unreachable: HOLD"
- "A drafted line is not a running service"

LAYOUT AND RELATIONSHIPS:
Row 1, read left to right: two input boxes stacked, 'Checked weight file' and 'Loopback configuration', each with an arrow into 'OMP drafts the launch line' (grey outline, marked as OMP's step). An arrow goes to a decision box, 'Your check: 127.0.0.1, context 32768, nothing that widens the boundary', with a solid outline marked as the operator's step. From the check, the 'Wrong' exit drops to a red-outlined box 'Wrong: reject the line and ask OMP for a new draft'. A short dashed return arrow goes from that box straight back to 'OMP drafts the launch line', a direct short return with no wraparound; nothing from this box reaches the server. Row 2: the 'Passes' exit drops to 'Passes: you start the server' (operator's step). After a visible gap, an arrow to a separate box 'Health probe: is the service reachable?', then a red-outlined exit 'Unreachable: HOLD'. A footnote under row 1, attached to the draft box by a thin line: 'A drafted line is not a running service'. Monospace for 127.0.0.1 and 32768. No terminal window, command text or PASS readout.

Before returning, check every text element is present, spelled exactly, and nothing else was added.
````

## m10-operator-boundary

- Title: What the local boundary does and does not limit
- Native size: 1536×1024; published SHA-256: `730d77514354a0e9d8a2fc0898e6485692e8743a74f3b0bfc641f8939f79a0f4`
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

TITLE (top-left): "What the local boundary does and does not limit"

TEXT ELEMENTS (each exactly once unless the layout says a token repeats; verbatim):
- "Service bound to 127.0.0.1 only"
- "One operator"
- "Local weights"
- "Requests and replies"
- "Prompts and replies are recorded"
- "Operator reviews output before any use"
- "Blocked at the boundary: no shared endpoint, no traffic from other people"
- "Identity check confirms the weight file only, not its safety or accuracy"

LAYOUT AND RELATIONSHIPS:
Centre-left: a rectangle outlined as the service boundary, labelled 'Service bound to 127.0.0.1 only' (127.0.0.1 in monospace). Inside it are two boxes, 'One operator' and 'Local weights', joined by a two-way arrow labelled 'Requests and replies'. Along the inner bottom edge is a strip 'Prompts and replies are recorded', with nothing crossing it. One arrow leaves the boundary on the right to a box outside it: 'Operator reviews output before any use'. There is no arrow from that box onward and no arrow anywhere toward publishing or other people. On the boundary's outer edge (top or right) is a short red barred segment with the list 'Blocked at the boundary: no shared endpoint, no traffic from other people', written as an edge annotation, not as destinations. A small separate grey callout, 'Identity check confirms the weight file only, not its safety or accuracy', attaches by one thin line to 'Local weights'. It does not cross the recording strip and does not enclose the boundary. No shield, lock, port number or model name.

Before returning, check every text element is present, spelled exactly, and nothing else was added.
````

## m10-package-boundary

- Title: What travels in the kit
- Native size: 1536×1024; published SHA-256: `e68fe5c4b19e127a28f66894893a877aff577fe9282db26ec68b0740864e00f2`
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

TITLE (top-left): "What travels in the kit"

TEXT ELEMENTS (each exactly once unless the layout says a token repeats; verbatim):
- "Declared kit"
- "shared/PACKAGE.md (instructions)"
- "scripts/ (adapters)"
- "shared/case/ (case and rules)"
- "shared/controls/ (active control)"
- "shared/baseline/ (baseline)"
- "Freeze the declared paths"
- "Digest-checked copy"
- "Fresh received folder"
- "Not in the kit"
- "Model weights: the recipient downloads them separately"
- "Run evidence, including the stop receipt: kept separately"
- "Conversation history"

LAYOUT AND RELATIONSHIPS:
Top row, read left to right. A box headed 'Declared kit' lists five monospace path rows, each with its role in plain text: 'shared/PACKAGE.md (instructions)', 'scripts/ (adapters)', 'shared/case/ (case and rules)', 'shared/controls/ (active control)', 'shared/baseline/ (baseline)'. A single arrow goes to the step box 'Freeze the declared paths', then an arrow to 'Digest-checked copy', then an arrow into the box 'Fresh received folder'. That box shows five short unlabelled rows standing for the same five members. Below the top row, separated by a gap, one panel headed 'Not in the kit' lists three parallel lines: 'Model weights: the recipient downloads them separately', 'Run evidence, including the stop receipt: kept separately', 'Conversation history'. No line connects this panel to the copy path or the received folder. Flat strokes; no file counts, sizes, digests or model names.

Before returning, check every text element is present, spelled exactly, and nothing else was added.
````

## m10-stop-restore

- Title: Service stop and control restore are separate
- Native size: 1536×1024; published SHA-256: `42fe48941a39278b97e507affd249348b52554b7404ec2fceb37bd761b29950a`
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

TITLE (top-left): "Service stop and control restore are separate"

TEXT ELEMENTS (each exactly once unless the layout says a token repeats; verbatim):
- "Stop (previous step)"
- "Operator stops the process (Ctrl+C)"
- "Probe reports unreachable"
- "Stop receipt"
- "Adapter verifies the stopped state"
- "Control"
- "Control disabled"
- "Every adapter command returns HOLD: control disabled"
- "This refusal is not evidence that the service stopped"
- "Validate the baseline digest"
- "Restore the control from the baseline"
- "Restoring the control does not restart the service"
- "To claim it is running again: launch it, then probe"

LAYOUT AND RELATIONSHIPS:
Two horizontal swimlanes in separate bordered panels with a clear gap between them; no line crosses between the lanes. Top lane, header 'Stop (previous step)', left to right with arrows: 'Operator stops the process (Ctrl+C)' (tagged as the operator's step) → 'Probe reports unreachable' → 'Stop receipt' → 'Adapter verifies the stopped state' (tagged as the adapter's check; no power or kill icon). Bottom lane, header 'Control', with two sub-sequences separated by a gap. First: 'Control disabled' → a red-outlined box 'Every adapter command returns HOLD: control disabled', which is a dead end, with the small note 'This refusal is not evidence that the service stopped' directly beneath it. Second: 'Validate the baseline digest' → 'Restore the control from the baseline' → a terminal note box 'Restoring the control does not restart the service'. A separate grey box beside that terminal note, with no incoming arrow, reads 'To claim it is running again: launch it, then probe'. No decorative bars, people, hands or shields.

Before returning, check every text element is present, spelled exactly, and nothing else was added.
````

