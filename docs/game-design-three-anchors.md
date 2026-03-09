# Game Design: Three Anchor Games

This note captures the gameplay and design logic of the three current anchor games:

- Zelda 3
- Super Metroid
- Super Mario World

The point is not only to describe how they work.
The point is to identify the design structures that romhacks and randomizers actually manipulate.

## Zelda 3

### What the player is doing

At the highest level, Zelda 3 is:

- top-down action-adventure
- item-driven exploration
- dungeon and overworld routing
- lock-and-key progression across both micro and macro scales

The player loops through:

1. explore a new area
2. find an item, key, shortcut, or dungeon prize
3. unlock new spaces or new affordances
4. revisit old spaces with a stronger toolkit

### Core verbs and mechanics

The player verbs are comparatively simple:

- move
- attack
- block or avoid
- use context-sensitive items
- interact with switches, blocks, doors, and NPCs

The complexity comes less from dexterity than from:

- inventory growth
- state changes in the world
- remembering what was gated earlier

### Goal structure

The overall goal is to move from early overworld survival and basic dungeon completion toward:

- rescuing Zelda
- acquiring Master Sword and progression items
- traversing Light World and Dark World
- collecting crystals and pendants
- defeating Agahnim and Ganon

This means the game has both:

- local objectives: one room, one puzzle, one chest, one dungeon
- global objectives: world-state changes and long-term item routing

### Underlying design grammar

Zelda 3 is built around:

- inventory gates
- room-state flags
- dungeon-state flags
- macro story-state flags
- overworld access transitions

This is why it randomizes so well.
Its progression logic is already legible as a dependency graph.

### What hacks and randomizers naturally modify

The easiest high-value design levers are:

- item placement
- entrance and door destinations
- key logic
- dungeon structure and order pressure
- world-state assumptions
- text, HUD, and progression feedback

### Why this matters for future ideas

Zelda 3 is the cleanest anchor for:

- state-driven exploration
- item graph design
- puzzle gating
- spoilerable progression logic

If we want to build games where progression is about gaining tools and reinterpreting space, Zelda is the strongest template.

## Super Metroid

### What the player is doing

At the highest level, Super Metroid is:

- side-view action exploration
- movement-driven traversal
- combat and survival under spatial pressure
- nonlinear route discovery constrained by both items and execution

The player loop is:

1. enter a new room or region
2. test movement and survival boundaries
3. collect upgrades
4. reinterpret earlier geography through new movement powers

### Core verbs and mechanics

The verbs are more expressive and composable than Zelda 3:

- run
- jump
- aim and shoot
- morph and bomb
- wall jump / shinespark / grapple / space jump / etc.
- tank or avoid environmental hazards

The design has much stronger mechanical depth because traversal itself is a skill system.

### Goal structure

The overall goal is to:

- escape the starting constraints
- expand Samus's traversal and combat kit
- defeat major bosses
- open access to deeper regions
- resolve Tourian and the final escape

Unlike Zelda 3, the player is often not solving explicit puzzles.
They are reading topology, movement thresholds, combat pressure, and resource viability.

### Underlying design grammar

Super Metroid is built around:

- item gates
- movement-tech gates
- environmental-damage gates
- resource gates
- room and door topology

That is why the community talks so much about logic presets, tricks, and reachability.

### What hacks and randomizers naturally modify

The strongest design levers are:

- item placement
- room connectivity
- door graph structure
- movement assumptions
- boss order
- environmental pressure
- save/start state

### Why this matters for future ideas

Super Metroid is the strongest anchor for:

- traversal as mastery
- world readability through movement
- player-authored routing
- soft nonlinear progression

If we want games where space itself becomes legible through skill growth rather than only inventory growth, Super Metroid is the better template.

## Super Mario World

### What the player is doing

At the highest level, SMW is:

- authored action-platforming
- obstacle-course mastery
- world map progression with optional branching
- mechanic teaching through short, focused stages

The player loop is:

1. enter a level
2. read and solve platforming challenges
3. use movement affordances efficiently
4. reach goal, secret exit, or alternate route

### Core verbs and mechanics

The verbs are built around movement precision and momentum:

- run
- jump
- spin jump
- carry and throw
- fly or glide with cape
- ride Yoshi
- interact with shells, blocks, and enemies as movement tools

The core design depth comes from level authorship.
The game is less about world-state logic than about obstacle grammar and pacing.

### Goal structure

The overall goal is to:

- clear levels
- uncover secret exits
- open world-map branches
- complete special zones and castles
- reach Bowser through escalating movement tests

This means the progression system is partly:

- level-by-level skill development
- world-map branching and secret routing

### Underlying design grammar

SMW is built around:

- movement affordance combinations
- object and enemy interaction rules
- level pacing
- secret exit graph design
- overworld route branching

This is why editor-driven workflows dominate the ecosystem.
The most valuable changes usually happen at the level, overworld, and asset-authoring layer rather than only through ROM-wide logic shuffles.

### What hacks and randomizers naturally modify

The strongest design levers are:

- level geometry
- sprite and object placement
- overworld route structure
- exits and secret-exit graph
- movement affordances and custom blocks/sprites
- difficulty curve and obstacle cadence

### Why this matters for future ideas

SMW is the strongest anchor for:

- authored challenge design
- teach-test-twist level pacing
- movement feel as the primary design material
- editor-assisted content production

If we want to build projects where custom content volume and deliberate obstacle craft matter most, SMW is the best template.

## Cross-game comparison

The cleanest summary is:

- Zelda 3: progression as item and world state
- Super Metroid: progression as movement and topology
- SMW: progression as authored challenge and route branching

That also tells us what kinds of hacks each game naturally supports:

- Zelda 3:
  - item randomizers
  - entrance and door randomizers
  - dungeon/state reshaping
- Super Metroid:
  - item randomizers
  - area/map randomizers
  - movement-logic and room-topology remixes
- SMW:
  - level hacks
  - overworld/exit remixes
  - editor-heavy and patch-augmented total conversions

## Design leverage for future projects

If we are mining these games for reusable ideas, the main reusable design grammars are:

- Zelda 3:
  - modular item-gated exploration
- Super Metroid:
  - spatial mastery through expanded movement verbs
- SMW:
  - compact, repeatable challenge authorship and pacing

The most interesting crossover ideas probably combine:

- Zelda-style dependency graphs
- Metroid-style movement discovery
- SMW-style authored micro-challenge pacing
