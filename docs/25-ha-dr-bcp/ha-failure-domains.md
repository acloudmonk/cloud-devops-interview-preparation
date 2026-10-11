# HA and Failure-Domain Architecture

[← Module overview](index.md) · [Recovery objectives](objectives-bia.md)

High availability uses redundancy, isolation, detection, and automated or rapid
recovery to maintain an acceptable service during expected failures. Adding
copies without eliminating shared dependencies creates apparent, not real, HA.

## Failure-domain method

For each critical request path, enumerate failure domains: process, host, rack,
power/network segment, Availability Zone, Region, account/project/subscription,
identity plane, DNS, certificate/key service, deployment system, and third party.
Then determine blast radius, detection, behavior, recovery, and test evidence.

## AWS-first regional pattern

- Distribute stateless workloads across at least two Availability Zones.
- Use health-aware load balancing and readiness that tests ability to serve safely.
- Choose Multi-AZ data services appropriate to the actual engine and failure mode.
- Keep capacity or scaling headroom for losing a zone; check quotas and IP space.
- Remove single-zone NAT, storage, secrets, and administration dependencies.
- Use queues, timeouts, bounded retries, circuit breakers, idempotency, and load shedding.
- Separate workload accounts and deployment controls where correlated errors dominate.

## Availability reasoning

Serial dependencies reduce end-to-end availability. Redundant components improve
availability only when failures are sufficiently independent and traffic can use
the healthy path. Shared IAM, DNS, code, configuration, database, or deployment
systems often create common-mode failure.

Active-active improves resource availability but adds state coordination,
conflict, routing, and operational complexity. Active-passive is easier to reason
about but depends on detection, promotion, capacity, and a practised failover path.

## Degraded modes

Define safe reduced service before incidents: cached reads, queued writes,
read-only mode, lower-priority feature removal, alternate payment or contact
channels, and controlled admission. State what data may become stale and prevent
degradation from violating security, money movement, or consistency obligations.

## Common traps

- health checks that validate a process but not critical dependencies;
- autoscaling that cannot overcome quota, database, or downstream limits;
- synchronous coupling across failure domains that turns isolation into latency;
- retries without budgets, jitter, idempotency, or overload protection;
- scheduled maintenance and deployments that consume redundancy;
- claiming Region recovery when identity, artifacts, keys, or IaC exist only in primary.

Return to the [module overview](index.md) when ready to continue.
