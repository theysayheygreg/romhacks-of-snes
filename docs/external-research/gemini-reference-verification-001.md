# SNES Reverse Engineering & Romhacking: Reference Verification (001)

## Executive Summary
This document provides a verified audit of the foundational tools, disassemblies, and documentation for the SNES reverse-engineering ecosystem. The research confirms that while the community is rooted in legacy disassemblies (MathOnNapkins, P.JBoy, Kejardon), the modern workflow has shifted toward **Asar-compatible relocatable disassemblies**, **multi-system emulators with advanced debugging (Mesen 2)**, and **build-orchestration templates (Callisto/smw-project-template)**. 

## Verified Keep (Highly Recommended)
These resources are current, actively maintained, or definitive standards that should form the core of any modern research workspace.

- **Mesen 2 (Successor to Mesen-S):** The definitive multi-system debugger/emulator. It has superseded Mesen-S and is more feature-rich than bsnes-plus for modern reverse engineering.
- **bsnes-plus:** While in maintenance mode, its specific UI for real-time memory highlighting and register editing remains a favorite for "surgical" ASM work.
- **sm_disassembly (InsaneFirebat):** The current standard for relocatable Super Metroid disassembly. It is Asar-compatible and actively used for modern engine-level hacks.
- **JaredBrian Zelda 3 Disassembly:** The primary active effort to bring the ALTTP disassembly into the modern Asar-compatible era.
- **alttp.run (RAM/SRAM References):** The most accessible and accurate live documentation for ALTTP memory mapping.
- **smw-project-template (Underrout):** The "Gold Standard" for modern SMW development, enabling Git-based version control via Callisto.
- **Displaced Gamers (Behind the Code):** High-signal video analysis that provides the best conceptual bridge between "playing a game" and "reading its assembly."

## Historical But Useful
These are "The Bibles" of the scene. They may not be the primary way you *write* code today, but they are the source of almost all nomenclature and technical discovery.

- **MathOnNapkins Zelda 3 Disassembly:** The "Root" of all ALTTP reverse engineering. Modern disassemblies are effectively commentaries on this work.
- **Zelda 3 Compendium (v1.8.4):** The ultimate technical PDF. While the wiki (alttp.run) is easier to search, the Compendium contains exhaustive logic details that aren't always fully mirrored online.
- **P.JBoy Super Metroid Disassembly:** The original bank logs that made `sm_disassembly` possible. Useful for verifying raw bank data.
- **Kejardon Technical Docs:** Foundational deep-dives into Super Metroid physics. Essential for understanding *why* Samus moves the way she does.
- **Danofmosttrades (Videos):** While specifically for SMW/Lunar Magic, his teaching methodology is the community standard for onboarding.

## Ambiguous / Needs More Caution
- **ZScream:** Currently in a "Legacy" state. While functional, it is being superseded by **yaze** (Yet Another Zelda3 Editor) in modern professional workflows. Use with caution in new projects.

## Not Recommended
- **Mesen-S (Standalone):** Deprecated. Use **Mesen 2** instead.

## Direct Links Table

| Resource | Category | Status | Primary / Archive Link |
| :--- | :--- | :--- | :--- |
| **Mesen 2** | Debugger/Emulator | **Active** | [GitHub: SourMesen/Mesen2](https://github.com/SourMesen/Mesen2) |
| **bsnes-plus** | Debugger/Emulator | Stable | [GitHub: devinacker/bsnes-plus](https://github.com/devinacker/bsnes-plus) |
| **sm_disassembly** | Source/Disassembly | **Active** | [GitHub: InsaneFirebat/sm_disassembly](https://github.com/InsaneFirebat/sm_disassembly) |
| **JaredBrian Z3 Disasm** | Source/Disassembly | **Active** | [GitHub: JaredBrian/AsarUSALTTPDisassembly](https://github.com/JaredBrian/AsarUSALTTPDisassembly) |
| **smw-project-template** | Editor/Tooling | **Active** | [GitHub: Underrout/smw-project-template](https://github.com/Underrout/smw-project-template) |
| **Kejardon Docs** | Community Docs | Archive | [Kejardon's SM Archive](http://jathys.zophar.net/supermetroid/kejardon/index.html) |
| **alttp.run** | Community Docs | **Active** | [alttp.run/hacking](http://alttp.run/hacking/) |
| **Displaced Gamers** | Video/Teaching | **Active** | [YouTube: Displaced Gamers](https://www.youtube.com/@DisplacedGamers) |
| **yaze (Z3 Editor)** | Editor/Tool | **Active** | [GitHub: gladiat0r/yaze](https://github.com/gladiat0r/yaze) |

## Suggested Workspace Updates
1.  **De-prioritize ZScream:** Update the workspace documentation to list **yaze** as the primary recommendation for ALTTP editing.
2.  **Standardize on Mesen 2:** Ensure all "Debugging" instructions favor Mesen 2's multi-system tools over the older Mesen-S or standalone bsnes.
3.  **Adopt Asar-Relocatable Source:** When importing disassemblies, prioritize the **JaredBrian (Z3)** and **InsaneFirebat (SM)** repos, as they are pre-configured for modern patching workflows.
4.  **Integrated Build Pipeline:** Use `smw-project-template` as the blueprint for how *all* games (Z3 and SM included) should eventually be handled: Source -> Assembler -> Orchestrator -> Final ROM.
