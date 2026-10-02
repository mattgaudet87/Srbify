"""Adds entries for subcategories that had nothing in them after the re-map. Idempotent (skips existing ids).
Run order: remap.py -> new_entries.py -> build_words.py -> check_words.py"""
import json, os, sys
os.chdir(os.path.join(os.path.dirname(__file__), '..')); sys.path.insert(0, 'scripts')
from remap import P

def X(ctx, sr, pr, en): return {'serbian': sr, 'pronunciation': pr, 'english': en, 'context': ctx}
def ex(t): return {'serbian': t[0], 'pronunciation': t[1], 'english': t[2]}
def F(sr, pr, use, e, **tags):
    f = {'serbian': sr, 'pronunciation': pr}; f.update(tags); f['useWhen'] = use; f['example'] = ex(e); return f
def A(sr, pr, nuance): return {'serbian': sr, 'pronunciation': pr, 'nuance': nuance}
def E(id, en, sr, pr, meaning, place, tags, register='neutral', by=(), ex_=(), forms=(), alts=(), texting=None, watch=None, hint=None, related=(), ijek=None):
    pl = P(place)
    e = {'id': id, 'english': en, 'serbian': sr, 'pronunciation': pr, 'meaning': meaning, 'category': pl[0][0], 'subcategory': pl[0][1],
         'tags': list(tags), 'register': register, 'changesBy': list(by)}
    if forms: e['forms'] = list(forms)
    if hint: e['patternHint'] = hint
    if alts: e['alternatives'] = list(alts)
    e['examples'] = list(ex_)
    if texting: e['texting'] = texting
    if ijek: e['ijekavian'] = ijek
    if watch: e['watchOut'] = watch
    e['related'] = list(related); e['verified'] = False
    e['placements'] = [{'category': c, 'subcategory': s} for c, s in pl]
    return e

NEW = [
 E('bolje', 'Better', 'Bolji / bolja / bolje', 'BOH-lyee / BOH-lyah / BOH-lyeh', 'Better, matching the thing described', 'compar;opin', ('compare', 'better', 'adjective'),
   by=('noun gender', 'describes'), hint='Masculine bolji, feminine bolja, neuter bolje. "Than" is od.',
   forms=[F('Bolji je', 'BOH-lyee yeh', 'Masculine noun, or a man', ('Taj film je bolji', 'TAH-ee FEELM yeh BOH-lyee', 'That movie is better'), nounGender='masculine'),
          F('Bolja je', 'BOH-lyah yeh', 'Feminine noun, or a woman', ('Ova kafa je bolja', 'OH-vah KAH-fah yeh BOH-lyah', 'This coffee is better'), nounGender='feminine'),
          F('Bolje je', 'BOH-lyeh yeh', 'Neuter noun, or a general "it"', ('Pivo je bolje od vina', 'PEE-vo yeh BOH-lyeh od VEE-nah', 'Beer is better than wine'), nounGender='neuter'),
          F('Bolja si', 'BOH-lyah see', 'Saying it to her', ('Ti si bolja od mene', 'TEE see BOH-lyah od MEH-neh', "You're better than me"), describes='her'),
          F('Bolji sam', 'BOH-lyee sahm', 'A man talking about himself', ('Bolji sam nego juče', 'BOH-lyee sahm NEH-go YOO-cheh', "I'm better than yesterday"), speaker='male')],
   alts=[A('Najbolji / najbolja / najbolje', 'NAI-bohl-yee / NAI-bohl-yah / NAI-bohl-yeh', 'The best'), A('Gori / gora / gore', 'GOH-ree / GOH-rah / GOH-reh', 'Worse, same endings as bolji')],
   ex_=[X('About a thing', 'Ova kafa je bolja', 'OH-vah KAH-fah yeh BOH-lyah', 'This coffee is better'), X('To her', 'Ti si bolja od mene', 'TEE see BOH-lyah od MEH-neh', "You're better than me"),
        X('About him', 'On je bolji od mene', 'OHN yeh BOH-lyee od MEH-neh', 'He is better than me'), X('About me', 'Danas sam bolje', 'DAH-nahs sahm BOH-lyeh', "I'm better today"),
        X('Plans', 'Bolje da ostanemo kod kuće', 'BOH-lyeh dah OH-stah-neh-mo kod KOO-cheh', "We'd better stay home")],
   texting='bolje', related=['nije-lose', 'dobro-lose', 'vise-nego']),
 E('vise-nego', 'More than', 'Više nego', 'VEE-sheh NEH-go', 'More than, less than', 'compar', ('compare', 'more'), alts=[A('Manje nego', 'MAH-nyeh NEH-go', 'Less than'), A('Od', 'od', 'Also "than" after a comparing word: bolji od mene')],
   ex_=[X('About me', 'Volim kafu više nego čaj', 'VOH-leem KAH-foo VEE-sheh NEH-go CHAHY', 'I like coffee more than tea'), X('To her', 'Fališ mi više nego što misliš', 'FAH-leesh mee VEE-sheh NEH-go shtoh MEE-sleesh', 'I miss you more than you think'),
        X('About her', 'Ona zna više nego ja', 'OH-nah ZNAH VEE-sheh NEH-go yah', 'She knows more than me'), X('About us', 'Radim manje nego ti', 'RAH-deem MAH-nyeh NEH-go tee', 'I work less than you'),
        X('About a thing', 'Ovo je skuplje nego juče', 'OH-vo yeh SKOOP-lyeh NEH-go YOO-cheh', "This is pricier than yesterday")],
   texting='više nego', related=['bolje', 'isto-kao']),
 E('isto-kao', 'Same as / me too', 'Isto kao', 'EE-sto KAH-oh', 'The same as; "same here"', 'compar;agree', ('compare', 'same', 'agree'), register='casual',
   alts=[A('I ja isto', 'ee yah EE-sto', 'Me too'), A('Nije isto', 'NEE-yeh EE-sto', "It's not the same")],
   ex_=[X('To her', 'Ti si isto kao tvoja mama', 'TEE see EE-sto KAH-oh TVOH-yah MAH-mah', "You're just like your mom"), X('Reply', 'I ja isto', 'ee yah EE-sto', 'Me too / same here'),
        X('About a thing', 'Nije isto', 'NEE-yeh EE-sto', "It's not the same"), X('About him', 'On je isto kao brat', 'OHN yeh EE-sto KAH-oh BRAHT', 'He is just like his brother')],
   texting='isto', related=['bolje', 'vise-nego']),
 E('levo-desno', 'Left / right / straight', 'Levo / desno / pravo', 'LEH-vo / DEH-sno / PRAH-vo', 'Left, right, straight ahead', 'dir;travel', ('directions', 'left', 'right', 'straight'),
   forms=[F('Levo', 'LEH-vo', 'Left', ('Skreni levo', 'SKREH-nee LEH-vo', 'Turn left')), F('Desno', 'DEH-sno', 'Right', ('Toalet je desno', 'toh-AH-let yeh DEH-sno', 'The toilet is on the right')),
          F('Pravo', 'PRAH-vo', 'Straight ahead', ('Idi pravo', 'EE-dee PRAH-vo', 'Go straight'))],
   alts=[A('Skreni', 'SKREH-nee', 'Turn (a command)'), A('Iza ugla', 'EE-zah OOG-lah', 'Around the corner')],
   ex_=[X('Giving directions', 'Idi pravo pa levo', 'EE-dee PRAH-vo pah LEH-vo', 'Go straight, then left'), X('Giving directions', 'Kafić je desno', 'KAH-feech yeh DEH-sno', 'The café is on the right'),
        X('Asking', 'Da li je ovo levo?', 'dah lee yeh OH-vo LEH-vo', 'Is this the left one?'), X('Taxi', 'Ovde desno, molim vas', 'OHV-deh DEH-sno MOH-leem VAHS', 'Right here, please (polite)')],
   texting='levo / desno', related=['gde-je', 'blizu-daleko'], ),
 E('gde-je', 'Where is…?', 'Gde je…? / Gde su…?', 'GDEH yeh / GDEH soo', 'Where is it? Where are they?', 'dir;q;travel', ('directions', 'question', 'where'), register='casual', by=('plural',),
   ijek='Gdje je…?', hint='"Je" for one thing, "su" for more than one.',
   forms=[F('Gde je…?', 'GDEH yeh', 'One thing or person', ('Gde je toalet?', 'GDEH yeh toh-AH-let', 'Where is the toilet?')), F('Gde su…?', 'GDEH soo', 'More than one', ('Gde su moji roditelji?', 'GDEH soo MOH-yee roh-DEE-teh-lyee', 'Where are my parents?'), nounGender='plural')],
   alts=[A('Kako da stignem do…?', 'KAH-ko dah STEEG-nem doh', 'How do I get to…?')],
   ex_=[X('Asking a stranger', 'Gde je stanica?', 'GDEH yeh STAH-nee-tsah', 'Where is the station?'), X('To her', 'Gde je tvoja mama?', 'GDEH yeh TVOH-yah MAH-mah', 'Where is your mom?'),
        X('About a group', 'Gde su svi?', 'GDEH soo SVEE', 'Where is everyone?'), X('Travel', 'Kako da stignem do aerodroma?', 'KAH-ko dah STEEG-nem doh ah-eh-ROH-droh-mah', 'How do I get to the airport?')],
   texting='gde je', related=['gde', 'levo-desno', 'gde-si']),
 E('blizu-daleko', 'Near / far', 'Blizu / daleko', 'BLEE-zoo / DAH-leh-ko', 'Close by, far away', 'dir;places', ('directions', 'near', 'far'),
   ex_=[X('Asking', 'Da li je daleko?', 'dah lee yeh DAH-leh-ko', 'Is it far?'), X('Answering', 'Nije daleko', 'NEE-yeh DAH-leh-ko', "It's not far"), X('About a place', 'Aerodrom je daleko', 'ah-eh-ROH-drohm yeh DAH-leh-ko', 'The airport is far'),
        X('About me', 'Stan je blizu', 'STAHN yeh BLEE-zoo', 'The apartment is close by'), X('To her', 'Živiš li blizu?', 'ZHEE-veesh lee BLEE-zoo', 'Do you live nearby?')],
   texting='blizu / daleko', related=['gde-je', 'levo-desno']),
 E('ovaj-taj', 'This / that', 'Ovaj / taj / onaj', 'OH-vai / TAH-ee / OH-nai', 'This (near me), that (near you), that over there', 'this', ('this', 'that', 'demonstrative'), by=('noun gender',),
   hint='Each one has three forms: masculine (-j), feminine (-a), neuter (-o): ovaj/ova/ovo, taj/ta/to, onaj/ona/ono.',
   forms=[F('Ovaj / ova / ovo', 'OH-vai / OH-vah / OH-vo', 'This: close to me', ('Ova kafa je odlična', 'OH-vah KAH-fah yeh od-LEECH-nah', 'This coffee is excellent'), nounGender='all three'),
          F('Taj / ta / to', 'TAH-ee / TAH / TOH', 'That: close to you, or just mentioned', ('Ta pesma je ludilo', 'TAH PEH-smah yeh LOO-dee-lo', 'That song is crazy'), nounGender='all three'),
          F('Onaj / ona / ono', 'OH-nai / OH-nah / OH-no', 'That one over there, far from both of us', ('Onaj tip je smešan', 'OH-nai TEEP yeh SMEH-shahn', 'That guy over there is funny'), nounGender='all three'),
          F('Ovo', 'OH-vo', 'This, about a general thing', ('Ovo je sve', 'OH-vo yeh SVEH', 'This is everything'), nounGender='neuter'),
          F('To', 'TOH', 'That / it: the all-purpose one', ('To je istina', 'TOH yeh EE-stee-nah', "That's the truth"), nounGender='neuter')],
   ex_=[X('About a thing', 'Ovaj telefon je skup', 'OH-vai TEH-leh-fon yeh SKOOP', 'This phone is expensive'), X('To her', 'Taj film je dobar', 'TAH-ee FEELM yeh DOH-bahr', 'That movie is good'),
        X('About someone', 'Ona haljina je prelepa', 'OH-nah HAHL-yee-nah yeh preh-LEH-pah', 'That dress over there is gorgeous'), X('Reaction', 'To je sve', 'TOH yeh SVEH', "That's all")],
   texting='ovo / to / ono', related=['ovde-tamo', 'koji']),
 E('ovde-tamo', 'Here / there', 'Ovde / tu / tamo', 'OHV-deh / TOO / TAH-mo', 'Here, right there, over there', 'this;dir', ('this', 'here', 'there', 'place'), ijek='Ovdje',
   forms=[F('Ovde', 'OHV-deh', 'Here, where I am', ('Ja sam ovde', 'YAH sahm OHV-deh', "I'm here")), F('Tu', 'TOO', 'Right here / right there, close by', ('Tu sam', 'TOO sahm', "I'm right here")), F('Tamo', 'TAH-mo', 'Over there, far away', ('Tamo je kafić', 'TAH-mo yeh KAH-feech', "There's a café over there"))],
   ex_=[X('To her', 'Dođi ovde', 'DOH-jee OHV-deh', 'Come here'), X('About me', 'Čekam te tamo', 'CHEH-kahm teh TAH-mo', "I'll wait for you there"), X('Reassuring', 'Nisi sama, tu sam', 'NEE-see SAH-mah TOO sahm', "You're not alone, I'm here"),
        X('About a thing', 'Ključevi su tamo', 'KLYOO-cheh-vee soo TAH-mo', 'The keys are over there')],
   texting='ovde / tamo', related=['ovaj-taj', 'gde-je']),
 E('boje', 'Colors', 'Crvena, plava, zelena, žuta, bela, crna', 'TSUR-veh-nah, PLAH-vah, zeh-LEH-nah, ZHOO-tah, BEH-lah, TSUR-nah', 'The basic colors', 'colors', ('colors', 'adjective'), by=('noun gender', 'plural'),
   ijek='bijela', hint='Colors match the noun: crven (m.), crvena (f.), crveno (n.). Same pattern for plava, zelena, žuta, bela, crna.',
   forms=[F('Crven / plav / zelen', 'TSUR-ven / PLAHV / ZEH-len', 'Masculine noun', ('Auto je crven', 'OW-toh yeh TSUR-ven', 'The car is red'), nounGender='masculine'),
          F('Crvena / plava / zelena', 'TSUR-veh-nah / PLAH-vah / zeh-LEH-nah', 'Feminine noun', ('Tvoja haljina je plava', 'TVOH-yah HAHL-yee-nah yeh PLAH-vah', 'Your dress is blue'), nounGender='feminine'),
          F('Crveno / plavo / zeleno', 'TSUR-veh-no / PLAH-vo / zeh-LEH-no', 'Neuter noun', ('Srce je crveno', 'SUHR-tseh yeh TSUR-veh-no', 'The heart is red'), nounGender='neuter'),
          F('Crvene / plave', 'TSUR-veh-neh / PLAH-veh', 'Several feminine things', ('Cipele su crvene', 'TSEE-peh-leh soo TSUR-veh-neh', 'The shoes are red'), nounGender='feminine plural')],
   alts=[A('Žuta / žut / žuto', 'ZHOO-tah / ZHOOT / ZHOO-to', 'Yellow'), A('Bela / beo / belo', 'BEH-lah / BEH-oh / BEH-lo', 'White'), A('Crna / crn / crno', 'TSUR-nah / TSURN / TSUR-no', 'Black'),
         A('Siva / siv / sivo', 'SEE-vah / SEEV / SEE-vo', 'Gray'), A('Roze', 'ROH-zeh', 'Pink: never changes')],
   ex_=[X('About a thing', 'Auto je crn', 'OW-toh yeh TSURN', 'The car is black'), X('To her', 'Volim tvoju žutu haljinu', 'VOH-leem TVOH-yoo ZHOO-too HAHL-yee-noo', 'I love your yellow dress'),
        X('About a drink', 'Vino je belo', 'VEE-no yeh BEH-lo', 'The wine is white'), X('Shopping', 'Imate li to u zelenoj?', 'EE-mah-teh lee toh oo zeh-LEH-noy', 'Do you have this in green?')],
   texting='boje', related=['ovaj-taj']),
 E('veliko-malo', 'Big / small', 'Veliki / mali', 'VEH-lee-kee / MAH-lee', 'Big, small', 'shapes;things', ('size', 'big', 'small', 'adjective'), by=('noun gender',),
   hint='Veliki, velika, veliko / mali, mala, malo. Careful: "malo" is also "a little".',
   forms=[F('Veliki / mali', 'VEH-lee-kee / MAH-lee', 'Masculine noun', ('Grad je veliki', 'GRAHD yeh VEH-lee-kee', 'The city is big'), nounGender='masculine'),
          F('Velika / mala', 'VEH-lee-kah / MAH-lah', 'Feminine noun', ('Kuća je velika', 'KOO-chah yeh VEH-lee-kah', 'The house is big'), nounGender='feminine'),
          F('Veliko / malo', 'VEH-lee-ko / MAH-lo', 'Neuter noun', ('Selo je malo', 'SEH-lo yeh MAH-lo', 'The village is small'), nounGender='neuter')],
   alts=[A('Ogroman', 'oh-GROH-mahn', 'Huge'), A('Mali / mala', 'MAH-lee / MAH-lah', 'Also a sweet way to call someone small: "mala" for a girl')],
   ex_=[X('About a thing', 'Stan je mali', 'STAHN yeh MAH-lee', 'The apartment is small'), X('About a place', 'Kafić je pun, ali nije veliki', 'KAH-feech yeh POON AH-lee NEE-yeh VEH-lee-kee', "The café is full but it's not big"),
        X('About me', 'Imam veliku porodicu', 'EE-mahm VEH-lee-koo poh-roh-DEE-tsoo', 'I have a big family'), X('Cute', 'Moja mala', 'MOH-yah MAH-lah', 'My little one (to her, playful)')],
   texting='veliko / malo', related=['boje', 'oblici']),
 E('oblici', 'Shapes', 'Krug, kvadrat, trougao', 'KROOG, KVAH-draht, TROH-oo-gah-oh', 'Basic shapes', 'shapes', ('shapes', 'noun'), by=('noun gender',),
   alts=[A('Srce', 'SUHR-tseh', 'Heart'), A('Linija', 'LEE-nee-yah', 'Line'), A('Okrugao / okrugla', 'OH-kroo-gah-oh / OH-krooglah', 'Round (m. / f.)')],
   ex_=[X('About a thing', 'Ovo je krug', 'OH-vo yeh KROOG', 'This is a circle'), X('About a thing', 'Torta je okrugla', 'TOHR-tah yeh OH-kroog-lah', 'The cake is round'),
        X('Sweet', 'Nacrtala sam srce', 'nah-TSUR-tah-lah sahm SUHR-tseh', 'I drew a heart'), X('About a thing', 'Ovo je kvadrat', 'OH-vo yeh KVAH-draht', 'This is a square')],
   texting='oblici', related=['veliko-malo', 'boje']),
 E('u-na', 'In / on / at', 'U / na', 'OO / NAH', 'In, on, at, to', 'prep;places', ('preposition', 'place', 'in', 'on'),
   hint='"U" for inside things and cities. "Na" for surfaces, events, open spaces and many "at" places (na poslu, na stanici).',
   forms=[F('U (+ place)', 'OO', 'Inside something, a city or a country', ('Ja sam u kafiću', 'YAH sahm oo KAH-fee-choo', "I'm in the café")), F('Na (+ place / event)', 'NAH', 'On something, at an event, a station, at work', ('Čekam te na stanici', 'CHEH-kahm teh nah STAH-nee-tsee', "I'm waiting for you at the station")),
          F('U / na (+ time)', 'OO / NAH', 'Time words: u petak is "on Friday"', ('Vidimo se u petak', 'VEE-dee-mo seh oo PEH-tahk', 'See you on Friday'))],
   ex_=[X('About me', 'Živim u Kanadi', 'ZHEE-veem oo KAH-nah-dee', 'I live in Canada'), X('To her', 'Gde si, na poslu?', 'GDEH see nah POH-sloo', 'Where are you, at work?'),
        X('About him', 'On radi u banci', 'OHN RAH-dee oo BAHN-tsee', 'He works at a bank'), X('About us', 'Idemo na žurku', 'EE-deh-mo nah ZHOOR-koo', "We're going to a party")],
   texting='u / na', related=['sa-bez', 'za-od']),
 E('sa-bez', 'With / without', 'Sa / bez', 'SAH / BEZ', 'With, without', 'prep', ('preposition', 'with', 'without'),
   forms=[F('Sa (+ person)', 'SAH', 'With someone (the word after changes a little: sa mnom, sa tobom)', ('Idem sa tobom', 'EE-dem sah TOH-bom', "I'm going with you")), F('Bez (+ thing)', 'BEZ', 'Without something', ('Kafa bez šećera', 'KAH-fah bez SHEH-cheh-rah', 'Coffee without sugar'))],
   ex_=[X('To her', 'Hoćeš li sa mnom?', 'HOH-chesh lee sah MNOHM', 'Do you want to come with me?'), X('About me', 'Ne mogu bez tebe', 'NEH MOH-goo bez TEH-beh', "I can't do without you"),
        X('About a drink', 'Pijem vodu bez gasa', 'PEE-yem VOH-doo bez GAH-sah', 'I drink still water'), X('About her', 'Ona je sa prijateljicom', 'OH-nah yeh sah pree-yah-teh-LYEE-tsom', "She's with a friend")],
   texting='sa / bez', related=['u-na', 'za-od']),
 E('za-od', 'For / from', 'Za / od / iz', 'ZAH / OD / EEZ', 'For, from, out of', 'prep', ('preposition', 'for', 'from'),
   forms=[F('Za', 'ZAH', 'For someone or something', ('Cveće je za tebe', 'TSVEH-cheh yeh zah TEH-beh', 'The flowers are for you')), F('Od', 'OD', 'From a person, or "than" after a comparison', ('Poruka od mame', 'POH-roo-kah od MAH-meh', 'A message from mom')),
          F('Iz', 'EEZ', 'From a place (where you come from)', ('Ja sam iz Kanade', 'YAH sahm eez KAH-nah-deh', "I'm from Canada"))],
   ex_=[X('Small talk', 'Ja sam iz Kanade', 'YAH sahm eez KAH-nah-deh', "I'm from Canada"), X('Thanks', 'Hvala za sve', 'HVAH-lah zah SVEH', 'Thanks for everything'),
        X('About a thing', 'Ovo je od mame', 'OH-vo yeh od MAH-meh', 'This is from mom'), X('About a thing', 'Ovo je za tebe', 'OH-vo yeh zah TEH-beh', 'This is for you')],
   texting='za / od / iz', related=['u-na', 'sa-bez', 'odakle-si']),
 E('dobar-dan', 'Good day (polite hello)', 'Dobar dan', 'DOH-bahr DAHN', 'The polite daytime hello', 'elders;gb;formal', ('greeting', 'polite', 'elders'),
   alts=[A('Dobro jutro', 'DOH-bro YOO-tro', 'Good morning'), A('Dobro veče', 'DOH-bro VEH-cheh', 'Good evening')],
   ex_=[X('To an elder', 'Dobar dan, kako ste?', 'DOH-bahr DAHN KAH-ko steh', 'Good day, how are you?'), X('To her dad', 'Dobar dan, gospodine', 'DOH-bahr DAHN GOH-spoh-dee-neh', 'Good day, sir'),
        X('To her mom', 'Dobar dan, gospođo', 'DOH-bahr DAHN GOH-spoh-jo', 'Good day, madam'), X('To a group', 'Dobar dan svima', 'DOH-bahr DAHN SVEE-mah', 'Good day, everyone')],
   texting='dobar dan', watch='With friends use "zdravo" or "ćao". "Dobar dan" is for elders, shops, offices and people you don\'t know.', related=['hello', 'dobro-vece', 'kako-ste']),
 E('kako-ste', 'How are you? (polite)', 'Kako ste?', 'KAH-ko steh', 'How are you, to someone older or a stranger', 'elders;formal;starters', ('greeting', 'polite', 'elders', 'question'), by=('formal',),
   forms=[F('Kako si?', 'KAH-ko see', 'Casual: friends, her', ('Kako si, lepotice?', 'KAH-ko see leh-poh-TEE-tseh', 'How are you, beautiful?')), F('Kako ste?', 'KAH-ko steh', 'Polite: elders, strangers, several people', ('Kako ste, gospođo?', 'KAH-ko steh GOH-spoh-jo', 'How are you, madam?'), formal='polite')],
   ex_=[X('To her mom', 'Kako ste vi?', 'KAH-ko steh VEE', 'And how are you?'), X('Morning visit', 'Kako ste spavali?', 'KAH-ko steh SPAH-vah-lee', 'How did you sleep?'), X('Reply', 'Dobro sam, hvala. A vi?', 'DOH-bro sahm HVAH-lah. ah VEE', "I'm good, thanks. And you?"),
        X('To a group', 'Kako ste, momci?', 'KAH-ko steh MOHM-tsee', 'How are you, guys?')],
   texting='kako ste', related=['kako-si', 'dobar-dan', 'ti-vi']),
 E('dovidjenja', 'Goodbye (polite)', 'Doviđenja', 'doh-VEE-jen-yah', 'Goodbye, literally "until we see each other"', 'elders;gb;formal', ('goodbye', 'polite', 'elders'),
   alts=[A('Vidimo se', 'VEE-dee-mo seh', 'See you: friendly, casual'), A('Ćao', 'CHOW', 'Bye: casual')],
   ex_=[X('To an elder', 'Doviđenja, gospodine', 'doh-VEE-jen-yah GOH-spoh-dee-neh', 'Goodbye, sir'), X('Thanking', 'Doviđenja i hvala', 'doh-VEE-jen-yah ee HVAH-lah', 'Goodbye and thank you'),
        X('To a group', 'Doviđenja svima', 'doh-VEE-jen-yah SVEE-mah', 'Goodbye, everyone'), X('Friendly', 'Doviđenja, vidimo se', 'doh-VEE-jen-yah VEE-dee-mo seh', 'Goodbye, see you')],
   texting='doviđenja', related=['see-you', 'cao', 'dobar-dan']),
]
if __name__ == '__main__':
    data = json.load(open('src/data/entries.json')); have = {e['id'] for e in data}; added = 0
    for e in NEW:
        if e['id'] in have: continue
        data.append(e); added += 1
    ids = [e['id'] for e in data]
    for e in NEW:
        for r in e['related']: assert r in ids, (e['id'], r)
    json.dump(data, open('src/data/entries.json', 'w'), ensure_ascii=False, indent=2)
    print('added', added, 'total', len(data))
