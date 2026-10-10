# Images and Build Engineering

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

An image is a content-addressed artifact, not a miniature server. Good image
engineering controls inputs, layer contents, runtime configuration, platform
targets, reproducibility, attack surface, and feedback speed together.

## Image anatomy

An OCI image manifest references configuration and ordered compressed layers by
digest. The configuration records command, entrypoint, environment, working
directory, user, exposed ports, labels, and history. An image index can point to
multiple platform-specific manifests under one name.

Layers are immutable filesystem changes. At runtime, a snapshotter presents their
merged view and a writable layer. Deleting a file in a later layer hides it through
a whiteout; bytes can remain in an earlier layer and registry history. Never copy
a secret into a layer and expect a later `RUN rm` to remove it.

## Build context and inputs

The builder can access files in the build context and declared remote/build inputs.
Keep the context small with `.dockerignore`; exclude source-control metadata,
credentials, test output, local dependencies, and unrelated directories. A small
context improves transfer, cache stability, reviewability, and leak prevention.

Pin important inputs according to assurance need:

- base image by digest, with an owned update process;
- dependency lockfiles and trusted package sources;
- toolchain/build frontend versions;
- target operating system and architecture;
- build arguments that affect output.

Pinning freezes known content; it does not make that content safe or current.

## Layer and cache design

Order stable dependency inputs before frequently changing source. Combine related
package-manager update/install operations so index and packages are consistent,
but do not collapse everything into one opaque step. Use cache and secret mounts
where supported so transient credentials and package caches do not enter layers.

Cache keys must represent every material input. Partition writable cache by trust
boundary. A cache accelerates work; it is not an authoritative release artifact or
proof of origin.

## Multi-stage builds

Use a builder stage for compilers, headers, test tools, and dependency resolution;
copy only verified runtime outputs into a minimal final stage. This reduces size
and attack surface, but minimal must remain operable: certificates, timezone data,
user records, diagnostics, and required shared libraries still matter.

Distroless or `scratch` images are useful when their constraints are understood.
Do not optimize for the smallest byte count at the expense of patchability,
debuggability, provenance, or platform support.

## Determinism and multi-platform output

Control timestamps, locale, file ordering, generated metadata, dependency sources,
and network access where practical. Record source, base digest, build definition,
builder identity, and output digest.

An image built for `linux/amd64` will not natively execute on `linux/arm64`.
Emulation can help but may be slower and can hide native differences. Build each
target deliberately, test on representative architecture, and publish an image
index only after every platform artifact is verified.

## Build review checklist

- Is the build context minimal and secret-free?
- Are base images and dependencies identifiable and updateable?
- Does the build run tests before producing the final artifact?
- Does the final stage contain only runtime requirements and a non-root identity?
- Are package caches, temporary files, and build tools absent from runtime?
- Is the entrypoint signal-safe and configuration externalized?
- Are digest, SBOM, provenance, and vulnerability results connected to promotion?
