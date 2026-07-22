# Backgammon Coach Backlog

## Product goal
Build a learning-first backgammon app that teaches the player while remaining pleasant to use on iPhone and iPad.

## Completed
- [x] v1.6 Core Game Stabilization: turn flow, user-only undo, compact version label, legal-sequence enforcement, rules self-tests.
- [x] v1.7 Hint Foundation: ranked complete legal sequences, highlighted first move, strategic explanations, transparent heuristic disclaimer.
- [x] v1.8 Guided Full-Turn Hints: execute the complete recommended sequence; step-by-step guided play; plain-English directions; optional standard notation; user/computer/both point labels; top and center Roll Dice controls; computer move notation from both perspectives.

## Next certified sequence
- [ ] v1.9 Complete Move Journal: append-only record of every roll, complete legal sequences, chosen sequence, checker steps, before/after positions, hits, bar entries, bearing off, hints, recommendation-followed status, Undo events, timestamps, player/turn identity, and result.
- [ ] v2.0 Replay and Branching Practice: replay from any recorded position; step forward/backward; branch into a separate practice session; reset or discard the branch without modifying the original game.

## Later learning backlog
- [ ] Beginner, Intermediate, and Tournament learning modes.
- [ ] Move review before the computer turn.
- [ ] Stronger AI and engine-grade evaluation using an appropriately licensed integration or server-side analysis.
- [ ] Opening, bearing-off, and pip-count trainers; daily puzzles.
- [ ] Post-game analysis, blunder detection, statistics, and progress tracking.
- [ ] Doubling cube and match play.
- [ ] Conversational Why? coach.
- [ ] Optional animation, sound, and haptics.
- [ ] Device profiles: Auto, iPhone, iPad, and future Desktop analysis layout.

## Guardrails
- Never describe the local heuristic as GNU Backgammon or world-class analysis.
- Never recommend or execute a move until complete legal-sequence enumeration passes.
- “Make this move now!” must execute the entire still-legal sequence, including two dice or four plays on doubles.
- User Undo must never reverse computer moves.
- Standard notation must always identify the perspective used.
- Original saved games must remain immutable when replay branches are introduced.
- Responsive changes must not degrade the successful iPad layout.
