"""Helper for content scripts: add_words([(word, meaning, note, 'tags,comma', pron), ...]) appends cards to
scripts/glossary/sweep.txt and pronunciations to pron_extra.json. Skips words that already have a card."""
import glob, json, os
os.chdir(os.path.join(os.path.dirname(__file__), '..'))
def add_words(rows):
    have = set()
    for p in glob.glob('scripts/glossary/*.txt'):
        for ln in open(p, encoding='utf8'):
            if '|' in ln and not ln.startswith('#'): have.add(ln.split('|')[0].strip())
    pron = json.load(open('scripts/glossary/pron_extra.json', encoding='utf8'))
    added = 0
    with open('scripts/glossary/sweep.txt', 'a', encoding='utf8') as f:
        for k, en, note, tags, pr in rows:
            if k in have: continue
            f.write(f'{k}|{en}|{note}|{tags}\n'); pron.setdefault(k, pr); have.add(k); added += 1
    json.dump(dict(sorted(pron.items())), open('scripts/glossary/pron_extra.json', 'w', encoding='utf8'), ensure_ascii=False)
    return added
if __name__ == '__main__':
    print(add_words([
        ('najverovatnije', 'most likely', 'Stronger than "verovatno"', 'adv', 'nai-veh-ROH-vaht-nee-yeh'),
        ('sasvim', 'completely; quite', '"Sasvim sigurno" = absolutely sure', 'adv', 'SAHS-veem'),
        ('sigurna', 'sure (feminine)', 'Masculine: siguran', 'adj,fem', 'SEE-goor-nah'),
    ]))
