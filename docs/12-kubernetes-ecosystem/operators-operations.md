# Operators and Ecosystem Operations

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

An operator combines custom APIs with controllers that encode domain operations.
It can automate expertise, but it also concentrates privilege and creates a long-lived
API/data/upgrade dependency. Not every deployment needs an operator.

## Operator decision

Use an operator when continuous domain reconciliation materially improves lifecycle:
provisioning, topology, backup, failover, upgrades, certificates, or external resources.
A script/Job, Deployment, managed service, or normal controller may be simpler for
one-time or stateless behavior.

Evaluate reconciliation idempotency, status/conditions, leader election, concurrency,
backoff, rate limits, dependency failure, manual intervention, backup/restore, and
how domain safety (quorum/fencing/data) is encoded and tested.

## CRD lifecycle

CRDs require structural schemas, validation/defaulting, version strategy, conversion,
served/storage versions, migration, status/scale subresources, finalizers, ownership,
and deletion behavior. Back up both custom objects and the external/domain data they
represent.

Upgrade order commonly involves CRD/schema, conversion webhook, controller, custom
resources, and managed workloads. Verify compatibility in both directions where a
rolling controller upgrade creates version skew. Deleting a CRD deletes all stored
custom resources; uninstall must be explicitly safe and reviewed.

## Add-on inventory

Maintain an owned catalog of every controller, webhook, APIService, CRD, DaemonSet,
node/kernel dependency, cloud IAM role, certificate, namespace, repository/chart,
configuration, supported Kubernetes version, upgrade path, data/backup, SLO, and
escalation. Discover shadow add-ons installed by teams.

Managed add-ons reduce some packaging/version work but do not eliminate configuration,
compatibility, identity, rollout, observability, or workload-impact decisions. Separate
cloud-provider ownership from platform-team responsibility.

## Upgrade dependency graph

Order changes from APIs and prerequisites through controllers to data planes and
consumers. Check Kubernetes/API deprecations, CRDs/conversion, webhooks, RBAC, images,
kernel/CNI/CSI, stored data, configuration schemas, and downgrade support. Use a
representative test cluster, cohorts, surge/headroom, health/business gates, and
explicit stop/recover decisions.

“Rollback the chart” may not reverse CRD storage migration, database change, generated
certificate, cloud resource, or data-plane state. Prefer forward-compatible staged
changes and backups/restores tested for irreversible boundaries.

## Failure and troubleshooting

Classify:

- source/render/apply and field-ownership failure;
- API/CRD/schema/conversion or admission failure;
- controller watch/cache/leader/workqueue/reconcile failure;
- external cloud/identity/rate-limit/availability failure;
- data-plane/node/webhook/certificate failure;
- unhealthy domain resource despite successful reconciliation.

Preserve object UID/generation/spec/status/conditions/managed fields/finalizers,
controller version/config/leader/logs/metrics/workqueue, webhook/APIService health,
RBAC/audit, cloud events, and customer signals before restarting or deleting.

## Continuity and removal

For each add-on define what existing and new workloads do when it is unavailable;
known-good images/manifests/config; identity and certificate recovery; backup; minimum
manual operation; and restoration order. Test control-plane dependency cycles.

Removal is a migration: stop new consumers, export/convert data, remove dependent
resources and finalizers through their controller, remove webhooks/API services only
when safe, retain or delete CRs deliberately, uninstall controller, then remove CRDs/
RBAC/cloud resources and verify no orphaned infrastructure remains.
