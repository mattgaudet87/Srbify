P = {}
P['ti-vi'] = dict(ctx0=['To her (casual)', 'To an elder (polite)'], fx=[
  ('Ti si divna', 'tee see DEEV-nah', "You're wonderful (to her)"),
  ('Vi ste jako ljubazni', 'vee steh YAH-ko LYOO-bahz-nee', 'You are very kind (polite)'),
], forms_add=[
  F('Vi (more than one friend)', 'VEE', 'To a group of friends', ('Vi ste najbolji, momci', 'vee steh NAI-bohl-yee, MOHM-tsee', "You guys are the best"), formal='polite'),
], add=[
  X('To her mom (polite)', 'Hvala vam što ste me pozvali', 'HVAH-lah vahm shtoh steh meh POHZ-vah-lee', 'Thank you for inviting me'),
  X('To her, switching to casual', 'Možemo li na ti?', 'MOH-zheh-mo lee nah TEE', 'Can we use "ti" with each other?'),
])
P['on-ona'] = dict(ctx0='About her', fx=[
  ('On je moj brat', 'OHN yeh MOY BRAHT', 'He is my brother'),
  ('Ona je moja sestra', 'OH-nah yeh MOH-yah SEH-strah', 'She is my sister'),
  ('Oni su moji prijatelji', 'OH-nee soo MOH-yee PREE-yah-teh-lyee', 'They are my friends'),
  ('One su moje sestre', 'OH-neh soo MOH-yeh SEH-streh', 'They are my sisters (all women)'),
], forms_add=[
  F('Ono', 'OH-no', 'It (a neuter thing)', ('Ono je lepo', 'OH-no yeh LEH-po', 'It is nice (about the wine, the weather...)'), describes='it'),
], add=[
  X('About him', 'On dolazi sutra', 'OHN DOH-lah-zee SOO-trah', 'He is coming tomorrow'),
  X('About a thing (masc.)', 'On je skup', 'OHN yeh SKOOP', "It's expensive (about a masculine noun)"),
  X('About a group', 'Oni su kod kuće', 'OH-nee soo kod KOO-cheh', 'They are at home'),
])
P['ja-mi'] = dict(ctx0='Contrast', forms=[
  F('Ja', 'YAH', 'I (me, a man or a woman)', ('Ja sam Met', 'yah sahm MET', "I'm Matt"), describes='me'),
  F('Mi', 'MEE', 'We (you and her, or a group)', ('Mi idemo na kafu', 'mee EE-deh-mo nah KAH-foo', "We're going for coffee"), describes='us'),
  F('Meni', 'MEH-nee', 'To me / for me', ('Meni treba kafa', 'MEH-nee TREH-bah KAH-fah', 'I need a coffee'), describes='me'),
  F('Mene', 'MEH-neh', 'Me (as the object)', ('Pitaj mene', 'PEE-tai MEH-neh', 'Ask me'), describes='me'),
  F('Mi dvoje', 'mee DVOH-yeh', 'The two of us (you and her)', ('Mi dvoje idemo na večeru', 'mee DVOH-yeh EE-deh-mo nah VEH-cheh-roo', "The two of us are going to dinner"), describes='us'),
], changesBy=['describes'], add=[
  X('To her', 'Ja ću doći po tebe', 'yah choo DOH-chee poh TEH-beh', "I'll come pick you up"),
  X('About us', 'Mi smo kod kuće', 'mee smoh kod KOO-cheh', 'We are at home'),
])
P['to-be'] = dict(ctx0='Me and you', fx=[
  ('Ja sam Met', 'yah sahm MET', "I'm Matt"),
  ('Ti si lepa', 'tee see LEH-pah', "You're beautiful (to her)"),
  ('Ona je ovde. On je tamo', 'OH-nah yeh OHV-deh. OHN yeh TAH-mo', 'She is here. He is there'),
  ('Mi smo kod kuće', 'mee smoh kod KOO-cheh', 'We are at home'),
  ('Vi ste jako ljubazni', 'vee steh YAH-ko LYOO-bahz-nee', 'You are very kind (polite)'),
  ('Oni su u kafiću', 'OH-nee soo oo KAH-fee-choo', 'They are in the café'),
], add=[
  X('Her, about herself', 'Ja sam iz Srbije', 'yah sahm eez SUR-bee-yeh', "I'm from Serbia"),
  X('About a thing', 'Ovo je dobro', 'OH-vo yeh DOH-bro', 'This is good'),
])
P['nisam'] = dict(ctx0=['About me (man)', 'About a thing'], fx=[
  ('Nisam siguran', 'NEE-sahm SEE-goo-rahn', "I'm not sure (a man says this)"),
  ('Nisi sama', 'NEE-see SAH-mah', "You're not alone (to her)"),
  ('On nije ovde', 'OHN NEE-yeh OHV-deh', "He isn't here"),
  ('Nismo kasnili', 'NEES-mo KAHS-nee-lee', "We weren't late"),
  ('Niste u pravu', 'NEES-teh oo PRAH-voo', "You're not right (polite)"),
  ('Oni nisu kod kuće', 'OH-nee NEE-soo kod KOO-cheh', "They aren't at home"),
], add=[
  X('Her, about herself', 'Nisam umorna', 'NEE-sahm OO-mor-nah', "I'm not tired (a woman says this)"),
  X('To her', 'Nisi sama, tu sam', 'NEE-see SAH-mah, TOO sahm', "You're not alone, I'm here"),
])
P['nemam'] = dict(ctx0='Me', fx=[
  ('Nemam vremena', 'NEH-mahm VREH-meh-nah', "I don't have time"),
  ('Nemaš razloga da brineš', 'NEH-mahsh RAHZ-lo-gah dah BREE-nesh', "You have no reason to worry"),
  ('Ona nema auto', 'OH-nah NEH-mah OW-toh', "She doesn't have a car"),
  ('Nemamo kartu', 'NEH-mah-mo KAHR-too', "We don't have a ticket"),
  ('Nemate ključ?', 'NEH-mah-teh KLYOOCH', "Don't you have a key? (polite)"),
  ('Oni nemaju decu', 'OH-nee NEH-mah-yoo DEH-tsoo', "They don't have kids"),
], add=[
  X('To her', 'Nemaš poruku od njega', 'NEH-mahsh POH-roo-koo od NYEH-gah', "You don't have a message from him"),
  X('About a thing', 'Nema problema', 'NEH-mah proh-BLEH-mah', 'No problem'),
])
P['moj'] = dict(ctx0='Feminine noun (female friend)', fx=[
  ('Moj brat živi u Kanadi', 'MOY braht ZHEE-vee oo KAH-nah-dee', 'My brother lives in Canada'),
  ('Moja sestra je ovde', 'MOH-yah SEH-strah yeh OHV-deh', 'My sister is here'),
  ('Moje pivo je hladno', 'MOH-yeh PEE-vo yeh HLAHD-no', 'My beer is cold'),
], forms_add=[
  F('moji prijatelji', 'MOH-yee PREE-yah-teh-lyee', 'Plural, masculine nouns', ('Moji roditelji dolaze', 'MOH-yee roh-DEE-teh-lyee DOH-lah-zeh', 'My parents are coming'), nounGender='masculine plural'),
  F('moje drugarice', 'MOH-yeh droo-GAH-ree-tseh', 'Plural, feminine nouns', ('Moje drugarice su tu', 'MOH-yeh droo-GAH-ree-tseh soo TOO', 'My friends (female) are here'), nounGender='feminine plural'),
], add=[
  X('About him', 'Moj prijatelj ti šalje pozdrav', 'MOY PREE-yah-tel tee SHAH-lyeh POHZ-drahv', 'My friend sends you his regards'),
  X('To her, about us', 'Moja si', 'MOH-yah see', "You're mine (to her)"),
])
P['tvoj'] = dict(ctx0='Feminine noun', fx=[
  ('Gde je tvoj telefon?', 'GDEH yeh TVOY TEH-leh-fon', 'Where is your phone?'),
  ('Tvoja kuća je prelepa', 'TVOH-yah KOO-chah yeh preh-LEH-pah', 'Your house is gorgeous'),
  ('Tvoje vino je odlično', 'TVOH-yeh VEE-no yeh od-LEECH-no', 'Your wine is excellent'),
], forms_add=[
  F('vaš / vaša / vaše', 'VAHSH / VAH-shah / VAH-sheh', 'Polite "your", for elders or a group', ('Vaša kuća je prelepa, gospođo', 'VAH-shah KOO-chah yeh preh-LEH-pah, GOH-spoh-jo', 'Your house is gorgeous, ma’am'), formal='polite'),
  F('tvoji / tvoje (plural)', 'TVOH-yee / TVOH-yeh', 'Plural: your parents, your friends', ('Tvoji roditelji su divni', 'TVOH-yee roh-DEE-teh-lyee soo DEEV-nee', 'Your parents are wonderful'), nounGender='plural'),
], add=[
  X('To her, about her sister', 'Tvoja sestra je lepa', 'TVOH-yah SEH-strah yeh LEH-pah', 'Your sister is pretty'),
  X('To her, about her mom (polite)', 'Vaša kafa je odlična', 'VAH-shah KAH-fah yeh od-LEECH-nah', 'Your coffee is excellent'),
])
P['i'] = dict(ctx0='You and me', add=[
  X('Her and me', 'Ti i ona', 'tee ee OH-nah', 'You and her'),
  X('Things', 'Kafa i kolač', 'KAH-fah ee KOH-lahch', 'Coffee and cake'),
  X('Meaning "too"', 'I ja bih kafu', 'ee yah bih KAH-foo', "I'd like a coffee too"),
])
P['ali'] = dict(ctx0='About me', add=[
  X('To her', 'Lepa si, ali si luda', 'LEH-pah see, AH-lee see LOO-dah', "You're pretty, but you're crazy"),
  X('About someone else', 'On je dobar, ali kasni', 'OHN yeh DOH-bahr, AH-lee KAHS-nee', "He's good, but he's late"),
  X('About a thing', 'Skupo je, ali je dobro', 'SKOO-po yeh, AH-lee yeh DOH-bro', "It's expensive, but it's good"),
])
P['ili'] = dict(ctx0='Offering', add=[
  X('To her', 'Hoćeš li kafu ili čaj?', 'HOH-chesh lee KAH-foo EE-lee CHAI', 'Do you want coffee or tea?'),
  X('About a plan', 'Danas ili sutra?', 'DAH-nahs EE-lee SOO-trah', 'Today or tomorrow?'),
  X('About someone else', 'On ili ona?', 'OHN EE-lee OH-nah', 'Him or her?'),
])
P['bas'] = dict(ctx0='About a thing', add=[
  X('To her', 'Baš si slatka', 'BAHSH see SLAHT-kah', "You're so cute (to her)"),
  X('To him', 'Baš si smešan', 'BAHSH see SMEH-shahn', "You're so funny (to a man)"),
  X('About me (man)', 'Baš sam umoran', 'BAHSH sahm OO-mo-rahn', "I'm really tired"),
  X('Meaning "exactly"', 'Baš to hoću', 'BAHSH toh HOH-choo', "That's exactly what I want"),
])
P['takodje'] = dict(ctx0='Me too', add=[
  X('To her', 'Ti takođe', 'tee tah-KOH-jeh', 'You too'),
  X('About someone else', 'I on takođe dolazi', 'ee ohn tah-KOH-jeh DOH-lah-zee', "He's coming too"),
  X('About a thing', 'To je takođe dobro', 'toh yeh tah-KOH-jeh DOH-bro', "That's also good"),
])
P['brojevi'] = dict(ctx0='Ordering', fx=[
  ('Jedan pas, dva psa', 'YEH-dahn PAHS, DVAH PSAH', 'One dog, two dogs'),
  ('Jedna kafa, dve kafe', 'YED-nah KAH-fah, DVEH KAH-feh', 'One coffee, two coffees'),
  ('Jedno pivo, dva piva', 'YED-no PEE-vo, DVAH PEE-vah', 'One beer, two beers'),
], add=[
  X('Me, ordering', 'Jedno pivo, molim', 'YED-no PEE-vo, MOH-leem', 'One beer, please'),
  X('About someone else', 'Ima pet godina', 'EE-mah PET GOH-dee-nah', 'He / she is five years old'),
  X('Telling time', 'Vidimo se u osam', 'VEE-dee-mo seh oo OH-sahm', 'See you at eight'),
  X('About us', 'Nas je troje', 'NAHS yeh TROH-yeh', 'There are three of us'),
])
