# SMW Lane Backlog

This backlog is for Super Mario World-specific work inside the SNES workspace.

## Now

- [ ] Establish the first SMW source/reference lane
  - [x] Ingest `SMWDisX` as the first SMW source-reference lane.
  - Decide whether to anchor primarily on J, U, E1.0, or E1.1 for this workspace.
  - Fingerprint it with SHA-1/MD5 and mapper/header facts.
  - Verify which local ROM revision matches the chosen lane target exactly.
  - Document how `SMWDisX`'s multi-version assembly strategy changes our workflow versus single-revision lanes like `jpdasm`.

- [ ] Establish the first SMW tool/ecosystem lane
  - [x] Classify Lunar Magic as a Windows-only editor/tooling lane.
  - [x] Classify `callisto` as an SMW build-system/orchestration lane.
  - Ingest the first wave of SMW-specific repos and tools.
  - Separate editor-driven tools from low-level patch/disassembly references.
  - Separate build orchestration from direct editing/disassembly tools.
  - Capture where Lunar Magic-style workflows differ from patch-first randomizers.

- [ ] Capture the first low-level SMW memory and patch notes
  - WRAM/SRAM anchor references from `SMWDisX/rammap.asm`
  - freespace / insertion conventions
  - patching formats and assembler assumptions

## Next

- [ ] Produce one first-pass vanilla SMW deep-dive note
  - ROM shape
  - major memory anchors
  - likely safe first patch targets

- [ ] Build an SMW design/mechanics note
  - core player loop
  - movement and obstacle grammar
  - world-map branching and secret-exit structure
  - what kinds of hacks preserve versus transform the original feel

- [ ] Produce one real standalone SMW ROM artifact
  - Prefer a small, safe patch or editor-like data edit first.
  - Keep it simple enough for later emulator and cartridge testing.

- [ ] Compare SMW workflows against Zelda and Metroid lanes
  - what is editor-centric
  - what is assembly-first
  - what is build-system/orchestration-centric
  - what is still patch-first over a canonical base ROM

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
