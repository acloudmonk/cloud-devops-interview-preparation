# Domain and Service Boundaries

[← Microservices decision model](concepts.md) · [Next: Communication and contracts →](communication-contracts.md)

## Model business language

Use domain discovery with business experts: capabilities, workflows, decisions,
events, policies, invariants, lifecycle, and language. A bounded context defines
where a model and its terms are consistent. The word “customer” may legitimately
mean different things in sales, billing, and support.

## Boundary signals

- related rules and data change together;
- one team can own the capability end to end;
- invariants fit inside one transactional boundary where possible;
- scale, security, availability, or cadence differs materially;
- the service exposes business behavior rather than database CRUD;
- consumers need the contract, not internal tables or implementation.

Avoid horizontal services such as “validation service” or “database service” that
force every business request across technical layers. Shared libraries can also
couple releases; use them for stable commodity behavior, not shared domain models.

## Context relationships

Document upstream/downstream ownership, published language, translation, and change
expectations. An anti-corruption layer protects a new context from legacy semantics.
APIs and events are contracts between contexts, not permission to share internal
models.

## Ownership and topology

One empowered team should own build, data, API/events, SLO, incident response,
cost, and retirement. Team cognitive load limits the number of services it can
operate. A service per individual or per endpoint fragments ownership and increases
coordination rather than reducing it.

## Boundary evolution

Boundaries are hypotheses. Track coordinated changes, synchronous call frequency,
shared queries, cross-service transactions, incidents, and team handoffs. Split or
merge when evidence shows different cohesion. Preserve consumer compatibility while
moving authority and data.
