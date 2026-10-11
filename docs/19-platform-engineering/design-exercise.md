# Enterprise Platform Engineering Design Exercise

[← Adoption, metrics, and economics](adoption-metrics-economics.md) · [Next: Scenario questions →](scenarios.md)

## Brief

Two hundred developers across 35 teams operate 80 services. Environment delivery
takes ten days, CI pipelines are copied, static AWS keys remain common, change
failure rate is 22%, and ownership is incomplete. Teams use EKS, ECS, Lambda, and
managed data services. Leadership asks for an internal developer platform in six
months while Azure and Google Cloud teams want reusable control principles.

## Constraints

- regulated and standard workloads require different isolation and evidence;
- the platform team begins with eight people and cannot rewrite every pipeline;
- product teams retain application SLO and on-call responsibility;
- production changes need traceable provenance and short-lived identity;
- current delivery must continue throughout migration;
- business expects measurable lead-time and reliability improvement.

## Candidate design

Start with service creation and safe deployment for one common workload archetype.
Use federated identity and AWS multi-account foundations. Expose versioned platform
APIs through CLI, Git declarations, and a portal such as Backstage. Templates create
ownership metadata, repository, reusable pipeline, IaC, workload identity, telemetry,
SLO skeleton, and cost tags. Durable workflows orchestrate provisioning while IaC
or scoped reconcilers own resource state.

Build once in isolated runners, produce SBOM/provenance, sign immutable artifacts,
and promote them through policy-controlled environments. Keep deployment authority
outside pull-request code. Scope platform controllers by environment/cell, record
intent and result, and provide status, retry, cancellation, recovery, and deletion.
Product teams own code, tests, data compatibility, rollout health, and operations.

## Rollout and measures

Baseline environment and deployment lead time, change failure, recovery time,
support tickets, task completion, satisfaction, and platform cost per active team.
Pilot three willing teams, canary platform versions, then migrate by archetype.
Provide office hours and governed escape hatches. Retire old paths only after
supported migration and evidence that outcomes improve.

## Scored deliverable (50 points)

| Area | Points | Strong evidence |
| --- | ---: | --- |
| Discovery and product outcome | 7 | Personas, journeys, baseline, non-goals, roadmap |
| Architecture and contracts | 9 | Layers, APIs, state ownership, interfaces, lifecycle |
| Security and tenancy | 8 | identities, isolation, policy, evidence, escape path |
| Delivery and supply chain | 7 | build trust, provenance, promotion, safe data change |
| Reliability and operations | 7 | SLO, failure modes, support, upgrade, recovery |
| Adoption and organization | 7 | ownership, pilot, migration, feedback, deprecation |
| Economics and multi-cloud | 5 | unit value, capacity, capability translation, trade-offs |

Score 40+ only when the proposal is an operable product, not a diagram of tools.
