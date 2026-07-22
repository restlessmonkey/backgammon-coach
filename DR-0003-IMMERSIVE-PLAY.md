# DR-0003 — Immersive Play

## Status
Implemented in v1.8.2.

## Decision
Treat the board as the primary application surface. On compact layouts, controls and coaching must overlay, collapse, or move out of the way rather than force the player to scroll away from the board.

## Consequences
- The title collapses after play begins.
- The Coach panel becomes a fixed bottom drawer on compact layouts.
- Larger layouts retain a persistent side Coach panel.
- Roll Dice becomes a large primary action and can optionally float at a user-chosen position.
- Handedness, lock, reset, and focus preferences are stored locally.

## Safety
No backgammon rule-engine logic was intentionally changed. v1.8 rules regression tests remain in the application and identify themselves as v1.8.2.
