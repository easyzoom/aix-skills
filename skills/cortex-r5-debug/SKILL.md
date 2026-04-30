---
name: cortex-r5-debug
description: Use when debugging Cortex-R5 or Cortex-R cores, startup, TCM, MPU, caches, exceptions, GIC/VIC interrupts, lockstep/SMP modes, JTAG, or real-time firmware bring-up
---

# Cortex-R5 Debug

## Overview

Use this skill to debug Cortex-R5 systems by separating core mode, boot source, memory map, exception vectors, TCM, MPU/cache policy, interrupt controller, and safety configuration. Cortex-R5 failures often come from memory attributes, coherency, or lockstep/SMP setup rather than C code.

## When To Use

Use this skill when:

- The user is bringing up or debugging Cortex-R5, Cortex-R4, Cortex-R7, or similar Arm Cortex-R firmware.
- The issue involves early boot, exceptions, aborts, IRQ/FIQ, TCM, MPU, caches, tightly coupled memory, lockstep, split mode, SMP, or JTAG attach.
- The platform is an SoC with real-time cores, safety islands, motor/control firmware, storage controllers, or heterogeneous Linux + R5 systems.

Do not use this skill for Cortex-M microcontrollers. Use `cortex-m-debug` when the target has NVIC, VTOR, and M-profile exception behavior.

## First Questions

Ask for:

- SoC/board, exact core, boot owner, toolchain, debugger, and whether the R5 runs bare metal or an RTOS.
- Core mode: single core, split/SMP, lockstep, secure/non-secure, EL/privilege mode if applicable.
- Memory map: boot ROM, flash, DDR, OCM/SRAM, ATCM/BTCM, stacks, heaps, and linker script.
- Cache/MPU policy, TCM enablement, ECC initialization, and DMA/coherency paths.
- Exception/interrupt symptom, register dump, CPSR/SPSR, fault status, and disassembly around PC/LR.

## Debug Workflow

1. Prove debugger attach and reset control.
   Confirm JTAG target, reset type, halt behavior, core selection, and whether the other R5 core or A-core changes state.

1. Verify boot entry.
   Check reset vector, vector table location, stack pointers for each mode, C runtime init, and linker load/run addresses.

1. Stabilize memory first.
   Initialize TCM, SRAM/OCM, ECC, BSS/data, and stack before touching DDR or cached regions.

1. Configure MPU/cache deliberately.
   Mark device memory, TCM, SRAM, DDR, DMA buffers, and shared memory with correct attributes and barriers.

1. Decode exceptions.
   For undefined, prefetch abort, data abort, IRQ, and FIQ, capture CPSR/SPSR, LR, fault status/address, and instruction context.

1. Bring up interrupts separately.
   Validate vector routing, GIC/VIC setup, priority, CPU interface, stack mode, and interrupt clearing.

1. Add multicore/safety features last.
   Prove single-core execution before enabling lockstep comparison, split mode messaging, SMP scheduling, watchdogs, or safety monitors.

## Common Failures

- Linker script places vectors, stacks, or data in memory not initialized by the boot stage.
- ATCM/BTCM is assumed enabled or mapped when it is not.
- ECC-protected RAM is used before initialization, causing aborts.
- Device registers are mapped cacheable or normal memory.
- DMA buffers are cached without clean/invalidate barriers.
- IRQ/FIQ mode stacks are missing, so the first interrupt corrupts memory.
- Lockstep or split-mode configuration does not match the debugger/core being halted.

## Verification

Before claiming Cortex-R5 firmware works:

- State SoC, core mode, boot chain, memory map, and debugger path.
- Confirm reset-to-main with vectors, stacks, and C runtime initialized.
- Confirm MPU/cache attributes for code, data, device, DMA, and shared memory.
- Confirm at least one timer/interrupt path and one exception dump path.
- Confirm watchdog, lockstep/SMP, and inter-core communication behavior if used.

## Example

User:

```text
Cortex-R5 一开 D-cache 就随机 data abort。
```

Agent:

1. Asks for MPU regions, fault status/address, DMA buffers, and memory map.
1. Checks whether peripheral registers or shared buffers are marked cacheable.
1. Adds barriers and cache maintenance around DMA/shared memory before changing application logic.
