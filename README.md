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
- [x] Phase 4: content for all categories (every subcategory filled)
- [x] Phase 5: intent-based categories ("what am I trying to say?"), tags, tap-any-word cards (`src/data/words.json`)
  - [ ] Native-speaker verification: set `"verified": true` per entry as it is checked

### Verifying entries

After a native speaker checks an entry, set `"verified": true` on it in `src/data/entries.json` (or ask Claude Code to). The checkmark badge updates automatically.

## Content rule: examples
Every entry needs 3+ example sentences. Wherever a word changes with context (me / you / someone else / a thing, male vs female, casual vs polite, singular vs plural), each form row in `forms[]` carries its own `example` (`{serbian, pronunciation, english}`) and entry-level `examples[]` carry a `context` label.

## Content pipeline (scripts/)

Entries and the word glossary are generated/checked by small Python scripts:

- `remap.py` is the one-time re-map of the original 179 entries onto the intent-based categories (adds `placements`, so one entry can live in several categories).
- `new_entries.py` adds entries for subcategories that were empty.
- `glossary/*.txt` holds a hand-written card for every Serbian word (`word|meaning|note|tags`); pronunciations come from the app's own sentences (`glossary/pron.json`).
- `build_words.py` builds `src/data/words.json`; `check_words.py` fails if any word in any sentence has no card. Run both after adding an entry.
