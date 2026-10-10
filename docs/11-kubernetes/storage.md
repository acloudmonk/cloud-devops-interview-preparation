# Kubernetes Storage and Stateful Workloads

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Kubernetes can provision and attach storage; it does not define application
consistency, replication, quorum, fencing, backup, or restore correctness. Start with
the data contract, then choose the volume and controller behavior.

## Objects and lifecycle

- **PersistentVolume (PV):** cluster storage resource with capacity, access modes,
  reclaim policy, and implementation details.
- **PersistentVolumeClaim (PVC):** workload request for storage characteristics.
- **StorageClass:** provisioning policy, driver, parameters, reclaim/binding behavior,
  expansion, and allowed topology.
- **CSI:** plugin contract for provisioning, attachment, mount, snapshot, and related
  operations.

Dynamic provisioning creates a PV from a StorageClass after a claim. `Immediate`
binding can select storage before node placement; `WaitForFirstConsumer` allows Pod
topology to influence provisioning. This matters for zonal block storage.

## Access and placement

Access modes describe intended node mount behavior but are not a universal filesystem
locking guarantee. A ReadWriteOnce volume generally constrains attachment to one node,
not necessarily one Pod. ReadWriteMany requires a compatible shared filesystem.
ReadWriteOncePod provides stricter single-Pod use where supported.

Volume node affinity, Pod scheduling, zone capacity, attachment limits, and failure
recovery must agree. Moving a Pod across zones cannot move a zonal disk automatically.
Multi-attach and stale attachment errors may require careful fencing, not force.

## StatefulSets and identity

StatefulSets provide stable ordinals, hostnames, and per-Pod claim templates. They do
not migrate data between replicas or elect leaders. Scale-down/deletion often retains
claims deliberately; define retention, ownership, and decommission procedures.

For databases and queues, prefer a managed service when it satisfies latency,
control, compliance, and portability needs. If self-hosting, design failure quorum,
anti-affinity/topology, replication lag, maintenance, version skew, backup, restore,
and operator competence—not just a StatefulSet manifest.

## AWS anchor

- Amazon EBS CSI provides zonal block volumes and snapshots; account for attachment,
  throughput/IOPS, expansion, KMS, zone, and node identity.
- Amazon EFS CSI provides shared network filesystem semantics; account for latency,
  throughput mode, access points, UID/GID, network, and mount availability.
- S3 is object storage and should normally be used with object semantics rather than
  treated as a transparent POSIX volume.
- EKS workload/driver identity and least privilege should replace node-wide storage
  permissions where supported.

AKS disks/files and GKE persistent disks/Filestore express similar block/shared
choices with different topology, identity, snapshot, and managed-control behavior.

## Backup and restore

Cluster-object backup, PV snapshot, and application-consistent backup are distinct.
Coordinate writes, transaction logs, external services, encryption keys, identity,
DNS, and restore order. Record recovery point/time objectives and test restoration
into an isolated environment. A successful snapshot API call does not prove a usable
business recovery point.

## Troubleshooting order

Inspect PVC/PV/StorageClass status and events, selected node/zone, CSI controller and
node plugin, cloud volume state, attachment limits, mount/device/filesystem errors,
permissions/security labels, capacity/inodes, and application consistency. Preserve
evidence before force-detaching or deleting finalizers.
