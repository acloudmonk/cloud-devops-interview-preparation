# Enterprise AWS Design Exercise

[← Well-Architected review](well-architected.md) · [Next: Scenarios →](scenarios.md)

## Brief

A regulated global commerce company is replacing a single-account, single-Region AWS
estate. The platform serves web/mobile users, processes orders and payments, streams
events to analytics, exchanges files with partners, and supports internal operators.
Campaign traffic reaches 20 times baseline. Recent incidents involved expired IAM
keys, NAT failure, database connection exhaustion, noisy queues, an untested backup,
and an unallocated cloud bill. Expansion into two regulated markets is planned.

## Candidate tasks

1. Clarify business journeys, demand, data, SLOs, RTO/RPO, residency, and economics.
2. Design Organizations, OUs, accounts, identity, guardrails, and platform ownership.
3. Select Regions/AZs, VPC and hybrid/edge paths, ingress, egress, and DNS.
4. Choose compute, container/serverless, storage, database, cache, and analytics services.
5. Design APIs, queues, events, workflows, idempotency, replay, and backpressure.
6. Define security, observability, deployment, incident, backup, and recovery evidence.
7. Model quotas, capacity, cost allocation, unit economics, and sustainability.

## Required artifacts

- context and dependency diagram with account/Region/AZ boundaries;
- identity, trust, data authority, key, and audit model;
- request, event, analytical, and administrative paths;
- availability/degradation and recovery matrix;
- quota/capacity model and failure-test plan;
- deployment, observability, incident, and operational-ownership model;
- cost drivers, allocation, unit metric, and decision log.

## Failure injects

- one AZ loses new-instance capacity during a campaign;
- IAM Identity Center or an external identity provider is impaired;
- a broad SCP blocks the production recovery action;
- NAT processing cost and failure affect private workloads;
- Lambda concurrency overwhelms the relational database;
- a poison message prevents healthy queue progress;
- an encrypted backup exists but its KMS key is unavailable;
- a Region fails after the business rejects active-active complexity.

## Evaluation rubric

| Dimension | Points |
| --- | ---: |
| Discovery, workload model, outcomes, and assumptions | 7 |
| Organization, governance, identity, and security | 9 |
| Global infrastructure, networking, hybrid, and edge | 8 |
| Compute, data, and integration service decisions | 10 |
| Reliability, observability, operations, and recovery | 9 |
| Capacity, quotas, cost, sustainability, and communication | 7 |
| **Total** | **50** |

A strong answer connects AWS choices to required qualities, identifies hidden service
dependencies, defines degraded behavior and evidence, and records alternatives. A
catalog of services without authority, failure, operations, and cost is incomplete.
