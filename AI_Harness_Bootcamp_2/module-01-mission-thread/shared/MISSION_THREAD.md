# Read a mission thread without getting lost in it

A polished brief can cite true facts and still recommend a movement those facts don't support. Before accepting Cold Lantern's `GO`, check what each step shows and what the next step needs. Allow about 15 minutes to examine the eight steps.

## What a mission thread is

A **mission thread** is the ordered path from a request to a result. It shows what must happen, in what order, and what each step must hand to the next.

![Evidence must support each required handoff to the decision point; expected arrival does not establish delivery or usable effect.](figures/m01-thread-handoffs.png)

*Evidence must support each required handoff to the decision point; expected arrival does not establish delivery or usable effect.*

<details markdown="1">
<summary>Figure text</summary>

Follow the required path in order: 1. Requirement defined; 2. Cargo received; 3. Cargo released; 4. Vehicle made ready; 5. Movement authorized; 6. Route window met; 7. Cargo delivered; 8. Usable effect confirmed. Each step's output must meet the next step's entry condition. The links show required handoffs, not checks already completed. Delivery and usable effect are not yet observed.

</details>

Cold Lantern uses eight steps:

1. **Requirement defined** — the destination, usable quantity, route, and deadline are clear.
2. **Cargo received** — the warehouse records the exact totes and lots in its custody.
3. **Cargo released** — the quality office identifies which lots may be used.
4. **Vehicle made ready** — the released load and required rack fit the vehicle.
5. **Movement authorized** — the permit applies to the exact vehicle and route.
6. **Route window met** — the vehicle can reach the gate before it closes.
7. **Cargo delivered** — the route can reach the clinic by the deadline, and later evidence records actual delivery.
8. **Usable effect confirmed** — the clinic records receipt of the required released quantity.

At step 6, decide whether the supplied evidence supports the brief's `GO`. Expected arrival does not prove delivery or clinic use.

## Why a thread becomes difficult

Check what each recorded state means. For example, a custody record alone doesn't show permission to use the cargo.

“Cargo received” opens into smaller questions:

- Were the exact totes scanned?
- Do their lot IDs match this mission?
- How many kits are in each tote?
- Does the warehouse record custody, or does it also have authority to release the kits?
- Was the record current at the decision time?
- What does the next step require?

The same pattern repeats inside every step. Check these seven parts when they matter:

| Part | Plain question |
|---|---|
| Identity | Is this the exact mission, route, vehicle, permit, lot, clinic, and source revision? |
| Authority | Is this source allowed to establish this kind of fact? |
| Time | Was it current at 14:05 MDT, and is its time zone understood? |
| Quantity or condition | Are the count, units, required equipment, and state correct? |
| Dependency | What had to be true before this step could begin? |
| Handoff | Does this step's output meet the next step's entry condition? |
| Uncertainty | What is unknown, assumed, contradicted, or not yet observed? |

**Stop decomposing**—splitting a claim into smaller claims to check—when you reach one of these:

- a fact you can read directly in an applicable source;
- a calculation you can reproduce from supported facts and units;
- an assumption you have named as an assumption;
- an unresolved item that requires `HOLD`; or
- a decision owned by a named person.

## Five kinds of statement

Give each **material statement** in the AI brief one label. These are the statements that could change the decision.

![Split a mixed sentence until each material statement has one kind and its own support.](figures/m01-statement-types.png)

*Split a mixed sentence until each material statement has one kind and its own support.*

<details markdown="1">
<summary>Figure text</summary>

Split a compound statement into separate rows so each row has one kind. A SOURCE FACT needs an applicable source that states it; a CALCULATION needs supported values and units; an INFERENCE needs an interpretation with a reason; and a DECISION needs a named human owner. Mark a statement UNSUPPORTED when adequate support is absent. These are different kinds of statements, not steps that turn a fact into an approval.

</details>

- `SOURCE FACT` — an applicable source directly states it.
- `CALCULATION` — supported numbers and units produce it.
- `INFERENCE` — you interpret facts and state why that reading follows.
- `DECISION` — a named person chooses what happens next.
- `UNSUPPORTED` — no applicable source or sound calculation establishes it.

A sentence can contain more than one kind. Split it until each row has one kind.

## Source authority belongs to the claim

A source is not trustworthy for everything.

![A genuine source may still be the wrong authority for this claim, entity, route, or decision time.](figures/m01-source-authority.png)

*A genuine source may still be the wrong authority for this claim, entity, route, or decision time.*

<details markdown="1">
<summary>Figure text</summary>

For custody, use the warehouse; for release, the quality office; for payload, Fleet Engineering; for the gate window, the Road Authority; and for permit status, the Movement Registry. Even a genuine warehouse record cannot establish release. Check the exact entity and current version for every claim: a genuine record may still be the wrong one.

</details>

- The warehouse records what it scanned.
- The quality office decides which lots are released.
- Fleet Engineering defines vehicle payload and required equipment.
- The Road Authority sets the gate window.
- The Movement Registry records permit status.

A genuine warehouse receipt can be the wrong source for usability. A current community update can be the wrong source for another route. A vendor note can contain real dimensions and a hostile instruction in the same file. Judge the source against the exact claim.

## The handoff rule

Even when one step is correct, the overall conclusion can be wrong if that step hasn't established what the next step requires.

![Check what the next step requires; the earlier true statement cannot supply missing authority or observation.](figures/m01-broken-handoff.png)

*Check what the next step requires; the earlier true statement cannot supply missing authority or observation.*

<details markdown="1">
<summary>Figure text</summary>

Recorded custody does not remove the need for release, and a received permit still needs approval. Expected arrival still needs delivery evidence, while delivery still needs confirmation of usable quantity. Each state can be true without meeting the next requirement.

</details>

- Twelve totes can be scanned while only ten are released.
- Released cargo can fit while the required rack pushes another load over capacity.
- A permit application can be received while the permit remains pending.
- The clinic can be reachable by 16:00 while the gate closes before the truck arrives.

The thread passes only when every required handoff to the decision point passes. An estimated clinic arrival is not delivery, and delivery is not yet clinic confirmation.
