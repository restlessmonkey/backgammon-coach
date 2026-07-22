# Changelog

## v2.0 — Grandmaster Engine Architecture

- Replaced the misleading assumption that the local heuristic is expert strength.
- Added a strict GNU Backgammon HTTPS analysis adapter.
- Added engine source selection:
  - GNU Backgammon service — verified
  - Local teaching fallback — not grandmaster
- Grandmaster recommendations are blocked until a compliant engine service responds.
- Added engine endpoint storage and connection testing.
- Added engine identity verification.
- Added request serialization for complete board state and every legal turn.
- Added engine equity/error fields to the internal ranking model.
- Watch the Coach Think now teaches from engine rankings when connected.
- Automatic Coach Think now waits for verified engine analysis.
- Preserved animation, candidate comparison, guided execution, and learning explanations.
- Added an engine API contract and deployment documentation.

## v1.9.3
- Added automatic Coach Think after every human roll.
