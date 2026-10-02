P = {}

def feeling(m, pm, f, pf, pl, ppl, fx, he, she, we, adds, ctx0='Me (man)'):
    return dict(ctx0=ctx0, fx=fx, forms_add=[
        F(f'{m} je', f'{pm} yeh', 'About a man (he)', he, describes='him'),
        F(f'{f} je', f'{pf} yeh', 'About a woman (she)', she, describes='her'),
        F(f'{pl} smo', f'{ppl} smoh', 'Us (mixed group)', we, describes='us'),
    ], add=adds)

P['gladan'] = feeling('Gladan', 'GLAH-dahn', 'Gladna', 'GLAHD-nah', 'Gladni', 'GLAHD-nee', [
  ('Gladan sam, hajdemo da jedemo', 'GLAH-dahn sahm, HAY-deh-mo dah YEH-deh-mo', "I'm hungry, let's eat (a man says this)"),
  ('Gladna sam, šta ima za ručak?', 'GLAHD-nah sahm, SHTAH EE-mah zah ROO-chahk', "I'm hungry, what's for lunch? (a woman says this)"),
  ('Gladan si? Evo sendvič', 'GLAH-dahn see? EH-vo SEND-veech', "You're hungry? Here's a sandwich (to a man)"),
  ('Gladna si, zar ne?', 'GLAHD-nah see, zahr NEH', "You're hungry, aren't you? (to her)"),
 ], ('On je gladan, daj mu nešto', 'OHN yeh GLAH-dahn, dai moo NEHSH-to', "He's hungry, give him something"),
    ('Ona je gladna, nije ništa jela', 'OH-nah yeh GLAHD-nah, NEE-yeh NEESH-tah YEH-lah', "She's hungry, she hasn't eaten anything"),
    ('Gladni smo, idemo na ćevape', 'GLAHD-nee smoh, EE-deh-mo nah CHEH-vah-peh', "We're hungry, let's get ćevapi"),
 [X('Her, about herself', 'Gladna sam kao vuk', 'GLAHD-nah sahm KAH-oh VOOK', "I'm hungry as a wolf (a woman says this)"),
  X('About a child', 'Dete je gladno', 'DEH-teh yeh GLAHD-no', 'The child is hungry')])
P['zedan'] = feeling('Žedan', 'ZHEH-dahn', 'Žedna', 'ZHEHD-nah', 'Žedni', 'ZHEHD-nee', [
  ('Žedan sam posle trčanja', 'ZHEH-dahn sahm POH-sleh TUR-chah-nyah', "I'm thirsty after running (a man says this)"),
  ('Žedna sam, hoću sok', 'ZHEHD-nah sahm, HOH-choo SOHK', "I'm thirsty, I want juice (a woman says this)"),
  ('Žedan si? Evo vode', 'ZHEH-dahn see? EH-vo VOH-deh', "You're thirsty? Here's water (to a man)"),
  ('Žedna si? Uzmi moju flašu', 'ZHEHD-nah see? OOZ-mee MOH-yoo FLAH-shoo', "You're thirsty? Take my bottle (to her)"),
 ], ('On je žedan', 'OHN yeh ZHEH-dahn', "He's thirsty"),
    ('Ona je žedna, daj joj vode', 'OH-nah yeh ZHEHD-nah, dai yoy VOH-deh', "She's thirsty, give her water"),
    ('Žedni smo, hajdemo na piće', 'ZHEHD-nee smoh, HAY-deh-mo nah PEE-cheh', "We're thirsty, let's get a drink"),
 [X('Me (man)', 'Žedan sam, hoću vodu', 'ZHEH-dahn sahm, HOH-choo VOH-doo', "I'm thirsty, I want water"),
  X('About a thing', 'Cveće je žedno', 'TSVEH-cheh yeh ZHED-no', 'The flowers are thirsty')], ctx0='Her, about herself')
P['tuzan'] = feeling('Tužan', 'TOO-zhahn', 'Tužna', 'TOOZH-nah', 'Tužni', 'TOOZH-nee', [
  ('Tužan sam danas', 'TOO-zhahn sahm DAH-nahs', "I'm sad today (a man says this)"),
  ('Tužna sam zbog toga', 'TOOZH-nah sahm zbog TOH-gah', "I'm sad because of that (a woman says this)"),
  ('Tužan si, šta se desilo?', 'TOO-zhahn see, SHTAH seh DEH-see-lo', "You're sad, what happened? (to a man)"),
  ('Tužna si? Hoćeš da pričamo?', 'TOOZH-nah see? HOH-chesh dah PREE-chah-mo', "Are you sad? Want to talk? (to her)"),
 ], ('On je tužan zbog posla', 'OHN yeh TOO-zhahn zbog POH-slah', "He's sad about work"),
    ('Ona je tužna, nazovi je', 'OH-nah yeh TOOZH-nah, NAH-zoh-vee yeh', "She's sad, call her"),
    ('Tužni smo što odlazite', 'TOOZH-nee smoh shtoh OD-lah-zee-teh', "We're sad that you're leaving"),
 [X('Me (man)', 'Tužan sam što odlaziš', 'TOO-zhahn sahm shtoh OD-lah-zeesh', "I'm sad that you're leaving"),
  X('Her, about herself', 'Tužna sam što odlaziš', 'TOOZH-nah sahm shtoh OD-lah-zeesh', "I'm sad that you're leaving (a woman says this)"),
  X('About a thing', 'Ova pesma je tužna', 'OH-vah PEH-smah yeh TOOZH-nah', 'This song is sad')], ctx0=None)
P['ljut'] = feeling('Ljut', 'LYOOT', 'Ljuta', 'LYOO-tah', 'Ljuti', 'LYOO-tee', [
  ('Ljut sam na sebe', 'LYOOT sahm nah SEH-beh', "I'm angry at myself (a man says this)"),
  ('Ljuta sam na njega', 'LYOO-tah sahm nah NYEH-gah', "I'm angry at him (a woman says this)"),
  ('Ljut si na mene?', 'LYOOT see nah MEH-neh', "Are you angry at me? (to a man)"),
  ('Ljuta si na mene?', 'LYOO-tah see nah MEH-neh', "Are you angry at me? (to her)"),
 ], ('On je ljut zbog kašnjenja', 'OHN yeh LYOOT zbog KAHSH-nyeh-nyah', "He's angry about the delay"),
    ('Ona je ljuta na mene', 'OH-nah yeh LYOO-tah nah MEH-neh', "She's angry at me"),
    ('Ljuti smo na njih', 'LYOO-tee smoh nah NYEEH', "We're angry at them"),
 [X('Her, about herself', 'Nisam ljuta na tebe', 'NEE-sahm LYOO-tah nah TEH-beh', "I'm not mad at you (a woman says this)"),
  X('Meaning "spicy"', 'Ovo je baš ljuto!', 'OH-vo yeh BAHSH LYOO-to', "This is really spicy!")])
if P['tuzan']['ctx0'] is None: del P['tuzan']['ctx0']

P['dosadno-mi-je'] = dict(ctx0='Me', forms=[
  F('Dosadno mi je', 'DOH-sahd-no mee yeh', 'Me (man or woman)', ('Dosadno mi je kod kuće', 'DOH-sahd-no mee yeh kod KOO-cheh', "I'm bored at home"), describes='me'),
  F('Dosadno ti je?', 'DOH-sahd-no tee yeh', 'You, to her or to him', ('Dosadno ti je? Hajde da izađemo', 'DOH-sahd-no tee yeh? HAY-deh dah ee-ZAH-jeh-mo', "Are you bored? Let's go out"), describes='her', formal='casual'),
  F('Dosadno mu je', 'DOH-sahd-no moo yeh', 'About him', ('Dosadno mu je na poslu', 'DOH-sahd-no moo yeh nah POH-sloo', "He's bored at work"), describes='him'),
  F('Dosadno joj je', 'DOH-sahd-no yoy yeh', 'About her', ('Dosadno joj je kad nema nas', 'DOH-sahd-no yoy yeh kahd NEH-mah NAHS', "She's bored when we're not around"), describes='her'),
  F('Dosadno nam je', 'DOH-sahd-no nahm yeh', 'Us', ('Dosadno nam je, šta da radimo?', 'DOH-sahd-no nahm yeh, SHTAH dah RAH-dee-mo', "We're bored, what should we do?"), describes='us'),
  F('Dosadno vam je?', 'DOH-sahd-no vahm yeh', 'Polite, or to a group', ('Dosadno vam je ovde?', 'DOH-sahd-no vahm yeh OHV-deh', 'Are you bored here?'), formal='polite'),
], changesBy=['describes', 'formal'], add=[
  X('To her', 'Dosadno ti je bez mene?', 'DOH-sahd-no tee yeh bez MEH-neh', 'Are you bored without me?'),
  X('About a thing', 'Film je dosadan', 'FEELM yeh DOH-sah-dahn', 'The movie is boring'),
])
P['pametan'] = dict(ctx0='To her', fx=[
  ('Pametan si, brate, to je dobra ideja', 'PAH-meh-tahn see, BRAH-teh, toh yeh DOH-brah ee-DEH-yah', "You're smart, man, that's a good idea"),
  ('Pametna si, uvek znaš šta da kažeš', 'PAH-meht-nah see, OO-vek ZNAHSH shtah dah KAH-zhesh', "You're smart, you always know what to say"),
], forms_add=[
  F('Pametna je', 'PAH-meht-nah yeh', 'About a woman (she)', ('Tvoja sestra je pametna', 'TVOH-yah SEH-strah yeh PAH-meht-nah', 'Your sister is smart'), describes='her'),
  F('Pametan je', 'PAH-meh-tahn yeh', 'About a man (he)', ('Njen brat je pametan', 'NYEHN braht yeh PAH-meh-tahn', 'Her brother is smart'), describes='him'),
  F('Pametan sam', 'PAH-meh-tahn sahm', 'Me, a man (joking)', ('Pametan sam, znam', 'PAH-meh-tahn sahm, znahm', "I'm smart, I know (a man says this)"), speaker='male'),
  F('Pametna sam', 'PAH-meht-nah sahm', 'Her, about herself', ('Pametna sam, zar ne?', 'PAH-meht-nah sahm, zahr NEH', "I'm smart, aren't I? (a woman says this)"), speaker='female'),
], changesBy=['describes', 'speaker'], add=[
  X('About an idea', 'To je pametna ideja', 'TOH yeh PAH-meht-nah ee-DEH-yah', "That's a smart idea"),
  X('About someone else', 'Ona je pametna i lepa', 'OH-nah yeh PAH-meht-nah ee LEH-pah', 'She is smart and beautiful'),
])
P['zgodan'] = dict(fx=[
  ('Zgodan si u tom odelu', 'ZGOH-dahn see oo tohm OH-deh-loo', "You're good-looking in that suit (to a man)"),
  ('Zgodna si danas', 'ZGOHD-nah see DAH-nahs', "You're good-looking today (to her)"),
], forms_add=[
  F('Zgodna je', 'ZGOHD-nah yeh', 'About a woman (she)', ('Tvoja drugarica je zgodna', 'TVOH-yah droo-GAH-ree-tsah yeh ZGOHD-nah', 'Your friend is good-looking'), describes='her'),
  F('Zgodan je', 'ZGOH-dahn yeh', 'About a man (he)', ('Njen brat je zgodan', 'NYEHN braht yeh ZGOH-dahn', 'Her brother is good-looking'), describes='him'),
], changesBy=['describes'], add=[
  X('To her', 'Zgodna si u toj haljini', 'ZGOHD-nah see oo toy HAHL-yee-nee', "You look good in that dress"),
  X('To him, from her', 'Zgodan si kad se smeješ', 'ZGOH-dahn see kahd seh SMEH-yesh', "You're good-looking when you smile"),
  X('About someone else', 'Ona je baš zgodna', 'OH-nah yeh BAHSH ZGOHD-nah', "She's really good-looking"),
])
P['smesan'] = dict(fx=[
  ('Smešan si, brate', 'SMEH-shahn see, BRAH-teh', "You're funny, man"),
  ('Smešna si kad se ljutiš', 'SMESH-nah see kahd seh LYOO-teesh', "You're funny when you're angry (to her)"),
], forms_add=[
  F('Smešna je', 'SMESH-nah yeh', 'About a woman (she)', ('Ona je smešna', 'OH-nah yeh SMESH-nah', 'She is funny'), describes='her'),
  F('Smešan je', 'SMEH-shahn yeh', 'About a man (he)', ('Njen tata je smešan', 'NYEHN TAH-tah yeh SMEH-shahn', 'Her dad is funny'), describes='him'),
], changesBy=['describes'], add=[
  X('To her', 'Smešna si, volim to', 'SMESH-nah see, VOH-leem toh', "You're funny, I love that"),
  X('About a thing', 'Taj film je smešan', 'TAH-ee FEELM yeh SMEH-shahn', 'That movie is funny'),
  X('Meaning "ridiculous"', 'To je smešno', 'TOH yeh SMESH-no', "That's ridiculous"),
])
def gendered(m, pm, f, pf, n, pn, pl, ppl, exm, exf, exn, expl, adds):
    return dict(forms=[
      F(m, pm, 'Masculine noun (telefon, film)', exm, nounGender='masculine'),
      F(f, pf, 'Feminine noun (kafa, pesma)', exf, nounGender='feminine'),
      F(n, pn, 'Neuter noun (pivo, vino), or a general "it"', exn, nounGender='neuter'),
      F(pl, ppl, 'More than one thing', expl, nounGender='plural'),
    ], changesBy=['noun gender'], add=adds)
P['ukusno'] = gendered('Ukusan', 'OO-koo-sahn', 'Ukusna', 'OO-koos-nah', 'Ukusno', 'OO-koos-no', 'Ukusni / ukusne', 'OO-koos-nee / OO-koos-neh',
  ('Hleb je ukusan', 'HLEHB yeh OO-koo-sahn', 'The bread is tasty'),
  ('Torta je ukusna', 'TOHR-tah yeh OO-koos-nah', 'The cake is tasty'),
  ('Pivo je ukusno', 'PEE-vo yeh OO-koos-no', 'The beer is tasty'),
  ('Ćevapi su ukusni', 'CHEH-vah-pee soo OO-koos-nee', 'The ćevapi are tasty'),
  [X('To her, about her cooking', 'Sve je ukusno, hvala', 'SVEH yeh OO-koos-no, HVAH-lah', 'Everything is delicious, thanks'),
   X('To her, a compliment', 'Ukusno kuvaš', 'OO-koos-no KOO-vahsh', 'You cook deliciously')])
P['ukusno']['ctx0'] = 'About a thing'
P['skupo'] = gendered('Skup je', 'SKOOP yeh', 'Skupa je', 'SKOO-pah yeh', 'Skupo je', 'SKOO-po yeh', 'Skupi / skupe su', 'SKOO-pee / SKOO-peh soo',
  ('Telefon je skup', 'TEH-leh-fon yeh SKOOP', 'The phone is expensive'),
  ('Kafa je skupa', 'KAH-fah yeh SKOO-pah', 'The coffee is expensive'),
  ('Pivo je skupo', 'PEE-vo yeh SKOO-po', 'The beer is expensive'),
  ('Cipele su skupe', 'TSEE-peh-leh soo SKOO-peh', 'The shoes are expensive'),
  [X('About a general thing', 'Sve je skupo ovde', 'SVEH yeh SKOO-po OHV-deh', 'Everything is expensive here'),
   X('About a place', 'Taj restoran je skup', 'TAH-ee reh-STOH-rahn yeh SKOOP', 'That restaurant is expensive')])
P['skupo']['ctx0'] = 'About a thing'
P['jeftino'] = gendered('Jeftin je', 'YEF-teen yeh', 'Jeftina je', 'YEF-tee-nah yeh', 'Jeftino je', 'YEF-tee-no yeh', 'Jeftini / jeftine su', 'YEF-tee-nee / YEF-tee-neh soo',
  ('Telefon je jeftin', 'TEH-leh-fon yeh YEF-teen', 'The phone is cheap'),
  ('Kafa je jeftina', 'KAH-fah yeh YEF-tee-nah', 'The coffee is cheap'),
  ('Pivo je jeftino', 'PEE-vo yeh YEF-tee-no', 'The beer is cheap'),
  ('Cipele su jeftine', 'TSEE-peh-leh soo YEF-tee-neh', 'The shoes are cheap'),
  [X('About a general thing', 'Sve je jeftino u Srbiji', 'SVEH yeh YEF-tee-no oo SUR-bee-yee', 'Everything is cheap in Serbia'),
   X('About a place', 'Taj restoran je jeftin', 'TAH-ee reh-STOH-rahn yeh YEF-teen', 'That restaurant is cheap')])
P['jeftino']['ctx0'] = 'About a thing'
P['dobro-lose'] = dict(ctx0='Not bad', forms=[
  F('Dobar / loš', 'DOH-bahr / LOHSH', 'Masculine noun, or a man (he)', ('On je dobar. Film je loš', 'OHN yeh DOH-bahr. FEELM yeh LOHSH', 'He is good. The movie is bad'), nounGender='masculine', describes='him'),
  F('Dobra / loša', 'DOH-brah / LOH-shah', 'Feminine noun, or a woman (she)', ('Ona je dobra. Ideja je loša', 'OH-nah yeh DOH-brah. ee-DEH-yah yeh LOH-shah', 'She is good. The idea is bad'), nounGender='feminine', describes='her'),
  F('Dobro / loše', 'DOH-bro / LOH-sheh', 'Neuter noun, or "well / badly"', ('Dobro sam. Loše spavam', 'DOH-bro sahm. LOH-sheh SPAH-vahm', "I'm fine. I sleep badly"), nounGender='neuter'),
], changesBy=['noun gender', 'describes'], add=[
  X('To her', 'Dobra si, hvala ti', 'DOH-brah see, HVAH-lah tee', "You're good (kind), thank you (to her)"),
  X('About a thing', 'Ovo vino je dobro', 'OH-vo VEE-no yeh DOH-bro', 'This wine is good'),
])
P['nije-lose'] = dict(ctx0='Adverb', forms=[
  F('Nije loš', 'NEE-yeh LOHSH', 'Masculine noun, or a man', ('Film nije loš', 'FEELM NEE-yeh LOHSH', "The movie isn't bad"), nounGender='masculine'),
  F('Nije loša', 'NEE-yeh LOH-shah', 'Feminine noun, or a woman', ('Ideja nije loša', 'ee-DEH-yah NEE-yeh LOH-shah', "The idea isn't bad"), nounGender='feminine'),
  F('Nije loše', 'NEE-yeh LOH-sheh', 'Neuter noun, or "not badly"', ('Pivo nije loše', 'PEE-vo NEE-yeh LOH-sheh', "The beer isn't bad"), nounGender='neuter'),
], changesBy=['noun gender'], add=[
  X('To her, about her singing', 'Nije loše pevaš', 'NEE-yeh LOH-sheh PEH-vahsh', "You don't sing badly"),
  X('About someone else', 'On nije loš momak', 'OHN NEE-yeh LOHSH MOH-mahk', "He's not a bad guy"),
])
P['nezgodno'] = dict(ctx0='Me, asking', forms=[
  F('Nezgodno je', 'NEZ-gohd-no yeh', 'It\'s awkward (a situation)', ('Nezgodno je kad se sretnemo', 'NEZ-gohd-no yeh kahd seh SRET-neh-mo', "It's awkward when we run into each other"), describes='it'),
  F('Nezgodno mi je', 'NEZ-gohd-no mee yeh', 'Me: "I feel awkward"', ('Nezgodno mi je da pitam', 'NEZ-gohd-no mee yeh dah PEE-tahm', "It's awkward for me to ask"), describes='me'),
  F('Nezgodno ti je?', 'NEZ-gohd-no tee yeh', 'Asking her: "is it awkward for you?"', ('Nezgodno ti je da pričaš?', 'NEZ-gohd-no tee yeh dah PREE-chahsh', 'Is it awkward for you to talk?'), describes='her', formal='casual'),
  F('Nezgodan trenutak', 'NEZ-go-dahn TREH-noo-tahk', 'Masculine noun: "an awkward moment"', ('Ovo je nezgodan trenutak', 'OH-vo yeh NEZ-go-dahn TREH-noo-tahk', 'This is an awkward moment'), nounGender='masculine'),
  F('Nezgodna situacija', 'NEZ-god-nah see-too-AH-tsee-yah', 'Feminine noun: "an awkward situation"', ('To je nezgodna situacija', 'TOH yeh NEZ-god-nah see-too-AH-tsee-yah', "That's an awkward situation"), nounGender='feminine'),
], changesBy=['describes', 'noun gender'], add=[
  X('To her', 'Nije ti nezgodno da pitaš?', 'NEE-yeh tee NEZ-gohd-no dah PEE-tahsh', "Isn't it awkward for you to ask?"),
  X('About a time', 'Nezgodno je sad, zovem te kasnije', 'NEZ-gohd-no yeh SAHD, ZOH-vem teh KAHS-nee-yeh', "It's not a good time now, I'll call you later"),
])
