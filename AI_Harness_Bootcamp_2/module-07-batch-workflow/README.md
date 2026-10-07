# Module 7 · Automate a spreadsheet with an agent

You already have local n8n. Build one workflow. It reads a batch, asks a model for one row per lot, and writes a spreadsheet. Download the file and check the rows. The text in the model node is not the file. Allow about three hours. [Open the lab](shared/MODULE_07_LAB.md).

## White Rack

White Rack carries refrigerated reagent kits from Icehouse Depot to Clinic I-6. The batch has 80 lots. The model writes one row per lot. The sheet does not authorize a movement, and it is not a quality release.

Read the [sheet rules](shared/SHEET_RULES.md) before you give them to the model. A note inside a lot is not a rule. Download [wave1.csv](shared/batch/wave1.csv) and keep it unchanged. Paste the OpenRouter key only into the credential form inside local n8n. Do not put it in the prompt, an export, a screenshot, or your notes.
