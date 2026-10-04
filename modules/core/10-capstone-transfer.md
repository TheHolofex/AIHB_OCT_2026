# Module 10 — Stand up a local uncensored AI and hand it off

**Serves oracle:** S04, S09, S10, S14, S20, S21, S22, S23  
**Primary objective:** PO-10 — Stand up a local uncensored AI and hand it off
**Prerequisites:** Earlier source verification, bounded controls, and recovery skills; a preflighted environment; this module's supplied task; and a Hugging Face account that has accepted the pinned model's conditions  
**Consumes:** VERIFY:PREFLIGHT; VERIFY:CASE; VERIFY:TRANSFER_TASK  
**Produces:** LOCAL_MODEL_SERVICE; PO10_RESULT  
**Rough time:** about 3 hours  
**Performance stage:** Transferred  
**Work surface:** A real local-model service on the learner's own laptop  
**Practical work:** Stand up the pinned uncensored model under OMP orchestration, prove one live interaction, stop and restore the service, and package the kit so it carries everything except the weights and passes its check from a fresh copy without the author's chat history.  
**Performance evidence:** Verified weights identity, loopback-only service proof, live-interaction transcript, stop/restore receipts, byte-identical restore comparison, frozen bundle record, digest-checked copy, received-package check, and close-out naming unresolved limits.  
**Failure / HOLD:** Hold the affected work for gated access not accepted, wrong-size or wrong-hash weights, insufficient hardware, a bind beyond loopback, public exposure, or a forced pass; record the missing prerequisite or escalation owner.  
**Scope boundary:** The kit proves a bounded local service and a cold handoff, not production serving, safety-stack completeness, or model quality.  
**Handoff:** Give the next owner purpose, bounds, the pinned identity, run/check/stop/restore actions, residual risks, and the trigger for the next bounded use.  
**Case family:** [CASE_FAMILY.md](../../CASE_FAMILY.md). This module runs real software under its own bounded-use rule instead of a fictional logistics movement; its independence rule is unchanged. This module's gate does not consume another module's product.  

## Why

Saved artifacts are the claim. A local uncensored model is finished when it runs on the learner's own machine under a verified identity, survives a stop and restore without conversational memory, and its package carries everything except the weights, with a fresh copy that passes its check without the author's chat history.

## Enabling objectives

1. Stand up only the components the task earns, and preserve the boundary under one adverse change.
2. Make the kit usable in a fresh session without relying on the author's chat history.
3. Record the received-package structure check result and any unresolved limits.

## Check the work

A clean session receives only the transfer kit, the pinned identity, ordinary operating access, and the supplied task. In a new terminal inside the received folder, run `scripts/check_package.py shared/PACKAGE.md` and record `PASS: package structure checked`. The structure check reads the package's named fields and confirms every named file is inside the received folder; it does not run the package's commands. PO10_RESULT records the verified identity, live interaction, stop/restore receipts, byte-identical restore comparison, frozen bundle, digest-checked copy, received-package check, and unresolved limits.

## Supplied-case domain (adapter)

The pinned model is `orcarouter/OrcaSAQ-2-Cyber-27B-Uncensored-GGUF`: a single 15.7 GB weight file, Apache-2.0, abliterated (uncensored) base, access-gated on Hugging Face. llama.cpp serves it loopback-only; OMP drives it through a generated provider overlay; the adapter scripts verify the pinned identity, wire the overlay, probe reachability, and prove the stopped state. A bind beyond loopback and an unserved capability claim are the core adverse cases. The transfer bundle carries everything except the weights; the next owner downloads under their own account against the pinned identity.
