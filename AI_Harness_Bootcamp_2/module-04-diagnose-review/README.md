# Module 4 · Diagnose and recover

Find where required information disappears from a Copper Span duty card before changing the workflow. Preserve the failure, use a check that distinguishes missing source data from a display failure, and make one authorized, reversible correction. Prove recovery under the original requirements.

Plan for one three-hour facilitated session, including two hours of practice. This is a planning allowance, not a measured completion guarantee.

The supplied ledger is the local record for this case. Current rows must supply `permit_status` and `gate_time_mdt`. These fields record permit status and the gate time in Mountain Daylight Time; they do not authorize movement.

## Start here

1. [Diagnose and recover the duty card](shared/MODULE_04_LAB.md).

Use your existing source checks, permission limits, and evidence records. Identify the last point where the required information is present and the first point where it is missing. Preserve both observations before authorizing a correction.

## What you inspect

The **renderer** is the supplied program that turns ledger rows into a duty card. The clean version writes both required fields. Prove that you can restore that version before a practice fault is placed. Save the first failure and its diagnostic evidence before replacing anything. Check recovery with a focused field check, a complete render, and a new process in a fresh folder.

## Class-only boundary

All names, times, and statuses are fictional course fixtures. Do not use this packet to plan, authorize, dispatch, or describe a real movement. A module result permits only class review.
