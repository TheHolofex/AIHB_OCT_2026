# Cold Foundry facilitator runbook

## Session result

The learner stands up the pinned uncensored model on their laptop under OMP orchestration, proves a live loopback-only interaction, stops and restores it, and freezes and copies a kit that passes its structure check from a new terminal without the author's chat history. All work is individual within the Thursday session. The package carries everything except the weights; the structure check does not run its commands or prove that another person can operate it. Learner retains ownership (recorded at close-out).

## Staff release validation

Validate the supplied runtime and pinned identity on supported hardware before delivery. These are staff maintenance checks, not learner pre-work or evidence that a learner completed the module:

1. `hf auth login`, accept the pinned repository's conditions on its page.
2. Download the 15.7 GB weight file and record the real SHA-256 into `shared/case/model-card.json` (replace `PENDING_REAL_HASH`); the adapter refuses to verify until the real digest is recorded.
3. Run the full bring-up once: verify, wire, launch loopback-only with context 32768, probe, one OMP interaction, stop, restore.
4. Record the observed memory use, startup time, and response time on the supported room hardware at the pinned context size. RAM capacity alone does not establish interactive performance or prove that the session allocation is sufficient.

An unvalidated runtime or model identity holds the live lane. Never fabricate a digest, accept a wrong-size file, or bind beyond loopback to save time. Learners establish their own account access, download, and live evidence during the session.

## Thursday delivery route

Total facilitated allocation: 3 hours. The blocks are planning allocations, not measured learner times.

| Block | Allocation | Facilitator action |
|---|---|---|
| Boundary discussion | 20 min | Service rules, uncensored behaviour, the community note as data |
| Account and download | 25 min | Device login, accepted conditions, resumable download |
| Verify and wire | 15 min | Pinned identity check, loopback overlay |
| Bring-up and probe | 25 min | OMP-drafted launch line, learner approval, probe to green |
| Live interaction and observation | 30 min | One live exchange, blunt-answer observation, named boundary |
| Stop and restore | 25 min | Stopped-state proof, control disable/restore, byte comparison |
| Package freeze and fresh-terminal check | 25 min | Freeze the declared ten-file bundle, make a digest-checked copy into `F`, then from a new terminal inside `F` run `scripts/check_package.py shared/PACKAGE.md` and record `PASS: package structure checked` or the observed HOLD |
| Close | 15 min | Learner shuts down the service and records verified identity, live interaction, stop receipt, restore comparison, fresh-terminal structure check, what ran, and unresolved limits in `E/close-out.md` |

## Close-out observations

The learner records the checks they actually ran and their limits. The fresh-terminal structure check confirms named fields and files within `F`; it neither executes package commands nor proves anyone else can operate the kit.

## HOLD conditions

Hold the affected work and name the reason when: the repository conditions are not accepted; the downloaded file's size or digest differs; disk space runs out during download; the server binds any address other than `127.0.0.1`; the endpoint becomes reachable from another machine; a helper pass is forced by editing `model-card.json` or any fixture; the fresh-terminal structure check fails; or access, download, or hardware prevents required steps. Preserve every artifact of a held attempt. Access/hardware/time misses close as honest HOLD in-session; no outside-session continuation or recipient work.
