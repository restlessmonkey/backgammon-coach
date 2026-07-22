# DR-0009 — Automatic Coach Think

## Status
Implemented in v1.9.3.

## Decision
Add an optional, persistent mode that starts Watch the Coach Think automatically after every human roll.

## Rationale
Repeated manual activation interrupts observation. Automatic playback allows continuous learning from candidate comparison and graphical demonstrations.

## Guardrails
- User-controlled and off by default.
- Saved locally.
- Runs only after a valid human roll with a legal move.
- Does not alter the real board.
- Can be stopped or disabled at any time.
