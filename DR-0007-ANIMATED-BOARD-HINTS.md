# DR-0007 — Animated Board Hints

## Status
Implemented in v1.9.1.

## Decision
The best ranked legal sequence is shown spatially on the board, because users should not have to translate notation into geometry before they can learn from a recommendation.

## Behavior
- Highlight the source checker.
- Highlight the destination.
- Draw a curved dashed route.
- Animate a ghost checker along that route.
- Display the die value on the moving checker.
- Repeat for each step in a complete turn.
- Never mutate the real board during preview.
- Allow immediate cancellation.
