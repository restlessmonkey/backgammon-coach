# Backgammon Coach Backlog

## Product goal
Build a learning-first backgammon app that teaches the player while remaining pleasant to play on an iPhone.

## Completed
- [x] v1.6 Core Game Stabilization: turn flow, user-only undo, compact version label, legal-sequence enforcement, rules self-tests.
- [x] v1.7 Hint Foundation: ranked legal sequences, highlighted first move, short strategic explanations, transparent heuristic disclaimer.

## Next
- [ ] v1.8 Move Review: compare the user's chosen sequence with the top-ranked sequence before the computer moves.
- [ ] v1.9 Learning Modes: Beginner, Intermediate, Tournament; Coach On/Off behavior by mode.
- [ ] v2.0 Replay and move history.
- [ ] Stronger AI and engine-grade evaluation using an appropriately licensed integration or server-side analysis.
- [ ] Opening trainer, bearing-off trainer, pip-count trainer, daily puzzles.
- [ ] Post-game analysis, blunder detection, statistics, and progress tracking.
- [ ] Doubling cube and match play.
- [ ] Conversational Why? coach.
- [ ] Optional animation, sound, and haptics.

## Guardrails
- Never describe the local heuristic as GNU Backgammon or world-class analysis.
- Never recommend a move until complete legal-sequence enumeration passes.
- User Undo must never reverse computer moves.
- The board, pips, dice, turn status, and version must remain usable on an iPhone screen.
