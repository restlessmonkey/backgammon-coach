# Changelog

## v1.7 — Hint Foundation
- Added `Rank my moves` to enumerate and rank complete legal move sequences.
- Shows up to three choices: best move, strong alternative, and another legal choice.
- Added standard-style move notation such as `13/7 8/5`, `bar/22`, and `6/off`.
- Added short explanations based on hits, made points, home-board strength, primes, blot changes, back-checker escape, racing efficiency, and bearing off.
- Added source-and-destination highlighting for a selected hint.
- Added an explicit notice that v1.7 uses a local teaching heuristic rather than embedded GNU Backgammon analysis.
- Added project backlog, changelog, release checklist, and design record.

## v1.6 — Core Game Stabilization
- Stabilized human/computer turn transition.
- Added human-only Undo.
- Moved status away from board pips.
- Added legal-sequence rules tests and compact version display.
