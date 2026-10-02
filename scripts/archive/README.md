# Archive

One-shot scripts that built the first content batches and are already applied to `src/data/entries.json`. Kept as
history only. They expect to run from `scripts/` (before they were moved) and `apply.py` rebuilds from git HEAD, so
don't run them against the current data. To change content now, edit `entries.json` directly or write a small
idempotent script like `../sweep_fixes.py`, then run the checks listed in `CLAUDE.md`.
