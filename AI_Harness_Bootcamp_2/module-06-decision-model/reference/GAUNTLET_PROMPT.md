# Gauntlet prompt — Module 6 Blue Gauge

Review the Module 6 learner pages (README.md and shared/MODULE_06_LAB.md) against this path: ordinary Oh My Pi, the TypeSafe skill from the quick start, and code that calls `jev-1.13` through OpenRouter with `OPENROUTER_API_KEY`. Jev is not the chat model. There is no TypeSafe key and no Oh My Pi judge-role overlay.

Review criteria:

- Start is `omp` in the module folder. No `TYPESAFE_API_KEY`. No `--config` judge file. No Python launcher.
- The skill install prompt is the quick-start paste, plus the OpenRouter `jev-1.13` constraint.
- Four sections, in TypeSafe order: fan-out, confidence routing, composite scoring, intent routing.
- Each section teaches the pattern, shows its diagram, and asks the agent to write the OpenRouter call.
- Questions and thresholds stay in one place. Code owns the route, gate, weights, and handler.
- No route, score, or handler result is cargo clearance, flight acceptance, or dispatch.
- The handoff is labeled "review packet — not a manifest or movement order".
- The key is not printed or saved in a file.
