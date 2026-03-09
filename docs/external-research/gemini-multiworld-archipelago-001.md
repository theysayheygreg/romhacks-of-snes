# Multiworld Synchronization: Archipelago & Cross-Game Architecture (001)

## Executive Summary
Multiworld systems, specifically **Archipelago (AP)**, have evolved from simple "item-swapping" scripts into a sophisticated **Cross-Game Progression Graph Abstraction**. While the primary user experience is social multiplayer, the underlying architecture provides a robust model for "Verifiable Progression" that is highly relevant to any serious SNES reverse-engineering workspace. By abstracting game-specific logic into a unified "Item/Location" schema, Archipelago enables complex crossovers like **SMZ3** to be treated as a single logical entity within a larger network.

---

## Technical Model
### The Client-Server Sync
Archipelago operates on a **Client-Server model** over WebSockets.
- **Server:** The central authority and "Source of Truth." It maintains the state of every player's "World" (Slot).
- **Client (SNI Client):** A middleware that bridges the network protocol to the SNES memory. It uses the **Super Nintendo Interface (SNI)** to read/write memory in real-time.
- **Sequential Indexing:** Items are sent using a strictly ordered `index`. If a client detects a skip (e.g., expected index 5 but got 7), it triggers a `Sync` request to rebuild the local state.

### Logic Abstraction (APL)
The **Archipelago Logic System (APL)** is the mathematical core.
- **Progression Graph:** It represents every game as a Directed Acyclic Graph (DAG) of **Nodes** (Locations) and **Edges** (Access Rules).
- **Atomic Requirements:** Rules are defined as "Logical Requirements" (e.g., `can_reach('Screw Attack')`).
- **Unified Fill Algorithm:** The system performs "Forward Fill" simulations across all connected games simultaneously to ensure no player is ever soft-locked by another's progress.

---

## SNES Relevance
Archipelago treats SNES games as "Local Modules" (APWorlds) that interface with standardized clients.

- **Zelda 3 (ALTTP):** The "Gold Standard" integration. It uses a custom patch (`.aplttp`) that hijacks the item-receiving routine to wait for network packets.
- **Super Metroid:** Deeply integrated, allowing for complex logic shuffles including "Area Randomization."
- **SMZ3 (Crossover):** Fully supported as a single "Game" in the AP ecosystem. The logic tracks dependencies across both ROMs (e.g., requiring a Zelda item to unlock a Metroid sector).
- **Super Mario World (SMW):** Transforms the vanilla linear platformer into an item-gated adventure. Abilities like "Spin Jump," "Run," and "Carry" are stripped and turned into network-distributable progression items.

---

## Useful Ideas for This Workspace
1. **Standardized Location IDs:** Using Archipelago's integer-based Location ID mapping is a fast way to cross-reference `RandomMetroidSolver` data with physical ROM offsets.
2. **Progression Bitmasking:** Archipelago uses specific RAM offsets (mirrored across games) to track "Items Received from Server." Studying these offsets is essential for writing custom ASM that reacts to external state.
3. **Graph-Based Logic Mapping:** The way Archipelago handles "Indirect Requirements" (Item A in Game X unlocks Path B in Game Y) is the best template for designing custom "Crossover" or "Multi-Stage" hack logic.
4. **SNI/WebSocket Tooling:** Integrating **SNI** into your local workspace allows you to write Python/Node scripts that can read/write SNES memory live without modifying the emulator source.

---

## Probably Out of Scope
- **Server Infrastructure:** Building a custom multiworld server is likely redundant; the existing Archipelago server (Python/Flask/WebSockets) is highly optimized.
- **Non-Standard Emulators:** Archipelago requires SNI-compatible emulators (Snes9x-NWA, Mesen 2, RetroArch). Trying to force sync on unsupported emulators is a significant engineering sink.

---

## Suggested Next Tasks
1. **[ ] Install SNI & SuperNintendoClient:** Observe the WebSocket traffic between a running game and the client to see the raw `ReceivedItems` packets.
2. **[ ] Review `smz3.py` (APWorld):** Examine the Archipelago source code for the SMZ3 logic to see how cross-game dependencies are programmatically defined.
3. **[ ] Trace "Item Received" Hook:** In a debugger (Mesen 2), find the ASM routine in an Archipelago-patched ALTTP ROM that listens for the "Incoming Item" RAM flag.
4. **[ ] Map SMW Ability Logic:** Document the RAM addresses SMW uses to "gate" the Spin Jump and Run abilities in an Archipelago seed.
5. **[ ] Script a "Logic Check":** Write a small local script that uses SNI to read the current "Items Collected" bitmask and compare it against a local progression graph.

## References
- **[Archipelago GitHub](https://github.com/ArchipelagoMW/Archipelago)** (Core Logic & APWorlds)
- **[SNI GitHub](https://github.com/alttpo/sni)** (The SNES Memory Bridge)
- **[Archipelago Documentation](https://archipelago.gg/tutorial)** (Technical & Player Guides)
