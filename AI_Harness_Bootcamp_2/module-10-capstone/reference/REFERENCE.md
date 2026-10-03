# Cold Foundry staff reference

Scope: design rationale for Module 10, the local uncensored AI capstone. Frozen as staff material; learners see the lab, the service rules, and the package, never this file.

## 1. The need

The course's final capability is transfer: work another person can operate cold. Earlier modules exercised transfer on bounded paperwork and on API-mediated tasks. Module 10 completes the arc on real software: an uncensored 27B model, downloaded to and served from the learner's own laptop, orchestrated through OMP, then handed to a colleague who repeats bring-up, proof, stop, and restore alone.

Three design decisions shape the module:

1. **A real model, not a fixture.** The pinned weights are a real Apache-2.0 release with a real identity. Size and digest checks are the learner's first verification behavior, exactly as in professional deployments.
2. **OMP as orchestrator, scripts as verifier.** OMP drafts the launch line and drives bring-up steps under learner approval — the same delegation pattern the course has taught since Module 00. The adapter scripts, not the model and not OMP, decide pass or hold: every claim in the package is checked against bytes and reachability.
3. **The uncensored model as the safety lesson.** The refusal direction is removed by the publisher. The module teaches that guardrails belong to the deployer: loopback bind only, weights that never leave the machine, prompts recorded by the harness, and a named personal boundary on the model's output.

## 2. Case

Pinned identity: `orcarouter/OrcaSAQ-2-Cyber-27B-Uncensored-GGUF`, a single 15.7 GB weight file `OrcaSAQ-2-27B-Uncensored.gguf` (15,676,553,472 bytes), repository pin `a0ebe1b5ad5c009cd382908585c04b7e9e0cf0c0`, blob `3312a8363a04f039c1825d8efe8c4c0314708a3c`, license Apache-2.0, base `orcarouter/Qwen3.8-27B-Uncensored`, gated `auto` on Hugging Face — login plus accepted conditions required before any download.

The stack: llama.cpp serves the weights loopback-only; OMP drives them through a generated provider overlay pointed at the loopback endpoint; the adapter verifies the pinned identity, generates the overlay, probes reachability, and proves the stopped state. The transfer package carries everything except the weights — the recipient downloads under their own account against the pinned identity.

The adverse cases are built in, not simulated: a hostile community note that argues for a `0.0.0.0` bind and a skipped digest check; the control file that must disable every command when turned off; the stop receipt that must name the port; and the deterministic re-wire whose bytes must compare equal after restore.

## 3. Transfer practice

What transfers: a bounded, verifiable bring-up procedure with an identity check, a live-interaction proof, a stopped-state proof, a restore comparison, and a package another person can run from a fresh directory on their own machine. This is the professional shape of a local-AI deployment handover.

What does not transfer, and the module says so: no claim of production fitness (no serving beyond loopback, no concurrency, no safety stack); no model-quality claim (the quantization is not lossless; the publisher reports 94.4% top-1 agreement with the base); no claim that the model guards itself (it does not refuse, warn, or judge). The uncensored behaviour is the reason the boundary is the operator's, and the module teaches it by observation, not assertion.

The honest floor: a machine that cannot hold the weights cannot complete the live lane; that machine records the probe-loop observation and the module marks the live lane unobserved.
