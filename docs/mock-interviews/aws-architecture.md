# AWS Architecture Mock Interview

[← Mock interview overview](index.md) · [Module 02 overview](../02-aws/index.md)

Duration: **50 minutes**
Level: **Senior / Architect**
Primary context: **Regulated global commerce platform on AWS**

## Candidate brief

A global commerce company runs in one AWS account and one Region. It serves web/mobile
users, processes orders and payments, sends events to analytics, exchanges files with
partners, and supports internal operations. Campaign traffic reaches 20 times normal.
Recent incidents involved long-lived keys, zonal dependencies, connection exhaustion,
queue backlog, an untested backup, quota pressure, and unexplained cost. Design the
AWS target and its operating model for expansion into two regulated markets.

## Interview structure

### 0–7 minutes — Discovery and workload

Clarify users, critical journeys, demand and burst, data/invariants, latency, SLOs,
RTO/RPO, residency, compliance, integrations, change, skills, support, and economics.
State assumptions and decision criteria.

### 7–17 minutes — Foundation and security

Design Organizations, OUs, accounts, landing zone, identity federation, workload roles,
SCPs and policy layers, keys, logs, detection, incident access, responsibilities,
exceptions, and platform ownership.

### 17–28 minutes — Platform architecture

Choose Regions/AZs, VPCs, ingress/egress, DNS, edge and hybrid paths; then select
compute, containers/serverless, storage, database, cache, analytics, API, messaging,
event, and workflow capabilities. Explain service scope, authority, and limits.

### 28–38 minutes — Failure branches

Choose three:

- an AZ cannot launch new capacity during a campaign;
- an SCP blocks the production recovery action;
- private egress fails and cross-AZ NAT cost is high;
- Lambda bursts exhaust database connections;
- a poison message causes an old queue backlog;
- a KMS key is unavailable during restore;
- a database failover completes but checkout remains down;
- a Region is impaired and data cannot accept concurrent writers.

### 38–45 minutes — Operations, recovery, and economics

Define observability, SLOs, incident and change paths, backup/restore, recovery testing,
quotas, failure capacity, allocation, unit economics, optimization, commitments,
sustainability, and Well-Architected review evidence.

### 45–50 minutes — Executive close

State the recommended architecture and first delivery slice, top risks and assumptions,
owners, measurable evidence, cost drivers, and conditions that would change the design.

## Scoring rubric

| Dimension | Points |
| --- | ---: |
| Discovery, workload model, outcomes, and assumptions | 7 |
| Global infrastructure, accounts, governance, identity, and security | 10 |
| Networking, hybrid connectivity, edge, and traffic | 8 |
| Compute, data, API, messaging, and event service decisions | 10 |
| Reliability, observability, operations, and recovery | 8 |
| Quotas, capacity, cost, sustainability, and evidence | 5 |
| Trade-offs and executive communication | 2 |
| **Total** | **50** |

Interpretation: **43–50** architect-ready; **35–42** strong with targeted gaps;
**25–34** incomplete service semantics or operational reasoning; **below 25** rebuild
from workload, boundaries, failure, and evidence. A service catalog without security,
failure, quotas, operations, and economics cannot exceed 34.

## Improvement loop

Record the three weakest decisions, revisit the matching module pages and primary
sources, redraw the boundaries and dependencies, then repeat within seven days using
different failure branches.
