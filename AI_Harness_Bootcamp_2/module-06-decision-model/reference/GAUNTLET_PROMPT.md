# Gauntlet prompt — Module 6 Blue Gauge

Review the Module 6 learner pages, case, controls, scripts, launcher judge profile, and guard against `reference/REFERENCE.md`.

Review criteria: decision-model selection and pinning (no alias, no router, no chat model as judge); question design for the model's documented weak spots (literal reading, numbers and dates in code, minimal state, adversarial text, option order); code and model split; thresholds set from tuning answers by error cost with a review band; freeze before the held-out run; one held-out measurement with build identity and cost; joined verification of launcher receipts; independence; HOLD behavior; parsimony and voice.

Required adversarial cases: the alias or the router written into `JUDGE.yml`; a question set that passes shape checks but asks two things at once; a twin status question in the same option order; the scan record placed in the model's state; thresholds tuned on held-out notes; questions edited after the tuning run a freeze names; a held-out run started before the freeze; a judgment answered by another build; an edited saved judgment or measurement; an eval cell other than the frozen one; a note's embedded instruction obeyed or never reviewed; staff tokens, other modules' cases, or the worked question set in learner files.
