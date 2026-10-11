# AWS Architecture Decision Model

[← Module overview](index.md) · [Next: Global infrastructure and service scope →](global-infrastructure.md)

## Begin with the workload

Define users, business journeys, data, transaction boundaries, demand, latency,
availability, durability, RTO/RPO, security, compliance, residency, delivery speed,
skills, support, and cost. Separate required qualities from preferences. Then choose
AWS capabilities; do not reverse-engineer requirements from a favorite service.

## Select the responsibility boundary

Compare managed services, serverless, containers, and instances by control needed,
compatibility, scaling, patching, deployment, isolation, observability, recovery,
limits, portability, skills, and total cost. Managed services shift work to AWS but
never transfer responsibility for configuration, identity, data, architecture, or use.

## Model service semantics

For each service, know resource and API scope, consistency, durability, availability,
scaling unit, quotas, maintenance, deployment behavior, encryption, logging, backup,
failure modes, pricing dimensions, and upstream dependencies. “Fully managed” and
“serverless” are operating models, not infinite capacity or automatic resilience.

## Design boundaries deliberately

Use Organizations, accounts, Regions, VPCs, subnets, identities, keys, data stores,
queues, and service ownership as explicit blast-radius and administration boundaries.
Every central capability also creates a dependency; define its service level,
degraded behavior, recovery, and accountable owner.

## Validate with evidence

Use architecture decision records, threat models, quotas, pricing models, load and
failure tests, restore exercises, deployment evidence, SLOs, and cost allocation.
Record assumptions and triggers for reconsideration. Provider diagrams do not prove
that a particular workload meets its required qualities.

## AWS decision record

Capture outcome, workload boundary, Region/account placement, services, alternatives,
identity and data authority, network paths, availability, recovery, observability,
delivery, quotas, cost, shared responsibility, risks, evidence, owner, and exit trigger.
