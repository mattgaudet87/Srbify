"""One-time: re-map entries onto the intent-based categories. Adds `placements` [{category, subcategory}]
(first one is primary and also written to category/subcategory). Idempotent: reads placements from MAP below."""
import json, os
os.chdir(os.path.join(os.path.dirname(__file__), '..'))
QP, CV, FR, DF, ES, VA, BA, SS, CE = ('Quick phrases', 'Conversation', 'Flirting and relationships', 'Describing and feelings',
    'Everyday situations', 'Verbs and actions', 'Basics', 'Slang and swearing', 'Culture and etiquette')
S = {  # short names for subcategories, validated against src/lib/categories.js by build check
 'gb': 'Greetings and goodbyes', 'starters': 'Conversation starters', 'ynm': 'Yes, no, maybe', 'manners': 'Thanks, sorry, please',
 'agree': 'Agree and disagree', 'react': 'Reactions', 'replies': 'Common replies', 'filler': 'Filler and transition words',
 'intro': 'Introductions', 'q': 'Questions', 'ans': 'Answering questions', 'know': 'Getting to know someone', 'plans': 'Making plans',
 'confirm': 'Confirming plans', 'late': 'Running late', 'cancel': 'Cancelling', 'casual': 'Casual conversation',
 'tease': 'Teasing and comebacks', 'formal': 'Formal and polite',
 'comp': 'Compliments', 'flirt': 'Flirting', 'like': 'I like you', 'miss': 'Missing someone', 'affection': 'Affection and romance',
 'gmgn': 'Good morning and good night', 'nick': 'Nicknames and pet names', 'ptease': 'Playful teasing', 'dating': 'Dating', 'rel': 'Relationship talk',
 'emo': 'Emotions', 'phys': 'Physical states', 'pers': 'People: personality', 'appear': 'People: appearance', 'things': 'Describing things',
 'opin': 'Opinions', 'compar': 'Comparisons', 'opp': 'Opposites',
 'food': 'Food and drink', 'rest': 'Restaurants and cafés', 'out': 'Going out', 'home': 'Home', 'shop': 'Shopping and money', 'places': 'Places',
 'dir': 'Directions', 'travel': 'Travel and transportation', 'fam': 'Friends and family', 'events': 'Events', 'hols': 'Holidays and celebrations',
 'everyday': 'Everyday verbs', 'can': 'Can and can’t', 'want': 'Want and don’t want', 'need': 'Need and have to', 'present': 'Present',
 'past': 'Past', 'future': 'Future', 'cmd': 'Commands', 'req': 'Requests', 'inv': 'Invitations',
 'pron': 'Pronouns', 'poss': 'My, your, his, her', 'this': 'This and that', 'num': 'Numbers', 'time': 'Time and days', 'colors': 'Colors',
 'shapes': 'Shapes and sizes', 'qw': 'Question words', 'conj': 'And, but, because', 'prep': 'Prepositions', 'flow': 'Flow words',
 'textslang': 'Texting slang', 'abbr': 'Abbreviations', 'attitude': 'Attitude words', 'sreact': 'Reactions', 'cslang': 'Casual slang',
 'mild': 'Mild swearing', 'strong': 'Strong swearing', 'insult': 'Insults', 'pinsult': 'Playful insults', 'warn': 'Tone and usage warnings',
 'cfam': 'Meeting family', 'elders': 'Talking to elders', 'guest': 'Being a guest', 'toast': 'Toasts', 'chols': 'Holidays', 'saying': 'Common sayings',
 'idiom': 'Idioms', 'dont': 'Things not to say', 'ctx': 'Cultural context',
}
# Which category each short key lives in:
CAT = {}
for cat, keys in {QP: 'gb starters ynm manners agree react replies filler', CV: 'intro q ans know plans confirm late cancel casual tease formal',
  FR: 'comp flirt like miss affection gmgn nick ptease dating rel', DF: 'emo phys pers appear things opin compar opp',
  ES: 'food rest out home shop places dir travel fam events hols', VA: 'everyday can want need present past future cmd req inv',
  BA: 'pron poss this num time colors shapes qw conj prep flow', SS: 'textslang abbr attitude sreact cslang mild strong insult pinsult warn',
  CE: 'cfam elders guest toast chols saying idiom dont ctx'}.items():
    for k in keys.split(): CAT[k] = cat
# Keys used twice with different categories get a prefix: 'Q:react' means Quick phrases, 'S:react' means Slang.
def P(spec):
    out = []
    for tok in spec.split(';'):
        tok = tok.strip()
        if tok.startswith('S:'): out.append((SS, S['sreact'])); continue
        out.append((CAT[tok], S[tok]))
    return out

MAP = {
 'hello': 'gb;starters', 'cao': 'gb;cslang', 'see-you': 'gb', 'good-morning': 'gb;gmgn', 'laku-noc': 'gb;gmgn',
 'kako-si': 'starters;q;know', 'sta-ima': 'starters;casual;cslang', 'dobro-sam': 'replies;ans', 'im-tired': 'phys;replies;ans', 'im-happy': 'emo;replies',
 'thank-you': 'manners', 'sorry': 'manners', 'please': 'manners;req',
 'ludilo': 'react;S:react;cslang', 'dying-laughing': 'react;textslang;emo', 'funny': 'react;opin', 'ma-daj': 'react;attitude;agree',
 'ma-nemoj': 'agree;attitude;tease', 'salis-se': 'react;tease', 'cool': 'opin;cslang;react', 'bezveze': 'opin;cslang',
 'bre': 'attitude;filler', 'ajde': 'attitude;inv;filler', 'joj': 'attitude;react', 'nzm': 'abbr;textslang;replies',
 'tacno': 'agree;replies', 'aha': 'filler;replies', 'stvarno': 'react;casual', 'znaci': 'filler', 'pa': 'filler', 'ono': 'filler',
 'sumnjam': 'agree;ynm', 'ne-bih-rekao': 'agree;formal', 'nema-veze': 'replies;manners', 'vazi': 'agree;confirm;replies;ynm',
 'mozda': 'ynm', 'naravno': 'agree;ynm',
 'sta': 'qw;q', 'ko': 'qw;q', 'gde': 'qw;q', 'kad': 'qw;q', 'zasto': 'qw;q', 'kako': 'qw;q', 'koji': 'qw;q', 'koliko': 'qw;q;shop',
 'sta-radis': 'q;know;starters', 'gde-si': 'q', 'jesi-li-gladna': 'q;food;phys', 'odakle-si': 'know;q',
 'jebote': 'strong;warn', 'majke-mi': 'mild', 'do-vraga': 'mild', 'sranje': 'strong', 'jebi-se': 'strong;insult;warn', 'mars': 'insult;warn',
 'izvini-na-izrazu': 'warn;formal', 'nemoj-tako': 'warn;dont',
 'falis-mi': 'miss;flirt', 'lepa-si': 'comp;flirt;appear', 'izgledas-lepo': 'comp;appear', 'svidjas-mi-se': 'like;flirt',
 'mislim-na-tebe': 'miss;affection', 'draga': 'nick', 'ljubavi': 'nick;affection', 'laku-noc-lepotice': 'gmgn;nick', 'ljubim-te': 'affection',
 'volim-te': 'affection;rel;present', 'nasmejavas-me': 'comp;flirt;ptease',
 'nisam-to-rekao': 'tease;ptease;past', 'zezas-me': 'tease;ptease', 'nemoguc-sam': 'tease;ptease;pers', 'samo-se-salim': 'tease;ptease',
 'ne-ljuti-se': 'tease;rel;manners', 'luda-si': 'tease;ptease;pinsult;pers',
 'hoces-da-izadjemo': 'plans;dating;inv', 'kad-si-slobodna': 'plans;dating', 'gde-da-se-nadjemo': 'plans', 'u-koliko-sati': 'plans;time',
 'kasnim': 'late;present', 'stigao-sam': 'late;past', 'ne-mogu-da-dodjem': 'cancel;can', 'pomerimo': 'cancel;req',
 'ti-vi': 'pron;formal', 'on-ona': 'pron', 'ja-mi': 'pron', 'to-be': 'everyday;present', 'nisam': 'present', 'nemam': 'present',
 'moj': 'poss', 'tvoj': 'poss', 'i': 'conj;flow', 'ali': 'conj;flow', 'ili': 'conj;flow', 'takodje': 'conj;flow', 'bas': 'flow;filler',
 'brojevi': 'num',
 'idem': 'everyday;present', 'radim': 'everyday;present', 'znam': 'everyday;present', 'volim': 'everyday;present',
 'bio-sam': 'past;everyday', 'isao-sam': 'past;everyday', 'video-sam': 'past;everyday', 'jeo-sam': 'past;everyday',
 'zvacu-te': 'future;plans', 'javicu-se': 'future;plans', 'videcemo-se': 'future;plans',
 'dodji': 'cmd;inv', 'cekaj': 'cmd', 'javi-se': 'cmd;plans', 'spavaj': 'cmd',
 'mogu': 'can', 'hocu': 'want', 'necu': 'want', 'moram': 'need',
 'gladan': 'phys', 'zedan': 'phys', 'tuzan': 'emo', 'ljut': 'emo', 'dosadno-mi-je': 'emo',
 'pametan': 'pers', 'zgodan': 'appear', 'smesan': 'pers',
 'ukusno': 'things;food;opin', 'skupo': 'things;shop', 'jeftino': 'things;shop', 'dobro-lose': 'opin;opp', 'nije-lose': 'opin;opp', 'nezgodno': 'opp;opin',
 'kafa': 'food;rest', 'pivo': 'food', 'vino': 'food', 'voda': 'food', 'kafic': 'out;rest;places', 'racun': 'rest;shop',
 'stan': 'home', 'kod-mene': 'home;plans', 'aerodrom': 'travel;places', 'stanica': 'travel;places',
 'mama-tata': 'fam;cfam', 'brat-sestra': 'fam;cfam', 'baka-deda': 'fam;cfam', 'prijatelj': 'fam',
 'danas-sutra-juce': 'time', 'veceras': 'time', 'dani': 'time', 'vikend': 'time',
 'svadba': 'events', 'slava': 'events;hols;ctx', 'srecan-rodjendan': 'events;hols',
 'drago-mi-je': 'intro;cfam;formal', 'dobro-vece': 'gb;formal;cfam', 'izvolite': 'formal;guest', 'prijatno': 'guest;rest', 'jos-malo': 'guest;rest',
 'ne-treba': 'guest;replies', 'sve-je-bilo-ukusno': 'guest;food', 'odlicno-kuvate': 'guest;comp' if False else 'guest;food',
 'zivili': 'toast;out', 'ucim-srpski': 'know;intro', 'govorim-malo': 'know;intro', 'pozdravi-roditelje': 'cfam;formal',
 'srecan-praznik': 'chols;hols', 'bozic': 'chols;hols', 'uskrs': 'chols;hols', 'rakija': 'toast;ctx;food',
 'gost-u-kuci': 'saying;guest', 'polako': 'saying;idiom;replies', 'inat': 'ctx;idiom;pers', 'politika': 'dont;ctx', 'srpski-jezik': 'dont;ctx',
 'ko-to-kaze': 'tease;ptease', 'vidi-ko-prica': 'tease;ptease', 'sta-ti-znas': 'tease;ptease', 'moze': 'confirm;agree;replies',
 'dogovoreno': 'confirm', 'da-ne': 'ynm;ans', 'jesam': 'ynm;ans', 'zavisi': 'ynm;ans',
}
if __name__ == '__main__':
    data = json.load(open('src/data/entries.json'))
    ids = {e['id'] for e in data}
    assert ids == set(MAP), (ids - set(MAP), set(MAP) - ids)
    for e in data:
        pl = P(MAP[e['id']])
        e['placements'] = [{'category': c, 'subcategory': s} for c, s in pl]
        e['category'], e['subcategory'] = pl[0]
    json.dump(data, open('src/data/entries.json', 'w'), ensure_ascii=False, indent=2)
    print('remapped', len(data))
