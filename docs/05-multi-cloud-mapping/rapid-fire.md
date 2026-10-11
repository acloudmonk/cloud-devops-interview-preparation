# Rapid-Fire Revision

[← Presentation](presentation-template.md) · [Next: Flashcards →](flashcards.md)

1. **What is the comparison unit?** A required capability and its semantics.
2. **Are mapped services equivalent?** Not until scope, behavior, limits, and operations are validated.
3. **AWS workload boundary?** Usually an account.
4. **Azure workload boundary?** Usually a subscription.
5. **GCP workload boundary?** Usually a project.
6. **AWS grouping?** Organizations and organizational units.
7. **Azure grouping?** Tenant and management groups.
8. **GCP grouping?** Organization and folders.
9. **Common guardrail principle?** Shared intent, native tested enforcement.
10. **Why federation?** Short-lived centralized identity lifecycle without static credentials.
11. **Workload identity rule?** Separate runtime identity and avoid exported secrets.
12. **Key-management risk?** Key availability and policy enter the workload RTO.
13. **Is a region comparable by name?** No; verify geography, services, and dependencies.
14. **Is a zone identical?** No; validate provider failure-domain definitions.
15. **AWS VPC scope?** Regional.
16. **Azure VNet scope?** Regional.
17. **GCP VPC scope?** Global, with regional subnets.
18. **Private circuit trio?** Direct Connect, ExpressRoute, Cloud Interconnect.
19. **Private service trio?** PrivateLink, Private Link, Private Service Connect patterns.
20. **Intercloud first question?** Which flows and business requirement justify it?
21. **VM trio?** EC2, Azure VMs, Compute Engine.
22. **Managed VM fleet trio?** ASG, VMSS, MIG.
23. **Kubernetes trio?** EKS, AKS, GKE.
24. **Function trio?** Lambda, Azure Functions, Cloud Run functions.
25. **Portable container means portable system?** No; identity, state, network, and ops differ.
26. **Object trio?** S3, Blob Storage, Cloud Storage.
27. **Block trio?** EBS, Managed Disks, Persistent Disk/Hyperdisk.
28. **Relational comparison start?** Engine, semantics, scale, HA, recovery, operations.
29. **Are NoSQL services interchangeable?** No; models and guarantees differ greatly.
30. **Data gravity?** Data size/location constrains placement and movement.
31. **Why avoid dual writes?** Partial failure creates divergence and ambiguity.
32. **Safer replication?** Authoritative transaction plus CDC/outbox and reconciliation.
33. **Queue mapping risk?** Delivery, ordering, visibility, rate, and replay differ.
34. **Exactly once end to end?** Still validate side effects and idempotency.
35. **IaC portability?** Common workflow, provider-specific resources and semantics.
36. **Module design?** Small interfaces plus explicit provider implementations.
37. **Artifact rule?** Promote signed immutable artifacts, not rebuild per environment.
38. **OpenTelemetry benefit?** Portable signal production and context.
39. **OpenTelemetry limitation?** It does not normalize all native audit and metrics.
40. **Central telemetry risk?** Cost, data exposure, and loss of visibility.
41. **Unified SLO?** Same user outcome, measured across provider components.
42. **Billing normalization?** Common dimensions plus retained native detail.
43. **Hidden multicloud cost?** Duplicated skills, tooling, controls, support, and exercises.
44. **Egress concern?** Cost plus bandwidth, latency, and dependency coupling.
45. **Commitment rule?** Rightsize and forecast before purchase.
46. **Quota rule?** Model provider/location/SKU limits including failover.
47. **Portability measure?** Time, data, skills, revalidation, readiness, feature loss.
48. **Single-cloud fit?** Simplicity meets requirements.
49. **Workload-per-cloud fit?** Portfolio placement without distributed hot paths.
50. **Distributed multicloud fit?** Components tolerate latency and provider failure.
51. **Redundant multicloud fit?** Tested recovery value exceeds duplication.
52. **Lowest-common-denominator risk?** Sacrifices native value without proven mobility.
53. **Placement criteria?** Value, regulation, data, latency, reliability, skills, cost.
54. **Recovery authority?** One defined writer/control owner during failover.
55. **Fencing?** Prevents obsolete site or writer from mutating state.
56. **Failback concern?** Reconciliation, authority, data transfer, and retesting.
57. **Central dashboard proof?** Insufficient without native control evidence.
58. **Mapping freshness?** Review dated and verified against current docs.
59. **Strong executive close?** Value, risks, roadmap, evidence, exit triggers.
60. **Answer loop?** Clarify, map, expose gap, place, fail, operate, verify.
