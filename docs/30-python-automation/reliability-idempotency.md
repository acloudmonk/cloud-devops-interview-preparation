# Reliability and Idempotency

[← SDK engineering](sdk-api-engineering.md) · [Next: Concurrency →](concurrency-performance.md)

Reliable automation makes repeated, interrupted, and partially successful execution
predictable.

## Idempotency patterns

- Read current state and calculate the minimum delta.
- Use provider conditional writes, versions, or idempotency tokens when available.
- Bind a run/item key to operation, target, and input fingerprint.
- Persist outcome atomically before acknowledging completion.
- Treat “already desired” as unchanged, not error or duplicate success.

Idempotency expires and has scope. Document retention, conflicts, concurrent runs,
external side effects, and what cannot be reversed.

## Failure model

Classify validation/permanent, authentication, authorization, conflict, quota,
throttling, timeout/uncertain, dependency, and code defects. Retry known transient
failures only. Use queues or durable workflow engines when work must survive process
loss, wait hours, coordinate compensation, or guarantee human approval.

## Checkpoint and resume

Store stable item identity, input/plan version, attempt, last known state, outcome,
and verification evidence. A resume revalidates target and authority; it does not
blindly continue stale actions. Separate failed items for bounded retry and preserve
a manifest for reconciliation.

## Rollback and compensation

Rollback is valid only when prior state is known and restoration is safe. Destructive
or external effects often need compensation, quarantine, restore, or human decision.
Prefer progressive rollout and small batches that limit rollback demand.

## Completion

Success means intended state is verified, not merely that API calls returned 2xx.
Report changed, unchanged, skipped, failed, uncertain, and reconciled outcomes.
