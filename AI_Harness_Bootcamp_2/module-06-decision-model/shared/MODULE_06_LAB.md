# Module 6 · Use Jev inside Oh My Pi

Open ordinary Oh My Pi, install the TypeSafe skill, and build four decision patterns on the Blue Gauge desk. Jev answers fixed questions. The chat model talks to you and writes the work. Both use the OpenRouter key you already have. Plan for about three hours.

## Blue Gauge: the last resupply flight

It is 05:00 UTC+02 on 15 October 2026 at Aster Airhead. Flight BG-F17 is planned to Forward Support Base Kestrel. The cargo list closes at 05:30 and the aircraft departs at 06:00. The next flight is **not supplied**.

Read the [desk rules](case/DESK_RULES.md). Stock release and exact-flight acceptance are separate records. `PASS`, `RETURN`, and `REVIEW` are message routes. None of them releases stock, accepts cargo for BG-F17, or dispatches the aircraft.

The messages are in `shared/case/notes`. The requests are in `shared/case/requests`. Stock is in `shared/case/scans.json`. Flight acceptance is in `shared/case/flight_acceptances.json`.

## Start Oh My Pi

Use the same terminal where Oh My Pi already works. Start in this module folder so the session can read the case. The extra config sets the judge role to Jev for this session only. It does not change the judge role saved on your computer.

**Terminal: Bash or zsh, ordinary user.**

```bash
cd "$HOME/Documents/AIHB_OCT_2026/AI_Harness_Bootcamp_2/module-06-decision-model"
omp --model openrouter/anthropic/claude-sonnet-4.6 --config shared/controls/judge.yml
```

**Terminal: PowerShell, ordinary user.**

```powershell
Set-Location "$HOME\Documents\AIHB_OCT_2026\AI_Harness_Bootcamp_2\module-06-decision-model"
omp --model openrouter/anthropic/claude-sonnet-4.6 --config shared/controls/judge.yml
```

**Expected:** Oh My Pi opens. The chat model is `openrouter/anthropic/claude-sonnet-4.6`. The judge role is `openrouter/typesafe/jev-1.13`.

**Stop:** Stop if `omp` is not found, or if the session asks for a separate TypeSafe key.

**Recovery:** Return to [setup](../../module-00-setup/README.md) if Oh My Pi is missing. The OpenRouter key already in this terminal is the only key. Do not start `scripts/blue_gauge.py`.

## Install the TypeSafe skill

In that Oh My Pi session, paste this. It is the install step from the [TypeSafe quick start](https://docs.typesafe.ai/introduction/quickstart#vibe-it-the-agent-skill). One extra constraint keeps the call on the Jev build you already have.

```text
Install the TypeSafe skill. If you're in Claude Code, run `claude plugin marketplace add typesafe-ai/skills`, then `claude plugin install typesafe@typesafe-ai`. If you're in another agent, run `npx skills add typesafe-ai/skills --skill typesafe-ai` and select your agent. Use one installation method. You can read the skill directly at https://github.com/typesafe-ai/skills/blob/main/skills/typesafe-ai/SKILL.md (raw: https://raw.githubusercontent.com/typesafe-ai/skills/main/skills/typesafe-ai/SKILL.md). Then use the TypeSafe skill when working on this project.

This session is Oh My Pi. Call Jev from this session as openrouter/typesafe/jev-1.13 through the OpenRouter key already in the environment. Do not ask for a TypeSafe key. Do not use jev-latest. Do not run scripts/blue_gauge.py.
```

**Expected:** The skill is loaded, and the agent agrees to use `openrouter/typesafe/jev-1.13`.

**Stop:** Stop if it asks for `TYPESAFE_API_KEY`, switches the judge to another model, or starts the course Python launcher.

**Recovery:** Paste the last paragraph again. If the installer does not list Oh My Pi, tell it to read the raw skill file above and use that.

## Build the four patterns

The patterns are [speculative fan-out](https://docs.typesafe.ai/patterns/fan-out), [confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing), [composite scoring](https://docs.typesafe.ai/patterns/composite-scoring), and [intent routing](https://docs.typesafe.ai/patterns/intent-routing). Read the questions the agent writes before you accept them. A Jev answer is not cargo authority.

### 1. Ask once, then use what matters

![One message goes to one Jev call. Used answers can change the route. An ignored answer stays visible and does nothing.](figures/m06-fan-out.png)

*One message goes to one Jev call. Used answers can change the route. An ignored answer stays visible and does nothing.*


```text
Using the TypeSafe skill, read the desk rules and the practice messages in shared/case/notes/tuning. Ask Jev several questions about each message in one call, including one question the route may ignore. Show which answers the route used and which it ignored. Use openrouter/typesafe/jev-1.13.
```

**Expected:** One Jev call per message carries every question. An ignored answer is marked and does not change the route.

**Stop:** Stop if it asks the questions one at a time when you asked for one call, or if a message route is treated as clearance.

### 2. Make uncertain notes wait

![Saved answers meet a confidence gate. At or above the gate, the desk continues. Below it, a person reads the message. Moving the gate does not call Jev again.](figures/m06-confidence.png)

*Saved answers meet a confidence gate. At or above the gate, the desk continues. Below it, a person reads the message. Moving the gate does not call Jev again.*


```text
Using the TypeSafe skill, keep those saved Jev answers. Send a message to a person when confidence on the chosen answer is low. Compare two gates on the same answers. Do not call Jev again for the comparison.
```

**Expected:** The second gate changes who waits for a person, and it makes no new Jev call.

**Stop:** Stop if the comparison calls Jev again, or if high confidence is treated as stock release or flight acceptance.

### 3. Change priorities without asking Jev again

![Saved scores for urgency, mission impact, and handoff risk. Two weight sets produce two attention orders. Neither calls Jev again.](figures/m06-scoring.png)

*Saved scores for urgency, mission impact, and handoff risk. Two weight sets produce two attention orders. Neither calls Jev again.*


```text
Using the TypeSafe skill, score the Blue Gauge messages for urgency, stated mission impact, and handoff risk. Combine those scores with weights. Then change the weights and show the new order from the saved scores, without another Jev call. This is desk attention, not cargo allocation.
```

**Expected:** You can see each score's contribution. The new weights change the order, or you can see why a message did not move. No new Jev call.

**Stop:** Stop if a high rank is treated as authority to load or dispatch.

### 4. Use the right kind of help

![Jev classifies the request. A lookup reads a record, a comparison checks the BG-F17 record, and a draft or approval comes to a person. None of those paths clears cargo.](figures/m06-intent.png)

*Jev classifies the request. A lookup reads a record, a comparison checks the BG-F17 record, and a draft or approval comes to a person. None of those paths clears cargo.*


```text
Using the TypeSafe skill, classify every request in shared/case/requests with Jev. Route a status lookup to a record lookup, a record question to a comparison of the supplied stock and flight records, and a draft, approval, or uncertain request to me. Show what actually ran. Nothing you run releases cargo or accepts it for BG-F17.
```

**Expected:** Each request has a typed intent and a path you can inspect. An approval comes to you. A lookup or comparison cites `scans.json` or `flight_acceptances.json`.

**Stop:** Stop if an approval is handled without you, or if a result is called clearance.

## Hand off

```text
Using the TypeSafe skill, write the airlift-desk handoff. Four rows: pattern, what I changed, what I observed, and the limit. Name one message or request I inspected for each pattern, with its source. List what a person still has to decide, and who owns it. Label it "review packet — not a manifest or movement order".
```

**Expected:** Every row names a real message or request from this session. No row claims cargo clearance, flight acceptance, or dispatch.
