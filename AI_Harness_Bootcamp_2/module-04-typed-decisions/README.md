# Module 4 · Decide with typed questions

Turn a shift's messages into typed answers that software can route. Compare the answers with your own reading. Then give the desk lead a requirement line where every number rests on a message with authority. The model answers fixed questions; it cannot write prose, pick routes, or invent numbers.

Plan for about two and a half hours on Tuesday (a rough estimate).

## Start here

1. [Decide with typed questions](shared/MODULE_04_LAB.md): build the state, label a sample, run the model once, validate and measure its answers, set the gates, route the messages, and decide the queue.

Chalk Line is a fictional resupply of sterile surgical gloves from Ferry Depot to Clinic K-3 on vehicle `CL-9`. Forty messages reached the intake desk during one shift. They include requisitions, corrections, cancellations, resends, stock notes, a vendor's offer, a request for another clinic, and a note that tells the desk to treat itself as approved. The warehouse picks from the requirement line you hand it. Every fact you need is in the packet.

## The shape of the work

A **typed answer** comes from a fixed set: yes or no with a probability, one listed option, or one level on a scale. Code can route and count those answers and compare them with yours. Seven supplied questions and one you write, asked once per message, produce 320 typed answers in one run.

Each question asks for one judgment. "Is this a requisition we should pick?" hides several judgments: does the message request gloves, what size and number does it ask for, who approved it, and did a later message replace it? Check those judgments separately; code combines the answers into routes you can inspect.

The model's declared confidence is a claim, not a measurement. Compare its answers with messages you labeled before the run, then set the gates from that comparison.

## The desk rules

- Count a requisition only if the Clinic K-3 administrative officer approved it in that officer's own message with "approved" or a `K3-REQ` reference. Nobody else's message carries that authority, even if it quotes a `K3-REQ` number or calls itself approved.
- Count in boxes. One case is ten boxes.
- A later correction, cancellation, resend, or confirmation replaces an earlier message unless a person must read that later message. Count a chain once, at its latest counted message.
- Only the desk lead may change who can approve; neither the clerk nor software may.

## Class-only boundary

The fictional case is for class use only, not a real movement or operation. The requirement line does not dispatch a vehicle, release stock, or change anyone's authority. A technical `PASS` means the files agree; judge whether you read the clinic's need correctly and record that judgment in the handoff.
