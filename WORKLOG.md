# Work Log

This file tracks notable workspace work as it moves from planning into execution.

Flow:

- `ROADMAP.md` and `BACKLOG.md` define what matters
- `WORKLOG.md` records what was actively done
- `CHANGELOG.md` records durable workspace changes and milestones
- `build/` holds generated ROM artifacts and other outputs that stay out of git by default

## Entries

### 2026-03-31

- Parked `bsnes` as a Metal R&D lane after proving native window output but not real SNES frame upload.
- Promoted `snes9x` to the default practical macOS emulator lane with a reliable `open -a` launcher.
- Produced a second standalone SMW ROM artifact that changes visible gameplay behavior by raising vanilla starting lives from 4 to 9.
- Wired the connected PS5 DualSense into the staged `snes9x` app as the default Player 1 controller.
- Built and staged a separate source-built `snes9x` app with a firmer `0.5` left-stick dead zone for DualSense comparison without replacing the stable release app.
- Completed a first-pass TAS / deterministic-harness research note for SMW, Super Metroid, and ALTTP, with a recommendation to start automation from the Metroid lane.
- Turned the TAS research into machine-readable harness sketches and a lightweight validator so the workspace has concrete automation targets for all three anchor games.
- Ingested `PJBoy/lua` into the Metroid lane and stood up the first concrete Super Metroid harness scenario plus a generic preflight runner.
- Generated the first Metroid harness result artifact by running a clean preflight against the staged Super Metroid ROM and source Lua harness files.
- Classified `sm_practice_hack` as a testing/instrumentation asset and pinned the first Metroid harness to an explicit early-game Landing Site -> Parlor candidate transition.
- Added a `Snes9x` manual-assist launcher for the first Metroid harness slice and emitted the first operator-facing manual-assist artifact for the Landing Site -> Parlor transition checklist.
- Added a companion completion tool so the Metroid manual-assist slice can now record pass/fail checklist results instead of stopping at `pending_operator`.
- Duplicated the same harness pattern into the SMW lane with a first visible-state manual-assist slice for the `smw-starting-lives-09.sfc` patch artifact.
- Completed the first SMW manual-assist result as a real `pass` artifact based on the already-verified start-lives patch behavior.
- Duplicated the same harness pattern into the Zelda lane with a first fresh-file boot manual-assist slice for the exact-match JP base ROM.
- Added a second Zelda manual-assist slice that ties fresh-file smoke testing back to trusted `jpdasm` and randomizer WRAM/SRAM anchors for basic world-state sanity.
- Promoted the existing Zelda general-bugfix patch path into a stable standalone artifact with a durable output name and probe record.
- Added the first standalone Super Metroid gameplay-state artifact by patching the vanilla new-file starting energy from 99 to 199.

### 2026-03-09

- Initialized the SNES workspace as its own git repository.
- Stood up the shared SNES docs, lane structure, and backlogs.
- Ingested emulator, disassembly, randomizer, editor, and build-system repos for Zelda, Super Metroid, SMZ3, and SMW.
- Verified the macOS lane with `bsnes`, `SMZ3`, `MapRandomizer`, and a `z3randomizer` patch-first ROM path.
- Added staged clean base ROM handling under `roms/base/` while keeping ROM binaries ignored in git.
- Produced first-pass deep-dive notes for Zelda and Super Metroid.
- Activated the SMW lane with `SMWDisX`, Lunar Magic, `callisto`, and a base SMW ROM fingerprint.
- Added external research, design notes, and a Gemini deep-research prompt.
- Ingested the first Gemini deep-research brief and distilled it into a canonical intake note with verification tasks.
- Ingested the first Gemini reference-verification brief and converted it into concrete debugger/disassembly/editor follow-up tasks.
- Ingested the Gemini Metroid PLM brief and turned it into a first-pass canonical Metroid note tied to local source evidence.
- Ingested the Gemini SMW pipeline brief and turned it into a first-pass canonical SMW workflow model with explicit open verification points.
- Ingested `multirando-asm` as a second major crossover example, broadening the crossover lane from two-game `SMZ3` thinking toward four-game composite-ROM architecture.
- Ingested the Gemini multiworld brief and turned it into a first shared note on why Archipelago-style models matter architecturally without making them a near-term implementation target.
- Completed the first vanilla SMW deep-dive pass with a symbol map, game-mode anchor, and WRAM/SRAM patch surfaces.
- Validated `smw-project-template` as the first modern SMW starter/template lane and aligned it with the existing Callisto model.
- Produced the first standalone SMW ROM artifact with a checksum-fixed patch-first workflow.
- Added a Documents-based emulator testing layout plus a sync script for curating GUI-emulator-ready ROM symlinks.
- Investigated the current `bsnes` black-video issue on this Apple Silicon Mac, tied it to an upstream macOS/OpenGL issue, and produced a clean `x86_64` Rosetta test app as the next validation step.
- Staged the official `snes9x` macOS release app as the practical GUI emulator lane and documented its expected config/data roots after confirming the local Xcode source-build path is blocked by the host Xcode installation state.
- Added a native Metal video backend to the vendored `bsnes` source lane, built it successfully on this Mac, and staged a native Apple Silicon Metal test app for manual verification.
- Refined the local `bsnes` Metal render loop to render through the `MTKView` delegate path, fixed the macOS driver registration guard, and refreshed the staged patched app for GUI verification on Apple Silicon.
