# Container Storage and State

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Containers are replaceable processes; data durability is an explicit architecture
decision. The writable container layer is usually tied to one container lifecycle
and is not a backup, shared filesystem, or durable database.

## Storage choices

| Choice | Lifecycle and use | Key risks |
| --- | --- | --- |
| Image layer | Immutable application/runtime content | Rebuild required; copied secrets remain in history |
| Writable layer | Temporary per-container changes | Lost on replacement; copy-on-write/capacity overhead |
| `tmpfs` | Memory-backed ephemeral data | Consumes memory; disappears on stop/restart |
| Bind mount | Host path exposed directly | Host coupling, permissions, escape/data-corruption risk |
| Managed volume | Engine/platform-managed persistent path | Backup, ownership, topology, and migration still required |
| Network/block/object service | External durable state | Latency, consistency, identity, availability, and cost |

Prefer external databases, object stores, queues, and managed filesystems for
business state. Use local ephemeral storage for caches, scratch, bounded buffering,
and diagnostics within defined capacity.

## Copy-on-write and permissions

The merged filesystem presents read-only image layers plus a writable layer. The
first modification of an image file may copy data into that layer. Write-heavy
workloads can suffer performance and space amplification.

Mount ownership is evaluated by host-kernel UID/GID and filesystem rules. A
non-root image may fail when a platform mounts a path owned by another ID. Avoid
world-writable fixes. Choose stable identities and understand user-namespace
mapping, mandatory-access-control labels, and network-filesystem identity behavior.

## Read-only root filesystem

A read-only root reduces persistence but requires an inventory of legitimate writes:
temporary files, PID/socket paths, language caches, certificates, and uploads.
Mount narrow writable paths with appropriate type, capacity, permissions, and
lifecycle rather than making the whole root writable.

## AWS choices

- ECS/Fargate ephemeral storage serves image layers and task-lifecycle scratch data.
- Amazon EFS provides shared network files where latency, throughput, consistency,
  and availability fit.
- EBS provides block storage to supported task/node patterns with attachment and
  availability-zone considerations.
- S3 is object storage, not a POSIX filesystem; use object semantics explicitly.
- RDS/Aurora/DynamoDB and managed services usually hold durable application state.

Do not claim “containers are stateless” when they write sessions, queues, uploads,
or indexes locally. Identify state, consistency, recovery objectives, topology,
encryption, access, backup, restore testing, and replacement behavior.

## Storage incident questions

- Which mount and backing system contains the missing/full/corrupt data?
- Is it an image layer, writable layer, volume, memory, or external service?
- Did the workload move to a different host, zone, or identity?
- Are bytes exhausted, or inodes, quotas, file descriptors, or permissions?
- Did partial writes or concurrent writers violate the data model?
- What exact restore point and application consistency can be proven?
