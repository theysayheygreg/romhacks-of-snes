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
