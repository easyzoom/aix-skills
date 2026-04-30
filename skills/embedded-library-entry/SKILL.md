---
name: embedded-library-entry
description: Use when integrating, porting, configuring, or debugging third-party MCU embedded C libraries in bare-metal or RTOS projects
---

# Embedded Library Entry

## Overview

Use this skill as the entry point for MCU library integration work. Classify the library type, target platform, runtime model, resource limits, and required porting layer before routing to a specific library skill.

## When To Use

Use this skill when:

- The user wants to add, port, configure, or debug an embedded C library.
- The task involves MCU storage, logging, crash diagnosis, shell commands, filesystems, protocol stacks, UI, parsers, buttons, timers, queues, or state machines.
- The target may be bare metal, RTOS-based, or resource-constrained.

Do not use this skill when the problem is only board bring-up, flashing, serial logs, or architecture faults. Use the embedded debug skills first.

## First Questions

Ask only what is needed to route:

- Library name and version or source repository.
- Target MCU/SoC, compiler, and build system.
- Runtime model: bare metal, FreeRTOS, RT-Thread, Zephyr, Linux, or unknown.
- Memory/storage resources: RAM, flash, block device, filesystem, heap, stack, and whether dynamic allocation is allowed.
- Existing porting layer: file I/O, flash driver, UART, timebase, mutex, malloc, display, network, or shell transport.
- Current task: first integration, compile error, link error, runtime failure, performance issue, or data corruption.

## Routing Guide

| Library or task | Prefer |
| --- | --- |
| littlefs filesystem or block device | `littlefs-integration` |
| FlashDB KV/time-series database | `flashdb-integration` |
| EasyLogger output, filters, async logs | `easylogger-integration` |
| Cortex-M crash backtrace with CmBacktrace | `cmbacktrace-integration` |
| letter-shell command shell | `letter-shell-integration` |
| MCU flash, erase, verify, or programmer failure | `mcu-flashing-debug` |
| UART transport or missing logs | `embedded-serial-log-debug` |
| RTOS task, mutex, queue, stack issue | `rtos-debug` |
| Board power, reset, pin, or signal issue | `hardware-interface-debug` |

## Workflow

1. Route by library responsibility.
   Identify whether the library depends on storage, UART, RTOS primitives, heap, timers, display, network, or flash erase/program operations.

1. Confirm platform contracts.
   Ask for the porting hooks the library expects and the project already provides.

1. Preserve data and flash.
   Formatting filesystems, erasing database partitions, wiping logs, or changing flash layout requires explicit user approval.

1. Keep integration minimal.
   Bring up one smallest working path before enabling optional features such as async logging, wear leveling stress tests, shell authentication, or compression.

1. Verify with a target-relevant scenario.
   A library compiles successfully only proves syntax. Require a read/write, log, shell command, or crash capture that exercises the port layer.

## Verification

Before moving to a specific library workflow:

- State the selected library skill and why.
- State target MCU/RTOS/compiler/build system if known.
- Identify required porting hooks and missing inputs.
- Confirm no data-destructive action has been recommended without approval.

## Common Mistakes

- Treating a library as portable because it compiles on desktop.
- Enabling all optional features before the minimal port works.
- Ignoring flash erase size, write alignment, and power-fail behavior.
- Debugging library logic before validating the porting layer.
- Assuming malloc, mutexes, time functions, or file APIs exist on bare metal.

## Example

User:

```text
我想在 STM32 项目里加 littlefs 保存配置。
```

Agent:

1. Routes to `littlefs-integration`.
1. Asks for flash layout, erase/program sizes, bad block assumptions, RTOS locking, and whether formatting is allowed.
1. Verifies mount, format-if-approved, file write, sync, reboot, and readback.
