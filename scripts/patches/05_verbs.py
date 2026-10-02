P = {}
P['idem'] = dict(ctx0='Me', fx=[
  ('Idem sa tobom', 'EE-dem sah TOH-bom', "I'm going with you"),
  ('Ideš li na žurku?', 'EE-desh lee nah ZHOOR-koo', 'Are you going to the party?'),
  ('Ona ide sutra', 'OH-nah EE-deh SOO-trah', 'She is going tomorrow'),
  ('Idemo na kafu', 'EE-deh-mo nah KAH-foo', "We're going for coffee"),
  ('Idete li vi na slavu?', 'EE-deh-teh lee vee nah SLAH-voo', 'Are you going to the slava?'),
  ('Oni idu kući', 'OH-nee EE-doo KOO-chee', 'They are going home'),
], add=[
  X('To her', 'Kuda ideš?', 'KOO-dah EE-desh', 'Where are you going?'),
  X('About a thing', 'Autobus ide u pet', 'ow-TOH-boos EE-deh oo PET', 'The bus leaves at five'),
])
P['radim'] = dict(ctx0='Me', fx=[
  ('Radim sutra', 'RAH-deem SOO-trah', "I'm working tomorrow"),
  ('Gde radiš?', 'GDEH RAH-deesh', 'Where do you work?'),
  ('On radi u banci', 'OHN RAH-dee oo BAHN-tsee', 'He works at a bank'),
  ('Radimo zajedno', 'RAH-dee-mo ZAH-yeh-dno', 'We work together'),
  ('Šta radite vi?', 'SHTAH RAH-dee-teh VEE', 'What do you do? (polite)'),
  ('Oni rade do osam', 'OH-nee RAH-deh doh OH-sahm', 'They work until eight'),
], add=[
  X('To her', 'Radiš li danas?', 'RAH-deesh lee DAH-nahs', 'Are you working today?'),
  X('About a thing', 'Telefon ne radi', 'TEH-leh-fon neh RAH-dee', "The phone doesn't work"),
])
P['znam'] = dict(ctx0='Me', fx=[
  ('Znam gde je', 'ZNAHM gdeh YEH', 'I know where it is'),
  ('Znaš li gde je?', 'ZNAHSH lee gdeh YEH', 'Do you know where it is?'),
  ('Ona zna sve', 'OH-nah ZNAH SVEH', 'She knows everything'),
  ('Znamo se odavno', 'ZNAH-mo seh OH-dahv-no', 'We have known each other a long time'),
  ('Znate li vi njega?', 'ZNAH-teh lee vee NYEH-gah', 'Do you know him? (polite)'),
  ('Oni znaju', 'OH-nee ZNAH-yoo', 'They know'),
], add=[
  X('To her', 'Znaš šta? Volim te', 'ZNAHSH SHTAH? VOH-leem teh', 'You know what? I love you'),
  X('About a thing', 'Ne znam odgovor', 'neh ZNAHM OD-goh-vor', "I don't know the answer"),
])
P['volim'] = dict(ctx0='About a thing', fx=[
  ('Volim tvoj smeh', 'VOH-leem TVOY SMEH', 'I love your laugh'),
  ('Voliš li kafu?', 'VOH-leesh lee KAH-foo', 'Do you like coffee?'),
  ('On voli fudbal', 'OHN VOH-lee FOOD-bahl', 'He loves football'),
  ('Volimo da putujemo', 'VOH-lee-mo dah poo-TOO-yeh-mo', 'We love to travel'),
  ('Volite li vi vino?', 'VOH-lee-teh lee vee VEE-no', 'Do you like wine? (polite)'),
  ('Oni vole muziku', 'OH-nee VOH-leh MOO-zee-koo', 'They love music'),
], add=[
  X('To her', 'Voliš li more ili planinu?', 'VOH-leesh lee MOH-reh EE-lee plah-NEE-noo', 'Do you like the sea or the mountains?'),
  X('About a feeling', 'Volim kad pada kiša', 'VOH-leem kahd PAH-dah KEE-shah', 'I love it when it rains'),
])
P['mogu'] = dict(ctx0='Me', fx=[
  ('Mogu da dođem', 'MOH-goo dah DOH-jem', 'I can come'),
  ('Možeš li da dođeš?', 'MOH-zhesh lee dah DOH-jesh', 'Can you come?'),
  ('On može sutra', 'OHN MOH-zheh SOO-trah', 'He can do tomorrow'),
  ('Možemo da idemo', 'MOH-zheh-mo dah EE-deh-mo', 'We can go'),
  ('Možete li da pomognete?', 'MOH-zheh-teh lee dah poh-MOHG-neh-teh', 'Can you help? (polite)'),
  ('Oni mogu da stignu', 'OH-nee MOH-goo dah STEEG-noo', 'They can make it'),
], add=[
  X('To her', 'Možeš li da me čekaš?', 'MOH-zhesh lee dah meh CHEH-kahsh', 'Can you wait for me?'),
  X('About a thing', 'To može da bude tačno', 'TOH MOH-zheh dah BOO-deh TAHCH-no', 'That could be true'),
])
P['hocu'] = dict(ctx0='Me', fx=[
  ('Hoću kafu', 'HOH-choo KAH-foo', 'I want a coffee'),
  ('Hoćeš li kafu?', 'HOH-chesh lee KAH-foo', 'Do you want a coffee?'),
  ('Ona hoće da ostane', 'OH-nah HOH-cheh dah OH-stah-neh', 'She wants to stay'),
  ('Hoćemo da idemo', 'HOH-cheh-mo dah EE-deh-mo', 'We want to go'),
  ('Hoćete li kafu?', 'HOH-cheh-teh lee KAH-foo', 'Would you like a coffee? (polite)'),
  ('Oni hoće da plate', 'OH-nee HOH-cheh dah PLAH-teh', 'They want to pay'),
], add=[
  X('To her', 'Hoćeš li da ostaneš još malo?', 'HOH-chesh lee dah OH-stah-nesh yohsh MAH-lo', 'Do you want to stay a bit longer?'),
  X('About a thing (will)', 'Hoće da pada kiša', 'HOH-cheh dah PAH-dah KEE-shah', "It's going to rain"),
])
P['necu'] = dict(ctx0='Me', fx=[
  ('Neću kafu', 'NEH-choo KAH-foo', "I don't want coffee"),
  ('Nećeš da dođeš?', 'NEH-chesh dah DOH-jesh', "You don't want to come?"),
  ('On neće da dođe', 'OHN NEH-cheh dah DOH-jeh', "He doesn't want to come"),
  ('Nećemo stići', 'NEH-cheh-mo STEE-chee', "We won't make it"),
  ('Nećete valjda otići?', 'NEH-cheh-teh VAHL-yah-dah OH-tee-chee', "You're not leaving, are you? (polite)"),
  ('Oni neće da idu', 'OH-nee NEH-cheh dah EE-doo', "They don't want to go"),
], add=[
  X('To her', 'Nećeš valjda da kasniš?', 'NEH-chesh VAHL-yah-dah dah KAHS-neesh', "You're not going to be late, are you?"),
  X('About a thing', 'Neće da pada kiša', 'NEH-cheh dah PAH-dah KEE-shah', "It won't rain"),
])
P['moram'] = dict(ctx0='Me', fx=[
  ('Moram da radim', 'MOH-rahm dah RAH-deem', 'I have to work'),
  ('Moraš da probaš ovo', 'MOH-rahsh dah PROH-bahsh OH-vo', 'You have to try this'),
  ('Ona mora da ide', 'OH-nah MOH-rah dah EE-deh', 'She has to go'),
  ('Moramo da idemo', 'MOH-rah-mo dah EE-deh-mo', 'We have to go'),
  ('Morate da sačekate', 'MOH-rah-teh dah sah-CHEH-kah-teh', 'You have to wait (polite)'),
  ('Moraju da stignu', 'MOH-rah-yoo dah STEEG-noo', 'They have to arrive'),
], add=[
  X('To her, reassuring', 'Ne moraš da ideš', 'neh MOH-rahsh dah EE-desh', "You don't have to go"),
  X('About a thing', 'Mora da je kasno', 'MOH-rah dah yeh KAHS-no', 'It must be late'),
])
P['bio-sam'] = dict(ctx0='Me (man)', fx=[
  ('Bio sam kod tebe', 'BEE-oh sahm kod TEH-beh', 'I was at your place (a man says this)'),
  ('Bila sam na poslu', 'BEE-lah sahm nah POH-sloo', 'I was at work (a woman says this)'),
  ('Bili smo u kafiću', 'BEE-lee smoh oo KAH-fee-choo', 'We were in the café'),
], forms_add=[
  F('Bila si', 'BEE-lah see', 'To her: "you were"', ('Gde si bila?', 'GDEH see BEE-lah', 'Where were you?'), describes='her'),
  F('Bio si', 'BEE-oh see', 'To a man: "you were"', ('Gde si bio, brate?', 'GDEH see BEE-oh, BRAH-teh', 'Where were you, man?'), describes='him'),
  F('Bila je / bio je', 'BEE-lah yeh / BEE-oh yeh', 'About someone else (she / he)', ('Ona je bila tamo. On je bio tamo', 'OH-nah yeh BEE-lah TAH-mo. OHN yeh BEE-oh TAH-mo', 'She was there. He was there'), describes='him / her'),
  F('Bili su', 'BEE-lee soo', 'They were', ('Bili su u Beogradu', 'BEE-lee soo oo beh-oh-GRAH-doo', 'They were in Belgrade'), describes='them'),
], changesBy=['speaker', 'describes', 'tense'], add=[
  X('To her', 'Gde si bila sinoć?', 'GDEH see BEE-lah SEE-nohch', 'Where were you last night?'),
  X('About a thing', 'Film je bio odličan', 'FEELM yeh BEE-oh od-LEECH-ahn', 'The movie was excellent'),
])
P['isao-sam'] = dict(ctx0='Me (man)', fx=[
  ('Išao sam sam', 'EE-shah-oh sahm SAHM', 'I went alone (a man says this)'),
  ('Išla sam sa drugaricom', 'EESH-lah sahm sah droo-GAH-ree-tsom', 'I went with a friend (a woman says this)'),
], forms_add=[
  F('Išla si', 'EESH-lah see', 'To her: "you went"', ('Gde si išla juče?', 'GDEH see EESH-lah YOO-cheh', 'Where did you go yesterday?'), describes='her'),
  F('Išao si', 'EE-shah-oh see', 'To a man: "you went"', ('Kuda si išao?', 'KOO-dah see EE-shah-oh', 'Where did you go?'), describes='him'),
  F('Išla je / išao je', 'EESH-lah yeh / EE-shah-oh yeh', 'About someone else (she / he)', ('Ona je išla kući. On je išao u grad', 'OH-nah yeh EESH-lah KOO-chee. OHN yeh EE-shah-oh oo GRAHD', 'She went home. He went to town'), describes='him / her'),
  F('Išli smo', 'EESH-lee smoh', 'We went', ('Išli smo zajedno', 'EESH-lee smoh ZAH-yeh-dno', 'We went together'), describes='us'),
], changesBy=['speaker', 'describes', 'tense'], add=[
  X('To her', 'Jesi li išla na posao?', 'YEH-see lee EESH-lah nah POH-sah-oh', 'Did you go to work?'),
  X('About someone else', 'Ona je išla sama', 'OH-nah yeh EESH-lah SAH-mah', 'She went alone'),
])
P['video-sam'] = dict(ctx0='Me (man)', fx=[
  ('Video sam film', 'VEE-deh-oh sahm FEELM', 'I saw the movie (a man says this)'),
  ('Videla sam tvoju sestru', 'VEE-deh-lah sahm TVOH-yoo SEH-stroo', 'I saw your sister (a woman says this)'),
], forms_add=[
  F('Videla si', 'VEE-deh-lah see', 'To her: "you saw"', ('Jesi li videla film?', 'YEH-see lee VEE-deh-lah FEELM', 'Did you see the movie?'), describes='her'),
  F('Video si', 'VEE-deh-oh see', 'To a man: "you saw"', ('Jesi li video utakmicu?', 'YEH-see lee VEE-deh-oh oo-TAHK-mee-tsoo', 'Did you see the game?'), describes='him'),
  F('Videla je / video je', 'VEE-deh-lah yeh / VEE-deh-oh yeh', 'About someone else (she / he)', ('Videla je tvoju mamu. Video je film', 'VEE-deh-lah yeh TVOH-yoo MAH-moo. VEE-deh-oh yeh FEELM', 'She saw your mom. He saw the movie'), describes='him / her'),
  F('Videli smo', 'VEE-deh-lee smoh', 'We saw', ('Videli smo ga juče', 'VEE-deh-lee smoh gah YOO-cheh', 'We saw him yesterday'), describes='us'),
], changesBy=['speaker', 'describes', 'tense'], add=[
  X('About her (I saw her)', 'Video sam je juče', 'VEE-deh-oh sahm yeh YOO-cheh', 'I saw her yesterday (a man says this)'),
  X('About him (I saw him)', 'Videla sam ga juče', 'VEE-deh-lah sahm gah YOO-cheh', 'I saw him yesterday (a woman says this)'),
])
P['jeo-sam'] = dict(ctx0='Her, about herself', fx=[
  ('Jeo sam picu', 'YEH-oh sahm PEE-tsoo', 'I ate pizza (a man says this)'),
  ('Jela sam ručak', 'YEH-lah sahm ROO-chahk', 'I ate lunch (a woman says this)'),
], forms_add=[
  F('Jela si', 'YEH-lah see', 'To her: "you ate"', ('Jesi li jela?', 'YEH-see lee YEH-lah', 'Have you eaten?'), describes='her'),
  F('Jeo si', 'YEH-oh see', 'To a man: "you ate"', ('Jesi li jeo?', 'YEH-see lee YEH-oh', 'Have you eaten?'), describes='him'),
  F('Jela je / jeo je', 'YEH-lah yeh / YEH-oh yeh', 'About someone else (she / he)', ('Ona je već jela. On je jeo', 'OH-nah yeh vehch YEH-lah. OHN yeh YEH-oh', 'She already ate. He ate'), describes='him / her'),
  F('Jeli smo', 'YEH-lee smoh', 'We ate', ('Jeli smo kod njih', 'YEH-lee smoh kod NYEEH', 'We ate at their place'), describes='us'),
], changesBy=['speaker', 'describes', 'tense'], add=[
  X('Me (man)', 'Već sam jeo, hvala', 'vehch sahm YEH-oh, HVAH-lah', "I've already eaten, thanks (a man says this)"),
  X('To her', 'Jesi li jela danas?', 'YEH-see lee YEH-lah DAH-nahs', 'Have you eaten today?'),
])
P['zvacu-te'] = dict(ctx0='Me, to her', forms=[
  F('Zvaću te', 'ZVAH-choo teh', 'Me: "I\'ll call you" (man or woman)', ('Zvaću te sutra', 'ZVAH-choo teh SOO-trah', "I'll call you tomorrow"), describes='me'),
  F('Zvaćeš me?', 'ZVAH-chesh meh', 'Asking her: "will you call me?"', ('Zvaćeš me večeras?', 'ZVAH-chesh meh VEH-cheh-rahs', 'Will you call me tonight?'), describes='her', formal='casual'),
  F('Zvaće te', 'ZVAH-cheh teh', 'Someone else will call you', ('Zvaće te moja mama', 'ZVAH-cheh teh MOH-yah MAH-mah', 'My mom will call you'), describes='him / her'),
  F('Zvaćemo te', 'ZVAH-cheh-mo teh', 'We will call you', ('Zvaćemo te kad stignemo', 'ZVAH-cheh-mo teh kahd STEEG-neh-mo', "We'll call you when we arrive"), describes='us'),
  F('Zvaću vas', 'ZVAH-choo vahs', 'Polite, to an elder', ('Zvaću vas u ponedeljak', 'ZVAH-choo vahs oo poh-NEH-deh-lyahk', "I'll call you on Monday"), formal='polite'),
], changesBy=['describes', 'formal'], add=[
  X('To him', 'Zvaću te, brate', 'ZVAH-choo teh, BRAH-teh', "I'll call you, man"),
  X('About someone else', 'Zvaću je kasnije', 'ZVAH-choo yeh KAHS-nee-yeh', "I'll call her later"),
])
P['javicu-se'] = dict(ctx0='Me, to her', forms=[
  F('Javiću se', 'YAH-vee-choo seh', 'Me: "I\'ll be in touch"', ('Javiću se čim stignem', 'YAH-vee-choo seh cheem STEEG-nem', "I'll be in touch as soon as I arrive"), describes='me'),
  F('Javićeš se?', 'YAH-vee-chesh seh', 'Asking her: "will you get in touch?"', ('Javićeš se kad stigneš?', 'YAH-vee-chesh seh kahd STEEG-nesh', 'Will you let me know when you arrive?'), describes='her', formal='casual'),
  F('Javiće se', 'YAH-vee-cheh seh', 'Someone else will get in touch', ('Javiće se sutra', 'YAH-vee-cheh seh SOO-trah', 'He / she will be in touch tomorrow'), describes='him / her'),
  F('Javićemo se', 'YAH-vee-cheh-mo seh', 'We will be in touch', ('Javićemo se vama', 'YAH-vee-cheh-mo seh VAH-mah', "We'll be in touch with you"), describes='us'),
], changesBy=['describes'], add=[
  X('To her, promise', 'Javiću se večeras, obećavam', 'YAH-vee-choo seh VEH-cheh-rahs, oh-beh-CHAH-vahm', "I'll be in touch tonight, I promise"),
  X('About someone else', 'Rekla je da će se javiti', 'REK-lah yeh dah cheh seh YAH-vee-tee', 'She said she would get in touch'),
])
P['videcemo-se'] = dict(ctx0='Us', forms=[
  F('Videćemo se', 'VEE-deh-cheh-mo seh', 'We\'ll see each other / we\'ll see', ('Videćemo se u petak', 'VEE-deh-cheh-mo seh oo PEH-tahk', "We'll see each other on Friday"), describes='us'),
  F('Videću te', 'VEE-deh-choo teh', 'Me: "I\'ll see you"', ('Videću te sutra', 'VEE-deh-choo teh SOO-trah', "I'll see you tomorrow"), describes='me'),
  F('Videćeš!', 'VEE-deh-chesh', 'To her: "you\'ll see!"', ('Videćeš, biće lepo', 'VEE-deh-chesh, BEE-cheh LEH-po', "You'll see, it'll be nice"), describes='her', formal='casual'),
  F('Videće se', 'VEE-deh-cheh seh', 'Vague: "we\'ll see"', ('Videće se, ne obećavam', 'VEE-deh-cheh seh, neh oh-beh-CHAH-vahm', "We'll see, I don't promise"), describes='it'),
], changesBy=['describes'], add=[
  X('Her, to me', 'Videćemo se, ljubavi', 'VEE-deh-cheh-mo seh, LYOO-bah-vee', "We'll see each other, my love"),
  X('About someone else', 'Videće je u subotu', 'VEE-deh-cheh yeh oo SOO-boh-too', "He'll see her on Saturday"),
])
P['dodji'] = dict(ctx0='To her', fx=[
  ('Dođi kod mene večeras', 'DOH-jee kod MEH-neh VEH-cheh-rahs', 'Come to my place tonight'),
  ('Dođite svi', 'DOH-jee-teh SVEE', 'Come, all of you'),
], add=[
  X('To him', 'Dođi, brate, čekamo te', 'DOH-jee, BRAH-teh, CHEH-kah-mo teh', "Come, man, we're waiting for you"),
  X('About someone else', 'Neka dođe i ona', 'NEH-kah DOH-jeh ee OH-nah', 'Let her come too'),
  X('About a thing', 'Dođi da vidiš ovo', 'DOH-jee dah VEE-deesh OH-vo', 'Come see this'),
])
P['cekaj'] = dict(ctx0='To her', fx=[
  ('Čekaj me ispred', 'CHEH-kai meh EES-pred', 'Wait for me outside'),
  ('Čekajte nas, molim vas', 'CHEH-kai-teh NAHS, MOH-leem vahs', 'Please wait for us (polite)'),
], forms_add=[
  F('Čekam te', 'CHEH-kahm teh', 'Me: "I\'m waiting for you"', ('Čekam te ispred', 'CHEH-kahm teh EES-pred', "I'm waiting for you outside"), describes='me'),
  F('Čeka te', 'CHEH-kah teh', 'Someone else is waiting for you', ('Mama te čeka', 'MAH-mah teh CHEH-kah', 'Mom is waiting for you'), describes='him / her'),
], changesBy=['formal', 'describes'], add=[
  X('To him', 'Čekaj, brate, stižem', 'CHEH-kai, BRAH-teh, STEE-zhem', "Wait, man, I'm coming"),
  X('About someone else', 'Čekaj ga', 'CHEH-kai gah', 'Wait for him'),
])
P['javi-se'] = dict(ctx0='To her', fx=[
  ('Javi se čim stigneš', 'YAH-vee seh cheem STEEG-nesh', 'Let me know as soon as you arrive'),
  ('Javite se kad stignete', 'YAH-vee-teh seh kahd STEEG-neh-teh', 'Let us know when you arrive (polite)'),
], add=[
  X('To him', 'Javi se, brate', 'YAH-vee seh, BRAH-teh', 'Text me, man'),
  X('About someone else', 'Neka se javi', 'NEH-kah seh YAH-vee', 'Let him / her get in touch'),
  X('Me, asking for news', 'Javi mi kad stigne paket', 'YAH-vee mee kahd STEEG-neh PAH-ket', 'Let me know when the package arrives'),
])
P['spavaj'] = dict(ctx0='To her', fx=[
  ('Spavaj lepo, lepotice', 'SPAH-vai LEH-po, leh-poh-TEE-tseh', 'Sleep well, beautiful'),
  ('Spavajte lepo', 'SPAH-vai-teh LEH-po', 'Sleep well (polite)'),
], forms_add=[
  F('Spavam', 'SPAH-vahm', 'Me: "I\'m sleeping"', ('Idem da spavam', 'EE-dem dah SPAH-vahm', "I'm going to sleep"), describes='me'),
  F('Spava', 'SPAH-vah', 'Someone else is sleeping', ('Ona već spava', 'OH-nah vehch SPAH-vah', 'She is already asleep'), describes='him / her'),
], changesBy=['formal', 'describes'], add=[
  X('To him', 'Spavaj, brate, kasno je', 'SPAH-vai, BRAH-teh, KAHS-no yeh', "Sleep, man, it's late"),
  X('About me', 'Ne spavam, čekam te', 'neh SPAH-vahm, CHEH-kahm teh', "I'm not sleeping, I'm waiting for you"),
])
