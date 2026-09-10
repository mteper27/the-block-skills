---
name: venue-unit-costs
description: Price a venue or stage build by the unit rather than the lump — take the quantities off the test fit, apply measured rates from what was actually paid on previous builds, and cross-check before sending. Covers crash barricade per foot with corners and freight, lighting per fixture with install as a ratio, containers and bars each, fence and feature wall per panel, decking, footings, structural and permitting soft costs. Carries an evidence hierarchy so a quote always beats a derived rate, scaling laws for extrapolating a lump to a different size, and the adjustments that must be made before any rate moves between projects. Use when reviewing a contractor's lump sum, building a bottom-up estimate from drawings, pricing a stage, or sanity-checking any line that should have a quantity behind it.
---

# Venue Unit Costs

A lump sum cannot be argued with. A unit rate times a quantity can. The point of this skill is to turn *"crowd control: $80,000"* into *"200 ft of black crash barricade at $200.76/ft = $40,151, plus 13.4% freight, plus corners — and we have measured all three."*

`data/factory-town-unit-costs.csv` holds the rate library mined from the Factory Town CAPEX file: 68 lines, most of them paid actuals with the vendor named.

## The evidence hierarchy — read this before using any rate

1. **A quote for this scope.** A fabricator's or trade's price for the thing in front of you.
2. **A delivered unit rate with a real count behind it** — this fixture, this foot, this container.
3. **A ratio** riding a number you already trust.
4. **A capacity or area band**, only when there are no dimensions at all.

**Never use a lower tier when a higher one exists.** The moment you have dimensions — and certainly the moment you have a quote — a band is not a candidate, it is a *check*, and a weak one.

This rule is here because it was broken. Pricing a 60' × 40' black steel stage, a capacity band returned **$2,369,220** against a fabricator quote of **$1,000,000** — 2.37x — and dragged engineering, design and foundations up with it, because all three ride the structure. **A quote existed and a proxy was used anyway.** That is the most expensive mistake available in this process.

## Record confidence, and never mix the levels silently

The CSV carries a `confidence` column for a reason:

- **actual** — invoiced and paid. The only rates worth arguing from.
- **forecast** — the owner's current view, not yet spent.
- **quote** — a vendor's number, not yet committed.
- **budget** — an approved allowance. Frequently wrong in both directions.
- **disputed** — invoiced and contested. Do not use.

On the Factory Town file the gap between budget and actual was routinely large: bike racks +69%, security screening +49%, entry façade and signage +204%, column underpinning +58%. **Budget lines are not rates.**

Worse than a wrong budget is a line approved at **zero** that was never optional. County and city impact fees were approved at $0 and came in at **$843,740**; a liquor licence approved at $0 forecast at $250,000. A zero is not a saving — it is scope nobody priced. Hunt them first.

The architect line shows the third trap: against a $250,000 approval, one sheet reports $132,500 committed and a later sheet forecasts **$981,740**. Same budget line, two views, an overrun still in flight. **Price the architect from a fee proposal for your own scope, not from anyone's ratio.**

## Take these quantities off the test fit

Nothing gets priced without one. If the drawing cannot produce a quantity, the line is an allowance and gets labelled one.

- **Stage deck** — width × depth → SF; trim height; clear height to underside of roof.
- **Roof** — covered area, and the question that changes everything: **does it cover the stage only, or the audience too?**
- **Rigging** — hung or ground-supported.
- **Foundations** — footing count, depth and locations if drawn. The widest number on the sheet.
- **Barricade** — LF of stage front, pit returns, gates. **Count corners separately.**
- **LED** — each wall's width × height → SF; ground-stacked or flown.
- **Lighting** — fixture count by type off the lighting plan.
- **Fence and walls** — LF by finish level.
- **Containers and bars** — count by size and fit-out.
- **Bathrooms** — fixture count from the code calculation, not from the plan's convenience.
- **Capacity** — from the egress and occupancy calculation. For cross-checking only.
- **Access** — crane position, hoisting route, and whether the work goes up in the open or inside an existing building. Scope, not a rate, and where transferred numbers break.

## Ratios, and where they stop working

| Ratio | Value | Rides on |
| --- | ---: | --- |
| Foundations and footings | **10 – 24%** | the whole delivered structure package |
| Erection labour + crane | ~5% | structure |
| Barricade corners | **19%** | barricade package |
| Barricade freight | **13.4%** | barricade equipment |
| Lighting install, single room | **16.7%** | fixture purchase |
| Lighting install, distributed across a site | **54%** (67% with electrical) | fixture purchase |

**Foundations are a range, and the driver is the design wind case.** The high end is a mass foundation resisting overturning and uplift on an open-air stage at Miami-Dade design wind; the low end is a different structure and a different wind case. Applied to a $1M steel-only quote, that is **$113K to $309K**. An interior structure carries no wind load at all, so the hurricane end is not a conservative choice indoors — it is the wrong load case.

**Percentages have absolute floors.** Structural engineering delivered at $22,060 and $31,920 per stage. Applying 1.5% to a $1M stage returns $15,000, below both fees actually paid. Below roughly $2M of structure, carry engineering ($22–32K per stage), plan review and inspections ($13,500 per stage), and expediting ($1,500 per permit) as **absolute amounts**.

## Watch the fit-out the headline rate hides

Container bars are the clearest case. The container is $16,875 for a 20 ft unit, but the openings cut into it, the roll-up door, plumbing roughing, power and the bar equipment are all separate lines. A "container bar" priced at the container is priced at perhaps a third of what it costs to serve a drink from.

The same trap applies to decking (fabrication, heavy equipment, crane and labour are four vendors), to stage structure (structure, video support, FOH platform, towers, footings, labour, crane), and to LED — **the steel that holds a wall up is priced by the stage fabricator, not the LED vendor.**

**And a quote for one item is not a rate for the next.** Bar #22 was estimated at $24,000 off Bar #61's quote and landed at $28,250 — 17.7% over.

## Extrapolating a lump to a different size

Most useful benchmark lines are lumps with no area behind them, and the room you are pricing is a different size. This is where the biggest errors get made.

**First, get the source dimension.** A lump without a dimension cannot be extrapolated — only used as a whole-item comparable for a similar-sized item. Chase it from the drawing, the fabrication quote or the vendor. If it cannot be found, say so and price the line another way rather than inventing a denominator.

**Then choose the right scaling law.** Cost rarely scales linearly with area:

- **Flat area work** — decking, platforms, membrane, flooring, paint — scales close to **linearly with area**.
- **Structure carrying load over a span** scales **faster than area**, because member depth grows with span. Doubling a span more than doubles the steel.
- **Perimeter items** — railing, edge detail, barricade, facade — scale with **perimeter, not area**. Doubling an area multiplies perimeter by about 1.4, so an area scale overstates them badly.
- **Fixed costs inside the lump** — mobilisation, engineering, shop drawings, crane, delivery — do **not scale at all**. Strip them out first, then add them back once.

So the honest form is `cost = fixed + (area rate × area) + (perimeter rate × perimeter)`, never `old cost × (new area / old area)`.

**Never price a stage by deck SF at all.** A stage is priced by span, height and load; the deck is the cheap part. The one deck rate in the library ($66/SF) is a small aux stage and does not scale to a roofed mainstage.

**State the confidence loss.** An extrapolated rate is weaker evidence than the actual it came from. Label it derived, and name the source line, the source dimension and the scaling law used.

## Adjust before you apply

Every adjustment is a named line, never a blended factor.

**Environmental design case.** Never move a foundation or structure rate between wind regions without restating it.

**Indoor versus outdoor — strip the scope before comparing the rate.** An open-air stage buys a roof and crowd weather protection that an enclosed room already has, and hurricane foundations an interior structure does not need. Take both out of an outdoor comparable before applying it indoors, or the transfer imports scope your project does not have.

**Labour market and prevailing wage.** Equipment and materials travel between markets; installation labour does not. Where a line splits into equipment and labour, escalate them separately — the source file breaks several lines out exactly this way.

**Access changes shape entirely.** A structure built in the open with a crane on the slab is a different scope from the same structure lifted into an existing building. No rate card covers that difference.

**Ground-supported still beats hung**, everywhere. A stage standing on its own footings takes the rigging load out of the building, which is what lets roof steel stay light.

## The calculation, in order

1. **Classify** — indoor or outdoor, roof over stage or crowd, ground-supported or hung.
2. **Get the structure priced by someone who builds them.** If a quote exists it is the number, and the job becomes leveling it: what is in, what is out, deck, roof, towers, erection, freight, engineering, and to what code.
3. **Foundations separately, as a range.** Fabricator quotes routinely exclude them.
4. **Erection and crane** — confirm in or out before adding.
5. **Production packages by count**, then install as a ratio of purchase.
6. **Site and guest infrastructure by measurement** — barricade LF plus corners plus freight, fence LF, containers each.
7. **Soft costs as absolutes** at this scale.
8. **Name what is excluded, and hunt the lines at zero** — sound, power, SFX, HVAC, utilities, impact fees, licensing.
9. **State the estimate class and band.** A test fit is Class 4 or 5 — roughly −15/−30% to +20/+50% at best. Never carry it to the dollar.

## Cross-check before you send

- **Against a quote**, if one exists anywhere in the market. Any derived number more than ~25% off a real quote is wrong until proven otherwise, and the quote is not what has to prove itself.
- **Against the contractor's lump.** A takeoff landing within ~15% validates it. A takeoff at half the lump is a conversation.
- **Per unit that travels** — per LF, per fixture, per seat, per capacity unit. Outside the expected range is either a specification decision worth naming or an error.
- **Direction of every variance** — overstated, understated, or a discrepancy between sources. Opposite actions.

## Worked example

A 60' × 40' black steel stage, ground-supported, outdoor; 180 LF of barricade; one 24' × 14' LED wall; 60 effects fixtures; four 20' bar containers; 300 LF of temporary fence. **A fabricator quote of $1,000,000 is in hand covering deck, roof, towers and erection. Footings excluded.**

| Line | Amount | Evidence |
| --- | ---: | --- |
| Black steel stage — deck, roof, towers, erection | 1,000,000 | **quoted** |
| Foundations & footings | 150,000 | ratio, range $113–309K |
| Anchor bolts, embeds, survey, setting template | 15,000 | allowance — interface gap |
| Structural engineering / PE stamp | 25,000 | absolute |
| Plan review + inspections | 13,500 | flat per stage |
| Stage / production design | 50,000 | allowance |
| Effects fixtures (60 @ $2,471) | 148,270 | counted |
| — install @ 16.7% | 24,761 | ratio |
| LED wall, 336 SF | 150,000 | **allowance — quote it** |
| Crash barricade, 180 LF @ $227.64 | 40,975 | counted |
| — corners @ 19% | 7,785 | ratio |
| 20' bar containers (4 @ $16,875) | 67,500 | counted |
| Temporary fence, 300 LF @ $22.79 | 6,837 | counted |
| **Total — excludes sound, power, SFX** | **1,699,628** | |

**The quote is 59% of the delivered cost.** The other $699,628 is everything a fabricator does not sell you — the most useful single number here, because it is what an owner reading a stage quote gets wrong.

Three leveling moves worth copying. **Erection was inside the quote**, so a separate erection allowance comes out — carrying both is a ~$68K double-count. **Footings were excluded**, so they are their own line, taken at the low end of the range because this roof covers the stage rather than the crowd. And **footings excluded plus erection included creates an interface**: the fabricator erects on a foundation someone else poured, so anchor bolts, embeds, the setting template and the survey belong to nobody until the contract says otherwise. That gap is where the change order comes from — the one delivered footing contract in the library took **34%**.

Still unpriced and worth asking before this is trusted: freight to site, shop drawings, the wind and live load basis and code edition, guardrail and stair compliance, ADA access to the deck, sales tax.

## Building the library

Every project should add to it. Mine invoice trackers rather than budget summaries — the vendor, the paid amount and the description together are what make a rate reusable. Record the quantity even when the file does not compute a rate, because a later takeoff can. Keep the source and the date on every row; rates age, and an undated rate is a guess with a decimal point.

## Never

Never use a band when dimensions or a quote exist, and never let a derived number stand against a real quote without explaining the gap. Never apply a budget line as a unit rate. Never move a foundation or structure rate across wind regions, or from open-air to enclosed, without restating the design case. Never apply a percentage below the absolute fee the work actually costs. Never price a container, a deck or a stage at its headline line — find the sibling lines. Never price a stage by deck square footage. Never take a barricade per-foot quote as the package price. Never take an LED quote without the steel that holds it. Never let sound, power, licensing or impact fees sit at zero without saying so on the face of the estimate. Never present a takeoff without the quantity source named.
