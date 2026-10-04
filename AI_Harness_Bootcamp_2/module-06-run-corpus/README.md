# Module 6 · Improve from observed failures

You're going to find a failure that shows up more than once in Blue Gauge's practice records. Before you look at any results, freeze which sixteen runs you'll read. For each run, write the first problem you can point to, or that you found no failure, and check that the category counts add up to sixteen. Then pick two exact pieces of text from your notes, put them in the supplied check, and see what it catches and what it misses.

Plan for about three hours. That's a rough estimate.

## Start here

1. [Improve from observed failures](shared/MODULE_06_LAB.md): prepare a work folder, then build one narrow check from the practice runs and test its limits.

## The supplied check

The supplied check is a predicate, which means a yes-or-no question a program can answer. You give it two exact pieces of text. It looks in a run file for both of them. Capitals and lowercase are different. It exits 1 if both are present and 0 if either is missing. A missing run file prints `HOLD: missing input`. A config that isn't the shape it expects prints `HOLD: malformed config`. Try it on a run you know is bad, a run you know is good, and a missing file. You configure this check. Don't write another one.

## Class-only boundary

The eighty records, names, identifiers, and run notes are made up for class. They're about oxygen cylinders moving from East Yard to Clinic O-2. They aren't real workplace notes, and they don't measure how reliable current models are. Don't use this packet to plan, authorize, dispatch, or describe a real movement. What you produce here is for class use only.
