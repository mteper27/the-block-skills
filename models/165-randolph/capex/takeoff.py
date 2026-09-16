# -*- coding: utf-8 -*-
"""Verbatim structural takeoff, 16 Sep 2026.

Source: 260916_165R_Baseline__VE1_Takeoff_Release.xlsx
Origin: DLUBAL RFEM 6.15.0010 export, model '165 Randolph - Bldg SD Rev 38.rf6'
Three model versions are in the file: Rev 43, Rev 43.1 and VE1 (value-engineered).
VE1 IS THE ONE WE PRICE. Rev 43 is carried so the VE saving is visible.

UNITS. The source reports a 't' column in METRIC TONNES (2,204.62 lb).
US structural steel is bought and erected in SHORT TONS (2,000 lb). Everything
below is short tons, converted from the lb column, never from the 't' column.
Using 904.62 (tonnes) where 997.17 (short tons) belongs understates the steel
by 10.2%.
"""
LB_PER_TON = 2000.0

# --- headline, VE1 vs Rev 43, straight off the 'Takeoff' sheet (lb) ---
VE_SAVING = [
 ("Beams / girders",        1_130_205.08, 1_016_730.12),
 ("Columns / extensions",   1_100_161.51,   721_235.36),
 ("Truss components",         166_783.23,   135_424.31),
 ("Braces",                   131_056.08,    80_323.25),
 ("CFS — BOH & closure framing",  0.00,    40_621.96),
]
REV43_TOTAL_LB = 2_528_205.89
VE1_TOTAL_LB   = 1_994_335.00

# --- VE1 member detail, aggregated by system and section type (8,658 rows) ---
# (system, section type, member count, LF, lb)
MEMBERS = [
 ("Beams/girders",      "Rolled W-shape",        992, 17_441.0, 1_003_473.0),
 ("Beams/girders",      "HSS tube",              104,    338.0,    13_258.0),
 ("Columns/extensions", "Built-up plate girder",  80,  1_320.0,   403_988.0),
 ("Columns/extensions", "Rolled W-shape",        148,  3_107.0,   307_818.0),
 ("Columns/extensions", "HSS tube",               15,    197.0,     9_430.0),
 ("Truss components",   "Rolled W-shape",        517,  5_187.0,   135_424.0),
 ("Braces",             "HSS tube",              281,  4_781.0,    52_722.0),
 ("Braces",             "Rolled W-shape",         21,    610.0,    27_601.0),
 ("Cold-formed steel",  "CFS stud / track / strap", 2686, 11_557.0, 40_622.0),
]

# --- areas, counts and masonry, VE1 column of the 'Takeoff' sheet ---
AREAS = [
 ("Mezzanine / floor (+20 ft)",            "SF", 29_062.39, 32_942.0),
 ("Additional tiered seating coverage",    "SF",       0.0, 13_077.0),
 ("Terrace / maintenance roof (+45 ft 7)", "SF", 29_059.08, 26_389.0),
 ("Lower roof (+60 ft 6)",                 "SF",  8_055.42,  5_706.0),
 ("High roof (+64 ft 6)",                  "SF", 27_392.99, 27_393.0),
 ("W01 / W02 roof caps",                   "SF",  1_441.28,  1_457.0),
 ("W03 / W09 roof caps (+60 ft 6)",        "SF",    363.06,    350.0),
 ("BOH CFS roof (+33 ft 6)",               "SF",       0.0,  4_230.0),
 ("Total new CMU",                         "SF", 23_329.93, 39_248.0),
 ("Footing allowance",              "locations",      81.0,    124.0),
]
def area(name):
    for n, u, r43, ve1 in AREAS:
        if n.startswith(name): return ve1
    raise KeyError(name)

FOOTINGS   = int(area("Footing allowance"))            # 124
CMU_SF     = area("Total new CMU")                     # 39,248
FLOOR_SF   = area("Mezzanine / floor") + area("Additional tiered")   # 46,019
ROOF_SF    = (area("Terrace / maintenance") + area("Lower roof")
              + area("High roof") + area("W01") + area("W03"))       # 61,295
BOH_ROOF_SF= area("BOH CFS roof")                      # 4,230

# ------------------------------------------------------------------
# WHAT THE MODEL SAYS ABOUT METHOD. Read off the member geometry, not off
# anybody's description of it. Each number below is reproducible from the
# 'Member Detail' sheet.
# ------------------------------------------------------------------
METHOD = [
 ("Where the columns start",
  "243 VE1 column members. 124 of them start at or below +2 ft — 450,114 lb, 225.1 short "
  "tons, 62.4% of all column steel — which is a NEW FULL-HEIGHT COLUMN off the slab. Only "
  "25 members start at ~+20 ft, the existing roof line: 89,113 lb, 44.6 tons, 12.4%. The grid "
  "B and grid E columns are 60.00 LF each, built up from plate as I 48/24, I 64.961/24 and "
  "I 69.023/24 segments."),
 ("The high roof",
  "All 517 truss members are phase NEW and sit between +56.5 ft and +64.5 ft: 135,424 lb of "
  "brand-new roof trusses at a level that does not exist in the building today."),
 ("The existing roof",
  "The level 'Existing Roof / Lower (+20 ft and below)' carries ZERO members in VE1. Nothing "
  "of the existing roof structure is retained in the priced model."),
 ("Replacement vs new",
  "Only 196,105 lb (98.1 short tons, 9.8%) is phase 'Replacement', and all of it is at "
  "'Consolidated floor +20 ft and below' or 'Shared columns and vertical bracing'. None at the "
  "high roof."),
 ("Lifting language",
  "The words lift, jack, shore, temporary, splice and underpin appear NOWHERE in the 8,658 "
  "member rows — not in phase, system, level, section or the overlap-review column."),
 ("Height",
  "High roof is at +64 ft 6 in. Our locked project facts target 50 ft clear."),
]
