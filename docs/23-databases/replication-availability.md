# Replication, Availability, and Global Data

[← Schema and query design](schema-index-query.md) · [Next: Partitioning, sharding, and scale →](partitioning-sharding.md)

## Replication goals

Replicas can improve availability, durability, read scale, geographic latency, or
recovery, but one topology rarely optimizes all goals. Define source, replica count,
fault-domain placement, synchronous/asynchronous mode, acknowledgment quorum, election,
lag, read policy, failover, failback, fencing, and data-loss behavior.

## Single writer and multiwriter

A single writable leader simplifies order and conflict but creates remote-write
latency and failover coordination. Multiwriter designs increase locality and write
availability but require conflict prevention or resolution. Last-write-wins can lose
valid business changes and depends on clock behavior. Partitioning ownership by region
or entity is often safer than arbitrary concurrent writes.

## Read replicas

Replicas offload tolerant reads and analytics but may lag during bursts, maintenance,
or network failure. Classify queries by staleness tolerance. Provide read-your-writes
through primary routing, session stickiness, version waiting, or a product-visible
pending state. Monitor lag in time and log position, plus replay/apply throughput.

## Failover is a distributed event

Election or promotion must prevent two writable leaders. Clients need bounded connect
and operation timeouts, DNS/endpoint refresh, transaction retry, connection-pool reset,
and idempotency for unknown outcomes. Test failover under write load and long
transactions; measure application recovery rather than only database promotion time.

## Global databases

Discover which invariants must span regions, where writes originate, legal placement,
latency, failure behavior, and conflict policy. Synchronous inter-region commit raises
latency and can reduce availability during partition. Asynchronous replication accepts
RPO and stale reads. A global endpoint does not remove propagation physics.

## Replication is not backup

Replication quickly copies legitimate writes, accidental deletion, corruption, and
ransomware. Backups and point-in-time recovery provide historical recovery boundaries;
isolated copies and tested restores protect against shared administrative compromise.
Both are required according to business impact.
