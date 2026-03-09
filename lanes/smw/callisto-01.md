# Callisto 01

This note classifies `callisto` inside the SMW lane.

## Local repo

Local path:

- `/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/repos/callisto`

Current local commit:

- `299b352`

## Classification

`callisto` belongs in the SMW lane as:

- build-system lane
- project orchestration lane
- ROM-production workflow lane

It is not primarily:

- a disassembly/source lane like `SMWDisX`
- a direct editor like Lunar Magic

## What it does

From the repo README, `callisto` is:

- a build-system for Super Mario World projects
- focused on git-compatibility and flexibility

The listed features are the important part:

- automated building and packaging of SMW projects
- multiple emulator support
- multiple build profiles
- modules for globally shareable code/data
- conflict detection between tools, patches, and resources
- global clean ROM support
- automatic resource exports from Lunar Magic
- automatic ROM reloading in Lunar Magic after successful builds
- standardized TOML configuration

That makes it one of the clearest examples so far of how mature SMW projects stop treating the ROM as the only source of truth.

## Engineering significance

`callisto` suggests an SMW workflow split like this:

1. source assets, patches, modules, and config live in git
2. a clean base ROM is referenced globally rather than copied per project
3. tools and patches are orchestrated into a generated ROM
4. editor outputs and ROM outputs are synchronized automatically

That is structurally closer to a modern build pipeline than to ad hoc single-patch hacking.

## Low-level signals from the repo

The repo includes:

- CMake-based native code
- embedded `asar` DLL bindings
- patch application logic
- initial-patch support through `FLIPS`
- TOML configuration templates that reference a clean SMW ROM

Representative local files:

- [README.md](/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/repos/callisto/README.md)
- [CMakeLists.txt](/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/repos/callisto/CMakeLists.txt)
- [user.toml](/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/repos/callisto/callisto/toml_config/user/user.toml)
- [initial_patch.cpp](/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/repos/callisto/callisto/insertables/initial_patch.cpp)
- [patch.cpp](/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/repos/callisto/callisto/insertables/patch.cpp)
- [module.cpp](/Users/theysayheygreg/clawd/projects/reverse-engineering-games/snes/repos/callisto/callisto/insertables/module.cpp)

## How it fits the SMW lane

The SMW lane now has three distinct artifact types:

- `SMWDisX`: source/disassembly and RAM-map understanding
- Lunar Magic: editor-driven ROM modification workflow
- `callisto`: build-system/orchestration workflow

That is already a useful shape for the lane, because it mirrors how the SMW community actually works:

- understand the base game
- edit rich structured content
- orchestrate patches/tools/resources into a reproducible ROM output

## Next implication

Once we have the base SMW ROM, `callisto` becomes more actionable.

The next concrete questions are:

- which SMW revision should the workspace standardize on
- whether `callisto` assumes SMW U 1.00 in practice for most projects
- whether a macOS build/run lane for `callisto` is worthwhile, or if it should stay a reference workflow note for now
