# Data Movement, Cutover, and Rollback

[← Waves and migration factory](waves-factory.md) · [Next: Validation and operations →](validation-operations.md)

## Choose the transition pattern from constraints

Options include offline copy, backup/restore, bulk load plus change data capture,
continuous replication, application dual write, event replay, phased cohorts, or
parallel operation. Decide from volume, change rate, downtime, consistency, schema
change, network, validation, encryption, source impact, and rollback requirements.
Dual write is a distributed-consistency design, not a convenient checkbox.

## Define authority during coexistence

At every phase name the authoritative write path, permitted readers, synchronization
direction, lag tolerance, conflict policy, delete handling, and reconciliation owner.
Use fencing or write quiescence so two systems cannot both become authoritative by
accident. Preserve audit and correlation identifiers across the transition.

## Engineer a cutover

A cutover plan includes prerequisites, roles, communications, command channel,
timestamps, backups, data sync, freeze/fencing, routing/DNS, caches, jobs, validation,
monitoring, go/no-go authority, abort thresholds, rollback/fallback, supplier contacts,
business acceptance, and post-cutover reconciliation. Rehearse with production-like
volume and record actual durations.

## Rollback is time-bound

Define the last safe rollback point, maximum decision time, reverse synchronization,
data created after cutover, destructive changes, and who may invoke rollback. When
reverse migration is unsafe, define a forward-fix or service fallback and say so.
“Restore the backup” is incomplete without restore time and lost-write treatment.

## Validate integrity

Reconcile counts, aggregates, keys, checksums/samples, referential and business
invariants, deletes, permissions, history, and downstream outputs. Explain tolerances
and exceptions. Continue reconciliation after cutover because delayed jobs and rarely
used paths may reveal silent divergence.
