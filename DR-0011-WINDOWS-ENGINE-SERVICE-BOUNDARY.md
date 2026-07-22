# DR-0011 — Windows Engine Service Boundary

## Status

Accepted and implemented in v2.0.1.

## Decision

Run GNU Backgammon behind a separately deployed Windows service rather than attempt to embed native GNU Backgammon directly in the iPhone PWA.

## Reasons

- Native GNU Backgammon cannot be assumed to run inside Safari.
- Server-side execution allows controlled versioning and validation.
- The boundary separates GPL-covered engine deployment from the PWA package.
- Request and response evidence can be retained.
- The app can fail closed when the engine is unavailable.
- A future engine can be substituted without rewriting the teaching interface.

## Consequences

- The iPhone requires network access to the server.
- HTTPS and CORS must be configured.
- The adapter becomes a critical correctness component.
- Engine deployment and licensing require explicit documentation.
