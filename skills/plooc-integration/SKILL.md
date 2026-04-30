---
name: plooc-integration
description: Use when integrating, evaluating, refactoring, or debugging PLOOC object-oriented C patterns, class-like modules, inheritance-style structures, or embedded C architecture
---

# PLOOC Integration

## Overview

Use this skill when PLOOC is being used to structure embedded C code. Treat it as an architectural tool: apply it only where object-style boundaries reduce real complexity, and verify that initialization, ownership, memory layout, and call paths remain understandable.

## When To Use

Use this skill when:

- The user mentions PLOOC, Protected Low-level Object-Oriented C, object-oriented C, class-like C modules, inheritance-style structs, or virtual tables in embedded C.
- A legacy driver/module is being wrapped into a clearer interface.
- The issue involves macro-heavy abstractions, initialization order, object lifetime, or callback dispatch.

Do not use this skill for simple drivers where plain C structs and functions are clearer.

## First Questions

Ask for:

- PLOOC source/version and target compiler.
- Module or driver being refactored.
- What problem PLOOC should solve: polymorphism, encapsulation, testability, shared interface, or reuse.
- Memory allocation policy and object lifetime.
- Existing module boundaries and call graph.

## Integration Checklist

1. Validate the abstraction need.
   Use PLOOC only where multiple implementations or strong encapsulation matter.

1. Define object ownership.
   Initialization, lifetime, deinitialization, and static versus dynamic allocation must be explicit.

1. Keep macros local.
   Avoid spreading framework macros through unrelated application code.

1. Preserve debuggability.
   Ensure call paths, object state, and virtual dispatch remain inspectable in GDB or logs.

1. Migrate one module first.
   Do not convert the entire project before proving the pattern improves one bounded area.

## Common Failures

- Framework added for style rather than a real interface problem.
- Macro expansion hides control flow and makes debugging harder.
- Object memory is static in one path and dynamic in another.
- Initialization order depends on hidden global state.
- Inheritance-like structure makes driver timing harder to reason about.

## Verification

Before claiming PLOOC integration works:

- State the interface problem PLOOC solves.
- Confirm object lifetime and allocation policy.
- Confirm one module works through the new interface and old behavior is preserved.
- Confirm debug/log visibility for object state and dispatch.

## Example

User:

```text
想用 PLOOC 重构几个传感器驱动。
```

Agent:

1. Asks whether drivers share a common interface and lifecycle.
1. Starts with one sensor family instead of whole-project migration.
1. Verifies init/read/deinit behavior and checks that debugging remains clear.
