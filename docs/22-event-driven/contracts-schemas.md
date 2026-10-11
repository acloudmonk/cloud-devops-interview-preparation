# Event Contracts and Schema Evolution

[← Partitioning and scaling](partitioning-scaling.md) · [Next: Processing state, replay, and consistency →](processing-state-replay.md)

## Contract ownership

The producer owns the meaning and quality of an integration event; consumers own
their reactions. A central platform can govern envelope, registry, compatibility,
and discovery without becoming the owner of every business schema. Publish purpose,
semantics, examples, data classification, SLO, ordering key, and deprecation policy.

## Envelope and payload

Use a consistent envelope for event ID, type, source, subject/key, schema version,
occurrence time, publication time, correlation, causation, trace context, tenant or
partition context where appropriate, and classification. CloudEvents can standardize
event metadata; AsyncAPI can describe channels and operations. Neither defines your
domain meaning automatically.

## Compatibility

Additive optional fields with stable meaning are usually safest. Consumers should
ignore unknown fields and distinguish absent from null. Avoid changing units, type,
enumeration meaning, key, or required behavior silently. Removing or renaming fields
requires an overlap and migration plan. Compatibility tooling checks structure;
consumer contract tests and production evidence check meaning.

## Version strategies

Evolve in place when change remains compatible. Use a new event type or destination
for intentionally incompatible meaning, not every minor field addition. If two
versions coexist, define publication duration, ownership, translation, replay, and
retirement. Do not mutate historical records to pretend they were emitted under a
new semantic contract.

## Event-carried state versus notification

A rich event reduces synchronous callbacks and preserves historical context but
duplicates data and expands privacy and compatibility scope. A thin notification is
small but creates availability coupling to the source during consumption or replay.
Select per consumer freshness, privacy, throughput, and autonomy needs.

## Governance and discovery

Maintain a searchable catalog of owners, producers, destinations, schemas, keys,
classifications, consumers, retention, SLOs, and lifecycle. Gate incompatible change,
secret/PII leakage, unowned destinations, and excessive payloads in delivery. Runtime
inventory is still required because declared consumers and actual access can diverge.
