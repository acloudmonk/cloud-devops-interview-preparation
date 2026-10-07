# Advanced Linux Incident Drills

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-07**

These ten drills bring the module total to 25 scenarios. Give a five-minute
answer before reading the response spine.

## 16. Latency rises every day at 02:00 UTC

**Testing intent:** Correlation, scheduled work, and evidence across layers.

**Strong response spine:** Confirm the exact journey and hosts; compare cron or
systemd timers, backups, log rotation, image scans, database maintenance, and
provider events. Correlate CPU, I/O, memory pressure, network, and dependency
latency. Stagger, throttle, reschedule, or isolate the job, then verify the
customer SLI and add ownership for scheduled workload capacity.

**Follow-ups:** What if no timer exists on the host? How do time zones affect the investigation?

## 17. Instances pass provider health but fail all requests

**Testing intent:** Control-plane versus application health.

**Strong response spine:** Provider health proves only selected host/guest
signals. Inspect load-balancer target health, local representative requests,
service readiness, listeners, dependencies, credentials, and recent release.
Drain affected hosts, rollback or replace safely, and redesign health checks so
the routing decision matches the customer-serving capability.

**Follow-ups:** Can a deep health check cause an outage? Which dependencies belong in readiness?

## 18. CPU is low, but Pressure Stall Information shows sustained I/O pressure

**Testing intent:** Saturation beyond utilization.

**Strong response spine:** Attribute waits to processes/cgroups and devices;
check queue, latency, request pattern, filesystem events, and cloud-volume
limits. Protect the workload with admission or concurrency bounds, move or
isolate competing I/O, and validate with both pressure reduction and customer latency.

**Follow-ups:** What if the block device metrics look healthy? Could network storage be involved?

## 19. A security agent consumes 30% CPU fleet-wide

**Testing intent:** Security/reliability trade-offs and stakeholder handling.

**Strong response spine:** Confirm version, rollout timing, scan policy, host
classes, customer impact, and security exposure. Do not disable the agent
unilaterally. Coordinate with security, reduce scan scope/rate or pause rollout
under an approved mitigation, isolate a representative sample, and establish
performance budgets and canary gates for future agent changes.

**Follow-ups:** What if the agent addresses an actively exploited vulnerability?

## 20. A node has free memory but containers are OOM-killed

**Testing intent:** Host versus cgroup scope.

**Strong response spine:** Confirm cgroup OOM evidence, workload limit, working
set, reclaim, page cache, and recent load/version change. Protect accepted work,
right-size requests/limits from measured behavior, fix leaks, and ensure node
capacity plus eviction/admission policies prevent correlated failure.

**Follow-ups:** Why can increasing the limit harm other workloads?

## 21. A failed deployment cannot roll back because the old service will not start

**Testing intent:** Compatibility and operational change safety.

**Strong response spine:** Stop expansion, preserve current state, and determine
whether configuration, schema, filesystem ownership, runtime, or package changes
broke backward compatibility. Route to healthy capacity, use a forward fix if
rollback is unsafe, and adopt expand/contract changes, versioned configuration,
image immutability, and rollback rehearsals.

**Follow-ups:** Who decides between rollback and forward fix? What evidence is required?

## 22. Kernel logs show intermittent device resets on one Availability Zone

**Testing intent:** Guest/provider boundary and blast radius.

**Strong response spine:** Correlate affected instance types, hosts, volumes,
zone, kernel/image version, and provider health. Reduce admission, move or
replace capacity across zones without overloading them, preserve device evidence,
and escalate with timestamps and resource identifiers. Verify data consistency
and avoid assuming replacement alone fixes a zonal or image-wide issue.

**Follow-ups:** When would you stop automatic replacement?

## 23. Support requests a full memory dump from production

**Testing intent:** Diagnostic value versus sensitivity and operational risk.

**Strong response spine:** Define the hypothesis, minimum evidence, dump size,
collection overhead, sensitive-data risk, approval, encrypted destination,
access, retention, and deletion. Prefer targeted profiles or a reproduced
environment when sufficient. Record chain of custody and never attach raw dumps
to an unrestricted ticket.

**Follow-ups:** What data classes could exist in process memory?

## 24. Fleet configuration differs despite successful automation runs

**Testing intent:** Drift, desired state, and verification.

**Strong response spine:** Define authoritative desired state and sample actual
package, unit, sysctl, identity, and file evidence. Check conditional automation,
partial failure, mutable manual changes, and image age. Quarantine material
drift, replace from a known image where possible, and make convergence plus
postcondition verification observable.

**Follow-ups:** When is configuration management preferable to image replacement?

## 25. Reboot fixes the incident, but the cause is unknown

**Testing intent:** Learning from destructive mitigation.

**Strong response spine:** Acknowledge that reboot cleared transient state and
destroyed some evidence. Verify customer recovery and reconcile work, then use
pre-reboot telemetry, provider metrics, prior logs, pressure trends, coredumps,
and peer comparison. Improve bounded automatic evidence capture, define reboot
authorization, and create recurrence signals rather than claiming root cause.

**Follow-ups:** When is an immediate reboot still the correct action?

## Drill scoring matrix

| Dimension | Weak | Strong | Architect-level |
| --- | --- | --- | --- |
| Scope | One host assumption | Customer, fleet, version, and failure-domain segmentation | Tests correlated platform and organizational boundaries |
| Evidence | Random commands | Hypothesis-linked, time-correlated evidence | Minimal safe evidence with privacy and overhead controls |
| Mitigation | Restart/reboot first | Reversible customer-impact reduction | Preserves invariants, capacity, and future diagnosis |
| Recovery | Service starts | Customer SLI and unfinished work verified | RTO, consistency, failback, and accountable ownership |
| Prevention | Add an alert | Correct lifecycle, limit, rollout, or runbook | Changes operating model and validates it through exercises |

Aim for strong evidence in every dimension on at least eight drills before the
timed mock interview.
