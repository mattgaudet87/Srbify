"""Batch 2 of promoting alternatives to their own entries (~49 entries). Idempotent.
Run: python3 scripts/content_alts2.py, then harvest_missing.py / glossary / build_words / checks (see CLAUDE.md)."""
import os, sys
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
sys.path.insert(0, os.path.join(root, 'scripts', 'archive')); import content_sweep as c
os.chdir(root)
E, F = c.E, c.F
NEW = []; add = NEW.append
CAS, POL = 'To one friend or someone your age', 'To an elder, a stranger, or a group'

# ───── Reactions, replies, slang ─────
add(E('kul', 'Cool', 'Kul', 'KOOL', "Cool; straight from English 'cool'",
  [('SS', 'Casual slang'), ('QP', 'Reactions')], ['cool', 'slang', 'approval'], 'slang',
  [('About a place', 'Ovaj kafić je kul', 'OH-vai KAH-feech yeh KOOL', 'This café is cool'),
   ('To her', 'Kul si', 'KOOL see', "You're cool"),
   ('Agreeing', 'Kul, vidimo se u osam', 'KOOL, VEE-dee-mo seh oo OH-sahm', 'Cool, see you at eight'),
   ('About them', 'Njeni prijatelji su kul', 'NYEH-nee PREE-yah-teh-lyee soo KOOL', 'Her friends are cool')],
  alts=[('Odlično', 'od-LEECH-no', 'Excellent; more polished'), ('Super', 'SOO-per', 'Great'), ('Fora', 'FOH-rah', 'Cool; a good one')],
  watch='Slang borrowed from English. Fine with friends and in texts; skip it with elders.', rel=['cool', 'odlicno', 'fora', 'faca']))

add(E('odlicno', 'Excellent', 'Odlično', 'od-LEECH-no', 'Excellent, great, wonderful',
  [('QP', 'Reactions'), ('QP', 'Common replies')], ['great', 'approval', 'reply'], 'neutral',
  [('Reply', 'Odlično, vidimo se sutra', 'od-LEECH-no, VEE-dee-mo seh SOO-trah', 'Excellent, see you tomorrow'),
   ('To her', 'Odlično izgledaš', 'od-LEECH-no EEZ-gleh-dahsh', 'You look great'),
   ('About me', 'Osećam se odlično', 'oh-SEH-tsahm seh od-LEECH-no', 'I feel great'),
   ('About a place', 'Hrana je odlična', 'HRAH-nah yeh od-LEECH-nah', 'The food is excellent')],
  alts=[('Super', 'SOO-per', 'Great, more casual'), ('Sjajno', 'SYAI-no', 'Wonderful, brilliant')],
  rel=['cool', 'kul', 'super', 'svaka-cast']))

add(E('faca', 'Awesome / badass', 'Faca', 'FAH-tsah', "Awesome, badass (literally 'knife')",
  [('SS', 'Casual slang'), ('QP', 'Reactions')], ['awesome', 'slang', 'compliment'], 'slang',
  [('To her', 'Faca si', 'FAH-tsah see', "You're awesome"),
   ('About him', 'On je faca', 'ohn yeh FAH-tsah', "He's a legend"),
   ('A place', 'Ova svirka je faca', 'OH-vah SVEER-kah yeh FAH-tsah', 'This gig is awesome'),
   ('About us', 'Mi smo faca ekipa', 'mee smo FAH-tsah eh-KEE-pah', "We're an awesome crew")],
  alts=[('Kul', 'KOOL', 'Cool'), ('Ludilo', 'LOO-dee-lo', 'Wild, awesome')], lit='Knife',
  watch='Slang. It is a compliment, but only with friends your age.', rel=['kul', 'cool', 'ludilo', 'fora']))

add(E('kako-ide', "How's it going?", 'Kako ide?', 'KAH-ko EE-deh', "How's it going?",
  [('QP', 'Greetings and goodbyes'), ('QP', 'Conversation starters')], ['greeting', 'how are you', 'casual'], 'casual',
  [('Greeting', 'Ej, kako ide?', 'AY, KAH-ko EE-deh', "Hey, how's it going?"),
   ('Reply', 'Ide, ide, a kod tebe?', 'EE-deh, EE-deh, ah kohd TEH-beh', "Going, going, and with you?"),
   ('About work', 'Kako ide posao?', 'KAH-ko EE-deh POH-sah-oh', "How's work going?"),
   ('About her studies', 'Kako ide učenje srpskog?', 'KAH-ko EE-deh OO-cheh-nyeh SUR-pskog', "How's learning Serbian going?")],
  alts=[('Šta ima?', 'SHTAH EE-mah', "What's up?"), ('Kako si?', 'KAH-ko see', 'How are you?')],
  rel=['kako-si', 'sta-ima', 'sta-ima-novo', 'dobro-sam']))

add(E('cujemo-se', "We'll talk", 'Čujemo se', 'CHOO-yeh-mo seh', "Talk soon; we'll be in touch (phone or text)",
  [('QP', 'Greetings and goodbyes'), ('CV', 'Confirming plans')], ['goodbye', 'talk', 'texting'], 'casual',
  [('Signing off', 'Čujemo se kasnije', 'CHOO-yeh-mo seh KAHS-nee-yeh', "Talk later"),
   ('To her', 'Čujemo se večeras', 'CHOO-yeh-mo seh VEH-cheh-rahs', "Let's talk tonight"),
   ('Plans', 'Čujemo se pre vikenda', 'CHOO-yeh-mo seh PREH VEE-ken-dah', "We'll talk before the weekend")],
  alts=[('Vidimo se', 'VEE-dee-mo seh', 'See you'), ('Javi se', 'YAH-vee seh', 'Get in touch')],
  watch='"Čujemo se" means you will talk by phone or text. "Vidimo se" means you will actually meet.', lit='We hear each other',
  rel=['see-you', 'javi-se', 'ajde', 'dogovoreno']))

add(E('hajde-da', "Let's…", 'Hajde da…', 'HAY-deh dah', "Let's…; come on, let's…",
  [('VA', 'Invitations'), ('CV', 'Making plans')], ['lets', 'invite', 'suggest'], 'casual',
  [('Suggesting', 'Hajde da idemo na kafu', 'HAY-deh dah EE-deh-mo nah KAH-foo', "Let's go for a coffee"),
   ('To her', 'Hajde da se vidimo sutra', 'HAY-deh dah seh VEE-dee-mo SOO-trah', "Let's meet tomorrow"),
   ('Encouraging', 'Hajde, probaj', 'HAY-deh, PROH-bai', 'Come on, try it')],
  forms=[F('Hajde da…', 'HAY-deh dah', CAS, ('Hajde da prošetamo', 'HAY-deh dah proh-SHEH-tah-mo', "Let's go for a walk"), formal='casual'),
         F('Hajdete da…', 'HAY-deh-teh dah', POL, ('Hajdete da probamo', 'HAY-deh-teh dah PROH-bah-mo', "Let's try (to a group)"), formal='polite'),
         F('Hajdemo da…', 'HAY-deh-mo dah', 'Us', ('Hajdemo da jedemo', 'HAY-deh-mo dah YEH-deh-mo', "Let's eat"), describes='us')],
  alts=[('Ajde', 'AY-deh', 'Short and very casual'), ('Idemo', 'EE-deh-mo', "Let's go")],
  rel=['ajde', 'idemo-u-grad', 'idemo-na-pice', 'na-kafu']))

add(E('zaista', 'Truly? / Really?', 'Zaista?', 'ZAH-ee-stah', 'Truly; really (a bit more formal than "stvarno")',
  [('QP', 'Reactions'), ('QP', 'Common replies')], ['surprise', 'really', 'formal'], 'neutral',
  [('Surprised', 'Zaista? Nisam znao', 'ZAH-ee-stah? NEE-sahm ZNAH-oh', "Really? I didn't know"),
   ('Meaning it', 'Zaista mi je žao', 'ZAH-ee-stah mee yeh ZHAH-oh', "I'm truly sorry"),
   ('To her', 'Zaista si divna', 'ZAH-ee-stah see DEEV-nah', "You're truly wonderful")],
  alts=[('Stvarno?', 'STVAHR-no', 'Really? (everyday)'), ('Ozbiljno?', 'OHZ-byl-no', 'Seriously?')],
  rel=['stvarno', 'ozbiljno', 'zar-ne', 'salis-se']))

add(E('ozbiljno', 'Seriously?', 'Ozbiljno?', 'OHZ-bee-lyno', 'Seriously? Are you serious?',
  [('QP', 'Reactions'), ('QP', 'Common replies')], ['surprise', 'seriously', 'disbelief'], 'casual',
  [('Disbelief', 'Ozbiljno? Sad?', 'OHZ-bee-lyno? SAHD', 'Seriously? Now?'),
   ('To her', 'Ozbiljno ti kažem', 'OHZ-bee-lyno tee KAH-zhem', "I'm telling you seriously"),
   ('About him', 'On je ozbiljan', 'ohn yeh OHZ-bee-lyahn', "He's serious"),
   ('Checking', 'Jesi li ozbiljna?', 'YEH-see lee OHZ-bee-lyah-nah', 'Are you serious? (to her)')],
  alts=[('Stvarno?', 'STVAHR-no', 'Really?'), ('Zaista?', 'ZAH-ee-stah', 'Truly?')],
  rel=['stvarno', 'zaista', 'salis-se', 'ma-daj']))

add(E('valjda', 'I guess / hopefully', 'Valjda', 'VAHL-dah', 'I guess; hopefully; presumably',
  [('QP', 'Yes, no, maybe'), ('QP', 'Filler and transition words')], ['guess', 'hope', 'maybe'], 'casual',
  [('Hoping', 'Valjda dolaziš?', 'VAHL-dah DOH-lah-zeesh', "You're coming, I hope?"),
   ('Guessing', 'Valjda je tako', 'VAHL-dah yeh TAH-ko', "I guess that's so"),
   ('About me', 'Valjda ću stići na vreme', 'VAHL-dah choo STEE-chee nah VREH-meh', "I'll make it on time, I hope"),
   ('About them', 'Valjda su već stigli', 'VAHL-dah soo vuhch STEEG-lee', 'They must have arrived by now')],
  alts=[('Možda', 'MOHZH-dah', 'Maybe'), ('Verovatno', 'veh-ROH-vaht-no', 'Probably')],
  rel=['mozda', 'verovatno', 'sigurno', 'sumnjam']))

add(E('nema-problema', 'No problem', 'Nema problema', 'NEH-mah proh-BLEH-mah', 'No problem',
  [('QP', 'Common replies'), ('QP', 'Thanks, sorry, please')], ['no problem', 'reply', 'okay'], 'casual',
  [('Replying to thanks', 'Hvala! Nema problema', 'HVAH-lah! NEH-mah proh-BLEH-mah', 'Thanks! No problem'),
   ('To her', 'Nema problema, čekam te', 'NEH-mah proh-BLEH-mah, CHEH-kahm teh', "No problem, I'll wait for you"),
   ('Making plans', 'Nema problema, može sutra', 'NEH-mah proh-BLEH-mah, MOH-zheh SOO-trah', 'No problem, tomorrow works')],
  alts=[('Nema frke', 'NEH-mah FUR-keh', 'No worries (casual)'), ('Nema veze', 'NEH-mah VEH-zeh', "Never mind, no worries")],
  text='nema problema / ntp', rel=['ntp', 'nema-veze', 'ne-brini', 'nema-na-cemu']))

add(E('tako-je', "That's right", 'Tako je', 'TAH-ko yeh', "That's right; exactly so",
  [('QP', 'Agree and disagree'), ('QP', 'Common replies')], ['agree', 'right', 'confirm'], 'neutral',
  [('Agreeing', 'Tako je, u pravu si', 'TAH-ko yeh, oo PRAH-voo see', "That's right, you're right"),
   ('Confirming', 'Tako je, to sam i mislio', 'TAH-ko yeh, toh sahm ee MEE-slee-oh', "Exactly, that's what I thought (a man says this)"),
   ('Closing', 'Tako je to', 'TAH-ko yeh toh', "That's how it is")],
  alts=[('Tačno', 'TAHCH-no', 'Exactly'), ('Upravo tako', 'oo-PRAH-vo TAH-ko', 'Precisely so (more formal)')],
  rel=['tacno', 'u-pravu-si', 'slazem-se', 'naravno']))

add(E('kunem-se', 'I swear', 'Kunem se', 'KOO-nem seh', 'I swear',
  [('QP', 'Common replies'), ('CE', 'Common sayings')], ['swear', 'honest', 'emphasis'], 'casual',
  [('Convincing her', 'Kunem ti se, nisam znao', 'KOO-nem tee seh, NEE-sahm ZNAH-oh', "I swear to you, I didn't know (a man says this)"),
   ('Her side', 'Kunem se, nisam znala', 'KOO-nem seh, NEE-sahm ZNAH-lah', "I swear, I didn't know (a woman says this)"),
   ('About a promise', 'Kunem se da ću doći', 'KOO-nem seh dah choo DOH-chee', 'I swear I will come')],
  alts=[('Majke mi', 'MAHY-keh mee', "I swear (on my mother's life)"), ('Iskreno', 'EES-kreh-no', 'Honestly')],
  rel=['majke-mi', 'iskreno', 'nisam-to-rekao', 'stvarno']))

add(E('iskreno', 'Honestly', 'Iskreno', 'EES-kreh-no', 'Honestly, frankly',
  [('QP', 'Filler and transition words'), ('CV', 'Casual conversation')], ['honest', 'opinion', 'filler'], 'neutral',
  [('Opinion', 'Iskreno, ne znam', 'EES-kreh-no, neh ZNAHM', "Honestly, I don't know"),
   ('To her', 'Iskreno, sviđaš mi se', 'EES-kreh-no, SVEE-jahsh mee seh', 'Honestly, I like you'),
   ('About him', 'Iskreno, on je u pravu', 'EES-kreh-no, ohn yeh oo PRAH-voo', 'Honestly, he is right'),
   ('Describing', 'Ona je iskrena', 'OH-nah yeh EES-kreh-nah', 'She is honest')],
  alts=[('Kunem se', 'KOO-nem seh', 'I swear'), ('Otvoreno', 'OHT-voh-reh-no', 'Openly, frankly')],
  rel=['kunem-se', 'majke-mi', 'zapravo', 'u-stvari']))

# ───── Flirting and affection ─────
add(E('prelepa-si', "You're gorgeous", 'Prelepa si', 'preh-LEH-pah see', "You're gorgeous (stronger than lepa si)",
  [('FR', 'Compliments'), ('FR', 'Flirting')], ['compliment', 'beautiful', 'flirty'], 'casual',
  [('To her', 'Prelepa si večeras', 'preh-LEH-pah see VEH-cheh-rahs', "You're gorgeous tonight"),
   ('With a photo', 'Prelepa si na slici', 'preh-LEH-pah see nah SLEE-tsee', "You look gorgeous in the picture"),
   ('About a place', 'Prelep je ovaj grad', 'PREH-lep yeh OH-vai GRAHD', 'This city is beautiful')],
  forms=[F('Prelepa si', 'preh-LEH-pah see', 'To her', ('Prelepa si, znaš li to?', 'preh-LEH-pah see, ZNAHSH lee toh', "You're gorgeous, do you know that?"), describes='her'),
         F('Prelep si', 'PREH-lep see', 'To a man', ('Prelep si u tom odelu', 'PREH-lep see oo TOHM OH-deh-loo', "You look great in that suit"), describes='him'),
         F('Prelepa je', 'preh-LEH-pah yeh', 'About her', ('Njena sestra je prelepa', 'NYEH-nah SEH-strah yeh preh-LEH-pah', 'Her sister is gorgeous'), describes='her')],
  alts=[('Lepa si', 'LEH-pah see', "You're beautiful"), ('Divna si', 'DEEV-nah see', "You're wonderful")],
  rel=['lepa-si', 'izgledas-lepo', 'slatka-si', 'preslatka-si']))

add(E('preslatka-si', "You're so cute", 'Preslatka si', 'preh-SLAHT-kah see', "You're so cute / so sweet",
  [('FR', 'Compliments'), ('FR', 'Playful teasing')], ['compliment', 'cute', 'sweet'], 'casual',
  [('To her', 'Preslatka si kad se smeješ', 'preh-SLAHT-kah see kahd seh SMEH-yesh', "You're so cute when you laugh"),
   ('A message', 'Preslatka si, hvala ti', 'preh-SLAHT-kah see, HVAH-lah tee', "You're so sweet, thank you"),
   ('About a thing', 'Ova mala je preslatka', 'OH-vah MAH-lah yeh preh-SLAHT-kah', 'This little one is adorable')],
  forms=[F('Preslatka si', 'preh-SLAHT-kah see', 'To her', ('Preslatka si, ljubavi', 'preh-SLAHT-kah see, LYOO-bah-vee', "You're so cute, love"), describes='her'),
         F('Presladak si', 'preh-SLAH-dahk see', 'To a man', ('Presladak si, brate', 'preh-SLAH-dahk see, BRAH-teh', "You're so sweet, man"), describes='him')],
  alts=[('Slatka si', 'SLAHT-kah see', "You're cute / sweet"), ('Draga si', 'DRAH-gah see', "You're dear")],
  rel=['slatka-si', 'prelepa-si', 'lepa-si', 'zlato-sunce']))

add(E('obozavam-te', 'I adore you', 'Obožavam te', 'oh-boh-ZHAH-vahm teh', 'I adore you',
  [('FR', 'Affection and romance'), ('FR', 'I like you')], ['adore', 'love', 'sweet'], 'casual',
  [('To her', 'Obožavam te, znaš to', 'oh-boh-ZHAH-vahm teh, ZNAHSH toh', 'I adore you, you know that'),
   ('About her laugh', 'Obožavam tvoj smeh', 'oh-boh-ZHAH-vahm tvoy SMEH', 'I adore your laugh'),
   ('A thing', 'Obožavam burek', 'oh-boh-ZHAH-vahm BOO-rek', 'I adore burek')],
  forms=[F('Obožavam te', 'oh-boh-ZHAH-vahm teh', 'To her', ('Obožavam te, nasmejavaš me', 'oh-boh-ZHAH-vahm teh, nah-smeh-YAH-vahsh meh', 'I adore you, you make me laugh'), describes='her'),
         F('Obožavaš li me?', 'oh-boh-ZHAH-vahsh lee meh', 'Asking her', ('Obožavaš li me bar malo?', 'oh-boh-ZHAH-vahsh lee meh BAHR MAH-lo', 'Do you adore me at least a little?'), describes='me'),
         F('Obožava te', 'oh-boh-ZHAH-vah teh', 'Someone else adores you', ('Moja mama te obožava', 'MOH-yah MAH-mah teh oh-boh-ZHAH-vah', 'My mom adores you'), describes='him / her'),
         F('Obožavamo te', 'oh-boh-ZHAH-vah-mo teh', 'We adore you', ('Obožavamo te, vrati se', 'oh-boh-ZHAH-vah-mo teh, VRAH-tee seh', 'We adore you, come back'), describes='us')],
  rel=['volim-te', 'mnogo-te-volim', 'svidjas-mi-se', 'ljubim-te']))

add(E('mnogo-te-volim', 'I love you a lot', 'Mnogo te volim', 'MNOH-go teh VOH-leem', 'I love you a lot',
  [('FR', 'Affection and romance'), ('FR', 'Relationship talk')], ['love', 'a lot', 'sweet'], 'casual',
  [('To her', 'Mnogo te volim', 'MNOH-go teh VOH-leem', 'I love you a lot'),
   ('Texting', 'Laku noć, mnogo te volim', 'LAH-koo NOHCH, MNOH-go teh VOH-leem', 'Good night, I love you a lot'),
   ('About family', 'Mnogo volim svoju porodicu', 'MNOH-go VOH-leem SVOH-yoo poh-roh-DEE-tsoo', 'I love my family a lot')],
  forms=[F('Mnogo te volim', 'MNOH-go teh VOH-leem', 'To her', ('Mnogo te volim, ne zaboravi to', 'MNOH-go teh VOH-leem, neh zah-boh-RAH-vee toh', "I love you a lot, don't forget it"), describes='her'),
         F('I ja tebe mnogo volim', 'ee yah TEH-beh MNOH-go VOH-leem', 'Her answer: "I love you a lot too"', ('I ja tebe mnogo volim', 'ee yah TEH-beh MNOH-go VOH-leem', 'I love you a lot too'), describes='me'),
         F('Mnogo vas volim', 'MNOH-go vahs VOH-leem', 'Polite or a group', ('Mnogo vas volim, deco', 'MNOH-go vahs VOH-leem, DEH-tso', 'I love you all a lot, kids'), formal='polite')],
  alts=[('Volim te', 'VOH-leem teh', 'I love you'), ('Obožavam te', 'oh-boh-ZHAH-vahm teh', 'I adore you')],
  rel=['volim-te', 'obozavam-te', 'ljubim-te', 'nedostajes-mi']))

add(E('duso', 'Darling (pet name)', 'Dušo', 'DOO-sho', "Darling; sweetheart (literally 'soul')",
  [('FR', 'Nicknames and pet names'), ('FR', 'Affection and romance')], ['pet name', 'sweet', 'darling'], 'casual',
  [('To her', 'Dobro jutro, dušo', 'DOH-bro YOO-tro, DOO-sho', 'Good morning, darling'),
   ('A text', 'Javi mi se, dušo', 'YAH-vee mee seh, DOO-sho', 'Get in touch, darling'),
   ('Comforting', 'Ne brini, dušo moja', 'neh BREE-nee, DOO-sho MOH-yah', "Don't worry, my darling")],
  alts=[('Mače', 'MAH-cheh', 'Kitten; playful'), ('Zlato', 'ZLAH-to', 'Gold; sweetheart'), ('Srce', 'SUR-tseh', 'Heart')],
  lit='Soul', rel=['zlato-sunce', 'ljubavi', 'draga', 'slatka-si']))

add(E('zafrkavas-me', "You're teasing me", 'Zafrkavaš me', 'zah-FUR-kah-vahsh meh', "You're messing with me / winding me up",
  [('FR', 'Playful teasing'), ('SS', 'Casual slang')], ['tease', 'joke', 'slang'], 'slang',
  [('To her', 'Zafrkavaš me, je l\' tako?', 'zah-FUR-kah-vahsh meh, yel TAH-ko', "You're messing with me, aren't you?"),
   ('Back at her', 'Samo te zafrkavam', 'SAH-mo teh zah-FUR-kah-vahm', "I'm just teasing you"),
   ('About him', 'On me stalno zafrkava', 'ohn meh STAHL-no zah-FUR-kah-vah', 'He keeps teasing me')],
  forms=[F('Zafrkavaš me', 'zah-FUR-kah-vahsh meh', 'To her', ('Zafrkavaš me od jutros', 'zah-FUR-kah-vahsh meh od YOO-tros', "You've been teasing me since this morning"), describes='her'),
         F('Zafrkavam te', 'zah-FUR-kah-vahm teh', 'About me teasing you', ('Zafrkavam te, ne ljuti se', 'zah-FUR-kah-vahm teh, neh LYOO-tee seh', "I'm teasing you, don't be mad"), describes='me'),
         F('Zafrkava me', 'zah-FUR-kah-vah meh', 'He / she is teasing me', ('Moj brat me zafrkava', 'moy BRAHT meh zah-FUR-kah-vah', 'My brother is teasing me'), describes='him / her')],
  alts=[('Zezaš me', 'ZEH-zahsh meh', 'You are teasing me (milder)')],
  watch='Slang. Very common, always light. Use "zezaš me" if you want the gentler version.', rel=['zezas-me', 'samo-se-salim', 'salis-se', 'drska-si']))

add(E('zaljubio-sam-se', 'I fell in love', 'Zaljubio sam se', 'zahl-YOO-bee-oh sahm seh', 'I fell in love; I have fallen for someone',
  [('FR', 'Relationship talk'), ('FR', 'Affection and romance')], ['love', 'fall', 'past'], 'casual',
  [('Admitting it', 'Mislim da sam se zaljubio', 'MEE-sleem dah sahm seh zahl-YOO-bee-oh', 'I think I fell in love (a man says this)'),
   ('Her answer', 'I ja sam se zaljubila', 'ee yah sahm seh zahl-YOO-bee-lah', 'I fell in love too (a woman says this)'),
   ('About a friend', 'Moj drug se zaljubio', 'moy DROOG seh zahl-YOO-bee-oh', 'My friend fell in love')],
  forms=[F('Zaljubio sam se', 'zahl-YOO-bee-oh sahm seh', 'A man says it', ('Zaljubio sam se u tebe', 'zahl-YOO-bee-oh sahm seh oo TEH-beh', 'I fell in love with you'), speaker='male'),
         F('Zaljubila sam se', 'zahl-YOO-bee-lah sahm seh', 'A woman says it', ('Zaljubila sam se u Beograd', 'zahl-YOO-bee-lah sahm seh oo beh-oh-GRAHD', 'I fell in love with Belgrade'), speaker='female'),
         F('Zaljubila si se?', 'zahl-YOO-bee-lah see seh', 'Asking her', ('Zaljubila si se? Ko je on?', 'zahl-YOO-bee-lah see seh? KOH yeh ohn', 'Did you fall in love? Who is he?'), describes='her')],
  alts=[('Imam krš na tebe', 'EE-mahm KURSH nah TEH-beh', 'I have a crush on you (casual slang)'), ('Zaljubljen sam', 'ZAHL-yoob-lyen sahm', "I'm in love")],
  ch=['tense'], rel=['zaljubljen-sam', 'svidjas-mi-se', 'volim-te', 'jesmo-li-zajedno']))

add(E('sta-smo-mi', 'What are we?', 'Šta smo mi?', 'SHTAH smo MEE', 'What are we? (to define the relationship)',
  [('FR', 'Relationship talk'), ('CV', 'Questions')], ['relationship', 'serious', 'question'], 'neutral',
  [('Asking', 'Šta smo mi, zapravo?', 'SHTAH smo MEE, ZAH-prah-vo', 'What are we, actually?'),
   ('Unsure (man)', 'Nisam siguran šta smo mi', 'NEE-sahm SEE-goo-rahn SHTAH smo MEE', "I'm not sure what we are (a man says this)"),
   ('Unsure (woman)', 'Nisam sigurna šta smo mi', 'NEE-sahm SEE-goor-nah SHTAH smo MEE', "I'm not sure what we are (a woman says this)")],
  alts=[('Hoćeš li da budemo zajedno?', 'HOH-chesh lee dah BOO-deh-mo ZAH-yed-no', 'Do you want us to be together?')],
  watch='A serious question. Pick the moment, in person or a call is better than a text.', rel=['jesmo-li-zajedno', 'moramo-da-pricamo', 'mozemo-li-da-razgovaramo', 'devojka-decko']))

add(E('mozemo-li-da-razgovaramo', 'Can we talk?', 'Možemo li da razgovaramo?', 'MOH-zheh-mo lee dah rahz-goh-VAH-rah-mo', 'Can we talk? (softer than "moramo da pričamo")',
  [('FR', 'Relationship talk'), ('CV', 'Questions')], ['talk', 'serious', 'gentle'], 'neutral',
  [('To her', 'Možemo li da razgovaramo večeras?', 'MOH-zheh-mo lee dah rahz-goh-VAH-rah-mo VEH-cheh-rahs', 'Can we talk tonight?'),
   ('Calm tone', 'Možemo li da razgovaramo mirno?', 'MOH-zheh-mo lee dah rahz-goh-VAH-rah-mo MEER-no', 'Can we talk calmly?'),
   ('Agreeing', 'Naravno da možemo', 'nah-RAHV-no dah MOH-zheh-mo', 'Of course we can')],
  alts=[('Treba da popričamo', 'TREH-bah dah poh-PREE-chah-mo', 'We should have a chat'), ('Moramo da pričamo', 'MOH-rah-mo dah PREE-chah-mo', 'We need to talk')],
  rel=['moramo-da-pricamo', 'sta-smo-mi', 'ne-ljuti-se', 'oprosti']))

# ───── Plans ─────
add(E('imas-li-vremena', 'Do you have time?', 'Imaš li vremena?', 'EE-mahsh lee VREH-meh-nah', 'Do you have time (tomorrow)?',
  [('CV', 'Making plans'), ('CV', 'Questions')], ['time', 'plans', 'question'], 'casual',
  [('To her', 'Imaš li vremena sutra?', 'EE-mahsh lee VREH-meh-nah SOO-trah', 'Do you have time tomorrow?'),
   ('Her answer', 'Imam vremena posle pet', 'EE-mahm VREH-meh-nah POH-sleh PEHT', 'I have time after five'),
   ('About them', 'Imaju li vremena za nas?', 'EE-mah-yoo lee VREH-meh-nah zah NAHS', 'Do they have time for us?')],
  forms=[F('Imaš li vremena?', 'EE-mahsh lee VREH-meh-nah', CAS, ('Imaš li vremena za kafu?', 'EE-mahsh lee VREH-meh-nah zah KAH-foo', 'Do you have time for a coffee?'), formal='casual'),
         F('Imate li vremena?', 'EE-mah-teh lee VREH-meh-nah', POL, ('Imate li vremena za pet minuta?', 'EE-mah-teh lee VREH-meh-nah zah PEHT mee-NOO-tah', 'Do you have five minutes?'), formal='polite')],
  alts=[('Jesi li slobodna?', 'YEH-see lee SLOH-bohd-nah', 'Are you free? (to her)')],
  rel=['kad-si-slobodna', 'kad-ti-odgovara', 'sta-radis-danas', 'hoces-da-izadjemo']))

add(E('tu-sam', "I'm here", 'Tu sam', 'TOO sahm', "I'm here (simplest way)",
  [('CV', 'Running late'), ('CV', 'Confirming plans')], ['here', 'arrive', 'texting'], 'casual',
  [('Arrived', 'Tu sam, ispred kafića', 'TOO sahm, EES-pred KAH-fee-chah', "I'm here, in front of the café"),
   ('Waiting', 'Tu sam, čekam te', 'TOO sahm, CHEH-kahm teh', "I'm here, waiting for you"),
   ('Her reply', 'Tu sam, dolazim', 'TOO sahm, doh-LAH-zeem', "I'm here, I'm coming")],
  forms=[F('Tu sam', 'TOO sahm', 'About me', ('Tu sam, vidim te', 'TOO sahm, VEE-deem teh', "I'm here, I see you"), describes='me'),
         F('Jesi li tu?', 'YEH-see lee TOO', 'Asking her', ('Jesi li tu? Ne vidim te', 'YEH-see lee TOO? neh VEE-deem teh', "Are you here? I can't see you"), describes='her'),
         F('Tu smo', 'TOO smo', 'About us', ('Tu smo, otvori vrata', 'TOO smo, OHT-voh-ree VRAH-tah', "We're here, open the door"), describes='us')],
  alts=[('Stigao sam', 'STEE-gah-oh sahm', "I've arrived"), ('Evo me', 'EH-vo meh', 'Here I am')],
  rel=['stigao-sam', 'evo', 'jesi-li-stigla', 'kasnim']))

add(E('moram-da-otkazem', 'I have to cancel', 'Moram da otkažem', 'MOH-rahm dah oht-KAH-zhem', 'I have to cancel',
  [('CV', 'Cancelling'), ('CV', 'Making plans')], ['cancel', 'plans', 'apology'], 'neutral',
  [('To her', 'Moram da otkažem večeras, izvini', 'MOH-rahm dah oht-KAH-zhem VEH-cheh-rahs, eez-VEE-nee', 'I have to cancel tonight, sorry'),
   ('A booking', 'Moram da otkažem rezervaciju', 'MOH-rahm dah oht-KAH-zhem reh-zehr-VAH-tsee-yoo', 'I have to cancel the reservation'),
   ('Asking her', 'Moraš li da otkažeš?', 'MOH-rahsh lee dah oht-KAH-zhesh', 'Do you have to cancel?')],
  forms=[F('Moram da otkažem', 'MOH-rahm dah oht-KAH-zhem', 'About me', ('Moram da otkažem, iskrslo mi je nešto', 'MOH-rahm dah oht-KAH-zhem, EES-kur-slo mee yeh NEHSH-to', 'I have to cancel, something came up'), describes='me'),
         F('Moraš li da otkažeš?', 'MOH-rahsh lee dah oht-KAH-zhesh', 'Asking her', ('Moraš li da otkažeš? Šteta', 'MOH-rahsh lee dah oht-KAH-zhesh? SHTEH-tah', 'Do you have to cancel? What a shame'), describes='her'),
         F('Moramo da otkažemo', 'MOH-rah-mo dah oht-KAH-zheh-mo', 'About us', ('Moramo da otkažemo putovanje', 'MOH-rah-mo dah oht-KAH-zheh-mo poo-toh-VAH-nyeh', 'We have to cancel the trip'), describes='us')],
  alts=[('Ne mogu da dođem', 'neh MOH-goo dah DOH-jem', "I can't come"), ('Nažalost ne mogu', 'NAH-zhah-lost neh MOH-goo', "Unfortunately I can't")],
  rel=['ne-mogu-da-dodjem', 'moze-li-drugi-dan', 'iskrslo-mi-je', 'nazalost']))

add(E('nazalost', 'Unfortunately', 'Nažalost', 'NAH-zhah-lost', 'Unfortunately; sadly',
  [('CV', 'Cancelling'), ('QP', 'Filler and transition words')], ['unfortunately', 'soften', 'apology'], 'neutral',
  [('Softening a no', 'Nažalost ne mogu večeras', 'NAH-zhah-lost neh MOH-goo VEH-cheh-rahs', "Unfortunately I can't tonight"),
   ('Bad news', 'Nažalost, kasnim', 'NAH-zhah-lost, KAHS-neem', "Unfortunately, I'm running late"),
   ('About a place', 'Nažalost je zatvoreno', 'NAH-zhah-lost yeh zah-TVOH-reh-no', "Unfortunately it's closed")],
  alts=[('Šteta', 'SHTEH-tah', 'What a shame'), ('Avaj', 'AH-vai', 'Alas (old-fashioned)')],
  rel=['moram-da-otkazem', 'ne-mogu-veceras', 'zao-mi-je', 'sorry']))

add(E('kad-ti-odgovara', 'When suits you?', 'Kad ti odgovara?', 'KAHD tee od-GOH-vah-rah', 'When suits you?',
  [('CV', 'Making plans'), ('CV', 'Questions')], ['plans', 'time', 'flexible'], 'casual',
  [('To her', 'Kad ti odgovara da se vidimo?', 'KAHD tee od-GOH-vah-rah dah seh VEE-dee-mo', 'When suits you for us to meet?'),
   ('Answering', 'Meni odgovara posle pet', 'MEH-nee od-GOH-vah-rah POH-sleh PEHT', 'After five suits me'),
   ('About a place', 'Da li ti odgovara taj kafić?', 'dah lee tee od-GOH-vah-rah TAH-ee KAH-feech', 'Does that café suit you?')],
  forms=[F('Kad ti odgovara?', 'KAHD tee od-GOH-vah-rah', CAS, ('Kad ti odgovara, ja sam fleksibilan', 'KAHD tee od-GOH-vah-rah, yah sahm fleh-ksee-BEE-lahn', "Whenever suits you, I'm flexible"), formal='casual'),
         F('Kad vam odgovara?', 'KAHD vahm od-GOH-vah-rah', POL, ('Kad vam odgovara, gospođo?', 'KAHD vahm od-GOH-vah-rah, GOH-spoh-joh', 'When suits you, ma’am?'), formal='polite')],
  rel=['imas-li-vremena', 'kad-si-slobodna', 'moze-li-drugi-dan', 'dogovoreno']))

add(E('imas-li-planove', 'Do you have plans?', 'Imaš li planove?', 'EE-mahsh lee PLAH-no-veh', 'Do you have plans?',
  [('CV', 'Making plans'), ('CV', 'Questions')], ['plans', 'weekend', 'question'], 'casual',
  [('To her', 'Imaš li planove za vikend?', 'EE-mahsh lee PLAH-no-veh zah VEE-kend', 'Do you have plans for the weekend?'),
   ('Her answer', 'Nemam planove, a ti?', 'NEH-mahm PLAH-no-veh, ah TEE', "I don't have plans, and you?"),
   ('Tonight', 'Šta radiš večeras?', 'SHTAH RAH-deesh VEH-cheh-rahs', 'What are you doing tonight?')],
  forms=[F('Imaš li planove?', 'EE-mahsh lee PLAH-no-veh', CAS, ('Imaš li planove za sutra?', 'EE-mahsh lee PLAH-no-veh zah SOO-trah', 'Do you have plans for tomorrow?'), formal='casual'),
         F('Imate li planove?', 'EE-mah-teh lee PLAH-no-veh', POL, ('Imate li planove za praznike?', 'EE-mah-teh lee PLAH-no-veh zah PRAHZ-nee-keh', 'Do you have plans for the holidays?'), formal='polite')],
  rel=['plan-za-vikend', 'imas-li-vremena', 'sta-radis-danas', 'hoces-da-izadjemo']))

add(E('nazovi-me', 'Call me', 'Nazovi me', 'nah-ZOH-vee meh', 'Call me',
  [('VA', 'Commands'), ('CV', 'Making plans')], ['call', 'phone', 'command'], 'casual',
  [('To her', 'Nazovi me kad stigneš', 'nah-ZOH-vee meh kahd STEEG-nesh', 'Call me when you arrive'),
   ('Later', 'Nazovi me večeras', 'nah-ZOH-vee meh VEH-cheh-rahs', 'Call me tonight'),
   ('Promise', 'Nazvaću te sutra', 'NAHZ-vah-choo teh SOO-trah', "I'll call you tomorrow")],
  forms=[F('Nazovi me', 'nah-ZOH-vee meh', CAS, ('Nazovi me ako ti nešto treba', 'nah-ZOH-vee meh AH-ko tee NEHSH-to TREH-bah', 'Call me if you need anything'), formal='casual'),
         F('Nazovite me', 'nah-ZOH-vee-teh meh', POL, ('Nazovite me kad možete', 'nah-ZOH-vee-teh meh kahd MOH-zheh-teh', 'Call me when you can'), formal='polite')],
  alts=[('Javi se', 'YAH-vee seh', 'Get in touch'), ('Zovni me', 'ZOHV-nee meh', 'Give me a ring (casual)')],
  rel=['javi-se', 'zvacu-te', 'javi-ako-se-promeni', 'tvoj-broj']))

# ───── Feelings and health ─────
add(E('zima-mi-je', "I'm freezing", 'Zima mi je', 'ZEE-mah mee yeh', "I'm freezing; I'm very cold",
  [('DF', 'Physical states'), ('DF', 'Describing things')], ['cold', 'body', 'feeling'], 'casual',
  [('About me', 'Zima mi je, daj mi jaknu', 'ZEE-mah mee yeh, DAI mee YAHK-noo', "I'm freezing, give me a jacket"),
   ('Her', 'Zima joj je u toj sobi', 'ZEE-mah yoy yeh oo TOY SOH-bee', "She's freezing in that room"),
   ('Caring', 'Zima ti je? Evo ti moj džemper', 'ZEE-mah tee yeh? EH-vo tee moy JEM-per', "Are you freezing? Here's my sweater")],
  forms=[F('Zima mi je', 'ZEE-mah mee yeh', 'About me', ('Zima mi je, ugasi klimu', 'ZEE-mah mee yeh, oo-GAH-see KLEE-moo', "I'm freezing, turn off the A/C"), describes='me'),
         F('Zima ti je?', 'ZEE-mah tee yeh', 'Asking her', ('Zima ti je? Hoćeš moju jaknu?', 'ZEE-mah tee yeh? HOH-chesh MOH-yoo YAHK-noo', 'Are you cold? Want my jacket?'), describes='her'),
         F('Zima mu je / Zima joj je', 'ZEE-mah moo yeh / ZEE-mah yoy yeh', 'About him / her', ('Zima joj je bez šala', 'ZEE-mah yoy yeh behz SHAH-lah', "She's cold without a scarf"), describes='him / her'),
         F('Zima nam je', 'ZEE-mah nahm yeh', 'About us', ('Zima nam je, hajde unutra', 'ZEE-mah nahm yeh, HAY-deh OO-noo-trah', "We're freezing, let's go inside"), describes='us')],
  alts=[('Hladno mi je', 'HLAHD-no mee yeh', "I'm cold")],
  rel=['hladno-mi-je', 'napolju-je-hladno', 'spava-mi-se', 'bolestan-sam']))

add(E('boli-me-glava', 'I have a headache', 'Boli me glava', 'BOH-lee meh GLAH-vah', 'I have a headache',
  [('DF', 'Physical states'), ('DF', 'Emotions')], ['health', 'pain', 'headache'], 'neutral',
  [('About me', 'Boli me glava od jutros', 'BOH-lee meh GLAH-vah od YOO-tros', "I've had a headache since this morning"),
   ('Her', 'Boli te glava? Ima tableta', 'BOH-lee teh GLAH-vah? EE-mah tah-BLEH-tah', 'Do you have a headache? There are pills'),
   ('Other pains', 'Boli me stomak', 'BOH-lee meh STOH-mahk', 'I have a stomach ache')],
  forms=[F('Boli me glava', 'BOH-lee meh GLAH-vah', 'About me', ('Boli me glava, idem da legnem', 'BOH-lee meh GLAH-vah, EE-dem dah LEG-nem', "I have a headache, I'm going to lie down"), describes='me'),
         F('Boli te glava?', 'BOH-lee teh GLAH-vah', 'Asking her', ('Boli te glava? Popij vode', 'BOH-lee teh GLAH-vah? POH-peey VOH-deh', 'Does your head hurt? Drink some water'), describes='her'),
         F('Boli ga glava / Boli je glava', 'BOH-lee gah GLAH-vah / BOH-lee yeh GLAH-vah', 'About him / her', ('Boli je glava od buke', 'BOH-lee yeh GLAH-vah od BOO-keh', 'Her head hurts from the noise'), describes='him / her')],
  alts=[('Boli me stomak', 'BOH-lee meh STOH-mahk', 'I have a stomach ache'), ('Prehlađen sam', 'preh-HLAH-jen sahm', 'I have a cold (a man says this)')],
  rel=['bolestan-sam', 'ozdravi-brzo', 'zima-mi-je', 'umoran']))

add(E('ozdravi-brzo', 'Get well soon', 'Ozdravi brzo', 'oz-DRAH-vee BUR-zo', 'Get well soon',
  [('DF', 'Physical states'), ('CE', 'Common sayings')], ['health', 'sympathy', 'wish'], 'neutral',
  [('Texting her', 'Ozdravi brzo, javi mi kako si', 'oz-DRAH-vee BUR-zo, YAH-vee mee KAH-ko see', 'Get well soon, tell me how you are'),
   ('To her mom', 'Ozdravite brzo, gospođo', 'oz-DRAH-vee-teh BUR-zo, GOH-spoh-joh', 'Get well soon, ma’am'),
   ('About him', 'Neka ozdravi brzo', 'NEH-kah oz-DRAH-vee BUR-zo', 'May he get well soon')],
  forms=[F('Ozdravi brzo', 'oz-DRAH-vee BUR-zo', CAS, ('Ozdravi brzo, odmaraj se', 'oz-DRAH-vee BUR-zo, OD-mah-rai seh', 'Get well soon, rest'), formal='casual'),
         F('Ozdravite brzo', 'oz-DRAH-vee-teh BUR-zo', POL, ('Ozdravite brzo, svi mislimo na vas', 'oz-DRAH-vee-teh BUR-zo, SVEE MEE-slee-mo nah vahs', "Get well soon, we're all thinking of you"), formal='polite')],
  alts=[('Brz oporavak', 'BURZ oh-POH-rah-vahk', 'A quick recovery')],
  rel=['bolestan-sam', 'boli-me-glava', 'zao-mi-je', 'cuvaj-se']))

add(E('dosta-mi-je', "I've had enough", 'Dosta mi je', 'DOH-stah mee yeh', "I've had enough; I'm fed up",
  [('DF', 'Emotions'), ('CV', 'Casual conversation')], ['enough', 'fed up', 'frustration'], 'casual',
  [('Frustrated', 'Dosta mi je gužve', 'DOH-stah mee yeh GOOZH-veh', "I've had enough of the crowds"),
   ('Food', 'Dosta mi je, hvala', 'DOH-stah mee yeh, HVAH-lah', "I've had enough, thanks"),
   ('Her', 'Dosta joj je svega', 'DOH-stah yoy yeh SVEH-gah', "She's had enough of everything")],
  forms=[F('Dosta mi je', 'DOH-stah mee yeh', 'About me', ('Dosta mi je posla za danas', 'DOH-stah mee yeh POH-slah zah DAH-nahs', "I've had enough work for today"), describes='me'),
         F('Dosta ti je?', 'DOH-stah tee yeh', 'Asking her', ('Dosta ti je? Idemo kući', 'DOH-stah tee yeh? EE-deh-mo KOO-chee', "Had enough? Let's go home"), describes='her'),
         F('Dosta nam je', 'DOH-stah nahm yeh', 'About us', ('Dosta nam je kiše', 'DOH-stah nahm yeh KEE-sheh', "We've had enough of the rain"), describes='us')],
  alts=[('Iznerviran sam', 'eez-NER-vee-rahn sahm', "I'm annoyed"), ('Nerviram se', 'NER-vee-rahm seh', "I'm getting wound up")],
  rel=['iznerviran-sam', 'dosadno-mi-je', 'zabrinut-sam', 'ne-da-mi-se']))

add(E('sit-sam', "I'm full", 'Sit sam', 'SEET sahm', "I'm full (after eating)",
  [('ES', 'Food and drink'), ('CE', 'Being a guest')], ['full', 'food', 'guest'], 'neutral',
  [('Politely declining', 'Hvala, sit sam', 'HVAH-lah, SEET sahm', "Thanks, I'm full (a man says this)"),
   ('Her side', 'Hvala, sita sam', 'HVAH-lah, SEE-tah sahm', "Thanks, I'm full (a woman says this)"),
   ('A host presses on', 'Jedi još malo, nisi sit', 'YEH-dee yohsh MAH-lo, NEE-see SEET', "Eat a little more, you're not full")],
  forms=[F('Sit sam', 'SEET sahm', 'A man says it', ('Sit sam, sve je bilo ukusno', 'SEET sahm, SVEH yeh BEE-lo OO-koos-no', "I'm full, everything was delicious"), speaker='male'),
         F('Sita sam', 'SEE-tah sahm', 'A woman says it', ('Sita sam, hvala puno', 'SEE-tah sahm, HVAH-lah POO-no', "I'm full, thanks a lot"), speaker='female'),
         F('Sit si?', 'SEET see', 'Asking a man', ('Sit si? Ima još', 'SEET see? EE-mah yohsh', "Are you full? There's more"), describes='him'),
         F('Sita si?', 'SEE-tah see', 'Asking her', ('Sita si? Hoćeš kolač?', 'SEE-tah see? HOH-chesh KOH-lahch', 'Are you full? Want a cake?'), describes='her')],
  alts=[('Prepun sam', 'PREH-poon sahm', "I'm stuffed (a man; a woman: prepuna sam)"), ('Dosta je, hvala', 'DOH-stah yeh, HVAH-lah', "That's enough, thanks")],
  watch='At a Serbian table "sit sam" is often not believed. Expect to be offered more; say it warmly, twice.',
  rel=['ne-treba', 'samo-malo-da-probam', 'jos-malo', 'sve-je-bilo-ukusno']))

# ───── Shops, manners, small words ─────
add(E('podelimo-racun', "Let's split the bill", 'Podelimo račun', 'poh-DEH-lee-mo RAH-choon', "Let's split the bill",
  [('ES', 'Restaurants and cafés'), ('ES', 'Shopping and money')], ['bill', 'pay', 'split'], 'casual',
  [('At the table', 'Podelimo račun?', 'poh-DEH-lee-mo RAH-choon', 'Shall we split the bill?'),
   ('To her', 'Ja častim, ti sledeći put', 'yah CHAH-steem, tee SLEH-deh-chee POOT', "My treat, you get the next one"),
   ('Insisting', 'Ne, ne, ja plaćam', 'neh, neh, yah PLAH-chahm', "No, no, I'm paying")],
  alts=[('Ja častim', 'yah CHAH-steem', "It's my treat"), ('Ja ću da platim', 'yah choo dah PLAH-teem', "I'll pay")],
  watch='In Serbia the person who invited usually pays, and arguing over the bill is almost a sport. "Ja častim" is the line to know.',
  rel=['racun', 'ja-cu-da-platim', 'kartica-ili-kes', 'koliko-kosta']))

add(E('ima-li-popusta', 'Is there a discount?', 'Ima li popusta?', 'EE-mah lee poh-POO-stah', 'Is there a discount?',
  [('ES', 'Shopping and money'), ('CV', 'Questions')], ['discount', 'shopping', 'price'], 'neutral',
  [('At a market', 'Ima li popusta ako uzmem dva?', 'EE-mah lee poh-POO-stah AH-ko OOZ-mem DVAH', 'Is there a discount if I take two?'),
   ('Asking nicely', 'Može li neki popust?', 'MOH-zheh lee NEH-kee POH-poost', 'Could there be some discount?'),
   ('Hearing it', 'Ima popusta na sve', 'EE-mah poh-POO-stah nah SVEH', 'There is a discount on everything')],
  alts=[('Može li jeftinije?', 'MOH-zheh lee YEF-tee-nee-yeh', 'Can it be cheaper?'), ('Po čemu je…?', 'poh CHEH-moo yeh', 'What is the price of…? (market)')],
  rel=['koliko-kosta', 'skuplje-jeftinije', 'skupo', 'pijaca']))

add(E('samo-razgledam', "I'm just browsing", 'Samo razgledam', 'SAH-mo rahz-GLEH-dahm', "I'm just browsing",
  [('ES', 'Shopping and money')], ['shop', 'browse', 'reply'], 'neutral',
  [('In a shop', 'Samo razgledam, hvala', 'SAH-mo rahz-GLEH-dahm, HVAH-lah', "I'm just browsing, thanks"),
   ('About us', 'Samo razgledamo, hvala', 'SAH-mo rahz-GLEH-dah-mo, HVAH-lah', "We're just browsing, thanks"),
   ('Asking for help later', 'Pozvaću vas ako zatreba', 'POHZ-vah-choo vahs AH-ko zah-TREH-bah', "I'll call you if I need anything")],
  alts=[('Samo gledam', 'SAH-mo GLEH-dahm', 'Just looking'), ('Hvala, ne treba', 'HVAH-lah, neh TREH-bah', 'Thanks, no need')],
  rel=['samo-gledam', 'ne-treba', 'uzecu-ovo', 'koliko-kosta']))

add(E('pazi-na-sebe', 'Look after yourself', 'Pazi na sebe', 'PAH-zee nah SEH-beh', 'Look after yourself; take care',
  [('QP', 'Greetings and goodbyes'), ('CE', 'Common sayings')], ['goodbye', 'care', 'warm'], 'neutral',
  [('Goodbye', 'Ćao, pazi na sebe', 'CHOW, PAH-zee nah SEH-beh', 'Bye, look after yourself'),
   ('Before a trip', 'Pazi na sebe i javi se', 'PAH-zee nah SEH-beh ee YAH-vee seh', 'Look after yourself and get in touch'),
   ('To her mom', 'Pazite na sebe', 'PAH-zee-teh nah SEH-beh', 'Take care')],
  forms=[F('Pazi na sebe', 'PAH-zee nah SEH-beh', CAS, ('Pazi na sebe, vidimo se', 'PAH-zee nah SEH-beh, VEE-dee-mo seh', 'Take care, see you'), formal='casual'),
         F('Pazite na sebe', 'PAH-zee-teh nah SEH-beh', POL, ('Pazite na sebe, gospođo', 'PAH-zee-teh nah SEH-beh, GOH-spoh-joh', 'Take care, ma’am'), formal='polite')],
  alts=[('Čuvaj se', 'CHOO-vai seh', 'Take care'), ('Srećno', 'SREHCH-no', 'Good luck')],
  rel=['cuvaj-se', 'srecan-put', 'see-you', 'laku-noc']))

add(E('bravo', 'Bravo', 'Bravo', 'BRAH-vo', 'Bravo; well done',
  [('QP', 'Reactions'), ('QP', 'Common replies')], ['praise', 'well done', 'reaction'], 'casual',
  [('To her', 'Bravo, odlično govoriš!', 'BRAH-vo, od-LEECH-no GOH-vo-reesh', 'Bravo, you speak really well!'),
   ('Cheering', 'Bravo za tebe!', 'BRAH-vo zah TEH-beh', 'Bravo to you!'),
   ('Teasing', 'Bravo, majstore', 'BRAH-vo, MAI-stoh-reh', 'Bravo, maestro')],
  alts=[('Svaka čast', 'SVAH-kah CHAHST', 'Well done, hats off'), ('Svaka ti čast', 'SVAH-kah tee CHAHST', 'Hats off to you (warmer)')],
  rel=['svaka-cast', 'odlicno', 'kul', 'cestitam']))

add(E('nikako', 'No way / not at all', 'Nikako', 'NEE-kah-ko', 'No way; not at all; by no means',
  [('QP', 'Yes, no, maybe'), ('QP', 'Agree and disagree')], ['no', 'refusal', 'emphasis'], 'neutral',
  [('Refusing', 'Nikako, ne dolazi u obzir', 'NEE-kah-ko, neh DOH-lah-zee oo OHB-zeer', 'No way, out of the question'),
   ('About me', 'Nikako ne mogu večeras', 'NEE-kah-ko neh MOH-goo VEH-cheh-rahs', "I really can't tonight"),
   ('Playful', 'Ni slučajno!', 'NEE SLOO-chai-no', 'Not a chance!')],
  alts=[('Ni slučajno', 'nee SLOO-chai-no', 'Not at all, not by accident'), ('Nema šanse', 'NEH-mah SHAHN-seh', 'No chance')],
  rel=['nema-sanse', 'ne-mogu', 'necu', 'ma-nemoj']))

add(E('milo-mi-je', 'Pleased to meet you', 'Milo mi je', 'MEE-lo mee yeh', 'Pleased to meet you; nice to meet you',
  [('CV', 'Introductions'), ('QP', 'Greetings and goodbyes')], ['meet', 'polite', 'introduction'], 'neutral',
  [('Introduced', 'Milo mi je, ja sam Met', 'MEE-lo mee yeh, yah sahm MET', "Pleased to meet you, I'm Matt"),
   ('To her mom', 'Milo mi je da vas upoznam', 'MEE-lo mee yeh dah vahs oo-POHZ-nahm', 'I am pleased to meet you'),
   ('Reply', 'I meni je milo', 'ee MEH-nee yeh MEE-lo', 'Pleased to meet you too')],
  alts=[('Drago mi je', 'DRAH-go mee yeh', 'Nice to meet you (the most common)'), ('Drago mi je što smo se upoznali', 'DRAH-go mee yeh shtoh smo seh oo-POHZ-nah-lee', 'Glad we met')],
  rel=['drago-mi-je', 'ovo-je', 'kako-se-zoves', 'dobar-dan']))

add(E('hvala-lepo', 'Thanks kindly', 'Hvala lepo', 'HVAH-lah LEH-po', 'Thank you kindly; thanks very much',
  [('QP', 'Thanks, sorry, please')], ['thanks', 'polite', 'warm'], 'neutral',
  [('Shop', 'Hvala lepo, prijatno', 'HVAH-lah LEH-po, PREE-yaht-no', 'Thank you kindly, enjoy'),
   ('To her', 'Hvala lepo na pomoći', 'HVAH-lah LEH-po nah POH-moh-chee', 'Thanks kindly for the help'),
   ('To an elder', 'Hvala lepo, gospođo', 'HVAH-lah LEH-po, GOH-spoh-joh', 'Thank you very much, ma’am')],
  alts=[('Najlepša hvala', 'NAI-lehp-shah HVAH-lah', 'Thank you so much (warm, a bit formal)'), ('Hvala puno', 'HVAH-lah POO-no', 'Thanks a lot')],
  rel=['thank-you', 'hvala-puno', 'nema-na-cemu', 'hvala-na-gostoprimstvu']))

add(E('u-stvari', 'In fact / actually', 'U stvari', 'oo STVAH-ree', 'In fact; actually',
  [('QP', 'Filler and transition words'), ('BA', 'Flow words')], ['filler', 'actually', 'flow'], 'neutral',
  [('Correcting', 'U stvari, ne znam', 'oo STVAH-ree, neh ZNAHM', "Actually, I don't know"),
   ('To her', 'U stvari, sviđaš mi se', 'oo STVAH-ree, SVEE-jahsh mee seh', 'Actually, I like you'),
   ('About him', 'U stvari, on je tu', 'oo STVAH-ree, ohn yeh TOO', 'Actually, he is here')],
  alts=[('Zapravo', 'ZAH-prah-vo', 'Actually'), ('Istina je da…', 'EES-tee-nah yeh dah', 'The truth is that…')],
  rel=['zapravo', 'ipak', 'uglavnom', 'iskreno']))

add(E('okej', 'Okay', 'Okej', 'oh-KAY', 'Okay (casual, from English)',
  [('QP', 'Common replies'), ('QP', 'Agree and disagree')], ['okay', 'agree', 'reply'], 'casual',
  [('Agreeing', 'Okej, vidimo se', 'oh-KAY, VEE-dee-mo seh', 'Okay, see you'),
   ('To her', 'Okej, kako ti odgovara', 'oh-KAY, KAH-ko tee od-GOH-vah-rah', 'Okay, whatever suits you'),
   ('Asking', 'Je l\' okej ako kasnim?', 'yel oh-KAY AH-ko KAHS-neem', 'Is it okay if I am late?')],
  alts=[('U redu', 'oo REH-doo', 'All right'), ('Može', 'MOH-zheh', 'OK, sure'), ('Važi', 'VAH-zhee', 'Deal')],
  text='okej / ok', rel=['u-redu', 'moze', 'vazi', 'dogovoreno']))

add(E('pare', 'Money', 'Pare', 'PAH-reh', 'Money (the everyday word)',
  [('ES', 'Shopping and money')], ['money', 'shopping', 'everyday'], 'neutral',
  [('Short on cash', 'Nemam pare kod sebe', 'NEH-mahm PAH-reh kohd SEH-beh', "I don't have money on me"),
   ('About work', 'Zarađujem dobre pare', 'zah-RAH-joo-yem DOH-breh PAH-reh', 'I earn good money'),
   ('To her', 'Imaš li para za taksi?', 'EE-mahsh lee PAH-rah zah TAHK-see', 'Do you have money for a taxi?'),
   ('About them', 'Oni imaju puno para', 'OH-nee EE-mah-yoo POO-no PAH-rah', 'They have a lot of money')],
  alts=[('Lova', 'LOH-vah', 'Money (slang)'), ('Novac', 'NOH-vahts', 'Money (formal)'), ('Keš', 'KESH', 'Cash')],
  rel=['lova', 'koliko-kosta', 'cena-u-dinarima', 'kartica-ili-kes']))

# ───── Questions ─────
add(E('kakav', 'What kind of…?', 'Kakav / kakva / kakvo', 'KAH-kahv / KAHK-vah / KAHK-vo', 'What kind of…? What is it like?',
  [('BA', 'Question words'), ('CV', 'Questions')], ['question', 'kind', 'describing'], 'neutral',
  [('Asking about a person', 'Kakav je on?', 'KAH-kahv yeh OHN', 'What is he like?'),
   ('About her', 'Kakva je ona?', 'KAHK-vah yeh OH-nah', 'What is she like?'),
   ('The weather', 'Kakvo je vreme?', 'KAHK-vo yeh VREH-meh', "What's the weather like?"),
   ('Food', 'Kakva je kafa ovde?', 'KAHK-vah yeh KAH-fah OHV-deh', 'What is the coffee like here?')],
  forms=[F('Kakav je…?', 'KAH-kahv yeh', 'Masculine thing, or a man', ('Kakav je film?', 'KAH-kahv yeh FEELM', 'What is the film like?'), nounGender='masculine'),
         F('Kakva je…?', 'KAHK-vah yeh', 'Feminine thing, or a woman', ('Kakva je hrana?', 'KAHK-vah yeh HRAH-nah', 'What is the food like?'), nounGender='feminine'),
         F('Kakvo je…?', 'KAHK-vo yeh', 'Neuter thing', ('Kakvo je pivo?', 'KAHK-vo yeh PEE-vo', 'What is the beer like?'), nounGender='neuter')],
  alts=[('Koji / koja / koje', 'KOH-yee / KOH-yah / KOH-yeh', 'Which one')],
  rel=['koji', 'kako', 'sta', 'najbolji']))

add(E('kako-to', 'How come?', 'Kako to?', 'KAH-ko TOH', 'How come? How so?',
  [('CV', 'Questions'), ('QP', 'Reactions')], ['question', 'surprise', 'how come'], 'casual',
  [('Surprised', 'Kako to? Mislio sam da dolaziš', 'KAH-ko TOH? MEE-slee-oh sahm dah DOH-lah-zeesh', 'How come? I thought you were coming'),
   ('Asking why', 'Kako to da si budna?', 'KAH-ko TOH dah see BOOD-nah', 'How come you are awake? (to her)'),
   ('What do you mean', 'Kako to misliš?', 'KAH-ko TOH MEE-sleesh', 'What do you mean?')],
  alts=[('Zašto?', 'ZAHSH-to', 'Why?'), ('Kako to misliš?', 'KAH-ko toh MEE-sleesh', 'What do you mean?')],
  rel=['zasto', 'kako', 'stvarno', 'sta-znaci']))

add(E('koliko-si-star', 'How old are you?', 'Koliko si star?', 'KOH-lee-ko see STAHR', 'How old are you?',
  [('CV', 'Getting to know someone'), ('CV', 'Questions')], ['age', 'question', 'getting to know'], 'casual',
  [('Asking a man', 'Koliko si star, brate?', 'KOH-lee-ko see STAHR, BRAH-teh', 'How old are you, man?'),
   ('Careful with her', 'Koliko si stara, ako smem da pitam?', 'KOH-lee-ko see STAH-rah, AH-ko smem dah PEE-tahm', 'How old are you, if I may ask?'),
   ('About me', 'Imam trideset godina', 'EE-mahm TREE-deh-set GOH-dee-nah', "I'm thirty years old")],
  forms=[F('Koliko si star?', 'KOH-lee-ko see STAHR', 'To a man', ('Koliko si star? Izgledaš mlađe', 'KOH-lee-ko see STAHR? EEZ-gleh-dahsh MLAH-jeh', 'How old are you? You look younger'), describes='him'),
         F('Koliko si stara?', 'KOH-lee-ko see STAH-rah', 'To a woman', ('Koliko si stara? Nemoj da kažeš!', 'KOH-lee-ko see STAH-rah? NEH-moy dah KAH-zhesh', "How old are you? (be careful: this can be a sensitive question)"), describes='her')],
  alts=[('Koliko imaš godina?', 'KOH-lee-ko EE-mahsh GOH-dee-nah', 'How old are you? (literally how many years do you have)')],
  watch='Asking a woman her age is touchy anywhere. "Koliko imaš godina?" is the safer, standard way to ask.',
  rel=['koliko-imas-godina', 'kako-se-zoves', 'odakle-si', 'cime-se-bavis']))

add(E('sta-se-desava', "What's happening?", 'Šta se dešava?', 'SHTAH seh DEH-shah-vah', "What's happening? What's going on?",
  [('CV', 'Questions'), ('QP', 'Conversation starters')], ['question', 'happening', 'casual'], 'casual',
  [('Greeting', 'Ej, šta se dešava?', 'AY, SHTAH seh DEH-shah-vah', "Hey, what's going on?"),
   ('Worried', 'Šta se dešava? Zvučiš čudno', 'SHTAH seh DEH-shah-vah? ZVOO-cheesh CHOOD-no', "What's going on? You sound odd"),
   ('Afterwards', 'Šta se desilo?', 'SHTAH seh DEH-see-lo', 'What happened?')],
  alts=[('Šta se desilo?', 'SHTAH seh DEH-see-lo', 'What happened?'), ("Šta ima?", 'SHTAH EE-mah', "What's up?")],
  rel=['sta-ima', 'kako-ide', 'jesi-li-dobro', 'sta-ima-novo']))

if __name__ == '__main__':
    c.NEW = NEW
    print('added', len(c.merge()), 'of', len(NEW), 'entries')
