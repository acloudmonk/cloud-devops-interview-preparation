# Python Language and Data Contracts

[← Decision model](concepts.md) · [Next: CLI and configuration →](cli-configuration.md)

Separate pure decisions from side effects. A small domain layer should accept typed,
validated values and return a plan; adapters call files, APIs, clocks, and clouds.

## Structure

- Use modules/packages by responsibility, not one growing script.
- Keep orchestration thin; inject clients, time, randomness, and configuration.
- Use functions for transformations and classes where lifecycle/state earns them.
- Add type hints at boundaries; static checks reduce ambiguity but do not validate input.
- Use dataclasses or validated models for explicit records; avoid unstructured dictionaries.
- Prefer iterators/streaming for large inventories; materialize only when required.

## Data correctness

Validate schema, required fields, types, ranges, identifiers, timezone, encoding,
duplicates, and unknown fields before mutation. Preserve decimal and datetime
semantics where business accuracy matters. Treat YAML, JSON, CSV, environment,
and API responses as untrusted inputs with versioned contracts.

## Exceptions and results

Catch exceptions only when adding context, translating a boundary error, retrying a
known transient condition, compensating, or producing an owned result. Preserve the
cause. Distinguish validation, authentication, authorization, throttling, conflict,
not-found, timeout, service, and internal defects. Never return success after silently
skipping unknown failures.

## Review test

Can core logic run without network credentials? Are side effects explicit? Can a
caller distinguish changed, unchanged, skipped, failed, and uncertain outcomes?
