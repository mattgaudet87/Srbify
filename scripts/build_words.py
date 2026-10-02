"""Build src/data/words.json from scripts/glossary/*.txt (meaning/notes written by hand), pronunciations
harvested from the app's own example sentences (scripts/extract_tokens.py), and entry links."""
import json, os, re, glob, subprocess, sys, unicodedata
root = os.path.join(os.path.dirname(__file__), '..'); os.chdir(root)
sys.path.insert(0, 'scripts')
tok = {k: {'pron': v} for k, v in json.load(open('scripts/glossary/pron.json')).items()}  # harvested by extract_tokens.py + ijekavian by hand
tok.update({k: {'pron': v} for k, v in json.load(open('scripts/glossary/pron_extra.json')).items()})  # words added in later batches
entries = json.load(open('src/data/entries.json'))

def norm(s):
    s = s.lower().replace('đ', 'dj')
    return re.sub(r'\s+', ' ', re.sub(r"[^\w' ]+", ' ', unicodedata.normalize('NFD', s).encode('ascii', 'ignore').decode())).strip()
def keyof(s): return re.sub(r'\s+', ' ', re.sub(r"[^\w' ]+", ' ', s.lower())).strip()

# entry links: exact match on the entry's own Serbian first, then its forms / alternatives
link = {}
for e in entries:
    for part in re.split(r'\s*/\s*', e['serbian']): link.setdefault(keyof(part), e['id'])
for e in entries:
    for f in e.get('forms', []): link.setdefault(keyof(f['serbian']), e['id'])
    for a in e.get('alternatives', []): link.setdefault(keyof(a['serbian']), e['id'])

words = {}
for p in sorted(glob.glob('scripts/glossary/*.txt')):
    for ln, line in enumerate(open(p, encoding='utf8'), 1):
        line = line.rstrip('\n')
        if not line.strip() or line.startswith('#'): continue
        parts = line.split('|')
        assert len(parts) == 4, f'{p}:{ln} {line}'
        k, en, note, tags = [x.strip() for x in parts]
        assert k not in words, f'dup {k}'
        w = {'en': en}
        if note: w['note'] = note
        w['tags'] = [t for t in tags.split(',') if t]
        words[k] = w

EXTRA_PRON = {'nzm': 'en-zeh-EM', "l'": 'leh'}
for k, w in words.items():
    if ' ' in k:  # chunk: join each word's pronunciation
        ps = [(tok.get(x) or {}).get('pron') for x in k.split()] if tok else None
        w['pron'] = ' '.join(p for p in ps) if ps and all(ps) else None
    else:
        w['pron'] = EXTRA_PRON.get(k) or ((tok.get(k) or {}).get('pron') if tok else None)
    if keyof(k) in link: w['entry'] = link[keyof(k)]
words["l'"] = {'en': 'short for "li" (question marker)', 'note': 'Spoken short form: "Je l\' si gladna?" = "Jesi li gladna?"', 'tags': ['particle', 'casual'], 'pron': 'leh'}
words['nzm'] = {'en': "I don't know; idk", 'note': 'Text abbreviation for "ne znam"', 'tags': ['interj', 'slang'], 'pron': 'en-zeh-EM', 'entry': link.get('ne znam') or 'nzm'}
missing = [k for k, w in words.items() if not w.get('pron')]
print(len(words), 'words; missing pron:', missing)
json.dump(dict(sorted(words.items())), open('src/data/words.json', 'w'), ensure_ascii=False, indent=0)
