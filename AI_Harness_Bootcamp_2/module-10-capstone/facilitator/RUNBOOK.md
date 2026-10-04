# Cold Foundry facilitator runbook

## Session result

The learner stands up the pinned uncensored model on their laptop under OMP orchestration, proves a live loopback-only interaction, stops and restores it, and freezes and copies a kit that passes its structure check from a new terminal without the author's chat history. The package carries everything except the weights; the structure check does not run its commands or prove that another person can operate it.

## Before class

Complete the live lane once on the facilitator machine before Thursday:

1. `hf auth login`, accept the pinned repository's conditions on its page.
2. Download the 15.7 GB weight file and record the real SHA-256 into `shared/case/model-card.json` (replace `PENDING_REAL_HASH`); the adapter refuses to verify until the real digest is recorded.
3. Run the full bring-up once: verify, wire, launch loopback-only with context 32768, probe, one OMP interaction, stop, restore.
4. Record hardware reality on the room machines: a laptop with 24 GB RAM or more runs the model at interactive speed; 16–24 GB runs slowly; a machine that cannot hold the file cannot run the module and must observe the probe loop instead.

Hold the session if any of these has not been done on the machine being used. Never fabricate a digest, never accept a wrong-size file, and never bind beyond loopback to save time.

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
| Package freeze and received-copy check | 25 min | Freeze the declared ten-file bundle, make a digest-checked copy into `F`, then from a new terminal inside `F` run `scripts/check_package.py shared/PACKAGE.md` and record `PASS: package structure checked` or the observed HOLD |
| Close | 15 min | Learner records verified identity, live interaction, stop receipt, restore comparison, received-package check, what ran, and unresolved limits in `E/close-out.md` |

## Close-out observations

The learner records the checks they actually ran and their limits. The received-package structure check confirms named fields and files within `F`; it neither executes package commands nor proves anyone else can operate the kit.

## HOLD conditions

Hold the affected work and name the reason when: the repository conditions are not accepted; the downloaded file's size or digest differs; disk space runs out during download; the server binds any address other than `127.0.0.1`; the endpoint becomes reachable from another machine; a helper pass is forced by editing `model-card.json` or any fixture; or the received-package structure check fails. Preserve every artifact of a held attempt.
