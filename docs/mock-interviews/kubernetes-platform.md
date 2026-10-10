# Mock Interview: Kubernetes Platform Architecture

[← Kubernetes module overview](../11-kubernetes/index.md) ·
[Master competency map](../master-competency-map.md)

Use this 50-minute interview after completing Module 11. Reveal follow-ups only
when their section begins.

## Candidate brief

A 300-engineer organization will move 45 services to EKS across two AWS regions.
Teams propose one shared production cluster with broad administrator and node IAM
roles. Workloads lack requests, topology, disruption budgets, network policy, and
restore tests. Liveness checks call a shared database. The platform must tolerate a
zone failure, isolate regulated and partner-controlled work, and recover bad releases
within ten minutes. Design the platform and adoption plan.

## Schedule

| Time | Candidate task | Interviewer observes |
| --- | --- | --- |
| 0–5 min | Clarify workload, data, tenant, recovery, compliance, team, and cost constraints | Discovery before topology/tool choice |
| 5–12 min | Explain API, reconciliation, control plane, nodes, and managed responsibility | Kubernetes mental model |
| 12–21 min | Design account/cluster/namespace/node topology and workload lifecycle | Architecture and availability |
| 21–29 min | Design requests, placement, autoscaling, probes, rollout, and disruption | Scheduling and reliability |
| 29–37 min | Design traffic, storage, state, and one-zone recovery | Network/data reasoning |
| 37–44 min | Design RBAC, workload identity, admission, secrets, and tenant isolation | Security depth |
| 44–50 min | Present upgrades, continuity, adoption, measures, and recommendation | Operations and leadership |

## Required follow-ups

1. Pods remain Pending after new nodes launch. What evidence changes your action?
2. A privileged DaemonSet is compromised across all nodes. How do you recover?
3. An admission webhook blocks every deployment. When may you bypass it?
4. A zonal EBS workload cannot start after availability-zone failure. What now?
5. A control-plane upgrade exposes a removed API and cannot be downgraded. Recover.

## Decision follow-ups

| Candidate choice | Ask |
| --- | --- |
| One shared cluster | How are hostile, regulated, noisy, and admin trust boundaries contained? |
| Cluster per team | How are cost, upgrades, add-ons, policy, and fleet consistency managed? |
| Use Fargate | Which DaemonSet, storage, network, performance, or cost needs do not fit? |
| Self-host databases | Who owns quorum, fencing, backup, restore, upgrade, and incident expertise? |
| Strict default deny | How do DNS, identity, telemetry, dependencies, and emergency diagnostics work? |
| Aggressive autoscaling | How are metric lag, cold start, node capacity, PDBs, and downstream limits handled? |

## Scorecard

Score each dimension from 0 to 4.

| Dimension | 0–1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| Discovery | Starts with manifests/tools | Basic scale questions | Workload, data, tenant, recovery, team | Finds constraints that change boundaries |
| Mental model | Command/resource trivia | Names components | Correct API/reconciliation/ownership model | Predicts distributed convergence failure |
| Workload/reliability | “Three replicas” | Controllers/probes | Placement, health, rollout, PDB, shutdown | Data/dependency/capacity failure integrated |
| Network/storage | Service/PVC lists | Plausible choices | End-to-end paths/topology/recovery | Consistency, identity, zone/region trade-offs |
| Security | RBAC only | Some policies/secrets | Human/workload identity, admission, runtime | Tenant isolation from attacker paths |
| Operations | Restart/upgrade | Logs and maintenance | Evidence, add-ons, nodes, skew, continuity | Irreversible state and tested recovery |
| AWS/platform | EKS service list | Reasonable node choices | Shared responsibility and integrations | Account/region/quota/cost/adoption evidence |
| Leadership | Tool dump | Understandable | Migration, measures, decision | Concise risk/trade-off with owner/evidence |

Maximum score: **32**. A score of 25 or more with no dimension below 2 is a
strong senior-level practice result.

## Reflection

Record one missed controller/owner, one invalid availability assumption, one unsafe
privilege path, one weak recovery step, and one answer to shorten. Repeat in seven days.
