# Enterprise Zero Trust Design Exercise

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

This is a paper exercise. Access reasoning, control boundaries, failure modes,
migration, and evidence matter more than vendor names.

## Scenario

A regulated enterprise has 18,000 employees and contractors, an on-premises
directory, broad VPN access, standing administrator roles, shared service
credentials, and flat application networks. AWS hosts most new workloads across
120 accounts; Azure supports workforce services and GCP supports analytics.
Several internal applications cannot federate. A stolen VPN session recently
enabled lateral movement and sensitive-data access.

## Deliverables

1. **Discovery:** crown-jewel resources, business transactions, data, identities,
   devices, workloads, flows, owners, dependencies, incidents, and constraints.
2. **Threat model:** stolen credentials/sessions, device compromise, privilege
   escalation, lateral movement, policy bypass, issuer compromise, and insider use.
3. **Decision model:** signals, policy information/decision/enforcement points,
   session lifetime, logging, and revocation for three critical transactions.
4. **Workforce architecture:** proofing, IdP, phishing-resistant authentication,
   federation, lifecycle, contractors, privileged elevation, and recovery.
5. **Workload architecture:** platform identity, federation, token audience,
   authorization, rotation, service calls, and legacy-secret transition.
6. **Access architecture:** application access, administrative sessions,
   segmentation, resource/data policy, egress, and alternate-path analysis.
7. **Reliability:** IdP, DNS, certificate, proxy, posture, and policy outages;
   degraded modes; emergency access; rollback; regional recovery.
8. **Multi-cloud translation:** common outcomes with provider-specific controls,
   authority, logs, and exception handling.
9. **Migration:** bounded pilot, coexistence, observe/warn/enforce phases, legacy
   adapters, user support, owners, exception expiry, and VPN retirement criteria.
10. **Measures:** exposure, privilege, credential age, decision quality,
    containment, control availability, friction, and business task success.

## Decision worksheets

| Transaction | Subject | Resource/action | Required signals | Enforcement | Expiry/revoke |
| --- | --- | --- | --- | --- | --- |
| Example: engineer views production logs | federated engineer | read scoped log group | strong auth, managed device, approved on-call role | identity-aware entry plus cloud IAM | one-hour session; revoke on role/posture change |

| Dependency failure | Default behavior | Reduced capability | Emergency path | Decision owner |
| --- | --- | --- | --- | --- |
| Example: device posture unavailable | deny privileged changes | read-only from recently verified device | monitored brokered session | production risk owner |

## Review rubric

Score 0–4 for discovery, threat reasoning, workforce identity, workload identity,
authorization, segmentation/data protection, operational resilience, cloud
translation, migration/measures, and executive communication. A strong answer
removes specific implicit trust, preserves recoverability, and avoids promising
that a single proxy, mesh, or identity provider delivers Zero Trust.

Return to the [module overview](index.md) when ready to continue.
