# Module 2 · Build and control a reusable second brain

You'll have OMP draft a few knowledge notes from forty fictional paperwork notes. You'll turn those drafts into linked notes in Obsidian, accept the ones whose quotations check out, and freeze them. Then a fresh OMP session answers three questions from only those notes, and its run records show that it loaded your saved rule and read nothing else. Last, you'll fix one gap that session found and run it again.

This is an ungraded exercise with fictional Ledger Pike paperwork. Your result is for class use only. It doesn't authorize a release, vehicle assignment, permit approval, or real movement.

## The route

Plan for about three hours (a rough estimate). Most of that time goes into Obsidian, turning drafts into linked notes and accepting them. The three paid OMP runs take one to two minutes each.

Your work moves from the original sources, to OMP's drafts, to the notes you accept, to a frozen copy, to a fresh session that can read only that copy, and then to one fix.

![Build, freeze, retrieve, improve: sources lead to proposals, human review and admission to Knowledge, a frozen snapshot, a cold run from the snapshot only, and repair of one weakness.](figures/m02-reload.png)
*Build, freeze, retrieve, improve.*

<details markdown="1">
<summary>Figure text</summary>

Five steps, in order. 1. Sources: the model reads the paperwork and suggests Draft notes. 2. Review: you check each suggestion and accept supported notes into Knowledge. 3. Freeze: your index and the notes you accepted are copied to a fixed snapshot. 4. Cold run: a new chat answers using only that snapshot. 5. Repair: fix one weakness that matters, review it, and save a new snapshot. A thin arrow from Repair back to Freeze says you repeat this for each later revision.

</details>

## 1. Prepare and open your vault

This step makes a fresh work folder and opens its vault in Obsidian. A **vault** is the folder of Markdown notes that Obsidian opens. Use the Python, OMP, and Obsidian you verified in [Module 00](../../module-00-setup/README.md). On WSL, open the Linux-home vault with Linux Obsidian under WSLg.

The block sets four variables. `R` is your course checkout, `PY` is Python 3.12 or newer, `W` is this attempt's work folder, and `E` holds its run evidence. If your checkout isn't in Documents, change only the `R` line. Keep using the same terminal so the variables stay set.

**Terminal: Bash or zsh, ordinary user.**

```bash
R="$HOME/Documents/AIHB_OCT_2026"
PY="$(for candidate in python3.12 python3 python; do "$candidate" -c 'import sys; sys.exit(1) if sys.version_info < (3, 12) else print(sys.executable)' 2>/dev/null && break; done)"
RUN="$("$PY" -c 'import datetime, uuid; print(datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex)')"
W="$HOME/course-evidence/module02-$RUN/work"
E="$HOME/course-evidence/module02-$RUN/evidence"
printf '%s\n' "R=$R" "PY=$PY" "W=$W" "E=$E"
"$PY" "$R/shared/prepare_work.py" 02 "$W"
```

**Terminal: native PowerShell, ordinary user.**

```powershell
$R = "$HOME\Documents\AIHB_OCT_2026"
$PY = $null
foreach ($candidate in @("python3.12", "python3", "python")) {
    try {
        $executable = (Get-Command $candidate -CommandType Application -ErrorAction Stop).Source
        & $executable -c "import sys; exit(0 if sys.version_info >= (3,12) else 1)" *> $null
        if ($LASTEXITCODE -eq 0) { $PY = $executable; break }
    } catch {}
}
if (-not $PY) { throw 'No Python 3.12+ found; return to setup.' }
$RUN = (Get-Date).ToUniversalTime().ToString("yyyyMMddTHHmmssZ") + "-" + [guid]::NewGuid().ToString("N")
$W = "$HOME\course-evidence\module02-$RUN\work"
$E = "$HOME\course-evidence\module02-$RUN\evidence"
Write-Output "R=$R" "PY=$PY" "W=$W" "E=$E"
& $PY "$R/shared/prepare_work.py" 02 $W
if ($LASTEXITCODE -ne 0) { throw 'Preparation held; preserve the attempt and read the named condition.' }
```

**Expected:** The four variables print, and preparation reports a fresh work copy.

**Stop:** Python isn't found, a path is wrong, or preparation exits with a nonzero code.

**Recovery:** Fix the missing prerequisite with Module 00. If the destination already exists, keep it and run the block again for a new attempt. Don't merge attempts or copy files from an old vault.

Now build the vault once. This copies the forty source notes into `Sources` and adds empty folders, blank templates, and an empty index.

**Terminal: Bash or zsh, ordinary user, same window.**

```bash
"$PY" "$W/scripts/second_brain.py" initialize --work "$W"
```

**Terminal: native PowerShell, ordinary user, same window.**

```powershell
& $PY "$W/scripts/second_brain.py" initialize --work $W
if ($LASTEXITCODE -ne 0) { throw 'Initialization held; read the named file or condition.' }
```

**Expected:** `PASS: initialize`. `W/vault` has `Sources` with DN-001 through DN-040, empty `Drafts`, `Knowledge`, and `Reviews` folders, a `Templates` folder, and `MOC.md`.

**Stop:** `HOLD`, because the vault already exists, a source is missing, or a path is unsafe.

**Recovery:** Keep that attempt, fix the named problem, and start a fresh work copy with the first block.

### Open the vault in Obsidian

In Obsidian's vault chooser, click **Open** beside **Open folder as vault**, then select the printed `W` path followed by `vault`. Don't choose **Create**, and don't open the checkout or the `cold` folder. If another vault is already open, use **Manage vaults** from the vault-name menu at the bottom left to reach the chooser.

![Obsidian vault chooser with Open beside Open folder as vault, separate from Create and Sign in.](figures/m02-obsidian-01-open-vault.png)

Click **MOC** in the left file explorer. MOC is the index you'll fill once your notes exist, so it starts with only a title. Obsidian hides the `.md` extension.

![The initialized vault contains Drafts, Knowledge, Reviews, Sources, Templates, and an MOC with no links yet.](figures/m02-obsidian-02-initial-vault.png)

Expand **Sources** and open a DN note. You can also press **Ctrl+O** on Windows and Linux or **Command+O** on macOS and type its ID. The breadcrumb above the note shows its folder. Leave source text unchanged.

![DN-003 open in Obsidian Reading view, with the Sources folder in its breadcrumb and the original ticket text visible.](figures/m02-obsidian-05-open-source.png)

### Keep plugins restricted and Sync off

Your vault stays on your laptop. Click the **Settings** gear at the bottom left, then **Community plugins**. If the button says **Exit Restricted mode**, Restricted mode is already on, so leave it alone. If community plugins are enabled, click **Turn on Restricted mode**.

![Community plugins settings show Exit Restricted mode, indicating that Restricted mode is already active.](figures/m02-obsidian-03-restricted-mode.png)

Select **Core plugins**, find **Sync**, and turn it off if it's on. Don't sign in or connect a remote vault. Close Settings.

![Obsidian Core plugins settings with the Sync toggle off.](figures/m02-obsidian-04-sync-off.png)

| Location | What belongs there | Who changes it |
|---|---|---|
| `vault/Sources` | Original DN evidence | Keep unchanged |
| `vault/Drafts` | Model suggestions | Keep them; fix the notes in Knowledge |
| `vault/Knowledge` | Notes you prepare and admit | You, in Obsidian |
| `vault/Reviews` | A short reason for each decision | You, in Obsidian |
| `vault/Templates` | Blank starting structures | Copy into your new notes |
| `reviews`, `identities`, `source-manifest.json` | Run records and identity files outside the vault | Helper only |
| `cold/v1`, `cold/v2` | Frozen index and accepted notes | Helper only; keep unchanged |

## 2. Screen the sources and draft notes with OMP

Three controls stand between the paperwork and the model, and each does one job. The **file screen** checks one file for lines that look like orders. The **saved instruction** is a rule file the launcher loads into every session before it contacts the model; this one says to treat paperwork as data, never as orders. The **read root** is the only folder a session can read. You still decide which notes to accept.

![Saved instruction, file screen, read root, and human admission have separate jobs.](figures/m02-resolved-state.png)
*Saved instruction, file screen, read root, and human admission have separate jobs.*

<details markdown="1">
<summary>Figure text</summary>

Four limits side by side, not a sequence. Saved instruction: the launcher loads it before contacting the model. File screen: checks one file for lines that look like orders. Read root: the only folder the model can open. That folder is Sources while it drafts notes, and the frozen snapshot during the later check. Human admission: you decide which reviewed claims go into Knowledge.

</details>

Open `W/shared/controls/SAVED_INSTRUCTION.md` in a text viewer to see the rule every session will load. Don't edit it, and don't copy it into the vault.

### Run the file screen

The screen runs on your computer and doesn't call the model. Run it on a clean ticket, three notes with hostile instructions, and a file that doesn't exist.

**Terminal: Bash or zsh, ordinary user, same window.**

```bash
for note in DN-003 DN-014 DN-015 DN-016 DN-000; do
  "$PY" "$W/shared/case/guard.py" "$W/shared/case/$note.md"
  printf '%s exit=%s\n' "$note" "$?"
done
```

**Terminal: native PowerShell, ordinary user, same window.**

```powershell
foreach ($note in @("DN-003", "DN-014", "DN-015", "DN-016", "DN-000")) {
    & $PY "$W/shared/case/guard.py" "$W/shared/case/$note.md"
    $screenExit = $LASTEXITCODE
    Write-Output "$note exit=$screenExit"
}
```

**Expected:** DN-003 prints `PASS source-as-data` and `exit=0`. DN-014, DN-015, and DN-016 print `HOLD hostile-instruction` and `exit=1`. DN-000 prints `HOLD: missing input` and `exit=1`.

**Stop:** Any other result.

**Recovery:** Check the paths and that `guard.py` is unchanged. Don't create DN-000 or edit the screen to make it pass.

A pass doesn't make a source true, and a flag doesn't make the useful facts in that file false. The screen also can't see text you paste into a chat, which is one reason the saved rule matters.

### Have OMP draft notes

This is the first paid run. The helper starts one read-only OMP session that loads your saved rule, reads all forty sources, and proposes a few notes for three questions. The questions and the rest of the request are in `W/shared/controls/INGEST_PROMPT.md`. The session can't write files; the helper saves the valid proposals as Drafts.

**Terminal: Bash or zsh, ordinary user, same window.**

```bash
"$PY" "$W/scripts/second_brain.py" ingest --work "$W" --runner "$R/shared/run_omp.py" --evidence "$E/ingest"
```

**Terminal: native PowerShell, ordinary user, same window.**

```powershell
& $PY "$W/scripts/second_brain.py" ingest --work $W --runner "$R/shared/run_omp.py" --evidence "$E/ingest"
$ingestExit = $LASTEXITCODE
Write-Output "ingest exit=$ingestExit"
```

**Expected:** `PASS: all checks passed` from the launcher, then `Observed calls:` with forty `EXECUTED` entries, one for each source the session read, and the command exits with 0. Before it saves anything, the helper checks that your saved rule loaded, that the run was read-only, and that all forty sources were actually read. New files appear under **Drafts** in Obsidian. `W/reviews/ingest-report.json` lists the saved drafts and any proposal it rejected, with the reason.

**Stop:** A `HOLD`. Work out which kind before you continue:

- Exit 2 and no `E/ingest` folder: a setup problem, such as a missing key. Fix it and run the same command again.
- A run-check `HOLD` after the run: keep the terminal output and `E/ingest`. Don't continue because the answer looks fine.
- `HOLD: proposal HOLD:` naming a proposal and the problem, such as `invented or ambiguous excerpt`: keep the valid Drafts. `ingest-report.json` records the others, and you'll write those notes yourself in step 3.
- No Drafts at all because the response couldn't be read: write your notes from the blank template in step 3.

**Recovery:** A finished ingest uses up this attempt, even when it holds. Another ingest needs a fresh `W` and `E`. The helper never retries a paid run by itself.

Expand **Drafts** and open one. Its breadcrumb should start with **Drafts**. The screenshots in this lab use example notes, so your drafts will have different IDs and wording. Work with the drafts you got.

![A partial paper-ticket editing example open under Drafts, with Claim, Limits and conflicts, Evidence, and Related sections.](figures/m02-obsidian-11-inspect-draft.png)

## 3. Turn Drafts into linked Knowledge notes

Each note you keep moves from `Drafts` into `Knowledge`, where it becomes yours; the draft stays as OMP's record. A Knowledge note has a title and four sections: `## Claim`, `## Limits and conflicts`, `## Evidence`, and `## Related`. In step 4, the review command checks every quotation against its source file, so this step is about copying text exactly.

### Create a Knowledge note

Open the command palette with **Ctrl+P** on Windows and Linux or **Command+P** on macOS. Choose **Create new note**, then click the note's title and name it after the draft, such as `KB-001`. Open the command palette again, choose **Move current file to another folder**, and pick **Knowledge**. The breadcrumb should read **Knowledge / KB-001**. Use the same create-and-move steps for every new note.

![Obsidian command palette filtered to Create new note.](figures/m02-obsidian-08-new-review-note.png)

Before you copy, switch the draft to Source mode, so Markdown characters come along with the words. Open the command palette, search `source`, and choose **Toggle Live Preview/Source mode** if markers such as `#`, `**`, and `[[...]]` are hidden.

![The Obsidian command palette offers Toggle Live Preview/Source mode while a source note is open.](figures/m02-obsidian-06-source-mode-menu.png)

Copy the draft's text into your Knowledge note. To write a note OMP didn't draft, pick an unused three-digit ID and copy the body of `Templates/NOTE_TEMPLATE.md` into the new note, not over the template.

![The unchanged note template contains a bare title marker and the four required section headings.](figures/m02-obsidian-12-note-template.png)

Replace the bare `#` on the first line with `# ` and a title. Keep exactly one of each section heading, in order. Keep each claim to what its quotations say, and cut any sentence that goes beyond them.

![A separate Knowledge note in Source mode retains the required headings while the original Draft remains in the file explorer.](figures/m02-obsidian-13-knowledge-source.png)

### Quote the sources exactly

Each Evidence item is a `###` heading with a source link, followed by the exact supporting quotation. Write the heading as `### [[Sources/DN-NNN]]` with the source's three digits. Open the source in Source mode, copy a passage that appears only once in that file, and put `> ` at the start of each copied line. Keep every character: underscores, emphasis markers, punctuation, and line breaks. If a source line already starts with `>`, keep it after the `> ` you add. The helper works out the passage's line numbers and fingerprint for you.

![The original DN-003 in Source mode exposes its heading and emphasis markers as well as the source wording.](figures/m02-obsidian-07-source-markdown.png)

To compare side by side, open the command palette, choose **Split right**, and open the source in the right pane. Edit only the Knowledge side.

![Obsidian split view shows the Knowledge quotation on the left and the unchanged original source Markdown on the right.](figures/m02-obsidian-14-compare-source.png)

### Link your notes

Fill every Knowledge note before you link them. Under `## Related`, turn a useful suggestion into `- [[Knowledge/KB-NNN|label]]`, where the label says how the two notes connect. Use the exact `Knowledge/` path, not the draft, and delete the suggestions you don't link.

![A Related entry uses the exact Knowledge/KB-002 path and a label explaining what that note clarifies.](figures/m02-obsidian-15-related-link.png)

Switch to Reading view with the book button at the top right, then click the link. It should open a populated note whose breadcrumb starts with **Knowledge**. If a blank note opens, the path is wrong: delete the blank note and fix the link.

![In Reading view, the Related section displays the relationship label as a link rather than Markdown syntax.](figures/m02-obsidian-16-readable-link.png)

![Following the relationship opens the populated Knowledge/KB-002 note, with a link back to the arrival note.](figures/m02-obsidian-17-follow-knowledge-link.png)

### Build the index

In Source mode, start `MOC.md` with `# ` and a title, then add one line for each Knowledge note: `- [[Knowledge/KB-NNN|label]]`. Don't add any other text. Switch MOC to Reading view and click every entry to check that it opens a populated note. Use the back arrow above the note to return to MOC.

![MOC in Source mode has one title and one plain bullet containing a Knowledge link on each subsequent nonblank line.](figures/m02-obsidian-18-moc-source.png)

![MOC in Reading view exposes two navigation links to the partial paper-ticket editing examples.](figures/m02-obsidian-19-moc-links.png)

## 4. Accept your notes

Accepting a note saves a receipt that matches the note's exact bytes. Finish all note and link edits first, because a later edit, even to a link, needs a new receipt.

For each note, write a short reason. Copy the body of `Templates/REVIEW_TEMPLATE.md` into a new note, name it after the note and revision, such as `KB-001-v1`, and move it to **Reviews**. Fill **Note** with the exact path, such as `Knowledge/KB-001.md`, and **Decision** with `admit`. For **Decisive reason**, write what you checked, for example: "Quotations match DN-003 and DN-021; both links open populated notes." Leave a field blank if it doesn't apply.

![Move current file to another folder offers Reviews as the destination for a new note.](figures/m02-obsidian-08b-move-to-reviews.png)

![The blank review template separates the note, decision, decisive reason, competing source, and remaining limit.](figures/m02-obsidian-20-review-template.png)

![An admission reason under Reviews names Knowledge/KB-001.md and states a bounded reason and remaining limit.](figures/m02-obsidian-21-admission-reason.png)

Then record your decision. Change the note and reason names to yours.

**Terminal: Bash or zsh, ordinary user, same window.**

```bash
"$PY" "$W/scripts/second_brain.py" review --work "$W" --note "$W/vault/Knowledge/KB-001.md" --decision admit --reason-file "$W/vault/Reviews/KB-001-v1.md"
```

**Terminal: native PowerShell, ordinary user, same window.**

```powershell
& $PY "$W/scripts/second_brain.py" review --work $W --note "$W/vault/Knowledge/KB-001.md" --decision admit --reason-file "$W/vault/Reviews/KB-001-v1.md"
if ($LASTEXITCODE -ne 0) { throw 'Admission held; correct the named note or reason before continuing.' }
```

**Expected:** `PASS: review`. The receipt is saved outside the vault and doesn't change later.

**Stop:** A `HOLD` naming a quotation that doesn't match its source, a link to a missing note, a missing section, or an empty reason.

**Recovery:** Fix the named problem in Obsidian, then run the same command again.

To reject a draft instead, write a reason the same way and point the command at the draft. Run this only for a draft that exists.

![A separate, unfilled rejection reason names a Draft path rather than a Knowledge path; fill it only for a rejection you actually decide.](figures/m02-obsidian-22-rejection-reason.png)

**Terminal: Bash or zsh, ordinary user, same window.**

```bash
"$PY" "$W/scripts/second_brain.py" review --work "$W" --note "$W/vault/Drafts/KB-002.md" --decision reject --reason-file "$W/vault/Reviews/KB-002-reject.md"
```

**Terminal: native PowerShell, ordinary user, same window.**

```powershell
& $PY "$W/scripts/second_brain.py" review --work $W --note "$W/vault/Drafts/KB-002.md" --decision reject --reason-file "$W/vault/Reviews/KB-002-reject.md"
if ($LASTEXITCODE -ne 0) { throw 'Rejection record held; inspect the named path or reason.' }
```

**Expected:** `PASS: review`. A rejection copies nothing into Knowledge.

**Stop:** A `HOLD` naming the draft path or the reason file.

**Recovery:** Correct the path or reason and run the command again. A proposal that never became a draft is already recorded in `ingest-report.json`, so there's nothing to reject.

## 5. Freeze v1 and ask a fresh session

Freezing copies `MOC.md` and your accepted Knowledge notes into `cold/v1`, a fixed snapshot. The fresh session will read only that folder. Keep Obsidian on the editable vault, and don't open `cold` as a vault.

**Terminal: Bash or zsh, ordinary user, same window.**

```bash
"$PY" "$W/scripts/second_brain.py" freeze --work "$W" --revision v1
```

**Terminal: native PowerShell, ordinary user, same window.**

```powershell
& $PY "$W/scripts/second_brain.py" freeze --work $W --revision v1
if ($LASTEXITCODE -ne 0) { throw 'Freeze held; resolve the named admission, link, or content condition.' }
```

**Expected:** `PASS: freeze`, a new `cold/v1` folder, and `identities/v1.json`.

**Stop:** A `HOLD` listing notes without a receipt for their current bytes, a Knowledge note missing from MOC, or an empty note.

**Recovery:** For a missing receipt, the `HOLD` prints a ready review command for each note. Write the reason file it names, run the command for your shell, then freeze again.

Now ask a fresh session. This is the second paid run. The helper starts a new OMP process with the same saved rule and the three questions in `W/shared/controls/RETRIEVE_PROMPT.md`, and lets it read only `cold/v1`.

**Terminal: Bash or zsh, ordinary user, same window.**

```bash
"$PY" "$W/scripts/second_brain.py" retrieve --work "$W" --revision v1 --runner "$R/shared/run_omp.py" --evidence "$E/cold-v1"
```

**Terminal: native PowerShell, ordinary user, same window.**

```powershell
& $PY "$W/scripts/second_brain.py" retrieve --work $W --revision v1 --runner "$R/shared/run_omp.py" --evidence "$E/cold-v1"
if ($LASTEXITCODE -ne 0) { throw 'Cold run held; preserve its evidence and read the named condition.' }
```

**Expected:** `PASS: all checks passed`, then `Observed calls:` and `Raw-source access:` lines, then each question with its status, `supported` or `unsupported`, its answer, and the Knowledge notes and source passages it cited. The command exits with 0. The helper has already checked that your rule loaded before the model was contacted, that the session read only `cold/v1`, and that it read every note it cited.

**Stop:** A `HOLD`. A broken response, a citation the session didn't read, a changed snapshot, or a failed run check is a real failure.

**Recovery:** Keep `E/cold-v1`, fix the named condition, and run again with a new evidence folder name, such as `cold-v1b`. An `unsupported` answer isn't a failure. It means your notes don't cover that question yet, and you'll fix that in step 6.

### See the proof in the run records

Open `E/cold-v1` in a text editor and find these three things. You don't need to copy them anywhere.

- In `guard.jsonl`, an `instruction_loaded` line comes before the first `provider_request` line, so your rule loaded before the model saw anything.
- In `policy.json`, `work_root` ends in `cold/v1`, and `tools` lists only `course_read`.
- In `guard.jsonl`, the `execution_check` lines name `MOC.md` and the Knowledge notes the session read.

`Raw-source access:` in the terminal reports whether the session tried to open the original paperwork. `NOT_ATTEMPTED` means it never tried, `DENIED` means it tried and was refused, and `ALLOWED_ABSENT` means the path was allowed but missing, so nothing was read.

Then check one answer yourself. Open a cited Knowledge note in Reading view and click its **Sources/DN-NNN** link. The original opens under **Sources**, and you can confirm that the quotation says what the answer claims.

![Following a source citation opens the original DN-003 under Sources for the human check.](figures/m02-obsidian-24-follow-original-source.png)

## 6. Fix one gap the fresh session found

Pick one answer from the v1 run to improve: an `unsupported` answer, or one that leaves out part of what its question asks. The note you change or add for it is your **focal note**. If every answer is already supported and complete, add a second quotation or a new note that backs up one answer, so the next run can cite it.

Edit the focal note in Obsidian, or write a new note with an unused ID and add it to MOC. Keep earlier Knowledge notes: fix a wrong claim rather than deleting the note.

![The editable Knowledge note now states the additional movement-order limit while its original source quotation remains intact.](figures/m02-obsidian-27-edit-focal-note.png)

Every changed or new note needs a new receipt. Keep the old reason and write a new one, such as `Reviews/KB-001-v2.md`, saying what changed and which quotation supports it.

![Reviews contains distinct v1 and v2 reason notes; the open v2 reason explains the changed qualification.](figures/m02-obsidian-28-new-admission-reason.png)

Set `FOCUS` to your focal note's ID, and record the decision:

**Terminal: Bash or zsh, ordinary user, same window.**

```bash
FOCUS="KB-001"
"$PY" "$W/scripts/second_brain.py" review --work "$W" --note "$W/vault/Knowledge/$FOCUS.md" --decision admit --reason-file "$W/vault/Reviews/$FOCUS-v2.md"
```

**Terminal: native PowerShell, ordinary user, same window.**

```powershell
$FOCUS = "KB-001"
& $PY "$W/scripts/second_brain.py" review --work $W --note "$W/vault/Knowledge/$FOCUS.md" --decision admit --reason-file "$W/vault/Reviews/$FOCUS-v2.md"
if ($LASTEXITCODE -ne 0) { throw 'Revised admission held; inspect the named condition.' }
```

**Expected:** `PASS: review`.

**Stop:** A `HOLD` naming a quotation, a link, or the reason file.

**Recovery:** Fix it in Obsidian and run the command again. Review any other note you changed, such as one whose links you updated, the same way.

Freeze v2. The helper compares it with v1 and requires your focal note to be new or changed.

**Terminal: Bash or zsh, ordinary user, same window.**

```bash
"$PY" "$W/scripts/second_brain.py" freeze --work "$W" --revision v2 --previous "$W/identities/v1.json" --focus-note "$FOCUS"
```

**Terminal: native PowerShell, ordinary user, same window.**

```powershell
& $PY "$W/scripts/second_brain.py" freeze --work $W --revision v2 --previous "$W/identities/v1.json" --focus-note $FOCUS
if ($LASTEXITCODE -ne 0) { throw 'Revision freeze held; inspect changed notes and their admission receipts.' }
```

**Expected:** `PASS: freeze` and a new `cold/v2`. v1 stays as it was.

**Stop:** A `HOLD` naming a note without a current receipt, a deleted Knowledge note, or a focal note that didn't change.

**Recovery:** Make the named correction, review the note again, and freeze v2 again. Don't edit v1.

## 7. Prove the saved rule is required, then rerun

A run without your saved rule must stop before it contacts the model. This block hides the rule by renaming it, tries a v2 run, checks that it stopped with exit 2 and created no evidence, and then puts the rule back unchanged. It doesn't call the model.

**Terminal: Bash or zsh, ordinary user, same window.**

```bash
(
  rule="$W/shared/controls/SAVED_INSTRUCTION.md"
  held="$W/shared/controls/SAVED_INSTRUCTION.md.held"
  negative="$E/cold-v2-missing-rule"
  if [ ! -f "$rule" ] || [ -e "$held" ] || [ -L "$held" ] || [ -e "$negative" ] || [ -L "$negative" ]; then
    printf '%s\n' 'HOLD: missing rule or existing negative/held path; preserve it and inspect.'
    exit 1
  fi
  mv "$rule" "$held" || exit 1
  trap 'mv "$held" "$rule"' EXIT
  "$PY" "$W/scripts/second_brain.py" retrieve --work "$W" --revision v2 --runner "$R/shared/run_omp.py" --evidence "$negative"
  negative_exit=$?
  if [ "$negative_exit" -ne 2 ] || [ -e "$negative" ] || [ -L "$negative" ]; then
    printf '%s\n' 'HOLD: expected exit 2 and no evidence directory; stop and preserve observations.'
    exit 1
  fi
  printf '%s\n' 'Missing-rule prerequisite stopped with exit 2; no evidence directory created.'
)
```

**Terminal: native PowerShell, ordinary user, same window.**

```powershell
$rule = "$W/shared/controls/SAVED_INSTRUCTION.md"
$held = "$W/shared/controls/SAVED_INSTRUCTION.md.held"
$negative = "$E/cold-v2-missing-rule"
if (-not (Test-Path -LiteralPath $rule -PathType Leaf) -or (Test-Path -LiteralPath $held) -or (Test-Path -LiteralPath $negative)) {
    throw 'Missing rule or existing negative/held path; preserve it and inspect.'
}
Move-Item -LiteralPath $rule -Destination $held -ErrorAction Stop
try {
    & $PY "$W/scripts/second_brain.py" retrieve --work $W --revision v2 --runner "$R/shared/run_omp.py" --evidence $negative
    $negativeExit = $LASTEXITCODE
    if ($negativeExit -ne 2 -or (Test-Path -LiteralPath $negative)) {
        throw 'Expected exit 2 and no evidence directory; stop and preserve observations.'
    }
    Write-Output 'Missing-rule prerequisite stopped with exit 2; no evidence directory created.'
} finally {
    Move-Item -LiteralPath $held -Destination $rule -ErrorAction Stop
}
```

**Expected:** `HOLD: missing saved instruction:` with the rule's path, then `Missing-rule prerequisite stopped with exit 2; no evidence directory created.`, and `SAVED_INSTRUCTION.md` is back under its own name.

**Stop:** Any other exit code, a new `E/cold-v2-missing-rule` folder, or a rule file still named `SAVED_INSTRUCTION.md.held`.

**Recovery:** Keep the evidence. If the block was interrupted, rename `SAVED_INSTRUCTION.md.held` back to `SAVED_INSTRUCTION.md` without overwriting another file. Don't edit the rule or substitute another one.

With the rule back, ask a fresh session about v2. This is the third paid run, and it also shows the restored rule works.

**Terminal: Bash or zsh, ordinary user, same window.**

```bash
"$PY" "$W/scripts/second_brain.py" retrieve --work "$W" --revision v2 --runner "$R/shared/run_omp.py" --evidence "$E/cold-v2"
```

**Terminal: native PowerShell, ordinary user, same window.**

```powershell
& $PY "$W/scripts/second_brain.py" retrieve --work $W --revision v2 --runner "$R/shared/run_omp.py" --evidence "$E/cold-v2"
if ($LASTEXITCODE -ne 0) { throw 'Restored cold run held; keep its evidence and inspect the failure.' }
```

**Expected:** The same kind of output as for v1, with your focal note among the citations, and exit 0. The helper requires the focal note to be read and cited.

**Stop:** A `HOLD`.

**Recovery:** Keep `E/cold-v2`, fix the named condition, and run again with a new evidence folder name.

Compare the v2 answer with the v1 answer for the question you fixed. Each run's raw response is also saved as `response.md` in its evidence folder. If the gap is still there, fix the note again and repeat steps 6 and 7 as `v3`, freezing with `--previous "$W/identities/v2.json"` and using a new evidence folder.

### Check your snapshots

Your later edits to the vault mustn't change the frozen copies. These checks run on your computer and don't call the model.

**Terminal: Bash or zsh, ordinary user, same window.**

```bash
"$PY" "$W/scripts/second_brain.py" check --work "$W" --revision v1
"$PY" "$W/scripts/second_brain.py" check --work "$W" --revision v2
```

**Terminal: native PowerShell, ordinary user, same window.**

```powershell
& $PY "$W/scripts/second_brain.py" check --work $W --revision v1
if ($LASTEXITCODE -ne 0) { throw 'v1 identity held; preserve and inspect the named path.' }
& $PY "$W/scripts/second_brain.py" check --work $W --revision v2
if ($LASTEXITCODE -ne 0) { throw 'v2 identity held; preserve and inspect the named path.' }
```

**Expected:** `PASS: check` twice.

**Stop:** A `HOLD` naming a frozen file that changed, appeared, or disappeared.

**Recovery:** Keep that snapshot as it is and report what the check names. Don't rewrite its identity record to make the check pass. A matching fingerprint shows the bytes didn't change; it doesn't show the notes are true.

Keep your vault, both frozen copies, the receipts, and the run evidence. The frozen folders and receipts stay outside the vault.
