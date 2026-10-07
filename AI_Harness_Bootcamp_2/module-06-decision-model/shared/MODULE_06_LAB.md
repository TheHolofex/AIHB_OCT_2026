# Module 6 · Use Jev inside Oh My Pi

Open ordinary Oh My Pi and install the TypeSafe skill. Oh My Pi stays the chat agent. It writes code that calls Jev through OpenRouter, using the key you already have. Jev answers the fixed questions. Your code decides what to do with those answers. Each pattern is its own section. Plan for about three hours.

## Blue Gauge: the last resupply flight

It is 05:00 UTC+02 on 15 October 2026 at Aster Airhead. Flight BG-F17 is planned to Forward Support Base Kestrel. The cargo list closes at 05:30 and the aircraft departs at 06:00. The next flight is **not supplied**.

Read the [desk rules](case/DESK_RULES.md). Stock release and exact-flight acceptance are separate records. `PASS`, `RETURN`, and `REVIEW` are message routes. None of them releases stock, accepts cargo for BG-F17, or dispatches the aircraft.

The messages are in `shared/case/notes`. The requests are in `shared/case/requests`. Stock is in `shared/case/scans.json`. Flight acceptance is in `shared/case/flight_acceptances.json`.

## Start Oh My Pi

Use the same terminal where Oh My Pi already works, with `OPENROUTER_API_KEY` already set. Start in this module folder so the session can read the case. Do not set a judge role, and do not create a TypeSafe key. Jev is not the chat model.

**Terminal: Bash or zsh, ordinary user.**

```bash
cd "$HOME/Documents/AIHB_OCT_2026/AI_Harness_Bootcamp_2/module-06-decision-model"
omp
```

**Terminal: PowerShell, ordinary user.**

```powershell
Set-Location "$HOME\Documents\AIHB_OCT_2026\AI_Harness_Bootcamp_2\module-06-decision-model"
omp
```

**Expected:** Oh My Pi opens in this folder. The chat model is the one you already use.

**Stop:** Stop if `omp` is not found, or if the key appears on screen.

**Recovery:** Return to [setup](../../module-00-setup/README.md) if Oh My Pi or the OpenRouter key is missing.

## Install the TypeSafe skill

In that session, paste the install step from the [TypeSafe quick start](https://docs.typesafe.ai/introduction/quickstart#vibe-it-the-agent-skill), then the OpenRouter constraint.

```text
Install the TypeSafe skill. If you're in Claude Code, run `claude plugin marketplace add typesafe-ai/skills`, then `claude plugin install typesafe@typesafe-ai`. If you're in another agent, run `npx skills add typesafe-ai/skills --skill typesafe-ai` and select your agent. Use one installation method. You can read the skill directly at https://github.com/typesafe-ai/skills/blob/main/skills/typesafe-ai/SKILL.md (raw: https://raw.githubusercontent.com/typesafe-ai/skills/main/skills/typesafe-ai/SKILL.md). Then use the TypeSafe skill when working on this project.

Call Jev through OpenRouter, not the TypeSafe API. Use the OpenRouter key already in OPENROUTER_API_KEY. Point the TypeSafe SDK at https://openrouter.ai/api, or POST https://openrouter.ai/api/v1/systemone. Use model jev-1.13. Do not ask for a TypeSafe key. Do not use jev-latest.
```

The skill reads the TypeSafe docs and writes the questions, gates, and code. OpenRouter serves Jev. Code owns the route, the gate, the weights, and the handler. Put the questions and thresholds in one place, and read them before you accept them. A Jev answer is not cargo authority.

**Expected:** The skill is loaded. The agent agrees to call `jev-1.13` through OpenRouter with the key already in the environment.

**Stop:** Stop if it asks for a TypeSafe key, uses `jev-latest`, makes Jev the chat model, prints the key, or writes the key into a file.

**Recovery:** Paste the second paragraph again. If the installer does not list Oh My Pi, tell it to read the raw skill file in that prompt and use that.

## 1. Speculative fan-out

[Speculative fan-out](https://docs.typesafe.ai/patterns/fan-out) asks every question you might need in one Jev call, including questions the route may not use. Jev answers them together. Your code then decides which answers matter.

Use it when one item needs several independent judgments, and you do not yet know which of them the next step will use. A support note may be a bug, a billing problem, and a feature request at once. A cargo message may claim release, claim flight acceptance, and also carry an instruction to skip a check. Asking the first question and waiting hides the others and costs another round trip. Ask them together, then ignore the answers the route does not use.

Do not ask the first question, wait, and then ask the next one. A follow-up call is slower, and it hides answers you already could have had. An ignored answer stays on the page. It must not change `PASS`, `RETURN`, or `REVIEW`.

![One message goes to one Jev call. Used answers can change the route. An ignored answer stays visible and does nothing.](figures/m06-fan-out.png)

*One message goes to one Jev call. Used answers can change the route. An ignored answer stays visible and does nothing.*

**In OMP:**
```text
Using the TypeSafe skill, read the fan-out pattern and the OpenRouter Jev docs. Write code that sends each practice message in shared/case/notes/tuning to jev-1.13 through OpenRouter with several questions in one call, including one the route may ignore. Put the questions in one place. Show the actual request, which answers the route used, and which it ignored.
```

**Expected:** One OpenRouter call per message carries every question. An ignored answer is marked and does not change the route.

**Stop:** Stop if it asks the questions one at a time when you asked for one call, or if a message route is treated as clearance.

## 2. Confidence-gated routing

[Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing) uses two facts from the same answer. The choice says what Jev selected. The confidence says whether you should act on it. Your code holds the gate. A low gate lets more messages through. A high gate sends more of them to a person.

Use it when a wrong automatic action is more costly than a delay. Checking a balance can accept a lower confidence than approving a transfer. On this desk, an ordinary message can pass at a lower gate than a message that claims stock is released. The middle band belongs to a person. Do not use a gate when you only need the best option and a wrong pick is harmless.

Compare gates on the saved answers. Do not call Jev again to move the gate. The confidence on a choice is not the same number as the top option's probability. Read the confidence the API returns.

![Saved answers meet a confidence gate. At or above the gate, the desk continues. Below it, a person reads the message. Moving the gate does not call Jev again.](figures/m06-confidence.png)

*Saved answers meet a confidence gate. At or above the gate, the desk continues. Below it, a person reads the message. Moving the gate does not call Jev again.*

**In OMP:**
```text
Using the TypeSafe skill, keep those saved Jev answers. In code, send a message to a person when confidence on the chosen answer is low. Compare two gates on the same answers. Do not call OpenRouter again for the comparison. Keep the gate next to the questions.
```

**Expected:** The second gate changes who waits for a person, and it makes no new Jev call.

**Stop:** Stop if the comparison calls Jev again, or if high confidence is treated as stock release or flight acceptance.

## 3. Composite scoring

[Composite scoring](https://docs.typesafe.ai/patterns/composite-scoring) asks Jev for separate scores, then combines them in code. Urgency, stated mission impact, and handoff risk are different questions. A weight says how much each score counts. Change the weights and the attention order can change. The scores do not.

Use it when several qualities matter at once and a person may want to change which one counts more. A queue can rank by customer frustration, revenue, and time waiting. This desk ranks by urgency, stated mission impact, and handoff risk. Ask for the scores once. Try a new policy by changing the weights, not by asking Jev again. Do not use one blended score when any single failure must stop the work. That needs a separate yes-or-no check.

Do not call Jev again to try a new weight set. A high rank is desk attention. It is not a loading list, a release, or acceptance for BG-F17.

![Saved scores for urgency, mission impact, and handoff risk. Two weight sets produce two attention orders. Neither calls Jev again.](figures/m06-scoring.png)

*Saved scores for urgency, mission impact, and handoff risk. Two weight sets produce two attention orders. Neither calls Jev again.*

**In OMP:**

```text
Using the TypeSafe skill, read the composite-scoring pattern. Write code that asks jev-1.13 through OpenRouter for urgency, stated mission impact, and handoff risk, then combines those scores with weights. Change the weights and show the new order from the saved scores, without another call. This is desk attention, not cargo allocation.
```

**Expected:** You can see each score's contribution. The new weights change the order, or you can see why a message did not move. No new Jev call.

**Stop:** Stop if a high rank is treated as authority to load or dispatch.

## 4. Intent routing

[Intent routing](https://docs.typesafe.ai/patterns/intent-routing) asks Jev what kind of work the request is, then sends it to the matching path. Judge the work being requested, not how serious the cargo sounds.

Use it when different requests need different kinds of help, and a chat reply would be the wrong tool for some of them. A status question can be a lookup. A record question can be a comparison. A draft, an approval, or an uncertain request needs a person. A loud shortage does not make a waiver into a lookup. Route by the work, then show what actually ran.

A status lookup reads one record. A record question compares the supplied stock and flight records for this cargo and BG-F17 at 05:00. A draft, an approval, or an uncertain request comes to you. Show what actually ran. A lookup is not a clearance. A comparison is not dispatch. A queue entry is not approval.

![Jev classifies the request. A lookup reads a record, a comparison checks the BG-F17 record, and a draft or approval comes to a person. None of those paths clears cargo.](figures/m06-intent.png)

*Jev classifies the request. A lookup reads a record, a comparison checks the BG-F17 record, and a draft or approval comes to a person. None of those paths clears cargo.*

**In OMP:**

```text
Using the TypeSafe skill, read the intent-routing pattern. Write code that asks jev-1.13 through OpenRouter to classify every request in shared/case/requests, then runs the matching path: a status lookup reads a record, a record question compares the supplied stock and flight records, and a draft, approval, or uncertain request comes to me. Show the request and what actually ran. Nothing you run releases cargo or accepts it for BG-F17.
```

**Expected:** Each request has a typed intent and a path you can inspect. An approval comes to you. A lookup or comparison cites `scans.json` or `flight_acceptances.json`.

**Stop:** Stop if an approval is handled without you, or if a result is called clearance.

## Hand off

```text
Using the TypeSafe skill, write the airlift-desk handoff. Four rows: pattern, what I changed, what I observed, and the limit. Name one message or request I inspected for each pattern, with its source. List what a person still has to decide, and who owns it. Label it "review packet — not a manifest or movement order".
```

**Expected:** Every row names a real message or request from this session. No row claims cargo clearance, flight acceptance, or dispatch.
