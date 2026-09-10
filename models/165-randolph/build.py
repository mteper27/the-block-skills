# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'.')
from lines import L
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

F='Arial'
BLUE=Font(name=F,size=10,color='0000FF'); BLK=Font(name=F,size=10); GRN=Font(name=F,size=10,color='008000')
BOLD=Font(name=F,size=10,bold=True); H1=Font(name=F,size=16,bold=True,color='1F3864')
H2=Font(name=F,size=12,bold=True,color='1F3864'); WHT=Font(name=F,size=10,bold=True,color='FFFFFF')
SM=Font(name=F,size=9,color='595959'); RED=Font(name=F,size=10,bold=True,color='C00000')
HDR=PatternFill('solid',fgColor='1F3864'); YEL=PatternFill('solid',fgColor='FFFF00')
T0=PatternFill('solid',fgColor='FCE4D6'); T1=PatternFill('solid',fgColor='DDEBF7')
T2=PatternFill('solid',fgColor='E2EFDA'); TR=PatternFill('solid',fgColor='FFF2CC')
thin=Side(style='thin',color='BFBFBF'); med=Side(style='medium',color='1F3864')
BOX=Border(left=thin,right=thin,top=thin,bottom=thin); TOPB=Border(top=med)
CUR='$#,##0;($#,##0);"-"'; PCT='0.0%'
def wrap(v='top'): return Alignment(wrap_text=True,vertical=v)

wb=Workbook()
STY=dict(BLUE=BLUE,BLK=BLK,BOLD=BOLD,H1=H1,H2=H2,WHT=WHT,SM=SM,RED=RED,HDR=HDR,YEL=YEL,
         BOX=BOX,TOPB=TOPB,CUR=CUR,wrap=wrap)
from infinity import NOT_INFINITY, INFINITY_REDUCED

# ============================================================ READ ME
ws=wb.active; ws.title='Read Me'
for col,w in zip('ABC',[3,26,104]): ws.column_dimensions[col].width=w
r=2
ws[f'B{r}']='165 RANDOLPH STREET — COST TO BUILD & OPEN'; ws[f'B{r}'].font=H1; r+=1
ws[f'B{r}']='Brooklyn, NY 11237  ·  Live Nation / Insomniac  ·  CONSTRUCTION ONLY  ·  CONFIDENTIAL'; ws[f'B{r}'].font=SM; r+=2
def para(label,text,rr):
    ws[f'B{rr}']=label; ws[f'B{rr}'].font=BOLD
    ws[f'C{rr}']=text; ws[f'C{rr}'].font=BLK; ws[f'C{rr}'].alignment=wrap()
    ws.row_dimensions[rr].height=max(14,12.5*(len(text)//98+1)); return rr+1
r=para('Scope of this model','Construction only: building the building, the production systems, getting it coded, and getting the liquor licence. No revenue, no operating costs, no returns — 165 Randolph has its own revenue model and this does not duplicate it.',r)
r=para('The question it answers','What is the least we can spend and still open the doors, and what does every additional item cost on top of that?',r)
r=para('Why the filed budget cannot answer it','The Master Development Budget v1 totals $42,555,099. One cell overstates it by $5,224,148 — 3rd-floor VIP pavers at $3,312.50/SF where the lines above and below are $31/SF — which marks up four times to $6,890,129. Meanwhile roughly two-thirds of the trade schedule carries a unit price against a QUANTITY OF ZERO. The two errors point opposite ways and roughly cancel, which is why the total looked plausible next to the $45M underwriting case.',r)
r=para('How to use it','Open Line Build. Every one of the 101 lines carries a TIER. Change a tier and all four scenarios on Scenario Summary recalculate. Blue cells are inputs you can edit, black cells are formulas, green cells pull from another sheet. The Reconciliation block at the bottom of Line Build proves the "As Filed" column ties to the source workbook to the dollar.',r)
r+=1
ws[f'B{r}']='THE TIERS'; ws[f'B{r}'].font=H2; r+=1
for code,name,fill,desc in [
 ('0','Shell & Life Safety',T0,'No Certificate of Occupancy without it. Structure, egress, fire protection and alarm, MEP, ADA, abatement, code compliance.'),
 ('1','Revenue Enabling',T1,'Cannot sell a ticket or serve a drink without it. Stage and rigging steel, bars, audio, performance lighting, acoustic treatment, screening, IT.'),
 ('R','Roof Raise — the fork',TR,'The 20ft to 50ft lift. Priced at ZERO in the filed budget. Drives the production ceiling and the premium positioning. It does NOT drive capacity — 7,440 works at either height.'),
 ('2','Positioning / Phase 2',T2,'The building opens and trades without it. Roof decks, restaurant, VIP fit-out, LED walls, architectural lighting, art, parking garage.')]:
    ws[f'B{r}']=f'  Tier {code} — {name}'; ws[f'B{r}'].font=BOLD; ws[f'B{r}'].fill=fill
    ws[f'C{r}']=desc; ws[f'C{r}'].font=BLK; ws[f'C{r}'].alignment=wrap(); r+=1
r+=1
ws[f'B{r}']='THE FOUR SCENARIOS'; ws[f'B{r}'].font=H2; r+=1
for n,d in [('1. Absolute Floor','Tiers 0 + 1, roof left alone, and the three rent-or-free items deferred (house audio, performance lighting, POS). The lowest number that still opens the doors.'),
            ('2. Open Minimum','Tiers 0 + 1, roof left alone. Own the audio and lighting rig from day one rather than renting it.'),
            ('3. Open + 50ft Raise','Scenario 2 plus Tier R. This is the building the underwriting describes.'),
            ('4. Full Scope','Everything — roof decks, restaurant, VIP lounge, LED walls, architectural lighting and the parking garage.')]:
    ws[f'B{r}']='  '+n; ws[f'B{r}'].font=BOLD
    ws[f'C{r}']=d; ws[f'C{r}'].font=BLK; ws[f'C{r}'].alignment=wrap(); r+=1
r+=1
r=para('Basis of the Corrected column','Where the source file supplies a unit price, the corrected cost uses THAT rate against a measured or reasoned quantity — so most of this is the estimator\'s own pricing, applied to quantities that were left at zero. Where the file gives no rate, the figure comes from NYC assembly-occupancy norms and the line note says so. Where MT supplied a better number in the annotated copy, MT\'s number is used and cited.',r)
r=para('Explicitly excluded','Revenue of any kind. Operating costs. Returns and IRR. Rent, NNN and lease economics. Pre-opening hiring, training and launch marketing. Anything from the Miami takeover folder or the Ace Mission analysis — neither was available. The Wake PD04 Rev 4.4 test fit has not been reviewed directly.',r)
r+=1
ws[f'B{r}']='Prepared 9 Sep 2026 from Master Development Budget v1 (7 Sep 2026) and MT notes & questions.'; ws[f'B{r}'].font=SM

# ============================================================ LINE BUILD
lb=wb.create_sheet('Line Build')
heads=['Code','Section','Description','Tier','Rent/\nFree','Infinity\nroom?','As Filed','Corrected','Infinity $','Variance','Basis / note']
for i,(h,w) in enumerate(zip(heads,[10,10,58,6,7,8,15,15,15,14,98]),1):
    c=lb.cell(1,i,h); c.font=WHT; c.fill=HDR; c.alignment=Alignment(horizontal='center',vertical='center',wrap_text=True)
    lb.column_dimensions[get_column_letter(i)].width=w
lb.row_dimensions[1].height=30; lb.freeze_panes='D2'
VE=('house audio system','performance lighting','POS terminals')
row=2
for code,sec,desc,filed,corr,tier,note in L:
    ve='Y' if any(k in desc for k in VE) else ''
    if desc in NOT_INFINITY:
        inf='N'; infv=0; extra=' [OUT of an Infinity room: '+NOT_INFINITY[desc]+']'
    elif desc in INFINITY_REDUCED:
        _a,_b,_why=INFINITY_REDUCED[desc]; inf='part'; infv=_b
        extra=' [Infinity room: reduced to $%s — %s]'%(format(_b,',d'),_why)
    else:
        inf='Y'; infv=corr if isinstance(corr,(int,float)) else corr; extra=''
    for i,v in enumerate([code,sec,desc,tier,ve,inf,filed,corr,infv,f'=H{row}-G{row}',note+extra],1):
        c=lb.cell(row,i,v); c.font=BLK; c.border=BOX
        if i in (7,8,9,10): c.number_format=CUR
        if i in (8,9): c.font=BLUE
        if i in (1,2,4,5,6): c.alignment=Alignment(horizontal='center')
        if i==3: c.alignment=Alignment(vertical='top')
        if i==11: c.font=SM; c.alignment=wrap()
    lb.cell(row,4).fill={'0':T0,'1':T1,'2':T2,'R':TR}[tier]
    if inf=='N': lb.cell(row,6).fill=PatternFill('solid',fgColor='FFC7CE')
    elif inf=='part': lb.cell(row,6).fill=PatternFill('solid',fgColor='FFEB9C')
    else: lb.cell(row,6).fill=PatternFill('solid',fgColor='C6EFCE')
    row+=1
LAST=row-1
lb.cell(row,3,'TOTAL').font=BOLD; lb.cell(row,3).border=TOPB
for col in (7,8,9,10):
    cl=get_column_letter(col); c=lb.cell(row,col,f'=SUM({cl}2:{cl}{LAST})')
    c.font=BOLD; c.number_format=CUR; c.border=TOPB
lb.auto_filter.ref=f'A1:K{LAST}'
r2=row+2
lb.cell(r2,3,'RECONCILIATION — the "As Filed" column must tie to the Master Development Budget').font=H2; r2+=1
for lab,sec,src in [('Trade costs','TRADE',18175107.5),('Off-site costs','OFFSITE',2257500),
                    ('Soft costs','SOFT',4006750),('FF&E','FFE',8232250)]:
    lb.cell(r2,3,lab).font=BLK
    lb.cell(r2,7,f'=SUMIFS($G$2:$G${LAST},$B$2:$B${LAST},"{sec}")').number_format=CUR
    c=lb.cell(r2,8,src); c.number_format=CUR; c.font=BLUE
    lb.cell(r2,10,f'=G{r2}-H{r2}').number_format=CUR
    lb.cell(r2,11,'Source workbook figure').font=SM; r2+=1
lb.cell(r2,3,'Total variance — must be zero').font=BOLD; lb.cell(r2,3).border=TOPB
c=lb.cell(r2,10,f'=SUM(J{r2-4}:J{r2-1})'); c.number_format=CUR; c.font=BOLD; c.border=TOPB

# ============================================================ ROOF LIFT
from roof import build_roof
build_roof(wb,STY)

from seating import build_seating
build_seating(wb,STY,4)

# ============================================================ SCENARIO SUMMARY
ss=wb.create_sheet('Scenario Summary',1)
for col,w in zip('ABCDEFG',[3,44,17,17,17,17,56]): ss.column_dimensions[col].width=w
r=2
ss[f'B{r}']='WHAT IT COSTS TO BUILD AND OPEN'; ss[f'B{r}'].font=H1; r+=1
ss[f'B{r}']='Construction, production, code and liquor licence. Driven entirely by the Tier column on Line Build.'; ss[f'B{r}'].font=SM; r+=2
ss[f'B{r}']='ASSUMPTIONS   —   edit the yellow cells'; ss[f'B{r}'].font=H2; r+=1
A0=r
for label,val,note in [
 ('General conditions, % of trade + escalation',0.110,'Filed $2,000,000 against $18,175,108 of trade. The hidden GC tab totals $2,082,000 — an $82k break.'),
 ('Overhead, profit & insurance, % of trade + GC',0.09,'As filed (9% combined).'),
 ('Contractor contingency, %',0.10,'As filed.'),
 ('Owner contingency, %',0.10,'As filed. 25-35% is the norm at this design stage with this much scope unpriced. Raise it to test.'),
 ('Escalation on trade cost, %',0.10,'FILED AT ZERO — the line exists and was left blank while the parking garage got 5%. 5%/yr across a 2-year build.'),
 ('Building footprint (SF, under roof)',74100,'YOUR CORRECTION. The rent basis, and what roofing, envelope and HVAC volume follow. The mezzanine sits inside this.'),
 ('Total floor area, all levels (SF)',135953,'What sprinklers, fire alarm, partitions and flooring follow. The dev budget uses this as its headline SF, which is why it reports $313/SF.'),
 ('Capacity, GA standing',7440,'Development budget and Wake test fit. Ground floor plus mezzanine, within the 74,100 SF footprint.')]:
    ss.cell(r,2,label).font=BLK
    c=ss.cell(r,3,val); c.font=BLUE; c.fill=YEL; c.border=BOX
    c.number_format=PCT if val<1 else '#,##0'
    ss.cell(r,7,note).font=SM; ss.cell(r,7).alignment=wrap(); r+=1
GC_R,OHP_R,CC_R,OC_R,ESC_R,SF_R,FA_R,CAP_R=[A0+i for i in range(8)]
r+=1
ss[f'B{r}']='THE LADDER'; ss[f'B{r}'].font=H2; r+=1
for i,t in enumerate(['','SHELL & CODE\ntier 0 only, no lift','BASE\nshell + revenue, no lift',
                      'BASE + LIFT\nshell + revenue + lift','ELEVATED\nfull fit-out + lift','PREMIUM\neverything']):
    c=ss.cell(r,2+i,t); c.font=WHT; c.fill=HDR; c.alignment=Alignment(horizontal='center',vertical='center',wrap_text=True)
ss.row_dimensions[r].height=34; r+=1
SEC=[('Trade costs','TRADE'),('Off-site costs','OFFSITE'),('Soft costs','SOFT'),('FF&E','FFE')]
secrow={}
for lab,key in SEC:
    ss.cell(r,2,lab).font=BLK; ss.cell(r,10,key).font=SM; secrow[key]=r; r+=1
ss.column_dimensions['J'].hidden=True
# A = Infinity $ column (I), tiers 0/1/R.  B,C,D = Corrected column (H).
SCEN=[(['0'],'I'),(['0','1'],'I'),(['0','1','R'],'I'),(['0','1','R'],'H'),(['0','1','R','2'],'H')]
for key,rr in secrow.items():
    for j,(tiers,valcol) in enumerate(SCEN):
        parts=[f'SUMIFS(\'Line Build\'!${valcol}$2:${valcol}${LAST},\'Line Build\'!$B$2:$B${LAST},$J{rr},'
               f'\'Line Build\'!$D$2:$D${LAST},"{t}")' for t in tiers]
        c=ss.cell(rr,3+j,'='+'+'.join(parts)); c.font=GRN; c.number_format=CUR; c.border=BOX
TR_,OF_,SO_,FF_=secrow['TRADE'],secrow['OFFSITE'],secrow['SOFT'],secrow['FFE']
r=max(secrow.values())+1
def line(label,fn,bold=False,top=False,fmt=CUR):
    global r
    c0=ss.cell(r,2,label); c0.font=BOLD if bold else BLK
    if top: c0.border=TOPB
    for j in range(5):
        col=get_column_letter(3+j); c=ss.cell(r,3+j,fn(col)); c.number_format=fmt
        c.font=BOLD if bold else BLK
        if top: c.border=TOPB
    r+=1; return r-1
ESC=line('Escalation on trade cost',lambda c:f'={c}{TR_}*$C${ESC_R}')
GC =line('General conditions',lambda c:f'=({c}{TR_}+{c}{ESC})*$C${GC_R}')
OHP=line('Overhead, profit & insurance',lambda c:f'=({c}{TR_}+{c}{ESC}+{c}{GC})*$C${OHP_R}')
CCX=line('Contractor contingency',lambda c:f'=({c}{TR_}+{c}{ESC}+{c}{GC}+{c}{OHP})*$C${CC_R}')
SUB=line('Subtotal before owner contingency',
         lambda c:f'={c}{TR_}+{c}{OF_}+{c}{SO_}+{c}{FF_}+{c}{ESC}+{c}{GC}+{c}{OHP}+{c}{CCX}',bold=True,top=True)
OWN=line('Owner contingency',lambda c:f'={c}{SUB}*$C${OC_R}')
TOT=line('TOTAL CAPITAL COST',lambda c:f'={c}{SUB}+{c}{OWN}',bold=True,top=True)
ss.row_dimensions[TOT].height=18
r+=1
line('Cost per SF — on 74,100 footprint',lambda c:f'={c}{TOT}/$C${SF_R}',fmt='$#,##0')
line('Cost per SF — on all floor area',lambda c:f'={c}{TOT}/$C${FA_R}',fmt='$#,##0')
line('Cost per capacity unit',lambda c:f'={c}{TOT}/$C${CAP_R}',fmt='$#,##0')
STEP=line('Step up from the scenario to its left',
          lambda c:'="—"' if c=='C' else f'={c}{TOT}-{get_column_letter(ord(c)-1)}{TOT}',bold=True)
r+=1
ss.cell(r,2,'MEMO — for comparison').font=H2; r+=1
for lab,val,note in [('Master Development Budget v1, as filed',42555099,'Contains the $5.22M paver error and ~2/3 of trades at zero quantity. Not a usable number.'),
                     ('Same budget, paver error corrected only',35664970,'What the filed schedule actually prices, before any missing scope is added back.'),
                     ('Underwriting base case',45000000,'Of which $12,280,860 — 27.3% — was explicitly unallocated scope on its own reconciliation line.'),
                     ('Underwriting high case',65000000,'')]:
    ss.cell(r,2,lab).font=BLK
    c=ss.cell(r,3,val); c.number_format=CUR; c.font=BLUE
    ss.cell(r,7,note).font=SM; ss.cell(r,7).alignment=wrap(); r+=1
r+=1
ss.cell(r,2,'THE POINT').font=RED
ss.cell(r,3,'=("Shell and code alone is "&TEXT(C'+str(TOT)+',"$#,##0")&". Adding what it takes to trade brings it to "&TEXT(D'+str(TOT)+',"$#,##0")&". The lift adds "&TEXT(E'+str(TOT)+'-D'+str(TOT)+',"$#,##0")&".")').font=BOLD
ss.merge_cells(start_row=r,start_column=3,end_row=r,end_column=7)
r+=2
ss.cell(r,2,'WHAT EACH STEP BUYS').font=H2; r+=1
for t in ['SHELL & CODE — the building exists and passes code, and nothing more. Structure, envelope, roof, full MEP, fire protection and alarm, egress, bathrooms to code, abatement, ADA, permits and licensing soft costs. No stage, no bars, no audio, no acoustic treatment. You cannot trade from here, but you can get a Certificate of Occupancy.',
          'BASE — the cheapest room that legally opens. Full structure, full MEP, full life safety, acoustic treatment, ground-supported stage and towers, mezzanine, six bars, bathrooms to code, and removable theatre seating on the mezzanine for the classification. Finishes are sealed concrete and exposed painted structure. No roof decks, no restaurant or kitchen (a separate company runs it), no VIP lounge, no architectural lighting, no art.',
          'BASE + LIFT — the same room, taller. With a ground-supported stage the lift no longer buys rigging capacity; it buys volume, LED headroom, sightlines and the feel of the room. Use the Roof Lift sheet to dial the height: 35-40 ft may get you most of it for materially less than 50.',
          'ELEVATED — restores the full fit-out at the same scope: nine bars rather than six, tile and resilient flooring instead of sealed concrete, four-stop lifts, the full signage package, VIP lounge and a proper finish standard throughout.',
          'PREMIUM — adds the things the concept does not need: roof decks and terraces, the restaurant, the $1.75M architectural lighting package, interior art and scenic, and the parking garage.',
          'THEATRE SEATING STAYS IN EVERY SCENARIO. The seating and the technical drawings that show it are what classify the room as a theater, and that classification carries the liquor and cabaret licences. It is repriced from $125 to $25 a seat per MT H127, saving $371,400 — but it is never deleted.',
          'What it keeps: the volume, the lift, a ground-supported stage and tower system, the mezzanine, bars, bathrooms to code, full life safety, full MEP, acoustic treatment, and the production rig.']:
    ss.cell(r,2,'•').font=BLK; c=ss.cell(r,3,t); c.font=BOLD if 'THEATRE' in t else BLK; c.alignment=wrap()
    ss.merge_cells(start_row=r,start_column=3,end_row=r,end_column=7)
    ss.row_dimensions[r].height=max(14,12.5*(len(t)//105+1)); r+=1
SUMMARY_TOT=TOT
wb.save('165_Randolph_Cost_To_Open.xlsx')
print('core sheets built. LAST line row =',LAST,' TOT row =',TOT)

# ============================================================ LEASE OR FINANCE
lf=wb.create_sheet('Lease or Finance')
for col,w in zip('ABCDEFGH',[3,40,17,15,17,13,13,74]): lf.column_dimensions[col].width=w
r=2
lf[f'B{r}']='EQUIPMENT FINANCING — OPTIONAL, REFERENCE ONLY'; lf[f'B{r}'].font=H1; r+=1
lf[f'B{r}']='Kit in the Line Build that does not have to be bought outright. Nothing here changes the build cost — it changes WHEN you pay. Property-lease and landlord matters are deliberately excluded.'; lf[f'B{r}'].font=SM; r+=2
lf[f'B{r}']='FINANCING ASSUMPTIONS  —  edit the yellow cells'; lf[f'B{r}'].font=H2; r+=1
LA=r
for lab,val,fmt,note in [('Equipment lease rate, annual',0.09,PCT,'Typical for AV/production gear on a 5-year lease with a $1 buyout.'),
                         ('Equipment lease term, years',5,'#,##0','Own the asset at the end.'),
                         ('Events per year (for rental comparisons)',85,'#,##0','Used only to convert per-event rental into an annual figure.')]:
    lf.cell(r,2,lab).font=BLK
    c=lf.cell(r,3,val); c.font=BLUE; c.fill=YEL; c.border=BOX; c.number_format=fmt
    lf.cell(r,8,note).font=SM; lf.cell(r,8).alignment=wrap(); r+=1
RATE_R,TERM_R,EV_R=LA,LA+1,LA+2
r+=1
lf.cell(r,2,'FOUR MECHANISMS').font=H2; r+=1
for m,d in [('Equipment lease','Fixed term, you own it at the end. Cheapest way to defer real CapEx. Best for audio, lighting, HVAC plant.'),
            ('Event rental','Pay per show. Flexible, no commitment, and by far the most expensive per year if you use it often.'),
            ('Vendor-supplied','A supplier funds the kit in exchange for exclusivity or volume. Zero CapEx, zero lease — costs margin instead.'),
            ('Third-party operator','Someone else builds and runs the scope. Removes it from the budget entirely; you take rent or a percentage.')]:
    lf.cell(r,2,'  '+m).font=BOLD; lf.cell(r,3,d).font=BLK; lf.cell(r,3).alignment=wrap()
    lf.merge_cells(start_row=r,start_column=3,end_row=r,end_column=8); r+=1
r+=1
hdr=['Item','CapEx if bought','Mechanism','Annual cost\nif not bought','Term','Own at\nend?','Verdict / what it costs you']
for i,h in enumerate(hdr,2):
    c=lf.cell(r,i,h); c.font=WHT; c.fill=HDR; c.alignment=Alignment(horizontal='center',vertical='center',wrap_text=True)
lf.row_dimensions[r].height=30; r+=1
LS=r
LEASE=[
 ('House audio system (L-Acoustics)',2_200_000,'Equipment lease','LEASE',5,'Yes','MT I301. Payback on buying vs event rental is 2-7 months, so DO NOT event-rent it long term. A 5-year lease keeps the asset and defers the cash.'),
 ('Performance lighting rig',850_000,'Equipment lease','LEASE',5,'Yes','MT I61/I305. Same logic as audio. Lease rather than rent show by show.'),
 ('LED video walls (upstage + overhead)',1_500_000,'Event rental','RENT',0,'No','Already Tier 2. Rent per show until the calendar proves the spend. Genuinely the right one to rent — spec moves fast and it dates quickly.'),
 ('Displays & distribution',200_000,'Event rental','RENT',0,'No','MT I294: "We can do any display or distribution by renting." Agreed.'),
 ('HVAC plant — chillers / air handling',5_300_000,'Equipment lease','LEASE',7,'Yes','The largest single leasable item in the build. Energy-as-a-Service and equipment leasing are both routine for plant this size. Check NYSERDA and Con Ed C&I incentives before signing anything.'),
 ('POS terminals (76)',228_000,'Vendor-supplied','VENDOR',0,'No','MT I50: "I can get someone to give it to us for free for using the venue." Standard deal — take it.'),
 ('Ice machines & walk-in coolers',90_000,'Vendor-supplied','VENDOR',0,'No','Beverage distributors routinely supply coolers, draft systems and ice against a pouring agreement.'),
 ('Bar equipment — draft systems portion',200_000,'Vendor-supplied','VENDOR',0,'No','Same pouring-rights mechanism. Negotiate before the equipment package is bought out.'),
 ('Kitchen equipment + kitchen roughing',215_000,'Third-party operator',"OPERATOR",0,'No','MT I49/I154: outsource the kitchen. The operator funds their own equipment. Removes the scope AND the $135k of plumbing roughing.'),
 ('Restaurant fit-out & furniture',70_000,'Third-party operator','OPERATOR',0,'No','Goes with the kitchen. 769 covers becomes their capital, not ours.'),
 ('Theatre GA seating (3,714 chairs)',92_850,'Event rental','RENT',0,'No','Only needed for seated configurations. Rent per seated show rather than storing 3,714 chairs.'),
 ('Fork lift & scissor lift',60_000,'Event rental','RENT',0,'No','Already cut per MT I275. Rent for load-ins.'),
]
for nm,capex,mech,kind,term,own,note in LEASE:
    lf.cell(r,2,nm).font=BLK
    c=lf.cell(r,3,capex); c.number_format=CUR; c.font=BLUE
    lf.cell(r,4,mech).font=BLK; lf.cell(r,4).alignment=Alignment(horizontal='center')
    if kind=='LEASE':
        f=(f'=C{r}*$C${RATE_R}/(1-(1+$C${RATE_R})^-{term})')
        lf.cell(r,6,term).alignment=Alignment(horizontal='center')
    elif kind=='RENT':
        f=f'=C{r}*0.35'   # event-rental rule of thumb: ~35% of purchase price per year of regular use
        lf.cell(r,6,'—').alignment=Alignment(horizontal='center')
    else:
        f='=0'
        lf.cell(r,6,'—').alignment=Alignment(horizontal='center')
    c=lf.cell(r,5,f); c.number_format=CUR; c.font=BLK
    lf.cell(r,7,own).alignment=Alignment(horizontal='center'); lf.cell(r,7).font=BLK
    lf.cell(r,8,note).font=SM; lf.cell(r,8).alignment=wrap()
    for i in range(2,9): lf.cell(r,i).border=BOX
    r+=1
LE=r-1
lf.cell(r,2,'TOTAL equipment CapEx that can be financed rather than bought').font=BOLD; lf.cell(r,2).border=TOPB
c=lf.cell(r,3,f'=SUM(C{LS}:C{LE})'); c.font=BOLD; c.number_format=CUR; c.border=TOPB
c=lf.cell(r,5,f'=SUM(E{LS}:E{LE})'); c.font=BOLD; c.number_format=CUR; c.border=TOPB
lf.cell(r,8,'Annual figure is what you pay instead. Leased items you still own at the end of the term.').font=SM
lf.cell(r,8).alignment=wrap(); lf.cell(r,8).border=TOPB
for i in (4,6,7): lf.cell(r,i).border=TOPB
TL=r; r+=2
lf.cell(r,2,'READ THIS FIRST')  # noqa
lf.cell(r,2,'READ THIS FIRST').font=RED; r+=1
for t in ['Financing does not make the building cheaper — it makes it cheaper TO START. Total cost over the life of the kit is higher than buying, always.',
          'Vendor-supplied kit is paid for in margin, not cash. A pouring agreement that funds coolers and draft systems has a price per keg attached — get that priced before signing.',
          'Rental figures use a 35%-of-purchase-price-per-year rule of thumb for regular use. For audio and lighting the Factory Town book shows the real number is far worse: buying pays back in 2-7 months, so lease those rather than renting them show by show.']:
    lf.cell(r,2,'•').font=BLK; lf.cell(r,3,t).font=BLK; lf.cell(r,3).alignment=wrap()
    lf.merge_cells(start_row=r,start_column=3,end_row=r,end_column=8)
    lf.row_dimensions[r].height=max(14,12.5*(len(t)//118+1)); r+=1

wb.save('165_Randolph_Cost_To_Open.xlsx')
print('lease sheet done, rows',LS,LE)

# ============================================================ COST-DOWN OPTIONS
cd_=wb.create_sheet('Cost-Down Options',2)
for col,w in zip('ABCDEFG',[3,42,15,15,13,13,78]): cd_.column_dimensions[col].width=w
r=2
cd_[f'B{r}']='HOW TO GET THE NUMBER DOWN'; cd_[f'B{r}'].font=H1; r+=1
cd_[f'B{r}']='Ranked by size. Everything here is a construction-cost lever — scope, procurement, delivery method or tax.'; cd_[f'B{r}'].font=SM; r+=2
for i,h in enumerate(['Lever','Saving (low)','Saving (high)','Certainty','Costs us','What it is and what it takes'],2):
    c=cd_.cell(r,i,h); c.font=WHT; c.fill=HDR; c.alignment=Alignment(horizontal='center',vertical='center',wrap_text=True)
cd_.row_dimensions[r].height=28; r+=1
CS=r
OPTS=[
 ('Correct the paver unit-price error',6_890_129,6_890_129,'Certain','Nothing',
  'CSI 075000 row 193: 1,592 SF at $3,312.50/SF where the lines above and below are $31/SF. Change one cell and the cascade through 9% OH&P, 10% contractor contingency and 10% owner contingency unwinds. This is not a saving so much as a correction — but it is the single largest number on this sheet and it costs nothing.'),
 ('Leave the roof at 20ft',15_500_000,19_000_000,'Certain','A lot',
  'The Tier R delta, all-in. Capacity is unaffected — 7,440 works at either height, it is driven by floor area and egress. What you lose is the production ceiling: no full concert lighting rig, no flown stage, no aerial, limited LED, worse HVAC at volume. It also removes the entire premium-positioning argument. Decide this one on strategy, not on cost.'),
 ('Competitively bid every trade package',1_600_000,3_200_000,'High','Time',
  'This is a Version 1 desktop estimate: Committed Costs $0, Invoices $0, Change Orders $0. Nothing has been bought. Three-bidding a $32M trade schedule in this market typically returns 5-10% against a first-pass estimate. Nothing else on this sheet is as reliable.'),
 ('NYC IDA / ICAP sales-tax exemption on materials',1_100_000,1_500_000,'Verify','Application',
  'NYC industrial and commercial incentive programmes can exempt construction materials from the 8.875% sales tax. On a $32M trade schedule with roughly 45% materials content that is ~$1.3M. Requires an IDA application and eligibility confirmation — start it before buyout, not after. VERIFY eligibility with counsel.'),
 ('Owner-furnish major equipment direct',900_000,1_400_000,'High','Coordination',
  'Buying switchgear, HVAC plant, elevators and production systems direct avoids the 9% OH&P and 10% contractor contingency stacked on them inside the trade schedule — roughly 20% on ~$6M of equipment. You take the delivery and warranty risk in exchange.'),
 ('Early buyout of steel and switchgear',800_000,1_600_000,'High','Cash earlier',
  'Locks the two longest-lead, most escalation-exposed packages against the 10% escalation assumption. Con Ed switchgear lead times are also the single biggest schedule risk in the job, so this buys programme as well as price.'),
 ('Open-book GMP with shared savings',600_000,1_300_000,'Medium','Negotiation',
  'The filed structure is a fixed 9% overhead, profit and insurance plus a 10% contractor contingency the contractor keeps. An open-book GMP with a shared-savings split returns unspent contingency instead of leaving it on the table. Typically worth 2-4% of trade cost.'),
 ('Re-use the existing roof and electrical service',600_000,2_500_000,'Verify','Nothing',
  'The structural and MEP assessment is still PENDING. If the precast roof is sound and the existing service can be uprated rather than replaced, the 74,000 SF roof demo ($1.11M) and part of the $1.4M Con Ed scope come out. This is the highest-value item on the pending due-diligence list — get the assessment done before buyout.'),
 ('Outsource the kitchen and restaurant',400_000,600_000,'High','Margin share',
  'MT I49 and I154. Removes the kitchen equipment, the $135k of kitchen plumbing roughing, the gas run, hood fire suppression, grease waste and the restaurant furniture. The operator funds their own fit-out. Bars stay ours either way.'),
 ('NYSERDA and Con Ed C&I incentives',200_000,600_000,'Verify','Application',
  'HVAC plant and lighting on a build this size normally qualifies for New York State and utility efficiency incentives. Has to be applied for during design, not after installation. VERIFY current programme availability.'),
 ('Cut architectural lighting to a defensible number',1_000_000,1_000_000,'High','Kerb appeal',
  'MT H313. A single unsupported $1,750,000 lump at 3.4x the performance-lighting budget. Take it to ~$750k and move some of it to production lighting where it earns.'),
 ('Stop taking contingency on contingency',220_000,220_000,'Certain','Nothing',
  'The 10% owner contingency is calculated on a subtotal that already contains the contractor 10%. Base the owner contingency on the pre-contractor-contingency figure instead.'),
 ('Phased Certificate of Occupancy',0,0,'Medium','Programme risk',
  'Open the main hall and complete the mezzanine, roof decks and VIP later. Defers rather than saves — and doing finish work in a live venue costs a premium (see Phase 2 Add-Backs). Use it for cash timing, not for savings.'),
]
for nm,lo,hi,cert,cost,desc in OPTS:
    cd_.cell(r,2,nm).font=BOLD
    for col,v in ((3,lo),(4,hi)):
        c=cd_.cell(r,col,v); c.number_format=CUR; c.font=BLUE
    c=cd_.cell(r,5,cert); c.alignment=Alignment(horizontal='center')
    c.font=Font(name=F,size=10,bold=True,color={'Certain':'008000','High':'1F3864','Medium':'8A5D00','Verify':'C00000'}[cert])
    cd_.cell(r,6,cost).font=BLK; cd_.cell(r,6).alignment=Alignment(horizontal='center')
    cd_.cell(r,7,desc).font=SM; cd_.cell(r,7).alignment=wrap()
    for i in range(2,8): cd_.cell(r,i).border=BOX
    r+=1
CE=r-1
cd_.cell(r,2,'TOTAL — every lever taken').font=BOLD; cd_.cell(r,2).border=TOPB
for col in (3,4):
    cl=get_column_letter(col); c=cd_.cell(r,col,f'=SUM({cl}{CS}:{cl}{CE})')
    c.font=BOLD; c.number_format=CUR; c.border=TOPB
for i in (5,6,7): cd_.cell(r,i).border=TOPB
cd_.cell(r,7,'Not additive in practice — the roof decision and the re-use decision overlap, and bidding may capture some of the same value as buyout.').font=SM
cd_.cell(r,7).alignment=wrap()
TCD=r; r+=1
cd_.cell(r,2,'Excluding the roof decision').font=BOLD
for col in (3,4):
    cl=get_column_letter(col); c=cd_.cell(r,col,f'={cl}{TCD}-{cl}{CS+1}')
    c.font=BOLD; c.number_format=CUR
cd_.cell(r,7,'What is available WITHOUT giving up the 50ft ceiling.').font=SM
r+=2
cd_.cell(r,2,'CERTAINTY KEY').font=H2; r+=1
for k,d in [('Certain','Arithmetic. The money is there the moment someone edits the cell or changes the calculation basis.'),
            ('High','Standard market practice on a job this size. Would be surprising not to achieve it.'),
            ('Medium','Achievable but depends on how the contract and programme are structured.'),
            ('Verify','Real money, but conditional on eligibility or on a survey that has not been done yet. Do not put these in a board number until confirmed.')]:
    cd_.cell(r,2,'  '+k).font=BOLD; cd_.cell(r,3,d).font=BLK; cd_.cell(r,3).alignment=wrap()
    cd_.merge_cells(start_row=r,start_column=3,end_row=r,end_column=7); r+=1

# ============================================================ PHASE 2 ADD-BACKS
p2=wb.create_sheet('Phase 2 Add-Backs',3)
for col,w in zip('ABCDEF',[3,44,16,16,14,80]): p2.column_dimensions[col].width=w
r=2
p2[f'B{r}']='WHAT THE EXTRAS COST'; p2[f'B{r}'].font=H1; r+=1
p2[f'B{r}']='Everything outside Scenario 2. Cost now, cost later, and the premium for doing it in a building that is already open.'; p2[f'B{r}'].font=SM; r+=2
for i,h in enumerate(['Item','Cost if built now','Cost if added later','Later premium','Why the premium, and what it buys'],2):
    c=p2.cell(r,i,h); c.font=WHT; c.fill=HDR; c.alignment=Alignment(horizontal='center',vertical='center',wrap_text=True)
p2.row_dimensions[r].height=28; r+=1
PS=r
ADD=[
 ('50ft roof raise — all Tier R scope',15_500_000,1.60,'Cannot realistically be done later at all. Raising a roof over a finished venue means gutting it: the room closes for a year, the rig and finishes come out, and every trade is re-mobilised. Treat this as now-or-never rather than as a phase.'),
 ('Roof terrace decks & membranes',512_128,1.35,'Structure and waterproofing are accessible now and awkward later. Crane access and roof loading are both easier before the building is occupied.'),
 ('Roof deck storefront & access doors',175_000,1.30,'Envelope penetrations in an operating building. Weather protection and out-of-hours working.'),
 ('LED video walls (upstage + overhead)',1_500_000,1.00,'No premium — genuinely modular. Rigging steel must be in from day one, but the walls themselves drop in whenever. This is the cleanest deferral in the whole budget.'),
 ('Displays & distribution',200_000,1.00,'No premium. Rentable per show in the meantime.'),
 ('Architectural & exterior lighting',750_000,1.20,'Exterior work needs access equipment and possibly a sidewalk shed again. Interior architectural lighting means working at height over a finished floor.'),
 ('Restaurant & kitchen fit-out',215_000,1.25,'If outsourced this becomes the operator\'s capital and the premium is theirs, not ours. Only relevant if we build it.'),
 ('Restaurant, VIP and roof furniture',290_000,1.00,'No premium. Furniture is furniture.'),
 ('Interior art, decor and murals',250_000,1.10,'MT I55: "Can be done after". Correct — and it works better once the room is finished and you can see what it needs.'),
 ('Theatre GA seating (3,714 chairs)',92_850,1.00,'No premium. Rent until seated shows justify buying.'),
 ('Parking garage',2_257_500,1.15,'Standalone off-site structure. Independent of the building programme — but confirm whose scope it is before pricing it at all.'),
]
for nm,now,mult,why in ADD:
    p2.cell(r,2,nm).font=BLK
    c=p2.cell(r,3,now); c.number_format=CUR; c.font=BLUE
    c=p2.cell(r,4,f'=C{r}*E{r}'); c.number_format=CUR; c.font=BLK
    c=p2.cell(r,5,mult); c.number_format='0.00"x"'; c.font=BLUE; c.alignment=Alignment(horizontal='center')
    p2.cell(r,6,why).font=SM; p2.cell(r,6).alignment=wrap()
    for i in range(2,7): p2.cell(r,i).border=BOX
    r+=1
PE=r-1
p2.cell(r,2,'TOTAL').font=BOLD; p2.cell(r,2).border=TOPB
for col in (3,4):
    cl=get_column_letter(col); c=p2.cell(r,col,f'=SUM({cl}{PS}:{cl}{PE})')
    c.font=BOLD; c.number_format=CUR; c.border=TOPB
c=p2.cell(r,5,f'=D{r}/C{r}'); c.number_format='0.00"x"'; c.font=BOLD; c.border=TOPB; c.alignment=Alignment(horizontal='center')
p2.cell(r,6,'Blended premium for deferring everything.').font=SM; p2.cell(r,6).border=TOPB
r+=2
p2.cell(r,2,'THE ONLY REAL DEADLINE').font=RED; r+=1
for t in ['Two things must be decided before construction starts and cannot be revisited: the roof height, and the rigging steel.',
          'Everything else on this sheet can wait. LED walls, displays, furniture, art, seating and the roof decks all carry little or no penalty for being added later — provided the STRUCTURE to hang and support them is built now. Steel is cheap while the building is open and ruinous afterwards.',
          'So the cost-down strategy is: build all the structure, defer all the finish and all the kit.']:
    p2.cell(r,2,'•').font=BLK; p2.cell(r,3,t).font=BLK; p2.cell(r,3).alignment=wrap()
    p2.merge_cells(start_row=r,start_column=3,end_row=r,end_column=6)
    p2.row_dimensions[r].height=max(14,12.5*(len(t)//120+1)); r+=1

wb.save('165_Randolph_Cost_To_Open.xlsx')
print('cost-down + phase2 done')

# ============================================================ FINDINGS
fd=wb.create_sheet('Findings')
for col,w in zip('ABCDEFG',[3,8,12,46,16,14,88]): fd.column_dimensions[col].width=w
r=2
fd[f'B{r}']='CONSTRUCTION FINDINGS REGISTER'; fd[f'B{r}'].font=H1; r+=1
fd[f'B{r}']='Every finding is sourced to a cell, quantity or unit price in the Master Development Budget. Revenue, operating and deal findings are excluded.'; fd[f'B{r}'].font=SM; r+=2
for i,h in enumerate(['ID','CSI / tab','Finding','Impact','Direction','Evidence'],2):
    c=fd.cell(r,i,h); c.font=WHT; c.fill=HDR; c.alignment=Alignment(horizontal='center',vertical='center',wrap_text=True)
fd.row_dimensions[r].height=26; r+=1
FS=r
FIND=[
 ('C-01','075000','Paver line priced at 107x its neighbours',-6_890_129,'Overstated','Row 193: 1,592 SF at $3,312.50/SF. Rows 192 and 194, same product, are $31/SF. $5,224,148 of trade cost, marked up through 9% OH&P, 10% contractor contingency and 10% owner contingency. Correct it and CSI 075000 falls from $5,736,276 to $512,128 — three terrace membranes and their pavers.'),
 ('C-02','055100 / 024100','The 50ft roof raise is quantified at zero',11_275_395,'Understated','Every related line carries a unit price and QTY 0: demo of elevated roof area $15/SF; excavation for new columns $6.50/SF "Based on Footprint of New Roof"; footings $7,500/EA; brick facade at music hall "BUMP UP" $35/SF; roof trusses, girders and columns $6,000/ton; roof deck $4/SF; temp roof $5/SF; fireproofing new roof steel $5/SF; furring at "BUMP UP" $20/SF. The soft-cost tab DOES fund 13 borings 50ft deep "required for ST permit".'),
 ('C-03','055100','Structural steel is $0 on an "Add Second Level" scope',3_400_000,'Understated','Mezzanine framing, upper balcony framing incl. balcony seating, stage lighting and AV support structure, stairs, railings, roof dunnage — all at $6,000/ton or $8/lb, all QTY 0. The FF&E schedule simultaneously buys 657 mezzanine box chairs.'),
 ('C-04','260000','Electrical has switchboards and temp power only',4_400_000,'Understated','$558,750 total = two 2,500A switchboards ($390k), temp light and power ($156,250), firestopping ($12,500). QTY 0 on: general power and devices, kitchen circuits, stage power, mechanical power, VAV and exhaust fan power, panels and secondary distribution, new CT cabinet and transformer switches, combine existing services. MT F41 asked whether stages can plug in here — they cannot.'),
 ('C-05','100500','Acoustic treatment is $0',2_000_000,'Understated','Acoustical panels at music hall walls $40/SF QTY 0; K13 at underside of mezzanine, music hall ceilings and VIP $12/SF QTY 0; acoustical doors $6,500 EA / $10,000 pair QTY 0. Soft-cost acoustical engineering is a single $15,000 line. MT G53 confirms $15-25k is right for the FEE — the treatment is the gap.'),
 ('C-06','FF&E 309','LED video walls are a note, not a number',1_500_000,'Understated','"Upstage Video Wall" carries the note "$1,400/SF" with no quantity and no total. "Overhead Video Wall" is blank. At $1,400/SF an 1,800 SF upstage wall is $2.52M. The underwriting raised its own lighting and video line to $1.5M explicitly for "expanded LED wall coverage".'),
 ('C-07','100','Escalation applied to the garage, left blank on the building',3_182_355,'Understated','Off-site: "Escalation (Calculated at 5%)" = $107,500. Building and Fit-Out: the same line exists and is BLANK. A single 5% pass on trade is ~$909k; compounding across a two-year build from 2027 is 10-15%.'),
 ('C-08','201 / 024100','Abatement is $8,750 on a 1948 building',1_000_000,'Understated','Soft cost 201: 350 units at $25. Demolition schedules "Demo Pre-cast concrete roof, 74,000 SF" marked "Abatement by others" — and that demo line itself carries no price. Total demolition for a decommissioned Caesarstone plant is $30,408. MT G32: "this is super low".'),
 ('C-09','210 / 260000','Con Ed fee is budgeted, the service upgrade is not',1_400_000,'Understated','Soft cost 210 note: "Service upgrade required. Vault located in street, new conduit and feeders from vault into MPOE electrical room. Only Con Ed costs carried." The physical work is QTY 0 in the trade schedule.'),
 ('C-10','various','Twelve further divisions at zero quantity',4_010_000,'Understated','Concrete, millwork, bar and kitchen plumbing roughing, doors and hardware, tile and flooring, scaffolding and hoarding, fireproofing, painting, storefront and glazing, specialties, rough carpentry, sitework. Each carries populated unit prices against QTY 0. MT F12 puts scaffolding alone at $1-2M.'),
 ('C-11','400','Contingency is stacked and thin',220_000,'Overstated','A 10% contractor contingency sits inside Building and Fit-Out; the 10% owner contingency is then taken on a subtotal that already includes it. Combined contingency is 14.3% of total against a 25-35% norm for a 1948 conversion at this design stage with this much scope unpriced.'),
 ('P-01','FF&E 302','F&B equipment 40% below our own Brooklyn Paramount build',990_000,'Understated','The sheet cites its own comp: "BPT: 26 POS / Prep Kitchen / 1 Walk-in Cooler $837K" = $32,192 per POS. 165 Randolph budgets $1,457,000 for 76 positions = $19,171 per POS. Kitchen equipment at $80,000 for 769 covers is the least credible line in the FF&E schedule.'),
 ('P-02','FF&E 310','Architectural lighting at 3.4x performance lighting',-1_000_000,'Overstated','$1,750,000 as a single lump, one line, no vendor, no detail — against $520,000 of performance lighting in a venue whose thesis is arena-grade production. MT H313: "??????????? Why spend so much on outside lighting". The only hard-cost line in the file that reads high.'),
 ('P-03','FF&E 309','Three different numbers for one audio system',800_000,'Understated','Dev budget $1,400,000 "Includes Theater / VIP / Restaurant & Roof Area". Underwriting $2,200,000 for the main room alone. The FF&E row\'s own benchmark note says $690k. Soft goods shows the same pattern: $200,000 budgeted against a $725,000 benchmark on the same row, with "CUTDOWN DRAPE @ MEZZ EDGE Not Included".'),
 ('P-04','000','Parking garage at $8,269 per space',0,'Discrepancy','$2,150,000 for 260 spaces. NYC structured parking is $25,000-50,000 per space — so either this is surface parking or the line is short by $4.3-10.8M. It appears in no sheet of the underwriting. MT I21: "Eric Paying for this????"'),
 ('P-05','100 / 213','General conditions and PM do not match a 24-month build',680_000,'Understated','Hidden GC tab totals $2,082,000 against $2,000,000 carried — an $82k break. Staff durations are inconsistent in the same sheet (60 units for PM, APM, engineer and three supers; 6 for exec, accountant and general super). The only duration in the file is 60 weeks of portable toilets, implying ~14 months. Owner PM is $520,000 = 1.2% of project against a 2-4% norm.'),
 ('P-06','230000 / 142000','Three lines where the contractor is right and the underwriting was light',-3_521_900,'Overstated','HVAC $5,300,000 vs $2,667,600 underwritten — the dev budget is correct for NYC assembly at 3.7M cu ft. Elevators $600,000 (2 cars x 4 stops) vs $200,000 for one 2-stop hydraulic. Plumbing 189 fixtures vs 100 assumed — the dev budget matches NYC code at 7,440. The underwriting was $3.5M short on these three.'),
 ('N-01','230000','No heating line exists at all',815_100,'Understated','MT F40: "Do we need heat?" Yes. HVAC is priced over 120,000 SF against a 135,953 SF building, and there is no heating scope whatsoever. The underwriting carries $815,100 for radiant tube on the correct reasoning that forced air fails at a 50ft ceiling.'),
 ('N-02','210000 / 283100','Fire protection and alarm priced over the wrong area',214_000,'Understated','Fire protection covers 122,300 SF and fire alarm 100,000 SF against a 135,953 SF building — short by 11% and 26% of area respectively. MT H429 asked about a double count between the Breakdown and Detail tabs: there is none, the two Breakdown lines sum exactly to the Detail tab\'s $400,000.'),
 ('R-01','basis','$313/SF and $607/SF describe the same building',0,'Discrepancy','Dev budget: $42,555,099 over 135,953 SF = $313/SF. Underwriting: $45,000,000 over 74,100 SF = $607/SF. Both correct, both will be read side by side. A reader who sees $313/SF against Brooklyn industrial comps of $394-554/SF concludes the build is cheap.'),
 ('R-02','reconciliation','27.3% of the underwriting CapEx was a plug',0,'Discrepancy','The underwriting CapEx tab states it: hard costs $24,103,600, directed base $40,000,000, and a reconciliation line of $12,280,860 described as "line items not yet priced". The $45M was a target, not an estimate. The development budget is the first genuine bottom-up.'),
 ('G-01','governance','The cost-control apparatus is an unwired template',0,'Discrepancy','Project At-a-Glance and Project Summary rollups are broken with #REF!. Cost Report Date reads 2023-01-31 and the contingency log is dated March 2020 — from the project this template was copied from. The Risk Report is empty with $0 exposure. Committed Costs, Invoices and Change Orders are all $0, so nothing has been bought and this is a desktop estimate, not a validated bottom-up.'),
]
for fid,csi,title,impact,direc,ev in FIND:
    fd.cell(r,2,fid).font=BOLD; fd.cell(r,2).alignment=Alignment(horizontal='center')
    fd.cell(r,3,csi).font=BLK; fd.cell(r,3).alignment=Alignment(horizontal='center')
    fd.cell(r,4,title).font=BLK; fd.cell(r,4).alignment=wrap()
    c=fd.cell(r,5,impact if impact else None); c.number_format=CUR
    c.font=Font(name=F,size=10,bold=True,color='C00000' if impact<0 else '1F3864')
    c=fd.cell(r,6,direc); c.alignment=Alignment(horizontal='center')
    c.font=Font(name=F,size=9,bold=True,color={'Overstated':'C00000','Understated':'1F3864','Discrepancy':'8A5D00'}[direc])
    fd.cell(r,7,ev).font=SM; fd.cell(r,7).alignment=wrap()
    for i in range(2,8): fd.cell(r,i).border=BOX
    r+=1
FE=r-1
fd.cell(r,4,'NET IMPACT vs the filed budget').font=BOLD; fd.cell(r,4).border=TOPB
c=fd.cell(r,5,f'=SUM(E{FS}:E{FE})'); c.font=BOLD; c.number_format=CUR; c.border=TOPB
for i in (2,3,6,7): fd.cell(r,i).border=TOPB
fd.cell(r,7,'Overstatements are negative, understatements positive. This is an indicative net, not the scenario total — see Scenario Summary for the modelled numbers.').font=SM
fd.cell(r,7).alignment=wrap()
fd.auto_filter.ref=f'B{FS-1}:G{FE}'

wb.save('165_Randolph_Cost_To_Open.xlsx')
print('findings done — sheets:',wb.sheetnames)
