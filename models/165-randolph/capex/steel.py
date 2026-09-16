# -*- coding: utf-8 -*-
"""Division 100 rebuilt from the measured takeoff, replacing our estimate.

Every quantity here comes from takeoff.py, which is the RFEM export verbatim.
Rates are NYC union supply-fabricate-deliver-erect, and where the estimator's
own file gives a rate we use his so the number cannot be argued about.
"""
import sys; sys.path.insert(0, '.')
import takeoff as T

TON = T.LB_PER_TON

def _t(system, kind):
    for s, k, n, lf, lb in T.MEMBERS:
        if s == system and k == kind: return lb / TON
    raise KeyError((system, kind))

def _lf(system, kind):
    for s, k, n, lf, lb in T.MEMBERS:
        if s == system and k == kind: return lf
    raise KeyError((system, kind))

# (description, qty, unit, rate, source)
STRUCTURE = [
 ("Beams & girders — rolled W-shapes", round(_t("Beams/girders","Rolled W-shape"),1), "TON", 6_000,
  "MEASURED: 992 members, 17,441 LF, 1,003,473 lb. Rate is THE ESTIMATOR'S OWN, from his "
  "unpriced 055100 line 'F&I new Roof Trusses, girders, Columns at Music Hall area @ $6,000/TON'."),
 ("Beams & girders — HSS tube", round(_t("Beams/girders","HSS tube"),1), "TON", 6_600,
  "MEASURED: 104 members, 338 LF. Tube carries more cutting, capping and end prep than rolled."),
 ("Columns — BUILT-UP PLATE GIRDER", round(_t("Columns/extensions","Built-up plate girder"),1), "TON", 8_400,
  "MEASURED: 80 members, 1,320 LF, 403,988 lb. These are NOT rolled shapes — they are "
  "shop-welded from plate, I 48/24/0.438/1.375 through I 69.023/24, on grids B and E at 60.00 "
  "LF each. Plate girder columns run 30-45% over rolled because of the welding, NDT and "
  "handling. $6,000/TON IS THE WRONG RATE FOR THIS LINE."),
 ("Columns — rolled W-shapes", round(_t("Columns/extensions","Rolled W-shape"),1), "TON", 6_000,
  "MEASURED: 148 members, 3,107 LF. Estimator's own rate."),
 ("Columns — HSS tube", round(_t("Columns/extensions","HSS tube"),1), "TON", 6_600,
  "MEASURED: 15 members, 197 LF."),
 ("Roof trusses — fabricated assemblies", round(_t("Truss components","Rolled W-shape"),1), "TON", 7_200,
  "MEASURED: 517 members, 5,187 LF, 135,424 lb, all between +56.5 ft and +64.5 ft. Truss "
  "fabrication carries more shop labour per ton than plain framing."),
 ("Braces — HSS tube", round(_t("Braces","HSS tube"),1), "TON", 6_600,
  "MEASURED: 281 members, 4,781 LF."),
 ("Braces — rolled W-shapes", round(_t("Braces","Rolled W-shape"),1), "TON", 6_000,
  "MEASURED: 21 members, 610 LF. Estimator's own rate."),
 ("Cold-formed steel — BOH & closure framing", _lf("Cold-formed steel","CFS stud / track / strap"), "LF", 22,
  "MEASURED: 2,686 pieces, 11,557 LF, 40,622 lb. CEMCO 1200S350-68 joists, 800S162-54 studs, "
  "track, blocking and flat strap. Priced per LF installed, which is how CFS is bought."),
]

CONNECTIONS = [
 ("Connection design & shop detailing", 1, "LS", 285_000,
  "976.9 tons of hot-rolled with built-up plate columns and a trussed high roof. Detailing and "
  "connection design is a separate engineering scope from the EOR's model."),
 ("Column base plates, anchor bolts & setting", T.FOOTINGS, "EA", 4_200,
  f"MEASURED: {T.FOOTINGS} footing locations in VE1, up from 81 in Rev 43."),
 ("Grouting at column bases & truss bearings", 1, "LS", 38_000,
  "The estimator's own 033000 line 'Grouting at Steel Trusses & Column Base Plates', which he "
  "left at zero quantity with a $15,000 rate. Scaled to 124 locations."),
 ("Shear studs & deck welding", round(T.FLOOR_SF), "SF", 1.85,
  f"MEASURED: {T.FLOOR_SF:,.0f} SF of composite floor and tiered seating."),
 ("Crane, rigging & hoisting for erection", 1, "LS", 940_000,
  "60 ft built-up columns and 150 ft trussed girders in a constrained Brooklyn lot. This is a "
  "crawler or tower crane over months, not a boom truck."),
 ("Erection engineering, temporary bracing & survey", 1, "LS", 265_000,
  "Stability of a 64 ft frame during erection is its own design."),
 ("Special & controlled inspections — structural", 1, "LS", 195_000,
  "NYC controlled inspection of welding, bolting and high-strength connections on 976.9 tons."),
]

FOUNDATIONS = [
 ("New column footings", T.FOOTINGS, "EA", 11_500,
  f"MEASURED: {T.FOOTINGS} locations. Rate is above our old $7,500 because these carry 60 ft "
  "built-up columns and a high roof, not a mezzanine. GEOTECH-DEPENDENT — 13 borings at "
  "50 ft are in the soft costs and not yet done."),
 ("Excavation, spoil removal & disposal", T.FOOTINGS, "EA", 3_400,
  "Per footing, replacing our old blanket 74,100 SF x $6.50. The takeoff gives locations, so "
  "price locations."),
 ("Underpinning at existing footings", 24, "EA", 9_500,
  "CARRIED FORWARD from our V2 — the takeoff does not enumerate underpinning. Confirm "
  "against the geotech and the existing foundation drawings."),
 ("Rebar, dowelling & pier caps", 1, "LS", 145_000, "Scaled from our V2 at 124 locations."),
 ("Slab cut, patch & pour-back at new columns", T.FOOTINGS, "EA", 2_600, "Measured locations."),
]

DECK_AND_ENVELOPE = [
 ("Composite metal deck & concrete — floor & tiered seating", round(T.FLOOR_SF), "SF", 34,
  f"MEASURED: {T.FLOOR_SF:,.0f} SF (mezzanine/floor 32,942 + tiered seating 13,077)."),
 ("Metal roof deck", round(T.ROOF_SF), "SF", 9.50,
  f"MEASURED: {T.ROOF_SF:,.0f} SF across terrace, lower roof, high roof and caps."),
 ("BOH CFS roof deck", round(T.BOH_ROOF_SF), "SF", 9.50, "MEASURED."),
 ("New CMU — walls, shafts & closure", round(T.CMU_SF), "SF", 35,
  f"MEASURED: {T.CMU_SF:,.0f} SF, up from 23,330 in Rev 43. Rate is THE ESTIMATOR'S OWN 042000 "
  "rate, $35/SF, which he left at zero quantity."),
 ("Spray-applied fireproofing on new steel", round(T.FLOOR_SF + T.ROOF_SF), "SF", 5,
  "Rate is THE ESTIMATOR'S OWN 078100 rate, $5.00/SF, which he left at zero quantity across "
  "all three of his fireproofing lines."),
]

GROUPS = [
 ("Structural steel — MEASURED off the RFEM model", STRUCTURE),
 ("Erection, connections & inspection", CONNECTIONS),
 ("Foundations for the new load path", FOUNDATIONS),
 ("Deck, masonry & fireproofing", DECK_AND_ENVELOPE),
]

def total():
    return sum(q * r for _, g in GROUPS for d, q, u, r, s in g)

# What this division REPLACES in V2: the roof-lift division (100) and the
# mezzanine division (300). Division 200 (stage, towers, rigging grid) is NOT
# in the structural model and is carried forward untouched.
V2_REPLACED = [
 ("100 Roof lift contract — YOUR QUOTE",              3_500_000.0),
 ("100 Foundations for the new load path",               1_087_650.0),
 ("100 Roof-to-wall closure",                              241_643.0),
 ("100 Envelope completion at the new band",               604_395.0),
 ("100 Roof reinstatement",                                782_600.0),
 ("100 Fireproofing on new steel",                         180_000.0),
 ("100 MEP disconnect & reinstatement",                    550_000.0),
 ("100 Fire separation",                                   200_000.0),
 ("300 Mezzanine foundations",                             247_800.0),
 ("300 Mezzanine structure",                             1_316_000.0),
 ("300 Raised premium tier — replaces built boxes",    261_000.0),
 ("300 Egress & guarding",                                 287_216.0),
]
# Two of those are scope the takeoff does NOT cover and must be carried forward.
CARRY_FORWARD = [
 ("MEP disconnect & reinstatement", 1, "LS", 550_000,
  "Carried forward from V2. The structural model has nothing to say about MEP."),
 ("Fire separation", 1, "LS", 200_000, "Carried forward from V2."),
 ("Egress & guarding at raised levels", 1, "LS", 287_216,
  "Carried forward from V2. Stairs and railings appear in the takeoff only as a few W-shapes; "
  "guarding, treads and nosings do not."),
]
GROUPS.append(("Carried forward — not in the structural model", CARRY_FORWARD))
