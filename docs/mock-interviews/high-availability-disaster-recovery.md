# High Availability, DR, and Business Continuity Mock Interview

[← Mock interview overview](index.md) ·
[Module 25 overview](../25-ha-dr-bcp/index.md) ·
[Scenario answer framework](../interview-playbook/scenario-answer-framework.md)

Duration: **50 minutes**

Level: **Senior / Architect**

Primary context: **AWS-first regulated payments platform with multi-cloud dependencies**

## Candidate brief

A payments company runs customer APIs and transaction processing across three AWS
Availability Zones in one Region. Aurora PostgreSQL is the system of record, EKS
hosts services, and S3 stores documents. Workforce identity is in Azure, analytics
is in Google Cloud, and external payment networks are critical. Leadership asks
for zero downtime and zero data loss. Backups share the production account, the
secondary Region is incomplete, and regional recovery has never been tested.
Design the continuity strategy and operating model.

## Interview structure

### 0–6 minutes — Discovery and impact

Ask about journeys, minimum service, impact over time, transaction semantics,
operating periods, regulation, dependencies, failure scope, current objectives,
staffing, suppliers, budget, authority, and evidence.

### 6–15 minutes — Objectives and tiering

Define BIA outputs, tiers, availability, RTO, RPO, MTPD, work recovery time,
measurement boundaries, prerequisite ordering, approval, and residual-risk process.

### 15–27 minutes — Architecture

Design Multi-AZ availability, degraded modes, selected regional recovery pattern,
traffic, capacity, single-writer/fencing, replication, immutable isolated backup,
keys/identity, artifacts/configuration, dependencies, cyber recovery, and failback.

### 27–37 minutes — Event branches

Choose two:

1. Regional errors are intermittent and the provider status page is green.
2. Replicated data may be corrupted by compromised credentials.
3. Warm standby reaches quota limits while scaling.
4. Both Regions accepted conflicting payment writes.
5. The primary Region returns midway through recovery.

Establish command and facts, protect customers and integrity, choose containment
and recovery, communicate uncertainty, validate business service, and plan return
to normal.

### 37–44 minutes — Continuity and evidence

Cover crisis leadership, workforce and supplier loss, manual process capacity,
alternate communications, runbooks, exercise progression, actual RTO/RPO,
findings, risk acceptance, change triggers, and corrective-action retest.

### 44–47 minutes — Executive recommendation

Summarize critical outcome, largest risk, objective, target architecture, first
three investments, evidence plan, cost/complexity trade-off, and decision required.

### 47–50 minutes — Candidate questions

Ask about risk appetite, regulatory duties, incident history, transaction semantics,
supplier commitments, staff capability, recovery funding, or board-level outcomes.

## Scoring rubric

| Dimension | Expected evidence |
| --- | --- |
| Discovery and BIA | business journeys, impact over time, minimum service, dependencies, owners |
| Objectives and tiers | measurable RTO/RPO/MTPD, scope, sequence, approval |
| HA and failure analysis | zones, correlated failure, dependencies, capacity, degradation |
| DR architecture | justified pattern, Region readiness, control-plane awareness |
| Data and cyber recovery | consistency, lag, fencing, immutable isolation, keys, reconciliation |
| Activation and failback | signals, authority, roles, validation, source of truth, safe return |
| Business continuity | people, suppliers, workarounds, communications, backlog |
| Testing and governance | progressive exercises, measurements, findings, retest, risk acceptance |
| Cloud and communication | AWS depth, multi-cloud translation, clear trade-offs and recommendation |

Score each 0–4. Maximum: **36**. Scores of 31–36 show strong architect signal;
24–30 are credible with gaps; 17–23 need deeper end-to-end recovery reasoning;
below 17 should revisit the concepts and scenarios.

Return to the [module overview](../25-ha-dr-bcp/index.md) after scoring.
