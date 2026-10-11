# Data Models and Platform Selection

[← Decision model](concepts.md) · [Next: Transactions, consistency, and concurrency →](transactions-consistency.md)

## Select model before product

| Model | Strong fit | Primary caution |
| --- | --- | --- |
| Relational | Transactions, constraints, joins, flexible queries | Horizontal write scale and schema change need planning |
| Key-value | Known-key low-latency access at scale | Queries outside designed keys are limited or expensive |
| Document | Aggregate-shaped hierarchical data | Duplication and cross-document invariants |
| Wide-column | Large sparse datasets and key/range access | Query-first modeling and denormalization |
| Graph | Relationship traversal and connected queries | Partitioning, global traversal, and specialized operations |
| Time-series | Timestamped append and window queries | Cardinality, retention, downsampling, late data |
| Search | Relevance, text, filters, and facets | Usually derived, eventually consistent, not transaction authority |
| Vector | Approximate semantic similarity | Recall/latency/cost, metadata filtering, model/version drift |
| Object | Large immutable blobs and archival data | Limited query and transaction semantics |
| Analytical/columnar | Historical scans and aggregation | Poor fit for high-concurrency row transactions |

## Access-pattern-first design

List required reads and writes before schema design. For each, specify key/predicate,
sort/range, result size, frequency, latency, consistency, and transaction scope. A
NoSQL table often embeds or duplicates data so known access paths are single-partition.
A relational model can preserve normalized truth and add indexes or derived views.

## Polyglot persistence

Use multiple models only where workloads genuinely diverge. Keep one authoritative
write path and feed derived search, cache, graph, or analytics views through a reliable
change mechanism. Define lag, replay, deletion, and repair. Dual writes from application
code create ambiguity when one write succeeds and another fails.

## Operational fit

Evaluate ecosystem, drivers, connection behavior, schema tools, backup/restore,
monitoring, debugging, regional availability, quota, upgrade, export, and staff skill.
A theoretically perfect model that the organization cannot operate safely is not the
best choice. Prefer the smallest portfolio that satisfies material differences.

## Selection traps

- choosing NoSQL only because volume sounds large;
- choosing relational only because the team knows SQL;
- treating flexible schema as schema-free governance;
- using a cache or search engine as authority by accident;
- putting operational transactions and unrestricted analytics on the same capacity;
- selecting global writes without defining conflicts and invariant scope;
- assuming service-compatible APIs behave identically to the original engine.
