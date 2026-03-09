# Super Metroid: PLM & Room State Deep Dive (001)

## Executive Summary
Super Metroid's engine is driven by two primary data-heavy structures: **PLMs (Post-Load Modifications)** and **Room State Headers**. PLMs handle nearly all interactivity (items, doors, toggles), while Room State Headers manage world progression by swapping room data based on "Events" (e.g., boss deaths). For a research workspace involving `RandomMetroidSolver` or `MapRandomizer`, understanding the pointer-heavy nature of Banks $84 (PLMs) and $8F (Rooms) is essential for mapping logic to ROM offsets.

---

## 1. PLM Understanding (Post-Load Modifications)
### What are PLMs?
PLMs are the "dynamic" layer of a room. Unlike tiles (which are static background data), PLMs are objects with associated code that execute every frame or upon specific triggers.

- **Storage (Bank $84):** This bank contains the PLM definitions, instruction lists, and the execution engine.
- **Loading:** When a room loads, the engine reads a list of PLM structs from the room data. Each struct typically contains:
  - **ID (2 bytes):** Pointer to the PLM definition in Bank $84.
  - **X/Y Position (1 byte each):** Position in 16x16 tile coordinates.
  - **Argument (2 bytes):** Used for door destinations, item types, or specific logic.
- **Update Loop:** The game maintains a "PLM Slot" table (usually 32 slots). Every frame, the engine iterates through active slots and executes their current "instruction" pointer.

### Key PLM Categories
- **Items:** All Missile tanks, Energy tanks, and upgrades are PLMs. When "collected," they trigger a PLM instruction to change the background tile to an "empty" state and set a bit in the save data.
- **Doors:** PLMs handle the door's "opening" animation and the transition logic.
- **Crumble/Speed Blocks:** These are PLMs that wait for Samus's collision or speed state to trigger a tile change.
- **Scroll Modifiers:** Invisible PLMs that lock/unlock camera scrolling in specific directions.

---

## 2. Room and State Structure (Bank $8F)
### Room Headers
Every room in the game starts with a header in Bank $8F. This header contains the "Static" room data (Area ID, Map X/Y, Width/Height). Crucially, it points to a **State Header**.

### State Headers & Event Logic
Super Metroid uses "States" to handle progression. A single room header can point to multiple "State" blocks. The engine evaluates these in a specific order:
1. **Event States:** "If Event $05 (Kraid Dead) is set, use *this* state."
2. **Boss States:** "If Boss in this area is dead, use *this* state."
3. **Morph/Power Bomb States:** Some rooms change based on whether Samus has specific equipment.
4. **Default State:** The fallback if no other conditions are met.

### Documentation Conventions
- **Metroid Construction (Wiki):** The standard for "Room Index" documentation.
- **Kejardon's Bank $8F Logs:** The definitive source for the exact byte-layout of every room state.
- **SMILE Logic:** Most community editors use a "Room-to-State" hierarchy that mirrors the ROM's pointer structure.

---

## 3. Randomizer Relationship
### Logic vs. ROM Structure
In projects like `RandomMetroidSolver`, the **Logic Layer** (JSON/YAML) and the **ROM Layer** (ASM/Hex) are usually decoupled but linked by **Location IDs**.

- **Item Randomizers:** These typically modify the **Argument** of an Item PLM or replace the PLM ID entirely.
- **Map Randomizers:** These are significantly more complex. They must rewrite the **Door PLM Arguments** (which point to transition data) and potentially re-calculate the **Room State Pointers** if room connections are shuffled.
- **Logic Mapping:** Randomizers map "Locations" (e.g., "Landing Site - Right Missile") to a specific `(RoomID, PLM_Index)` pair.

### Common Conflicts
- **Disassembly Differences:** `strager/supermetroid` (match-accuracy) vs. `sm_disassembly` (relocatable). If you are using `MapRandomizer`, ensure your offsets align with the relocatable labels in `sm_disassembly`, as standard randomizers often "move" data blocks to make room for new logic.

---

## 4. Technical Glossary
- **PLM ID:** A 2-byte pointer into Bank $84 where the object's properties begin.
- **Door Pointer:** A 2-byte pointer (usually in Bank $83) defining where a door transition leads.
- **Event Bit:** A flag in RAM (Bank $7E:D820 range) that signals world changes.
- **BTS (Behind the Scenes):** A 1-byte value per tile that provides extra metadata (like slope type or water level), often interacting with PLM collision logic.

---

## 5. Best Next Local Tasks
For a workspace containing `strager/supermetroid` and `RandomMetroidSolver`:

1. **[ ] Trace a PLM Collection:** Use a debugger (Mesen 2) to set a breakpoint on the "Item Collected" PLM routine. Trace how it sets the event bit and updates the RAM map.
2. **[ ] Map Location IDs to ROM Offsets:** Use the `RandomMetroidSolver` logic files to find the "Landing Site" location and verify the corresponding PLM offset in the `strager` disassembly.
3. **[ ] Header Analysis:** Write a small script to parse a Bank $8F Room Header and print out all associated State Header pointers.
4. **[ ] Door Transition Audit:** Use `MapRandomizer` logs to identify which Door PLM arguments are modified during a "shuffled" seed.
5. **[ ] PLM Instruction Hooking:** Attempt to write a small Asar patch that hooks into the PLM execution loop to log PLM IDs as they are processed in real-time.

## References
- **[Kejardon's Bank $84 / $8F Logs](http://jathys.zophar.net/supermetroid/kejardon/index.html):** The primary source for raw bank structure.
- **[Metroid Construction Wiki (PLMs)](https://metroidconstruction.com/wiki/PLM):** Best community-level summary of PLM types.
- **[sm-json-data (GitHub)](https://github.com/thefuzzlyn/sm-json-data):** The logic files used by most modern randomizers to link "Locations" to ROM data.
