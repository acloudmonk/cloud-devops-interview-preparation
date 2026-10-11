# Testing and Verification

[← Concurrency](concurrency-performance.md) · [Next: Packaging →](packaging-delivery.md)

Tests must prove decisions and safety, not merely line coverage.

## Test layers

1. **Unit:** pure selection, validation, planning, retry classification, and formatting.
2. **Contract:** recorded or provider-defined request/response schemas and error mapping.
3. **Adapter:** SDK wrappers with fakes/stubs that model pagination and partial failure.
4. **Integration:** isolated account/project/subscription with real identity and APIs.
5. **Failure:** throttling, timeout-after-success, stale state, denial, cancellation, resume.
6. **Safety:** production-shaped inventory with nonproduction targets, canary, and rollback.

Mock your adapter, not every SDK internal. Over-mocking can prove code agrees with an
invented cloud. Test permissions with the runtime identity and include denied actions.

## Determinism

Inject time, randomness, clients, and configuration. Seed generated data, freeze time
where relevant, isolate files/network, and remove order dependence. Property-based
tests suit parsers, identifiers, filters, and invariants; fuzz untrusted formats.

## Destructive-path proof

Test empty selection, unexpectedly broad selection, protected resource, wrong account,
changed state between plan/apply, partial batch, confirmation absent, and maximum-
change stop. Verify dry-run and apply share selection and plan logic.

## Release evidence

Use formatting/linting, type checking, tests, dependency and secret scanning,
artifact provenance, review, and environment promotion. Coverage is a navigation
signal; mutation, branch, and scenario evidence better reveal weak decisions.

## Production verification

Canary on a bounded target, validate business/technical outcome, observe errors and
cost, then expand. Reconcile independently rather than trusting the automation report.
