# SMZ3 Case Study

The canonical repo in this workspace is:

- `../repos/SMZ3`

This is a strong example because it is not just "a patch". It is a structured pipeline that:

- models world logic in high-level code
- emits binary patch payloads
- combines two commercial base ROMs into one final SNES image
- adds new mechanics, portals, UI, and progression rules

It also represents the broader romhacking pattern you called out:

- begin with canonical base ROMs
- keep the original games as binary inputs
- generate targeted patches and transformed data
- produce a new ROM as the output artifact

That is different from a pure reverse-engineering goal where the main objective is recreating source from scratch.

For Zelda lineage in this workspace, it is useful to treat `SMZ3` as downstream of at least two related reference styles:

- `../repos/z3randomizer`: closer to the direct ALTTP assembly patch layer
- `../repos/alttp_vt_randomizer`: closer to the higher-level randomizer application/service layer
- `../repos/ALttPDoorRandomizer`: closer to the Python modeling/logic-heavy dungeon-randomizer layer

For Super Metroid lineage in this workspace, the closest reference styles now look like:

- `../repos/RandomMetroidSolver`: explicit randomizer/solver/tracker model
- `../repos/MapRandomizer`: topology and reachability-heavy randomizer model

Useful distinction:

- `SMZ3` appears primarily in the item/progression randomizer family
- `ALttPDoorRandomizer` and `MapRandomizer` represent a more topology-changing family

That matters because the latter are changing the world graph itself, which is a deeper kind of procedural design pressure than simple item shuffling.

## What the code does

The most important local files are:

- `../repos/SMZ3/Randomizer.CLI/Verbs/GenSeed.cs`
- `../repos/SMZ3/Randomizer.CLI/FileData/Rom.cs`
- `../repos/SMZ3/Randomizer.SMZ3/Patch.cs`
- `../repos/SMZ3/WebRandomizer/ClientApp/src/resources/markdown/smz3information.md`

From the current source:

- the CLI expects base ROM filenames:
  - `Super_Metroid_JU_.sfc`
  - `Zelda_no_Densetsu_-_Kamigami_no_Triforce_Japan.sfc`
- `CombineSMZ3Rom()` allocates a `0x600000` byte output ROM
- it lays Super Metroid into the first `0x400000` bytes using bank-aware placement
- it lays Zelda 3 into the upper region beginning at `0x400000`
- it applies an IPS base patch
- it applies generated seed patches
- it can apply additional IPS patches and RDC resources before writing the final `.sfc`

## Why it matters architecturally

`SMZ3` demonstrates a pattern we should reuse for future SNES work:

- separate game logic from binary patch emission
- treat ROM layout as an explicit memory-allocation problem
- keep generated patches as data structures, not ad hoc hex edits
- make the final build step deterministic

The project also shows how new mechanics get layered in:

- cross-game portals
- shared progression
- boss-token logic
- keycard systems in `Keysanity`
- in-game UI indicators for the new rule set

That is exactly the class of work you described: using reverse engineering to create new design spaces rather than only restoring or translating an original game.

## Lessons for future hacks

- Start with a bank map before writing patches.
- Keep a reproducible base-ROM preparation step.
- Keep gameplay logic in a high-level representation where possible.
- Emit patches late.
- Validate both emulator behavior and flashcart behavior, because a merged ROM is more likely to hit mapper and compatibility edges.
