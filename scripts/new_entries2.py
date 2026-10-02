"""Content batch 2: ~125 new entries (batch2_a/b/c.py) plus cross-links. Idempotent (skips existing ids).
Run order: new_entries2.py -> (add glossary words) -> build_words.py -> check_words.py"""
import json, os, sys
os.chdir(os.path.join(os.path.dirname(__file__), '..')); sys.path.insert(0, 'scripts')
from remap import P
import batch2_a, batch2_b, batch2_c

NEW = batch2_a.NEW + batch2_b.NEW + batch2_c.NEW

# Extra homes for existing entries (an entry can sit in several subcategories).
EXTRA_PLACES = {
 'ucim-srpski': 'can', 'veceras': 'plans', 'kafic': 'plans', 'rakija': 'guest', 'koliko': 'num', 'brojevi': 'shop',
 'mozda': 'filler', 'sumnjam': 'opin', 'stvarno': 'ynm', 'racun': 'dating', 'kafa': 'plans', 'voda': 'rest',
 'dobar-dan': 'cfam', 'nema-veze': 'agree', 'ne-treba': 'formal',
}

if __name__ == '__main__':
    data = json.load(open('src/data/entries.json')); by = {e['id']: e for e in data}; added = []
    for e in NEW:
        if e['id'] in by: continue
        data.append(e); by[e['id']] = e; added.append(e['id'])
    new_ids = set(added)
    # drop related ids that don't exist, then link both ways
    for e in data:
        e['related'] = [r for r in e['related'] if r in by and r != e['id']]
    for i in added:
        for r in by[i]['related']:
            if i not in by[r]['related'] and len(by[r]['related']) < 8: by[r]['related'].append(i)
    for k, spec in EXTRA_PLACES.items():
        e = by[k]
        for c, s in P(spec):
            if not any(p['category'] == c and p['subcategory'] == s for p in e['placements']): e['placements'].append({'category': c, 'subcategory': s})
    json.dump(data, open('src/data/entries.json', 'w'), ensure_ascii=False, indent=2)
    open('src/data/entries.json', 'a').write('\n')
    print('added', len(added), 'total', len(data))
    # sanity: counts of examples, forms examples
    bad = [(e['id'], len(e['examples'])) for e in data if len(e['examples']) < 3]
    nof = [(e['id'], f['serbian']) for e in data for f in e.get('forms', []) if 'example' not in f]
    print('examples<3:', bad, 'forms without example:', nof)
