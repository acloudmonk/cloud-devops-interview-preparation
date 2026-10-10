# Container Engineering Active-Recall Flashcards

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Use each prompt without viewing the cue. Explain the mechanism, failure mode, and
one context-dependent trade-off.

| Prompt | Answer cue |
| --- | --- |
| Container boundary | host process; kernel namespaces/cgroups/credentials/mounts/policy |
| OCI split | image layout, distribution protocol, runtime bundle/process configuration |
| Engine versus orchestrator | local lifecycle/build primitives versus scheduling/reconciliation/service rollout |
| Tag versus digest | mutable release name versus immutable content identity |
| Layer deletion | whiteout hides path; earlier bytes remain in image history |
| Build context | builder-visible files; `.dockerignore` limits leak and invalidation surface |
| Multi-stage value | separate build/test tools from minimal runtime content |
| Base pin obligation | stable digest plus owner, vulnerability signal, and update/rebuild process |
| Multi-platform index | one reference to verified architecture/OS-specific child manifests |
| Cache boundary | acceleration only; partition by trust and never treat as provenance |
| Namespace versus cgroup | resource view isolation versus resource accounting/control |
| Non-root boundary | reduces privilege but mounts/capabilities/socket/cloud identity still matter |
| Capability policy | drop all; add the minimum named privilege with evidence |
| Rootless trade-off | less host privilege versus network/storage/cgroup/compatibility constraints |
| PID 1 lifecycle | foreground process, signal forwarding, child reaping, bounded shutdown |
| Bridge connectivity | veth/bridge/routes/NAT/policy plus application bind/listener |
| `EXPOSE` boundary | metadata only; no listener or host publication |
| Writable layer | ephemeral copy-on-write state; capacity/performance/durability risk |
| Read-only root | controlled immutable runtime plus explicit narrow writable mounts |
| Workload AWS identity | task/pod-specific role; avoid host/node-wide credentials |
| Health separation | startup initializes, readiness receives traffic, liveness justifies restart |
| OOM evidence | cgroup events and kernel/platform state before limit/heap conclusions |
| Registry lifecycle | retain active/rollback/audit digests and related index/signature/attestation |
| Compromise recovery | isolate, revoke, block, scope, rebuild from known inputs, verify customer/data impact |
| Platform selection | workload/team/security/operations/cost evidence—not Kubernetes prestige |

Review missed cards after one day, three days, and seven days.
