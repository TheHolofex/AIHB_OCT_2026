# Module 6 · Design a workflow for a decision model

Choose a decision model in Oh My Pi, pin it through OpenRouter, and build a screen around it. Blue Gauge's desk checks AI-drafted handoff notes for oxygen cylinders against the yard's scan record. Write the questions the model answers, set the thresholds that turn its probabilities into routes, and prove the frozen screen on notes you didn't tune it on.

Plan for about three hours on Wednesday (a rough estimate).

## Start here

1. [Design, tune, and prove the screen](shared/MODULE_06_LAB.md).

## What a decision model does

A decision model answers fixed questions about a piece of text with typed values: the probability of yes, one option from a list with a probability for each, or a position on a scale you define. It writes no prose and can't answer outside the options you give it. Code acts on its answers, and the probability tells the code when to hand a case to a person.

TypeSafe's Jev is one such model. Oh My Pi calls it as the **judge** through OpenRouter, billed to the same key as the course chat model. Jev reads what you wrote literally, does poorly at counting and comparing dates, and leans toward the first option in a list, so the screen is designed around those weak spots.

## How the screen divides the work

- **Code** settles what a rule can: the cylinder ID, a cited release order, and the scan status.
- **The decision model** reads the note: whether it claims a release, which status it gives, whether it tells the reader to do something, and how urgent it sounds.
- **The duty officer** gets every note the screen can't settle. **The Release Authority** owns every release.

## Class-only boundary

The eighty notes, scan records, and desk labels are fictional practice material about oxygen cylinders moving from East Yard to Clinic O-2. Don't use them to plan, authorize, or describe a real movement. A module result is for class review only.
