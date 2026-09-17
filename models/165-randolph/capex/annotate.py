# -*- coding: utf-8 -*-
"""Put our questions ON Thomas's own workbook.

Loads the 16 Sep Master Development Budget untouched, adds one column per
sheet headed OUR QUESTION / ANALYSIS, writes a question beside every line we
have one for, highlights the cell it refers to, and adds a front sheet that
indexes them and states our numbers against his. None of his cells change.
"""
import openpyxl, re
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter as L

SRC = "source/260916_Master_Development_Budget_165_Randolph.xlsx"
OUT = "165_Randolph_MDB_260916_with_MT_Questions.xlsx"
wb = openpyxl.load_workbook(SRC)

F = "Arial"
Q  = Font(name=F, size=9, color="1F3864")
QB = Font(name=F, size=9, bold=True, color="1F3864")
H  = Font(name=F, size=9, bold=True, color="FFFFFF")
HF = PatternFill("solid", fgColor="1F3864")
YEL = PatternFill("solid", fgColor="FFF2CC")
PNK = PatternFill("solid", fgColor="FCE4E4")
WRAP = Alignment(wrap_text=True, vertical="top")
INDEX = []   # (sheet, cell, his text, question)

def head(ws, col, row):
    c = ws.cell(row, col, "OUR QUESTION / ANALYSIS  (MT, 17 Sep)")
    c.font = H; c.fill = HF; c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.column_dimensions[L(col)].width = 78

def note(ws, row, col, text, mark=None, his=None, fill=YEL):
    from openpyxl.cell.cell import MergedCell
    while isinstance(ws.cell(row, col), MergedCell): col += 1   # step past merged ranges
    c = ws.cell(row, col, text); c.font = Q; c.alignment = WRAP
    ws.row_dimensions[row].height = max(ws.row_dimensions[row].height or 15, 12 * (len(text) // 95 + 1))
    if mark:
        for m in (mark if isinstance(mark, (list, tuple)) else [mark]):
            ws[m].fill = fill
    INDEX.append((ws.title, mark[0] if isinstance(mark, (list, tuple)) else (mark or f"row {row}"),
                  his or "", text))

def find(ws, col, pattern, start=1):
    rx = re.compile(pattern, re.I)
    for r in range(start, ws.max_row + 1):
        v = ws.cell(r, col).value
        if v is not None and rx.search(str(v)): return r
    raise KeyError(pattern)

def find_item(ws, csi, pattern):
    """Row whose description matches `pattern` inside CSI division `csi` on the Breakdown sheet.
    Item numbers in column A are formulas (=A13+1), so match on the description instead."""
    r = find(ws, 1, rf"^{csi}$")
    rx = re.compile(pattern, re.I)
    for rr in range(r + 1, ws.max_row + 1):
        a = ws.cell(rr, 1).value
        if isinstance(a, str) and re.fullmatch(r"\d{6}", a.strip()): break
        b = ws.cell(rr, 2).value
        if b is not None and rx.search(str(b)): return rr
    raise KeyError((csi, pattern))

# ======================================================== BUDGET SUMMARY
ws = wb["Budget Summary"]; C = 12; head(ws, C, 19)
note(ws, 21, C, "Formula is =86*25000 but the label says 260 spaces. Which is right? And is off-site parking in this deal at all? We carry none.", "D21", "Parking Garage - 260/spaces")
note(ws, 26, C, "What scope is inside the $12,000,000, and when can it be priced? Our measured structure alone is $16,710,249 (997.2 short tons off the RFEM takeoff), and this plug also has to cover millwork, doors, glazing, tile, fireproofing and drywall. We expect it to go UP when priced.", "D26", "Trade Costs To Be Priced")
note(ws, 27, C, "$3,141,000 here PLUS $3,034,000 of division 013000 inside the trade cost = $6,175,000, 12.36% of trade. Schimenti ran 7.80% and 8.90% at 555 Johnson. Which is the one we are paying? We hold 8.5%.", "D27", "General Conditions")
note(ws, 28, C, "=SUM(D25:D27)*0.09 charges the 9% on trade + the $12M plug + general conditions. Fee on your own GC is $555,750; fee on unpriced scope is $1,080,000. Can the fee be a fixed dollar amount, and come off both?", "D28", "OH&P 9%")
note(ws, 29, C, "=SUM(D25:D28)*0.1 is 10% on a base that already holds the 9% OH&P. Intentional? We hold ONE owner contingency of $5,000,000 below the line.", "D29", "Contractor Contingency 10%")
note(ws, 30, C, "Blank in all three versions of this file, while the parking garage gets 5% on D22. On a 20-month programme what should the building carry? We hold 10%.", "D30", "Escalation", PNK)
note(ws, 31, C, "I31 divides by 135,953. On the 74,100 SF footprint this is $859/SF.", "I31", "$/SF")
note(ws, 45, C, "This is our own team, not Live Nation. Same $520,000 in our budget - just the label.", "D45", "Project Management (Live Nation)")
note(ws, 67, C, "Label says Soft Costs & FFE. Formula is =(D23+D31+D47+D65)*0.1 = 10% of the WHOLE PROJECT, on top of the contractor contingency already inside D31. As labelled it would be $1,507,723. $578,648 of it is contingency on contingency. Which is intended?", "D67", "Soft Costs & FFE Contingency 10%", PNK)
note(ws, 69, C, "Ours: V3 $77,897,555 on the same programme, measured steel. Apply only the corrections that survive the takeoff and this cell becomes about $77,247,828 - 0.8% from ours.", "D69", "Total Capital")
note(ws, 71, C, "Divides by 135,953 SF. Where does that number come from? We cannot find a schedule or calculation behind it. On 74,100 SF this total is $1,202/SF. Both are true; please label which.", ["D71", "I71"], "$ PER SF")
note(ws, 8, C, "135,953 SF appears here and in 6 formula cells. Source? The RFEM model has 146,508 SF gross / 120,119 SF enclosed floor; the test fit governs at 74,100 SF footprint. 555 Johnson at $208.63/SF is 134,993 SF - please rule that out.", "B8", "SF: 135,953")
note(ws, 9, C, "Dated 7 Sep; the Breakdown tab says 16 Sep. Which is current?", "A9")

# ============================================================ GENERAL CONDITIONS
ws = wb["General Conditions"]; C = 7; head(ws, C, 2)
note(ws, 3, C, "This tab is the best-evidenced page in the file and we would rather build on it than argue with it. Is the $3,141,000 the ONLY place general conditions lives? Division 013000 on the Breakdown carries site office, field tech, safety, toilets, protection, clean-up, rubbish and final clean for another $3,034,000.", "E13")
note(ws, 4, C, "90 weeks - is that construction only, or does it include pre-con and closeout? Can we see it as a rate x duration so that shortening the programme visibly shortens the cost?", "C4")
note(ws, 9, C, "Three superintendents for the full 90 weeks each - all three for the whole period, or overlapping phases?", ["C9", "C10", "C11"])

# ================================================ BUILDING & FIT-OUT BREAKDOWN
ws = wb["Building & Fit-out Breakdown"]; C = 11; head(ws, C, 10)
r = find_item(ws, "013000", r"^Project Labor"); note(ws, r, C, "Crew, rate and weeks? The General Conditions tab already funds three supers + a general super for 90 weeks. No quantity behind this line.", f"F{r}", "Project Labor $2,000,000", PNK)
r = find_item(ws, "013000", r"^Field Tech");  note(ws, r, C, "What is included in Field Technology at $200,000?", f"F{r}")
r = find(ws, 1, r"^013000$"); r2 = find(ws, 1, r"^Sub Total", r); note(ws, r2, C, "All of this division reads as general conditions. Is it meant to sit inside trade cost AND under the GC line on the summary? We think it is one function in two places.", f"F{r2}", "013000 subtotal $3,034,000")
r = find_item(ws, "015800", r"^Install sidewalk bridge");  note(ws, r, C, "The lump says $4,000,000. The two rows beneath it - 1,126 LF @ $500 and 27,024 SF @ $75 - foot to $2,589,800. Which is right? And how many LF of PUBLIC sidewalk does the building front? A shed is only required where there is one; the alleys and lot lines have none. We carry 1,089 LF perimeter x $210 erected + 24 months rental.", f"F{r}", "Sidewalk bridge $4,000,000", PNK)
r = find_item(ws, "015800", r"^Interior scaffolding");  note(ws, r, C, "What is being staged, at what rate, for how many weeks? The high roof is only 8.65 lb/SF of short-span W12/W6 framing - not a heavy erection. And the ground-supported stage and production towers are erected FIRST; can they carry the access instead of renting it twice?", f"F{r}", "Interior scaffolding $2,000,000")
r = find_item(ws, "024100", r"^Demo Pre-cast concrete roof"); note(ws, r, C, "Confirms the REBUILD method, which the RFEM model also uses and which we now accept. Separate question: is the existing roof genuinely pre-cast concrete? It decides whether a PARTIAL lift over the 27,393 SF high-roof zone is even possible.", f"F{r}", "Demo pre-cast roof 74,000 SF")
r = find(ws, 1, r"^033000$"); r2 = find(ws, 1, r"^Sub Total", r); note(ws, r2, C, "Nearly every line zero quantity - no footings, no stage slab, no mezzanine deck pour, no base-plate grout. The takeoff gives 124 footing locations (up from 81 in Rev 43). We carry $2,543,000 of foundations.", f"F{r2}", "033000 subtotal $177,450")
r = find(ws, 1, r"^055100$"); r2 = find(ws, 1, r"^Sub Total", r)
note(ws, r2, C, "ALL 19 LINES ZERO. The RFEM takeoff (VE1) gives 997.2 SHORT TONS: beams/girders 508.4, columns 360.6, trusses 67.7, braces 40.2, CFS 20.3 (11,557 LF). Please price off the lb column - the file's 't' column is metric tonnes (904.6) and using it understates steel by 10.2%. Your own $6,000/TON on line 2 is right for rolled framing.", f"F{r2}", "055100 STRUCTURAL STEEL $0", PNK)
r = find_item(ws, "055100", r"^F&I new Roof Trusses"); note(ws, r, C, "202.0 tons of the columns are BUILT-UP PLATE GIRDERS (I 48/24 through I 69.023/24, 60 LF each on grids B and E), not rolled shapes. Does $6,000/TON apply to shop-welded plate? We carry $8,400.", f"E{r}", "Trusses/girders/columns @ $6,000/TON")
r = find_item(ws, "055100", r"^Stage Lighting & AV support"); note(ws, r, C, "Your $8.00/LB here corroborates our ground-supported rigging grid, which works out to $9.21/LB. Note: the stage carries the rigging, not the roof. Please confirm the roof design loads EXCLUDE production rigging.", f"E{r}", "Stage lighting & AV support @ $8/LB")
r = find(ws, 1, r"^064000$"); r2 = find(ws, 1, r"^Sub Total", r); note(ws, r2, C, "Every bar and back bar at $2,000/LF with no linear feet - but 220000 already carries NINE bars roughed at $30,000 each. Nate can give you the LF off the test fit. We carry $510,500 of millwork.", f"F{r2}", "064000 MILLWORK $0", PNK)
r = find(ws, 1, r"^078100$"); r2 = find(ws, 1, r"^Sub Total", r); note(ws, r2, C, "All three lines zero at $5.00/SF. On ~107,000 SF of new deck and roof that is about $536,000 at your own rate.", f"F{r2}", "078100 FIREPROOFING $0")
r = find(ws, 1, r"^081000$"); r2 = find(ws, 1, r"^Sub Total", r); note(ws, r2, C, "Zero, including every acoustical door and pair into the music hall at $10,000 / $20,000. We carry $546,800.", f"F{r2}", "081000 DOORS $0")
r = find(ws, 1, r"^084100$"); r2 = find(ws, 1, r"^Sub Total", r); note(ws, r2, C, "Zero. We carry $292,000 for storefront and glazing together.", f"F{r2}", "084100 STOREFRONT $0")
r = find(ws, 1, r"^092000$"); r2 = find(ws, 1, r"^Sub Total", r); note(ws, r2, C, "9 of 10 lines zero. $119,664 looks like a fraction of a room needing sound-rated separation between a 7,440-capacity hall and everything else. We carry $1,019,276.", f"F{r2}", "092000 DRYWALL $119,664")
r = find(ws, 1, r"^100000$"); rr = find(ws, 2, r"Coat Check Lockers", r); note(ws, rr, C, "2,000 lockers serves 27% of a 7,440 house at once, at a gym-locker rate. Is 2,000 right? 750 @ $350 is a generous January coat check. Worth $737,500 at trade.", f"F{rr}", "Coat Check Lockers 2,000 @ $500", PNK)
r = find(ws, 1, r"^100500$"); r2 = find(ws, 1, r"^Sub Total", r); note(ws, r2, C, "$581,802 of K13 against our $1,864,000 of acoustic treatment. Next to residential this is the licence to operate. What is the acoustic performance target this was priced to?", f"F{r2}", "100500 ACOUSTICAL $581,802")
r = find(ws, 1, r"^142000$"); r2 = find(ws, 1, r"^Sub Total", r); note(ws, r2, C, "No question - 4 lobby + 2 stage stops @ $75,000 plus a hydraulic lift is better built than our $300,000 allowance. We are adopting yours.", f"F{r2}", "142000 ELEVATOR $480,000")
r = find(ws, 1, r"^210000$"); rr = find(ws, 2, r"2nd Floor Extend Sprinkler", r); note(ws, rr, C, "50,000 SF. The RFEM model measures the mezzanine at 32,942 SF + 13,077 SF tiered seating = 46,019 SF. Close - can you confirm the basis?", f"C{rr}", "2nd floor sprinklers 50,000 SF")
rr = find(ws, 2, r"First Floor Rework Existing Fire Protection", r); note(ws, rr, C, "69,000 SF - the footprint is 74,100 SF. Should this be higher?", f"C{rr}")
r = find(ws, 1, r"^220000$"); rr = find(ws, 2, r"^W/C 1st Fl", r); note(ws, rr, C, "178 WC + 154 lavs + 51 urinals across the building at $4,000 each. Can we see the CODE FIXTURE CALCULATION behind the count? We are at $1,757,502 vs your $3,717,250 and one of us is wrong - settleable in an afternoon.", f"C{rr}", "Fixture counts")
rr = find(ws, 2, r"F&I Bar roughing", r); note(ws, rr, C, "Nine bars roughed here - so the building knows it has nine bars, but 064000 prices none of them.", f"C{rr}")
r = find(ws, 1, r"^230000$"); rr = find(ws, 2, r"HVAC System including BMS", r); note(ws, rr, C, "ONE LINE, 132,542 SF x $45.00, no tonnage. Was this priced on a LOAD or an AREA? A 64 ft clear room with 7,440 people is a volume and occupancy load. Can we see tons and the basis? Ours is $5,950,650 built from load - almost the same total, which is a coincidence not agreement.", f"F{rr}", "HVAC 132,542 SF @ $45")
r = find(ws, 1, r"^260000$"); rr = find(ws, 2, r"I/O lighting package", r); note(ws, rr, C, "'PROVIDED BY OTHERS' - is this yours or ours? FF&E line 310 separately carries $1,750,000 of Architectural & Exterior Lighting. That is $3,381,436 of architectural lighting in one budget. Keep the conduit and wiring here, delete the fixtures?", f"F{rr}", "I/O lighting package $1,631,436", PNK)
rr = find(ws, 2, r"4000A 208Y/120V Switchboard", r); note(ws, rr, C, "Two 4,000A boards = 8,000A service, matches our sizing. Is this confirmed with Con Ed - is there a feasibility letter?", f"F{rr}")
rr = find(ws, 2, r"Con Edison customer contribution", r); note(ws, rr, C, "$250,000 allowance - has Con Ed responded on the 8,000A service and the vault?", f"F{rr}")
r = find(ws, 1, r"^283100$"); rr = find(ws, 2, r"Vesda", r); note(ws, rr, C, "Adopting this. We had not carried VESDA and you are right that a 64 ft volume with haze and pyro needs it.", f"F{rr}")
rr = find(ws, 2, r"^F&I Fire alarm system", r); note(ws, rr, C, "135,953 SF basis - see the area question on the summary sheet.", f"C{rr}")

# ============================================== SOFT COST & FF&E BUDGET DETAIL
ws = wb["Soft Cost & FF&E Budget Detail"]; C = 7; head(ws, C, 11)
def sc(pat, text, mark_col="E", start=1, fill=YEL, his=None):
    r = find(ws, 2, pat, start); note(ws, r, C, text, f"{mark_col}{r}", his, fill); return r
sc(r"^Roof Abatement", "70,000 SF @ $21 = $1,470,000. Where does $21/SF come from, and has anyone SAMPLED the roof? No ACP-5 exists. We carry $7.50/SF. Also: this sits in soft costs; we carry abatement as a trade.", his="Roof Abatement", fill=PNK)
sc(r"^Architecture & Engineering$", "One $3,100,000 lump with architecture, MEP and structural all 'carried in line #3'. Can it be split? We cannot tell whether structural is funded at the level the RFEM model needs.", his="A&E $3,100,000")
sc(r"Sound and Vibration Testing", "$15,000 is testing. Is there an acoustic DESIGN fee anywhere? We carry $200,000 - next to residential it is the licence to operate.", his="Acoustical $15,000")
sc(r"Permit fees & plan review", "1.3% of trade cost - understood, so this falls automatically as trade moves. Is 1.3% right for a project filing an ST structural permit at +64 ft 6 in? We carry a separate $120,000 for the ST filing and expediting; we cannot find it here.", his="Permit fees 1.3%")
sc(r"SLA Legal Fees carried", "Attorney fees $0. Is the SLA application, the cabaret question and the theater use-classification filing genuinely inside the $342,000 already spent? On a comparable project the liquor licence was approved at zero and came in at $250,000. We carry $250,000.", his="Attorney Fees $0", fill=PNK)
sc(r"^Controlled inspections", "$50,000 on a job with new structural steel, welding, fireproofing, sprinklers and a new 8,000A service. We carry $140,000. Does this cover NYC special inspections?", his="Controlled inspections $50,000")
sc(r"^Project Management$", "Same $500,000 in our budget - no question on the number. Only the '(Live Nation)' label on the summary sheet; this is our team.", his="Project Management")
sc(r"^Theater Ground Floor GA", "3,714 @ $125 = $464,250, plus 657 box chairs @ $300 below. HOLDING - seat count is a licensing determination (theater classification drives the liquor licence) and counsel has not ruled. Not a pricing disagreement. We carry 720 removable @ $25.", his="GA folding chairs", fill=YEL)
r = sc(r"^Kitchen Equipment$", "Your note above - '* BPT: 26 POS / Prep Kitchen / 1 Walk-in Cooler $837K' - is the most useful line in the file. Against it, 74 bar positions here at $9,000 = $666,000 looks LIGHT to us, and so do our 53. Is it?", his="Bar & kitchen equipment")
sc(r"^Freight & Installation", "$375,000 is 40% of the equipment above it. Freight and install only, or does it carry something else?", his="Freight & Installation $375,000")
sc(r"^Metal Detectors", "1 allowance, $70,000 - how many screening lanes does that buy? We carry 12 walk-through units for a 7,440 house.", his="Metal Detectors")
sc(r"^All soft goods", "$500,000, and the note excludes the mezzanine-edge cutdown drape. Your own benchmark note on the Production subtotal says Soft Goods $725k. Which is right? We are at $220,000 and think we are light.", his="Soft goods $500,000")
sc(r"^Upstage Video Wall", "Blank, note $1,400/SF. Confirming you also intend both video walls OUT of this budget (Phase 2, artists bring their own)?", mark_col="B", his="Video walls")
sc(r"^House Sound System", "$1,400,000 'includes Theater / VIP / Restaurant & Roof'. Your benchmark note says Audio $690k. We carry $2,200,000 and want to be challenged on it - do you have a vendor who will quote a house PA for a 7,440 room?", his="House Sound System")
sc(r"^Performance Lighting$", "$520,000 against your benchmark note of $450k. We are at $340,000 and probably light.", his="Performance Lighting")
sc(r"^Architectural & Exterior Lighting", "$1,750,000 here AND $1,631,436 of 'I/O lighting package PROVIDED BY OTHERS' inside the electrical trade (260000). Bought twice? Which one survives?", his="Architectural lighting $1,750,000", fill=PNK)
r = find(ws, 2, r"^Misc. Equipment \$60K|Misc\. Equipment", 1) if False else None
try:
    rr = find(ws, 6, r"Misc\. Equipment \$60K", 1); note(ws, rr, C, "Where are these benchmarks from - Soft Goods $725k, Video $236k, Audio $690k, Performance Lighting $450k? They are more useful to us than any published index and we would like to use them.", f"F{rr}", "Production benchmark note")
except KeyError: pass
ws2 = wb["Building & Fit-outBudget Detail"]; C2 = 7; head(ws2, C2, 10)
r = find(ws2, 2, r"G\.L\. INSURANCE"); note(ws2, r, C2, "G.L. $0 and Builder's Risk $0 - both genuinely inside the 9% combined? Schimenti's equivalent line at 555 Johnson says 'Builder's Risk - Excluded' in writing. Can your broker quote both SEPARATELY, and quote an owner-controlled programme? We carry $385,000.", [f"C{r}", f"C{r+1}"], "GL / Builder's Risk $0", PNK)
r = find(ws2, 2, r"GENERAL CONDITIONS"); note(ws2, r, C2, "'Carried in budget summary' - and also carried as division 013000 in trade cost. One function, two places.", f"C{r}")

# ================================================================ FRONT SHEET
fs = wb.create_sheet("MT QUESTIONS", 0)
for col, w in zip("ABCDE", [3, 30, 14, 44, 90]): fs.column_dimensions[col].width = w
fs.sheet_view.showGridLines = False
fs.cell(2, 2, "165 RANDOLPH - QUESTIONS ON THE 16 SEP MASTER DEVELOPMENT BUDGET").font = Font(name=F, size=16, bold=True, color="1F3864")
fs.cell(3, 2, "Matthew Teper, 17 Sep 2026. Every question is written beside the line it refers to, in a new right-hand column on each of your sheets. Highlighted cells are the ones asked about. None of your cells have been changed.").font = Font(name=F, size=9, color="595959")
fs.merge_cells("B3:E3"); fs.row_dimensions[3].height = 26; fs["B3"].alignment = WRAP
r = 5
fs.cell(r, 2, "WHERE THE NUMBERS STAND").font = QB; r += 1
for lab, v, n in [("Master Development Budget, 16 Sep", 89_084_591, "$1,202/SF on 74,100 SF; your sheet shows $655/SF on 135,953"),
                  ("Our V3, rebuilt on the measured RFEM steel", 77_897_555, "$1,051/SF. Same programme, 997.2 short tons priced by the ton"),
                  ("Yours after the corrections that survive the takeoff", 77_247_828, "0.8% from ours"),
                  ("Trade cost reconciliation, our extract vs your D25", 0, "309 lines, variance $0.00")]:
    fs.cell(r, 2, lab).font = Q; c = fs.cell(r, 3, v); c.number_format = '$#,##0;($#,##0);"-"'; c.font = QB
    fs.cell(r, 4, n).font = Font(name=F, size=8, color="595959"); r += 1
r += 1
fs.cell(r, 2, "THE FIVE WE NEED FIRST").font = QB; r += 1
for t in ["Budget Summary D67 - the contingency formula is 10% of the whole project, not of soft costs and FF&E as labelled.",
          "Budget Summary D30 - escalation on the building is blank.",
          "Budget Summary D26 - what is in the $12,000,000 and when is it priced? We expect it to go UP.",
          "General Conditions tab vs Breakdown division 013000 - the same function in two places, $6,175,000 combined.",
          "Breakdown 015800-1 - the $4,000,000 lump vs the $2,589,800 of backup beneath it."]:
    fs.cell(r, 2, f"{r-13}."); fs.cell(r, 3, t).font = Q; fs.merge_cells(start_row=r, start_column=3, end_row=r, end_column=5); r += 1
r += 1
fs.cell(r, 2, "TWO THINGS WE HAD WRONG AND ARE WITHDRAWING").font = QB; r += 1
for t in ["The roof: we had assumed a lift. The RFEM model is a rebuild - 62.4% of column steel starts at grade, all 517 truss members are new at +56.5 to +64.5 ft. Your 74,000 SF of roof demolition is the method, not an error.",
          "The area: we had called 135,953 SF wrong. We can no longer prove that - the model carries 146,508 SF gross. We are now only asking where the number comes from, and for one agreed area schedule derived from the test fit."]:
    c = fs.cell(r, 3, t); c.font = Q; c.alignment = WRAP; fs.merge_cells(start_row=r, start_column=3, end_row=r, end_column=5); fs.row_dimensions[r].height = 28; r += 1
r += 1
fs.cell(r, 2, "INDEX OF EVERY QUESTION").font = QB; r += 1
for i, h in enumerate(["Sheet", "Cell", "Your line", "Our question"], 2):
    c = fs.cell(r, i, h); c.font = H; c.fill = HF
r += 1
for sheet, cell, his, q in INDEX:
    fs.cell(r, 2, sheet).font = Q; fs.cell(r, 3, cell).font = QB
    c = fs.cell(r, 4, his); c.font = Q; c.alignment = WRAP
    c = fs.cell(r, 5, q); c.font = Q; c.alignment = WRAP
    fs.row_dimensions[r].height = max(15, 12 * (len(q) // 100 + 1)); r += 1
fs.freeze_panes = "A5"
wb.calculation.fullCalcOnLoad = True
wb.save(OUT); print("wrote", OUT, "| questions:", len(INDEX))
