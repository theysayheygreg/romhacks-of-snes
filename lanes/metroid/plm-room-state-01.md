# Super Metroid PLM and Room State 01

This note is the first canonical pass on PLMs and room-state structure in the Metroid lane.

It is based on:

- local exact-match source lane material in `../../repos/supermetroid`
- local patch/model code in `../../repos/RandomMetroidSolver`
- local topology/randomizer material in `../../repos/MapRandomizer`
- secondary-source intake from `../../docs/external-research/gemini-metroid-plm-deep-dive-001.md`

The goal is to keep the structural model that is strongly supported by local sources, while avoiding overcommitting to engine details that still need direct tracing.

## Core model

Super Metroid room behavior appears to split cleanly into two major layers:

- room and state data in bank `8F`
- PLM execution and definitions in bank `84`

That matches both:

- the local exact-match disassembly structure
- the randomizer community’s patch surfaces

## What bank `84` appears to own

From the local exact-match source lane:

- `../../repos/supermetroid/src/bank84.asm`

Bank `84` is clearly one of the core interactivity banks.

The comments and routine labels in that file repeatedly point at:

- spawning PLMs
- enabling/disabling/clearing PLMs
- handling PLMs
- processing PLM draw instructions
- drawing PLM blocks
- item PLM graphics loading

Representative comment anchors in the local source:

- `Spawn hard-coded PLM`
- `Spawn room PLM`
- `Spawn PLM`
- `PLM handler`
- `Process PLM`
- `Process PLM draw instruction`
- `Draw PLM`

Even before deeper tracing, that is enough to justify this working interpretation:

- bank `84` is a central execution and data bank for room-local interactive objects

## What PLMs appear to be

The most useful practical model is:

- PLMs are room-local interactive objects with data and behavior

From local sources, PLMs clearly cover at least:

- item pickups
- door-related behavior
- room-local blockers and crumble behavior
- scroll or camera-affecting room-local behavior

Why this model is strong:

- `RandomMetroidSolver/rom/leveldata.py` has explicit `PLM`, `PLMItem`, and `PLMDoor` classes
- `RandomMetroidSolver/rom/rompatcher.py` has explicit `applyPLMs` logic and writes PLM spawn tables
- the exact-match source lane puts the PLM execution machinery in bank `84`

So even without full runtime tracing yet, the workspace can already treat PLMs as one of the primary mod surfaces for:

- item placement
- door logic and door indicators
- room-local interactivity

## What bank `8F` appears to own

From the existing Metroid deep dive and local randomizer symbols:

- `../../analysis/super-metroid-key-symbols.json`
- `../../repos/RandomMetroidSolver/patches/vanilla/sym/bank_8f.json`
- `../../repos/RandomMetroidSolver/rom/leveldata.py`

Bank `8F` appears to be one of the main room-data banks.

The current local evidence strongly supports this interpretation:

- room pointers and room-local symbols live here
- room PLM set pointers are modeled against room/state structures here
- randomizers already treat `8F` as a core room-local patch bank

The existing workspace anchors still hold:

- `plm_lists = 0x8FE9BF`
- `room_plms_upwards = 0x8FF000`

So the practical working split is:

- `8F` = room/state/local data structures
- `84` = PLM execution/definitions/instruction behavior

## Room states

The local patch/model code shows that room states are not just a theoretical concept.

In:

- `../../repos/RandomMetroidSolver/rom/leveldata.py`

the code explicitly:

- loads state headers
- logs state-header addresses and header types
- loads PLMs associated with those states
- writes state headers and PLMs back out

That is enough to treat room-state structure as a real editable surface, not just documentation lore.

Practical implication:

- a room is not just one static layout
- room-local behavior can vary by state
- PLM data is tied to room/state structure rather than existing as an isolated object list

This matters because it explains why randomizer and hack tooling often have to think in tuples closer to:

- room
- state
- door or local transition context

not just:

- room ID

## What this means for randomizers

The local repos split responsibilities in a useful way.

### RandomMetroidSolver

Best viewed as:

- logic graph and solver layer
- room/state/PLM serialization layer
- patch composition layer

Important local evidence:

- `rompatcher.py` applies PLMs as structured entries
- PLMs are grouped against room/state keys
- `leveldata.py` explicitly loads and writes state headers and PLMs

Interpretation:

- item randomization and room-local patching are already modeled as structured data edits, not just blind hex writes

### MapRandomizer

Best viewed as:

- topology-heavy layer that still depends on the same room/PLM foundation

Important local evidence:

- `sm-json-data` is present in the repo
- room exports include explicit `<PLMs>` sections
- title-screen and room export tooling preserve PLM structure as first-class data

Interpretation:

- topology randomization still sits on top of the room/state/PLM substrate
- changing the map graph does not remove the need to understand bank `84` and bank `8F`

## Current strongest local references

For future Metroid work in this workspace, the most important local files around PLMs and room states are:

- `../../repos/supermetroid/src/bank84.asm`
- `../../repos/RandomMetroidSolver/rom/leveldata.py`
- `../../repos/RandomMetroidSolver/rom/rompatcher.py`
- `../../repos/RandomMetroidSolver/patches/vanilla/sym/bank_8f.json`
- `../../repos/MapRandomizer/sm-json-data/`

## What is still not fully settled

These parts still deserve direct source tracing or debugger confirmation before we treat them as fully canonical:

- exact PLM runtime slot counts and frame-loop mechanics
- exact room-state evaluation ordering under all conditions
- exact RAM event-bit ranges and how they map onto every room-state transition
- which community descriptions are exact engine truth versus editor/randomizer convention

So this note should be treated as:

- a strong first structural model
- not the final word on the runtime loop

## Best next tasks

1. Trace one concrete item PLM from room/state data into runtime handling.
2. Trace one door PLM from room data into transition behavior.
3. Use `RandomMetroidSolver/rom/leveldata.py` to map one real room’s state headers and PLM set pointers.
4. Compare the exact-match `strager/supermetroid` lane with `sm_disassembly` if we add it, specifically for PLM and room-state authoring workflows.
