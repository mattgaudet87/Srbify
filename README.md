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

- [x] Phase 1: foundation (starter entries, Home / Category / Entry pages, search)
- [x] Phase 2: variation system (highlighting, Settings, vulgar toggle)
- [x] Phase 3: phone polish (copy buttons, favorites, installable, offline)
- [x] Phase 4: content for all 14 categories (179 entries, every subcategory filled)
  - [ ] Native-speaker verification: set `"verified": true` per entry as it is checked

### Verifying entries

After a native speaker checks an entry, set `"verified": true` on it in `src/data/entries.json` (or ask Claude Code to). The checkmark badge updates automatically.
