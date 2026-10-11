# Observability, Operations, and Incident Response

[← Delivery and IaC](delivery-iac.md) · [Next: Cost and commercial →](cost-commercial.md)

| Capability | AWS | Azure | Google Cloud |
| --- | --- | --- | --- |
| Native telemetry | CloudWatch/X-Ray | Azure Monitor/Application Insights | Cloud Monitoring/Logging/Trace |
| Audit | CloudTrail | Azure Activity/Entra/resource logs | Cloud Audit Logs |
| Service health | AWS Health | Azure Service Health | Personalized Service Health |

Unify service names, owners, environments, trace context, SLI definitions, incident
severity, and retention intent. Preserve native resource identifiers, audit evidence,
and provider consoles for diagnosis. OpenTelemetry improves signal portability but does
not normalize every provider metric or control-plane event.

Define who detects, declares, coordinates, accesses each provider, contacts support,
stabilizes, communicates, and validates recovery. Test identity-provider outage,
expired federation, telemetry pipeline failure, regional events, quota, carrier loss,
and provider-status ambiguity.

Central tools are dependencies: buffer telemetry, protect sensitive fields, monitor
ingestion gaps, govern egress and cardinality cost, and retain a native diagnostic path.
Measure user journeys and business completion across boundaries, not three disconnected
green dashboards.
