P = {}
P['drago-mi-je'] = dict(ctx0='Introducing myself', forms=[
  F('Drago mi je', 'DRAH-go mee yeh', 'Me: "nice to meet you" (man or woman)', ('Drago mi je, ja sam Met', 'DRAH-go mee yeh, yah sahm MET', "Nice to meet you, I'm Matt"), describes='me'),
  F('Drago mi je i meni', 'DRAH-go mee yeh ee MEH-nee', 'Replying: "nice to meet you too"', ('Drago mi je i meni, Ana', 'DRAH-go mee yeh ee MEH-nee, AH-nah', 'Nice to meet you too, Ana'), describes='me'),
  F('Drago nam je', 'DRAH-go nahm yeh', 'We: "we\'re glad to meet you"', ('Drago nam je što ste došli', 'DRAH-go nahm yeh shtoh steh DOH-shlee', "We're glad you came"), describes='us'),
  F('Drago joj je / drago mu je', 'DRAH-go yoy yeh / DRAH-go moo yeh', 'About someone else (she / he is glad)', ('Mami je drago što te upoznaje', 'MAH-mee yeh DRAH-go shtoh teh oo-POHZ-nah-yeh', "Mom is glad to meet you"), describes='him / her'),
], changesBy=['describes'], add=[
  X('To her mom (polite)', 'Drago mi je, gospođo', 'DRAH-go mee yeh, GOH-spoh-jo', 'Nice to meet you, ma’am'),
  X('To her dad (polite)', 'Drago mi je, gospodine', 'DRAH-go mee yeh, GOH-spoh-dee-neh', 'Nice to meet you, sir'),
])
P['dobro-vece'] = dict(ctx0='To her parents', add=[
  X('To her mom (polite)', 'Dobro veče, gospođo', 'DOH-bro VEH-cheh, GOH-spoh-jo', 'Good evening, ma’am'),
  X('To her', 'Dobro veče, lepotice', 'DOH-bro VEH-cheh, leh-poh-TEE-tseh', 'Good evening, beautiful'),
  X('To a group', 'Dobro veče svima', 'DOH-bro VEH-cheh SVEE-mah', 'Good evening, everyone'),
])
P['izvolite'] = dict(ctx0='Inviting to sit', fx=[
  ('Izvoli, tvoja kafa', 'EEZ-vo-lee, TVOH-yah KAH-fah', "Here you go, your coffee (to her)"),
  ('Izvolite svi, večera je gotova', 'EEZ-vo-lee-teh SVEE, VEH-cheh-rah yeh GOH-toh-vah', 'Everyone, please, dinner is ready'),
], add=[
  X('Answering the door', 'Izvolite, uđite', 'EEZ-vo-lee-teh, OO-jee-teh', 'Please, come in (polite)'),
  X('In a shop (polite)', 'Izvolite? Kako mogu da pomognem?', 'EEZ-vo-lee-teh? KAH-ko MOH-goo dah poh-MOHG-nem', 'Yes, please? How can I help?'),
])
P['prijatno'] = dict(ctx0='To a group', add=[
  X('To her', 'Prijatno, lepotice', 'PREE-yaht-no, leh-poh-TEE-tseh', 'Enjoy, beautiful'),
  X('Reply, casual', 'Hvala, i tebi', 'HVAH-lah, ee TEH-bee', 'Thanks, you too'),
  X('Reply, polite', 'Hvala, i vama', 'HVAH-lah, ee VAH-mah', 'Thanks, you too (polite)'),
])
P['jos-malo'] = dict(ctx0='Me, asking', add=[
  X('To her mom (polite)', 'Još malo, hvala, odlično je', 'YOHSH MAH-lo, HVAH-lah, od-LEECH-no yeh', "A little more, thanks, it's excellent"),
  X('Offering to her', 'Još malo?', 'YOHSH MAH-lo', 'A little more?'),
  X('Declining', 'Ne više, hvala, sit sam', 'neh VEE-sheh, HVAH-lah, SEET sahm', "No more, thanks, I'm full (a man says this)"),
])
P['ne-treba'] = dict(ctx0='Me, declining', add=[
  X('To her mom (polite)', 'Ne treba, hvala, stvarno', 'neh TREH-bah, HVAH-lah, STVAHR-no', "No need, thanks, really"),
  X('To her', 'Ne treba, ja ću', 'neh TREH-bah, yah choo', "No need, I'll do it"),
  X('About someone else', 'Njemu ne treba, hvala', 'NYEH-moo neh TREH-bah, HVAH-lah', "He doesn't need any, thanks"),
  X('Declining a drink', 'Ne treba, hvala, vozim', 'neh TREH-bah, HVAH-lah, VOH-zeem', "No need, thanks, I'm driving"),
])
P['sve-je-bilo-ukusno'] = dict(ctx0='To her mom', add=[
  X('To her', 'Sve je bilo ukusno, ti si odlična kuvarica', 'SVEH yeh BEE-lo OO-koos-no, tee see od-LEECH-nah koo-VAH-ree-tsah', "Everything was delicious, you're a great cook"),
  X('About a dish (fem.)', 'Pita je bila ukusna', 'PEE-tah yeh BEE-lah OO-koos-nah', 'The pie was delicious'),
  X('About a dish (masc.)', 'Hleb je bio ukusan', 'HLEHB yeh BEE-oh OO-koo-sahn', 'The bread was delicious'),
  X('About a dish (neuter)', 'Meso je bilo ukusno', 'MEH-so yeh BEE-lo OO-koos-no', 'The meat was delicious'),
])
P['odlicno-kuvate'] = dict(ctx0='To her mom (polite)', fx=[
  ('Odlično kuvaš, ljubavi', 'od-LEECH-no KOO-vahsh, LYOO-bah-vee', 'You cook great, my love (to her)'),
  ('Odlično kuvate, gospođo', 'od-LEECH-no KOO-vah-teh, GOH-spoh-jo', 'You cook great, ma’am'),
], forms_add=[
  F('Odlično kuva', 'od-LEECH-no KOO-vah', 'About someone else (he / she)', ('Njena mama odlično kuva', 'NYEH-nah MAH-mah od-LEECH-no KOO-vah', 'Her mom cooks great'), describes='him / her'),
  F('Ne kuvam baš dobro', 'neh KOO-vahm BAHSH DOH-bro', 'Me, being modest', ('Ne kuvam baš dobro', 'neh KOO-vahm BAHSH DOH-bro', "I don't cook very well"), describes='me'),
], changesBy=['formal', 'describes'], add=[
  X('About her mom', 'Tvoja mama odlično kuva', 'TVOH-yah MAH-mah od-LEECH-no KOO-vah', 'Your mom cooks great'),
  X('About her dad', 'Tvoj tata odlično kuva', 'TVOY TAH-tah od-LEECH-no KOO-vah', 'Your dad cooks great'),
])
P['zivili'] = dict(ctx0='To the table', add=[
  X('To her', 'Za tebe, živeli!', 'zah TEH-beh, ZHEE-veh-lee', 'To you, cheers!'),
  X('To the host (polite)', 'Živeli, hvala na gostoprimstvu', 'ZHEE-veh-lee, HVAH-lah nah goh-stoh-PREEM-stvoo', 'Cheers, thanks for the hospitality'),
  X('To a group', 'Živeli svima!', 'ZHEE-veh-lee SVEE-mah', 'Cheers, everyone!'),
])
P['ucim-srpski'] = dict(ctx0='To her', forms=[
  F('Učim srpski', 'OO-cheem SUHR-pskee', 'Me (man or woman)', ('Učim srpski svaki dan', 'OO-cheem SUHR-pskee SVAH-kee DAHN', "I'm learning Serbian every day"), describes='me'),
  F('Učiš li srpski?', 'OO-cheesh lee SUHR-pskee', 'Asking her: "are you learning?"', ('Učiš li engleski?', 'OO-cheesh lee EN-gleh-skee', 'Are you learning English?'), describes='her', formal='casual'),
  F('Uči srpski', 'OO-chee SUHR-pskee', 'Someone else (he / she)', ('Moj brat takođe uči srpski', 'MOY braht tah-KOH-jeh OO-chee SUHR-pskee', 'My brother is learning Serbian too'), describes='him / her'),
  F('Učimo srpski', 'OO-chee-mo SUHR-pskee', 'We', ('Učimo srpski zajedno', 'OO-chee-mo SUHR-pskee ZAH-yeh-dno', "We're learning Serbian together"), describes='us'),
], changesBy=['describes'], add=[
  X('To her mom (polite)', 'Učim srpski, ali je teško', 'OO-cheem SUHR-pskee, AH-lee yeh TEHSH-ko', "I'm learning Serbian, but it's hard"),
  X('Her, to me', 'Učiš srpski? Bravo!', 'OO-cheesh SUHR-pskee? BRAH-vo', "You're learning Serbian? Bravo! (what she might say)"),
])
P['govorim-malo'] = dict(ctx0='Me', forms=[
  F('Govorim malo srpski', 'GOH-vo-reem MAH-lo SUHR-pskee', 'Me (man or woman)', ('Govorim malo srpski i engleski', 'GOH-vo-reem MAH-lo SUHR-pskee ee EN-gleh-skee', 'I speak a little Serbian and English'), describes='me'),
  F('Govoriš li engleski?', 'GOH-vo-reesh lee EN-gleh-skee', 'Asking her: "do you speak English?"', ('Govoriš li engleski?', 'GOH-vo-reesh lee EN-gleh-skee', 'Do you speak English?'), describes='her', formal='casual'),
  F('Govori', 'GOH-vo-ree', 'Someone else (he / she)', ('Ona govori tri jezika', 'OH-nah GOH-vo-ree TREE YEH-zee-kah', 'She speaks three languages'), describes='him / her'),
  F('Govorimo', 'GOH-vo-ree-mo', 'We', ('Govorimo srpski i engleski', 'GOH-vo-ree-mo SUHR-pskee ee EN-gleh-skee', 'We speak Serbian and English'), describes='us'),
  F('Govorite li engleski?', 'GOH-vo-ree-teh lee EN-gleh-skee', 'Polite, to her parents', ('Govorite li engleski, gospođo?', 'GOH-vo-ree-teh lee EN-gleh-skee, GOH-spoh-jo', 'Do you speak English, ma’am?'), formal='polite'),
], changesBy=['describes', 'formal'], add=[
  X('To her', 'Govoriš li polako, molim te?', 'GOH-vo-reesh lee poh-LAH-ko, MOH-leem teh', 'Can you speak slowly, please?'),
  X('About someone else', 'Njen tata govori malo engleski', 'NYEHN TAH-tah GOH-vo-ree MAH-lo EN-gleh-skee', 'Her dad speaks a little English'),
])
P['pozdravi-roditelje'] = dict(ctx0='To her', fx=[
  ('Pozdravi sestru i brata', 'pohz-DRAH-vee SEH-stroo ee BRAH-tah', 'Say hi to your sister and brother'),
  ('Pozdravite porodicu', 'pohz-DRAH-vee-teh poh-roh-DEE-tsoo', 'Say hi to your family (polite)'),
], add=[
  X('Me, sending a greeting', 'Pozdravljam te', 'pohz-DRAHV-lyahm teh', 'I send you my greetings'),
  X('From someone else', 'Moja mama te pozdravlja', 'MOH-yah MAH-mah teh pohz-DRAHV-lyah', 'My mom says hi to you'),
  X('Her, to me', 'Pozdravi i ti svoje', 'pohz-DRAH-vee ee tee SVOH-yeh', 'Say hi to yours too (what she might say)'),
])
P['srecan-praznik'] = dict(ctx0='New Year', fx=[
  ('Srećan Božić, Hristos se rodi!', 'SREH-chahn BOH-zheech, HREE-stohs seh ROH-dee', 'Merry Christmas, Christ is born!'),
  ('Srećna Nova godina, ljubavi', 'SRETCH-nah NOH-vah GOH-dee-nah, LYOO-bah-vee', 'Happy New Year, my love'),
  ('Srećan Uskrs, sve najbolje', 'SREH-chahn OO-skrs, SVEH NAI-bohl-yeh', 'Happy Easter, all the best'),
], forms_add=[
  F('Srećni praznici', 'SRETCH-nee PRAHZ-nee-tsee', 'Happy holidays (any, plural)', ('Srećni praznici svima!', 'SRETCH-nee PRAHZ-nee-tsee SVEE-mah', 'Happy holidays to all!'), nounGender='plural'),
], add=[
  X('To her family (polite)', 'Srećan Božić vama i porodici', 'SREH-chahn BOH-zheech VAH-mah ee poh-roh-DEE-tsee', 'Merry Christmas to you and your family'),
  X('To him', 'Srećan Božić, brate', 'SREH-chahn BOH-zheech, BRAH-teh', 'Merry Christmas, man'),
])
P['bozic'] = dict(ctx0='The greeting', add=[
  X('The reply', 'Vaistinu se rodi!', 'VAH-ee-stee-noo seh ROH-dee', 'Truly He is born!'),
  X('To her', 'Kako slavite Božić?', 'KAH-ko SLAH-vee-teh BOH-zheech', 'How do you celebrate Christmas?'),
  X('About a thing', 'Badnje veče je šestog januara', 'BAHD-nyeh VEH-cheh yeh SHEH-stog YAH-noo-ah-rah', 'Christmas Eve is on January 6'),
])
P['uskrs'] = dict(ctx0='The greeting', add=[
  X('The reply', 'Vaistinu vaskrse!', 'VAH-ee-stee-noo VAH-skrseh', 'Truly He is risen!'),
  X('To her', 'Hoćeš li da tucamo jaja?', 'HOH-chesh lee dah TOO-tsah-mo YAH-yah', 'Want to crack eggs with me?'),
  X('About a thing', 'Jaja su crvena', 'YAH-yah soo TSUR-veh-nah', 'The eggs are red'),
])
P['rakija'] = dict(ctx0='Being offered', fx=[('Ovo je domaća rakija', 'OH-vo yeh DOH-mah-chah RAH-kee-yah', 'This is homemade rakija')], forms_add=[
  F('rakiju', 'RAH-kee-yoo', 'When it is the thing you take or want', ('Hvala, uzeću rakiju', 'HVAH-lah, OO-zeh-choo RAH-kee-yoo', "Thanks, I'll have a rakija"), nounGender='feminine (object)'),
  F('rakije', 'RAH-kee-yeh', '"A bit of rakija" / "of rakija"', ('Malo rakije, hvala', 'MAH-lo RAH-kee-yeh, HVAH-lah', 'A little rakija, thanks'), nounGender='feminine (of)'),
], add=[
  X('About her grandpa', 'Njen deda pravi rakiju', 'NYEHN DEH-dah PRAH-vee RAH-kee-yoo', 'Her grandpa makes rakija'),
  X('About a thing', 'Rakija je jaka', 'RAH-kee-yah yeh YAH-kah', 'The rakija is strong'),
])
P['gost-u-kuci'] = dict(ctx0='The saying', add=[
  X('Her family, to me', 'Ti si naš gost', 'tee see NAHSH GOHST', "You're our guest (what her family might say)"),
  X('Me, thanking them', 'Hvala što ste me ugostili', 'HVAH-lah shtoh steh meh oo-GOH-stee-lee', 'Thanks for hosting me (polite)'),
  X('About someone else', 'On je naš gost', 'OHN yeh NAHSH GOHST', 'He is our guest'),
  X('A general truth', 'Gost je uvek dobrodošao', 'GOHST yeh OO-vek doh-broh-DOH-shah-oh', 'A guest is always welcome'),
])
P['polako'] = dict(ctx0='Take it easy', add=[
  X('To her, speaking too fast', 'Polako, molim te', 'poh-LAH-ko, MOH-leem teh', 'Slowly, please'),
  X('To him', 'Polako, brate, ne žuri', 'poh-LAH-ko, BRAH-teh, neh ZHOO-ree', "Easy, man, don't rush"),
  X('About me', 'Idem polako', 'EE-dem poh-LAH-ko', "I'm going slowly"),
  X('About someone else', 'Ona vozi polako', 'OH-nah VOH-zee poh-LAH-ko', 'She drives slowly'),
])
P['inat'] = dict(ctx0='About someone', add=[
  X('To her, teasing', 'Ti si baš inatljiva', 'tee see BAHSH EE-naht-lyee-vah', "You're so stubborn (to her)"),
  X('To him', 'Inatljiv si, brate', 'EE-naht-lyeev see, BRAH-teh', "You're stubborn, man"),
  X('Me (man)', 'Uradio sam to iz inata', 'OO-rah-dee-oh sahm toh eez EE-nah-tah', 'I did it out of stubbornness'),
  X('Her, about herself', 'Uradila sam to iz inata', 'OO-rah-dee-lah sahm toh eez EE-nah-tah', 'I did it out of stubbornness (a woman says this)'),
])
P['politika'] = dict(add=[
  X('Suggesting', 'Ne pričajmo o politici', 'neh PREE-chai-mo oh POH-lee-tee-tsee', "Let's not talk about politics"),
  X('To her', 'Hoćemo li o nečem drugom?', 'HOH-cheh-mo lee oh NEH-chem DROO-gom', 'Shall we talk about something else?'),
  X('Her, to me', 'Ne pričaj o politici pred mojim tatom', 'neh PREE-chai oh POH-lee-tee-tsee pred MOH-yeem TAH-tom', "Don't talk politics in front of my dad (what she might say)"),
  X('About someone else', 'On stalno priča o politici', 'OHN STAHL-no PREE-chah oh POH-lee-tee-tsee', 'He is always talking politics'),
])
P['srpski-jezik'] = dict(ctx0='Me', add=[
  X('To her', 'Govoriš li srpski ili engleski?', 'GOH-vo-reesh lee SUHR-pskee EE-lee EN-gleh-skee', 'Do you speak Serbian or English?'),
  X('About someone else', 'Ona govori srpski i engleski', 'OH-nah GOH-vo-ree SUHR-pskee ee EN-gleh-skee', 'She speaks Serbian and English'),
  X('About the language', 'Srpski je težak, ali lep', 'SUHR-pskee yeh TEH-zhahk, AH-lee LEHP', 'Serbian is hard, but beautiful'),
])
