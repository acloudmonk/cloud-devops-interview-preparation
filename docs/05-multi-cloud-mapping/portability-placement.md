# Portability, Interoperability, and Placement

[← Cost and commercial](cost-commercial.md) · [Next: Capability matrices →](capability-matrices.md)

## Portability layers

| Layer | More portable choice | Remaining provider coupling |
| --- | --- | --- |
| Application | open protocols, containers | identity, network, runtime limits |
| Orchestration | Kubernetes | cluster integrations, storage, load balancing |
| Infrastructure | Terraform/OpenTofu | provider resources and state semantics |
| Telemetry | OpenTelemetry | native metrics, audit, backend queries |
| Data | open formats/protocols | consistency, replication, managed operations |

Portability is a spectrum. Measure time, data, skills, security revalidation, operational
readiness, and feature loss required to move—not whether source code compiles elsewhere.

## Placement scorecard

Score business differentiation, regulatory fit, data gravity, latency, reliability,
service maturity, skills, operational burden, commercial terms, exit cost, and
integration complexity. Weight criteria with stakeholders and record uncertainty.

Use one cloud when simplicity wins; workload-per-cloud for portfolio optimization;
portable platforms when mobility has demonstrated value; distributed multicloud only
when components can tolerate network and provider failure; redundant multicloud only
when tested recovery value exceeds duplication.

Avoid provider abstraction that erases useful differentiation. Standardize outcomes and
interfaces, retain native controls, and define exit triggers before sunk cost dominates.
