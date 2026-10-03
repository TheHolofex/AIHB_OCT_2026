# Raster figure prompts and provenance — module-03-mcp-research

Staff-only record. Not published (absent from `course.json`).

- Generator: `codex-cli 0.154.0` (`codex exec`, ChatGPT login, built-in `image_gen`).
- Style references attached to every invocation: `ui/images/home-hero.webp` and `ui/images/home-band-custody.webp`, decoded losslessly to PNG with `dwebp`; every figure except `m00-bounded-direction` also received the accepted `m00-bounded-direction` attempt-01 raster as a style-only reference. Label edits additionally attached the image being edited as the first input.
- Post-processing: the generator returns RGBA with a transparent ground. Each accepted raster was alpha-composited onto the specified `#0D0906` ground and saved as opaque lossless RGB PNG at native size. No other pixel changes, no resizing.
- Run evidence (all attempts, logs, rejected rasters, reviews): `~/course-evidence/course-raster-visuals/20261002T233502`
- Module source contract: `module-03-mcp-research/shared/MODULE_03_LAB.md`, `shared/mcp/authority_probe.py`, `shared/mcp/vault_mcp.py`, and `shared/vault/Handbook/Handling rules.md`. The exact stretch flag is `--ignore-allow-list`. A server cannot audit a call never sent to it. Handling is exercise-specific, not a real classification system.
- Owning page digests at integration (SHA-256): `shared/MODULE_03_LAB.md` 32f472ca7c93cedb…

## m03-aggregation

- Title: `THE COMBINATION CHANGES THE LIMIT`
- Publication path: `shared/figures/m03-aggregation.png`
- Anchor: Lab `## Check the AI's handling calls against the rules`; replace `m03-aggregation.svg`.
- Caption: One product containing at least three movement-element types is STAFF at minimum, even when its sources are individually OPEN or PARTNER.
- Native size: 1536×1024; published SHA-256: `58edeb0c1855b9e9c3692e45c372e9a8d4d5dd22b45f6194b267e0e3669647d1`
- Iteration history:
  - attempt-01: full generation; session `01a10051-1e72-7931-93d6-dc5856699776`; raw SHA-256 `5626ceebdc8b68e5…`; superseded — review: Remove added periods and cold blue/purple glyphs (m03-aggregation)
  - attempt-02: full generation; session `01a1007e-23f6-71e2-b407-17989f187bd5`; raw SHA-256 `4ef76354dfb1197b…`; ACCEPTED
- Final review outcome: accepted attempt-02. F03: m03-aggregation: ACCEPT_A2 — the eight labels are verbatim with no periods. Three chips feed one product boundary, \"At least 3 of 4\" sits inside it and leads to STAFF minimum, and the separate files below are not aggregated. The palette is all gold; A1 has periods and cold blue/mauve glyphs.

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.
[Block 1: tool/output instruction]

2. Lesson contract
Module 03 — Kiln Hold; shared/MODULE_03_LAB.md; H2 “Check the AI's handling calls against the rules”. Caption / learning takeaway: “One product containing at least three movement-element types is STAFF at minimum, even when its sources are individually OPEN or PARTNER.” Intended transfer action: Count distinct movement-element types inside one product before deciding whether its handling floor rises. Misconception to prevent: Three separate shareable notes automatically aggregate without being combined into one product. The lesson prose here is NOT in-image text.

3. Composition
Diagram-first containment and threshold diagram. Native 1536×1024 landscape raster PNG; 64 px safe margin, top title zone, remaining canvas for the mechanism; prefer two rows to tiny copy. Reading order and zones: Four source-category chips form a small pool on the left, without actual case values. A selection of ANY THREE DIFFERENT categories crosses into a SINGLE prominent product boundary at center. Only inside that combined boundary is the at-least-three-of-four threshold evaluated; outgoing constrained result at right is STAFF minimum. An alternate separate-parts lane remains outside the product and must not point to the STAFF outcome. No multiple-product aggregation. Focal relationship: three distinct types within ONE product → STAFF floor Arrows mean only their described relationships, NEVER approval. No decorative connectors, no slide-overlay reserve.

4. Verbatim label map
Title zone: THE COMBINATION CHANGES THE LIMIT.
Four category chips: Location grid | Time + zone letter | Named route | Quantity or lot. Central enclosing boundary: One product | At least 3 of 4. Right result: STAFF minimum. Bottom contrast: Shareable parts ≠ shareable combination.
Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Duplicate a label only where its specified branches require it. Yes and No are allowed solely on edges leaving a question ending in ? with both destinations specified; there are no question nodes here. Structural numbers only where specified numbered steps/rows (none here). The mapping text, zone names and directions are instructions, NOT visible words.

5. Visual family
#0D0906 primary ground; #17110C panel fill; #A58650 primary gold; #C8A96A sheen and connector highlights; #C8B78A secondary readable text; #FFF8E7 primary text; #655337 subdued nonessential rules; #3A2E1B faint structural lines; #4F5634 restrained verified/allowed accents; #B43A2F warnings/blocked branches; #2D3030 neutral mechanisms. Olive and brick red are fills/strokes/pills ONLY; text off-white or sandstone with high contrast; every status has a text label plus color. No bright green/blue/cyan/teal/purple. No Starzl product names or product-specific color identities. The site references supply the warm earth lineage, not photographic composition or subject matter.

6. Richness and legibility
Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots ONLY on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Clean Inter/Helvetica-like sans-serif; exact filenames/tokens in clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density; wrap inside generous cells rather than shrinking type.

7. Honesty/exclusions
No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs only if they explain containment/transformation. This is an exercise-specific vault/MCP mechanism, not an operating-system sandbox or real classification system. Do not use actual grid/time/route/quantity/lot identifiers; three separate files do not themselves constitute a single aggregated product.

8. Generation self-check
Before returning the PNG, ensure this precise relationship reads immediately: At least three distinct kinds INSIDE a single product impose STAFF minimum even if individual sources are OPEN or PARTNER. Reject if source coexistence alone triggers the floor or any of the four chips, threshold, and product boundary is absent. This is a generation check, not a claim that the image has been externally reviewed.


## 9. Revision requirements from review of the previous attempt
A previous generation of this figure was rejected. Generate a NEW image from this full contract and fix every defect below. All earlier blocks still govern; labels stay verbatim; add no words. Title text sits directly on the dark ground with no white bloom/haze band.

- Remove added periods and cold blue/purple glyphs (m03-aggregation)
Transcription: "THE COMBINATION CHANGES THE LIMIT."; chips "Location grid" (green circle), "Time + zone letter" (gold triangle), "Named route" (blue diamond), "Quantity or lot" (mauve square); three chips feed a box "One product" holding three document glyphs and "At least 3 of 4" → "STAFF minimum"; unlabeled lower lane of three separate documents with no arrow; footer "Shareable parts ≠ shareable combination.". The structure matches H5: a single product is the trigger, and the separate parts do not point to STAFF. Defects: (1) Periods were added to the title and the footer. (2) The prompt's visual family (§5) bans blue and purple, but the Named route diamond is steel blue and the Quantity or lot square is mauve; they are the only cold hues on the canvas. Verdict: LABEL_EDIT plus glyph recolor, with no structural change. Remove the period from the title and from "Shareable parts ≠ shareable combination". Recolor the diamond to #C8A96A sandstone-gold and the square to #B43A2F-tinted brick or #655337 umber, everywhere each glyph appears: chip, product box and lower lane.


## 10. Global rendering corrections (apply to this image)
- Background is flat-to-subtle #0D0906 near-black with at most a faint warm vignette. NO white, grey, cream or yellow bloom/glow/haze anywhere, especially not behind the title; title text is solid #FFF8E7 on dark ground, at least 64 px from the top edge, with only a thin warm sheen.
- Do not add trailing periods or any punctuation not in the label map.
- No people, silhouettes, hands, phones, gears, shields, medals, check-mark badges, browser windows or other decorative pictograms. Nodes are text-first; generic document glyphs only where they explain containment.
- Every essential label at least 32 px in #FFF8E7 or #C8B78A; never dim tan small text.
- Olive (#4F5634) only for allowed/verified states; brick red (#B43A2F) only for blocked/HOLD/warning; neutral routes use #2D3030 with gold stroke.
````

## m03-authority-layers

- Title: `LIMIT THE CALL AT EACH BOUNDARY`
- Publication path: `shared/figures/m03-authority-layers.png`
- Anchor: Lab `## Declare what the connection may do, then prove the limits`; replace `m03-mcp-layers.svg`.
- Caption: Use separate tool, guard, and server limits, then inspect the evidence from the layer actually exercised; the server cannot log a call it never received.
- Native size: 1536×1024; published SHA-256: `0c06fc09890d51a413f9af39e1b4283cdfce899ed8e74e81edb15b0b356fe4a2`
- Iteration history:
  - attempt-01: full generation; session `01a10052-0538-7d33-9564-a6a84f6c5f87`; raw SHA-256 `2967d91effcc24fb…`; superseded — review: Fold Read-only / create-only into the server boundary (m03-authority-layers)
  - attempt-02: full generation; session `01a1007c-1d61-71e3-b35e-fd9c6d6da751`; raw SHA-256 `bf5f92b3f7d1cb82…`; superseded
  - attempt-03: edit; session `01a10089-4d7f-77c1-9ffc-439fcd491aec`; raw SHA-256 `d9013462f13afc5b…`; ACCEPTED
- Final review outcome: accepted attempt-03. Final1: m03-authority-layers: ACCEPT_A3 — the Files on disk → Server audit + disk effects arrow is now gold. The three red stop exits and every label are unchanged (LIMIT THE CALL AT EACH BOUNDARY; Tool offer / allow-list; Guard; Server scope / Read-only / create-only; Files on disk; Not sent; Blocked before server; Server denial; Harness / probe record ×2; Server audit + disk effects ×2), and the title has no period.

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to EDIT the first attached image and save exactly ONE corrected PNG with an OPAQUE #0D0906 background (no transparency). Do not use a CLI image fallback or write code/SVG. The other attachments are STYLE references only. Return the absolute saved PNG path and no claim of verification.

CORRECTIONS (apply exactly; preserve every other relationship, label, position and color):
m03-authority-layers: LABEL_EDIT_A2 — recolor the Files-on-disk evidence arrow to gold
A2 is structurally correct and matches PLAN.md item 2. Read in order: Tool offer / allow-list → Guard → Server scope, with Read-only / create-only folded into the Server scope cell, → Files on disk. Each boundary has its own red exit: Not sent, Blocked before server, Server denial. Evidence sits under the layer that was exercised: Harness / probe record twice, under the first two exits, and Server audit + disk effects twice, under Server denial and under Files on disk. The title has no period. One defect remains: the vertical arrow in the far-right column, from the olive "Files on disk" box down to "Server audit + disk effects" (x≈1335, y≈415–720), is drawn in brick red #B43A2F, the same as the three stop-exit arrows. The contract (§10) reserves brick red for blocked or warning branches and puts neutral or allowed routes in gold. A red arrow here makes the allowed path read as a fourth refusal branch. Fix with an image edit of attempt-02/flattened.png: change only that right-column vertical arrow, shaft and arrowhead, to gold #A58650 with a #C8A96A highlight, matching the gold horizontal arrows in the top row. Keep all text, boxes, the three red exit arrows, and the red arrows below the exits unchanged.

The original full generation contract follows and still governs labels and composition:

$imagegen
Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.
[Block 1: tool/output instruction]

2. Lesson contract
Module 03 — Kiln Hold; shared/MODULE_03_LAB.md; H2 “Declare what the connection may do, then prove the limits”. Caption / learning takeaway: “Tool offer, guard, and server boundaries stop different calls; inspect evidence from the boundary actually reached.” Intended transfer action: Determine where a forbidden request stopped and seek evidence from that boundary instead of claiming the server saw it. Misconception to prevent: A server audit must contain every attempted tool request, even one blocked upstream. The lesson prose here is NOT in-image text.

3. Composition
Diagram-first layered conditional flow. Native 1536×1024 landscape raster PNG; 64 px safe margin, top title zone, remaining canvas for the mechanism; prefer two rows to tiny copy. Reading order and zones: Three left-to-right boundaries along a REQUEST path: tool offer / allow-list, guard, server scope; only allowed requests reach files on disk. At the first boundary branch to Not sent and Harness / probe record; at guard branch to Blocked before server and Harness / probe record; at server branch to Server denial and Server audit + disk effects. After server scope, successful permitted request continues through Read-only / create-only restriction to Files on disk, with Server audit + disk effects. Stops are separate exits, NEVER a single chain of refusals. No text label REQUEST in the image. Focal relationship: pre-server stop ≠ server audit Arrows mean only their described relationships, NEVER approval. No decorative connectors, no slide-overlay reserve.

4. Verbatim label map
Title zone: LIMIT THE CALL AT EACH BOUNDARY.
First boundary: Tool offer / allow-list | Not sent. Second: Guard | Blocked before server. Third: Server scope | Server denial | Read-only / create-only. End: Files on disk. Evidence beneath pre-server exits: Harness / probe record. Evidence beneath server arrival and disk: Server audit + disk effects.
Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Duplicate a label only where its specified branches require it. Yes and No are allowed solely on edges leaving a question ending in ? with both destinations specified; there are no question nodes here. Structural numbers only where specified numbered steps/rows (none here). The mapping text, zone names and directions are instructions, NOT visible words.

5. Visual family
#0D0906 primary ground; #17110C panel fill; #A58650 primary gold; #C8A96A sheen and connector highlights; #C8B78A secondary readable text; #FFF8E7 primary text; #655337 subdued nonessential rules; #3A2E1B faint structural lines; #4F5634 restrained verified/allowed accents; #B43A2F warnings/blocked branches; #2D3030 neutral mechanisms. Olive and brick red are fills/strokes/pills ONLY; text off-white or sandstone with high contrast; every status has a text label plus color. No bright green/blue/cyan/teal/purple. No Starzl product names or product-specific color identities. The site references supply the warm earth lineage, not photographic composition or subject matter.

6. Richness and legibility
Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots ONLY on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Clean Inter/Helvetica-like sans-serif; exact filenames/tokens in clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density; wrap inside generous cells rather than shrinking type.

7. Honesty/exclusions
No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs only if they explain containment/transformation. This is an exercise-specific vault/MCP mechanism, not an operating-system sandbox or real classification system. Do not show server audit for a call not sent; server restrictions are application-level limits, not OS isolation.

8. Generation self-check
Before returning the PNG, ensure this precise relationship reads immediately: The server cannot audit an attempt stopped by the tool offer or guard; a call reaching the server can yield server denial and a server audit. Reject any missing stop or evidence label, or any arrow that sends a pre-server refusal through the server. This is a generation check, not a claim that the image has been externally reviewed.
````

## m03-contract-authority

- Title: `AN ANNOTATION IS A CLAIM`
- Publication path: `shared/figures/m03-contract-authority.png`
- Anchor: Lab `## Read the server's contract before you connect it`; replace `m03-contract-read.svg`.
- Caption: Inspect what the tool can change; a read-only annotation or a server's instructions do not enforce your authority boundary.
- Native size: 1536×1024; published SHA-256: `404bba322757ceca0e3d58729e123d2966d0654dc93697554a8e28c0e8e844ca`
- Iteration history:
  - attempt-01: full generation; session `01a10052-ea75-74f0-b37f-b2e0c2ab036a`; raw SHA-256 `d20549c89f4ba49a…`; superseded — review: Strip added periods from labels (m03-contract-authority)
  - attempt-02: full generation; session `01a1007e-2298-7d73-a696-059e461cbb50`; raw SHA-256 `6ce094f69e51b17a…`; ACCEPTED
- Final review outcome: accepted attempt-02. F03: m03-contract-authority: ACCEPT_A2 — the seven labels are verbatim with no periods. manage_tags/Claim: read-only ≠ Effect: adds or removes tags; Inspect tool descriptions spans both panels; Server instructions → Model steering only, with no permission node; no pictograms. A1 has periods plus gear/brain/document pictograms.

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.
[Block 1: tool/output instruction]

2. Lesson contract
Module 03 — Kiln Hold; shared/MODULE_03_LAB.md; H2 “Read the server's contract before you connect it”. Caption / learning takeaway: “A tool's read-only mark and server instructions are claims to check, not facts that enforce authority.” Intended transfer action: Inspect actual effects and decide whether a tool description or annotation can be trusted before connecting it. Misconception to prevent: A read-only annotation or server instructions enforce permission. The lesson prose here is NOT in-image text.

3. Composition
Diagram-first contrast. Native 1536×1024 landscape raster PNG; 64 px safe margin, top title zone, remaining canvas for the mechanism; prefer two rows to tiny copy. Reading order and zones: Two opposed central panels compare an annotation to a described effect: manage_tags marked read-only but adds/removes tags. An independent lower rail sends server instructions toward model steering, NOT authorization. Place inspection across the contradiction; never connect instructions to permission. Focal relationship: annotation ≠ mutating effect; instructions ≠ permission Arrows mean only their described relationships, NEVER approval. No decorative connectors, no slide-overlay reserve.

4. Verbatim label map
Title zone: AN ANNOTATION IS A CLAIM.
Left claimed annotation: manage_tags | Claim: read-only. Right actual effect: Effect: adds or removes tags. Lower separate rail: Server instructions | Model steering. Central comparison and footer: Inspect tool descriptions | Claim ≠ enforcement.
Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Duplicate a label only where its specified branches require it. Yes and No are allowed solely on edges leaving a question ending in ? with both destinations specified; there are no question nodes here. Structural numbers only where specified numbered steps/rows (none here). The mapping text, zone names and directions are instructions, NOT visible words.

5. Visual family
#0D0906 primary ground; #17110C panel fill; #A58650 primary gold; #C8A96A sheen and connector highlights; #C8B78A secondary readable text; #FFF8E7 primary text; #655337 subdued nonessential rules; #3A2E1B faint structural lines; #4F5634 restrained verified/allowed accents; #B43A2F warnings/blocked branches; #2D3030 neutral mechanisms. Olive and brick red are fills/strokes/pills ONLY; text off-white or sandstone with high contrast; every status has a text label plus color. No bright green/blue/cyan/teal/purple. No Starzl product names or product-specific color identities. The site references supply the warm earth lineage, not photographic composition or subject matter.

6. Richness and legibility
Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots ONLY on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Clean Inter/Helvetica-like sans-serif; exact filenames/tokens in clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density; wrap inside generous cells rather than shrinking type.

7. Honesty/exclusions
No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs only if they explain containment/transformation. This is an exercise-specific vault/MCP mechanism, not an operating-system sandbox or real classification system. Do not suggest all uses of manage_tags are read-only: add/remove mutate the note header.

8. Generation self-check
Before returning the PNG, ensure this precise relationship reads immediately: The manage_tags claim contradicts its mutating effect; server instructions steer the model but cannot grant permission. Reject if any of seven labels is missing, or if an instructions arrow becomes authorization. This is a generation check, not a claim that the image has been externally reviewed.


## 9. Revision requirements from review of the previous attempt
A previous generation of this figure was rejected. Generate a NEW image from this full contract and fix every defect below. All earlier blocks still govern; labels stay verbatim; add no words. Title text sits directly on the dark ground with no white bloom/haze band.

- Strip added periods from labels (m03-contract-authority)
Transcription: "AN ANNOTATION IS A CLAIM."; left panel "manage_tags" (monospace) / "Claim: read-only."; red ≠ disc; right panel "Effect: adds or removes tags."; band "Inspect tool descriptions"; rail "Server instructions" → "Model steering"; footer "Claim ≠ enforcement.". The relationships are correct. vault_mcp.py:243-245 gives manage_tags readOnlyHint True with a description that adds and removes tags. The instructions arrow ends at model steering and connects to no permission node. Defect: four strings carry trailing periods that the label map does not have; the periods come from the prompt's sentence punctuation. They are the title, "Claim: read-only.", "Effect: adds or removes tags." and "Claim ≠ enforcement.". The pilot title has no period. Verdict: LABEL_EDIT. Change the title to "AN ANNOTATION IS A CLAIM", the left panel to "Claim: read-only", the right panel to "Effect: adds or removes tags", and the footer to "Claim ≠ enforcement". Change nothing else.


## 10. Global rendering corrections (apply to this image)
- Background is flat-to-subtle #0D0906 near-black with at most a faint warm vignette. NO white, grey, cream or yellow bloom/glow/haze anywhere, especially not behind the title; title text is solid #FFF8E7 on dark ground, at least 64 px from the top edge, with only a thin warm sheen.
- Do not add trailing periods or any punctuation not in the label map.
- No people, silhouettes, hands, phones, gears, shields, medals, check-mark badges, browser windows or other decorative pictograms. Nodes are text-first; generic document glyphs only where they explain containment.
- Every essential label at least 32 px in #FFF8E7 or #C8B78A; never dim tan small text.
- Olive (#4F5634) only for allowed/verified states; brick red (#B43A2F) only for blocked/HOLD/warning; neutral routes use #2D3030 with gold stroke.
````

## m03-effective-handling

- Title: `DERIVE THE EFFECTIVE HANDLING`
- Publication path: `shared/figures/m03-effective-handling.png`
- Anchor: Lab `## Judge six notes yourself before the AI works`; replace `m03-handling-ladder.svg`.
- Caption: Apply header, valid notice, inheritance, and aggregation in order; a body claim or a proposed marking does not grant release authority.
- Native size: 1536×1024; published SHA-256: `d57cf5ecfdeac719bf4f33766d0228a5438e8eb733eb31ac9873746b77f8654b`
- Iteration history:
  - attempt-01: full generation; session `01a10053-d97f-7912-86fe-64632af760d9`; raw SHA-256 `685be098aef34f4b…`; superseded — review: Regenerate on dark ground; title washed out (m03-effective-handling)
  - attempt-02: full generation; session `01a1007d-25ec-74d1-a605-5ae630d0c77c`; raw SHA-256 `7cca47b0efff69f6…`; ACCEPTED
- Final review outcome: accepted attempt-02. F03: m03-effective-handling: ACCEPT_A2 — the nine labels are verbatim with no periods. The order is header/Missing → STAFF, then latest valid Release Authority notice by zulu, then inheritance/most restricted wins, then 3 of 4 → STAFF minimum. This matches H1–H5 and lab line 301. The separate rail is New AI notes start STAFF | Proposal ≠ release.

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.
[Block 1: tool/output instruction]

2. Lesson contract
Module 03 — Kiln Hold; shared/MODULE_03_LAB.md; H2 “Judge six notes yourself before the AI works”. Caption / learning takeaway: “Apply header, valid notice, inheritance, and aggregation in order; a body claim or a proposed marking does not grant release authority.” Intended transfer action: Apply exercise handling rules in order, checking the authority and effective handling of each input before sharing a derived note. Misconception to prevent: A body claim, invalid notice, or AI proposal changes a release marking. The lesson prose here is NOT in-image text.

3. Composition
Diagram-first ordered rule flow with separate authority rail. Native 1536×1024 landscape raster PNG; 64 px safe margin, top title zone, remaining canvas for the mechanism; prefer two rows to tiny copy. Reading order and zones: Four ordered wide steps in a two-row serpentine flow, with clear 1→2→3→4 connectors: header/default → latest valid notice → most restricted effective source → one-product aggregation floor. Run a separate authority rail under the steps: Release Authority alone can change markings/release; Proposal ≠ release. Do not turn the authority rail into an automatic fifth step or imply notices always exist. Focal relationship: ordered effective-handling derivation ≠ authority to release Arrows mean only their described relationships, NEVER approval. No decorative connectors, no slide-overlay reserve.

4. Verbatim label map
Title zone: DERIVE THE EFFECTIVE HANDLING.
Step 1: Header marking | Missing → STAFF. Step 2: Latest valid notice by zulu | Release Authority. Step 3: Inherit effective source levels | Most restricted wins. Step 4: 3 of 4 elements → STAFF minimum. Separate new-note/authority rail: New AI notes start STAFF | Proposal ≠ release.
Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Duplicate a label only where its specified branches require it. Yes and No are allowed solely on edges leaving a question ending in ? with both destinations specified; there are no question nodes here. Structural numbers only where specified numbered steps/rows (none here). The mapping text, zone names and directions are instructions, NOT visible words.

5. Visual family
#0D0906 primary ground; #17110C panel fill; #A58650 primary gold; #C8A96A sheen and connector highlights; #C8B78A secondary readable text; #FFF8E7 primary text; #655337 subdued nonessential rules; #3A2E1B faint structural lines; #4F5634 restrained verified/allowed accents; #B43A2F warnings/blocked branches; #2D3030 neutral mechanisms. Olive and brick red are fills/strokes/pills ONLY; text off-white or sandstone with high contrast; every status has a text label plus color. No bright green/blue/cyan/teal/purple. No Starzl product names or product-specific color identities. The site references supply the warm earth lineage, not photographic composition or subject matter.

6. Richness and legibility
Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots ONLY on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Clean Inter/Helvetica-like sans-serif; exact filenames/tokens in clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density; wrap inside generous cells rather than shrinking type.

7. Honesty/exclusions
No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs only if they explain containment/transformation. This is an exercise-specific vault/MCP mechanism, not an operating-system sandbox or real classification system. These are exercise-specific OPEN/PARTNER/STAFF levels, NOT a real classification system. Do not depict a proposed marking as approved. Valid notices must meet type/originator/target/level requirements.

8. Generation self-check
Before returning the PNG, ensure this precise relationship reads immediately: Valid marking-change notice needs Release Authority originator, existing target, permitted new marking, and latest zulu among valid notices; inheritance uses effective source levels. Reject missing steps/default, reversed ordering, or a path from AI proposal to release. This is a generation check, not a claim that the image has been externally reviewed.


## 9. Revision requirements from review of the previous attempt
A previous generation of this figure was rejected. Generate a NEW image from this full contract and fix every defect below. All earlier blocks still govern; labels stay verbatim; add no words. Title text sits directly on the dark ground with no white bloom/haze band.

- Regenerate on dark ground; title washed out (m03-effective-handling)
Transcription: "DERIVE THE EFFECTIVE HANDLING."; step boxes "Header marking" / "Missing → STAFF" → "Latest valid notice by zulu" / "Release Authority" ↓ "Inherit effective source levels" / "Most restricted wins" ← "3 of 4 elements → STAFF minimum"; rail "New AI notes start STAFF" | "Proposal ≠ release.". The order and wording match Handling rules H1–H5 and H7. Defects: (1) The title sits on a white-cream bloom and has very low contrast. (2) The whole canvas is an olive/khaki haze instead of the #0D0906 ground used by the pilot, which muddies every panel edge. (3) "New AI notes start STAFF" is filled in olive, the prompt's "verified/allowed" accent. That colours a restrictive default as allowed. (4) Periods were added to the title and to "Proposal ≠ release.". Verdict: REGENERATE. Keep the same serpentine 1→2→3→4 layout and labels. Use a dark #0D0906 ground with no bloom behind the title. Give "New AI notes start STAFF" a neutral #2D3030 fill with a gold border. Keep "Proposal ≠ release" in the brick-red stroke. Drop both trailing periods.


## 10. Global rendering corrections (apply to this image)
- Background is flat-to-subtle #0D0906 near-black with at most a faint warm vignette. NO white, grey, cream or yellow bloom/glow/haze anywhere, especially not behind the title; title text is solid #FFF8E7 on dark ground, at least 64 px from the top edge, with only a thin warm sheen.
- Do not add trailing periods or any punctuation not in the label map.
- No people, silhouettes, hands, phones, gears, shields, medals, check-mark badges, browser windows or other decorative pictograms. Nodes are text-first; generic document glyphs only where they explain containment.
- Every essential label at least 32 px in #FFF8E7 or #C8B78A; never dim tan small text.
- Olive (#4F5634) only for allowed/verified states; brick red (#B43A2F) only for blocked/HOLD/warning; neutral routes use #2D3030 with gold stroke.
````

## m03-phase-scope-revoke

- Title: `NARROW, THEN REMOVE`
- Publication path: `shared/figures/m03-phase-scope-revoke.png`
- Anchor: Lab `## Disconnect and prove it`; replace `m03-revoke.svg` after the revoked-phase JSON block and introductory sentence, before the revoked-run commands. Do not place the scope answers before the partner section asks the learner to derive them.
- Caption: Give each phase only its declared reach, then remove the connection and confirm a fresh run was offered no MCP tools.
- Native size: 1536×1024; published SHA-256: `7dbd3797f20c0a6cf79f34e0f6e7278ca0529c93933ffd0b9ddcbb1a5981e2c7`
- Iteration history:
  - attempt-01: full generation; session `01a10054-cb84-74a0-83e7-2b077da69c66`; raw SHA-256 `4df7ded099f5ae4d…`; superseded — review: Regenerate with legible title; it is lost in the bloom (m03-phase-scope-revoke)
  - attempt-02: full generation; session `01a1007d-2d27-7ca3-a7b7-30e171f18139`; raw SHA-256 `e55381e31e7129e7…`; ACCEPTED
- Final review outcome: accepted attempt-02. F03: m03-phase-scope-revoke: ACCEPT_A2 — the labels and paths are verbatim and match lab lines 364/423/466/498. There are three separate envelopes under a plain time arrow, read and write rows are distinct, and REVOKED ends at mcpServers: {} / No tools offered / No server started with no denial node.

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.
[Block 1: tool/output instruction]

2. Lesson contract
Module 03 — Kiln Hold; shared/MODULE_03_LAB.md; H2 “Disconnect and prove it”. Caption / learning takeaway: “Give each phase only its declared reach, then remove the connection and confirm a fresh run was offered no MCP tools.” Intended transfer action: Declare distinct per-phase read and write reaches, then remove the server entry and inspect a fresh run for an empty tool offer. Misconception to prevent: A revoked phase is proved by asking an active server for a denied request, or partner work can still read research sources. The lesson prose here is NOT in-image text.

3. Composition
Diagram-first three permission envelopes with time progression. Native 1536×1024 landscape raster PNG; 64 px safe margin, top title zone, remaining canvas for the mechanism; prefer two rows to tiny copy. Reading order and zones: Three distinct permission envelopes in left-to-right time order, with a time arrow ABOVE them, not a data-copy arrow. RESEARCH has distinct read/write rows; PARTNER has separate narrower read/write rows and no path back to Sources; REVOKED shows an empty server map and fresh-run no-tool result, no active-server denial. No advance visual reveal of derived partner-scope answers outside this after-revocation anchor. Focal relationship: research scope → narrower partner scope → removed connection Arrows mean only their described relationships, NEVER approval. No decorative connectors, no slide-overlay reserve.

4. Verbatim label map
Title zone: NARROW, THEN REMOVE.
Left envelope: RESEARCH | Read: Handbook/ + Sources/ | New writes: Drafts/research/. Middle envelope: PARTNER | Read: Estimate/Releasable/ | New writes: Drafts/partner/. Right envelope: REVOKED | mcpServers: {} | No tools offered | No server started.
Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Duplicate a label only where its specified branches require it. Yes and No are allowed solely on edges leaving a question ending in ? with both destinations specified; there are no question nodes here. Structural numbers only where specified numbered steps/rows (none here). The mapping text, zone names and directions are instructions, NOT visible words.

5. Visual family
#0D0906 primary ground; #17110C panel fill; #A58650 primary gold; #C8A96A sheen and connector highlights; #C8B78A secondary readable text; #FFF8E7 primary text; #655337 subdued nonessential rules; #3A2E1B faint structural lines; #4F5634 restrained verified/allowed accents; #B43A2F warnings/blocked branches; #2D3030 neutral mechanisms. Olive and brick red are fills/strokes/pills ONLY; text off-white or sandstone with high contrast; every status has a text label plus color. No bright green/blue/cyan/teal/purple. No Starzl product names or product-specific color identities. The site references supply the warm earth lineage, not photographic composition or subject matter.

6. Richness and legibility
Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots ONLY on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Clean Inter/Helvetica-like sans-serif; exact filenames/tokens in clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density; wrap inside generous cells rather than shrinking type.

7. Honesty/exclusions
No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs only if they explain containment/transformation. This is an exercise-specific vault/MCP mechanism, not an operating-system sandbox or real classification system. Never imply a guard refusal from an active server proves disconnection; revoked has no server started. Read and new-write scopes must remain separate.

8. Generation self-check
Before returning the PNG, ensure this precise relationship reads immediately: The connection is narrowed for partner work and REMOVED for revoked work; fresh run offers zero MCP tools and starts no server. Reject any data-copy arrow, lingering partner read access to Sources, or revoked server-denial node. This is a generation check, not a claim that the image has been externally reviewed.


## 9. Revision requirements from review of the previous attempt
A previous generation of this figure was rejected. Generate a NEW image from this full contract and fix every defect below. All earlier blocks still govern; labels stay verbatim; add no words. Title text sits directly on the dark ground with no white bloom/haze band.

- Regenerate with legible title; it is lost in the bloom (m03-phase-scope-revoke)
Transcription: "NARROW, THEN REMOVE."; plain time arrow above; "RESEARCH" / "Read:" "Handbook/" "+ Sources/" / "New writes:" "Drafts/research/"; "PARTNER" / "Read:" "Estimate/Releasable/" (wrapped as Estimate/ + Releasable/) / "New writes:" "Drafts/partner/"; "REVOKED" / "mcpServers: {}" / "No tools offered" / "No server started". The scopes match spec.json:123-129 and the lab text at :548. Revoked shows no server-denial node, and there is no data-copy arrow. Defect: the title is cream text on a near-white bloom, the lowest-contrast heading in the module. It is barely readable at article width and breaks the dark-ground style of the pilot. The title also has an added trailing period. Verdict: REGENERATE, keeping the layout exactly. Use a dark #0D0906 ground behind "NARROW, THEN REMOVE" (no period) with #FFF8E7 text and a restrained glow at most. If possible, keep "Estimate/Releasable/" on one line.


## 10. Global rendering corrections (apply to this image)
- Background is flat-to-subtle #0D0906 near-black with at most a faint warm vignette. NO white, grey, cream or yellow bloom/glow/haze anywhere, especially not behind the title; title text is solid #FFF8E7 on dark ground, at least 64 px from the top edge, with only a thin warm sheen.
- Do not add trailing periods or any punctuation not in the label map.
- No people, silhouettes, hands, phones, gears, shields, medals, check-mark badges, browser windows or other decorative pictograms. Nodes are text-first; generic document glyphs only where they explain containment.
- Every essential label at least 32 px in #FFF8E7 or #C8B78A; never dim tan small text.
- Olive (#4F5634) only for allowed/verified states; brick red (#B43A2F) only for blocked/HOLD/warning; neutral routes use #2D3030 with gold stroke.
````

## m03-probe-proof

- Title: `TEST THE EFFECT, NAME THE LAYER`
- Publication path: `shared/figures/m03-probe-proof.png`
- Anchor: same section; replace `m03-probe-matrix.svg` after the bounded probe instructions.
- Caption: With deletion excluded, the normal probe reports HELD by the allow-list in both configurations; only the server-only probe establishes the server's response to that call.
- Native size: 1536×1024; published SHA-256: `745ac0669ac98ae7759d0d0bf086a578dd8dfb2b679daac499c3070642d7161b`
- Iteration history:
  - attempt-01: full generation; session `01a10055-ac66-7f30-9378-6c62cfe015b3`; raw SHA-256 `74413a81f7eabb66…`; superseded — review: Remove blown-out haze behind title and footer (m03-probe-proof)
  - attempt-02: full generation; session `01a1007c-20cf-7ab2-a7f9-c9783caaf0d3`; raw SHA-256 `3b2e15ec9792a8cc…`; superseded
  - attempt-03: edit; session `01a10089-7416-75f0-b6cc-31c3a4e10498`; raw SHA-256 `c554663eb2c2f365…`; ACCEPTED
- Final review outcome: accepted attempt-03. Final1: m03-probe-proof: ACCEPT_A3 — all three trailing periods are gone (TEST THE EFFECT, NAME THE LAYER; Not sent to server; Permitted actions must work) and the title comma is kept. Matrix, colors, bracket and SERVER-ONLY STRETCH lane (--ignore-allow-list → Server denial + disk check) match A1 exactly.

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to EDIT the first attached image and save exactly ONE corrected PNG with an OPAQUE #0D0906 background (no transparency). Do not use a CLI image fallback or write code/SVG. The other attachments are STYLE references only. Return the absolute saved PNG path and no claim of verification.

CORRECTIONS (apply exactly; preserve every other relationship, label, position and color):
m03-probe-proof: LABEL_EDIT_A1 — remove three trailing periods
Transcription of A1: "TEST THE EFFECT, NAME THE LAYER."; "NORMAL PROBE"; headers "Open" | "Bounded"; rows "Read outside scope", "Overwrite source" and "Create outside folder", each = "BREACHED" (red) | "HELD" (olive); "Delete source" = "HELD (allow-list)" | "HELD (allow-list)" (amber), with a bracket under both delete cells to "Not sent to server."; a separate panel "SERVER-ONLY STRETCH" with "--ignore-allow-list" → "Server denial + disk check"; footer "Permitted actions must work.". The structure and outcomes match authority_probe.py:298 (held_by allow-list when not sent), spec.json:155-171, and lab lines 225/246/282. It also uses distinct colors for BREACHED, HELD and HELD (allow-list). A2 fills every result cell, HELD and BREACHED alike, with the same brick red, and its frame has a stray broken border, so A1 is the better base. Defect: three strings carry trailing periods that are absent from the PLAN.md label list and that §10 forbids. Fix with an image edit of attempt-01/flattened.png. Title (top center): "TEST THE EFFECT, NAME THE LAYER." → "TEST THE EFFECT, NAME THE LAYER". Bracket note box below the delete row: "Not sent to server." → "Not sent to server". Footer (bottom center): "Permitted actions must work." → "Permitted actions must work". Keep the comma in the title and change nothing else.

The original full generation contract follows and still governs labels and composition:

$imagegen
Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.
[Block 1: tool/output instruction]

2. Lesson contract
Module 03 — Kiln Hold; shared/MODULE_03_LAB.md; H2 “Declare what the connection may do, then prove the limits”. Caption / learning takeaway: “With deletion excluded, the normal probe reports HELD by the allow-list in both configurations; only the server-only probe establishes the server’s response to that call.” Intended transfer action: Compare normal probe outcomes against an open and bounded server, then use the separate bypass to isolate server enforcement. Misconception to prevent: HELD on a delete attempt in the normal run proves the server itself denied deletion. The lesson prose here is NOT in-image text.

3. Composition
Diagram-first matrix with independent lower probe lane. Native 1536×1024 landscape raster PNG; 64 px safe margin, top title zone, remaining canvas for the mechanism; prefer two rows to tiny copy. Reading order and zones: Upper normal-probe matrix has four rows and two columns. Read outside scope, Overwrite source, Create outside folder are BREACHED under Open, HELD under Bounded. Delete source is HELD (allow-list) in BOTH columns; explicitly connect this row to Not sent to server. Lower independent SERVER-ONLY STRETCH lane runs --ignore-allow-list → forbidden attempt reaches server → Server denial + disk check; do not imply a completed learner run. Separate footer states Permitted actions must work. Matrix status words are only illustrative of supplied probe contract, not measured learner output. Focal relationship: normal delete stopped upstream ≠ server denial Arrows mean only their described relationships, NEVER approval. No decorative connectors, no slide-overlay reserve.

4. Verbatim label map
Title zone: TEST THE EFFECT, NAME THE LAYER.
Upper heading: NORMAL PROBE. Column headers: Open | Bounded. Rows: Read outside scope | Overwrite source | Create outside folder | Delete source. Cells rows 1–3: BREACHED in Open; HELD in Bounded (repeat labels in their separate specified cells). Row 4: HELD (allow-list) in Open; HELD (allow-list) in Bounded. Delete-row side note: Not sent to server. Lower heading: SERVER-ONLY STRETCH. Lower flow: --ignore-allow-list | Server denial + disk check. Footer: Permitted actions must work.
Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Duplicate a label only where its specified branches require it. Yes and No are allowed solely on edges leaving a question ending in ? with both destinations specified; there are no question nodes here. Structural numbers only where specified numbered steps/rows (none here). The mapping text, zone names and directions are instructions, NOT visible words.

5. Visual family
#0D0906 primary ground; #17110C panel fill; #A58650 primary gold; #C8A96A sheen and connector highlights; #C8B78A secondary readable text; #FFF8E7 primary text; #655337 subdued nonessential rules; #3A2E1B faint structural lines; #4F5634 restrained verified/allowed accents; #B43A2F warnings/blocked branches; #2D3030 neutral mechanisms. Olive and brick red are fills/strokes/pills ONLY; text off-white or sandstone with high contrast; every status has a text label plus color. No bright green/blue/cyan/teal/purple. No Starzl product names or product-specific color identities. The site references supply the warm earth lineage, not photographic composition or subject matter.

6. Richness and legibility
Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots ONLY on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Clean Inter/Helvetica-like sans-serif; exact filenames/tokens in clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density; wrap inside generous cells rather than shrinking type.

7. Honesty/exclusions
No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs only if they explain containment/transformation. This is an exercise-specific vault/MCP mechanism, not an operating-system sandbox or real classification system. Do not report the normal delete as server-denied, and do not present illustrative outcomes as a real learner measurement.

8. Generation self-check
Before returning the PNG, ensure this precise relationship reads immediately: Normal delete has HELD (allow-list) twice and server.outcome NOT_SENT conceptually; server-only stretch is a distinct bypass, not normal probe evidence. Reject if either delete cell differs, if any first-three cells reverse, if stretch merges with normal results, or if permitted-work check disappears. This is a generation check, not a claim that the image has been externally reviewed.
````

