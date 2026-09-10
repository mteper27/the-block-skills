# 165 Randolph — Cost to Build & Open

Construction capex only. Regenerates `165_Randolph_Cost_To_Open.xlsx` from source.

## Run

```bash
pip install openpyxl
python3 build.py                 # writes 165_Randolph_Cost_To_Open.xlsx
```

Then arm recalculation (openpyxl writes formulas with no cached values):

```python
import openpyxl
p='165_Randolph_Cost_To_Open.xlsx'
wb=openpyxl.load_workbook(p)
wb.calculation.fullCalcOnLoad=True; wb.calculation.calcCompleted=False
wb.calculation.calcMode='auto'; wb.save(p)
```

## Files

| File | What it is |
| --- | --- |
| `lines.py` | The line schedule — 102 lines, each with tier (0/1/R/2), as-filed and corrected cost, and a sourced note. **This is where you edit costs.** |
| `infinity.py` | Which lines survive an Infinity-room build, and which shrink |
| `roof.py` | The Roof Lift sheet — parametric build-up plus the Rooflifters 2022 rate card |
| `seating.py` | Theater seating: compliance vs as-filed vs a beautiful theater |
| `build.py` | Assembles all nine sheets |

## Verification

LibreOffice cannot run in the Claude Code container (a 3-cell file hangs), so
`recalc.py` is unusable. Verify instead with the `formulas` package:

```bash
pip install formulas
```

Then load the workbook, `calculate()`, and assert (a) zero cells whose value
starts with `#`, and (b) the Line Build reconciliation rows J105:J111 sum to
0.00. Last run: **1,893 cells, 0 errors, reconciliation $0.00.**

## Reconciliation

The `As Filed` column ties to the Master Development Budget v1 exactly:
trade $18,175,107.50 · off-site $2,257,500 · soft $4,006,750 · FF&E $8,232,250.
If that variance is not zero, the line schedule has drifted from source.

## Current ladder

| Scenario | Total |
| --- | --- |
| SHELL & CODE | $41,474,352 |
| BASE | $63,423,011 |
| BASE + LIFT | $80,104,513 |
| ELEVATED | $82,940,222 |
| PREMIUM | $90,160,542 |

## Open inputs

- **Factory Town VIP platform + decking areas (SF)** — replaces the $2.85M
  unbenchmarked mezzanine block (steel $2.0M, poured deck $500k, footings $350k)
- **Rooflifters on a union basis** — the card is explicitly non-union; that
  multiplier (currently 1.8x) is the largest single uncertainty
- **Wake test fit** — never received; mezzanine and seating logic is unverified
  against it
- **Counsel:** as-of-right determination in M3-1; theater seat count and whether
  removable is acceptable; whether the cabaret licence still exists (NYC repealed
  the cabaret law in 2017)
