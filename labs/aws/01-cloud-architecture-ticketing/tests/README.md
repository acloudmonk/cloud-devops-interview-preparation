# Required Tests

## Correctness

- two callers compete for one seat and exactly one reservation succeeds;
- replaying one idempotency key returns the stored result;
- reusing a key with a different request fingerprint is rejected;
- duplicate queue delivery has no duplicate business effect;
- expired holds can be reclaimed safely;
- ambiguous payment results reconcile before another charge.

## Resilience

- one API task terminates without breaching the defined objective;
- stopped workers produce a visible backlog and recover within target;
- a poison message reaches the DLQ after the configured attempt count;
- bounded dependency latency does not create an unbounded retry storm;
- rollback restores the previous version and compatible data behavior.

## Recovery

- infrastructure can be recreated from source;
- protected data can be restored within measured RTO/RPO;
- outstanding messages and payment outcomes are reconciled;
- teardown leaves no tagged billable workload resource.
