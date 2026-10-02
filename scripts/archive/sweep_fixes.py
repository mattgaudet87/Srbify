"""One-off Sweep fixes (B1-B5, B9) applied to src/data/entries.json in place. Idempotent: safe to re-run."""
import json, os, re
os.chdir(os.path.join(os.path.dirname(__file__), '..'))
P = 'src/data/entries.json'

# --- B3: pronunciation respellings (plain-text, so they also hit forms and examples) ---
text = open(P, encoding='utf8').read()
for a, b in [('NOHTCH', 'NOHCH'), ('SRETCH-', 'SREHCH-'), ('NEH-mo-goochh', 'NEH-mo-gooch'), ('PREE-yah-telyh', 'PREE-yah-tel')]:
    text = text.replace(a, b)
open(P, 'w', encoding='utf8').write(text)
pr = 'scripts/glossary/pron.json'
t = open(pr, encoding='utf8').read()
for a, b in [('NOHTCH', 'NOHCH'), ('SRETCH-', 'SREHCH-'), ('"EE-dem"', '"EE-dehm"')]:
    t = t.replace(a, b)
open(pr, 'w', encoding='utf8').write(t)

data = json.load(open(P, encoding='utf8'))
by = {e['id']: e for e in data}
def X(ctx, sr, pron, en): return {'serbian': sr, 'pronunciation': pron, 'english': en, 'context': ctx}

# --- B1: "Are you hungry?" leads with the form for her ---
e = by['jesi-li-gladna']
e['serbian'], e['pronunciation'] = 'Jesi li gladna?', 'YEH-see lee GLAHD-nah'
if not any(a['serbian'] == 'Jesi li gladan?' for a in e['alternatives']):
    e['alternatives'].insert(0, {'serbian': 'Jesi li gladan?', 'pronunciation': 'YEH-see lee GLAH-dahn', 'nuance': 'The same question to a man'})

# --- B2: split "Sigurno / Verovatno" into two entries ---
if 'verovatno' not in by:
    s = by['sigurno']
    s.update({
        'english': 'Definitely / for sure', 'serbian': 'Sigurno', 'pronunciation': 'SEE-goor-no',
        'meaning': 'Surely, for sure, definitely', 'tags': ['sure', 'certain', 'definitely'],
        'related': ['verovatno', 'mozda', 'naravno', 'sumnjam'],
        'alternatives': [
            {'serbian': 'Svakako', 'pronunciation': 'SVAH-kah-ko', 'nuance': 'Certainly; a touch more formal'},
            {'serbian': 'Sasvim sigurno', 'pronunciation': 'sahs-VEEM SEE-goor-no', 'nuance': 'Absolutely sure'},
        ],
        'examples': [
            X('To her', 'Sigurno ću doći', 'SEE-goor-no choo DOH-chee', "I'll definitely come"),
            X('Asking her', 'Jesi li sigurna?', 'YEH-see lee SEE-goor-nah', 'Are you sure?'),
            X('About me', 'Nisam siguran', 'NEE-sahm SEE-goo-rahn', "I'm not sure (a man says this)"),
            X('About me (her)', 'Nisam sigurna', 'NEE-sahm SEE-goor-nah', "I'm not sure (a woman says this)"),
            X('About him', 'Sigurno je kod kuće', 'SEE-goor-no yeh kohd KOO-cheh', "He's definitely at home"),
            X('About us', 'Sigurno ćemo stići na vreme', 'SEE-goor-no CHEH-mo STEE-chee nah VREH-meh', "We'll definitely get there on time"),
        ],
        'texting': 'sigurno',
    })
    s.pop('forms', None); s.pop('ijekavian', None)
    s['placements'] = [{'category': 'Quick phrases', 'subcategory': 'Yes, no, maybe'}, {'category': 'Quick phrases', 'subcategory': 'Agree and disagree'}]
    s['changesBy'] = []
    s['watchOut'] = '"Sigurno" is a firm yes. If you only lean yes, use "verovatno" (probably).'
    data.append({
        'id': 'verovatno', 'english': 'Probably', 'serbian': 'Verovatno', 'pronunciation': 'veh-ROH-vaht-no',
        'meaning': 'Probably, most likely', 'category': 'Quick phrases', 'subcategory': 'Yes, no, maybe',
        'tags': ['maybe', 'probably', 'likely'], 'register': 'neutral', 'changesBy': [],
        'alternatives': [
            {'serbian': 'Najverovatnije', 'pronunciation': 'nai-veh-ROH-vaht-nee-yeh', 'nuance': 'Most likely; stronger'},
            {'serbian': 'Možda', 'pronunciation': 'MOHZH-dah', 'nuance': 'Maybe; closer to 50/50'},
        ],
        'examples': [
            X('About me', 'Verovatno kasnim', 'veh-ROH-vaht-no KAHS-neem', "I'll probably be late"),
            X('To her', 'Verovatno si umorna', 'veh-ROH-vaht-no see OO-mor-nah', "You're probably tired"),
            X('About her', 'Verovatno je u gradu', 'veh-ROH-vaht-no yeh oo GRAH-doo', "She's probably in town"),
            X('About us', 'Verovatno ćemo ići', 'veh-ROH-vaht-no CHEH-mo EE-chee', "We'll probably go"),
        ],
        'texting': 'verovatno', 'related': ['sigurno', 'mozda', 'sumnjam'], 'verified': False,
        'ijekavian': 'Vjerovatno',
        'watchOut': '"Verovatno" leans yes (about 70%). "Možda" is closer to 50/50.',
        'placements': [{'category': 'Quick phrases', 'subcategory': 'Yes, no, maybe'}, {'category': 'Quick phrases', 'subcategory': 'Common replies'}],
    })
    for i in ('mozda', 'sumnjam'):
        if 'verovatno' not in by[i]['related']: by[i]['related'].append('verovatno')

# --- B4 / B9 ---
by['dying-laughing']['texting'] = 'umirem / crkoh'
WATCH = {
    'lova': 'Street slang. Fine with friends; with strangers or at work say "novac" or "pare".',
    'tip': '"Tip" also just means "type" or "kind". As slang for a guy it can sound dismissive, so say "momak" or "čovek" to stay neutral.',
    'maler': 'Always said lightly. For something actually serious, say "greška" (mistake) or "problem".',
}
for k, w in WATCH.items(): by[k].setdefault('watchOut', w)

# --- B5 / C3: changesBy follows the forms table ---
FORM_KEYS = {'speaker': 'speaker', 'describes': 'describes', 'nounGender': 'noun gender', 'region': 'region'}
for e in data:
    fs = e.get('forms', [])
    derived = {v for k, v in FORM_KEYS.items() if any(f.get(k) for f in fs)}
    if any(f.get('formal') and f['formal'] != 'casual' for f in fs): derived.add('formal')
    old = list(e['changesBy'])
    polite_alt = any(re.search(r'polite|formal', a.get('nuance', ''), re.I) for a in e.get('alternatives', []))
    keep = [c for c in old if c not in FORM_KEYS.values() and c != 'formal' or c in derived or (c == 'formal' and polite_alt)]
    e['changesBy'] = keep + sorted(derived - set(keep))

json.dump(data, open(P, 'w', encoding='utf8'), ensure_ascii=False, indent=2)
open(P, 'a').write('\n')
print(len(data), 'entries')
