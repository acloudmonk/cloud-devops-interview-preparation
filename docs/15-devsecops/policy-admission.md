# Policy, Admission, and Release Decisions

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Policy converts evidence and context into a decision. Effective policy is
specific, testable, observable, owned, recoverable, and usable by delivery teams.

## Decision inputs

Consider artifact digest, source and builder identity, provenance, signature,
SBOM, test/scan evidence, severity, exploitability, reachability, environment,
asset criticality, exposure, exception, and evidence freshness. Bind every result
to the exact artifact; do not approve a tag or branch name as if it were immutable.

## Enforcement points

| Point | Strength | Failure concern |
| --- | --- | --- |
| IDE/pre-commit | Fast feedback | Bypassable and inconsistent |
| Pull request | Review context | Fork and token trust |
| Protected build | Strong artifact binding | Builder compromise |
| Registry | Distribution control | Replication and availability |
| Deployment pipeline | Environment context | Credential/pipeline compromise |
| Admission | Last preventive boundary | Control-plane availability and bypass |
| Runtime | Actual behavior | Detection after exposure |

Use multiple independent points for high-risk threats, without duplicating noisy
scans that produce no different decision.

## Progressive rollout

Observe current violations, publish ownership, run advisory mode, provide fixes,
enforce on new/changed workloads, then address legacy risk in waves. Define a
deadline and measure exceptions so "temporary warn" does not become permanent.

## Availability and recovery

Decide timeout, cache, degraded mode, fail-open/closed behavior, and emergency
bypass per environment and threat. Protect policy bundles, admission identities,
trust roots, and exception APIs. Rehearse controller outage and disaster recovery.

## Policy quality

Measure prevented high-risk releases, false-positive rate, decision latency,
bypass/exception volume and age, fix time, and incidents. A gate with many alerts
but routine overrides is neither secure nor trusted.

Return to the [module overview](index.md) when ready to continue.
