# Facilitator runbook — Module 6 Blue Gauge

The learner opens ordinary Oh My Pi in the module directory. Oh My Pi remains the chat agent. They export `TYPESAFE_API_KEY` for that terminal, paste the TypeSafe skill install prompt, and have the agent write code that calls the TypeSafe API. They do not set an Oh My Pi judge role and they do not start `scripts/blue_gauge.py`.

## Before class

1. Confirm Oh My Pi starts and `omp --version` prints `omp/<semver>`.
2. Confirm each learner can create a TypeSafe key at the dashboard. If the key is missing, hold the live Jev calls. Do not substitute the OpenRouter judge role.
3. Keep reference materials to yourself.

## Route

| Clock (approx.) | Work | Observable |
|---|---|---|
| 0:00–0:20 | Start Oh My Pi and install the TypeSafe skill | Session open; skill loaded; key not printed |
| 0:20–1:00 | Section 1, speculative fan-out | One multi-question API call per message; ignored answers marked |
| 1:00–1:30 | Section 2, confidence-gated routing | Two gates on saved answers; no new API call for the comparison |
| 1:30–2:10 | Section 3, composite scoring | New order from saved scores; no new API call |
| 2:10–2:40 | Section 4, intent routing | Lookup, comparison, and human path are distinct; approvals come to the learner |
| 2:40–3:00 | Hand off | Four rows, real IDs, review packet not a manifest |

Clock marks are planning guides. The day's clock is in `COURSE_MAP.md`.

## Coaching boundary

You may point to a desk rule, a source file, or the skill install prompt. Do not write the questions for them, set the Oh My Pi judge role, or start the Python launcher. Record assistance as an observation, not a learner score.

## Hold

- The TypeSafe key is missing or rejected: hold the live Jev calls.
- The agent makes Jev the chat model, prints the key, or writes the key into a file: stop that path and return to the lab.
- A route, score, or handler result is treated as cargo clearance, flight acceptance, or dispatch: return the handoff for correction.
