P = {}
P['hello'] = dict(ctx0='To her', add=[
  X('To a group', 'Zdravo svima!', 'ZDRAH-voh SVEE-mah', 'Hi everyone!'),
  X('Introducing yourself', 'Zdravo, ja sam Met', 'ZDRAH-voh, yah sahm MET', "Hi, I'm Matt"),
  X('About someone else', 'On ti kaže zdravo', 'OHN tee KAH-zheh ZDRAH-voh', 'He says hi to you'),
])
P['cao'] = dict(ctx0='Leaving (to her)', add=[
  X('Greeting a friend', 'Ćao, Ana!', 'CHOW, AH-nah', 'Hi, Ana!'),
  X('Leaving a group', 'Ćao svima, vidimo se!', 'CHOW SVEE-mah, VEE-dee-mo seh', 'Bye everyone, see you!'),
  X('Playful double', 'Ćao, ćao!', 'CHOW, CHOW', 'Bye bye!'),
])
P['see-you'] = dict(ctx0='Talking later (text / call)', add=[
  X('Setting a day', 'Vidimo se u petak', 'VEE-dee-mo seh oo PEH-tahk', 'See you on Friday'),
  X('Later today', 'Vidimo se kasnije', 'VEE-dee-mo seh KAH-sneeh-yeh', 'See you later'),
  X('Asking her', 'Vidimo se večeras?', 'VEE-dee-mo seh VEH-cheh-rahs', 'See you tonight?'),
])
P['good-morning'] = dict(ctx0='To her', add=[
  X('To him', 'Dobro jutro! Kako si spavao?', 'DOH-bro YOO-tro! KAH-ko see SPAH-vah-oh', 'Good morning! How did you sleep? (to a man)'),
  X('About me (man)', 'Dobro jutro! Spavao sam odlično', 'DOH-bro YOO-tro! SPAH-vah-oh sahm od-LEECH-no', 'Good morning! I slept great'),
  X('Her, about herself', 'Dobro jutro! Spavala sam odlično', 'DOH-bro YOO-tro! SPAH-vah-lah sahm od-LEECH-no', 'Good morning! I slept great (a woman says this)'),
  X('Polite / to her parents', 'Dobro jutro! Kako ste spavali?', 'DOH-bro YOO-tro! KAH-ko steh SPAH-vah-lee', 'Good morning! How did you sleep? (polite)'),
])
P['laku-noc'] = dict(ctx0='Leaving a chat', add=[
  X('To her', 'Laku noć, lepo sanjaj', 'LAH-koo NOHTCH, LEH-po SAH-nyai', 'Good night, sweet dreams'),
  X('To a group', 'Laku noć svima', 'LAH-koo NOHTCH SVEE-mah', 'Good night, everyone'),
  X('About me', 'Idem da spavam, laku noć', 'EE-dehm dah SPAH-vahm, LAH-koo NOHTCH', "I'm going to sleep, good night"),
  X('To her parents (polite)', 'Laku noć, hvala na svemu', 'LAH-koo NOHTCH, HVAH-lah nah SVEH-moo', 'Good night, thanks for everything'),
])
P['kako-si'] = dict(ctx0='To a friend', add=[
  X('To her', 'Hej, kako si danas?', 'HAY, KAH-ko see DAH-nahs', 'Hey, how are you today?'),
  X('About someone else', 'Kako je tvoja mama?', 'KAH-ko yeh TVOH-yah MAH-mah', 'How is your mom?'),
  X('About something', 'Kako je posao?', 'KAH-ko yeh POH-sah-oh', "How's work?"),
  X('To a group', 'Kako ste svi?', 'KAH-ko steh SVEE', 'How are you all?'),
], fx=[('Ćao, Ana, kako si?', 'CHOW, AH-nah, KAH-ko see', 'Hi, Ana, how are you?'),
       ('Dobar dan, gospođo, kako ste?', 'DOH-bar DAHN, GOH-spoh-jo, KAH-ko steh', 'Good day, ma’am, how are you?')])
P['sta-ima'] = dict(ctx0=['To her', 'Answering'], add=[
  X('To her, asking for news', 'Šta ima novo?', 'SHTAH EE-mah NOH-vo', "What's new?"),
  X('About me', 'Ništa posebno, radim', 'NEESH-tah POH-seh-bno, RAH-deem', 'Nothing special, working'),
  X('About someone else', 'Šta ima kod Marka?', 'SHTAH EE-mah kod MAHR-kah', "What's new with Marko?"),
])
P['dobro-sam'] = dict(ctx0='Me, answering', add=[
  X('About me (man)', 'Dobro sam, samo sam malo umoran', 'DOH-bro sahm, SAH-mo sahm MAH-lo OO-mo-rahn', "I'm good, just a bit tired"),
  X('Her, about herself', 'Dobro sam, samo sam malo umorna', 'DOH-bro sahm, SAH-mo sahm MAH-lo OO-mor-nah', "I'm good, just a bit tired (a woman says this)"),
  X('About someone else', 'Ona je dobro, hvala što pitaš', 'OH-nah yeh DOH-bro, HVAH-lah shtoh PEE-tahsh', "She's good, thanks for asking"),
  X('About things', 'Sve je dobro, hvala', 'SVEH yeh DOH-bro, HVAH-lah', "Everything's good, thanks"),
], forms=[
  F('Dobro sam', 'DOH-bro sahm', 'Me, about myself', ('Dobro sam, hvala', 'DOH-bro sahm, HVAH-lah', "I'm good, thanks"), describes='me'),
  F('Dobro si?', 'DOH-bro see', 'Asking her if she is OK', ('Jesi li dobro? Dobro si?', 'YEH-see lee DOH-bro? DOH-bro see', 'Are you OK? You good?'), describes='her', formal='casual'),
  F('Dobro ste?', 'DOH-bro steh', 'Polite, to an elder or a group', ('Da li ste dobro? Dobro ste?', 'dah lee steh DOH-bro? DOH-bro steh', 'Are you all right?'), formal='polite'),
  F('Dobro je', 'DOH-bro yeh', 'Someone else (he / she) or a thing', ('On je dobro. Sve je dobro', 'OHN yeh DOH-bro. SVEH yeh DOH-bro', "He's fine. Everything is fine"), describes='him / her'),
  F('Dobro smo', 'DOH-bro smoh', 'Us', ('Dobro smo, hvala', 'DOH-bro smoh, HVAH-lah', "We're good, thanks"), describes='us'),
], changesBy=['describes', 'formal'])
P['im-tired'] = dict(ctx0='About me (man)', fx=[
  ('Umoran sam, idem da spavam', 'OO-mo-rahn sahm, EE-dehm dah SPAH-vahm', "I'm tired, I'm going to sleep"),
  ('Umorna sam posle posla', 'OO-mor-nah sahm POH-sleh POH-slah', "I'm tired after work (a woman says this)"),
  ('Umoran si? Idi spavaj', 'OO-mo-rahn see? EE-dee SPAH-vai', "You're tired? Go to sleep (to a man)"),
  ('Umorna si? Spavaj lepo', 'OOM-or-nah see? SPAH-vai LEH-po', "Are you tired? Sleep well (to her)"),
  ('Umorni smo, ali srećni', 'OO-mor-nee smoh, ah-lee SRETCH-nee', "We're tired but happy"),
], forms_add=[
  F('Umoran je', 'OO-mo-rahn yeh', 'Telling someone about a man (he)', ('Marko je umoran, ceo dan radi', 'MAHR-ko yeh OO-mo-rahn, TSEH-oh dahn RAH-dee', "Marko is tired, he's been working all day"), describes='him'),
  F('Umorna je', 'OOM-or-nah yeh', 'Telling someone about a woman (she)', ('Tvoja sestra je umorna', 'TVOH-yah SEH-strah yeh OOM-or-nah', 'Your sister is tired'), describes='her'),
  F('Umorni su', 'OO-mor-nee soo', 'They (mixed group or all men)', ('Deca su umorna', 'DEH-tsah soo OO-mor-nah', 'The kids are tired'), describes='them'),
], add=[
  X('About a thing', 'Taj dan je bio naporan', 'TAH-ee DAHN yeh BEE-oh NAH-poh-rahn', 'That day was exhausting'),
  X('Her, explaining', 'Umorna sam, nisam spavala', 'OO-mor-nah sahm, NEE-sahm SPAH-vah-lah', "I'm tired, I didn't sleep (a woman says this)"),
])
P['im-happy'] = dict(ctx0='About me (man)', fx=[
  ('Srećan sam što te vidim', 'SREH-chahn sahm shtoh teh VEE-deem', "I'm happy to see you"),
  ('Srećna sam što dolaziš', 'SRETCH-nah sahm shtoh DOH-lah-zeesh', "I'm happy you're coming (a woman says this)"),
  ('Srećna si, vidi se', 'SRETCH-nah see, VEE-dee seh', "You're happy, you can tell (to her)"),
], forms_add=[
  F('Srećan je', 'SREH-chahn yeh', 'About a man (he)', ('Brat je srećan zbog posla', 'BRAHT yeh SREH-chahn zbog POH-slah', "My brother is happy about his job"), describes='him'),
  F('Srećna je', 'SRETCH-nah yeh', 'About a woman (she)', ('Mama je srećna što dolaziš', 'MAH-mah yeh SRETCH-nah shtoh DOH-lah-zeesh', "Mom is happy you're coming"), describes='her'),
  F('Srećni smo', 'SRETCH-nee smoh', 'Us (mixed group)', ('Srećni smo zajedno', 'SRETCH-nee smoh ZAH-yeh-dno', "We're happy together"), describes='us'),
], add=[X('Short and sweet', 'Srećan sam', 'SREH-chahn sahm', "I'm happy (a man says this)"),
  X('Her, about herself', 'Srećna sam danas', 'SRETCH-nah sahm DAH-nahs', "I'm happy today (a woman says this)")])
P['thank-you'] = dict(ctx0='To her', forms=[
  F('Hvala', 'HVAH-lah', 'The basic thanks, to anyone', ('Hvala, to je to', 'HVAH-lah, toh yeh TOH', "Thanks, that's it"), formal='casual'),
  F('Hvala ti', 'HVAH-lah tee', 'To one friend: a warmer thanks', ('Hvala ti za večeras', 'HVAH-lah tee zah VEH-cheh-rahs', 'Thank you for tonight'), formal='casual'),
  F('Hvala vam', 'HVAH-lah vahm', 'Polite, to an elder or group', ('Hvala vam na pozivu', 'HVAH-lah vahm nah POH-zee-voo', 'Thank you for the invitation'), formal='polite'),
], changesBy=['formal'], add=[
  X('Thanking her for coming', 'Hvala što si došla', 'HVAH-lah shtoh see DOH-shlah', 'Thanks for coming (to her)'),
  X('Thanking him for coming', 'Hvala što si došao', 'HVAH-lah shtoh see DOH-shah-oh', 'Thanks for coming (to a man)'),
  X('Thanks for help', 'Hvala na pomoći', 'HVAH-lah nah POH-mo-chee', 'Thanks for the help'),
  X('Replying to thanks', 'Nema na čemu', 'NEH-mah nah CHEH-moo', "You're welcome"),
])
P['sorry'] = dict(ctx0='Me, about being late', fx=[
  ('Izvini, nisam hteo', 'eez-VEE-nee, NEE-sahm HTEH-oh', "Sorry, I didn't mean to (a man says this)"),
  ('Izvinite, gde je toalet?', 'eez-VEE-nee-teh, GDEH yeh toh-AH-let', 'Excuse me, where is the restroom?'),
], add=[
  X('Her, about herself', 'Izvini, nisam htela', 'eez-VEE-nee, NEE-sahm HTEH-lah', "Sorry, I didn't mean to (a woman says this)"),
  X('Me, admitting a mistake', 'Izvini, pogrešio sam', 'eez-VEE-nee, poh-GREH-shee-oh sahm', 'Sorry, I made a mistake (a man says this)'),
  X('Her, admitting a mistake', 'Izvini, pogrešila sam', 'eez-VEE-nee, poh-GREH-shee-lah sahm', 'Sorry, I made a mistake (a woman says this)'),
  X('About someone else', 'On kaže da mu je žao', 'OHN KAH-zheh dah moo yeh ZHAH-oh', 'He says he is sorry'),
])
P['please'] = dict(ctx0='To her', fx=[
  ('Molim te, javi se čim stigneš', 'MOH-leem teh, YAH-vee seh cheem STEEG-nesh', 'Please text me as soon as you arrive'),
  ('Molim vas, jednu kafu', 'MOH-leem vahs, YED-noo KAH-foo', 'One coffee, please (to a waiter)'),
], add=[
  X('Begging her', 'Molim te, nemoj da se ljutiš', 'MOH-leem teh, NEH-moy dah seh LYOO-teesh', "Please don't be mad"),
  X('Not hearing', 'Molim? Nisam čuo', 'MOH-leem? NEE-sahm CHOO-oh', "Pardon? I didn't hear (a man says this)"),
  X('Her, not hearing', 'Molim? Nisam čula', 'MOH-leem? NEE-sahm CHOO-lah', "Pardon? I didn't hear (a woman says this)"),
])
P['ludilo'] = dict(ctx0='About news', add=[
  X('About a thing', 'Ludilo koliko je gužva', 'LOO-dee-lo KOH-lee-ko yeh GOOZH-vah', "It's crazy how crowded it is"),
  X('About her', 'Ona je ludilo!', 'OH-nah yeh LOO-dee-lo', "She's amazing! (about a woman)"),
  X('About me (man)', 'Ludilo! Prošao sam ispit', 'LOO-dee-lo! PROH-shah-oh sahm EES-peet', 'Wow! I passed the exam'),
  X('Her, about herself', 'Ludilo! Prošla sam ispit', 'LOO-dee-lo! PROSH-lah sahm EES-peet', 'Wow! I passed the exam (a woman says this)'),
])
P['dying-laughing'] = dict(ctx0='Me, reacting', forms=[
  F('Umirem od smeha', 'oo-MEE-rem od SMEH-hah', 'Me, right now', ('Umirem od smeha, pošalji još', 'oo-MEE-rem od SMEH-hah, POH-shah-lyee yohsh', "I'm dying laughing, send more"), describes='me'),
  F('Umireš od smeha', 'oo-MEE-resh od SMEH-hah', 'You, to her', ('Vidim da umireš od smeha', 'VEE-deem dah oo-MEE-resh od SMEH-hah', 'I can see you are dying laughing'), describes='her', formal='casual'),
  F('Umire od smeha', 'oo-MEE-reh od SMEH-hah', 'Someone else (he / she)', ('Moja sestra umire od smeha', 'MOH-yah SEH-strah oo-MEE-reh od SMEH-hah', 'My sister is dying laughing'), describes='him / her'),
  F('Umiremo od smeha', 'oo-MEE-reh-mo od SMEH-hah', 'Us', ('Umiremo od smeha zajedno', 'oo-MEE-reh-mo od SMEH-hah ZAH-yeh-dno', "We're dying laughing together"), describes='us'),
], changesBy=['describes'], add=[X('Past, same for both', 'Crkoh od smeha!', 'TSUR-koh od SMEH-hah', 'I died laughing! (man or woman)'),
  X('Sending a meme', 'Umirem, pogledaj ovo', 'oo-MEE-rem, POH-gleh-dai OH-vo', "I'm dying, look at this")])
P['funny'] = dict(ctx0='About a thing', forms=[
  F('Baš je smešno', 'BAHSH yeh SMESH-no', 'About a situation or joke', ('Baš je smešno, ne mogu', 'BAHSH yeh SMESH-no, neh MOH-goo', "That's so funny, I can't"), describes='it'),
  F('Baš si smešna', 'BAHSH see SMESH-nah', 'To her', ('Baš si smešna večeras', 'BAHSH see SMESH-nah VEH-cheh-rahs', "You're really funny tonight"), describes='her'),
  F('Baš si smešan', 'BAHSH see SMEH-shahn', 'To a man', ('Baš si smešan, brate', 'BAHSH see SMEH-shahn, BRAH-teh', "You're really funny, man"), describes='him'),
  F('Baš je smešan / smešna', 'BAHSH yeh SMEH-shahn / SMESH-nah', 'About someone else (he / she)', ('Tvoj brat je baš smešan', 'TVOY braht yeh BAHSH SMEH-shahn', 'Your brother is really funny'), describes='him / her'),
], changesBy=['describes'], add=[X('About a film', 'Film je bio baš smešan', 'FEELM yeh BEE-oh BAHSH SMEH-shahn', 'The movie was really funny'),
  X('About a show', 'Serija je baš smešna', 'SEH-ree-yah yeh BAHSH SMESH-nah', 'The series is really funny')])
P['ma-daj'] = dict(ctx0='Disbelief', add=[
  X('To her', 'Ma daj, nisi ozbiljna', 'mah DAH-ee, NEE-see OHZ-beel-nah', "Come on, you're not serious (to her)"),
  X('To him', 'Ma daj, nisi ozbiljan', 'mah DAH-ee, NEE-see OHZ-bee-lyahn', "Come on, you're not serious (to a man)"),
  X('About someone else', 'Ma daj, on to nikad ne bi rekao', 'mah DAH-ee, ohn toh NEE-kahd neh bee REH-kah-oh', "No way, he would never say that"),
  X('About me (man)', 'Ma daj, nisam ja kriv', 'mah DAH-ee, NEE-sahm yah KREEV', "Come on, it's not my fault (a man says this)"),
])
P['ma-nemoj'] = dict(ctx0='Sarcasm, to her', add=[
  X('To her, sarcastic', 'Ma nemoj, pa ti si to znala', 'mah NEH-moy, pah tee see toh ZNAH-lah', 'Yeah right, you knew that all along (to her)'),
  X('To him, sarcastic', 'Ma nemoj, pa ti si to znao', 'mah NEH-moy, pah tee see toh ZNAH-oh', 'Yeah right, you knew that all along (to a man)'),
  X('About someone else', 'Ma nemoj, on je to platio?', 'mah NEH-moy, ohn yeh toh PLAH-tee-oh', 'No way, he paid for that?'),
  X('Different meaning', 'Ma nemoj da kukaš', 'mah NEH-moy dah KOO-kahsh', "Come on, don't whine"),
])
P['salis-se'] = dict(ctx0='To a friend', fx=[
  ('Šališ se, ne mogu da verujem', 'SHAH-leesh seh, neh MOH-goo dah VEH-roo-yem', "You're kidding, I can't believe it"),
  ('Šalite se, zar stvarno?', 'SHAH-lee-teh seh, zahr STVAHR-no', "You must be joking, really?"),
], forms_add=[
  F('Šalim se', 'SHAH-leem seh', 'Me: "I\'m joking"', ('Ne šalim se, ozbiljno', 'neh SHAH-leem seh, OHZ-beel-yno', "I'm not kidding, seriously"), describes='me'),
  F('Šali se', 'SHAH-lee seh', 'Someone else (he / she)', ('On se šali, ne brini', 'OHN seh SHAH-lee, neh BREE-nee', "He's joking, don't worry"), describes='him / her'),
  F('Šalimo se', 'SHAH-lee-mo seh', 'Us', ('Samo se šalimo', 'SAH-mo seh SHAH-lee-mo', "We're just joking"), describes='us'),
], changesBy=['formal', 'describes'], add=[X('To her, a bit worried', 'Šališ se, zar ne? Nije to istina', 'SHAH-leesh seh, zahr NEH? NEE-yeh toh EES-tee-nah', "You're kidding, right? It's not true"),
  X('About a thing', 'Šališ se, to je preskupo', 'SHAH-leesh seh, toh yeh preh-SKOO-po', "You're kidding, that's way too expensive")])
P['cool'] = dict(ctx0='About a plan', add=[
  X('About me', 'Super sam, hvala', 'SOO-per sahm, HVAH-lah', "I'm great, thanks (same for a man or a woman)"),
  X('To her', 'Super si!', 'SOO-per see', "You're great! (same for a man or a woman)"),
  X('About someone else', 'On je super tip', 'OHN yeh SOO-per TEEP', "He's a great guy"),
  X('About a thing', 'Ovo je super', 'OH-vo yeh SOO-per', 'This is great'),
])
P['bezveze'] = dict(ctx0=['About a thing', 'Me, just asking (man)'], add=[
  X('Her, just asking', 'Ništa, bezveze sam pitala', 'NEESH-tah, BEZ-veh-zeh sahm PEE-tah-lah', 'Nothing, I was just asking (a woman says this)'),
  X('About someone else', 'On je malo bezveze', 'OHN yeh MAH-lo BEZ-veh-zeh', "He's kind of lame"),
  X('About a mood', 'Nešto mi je bezveze danas', 'NEHSH-to mee yeh BEZ-veh-zeh DAH-nahs', "I'm feeling kind of meh today"),
])
P['bre'] = dict(ctx0='Between friends', add=[
  X('To her, playful', 'Bre, pa ti si luda!', 'BREH, pah tee see LOO-dah', "Girl, you're crazy!"),
  X('To him', 'Šta je bre?', 'SHTAH yeh BREH', "What's up, man?"),
  X('Annoyed', 'Pa dobro bre, dolazim', 'pah DOH-bro BREH, DOH-lah-zeem', "Alright, man, I'm coming"),
])
P['ajde'] = dict(ctx0=['Let’s go', 'Ending a chat'], fx=[
  ('Ajde, pričaj mi', 'AY-deh, PREE-chai mee', 'Come on, tell me (to her)'),
  ('Ajmo na kafu!', 'AY-mo nah KAH-foo', "Let's go for a coffee!"),
  ('Ajte, sedite', 'AY-teh, SEH-dee-teh', 'Come on, sit down (to a group)'),
], add=[
  X('Encouraging her', 'Ajde, javi se', 'AY-deh, YAH-vee seh', 'Come on, text me'),
  X('About someone else', 'Ajde, on dolazi', 'AY-deh, ohn DOH-lah-zee', "OK, he's coming"),
])
P['joj'] = dict(ctx0='Sympathy', add=[
  X('About me (man)', 'Joj, zaboravio sam', 'YOY, zah-BOH-rah-vee-oh sahm', 'Oh no, I forgot (a man says this)'),
  X('Her, about herself', 'Joj, zaboravila sam', 'YOY, zah-BOH-rah-vee-lah sahm', 'Oh no, I forgot (a woman says this)'),
  X('To her', 'Joj, jadna ti', 'YOY, YAHD-nah tee', 'Oh, poor you (to her)'),
  X('About someone else', 'Joj, jadan on', 'YOY, YAH-dahn ohn', 'Oh, poor him'),
  X('About a thing', 'Joj, kako je hladno!', 'YOY, KAH-ko yeh HLAHD-no', "Ugh, it's so cold!"),
])
P['nzm'] = dict(ctx0='Me', forms=[
  F('Ne znam', 'neh ZNAHM', 'Me: "I don\'t know"', ('Ne znam, možda', 'neh ZNAHM, MOHZH-dah', "I don't know, maybe"), describes='me'),
  F('Ne znaš', 'neh ZNAHSH', 'You, to her', ('Ne znaš? Pitaj Anu', 'neh ZNAHSH? PEE-tai AH-noo', "You don't know? Ask Ana"), describes='her', formal='casual'),
  F('Ne zna', 'neh ZNAH', 'Someone else (he / she)', ('On ne zna gde je', 'OHN neh ZNAH gdeh YEH', "He doesn't know where it is"), describes='him / her'),
  F('Ne znamo', 'neh ZNAH-mo', 'Us', ('Ne znamo još', 'neh ZNAH-mo YOHSH', "We don't know yet"), describes='us'),
  F('Ne znate', 'neh ZNAH-teh', 'Polite, or to a group', ('Ne znate? Pitajte ga', 'neh ZNAH-teh? PEE-tai-teh gah', "You don't know? Ask him"), formal='polite'),
  F('Ne znaju', 'neh ZNAH-yoo', 'They', ('Oni ne znaju ništa', 'OH-nee neh ZNAH-yoo NEESH-tah', "They don't know anything"), describes='them'),
], changesBy=['describes', 'formal'], add=[X('Texting version', 'nzm, ti?', 'neh ZNAHM, tee', "idk, you?"),
  X('Asked about a plan', 'Ne znam još kad stižem', 'neh ZNAHM yohsh kahd STEE-zhem', "I don't know yet when I'm arriving")])
