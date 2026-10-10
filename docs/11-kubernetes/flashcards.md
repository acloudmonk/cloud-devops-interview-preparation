# Kubernetes Active-Recall Flashcards

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Use each prompt without viewing the cue. Explain the mechanism, failure mode, and
one context-dependent trade-off.

| Prompt | Answer cue |
| --- | --- |
| Reconciliation loop | desired object → observe → diff → act → status → retry/converge |
| API success boundary | accepted/persisted intent; workload convergence and customer health remain separate |
| Resource version | optimistic concurrency and watch continuity, not release numbering |
| Owner/finalizer | dependent garbage collection versus cleanup gate before deletion |
| Managed fields | server-side field ownership; detect conflicts between declarative actors |
| Control-plane split | API/etcd/scheduler/controllers versus kubelet/runtime/plugins on nodes |
| Pod boundary | shared network/lifecycle/volumes; controller normally owns replacement |
| StatefulSet limit | stable identity/claims, not replication, quorum, fencing, backup, or consistency |
| Probe separation | startup initializes, readiness routes, liveness justifies local restart |
| PDB boundary | voluntary eviction budget, not protection from involuntary failure |
| Request/limit | placement/accounting versus runtime bound; throttling and OOM differ |
| Taint/toleration | repel and permit; toleration alone does not select a node |
| Autoscaling chain | workload metric/replicas → pending demand → node capacity with lag/constraints |
| Service/EndpointSlice | stable virtual identity mapped to ready selected Pod endpoints |
| NetworkPolicy boundary | additive allow for selected directions; CNI enforcement/features required |
| PVC/topology | claim/class/binding plus node/zone/attachment constraints |
| Snapshot boundary | crash/storage consistency only unless application and external state coordinated |
| RBAC indirect privilege | workload create/exec/impersonate/bind/escalate may expose identities and data |
| EKS workload identity | bounded service account to narrow IAM role; avoid node-role inheritance |
| Namespace tenancy | useful scope/quota/RBAC boundary, not hostile-code isolation |
| Admission availability | policy dependency needs scope, HA, timeout, failure policy, break-glass |
| Events versus audit | transient observations versus durable API request evidence |
| Drain safety | PDB/capacity/topology/state/shutdown/traffic must agree before eviction |
| Upgrade contract | APIs, webhooks, CRDs/controllers, add-ons, nodes, skew, irreversible steps |
| Incident method | desired/observed/owner/controller/dependency/evidence/recovery verification |

Review missed cards after one day, three days, and seven days.
