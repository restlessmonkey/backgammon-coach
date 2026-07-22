# DR-0005 — Victory Celebration Test Control

## Decision
Expose a one-tap test control in Play experience that invokes the production victory celebration function directly.

## Rationale
Waiting to win a full game makes visual validation slow and discourages repeated testing of randomized finales.

## Safety boundary
The test control calls only `startVictoryCelebration()`. It does not modify board state, dice, turn ownership, score, move history, or win detection.

## User control
The existing Stop celebration button and Escape-key handler stop the animation at any time.
