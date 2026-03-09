# SMW Intake Checklist

Use this note when adding the first real SMW artifacts to the workspace.

## Needed inputs

- one canonical base SMW ROM
- one or more repo links
- any known patching or editor tools that matter to the workflow

## First-pass intake steps

1. Fingerprint the ROM.
   - SHA-1
   - MD5
   - mapper/header facts
   - reset vector
   - ROM and SRAM size
2. Decide what kind of lane each repo is.
   - exact-match source/disassembly
   - editor/tooling
   - patch-first hack base
   - docs/reference
3. Identify the first anchor artifacts.
   - canonical ROM note
   - WRAM/SRAM references
   - toolchain/build notes
   - safe patch or edit targets

## Questions to answer early

- Which SMW ROM revision should this lane standardize on?
- Do we use `SMWDisX` as a multi-version source lane first, then pin one canonical revision on top of it?
- Which part of the ecosystem is most reusable outside SMW:
  - level/data editing
  - ASM insertion
  - graphics/compression handling
  - freespace management

## Current known source lane

- `SMWDisX` is the first ingested SMW source/reference lane.
- It is designed to assemble multiple releases instead of one single canonical revision:
  - J
  - U
  - E 1.0
  - E 1.1
  - Super System
- It uses `asar` and version selection via `!_VER` in `smw.asm`.
- It includes a large low-level RAM map in `rammap.asm`, which should be our first memory-anchor source for SMW.

## Current known tooling lane

- Lunar Magic `3.63` is available locally as a Windows editor/tooling lane.
- Local path:
  - `/Users/theysayheygreg/Downloads/lm363`
- Supported ROMs from its bundled readme:
  - American Super Mario World version 1.00
  - Japanese Super Mario World version 1.00
  - Super Mario All-Stars + World, American version 1.00, SMW portion
- It is useful as an editor-driven workflow reference even when not directly runnable on this Mac.

## Current known build-system lane

- `callisto` is now ingested as an SMW project build-system/orchestration lane.
- It is not a disassembly and not a level editor.
- Its role is to coordinate:
  - clean ROM usage
  - patches
  - modules
  - Lunar Magic exports
  - packaging and emulator launch flows
- This makes it a strong reference for how mature SMW projects are structured in git without treating the ROM itself as the primary working format.

## Expected outputs

- one `analysis/` artifact for ROM facts
- one lane note for the first deep-dive pass
- one repo/classification update in the shared workspace docs
