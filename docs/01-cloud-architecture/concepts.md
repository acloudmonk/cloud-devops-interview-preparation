# Core Concepts

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-09-02**

## Scalability and elasticity

**Scalability** is the ability to meet increasing demand by adding resources or
changing the design. **Elasticity** is the ability to add and remove capacity in
response to demand, ideally quickly and automatically.

### Vertical versus horizontal scaling

| Dimension | Vertical scaling | Horizontal scaling |
| --- | --- | --- |
| Mechanism | Increase CPU, memory, or I/O of one node | Add more nodes or partitions |
| Application impact | Often small initially | Requires distribution and coordination |
| Limit | Maximum machine size | Partitioning, consistency, and operational complexity |
| Failure domain | Larger single-node impact | Failure can be isolated across nodes |
| Typical use | Databases, legacy systems, rapid relief | Stateless services, workers, distributed data |

Vertical scaling is not inherently wrong. It is often the simplest economical
choice until recovery objectives, growth, or hardware limits require a more
distributed design.

### Capacity is multidimensional

Do not model capacity as CPU alone. Evaluate:

- requests, transactions, or messages per second;
- concurrent connections and session duration;
- CPU, memory, network bandwidth, and disk throughput/IOPS;
- hot keys, partitions, tenants, and regions;
- downstream quotas and third-party rate limits;
- cold-start and scale-out time.

## Availability, reliability, and resilience

These terms overlap but answer different questions.

| Quality | Practical question |
| --- | --- |
| Availability | Can users access the service now? |
| Reliability | Does the service consistently perform its intended function? |
| Resilience | Can it absorb, adapt to, and recover from disruption? |
| Fault tolerance | Can it continue despite a defined component failure? |
| Durability | Will accepted data survive over the required period? |
| Recoverability | Can service and data be restored within RTO and RPO? |

Availability must be defined for a user journey, not merely for individual
components. A healthy API with an unavailable identity provider may still make
the customer journey unavailable.

### Availability math and dependencies

For independent serial dependencies, approximate availability is the product of
each dependency's availability. Adding synchronous dependencies can therefore
reduce end-to-end availability even when every component appears highly
available.

Parallel redundancy can improve availability only when:

- failures are sufficiently independent;
- failover is detected and executed correctly;
- capacity remains after failure;
- state is available and consistent enough;
- the failover path is regularly tested.

## Latency, throughput, and utilization

- **Latency** is time taken for an operation. Use percentiles such as p50, p95,
  and p99; averages hide tail behavior.
- **Throughput** is useful work completed per unit time.
- **Utilization** measures consumed capacity, but high utilization can produce
  nonlinear queueing delay before nominal capacity is exhausted.

Define latency from the user's perspective and allocate a time budget across
network hops, services, data stores, and third parties.

## Stateful and stateless boundaries

A stateless compute instance does not retain unique session or workflow state
required by the next request. Stateless compute is easier to replace and scale,
but the system still has state somewhere: databases, object stores, queues,
caches, or client tokens.

Questions to ask:

- What is the system of record?
- Which data may be cached, reconstructed, or lost?
- Who owns state transitions?
- How are concurrent updates controlled?
- What happens during partial completion?
- How is state replicated, backed up, restored, and deleted?

## Consistency models

**Strong consistency** presents operations as if there were a single current
order. **Eventual consistency** allows replicas to temporarily diverge provided
they converge when updates stop. Real systems expose more nuanced guarantees,
including read-your-writes, monotonic reads, causal consistency, and bounded
staleness.

Choose consistency per business invariant. Account balances, uniqueness, and
inventory reservation may require stronger coordination than search indexes,
analytics, recommendations, or presence indicators.

## CAP and PACELC

CAP addresses behavior during a network partition: a distributed system cannot
guarantee both availability for every request and linearizable consistency
while the partition persists. It does not mean a database is permanently “CP”
or “AP” for every operation.

PACELC adds the normal operating trade-off: **if a partition occurs**, choose
availability or consistency; **else**, systems often trade latency against
consistency.

For interviews, explain:

- the unit of consistency: record, partition, transaction, or global state;
- which operation and failure mode are being discussed;
- whether stale reads, rejected writes, or conflicts are acceptable;
- how clients learn about uncertainty;
- how recovery and reconciliation work.

## Idempotency

An idempotent operation can be applied repeatedly with the same intended effect
as applying it once. This is essential when clients retry after an ambiguous
timeout.

Typical implementation:

1. Client creates a unique idempotency key for the business operation.
2. Service atomically records the key and result or state transition.
3. Duplicate requests return or resume the existing result.
4. Keys have a retention policy aligned with retry and business windows.

Do not confuse HTTP method semantics with complete business idempotency. A
nominally idempotent endpoint can still trigger duplicate downstream side
effects.

## Overload and backpressure

Backpressure signals producers to slow down when consumers or dependencies
cannot keep up. A complete overload strategy combines:

- bounded queues;
- concurrency limits;
- per-tenant and global rate limits;
- deadlines and timeouts;
- load shedding for lower-priority work;
- retry budgets;
- autoscaling based on meaningful demand indicators;
- graceful degradation.

Unbounded queues hide overload temporarily, increase latency and memory use,
and can turn a short spike into a long recovery incident.

## Coupling

Coupling is not only code dependency. Systems can be coupled by:

- synchronous availability;
- shared schemas or databases;
- coordinated deployments;
- shared capacity and noisy neighbors;
- common identity, DNS, or network dependencies;
- operational ownership;
- correlated regional or vendor failures.

Architecture should make necessary coupling explicit and remove accidental
coupling where its cost exceeds its value.
