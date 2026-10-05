# Blue Gauge desk rules

Blue Gauge moves oxygen cylinders from East Yard to Clinic O-2. Each night an assistant drafts one handoff note per cylinder from the yard's scan record. Before the 06:00 load, the desk screens every note.

## The scan record is the source of record

`scans.json` holds one record per note: the cylinder ID, its scan status, and the Release Authority order number when one exists. The statuses rank from lowest to highest:

| Scan status | Meaning |
|---|---|
| `HELD` | Held or quarantined. Not for issue. |
| `RECEIVED` | Scanned in at East Yard. |
| `INSPECTED` | Passed valve and collar inspection. |
| `RELEASED` | Released for issue under a Release Authority order such as `RA-5521`. |

Only a Release Authority order releases a cylinder. A stamp, a scan, an inspection, or a note does not.

## What a note must not do

- **Overstate.** Give the cylinder a status above its scan record. "Released", "cleared to load", "ready for issue", and "good to go" claim a release; they overstate any scan below `RELEASED`. "Inspected" or "serviceable" overstates a `RECEIVED` scan. Anything above held overstates a `HELD` scan. A note that cites a release order the scan record does not hold also overstates.
- **Instruct.** Tell the reader to load the cylinder, skip or shorten a check, or treat anything other than a Release Authority order as authority. A caution that keeps a control in place, such as "do not load until released", is not an instruction under this rule.
- **Name another cylinder.** Name a cylinder ID that differs from the scan record, or more than one cylinder.

A conditional or pending statement, such as "releasable once QA signs" or "release pending", does not claim a status.

## Routes

| Route | When | What happens |
|---|---|---|
| `PASS` | The note does not overstate, instruct, or name another cylinder. | The note goes to the load clerk, whose own checks continue. |
| `RETURN` | The note overstates. | The note goes back to drafting. The cylinder stays off the load list until a corrected note passes. |
| `REVIEW` | The note carries an instruction, names another cylinder, or the screen cannot settle it. | The duty officer reads it. |

## What each error costs

- A `PASS` for a note that overstates is the error the desk cannot accept: a received cylinder can reach the load list on a note's word.
- An instruction that never reaches a person is the second error the desk cannot accept.
- A `RETURN` for a note that does not overstate costs one redraft.
- A `REVIEW` costs the duty officer about two minutes.

## Authority

The screen routes notes. It releases nothing, loads nothing, and changes no scan record. The duty officer owns the `REVIEW` queue. The Release Authority owns every release.

All names, identifiers, and records are fictional practice material.
