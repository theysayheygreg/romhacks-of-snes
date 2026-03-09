# SMZ3 Lineage Concepts

This note is intentionally concept-level.

The point is not to prove that a specific feature came from one exact upstream repository. The useful model is that `SMZ3` sits on top of a long accumulation of fan knowledge, patching patterns, logic work, and randomizer design from both the Zelda and Super Metroid communities.

## What SMZ3 is, conceptually

`SMZ3` is not just:

- a Zelda randomizer with Super Metroid attached

and not just:

- a Super Metroid randomizer with Zelda attached

It is better understood as:

- a crossover progression randomizer that uses two existing SNES games as substrates
- a merged-world logic engine
- a ROM build pipeline that emits one unified cartridge image

## What it likely inherits from the Zelda randomizer tradition

At the concept level, the Zelda side contributes a lot of the mature randomizer language and structure around:

- item-based progression routing
- location accessibility logic
- key logic and dungeon item handling
- spoiler logs and playthrough output
- settings-rich seed generation
- race/tournament style concerns

The Zelda randomizer ecosystem is especially strong at:

- expressing progression as a graph of item-gated checks
- exposing that graph through spoiler and playthrough artifacts
- supporting many seed settings while still preserving beatability

So one part of `SMZ3` clearly lives in that tradition:

- the seed is a constrained progression puzzle
- the generated world needs a coherent unlock path
- the output needs to be explainable through spoiler/playthrough structures

## What it likely inherits from the Super Metroid randomizer tradition

At the concept level, the Super Metroid side contributes a different emphasis:

- movement and execution assumptions
- trick-based accessibility
- area and room traversal gating
- progression difficulty as more than item ownership
- player-skill-aware logic

The Super Metroid randomizer ecosystem is especially strong at modeling:

- how movement ability changes route space
- how difficult tricks alter what is considered reachable
- how to express progression in a game where traversal skill is part of the logic

So another part of `SMZ3` clearly lives in that tradition:

- "logic" is not only inventory-based
- route access can depend on technique and movement assumptions
- the generated progression has to respect action-game traversal constraints, not only item ownership

## What is genuinely crossover-specific in SMZ3

This is the part that matters most.

`SMZ3` is not interesting only because it borrows two mature randomizer traditions. It is interesting because it has to solve problems that neither source game has on its own.

### Cross-game world graph

The two games are connected into one progression graph.

That means the generator must reason about:

- Zelda locations unlocking Metroid progress
- Metroid locations unlocking Zelda progress
- cross-game deadlock prevention
- cross-game portal placement and portal assumptions

This is more than "shuffle both item pools together". It is a merged dependency graph.

### Cross-game pacing

The seed has to feel playable across two very different action languages:

- Zelda-style overworld/dungeon progression
- Metroid-style traversal/exploration progression

That means `SMZ3` has to balance:

- where the player is likely to go next
- how early one game can dominate the seed
- whether the player can get trapped in one game's logic without the other game's expected tools

### Cross-game rule translation

Some progression artifacts have to be translated into a shared framework:

- crystals and pendants
- boss tokens
- keycards
- medallion or portal requirements
- map indicators and UI feedback

This is a design act as much as a technical one. The project has to invent equivalent currencies and access rules that let the two games speak a common progression language.

### Unified ROM build

Technically, `SMZ3` also solves a cartridge-level problem:

- combine two base ROMs
- lay them out into one larger ROM image
- apply the right patch layers
- preserve valid runtime behavior in emulators and on hardware

This is not just game logic. It is ROM architecture.

## Why this matters for your goals

For future game-dev ideas, `SMZ3` is valuable because it shows how to combine:

- reverse-engineered understanding of existing games
- deterministic procedural generation
- progression-graph design
- ROM patch/build engineering
- new mechanics that bridge previously separate systems

In other words, it is a strong example of how fan reverse engineering turns into actual game design.

## Best mental model

The cleanest way to think about `SMZ3` is:

- Zelda randomizers contribute strong item-graph and spoiler/playthrough traditions
- Super Metroid randomizers contribute strong traversal-skill and route-feasibility traditions
- `SMZ3` adds the genuinely hard part: merging two different progression grammars into one coherent game

That merged-progression problem is the real inheritance worth paying attention to.
