# -*- coding: utf-8 -*-
"""Apples to apples: both budgets, complete, in one identical structure.

Nothing is stripped from either side. Every row means the same thing in both
columns, and each column foots to the total that budget actually publishes:
his $89,084,591 and our $64,648,067.

Two normalisations, and only two, so the rows line up. Both are disclosed on
the face of the sheet and neither changes either total:
  1. His division 013000 PROJECT REQUIREMENTS ($3,034,000) and 001000
     PRECONSTRUCTION ($60,000) move out of his trade cost and onto the
     'running the site' rows, where our equivalent already sits.
  2. His abatement ($1,483,680) moves out of his soft costs and into the
     hazmat work package, where ours already sits.
"""
import sys; sys.path.insert(0, '.')
import b2b, sept16_raw as R, detail

SF, CAP = 74_100, 7_440
CASCADE = 1.09 * 1.10 * 1.10   # what $1 of his trade cost becomes, all-in

# ------------------------------------------------------------------ OURS
OURS_TRADE = b2b.OURS                       # 38,166,123, asserted in b2b.py
OURS_ESC   = OURS_TRADE * 0.10
OURS_GC    = OURS_TRADE * 0.085             # Schimenti, 555 Johnson
OURS_OHP   = OURS_TRADE * 0.09
OURS_CONT  = 5_000_000.0
OURS_FFE   = 5_588_260.0                    # incl. 720 removable seats at the $25 toggle
OURS_SOFT  = 5_398_000.0
OURS_TOTAL = (OURS_TRADE + OURS_ESC + OURS_GC + OURS_OHP
              + OURS_CONT + OURS_FFE + OURS_SOFT)
assert abs(OURS_TOTAL - 64_648_067.0) < 1.0, OURS_TOTAL

# ------------------------------------------------------------------- HIS
HIS_013, HIS_001, HIS_ABATE = 3_034_000.0, 60_000.0, 1_483_680.0
HIS_TRADE = R.TRADE - HIS_013 - HIS_001 + HIS_ABATE   # normalised, = b2b.HIS
HIS_SOFT  = R.SOFT - HIS_ABATE
assert abs(HIS_TRADE - b2b.HIS) < 1.0

# ------------------------------------------------- THE CHASSIS
# kind: 'pkg' work package | 'sub' subtotal | 'line' below-the-line | 'tot' total
ROWS = []
for name, o, h, csi, note in b2b.WP:
    ROWS.append(('pkg', name, o, h, note))
ROWS += [
 ('sub', 'TRADE COST — the work itself', OURS_TRADE, HIS_TRADE,
  "His priced lines come to LESS than our entire trade cost — because eight of his "
  "divisions are still at zero quantity."),
 ('line', 'Trade costs to be priced (his plug)', 0.0, R.TBP,
  "Standing in for structural steel, fireproofing, concrete, doors, glazing, drywall, all "
  "millwork and the kitchen. We price that scope at $%s, so the plug is right-sized."
  % f'{-b2b.UNPRICED:,.0f}'),
 ('sub', 'ALL THE WORK', OURS_TRADE, HIS_TRADE + R.TBP, ''),

 ('line', 'General conditions — running the site', OURS_GC, HIS_013 + R.GCLINE,
  "Ours is 8.5%% of trade. His is a $3,141,000 staffing chart (90 weeks, PM, APM, engineer, "
  "three supers) PLUS $3,034,000 of division 013000 sitting inside his trade cost doing the "
  "same job. Combined 12.36%% against Schimenti's 7.80%% and 8.90%% at 555 Johnson."),
 ('line', 'Preconstruction', 0.0, HIS_001,
  "He prices it as a trade. We carry it inside design fees."),
 ('line', 'Escalation', OURS_ESC, 0.0,
  "BLANK IN HIS FILE for the third version running — while the $2,150,000 parking garage "
  "gets 5%% on the row above. On a 20-month programme this is real and it should be funded."),
 ('line', 'Overhead, profit & insurance', OURS_OHP, R.OHP,
  "Same 9%% rate. His is bigger because his base is bigger — he charges it on trade plus "
  "the $12M plug plus general conditions."),
 ('line', 'Contractor contingency', 0.0, R.CONTRCT,
  "10%% on a base that already contains the 9%% overhead and profit. We hold ONE contingency, "
  "below, and the owner holds it."),
 ('sub', 'CONSTRUCTION COST', OURS_TRADE + OURS_GC + OURS_ESC + OURS_OHP,
  HIS_TRADE + R.TBP + HIS_013 + HIS_001 + R.GCLINE + R.OHP + R.CONTRCT, ''),

 ('line', 'Contingency', OURS_CONT, R.CONTING,
  "His line is labelled 'Soft Costs & FFE Contingency 10%%' but the formula is "
  "=(D23+D31+D47+D65)*0.1 — 10%% of the WHOLE PROJECT, on top of the contractor "
  "contingency already inside it. As labelled it would be $1,507,723."),
 ('line', 'Soft costs', OURS_SOFT, HIS_SOFT,
  "Within $97,000 of each other once his abatement is moved to the work above. The closest "
  "agreement anywhere in either budget."),
 ('line', 'FF&E', OURS_FFE, R.FFE,
  "His carries $1,750,000 of architectural lighting AND a $1,631,436 'I/O lighting package "
  "provided by others' inside his electrical trade. One of those is bought twice."),
 ('line', 'Off-site parking garage', 0.0, R.OFFSITE,
  "D21 is '=86*25000' under a label reading '260/spaces'. We do not carry off-site parking "
  "at all. The label and the formula disagree with each other."),
 ('tot', 'TOTAL DEVELOPMENT COST', OURS_TOTAL, R.TOTAL, ''),
]
_o = sum(r[2] for r in ROWS if r[0] == 'line') + OURS_TRADE
_h = sum(r[3] for r in ROWS if r[0] == 'line') + HIS_TRADE
assert abs(_o - OURS_TOTAL) < 1.0 and abs(_h - R.TOTAL) < 1.0, (_o, _h)

METRICS = [
 ('Total development cost', OURS_TOTAL, R.TOTAL, '$#,##0'),
 ('$ per SF on 74,100 SF', OURS_TOTAL / SF, R.TOTAL / SF, '$#,##0'),
 ('$ per capacity unit (7,440)', OURS_TOTAL / CAP, R.TOTAL / CAP, '$#,##0'),
 ('Markups + contingency as %% of the work',
  (OURS_ESC + OURS_GC + OURS_OHP + OURS_CONT) / OURS_TRADE,
  (HIS_013 + HIS_001 + R.GCLINE + R.OHP + R.CONTRCT + R.CONTING) / (HIS_TRADE + R.TBP), '0.0%'),
 ('Contingency as %% of construction cost', OURS_CONT / (OURS_TRADE + OURS_GC + OURS_ESC + OURS_OHP),
  R.CONTING / R.CONSTR, '0.0%'),
]

# --------------------------------------------------------------- THE ISSUES
# (whose, issue, evidence, what to do, $ at stake all-in)
ISSUES = [
("HIS","Contingency is charged on the whole project, not on what the label says",
 "D67 reads 'Soft Costs & FFE Contingency 10%' and computes =(D23+D31+D47+D65)*0.1. D31 is "
 "the $63,651,265 construction number, which already holds $5,786,479 of contractor "
 "contingency.",
 "Keep one or the other, not both. $578,648 of it is literally contingency on contingency.",
 R.CONTING - (R.SOFT + R.FFE) * 0.10),
("HIS","$9.7M of trade cost is multiplied by a floor area this building does not have",
 "HVAC is one line: 132,542 SF x $45.00 = $5,964,390, no tonnage, no load. Eight more run on "
 "135,953 SF — paint $5, I/O lighting $12, general power $6, mechanical power $3, temp "
 "light $2, fire alarm $2, emergency $1, dimming $0.75. Sprinkler mains for a 14,000 SF "
 "mezzanine deck are priced on 50,000 SF. (The I/O lighting line runs on 135,953 SF too, "
 "but it is counted once below instead of twice here.)",
 "Re-cut to 74,100 SF (footprint) or 88,100 SF (covered floor). 135,953 SF is 555 Johnson, "
 "not this building — it is a template carryover.", 4_136_587.0 * CASCADE),
 # 4,136,587 EXCLUDES the I/O lighting line. That line runs on 135,953 SF too, but it is
 # counted once below under "the lighting package is bought twice". Counting its area
 # correction here as well would double-count $757,371.
("HIS","General conditions is charged in two places at once",
 "$3,141,000 as a staffing chart below the line, plus $3,034,000 of division 013000 inside "
 "trade cost — including 'Project Labor 1 LS $2,000,000' with no crew, rate or duration.",
 "12.36% combined against 7.80% and 8.90% from Schimenti at 555 Johnson — open shop, this "
 "submarket, Eric's own GC. Pick one place and hold it at 8.35%.", 2_643_751.0),
("HIS","Scaffolding is the biggest single package gap in the file",
 "$6,170,000 against our $1,438,262. A $4,000,000 sidewalk bridge lump with his own backup "
 "rows — 1,126 LF @ $500 and 27,024 SF @ $75 — footing to $2,589,800 directly "
 "beneath it, plus $2,000,000 of interior scaffolding.",
 "Ask which of his two numbers is right, and how many linear feet of actual public sidewalk "
 "this building has.", 3_970_153.0),
("HIS","Structural steel is $0 on a project scoped 'Add Second Level'",
 "All nineteen lines of 055100 are zero quantity: roof trusses and columns at $6,000/TON, "
 "mezzanine framing, balcony framing, stage lighting and AV support structure at $8.00/LB, "
 "railings, stairs, dunnage, lintels. We carry $5,827,741.",
 "His own $8.00/LB rate is good — our rigging grid works out to $9.21/LB, so he "
 "corroborates us within 15%. Give him the tonnage.", 0.0),
("HIS","2,000 coat check lockers at $500 each",
 "$1,000,000 inside specialties, note '333LF'. That serves 27% of a 7,440-capacity house at "
 "once, at a rate for a gym locker bank.",
 "750 at $350 is a generous January coat check.", 972_689.0),
("HIS","The lighting package is bought twice",
 "'I/O lighting package throughout PROVIDED BY OTHERS  135,953 SF @ $12 = $1,631,436' sits in "
 "his electrical trade, while FF&E separately carries $1,750,000 of architectural lighting and "
 "$520,000 of performance lighting.",
 "His own line says others provide it. Keep the conduit and wiring, delete the fixtures.",
 2_151_701.0),
("HIS","Plumbing is 2.1x ours and one of us has the fixture count wrong",
 "$3,717,250 against our $1,757,502. 178 water closets, 154 lavatories and 51 urinals at "
 "$4,000 each, nine bars roughed, a $125,000 restaurant grease trap.",
 "GET THE ARCHITECT'S CODE FIXTURE CALCULATION. Settleable with arithmetic in an afternoon, "
 "and ours may well be the light one.", 0.0),
("BOTH","We are building two different roofs",
 "He demolishes 74,000 SF of pre-cast roof at $8/SF and lays 56,085 SF of new membrane at "
 "$36/SF. We lift the existing roof on the lifter's towers, extend the columns and clad a new "
 "30 ft band.",
 "SETTLE THIS FIRST. It moves concrete, steel, scaffolding, demolition and roofing all at "
 "once, and nothing else reconciles until it is decided.", 0.0),
("BOTH","Second floor, third floor, roof decks, balcony, two lounges, foundry, restaurant",
 "Finishes are 4x ours — $3,509,501 against $866,500. He is pricing a programme off the "
 "test fit, and it drives his sprinkler quantities, his fixture counts and the 135,953 SF.",
 "PROGRAMME, NOT AN ERROR. He priced what the drawings showed him. That conversation is with "
 "Wake and with us, and it has to happen before the next version.", 0.0),
("BOTH","HVAC agreeing is a coincidence",
 "$5,964,390 his against $5,950,650 ours — $13,740 apart. His is one line on an area "
 "basis. Ours is built from the occupancy load.",
 "Two different methods landing in the same place. Get tons from the mechanical engineer "
 "before either number is trusted.", 0.0),
("NEITHER","The $12,000,000 plug is right-sized — leave it alone",
 "The scope he left at zero or barely touched is scope we price at $%s. His plug covers it "
 "with about $%s of headroom." % (f'{-b2b.UNPRICED:,.0f}', f'{b2b.PLUG + b2b.UNPRICED:,.0f}'),
 "The instinct is to attack the biggest round number in the file. Don't. Ask him to PRICE it, "
 "not cut it — and when he does, the trade cost moves, not the plug.", 0.0),
("OURS","Acoustics is under-carried by him and must not be cut to his number",
 "$581,802 of K13 against our $1,864,000.",
 "Ours is not decoration — it is the licence to operate next to residential.", 0.0),
("OURS","His elevator build-up is better than our allowance",
 "4 lobby stops + 2 stage stops at $75,000 plus a hydraulic lift = $480,000. Ours is a "
 "$300,000 allowance.", "Take his.", 0.0),
("OURS","VESDA — he is right and we do not carry it",
 "$250,000 for aspirating smoke detection in the music hall.",
 "A 50 ft clear volume with haze and pyro needs it. Add it.", 0.0),
("OURS","Sitework — we under-carry",
 "$346,335 against our $90,000: 8,295 SF of sidewalk repair, trees, fencing and a 2,380 SF "
 "fire-escape egress route at $75/SF.", "His is the real number; ours is an allowance.", 0.0),
]
