# Raster figure prompts and provenance — module-04-typed-decisions

Staff-only record. Not published (absent from `course.json`).

- Generator: `codex-cli 0.154.0` (`codex exec`, ChatGPT login, built-in `image_gen`).
- Style references attached to every invocation: `ui/images/home-hero.webp` and `ui/images/home-band-custody.webp`, decoded losslessly to PNG with `dwebp`; every figure except `m00-bounded-direction` also received the accepted `m00-bounded-direction` attempt-01 raster as a style-only reference. Label edits additionally attached the image being edited as the first input.
- Post-processing: the generator returns RGBA with a transparent ground. Each accepted raster was alpha-composited onto the specified `#0D0906` ground and saved as opaque lossless RGB PNG at native size. No other pixel changes, no resizing.
- Run evidence (all attempts, logs, rejected rasters, reviews): `~/course-evidence/course-raster-visuals/20261002T233502`
- Module source contract: `module-04-typed-decisions/shared/MODULE_04_LAB.md`, `shared/controls/questions.json`, and `scripts/chalk.py` (`referred`, `route`, `noul_confidence`). Current core volume is 40 messages × 8 questions = 320 typed answers; the human-label sample is ten messages. No route totals or message answers are illustrated.
- Owning page digests at integration (SHA-256): `shared/MODULE_04_LAB.md` 1c63c124a316edc3…

## m04-answer-types

- Title: `MATCH EACH QUESTION TO A TYPE`
- Publication path: `shared/figures/m04-answer-types.png`
- Anchor: same section, immediately after its three answer-type bullets.
- Caption: Fixed answer shapes constrain what the model can return; they do not establish that its interpretation is correct.
- Native size: 1536×1024; published SHA-256: `94af9bbc6b71c24944fb1dfe18d215e7585c8e302d81bbb8218bb82e41a21b0b`
- Iteration history:
  - attempt-01: full generation; session `01a10052-13b5-71a3-8f6d-8fc6580ba478`; raw SHA-256 `50f652f6d961f021…`; ACCEPTED
- Final review outcome: accepted attempt-01. FAcc: m04-answer-types: ACCEPT_A1 — the light body text is legible and the connector stubs are visible.

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

2. LESSON CONTRACT
Owning module: Module 04 — Chalk Line, AI_Harness_Bootcamp_2/module-04-typed-decisions; page: shared/MODULE_04_LAB.md; H2: ## Build the state and read the questions. Learning takeaway (caption, not visible image text): “Fixed answer shapes constrain what the model can return; they do not establish that its interpretation is correct.” Intended learner action in unfamiliar work: When defining a new fixed question, select the answer schema that matches the judgment and bind choices to the actual listed options. Misconception to prevent: A schema-valid answer proves the model understood the message. This section is instruction for generation, not additional image wording.

3. COMPOSITION
three-card schema comparison. Generate a 1536×1024 landscape raster PNG with 64 px safe margin; title zone at top and remaining canvas for the mechanism. Prefer two rows over tiny type; no slide-overlay reserved space. Reading order left-to-right then top-to-bottom. Three aligned large cards: YES / NO pairs the YES probability p with no binary result field; CHOICE pairs a listed value with confidence; SCORE pairs a level index with confidence. Under CHOICE, two lower constraint rails bind quantity to message-specific candidate IDs or NONE and replaces to earlier message IDs or NONE. End with the distinct warning that schema validity does not certify interpretation. No fabricated values. Arrows signify only the specified dependency or movement, never automatic approval. No decorative connectors.

4. VERBATIM LABEL MAP
Top title: `MATCH EACH QUESTION TO A TYPE`
YES / NO card: `YES / NO`; `p: model's YES probability`
CHOICE card: `CHOICE`; `Listed value + confidence`
SCORE card: `SCORE`; `Level index + confidence`
Choice constraints and limit: `quantity: candidate ID or NONE`; `replaces: earlier ID or NONE`; `Schema validity ≠ correct interpretation`
Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Duplicate a label only where its specified branches require it. Yes and No are the only additional words allowed, solely on edges leaving a question ending in ?; every such node must have both explicitly assigned destinations. Structural step numbers are permitted only where the brief specifies numbered steps/rows.

5. VISUAL FAMILY
Primary ground #0D0906; panel fill #17110C; primary gold #A58650; sheen and connector highlights #C8A96A; secondary readable text #C8B78A; primary text #FFF8E7; subdued nonessential rules #655337; faint structural lines #3A2E1B; restrained verified/allowed accents #4F5634; warnings/blocked branches #B43A2F; neutral mechanisms #2D3030. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities.

6. RICHNESS AND LEGIBILITY
Use subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Clean Inter/Helvetica-like sans-serif; exact filenames/tokens may use clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density.

7. HONESTY AND EXCLUSIONS
No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Do not show message answers, route totals, invented probability values, live successes, dispatch or release authorization.

8. GENERATION SELF-CHECK
Three different shapes must be distinct, and both constrained CHOICE domains must appear. Omitting p as YES probability, the earlier-ID constraint, or the schema-versus-meaning warning makes the figure unusable.
````

## m04-final-confidence

- Title: `CONFIDENCE IS A FINAL GATE`
- Publication path: `shared/figures/m04-final-confidence.png`
- Anchor: Lab `## Measure the answers against your labels`; replace `m04-declared-vs-measured.svg`.
- Caption: Only requests reaching the final gate use these five confidences; a threshold equal to an observed wrong answer's confidence does not exclude it.
- Native size: 1536×1024; published SHA-256: `ae70147c874c85e36a2ef19f0c20a507d3e6e044568ef5af7448093251d09535`
- Iteration history:
  - attempt-01: full generation; session `01a10052-f67f-79d3-b91a-fdd4eff97ecf`; raw SHA-256 `1e9d1226ac3c1164…`; ACCEPTED
- Final review outcome: accepted attempt-01. FAcc: m04-final-confidence: ACCEPT_A1 — all five field chips, the formula and the REVIEW/PICK boxes are legible.

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

2. LESSON CONTRACT
Owning module: Module 04 — Chalk Line, AI_Harness_Bootcamp_2/module-04-typed-decisions; page: shared/MODULE_04_LAB.md; H2: ## Measure the answers against your labels. Learning takeaway (caption, not visible image text): “Only requests reaching the final gate use these five confidences; a threshold equal to an observed wrong answer's confidence does not exclude it.” Intended learner action in unfamiliar work: In a new workflow, compare the weakest confidence among only the eligible answers against a threshold strictly greater than an observed wrong answer confidence when seeking to exclude it. Misconception to prevent: Setting the threshold equal to a wrong answer confidence, or to 1, excludes all confident errors. This section is instruction for generation, not additional image wording.

3. COMPOSITION
five-input minimum selector with two outcome branches. Generate a 1536×1024 landscape raster PNG with 64 px safe margin; title zone at top and remaining canvas for the mechanism. Prefer two rows over tiny type; no slide-overlay reserved space. Reading order left-to-right then top-to-bottom. At left, a small entry gate marked After earlier routing gates admits only a remaining usable, authorized request. Five independently labeled confidence inputs enter a prominent Weakest confidence minimum selector. Convert YES/NO probability p to abs(2p - 1) for the three YES/NO inputs request, authority and instructs_desk; line and quantity carry declared choice confidence. Replaces-link confidence stays entirely outside this selector. Two clean outgoing branches: strict below min_confidence leads REVIEW, greater-than-or-equal leads PICK. An inset Equality passes explains why an observed wrong answer is excluded only by a strictly higher threshold; no invented numerical sample. PICK is only a requirement-queue result, never dispatch permission. If no wrong answer is observed there is no observed maximum, not perfect reliability. No valid threshold exceeds 1; a wrong confidence of 1 cannot be excluded by this gate alone. Arrows signify only the specified dependency or movement, never automatic approval. No decorative connectors.

4. VERBATIM LABEL MAP
Title: `CONFIDENCE IS A FINAL GATE`
Entry: `After earlier routing gates`
Five inputs: `request`; `line`; `quantity`; `authority`; `instructs_desk`
Selector: `YES/NO confidence = abs(2p - 1)`; `Weakest confidence`
Outcomes and threshold: `< min_confidence → REVIEW`; `≥ min_confidence → PICK`; `Equality passes`
Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Duplicate a label only where its specified branches require it. Yes and No are the only additional words allowed, solely on edges leaving a question ending in ?; every such node must have both explicitly assigned destinations. Structural step numbers are permitted only where the brief specifies numbered steps/rows.

5. VISUAL FAMILY
Primary ground #0D0906; panel fill #17110C; primary gold #A58650; sheen and connector highlights #C8A96A; secondary readable text #C8B78A; primary text #FFF8E7; subdued nonessential rules #655337; faint structural lines #3A2E1B; restrained verified/allowed accents #4F5634; warnings/blocked branches #B43A2F; neutral mechanisms #2D3030. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities.

6. RICHNESS AND LEGIBILITY
Use subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Clean Inter/Helvetica-like sans-serif; exact filenames/tokens may use clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density.

7. HONESTY AND EXCLUSIONS
No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Do not show message answers, route totals, invented probability values, live successes, dispatch or release authorization.

8. GENERATION SELF-CHECK
Only remaining usable authorized requests enter; the five specified fields feed a minimum, excluding replaces; strict-below goes REVIEW, equality and above go PICK. Missing a field, swapped inequality, or implication that 1 excludes every confidently wrong answer makes the figure unusable.
````

## m04-freeze-measure

- Title: `LABEL FIRST, THEN MEASURE`
- Publication path: `shared/figures/m04-freeze-measure.png`
- Anchor: Lab `## Label the sample before the model runs`; replace `m04-measure-before-trust.svg`.
- Caption: Freeze your labels before the run, adjudicate disagreements, and use the observed mistakes without treating a small sample as a general reliability estimate.
- Native size: 1536×1024; published SHA-256: `6cd2ec27df28bd7d7919697234e9b6db4bcdf6c83b931b95b445f6111428e4b6`
- Iteration history:
  - attempt-01: full generation; session `01a10053-e634-7c41-9fe5-6b4930e85a76`; raw SHA-256 `44db152f02ae0364…`; superseded
  - attempt-02: edit; session `01a10087-4eee-7a51-bae9-55c233c63f9e`; raw SHA-256 `28c193a175381bdf…`; ACCEPTED
- Final review outcome: accepted attempt-02. Final1: m04-freeze-measure: ACCEPT_A2 — the person silhouette is replaced by a plain document glyph above 'Human labels'. All other strings (LABEL FIRST, THEN MEASURE; 10-message sample; Freeze digest + UTC time; Run once; 8 × 40 = 320 typed answers; Compare four labeled fields; Adjudicate disagreements; Declared confidence ≠ measured agreement; Not a reliability rate), the lock, and both lanes meeting only at Compare are unchanged.

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to EDIT the first attached image and save exactly ONE corrected PNG with an OPAQUE #0D0906 background (no transparency). Do not use a CLI image fallback or write code/SVG. The other attachments are STYLE references only. Return the absolute saved PNG path and no claim of verification.

CORRECTIONS (apply exactly; preserve every other relationship, label, position and color):
m04-freeze-measure: LABEL_EDIT_A1 — remove person silhouette above 'Human labels'
In RUN/m04-freeze-measure/attempt-01/flattened.png, the second box of the top lane (x≈410–715, y≈180–410) shows a person icon (head and shoulders) above the text 'Human labels'. Section 7 of prompt.md bans people/hands. Only generic document/table glyphs are allowed, and only to show containment or transformation. The flattened image shows this icon clearly; the transparency did not hide it. Edit only that box: delete the person icon and put a plain document/table glyph in its place, matching the style of the glyph in the '10-message sample' box. Alternatively, leave the box with no icon and center 'Human labels' vertically. Keep every other string, box, arrow and the freeze lock exactly as they are.

The original full generation contract follows and still governs labels and composition:

$imagegen
Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

2. LESSON CONTRACT
Owning module: Module 04 — Chalk Line, AI_Harness_Bootcamp_2/module-04-typed-decisions; page: shared/MODULE_04_LAB.md; H2: ## Label the sample before the model runs. Learning takeaway (caption, not visible image text): “Freeze your labels before the run, adjudicate disagreements, and use the observed mistakes without treating a small sample as a general reliability estimate.” Intended learner action in unfamiliar work: Write and freeze independent human labels first, then compare the model run and adjudicate errors before selecting gates in another workflow. Misconception to prevent: Model-declared confidence or agreement on ten samples is a population reliability rate. This section is instruction for generation, not additional image wording.

3. COMPOSITION
two-lane evidence convergence. Generate a 1536×1024 landscape raster PNG with 64 px safe margin; title zone at top and remaining canvas for the mechanism. Prefer two rows over tiny type; no slide-overlay reserved space. Reading order left-to-right then top-to-bottom. Upper lane: 10-message sample → Human labels → Freeze digest + UTC time, visibly sealed before model results. Separate lower lane: Run once → 8 × 40 = 320 typed answers. The two lanes first meet at Compare four labeled fields → Adjudicate disagreements, then inform later gate selection without adding an extra visible label. No arrows from model output back into frozen labels. Put confidence and reliability warnings in a subordinate footer. Arrows signify only the specified dependency or movement, never automatic approval. No decorative connectors.

4. VERBATIM LABEL MAP
Top title: `LABEL FIRST, THEN MEASURE`
Human lane: `10-message sample`; `Human labels`; `Freeze digest + UTC time`
Model lane: `Run once`; `8 × 40 = 320 typed answers`
Comparison: `Compare four labeled fields`; `Adjudicate disagreements`
Limits: `Declared confidence ≠ measured agreement`; `Not a reliability rate`
Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Duplicate a label only where its specified branches require it. Yes and No are the only additional words allowed, solely on edges leaving a question ending in ?; every such node must have both explicitly assigned destinations. Structural step numbers are permitted only where the brief specifies numbered steps/rows.

5. VISUAL FAMILY
Primary ground #0D0906; panel fill #17110C; primary gold #A58650; sheen and connector highlights #C8A96A; secondary readable text #C8B78A; primary text #FFF8E7; subdued nonessential rules #655337; faint structural lines #3A2E1B; restrained verified/allowed accents #4F5634; warnings/blocked branches #B43A2F; neutral mechanisms #2D3030. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities.

6. RICHNESS AND LEGIBILITY
Use subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Clean Inter/Helvetica-like sans-serif; exact filenames/tokens may use clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density.

7. HONESTY AND EXCLUSIONS
No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Do not show message answers, route totals, invented probability values, live successes, dispatch or release authorization.

8. GENERATION SELF-CHECK
The frozen human labels must precede and remain independent of the one run; both lanes meet only at comparison. Missing freeze, four-field comparison, or the not-a-reliability-rate warning makes the figure unusable.
````

## m04-routing-order

- Title: `FIRST MATCH DETERMINES THE ROUTE`
- Publication path: `shared/figures/m04-routing-order.png`
- Anchor: same section, replace `m04-routes.svg` after the ordered rule paragraphs.
- Caption: Code applies the rules in this order; earlier routes take precedence, and only a remaining usable, authorized request reaches the final confidence check.
- Native size: 1536×1024; published SHA-256: `1644c1e4d24620348d9156804eddc4c0349e655c39877837a46afd7939cd355d`
- Iteration history:
  - attempt-01: full generation; session `01a10054-c26f-7f41-b7f7-c2172090dcdb`; raw SHA-256 `14455d234f2e6577…`; superseded — review: Remove the maxim-to-row-6 arrow so evaluation starts at rule 1
  - attempt-02: full generation; session `01a1006a-e7ef-77c1-9ed6-889775cd76d1`; raw SHA-256 `662baa68b02d058e…`; ACCEPTED
- Final review outcome: accepted attempt-02. F0405: m04-routing-order: ACCEPT_A2 — all nine numbered rows, the title and the maxim are exact. Each row's label and route match `chalk.py` `route()` order exactly: SUPERSEDED, REFER, uncertain-link REVIEW, IGNORE, MIXED REVIEW, CLARIFY, CLARIFY, authority REFER, then the confidence gate. A hit exits right; a miss continues down and across the turn from row 5 to row 6. Row 9 has no route, so nothing implies PICK or dispatch. The pills are neutral. A1 colors REFER/IGNORE olive (the allowed accent), which implies approval.

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

2. LESSON CONTRACT
Owning module: Module 04 — Chalk Line, AI_Harness_Bootcamp_2/module-04-typed-decisions; page: shared/MODULE_04_LAB.md; H2: ## Set the gates and route the pile. Learning takeaway (caption, not visible image text): “Code applies the rules in this order; earlier routes take precedence, and only a remaining usable, authorized request reaches the final confidence check.” Intended learner action in unfamiliar work: Use an ordered first-match decision list, checking every earlier route before considering a final confidence gate in new work. Misconception to prevent: The presence of any uncertainty overrides supersession or instruction referral, or PICK authorizes dispatch. This section is instruction for generation, not additional image wording.

3. COMPOSITION
nine numbered ordered rule rows. Generate a 1536×1024 landscape raster PNG with 64 px safe margin; title zone at top and remaining canvas for the mechanism. Prefer two rows over tiny type; no slide-overlay reserved space. Reading order left-to-right then top-to-bottom. Use nine spacious numbered rows arranged as two connected columns (rows 1–5 left and 6–9 right), with continuous top-to-bottom evaluation clearly marked through the turn. Each matched row exits horizontally to its route word already contained in that row label; a miss alone continues to the next rule. Row 1 replaced target supersedes before row 2 instruction referral, which precedes row 3 uncertain-link review, then row 4 not-request ignore, row 5 MIXED review, row 6 missing size/quantity clarify, row 7 invalid converted box count clarify, row 8 insufficient authority refer, row 9 final confidence gate. Row 9 points conceptually to the separate five-confidence selector but does not reproduce it. Make First matching rule wins focal and readable. Conditions: instruction p ≥ its gate; request p < its gate; missing line UNSTATED/NONE or quantity NONE; selected candidate begins with number plus box/case unit; cases multiply by ten, converted boxes positive and whole (case number need not itself be whole); authority p < its gate. PICK is only a requirement queue result, never stock release or dispatch authorization. Structural row numbers 1–9 only. Arrows signify only the specified dependency or movement, never automatic approval. No decorative connectors.

4. VERBATIM LABEL MAP
Title: `FIRST MATCH DETERMINES THE ROUTE`
Rule 1: `Replaced target → SUPERSEDED`
Rule 2: `Desk instruction → REFER`
Rule 3: `Uncertain link → REVIEW`
Rule 4: `Not a request → IGNORE`
Rule 5: `MIXED size → REVIEW`
Rule 6: `Missing size or quantity → CLARIFY`
Rule 7: `Invalid converted box count → CLARIFY`
Rule 8: `Insufficient authority → REFER`
Rule 9: `Otherwise: final confidence gate`
Ordering maxim: `First matching rule wins`
Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Duplicate a label only where its specified branches require it. Yes and No are the only additional words allowed, solely on edges leaving a question ending in ?; every such node must have both explicitly assigned destinations. Structural step numbers are permitted only where the brief specifies numbered steps/rows.

5. VISUAL FAMILY
Primary ground #0D0906; panel fill #17110C; primary gold #A58650; sheen and connector highlights #C8A96A; secondary readable text #C8B78A; primary text #FFF8E7; subdued nonessential rules #655337; faint structural lines #3A2E1B; restrained verified/allowed accents #4F5634; warnings/blocked branches #B43A2F; neutral mechanisms #2D3030. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities.

6. RICHNESS AND LEGIBILITY
Use subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Clean Inter/Helvetica-like sans-serif; exact filenames/tokens may use clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density.

7. HONESTY AND EXCLUSIONS
No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Do not show message answers, route totals, invented probability values, live successes, dispatch or release authorization.

8. GENERATION SELF-CHECK
Every rule must appear once in exactly the numbered order 1–9, with matched rows exiting and misses continuing. Swapping supersession/instruction/uncertain link, placing authority before quantity usability, omitting either CLARIFY row, or treating PICK as dispatch makes the figure unusable.


## 9. Revision requirements from review of the previous attempt
A previous generation of this figure was rejected. Generate a NEW image from this full contract and fix every defect below. All earlier blocks still govern; labels stay verbatim; add no words. Title text sits directly on the dark ground with no white bloom/haze band.

- Remove the maxim-to-row-6 arrow so evaluation starts at rule 1
m04-routing-order image transcription: title `FIRST MATCH DETERMINES THE ROUTE`; banner `First matching rule wins`; rows 1 `Replaced target`→`SUPERSEDED`, 2 `Desk instruction`→`REFER`, 3 `Uncertain link`→`REVIEW`, 4 `Not a request`→`IGNORE`, 5 `MIXED size`→`REVIEW`, 6 `Missing size or quantity`→`CLARIFY`, 7 `Invalid converted box count`→`CLARIFY`, 8 `Insufficient authority`→`REFER`, 9 `Otherwise: final confidence gate`. All labels are present and correctly spelled, and the order matches chalk.py route() lines 359-385. Structural defect: a gold down-arrow leaves the `First matching rule wins` banner at about x≈1005 and enters the top of row 6. Row 1 has no entry arrow. Row 6 therefore has two entries (the banner and the loop from row 5), and the most prominent entry point in the figure starts evaluation at rule 6. That contradicts the first-match order the figure exists to teach: a reader could skip rules 1-5 (supersession, desk instruction, uncertain link, not-a-request, MIXED). Verdict REGENERATE: keep the banner as a free-standing header with no connector, or point its single arrow into the top of row 1. Keep the 5→6 turn loop as the only entry into row 6.

- Stop coloring REFER and IGNORE with the verified/allowed olive
In m04-routing-order, the REFER pills (rows 2 and 8) and the IGNORE pill (row 4) use olive #4F5634. The prompt's palette reserves that color for 'restrained verified/allowed accents'. SUPERSEDED, REVIEW and CLARIFY use brick red ('warnings/blocked'). Row 2 is the desk-instruction (hostile note) route, and row 8 is the no-authority route. Painting both in the allowed color suggests approval for exactly the messages that must go to a person, which is the accidental-approval reading that acceptance criteria 1 and 4 forbid. None of these routes is PICK, so no route pill in this figure should carry the allowed accent. During the REGENERATE above, render all eight route pills in one neutral mechanism fill (#2D3030 with gold stroke), or use brick red for all non-PICK routes.
````

## m04-state-and-questions

- Title: `USE THE MODEL AS A BOUNDED FUNCTION`
- Publication path: `shared/figures/m04-state-and-questions.png`
- Anchor: Lab `## Build the state and read the questions`; replace `m04-function-not-chat.svg`.
- Caption: Software supplies bounded state and answer choices; the model returns typed proposals, while code validates and routes and people retain consequential decisions.
- Native size: 1536×1024; published SHA-256: `979be576c01e760b2e21029e31370a7c441cc7a431eaee10c793b1fb2a02a4e9`
- Iteration history:
  - attempt-01: full generation; session `01a10055-aead-7af3-a3f1-e7ff1d4f52a9`; raw SHA-256 `48dafde4db5803c9…`; ACCEPTED
- Final review outcome: accepted attempt-01. FAcc: m04-state-and-questions: ACCEPT_A1 — the 'Candidate IDs' inset and all arrows read cleanly.

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

2. LESSON CONTRACT
Owning module: Module 04 — Chalk Line, AI_Harness_Bootcamp_2/module-04-typed-decisions; page: shared/MODULE_04_LAB.md; H2: ## Build the state and read the questions. Learning takeaway (caption, not visible image text): “Software supplies bounded state and answer choices; the model returns typed proposals, while code validates and routes and people retain consequential decisions.” Intended learner action in unfamiliar work: In unfamiliar intake work, build bounded state and selectable answer choices before asking a model; keep routing and consequential decisions outside it. Misconception to prevent: A fluent model response or selected quantity can itself dispatch work. This section is instruction for generation, not additional image wording.

3. COMPOSITION
horizontal dependency flow. Generate a 1536×1024 landscape raster PNG with 64 px safe margin; title zone at top and remaining canvas for the mechanism. Prefer two rows over tiny type; no slide-overlay reserved space. Reading order left-to-right then top-to-bottom. Place software-built state and fixed questions in two upper-left compartments, with Candidate IDs attached to state as a constraint on quantity selection. Both enter MODEL at center. Typed answers only exits right into Validate, then Measure, then Code routes; People decide is a distinct final responsibility compartment. Make the model-to-typed-output boundary focal; never draw a MODEL-to-dispatch edge. Arrows signify only the specified dependency or movement, never automatic approval. No decorative connectors.

4. VERBATIM LABEL MAP
Title: `USE THE MODEL AS A BOUNDED FUNCTION`
Inputs: `State: catalog + rules + messages`; `Candidate IDs`; `7 supplied questions + 1 learner question`
Function: `MODEL`; `No model side effects`
Outputs and ownership: `Typed answers only`; `Validate`; `Measure`; `Code routes`; `People decide`
Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Duplicate a label only where its specified branches require it. Yes and No are the only additional words allowed, solely on edges leaving a question ending in ?; every such node must have both explicitly assigned destinations. Structural step numbers are permitted only where the brief specifies numbered steps/rows.

5. VISUAL FAMILY
Primary ground #0D0906; panel fill #17110C; primary gold #A58650; sheen and connector highlights #C8A96A; secondary readable text #C8B78A; primary text #FFF8E7; subdued nonessential rules #655337; faint structural lines #3A2E1B; restrained verified/allowed accents #4F5634; warnings/blocked branches #B43A2F; neutral mechanisms #2D3030. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities.

6. RICHNESS AND LEGIBILITY
Use subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Clean Inter/Helvetica-like sans-serif; exact filenames/tokens may use clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density.

7. HONESTY AND EXCLUSIONS
No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Do not show message answers, route totals, invented probability values, live successes, dispatch or release authorization.

8. GENERATION SELF-CHECK
State and fixed questions constrain MODEL; typed answers go to validation and measurement before code routes and people decide. Missing Candidate IDs, No model side effects, or a direct model-to-dispatch connector makes the figure unusable.
````

## m04-supersession

- Title: `RESOLVE REPLACEMENT LINKS FIRST`
- Publication path: `shared/figures/m04-supersession.png`
- Anchor: Lab `## Set the gates and route the pile`, before the ordered routing explanation.
- Caption: A referred message cannot replace another; uncertain links mark both endpoints for the later routing checks, whose earlier rules still take precedence.
- Native size: 1536×1024; published SHA-256: `11ad9b81ce00cb717544eaf09a4b42bc58374954e3556f4f5e2d72b3386effa5`
- Iteration history:
  - attempt-01: full generation; session `01a10056-9ad7-7060-a7d8-7be419e190aa`; raw SHA-256 `55d2be9138ac3da8…`; ACCEPTED
- Final review outcome: accepted attempt-01. FAcc: m04-supersession: ACCEPT_A1 — the branch lines and the dark-grey 'Ignore link' box are visible.

### Final prompt

````text
$imagegen
Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

2. LESSON CONTRACT
Owning module: Module 04 — Chalk Line, AI_Harness_Bootcamp_2/module-04-typed-decisions; page: shared/MODULE_04_LAB.md; H2: ## Set the gates and route the pile. Learning takeaway (caption, not visible image text): “A referred message cannot replace another; uncertain links mark both endpoints for the later routing checks, whose earlier rules still take precedence.” Intended learner action in unfamiliar work: In an unfamiliar message pile, evaluate replacement proposals as a pre-pass and carry link flags to a separate first-match router. Misconception to prevent: Any uncertain replacement unconditionally assigns REVIEW to both endpoints ahead of supersession or instruction referrals. This section is instruction for generation, not additional image wording.

3. COMPOSITION
conditional pre-pass with three distinct exits. Generate a 1536×1024 landscape raster PNG with 64 px safe margin; title zone at top and remaining canvas for the mechanism. Prefer two rows over tiny type; no slide-overlay reserved space. Reading order left-to-right then top-to-bottom. Start Proposed replaces link at upper left. First condition: when link is NONE or replacer is referred, Ignore link and do not check link confidence. Otherwise test link confidence < min_confidence: if true, Flag both endpoints uncertain. Otherwise record replacement with Target is superseded as a later-routing flag. Bring flags to Flags enter routing precedence at bottom, clearly showing this is not an immediate unconditional REVIEW result. Referred replacer means instructs_desk p ≥ its gate OR request p ≥ its gate while authority p < its gate. A valid replacement can SUPERSEDE a target before an uncertain-link REVIEW; instruction REFER precedes uncertain-link REVIEW. Use conditional forks without printing new condition words: the only visible condition labels are those specified in the label map. Arrows signify only the specified dependency or movement, never automatic approval. No decorative connectors.

4. VERBATIM LABEL MAP
Title: `RESOLVE REPLACEMENT LINKS FIRST`
Input: `Proposed replaces link`
Ignored branch: `NONE or referred replacer`; `Ignore link`
Uncertain branch: `Link confidence < min_confidence`; `Flag both endpoints uncertain`
Valid branch: `Otherwise record replacement`; `Target is superseded`
Handoff: `Flags enter routing precedence`
Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Duplicate a label only where its specified branches require it. Yes and No are the only additional words allowed, solely on edges leaving a question ending in ?; every such node must have both explicitly assigned destinations. Structural step numbers are permitted only where the brief specifies numbered steps/rows.

5. VISUAL FAMILY
Primary ground #0D0906; panel fill #17110C; primary gold #A58650; sheen and connector highlights #C8A96A; secondary readable text #C8B78A; primary text #FFF8E7; subdued nonessential rules #655337; faint structural lines #3A2E1B; restrained verified/allowed accents #4F5634; warnings/blocked branches #B43A2F; neutral mechanisms #2D3030. Olive and brick red are fills/strokes/pills only; text is off-white or sandstone with high contrast, and every status has a text label as well as color. No bright green/blue/cyan/teal/purple. Do not use Starzl product names or product-specific color identities.

6. RICHNESS AND LEGIBILITY
Use subtle warm panel gradients, thin gold sheen, precise gold traces and restrained emission dots only on meaningful connections, modest inner/elevation shadows, sharp corners, faint survey-grid texture away from text. Warm, restrained operational luminance—not neon, sci-fi, cinematic haze, or a sterile flat wireframe. Clean Inter/Helvetica-like sans-serif; exact filenames/tokens may use clean monospace. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density.

7. HONESTY AND EXCLUSIONS
No scene, people/hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal/UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document/table glyphs are permitted only to explain containment or transformation, not as decoration. Do not show message answers, route totals, invented probability values, live successes, dispatch or release authorization.

8. GENERATION SELF-CHECK
NONE/referred replacers must be ignored before confidence testing; low link confidence flags both endpoints; other links record the target. Missing the ignored branch, both endpoints, or later precedence handoff makes the figure unusable.
````

