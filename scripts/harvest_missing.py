"""List words that have no card yet, with a pronunciation harvested from the sentence they appear in
(only when the sentence and its pronunciation have the same number of words)."""
import json, os, re, sys
os.chdir(os.path.join(os.path.dirname(__file__), '..'))
W = json.load(open('src/data/words.json', encoding='utf8')); D = json.load(open('src/data/entries.json', encoding='utf8'))
TOK = re.compile(r"[^\W\d_]+", re.U)
def pairs(e):
    yield e['serbian'], e['pronunciation']
    for x in e['examples']: yield x['serbian'], x['pronunciation']
    for f in e.get('forms', []):
        yield f['serbian'], f['pronunciation']
        if 'example' in f: yield f['example']['serbian'], f['example']['pronunciation']
    for a in e.get('alternatives', []): yield a['serbian'], a['pronunciation']
out = {}
for e in D:
    for sr, pr in pairs(e):
        s2 = re.sub(r'\([^)]*\)', ' ', sr); ws = TOK.findall(s2); ps = [p.strip('.,?!…;:"“”\'') for p in re.split(r'[\s/]+', pr) if p.strip('/ ')]
        ps = [p for p in ps if p]
        for i, w in enumerate(ws):
            k = w.lower()
            if k in W or k in out and out[k][0]: continue
            out[k] = (ps[i] if len(ws) == len(ps) else None, sr)
bad = {k: v for k, v in out.items() if not v[0]}
for k, (p, sr) in sorted(out.items()): print(f'{k}\t{p}\t{sr}')
print(len(out), 'missing,', len(bad), 'without harvested pronunciation', file=sys.stderr)
