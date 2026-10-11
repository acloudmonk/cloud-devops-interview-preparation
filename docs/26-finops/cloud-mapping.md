# AWS-First Multi-Cloud and Sustainability

[← Module overview](index.md) · [Governance and practice](governance-operating-model.md)

Map FinOps capabilities and commercial semantics, not similarly named tools. Cloud
providers differ in hierarchy, billing relationships, discounts, data schemas,
allocation, recommendations, carbon data, and contract treatment.

## Capability orientation

| Intent | AWS | Azure | Google Cloud |
| --- | --- | --- | --- |
| Interactive analysis | Cost Explorer | Cost Management cost analysis | Cloud Billing reports |
| Detailed export | Data Exports / CUR 2.0 | Cost Management exports | Billing export to BigQuery |
| Budget alerts | AWS Budgets | Cost Management budgets | Cloud Billing budgets and alerts |
| Anomaly detection | Cost Anomaly Detection | Cost anomaly alerts | Cost Anomaly Detection |
| Business grouping | Cost Categories, tags, accounts | scopes, tags, cost allocation rules | hierarchy, projects, labels |
| Recommendations | Cost Optimization Hub, Trusted Advisor | Azure Advisor | FinOps hub and recommender capabilities |
| Commitments | Savings Plans, reservations | savings plan, reservations, Hybrid Benefit | committed use discounts and service-specific constructs |
| Carbon information | Customer Carbon Footprint Tool / Data Exports | Azure Carbon Optimization | Carbon Footprint |

This table is orientation only. Validate feature availability, data timing,
commercial eligibility, contract, currency, support, and sharing behavior.

## Normalization and FOCUS

The FinOps Open Cost and Usage Specification (FOCUS) provides a common billing-data
schema that can reduce cross-provider normalization effort. It does not make service
semantics, prices, discounts, resource identities, or allocation rules equivalent.
Preserve provider-specific fields required for reconciliation and optimization.

## Sustainability relationship

Energy and carbon do not map perfectly to currency. Efficiency actions such as
removing idle capacity, improving utilization, appropriate storage lifecycle, and
reducing unnecessary data movement may benefit both. Region, hardware, time, and
managed-service choices can trade carbon, cost, latency, resilience, sovereignty,
and migration effort. Report these dimensions rather than claiming automatic alignment.

## Multi-cloud economics

Include connectivity and egress, duplicated security/observability, identity,
skills, support, commitments, data gravity, operational complexity, resilience,
and exit cost. A lower provider unit price can increase total cost if it fragments
operations or misses existing commitments. Conversely, concentration risk and
business leverage may justify deliberate duplication.

## Interview guidance

Explain the AWS operating design in depth, then map its outcomes to Azure and
Google Cloud. State where data and discount semantics must be reconciled, how unit
economics span providers, who owns commitments, and which trade-offs remain.

Return to the [module overview](index.md) when ready to continue.
