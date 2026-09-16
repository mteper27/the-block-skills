---
name: construction-budget-audit
description: Forensic audit of a construction or development budget before it is trusted — unit-price outliers, trades priced at zero quantity, contingency stacking, blank escalation, markup cascades, area-basis mismatches and broken rollups. Reconciles every line back to the source workbook to the dollar so the audit is provably complete. Use whenever a GC estimate, master development budget, schedule of values or contractor proposal has to be checked before it goes to an investment committee, a lender or a buyout — and any time a budget total looks plausible and you need to know whether it is.
---

# Construction Budget Audit

A budget total can be right for the wrong reasons. The 165 Randolph master development budget footed to $42.56M against a $45M underwriting case, and that agreement was a coincidence: one cell overstated it by $5.2M while two-thirds of the trade schedule was priced at zero quantity. The errors pointed opposite ways and nearly cancelled. **A plausible total is not evidence of a complete estimate.**

## The audit, in order

**1. Reconcile before you analyse.** Decompose the budget into your own line schedule and prove each section ties to the source to the dollar — trade, off-site, soft costs, FF&E. Print the variance. If it is not zero you are auditing your own transcription, not their budget. This reconciliation belongs in the deliverable, because it is what lets a reader trust every later number.

**2. Hunt zero quantities.** The most expensive thing in an early estimate is scope that carries a unit price and a quantity of zero — it looks priced and totals nothing. Read every line, not every subtotal. At 165 Randolph: structural steel $0 on a project whose scope line read "Add Second Level"; electrical distribution $0 behind two funded switchboards; acoustical panels $0 in a music venue; LED video walls present only as a "$1,400/SF" note. Sum them and state the range.

**3. Test every unit price against its neighbours.** Sort each trade by $/unit and look at the outliers. Three consecutive paver lines read $31/SF, **$3,312.50/SF**, $31/SF. Same product, same sheet, adjacent rows. A single cell, marked up four times, moved the project total by $6.89M.

**4. Follow the markup cascade.** An error in trade cost does not stay there: it attracts overhead and profit, contractor contingency and owner contingency in sequence. Always report the all-in effect, not the raw cell. Conversely, when scope is missing, add it back through the same cascade.

**5. Check what escalation was applied to.** A blank escalation line is easy to miss because the line exists. At 165 Randolph the off-site parking garage got 5% and the $18.2M building got nothing.

**6. Un-stack the contingency.** Owner contingency calculated on a subtotal that already contains contractor contingency is contingency on contingency. Separately, judge the *level*: 10-14% is normal for a documented design and far too thin for a pre-design conversion with unpriced scope. Contingency held against scope that was never priced is not contingency.

**7. Reconcile the area basis.** Footprint, gross floor area across levels, and rentable area are three different numbers and trades follow different ones. Roofing, envelope and HVAC *volume* follow footprint; sprinklers, alarm, partitions and flooring follow stacked floor area. A budget reporting $313/SF on all-floor area and an underwriting reporting $607/SF on footprint describe the same building — and a reader comparing either to market comps is being misled.

**8. Read the hidden tabs.** Cost-control templates get copied between projects. Look for `#REF!` rollups, a cost-report date from a previous job, an empty risk register, and zero committed costs. Zero commitments means nothing has been bought and the total is a desktop estimate, not a validated bottom-up — say so plainly.

**9. Find the internal comps.** Estimators leave benchmarks in the notes column. A note reading `* BPT: 26 POS / Prep Kitchen / 1 Walk-in Cooler $837K` is a prior build by the same owner: $32,192 per POS against $19,171 budgeted here. That is a 40% variance against their own delivered project — worth more than any published cost index.

## Reporting

Report direction, not just size: **overstated** (priced too high), **understated** (too low or missing), **discrepancy** (sources disagree). Never collapse them into one "variance" figure — an owner needs to know whether to negotiate the price down or fund scope back in, and those are opposite actions.

Every finding cites a cell, a quantity or a unit price, quoted verbatim. Where you estimate missing scope, price it at **the estimator's own unit rates** wherever the file supplies them — that removes the argument about whose rates are right and makes the finding very hard to dismiss. Where the file gives no rate, say which external basis you used.

Distinguish an **estimate-quality** problem from a **programme** problem. A contractor who priced four levels, roof decks and a restaurant because the test fit showed them has not over-scoped anything — the scope question belongs upstream with the architect and the owner. A contractor who left escalation blank and priced abatement at $8,750 on a 1948 building has made estimating errors. Those are different conversations with different people, and conflating them wastes the owner's credibility.

## Never

Never treat a matching total as validation. Never report a raw cell error without its markup cascade. Never call scope "missing" without first checking whether it sits in another cost code. Never assume the larger of two area figures is the right denominator. Never accuse a contractor of padding when the scope came from the drawings they were given.

## Two things the second pass at 165 Randolph taught

**Read the contingency line's formula, not its label.** The 16 Sep revision carried a line reading `Soft Costs & FFE Contingency 10%` whose formula was `=(D23+D31+D47+D65)*0.1` — ten percent of the *entire project*, including a construction subtotal that already held its own 10% contractor contingency. As labelled it should have been $1,507,723; it was $8,098,599. A label and a formula disagreeing is worth more than any benchmark, and it will never show up in a subtotal check.

**The convergence test is the finding.** Correct only the estimator's own arithmetic and basis errors — his rates, his quantities, his own backup rows — then re-run *his* formula chain rather than applying markups by hand. If his corrected total lands near an independently built bottom-up budget, the disagreement was never about how hard the building is to build, and you can say so. At 165 Randolph a $24.4M gap closed to 1.9% this way. That reframes the conversation from "you are too expensive" to "four cells are wrong", which is the one version a project manager can act on without losing face.

Applying a hand-computed cascade to each correction instead would have double-counted: several corrections touch lines that also appear in the area-basis finding, and the contingency correction is itself part of the cascade. Fix the source cell, re-run the chain, and the arithmetic cannot lie to you.
