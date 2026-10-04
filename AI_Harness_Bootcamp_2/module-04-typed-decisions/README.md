# Module 4 · Decide with typed questions

Turn a shift's raw intake messages into typed answers that software can route. Before trusting those answers, compare them with your own reading. Then give the desk lead a requirement line where every number is backed by a message with authority. The model answers fixed questions from fixed answer sets; it cannot write a sentence, pick a route, or invent a number.

Chalk Line is a vehicle resupply of sterile surgical gloves from Ferry Depot to Clinic K-3 on vehicle `CL-9`. Forty messages reached the intake desk during one shift: requisitions, corrections, cancellations, resends, stock notes, a vendor's offer, a request meant for another clinic, and one note that tells the desk to treat itself as approved. The warehouse picks from the requirement line the desk hands it. Every fact you need is in the packet, and the case is fictional.

Plan for about two and a half hours on Tuesday. That's a rough estimate, not a measured time.

## Start here

1. [Decide with typed questions](shared/MODULE_04_LAB.md): build the state, label a sample, run the model once as a decision function, validate and measure its answers, set the gates, route the pile, and decide the queue.

## The shape of the work

A chat answer is a paragraph that a person has to read and interpret before anything can act on it. A typed answer comes from a fixed set: yes or no with a probability, one option from a list, or one level on a scale. Code can branch on a typed answer, count it, and compare it with your own answer to the same question. Seven supplied questions and one you write yourself, asked once per message, give you 320 typed answers from one run, and software draws every route from them.

Each question is atomic: it asks for one judgment at a time. "Is this a requisition we should pick?" hides five judgments behind one answer: whether the message requests anything, which size, which number, whether it has authority, and whether a later message replaced it. Asked separately, each judgment can be checked on its own, and the rule that combines them lives in code you can read, not in the model's reasoning.

You can hold a general model running through a harness to a typed-answer contract. But the confidence it declares is its own claim. Measure that claim on messages you labeled before the run, then set the gates from what you measured.

## The desk rules

- A requisition counts only when the Clinic K-3 administrative officer approved it, shown in that officer's own message by the word "approved" or a `K3-REQ` reference. Nobody else's message carries that authority, even one that quotes a `K3-REQ` number, and no note that calls itself approved does.
- A box is the unit of issue. A case is ten boxes. The requirement line is counted in boxes.
- A later message that corrects, cancels, resends, or confirms an earlier one replaces it, unless that later message is itself one a person must read. The chain counts once, at its latest counted message.
- A change to who may approve is a decision for the desk lead, not for the clerk and not for software.

## Class-only boundary

The requirement line is for class review only. It does not dispatch a vehicle, release stock, or change anyone's authority. A technical `PASS` tells you the files agree with each other. You still need to judge whether you read the clinic's need correctly and record that judgment in the handoff.
