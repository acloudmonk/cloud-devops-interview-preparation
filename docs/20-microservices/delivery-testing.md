# Delivery and Testing

[← Security and identity](security-identity.md) · [Next: Observability and operations →](observability-operations.md)

## Independent deployment is earned

A service is independently deployable only when contracts are compatible, data
changes tolerate version overlap, delivery is automated, and teams can verify and
recover without coordinating the whole system. Separate repositories are neither
required nor sufficient.

## Test portfolio

Use fast unit/domain tests, component tests with real storage where valuable,
provider/consumer contract tests, integration tests for infrastructure semantics,
selected end-to-end journeys, and production canaries. Too many end-to-end tests
become slow and flaky; mocks alone miss network, serialization, identity, and data.

Test timeout-after-success, duplicate/out-of-order events, stale reads, unavailable
dependencies, schema overlap, token scope, retries, partial workflows, and recovery.
Maintain representative test data without copying sensitive production data.

## Release compatibility

Use expand/migrate/contract for databases and additive event/API evolution. Deploy
producers and consumers in either order when possible. Feature flags separate code
deployment from release but require ownership and retirement. Rollback must account
for data and emitted events, not only container image.

## Progressive delivery

Canary by representative tenant, region, journey, and dependency. Define technical
and business stop signals, automate rollback or roll-forward, and prevent one bad
service release from cascading through shared clients or schemas.

## Supply chain

Build once in isolated runners, create SBOM/provenance, sign immutable artifacts,
scan and verify at deployment, use workload identity, and record promotion evidence.
Generated clients and shared libraries require versioning and compatibility just
like network contracts.
