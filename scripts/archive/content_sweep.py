"""Content batch from the PM sweep: ~50 new entries (missing everyday phrases + thin subcategories).
Idempotent (skips ids that already exist). Run order:
  python3 scripts/content_sweep.py   (adds entries, then adds word cards from NEW_WORDS)
  python3 scripts/build_words.py && python3 scripts/check_words.py && python3 scripts/check_data.py
"""
import json, os, sys, unicodedata
os.chdir(os.path.join(os.path.dirname(__file__), '..')); sys.path.insert(0, 'scripts')

CAT = {'QP': 'Quick phrases', 'CV': 'Conversation', 'FR': 'Flirting and relationships', 'DF': 'Describing and feelings',
       'ES': 'Everyday situations', 'VA': 'Verbs and actions', 'BA': 'Basics', 'SS': 'Slang and swearing', 'CE': 'Culture and etiquette'}

def X(ctx, sr, pr, en): return {'serbian': sr, 'pronunciation': pr, 'english': en, 'context': ctx}
def F(sr, pr, use, ex, **tags):
    f = {'serbian': sr, 'pronunciation': pr}; f.update(tags); f['useWhen'] = use
    f['example'] = {'serbian': ex[0], 'pronunciation': ex[1], 'english': ex[2]}; return f
def A(sr, pr, nuance): return {'serbian': sr, 'pronunciation': pr, 'nuance': nuance}

def strip(t): return unicodedata.normalize('NFD', t.lower().replace('đ', 'dj')).encode('ascii', 'ignore').decode()
FORM_KEYS = {'speaker': 'speaker', 'describes': 'describes', 'nounGender': 'noun gender', 'region': 'region'}
def E(id, en, sr, pr, meaning, places, tags, reg, ex, forms=None, alts=None, text=None, rel=(), watch=None, ij=None, hint=None, lit=None, ch=()):
    forms = forms or []
    by = {v for k, v in FORM_KEYS.items() if any(f.get(k) for f in forms)}
    if any(f.get('formal') == 'polite' for f in forms): by.add('formal')
    e = {'id': id, 'english': en, 'serbian': sr, 'pronunciation': pr, 'meaning': meaning,
         'category': CAT[places[0][0]], 'subcategory': places[0][1], 'tags': list(tags), 'register': reg,
         'changesBy': sorted(by) + list(ch)}
    if lit: e['literal'] = lit
    if forms: e['forms'] = forms
    if hint: e['patternHint'] = hint
    e['alternatives'] = [A(*a) for a in (alts or [])]
    if not e['alternatives']: del e['alternatives']
    e['examples'] = [X(*x) for x in ex]
    e['texting'] = text if text is not None else strip(sr).replace('?', '').replace('!', '').replace('…', '').strip(' ,')
    e['related'] = list(rel)
    if watch: e['watchOut'] = watch
    if ij: e['ijekavian'] = ij
    e['verified'] = False
    e['placements'] = [{'category': CAT[c], 'subcategory': s} for c, s in places]
    return e

NEW = []
add = NEW.append

# ───────── Not understanding / asking for help ─────────
add(E('ponovi', 'Can you repeat that?', 'Možeš li da ponoviš?', 'MOH-zhesh lee dah poh-NOH-veesh', 'Can you say that again?',
  [('CV', 'Questions'), ('QP', 'Common replies')], ['repeat', 'understand', 'language'], 'neutral',
  [('Slower', 'Možeš li da ponoviš sporije?', 'MOH-zhesh lee dah poh-NOH-veesh SPOH-ree-yeh', 'Can you repeat that more slowly?'),
   ('Bad connection', 'Ne čujem te, možeš li da ponoviš?', 'neh CHOO-yem teh, MOH-zhesh lee dah poh-NOH-veesh', "I can't hear you, can you repeat that?"),
   ('Missed it (man)', 'Nisam razumeo, možeš li da ponoviš?', 'NEE-sahm rah-ZOO-meh-oh, MOH-zhesh lee dah poh-NOH-veesh', "I didn't understand, can you repeat that? (a man says this)"),
   ('Missed it (woman)', 'Nisam razumela, možeš li da ponoviš?', 'NEE-sahm rah-ZOO-meh-lah, MOH-zhesh lee dah poh-NOH-veesh', "I didn't understand, can you repeat that? (a woman says this)")],
  forms=[F('Možeš li da ponoviš?', 'MOH-zhesh lee dah poh-NOH-veesh', 'To one friend or someone your age', ('Izvini, možeš li da ponoviš?', 'eez-VEE-nee, MOH-zhesh lee dah poh-NOH-veesh', 'Sorry, can you repeat that?'), formal='casual'),
         F('Možete li da ponovite?', 'MOH-zheh-teh lee dah poh-NOH-vee-teh', 'To an elder, a stranger, or a group', ('Oprostite, možete li da ponovite?', 'oh-PROH-stee-teh, MOH-zheh-teh lee dah poh-NOH-vee-teh', 'Excuse me, could you repeat that?'), formal='polite')],
  alts=[('Molim?', 'MOH-leem', 'Pardon? Quick and casual'), ('Šta si rekla?', 'SHTAH see REH-klah', 'What did you say? (to her; to a man: šta si rekao)'), ('Još jednom, molim te', 'yohsh YED-nom, MOH-leem teh', 'One more time, please')],
  text='mozes li da ponovis', rel=['razumem', 'govori-sporije', 'sta-znaci', 'govoris-li-engleski']))

add(E('govori-sporije', 'Speak slower, please', 'Govori sporije, molim te', 'GOH-vo-ree SPOH-ree-yeh, MOH-leem teh', 'Please speak more slowly',
  [('CV', 'Questions'), ('QP', 'Common replies')], ['slow', 'understand', 'language', 'request'], 'neutral',
  [('To her', 'Govori malo sporije, još učim', 'GOH-vo-ree MAH-lo SPOH-ree-yeh, yohsh OO-cheem', "Speak a bit slower, I'm still learning"),
   ('Quick ask', 'Sporije, molim te!', 'SPOH-ree-yeh, MOH-leem teh', 'Slower, please!'),
   ("To her mom", 'Možete li da govorite sporije?', 'MOH-zheh-teh lee dah GOH-vo-ree-teh SPOH-ree-yeh', 'Could you speak more slowly?'),
   ('About her', 'Ona govori brzo', 'OH-nah GOH-vo-ree BUR-zo', 'She talks fast')],
  forms=[F('Govori sporije', 'GOH-vo-ree SPOH-ree-yeh', 'To one friend or someone your age', ('Govori sporije, molim te', 'GOH-vo-ree SPOH-ree-yeh, MOH-leem teh', 'Speak slower, please'), formal='casual'),
         F('Govorite sporije', 'GOH-vo-ree-teh SPOH-ree-yeh', 'To an elder, a stranger, or a group', ('Govorite sporije, molim vas', 'GOH-vo-ree-teh SPOH-ree-yeh, MOH-leem vahs', 'Please speak more slowly'), formal='polite')],
  alts=[('Polako', 'poh-LAH-ko', 'Slowly, take it easy'), ('Malo sporije', 'MAH-lo SPOH-ree-yeh', 'A bit slower')],
  rel=['ponovi', 'razumem', 'polako', 'ucim-srpski']))

add(E('sta-znaci', 'What does … mean?', 'Šta znači…?', 'SHTAH ZNAH-chee', 'What does this word or phrase mean?',
  [('CV', 'Questions'), ('CV', 'Casual conversation')], ['meaning', 'language', 'question'], 'neutral',
  [('A word', "Šta znači 'inat'?", 'SHTAH ZNAH-chee EE-naht', "What does 'inat' mean?"),
   ('A phrase', "Šta znači 'majke mi'?", 'SHTAH ZNAH-chee MAHY-keh mee', "What does 'majke mi' mean?"),
   ('Her words', 'Šta znači to što si rekla?', 'SHTAH ZNAH-chee toh shtoh see REH-klah', 'What does what you said mean?'),
   ('A sign', 'Šta ovo znači?', 'SHTAH OH-vo ZNAH-chee', 'What does this mean?')],
  alts=[('Šta to znači?', 'SHTAH toh ZNAH-chee', 'What does that mean?'), ('Šta je to?', 'SHTAH yeh toh', 'What is that?')],
  rel=['kako-se-kaze', 'ponovi', 'razumem', 'inat']))

add(E('kako-se-kaze', 'How do you say … in Serbian?', 'Kako se kaže… na srpskom?', 'KAH-ko seh KAH-zheh … nah SUR-pskom', 'How do you say this in Serbian?',
  [('CV', 'Questions'), ('QP', 'Conversation starters')], ['language', 'learning', 'question'], 'neutral',
  [('Asking her', 'Kako se kaže (coffee) na srpskom?', 'KAH-ko seh KAH-zheh nah SUR-pskom', "How do you say 'coffee' in Serbian?"),
   ('Pointing at it', 'Kako se ovo kaže?', 'KAH-ko seh OH-vo KAH-zheh', 'How do you say this?'),
   ('Teaching her', "Kako se kaže 'zdravo' na engleskom?", 'KAH-ko seh KAH-zheh ZDRAH-voh nah ENG-leh-skom', "How do you say 'zdravo' in English?"),
   ('Spelling', 'Kako se piše?', 'KAH-ko seh PEE-sheh', 'How is it written? How do you spell it?')],
  alts=[('Kako se to izgovara?', 'KAH-ko seh toh eez-GOH-vah-rah', 'How do you pronounce that?')],
  rel=['sta-znaci', 'ucim-srpski', 'govorim-malo', 'ponovi']))

add(E('ne-govorim-dobro', "I don't speak Serbian well", 'Ne govorim dobro srpski', 'neh GOH-vo-reem DOH-bro SUR-pskee', "I'm not good at Serbian yet",
  [('CV', 'Getting to know someone'), ('QP', 'Common replies')], ['language', 'learning', 'apology'], 'neutral',
  [('To her', 'Ne govorim dobro srpski, ali trudim se', 'neh GOH-vo-reem DOH-bro SUR-pskee, AH-lee TROO-deem seh', "I don't speak Serbian well, but I'm trying"),
   ('Understanding', 'Razumem više nego što govorim', 'rah-ZOO-mem VEE-sheh NEH-go shtoh GOH-vo-reem', 'I understand more than I speak'),
   ('Both languages', 'Govorim engleski i malo srpski', 'GOH-vo-reem ENG-leh-skee ee MAH-lo SUR-pskee', 'I speak English and a little Serbian'),
   ('Complimenting her', 'Ti odlično govoriš engleski', 'tee od-LEECH-no GOH-vo-reesh ENG-leh-skee', 'You speak English really well')],
  alts=[('Još učim srpski', 'yohsh OO-cheem SUR-pskee', "I'm still learning Serbian")],
  rel=['govorim-malo', 'ucim-srpski', 'govori-sporije', 'govoris-li-engleski']))

# ───────── About you ─────────
add(E('iz-kanade', "I'm from Canada", 'Ja sam iz Kanade', 'yah sahm eez KAH-nah-deh', "I'm from Canada",
  [('CV', 'Getting to know someone'), ('CV', 'Introductions')], ['canada', 'from', 'origin'], 'neutral',
  [('To her', 'Ja sam iz Kanade, a ti?', 'yah sahm eez KAH-nah-deh, ah TEE', "I'm from Canada, and you?"),
   ('About a friend', 'Moj prijatelj je iz Kanade', 'moy PREE-yah-tel yeh eez KAH-nah-deh', 'My friend is from Canada'),
   ('Asking her', 'Jesi li ti iz Beograda?', 'YEH-see lee tee eez beh-oh-GRAH-dah', 'Are you from Belgrade?'),
   ('About us', 'Mi smo iz Kanade', 'mee smo eez KAH-nah-deh', "We're from Canada")],
  forms=[F('Ja sam iz Kanade', 'yah sahm eez KAH-nah-deh', 'About me', ('Ja sam iz Kanade, ali mi se Srbija sviđa', 'yah sahm eez KAH-nah-deh, AH-lee mee seh SUR-bee-yah SVEE-jah', "I'm from Canada, but I like Serbia"), describes='me'),
         F('Ti si iz Srbije?', 'tee see eez SUR-bee-yeh', 'Asking her', ('Ti si iz Srbije? Odakle tačno?', 'tee see eez SUR-bee-yeh? OH-dahk-leh TAHCH-no', 'Are you from Serbia? Where exactly?'), describes='her'),
         F('On je iz Kanade / Ona je iz Kanade', 'ohn yeh eez KAH-nah-deh / OH-nah yeh eez KAH-nah-deh', 'About someone else', ('Ona je iz Kanade, ali živi ovde', 'OH-nah yeh eez KAH-nah-deh, AH-lee ZHEE-vee OHV-deh', "She's from Canada, but she lives here"), describes='him / her'),
         F('Mi smo iz Kanade', 'mee smo eez KAH-nah-deh', 'About us', ('Mi smo iz Kanade, prvi put smo ovde', 'mee smo eez KAH-nah-deh, PUR-vee poot smo OHV-deh', "We're from Canada, it's our first time here"), describes='us')],
  alts=[('Dolazim iz Kanade', 'doh-LAH-zeem eez KAH-nah-deh', 'I come from Canada'), ('Kanađanin sam', 'kah-NAH-jah-neen sahm', "I'm a Canadian (a man says this; a woman: Kanađanka sam)")],
  rel=['odakle-si', 'drago-mi-je', 'kako-se-zoves', 'prvi-put']))

add(E('cime-se-bavis', 'What do you do (for work)?', 'Čime se baviš?', 'CHEE-meh seh BAH-veesh', 'What is your job or what are you into?',
  [('CV', 'Getting to know someone'), ('CV', 'Questions')], ['work', 'job', 'question'], 'neutral',
  [('Asking her', 'Čime se baviš? Radiš ili studiraš?', 'CHEE-meh seh BAH-veesh? RAH-deesh EE-lee stoo-DEE-rahsh', 'What do you do? Do you work or study?'),
   ('Answering', 'Bavim se dizajnom', 'BAH-veem seh dee-ZAHY-nom', 'I work in design'),
   ('About her brother', 'Čime se bavi tvoj brat?', 'CHEE-meh seh BAH-vee tvoy BRAHT', 'What does your brother do?'),
   ('About her', 'Ona se bavi muzikom', 'OH-nah seh BAH-vee MOO-zee-kom', 'She does music')],
  forms=[F('Čime se baviš?', 'CHEE-meh seh BAH-veesh', 'To one friend or someone your age', ('Čime se baviš u slobodno vreme?', 'CHEE-meh seh BAH-veesh oo SLOH-bod-no VREH-meh', 'What are you into in your free time?'), formal='casual'),
         F('Čime se bavite?', 'CHEE-meh seh BAH-vee-teh', 'To an elder, a stranger, or a group', ('Čime se bavite, ako smem da pitam?', 'CHEE-meh seh BAH-vee-teh, AH-ko smem dah PEE-tahm', 'What do you do, if I may ask?'), formal='polite')],
  alts=[('Šta radiš od posla?', 'SHTAH RAH-deesh od POH-slah', 'What do you do for work?'), ('Gde radiš?', 'GDEH RAH-deesh', 'Where do you work?')],
  rel=['sta-radis', 'odakle-si', 'gde-zivis', 'ucim-srpski']))

add(E('prvi-put', 'First time in Serbia', 'Prvi put sam u Srbiji', 'PUR-vee poot sahm oo SUR-bee-yee', "It's my first time in Serbia",
  [('CV', 'Getting to know someone'), ('ES', 'Travel and transportation')], ['travel', 'first time', 'serbia'], 'neutral',
  [('To her', 'Prvi put sam u Srbiji, pokaži mi grad', 'PUR-vee poot sahm oo SUR-bee-yee, poh-KAH-zhee mee GRAHD', "It's my first time in Serbia, show me the city"),
   ('Trying food', 'Prvi put probam burek', 'PUR-vee poot PROH-bahm BOO-rek', "I'm trying burek for the first time"),
   ('About him', 'On je prvi put u Srbiji', 'ohn yeh PUR-vee poot oo SUR-bee-yee', "It's his first time in Serbia")],
  forms=[F('Prvi put sam u Srbiji', 'PUR-vee poot sahm oo SUR-bee-yee', 'About me', ('Prvi put sam u Beogradu', 'PUR-vee poot sahm oo beh-oh-GRAH-doo', "It's my first time in Belgrade"), describes='me'),
         F('Jesi li ovde prvi put?', 'YEH-see lee OHV-deh PUR-vee poot', 'Asking her', ('Jesi li ovde prvi put? Kako ti se sviđa?', 'YEH-see lee OHV-deh PUR-vee poot? KAH-ko tee seh SVEE-jah', 'Is it your first time here? How do you like it?'), describes='her'),
         F('Prvi put smo ovde', 'PUR-vee poot smo OHV-deh', 'About us', ('Prvi put smo ovde, pokaži nam grad', 'PUR-vee poot smo OHV-deh, poh-KAH-zhee nahm GRAHD', "It's our first time here, show us the city"), describes='us')],
  rel=['iz-kanade', 'srecan-put', 'ucim-srpski', 'cevapi']))

# ───────── Daily check-ins ─────────
add(E('kako-je-prosao-dan', 'How was your day?', 'Kako je prošao dan?', 'KAH-ko yeh PROH-shah-oh DAHN', 'How did your day go?',
  [('CV', 'Casual conversation'), ('FR', 'Relationship talk')], ['day', 'question', 'check in'], 'casual',
  [('To her', 'Kako je prošao dan? Jesi li umorna?', 'KAH-ko yeh PROH-shah-oh DAHN? YEH-see lee OO-mor-nah', 'How was your day? Are you tired?'),
   ('Answering', 'Prošao je dobro, malo naporno', 'PROH-shah-oh yeh DOH-bro, MAH-lo nah-POR-no', 'It went well, a bit tiring'),
   ('About her exam', 'Kako je prošao njen ispit?', 'KAH-ko yeh PROH-shah-oh nyen EES-peet', 'How did her exam go?'),
   ('Long day', 'Dug dan, ali dobar', 'DOOG dahn, AH-lee DOH-bahr', 'A long day, but a good one')],
  forms=[F('Kako je prošao dan?', 'KAH-ko yeh PROH-shah-oh DAHN', 'To one friend or someone your age', ('Kako je prošao dan na poslu?', 'KAH-ko yeh PROH-shah-oh DAHN nah POH-sloo', 'How was your day at work?'), formal='casual'),
         F('Kako vam je prošao dan?', 'KAH-ko vahm yeh PROH-shah-oh DAHN', 'To an elder, a stranger, or a group', ('Kako vam je prošao dan, gospođo?', 'KAH-ko vahm yeh PROH-shah-oh DAHN, GOH-spoh-joh', 'How was your day, ma’am?'), formal='polite')],
  alts=[('Kako ti je bio dan?', 'KAH-ko tee yeh BEE-oh DAHN', "How was your day? (literally 'how was the day to you')")],
  rel=['kako-si', 'kako-je-bilo', 'sta-radis-danas', 'jesi-li-dobro']))

add(E('jesi-li-stigla', 'Did you arrive?', 'Jesi li stigla?', 'YEH-see lee STEEG-lah', 'Did you get there? Are you there yet?',
  [('CV', 'Questions'), ('CV', 'Running late'), ('VA', 'Past')], ['arrive', 'question', 'past'], 'casual',
  [('To her', 'Jesi li stigla? Javi mi', 'YEH-see lee STEEG-lah? YAH-vee mee', 'Did you arrive? Let me know'),
   ('Her reply', 'Stigla sam, sve je u redu', 'STEEG-lah sahm, SVEH yeh oo REH-doo', "I've arrived, everything's fine (a woman says this)"),
   ('My reply', 'Stigao sam pre tebe', 'STEE-gah-oh sahm PREH TEH-beh', "I got here before you (a man says this)"),
   ('About a thing', 'Je li stigao paket?', 'YEH lee STEE-gah-oh PAH-ket', 'Has the package arrived?')],
  forms=[F('Jesi li stigla?', 'YEH-see lee STEEG-lah', 'Asking her', ('Jesi li stigla kući?', 'YEH-see lee STEEG-lah KOO-chee', 'Did you get home?'), describes='her'),
         F('Jesi li stigao?', 'YEH-see lee STEE-gah-oh', 'Asking a man', ('Jesi li stigao na posao?', 'YEH-see lee STEE-gah-oh nah POH-sah-oh', 'Did you get to work?'), describes='him'),
         F('Je li stigla?', 'YEH lee STEEG-lah', 'Asking about her', ('Je li stigla Ana?', 'YEH lee STEEG-lah AH-nah', 'Has Ana arrived?'), describes='her'),
         F('Jesmo li već stigli?', 'YES-mo lee vuhch STEEG-lee', 'Asking about us', ('Jesmo li već stigli? Ne vidim ništa', 'YES-mo lee vuhch STEEG-lee? neh VEE-deem NEESH-tah', "Are we there already? I can't see anything"), describes='us')],
  alts=[('Je l\' si stigla?', 'yel see STEEG-lah', 'Very casual spoken version')],
  text='jesi li stigla', rel=['stigao-sam', 'javi-mi-kad-stignes', 'kasnim', 'jesi-li-dobro']))

add(E('jesi-li-dobro', 'Are you okay?', 'Jesi li dobro?', 'YEH-see lee DOH-bro', 'Are you okay? Is everything alright?',
  [('CV', 'Questions'), ('DF', 'Emotions')], ['okay', 'worried', 'question'], 'casual',
  [('To her, worried', 'Jesi li dobro? Zvučiš umorno', 'YEH-see lee DOH-bro? ZVOO-cheesh oo-MOR-no', 'Are you okay? You sound tired'),
   ('Answering (woman)', 'Dobro sam, samo sam umorna', 'DOH-bro sahm, SAH-mo sahm OO-mor-nah', "I'm okay, just tired (a woman says this)"),
   ('Answering (man)', 'Dobro sam, samo sam umoran', 'DOH-bro sahm, SAH-mo sahm OO-mo-rahn', "I'm okay, just tired (a man says this)"),
   ('About him', 'Je li on dobro?', 'YEH lee ohn DOH-bro', 'Is he okay?')],
  forms=[F('Jesi li dobro?', 'YEH-see lee DOH-bro', 'To one friend or someone your age', ('Jesi li dobro? Nisi se javila', 'YEH-see lee DOH-bro? NEE-see seh YAH-vee-lah', "Are you okay? You didn't get in touch"), formal='casual'),
         F('Jeste li dobro?', 'YES-teh lee DOH-bro', 'To an elder, a stranger, or a group', ('Jeste li dobro, gospođo?', 'YES-teh lee DOH-bro, GOH-spoh-joh', 'Are you alright, ma’am?'), formal='polite')],
  alts=[("Je l' sve u redu?", 'yel SVEH oo REH-doo', 'Is everything okay?')],
  rel=['kako-si', 'ne-brini', 'jesi-li-stigla', 'kako-je-prosao-dan']))

add(E('sta-radis-danas', 'What are you doing today?', 'Šta radiš danas?', 'SHTAH RAH-deesh DAH-nahs', 'What are you up to today?',
  [('CV', 'Making plans'), ('CV', 'Questions')], ['today', 'plans', 'question'], 'casual',
  [('To her', 'Šta radiš danas? Hoćeš da se vidimo?', 'SHTAH RAH-deesh DAH-nahs? HOH-chesh dah seh VEE-dee-mo', 'What are you up to today? Want to meet up?'),
   ('About me', 'Danas radim od kuće', 'DAH-nahs RAH-deem od KOO-cheh', "I'm working from home today"),
   ('About him', 'Šta on radi danas?', 'SHTAH ohn RAH-dee DAH-nahs', 'What is he doing today?'),
   ('About us', 'Šta radimo danas?', 'SHTAH RAH-dee-mo DAH-nahs', 'What are we doing today?')],
  forms=[F('Šta radiš danas?', 'SHTAH RAH-deesh DAH-nahs', 'To one friend or someone your age', ('Šta radiš danas posle posla?', 'SHTAH RAH-deesh DAH-nahs POH-sleh POH-slah', 'What are you doing after work today?'), formal='casual'),
         F('Šta radite danas?', 'SHTAH RAH-dee-teh DAH-nahs', 'To an elder, a stranger, or a group', ('Šta radite danas, imate li vremena?', 'SHTAH RAH-dee-teh DAH-nahs, EE-mah-teh lee VREH-meh-nah', 'What are you doing today, do you have time?'), formal='polite')],
  rel=['sta-radis', 'plan-za-vikend', 'kad-si-slobodna', 'kako-je-prosao-dan']))

add(E('jesi-li-se-naspavala', 'Did you sleep well?', 'Jesi li se naspavala?', 'YEH-see lee seh nah-SPAH-vah-lah', 'Did you get a good night of sleep?',
  [('FR', 'Good morning and good night'), ('CV', 'Questions')], ['sleep', 'morning', 'question'], 'casual',
  [('Morning text', 'Dobro jutro! Jesi li se naspavala?', 'DOH-bro YOO-tro! YEH-see lee seh nah-SPAH-vah-lah', 'Good morning! Did you sleep well?'),
   ('Not really (man)', 'Nisam se baš naspavao', 'NEE-sahm seh BAHSH nah-SPAH-vah-oh', "I didn't sleep that well (a man says this)"),
   ('Her reply', 'Naspavala sam se, hvala', 'nah-SPAH-vah-lah sahm seh, HVAH-lah', 'I slept well, thanks (a woman says this)')],
  forms=[F('Jesi li se naspavala?', 'YEH-see lee seh nah-SPAH-vah-lah', 'Asking her', ('Jesi li se naspavala? Izgledaš odmorno', 'YEH-see lee seh nah-SPAH-vah-lah? EEZ-gleh-dahsh OD-mor-no', 'Did you sleep well? You look rested'), describes='her'),
         F('Jesi li se naspavao?', 'YEH-see lee seh nah-SPAH-vah-oh', 'Asking a man', ('Jesi li se naspavao, brate?', 'YEH-see lee seh nah-SPAH-vah-oh, BRAH-teh', 'Did you sleep well, man?'), describes='him'),
         F('Naspavao sam se', 'nah-SPAH-vah-oh sahm seh', 'A man says it about himself', ('Naspavao sam se kao beba', 'nah-SPAH-vah-oh sahm seh KAH-oh BEH-bah', 'I slept like a baby'), speaker='male'),
         F('Naspavala sam se', 'nah-SPAH-vah-lah sahm seh', 'A woman says it about herself', ('Naspavala sam se kao beba', 'nah-SPAH-vah-lah sahm seh KAH-oh BEH-bah', 'I slept like a baby'), speaker='female')],
  rel=['good-morning', 'laku-noc', 'dobro-jutro-sunce', 'spavaj']))

add(E('dobro-jutro-sunce', 'Good morning, sunshine', 'Dobro jutro, sunce', 'DOH-bro YOO-tro, SOON-tseh', 'A warm good-morning text to someone you like',
  [('FR', 'Good morning and good night'), ('FR', 'Nicknames and pet names')], ['morning', 'sweet', 'pet name'], 'casual',
  [('Morning text', 'Dobro jutro, sunce moje', 'DOH-bro YOO-tro, SOON-tseh MOH-yeh', 'Good morning, my sunshine'),
   ('With coffee', 'Dobro jutro! Kafa je spremna', 'DOH-bro YOO-tro! KAH-fah yeh SPREM-nah', 'Good morning! The coffee is ready'),
   ('Late wake-up', 'Dobro jutro, spavalice', 'DOH-bro YOO-tro, spah-vah-LEE-tseh', 'Good morning, sleepyhead')],
  forms=[F('Dobro jutro, sunce', 'DOH-bro YOO-tro, SOON-tseh', 'To her, warm', ('Dobro jutro, sunce! Kako si spavala?', 'DOH-bro YOO-tro, SOON-tseh! KAH-ko see SPAH-vah-lah', 'Good morning, sunshine! How did you sleep?'), describes='her'),
         F('Dobro jutro, ljubavi', 'DOH-bro YOO-tro, LYOO-bah-vee', 'To a partner', ('Dobro jutro, ljubavi, spavaj još malo', 'DOH-bro YOO-tro, LYOO-bah-vee, SPAH-vai yohsh MAH-lo', 'Good morning, love, sleep a little more'), describes='her'),
         F('Dobro jutro, brate', 'DOH-bro YOO-tro, BRAH-teh', 'To a guy friend', ('Dobro jutro, brate, spreman za posao?', 'DOH-bro YOO-tro, BRAH-teh, SPREH-mahn zah POH-sah-oh', 'Morning, man, ready for work?'), describes='him')],
  alts=[('Dobro jutro, lepotice', 'DOH-bro YOO-tro, leh-poh-TEE-tseh', 'Good morning, beautiful')],
  rel=['good-morning', 'laku-noc-lepotice', 'zlato-sunce', 'jesi-li-se-naspavala']))

# ───────── Missing someone / affection ─────────
add(E('nedostajes-mi', 'I miss you', 'Nedostaješ mi', 'neh-doh-STAH-yesh mee', 'I miss you (standard way)',
  [('FR', 'Missing someone'), ('FR', 'Affection and romance')], ['miss', 'love', 'sweet'], 'casual',
  [('To her', 'Nedostaješ mi više nego što misliš', 'neh-doh-STAH-yesh mee VEE-sheh NEH-go shtoh MEE-sleesh', 'I miss you more than you think'),
   ('Late night', 'Nedostaješ mi večeras', 'neh-doh-STAH-yesh mee VEH-cheh-rahs', 'I miss you tonight'),
   ('About a place', 'Nedostaje mi Beograd', 'neh-doh-STAH-yeh mee beh-oh-GRAHD', 'I miss Belgrade'),
   ('About a thing', 'Nedostaje mi naš razgovor', 'neh-doh-STAH-yeh mee NAHSH rahz-GOH-vor', 'I miss our conversations')],
  forms=[F('Nedostaješ mi', 'neh-doh-STAH-yesh mee', 'I miss you (to one person)', ('Nedostaješ mi, kad se vidimo?', 'neh-doh-STAH-yesh mee, KAHD seh VEE-dee-mo', 'I miss you, when do we see each other?'), describes='her', formal='casual'),
         F('Nedostajem li ti?', 'neh-doh-STAH-yem lee tee', 'Asking her: "do you miss me?"', ('Nedostajem li ti makar malo?', 'neh-doh-STAH-yem lee tee MAH-kahr MAH-lo', 'Do you miss me even a little?'), describes='me'),
         F('I ti meni nedostaješ', 'ee tee MEH-nee neh-doh-STAH-yesh', 'Replying: "I miss you too"', ('I ti meni nedostaješ, jako', 'ee tee MEH-nee neh-doh-STAH-yesh, YAH-ko', 'I miss you too, a lot'), describes='her'),
         F('Nedostaje mi…', 'neh-doh-STAH-yeh mee', 'I miss someone else or something', ('Nedostaje mi moja mama', 'neh-doh-STAH-yeh mee MOH-yah MAH-mah', 'I miss my mom'), describes='him / her'),
         F('Nedostajete mi', 'neh-doh-STAH-yeh-teh mee', 'Polite or to a group', ('Nedostajete mi svi', 'neh-doh-STAH-yeh-teh mee SVEE', 'I miss you all'), formal='polite')],
  alts=[('Fališ mi', 'FAH-leesh mee', 'The everyday spoken way to say it'), ('Mnogo mi nedostaješ', 'MNOH-go mee neh-doh-STAH-yesh', 'I miss you so much')],
  watch='Both "nedostaješ mi" and "fališ mi" are used. "Nedostaješ mi" is a little softer and also reads well in writing; "fališ mi" is the everyday spoken version.',
  rel=['falis-mi', 'mislim-na-tebe', 'jedva-cekam', 'sanjao-sam-te']))

add(E('sanjao-sam-te', 'I dreamed about you', 'Sanjao sam te', 'SAHN-yah-oh sahm teh', 'I dreamed about you',
  [('FR', 'Missing someone'), ('FR', 'Affection and romance')], ['dream', 'sweet', 'past'], 'casual',
  [('To her', 'Sanjao sam te sinoć', 'SAHN-yah-oh sahm teh SEE-noch', 'I dreamed about you last night'),
   ('A strange dream', 'Sanjao sam čudan san', 'SAHN-yah-oh sahm CHOO-dahn SAHN', 'I had a strange dream'),
   ('Sweet dreams', 'Slatkih snova, sanjaj me', 'SLAHT-keeh SNOH-vah, SAHN-yai meh', 'Sweet dreams, dream of me')],
  forms=[F('Sanjao sam te', 'SAHN-yah-oh sahm teh', 'A man says it', ('Sinoć sam te sanjao', 'SEE-noch sahm teh SAHN-yah-oh', 'I dreamed about you last night'), speaker='male'),
         F('Sanjala sam te', 'SAHN-yah-lah sahm teh', 'A woman says it', ('Sanjala sam te noćas', 'SAHN-yah-lah sahm teh NOH-chahs', 'I dreamed about you tonight'), speaker='female'),
         F('Jesi li me sanjala?', 'YEH-see lee meh SAHN-yah-lah', 'Asking her', ('Jesi li me sanjala? Ja sam tebe sanjao', 'YEH-see lee meh SAHN-yah-lah? yah sahm TEH-beh SAHN-yah-oh', 'Did you dream about me? I dreamed about you'), describes='her')],
  ch=['tense'], rel=['nedostajes-mi', 'slatkih-snova', 'mislim-na-tebe', 'laku-noc-lepotice']))

add(E('jedva-cekam', "I can't wait to see you", 'Jedva čekam da te vidim', 'YED-vah CHEH-kahm dah teh VEE-deem', "I can't wait to see you",
  [('FR', 'Missing someone'), ('FR', 'Dating')], ['excited', 'wait', 'dating'], 'casual',
  [('Before a date', 'Jedva čekam večeras', 'YED-vah CHEH-kahm VEH-cheh-rahs', "I can't wait for tonight"),
   ('The trip', 'Jedva čekam da stignem', 'YED-vah CHEH-kahm dah STEEG-nem', "I can't wait to get there"),
   ('Text sign-off', 'Jedva čekam subotu!', 'YED-vah CHEH-kahm SOO-bo-too', "Can't wait for Saturday!")],
  forms=[F('Jedva čekam da te vidim', 'YED-vah CHEH-kahm dah teh VEE-deem', "To her: I can't wait to see you", ('Jedva čekam da te vidim u petak', 'YED-vah CHEH-kahm dah teh VEE-deem oo PEH-tahk', "I can't wait to see you on Friday"), describes='her'),
         F('Jedva čekaš?', 'YED-vah CHEH-kahsh', "Teasing her: can't you wait?", ('Jedva čekaš vikend, je l\' tako?', 'YED-vah CHEH-kahsh VEE-kend, yel TAH-ko', "You can't wait for the weekend, can you?"), describes='her'),
         F('Jedva čeka', 'YED-vah CHEH-kah', "He / she can't wait", ('Moja sestra jedva čeka put', 'MOH-yah SEH-strah YED-vah CHEH-kah POOT', "My sister can't wait for the trip"), describes='him / her'),
         F('Jedva čekamo', 'YED-vah CHEH-kah-mo', "We can't wait", ('Jedva čekamo svadbu', 'YED-vah CHEH-kah-mo SVAHD-boo', "We can't wait for the wedding"), describes='us')],
  alts=[('Jedva čekam', 'YED-vah CHEH-kahm', "I can't wait (short)")],
  rel=['hocu-da-te-vidim', 'nedostajes-mi', 'vidimo-se-u-osam', 'kad-si-slobodna']))

# ───────── Apologies ─────────
add(E('zao-mi-je', "I'm sorry (I feel bad)", 'Žao mi je', 'ZHAH-oh mee yeh', "I'm sorry; I feel regret or sympathy",
  [('QP', 'Thanks, sorry, please'), ('FR', 'Relationship talk')], ['sorry', 'sympathy', 'regret'], 'neutral',
  [('Sympathy', 'Žao mi je što si bolesna', 'ZHAH-oh mee yeh shtoh see BOH-lesh-nah', "I'm sorry you're sick (to her)"),
   ('Regret', 'Žao mi je zbog sinoć', 'ZHAH-oh mee yeh ZBOHG SEE-noch', "I'm sorry about last night"),
   ('Condolences', 'Žao mi je zbog tvog dede', 'ZHAH-oh mee yeh ZBOHG tvohg DEH-deh', "I'm sorry about your grandfather")],
  forms=[F('Žao mi je', 'ZHAH-oh mee yeh', 'About me', ('Žao mi je, nisam hteo da te povredim', 'ZHAH-oh mee yeh, NEE-sahm HTEH-oh dah teh poh-VREH-deem', "I'm sorry, I didn't mean to hurt you"), describes='me'),
         F('Žao ti je?', 'ZHAH-oh tee yeh', 'Asking her', ('Žao ti je što ne dolaziš?', 'ZHAH-oh tee yeh shtoh neh DOH-lah-zeesh', "Are you sorry you're not coming?"), describes='her'),
         F('Žao mu je / Žao joj je', 'ZHAH-oh moo yeh / ZHAH-oh yoy yeh', 'About him / her', ('Žao joj je zbog toga', 'ZHAH-oh yoy yeh ZBOHG TOH-gah', "She's sorry about that"), describes='him / her'),
         F('Žao nam je', 'ZHAH-oh nahm yeh', 'About us', ('Žao nam je što kasnimo', 'ZHAH-oh nahm yeh shtoh KAH-snee-mo', "We're sorry we're late"), describes='us')],
  alts=[('Izvini', 'eez-VEE-nee', 'Asks forgiveness; more of an "excuse me" or "sorry I did it"')],
  watch='"Izvini" asks for forgiveness for something you did. "Žao mi je" says you feel bad, and it is also what you say when someone is hurting ("I\'m sorry for your loss").',
  ij='Žao mi je (same)', rel=['sorry', 'oprosti', 'ne-ljuti-se', 'izvini-sto-kasnim']))

add(E('oprosti', 'Forgive me', 'Oprosti', 'oh-PROH-stee', 'Forgive me; a warmer, more personal sorry',
  [('QP', 'Thanks, sorry, please'), ('FR', 'Relationship talk')], ['sorry', 'forgive', 'apology'], 'casual',
  [('Apologizing (man)', 'Oprosti, nisam hteo', 'oh-PROH-stee, NEE-sahm HTEH-oh', "Forgive me, I didn't mean to (a man says this)"),
   ('Apologizing (woman)', 'Oprosti, nisam htela', 'oh-PROH-stee, NEE-sahm HTEH-lah', "Forgive me, I didn't mean to (a woman says this)"),
   ('Begging', 'Oprosti mi, molim te', 'oh-PROH-stee mee, MOH-leem teh', 'Forgive me, please')],
  forms=[F('Oprosti', 'oh-PROH-stee', 'To one friend or someone your age', ('Oprosti mi što sam kasnio', 'oh-PROH-stee mee shtoh sahm KAH-snee-oh', "Forgive me for being late"), formal='casual'),
         F('Oprostite', 'oh-PROH-stee-teh', 'To an elder, a stranger, or a group', ('Oprostite, gde je stanica?', 'oh-PROH-stee-teh, GDEH yeh STAH-nee-tsah', 'Excuse me, where is the station?'), formal='polite')],
  alts=[('Pardon', 'pahr-DOHN', 'Pardon (casual, from French)')],
  watch='"Oprosti" is warmer and more personal than "izvini". Use it when you really want to be forgiven.',
  rel=['sorry', 'zao-mi-je', 'ne-ljuti-se', 'izvini-sto-kasnim']))

# ───────── Replies and fillers ─────────
add(E('jel-tako', "Right? / Isn't that so?", "Je l' tako?", 'yel TAH-ko', "Isn't that right?",
  [('QP', 'Filler and transition words'), ('QP', 'Agree and disagree')], ['tag question', 'agree', 'spoken'], 'casual',
  [('Checking agreement', "Lepo je, je l' tako?", 'LEH-po yeh, yel TAH-ko', "It's nice, isn't it?"),
   ('To her', "Ti si umorna, je l' tako?", 'tee see OO-mor-nah, yel TAH-ko', "You're tired, aren't you?"),
   ('About him', "On kasni, je l' tako?", 'ohn KAHS-nee, yel TAH-ko', "He's late, right?"),
   ('About us', "Vidimo se sutra, je l' tako?", 'VEE-dee-mo seh SOO-trah, yel TAH-ko', "We're meeting tomorrow, right?")],
  alts=[('Je li tako?', 'yeh lee TAH-ko', 'The fuller, slightly more careful version'), ("Je l' da?", 'yel DAH', 'Very casual: "right?"')],
  text='je l tako', rel=['zar-ne', 'tacno', 'u-pravu-si', 'slazem-se']))

add(E('zar-ne', "Isn't it? / Really?", 'Zar ne?', 'ZAHR neh', "Don't you think? Isn't it so?",
  [('QP', 'Filler and transition words'), ('QP', 'Reactions')], ['tag question', 'surprise', 'spoken'], 'neutral',
  [('Agreeing', 'Lepo je, zar ne?', 'LEH-po yeh, ZAHR neh', "It's nice, isn't it?"),
   ('Surprised at her', 'Zar nisi umorna?', 'ZAHR NEE-see OO-mor-nah', "Aren't you tired?"),
   ('About him', 'Zar on nije došao?', 'ZAHR ohn NEE-yeh DOH-shah-oh', "Hasn't he come?"),
   ('Disbelief', 'Zar stvarno?', 'ZAHR STVAHR-no', 'Really? Seriously?')],
  alts=[("Je l' tako?", 'yel TAH-ko', 'Right?'), ('Zar nije?', 'ZAHR NEE-yeh', "Isn't it?")],
  watch='At the end of a sentence "zar ne?" is a friendly "isn\'t it?". At the start ("Zar nisi…?") it shows surprise.',
  rel=['jel-tako', 'stvarno', 'salis-se', 'ma-daj']))

add(E('dakle', 'So / therefore', 'Dakle', 'DAHK-leh', 'So, in that case; starts a point or a conclusion',
  [('QP', 'Filler and transition words'), ('BA', 'Flow words')], ['filler', 'conclusion', 'flow'], 'neutral',
  [('Making a point', 'Dakle, vidimo se u osam', 'DAHK-leh, VEE-dee-mo seh oo OH-sahm', 'So, see you at eight'),
   ('To her', 'Dakle, ne dolaziš?', 'DAHK-leh, neh DOH-lah-zeesh', "So, you're not coming?"),
   ('About him', 'Dakle, on je kriv', 'DAHK-leh, ohn yeh KREEV', "So, he's the one to blame"),
   ('About us', 'Dakle, mi idemo', 'DAHK-leh, mee EE-deh-mo', "So, we're going")],
  alts=[('Znači', 'ZNAH-chee', 'So / that means (more casual)'), ('Onda', 'ON-dah', 'Then')],
  rel=['znaci', 'onda', 'uglavnom', 'zapravo']))

add(E('uglavnom', 'Anyway / mostly', 'Uglavnom', 'OO-glahv-nom', 'Anyway; mostly; in short',
  [('QP', 'Filler and transition words'), ('BA', 'Flow words')], ['filler', 'anyway', 'flow'], 'neutral',
  [('Wrapping up', 'Uglavnom, javi mi', 'OO-glahv-nom, YAH-vee mee', 'Anyway, let me know'),
   ('Mostly', 'Uglavnom sam kod kuće', 'OO-glahv-nom sahm kohd KOO-cheh', "I'm mostly at home"),
   ('About her', 'Ona uglavnom kasni', 'OH-nah OO-glahv-nom KAHS-nee', "She's mostly late"),
   ('About us', 'Uglavnom idemo u kafić', 'OO-glahv-nom EE-deh-mo oo KAH-feech', 'We mostly go to a café')],
  alts=[('U svakom slučaju', 'oo SVAH-kom SLOO-chah-yoo', 'In any case')],
  rel=['dakle', 'ipak', 'zapravo', 'znaci']))

add(E('mnogo', 'A lot / very', 'Mnogo', 'MNOH-go', 'A lot, very, many',
  [('BA', 'Flow words'), ('QP', 'Thanks, sorry, please')], ['very', 'a lot', 'emphasis'], 'neutral',
  [('Thanks', 'Hvala mnogo', 'HVAH-lah MNOH-go', 'Thanks a lot'),
   ('To her, flirty', 'Mnogo mi se sviđaš', 'MNOH-go mee seh SVEE-jahsh', 'I like you a lot'),
   ('Weather', 'Mnogo je hladno', 'MNOH-go yeh HLAHD-no', "It's very cold"),
   ('About him', 'On mnogo radi', 'ohn MNOH-go RAH-dee', 'He works a lot'),
   ('About us', 'Mnogo smo se smejali', 'MNOH-go smo seh smeh-YAH-lee', 'We laughed a lot')],
  alts=[('Puno', 'POO-no', 'A lot; very common, same idea'), ('Jako', 'YAH-ko', 'Very, strongly'), ('Baš', 'BAHSH', 'Really (casual emphasis)')],
  rel=['bas', 'hvala-puno', 'svidjas-mi-se', 'vise-nego']))

add(E('eto', 'There you go', 'Eto', 'EH-to', 'There; here you go; well then',
  [('QP', 'Filler and transition words'), ('QP', 'Common replies')], ['filler', 'handing over', 'reaction'], 'casual',
  [('Handing over', 'Eto, izvoli', 'EH-to, EEZ-vo-lee', 'Here you go'),
   ('Making a point', 'Eto, vidiš', 'EH-to, VEE-deesh', 'See? There you go'),
   ('Finding it', 'Eto ga!', 'EH-to gah', 'There he is / there it is!'),
   ('Giving in', 'Eto, u pravu si', 'EH-to, oo PRAH-voo see', "Fine, you're right")],
  alts=[('Evo', 'EH-vo', 'Here (it is); for something close to you')],
  rel=['izvolite', 'u-pravu-si', 'pa', 'aha']))

# ───────── Going out and food ─────────
add(E('idemo-na-pice', "Let's go for a drink", 'Idemo na piće', 'EE-deh-mo nah PEE-cheh', "Let's go out for a drink",
  [('ES', 'Going out'), ('CV', 'Making plans')], ['drink', 'invite', 'plans'], 'casual',
  [('To her', 'Hoćeš da izađemo na piće?', 'HOH-chesh dah ee-ZAH-jeh-mo nah PEE-cheh', 'Want to go out for a drink?'),
   ('After work', 'Idemo na piće posle posla', 'EE-deh-mo nah PEE-cheh POH-sleh POH-slah', "Let's get a drink after work"),
   ('With friends', 'Idemo svi na piće', 'EE-deh-mo svee nah PEE-cheh', 'Everyone is going for a drink'),
   ('Beer', 'Idemo na pivo', 'EE-deh-mo nah PEE-vo', "Let's get a beer")],
  alts=[('Idemo na pivo', 'EE-deh-mo nah PEE-vo', "Let's get a beer"), ('Ajde na piće', 'AY-deh nah PEE-cheh', "Come on, let's get a drink")],
  rel=['na-kafu', 'hoces-da-izadjemo', 'idemo-u-grad', 'pivo']))

add(E('hoces-da-prosetamo', 'Want to take a walk?', 'Hoćeš da prošetamo?', 'HOH-chesh dah proh-SHEH-tah-mo', 'Do you want to go for a walk together?',
  [('ES', 'Going out'), ('FR', 'Dating')], ['walk', 'invite', 'dating'], 'casual',
  [('To her', 'Hoćeš da prošetamo pored reke?', 'HOH-chesh dah proh-SHEH-tah-mo POH-red REH-keh', 'Want to walk by the river?'),
   ('Evening', 'Prošetajmo posle večere', 'proh-SHEH-tai-mo POH-sleh VEH-cheh-reh', "Let's take a walk after dinner"),
   ('Her reply', 'Hoću, daj mi pet minuta', 'HOH-choo, DAI mee PEHT mee-NOO-tah', 'Sure, give me five minutes'),
   ('About us', 'Šetamo svako veče', 'SHEH-tah-mo SVAH-ko VEH-cheh', 'We walk every evening')],
  forms=[F('Hoćeš da prošetamo?', 'HOH-chesh dah proh-SHEH-tah-mo', 'To one friend or someone your age', ('Hoćeš da prošetamo do centra?', 'HOH-chesh dah proh-SHEH-tah-mo doh TSEN-trah', 'Want to walk to the center?'), formal='casual'),
         F('Hoćete li da prošetamo?', 'HOH-cheh-teh lee dah proh-SHEH-tah-mo', 'To an elder or a group', ('Hoćete li da prošetamo posle ručka?', 'HOH-cheh-teh lee dah proh-SHEH-tah-mo POH-sleh ROOCH-kah', 'Would you like to take a walk after lunch?'), formal='polite')],
  alts=[('Idemo u šetnju', 'EE-deh-mo oo SHET-nyoo', "Let's go for a stroll"), ('Prošetajmo', 'proh-SHEH-tai-mo', "Let's walk")],
  rel=['hoces-da-izadjemo', 'idemo-na-pice', 'korzo', 'veceras']))

add(E('sta-ti-se-jede', 'What do you feel like eating?', 'Šta ti se jede?', 'SHTAH tee seh YEH-deh', 'What are you in the mood to eat?',
  [('ES', 'Food and drink'), ('CV', 'Questions')], ['food', 'mood', 'question'], 'casual',
  [('To her', 'Šta ti se jede večeras?', 'SHTAH tee seh YEH-deh VEH-cheh-rahs', 'What do you feel like eating tonight?'),
   ('About me', 'Jede mi se nešto slatko', 'YEH-deh mee seh NEHSH-to SLAHT-ko', 'I feel like something sweet'),
   ('About her', 'Njoj se jede burek', 'NYOY seh YEH-deh BOO-rek', 'She feels like burek'),
   ('A drink', 'Pije mi se kafa', 'PEE-yeh mee seh KAH-fah', 'I feel like a coffee')],
  forms=[F('Šta ti se jede?', 'SHTAH tee seh YEH-deh', 'To one friend or someone your age', ('Šta ti se jede za ručak?', 'SHTAH tee seh YEH-deh zah ROO-chahk', 'What do you feel like for lunch?'), formal='casual'),
         F('Šta vam se jede?', 'SHTAH vahm seh YEH-deh', 'To an elder, a stranger, or a group', ('Šta vam se jede, gospodine?', 'SHTAH vahm seh YEH-deh, goh-SPOH-dee-neh', 'What would you like to eat, sir?'), formal='polite'),
         F('Jede mi se…', 'YEH-deh mee seh', 'I feel like eating…', ('Jede mi se pica', 'YEH-deh mee seh PEE-tsah', 'I feel like pizza'), describes='me')],
  hint='"Jede mi se" = I feel like eating. "Pije mi se" = I feel like a drink. "Spava mi se" = I feel sleepy. The person goes in the middle: mi, ti, mu, joj, nam.',
  lit='What eats itself to you?',
  rel=['spava-mi-se', 'gladan', 'dorucak-rucak-vecera', 'idemo-na-veceru']))

# ───────── Time and weather ─────────
add(E('jutros-sinoc', 'This morning / last night', 'Jutros / sinoć', 'YOO-tros / SEE-noch', 'This morning; last night',
  [('BA', 'Time and days'), ('CV', 'Casual conversation')], ['time', 'morning', 'night'], 'neutral',
  [('About me', 'Jutros sam kasnio', 'YOO-tros sahm KAHS-nee-oh', 'I was late this morning'),
   ('To her', 'Šta si radila sinoć?', 'SHTAH see RAH-dee-lah SEE-noch', 'What did you do last night?'),
   ('About him', 'On je sinoć bio kod nas', 'ohn yeh SEE-noch BEE-oh kohd NAHS', 'He was at our place last night'),
   ('Weather', 'Jutros je bilo hladno', 'YOO-tros yeh BEE-lo HLAHD-no', 'It was cold this morning')],
  alts=[('Noćas', 'NOH-chahs', 'Tonight, or during the night'), ('Prekjuče', 'PREHK-yoo-cheh', 'The day before yesterday')],
  rel=['danas-sutra-juce', 'veceras', 'jutro-vece', 'dani']))

add(E('za-sat-vremena', 'In an hour', 'Za sat vremena', 'zah SAHT VREH-meh-nah', 'In an hour',
  [('BA', 'Time and days'), ('CV', 'Running late')], ['time', 'wait', 'late'], 'neutral',
  [('Running late', 'Stižem za sat vremena', 'STEE-zhem zah SAHT VREH-meh-nah', "I'll be there in an hour"),
   ('Food', 'Ručak je gotov za sat vremena', 'ROO-chahk yeh GOH-tov zah SAHT VREH-meh-nah', 'Lunch will be ready in an hour'),
   ('To her', 'Zovem te za sat vremena', 'ZOH-vem teh zah SAHT VREH-meh-nah', "I'll call you in an hour"),
   ('About them', 'Oni stižu za sat vremena', 'OH-nee STEE-zhoo zah SAHT VREH-meh-nah', 'They arrive in an hour')],
  alts=[('Za pola sata', 'zah POH-lah SAH-tah', 'In half an hour'), ('Za petnaest minuta', 'zah PEHT-nah-est mee-NOO-tah', 'In fifteen minutes'), ('Za dva sata', 'zah DVAH SAH-tah', 'In two hours')],
  rel=['stizem-za-pet', 'kasnim', 'koliko-je-sati', 'veceras']))

add(E('pada-kisa', "It's raining", 'Pada kiša', 'PAH-dah KEE-shah', "It's raining",
  [('DF', 'Describing things'), ('ES', 'Places')], ['weather', 'rain', 'description'], 'neutral',
  [('Texting', 'Pada kiša, kasnim malo', 'PAH-dah KEE-shah, KAHS-neem MAH-lo', "It's raining, I'm running a bit late"),
   ('To her', 'Uzmi kišobran, pada kiša', 'OOZ-mee KEE-sho-brahn, PAH-dah KEE-shah', "Take an umbrella, it's raining"),
   ('Plans', 'Ako pada kiša, ostajemo kod kuće', 'AH-ko PAH-dah KEE-shah, oh-STAH-yeh-mo kohd KOO-cheh', "If it rains, we're staying home"),
   ('Forecast', 'Sutra će padati kiša', 'SOO-trah cheh PAH-dah-tee KEE-shah', "It's going to rain tomorrow")],
  alts=[('Pljušti', 'PLYOOSH-tee', "It's pouring"), ('Pada sneg', 'PAH-dah SNEG', "It's snowing"), ('Duva vetar', 'DOO-vah VEH-tar', 'The wind is blowing')],
  ij='Pada kiša (same)', rel=['kao-iz-kabla', 'napolju-je-hladno', 'kasnim', 'ajde']))

add(E('napolju-je-hladno', "It's cold outside", 'Napolju je hladno', 'nah-POH-lyoo yeh HLAHD-no', "It's cold outside",
  [('DF', 'Describing things'), ('ES', 'Places')], ['weather', 'cold', 'warm'], 'neutral',
  [('To her', 'Obuci jaknu, napolju je hladno', 'OH-boo-tsee YAHK-noo, nah-POH-lyoo yeh HLAHD-no', "Put on a jacket, it's cold outside"),
   ('About me', 'Hladno mi je, napolju je minus', 'HLAHD-no mee yeh, nah-POH-lyoo yeh MEE-noos', "I'm cold, it's below zero outside"),
   ('Summer', 'Napolju je vruće, idemo na reku', 'nah-POH-lyoo yeh VROO-cheh, EE-deh-mo nah REH-koo', "It's hot outside, let's go to the river"),
   ('Nice day', 'Lepo je vreme, hajde da prošetamo', 'LEH-po yeh VREH-meh, HAY-deh dah proh-SHEH-tah-mo', "The weather's nice, let's go for a walk")],
  alts=[('Napolju je toplo', 'nah-POH-lyoo yeh TOH-plo', "It's warm outside"), ('Napolju je vruće', 'nah-POH-lyoo yeh VROO-cheh', "It's hot outside"), ('Sunčano je', 'SOON-chah-no yeh', "It's sunny")],
  hint='"Hladno je" describes the weather. "Hladno mi je" says YOU feel cold (the person goes in the middle: mi, ti, mu, joj).',
  ij='Vani je hladno', rel=['hladno-mi-je', 'pada-kisa', 'jutros-sinoc', 'lepo-mi-je-s-tobom']))

# ───────── Basics: colors, numbers, sizes, pronouns, this/that ─────────
add(E('koje-je-boje', 'What colour is it?', 'Koje je boje?', 'KOH-yeh yeh BOH-yeh', 'What colour is it?',
  [('BA', 'Colors'), ('CV', 'Questions')], ['color', 'question', 'describing'], 'neutral',
  [('Asking', 'Koje je boje tvoja jakna?', 'KOH-yeh yeh BOH-yeh TVOH-yah YAHK-nah', 'What colour is your jacket?'),
   ('Answering', 'Crvena je', 'TSUR-veh-nah yeh', "It's red"),
   ('Favourite', 'Koja ti je omiljena boja?', 'KOH-yah tee yeh oh-MEEL-yeh-nah BOH-yah', "What's your favourite colour?"),
   ('About me', 'Moja omiljena boja je plava', 'MOH-yah oh-MEEL-yeh-nah BOH-yah yeh PLAH-vah', 'My favourite colour is blue')],
  forms=[F('Crven je auto', 'TSUR-ven yeh OW-toh', 'Masculine thing', ('Crven je auto ispred kuće', 'TSUR-ven yeh OW-toh EES-pred KOO-cheh', 'The car in front of the house is red'), nounGender='masculine'),
         F('Crvena je jakna', 'TSUR-veh-nah yeh YAHK-nah', 'Feminine thing', ('Crvena je moja omiljena jakna', 'TSUR-veh-nah yeh MOH-yah oh-MEEL-yeh-nah YAHK-nah', 'The red one is my favourite jacket'), nounGender='feminine'),
         F('Crveno je vino', 'TSUR-veh-no yeh VEE-no', 'Neuter thing', ('Crveno je vino bolje', 'TSUR-veh-no yeh VEE-no BOH-lyeh', 'The red wine is better'), nounGender='neuter')],
  hint='Colours match the thing: crven auto, crvena jakna, crveno vino.',
  rel=['boje', 'tamno-svetlo', 'tvoj', 'veliko-malo']))

add(E('tamno-svetlo', 'Dark / light', 'Tamno / svetlo', 'TAHM-no / SVEHT-lo', 'Dark and light (colours, rooms, hair)',
  [('BA', 'Colors'), ('DF', 'People: appearance')], ['color', 'dark', 'light'], 'neutral',
  [('A dark shade', 'Tamnoplava jakna', 'tahm-no-PLAH-vah YAHK-nah', 'A dark blue jacket'),
   ('A light shade', 'Svetloplava majica', 'svet-lo-PLAH-vah MAH-ee-tsah', 'A light blue t-shirt'),
   ('A room', 'U sobi je tamno', 'oo SOH-bee yeh TAHM-no', "It's dark in the room"),
   ('About her', 'Ona ima tamnu kosu', 'OH-nah EE-mah TAHM-noo KOH-soo', 'She has dark hair')],
  alts=[('Tamna / svetla', 'TAHM-nah / SVEHT-lah', 'Dark / light (feminine)')],
  ij='svijetlo (light)', rel=['boje', 'koje-je-boje', 'veliko-malo', 'staro-novo']))

add(E('prvi-drugi-treci', 'First, second, third', 'Prvi / drugi / treći', 'PUR-vee / DROO-gee / TREH-chee', 'Ordinal numbers: first, second, third…',
  [('BA', 'Numbers'), ('BA', 'Time and days')], ['numbers', 'order', 'first'], 'neutral',
  [('Dates', 'Prvi maj je praznik', 'PUR-vee MAI yeh PRAHZ-neek', 'The first of May is a holiday'),
   ('Floors', 'Živim na trećem spratu', 'ZHEE-veem nah TREH-chem SPRAH-too', 'I live on the third floor'),
   ('To her', 'Ti si prva kojoj ovo kažem', 'tee see PUR-vah KOH-yoy OH-vo KAH-zhem', "You're the first person I'm telling this"),
   ('About us', 'Mi smo drugi na redu', 'mee smo DROO-gee nah REH-doo', "We're second in line")],
  forms=[F('Prvi / prva / prvo', 'PUR-vee / PUR-vah / PUR-vo', 'First', ('Prvi dan, prva noć, prvo veče', 'PUR-vee DAHN, PUR-vah NOHCH, PUR-vo VEH-cheh', 'First day, first night, first evening'), nounGender='masculine / feminine / neuter'),
         F('Drugi / druga / drugo', 'DROO-gee / DROO-gah / DROO-go', 'Second', ('Drugi put, druga ulica, drugo pitanje', 'DROO-gee POOT, DROO-gah OO-lee-tsah, DROO-go PEE-tah-nyeh', 'Second time, second street, second question'), nounGender='masculine / feminine / neuter'),
         F('Treći / treća / treće', 'TREH-chee / TREH-chah / TREH-cheh', 'Third', ('Treći sprat, treća vrata, treće mesto', 'TREH-chee SPRAHT, TREH-chah VRAH-tah, TREH-cheh MEH-sto', 'Third floor, third door, third place'), nounGender='masculine / feminine / neuter'),
         F('Poslednji / poslednja / poslednje', 'POH-sled-nyee / POH-sled-nyah / POH-sled-nyeh', 'Last', ('Poslednji autobus je u ponoć', 'POH-sled-nyee ow-TOH-boos yeh oo POH-noch', 'The last bus is at midnight'), nounGender='masculine / feminine / neuter')],
  alts=[('Četvrti', 'CHEH-tur-tee', 'Fourth'), ('Peti', 'PEH-tee', 'Fifth')],
  hint='After 1-4 the pattern is regular: -i / -a / -o. Say the full ordinal for dates: prvi maj, drugi januar.',
  ij='posljednji (last)', rel=['brojevi', 'dani', 'meseci', 'prvi-put']))

add(E('cena-u-dinarima', 'Prices in dinars', 'Sto pedeset dinara', 'STOH PEH-deh-set DEE-nah-rah', '150 dinars; how the word "dinar" changes with the number',
  [('BA', 'Numbers'), ('ES', 'Shopping and money')], ['price', 'dinar', 'numbers'], 'neutral',
  [('Asking the price', 'Koliko košta? Sto dvadeset dinara', 'KOH-lee-ko KOH-shtah? STOH DVAH-deh-set DEE-nah-rah', 'How much is it? 120 dinars'),
   ('Cheap', 'Samo pedeset dinara', 'SAH-mo PEH-deh-set DEE-nah-rah', 'Only 50 dinars'),
   ('Expensive', 'Dve hiljade dinara', 'DVEH HEEL-yah-deh DEE-nah-rah', 'Two thousand dinars'),
   ('One dinar', 'To košta jedan dinar', 'TOH KOH-shtah YEH-dahn DEE-nahr', 'That costs one dinar')],
  forms=[F('jedan dinar', 'YEH-dahn DEE-nahr', '1 (and 21, 31…)', ('Jedan dinar je mala para', 'YEH-dahn DEE-nahr yeh MAH-lah PAH-rah', 'One dinar is a small amount')),
         F('dva / tri / četiri dinara', 'DVAH / TREE / CHEH-tee-ree DEE-nah-rah', '2, 3 and 4 (also 22, 23, 24…)', ('Tri dinara, molim', 'TREE DEE-nah-rah, MOH-leem', 'Three dinars, please')),
         F('pet i više dinara', 'PEHT ee VEE-sheh DEE-nah-rah', '5 and up, and all the teens (11 to 14 too)', ('Dvanaest dinara je jeftino', 'DVAH-nah-est DEE-nah-rah yeh YEF-tee-no', 'Twelve dinars is cheap'))],
  hint='1 → dinar. 2 to 4 → dinara. 5 and up → dinara too. Only "jedan" and "dva" change themselves (dve with feminine words: dve hiljade).',
  ch=['plural'], rel=['koliko-kosta', 'brojevi', 'skupo', 'jeftino']))

add(E('dugacko-kratko', 'Long / short', 'Dugačak / kratak', 'DOO-gah-chahk / KRAH-tahk', 'Long and short (things, time, hair)',
  [('BA', 'Shapes and sizes'), ('DF', 'People: appearance')], ['size', 'long', 'short'], 'neutral',
  [('A thing', 'Haljina je kratka', 'HAHL-yee-nah yeh KRAHT-kah', 'The dress is short'),
   ('About her', 'Ona ima dugu kosu', 'OH-nah EE-mah DOO-goo KOH-soo', 'She has long hair'),
   ('A day', 'Dan je bio dugačak', 'DAHN yeh BEE-oh DOO-gah-chahk', 'The day was long'),
   ('A film', 'Kratak film, ali dobar', 'KRAH-tahk FEELM, AH-lee DOH-bahr', 'A short film, but a good one')],
  forms=[F('Dugačak je', 'DOO-gah-chahk yeh', 'Masculine thing', ('Ovaj put je dugačak', 'OH-vai POOT yeh DOO-gah-chahk', 'This road is long'), nounGender='masculine'),
         F('Dugačka je', 'DOO-gahch-kah yeh', 'Feminine thing', ('Dugačka je ulica', 'DOO-gahch-kah yeh OO-lee-tsah', 'The street is long'), nounGender='feminine'),
         F('Dugačko je', 'DOO-gahch-ko yeh', 'Neuter thing', ('Dugačko je putovanje', 'DOO-gahch-ko yeh poo-toh-VAH-nyeh', "It's a long trip"), nounGender='neuter')],
  alts=[('Kratak / kratka / kratko', 'KRAH-tahk / KRAHT-kah / KRAHT-ko', 'Short (m. / f. / n.)'), ('Dug / duga / dugo', 'DOOG / DOO-gah / DOO-go', 'Long (shorter form; also "for a long time")')],
  rel=['veliko-malo', 'oblici', 'staro-novo', 'visok-nizak']))

add(E('siroko-usko', 'Wide / narrow', 'Širok / uzak', 'SHEE-rok / OO-zahk', 'Wide and narrow',
  [('BA', 'Shapes and sizes'), ('DF', 'Describing things')], ['size', 'wide', 'narrow'], 'neutral',
  [('Clothes', 'Ove cipele su preuske', 'OH-veh TSEE-peh-leh soo preh-OOS-keh', 'These shoes are too tight'),
   ('About her', 'Ona ima širok osmeh', 'OH-nah EE-mah SHEE-rok OS-meh', 'She has a wide smile'),
   ('A room', 'Soba je široka', 'SOH-bah yeh SHEE-ro-kah', 'The room is wide'),
   ('A road', 'Ulica je preuska za kamion', 'OO-lee-tsah yeh preh-OOS-kah zah KAH-mee-on', 'The street is too narrow for a truck')],
  forms=[F('Širok je', 'SHEE-rok yeh', 'Masculine thing', ('Put je širok', 'POOT yeh SHEE-rok', 'The road is wide'), nounGender='masculine'),
         F('Široka je', 'SHEE-ro-kah yeh', 'Feminine thing', ('Ulica je široka', 'OO-lee-tsah yeh SHEE-ro-kah', 'The street is wide'), nounGender='feminine'),
         F('Široko je', 'SHEE-ro-ko yeh', 'Neuter thing', ('Široko je polje', 'SHEE-ro-ko yeh POH-lyeh', 'The field is wide'), nounGender='neuter')],
  alts=[('Uzak / uska / usko', 'OO-zahk / OOS-kah / OOS-ko', 'Narrow (m. / f. / n.)')],
  ij='širok / uzak (same)', rel=['dugacko-kratko', 'veliko-malo', 'oblici', 'nezgodno']))

add(E('mene-tebe', 'Me / you / him / her (as the object)', 'Mene / tebe / njega / nju', 'MEH-neh / TEH-beh / NYEH-gah / NYOO', 'The object forms of the pronouns',
  [('BA', 'Pronouns'), ('FR', 'Affection and romance')], ['pronoun', 'object', 'grammar'], 'neutral',
  [('To her', 'Volim tebe, ne njega', 'VOH-leem TEH-beh, neh NYEH-gah', 'I love you, not him'),
   ('Asking', 'Zoveš li mene ili nju?', 'ZOH-vesh lee MEH-neh EE-lee NYOO', 'Are you calling me or her?'),
   ('About them', 'Pitam njih, ne vas', 'PEE-tahm NYEEH, neh VAHS', "I'm asking them, not you (all)"),
   ('Short forms', 'Vidim te, vidiš li me?', 'VEE-deem teh, VEE-deesh lee meh', 'I see you, do you see me?')],
  forms=[F('mene / me', 'MEH-neh / meh', 'Me', ('Zovi mene, ne njega', 'ZOH-vee MEH-neh, neh NYEH-gah', 'Call me, not him'), describes='me'),
         F('tebe / te', 'TEH-beh / teh', 'You (to one person)', ('Čekam tebe', 'CHEH-kahm TEH-beh', "I'm waiting for you"), describes='you'),
         F('njega / ga', 'NYEH-gah / gah', 'Him', ('Vidim njega, ne vidim nju', 'VEE-deem NYEH-gah, neh VEE-deem NYOO', 'I see him, I do not see her'), describes='him'),
         F('nju / je', 'NYOO / yeh', 'Her', ('Pitaj nju', 'PEE-tai NYOO', 'Ask her'), describes='her'),
         F('nas / nas', 'NAHS / nahs', 'Us', ('Zovu nas na večeru', 'ZOH-voo NAHS nah VEH-cheh-roo', 'They are inviting us to dinner'), describes='us'),
         F('njih / ih', 'NYEEH / eeh', 'Them', ('Vidim njih', 'VEE-deem NYEEH', 'I see them'), describes='them')],
  hint='The short forms (me, te, ga, je, nas, ih) are the everyday ones: "volim te". The long forms (mene, tebe…) add emphasis or come after a preposition: "za tebe".',
  rel=['ja-mi', 'ti-vi', 'on-ona', 'meni-tebi']))

add(E('meni-tebi', 'To me / to you / to him / to her', 'Meni / tebi / njemu / njoj', 'MEH-nee / TEH-bee / NYEH-moo / NYOY', 'The "to someone" forms of the pronouns',
  [('BA', 'Pronouns'), ('FR', 'Affection and romance')], ['pronoun', 'dative', 'grammar'], 'neutral',
  [('To her', 'Pošalji mi sliku', 'POH-shah-lyee mee SLEE-koo', 'Send me a picture'),
   ('For her', 'Doneo sam ti kafu', 'DOH-neh-oh sahm tee KAH-foo', 'I brought you a coffee'),
   ('About him', 'Rekao sam mu istinu', 'REH-kah-oh sahm moo EES-tee-noo', 'I told him the truth'),
   ('About her', 'Pišem joj svaki dan', 'PEE-shem yoy SVAH-kee DAHN', 'I write to her every day')],
  forms=[F('meni / mi', 'MEH-nee / mee', 'To me', ('Daj mi to', 'DAI mee TOH', 'Give me that'), describes='me'),
         F('tebi / ti', 'TEH-bee / tee', 'To you', ('Šaljem ti poruku', 'SHAH-lyem tee POH-roo-koo', "I'm sending you a message"), describes='you'),
         F('njemu / mu', 'NYEH-moo / moo', 'To him', ('Dajem mu knjigu', 'DAH-yem moo KNYEE-goo', "I'm giving him a book"), describes='him'),
         F('njoj / joj', 'NYOY / yoy', 'To her', ('Kupio sam joj cveće', 'KOO-pee-oh sahm yoy TSVEH-cheh', 'I bought her flowers'), describes='her'),
         F('nama / nam', 'NAH-mah / nahm', 'To us', ('Javi nam kad stigneš', 'YAH-vee nahm kahd STEEG-nesh', 'Let us know when you arrive'), describes='us'),
         F('njima / im', 'NYEE-mah / eem', 'To them', ('Javi im da kasnimo', 'YAH-vee eem dah KAHS-nee-mo', "Tell them we're late"), describes='them')],
  hint='The short forms (mi, ti, mu, joj, nam, im) are the everyday ones and sit right after the first word: "Daj mi", "Javi mi", "Kupio sam joj".',
  rel=['mene-tebe', 'daj-mi', 'javi-se', 'ja-mi']))

add(E('ko-to-je', 'Who is that? / What is that?', 'Ko je to?', 'KOH yeh toh', 'Who is that?',
  [('BA', 'This and that'), ('CV', 'Questions')], ['question', 'this and that', 'who'], 'neutral',
  [('A photo', 'Ko je to na slici?', 'KOH yeh toh nah SLEE-tsee', "Who's that in the picture?"),
   ('At the door', 'Ko je to? Uđi', 'KOH yeh toh? OO-jee', 'Who is it? Come in'),
   ('A thing', 'Šta je ovo?', 'SHTAH yeh OH-vo', 'What is this?'),
   ('About her', 'Ko je ona?', 'KOH yeh OH-nah', 'Who is she?')],
  alts=[('Šta je to?', 'SHTAH yeh toh', 'What is that?'), ('Ko je ovaj?', 'KOH yeh OH-vai', 'Who is this (guy)?')],
  rel=['ko', 'sta', 'ovaj-taj', 'ovo-je']))

add(E('vidimo-se-u-osam', 'See you at eight', 'Vidimo se u osam', 'VEE-dee-mo seh oo OH-sahm', 'See you at eight o’clock',
  [('CV', 'Confirming plans'), ('CV', 'Making plans'), ('BA', 'Time and days')], ['time', 'plans', 'meet'], 'neutral',
  [('Confirming', 'Vidimo se u osam ispred kafića', 'VEE-dee-mo seh oo OH-sahm EES-pred KAH-fee-chah', 'See you at eight in front of the café'),
   ('Picking her up', 'Dolazim po tebe u sedam', 'doh-LAH-zeem poh TEH-beh oo SEH-dahm', "I'll pick you up at seven"),
   ('Checking', "Je l' i dalje u osam?", 'yel ee DAHL-yeh oo OH-sahm', 'Is it still at eight?'),
   ('About them', 'Oni stižu u devet', 'OH-nee STEE-zhoo oo DEH-veht', 'They arrive at nine')],
  forms=[F('Vidimo se u osam', 'VEE-dee-mo seh oo OH-sahm', 'On the hour', ('Vidimo se u osam, ne kasni', 'VEE-dee-mo seh oo OH-sahm, neh KAHS-nee', "See you at eight, don't be late")),
         F('Vidimo se u pola osam', 'VEE-dee-mo seh oo POH-lah OH-sahm', 'At 7:30 (half to eight)', ('Vidimo se u pola osam kod mene', 'VEE-dee-mo seh oo POH-lah OH-sahm kohd MEH-neh', 'See you at 7:30 at my place')),
         F('Vidimo se u osam i petnaest', 'VEE-dee-mo seh oo OH-sahm ee PEHT-nah-est', 'At 8:15', ('Vidimo se u osam i petnaest', 'VEE-dee-mo seh oo OH-sahm ee PEHT-nah-est', 'See you at 8:15')),
         F('Vidimo se u petnaest do osam', 'VEE-dee-mo seh oo PEHT-nah-est doh OH-sahm', 'At 7:45', ('Vidimo se u petnaest do osam', 'VEE-dee-mo seh oo PEHT-nah-est doh OH-sahm', 'See you at 7:45'))],
  watch='"U pola osam" means HALF TO eight, so 7:30, not 8:30. It is a very easy slip. Say "u osam i trideset" if you want to be unmistakable.',
  rel=['u-koliko-sati', 'dogovoreno', 'koliko-je-sati', 'javi-ako-se-promeni']))

add(E('javi-ako-se-promeni', 'Let me know if anything changes', 'Javi mi ako se nešto promeni', 'YAH-vee mee AH-ko seh NEHSH-to proh-MEH-nee', 'Let me know if anything changes',
  [('CV', 'Confirming plans'), ('CV', 'Cancelling')], ['plans', 'update', 'request'], 'neutral',
  [('To her', 'Javi mi ako se plan promeni', 'YAH-vee mee AH-ko seh PLAHN proh-MEH-nee', 'Let me know if the plan changes'),
   ('Promise', 'Javiću ti ako se nešto promeni', 'YAH-vee-choo tee AH-ko seh NEHSH-to proh-MEH-nee', "I'll tell you if anything changes"),
   ('Weather', 'Javi ako počne kiša', 'YAH-vee AH-ko POHCH-neh KEE-shah', 'Let me know if it starts raining'),
   ('Running late', 'Javi mi ako kasniš', 'YAH-vee mee AH-ko KAHS-neesh', "Let me know if you're running late")],
  forms=[F('Javi mi ako se nešto promeni', 'YAH-vee mee AH-ko seh NEHSH-to proh-MEH-nee', 'To one friend or someone your age', ('Javi mi ako se nešto promeni do petka', 'YAH-vee mee AH-ko seh NEHSH-to proh-MEH-nee doh PET-kah', 'Let me know if anything changes by Friday'), formal='casual'),
         F('Javite mi ako se nešto promeni', 'YAH-vee-teh mee AH-ko seh NEHSH-to proh-MEH-nee', 'To an elder, a stranger, or a group', ('Javite mi ako se nešto promeni, molim vas', 'YAH-vee-teh mee AH-ko seh NEHSH-to proh-MEH-nee, MOH-leem vahs', 'Please let me know if anything changes'), formal='polite')],
  rel=['javi-se', 'dogovoreno', 'vidimo-se-u-osam', 'moze-li-drugi-dan']))

# ───────── Comparisons, dating, slang ─────────
add(E('najbolji', 'The best', 'Najbolji / najbolja / najbolje', 'NAI-bohl-yee / NAI-bohl-yah / NAI-bohl-yeh', 'The best',
  [('DF', 'Comparisons'), ('DF', 'Opinions')], ['best', 'compliment', 'comparison'], 'neutral',
  [('To her', 'Ti si najbolja', 'tee see NAI-bohl-yah', "You're the best"),
   ('About him', 'On je najbolji', 'ohn yeh NAI-bohl-yee', "He's the best"),
   ('A thing', 'Ovo je najbolja kafa u gradu', 'OH-vo yeh NAI-bohl-yah KAH-fah oo GRAH-doo', "This is the best coffee in town"),
   ('About us', 'Mi smo najbolji tim', 'mee smo NAI-bohl-yee TEEM', "We're the best team")],
  forms=[F('Najbolji je', 'NAI-bohl-yee yeh', 'Masculine thing, or a man', ('Ovo je najbolji burek', 'OH-vo yeh NAI-bohl-yee BOO-rek', 'This is the best burek'), nounGender='masculine'),
         F('Najbolja je', 'NAI-bohl-yah yeh', 'Feminine thing, or a woman', ('Ona je najbolja drugarica', 'OH-nah yeh NAI-bohl-yah droo-GAH-ree-tsah', 'She is the best friend'), nounGender='feminine'),
         F('Najbolje je', 'NAI-bohl-yeh yeh', 'Neuter thing, or the best option', ('Najbolje je da ostanemo kod kuće', 'NAI-bohl-yeh yeh dah oh-STAH-neh-mo kohd KOO-cheh', 'The best thing is to stay home'), nounGender='neuter')],
  hint='Add "naj-" in front of the comparative: bolji → najbolji, lepši → najlepši, veći → najveći.',
  rel=['bolje', 'dobro-lose', 'svaka-cast', 'skuplje-jeftinije']))

add(E('skuplje-jeftinije', 'More expensive / cheaper', 'Skuplje / jeftinije', 'SKOOP-lyeh / YEF-tee-nee-yeh', 'More expensive; cheaper',
  [('DF', 'Comparisons'), ('ES', 'Shopping and money')], ['price', 'comparison', 'shopping'], 'neutral',
  [('Comparing', 'Ovo je skuplje nego ono', 'OH-vo yeh SKOOP-lyeh NEH-go OH-no', 'This is more expensive than that'),
   ('In a shop', 'Imate li nešto jeftinije?', 'EE-mah-teh lee NEHSH-to YEF-tee-nee-yeh', 'Do you have anything cheaper?'),
   ('Eating out', 'Ovde je jeftinije', 'OHV-deh yeh YEF-tee-nee-yeh', "It's cheaper here"),
   ('To her', 'Skuplje je nego što misliš', 'SKOOP-lyeh yeh NEH-go shtoh MEE-sleesh', "It's more expensive than you think")],
  alts=[('Najskuplje', 'NAI-skoop-lyeh', 'The most expensive'), ('Najjeftinije', 'nai-YEF-tee-nee-yeh', 'The cheapest')],
  rel=['skupo', 'jeftino', 'koliko-kosta', 'vise-nego']))

add(E('tvoj-broj', 'Can I get your number?', 'Daj mi svoj broj', 'DAI mee svoy BROY', 'Give me your number',
  [('FR', 'Dating'), ('CV', 'Getting to know someone')], ['number', 'phone', 'dating'], 'casual',
  [('Asking', 'Možeš li da mi daš svoj broj?', 'MOH-zhesh lee dah mee DAHSH svoy BROY', 'Can you give me your number?'),
   ('Texting first', 'Ovo je moj broj', 'OH-vo yeh moy BROY', 'This is my number'),
   ('Saving it', 'Sačuvaj moj broj', 'sah-CHOO-vai moy BROY', 'Save my number')],
  forms=[F('Daj mi svoj broj', 'DAI mee svoy BROY', 'To her, casual', ('Daj mi svoj broj da ti pišem', 'DAI mee svoy BROY dah tee PEE-shem', 'Give me your number so I can text you'), describes='her'),
         F('Koji ti je broj?', 'KOH-yee tee yeh BROY', 'Asking neutrally', ('Koji ti je broj telefona?', 'KOH-yee tee yeh BROY teh-leh-FOH-nah', "What's your phone number?"), describes='you'),
         F('Evo mog broja', 'EH-vo mohg BROH-yah', 'Giving yours', ('Evo mog broja, javi se', 'EH-vo mohg BROH-yah, YAH-vee seh', "Here's my number, get in touch"), describes='me')],
  alts=[('Imaš li Viber?', 'EE-mahsh lee VEE-ber', 'Do you have Viber? (very common in Serbia)')],
  rel=['javi-se', 'kako-se-zoves', 'kad-si-slobodna', 'hocu-da-te-vidim']))

add(E('drska-si', "You're cheeky", 'Drska si', 'DUR-skah see', "You're cheeky; you've got nerve",
  [('SS', 'Playful insults'), ('FR', 'Playful teasing')], ['teasing', 'cheeky', 'playful'], 'casual',
  [('Teasing her', 'Drska si, ali mi se sviđa', 'DUR-skah see, AH-lee mee seh SVEE-jah', "You're cheeky, but I like it"),
   ('Owning it (man)', 'Znam, drzak sam', 'znahm, DUR-zahk sahm', "I know, I'm cheeky (a man says this)"),
   ('Owning it (woman)', 'Znam, drska sam', 'znahm, DUR-skah sahm', "I know, I'm cheeky (a woman says this)")],
  forms=[F('Drska si', 'DUR-skah see', 'Teasing her', ('Drska si, ali slatka', 'DUR-skah see, AH-lee SLAHT-kah', "You're cheeky, but sweet"), describes='her'),
         F('Drzak si', 'DUR-zahk see', 'Teasing a man', ('Drzak si, brate', 'DUR-zahk see, BRAH-teh', "You've got nerve, man"), describes='him'),
         F('Drzak sam', 'DUR-zahk sahm', 'A man about himself', ('Možda sam drzak, ali iskren', 'MOHZH-dah sahm DUR-zahk, AH-lee EES-kren', "Maybe I'm bold, but honest"), speaker='male'),
         F('Drska sam', 'DUR-skah sahm', 'A woman about herself', ('Možda sam drska, ali iskrena', 'MOHZH-dah sahm DUR-skah, AH-lee EES-kreh-nah', "Maybe I'm bold, but honest"), speaker='female'),
         F('Drzak je / drska je', 'DUR-zahk yeh / DUR-skah yeh', 'About someone else', ('Moj brat je drzak', 'moy BRAHT yeh DUR-zahk', 'My brother is cheeky'), describes='him / her')],
  watch='"Drzak" can be a real insult if said seriously (rude, disrespectful). With a smile and the right tone it is teasing.',
  rel=['zezas-me', 'luda-si', 'nemoguc-sam', 'budala']))

add(E('kapiram', 'I get it', 'Kapiram', 'kah-PEE-rahm', 'I get it, I catch your meaning',
  [('SS', 'Reactions'), ('SS', 'Casual slang'), ('QP', 'Common replies')], ['understand', 'slang', 'reply'], 'slang',
  [('Got it', 'Aha, kapiram', 'AH-hah, kah-PEE-rahm', 'Ah, I get it'),
   ('Asking her', 'Kapiraš li?', 'kah-PEE-rahsh lee', 'Do you get it?'),
   ('Not getting it', 'Ne kapiram', 'neh kah-PEE-rahm', "I don't get it"),
   ('About him', 'On ne kapira', 'ohn neh kah-PEE-rah', "He doesn't get it")],
  forms=[F('Kapiram', 'kah-PEE-rahm', 'About me', ('Kapiram šta hoćeš da kažeš', 'kah-PEE-rahm SHTAH HOH-chesh dah KAH-zhesh', 'I get what you mean'), describes='me'),
         F('Kapiraš', 'kah-PEE-rahsh', 'About her', ('Kapiraš brzo', 'kah-PEE-rahsh BUR-zo', 'You catch on fast'), describes='her'),
         F('Kapira', 'kah-PEE-rah', 'About someone else', ('Ona sve kapira', 'OH-nah SVEH kah-PEE-rah', 'She gets everything'), describes='him / her')],
  alts=[('Razumem', 'rah-ZOO-mem', 'I understand (neutral, fine for anyone)')],
  watch='Casual slang. Fine with friends; with elders or in formal settings say "razumem".',
  rel=['razumem', 'aha', 'znaci', 'nemam-pojma']))

add(E('fora', 'Cool / a good one', 'Fora', 'FOH-rah', 'Cool, a neat trick, a good joke',
  [('SS', 'Reactions'), ('SS', 'Casual slang')], ['cool', 'slang', 'joke'], 'slang',
  [('Cool', 'To je fora!', 'toh yeh FOH-rah', "That's cool!"),
   ('A good joke', 'Dobra fora', 'DOH-brah FOH-rah', 'Good one'),
   ('A place', 'Ovaj kafić je fora', 'OH-vai KAH-feech yeh FOH-rah', 'This café is cool'),
   ('About her', 'Ona je fora', 'OH-nah yeh FOH-rah', "She's cool")],
  alts=[('Super', 'SOO-per', 'Great, cool (more neutral)'), ('Ludilo', 'LOO-dee-lo', 'Wild, awesome')],
  watch='Slang. Use it with friends; it can sound too casual for elders or formal situations.',
  rel=['cool', 'ludilo', 'bezveze', 'svaka-cast']))

add(E('jao', 'Oh no / wow / ouch', 'Jao', 'YAH-oh', 'Oh no, wow, ouch',
  [('SS', 'Reactions'), ('QP', 'Reactions')], ['reaction', 'surprise', 'pain'], 'casual',
  [('Pain', 'Jao, boli me!', 'YAH-oh, BOH-lee meh', 'Ow, it hurts!'),
   ('Awe', 'Jao, kako je lepo!', 'YAH-oh, KAH-ko yeh LEH-po', 'Wow, how beautiful!'),
   ('Oh no (woman)', 'Jao, zaboravila sam!', 'YAH-oh, zah-boh-RAH-vee-lah sahm', 'Oh no, I forgot! (a woman says this)'),
   ('Oh no (man)', 'Jao, zaboravio sam!', 'YAH-oh, zah-boh-RAH-vee-oh sahm', 'Oh no, I forgot! (a man says this)')],
  alts=[('Joj', 'YOY', 'Oh my / aw / ouch (very similar)'), ('Majko', 'MAHY-ko', 'Oh my goodness (literally "mother")')],
  rel=['joj', 'ludilo', 'boze-moj', 'ma-daj']))

# ───────── Words used by the new entries (meaning, note, tags). Pronunciation is harvested from the sentences. ─────────
NEW_WORDS = {}

def merge():
    data = json.load(open('src/data/entries.json', encoding='utf8')); by = {e['id']: e for e in data}; added = []
    for e in NEW:
        if e['id'] in by: continue
        data.append(e); by[e['id']] = e; added.append(e['id'])
    for e in data:
        e['related'] = [r for r in e['related'] if r in by and r != e['id']]
    for i in added:  # link both ways (cap 8 so nothing balloons)
        for r in by[i]['related']:
            if i not in by[r]['related'] and len(by[r]['related']) < 8: by[r]['related'].append(i)
    json.dump(data, open('src/data/entries.json', 'w', encoding='utf8'), ensure_ascii=False, indent=2)
    open('src/data/entries.json', 'a').write('\n')
    return added

if __name__ == '__main__':
    added = merge()
    print('added', len(added), 'entries:', ', '.join(added))
