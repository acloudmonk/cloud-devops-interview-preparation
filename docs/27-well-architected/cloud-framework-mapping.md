# Azure and Google Cloud Framework Mapping

[← Module overview](index.md) · [AWS framework](aws-framework.md)

All three frameworks pursue durable business outcomes through architecture and
operations, but their organization, terminology, assessments, workload guidance,
and provider recommendations differ. Map intent first and confirm current guidance.

## Current pillar orientation

| Quality area | AWS | Azure | Google Cloud |
| --- | --- | --- | --- |
| Operations | Operational Excellence | Operational Excellence | Operational excellence |
| Security | Security | Security | Security, privacy, and compliance |
| Reliability | Reliability | Reliability | Reliability |
| Performance | Performance Efficiency | Performance Efficiency | Performance optimization |
| Cost | Cost Optimization | Cost Optimization | Cost optimization |
| Sustainability | Sustainability pillar | Workload guidance and sustainability resources | Sustainability pillar |

AWS and Google Cloud currently expose six pillars. Azure’s core framework uses five
pillars and provides sustainability through additional workload and service guidance.
Do not invent a sixth Azure pillar merely to make a symmetric table.

## Framework layers and tools

- **AWS:** core framework, pillar questions, official/custom lenses, workload records,
  improvement items, and milestones in the AWS Well-Architected Tool.
- **Azure:** five pillars, design principles/checklists, workload guidance, service
  guides, design guides, and the Azure Well-Architected Review assessment.
- **Google Cloud:** six pillars with principles/recommendations plus cross-pillar
  perspectives such as AI/ML and financial services, supported by Architecture Center guidance.

Provider advisory services may supply configuration recommendations, but telemetry
cannot determine business criticality, acceptable trade-offs, organizational
capability, or every application-level failure. Combine tool evidence with people,
tests, incidents, and business context.

## Cross-cloud review method

Use one workload context and common quality objectives. Review shared journeys,
identity, network, data, delivery, observability, recovery, cost, and governance;
then apply each provider’s framework to provider-specific controls. Consolidate
duplicate risks while retaining the source, environment, provider, and remediation owner.

## Translation traps

- assuming similarly named services have identical scope or responsibility;
- applying a provider score as an enterprise maturity measure;
- treating multi-cloud duplication as independent resilience without common-mode analysis;
- losing provider-specific evidence during normalization;
- comparing pillars by name while ignoring different recommendations and workload classes;
- forcing one provider’s best practice where a platform-independent pattern is better.

## Interview guidance

Lead with workload outcome, quality targets, and failure/trust boundaries. Use the
AWS framework for depth, then state how Azure and Google Cloud organize equivalent
concerns and where their guidance or tooling must be verified. Avoid reciting pillar lists.

Return to the [module overview](index.md) when ready to continue.
