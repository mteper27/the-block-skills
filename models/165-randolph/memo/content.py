# -*- coding: utf-8 -*-
"""Single source for the three-part document. Page 1 questions, page 2
recommendations, then clarification. Rendered to HTML/PDF and DOCX."""

TITLE = "165 Randolph Ave — “The BLOCK”"
SUB   = "Questions, Recommendations & Clarification on the 16 September Master Development Budget"
BYLINE = "To: Thomas · cc: Nate (Wake)  —  From: Matthew Teper  —  17 September 2026"

# ---------------------------------------------------------------- PAGE 1
Q_INTRO = ("Referenced to your sheet and cell. Our reasoning is in the Clarification at the back; "
           "you should not need it to answer these.")
QUESTIONS = [
 # (cell / line, his label as it reads in the file, question)
 ("Budget Summary", [
   ("D67", "Soft Costs & FFE Contingency 10%", "The formula is `=(D23+D31+D47+D65)*0.1` \u2014 10% of the whole project, not of soft costs and FF&E. Which is intended? If it is a project contingency, does D29 stay?"),
   ("D30", "Escalation (Calculated at 5%) \u2014 building", "Blank. What should the building carry?"),
   ("D26", "Trade Costs To Be Priced \u2014 $12,000,000", "What scope is inside it, and when can it be priced?"),
   ("D28", "Overhead, Profit & Insurance (9% Combined)", "Applied to trade + D26 + D27. Is it intended to run on general conditions and on unpriced scope?"),
   ("D21", "Parking Garage \u2014 260/spaces", "Formula is `=86*25000`. 86 or 260? And is off-site parking in this deal?"),
   ("B8, D71", "SF: 135,953 / $ PER SF", "Where does 135,953 SF come from? Can the $/SF basis be stated on the sheet?"),
 ]),
 ("General Conditions", [
   ("GC tab + 013000", "General Conditions $3,141,000 / PROJECT REQUIREMENTS $3,034,000", "The same function carried twice \u2014 once on the tab, once inside trade cost?"),
   ("013000-11", "Project Labor \u2014 1 LS \u2014 $2,000,000", "Crew, rate and weeks?"),
 ]),
 ("Building & Fit-out Breakdown", [
   ("015800-1", "Install sidewalk bridge and scaffolding around building \u2014 $4,000,000", "The backup rows beneath (1,126 LF @ $500 + 27,024 SF @ $75) total $2,589,800. Which is right? How many LF of public sidewalk does the building front?"),
   ("015800-2", "Interior scaffolding \u2014 $2,000,000", "Staging what, at what rate, for how long? Does the sequence assume the ground-supported stage and towers are already erected?"),
   ("055100", "STRUCTURAL STEEL & MISC METALS \u2014 all 19 lines at zero", "When is this priced from the RFEM takeoff? Does $6,000/TON apply to the built-up plate columns?"),
   ("064000 / 078100 / 081000 / 084100 / 088000 / 092300", "Millwork, Fireproofing, Doors, Storefront, Glazing, Tile \u2014 all at zero", "When are these priced?"),
   ("230000-1", "HVAC System including BMS \u2014 132,542 SF @ $45", "Priced on load or on area? Can we see tonnage?"),
   ("260000", "I/O lighting package throughout \u2014 provided by others \u2014 $1,631,436", "FF&E line 310 carries *Architectural & Exterior Lighting $1,750,000*. Which of the two survives?"),
   ("100000", "Coat Check Lockers \u2014 2,000 EA @ $500", "Is 2,000 the intended count?"),
   ("220000", "W/C, Lavs, Urinals \u2014 178 / 154 / 51 @ $4,000", "Can we see the code fixture calculation?"),
   ("024100-19", "Demo Pre-cast concrete roof \u2014 74,000 SF @ $8", "Is the existing roof confirmed as pre-cast concrete?"),
 ]),
 ("Soft Cost & FF&E Detail", [
   ("201-2", "Roof Abatement \u2014 70,000 SF @ $21", "Where does the rate come from, and has the roof been sampled?"),
   ("211-1", "Attorney Fees \u2014 $0 (\u201cSLA Legal Fees carried in Feasibility DD\u201d)", "Are the SLA, cabaret and theater-classification filings inside the feasibility study already spent?"),
   ("500005 / 500006", "G.L. INSURANCE $0 / BUILDERS RISK INSURANCE $0", "Inside the 9%? Can your broker quote them separately, and quote an owner-controlled programme?"),
 ]),
]

# ---------------------------------------------------------------- PAGE 2
R_INTRO = ("What we would like to do to bring the number down, in the order it is worth doing. "
           "Where an item is yours to action, it is written as an ask.")
RECS = [
 ("Fix the four workbook items", "Thomas",
  "Contingency to its labelled base; general conditions in one place; delete the duplicated lighting package; reconcile the sidewalk bridge to its own backup. About **$11.8M** all-in and none of it is a re-estimate."),
 ("Restructure the contract", "Us + Thomas",
  "Cost of the work open-book. General conditions as a **rate × duration**, capped. Fee as a **fixed dollar amount**, not charged on general conditions or unpriced scope. Insurance as an actual broker premium, with an **owner-controlled programme** quoted alongside. One owner-held contingency. Please have your broker price it both ways."),
 ("Settle the programme", "Us + Nate",
  "Occupied terrace, third floor, restaurant, lounges, foundry. Every square foot removed takes steel, deck, sprinklers, fixtures, HVAC, finishes and general conditions with it. **$5–12M.**"),
 ("Second value-engineering pass on the structure", "Structural + Thomas",
  "VE1 already took 533,871 lb out of Rev 43 (21%) with no loss of programme. Ask for VE2 now the scheme is stable. **$1–3M.**"),
 ("Lower the high roof if +64 ft 6 in is not needed", "Nate + structural",
  "Steel, envelope, scaffolding, crane and erection all move together. **$1–3M.**"),
 ("Test a partial roof lift over the high-roof zone", "Rooflifters + structural",
  "The stage and mezzanine are ground-supported, so the 27,393 SF high roof carries weather only. Confirm what the existing roof is made of, then run Rooflifters Stage 3. Close to a wash on cost; the prize is weather exposure and the DOB route."),
 ("Shorten the programme", "Thomas",
  "90 weeks of staffing is $3,141,000. Each quarter off the schedule is about **$420,000** of general conditions before anything else."),
 ("Buy out long-lead packages early", "Thomas",
  "Steel, switchgear, elevators, HVAC plant. Every package fixed early collapses its share of escalation. **$1–2M.**"),
 ("Price the plug honestly, and expect it to rise", "Thomas",
  "055100 and 064000 off the takeoff and the test fit. We think D26 goes **up** when priced. Better now than at buyout, and it will not be read as your number moving."),
 ("Seating — wait for counsel", "Counsel + Nate",
  "3,714 chairs at $125 is a licensing input, not a furniture choice. Do not buy until the classification is ruled. **Up to $0.75M.**"),
 ("Off-site parking", "Us",
  "Confirm whether it is in the deal. **$2.26M.**"),
 ("Use your own benchmarks to right-size FF&E", "Thomas",
  "BPT $837K on 26 POS; soft goods $725k; audio $690k; lighting $450k. They cut both ways — they say the bar package is light and our PA is heavy."),
]
R_DONT = [
 ("Acoustic treatment", "Next to residential this is the licence to operate. We will not take the lower number."),
 ("The investigation package", "Phase I/II, existing-conditions survey, structural peer review, Rooflifters Stage 3: $435,000 that closes the unknowns contingency is being held against."),
]

# ---------------------------------------------------------------- CLARIFICATION
CLAR = [
 ("Where the numbers stand",
  ["| | Total | $/SF on 74,100 SF |\n| --- | --- | --- |\n| Master Development Budget, 16 Sep | $89,084,591 | $1,202 |\n| Our V2, before the takeoff | $64,648,067 | $872 |\n| Our V3, rebuilt on the measured steel | $77,897,555 | $1,051 |",
   "Our reconstruction of your trade cost ties to your Trade Cost cell to **$0.00** across 309 lines. Applying only the corrections that survive the takeoff, your budget lands near **$77,247,828** against our **$77,897,555** — about 0.8% apart. This is not a disagreement about how hard the building is to build."]),
 ("What the structural takeoff settles",
  ["The RFEM export (Rev 38, VE1) measures **1,994,335 lb** of new and replacement steel — **997.2 short tons**. The file’s tonnes column reads 904.62 (metric); pricing off it understates steel by 10.2%.",
   "**It is a rebuild, not a lift.** 124 of 243 column members start at or below +2 ft (450,114 lb, 62.4% of column steel); all 517 truss members are new between +56.5 and +64.5 ft; the *Existing Roof / Lower* level carries zero members; the words lift, jack, shore and splice appear nowhere in 8,658 rows. Your 74,000 SF of roof demolition is the method, not an error.",
   "**The roof carries no rigging.** High roof is 8.65 lb/SF of short-span W12/W6 framing — weather only. The stage and towers stand on their own footings and carry all production load. Please confirm in writing the roof design loads exclude rigging, so it is not quietly added back at DD. Separately, the lower roof at 20.81 lb/SF is the heaviest per SF in the building; why?",
   "**Where the steel actually is:** shared columns and vertical bracing, 718,634 lb, 37% of the whole — driven by 60 ft of column height and the occupied terrace, not the roof.",
   "**One rate flag:** 80 columns (202 tons) are shop-welded built-up plate girders, I 48/24 through I 69.023/24. $6,000/TON is the rolled-shape rate; we carry $8,400 for these."]),
 ("Two corrections we are taking back",
  ["**135,953 SF.** We had called it wrong. The model carries 146,508 SF gross and 120,119 SF enclosed floor; our 14,000 SF mezzanine was derived from occupancy loads and the model says 32,942 + 13,077 SF of seating. We can no longer prove your figure wrong — but it is unsourced and does not derive from the test fit, and 555 Johnson at $208.63/SF is 134,993 SF. We are asking for its derivation and for one agreed area schedule, from PD04 Rev 4.4, that every budget labels.",
   "**The roof method.** We had asked you to delete the roof demolition. Withdrawn. The partial-lift question above is ours to answer, not yours."]),
 ("What still needs fixing — $11,836,763 all-in",
  ["**Contingency, $6,590,876.** D67 computes 10% of the whole project on top of $5,786,479 of contractor contingency already inside D31. As labelled it is $1,507,723; $578,648 of it is contingency on contingency.",
   "**General conditions twice, $2,643,751.** $3,141,000 staffing chart plus $3,034,000 of division 013000 inside trade = 12.36% of trade. Schimenti ran 7.80% and 8.90% at 555 Johnson. *Project Labor $2,000,000* has no crew, rate or duration.",
   "**Sidewalk bridge, $1,859,913.** $4,000,000 lump; the backup rows beneath foot to $2,589,800. The $2,000,000 interior scaffolding we are no longer contesting outright — but the ground-supported stage and towers go up first and could carry the access.",
   "**Lighting bought twice, $2,151,701.** $1,750,000 in FF&E plus $1,631,436 of *I/O lighting package — provided by others* inside electrical.",
   "**Coat check lockers, $972,689.** 2,000 at $500 serves 27% of the house at once.",
   "**And the $12,000,000 plug is too small, not too big.** Measured structure alone is $16,710,249, of which $6,703,714 is bare steel, before millwork, doors, glazing, tile, fireproofing and drywall. We expect it to rise when priced."]),
 ("Why the fee structure matters",
  ["The 9% is currently earned on your own general conditions ($555,750 of fee, $672,458 all-in) and on the $12M of unpriced scope ($1,080,000, $1,306,800 all-in). Profit on the cost of your own staff is double-dipping; fee on a plug rises automatically when the plug is priced. A fixed fee removes both. Insurance is a quotable premium, not a margin — and under NY Labor Law 240 the owner is exposed whether or not the contractor holds the policy, so the only question is who buys it and at what markup."]),
 ("Deal structure, for the record",
  ["EBC owns the land; we sign a 30-year lease; Insomniac funds and builds out. Everything here is a leasehold improvement — at base case about $2.6M a year of capital before financing. The largest untested lever in the whole exercise is what EBC contributes to a build on its own land. Nobody has asked yet."]),
]
