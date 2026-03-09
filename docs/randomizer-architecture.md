# Randomizer Architecture

This note describes randomizers at the game-design and build-system level.

## Core concepts

### Seed generation

A randomizer is usually driven by a `seed`.

The seed is the deterministic input that drives:

- item placement
- entrance or door placement
- key logic
- boss/prize assignment
- patch payload generation
- spoiler output
- final ROM generation

Two runs with the same settings and the same seed should produce the same game.

### Logic

In player-facing language, `logic` is the rule system that decides what counts as reachable.

Logic defines:

- which items or abilities are required to access a location
- which tricks are allowed
- which progression states are valid
- whether a seed is considered beatable

So a useful way to phrase it is:

- `seed` is the deterministic generator input
- `logic` is the reachability model used to validate and shape the generated world

### Spoiler log

A spoiler log is an optional generated record of the seed's contents.

It usually contains:

- item locations
- dungeon prizes
- entrance or door mappings
- progression spheres or progression path
- sometimes patch metadata or settings

This is not just a convenience feature. It is often the easiest human-readable proof of what the seed-generation layer actually produced.

## Conceptual model

Most randomizers in this workspace fit a layered model:

1. Base game model
2. Logic and rule model
3. Seed generation
4. Patch/ROM write layer
5. Final ROM output
6. Optional spoiler and metadata output

## Two major randomizer families

### Item-location randomizers

These keep the world structure mostly recognizable and primarily shuffle:

- item locations
- rewards
- key items
- sometimes entrances or minor rule variations

The player's main challenge is:

- understanding progression under a changed item graph

### World-structure randomizers

These change the structure of the world itself:

- doors can lead to different rooms
- room connections can be remapped
- dungeon topology can change
- area traversal can be redefined

The player's challenge becomes two-layered:

- understand progression under changed item logic
- learn and navigate a newly generated world graph

This is a materially different design problem from simple item shuffling, because the generator is no longer only permuting rewards. It is also rewriting navigation.

## Progression path

A good randomizer is usually not "pure chaos".

At a high level, it preserves a progression structure:

- item `A` unlocks access to area or check set `B`
- which yields item `C`
- which unlocks a later part of the game
- and so on until the game is beatable

So even when locations are randomized, there is still an intended progression path, often close in shape to the original game's pacing:

- early-game access
- mid-game expansion
- late-game lock/key resolution
- endgame completion route

The exact path changes per seed, but the randomizer tries to ensure the path exists.

## Typical outputs

Randomizers often emit more than one artifact:

- generated ROM
- patch file
- spoiler log
- settings summary
- playthrough or progression spheres

That means a randomizer repo should not be read only as "ROM patch code". It is usually also:

- a rules engine
- a constrained world generator
- a validation system
- a reporting system

## How this maps to current repos

- `jpdasm`
  - not a randomizer
  - source/disassembly reference for Zelda 3

- `z3randomizer`
  - strong low-level patch layer
  - useful for understanding how ALTTP randomizer behavior gets injected into the ROM

- `alttp_vt_randomizer`
  - clear seed-generation and application layer
  - useful for understanding settings, build records, patch generation, and ROM output

- `ALttPDoorRandomizer`
  - strong logic/modeling layer for dungeon and door topology
  - useful for understanding richer world-state generation

- `RandomMetroidSolver`
  - explicit split between generation, solver, presets, and spoiler-path display
  - useful for seeing the Super Metroid side of logic and progression analysis

- `MapRandomizer`
  - strong reachability and room-connectivity model
  - useful for seeing how topology randomization changes the meaning of progression

- `SMZ3`
  - crossover seed-generation and patch pipeline across two base games
  - useful for understanding how multi-game logic and ROM emission are combined

## Why this matters for this workspace

If we want to build understanding for future game-dev ideas, randomizers are valuable because they expose:

- the game's dependency graph
- the designers' assumptions about progression
- what game state is safe to permute
- what must remain fixed for the game to stay completable

The topology-changing randomizers add one more useful design lens:

- what parts of the world's spatial graph can be rewritten while still preserving learnable, completable exploration

That makes them useful not only as hacks, but as machine-readable design analysis of the original games.
