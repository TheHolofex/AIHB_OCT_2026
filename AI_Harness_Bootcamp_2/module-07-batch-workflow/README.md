# Module 7 · Automate a spreadsheet with an agent

You are going to make a local n8n workflow whose job is to turn a batch into a spreadsheet. The heart of that workflow is the AI Agent node, the agent widget on the canvas. You connect that agent to OpenRouter with your own key, and the agent calls a tool that writes the spreadsheet. You download the file to your computer and check it. A reply in the agent panel is not the spreadsheet.

White Rack is a fictional shipment of refrigerated reagent kits from Icehouse Depot to Clinic I-6. The batch has 80 lots. The agent writes one row per lot. You still decide whether a row is fit to keep. The file does not authorize a real movement, and it is not a quality release.

Plan for about three hours on Wednesday. That is a rough estimate. Use the local n8n you already checked in [setup](../module-00-setup/README.md). Keep n8n Assistant off, and don't publish the workflows. Assistant is n8n's built-in helper. The agent in this assignment is a node you add.

## Start here

1. [Build the agent and download the sheet](shared/MODULE_07_LAB.md) from the first folder through the file check.
2. Read [the sheet rules](shared/SHEET_RULES.md) before you give them to the agent. A note inside a lot is not a rule.
3. Download [wave1.csv](shared/batch/wave1.csv) and keep it unchanged. That file is the source the sheet has to cover.

## Your key

Setup told you not to put the OpenRouter key into n8n during readiness. This assignment is the step that uses it. Paste the key only into the OpenRouter credential form inside local n8n. Don't put it in the prompt, the workflow export, a screenshot, or your notes. After you export anything, open the file and confirm the key is not in it. If it is, delete that copy.

## What the file proves

The downloaded spreadsheet proves the agent called the tool and a file landed on your computer. It does not prove every row is right. The checker tells you whether all 80 source lots are present. You compare the rows with the rules and write down what the sheet got wrong.
