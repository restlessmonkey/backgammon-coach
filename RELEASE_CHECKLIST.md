# v1.8.2 Release Validation Checklist

## Identity
- [ ] Version badge reads v1.8.2
- [ ] Page title reads v1.8.2
- [ ] Service-worker cache is backgammon-coach-v1-8-2

## Core gameplay regression
- [ ] New game starts correctly
- [ ] Both Roll Dice controls invoke the same roll
- [ ] Legal checker and destination highlights work
- [ ] Undo works only during the human turn
- [ ] Finish turn appears when no legal move remains
- [ ] Computer turn runs automatically
- [ ] Make this move now executes a complete legal sequence
- [ ] Show me guides each linked move
- [ ] Rules self-test reports PASS

## Immersive Play
- [ ] Header is full before first roll
- [ ] Header collapses after first human roll
- [ ] Mobile Coach drawer starts collapsed
- [ ] Coach drawer opens without moving the board
- [ ] Hint request opens the drawer
- [ ] Larger Roll Dice control is easy to reach
- [ ] Floating mode can be enabled/disabled
- [ ] Dragged position survives reload
- [ ] Lock prevents dragging
- [ ] Reset restores a valid default position
- [ ] Left/right handed preferences work
- [ ] Focus mode hides and restores extra panels

## Device review
- [ ] iPhone portrait
- [ ] iPhone landscape
- [ ] iPad portrait
- [ ] iPad landscape
- [ ] Desktop browser
