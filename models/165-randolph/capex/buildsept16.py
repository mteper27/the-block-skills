# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
import sept16 as S
import sept16_raw as R
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

F = 'Arial'
BLK  = Font(name=F, size=9);                 BOLD = Font(name=F, size=9, bold=True)
BLUE = Font(name=F, size=9, color='0000FF'); RED  = Font(name=F, size=9, bold=True, color='C00000')
GRN  = Font(name=F, size=9, bold=True, color='1F6B3B')
H1   = Font(name=F, size=18, bold=True, color='1F3864')
H2   = Font(name=F, size=11, bold=True, color='1F3864')
WHT  = Font(name=F, size=9, bold=True, color='FFFFFF')
SM   = Font(name=F, size=8, color='595959')
BIG  = Font(name=F, size=14, bold=True, color='1F3864')
HDR = PatternFill('solid', fgColor='1F3864'); GPF = PatternFill('solid', fgColor='D9E2F3')
YEL = PatternFill('solid', fgColor='FFF2CC'); GRY = PatternFill('solid', fgColor='F2F2F2')
PNK = PatternFill('solid', fgColor='FCE4E4'); GRF = PatternFill('solid', fgColor='E2EFDA')
thin = Side(style='thin', color='D0D0D0'); med = Side(style='medium', color='1F3864')
BOX = Border(left=thin, right=thin, top=thin, bottom=thin); TOPB = Border(top=med)
CUR = '$#,##0;($#,##0);"-"'; CUR2 = '$#,##0.00;($#,##0.00);"-"'
def wr(): return Alignment(wrap_text=True, vertical='top')

wb = Workbook()

def head(ws, sub):
    for i, t, f in ((2, '165 RANDOLPH STREET', H1), (3, sub, H2),
                    (4, 'Audit of the Master Development Budget dated 16 Sep 2026 · '
                        'method: construction-budget-audit skill · CONFIDENTIAL', SM)):
        ws.cell(i, 2, t).font = f
    return 6

def hrow(ws, r, cols):
    for i, h in enumerate(cols, 2):
        c = ws.cell(r, i, h); c.font = WHT; c.fill = HDR
        c.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    return r + 1

# ============================================================ 1. READ ME FIRST
ws = wb.active; ws.title = 'Read Me First'
for col, w in zip('ABCDE', [3, 62, 18, 18, 18]): ws.column_dimensions[col].width = w
r = head(ws, 'THE ANSWER, IN ONE PAGE')

gap = R.TOTAL - S.V2_TOTAL
ws.cell(r, 2, 'He is $%s high. About $21M of that is mechanical.' % f'{gap/1e6:,.1f}M').font = BIG
r += 2
for t in [
  'His 16 Sep budget totals $%s. Our own bottom-up budget is $%s. That is a $%s gap.' %
      (f'{R.TOTAL:,.0f}', f'{S.V2_TOTAL:,.0f}', f'{gap:,.0f}'),
  '',
  'I rebuilt his workbook line by line. My reconstruction of his trade cost ties to his own '
  'cell to $0.00, so every number below is his, not mine.',
  '',
  'Then I corrected only his own arithmetic and basis errors — using his rates, his '
  'quantities and, where he wrote them down, his own backup rows. His budget falls to $%s.'
      % f"{S.FIX['tot']:,.0f}",
  '',
  'Strip the off-site parking garage, which we do not carry at all, and he lands at $%s '
  'against our $%s. That is %s apart.' % (f'{S.FIX_NO_GARAGE:,.0f}', f'{S.V2_TOTAL:,.0f}',
      f"{(S.FIX_NO_GARAGE-S.V2_TOTAL)/S.V2_TOTAL:.1%}"),
  '',
  'So the two estimates actually agree. The quote is not high because he thinks the building '
  'is harder to build than we do. It is high because of four mechanical faults: a contingency '
  'line that computes on the whole project instead of on what its label says, $10.3M of trade '
  'cost multiplied by a square footage this building does not have, the general-conditions '
  'function charged in two places at once, and three lump sums that disagree with their own '
  'backup.',
  '',
  'Do NOT go back at him with the $24M. Go back with the four faults. They are checkable, they '
  'are his own cells, and they are very hard to argue with.']:
    c = ws.cell(r, 2, t); c.font = BOLD if t.startswith('He is') else BLK
    c.alignment = wr(); ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=5)
    ws.row_dimensions[r].height = 26 if len(t) > 110 else (13 if t else 7)
    r += 1
r += 1

ws.cell(r, 2, 'THE BRIDGE').font = H2; r += 1
r = hrow(ws, r, ['', '16 Sep as sent', 'Corrected', 'Delta'])
for lab, a, b in S.BRIDGE:
    tot = lab.startswith('CONSTRUCTION') or lab.startswith('TOTAL')
    c = ws.cell(r, 2, lab); c.font = BOLD if tot else BLK
    for col, v in ((3, a), (4, b), (5, b - a)):
        c = ws.cell(r, col, v); c.number_format = CUR
        c.font = BOLD if tot else (RED if col == 5 and b - a < -1000 else BLK)
        if tot: c.border = TOPB; ws.cell(r, 2).border = TOPB
        if tot: c.fill = GPF
    if tot: ws.cell(r, 2).fill = GPF
    r += 1
r += 1
for lab, v, note in [
  ('$ per SF on the real 74,100 SF — as sent', R.TOTAL / S.SF, 'His own sheet reports $655/SF, but it divides by 135,953.'),
  ('$ per SF on the real 74,100 SF — corrected', S.FIX['tot'] / S.SF, ''),
  ('$ per SF on the real 74,100 SF — our V2', S.V2_TOTAL / S.SF, '')]:
    ws.cell(r, 2, lab).font = BLK
    c = ws.cell(r, 3, v); c.number_format = '$#,##0'; c.font = BOLD
    ws.cell(r, 5, note).font = SM; r += 1

# =============================================================== 2. RECONCILE
ws = wb.create_sheet('Reconciliation')
for col, w in zip('ABCDEF', [3, 66, 18, 22, 18, 70]): ws.column_dimensions[col].width = w
r = head(ws, 'STEP 1 — RECONCILE BEFORE YOU ANALYSE')
ws.cell(r, 2, 'If this variance is not zero I am auditing my own transcription, not his budget.').font = SM
r += 2
r = hrow(ws, r, ['', 'Amount'])
for lab, v in S.RECON:
    z = lab == 'VARIANCE'
    c = ws.cell(r, 2, lab); c.font = GRN if z else BLK
    c2 = ws.cell(r, 3, v); c2.number_format = CUR2; c2.font = GRN if z else BLK
    if z: c.fill = GRF; c2.fill = GRF
    r += 1
ws.cell(r, 2, '309 line items extracted from his Breakdown sheet. Variance $0.00.').font = SM
r += 3

ws.cell(r, 2, 'STEP 2 — HIS ARITHMETIC, PROVEN CELL BY CELL').font = H2; r += 2
r = hrow(ws, r, ['Cell', 'His formula', 'Recomputed', 'In the file', 'What it means'])
for cell, form, calc, infile, note in S.PROOF:
    ws.cell(r, 2, cell).font = BOLD
    c = ws.cell(r, 3, form); c.data_type = 's'; c.font = BLUE
    for col, v in ((4, calc), (5, infile)):
        c = ws.cell(r, col, v); c.number_format = CUR2; c.font = BLK
    c = ws.cell(r, 6, note); c.font = BLK; c.alignment = wr()
    ws.row_dimensions[r].height = 46
    r += 1
r += 1
ws.cell(r, 2, 'CASCADE — what $1 of trade cost actually costs you, as the file is built today').font = H2
r += 1
for lab, v in [('x 1.09  overhead, profit & insurance', 1.09),
               ('x 1.10  contractor contingency', 1.10),
               ('x 1.10  the project contingency on row 67', 1.10),
               ('Every $1 of trade cost becomes', S.CASCADE)]:
    fnt = BOLD if lab.startswith('Every') else BLK
    ws.cell(r, 2, lab).font = fnt
    c = ws.cell(r, 3, v); c.number_format = '0.0000'; c.font = fnt
    r += 1
ws.cell(r, 2, 'Escalation is blank, so it adds nothing to the cascade today — which is itself '
              'a fault, not a saving.').font = SM

# ================================================================ 3. FINDINGS
ws = wb.create_sheet('Findings')
for col, w in zip('ABCDEFG', [3, 5, 48, 74, 15, 15, 74]): ws.column_dimensions[col].width = w
r = head(ws, 'THE FINDINGS — direction, evidence, dollars')
ws.cell(r, 2, 'OVERSTATED = priced too high, negotiate it down.  UNDERSTATED = missing or too '
              'low, fund it back in.  These are opposite actions — never net them together.').font = SM
ws.row_dimensions[r].height = 24; r += 2
r = hrow(ws, r, ['No.', 'Direction / headline', 'The evidence, quoted from his file',
                 'His $', 'Should be', 'What to do'])
for i, d, head_, ev, his, ok, rem in S.FINDINGS:
    ws.cell(r, 2, i).font = BOLD
    c = ws.cell(r, 3, d + '\n' + head_)
    c.font = RED if d in ('OVERSTATED', 'DOUBLE-COUNT') else (GRN if d == 'UNDERSTATED' else BOLD)
    c.alignment = wr()
    c = ws.cell(r, 4, ev); c.font = BLK; c.alignment = wr()
    for col, v in ((5, his), (6, ok)):
        c = ws.cell(r, col, v if v else None); c.number_format = CUR; c.font = BLK
    if his and ok is not None and ok < his:
        ws.cell(r, 5).fill = PNK; ws.cell(r, 6).fill = GRF
    c = ws.cell(r, 7, rem); c.font = BLK; c.alignment = wr()
    ws.row_dimensions[r].height = max(58, 11 * (len(ev) // 70 + 1))
    r += 1

# =============================================== 4. CORRECTIONS APPLIED
ws = wb.create_sheet('Corrections Applied')
for col, w in zip('ABCDE', [3, 6, 96, 18, 18]): ws.column_dimensions[col].width = w
r = head(ws, 'EVERY CORRECTION IS MADE TO A SOURCE CELL, THEN HIS OWN FORMULA CHAIN IS RE-RUN')
ws.cell(r, 2, 'No markup is applied by hand anywhere on this sheet. That is deliberate — it is '
              'the only way to be sure a correction is not counted twice as it passes through '
              'overhead, contingency and contingency-on-contingency.').font = SM
ws.row_dimensions[r].height = 24; r += 2
r = hrow(ws, r, ['', 'Correction to trade cost', 'Trade $', 'All-in effect'])
for i, lab, v in S.CORR:
    ws.cell(r, 2, i).font = BOLD
    c = ws.cell(r, 3, lab); c.font = BLK; c.alignment = wr()
    for col, val in ((4, v), (5, v * S.CASCADE)):
        c = ws.cell(r, col, val); c.number_format = CUR; c.font = RED
    ws.row_dimensions[r].height = 26
    r += 1
tot = sum(v for _, _, v in S.CORR)
ws.cell(r, 3, 'NET CORRECTION TO TRADE COST').font = BOLD
for col, val in ((4, tot), (5, tot * S.CASCADE)):
    c = ws.cell(r, col, val); c.number_format = CUR; c.font = BOLD; c.border = TOPB; c.fill = GPF
ws.cell(r, 3).fill = GPF; ws.cell(r, 3).border = TOPB
r += 2
ws.cell(r, 2, 'The all-in column is indicative only — the real total on "Read Me First" comes '
              'from re-running his formulas, not from multiplying by 1.3189.').font = SM
r += 2
for lab, v in [('His trade cost', R.TRADE), ('Corrected trade cost', S.TRADE_FIX),
               ('General conditions at 8.35% (Schimenti, 555 Johnson)', S.GC_FIX),
               ('Escalation at 6% on the corrected trade cost', S.FIX['esc'])]:
    ws.cell(r, 3, lab).font = BLK
    c = ws.cell(r, 4, v); c.number_format = CUR; c.font = BOLD; r += 1

# ====================================================== 5. SEPT 4 -> SEPT 16
ws = wb.create_sheet('Sept 4 to Sept 16')
for col, w in zip('ABCDE', [3, 10, 46, 17, 17]): ws.column_dimensions[col].width = w
for c, w in (('F', 17), ('G', 60)): ws.column_dimensions[c].width = w
r = head(ws, 'WHAT MOVED IN TWELVE DAYS')
ws.cell(r, 2, 'The 4 Sep file totalled $42,555,099. The 16 Sep file totals $89,084,591. '
              'Most of that is real pricing work he genuinely did — and it is worth saying so.').font = SM
ws.row_dimensions[r].height = 24; r += 2
r = hrow(ws, r, ['CSI', 'Division', '4 Sep', '16 Sep', 'Delta', 'Note'])
notes = {'015800': 'ENTIRELY NEW. The single biggest addition in the file.',
         '055100': 'STILL ZERO. Nineteen lines, every quantity blank.',
         '064000': 'STILL ZERO. Every bar in the building.',
         '081000': 'STILL ZERO.', '084100': 'STILL ZERO.', '088000': 'STILL ZERO.',
         '078100': 'STILL ZERO.', '092300': 'STILL ZERO.', '062000': 'STILL ZERO.',
         '075000': 'DOWN $3.2M — he moved off full roof replacement. Good.',
         '230000': 'One line: 132,542 SF @ $45. No tonnage, no load.',
         '260000': 'Real distribution now priced. But on 135,953 SF.',
         '013000': 'General conditions content, sitting in trade cost.'}
for csi, name, a, b in S.MOVED:
    ws.cell(r, 2, csi).font = BLK
    ws.cell(r, 3, name).font = BLK
    for col, v in ((4, a), (5, b), (6, b - a)):
        c = ws.cell(r, col, v); c.number_format = CUR
        c.font = GRN if col == 6 and b > a else (BLK if col < 6 else BLK)
    if b == 0 and a == 0:
        for col in range(2, 7): ws.cell(r, col).fill = PNK
    c = ws.cell(r, 7, notes.get(csi, '')); c.font = SM; c.alignment = wr()
    r += 1

# ============================================== 6. ZERO-QUANTITY REGISTER
ws = wb.create_sheet('Zero Quantity Register')
for col, w in zip('ABCDEF', [3, 10, 62, 10, 10, 16]): ws.column_dimensions[col].width = w
r = head(ws, 'SCOPE THAT CARRIES A UNIT PRICE AND A QUANTITY OF ZERO')
ws.cell(r, 2, 'This is what the $12,000,000 "Trade Costs To Be Priced" plug stands in for. '
              'Each line has his rate on it already — it only needs a quantity.').font = SM
r += 2
r = hrow(ws, r, ['CSI', 'Description', 'Qty', 'Unit', 'His rate'])
n = 0
for csi, dn, item, desc, qty, unit, rate, tot, note in R.LINES:
    try: t = float(tot)
    except (TypeError, ValueError): t = 0.0
    try: rt = float(rate)
    except (TypeError, ValueError): rt = 0.0
    if t == 0 and rt > 0:
        n += 1
        ws.cell(r, 2, csi).font = BLK
        c = ws.cell(r, 3, desc); c.font = BLK; c.alignment = wr()
        ws.cell(r, 4, 0).font = RED
        ws.cell(r, 5, unit).font = BLK
        c = ws.cell(r, 6, rt); c.number_format = CUR2; c.font = BLUE
        r += 1
r += 1
ws.cell(r, 3, f'{n} lines').font = BOLD
ws.cell(r, 3).border = TOPB

# ==================================================== 7. QUESTIONS FOR THOMAS
ws = wb.create_sheet('Questions for Thomas')
for col, w in zip('ABC', [3, 56, 96]): ws.column_dimensions[col].width = w
r = head(ws, 'THE ELEVEN QUESTIONS')
ws.cell(r, 2, 'Every one of these is answerable from his own workbook. None of them accuses him '
              'of padding — and he has not padded. He has made four mechanical mistakes and '
              'priced a programme nobody has settled yet.').font = SM
ws.row_dimensions[r].height = 24; r += 2
r = hrow(ws, r, ['Ask', 'Why'])
for q, why in S.ASKS:
    c = ws.cell(r, 2, q); c.font = BOLD; c.alignment = wr()
    c = ws.cell(r, 3, why); c.font = BLK; c.alignment = wr()
    ws.row_dimensions[r].height = max(30, 11 * (len(why) // 88 + 1) + 14)
    r += 1

for sheet in wb.worksheets:
    sheet.sheet_view.showGridLines = False
    sheet.freeze_panes = 'A7'
wb.properties.title = '165 Randolph - Sept 16 GC Estimate Audit'
wb.calculation.fullCalcOnLoad = True
OUT = '165_Randolph_Audit_of_Sept16_GC_Estimate.xlsx'
wb.save(OUT)
print('wrote', OUT)
