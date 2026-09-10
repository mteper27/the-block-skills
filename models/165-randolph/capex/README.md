# 165 Randolph — construction capex model

Construction capex only. No revenue, no lease, no rental-vs-payback. What it costs to
raise the roof, build the stage and mezzanine from the ground up, and get the building to code.

## Run it

    python3 builddetail.py     # -> 165_Randolph_Detailed_Budget.xlsx

LibreOffice is unusable in the container (it hangs on a three-cell file). Formulas are
verified with the `formulas` package and the workbook is saved with `fullCalcOnLoad=True`
so Excel recalculates on open.

## Files

| File | What it holds |
|---|---|
| `detail.py` | The line schedule. `division -> group -> [(description, qty, unit, rate, source)]`. Drivers at the top: `SF`, `MEZZ`, `PERI`, `RISE`, `STAGE`, and the rigging-grid geometry `CROWDW`/`CROWDD`. |
| `markups.py` | Escalation, general conditions, overhead/profit/insurance, contingency — what each is, who gets it, whether it is necessary, what is negotiable. |
| `cuts.py` | Cut opportunities. `(division, item, type, carried, cut_to, gate, why)`. Type is FIX/VERIFY/ASK/SCOPE/DEFER/SCHEDULE; gate is OK/CODE/SLA/ASK. |
| `questions.py` | Questions for the estimator, architect, mechanical engineer, Rooflifters, landlord and counsel, each with why it is hard to deflect and the dollars at stake. |
| `thomas_raw.py` | All 199 trade lines extracted verbatim from the Master Development Budget of 7 Sep 2026. |
| `thomas.py` | Classification of every one of those lines: IN / ADD / GC / OUT, with where it lands here or why it is off. |
| `builddetail.py` | Assembles the six-sheet workbook. |

## Structure of the number

Trade cost stands alone. Everything else sits below the line as a separate cost, and the
three markup rates are each applied to trade cost only — they do not compound on each other.

    TRADE COST (div 000-500)          the work itself
      + escalation        10% of trade
      + general conditions 11% of trade      <- toggles to Thomas's own line items
      + overhead/profit/insurance 9% of trade
    = CONSTRUCTION COST
      + contingency                   ONE pot, a flat figure you set
      + Thomas's lines toggled on     from the reconciliation sheet, default zero
      + FF&E (div 600)
      + soft costs (div 700)
    = TOTAL DEVELOPMENT COST

There is exactly one contingency. The earlier version stacked a contractor contingency and
an owner contingency, and the owner contingency was also displayed twice.

## Toggles

| Cell | What it does |
|---|---|
| `Detailed Budget!E7` | Theatre seat rate. 25 = own sourcing, 125 = as filed. Drives the removable seating line in division 600. |
| `Detailed Budget!E12` | General conditions basis. 1 = the 11% percentage. 0 = Thomas's 013000 + 015800 line items instead. Never both — they are the same site cost. |
| `Detailed Budget!F451` | Contingency, as a dollar figure. |
| `Thomas Reconciliation!H*` | One toggle per line of Thomas's budget. Default off where the scope is already carried here. |

## Settled facts this model depends on

See `CLAUDE.md` at the repository root. The load-bearing ones: 74,100 SF is the basis, the
mezzanine adds capacity inside that envelope and not area, the roof lift is mandatory, a lift
keeps the existing roof rather than replacing it, and the stage and mezzanine are ground-up on
their own footings so nothing hangs from the building.
