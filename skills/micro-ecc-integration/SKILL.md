---
name: micro-ecc-integration
description: Use when integrating, porting, configuring, or debugging micro-ecc ECDH, ECDSA, elliptic-curve keys, RNG, signatures, or embedded ECC operations
---

# micro-ecc Integration

## Overview

Use this skill to integrate micro-ecc by treating randomness, key storage, curve choice, and test vectors as security-critical. ECC that compiles but uses weak RNG or mismatched key formats is not working.

## When To Use

Use this skill when:

- The user wants ECDH, ECDSA, public/private key generation, signature verification, or ECC on an MCU using micro-ecc.
- The issue involves bad signatures, key mismatch, RNG, curve selection, endian/format mismatch, or slow scalar multiplication.

Do not use this skill for full TLS stacks. Use `mbedtls-integration` for TLS.

## First Questions

Ask for:

- Curve, operation, and protocol using ECC.
- Target MCU, compiler, and whether hardware TRNG/crypto exists.
- RNG source and key storage policy.
- Public/private key byte format and endian expectations.
- Test vector, signature, or verification failure details.

## Integration Checklist

1. Choose curve deliberately.
   Match peer requirements and security level.

1. Provide real RNG.
   Key generation and ECDSA require strong randomness. Do not use pseudo-random test stubs in production.

1. Verify key formats.
   Public key layout, private key length, endian, and compressed/uncompressed format must match protocol.

1. Run known test vectors.
   Validate sign/verify or shared-secret derivation against expected data.

1. Protect secrets.
   Do not log private keys, nonces, or raw secrets.

## Common Failures

- Weak or deterministic RNG used in production.
- Public key format mismatches peer protocol.
- Curve mismatch between device and server.
- Signature verification uses hashed versus unhashed data inconsistently.
- Stack buffers expose private key material in logs or dumps.

## Verification

Before claiming micro-ecc works:

- State curve, operation, key format, and RNG source.
- Confirm known test vectors pass.
- Confirm negative verification fails for modified data.
- Confirm secrets are not logged and storage policy is explicit.

## Example

User:

```text
micro-ecc 签名服务器验不过。
```

Agent:

1. Asks for curve, key format, hash/sign input, RNG, and server expected format.
1. Checks endian and hashed-versus-raw message handling.
1. Verifies with known vectors before changing protocol code.
