# Pipeline Operations and Troubleshooting

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Operate CI/CD as a service with users, capacity, dependencies, security boundaries,
objectives, and incident procedures. A fast pipeline that sometimes publishes the
wrong artifact is worse than a slower trustworthy one.

## Useful service indicators

- queue time, execution time, and end-to-end lead time;
- success rate by stage and failure category;
- flaky-test rate and rerun dependence;
- deployment frequency and change failure rate;
- time to detect, restore, and complete rollback/roll-forward;
- runner utilization, saturation, and startup latency;
- cache hit rate with correctness guardrails;
- approval wait and blocked-deployment age;
- artifact, log, and runner cost per team or service.

Segment by repository, workflow, runner pool, branch/event, target environment, and
failure class. A global average can hide one team waiting hours in a saturated pool.

## Failure classification

| Class | Examples | First question |
| --- | --- | --- |
| Product change | Compile, test, policy, or compatibility failure | Is the change or its assumptions wrong? |
| Pipeline definition | Syntax, permissions, wrong path/filter | Did executable delivery logic change? |
| Execution platform | Runner loss, capacity, filesystem, network | Is this shared or isolated to one worker/pool? |
| External dependency | Registry, package source, cloud API, identity provider | What is the dependency objective and safe degraded mode? |
| Target environment | Capacity, policy, drift, health-check failure | Did the intended artifact reach the intended target? |
| Observation | Missing, delayed, or misleading telemetry | Can promotion be trusted without this signal? |

## Incident workflow

1. Protect customers: stop promotion or exposure and prevent stale runs from
   overtaking newer ones.
2. Preserve run IDs, commit SHA, artifact digest, workflow version, runner identity,
   logs, approvals, target state, and relevant cloud audit events.
3. Establish scope across repositories, runner pools, regions, and environments.
4. Classify the failure and test the smallest safe hypothesis.
5. Recover with a bounded retry, clean rebuild, rollback, roll-forward, or manual
   continuity path.
6. Verify customer and system outcomes, then reconcile temporary actions.

## Retry safely

A retry is safe only when the operation is idempotent or protected by an idempotency
key/state check. Publishing, database migration, traffic shift, and infrastructure
mutation can partially succeed. Re-read actual state before repeating them.

Bound exponential backoff and jitter, distinguish transient from deterministic
errors, and stop retry storms during dependency failure. Never make “rerun until
green” the response to a flaky gate; quarantine only with ownership, expiry, and
visible risk.

## Concurrency and ordering

Use concurrency groups or deployment locks so obsolete runs cannot deploy after a
newer change. Cancellation must not leave partial external state. Serialize only
the critical target mutation; excessive global locking creates long queues and
encourages bypass.

## Capacity, resilience, and cost

Autoscale ephemeral runners against queue objectives, keep trusted/untrusted pools
separate, and reserve capacity for emergency fixes. Cache expensive dependencies
without sharing unsafe writable state. Define behavior for source host, registry,
cloud API, and identity outages. Regularly test whether a critical fix can still be
built, verified, approved, and deployed.

Optimize the constraint seen by developers and customers—not merely billable
minutes. First remove duplicated work, oversized checkouts/artifacts, needless
matrix jobs, and serial dependencies; then tune compute and caching.

## Tool selection

Compare governance, identity federation, runner isolation, artifact/provenance
support, environment controls, observability, extensibility, portability, operating
burden, and total cost. GitHub Actions, GitLab CI/CD, Jenkins, Azure Pipelines, and
cloud-native services can all be appropriate. The design should survive a tool
translation because its trust boundaries and delivery invariants are explicit.
