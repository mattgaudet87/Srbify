"""Merge scripts/patches/*.py into src/data/entries.json (always starts from git HEAD's copy).
Patch keys per id: ctx0 (label(s) for existing examples), add (new examples), fx (example per existing form, in order),
forms_add (new forms appended), forms (full replacement), changesBy (override)."""
import json, glob, subprocess, importlib.util, sys, os
os.chdir(os.path.join(os.path.dirname(__file__), '..'))
base = subprocess.check_output(['git', 'show', 'HEAD:src/data/entries.json']).decode()
data = json.loads(base)
by = {e['id']: e for e in data}

def X(ctx, sr, pr, en): return {'context': ctx, 'serbian': sr, 'pronunciation': pr, 'english': en}
def ex(t): return {'serbian': t[0], 'pronunciation': t[1], 'english': t[2]}
def F(sr, pr, use, e, **tags):
    f = {'serbian': sr, 'pronunciation': pr}; f.update(tags); f['useWhen'] = use; f['example'] = ex(e); return f

patches = {}
for p in sorted(glob.glob('scripts/patches/*.py')):
    spec = importlib.util.spec_from_file_location('p', p); m = importlib.util.module_from_spec(spec)
    m.X, m.F = X, F; spec.loader.exec_module(m)
    for k, v in m.P.items():
        assert k in by, f'unknown id {k}'; assert k not in patches, f'dup {k}'; patches[k] = v

for k, v in patches.items():
    e = by[k]
    old = e.get('examples', [])
    c0 = v.get('ctx0', [])
    if isinstance(c0, str): c0 = [c0]
    for i, c in enumerate(c0): old[i]['context'] = c
    e['examples'] = old + v.get('add', [])
    if 'forms' in v: e['forms'] = v['forms']
    if 'fx' in v:
        assert len(v['fx']) == len(e['forms']), f'{k}: fx count'
        for f, t in zip(e['forms'], v['fx']):
            if t: f['example'] = ex(t)
    if 'forms_add' in v: e['forms'] = e.get('forms', []) + v['forms_add']
    if 'changesBy' in v: e['changesBy'] = v['changesBy']

json.dump(data, open('src/data/entries.json', 'w'), ensure_ascii=False, indent=2)
open('src/data/entries.json', 'a').write('\n')
bad = [(e['id'], len(e.get('examples', []))) for e in data if len(e.get('examples', [])) < 3]
nof = [(e['id'], f['serbian']) for e in data for f in e.get('forms', []) if 'example' not in f]
print(f'patched {len(patches)}/{len(data)}; <3 examples: {len(bad)}; forms w/o example: {len(nof)}')
if '-v' in sys.argv: print(bad); print(nof)
