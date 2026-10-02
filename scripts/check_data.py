"""Data integrity checks for src/data/entries.json. Exit 1 on any problem. Run after every content change:
  python3 scripts/check_data.py && python3 scripts/check_words.py"""
import json, os, re, sys, collections
os.chdir(os.path.join(os.path.dirname(__file__), '..'))
E = json.load(open('src/data/entries.json', encoding='utf8')); W = json.load(open('src/data/words.json', encoding='utf8'))
cats = open('src/lib/categories.js', encoding='utf8').read()
ids = [e['id'] for e in E]; S = set(ids); bad = []
def err(*a): bad.append(' '.join(map(str, a)))
for i, c in collections.Counter(ids).items():
    if c > 1: err('duplicate id', i)
for e in E:
    i = e['id']
    for r in e['related']:
        if r not in S: err(i, 'related id missing:', r)
        if r == i: err(i, 'relates to itself')
    if not e['related']: err(i, 'has no related entries')
    if len(e['examples']) < 3: err(i, 'fewer than 3 examples')
    for x in e['examples']:
        if not x.get('context'): err(i, 'example without context:', x['serbian'])
    for f in e.get('forms', []):
        if 'example' not in f: err(i, 'form without example:', f['serbian'])
    for p in e['placements']:
        if p['subcategory'] not in cats: err(i, 'unknown subcategory', p['subcategory'])
    if not e['pronunciation'].strip(): err(i, 'empty pronunciation')
    if re.search(r'tch|TCH|chh', e['pronunciation']): err(i, 'odd pronunciation spelling:', e['pronunciation'])
    fs = e.get('forms', [])
    for c, k in (('speaker', 'speaker'), ('describes', 'describes'), ('noun gender', 'nounGender')):
        if c in e['changesBy'] and not any(f.get(k) for f in fs): err(i, f'changesBy "{c}" but no form row tags {k}')
        if any(f.get(k) for f in fs) and c not in e['changesBy']: err(i, f'a form row tags {k} but changesBy lacks "{c}"')
    if e['register'] in ('slang', 'vulgar') and 'watchOut' not in e: err(i, 'slang/vulgar entry without watchOut')
for k, v in W.items():
    if v.get('entry') and v['entry'] not in S: err('word card', k, 'links to missing entry', v['entry'])
    if not v.get('pron') or not v.get('en') or not v.get('tags'): err('word card', k, 'incomplete')
for b in bad: print(b)
print(len(bad), 'problems;', len(E), 'entries;', len(W), 'word cards')
sys.exit(1 if bad else 0)
