# Capability-First Decision Model

[← Module overview](index.md) · [Next: Governance →](governance.md)

## The comparison unit

Compare a required capability—not a product name—across:

1. resource and failure scope;
2. control-plane and data-plane semantics;
3. identity and network integration;
4. consistency, delivery, and recovery guarantees;
5. quotas, scaling, regional availability, and dependencies;
6. operating model, skills, evidence, cost, and exit conditions.

An apparent equivalent may require several services, expose different defaults, or
have no safe substitute. Record **equivalent**, **similar with gaps**, **composition
required**, or **no acceptable match**.

## Placement decision

Clarify the business driver, workload qualities, data gravity, regulation, existing
skills, contracts, dependency graph, and migration horizon. Compare:

- one strategic cloud with SaaS exceptions;
- different workloads assigned to different clouds;
- a portable workload platform with native supporting services;
- deliberately distributed application components;
- redundant deployments for recovery.

Choose the simplest model that meets the requirement. Provider optionality has value,
but unused portability and duplicated operations have costs.

## Interview loop

Use **clarify → map capability → expose semantic gap → decide placement → fail →
operate → verify**. Name the evidence and trigger that could change the choice.
