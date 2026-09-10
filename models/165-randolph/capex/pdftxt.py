#!/usr/bin/env python3
"""Minimal PDF text extractor: inflate content streams, pull text-showing operators."""
import re,sys,zlib
def extract(path):
    d=open(path,'rb').read()
    out=[]
    for m in re.finditer(rb'stream\r?\n',d):
        s=m.end()
        e=d.find(b'endstream',s)
        if e<0: continue
        raw=d[s:e]
        try: data=zlib.decompress(raw)
        except Exception:
            try: data=zlib.decompressobj().decompress(raw)
            except Exception: continue
        if b'Tj' not in data and b'TJ' not in data: continue
        buf=[]
        # (text) Tj   and   [(a)-1(b)] TJ
        for t in re.finditer(rb'\((?:\\.|[^\\()])*\)|\bTJ\b|\bTj\b|\bTd\b|\bTD\b|\bT\*\b|\bET\b',data):
            tok=t.group(0)
            if tok.startswith(b'('):
                v=tok[1:-1]
                v=re.sub(rb'\\([()\\])',rb'\1',v)
                v=v.replace(b'\\n',b' ').replace(b'\\r',b' ').replace(b'\\t',b' ')
                buf.append(v)
            elif tok in (b'Td',b'TD',b'T*',b'ET'):
                buf.append(b'\n')
        txt=b''.join(buf).decode('latin-1')
        txt=re.sub(r'[ \t]+',' ',txt)
        txt='\n'.join(l.strip() for l in txt.split('\n') if l.strip())
        if txt: out.append(txt)
    return '\n'.join(out)
if __name__=='__main__':
    for p in sys.argv[1:]:
        t=extract(p)
        print(f"\n{'='*90}\n### {p}  ({len(t)} chars)\n{'='*90}")
        print(t if t else "[NO EXTRACTABLE TEXT — scanned image or vector-only drawing]")
