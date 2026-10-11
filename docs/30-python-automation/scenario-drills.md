# Advanced Automation Incident Drills

[← Module overview](index.md) · [Scenario questions](scenarios.md)

Use five minutes per drill. State impact, facts, containment, authoritative state,
safe recovery, evidence, communication, reconciliation, and prevention.

## 1. An account-selection regex expands unexpectedly

Stop dispatch, revoke the run session, preserve effective configuration and target
manifest, and enumerate completed/in-flight work. Restore affected resources, replace
regex-only selection with owned inventory and explicit scope, preview resolved targets,
cap changes, and test production naming edge cases.

## 2. Credential-chain fallback uses a developer identity

End the process, revoke sessions if exposed, and inspect actions under the unexpected
principal. Configure allowed credential type and account explicitly in production,
fail on interactive/developer fallback, verify caller identity at startup, and test
the runtime trust policy.

## 3. A retry storm amplifies a provider outage

Disable or drain new work, reduce concurrency, enforce global attempt and elapsed-time
budgets, and honor provider guidance. Preserve pending items durably, communicate
degraded objectives, then resume gradually with jitter and reconcile every ambiguous
operation instead of releasing a synchronized backlog.

## 4. Two runs change the same resource

Pause one run, inspect versions and authoritative state, and prevent further lost
updates. Use a lease, conditional write, resource version, or partitioned ownership;
make lock expiry and fencing explicit, then test crash, stale owner, and retry behavior.

## 5. A dependency package is compromised

Stop builds/deployments, identify artifacts and runs containing the version, revoke
credentials exposed during execution, and quarantine affected automation. Rebuild from
reviewed locked inputs on trusted infrastructure, verify provenance, and strengthen
index policy, hashes, scanning, and dependency update review.

## 6. A checkpoint file is corrupted

Preserve it, halt destructive resume, and derive actual state from provider evidence
and immutable plan rather than guessing. Validate schema/version/checksum, use atomic
writes and durable storage, retain prior checkpoint generations, and test interrupted
writes plus migration between tool versions.

## 7. Cancellation leaves temporary access enabled

Contain the temporary grant, identify every affected target, and reconcile cleanup
from durable state. Model temporary access as an expiring resource, use finally only
as a best-effort helper, add independent janitor/reconciliation, and test termination
during each lifecycle step.

## 8. A CSV inventory contains formula and encoding surprises

Treat the file as untrusted, stop before mutation, preserve safely, and validate
encoding, delimiter, schema, identifiers, duplicates, size, and control characters.
Neutralize spreadsheet formula injection in exports, use versioned ingestion, and
report rejected rows without leaking sensitive content.

## 9. A rollback script is older than the deployed schema

Do not run it blindly. Stabilize forward where safer, compare artifact/state schema,
and obtain the current owner’s recovery decision. Version and compatibility-test
rollback tools with releases, retain immutable artifacts, rehearse restoration, and
prefer expand/contract changes that allow mixed versions.

## 10. Metrics show success while reconciliation finds drift

Change the success definition from API acknowledgement to verified outcome. Preserve
the false-positive population, identify consistency delay or incomplete checks, repair
state, and add independent reconciliation, uncertainty status, evidence freshness,
and an SLO for durable correct outcomes.

## Self-review

- Did I stop blast-radius growth before debugging?
- Did I distinguish requested, acknowledged, verified, and reconciled state?
- Did I treat credentials, inventory, config, and checkpoints as trust boundaries?
- Did I preserve partial/unknown outcomes rather than report false success?
- Did I improve a reusable guardrail instead of only patching one script?
