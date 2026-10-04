# Module 6 · Improve from observed failures

Find a repeated failure in Blue Gauge's practice records. Choose two exact pieces of text from your notes, configure the supplied check, and test what it catches and misses. Freeze the sixteen-run sample before you read outcomes. Record each run's first failure or no failure, then group the failures and check that the counts add up to sixteen.

Plan for about three hours (a rough estimate, not a measured time).

## Start here

1. [Improve from observed failures](shared/MODULE_06_LAB.md): start with the sample rule, then build and test one narrow check.

## The supplied check

A **predicate** is a yes-or-no condition. The supplied predicate checks whether a run file contains both exact strings you configure; uppercase and lowercase differ. It exits 1 when both are present and 0 when either is absent. A missing run file prints `HOLD: missing input`; a malformed configuration prints `HOLD: malformed config`. Check the predicate on known-bad, known-good, and missing input. Configure this control; don't write another checker.

## Class-only boundary

The eighty records, names, identifiers, and run notes are fictional practice data about oxygen cylinders moving from East Yard to Clinic O-2. They aren't real workplace observations or a measure of current models' reliability. Don't use them to plan, authorize, dispatch, or describe a real movement. Results are for class review only.
