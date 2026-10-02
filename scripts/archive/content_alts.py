"""Alternatives promoted to their own entries (svakako, lepo spavaj, evo, jako, puno, molim).
Reuses the E/F helpers from archive/content_sweep.py. Idempotent."""
import os, sys
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
sys.path.insert(0, os.path.join(root, 'scripts', 'archive')); import content_sweep as c
os.chdir(root)
E, F = c.E, c.F
NEW = []; add = NEW.append

add(E('svakako', 'Certainly / by all means', 'Svakako', 'SVAH-kah-ko', 'Certainly; by all means; for sure',
  [('QP', 'Agree and disagree'), ('QP', 'Common replies')], ['sure', 'certain', 'polite'], 'neutral',
  [('To her', 'Svakako dođi, svi te čekamo', 'SVAH-kah-ko DOH-jee, SVEE teh CHEH-kah-mo', "By all means come, we're all waiting for you"),
   ('Polite yes', 'Svakako, izvolite', 'SVAH-kah-ko, EEZ-vo-lee-teh', 'Certainly, go ahead'),
   ('About me', 'Svakako ću doći', 'SVAH-kah-ko choo DOH-chee', "I'll certainly come"),
   ('About us', 'Svakako ćemo vam javiti', 'SVAH-kah-ko CHEH-mo vahm YAH-vee-tee', "We'll certainly let you know")],
  alts=[('Sigurno', 'SEE-goor-no', 'Definitely; a bit more everyday'), ('Naravno', 'nah-RAHV-no', 'Of course'), ('Apsolutno', 'ahp-soh-LOOT-no', 'Absolutely')],
  rel=['sigurno', 'naravno', 'moze', 'izvolite']))

add(E('lepo-spavaj', 'Sleep well', 'Lepo spavaj', 'LEH-po SPAH-vai', 'Sleep well; have a good sleep',
  [('FR', 'Good morning and good night'), ('QP', 'Greetings and goodbyes')], ['sleep', 'night', 'sweet'], 'casual',
  [('To her', 'Lepo spavaj, lepotice', 'LEH-po SPAH-vai, leh-poh-TEE-tseh', 'Sleep well, beautiful'),
   ('Late text', 'Lepo spavaj i javi mi se ujutru', 'LEH-po SPAH-vai ee YAH-vee mee seh oo-YOO-troo', 'Sleep well and text me in the morning'),
   ('Her reply', 'Lepo spavaj i ti', 'LEH-po SPAH-vai ee TEE', 'Sleep well, you too')],
  forms=[F('Lepo spavaj', 'LEH-po SPAH-vai', 'To one friend or someone your age', ('Lepo spavaj, vidimo se sutra', 'LEH-po SPAH-vai, VEE-dee-mo seh SOO-trah', 'Sleep well, see you tomorrow'), formal='casual'),
         F('Lepo spavajte', 'LEH-po SPAH-vai-teh', 'To an elder, a stranger, or a group', ('Lepo spavajte, laku noć', 'LEH-po SPAH-vai-teh, LAH-koo NOHCH', 'Sleep well, good night'), formal='polite')],
  ij='Lijepo spavaj', rel=['laku-noc', 'laku-noc-lepotice', 'slatkih-snova', 'spavaj']))

add(E('evo', 'Here (it is)', 'Evo', 'EH-vo', 'Here it is; here I come; here we are',
  [('QP', 'Filler and transition words'), ('QP', 'Common replies')], ['here', 'handing over', 'arriving'], 'casual',
  [('Coming', 'Evo me, stižem!', 'EH-vo meh, STEE-zhem', "Here I am, I'm coming!"),
   ('Handing over', 'Evo ti telefon', 'EH-vo tee TEH-leh-fon', "Here's your phone"),
   ('Spotting him', 'Evo ga!', 'EH-vo gah', 'Here he is!')],
  forms=[F('Evo me', 'EH-vo meh', 'Me', ('Evo me, čekaj još malo', 'EH-vo meh, CHEH-kai yohsh MAH-lo', "Here I come, wait a little longer"), describes='me'),
         F('Evo ga', 'EH-vo gah', 'Him / it', ('Evo ga, stigao je', 'EH-vo gah, STEE-gah-oh yeh', 'Here he is, he has arrived'), describes='him'),
         F('Evo je', 'EH-vo yeh', 'Her', ('Evo je, dolazi', 'EH-vo yeh, DOH-lah-zee', 'Here she is, she is coming'), describes='her'),
         F('Evo nas', 'EH-vo nahs', 'Us', ('Evo nas, otvori vrata', 'EH-vo nahs, OHT-voh-ree VRAH-tah', 'Here we are, open the door'), describes='us')],
  alts=[('Eto', 'EH-to', 'There; there you go (about something near you or just done)')],
  rel=['eto', 'izvolite', 'stigao-sam', 'stizem-za-pet']))

add(E('jako', 'Very / strongly', 'Jako', 'YAH-ko', 'Very, really, strongly',
  [('BA', 'Flow words'), ('FR', 'Flirting')], ['very', 'emphasis', 'intensifier'], 'casual',
  [('To her', 'Jako mi se sviđaš', 'YAH-ko mee seh SVEE-jahsh', 'I like you a lot'),
   ('Missing her', 'Jako mi fališ', 'YAH-ko mee FAH-leesh', 'I miss you a lot'),
   ('About me (man)', 'Jako sam umoran', 'YAH-ko sahm OO-mo-rahn', "I'm very tired (a man says this)"),
   ('About me (woman)', 'Jako sam umorna', 'YAH-ko sahm OO-mor-nah', "I'm very tired (a woman says this)"),
   ('A thing', 'Jako lepo', 'YAH-ko LEH-po', 'Really nice')],
  alts=[('Mnogo', 'MNOH-go', 'A lot, very'), ('Baš', 'BAHSH', 'Really'), ('Puno', 'POO-no', 'A lot')],
  rel=['mnogo', 'bas', 'puno', 'svidjas-mi-se']))

add(E('puno', 'A lot / much', 'Puno', 'POO-no', 'A lot, much, many',
  [('BA', 'Flow words'), ('QP', 'Thanks, sorry, please')], ['a lot', 'many', 'amount'], 'neutral',
  [('Thanks', 'Puno ti hvala', 'POO-no tee HVAH-lah', 'Thanks a lot'),
   ('Sign-off', 'Puno pozdrava', 'POO-no POHZ-drah-vah', 'Lots of love / best wishes'),
   ('About me', 'Puno radim ovih dana', 'POO-no RAH-deem OH-veeh DAH-nah', "I'm working a lot these days"),
   ('Many people', 'Puno ljudi je došlo', 'POO-no LYOO-dee yeh DOHSH-lo', 'A lot of people came')],
  alts=[('Mnogo', 'MNOH-go', 'A lot, very'), ('Jako', 'YAH-ko', 'Very, strongly')],
  rel=['mnogo', 'jako', 'hvala-puno', 'vise-nego']))

add(E('molim', 'Pardon? / Can I help you?', 'Molim?', 'MOH-leem', 'Pardon? Can I help you? You are welcome',
  [('QP', 'Common replies'), ('QP', 'Thanks, sorry, please')], ['pardon', 'shop', 'polite'], 'neutral',
  [('Not hearing (man)', 'Molim? Nisam čuo', 'MOH-leem? NEE-sahm CHOO-oh', "Pardon? I didn't hear (a man says this)"),
   ('Not hearing (woman)', 'Molim? Nisam čula', 'MOH-leem? NEE-sahm CHOO-lah', "Pardon? I didn't hear (a woman says this)"),
   ('In a shop', 'Izvolite, molim vas?', 'EEZ-vo-lee-teh, MOH-leem vahs', 'Yes, how can I help you?'),
   ('You are welcome', 'Molim, nema problema', 'MOH-leem, NEH-mah proh-BLEH-mah', "You're welcome, no problem")],
  alts=[('Molim te', 'MOH-leem teh', 'Please (to a friend)'), ('Šta?', 'SHTAH', 'What? (very casual)'), ('Izvolite?', 'EEZ-vo-lee-teh', 'Yes? / how can I help? (polite)')],
  watch='"Molim?" with a rising tone means "pardon?". "Molim" said to thank-you means "you\'re welcome". Say "Šta?" only to friends, it can sound rude.',
  rel=['please', 'ponovi', 'izvolite', 'nema-na-cemu']))

if __name__ == '__main__':
    c.NEW = NEW
    print('added', len(c.merge()), 'entries')
