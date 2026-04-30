# AIX Skills

[English](README.md) | 简体中文

![AIX Skills Overview](docs/assets/aix-skills-overview.svg)

AIX Skills 是一个公开的 Agent Skills 集合，提供可直接使用的 skills、创建 skills 的模板，以及精选外部资源目录。

本仓库采用混合型结构：一部分是自研 skills，一部分是模板和规范，另一部分是 awesome 资源索引。目标是让读者既能拿来用，也能照着规范贡献新的 skill。

## 什么是 Agent Skill？

Agent Skills 是面向特定任务的说明、脚本和参考资料，AI agent 可以在相关任务出现时动态加载。一个好的 skill 会告诉 agent 什么时候使用、如何执行，以及应该避免哪些错误。

![Anatomy of an Agent Skill](docs/assets/skill-anatomy.svg)

一个好的 skill 应该具备：

- 清晰的触发条件：什么时候应该加载它。
- 可重复的流程：agent 可以按步骤稳定执行。
- 轻量的上下文：主文件聚焦核心流程，重资料放到独立引用文件。
- 可验证的结果：说明如何检查 skill 是否被正确使用。

## 仓库结构

```text
.
├── skills/                 # 本仓库维护的自研 skills
├── template/               # 创建新 skill 的可复制模板
├── awesome/                # 精选外部 skills 和参考资源
├── docs/                   # 编写、维护和发布指南
├── scripts/                # 仓库校验工具
├── CONTRIBUTING.md         # 贡献指南
└── README.md
```

## 当前 Skills

| Skill | 用途 |
| --- | --- |
| `8051-mcu-debug` | 帮助 agent 调试 8051/51 单片机固件、下载、时钟、中断和外设问题。 |
| `avem-integration` | 帮助 agent 集成和评估 Avem 嵌入式 C 框架模块。 |
| `ble-gatt-integration` | 帮助 agent 集成 BLE GATT 服务、特征值、MTU、安全和吞吐。 |
| `bootloader-debug` | 帮助 agent 调试 bootloader、应用跳转、固件升级状态和回滚路径。 |
| `canbus-integration` | 帮助 agent 集成 CAN 总线库、CANBus-Triple、MCP2515、过滤器和位时序。 |
| `canopen-integration` | 帮助 agent 集成 CANopen 对象字典、NMT、SDO、PDO、心跳和 EDS/DCF。 |
| `cmbacktrace-integration` | 帮助 agent 集成 CmBacktrace，用于 Cortex-M 崩溃报告和调用栈回溯。 |
| `cmsis-dsp-integration` | 帮助 agent 集成 CMSIS-DSP 数学、FFT、滤波和定点处理。 |
| `cortex-m-debug` | 帮助 agent 调试 Cortex-M 固件、异常、启动代码和 SWD/JTAG 会话。 |
| `cortex-r5-debug` | 帮助 agent 调试 Cortex-R5 启动、TCM、MPU/cache、异常、中断和核心模式。 |
| `crc-checksum-integration` | 帮助 agent 实现和校验 CRC、checksum、字节覆盖范围和协议完整性检查。 |
| `embedded-app-example-libs` | 帮助 agent 改造嵌入式应用示例，同时避免复制不安全假设。 |
| `embedded-buffer-queue-libs` | 帮助 agent 集成 ring buffer、循环缓冲、FIFO 和 MCU 队列。 |
| `embedded-data-parsing-libs` | 帮助 agent 安全集成 cJSON、jsmn、inih 和小型嵌入式解析库。 |
| `embedded-debug-entry` | 将嵌入式调试请求路由到正确的架构或工作流 skill。 |
| `embedded-fault-debug` | 帮助 agent 保留并分析崩溃、trap、fault、栈和复位证据。 |
| `embedded-framework-libs` | 帮助 agent 评估和集成 PLOOC、Avem 等嵌入式 C 框架库。 |
| `embedded-input-libs` | 帮助 agent 集成 MultiButton、FlexibleButton 和简单 MCU 输入库。 |
| `embedded-library-entry` | 将嵌入式开源库集成和移植请求路由到正确的 library skill。 |
| `embedded-linux-login-debug` | 帮助 agent 在调试嵌入式 Linux 设备前选择安全的登录方式。 |
| `embedded-peripheral-bringup` | 帮助 agent bring up GPIO、UART、SPI、I2C、PWM、ADC、定时器、DMA 和中断。 |
| `embedded-serial-log-debug` | 帮助 agent 采集并验证串口日志、启动控制台和无输出问题证据。 |
| `embedded-state-machine-libs` | 帮助 agent 集成嵌入式状态机库和事件驱动工作流。 |
| `embedded-timing-libs` | 帮助 agent 集成 MultiTimer 和轻量软件定时器库。 |
| `easylogger-integration` | 帮助 agent 集成 EasyLogger 输出、时间戳、过滤器和嵌入式日志后端。 |
| `epd-integration` | 帮助 agent 集成电子纸显示、busy 时序、framebuffer 布局和刷新模式。 |
| `esp-idf-integration` | 帮助 agent 集成 ESP-IDF 组件、sdkconfig、分区、bootloader、NVS、Wi-Fi、BLE 和 flash。 |
| `fatfs-integration` | 帮助 agent 集成 FatFs disk I/O、FAT/exFAT 配置和文件持久化。 |
| `flashdb-integration` | 帮助 agent 在 MCU flash 或文件后端上集成 FlashDB KVDB/TSDB。 |
| `freemodbus-integration` | 帮助 agent 集成 FreeModbus RTU、ASCII、TCP、端口层、定时器和寄存器回调。 |
| `freertos-kernel-debug` | 帮助 agent 调试 FreeRTOS 任务、优先级、栈、heap、tick、ISR API 和死锁。 |
| `freertos-plus-tcp-integration` | 帮助 agent 集成 FreeRTOS+TCP 网卡驱动、buffer、socket 和 IP task。 |
| `hardware-interface-debug` | 帮助 agent 调试板级电源、复位、时钟、引脚和信号问题。 |
| `heatshrink-integration` | 帮助 agent 集成 heatshrink 压缩、流式 buffer 和解压校验。 |
| `letter-shell-integration` | 帮助 agent 集成 letter-shell 命令控制台并保护调试命令。 |
| `littlefs-integration` | 帮助 agent 将 littlefs 接入 MCU 块设备并安全验证持久化。 |
| `low-power-debug` | 帮助 agent 调试睡眠、唤醒、电流消耗和低功耗模式异常。 |
| `lvgl-integration` | 帮助 agent 集成 LVGL 显示、输入设备、tick、buffer 和 GUI 性能。 |
| `lwip-integration` | 帮助 agent 集成 lwIP netif、sys_arch、内存池、DHCP、TCP 和 UDP。 |
| `mbedtls-integration` | 帮助 agent 集成 mbedTLS 熵源、证书、TLS 握手和安全传输。 |
| `mcu-flashing-debug` | 帮助 agent 调试 MCU 烧录、擦除、写入、校验和下载器连接失败。 |
| `mcuboot-integration` | 帮助 agent 集成 MCUboot 安全启动、flash slots、镜像签名、swap 和回滚。 |
| `micro-ecc-integration` | 帮助 agent 集成 micro-ecc ECDH、ECDSA、密钥、RNG 和签名。 |
| `miniz-integration` | 帮助 agent 集成 miniz 压缩、DEFLATE/zlib 数据、ZIP archive 和嵌入式 buffer。 |
| `mqtt-embedded-integration` | 帮助 agent 集成嵌入式 MQTT client、keepalive、QoS、TLS 和重连流程。 |
| `nanopb-integration` | 帮助 agent 集成 nanopb Protocol Buffers 生成、编码和解码。 |
| `nrf-connect-sdk-integration` | 帮助 agent 集成 Nordic nRF Connect SDK、Zephyr、BLE、Partition Manager、DFU 和 nrfx。 |
| `nr-micro-shell-integration` | 帮助 agent 集成 nr_micro_shell 微型命令控制台和有界 CLI buffer。 |
| `openocd-jlink-stlink-debug` | 帮助 agent 调试 OpenOCD、J-Link、ST-Link、探针连接、reset、flash 和 GDB 会话。 |
| `openthread-integration` | 帮助 agent 集成 OpenThread radio 平台、入网、dataset 和 mesh 行为。 |
| `ota-update-integration` | 帮助 agent 设计和调试 OTA 包、传输、校验、激活和回滚流程。 |
| `plooc-integration` | 帮助 agent 将 PLOOC 面向对象 C 模式接入嵌入式模块。 |
| `power-management-integration` | 帮助 agent 集成嵌入式电源管理框架和设备 suspend/resume 流程。 |
| `qspi-xip-flash-debug` | 帮助 agent 调试 QSPI/OSPI flash、XIP、memory-mapped、启动、时序和 cache 问题。 |
| `readme-writing` | 帮助 agent 编写更有吸引力、更可信、带有清晰快速开始路径的 README。 |
| `riscv-mcu-debug` | 帮助 agent 调试 RISC-V MCU 固件、trap、CSR、启动代码和 OpenOCD/GDB 会话。 |
| `rt-thread-integration` | 帮助 agent 集成 RT-Thread BSP、组件、FinSH、设备框架、DFS 和网络。 |
| `rtos-debug` | 帮助 agent 调试嵌入式 RTOS 任务、栈、优先级、队列、互斥锁和中断。 |
| `segger-rtt-integration` | 帮助 agent 集成 SEGGER RTT 日志、control block、buffer 和 J-Link 终端 I/O。 |
| `sensor-driver-integration` | 帮助 agent 集成 MCU 传感器驱动、总线传输、中断、FIFO、时序和校准。 |
| `skill-writing-guide` | 指导 agent 为本仓库编写简洁、可发现、可验证的 skills。 |
| `stm32-hal-ll-integration` | 帮助 agent 集成 STM32 HAL/LL、CubeMX 代码、时钟、GPIO、DMA、NVIC 和回调。 |
| `tjpgd-integration` | 帮助 agent 集成 TJpgDec 嵌入式 JPEG 解码、回调、buffer 和显示输出。 |
| `tinymaix-integration` | 帮助 agent 集成 TinyMaix MCU 推理、模型加载、张量和内存。 |
| `tinycrypt-integration` | 帮助 agent 集成 TinyCrypt primitive、模式、nonce、tag 和测试向量。 |
| `tinyusb-integration` | 帮助 agent 集成 TinyUSB device、host、描述符、端点和 USB class。 |
| `u8g2-integration` | 帮助 agent 集成 U8g2 显示、总线回调、字体和小型嵌入式 UI。 |
| `unity-ceedling-integration` | 帮助 agent 为嵌入式 C 添加 Unity、Ceedling、CMock、fixtures 和 CI 测试。 |
| `webpage-to-markdown` | 将公开网页 URL 转换为干净的 Markdown 内容。 |
| `ymodem-xmodem-integration` | 帮助 agent 集成 XMODEM/YMODEM 串口传输和 bootloader 升级流程。 |
| `zephyr-integration` | 帮助 agent 集成 Zephyr RTOS、west build、devicetree、Kconfig、驱动和板级支持。 |
| `zoom-shell-integration` | 帮助 agent 安全集成嵌入式 zoom-shell 风格命令控制台。 |

每个 skill 都放在 `skills/` 下的独立目录中，并以 `SKILL.md` 作为入口文件。

## 快速开始

把某个 skill 复制到你的 agent skill 目录中，或使用你的运行环境支持的 skill 管理器安装。

```bash
cp -R skills/webpage-to-markdown ~/.claude/skills/
```

创建新 skill 时，从模板开始：

```bash
cp -R template/skill-template skills/my-new-skill
```

编辑 `skills/my-new-skill/SKILL.md` 后运行校验：

```bash
python3 scripts/validate-skills.py
```

## 设计原则

![Repeatable AI Workflow](docs/assets/repeatable-workflow.svg)

- **小核心，重参考外置**：`SKILL.md` 应该便于快速扫描，长参考资料放到 supporting files。
- **描述字段先写触发条件**：frontmatter 的 `description` 说明何时使用，而不是复述完整流程。
- **一个高质量示例胜过多个泛泛示例**：示例应该真实、可迁移。
- **默认适合公开发布**：避免 secrets、私有链接、公司内部假设和未授权复制内容。
- **结果必须可验证**：说明 agent 如何证明 skill 被正确使用。

## 参考项目

本仓库参考了：

- [google/skills](https://github.com/google/skills)：产品和 Google Cloud 方向的 skill packs。
- [anthropics/skills](https://github.com/anthropics/skills)：skill 结构、模板和示例。
- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)：按主题组织的 skills 资源目录。

## 贡献

欢迎贡献。提交 PR 前请阅读 `CONTRIBUTING.md`，并运行：

```bash
python3 scripts/validate-skills.py
```

## License

MIT. See `LICENSE`.
