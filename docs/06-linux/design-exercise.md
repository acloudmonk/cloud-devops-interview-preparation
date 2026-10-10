# Linux Production Design Exercise

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-07**
Estimated time: **3–4 hours**
Expected cloud cost: **None**

This is a paper-and-whiteboard exercise. It requires no VM, cloud account,
commands, application code, or infrastructure deployment.

## Scenario

A company runs a customer-facing document-conversion service on 60 Linux VMs
across three AWS Availability Zones. Traffic doubles during business hours.
Each request uploads a document, invokes CPU- and memory-intensive conversion,
writes temporary files, and stores the result in durable object storage.

Recent incidents include:

- hosts becoming unreachable after the root filesystem fills;
- conversion workers killed during peak traffic;
- a patch rollout causing 20% of instances to fail readiness;
- SSH unavailable during one recovery attempt;
- inconsistent logs and no agreed host replacement threshold.

Business requirements:

- 99.9% successful conversion availability per month;
- 95% of accepted documents complete within two minutes;
- no accepted document may be silently lost;
- customer documents and derived content are sensitive;
- critical security fixes must reach the fleet within 72 hours;
- the team has six engineers and limited overnight support.

## Tasks

### 1. Define the operating model

State assumptions about traffic, conversion duration, document size, temporary
storage, retry behavior, and accepted-work durability. Define ownership between
application, platform, security, and incident roles.

### 2. Model resource and concurrency boundaries

Estimate concurrent conversions and identify CPU, memory, process, file
descriptor, temporary storage, and downstream limits. Explain admission and
backpressure before autoscaling.

### 3. Design the Linux service lifecycle

Describe systemd ownership, readiness, graceful termination, restart limits,
temporary-file cleanup, log retention, and behavior when dependencies fail.

### 4. Design fleet replacement and patching

Compare in-place patching with image replacement. Propose canary, expansion,
rollback, drain, inventory, and old-instance removal gates.

### 5. Define secure access

Design routine and emergency access using AWS identity, Systems Manager or SSH,
least privilege, session audit, serial/offline recovery, and sensitive evidence handling.

### 6. Walk through failures

For each event, define detection, customer behavior, immediate mitigation,
evidence, recovery, and prevention:

1. root filesystem reaches 100%;
2. cgroup or guest OOM kills workers;
3. EBS latency rises in one Availability Zone;
4. a new image fails readiness after ten minutes;
5. managed access agent and SSH are both unavailable;
6. temporary-file cleanup deletes an active conversion;
7. one host’s clock differs enough to confuse event ordering.

### 7. Define telemetry and objectives

Include customer completion, accepted-work age, conversion queue, process exits,
OOM events, pressure, filesystem growth, I/O latency, instance health, version,
patch status, and access audit. State which conditions page a human.

### 8. Present two options

Compare:

- long-lived hosts patched and repaired in place;
- image-based replaceable hosts with externalized accepted-work state.

Recommend one, state migration constraints, and define when the alternative is preferable.

## Deliverables

- assumptions and service-objective table;
- resource/concurrency model;
- process and service-lifecycle diagram;
- access and trust-boundary diagram;
- patch/replacement decision record;
- failure-mode and recovery table;
- telemetry and paging proposal;
- phased 12-week improvement plan;
- ten-minute spoken operations review.

## Scoring rubric

| Area | Weight | Strong evidence |
| --- | ---: | --- |
| Requirements | 10% | Critical journey, accepted-work invariant, measurable objectives |
| Resource reasoning | 15% | Concurrency, limits, pressure, saturation, admission |
| Linux lifecycle | 15% | systemd, readiness, termination, logs, temporary data |
| Reliability | 20% | Failure layers, safe mitigation, recovery, replacement |
| Security | 15% | Identity, least privilege, access fallback, evidence handling |
| Operations | 15% | Telemetry, rollout, rollback, runbooks, ownership |
| Communication | 10% | Clear options, assumptions, risks, and phased recommendation |

## Self-review questions

- Did I preserve accepted work before discussing process restart?
- Did I distinguish host capacity from cgroup and configured limits?
- Did I cover failure of the normal access mechanism?
- Did I define evidence that replacement fixed the customer problem?
- Did I identify what remains stateful and who owns its recovery?
