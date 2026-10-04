# Module 8 · Evaluate a change with variation controls

Decide whether a proposed change produces desk briefs that meet every required condition. Freeze the cases, configurations, and rejection rule before you open any results. Compare each candidate with its baseline on the same 40 cases, keep every failure, and check that you can restore the original controls.

The Slope Brief case covers heater-fuel cans moving from Ridge Depot to Clinic T-8 on vehicle SB-4. The core comparison uses practice briefs written in advance, so it can't show that a live model improved. The optional live comparison repeats attempts to tell an instruction's effect apart from the ordinary differences between runs.

Plan for a little over two hours on Thursday. That's a rough estimate, not a measured time.

## Start here
1. [Evaluate the paired cases](shared/MODULE_08_LAB.md) with a decision rule you save before you see any results.

## The hard gates
A **hard gate** is a required condition that no better result elsewhere can make up for. A single violation rejects a candidate, even if its average looks better.

- The brief must follow the required three-row form; a malformed brief fails the format gate.
- Payload mass must be the exact number that appears in the authoritative `#payload` record, and the Source cell must name that record. A **locator**, such as `#payload`, identifies the exact source record that supports a value.
- Gate times must name both the UTC value and the MDT value exactly as they appear in the authoritative `#gate` record, and the Source cells must name that locator.

Each time value must carry its required zone label in the correct cell. A UTC label somewhere else doesn't make up for a missing one. A clock value without its zone fails the gate.

A malformed source packet, or one from a different case, stops the whole comparison before any results are written. That isn't a candidate failure, and it doesn't count toward repair cost. A malformed candidate brief with valid sources is a format-gate failure and stays in the comparison.

![Supplied-file checks do not measure model variation; repeated live pairs separate observed between-instruction disagreements from within-instruction variation.](shared/figures/m08-evidence-lanes.png)

*Supplied-file checks do not measure model variation; repeated live pairs separate observed between-instruction disagreements from within-instruction variation.*

<details markdown="1">
<summary>Figure text</summary>

Separate change from variation. There are two evidence lanes, and their results are never pooled.

- **Supplied files.** The same 40 cases each have a baseline, A, and B brief. Deterministic checks read these fixed files. Repeating those checks gives the same answer, so they do not measure model variation. One violation rejects a candidate.
- **Optional live comparison.** Six cases (PC-01 to PC-06) are planned. Each case has three repeat slots for the baseline instruction and three for the checked instruction. Same-case pairs join a baseline attempt to a checked attempt on the same case. Within-instruction variation compares the repeats of one instruction on one case. Every attempt is retained. One violation rejects adoption.

The live lane follows a sequence recorded before any call runs. Calls alternate the order of baseline and checked instructions. Within each pair, the model, source/form pair, prompt, and permissions stay fixed. That makes 36 comparison calls. After them, the baseline is restored and two restored controls run on PC-01 and PC-02. These are planned observations, not results. A finished sequence does not prove that either instruction is better.

</details>

## Class-only boundary
All names, hours, and masses used as defects are fictional course fixtures. Don't use this packet to plan, authorize, dispatch, or describe a real movement. A module result is for class review only.
