# -*- coding: utf-8 -*-
"""Forensic audit of the 16 Sep 2026 Master Development Budget.

Method: construction-budget-audit skill, in its stated order. Every correction
is applied to a SOURCE CELL and the file's own formula chain is then re-run, so
no markup is ever applied by hand and nothing can be double-counted.
"""
import sept16_raw as R

SF      = 74_100     # CLAUDE.md. THE basis.
MEZZ    = 14_000     # inside the envelope
COVERED = SF + MEZZ  # 88,100 -- sprinkler / alarm / power coverage

# ---------------------------------------------------------------- 1. RECONCILE
def _n(x):
    try: return float(x)
    except (TypeError, ValueError): return 0.0

EXTRACT = sum(_n(l[7]) for l in R.LINES)
RECON = [
 ("Sum of the 309 line items I extracted from 'Building & Fit-out Breakdown'", EXTRACT),
 ("+ 001000 PRECONSTRUCTION (on 'Building & Fit-outBudget Detail' C46 only)", R.PRECON),
 ("My reconstruction of his trade cost", EXTRACT + R.PRECON),
 ("His Trade Cost, Budget Summary D25", R.TRADE),
 ("VARIANCE", EXTRACT + R.PRECON - R.TRADE),
]

# ------------------------------------------------- 2. THE ARITHMETIC, PROVEN
PROOF = [
 ("D28  Overhead, Profit & Insurance", "=SUM(D25:D27)*0.09",
  (R.TRADE+R.TBP+R.GCLINE)*0.09, R.OHP,
  "9% is charged on trade + the $12M plug + general conditions. GC is being marked up."),
 ("D29  Contractor Contingency 10%", "=SUM(D25:D28)*0.1",
  (R.TRADE+R.TBP+R.GCLINE+R.OHP)*0.10, R.CONTRCT,
  "10% on a base that already contains the 9% OH&P. Markup on markup."),
 ("D67  'Soft Costs & FFE Contingency 10%'", "=(D23+D31+D47+D65)*0.1",
  (R.OFFSITE+R.CONSTR+R.SOFT+R.FFE)*0.10, R.CONTING,
  "THE LINE DOES NOT DO WHAT IT SAYS. D31 is the whole construction number, which "
  "already carries its own 10% contractor contingency. 10% of soft + FF&E, as labelled, "
  "is $1,507,723."),
 ("D30  Escalation on the building", "(blank)", 0.0, 0.0,
  "The $2,150,000 parking garage gets 5% escalation on row 22. The $63,651,265 building "
  "gets nothing. Same as the 4 Sep file -- still not fixed."),
 ("D71  $ PER SF", "=D69/135953", R.TOTAL/135_953, R.TOTAL/135_953,
  "135,953 SF is stacked floor area across all levels and it is not this building. "
  "On the real 74,100 SF the same total is $%s/SF." % f"{R.TOTAL/SF:,.0f}"),
]

CASCADE = 1.09 * 1.10 * 1.10   # $1 of trade cost all-in, as the file is built today

# --------------------------------------------------------------- 3. FINDINGS
# (id, direction, headline, evidence quoted from the file, his $, corrected $, remedy)
FINDINGS = [
("1","OVERSTATED",
 "The contingency line is computed on the whole project, not on what its label says",
 "D67 reads 'Soft Costs & FFE Contingency 10%' and the formula is =(D23+D31+D47+D65)*0.1. "
 "D31 is the $63,651,265 construction number, which already contains $5,786,479 of contractor "
 "contingency on row 29.",
 R.CONTING, (R.SOFT+R.FFE)*0.10,
 "Either rename it 'Project Contingency' and delete the contractor contingency on row 29, or "
 "keep row 29 and cut row 67 back to soft + FF&E. Not both. $578,648 of it is literally "
 "contingency on contingency."),

("2","OVERSTATED",
 "$10.3M of trade cost is priced on 135,953 SF - a floor area this building does not have",
 "'HVAC System including BMS  132,542 SF @ $45.00 = $5,964,390' is one line with no tonnage "
 "and no load behind it. Seven more lines multiply 135,953 SF: paint @ $5, I/O lighting @ $12, "
 "general power @ $6, power to mechanical @ $3, temp light & power @ $2, fire alarm @ $2, "
 "emergency lighting @ $1, dimming @ $0.75.",
 11_306_898.0, 6_596_075.0,
 "Re-cut every one to 74,100 SF (footprint: HVAC volume, mechanical power) or 88,100 SF "
 "(covered floor: power, lighting, paint, alarm). Separately, HVAC on a 50 ft clear room is a "
 "LOAD, not an area - ask the mechanical engineer for tons, not $/SF."),

("3","OVERSTATED",
 "The general-conditions function is charged twice, in two different places",
 "Row 27 carries $3,141,000, and the 'General Conditions' tab backs it with a real staffing "
 "chart: Exec 10 wks, PM 90 wks @ $6,400, APM, Engineer, Accountant, three Supers @ $6,000 for "
 "90 weeks. That part is good work. But division 013000 PROJECT REQUIREMENTS, $3,034,000, sits "
 "INSIDE the trade cost doing the same job - site office, field technology $200,000, site "
 "safety plan and inspector $400,000, portable toilets, protection, clean-up, rubbish, final "
 "clean, and 'Project Labor 1 LS $2,000,000'.",
 R.GCLINE+3_034_000.0, None,   # filled in below once TRADE_FIX is known
 "Combined that is 12.36% of trade. Schimenti priced general conditions at 7.80% and 8.90% on "
 "555 Johnson - open shop, this submarket, Eric Cohen's own GC. Pick ONE place and hold it at "
 "8.35%. 'Project Labor $2,000,000' has no crew, no rate and no duration behind it and the "
 "staffing chart already funds three supers for 90 weeks."),

("4","OVERSTATED",
 "The sidewalk bridge lump does not agree with its own backup rows",
 "'Install sidewalk bridge and scaffolding around building  1 LS  $4,000,000', and directly "
 "beneath it, in his own hand: 1,126 LF @ $500 and 27,024 SF @ $75. Those foot to $563,000 + "
 "$2,026,800 = $2,589,800.",
 4_000_000.0, 2_589_800.0,
 "Ask him which number is right. Also ask why 1,126 LF - a sidewalk bridge is only required "
 "where there is a sidewalk, and the alleys and interior lot lines do not have one."),

("5","OVERSTATED",
 "$2,000,000 of interior scaffolding is priced for a method we are not using",
 "'Interior scaffolding  1 LS  $2,000,000', note '$75/SF for scaffolding' - which implies "
 "26,667 SF of floor plate scaffolded.",
 2_000_000.0, 400_000.0,
 "A roof LIFT jacks the existing roof on the lifter's own towers. You do not scaffold the floor "
 "plate to do it. Carry jacking access, rigging access and edge protection instead."),

("6","OVERSTATED",
 "2,000 coat check lockers",
 "'Coat Check Lockers  2000 EA @ $500 = $1,000,000', note '333LF'.",
 1_000_000.0, 262_500.0,
 "2,000 lockers serves 27% of a 7,440-capacity house at once. 750 at $350 is a generous "
 "January coat check. $500 each is a rate for a gym locker bank, not a cloakroom."),

("7","DOUBLE-COUNT",
 "The lighting package is bought twice",
 "'I/O lighting package throughout PROVIDED BY OTHERS  135,953 SF @ $12 = $1,631,436' sits "
 "inside the trade cost. Meanwhile the FF&E schedule separately carries Architectural Lighting "
 "$1,750,000 and Production - Performance Lighting $520,000, and division 270000 carries "
 "'LIGHTING AND CONTROLS - BY OWNER $40,000'.",
 1_631_436.0, 0.0,
 "His own line says 'provided by others'. If others provide it, it is not his cost. Keep the "
 "conduit, boxes and wiring in the electrical trade and delete the fixture package."),

("8","METHOD",
 "The budget still demolishes the roof instead of lifting it",
 "'Demo Pre-cast concrete roof  74,000 SF @ $8 = $592,000', note 'Abatement by others'. Roofing "
 "then rebuilds 56,085 SF at $36/SF.",
 592_000.0, 0.0,
 "A roof lift KEEPS the roof: you cut it free of the perimeter walls, jack it, extend the "
 "columns underneath and clad the new band. This is the same assumption the 4 Sep file made and "
 "it is the single biggest methodological difference between his estimate and ours."),

("9","UNDERSTATED",
 "Structural steel is still $0 on a project whose own scope line reads 'Add Second Level'",
 "Division 055100 carries nineteen lines and every one of them is zero quantity: 'F&I new Roof "
 "Trusses, girders, Columns at Music Hall area  0 TONS @ $6,000', 'Steel Framing at Mezz area  "
 "0 TONS @ $6,000', 'Steel Framing at upper balcony  0 TONS @ $6,000', 'Stage Lighting & AV "
 "support structure  0 LBS @ $8.00', railings, stairs, dunnage, lintels - all zero.",
 0.0, 0.0,
 "This is what the $12,000,000 'Trade Costs To Be Priced' plug is standing in for. His own "
 "$8.00/LB rate for stage lighting and AV support structure is worth keeping - our "
 "ground-supported rigging grid works out to $9.21/LB, so his rate corroborates ours."),

("10","UNDERSTATED",
 "106 line items carry a unit price and a quantity of zero",
 "Eight whole divisions total nothing: 055100 structural steel, 062000 rough carpentry, 064000 "
 "millwork (every bar in the building - 'Lobby Bar/Back Bar 0 LF @ $2,000', VIP, Music Hall GA, "
 "Mezzanine, Balcony, Upper lounge, Lower lounge, Foundry), 078100 fireproofing, 081000 doors "
 "and frames, 084100 storefront, 088000 glazing, 092300 tile. Drywall is priced at $119,664 "
 "with nine of its ten lines at zero.",
 0.0, 0.0,
 "Priced bottom-up at our own rates this scope is roughly $13.4M, against his $12M plug - so "
 "the plug is about right-sized, which is worth saying. But you cannot hold 10% contingency "
 "against scope nobody has priced. That is not contingency, it is a guess with a percentage "
 "on it."),

("11","UNDERSTATED",
 "Escalation on the building is blank",
 "Row 22: the $2,150,000 parking garage gets 'Escalation (Calculated at 5%)' = $107,500. "
 "Row 30: 'Escalation (Calculated at 5%)' on the $63,651,265 building is an empty cell.",
 0.0, 0.0,
 "Third version of this file in a row with that cell blank. On a 20-month programme it is real "
 "money and it should be funded. We carry 6%."),

("12","SCOPE",
 "Off-site parking garage, 86 spaces",
 "D21 '=86*25000' = $2,150,000, labelled 'Parking Garage - 260/spaces'. The label says 260, the "
 "formula says 86.",
 2_257_500.0, 0.0,
 "Our budget does not carry this at all. Decide whether off-site parking is in the deal, then "
 "fix the label or the formula - they disagree with each other."),
]

# ----------------------------------------- 4. THE BRIDGE, RUN THROUGH HIS OWN CHAIN
# Corrections applied to source cells. Mutually exclusive by construction.
CORR = [
 ("A", "Area basis: 8 lines re-cut off 135,953 / 132,542 SF onto 74,100 or 88,100 SF", -3_616_987.0),
 ("B", "Sprinklers: 2nd-floor mains priced on 50,000 SF against a 14,000 SF mezzanine deck "
       "(1st floor re-cut UP from 69,000 to 74,100 SF)", -519_600.0),
 ("C", "Sidewalk bridge cut to his own backup rows", -1_410_200.0),
 ("D", "Interior scaffolding cut to jacking and rigging access", -1_600_000.0),
 ("E", "Coat check lockers 2,000 EA -> 750 EA @ $350", -737_500.0),
 ("F", "I/O lighting package removed from trade - FF&E already buys it", -1_631_436.0),
 ("G", "Demo of the pre-cast roof removed - a lift keeps the roof", -592_000.0),
 ("H", "Division 013000 moved out of trade and into the general-conditions line", -3_034_000.0),
]
TRADE_FIX = R.TRADE + sum(v for _, _, v in CORR)

def rollup(trade, tbp, gc, esc_pct, cont_on_everything):
    """Re-runs the Budget Summary formula chain exactly as the file builds it."""
    esc  = trade * esc_pct
    ohp  = (trade + tbp + gc) * 0.09
    cc   = (trade + tbp + gc + ohp) * 0.10
    constr = trade + tbp + gc + ohp + cc + esc
    cont = ((R.OFFSITE + constr + R.SOFT + R.FFE) * 0.10 if cont_on_everything
            else (R.SOFT + R.FFE) * 0.10)
    return dict(esc=esc, ohp=ohp, cc=cc, constr=constr, cont=cont,
                tot=R.OFFSITE + constr + R.SOFT + R.FFE + cont)

HIS = rollup(R.TRADE, R.TBP, R.GCLINE, 0.00, True)
GC_FIX = (TRADE_FIX + R.TBP) * 0.0835        # Schimenti, 555 Johnson, Eric's own GC
FIX = rollup(TRADE_FIX, R.TBP, GC_FIX, 0.06, False)

V2_TOTAL = 64_648_067.0                      # our own bottom-up budget, V2 diligence reviewed
FIX_NO_GARAGE = FIX['tot'] - R.OFFSITE       # apples to apples: we carry no off-site parking

BRIDGE = [
 ("Off-site - parking garage + 5% escalation", R.OFFSITE,  R.OFFSITE),
 ("Trade cost",                                R.TRADE,    TRADE_FIX),
 ("Trade cost to be priced (the plug)",        R.TBP,      R.TBP),
 ("General conditions",                        R.GCLINE,   GC_FIX),
 ("Escalation on the building",                0.0,        FIX['esc']),
 ("Overhead, profit & insurance 9%",           R.OHP,      FIX['ohp']),
 ("Contractor contingency 10%",                R.CONTRCT,  FIX['cc']),
 ("CONSTRUCTION COST \u2014 the work plus its markups",                       R.CONSTR,   FIX['constr']),
 ("Soft costs",                                R.SOFT,     R.SOFT),
 ("FF&E",                                      R.FFE,      R.FFE),
 ("Contingency",                               R.CONTING,  FIX['cont']),
 ("TOTAL CAPITAL",                           R.TOTAL,    FIX['tot']),
]

# --------------------------------------------------------- 5. WHAT MOVED SINCE 4 SEP
MOVED = [
 ("015800","SCAFFOLDING & HOARDING",            0,  6_170_000),
 ("260000","ELECTRIC",                    558_750,  5_512_337),
 ("220000","PLUMBING",                  1_344_500,  3_717_250),
 ("100000","SPECIALTIES",                      0,  1_548_500),
 ("013000","PROJECT REQUIREMENTS",      1_696_000,  3_034_000),
 ("024100","DEMOLITION",                   30_408,  1_287_817),
 ("099000","PAINTING/PLASTER",                  0,  1_091_765),
 ("044200","STONE & CERAMICS",                  0,    764_340),
 ("096000","CARPET/RESILIENT FLOORING",         0,    765_048),
 ("230000","HVAC",                     5_300_000,  5_964_390),
 ("100500","ACOUSTICAL PANELS / K13",           0,    581_802),
 ("283100","FIRE ALARM",                        0,    521_906),
 ("096050","FLOOR PREPARATION",                 0,    515_298),
 ("096400","WOOD FLOORING",                     0,    373_050),
 ("320000","SITEWORK",                          0,    346_335),
 ("210000","FIRE PROTECTION",           1_026_000,  1_334_070),
 ("033000","CONCRETE",                          0,    177_450),
 ("083000","SPECIAL DOORS",                 6_000,     76_000),
 ("142000","ELEVATOR",                    600_000,    480_000),
 ("075000","ROOFING",                   5_736_276,  2_557_428),
 ("055100","STRUCTURAL STEEL & MISC METALS",    0,          0),
 ("064000","MILLWORK",                          0,          0),
 ("081000","DOORS, FRAMES & HARDWARE",          0,          0),
 ("084100","STOREFRONT",                        0,          0),
 ("088000","GLAZING",                           0,          0),
 ("078100","FIREPROOFING",                      0,          0),
 ("092300","TILE",                              0,          0),
 ("062000","ROUGH CARPENTRY",                   0,          0),
]

# ---------------------------------------------------------------- 6. THE ASKS
ASKS = [
("Which number is the sidewalk bridge?",
 "$4,000,000 as a lump, or the 1,126 LF @ $500 + 27,024 SF @ $75 = $2,589,800 written directly "
 "underneath it? And how many linear feet of actual public sidewalk does this building have?"),
("What is 'Project Labor, 1 LS, $2,000,000'?",
 "Give me the crew, the rate and the weeks. The General Conditions tab already funds three "
 "superintendents and a general super for 90 weeks."),
("Why is the whole building's escalation blank when the parking garage gets 5%?",
 "Row 30 has been empty in all three versions of this file."),
("Is 'Soft Costs & FFE Contingency 10%' meant to be a project contingency?",
 "The formula is =(D23+D31+D47+D65)*0.1 - that is 10% of everything, on top of the 10% "
 "contractor contingency already inside D31. As labelled it should be $1,507,723."),
("Where does 135,953 SF come from?",
 "It is not this building. 165 Randolph is 74,100 SF under roof with a 14,000 SF mezzanine "
 "inside that envelope. 555 Johnson is about 135,000 SF - I think this is a template carryover. "
 "Today it multiplies $10.3M of real trade cost."),
("Was HVAC priced on a load or on an area?",
 "$45.00 x 132,542 SF is one line with no tonnage. A 50 ft clear room with 7,440 people is a "
 "volume and an occupancy load, not a floor area. If it was priced on area, it needs to be "
 "re-priced by the mechanical engineer."),
("Does the interior scaffolding assume the roof comes off?",
 "Demo carries 74,000 SF of pre-cast roof demolition at $8. We are LIFTING the roof, not "
 "replacing it. If that is the assumption behind the $2,000,000 of interior scaffolding too, "
 "both lines need to be re-thought together."),
("Is the I/O lighting package his or ours?",
 "The line says 'provided by others' and sits in his trade cost at $1,631,436, while FF&E "
 "separately carries $1,750,000 of architectural lighting."),
("When do the 106 zero-quantity lines get priced?",
 "Structural steel, every bar, all doors, storefront, glazing, fireproofing, tile and most of "
 "the drywall. The $12,000,000 plug is roughly the right size - we price that scope at about "
 "$13.4M - but it is a plug, and contingency should not be charged on top of it."),
("Parking garage: 86 spaces or 260?",
 "The label says 260 spaces, the formula says =86*25000. And is off-site parking in this deal "
 "at all? We do not carry it."),
("Second floor, third floor, roof decks, balcony, upper and lower lounge, foundry, restaurant.",
 "This is a PROGRAMME question for us and Wake, not an estimating error - he priced what the "
 "test fit showed him. But it drives the sprinkler quantities, the fixture counts and the "
 "135,953 SF, so we need to settle it before the next version."),
]

# Finding 3's corrected figure is the 8.35% general-conditions line itself, which
# cannot be written until TRADE_FIX exists. Patch it in rather than hard-key it.
FINDINGS[2] = FINDINGS[2][:5] + (GC_FIX,) + FINDINGS[2][6:]
assert FINDINGS[2][5] is not None
