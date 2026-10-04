# Module 8 · Control hallucinations

Turn a plausible brief into a claim-by-claim account of what the sources support, what needs correction, and what remains unknown. Have separate agents challenge the claims, then check their corrections yourself. A clean JSON response can contain a false fact. Two reviewers can agree and still be wrong.

Plan for a little over two hours on Thursday (a rough estimate). The work uses five paid agent sessions: two initial reviews, one correction, and two fresh reviews of the correction. Each session may make several provider requests.

[Open the hallucination-control lab](shared/MODULE_08_LAB.md).

## The brief someone might act on

Slope Brief concerns heater-fuel cans at Ridge Depot for Clinic T-8 on vehicle `SB-4`. A desk brief gives the mass, gate times, and a claim about permission to depart. If an unsupported number or an unlabeled clock reaches the next desk as fact, a fluent answer has become a bad operating instruction.

You have seven material claims—claims that could change a decision—across three separate case packets, PC-01, PC-02, and PC-03. Keep each claim with its own packet; don't combine their masses or clocks into one shipment record. The draft is authored practice data with deliberate defects, not a recorded model failure. Your agents' reviews and corrections are live outputs. Keep those two kinds of evidence separate.

The supplied sources can establish facts about a shipment. They don't supply every fact or permission needed to dispatch it. An honest brief must preserve that gap.

## Keep three questions separate

| Question | What checks it | What it cannot establish |
|---|---|---|
| Does the answer have the required shape? | A **schema**, the list of required fields and allowed values. The checker also requires every claim exactly once. | Valid JSON doesn't make a number or a judgment true. |
| Does this source support this claim? | Exact checks for values, units, zones, shipment identity, and source locators; separate agent reviews of the claim and evidence; your reading of the original source. | A real citation doesn't establish a claim beyond what its text says. |
| May someone act on it? | The responsible person's authority and any required operational facts. | A supported mass, an open gate, or unanimous reviewers do not authorize departure. |

A **hallucination** is an assertion presented as established when the available evidence doesn't establish it. It can be an invented fact, a claim attached to the wrong source, or a stronger conclusion than the source permits. Control the claim at the point it would become usable work; don't rely on a reminder to “be accurate.”

## Use a model for a narrow judgment

[Jev](https://docs.typesafe.ai/introduction) takes a **state**—the facts to inspect—and **typed questions**, which have fixed answer types. That pattern makes a judgment inspectable: ask one question about one claim, return a named answer, and let code decide which checks or holds follow.

Here the question is: **Does this source packet establish this exact claim?** Each reviewer must choose `supported`, `contradicted`, or `unknown`, identify the source, quote it, and explain the connection. `unknown` means the packet doesn't settle the claim; it doesn't mean the claim is false. Use the [typed-question discipline](../module-04-typed-decisions/README.md) you already practiced, now on a draft's factual claims.

These runs use the pinned course model through Oh My Pi, not Jev's service. The model generates JSON and a supplied checker validates it; this is not provider-enforced structured output. Jev's [probabilities and confidence](https://docs.typesafe.ai/confidence) are separate from the evidence that establishes a fact. A model's confident wording is not a calibrated probability, and no confidence threshold replaces a source check here.

## Let reviewers challenge before they confer

An **ensemble** uses several model or agent judgments on the same work. Give the reviewers different jobs and keep their first judgments separate.

| Agent | Job | What it can see |
|---|---|---|
| Source reviewer | Check the exact claim against the appropriate source, including units and zone labels. | The claim set and original source packets. |
| Skeptical reviewer | Look for a wrong shipment, a misleading citation, an omitted condition, or a fact being treated as permission. | The same claims and sources, without the other reviewer's verdicts. |
| Correcting agent | Repair only what the sources support and keep missing facts explicitly unknown. | The original claims and sources, deterministic findings, and both completed reviews. |

After correction, both reviewers start fresh again. They see the revised claims and original sources, not their earlier verdicts. The supplied tool checks every claim again, including the ones that were already correct.

All five turns use separate sessions of `openrouter/anthropic/claude-sonnet-4.6`. Separate sessions prevent one reviewer from copying the other's answer; they do not create independent model families or independent sources. The agents can share the same blind spot. In workplace use, an approved different model can add another perspective, but it still needs the same evidence checks.

## Decide from evidence, not votes

If both reviewers approve a mass that disagrees with the inventory record, the mass stays on hold. If they disagree, read the cited passages and identify which supports the exact claim; don't ask a third agent to break the tie by vote. If neither source establishes permission to depart, keep that permission unknown.

A correction is another model output, not a trusted repair. Preserve the original, check every changed value, and check that a previously supported claim wasn't damaged or dropped. You can accept a useful internal source summary with a clearly stated unknown. You cannot turn that acceptance into dispatch authority.

## Class-only boundary

The Slope Brief case is fictional: heater-fuel cans move from Ridge Depot to Clinic T-8 on vehicle SB-4. Names, hours, and masses used as defects are fictional course fixtures. Don't use this packet to plan, authorize, dispatch, or describe a real movement. Results are for class review only.
