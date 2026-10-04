# Module 5 · Diagnose and recover

Before changing the workflow, find where required information disappears from a Copper Span duty card. Keep the failed result, use a check to tell missing source data from a display failure, and make one authorized correction you can reverse. Then prove recovery against the original requirements.

Plan for about three hours, though that's a rough estimate rather than a measured time.

The supplied ledger is the local record for this case. Current rows must include `permit_status` and `gate_time_mdt`. These fields record permit status and gate time in Mountain Daylight Time, but they do not authorize movement.

## Start here

1. [Diagnose and recover the duty card](shared/MODULE_05_LAB.md).

Use the source checks, permission limits, and evidence records you already have. Find the last point where the required information is present and the first point where it goes missing, then record both before authorizing a correction.

## What you inspect

The supplied **renderer** turns ledger rows into a duty card. The clean version writes both required fields. Before a practice fault is placed, prove that you can restore that version. Keep the first failure and its diagnostic evidence before replacing anything. Then check recovery with a focused field check, a complete render, and a new process in a fresh folder.

## Class-only boundary

All names, times, and statuses are fictional course fixtures. Do not use this packet to plan, authorize, dispatch, or describe a real movement. A module result permits only class review.
