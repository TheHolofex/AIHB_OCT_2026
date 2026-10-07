# Facilitator runbook — Module 6 Blue Gauge

The learner opens ordinary Oh My Pi in the module directory, with the chat model `openrouter/anthropic/claude-sonnet-4.6` and the session judge role `openrouter/typesafe/jev-1.13`. They paste the TypeSafe skill install prompt from the lab, then build the four patterns in that session. They do not start `scripts/blue_gauge.py` and they do not need a separate TypeSafe key.

## Before class

1. Confirm Oh My Pi starts and `omp --version` prints `omp/<semver>`.
2. Confirm `omp models --kind judge` offers `openrouter/typesafe/jev-1.13` through the course OpenRouter key. If it is not offered, hold the live work. Do not substitute another judge or `~typesafe/jev-latest`.
3. Keep reference materials to yourself.

## Route

| Clock (approx.) | Work | Observable |
|---|---|---|
| 0:00–0:20 | Start Oh My Pi and install the TypeSafe skill | Session open; judge is `openrouter/typesafe/jev-1.13`; skill loaded |
| 0:20–1:00 | Section 1, speculative fan-out | One multi-question Jev call per message; ignored answers marked |
| 1:00–1:30 | Section 2, confidence-gated routing | Two gates on saved answers; no new Jev call for the comparison |
| 1:30–2:10 | Section 3, composite scoring | New order from saved scores; no new Jev call |
| 2:10–2:40 | Section 4, intent routing | Lookup, comparison, and human path are distinct; approvals come to the learner |
| 2:40–3:00 | Hand off | Four rows, real IDs, review packet not a manifest |

Clock marks are planning guides. The day's clock is in `COURSE_MAP.md`.

## Coaching boundary

You may point to a desk rule, a source file, or the skill install prompt. Do not write the questions for them, start the Python launcher, or create a TypeSafe key. Record assistance as an observation, not a learner score.

## Hold

- Jev 1.13 is not offered, the key lacks credit, or Oh My Pi will not start: hold the live work.
- The agent asks for `TYPESAFE_API_KEY`, uses `jev-latest`, or starts `scripts/blue_gauge.py`: stop that path and return to the lab prompt.
- A route, score, or handler result is treated as cargo clearance, flight acceptance, or dispatch: return the handoff for correction.
