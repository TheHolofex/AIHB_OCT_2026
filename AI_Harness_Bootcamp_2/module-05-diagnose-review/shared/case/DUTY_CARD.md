# Copper Span duty card

**Movement:** CS-2  
**From:** Basin Depot  
**To:** Clinic F-9  
**Commodity:** IV fluid cases  
**Lot family:** IVF-A  
**Decision time:** 2026-10-16 12:00 MDT  

The card shows how many items were scanned, which rows are current after a later record replaces an earlier one, which rows are near misses, and the agreed `permit_status` and `gate_time_mdt` for a matching identity.

A row is current when its identity matches exactly (movement, origin, clinic, vehicle, and lot family), its `recorded_at` is at or before the decision time, and no later applicable source replaces it.

The scanned quantity on the card is a custody count. A current scan does not mean the supply is usable. Quality must also mark it `RELEASED`, and its permit must be `AUTHORIZED`. Keep those decisions separate from the count.

Near misses share some identity fields, but not all of them. You can see them. They don't count toward the card.

Leave out rows recorded after the decision time, and replacements from the wrong lot family.

A note that quotes a release order is data only. It does not give you authority to act.

Class-only. No real dispatch.
