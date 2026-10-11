# Operations, Governance, and Resilience

[← Security](security-threats.md) · [Next: Design exercise →](design-exercise.md)

API and identity platforms are products with consumers, SLOs, roadmaps, support,
and retirement—not one-time integrations.

## Operating model

- Capability owner owns semantics and consumer outcome.
- API platform owns gateway, catalog, paved road, traffic policy, and evidence.
- Identity team owns issuer, federation, directories, credentials, and recovery.
- Product/service owner owns resource-level authorization and data invariants.
- Security defines control objectives; risk owners accept time-bound residual risk.

## Reliability and degraded modes

Set separate service level objectives for token issue, federation, key discovery,
authorization decision, gateway, and critical APIs. Model dependency budgets end to
end. Cache public keys with controlled refresh and overlap; cache authorization only
when staleness is safe. Decide whether sessions continue during identity-provider
outage, which actions require step-up, and how revocation delay affects risk.

## Lifecycle governance

Maintain API/owner/consumer inventory, data classification, identity population,
client and redirect registry, scopes/roles, policy version, credentials, dependencies,
support tier, cost, and retirement state. Deprecation needs telemetry, consumer
contact, migration help, deadline, exception, and verified traffic removal.

## Observability and incident command

Measure user journey, authentication and token failures, authorization denies,
gateway saturation, quota rejection, dependency latency, webhook backlog,
contract/version use, and policy change impact. One incident command coordinates
API, identity, security, product, and provider teams while preserving evidence.

## Cost and simplification

Track requests, payload/egress, gateway and policy calls, logs, active users,
support, duplicated products, and engineering operations. Prefer a small number of
well-owned trust patterns; exceptions state driver, owner, expiry, and exit plan.
