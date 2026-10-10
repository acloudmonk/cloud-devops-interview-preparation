# Mock Interview: Docker and Container Engineering

[← Container module overview](../10-docker/index.md) ·
[Master competency map](../master-competency-map.md)

Use this 50-minute interview after completing Module 10. Reveal follow-ups only
when their section begins.

## Candidate brief

A 250-engineer company is moving 35 services from EC2 virtual machines to AWS
containers. Images are rebuilt per environment under mutable tags, average 1.8 GB,
run as root without limits, share one AWS role, and store logs/uploads locally.
Production must support two regions, ARM and AMD64, ten-minute bad-release recovery,
and isolated execution of untrusted customer code. Design the container platform.

## Schedule

| Time | Candidate task | Interviewer observes |
| --- | --- | --- |
| 0–5 min | Clarify workload, data, security, recovery, team, and cost constraints | Discovery before platform choice |
| 5–12 min | Explain image, registry, runtime, kernel, and orchestrator boundaries | Container mental model |
| 12–20 min | Design build, base, layer, multi-platform, and promotion standards | Artifact engineering |
| 20–29 min | Design identity, isolation, secrets, network, mount, and supply-chain controls | Security depth |
| 29–37 min | Choose ECS/Fargate/EC2/EKS patterns and resource/health lifecycle | AWS and operations judgment |
| 37–44 min | Handle state, bad release, compromise, registry/region failure | Recovery reasoning |
| 44–50 min | Present migration, measures, and executive recommendation | Adoption and communication |

## Required follow-ups

1. The approved base digest is compromised across 160 derived images. What now?
2. ARM and AMD64 manifests contain different source revisions. How do you recover?
3. A service is repeatedly OOM-killed. Which evidence changes your response?
4. The registry is unavailable during a critical regional recovery. What is allowed?
5. Why is a non-root container with the Docker socket still a critical risk?

## Decision follow-ups

| Candidate choice | Ask |
| --- | --- |
| Standardize on Fargate | Which workloads/features/cost profiles do not fit? |
| Standardize on EKS | Which Kubernetes capabilities justify its operational burden? |
| Use distroless images | How are certificates, diagnostics, patching, and incident access handled? |
| Require read-only root | Which paths write, what backs them, and how is capacity controlled? |
| Sign every image | Which identity, builder, claims, revocation, and admission policy are trusted? |
| Use ARM for savings | How are native dependencies, tests, manifests, capacity, and fallback handled? |

## Scorecard

Score each dimension from 0 to 4.

| Dimension | 0–1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| Discovery | Chooses Kubernetes/Docker immediately | Basic workload questions | Data, risk, recovery, scale, team | Finds constraints that change platform/boundary |
| Mental model | Containers are small VMs | Basic image/process | Correct OCI/runtime/kernel/orchestrator split | Predicts subtle lifecycle/isolation failures |
| Build/artifact | Small image only | Multi-stage and scanning | Controlled inputs, digest, platform, evidence | Reproducibility and compromise response integrated |
| Runtime security | “Run non-root” | Some capabilities/secrets | Layered identity, syscall, mount, network, host | Tenant boundary chosen from attacker paths |
| Operations | Restart and add resources | Logs/health/limits | Evidence-led resource/lifecycle/debug design | Capacity, correlated failure, and recovery tested |
| State/network | Volumes and ports | Plausible services | Explicit lifecycle, discovery, policy, backup | Consistency/topology/outage behavior integrated |
| AWS/platform | Lists ECS/EKS | Reasonable preference | Workload-specific managed/self-managed trade-off | Multi-region/isolation/cost and adoption evidence |
| Leadership | Tool dump | Understandable | Migration, measures, decision | Concise risk/trade-off with owner and evidence |

Maximum score: **32**. A score of 25 or more with no dimension below 2 is a
strong senior-level practice result.

## Reflection

Record one incorrect boundary, one weak artifact assumption, one unsafe privilege,
one missed recovery dependency, and one answer to shorten. Repeat within seven days.
