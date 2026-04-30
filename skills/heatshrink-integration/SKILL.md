---
name: heatshrink-integration
description: Use when integrating, porting, configuring, or debugging heatshrink embedded compression, decompression, streaming buffers, window sizes, or firmware/resource compression
---

# heatshrink Integration

## Overview

Use this skill to integrate heatshrink by fixing memory budget, window/lookahead sizes, stream chunking, and decompression safety. Compression bugs often come from mismatched encoder/decoder settings or insufficient output buffers.

## When To Use

Use this skill when:

- The user wants heatshrink compression/decompression on an MCU.
- The task involves compressed logs, resources, firmware chunks, OTA payloads, or serial transfer compression.
- Decompression fails, output is truncated, memory is too high, or compressed data is incompatible.

Do not use this skill for general archive formats like gzip/zip unless heatshrink is specifically involved.

## First Questions

Ask for:

- Use case: logs, UI assets, firmware chunks, telemetry, or storage.
- Encoder and decoder settings: window size and lookahead.
- Streaming or one-shot mode.
- Input/output maximum sizes and RAM budget.
- Whether compressed data comes from host tools or target firmware.
- Current error or mismatch symptom.

## Integration Checklist

1. Match settings.
   Encoder and decoder window/lookahead parameters must match.

1. Bound buffers.
   Define maximum compressed input chunk, output chunk, and decompressed size.

1. Choose streaming model.
   Plan how input is sunk, polled, and flushed without blocking.

1. Validate data integrity.
   Pair compression with CRC/hash when data corruption matters.

1. Test worst case.
   Some data expands or compresses poorly; do not assume size savings.

## Common Failures

- Host encoder uses different window/lookahead than MCU decoder.
- Output buffer too small and caller treats partial output as complete.
- Decompressor waits for more data because finish/flush was not called.
- Compressed firmware lacks CRC before flash write.
- Worst-case expansion exceeds allocated storage.

## Verification

Before claiming heatshrink works:

- State window/lookahead, streaming mode, and buffer sizes.
- Confirm round-trip test for representative and worst-case data.
- Confirm truncated/corrupt data fails safely.
- Confirm integrity check if used for firmware or persistent assets.

## Example

User:

```text
用 heatshrink 压缩资源，设备端解压出来缺尾巴。
```

Agent:

1. Asks for encoder settings, decoder settings, chunk sizes, and finish/flush handling.
1. Checks partial-output loop and output buffer handling.
1. Verifies round-trip and truncated-input behavior.
