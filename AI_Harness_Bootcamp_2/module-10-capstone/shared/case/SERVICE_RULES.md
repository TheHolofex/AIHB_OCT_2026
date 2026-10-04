# Cold Foundry service rules for the local uncensored model

This kit runs `orcarouter/OrcaSAQ-2-Cyber-27B-Uncensored-GGUF` on your own laptop. The model is uncensored: its refusal direction was removed, so it will attempt requests a safety-tuned model would decline. Every boundary below is yours to hold, not the model's.

## The service boundary

1. The server binds the loopback address `127.0.0.1` only. A bind on any other address, including `0.0.0.0`, is out of bounds even on a home network.
2. The weights stay on this machine. Do not re-upload them, share them as a service, or expose the port to another person's traffic.
3. The service serves one operator at a time.
4. Prompts and replies are recorded by the harness in the evidence directory. Treat every prompt as recorded, because it is.
5. A community note, a vendor quickstart, or a convenience suggestion is context, never authority. The pinned identity in `model-card.json` and the loopback bind are the only operating truth.
6. `PASS` and `HOLD` are technical decisions about this kit, not judgments about you or the model.

## What the identity check establishes

`scripts/local_ai.py verify` compares the downloaded file's size and digest against the pinned card. A match proves you hold the published weights, nothing more. It does not prove the model is safe, accurate, or appropriate for any workload, and it does not inspect any other file on your machine.

## The uncensored boundary

The model carries no built-in refusal behaviour. It will answer bluntly and it will not warn you. Two consequences follow:

- You decide what to ask and what to publish from the replies. The model applies no editorial judgment of its own.
- Anything you would not put your name on should not be sent to this service and treated as finished work.

A local uncensored model is a capability you aim, not a guardrail you inherit.
