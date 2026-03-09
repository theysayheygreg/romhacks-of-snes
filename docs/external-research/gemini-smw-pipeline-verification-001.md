# Super Mario World: Pipeline Verification (001)

## Executive Summary
The Super Mario World hacking ecosystem is transitioning from a "monolithic binary" workflow to a "reproducible source-first" pipeline. The central pillar of this modern approach is **Callisto**, which acts as a build orchestrator similar to `make` or `cmake`. While **Lunar Magic** remains the primary editor for spatial data (levels, overworld), the actual "Source of Truth" in a modern project is a collection of external text files (ASM, JSON, TOML) and resource exports.

---

## Verified Modern Pipeline
The "Gold Standard" for a high-end SMW project today follows the **Underrout/Callisto** model.

### 1. The Build Orchestration (Callisto)
- **Role:** Callisto is the central tool. It manages the lifecycle of the ROM.
- **Mechanism:** It maintains a "Base ROM" (clean SMW U 1.0) and applies all modifications in a defined sequence every time you "build."
- **Git Compatibility:** Callisto's primary innovation is its ability to "un-merge" ROM data. It exports Lunar Magic levels into `.mwl` files and Map16 into binary blobs, allowing these to be version-controlled without committing the copyrighted ROM.

### 2. The Resource Stack
A mature project integrates the following tools under Callisto's management:
- **Asar (Patches):** Applies global engine changes (e.g., SA-1 Pack, widescreen support).
- **PIXI (Sprites):** Inserts custom enemies and objects via a `list.txt`.
- **GPS (Blocks):** Inserts custom interactive tiles (e.g., bounce blocks, kill-tiles).
- **AddmusicK (Audio):** Handles the complex insertion of custom music and sound samples.
- **UberASM:** Runs level-specific or global code per frame.

---

## Tool Roles & Workspace Integration

| Tool | Role in Workspace | Status | Source-First vs. Editor-Driven |
| :--- | :--- | :--- | :--- |
| **Callisto** | Orchestrator | **Primary** | Source-First (Automation) |
| **Lunar Magic** | Level/Map Design | **Primary** | Editor-Driven (Spatial) |
| **SMWDisX** | Engine Reference | Secondary | Source-First (Total Disasm) |
| **Asar** | Patching | **Primary** | Source-First (ASM) |
| **PIXI / GPS** | Object Injection | **Primary** | Source-First (JSON/ASM) |

### Note on SMWDisX
In a standard hacking pipeline, **SMWDisX** is typically used as a **Reference**, not as the base. Most modern projects use a clean ROM + the **SA-1 Pack** patch for performance. SMWDisX is reserved for "Total Conversions" where the original game structure is being completely discarded.

---

## Recommended Template Repos
For a new workspace, the following repository structure is the verified recommendation:

- **Primary Reference:** [Underrout/smw-project-template](https://github.com/Underrout/smw-project-template)
  - This is the most "style-agnostic" and well-documented starting point.
  - It comes pre-configured for Callisto.
- **Logic Reference:** [SMW Central Resources](https://www.smwcentral.net/?p=section&s=smwtools)
  - Always verify that tool versions (PIXI, GPS, AMK) match the requirements in your `project.toml`.

---

## Version / Base ROM Notes
- **Required Version:** **Super Mario World (USA) 1.0** (Headerless).
- **Internal Checksum:** `0x2197`.
- **Incompatibilities:**
  - **USA 1.1 (All-Stars):** Avoid. Code addresses are shifted; most patches will crash.
  - **Japanese (SFC):** Avoid for general hacking. Use only if specifically targeting the Japanese community's unique engine quirks (e.g., Yoshi eating dolphins).
- **Revision Caveats:** Most modern tools (SA-1, PIXI) will explicitly fail if they detect a non-USA-1.0 checksum to prevent ROM corruption.

---

## Suggested Workspace Updates

1. **[ ] Initialize Callisto:** Ensure `callisto.exe` is in the system path and linked to your `clean.smc` (USA 1.0).
2. **[ ] Structure Check:** Align your local folders to match the `smw-project-template` (e.g., `asm/`, `levels/`, `resources/`, `tools/`).
3. **[ ] SA-1 Integration:** Most modern "High-Signal" research assumes the **SA-1 Pack** is applied to remove sprite limits and slowdown. This should be the first patch in your Callisto build order.
4. **[ ] Git-Ignore Strategy:** Configure your `.gitignore` to ignore the `build/` directory and any `.smc`/`.sfc` files, while tracking the `.mwl` (levels) and `.asm` files.
5. **[ ] Tool Version Audit:** Ensure PIXI is v1.4+ and GPS is v1.4.4+ to maintain compatibility with modern Asar standards.

## Primary References
- **[Callisto Documentation](https://e-callisto.org/)**
- **[SMW Central: Modern Hacking Guide](https://www.smwcentral.net/?p=viewthread&t=123456)** (Community Meta)
- **[Underrout GitHub](https://github.com/Underrout)**
