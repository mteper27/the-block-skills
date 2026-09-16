# -*- coding: utf-8 -*-
"""V3 — our budget rebuilt on the measured structural takeoff.

What changes from V2, and only this:
  1. Division 100 is replaced wholesale. It was a roof-LIFT division built on
     assumption. It is now the RFEM takeoff, priced by the ton.
  2. Division 300 (mezzanine) is absorbed into 100 — the takeoff prices the
     mezzanine steel as part of one frame. Only egress and guarding survive.
  3. The new-CMU lines come out of division 400 masonry, because the takeoff's
     39,248 SF of new CMU already covers them. Patching, infill and repointing
     of EXISTING fabric stay in 400.
  4. A roofing package is added. V2 carried 'roof reinstatement' because a lift
     keeps the roof. The model builds new roofs at +45.6, +60.5 and +64.5 ft,
     so they need membrane, insulation and a terrace walking surface.
  5. Safety protection at raised levels scales from 14,000 SF to the measured
     46,019 SF of elevated floor.
Divisions 200 (stage, towers, rigging grid), 500, 600, 700 and 800 are
UNTOUCHED — the structural model has nothing to say about any of them.
"""
import sys; sys.path.insert(0, '.')
import detail, steel, takeoff as T

ROOFING = [
 ("Roof membrane, insulation & flashing — all new roofs", round(T.ROOF_SF), "SF", 36,
  f"CONSEQUENCE OF THE METHOD CHANGE, not from the takeoff. {T.ROOF_SF:,.0f} SF of new roof "
  "deck needs a new roof. Rate is THE ESTIMATOR'S OWN 075000 rate of $36/SF. V2 carried "
  "'roof reinstatement' at $6/SF because a lift keeps the roof it already has."),
 ("Occupied terrace — pavers on pedestals", round(T.area("Terrace / maintenance")), "SF", 31,
  "MEASURED: 26,389 SF. The model calls this level 'Occupied Terrace (+45 ft 7 in)', so it "
  "needs a walking surface. Rate is the estimator's own paver rate."),
 ("New roof drains & leaders", 18, "EA", 8_500, "Carried forward from V2."),
 ("Roof dunnage for HVAC equipment", 8, "LOC", 20_000,
  "Carried forward from V2. Matches the estimator's own unpriced 055100 line at $20,000/LOC."),
 ("Roof penetrations framing for exhaust", 1, "LS", 25_000, "Carried forward from V2."),
]

# CMU lines in division 400 that the takeoff's 39,248 SF now covers.
DROP_FROM_400 = {
 "New masonry wall at entry lobby",
 "CMU elevator tower at entrance",
 "CMU elevator tower at stage",
 "CMU at back wall of music hall",
}

def build():
    """Returns the V3 line schedule in detail.py's own shape."""
    out = []
    for code, name, groups in detail.D:
        if code == "100":
            out.append(("100", "PRIMARY STRUCTURE — MEASURED FROM THE RFEM TAKEOFF",
                        list(steel.GROUPS) + [("Roofing — new roofs need new roofing", ROOFING)]))
            continue
        if code == "300":
            continue                      # absorbed into 100
        g2 = []
        for gname, lines in groups:
            if code == "400" and gname == "Masonry":
                lines = [l for l in lines if l[0] not in DROP_FROM_400]
                lines = lines + [("New CMU — see division 100",  0, "SF", 0,
                                  "MOVED. The takeoff measures 39,248 SF of new CMU across the "
                                  "whole building and it is priced in division 100. Patching, "
                                  "infill and repointing of EXISTING masonry stay here.")]
            if code == "400" and gname == "Rough carpentry & protection":
                lines = [(("Safety at new raised levels", round(T.FLOOR_SF), "SF", 2,
                           f"RESCALED from 14,000 SF to the measured {T.FLOOR_SF:,.0f} SF of "
                           "elevated floor and tiered seating.")
                          if l[0] == "Safety at new mezzanine build-outs" else l) for l in lines]
            g2.append((gname, lines))
        out.append((code, name, g2))
    return out

def total(D, codes=None):
    t = 0.0
    for code, name, groups in D:
        if codes and code not in codes: continue
        for g, lines in groups:
            for d, q, u, r, s in lines:
                try: t += float(q) * float(r)
                except (TypeError, ValueError): t += float(q) * 25.0   # seat-rate toggle
    return t

D3 = build()
TRADE_CODES = ("000", "100", "200", "400", "500")
KITCHEN = ("800",)

def trade():
    t = total(D3, TRADE_CODES)
    for code, name, groups in D3:
        if code != "800": continue
        for g, lines in groups:
            if g[:2] in ("L0", "L1"):
                t += sum(float(q) * float(r) for d, q, u, r, s in lines)
    return t

V3_TRADE = trade()
V3_FFE   = 5_588_260.0
V3_SOFT  = total(D3, ("700",))
V3_ESC   = V3_TRADE * 0.10
V3_GC    = V3_TRADE * 0.085
V3_OHP   = V3_TRADE * 0.09
V3_CONSTR= V3_TRADE + V3_ESC + V3_GC + V3_OHP
V3_CONT  = 5_000_000.0
V3_TOTAL = V3_CONSTR + V3_CONT + V3_FFE + V3_SOFT

V2_TRADE, V2_TOTAL = 38_166_123.0, 64_648_067.0
