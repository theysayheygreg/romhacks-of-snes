# Metroid Randomizer Progression Notes

This note captures the Super Metroid side of the same progression concepts used in the Zelda randomizer note.

## Core idea

The concept is the same as Zelda:

- some locations are reachable at the start
- those locations yield items or state changes
- those unlock more locations
- the seed remains valid only if a full progression path to completion exists

What changes more on the Metroid side is the vocabulary and the shape of the logic model.

## Repo-specific notes

### VARIA / RandomMetroidSolver

Relevant paths:

- `../repos/RandomMetroidSolver/randomizer.py`
- `../repos/RandomMetroidSolver/solver.py`
- `../repos/RandomMetroidSolver/logic/`
- `../repos/RandomMetroidSolver/rando/`

Observed structure:

- explicit `randomizer.py` and `solver.py`
- seed generation is configured through:
  - a vanilla ROM
  - a `randoPreset`
  - a skill preset via `--param`
  - optional explicit seed
- solver output can display a generated path with `-g`
- solver also exposes a pickup strategy and difficulty target
- randomizer options include `progressionSpeed`, `progressionDifficulty`, and `logic`

Interpretation:

- `logic` is still a first-class concept, but VARIA also emphasizes player capability through `skill presets`
- the `solver` is an explicit artifact, not just internal validation
- the generated path plays a role similar to spoiler/playthrough output in Zelda

This makes the Super Metroid terminology feel slightly different, but the underlying design is the same:

- model what the player can do
- generate a world
- solve that world under the chosen assumptions

### MapRandomizer

Relevant paths:

- `../repos/MapRandomizer/cpp/reachability.cpp`
- `../repos/MapRandomizer/rust/maprando-logic/`
- `../repos/MapRandomizer/rust/maprando-game/`
- `../repos/MapRandomizer/patches/`

Observed structure:

- seed generation is tied to randomized map pools and room connectivity
- there is an explicit `reachability` component
- the logic layer includes many notes about what is or is not "in logic"
- route information is updated for spoiler-log extraction in `reachability.cpp`
- the CLI can generate a seed directly from an input ROM and map JSON

Interpretation:

- this repo pushes harder on topology than item-placement-only randomizers
- progression depends not only on items and tricks, but on how rooms are connected
- the underlying abstraction is still reachable-state expansion over a constrained world graph

Additional design note:

- this is the Super Metroid-side analogue to Zelda Door Randomizer at a high level
- the randomizer is changing the explorable world structure itself, not only the item placements
- that adds an extra player challenge: learning the generated spatial layout while also solving progression

## Vocabulary alignment with Zelda

Closest conceptual mapping:

- Zelda `logic`
  - Metroid `logic`

- Zelda `playthrough`
  - Metroid `generated path` or solver path

- Zelda `spheres`
  - not always surfaced with the same terminology, but still conceptually reachable frontiers or layers

- Zelda `spoiler log`
  - Metroid spoiler/path/solver output

The names differ, but the dependency structure is the same.

## Important Metroid-specific emphasis

Compared to Zelda, the Metroid side appears to encode more of the player's physical execution assumptions directly:

- movement tricks
- route difficulty
- skill presets
- strategy videos and reachability caveats

That means the logic model is often closer to:

- "what can a player with this skill profile actually do?"

rather than only:

- "what items are owned?"

Both matter in Zelda too, but the Metroid repos make this dimension much more explicit.

## Design takeaway

For future game-design ideas, the Metroid randomizer ecosystem is useful because it exposes:

- item gating
- movement/trick gating
- route difficulty assumptions
- how world topology changes progression

So if Zelda randomizers teach us the dependency graph of inventory and dungeon access, Metroid randomizers add a stronger model of:

- player execution skill
- traversal graph shape
- route feasibility under different assumptions

And topology-changing variants like `MapRandomizer` make the traversal graph itself part of the randomized content.

That makes them especially valuable for any design work around exploration-driven action games.
