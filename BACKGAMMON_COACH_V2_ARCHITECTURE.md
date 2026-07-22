# Backgammon Coach v2 Architecture

## Document status

- Architecture version: 2.0.1
- Product version: Backgammon Coach v2.0.1
- Status: Engine-service foundation implemented; live GNU Backgammon adapter not yet certified
- Governing principle: **Engine decides. Coach teaches.**
- Safety principle: **No verified engine, no grandmaster claim.**

## 1. Purpose

Backgammon Coach is an iPhone-oriented progressive web application that combines playable backgammon, visual instruction, move comparison, animation, and persistent learning features. Version 2 separates move authority from teaching presentation so that attractive explanations cannot disguise a weak move evaluator.

## 2. System context

```text
iPhone/iPad PWA
    |
    | HTTPS JSON
    v
Backgammon Coach Engine Server
    |
    | adapter subprocess / documented boundary
    v
GNU Backgammon
```

The PWA remains responsible for game interaction, legal-move generation, animation, explanations, and user learning controls. The server validates requests, invokes the engine adapter, preserves request evidence, and returns ranked candidates. GNU Backgammon is the authoritative evaluator only after the adapter has been validated.

## 3. Components

### 3.1 PWA

Responsibilities:

- Maintain playable game state.
- Generate complete legal candidate turns.
- Send the board, dice, cube/match context, and candidates to `/analyze`.
- Reject responses that do not identify the source as GNU Backgammon.
- Animate and explain the chosen sequence.
- Distinguish verified analysis from the local teaching fallback.
- Preserve automatic Watch the Coach behavior.

### 3.2 Engine server

Responsibilities:

- Expose `/health` and `/analyze`.
- Enforce the `backgammon-coach-engine-v1` protocol.
- Validate board and candidate structure.
- Write each request into an isolated runtime evidence directory.
- Invoke the configured adapter with a timeout.
- Reject missing, malformed, or unverified output.
- Return HTTP 503 rather than fabricate an answer.

### 3.3 GNU Backgammon adapter

Responsibilities after certification:

- Convert the PWA board orientation into an accepted GNU Backgammon position representation.
- Apply dice, player-on-roll, cube, score, match length, Crawford, and Jacoby context correctly.
- Evaluate each complete legal candidate at the approved analysis strength.
- Return rank, equity, error relative to best, notation, and engine identity.
- Preserve raw GNU Backgammon output or machine-readable evidence.
- Record executable path, version, settings, and analysis depth.

The adapter in v2.0.1 is deliberately a fail-closed scaffold. It does not fabricate rankings.

## 4. Trust boundaries

1. Browser input is untrusted.
2. The server validates every request.
3. Candidate moves supplied by the PWA are not treated as engine conclusions.
4. Adapter output is untrusted until its schema and engine identity are verified.
5. A successful `/health` response does not alone certify move accuracy.
6. Grandmaster status requires benchmark-position validation.

## 5. Request lifecycle

1. Human rolls.
2. PWA generates all legal complete turns.
3. PWA POSTs the position and candidates.
4. Server validates the request.
5. Server creates `runtime/<request-id>/request.json`.
6. Adapter evaluates through GNU Backgammon.
7. Adapter writes `response.json`.
8. Server verifies engine identity and rankings.
9. Server returns the response and stores `final_response.json`.
10. PWA uses the engine order as authoritative and generates the visual lesson.

## 6. Failure behavior

- Missing endpoint: PWA blocks verified analysis.
- GNU Backgammon missing: `/health` returns setup-required.
- Analysis disabled: `/analyze` returns 503.
- Adapter error or timeout: `/analyze` returns 503 with request ID.
- Unverified engine identity: response rejected.
- Invalid candidate mapping: response rejected.
- Local fallback: permitted only when deliberately selected and labeled not grandmaster.

## 7. Network model

Initial supported model:

- Windows server on the same trusted home network.
- Local HTTP may be used only for server diagnostics.
- The deployed PWA requires an HTTPS-accessible endpoint because browsers can block mixed content.
- Recommended production options are a properly secured reverse proxy or a private HTTPS tunnel.
- Authentication, rate limiting, and secret management remain required before internet exposure.

## 8. Security requirements before internet exposure

- HTTPS only.
- Authentication token or mutual trust mechanism.
- Restricted CORS origins.
- Request-size limits.
- Rate limits.
- No shell interpolation.
- Fixed adapter command array.
- Non-administrator service account.
- Runtime evidence retention policy.
- Firewall rules limited to necessary traffic.

## 9. Licensing boundary

GNU Backgammon is GPL software. This package does not bundle GNU Backgammon, its neural-network files, or modified GNU Backgammon code. The deployment and distribution model must be reviewed before combining or redistributing GPL-covered components.

## 10. Certification gates

The service may be labeled live grandmaster only when all are true:

- GNU Backgammon executable located and version recorded.
- Board orientation conversion independently verified.
- Bar, bear-off, hit, doubles, and forced-move positions pass.
- Money-game and match-play contexts pass.
- Candidate rankings match direct GNU Backgammon analysis.
- Equity/error mapping passes.
- Raw evidence is retained.
- iPhone HTTPS/CORS operation passes.
- No silent fallback is possible.

## 11. Current state at v2.0.1

Implemented:

- Root package.
- Windows Python service runtime.
- Health and analyze endpoints.
- Request validation.
- Evidence directories and logs.
- BAT installation, diagnostic, run, stop, and test controls.
- Fail-closed adapter boundary.
- Architecture, backlog, setup, validation, and handoff documents.

Not yet implemented or certified:

- Final GNU Backgammon position conversion.
- Real candidate evaluation.
- Production HTTPS exposure.
- Authentication.
- Benchmark certification.

## 12. Next architectural milestone

v2.0.2 should be a read-only GNU Backgammon Interface Discovery and Live Validation package. It should inspect the installed Windows build, determine the most reliable automation interface, capture exact commands and outputs, and produce the evidence needed to implement the adapter without guessing.
