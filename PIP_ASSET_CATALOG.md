# Pip Character Asset Catalog
Version 1.0
Backgammon Coach package version: v2.0.6.1

## Purpose

This catalog defines the first reusable Pip expression and pose system.

Pip remains a literal backgammon pip/checker. Boy Pip and Girl Pip are variants of the same character, not separate mascots. Skin tone, personality, expression, and pose are independent attributes.

Permanent rule:

> Engine decides. Pip teaches.

## Asset Naming Convention

Use:

`pip_<style>_<tone>_<expression>_<pose>_<variant>.<ext>`

Examples:

- `pip_boy_medium_happy_standing_v01.svg`
- `pip_girl_deep_thinking_pointing_v01.png`
- `pip_universal_medium_aha_holding-dice_v01.svg`

Preferred style values:

- `boy`
- `girl`
- `universal`

Preferred tone values:

- `light`
- `light-medium`
- `medium`
- `medium-deep`
- `deep`
- `very-deep`

## Expression Set v1

1. Neutral
2. Happy
3. Thinking
4. Curious
5. Excited
6. Proud
7. Aha
8. Concerned
9. Oops
10. Confused
11. Winking
12. Celebrating

### Expression Semantics

**Neutral**  
Default resting state. Calm, alert, welcoming.

**Happy**  
Used for ordinary encouragement, legal moves, and successful setup.

**Thinking**  
Used while analysis is running or while explaining alternatives.

**Curious**  
Used when inviting the player to inspect another possibility.

**Excited**  
Used for excellent finds, strong tactical shots, and major improvements.

**Proud**  
Used after the player follows a strong recommendation or solves a teaching moment.

**Aha**  
Used when revealing a key tactical or positional insight.

**Concerned**  
Used for exposed blots, timing problems, trapped back checkers, or opponent-board danger.

**Oops**  
Used gently after an avoidable error; never shaming.

**Confused**  
Used sparingly for unusual states, incomplete actions, or “Helpful” Mode jokes.

**Winking**  
Used for light humor, Easter eggs, and Great Expectations references.

**Celebrating**  
Used for wins, achievements, excellent moves, and milestones.

## Pose Set v1

1. Standing
2. Pointing
3. Looking at Board
4. Holding Dice
5. Holding Doubling Cube
6. Holding Magnifying Glass
7. Thumbs Up
8. Peeking

### Pose Semantics

**Standing**  
Default general-purpose pose.

**Pointing**  
Calls attention to a board location, move sequence, or explanation.

**Looking at Board**  
Used during analysis and Watch Pip Think.

**Holding Dice**  
Used before rolling, after rolling, and in dice-related teaching.

**Holding Doubling Cube**  
Used for cube decisions and match equity explanations.

**Holding Magnifying Glass**  
Used for deeper analysis, comparisons, and “Let's look a little deeper.”

**Thumbs Up**  
Used for encouragement and confirmed strong play.

**Peeking**  
Reserved primarily for “Helpful” Mode and playful Easter eggs.

## Approved Pairings v1

- Neutral + Standing
- Happy + Thumbs Up
- Thinking + Looking at Board
- Curious + Pointing
- Excited + Holding Dice
- Proud + Thumbs Up
- Aha + Pointing
- Concerned + Looking at Board
- Oops + Standing
- Confused + Holding Magnifying Glass
- Winking + Peeking
- Celebrating + Holding Doubling Cube

## Accessibility Rules

- Expressions must remain understandable without color alone.
- Do not rely only on eyebrow position; mouth and pose should reinforce meaning.
- Maintain readable contrast at small mobile sizes.
- Respect reduced-motion preferences.
- Provide text equivalents through aria-labels or nearby coaching text.
- Avoid rapid flashing or repetitive bouncing.

## Rendering Rules

- Pip must remain recognizable at 64 px.
- Primary master assets should be vector where practical.
- Transparent PNG exports should be available for static use.
- Keep a consistent checker diameter and face placement.
- Preserve the signature P cap unless a future approved identity revision supersedes it.
- Do not create visual differences that imply one Pip style is more skilled or authoritative.

## Current Implementation Status

v2.0.6.1 adds:

- `pip-studio.html`, an interactive character preview page.
- Twelve expression states.
- Eight pose states.
- Boy Pip and Girl Pip.
- Six skin tones.
- Live aria-label updates.
- No gameplay integration changes.

## Next Asset Work

1. Review the Character Studio on iPhone and desktop.
2. Approve or revise the twelve expressions.
3. Approve or revise the eight poses.
4. Create production SVG masters.
5. Add expression selection rules to coaching events.
6. Connect Thinking to Watch Pip Think.
7. Connect Concerned to exposed blot and danger explanations.
8. Connect Aha to strongest-position-factor explanations.
9. Connect Celebrating to existing celebration triggers.
10. Reserve Peeking for “Helpful” Mode escalation.
