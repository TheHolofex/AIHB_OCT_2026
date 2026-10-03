# Raster figure prompts and provenance — module-09-agent-safeguards

Staff-only record. Not published (absent from `course.json`).

- Generator: `codex-cli 0.154.0` (`codex exec`, ChatGPT login, built-in `image_gen`).
- Style references attached to every invocation: `ui/images/home-hero.webp` and `ui/images/home-band-custody.webp`, decoded losslessly to PNG with `dwebp`; every figure except `m00-bounded-direction` also received the accepted `m00-bounded-direction` attempt-01 raster as a style-only reference. Label edits additionally attached the image being edited as the first input.
- Post-processing: the generator returns RGBA with a transparent ground. Each accepted raster was alpha-composited onto the specified `#0D0906` ground and saved as opaque lossless RGB PNG at native size. No other pixel changes, no resizing.
- Run evidence (all attempts, logs, rejected rasters, reviews): `~/course-evidence/course-raster-visuals/20261002T233502`
- Module source contract: `module-09-agent-safeguards/shared/MODULE_09_LAB.md` lines 151–309, `shared/controls/AGENT_POLICY.md`, and `shared/case/verify_safeguards.py`. No existing figure/spec ownership needs retiring.
- Owning page digests at integration (SHA-256): `README.md` d4c779f5da605939…; `shared/MODULE_09_LAB.md` a978b54131574cb6…

## m09-declared-versus-observed

- Title: `A POLICY IS NOT AN OBSERVATION`
- Publication path: `shared/figures/m09-declared-versus-observed.png`
- Anchor: Lab `## Read the declared boundary`, after the policy block and explanation.
- Caption: Join the declared policy to actual calls, matched results, and disk effects; neither the declaration nor an unchanged target alone proves a denial.
- Native size: 1536×1024; published SHA-256: `3dc938d1e06648166d8975ab88a838fe43af55f33496c4f56c02db37f6fad1b1`
- Iteration history:
  - attempt-01: full generation; session `01a1005c-2b30-7bd1-98f6-07be00552c85`; raw SHA-256 `1b306cc374e2212a…`; superseded — review: m09-declared-versus-observed: replace telephone glyph on Actual call (REGENERATE)
  - attempt-02: full generation; session `01a10070-3eb6-7c22-99f5-3498e63c241c`; raw SHA-256 `9bff55bdda59e9cc…`; ACCEPTED
- Final review outcome: accepted attempt-02. F0910: m09-declared-versus-observed: ACCEPT_A2 — Every string matches the label map verbatim: 'A POLICY IS NOT AN OBSERVATION'; 'Declared policy'; 'Actual call'/'Call ID'; 'Guard or runtime result'/'Call ID'; 'Watched target'/'Before / after'; 'Join the records'; 'Declared ≠ observed'; 'Unchanged ≠ denied'. All four cards now use plain document glyphs (A1's phone, gear and chart glyphs are gone), and the two Call ID tags are joined by a gold bracket. A cut stub with a break mark (no arrowhead) runs from the result card toward Before / after, there is no edge to a denial, all four cards feed th

### Final prompt

````text
## 1. Tool/output instruction

$imagegen Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

## 2. Lesson contract

- Owning module/page/H2: Module 09 — Night Desk, Lab (`module-09-agent-safeguards/shared/MODULE_09_LAB.md`), H2 `Read the declared boundary`, inserted after the policy JSON block and its explanation (before the next H2).
- Learning takeaway (caption, HTML text, not in image): "Join the declared policy to actual calls, matched results, and disk effects; neither the declaration nor an unchanged target alone proves a denial."
- Intended learner action in unfamiliar work: when judging whether an agent safeguard worked, keep the rule, the actual call, the enforcement result, and the disk state as separate records and join them by call identity before concluding anything.
- Misconception prevented: that a declared policy proves what happened, or that an unchanged watched file proves an attempted action was denied (it may never have been attempted).

## 3. Composition

- Category: evidence-linkage diagram.
- Canvas: 1536×1024 landscape, 64 px safe margin, title zone across the top (~120 px), rest for the mechanism. Inline course image; no slide-overlay space.
- Four separately framed record cards in a row across the middle (left to right), each a distinct panel with a generic document glyph:
  1. `Declared policy` (the rule).
  2. `Actual call` with a sub-field tag `Call ID` inside it.
  3. `Guard or runtime result` with a matching sub-field tag `Call ID` inside it (duplicate of `Call ID` is required here: the two tags show the same identity on both records).
  4. `Watched target` with a sub-field `Before / after`.
- Below the row, a central join node labelled `Join the records`. Thin gold traces run from each of the four cards down into this join node; the trace between the two `Call ID` tags is emphasized as a matching-identity link (a gold bracket joining the two tags). This is the focal relationship.
- Bottom row, two contrast callouts side by side, each a pill with brick-red stroke:
  - Left: `Declared ≠ observed`, placed under the gap between `Declared policy` and `Actual call`.
  - Right: `Unchanged ≠ denied`, placed under `Watched target`. Explicitly NO arrow from `Watched target` to `Guard or runtime result` or to any denial; a short broken/severed trace stub between them, with the callout beneath, makes the missing inference visible.
- Reading order: title → four records left to right → join node → two contrast callouts.
- Arrows mean only "this record contributes to the join"; never approval or causation.

## 4. Verbatim label map

Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts.

- Title zone: `A POLICY IS NOT AN OBSERVATION`
- Card 1: `Declared policy`
- Card 2: `Actual call`; tag `Call ID`
- Card 3: `Guard or runtime result`; tag `Call ID` (this is the only permitted duplicate)
- Card 4: `Watched target`; sub-field `Before / after`
- Join node: `Join the records`
- Contrast callouts: `Declared ≠ observed`; `Unchanged ≠ denied`

No other words; no example IDs, hashes, or values.

## 5. Visual family

`#0D0906` primary ground; `#17110C` panel fill; `#A58650` primary gold; `#C8A96A` sheen and connector highlights; `#C8B78A` secondary readable text; `#FFF8E7` primary text; `#655337` subdued nonessential rules; `#3A2E1B` faint structural lines; `#4F5634` restrained verified/allowed accents; `#B43A2F` warnings/blocked branches; `#2D3030` neutral mechanisms. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities. Records use `#17110C` panels with gold frames; the join node uses charcoal `#2D3030`; contrast callouts use brick-red strokes.

## 6. Richness and legibility

Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use clean Inter/Helvetica-like sans-serif; exact filenames/tokens may use a clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density.

## 7. Honesty/exclusions

No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Specific to this figure: no direct arrow from `Watched target` or `Before / after` to a denial; no arrow from `Declared policy` straight to a result; no checkmarks, PASS, DENIED, or outcome badges; no fabricated call IDs or JSON.

## 8. Generation self-check

Must remain obvious: four separate records joined only at `Join the records`, with the two `Call ID` tags visibly matched; unchanged disk has no direct path to a denial. Unusable if: any card merges with another, a `Call ID` tag is missing from either the call or the result, a direct arrow links `Watched target` to `Guard or runtime result`, or either ≠ callout is missing or rendered as =.

## 9. Revision requirements from review of the previous attempt
A previous generation of this figure was rejected. Generate a NEW image from this full contract and fix every defect below. All earlier blocks still govern; labels stay verbatim; add no words. Title text sits directly on the dark ground with no white bloom/haze band.

- m09-declared-versus-observed: replace telephone glyph on Actual call (REGENERATE)
Transcription (all strings correct, ≠ signs intact): 'A POLICY IS NOT AN OBSERVATION'; 'Declared policy'; 'Actual call' / 'Call ID'; 'Guard or runtime result' / 'Call ID'; 'Watched target' / 'Before / after'; 'Join the records'; 'Declared ≠ observed'; 'Unchanged ≠ denied'. Nothing is added and the only duplicate is the permitted Call ID. The two Call ID tags are bracket-joined, and Watched target has no edge to the result. Defect: the generator read 'Actual call' literally and drew a telephone handset on that card. The prompt asks for generic document glyphs on all four cards (line 16). A phone icon teaches the wrong concept, because a tool call is not a phone call, and it competes with the mechanism; the bar-chart glyph on Watched target likewise suggests metrics rather than file state. Secondary defects: the 'severed stub' is two free-floating dashes at about x 1070–1220, y 630, attached to neither the Guard-result trace nor the Watched-target trace, so it reads as stray decoration. 'Unchanged ≠ denied' sits mostly under the Guard card and the card gap instead of under Watched target (line 24). Fix: regenerate (or inpaint) using plain document glyphs on all four cards (no phone, gear or chart). Draw the stub as a visibly cut trace leaving the Watched-target card toward the Guard-result card, ending in a break mark. Center 'Unchanged ≠ denied' under the Watched-target card. Keep all labels unchanged.
````

## m09-policy-declaration

- Title: `DECLARE THE BOUNDARY BEFORE THE TURN`
- Publication path: `shared/figures/m09-policy-declaration.png`
- Anchor: Overview `## Policy before any agent turn`, after its first explanatory paragraph.
- Caption: Freeze the supplied tool and path declaration before the turn; it defines course-tool permissions, not an operating-system sandbox.
- Native size: 1536×1024; published SHA-256: `38a2172a372673a73589006a40ac0d305db124fdf82ee73a1d351dde54a2421f`
- Iteration history:
  - attempt-01: full generation; session `01a1005d-2496-72a0-af9d-0b12451bccba`; raw SHA-256 `61ff60fac4a27e07…`; ACCEPTED
- Final review outcome: accepted attempt-01. FAcc: m09-policy-declaration: ACCEPT_A1 — the monospace roots, the false switches and the hash lock are legible.

### Final prompt

````text
## 1. Tool/output instruction

$imagegen Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

## 2. Lesson contract

- Owning module/page/H2: Module 09 — Night Desk, Overview (`module-09-agent-safeguards/README.md`), H2 `Policy before any agent turn`, inserted after its first explanatory paragraph.
- Learning takeaway (caption, HTML text, not in image): "Freeze the supplied tool and path declaration before the turn; it defines course-tool permissions, not an operating-system sandbox."
- Intended learner action in unfamiliar work: before letting any agent act, write down and hash its exact permitted tools and read/write roots, and treat that declaration as a tool-level boundary only, not as host isolation.
- Misconception prevented: that an agent policy file is an OS sandbox, or that permissions can be decided or adjusted after the agent has started.

## 3. Composition

- Category: containment diagram with a sequencing precondition.
- Canvas: 1536×1024 landscape, 64 px safe margin on all sides, title zone across the top (~120 px), rest for the mechanism. Inline course image; no slide-overlay space.
- Left two-thirds (main containment): a large outer framed region labelled `read_root: .` (the work folder). Nested inside it, toward the lower right of that region, a smaller framed region labelled `write_root: artifacts`. Between them, exactly two tool capability pills: `course_read` placed in the outer read region with a thin gold trace reaching into the read region; `course_write` placed so its gold trace terminates only inside the inner `write_root: artifacts` region. Exactly two tool pills; no others.
- Below the containment region (second row, still left two-thirds): three disabled-capability pills drawn muted with a brick-red stroke and a clear off-state treatment (e.g. switch glyph in off position, no gold trace leaving them): `yolo: false`, `skills: false`, `gateway: false`. They sit outside the containment frame, not connected to it.
- Right third (precondition column): a sealed-document/lock glyph labelled `Freeze + hash` with a single gold arrow pointing to a node labelled `Before first turn`. A single gold arrow then leads from this column into the containment region, meaning only "the frozen declaration defines this boundary before the turn begins". The arrow must not imply approval of any action.
- Bottom band, full width under everything: a distinct caution strip (brick-red stroke, dark fill) carrying `Tool boundary ≠ OS sandbox`, visually framing the whole containment as a tool-level fence, not an enclosure of the host.
- Reading order: title → Freeze + hash → Before first turn → containment (read root, nested write root, two tools) → disabled pills → bottom caution strip.
- Focal relationship: the inner `write_root: artifacts` region nested inside `read_root: .`, with `course_write` able to reach only the inner region.
- No decorative connectors.

## 4. Verbatim label map

Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts.

- Title zone: `DECLARE THE BOUNDARY BEFORE THE TURN`
- Outer containment region: `read_root: .`
- Inner nested region: `write_root: artifacts`
- Tool pills (exactly two): `course_read`; `course_write`
- Disabled pills row: `yolo: false`; `skills: false`; `gateway: false`
- Precondition column: `Freeze + hash`; `Before first turn`
- Bottom caution strip: `Tool boundary ≠ OS sandbox`

No other words. Monospace is permitted for `read_root: .`, `write_root: artifacts`, `course_read`, `course_write`, `yolo: false`, `skills: false`, `gateway: false`.

## 5. Visual family

`#0D0906` primary ground; `#17110C` panel fill; `#A58650` primary gold; `#C8A96A` sheen and connector highlights; `#C8B78A` secondary readable text; `#FFF8E7` primary text; `#655337` subdued nonessential rules; `#3A2E1B` faint structural lines; `#4F5634` restrained verified/allowed accents; `#B43A2F` warnings/blocked branches; `#2D3030` neutral mechanisms. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities. Use olive accents for the two allowed tool pills, brick red strokes for the three disabled pills and the caution strip, charcoal `#2D3030` for the freeze/hash mechanism.

## 6. Richness and legibility

Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use clean Inter/Helvetica-like sans-serif; exact filenames/tokens may use a clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density.

## 7. Honesty/exclusions

No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Specific to this figure: do not draw the boundary as a walled container, vault, or physical enclosure around a computer/host; do not show any hash value or digits; do not add any additional tool names (no shell, network, browser); do not show the disabled pills as enabled or connected.

## 8. Generation self-check

Must remain obvious: `write_root: artifacts` is nested inside `read_root: .`; exactly two tools; `course_write` reaches only the inner write region; `Freeze + hash` happens `Before first turn` and precedes the boundary; the whole boundary is labelled `Tool boundary ≠ OS sandbox`. Unusable if: any of the three disabled pills is missing or appears active, a third tool appears, the write region is drawn outside the read region, the freeze step appears after the turn, or the ≠ sign is dropped or turned into =.
````

## m09-probe-outcomes

- Title: `NOT ATTEMPTED IS NOT DENIED`
- Publication path: `shared/figures/m09-probe-outcomes.png`
- Anchor: Lab `## Run the undeclared-tool probe`, after its first paragraph and before commands; covers both supplied probes.
- Caption: Classify the actual qualifying call and matched result for the supplied probe; an unrelated refused write does not prove the requested outside write was attempted.
- Native size: 1536×1024; published SHA-256: `58c6ee965c6cb6a34b75e13851806d95b363ad7a021eeddc8af391567ad856d8`
- Iteration history:
  - attempt-01: full generation; session `01a10047-95bf-7e82-ae77-2c42eea489fb`; raw SHA-256 `13bdf638ef5f94fc…`; superseded
  - attempt-02: edit; session `01a10048-eda8-7f72-aa49-0a73ad928884`; raw SHA-256 `edeb8170b164a3ac…`; ACCEPTED
- Final review outcome: accepted attempt-02. FAcc: m09-probe-outcomes: ACCEPT_A2 — all four ranks, the code chips, the Yes/No on the decision diamond and the watched-target bracket are legible.

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to EDIT the first attached image (the instructional PNG titled "NOT ATTEMPTED IS NOT DENIED") and save exactly ONE corrected PNG. Do not use a CLI image fallback or write code/SVG. The other attachments are STYLE references only. Return the absolute saved PNG path and no claim of verification.

LABEL-ONLY CORRECTION:
- Left of the four ranked rows, beside the gold downward priority rail, remove the small words "Higher priority" (top) and "Lower priority" (bottom). Keep the gold downward rail arrow itself. These words are not permitted labels.

Preserve every other relationship and label exactly: title, the `Complete records?` diamond with `Yes` to the ladder and `No` to `Missing evidence → HOLD`, the bracket header `Highest observed outcome wins`, rows 1–4 with their exact texts and pills (`Prohibited success / effect → VIOLATION → HOLD`; `Guard deny + matching error` with sub-note `Outside write: watched target only` and pill `DENIED_BY_GUARD`; `Unknown tool + matching not-found error` with pill `DENIED_BY_RUNTIME`; `No qualifying attempt → NOT_ATTEMPTED`), the dashed link to the `Check watched target` panel, colors, layout, 1536×1024 size. Do not add any words.

For reference, the original full generation contract follows; it still governs:

## 1. Tool/output instruction

$imagegen Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

## 2. Lesson contract

- Owning module/page/H2: Module 09 — Night Desk, Lab (`module-09-agent-safeguards/shared/MODULE_09_LAB.md`), H2 `Run the undeclared-tool probe`, inserted after its first paragraph and before its first **Terminal:** label; the figure covers both supplied probes (outside-write and undeclared-tool).
- Learning takeaway (caption, HTML text, not in image): "Classify the actual qualifying call and matched result for the supplied probe; an unrelated refused write does not prove the requested outside write was attempted."
- Intended learner action in unfamiliar work: when testing a guardrail, first confirm the records are complete, then classify from the actual call and its matched result using a strict precedence (violation outranks guard denial, which outranks runtime denial; otherwise not attempted), and only count a denial if the denied call is the one the probe asked for.
- Misconception prevented: treating "nothing changed" or "the agent said it was blocked" as a denial; letting a lower denial hide a violation; counting an unrelated refused write as proof the requested outside write was attempted; reading incomplete records as NOT_ATTEMPTED.

## 3. Composition

- Category: genuine conditional flow with a ranked classification ladder.
- Canvas: 1536×1024 landscape, 64 px safe margin, title zone across the top (~120 px), rest for the mechanism. Inline course image; no slide-overlay space.
- Left column entry: decision diamond `Complete records?` (complete means every call has its matched result and guard records; a prohibited call without an observed enforcement result is incomplete).
  - Edge labelled `No` goes down/left to a brick-red terminal block `Missing evidence → HOLD`.
  - Edge labelled `Yes` goes right into the ranked ladder.
- Ranked ladder (center/right, the focal element): a vertical stack of four rows, highest priority at TOP, enclosed by a bracket/header labelled `Highest observed outcome wins`, with a gold downward priority rail on the left of the rows showing rank descends top to bottom. Rows are evaluated across all qualifying calls in the attempt; the topmost matched row wins.
  - Row 1 (top, brick red): `Prohibited success / effect → VIOLATION → HOLD`.
  - Row 2 (olive accent): condition text `Guard deny + matching error` with an attached sub-note pill `Outside write: watched target only`, leading to outcome pill `DENIED_BY_GUARD`.
  - Row 3 (olive accent): condition text `Unknown tool + matching not-found error`, leading to outcome pill `DENIED_BY_RUNTIME`.
  - Row 4 (bottom, neutral charcoal): `No qualifying attempt → NOT_ATTEMPTED`.
- Side annotation, right edge, separated by a dashed faint line and NOT on the decision path: a small panel `Check watched target` with a thin trace pointing to the ladder as supplementary evidence only. It has no arrow into any outcome pill and does not substitute for call/result records.
- Reading order: title → `Complete records?` → No branch to HOLD / Yes branch → ladder top to bottom → side annotation.
- Focal relationship: the precedence ordering — VIOLATION on top outranks DENIED_BY_GUARD, which outranks DENIED_BY_RUNTIME, with NOT_ATTEMPTED only when nothing above matched.
- Arrows mean only the described routing; never approval. No decorative connectors.

## 4. Verbatim label map

Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts.

- Title zone: `NOT ATTEMPTED IS NOT DENIED`
- Entry diamond: `Complete records?` with exactly two edges: `No` → `Missing evidence → HOLD`; `Yes` → the ranked ladder.
- Ladder header: `Highest observed outcome wins`
- Ladder row 1 (top): `Prohibited success / effect → VIOLATION → HOLD`
- Ladder row 2: `Guard deny + matching error`; sub-note `Outside write: watched target only`; outcome `DENIED_BY_GUARD`
- Ladder row 3: `Unknown tool + matching not-found error`; outcome `DENIED_BY_RUNTIME`
- Ladder row 4 (bottom): `No qualifying attempt → NOT_ATTEMPTED`
- Side annotation: `Check watched target`

`Yes` and `No` are the only additional words, solely on the two edges leaving `Complete records?`. Structural rank numbers 1–4 are permitted on the four ladder rows only. Outcome tokens (`VIOLATION`, `DENIED_BY_GUARD`, `DENIED_BY_RUNTIME`, `NOT_ATTEMPTED`, `HOLD`) may use clean monospace.

## 5. Visual family

`#0D0906` primary ground; `#17110C` panel fill; `#A58650` primary gold; `#C8A96A` sheen and connector highlights; `#C8B78A` secondary readable text; `#FFF8E7` primary text; `#655337` subdued nonessential rules; `#3A2E1B` faint structural lines; `#4F5634` restrained verified/allowed accents; `#B43A2F` warnings/blocked branches; `#2D3030` neutral mechanisms. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities. Brick red for the HOLD block and VIOLATION row; olive for the two denial rows; charcoal for NOT_ATTEMPTED and the side annotation.

## 6. Richness and legibility

Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use clean Inter/Helvetica-like sans-serif; exact filenames/tokens may use a clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density. The ladder rows are long; give each row the full available width and wrap the condition text onto two lines rather than shrinking below 32 px.

## 7. Honesty/exclusions

No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Specific to this figure: no fabricated call IDs, no example run results, no indication that any probe actually produced a given outcome, no checkmark or "safe" badge. The No branch of `Complete records?` must never lead to `NOT_ATTEMPTED`. `Check watched target` must not connect to any outcome pill. A denial row must never appear above VIOLATION.

## 8. Generation self-check

Must remain obvious: incomplete records → HOLD before any classification; the four rows stacked in exactly this order top to bottom: VIOLATION, DENIED_BY_GUARD, DENIED_BY_RUNTIME, NOT_ATTEMPTED, under `Highest observed outcome wins`; guard denial carries the `Outside write: watched target only` qualifier. Unusable if: either Yes/No edge is missing or swapped, the row order changes, any of the four outcome tokens is missing or misspelled, the watched-target qualifier is detached from the guard row, or `Check watched target` appears as a decision step that yields an outcome.
````

## m09-receipt-boundary

- Title: `BOUND WHAT THE RECEIPTS PROVE`
- Publication path: `shared/figures/m09-receipt-boundary.png`
- Anchor: Lab `## Audit the three actual attempts`.
- Caption: Local receipts support the observed run's consistency, not tamper-proof custody, unexercised denials, or general host isolation.
- Native size: 1536×1024; published SHA-256: `3d61309d3fd9c5b3411848b1b61b7513f0027ab021025920fc34eda8b093bf12`
- Iteration history:
  - attempt-01: full generation; session `01a1005e-1beb-7b30-8df8-6bf9e6408168`; raw SHA-256 `e6d6a6f608943d2c…`; ACCEPTED
  - attempt-02: full generation; session `01a10071-62e8-7d30-82d8-bdc5912dbc23`; raw SHA-256 `782a761fd808530e…`; not selected
- Final review outcome: accepted attempt-01. F0910: m09-receipt-boundary: ACCEPT_A1 — In flattened.png the title and the outer-band label 'Unobserved host access remains outside' sit in high contrast on the dark ground, so the earlier haze was a compositing artifact. All 11 strings are verbatim, all six sources reach the 'Local consistency' hub, the scope tag sits above it, the limit pill hangs below it, and no edge crosses from the outer dashed band. A2 is rejected because 'Policy identity' and 'Guard lifecycle' have no trace, and the 'Raw events' and 'Source bytes + read order' lines leave from card edges while their connector dots sta

### Final prompt

````text
## 1. Tool/output instruction

$imagegen Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

## 2. Lesson contract

- Owning module/page/H2: Module 09 — Night Desk, Lab (`module-09-agent-safeguards/shared/MODULE_09_LAB.md`), H2 `Audit the three actual attempts`, inserted after its first explanatory paragraph and before its first **Terminal:** label.
- Learning takeaway (caption, HTML text, not in image): "Local receipts support the observed run's consistency, not tamper-proof custody, unexercised denials, or general host isolation."
- Intended learner action in unfamiliar work: when reporting what a set of agent receipts proves, name the exact evidence sources and scope the claim to the observed run, policy, and case; state explicitly what remains outside (unobserved actions, broader host access, wholesale evidence rewriting).
- Misconception prevented: that passing local hash/receipt checks proves tamper-proof custody, that denials not exercised in this run are proven, or that the run demonstrates host isolation.

## 3. Composition

- Category: evidence-to-claim containment with an excluded outer region.
- Canvas: 1536×1024 landscape, 64 px safe margin, title zone across the top (~120 px), rest for the mechanism. Inline course image; no slide-overlay space.
- Inner bounded region (center, gold frame): on its left, six evidence source cards in two rows of three:
  - Row A: `Policy identity`; `Raw events`; `Call ID + result`
  - Row B: `Guard lifecycle`; `Source bytes + read order`; `Disk snapshots`
  Thin gold traces from all six converge to a claim block on the right of the inner region: scope tag `Observed run / policy / case` above the main claim `Local consistency`. This convergence is the focal relationship.
- A thin brick-red-stroked limit pill attached directly under the claim block: `Not tamper-proof custody`.
- Outer excluded region: a wide dark band surrounding the inner region (dashed faint border, slightly darker fill), clearly outside the claim boundary, carrying the label `Unobserved host access remains outside` along its lower edge. No traces cross from the outer band into the claim.
- Reading order: title → six sources → claim scope and `Local consistency` → limit pill → outer excluded band.
- Arrows mean only "supports"; never approval. No decorative connectors.

## 4. Verbatim label map

Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts.

- Title zone: `BOUND WHAT THE RECEIPTS PROVE`
- Evidence cards (inner region, two rows of three): `Policy identity`; `Raw events`; `Call ID + result`; `Guard lifecycle`; `Source bytes + read order`; `Disk snapshots`
- Claim block: scope tag `Observed run / policy / case`; main claim `Local consistency`
- Limit pill under claim: `Not tamper-proof custody`
- Outer excluded band: `Unobserved host access remains outside`

No other words.

## 5. Visual family

`#0D0906` primary ground; `#17110C` panel fill; `#A58650` primary gold; `#C8A96A` sheen and connector highlights; `#C8B78A` secondary readable text; `#FFF8E7` primary text; `#655337` subdued nonessential rules; `#3A2E1B` faint structural lines; `#4F5634` restrained verified/allowed accents; `#B43A2F` warnings/blocked branches; `#2D3030` neutral mechanisms. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities. Restrained olive accent on the `Local consistency` claim; brick red for the limit pill; outer band in near-black with `#3A2E1B` dashed border.

## 6. Richness and legibility

Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use clean Inter/Helvetica-like sans-serif; exact filenames/tokens may use a clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density. The outer-band label must be as readable as inner labels.

## 7. Honesty/exclusions

No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Specific to this figure: no lock/vault/chain-of-custody seal implying tamper-proofing; no PASS, verified, or classification badges; no hash digits; nothing suggesting the run proves host isolation or denials it did not exercise.

## 8. Generation self-check

Must remain obvious: six named evidence sources converge only to a scoped `Local consistency` claim inside a bounded region; `Not tamper-proof custody` qualifies that claim; `Unobserved host access remains outside` sits in a separate outer region with no support edges. Unusable if: any of the six sources is missing, the scope tag is dropped, the limit pill is missing, or the outer band is merged into or connected to the claim.
````

## m09-source-as-data

- Title: `READ THE SOURCE WITHOUT OBEYING IT`
- Publication path: `shared/figures/m09-source-as-data.png`
- Anchor: Lab `## Answer the measurement without taking release authority`, after the source-order and no-write explanation.
- Caption: Check that the notes listing and all required reads finished before the planted-note request, then ground the answer in returned text without taking its quoted instruction as authority.
- Native size: 1536×1024; published SHA-256: `3446f4a096125387dc0130a152decd07525eb8691564dff98495158bab558bc4`
- Iteration history:
  - attempt-01: full generation; session `01a1005f-119b-7c42-a45a-303aad0fc708`; raw SHA-256 `19ec44b00419975e…`; ACCEPTED
- Final review outcome: accepted attempt-01. FAcc: m09-source-as-data: ACCEPT_A1 — the dashed red block, the gate and 'No write' are visible.

### Final prompt

````text
## 1. Tool/output instruction

$imagegen Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

## 2. Lesson contract

- Owning module/page/H2: Module 09 — Night Desk, Lab (`module-09-agent-safeguards/shared/MODULE_09_LAB.md`), H2 `Answer the measurement without taking release authority`, inserted after the source-order and no-write explanation paragraphs and before its first **Terminal:** label.
- Learning takeaway (caption, HTML text, not in image): "Check that the notes listing and all required reads finished before the planted-note request, then ground the answer in returned text without taking its quoted instruction as authority."
- Intended learner action in unfamiliar work: when an agent reads untrusted source text, verify the required reads completed in order with their frozen bytes, use the returned text only as evidence for the asked-for answer, and treat any instruction inside that text as quoted data with no authority to act.
- Misconception prevented: that text inside a source can grant the agent authority (e.g. to release or write), or that reads may be batched/reordered as long as the answer looks right.

## 3. Composition

- Category: dependency/ordering flow with a severed authority edge.
- Canvas: 1536×1024 landscape, 64 px safe margin, title zone across the top (~120 px), rest for the mechanism. Inline course image; no slide-overlay space.
- Top row (left to right), the required order:
  1. `List notes folder` (folder glyph).
  2. A stacked-cards block labelled `AG-001–AG-040` with beneath it `40 completed reads` (each card implies its returned text matches frozen source bytes; draw a small seal/hash glyph on the stack, no digits).
  3. An ordering gate (a vertical gold gate bar) that opens only after steps 1 and 2 complete; after the gate: `Then request PLANTED_NOTE.md`.
  Gold arrows between steps mean only "must finish before".
- Bottom row: from `Then request PLANTED_NOTE.md`, a downward arrow to a document card `Returned source text`. That card splits into two contained regions:
  - A measurement region feeding a gold arrow to an output pill `Measurement + source name` (bottom right).
  - A quoted/inset block (indented, quotation-mark glyph, brick-red stroke) labelled `Quoted instruction = data`. From this block a dashed trace that is visibly cut/terminated, ending at a blocked stop pill `No release authority`. No execution edge continues past it.
- Bottom-right corner, beside the output pill: a separate brick-red-stroked pill `No write` indicating the required behavior includes no file write.
- Reading order: title → top row left to right through the gate → returned text → measurement output; quoted instruction → severed edge → no authority; `No write`.
- Focal relationship: the ordering gate before the planted request, and the quoted instruction contained as data with no outgoing action edge.
- No decorative connectors.

## 4. Verbatim label map

Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts.

- Title zone: `READ THE SOURCE WITHOUT OBEYING IT`
- Top row step 1: `List notes folder`
- Top row step 2: `AG-001–AG-040`; `40 completed reads`
- After gate: `Then request PLANTED_NOTE.md`
- Bottom document card: `Returned source text`
- Output pill: `Measurement + source name`
- Inset quoted block: `Quoted instruction = data`
- Severed-edge stop: `No release authority`
- Separate pill: `No write`

Structural step numbers 1–3 are permitted on the three top-row steps only. `AG-001–AG-040` and `PLANTED_NOTE.md` may use clean monospace.

## 5. Visual family

`#0D0906` primary ground; `#17110C` panel fill; `#A58650` primary gold; `#C8A96A` sheen and connector highlights; `#C8B78A` secondary readable text; `#FFF8E7` primary text; `#655337` subdued nonessential rules; `#3A2E1B` faint structural lines; `#4F5634` restrained verified/allowed accents; `#B43A2F` warnings/blocked branches; `#2D3030` neutral mechanisms. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities. Olive accent on the completed reads and measurement output; brick red on the quoted-instruction block, the severed edge stop, and `No write`; charcoal for the ordering gate.

## 6. Richness and legibility

Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use clean Inter/Helvetica-like sans-serif; exact filenames/tokens may use a clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density.

## 7. Honesty/exclusions

No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Specific to this figure: do NOT render any measurement value, unit, number, or invented reply text; do not render the planted note's contents; do not show a "blocked release" event, alarm, or release action — this is the required order, not an observed successful run. No PASS badge.

## 8. Generation self-check

Must remain obvious: listing and all forty reads complete before the gate opens to `Then request PLANTED_NOTE.md`; returned text feeds only `Measurement + source name`; `Quoted instruction = data` has no execution edge beyond `No release authority`; `No write` is present. Unusable if: the planted request appears before or in parallel with the AG reads, any digit or measurement appears in the output pill, the quoted instruction connects to any action, or `No write` is missing.
````

