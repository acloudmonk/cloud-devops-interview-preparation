# Hybrid and Multi-Cloud Architecture Mock Interview

[← Mock interview overview](index.md) · [Module 28 overview](../28-hybrid-multicloud/index.md) ·
[Scenario framework](../interview-playbook/scenario-answer-framework.md)

Duration: **50 minutes** · Level: **Senior / Architect**

## Candidate brief

A regulated manufacturer runs SAP/factory systems on-premises, customer services
on AWS, workforce identity on Azure, and analytics/ML on Google Cloud. Acquisitions
created overlapping networks/directories. Factories need autonomous WAN-loss operation.
Leadership wants full portability and cross-provider failover while reducing data-center cost.

## Interview structure

### 0–7 — Discovery

Clarify business drivers, workloads, users/devices, latency, data/sovereignty, SLOs,
RTO/RPO, estate, contracts, skills, cost, timeline, authority, and exit expectation.

### 7–18 — Strategy and placement

Choose patterns and component/data placement. Distinguish transition from steady state,
test single-provider simplification, and define portability tiers and rejected options.

### 18–30 — Architecture and operation

Cover connectivity/BGP/IP/DNS, identity/trust/keys, data authority/integration,
platform/delivery, telemetry, incident command, support, capacity, drift, and economics.

### 30–40 — Failure branches

Choose two: central identity outage; carrier common mode; cross-cloud data divergence;
factory disconnection; compromised delivery system; or provider control-plane outage.
Contain, degrade, recover, reconcile, communicate, and improve.

### 40–46 — Governance and roadmap

Define placement authority, landing zones, policy intent/native controls, ownership,
skills, TCO/egress, exceptions, recovery/exit tests, sequencing, and retirement.

### 46–50 — Executive summary and questions

Present driver, pattern, largest risks, investment, proof, residual risk, decision,
and simplification trigger; ask about sovereignty, acquisitions, contracts, or capability.

## Scoring rubric

| Dimension | Expected evidence |
| --- | --- |
| Driver and placement | durable outcomes, constraints, pattern, simplification |
| Network and DNS | addressing, routing, diversity, encryption, capacity, failure |
| Identity/security | federation, native authorization, trust, keys, recovery |
| Data/integration | authority, consistency, sovereignty, async, reconciliation |
| Platform/delivery | portability tier, native value, artifacts, rollout |
| Operations | inventory, SLO, telemetry, incident, support, drift |
| Resilience | common mode, degraded/offline service, DR, failback, exit |
| Governance/economics | decision rights, TCO, egress, skills, lifecycle |
| Communication | clear trade-offs, roadmap, evidence, residual decision |

Score each 0–4. Maximum **36**; 31–36 is strong architect signal, 24–30 credible
with gaps, 17–23 needs deeper boundary/operating reasoning, and below 17 should
revisit the module.

Return to the [module overview](../28-hybrid-multicloud/index.md) after scoring.
