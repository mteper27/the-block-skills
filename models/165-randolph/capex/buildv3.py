# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
import v3, steel, takeoff as T, revised as V, sept16_raw as R
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

F='Arial'
BLK=Font(name=F,size=9); BOLD=Font(name=F,size=9,bold=True); BLUE=Font(name=F,size=9,color='0000FF')
RED=Font(name=F,size=9,bold=True,color='C00000'); GRN=Font(name=F,size=9,bold=True,color='1F6B3B')
H1=Font(name=F,size=18,bold=True,color='1F3864'); H2=Font(name=F,size=11,bold=True,color='1F3864')
WHT=Font(name=F,size=9,bold=True,color='FFFFFF'); SM=Font(name=F,size=8,color='595959')
BIG=Font(name=F,size=14,bold=True,color='1F3864'); DIVF=Font(name=F,size=11,bold=True,color='FFFFFF')
GRP=Font(name=F,size=9,bold=True,color='1F3864')
HDR=PatternFill('solid',fgColor='1F3864'); DVF=PatternFill('solid',fgColor='2E5C8A')
GPF=PatternFill('solid',fgColor='D9E2F3'); GRY=PatternFill('solid',fgColor='F2F2F2')
PNK=PatternFill('solid',fgColor='FCE4E4'); GRF=PatternFill('solid',fgColor='E2EFDA')
YEL=PatternFill('solid',fgColor='FFF2CC')
med=Side(style='medium',color='1F3864'); TOPB=Border(top=med)
CUR='$#,##0;($#,##0);"-"'
def wr(): return Alignment(wrap_text=True,vertical='top')
wb=Workbook()
def head(ws,sub):
    ws.cell(2,2,'165 RANDOLPH STREET').font=H1
    ws.cell(3,2,sub).font=H2
    ws.cell(4,2,'V3 — rebuilt on the measured structural takeoff · RFEM 6.15 export, '
                'model Rev 38, version VE1 · CONFIDENTIAL').font=SM
    return 6
def hrow(ws,r,cols):
    for i,h in enumerate(cols,2):
        c=ws.cell(r,i,h); c.font=WHT; c.fill=HDR
        c.alignment=Alignment(horizontal='center',vertical='center',wrap_text=True)
    return r+1

# ====================================================== 1. READ ME FIRST
ws=wb.active; ws.title='Read Me First'
for col,w in zip('ABCDE',[3,60,17,17,17]): ws.column_dimensions[col].width=w
r=head(ws,'THE TAKEOFF CHANGES THE ANSWER')
ws.cell(r,2,'We were $24.4M apart. We are now $649,727 apart.').font=BIG; r+=2
for t in [
 'The RFEM model measures 1,994,335 lb of new and replacement steel — 997.2 SHORT TONS. '
 'Priced by the ton, our structure goes from an estimated $9,258,304 to a measured '
 '$16,710,249, and our budget goes from $64,648,067 to $77,897,555.',
 '',
 'TWO OF MY 16 SEP FINDINGS ARE WRONG AND I AM WITHDRAWING THEM.',
 '     The model is NOT a roof lift. 62.4% of column steel starts at grade, all 517 truss '
 'members are new at +56.5 to +64.5 ft, the existing roof level carries zero members, and the '
 'words lift, jack, shore and splice appear nowhere in 8,658 rows. He and the structural '
 'engineer are building the same building; our lift assumption is the outlier.',
 '     His 135,953 SF is defensible. The model has 146,508 SF gross and 120,119 SF of enclosed '
 'floor. Our 14,000 SF mezzanine was an assumption; the model says 32,942 SF plus 13,077 SF of '
 'tiered seating plus a 26,389 SF occupied terrace.',
 '',
 'Strip those two and the correction I reported falls from $20,940,896 to $11,836,763. Apply '
 'only what still stands and his $89,084,591 becomes about $77,247,828 — against our V3 '
 'of $77,897,555. That is 0.8% apart.',
 '',
 'AND THE $12,000,000 PLUG IS NOW THE OTHER WAY ROUND. I told you it was right-sized. The '
 'measured structure alone is $16,710,249, of which $6,703,714 is bare steel by the ton, and '
 'his plug still has to cover all millwork, doors, storefront, glazing, tile, fireproofing and '
 'most of the drywall on top of that. When he prices it, his number goes UP.']:
    c=ws.cell(r,2,t); c.font=BOLD if t.startswith('TWO OF') else BLK; c.alignment=wr()
    ws.merge_cells(start_row=r,start_column=2,end_row=r,end_column=5)
    ws.row_dimensions[r].height=30 if len(t)>150 else (13 if t else 7); r+=1
r+=1
r=hrow(ws,r,['','V2 (estimated)','V3 (measured)','Delta'])
for lab,a,b in [('Trade cost',v3.V2_TRADE,v3.V3_TRADE),
                ('Escalation 10%',v3.V2_TRADE*.10,v3.V3_ESC),
                ('General conditions 8.5%',v3.V2_TRADE*.085,v3.V3_GC),
                ('Overhead, profit & insurance 9%',v3.V2_TRADE*.09,v3.V3_OHP),
                ('CONSTRUCTION COST',v3.V2_TRADE*1.275,v3.V3_CONSTR),
                ('Contingency',5_000_000.0,v3.V3_CONT),
                ('FF&E',5_588_260.0,v3.V3_FFE),
                ('Soft costs',5_398_000.0,v3.V3_SOFT),
                ('TOTAL DEVELOPMENT COST',v3.V2_TOTAL,v3.V3_TOTAL)]:
    tot=lab.startswith('TOTAL') or lab.startswith('CONSTRUCTION')
    c=ws.cell(r,2,lab); c.font=BOLD if tot else BLK
    for col,v in ((3,a),(4,b),(5,b-a)):
        c=ws.cell(r,col,v); c.number_format=CUR; c.font=BOLD if tot else BLK
    if tot:
        for col in range(2,6): ws.cell(r,col).fill=GPF if lab.startswith('TOTAL') else GRY; ws.cell(r,col).border=TOPB
    r+=1
r+=1
for lab,v in [('V3 $ per SF on 74,100 SF',v3.V3_TOTAL/74_100),
              ('V3 $ per SF on the measured 146,508 SF gross',v3.V3_TOTAL/V.GROSS_SF),
              ('Thomas, as sent',R.TOTAL),
              ('Thomas, after the corrections that SURVIVE the takeoff',89_084_591+V.NEW_CORRECTION),
              ('GAP to our V3',89_084_591+V.NEW_CORRECTION-v3.V3_TOTAL)]:
    ws.cell(r,2,lab).font=BLK
    c=ws.cell(r,3,v); c.number_format='$#,##0'; c.font=BOLD
    if lab.startswith('GAP'): c.fill=GRF
    r+=1

# ========================================================= 2. THE TAKEOFF
ws=wb.create_sheet('The Takeoff')
for col,w in zip('ABCDEFG',[3,40,14,14,14,12,60]): ws.column_dimensions[col].width=w
r=head(ws,'WHAT THE STRUCTURAL MODEL ACTUALLY MEASURES')
ws.cell(r,2,'UNITS. The source reports tonnes (2,204.62 lb). US steel is bought in SHORT TONS '
            '(2,000 lb). Everything here is short tons, converted from the lb column. Using '
            '904.62 where 997.17 belongs understates the steel by 10.2%.').font=SM
ws.cell(r,2).alignment=wr(); ws.merge_cells(start_row=r,start_column=2,end_row=r,end_column=7)
ws.row_dimensions[r].height=26; r+=2
ws.cell(r,2,'VALUE ENGINEERING: MODEL REV 43 → VE1').font=H2; r+=1
r=hrow(ws,r,['','Rev 43 (lb)','VE1 (lb)','Saved (lb)','VE1 tons','%'])
for n,a,b in T.VE_SAVING:
    ws.cell(r,2,n).font=BLK
    for col,v,f in ((3,a,'#,##0'),(4,b,'#,##0'),(5,a-b,'#,##0'),(6,b/2000,'#,##0.0')):
        c=ws.cell(r,col,v); c.number_format=f; c.font=BLK
    c=ws.cell(r,7,(a-b)/a if a else None); c.number_format='0.0%'; c.font=GRN if a>b else RED
    r+=1
ws.cell(r,2,'TOTAL NEW / REPLACEMENT STEEL').font=BOLD
for col,v,f in ((3,T.REV43_TOTAL_LB,'#,##0'),(4,T.VE1_TOTAL_LB,'#,##0'),
                (5,T.REV43_TOTAL_LB-T.VE1_TOTAL_LB,'#,##0'),(6,T.VE1_TOTAL_LB/2000,'#,##0.0')):
    c=ws.cell(r,col,v); c.number_format=f; c.font=BOLD; c.border=TOPB; c.fill=GPF
c=ws.cell(r,7,(T.REV43_TOTAL_LB-T.VE1_TOTAL_LB)/T.REV43_TOTAL_LB); c.number_format='0.0%'
c.font=BOLD; c.border=TOPB; c.fill=GPF
ws.cell(r,2).border=TOPB; ws.cell(r,2).fill=GPF; r+=2
ws.cell(r,2,'VE1 MEMBER DETAIL — 8,658 rows aggregated by system and section type').font=H2; r+=1
r=hrow(ws,r,['System','Section type','Members','LF','lb','Short tons'])
for s,k,n,lf,lb in T.MEMBERS:
    ws.cell(r,2,s).font=BLK; ws.cell(r,3,k).font=BLK
    for col,v,f in ((4,n,'#,##0'),(5,lf,'#,##0'),(6,lb,'#,##0'),(7,lb/2000,'#,##0.0')):
        c=ws.cell(r,col,v); c.number_format=f; c.font=BLK
    if 'Built-up' in k:
        for col in range(2,8): ws.cell(r,col).fill=YEL
    r+=1
r+=1
ws.cell(r,2,'The highlighted row is the one that breaks a $6,000/TON rate: 80 shop-welded plate '
            'girder columns, I 48/24 to I 69.023/24, 60.00 LF each on grids B and E.').font=SM
ws.cell(r,2).alignment=wr(); ws.merge_cells(start_row=r,start_column=2,end_row=r,end_column=7)
ws.row_dimensions[r].height=24; r+=2
ws.cell(r,2,'AREAS, COUNTS AND MASONRY').font=H2; r+=1
r=hrow(ws,r,['Scope','Unit','Rev 43','VE1','Change'])
for n,u,a,b in T.AREAS:
    ws.cell(r,2,n).font=BLK; ws.cell(r,3,u).font=BLK
    for col,v in ((4,a),(5,b),(6,b-a)):
        c=ws.cell(r,col,v); c.number_format='#,##0'; c.font=BLK
    r+=1

# ================================================== 3. LIFT OR REBUILD
ws=wb.create_sheet('Lift or Rebuild')
for col,w in zip('ABC',[3,34,118]): ws.column_dimensions[col].width=w
r=head(ws,'IS HE USING ROOF LIFTERS? NO. AND NEITHER IS THE STRUCTURAL ENGINEER.')
ws.cell(r,2,'Read off the member geometry, not off anybody’s description of it. Every '
            'number below is reproducible from the Member Detail sheet.').font=SM
r+=2
r=hrow(ws,r,['Test','What the model says'])
for k,vtext in T.METHOD:
    c=ws.cell(r,2,k); c.font=BOLD; c.alignment=wr()
    c=ws.cell(r,3,vtext); c.font=BLK; c.alignment=wr()
    ws.row_dimensions[r].height=max(34,10.5*(len(vtext)//118+1)); r+=1
r+=1
ws.cell(r,2,'WHAT THIS MEANS').font=H2; r+=1
for t in ['Thomas’s budget and the structural model agree with each other. Both demolish '
          'the existing roof and build new at height. His 74,000 SF of pre-cast roof demolition '
          'at $8/SF is not an error — it is the method.',
          'Our locked project facts say a roof lift is mandatory, carried at $3.5M for the '
          'lifter plus roughly $3.5M of surrounding work, and that the 50 ft clear height is '
          'the moat. The model builds to +64 ft 6 in by rebuilding instead.',
          'THIS IS THE DECISION THAT HAS TO BE MADE BEFORE ANYTHING ELSE RECONCILES. It moves '
          'concrete, steel, scaffolding, demolition, roofing, the DOB filing route and the '
          'programme. I have NOT changed the project facts file — that is your call, not '
          'mine, and it should be made with Wake and the structural engineer in the room.']:
    c=ws.cell(r,2,t); c.font=BOLD if t.startswith('THIS IS') else BLK; c.alignment=wr()
    ws.merge_cells(start_row=r,start_column=2,end_row=r,end_column=3)
    ws.row_dimensions[r].height=30; r+=1

# ================================================ 4. FINDINGS REVISED
ws=wb.create_sheet('Findings Revised')
for col,w in zip('ABCDEF',[3,40,60,74,50,16]): ws.column_dimensions[col].width=w
r=head(ws,'WHAT THE TAKEOFF CHANGES ABOUT THE 16 SEP AUDIT')
r+=1
r=hrow(ws,r,['Finding','What I said on 16 Sep','What the takeoff says','Verdict','$ withdrawn'])
for f,mine,tk,verdict,amt in V.REVISED:
    c=ws.cell(r,2,f); c.font=BOLD; c.alignment=wr()
    c=ws.cell(r,3,mine); c.font=SM; c.alignment=wr()
    c=ws.cell(r,4,tk); c.font=BLK; c.alignment=wr()
    c=ws.cell(r,5,verdict); c.alignment=wr()
    c.font=RED if verdict.startswith(('WITHDRAWN','REVERSED')) else (GRN if verdict.startswith('STANDS') else BOLD)
    c=ws.cell(r,6,-amt if amt else None); c.number_format=CUR; c.font=BOLD
    ws.row_dimensions[r].height=max(48,10.5*(max(len(tk)//74,len(mine)//60)+1)); r+=1
r+=1
for lab,v in [('Correction I reported on 16 Sep',V.OLD_CORRECTION),
              ('Withdrawn by the takeoff',-V.WITHDRAWN),
              ('CORRECTION THAT STILL STANDS',V.NEW_CORRECTION)]:
    c=ws.cell(r,2,lab); c.font=BOLD if lab.isupper() else BLK
    c=ws.cell(r,6,v); c.number_format=CUR; c.font=BOLD
    if lab.isupper():
        for col in (2,6): ws.cell(r,col).fill=GPF; ws.cell(r,col).border=TOPB
    r+=1

# =============================================== 5. V3 DETAILED BUDGET
ws=wb.create_sheet('V3 Detailed Budget')
for col,w in zip('ABCDEFG',[3,56,11,7,13,15,72]): ws.column_dimensions[col].width=w
r=head(ws,'V3 LINE SCHEDULE')
r=hrow(ws,r,['Item','Qty','Unit','Rate','Amount','Basis / source'])
for code,name,groups in v3.D3:
    ws.cell(r,2,f'{code}   {name}').font=DIVF
    for i in range(2,8): ws.cell(r,i).fill=DVF
    r+=1
    for gname,lines in groups:
        ws.cell(r,2,'   '+gname).font=GRP
        for i in range(2,8): ws.cell(r,i).fill=GPF
        r+=1
        for d,q,u,rate,src in lines:
            ws.cell(r,2,'      '+d).font=BLK; ws.cell(r,2).alignment=wr()
            c=ws.cell(r,3,q); c.number_format='#,##0'
            ws.cell(r,4,u).alignment=Alignment(horizontal='center')
            try: rr=float(rate)
            except (TypeError,ValueError): rr=25.0
            c=ws.cell(r,5,rr); c.number_format='$#,##0.00'; c.font=BLUE
            c=ws.cell(r,6,f'=C{r}*E{r}'); c.number_format=CUR
            c=ws.cell(r,7,src); c.font=SM; c.alignment=wr()
            if 'MEASURED' in src: ws.cell(r,3).fill=GRF
            ws.row_dimensions[r].height=max(13,10.5*(len(src)//72+1))
            r+=1

# ================================================== 6. V3 VS THOMAS
ws=wb.create_sheet('V3 vs Thomas')
for col,w in zip('ABCDE',[3,52,17,17,17]): ws.column_dimensions[col].width=w
r=head(ws,'WHERE WE LAND AGAINST HIM NOW')
r+=1
r=hrow(ws,r,['','Our V3','Thomas as sent','Delta'])
HIS_STRUCT = 0.0
for lab,a,b,note in [
 ('Primary structure — measured',v3.total([x for x in v3.D3 if x[0]=='100']),HIS_STRUCT,
  'His division 055100 is $0. All nineteen lines, zero quantity.'),
 ('His "Trade Costs To Be Priced" plug',0.0,R.TBP,
  'Covers our $16.7M of structure PLUS millwork, doors, glazing, tile, fireproofing and drywall.'),
 ('Everything else, trade cost',v3.V3_TRADE-v3.total([x for x in v3.D3 if x[0]=='100']),
  R.TRADE-3_034_000.0-60_000.0,'His trade less general-conditions content and preconstruction.'),
 ('TRADE COST',v3.V3_TRADE,R.TRADE+R.TBP-3_034_000.0-60_000.0,''),
 ('General conditions',v3.V3_GC,3_141_000.0+3_034_000.0,'Ours 8.5%. His staffing chart + div 013000.'),
 ('Escalation',v3.V3_ESC,0.0,'Blank in his file.'),
 ('Overhead, profit & insurance',v3.V3_OHP,R.OHP,''),
 ('Contractor contingency',0.0,R.CONTRCT,'We hold one contingency, below.'),
 ('Preconstruction',0.0,60_000.0,''),
 ('CONSTRUCTION COST',v3.V3_CONSTR,R.CONSTR,''),
 ('Contingency',v3.V3_CONT,R.CONTING,'His computes on the whole project. Still stands.'),
 ('Soft costs',v3.V3_SOFT,R.SOFT,''),
 ('FF&E',v3.V3_FFE,R.FFE,''),
 ('Off-site parking garage',0.0,R.OFFSITE,'We carry none.'),
 ('TOTAL',v3.V3_TOTAL,R.TOTAL,'')]:
    tot=lab.isupper()
    c=ws.cell(r,2,lab); c.font=BOLD if tot else BLK
    for col,v in ((3,a),(4,b),(5,b-a)):
        c=ws.cell(r,col,v); c.number_format=CUR; c.font=BOLD if tot else BLK
    if tot:
        for col in range(2,6): ws.cell(r,col).fill=GPF if lab=='TOTAL' else GRY; ws.cell(r,col).border=TOPB
    ws.cell(r,6,note).font=SM; ws.cell(r,6).alignment=wr()
    r+=1
ws.column_dimensions['F'].width=76
r+=2
ws.cell(r,2,'AND AFTER THE CORRECTIONS THAT SURVIVE THE TAKEOFF').font=H2; r+=1
for lab,v in [('Thomas as sent',R.TOTAL),
              ('Corrections that still stand',V.NEW_CORRECTION),
              ('Thomas, defensible',R.TOTAL+V.NEW_CORRECTION),
              ('Our V3, measured',v3.V3_TOTAL),
              ('GAP',R.TOTAL+V.NEW_CORRECTION-v3.V3_TOTAL)]:
    c=ws.cell(r,2,lab); c.font=BOLD if lab=='GAP' else BLK
    c=ws.cell(r,3,v); c.number_format=CUR; c.font=BOLD
    if lab=='GAP': c.fill=GRF; ws.cell(r,2).fill=GRF
    r+=1
ws.cell(r+1,2,'0.8% apart. The two budgets were never really in disagreement about the building '
              '— only about how much of it had been measured.').font=BOLD

for s in wb.worksheets:
    s.sheet_view.showGridLines=False; s.freeze_panes='A7'
wb.properties.title='165 Randolph V3 - Measured Takeoff'
wb.calculation.fullCalcOnLoad=True
OUT='165_Randolph_Capex_V3_Measured_Structural_Takeoff.xlsx'
wb.save(OUT); print('wrote',OUT)
