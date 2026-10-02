"""Fail if any Serbian word in any sentence has no word card (parenthetical English notes are ignored)."""
import json, re, os, sys
os.chdir(os.path.join(os.path.dirname(__file__), '..'))
words = json.load(open('src/data/words.json')); d = json.load(open('src/data/entries.json'))
S = []
for e in d:
    S.append(e['serbian'])
    S += [x['serbian'] for x in e['examples']]
    for f in e.get('forms', []):
        S.append(f['serbian'])
        if 'example' in f: S.append(f['example']['serbian'])
    S += [a['serbian'] for a in e.get('alternatives', [])]
    S += [x for x in [e.get('ijekavian')] if x]
missing = {}
for s in S:
    s2 = re.sub(r'\([^)]*\)', ' ', s)
    for w in re.findall(r"l'|[^\W\d_]+", s2.lower()):
        if w not in words: missing.setdefault(w, s)
for w, s in sorted(missing.items()): print(w, '<-', s)
print(len(missing), 'words without a card')
sys.exit(1 if missing else 0)
