# Module 10 — Stand up a local uncensored AI and hand it off

**Serves oracle:** S04, S09, S10, S14, S20, S21, S22, S23  
**Primary objective:** PO-10 — Stand up a local uncensored AI and hand it off  
**Prerequisites:** Earlier source verification, bounded controls, and recovery skills; a preflighted environment; this module's supplied task; and a Hugging Face account that has accepted the pinned model's conditions  
**Consumes:** VERIFY:PREFLIGHT; VERIFY:CASE; VERIFY:TRANSFER_TASK  
**Produces:** LOCAL_MODEL_SERVICE; PO10_RESULT  
**Rough time:** about 3 hours  
**Performance stage:** Transferred  
**Work surface:** A real local-model service on the learner's own laptop  
**Practical work:** Stand up the pinned uncensored model under OMP orchestration, prove one live interaction, stop and restore the service, and transfer the complete kit to another person.  
**Performance evidence:** Verified weights identity, loopback-only service proof, live-interaction transcript, stop/restore receipts, recipient observations and questions.  
**Failure / HOLD:** Hold the affected work for gated access not accepted, wrong-size or wrong-hash weights, insufficient hardware, a bind beyond loopback, public exposure, a forced pass, or an unavailable recipient; record the missing prerequisite or escalation owner, and record the person-to-person attempt as unobserved when no recipient is available.  
**Scope boundary:** The kit proves a bounded local service and a cold handoff, not production serving, safety-stack completeness, or model quality.  
**Handoff:** Give the next owner purpose, bounds, the pinned identity, run/check/stop/restore actions, residual risks, and the trigger for the next bounded use.  
**Case family:** [CASE_FAMILY.md](../../CASE_FAMILY.md). This module runs real software under its own bounded-use rule instead of a fictional logistics movement; its independence rule is unchanged. This module's gate does not consume another module's product.  

## Why

Saved artifacts are the claim. A local uncensored model is finished when it runs on the learner's own machine under a verified identity, survives a stop and restore without conversational memory, and carries enough evidence for someone else to bring it up cold — on their own machine, under their own account.

## Enabling objectives

1. Stand up only the components the task earns, and preserve the boundary under one adverse change.
2. Make the kit usable in a fresh session and by another person without relying on the author's chat history.
3. Use recipient observations to resolve gaps in operating, stopping, restoring, and handing off the kit.

## Check the work

A clean session receives only the transfer kit, the pinned identity, ordinary operating access, and the supplied task. Inspect its bring-up, stop, and restore behavior. Separately, give another person the same kit and task. Preserve what they do, the questions they ask, and any help supplied. PO10_RESULT records those observations and unresolved limits so the kit can be improved. A technical replay and a person-to-person attempt remain separate evidence; neither is a learner score.

## Supplied-case domain (adapter)

The pinned model is `orcarouter/OrcaSAQ-2-Cyber-27B-Uncensored-GGUF`: a single 15.7 GB weight file, Apache-2.0, abliterated (uncensored) base, access-gated on Hugging Face. llama.cpp serves it loopback-only; OMP drives it through a generated provider overlay; the adapter scripts verify the pinned identity, wire the overlay, probe reachability, and prove the stopped state. A bind beyond loopback and an unserved capability claim are the core adverse cases. The transfer bundle carries everything except the weights; the recipient downloads under their own account against the pinned identity.
