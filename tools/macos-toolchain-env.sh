#!/usr/bin/env bash

export PATH="/opt/homebrew/opt/dotnet@9/bin:/opt/homebrew/opt/rustup/bin:$HOME/.cargo/bin:$PATH"
export DOTNET_ROOT="/opt/homebrew/opt/dotnet@9/libexec"
export DOTNET_ROLL_FORWARD="${DOTNET_ROLL_FORWARD:-Major}"

export SNES_DOTNET_8="/opt/homebrew/opt/dotnet@8/bin/dotnet"
export SNES_DOTNET_9="/opt/homebrew/opt/dotnet@9/bin/dotnet"
