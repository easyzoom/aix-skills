# AIX Skills

English | [简体中文](README.zh-CN.md)

![AIX Skills Overview](docs/assets/aix-skills-overview.svg)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Skills](https://img.shields.io/badge/skills-72-7c3aed)
![Validation](https://img.shields.io/badge/validation-docker%20ready-16a34a)
![Agent Skills](https://img.shields.io/badge/agent--skills-public-0f766e)

AIX Skills is a public collection of Agent Skills, templates, and references for building repeatable AI workflows.

This repository uses a hybrid structure: first-party skills that can be used directly, templates and authoring guidance for creating new skills, and a curated directory of external resources.

## What Is An Agent Skill?

Agent Skills are task-specific instructions, scripts, and references that an AI agent can load only when they are relevant. A good skill teaches an agent when to use a workflow, how to execute it, and what mistakes to avoid.

![Anatomy of an Agent Skill](docs/assets/skill-anatomy.svg)

A good skill should have:

- Clear trigger conditions: when the agent should load it.
- A repeatable workflow: steps the agent can follow reliably.
- Lightweight context: core guidance in `SKILL.md`, heavy references in supporting files.
- Verifiable results: checks that prove the skill was used correctly.

## Repository Layout

```text
.
├── skills/                 # First-party skills maintained in this repo
├── template/               # Copyable templates for new skills
├── awesome/                # Curated external skill resources
├── docs/                   # Maintainer guides and publishing checklists
├── scripts/                # Repository validation tools
├── CONTRIBUTING.md         # Contribution guide
└── README.md
```

## Available Skills

| Skill | Purpose |
| --- | --- |
| `8051-mcu-debug` | Helps agents debug 8051-compatible MCU firmware, downloads, clocks, interrupts, and peripherals. |
| `avem-integration` | Helps agents integrate and evaluate Avem embedded C framework modules. |
| `ble-gatt-integration` | Helps agents integrate BLE GATT services, characteristics, MTU, security, and throughput. |
| `bootloader-debug` | Helps agents debug bootloaders, app jumps, firmware upgrade state, and rollback paths. |
| `canbus-integration` | Helps agents integrate CAN bus libraries, CANBus-Triple, MCP2515, filters, and bit timing. |
| `canopen-integration` | Helps agents integrate CANopen object dictionaries, NMT, SDO, PDO, heartbeat, and EDS/DCF files. |
| `cmbacktrace-integration` | Helps agents integrate CmBacktrace for Cortex-M crash reports and stack backtraces. |
| `cmsis-dsp-integration` | Helps agents integrate CMSIS-DSP math, FFT, filters, and fixed-point processing. |
| `cortex-m-debug` | Helps agents debug Cortex-M firmware, faults, startup code, and SWD/JTAG sessions. |
| `cortex-r5-debug` | Helps agents debug Cortex-R5 startup, TCM, MPU/cache, exceptions, interrupts, and core modes. |
| `crc-checksum-integration` | Helps agents implement and verify CRCs, checksums, byte coverage, and protocol integrity checks. |
| `embedded-app-example-libs` | Helps agents adapt embedded application examples without copying unsafe assumptions. |
| `embedded-buffer-queue-libs` | Helps agents integrate ring buffers, circular buffers, FIFOs, and MCU queues. |
| `embedded-data-parsing-libs` | Helps agents integrate cJSON, jsmn, inih, and small embedded parsers safely. |
| `embedded-debug-entry` | Routes embedded debugging requests to the right architecture or workflow skill. |
| `embedded-fault-debug` | Helps agents preserve and analyze crash, trap, fault, stack, and reset evidence. |
| `embedded-framework-libs` | Helps agents evaluate and integrate embedded C framework libraries such as PLOOC or Avem. |
| `embedded-input-libs` | Helps agents integrate MultiButton, FlexibleButton, and simple MCU input libraries. |
| `embedded-library-entry` | Routes embedded library integration and porting requests to the right library skill. |
| `embedded-linux-login-debug` | Helps agents choose a safe login method before debugging embedded Linux devices. |
| `embedded-peripheral-bringup` | Helps agents bring up GPIO, UART, SPI, I2C, PWM, ADC, timers, DMA, and interrupts. |
| `embedded-serial-log-debug` | Helps agents collect and trust serial UART logs, boot consoles, and missing-output evidence. |
| `embedded-state-machine-libs` | Helps agents integrate embedded state-machine libraries and event-driven workflows. |
| `embedded-timing-libs` | Helps agents integrate MultiTimer and lightweight software timer libraries. |
| `easylogger-integration` | Helps agents integrate EasyLogger output, timestamps, filters, and embedded log backends. |
| `epd-integration` | Helps agents integrate e-paper displays, busy timing, framebuffer layout, and refresh modes. |
| `esp-idf-integration` | Helps agents integrate ESP-IDF components, sdkconfig, partitions, bootloader, NVS, Wi-Fi, BLE, and flash. |
| `fatfs-integration` | Helps agents integrate FatFs disk I/O, FAT/exFAT configuration, and file persistence. |
| `flashdb-integration` | Helps agents integrate FlashDB KVDB/TSDB storage on MCU flash or file backends. |
| `freemodbus-integration` | Helps agents integrate FreeModbus RTU, ASCII, TCP, ports, timers, and register callbacks. |
| `freertos-kernel-debug` | Helps agents debug FreeRTOS tasks, priorities, stacks, heap, tick, ISR APIs, and deadlocks. |
| `freertos-plus-tcp-integration` | Helps agents integrate FreeRTOS+TCP network drivers, buffers, sockets, and IP tasks. |
| `hardware-interface-debug` | Helps agents debug board-level power, reset, clock, pin, and signal issues. |
| `heatshrink-integration` | Helps agents integrate heatshrink compression, streaming buffers, and decompression checks. |
| `letter-shell-integration` | Helps agents integrate letter-shell command consoles and guard debug commands. |
| `littlefs-integration` | Helps agents integrate littlefs with MCU block devices and verify persistence safely. |
| `low-power-debug` | Helps agents debug sleep, wakeup, current consumption, and low-power mode failures. |
| `lvgl-integration` | Helps agents integrate LVGL displays, input devices, ticks, buffers, and GUI performance. |
| `lwip-integration` | Helps agents integrate lwIP netifs, sys_arch, memory pools, DHCP, TCP, and UDP. |
| `mbedtls-integration` | Helps agents integrate mbedTLS entropy, certificates, TLS handshakes, and secure transports. |
| `mcu-flashing-debug` | Helps agents debug MCU flashing, erase, program, verify, and probe connection failures. |
| `mcuboot-integration` | Helps agents integrate MCUboot secure boot, flash slots, image signing, swap, and rollback. |
| `micro-ecc-integration` | Helps agents integrate micro-ecc ECDH, ECDSA, keys, RNG, and signatures. |
| `miniz-integration` | Helps agents integrate miniz compression, DEFLATE/zlib data, ZIP archives, and embedded buffers. |
| `mqtt-embedded-integration` | Helps agents integrate embedded MQTT clients, keepalive, QoS, TLS, and reconnect flows. |
| `nanopb-integration` | Helps agents integrate nanopb Protocol Buffers generation, encoding, and decoding. |
| `nrf-connect-sdk-integration` | Helps agents integrate Nordic nRF Connect SDK, Zephyr, BLE, Partition Manager, DFU, and nrfx. |
| `nr-micro-shell-integration` | Helps agents integrate nr_micro_shell tiny command consoles and bounded CLI buffers. |
| `openocd-jlink-stlink-debug` | Helps agents debug OpenOCD, J-Link, ST-Link, probe attach, reset, flash, and GDB sessions. |
| `openthread-integration` | Helps agents integrate OpenThread radio platforms, commissioning, datasets, and mesh behavior. |
| `ota-update-integration` | Helps agents design and debug OTA package, transport, validation, activation, and rollback flows. |
| `plooc-integration` | Helps agents integrate PLOOC object-oriented C patterns into embedded modules. |
| `power-management-integration` | Helps agents integrate embedded power-management frameworks and device suspend/resume flows. |
| `qspi-xip-flash-debug` | Helps agents debug QSPI/OSPI flash, XIP, memory-mapped mode, boot, timing, and cache issues. |
| `readme-writing` | Helps agents create attractive, trustworthy, quickstart-friendly README files. |
| `riscv-mcu-debug` | Helps agents debug RISC-V MCU firmware, traps, CSRs, startup code, and OpenOCD/GDB sessions. |
| `rt-thread-integration` | Helps agents integrate RT-Thread BSPs, components, FinSH, device framework, DFS, and networking. |
| `rtos-debug` | Helps agents debug embedded RTOS tasks, stacks, priorities, queues, mutexes, and interrupts. |
| `segger-rtt-integration` | Helps agents integrate SEGGER RTT logs, control blocks, buffers, and J-Link terminal I/O. |
| `sensor-driver-integration` | Helps agents integrate MCU sensor drivers, bus transport, interrupts, FIFO, timing, and calibration. |
| `skill-writing-guide` | Teaches agents how to write concise, discoverable, testable skills for this repository. |
| `stm32-hal-ll-integration` | Helps agents integrate STM32 HAL/LL, CubeMX code, clocks, GPIO, DMA, NVIC, and callbacks. |
| `tjpgd-integration` | Helps agents integrate TJpgDec embedded JPEG decoding, callbacks, buffers, and display output. |
| `tinymaix-integration` | Helps agents integrate TinyMaix MCU inference, model loading, tensors, and memory. |
| `tinycrypt-integration` | Helps agents integrate TinyCrypt primitives, modes, nonces, tags, and test vectors. |
| `tinyusb-integration` | Helps agents integrate TinyUSB device, host, descriptors, endpoints, and USB classes. |
| `u8g2-integration` | Helps agents integrate U8g2 displays, bus callbacks, fonts, and small embedded UI. |
| `unity-ceedling-integration` | Helps agents add Unity, Ceedling, CMock, fixtures, and CI tests for embedded C. |
| `webpage-to-markdown` | Converts a public webpage URL into clean Markdown content. |
| `ymodem-xmodem-integration` | Helps agents integrate XMODEM/YMODEM serial transfer and bootloader update flows. |
| `zephyr-integration` | Helps agents integrate Zephyr RTOS, west builds, devicetree, Kconfig, drivers, and board support. |
| `zoom-shell-integration` | Helps agents integrate embedded zoom-shell style command consoles safely. |

Each skill lives in its own folder under `skills/` and uses `SKILL.md` as the entry point.

## Quickstart

Copy a skill folder into your agent's skill directory, or install it with the skill manager used by your environment if supported.

```bash
cp -R skills/webpage-to-markdown ~/.claude/skills/
```

To create a new skill, start from the template:

```bash
cp -R template/skill-template skills/my-new-skill
```

Then edit `skills/my-new-skill/SKILL.md` and run validation:

```bash
python3 scripts/validate-skills.py
```

## Design Principles

![Repeatable AI Workflow](docs/assets/repeatable-workflow.svg)

- **Small core, rich references**: keep `SKILL.md` fast to scan; move long API references or scripts into supporting files.
- **Trigger-first descriptions**: frontmatter descriptions should say when to use a skill, not summarize every step.
- **One excellent example**: prefer one realistic example over many generic snippets.
- **Public-ready by default**: avoid secrets, private links, company-only assumptions, or unlicensed copied content.
- **Verification matters**: include checks so contributors can prove their skill works.

## References

This repository is inspired by:

- [google/skills](https://github.com/google/skills) for product-focused skill packs.
- [anthropics/skills](https://github.com/anthropics/skills) for skill structure, templates, and examples.
- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) for curated skill discovery.

## Contributing

Contributions are welcome. Read `CONTRIBUTING.md` before opening a pull request, and run:

```bash
python3 scripts/validate-skills.py
```

## License

MIT. See `LICENSE`.
