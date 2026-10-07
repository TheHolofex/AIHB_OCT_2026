# Facilitator runbook — Module 6 Blue Gauge

The learner starts the native OMP TUI from the module directory, uses the supplied `blue_gauge` tool to inspect controls and sources, configures pattern settings through plain prompts, prepares one frozen plan per exercise, runs serial then fan-out on the twenty practice messages, replays the same answers for three confidence gates, scores and reweights all eighty messages by replay, classifies sixteen requests through Jev, runs the three routed handlers (record lookup, deterministic record comparison, human officer queue), and requests a final review packet. All execution, routing, and evidence handling is supplied. The learner owns inspected configuration changes and the explanation of observed effects.

**What the harness changes:** The `blue_gauge.py start` command prepares the isolated work area, records absolute shared-helper paths, opens the real interactive OMP TUI with only `blue_gauge` and `eval` active, and supplies the extension that renders native panels. Inside the session the Python adapter owns source checks, the router, arithmetic, handler dispatch, and immutable revisions. Native `judgeBatch` is called only through the supplied runner for prepare-issued cells; the cell is exactly `run({judgeBatch,plan})`. Replays and shows make zero Jev or handler calls. The guard admits one exact eval cell per plan, once. The Python `control` and `verify` adapters rejoin native usage, guard decisions, raw results, and disk effects. One paid operation is allowed at a time. Each operation is bounded by 240 s; outstanding handles are cancelled on deadline or interrupt; partial results are preserved and the operation is held.

## Before class

1. Confirm the verified latest stable OMP release is installed and record its actual `omp --version` output.
2. Start the supplied launcher with a course OpenRouter key and confirm its preflight offers `openrouter/typesafe/jev-1.13`. If it is not offered, the live work holds; do not substitute another judge or the `~typesafe/jev-latest` alias.
3. Keep reference materials to yourself. They are for diagnosing a stuck learner, not for distribution.
4. Verify that the classroom runtime supports the extension registration and tool-result rendering used by the supplied controls.

## Route

| Clock (approx.) | Work | Observable |
|---|---|---|
| 0:00–0:10 | Start or resume; inspect mission, controls, and one source record | Native TUI open; work/evidence paths printed; `inspect` on mission and BG-C104 succeeds |
| 0:10–0:45 | Exercise 1: serial arm then fan-out arm on the same 20 practice messages | Two runs, six-question request visible, ignored answers marked, run IDs saved |
| 0:45–1:25 | Exercise 2: gate replays at 0.4/0.6/0.8 then freeze and one unseen run of 60 | Zero additional Jev on replays; one frozen unseen plan; PASS or HOLD recorded |
| 1:25–2:00 | Exercise 3: obtain missing dimensions for all 80 messages, compare two weight sets, learner third set | Live Jev calls recorded once; weight replays make zero additional Jev calls; contributions explain actual rank movement or non-movement |
| 2:00–2:40 | Exercise 4: Jev classification on 16 requests; routed handlers (lookup, deterministic comparison, officer queue); stricter-gate preview | Actual lookup, deterministic comparison and human queue where gates and saved choices allow; preview labeled no-execution |
| 2:40–3:00 | 5. Inspect and hand off | Four-row comparison with real run IDs and concrete examples; review packet not manifest |

Clock marks count from the start of the block, exclude breaks, and are planning guides only. On Wednesday the block's break falls after Exercise 2, roughly an hour and a quarter in. The day's clock is in `COURSE_MAP.md`.

## Coaching boundary

You may point to a file, a rule in the desk rules, or a control setting the learner can inspect. You may help read a native panel or the difference returned by configure. Do not author a prompt that bypasses the prepare/guard boundary, read held-out labels before the frozen unseen measurement completes, or edit saved answers, revisions, or evidence. Record any assistance as an observation, not a learner score or qualification decision.

## `HOLD` conditions

- The pinned judge is not offered, the key lacks credit, or the OMP installation/version report is unusable: hold the live work.
- A prepare step is refused because the revision does not match the active configuration, or because a prior paid operation is still open: hold that lane; a new prepare is allowed only after the prior operation completes or is held.
- The learner alters the issued eval cell or attempts a second invocation of the same plan: the guard blocks; preserve the partial evidence.
- A replay is claimed to have made new Jev or handler calls: the evidence is inconsistent; use `verify` to surface the mismatch.
- The unseen measurement is started before the freeze, or unseen labels are inspected before the frozen measurement completes: hold the attempt.
- The final review packet claims cargo clearance, flight acceptance, or dispatch, or mislabels a replay as executed work: the handoff is returned for correction.
- A critical miss, changed source or build, incomplete result, or review share above the chosen ceiling on the unseen run yields `HOLD`. That is a result, not a failed exercise.
- A selected handler marked `executed=false` did not produce a verified result. Inspect its saved error and handler file; do not substitute a chat summary. Compare the record-comparison score with `max_comparison_complexity` (maximum 1) and its confidence with the separate 0.5 gate.
- Lookup and comparison are pure code. Human-review items are queue entries, not assistant completions or approvals. A missing handler result holds the corresponding execution claim.

A precisely recorded failure or `HOLD` is the feedback the exercise needs. Do not erase or retune on unseen data to force a different decision.

## Staff boundary checks

With explicit paid authorization, exercise the actual native four-pattern paths, then quit and resume by exact attempt and session IDs. Hash previous receipts before and after resume/replay. For a negative guard check, request one disallowed eval that attempts to write the copied scan source. Observe the actual pre-execution denial and unchanged source bytes; a chat refusal alone does not prove enforcement. Do not prepare a paid plan or retry the denied cell.
