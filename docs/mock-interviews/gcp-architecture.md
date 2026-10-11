# Timed GCP Architecture Mock Interview

[← GCP module](../04-gcp/index.md)

Time: **50 minutes** · Score: **50 points** · Target: **40+**

## Candidate brief

Design a regulated global order and media platform on Google Cloud. It has three
acquired teams, 10× campaign spikes, private partner connectivity, EU residency,
event-fed analytics, RTO 60 minutes/RPO 5 minutes, and a small platform team.

## Interview sequence

| Time | Prompt | Points |
| --- | --- | ---: |
| 0–5 | Clarify journeys, scale, data, SLO, constraints, assumptions | 5 |
| 5–12 | Organization, folders, projects, billing, ownership, governance | 7 |
| 12–20 | Identity, network, DNS, ingress, egress, private/hybrid paths | 8 |
| 20–28 | Runtime, data, integration, analytics; compare alternatives | 8 |
| 28–36 | Zone/region loss, corruption, recovery, quota, degradation | 8 |
| 36–42 | Security, delivery, observability, incident operations | 6 |
| 42–47 | Cost, capacity, sustainability, unit economics | 3 |
| 47–50 | Risks, evidence, decision record, exit triggers | 5 |

## Mandatory follow-ups

1. Cloud Run exhausts Cloud SQL connections during a campaign.
2. Organization Policy blocks the documented recovery region.
3. Pub/Sub backlog grows while consumer CPU remains low.
4. Restored records are consistent but completed-order totals differ.

## Scoring anchors

- **0:** omitted or unsafe.
- **1:** names a concept without applying it.
- **2:** makes a coherent choice.
- **3:** explains failure, operations, evidence, and trade-offs.

Use the table points as maxima. A response that ignores identity compromise or data
integrity cannot pass. After scoring, record three weak areas, revisit their primary
references, answer the related scenarios aloud, and repeat with changed constraints.
