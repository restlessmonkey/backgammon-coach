# DR-0008 — Watch the Coach Think

## Status
Implemented in v1.9.2.

## Purpose
Teach decision-making rather than only reveal the answer.

## Sequence
1. Rank complete legal turns.
2. Display up to three candidates.
3. Highlight each candidate on the board.
4. Explain the strategic effect.
5. Reject weaker candidates with concrete reasons.
6. Select the strongest candidate.
7. Animate the final recommendation.

## Boundary
This is a transparent local teaching heuristic, not engine-grade equity analysis.
All previews operate on cloned state and do not mutate the real game.
