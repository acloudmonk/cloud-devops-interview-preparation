# Zero Trust Architecture Mock Interview

[← Mock interview overview](index.md) ·
[Module 16 overview](../16-zero-trust/index.md) ·
[Scenario answer framework](../interview-playbook/scenario-answer-framework.md)

Duration: **50 minutes**

Level: **Senior / Architect**

Primary context: **AWS-first hybrid enterprise with Azure and Google Cloud follow-ups**

## Candidate brief

A regulated enterprise with 18,000 employees and contractors uses broad VPN
access, standing cloud administrator roles, shared workload credentials, flat
application networks, and inconsistent access evidence. AWS hosts most workloads;
Azure supports workforce services and GCP supports analytics. Design a phased
Zero Trust architecture after a stolen session enabled lateral movement.

## Interview structure

### 0–5 minutes — Discovery

Ask about critical transactions, data, users, workloads, devices, existing
identity, flows, protocols, administrators, incidents, constraints, ownership,
availability, privacy, and recovery.

### 5–15 minutes — Decision architecture

Define protect surfaces and implicit trust. Draw subjects, identity/posture/data
signals, policy information and decision points, enforcement, telemetry, expiry,
revocation, and responsibility. Trace one human and one workload request.

### 15–25 minutes — Target controls

Cover identity lifecycle, phishing-resistant authentication, sessions, governed
privilege, RBAC/ABAC, workload federation, service authorization, segmentation,
application access, data/resource policy, credentials, certificates, and evidence.

### 25–35 minutes — Incident branches

Choose two:

1. The enterprise IdP signing key might be compromised.
2. A valid administrator session is replayed from an attacker-controlled device.
3. EKS workloads use a broad node role after pod identity fails.
4. An ABAC error permits cross-tenant data access.
5. The identity proxy and device-posture provider fail during an incident.

Contain, preserve evidence, identify blast radius, maintain essential access,
recover trust, communicate, and prevent recurrence.

### 35–42 minutes — Trade-offs and multi-cloud

Discuss fail-open versus fail-closed, central versus local policy, privacy versus
device context, mesh versus application authorization, token lifetime versus
availability, and common outcomes with native AWS, Azure, and Google Cloud controls.

### 42–47 minutes — Executive recommendation

Summarize the business risk, bounded first protect surface, target state,
migration waves, ownership, investment, residual risk, and success measures in
two minutes.

### 47–50 minutes — Candidate questions

Ask about incidents, business-critical recovery, identity authority, resource
ownership, regulatory/privacy constraints, user experience, or first measurable
outcome.

## Scoring rubric

| Dimension | Expected evidence |
| --- | --- |
| Discovery and scope | resources, transactions, subjects, flows, threats, constraints |
| Decision model | signals, policy, enforcement, expiry, revocation, evidence |
| Workforce identity | lifecycle, assurance, session, privilege, contractor, recovery |
| Workload identity | issuance, federation, audience, authorization, rotation |
| Segmentation and data | paths, application access, lateral movement, resource policy |
| Reliability and response | dependency failure, containment, break-glass, recovery |
| Cloud translation | AWS depth with accurate Azure and Google Cloud outcomes |
| Migration and ownership | phased rollout, legacy coexistence, owners, exceptions |
| Measures and communication | risk and usability outcomes, structure, trade-offs |

Score each 0–4. Maximum: **36**. Scores of 31–36 show strong architect signal;
24–30 are credible with gaps; 17–23 need deeper decision and failure reasoning;
below 17 should revisit the concepts and scenarios.

Return to the [module overview](../16-zero-trust/index.md) after scoring.
