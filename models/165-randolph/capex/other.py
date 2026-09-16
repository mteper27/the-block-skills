# -*- coding: utf-8 -*-
"""The other expenses: soft costs, FF&E and off-site, line by line.

Everything below the construction number. His figures come off 'Soft Cost &
FF&E Budget Detail'; ours off divisions 600 and 700. Each column foots to the
total its own budget publishes.
"""
import sys; sys.path.insert(0, '.')
import sept16_raw as R

# ============================================================= SOFT COSTS
# (package, ours, his, his line detail, comment)
SOFT = [
("Abatement", 1_000_750.0, 1_483_680.0,
 "Pipe insulation 190 LF @ $72 = $13,680. ROOF ABATEMENT 70,000 SF @ $21 = $1,470,000.",
 "HIS ROOF RATE IS 2.8x OURS ($21 vs our $7.50/SF) and it presumes the roof comes off. A lift "
 "keeps it — you abate what you disturb at the perimeter, not the whole field. Also: HE "
 "CARRIES THIS AS A SOFT COST, WE CARRY IT AS A TRADE. Neither number means anything until "
 "somebody does the ACP-5 survey. Nobody has sampled that roof."),

("Feasibility & due diligence (spent)", 342_000.0, 342_000.0,
 "Due Diligence & Feasibility Study 1 LS @ $342,000.",
 "IDENTICAL. Already committed, already spent."),

("Design & engineering", 2_906_000.0, 3_561_000.0,
 "Architecture & Engineering $3,100,000 as ONE LUMP, with architecture, MEP and structural all "
 "noted 'Carried in line #3'. Plus brand $45,000, interior design $90,000, MEP consultant "
 "$30,000, lighting design $51,000, kitchen design $20,000, LV/AV $35,000, signage design "
 "$75,000, renderings $50,000, reimbursables $30,000, civil $10,000, traffic $10,000, "
 "acoustical $15,000.",
 "He is $655,000 over us, but the comparison is unfair to him until that $3.1M lump is split. "
 "Note his ACOUSTICAL ENGINEERING IS $15,000 — 'sound and vibration testing'. We carry "
 "$200,000, because acoustic design next to residential is the licence to operate, not a test."),

("Investigation", 435_000.0, 150_000.0,
 "Geotechnical $150,000 (13 borings 50 ft deep, required for the ST permit). Environmental "
 "studies: $0, 'Carried in Feasibility Study'.",
 "WE ARE $285,000 HIGHER AND WE SHOULD BE. He carries no Phase I, no Phase II, no "
 "existing-conditions survey and no Rooflifters Stage 3 structural analysis. Those four are "
 "exactly what turns this budget from an estimate into a number — and the Stage 3 "
 "analysis decides whether the roof can be lifted at all."),

("Permits & approvals", 420_000.0, 678_297.48,
 "Permit & plan review fees $493,297, stated as '1.3% Trade Costs'. Special Projects Program "
 "$50,000, MEP permits $10,000, FA consultant $35,000, fire safety plan $21,500, fire "
 "protection plan $18,500, Con Ed connection $50,000.",
 "His $493,297 is a PERCENTAGE OF HIS OWN TRADE COST, so it inherits every inflation in it. "
 "Cut the trade cost and this falls with it. We carry $120,000 for DOB structural (ST) permit "
 "filing and expediting, which he does not — on a roof lift that filing is 12-18 months "
 "and it is the hardest permit in the job."),

("Legal & licensing", 250_000.0, 0.0,
 "Attorney Fees: $0. 'SLA Legal Fees carried in Feasibility DD'.",
 "HE CARRIES NO LEGAL AT ALL. On Factory Town the liquor licence was approved at ZERO and came "
 "in at $250,000. We carry SLA counsel $120,000, cabaret or its current equivalent $45,000, "
 "theater use-classification filing $55,000 and a zoning determination $30,000. The seating on "
 "the drawings is a licensing dependency — this is not optional."),

("Testing & controlled inspections", 140_000.0, 50_000.0,
 "Controlled inspections 1 LS @ $50,000.",
 "Light. NYC special inspections on a job with new structural steel, a lifted roof, "
 "fireproofing, sprinklers and a new 8,000A service run well past $50,000."),

("Builder's risk & GL insurance", 385_000.0, 0.0,
 "G.L. INSURANCE $0 and BUILDERS RISK INSURANCE $0 on his fit-out sheet. Notionally inside the "
 "9% 'Overhead, Profit & Insurance'.",
 "ASK HIM TO CONFIRM IT IS ACTUALLY IN THE 9%. Schimenti's comparable line at 555 Johnson says "
 "'Builder's Risk Insurance — Excluded' in black and white. If it is excluded here too, "
 "this is missing money, not a structural difference."),

("Project management", 520_000.0, 520_000.0,
 "Project Management $500,000 + Estimating Services $20,000.",
 "IDENTICAL TO THE DOLLAR. But the Budget Summary labels it 'Project Management (Live "
 "Nation)'. It is not — Live Nation is the co-pro and programming partner. This is our own "
 "development team. Fix the label before this budget goes to a lender."),
]

# ================================================================== FF&E
FFE = [
("Seating & furniture", 196_760.0, 1_043_750.0,
 "3,714 GA cushioned folding chairs @ $125 = $464,250. 657 mezzanine box chairs @ $300 = "
 "$197,100. 63 elevated chairs, 15 couches, 24 coffee tables. VIP lounge $75,000, VIP roof "
 "terrace $15,000, restaurant $60,000, restaurant terrace $10,000, roof terrace $25,000, roof "
 "lounge $35,000. Dressing rooms $60,000, crew lounge $25,000.",
 "THE BIGGEST FF&E GAP AND IT IS A LEGAL QUESTION, NOT A FURNITURE ONE. We carry 720 removable "
 "mezzanine seats at $25 (MT H127 sourcing) and replace the 657 box chairs with $45,000 of "
 "loose stools, high-tops and rail perches. Seating shown on the drawings drives the theater "
 "use-classification, which drives the liquor licence. COUNSEL HAS TO SET THE SEAT COUNT "
 "BEFORE EITHER NUMBER IS RIGHT. The rest is furniture for a VIP/restaurant/roof programme "
 "nobody has designed."),

("Bar & kitchen equipment", 1_050_000.0, 1_317_000.0,
 "Kitchen equipment $130,000. Nine bars at $9,000 per POS position: lobby 5, music hall L 16, "
 "R 15, rear 14, mezz R 8, mezz L 8, VIP 2, restaurant 2, roof 4 = 74 positions. Ice machines "
 "4 @ $15,000, walk-ins 2 @ $15,000. Freight & installation $375,000.",
 "HIS OWN NOTE ON THIS SHEET IS THE MOST VALUABLE LINE IN THE FILE: '* BPT: 26 POS / Prep "
 "Kitchen / 1 Walk-in Cooler $837K'. That is a prior build. 74 positions here at $9,000 = "
 "$666,000 against $837,000 for 26 positions plus a prep kitchen there. EVEN ALLOWING FOR THE "
 "KITCHEN, HE IS LIGHT — and so are we, at 53 positions. This is the one line where his "
 "own benchmark says the budget should go UP."),

("Data, IT & CCTV", 420_000.0, 420_000.0,
 "VoIP phones / data switch / WiFi $200,000. CCTV 110 cameras @ $2,000 = $220,000. Data "
 "cabling: 'Carried Construction Costs'.",
 "IDENTICAL TO THE DOLLAR, camera for camera. We took his rate."),

("Office furniture", 65_000.0, 65_000.0,
 "Administration $50,000, production desks $15,000.", "IDENTICAL."),

("Signage, wayfinding & art", 275_000.0, 650_000.0,
 "Exterior signage $400,000, interior wayfinding and ADA $100,000, interior art and decor "
 "$150,000 ('interior scenic work & exterior building murals').",
 "We carry $150,000 of exterior signage in FF&E plus $125,000 of signage and wayfinding inside "
 "the trade cost. He is $375,000 higher. A $400,000 exterior sign is a marquee, and on this "
 "building it may well be worth it — but it is a brand decision, not an estimate."),

("Administration & screening", 143_000.0, 93_000.0,
 "Three safes @ $1,000, radios $20,000, METAL DETECTORS 1 LOT @ $70,000.",
 "WE ARE HIGHER AND WE ARE RIGHT. One lot of metal detectors does not move 7,440 people. We "
 "carry 12 walk-through magnetometers at $10,000. Factory Town's security screening came in "
 "49% over its budget."),

("Facility — merchandise", 26_000.0, 26_000.0, "Merch cases $26,000.", "IDENTICAL."),

("Operations — custodial, barricades, shop", 29_000.0, 29_000.0,
 "80 trash cans @ $150, 2 janitor carts, bike rack $1,000, police barricades $10,000, hand "
 "tools $3,000, ladders $1,000, shelving $1,000.",
 "IDENTICAL. Note the bike rack at $1,000 — Factory Town's bike racks came in 69% over "
 "budget. Small line, but it is a known direction."),

("Production equipment", 73_500.0, 193_500.0,
 "Stage barricade $18,000, portable stage $30,000, FORK LIFT $35,000, SCISSOR LIFT $25,000, "
 "washer & dryer $5,000, risers $12,000, dock plates and dollies $60,000, shelving and tools "
 "$8,500.",
 "He carries a fork lift, a scissor lift, a portable stage and a washer/dryer that we do not. "
 "HE IS RIGHT ON THE LIFTS — a room this size owns them rather than renting them every "
 "load-in. Add $60,000 to ours."),

("Soft goods", 220_000.0, 500_000.0,
 "'All soft goods' 1 LS @ $500,000, note: 'Stage / Perimeter Walls Music Hall — CUTDOWN "
 "DRAPE @ MEZZ EDGE Not Included'.",
 "His own production benchmark note on the same sheet reads 'Soft Goods $725k'. So his $500,000 "
 "is already below his own comp AND explicitly excludes the mezzanine-edge cutdown drape. Ours "
 "at $220,000 is the light one here. This needs a real drape package priced off the section."),

("Video", 75_000.0, 285_000.0,
 "Music hall projector $75,000, displays & distribution $200,000, VIP projector $10,000. "
 "UPSTAGE VIDEO WALL and OVERHEAD VIDEO WALL are both blank, with a note reading '$1,400/SF'.",
 "The projector matches exactly. His $200,000 of displays and distribution is real scope we do "
 "not carry — concourse screens, box office, BOH. The video WALLS are Phase 2 in our plan "
 "and artists bring or rent their own; his file agrees by leaving them unpriced."),

("Audio — house PA", 2_200_000.0, 1_400_000.0,
 "House Sound System 1 LS @ $1,400,000, 'Includes Theater / VIP / Restaurant & Roof Area'.",
 "WE ARE $800,000 HIGHER AND THIS IS OUR NUMBER TO DEFEND. His own benchmark note on the same "
 "sheet says 'Audio $690k'. Ours is $1,850,000 of PA plus $145,000 of tuning and $205,000 of "
 "flying hardware. Nobody tours a PA for this size room so it has to be house — but GET A "
 "VENDOR QUOTE before this goes to a lender. Right now it is the weakest number we own."),

("Performance lighting", 340_000.0, 520_000.0,
 "Performance Lighting 1 LS @ $520,000. VIP performance lighting $0.",
 "His benchmark note says $450k. He is above it, we are below it. A house rig of fixtures, "
 "truss and hoists at $340,000 is thin for a 7,440 room — ours probably moves up."),

("FF&E installation labour", 600_000.0, 0.0,
 "Not carried as its own line. His $375,000 of 'Freight & Installation' sits inside the bar "
 "and kitchen equipment package above.",
 "Different home, not a different view — but ours is $600,000 across all FF&E against his "
 "$375,000 on the bar package alone. Once his lifts, soft goods and screening are installed "
 "too, the two get closer than they look."),

("Architectural lighting", 299_100.0, 1_750_000.0,
 "Architectural & Exterior Lighting 1 LS @ $1,750,000. SEPARATELY, his ELECTRICAL trade carries "
 "'I/O lighting package throughout PROVIDED BY OTHERS 135,953 SF @ $12 = $1,631,436'.",
 "THE BIGGEST SINGLE ITEM IN THE OTHER EXPENSES, AND IT IS BOUGHT TWICE. $1,750,000 here plus "
 "$1,631,436 inside the electrical trade = $3,381,436 of architectural lighting against our "
 "$299,100 of lighting and controls. Ours is almost certainly too thin for a room that trades "
 "on how it looks — but his is the same package paid for twice, and his own line says "
 "'provided by others'."),
]

# ============================================================== OFF-SITE
OFFSITE = [
("Off-site parking garage", 0.0, 2_257_500.0,
 "D21 is '=86*25000' = $2,150,000 under a label reading 'Parking Garage - 260/spaces', plus 5% "
 "escalation = $107,500.",
 "THE LABEL SAYS 260 SPACES AND THE FORMULA SAYS 86. We carry no off-site parking at all. "
 "Decide whether it is in the deal, then fix whichever of the two is wrong. Note this is the "
 "ONE line in his whole budget that gets escalation — the $63.7M building gets none."),
]

OURS_SOFT = sum(s[1] for s in SOFT); HIS_SOFT = sum(s[2] for s in SOFT)
OURS_FFE  = sum(f[1] for f in FFE);  HIS_FFE  = sum(f[2] for f in FFE)
OURS_OFF  = sum(o[1] for o in OFFSITE); HIS_OFF = sum(o[2] for o in OFFSITE)

# His side must tie to his own Budget Summary rows, untouched.
assert abs(HIS_SOFT - R.SOFT) < 0.01, HIS_SOFT - R.SOFT
assert abs(HIS_FFE  - R.FFE)  < 0.01, HIS_FFE - R.FFE

# Our side ties to divisions 700 and 600 as published, plus three items we carry inside
# the TRADE cost that he carries here. Each is disclosed on the face of the sheet.
OUR_700, OUR_600 = 5_398_000.0, 5_588_260.0
XFER_SOFT = [("Abatement, division 000", 1_000_750.0)]
XFER_FFE  = [("Signage & wayfinding, division 400", 125_000.0),
             ("Lighting & controls, division 500", 299_100.0)]
assert abs(OURS_SOFT - OUR_700 - sum(v for _, v in XFER_SOFT)) < 0.01, OURS_SOFT
assert abs(OURS_FFE  - OUR_600 - sum(v for _, v in XFER_FFE))  < 0.01, OURS_FFE

TOTAL_OURS = OURS_SOFT + OURS_FFE + OURS_OFF
TOTAL_HIS  = HIS_SOFT + HIS_FFE + HIS_OFF
