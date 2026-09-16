# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
import other as O, sept16_raw as R
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

F = 'Arial'
BLK = Font(name=F, size=9);  BOLD = Font(name=F, size=9, bold=True)
RED = Font(name=F, size=9, bold=True, color='C00000')
GRN = Font(name=F, size=9, bold=True, color='1F6B3B')
H1  = Font(name=F, size=18, bold=True, color='1F3864')
H2  = Font(name=F, size=11, bold=True, color='1F3864')
WHT = Font(name=F, size=9, bold=True, color='FFFFFF')
SM  = Font(name=F, size=8, color='595959')
BIG = Font(name=F, size=14, bold=True, color='1F3864')
SUB = Font(name=F, size=9, bold=True, color='1F3864')
HDR = PatternFill('solid', fgColor='1F3864'); GPF = PatternFill('solid', fgColor='D9E2F3')
GRY = PatternFill('solid', fgColor='F2F2F2'); GRF = PatternFill('solid', fgColor='E2EFDA')
med = Side(style='medium', color='1F3864'); TOPB = Border(top=med)
CUR = '$#,##0;($#,##0);"-"'
def wr(): return Alignment(wrap_text=True, vertical='top')

wb = Workbook()
def head(ws, sub):
    ws.cell(2, 2, '165 RANDOLPH STREET').font = H1
    ws.cell(3, 2, sub).font = H2
    ws.cell(4, 2, 'Soft costs, FF&E and off-site · everything below the construction number '
                  '· 16 Sep 2026 vs our V2 · CONFIDENTIAL').font = SM
    return 6
def hrow(ws, r, cols):
    for i, h in enumerate(cols, 2):
        c = ws.cell(r, i, h); c.font = WHT; c.fill = HDR
        c.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    return r + 1

# ===================================================== 1. THE COMPARISON
ws = wb.active; ws.title = 'The Other Expenses'
for col, w in zip('ABCDEFG', [3, 40, 14, 14, 14, 72, 84]): ws.column_dimensions[col].width = w
r = head(ws, 'EVERY LINE BELOW THE CONSTRUCTION NUMBER')
ws.cell(r, 2, 'Ours $%s.  His $%s.  He is $%s higher.'
        % (f'{O.TOTAL_OURS:,.0f}', f'{O.TOTAL_HIS:,.0f}',
           f'{O.TOTAL_HIS - O.TOTAL_OURS:,.0f}')).font = BIG
r += 2
for t in ['His columns tie to his own Budget Summary rows D47, D65 and D23, untouched. Ours tie '
          'to divisions 700 and 600 as published, plus three items we carry inside the TRADE '
          'cost that he carries here — abatement $1,000,750, signage and wayfinding '
          '$125,000, and lighting and controls $299,100. Each is flagged on its own row.',
          '',
          'SIX LINES ARE IDENTICAL TO THE DOLLAR: feasibility, project management, data and '
          'CCTV, office furniture, merchandise cases, and operations. That is not a coincidence '
          '— we built ours off his where his was sound.']:
    c = ws.cell(r, 2, t); c.font = BLK; c.alignment = wr()
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=7)
    ws.row_dimensions[r].height = 30 if len(t) > 140 else (13 if t else 7)
    r += 1
r += 1

def block(r, title, rows, ours_tot, his_tot, foot):
    ws.cell(r, 2, title).font = H2; r += 1
    r = hrow(ws, r, ['', 'OURS', 'HIS', 'Delta', 'His lines, verbatim', 'What it means'])
    for name, o, h, det, com in rows:
        ws.cell(r, 2, name).font = BLK
        for col, v in ((3, o), (4, h), (5, h - o)):
            c = ws.cell(r, col, v); c.number_format = CUR
            c.font = (RED if h > o else (GRN if h < o else BLK)) if col == 5 else BLK
        if abs(h - o) < 1:
            for col in range(2, 6): ws.cell(r, col).fill = GRF
        c = ws.cell(r, 6, det); c.font = SM; c.alignment = wr()
        c = ws.cell(r, 7, com); c.font = BLK; c.alignment = wr()
        ws.row_dimensions[r].height = max(38, 10.5 * (max(len(det) // 74, len(com) // 86) + 1))
        r += 1
    ws.cell(r, 2, foot).font = BOLD
    for col, v in ((3, ours_tot), (4, his_tot), (5, his_tot - ours_tot)):
        c = ws.cell(r, col, v); c.number_format = CUR; c.font = BOLD
    for col in range(2, 8):
        ws.cell(r, col).fill = GRY; ws.cell(r, col).border = TOPB
    return r + 2

r = block(r, 'SOFT COSTS', O.SOFT, O.OURS_SOFT, O.HIS_SOFT, 'TOTAL SOFT COSTS')
r = block(r, 'FF&E', O.FFE, O.OURS_FFE, O.HIS_FFE, 'TOTAL FF&E')
r = block(r, 'OFF-SITE', O.OFFSITE, O.OURS_OFF, O.HIS_OFF, 'TOTAL OFF-SITE')
ws.cell(r, 2, 'TOTAL OTHER EXPENSES').font = BOLD
for col, v in ((3, O.TOTAL_OURS), (4, O.TOTAL_HIS), (5, O.TOTAL_HIS - O.TOTAL_OURS)):
    c = ws.cell(r, col, v); c.number_format = CUR; c.font = BOLD
for col in range(2, 8):
    ws.cell(r, col).fill = GPF; ws.cell(r, col).border = TOPB

# ============================================== 2. WHAT TO DO ABOUT IT
ws = wb.create_sheet('What To Do')
for col, w in zip('ABCD', [3, 46, 16, 96]): ws.column_dimensions[col].width = w
r = head(ws, 'THE OTHER EXPENSES, SORTED INTO ACTIONS')

WE_ADD = [(n, o, h, c) for n, o, h, d, c in O.SOFT + O.FFE if o > h]
HE_CUTS = [(n, o, h, c) for n, o, h, d, c in O.SOFT + O.FFE if h > o]

ws.cell(r, 2, 'WE CARRY SCOPE HE DOES NOT — and in most of these we are right').font = H2
r += 1
r = hrow(ws, r, ['', 'Ours minus his', 'Why we are right to carry it'])
for n, o, h, c in WE_ADD:
    ws.cell(r, 2, n).font = BLK
    cc = ws.cell(r, 3, o - h); cc.number_format = CUR; cc.font = GRN
    txt = '. '.join(c.split('. ')[:2]).rstrip('.') + '.'
    cc = ws.cell(r, 4, txt); cc.font = BLK; cc.alignment = wr()
    ws.row_dimensions[r].height = max(26, 10.5 * (len(txt) // 96 + 1))
    r += 1
ws.cell(r, 2, 'SUBTOTAL').font = BOLD
cc = ws.cell(r, 3, sum(o - h for _, o, h, _ in WE_ADD))
cc.number_format = CUR; cc.font = BOLD; cc.border = TOPB
ws.cell(r, 2).border = TOPB
r += 2
ws.cell(r, 2, 'If our numbers are right, HIS budget is missing this money — no Phase I or '
              'Phase II, no existing-conditions survey, no Rooflifters Stage 3 analysis, no '
              'legal at all, one lot of metal detectors for 7,440 people, and builder’s '
              'risk that may or may not be inside his 9%.').font = BLK
ws.cell(r, 2).alignment = wr()
ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=4)
ws.row_dimensions[r].height = 30
r += 3

ws.cell(r, 2, 'HE CARRIES MORE THAN US — and these split three ways').font = H2
r += 1
r = hrow(ws, r, ['', 'His minus ours', 'What kind of difference it is'])
KIND = {
 'Architectural lighting': 'BOUGHT TWICE. $1,750,000 here plus $1,631,436 inside his electrical '
   'trade. His own line says "provided by others".',
 'Seating & furniture': 'A LEGAL QUESTION. Seat count drives the theater classification which '
   'drives the liquor licence. Counsel decides this, not the estimator.',
 'Signage, wayfinding & art': 'A BRAND DECISION. A $400,000 exterior sign may well be worth it '
   'on this building, but it is ours to decide, not an estimating error.',
 'Soft goods': 'HE IS PROBABLY RIGHT AND WE ARE LIGHT. His own benchmark note says $725k, and '
   'his $500,000 explicitly excludes the mezzanine-edge cutdown drape.',
 'Video': 'REAL SCOPE WE DO NOT CARRY. Concourse displays and distribution. The projector '
   'matches exactly and the video walls are Phase 2 on both sides.',
 'Bar & kitchen equipment': 'BOTH OF US MAY BE LIGHT. His own note reads "BPT: 26 POS / Prep '
   'Kitchen / 1 Walk-in Cooler $837K" against 74 positions at $9,000 here.',
 'Performance lighting': 'HE IS ABOVE HIS OWN BENCHMARK ($450k) AND WE ARE BELOW IT. Ours '
   'probably moves up.',
 'Production equipment': 'HE IS RIGHT ON THE LIFTS. A room this size owns a fork lift and a '
   'scissor lift rather than renting them every load-in.',
 'Permits & approvals': 'A PERCENTAGE OF HIS OWN TRADE COST (1.3%). Cut the trade cost and this '
   'falls with it automatically.',
 'Design & engineering': 'UNKNOWABLE UNTIL HE SPLITS THE $3.1M A/E LUMP. But his acoustical '
   'engineering at $15,000 against our $200,000 is a real difference of view.',
 'Abatement': 'A METHOD DIFFERENCE. $21/SF on 70,000 SF of roof presumes the roof comes off. '
   'A lift keeps it. And nobody has done the ACP-5 survey.',
}
for n, o, h, c in HE_CUTS:
    ws.cell(r, 2, n).font = BLK
    cc = ws.cell(r, 3, h - o); cc.number_format = CUR; cc.font = RED
    cc = ws.cell(r, 4, KIND.get(n, c.split('. ')[0] + '.')); cc.font = BLK; cc.alignment = wr()
    ws.row_dimensions[r].height = max(26, 10.5 * (len(KIND.get(n, '')) // 98 + 1))
    r += 1
ws.cell(r, 2, 'SUBTOTAL').font = BOLD
cc = ws.cell(r, 3, sum(h - o for _, o, h, _ in HE_CUTS))
cc.number_format = CUR; cc.font = BOLD; cc.border = TOPB
ws.cell(r, 2).border = TOPB
r += 2
ws.cell(r, 2, 'Plus the $2,257,500 off-site parking garage, which we do not carry at all and '
              'whose own label (260 spaces) contradicts its own formula (=86*25000).').font = BLK
ws.cell(r, 2).alignment = wr()
ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=4)
r += 3
ws.cell(r, 2, 'ONLY ONE OF THESE IS A STRAIGHT ERROR').font = H2; r += 1
ws.cell(r, 2, 'The architectural lighting bought twice. Everything else in the other expenses is '
              'either scope he is missing, scope we are missing, or a decision that belongs to '
              'us and to counsel — not to the estimator.').font = BOLD
ws.cell(r, 2).alignment = wr()
ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=4)
ws.row_dimensions[r].height = 28

for s in wb.worksheets:
    s.sheet_view.showGridLines = False
    s.freeze_panes = 'A7'
wb.properties.title = '165 Randolph - The Other Expenses'
wb.calculation.fullCalcOnLoad = True
OUT = '165_Randolph_Other_Expenses_Ours_vs_His.xlsx'
wb.save(OUT)
print('wrote', OUT)
