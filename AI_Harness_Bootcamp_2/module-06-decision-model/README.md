# Module 6 · Use Jev inside Oh My Pi

At the Blue Gauge airlift desk, you can put typed answers to work in four different ways: ask several questions together, hold uncertain messages for a person, combine separate scores into an attention order, and send requests to the right kind of help. Allow about three hours for the four experiments and a review packet. [Open the Blue Gauge desk lab](shared/MODULE_06_LAB.md).

## Blue Gauge: the last resupply flight

It is 05:00 UTC+02 on 15 October 2026 at Aster Airhead, the cargo-staging airfield. Flight BG-F17 is planned for Forward Support Base Kestrel. The cargo list closes at 05:30 and the aircraft departs at 06:00. The following flight is **not supplied**. Kestrel needs generator spares, medical-equipment battery kits, and water-system repair parts. Eighty overnight messages describe cargo and shortages; sixteen requests ask the desk for help. Some cargo is received but not released. Other cargo is released but has no acceptance for BG-F17.

[Desk rules](shared/case/DESK_RULES.md) separate stock release from acceptance for this exact flight. The duty logistics officer owns the message-review queue and proposed handoff. The cargo release officer owns stock release; the air movement controller owns flight acceptance and dispatch. A message route of `PASS` means normal desk processing, `RETURN` requests correction, and `REVIEW` calls for officer attention. None clears cargo.

## The work in Oh My Pi

Oh My Pi (OMP) keeps the conversation and the desk controls together. Its chat model is `openrouter/anthropic/claude-sonnet-4.6`; its typed decision model, Jev, is `openrouter/typesafe/jev-1.13`. Both use the same OpenRouter key; no separate TypeSafe key is needed. You tell OMP which supplied control to change and inspect what actually ran. The supplied engine does the source checks and arithmetic; you don't write executable code.

The case messages and requests are fictional. Their text goes through OpenRouter to Jev for typed judgments; the OMP chat model remains conversational. Keep real operational and personal data out of this case. Supplied code checks source records and executes lookups, record comparisons, or officer-queue entries. No message, model confidence, attention score, or handler result can release stock, accept cargo for a flight, or dispatch an aircraft. The handoff is a **review packet — not a manifest or movement order**.
