import json,sys
d=json.load(open('src/data/entries.json'))
ids=sys.argv[1:]
for e in d:
    if e['id'] in ids or e['category'] in ids:
        print(e['id'],'|',e['serbian'],'|',e['english'],'|',e['meaning'],'| watch:',e.get('watchOut','')[:90])
        for x in e.get('examples',[]): print('   ex:',x['serbian'],'|',x['pronunciation'],'|',x['english'])
