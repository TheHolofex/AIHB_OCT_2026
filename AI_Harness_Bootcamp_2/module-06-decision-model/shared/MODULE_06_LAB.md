# Module 6 · Design a workflow for a decision model

Blue Gauge screens the handoff notes an assistant drafts each night for oxygen cylinders moving from East Yard to Clinic O-2. A note can claim more than the yard's scan record shows, carry an instruction to the desk, or name the wrong cylinder. Build the screen around a **decision model**: an AI model that returns typed answers with probabilities instead of prose. Choose and pin the model in Oh My Pi (OMP) through OpenRouter, write the questions it answers, set the thresholds that turn its probabilities into routes, and prove the frozen screen on notes you didn't tune it on.

Plan for about three hours (a rough estimate).

## Prepare the work folder and evidence

Use the checkout, Python, and OMP you verified in setup, and your OpenRouter key, which you enter in the terminal rather than save in a file. `W` is the work folder you edit. `E` holds evidence: the judge candidate list, one folder per judge run with that run's receipts, your notes, the freeze record, and the handoff. Both sit outside the checkout.

**Terminal: Bash or zsh, ordinary user.**

```bash
R="$HOME/Documents/AIHB_OCT_2026"
PY="$(for candidate in python3.12 python3 python; do "$candidate" -c 'import sys; sys.exit(1) if sys.version_info < (3, 12) else print(sys.executable)' 2>/dev/null && break; done)"
[ -n "$PY" ] || echo 'HOLD: Python 3.12 or newer is required.' >&2
RUN="$(date -u +%Y%m%dT%H%M%SZ)-$$"
mkdir -p "$HOME/course-evidence" && printf '%s\n' "$RUN" > "$HOME/course-evidence/module-06-run" && printf 'RUN=%s\n' "$RUN"
BASE="$HOME/course-evidence/module-06-$RUN"
W="$BASE/work"
E="$BASE/evidence"
"$PY" "$R/shared/prepare_work.py" 06 "$W" && mkdir "$E"
```

**Terminal: PowerShell, ordinary user.**

```powershell
$R = "$HOME\Documents\AIHB_OCT_2026"
$PY = $(foreach ($candidate in 'python3.12','python3','python') { try { $resolved = & $candidate -c 'import sys; sys.exit(1) if sys.version_info < (3,12) else print(sys.executable)' 2>$null; if ($LASTEXITCODE -eq 0 -and $resolved) { $resolved.Trim(); break } } catch {} })
if (-not $PY) { throw 'HOLD: Python 3.12 or newer is required.' }
$RUN = [guid]::NewGuid().ToString('N')
New-Item -ItemType Directory -Force -Path "$HOME\course-evidence" | Out-Null; Set-Content -LiteralPath "$HOME\course-evidence\module-06-run" -Value $RUN; "RUN=$RUN"
$BASE = "$HOME\course-evidence\module-06-$RUN"
$W = "$BASE\work"
$E = "$BASE\evidence"
& $PY "$R\shared\prepare_work.py" 06 "$W"
if ($LASTEXITCODE -eq 0) { New-Item -ItemType Directory -Path "$E" | Out-Null }
```

**Expected:** `RUN=` and this attempt's identifier (note it down), then `PASS: created` followed by the work path. Ignore the printed `Next` suggestion. The work folder holds `QUESTIONS.json`, `THRESHOLDS.json`, `SELECTION.md`, `scripts/blue_gauge.py`, `shared/case`, and `shared/controls`.

**Stop:** Python isn't found, preparation prints `HOLD`, or a path points inside the checkout.

**Recovery:** Fix the prerequisite the message names, then run the block again in a new terminal to get a new `RUN`. Never reset or clean the checkout to make preparation pass.

### If you open a new terminal

A closed terminal forgets these variables. In a new terminal, reload them for the same attempt instead of preparing another one.

**Terminal: Bash or zsh, ordinary user.**

```bash
R="$HOME/Documents/AIHB_OCT_2026"
PY="$(for candidate in python3.12 python3 python; do "$candidate" -c 'import sys; sys.exit(1) if sys.version_info < (3, 12) else print(sys.executable)' 2>/dev/null && break; done)"
[ -n "$PY" ] || echo 'HOLD: Python 3.12 or newer is required.' >&2
RUN="$(cat "$HOME/course-evidence/module-06-run")"
BASE="$HOME/course-evidence/module-06-$RUN"
W="$BASE/work"
E="$BASE/evidence"
printf '%s\n' "RUN=$RUN" "W=$W"
```

**Terminal: PowerShell, ordinary user.**

```powershell
$R = "$HOME\Documents\AIHB_OCT_2026"
$PY = $(foreach ($candidate in 'python3.12','python3','python') { try { $resolved = & $candidate -c 'import sys; sys.exit(1) if sys.version_info < (3,12) else print(sys.executable)' 2>$null; if ($LASTEXITCODE -eq 0 -and $resolved) { $resolved.Trim(); break } } catch {} })
if (-not $PY) { throw 'HOLD: Python 3.12 or newer is required.' }
$RUN = (Get-Content -LiteralPath "$HOME\course-evidence\module-06-run" -Raw).Trim()
$BASE = "$HOME\course-evidence\module-06-$RUN"
$W = "$BASE\work"
$E = "$BASE\evidence"
"RUN=$RUN"; "W=$W"
```

**Expected:** `RUN=` followed by the identifier you noted, then `W=` followed by the existing work folder.

**Stop:** The identifier differs from the one you noted, or the folder after `W=` doesn't exist.

**Recovery:** A different identifier means a later attempt replaced the saved marker; set `RUN` by hand to the value you noted and run the block again. A missing folder means the attempt was never prepared; prepare it with the first block.

### Enter your key in this terminal

The launcher reads your OpenRouter key only from this terminal's environment. Paste the first command by itself and press Enter, type or paste the key at the prompt, which shows nothing, and press Enter again. Then paste the second block.

**Terminal: Bash or zsh, ordinary user.**

```bash
IFS= read -r -s OPENROUTER_API_KEY
```

**Terminal: PowerShell, ordinary user.**

```powershell
$secret = Read-Host 'OpenRouter key' -AsSecureString
```

**Expected:** The terminal waits silently for the key, then returns to its prompt without showing the value.

**Stop:** Characters appear as you type, or you're not sure which program is reading the input.

**Recovery:** Cancel with Ctrl+C and close that terminal. If the value was shown, revoke the key at OpenRouter and use a replacement.

**Terminal: Bash or zsh, ordinary user.**

```bash
export OPENROUTER_API_KEY
if [ -n "${OPENROUTER_API_KEY:-}" ]; then printf 'SET\n'; else printf 'MISSING\n'; fi
```

**Terminal: PowerShell, ordinary user.**

```powershell
$bstr = [IntPtr]::Zero
try {
  $bstr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secret)
  $env:OPENROUTER_API_KEY = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($bstr)
} finally {
  if ($bstr -ne [IntPtr]::Zero) { [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($bstr) }
  if ($secret) { $secret.Dispose() }
  Remove-Variable secret,bstr -ErrorAction SilentlyContinue
}
if ([string]::IsNullOrWhiteSpace($env:OPENROUTER_API_KEY)) { 'MISSING' } else { 'SET' }
```

**Expected:** `SET`. That proves the key is present in this terminal; it doesn't prove the key is valid or has credit.

**Stop:** `MISSING`, or any part of the key appears in the output.

**Recovery:** Repeat the hidden prompt in this terminal. Never print the environment to troubleshoot a key, and never save the key in a file or a shell profile.

## 1. Split the desk decision

Open `W/shared/case/DESK_RULES.md`. Then open `W/shared/case/scans.json` and two notes in `W/shared/case/notes/tuning`, such as `BG-002.json` and `BG-005.json`.

Each note is a small JSON file whose `state` holds only the note's text: the part a model reads. The scan record stays in `scans.json`, where code reads it.

Before you write a question, split the desk decision three ways:

| Part of the decision | Who answers it | Why |
|---|---|---|
| Does the note name exactly the cylinder on its scan record? Does it cite a release order the record doesn't hold? Is the status it gives above the scan status? | Code | A rule settles these exactly. A model adds nothing but error. |
| Does the note claim a release? Which status does it give? Does it tell the reader to do something? How urgent does it sound? | The decision model | These are readings of plain language that no rule settles. |
| Every note the screen can't settle, and every release | The duty officer and the Release Authority | The screen routes notes. It releases nothing. |

The supplied router already does the code part. Your work is the middle row: the questions, and the thresholds that turn their probabilities into routes.

## 2. List the judge models OMP can reach

A **chat model** writes prose for a person to read. A **decision model** answers fixed questions with typed values your code can act on: a yes probability, one option from a list with a probability for each option, or a position on a scale you define. It writes no explanation, can't answer outside the options you give it, and costs a small fraction of a chat model per item. OMP calls this kind of model its **judge** and lists the ones your OpenRouter key can reach.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$R/shared/run_omp.py" --list-judges --evidence "$E/judge-candidates"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$R\shared\run_omp.py" --list-judges --evidence "$E\judge-candidates"
```

**Expected:** A table of judge models with each one's context window and price per million input and output tokens, the row `openrouter/typesafe/jev-1.13` marked `<- course pin`, then `PASS: saved` with the number of candidates. The list comes live from OpenRouter, so its rows and prices can change from day to day. Listing calls no model.

**Stop:** `HOLD`, or the pinned row is missing.

**Recovery:** A missing key means repeating the hidden key entry in this terminal. A version message means returning to setup. If the pinned row is missing, record `HOLD` for the live work and keep the saved list; don't choose another model.

Read three rows before you choose:

- `openrouter/typesafe/jev-1.13` is TypeSafe's Jev at one fixed version.
- `openrouter/~typesafe/jev-latest` is an alias. It follows TypeSafe's newest release, so the model behind it can change between your tuning run and your held-out run.
- `openrouter/typesafe/jev-router` doesn't answer your questions. OpenRouter uses Jev inside it to choose a chat model for each request.

Open the model's page, [openrouter.ai/typesafe/jev-1.13](https://openrouter.ai/typesafe/jev-1.13), and TypeSafe's list of its known weak spots, [Jev 1.13 jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13). Note the context window, what you pay for (input tokens; output is free), the data policy, and the weak spots you'll design around: literal reading, counting and date comparison, long input full of unrelated detail, text written to steer the answer, and a lean toward the first option in a list.

## 3. Record the selection and set the judge

Open `W/SELECTION.md` in your text editor and answer each heading in a few sentences of your own: the decision point, why a decision model and not the chat model, the candidate you chose and why you passed over the alias and the router, three weak spots and the part of the screen that answers each, and the data boundary. When the screen runs, each note's text goes to OpenRouter and on to TypeSafe, billed to the account behind your key. No separate TypeSafe account is involved. Name the kind of data you wouldn't send.

Then point OMP's judge at the pinned model. `modelRoles.judge` is the OMP setting that names the model answering judge calls; two lines hold it.

**Terminal: Bash or zsh, ordinary user.**

```bash
printf 'modelRoles:\n  judge: openrouter/typesafe/jev-1.13\n' > "$W/JUDGE.yml" && cat "$W/JUDGE.yml"
```

**Terminal: PowerShell, ordinary user.**

```powershell
$utf8 = New-Object System.Text.UTF8Encoding $false
[IO.File]::WriteAllText("$W\JUDGE.yml", "modelRoles:`n  judge: openrouter/typesafe/jev-1.13`n", $utf8)
Get-Content -LiteralPath "$W\JUDGE.yml"
```

**Expected:** The two lines: `modelRoles:` and, indented below it, `judge: openrouter/typesafe/jev-1.13`.

**Stop:** Anything else appears.

**Recovery:** Run the block again; it replaces the file. The launcher accepts only these two lines with the pinned name, and it stops before any call if the file names the alias, the router, or a chat model.

## 4. Repair the question set

`W/QUESTIONS.json` holds a starter question set with the mistakes people make first. The router reads five answers by fixed ID: `claims_release` (yes/no), `note_status` and `note_status_reversed` (choice), `instructs_reader` (yes/no), and `urgency` (score). You already know how to write a typed question with a fixed answer set. A decision model rewards a few more rules:

| Rule | In this screen |
|---|---|
| Keep anything a rule can settle in code. | The cylinder ID, a cited order, the scan rank, and any time comparison never become questions. The model reads numbers and times as text. |
| Send only what the question needs. | The state is the note alone. A long state full of unrelated detail costs accuracy. |
| Ask one condition per question, worded so yes means the condition you act on. | "Is the note free of instructions?" makes yes mean safe; turn it around. "Is it released and ready to load?" asks two things at once. |
| Name the part of the state you mean, in backticks. | Write `` `note` `` in every question. |
| Say what counts and what doesn't. | Put boundary cases in `criteria`: a pending or negated release isn't a release; a caution such as "do not load until released" isn't an instruction. |
| Give every list a way out. | `note_status` needs `not_stated` for a note that gives no status. |
| Use a yes/no for one condition, a choice for one of a set, a score for degree. | Urgency has three levels, lowest first: routine, needed today, needed immediately. |
| Ask everything in one call. | Every question sees the same note and is answered independently and in parallel, so a question only some notes need costs almost nothing. Give any question the router doesn't read an ID that starts with `extra_`. |
| Ask the list twice, in opposite orders. | `note_status_reversed` repeats `note_status` with the same instructions and option descriptions in reverse order. An answer that changes with the order goes to a person. |

Option and level descriptions are text. A yes/no question may add `criteria` with `true` and `false` descriptions. The question ID is for your code; the model sees only `instructions` and `criteria`, so write the whole question there.

Check the file after each edit. The check reads the file and calls no model.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$W/scripts/blue_gauge.py" check-questions "$W/QUESTIONS.json"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$W\scripts\blue_gauge.py" check-questions "$W\QUESTIONS.json"
```

**Expected:** At first, a `HOLD` line for each problem in the starter set. After your repairs, one line per question with its type, then `PASS` with the number of questions.

**Stop:** A `HOLD` line won't go away, or `PASS` appears while a question still asks two things.

**Recovery:** Read the named question and the rule it breaks, edit the file, and check again. The check confirms the shape the router reads; it can't tell whether your words ask the right thing. The tuning run tells you that.

## 5. Run the tuning notes through the judge

OMP runs judge calls from its code tool inside a session. The launcher starts a session with the course chat model and allows exactly one call: a cell the launcher writes, which sends all twenty tuning notes and every question to Jev in one batch and saves each answer with the build that gave it. The guard refuses any other code. Afterward the launcher checks every answer against your question file, the build that answered, the cost, and the work folder.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$R/shared/run_omp.py" --workdir "$W" --evidence "$E/tuning-1" --judge-config "$W/JUDGE.yml" --judge-questions "$W/QUESTIONS.json" --judge-states "$W/shared/case/notes/tuning" --judge-output out/tuning-1
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$R\shared\run_omp.py" --workdir "$W" --evidence "$E\tuning-1" --judge-config "$W\JUDGE.yml" --judge-questions "$W\QUESTIONS.json" --judge-states "$W\shared\case\notes\tuning" --judge-output out/tuning-1
```

**Expected:** `JUDGE: 20 judged by` followed by a dated build such as `openrouter/typesafe/jev-1.13-20260917` and the cost in US dollars, then `PASS: complete guarded OMP turn`. The answers are in `W/out/tuning-1`; the receipts are in `E/tuning-1`.

**Stop:** The launcher prints `HOLD`, a judgment is missing, or a build other than `jev-1.13` answered.

**Recovery:** Keep the held folder. If the message names your question file or `JUDGE.yml`, fix that file and run again under a new name such as `tuning-1b`. A provider or credit failure holds the live work; don't switch models.

## 6. Read the misses before you change anything

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$W/scripts/blue_gauge.py" report --work "$W" --run tuning-1
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$W\scripts\blue_gauge.py" report --work "$W" --run tuning-1
```

**Expected:** One row per tuning note: the scan status, the release-claim probability, the status answer in both option orders with each one's confidence, the instruction probability, urgency, the route the current thresholds give with its reason, and the desk outcome. A `SUMMARY` line counts the errors that matter. `QUESTION MISSES` lists each note where an answer, read at 0.50, disagrees with the desk label, with the note's text.

**Stop:** The report holds because a judgment is missing.

**Recovery:** Return to step 5 and run the tuning notes under a new name. Don't edit saved judgments.

Create `E/first-misses.md` in your text editor. For each note under `QUESTION MISSES`, write one line: the note ID, what the answer got wrong, and the words in your question the model took literally. The model answers the question you wrote, not the one you meant. When you find yourself explaining what you meant, write that explanation into the question.

Write the notes before you change any question. They record what your first wording did.

## 7. Revise the wording and run the tuning notes again

If `QUESTION MISSES` said `none`, skip this step and use `tuning-1` as your tuning run from here on.

Change only the questions your notes point to. Usually the fix is a boundary case added to `criteria`, or a vague word replaced by the exact condition. Then check the file, run the tuning notes as `tuning-2`, and read the report.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$W/scripts/blue_gauge.py" check-questions "$W/QUESTIONS.json" &&
"$PY" "$R/shared/run_omp.py" --workdir "$W" --evidence "$E/tuning-2" --judge-config "$W/JUDGE.yml" --judge-questions "$W/QUESTIONS.json" --judge-states "$W/shared/case/notes/tuning" --judge-output out/tuning-2 &&
"$PY" "$W/scripts/blue_gauge.py" report --work "$W" --run tuning-2
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$W\scripts\blue_gauge.py" check-questions "$W\QUESTIONS.json"
if ($LASTEXITCODE -eq 0) { & $PY "$R\shared\run_omp.py" --workdir "$W" --evidence "$E\tuning-2" --judge-config "$W\JUDGE.yml" --judge-questions "$W\QUESTIONS.json" --judge-states "$W\shared\case\notes\tuning" --judge-output out/tuning-2 }
if ($LASTEXITCODE -eq 0) { & $PY "$W\scripts\blue_gauge.py" report --work "$W" --run tuning-2 }
```

**Expected:** `PASS` from the check, the launcher's `JUDGE` and `PASS` lines, then the report, with fewer notes under `QUESTION MISSES` than `tuning-1` had.

**Stop:** The same misses remain, or new misses appear on notes the first wording got right.

**Recovery:** Compare the two reports note by note, revise again, and run under the next name, `tuning-3`. Expect each run to cost a fraction of a cent for Jev and a few cents for the chat turn that carries the cell. Keep every run; the final check reads all of them.

## 8. Set thresholds from the tuning answers

Thresholds turn probabilities into routes. Set them from what the model did on your tuning notes, weighted by what each error costs the desk. A note that overstates and passes can put a received cylinder on the load list, and an instruction no one reads can authorize a load. A wrong return costs one redraft. A review costs the duty officer about two minutes.

See each signal laid out against the desk labels. Use the name of your last tuning run.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$W/scripts/blue_gauge.py" spread --work "$W" --run tuning-2
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$W\scripts\blue_gauge.py" spread --work "$W" --run tuning-2
```

**Expected:** Three blocks. `INSTRUCTION` lists the instruction probability for each note the desk says carries an instruction, lowest first, beside the highest values among notes without one. `RELEASE CLAIM` does the same for release claims on the notes code leaves open. `STATUS` lists the lower confidence of the two option orders.

**Stop:** The command holds.

**Recovery:** Name a tuning run with `--run`. Thresholds come from tuning notes only; the held-out notes wait for the final measurement.

Open `W/THRESHOLDS.json` and set four values from 0 to 1:

| Threshold | What it does | Where to set it |
|---|---|---|
| `instruction_review` | An instruction probability at or above it sends the note to a person. | Below the lowest value among notes that carry an instruction, with room to spare. |
| `return_at` | A release-claim probability at or above it returns the note, unless the scan record holds a release order. | Above the highest value among notes that make no claim, or accept the wrong returns it causes. |
| `pass_below` | A release-claim probability at or below it can pass. A value between `pass_below` and `return_at` goes to a person. | Below the lowest value among notes that claim a release, with room to spare. |
| `status_confidence` | A status answer whose confidence falls below it, in either option order, goes to a person instead of passing. | Below the confidence of the status answers that match the desk, so only the doubtful ones go to review. |

A second run of the same notes can move a probability by a few hundredths. A threshold that sits right beside a tuning value can send that note the other way next time, so put each one in a gap.

Then route the tuning notes with your values. Rerun the report as often as you like; it reads the saved answers and calls no model.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$W/scripts/blue_gauge.py" report --work "$W" --run tuning-2
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$W\scripts\blue_gauge.py" report --work "$W" --run tuning-2
```

**Expected:** A `SUMMARY` line with no missed overstatement, no instruction left unreviewed, no note about another cylinder left unreviewed, and a review share the duty officer can staff.

**Stop:** An error that matters remains at every setting you try.

**Recovery:** Fix the question whose probabilities overlap between the two groups, then run the tuning notes again as in step 7. A threshold can't separate answers the question doesn't separate.

## 9. Freeze, then judge the held-out notes once

Choose a **review ceiling** first: the largest share of notes you'll accept sending to the duty officer. Then freeze the questions, the thresholds, the build that answered your tuning run, and the ceiling. The freeze is written once; the held-out run and its measurement are checked against it. Replace `tuning-2` with your last tuning run and `0.4` with your ceiling.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$W/scripts/blue_gauge.py" freeze --work "$W" --evidence "$E" --tuning-run tuning-2 --review-ceiling 0.4
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$W\scripts\blue_gauge.py" freeze --work "$W" --evidence "$E" --tuning-run tuning-2 --review-ceiling 0.4
```

**Expected:** `PASS: froze questions` with the first characters of each fingerprint, the build, and your ceiling.

**Stop:** The freeze refuses because the questions changed after the tuning run you named, or because `E/freeze.json` already exists.

**Recovery:** Name the tuning run that used your current questions, or run the tuning notes once more if none did. A freeze is recorded once; to start over, prepare a new attempt.

Judge the sixty held-out notes once, then measure the frozen screen on them.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$R/shared/run_omp.py" --workdir "$W" --evidence "$E/held-out" --judge-config "$W/JUDGE.yml" --judge-questions "$W/QUESTIONS.json" --judge-states "$W/shared/case/notes/held-out" --judge-output out/held-out &&
"$PY" "$W/scripts/blue_gauge.py" measure --work "$W" --evidence "$E"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$R\shared\run_omp.py" --workdir "$W" --evidence "$E\held-out" --judge-config "$W\JUDGE.yml" --judge-questions "$W\QUESTIONS.json" --judge-states "$W\shared\case\notes\held-out" --judge-output out/held-out
if ($LASTEXITCODE -eq 0) { & $PY "$W\scripts\blue_gauge.py" measure --work "$W" --evidence "$E" }
```

**Expected:** The launcher's `JUDGE: 60 judged` and `PASS` lines, then `HELD-OUT 60 notes` with each error count and the review share, a `COST` line with the decision model's cost per 1,000 notes and the cost of the chat turn that carried the cell, and `DECISION:` followed by `ADOPT for bounded internal screening` or `HOLD` with the reasons.

**Stop:** The launcher holds, or `measure` refuses the run.

**Recovery:** A `HOLD` decision is a result; keep it and report it. Don't change a frozen file and judge the held-out notes again, which would turn them into tuning notes. If the launcher held before saving any judgment, rename `E/held-out` and `W/out/held-out` to `held-out-attempt-1`, then run the same block again.

## 10. Hand off and run the final check

Create `E/HANDOFF.md` with these headings, each followed by a few sentences of your own: `## What the screen decides`, `## Settings in force`, `## Held-out result`, `## Limits`, and `## Owner`. Name the pinned model and the build that answered, the frozen thresholds and ceiling, every held-out error count and the review share, the cost per 1,000 notes, what the result can't show, and who owns the review queue and every release.

Then run the final check. It rechecks every launcher receipt with the course auditor, compares your first-miss notes with the first tuning run, confirms that the freeze came before the held-out run, measures the saved held-out answers again, and reads your selection and handoff.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$W/scripts/blue_gauge.py" verify --work "$W" --evidence "$E" --launcher "$R/shared/run_omp.py"
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$W\scripts\blue_gauge.py" verify --work "$W" --evidence "$E" --launcher "$R\shared\run_omp.py"
```

**Expected:** A `PASS` line for each check, then a final `PASS` naming the held-out decision on record.

**Stop:** Any `HOLD` line.

**Recovery:** Each `HOLD` names the record and the reason. Correct the named file; don't edit saved judgments, receipts, or the freeze. A `PASS` means the records agree with one another; it can't judge whether your questions were wise.

## Use the judge in your own OMP sessions

The same two-line file works outside the launcher: start OMP with `omp --config JUDGE.yml`, and the session's judge calls go to the pinned model. Inside a session, ask the agent to judge a pile of items with your question file. It calls `judgeBatch` (`judge_batch` in Python) from OMP's code tool, and each batch reports the build that answered and the cost.

The design doesn't change outside class. Settle what code can settle. Ask narrow questions about only the part of the input they need. Set thresholds from labeled examples, weighted by what each error costs. Measure the frozen version on examples you didn't tune on, and pin the version you measured. When the model isn't sure, its probability says so: send that case to a person, or to a chat model that can explain it.

## Before you stop

Confirm that:

- your selection record names the pinned model and three weak spots, each matched to part of the screen;
- every tuning run is saved, and your first-miss notes name every note the first run missed;
- your thresholds came from tuning answers, and the freeze came before the held-out run;
- the held-out run used the frozen questions and the same build as your tuning run;
- your handoff reports the held-out errors, the review share, and the cost per 1,000 notes, and names who owns the review queue and every release.

The held-out result describes sixty practice notes judged by one build. It doesn't show how the screen does on real notes, how a later build will answer, or how well the probabilities hold beyond this sample. The screen routes notes; it releases nothing.

## Stretch: run the tuning notes a second time

<details class="rf-stretch" markdown="1">
<summary>Optional stretch: judge the tuning notes again and compare</summary>

The same notes, questions, and build can come back with slightly different probabilities on a second run, and a small shift near a threshold can change a route. Measure that on your own notes: judge the tuning notes again with your frozen questions as `tuning-3` (or the next unused name), then report it.

**Terminal: Bash or zsh, ordinary user.**

```bash
"$PY" "$R/shared/run_omp.py" --workdir "$W" --evidence "$E/tuning-3" --judge-config "$W/JUDGE.yml" --judge-questions "$W/QUESTIONS.json" --judge-states "$W/shared/case/notes/tuning" --judge-output out/tuning-3 &&
"$PY" "$W/scripts/blue_gauge.py" report --work "$W" --run tuning-3
```

**Terminal: PowerShell, ordinary user.**

```powershell
& $PY "$R\shared\run_omp.py" --workdir "$W" --evidence "$E\tuning-3" --judge-config "$W\JUDGE.yml" --judge-questions "$W\QUESTIONS.json" --judge-states "$W\shared\case\notes\tuning" --judge-output out/tuning-3
if ($LASTEXITCODE -eq 0) { & $PY "$W\scripts\blue_gauge.py" report --work "$W" --run tuning-3 }
```

**Expected:** The launcher's `PASS`, then a report you can set beside the report of your tuning run.

**Stop:** The launcher holds.

**Recovery:** Keep the held folder and run again under the next name.

List each note whose route changed and the largest change you see in any probability. Add both to your handoff under `## Limits`. A repeated answer isn't a correct one: a stable wrong answer is still wrong.

</details>

## Class-only boundary

All names, identifiers, records, and notes are fictional practice material. Don't use them to plan, authorize, or describe a real movement or handling decision. A module result is for class review only.
