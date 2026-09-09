---
name: venue-buildout-underwriting
description: Turn a venue development budget into a decision — the least it can cost to legally open, and what every increment above that buys. Tiers every line by whether it gates the Certificate of Occupancy, gates revenue, or is discretionary; models the shell/height decision separately because it usually dominates; and produces a BASE / ELEVATED / PREMIUM ladder with the step-ups priced. Use for any venue, club, theater or large-format room conversion where someone has to decide what to build now, what to defer, and what to cut — and to sanity-check a development budget against a separate underwriting model.
---

# Venue Build-Out Underwriting

The question an owner actually asks is never "what does this budget total". It is **"what is the least I can spend and still open the doors, and what does everything else cost on top?"** A flat budget cannot answer that. A tiered one can.

## Tier every line

Four tiers, assigned line by line, never by cost code:

- **Tier 0 — Shell & Life Safety.** No Certificate of Occupancy without it. Structure, egress, fire protection and alarm, MEP, ADA, abatement, code compliance.
- **Tier 1 — Revenue Enabling.** Cannot sell a ticket or serve a drink without it. Stage and production structure, bars, audio, acoustic treatment, screening, IT, box office.
- **Tier R — The shell/height decision.** Isolated because it usually dominates every other number and is decided on strategy, not cost.
- **Tier 2 — Positioning.** The venue opens and trades without it. Roof programme, restaurant, VIP, architectural lighting, art, decorative finishes.

Then the ladder is arithmetic: BASE = 0+1, and each step up is a priced increment. Present it as **BASE / ELEVATED / PREMIUM** with the step between each stated in dollars — that is the shape an owner and an IC can both act on.

## Model the height or shell decision on its own sheet

It is a dial, not a switch, and it deserves its own parametric model: footprint, existing height, target height, perimeter, structural rate. Only some scope scales with height — facade and furring do, the roof itself does not, so lifting 10 ft and lifting 30 ft cost the same for most of the package. Showing that lets an owner find the height that actually serves the room instead of defending a round number.

**Ask what the height is buying before pricing it.** At 165 Randolph the answer changed the spec: with a ground-supported stage and mezzanine (Factory Town style), the roof carries no rigging load, so roof steel drops from ~20 lb/SF to ~15 and the heavy transfer girders disappear. Height then buys volume, LED headroom, sightlines and HVAC stratification — real things, but not tonnage. A "50 ft clear height" thesis written for rigging capacity does not survive that change unexamined.

**A quote beats every rate you can derive.** Build the parametric model so it can be replaced: leave explicit cells for the quoted price, what it includes, what it excludes, and its date. Then show build-up vs quote, so the gap between what a specialist charges and what the general estimate carries is visible.

## Split the analysis correctly

**Construction is not operations.** If the project has its own revenue model, do not rebuild it and do not import operating costs. Underwrite the build: construction, production systems, code compliance and licensing. Say explicitly what is excluded.

**Programme scope is not contractor pricing.** Scope that traces to the architect's test fit is a design decision; only pricing errors belong to the contractor. Keep them in separate sections — they are different conversations with different people.

## The cost-down levers, ranked by certainty

Rank every lever as **Certain / High / Medium / Verify**, and never let a Verify item into a board number:

- **Certain** — arithmetic corrections. Unit-price errors, contingency-on-contingency.
- **High** — standard market practice. Competitive bidding a schedule where nothing is committed (5-10%); owner-furnishing major equipment to avoid stacked markup (~20% on that equipment); early buyout of long-lead packages against escalation.
- **Medium** — contract structure. Open-book GMP with shared savings against a fixed overhead-and-profit plus a contingency the contractor keeps.
- **Verify** — conditional. Sales-tax exemptions and utility incentives (real money, must be applied for *before* buyout), and re-use of existing structure or services (which depends on a survey that is often still pending).

Then price the phasing separately: what each deferred item costs to add later, as a multiple. Most finish and equipment carries a ~1.0x later premium — genuinely free to defer. Structure does not. **Build all the structure, defer all the finish and all the kit** is usually the right answer, because steel is cheap while the building is open and ruinous afterwards.

## Deliverable

A live workbook, not a memo. Tier assignments drive scenario totals by formula, so the owner can move a line between tiers and watch the ladder move. Blue input cells, formulas everywhere else, a reconciliation block proving the source ties, and every assumption in a labelled cell rather than buried in a formula.

Report cost per SF on **both** bases (footprint and all floors) and cost per capacity unit — and state which basis each comparable uses before comparing to it.

## Never

Never present a single total. Never let the height or shell decision hide inside a trade total. Never carry an operating assumption into a construction number. Never mark scope as deferrable without checking whether the structure it depends on must go in now.
