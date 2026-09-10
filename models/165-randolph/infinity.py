# -*- coding: utf-8 -*-
# Which lines survive an INFINITY-ROOM build: a big volume, ground-supported stage
# and towers, mezzanine for capacity, bars, bathrooms, life safety, exposed finish.
# 'N' = theatre / hospitality overlay this contractor has layered on top.
NOT_INFINITY = {
 'Roofing — 3 terrace membranes':'Roof decks are not part of an Infinity room.',
 'Roofing — 3 terrace paver decks (CORRECTED)':'Roof decks are not part of an Infinity room.',
 'Storefront — roof deck & VIP lounge':'Serves the roof decks and VIP lounge — both out.',
 'Carpet / resilient flooring — BOH, offices, dressing':'Sealed concrete throughout except dressing rooms.',
 'Furniture — VIP lounge & VIP roof terrace':'No VIP lounge in an Infinity room; VIP is a rail and tables on the floor.',
 'Furniture — restaurant & restaurant terrace':'No restaurant.',
 'Furniture — roof terrace & roof lounge':'No roof programme.',
 'Kitchen equipment':'No kitchen — outsource or omit entirely.',
 'Plumbing — kitchen roughing, gas piping to kitchen':'Follows the kitchen out.',
 'Architectural & exterior lighting':'A $1.75M architectural lighting package is the opposite of this concept.',
 'Interior art, decor, scenic & exterior murals':'Exposed structure IS the aesthetic. MT I55/I209 already deferred it.',
 'Production — displays & distribution':'MT I294 — rent it.',
 'Production — VIP lounge projector':'No VIP lounge.',
 'Seating — mezz elevated chairs, couches, coffee tables':'Reduce to rail and a handful of tables.',
 'Parking garage — 260 spaces':'Off-site, and probably not our scope at all (MT I21).',
 'Escalation on off-site @5%':'Follows the garage out.',
}
# Lines that stay but shrink under an Infinity concept (description -> reduced $)
INFINITY_REDUCED = {
 # Theatre seating STAYS in every scenario — it is what makes the room a theater
 # for use-classification purposes, which is what carries the liquor and cabaret
 # licences. It is a licensing dependency, not a furniture choice.

 'Elevators — 2 cars x 4 stops': (600_000, 300_000,
   'Two levels not four: one ADA car, two stops, plus a small BOH lift. Still code-required.'),
 'Tile — restrooms, bars, kitchen': (250_000, 140_000,
   'Restrooms only. Sealed concrete at bars and BOH.'),
 'Millwork — box office, coat, merch, BOH counters': (200_000, 110_000,
   'Box office and merch only. No coat check millwork, no decorative back-bar features.'),
 'Millwork — 9 bars & back bars': (600_000, 420_000,
   'Six bars rather than nine — the VIP, restaurant and roof-lobby bars go with their rooms.'),
 'Bar equipment — 9 bars, 76 POS positions': (684_000, 480_000,
   'Six bars, ~53 POS positions.'),
 "Bar equipment — uplift to Brooklyn Paramount's realised rate": (990_000, 694_000,
   'Same $32,192/POS benchmark applied to the reduced position count.'),
 'Plumbing — bar roughing, 9 bars': (400_000, 265_000,
   'Six bars.'),
 'Exterior building signage': (400_000, 150_000,
   'Identification and wayfinding, not a facade programme.'),
 'Painting & plaster': (320_000, 200_000,
   'Exposed painted structure. No plaster, no upgraded finishes.'),
 'Production — soft goods / drape': (400_000, 300_000,
   'Stage and perimeter drape only.'),
 'Seating — mezzanine box chairs (657)': (197_100, 120_000,
   'Fewer boxes, rail standing behind.'),
}
