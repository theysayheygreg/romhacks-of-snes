# Super Metroid Deep Dive 01

This is the first practical reverse-engineering note for the Metroid lane.

It is not a full disassembly. The goal is to establish:

- how the vanilla game is structured for hacking purposes
- where the randomizer community anchors its logic and patching
- which ROM surfaces are stable enough for first experiments

This note now has a canonical source-reference companion:

- `../../repos/supermetroid`

That repository matches the local ROM exactly by SHA-1 and should be treated as the vanilla/source lane for this game.

## Anchor ROM facts

Reference ROM:

- `../../roms/base/Super Metroid (Japan, USA) (En,Ja).sfc`

Verified facts:

- mapping: `LoROM`
- speed: `FastROM`
- file size: `0x300000` bytes (`3 MiB`)
- declared ROM size in header: `0x400000` bytes (`4 MiB`)
- SRAM declaration: `0x2000` bytes (`8 KiB`)
- native reset vector: `80:841C`
- reverse symbol match in VARIA symbol dump: `80:841C = Boot`
- exact-match source lane available locally: `repos/supermetroid`
- exact-match source-lane SHA-1: `da957f0d63d14cb441d215462904c4fa8519c613`

Implication:

- this is a LoROM game with a large amount of banked content and an existing community convention of referring to major structures by SNES bank names like `bank_83`, `bank_84`, `bank_8B`, and `bank_8F`

## Practical ROM model

The local source trees suggest a three-layer working model.

### 1. Gameplay graph layer

This is the player-facing progression model:

- areas
- access points
- item locations
- boss/event gates
- movement and trick assumptions

Best local source:

- `RandomMetroidSolver/graph/vanilla/graph_access.py`
- `RandomMetroidSolver/graph/vanilla/graph_locations.py`
- `SMZ3/Randomizer.SuperMetroid/Regions/`

This layer treats the game as a directed graph:

- nodes: rooms, area transitions, item locations
- edges: requirements to traverse
- requirements: items, ammo, heat tolerance, movement tech, boss state

### 2. ROM-address layer

This is the hacking surface:

- room pointers
- door pointers
- PLM item locations
- patch-owned tables
- metadata fields used by randomizers

Best local source:

- `RandomMetroidSolver/patches/common/sym/*.json`
- `RandomMetroidSolver/patches/vanilla/sym/bank_8f.json`
- `SMZ3/Randomizer.SuperMetroid/Patch.cs`

### 3. Patch pipeline layer

This is how modern hacks/randomizers actually modify the game:

- apply IPS/BPS/Asar patches
- rewrite item PLMs at known offsets
- inject new tables into reserved ROM space
- redirect door or startup behavior through patch-owned routines

Best local source:

- `RandomMetroidSolver/rom/rom_patches.py`
- `RandomMetroidSolver/patches/common/src/`
- `SMZ3/Randomizer.SuperMetroid/Patch.cs`
- `MapRandomizer/python/rando/`

## Vanilla progression grammar

Super Metroid progression is not just "item X unlocks door Y". It is a compound grammar:

- inventory gates
- movement-tech gates
- environmental-damage gates
- boss/event gates
- room-topology knowledge

### Inventory gates

Core examples:

- `Morph` opens early tunnel-scale progression
- `Missile` / `Super` / `PowerBomb` map directly to red, green, and yellow door families
- `SpeedBooster`, `Grapple`, `SpaceJump`, `HiJump`, `Ice`, `Varia`, `Gravity` all unlock distinct route classes rather than only single checks

### Technique gates

The logic layer treats player execution as first-class:

- mockball
- bomb jump / infinite bomb jump
- short charge
- gate glitches
- suitless traversal
- wall jump and shinespark routes

This is the biggest conceptual difference from Zelda logic. Metroid logic is much more explicit about what the player can physically perform.

### Environmental gates

The helpers layer encodes damage and survivability as logic, not just flavor:

- heat runs
- acid/lava traversal
- hard rooms
- lower Norfair crystal-flash expectations

Representative source:

- `RandomMetroidSolver/logic/helpers.py`
- `MapRandomizer/sm-json-data/logicalRequirements.md`

That means the progression model is partly geometric and partly resource-economic.

## Concrete ROM anchors

These are the most useful low-level anchors pulled from the current local sources.

### Startup and randomizer-owned metadata

From `RandomMetroidSolver/patches/common/sym/`:

- `start_location = 0xA1F200`
- `startup = 0xA1F220`
- `starting_energy = 0xA1F470`
- `timer_value = 0x809E21`
- `timer_values_by_area_id = 0xA1F0D0`
- `plm_lists = 0x8FE9BF`
- `room_plms_upwards = 0x8FF000`
- `scav_order = 0xA1F560`
- `InfoStr = 0x82FB6C`

Interpretation:

- bank `A1` is a major patch-owned control region in the VARIA ecosystem for startup, start-state, escape data, and HUD-adjacent randomizer metadata
- bank `8F` is a major room/PLM table bank and a prime place to look for item placement and room-local patching

### Representative room pointers from vanilla access graph

From `RandomMetroidSolver/graph/vanilla/graph_access.py`:

- `Lower Mushrooms Left`: room pointer `0x9969`
- `Morph Ball Room Left`: room pointer `0x9E9F`
- `Green Hill Zone Top Right`: room pointer `0x9E52`
- `PhantoonRoomOut`: room pointer `0xCC6F`
- `Wrecked Ship Main`: room pointer `0xCC6F`
- `Lava Dive Right`: room pointer `0xAF14`

Why these matter:

- the access graph is already bridging gameplay logic to concrete room IDs
- that makes it a usable lookup layer when we want to map a gameplay concept back to ROM data

### Representative item PLM write targets

From `SMZ3/Randomizer.SuperMetroid/Regions/` and `Patch.cs`, these are written as direct ROM offsets:

- `Bombs = 0x78404`
- `Morphing Ball = 0x786DE`
- `Power Bomb (blue Brinstar) = 0x7874C`
- `Reserve Tank, Wrecked Ship = 0x7C2E9`

Important detail:

- `SMZ3` writes item PLMs directly with `patches.Add(location.Address, GetSMItemPLM(location))`
- that means these offsets are stable and already trusted by an active randomizer codebase as patch surfaces

## What bank 8F appears to mean in practice

The local evidence strongly suggests that `8F` is one of the most important banks for room-local hacking:

- room/item symbols in `patches/vanilla/sym/bank_8f.json`
- room-local item addresses in `graph_locations.py`
- door/PLM editing in VARIA mirror patches
- `SMZ3` combo patching writing door/keycard data into `0x8F0000 + ...`

Practical inference:

- when we want to alter item placements, room-local PLMs, door data, or per-room patch structures, `8F` is one of the first banks to inspect

## How the current repos divide the problem

### VARIA / RandomMetroidSolver

Best viewed as four connected subsystems:

- graph definitions
- logic helpers and presets
- symbol-aware ROM patching
- higher-level seed/solver/customizer workflow

This repo is valuable because it does not just randomize items. It exposes how the community operationalizes:

- room graph structure
- trick assumptions
- damage economics
- patch composition

### MapRandomizer

Best viewed as the topology-heavy lane:

- explicit logical requirements
- room geometry and map data
- room connection randomization
- reachability engine

This is where the world graph itself becomes editable, not just the reward graph.

### SMZ3 Super Metroid side

Best viewed as the minimal patch emitter:

- region list
- location list
- direct ROM write targets
- seed data tables

This repo is valuable because it strips the problem down to:

- what locations exist
- what logic unlocks them
- what bytes need to change in the ROM

## First patch targets

These are the safest-looking early targets from the current source base.

### 1. Startup configuration patching

Addresses:

- `0xA1F200` `start_location`
- `0xA1F220` `startup`
- `0xA1F470` `starting_energy`

Why first:

- high leverage
- already isolated by community patch code
- easy to verify behaviorally

### 2. Escape timer patching

Addresses:

- `0x809E21` active timer value
- `0xA1F0D0` timer values by area

Why first:

- easy to observe in-game
- low ambiguity
- useful bridge between gameplay and patch-owned data

### 3. Single-item PLM replacement

Example offsets:

- `Bombs = 0x78404`
- `Morphing Ball = 0x786DE`

Why first:

- this is the core randomizer operation
- already validated by `SMZ3`
- simple to diff and reason about

### 4. HUD / seed metadata writes

Addresses:

- `0x82FB6C` `InfoStr`
- `0xA1F560` `scav_order`

Why first:

- high visibility
- useful for proving we can inject new state without changing traversal logic yet

## Working conclusions

The important structural fact is that Super Metroid reverse engineering in practice is already organized around:

- a gameplay graph
- a symbol map
- patch-owned ROM regions
- a small set of trusted room/item write points

That means we do not need a full vanilla disassembly before making useful progress.

The next Metroid passes should probably be:

1. turn this note into a cleaner vanilla progression note
2. isolate 3-5 concrete item/door/startup edits into a patch-target sheet
3. produce one standalone Super Metroid ROM artifact with a deliberately small patch
