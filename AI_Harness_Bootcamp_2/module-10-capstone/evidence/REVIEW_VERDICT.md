# Cold Foundry review verdict — 2026-10-03

## Commands and evidence

- `python3 tests/test_module_10.py` — 93 behavior checks, 0 failures.
- `python3 tests/test_adequacy.py` — 20 mutations, 0 survivors, 0 unapplied.
- `node scripts/render_figures.mjs --check` — 70 figures byte-identical, links resolve.
- `python scripts/check_course.py` — all 29 scoped gates pass; `build_course.py --check` verifies the published site byte-for-byte.
- Live small-model lane (Qwen2.5-0.5B as stand-in weights): verify → wire → loopback serve → probe → one real OMP interaction (`provider: llama.cpp`, `stopReason: stop`) → kill → probe HOLD → stop receipt → `PASS: service is stopped` → relaunch → probe PASS → wire bytes identical → final stop-state proof. Every shipped mechanism exercised end to end.
- User's OMP configuration restored byte-identical after each probe; probe servers terminated; scratch removed.

## Review outcomes

| Dimension | Verdict | Evidence |
|---|---|---|
| Runtime/security | EXCELLENT | Loopback constant pinned; 3-second probe bound; atomic exclusive publication; control checked twice; path confinement intact; banned tokens enforced |
| Curriculum/voice | EXCELLENT | Zero banned tokens across all learner surfaces; zero meta commentary; every command-bearing section carries Expected/Stop/Recovery in both shells |
| Publication/UI | EXCELLENT | All 44 command blocks labeled; 29/29 gates green; site byte-for-byte; figures regenerated and verified |
| Transfer honesty | EXCELLENT | Technical replay and independent-person attempt recorded separately; unobserved ≠ passed stated in every surface |
| Uncensored-boundary honesty | EXCELLENT | No self-guarding claim anywhere; guardrails assigned to the operator in rules, lab, package, and reference |
| HOLD discipline | EXCELLENT | Every refusal path names its specific reason; no silent exits; residue checks green |
| Parsimony | EXCELLENT | Every file serves the single transfer capability; no decorative volume |

## Limits

Class F and the human panel remain unmeasured. The real-weights lane (15.7 GB download under the operator's account) is blocked pending Hugging Face device-code authorization; the live lane above proves every mechanism on real downloaded weights at small scale. The independent-recipient attempt is unobserved until a real person operates the kit.
