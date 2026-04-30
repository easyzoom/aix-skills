---
name: openocd-jlink-stlink-debug
description: Use when debugging OpenOCD, J-Link, ST-Link, CMSIS-DAP, probe connection, reset scripts, flash algorithms, GDB attach, semihosting, RTT, or SWD/JTAG failures
---

# OpenOCD J-Link ST-Link Debug

## Overview

Use this skill to debug probe sessions by separating physical wiring, probe
firmware, target voltage, reset strategy, transport, target script, flash
algorithm, and GDB behavior. Probe failures are often reset or adapter issues.

## When To Use

Use this skill when:

- The user cannot connect, halt, reset, flash, erase, verify, or attach with
  OpenOCD, J-Link, ST-Link, CMSIS-DAP, pyOCD, or GDB.
- The issue involves SWD/JTAG wiring, adapter speed, reset config, target
  scripts, flash loaders, protected devices, semihosting, RTT, or multicore.
- The same firmware behaves differently under debugger and standalone boot.

Do not use this skill for application fault analysis after a stable debug
session exists. Use the architecture-specific debug skill then.

## First Questions

Ask for:

- Probe model, firmware version, debugger tool, target MCU/SoC, board, and OS.
- Wiring: VTref, GND, SWDIO/TMS, SWCLK/TCK, reset, SWO, and power ownership.
- Exact command, config scripts, adapter speed, transport, and full log.
- Reset mode, boot pins, readout protection, low-power state, and external flash.
- Whether connect-under-reset, halt-after-reset, or attach-to-running is needed.

## Debug Workflow

1. Prove physical connection.
   Check target voltage, ground, cable length, pinout, reset line, and whether
   the probe powers or only senses the target.

1. Lower the adapter speed.
   Start slow, then increase only after IDCODE, halt, reset, and memory reads
   are stable.

1. Pick the right reset strategy.
   Test software reset, hardware reset, connect-under-reset, and boot pin modes.

1. Validate target scripts.
   Confirm transport, chip family, TAP/SWD IDs, flash bank, work area, and
   multicore selection.

1. Separate attach from flash.
   First connect and halt, then read memory/registers, then erase/program/verify.

1. Add extras last.
   Enable semihosting, SWO, RTT, trace, or external flash loaders only after the
   base debug path is reliable.

## Common Failures

- VTref is missing, so the probe cannot sense target voltage.
- Adapter speed is too high for early boot, low-power state, or long wires.
- Reset line is not connected but the script assumes hardware reset.
- Device is readout-protected or locked.
- OpenOCD target script selects the wrong flash bank or work-area RAM.
- External flash programming needs a board-specific loader, not a generic one.

## Verification

Before claiming the debug path works:

- State probe, tool, command, transport, adapter speed, and reset mode.
- Confirm IDCODE or target detection, halt, register read, and memory read.
- Confirm erase/program/verify when flashing is part of the requirement.
- Confirm standalone boot still works after debugger-specific settings.

## Example

User:

```text
OpenOCD 连 STM32 一直 timeout。
```

Agent:

1. Checks VTref, ground, SWD pins, reset line, and adapter speed.
1. Tries connect-under-reset with the correct STM32 target script.
1. Separates connection evidence from flash-programming errors.
