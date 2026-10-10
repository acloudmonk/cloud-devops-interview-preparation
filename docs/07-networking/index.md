# Cloud Networking & DNS

[← Curriculum overview](../curriculum/index.md) ·
[Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**
Level: **Senior / Architect**

Senior networking interviews test whether you can follow a request across name
resolution, routes, policy, transport, encryption, proxies, and application
health. The goal is to isolate the failing boundary, not recite the OSI model.

!!! tip "Where to start"
    Start with **1. Network mental model** and follow the numbered path. AWS VPC
    is the cloud anchor, with Azure and Google Cloud differences where semantics
    affect design or troubleshooting. No cloud account or packet lab is required.

## Learning objectives

By the end of this module, you should be able to:

- trace a client request through DNS, routing, policy, transport, TLS, and proxies;
- calculate and review CIDR plans, subnet boundaries, and address consumption;
- distinguish reachability, transport establishment, TLS negotiation, and application success;
- explain DNS delegation, recursion, caching, TTL, negative answers, and split-horizon risks;
- reason about TCP behavior, UDP trade-offs, HTTP connection reuse, and timeouts;
- design load-balancing, egress, ingress, private-access, and hybrid-network patterns;
- translate AWS networking decisions to Azure and Google Cloud without false equivalence;
- troubleshoot from customer symptom to the smallest failing boundary using safe evidence;
- communicate security, reliability, operational, latency, and cost trade-offs.

## Recommended module path

### Phase 1 — Learn the system

| Step | Page | Outcome |
| ---: | --- | --- |
| 1 | [Network mental model](concepts.md) | Trace packets and requests across layers and administrative boundaries |
| 2 | [IP, CIDR, subnetting, and routing](ip-cidr-routing.md) | Plan addresses and reason about route selection, NAT, and return paths |
| 3 | [DNS and service discovery](dns-service-discovery.md) | Explain resolution, caching, delegation, health, and failure behavior |
| 4 | [Transport, HTTP, and TLS](transport-http-tls.md) | Separate connection, encryption, protocol, and application failures |
| 5 | [Load balancing and proxies](load-balancing-proxies.md) | Design traffic distribution, health checks, draining, and client identity |
| 6 | [Cloud network architecture](cloud-networking.md) | Apply AWS-first VPC patterns and translate Azure/GCP semantics |
| 7 | [Hybrid and private connectivity](hybrid-connectivity.md) | Choose VPN, dedicated links, peering, transit, and private service access |
| 8 | [Troubleshooting playbook](troubleshooting-playbook.md) | Investigate methodically with bounded, privacy-aware evidence |

### Phase 2 — Apply the reasoning

| Step | Page | Outcome |
| ---: | --- | --- |
| 9 | [Network design exercise](design-exercise.md) | Design a resilient private application network without deployment |
| 10 | [Scenario questions and model answers](scenarios.md) | Practise 15 core networking scenarios |
| 11 | [Advanced incident drills](scenario-drills.md) | Handle 10 ambiguous cross-layer failures |
| 12 | [Ten-minute network review](presentation-template.md) | Present flows, risks, decisions, and verification clearly |

### Phase 3 — Revise and assess

| Step | Page | Outcome |
| ---: | --- | --- |
| 13 | [Rapid-fire revision](rapid-fire.md) | Test 50 concise verbal explanations |
| 14 | [Active-recall flashcards](flashcards.md) | Revisit weak concepts with spaced repetition |
| 15 | [Timed networking mock interview](../mock-interviews/networking-operations.md) | Complete a scored 50-minute assessment |
| 16 | [References and videos](references.md) | Deepen weak areas with primary sources |

## Scope boundary

This module covers network architecture and troubleshooting. Detailed Linux
process/socket ownership belongs to [Module 06](../06-linux/index.md).
Kubernetes CNI, Services, ingress, and network policy belong to
[Module 11](../11-kubernetes/index.md). Provider landing-zone implementation
belongs to the dedicated AWS, Azure, and GCP modules.

## Completion checklist

- [ ] I can narrate a request path and name every policy and state boundary.
- [ ] I can calculate subnet size and explain reserved/consumed addresses.
- [ ] I can distinguish DNS, route, firewall, TCP, TLS, proxy, and application failure.
- [ ] I can explain safe rollback for DNS, route, and firewall changes.
- [ ] I answered all 25 scenarios aloud and recorded weak areas.
- [ ] I completed the design exercise before reading scenario answers.
- [ ] I completed the mock interview and recorded evidence for each score.
