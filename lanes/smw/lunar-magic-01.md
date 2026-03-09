# Lunar Magic 01

This note classifies the local Lunar Magic copy as an SMW tooling lane artifact.

## Local artifact

Local folder:

- `/Users/theysayheygreg/Downloads/lm363`

Observed files:

- `Lunar Magic.exe`
- `x64/Lunar Magic.exe`
- `Lunar Magic.chm`
- `readme.txt`

Version from `readme.txt`:

- `3.63`
- dated `December 25, 2025`

Binary shape:

- `Lunar Magic.exe`: `PE32` Windows GUI executable
- `x64/Lunar Magic.exe`: `PE32+` Windows GUI executable
- `Lunar Magic.chm`: Windows HTML Help

## Classification

Lunar Magic belongs in the SMW lane as:

- editor/tooling lane
- Windows-assisted workflow
- reconstruction-heavy ROM editing reference

It is not the same kind of artifact as `SMWDisX`.

`SMWDisX` gives us source/disassembly and memory-map style understanding.
Lunar Magic gives us the practical editor-driven ecosystem that writes valid SMW ROMs while also applying targeted ASM/data extensions.

## Supported ROM targets

From the bundled `readme.txt`, Lunar Magic supports:

- American Super Mario World version `1.00`
- Japanese Super Mario World version `1.00`
- American Super Mario All-Stars + World version `1.00`, SMW portion

That makes it a strong signal for which base ROM revisions the editor-centric ecosystem cares about most.

## Useful engineering signals

The bundled readme explicitly describes Lunar Magic as more than a map editor.

It combines:

- WYSIWYG level editing
- graphics editing
- palette editing
- world map editing
- text editing
- external level import/export
- numerous `65816` ASM enhancements

The credits are also informative. They reference:

- a VRAM optimization patch
- dynamic levels work
- FastROM address lists
- LC_LZ2 / LC_LZ3 compression patches
- ZSNES debugger and Snes9x tracer usage during development

That makes Lunar Magic important here not because we can run it on macOS today, but because it captures the mature SMW pattern:

- parse and rewrite structured ROM data
- recompress assets
- extend the original engine with targeted assembly patches
- preserve a valid runnable ROM as the output

## Practical implication for this workspace

For the SMW lane, we should treat Lunar Magic as:

- the canonical editor-driven workflow reference
- a Windows helper lane when needed
- a design pattern source for future editor-like tooling

We should not block the SMW lane on running it locally.
The more immediate need is:

- choose a base SMW ROM revision
- fingerprint that ROM
- connect it to `SMWDisX`
- then decide when Lunar Magic needs a Windows execution lane rather than just documentation/reference status
