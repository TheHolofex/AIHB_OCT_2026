# Module 5 · Diagnose and recover

A required field drops off a Copper Span duty card. Find where it disappeared before you change anything. Keep the failed card. The probe tells you whether the source never had the field, or the program that writes the card left it out. Then make one correction you can undo, and show the card meets the same rules as before.

Plan for about three hours (a rough estimate).

The supplied ledger is the record for this case. Its current rows must include `permit_status` and `gate_time_mdt` (the gate time is in Mountain Daylight Time). Neither field authorizes movement.

## Start here

1. [Diagnose and recover the duty card](shared/MODULE_05_LAB.md).

Bring the source checks, permission limits, and evidence records from earlier modules. Write down the last place the field is still there, and the first place it's gone, before you allow any correction.

## What you inspect

The **renderer** is the program that turns ledger rows into a duty card. The clean version writes both required fields. First check that you can put that clean version back. Then place a practice fault, keep the first failure and what the probe prints, and replace the renderer once. Show the repair three ways: a check of just those fields, a complete card, and a new run in a fresh folder.

## Class-only boundary

All names, times, and statuses are fictional. Don't use this packet to plan, authorize, dispatch, or describe a real movement. A module result is for class use only.
