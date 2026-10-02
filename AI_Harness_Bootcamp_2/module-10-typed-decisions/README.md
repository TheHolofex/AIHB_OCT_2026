# Module 10 · Decide with typed questions

Turn a shift's pile of raw intake messages into typed answers that software can route, measure those answers against your own reading before you trust them, and hand the desk lead a requirement line in which every number rests on a message with authority. The model answers fixed questions with fixed answer sets; it writes no sentence, picks no route, and invents no number.

Chalk Line is a vehicle resupply of sterile surgical gloves from Ferry Depot to Clinic K-3 on vehicle `CL-9`. Forty messages reached the intake desk during one shift: requisitions, corrections, cancellations, resends, stock notes, a vendor's offer, a request meant for another clinic, and one note that tells the desk to treat itself as approved. The warehouse picks from the requirement line the desk hands it. Every fact you need is in the packet, and the case is fictional.

Plan for 2 hours 30 minutes on Tuesday, including 2 hours of practice. This is a planning allowance, not a measured completion guarantee.

## Start here

1. [Decide with typed questions](shared/MODULE_10_LAB.md): build the state, label a sample, run the model once as a decision function, validate and measure its answers, set the gates, route the pile, and decide the queue.

## The shape of the work

A chat answer is a paragraph a person has to read and interpret before anything can act on it. A typed answer is a value from a fixed set: yes or no with a probability, one option from a list, one level on a scale. Code can branch on a typed answer, count it, and compare it with your own answer to the same question. Seven supplied questions and one you write yourself, asked once per message, give you 320 typed answers from one run, and software draws every route from them.

Each question is atomic. "Is this a requisition we should pick?" hides five judgments behind one answer: whether it is a request at all, which size, which number, whether it carries authority, and whether a later message replaced it. Asked separately, each judgment can be checked separately, and the rule that combines them lives in code you can read, not in the model's reasoning.

A general model run through a harness can be held to a typed-answer contract, with one difference you must respect: the confidence it declares is a claim about itself. You measure that claim on messages you labeled first, and you set the gates from the measurement.

## The desk rules

- A requisition counts only when the Clinic K-3 administrative officer approved it, shown in that officer's own message by the word "approved" or a `K3-REQ` reference. Nobody else's message carries that authority, even one that quotes a `K3-REQ` number, and no note that calls itself approved does.
- A box is the unit of issue. A case is ten boxes. The requirement line is counted in boxes.
- A later message that corrects, cancels, resends, or confirms an earlier one replaces it, unless that later message is itself one a person must read. The chain counts once, at its latest counted message.
- A change to who may approve is a decision for the desk lead, not for the clerk and not for software.

## Class-only boundary

The requirement line permits only class review. It dispatches no vehicle, releases no stock, and changes nobody's authority. A technical `PASS` says the files agree with each other; whether the clinic's need was read correctly is your judgment, recorded in the handoff.
