# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'.')
from detail import D, SF, MEZZ, PERI, BAND
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
F='Arial'
BLUE=Font(name=F,size=9,color='0000FF'); BLK=Font(name=F,size=9)
BOLD=Font(name=F,size=9,bold=True); H1=Font(name=F,size=18,bold=True,color='1F3864')
H2=Font(name=F,size=11,bold=True,color='1F3864'); WHT=Font(name=F,size=9,bold=True,color='FFFFFF')
SM=Font(name=F,size=8,color='595959'); DIV=Font(name=F,size=11,bold=True,color='FFFFFF')
GRP=Font(name=F,size=9,bold=True,color='1F3864')
HDR=PatternFill('solid',fgColor='1F3864'); DVF=PatternFill('solid',fgColor='2E5C8A')
GPF=PatternFill('solid',fgColor='D9E2F3'); YEL=PatternFill('solid',fgColor='FFFF00')
GRY=PatternFill('solid',fgColor='F2F2F2')
thin=Side(style='thin',color='D0D0D0'); med=Side(style='medium',color='1F3864')
BOX=Border(left=thin,right=thin,top=thin,bottom=thin); TOPB=Border(top=med)
CUR='$#,##0;($#,##0);"-"'; PCT='0.0%'
def wr(): return Alignment(wrap_text=True,vertical='top')
TRGC,TRADD=5,6   # rows of the two summary cells on the Thomas Reconciliation sheet
wb=Workbook(); ws=wb.active; ws.title='Detailed Budget'
for col,w in zip('ABCDEFG',[3,58,10,7,12,14,64]): ws.column_dimensions[col].width=w
r=2
ws.cell(r,2,'165 RANDOLPH STREET').font=H1; r+=1
ws.cell(r,2,'DETAILED DEVELOPMENT BUDGET').font=H2; r+=1
ws.cell(r,2,'Brooklyn NY 11237 · Developer: owner\u2019s team \u00b7 Co-pro: Live Nation / Insomniac \u00b7 Landlord: Eric Cohen \u00b7 CONSTRUCTION CAPEX ONLY \u00b7 CONFIDENTIAL').font=SM; r+=2
for lab,v,note in [('Building SF',SF,'THE basis. Mezzanine adds capacity inside this envelope, not area. Alleys carry no cost.'),
                   ('Theatre seat rate ($/seat)',25,'TOGGLE: 25 = MT sourcing, 125 = as filed in the dev budget. Drives the removable seating line in division 600.'),
                   ('Mezzanine SF',MEZZ,'Inside the 74,100. Derived from the Wake test-fit occupancy loads.'),
                   ('Perimeter LF',PERI,'Approximated as square. Replace with the survey.'),
                   ('New wall band SF',BAND,'1,089 LF perimeter x 30 ft lift.'),
                   ('Capacity',7440,'Wake PD04 Rev 4.4.'),
                   ('General conditions basis',1,'TOGGLE: 1 = the 11% percentage. 0 = Thomas\u2019s own 013000 + 015800 line items ($1,696,000) instead. NEVER BOTH \u2014 they are the same site cost.'),
                   ('Kitchen scope (0 / 1 / 2)',1,'TOGGLE for division 800. 0 = concessions only, no kitchen. 1 = warming / finishing kitchen. 2 = full production kitchen with a grease hood. Each level includes the one below it.')]:
    ws.cell(r,2,lab).font=BLK
    c=ws.cell(r,5,v); c.font=BLUE; c.fill=YEL; c.border=BOX; c.number_format='#,##0'
    ws.cell(r,7,note).font=SM; ws.cell(r,7).alignment=wr(); r+=1
SFR=r-8; SEATR=SFR+1; GCMODE=SFR+6; KITCH=SFR+7; r+=1
for i,h in enumerate(['Item','Qty','Unit','Rate','Amount','Rate source / basis'],2):
    c=ws.cell(r,i,h); c.font=WHT; c.fill=HDR; c.alignment=Alignment(horizontal='center',vertical='center',wrap_text=True)
r+=1
divs=[]
for code,name,groups in D:
    ws.cell(r,2,f'{code}   {name}').font=DIV
    for i in range(2,8): ws.cell(r,i).fill=DVF
    dstart=r+1; r+=1
    gsubs=[]
    for gname,subs in groups:
        ws.cell(r,2,'   '+gname).font=GRP
        for i in range(2,8): ws.cell(r,i).fill=GPF
        gstart=r+1; r+=1
        for desc,qty,unit,rate,src in subs:
            ws.cell(r,2,'      '+desc).font=BLK; ws.cell(r,2).alignment=wr()
            ws.cell(r,3,qty).number_format='#,##0'
            ws.cell(r,4,unit).alignment=Alignment(horizontal='center')
            if rate=='=SEATRATE':
                c=ws.cell(r,5,f'=$E${SEATR}'); c.font=BLK
            else:
                c=ws.cell(r,5,rate); c.font=BLUE
            c.number_format='$#,##0.00'
            c=ws.cell(r,6,f'=C{r}*E{r}'); c.number_format=CUR
            ws.cell(r,7,src).font=SM; ws.cell(r,7).alignment=wr()
            for i in range(2,8): ws.cell(r,i).border=BOX
            r+=1
        ws.cell(r,2,'   '+gname+' — subtotal').font=BOLD
        lvl=int(gname[1]) if code=='800' and gname[:1]=='L' else None
        f_=f'=SUM(F{gstart}:F{r-1})' if lvl is None else f'=IF($E${KITCH}>={lvl},SUM(F{gstart}:F{r-1}),0)'
        c=ws.cell(r,6,f_); c.font=BOLD; c.number_format=CUR
        if lvl is not None:
            ws.cell(r,7,f'Included only when the kitchen scope toggle is {lvl} or higher.').font=SM
        for i in range(2,8): ws.cell(r,i).fill=GRY
        gsubs.append(r); r+=1
    ws.cell(r,2,f'{code} — DIVISION TOTAL').font=Font(name=F,size=10,bold=True,color='1F3864')
    c=ws.cell(r,6,'='+'+'.join(f'F{g}' for g in gsubs))
    c.font=Font(name=F,size=10,bold=True,color='1F3864'); c.number_format=CUR; c.border=TOPB
    for i in (2,3,4,5,7): ws.cell(r,i).border=TOPB
    divs.append((code,r)); r+=2
TR=[x for c,x in divs if c not in ('600','700')]
FFE=[x for c,x in divs if c=='600'][0]; SOFT=[x for c,x in divs if c=='700'][0]
ws.cell(r,2,'TRADE COST — divisions 000-500 plus 800 (kitchen)').font=Font(name=F,size=12,bold=True,color='1F3864')
ws.cell(r,2).border=TOPB
c=ws.cell(r,6,'='+'+'.join(f'F{x}' for x in TR)); c.font=Font(name=F,size=12,bold=True,color='1F3864')
c.number_format=CUR; c.border=TOPB
for i in (3,4,5,7): ws.cell(r,i).border=TOPB
TRADE=r; r+=1
ws.cell(r,4,'Everything above this line is WORK. Everything below it is markup, reserve, equipment and fees.').font=SM
r+=2

ws.cell(r,2,'BELOW THE LINE — separate costs').font=H2; r+=1
ws.cell(r,4,'Each rate below is applied to TRADE COST only. They do not compound on each other.').font=SM
r+=1
M0=r
for lab,basis,rate in [('Escalation','% of trade cost',0.10),
                       ('General conditions','% of trade cost',0.110),
                       ('Overhead, profit & insurance','% of trade cost',0.09)]:
    ws.cell(r,2,lab).font=BLK; ws.cell(r,4,basis).font=SM
    c=ws.cell(r,5,rate); c.number_format=PCT; c.font=BLUE; c.fill=YEL; c.border=BOX
    for i in (2,3,6,7): ws.cell(r,i).border=BOX
    r+=1
ESC,GC,OHP=[M0+i for i in range(3)]
for x in (ESC,OHP): ws.cell(x,6,f'=F{TRADE}*E{x}').number_format=CUR
ws.cell(GC,6,f"=IF($E${GCMODE}=1,F{TRADE}*E{GC},'Thomas Reconciliation'!$G${TRGC})").number_format=CUR
ws.cell(GC,7,'Switches with the General conditions basis toggle at the top of this sheet.').font=SM
ws.cell(r,2,'Markups — subtotal').font=BOLD; ws.cell(r,2).border=TOPB
c=ws.cell(r,6,f'=F{ESC}+F{GC}+F{OHP}'); c.font=BOLD; c.number_format=CUR; c.border=TOPB
for i in (3,4,5,7): ws.cell(r,i).border=TOPB
MKS=r; r+=2

ws.cell(r,2,'CONSTRUCTION COST — trade + markups').font=BOLD; ws.cell(r,2).border=TOPB
c=ws.cell(r,6,f'=F{TRADE}+F{MKS}'); c.font=BOLD; c.number_format=CUR; c.border=TOPB
for i in (3,4,5,7): ws.cell(r,i).border=TOPB
CONSTR=r; r+=2

ws.cell(r,2,'CONTINGENCY').font=BLK; ws.cell(r,4,'single pot — edit the yellow cell').font=SM
c=ws.cell(r,6,5_000_000); c.number_format=CUR; c.font=BLUE; c.fill=YEL; c.border=BOX
for i in (2,3,4,5): ws.cell(r,i).border=BOX
CONT=r; r+=1
ws.cell(r,4,'ONE contingency, not two. Replaces the old contractor contingency and owner contingency, which stacked.').font=SM
r+=1
ws.cell(r,2,'THOMAS\u2019S LINES TOGGLED ON').font=BLK
ws.cell(r,4,'from the reconciliation sheet').font=SM
ws.cell(r,6,f"='Thomas Reconciliation'!$G${TRADD}").number_format=CUR
ws.cell(r,7,'Every one of his 199 lines is listed on the Thomas Reconciliation sheet with an on/off toggle. Default OFF where we already carry the scope, so nothing is double counted. Flip one ON to buy it at HIS price.').font=SM
THOM=r; r+=1
ws.cell(r,2,'FF&E — division 600').font=BLK
ws.cell(r,6,f'=F{FFE}').number_format=CUR; r+=1
ws.cell(r,2,'SOFT COSTS — division 700').font=BLK
ws.cell(r,6,f'=F{SOFT}').number_format=CUR; r+=2

ws.cell(r,2,'TOTAL DEVELOPMENT COST').font=Font(name=F,size=13,bold=True,color='1F3864')
c=ws.cell(r,6,f'=F{TRADE}+F{MKS}+F{CONT}+F{THOM}+F{FFE}+F{SOFT}')
c.font=Font(name=F,size=13,bold=True,color='1F3864')
c.number_format=CUR; c.border=TOPB
for i in (2,3,4,5,7): ws.cell(r,i).border=TOPB
TOT=r; r+=2
for lab,f_,fmt in [('Cost per SF (74,100)',f'=F{TOT}/$E${SFR}','$#,##0'),
                   ('Cost per capacity unit',f'=F{TOT}/$E${SFR+5}','$#,##0'),
                   ('Contingency as % of construction cost',f'=F{CONT}/F{CONSTR}','0.0%')]:
    ws.cell(r,2,lab).font=BLK
    c=ws.cell(r,6,f_); c.number_format=fmt; c.font=BOLD; r+=1
r+=1
ws.freeze_panes='B12'
ws.auto_filter.ref=f'B{SFR+6}:G{TRADE}'

# ================= CUT ANALYSIS SHEET =================
from cuts import C
cs=wb.create_sheet('Cut Analysis')
for col,w in zip('ABCDEFGH',[3,7,46,11,14,14,13,66]): cs.column_dimensions[col].width=w
GRN=Font(name=F,size=9,bold=True,color='008000'); RED2=Font(name=F,size=9,bold=True,color='C00000')
AMB=Font(name=F,size=9,bold=True,color='8A5D00')
r=2
cs.cell(r,2,'WHERE WE CAN CUT').font=H1; r+=1
cs.cell(r,2,'Sorted by how much it costs you to take the saving. Free money first.').font=SM; r+=2
cs.cell(r,2,('Read the TYPE column before the number. A FIX costs nothing. A VERIFY may vanish entirely '
             'once somebody checks. A SCOPE cut means the building is less than it was. Two rows are flagged '
             'SLA or CODE — those need a professional to sign off before they are banked.')).font=BLK
cs.cell(r,2).alignment=wr(); cs.merge_cells(start_row=r,start_column=2,end_row=r,end_column=8)
cs.row_dimensions[r].height=30; r+=2
ORDER=[('FIX','FIX — errors and overpricing. Nothing is lost.'),
       ('VERIFY','VERIFY — may vanish entirely once someone checks. Cheapest money on the sheet.'),
       ('ASK','ASK ROOFLIFTERS — may already sit inside the $3-4M quote.'),
       ('DEFER','DEFER — pay later, little or no penalty.'),
       ('SCOPE','SCOPE — real cuts. You lose something.'),
       ('SCHEDULE','SCHEDULE — programme is the cost driver, not the rate.')]
grand=[]
for key,title in ORDER:
    rows=[x for x in C if x[2]==key]
    if not rows: continue
    cs.cell(r,2,title).font=H2
    for i in range(2,9): cs.cell(r,i).fill=GPF
    r+=1
    for i,h in enumerate(['Div','Item','Carried','Cut to','Saving','Gate','Why, and what it costs you'],2):
        c=cs.cell(r,i,h); c.font=WHT; c.fill=HDR; c.alignment=Alignment(horizontal='center',wrap_text=True)
    r+=1; first=r
    for d,n,t,now,alt,gate,why in rows:
        cs.cell(r,2,d).alignment=Alignment(horizontal='center'); cs.cell(r,2).font=BLK
        cs.cell(r,3,n).font=BLK; cs.cell(r,3).alignment=wr()
        c=cs.cell(r,4,now); c.number_format=CUR; c.font=BLUE
        c=cs.cell(r,5,alt); c.number_format=CUR; c.font=BLUE
        c=cs.cell(r,6,f'=D{r}-E{r}'); c.number_format=CUR; c.font=BOLD
        c=cs.cell(r,7,gate); c.alignment=Alignment(horizontal='center')
        c.font={'OK':GRN,'CODE':RED2,'SLA':RED2,'ASK':AMB}[gate]
        cs.cell(r,8,why).font=SM; cs.cell(r,8).alignment=wr()
        for i in range(2,9): cs.cell(r,i).border=BOX
        r+=1
    cs.cell(r,3,title.split('—')[0].strip()+' subtotal').font=BOLD
    c=cs.cell(r,6,f'=SUM(F{first}:F{r-1})'); c.font=BOLD; c.number_format=CUR; c.border=TOPB
    for i in (2,3,4,5,7,8): cs.cell(r,i).border=TOPB
    grand.append(r); r+=2
cs.cell(r,3,'TOTAL IDENTIFIED').font=Font(name=F,size=12,bold=True,color='1F3864')
c=cs.cell(r,6,'='+'+'.join(f'F{g}' for g in grand))
c.font=Font(name=F,size=12,bold=True,color='1F3864'); c.number_format=CUR; c.border=TOPB
for i in (2,3,4,5,7,8): cs.cell(r,i).border=TOPB
CUTTOT=r; r+=1
cs.cell(r,3,'Budget as it stands').font=BLK
cs.cell(r,6,f"='Detailed Budget'!F{TOT}").number_format=CUR; r+=1
cs.cell(r,3,'Budget with every cut taken').font=BOLD
c=cs.cell(r,6,f"='Detailed Budget'!F{TOT}-F{CUTTOT}"); c.font=BOLD; c.number_format=CUR; c.border=TOPB
cs.cell(r,3).border=TOPB
cs.cell(r,8,'Not realistic to take all of them — the SCOPE and SLA rows have real consequences. Treat FIX + VERIFY + ASK as the honest target.').font=SM
cs.cell(r,8).alignment=wr(); r+=2
cs.cell(r,2,'DO THESE FOUR THINGS FIRST').font=RED2; r+=1
for t in ['Commission the ACP-5 asbestos survey. A few thousand dollars could delete $555,750 of presumed roof abatement. Best return on this sheet by an order of magnitude.',
          'Get the four Rooflifters answers in writing: are footings in, is the roof-to-wall closure in, union or non-union basis, and the quote date. Worth $1.33M of swing.',
          'Ask the mechanical engineer whether HVAC was priced on load or on area. The contractor used $40/SF over 120,000 SF against a 74,100 SF building. Worth $1M+.',
          'Get the Con Ed feasibility letter. The $850,000 vault and feeder line is my estimate with no utility quote behind it, and the lead time drives the schedule.']:
    cs.cell(r,2,'•').font=BLK; cs.cell(r,3,t).font=BLK; cs.cell(r,3).alignment=wr()
    cs.merge_cells(start_row=r,start_column=3,end_row=r,end_column=8)
    cs.row_dimensions[r].height=max(13,12*(len(t)//105+1)); r+=1


# ================= OPTIONS SHEET =================
op=wb.create_sheet('Options')
for col,w in zip('ABCDEFG',[3,46,15,15,13,13,62]): op.column_dimensions[col].width=w
r=2
op.cell(r,2,'HOW TO GET THIS NUMBER DOWN').font=H1; r+=1
op.cell(r,2,'Six options, stacked. Each one includes everything above it.').font=SM; r+=2
op.cell(r,2,'FIRST — LOOK AT THE MARKUP STACK').font=H2; r+=1
op.cell(r,2,('Trade cost is $37.5M. Below the line sits $27.2M more — $11.3M of markups, a $5.0M contingency, '
             '$5.6M of FF&E and $5.4M of soft costs. The three markup RATES total 30% of trade cost and buy you '
             'no work at all, so every point negotiated off them is free money. Nothing here costs you scope.')).font=BLK
op.cell(r,2).alignment=wr(); op.merge_cells(start_row=r,start_column=2,end_row=r,end_column=7)
op.row_dimensions[r].height=30; r+=2
for i,h in enumerate(['Rate','As carried','Target','Worth','','Why the target is reasonable'],2):
    if i==6: continue
    c=op.cell(r,i,h); c.font=WHT; c.fill=HDR; c.alignment=Alignment(horizontal='center',wrap_text=True)
r+=1
for lab,now,tgt,worth,why in [
  ('Escalation',0.10,0.06,1_500_053,'10% assumes a long gap between estimate and buyout. Buy out steel, switchgear, elevators and HVAC plant early and lock the price.'),
  ('General conditions',0.110,0.085,937_533,'Duration-driven, not scope-driven. Ask for it as a MONTHLY RATE plus a duration instead of a percentage and it has to defend itself.'),
  ('Overhead, profit & insurance',0.09,0.065,937_533,'Split it apart: insurance as an actual broker premium, overhead and profit as a FIXED FEE IN DOLLARS so it does not grow when scope grows.')]:
    op.cell(r,2,lab).font=BLK
    c=op.cell(r,3,now); c.number_format=PCT; c.font=BLUE
    c=op.cell(r,4,tgt); c.number_format=PCT; c.font=BLUE
    c=op.cell(r,5,worth); c.number_format=CUR; c.font=BOLD
    op.cell(r,7,why).font=SM; op.cell(r,7).alignment=wr()
    for i in range(2,8): op.cell(r,i).border=BOX
    r+=1
op.cell(r,2,'Total available on rates alone').font=BOLD; op.cell(r,2).border=TOPB
c=op.cell(r,5,f'=SUM(E{r-3}:E{r-1})'); c.font=BOLD; c.number_format=CUR; c.border=TOPB
for i in (3,4,7): op.cell(r,i).border=TOPB
r+=2
op.cell(r,2,'THE SIX OPTIONS').font=H2; r+=1
for i,h in enumerate(['Option','Total','$/SF','$/cap','Step','What it costs you'],2):
    c=op.cell(r,i,h); c.font=WHT; c.fill=HDR; c.alignment=Alignment(horizontal='center',wrap_text=True)
r+=1
OPTS=[('0.  As it stands',73_962_877,998,9_941,None,'—'),
      ('1.  Take the free cuts',67_244_411,907,9_038,-6_718_466,'Nothing. Asbestos survey, Rooflifters answers, HVAC load basis, two arithmetic errors.'),
      ('2.  + negotiate the markups',59_130_282,798,7_948,-8_114_129,'Nothing in scope. Open-book GMP with shared savings, earlier buyout, contingency to 12%. THIS IS THE TARGET.'),
      ('3.  + landlord funds the roof lift',48_836_545,659,6_564,-10_293_737,'Negotiating capital with Eric. The lift is a permanent improvement to his building that outlives a 20-year lease.'),
      ('4.  + drop the lift 50ft to 40ft',46_900_000,633,6_304,-1_936_545,'THE MOAT. Not recommended — shown only so the number is visible. At 40 ft you lose flown production and the positioning argument.'),
      ('5.  + defer the mezzanine',43_900_000,592,8_442,-3_000_000,'2,240 capacity and the compliance seating location. Opens floor-only at ~5,200. Structure must still go in later at a premium.'),
      ('6.  + owner-furnish, direct trades',40_300_000,544,7_750,-3_600_000,'Delivery risk moves to you. Buy switchgear, HVAC plant and elevators direct; fewer trades under GC markup.')]
for nm,tot,psf,pcap,step,cost in OPTS:
    op.cell(r,2,nm).font=BOLD if '2.' in nm else BLK
    c=op.cell(r,3,tot); c.number_format=CUR; c.font=BOLD if '2.' in nm else BLUE
    op.cell(r,4,psf).number_format='$#,##0'
    op.cell(r,5,pcap).number_format='$#,##0'
    if step: 
        c=op.cell(r,6,step); c.number_format=CUR
    op.cell(r,7,cost).font=SM; op.cell(r,7).alignment=wr()
    for i in range(2,8): op.cell(r,i).border=BOX
    if '2.' in nm:
        for i in range(2,8): op.cell(r,i).fill=PatternFill('solid',fgColor='E2EFDA')
    r+=1
r+=1
op.cell(r,2,('RECOMMENDED: Option 2 at $59.1M. It costs nothing in scope — it is arithmetic corrections, '
             'evidence-gathering and contract structure. Options 3 through 6 all trade something real away, '
             'and Option 4 trades the moat.')).font=RED2
op.cell(r,2).alignment=wr(); op.merge_cells(start_row=r,start_column=2,end_row=r,end_column=7)
op.row_dimensions[r].height=30

# ================= QUESTIONS SHEET =================
from questions import Q
qs=wb.create_sheet('Questions to Ask')
for col,w in zip('ABCDE',[3,6,78,62,15]): qs.column_dimensions[col].width=w
r=2
qs.cell(r,2,'QUESTIONS').font=H1; r+=1
qs.cell(r,2,'49 questions, by who to ask. Each carries the evidence that makes it hard to deflect.').font=SM; r+=2
num=0
for who,items in Q:
    qs.cell(r,2,who).font=DIV
    for i in range(2,6): qs.cell(r,i).fill=DVF
    r+=1
    for i,h in enumerate(['No.','Question','Why it is hard to deflect','$ at stake'],2):
        c=qs.cell(r,i,h); c.font=WHT; c.fill=HDR; c.alignment=Alignment(horizontal='center',wrap_text=True)
    r+=1
    for q,why,stake in items:
        num+=1
        qs.cell(r,2,num).alignment=Alignment(horizontal='center'); qs.cell(r,2).font=BLK
        qs.cell(r,3,q).font=BLK; qs.cell(r,3).alignment=wr()
        qs.cell(r,4,why).font=SM; qs.cell(r,4).alignment=wr()
        c=qs.cell(r,5,stake); c.font=BOLD; c.alignment=Alignment(horizontal='right',vertical='top')
        for i in range(2,6): qs.cell(r,i).border=BOX
        r+=1
    r+=1


from markups import M
mk=wb.create_sheet('Markups Explained',1)
for col,w in zip('ABCDEF',[3,26,10,12,44,60]): mk.column_dimensions[col].width=w
r=2
mk.cell(r,2,'THE MARKUPS, EXPLAINED').font=H1; r+=1
mk.cell(r,2,'What each one is, who gets it, whether it is necessary, and what is actually negotiable.').font=SM; r+=2
mk.cell(r,2,('RESTRUCTURED. Trade cost now stands alone at $37.5M and everything else sits BELOW THE LINE as a '
             'separate cost. The three markup rates are each applied to trade cost only — they no longer compound '
             'on each other. Contractor contingency and owner contingency have been replaced by ONE $5.0M '
             'contingency, so no contingency is charged twice. A dollar of trade scope removed now saves $1.30.')).font=BLK
mk.cell(r,2).alignment=wr(); mk.merge_cells(start_row=r,start_column=2,end_row=r,end_column=6)
mk.row_dimensions[r].height=32; r+=2
for i,h in enumerate(['Line','Carried','Target','What it is / who gets it / is it necessary','What is actually negotiable'],2):
    c=mk.cell(r,i,h); c.font=WHT; c.fill=HDR; c.alignment=Alignment(horizontal='center',vertical='center',wrap_text=True)
r+=1
for name,now,tgt,what,who,nec,neg in M:
    mk.cell(r,2,name).font=BOLD; mk.cell(r,2).alignment=wr()
    mk.cell(r,3,now).alignment=Alignment(horizontal='center'); mk.cell(r,3).font=BLUE
    mk.cell(r,4,tgt).alignment=Alignment(horizontal='center'); mk.cell(r,4).font=BLUE
    mk.cell(r,5,'WHAT IT IS: '+what+'\n\nWHO GETS IT: '+who+'\n\nNECESSARY? '+nec).font=BLK; mk.cell(r,5).alignment=wr()
    mk.cell(r,6,neg).font=SM; mk.cell(r,6).alignment=wr()
    for i in range(2,7): mk.cell(r,i).border=BOX
    mk.row_dimensions[r].height=max(90,10.5*((len(what)+len(who)+len(nec))//38))
    r+=1
r+=1
mk.cell(r,2,'HOW IT STACKS NOW').font=H2; r+=1
for lab,f_,note in [('TRADE COST — the work itself',f"='Detailed Budget'!F{TRADE}",'divisions 000-500 plus 800'),
    ('+ Escalation, 10% of trade',f"='Detailed Budget'!F{ESC}",'on trade cost only'),
    ('+ General conditions, 11% of trade',f"='Detailed Budget'!F{GC}",'on trade cost only'),
    ('+ Overhead, profit & insurance, 9% of trade',f"='Detailed Budget'!F{OHP}",'on trade cost only'),
    ('CONSTRUCTION COST — the work plus its markups',f"='Detailed Budget'!F{CONSTR}",'what it costs to build'),
    ('+ Contingency',f"='Detailed Budget'!F{CONT}",'ONE pot. Was two, stacked. Now a flat dollar figure you set'),
    ('+ FF&E',f"='Detailed Budget'!F{FFE}",'sound, lights, video, bars, seating, furniture'),
    ('+ Soft costs',f"='Detailed Budget'!F{SOFT}",'design, permits, legal, project management'),
    ('TOTAL DEVELOPMENT COST',f"='Detailed Budget'!F{TOT}",'')]:
    hv=lab.startswith(('TOTAL','CONSTRUCTION','TRADE'))
    mk.cell(r,2,lab).font=BOLD if hv else BLK
    c=mk.cell(r,4,f_); c.number_format=CUR; c.font=BOLD if hv else BLK
    if lab.startswith('TOTAL'):
        c.border=TOPB; mk.cell(r,2).border=TOPB
    mk.cell(r,5,note).font=SM
    r+=1
r+=2
mk.cell(r,2,'TWO THINGS TO UNDERSTAND BEFORE YOU CUT ANY OF THESE').font=RED2; r+=1
for t in ['CONTINGENCY IS THE ONE NOT TO CUT — and it matters MORE here than on a normal job. Eric owns the building; you are building it out and renting it. If you run out of money mid-construction you cannot pause, cannot walk away, and cannot refinance against the asset, because the improvement is already sunk into someone else\'s building. Every change order lands on you. $5,000,000 is about 10% of construction cost — thin for a design-stage number on a 1920s warehouse with no asbestos survey, no Con Ed feasibility letter and no structural analysis of whether the roof can be lifted at all. Do not draw it down for scope you choose to add; that is a budget increase, not a contingency draw.',
          'THE ROOF LIFT IS THE MOST EXPENSIVE THING IN THE PROJECT. Division 100 is $7,146,288 before markups — 19% of trade cost, and roughly $9.3M of the final number once the markups are applied. $3.5M of that is your quoted lift contract; $3.6M is scope the lifter explicitly excludes. It is also mandatory, so the only two questions are whether it is a LIFT or a REPLACEMENT (a $4.9M difference) and how much of the surrounding scope is already inside the quote ($1.33M of swing). Both are answered by the same phone call.']:
    mk.cell(r,2,'•').font=BLK; mk.cell(r,3,t).font=BLK; mk.cell(r,3).alignment=wr()
    mk.merge_cells(start_row=r,start_column=3,end_row=r,end_column=6)
    mk.row_dimensions[r].height=max(13,12*(len(t)//110+1)); r+=1


# ================= THOMAS RECONCILIATION SHEET =================
import thomas as TH
tr=wb.create_sheet('Thomas Reconciliation')
for col,w in zip('ABCDEFGHI',[3,7,52,7,6,11,12,9,66]): tr.column_dimensions[col].width=w
r=2
tr.cell(r,2,'THOMAS’S BUDGET — EVERY LINE, RECONCILED').font=H1; r+=1
tr.cell(r,2,'All 199 trade lines from the Master Development Budget dated 7 Sep 2026. Nothing dropped.').font=SM; r+=2

tr.cell(r,2,'GENERAL CONDITIONS — PICK ONE, NOT BOTH').font=H2
tr.cell(r,6,'GC line items').font=SM
assert r==TRGC,(r,TRGC)
GCROW=r
tr.cell(r,9,('Thomas carries $1,696,000 of general conditions as TRADE LINES (013000 + 015800: site office, site security, '
             'safety plan, portable toilets, clean-up, rubbish, final clean, project labour, field technology). We also apply an '
             '11%% general conditions markup on trade cost, which is $4,125,146. THAT IS THE SAME SITE COST TWICE. '
             'The toggle at the top of the Detailed Budget picks one: 1 = the percentage, 0 = his line items. '
             'His line items are $2,429,146 CHEAPER — but they are also incomplete, since all of 015800 sits at qty 0.')).font=BLK
tr.cell(r,9).alignment=wr(); tr.row_dimensions[r].height=58
r+=1
assert r==TRADD,(r,TRADD)
ADDROW=r
tr.cell(r,2,'ADD-BACKS TOGGLED ON').font=BOLD
tr.cell(r,9,'Live total of every non-GC line whose toggle is 1. Feeds the Detailed Budget below the line. Default is zero.').font=SM
r+=2

for i,h in enumerate(['CSI','Description','Qty','Unit','His rate','His total','ON=1','Status — where it lands in this model / why it is off'],2):
    c=tr.cell(r,i,h); c.font=WHT; c.fill=HDR; c.alignment=Alignment(horizontal='center',vertical='center',wrap_text=True)
r+=1
first=r; cur=None; togs=[]
for l in TH.LINES:
    if l['csi']!=cur:
        cur=l['csi']
        tr.cell(r,2,f"{l['csi']}   {l['dname']}").font=DIV
        for i in range(2,10): tr.cell(r,i).fill=DVF
        r+=1
    tr.cell(r,2,l['csi']).font=SM
    tr.cell(r,3,f"{l['no']}. {l['desc']}").font=BLK; tr.cell(r,3).alignment=wr()
    tr.cell(r,4,l['qty']).number_format='#,##0;;"-"'
    tr.cell(r,5,l['unit']).font=SM
    tr.cell(r,6,l['rate']).number_format=CUR
    tr.cell(r,7,l['tot']).number_format=CUR
    c=tr.cell(r,8,l['on']); c.font=BLUE; c.fill=YEL; c.border=BOX; c.alignment=Alignment(horizontal='center')
    txt=l['status']+' — '+l['where']
    if l['his_note']: txt+='  [his note: '+l['his_note']+']'
    cc=tr.cell(r,9,txt); cc.alignment=wr()
    cc.font=RED2 if l['status'] in ('ADD','GC') else BLK
    for i in range(2,10): tr.cell(r,i).border=BOX
    tr.cell(r,10,0 if l['status']=='GC' else f'=H{r}*G{r}').number_format=CUR
    tr.row_dimensions[r].height=max(13,11*(len(txt)//60+1))
    togs.append(r); r+=1
last=r-1
tr.cell(r,3,'THOMAS’S SCHEDULE AS FILED — total of all 199 lines').font=BOLD; tr.cell(r,3).border=TOPB
c=tr.cell(r,7,f'=SUM(G{first}:G{last})'); c.font=BOLD; c.number_format=CUR; c.border=TOPB
for i in (2,4,5,6,8,9): tr.cell(r,i).border=TOPB
r+=1
tr.cell(r,3,'Two thirds of his schedule sits at QTY 0, which is why $10.5M of lines describes a $42.6M project.').font=SM

# wire the two summary cells now that the rows are known
tr.cell(GCROW,7,f'=SUMIF(I{first}:I{last},"GC*",G{first}:G{last})').number_format=CUR
tr.cell(GCROW,7).font=BOLD
tr.cell(ADDROW,7,f'=SUM(J{first}:J{last})').number_format=CUR
tr.cell(ADDROW,7).font=BOLD
tr.column_dimensions['J'].hidden=True
tr.freeze_panes='C%d'%first
tr.auto_filter.ref=f'B{first-1}:I{last}'
print('total row',TOT)

wb.calculation.fullCalcOnLoad=True
wb.save('165_Randolph_Detailed_Budget.xlsx')