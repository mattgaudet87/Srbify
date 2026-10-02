"""Confidence and review tracking for entries.

Every entry has  confidence: "sure" | "unsure"  (Claude's own confidence, NOT native-speaker verification).
Unsure entries also carry  reviewNote  (what to check)  and  reviewFlagged  (date). verified: true means a native speaker checked it.

  python3 scripts/review.py seed                 # apply the UNSURE table below to entries.json (idempotent)
  python3 scripts/review.py flag ID "note"       # mark an entry unsure
  python3 scripts/review.py resolve ID "outcome" # checked: sets verified + sure, logs the outcome
  python3 scripts/review.py log                  # regenerate REVIEW_LOG.md from the data
"""
import json, os, sys, datetime
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
P, H, LOG = 'src/data/entries.json', 'scripts/review_history.json', 'REVIEW_LOG.md'
TODAY = datetime.date.today().isoformat()

UNSURE = {
 # ── new this sweep ──
 'zafrkavas-me': 'Slang. Confirm it is common and fine to say to someone you are dating (vs. the gentler "zezaš me").',
 'faca': 'Slang. Confirm "Faca si" is still current and works as a compliment to a woman.',
 'kul': 'Slang from English. Confirm the spelling "kul" and that it does not sound dated.',
 'kunem-se': 'Confirm "Kunem ti se" is natural in casual texts and does not sound dramatic or old-fashioned.',
 'valjda': 'Confirm both senses (hopefully / I guess) and the example "Valjda ću stići na vreme".',
 'koliko-si-star': 'Confirm this is acceptable to ask a woman, and that "Koliko si stara?" reads naturally.',
 'ima-li-popusta': 'Confirm "Može li neki popust?" and "Ima li popusta ako uzmem dva?" are natural at a market.',
 'sta-ti-se-jede': 'Confirm the idiom "Šta ti se jede?" / "Jede mi se pica", and whether to write "pica" or "pizza".',
 'kapiram': 'Slang. Confirm register (is it fine with her friends/family?) and that "kapiraš li?" sounds right.',
 'fora': 'Confirm the meaning: "cool" vs "a trick/gag". Is "Ona je fora" natural for a person?',
 'drska-si': 'Confirm "Drska si" reads as playful, not insulting, and that "Drzak si" is OK to say to a man.',
 'preslatka-si': 'Confirm the masculine "Presladak si" (and whether men are called this at all).',
 'zaljubio-sam-se': 'Confirm the alternative "Imam krš na tebe" (crush) is a real, current expression.',
 'prvi-drugi-treci': 'Confirm the example "Ti si prva kojoj ovo kažem" and the ijekavian "posljednji".',
 'cena-u-dinarima': 'Grammar is standard, but confirm the idiom "Jedan dinar je mala para".',
 'napolju-je-hladno': 'Confirm the ijekavian/regional "Vani je hladno" and that "Obuci jaknu" is the natural phrase.',
 'evo': 'Confirm the difference between "evo" and "eto", and the example "Evo ti telefon".',
 'hajde-da': 'Confirm "Hajdete da…" is a real group/polite form.',
 'verovatno': 'The "about 70%" in the Watch-out is my own estimate. Confirm how strongly "verovatno" leans yes.',
 'sigurno': 'Confirm "Sasvim sigurno" and "Svakako" as alternatives.',
 'nedostajes-mi': 'Confirm my note that "nedostaješ mi" is softer/more written and "fališ mi" more spoken.',
 'falis-mi': 'Confirm the register difference with "nedostaješ mi".',
 # ── older entries ──
 'jebote': 'Vulgar. Confirm the strength and where it is acceptable.',
 'jebi-se': 'Vulgar. Confirm strength and the clean alternatives.',
 'jbg': 'Confirm "jbg" is really used in texts and what it means to her generation.',
 'sranje': 'Vulgar. Confirm strength.',
 'ne-seri': 'Vulgar. Confirm strength and that the clean alternative reads right.',
 'kreten': 'Confirm strength (insult) and whether there is a female form worth adding.',
 'mars': 'Slang. Confirm tone ("get lost") and the stronger "gubi se".',
 'do-vraga': 'Confirm it is not old-fashioned.',
 'bre': 'Regional filler. Confirm where it is used and when it can sound rude.',
 'care': 'Confirm "Care" (friendly address, "king") is current slang.',
 'keva-cale': 'Slang for mom/dad. Confirm usage and spelling (keva / ćale).',
 'maler': 'Slang. Confirm it is common and not regional.',
 'dying-laughing': 'Confirm "crkoh" and "umirem od smeha" are what people actually text.',
 'bzvz': 'Text abbreviation. Confirm it is used.',
 'ntp': 'Text abbreviation. Confirm it is used.',
 'lp': 'Text abbreviation. Confirm it is used and reads as friendly.',
 'ma-nemoj': 'Confirm the meaning ("yeah right" vs "you don\'t say") and when it is sarcastic.',
 'nemoguc-sam': 'Confirm the phrase sounds natural, not literal.',
 'ludilo': 'Slang. Confirm usage as "awesome" vs "crazy".',
 'majke-mi': 'Slang. Confirm tone and spelling.',
}

def load(): return json.load(open(P, encoding='utf8'))
def save(d):
    json.dump(d, open(P, 'w', encoding='utf8'), ensure_ascii=False, indent=2); open(P, 'a').write('\n')
def hist(): return json.load(open(H)) if os.path.exists(H) else []

def seed():
    d = load(); ids = {e['id'] for e in d}
    for k in UNSURE: assert k in ids, f'unknown id {k}'
    for e in d:
        if e['id'] in UNSURE and not e.get('verified'):
            e['confidence'] = 'unsure'; e['reviewNote'] = UNSURE[e['id']]; e.setdefault('reviewFlagged', TODAY)
        elif 'confidence' not in e:
            e['confidence'] = 'sure'
    save(d); log()

def flag(i, note):
    d = load(); e = next(x for x in d if x['id'] == i)
    e['confidence'] = 'unsure'; e['reviewNote'] = note; e['reviewFlagged'] = TODAY; e['verified'] = False; save(d); log()

def resolve(i, outcome):
    d = load(); e = next(x for x in d if x['id'] == i)
    h = hist(); h.append({'id': i, 'serbian': e['serbian'], 'was': e.get('reviewNote', ''), 'outcome': outcome, 'resolved': TODAY})
    json.dump(h, open(H, 'w'), ensure_ascii=False, indent=2)
    e['confidence'] = 'sure'; e['verified'] = True; e.pop('reviewNote', None); e.pop('reviewFlagged', None); save(d); log()

def log():
    d = load(); op = [e for e in d if e.get('confidence') == 'unsure']; h = hist()
    L = ['# Review log', '',
         'Things Claude is unsure about, kept on the site with a gray badge so they can be double-checked later by a native speaker.',
         'Blue badge = Claude is confident (or a native speaker verified it). Generated by `python3 scripts/review.py log`; do not edit by hand.', '',
         '**General caveats:** all pronunciation respellings are approximations, and the Ijekavian forms were written by hand. Neither is checked by a native speaker.', '',
         f'## Open ({len(op)})', '', '| Entry | Serbian | What to check | Flagged |', '|---|---|---|---|']
    for e in sorted(op, key=lambda x: x['id']):
        L.append(f"| `{e['id']}` | {e['serbian']} | {e['reviewNote'].replace('|', '/')} | {e.get('reviewFlagged', '')} |")
    L += ['', f'## Resolved ({len(h)})', '']
    if h:
        L += ['| Entry | Serbian | Was | Outcome | Resolved |', '|---|---|---|---|---|']
        for r in h: L.append(f"| `{r['id']}` | {r['serbian']} | {r['was'].replace('|', '/')} | {r['outcome'].replace('|', '/')} | {r['resolved']} |")
    else: L.append('Nothing resolved yet.')
    L += ['', '## How to close an item', '', '```', 'python3 scripts/review.py resolve ID "what the native speaker said"', '```',
          'This marks the entry verified (blue badge) and moves it here. If the answer means the entry must change, edit `src/data/entries.json` first.', '']
    open(LOG, 'w', encoding='utf8').write('\n'.join(L))
    print(f'{len(op)} open, {len(h)} resolved, {len(d) - len(op)} sure')

if __name__ == '__main__':
    c = sys.argv[1] if len(sys.argv) > 1 else 'log'
    {'seed': seed, 'log': log}.get(c, lambda: None)() if c in ('seed', 'log') else (flag if c == 'flag' else resolve)(*sys.argv[2:])
