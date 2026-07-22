# DR-0002 — Guided Full-Turn Hints and Dual-Perspective Notation

## Status
Implemented in v1.8.

## Decision
Treat a backgammon recommendation as a complete legal turn sequence rather than an isolated checker movement. Provide two teaching actions: automatically execute the still-legal sequence, or guide the learner through it one checker step at a time.

## Rationale
A learner should not be expected to infer how two dice combine, understand unexplained notation, or guess which checker to move second. Plain-English directions are primary. Standard notation is optional and always tied to a stated player perspective.

## Safety and validation
- Recheck each step against the current legal-sequence engine immediately before applying it.
- Preserve Undo only within the human turn.
- Keep point labels optional to avoid iPhone clutter.
- Preserve the successful iPad presentation.
- Do not represent the local heuristic as engine-grade analysis.
