# Bonus Research: SMW Central and FuSoYa

## Status

This pass is partial but useful.

- `SMW Central` is clearly still a major hub for low-level SMW hacking material, especially RAM maps, documents, tutorials, and community tool conventions.
- Direct terminal scraping of `smwcentral.net` is currently blocked here by a Cloudflare challenge, so this workspace does not yet contain a deep local mirror of those materials.
- `FuSoYa`'s Lunar Magic site is directly readable and gives a strong model for how editor-driven ROM hacking tools are built.

## What Lunar Magic tells us

Source URL:

- [FuSoYa Lunar Magic Introduction](https://fusoya.eludevisibility.org/lm/)

The introduction page is valuable because it describes the editor as an engineering pipeline, not a black box:

- reverse-engineer graphics compression
- build decompression/recompression tools
- decode level layout data
- disassemble enough ROM ASM to understand formats and behavior
- add targeted ASM ROM modifications where the original game needs extra support

That is the right mental model for "editor-like SNES tooling" in this project:

- structured binary parsers
- reversible serializers
- mapper-aware writes
- optional helper ASM patches that extend the base game without invalidating the ROM

It also illustrates a more advanced romhacking mode than a typical randomizer:

- the original Super Mario World ROM remains the compatibility base
- but substantial behavior, content, and data organization can be replaced or regenerated
- the authored layer is still usually assembly-centric rather than a high-level gameplay codebase

So for this workspace, SMW/Lunar Magic is the best example of a reconstruction-heavy, editor-assisted hacking ecosystem, while projects like `SMZ3` are better examples of patch-first build pipelines.

## What to mine from SMW Central next

Source URL:

- [SMW Central](https://www.smwcentral.net/)

The most relevant sections to extract next are:

- RAM map references
- documents/tutorials for 65c816 and SMW internals
- patch and tool documentation
- examples of community conventions around labels, freespace, and insertion workflows

## Why this matters outside SMW

SMW hacking is one of the most mature SNES hacking ecosystems. Even when the target game is not SMW, the ecosystem is still useful as a pattern library for:

- assembler-based patch workflows
- editor + patch hybrid tooling
- community conventions for labels and freespace
- producing valid ROMs after structured edits

For this reason, `SMW Central` and `Lunar Magic` are worth keeping in the knowledge graph even though the first playable targets in this workspace are Super Metroid and Zelda 3.
