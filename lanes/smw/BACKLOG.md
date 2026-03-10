# SMW Lane Backlog

This backlog is for Super Mario World-specific work inside the SNES workspace.

## Now

- [x] Establish the first SMW source/reference lane
  - [x] Ingest `SMWDisX` as the first SMW source-reference lane.
  - [x] Decide to anchor primarily on the staged U ROM for now.
  - [x] Fingerprint it with SHA-1/MD5 and mapper/header facts.
  - [x] Verify that the staged ROM is the working U anchor for this lane.
  - [x] Document how `SMWDisX`'s multi-version assembly strategy changes our workflow versus single-revision lanes like `jpdasm`.

- [x] Establish the first SMW tool/ecosystem lane
  - [x] Classify Lunar Magic as a Windows-only editor/tooling lane.
  - [x] Classify `callisto` as an SMW build-system/orchestration lane.
  - [x] Ingest the first wave of SMW-specific repos and tools.
  - [x] Separate editor-driven tools from low-level patch/disassembly references.
  - [x] Separate build orchestration from direct editing/disassembly tools.
  - [x] Capture where Lunar Magic-style workflows differ from patch-first randomizers.

- [x] Capture the first low-level SMW memory and patch notes
  - [x] WRAM/SRAM anchor references from `SMWDisX/rammap.asm`
  - [ ] freespace / insertion conventions
  - [x] patching formats and assembler assumptions

## Next

- [x] Produce one first-pass vanilla SMW deep-dive note
  - [x] ROM shape
  - [x] major memory anchors
  - [x] likely safe first patch targets

- [ ] Build an SMW design/mechanics note
  - core player loop
  - movement and obstacle grammar
  - world-map branching and secret-exit structure
  - what kinds of hacks preserve versus transform the original feel

- [x] Produce one real standalone SMW ROM artifact
  - [x] Prefer a small, safe patch or editor-like data edit first.
  - [x] Keep it simple enough for later emulator and cartridge testing.

- [ ] Compare SMW workflows against Zelda and Metroid lanes
  - what is editor-centric
  - what is assembly-first
  - what is build-system/orchestration-centric
  - what is still patch-first over a canonical base ROM
  - [x] Produce one first-pass SMW workflow model note.

- [x] Verify whether a modern `smw-project-template` belongs in this lane
  - [x] confirm repo identity and maintenance state
  - [x] classify it relative to `callisto`, Lunar Magic, and `SMWDisX`
  - [x] compare template assumptions against the staged SMW U 1.00 base ROM

- [ ] Verify modern SMW pipeline assumptions
  - likely role of SA-1 in current workflows
  - likely tool ordering for Asar / PIXI / GPS / AddmusicK / UberASM
  - whether the community still treats clean ROM + tools as the normal base

## Research Gaps

- [ ] Pull more material from `SMW Central`
  - RAM maps
  - assembly docs
  - community conventions

- [ ] Determine which parts of Lunar Magic are useful as engineering patterns here
  - binary parsing and serialization
  - compression/decompression
  - generated ASM support
  - command-line or batchable capabilities versus GUI-only workflows
