# Backgammon Coach Cumulative Backlog

## Product direction

Build a genuine teaching system in which a strong engine decides and a transparent visual coach teaches. Never present heuristic output as verified grandmaster analysis.

## Completed

### v1.8 — Guided Full-Turn Hints
- Dual Roll Dice controls.
- Optional point numbering.
- Plain-English instructions and notation.
- Full-sequence execution and guided steps.

### v1.9 — Explain Every Move
- Move ratings and explanations.
- Why Not This Move?
- Risk meters, favorites, Coach Report, explanation modes.

### v1.9.1 — Animated Board Hints
- Source/destination highlighting.
- Curved path and moving ghost checker.
- Multi-step non-destructive preview.

### v1.9.2 — Watch the Coach Think
- Candidate comparison.
- Rejection explanations.
- Final recommendation animation.

### v1.9.3 — Automatic Coach Think
- Persistent automatic coaching after every human roll.

### v2.0 — Grandmaster Engine Architecture
- Strict GNU Backgammon service contract.
- Explicit non-grandmaster local fallback.
- No silent fallback under a grandmaster label.

### v2.0.1 — Windows Engine Server Foundation
- Root package containing PWA, service, automation, tests, architecture, setup, validation, backlog, and handoff.
- `/health` and `/analyze` service endpoints.
- Request validation and evidence retention.
- Fail-closed adapter boundary.
- Windows install, diagnostic, run, stop, and test BAT files.
- Live validation checklist.

### v2.0.1.1 — Advanced Local Coach Strength Upgrade
- Replaced shallow one-position scoring with opponent-response expectation.
- Examines all 21 distinct opponent dice combinations for top candidate turns.
- Uses correct 36-outcome weighting.
- Added standard opening-book moves for all 15 non-double opening rolls.
- Added key-point, anchor, prime, exposure, stack, race/contact, and bear-off evaluation.
- Added performance caps for large doubles trees.
- Renamed fallback to **Advanced local coach — offline, not grandmaster**.
- Preserved v2.0.2 as the next GNU Backgammon interface-discovery milestone.

## Immediate next milestone

### v2.0.2 — GNU Backgammon Interface Discovery and Live Validation

Status: REQUIRED NEXT; implementation not started.

Goals:

- Inspect the exact installed Windows GNU Backgammon build.
- Identify the reliable command-line, script, or embedded-Python interface.
- Record exact commands, flags, accepted position format, and raw output.
- Create read-only benchmark probes.
- Prove board-orientation conversion.
- Produce an implementation-ready adapter specification.

Safety:

- Read-only discovery.
- No PWA promotion.
- No grandmaster certification.
- No enabling `analysis_enabled`.

## Subsequent milestones

### v2.0.3 — Certified GNU Backgammon Adapter
- Implement real candidate evaluation.
- Preserve raw engine evidence.
- Pass benchmark suite.
- Enable analysis only after independent validation.

### v2.0.4 — Secure iPhone Connectivity
- HTTPS reverse proxy or private tunnel.
- Authentication.
- Restricted CORS.
- Firewall and rate limiting.
- iPhone Safari validation.

### v2.1 — Engine-Powered Opponent and Cube Coaching
- Engine-selected computer moves.
- Double/take/pass analysis.
- Match-equity teaching.

### v2.2 — Complete Move Journal and Replay
- Append-only event history.
- Full replay.
- Branch-from-position practice.
- Immutable original game.

## Long-term ideas

- Voice narration.
- Coaching speed controls.
- Step backward/forward through analysis.
- Benchmark library.
- Personalized lesson progression.
- Opening-book and reference-position curriculum.
- Exportable match files.
- Tournament and money-game profiles.
