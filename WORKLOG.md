# Work Log

This file tracks notable workspace work as it moves from planning into execution.

Flow:

- `ROADMAP.md` and `BACKLOG.md` define what matters
- `WORKLOG.md` records what was actively done
- `CHANGELOG.md` records durable workspace changes and milestones
- `build/` holds generated ROM artifacts and other outputs that stay out of git by default

## Entries

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
