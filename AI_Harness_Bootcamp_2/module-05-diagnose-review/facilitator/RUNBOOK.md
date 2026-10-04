# Module 5 facilitator runbook

## Session result

The learner prepares W with prepare_work, verifies restore from the hashed baseline, has a public fault placed, localizes with the probe, makes one authorized replace, and proves recovery with three distinct runs.

Desk knowledge outside the packet is not tested. If learners need facts that are not in the packet, the case is defective.

## What the harness changes

The harness forces explicit ledger input to the renderer, a digest-checked baseline restore before any edit, public fault placement on the work copy, and a read-only probe that uses the renderer's classify on current rows only. Source omissions correctly prevent render; the probe diagnoses them from the ledger. Three recovery proofs are distinct: required-field probe, complete render, and fresh-folder process from unrelated cwd. The 80-row pile with near misses, supersession, hostile notes, future records, and condition collisions is processed end to end.

## Before class

1. Run the prepare_work for 04 into a throwaway and confirm the next render command succeeds with both fields.
2. Confirm python scripts/restore.py <workdir> against a throwaway copy prints RESTORE OK.
3. Confirm the public place_practice_fault.py and probe_fields.py run from source paths.

## Route

| Roughly | Facilitator action | Learner result |
|---|---|---|
| 0:00–0:20 | Introduce restore-first and the ledger | Learner prepares W and sees both fields |
| 0:20–0:40 | Learner runs the clean renderer and restore | RESTORE OK |
| 0:40–0:45 | Place the prepared work copy using public place script | Work copy drops one field |
| 0:45–1:20 | Learner seals the first miss with probe | Sealed record before replace |
| 1:20–1:50 | Learner runs one restore replace | Single RESTORE OK |
| 1:50–2:30 | Learner reruns three ways (incl. fresh-process) | Both fields present in each |
| 2:30–3:00 | Collect the handoff | Reconstruction without coaching, or HOLD |

Clock marks count from the start of the block, exclude breaks, and are approximate planning guides: follow the learners' progress, not the clock. On Wednesday the block's break falls after the learner seals the first miss and before the authorized replace, roughly 80 minutes in. The day's clock is in `COURSE_MAP.md` and on the public homepage.

## Coaching boundary

You may:

- define a term already stated in the packet;
- point to the current step or file;
- help open a file or run a supplied command;
- place the prepared work copy after restore is proved.

You may not supply:

- the name of the missing field;
- the reason it dropped;
- a hand-edited review.md; or
- the replace command wording.

If you cross that line, mark the work as guided practice.

## HOLD conditions

Use HOLD when restore fails, the first miss is not sealed, more than one change is made, a decisive field is inaccessible, or the learner attempts consequential use.

A well-documented HOLD can complete practice. It does not satisfy the module requirements.

## Collect

- clean render;
- restore output;
- sealed first miss + probe output;
- replace record;
- three reruns;
- handoff; and
- result or reason for HOLD.

Do not collect credentials, private local files, outside operational details, or model chat history unrelated to the case.
