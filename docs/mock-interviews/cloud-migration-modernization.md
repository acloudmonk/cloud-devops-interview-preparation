# Cloud Migration and Modernization Mock Interview

[← Mock interview overview](index.md) · [Module 24 overview](../24-migration-modernization/index.md)

Duration: **50 minutes**
Level: **Senior / Architect**
Primary context: **AWS-first regulated enterprise with multi-cloud dependencies**

## Candidate brief

A regulated global enterprise must exit two data centers within 18 months. Its 600
applications include VMware, physical hosts, mainframe integration, commercial
products, custom Java/.NET, databases, and end-of-life technology. Inventory and
ownership are incomplete. AWS is the primary target, acquisitions use Azure, analytics
uses Google Cloud, and PCI/PII/residency constraints apply. Design the program and
transition—not merely the final platform.

## Interview structure

### 0–8 minutes — Outcomes and discovery

Clarify forcing event, business outcomes, definition of done, scope, criticality,
deadlines, change calendars, owners, data/control constraints, RTO/RPO, baseline cost,
skills, contracts, and risk appetite. Explain inventory, confidence, and dependency
discovery.

### 8–18 minutes — Portfolio and target decisions

Define workload boundaries, segmentation, seven-R criteria, target and transition
states, business case, assumptions, decision rights, and re-evaluation triggers. Show
how AWS-first placement coexists with justified Azure, Google Cloud, and retained
systems.

### 18–28 minutes — Foundation, waves, and factory

Prove landing-zone readiness across identity, network, security, delivery, logging,
recovery, cost, quotas, and operations. Select a representative first wave, form later
dependency groups, and explain gates, factory flow, governance, and useful metrics.

### 28–38 minutes — Cutover and failure branches

Choose three:

- a hidden license-server dependency appears three days before cutover;
- database replication lag exceeds the rollback window;
- DNS switches only part of the user population;
- security blocks temporary vendor administration;
- performance passes but month-end batch misses its deadline;
- new target writes make rollback unsafe;
- target cloud spend and legacy cost overlap indefinitely;
- a quota blocks production deployment.

### 38–45 minutes — Acceptance and modernization

Cover functional/data/performance/security/resilience evidence, operational acceptance,
hypercare, control mapping, records, decommissioning, unit economics, skill/operating
model, and evidence-based modernization sequencing.

### 45–50 minutes — Executive close

State the recommended first decision and wave, top risks and assumptions, cutover
authority, measurable outcomes, closure criteria, and evidence that would cause a
change of direction.

## Scoring rubric

| Dimension | Points |
| --- | ---: |
| Outcomes, discovery, dependencies, and business case | 9 |
| Dispositions, target/transition design, and multi-cloud judgment | 8 |
| Landing zone, waves, factory flow, governance, and ownership | 9 |
| Data movement, cutover, rollback, integrity, and failure handling | 9 |
| Security, validation, operations, and recovery evidence | 8 |
| Modernization, decommissioning, economics, and value | 5 |
| Trade-offs and executive communication | 2 |
| **Total** | **50** |

Interpretation: **43–50** architect-ready; **35–42** strong with targeted gaps;
**25–34** incomplete transition or operating reasoning; **below 25** rebuild from
outcomes, dependencies, authority, and evidence. A service list without cutover,
rollback, acceptance, and closure cannot exceed 34.

## Improvement loop

Record the three weakest decisions, revisit the matching module pages and primary
sources, redraw the transition and authority boundaries, then repeat within seven days
using different failure branches.
