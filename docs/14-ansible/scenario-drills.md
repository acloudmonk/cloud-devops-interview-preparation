# Advanced Incident Drills

[← Module overview](index.md) ·
[Scenario answer framework](../interview-playbook/scenario-answer-framework.md)

For each drill, state the first containment action, evidence to preserve,
decision owner, recovery path, and prevention changes.

## 1. Inventory filter expands from 40 to 4,000 hosts

An approved patch job has begun. Explain how you stop new batches, determine the
resolved snapshot and mutations, isolate the filter or tag change, recover
affected services, and add count thresholds without blocking legitimate scaling.

## 2. A signed execution image contains a compromised collection

Contain jobs using the digest, revoke exposed credentials, preserve image and job
evidence, identify executed modules and targets, rebuild from trusted inputs, and
reconcile state. Explain why signing proves origin, not harmlessness.

## 3. The controller database fails during a rolling restart

Some runners continue while job status is unavailable. Decide how to halt safely,
discover in-flight batches from target and runner evidence, restore controller
state, verify services, and prevent duplicate or overlapping execution.

## 4. An SSM-connected job leaves plaintext in S3

Contain bucket and role access, identify object and log exposure, delete only
after preserving required evidence, rotate affected secrets, and inspect plugin
cleanup failure. Redesign encryption, lifecycle, dedicated bucket, monitoring,
and failure-path tests.

## 5. A rescue block reports success after service failure

Explain how rescued failures affect job status, find unhealthy hosts, stop
expansion, restore service, and change the content so recovery is observable and
the final outcome assertion fails when service health is not restored.

## 6. Two teams launch conflicting production jobs

Contain both jobs, classify completed changes, and restore one authoritative
configuration. Design concurrency controls by service/environment, ownership,
change windows, workflow locks, and detection for overlapping target sets.

## 7. A Windows credential expires halfway through the estate

Separate unreachable from mutated hosts, renew through the approved identity
path, verify completed systems, and resume idempotently from a bounded limit.
Improve short-lived credential renewal, preflight lifetime checks, and batching.

## 8. Package repository metadata changes between batches

Stop rollout, record installed versions, and assess compatibility. Use immutable
repository snapshots or explicit versions, canary the corrected artifact, and
recover inconsistent hosts. Explain why identical playbook content was not an
identical change.

## 9. A malicious tag routes privileged automation to an attacker VM

Revoke automation access, stop workflows, preserve CloudTrail/controller/host
evidence, and determine executed tasks. Separate tag discovery from authorization,
govern tag writers, constrain account/network/identity, and validate host trust.

## 10. Terraform replaces instances during an Ansible run

Stop both change streams, establish authoritative infrastructure state, identify
terminated and partially configured instances, and keep uncertain nodes out of
traffic. Add orchestration, maintenance ownership, readiness signals, and
ephemeral-fleet semantics instead of relying on hostnames.

Return to the [module overview](index.md) when ready to continue.
