P = {}
# ---------- Flirting ----------
P['falis-mi'] = dict(ctx0='To her', forms=[
  F('Fališ mi', 'FAH-leesh mee', 'I miss you (to one person)', ('Fališ mi večeras', 'FAH-leesh mee VEH-cheh-rahs', 'I miss you tonight'), describes='her', formal='casual'),
  F('Falim li ti?', 'FAH-leem lee tee', 'Asking her: "do you miss me?"', ('Falim li ti malo?', 'FAH-leem lee tee MAH-lo', 'Do you miss me a little?'), describes='me'),
  F('I ti meni fališ', 'ee tee MEH-nee FAH-leesh', 'Replying: "I miss you too"', ('I ti meni fališ, mnogo', 'ee tee MEH-nee FAH-leesh, MNOH-go', 'I miss you too, a lot'), describes='her'),
  F('Fali mi (mama)', 'FAH-lee mee (MAH-mah)', 'I miss someone else or something', ('Fali mi sestra', 'FAH-lee mee SEH-strah', 'I miss my sister'), describes='him / her'),
  F('Falite mi', 'FAH-lee-teh mee', 'Polite or to a group', ('Falite mi svi', 'FAH-lee-teh mee SVEE', 'I miss you all'), formal='polite'),
], changesBy=['describes', 'formal'], add=[
  X('To her, more', 'Fališ mi više nego što misliš', 'FAH-leesh mee VEE-sheh NEH-go shtoh MEE-sleesh', 'I miss you more than you think'),
  X('About a thing', 'Fali mi tvoj smeh', 'FAH-lee mee TVOY SMEH', 'I miss your laugh'),
])
P['lepa-si'] = dict(ctx0='To her, in the moment', fx=[
  ('Lepa si večeras', 'LEH-pah see VEH-cheh-rahs', "You're beautiful tonight"),
  ('Lep si u tom odelu', 'LEHP see oo tohm OH-deh-loo', "You look handsome in that suit"),
], forms_add=[
  F('Lepa je', 'LEH-pah yeh', 'Telling someone about a woman (she)', ('Tvoja mama je lepa', 'TVOH-yah MAH-mah yeh LEH-pah', 'Your mom is beautiful'), describes='her'),
  F('Lep je', 'LEHP yeh', 'Telling someone about a man (he)', ('Njen brat je lep', 'NYEHN braht yeh LEHP', 'Her brother is handsome'), describes='him'),
  F('Lepo je', 'LEH-po yeh', 'About a place or thing (neuter)', ('Lepo je ovde', 'LEH-po yeh OHV-deh', "It's beautiful here"), describes='it'),
  F('Lepa sam', 'LEH-pah sahm', 'Her, about herself', ('Lepa sam danas, zar ne?', 'LEH-pah sahm DAH-nahs, zahr NEH', "I'm pretty today, aren't I? (a woman says this)"), speaker='female'),
], changesBy=['describes', 'addressing'], add=[
  X('About a photo', 'Slika je lepa', 'SLEE-kah yeh LEH-pah', 'The picture is beautiful'),
  X('About a view', 'Pogled je prelep', 'POH-gled yeh PREH-lep', 'The view is gorgeous'),
])
P['izgledas-lepo'] = dict(ctx0='To her', forms=[
  F('Lepo izgledaš', 'LEH-po EEZ-gleh-dahsh', 'You (to her or to him, same)', ('Lepo izgledaš danas', 'LEH-po EEZ-gleh-dahsh DAH-nahs', 'You look nice today'), describes='her', formal='casual'),
  F('Lepo izgledam?', 'LEH-po EEZ-gleh-dahm', 'Me: asking "do I look nice?"', ('Lepo izgledam u ovome?', 'LEH-po EEZ-gleh-dahm oo OH-vo-meh', 'Do I look nice in this?'), describes='me'),
  F('Lepo izgleda', 'LEH-po EEZ-gleh-dah', 'Someone else (he / she) or a thing', ('Ona lepo izgleda. Jelo lepo izgleda', 'OH-nah LEH-po EEZ-gleh-dah. YEH-lo LEH-po EEZ-gleh-dah', 'She looks nice. The dish looks nice'), describes='him / her'),
  F('Lepo izgledate', 'LEH-po EEZ-gleh-dah-teh', 'Polite, or to a group', ('Lepo izgledate, gospođo', 'LEH-po EEZ-gleh-dah-teh, GOH-spoh-jo', 'You look nice, ma’am'), formal='polite'),
], changesBy=['describes', 'formal'], add=[
  X('To him', 'Lepo izgledaš, brate', 'LEH-po EEZ-gleh-dahsh, BRAH-teh', 'You look nice, man'),
  X('About a thing', 'Lepo izgleda tvoja haljina', 'LEH-po EEZ-gleh-dah TVOH-yah HAHL-yee-nah', 'Your dress looks nice'),
])
P['svidjas-mi-se'] = dict(ctx0='To her', forms=[
  F('Sviđaš mi se', 'SVEE-jahsh mee seh', 'I like you (to her or to him)', ('Sviđaš mi se, iskreno', 'SVEE-jahsh mee seh, EES-kreh-no', 'I like you, honestly'), describes='her', formal='casual'),
  F('Sviđam ti se?', 'SVEE-jahm tee seh', 'Asking her: "do you like me?"', ('Sviđam ti se bar malo?', 'SVEE-jahm tee seh bahr MAH-lo', 'Do you like me at least a little?'), describes='me'),
  F('Sviđaš joj / mu se', 'SVEE-jahsh yoy / moo seh', 'Someone else likes you (she / he)', ('Sviđaš joj se, vidim', 'SVEE-jahsh yoy seh, VEE-deem', 'She likes you, I can tell'), describes='him / her'),
  F('Sviđa mi se (ona)', 'SVEE-jah mee seh (OH-nah)', 'I like someone else or a thing', ('Sviđa mi se tvoja sestra. Sviđa mi se ova pesma', 'SVEE-jah mee seh TVOH-yah SEH-strah. SVEE-jah mee seh OH-vah PEH-smah', 'I like your sister. I like this song'), describes='him / her'),
  F('Sviđamo se', 'SVEE-jah-mo seh', 'We like each other', ('Sviđamo se jedno drugom', 'SVEE-jah-mo seh YED-no DROO-gom', 'We like each other'), describes='us'),
], changesBy=['describes'], add=[
  X('Her, to me', 'I ti se meni sviđaš', 'ee tee seh MEH-nee SVEE-jahsh', 'I like you too (she says this)'),
  X('About a place', 'Sviđa mi se ovaj kafić', 'SVEE-jah mee seh OH-vai KAH-feech', 'I like this café'),
])
P['mislim-na-tebe'] = dict(ctx0='To her', forms=[
  F('Mislim na tebe', 'MEE-sleem nah TEH-beh', 'I\'m thinking of you', ('Mislim na tebe ceo dan', 'MEE-sleem nah TEH-beh TSEH-oh DAHN', "I've been thinking of you all day"), describes='her', formal='casual'),
  F('Misliš li na mene?', 'MEE-sleesh lee nah MEH-neh', 'Asking her: "do you think of me?"', ('Misliš li ponekad na mene?', 'MEE-sleesh lee POH-neh-kahd nah MEH-neh', 'Do you ever think of me?'), describes='me'),
  F('Misli na tebe', 'MEE-slee nah TEH-beh', 'Someone else is thinking of you', ('Mama misli na tebe', 'MAH-mah MEE-slee nah TEH-beh', 'Mom is thinking of you'), describes='him / her'),
  F('Mislim na nju / njega', 'MEE-sleem nah NYOO / NYEH-gah', 'I think about someone else', ('Mislim na nju. Mislim na njega', 'MEE-sleem nah NYOO. MEE-sleem nah NYEH-gah', 'I think about her. I think about him'), describes='him / her'),
  F('Mislimo na tebe', 'MEE-slee-mo nah TEH-beh', 'We\'re thinking of you', ('Mislimo na tebe svi', 'MEE-slee-mo nah TEH-beh SVEE', 'We are all thinking of you'), describes='us'),
], changesBy=['describes'], add=[
  X('Her, to me', 'I ja mislim na tebe', 'ee yah MEE-sleem nah TEH-beh', "I'm thinking of you too (she says this)"),
  X('About a thing', 'Mislim na onaj dan', 'MEE-sleem nah OH-nai DAHN', "I'm thinking of that day"),
])
P['draga'] = dict(ctx0='To her', fx=[
  ('Draga, kako si?', 'DRAH-gah, KAH-ko see', 'Dear, how are you? (to her)'),
  ('Dragi, hvala ti', 'DRAH-gee, HVAH-lah tee', 'Dear, thank you (to a man)'),
], forms_add=[
  F('Draga moja', 'DRAH-gah MOH-yah', 'More tender, to her', ('Draga moja, ne brini', 'DRAH-gah MOH-yah, neh BREE-nee', "My dear, don't worry"), describes='her'),
  F('Dragi moj', 'DRAH-gee MOY', 'More tender, to a man', ('Dragi moj, hvala za sve', 'DRAH-gee MOY, HVAH-lah zah SVEH', 'My dear, thanks for everything'), describes='him'),
  F('Draga Ana,', 'DRAH-gah AH-nah', 'Starting a letter or message to her', ('Draga Ana, piše ti Met', 'DRAH-gah AH-nah, PEE-sheh tee MET', 'Dear Ana, it is Matt writing to you'), describes='her'),
], add=[
  X('About someone else', 'Ona je draga osoba', 'OH-nah yeh DRAH-gah OH-soh-bah', 'She is a dear person'),
  X('About him', 'On je dragi prijatelj', 'OHN yeh DRAH-gee PREE-yah-tel', 'He is a dear friend'),
])
P['ljubavi'] = dict(ctx0='To her, goodnight', add=[
  X('To her, daytime', 'Ljubavi, gde si?', 'LYOO-bah-vee, GDEH see', 'Love, where are you?'),
  X('Replying', 'Hvala, ljubavi', 'HVAH-lah, LYOO-bah-vee', 'Thanks, my love'),
  X('About someone (noun)', 'Ona je ljubav mog života', 'OH-nah yeh LYOO-bahv mohg ZHEE-voh-tah', 'She is the love of my life'),
  X('About a thing', 'Muzika je moja ljubav', 'MOO-zee-kah yeh MOH-yah LYOO-bahv', 'Music is my love'),
])
P['laku-noc-lepotice'] = dict(ctx0='To her', fx=[('Laku noć, lepotice, sanjaj me', 'LAH-koo NOHTCH, leh-poh-TEE-tseh, SAH-nyai meh', 'Good night, beautiful, dream of me')], forms_add=[
  F('Dobro jutro, lepotice', 'DOH-bro YOO-tro, leh-poh-TEE-tseh', 'Morning version, to her', ('Dobro jutro, lepotice. Kako si spavala?', 'DOH-bro YOO-tro, leh-poh-TEE-tseh. KAH-ko see SPAH-vah-lah', 'Good morning, beautiful. How did you sleep?'), addressing='her', describes='her'),
  F('Ona je prava lepotica', 'OH-nah yeh PRAH-vah leh-poh-TEE-tsah', 'Talking about her to someone else', ('Tvoja sestra je prava lepotica', 'TVOH-yah SEH-strah yeh PRAH-vah leh-poh-TEE-tsah', 'Your sister is a real beauty'), describes='her'),
], add=[
  X('Morning', 'Dobro jutro, lepotice', 'DOH-bro YOO-tro, leh-poh-TEE-tseh', 'Good morning, beautiful'),
  X('About someone else', 'Ona je prava lepotica', 'OH-nah yeh PRAH-vah leh-poh-TEE-tsah', 'She is a real beauty'),
])
P['ljubim-te'] = dict(ctx0='Me, signing off', forms=[
  F('Ljubim te', 'LYOO-beem teh', 'Me to her or to him (sign-off)', ('Čujemo se, ljubim te', 'CHOO-yeh-mo seh, LYOO-beem teh', 'Talk soon, kisses'), describes='her', formal='casual'),
  F('Ljubi te (mama)', 'LYOO-bee teh (MAH-mah)', 'Someone else sends kisses', ('Mama te ljubi', 'MAH-mah teh LYOO-bee', 'Mom sends you kisses'), describes='him / her'),
  F('Ljubimo te', 'LYOO-bee-mo teh', 'We send kisses', ('Ljubimo te svi', 'LYOO-bee-mo teh SVEE', 'We all send kisses'), describes='us'),
  F('Ljubim vas', 'LYOO-beem vahs', 'Polite, to her parents or a group', ('Pozdrav i ljubim vas', 'POHZ-drahv ee LYOO-beem vahs', 'Greetings and kisses to you all'), formal='polite'),
], changesBy=['describes', 'formal'], add=[
  X('Her, to me', 'Ljubim te i ja', 'LYOO-beem teh ee YAH', 'Kisses to you too (she says this)'),
  X('Short', 'Ljubim te, laku noć', 'LYOO-beem teh, LAH-koo NOHTCH', 'Kisses, good night'),
])
P['volim-te'] = dict(ctx0='To her', forms=[
  F('Volim te', 'VOH-leem teh', 'I love you (to one person)', ('Volim te, znaš to', 'VOH-leem teh, ZNAHSH toh', 'I love you, you know that'), describes='her', formal='casual'),
  F('Voliš li me?', 'VOH-leesh lee meh', 'Asking her: "do you love me?"', ('Voliš li me stvarno?', 'VOH-leesh lee meh STVAHR-no', 'Do you really love me?'), describes='me'),
  F('Voli te', 'VOH-lee teh', 'Someone else loves you', ('Moja mama te voli', 'MOH-yah MAH-mah teh VOH-lee', 'My mom loves you'), describes='him / her'),
  F('Volim je / ga', 'VOH-leem yeh / gah', 'I love someone else (her / him)', ('Volim je. Volim ga kao brata', 'VOH-leem yeh. VOH-leem gah KAH-ko BRAH-tah', 'I love her. I love him like a brother'), describes='him / her'),
  F('Volimo te', 'VOH-lee-mo teh', 'We love you', ('Volimo te, vrati se', 'VOH-lee-mo teh, VRAH-tee seh', 'We love you, come back'), describes='us'),
  F('Volim vas', 'VOH-leem vahs', 'Polite or to a group', ('Volim vas sve', 'VOH-leem vahs SVEH', 'I love you all'), formal='polite'),
], changesBy=['describes', 'formal'], add=[
  X('Her, to me', 'I ja tebe volim', 'ee yah TEH-beh VOH-leem', 'I love you too (she says this)'),
  X('About a thing', 'Volim ovu pesmu', 'VOH-leem OH-voo PEH-smoo', 'I love this song'),
])
P['nasmejavas-me'] = dict(ctx0='To her', forms=[
  F('Nasmejavaš me', 'nah-smeh-YAH-vahsh meh', 'You make me laugh', ('Nasmejavaš me bez razloga', 'nah-smeh-YAH-vahsh meh bez RAHZ-lo-gah', 'You make me laugh for no reason'), describes='her', formal='casual'),
  F('Nasmejavam te', 'nah-smeh-YAH-vahm teh', 'Me: "I make you laugh"', ('Nasmejavam te, zar ne?', 'nah-smeh-YAH-vahm teh, zahr NEH', 'I make you laugh, don\'t I?'), describes='me'),
  F('Nasmejava me', 'nah-smeh-YAH-vah meh', 'Someone else (he / she) makes me laugh', ('Tvoj brat me nasmejava', 'TVOY braht meh nah-smeh-YAH-vah', 'Your brother makes me laugh'), describes='him / her'),
], changesBy=['describes'], add=[
  X('To him', 'Nasmejavaš me, brate', 'nah-smeh-YAH-vahsh meh, BRAH-teh', 'You make me laugh, man'),
  X('About a thing', 'Taj film me nasmejava', 'TAH-ee FEELM meh nah-smeh-YAH-vah', 'That film makes me laugh'),
])
# ---------- Teasing ----------
P['nisam-to-rekao'] = dict(ctx0='Me denying (man)', fx=[
  ('Nisam to rekao, kunem se', 'NEE-sahm toh REH-kah-oh, KOO-nem seh', "I didn't say that, I swear"),
  ('Nisam to rekla, ti izmišljaš', 'NEE-sahm toh REK-lah, tee eez-MEESH-lyahsh', "I didn't say that, you're making it up (a woman says this)"),
], forms_add=[
  F('Nisi to rekla', 'NEE-see toh REK-lah', 'To her: "you didn\'t say that"', ('Nisi to rekla, sećam se', 'NEE-see toh REK-lah, SEH-chahm seh', "You didn't say that, I remember"), describes='her'),
  F('Nije to rekao / rekla', 'NEE-yeh toh REH-kah-oh / REK-lah', 'About someone else (he / she)', ('Nije to rekao, ja sam bio tamo', 'NEE-yeh toh REH-kah-oh, yah sahm BEE-oh TAH-mo', "He didn't say that, I was there"), describes='him / her'),
], add=[
  X('To her', 'Ti si to rekla, ne ja', 'tee see toh REK-lah, neh YAH', 'You said that, not me (to her)'),
  X('To him', 'Ti si to rekao, ne ja', 'tee see toh REH-kah-oh, neh YAH', 'You said that, not me (to a man)'),
  X('About someone else', 'Ona nije to rekla', 'OH-nah NEE-yeh toh REK-lah', "She didn't say that"),
])
P['zezas-me'] = dict(ctx0='To her', forms=[
  F('Zezaš me', 'ZEH-zahsh meh', 'You, messing with me', ('Zezaš me, vidim te', 'ZEH-zahsh meh, VEE-deem teh', "You're messing with me, I can tell"), describes='her', formal='casual'),
  F('Zezam te', 'ZEH-zahm teh', 'Me, messing with you', ('Samo te zezam', 'SAH-mo teh ZEH-zahm', "I'm just messing with you"), describes='me'),
  F('Zeza me', 'ZEH-zah meh', 'Someone else is teasing me', ('Brat me stalno zeza', 'BRAHT meh STAHL-no ZEH-zah', 'My brother is always teasing me'), describes='him / her'),
  F('Zezate me', 'ZEH-zah-teh meh', 'Polite or a group', ('Zezate me, zar ne?', 'ZEH-zah-teh meh, zahr NEH', "You're messing with me, aren't you?"), formal='polite'),
], changesBy=['describes', 'formal'], add=[
  X('To him', 'Zezaš me, brate?', 'ZEH-zahsh meh, BRAH-teh', "Are you messing with me, man?"),
  X('Her teasing me', 'Zezam te malo', 'ZEH-zahm teh MAH-lo', "I'm teasing you a little (she says this)"),
])
P['nemoguc-sam'] = dict(ctx0='Me (man)', fx=[
  ('Nemoguć sam, ali me voliš', 'NEH-moh-gooch sahm, AH-lee meh VOH-leesh', "I'm impossible, but you love me"),
  ('Nemoguća sam, znam', 'NEH-moh-goo-chah sahm, znahm', "I'm impossible, I know (a woman says this)"),
], forms_add=[
  F('Nemoguća si', 'NEH-moh-goo-chah see', 'Teasing her', ('Nemoguća si, znaš li to?', 'NEH-moh-goo-chah see, znahsh lee TOH', "You're impossible, you know that?"), describes='her'),
  F('Nemoguć si', 'NEH-moh-gooch see', 'Teasing a man', ('Nemoguć si, brate', 'NEH-moh-gooch see, BRAH-teh', "You're impossible, man"), describes='him'),
  F('Nemoguć / nemoguća je', 'NEH-moh-gooch / NEH-moh-goo-chah yeh', 'About someone else (he / she)', ('Moja sestra je nemoguća', 'MOH-yah SEH-strah yeh NEH-moh-goo-chah', 'My sister is impossible'), describes='him / her'),
], add=[
  X('To her', 'Nemoguća si, ali si moja', 'NEH-moh-goo-chah see, AH-lee see MOH-yah', "You're impossible, but you're mine"),
  X('About someone else', 'On je nemoguć', 'OHN yeh NEH-moh-gooch', "He's impossible"),
])
P['samo-se-salim'] = dict(ctx0='Me', forms=[
  F('Samo se šalim', 'SAH-mo seh SHAH-leem', 'Me (same for a man or a woman)', ('Samo se šalim, stvarno', 'SAH-mo seh SHAH-leem, STVAHR-no', "I'm only joking, really"), describes='me'),
  F('Samo se šališ?', 'SAH-mo seh SHAH-leesh', 'Asking her: "are you just joking?"', ('Samo se šališ, zar ne?', 'SAH-mo seh SHAH-leesh, zahr NEH', "You're just joking, right?"), describes='her', formal='casual'),
  F('Samo se šali', 'SAH-mo seh SHAH-lee', 'Someone else (he / she)', ('Ne brini, samo se šali', 'neh BREE-nee, SAH-mo seh SHAH-lee', "Don't worry, he's just joking"), describes='him / her'),
  F('Samo se šalimo', 'SAH-mo seh SHAH-lee-mo', 'We\'re just joking', ('Samo se šalimo malo', 'SAH-mo seh SHAH-lee-mo MAH-lo', "We're just joking a little"), describes='us'),
], changesBy=['describes'], add=[
  X('Her, about herself', 'Samo se šalim, ljubavi', 'SAH-mo seh SHAH-leem, LYOO-bah-vee', "I'm just joking, my love (same for a man or a woman)"),
  X('About a thing', 'To je samo šala', 'TOH yeh SAH-mo SHAH-lah', "It's just a joke"),
])
P['ne-ljuti-se'] = dict(fx=[
  ('Ne ljuti se, molim te', 'neh LYOO-tee seh, MOH-leem teh', "Don't be mad, please (to her or to him)"),
  ('Ne ljutite se, nije moja greška', 'neh LYOO-tee-teh seh, NEE-yeh MOH-yah GREH-shkah', "Don't be angry, it's not my fault"),
], forms_add=[
  F('Ne ljuti se na mene', 'neh LYOO-tee seh nah MEH-neh', 'Don\'t be mad at me', ('Ne ljuti se na mene, molim te', 'neh LYOO-tee seh nah MEH-neh, MOH-leem teh', "Don't be mad at me, please"), describes='me'),
  F('Ne ljuti se na njega', 'neh LYOO-tee seh nah NYEH-gah', 'Don\'t be mad at him', ('Ne ljuti se na njega, nije hteo', 'neh LYOO-tee seh nah NYEH-gah, NEE-yeh HTEH-oh', "Don't be mad at him, he didn't mean to"), describes='him'),
  F('Ne ljuti se na nju', 'neh LYOO-tee seh nah NYOO', 'Don\'t be mad at her', ('Ne ljuti se na nju, ona je dete', 'neh LYOO-tee seh nah NYOO, OH-nah yeh DEH-teh', "Don't be mad at her, she is a kid"), describes='her'),
], changesBy=['formal', 'describes'], add=[
  X('To her, after a joke', 'Ne ljuti se, samo sam se šalio', 'neh LYOO-tee seh, SAH-mo sahm seh SHAH-lee-oh', "Don't be mad, I was only joking (a man says this)"),
  X('To him', 'Ne ljuti se, brate, nisam hteo', 'neh LYOO-tee seh, BRAH-teh, NEE-sahm HTEH-oh', "Don't be mad, man, I didn't mean to"),
  X('Her, to me', 'Ne ljuti se, samo sam se šalila', 'neh LYOO-tee seh, SAH-mo sahm seh SHAH-lee-lah', "Don't be mad, I was only joking (a woman says this)"),
])
P['luda-si'] = dict(ctx0='To her', fx=[
  ('Ti si luda, volim te', 'tee see LOO-dah, VOH-leem teh', "You're crazy, I love you"),
  ('Ti si lud, brate', 'tee see LOOD, BRAH-teh', "You're crazy, man"),
], forms_add=[
  F('Ja sam lud', 'yah sahm LOOD', 'Me, a man about himself', ('Ja sam lud za tobom', 'yah sahm LOOD zah TOH-bom', "I'm crazy about you (a man says this)"), speaker='male'),
  F('Ja sam luda', 'yah sahm LOO-dah', 'Her, about herself', ('Ja sam luda, znam', 'yah sahm LOO-dah, znahm', "I'm crazy, I know (a woman says this)"), speaker='female'),
  F('On je lud / ona je luda', 'ohn yeh LOOD / OH-nah yeh LOO-dah', 'About someone else', ('Njena sestra je luda', 'NYEH-nah SEH-strah yeh LOO-dah', 'Her sister is crazy'), describes='him / her'),
], changesBy=['describes', 'speaker'], add=[
  X('About me', 'Ja sam lud za tobom', 'yah sahm LOOD zah TOH-bom', "I'm crazy about you (a man says this)"),
  X('About someone else', 'Ona je luda, ali simpatična', 'OH-nah yeh LOO-dah, AH-lee seem-pah-TEECH-nah', "She's crazy, but nice"),
])
# ---------- Making plans ----------
P['hoces-da-izadjemo'] = dict(ctx0='To her', forms=[
  F('Hoćeš da izađemo?', 'HOH-chesh dah ee-ZAH-jeh-mo', 'To her or to him (casual)', ('Hoćeš da izađemo večeras?', 'HOH-chesh dah ee-ZAH-jeh-mo VEH-cheh-rahs', 'Do you want to go out tonight?'), describes='her', formal='casual'),
  F('Želite li da izađemo?', 'ZHEH-lee-teh lee dah ee-ZAH-jeh-mo', 'Polite, to an elder', ('Želite li da izađemo na kafu?', 'ZHEH-lee-teh lee dah ee-ZAH-jeh-mo nah KAH-foo', 'Would you like to go out for coffee?'), formal='polite'),
  F('Hoću da izađem', 'HOH-choo dah ee-ZAH-jem', 'Me: "I want to go out"', ('Hoću da izađem, dosadno mi je', 'HOH-choo dah ee-ZAH-jem, doh-SAHD-no mee yeh', "I want to go out, I'm bored"), describes='me'),
  F('Hoće li da izađe?', 'HOH-cheh lee dah ee-ZAH-jeh', 'Asking about someone else', ('Hoće li ona da izađe sa nama?', 'HOH-cheh lee OH-nah dah ee-ZAH-jeh sah NAH-mah', 'Does she want to go out with us?'), describes='him / her'),
], changesBy=['formal', 'describes'], add=[
  X('To him', 'Hoćeš da izađemo, brate?', 'HOH-chesh dah ee-ZAH-jeh-mo, BRAH-teh', 'Want to go out, man?'),
  X('About a group', 'Hoćemo li da izađemo svi?', 'HOH-cheh-mo lee dah ee-ZAH-jeh-mo SVEE', 'Shall we all go out?'),
])
P['kad-si-slobodna'] = dict(fx=[
  ('Kad si slobodna ovog vikenda?', 'KAHD see SLOHB-od-nah OH-vog VEE-ken-dah', 'When are you free this weekend?'),
  ('Kad si slobodan, brate?', 'KAHD see SLOH-bo-dahn, BRAH-teh', 'When are you free, man?'),
], forms_add=[
  F('Slobodan sam', 'SLOH-bo-dahn sahm', 'Me, a man: "I\'m free"', ('Slobodan sam u subotu', 'SLOH-bo-dahn sahm oo SOO-boh-too', "I'm free on Saturday"), speaker='male'),
  F('Slobodna sam', 'SLOHB-od-nah sahm', 'Her: "I\'m free"', ('Slobodna sam posle šest', 'SLOHB-od-nah sahm POH-sleh SHEST', "I'm free after six (a woman says this)"), speaker='female'),
  F('Kad je ona / on slobodan?', 'KAHD yeh OH-nah / ohn SLOH-bo-dahn', 'Asking about someone else', ('Kad je ona slobodna?', 'KAHD yeh OH-nah SLOHB-od-nah', 'When is she free?'), describes='him / her'),
  F('Kad smo slobodni?', 'KAHD smoh SLOHB-od-nee', 'Us', ('Kad smo slobodni oboje?', 'KAHD smoh SLOHB-od-nee OH-bo-yeh', 'When are we both free?'), describes='us'),
], changesBy=['describes', 'speaker'], add=[
  X('To her', 'Kad si slobodna da se vidimo?', 'KAHD see SLOHB-od-nah dah seh VEE-dee-mo', 'When are you free to meet?'),
  X('To him', 'Kad si slobodan da se vidimo?', 'KAHD see SLOH-bo-dahn dah seh VEE-dee-mo', 'When are you free to meet? (to a man)'),
  X('About me (man)', 'Slobodan sam sutra uveče', 'SLOH-bo-dahn sahm SOO-trah OO-veh-cheh', "I'm free tomorrow evening"),
])
P['gde-da-se-nadjemo'] = dict(ctx0='To her', add=[
  X('Suggesting', 'Nađimo se ispred kafića', 'NAH-jee-mo seh EES-pred KAH-fee-chah', "Let's meet in front of the café"),
  X('About me', 'Ja sam kod fontane', 'yah sahm kod FOHN-tah-neh', "I'm by the fountain"),
  X('About a group', 'Gde da se nađemo svi?', 'GDEH dah seh NAH-jeh-mo SVEE', 'Where should we all meet?'),
  X('About someone else', 'Gde da se nađe sa nama?', 'GDEH dah seh NAH-jeh sah NAH-mah', 'Where should he / she meet us?'),
])
P['u-koliko-sati'] = dict(ctx0='To her', add=[
  X('Suggesting', 'U osam, može?', 'oo OH-sahm, MOH-zheh', 'At eight, OK?'),
  X('About someone else', 'U koliko sati on stiže?', 'oo KOH-lee-ko SAH-tee ohn STEE-zheh', 'What time is he arriving?'),
  X('About a thing', 'U koliko sati počinje film?', 'oo KOH-lee-ko SAH-tee POH-chee-nyeh FEELM', 'What time does the movie start?'),
  X('About me', 'U koliko sati treba da budem tamo?', 'oo KOH-lee-ko SAH-tee TREH-bah dah BOO-dem TAH-mo', 'What time should I be there?'),
])
P['kasnim'] = dict(ctx0='Me, now', forms=[
  F('Kasnim malo', 'KAHS-neem MAH-lo', 'Me, right now (man or woman)', ('Kasnim malo, stižem za deset', 'KAHS-neem MAH-lo, STEE-zhem zah DEH-set', "I'm a bit late, arriving in ten"), describes='me'),
  F('Kasniš', 'KAHS-neesh', 'You, to her', ('Kasniš, gde si?', 'KAHS-neesh, GDEH see', "You're late, where are you?"), describes='her', formal='casual'),
  F('Kasni', 'KAHS-nee', 'Someone else, or a bus / train', ('On kasni. Autobus kasni', 'OHN KAHS-nee. ow-TOH-boos KAHS-nee', 'He is late. The bus is late'), describes='him / her'),
  F('Kasnimo', 'KAHS-nee-mo', 'We', ('Kasnimo, izvini', 'KAHS-nee-mo, eez-VEE-nee', "We're late, sorry"), describes='us'),
  F('Kasnio sam', 'KAHS-nee-oh sahm', 'Me, past, a man', ('Kasnio sam, izvini', 'KAHS-nee-oh sahm, eez-VEE-nee', 'I was late, sorry'), speaker='male'),
  F('Kasnila sam', 'KAHS-nee-lah sahm', 'Her, past, about herself', ('Kasnila sam, bila je gužva', 'KAHS-nee-lah sahm, BEE-lah yeh GOOZH-vah', 'I was late, there was traffic (a woman says this)'), speaker='female'),
], changesBy=['speaker', 'describes'], add=[
  X('To her', 'Kasniš malo, sve u redu?', 'KAHS-neesh MAH-lo, SVEH oo REH-doo', "You're a bit late, everything OK?"),
  X('About a thing', 'Voz kasni dvadeset minuta', 'VOHZ KAHS-nee DVAH-deh-set mee-NOO-tah', 'The train is twenty minutes late'),
])
P['stigao-sam'] = dict(ctx0='Me (man)', fx=[
  ('Stigao sam u grad', 'STEE-gah-oh sahm oo GRAHD', "I've arrived in the city"),
  ('Stigla sam kući', 'STEEG-lah sahm KOO-chee', "I've arrived home (a woman says this)"),
], forms_add=[
  F('Stigla si?', 'STEEG-lah see', 'Asking her: "did you arrive?"', ('Stigla si? Javi mi', 'STEEG-lah see? YAH-vee mee', 'Did you arrive? Let me know'), describes='her'),
  F('Stigao si?', 'STEE-gah-oh see', 'Asking a man', ('Stigao si, brate?', 'STEE-gah-oh see, BRAH-teh', 'Did you arrive, man?'), describes='him'),
  F('Stigla je / stigao je', 'STEEG-lah yeh / STEE-gah-oh yeh', 'Someone else (she / he)', ('Ona je stigla. On je stigao', 'OH-nah yeh STEEG-lah. OHN yeh STEE-gah-oh', 'She arrived. He arrived'), describes='him / her'),
  F('Stigli smo', 'STEEG-lee smoh', 'We arrived', ('Stigli smo, gde si?', 'STEEG-lee smoh, GDEH see', 'We arrived, where are you?'), describes='us'),
], changesBy=['speaker', 'describes', 'tense'], add=[
  X('To her', 'Stigla si na vreme', 'STEEG-lah see nah VREH-meh', 'You arrived on time (to her)'),
  X('About a thing', 'Paket je stigao', 'PAH-ket yeh STEE-gah-oh', 'The package arrived'),
])
P['ne-mogu-da-dodjem'] = dict(ctx0='Me', forms=[
  F('Ne mogu da dođem', 'neh MOH-goo dah DOH-jem', 'Me (man or woman)', ('Ne mogu da dođem, radim', 'neh MOH-goo dah DOH-jem, RAH-deem', "I can't come, I'm working"), describes='me'),
  F('Ne možeš da dođeš?', 'neh MOH-zhesh dah DOH-jesh', 'Asking her: "you can\'t come?"', ('Ne možeš da dođeš večeras?', 'neh MOH-zhesh dah DOH-jesh VEH-cheh-rahs', "You can't come tonight?"), describes='her', formal='casual'),
  F('Ne može da dođe', 'neh MOH-zheh dah DOH-jeh', 'Someone else (he / she)', ('Ona ne može da dođe', 'OH-nah neh MOH-zheh dah DOH-jeh', "She can't come"), describes='him / her'),
  F('Ne možemo da dođemo', 'neh MOH-zheh-mo dah DOH-jeh-mo', 'We', ('Ne možemo da dođemo oboje', 'neh MOH-zheh-mo dah DOH-jeh-mo OH-bo-yeh', "We can't both come"), describes='us'),
  F('Ne mogu da dođu', 'neh MOH-goo dah DOH-joo', 'They', ('Roditelji ne mogu da dođu', 'roh-DEE-teh-lyee neh MOH-goo dah DOH-joo', "My parents can't come"), describes='them'),
], changesBy=['describes', 'formal'], add=[
  X('To her, with an excuse', 'Ne mogu da dođem, bolestan sam', 'neh MOH-goo dah DOH-jem, BOH-leh-stahn sahm', "I can't come, I'm sick (a man says this)"),
  X('Her, to me', 'Ne mogu da dođem, bolesna sam', 'neh MOH-goo dah DOH-jem, BOH-less-nah sahm', "I can't come, I'm sick (a woman says this)"),
])
P['pomerimo'] = dict(ctx0='Us', forms=[
  F('Možemo li da pomerimo?', 'MOH-zheh-mo lee dah poh-MEH-ree-mo', 'Us: "can we reschedule?"', ('Možemo li da pomerimo za sat?', 'MOH-zheh-mo lee dah poh-MEH-ree-mo zah SAHT', 'Can we move it by an hour?'), describes='us'),
  F('Možeš li da pomeriš?', 'MOH-zhesh lee dah poh-MEH-reesh', 'Asking her: "can you move it?"', ('Možeš li da pomeriš za sutra?', 'MOH-zhesh lee dah poh-MEH-reesh zah SOO-trah', 'Can you move it to tomorrow?'), describes='her', formal='casual'),
  F('Mogu li da pomerim?', 'MOH-goo lee dah poh-MEH-reem', 'Me: "can I move it?"', ('Mogu li da pomerim na osam?', 'MOH-goo lee dah poh-MEH-reem nah OH-sahm', 'Can I move it to eight?'), describes='me'),
  F('Može li da pomeri?', 'MOH-zheh lee dah poh-MEH-ree', 'Someone else', ('Može li on da pomeri?', 'MOH-zheh lee ohn dah poh-MEH-ree', 'Can he move it?'), describes='him / her'),
], changesBy=['describes', 'formal'], add=[
  X('To her, explaining', 'Moram da pomerim, imam sastanak', 'MOH-rahm dah poh-MEH-reem, EE-mahm SAH-stah-nahk', 'I have to reschedule, I have a meeting'),
  X('About a thing', 'Sastanak je pomeren za petak', 'SAH-stah-nahk yeh POH-meh-ren zah PEH-tahk', 'The meeting was moved to Friday'),
])
P['moze'] = dict(ctx0='Agreeing', add=[
  X('To her', 'Može, ti odluči', 'MOH-zheh, tee OHD-loo-chee', 'OK, you decide'),
  X('As a question', 'Može li u osam?', 'MOH-zheh lee oo OH-sahm', 'Is eight OK?'),
  X('About someone else', 'Može, on dolazi', 'MOH-zheh, ohn DOH-lah-zee', "OK, he's coming"),
  X('About a thing', 'Može i to', 'MOH-zheh ee TOH', 'That works too'),
])
P['dogovoreno'] = dict(ctx0='Settling a plan', add=[
  X('Past, we agreed', 'Dogovorili smo se za petak', 'doh-GOH-vo-ree-lee smoh seh zah PEH-tahk', 'We agreed on Friday'),
  X('To her', 'Jesmo li se dogovorili?', 'YES-mo lee seh doh-GOH-vo-ree-lee', 'Did we agree?'),
  X('About her', 'Ona se složila, dogovoreno je', 'OH-nah seh SLOH-zhee-lah, doh-GOH-vo-reh-no yeh', 'She agreed, it is settled'),
  X('About him', 'On se složio, dogovoreno je', 'OHN seh SLOH-zhee-oh, doh-GOH-vo-reh-no yeh', 'He agreed, it is settled'),
])
# ---------- Swearing ----------
P['jebote'] = dict(ctx0='Shock', add=[
  X('About a thing', 'Jebote, kakva gužva!', 'YEH-bo-teh, KAHK-vah GOOZH-vah', 'Damn, what a crowd!'),
  X('Me (man)', 'Jebote, zaboravio sam ključeve', 'YEH-bo-teh, zah-BOH-rah-vee-oh sahm KLYOO-cheh-veh', 'Damn, I forgot my keys'),
  X('Her, about herself', 'Jebote, zaboravila sam ključeve', 'YEH-bo-teh, zah-BOH-rah-vee-lah sahm KLYOO-cheh-veh', 'Damn, I forgot my keys (a woman says this)'),
  X('About someone else', 'Jebote, ona je pobedila!', 'YEH-bo-teh, OH-nah yeh poh-BEH-dee-lah', 'Damn, she won!'),
])
P['majke-mi'] = dict(ctx0='Me (man)', add=[
  X('Her, about herself', 'Majke mi, nisam znala', 'MAI-keh mee, NEE-sahm ZNAH-lah', "I swear, I didn't know (a woman says this)"),
  X('About someone else', 'Majke mi, ona je to rekla', 'MAI-keh mee, OH-nah yeh toh REK-lah', 'I swear, she said that'),
  X('About a thing', 'Majke mi, ovo je najbolja kafa', 'MAI-keh mee, OH-vo yeh NAI-bohl-yah KAH-fah', 'I swear, this is the best coffee'),
])
P['do-vraga'] = dict(ctx0='Me (man)', add=[
  X('Her, about herself', 'Do vraga, zaboravila sam telefon', 'doh VRAH-gah, zah-BOH-rah-vee-lah sahm TEH-leh-fon', 'Damn, I forgot my phone (a woman says this)'),
  X('About a thing', 'Do vraga, pokvario se telefon', 'doh VRAH-gah, POHK-vah-ree-oh seh TEH-leh-fon', 'Damn, the phone broke'),
  X('About someone else', 'Do vraga, opet je on kasnio', 'doh VRAH-gah, OH-pet yeh ohn KAHS-nee-oh', 'Damn, he is late again'),
  X('Stronger, to someone', 'Idi do vraga!', 'EE-dee doh VRAH-gah', 'Go to hell!'),
])
P['sranje'] = dict(ctx0='Me', add=[
  X('About a thing', 'Sranje, nema interneta', 'SRAH-nyeh, NEH-mah EEN-ter-neh-tah', 'Crap, there is no internet'),
  X('Her, about herself', 'Sranje, ostavila sam ključeve', 'SRAH-nyeh, oh-STAH-vee-lah sahm KLYOO-cheh-veh', 'Crap, I left my keys (a woman says this)'),
  X('About someone else', 'Sranje, on je sve pokvario', 'SRAH-nyeh, ohn yeh SVEH POHK-vah-ree-oh', 'Crap, he ruined everything'),
  X('About an opinion', 'To je sve sranje', 'TOH yeh SVEH SRAH-nyeh', "That's all bullshit"),
])
P['jebi-se'] = dict(forms=[
  F('Jebi se', 'YEH-bee seh', 'To one person (a man or a woman)', ('Jebi se, nisam ja kriv', 'YEH-bee seh, NEE-sahm yah KREEV', "F*** off, it's not my fault (a man says this)"), formal='casual'),
  F('Jebite se', 'YEH-bee-teh seh', 'To a group', ('Jebite se, ostavite me na miru', 'YEH-bee-teh seh, oh-STAH-vee-teh meh nah MEE-roo', 'F*** off, leave me alone'), formal='polite'),
], changesBy=['formal'], add=[
  X('Her, to me', 'Jebi se, što si to uradio?', 'YEH-bee seh, shtoh see toh OO-rah-dee-oh', 'F*** off, why did you do that? (what she might say)'),
  X('Playful, close friends only', 'Jebi se, bre, to nije smešno', 'YEH-bee seh, BREH, toh NEE-yeh SMESH-no', "F*** off, man, that's not funny"),
  X('Group', 'Jebite se svi', 'YEH-bee-teh seh SVEE', 'F*** off, all of you'),
])
P['mars'] = dict(ctx0='To a friend', add=[
  X('To her, playful', 'Marš, ne zezaj me', 'MAHRSH, neh ZEH-zai meh', "Get lost, don't tease me"),
  X('To a kid', 'Marš u krevet!', 'MAHRSH oo KREH-vet', 'Off to bed!'),
  X('Disbelief', 'Marš odavde, nisi ozbiljan', 'MAHRSH OH-dahv-deh, NEE-see OHZ-bee-lyahn', "Get out of here, you're not serious (to a man)"),
])
P['izvini-na-izrazu'] = dict(ctx0='Me, after swearing', fx=[
  ('Izvini na izrazu, ljut sam', 'eez-VEE-nee nah EEZ-rah-zoo, LYOOT sahm', "Pardon my language, I'm angry (a man says this)"),
  ('Izvinite na izrazu, nisam hteo', 'eez-VEE-nee-teh nah EEZ-rah-zoo, NEE-sahm HTEH-oh', "Pardon my language, I didn't mean to"),
], add=[
  X('Her, about herself', 'Izvini na izrazu, ljuta sam', 'eez-VEE-nee nah EEZ-rah-zoo, LYOO-tah sahm', "Pardon my language, I'm angry (a woman says this)"),
  X('About a thing', 'Izvini na izrazu, ali ovo je sranje', 'eez-VEE-nee nah EEZ-rah-zoo, AH-lee OH-vo yeh SRAH-nyeh', "Pardon my language, but this is crap"),
])
P['nemoj-tako'] = dict(ctx0='To a friend', fx=[
  ('Nemoj tako da pričaš, molim te', 'NEH-moy TAH-ko dah PREE-chahsh, MOH-leem teh', "Don't talk like that, please (to her or to him)"),
  ('Nemojte tako da pričate pred decom', 'NEH-moy-teh TAH-ko dah PREE-chah-teh pred DEH-tsom', "Don't talk like that in front of the kids"),
], forms_add=[
  F('Nemoj tako da pričaš o njemu', 'NEH-moy TAH-ko dah PREE-chahsh oh NYEH-moo', 'About him', ('Nemoj tako da pričaš o njemu', 'NEH-moy TAH-ko dah PREE-chahsh oh NYEH-moo', "Don't talk about him like that"), describes='him'),
  F('Nemoj tako da pričaš o njoj', 'NEH-moy TAH-ko dah PREE-chahsh oh NYOY', 'About her', ('Nemoj tako da pričaš o njoj', 'NEH-moy TAH-ko dah PREE-chahsh oh NYOY', "Don't talk about her like that"), describes='her'),
], changesBy=['formal', 'describes'], add=[
  X('Her, to me', 'Nemoj tako sa mnom da pričaš', 'NEH-moy TAH-ko sah MNOHM dah PREE-chahsh', "Don't talk to me like that (what she might say)"),
  X('To him', 'Nemoj tako, brate, ima dece', 'NEH-moy TAH-ko, BRAH-teh, EE-mah DEH-tseh', "Don't talk like that, man, there are kids here"),
])
P['ko-to-kaze'] = dict(ctx0='Me, defending myself', add=[
  X('To her', 'Ko to kaže? Ti?', 'KOH toh KAH-zheh? TEE', 'Says who? You?'),
  X('Her, to me', 'Ko to kaže? Nisam ja kasnila', 'KOH toh KAH-zheh? NEE-sahm yah KAHS-nee-lah', "Says who? I wasn't late (a woman says this)"),
  X('About someone else', 'Ko je to rekao? On?', 'KOH yeh toh REH-kah-oh? OHN', 'Who said that? Him?'),
  X('A challenge', 'Ko kaže da ne mogu?', 'KOH KAH-zheh dah neh MOH-goo', "Who says I can't?"),
])
P['vidi-ko-prica'] = dict(ctx0='To her', fx=[
  ('Vidi ko priča, sam stalno kasniš', 'VEE-dee KOH PREE-chah, SAHM STAHL-no KAHS-neesh', "Look who's talking, you're always late yourself (to a man)"),
  ('Vidite ko priča, i vi kasnite', 'VEE-dee-teh KOH PREE-chah, ee vee KAHS-nee-teh', "Look who's talking, you're late too"),
], add=[
  X('About someone else', 'Vidi ko priča, on nikad ne stigne na vreme', 'VEE-dee KOH PREE-chah, ohn NEE-kahd neh STEEG-neh nah VREH-meh', "Look who's talking, he never arrives on time"),
  X('About her, to a friend', 'Vidi ko priča, ona je najgora', 'VEE-dee KOH PREE-chah, OH-nah yeh NAI-go-rah', "Look who's talking, she is the worst"),
])
P['sta-ti-znas'] = dict(ctx0='To her', forms=[
  F('Šta ti znaš', 'SHTAH tee ZNAHSH', 'To her or to him (teasing)', ('Šta ti znaš o fudbalu?', 'SHTAH tee ZNAHSH oh FOOD-bah-loo', 'What do you know about football?'), describes='her', formal='casual'),
  F('Šta ja znam', 'SHTAH yah ZNAHM', 'Me: "what do I know?" / "who knows"', ('Šta ja znam, možda?', 'SHTAH yah ZNAHM, MOHZH-dah', 'What do I know, maybe?'), describes='me'),
  F('Šta on / ona zna', 'SHTAH ohn / OH-nah ZNAH', 'About someone else', ('Šta on zna o tome?', 'SHTAH ohn ZNAH oh TOH-meh', 'What does he know about it?'), describes='him / her'),
  F('Šta vi znate', 'SHTAH vee ZNAH-teh', 'Polite, or to a group', ('Šta vi znate o tome?', 'SHTAH vee ZNAH-teh oh TOH-meh', 'What do you know about it?'), formal='polite'),
], changesBy=['describes', 'formal'], add=[
  X('To him', 'Šta ti znaš, brate?', 'SHTAH tee ZNAHSH, BRAH-teh', 'What do you know, man?'),
  X('About a topic', 'Šta ti znaš o kuvanju?', 'SHTAH tee ZNAHSH oh KOO-vah-nyoo', 'What do you know about cooking?'),
])
