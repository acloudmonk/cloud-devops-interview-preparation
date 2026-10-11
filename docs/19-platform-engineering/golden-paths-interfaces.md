# Golden Paths and Interfaces

[← Platform architecture](platform-architecture.md) · [Next: Self-service and control planes →](self-service-control-planes.md)

## A path is a product contract

A golden path combines documentation, templates, APIs, policy, delivery, runtime,
observability, ownership, and support for a common workload class. It should make
the safe path easier while exposing essential decisions such as data classification,
availability, ownership, cost, and recovery.

## Start right and stay right

Scaffolding creates an initial state; it does not keep hundreds of repositories
current. Prefer centrally versioned workflow components, reusable modules, policy,
dependency automation, and reconciliation. Track template provenance and version,
support upgrades, and avoid uncontrolled copy-and-own assets.

## Interface choices

| Interface | Strength | Risk |
| --- | --- | --- |
| Portal | Discovery, status, cohesive journeys | UI can hide weak APIs or become bottleneck |
| CLI | Scriptable, fast expert workflow | Distribution and compatibility burden |
| API | Composable automation contract | Requires strong lifecycle and authorization |
| Git declaration | Reviewable desired state and audit | Slow feedback or reconciliation ambiguity |
| IDE integration | In-context feedback | Fragmented clients and upgrade support |

Use more than one interface over the same domain contracts. Return operation IDs,
status, errors, ownership, and remediation. A self-service failure that opens an
opaque ticket is not a complete interface.

## Opinion and escape

Offer a small number of workload archetypes based on evidence. Define extension
points and escape hatches with owners, risks, and re-entry paths. Unbounded choice
recreates cognitive load; forced uniformity causes shadow platforms and blocks
legitimate workloads.

## Documentation

Document tasks, decisions, guarantees, limits, cost, examples, failure recovery,
support, versions, and ownership. Test documentation and templates as part of the
release. Search and service catalogs improve discovery only when metadata is owned
and freshness is measured.
