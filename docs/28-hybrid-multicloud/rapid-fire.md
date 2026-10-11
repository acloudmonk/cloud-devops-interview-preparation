# Rapid-Fire Revision

[← Module overview](index.md) · [Flashcards](flashcards.md)

1. **Hybrid cloud?** Public cloud combined with private, hosted, on-premises, or edge environments.
2. **Multi-cloud?** Deliberate use of more than one public-cloud provider.
3. **Does SaaS imply multi-cloud architecture?** Not necessarily; it can be an external dependency.
4. **First design question?** Which durable business driver requires each environment?
5. **Portfolio multi-cloud?** Different workloads placed on different providers.
6. **Distributed application multi-cloud?** One workload has components across providers; it carries stronger coupling risk.
7. **Tiered hybrid?** Application tiers run in different environments.
8. **Environment hybrid?** Lifecycle environments such as development and production run in different locations.
9. **Partitioned multi-cloud?** Users, geographies, workloads, or capabilities are assigned to different providers.
10. **Cloud bursting?** Temporary external capacity supplements a constrained primary environment.
11. **Placement criteria?** Outcome, latency, data, sovereignty, capability, dependency, skills, risk, cost, and exit.
12. **Why prefer asynchronous boundaries?** They reduce latency coupling and allow buffering, replay, and independent recovery.
13. **Connectivity options?** Public TLS, VPN, private interconnect, carrier exchange, SD-WAN, or provider cross-cloud products.
14. **Private link means trusted?** No; authenticate, authorize, encrypt, inspect, and log according to risk.
15. **Route diversity?** Independent devices, connections, locations, carriers, and control paths where required.
16. **CIDR overlap response?** Strategic re-addressing or controlled translation/proxy as transition debt.
17. **BGP risk?** Leaks, default propagation, asymmetric paths, loops, and unstable preference.
18. **DNS design needs?** Authority, private zones, delegation, forwarding, split horizon, caching, ownership, and failure tests.
19. **Why TTL is not failover control?** Resolver/client caching and connection behavior vary.
20. **Workforce federation?** Central authentication with provider-native least-privilege authorization.
21. **Workload federation?** Short-lived, audience-scoped service identity instead of shared long-lived keys.
22. **Identity resilience?** Provider-local constrained emergency access and tested federation recovery.
23. **Data gravity?** Large/stateful data attracts compute and makes movement slow or expensive.
24. **Data authority?** The defined source allowed to decide or mutate a domain’s state.
25. **Replication is consistency?** No; replication mode, lag, ordering, conflicts, and application semantics matter.
26. **Sovereignty versus residency?** Sovereignty can include administration, keys, metadata, support, and legal control beyond location.
27. **Portability spectrum?** Source, artifact, infrastructure, runtime, data, operations, and organizational capability.
28. **Kubernetes portability limit?** It does not normalize IAM, data, network, storage, managed services, or operations.
29. **Good abstraction?** Stable business/platform interface with provider-specific implementation behind ownership.
30. **Lowest-common-denominator risk?** Losing provider value while still paying multi-provider complexity.
31. **Portable artifact?** Reproducible, signed package with explicit architecture/runtime dependencies.
32. **Portability evidence?** Timed deployment, data movement, traffic, rollback, and operator exercise on target.
33. **One service operating model?** Shared ownership, SLO, incident, inventory, lifecycle, and evidence across providers.
34. **Single pane risk?** Central tooling can become a common-mode blind spot or control failure.
35. **Telemetry standardization?** Common semantics and OpenTelemetry where useful, plus retained native detail.
36. **Cross-cloud incident command?** One commander with provider leads, shared facts/timeline, and vendor liaisons.
37. **Common-mode failures?** Identity, DNS, CI/CD, code, carrier, SaaS, data, and human operations.
38. **Provider diversity equals DR?** No; complete independent data, identity, capacity, traffic, and operating paths must be proven.
39. **Safe disconnected edge?** Local identity/policy/data, bounded operation, queues, and reconciliation.
40. **Multi-writer requirement?** Ownership, conflict policy, fencing, idempotency, reconciliation, and failback.
41. **DR versus provider exit?** Shorter disruption recovery versus strategic platform replacement and contract/data closure.
42. **Full TCO?** Services, network/egress, licenses, support, duplication, people, migration, testing, and retirement.
43. **Why egress matters?** Architectural coupling becomes recurring cost and can constrain movement/recovery.
44. **Governance principle?** Common outcome and evidence, provider-native implementation.
45. **Who needs every-cloud depth?** Provider/platform specialists; product teams need bounded interfaces and failure knowledge.
46. **Useful measure?** Business SLO, recovery, drift, unit cost, egress, skill coverage, and tested exit.
47. **Useless goal?** Provider count or portability percentage without business outcome.
48. **When simplify?** When transition ends or the original driver no longer justifies duplication.
49. **Strong multi-cloud recommendation?** Placement and pattern plus boundaries, operations, economics, evidence, and exit trigger.
50. **Best closing point?** Multi-cloud is justified only when measured business value exceeds lifecycle complexity and risk.

Return to the [module overview](index.md) when ready to continue.
