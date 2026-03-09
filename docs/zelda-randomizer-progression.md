# Zelda Randomizer Progression Notes

This note captures the higher-level progression model used by the Zelda randomizer repos in this workspace.

## Core idea

These randomizers are not just shuffling items blindly.

They build a world that must remain logically completable:

- some locations are reachable at the start
- those locations yield items
- those items unlock more locations
- that unlock chain continues until the game can be beaten

At a concept level, this is a dependency graph over:

- items
- locations
- entrances or doors
- dungeon states
- mode and glitch assumptions

## Terminology

### Logic

In the Zelda randomizer ecosystem, `logic` is the main player-facing term for the reachability model.

Logic settings typically encode:

- what tricks are allowed
- whether glitches are in logic
- what counts as reachable
- what must be true for a seed to be considered valid

Examples visible in the current repos:

- `NoGlitches`
- `OverworldGlitches`
- `MajorGlitches`
- `NoLogic`
- door/key-specific logic variants

### Spoiler log

A spoiler log is the generated explanation of the seed.

It can include:

- item placements
- metadata and settings
- entrance/door mappings
- playthrough or progression data

In `alttp_vt_randomizer`, the spoiler output can be filtered based on spoiler mode, and it explicitly treats playthrough data as a separately removable section.

### Playthrough

In these repos, `playthrough` usually means a structured explanation of the required progression path through the generated seed.

It is not necessarily every item in the world. It is usually the items and steps needed to show how the seed is beatable.

### Spheres

`Spheres` are progression layers.

A sphere is a set of locations that become reachable with the items from all previous spheres.

That means:

- sphere 0 or sphere 1 is the start-accessible set
- later spheres are unlocked by earlier ones
- the sphere model is a human-readable approximation of the dependency order

This is one of the best abstractions in randomizer design because it turns a nonlinear game into a sequence of reachable frontiers.

## Repo-specific notes

### alttp_vt_randomizer

Relevant paths:

- `../repos/alttp_vt_randomizer/routes/console.php`
- `../repos/alttp_vt_randomizer/app/Support/WorldCollection.php`
- `../repos/alttp_vt_randomizer/app/EntranceRandomizer.php`

Observed structure:

- the app checks winnability before finalizing output
- it generates spoiler data from the world model
- spoiler output can include or omit playthrough information depending on settings
- the application stores logic and patch data alongside generated seed information

Interpretation:

- this repo treats spoiler/playthrough data as part of the formal generated artifact set, not just debugging output

### ALttPDoorRandomizer

Relevant paths:

- `../repos/ALttPDoorRandomizer/Main.py`
- `../repos/ALttPDoorRandomizer/DoorShuffle.py`
- `../repos/ALttPDoorRandomizer/Doors.py`

Observed structure:

- `create_playthrough(world)` explicitly constructs progression spheres
- it first gathers advancement-item locations
- it builds reachability spheres with current collected state
- it errors if required progression cannot be reached
- it then prunes spheres backward to reduce them to the minimum required path
- it rebuilds final spheres after pruning so the final spoiler walk is dependency-correct

This is a strong concrete implementation of the concept you described:

- not all randomized items matter equally
- the seed generator can derive the required chain of progression
- the spoiler/playthrough is a distilled explanation of that chain

Additional design note:

- this is not only an item randomizer
- it is also a world-structure randomizer
- door transitions and dungeon layout meaningfully change, so the player must learn a generated world graph rather than only a generated item graph

### SMZ3

Relevant paths:

- `../repos/SMZ3/Randomizer.SMZ3/Playthrough.cs`
- `../repos/SMZ3/Randomizer.SMZ3/Filler.cs`

Observed structure:

- `Playthrough.Generate()` constructs spheres across all worlds
- it repeatedly finds newly available locations from the currently owned item set
- it records only progression-relevant locations/items into the playthrough
- it throws if inaccessible items accumulate past a threshold, treating that as likely impossible
- it appends reward and medallion requirement data as an extra sphere-like output

Interpretation:

- the sphere model carries over cleanly into a multi-game randomizer
- the terminology is similar, but the content expands beyond item pickup into cross-game requirements and rewards

## Design takeaway

Randomizers expose the game's progression grammar.

For Zelda, that grammar is largely:

- item-gated exploration
- dungeon access conditions
- key logic
- mode/goal variants
- optionally entrance or door remapping

The spoiler log and playthrough are useful because they turn that grammar into a readable artifact.

That makes these repos valuable for more than romhacking:

- they are models of how the game's progression really works
- they encode what can safely be permuted
- they show which dependencies are fundamental and which are optional

## Relation to Metroid

The exact terminology may differ on the Super Metroid side, but the underlying idea is the same:

- some locations are gated by previous items or abilities
- a seed must preserve a valid unlock chain
- progression can still be analyzed as reachable frontiers or spheres, even if the community names them differently

So this Zelda note should transfer conceptually to Metroid work later, even if the terms change.
