P = {}
P['tacno'] = dict(ctx0='Me (man)', add=[
  X('Her, about herself', 'Tačno, to sam i ja mislila', 'TAHCH-no, toh sahm ee yah MEE-slee-lah', "Exactly, that's what I thought too (a woman says this)"),
  X('To her', 'Tačno, u pravu si', 'TAHCH-no, oo PRAH-voo see', "Exactly, you're right"),
  X('About someone else', 'Tačno, on je to rekao', 'TAHCH-no, ohn yeh toh REH-kah-oh', 'Right, he did say that'),
  X('About a thing', 'Tačno, to je to', 'TAHCH-no, toh yeh TOH', "Exactly, that's it"),
])
P['aha'] = dict(ctx0='Listening', add=[
  X('Now I get it', 'Aha, sad kapiram', 'AH-hah, sahd KAH-pee-rahm', 'Aha, now I get it'),
  X('To her, following a story', 'Aha, i šta je ona rekla?', 'AH-hah, ee SHTAH yeh OH-nah REK-lah', 'Uh-huh, and what did she say?'),
  X('To her', 'Aha, znači ti dolaziš?', 'AH-hah, ZNAH-chee tee DOH-lah-zeesh', 'Aha, so you are coming?'),
  X('Short and clear', 'Aha, jasno', 'AH-hah, YAHS-no', 'Aha, clear'),
])
P['stvarno'] = dict(ctx0='Me (man)', add=[
  X('Her, about herself', 'Stvarno? Nisam znala', 'STVAHR-no? NEE-sahm ZNAH-lah', "Really? I didn't know (a woman says this)"),
  X('To her', 'Stvarno hoćeš da dođeš?', 'STVAHR-no HOH-chesh dah DOH-jesh', 'Do you really want to come?'),
  X('About someone else', 'Stvarno? On je to rekao?', 'STVAHR-no? ohn yeh toh REH-kah-oh', 'Really? He said that?'),
  X('About a thing', 'Stvarno je lepo ovde', 'STVAHR-no yeh LEH-po OHV-deh', "It's really nice here"),
])
P['znaci'] = dict(ctx0='To her', add=[
  X('To her, checking', 'Znači, ti dolaziš sutra?', 'ZNAH-chee, tee DOH-lah-zeesh SOO-trah', 'So, you are coming tomorrow?'),
  X('Summing up', 'Znači, nema problema', 'ZNAH-chee, NEH-mah PROH-bleh-mah', 'So, no problem'),
  X('About someone else', 'Znači, on ne dolazi?', 'ZNAH-chee, ohn neh DOH-lah-zee', "So, he's not coming?"),
  X('Real meaning', 'Šta to znači?', 'SHTAH toh ZNAH-chee', 'What does that mean?'),
])
P['pa'] = dict(ctx0='Hesitating', add=[
  X('To her', 'Pa, ti znaš najbolje', 'PAH, tee ZNAHSH NAI-bol-yeh', 'Well, you know best'),
  X('About someone else', 'Pa on nije znao', 'PAH ohn NEE-yeh ZNAH-oh', "Well, he didn't know"),
  X('Giving in', 'Pa dobro, ajde', 'PAH DOH-bro, AY-deh', 'Well OK, fine'),
  X('Meaning "then"', 'Pa dođi!', 'PAH DOH-jee', 'Then come!'),
])
P['ono'] = dict(ctx0='Me, searching for a word', add=[
  X('About her', 'Ona je, ono, jako simpatična', 'OH-nah yeh, OH-no, YAH-ko seem-pah-TEECH-nah', "She's, like, really nice"),
  X('To her', 'Ono, ne znam kako da ti kažem', 'OH-no, neh ZNAHM KAH-ko dah tee KAH-zhem', "Like, I don't know how to tell you"),
  X('About a thing', 'To je, ono, malo čudno', 'TOH yeh, OH-no, MAH-lo CHOOD-no', "That's, like, a bit weird"),
])
P['sumnjam'] = dict(ctx0='About him', add=[
  X('About her', 'Sumnjam da će ona stići na vreme', 'SOOM-nyahm dah cheh OH-nah STEE-chee nah VREH-meh', 'I doubt she will arrive on time'),
  X('To her', 'Sumnjam da si to mislila ozbiljno', 'SOOM-nyahm dah see toh MEE-slee-lah OHZ-beel-no', 'I doubt you meant that seriously (to her)'),
  X('To him', 'Sumnjam da si to mislio ozbiljno', 'SOOM-nyahm dah see toh MEE-slee-oh OHZ-beel-no', 'I doubt you meant that seriously (to a man)'),
  X('About a thing', 'Sumnjam da je to istina', 'SOOM-nyahm dah yeh toh EES-tee-nah', 'I doubt that is true'),
])
P['ne-bih-rekao'] = dict(ctx0='Opinion (man)', fx=[
  ('Ne bih rekao da je to lepo', 'neh bih REH-kah-oh dah yeh toh LEH-po', "I wouldn't say that's nice"),
  ('Ne bih rekla da je to istina', 'neh bih REK-lah dah yeh toh EES-tee-nah', "I wouldn't say that's true"),
], add=[
  X('To her, disagreeing gently', 'Ne bih rekao da si u pravu', 'neh bih REH-kah-oh dah see oo PRAH-voo', "I wouldn't say you're right (a man says this)"),
  X('Her, disagreeing', 'Ne bih rekla da si u pravu', 'neh bih REK-lah dah see oo PRAH-voo', "I wouldn't say you're right (a woman says this)"),
  X('About someone else', 'Ne bih rekao da je on loš', 'neh bih REH-kah-oh dah yeh ohn LOHSH', "I wouldn't say he's bad (a man says this)"),
])
P['nema-veze'] = dict(ctx0='Letting something go', add=[
  X('Replying to her sorry', 'Nema veze, ne brini', 'NEH-mah VEH-zeh, neh BREE-nee', "Never mind, don't worry"),
  X('To her, about her lateness', 'Nema veze što kasniš', 'NEH-mah VEH-zeh shtoh KAHS-neesh', "It doesn't matter that you're late"),
  X('About a thing', 'To nema veze sa tim', 'TOH NEH-mah VEH-zeh sah TEEM', "That has nothing to do with it"),
  X('Taking charge', 'Nema veze, ja ću', 'NEH-mah VEH-zeh, yah choo', "Never mind, I'll do it"),
])
P['vazi'] = dict(ctx0='Agreeing to a time', add=[
  X('To her', 'Važi, javi se kad stigneš', 'VAH-zhee, YAH-vee seh kahd STEEG-nesh', 'OK, let me know when you get there'),
  X('Me, volunteering', 'Važi, ja ću doneti vino', 'VAH-zhee, yah choo DOH-neh-tee VEE-no', "OK, I'll bring the wine"),
  X('Meaning "it applies"', 'To važi i za tebe', 'TOH VAH-zhee ee zah TEH-beh', 'That goes for you too'),
  X('About a thing', 'Karta važi do petka', 'KAHR-tah VAH-zhee doh PET-kah', 'The ticket is valid until Friday'),
])
P['mozda'] = dict(ctx0='Noncommittal', add=[
  X('About me', 'Možda dođem kasnije', 'MOHZH-dah DOH-jem KAHS-nee-yeh', 'Maybe I will come later'),
  X('To her', 'Možda si u pravu', 'MOHZH-dah see oo PRAH-voo', "Maybe you're right"),
  X('About someone else', 'Možda je on bolestan', 'MOHZH-dah yeh ohn BOH-leh-stahn', 'Maybe he is sick'),
  X('About a plan', 'Možda sutra', 'MOHZH-dah SOO-trah', 'Maybe tomorrow'),
])
P['naravno'] = dict(ctx0='Me', add=[
  X('To her', 'Naravno da možeš', 'nah-RAHV-no dah MOH-zhesh', 'Of course you can'),
  X('About someone else', 'Naravno da je ona došla', 'nah-RAHV-no dah yeh OH-nah DOH-shlah', 'Of course she came'),
  X('About a thing', 'Naravno da je skupo', 'nah-RAHV-no dah yeh SKOO-po', "Of course it's expensive"),
  X('Warm yes', 'Naravno, rado', 'nah-RAHV-no, RAH-do', 'Of course, gladly'),
])
P['sta'] = dict(ctx0='To her', add=[
  X('About a thing', 'Šta je ovo?', 'SHTAH yeh OH-vo', 'What is this?'),
  X('To her, "what did you say"', 'Šta si rekla?', 'SHTAH see REK-lah', 'What did you say? (to her)'),
  X('To him, "what did you say"', 'Šta si rekao?', 'SHTAH see REH-kah-oh', 'What did you say? (to a man)'),
  X('About someone else', 'Šta je on rekao?', 'SHTAH yeh ohn REH-kah-oh', 'What did he say?'),
])
P['ko'] = dict(ctx0='About a thing', add=[
  X('About her', 'Ko je ona?', 'KOH yeh OH-nah', 'Who is she?'),
  X('About him', 'Ko je on?', 'KOH yeh OHN', 'Who is he?'),
  X('To her', 'Ko si ti?', 'KOH see TEE', 'Who are you?'),
  X('About a group', 'Ko dolazi sve?', 'KOH DOH-lah-zee SVEH', "Who's coming?"),
])
P['gde'] = dict(ctx0='About a place', fx=[
  ('Gde si sada?', 'GDEH see SAH-dah', 'Where are you now?'),
  ('Gdje si sada?', 'GDYEH see SAH-dah', 'Where are you now? (ijekavian)'),
], add=[
  X('About her', 'Gde je ona?', 'GDEH yeh OH-nah', 'Where is she?'),
  X('About him', 'Gde je on?', 'GDEH yeh OHN', 'Where is he?'),
  X('About a thing', 'Gde je moj telefon?', 'GDEH yeh MOY TEH-leh-fon', 'Where is my phone?'),
  X('About us', 'Gde idemo?', 'GDEH EE-deh-mo', 'Where are we going?'),
])
P['kad'] = dict(ctx0='About us', add=[
  X('To her', 'Kad stižeš?', 'KAHD STEE-zhesh', 'When are you arriving?'),
  X('About someone else', 'Kad on dolazi?', 'KAHD ohn DOH-lah-zee', 'When is he coming?'),
  X('About me', 'Kad treba da dođem?', 'KAHD TREH-bah dah DOH-jem', 'When should I come?'),
  X('About a thing', 'Kad počinje film?', 'KAHD POH-chee-nyeh FEELM', 'When does the movie start?'),
])
P['zasto'] = dict(ctx0='Short challenge', add=[
  X('To her', 'Zašto si tužna?', 'ZAHSH-toh see TOOZH-nah', 'Why are you sad? (to her)'),
  X('To him', 'Zašto si tužan?', 'ZAHSH-toh see TOO-zhahn', 'Why are you sad? (to a man)'),
  X('About someone else', 'Zašto je on otišao?', 'ZAHSH-toh yeh ohn OH-tee-shah-oh', 'Why did he leave?'),
  X('About a thing', 'Zašto je zatvoreno?', 'ZAHSH-toh yeh zaht-VOH-reh-no', 'Why is it closed?'),
])
P['kako'] = dict(ctx0='Asking how to say it', add=[
  X('To her', 'Kako se zoveš?', 'KAH-ko seh ZOH-vesh', "What's your name?"),
  X('About someone else', 'Kako se zove on?', 'KAH-ko seh ZOH-veh ohn', "What's his name?"),
  X('About a thing', 'Kako je bilo?', 'KAH-ko yeh BEE-lo', 'How was it?'),
  X('Meaning "pardon?"', 'Kako? Nisam čuo', 'KAH-ko? NEE-sahm CHOO-oh', "Pardon? I didn't hear (a man says this)"),
])
P['koji'] = dict(ctx0='Feminine noun', fx=[
  ('Koji film hoćeš da gledamo?', 'KOH-yee FEELM HOH-chesh dah GLEH-dah-mo', 'Which movie do you want to watch?'),
  ('Koja pesma je ovo?', 'KOH-yah PEH-smah yeh OH-vo', 'Which song is this?'),
  ('Koje vino hoćeš?', 'KOH-yeh VEE-no HOH-chesh', 'Which wine do you want?'),
], add=[
  X('About her', 'Koja je tvoja sestra?', 'KOH-yah yeh TVOH-yah SEH-strah', 'Which one is your sister?'),
  X('About him', 'Koji je tvoj brat?', 'KOH-yee yeh TVOY BRAHT', 'Which one is your brother?'),
  X('About a thing', 'Koje je tvoje omiljeno jelo?', 'KOH-yeh yeh TVOH-yeh oh-MEE-lyeh-no YEH-lo', 'What is your favorite dish?'),
])
P['sta-radis'] = dict(ctx0='To her', fx=[
  ('Šta radiš sutra?', 'SHTAH RAH-deesh SOO-trah', 'What are you doing tomorrow?'),
  ('Šta radite u slobodno vreme?', 'SHTAH RAH-dee-teh oo SLOH-bod-no VREH-meh', 'What do you do in your free time?'),
], forms_add=[
  F('Šta radim?', 'SHTAH RAH-deem', 'Me: "what am I doing?"', ('Šta radim? Radim, a ti?', 'SHTAH RAH-deem? RAH-deem, ah TEE', "What am I doing? Working, and you?"), describes='me'),
  F('Šta radi?', 'SHTAH RAH-dee', 'Someone else (he / she)', ('Šta radi tvoja sestra?', 'SHTAH RAH-dee TVOH-yah SEH-strah', 'What does your sister do?'), describes='him / her'),
  F('Šta radimo?', 'SHTAH RAH-dee-mo', 'Us', ('Šta radimo večeras?', 'SHTAH RAH-dee-mo VEH-cheh-rahs', 'What are we doing tonight?'), describes='us'),
  F('Šta rade?', 'SHTAH RAH-deh', 'They', ('Šta rade tvoji roditelji?', 'SHTAH RAH-deh TVOH-yee roh-DEE-teh-lyee', 'What do your parents do?'), describes='them'),
], changesBy=['formal', 'describes'], add=[
  X('About someone else', 'Šta radi on?', 'SHTAH RAH-dee OHN', 'What is he doing?'),
  X('About me', 'Radim, a ti?', 'RAH-deem, ah TEE', 'Working, and you?'),
])
P['gde-si'] = dict(ctx0='To her', fx=[
  ('Gde si ti? Ja sam ispred', 'GDEH see TEE? yah sahm EES-pred', "Where are you? I'm outside"),
  ('Gde ste sada?', 'GDEH steh SAH-dah', 'Where are you now?'),
], forms_add=[
  F('Gde sam ja?', 'GDEH sahm YAH', 'Me: "where am I?"', ('Izgubio sam se, gde sam ja?', 'eez-GOO-bee-oh sahm seh, GDEH sahm YAH', "I'm lost, where am I? (a man says this)"), describes='me'),
  F('Gde je on / ona?', 'GDEH yeh ohn / OH-nah', 'Someone else (he / she)', ('Gde je ona? Nisam je videla', 'GDEH yeh OH-nah? NEE-sahm yeh VEE-deh-lah', "Where is she? I haven't seen her (a woman says this)"), describes='him / her'),
  F('Gde smo?', 'GDEH smoh', 'Us', ('Gde smo? Izgubili smo se', 'GDEH smoh? eez-GOO-bee-lee smoh seh', "Where are we? We're lost"), describes='us'),
], changesBy=['formal', 'describes'], add=[
  X('Her, lost', 'Izgubila sam se, gde sam?', 'eez-GOO-bee-lah sahm seh, GDEH sahm', "I'm lost, where am I? (a woman says this)"),
  X('About someone else', 'Gde je on? Čekam ga', 'GDEH yeh OHN? CHEH-kahm gah', 'Where is he? I am waiting for him'),
])
P['jesi-li-gladna'] = dict(ctx0='To her', fx=[
  ('Jesi li gladan, brate?', 'YEH-see lee GLAH-dahn, BRAH-teh', 'Are you hungry, man?'),
  ('Jesi li gladna? Hoćeš da jedemo?', 'YEH-see lee GLAHD-nah? HOH-chesh dah YEH-deh-mo', 'Are you hungry? Want to eat?'),
], forms_add=[
  F('Je li ona gladna?', 'YEH lee OH-nah GLAHD-nah', 'Asking about her (not there)', ('Je li ona gladna? Pitaj je', 'YEH lee OH-nah GLAHD-nah? PEE-tai yeh', 'Is she hungry? Ask her'), describes='her'),
  F('Je li on gladan?', 'YEH lee OHN GLAH-dahn', 'Asking about him (not there)', ('Je li on gladan? Ima sendvič', 'YEH lee OHN GLAH-dahn? EE-mah SEND-veech', "Is he hungry? There's a sandwich"), describes='him'),
  F('Jesmo li gladni?', 'YES-mo lee GLAHD-nee', 'Asking about us', ('Jesmo li gladni? Hajde da jedemo', 'YES-mo lee GLAHD-nee? HAY-deh dah YEH-deh-mo', "Are we hungry? Let's eat"), describes='us'),
], changesBy=['describes'], add=[
  X('To him', 'Jesi li gladan? Imam pizzu', 'YEH-see lee GLAH-dahn? EE-mahm PEE-tsoo', 'Are you hungry? I have pizza (to a man)'),
  X('About a thing', 'Je li ručak gotov?', 'YEH lee ROO-chahk GOH-tov', 'Is lunch ready?'),
])
P['odakle-si'] = dict(ctx0='Returning the question', fx=[
  ('Odakle si, iz Beograda?', 'OH-dahk-leh see, eez beh-oh-GRAH-dah', 'Where are you from, Belgrade?'),
  ('Odakle ste vi?', 'OH-dahk-leh steh VEE', 'Where are you from?'),
], forms_add=[
  F('Odakle je on / ona?', 'OH-dahk-leh yeh ohn / OH-nah', 'Someone else (he / she)', ('Odakle je tvoja mama?', 'OH-dahk-leh yeh TVOH-yah MAH-mah', 'Where is your mom from?'), describes='him / her'),
], changesBy=['formal', 'describes'], add=[
  X('Me, answering (man)', 'Ja sam Kanađanin', 'yah sahm kah-NAH-jah-neen', "I'm Canadian (a man says this)"),
  X('Her, answering', 'Ja sam iz Novog Sada', 'yah sahm eez NOH-vog SAH-dah', "I'm from Novi Sad"),
  X('About someone else', 'Ona je Kanađanka', 'OH-nah yeh kah-NAH-jahn-kah', 'She is Canadian'),
])
P['koliko'] = dict(ctx0='About time', add=[
  X('About a thing', 'Koliko košta?', 'KOH-lee-ko KOH-shtah', 'How much does it cost?'),
  X('To her', 'Koliko ti je godina?', 'KOH-lee-ko tee yeh GOH-dee-nah', 'How old are you?'),
  X('About someone else', 'Koliko godina ima on?', 'KOH-lee-ko GOH-dee-nah EE-mah ohn', 'How old is he?'),
  X('About people', 'Koliko ljudi dolazi?', 'KOH-lee-ko LYOO-dee DOH-lah-zee', 'How many people are coming?'),
])
P['da-ne'] = dict(ctx0=['Saying yes', 'Saying no'], add=[
  X('About her', 'Da, ona dolazi', 'DAH, OH-nah DOH-lah-zee', 'Yes, she is coming'),
  X('About him', 'Ne, on nije ovde', 'NEH, ohn NEE-yeh OHV-deh', "No, he isn't here"),
])
P['jesam'] = dict(ctx0='Me, answering', fx=[
  ('Jesi li ti Met? Jesam', 'YEH-see lee tee MET? YEH-sahm', 'Are you Matt? I am'),
  ('Jesam li lud? Jesi!', 'YEH-sahm lee LOOD? YEH-see', 'Am I crazy? You are!'),
  ('Je li ona kod kuće? Jeste', 'YEH lee OH-nah kod KOO-cheh? YEH-steh', 'Is she at home? She is'),
  ('Jesmo li gotovi? Jesmo', 'YES-mo lee GOH-toh-vee? YES-mo', 'Are we done? We are'),
  ('Jesu li stigli? Jesu', 'YEH-soo lee STEEG-lee? YEH-soo', 'Have they arrived? They have'),
], add=[
  X('Her, answering', 'Jesi li umorna? Jesam', 'YEH-see lee OO-mor-nah? YEH-sahm', 'Are you tired? I am (a woman says this)'),
  X('About a thing', 'Je li skupo? Jeste', 'YEH lee SKOO-po? YEH-steh', 'Is it expensive? It is'),
])
P['zavisi'] = dict(ctx0='Me', add=[
  X('To her', 'Zavisi od tebe', 'zah-VEE-see od TEH-beh', 'It depends on you'),
  X('About someone else', 'Zavisi ko pita', 'zah-VEE-see KOH PEE-tah', 'Depends who is asking'),
  X('About a thing', 'Zavisi od vremena', 'zah-VEE-see od VREH-meh-nah', 'It depends on the weather'),
  X('About timing', 'Zavisi kad stigneš', 'zah-VEE-see kahd STEEG-nesh', 'It depends when you arrive'),
])
