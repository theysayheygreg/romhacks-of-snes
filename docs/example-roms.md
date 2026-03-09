# Example ROM Profiles

The generated source-of-truth files are:

- `../analysis/super-metroid-rom.json`
- `../analysis/zelda-jp-rom.json`
- `../analysis/super-mario-world-usa-rom.json`

The clean base ROM copies used by this workspace live under:

- `../roms/base/`

## Super Metroid (Japan, USA) (En,Ja)

- File size: `3,145,728` bytes
- SHA-256: `12b77c4bc9c1832cee8881244659065ee1d84c70c3d29e6eaf92e6798cc2ca72`
- Selected header: `LoROM`
- Speed flag: `FastROM`
- Internal title: `Super Metroid`
- Declared ROM size: `4,194,304` bytes
- Declared RAM size: `8,192` bytes
- Destination: `Japan`
- Checksum pair validates: `yes`

Observations:

- The header at `0x7FC0` is clean and wins decisively over the HiROM candidate.
- The file is `3 MiB`, but the header declares `4 MiB` capacity. That is a useful reminder that header metadata describes intended cartridge layout, not always the exact dumped file size.
- As a `FastROM` LoROM game, it is a strong study target for action-heavy engine work and mapper-aware expansion.

## Zelda no Densetsu - Kamigami no Triforce (Japan)

- File size: `1,048,576` bytes
- SHA-256: `794e040b02c7591b59ad8843b51e7c619b88f87cddc6083a8e7a4027b96a2271`
- Selected header: `LoROM`
- Speed flag: `SlowROM`
- Internal title: `ZELDANODENSETSU`
- Declared ROM size: `1,048,576` bytes
- Declared RAM size: `8,192` bytes
- Destination: `Japan`
- Checksum pair validates: `yes`

Observations:

- This dump also resolves cleanly as `LoROM` with no copier header.
- Compared to Super Metroid, it gives us a simpler, smaller first-party structure to compare against when we study room tables, overworld state, and menu/UI code.
- We now have a matching high-value source reference in `../repos/jpdasm`, which targets the same Japanese 1.0 game revision and includes full banked assembly plus symbol files.

## Super Mario World (USA)

- File size: `524,288` bytes
- SHA-256: `0838e531fe22c077528febe14cb3ff7c492f1f5fa8de354192bdff7137c27f5b`
- Selected header: `LoROM`
- Speed flag: `SlowROM`
- Internal title: `SUPER MARIOWORLD`
- Declared ROM size: `524,288` bytes
- Declared RAM size: `2,048` bytes
- Destination: `North America`
- Checksum pair validates: `yes`

Observations:

- This is a clean `LoROM` / `SlowROM` image with no copier header and a native reset at `80:8000`.
- It lines up cleanly with the cartridge shape declared in `SMWDisX/smw.asm`.
- It gives the SMW lane its first concrete base-ROM anchor for comparing `SMWDisX`, Lunar Magic support expectations, and build-system assumptions like `callisto`.

## Why these two are a useful pair

Together they cover two very different design families on the same hardware:

- `Super Metroid`:
  - systemic action engine
  - room and state complexity
  - heavy movement/item logic
- `Zelda 3`:
  - overworld + dungeon split
  - event/state progression
  - menu/UI and data-driven room scripting

That makes them ideal reference anchors for future hacks and for cross-game projects like `SMZ3`.
