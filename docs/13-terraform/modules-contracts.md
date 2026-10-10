# Module Contracts and Composition

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

A module packages an infrastructure capability behind a versioned interface. Its value
comes from safe defaults, invariants, documentation, tests, ownership, and evolution—not
from reducing line count.

## Root versus reusable module

- A **root module** owns a deployment boundary, backend, provider configuration,
  environment inputs, and execution workflow.
- A **reusable module** exposes a capability through variables and outputs and must not
  assume the caller's backend or credentials.

Keep provider configurations in roots. Reusable modules declare provider requirements
and accept aliased providers explicitly when necessary.

## Design a useful contract

1. Define the user outcome and supported variants.
2. Choose a small, typed input surface with safe defaults and validation.
3. Encode security, resilience, tagging, logging, and deletion invariants.
4. Return stable outcomes, not every internal attribute.
5. Document prerequisites, replacement behavior, cost, examples, and limitations.
6. Test behavior, upgrades, failure paths, and expected policy results.
7. Publish immutable versions with compatibility and deprecation guidance.

## Abstraction test

| Too thin | Useful | Too broad |
| --- | --- | --- |
| renames provider arguments | encodes an owned platform capability | creates a whole enterprise environment |
| exposes every raw field | offers intentional extension points | combines unrelated lifecycles and owners |
| adds no policy or defaults | makes the safe path easy | changes slowly because every team depends on it |

Avoid universal modules with dozens of booleans. When variants have different lifecycle
or security semantics, use separate modules or higher-level composition.

## Composition and dependency

Prefer shallow composition from a root module. Pass the minimum explicit output needed
by another module. Cyclic dependencies usually reveal misplaced ownership. If two stacks
change together atomically, consider the same state; if they have different owners and
cadence, publish a stable external contract.

## Versioning and upgrades

- Pin reusable module versions and provider constraints deliberately.
- Treat default changes, address changes, and output removal as compatibility events.
- Use moved declarations for address refactors when supported.
- Publish an upgrade guide for replacements, imports, state moves, and removed features.
- Test from supported previous versions, not only clean creation.
- Deprecate with a deadline, inventory consumers, and measure adoption.

Semantic versioning communicates intent but does not prove a non-destructive plan.
Consumers must review the plan in their own state and cloud context.

## AWS platform-module example

An AWS VPC module might own subnets, routing, flow logs, endpoints, and baseline controls.
It should not automatically own every workload security group, DNS zone, or application
load balancer. Expose subnet identifiers and supported attachment points; keep workload
lifecycle with workload owners.

Translate the capability—not resource names—to Azure virtual networks and GCP VPCs.
Provider differences in hierarchy, routing, identity, and service networking mean a
single “multi-cloud network module” often becomes a lowest-common-denominator trap.

## Module governance measures

Track adoption by version, upgrade lead time, destructive-plan rate, policy exceptions,
support demand, change failure, consumer satisfaction, and time to provision. A heavily
reused module with slow unsafe upgrades is not automatically successful.
