# State, Backends, Locking, and Recovery

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

State maps configuration addresses to remote object identities and records metadata
needed for planning. Losing or corrupting it does not necessarily delete infrastructure,
but it removes the engine's reliable knowledge of ownership.

## State security model

State can contain resource identifiers, topology, attributes, outputs, and secret values.
Marking a value sensitive reduces display; it does not remove the value from state.
Protect state with encryption, least privilege, private transport, audit, versioning,
backup, and tightly controlled administrative recovery.

## Backend decision

| Concern | Required decision |
| --- | --- |
| Durability | versioned, replicated storage and tested restore |
| Concurrency | supported locking or an execution system that serializes writes |
| Confidentiality | encryption, access boundary, logging redaction, retention |
| Availability | behavior when storage or lock service is unavailable |
| Identity | separate read/plan, apply, and backend administration authority |
| Recovery | ownership, runbook, backup age, validation, and escalation |
| Migration | controlled initialization, source backup, destination verification |

For AWS, common choices are HCP Terraform/Enterprise or an S3-based backend with the
currently supported locking mechanism, versioning, encryption, and restricted IAM.
Do not copy an old locking pattern without checking current backend documentation.

## Choose state boundaries by failure domain

Do not place an entire enterprise in one state. Split when components have materially
different owners, credentials, change cadence, availability requirements, or blast
radius. Do not split every resource either: excessive state-to-state outputs create a
distributed dependency graph that is difficult to change safely.

Prefer explicit platform contracts—published parameters, DNS, service discovery, or a
small output interface—over broad remote-state access. Reading another state often grants
access to all its sensitive contents, not only the selected output.

## Lock handling

A lock protects concurrent mutation; it does not prove that no external system is
changing the infrastructure. On a stuck lock:

1. identify the run and operator that owns it;
2. confirm whether an apply process is still active;
3. inspect runner and backend logs;
4. stop or recover the original execution safely;
5. force-unlock only with the exact lock identifier and recorded approval;
6. refresh and produce a new plan before any apply.

Never automate blind force-unlock retries.

## Recovery cases

### State unavailable

Freeze applies, preserve configuration and logs, restore a known state version, compare
lineage/serial and cloud inventory, refresh, and require a reviewed recovery plan.

### Resource exists but is absent from state

Confirm intended ownership, add an import declaration or controlled import, generate a
plan, and make configuration match the real object without accidental mutation.

### Wrong resource bound to an address

Stop applies. Back up state, prove both identities, use supported state move/remove and
import operations, then plan against restricted credentials. Do not edit JSON directly.

### Partial apply

Assume some API actions succeeded. Preserve logs and state, inspect cloud events, refresh,
and choose roll-forward or explicit recovery based on customer impact. Re-running apply
without diagnosis may compound side effects.

## Recovery evidence

Test restore into an isolated control path, validate state metadata, perform a read-only
plan, reconcile inventory, and record recovery time. “Bucket versioning enabled” is a
control; a successful rehearsal is evidence.
