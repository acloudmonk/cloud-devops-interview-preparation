# Database, Configuration, and Feature-Flag Change

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Application binaries are only one part of a release. Database schemas, messages,
APIs, configuration, secrets, and feature flags must remain compatible while old
and new versions overlap.

## Expand–migrate–contract

Use multiple releases for a destructive schema change:

1. **Expand:** add a compatible column, table, index, or API field. Old consumers
   continue to work.
2. **Migrate:** deploy code that understands both forms, backfill in bounded and
   observable batches, and verify completeness.
3. **Contract:** stop old writes/reads, prove no old consumers remain, then remove
   the obsolete structure in a later change.

Avoid coupling a long-running migration to the application startup path. Set lock,
statement, batch, and retry bounds; measure lag and database pressure; and make
steps restartable. Take backups where appropriate, but do not confuse backup with
instant rollback.

## Compatibility dimensions

- Old application with new schema
- New application with old/partially migrated data
- Old and new services exchanging API calls or events
- Delayed messages and replayed jobs
- Mobile, desktop, partner, or device clients that upgrade slowly

Prefer additive contracts, tolerant readers, explicit version policies, consumer
contract tests, and deprecation telemetry. Removing a field because repository
search finds no use does not prove external consumers have stopped using it.

## Configuration as a versioned input

Configuration should have ownership, schema validation, review, target scope,
change history, safe defaults, and rollback. Record the effective configuration
version with deployment evidence. Test combinations that can exist during rollout.

Separate secrets from ordinary configuration. A secret needs restricted access,
rotation, revocation, and audit; configuration needs correctness and controlled
promotion. Do not put either into an immutable application image merely to simplify
deployment.

On AWS, systems may use Systems Manager Parameter Store or AWS AppConfig for
configuration and Secrets Manager for secrets. The product choice matters less
than access boundaries, validation, encryption, audit, and failure behavior.

## Feature-flag lifecycle

Each flag needs:

- an owner and business/operational purpose;
- safe default and failure mode;
- target population and privacy review;
- creation and planned removal date;
- telemetry for both paths;
- authorization for emergency changes;
- tested behavior if the flag service is slow or unavailable.

Flags can act as release controls, experiments, operational kill switches, or
permissions. Do not mix these meanings casually. Protect server-side authorization
independently; a client-visible flag is not an access-control boundary.

## Coordinated release example

For a renamed customer-status field: add the new field, dual-write, backfill,
deploy readers preferring the new field with fallback, observe old-field reads,
move exposure with a flag, stop old writes, and remove the old field later. Every
stage has a verification query and a recovery action.

## Interview test

When asked “How will you roll back?”, state what happens to data written by the new
version. A credible answer names compatibility windows, irreversible boundaries,
backfill controls, flag/config state, and whether recovery is rollback, roll-forward,
or exposure removal.
