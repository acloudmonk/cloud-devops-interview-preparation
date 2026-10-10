# Pipeline Architecture

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

## Architectural components

| Component | Responsibility | Failure questions |
| --- | --- | --- |
| Event source | Emits push, PR, tag, schedule, or manual event | Duplicate, missing, stale, or forged event? |
| Orchestrator | Builds workflow graph and state transitions | Can it resume, cancel, deduplicate, and audit? |
| Worker/runner | Executes code in an environment | Isolation, image, network, capacity, cleanup? |
| Artifact/evidence store | Retains immutable outputs and attestations | Identity, retention, access, replication? |
| Policy service | Evaluates required evidence and authorization | Versioned policy, trusted inputs, exceptions? |
| Deployment controller | Applies desired artifact/configuration | Idempotency, concurrency, drift, rollback? |
| Target/observability | Serves workload and reports outcome | Is verification representative and timely? |

## Event and concurrency design

Events can be duplicated, delayed, reordered, or superseded. Use stable run and
artifact identities, idempotent transitions, cancellation of obsolete runs, and
concurrency controls by branch/environment/resource. Never let an older run
overwrite a newer successfully deployed version.

## Pipeline as code

Versioned workflow definitions improve review and repeatability but execute from
different trust contexts. Decide whether PR checks use workflow code from the
untrusted branch or trusted base, and never expose privileged secrets merely
because a workflow file asks for them.

Reusable workflows/templates reduce duplication. Pin versions, define inputs
and outputs, publish compatibility policy, test changes, and avoid a central
template update breaking every repository simultaneously.

## Jobs, stages, and dependencies

Model a directed acyclic graph based on real data/evidence dependencies. Use
parallelism for independent checks and explicit artifacts for handoff. Avoid
hidden state on a persistent worker and order-only stages that add wait without
assurance.

## Worker models

| Model | Strength | Risk/cost |
| --- | --- | --- |
| Hosted ephemeral | Low operations burden and clean isolation | Capability, network, locality, and usage constraints |
| Self-hosted ephemeral | Custom network/tooling with per-job cleanup | Image, autoscaling, identity, patching, and cost ownership |
| Persistent self-hosted | Fast warm state and specialist hardware | Cross-job contamination, credential persistence, drift |

Do not place untrusted fork code on a privileged internal runner. Segment worker
pools by trust, data, network, platform, and workload class.

## GitHub Actions anchor

Workflows trigger jobs on runners; environments can add approval and secret
boundaries; reusable workflows centralize contracts; artifacts/caches retain
different classes of data; OIDC can exchange a signed job identity for
short-lived cloud credentials. Repository permissions and event types materially
change trust—especially `pull_request` versus privileged base-context execution.

## Tool translation

Jenkins controllers/agents/plugins, GitLab pipelines/runners/environments, and
Azure Pipelines/stages/agents/environments express similar concerns with
different identity, isolation, template, approval, and inheritance semantics.
Compare trust and lifecycle, not YAML keywords.

## Platform reliability

Set SLOs for trigger latency, queue time, worker availability, artifact access,
run completion, and deployment control. Provide degradation modes: cached
dependencies, alternate worker pools, safe manual promotion, and recovery from
provider outage without creating an uncontrolled second source of truth.
