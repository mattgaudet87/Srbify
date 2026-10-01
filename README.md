# Srbify

A personal, mobile-first Serbian phrasebook for texting. Full spec in [PLAN.md](PLAN.md).

**Stack:** React + Vite, Fuse.js search, all content in `src/data/entries.json`. Static site, deployed on Vercel.

## Run locally

```bash
npm install
npm run dev
```

## Adding entries

Add objects to `src/data/entries.json` following section 5 of the plan. New entries show up in categories and search automatically. Every entry starts with `"verified": false`.

## Status

- [x] Phase 1: foundation (49 starter entries, Home / Category / Entry pages, search)
- [ ] Phase 2: variation system (highlighting, Settings, vulgar toggle)
- [ ] Phase 3: phone polish (copy buttons, favorites, recents, installable, offline)
- [ ] Phase 4: content batches and native-speaker verification
