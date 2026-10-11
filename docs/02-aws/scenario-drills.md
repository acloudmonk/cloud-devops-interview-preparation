# Advanced AWS Architecture and Incident Drills

[← Scenario questions](scenarios.md) · [Next: Presentation template →](presentation-template.md)

For each drill, state containment, investigation, decision authority, recovery,
communications, evidence, and prevention. Practise a three-minute response.

## Drill 1 — SCP blocks incident recovery

Confirm the denied action and policy path from CloudTrail without weakening the whole
organization. Use a predesigned emergency role or narrow, time-bound policy change
through authorized owners; record every action. Restore service and then stage the
corrected SCP in a policy-test OU. Add recovery-action tests, exception expiry, and
independent review. A broad detach during an incident can expand compromise and hide
the underlying policy error.

## Drill 2 — One AZ cannot launch capacity

Stop assuming Auto Scaling guarantees replacement. Inspect instance type, purchase
option, subnet IPs, placement, quotas, and launch failures. Shift load safely to proven
remaining capacity, diversify instance families/sizes and AZs where compatible, and
protect downstreams from retry amplification. If headroom is insufficient, degrade
lower-priority features. Future capacity tests and deployment models must include
zonal scarcity and static stability.

## Drill 3 — NAT gateway failure and high transfer cost

Map each private-subnet route and AZ dependency, then restore egress through an
independent same-AZ path or controlled failover. Separate outage from cost analysis.
Move AWS-service traffic to appropriate VPC endpoints, reduce unnecessary cross-AZ
paths and external transfers, and examine caching/proxy needs. Validate DNS, firewall,
port, and return paths. Centralized egress needs an explicit availability and cost
case, not only visual simplicity.

## Drill 4 — KMS key becomes unavailable

Identify affected services, ciphertext, key state, Region/account, policy/grants, and
whether deletion is pending. Freeze destructive changes, restore authorized key access
or cancel deletion if still possible through controlled break-glass procedures, and
validate applications and backups. Communicate potential data unavailability. Improve
separation of key administration/use, deletion safeguards, multi-Region strategy where
justified, key dependency inventory, and restore exercises.

## Drill 5 — Queue backlog grows while consumers look healthy

Measure oldest-message age, arrival and completion rates, in-flight work, visibility
timeouts, retries, DLQ, poison messages, partition/group skew, and downstream latency.
Quarantine bad work and scale consumers only within downstream budgets. Correct
acknowledgement/idempotency behavior and safely redrive. Monitor business completion,
not container health or queue depth alone, and load-test burst plus dependency failure.

## Drill 6 — Multi-AZ database is available but checkout fails

Trace DNS and failover timing, application connection pools, stale addresses, TLS,
credentials, transaction retries, timeouts, proxy behavior, and dependency capacity.
Contain retry storms and establish whether writes committed before retrying. Restore
with bounded, idempotent behavior and reconcile orders/payments. Update failover tests
to include applications, caches, connections, alerts, and business invariants—not only
database status.

## Drill 7 — Root credentials appear in an audit log

Invoke the security incident process, validate the event, restrict root use, rotate or
remove credentials, review MFA/contact controls, preserve evidence, and search
CloudTrail plus affected resources/accounts for actions. Contain compromised resources
without destroying forensic data. Test alternate explanations but assume impact until
bounded. Prevent with no root access keys, protected root MFA, monitored use, shared
business contacts, and rehearsed recovery.

## Drill 8 — CloudFormation deployment partially changes production

Stop concurrent change, inspect stack events, nested/custom resources, rollback state,
and external side effects. Restore through the safest known template or bounded manual
action recorded for reconciliation; do not edit randomly. Validate service and data,
then reconcile drift. Improve change sets, policy checks, contract/data compatibility,
canaries, failure injection for custom resources, and a tested path for
UPDATE_ROLLBACK_FAILED or delivery-system loss.

## Drill 9 — Cross-Region failover causes split writes

Fence one writer and preserve logs before changing routing again. Determine committed
writes, replication state, clock/order assumptions, conflicts, and business invariants.
Choose authoritative records with data owners, reconcile and compensate, and restore
controlled service even if degraded. Redesign global write authority, health criteria,
failover decision rights, idempotency, conflict policy, failback, and game-day evidence.

## Drill 10 — Cost anomaly follows a release

Correlate CUR/Cost Explorer dimensions, deployment time, usage, requests, data transfer,
logs, storage, retries, scaling, and third-party charges. Contain runaway behavior with
safe budgets, quotas, concurrency, or rollback while preserving user priorities.
Compare unit economics and performance, not total cost alone. Add cost forecasts and
telemetry to release gates, ownership tags/categories, anomaly routing, and architecture
tests for retry or transfer amplification.

## Drill 11 — Identity provider is unavailable

Separate existing workload credentials from new workforce sessions. Preserve service
operation, invoke tightly protected and tested break-glass roles for essential human
actions, and prevent uncontrolled local-user creation. Coordinate with the identity
owner and log every emergency session. Validate expiry and revoke access after
recovery. Design federation redundancy where supported, cached session expectations,
emergency contacts, root/account recovery, and regular access exercises.
