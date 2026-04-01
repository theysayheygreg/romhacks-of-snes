# TAS Harnesses Note 01

This note captures the most useful TAS and TAS-adjacent harnesses for the current SNES anchor lanes.

The reason this matters for the workspace is simple:

- TAS tooling already knows how to drive a game frame by frame
- TAS tooling usually exposes RAM, savestates, and movie input files
- that makes it useful not just for showcase runs, but for automated smoke tests, deterministic repro cases, and patch validation

## What counts as a useful harness here

For this workspace, a useful harness is any stack that gives us some combination of:

- deterministic frame-accurate input playback
- Lua or scriptable emulator control
- RAM inspection or state overlays
- movie files that can be replayed across patched ROM revisions
- automated launch / sync workflows
- real-hardware or FX Pak Pro-adjacent memory interfaces

That means some tools are "pure TAS" and some are better described as TAS-adjacent automation.

## Cross-game baseline

The recurring emulator layer is:

- `BizHawk`
- `lsnes`
- older rerecording emulators like `snes9x-rr`

Those matter because the per-game harnesses usually live on top of them as:

- Lua overlays
- RAM watches
- movie files
- practice-hack instrumentation

## Super Mario World

Most useful leads:

- `brunovalads/smw-stuff`
  - GitHub: https://github.com/brunovalads/smw-stuff
  - This includes a large `SMW-Utils-Script-Snes9x.lua` script for emulator-assisted SMW analysis and utility work.
- TASVideos / BizHawk multi-instance orchestration example from Masterjun
  - Topic: https://tasvideos.org/Forum/Topics/22544
  - This is not a reusable library by itself, but it is a strong proof that SMW can be driven by external scripts across multiple emulator instances with synchronized savestate/input control.

Why SMW looks promising:

- SMW is a mature TAS game with well-understood frame rules.
- The Masterjun writeup explicitly describes using BizHawk sockets, external Python orchestration, synchronized frame advance, savestates, and RAM edits.
- That is very close to the kind of smoke-test harness we would want for patched ROMs.

Best near-term use for this workspace:

- deterministic title-to-level boot checks
- replaying short curated movie segments across patched ROMs
- verifying that a patch did not break level entry, overworld state, or specific movement setups

## Super Metroid

Most useful leads:

- `PJBoy/lua`
  - GitHub: https://github.com/PJBoy/lua
  - This is the strongest immediately useful Super Metroid script stack found in this pass.
  - The README explicitly calls out:
    - `Super Metroid.lua`
    - `Super Hitbox.lua`
    - `Super Hitbox + TAS.lua`
    - `Super Camhack.lua`
    - `Super charge shinespark.lua`
    - `smz3.lua`
  - It supports multiple emulators, including `snes9x-rr`, `BizHawk`, `Mesen`, and `lsnes`.
- Super Metroid Practice Hack
  - Site: https://smpractice.speedga.me/
  - Source: https://github.com/tewtal/sm_practice_hack/
  - This is not a TAS movie harness by itself, but it is a powerful instrumentation and setup stack for controlled practice and debugging.
- Super Metroid TAS references
  - Wiki: https://wiki.supermetroid.run/Tool_Assisted_Speedruns
  - The page confirms a real long-lived tool chain around `lsnes` and older rerecording emulators for published SM TAS work.

Why Super Metroid is the strongest TAS-harness lane:

- It has a real script ecosystem, not just movie files.
- It already exposes hitboxes, doors, room data, enemy state, and TAS-facing overlays.
- It is close to what we want for hack validation:
  - can Samus spawn?
  - can the room load?
  - can a door transition complete?
  - does a short movement script still work?

Best near-term use for this workspace:

- room-load and door-transition smoke tests
- item and PLM regression checks
- movement-tech validation against patched rooms
- SMZ3 crossover validation on the Super Metroid side

## Zelda 3 / A Link to the Past

The ALTTP picture is weaker if the bar is "dedicated TAS harness repo", but still strong if the bar is "automation-ready deterministic interface".

Most useful leads:

- `alttpo/sni`
  - GitHub: https://github.com/alttpo/sni
  - SNI is not a TAS runner. It is a Super Nintendo Interface for emulators and devices, including FX Pak Pro / SD2SNES-class hardware and Lua-bridge-compatible emulators.
  - For this workspace, that makes it one of the strongest candidates for automation and hardware-aware smoke tests.
- `ArchipelagoMW/Archipelago`
  - GitHub: https://github.com/ArchipelagoMW/Archipelago
  - This is not a TAS tool either, but it proves there is already a mature automation/control ecosystem for ALTTP, Super Metroid, SMW, and SMZ3-like crossover cases.
  - Architecturally, it matters because it already expects emulator/hardware-side state synchronization and deterministic world logic.

Why ALTTP is still promising:

- Even if the public "pure TAS harness" repo picture is thinner than Super Metroid, ALTTP has serious state/control tooling around randomizer automation, autotracking, and emulator/hardware interfaces.
- That may be more valuable to this workspace than a traditional TAS overlay if the actual goal is "does this modified ROM still behave correctly?"

Best near-term use for this workspace:

- memory/state observation for key progression flags
- deterministic launch-and-check workflows against emulator or FX Pak Pro-compatible interfaces
- future seed or patch validation that needs to inspect item state or world-state flags quickly

## Practical recommendation

If the goal is to turn this into a real automated smoke-test lane, the best order is:

1. Super Metroid
2. Super Mario World
3. ALTTP

Why:

- Super Metroid already has the richest script/hitbox/TAS stack.
- SMW clearly supports external orchestration and emulator scripting, and is likely easier to make deterministic for short harnesses than a whole Zelda seed.
- ALTTP is still important, but the first useful harness there may look more like state validation and interface automation than classic TAS scripting.

## What I would build from this

Instead of trying to "adopt TAS" as one monolithic thing, build three harness layers:

1. `movie-replay`
   - boot ROM
   - load a short input movie or deterministic input script
   - verify expected state after N frames

2. `ram-assert`
   - boot ROM
   - inspect a handful of critical memory/state flags
   - fail early if they diverge

3. `room-or-level-smoke`
   - warp or enter a known room/level
   - replay a short deterministic sequence
   - assert that no crash, hang, or bad transition occurred

That model fits all three anchor games better than trying to force one "TAS framework" abstraction.

## Best next tasks

- Evaluate whether `BizHawk` is the most useful first harness emulator for the workspace, or whether `lsnes` gives us better long-term determinism for the SNES lanes.
- Clone and ingest `PJBoy/lua` into the Metroid lane as the first serious TAS-script repo.
- Ingest `brunovalads/smw-stuff` into the SMW lane as the first real SMW emulator-script lane.
- Decide whether the first automation prototype should be:
  - Super Metroid room transition test
  - SMW title-to-Yoshi's House boot test
  - ALTTP boot-and-state-flag test
- Keep ALTTP's first harness scoped to deterministic state validation rather than chasing a full TAS stack immediately.

## Sources

- ScriptHawk README: https://github.com/Isotarge/ScriptHawk
- PJBoy Lua scripts: https://github.com/PJBoy/lua
- Super Metroid Practice Hack: https://smpractice.speedga.me/
- Super Metroid Practice Hack source: https://github.com/tewtal/sm_practice_hack/
- Super Metroid TAS wiki page: https://wiki.supermetroid.run/Tool_Assisted_Speedruns
- SMW multi-instance BizHawk orchestration writeup: https://tasvideos.org/Forum/Topics/22544
- SMW utility script repo: https://github.com/brunovalads/smw-stuff
- SNI: https://github.com/alttpo/sni
- Archipelago: https://github.com/ArchipelagoMW/Archipelago
