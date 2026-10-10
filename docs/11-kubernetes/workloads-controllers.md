# Workloads, Controllers, and Lifecycle

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

A Pod is the smallest scheduling unit: one or more tightly coupled containers that
share network and selected Linux namespaces/volumes. A bare Pod is rarely the right
production unit; a controller should own replacement, rollout, and desired count.

## Workload selection

| Workload | Use when | Important contract |
| --- | --- | --- |
| Deployment | Replaceable stateless replicas and rolling updates | ReplicaSet ownership, surge/unavailable, readiness |
| StatefulSet | Stable ordinal/network/storage identity and ordered behavior matter | Headless discovery, per-Pod claims, update policy |
| DaemonSet | One eligible Pod per node for node-local function | Tolerations, priority, rollout, resource reservation |
| Job | Finite work must complete successfully | Idempotency, completions/parallelism, retry/deadline |
| CronJob | Jobs start on a schedule | Concurrency policy, missed schedules, timezone, idempotency |

StatefulSet does not make an application stateful-safe. The application and storage
system still own replication, quorum, fencing, backup, restore, and data consistency.

## Pod composition

Keep containers in one Pod only when they share lifecycle, placement, network, and
volumes. Init containers perform ordered setup and must be restart-safe. Sidecars can
provide tightly coupled supporting behavior but consume resources and complicate
startup, shutdown, security, and ownership. Ephemeral containers support debugging;
they are not normal application lifecycle or a repair mechanism.

## Health and startup

- **Startup probe:** suppresses liveness/readiness until slow initialization succeeds.
- **Readiness probe:** controls endpoint eligibility; failure should remove traffic,
  not restart the process.
- **Liveness probe:** restarts when local process recovery is likely; avoid deep shared
  dependency checks that can create restart storms.

The application must also handle `preStop`/SIGTERM, endpoint removal propagation,
connection draining, in-flight work, lease/message visibility, and the termination
grace period. Test shutdown during real traffic and node drain.

## Deployment rollout

RollingUpdate uses `maxSurge` and `maxUnavailable` to balance capacity, speed, and
resource headroom. Progress depends on readiness and deadline; old/new versions can
coexist, so APIs, schemas, messages, and configuration must be compatible.

Kubernetes Deployment rollback changes the Pod template to an earlier revision; it
does not reverse databases, external effects, ConfigMaps/Secrets, or every dependency.
Deployments also do not provide true canary analysis by themselves. Progressive
delivery controllers belong to Module 12.

## Disruption and availability

PodDisruptionBudgets limit voluntary disruptions against healthy desired replicas;
they do not protect against node failure, application crash, force deletion, or every
controller action. Set them with replica count, quorum, rollout, autoscaling, and
maintenance capacity in mind. An impossible budget can block drains and upgrades.

Use topology spread and anti-affinity to distribute replicas across failure domains,
but confirm the cluster has capacity in those domains. Balance strict placement
against schedulability during failures.

## Job semantics

Retries, duplicate starts, worker/node loss, and uncertain completion make job work
at-least-once in many designs. Use idempotency keys, transactional/outbox patterns,
checkpointing, bounded backoff, active deadlines, and explicit failure/dead-letter
handling. A successful Pod status alone may not prove the external business action.
