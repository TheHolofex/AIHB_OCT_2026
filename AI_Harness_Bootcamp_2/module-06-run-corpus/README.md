# Module 6 · Improve from observed failures

Find a repeated failure in Blue Gauge's practice records. Before you look at any outcomes, freeze the sixteen-run sample. Record each run's first failure or no failure and check that the category counts add up to sixteen. Choose two exact pieces of text from your notes, configure the supplied check, and test what it catches and misses.

Plan for about three hours (a rough estimate).

## Start here

1. [Improve from observed failures](shared/MODULE_06_LAB.md): prepare a work folder, then build one narrow check from the practice runs and test its limits.

## The supplied check

A **predicate** is a yes-or-no condition. The supplied predicate checks whether a run file contains both exact strings you configure; uppercase and lowercase differ. It exits 1 if both are present and 0 if either is absent. A missing run file prints `HOLD: missing input`; a malformed configuration prints `HOLD: malformed config`. Try it on known-bad, known-good, and missing input. Configure this control; don't write another checker.

## Class-only boundary

The eighty records, names, identifiers, and run notes are fictional course fixtures about oxygen cylinders moving from East Yard to Clinic O-2. They aren't real workplace observations or a measure of current models' reliability. Don't use this packet to plan, authorize, dispatch, or describe a real movement. A module result is for class use only.
