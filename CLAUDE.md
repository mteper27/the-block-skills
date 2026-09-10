# THE BLOCK — project facts

**These are settled. Do not re-derive them, do not substitute other figures, and
do not let a source document's own headline override them.**

## 165 Randolph Street, Brooklyn

| Fact | Value | Note |
| --- | --- | --- |
| **Building area** | **74,100 SF** | THE basis for every calculation. Under roof. |
| Mezzanine | ~14,000 SF | Adds **capacity, not square footage**. Sits INSIDE the 74,100 SF envelope. Never add it to the building area. |
| Outdoor / alleys | 22,000 SF | **No construction cost.** Bonus area only. Never price it. |
| Capacity | 7,440 GA standing | Wake PD04 Rev 4.4 test fit. |
| Existing clear height | 20 ft | |
| Target clear height | **50 ft** | |
| Perimeter | ~1,089 LF | Approximated as square from 74,100 SF. Replace with survey when available. |
| Landlord | Eric Cohen | Also owns 537 Johnson and 198 Randolph across the street. |
| Architect | Wake | Test fit PD04 Rev 4.4, 31 Aug 2026. |

### 135,953 SF is WRONG

The Master Development Budget uses 135,953 SF as its headline. That is stacked
floor area across all levels and it **inflates every $/SF metric**. It is not
used anywhere in our model. If it appears, it is a bug.

The single exception: sprinkler and fire alarm **coverage** is 88,100 SF
(74,100 ground + 14,000 mezzanine deck), because a mezzanine deck is a floor
that must be protected.

### The roof lift is MANDATORY

It is not an option, not a scenario, not a value-engineering candidate. The 50 ft
clear height is the moat — column-free industrial buildings over 50K SF are
extremely rare in NYC, and the 12-18 month DOB structural approval is itself the
barrier that protects the position once built. **Every scenario includes it.**

Roof lift quote (Matthew + Eric): **$3–4M**, carried at $3.5M. That is the
LIFTER'S SCOPE ONLY. Surrounding work — sidewalk shed, MEP off and back on, roof
repair, fireproofing, insulation, fire separation, permits — is separate and adds
roughly $3.5M more.

**A roof lift keeps the existing roof.** You cut it free of the perimeter walls,
jack it up, extend the columns underneath, and clad the new band of wall. You do
NOT demolish the roof and rebuild at height — that is a different, far more
expensive operation, and the development budget wrongly assumed it.

### Stage and mezzanine are GROUND-UP

Both stand on their own footings poured into the slab, Factory Town Infinity
style. Nothing hangs from the building. This is what removes the rigging load
from the roof and lets roof steel stay at ~15 lb/SF.

### Factory Town is a comp, with two adjustments

FT Infinity is **open-air** and **Miami-Dade hurricane-rated** (~175 mph design
wind). Before applying any FT structure or foundation rate:
1. Strip the open-air stage roof and crowd weather protection — this building has a roof.
2. Strip the hurricane foundations — an interior Brooklyn structure carries no wind load.

FT Infinity actual structure + foundations was $3,506,289 against a $2.0M budget
(+75%). Use actuals, never FT's budget lines.

### House setup, not touring inventory

Every artist brings a different production. The venue provides a **house** PA
(always house — nobody tours a PA for this size room), house lighting positions
and a competent house rig, and the mounting structure and power for visiting
productions. LED walls are Phase 2 — artists bring or rent their own.

### Licensing chain

Theatre seating shown on the technical drawings → theater use-classification →
liquor licence AND cabaret licence. **The seating is a licensing dependency, not
furniture.** Reprice it before deleting it. Seat count, and whether removable is
acceptable, is a legal determination we do not yet have.

**Verify:** NYC repealed the cabaret law in 2017. Confirm what actually applies
today before designing around it.

## Scope of the current work

**Construction capex only.** 165 Randolph has its own revenue model — do not
rebuild it, do not import operating costs, do not model returns.

## Environment note

LibreOffice cannot run in this container (a 3-cell file hangs at 179s on 0.6s of
CPU), so the xlsx skill's `recalc.py` is unusable. Verify workbooks with the
`formulas` package instead, and set `fullCalcOnLoad` so Excel computes on open.
