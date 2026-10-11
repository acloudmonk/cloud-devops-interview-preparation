# Organization and Migration

[← Observability and operations](observability-operations.md) · [Next: Enterprise design exercise →](design-exercise.md)

## Sociotechnical architecture

Align long-lived teams to business capabilities and give them authority over code,
contracts, data, delivery, SLO, cost, and lifecycle. Platform teams supply paved
roads; enabling teams help adoption. Central architecture should govern important
constraints and evolution, not approve every service decision.

## Distributed-monolith symptoms

- every feature changes and deploys many services together;
- services share tables, domain libraries, or one release train;
- synchronous call chains are long and failure-correlated;
- no team owns end-to-end business outcomes or data;
- staging must contain the entire estate for any useful test;
- one platform or identity failure disables every journey.

The remedy may be merging services, redrawing domains, changing ownership, removing
synchronous hops, or improving platform capability—not creating more services.

## Incremental modernization

Use business outcomes and change pain to select a capability. Establish observability
and tests, create an anti-corruption layer, route a small slice through a strangler
boundary, transfer data authority explicitly, compare outcomes, and retire old paths.
Dual writes require failure/reconciliation design and should be time-bound.

## Migration decisions

Prefer extraction where independent change, scaling, security, or ownership value
is clear. Leave cohesive stable modules in place. Avoid extracting shared utilities
first because they create dependencies without business autonomy. Record rollback,
data synchronization, contract overlap, and retirement criteria for each wave.

## Governance and economics

Limit languages, frameworks, protocols, and stores based on support capacity, while
allowing justified exceptions. Measure lead time, coordination, change failure,
recovery, reliability, cognitive load, and cost per business transaction. Service
count and repository count are not transformation outcomes.
