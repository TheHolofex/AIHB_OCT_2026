# Module 6 · Design a workflow for a decision model

You're going to choose a decision model in Oh My Pi, pin it through OpenRouter, and build a screen around it. Blue Gauge's desk checks the handoff notes an assistant drafts for oxygen cylinders against the yard's scan record. You'll write the questions the model answers, set the thresholds that turn its probabilities into routes, and prove the frozen screen on notes you didn't tune it on.

Plan for about three hours on Wednesday. That's a rough estimate.

## Start here

1. [Design, tune, and prove the screen](shared/MODULE_06_LAB.md).

## What a decision model does

A decision model answers fixed questions about a piece of text with typed values. That can be how likely the answer is yes, which option from a list fits, with a probability for each, or where something sits on a scale you define. It doesn't write prose, and it can't answer outside the options you give it. Your code acts on its answers, and the probability tells your code when to hand a case to a person.

TypeSafe's Jev is one of these models. Oh My Pi calls it as the judge through OpenRouter, billed to the same key as the course chat model. Jev reads your words literally, it's weak at counting and comparing dates, and it leans toward the first option in a list. The screen is built around those weak spots.

## How the screen splits the work

- Code settles what a rule can: the cylinder ID, a cited release order, and the scan status.
- The decision model reads the note. It says whether the note claims a release, which status it gives, whether it tells the reader to do something, and how urgent it sounds.
- The duty officer gets every note the screen can't settle. The Release Authority owns every release.

## Class-only boundary

The eighty notes, scan records, and desk labels are made up for class. They're about oxygen cylinders moving from East Yard to Clinic O-2. Don't use them to plan, authorize, or describe a real movement. What you produce here is for class review only.
