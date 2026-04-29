---
name: embedded-debug-entry
description: Use when triaging embedded device, MCU, firmware, board bring-up, flashing, serial log, RTOS, bootloader, low-power, or peripheral debug requests
---

# Embedded Debug Entry

## Overview

Use this skill as the first stop for embedded debugging. The agent should classify the target, failure phase, access method, toolchain, and risk level, then route to the narrowest specialized skill instead of guessing from incomplete context.

## When To Use

Use this skill when:

- The user reports an embedded device, MCU, board, firmware, RTOS, bootloader, or peripheral issue.
- The architecture or debugging path is unclear.
- The task might involve flashing, serial logs, SWD/JTAG, UART, ADB, bootloaders, low power, or hardware signals.

Do not use this skill when the user already named a more specific skill path, such as Cortex-M HardFault, 8051 timer, RISC-V trap, or embedded Linux SSH login.

## First Questions

Ask only what is needed to route:

- Target type: MCU, embedded Linux device, mixed SoC, module, or unknown board.
- Architecture or chip family: Cortex-M, RISC-V, 8051, Linux-capable ARM, or unknown.
- Failure phase: cannot connect, cannot flash, no boot, crash/fault, no logs, peripheral failure, RTOS issue, bootloader issue, low-power issue.
- Available access: SWD/JTAG, serial UART, SSH, ADB, Telnet, local console, logic analyzer, oscilloscope, or vendor tool.
- Toolchain and artifacts: ELF/HEX/MAP, firmware log, programmer output, schematic, boot log, or fault dump.

## Routing Guide

Use the most specific path:

| Symptom or target | Prefer |
| --- | --- |
| Cortex-M MCU, SWD/JTAG, HardFault, startup | `cortex-m-debug` |
| 8051/51/STC/Nuvoton/Silabs C8051 | `8051-mcu-debug` |
| RISC-V MCU, OpenOCD/GDB, trap, CSR | `riscv-mcu-debug` |
| Embedded Linux login before debugging | `embedded-linux-login-debug` |
| Flash/download/verify/connect failure | `mcu-flashing-debug` |
| UART boot log, serial console,乱码, no logs | `embedded-serial-log-debug` |
| Crash, exception, trap, fault, stack corruption | `embedded-fault-debug` |
| GPIO/UART/SPI/I2C/PWM/ADC bring-up | `embedded-peripheral-bringup` |
| FreeRTOS, RT-Thread, Zephyr, scheduler issue | `rtos-debug` |
| Bootloader, app jump, OTA, upgrade state | `bootloader-debug` |
| Sleep, wakeup, current consumption, lost debug | `low-power-debug` |
| Power, reset, clock, pins, board-level signals | `hardware-interface-debug` |

## Workflow

1. Classify before acting.
   Do not start with code edits, reflashing, or resets until the target and failure phase are known.

1. Route to one primary skill.
   If multiple skills apply, pick the one closest to the current blocker. Example: "cannot flash Cortex-M" starts with `mcu-flashing-debug`, not general Cortex-M logic.

1. Collect minimal evidence.
   Ask for the smallest artifact that proves the current state: programmer error, serial log, GDB register dump, schematic snippet, or tool output.

1. Preserve safety boundaries.
   Treat erase, option bytes, boot config, security bits, fuses, production data, and power changes as explicit-approval actions.

1. Summarize the route.
   Tell the user which path you selected and why before continuing with detailed debug instructions.

## Verification

Before moving into a specialized workflow:

- State target class, architecture, failure phase, available access, and selected skill.
- State what evidence is already available and what is still missing.
- Confirm no destructive operation has been recommended without approval.

## Common Mistakes

- Treating every embedded issue as a firmware code problem.
- Asking for every possible tool output before choosing a debug path.
- Starting with flash erase when the failure is actually serial wiring or reset.
- Debugging application logic before proving the target boots and the image matches.
- Mixing Linux device login workflows with MCU bare-metal workflows.

## Example

User:

```text
板子起来以后没日志，也不知道是不是程序没跑。
```

Agent:

1. Asks for chip family, access methods, firmware artifact, and whether serial pins are known.
1. Routes to `embedded-serial-log-debug` if the first blocker is "no logs".
1. If serial is healthy but no heartbeat exists, routes to the architecture-specific startup workflow.
