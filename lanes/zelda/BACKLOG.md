# Zelda Lane Backlog

This backlog is for Zelda 3 / ALttP-specific work inside the SNES workspace.

## Now

- [ ] Establish the Zelda 3 source-reference lane using `jpdasm`
  - Verify the example JP ROM against `jpdasm`'s expected revision and checksums.
  - Document how its banked assembly, symbols, and extracted binary assets are organized.
  - Identify the most useful files for overworld, room, sprite, and SRAM work.
  - [x] Produce one first-pass vanilla deep-dive note with concrete WRAM/SRAM and patch anchors.

- [ ] Map the Zelda randomizer lineage
  - Compare `z3randomizer` and `alttp_vt_randomizer`.
  - Add `ALttPDoorRandomizer` to the comparison.
  - Identify which parts are low-level patch payloads versus higher-level seed-generation logic.
  - Relate them to the Zelda-side concepts that show up in `SMZ3`.

## Next

- [ ] Build a Zelda vanilla progression note
  - Overworld progression grammar
  - Dungeon gating grammar
  - Key logic in the base game versus randomizers

- [ ] Build a Zelda design/mechanics note
  - core player loop
  - item and world-state grammar
  - what kinds of hacks preserve versus transform the original feel

- [ ] Produce one real standalone Zelda ROM artifact
  - Prefer a small, safe data or config patch first.
  - Keep it simple enough that we can later boot it on cartridge without ambiguity.

- [ ] Add Zelda-specific patch target notes
  - Safe early experiments
  - Candidate systems for data-only edits
  - Candidate systems for ASM patching

## Research Gaps

- [ ] Verify the exact local reassembly path for `jpdasm`
  - Extracted asset requirements
  - Assembler requirements
  - Whether exact reassembly is practical on this Mac
