# Advanced Local Coach Architecture — v2.0.1.1

## Status

Implemented. This is an offline strength upgrade, not a grandmaster certification.

## Problem corrected

The previous local evaluator primarily judged the board immediately after the coach's own move. That creates shallow recommendations: a move can look attractive before considering whether the opponent can hit, escape, make a key point, or destroy the resulting structure.

## New analysis pipeline

1. Generate every legal complete turn.
2. Apply an advanced static evaluation.
3. Keep the strongest 10 candidates, or 6 for doubles.
4. For each retained candidate, examine all 21 distinct opponent dice combinations.
5. For each roll, generate the opponent's legal complete turns and select its strongest reply.
6. Evaluate the resulting position from the original player's perspective.
7. Weight non-double rolls twice and doubles once, reproducing all 36 dice outcomes.
8. Blend immediate value and expected post-reply value.
9. Rank moves using the reply-adjusted score.

## Added strategic knowledge

- Standard non-double opening book.
- Race-versus-contact classification.
- Pip-count weighting appropriate to race positions.
- Key-point values, especially the 5-point, bar point, anchors, and home-board points.
- Prime length and prime strength.
- Advanced-anchor value.
- Blot exposure estimates.
- Home-board-dependent hit value.
- Stack and distribution penalties.
- Back-checker escape value.
- Bear-off wastage and gaps.
- Strategy adjustment when leading or trailing in the race.

## Performance boundary

Opponent-response analysis is capped at the strongest preliminary candidates. This avoids freezing an iPhone on unusually large doubles trees. Unexamined candidates receive a conservative ranking penalty.

## Trust label

The UI calls this:

**Advanced local coach — offline, not grandmaster**

The local coach may be useful and substantially stronger, but only GNU Backgammon benchmark validation can support a grandmaster claim.
