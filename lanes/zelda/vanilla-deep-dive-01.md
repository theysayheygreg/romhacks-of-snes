# Zelda 3 Deep Dive 01

This is the first practical reverse-engineering note for the Zelda lane.

The goal is to establish:

- how the exact local ALTTP JP1.0 ROM is structured for hacking purposes
- how `jpdasm` and the patch-first randomizer ecosystem fit together
- which WRAM/SRAM and ROM surfaces are stable enough for first experiments

## Anchor ROM facts

Reference ROM:

- `../../roms/base/Zelda no Densetsu - Kamigami no Triforce (Japan).sfc`

Verified facts:

- mapping: `LoROM`
- speed: `SlowROM`
- file size: `0x100000` bytes (`1 MiB`)
- declared ROM size in header: `0x100000` bytes (`1 MiB`)
- SRAM declaration: `0x2000` bytes (`8 KiB`)
- native reset vector: `80:8000`
- internal checksum pair: `CDC8 / 3237`
- SHA-1: `e7e852f0159ce612e3911164878a9b08b3cb9060`
- MD5: `03a63945398191337e896e5771f77173`

Important result:

- `jpdasm` states those same hashes in its README
- so `jpdasm` is a revision-matched vanilla/source lane for the exact local ROM, not just a related disassembly

## Practical ROM model

Zelda 3 in this workspace now has two complementary lanes:

### 1. Vanilla/source lane

Best local source:

- `jpdasm/main.asm`
- `jpdasm/bank_00.asm` through `jpdasm/bank_1F.asm`
- `jpdasm/symbols_wram.asm`
- `jpdasm/symbols_sram.asm`
- `jpdasm/values.asm`

This is the banked source-reference view of the original game.

### 2. Patch-first lane

Best local source:

- `z3randomizer/LTTP_RND_GeneralBugfixes.asm`
- `z3randomizer/hooks.asm`
- `z3randomizer/tables.asm`
- `z3randomizer/ram.asm`
- `z3randomizer/sram.asm`

This is the modern romhacking/randomizer view:

- hook key routines
- allocate new config/data tables
- write into WRAM/SRAM-aware systems
- emit a modified ROM from a canonical base ROM

## Vanilla source structure

`jpdasm` organizes the ROM cleanly:

- `main.asm` includes `bank_00.asm` through `bank_1F.asm`
- `symbols_wram.asm` documents runtime memory
- `symbols_sram.asm` documents save data
- `values.asm` provides semantic enums like dungeon IDs, overworld screens, and sprite IDs

That gives us a clean split:

- ROM code/data by bank
- runtime state in WRAM
- persistent state in SRAM

## Runtime memory model

The most important immediate Zelda distinction versus Metroid is that a lot of practical state is already human-readable in `jpdasm`.

### WRAM

Best canonical source:

- `jpdasm/symbols_wram.asm`

Representative anchors:

- `MODE = $7E0010`
- `SUBMODE = $7E0011`
- `LAG = $7E0012`
- `FRAME = $7E001A`
- `INDOORS = $7E001B`
- `POSY = $7E0020`
- `POSX = $7E0022`
- `LDIR = $7E002F`

This is useful because `jpdasm` gives semantic names to core game-loop and player-state memory immediately, rather than forcing us to infer them from hooks later.

### SRAM / save image

Best canonical source:

- `jpdasm/symbols_sram.asm`

Important structural facts:

- save files live in SRAM bank `$70`
- file 1 main copy starts at `$700000`
- file 2 main copy starts at `$700500`
- file 3 main copy starts at `$700A00`
- each file also has a mirrored backup copy
- active save data is copied into WRAM at `$7EF000`

Representative persistent-state anchors:

- room flags begin at `RMFLG000 = $7EF000`
- room flags are two bytes per room
- the room-flag bits encode doors, boss kill/heart container, keys, chest state, and visited quadrants

This is one of the most important Zelda hacking facts in the whole workspace: dungeon and room progression are already normalized into a compact room-flag table.

## Patch-first memory model

`z3randomizer` explicitly builds on `jpdasm`-style understanding rather than replacing it.

Its RAM/SRAM labels even say so:

- `z3randomizer/ram.asm` points back to `jpdasm/symbols_wram.asm`
- `z3randomizer/sram.asm` re-documents save structures for patching and asserts addresses

High-value patch-oriented anchors:

- `RoomDataWRAM = $7EF000`
- `OverworldEventDataWRAM = $7EF280`
- `InventoryTracking = $7EF38C`
- `ProgressIndicator = $7EF3C5`
- `CurrentWorld = $7EF3CA`
- `FollowerIndicator = $7EF3CC`

These matter because they are exactly the kinds of values randomizers and hacks manipulate:

- world state
- follower state
- inventory state
- dungeon/overworld completion state
- pre-/post-Zelda / pre-/post-Agahnim progression

## Progression grammar

Zelda 3 progression is more inventory- and state-graph-centric than Metroid.

The main grammar is:

- overworld access state
- dungeon item state
- room/event flags
- NPC/follower state
- world-state progression

### Overworld grammar

Key axes:

- Light World vs Dark World
- overworld screen events
- entrance structure
- bridge/overlay/bomb-wall state

Patch-facing anchor:

- `OverworldEventDataWRAM = $7EF280`

### Dungeon grammar

Key axes:

- room flags
- small keys
- big keys
- map/compass state
- boss completion flags

Patch-facing anchors:

- `RoomDataWRAM = $7EF000`
- `CurrentSmallKeys`
- per-dungeon small-key counters
- `CompassField`, `BigKeyField`, `MapField`

### Global story grammar

Key axis:

- `ProgressIndicator`

From `z3randomizer/sram.asm`:

- `$00 = Pre-Uncle`
- `$01 = Post-Uncle item`
- `$02 = Zelda rescued`
- `$03 = Agahnim 1 defeated`

That single byte is one of the cleanest examples of Zelda’s progression grammar being far more macro-state driven than Metroid’s.

## Concrete ROM anchors

### Vanilla/source anchors

From `jpdasm`:

- `main.asm` uses `lorom`
- banks are split into `bank_00.asm` through `bank_1F.asm`
- `symbols_wram.asm` is the canonical runtime symbol map
- `symbols_sram.asm` is the canonical save/persistent-state symbol map
- `values.asm` is the easiest way to map IDs to game concepts quickly

### Patch-first hook anchors

From `z3randomizer/hooks.asm`:

- init hook at `80:802F`
- frame hook at `80:8056`
- NMI hook at `80:80CC`
- anti-ZSNES check hook at `80:8023`

These are high-value because they show exactly where a modern patch pipeline starts intercepting the vanilla engine.

### Config table anchors

From `z3randomizer/tables.asm`:

- `SpriteItemValues` at `PC 0x180010`
- `DiggingGameRNG` at `PC 0x180020`
- `MireRequiredMedallion` at `PC 0x180022`
- `TRockRequiredMedallion` at `PC 0x180023`
- `MapMode` at `PC 0x18003B`
- `HUDDungeonItems` at `PC 0x180045`
- `RomSpeed` at `PC 0x187032`

This is the clearest practical patch surface in the Zelda ecosystem here:

- a high-bank config/data table area for randomizer-owned behavior

### ROM-header / cartridge-shape anchors

From `z3randomizer/LTTP_RND_GeneralBugfixes.asm`:

- SRAM size header byte patched at `80:FFD8`

From `z3randomizer/tables.asm`:

- `RomSpeed` controls FastROM/SlowROM behavior in the patch-owned config area

This matters because the patch-first ecosystem is not only changing game logic; it is also changing cartridge/runtime assumptions.

## How the current repos divide the problem

### jpdasm

Best viewed as:

- exact vanilla source reference
- symbolic WRAM/SRAM documentation
- bank-by-bank code and data inspection surface

### z3randomizer

Best viewed as:

- low-level patch payload and hook lane
- randomizer-owned config table lane
- practical ASM-first hacking lane

### alttp_vt_randomizer / ALttPDoorRandomizer

Best viewed as:

- seed-generation and higher-level world-logic lanes

Those repos are less useful for raw vanilla memory truth and more useful for generated-world and logic behavior.

## First patch targets

These are the safest-looking first experiments from the current source base.

### 1. Config-table edits

Examples:

- `DiggingGameRNG`
- `MireRequiredMedallion`
- `TRockRequiredMedallion`
- `MapMode`
- `HUDDungeonItems`

Why first:

- isolated
- easy to diff
- already designed as patch-owned data knobs

### 2. Progress/state initialization

Examples:

- `ProgressIndicator`
- `StartingEntrance`
- static file-name behavior in `initsramtable.asm`

Why first:

- high leverage
- visible quickly
- low ambiguity if the patch is small

### 3. File-select / menu layer

Evidence:

- significant patching in `hooks.asm`
- `fileselect.asm`
- `FileSelectPosition`

Why first:

- visible immediately at boot
- less likely to create deep dungeon softlocks than room logic edits

### 4. Room and overworld state bits

Examples:

- `RoomDataWRAM`
- `OverworldEventDataWRAM`

Why first:

- central to progression
- but slightly higher risk than pure config-table edits, because these can create state inconsistencies if changed carelessly

## Working conclusions

The most important practical Zelda fact is that the exact local ROM already has:

- a canonical vanilla/source lane in `jpdasm`
- a canonical patch-first lane in `z3randomizer`

So we do not need to choose between “understand the original game” and “understand how hacks are made.” The workspace now has both.

The next Zelda passes should probably be:

1. turn this into a cleaner Zelda progression-grammar note
2. make a short patch-target sheet from the config table area around `0x180000`
3. produce one standalone Zelda ROM artifact with a deliberately small patch
