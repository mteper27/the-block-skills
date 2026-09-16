# -*- coding: utf-8 -*-
"""Building to building: the physical work only.

Every markup comes off BOTH sides - general conditions, overhead, profit,
insurance, contractor contingency, project contingency, escalation - and so do
soft costs, FF&E and the off-site parking garage. What is left is bricks,
steel, pipe and wire, mapped into one common frame so the two estimates can be
read against each other line for line.
"""
import sys; sys.path.insert(0, '.')
import detail
import sept16_raw as R

SF = 74_100

# ---------------------------------------------------------------- OUR SIDE
def _grp():
    out = {}
    for code, _name, groups in detail.D:
        for g, lines in groups:
            s = 0.0
            for d, q, u, rate, src in lines:
                try: s += float(q) * float(rate)
                except (TypeError, ValueError): pass
            out[(code, g)] = s
    return out
G = _grp()
def og(*keys):
    t = 0.0
    for k in keys:
        assert k in G, f'no such group: {k}'
        t += G[k]
    return t

# -------------------------------------------------------------- HIS SIDE
# His division subtotals, read off 'Building & Fit-outBudget Detail' column C.
H = {
 '013000': 3_034_000.0, '015800': 6_170_000.0, '024100': 1_287_817.0,
 '033000':   177_450.0, '042000':   530_010.0, '044200':   764_340.0,
 '055100':         0.0, '061000':         0.0, '064000':         0.0,
 '075000': 2_557_428.0, '078100':         0.0, '081000':         0.0,
 '083000':    76_000.0, '084100':         0.0, '088000':         0.0,
 '092000':   119_664.0, '092300':         0.0, '096000':   765_048.0,
 '096050':   515_298.0, '096400':   373_050.0, '099000': 1_091_765.0,
 '100000': 1_548_500.0, '100500':   581_802.0, '101400':    50_000.0,
 '120000':    50_000.0, '114000':    50_000.0, '142000':   480_000.0,
 '210000': 1_334_070.0, '220000': 3_717_250.0, '230000': 5_964_390.0,
 '260000': 5_512_336.75,'270000':   227_500.0, '265000':    40_000.0,
 '283100':   521_906.0, '320000':   346_335.0, '001000':    60_000.0,
}
assert abs(sum(H.values()) - R.TRADE) < 0.01, sum(H.values()) - R.TRADE
def hd(*codes): return sum(H[c] for c in codes)

# ------------------------------------------------------- THE COMMON FRAME
# (work package, ours, his, his CSI codes, note)
WP = [
("Enabling, sidewalk shed & scaffolding",
 og(('000','Sidewalk shed / bridge'), ('000','Interior protection & containment'),
    ('000','Temporary weather protection')),
 hd('015800'), '015800',
 "His single biggest line anywhere. $4,000,000 sidewalk bridge as a lump against his own "
 "backup rows of $2,589,800, plus $2,000,000 of interior scaffolding. We carry a shed at "
 "$210/LF erected plus 24 months of rental, priced off the perimeter."),

("Hazmat & abatement",
 og(('000','Asbestos / hazmat abatement')),
 1_483_680.0, 'soft costs',
 "HE CARRIES THIS AS A SOFT COST, NOT A TRADE. Pulled across here so the comparison is "
 "physical-to-physical. Ours presumes ACM on the 1948 precast roof - nobody has sampled it. "
 "The ACP-5 survey is worth $555,750 of that line."),

("Demolition",
 og(('000','Demolition — interior')),
 hd('024100'), '024100',
 "$592,000 of his is 74,000 SF of pre-cast ROOF demolition at $8/SF. A roof lift keeps the "
 "roof. Strip that and he is at $695,817 against our $601,978 - close."),

("Sitework",
 og(('000','Sitework')),
 hd('320000'), '320000',
 "He prices 8,295 SF of sidewalk repair, trees, fencing and a 2,380 SF fire-escape egress "
 "route. We under-carry this."),

("Concrete & foundations",
 og(('100','Foundations for the new load path — ASK if in quote'),
    ('200','Stage foundations'), ('300','Mezzanine foundations')),
 hd('033000'), '033000',
 "EVERY LINE in his 033000 is zero quantity except three. No footings for new columns, no "
 "stage platform slab, no mezzanine deck pour. Ours funds the new load path for the lift plus "
 "ground-supported stage and mezzanine footings."),

("Roof: lift contract vs roofing works",
 og(('100','Roof lift contract — YOUR QUOTE'),
    ('100','Roof-to-wall closure — ASK if in quote'), ('100','Roof reinstatement'),
    ('100','Fire separation'), ('100','MEP disconnect & reinstatement')),
 hd('075000'), '075000',
 "THESE ARE NOT THE SAME SCOPE. Ours is a $3.5M lifter's contract plus the surrounding work - "
 "cut the roof free, jack it, extend the columns, clad the new band. His is 56,085 SF of new "
 "membrane at $36/SF over a roof he has already demolished. This is the single biggest "
 "methodological difference in the two files."),

("Structural steel, stage, mezzanine & rigging",
 og(('200','Stage structure & deck'), ('200','Production towers & mounting structure'),
    ('200','Rigging grid over the crowd — ground-supported lighting towers + spanning steel'),
    ('200','Platforms & FOH'), ('200','Erection labour & equipment'),
    ('300','Mezzanine structure'), ('300','Raised premium tier — replaces built boxes'),
    ('300','Egress & guarding')),
 hd('055100'), '055100',
 "ZERO. Nineteen lines, every quantity blank, on a project whose own scope line reads 'Add "
 "Second Level'. His own unpriced rate for stage lighting and AV support structure is $8.00/LB; "
 "our rigging grid works out to $9.21/LB, so his rate corroborates ours within 15%."),

("Fireproofing",
 og(('100','Fireproofing on new steel')),
 hd('078100'), '078100',
 "ZERO. Three lines at $5/SF, all blank quantity - new roof steel, new mezzanine steel, and "
 "fireproofing added to the existing roof steel."),

("Envelope - masonry, doors, storefront, glazing",
 og(('100','Envelope completion at the new band'), ('400','Masonry'),
    ('400','Doors, frames & hardware'), ('400','Storefront & glazing')),
 hd('042000','081000','083000','084100','088000'), '042000/081000/083000/084100/088000',
 "Masonry is close ($530,010 his vs our $739,626). But doors, storefront and glazing are all "
 "zero - including every acoustical door into the music hall at $10,000 each. We also carry "
 "32,670 SF of new wall band created by the 30 ft lift, which his file has nowhere to put."),

("Interior construction - drywall & carpentry",
 og(('400','Drywall & partitions'), ('400','Rough carpentry & protection')),
 hd('092000','061000'), '092000/061000',
 "Nine of his ten drywall lines are zero quantity. The $119,664 he does carry is a fraction of "
 "a room that needs sound-rated separation between a 7,440-capacity hall and everything else."),

("Finishes - flooring, stone, tile, paint",
 og(('400','Finishes')),
 hd('044200','092300','096000','096050','096400','099000'),
 '044200/092300/096000/096050/096400/099000',
 "HE IS 4x US HERE AND HE MAY WELL BE RIGHT. $764,340 of stone, $765,048 of resilient, "
 "$515,298 of floor prep, $373,050 of wood, $1,091,765 of paint. Some of it is the 135,953 SF "
 "error (paint is 135,953 x $5), but most of it is finish level - he is pricing a restaurant "
 "and VIP lounges we have not designed. This is a PROGRAMME conversation, not an error."),

("Acoustics",
 og(('400','Acoustic treatment — licence to operate')),
 hd('100500'), '100500',
 "$581,802 of K13 against our $1,864,000. Ours is not decoration - it is the licence to "
 "operate next to residential. Under-carried by him."),

("Specialties, millwork & signage",
 og(('400','Specialties'), ('400','Millwork'), ('400','Signage & wayfinding')),
 hd('100000','064000','101400','120000'), '100000/064000/101400/120000',
 "His $1,548,500 of specialties contains $1,000,000 of coat check lockers - 2,000 at $500 "
 "each. Meanwhile ALL millwork is zero: every bar in the building at $2,000/LF with no "
 "linear feet against it, eight bars, plus back bars, box office and counters."),

("Conveying / elevators",
 og(('500','Conveying')),
 hd('142000'), '142000',
 "4 lobby stops + 2 stage stops at $75,000 plus a hydraulic lift. His is the better-built "
 "number; ours is a $300,000 allowance."),

("Fire protection - sprinklers",
 og(('500','Fire protection')),
 hd('210000'), '210000',
 "He prices 119,000 SF of sprinkler coverage (69,000 + 50,000). Coverage is 88,100 SF - "
 "74,100 ground plus the 14,000 SF mezzanine deck. The 2nd-floor line alone is $540,000 over."),

("Plumbing",
 og(('500','Plumbing')),
 hd('220000'), '220000',
 "HE IS 2.1x US. 178 water closets, 154 lavatories, 51 urinals at $4,000 each, nine bars "
 "roughed, a $125,000 restaurant grease trap. His fixture count may be right for 7,440 - ours "
 "may be light. GET THE ARCHITECT'S CODE FIXTURE CALCULATION and settle it with arithmetic."),

("HVAC",
 og(('500','HVAC'), ('500','Heating')),
 hd('230000'), '230000',
 "Almost identical totals - and that is a coincidence, not agreement. His is ONE LINE: "
 "132,542 SF x $45.00, no tonnage, no load, on an area this building does not have. Ours is "
 "built from the occupancy load. Same answer, one of us by accident."),

("Electrical, power & low voltage",
 og(('500','Electrical service & distribution'), ('500','Production power'),
    ('500','Lighting & controls'), ('500','Low voltage')),
 hd('260000','270000','265000'), '260000/270000/265000',
 "Within 13% of each other, and his two 4,000A switchboards match our service sizing. But "
 "$3,092,931 of his is priced on 135,953 SF, and $1,631,436 of it is an 'I/O lighting package "
 "PROVIDED BY OTHERS' that FF&E buys again."),

("Fire alarm & detection",
 og(('500','Fire alarm & detection')),
 hd('283100'), '283100',
 "Close. His includes a $250,000 VESDA system for the music hall that we do not carry and "
 "probably should."),

("Kitchen & food service - construction side",
 og(('800','L0 · Base food service — you need this at ANY scope'),
    ('800','L1 · Warming / finishing kitchen — adds to L0')),
 hd('114000'), '114000',
 "Both of us carry almost nothing here, for different reasons. His kitchen money is in FF&E "
 "($1,317,000) and in plumbing roughing. Ours is a three-level toggle with L0 and L1 on — a warming kitchen, no grease hood. The "
 "Type I versus Type II hood decision still drives this and nobody has made it."),
]

OURS  = sum(w[1] for w in WP)
HIS   = sum(w[2] for w in WP)
PLUG  = R.TBP
HIS_ALL = HIS + PLUG

# ------------------------------------------------- WHAT CAME OFF BOTH SIDES
STRIPPED = [
 ("General conditions / project requirements", "Div 013000 $3,034,000 + the $3,141,000 "
  "staffing line below the line", 3_034_000.0 + 3_141_000.0, "carried as a % below the line"),
 ("Preconstruction", "Div 001000", 60_000.0, "we carry it in soft costs"),
 ("Overhead, profit & insurance 9%", "Budget Summary D28", R.OHP, "below the line"),
 ("Contractor contingency 10%", "D29", R.CONTRCT, "below the line"),
 ("Project contingency", "D67", R.CONTING, "single $5,000,000 owner-held pot"),
 ("Escalation", "D30 - blank in his file", 0.0, "6% below the line"),
 ("Soft costs", "D47", R.SOFT, "$5,398,000, separately"),
 ("FF&E", "D65", R.FFE, "$5,570,260, separately"),
 ("Off-site parking garage", "D21+D22", R.OFFSITE, "NOT CARRIED AT ALL"),
]

# Our side must tie to the trade cost our own V2 workbook publishes, or this
# comparison is auditing my mapping rather than the two budgets.
V2_TRADE = 38_166_123.0
assert abs(OURS - V2_TRADE) < 1.0, OURS - V2_TRADE

# --------------------------------------- WHERE THE GAP ACTUALLY SITS
# Three buckets, and they mean three different things. Never net them.
#   OVER   - scope BOTH of us priced, where his number is higher. This is the negotiation.
#   UNPRICED - scope he left at zero or barely touched. This is what the $12M plug is FOR.
#   JUDGEMENT - scope he priced properly but lower, because he made a different call
#               (a different roof method, a lower acoustic spec). Decisions, not missing lines.
JUDGEMENT_PKGS = {"Roof: lift contract vs roofing works", "Acoustics"}
OVER      = sum(w[2] - w[1] for w in WP if w[2] > w[1])
_under    = [w for w in WP if w[2] < w[1]]
JUDGEMENT = sum(w[2] - w[1] for w in _under if w[0] in JUDGEMENT_PKGS)
UNPRICED  = sum(w[2] - w[1] for w in _under if w[0] not in JUDGEMENT_PKGS)
UNDER     = JUDGEMENT + UNPRICED
assert abs(OVER + UNDER + PLUG - (HIS_ALL - OURS)) < 1.0

SPLIT = [
 ("Scope we BOTH priced, where he is higher", OVER,
  "This is the negotiation. Three packages are 73% of it: scaffolding $4.73M, "
  "finishes $2.64M, plumbing $1.96M."),
 ("Scope he left at zero or barely touched", UNPRICED,
  "Structural steel, fireproofing, concrete and foundations, doors and glazing, drywall, "
  "millwork, kitchen. This is what the plug is FOR."),
 ("His 'Trade Costs To Be Priced' plug", PLUG,
  "$%s against $%s of scope. RIGHT-SIZED, with about $%s of headroom. Do not negotiate "
  "this line - ask him to price it."
  % (f"{PLUG:,.0f}", f"{-UNPRICED:,.0f}", f"{PLUG + UNPRICED:,.0f}")),
 ("Different calls, properly priced on both sides", JUDGEMENT,
  "The roof lift versus roof replacement, and acoustic spec. These are DECISIONS, not "
  "missing lines, and the plug should not have to cover them."),
 ("BUILDING-TO-BUILDING GAP", OVER + UNDER + PLUG, ""),
]
