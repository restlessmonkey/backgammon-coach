# Pip — Your Backgammon Coach
## Project File
Version 1.0
Backgammon Coach package version: v2.0.5.3

---

## 1. Purpose

Pip is the permanent in-app coaching mascot for Backgammon Coach.

Pip is not the analysis engine. Pip is the teacher and personality layer that explains, encourages, celebrates, and helps the player understand the engine's decisions.

Permanent architecture rule:

> Engine decides. Pip teaches.

Only verified GNU Backgammon may be labeled Grandmaster. The Advanced Local Coach must remain honestly labeled as local/offline analysis.

---

## 2. Core Identity

Official name:

**Pip — Your Backgammon Coach**

Literary branding:

The name intentionally preserves the **Great Expectations** wordplay. This may appear in optional Pip personality lines, achievements, release notes, and playful Easter eggs.

Pip's mission:

- Teach rather than merely score moves.
- Explain why a move is better.
- Encourage without embarrassing the player.
- Never become sarcastic, cruel, or condescending.
- Never imply that Pip is the engine.
- Make backgammon instruction feel friendly, memorable, and approachable.

---

## 3. Visual Identity

Pip is a literal backgammon pip/checker.

Pip is not:

- a human wearing a checker costume
- an animal mascot
- a generic cartoon child
- a replacement for the board pieces

Pip is the checker itself, made cute and welcoming.

Permanent visual traits:

- round checker body
- expressive eyes
- eyebrows
- friendly mouth
- simple arms and hands
- simple legs and shoes
- clean, readable silhouette
- suitable for small mobile display sizes
- welcoming rather than overly childish
- consistent across all appearances

Signature brand element:

Pip should retain a recognizable cap or equivalent signature element featuring the letter **P**, unless future design testing proves a stronger permanent silhouette.

---

## 4. Pip Variants and Inclusive Customization

Users must be able to personalize Pip without changing Pip's underlying identity.

Current required options:

- Boy Pip
- Girl Pip
- Multiple inclusive skin-tone options
- Visible or hidden
- Personality choice

Current v2.0.4.x implementation includes six skin-tone options.

Future customization may include:

- hair styles
- glasses
- hats
- bows
- winter hat
- Santa hat
- birthday hat
- seasonal accessories
- optional clothing accents
- accessibility-friendly contrast variants

Customization must remain separate from gameplay and engine logic.

---

## 5. Settings Architecture

A standard gear icon provides access to a dedicated Settings page or modal.

The gameplay screen must remain clean and should not be overloaded with avatar controls.

Planned Settings structure:

### Pip
- Boy Pip or Girl Pip
- skin tone
- visibility
- avatar size or presentation
- personality
- speaking frequency
- optional accessories

### Coaching
- skill level
- explanation detail
- automatic Watch Pip Think behavior
- hints
- coaching frequency
- analysis source

### Playback
- restart
- pause
- resume
- previous move
- next move
- playback speed such as 0.5×, 1×, and 2×
- automatic replay behavior
- explanation synchronization

### Game Experience
- sound
- celebrations
- dice animation
- board appearance
- accessibility
- reduced motion

### Engine
- Advanced Local Coach
- verified GNU Backgammon connection
- honest source labeling
- no misleading Grandmaster label for non-GNU analysis

All settings should persist locally in the browser/PWA where practical.

---

## 6. Pip Personality Modes

### Calm Coach
Short, steady, reassuring explanations.

Example:

> Ready when you are. We'll take this one move at a time.

### Friendly Coach
Warm, conversational, and encouraging.

Example:

> Hi! I'm Pip. Let's find a strong move together.

### Cheerleader
More energetic and celebratory.

Example:

> You've got this! Let's make a great move!

### Great Expectations
Optional literary personality that uses tasteful Great Expectations references without becoming repetitive.

Examples:

> I have great expectations for this position.

> Great expectations—and a strong anchor.

### “Helpful” Mode
A deliberate Easter egg and comedy mode inspired by the famously intrusive office assistant archetype.

This is not a normal coaching mode.

Pip becomes pathologically enthusiastic about helping, increasingly intrusive, and intentionally in the player's way—but never cruel.

The joke is that Pip remains sincere and believes he is being useful.

---

## 7. “Helpful” Mode Design

Display name:

**“Helpful”**

The quotation marks are part of the joke.

Recommended Settings placement:

- Advanced
- Personality
- Easter Eggs

Activation warning:

> Wonderful! I'll make sure you never miss another opportunity to improve!

### Core behavior

Pip may react to:

- rolling the dice
- moving a checker
- undo
- replay
- inactivity
- hovering over or selecting a blot
- bearing off
- opening or closing coaching panels
- repeated analysis
- repeated example playback

### Example lines

After rolling:

> I noticed you rolled the dice!

> Excellent! Those are definitely numbers.

After moving:

> I noticed you moved a checker.

> That's definitely a legal move.

> Would you like to know why you did that?

After undo:

> Excellent! We can make mistakes together.

> Undo is just learning in reverse.

After replay:

> Again? I like your dedication.

> I can watch this all day.

After inactivity:

> Thinking?

> Take your time. I'll wait.

> I'm still here.

> Would a hint help?

When hovering over a blot:

> It looks like you're leaving a blot. Would you like to leave a blot?

When bearing off:

> Only fourteen more!

When winning by a large margin:

> I don't want to jinx it...

### Escalation system

Helpful Mode should become progressively more intrusive.

Possible levels:

1. Slightly too helpful
2. Frequent observations
3. Repeated suggestions
4. Inactivity commentary
5. Visual interruptions
6. Edge peeking
7. Returns after being dismissed
8. Maximum helpfulness

Possible visual gags:

- Pip peeks from behind the board.
- Pip slides in from the edge.
- Pip carries a magnifying glass.
- Pip wears reading glasses.
- Pip holds a sign reading “Helpful!”
- Pip returns after being dragged away.
- Pip's eyes remain visible after minimization.
- Pip eventually appears with popcorn.
- Pip dramatically faints when a blot is left.
- Pip walks back after being moved.

### Escape action

After sufficient interruptions, reveal:

> Pip... that's enough.

When selected:

> Oh... I thought I was helping.

Then:

> I'll be quieter now.

Helpful Mode returns to a normal Pip personality.

### Achievement Easter egg

After Helpful Mode is activated three separate times:

**Great Expectations Met**

Pip says:

> I had great expectations... and you exceeded them.

This achievement is optional future work and should not block the base Helpful Mode.

---

## 8. Pip Expressions

A reusable Pip expression library should eventually include at least:

- happy
- thinking
- curious
- excited
- celebrating
- oops
- confused
- proud
- concentrating
- aha
- winking
- thumbs up
- cheering
- concerned
- surprised
- encouraging
- patient
- skeptical
- sleepy
- relieved
- fainting

Expressions should communicate meaning and reduce the need for text.

---

## 9. Pip Poses and Props

Reusable poses:

- standing
- pointing
- looking at the board
- holding a magnifying glass
- holding dice
- holding the doubling cube
- holding a trophy
- holding a heart
- celebrating
- thinking
- shrugging
- peeking
- waving
- reading
- fainting

Reusable props:

- dice
- doubling cube
- magnifying glass
- trophy
- heart
- speech bubble
- sign
- popcorn
- book
- lightbulb

---

## 10. Animation Language

Pip animations should have meaning.

Examples:

- Thinking: scratch chin
- Idea: finger up or lightbulb
- Great move: small jump
- Mistake or danger: gentle head tilt
- Celebration: spin or bounce
- Blot danger: dramatic but playful faint
- Helpful Mode escalation: edge peek or repeated return

Animations must respect reduced-motion accessibility settings.

---

## 11. Voice and Dialogue Rules

Potential future voice:

- warm
- calm
- teacher-like
- optimistic
- never robotic
- never patronizing

Permanent dialogue rules:

- Never say merely “Wrong move.”
- Explain the concern or opportunity.
- Prefer constructive phrasing.
- Avoid shame.
- Avoid sarcasm outside explicitly comedic Easter eggs.
- Even in Helpful Mode, Pip remains well-intentioned rather than hostile.

Preferred coaching phrasing:

> Interesting idea. Let's see another possibility.

> That move leaves a blot. We can make it a little safer.

> Nice find!

> Let's look a little deeper.

> I think we can improve this.

> That's a strong point.

> Excellent timing.

> Good racing.

> That keeps your options open.

---

## 12. Asset Library Plan

Future assets should be organized into a stable Pip library.

Suggested structure:

```text
Pip/
  Base_Body/
  Boy/
  Girl/
  Skin_Tones/
  Expressions/
  Poses/
  Hats/
  Accessories/
  Hands/
  Dice/
  Doubling_Cube/
  Magnifying_Glass/
  Trophy/
  Speech_Bubbles/
  Loading_Animations/
  Celebration_Animations/
  SVG/
  PNG/
  Dark_Mode/
  Reduced_Motion/
  Source_Art/
```

Every asset should identify:

- version
- variant
- expression
- pose
- skin tone
- file format
- intended UI use
- source artwork
- export dimensions
- transparency status

---

## 13. Current Implemented State — v2.0.4.x

Implemented:

- fixed gear button
- Pip Settings modal
- Boy Pip
- Girl Pip
- six skin tones
- Pip visibility
- local persistence
- Calm Coach
- Friendly Coach
- Cheerleader
- Great Expectations
- “Helpful” Mode
- Helpful reactions to:
  - inactivity
  - roll
  - move
  - undo
  - replay
- Helpful intensity meter
- edge-peeking behavior
- “Pip... that's enough.” escape action
- CSS-rendered Pip avatar
- no gameplay-function replacement
- existing board and panels preserved

Preserved:

- collapsible side panels
- independent side-panel scrolling
- Replay Example
- Watch Pip Think
- Advanced Local Coach
- GNU integration
- position intelligence
- 44 celebrations
- gameplay behavior

---

## 14. Existing Coaching Playback Backlog

The following remain on the backlog:

1. Playback controls:
   - restart
   - pause
   - resume
   - previous move
   - next move
   - playback speed options such as 0.5×, 1×, and 2×

2. Coach Timeline:
   - show each move step
   - show final position
   - tap-to-jump navigation

3. Active explanation synchronization:
   - highlight the matching explanation
   - auto-scroll as each checker moves

4. Post-animation actions:
   - Replay
   - Try it yourself
   - Why was this better?

---

## 15. Local Coach Development Direction

Active architectural principle:

> Engine decides. Pip teaches.

Current local evaluator direction includes transparent factors such as:

- pip count
- race lead
- blot exposure
- direct and indirect shots
- point strength
- anchors
- primes
- builders and distribution
- flexibility
- duplicated numbers
- timing
- contact versus race
- back-checker escape
- opponent-board danger
- gammons
- bear-off efficiency

Future algorithm backlog:

- position-specific evaluators
- expectiminimax
- candidate pruning
- Monte Carlo rollouts
- self-play learning
- opening and reference knowledge
- confidence reporting

Only verified GNU Backgammon may be labeled Grandmaster.

---

## 16. Product and Safety Rules

- Pip customization must never alter move legality or engine analysis.
- Pip must not cover critical controls in normal modes.
- Helpful Mode may intentionally become intrusive, but the escape control must remain available.
- Helpful Mode must be opt-in and never enabled by default.
- The board and primary gameplay controls must remain usable.
- Pip must respect reduced motion and accessibility settings.
- Pip must not misrepresent local analysis as GNU output.
- Pip must not insult or shame the player.
- User choices should persist locally.
- All future releases should preserve existing functionality unless a change is explicitly approved.

---

## 17. Release and Documentation Rules

Every future Pip release package should include:

- package version
- ZIP name
- SHA-256
- extraction instructions
- change summary
- validation report
- known limitations
- next validation step
- standalone `COMMIT_MESSAGE.txt`
- updated project file
- exact statement of what gameplay or engine behavior changed
- exact statement of what remained unchanged

The project file must be cumulative. New decisions should be added without deleting prior reasoning, deferred work, Easter eggs, or unresolved design questions.

---

## 18. Immediate Next Steps

Recommended next work:

1. Visually test the current CSS Pip on iPhone and iPad.
2. Confirm gear placement does not obscure controls.
3. Confirm the Settings modal scrolls correctly.
4. Confirm Boy Pip and Girl Pip are visually distinct but clearly the same mascot.
5. Confirm all six skin tones remain readable against the board and modal backgrounds.
6. Tune Helpful Mode timing so it is funny rather than immediately exhausting.
7. Replace or supplement the CSS avatar with a formal Pip asset set after the Pip Bible is approved.
8. Create the first expression sheet and pose sheet.
9. Add accessibility and reduced-motion controls.
10. Add Pip asset versioning and naming conventions.

---

## 19. Canonical Decision Summary

Pip is now a permanent product character, not a temporary decoration.

The character must remain:

- a literal pip/checker
- cute and welcoming
- inclusive and customizable
- separate from engine logic
- honest about analysis source
- useful in normal modes
- comically overhelpful only when the user deliberately enables “Helpful” Mode

The defining product principles are:

> Engine decides. Pip teaches.

and, in the appropriate optional personality:

> Great expectations.


---

## 20. Character Studio and Asset Catalog — v2.0.5.3

The first reusable Pip character system is now defined.

Added:

- `PIP_ASSET_CATALOG.md`
- `pip-studio.html`
- twelve expression states
- eight pose states
- live Boy Pip / Girl Pip selection
- all six approved skin tones
- accessible live labels

This is a design and preview release. Gameplay event integration remains intentionally deferred until the expressions and poses are visually reviewed and approved.


---

## 21. Character Studio Navigation — v2.0.5.3

The Pip Character Studio is now directly accessible from the main app.

Navigation path:

1. Open `index.html`.
2. Select the gear icon.
3. Select **Open Pip Character Studio**.
4. Use **Back to Backgammon Coach** to return.

This is a navigation-only update. Gameplay and Pip behavior are unchanged.


---

## 22. Main Screen and Settings Panel Architecture — v2.0.5.3

The main app screen now keeps only the **Game** panel.

All other app panels are located behind the gear in:

**Settings → App Panels**

This is now the preferred interface rule:

- Game panel: main screen
- All non-Game panels: Settings
- Pip Character Studio: Settings
- Pip customization: Settings

The implementation moved 6 detected non-Game panels while preserving their existing markup, IDs, and controls.


---

## 23. Pip Mobility, Dismissal, and Restoration — v2.0.5.3

Pip is now directly movable and dismissible.

Implemented:

- drag Pip anywhere on screen
- save Pip’s location locally
- clamp Pip within the visible viewport
- dismiss Pip using the X control
- restore Pip using **Bring Pip back**
- reset Pip to his normal position from Settings
- dismiss Pip from Settings

The floating Roll Dice control was also restored to its intended behavior:

- floating mode now works at all viewport widths
- it remains visible while temporarily disabled
- its saved drag position, lock setting, and reset control remain supported
