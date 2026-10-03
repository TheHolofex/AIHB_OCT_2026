# Raster figure prompts and provenance — module-00-setup

Staff-only record. Not published (absent from `course.json`).

- Generator: `codex-cli 0.154.0` (`codex exec`, ChatGPT login, built-in `image_gen`).
- Style references attached to every invocation: `ui/images/home-hero.webp` and `ui/images/home-band-custody.webp`, decoded losslessly to PNG with `dwebp`; every figure except `m00-bounded-direction` also received the accepted `m00-bounded-direction` attempt-01 raster as a style-only reference. Label edits additionally attached the image being edited as the first input.
- Post-processing: the generator returns RGBA with a transparent ground. Each accepted raster was alpha-composited onto the specified `#0D0906` ground and saved as opaque lossless RGB PNG at native size. No other pixel changes, no resizing.
- Run evidence (all attempts, logs, rejected rasters, reviews): `~/course-evidence/course-raster-visuals/20261002T233502`
- Module source contract: `module-00-setup/README.md` §§When a step fails, Ready means observable, Set up local Obsidian, Local n8n readiness; `shared/MODULE_00_LAB.md` steps 2–14. The screen's exact questions and direction's precedence/falsifier are at lab lines 181–220. Setup is a prerequisite, not the new mastery.
- Owning page digests at integration (SHA-256): `README.md` 135dbf25f46744e1…; `shared/MODULE_00_LAB.md` e1a3e794d5051dad…

## m00-bounded-direction

- Title: `MAKE THE JOB TESTABLE`
- Publication path: `shared/figures/m00-bounded-direction.png`
- Anchor: Lab `## 6. Freeze a testable direction`, after the first paragraph. Remove the old `m00-delegation.svg` block from step 4 while retaining its factual delegation prose.
- Caption: Give the model a limited drafting job, name the evidence that could defeat acceptance, and keep consequential decisions with their owner.
- Native size: 1536×1024; published SHA-256: `d7d607497455f2dccde9cec315ac2f180104f0a630a59520bb1543fd7a88a30d`
- Iteration history:
  - attempt-01: full generation; session `01a10045-fd38-7412-8767-62a40d0a1751`; raw SHA-256 `c1afccd6bcee3a94…`; ACCEPTED
- Final review outcome: accepted attempt-01. FAcc: m00-bounded-direction: ACCEPT_A1 — all text is legible on the dark ground and no element was lost in flattening.

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

2. LESSON CONTRACT
Module 00 — North Shelf; Lab / 6. Freeze a testable direction; 4. Divide drafting, judgment, and prohibited action. Learning takeaway/caption: “Give the model a limited drafting job, name the evidence that could defeat acceptance, and keep consequential decisions with their owner.” Intended learner action in unfamiliar work: For an unfamiliar assignment, write the allowed work, precedence, observable acceptance and falsifier before a model run. Common misconception to prevent: A helpful model sentence overrides the packet or moves an acceptance decision to the model. These instructions are not extra in-image words.

3. COMPOSITION
Produce an original diagram-first raster instructional figure, 1536×1024 landscape, 64 px safe margin. Place the title in a dedicated top zone and give the remaining area to the actual mechanism; prefer two spacious rows over tiny type. Category and reading order: three upper responsibility compartments feed a bounded-direction frame below; the frame is a constraint specification, not an approval flow. Exact nodes and relationships: Upper row has three discrete compartments AI: draft supplied facts; Person: interpret and decide; Refuse: external action. Their vertical constraints meet a large central bounded-direction frame. Inside its two lower rows: Outcome + audience, Allowed sources + constraints, Precedence; Acceptance condition, Falsifier, Stop condition, Decision owner. Freeze before the run is the frame footer. Highlight packet/source precedence conceptually without inventing a source label or an approval arrow. Make the stated distinction the focal relationship, not a decorative list. Arrows mean only the explicit relationship specified here, never automatic approval; no decorative connectors and no slide-overlay space. This is an inline course image readable at normal article width.

4. VERBATIM LABEL MAP
Title zone: `MAKE THE JOB TESTABLE`.
Required visible labels, each exactly once unless a specified branch expressly requires repetition:
- `AI: draft supplied facts`
- `Person: interpret and decide`
- `Refuse: external action`
- `Outcome + audience`
- `Allowed sources + constraints`
- `Precedence`
- `Acceptance condition`
- `Falsifier`
- `Stop condition`
- `Decision owner`
- `Freeze before the run`
Placement and connection map: Upper row has three discrete compartments AI: draft supplied facts; Person: interpret and decide; Refuse: external action. Their vertical constraints meet a large central bounded-direction frame. Inside its two lower rows: Outcome + audience, Allowed sources + constraints, Precedence; Acceptance condition, Falsifier, Stop condition, Decision owner. Freeze before the run is the frame footer. Highlight packet/source precedence conceptually without inventing a source label or an approval arrow.
Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Duplicate a label only where its specified branches require it. `Yes` and `No` are the only additional words allowed, solely on edges leaving a question ending in `?`; every such node must have both explicitly assigned destinations. Structural step numbers are permitted only where the brief specifies numbered steps/rows. Do not print block headings, explanatory prose, caption, page name or art instructions inside the image.

5. VISUAL FAMILY
Exact palette: #0D0906 primary ground; #17110C panel fill; #A58650 primary gold; #C8A96A sheen and connector highlights; #C8B78A secondary readable text; #FFF8E7 primary text; #655337 subdued nonessential rules; #3A2E1B faint structural lines; #4F5634 restrained verified/allowed accents; #B43A2F warnings/blocked branches; #2D3030 neutral mechanisms. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities. Match the existing site’s warm near-black, sandstone, gold-trace operational visual family; adapt its palette, not the reference photographs’ subjects, scene composition or no-text constraint.

6. RICHNESS AND LEGIBILITY
Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use clean Inter/Helvetica-like sans-serif; exact filenames/tokens may use a clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density. Keep each essential relationship and full label legible at article width; distribute dense cells over the canvas.

7. HONESTY AND EXCLUSIONS
No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. No automatic approval from completion of the brief; do not imply a request or helpful closing supplies missing release authority or that the AI can decide use.

8. GENERATION SELF-CHECK
Before returning the PNG path, check that every title and required label is present verbatim, no extra visible words appear, and the relationship is unmistakable: The source-precedence and falsifier cells must both be legible while retained human judgment stays separate from model drafting and external action remains refused; missing any responsibility compartment makes this unusable. If any required label or branch is absent, revise the image rather than claiming it is verified. This internal generation check does not replace a later visual inspection.
````

## m00-change-isolation

- Title: `CHANGE ONLY WHAT DEPENDS ON IT`
- Publication path: `shared/figures/m00-change-isolation.png`
- Anchor: Lab `## 13. Predict and apply the changed input`.
- Caption: Predict the changed fact's effects before rerunning, preserve unrelated constraints, and explain the original checker's stale-count failure.
- Native size: 1536×1024; published SHA-256: `ca7b79ea8af534f0d8f2efde06f5f883fb435759098ff591850269c24b741e4e`
- Iteration history:
  - attempt-01: full generation; session `01a10049-da4f-7720-a56b-d3b301f666e7`; raw SHA-256 `f41ae8e792bfaafa…`; superseded — review: m00-change-isolation: tone down title bloom; replace magnifier
  - attempt-02: edit; session `01a10076-8a5b-7190-a35b-ed8c535c2baf`; raw SHA-256 `26c1003cf9fb30c9…`; ACCEPTED
- Final review outcome: accepted attempt-02. F00: m00-change-isolation: ACCEPT_A2 — all 8 labels and the title match the label map exactly, with no counts shown; baseline → Predict first → One changed fact forks and rejoins only at Compare both drafts; a separate red branch runs from the revised draft to the unaltered old checker → Do not edit away the failure; the magnifier is removed; flattened ground is clean (the A1/A2 labels and layout are otherwise identical).

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to EDIT the first attached image and save exactly ONE corrected PNG. Do not use a CLI image fallback or write code/SVG. The other attachments are STYLE references only. Return the absolute saved PNG path and no claim of verification.

LABEL-LEVEL CORRECTIONS (apply exactly; preserve every other relationship and label):
- m00-change-isolation: tone down title bloom; replace magnifier
LABEL_EDIT. Transcription: CHANGE ONLY WHAT DEPENDS ON IT; Preserve baseline; Predict first; One changed fact; Dependent statements change; Other constraints stay fixed; Compare both drafts; Original checker still expects old count; Do not edit away the failure. Every label is exact, and no counts are revealed. Structure matches the brief and lab step 13: baseline → prediction → changed fact, then a fork that converges only at Compare both drafts. A separate red branch runs from the revised draft through an unlabeled document glyph to the stale checker → Do not edit away the failure, and the checker is not altered. Defects: the title sits in a white bloom band, with weaker contrast than the pilot. A heavy red smoke haze also fills the left-center. The magnifier on Predict first is a search/inspect metaphor, not a prediction, and is decorative per §7. Fix: re-render the title zone on the near-black ground with a mild glow, remove the red fog (keep the red traces and box strokes), and delete the magnifier glyph from Predict first, centering the label. No connector changes.

The original full generation contract follows and still governs labels and composition:

$imagegen
Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

2. LESSON CONTRACT
Module 00 — North Shelf; Lab / 13. Predict and apply the changed input; 14. Check and compare the two drafts. Learning takeaway/caption: “Predict the changed fact’s effects before rerunning, preserve unrelated constraints, and explain the original checker’s stale-count failure.” Intended learner action in unfamiliar work: In unfamiliar change requests, freeze the first version, predict dependencies, revise only affected statements and explain a now-stale check without editing it. Common misconception to prevent: A changed count also changes authority, audience or unrelated facts; or an old checker’s mismatch should be edited away. These instructions are not extra in-image words.

3. COMPOSITION
Produce an original diagram-first raster instructional figure, 1536×1024 landscape, 64 px safe margin. Place the title in a dedicated top zone and give the remaining area to the actual mechanism; prefer two spacious rows over tiny type. Category and reading order: baseline-plus-prediction before changed input; dependency fork and a separate stale-checker evidence branch. Exact nodes and relationships: Top reading order Preserve baseline → Predict first → One changed fact. Fork into Dependent statements change versus Other constraints stay fixed; converge only at Compare both drafts. A separate checker branch from the revised draft leads to Original checker still expects old count and Do not edit away the failure. Keep original and changed drafts visually distinct without adding labels. Make the stated distinction the focal relationship, not a decorative list. Arrows mean only the explicit relationship specified here, never automatic approval; no decorative connectors and no slide-overlay space. This is an inline course image readable at normal article width.

4. VERBATIM LABEL MAP
Title zone: `CHANGE ONLY WHAT DEPENDS ON IT`.
Required visible labels, each exactly once unless a specified branch expressly requires repetition:
- `Preserve baseline`
- `Predict first`
- `One changed fact`
- `Dependent statements change`
- `Other constraints stay fixed`
- `Compare both drafts`
- `Original checker still expects old count`
- `Do not edit away the failure`
Placement and connection map: Top reading order Preserve baseline → Predict first → One changed fact. Fork into Dependent statements change versus Other constraints stay fixed; converge only at Compare both drafts. A separate checker branch from the revised draft leads to Original checker still expects old count and Do not edit away the failure. Keep original and changed drafts visually distinct without adding labels.
Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Duplicate a label only where its specified branches require it. `Yes` and `No` are the only additional words allowed, solely on edges leaving a question ending in `?`; every such node must have both explicitly assigned destinations. Structural step numbers are permitted only where the brief specifies numbered steps/rows. Do not print block headings, explanatory prose, caption, page name or art instructions inside the image.

5. VISUAL FAMILY
Exact palette: #0D0906 primary ground; #17110C panel fill; #A58650 primary gold; #C8A96A sheen and connector highlights; #C8B78A secondary readable text; #FFF8E7 primary text; #655337 subdued nonessential rules; #3A2E1B faint structural lines; #4F5634 restrained verified/allowed accents; #B43A2F warnings/blocked branches; #2D3030 neutral mechanisms. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities. Match the existing site’s warm near-black, sandstone, gold-trace operational visual family; adapt its palette, not the reference photographs’ subjects, scene composition or no-text constraint.

6. RICHNESS AND LEGIBILITY
Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use clean Inter/Helvetica-like sans-serif; exact filenames/tokens may use a clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density. Keep each essential relationship and full label legible at article width; distribute dense cells over the canvas.

7. HONESTY AND EXCLUSIONS
No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Do not disclose old or new count; do not infer new release, pickup, sharing or other authority from the changed fact.

8. GENERATION SELF-CHECK
Before returning the PNG path, check that every title and required label is present verbatim, no extra visible words appear, and the relationship is unmistakable: Prediction must precede input, dependency branch must leave unrelated constraints unchanged, and stale checker failure must be explained rather than erased; omit all numerical case counts. If any required label or branch is absent, revise the image rather than claiming it is verified. This internal generation check does not replace a later visual inspection.


## 10. Global rendering corrections (apply to this image)
- Background is flat-to-subtle #0D0906 near-black with at most a faint warm vignette. NO white, grey, cream or yellow bloom/glow/haze anywhere, especially not behind the title; title text is solid #FFF8E7 on dark ground, at least 64 px from the top edge, with only a thin warm sheen.
- Do not add trailing periods or any punctuation not in the label map.
- No people, silhouettes, hands, phones, gears, shields, medals, check-mark badges, browser windows or other decorative pictograms. Nodes are text-first; generic document glyphs only where they explain containment.
- Every essential label at least 32 px in #FFF8E7 or #C8B78A; never dim tan small text.
- Olive (#4F5634) only for allowed/verified states; brick red (#B43A2F) only for blocked/HOLD/warning; neutral routes use #2D3030 with gold stroke.
````

## m00-claim-check

- Title: `TRACE THE CLAIM, NOT THE CONFIDENCE`
- Publication path: `shared/figures/m00-claim-check.png`
- Anchor: Lab `## 9. Trace material claims yourself`.
- Caption: A source can support the stated fact without supporting the action a reader might infer from it.
- Native size: 1536×1024; published SHA-256: `05448aeb48fe46367e970a9cca84d37d40f1c18a8bb2a9796c1c3ac2100d601e`
- Iteration history:
  - attempt-01: full generation; session `01a1004a-bbe3-74f3-8703-5cb73d40f4e9`; raw SHA-256 `13a6c89d9cf93958…`; superseded — review: m00-claim-check: remove person pictogram and decorative icons
  - attempt-02: full generation; session `01a10074-933c-7163-9299-62c689dee720`; raw SHA-256 `32ac0da509fc6eb0…`; ACCEPTED
- Final review outcome: accepted attempt-02. F00: m00-claim-check: ACCEPT_A2 — title and all 8 labels exact, comma spacing correct; Material claim → Source + locator → Quoted support forks to Establishes / Does not establish; a dashed red bar (not a validating arrow) blocks Unsupported implication; Mechanical checks ends at Human interpretation, which takes both branches; the person, gear and other pictograms in A1 are gone.

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

2. LESSON CONTRACT
Module 00 — North Shelf; Lab / 9. Trace material claims yourself; 8. Read the disk file, count words, and check. Learning takeaway/caption: “A source can support the stated fact without supporting the action a reader might infer from it.” Intended learner action in unfamiliar work: For an unfamiliar claim, locate exact quoted support and separate the narrow fact it establishes from an unsupported consequential inference. Common misconception to prevent: A supported fact or green mechanical check supports any action a reader infers. These instructions are not extra in-image words.

3. COMPOSITION
Produce an original diagram-first raster instructional figure, 1536×1024 landscape, 64 px safe margin. Place the title in a dedicated top zone and give the remaining area to the actual mechanism; prefer two spacious rows over tiny type. Category and reading order: claim-to-locator-to-quote evidence chain with a split into warranted and unwarranted meanings; independent narrow mechanical lane. Exact nodes and relationships: Top primary chain: Material claim → Source + locator → Quoted support. From quoted support fork down to Establishes and Does not establish; the latter points to Unsupported implication, with a blocked treatment, not a validating arrow. Lower parallel lane Mechanical checks terminates before the inference and is interpreted with Human interpretation, which inspects both branches. Make the stated distinction the focal relationship, not a decorative list. Arrows mean only the explicit relationship specified here, never automatic approval; no decorative connectors and no slide-overlay space. This is an inline course image readable at normal article width.

4. VERBATIM LABEL MAP
Title zone: `TRACE THE CLAIM, NOT THE CONFIDENCE`.
Required visible labels, each exactly once unless a specified branch expressly requires repetition:
- `Material claim`
- `Source + locator`
- `Quoted support`
- `Establishes`
- `Does not establish`
- `Unsupported implication`
- `Mechanical checks`
- `Human interpretation`
Placement and connection map: Top primary chain: Material claim → Source + locator → Quoted support. From quoted support fork down to Establishes and Does not establish; the latter points to Unsupported implication, with a blocked treatment, not a validating arrow. Lower parallel lane Mechanical checks terminates before the inference and is interpreted with Human interpretation, which inspects both branches.
Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Duplicate a label only where its specified branches require it. `Yes` and `No` are the only additional words allowed, solely on edges leaving a question ending in `?`; every such node must have both explicitly assigned destinations. Structural step numbers are permitted only where the brief specifies numbered steps/rows. Do not print block headings, explanatory prose, caption, page name or art instructions inside the image.

5. VISUAL FAMILY
Exact palette: #0D0906 primary ground; #17110C panel fill; #A58650 primary gold; #C8A96A sheen and connector highlights; #C8B78A secondary readable text; #FFF8E7 primary text; #655337 subdued nonessential rules; #3A2E1B faint structural lines; #4F5634 restrained verified/allowed accents; #B43A2F warnings/blocked branches; #2D3030 neutral mechanisms. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities. Match the existing site’s warm near-black, sandstone, gold-trace operational visual family; adapt its palette, not the reference photographs’ subjects, scene composition or no-text constraint.

6. RICHNESS AND LEGIBILITY
Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use clean Inter/Helvetica-like sans-serif; exact filenames/tokens may use a clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density. Keep each essential relationship and full label legible at article width; distribute dense cells over the canvas.

7. HONESTY AND EXCLUSIONS
No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Never imply custody establishes release, a paperwork window establishes pickup, or a checker certifies meaning. No fabricated case quotes.

8. GENERATION SELF-CHECK
Before returning the PNG path, check that every title and required label is present verbatim, no extra visible words appear, and the relationship is unmistakable: The quoted support must visibly bound what it establishes and does not establish; mechanical checks cannot connect as authorization to unsupported implication; missing locator or human interpretation makes this unusable. If any required label or branch is absent, revise the image rather than claiming it is verified. This internal generation check does not replace a later visual inspection.


## 9. Revision requirements from review of the previous attempt
A previous generation of this figure was rejected. Generate a NEW image from this full contract and fix every defect below. All earlier blocks still govern; labels stay verbatim; add no words. Title text sits directly on the dark ground with no white bloom/haze band.

- m00-claim-check: remove person pictogram and decorative icons
REGENERATE. Transcription: TRACE THE CLAIM, NOT THE CONFIDENCE (the comma sits tight against N; verify the space at native size); Material claim; Source + locator; Quoted support; Establishes; Does not establish; Unsupported implication; Mechanical checks; Human interpretation. No word is added or missing. The topology matches the brief: the chain, the fork, a blocked dashed red bar from Does not establish to Unsupported implication, Mechanical checks → Human interpretation, and Human interpretation inspecting both branches. Defects: Human interpretation contains a person silhouette with a thought cloud, which the prompt's §7 forbids ('No … people/hands'). Every node also carries a decorative pictogram: document, open book with magnifier, quote bubble, gear, and document glyphs in Establishes, Does not establish and Unsupported implication. These are decoration, not containment or transformation, which §7 restricts, and they push the labels into the top third of each box. The title sits in a white bloom band (cinematic haze). Fix: regenerate with text-only nodes and no person/gear/book/thought-bubble glyphs. Optionally keep a single quote-mark accent in Quoted support. Render the title on the near-black ground with a normal space after the comma and only a mild glow. Make Mechanical checks a visibly narrower parallel lane, as the brief specifies.


## 10. Global rendering corrections (apply to this image)
- Background is flat-to-subtle #0D0906 near-black with at most a faint warm vignette. NO white, grey, cream or yellow bloom/glow/haze anywhere, especially not behind the title; title text is solid #FFF8E7 on dark ground, at least 64 px from the top edge, with only a thin warm sheen.
- Do not add trailing periods or any punctuation not in the label map.
- No people, silhouettes, hands, phones, gears, shields, medals, check-mark badges, browser windows or other decorative pictograms. Nodes are text-first; generic document glyphs only where they explain containment.
- Every essential label at least 32 px in #FFF8E7 or #C8B78A; never dim tan small text.
- Olive (#4F5634) only for allowed/verified states; brick red (#B43A2F) only for blocked/HOLD/warning; neutral routes use #2D3030 with gold stroke.
````

## m00-decision-owner

- Title: `A CHECK IS NOT AN OWNER`
- Publication path: `shared/figures/m00-decision-owner.png`
- Anchor: Lab `## 2. Identify who decides acceptance`; replace `m00-independent-accept.svg`.
- Caption: The checker reports mechanical results; a named person owns the supported decision about the email's stated use.
- Native size: 1536×1024; published SHA-256: `099a41ab4dffb0171f6bd4de6ea062e926ae7dbf26010e8f28aa02f083bfa207`
- Iteration history:
  - attempt-01: full generation; session `01a1004b-9c1c-72e1-b8e3-f5cdaf1f22da`; raw SHA-256 `0dedeac74d3586c1…`; ACCEPTED
  - attempt-02: edit; session `01a10075-b893-7f10-a753-b089d1790911`; raw SHA-256 `ef98e10a6c7ed490…`; not selected
- Final review outcome: accepted attempt-01. F00: m00-decision-owner: ACCEPT_A1 — all 9 labels exact; the checker lane and the human-review lane stay separate until Named decision owner; it branches to PASS FOR CLASS REVIEW (olive) and HOLD (red), and the bracket labelled Not operational permission spans both outcomes, matching lab steps 2 and 12; flattened ground is clean (A2 adds a visible brown haze band across the middle).

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

2. LESSON CONTRACT
Module 00 — North Shelf; Lab / 2. Identify who decides acceptance. Learning takeaway/caption: “The checker reports mechanical results; a named person owns the supported decision about the email’s stated use.” Intended learner action in unfamiliar work: In unfamiliar work, separate a practice check from interpretation and name the person authorized to decide bounded use. Common misconception to prevent: A PASS from an inspectable checker independently certifies meaning or permits real-world use. These instructions are not extra in-image words.

3. COMPOSITION
Produce an original diagram-first raster instructional figure, 1536×1024 landscape, 64 px safe margin. Place the title in a dedicated top zone and give the remaining area to the actual mechanism; prefer two spacious rows over tiny type. Category and reading order: two distinct assessment lanes converge only as evidence at a human decision boundary. Exact nodes and relationships: AI draft enters two parallel paths: Practice checker → Mechanical conditions, and Human review → Sources + meaning. Both evidence paths reach Named decision owner, who may choose PASS FOR CLASS REVIEW or HOLD. Not operational permission sits below the decision boundary, never beneath the checker alone. Make the stated distinction the focal relationship, not a decorative list. Arrows mean only the explicit relationship specified here, never automatic approval; no decorative connectors and no slide-overlay space. This is an inline course image readable at normal article width.

4. VERBATIM LABEL MAP
Title zone: `A CHECK IS NOT AN OWNER`.
Required visible labels, each exactly once unless a specified branch expressly requires repetition:
- `AI draft`
- `Practice checker`
- `Mechanical conditions`
- `Human review`
- `Sources + meaning`
- `Named decision owner`
- `PASS FOR CLASS REVIEW`
- `HOLD`
- `Not operational permission`
Placement and connection map: AI draft enters two parallel paths: Practice checker → Mechanical conditions, and Human review → Sources + meaning. Both evidence paths reach Named decision owner, who may choose PASS FOR CLASS REVIEW or HOLD. Not operational permission sits below the decision boundary, never beneath the checker alone.
Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Duplicate a label only where its specified branches require it. `Yes` and `No` are the only additional words allowed, solely on edges leaving a question ending in `?`; every such node must have both explicitly assigned destinations. Structural step numbers are permitted only where the brief specifies numbered steps/rows. Do not print block headings, explanatory prose, caption, page name or art instructions inside the image.

5. VISUAL FAMILY
Exact palette: #0D0906 primary ground; #17110C panel fill; #A58650 primary gold; #C8A96A sheen and connector highlights; #C8B78A secondary readable text; #FFF8E7 primary text; #655337 subdued nonessential rules; #3A2E1B faint structural lines; #4F5634 restrained verified/allowed accents; #B43A2F warnings/blocked branches; #2D3030 neutral mechanisms. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities. Match the existing site’s warm near-black, sandstone, gold-trace operational visual family; adapt its palette, not the reference photographs’ subjects, scene composition or no-text constraint.

6. RICHNESS AND LEGIBILITY
Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use clean Inter/Helvetica-like sans-serif; exact filenames/tokens may use a clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density. Keep each essential relationship and full label legible at article width; distribute dense cells over the canvas.

7. HONESTY AND EXCLUSIONS
No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Do not imply the checker is tamper-proof, independent acceptance authority, or a real operational approval. No scoring rubric or qualification claim.

8. GENERATION SELF-CHECK
Before returning the PNG path, check that every title and required label is present verbatim, no extra visible words appear, and the relationship is unmistakable: The mechanical and meaning paths must remain separate until the named owner, whose bounded alternatives are both visible; missing HOLD or Not operational permission makes this unusable. If any required label or branch is absent, revise the image rather than claiming it is verified. This internal generation check does not replace a later visual inspection.
````

## m00-falsifier

- Title: `TEST THE CHECK ON A COPY`
- Publication path: `shared/figures/m00-falsifier.png`
- Anchor: Lab `## 10. Make a failing copy without changing the original`.
- Caption: A rejected known-bad copy shows that this check catches that defect; it does not certify the original draft's meaning.
- Native size: 1536×1024; published SHA-256: `cdc314f7eed05f0134df730b4d14ac3163221f8b7cea87f182281f697526a4c4`
- Iteration history:
  - attempt-01: full generation; session `01a1004c-8005-7843-ad0f-f9a02c31dd98`; raw SHA-256 `7490a61b40008ed1…`; ACCEPTED
- Final review outcome: accepted attempt-01. FAcc: m00-falsifier: ACCEPT_A1 — all strings and connectors are visible on #0D0906.

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

2. LESSON CONTRACT
Module 00 — North Shelf; Lab / 10. Make a failing copy without changing the original. Learning takeaway/caption: “A rejected known-bad copy shows that this check catches that defect; it does not certify the original draft’s meaning.” Intended learner action in unfamiliar work: For an unfamiliar validation check, preserve the original bytes, introduce one known defect only in a separate copy, run that same checker and compare the original hash. Common misconception to prevent: Rejection of one deliberately bad copy proves the untouched original fully correct. These instructions are not extra in-image words.

3. COMPOSITION
Produce an original diagram-first raster instructional figure, 1536×1024 landscape, 64 px safe margin. Place the title in a dedicated top zone and give the remaining area to the actual mechanism; prefer two spacious rows over tiny type. Category and reading order: two isolated lanes: original protected by procedure, separate bad copy tested; a strict non-equivalence boundary. Exact nodes and relationships: Left stable lane Original: preserve → Record hash → Original hash unchanged, with before/after byte identity expressed by a matched abstract byte-pattern glyph (no fabricated hex). Right test lane Separate copy → One deliberate error → Same checker → Expected rejection. Bottom boundary Check sensitivity ≠ full correctness. Never connect expected rejection to an original-correct endpoint. Make the stated distinction the focal relationship, not a decorative list. Arrows mean only the explicit relationship specified here, never automatic approval; no decorative connectors and no slide-overlay space. This is an inline course image readable at normal article width.

4. VERBATIM LABEL MAP
Title zone: `TEST THE CHECK ON A COPY`.
Required visible labels, each exactly once unless a specified branch expressly requires repetition:
- `Original: preserve`
- `Record hash`
- `Separate copy`
- `One deliberate error`
- `Same checker`
- `Expected rejection`
- `Original hash unchanged`
- `Check sensitivity ≠ full correctness`
Placement and connection map: Left stable lane Original: preserve → Record hash → Original hash unchanged, with before/after byte identity expressed by a matched abstract byte-pattern glyph (no fabricated hex). Right test lane Separate copy → One deliberate error → Same checker → Expected rejection. Bottom boundary Check sensitivity ≠ full correctness. Never connect expected rejection to an original-correct endpoint.
Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Duplicate a label only where its specified branches require it. `Yes` and `No` are the only additional words allowed, solely on edges leaving a question ending in `?`; every such node must have both explicitly assigned destinations. Structural step numbers are permitted only where the brief specifies numbered steps/rows. Do not print block headings, explanatory prose, caption, page name or art instructions inside the image.

5. VISUAL FAMILY
Exact palette: #0D0906 primary ground; #17110C panel fill; #A58650 primary gold; #C8A96A sheen and connector highlights; #C8B78A secondary readable text; #FFF8E7 primary text; #655337 subdued nonessential rules; #3A2E1B faint structural lines; #4F5634 restrained verified/allowed accents; #B43A2F warnings/blocked branches; #2D3030 neutral mechanisms. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities. Match the existing site’s warm near-black, sandstone, gold-trace operational visual family; adapt its palette, not the reference photographs’ subjects, scene composition or no-text constraint.

6. RICHNESS AND LEGIBILITY
Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use clean Inter/Helvetica-like sans-serif; exact filenames/tokens may use a clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density. Keep each essential relationship and full label legible at article width; distribute dense cells over the canvas.

7. HONESTY AND EXCLUSIONS
No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. The original is preserved by procedure rather than inaccessible hardware; no invented defect count, actual hash, or certification of meaning.

8. GENERATION SELF-CHECK
Before returning the PNG path, check that every title and required label is present verbatim, no extra visible words appear, and the relationship is unmistakable: Both separate-copy rejection and unchanged original hash must be visible; the non-equivalence boundary must prevent any arrow from rejection to original correctness. If any required label or branch is absent, revise the image rather than claiming it is verified. This internal generation check does not replace a later visual inspection.
````

## m00-readiness-lanes

- Title: `READY MEANS OBSERVED`
- Publication path: `shared/figures/m00-readiness-lanes.png`
- Anchor: Overview `## Ready means observable`; replace `m00-setup-chain.svg`.
- Caption: A prerequisite report, a live tool write, and the two application checks establish different readiness claims; one does not prove the others.
- Native size: 1536×1024; published SHA-256: `b7a91c0c6ed247cbfc2a710afd8c676e239c5ca146e17e694c12c4369b16564b`
- Iteration history:
  - attempt-01: full generation; session `01a1004d-6c72-7863-a1f4-006549ae3cf2`; raw SHA-256 `8586e815b4f69548…`; superseded — review: m00-readiness-lanes: re-render bloomed title and dim footer
  - attempt-02: edit; session `01a10075-8b3b-76b2-9844-b2af3ff44bb8`; raw SHA-256 `c0e0a340c4b659a0…`; ACCEPTED
- Final review outcome: accepted attempt-02. F00: m00-readiness-lanes: ACCEPT_A2 — title and all 9 labels exact, ≠ correct; four independent lanes with no arrows between them; the PASS ≠ bar sits under the report and live lanes; Separate readiness evidence is now off-white and legible (A1 footer was dim tan).

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to EDIT the first attached image and save exactly ONE corrected PNG. Do not use a CLI image fallback or write code/SVG. The other attachments are STYLE references only. Return the absolute saved PNG path and no claim of verification.

LABEL-LEVEL CORRECTIONS (apply exactly; preserve every other relationship and label):
- m00-readiness-lanes: re-render bloomed title and dim footer
LABEL_EDIT. Transcription: READY MEANS OBSERVED; New terminal; Prerequisite report; Live OMP call; Written file; Receipt + disk readback; Setup report PASS ≠ live readiness; Obsidian: disk + GUI; n8n: stack + browser; Separate readiness evidence. All labels and the ≠ are exact, with nothing added. Structure is correct: the lanes are independent, there are no inter-lane arrows, and the PASS ≠ bar separates the report and live lanes from the application lanes. This is consistent with README 'A passing setup report does not replace the live readiness check' and the separate Obsidian and n8n READY rules. Defects: (1) the title sits in a white bloom band, so off-white text on near-white fog has low contrast, unlike the pilot. (2) 'Separate readiness evidence' is the smallest text on the canvas, in tan, set into the frame's bottom rule. It reads as a dim caption rather than the grouping label and is marginal at article width. Fix: re-render the top zone on the near-black ground with only a mild gold glow behind 'READY MEANS OBSERVED'. Re-render 'Separate readiness evidence' at ≥38 px in #FFF8E7 or #C8B78A at full contrast, centered on the bottom rule, with the rule broken around it. No other changes.

The original full generation contract follows and still governs labels and composition:

$imagegen
Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

2. LESSON CONTRACT
Module 00 — North Shelf; Overview / Ready means observable; Set up local Obsidian; Local n8n readiness for Module 7. Learning takeaway/caption: “A prerequisite report, a live tool write, and the two application checks establish different readiness claims; one does not prove the others.” Intended learner action in unfamiliar work: In unfamiliar setup, name the observation and evidence endpoint for each separate readiness claim. Common misconception to prevent: A passing setup report or one application check proves the entire environment ready. These instructions are not extra in-image words.

3. COMPOSITION
Produce an original diagram-first raster instructional figure, 1536×1024 landscape, 64 px safe margin. Place the title in a dedicated top zone and give the remaining area to the actual mechanism; prefer two spacious rows over tiny type. Category and reading order: four independent horizontal lanes in two spacious rows; left-to-right evidence within each lane; no arrow between lanes. Exact nodes and relationships: Top-left: New terminal → Prerequisite report. Top-right: Live OMP call → Written file → Receipt + disk readback. Bottom-left: Obsidian: disk + GUI. Bottom-right: n8n: stack + browser. Separate readiness evidence groups the endpoints without merging them; Setup report PASS ≠ live readiness is a prominent boundary under the first two lanes. Make the stated distinction the focal relationship, not a decorative list. Arrows mean only the explicit relationship specified here, never automatic approval; no decorative connectors and no slide-overlay space. This is an inline course image readable at normal article width.

4. VERBATIM LABEL MAP
Title zone: `READY MEANS OBSERVED`.
Required visible labels, each exactly once unless a specified branch expressly requires repetition:
- `New terminal`
- `Prerequisite report`
- `Live OMP call`
- `Written file`
- `Receipt + disk readback`
- `Obsidian: disk + GUI`
- `n8n: stack + browser`
- `Separate readiness evidence`
- `Setup report PASS ≠ live readiness`
Placement and connection map: Top-left: New terminal → Prerequisite report. Top-right: Live OMP call → Written file → Receipt + disk readback. Bottom-left: Obsidian: disk + GUI. Bottom-right: n8n: stack + browser. Separate readiness evidence groups the endpoints without merging them; Setup report PASS ≠ live readiness is a prominent boundary under the first two lanes.
Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Duplicate a label only where its specified branches require it. `Yes` and `No` are the only additional words allowed, solely on edges leaving a question ending in `?`; every such node must have both explicitly assigned destinations. Structural step numbers are permitted only where the brief specifies numbered steps/rows. Do not print block headings, explanatory prose, caption, page name or art instructions inside the image.

5. VISUAL FAMILY
Exact palette: #0D0906 primary ground; #17110C panel fill; #A58650 primary gold; #C8A96A sheen and connector highlights; #C8B78A secondary readable text; #FFF8E7 primary text; #655337 subdued nonessential rules; #3A2E1B faint structural lines; #4F5634 restrained verified/allowed accents; #B43A2F warnings/blocked branches; #2D3030 neutral mechanisms. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities. Match the existing site’s warm near-black, sandstone, gold-trace operational visual family; adapt its palette, not the reference photographs’ subjects, scene composition or no-text constraint.

6. RICHNESS AND LEGIBILITY
Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use clean Inter/Helvetica-like sans-serif; exact filenames/tokens may use a clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density. Keep each essential relationship and full label legible at article width; distribute dense cells over the canvas.

7. HONESTY AND EXCLUSIONS
No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Never portray setup report PASS as the live OMP check, disk-only Obsidian evidence as GUI observation, or a running n8n stack as proof of browser persistence.

8. GENERATION SELF-CHECK
Before returning the PNG path, check that every title and required label is present verbatim, no extra visible words appear, and the relationship is unmistakable: Each of the four lanes must end in its own evidence, with no shared all-clear path; absence of the report/live distinction or either application evidence label makes this unusable. If any required label or branch is absent, revise the image rather than claiming it is verified. This internal generation check does not replace a later visual inspection.


## 10. Global rendering corrections (apply to this image)
- Background is flat-to-subtle #0D0906 near-black with at most a faint warm vignette. NO white, grey, cream or yellow bloom/glow/haze anywhere, especially not behind the title; title text is solid #FFF8E7 on dark ground, at least 64 px from the top edge, with only a thin warm sheen.
- Do not add trailing periods or any punctuation not in the label map.
- No people, silhouettes, hands, phones, gears, shields, medals, check-mark badges, browser windows or other decorative pictograms. Nodes are text-first; generic document glyphs only where they explain containment.
- Every essential label at least 32 px in #FFF8E7 or #C8B78A; never dim tan small text.
- Olive (#4F5634) only for allowed/verified states; brick red (#B43A2F) only for blocked/HOLD/warning; neutral routes use #2D3030 with gold stroke.
````

## m00-recovery-loop

- Title: `KEEP THE FIRST ERROR`
- Publication path: `shared/figures/m00-recovery-loop.png`
- Anchor: Overview `## When a step fails`; replace `m00-recovery.svg`.
- Caption: Save the first error before changing anything, change one thing, and rerun the same check.
- Native size: 1536×1024; published SHA-256: `96dc9d8951b492fd28563164783ac1d20e49e32f617a1d525609aaabe11604fd`
- Iteration history:
  - attempt-01: full generation; session `01a1004e-5780-7b80-847e-bcbcc7061dee`; raw SHA-256 `7626064f6f7ced31…`; superseded — review: m00-recovery-loop: route Still unresolved? from Compare evidence
  - attempt-02: full generation; session `01a10072-9eb6-7f11-b06e-bd35f68e1ecf`; raw SHA-256 `ac9150d787321270…`; ACCEPTED
- Final review outcome: accepted attempt-02. F00: m00-recovery-loop: ACCEPT_A2 — all 8 labels exact; Yes/No appear only on the edges leaving Still unresolved?; First error: preserve feeds Compare evidence, then Compare evidence → Still unresolved? → Yes Use recovery guidance / No Record what changed, with no retry loop (A1's preserved-error line drops straight into the question, and Compare evidence has no outgoing edge).

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

2. LESSON CONTRACT
Module 00 — North Shelf; Overview / When a step fails. Learning takeaway/caption: “Save the first error before changing anything, change one thing, and rerun the same check.” Intended learner action in unfamiliar work: When an unfamiliar check fails, retain the initial error, isolate one change and compare the repeat observation. Common misconception to prevent: Rerunning or changing several things at once replaces the first error with useful evidence. These instructions are not extra in-image words.

3. COMPOSITION
Produce an original diagram-first raster instructional figure, 1536×1024 landscape, 64 px safe margin. Place the title in a dedicated top zone and give the remaining area to the actual mechanism; prefer two spacious rows over tiny type. Category and reading order: preserved reference beside a single correction sequence; branching question beneath comparison. Exact nodes and relationships: Left protected reference: First error: preserve and Do not overwrite the first attempt. Center path: Change one thing → Run the same check → Compare evidence, with the preserved error feeding comparison. Bottom question Still unresolved? sends Yes to Use recovery guidance and No to Record what changed. No arrow automatically returns to the check. Make the stated distinction the focal relationship, not a decorative list. Arrows mean only the explicit relationship specified here, never automatic approval; no decorative connectors and no slide-overlay space. This is an inline course image readable at normal article width.

4. VERBATIM LABEL MAP
Title zone: `KEEP THE FIRST ERROR`.
Required visible labels, each exactly once unless a specified branch expressly requires repetition:
- `First error: preserve`
- `Change one thing`
- `Run the same check`
- `Compare evidence`
- `Still unresolved?`
- `Use recovery guidance`
- `Record what changed`
- `Do not overwrite the first attempt`
Placement and connection map: Left protected reference: First error: preserve and Do not overwrite the first attempt. Center path: Change one thing → Run the same check → Compare evidence, with the preserved error feeding comparison. Bottom question Still unresolved? sends Yes to Use recovery guidance and No to Record what changed. No arrow automatically returns to the check.
Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Duplicate a label only where its specified branches require it. `Yes` and `No` are the only additional words allowed, solely on edges leaving a question ending in `?`; every such node must have both explicitly assigned destinations. Structural step numbers are permitted only where the brief specifies numbered steps/rows. Do not print block headings, explanatory prose, caption, page name or art instructions inside the image.

5. VISUAL FAMILY
Exact palette: #0D0906 primary ground; #17110C panel fill; #A58650 primary gold; #C8A96A sheen and connector highlights; #C8B78A secondary readable text; #FFF8E7 primary text; #655337 subdued nonessential rules; #3A2E1B faint structural lines; #4F5634 restrained verified/allowed accents; #B43A2F warnings/blocked branches; #2D3030 neutral mechanisms. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities. Match the existing site’s warm near-black, sandstone, gold-trace operational visual family; adapt its palette, not the reference photographs’ subjects, scene composition or no-text constraint.

6. RICHNESS AND LEGIBILITY
Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use clean Inter/Helvetica-like sans-serif; exact filenames/tokens may use a clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density. Keep each essential relationship and full label legible at article width; distribute dense cells over the canvas.

7. HONESTY AND EXCLUSIONS
No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Never depict indefinite automatic retries, replacement of the first failed attempt, or a claim that a changed check proves repair.

8. GENERATION SELF-CHECK
Before returning the PNG path, check that every title and required label is present verbatim, no extra visible words appear, and the relationship is unmistakable: First error survives outside the correction path; both Yes→recovery and No→record destinations must be visible; missing comparison or the preserved-error boundary makes this unusable. If any required label or branch is absent, revise the image rather than claiming it is verified. This internal generation check does not replace a later visual inspection.


## 9. Revision requirements from review of the previous attempt
A previous generation of this figure was rejected. Generate a NEW image from this full contract and fix every defect below. All earlier blocks still govern; labels stay verbatim; add no words. Title text sits directly on the dark ground with no white bloom/haze band.

- m00-recovery-loop: route Still unresolved? from Compare evidence
REGENERATE. Transcription: KEEP THE FIRST ERROR; First error: preserve; Do not overwrite the first attempt; Change one thing; Run the same check; Compare evidence; Still unresolved?; Yes; No; Use recovery guidance; Record what changed. Every string matches the label map, and Yes/No are permitted. The defect is structural. The gold trace leaves First error: preserve at about y=477 and runs right. At about x=1085 a down arrow branches off it into Still unresolved?, and the same trace then curves up into Compare evidence. Compare evidence has no outgoing edge. As drawn, the decision is fed directly by the preserved first error and bypasses the comparison. The brief requires Change one thing → Run the same check → Compare evidence → Still unresolved?, and the README requires the comparison against the first error before any next step. Fix: draw one arrow from the bottom of Compare evidence down to Still unresolved?. Have the preserved-error trace end only at Compare evidence (its left or bottom edge) with no branch toward the question. Keep the Yes→Use recovery guidance and No→Record what changed branches and add no return arrow. Also reduce the dark vignette blotch in the lower-left.


## 10. Global rendering corrections (apply to this image)
- Background is flat-to-subtle #0D0906 near-black with at most a faint warm vignette. NO white, grey, cream or yellow bloom/glow/haze anywhere, especially not behind the title; title text is solid #FFF8E7 on dark ground, at least 64 px from the top edge, with only a thin warm sheen.
- Do not add trailing periods or any punctuation not in the label map.
- No people, silhouettes, hands, phones, gears, shields, medals, check-mark badges, browser windows or other decorative pictograms. Nodes are text-first; generic document glyphs only where they explain containment.
- Every essential label at least 32 px in #FFF8E7 or #C8B78A; never dim tan small text.
- Olive (#4F5634) only for allowed/verified states; brick red (#B43A2F) only for blocked/HOLD/warning; neutral routes use #2D3030 with gold stroke.
````

## m00-responsibility-screen

- Title: `SCREEN BEFORE DELEGATING`
- Publication path: `shared/figures/m00-responsibility-screen.png`
- Anchor: Lab `## 5. Complete the minimum responsibility screen`; after its introductory paragraph, before the text template.
- Caption: Resolve data authority and decision ownership before drafting, and name who could be affected by an unsupported implication.
- Native size: 1536×1024; published SHA-256: `1e9931c7e1902778ffbdb7e78efb41770fd1338915cc56441cb8a12cc939e857`
- Iteration history:
  - attempt-01: full generation; session `01a1004f-58de-7fe0-90c6-82a46086ae8c`; raw SHA-256 `ead5a76751eab725…`; ACCEPTED
  - attempt-02: edit; session `01a10074-a541-7830-816d-79e4208c52da`; raw SHA-256 `3eaddb48aa932dd7…`; not selected
- Final review outcome: accepted attempt-01. F00: m00-responsibility-screen: ACCEPT_A1 — all 10 labels exact (the → included); both gates meet at a junction → Resolved → class draft only; the red exit Unresolved authority or owner → HOLD → Resolve before drafting has no path back; the four review conditions sit unconnected in the frame corners, matching lab step 5; flattened title is solid on dark ground (A2 has heavy red fog and a title-band seam).

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

2. LESSON CONTRACT
Module 00 — North Shelf; Lab / 5. Complete the minimum responsibility screen. Learning takeaway/caption: “Resolve data authority and decision ownership before drafting, and name who could be affected by an unsupported implication.” Intended learner action in unfamiliar work: Before delegating an unfamiliar task, identify permitted data, affected parties and the person who owns the decision; stop if authority or ownership is unresolved. Common misconception to prevent: A draft can proceed while source permission or decision ownership remains someone else’s unspecified problem. These instructions are not extra in-image words.

3. COMPOSITION
Produce an original diagram-first raster instructional figure, 1536×1024 landscape, 64 px safe margin. Place the title in a dedicated top zone and give the remaining area to the actual mechanism; prefer two spacious rows over tiny type. Category and reading order: two explicit gates around a bounded draft, with surrounding risk questions and one stopped exit. Exact nodes and relationships: Upper gate Source and data authority and lower paired gate Human decision owner both must be resolved before Resolved → class draft only. Around the gate perimeter, Sensitive data, Affected people, Disclosure, Consequential action are review conditions, not downstream permissions. Unresolved authority or owner → HOLD → Resolve before drafting. No path from HOLD to drafting without resolution. Make the stated distinction the focal relationship, not a decorative list. Arrows mean only the explicit relationship specified here, never automatic approval; no decorative connectors and no slide-overlay space. This is an inline course image readable at normal article width.

4. VERBATIM LABEL MAP
Title zone: `SCREEN BEFORE DELEGATING`.
Required visible labels, each exactly once unless a specified branch expressly requires repetition:
- `Source and data authority`
- `Sensitive data`
- `Affected people`
- `Disclosure`
- `Consequential action`
- `Human decision owner`
- `Unresolved authority or owner`
- `HOLD`
- `Resolve before drafting`
- `Resolved → class draft only`
Placement and connection map: Upper gate Source and data authority and lower paired gate Human decision owner both must be resolved before Resolved → class draft only. Around the gate perimeter, Sensitive data, Affected people, Disclosure, Consequential action are review conditions, not downstream permissions. Unresolved authority or owner → HOLD → Resolve before drafting. No path from HOLD to drafting without resolution.
Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Duplicate a label only where its specified branches require it. `Yes` and `No` are the only additional words allowed, solely on edges leaving a question ending in `?`; every such node must have both explicitly assigned destinations. Structural step numbers are permitted only where the brief specifies numbered steps/rows. Do not print block headings, explanatory prose, caption, page name or art instructions inside the image.

5. VISUAL FAMILY
Exact palette: #0D0906 primary ground; #17110C panel fill; #A58650 primary gold; #C8A96A sheen and connector highlights; #C8B78A secondary readable text; #FFF8E7 primary text; #655337 subdued nonessential rules; #3A2E1B faint structural lines; #4F5634 restrained verified/allowed accents; #B43A2F warnings/blocked branches; #2D3030 neutral mechanisms. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities. Match the existing site’s warm near-black, sandstone, gold-trace operational visual family; adapt its palette, not the reference photographs’ subjects, scene composition or no-text constraint.

6. RICHNESS AND LEGIBILITY
Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use clean Inter/Helvetica-like sans-serif; exact filenames/tokens may use a clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density. Keep each essential relationship and full label legible at article width; distribute dense cells over the canvas.

7. HONESTY AND EXCLUSIONS
No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Do not imply identifying affected people grants source authority, or that permission to draft grants permission to send, release or take other consequential action.

8. GENERATION SELF-CHECK
Before returning the PNG path, check that every title and required label is present verbatim, no extra visible words appear, and the relationship is unmistakable: Both authority and owner gates must be visible; unresolved exits at HOLD while resolved reaches only class drafting; omission of affected people or the prohibited consequence makes this unusable. If any required label or branch is absent, revise the image rather than claiming it is verified. This internal generation check does not replace a later visual inspection.
````

## m00-tool-layers

- Title: `NAME WHAT YOU ACTUALLY OBSERVED`
- Publication path: `shared/figures/m00-tool-layers.png`
- Anchor: Lab `## 11. Describe an observed capability and limit`.
- Caption: Distinguish the model's words, the actual file, the harness's recorded behavior, and the decision a person owns.
- Native size: 1536×1024; published SHA-256: `342d2326d8b1d44336beb060ee602cd4889048e4aad40c5982c7683554d56120`
- Iteration history:
  - attempt-01: full generation; session `01a10050-4a9d-71a3-9332-831386190276`; raw SHA-256 `095cb05f7cb7cc22…`; superseded — review: m00-tool-layers: remove Interface↔Person link and haze
  - attempt-02: full generation; session `01a10072-9eb5-7e13-b7f8-3dbc6fbd9a9d`; raw SHA-256 `887dcdbdc4b9d3ac…`; ACCEPTED
- Final review outcome: accepted attempt-02. F00: m00-tool-layers: ACCEPT_A2 — title and all 8 labels exact, ≠ signs correct; four separate rows, with Text ≠ fact between Model and Interface and Receipt ≠ correctness between Harness and Person; every layer feeds one shared line to both record boxes, so there is no Interface↔Person shortcut and no Model-only path (A1 defects); the short dangling end of that line near the title is cosmetic only.

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

2. LESSON CONTRACT
Module 00 — North Shelf; Lab / 11. Describe an observed capability and limit. Learning takeaway/caption: “Distinguish the model’s words, the actual file, the harness’s recorded behavior, and the decision a person owns.” Intended learner action in unfamiliar work: In unfamiliar AI-assisted work, assign each observation to its originating layer and report a supported capability and limit. Common misconception to prevent: A fluent model statement or saved receipt proves factual correctness or transfers the use decision to software. These instructions are not extra in-image words.

3. COMPOSITION
Produce an original diagram-first raster instructional figure, 1536×1024 landscape, 64 px safe margin. Place the title in a dedicated top zone and give the remaining area to the actual mechanism; prefer two spacious rows over tiny type. Category and reading order: four aligned independent evidence layers, each linked to its own observation, with explicit non-equivalence markers rather than a success ladder. Exact nodes and relationships: Four horizontal rows: Model: generated text; Interface: file on disk; Harness: permissions + receipts; Person: interpretation + use decision. Across row boundaries place Text ≠ fact and Receipt ≠ correctness as visible dividers. Lower two output boxes Record a capability and Record a limit link back to observed layers but do not claim universal reliability. Make the stated distinction the focal relationship, not a decorative list. Arrows mean only the explicit relationship specified here, never automatic approval; no decorative connectors and no slide-overlay space. This is an inline course image readable at normal article width.

4. VERBATIM LABEL MAP
Title zone: `NAME WHAT YOU ACTUALLY OBSERVED`.
Required visible labels, each exactly once unless a specified branch expressly requires repetition:
- `Model: generated text`
- `Interface: file on disk`
- `Harness: permissions + receipts`
- `Person: interpretation + use decision`
- `Text ≠ fact`
- `Receipt ≠ correctness`
- `Record a capability`
- `Record a limit`
Placement and connection map: Four horizontal rows: Model: generated text; Interface: file on disk; Harness: permissions + receipts; Person: interpretation + use decision. Across row boundaries place Text ≠ fact and Receipt ≠ correctness as visible dividers. Lower two output boxes Record a capability and Record a limit link back to observed layers but do not claim universal reliability.
Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Duplicate a label only where its specified branches require it. `Yes` and `No` are the only additional words allowed, solely on edges leaving a question ending in `?`; every such node must have both explicitly assigned destinations. Structural step numbers are permitted only where the brief specifies numbered steps/rows. Do not print block headings, explanatory prose, caption, page name or art instructions inside the image.

5. VISUAL FAMILY
Exact palette: #0D0906 primary ground; #17110C panel fill; #A58650 primary gold; #C8A96A sheen and connector highlights; #C8B78A secondary readable text; #FFF8E7 primary text; #655337 subdued nonessential rules; #3A2E1B faint structural lines; #4F5634 restrained verified/allowed accents; #B43A2F warnings/blocked branches; #2D3030 neutral mechanisms. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities. Match the existing site’s warm near-black, sandstone, gold-trace operational visual family; adapt its palette, not the reference photographs’ subjects, scene composition or no-text constraint.

6. RICHNESS AND LEGIBILITY
Subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Use clean Inter/Helvetica-like sans-serif; exact filenames/tokens may use a clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density. Keep each essential relationship and full label legible at article width; distribute dense cells over the canvas.

7. HONESTY AND EXCLUSIONS
No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. No implication that the model physically performed file effects without interface evidence, or that receipts confer correctness or human decision authority.

8. GENERATION SELF-CHECK
Before returning the PNG path, check that every title and required label is present verbatim, no extra visible words appear, and the relationship is unmistakable: All four evidence layers must stay distinct; Text ≠ fact and Receipt ≠ correctness must remain legible and the human decision cannot appear inherited from fluent text. If any required label or branch is absent, revise the image rather than claiming it is verified. This internal generation check does not replace a later visual inspection.


## 9. Revision requirements from review of the previous attempt
A previous generation of this figure was rejected. Generate a NEW image from this full contract and fix every defect below. All earlier blocks still govern; labels stay verbatim; add no words. Title text sits directly on the dark ground with no white bloom/haze band.

- m00-tool-layers: remove Interface↔Person link and haze
REGENERATE. Transcription: NAME WHAT YOU ACTUALLY OBSERVED; Model: generated text; Text ≠ fact; Interface: file on disk; Harness: permissions + receipts; Receipt ≠ correctness; Person: interpretation + use decision; Record a capability; Record a limit. Every label is exact and the ≠ signs are correct. Relationship defects: on both sides, a bracket connector (x≈80 left, x≈1455 right) joins the Interface row directly to the Person row and nowhere else. This invents an Interface→Person-decision dependency, and the Person and Interface layers never reach the record boxes. The outermost connectors run from Model: generated text straight to both Record a capability and Record a limit, past the Text ≠ fact divider. That suggests model text alone can ground a capability record, which contradicts lab step 11 ('a chat statement is being used as proof of an action' is a Stop). Style: heavy yellow edge glow and title bloom flood the canvas, far brighter than the approved pilot ('not … cinematic haze'). Fix: four independent rows with no row-to-row connectors. Each row gets one short gold tick to a shared evidence rail that feeds Record a capability and Record a limit equally. Keep Text ≠ fact between Model and Interface and Receipt ≠ correctness between Harness and Person. Use a near-black ground with only a mild title glow, as in m00-bounded-direction.


## 10. Global rendering corrections (apply to this image)
- Background is flat-to-subtle #0D0906 near-black with at most a faint warm vignette. NO white, grey, cream or yellow bloom/glow/haze anywhere, especially not behind the title; title text is solid #FFF8E7 on dark ground, at least 64 px from the top edge, with only a thin warm sheen.
- Do not add trailing periods or any punctuation not in the label map.
- No people, silhouettes, hands, phones, gears, shields, medals, check-mark badges, browser windows or other decorative pictograms. Nodes are text-first; generic document glyphs only where they explain containment.
- Every essential label at least 32 px in #FFF8E7 or #C8B78A; never dim tan small text.
- Olive (#4F5634) only for allowed/verified states; brick red (#B43A2F) only for blocked/HOLD/warning; neutral routes use #2D3030 with gold stroke.
````

