# v2.0 Release Checklist

## Automated
- [x] HTML and JavaScript syntax validation.
- [x] Version and cache identity updated.
- [x] GNU Backgammon engine mode exists.
- [x] Local fallback is explicitly labeled not grandmaster.
- [x] Engine endpoint and health test exist.
- [x] Engine response identity is verified.
- [x] Position and legal candidates are serialized.
- [x] Grandmaster flow blocks on engine failure.
- [x] Watch the Coach Think accepts engine rankings.
- [x] Automatic coaching waits for engine rankings.
- [x] Engine API contract is included.

## Required before claiming live grandmaster play
- [ ] Deploy a real GNU Backgammon service.
- [ ] Test `/health`.
- [ ] Test `/analyze`.
- [ ] Validate benchmark positions.
- [ ] Verify iPhone HTTPS/CORS behavior.
- [ ] Review GNU GPL obligations.
