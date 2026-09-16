# -*- coding: utf-8 -*-
"""What the structural takeoff changes about the 16 Sep audit.

The takeoff is the structural engineer's own model. Where it contradicts an
assumption of ours, the takeoff wins and the finding built on that assumption
has to come off the table. Two of my findings do.
"""
import sys; sys.path.insert(0, '.')
import takeoff as T, sept16_raw as R

CASCADE = 1.09 * 1.10 * 1.10

GROSS = [
 ("Ground floor",                              74_100.0, "CLAUDE.md, under roof"),
 ("Mezzanine / floor (+20 ft)",                32_942.0, "TAKEOFF, VE1 — we assumed 14,000"),
 ("Additional tiered seating",                 13_077.0, "TAKEOFF, VE1 — we assumed none"),
 ("Occupied terrace (+45 ft 7)",               26_389.0, "TAKEOFF, VE1 — the model calls it OCCUPIED"),
]
GROSS_SF = sum(v for _, v, _ in GROSS)                      # 146,508
FLOOR_SF = 74_100.0 + 32_942.0 + 13_077.0                   # 120,119 enclosed floor

# (finding, what I said on 16 Sep, what the takeoff says, verdict, $ I claimed)
REVISED = [
("Area basis — $11.3M of trade priced on 135,953 SF",
 "I said 135,953 SF is a floor area this building does not have, and re-cut eight electrical, "
 "HVAC, paint and alarm lines plus two sprinkler lines onto 74,100 or 88,100 SF. I called it "
 "$4,710,823 of trade cost, $6,213,104 all-in.",
 f"The model has {GROSS_SF:,.0f} SF of gross area: 74,100 ground + 32,942 mezzanine/floor + "
 f"13,077 tiered seating + 26,389 occupied terrace. Enclosed floor alone is {FLOOR_SF:,.0f} SF. "
 "Our 14,000 SF mezzanine was derived from test-fit occupancy loads; the structural model says "
 "it is 32,942 SF plus 13,077 SF of seating. His 135,953 SF sits between the enclosed floor "
 "and the gross, which is exactly where a stacked-area figure should sit.",
 "WITHDRAWN. His denominator is defensible. Sprinkler coverage of 119,000 SF against a "
 "measured 120,119 SF of enclosed floor is close to right, and his 50,000 SF second-floor line "
 "lands near the measured 46,019 SF. I was wrong about this and the correction comes off.",
 -6_213_104.0),

("Roof method — he demolishes, we lift",
 "I said his 74,000 SF of pre-cast roof demolition at $8/SF was pricing the wrong method, "
 "because a roof lift keeps the roof. $592,000 of trade, $780,789 all-in.",
 "The structural model does not lift anything. 124 of 243 columns start at or below +2 ft "
 "— 450,114 lb, 62.4% of column steel — which is a new full-height column off the "
 "slab. Only 25 members start at the +20 ft existing roof line. All 517 truss members are new, "
 "between +56.5 and +64.5 ft. The level 'Existing Roof / Lower' carries ZERO members. The "
 "words lift, jack, shore, splice and underpin appear nowhere in 8,658 rows.",
 "WITHDRAWN AND REVERSED. He and the structural engineer are building the same building. OUR "
 "roof-lift assumption is the outlier, and it is the single biggest thing to settle.",
 -780_789.0),

("Interior scaffolding — $2,000,000",
 "I cut it to $400,000 on the grounds that a lift jacks the roof on the lifter's own towers "
 "and does not need the floor plate scaffolded. $1,600,000 of trade, $2,110,240 all-in.",
 "If the roof comes off and a 64 ft frame goes up inside the existing walls, access, edge "
 "protection and interior staging are real and substantial.",
 "WEAKENED, NOT WITHDRAWN. The $4,000,000 sidewalk-bridge lump still disagrees with his own "
 "$2,589,800 of backup rows, and that half of the finding stands. Hold the interior scaffolding "
 "at his number until he shows the staging plan.",
 -2_110_240.0),

("Contingency computed on the whole project",
 "D67 reads 'Soft Costs & FFE Contingency 10%' and computes =(D23+D31+D47+D65)*0.1.",
 "The takeoff has nothing to say about a spreadsheet formula.",
 "STANDS. $6,590,876 over its own label, $578,648 of it contingency on contingency.",
 0.0),

("General conditions charged in two places",
 "$3,141,000 below the line plus $3,034,000 of division 013000 inside trade cost = 12.36% "
 "against Schimenti's 7.80% and 8.90%.",
 "Unaffected.",
 "STANDS.", 0.0),

("Coat check lockers, 2,000 at $500",
 "$1,000,000 for lockers serving 27% of the house.",
 "Unaffected — though a building with 120,119 SF of enclosed floor has more room for them "
 "than one with 88,100.",
 "STANDS.", 0.0),

("Architectural lighting bought twice",
 "$1,750,000 in FF&E plus $1,631,436 of 'I/O lighting package provided by others' inside the "
 "electrical trade.",
 "Unaffected. The per-SF portion of that line is now defensible, but buying the package twice "
 "is not.",
 "STANDS.", 0.0),

("Structural steel at $0 and the $12,000,000 plug",
 "I said the plug was right-sized — $12,000,000 against $10,614,464 of scope we price "
 "— and told you not to negotiate it.",
 "The measured structure alone prices at $16,710,249 in our V3, of which $6,703,714 is bare "
 "steel by the ton. His plug has to cover that PLUS all millwork, doors, storefront, glazing, "
 "tile, fireproofing and most of the drywall.",
 "REVERSED IN THE OTHER DIRECTION. The plug is far too SMALL. Do not negotiate it — but "
 "do not take comfort from it either. When he prices it, his total goes UP, not down.",
 0.0),
]
WITHDRAWN = sum(v for *_, v in REVISED)

OLD_CORRECTION = -20_940_896.0    # what the 16 Sep audit bridge produced
NEW_CORRECTION = OLD_CORRECTION - WITHDRAWN
