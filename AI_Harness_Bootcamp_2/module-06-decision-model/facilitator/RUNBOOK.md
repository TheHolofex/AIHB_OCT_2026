# Facilitator runbook — Module 6 Blue Gauge

The learner selects and pins a decision model for OMP's judge role through OpenRouter, repairs a starter question set, runs twenty tuning notes, records the first misses, revises the wording, sets four thresholds from the tuning answers, freezes them with a review ceiling, judges sixty held-out notes once, and hands off the measured screen.

**What the harness changes:** The supplied launcher sets the judge role, lets the course chat model make exactly one eval call with a launcher-written cell, and checks every saved answer, the build that answered, the cost, and the work folder. `blue_gauge.py` supplies the code checks, the router, the threshold spread, the freeze, the held-out measurement, and the joined verifier. The learner writes the selection record, the questions, the thresholds, the first-miss notes, and the handoff.

## Before class

1. Confirm the verified latest stable OMP release is installed, record its actual `omp --version` output, and confirm each learner's OpenRouter key has credit.
2. Run `run_omp.py --list-judges --evidence <new folder>` with a course key and confirm `openrouter/typesafe/jev-1.13` is offered. If it isn't, the live work holds for everyone; do not substitute another judge or the `~typesafe/jev-latest` alias.
3. Keep `reference/WORKED_QUESTIONS.json` to yourself. It is a working question set for diagnosing a stuck learner, not something to hand out.

## Route

| Clock (approx.) | Work | Observable |
|---|---|---|
| 0:00–0:20 | Prepare, enter the key, split the desk decision | Work folder; the three-way split in the learner's own words |
| 0:20–0:40 | List judges, write the selection record, write `JUDGE.yml` | `judge-candidates`; `SELECTION.md`; two-line `JUDGE.yml` |
| 0:40–1:15 | Repair the question set | `check-questions` PASS |
| 1:15–1:25 | First tuning run | `tuning-1` PASS with the served build |
| 1:25–1:45 | Read the report and write first-miss notes | `first-misses.md` naming every missed note |
| 1:45–2:10 | Revise and run `tuning-2` | Fewer question misses |
| 2:10–2:30 | Spread, thresholds, offline reports | No critical error on the tuning notes; review share recorded |
| 2:30–2:45 | Freeze, held-out run, measure | `freeze.json`; `held-out-measure.json` with a decision |
| 2:45–3:00 | Handoff and verify | `verify` PASS or named HOLDs |

Clock marks count from the start of the block, exclude breaks, and are planning guides only. On Wednesday the block's break falls after the first-miss notes and before the revision, roughly an hour and three quarters in. The day's clock is in `COURSE_MAP.md` and on the public homepage.

## Coaching boundary

You may point to a file, a rule in the lab's table, or a supplied command. You may help read the report or the spread. You may not write a question, choose a threshold, choose the review ceiling, or open the held-out labels for a learner before the freeze. If you cross that line, mark the work as guided practice.

## `HOLD` conditions

- The pinned judge isn't offered, the key lacks credit, or the OMP installation/version report is unusable: hold the live work; keep any candidate list already saved.
- `JUDGE.yml` names the alias, the router, or a chat model: the launcher holds before any call.
- A judgment is missing, malformed, or from another build: the run holds; keep the folder and rerun under a new name.
- The questions changed after the tuning run a freeze names, or the held-out run started before the freeze: no measurement.
- The held-out measurement shows a missed overstatement, an unreviewed instruction, an unreviewed note about another cylinder, a changed build, or a review share above the frozen ceiling: the decision is `HOLD`. That is a result, not a failed exercise.
