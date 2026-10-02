import json,re,os,collections
os.chdir(os.path.join(os.path.dirname(__file__),'..'))
d=json.load(open('src/data/entries.json'))
pairs=[]  # (serbian, pron, english)
for e in d:
    pairs.append((e['serbian'],e['pronunciation'],e['english']))
    for x in e['examples']: pairs.append((x['serbian'],x['pronunciation'],x['english']))
    for f in e.get('forms',[]):
        pairs.append((f['serbian'],f['pronunciation'],f['useWhen']))
        if 'example' in f: pairs.append((f['example']['serbian'],f['example']['pronunciation'],f['example']['english']))
    for a in e.get('alternatives',[]): pairs.append((a['serbian'],a['pronunciation'],a['nuance']))
W=re.compile(r"[\wčćžšđČĆŽŠĐ]+(?:'[\wčćžšđ]+)?")
pron=collections.defaultdict(collections.Counter); ctx={}; miss=collections.Counter()
for sr,pr,en in pairs:
    ws=W.findall(sr); ps=[p.strip('.,?!…;:"“”') for p in pr.split()]
    ps=[p for p in ps if p and p not in '/—-']
    if len(ws)==len(ps):
        for w,p in zip(ws,ps): pron[w.lower()][p]+=1
    else:
        for w in ws: miss[w.lower()]+=1
    for w in ws: ctx.setdefault(w.lower(),(sr,en))
out={}
for w in sorted(ctx):
    out[w]={'pron':pron[w].most_common(1)[0][0] if pron[w] else None,'ctx':ctx[w]}
json.dump(out,open(os.environ.get('OUT','/tmp/tokens.json'),'w'),ensure_ascii=False,indent=0)
print(len(out),sum(1 for v in out.values() if not v['pron']))
