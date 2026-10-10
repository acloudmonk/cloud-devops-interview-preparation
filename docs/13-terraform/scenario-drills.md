# Advanced IaC Incident Drills

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

For each drill, state assumptions, immediate containment, evidence, competing hypotheses,
recovery decision, prevention, and stakeholder communication.

## 1. State version restored from the wrong environment

Production planning suddenly proposes creation and deletion across unrelated resources.
Explain how you freeze execution, preserve both state histories, compare lineage/serial
and cloud identities, restore the correct binding safely, validate with read-only plans,
and investigate backend permissions and restore controls.

## 2. Compromised provider plugin executed in CI

The provider checksum changed outside the dependency-update process. Scope runner tokens,
cloud sessions, backend access, logs, network activity, roots executed, and possible state
tampering. Revoke identity, isolate runners, restore trusted artifacts, compare cloud/state,
rotate exposed secrets, and improve mirrors, locks, verification, and egress controls.

## 3. Cross-account role assumption targeted production accidentally

A default AWS provider used production credentials during a non-production run. Protect
customers, capture STS/CloudTrail evidence, determine completed calls, refresh relevant
state, and recover deliberately. Redesign aliases, defaults, account assertions, role
conditions, environment protection, and plan evidence so targets cannot be implicit.

## 4. Remote backend is unavailable during an incident

Teams request local state so they can restore service. Explain when cloud-native emergency
operations are safer than creating a second IaC authority. Define break-glass scope,
evidence, backend recovery, source reconciliation, drift handling, and how to avoid merging
ad-hoc local state into production blindly.

## 5. Module release causes organization-wide replacement

Hundreds of roots consume a module whose internal address changed. Stop rollout, identify
applied consumers, publish a repaired version with moved declarations or migration steps,
and canary recovery. Discuss immutable releases, representative upgrade tests, dependency
automation limits, staged adoption, and consumer inventory.

## 6. OpenTofu-encrypted state loses key access

Clarify encryption method, metadata, key provider, replicas, last usable backup, and roots
affected. Freeze writers, restore key access through the approved recovery path, test
decryption in isolation, and verify state/cloud bindings. Address key separation,
availability, rotation, escrow/recovery, and migration compatibility.

## 7. Drift remediation deletes an incident-created resource

An automated apply removes a temporary capacity resource still carrying traffic. Restore
service first, suspend automation, reconstruct authorization and dependencies, then encode
or retire the change deliberately. Redesign drift automation to classify severity,
respect emergency ownership/expiry, and require outcome-aware approval for deletion.

## 8. Import binds the wrong database instance

Stop applies and protect both databases. Back up state, prove resource identifiers and
configuration intent, remove the incorrect binding without deleting the remote object,
import the intended instance, and require a read-only/no-replacement plan. Add peer review,
environment assertions, and isolated adoption waves.

## 9. A policy rule blocks the disaster-recovery region

Determine whether the rule encodes a valid production invariant or assumes the primary
region. Do not broadly disable policy. Use a bounded tested exception or policy correction,
record compensating controls and expiry, restore DR, and add region/failure scenario tests
to the policy and module contracts.

## 10. Terraform-to-OpenTofu migration breaks remote-state consumers

Map producer/consumer direction, state-format features, encryption, backends, and tool
versions. Freeze writes, restore compatible backups if needed, and migrate in the supported
dependency order. Replace broad remote-state reads with stable contracts over time. Record
which roots use tool-specific features and prove rollback before continuing.
