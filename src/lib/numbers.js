// Serbian numbers (ekavian). Each row: [digits, serbian, pronunciation].
const UNITS = [
  ['jedan', 'YEH-dahn'], ['dva', 'DVAH'], ['tri', 'TREE'], ['četiri', 'CHEH-tee-ree'], ['pet', 'PEHT'],
  ['šest', 'SHEHST'], ['sedam', 'SEH-dahm'], ['osam', 'OH-sahm'], ['devet', 'DEH-veht'],
]
const TEENS = [
  ['deset', 'DEH-seht'], ['jedanaest', 'yeh-DAH-nah-est'], ['dvanaest', 'DVAH-nah-est'], ['trinaest', 'TREE-nah-est'],
  ['četrnaest', 'CHEH-tur-nah-est'], ['petnaest', 'PEHT-nah-est'], ['šesnaest', 'SHEHS-nah-est'],
  ['sedamnaest', 'SEH-dahm-nah-est'], ['osamnaest', 'OH-sahm-nah-est'], ['devetnaest', 'DEH-veht-nah-est'],
]
const TENS = [
  ['dvadeset', 'DVAH-deh-seht'], ['trideset', 'TREE-deh-seht'], ['četrdeset', 'CHEH-tur-deh-seht'], ['pedeset', 'PEH-deh-seht'],
  ['šezdeset', 'SHEZ-deh-seht'], ['sedamdeset', 'SEH-dahm-deh-seht'], ['osamdeset', 'OH-sahm-deh-seht'], ['devedeset', 'DEH-veh-deh-seht'],
]

export const NUMBERS = []
for (let n = 1; n <= 100; n++) {
  let w
  if (n < 10) w = UNITS[n - 1]
  else if (n < 20) w = TEENS[n - 10]
  else if (n === 100) w = ['sto', 'STOH']
  else {
    const t = TENS[Math.floor(n / 10) - 2], u = n % 10 ? UNITS[(n % 10) - 1] : null
    w = u ? [`${t[0]} ${u[0]}`, `${t[1]} ${u[1]}`] : t
  }
  NUMBERS.push([n, ...w])
}
export const BIG_NUMBERS = [
  [1000, 'hiljadu', 'HEEL-yah-doo', 'Also "jedna hiljada". Used for prices: hiljadu dinara'],
  [10000, 'deset hiljada', 'DEH-seht HEEL-yah-dah', ''],
  [100000, 'sto hiljada', 'STOH HEEL-yah-dah', ''],
  [1000000, 'milion', 'MEE-lee-on', 'Also "jedan milion"'],
]
