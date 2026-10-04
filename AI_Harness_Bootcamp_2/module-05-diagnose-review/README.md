# Module 5 · Diagnose and recover

Find where a required field disappears from a Copper Span duty card before you change anything. Keep the failed result. Use the probe to tell whether the source lacks the field or the renderer dropped it. Make one authorized correction you can undo, then prove the card recovered under the original acceptance requirements.

Plan for about three hours (a rough estimate).

The supplied ledger is the record for this case. Its current rows must include `permit_status` and `gate_time_mdt` (the gate time is in Mountain Daylight Time). Neither field authorizes movement.

## Start here

1. [Diagnose and recover the duty card](shared/MODULE_05_LAB.md).

Bring the source checks, permission limits, and evidence records from earlier modules. Record the last point where the field is present and the first point where it's missing before you authorize any correction.

## What you inspect

The supplied **renderer** turns ledger rows into a duty card. The clean version writes both required fields. First check that restore works. Then place a practice fault, keep the first failure and its probe output, and replace the renderer once. Prove the repair three ways: a focused field check, a complete render, and a new process in a fresh folder.

## Class-only boundary

All names, times, and statuses are fictional course fixtures. Don't use this packet to plan, authorize, dispatch, or describe a real movement. A module result is for class use only.
