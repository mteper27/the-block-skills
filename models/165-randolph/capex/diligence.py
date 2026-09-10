# -*- coding: utf-8 -*-
"""Review of the 165 Randolph diligence folder uploaded 10 Sep 2026.

26 files. Two of them are readable cost documents and they are the most useful
third-party evidence in the whole exercise: Schimenti Construction's conceptual
budgets for 555 Johnson Avenue, addressed to Eric Cohen at EBC Capital — our own
landlord, same submarket, open-shop labour. Everything else is a scanned drawing,
a vector CAD plot or a custom-font PDF with no recoverable text.
"""

# --- what actually arrived, and whether it could be read -------------------
DOCS = [
 ("555 Johnson Ave_Conceptual Summary_190108.pdf","READ",
  "Schimenti Construction to Eric Cohen, EBC Capital, 8 Jan 2019. Full conceptual budget by CSI division with $/SF, project timeline, and qualifications. THE most useful document in the folder."),
 ("555 Johnson Avenu_Conceptual Analysis_R1 Partial Reuse.pdf","READ",
  "Schimenti, 11 Jan 2019. The PARTIAL SITE RE-USE option — keep existing buildings rather than demolish. The direct analogue to what we are doing at 165 Randolph."),
 ("555 Johnson Ave_Conceptual Summary_190108(1).pdf","DUPLICATE","Byte-identical to the file above."),
 ("555 Johnson Avenu_Conceptual Analysis_R1 Partial Reuse(1).pdf","DUPLICATE","Byte-identical to the partial-reuse file above."),
 ("180730- Production Studios Budget .pdf","PARTIAL",
  "A three-column budget (three scheme sizes) with CSI row labels. The row labels decode — General Requirements, Sitework, Concrete, Masonry, Metals, Carpentry, Thermal & Moisture Protection, Doors & Windows, Finishes, ACOUSTIC WALLS, Equipment, Furnishings, HVAC, Plumbing, Sprinkler, Electrical — but the amounts use a custom font encoding that does not decode reliably. DO NOT quote figures from this file until someone opens it and reads them out."),
 ("180730- Production Studio CM Services.pdf","NO TEXT","Custom font encoding, no recoverable text. Likely the CM fee structure — worth reading manually, it would settle the general-conditions and fee argument outright."),
 ("537 Johnson Av_Assessment of Work (09.14.16).pdf","NO TEXT","Scanned. THE ROOF-LIFT PRECEDENT — a structural assessment of an existing building on the same block. Highest-value unread document."),
 ("537 Johnson Av_Draft Recommended Means & Methods (03.22.17).pdf","NO TEXT","Scanned. Means and methods for the structural work. Directly relevant to how the lift gets sequenced."),
 ("537 Johnson Av_Proposed Structural Plans (03.22.17).pdf","NO TEXT","Vector CAD plot."),
 ("537 Johnson Av_Proposed Conditions+Take off (05.12.17).pdf","NO TEXT","Vector CAD plot. A TAKE-OFF — quantities we could compare against."),
 ("537-561 Johnson Av_Progress Structural Plans (01.19.17).pdf","NO TEXT","Vector CAD plot."),
 ("50 Kip_Pile Cap Adequacy Check (03.22.17).pdf","NO TEXT","Scanned calculation. Foundation capacity — bears directly on both the roof-lift load path and the rigging-grid footings."),
 ("65 Kip_Pile Cap Adequacy Check (03.22.17).pdf","NO TEXT","Scanned calculation, the 65-kip case."),
 ("198 Randolph Street_Alt.2_11-23-2016.pdf","NO TEXT","Scanned drawing set. 198 Randolph is the smaller sibling of this building."),
 ("198 Randolph Street_11-23-2016.dwg","NOT READABLE","AutoCAD binary. Needs CAD software."),
 ("20180907 Randolph.dwg","NOT READABLE","AutoCAD binary."),
 ("20181207_555 Johnson Schematic Design Drawings.pdf","NO TEXT","12.9 MB vector drawing set by Relativity Architects — the documents Schimenti priced against."),
 ("20180613_NF Campus_PLANS & RENDERS.pdf","NO TEXT","Vector plans and renders."),
 ("Acoustical Data.pdf","NO TEXT","Scanned. Would inform the acoustic treatment line, which is a licence-to-operate item."),
 ("20190403 SK-01 DEMISING PARTITION.pdf","NO TEXT","Vector sketch."),
 ("A1 01032017.pdf / A1 12262016.pdf","NO TEXT","Two revisions of an A1 sheet."),
 ("1302046 & 1302047.pdf","NO TEXT","Scanned — looks like DOB job numbers."),
 ("20170523 Covered.jpg / 20170523 Roof Soccer Night.jpg","IMAGE","Photographs of a covered roof and a rooftop pitch at night."),
]

# --- Schimenti 555 Johnson, division by division ---------------------------
# (division, full scheme $, full $/SF, partial-reuse $, partial $/SF)
COMPS = [
 ("2-000  Existing conditions",  3_128_000, 23.17, 1_525_000, 25.00),
 ("3-000  Concrete / precast",   6_973_000, 51.65, 2_078_519, 34.07),
 ("4-000  Masonry",              3_996_000, 29.60,   765_000, 12.54),
 ("5-000  Steel",                2_105_000, 15.59, 1_905_000, 31.23),
 ("6-000  Wood & plastics",        168_000,  1.24,    77_156,  1.26),
 ("7-000  Thermal, moisture & fireproofing", 3_062_000, 22.68, 1_860_000, 30.49),
 ("8-000  Doors & windows",        460_000,  3.41,    36_000,  0.59),
 ("9-000  Finishes",               303_000,  2.24,   108_500,  1.78),
 ("10-000 Specialties",             25_000,  0.19,    25_000,  0.41),
 ("14-000 Elevators & lifts",      427_000,  3.16,         0,  0.00),
 ("15-000 Mechanical (FP + plumbing + HVAC)", 4_258_000, 31.54, 1_200_000, 19.67),
 ("16-000 Electrical (service, power, alarm)", 3_260_000, 24.15, 1_530_000, 25.08),
 ("       CONSTRUCTION SUBTOTAL",28_165_000,208.63,11_110_174,182.13),
 ("17-000 General conditions",   2_198_000, 16.28,   989_100, 16.21),
 ("18-000 Insurance, fees & bonds", 2_002_000, 14.83,  998_190, 16.36),
 ("       CORE & SHELL TOTAL",   32_365_000,239.74,13_097_464,214.71),
 ("       Fit-out per scope letter", 8_614_000, 81.42,10_958_000,103.57),
 ("       GRAND TOTAL",          40_979_000,303.55,24_055_464,178.19),
]

# --- findings: (topic, what the diligence says, what we carried, so what, action) ---
F = [
("GENERAL CONDITIONS IS THE ONE HARD NUMBER WE NOW HAVE",
 "Schimenti priced general conditions at $2,198,000 on a $28,165,000 construction subtotal = 7.80% on the full 555 Johnson scheme, and $989,100 on $11,110,174 = 8.90% on the partial-reuse option. Both open shop, both for Eric Cohen, both in this submarket.",
 "11.0%, which was my own benchmark rather than a quote.",
 "Two real data points from our own landlord's general contractor average 8.35%. My 11% was too high. Changed to 8.5%.",
 "APPLIED — rate moved from 11% to 8.5%. Worth $954,153 at the current trade cost. Push the estimator to justify anything above 8.5% with a staffing chart and a duration, not a percentage."),

("OVERHEAD, PROFIT & INSURANCE IS ABOUT RIGHT — DO NOT CUT IT",
 "Schimenti's insurance/fees/bonds line is 7.11% (full) and 8.98% (partial reuse). CRITICALLY, both lines say 'Construction Contingency — Excluded' and 'Builder's Risk Insurance — Excluded'.",
 "9.0%, described as including insurance.",
 "Comparing like with like, 9% including builder's risk against ~8% excluding it is consistent. This rate is NOT the soft one. The soft one was general conditions.",
 "NO CHANGE. Stop arguing about this line and spend the leverage on general conditions and the roof."),

("CONTINGENCY BELONGS TO YOU, NOT THE CONTRACTOR — CONFIRMED",
 "Schimenti explicitly EXCLUDES construction contingency from both budgets.",
 "One $5,000,000 owner-held contingency below the line.",
 "A real NYC GC pricing for your own landlord excluded contractor contingency entirely. The restructure you asked for matches how this market actually quotes.",
 "NO CHANGE — this validates the structure. If our estimator insists on a 10% contractor contingency he holds and keeps, ask him why Schimenti didn't."),

("THE 135,953 SF ERROR HAS A TRACEABLE ORIGIN",
 "555 Johnson is ~135,000 SF: $28,165,000 divided by $208.63/SF = 134,993 SF.",
 "Thomas's Master Development Budget header states SF: 135,953. The building is 74,100 SF.",
 "The wrong area almost certainly came across from the 555 Johnson job. It is not a typo, it is a template carried over from a different building on the next block.",
 "ASK. This makes the correction much easier to land: you are not telling him he cannot count, you are showing him which file it came from. Every SF-driven line in his schedule needs re-running at 74,100."),

("OPEN SHOP IS THE NORM ON ERIC'S PROJECTS",
 "Schimenti qualification 1.1: 'Labor Type — Open Shop'. Work hours 7am-3:30pm, single shift. A NYC licensed superintendent is required.",
 "The Rooflifters 2022 rate card, whose union status we flagged as unknown.",
 "Open shop is what got priced across the street. It supports non-union pricing as the base case and it means the Rooflifters card is probably the right basis, not a low one.",
 "ASK Rooflifters to confirm open shop, and hold the estimator to a single-shift 7am-3:30pm assumption unless he is pricing overtime for a reason he can name."),

("THE CONSTRUCTION WINDOW COMP IS 60 WEEKS, NOT 24 MONTHS",
 "Schimenti: '70 week active project schedule and 60 weeks of construction.' Their timeline runs design kick-off Feb 2019 to TCO Feb 2021, with foundation 2 months, core and shell 6-8 months, interior fit 4 months.",
 "24 months of sidewalk shed rental at $23,958/month.",
 "60 weeks is 13.8 months of construction. Our roof lift genuinely extends the programme beyond their case, so I have NOT cut the duration — but 24 months now needs defending against a real comp rather than being assumed.",
 "VERIFY with the estimator. Every month you take out of the programme is $23,958 of shed alone, before general conditions. An 18-month shed saves $143,748."),

("MEP IS 3.4x THE COMP AND THAT IS THE SECOND-BIGGEST QUESTION AFTER THE ROOF",
 "555 Johnson mechanical + electrical = $31.54 + $24.15 = $55.69/SF. Elevators $3.16/SF.",
 "Our division 500 excluding conveying is $191.58/SF. Conveying at $4.05/SF is a near-perfect match to their $3.16.",
 "The elevator match tells us the comparison is meaningful. A 7,440-occupant assembly venue legitimately carries far more MEP than production studios — ventilation alone for 7,440 people is 110,000-150,000 CFM, and body heat is over 300 tons before a single fixture. But 3.4x is a big number to accept on trust, and it is the same doubt as the HVAC basis question.",
 "ASK. This is now the strongest reason to get a written answer on whether HVAC was priced on a load calculation or a rate per square foot."),

("RENOVATION AND FIT-OUT OF AN EXISTING BUILDING NEARBY RAN $120-135/SF",
 "Schimenti's partial-reuse option prices Lots 25 & 37 renovation and fit-out at $2,760,000 over 23,000 SF = $120/SF, and Lot 42 at $4,050,000 over 30,000 SF = $135/SF.",
 "Not directly comparable — those are light industrial and office fit-outs, not an 8,000-cap venue.",
 "Useful as a floor, not a target. It tells you what ordinary warehouse conversion costs on this block, so any line in our budget that is just ordinary construction should sit near that band.",
 "Use it to sanity-check the non-venue-specific parts: BOH, offices, circulation, restroom blocks."),

("GEOTECHNICAL WORK BEFORE FOUNDATION PRICING — THEIR FIRST RECOMMENDATION",
 "Schimenti's recommended next steps lead with: 'Conduct a GeoTechnical Survey of Existing Soil Conditions, Probes and Test Pits. Better information on the existing conditions will allow a targeted foundation and sub grade approach.' Their timeline puts test pits and additional borings before CDs are issued for foundations.",
 "$150,000 for 13 borings 50 ft deep, plus $85,000 existing-conditions survey and scan.",
 "We carry borings but not test pits and probes as a separate item, and their sequencing point is the real one: the survey comes BEFORE foundation pricing, not alongside it.",
 "SEQUENCE IT FIRST. This is also the strongest single argument for holding the $5,000,000 contingency: their own GC says foundation cost is unknowable until this is done."),

("ADD ALTERNATE PRICING EXISTS FOR ADDING A FLOOR — RELEVANT TO THE BALCONY QUESTION",
 "Schimenti priced 'Add 1 Floor to Lot 25 & 37' at $9,450,000, noted as reinforce plus core and shell.",
 "Thomas carries steel framing at an upper balcony at QTY 0 — a third level that is not in our model at all.",
 "Adding a floor to an existing building is a nine-figure-per-acre proposition, not a line item. It is a reminder that the upper balcony is a scope decision with real money behind it, not a detail.",
 "DECIDE. If the test fit keeps a balcony above the mezzanine, it needs pricing as a structural addition — new steel, new egress, new sprinkler, new seating."),

("ACOUSTIC WALLS APPEAR AS THEIR OWN DIVISION IN THE PRODUCTION STUDIO BUDGET",
 "The Production Studios budget carries 'Acoustic Walls' as a top-level trade line alongside Concrete, Masonry and Metals.",
 "Acoustic treatment is grouped under division 400 as a licence-to-operate item.",
 "Confirms that acoustic scope is treated as a major trade on this kind of building rather than a finish, which is how we treat it.",
 "NO CHANGE — but the Acoustical Data.pdf in this folder is a scanned document nobody has read. It may contain the actual STC targets, which would let us price the treatment instead of allowing for it."),
]

NOT_READ = [
 ("537 Johnson Av_Assessment of Work (09.14.16).pdf",
  "A structural assessment of an existing building on the same block. This is the closest thing to a roof-lift precedent in the folder and it is scanned, so no text came out. Reading it could confirm or kill the whole lift approach."),
 ("50 Kip and 65 Kip Pile Cap Adequacy Check (03.22.17).pdf",
  "Foundation capacity calculations. These bear on two live numbers: the roof-lift load path ($1.33M of swing on whether footings are inside the Rooflifters quote) and the rigging-grid footings we priced at $8,500 each."),
 ("537 Johnson Av_Draft Recommended Means & Methods (03.22.17).pdf",
  "How the structural work was sequenced. Relevant to whether the grid can be erected through the open roof."),
 ("Acoustical Data.pdf",
  "Would let us price acoustic treatment to a target instead of carrying an allowance."),
 ("180730- Production Studio CM Services.pdf",
  "Almost certainly the CM fee structure. Would settle the general-conditions and fee argument outright rather than by comparison."),
 ("198 Randolph Street_Alt.2 and the two .dwg files",
  "198 Randolph is the smaller sibling building. The DWGs need CAD software this container does not have."),
]
