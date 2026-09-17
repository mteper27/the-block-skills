# -*- coding: utf-8 -*-
import re, html, subprocess, json, sys
sys.path.insert(0,'.'); import content as C

def inl(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'\*([^*]+)\*', r'<i>\1</i>', s)
    return s

def md_table(t):
    rows=[r.strip() for r in t.strip().split('\n') if r.strip() and not re.match(r'^\|\s*-', r)]
    out=['<table>']
    for i,r in enumerate(rows):
        cells=[c.strip() for c in r.strip('|').split('|')]
        tag='th' if i==0 else 'td'
        out.append('<tr>'+''.join(f'<{tag}>{inl(c)}</{tag}>' for c in cells)+'</tr>')
    return ''.join(out)+'</table>'

def para(p):
    return md_table(p) if p.strip().startswith('|') else f'<p>{inl(p)}</p>'

css = """
@page { size: letter; margin: 0.5in 0.55in; }
body { font-family: Arial, Helvetica, sans-serif; font-size: 9pt; color:#1a1a1a; line-height:1.22; }
h1 { font-size: 17pt; color:#1F3864; margin:0 0 2px 0; }
.sub { font-size: 10pt; color:#1F3864; margin:0 0 3px 0; }
.by { font-size: 8.5pt; color:#595959; margin:0 0 7px 0; border-bottom:1.5px solid #1F3864; padding-bottom:5px; }
h2 { font-size: 12.5pt; color:#1F3864; margin:0 0 4px 0; }
h3 { font-size: 9.4pt; color:#1F3864; margin:6px 0 2px 0; text-transform:uppercase; letter-spacing:.03em; }
.intro { font-size: 9pt; color:#444; margin:0 0 6px 0; }
table { border-collapse:collapse; width:100%; margin:0 0 6px 0; }
th { background:#1F3864; color:#fff; text-align:left; font-size:8.6pt; padding:3px 5px; }
td { border-bottom:1px solid #d9d9d9; padding:2px 5px; vertical-align:top; font-size:8.6pt; }
td.ref { width:14%; font-weight:bold; color:#1F3864; }
td.lab { width:31%; color:#444; font-style:italic; }
td.n { width:3%; font-weight:bold; color:#1F3864; }
td.who { width:14%; color:#444; }
code { font-family: Consolas, Menlo, monospace; font-size:8.6pt; background:#f2f2f2; padding:0 2px; }
p { margin:0 0 6px 0; }
.pb { page-break-after: always; }
.dont { background:#FCE4E4; padding:6px 8px; margin-top:8px; }
.dont h3 { margin-top:0; color:#C00000; }
.small { font-size:8.5pt; color:#595959; }\ntd.sec { background:#D9E2F3; color:#1F3864; font-weight:bold; font-size:8.6pt; text-transform:uppercase; letter-spacing:.03em; padding:2px 5px; }
"""
h=[f'<html><head><meta charset="utf-8"><title>{html.escape(C.TITLE)}</title><style>{css}</style></head><body>']
def header(kind):
    h.append(f'<h1>{html.escape(C.TITLE)}</h1><div class="sub">{html.escape(C.SUB)}</div><div class="by">{html.escape(C.BYLINE)} &nbsp;&middot;&nbsp; <b>{kind}</b></div>')

# PAGE 1
header('1 · QUESTIONS'); h.append(f'<p class="intro">{inl(C.Q_INTRO)}</p>')
h.append('<table><tr><th style="width:3%"></th><th style="width:14%">Cell / line</th><th style="width:31%">Your line reads</th><th>Question</th></tr>')
n=0
for sheet, qs in C.QUESTIONS:
    h.append(f'<tr><td colspan="4" class="sec">{html.escape(sheet)}</td></tr>')
    for ref, lab, q in qs:
        n+=1; h.append(f'<tr><td class="n">{n}</td><td class="ref">{inl(ref)}</td><td class="lab">{inl(lab)}</td><td>{inl(q)}</td></tr>')
h.append('</table><div class="pb"></div>')

# PAGE 2
header('2 · RECOMMENDATIONS — WHAT WE CAN DO TO CUT COSTS'); h.append(f'<p class="intro">{inl(C.R_INTRO)}</p>')
h.append('<table><tr><th style="width:3%"></th><th style="width:24%">Lever</th><th style="width:13%">Who</th><th>What and why</th></tr>')
for i,(lever,who,what) in enumerate(C.RECS,1):
    h.append(f'<tr><td class="n">{i}</td><td><b>{inl(lever)}</b></td><td class="who">{inl(who)}</td><td>{inl(what)}</td></tr>')
h.append('</table><div class="dont"><h3>Two things we do not want cut</h3>')
for k,v in C.R_DONT: h.append(f'<p><b>{inl(k)}.</b> {inl(v)}</p>')
h.append('</div><div class="pb"></div>')

# CLARIFICATION
header('3 · CLARIFICATION — THE REASONING BEHIND PAGES 1 AND 2')
for title, paras in C.CLAR:
    h.append(f'<h2>{inl(title)}</h2>' + ''.join(para(p) for p in paras))
h.append('</body></html>')
open('block.html','w',encoding='utf-8').write('\n'.join(h))

js = r"""
const { chromium } = require('/tmp/claude-0/-home-user/0521d668-0b2b-59fd-8f23-d788cbd0efd6/scratchpad/node_modules/playwright');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.PWEXE || undefined });
  const p = await b.newPage();
  await p.goto('file://' + process.cwd() + '/block.html', { waitUntil: 'load' });
  await p.pdf({ path: process.argv[2], format: 'Letter', printBackground: true, preferCSSPageSize: true });
  await b.close(); console.log('pdf ok');
})().catch(e => { console.error(e); process.exit(1); });
"""
open('topdf.js','w').write(js)
OUT='165_Randolph_The_BLOCK_Questions_Recommendations_Clarification.pdf'
r=subprocess.run(['node','topdf.js',OUT],capture_output=True,text=True)
print(r.stdout.strip() or r.stderr[-800:])
