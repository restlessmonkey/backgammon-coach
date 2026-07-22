# DR-0010 — Engine Decides, Coach Teaches

## Status

Implemented as the v2.0 architecture.

## Decision

Only a verified GNU Backgammon service may supply moves labeled grandmaster. The local heuristic cannot be silently substituted.

## Reason

Presentation quality does not establish playing strength. Animated reasoning built on a weak evaluator can teach the wrong lesson more convincingly. Therefore move selection and teaching presentation must be separate, independently identifiable layers.

## Modes

1. GNU Backgammon service — verified.
2. Local teaching fallback — explicitly not grandmaster.

## Remaining deployment dependency

A compliant HTTPS GNU Backgammon service is required before the app has live grandmaster-strength analysis.
