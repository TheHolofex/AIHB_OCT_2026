# Raster figure prompts and provenance — module-10-capstone

Staff-only record. Not published (absent from `course.json`).

- Generator: `codex-cli 0.154.0` (`codex exec`, ChatGPT login, built-in `image_gen`).
- Style references attached to every invocation: `ui/images/home-hero.webp` and `ui/images/home-band-custody.webp`, decoded losslessly to PNG with `dwebp`; every figure except `m00-bounded-direction` also received the accepted `m00-bounded-direction` attempt-01 raster as a style-only reference. Label edits additionally attached the image being edited as the first input.
- Post-processing: the generator returns RGBA with a transparent ground. Each accepted raster was alpha-composited onto the specified `#0D0906` ground and saved as opaque lossless RGB PNG at native size. No other pixel changes, no resizing.
- Run evidence (all attempts, logs, rejected rasters, reviews): `~/course-evidence/course-raster-visuals/20261002T233502`
- Module source contract: the current `module-10-capstone/README.md` title is “Stand up a local uncensored AI and hand it off”; its current Lab and `shared/PACKAGE.md` supersede the older logistics story for these visuals. `PACKAGE.md` is a raw exercise download, **not** a rendered page: use it as evidence only and do not insert images into it. Verify transition claims against `scripts/local_ai.py`. Do not copy unsupported promises about universal model refusal behavior into artwork.
- Owning page digests at integration (SHA-256): `README.md` b5f12075c0b764f2…; `shared/MODULE_10_LAB.md` 3ad2f28af0ff61c5…

## m10-evidence-boundaries

- Title: `MATCH EACH CLAIM TO ITS EVIDENCE`
- Publication path: `shared/figures/m10-evidence-boundaries.png`
- Anchor: Lab `## Prove one live interaction`, immediately after the opening explanation and before command blocks.
- Caption: Each check supports a narrow claim; neither a health probe nor a package-structure pass proves model quality or another person's operation.
- Native size: 1536×1024; published SHA-256: `7fd66410235792e7357e0f6bd28c1fad99fdb3a17d20f07cf90822e2c94b28ce`
- Iteration history:
  - attempt-01: full generation; session `01a1005f-5a30-75f2-b5e7-3a8c7f0b590d`; raw SHA-256 `fe04ec4e97d0193f…`; ACCEPTED
- Final review outcome: accepted attempt-01. FAcc: m10-evidence-boundaries: ACCEPT_A1 — all four rows and the four 'Not …' limits are legible.

### Final prompt

````text
## 1. Tool/output instruction

$imagegen Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

## 2. Lesson contract

- Owning page: Module 10 lab, `AI_Harness_Bootcamp_2/module-10-capstone/shared/MODULE_10_LAB.md`, H2 `## Prove one live interaction`. Insert immediately after the opening explanation and before the command blocks.
- Learning takeaway (caption, rendered as HTML text and not in the image): "Each check supports a narrow claim; neither a health probe nor a package-structure pass proves model quality or another person's operation."
- Learner action in unfamiliar work: for every PASS, write the single claim it actually supports, and list separately the conclusions no current check reaches.
- Misconception prevented: "All my checks passed, so the service is safe, good, production-ready, and transferable."

## 3. Composition

Figure category: evidence-to-claim matching table. Canvas 1536×1024 landscape, 64 px safe margin on all sides. Title zone across the top. The rest holds the mechanism. These are inline course images, so leave no slide-overlay space.

Zones:
- UPPER BAND: four equal, non-hierarchical horizontal rows of the same width and weight, with no ranking, numbering, or flow between rows. Each row is one panel. On the left is an evidence glyph cell (simple generic glyph: scale/digest, pulse probe, transcript lines, checklist). It connects by one short gold trace with an arrowhead to a narrow claim cell on the right. Each row's full label text spans the panel, with the evidence wording at the left and the claim wording at the right of the arrow already included in the label.
  1. `Size + digest → weight identity`
  2. `Health probe → reachable at probe time`
  3. `Live transcript → recorded interaction`
  4. `Structure check → named fields + local paths`
- LOWER BAND: a distinct region with a brick-red border holding four brick-red outlined pills in one row (or a 2×2 grid if needed for size): `Not safety`, `Not model quality`, `Not production readiness`, `Not independent transfer`. No arrow from any upper row enters this region. A thin barred separator line divides the bands.

Focal relationship: each evidence item points to exactly one narrow claim, and the lower region sits beyond every arrow's reach. Arrows mean only "supports this claim", never approval. No decorative connectors.

## 4. Verbatim label map

Title (top zone): `MATCH EACH CLAIM TO ITS EVIDENCE`

Evidence → claim rows (unnumbered, equal weight):
- `Size + digest → weight identity`
- `Health probe → reachable at probe time`
- `Live transcript → recorded interaction`
- `Structure check → named fields + local paths`

No-conclusion region:
- `Not safety`
- `Not model quality`
- `Not production readiness`
- `Not independent transfer`

Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Do not number the rows.

## 5. Visual family

`#0D0906` primary ground; `#17110C` panel fill; `#A58650` primary gold; `#C8A96A` sheen and connector highlights; `#C8B78A` secondary readable text; `#FFF8E7` primary text; `#655337` subdued nonessential rules; `#3A2E1B` faint structural lines; `#4F5634` restrained verified/allowed accents; `#B43A2F` warnings/blocked branches; `#2D3030` neutral mechanisms. Olive and brick red are fills, strokes, and pills only. Text is off-white or sandstone with high contrast, and every status has a text label as well as a color. No bright green, blue, cyan, teal, or purple. Do not use Starzl product names or product-specific color identities.

## 6. Richness and legibility

Subtle warm panel gradients, a thin gold sheen, and precise gold traces. Use restrained emission dots only on the four evidence→claim arrows. Modest inner and elevation shadows, sharp corners, and a faint survey-grid texture away from text. Warm, restrained operational luminance: not neon, sci-fi, or cinematic haze, and not a sterile flat wireframe. Use a clean Inter/Helvetica-like sans-serif. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density.

## 7. Honesty/exclusions

No scene, people or hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal or UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. No checkmarks, PASS stamps, or transcript text. Do not rank the evidence rows or chain them into a combined verdict. Do not imply that the four checks together reach any lower-band conclusion.

## 8. Generation self-check instruction

This must stay obvious: four separate, equal evidence→claim rows, and a walled-off region of four non-conclusions that no arrow reaches. The image is unusable if any of these happen: a row or pill is missing; the rows are numbered or ranked; an arrow enters the lower region; a combined verdict or checkmark appears; or any label is altered.
````

## m10-independent-transfer

- Title: `A DIFFERENT PERSON IS DIFFERENT EVIDENCE`
- Publication path: `shared/figures/m10-independent-transfer.png`
- Anchor: Lab `## Hand the package to another person`.
- Caption: Keep technical replay separate from another person's attempt, record every intervention, and mark human transfer unobserved when no recipient has operated the kit.
- Native size: 1536×1024; published SHA-256: `b90a40574b795d37f2c1dddb4a1dc3fe03c2292fc9aa6ebab85a1de3a35e1308`
- Iteration history:
  - attempt-01: full generation; session `01a10060-5d25-7930-92e7-f97ad0346d1c`; raw SHA-256 `015c27bb61ebc470…`; superseded — review: m10-independent-transfer: REGENERATE — avatar on Different person; title haze
  - attempt-02: full generation; session `01a10069-eb09-7902-95bb-f5a64b9832ec`; raw SHA-256 `b4c6bf05084a7d1c…`; ACCEPTED
- Final review outcome: accepted attempt-02. F0910: m10-independent-transfer: ACCEPT_A2 — Verbatim labels, including 'No recipient → UNOBSERVED'. There is no person avatar (A1 has one, which is banned). The three lanes are walled off, 'Not passed by substitution' is the barred stub on the replay lane, Questions / actions / outcomes → Record any help → Assisted stays assisted, and the red branch from 'Different person' leads to UNOBSERVED. This matches MODULE_10_LAB l.458-462 and RUNBOOK l.35. The bottom pills are about 28-29 px, slightly under the 32 px target, but still clearly legible as off-white on dark at 800 px width.

### Final prompt

````text
## 1. Tool/output instruction

$imagegen Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

## 2. Lesson contract

- Owning page: Module 10 lab, `AI_Harness_Bootcamp_2/module-10-capstone/shared/MODULE_10_LAB.md`, H2 `## Hand the package to another person`.
- Learning takeaway (caption, rendered as HTML text and not in the image): "Keep technical replay separate from another person's attempt, record every intervention, and mark human transfer unobserved when no recipient has operated the kit."
- Learner action in unfamiliar work: when claiming that a handoff works, record the author's rerun, any fresh-session or agent replay, and a different person's attempt as three distinct kinds of evidence. Log the recipient's questions, actions, outcomes, and help, and write "unobserved" when no person has tried it.
- Misconception prevented: "My clean rerun, or an agent replay, proves someone else can operate the kit", or "a helped attempt counts as independent."

## 3. Composition

Figure category: separated evidence lanes with a conditional branch. Canvas 1536×1024 landscape, 64 px safe margin on all sides. Title zone across the top. The rest holds three horizontal lanes in separate bordered panels. These are inline course images, so leave no slide-overlay space.

- LANE 1 (top, neutral `#2D3030`): `Author rerun`. Short, self-contained, with no arrow leaving the lane.
- LANE 2 (middle, neutral `#2D3030`): `Fresh-session technical replay`. Self-contained. At its right end is a brick-red barred stub labelled `Not passed by substitution`, showing this lane is blocked from reaching the person lane. No connector from lanes 1 or 2 reaches lane 3's observation.
- LANE 3 (bottom, gold-accented, the visual focus): `Different person` → `Package alone` (the fresh declared kit and ordinary access) → a record panel `Questions / actions / outcomes`, with a smaller attached tag `Record any help`. From `Record any help`, an olive-or-gold path leads to the pill `Assisted stays assisted`.
- BRANCH at the start of lane 3: a brick-red side branch drops from `Different person` to the pill `No recipient → UNOBSERVED`.

Focal relationship: only lane 3, a different person working from the package alone, produces the person observation. The replay lanes are walled off, a missing person yields UNOBSERVED, and help stays labelled as assisted. Arrows mean only sequence, never approval. No decorative connectors.

## 4. Verbatim label map

Title (top zone): `A DIFFERENT PERSON IS DIFFERENT EVIDENCE`

Lane 1:
- `Author rerun`

Lane 2:
- `Fresh-session technical replay`
- `Not passed by substitution`

Lane 3:
- `Different person`
- `Package alone`
- `Questions / actions / outcomes`
- `Record any help`
- `Assisted stays assisted`

Branch:
- `No recipient → UNOBSERVED`

Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Do not number the lanes.

## 5. Visual family

`#0D0906` primary ground; `#17110C` panel fill; `#A58650` primary gold; `#C8A96A` sheen and connector highlights; `#C8B78A` secondary readable text; `#FFF8E7` primary text; `#655337` subdued nonessential rules; `#3A2E1B` faint structural lines; `#4F5634` restrained verified/allowed accents; `#B43A2F` warnings/blocked branches; `#2D3030` neutral mechanisms. Olive and brick red are fills, strokes, and pills only. Text is off-white or sandstone with high contrast, and every status has a text label as well as a color. No bright green, blue, cyan, teal, or purple. Do not use Starzl product names or product-specific color identities.

## 6. Richness and legibility

Subtle warm panel gradients, a thin gold sheen, and precise gold traces. Use restrained emission dots only on lane 3's path. Modest inner and elevation shadows, sharp corners, and a faint survey-grid texture away from text. Warm, restrained operational luminance: not neon, sci-fi, or cinematic haze, and not a sterile flat wireframe. Use a clean Inter/Helvetica-like sans-serif. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density.

## 7. Honesty/exclusions

No scene, people or hands, silhouettes, faces, avatars, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal or UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Represent the person by a label only, not a figure. Do not show any recipient success, PASS, or checkmark. Do not show an agent, robot, or checker reaching the person lane.

## 8. Generation self-check instruction

This must stay obvious: three separate lanes, with only the different-person lane producing an observation record. The replay lanes are blocked by `Not passed by substitution`, a missing person branches to `No recipient → UNOBSERVED`, and help leads to `Assisted stays assisted`. The image is unusable if any of these happen: a connector runs from lanes 1 or 2 into lane 3; the UNOBSERVED branch or `Record any help` is missing; a success mark or person illustration appears; or any label is altered.

## 9. Revision requirements from review of the previous attempt
A previous generation of this figure was rejected. Generate a NEW image from this full contract and fix every defect below. All earlier blocks still govern; labels stay verbatim; add no words.

Transcription: "A DIFFERENT PERSON IS DIFFERENT EVIDENCE" | "Author rerun" | "Fresh-session technical replay" | "Not passed by substitution" | "Different person" → "Package alone" → "Questions / actions / outcomes" | "Record any help" → "Assisted stays assisted" | "No recipient → UNOBSERVED". All labels are verbatim and the → sign is correct. The lane separation, UNOBSERVED branch, and assisted path match MODULE_10_LAB.md lines 460–462 and the facilitator RUNBOOK. Defects: (1) `Different person` has a circular person avatar (head-and-shoulders silhouette). The prompt bans "silhouettes, faces, avatars" and says to represent the person by a label only. Its self-check lists "a person illustration appears" as making the image unusable. (2) The title sits in a bright cream glow that bleeds across the top edge. That is the cinematic haze the style rules exclude. The title face is also visibly compressed or condensed, unlike the rest of the M10 set, and sits closer to the top than the 64 px safe margin. Fix by regenerating with the same three-lane layout, using a text-only `Different person` node or a neutral non-human glyph, and no glow behind the title. Set the title in the same Inter/Helvetica-like weight as the other M10 figures, at about 60 px, inside the safe margin.
````

## m10-launch-approval

- Title: `THE OPERATOR APPROVES THE LAUNCH`
- Publication path: `shared/figures/m10-launch-approval.png`
- Anchor: Lab `## Bring the service up under OMP orchestration`, after the introductory explanation and before the orchestration brief.
- Caption: OMP drafts the launch line, but you check it against the pinned boundary and start the server; reachability is a separate probe.
- Native size: 1536×1024; published SHA-256: `c1ccf62db015f880a51ca5e8584e7039a03553a8e33507d53a6d4a0b43e0de4f`
- Iteration history:
  - attempt-01: full generation; session `01a10061-5908-7a20-aeb6-c12b630a3f37`; raw SHA-256 `058d7afab5009612…`; ACCEPTED
- Final review outcome: accepted attempt-01. FAcc: m10-launch-approval: ACCEPT_A1 — the dashed reject loop and both HOLD paths are visible.

### Final prompt

````text
## 1. Tool/output instruction

$imagegen Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

## 2. Lesson contract

- Owning page: Module 10 lab, `AI_Harness_Bootcamp_2/module-10-capstone/shared/MODULE_10_LAB.md`, H2 `## Bring the service up under OMP orchestration`. Insert after the introductory paragraph and before the orchestration brief.
- Learning takeaway (caption, rendered as HTML text and not in the image): "OMP drafts the launch line, but you check it against the pinned boundary and start the server; reachability is a separate probe."
- Learner action in unfamiliar work: when an agent drafts a command that opens a service, check its bind and limits against the written boundary before running it yourself. Reject a wrong draft rather than editing around it, and confirm the result with an independent probe.
- Misconception prevented: "The agent's drafted launch line, or the fact that I ran it, means the service is up and correctly bounded."

## 3. Composition

Figure category: conditional flow with an operator gate. Canvas 1536×1024 landscape, 64 px safe margin on all sides. Title zone across the top. The rest holds the mechanism in two rows. These are inline course images, so leave no slide-overlay space.

Top row, left to right:
- Two input tiles stacked at the left, `Checked weights` and `Wired loopback config`. Both feed one gold arrow into the node `OMP drafts launch line`, drawn as a neutral `#2D3030` draft (a proposal, not running).
- Arrow → a gate node `Check: 127.0.0.1 + context 32768` (the operator's check, the visual focus).
- From the gate, a downward brick-red branch to a blocked pill `Wrong bind → reject line`. This branch loops back only toward `OMP drafts launch line` with a thin dashed brick-red return, and never reaches the server.

Bottom row, left to right, continuing from the gate's passing branch:
- Gold arrow → `Operator starts server`.
- A clearly separate gap, then a distinct probe step `Health probe`, drawn as an independent observation and not a continuation of the draft.
- From `Health probe`, a brick-red branch to a pill `Unreachable → HOLD`.

Focal relationship: the operator's check gate sits between the drafted line and starting the server. Reachability is a separate probe after the start. No arrow from `OMP drafts launch line` goes straight to a running state. Arrows mean only sequence or condition, never approval. No decorative connectors.

## 4. Verbatim label map

Title (top zone): `THE OPERATOR APPROVES THE LAUNCH`

Inputs:
- `Checked weights`
- `Wired loopback config`

Draft and gate:
- `OMP drafts launch line`
- `Check: 127.0.0.1 + context 32768`
- `Wrong bind → reject line`

Start and observation:
- `Operator starts server`
- `Health probe`
- `Unreachable → HOLD`

Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. No Yes/No edge words are needed; the arrow labels are given above.

## 5. Visual family

`#0D0906` primary ground; `#17110C` panel fill; `#A58650` primary gold; `#C8A96A` sheen and connector highlights; `#C8B78A` secondary readable text; `#FFF8E7` primary text; `#655337` subdued nonessential rules; `#3A2E1B` faint structural lines; `#4F5634` restrained verified/allowed accents; `#B43A2F` warnings/blocked branches; `#2D3030` neutral mechanisms. Olive and brick red are fills, strokes, and pills only. Text is off-white or sandstone with high contrast, and every status has a text label as well as a color. No bright green, blue, cyan, teal, or purple. Do not use Starzl product names or product-specific color identities.

## 6. Richness and legibility

Subtle warm panel gradients, a thin gold sheen, and precise gold traces. Use restrained emission dots only on the main passing path. Modest inner and elevation shadows, sharp corners, and a faint survey-grid texture away from text. Warm, restrained operational luminance: not neon, sci-fi, or cinematic haze, and not a sterile flat wireframe. Use a clean Inter/Helvetica-like sans-serif, with monospace for `127.0.0.1` and `32768`. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density.

## 7. Honesty/exclusions

No scene, people or hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal or UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Do not render the command line itself, a terminal window, load times, or a PASS readout. Do not show the agent starting the server. Do not equate a drafted line with a running service, and do not show any path from a wrong bind to launch.

## 8. Generation self-check instruction

This must stay obvious: drafted line → operator check → operator starts server → separate health probe. A wrong bind exits to rejection, and an unreachable probe exits to HOLD. The image is unusable if any of these happen: the check gate is missing; the reject branch reaches the server; the probe merges with the start step; `Unreachable → HOLD` is missing; there is an arrow from the draft straight to a running state; or any label is altered.
````

## m10-operator-boundary

- Title: `LOCAL DOES NOT MEAN SAFE`
- Publication path: `shared/figures/m10-operator-boundary.png`
- Anchor: Lab `## Read the boundary before the first launch`.
- Caption: Loopback limits network reach, and the identity check identifies the checked weight file; neither establishes the model's safety, accuracy, or fitness for publication.
- Native size: 1536×1024; published SHA-256: `af68e50d95e4395dbec4f2aea347c8220efc9261d48b95bdbce001fca4eb7686`
- Iteration history:
  - attempt-01: full generation; session `01a10062-7926-7d81-ac8f-3627d10b9904`; raw SHA-256 `8b4e0347e8befda2…`; superseded — review: m10-operator-boundary: REGENERATE — identity line crosses recording strip
  - attempt-02: full generation; session `01a10068-f794-78f1-9f26-01fe5bab89c7`; raw SHA-256 `08993a26f647016c…`; ACCEPTED
- Final review outcome: accepted attempt-02. F0910: m10-operator-boundary: ACCEPT_A2 — All 9 strings are verbatim, with '127.0.0.1 only' in monospace and the ≠ intact. The recording strip now sits only under 'One operator' at ≥32 px, and the identity connector leaves 'Local weights' crossing nothing but the boundary edge. The only output arrow goes to 'Operator reviews output', both blocked pills have barred stubs, and there is no shield or lock. This matches local_ai.py LOOPBACK (l.34, l.302-303). A1's flattened.png is a 33-byte undecodable file, so it cannot be a candidate.

### Final prompt

````text
## 1. Tool/output instruction

$imagegen Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

## 2. Lesson contract

- Owning page: Module 10 lab, `AI_Harness_Bootcamp_2/module-10-capstone/shared/MODULE_10_LAB.md`, H2 `## Read the boundary before the first launch`.
- Learning takeaway (caption, rendered as HTML text and not in the image): "Loopback limits network reach, and the identity check identifies the checked weight file; neither establishes the model's safety, accuracy, or fitness for publication."
- Learner action in unfamiliar work: when running any local model or tool, draw the network boundary and the human review gate separately. Treat file-identity checks as narrow identification, and personally review output before it goes anywhere.
- Misconception prevented: "It runs locally and the file hash matched, so it is safe."

## 3. Composition

Figure category: boundary and review-gate diagram. Canvas 1536×1024 landscape, 64 px safe margin on all sides. Title zone across the top. The rest of the canvas holds the mechanism. These are inline course images, so leave no slide-overlay space.

Zones and relationships:
- CENTER-LEFT: a sharp-cornered loopback service boundary panel with the header `127.0.0.1 only`. Inside it are a node `One operator`, a node `Local weights`, and a recording strip `Prompts + replies recorded` along the bottom inner edge. A short gold request/reply trace runs between `One operator` and `Local weights` inside the boundary.
- CENTER-RIGHT: one gold arrow leaves the boundary to a gate node `Operator reviews output`. Proposed output goes there, and only there.
- FAR RIGHT, outside the boundary: two brick-red blocked pills, `No shared endpoint` and `No traffic for other people`. Each sits against a short brick-red barred stub at the boundary edge. No arrow from inside the boundary reaches beyond these pills, and no arrow goes straight from the model to anywhere except the review gate.
- BOTTOM: a small, separate, neutral `#2D3030` side panel `Identity ≠ safety or accuracy`. It attaches by one thin line only to `Local weights`, as a limited check. It must NOT enclose or shield the service boundary.

Focal relationship: everything the model produces goes to `Operator reviews output`. The loopback boundary limits network reach, and the identity check is a separate narrow panel. Arrows mean only data flow, never approval. No decorative connectors.

## 4. Verbatim label map

Title (top zone): `LOCAL DOES NOT MEAN SAFE`

Service boundary:
- `127.0.0.1 only` (boundary header)
- `One operator`
- `Local weights`
- `Prompts + replies recorded`

Review gate:
- `Operator reviews output`

Blocked pills outside the boundary:
- `No shared endpoint`
- `No traffic for other people`

Separate limited check:
- `Identity ≠ safety or accuracy`

Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. `127.0.0.1` uses clean monospace.

## 5. Visual family

`#0D0906` primary ground; `#17110C` panel fill; `#A58650` primary gold; `#C8A96A` sheen and connector highlights; `#C8B78A` secondary readable text; `#FFF8E7` primary text; `#655337` subdued nonessential rules; `#3A2E1B` faint structural lines; `#4F5634` restrained verified/allowed accents; `#B43A2F` warnings/blocked branches; `#2D3030` neutral mechanisms. Olive and brick red are fills, strokes, and pills only. Text is off-white or sandstone with high contrast, and every status has a text label as well as a color. No bright green, blue, cyan, teal, or purple. Do not use Starzl product names or product-specific color identities.

## 6. Richness and legibility

Subtle warm panel gradients, a thin gold sheen, and precise gold traces. Use restrained emission dots only on the request/reply trace and the arrow to review. Modest inner and elevation shadows, sharp corners, and a faint survey-grid texture away from text. Warm, restrained operational luminance: not neon, sci-fi, or cinematic haze, and not a sterile flat wireframe. Use a clean Inter/Helvetica-like sans-serif. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density.

## 7. Honesty/exclusions

No scene, people or hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal or UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. No shield, lock, or padlock icon that suggests safety. No model name, port number, or digest. Do not imply that the model refuses, filters, or warns, or that loopback or identity makes output safe, accurate, or publishable. No arrow straight to publishing or to other people.

## 8. Generation self-check instruction

This must stay obvious: model output leaves the loopback boundary only into `Operator reviews output`, and the identity check is a small separate panel, not an enclosing shield. The image is unusable if any of these happen: a blocked pill is missing; there is an arrow past the boundary to other people; the identity panel encloses the service; `Prompts + replies recorded` is missing; a shield or lock motif appears; or any label is altered.

## 9. Revision requirements from review of the previous attempt
A previous generation of this figure was rejected. Generate a NEW image from this full contract and fix every defect below. All earlier blocks still govern; labels stay verbatim; add no words.

Transcription: "LOCAL DOES NOT MEAN SAFE" | "127.0.0.1 only" | "One operator" | "Local weights" | "Prompts + replies recorded" | "Operator reviews output" | "No shared endpoint" | "No traffic for other people" | "Identity ≠ safety or accuracy". Every label is verbatim, the ≠ sign is correct, nothing is added, and there is no shield or lock. Defects: (1) The thin line from `Local weights` down to `Identity ≠ safety or accuracy` passes straight through the `Prompts + replies recorded` strip at x≈745. It looks like the identity check attaches to or runs through the recording. This is the ambiguous crossing that acceptance criterion 4 forbids, and it blurs the point that identity is a separate narrow check. (2) The `Prompts + replies recorded` text is about 26 px, below the 32 px minimum, and its tan text is lower contrast than the other labels. Fix by regenerating with the same composition and two changes. Make the recording strip span only the left half of the boundary's bottom inner edge, under `One operator`, or keep it full width and route the identity connector down the boundary's right side. The connector must exit `Local weights` without crossing any other element. Render the strip text at 32 px or more in off-white #FFF8E7. Keep everything else, which matches the source (PACKAGE.md Bounds; local_ai.py LOOPBACK).
````

## m10-package-boundary

- Title: `TRANSFER THE DECLARED KIT`
- Publication path: `shared/figures/m10-package-boundary.png`
- Anchor: Overview `## Start here`; replace `m10-package.svg`.
- Caption: Transfer only the declared, digest-checked files; the recipient downloads weights separately, and evidence and conversation history stay outside the kit.
- Native size: 1536×1024; published SHA-256: `6f717ce89595e9e4a716e23634c6b69406366e77cbf751851a6eea5b6f1e2465`
- Iteration history:
  - attempt-01: full generation; session `01a10063-67a0-7e92-adda-9d44ba998042`; raw SHA-256 `1bdf4cf5f29bddb2…`; ACCEPTED
- Final review outcome: accepted attempt-01. FAcc: m10-package-boundary: ACCEPT_A1 — the dashed exclusion boxes and the empty received slots show on the dark ground.

### Final prompt

````text
## 1. Tool/output instruction

$imagegen Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

## 2. Lesson contract

- Owning page: Module 10 overview, `AI_Harness_Bootcamp_2/module-10-capstone/README.md`, H2 `## Start here`. This image replaces `m10-package.svg`.
- Learning takeaway (caption, rendered as HTML text and not in the image): "Transfer only the declared, digest-checked files; the recipient downloads weights separately, and evidence and conversation history stay outside the kit."
- Learner action in unfamiliar work: before handing any runnable kit to another person, list the paths it declares. Freeze their digests, copy only those members into a fresh folder, and verify each copy. Large licensed assets, local evidence, and conversation history stay outside the kit.
- Misconception prevented: "Hand-off means zipping my working folder", meaning the weights, evidence, chat history, or stop receipt travel inside the package.

## 3. Composition

Figure category: containment and transfer diagram. Canvas 1536×1024 landscape, 64 px safe margin on all sides. Title zone across the top. The rest of the canvas holds the mechanism. These are inline course images, so leave no slide-overlay space.

Zones and relationships, read left to right:
- LEFT (largest): a nested, bordered declared-package region containing five stacked member tiles: `shared/PACKAGE.md`, `scripts/`, `shared/case/`, `shared/controls/`, `shared/baseline/`. Show them as one enclosed set with a single gold outline.
- CENTER: one gold transfer path leaves the declared region. It passes first through a step node `Freeze declared paths`, then through a step node `Digest-checked copy`, and ends at the RIGHT-TOP region.
- RIGHT-TOP: a clean, separate bordered region `Fresh received folder`. The transfer arrow ends here. Inside it are five faint generic tile outlines (no text) to show the same declared members arriving.
- BOTTOM ROW (separate, outside the declared region, and not connected by any transfer path): three external regions with dashed brick-red or muted borders: `Weights: downloaded separately`, `Evidence: retained separately`, `No chat history`. No arrow connects them to the fresh received folder. The weights region may carry a thin, separate muted line to the right edge of the received folder, labelled only by its own label text, to suggest the recipient fetches it independently. Do not draw it as part of the copy path.

Focal relationship: the single gold path from declared package → freeze → digest-checked copy → fresh received folder. Excluded regions visibly do not travel. Arrows mean only "copied as a declared member"; they never mean approval. No decorative connectors. Prefer two rows to tiny type.

## 4. Verbatim label map

Title (top zone): `TRANSFER THE DECLARED KIT`

Declared-package region, member tiles:
- `shared/PACKAGE.md`
- `scripts/`
- `shared/case/`
- `shared/controls/`
- `shared/baseline/`

Transfer path steps:
- `Freeze declared paths`
- `Digest-checked copy`

Destination region:
- `Fresh received folder`

External regions (bottom row):
- `Weights: downloaded separately`
- `Evidence: retained separately`
- `No chat history`

Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. No total file count. Paths use a clean monospace face.

## 5. Visual family

`#0D0906` primary ground; `#17110C` panel fill; `#A58650` primary gold; `#C8A96A` sheen and connector highlights; `#C8B78A` secondary readable text; `#FFF8E7` primary text; `#655337` subdued nonessential rules; `#3A2E1B` faint structural lines; `#4F5634` restrained verified/allowed accents; `#B43A2F` warnings/blocked branches; `#2D3030` neutral mechanisms. Olive and brick red are fills, strokes, and pills only. Text is off-white or sandstone with high contrast, and every status has a text label as well as a color. No bright green, blue, cyan, teal, or purple. Do not use Starzl product names or product-specific color identities.

## 6. Richness and legibility

Subtle warm panel gradients, a thin gold sheen, and precise gold traces. Use restrained emission dots only on the transfer path. Modest inner and elevation shadows, sharp corners, and a faint survey-grid texture away from text. Warm, restrained operational luminance: not neon, sci-fi, or cinematic haze, and not a sterile flat wireframe. Use a clean Inter/Helvetica-like sans-serif, with clean monospace for paths. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density.

## 7. Honesty/exclusions

No scene, people or hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal or UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. Generic document or folder glyphs are allowed only to show containment. No file count, byte size, model name, or digest string. Do not draw a stop receipt, log, or transcript as a copied package member. Do not imply that the copy proves another person can operate the kit.

## 8. Generation self-check instruction

This must stay obvious: only the five declared members travel, through freeze and digest-checked copy, into the fresh received folder, and the weights, evidence, and chat history sit outside with no transfer arrow. The image is unusable if any of these happen: a declared path label is missing; the freeze or copy step is missing; an excluded region connects to the copy path; a file count appears; or any label is altered.
````

## m10-stop-restore

- Title: `RESTORING CONTROL IS NOT RESTARTING`
- Publication path: `shared/figures/m10-stop-restore.png`
- Anchor: Lab `## Disable the control and prove the refusal`, after the introductory paragraph, referring to the preceding actual stop.
- Caption: The operator stops the process; the adapter verifies the stopped state. Restoring an enabled control does not itself restart the service.
- Native size: 1536×1024; published SHA-256: `f4f3f74981b7602488e10be086876ef1a57f0b46e72cda0d517a335f657f3d7e`
- Iteration history:
  - attempt-01: full generation; session `01a10064-51a5-7693-9934-7e809912aeff`; raw SHA-256 `6c831c803866e8b9…`; superseded — review: m10-stop-restore: REGENERATE — person/hand/shield glyphs and undersized lane text
  - attempt-02: full generation; session `01a10069-e5cf-7d03-9c74-26adb3ce79b0`; raw SHA-256 `fd748500a182024a…`; ACCEPTED
- Final review outcome: accepted attempt-02. F0910: m10-stop-restore: ACCEPT_A2 — All labels are verbatim, with no person, hand or shield glyphs and no check mark. 'Restore control' has only an olive stroke and dead-ends at 'No automatic restart'. 'Restart requires launch + probe' is isolated with no incoming arrow, and 'HOLD: control disabled' is a dead end. The two lanes never touch. The top-lane order is Ctrl+C → probe unreachable → receipt → stop verify, which matches MODULE_10_LAB l.260-317 and local_ai.py l.207-208 and l.346-349.

### Final prompt

````text
## 1. Tool/output instruction

$imagegen Use the built-in image_gen tool to generate exactly ONE original instructional PNG. Do not use a CLI image fallback or write code/SVG to draw the image. The attachments are STYLE references only. Do not copy their subjects or labels. Return the absolute saved PNG path and no claim of verification.

## 2. Lesson contract

- Owning page: Module 10 lab, `AI_Harness_Bootcamp_2/module-10-capstone/shared/MODULE_10_LAB.md`, H2 `## Disable the control and prove the refusal`. Insert after the introductory paragraph; the figure refers back to the stop already performed in `## Stop the service and prove the stopped state`.
- Learning takeaway (caption, rendered as HTML text and not in the image): "The operator stops the process; the adapter verifies the stopped state. Restoring an enabled control does not itself restart the service."
- Learner action in unfamiliar work: keep the process lifecycle (stop, then verify stopped) separate from configuration-gate state (disabled, then refused, then restored). Claim a running service only after an explicit launch and a fresh probe.
- Misconception prevented: "The adapter's stop command killed the server", "a control-disabled refusal shows the service is down", or "restoring the control brought the service back."

## 3. Composition

Figure category: two-lane state contrast. Canvas 1536×1024 landscape, 64 px safe margin on all sides. Title zone across the top. The rest holds two clearly separated horizontal lanes, each in its own bordered panel, with a visible gap between them. These are inline course images, so leave no slide-overlay space.

TOP LANE (process lifecycle), left to right with gold arrows:
`Operator stops process` → `Probe: unreachable` → `Stop receipt` → `Verify stopped`. The first node is drawn as the operator's own action. `Verify stopped` is drawn as the adapter checking the receipt and confirming the port is unreachable, a verification step and not an action that ends anything.

BOTTOM LANE (control gate), left to right:
`Control disabled` → a brick-red pill `HOLD: control disabled`. This refusal is a dead end: no line connects it to `Probe: unreachable` or `Verify stopped`, because a gate refusal is not a health observation. Then, separately within the same lane: `Validate baseline digest` → `Restore control` (olive accent).

RIGHT EDGE, after `Restore control`: a barred brick-red stop marker labelled `No automatic restart`. There is NO arrow from `Restore control` to any running-service state or back to the top lane. Beside it sits a separate, isolated neutral `#2D3030` note node `Restart requires launch + probe`, with no incoming arrow from `Restore control`.

Focal relationship: the two lanes never merge. Restoring the control dead-ends at `No automatic restart`, and the gate refusal never counts as stop evidence. Arrows mean only sequence, never approval. No decorative connectors.

## 4. Verbatim label map

Title (top zone): `RESTORING CONTROL IS NOT RESTARTING`

Top lane (process):
- `Operator stops process`
- `Probe: unreachable`
- `Stop receipt`
- `Verify stopped`

Bottom lane (control):
- `Control disabled`
- `HOLD: control disabled`
- `Validate baseline digest`
- `Restore control`

Right edge:
- `No automatic restart`
- `Restart requires launch + probe`

Render every label exactly as written and in its assigned region. Do not invent, translate, abbreviate, duplicate, or add words, figures, tick marks, axes, timestamps, percentages, or status readouts. Do not number the steps.

## 5. Visual family

`#0D0906` primary ground; `#17110C` panel fill; `#A58650` primary gold; `#C8A96A` sheen and connector highlights; `#C8B78A` secondary readable text; `#FFF8E7` primary text; `#655337` subdued nonessential rules; `#3A2E1B` faint structural lines; `#4F5634` restrained verified/allowed accents; `#B43A2F` warnings/blocked branches; `#2D3030` neutral mechanisms. Olive and brick red are fills, strokes, and pills only. Text is off-white or sandstone with high contrast, and every status has a text label as well as a color. No bright green, blue, cyan, teal, or purple. Do not use Starzl product names or product-specific color identities.

## 6. Richness and legibility

Subtle warm panel gradients, a thin gold sheen, and precise gold traces. Use restrained emission dots only on in-lane arrows. Modest inner and elevation shadows, sharp corners, and a faint survey-grid texture away from text. Warm, restrained operational luminance: not neon, sci-fi, or cinematic haze, and not a sterile flat wireframe. Use a clean Inter/Helvetica-like sans-serif. Title about 60 px; major labels at least 38 px; all essential copy at least 32 px at 1536 px width. Never dim essential words into low-contrast tan. Clear hierarchy beats ornamental density.

## 7. Honesty/exclusions

No scene, people or hands, vehicles, monitor bezel, desk, room, horizon, photography, faux terminal or UI, fabricated live data, numerical results, approvals, course scores, real operational claims, or revealed exercise answers. No power-button or kill icon on `Verify stopped`. Do not invent a restore subcommand or command text. Do not let the adapter appear to terminate the process. Do not draw any arrow from the control lane into the process lane, or from `Restore control` to a running state.

## 8. Generation self-check instruction

This must stay obvious: two separate lanes. The process is stopped by the operator and verified by the adapter. The control lane's refusal and restore never touch the process lane, and restore ends at `No automatic restart`. The image is unusable if any of these happen: there is an arrow from `Restore control` to a running or restarted state; `HOLD: control disabled` connects to the stop evidence; `Verify stopped` looks like the action that ends the process; `No automatic restart` or `Restart requires launch + probe` is missing; or any label is altered.

## 9. Revision requirements from review of the previous attempt
A previous generation of this figure was rejected. Generate a NEW image from this full contract and fix every defect below. All earlier blocks still govern; labels stay verbatim; add no words.

Transcription: "RESTORING CONTROL IS NOT RESTARTING" (wrapped onto 2 lines) | top lane: "Operator stops process" → "Probe: unreachable" → "Stop receipt" → "Verify stopped" | bottom lane: "Control disabled" → "HOLD: control disabled"; "Validate baseline digest" → "Restore control" → [red minus marker] "No automatic restart"; "Restart requires launch + probe". All labels are verbatim and nothing is added. The structure matches local_ai.py: the enabled check returns `HOLD: control disabled` at line 208 before any command runs, `stop` only validates the receipt and probes (lines 321–350), the operator interrupts the process (PACKAGE.md Stop), and no lane crosses into the other. Defects: (1) `Operator stops process` has a person-silhouette glyph and the `HOLD: control disabled` pill has a raised-hand glyph. Section 7 of the prompt excludes "people or hands". (2) `Restore control` carries an olive shield with a check mark. That reads as a safety or verified-approval badge on the restore step, the same false-assurance motif the module's operator-boundary figure bans, and it pulls attention to restore as a success. (3) Bottom-lane copy (`Validate baseline digest`, `Restore control`, `No automatic restart`, `Restart requires launch + probe`) is about 24–28 px, below the 32 px minimum. At article width it is the hardest text in the M10 set to read. Fix by regenerating the same two-lane layout without person, hand, or shield glyphs: use a plain text-only node or a neutral process glyph, keep the restore node's olive accent as a stroke only, and use no check mark. Give the bottom lane more height, or move `Restart requires launch + probe` below `No automatic restart` with a full-width allowance, so every label is at least 32 px.
````

