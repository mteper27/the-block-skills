# -*- coding: utf-8 -*-
"""Reconciliation of every line in Thomas's Master Development Budget against this model.

STATUS meanings
  GC   General-conditions content. Thomas carries it as a trade line AND we apply an 11%
       general conditions markup on top of trade cost. That is the same site cost twice.
       Governed by the master toggle at the top of the sheet: percentage OR line items, never both.
  IN   Already carried in this model, priced independently. Toggle defaults OFF so it is not
       added twice. Turn it ON only if you want HIS price instead of ours.
  ADD  Real scope that is NOT in this model. Toggle defaults OFF so the headline number stays
       honest about what it covers. Turn ON to buy it.
  OUT  Deliberately excluded by a decision already taken. Reason given.
"""
from thomas_raw import RAW

DIV = {
 '013000': ('GC',  'GENERAL CONDITIONS CONTENT — see the master toggle above'),
 '015800': ('GC',  'GENERAL CONDITIONS CONTENT — see the master toggle above'),
 '024100': ('IN',  'Div 000 — Demolition, interior'),
 '033000': ('IN',  'Div 200/300 foundations + Div 000 sitework'),
 '042000': ('IN',  'Div 400 — Masonry'),
 '044200': ('IN',  'Div 400 — Finishes'),
 '055100': ('IN',  'Div 100/200/300 — structural steel'),
 '062000': ('IN',  'Div 400 — Rough carpentry & protection'),
 '064000': ('IN',  'Div 400 — Millwork'),
 '075000': ('IN',  'Div 100 — Roof reinstatement'),
 '078100': ('IN',  'Div 100/300 — Fireproofing'),
 '081000': ('IN',  'Div 400 — Doors, frames & hardware'),
 '083000': ('IN',  'Div 400 — Doors, frames & hardware'),
 '084100': ('IN',  'Div 400 — Storefront & glazing'),
 '088000': ('IN',  'Div 400 — Storefront & glazing'),
 '092000': ('IN',  'Div 400 — Drywall & partitions'),
 '092300': ('IN',  'Div 400 — Finishes'),
 '096000': ('IN',  'Div 400 — Finishes'),
 '096050': ('IN',  'Div 400 — Finishes'),
 '096400': ('IN',  'Div 200 — Stage T&G wood floor'),
 '099000': ('IN',  'Div 400 — Finishes'),
 '100000': ('IN',  'Div 400 — Specialties'),
 '100500': ('IN',  'Div 400 — Acoustic treatment'),
 '101400': ('IN',  'Div 400 — Signage & wayfinding'),
 '114000': ('OUT', 'KITCHEN OUTSOURCED. Your decision: bring in an operator to run F&B rather than build a kitchen. Hood, hood fire suppression and food service equipment all come with them.'),
 '142000': ('IN',  'Div 500 — Conveying'),
 '210000': ('IN',  'Div 500 — Fire protection'),
 '220000': ('IN',  'Div 500 — Plumbing'),
 '230000': ('IN',  'Div 500 — HVAC'),
 '260000': ('IN',  'Div 500 — Electrical'),
 '270000': ('IN',  'Div 500 — Low voltage / Div 600 production lighting'),
 '283100': ('IN',  'Div 500 — Fire alarm & detection'),
}

# (csi, item_no, description-prefix) -> (status, on_by_default, note)
OVR = {
 ('013000',4,'Field'): ('GC',0,'$200,000 of "field technology" is a general conditions item and a big one. Ask what it actually buys — Procore licences and a few tablets are not $200,000.'),
 ('013000',11,'Project'): ('GC',0,'$900,000 of "project labor" is the single largest general conditions line. This is GC labour on site. It is exactly what the 11% markup is for. Do not pay both.'),
 ('013000',7,'Site Safety'): ('GC',0,'$250,000. NYC site safety is real and required, but it belongs in general conditions, not on top of a general conditions percentage.'),
 ('015800',1,'Install sidewalk'): ('IN',0,'Div 000 — we price the shed at $210/LF over 1,089 LF plus 24 months of rental, which is a build-up rather than his $250,000 lump. Ours is the more defensible number.'),

 ('055100',5,'Steel Framing at upper balcony'): ('ADD',0,'UPPER BALCONY IS A THIRD LEVEL AND IS NOT IN THIS MODEL. We carry stage + one mezzanine. If the test fit keeps a balcony above the mezzanine it is new steel, new egress, new sprinkler and new seating. Priced at 0 by Thomas so its real cost is unknown. DECISION NEEDED.'),
 ('055100',6,'Stage Lighting & AV'): ('IN',0,'THE RIGGING GRID. His rate is $8/LB with qty 0, so he never priced it. Our ground-supported grid is $1,363,450 for roughly 74 tons — that is $9.21/LB, within 15% of his own rate. His rate corroborates ours.'),
 ('055100',12,'Railing at Roof Deck'): ('ADD',0,'Roof deck is outdoor terrace programme, not in this model.'),
 ('075000',1,'2nd Floor Terrace'): ('ADD',0,'OUTDOOR TERRACE. 2,041 SF of second-floor roof deck. Programme scope — it is not needed to open the room and it is not in this model. His price, $66,333.'),
 ('075000',2,'2nd Floor concrete pavers'): ('ADD',0,'OUTDOOR TERRACE paving on pedestals, 2,041 SF. Pairs with the line above. Note this is the line whose unit price is broken on his summary sheet — $31/SF here, but the summary carries $5,224,148 against it. The detail is right and the summary is wrong.'),
 ('084100',2,'F&I New Storefront with doors to roof'): ('ADD',0,'Serves the roof terrace. Follows that decision.'),
 ('084100',3,'Storefront double door to roof'): ('ADD',0,'Serves the roof terrace. Follows that decision.'),

 ('100000',2,'Toilet Acc'): ('IN',0,'Watch the basis. $7,500 per SET reads as a per-restroom allowance, not per fixture. At 30 sets that is $225,000; roughly 10 restroom groups is the right count and we carry it that way.'),
 ('210000',1,'First Floor Rework'): ('IN',0,'HIS BASIS IS 69,000 SF at $7. Sprinkler coverage in this model is 88,100 SF — the floor plus the mezzanine, because the mezzanine needs heads above and below. His 69,000 SF understates it.'),
 ('230000',1,'HVAC System'): ('IN',0,'HIS BASIS IS 120,000 SF at $40 = $4,800,000, against a 74,100 SF building. Area is the wrong driver anyway — an assembly room is sized on occupant load and latent heat, not floor area. THE OPEN QUESTION FOR THE MECHANICAL ENGINEER: was this priced on a load calculation or on a rate per SF? $1.1M+ turns on the answer.'),
 ('230000',2,'BMS'): ('IN',0,'$500,000 for building management on a single-tenant venue with a handful of air handlers is a commercial-office number. Ours is lower.'),
 ('260000',16,'Provide temp. lighting'): ('IN',0,'HIS BASIS IS 125,000 SF at $1.25. The building is 74,100 SF.'),
 ('283100',1,'F&I Fire alarm'): ('IN',0,'HIS BASIS IS 100,000 SF at $2.50. Alarm coverage in this model is 88,100 SF — floor plus mezzanine.'),
 ('142000',3,'Hydraulic Lift'): ('ADD',0,'Priced at nothing. A 12x6 stage lift is real money — budget $85,000-140,000 installed if the production team wants it.'),
 ('220000',15,'F&I Kitchen roughing'): ('OUT',0,'KITCHEN OUTSOURCED. Rough-in follows the operator, and most operators bring their own fit-out.'),
 ('220000',18,'Gas Piping to Equipment'): ('OUT',0,'KITCHEN OUTSOURCED. Revisit only if the operator needs gas.'),
 ('092000',9,'FRP Kitchen walls'): ('OUT',0,'KITCHEN OUTSOURCED.'),
 ('092300',5,'Tile & Base at Kitchen'): ('OUT',0,'KITCHEN OUTSOURCED.'),
 ('260000',8,'F/I dedicated circuits at all Kitchen'): ('OUT',0,'KITCHEN OUTSOURCED.'),
}

def classify(csi,no,desc):
    for (c,n,pref),v in OVR.items():
        if c==csi and n==no and desc.startswith(pref): return v
    st,where = DIV.get(csi,('IN','Not mapped — REVIEW'))
    return (st,0,where)

LINES=[]
for csi,dname,no,desc,qty,unit,rate,tot,note in RAW:
    st,on,where = classify(csi,no,desc)
    LINES.append(dict(csi=csi,dname=dname,no=no,desc=desc,qty=qty,unit=unit,rate=rate,
                      tot=tot,his_note=note,status=st,on=on,where=where))

GC_LINES=[l for l in LINES if l['status']=='GC']
GC_TOTAL=sum(l['tot'] for l in GC_LINES)
