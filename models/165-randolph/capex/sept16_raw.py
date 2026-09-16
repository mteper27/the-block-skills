# -*- coding: utf-8 -*-
"""Verbatim extract of the 16 Sep 2026 Master Development Budget.

Generated from `260916_Master_Development_Budget_165_Randolph.xlsx`, sheet
'Building & Fit-out Breakdown'. Nothing here is interpreted -- it is the file.
The extract reconciles to the file's own Trade Cost cell to $0.00; see
sept16.py RECON.
"""
import json, os
_p = os.path.join(os.path.dirname(__file__), 'sept16_lines.json')
LINES = json.load(open(_p))          # (csi, division, item_no, desc, qty, unit, rate, total, note)

# The file's own roll-up cells, Budget Summary sheet, read verbatim.
TRADE   = 37_945_959.75   # D25  ='Building & Fit-outBudget Detail'!C49-C47
TBP     = 12_000_000.00   # D26  hard-keyed "Trade Costs To Be Priced"
GCLINE  =  3_141_000.00   # D27  General Conditions -- staff build-up, 90 wks
OHP     =  4_777_826.38   # D28  =SUM(D25:D27)*0.09
CONTRCT =  5_786_478.61   # D29  =SUM(D25:D28)*0.1
CONSTR  = 63_651_264.74   # D31  =SUM(D25:D30)
SOFT    =  6_784_977.48   # D47
FFE     =  8_292_250.00   # D65
OFFSITE =  2_257_500.00   # D23  parking garage 86 x $25,000 + 5% escalation
CONTING =  8_098_599.22   # D67  =(D23+D31+D47+D65)*0.1  <-- labelled "Soft Costs & FFE"
TOTAL   = 89_084_591.44   # D69
PRECON  =     60_000.00   # Building & Fit-outBudget Detail C46, not on the Breakdown sheet
HIS_SF  = 135_953         # hard-keyed in D71, I31, I47, I65, I67
