# Module 10 · Stand up a local uncensored AI and hand it off

Stand up the pinned uncensored model on your laptop as a loopback-only service. Prove one live interaction, stop and restore the service, then hand the kit to a colleague who can run it without you. OMP drafts the launch line and the bring-up steps and fills in package fields; you approve and run the server line, and the adapter scripts check the package's claims.

The model is `orcarouter/OrcaSAQ-2-Cyber-27B-Uncensored-GGUF`, a 15.7 GB uncensored build. Its identity does not guarantee an answer, refusal, warning, safety, or accuracy. You retain every consequential decision and operating boundary.

Plan for about three hours on Thursday (a rough estimate). Your recipient's attempt happens outside class hours. If no recipient is available, record independent-person operation as unobserved, not passed.

## Start here

Ask staff for the approved `hf` and `llama-server` executable paths, then [check local-model readiness](shared/MODULE_10_LAB.md#check-local-model-readiness-before-downloading) before downloading or launching. Keep existing installations. A preflight reports capacity and prerequisites without downloading or starting a service; each machine still needs a complete exact-model rehearsal.

1. [Stand the service up and transfer it](shared/MODULE_10_LAB.md) end to end.
2. Read the [service rules](shared/case/SERVICE_RULES.md) before the first launch.
3. Transfer the [runnable package](shared/PACKAGE.md) only after your own run is complete.

![Transfer only the declared, digest-checked files; the recipient downloads weights separately, and evidence and conversation history stay outside the kit.](shared/figures/m10-package-boundary.png)

*Transfer only the declared, digest-checked files; the recipient downloads weights separately, and evidence and conversation history stay outside the kit.*

<details markdown="1">
<summary>Figure text</summary>

The declared kit lists `shared/PACKAGE.md` (instructions), `scripts/` (adapters), `shared/case/` (case and rules), `shared/controls/` (active control), `shared/baseline/` (baseline). Freeze the declared paths, then make a digest-checked copy into a fresh received folder. Only those declared members travel. Not in the kit: model weights (recipient downloads them separately), run evidence including the stop receipt (kept separately), and conversation history.

</details>

## Bounded use

Bind the service only to `127.0.0.1`. Keep the weights on this laptop under your own account. Don't re-upload them, share the endpoint, or serve anyone else's traffic. The harness records prompts and replies in your evidence folder. Results are for class review only. This kit is a limited local service, not a deployment. Completing the run authorizes nothing beyond its evidence bundle.
