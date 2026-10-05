# Reference: Module 6 — Design a workflow for a decision model

**Frozen on:** 2026-10-04 (revision 4; replaces the observed-run predicate module)
**Scope:** one Wednesday block of about three hours built around eighty fictional AI-drafted handoff notes `BG-001`–`BG-080` for oxygen cylinders moving from East Yard to Clinic O-2, with one scan record per note
**Course objective:** select and pin a structured decision model as OMP's judge through OpenRouter, design the questions and code split for that model class, set risk-weighted thresholds from tuning answers, freeze them, and measure the frozen screen once on held-out notes, including the build that answered and the cost

## 1. The need

Module 04 taught the learner to give an AI judgment a shape: atomic typed questions, labels frozen before a run, routing in code, gates set from measurement. Its decision function was the course chat model, whose confidence is self-declared. A professional who automates a judgment at volume now has a second kind of model available: a decision model that returns typed answers with probabilities from the model itself, at a small fraction of a chat model's cost and latency, and that writes no prose. Using one well is a distinct capability: choose and pin it in the harness, design around its documented weak spots, place thresholds by the cost of each error, and prove the frozen design on data the learner did not tune on.

Capability delta: before, the learner could decompose a decision into typed questions answered by the chat model and gate on its declared confidence. After, the learner can select, pin, and operate a dedicated decision model in their own harness, design a question set and code split for its failure modes, set thresholds from its probabilities on tuning data, and prove the frozen screen on held-out data with build identity and cost.

## 2. Sources

TypeSafe documentation, read 2026-10-04:

- [How to build with TypeSafe](https://docs.typesafe.ai/concepts/how-to-build-with-system-one): code owns control flow; decompose the state and the questions; atomic questions; structure in questions; ask many questions in one request; combine answers in code; route on uncertainty.
- [Patterns](https://docs.typesafe.ai/patterns): speculative fan-out, confidence-gated routing, composite scoring, intent routing.
- [Primitives](https://docs.typesafe.ai/primitives), [Noul](https://docs.typesafe.ai/primitives/noul), [Confidence](https://docs.typesafe.ai/confidence): Choice, Score, and Noul; phrase a Noul so a high value means yes; one condition per Noul; thresholds by error cost with a middle band to a person; Choice confidence `(p_max − 1/n)/(1 − 1/n)`; Score confidence by distance from the peak level.
- [Jev 1.13 jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13) (reviewed 2026-10-02): literal reading; math and counting; date and time comparison; indirection; large irrelevant state; adversarial content; contradictory instructions and criteria; Choice option order (leans to the first option); no generation.
- Cookbooks: self-consistency for Nouls and Choices (illustrative bands, not fitted), citation check (`supports` / `contradicts` / `says_nothing`, auto-accept at 0.8 as a starting point), guardrails (instruction-override hazard Noul), SDE cascade (per-field error Nouls, any-gate), date extraction (`none` options, arithmetic in code), parallel questions (13 questions batched: 12.2x cheaper, 10.0x faster, unchanged answers).
- OpenRouter: [Jev hub](https://openrouter.ai/docs/guides/community/jev.md) (Decisions API `POST /api/alpha/decisions`; System One API `POST /api/v1/systemone`; OpenRouter key only; input billed, output free; 32,000-token context; `~typesafe/jev-latest` follows the newest release), [Gate agent tool calls with Jev](https://openrouter.ai/docs/cookbook/building-agents/gate-tool-calls-with-jev) (approve only if every Noul ≥ 0.9, block if any ≤ 0.1, review otherwise; never treat a failed check as approval), [Classify and tag text at scale](https://openrouter.ai/docs/cookbook/evaluate-and-optimize/jev-classification) (thresholds from 100–200 labeled items; 150-item calibration: confidence ≥ 0.8 right on 114/122, 0.5–0.8 on 9/18, below 0.5 on 4/10).
- TypeSafe's launch post (2026-09-15) states Jev's type safety as a guarantee and its speed, cost, and calibration from its own workflow evals against reference models. Treat those as vendor claims; the module measures only its own sample.

Historical Oh My Pi observations at tag `v18.3.5` follow. Current installation tracks the latest stable release; the launcher records its actual version rather than requiring this historical tag.

- `modelRoles.judge` selects the judge role chain (`packages/coding-agent/src/config/model-roles.ts`, `src/judgment/index.ts`). OpenRouter models whose API is `openrouter-decisions` go to the Decisions endpoint (`docs/models.md`). After the first native judge in a chain, only native candidates remain, so a failed Jev call does not fall back to a prompted chat model.
- Eval exposes `judge` and `judgeBatch` in JS (`judge_batch` in Python). The bridge maps `bool` to Noul and returns `{type: "bool", bool}`; `choice` and `score` keep their names (`src/eval/judgment-bridge.ts`). Choice option descriptions must be strings in this version (observed: object descriptions are refused).
- Batch items carry `model`; `status()` carries `model`, `cost`, `done`, `failed`, and `running` (`src/eval/judgment-batch-bridge.ts`, `src/eval/js/shared/prelude.txt`).
- `omp models --kind judge --json` lists judge candidates for the credentials present. A `--config` overlay can set `modelRoles.judge` for one run. `omp config set modelRoles.judge` is not a known CLI key in 18.3.5 (observed).
- The `jevify` notice in 18.3.5 still teaches the removed handle API; the lab does not use it.

## 3. Case

Desk rules: `DESK_RULES.md`. Scan ranks `HELD` < `RECEIVED` < `INSPECTED` < `RELEASED`; a release order exists exactly for `RELEASED`. Routes `PASS`, `RETURN` (overstates), `REVIEW` (instruction, other cylinder, or unsettled). Two errors the desk cannot accept: an overstating note that passes, and an instruction that reaches no person.

Eighty notes, each with one label (`overstates`, `instructs`, `other_cylinder`, `note_status`, `why`). Tuning `BG-001`–`BG-020`: seven overstatements, two instructions, one other cylinder. Held-out `BG-021`–`BG-080`: seventeen overstatements, six instructions, three other-cylinder notes. Traps: release claims without the word released ("good to go", "cleared", "okay to load"); negated, pending, conditional, and expected releases; cautions that keep a control in place; embedded instructions with and without a release claim; a cited order the scan record lacks; status claims on held cylinders; a vendor tag reading `READY` beside a received status (`BG-078`).

The state sent to the model is the note text alone. The scan record, cylinder ID comparison, cited-order comparison, and scan-rank comparison stay in code.

## 4. Mechanics

- `shared/run_omp.py` judge profile: validates `JUDGE.yml` (exactly the two-line setting, pinned model selector only), the question file's supported judge shapes, and the states folder; records the actual OMP version; freezes the questions, setting, and plan into the evidence folder; overlays `modelRoles.judge`; exposes only `eval`; and after the run checks one completed frozen cell, every answer's shape against the frozen questions, one served `jev-1.13` build, a finished batch with cost, and no work-folder change beyond the declared output. `--list-judges` saves the candidate list and actual runtime version with no model call.
- `shared/course_guard.mjs`: in a judge run, allows `eval` only for the frozen cell in JS, once, and aborts if any judge input changes.
- `shared/judge_runner.mjs`: reads the plan, runs one `judgeBatch` with no retries, drains to a deadline, cancels unfinished work, and writes `judgments.jsonl` and `batch-status.json` exclusively.
- `scripts/blue_gauge.py`: `check-questions` (router contract and design rules a file can show), `report`, `spread`, `freeze`, `measure`, `verify`. Router order: other cylinder → cited order → instruction → scan holds a release order → release claim or settled status above the scan → unsettled status → pass below → review. A missing judgment never passes. `verify` audits completed tuning runs and lists held ones as kept; the first tuning run with saved judgments sets the first-miss comparison whatever its recorded status, so relabelling a run cannot excuse its misses.

## 5. Observed staff runs, 2026-10-04

Pinned OMP 18.3.5 (`omp-darwin-arm64`, checksum verified against the release `SHA256SUMS.txt`), isolated home, OpenRouter key only. Private evidence: `~/course-evidence/module06-decision-model-20261004-maintainer-live/` and its `-attempt-1` sibling.

- `--list-judges`: eleven candidates, including `openrouter/typesafe/jev-1.13`, `openrouter/~typesafe/jev-latest`, and `openrouter/typesafe/jev-router`.
- Every judge run was answered by `openrouter/typesafe/jev-1.13-20260917`. A YAML `JUDGE.yml` passed directly as `omp --config` also routed `judgeBatch` to that build.
- Development run, worked set frozen from its first tuning run at 0.6 / 0.6 / 0.2 / 0.4 and a 40% ceiling: held-out no critical error, one wrong return (`BG-078`), sixteen reviews (27%); Jev USD 0.00234 for sixty notes. `BG-036` changed its status answer with option order and went to review.
- Final Bash run, the lab's commands from a fresh preparation:
  - The starter set held on nine named problems. Tuning-1 with the worked set as the first repair: question misses on `BG-002` and `BG-008` (status claims read as instructions), `BG-006` (an instruction read as a release), `BG-011` (a caution read as a hold), and `BG-019` (status changed with option order and went to review).
  - First-miss notes, then a criteria-only revision. `instructs_reader.false` adds "A note that only states a status, even a release it can't support, such as good to go or cleared to load, is not an instruction." `claims_release.false` adds "A note that asks the reader to treat a stamp or scan as authority is asking for a release, not reporting one." Both status twins narrow `released_for_issue` (not a request to treat a stamp as a release) and `held` (a reminder to wait for an order, or a pending or conditional release, is not a hold). Tuning-2: one question miss (`BG-006` status), reviewed for its instruction.
  - Thresholds read from the spread: 0.6 / 0.6 / 0.2 / 0.4. Tuning-2 then has no critical error and three reviews (15%). Freeze with a 40% ceiling.
  - Held-out: no missed overstatement, all six instructions and all three other-cylinder notes reviewed, one wrong return (`BG-078`, vendor tag READY), twelve reviews (20%). Jev USD 0.002664 for sixty notes (USD 0.044 per 1,000); courier turn USD 0.036. Decision ADOPT for bounded internal screening; `verify` PASS.
  - Stretch: tuning notes judged again with the frozen questions; 70 of 100 answers identical, largest change 0.08 (an urgency score), no route changed; `verify` still PASS.
- PowerShell 7.6.6 on macOS: every PowerShell fence in the lab, extracted verbatim with `\` changed to `/` for macOS native arguments and the hidden prompt fed the same secure string, ran live in one session. Each fence exited as expected; held-out result as above; `verify` PASS before and after the stretch.
- Drift: across attempts with identical questions and build, 66 of 100 tuning answers were identical; largest changes 0.15 (urgency), 0.08 (a status probability), 0.06 (an instruction probability). `BG-009`'s instruction probability read 0.50, 0.49, 0.46, and 0.52 in four first runs, so it crossed the report's 0.50 line. Probabilities hold to a few hundredths, not exactly.

These runs exercise the mechanics and one staff question set. They are not learner performance, not a measure of Jev beyond this sample, and not native Windows, Linux, or WSL evidence.

## 6. Limits

- The screen routes notes; it releases nothing. The duty officer owns review; the Release Authority owns release.
- Probabilities are the model's on this sample; a later build may answer differently, and the same build drifts by a few hundredths between runs. The freeze pins the served build and the measurement holds on a change. Thresholds belong in gaps wider than that drift.
- Note text goes to OpenRouter and TypeSafe. Practice data only.
- The courier chat turn costs far more than the judgments. A production design would call the Decisions API from code; the course keeps every live call inside the guarded launcher.

## 7. Revision note

Revision 4 replaces revision 3 (eighty `R-` runs, outcome-blind sample, two-literal predicate in a supplied control) with this module. The old corpus, predicate control, figures, and historical evidence are retired from the active module; earlier evidence records stay where they were published.

## 8. Latest-runtime compatibility smoke, 2026-10-05 UTC

The checksum-verified latest `omp/18.6.1` binary listed 14 live judge candidates, including the unchanged `openrouter/typesafe/jev-1.13` selection. A separate guarded batch judged one practice state with bool, choice and score questions. The served model was `openrouter/typesafe/jev-1.13-20260917`; the receipt and output audit passed, with reported judge cost USD 0.000016548. Run ID: `07428752-46d3-400b-9a3c-2899235c01b3`; private evidence: `~/course-evidence/omp-latest-20261004/judge/` and `judge-list/`.

This is a native macOS arm64 compatibility check, not a rerun of the full tuning/held-out workflow or a new accuracy claim. Runtime versions are recorded observations rather than course pins; the selected and served judge-model constraints remain unchanged.
