# Testing and Quality Gates

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

## Evidence portfolio

No single test type proves release safety.

| Evidence | Best purpose | Common limitation |
| --- | --- | --- |
| Static/format/type checks | Very fast structural feedback | Cannot prove runtime behavior |
| Unit tests | Local logic and edge cases | Mocks can hide integration contracts |
| Component/integration tests | Real boundaries and dependencies | Environment/data cost and flakiness |
| Contract tests | Producer/consumer compatibility | Requires versioned contracts and participant discipline |
| Security/license/policy checks | Known risks and organizational constraints | False positives, freshness, coverage gaps |
| End-to-end tests | Critical user journeys | Slow, brittle, and weak at fault localization |
| Production verification | Real environment, traffic, and dependencies | Must limit exposure and detect harm quickly |

Use a test pyramid or portfolio based on feedback value, not fixed percentages.
Move correctness to the cheapest reliable layer that can prove it.

## Gate design

A blocking gate needs a named risk, trusted evidence source, threshold, owner,
failure procedure, exception authority, and review cadence. Advisory evidence
can become blocking only after quality and response ownership are established.

Do not allow a PR to weaken the test or policy that approves that same PR
without independent ownership.

## Flaky tests

Retries can distinguish intermittent infrastructure from deterministic failure,
but silently retrying to green hides risk. Record each attempt, quarantine only
with owner/expiry/risk acceptance, and prioritize fixes using frequency, impact,
and affected path. A quarantined critical test is missing assurance.

## Test data and environments

Use synthetic or properly governed masked data; prevent production secrets and
personal data entering logs/artifacts. Make fixtures versioned and deterministic.
Prefer disposable environments where feasible, but account for provisioning
time, quotas, cleanup, and differences from production.

## Change-aware selection

Path and dependency-graph selection can reduce time, but a wrong graph silently
skips required tests. Validate selection logic, run periodic broader suites,
include shared/build/configuration changes, and measure escaped defects.

## Performance and reliability tests

Define representative workload, warmup, baseline, environment variance,
statistical threshold, and ownership. A single noisy benchmark should not block
randomly; trend meaningful regressions and confirm against controlled baselines.

## Quality metrics

Track detection lead time, false-positive/flaky rate, queue time, skipped or
quarantined assurance, escaped defects, change failure, and time to restore.
Coverage percentage is a signal, not a business-risk guarantee.
