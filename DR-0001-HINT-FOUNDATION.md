# DR-0001 — Hint Foundation

## Decision
Version 1.7 ranks every maximum-length legal sequence using a transparent local heuristic and presents the top choices with concise teaching explanations.

## Why
A useful coach must first be legally reliable, fast on an iPhone, understandable, and available offline. A browser-only PWA cannot directly run the desktop GNU Backgammon application.

## Current scoring signals
Pip progress, bearing off, hits, made points, home-board points, prime length, blot creation/removal, bar exposure, and back-checker escape.

## Limitation
The ranking is educational and approximate. It is not a neural-network equity evaluation, rollout, or claim of world-class play.

## Future path
Evaluate a license-compatible GNU Backgammon neural-network integration, WebAssembly approach, or optional server-side analysis. Keep the teaching explanation layer separate from the evaluation engine so sources and confidence can be disclosed accurately.
