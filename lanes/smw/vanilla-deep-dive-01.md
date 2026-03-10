# SMW Vanilla Deep Dive 01

This is the first anchor note for the Super Mario World lane.

It is based on:

- `../../roms/base/Super Mario World (USA).sfc`
- `../../analysis/super-mario-world-usa-rom.json`
- `../../analysis/super-mario-world-key-symbols.json`
- `../../repos/SMWDisX`
- `../../repos/SMWDisX/SMW_U.sym`

## ROM anchor

Current local base ROM facts:

- mapper: `LoROM`
- speed: `SlowROM`
- file size: `524288` bytes
- native reset vector: `80:8000`
- checksum pair in header is internally valid

This gives SMW a much smaller initial image than Super Metroid or a merged project like `SMZ3`, but it still has a large amount of mutable runtime state in WRAM and SRAM.

## Source lane status

`SMWDisX` is the canonical source/reference lane for this workspace right now.

Important distinction versus the Zelda and Metroid lanes:

- `jpdasm` and `strager/supermetroid` are exact-match single-revision anchors
- `SMWDisX` is multi-version by design

So the current safe statement is:

- the staged local ROM is a strong SMW U anchor for this lane
- `SMWDisX` clearly supports that U lane
- exact bit-perfect rebuild parity against the local ROM is still unverified in this workspace

## High-level engine shape

The main control surface is the game-mode state machine:

- `RunGameMode` at `00:9322`
- `GameMode` WRAM byte at `7E:0100`

`bank_00.asm` shows a direct dispatch table from `GameMode` to the current major engine state, including:

- title flow
- file-select flow
- overworld flow
- level flow
- game-over / cutscene transitions

This is the first big structural difference from Zelda and Metroid:

- Zelda progression is item/state-heavy across a persistent world
- Metroid progression is item/traversal-heavy across a room graph
- SMW progression is strongly mode-based and route-based, switching between overworld and authored levels

## Key memory anchors

Useful WRAM anchors from `rammap.asm` and `SMW_U.sym`:

- `7E:0013` `TrueFrame`
- `7E:0014` `EffFrame`
- `7E:0019` `Powerup`
- `7E:0100` `GameMode`
- `7E:0DB4` `SavedPlayerLives`
- `7E:0DBE` `PlayerLives`
- `7E:0FBE` `Map16Pointers`
- `7E:13BF` `TranslevelNo`
- `7E:1DEA` `OverworldEvent`
- `7E:1F49` `SaveDataBuffer`

Useful SRAM anchors:

- `70:0000` `SaveData`
- `70:008C` `SaveDataExitCount`
- `70:008D` `SaveDataChecksum`
- `70:01AD` `SaveDataBackup`

These addresses show what matters most in SMW:

- engine mode
- player-state continuity
- overworld progression
- level identity
- Map16/tile mutation
- compact save-file state

## Design interpretation

The progression grammar is not mostly “find the right item” like Zelda or “perform the right traversal sequence” like Super Metroid.

It is closer to:

- clear authored challenges
- unlock overworld movement and events
- branch through exits and secret exits
- carry player-state and file-state across levels

That means the most important low-level mod surfaces are usually not just player physics or item flags.
They are:

- level identity and exit routing
- overworld reveal/event state
- Map16 mutation and tile behavior
- save-file serialization
- mode transitions between title, overworld, and level play

## Safe first patch surfaces

Current low-risk to medium-risk surfaces:

- `00:FFC0`
  - internal ROM title
  - safest possible patch-first validation surface
- `00:18E4`
  - life-award logic
  - narrow gameplay effect
- `00:9322`
  - game-mode dispatch
  - high leverage, higher risk
- `00:96AE`
  - title-screen load path
  - likely useful later for custom boot/title experiments
- `00:9F06`
  - save initialization
  - useful later for default-state or challenge-mode starts

## Current practical read

SMW already looks like the most “toolchain-shaped” of the three anchor games:

- vanilla engine understanding comes from `SMWDisX`
- project authoring often lives in Lunar Magic and related inserters
- reproducible builds want a Callisto-style orchestration layer

So the SMW lane should be treated less like “just patch a ROM” and more like:

- engine/source reference
- editor/export workflow
- orchestrated rebuild pipeline

## Next steps

1. Produce a tiny standalone SMW ROM artifact with a patch-first workflow.
2. Validate `smw-project-template` as the current template/starter lane.
3. Add a second deep-dive note focused on:
   - overworld route state
   - exits and secret exits
   - Map16 and tile mutation
