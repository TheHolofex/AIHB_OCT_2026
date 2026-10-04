# Module 6 · Improve from observed failures

Find a repeated failure in Blue Gauge's practice records and turn it into one check that the supplied control applies the same way every time. Use the notes you kept to choose an exact text condition, then find out what it catches and what it misses.

The eighty records are invented practice runs about oxygen cylinders moving from East Yard to Clinic O-2. They aren't real workplace observations, and they don't show how reliable current models are. Freeze the sixteen-run sample before you look at any outcomes. Note each run's first failure, or that you found none, before you group the failures and check that the counts add up to sixteen.

Plan for about three hours. That's a rough estimate, not a measured time.

## Start here

1. [Improve from observed failures](shared/MODULE_06_LAB.md): build one narrow check from the practice runs and test its limits.

## The supplied check

A **predicate** is a condition with a yes-or-no answer. The supplied predicate checks whether one run file contains both of the exact pieces of text you configure, with uppercase and lowercase treated as different. It exits 1 when both are present and 0 when at least one is absent. A missing run file prints `HOLD: missing input`, and a malformed configuration prints `HOLD: malformed config`. You choose the two strings from your failure notes and check them on known-bad, known-good, and missing input. You configure the supplied control; you don't write a second checker.

## Class-only boundary

All names, identifiers, and run notes are fictional course fixtures. Don't use this packet to plan, authorize, dispatch, or describe a real movement. A module result is for class review only.
