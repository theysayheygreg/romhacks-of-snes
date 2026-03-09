# Metroid Lane Backlog

This backlog is for Super Metroid-specific work inside the SNES workspace.

## Now

- [ ] Deep-dive Super Metroid as the first anchor game
  - Map bank layout, major data regions, and reset/entry behavior.
  - Document room/state structure, save RAM usage, and item/progression hooks.
  - Identify likely first mod targets for small, safe experimental patches.
  - Produce one first-pass vanilla deep-dive note with concrete addresses and room pointers.

- [ ] Add the Super Metroid-side terminology for progression analysis
  - Compare it to Zelda randomizer terms like logic, playthrough, and spheres.
  - Note where the concepts match even if the names differ.

- [ ] Map the Super Metroid randomizer lineage
  - Compare `RandomMetroidSolver` and `MapRandomizer`.
  - Identify where item logic, solver logic, topology logic, and ROM patching live.
  - Relate both to how `SMZ3` likely composes its Super Metroid-side behavior.

## Next

- [ ] Build a vanilla Super Metroid progression note
  - Item gating
  - Movement/trick gating
  - Area progression and route structure

- [ ] Build a Super Metroid design/mechanics note
  - core player loop
  - movement and topology grammar
  - what kinds of hacks preserve versus transform the original feel

- [ ] Produce one real standalone Super Metroid ROM artifact
  - Prefer a small, safe patch target first.
  - Keep it simple enough that we can later boot it on cartridge without ambiguity.

- [ ] Add Super Metroid patch target notes
  - Low-risk ROM edits
  - Compression/decompression touchpoints
  - Save-state or SRAM-adjacent systems worth understanding

- [ ] Document the PLM execution model
  - [x] Produce one first-pass structural note for PLMs and room states.
  - what Bank `84` owns
  - how room-loaded interactivity is updated
  - how that connects to item and door behavior

- [ ] Evaluate `InsaneFirebat/sm_disassembly`
  - how it compares to `strager/supermetroid`
  - whether it should become a second modern Metroid source lane
