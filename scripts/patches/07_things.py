P = {}
def noun(ex0ctx, fx, forms_add, adds):
    return dict(ctx0=ex0ctx, fx=[fx], forms_add=forms_add, add=adds)
P['kafa'] = noun('Ordering', ('Ovo je dobra kafa', 'OH-vo yeh DOH-brah KAH-fah', 'This is good coffee'), [
  F('kafu', 'KAH-foo', 'When it is the thing you order or want', ('Hoću kafu', 'HOH-choo KAH-foo', 'I want a coffee'), nounGender='feminine (object)'),
  F('kafe', 'KAH-feh', 'Two to four, or "of coffee"', ('Dve kafe, molim', 'DVEH KAH-feh, MOH-leem', 'Two coffees, please'), nounGender='feminine (plural)'),
], [X('To her', 'Hoćeš li kafu?', 'HOH-chesh lee KAH-foo', 'Do you want a coffee?'),
    X('About someone else', 'Ona pije kafu bez šećera', 'OH-nah PEE-yeh KAH-foo bez SHEH-cheh-rah', 'She drinks coffee without sugar'),
    X('About a thing', 'Kafa je hladna', 'KAH-fah yeh HLAHD-nah', 'The coffee is cold')])
P['pivo'] = noun('Ordering', ('Ovo je dobro pivo', 'OH-vo yeh DOH-bro PEE-vo', 'This is good beer'), [
  F('piva', 'PEE-vah', 'Two to four, or "of beer"', ('Dva piva, molim', 'DVAH PEE-vah, MOH-leem', 'Two beers, please'), nounGender='neuter (plural)'),
], [X('To her', 'Hoćeš li pivo?', 'HOH-chesh lee PEE-vo', 'Do you want a beer?'),
    X('About someone else', 'On pije samo pivo', 'OHN PEE-yeh SAH-mo PEE-vo', 'He only drinks beer'),
    X('About a thing', 'Pivo je hladno', 'PEE-vo yeh HLAHD-no', 'The beer is cold')])
P['vino'] = noun('Offering', ('Ovo je dobro vino', 'OH-vo yeh DOH-bro VEE-no', 'This is good wine'), [
  F('vina', 'VEE-nah', 'Two to four, or "of wine"', ('Dva vina, molim', 'DVAH VEE-nah, MOH-leem', 'Two glasses of wine, please'), nounGender='neuter (plural)'),
], [X('To her', 'Hoćeš li čašu vina?', 'HOH-chesh lee CHAH-shoo VEE-nah', 'Do you want a glass of wine?'),
    X('About someone else', 'Ona voli crno vino', 'OH-nah VOH-lee TSUR-no VEE-no', 'She likes red wine'),
    X('About a thing', 'Vino je odlično', 'VEE-no yeh od-LEECH-no', 'The wine is excellent')])
P['voda'] = noun('Ordering', ('Ovo je dobra voda', 'OH-vo yeh DOH-brah VOH-dah', 'This is good water'), [
  F('vodu', 'VOH-doo', 'When it is the thing you order or want', ('Hoću vodu', 'HOH-choo VOH-doo', 'I want water'), nounGender='feminine (object)'),
  F('vode', 'VOH-deh', '"Some water" / "of water"', ('Hoćeš li vode?', 'HOH-chesh lee VOH-deh', 'Do you want some water?'), nounGender='feminine (of)'),
], [X('To her', 'Hoćeš li vode?', 'HOH-chesh lee VOH-deh', 'Do you want some water?'),
    X('About someone else', 'On pije samo vodu', 'OHN PEE-yeh SAH-mo VOH-doo', 'He only drinks water'),
    X('About a thing', 'Voda je hladna', 'VOH-dah yeh HLAHD-nah', 'The water is cold')])
P['kafic'] = noun('Suggesting', ('Ovo je dobar kafić', 'OH-vo yeh DOH-bahr KAH-feech', 'This is a good café'), [
  F('u kafiću', 'oo KAH-fee-choo', 'In the café (where you are)', ('Ja sam u kafiću', 'yah sahm oo KAH-fee-choo', "I'm at the café"), nounGender='masculine (location)'),
], [X('To her', 'Hoćeš li u kafić?', 'HOH-chesh lee oo KAH-feech', 'Do you want to go to a café?'),
    X('About someone else', 'Ona radi u kafiću', 'OH-nah RAH-dee oo KAH-fee-choo', 'She works at a café'),
    X('About a thing', 'Kafić je pun', 'KAH-feech yeh POON', 'The café is full')])
P['racun'] = dict(fx=[
  ('Račun, molim te, kartica', 'RAH-choon, MOH-leem teh, KAHR-tee-tsah', 'The bill, please, by card (to a friend)'),
  ('Račun, molim vas', 'RAH-choon, MOH-leem vahs', 'The bill, please (polite)'),
], add=[
  X('Me, to her', 'Ja častim večeras', 'yah CHAH-steem VEH-cheh-rahs', "It's my treat tonight"),
  X('Her, to me', 'Ja plaćam, ti si platio prošli put', 'yah PLAH-chahm, tee see PLAH-tee-oh PROSH-lee POOT', "I'll pay, you paid last time (she says this)"),
  X('About us', 'Hoćemo li da podelimo račun?', 'HOH-cheh-mo lee dah poh-DEH-lee-mo RAH-choon', 'Shall we split the bill?'),
])
P['stan'] = noun('About me', ('Imam mali stan', 'EE-mahm MAH-lee STAHN', 'I have a small apartment'), [
  F('u stanu', 'oo STAH-noo', 'In the apartment (where you are)', ('Ja sam u stanu', 'yah sahm oo STAH-noo', "I'm in the apartment"), nounGender='masculine (location)'),
], [X('To her', 'Hoćeš li da vidiš moj stan?', 'HOH-chesh lee dah VEE-deesh MOY STAHN', 'Do you want to see my apartment?'),
    X('About her', 'Tvoj stan je lep', 'TVOY STAHN yeh LEHP', 'Your apartment is nice'),
    X('About someone else', 'Njihov stan je veliki', 'NYEE-hov STAHN yeh VEH-lee-kee', 'Their apartment is big')])
P['kod-mene'] = dict(ctx0='To her', forms=[
  F('kod mene', 'kod MEH-neh', 'At my place', ('Dođi kod mene', 'DOH-jee kod MEH-neh', 'Come to my place'), describes='me'),
  F('kod tebe', 'kod TEH-beh', 'At your place (her or his)', ('Ja ću doći kod tebe', 'yah choo DOH-chee kod TEH-beh', "I'll come to your place"), describes='her', formal='casual'),
  F('kod nje / kod njega', 'kod NYEH / kod NYEH-gah', 'At her / his place', ('Večeras smo kod nje. Sutra smo kod njega', 'VEH-cheh-rahs smoh kod NYEH. SOO-trah smoh kod NYEH-gah', "Tonight we're at her place. Tomorrow we're at his"), describes='him / her'),
  F('kod nas', 'kod NAHS', 'At our place', ('Dođite kod nas', 'DOH-jee-teh kod NAHS', 'Come to our place'), describes='us'),
  F('kod vas', 'kod VAHS', 'At your place (polite, or a group)', ('Možemo li kod vas?', 'MOH-zheh-mo lee kod VAHS', 'Can we come to your place?'), formal='polite'),
], changesBy=['describes', 'formal'], add=[
  X('Meaning "in my case"', 'Kod mene je to drugačije', 'kod MEH-neh yeh toh DROO-gah-chee-yeh', "In my case it's different"),
  X('About someone else', 'Ona je kod mame', 'OH-nah yeh kod MAH-meh', "She's at her mom's"),
])
P['aerodrom'] = noun('Me going', ('Aerodrom je daleko', 'ah-eh-ROH-drohm yeh DAH-leh-ko', 'The airport is far'), [
  F('na aerodromu', 'nah ah-eh-ROH-droh-moo', 'At the airport (where you are)', ('Sada sam na aerodromu', 'SAH-dah sahm nah ah-eh-ROH-droh-moo', "I'm at the airport now"), nounGender='masculine (location)'),
], [X('To her', 'Hoćeš da te odvezem na aerodrom?', 'HOH-chesh dah teh od-VEH-zem nah ah-eh-ROH-drohm', 'Do you want me to drive you to the airport?'),
    X('About someone else', 'Ona radi na aerodromu', 'OH-nah RAH-dee nah ah-eh-ROH-droh-moo', 'She works at the airport'),
    X('About a thing', 'Aerodrom je veliki', 'ah-eh-ROH-drohm yeh VEH-lee-kee', 'The airport is big')])
P['stanica'] = noun('Asking', ('Autobuska stanica je tamo', 'ow-toh-BOO-skah STAH-nee-tsah yeh TAH-mo', 'The bus station is over there'), [
  F('na stanici', 'nah STAH-nee-tsee', 'At the station (where you are)', ('Čekam te na stanici', 'CHEH-kahm teh nah STAH-nee-tsee', "I'm waiting for you at the station"), nounGender='feminine (location)'),
], [X('To her', 'Čekam te na stanici', 'CHEH-kahm teh nah STAH-nee-tsee', "I'm waiting for you at the station"),
    X('About someone else', 'On je na stanici', 'OHN yeh nah STAH-nee-tsee', 'He is at the station'),
    X('About a thing', 'Stanica je blizu', 'STAH-nee-tsah yeh BLEE-zoo', 'The station is close')])
fam = lambda: None
P['mama-tata'] = dict(ctx0='About my dad', fx=[
  ('Moja mama kuva odlično', 'MOH-yah MAH-mah KOO-vah od-LEECH-no', 'My mom cooks great'),
  ('Moj tata radi u banci', 'MOY TAH-tah RAH-dee oo BAHN-tsee', 'My dad works at a bank'),
], forms_add=[
  F('tvoja mama', 'TVOH-yah MAH-mah', 'Her mom (asking her)', ('Kako je tvoja mama?', 'KAH-ko yeh TVOH-yah MAH-mah', 'How is your mom?'), describes='her'),
  F('tvoj tata', 'TVOY TAH-tah', 'Her dad (asking her)', ('Kako je tvoj tata?', 'KAH-ko yeh TVOY TAH-tah', 'How is your dad?'), describes='her'),
  F('njena mama / njen tata', 'NYEH-nah MAH-mah / NYEHN TAH-tah', 'Her parents (talking about her to someone)', ('Njena mama je ljubazna. Njen tata je tih', 'NYEH-nah MAH-mah yeh LYOO-bahz-nah. NYEHN TAH-tah yeh TEEH', 'Her mom is kind. Her dad is quiet'), describes='her'),
], changesBy=['noun gender', 'describes'], add=[
  X('To her', 'Kako su tvoja mama i tata?', 'KAH-ko soo TVOH-yah MAH-mah ee TAH-tah', 'How are your mom and dad?'),
  X('Her, to me', 'Moja mama želi da te upozna', 'MOH-yah MAH-mah ZHEH-lee dah teh OO-pohz-nah', 'My mom wants to meet you (she says this)'),
])
P['brat-sestra'] = dict(ctx0='About me', fx=[
  ('Moj brat živi u Kanadi', 'MOY BRAHT ZHEE-vee oo KAH-nah-dee', 'My brother lives in Canada'),
  ('Moja sestra je mlađa od mene', 'MOH-yah SEH-strah yeh MLAH-jah od MEH-neh', 'My sister is younger than me'),
], forms_add=[
  F('tvoj brat / tvoja sestra', 'TVOY BRAHT / TVOH-yah SEH-strah', 'Her brother / sister (asking her)', ('Kako su tvoj brat i tvoja sestra?', 'KAH-ko soo TVOY BRAHT ee TVOH-yah SEH-strah', 'How are your brother and sister?'), describes='her'),
  F('njegov brat / njegova sestra', 'NYEH-gov BRAHT / NYEH-go-vah SEH-strah', 'His brother / sister', ('Njegova sestra je moja drugarica', 'NYEH-go-vah SEH-strah yeh MOH-yah droo-GAH-ree-tsah', 'His sister is my friend'), describes='him'),
], changesBy=['noun gender', 'describes'], add=[
  X('To her', 'Imaš li brata ili sestru?', 'EE-mahsh lee BRAH-tah EE-lee SEH-stroo', 'Do you have a brother or a sister?'),
  X('About someone else', 'Njen brat je stariji od nje', 'NYEHN BRAHT yeh STAH-ree-yee od NYEH', 'Her brother is older than her'),
])
P['baka-deda'] = dict(ctx0='About my grandma', fx=[
  ('Moja baka pravi pitu', 'MOH-yah BAH-kah PRAH-vee PEE-too', 'My grandma makes pie'),
  ('Moj deda priča priče', 'MOY DEH-dah PREE-chah PREE-cheh', 'My grandpa tells stories'),
], forms_add=[
  F('tvoja baka / tvoj deda', 'TVOH-yah BAH-kah / TVOY DEH-dah', 'Her grandparents (asking her)', ('Kako su tvoja baka i deda?', 'KAH-ko soo TVOH-yah BAH-kah ee DEH-dah', 'How are your grandma and grandpa?'), describes='her'),
  F('njegova baka / njen deda', 'NYEH-go-vah BAH-kah / NYEHN DEH-dah', 'His / her grandparents', ('Njena baka živi na selu', 'NYEH-nah BAH-kah ZHEE-vee nah SEH-loo', 'Her grandma lives in the village'), describes='him / her'),
], changesBy=['noun gender', 'describes'], add=[
  X('To her', 'Da li si bila kod bake?', 'dah lee see BEE-lah kod BAH-keh', 'Were you at your grandma’s?'),
  X('About a thing', 'Bakina pita je najbolja', 'BAH-kee-nah PEE-tah yeh NAI-bohl-yah', "Grandma's pie is the best"),
])
P['prijatelj'] = dict(ctx0='About a female friend', fx=[
  ('To je moj prijatelj, Marko', 'TOH yeh MOY PREE-yah-tel, MAHR-ko', "That's my friend, Marko"),
  ('Ona je moja prijateljica', 'OH-nah yeh MOH-yah pree-yah-teh-LYEE-tsah', 'She is my (female) friend'),
], forms_add=[
  F('prijatelji', 'PREE-yah-teh-lyee', 'Friends (a mixed group or all men)', ('Moji prijatelji dolaze večeras', 'MOH-yee PREE-yah-teh-lyee DOH-lah-zeh VEH-cheh-rahs', 'My friends are coming tonight'), describes='them'),
  F('prijateljice', 'pree-yah-teh-LYEE-tseh', 'Friends (all women)', ('Njene prijateljice su tu', 'NYEH-neh pree-yah-teh-LYEE-tseh soo TOO', 'Her friends are here'), describes='them (all women)'),
], changesBy=['describes'], add=[
  X('To her', 'Ti si moja najbolja prijateljica', 'tee see MOH-yah NAI-bohl-yah pree-yah-teh-LYEE-tsah', "You're my best friend (to her)"),
  X('To him', 'Ti si moj najbolji prijatelj', 'tee see MOY NAI-bohl-yee PREE-yah-tel', "You're my best friend (to a man)"),
])
P['danas-sutra-juce'] = dict(ctx0='About a plan', forms=[
  F('Danas', 'DAH-nahs', 'Today (the present)', ('Danas radim do šest', 'DAH-nahs RAH-deem doh SHEST', "Today I'm working until six")),
  F('Sutra', 'SOO-trah', 'Tomorrow (the future)', ('Sutra sam slobodan', 'SOO-trah sahm SLOH-bo-dahn', "Tomorrow I'm free (a man says this)")),
  F('Juče', 'YOO-cheh', 'Yesterday (the past)', ('Juče sam bila kod kuće', 'YOO-cheh sahm BEE-lah kod KOO-cheh', 'Yesterday I was at home (a woman says this)')),
], add=[
  X('To her', 'Šta si radila juče?', 'SHTAH see RAH-dee-lah YOO-cheh', 'What did you do yesterday?'),
  X('About someone else', 'Ona dolazi sutra', 'OH-nah DOH-lah-zee SOO-trah', 'She is coming tomorrow'),
  X('About a thing', 'Danas je hladno', 'DAH-nahs yeh HLAHD-no', "It's cold today"),
])
P['veceras'] = dict(ctx0='To her', add=[
  X('About me', 'Večeras ostajem kod kuće', 'VEH-cheh-rahs oh-STAH-yem kod KOO-cheh', "I'm staying home tonight"),
  X('To her, a compliment', 'Večeras izgledaš prelepo', 'VEH-cheh-rahs EEZ-gleh-dahsh preh-LEH-po', 'You look gorgeous tonight'),
  X('About someone else', 'Ona radi večeras', 'OH-nah RAH-dee VEH-cheh-rahs', 'She is working tonight'),
  X('About a thing', 'Večeras je hladno', 'VEH-cheh-rahs yeh HLAHD-no', "It's cold tonight"),
])
P['dani'] = dict(ctx0='Making a plan', add=[
  X('To her', 'Jesi li slobodna u utorak?', 'YEH-see lee SLOHB-od-nah oo OO-toh-rahk', 'Are you free on Tuesday?'),
  X('About me', 'U sredu radim', 'oo SREH-doo RAH-deem', 'I work on Wednesday'),
  X('About someone else', 'Ona ne radi u nedelju', 'OH-nah neh RAH-dee oo NEH-deh-lyoo', "She doesn't work on Sunday"),
])
P['vikend'] = dict(ctx0='To her', add=[
  X('About me', 'Za vikend idem kod roditelja', 'zah VEE-kend EE-dem kod roh-DEE-teh-lyah', "This weekend I'm going to my parents'"),
  X('About us', 'Vikend provodimo zajedno', 'VEE-kend proh-VOH-dee-mo ZAH-yeh-dno', "We're spending the weekend together"),
  X('About someone else', 'Ona radi vikendom', 'OH-nah RAH-dee VEE-keh-ndom', 'She works on weekends'),
])
P['svadba'] = noun('Me, to her', ('Svadba je sutra', 'SVAHD-bah yeh SOO-trah', 'The wedding is tomorrow'), [
  F('na svadbi', 'nah SVAHD-bee', 'At the wedding (where you are)', ('Bili smo na svadbi', 'BEE-lee smoh nah SVAHD-bee', 'We were at a wedding'), nounGender='feminine (location)'),
], [X('To her', 'Hoćeš li da ideš na svadbu sa mnom?', 'HOH-chesh lee dah EE-desh nah SVAHD-boo sah MNOHM', 'Do you want to go to the wedding with me?'),
    X('About her sister', 'Njena sestra se udaje', 'NYEH-nah SEH-strah seh OO-dah-yeh', 'Her sister is getting married (a woman marries: udaje se)'),
    X('About her brother', 'Njen brat se ženi', 'NYEHN BRAHT seh ZHEH-nee', 'Her brother is getting married (a man marries: ženi se)')])
P['slava'] = noun('Greeting', ('Slava je u decembru', 'SLAH-vah yeh oo deh-TSEM-broo', 'The slava is in December'), [
  F('na slavi', 'nah SLAH-vee', 'At the slava (where you are)', ('Bili smo na slavi kod njih', 'BEE-lee smoh nah SLAH-vee kod NYEEH', 'We were at their slava'), nounGender='feminine (location)'),
], [X('About me, going', 'Idem na slavu kod tvojih', 'EE-dem nah SLAH-voo kod TVOH-yeeh', "I'm going to your family's slava"),
    X('To her', 'Kad vam je slava?', 'KAHD vahm yeh SLAH-vah', 'When is your slava?'),
    X('About someone else', 'Njihova slava je u decembru', 'NYEE-ho-vah SLAH-vah yeh oo deh-TSEM-broo', 'Their slava is in December')])
P['srecan-rodjendan'] = dict(ctx0='To her', fx=[
  ('Srećan rođendan, brate!', 'SREH-chahn ROH-jen-dahn, BRAH-teh', 'Happy birthday, man!'),
  ('Srećna slava, domaćine!', 'SRETCH-nah SLAH-vah, doh-MAH-chee-neh', 'Happy slava, host!'),
], add=[
  X('To her mom (polite)', 'Srećan rođendan, gospođo!', 'SREH-chahn ROH-jen-dahn, GOH-spoh-jo', 'Happy birthday, ma’am!'),
  X('About her', 'Danas joj je rođendan', 'DAH-nahs yoy yeh ROH-jen-dahn', "It's her birthday today"),
  X('About me', 'Sutra mi je rođendan', 'SOO-trah mee yeh ROH-jen-dahn', "It's my birthday tomorrow"),
])
