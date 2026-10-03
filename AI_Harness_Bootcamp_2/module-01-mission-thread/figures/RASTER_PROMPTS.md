# Raster figure prompts and provenance — module-01-mission-thread

Staff-only record. Not published (absent from `course.json`).

- Generator: `codex-cli 0.154.0` (`codex exec`, ChatGPT login, built-in `image_gen`).
- Style references attached to every invocation: `ui/images/home-hero.webp` and `ui/images/home-band-custody.webp`, decoded losslessly to PNG with `dwebp`; every figure except `m00-bounded-direction` also received the accepted `m00-bounded-direction` attempt-01 raster as a style-only reference. Label edits additionally attached the image being edited as the first input.
- Post-processing: the generator returns RGBA with a transparent ground. Each accepted raster was alpha-composited onto the specified `#0D0906` ground and saved as opaque lossless RGB PNG at native size. No other pixel changes, no resizing.
- Run evidence (all attempts, logs, rejected rasters, reviews): `~/course-evidence/course-raster-visuals/20261002T233502`
- Module source contract: `module-01-mission-thread/shared/MISSION_THREAD.md` §§What a mission thread is, Five kinds of statement, Source authority belongs to the claim, The handoff rule; Lab steps 1–10. `shared/WHEN_EVIDENCE_BREAKS.md` supports mismatch reasoning. The protected arithmetic/answer model and sealed change are not image content.
- Owning page digests at integration (SHA-256): `shared/MISSION_THREAD.md` 874dc4073b28c02c…; `shared/MODULE_01_LAB.md` f753a17df0dfa91c…

## m01-atomic-ledger

- Title: `ONE MATERIAL CLAIM PER ROW`
- Publication path: `shared/figures/m01-atomic-ledger.png`
- Anchor: Lab `## 3. Split the AI brief into material claims`.
- Caption: Give each action-changing claim its own support, dependency, and uncertainty instead of letting one citation carry a compound conclusion.
- Native size: 1536×1024; published SHA-256: `8186c81b7d6e52c7845baf305e2f5a4cf8d2a819d81b2a990d2af499dc460912`
- Iteration history:
  - attempt-01: full generation; session `01a10049-da4f-7943-9ec0-a5563729b455`; raw SHA-256 `f27f692d9d50cef7…`; superseded — review: m01-atomic-ledger: REGENERATE — compound glyph splits into column headers, not the claims
  - attempt-02: full generation; session `01a10079-7a6d-7682-81fa-90d31454774b`; raw SHA-256 `0cf68cb5989fb38e…`; superseded
  - attempt-03: full generation; session `01a10088-56ea-7650-83f7-ecbd9a2fd4dc`; raw SHA-256 `8ce8737e7d3ea98f…`; ACCEPTED
- Final review outcome: accepted attempt-03. Final1: m01-atomic-ledger: ACCEPT_A3 — strings: ONE MATERIAL CLAIM PER ROW; Source + version + locator; Statement kind; Warrant; Units + calculation; Dependency + handoff; Uncertainty; Count claim; State claim; Decision claim; Stop at fact, calculation, assumption, HOLD, or human decision (pills, HOLD the only brick-red one). The glyph sends three arrows to the three claims. Each row has its own horizontal trace with no vertical link inside the grid. The corner cell is gone and the bottom strip is plain with no connectors. The two-line headers are larger than A2 but still ~28–29 px against a 3

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

2. Lesson contract
Owning module: Module 01, Cold Lantern. Owning page: shared/MODULE_01_LAB.md, section "3. Split the AI brief into material claims". Takeaway: “Give each action-changing claim its own support, dependency, and uncertainty instead of letting one citation carry a compound conclusion.” Intended learner action in unfamiliar work: For an unfamiliar AI recommendation, split a compound assertion into individual ledger rows and follow dependencies until a valid stopping condition. Prevent this misconception: Using one citation to justify a count, a release state and a decision all at once. These are production instructions, not additional text to draw.

3. Composition
Figure category: branching evidence ledger. Use a 1536×1024 landscape canvas and 64 px safe margin. Place the exact title in a clear top zone; reserve the rest for the mechanism, preferably two spacious rows rather than tiny type. Reading order and spatial zones: One unlabeled compound assertion glyph at the top splits into Count claim, State claim and Decision claim, each in a separate ledger row with its own Source + version + locator, Statement kind, Warrant, Units + calculation where applicable, Dependency + handoff, and Uncertainty. A common bottom strip reads Stop at fact, calculation, assumption, HOLD, or human decision. Do not repeat label text on every row; use a shared field-header strip aligned over independent rows and thin traces from each row to its own evidence slot. The focal relationship is: Separate material claims cannot share one unexamined warrant Arrows mean only the stated dependency or classification, never automatic approval. No decorative connectors or slide-overlay space; this is an inline course figure.

4. Verbatim label map
Title, top zone: ONE MATERIAL CLAIM PER ROW
Permitted labels in their composition-assigned nodes, strips or branches:
- Count claim
- State claim
- Decision claim
- Source + version + locator
- Statement kind
- Warrant
- Units + calculation
- Dependency + handoff
- Uncertainty
- Stop at fact, calculation, assumption, HOLD, or human decision
Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Duplicate a label only where its specified branches require it. Yes and No are the only additional words allowed, solely on edges leaving a question ending in ?; every such node must have both explicitly assigned destinations. Structural step numbers are permitted only where the brief specifies numbered steps/rows.

5. Visual family
#0D0906 primary ground; #17110C panel fill; #A58650 primary gold; #C8A96A sheen and connector highlights; #C8B78A secondary readable text; #FFF8E7 primary text; #655337 subdued nonessential rules; #3A2E1B faint structural lines; #4F5634 restrained verified/allowed accents; #B43A2F warnings/blocked branches; #2D3030 neutral mechanisms. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities. Keep the same warm-earth lineage as the attached homepage references, but not their photographic subject matter.

6. Richness and legibility
Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use clean Inter/Helvetica-like sans-serif; exact filenames/tokens may use a clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density. Full-frame technical figure only; no decorative scenery.

7. Honesty and exclusions
No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Specific constraint: No case counts, document IDs, cited case values, or implicit AI decision authority. Never expose source IDs, protected numerical answers, sealed-change values, or the correct case verdict. These constraints are not in-image words.

8. Generation self-check
Before returning the PNG, ensure this exact relationship remains obvious: Separate material claims cannot share one unexamined warrant; keep their three evidence paths distinct and show all five stopping endpoints. Check that the title and every permitted label appear once in the proper zone, except branch-specific repetition. Missing or misspelled labels, implicit Yes/No destinations, false approval arrows, or actual case answers make the figure unusable. Do not claim that you verified the result.


## 9. Revision requirements from review of the previous attempt
A previous generation of this figure was rejected. Generate a NEW image from this full contract and fix every defect below. All earlier blocks still govern; labels stay verbatim; add no words. Title text sits directly on the dark ground with no white bloom/haze band.

- m01-atomic-ledger: REGENERATE — compound glyph splits into column headers, not the claims
Transcription: 'ONE MATERIAL CLAIM PER ROW'; unlabeled document glyph; header strip 'Source + version + locator', 'Statement kind', 'Warrant', 'Units + calculation', 'Dependency + handoff', 'Uncertainty' (plus an empty corner header cell); rows 'Count claim', 'State claim', 'Decision claim', each with six empty cells (one cell, Count × Units + calculation, has a brighter outline); bottom 'Stop at' [fact], [calculation], [assumption], [HOLD], ', or' [human decision]. All labels are exact, with the stop strip split into pills but word-for-word intact, and nothing is added. Defects: (1) The branch from the compound glyph lands on the column headers Source + version + locator, Warrant, and Dependency + handoff, not on Count claim, State claim, and Decision claim. That inverts the mechanism: it shows one document splitting into fields rather than one compound assertion splitting into three claims (MODULE_01_LAB.md:238). (2) Header text is about 22–24 px, below 32 px. (3) The lone highlighted cell is unexplained and looks like a selected or passed status. (4) The result is an empty blank-form grid with no visible per-row thread-dependency link, so it fails learning utility. Fix: regenerate with the glyph's three traces ending at the left edge of the three claim labels. Use a single shared header strip with ≥32 px text, uniform cells with no highlight, and a thin trace from each row's Dependency + handoff cell to the bottom stop strip.


## 10. Global rendering corrections (apply to this image)
- Background is flat-to-subtle #0D0906 near-black with at most a faint warm vignette. NO white, grey, cream or yellow bloom/glow/haze anywhere, especially not behind the title; title text is solid #FFF8E7 on dark ground, at least 64 px from the top edge, with only a thin warm sheen.
- Do not add trailing periods or any punctuation not in the label map.
- No people, silhouettes, hands, phones, gears, shields, medals, check-mark badges, browser windows or other decorative pictograms. Nodes are text-first; generic document glyphs only where they explain containment.
- Every essential label at least 32 px in #FFF8E7 or #C8B78A; never dim tan small text.
- Olive (#4F5634) only for allowed/verified states; brick red (#B43A2F) only for blocked/HOLD/warning; neutral routes use #2D3030 with gold stroke.


## 11. Final revision requirements
Render on an OPAQUE #0D0906 background with no transparent pixels. Fix every defect below:

m01-atomic-ledger: REGENERATE — merged dependency trunk, 3/5 stop arrows, 25 px headers
Neither candidate is acceptable. A1 still branches the compound glyph into the column headers (Source + version + locator, Warrant, Dependency + handoff) instead of into the three claims, which is the inverted mechanism the revision rejected. A2 fixes the split: the glyph sends three arrows to Count claim, State claim and Decision claim, and every label is exact with nothing added (title; six headers; three claims; strip 'Stop at' [fact], [calculation], [assumption], [HOLD], ', or' [human decision]). A2 has three structural/legibility defects. (1) A single vertical gold trunk at x≈1180 joins the Dependency + handoff cells of all three rows, so the three claims visibly share one dependency path. That contradicts the focal relationship ('Separate material claims cannot share one unexamined warrant; keep their three evidence paths distinct') and MODULE_01_LAB.md:238 ('Do not let one citation stand in for all three'). (2) From that trunk a horizontal bar drops arrows only into fact, calculation and assumption. HOLD and human decision get no arrow, and the trunk ends on the strip border beside ', or', which implies only three of the lab's five legitimate stopping endpoints (MODULE_01_LAB.md:251-257) are reachable. (3) The header strip text measures ≈18 px cap height (≈25 px font; e.g. 'Warrant' y 210–227) against the required ≥32 px, about 13 px at 800 px article width, and the revision explicitly required ≥32 px headers. Regenerate keeping A2's layout: glyph at top-left with three separate arrows ending at the left edge of Count claim, State claim and Decision claim; one shared header strip with ≥32 px #FFF8E7 text (allow two lines and a taller strip; drop the empty corner cell); each row has its own horizontal trace through its six cells and no vertical connection between rows anywhere in the grid. Either drop all connectors between the grid and the bottom strip (a plain shared strip), or give each row its own thin trace from its Dependency + handoff cell to the strip with the strip as a whole as the target (not individual pills). If arrows land on pills, all five pills (fact, calculation, assumption, HOLD, human decision) must receive one. Keep HOLD as the only brick-red pill and add no words.
````

## m01-broken-handoff

- Title: `LOCALLY TRUE CAN STILL FAIL`
- Publication path: `shared/figures/m01-broken-handoff.png`
- Anchor: same guide, `## The handoff rule`; replace `m01-handoff-break.svg`.
- Caption: Check what the next step requires; the earlier true statement cannot supply missing authority or observation.
- Native size: 1536×1024; published SHA-256: `293b3bf4fd610dc17f00ac1b55da14d9f66968240020c1b198929009823ff117`
- Iteration history:
  - attempt-01: full generation; session `01a1004a-c6ca-78c1-9270-bdecd0c0ebbd`; raw SHA-256 `a205698a718a8a89…`; superseded — review: m01-broken-handoff: REGENERATE — washed-out title and gates that do not read as unmet
  - attempt-02: full generation; session `01a10078-823d-7e33-b2b5-a077aeedd223`; raw SHA-256 `c8b8b5f269f4c18b…`; ACCEPTED
- Final review outcome: accepted attempt-02. F01a: m01-broken-handoff: ACCEPT_A2 — the title and all 9 labels are exact and appear once. Each row has a brick-red X barrier gate and a dashed 'required' box on the right, with no connector into the requirement and no progression arrow. The ground is flat dark, all text measures about 34 px or larger, and the result matches MISSION_THREAD.md 'The handoff rule'. (A1 still uses the rejected pause-bar gates.)

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

2. Lesson contract
Owning module: Module 01, Cold Lantern. Owning page: shared/MISSION_THREAD.md, section "The handoff rule". Takeaway: “Check what the next step requires; the earlier true statement cannot supply missing authority or observation.” Intended learner action in unfamiliar work: In unfamiliar workflows, inspect each handoff for the separate authority or observed evidence required downstream. Prevent this misconception: Equating custody with release, permit intake with approval, expected arrival with delivery, or delivery with confirmed usability. These are production instructions, not additional text to draw.

3. Composition
Figure category: paired-state matrix. Use a 1536×1024 landscape canvas and 64 px safe margin. Place the exact title in a clear top zone; reserve the rest for the mechanism, preferably two spacious rows rather than tiny type. Reading order and spatial zones: Make four independent paired rows, left condition versus separately required right condition, with a clear unmet-evidence gate between each pair and no arrow of automatic progression: Recorded custody / Release required; Permit received / Approval required; Expected arrival / Delivery evidence required; Delivered / Usable quantity confirmation required. Place True here ≠ sufficient there as shared bottom conclusion. No row asserts whether the required right-side evidence exists. The focal relationship is: Four gaps between a locally true state and a distinct next requirement Arrows mean only the stated dependency or classification, never automatic approval. No decorative connectors or slide-overlay space; this is an inline course figure.

4. Verbatim label map
Title, top zone: LOCALLY TRUE CAN STILL FAIL
Permitted labels in their composition-assigned nodes, strips or branches:
- Recorded custody
- Release required
- Permit received
- Approval required
- Expected arrival
- Delivery evidence required
- Delivered
- Usable quantity confirmation required
- True here ≠ sufficient there
Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Duplicate a label only where its specified branches require it. Yes and No are the only additional words allowed, solely on edges leaving a question ending in ?; every such node must have both explicitly assigned destinations. Structural step numbers are permitted only where the brief specifies numbered steps/rows.

5. Visual family
#0D0906 primary ground; #17110C panel fill; #A58650 primary gold; #C8A96A sheen and connector highlights; #C8B78A secondary readable text; #FFF8E7 primary text; #655337 subdued nonessential rules; #3A2E1B faint structural lines; #4F5634 restrained verified/allowed accents; #B43A2F warnings/blocked branches; #2D3030 neutral mechanisms. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities. Keep the same warm-earth lineage as the attached homepage references, but not their photographic subject matter.

6. Richness and legibility
Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use clean Inter/Helvetica-like sans-serif; exact filenames/tokens may use a clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density. Full-frame technical figure only; no decorative scenery.

7. Honesty and exclusions
No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Specific constraint: Never claim actual delivery, permit approval, or confirmed usable quantity. Never expose source IDs, protected numerical answers, sealed-change values, or the correct case verdict. These constraints are not in-image words.

8. Generation self-check
Before returning the PNG, ensure this exact relationship remains obvious: Four gaps between a locally true state and a distinct next requirement; if any pair appears as successful progression or the gap disappears, unusable. Check that the title and every permitted label appear once in the proper zone, except branch-specific repetition. Missing or misspelled labels, implicit Yes/No destinations, false approval arrows, or actual case answers make the figure unusable. Do not claim that you verified the result.


## 9. Revision requirements from review of the previous attempt
A previous generation of this figure was rejected. Generate a NEW image from this full contract and fix every defect below. All earlier blocks still govern; labels stay verbatim; add no words. Title text sits directly on the dark ground with no white bloom/haze band.

- m01-broken-handoff: REGENERATE — washed-out title and gates that do not read as unmet
Transcription: 'LOCALLY TRUE CAN STILL FAIL'; rows 'Recorded custody | Release required', 'Permit received | Approval required', 'Expected arrival | Delivery evidence required', 'Delivered | Usable quantity confirmation required'; bottom 'True here ≠ sufficient there'. All labels are exact and appear once; nothing is added; there are no progression arrows. Defects: (1) An intense white bloom sits behind the title and the bottom conclusion, and a fog spreads across the whole canvas. The title's off-white letters dissolve into the halo, so legibility drops, and this is the banned 'cinematic haze'. (2) The 'unmet-evidence gate' is a pair of plain gold bars in each gutter. They read as a pause icon or a decorative divider, not as missing evidence. They use the same gold as connectors, have no red/blocked treatment and no closed-gate shape, so the figure reads as a two-column table. Learning utility fails the brief's focal relationship ('if … the gap disappears, unusable'). Fix: regenerate with a flat dark ground and no bloom, and put a closed-gate glyph in each gutter: a brick-red (#B43A2F) barrier or broken connector stub that ends before the right card. Keep the right-hand 'required' cards visually open or unfilled (for example a dashed outline) so that no row asserts the evidence exists. Render the bottom conclusion as a solid panel with no glow.


## 10. Global rendering corrections (apply to this image)
- Background is flat-to-subtle #0D0906 near-black with at most a faint warm vignette. NO white, grey, cream or yellow bloom/glow/haze anywhere, especially not behind the title; title text is solid #FFF8E7 on dark ground, at least 64 px from the top edge, with only a thin warm sheen.
- Do not add trailing periods or any punctuation not in the label map.
- No people, silhouettes, hands, phones, gears, shields, medals, check-mark badges, browser windows or other decorative pictograms. Nodes are text-first; generic document glyphs only where they explain containment.
- Every essential label at least 32 px in #FFF8E7 or #C8B78A; never dim tan small text.
- Olive (#4F5634) only for allowed/verified states; brick red (#B43A2F) only for blocked/HOLD/warning; neutral routes use #2D3030 with gold stroke.
````

## m01-byte-identity

- Title: `IDENTITY IS NOT TRUTH`
- Publication path: `shared/figures/m01-byte-identity.png`
- Anchor: Lab `## 1. Open and hash the inbox`; replace `m01-desk-intake.svg`.
- Caption: A hash identifies the bytes you used; source authority and applicability still require inspection.
- Native size: 1536×1024; published SHA-256: `087186460729ac60107f073a963c449ece8231ede779ef4b1b2a6dd17a444beb`
- Iteration history:
  - attempt-01: full generation; session `01a1004b-96b5-7ee2-ae7c-58e7ef040666`; raw SHA-256 `aacf83c400da7a74…`; superseded — review: m01-byte-identity: REGENERATE — applicability checks drawn as two serial chains
  - attempt-02: full generation; session `01a10078-9367-7102-b9af-526d8d5e8ca3`; raw SHA-256 `eeb3af0a9ab49c8a…`; ACCEPTED
- Final review outcome: accepted attempt-02. F01a: m01-byte-identity: ACCEPT_A2 — the title and all 10 labels are exact, ≠ is correct and nothing is added. Issuer, Version + time, Exact entity and Allowed use each send their own arrow into Claim fit. The byte lane is File bytes→Hash→Byte identity. The two lanes meet only at Traceable evidence, with no trust badge. The divider 'Hash ≠ truth or authority' has a contrast ratio of about 13.6:1 at about 34 px. (A1 keeps the rejected serial pairs.)

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

2. Lesson contract
Owning module: Module 01, Cold Lantern. Owning page: shared/MODULE_01_LAB.md, section "1. Open and hash the inbox". Takeaway: “A hash identifies the bytes you used; source authority and applicability still require inspection.” Intended learner action in unfamiliar work: For an unfamiliar source file, record its exact bytes, then independently check whether its issuer, version, entity and allowed use fit the claim. Prevent this misconception: Assuming a matching hash proves that the document is true, authoritative, or applicable. These are production instructions, not additional text to draw.

3. Composition
Figure category: converging evidence lanes. Use a 1536×1024 landscape canvas and 64 px safe margin. Place the exact title in a clear top zone; reserve the rest for the mechanism, preferably two spacious rows rather than tiny type. Reading order and spatial zones: Two separate lanes converge on a single Traceable evidence record without an automatic trust badge. Upper lane File bytes → Hash → Byte identity. Lower lane Issuer, Version + time, Exact entity, Allowed use → Claim fit. Place Hash ≠ truth or authority on the dividing rule. Byte identity is not a substitute for claim fit. The focal relationship is: Hash establishes byte identity alone while four independent applicability checks establish claim fit Arrows mean only the stated dependency or classification, never automatic approval. No decorative connectors or slide-overlay space; this is an inline course figure.

4. Verbatim label map
Title, top zone: IDENTITY IS NOT TRUTH
Permitted labels in their composition-assigned nodes, strips or branches:
- File bytes
- Hash
- Byte identity
- Issuer
- Version + time
- Exact entity
- Allowed use
- Claim fit
- Traceable evidence
- Hash ≠ truth or authority
Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Duplicate a label only where its specified branches require it. Yes and No are the only additional words allowed, solely on edges leaving a question ending in ?; every such node must have both explicitly assigned destinations. Structural step numbers are permitted only where the brief specifies numbered steps/rows.

5. Visual family
#0D0906 primary ground; #17110C panel fill; #A58650 primary gold; #C8A96A sheen and connector highlights; #C8B78A secondary readable text; #FFF8E7 primary text; #655337 subdued nonessential rules; #3A2E1B faint structural lines; #4F5634 restrained verified/allowed accents; #B43A2F warnings/blocked branches; #2D3030 neutral mechanisms. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities. Keep the same warm-earth lineage as the attached homepage references, but not their photographic subject matter.

6. Richness and legibility
Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use clean Inter/Helvetica-like sans-serif; exact filenames/tokens may use a clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density. Full-frame technical figure only; no decorative scenery.

7. Honesty and exclusions
No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Specific constraint: No source identifiers, actual hashes, numerical answers, or issuer approval claims. Never expose source IDs, protected numerical answers, sealed-change values, or the correct case verdict. These constraints are not in-image words.

8. Generation self-check
Before returning the PNG, ensure this exact relationship remains obvious: Hash establishes byte identity alone while four independent applicability checks establish claim fit; both lanes must meet only at traceable evidence, never certified truth. Check that the title and every permitted label appear once in the proper zone, except branch-specific repetition. Missing or misspelled labels, implicit Yes/No destinations, false approval arrows, or actual case answers make the figure unusable. Do not claim that you verified the result.


## 9. Revision requirements from review of the previous attempt
A previous generation of this figure was rejected. Generate a NEW image from this full contract and fix every defect below. All earlier blocks still govern; labels stay verbatim; add no words. Title text sits directly on the dark ground with no white bloom/haze band.

- m01-byte-identity: REGENERATE — applicability checks drawn as two serial chains
Transcription: 'IDENTITY IS NOT TRUTH'; upper lane 'File bytes' → 'Hash' → 'Byte identity' → 'Traceable evidence'; divider pill 'Hash ≠ truth or authority'; lower lane 'Issuer'–'Version + time', 'Exact entity'–'Allowed use' → 'Claim fit' → 'Traceable evidence'. All labels are exact and appear once; nothing is added; ≠ is correct. Defect: the brief's focal relationship is 'four independent applicability checks establish claim fit'. In the image, Issuer is joined by a connector dot to Version + time, and Exact entity to Allowed use. Only Version + time and Allowed use carry traces into Claim fit. That shows two serial chains (Issuer → Version, Entity → Use) in which Issuer and Exact entity never reach Claim fit directly, as if issuer were merely a prerequisite of version. Secondary: the divider rule runs right up to the arrowhead at Traceable evidence and reads as a possible third input. Fix: regenerate with the four checks as a vertical stack (Issuer, Version + time, Exact entity, Allowed use), each with its own trace converging on Claim fit and no connectors between the checks. End the dividing rule well before the Traceable evidence card.


## 10. Global rendering corrections (apply to this image)
- Background is flat-to-subtle #0D0906 near-black with at most a faint warm vignette. NO white, grey, cream or yellow bloom/glow/haze anywhere, especially not behind the title; title text is solid #FFF8E7 on dark ground, at least 64 px from the top edge, with only a thin warm sheen.
- Do not add trailing periods or any punctuation not in the label map.
- No people, silhouettes, hands, phones, gears, shields, medals, check-mark badges, browser windows or other decorative pictograms. Nodes are text-first; generic document glyphs only where they explain containment.
- Every essential label at least 32 px in #FFF8E7 or #C8B78A; never dim tan small text.
- Olive (#4F5634) only for allowed/verified states; brick red (#B43A2F) only for blocked/HOLD/warning; neutral routes use #2D3030 with gold stroke.
````

## m01-change-isolation

- Title: `PREDICT BEFORE THE SOURCE CHANGES`
- Publication path: `shared/figures/m01-change-isolation.png`
- Anchor: Lab `## 10. Predict the source-change effect`; replace `m01-changed-source.svg`.
- Caption: Predict the update's reach before seeing it, change only dependent claims, and keep unrelated blockers visible.
- Native size: 1536×1024; published SHA-256: `9f05dae9b6219f49ef2506dc3629ed80f4f017cbdc18c6f9502239379d6cc6d3`
- Iteration history:
  - attempt-01: full generation; session `01a1004c-8258-7a43-b0bf-8819fc8125ff`; raw SHA-256 `0b9bf2817e467816…`; superseded — review: m01-change-isolation: REGENERATE — clip-art head/chart icons; reveal label on hazard stripes
  - attempt-02: full generation; session `01a1007a-cb48-76d2-ae79-7997c2092085`; raw SHA-256 `5c4dd5f4bc91b81e…`; ACCEPTED
- Final review outcome: accepted attempt-02. F01a: m01-change-isolation: ACCEPT_A2 — the title and all 9 labels are exact, there are no pictograms, and Reveal source update is a solid sealed panel with large text. May change→Update dependent claims (gold) and Must not change→Preserve unrelated blockers (brick red) stay as separate paths into Recompute verdict. The flat red banner reads 'New evidence ≠ automatic GO', with no value or verdict leaked. (A1 has head/gear and chart icons and a hazard-striped reveal bar.)

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

2. Lesson contract
Owning module: Module 01, Cold Lantern. Owning page: shared/MODULE_01_LAB.md, section "10. Predict the source-change effect". Takeaway: “Predict the update's reach before seeing it, change only dependent claims, and keep unrelated blockers visible.” Intended learner action in unfamiliar work: In unfamiliar revision work, freeze the original, predict both changing and fixed claims, reveal the update and revisit only downstream dependencies. Prevent this misconception: Assuming one updated source automatically clears every blocker or permits a GO. These are production instructions, not additional text to draw.

3. Composition
Figure category: controlled dependency fork. Use a 1536×1024 landscape canvas and 64 px safe margin. Place the exact title in a clear top zone; reserve the rest for the mechanism, preferably two spacious rows rather than tiny type. Reading order and spatial zones: Left-to-right ordered path Frozen baseline → Predict first, which forks into May change and Must not change. Both are recorded before Reveal source update. After reveal, Update dependent claims connects only to the may-change path while Preserve unrelated blockers remains fixed on the must-not-change path. Both feed Recompute verdict, with New evidence ≠ automatic GO as a visible boundary below. Do not insert any specific source change value or imply the recomputed verdict. The focal relationship is: Prediction precedes reveal, dependent claims update while unrelated blockers persist Arrows mean only the stated dependency or classification, never automatic approval. No decorative connectors or slide-overlay space; this is an inline course figure.

4. Verbatim label map
Title, top zone: PREDICT BEFORE THE SOURCE CHANGES
Permitted labels in their composition-assigned nodes, strips or branches:
- Frozen baseline
- Predict first
- May change
- Must not change
- Reveal source update
- Update dependent claims
- Preserve unrelated blockers
- Recompute verdict
- New evidence ≠ automatic GO
Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Duplicate a label only where its specified branches require it. Yes and No are the only additional words allowed, solely on edges leaving a question ending in ?; every such node must have both explicitly assigned destinations. Structural step numbers are permitted only where the brief specifies numbered steps/rows.

5. Visual family
#0D0906 primary ground; #17110C panel fill; #A58650 primary gold; #C8A96A sheen and connector highlights; #C8B78A secondary readable text; #FFF8E7 primary text; #655337 subdued nonessential rules; #3A2E1B faint structural lines; #4F5634 restrained verified/allowed accents; #B43A2F warnings/blocked branches; #2D3030 neutral mechanisms. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities. Keep the same warm-earth lineage as the attached homepage references, but not their photographic subject matter.

6. Richness and legibility
Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use clean Inter/Helvetica-like sans-serif; exact filenames/tokens may use a clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density. Full-frame technical figure only; no decorative scenery.

7. Honesty and exclusions
No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Specific constraint: Never reveal sealed source values, source IDs, numerical answers, or the case verdict. Never expose source IDs, protected numerical answers, sealed-change values, or the correct case verdict. These constraints are not in-image words.

8. Generation self-check
Before returning the PNG, ensure this exact relationship remains obvious: Prediction precedes reveal, dependent claims update while unrelated blockers persist; no automatic GO and no changed source value. Check that the title and every permitted label appear once in the proper zone, except branch-specific repetition. Missing or misspelled labels, implicit Yes/No destinations, false approval arrows, or actual case answers make the figure unusable. Do not claim that you verified the result.


## 9. Revision requirements from review of the previous attempt
A previous generation of this figure was rejected. Generate a NEW image from this full contract and fix every defect below. All earlier blocks still govern; labels stay verbatim; add no words. Title text sits directly on the dark ground with no white bloom/haze band.

- m01-change-isolation: REGENERATE — clip-art head/chart icons; reveal label on hazard stripes
Transcription: 'PREDICT BEFORE THE SOURCE CHANGES'; 'Frozen baseline' → 'Predict first' → forks to 'May change' and 'Must not change'; vertical hazard-striped bar 'Reveal source update'; then 'Update dependent claims' (from May change) and 'Preserve unrelated blockers' (from Must not change) → 'Recompute verdict'; bottom red banner '! New evidence ≠ automatic GO'. All labels are exact and appear once; nothing is added; ≠ is correct. The topology matches the brief, and no change value or verdict is leaked. Defects: (1) 'Predict first' uses a human-head silhouette with a gear, a person-like clip-art glyph excluded by 'no people', and 'Recompute verdict' uses a bar-chart document that implies numeric output. Six decorative icons compete with the mechanism. (2) 'Reveal source update' is set at about 26–28 px over a high-contrast diagonal hazard stripe in a narrow bar, so it is the hardest label to read at article width, below 32 px. (3) The bottom banner has a strong red glow (haze). Fix: regenerate with no pictograms, or only one neutral document glyph on Frozen baseline. Make 'Reveal source update' a solid sealed panel (#2D3030 fill, gold border) at least 220 px wide with ≥34 px text, and use a flat red-stroke banner with no glow.


## 10. Global rendering corrections (apply to this image)
- Background is flat-to-subtle #0D0906 near-black with at most a faint warm vignette. NO white, grey, cream or yellow bloom/glow/haze anywhere, especially not behind the title; title text is solid #FFF8E7 on dark ground, at least 64 px from the top edge, with only a thin warm sheen.
- Do not add trailing periods or any punctuation not in the label map.
- No people, silhouettes, hands, phones, gears, shields, medals, check-mark badges, browser windows or other decorative pictograms. Nodes are text-first; generic document glyphs only where they explain containment.
- Every essential label at least 32 px in #FFF8E7 or #C8B78A; never dim tan small text.
- Olive (#4F5634) only for allowed/verified states; brick red (#B43A2F) only for blocked/HOLD/warning; neutral routes use #2D3030 with gold stroke.
````

## m01-recompute-feasibility

- Title: `CALCULATION IS NOT FEASIBILITY`
- Publication path: `shared/figures/m01-recompute-feasibility.png`
- Anchor: Lab `## 5. Recompute every deterministic claim`.
- Caption: Recompute from supported premises and units, then check feasibility separately; a valid calculation does not establish that the handoff can occur.
- Native size: 1536×1024; published SHA-256: `b57e2c88ae4363afba49df95eda526f56870e842ddca4a0214f54598f22e9c1e`
- Iteration history:
  - attempt-01: full generation; session `01a1004d-5ecf-7bc3-bc50-8312a132d634`; raw SHA-256 `3feca8bd4ca74a74…`; superseded — review: m01-recompute-feasibility: REGENERATE — title dissolved in bloom; footer label undersized
  - attempt-02: full generation; session `01a10079-a020-7522-a638-3d62c93744ee`; raw SHA-256 `27aac313a89d174a…`; ACCEPTED
- Final review outcome: accepted attempt-02. F01a: m01-recompute-feasibility: ACCEPT_A2 — all 11 labels are exact, including the → and ≠ glyphs and the apostrophe. Both questions have explicit Yes and No destinations. 'Do not copy the producer's result' sits under the operation lane. 'Not observed delivery' is about 34 px off-white inside the olive feasible card, with no loops or numbers. This matches MODULE_01_LAB.md §5. (In A1, 'Not observed delivery' is undersized and 'Feasible at this boundary' runs into its border.)

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

2. Lesson contract
Owning module: Module 01, Cold Lantern. Owning page: shared/MODULE_01_LAB.md, section "5. Recompute every deterministic claim". Takeaway: “Recompute from supported premises and units, then check feasibility separately; a valid calculation does not establish that the handoff can occur.” Intended learner action in unfamiliar work: In unfamiliar work, verify source premises, reproduce arithmetic and test conditions before presenting an estimate as achievable. Prevent this misconception: A mathematically valid arrival computation being mistaken for an available or observed delivery. These are production instructions, not additional text to draw.

3. Composition
Figure category: two-stage conditional flow. Use a 1536×1024 landscape canvas and 64 px safe margin. Place the exact title in a clear top zone; reserve the rest for the mechanism, preferably two spacious rows rather than tiny type. Reading order and spatial zones: Source values and Units jointly enter Premises supported?; No edge ends at UNSUPPORTED → HOLD, Yes edge reaches Visible operation then Independent result. Result enters Required entry conditions met?; No edge reaches Counterfactual ≠ observed, Yes edge reaches Feasible at this boundary, which is bounded by Not observed delivery. Put Do not copy the producer’s result below the independent-operation lane. Every question has explicit Yes and No edges; no branch loops back as an automatic fix. The focal relationship is: Two independent gates: valid supported premises before arithmetic and required entry conditions after it. Missing any Yes/No destination or confusing feasible with observed delivery invalidates the image. Arrows mean only the stated dependency or classification, never automatic approval. No decorative connectors or slide-overlay space; this is an inline course figure.

4. Verbatim label map
Title, top zone: CALCULATION IS NOT FEASIBILITY
Permitted labels in their composition-assigned nodes, strips or branches:
- Source values
- Units
- Premises supported?
- UNSUPPORTED → HOLD
- Visible operation
- Independent result
- Required entry conditions met?
- Counterfactual ≠ observed
- Feasible at this boundary
- Not observed delivery
- Do not copy the producer's result
Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Duplicate a label only where its specified branches require it. Yes and No are the only additional words allowed, solely on edges leaving a question ending in ?; every such node must have both explicitly assigned destinations. Structural step numbers are permitted only where the brief specifies numbered steps/rows.

5. Visual family
#0D0906 primary ground; #17110C panel fill; #A58650 primary gold; #C8A96A sheen and connector highlights; #C8B78A secondary readable text; #FFF8E7 primary text; #655337 subdued nonessential rules; #3A2E1B faint structural lines; #4F5634 restrained verified/allowed accents; #B43A2F warnings/blocked branches; #2D3030 neutral mechanisms. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities. Keep the same warm-earth lineage as the attached homepage references, but not their photographic subject matter.

6. Richness and legibility
Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use clean Inter/Helvetica-like sans-serif; exact filenames/tokens may use a clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density. Full-frame technical figure only; no decorative scenery.

7. Honesty and exclusions
No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Specific constraint: No arithmetic operands, arrival times, case result, or implied delivery. Never expose source IDs, protected numerical answers, sealed-change values, or the correct case verdict. These constraints are not in-image words.

8. Generation self-check
Before returning the PNG, ensure this exact relationship remains obvious: Two independent gates: valid supported premises before arithmetic and required entry conditions after it. Missing any Yes/No destination or confusing feasible with observed delivery invalidates the image. Check that the title and every permitted label appear once in the proper zone, except branch-specific repetition. Missing or misspelled labels, implicit Yes/No destinations, false approval arrows, or actual case answers make the figure unusable. Do not claim that you verified the result.


## 9. Revision requirements from review of the previous attempt
A previous generation of this figure was rejected. Generate a NEW image from this full contract and fix every defect below. All earlier blocks still govern; labels stay verbatim; add no words. Title text sits directly on the dark ground with no white bloom/haze band.

- m01-recompute-feasibility: REGENERATE — title dissolved in bloom; footer label undersized
Transcription: 'CALCULATION IS NOT FEASIBILITY'; 'Source values', 'Units' → 'Premises supported?'; Yes → 'Visible operation' → 'Independent result'; No → 'UNSUPPORTED → HOLD'; 'Do not copy the producer's result' (under the operation lane); 'Independent result' → 'Required entry conditions met?'; No → 'Counterfactual ≠ observed'; Yes → 'Feasible at this boundary' with inner footer 'Not observed delivery'. All labels are exact, the → and ≠ glyphs are correct, both questions have explicit Yes and No destinations, there are no loops and no invented numbers, and the logic matches MODULE_01_LAB.md:267-280. Defects: (1) The title sits in a near-white bloom, so off-white letters on a pale halo have very low contrast and the headline is the least legible text in the figure. Heavy red and gold fog also spreads across the canvas (banned haze). (2) 'Not observed delivery', the decisive bound on feasibility, is about 24 px in tan, below 32 px. (3) 'Feasible at this boundary' runs into its right border. Fix: regenerate with the same topology, a flat ground with no bloom, and 'Not observed delivery' at ≥32 px #FFF8E7 as a clearly attached boundary tag. Widen the feasible card so its text has an internal margin.


## 10. Global rendering corrections (apply to this image)
- Background is flat-to-subtle #0D0906 near-black with at most a faint warm vignette. NO white, grey, cream or yellow bloom/glow/haze anywhere, especially not behind the title; title text is solid #FFF8E7 on dark ground, at least 64 px from the top edge, with only a thin warm sheen.
- Do not add trailing periods or any punctuation not in the label map.
- No people, silhouettes, hands, phones, gears, shields, medals, check-mark badges, browser windows or other decorative pictograms. Nodes are text-first; generic document glyphs only where they explain containment.
- Every essential label at least 32 px in #FFF8E7 or #C8B78A; never dim tan small text.
- Olive (#4F5634) only for allowed/verified states; brick red (#B43A2F) only for blocked/HOLD/warning; neutral routes use #2D3030 with gold stroke.
````

## m01-source-authority

- Title: `AUTHORITY BELONGS TO THE CLAIM`
- Publication path: `shared/figures/m01-source-authority.png`
- Anchor: same guide, `## Source authority belongs to the claim`; replace `m01-claim-authority.svg`.
- Caption: A genuine source may still be the wrong authority for this claim, entity, route, or decision time.
- Native size: 1536×1024; published SHA-256: `1209fa7495fd0cab35b93d5c7510f3922f1771716c2956b7531d1a6a606e35a3`
- Iteration history:
  - attempt-01: full generation; session `01a1004e-6711-7af0-a8ce-e27a964f9f7c`; raw SHA-256 `0d57724a7f524681…`; superseded — review: m01-source-authority: LABEL_EDIT — 'Genuine ≠ applicable' undersized and crossed by trace
  - attempt-02: edit; session `01a10077-9f79-7e73-8e63-8c84cc5e745d`; raw SHA-256 `a1e1ccfff612e23e…`; superseded
  - attempt-03: edit; session `01a10088-6929-79b0-94c2-3b2d6d09abe9`; raw SHA-256 `d008c6bce018c2dd…`; ACCEPTED
- Final review outcome: accepted attempt-03. Final1: m01-source-authority: ACCEPT_A3 — 'Genuine ≠ applicable' now sits just below the X, right of the Warehouse box (x 594–874, y 296–323). It touches neither the red diagonal nor the gold release arrow; at 23 px cap height it meets the minimum. The five role→claim rows, Exact entity, Current version and the title are unchanged and verbatim.

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to EDIT the first attached image and save exactly ONE corrected PNG with an OPAQUE #0D0906 background (no transparency). Do not use a CLI image fallback or write code/SVG. The other attachments are STYLE references only. Return the absolute saved PNG path and no claim of verification.

CORRECTIONS (apply exactly; preserve every other relationship, label, position and color):
m01-source-authority: LABEL_EDIT_A2 — move 'Genuine ≠ applicable' off the custody lane
A2 transcription: 'AUTHORITY BELONGS TO THE CLAIM'; rows 'Warehouse'→'custody', 'Quality office'→'release', 'Fleet Engineering'→'payload', 'Road Authority'→'gate window', 'Movement Registry'→'permit status'; red diagonal from Warehouse to release crossed by a red X; 'Genuine ≠ applicable'; full-width bars 'Exact entity' and 'Current version'. All labels are exact, the ≠ sign is correct, nothing is added, and the five matches agree with MISSION_THREAD.md 'Source authority belongs to the claim'. At about 32 px (23 px cap height measured) the label now meets the size minimum, which A1 (about 26 px) does not. Defect: the brief says 'Genuine ≠ applicable sits beside the crossing'. In A2 the label sits at roughly x 705–990, y 165–190, directly above the gold Warehouse→custody arrow and about 75 px above the X, with the gold arrow between the label and the X. At article width it reads as an annotation on the valid Warehouse→custody match, which suggests that the warehouse is not applicable for custody, the opposite of the lesson. Image-edit fix on A2: erase 'Genuine ≠ applicable' from above the Warehouse→custody arrow. Re-letter the same text, unchanged, in #FFF8E7 at ≥32 px (no wider than the current label) in the empty band between the red diagonal and the Quality office→release arrow, left-aligned just right of the Warehouse box (start x≈565, baseline y≈318). It must sit immediately below and beside the X and touch neither the red line nor the gold release arrow. Change nothing else.

The original full generation contract follows and still governs labels and composition:

$imagegen
Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

2. Lesson contract
Owning module: Module 01, Cold Lantern. Owning page: shared/MISSION_THREAD.md, section "Source authority belongs to the claim". Takeaway: “A genuine source may still be the wrong authority for this claim, entity, route, or decision time.” Intended learner action in unfamiliar work: For each unfamiliar claim, match its precise entity and current version to the source that is authorized to establish that kind of fact. Prevent this misconception: Assuming one genuine or recently updated document is authority for every adjacent claim. These are production instructions, not additional text to draw.

3. Composition
Figure category: matched authority rows. Use a 1536×1024 landscape canvas and 64 px safe margin. Place the exact title in a clear top zone; reserve the rest for the mechanism, preferably two spacious rows rather than tiny type. Reading order and spatial zones: Five horizontally aligned role-to-claim matches, separated rather than a serial workflow: Warehouse → custody; Quality office → release; Fleet Engineering → payload; Road Authority → gate window; Movement Registry → permit status. Beneath them place Exact entity and Current version as applicability filters across every row. A thin crossed connector from the warehouse end of the custody row toward release visually rejects that mismatch; Genuine ≠ applicable sits beside the crossing. Avoid implying an actual release outcome. The focal relationship is: Role-specific authority and a crossed warehouse-to-release mismatch Arrows mean only the stated dependency or classification, never automatic approval. No decorative connectors or slide-overlay space; this is an inline course figure.

4. Verbatim label map
Title, top zone: AUTHORITY BELONGS TO THE CLAIM
Permitted labels in their composition-assigned nodes, strips or branches:
- Warehouse → custody
- Quality office → release
- Fleet Engineering → payload
- Road Authority → gate window
- Movement Registry → permit status
- Exact entity
- Current version
- Genuine ≠ applicable
Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Duplicate a label only where its specified branches require it. Yes and No are the only additional words allowed, solely on edges leaving a question ending in ?; every such node must have both explicitly assigned destinations. Structural step numbers are permitted only where the brief specifies numbered steps/rows.

5. Visual family
#0D0906 primary ground; #17110C panel fill; #A58650 primary gold; #C8A96A sheen and connector highlights; #C8B78A secondary readable text; #FFF8E7 primary text; #655337 subdued nonessential rules; #3A2E1B faint structural lines; #4F5634 restrained verified/allowed accents; #B43A2F warnings/blocked branches; #2D3030 neutral mechanisms. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities. Keep the same warm-earth lineage as the attached homepage references, but not their photographic subject matter.

6. Richness and legibility
Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use clean Inter/Helvetica-like sans-serif; exact filenames/tokens may use a clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density. Full-frame technical figure only; no decorative scenery.

7. Honesty and exclusions
No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Specific constraint: Never imply warehouse custody establishes lot release or a source applies to another route or entity. Never expose source IDs, protected numerical answers, sealed-change values, or the correct case verdict. These constraints are not in-image words.

8. Generation self-check
Before returning the PNG, ensure this exact relationship remains obvious: Role-specific authority and a crossed warehouse-to-release mismatch; all five matches and the entity/version filters must be legible. Check that the title and every permitted label appear once in the proper zone, except branch-specific repetition. Missing or misspelled labels, implicit Yes/No destinations, false approval arrows, or actual case answers make the figure unusable. Do not claim that you verified the result.
````

## m01-statement-types

- Title: `SEPARATE FIVE KINDS OF CLAIM`
- Publication path: `shared/figures/m01-statement-types.png`
- Anchor: same guide, `## Five kinds of statement`; replace `m01-statement-kinds.svg`.
- Caption: Split a mixed sentence until each material statement has one kind and its own support.
- Native size: 1536×1024; published SHA-256: `2c3af36e899a3a53a4a76bcd80fa703e8c8fb3c8ab80dd3d2f390f8fb3e15db6`
- Iteration history:
  - attempt-01: full generation; session `01a1004f-55ae-7662-b7a2-a39c728152ba`; raw SHA-256 `b3421d4c29d11d0f…`; superseded — review: m01-statement-types: REGENERATE — green→red border ramp turns five kinds into a ranked ladder
  - attempt-02: full generation; session `01a10077-896c-79d1-9ca3-125a666baf30`; raw SHA-256 `99414cb762e594ad…`; ACCEPTED
- Final review outcome: accepted attempt-02. F01b: m01-statement-types: ACCEPT_A2 — 'SEPARATE FIVE KINDS OF CLAIM' plus five neutral, identically styled cards with exact pairs (SOURCE FACT/Applicable source states it; CALCULATION/Supported values + units; INFERENCE/Interpretation + reason; DECISION/Named human owner; UNSUPPORTED/No adequate support). The unlabeled document glyph fans out to all five with no ranking color ramp. 'One kind per row' is off-white at about 35 px. Pairs match MISSION_THREAD.md 'Five kinds of statement'.

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

2. Lesson contract
Owning module: Module 01, Cold Lantern. Owning page: shared/MISSION_THREAD.md, section "Five kinds of statement". Takeaway: “Split a mixed sentence until each material statement has one kind and its own support.” Intended learner action in unfamiliar work: For a new brief, separate a compound assertion and demand the appropriate warrant for each resulting statement. Prevent this misconception: Treating an inference, decision, or unsupported assertion as a directly sourced fact. These are production instructions, not additional text to draw.

3. Composition
Figure category: five-way classification. Use a 1536×1024 landscape canvas and 64 px safe margin. Place the exact title in a clear top zone; reserve the rest for the mechanism, preferably two spacious rows rather than tiny type. Reading order and spatial zones: Place one unlabeled compound-statement glyph above five parallel cards, not an ascending ladder. Pair each kind with precisely its own support in five aligned rows: SOURCE FACT / Applicable source states it; CALCULATION / Supported values + units; INFERENCE / Interpretation + reason; DECISION / Named human owner; UNSUPPORTED / No adequate support. Bottom strip One kind per row. The split is classification, never a flow to approval. The focal relationship is: A compound statement splits into distinct kinds, each requiring its own support Arrows mean only the stated dependency or classification, never automatic approval. No decorative connectors or slide-overlay space; this is an inline course figure.

4. Verbatim label map
Title, top zone: SEPARATE FIVE KINDS OF CLAIM
Permitted labels in their composition-assigned nodes, strips or branches:
- SOURCE FACT
- Applicable source states it
- CALCULATION
- Supported values + units
- INFERENCE
- Interpretation + reason
- DECISION
- Named human owner
- UNSUPPORTED
- No adequate support
- One kind per row
Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Duplicate a label only where its specified branches require it. Yes and No are the only additional words allowed, solely on edges leaving a question ending in ?; every such node must have both explicitly assigned destinations. Structural step numbers are permitted only where the brief specifies numbered steps/rows.

5. Visual family
#0D0906 primary ground; #17110C panel fill; #A58650 primary gold; #C8A96A sheen and connector highlights; #C8B78A secondary readable text; #FFF8E7 primary text; #655337 subdued nonessential rules; #3A2E1B faint structural lines; #4F5634 restrained verified/allowed accents; #B43A2F warnings/blocked branches; #2D3030 neutral mechanisms. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities. Keep the same warm-earth lineage as the attached homepage references, but not their photographic subject matter.

6. Richness and legibility
Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use clean Inter/Helvetica-like sans-serif; exact filenames/tokens may use a clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density. Full-frame technical figure only; no decorative scenery.

7. Honesty and exclusions
No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Specific constraint: Never imply that a calculation, inference, or AI draft grants decision authority. Never expose source IDs, protected numerical answers, sealed-change values, or the correct case verdict. These constraints are not in-image words.

8. Generation self-check
Before returning the PNG, ensure this exact relationship remains obvious: A compound statement splits into distinct kinds, each requiring its own support; five kinds and five exact paired warrants must be visible, with no ladder to approval. Check that the title and every permitted label appear once in the proper zone, except branch-specific repetition. Missing or misspelled labels, implicit Yes/No destinations, false approval arrows, or actual case answers make the figure unusable. Do not claim that you verified the result.


## 9. Revision requirements from review of the previous attempt
A previous generation of this figure was rejected. Generate a NEW image from this full contract and fix every defect below. All earlier blocks still govern; labels stay verbatim; add no words. Title text sits directly on the dark ground with no white bloom/haze band.

- m01-statement-types: REGENERATE — green→red border ramp turns five kinds into a ranked ladder
Transcription: 'SEPARATE FIVE KINDS OF CLAIM'; one unlabeled document glyph with a five-segment color bar; rows 'SOURCE FACT | Applicable source states it', 'CALCULATION | Supported values + units', 'INFERENCE | Interpretation + reason', 'DECISION | Named human owner', 'UNSUPPORTED | No adequate support'; bottom strip 'One kind per row'. All labels are exact, appear once, and nothing is added. The pairings are consistent with MISSION_THREAD.md:77-87. Defects: (1) The card borders run olive (SOURCE FACT, the palette's 'verified' accent) through gold and brown to brick red (UNSUPPORTED, the 'blocked' accent), and the glyph's color bar repeats that ramp. That encodes a quality ranking from fact down to failure, which the brief forbids ('not a ladder'). It also dims DECISION into the weakest-looking brown card, so status is carried only by color. (2) 'One kind per row' is dim tan type at about 26–28 px, below the 32 px minimum, and it does not pass the 'never dim essential words' rule. Fix: regenerate with all five cards in one neutral gold stroke (#A58650) and identical fills. If UNSUPPORTED keeps a brick-red accent, that is the only status color. Remove the colored segments from the glyph, or make them neutral and identical. Render the bottom strip 'One kind per row' in #FFF8E7 at ≥34 px.


## 10. Global rendering corrections (apply to this image)
- Background is flat-to-subtle #0D0906 near-black with at most a faint warm vignette. NO white, grey, cream or yellow bloom/glow/haze anywhere, especially not behind the title; title text is solid #FFF8E7 on dark ground, at least 64 px from the top edge, with only a thin warm sheen.
- Do not add trailing periods or any punctuation not in the label map.
- No people, silhouettes, hands, phones, gears, shields, medals, check-mark badges, browser windows or other decorative pictograms. Nodes are text-first; generic document glyphs only where they explain containment.
- Every essential label at least 32 px in #FFF8E7 or #C8B78A; never dim tan small text.
- Olive (#4F5634) only for allowed/verified states; brick red (#B43A2F) only for blocked/HOLD/warning; neutral routes use #2D3030 with gold stroke.
````

## m01-supported-verdict

- Title: `MAKE THE VERDICT REOPENABLE`
- Publication path: `shared/figures/m01-supported-verdict.png`
- Anchor: Lab `## 8. Write the corrected internal brief`; replace `m01-verdict-packet.svg`.
- Caption: A defensible verdict names its evidence, blockers, uncertainty, and next evidence; a producer's rebuttal is not independent verification.
- Native size: 1536×1024; published SHA-256: `4b8f99fee84d09f12975f20c22d6aa935de9e81b5e0222e925de4d1e3acc627c`
- Iteration history:
  - attempt-01: full generation; session `01a10050-3d1d-7a42-bab6-b89224c7d156`; raw SHA-256 `62091a79562dbfab…`; superseded — review: m01-supported-verdict: REGENERATE — producer rebuttal routed into the evidence-link node
  - attempt-02: full generation; session `01a1007a-9f21-7391-852b-46945b0bde06`; raw SHA-256 `465f0fe5255a5251…`; ACCEPTED
- Final review outcome: accepted attempt-02. F01b: m01-supported-verdict: ACCEPT_A2 — 'Producer rebuttal = another claim' now feeds the Supported/Contradicted/Unresolved classification as a claim to inspect, not the evidence links. The three categories converge through 'Exact sources + calculations' into a 'Class-only decision' box holding an unselected 'ACCEPT / REVISE / REJECT / HOLD', with 'Current blockers' and 'Next evidence + owner'. Unresolved routes to the owner. Labels are exact with nothing added, and this agrees with MODULE_01_LAB.md:335 and §8.

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

2. Lesson contract
Owning module: Module 01, Cold Lantern. Owning page: shared/MODULE_01_LAB.md, section "8. Write the corrected internal brief". Takeaway: “A defensible verdict names its evidence, blockers, uncertainty, and next evidence; a producer's rebuttal is not independent verification.” Intended learner action in unfamiliar work: When reviewing an unfamiliar AI-produced recommendation, keep supporting and conflicting evidence traceable and name the owner who can resolve what remains open. Prevent this misconception: Treating producer rebuttal as independent proof or a proposed verdict as operational permission. These are production instructions, not additional text to draw.

3. Composition
Figure category: convergent evidence packet. Use a 1536×1024 landscape canvas and 64 px safe margin. Place the exact title in a clear top zone; reserve the rest for the mechanism, preferably two spacious rows rather than tiny type. Reading order and spatial zones: Supported, Contradicted and Unresolved occupy three separate upper branches. They converge only through Exact sources + calculations into a central bounded decision field ACCEPT / REVISE / REJECT / HOLD, with no option preselected. Under the decision field place Current blockers and Next evidence + owner; unresolved evidence must route to that owner. Producer rebuttal = another claim returns to the evidence-inspection side, not into a proof or approval node. Bound all decision material with Class-only decision. The focal relationship is: Evidence categories and exact links lead to an unselected bounded verdict Arrows mean only the stated dependency or classification, never automatic approval. No decorative connectors or slide-overlay space; this is an inline course figure.

4. Verbatim label map
Title, top zone: MAKE THE VERDICT REOPENABLE
Permitted labels in their composition-assigned nodes, strips or branches:
- Supported
- Contradicted
- Unresolved
- Exact sources + calculations
- ACCEPT / REVISE / REJECT / HOLD
- Current blockers
- Next evidence + owner
- Producer rebuttal = another claim
- Class-only decision
Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Duplicate a label only where its specified branches require it. Yes and No are the only additional words allowed, solely on edges leaving a question ending in ?; every such node must have both explicitly assigned destinations. Structural step numbers are permitted only where the brief specifies numbered steps/rows.

5. Visual family
#0D0906 primary ground; #17110C panel fill; #A58650 primary gold; #C8A96A sheen and connector highlights; #C8B78A secondary readable text; #FFF8E7 primary text; #655337 subdued nonessential rules; #3A2E1B faint structural lines; #4F5634 restrained verified/allowed accents; #B43A2F warnings/blocked branches; #2D3030 neutral mechanisms. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities. Keep the same warm-earth lineage as the attached homepage references, but not their photographic subject matter.

6. Richness and legibility
Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use clean Inter/Helvetica-like sans-serif; exact filenames/tokens may use a clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density. Full-frame technical figure only; no decorative scenery.

7. Honesty and exclusions
No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Specific constraint: Never choose the case verdict, endorse movement, propose a route, infer permit approval, or imply clinic receipt. Never expose source IDs, protected numerical answers, sealed-change values, or the correct case verdict. These constraints are not in-image words.

8. Generation self-check
Before returning the PNG, ensure this exact relationship remains obvious: Evidence categories and exact links lead to an unselected bounded verdict; unresolved items retain owner and next evidence, and producer rebuttal is explicitly a claim to inspect. Check that the title and every permitted label appear once in the proper zone, except branch-specific repetition. Missing or misspelled labels, implicit Yes/No destinations, false approval arrows, or actual case answers make the figure unusable. Do not claim that you verified the result.


## 9. Revision requirements from review of the previous attempt
A previous generation of this figure was rejected. Generate a NEW image from this full contract and fix every defect below. All earlier blocks still govern; labels stay verbatim; add no words. Title text sits directly on the dark ground with no white bloom/haze band.

- m01-supported-verdict: REGENERATE — producer rebuttal routed into the evidence-link node
Transcription: 'MAKE THE VERDICT REOPENABLE'; 'Supported', 'Contradicted', 'Unresolved' → 'Exact sources + calculations' → bounded field 'Class-only decision' containing 'ACCEPT / REVISE / REJECT / HOLD' (none preselected), 'Current blockers', 'Next evidence + owner'; Unresolved also routes directly to Next evidence + owner; 'Producer rebuttal = another claim' arrows into 'Exact sources + calculations'. All labels are exact and appear once; nothing is added. Defects: (1) The rebuttal's arrow ends in 'Exact sources + calculations', the node that carries the verdict's evidence links straight into the decision field. Visually the rebuttal becomes one of the exact sources behind the verdict, which contradicts MODULE_01_LAB.md:335 ('produce claims for you to inspect; neither makes the producer an independent verifier') and the takeaway. (2) The title sits in a white bloom with low contrast and fog surrounds every panel (banned haze). Fix: regenerate with the rebuttal box at the upper left, its trace returning to the top of the Supported / Contradicted / Unresolved classification row (entering above those three cards as an item to be classified), never touching 'Exact sources + calculations' or the decision field. Use a flat ground with no title bloom.


## 10. Global rendering corrections (apply to this image)
- Background is flat-to-subtle #0D0906 near-black with at most a faint warm vignette. NO white, grey, cream or yellow bloom/glow/haze anywhere, especially not behind the title; title text is solid #FFF8E7 on dark ground, at least 64 px from the top edge, with only a thin warm sheen.
- Do not add trailing periods or any punctuation not in the label map.
- No people, silhouettes, hands, phones, gears, shields, medals, check-mark badges, browser windows or other decorative pictograms. Nodes are text-first; generic document glyphs only where they explain containment.
- Every essential label at least 32 px in #FFF8E7 or #C8B78A; never dim tan small text.
- Olive (#4F5634) only for allowed/verified states; brick red (#B43A2F) only for blocked/HOLD/warning; neutral routes use #2D3030 with gold stroke.
````

## m01-thread-handoffs

- Title: `A RESULT DEPENDS ON EVERY HANDOFF`
- Publication path: `shared/figures/m01-thread-handoffs.png`
- Anchor: `shared/MISSION_THREAD.md`, `## What a mission thread is`; replace `m01-eight-steps.svg`.
- Caption: Evidence must support each required handoff to the decision point; expected arrival does not establish delivery or usable effect.
- Native size: 1536×1024; published SHA-256: `1704b6eab0fea3776eaecf2c243d6ddf2099bd25b736dd6d2a3d1741ff934cc4`
- Iteration history:
  - attempt-01: full generation; session `01a10051-2958-7220-9da8-708c9bcdbbe9`; raw SHA-256 `e24cadcb61931c49…`; superseded — review: m01-thread-handoffs: REGENERATE — title bloom and invisible step-6 decision boundary
  - attempt-02: full generation; session `01a10076-96f2-7192-9d51-cf5a15d7f1bf`; raw SHA-256 `6994ffb6718dace6…`; ACCEPTED
- Final review outcome: accepted attempt-02. F01b: m01-thread-handoffs: ACCEPT_A2 — 'A RESULT DEPENDS ON EVERY HANDOFF', nodes 1–8 exact and in the MISSION_THREAD.md order, 'Output meets next entry condition' on the 4→5 continuation, red 'Not yet observed' bracket under 7–8, and a solid gold vertical boundary between 6 and 7 (the step-6 GO decision point). No checks or extra words, flat dark ground, every label legible. The boundary crossing the 6→7 arrow marks the decision point and does not signal a passed check.

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

2. Lesson contract
Owning module: Module 01, Cold Lantern. Owning page: shared/MISSION_THREAD.md, section "What a mission thread is". Takeaway: “Evidence must support each required handoff to the decision point; expected arrival does not establish delivery or usable effect.” Intended learner action in unfamiliar work: In unfamiliar work, identify each output and test whether it meets the next entry condition before claiming a result. Prevent this misconception: Mistaking an ordered plan or expected arrival for observed completion. These are production instructions, not additional text to draw.

3. Composition
Figure category: horizontal-flow. Use a 1536×1024 landscape canvas and 64 px safe margin. Place the exact title in a clear top zone; reserve the rest for the mechanism, preferably two spacious rows rather than tiny type. Reading order and spatial zones: Top mechanism row: numbered nodes 1 Requirement defined → 2 Cargo received → 3 Cargo released → 4 Vehicle made ready. Continue unmistakably downward from node 4 into the second row, then left-to-right nodes 5 Movement authorized → 6 Route window met → 7 Cargo delivered → 8 Usable effect confirmed. Put Output meets next entry condition prominently across the inter-row handoff boundary, without interrupting node sequence. Bracket nodes 7 and 8 as Not yet observed. Arrows signify required handoffs, not passed checks; no green checks or confirmation status. The focal relationship is: The output-to-next-entry-condition test, and distinction between the decision boundary and unobserved later events. All eight nodes and continuation arrow are mandatory Arrows mean only the stated dependency or classification, never automatic approval. No decorative connectors or slide-overlay space; this is an inline course figure.

4. Verbatim label map
Title, top zone: A RESULT DEPENDS ON EVERY HANDOFF
Permitted labels in their composition-assigned nodes, strips or branches:
- Requirement defined
- Cargo received
- Cargo released
- Vehicle made ready
- Movement authorized
- Route window met
- Cargo delivered
- Usable effect confirmed
- Output meets next entry condition
- Not yet observed
Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Duplicate a label only where its specified branches require it. Yes and No are the only additional words allowed, solely on edges leaving a question ending in ?; every such node must have both explicitly assigned destinations. Structural step numbers are permitted only where the brief specifies numbered steps/rows.

5. Visual family
#0D0906 primary ground; #17110C panel fill; #A58650 primary gold; #C8A96A sheen and connector highlights; #C8B78A secondary readable text; #FFF8E7 primary text; #655337 subdued nonessential rules; #3A2E1B faint structural lines; #4F5634 restrained verified/allowed accents; #B43A2F warnings/blocked branches; #2D3030 neutral mechanisms. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities. Keep the same warm-earth lineage as the attached homepage references, but not their photographic subject matter.

6. Richness and legibility
Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use clean Inter/Helvetica-like sans-serif; exact filenames/tokens may use a clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density. Full-frame technical figure only; no decorative scenery.

7. Honesty and exclusions
No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Specific constraint: Never imply any eight steps passed or delivery/usable effect occurred. Never expose source IDs, protected numerical answers, sealed-change values, or the correct case verdict. These constraints are not in-image words.

8. Generation self-check
Before returning the PNG, ensure this exact relationship remains obvious: The output-to-next-entry-condition test, and distinction between the decision boundary and unobserved later events. All eight nodes and continuation arrow are mandatory; missing either later-event bracket or handoff condition makes it unusable. Check that the title and every permitted label appear once in the proper zone, except branch-specific repetition. Missing or misspelled labels, implicit Yes/No destinations, false approval arrows, or actual case answers make the figure unusable. Do not claim that you verified the result.


## 9. Revision requirements from review of the previous attempt
A previous generation of this figure was rejected. Generate a NEW image from this full contract and fix every defect below. All earlier blocks still govern; labels stay verbatim; add no words. Title text sits directly on the dark ground with no white bloom/haze band.

- m01-thread-handoffs: REGENERATE — title bloom and invisible step-6 decision boundary
Transcription: 'A RESULT DEPENDS ON EVERY HANDOFF'; 1 'Requirement defined'; 2 'Cargo received'; 3 'Cargo released'; 4 'Vehicle made ready'; 'Output meets next entry condition' (on the 4→5 continuation connector); 5 'Movement authorized'; 6 'Route window met'; 7 'Cargo delivered'; 8 'Usable effect confirmed'; 'Not yet observed' (red bracket under 7–8). Every label is present, spelled correctly, and appears once; nothing extra; the step numbers are permitted. The node order matches MISSION_THREAD.md:16 and the continuation arrow is clear. Defects: (1) The title sits in a large white bloom, and a bright fog washes over the upper third. The bracket and 'Not yet observed' have a strong red glow. Both violate the 'not neon … cinematic haze' rule, and the bloom lowers title contrast. (2) The self-check requires the decision boundary to stand out from the unobserved later events. MISSION_THREAD.md:31 puts the GO decision at step 6, but the only marker between nodes 6 and 7 is a faint dashed vertical hairline that is invisible at article width. Fix: regenerate with the same layout and labels, a flat warm ground with no bloom behind the title or bracket, and a clearly drawn vertical boundary rule between nodes 6 and 7 (solid #A58650 stroke, full row height, no new words). Make sure the boundary does not cross the 6→7 arrow so that it reads as a passed gate.


## 10. Global rendering corrections (apply to this image)
- Background is flat-to-subtle #0D0906 near-black with at most a faint warm vignette. NO white, grey, cream or yellow bloom/glow/haze anywhere, especially not behind the title; title text is solid #FFF8E7 on dark ground, at least 64 px from the top edge, with only a thin warm sheen.
- Do not add trailing periods or any punctuation not in the label map.
- No people, silhouettes, hands, phones, gears, shields, medals, check-mark badges, browser windows or other decorative pictograms. Nodes are text-first; generic document glyphs only where they explain containment.
- Every essential label at least 32 px in #FFF8E7 or #C8B78A; never dim tan small text.
- Olive (#4F5634) only for allowed/verified states; brick red (#B43A2F) only for blocked/HOLD/warning; neutral routes use #2D3030 with gold stroke.
````

