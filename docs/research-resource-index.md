# Research Resource Index

This note curates external resources worth keeping in the SNES workspace.

The goal is not to dump every site in the ecosystem.
The goal is to keep the resources that are most likely to help with:

- hardware understanding
- ROM structure and patching workflows
- game-specific hacking conventions
- design-level understanding of Zelda 3, Super Metroid, and SMW

## General SNES romhacking and development

### Hardware, memory, and low-level programming

- [SNESdev Wiki](https://snes.nesdev.org/wiki/SNESdev_Wiki)
  - Best general entry point for SNES hardware, memory mapping, and programming references.
- [SNES Development Manual](https://snes.nesdev.org/wiki/SNES_Development_Manual)
  - Good hardware-oriented reference with practical system-level coverage.
- [SNESdev Tutorials](https://snes.nesdev.org/wiki/Tutorials)
  - Useful for learning the platform from the programming side, even when the end goal is hacking rather than homebrew.
- [SnesLab Programming Guide](https://sneslab.net/wiki/Programming_guide)
  - Good alternate perspective on how to reason about the console as an engine target.
- [fullsnes](https://problemkaputt.de/fullsnes.htm)
  - Dense hardware reference that is still worth keeping around for edge cases and mapper/register details.

### Patch and assembler workflow

- [Asar User Manual](https://rpghacker.github.io/asar/asar_19/manual/)
  - Canonical reference for the assembler that dominates modern SNES patch workflows.
- [Flips / Floating IPS](https://github.com/Alcaro/Flips)
  - Practical reference for IPS/BPS patch application and generation workflows.

## Zelda 3 resources

### Hacking and patch ecosystem

- [ALTTPHacking.net](https://alttphacking.net/)
  - Community hub for Zelda 3 hacks, tools, and editor-oriented workflows.
- [ALttP Randomizer](https://alttpr.com/)
  - Important because it captures modern seed-generation, logic, settings, and spoiler expectations.
- [ALttP Randomizer Resources](https://alttpr.com/resources)
  - Good community-facing orientation material around racing, guides, and support.
- [ALttP Randomizer Game Options](https://alttpr.com/en/options)
  - Useful for understanding how the community exposes logic, mode, and progression switches.

### Local source/reference lanes already in workspace

- `repos/jpdasm`
- `repos/z3randomizer`
- `repos/alttp_vt_randomizer`
- `repos/ALttPDoorRandomizer`

## Super Metroid resources

### Hacking and randomizer ecosystem

- [Super Metroid Mod Manual](https://metroidconstruction.com/SMMM/)
  - Best beginner-to-intermediate hack-construction reference surfaced so far.
- [VARIA Randomizer Infos](https://randommetroidsolver.pythonanywhere.com/infos)
  - Good source for how the modern Super Metroid randomizer ecosystem frames logic, presets, and patch behavior.
- [VARIA Randomizer](https://randommetroidsolver.pythonanywhere.com/randomizer)
  - Useful for understanding exposed logic settings and what they imply about the underlying game.
- [Super Metroid Instruction Manual Scan](https://www.metroid.retropixel.net/games/metroid3/manual/)
  - Useful for original intended player-facing mechanics framing.

### Local source/reference lanes already in workspace

- `repos/supermetroid`
- `repos/RandomMetroidSolver`
- `repos/MapRandomizer`

## Super Mario World resources

### Editing and community ecosystem

- [FuSoYa Lunar Magic Introduction](https://fusoya.eludevisibility.org/lm/)
  - Best concise explanation of the editor-driven SMW workflow model.
- [SMW Central](https://www.smwcentral.net/)
  - Core community hub for tools, patches, RAM maps, and conventions.
- [SMW Central Getting Started archive snapshot](https://archive.li/AKQe1)
  - Useful because direct scraping is unreliable here, but the snapshot still exposes the beginner-facing workflow framing.
- [SnesLab Lunar Magic page](https://sneslab.net/wiki/Lunar_Magic)
  - Useful secondary reference summarizing ROM/version expectations and release history.

### Local source/reference lanes already in workspace

- `repos/SMWDisX`
- `repos/callisto`
- `lanes/smw/lunar-magic-01.md`

## Why these matter for our workspace

The resource split is now clearer:

- general SNES docs explain the machine
- source/disassembly repos explain specific games
- randomizer sites explain modern logic/seed/spoiler practice
- editor communities explain reconstruction-heavy workflows

That combination is what we need if the goal is not just to read ROMs, but to:

- modify them safely
- generate reproducible outputs
- understand the design consequences of those modifications
