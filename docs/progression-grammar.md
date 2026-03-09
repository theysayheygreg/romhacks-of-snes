# Progression Grammar

This note describes the higher-level progression assumptions encoded by the randomizer ecosystems in this workspace.

## What "progression grammar" means

A game's progression grammar is the set of rules that determines:

- what counts as an unlock
- what kinds of gates exist
- how new space becomes reachable
- how the player learns what to do next

Randomizers are useful because they expose this grammar directly.

## Zelda progression grammar

At a high level, Zelda randomizers tend to assume progression is built from:

- item-gated checks
- dungeon access requirements
- key logic
- reward thresholds
- mode and glitch assumptions

The player experience is usually:

- explore known world
- find new item
- mentally re-evaluate known checks
- open a new region, dungeon, or reward path

This creates a grammar centered on:

- inventory expansion
- lock/key resolution
- location revisitation

The world is often legible even when the item graph changes.

## Metroid progression grammar

At a high level, Metroid randomizers assume progression is built from:

- item-gated traversal
- movement-technique gating
- room-to-room route feasibility
- survival/resource constraints
- player skill presets or trick assumptions

The player experience is usually:

- gain item or movement option
- reconsider route possibilities
- test traversal chains
- access a new area or sequence of rooms

This creates a grammar centered on:

- traversal capability
- execution difficulty
- graph reachability

Compared to Zelda, the world graph itself and the player's movement competence are much more central.

## Topology-randomizer grammar

Door randomizers and map randomizers add another layer:

- the world graph is itself unstable

The player experience becomes:

- learn the generated spatial graph
- learn the generated progression graph
- reconcile both while exploring

This grammar adds:

- navigation discovery
- mental remapping
- uncertainty about where transitions lead

So these seeds are not only "where is the item?" puzzles.
They are also "what is this world?" puzzles.

## Crossover progression grammar

`SMZ3`-style crossover randomizers have to merge multiple grammars at once.

That means the player may need to reason across:

- Zelda-style inventory locks
- Metroid-style traversal locks
- cross-game portals
- cross-game rewards
- cross-game pacing

The player experience becomes:

- acquire an unlock in one game
- realize it changes reachability in the other game
- bounce across multiple world models
- maintain a shared mental progression state

This is harder than either source grammar alone because the player is not just learning one rule system. They are learning the translation layer between two rule systems.

## Why this matters for design

These grammars are reusable design tools.

They suggest distinct game-design levers:

- inventory-graph remix
- traversal-graph remix
- world-topology remix
- multi-grammar crossover design

If your goal is future game ideas, randomizers are useful because they show how far each lever can be pushed before the game stops being readable or completable.

## Working taxonomy for this workspace

- Zelda randomizers:
  - strongest on item-graph and lock/key grammar

- Super Metroid randomizers:
  - strongest on traversal-skill and route-feasibility grammar

- Door/Map randomizers:
  - strongest on world-topology grammar

- `SMZ3`:
  - strongest on multi-grammar crossover design
