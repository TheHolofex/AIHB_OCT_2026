# Module 5 · Improve from observed failures

Find a repeated failure in Blue Gauge's practice records and turn it into one check the supplied control can apply consistently. Use your preserved observations to choose an exact text condition, then establish what it catches and what it misses.

The eighty records are authored practice runs about oxygen cylinders moving from East Yard to Clinic O-2. They are not workplace observations or evidence of current model reliability. Freeze the sixteen-run sample before opening outcomes. Record each run's first failure, or that you found none, before grouping failures and reconciling the counts to sixteen.

Plan for one three-hour facilitated session, including two hours of practice. This is a planning allowance, not a measured completion guarantee.

## Start here

1. [Derive and check a bounded control](shared/MODULE_05_LAB.md) from the authored run records.

## The supplied check

A **predicate** is a condition with a yes-or-no result. The supplied predicate checks whether one run file contains both exact pieces of text you configure. It treats uppercase and lowercase as different. It exits 1 when both are present and 0 when at least one is absent. A missing run file prints `HOLD: missing input`. A malformed configuration prints `HOLD: malformed config`. Choose the two strings from your failure notes and check known-bad, known-good, and missing input. You configure the supplied control; you do not write a second checker.

## Class-only boundary

All names, identifiers, and run notes are fictional course fixtures. Do not use this packet to plan, authorize, dispatch, or describe a real movement. A module result permits only class review.
