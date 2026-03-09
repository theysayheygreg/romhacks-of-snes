# SNES Reverse Engineering & Romhacking: Deep Research Brief (001)

## Executive Summary
The SNES romhacking ecosystem is one of the most mature and technically sophisticated reverse-engineering communities in existence. While it began with simple hex editing and "Lunar Magic" (SMW), it has evolved into a discipline involving full disassemblies, modern CI/CD-like build pipelines, and complex graph-based logic for randomizers. This document anchors on three games—*The Legend of Zelda: A Link to the Past*, *Super Metroid*, and *Super Mario World*—which represent the three pillars of SNES hacking: Adventure/Logic (Z3), Atmosphere/Physics (Metroid), and Editor-Centric Platforming (SMW).

---

## General SNES Resources
### Foundational Concepts
- **Memory Mapping:**
    - **LoROM (Mode 20):** ROM mapped to $8000-$FFFF of banks $00-$7F. System registers mirrored in $0000-$7FFF. Used by most early/smaller games.
    - **HiROM (Mode 21):** ROM mapped to $0000-$FFFF of banks $C0-$FF. More efficient for large data (>32KB chunks).
    - **ExHiROM:** Extension for ROMs > 4MB (32Mbit), using banks $40-$7D and $C0-$FF.
- **FastROM:** Setting bit 0 of `$420D` allows the CPU to run at 3.58 MHz (vs 2.68 MHz) when accessing banks $80-$FF. Essential for performance-heavy hacks.
- **Assemblers:** **Asar** is the industry standard. It supports 65816, SPC700 (audio), and SuperFX. It is the backbone of modern patch-based workflows.
- **Patching Formats:** **BPS (Beat Patching System)** is preferred over IPS. It includes checksums and handles data shifts, making it safer and more efficient for modern hacks.

### Essential Tooling
- **Debuggers:** **bsnes-plus** and **Mesen-S** are the gold standards for cycle-accurate debugging, memory viewing, and trace logging.
- **Patchers:** **Floating IPS (Flips)** for BPS/IPS application and creation.

---

## Zelda 3 Resources (A Link to the Past)
### Disassembly & Memory
- **Foundational Disassembly:** **MathOnNapkins'** disassembly is the historical reference. Modern projects like **JaredBrian's Asar-compatible disassembly** and **spannerisms' Japanese 1.0 disassembly** are more usable for new projects.
- **RAM/SRAM Maps:** **alttp.run** (Hacking Wiki) maintains the definitive RAM map (Bank $7E/$7F) and SRAM map for save states.
- **Key Logic:** ALTTP uses "Game States" (Bank $7E:0010) to manage the main loop (Overworld, Dungeon, Menu, etc.).

### Randomizer & Logic
- **ALTTPR Logic:** Uses a **Graph-Based Logic** (Nodes and Edges). Nodes are locations; Edges are the requirements (e.g., "Must have Hammer") to reach them.
- **Fill Algorithms:** **Assumed Fill** (assumes all other items are in inventory to check reachability) is the primary method for ensuring beatability.
- **Entrance/Door Randomizer:** These shuffle the pointers between overworld transitions and underworld interior headers.

---

## Super Metroid Resources
### Technical Documentation
- **Disassembly:** **P.JBoy's Disassembly** is the standard for relocatable code. **sm_disassembly (GitHub)** is the most active community fork.
- **PLMs (Post-Load Modifications):** The lifeblood of Super Metroid's interactivity. Items, doors, and crumbling blocks are all PLMs (Bank $84).
- **Room Data:** Stored in Bank $8F. Headers define dimensions, map color, and "State Headers" (pointers to room versions based on game events like boss deaths).

### Communities & Editors
- **Metroid Construction:** The central hub for all documentation, including the "Metroid Mod Manual."
- **SMILE (Super Metroid Integrated Level Editor):** The primary tool for level design. Understanding its internal "Room Header" logic is critical for any SM reverse engineering.

---

## Super Mario World Resources
### The Modern Pipeline
- **Callisto:** The revolutionary build system that enables a "source-code first" approach. It exports ROM resources (levels, Map16) to text/binary files, allowing for Git-based version control.
- **SMWDisX:** The definitive disassembly of SMW, often used as the base for "engine-level" modifications.
- **Build Flow:** Clean ROM -> SMWDisX -> PIXI (Sprites) -> GPS (Blocks) -> AddmusicK (Audio) -> Lunar Magic (Levels) = Final Hack.

### Editor-Centric Culture
- **Lunar Magic (LM):** The most powerful editor in the SNES scene. It bypasses original game limits (e.g., VRAM management) through its own internal "LM-Logic" patches.
- **SMW Central (SMWC):** The most organized resource repository, featuring thousands of custom sprites, blocks, and patches, all vetted for compatibility.

---

## Game Design Analysis

| Game | Core Player Loop | Main Verbs | Progression Grammar | World Structure |
| :--- | :--- | :--- | :--- | :--- |
| **Zelda 3** | Explore -> Dungeon -> Item -> Boss | Slash, Dash, Lift, Use Tool | Episodic/Structural (Dual World) | Parallel Overworlds (Hub-and-Spoke) |
| **Metroid** | Navigate -> Gated Path -> Ability -> Backtrack | Shoot, Jump, Morph, Run | Ability-Based Locks (Lock-and-Key) | Interconnected Labyrinth (Vertical/Hive) |
| **SMW** | Clear Level -> Map Expansion -> Secret Exit | Run, Jump, Spin-Jump, Fly | Linear-Branching (Secret Exits) | Macro-Map (Hub/World State) |

### Modification Impact
- **Original Feel:** Tweaking room layouts, enemy placement, or palette shifts.
- **Radical Transformation:** Changing "verbs" (e.g., adding a Wall Jump to Zelda) or "progression grammar" (e.g., Randomizers), which shifts the game from a test of execution to a test of **knowledge and routing**.

---

## Best Video Resources
1. **Retro Game Mechanics Explained:** Essential for hardware-level understanding (DMA, Background Layers, Sprite Limits).
2. **Displaced Gamers (Behind the Code):** Deep dives into original game logic (e.g., Zelda Hit Detection, Metroid Physics).
3. **"Yes I Froze an SNES for TASBot" (MAGFest/GDQ):** Technical showcases of code injection and hardware exploits.
4. **Danofmosttrades (Lunar Magic Series):** The definitive beginner-to-intermediate guide for the SMW ecosystem.

---

## Foundational Community Docs
- **The Zelda 3 Compendium:** A massive technical reference for the Z3 engine.
- **Kejardon’s Documents (Metroid):** High-level technical notes on Super Metroid's physics and state machine.
- **SMW Central RAM/ROM Maps:** The most comprehensive byte-level documentation of any SNES game.
- **Asar Manual:** The "bible" for modern SNES assembly patching.

---

## Most Useful Repos and Tools
- **Repos:**
    - `sm-json-data` (GitHub): The logic definitions for Super Metroid randomizers.
    - `ALttP-Logic` (GitHub): The node/edge definitions for Zelda 3.
    - `smw-project-template` (GitHub): The modern Callisto-based starting point for SMW hacks.
- **Tools:**
    - **Asar:** CLI-based assembler.
    - **Callisto:** SNES build system.
    - **SMILE / Lunar Magic / ZScream:** Level editors for Metroid, SMW, and Zelda respectively.

---

## Open Research Questions
1. **Universal Logic Standard:** Can the logic graphs of ALTTPR and SM-Randomizer be unified into a single "Progression Grammar" schema for multi-game "Archipelago" style randomizers?
2. **Modernization of Metroid/Zelda Pipelines:** Can the "Callisto" (source-first) workflow be effectively ported to Super Metroid and Zelda 3 to replace the current editor-first/binary-first workflows?
3. **SA-1 Optimization:** How can the SA-1 coprocessor be more easily integrated into existing disassemblies to remove slowdown in complex room/sprite scenarios?

---

## Next-Step Research Tasks
1. **[ ]** Clone and build the `smw-project-template` using Callisto to understand the build-pipeline orchestration.
2. **[ ]** Analyze the `.json` files in `sm-json-data` to map out Super Metroid's "Basic" vs "Advanced" logic gates.
3. **[ ]** Diff the US and Japanese 1.0 Zelda 3 disassemblies to understand why the Japanese 1.0 is the preferred base for hacking.
4. **[ ]** Create a "Hello World" Asar patch that hijacks the SNES NMI (Non-Maskable Interrupt) to display a custom color on the screen.
5. **[ ]** Research the "Archipelago" multi-world randomizer protocol to understand how cross-game state is synchronized.
6. **[ ]** Investigate the `sm_disassembly` repo for Super Metroid and attempt to re-assemble it into a bit-perfect ROM.
7. **[ ]** Map the "PLM" execution loop in Super Metroid to understand how the game handles frame-by-frame object updates.
8. **[ ]** Review the "Vanilla Level Design Contest" (VLDC) winner entries to analyze modern "Vanilla" design constraints.
9. **[ ]** Research the "FastROM" conversion process for Zelda 3 to identify the exact bank-mirroring addresses required.
10. **[ ]** Examine the `EmoTracker` logic scripts for ALTTPR to see how "Inverted" world logic differs from "Standard" world logic.
