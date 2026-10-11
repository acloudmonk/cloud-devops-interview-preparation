# Packaging and Delivery

[← Testing](testing-verification.md) · [Next: Security and operations →](security-operations.md)

Ship automation as a reproducible artifact with an owner and supported runtime.

## Project and dependency contract

Use `pyproject.toml`, a `src` layout where appropriate, explicit runtime support,
entry points, semantic versioning, and generated lock/constraint strategy suited to
deployment. Pin reproducible applications; use compatible bounds for reusable
libraries and continuously test the resolution. Separate runtime and development tools.

Virtual environments isolate dependencies, not operating-system libraries or supply-
chain risk. Build in a controlled environment, capture hashes/provenance/SBOM where
risk warrants, scan dependencies, and promote the same artifact across environments.

## Deployment choices

| Form | Fit | Operational concern |
| --- | --- | --- |
| wheel/CLI | operator or pipeline tool | Python/runtime compatibility |
| container | controlled dependencies and scheduled jobs | image lifecycle, identity, patching |
| Lambda/function | event-driven bounded work | timeout, cold start, retries, package limits |
| workflow workers | durable multi-step operation | state, duplicate work, version migration |
| service | shared continuous capability | SLO, scaling, API lifecycle, on-call |

## Release safety

Version code, plan/schema, configuration, and checkpoint formats. Use signed reviewed
commits, CI identity, immutable artifacts, environment approvals, canaries, and rapid
rollback. Database/state migrations need forward/backward compatibility.

## Lifecycle

Publish usage and support policy, ownership, changelog, migration, telemetry, and
deprecation. Remove credentials, schedules, queues, roles, dashboards, and stale
artifacts when retiring automation; abandoned jobs are security and cost risks.
