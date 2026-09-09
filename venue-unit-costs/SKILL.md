---
name: venue-unit-costs
description: Price a venue build by the unit rather than the lump — crash barricade per foot, bike racks each, container bars each, security lanes, LED, decking, footings, bathroom fixtures — using rates mined from what we actually paid on previous builds. Takes a test fit or plan, counts the quantities off it, and applies measured rates so a budget line can be checked against a takeoff instead of an allowance. Use when reviewing a contractor's lump sum, building a bottom-up estimate from drawings, or sanity-checking any line that should have a quantity behind it.
---

# Venue Unit Costs

A lump sum cannot be argued with. A unit rate times a quantity can. The point of this skill is to turn *"crowd control: $80,000"* into *"200 ft of black crash barricade at $200.76/ft = $40,151, and we have measured that"* — which is checkable, defensible, and scales to the next room.

`data/factory-town-unit-costs.csv` holds rates mined from the Factory Town CAPEX file: 48 lines, 37 of them paid actuals with the vendor named.

## The method

1. **Take the quantity off the drawing, not off a feeling.** Linear feet of barricade along the front-of-house line and the rails. Number of bar positions. Number of screening lanes at the entry. Square feet of decking. Number of footings. Fixture count from the code calculation. If the plan cannot produce a quantity, the line is an allowance and should be labelled one.
2. **Apply a measured rate.** Prefer an actual we paid over a quote, a quote over a budget, and any of those over a published index.
3. **Adjust for what is different about this project**, explicitly and in writing — see below. This is where naive benchmarking goes wrong.
4. **Compare to the contractor's lump.** A takeoff that lands within ~15% of a lump sum validates it. A takeoff at half the lump is a conversation.

## Always record confidence, and never mix the levels silently

The CSV carries a `confidence` column for a reason:

- **actual** — invoiced and paid. The only rates worth arguing from.
- **forecast** — the owner's current view, not yet spent.
- **quote** — a vendor's number, not yet committed.
- **budget** — an approved allowance. Frequently wrong in both directions.
- **disputed** — invoiced and contested. Do not use.

On the Factory Town file the gap between budget and actual was routinely large: bike racks +69%, security screening +49%, entry façade and signage +204%, column underpinning +58%, architect +293%. **Budget lines are not rates.** Two lines were approved at zero and came in at real money — the liquor licence at $250,000 and impact fees at $843,740.

## Adjust before you apply — the three that matter most

**Environmental design case.** Factory Town's Infinity footings cost $826,996 because they are mass foundations resisting overturning and uplift on an open-air stage at Miami-Dade design wind. Park's footings, a different structure and wind case, were $60,000 of concrete plus $111,400 of rebar. An interior structure in a northern city carries no wind load at all. Never move a foundation rate between wind regions without restating the design case.

**Indoor versus outdoor.** An open-air stage buys a roof and weather protection that an enclosed room already has. Strip that scope before comparing structure rates.

**Labour market and prevailing wage.** A Florida rate is not a New York rate. Equipment and materials travel between markets; installation labour does not. Where a line splits into equipment and labour, escalate them separately — the Factory Town file breaks several lines out exactly this way.

## Watch the fit-out that the headline rate hides

Container bars are the clearest case. The container itself is $16,875 for a 20 ft warehouse unit, but the openings cut into it, the roll-up door, plumbing roughing, power and the bar equipment are all separate lines. A "container bar" priced at the container is priced at perhaps a third of what it costs to serve a drink from. The same trap applies to decking (fabrication, heavy equipment, crane and labour are four vendors), and to stage structure (structure, video support, FOH platform, towers, footings, labour, crane).

## Building the library

Every project should add to it. Mine invoice trackers rather than budget summaries — the vendor, the paid amount and the description together are what make a rate reusable. Record the quantity even when the file does not compute a rate, because a later takeoff can. Keep the source and the date on every row; rates age, and an undated rate is a guess with a decimal point.

## Never

Never apply a budget line as a unit rate. Never move a foundation or structure rate across wind regions or between indoor and outdoor without restating the design case. Never price a container, a deck or a stage at its headline line — find the sibling lines. Never present a takeoff without the quantity source named.
