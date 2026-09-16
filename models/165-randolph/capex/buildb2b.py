# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
import b2b, sept16_raw as R
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

F = 'Arial'
BLK = Font(name=F, size=9);                  BOLD = Font(name=F, size=9, bold=True)
RED = Font(name=F, size=9, bold=True, color='C00000')
GRN = Font(name=F, size=9, bold=True, color='1F6B3B')
BLU = Font(name=F, size=9, color='0000FF')
H1  = Font(name=F, size=18, bold=True, color='1F3864')
H2  = Font(name=F, size=11, bold=True, color='1F3864')
WHT = Font(name=F, size=9, bold=True, color='FFFFFF')
SM  = Font(name=F, size=8, color='595959')
BIG = Font(name=F, size=14, bold=True, color='1F3864')
HDR = PatternFill('solid', fgColor='1F3864'); GPF = PatternFill('solid', fgColor='D9E2F3')
PNK = PatternFill('solid', fgColor='FCE4E4'); GRF = PatternFill('solid', fgColor='E2EFDA')
GRY = PatternFill('solid', fgColor='F2F2F2')
thin = Side(style='thin', color='D0D0D0'); med = Side(style='medium', color='1F3864')
TOPB = Border(top=med)
CUR = '$#,##0;($#,##0);"-"'
def wr(): return Alignment(wrap_text=True, vertical='top')
SF = b2b.SF

wb = Workbook()
def head(ws, sub):
    ws.cell(2, 2, '165 RANDOLPH STREET').font = H1
    ws.cell(3, 2, sub).font = H2
    ws.cell(4, 2, 'Building to building · every markup, soft cost and FF&E stripped from '
                  'BOTH sides · 16 Sep 2026 estimate vs our V2 · CONFIDENTIAL').font = SM
    return 6
def hrow(ws, r, cols):
    for i, h in enumerate(cols, 2):
        c = ws.cell(r, i, h); c.font = WHT; c.fill = HDR
        c.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    return r + 1

# ======================================================= 1. THE COMPARISON
ws = wb.active; ws.title = 'Building to Building'
for col, w in zip('ABCDEFG', [3, 46, 15, 15, 15, 8, 92]): ws.column_dimensions[col].width = w
r = head(ws, 'JUST THE BRICKS, STEEL, PIPE AND WIRE')
ws.cell(r, 2, 'He is $%s over us on physical work — %s' %
        (f'{b2b.HIS_ALL - b2b.OURS:,.0f}', f'{(b2b.HIS_ALL-b2b.OURS)/b2b.OURS:+.1%}')).font = BIG
r += 2
for t in [
  'No general conditions. No overhead, profit or insurance. No contractor contingency, no '
  'project contingency, no escalation. No soft costs, no FF&E, no off-site parking garage. '
  'Both budgets, same treatment.',
  '',
  'Our column ties to the $38,166,123 trade cost our own V2 workbook publishes, to the dollar. '
  'His column ties to his own $37,945,960 trade cost less the general-conditions content and '
  'preconstruction that come off both sides, plus the $1,483,680 of abatement he carries as a '
  'soft cost and we carry as a trade.']:
    c = ws.cell(r, 2, t); c.font = BLK; c.alignment = wr()
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=7)
    ws.row_dimensions[r].height = 26 if len(t) > 150 else (13 if t else 7)
    r += 1
r += 1
r = hrow(ws, r, ['Work package', 'OURS', 'HIS', 'Delta', 'His CSI', 'What is going on'])
for name, o, h, csi, note in b2b.WP:
    ws.cell(r, 2, name).font = BLK
    for col, v in ((3, o), (4, h), (5, h - o)):
        c = ws.cell(r, col, v); c.number_format = CUR
        c.font = (RED if h > o else GRN) if col == 5 else BLK
    if h == 0: ws.cell(r, 4).fill = PNK
    ws.cell(r, 6, csi).font = SM
    c = ws.cell(r, 7, note); c.font = BLK; c.alignment = wr()
    ws.row_dimensions[r].height = max(40, 10.5 * (len(note) // 95 + 1))
    r += 1
for lab, o, h, note in [
  ('PHYSICAL WORK — priced lines only', b2b.OURS, b2b.HIS,
   'His priced lines come to LESS than our entire budget.'),
  ('+ his "Trade Costs To Be Priced"', 0, b2b.PLUG,
   'The plug standing in for everything above that he left at zero quantity.'),
  ('BUILDING TO BUILDING', b2b.OURS, b2b.HIS_ALL, '')]:
    tot = lab.startswith('BUILDING')
    c = ws.cell(r, 2, lab); c.font = BOLD; c.border = TOPB; c.fill = GPF if tot else GRY
    for col, v in ((3, o), (4, h), (5, h - o)):
        c = ws.cell(r, col, v); c.number_format = CUR; c.font = BOLD
        c.border = TOPB; c.fill = GPF if tot else GRY
    ws.cell(r, 6).fill = GPF if tot else GRY; ws.cell(r, 6).border = TOPB
    c = ws.cell(r, 7, note); c.font = SM; c.alignment = wr()
    c.fill = GPF if tot else GRY; c.border = TOPB
    r += 1
r += 1
for lab, v in [('$ per SF on 74,100 SF — ours', b2b.OURS / SF),
               ('$ per SF on 74,100 SF — his', b2b.HIS_ALL / SF)]:
    ws.cell(r, 2, lab).font = BLK
    c = ws.cell(r, 3, v); c.number_format = '$#,##0'; c.font = BOLD; r += 1

# ============================================== 2. WHERE THE GAP SITS
ws = wb.create_sheet('Where the Gap Sits')
for col, w in zip('ABCD', [3, 54, 18, 96]): ws.column_dimensions[col].width = w
r = head(ws, 'THE GAP IS NOT ONE THING — IT IS THREE, AND THEY MEAN DIFFERENT THINGS')
ws.cell(r, 2, 'Never net these together. One says negotiate the price down, one says fund scope back '
              'in, and one is a decision we owe him. Three different actions.').font = SM
r += 2
r = hrow(ws, r, ['', 'Amount', 'Note'])
for lab, v, note in b2b.SPLIT:
    tot = lab.startswith('BUILDING')
    c = ws.cell(r, 2, lab); c.font = BOLD if tot else BLK
    c2 = ws.cell(r, 3, v); c2.number_format = CUR
    c2.font = BOLD if tot else (RED if v > 0 else GRN)
    c3 = ws.cell(r, 4, note); c3.font = BLK; c3.alignment = wr()
    if tot:
        for col in (2, 3, 4): ws.cell(r, col).border = TOPB; ws.cell(r, col).fill = GPF
    ws.row_dimensions[r].height = 28
    r += 1
r += 2
ws.cell(r, 2, 'THE POINT').font = H2; r += 1
for t in ['His $12,000,000 plug covers scope we price at $%s. It is right-sized — do not '
          'negotiate that line, ask him to price it.' % f'{-b2b.UNPRICED:,.0f}',
          '',
          'The real argument is the $%s he is over on scope we BOTH priced. Scaffolding alone is '
          '$4,731,738 of it.' % f'{b2b.OVER:,.0f}',
          '',
          'And $%s of the difference is two decisions nobody has made yet: lift the roof or '
          'replace it, and how much acoustic treatment the licence actually needs. Those get '
          'settled with Wake and Rooflifters, not with Thomas.' % f'{-b2b.JUDGEMENT:,.0f}']:
    c = ws.cell(r, 2, t); c.font = BOLD if t.startswith('The real') else BLK; c.alignment = wr()
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=4)
    ws.row_dimensions[r].height = 15 if t else 7
    r += 1

# ============================================== 3. WHAT CAME OFF BOTH SIDES
ws = wb.create_sheet('What Came Off')
for col, w in zip('ABCDE', [3, 44, 44, 18, 44]): ws.column_dimensions[col].width = w
r = head(ws, 'EVERYTHING STRIPPED OUT, AND WHERE IT LIVES INSTEAD')
r += 1
r = hrow(ws, r, ['Stripped from his budget', 'His cell', 'Amount', 'How we carry it'])
t = 0
for lab, cell, v, ours in b2b.STRIPPED:
    t += v
    ws.cell(r, 2, lab).font = BLK
    ws.cell(r, 3, cell).font = SM
    c = ws.cell(r, 4, v); c.number_format = CUR; c.font = BLK
    c = ws.cell(r, 5, ours); c.font = BLK; c.alignment = wr()
    r += 1
ws.cell(r, 2, 'TOTAL STRIPPED FROM HIS $89,084,591').font = BOLD
c = ws.cell(r, 4, t); c.number_format = CUR; c.font = BOLD; c.border = TOPB
ws.cell(r, 2).border = TOPB; r += 2
ws.cell(r, 2, 'Added back to his physical column').font = H2; r += 1
ws.cell(r, 2, 'Abatement, which he carries as a soft cost and we carry as a trade').font = BLK
c = ws.cell(r, 4, 1_483_680.0); c.number_format = CUR; c.font = BLK; r += 2
assert abs(R.TOTAL - t + 1_483_680.0 - b2b.HIS_ALL) < 1.0
ws.cell(r, 2, '$89,084,591 − $%s stripped + $1,483,680 of abatement = $%s of physical work. His $12,000,000 plug was never stripped — it is inside that number already.'
        % (f'{t:,.0f}', f'{b2b.HIS_ALL:,.0f}')).font = BOLD

# ===================================================== 4. THE ISSUES
ISSUES = [
("HIS","Scaffolding is the single biggest package gap in the file",
 "$6,170,000 against our $1,438,262. A $4,000,000 sidewalk bridge lump with his own backup "
 "rows footing to $2,589,800 directly beneath it, plus $2,000,000 of interior scaffolding.",
 "Ask which of his two numbers is right. Then ask how many linear feet of actual public "
 "sidewalk this building has — a shed is only required where there is one, and the alleys "
 "and interior lot lines do not have one."),
("HIS","Structural steel is $0 on a project scoped 'Add Second Level'",
 "All nineteen lines of division 055100 are zero quantity: roof trusses and columns at "
 "$6,000/TON, mezzanine framing at $6,000/TON, balcony framing, stage lighting and AV support "
 "structure at $8.00/LB, railings, stairs, dunnage, lintels. We carry $5,827,740 of it.",
 "This is the biggest single thing his $12M plug has to absorb. His own $8.00/LB rate is good "
 "— our rigging grid works out to $9.21/LB, so he corroborates us within 15%."),
("NEITHER","The $12,000,000 plug is right-sized — leave it alone",
 "The scope he left at zero or barely touched is scope we price at $%s. His plug is "
 "$12,000,000, so it covers it with about $%s of headroom."
 % (f'{-b2b.UNPRICED:,.0f}', f'{b2b.PLUG + b2b.UNPRICED:,.0f}'),
 "The instinct is to attack the biggest round number in the file. Don't. It is the one "
 "line in his budget that is about right. Ask him to PRICE it, not cut it — and when "
 "he does, the number that changes is the trade cost, not the plug."),
("BOTH","We are building two different roofs",
 "He demolishes 74,000 SF of pre-cast roof at $8/SF and lays 56,085 SF of new membrane at "
 "$36/SF. We lift the existing roof on the lifter's towers, extend the columns and clad a new "
 "30 ft band — $3.5M contract plus surrounding work.",
 "SETTLE THIS FIRST. It moves concrete, steel, scaffolding, demolition and roofing all at once, "
 "and nothing else in either budget can be reconciled until it is decided."),
("HIS","Finishes are 4x ours — and he is probably right",
 "$3,509,501 against our $866,500: stone $764,340, resilient $765,048, floor prep $515,298, "
 "wood $373,050, paint $1,091,765.",
 "PROGRAMME, NOT ERROR. He is pricing a restaurant, VIP lounges and a foundry off the test fit. "
 "Some of it is the 135,953 SF mistake (paint is 135,953 x $5), but most is finish level. That "
 "conversation is with Wake and with us, not with him."),
("HIS","Plumbing is 2.1x ours and one of us has the fixture count wrong",
 "$3,717,250 against our $1,757,502. 178 water closets, 154 lavatories and 51 urinals at "
 "$4,000 each, nine bars roughed, a $125,000 restaurant grease trap.",
 "GET THE ARCHITECT'S CODE FIXTURE CALCULATION. This is settleable with arithmetic in an "
 "afternoon and it is worth $2M. Our number may be the light one."),
("OURS","Acoustics is under-carried by him",
 "$581,802 of K13 against our $1,864,000.",
 "Ours is not decoration — it is the licence to operate next to residential. Do not let "
 "this one get value-engineered because his number is lower."),
("HIS","Concrete and foundations are effectively $0",
 "$177,450 against our $1,476,450. Every footing line, the stage platform slab, the mezzanine "
 "deck pour and the column base grouting are all zero quantity.",
 "Follows directly from the steel being zero. Same plug."),
("HIS","Every bar in the building is priced at zero",
 "Division 064000: lobby, VIP, music hall GA, mezzanine, balcony, upper lounge, lower lounge "
 "and foundry bars, all at $2,000/LF with no linear feet against them. But his PLUMBING carries "
 "nine bars roughed at $30,000 each.",
 "His own plumbing sheet knows there are nine bars. Give him the linear feet off the test fit "
 "and the millwork prices itself."),
("HIS","$1,000,000 of coat check lockers sits inside specialties",
 "2,000 EA at $500, note '333LF'. That serves 27% of a 7,440-capacity house at once, at a rate "
 "for a gym locker bank.",
 "750 at $350 is a generous January coat check. Worth $737,500."),
("BOTH","HVAC matching is a coincidence, not agreement",
 "$5,964,390 his, $5,950,650 ours. His is ONE LINE — 132,542 SF x $45.00, no tonnage, no "
 "load, on an area this building does not have. Ours is built off the occupancy load.",
 "Two wrong methods landing in the same place. Get tons from the mechanical engineer before "
 "either number is trusted."),
("HIS","Abatement is in his soft costs, not his trade cost",
 "$1,483,680 under soft costs. We carry $1,000,750 as a trade.",
 "Not an error, just a different home — but it matters, because abatement is physical work "
 "and it belongs in the comparison. Both numbers are guesses until the ACP-5 survey is done."),
("OURS","Elevators — his number is better built than ours",
 "4 lobby stops + 2 stage stops at $75,000 plus a hydraulic lift = $480,000. Ours is a "
 "$300,000 allowance.",
 "Take his. Ours is a placeholder and his has stops behind it."),
("OURS","VESDA — he is right and we do not carry it",
 "$250,000 for aspirating smoke detection in the music hall.",
 "A 50 ft clear volume with haze and pyro needs it. Add it to ours."),
("OURS","Sitework — we under-carry",
 "$346,335 against our $90,000: 8,295 SF of sidewalk repair, trees, fencing and a 2,380 SF "
 "fire-escape egress route at $75/SF.",
 "His is the real number. Ours is an allowance."),
]
ws = wb.create_sheet('The Issues')
for col, w in zip('ABCDE', [3, 11, 52, 78, 78]): ws.column_dimensions[col].width = w
r = head(ws, 'THE ISSUES, BUILDING TO BUILDING')
ws.cell(r, 2, 'HIS = his number needs to move. OURS = ours does. BOTH = a decision neither of us can '
              'make alone. NEITHER = leave it exactly where it is.').font = SM
r += 2
r = hrow(ws, r, ['Whose', 'Issue', 'The evidence', 'What to do'])
for whose, title, ev, act in ISSUES:
    c = ws.cell(r, 2, whose)
    c.font = RED if whose == 'HIS' else (GRN if whose == 'OURS' else BOLD)
    c.alignment = Alignment(horizontal='center', vertical='top')
    c = ws.cell(r, 3, title); c.font = BOLD; c.alignment = wr()
    c = ws.cell(r, 4, ev); c.font = BLK; c.alignment = wr()
    c = ws.cell(r, 5, act); c.font = BLK; c.alignment = wr()
    ws.row_dimensions[r].height = max(44, 10.5 * (max(len(ev), len(act)) // 80 + 1))
    r += 1

for s in wb.worksheets:
    s.sheet_view.showGridLines = False
    s.freeze_panes = 'A7'
wb.properties.title = '165 Randolph - Building to Building'
wb.calculation.fullCalcOnLoad = True
OUT = '165_Randolph_Building_to_Building_Ours_vs_His.xlsx'
wb.save(OUT)
print('wrote', OUT)
