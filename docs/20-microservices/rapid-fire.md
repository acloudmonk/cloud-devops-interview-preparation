# Rapid-Fire Revision

[← Ten-minute architecture review](presentation-template.md) · [Next: Active-recall flashcards →](flashcards.md)

1. **What defines a microservice?** — A cohesive business capability with owned data, contracts, lifecycle, and team responsibility.
2. **Are microservices always better than a monolith?** — No; they add distributed cost and require a justified need for independence.
3. **What is a modular monolith?** — One deployable with explicit internal modules and controlled dependencies.
4. **What is a bounded context?** — A boundary within which a domain model and language have consistent meaning.
5. **What is high cohesion?** — Related rules and changes reside in the same boundary.
6. **What is loose coupling?** — A service can change without requiring coordinated consumer or data changes.
7. **Why not one service per noun?** — Domain behavior and invariants, not vocabulary or size, determine useful boundaries.
8. **What reveals an overly small service?** — Chattiness, cross-service transactions, lockstep releases, and shared ownership.
9. **What is a distributed monolith?** — Networked components that must change, deploy, and fail together.
10. **Who owns a service?** — A long-lived team owning code, contract, data, SLO, on-call, cost, and retirement.
11. **When choose synchronous communication?** — When an immediate result is necessary and dependency latency/availability are acceptable.
12. **When choose asynchronous communication?** — When completion can be deferred or temporal decoupling/buffering is valuable.
13. **Does async remove coupling?** — No; schema, ordering, timing, semantics, and business workflow remain contracts.
14. **Why avoid long synchronous chains?** — Latency and failure probability accumulate across every hop.
15. **What makes an event useful?** — It states a specific completed domain fact with identity, schema, owner, and time.
16. **What is tolerant reading?** — Consumers ignore unknown additive fields and depend only on their contract.
17. **Why use an API gateway?** — To provide stable external routing and cross-cutting edge controls, not domain authorization alone.
18. **What does service discovery solve?** — Mapping logical service identity to reachable healthy endpoints.
19. **Does a service mesh solve business resilience?** — No; it cannot decide safe retries, idempotency, or business fallback.
20. **What is database per service?** — Each service exclusively owns its logical data and exposes it through contracts.
21. **Must every service use a separate server?** — No; logical schema/credential ownership can exist on shared infrastructure.
22. **What is eventual consistency?** — Replicas or workflows converge after a bounded delay with defined failure handling.
23. **What is a saga?** — A sequence of local transactions with explicit progress and compensating business actions.
24. **Choreography versus orchestration?** — Events distribute coordination; an orchestrator makes workflow state explicit.
25. **Why is compensation not rollback?** — External effects occurred and may only be counteracted by another business action.
26. **What is a transactional outbox?** — Domain state and event intent commit atomically, then a relay publishes.
27. **Does outbox prevent duplicate delivery?** — No; consumers still need idempotency and ordering logic.
28. **What is a materialized view?** — A derived query model built from authoritative data/events.
29. **When use API composition?** — For bounded fan-out queries requiring fresher owner responses.
30. **What is business idempotency?** — Repeated intent with one key produces one logical outcome and retrievable result.
31. **Why is a timeout ambiguous?** — The remote side may have succeeded after the caller stopped waiting.
32. **What is a retry budget?** — A limit on extra attempts so retries cannot consume unsafe capacity.
33. **What is backpressure?** — Signaling or limiting intake when downstream capacity cannot keep up.
34. **Rate limiting versus load shedding?** — Rate limits enforce policy; shedding protects system recovery under overload.
35. **What is a bulkhead?** — Resource isolation that prevents one tenant/dependency/workload from exhausting all capacity.
36. **Why propagate deadlines?** — Downstream work should stop when the end-to-end result can no longer be useful.
37. **What is a cell architecture?** — Repeated bounded stacks that limit tenant or workload blast radius.
38. **What is workload identity?** — Short-lived service-specific credentials derived from runtime identity.
39. **Why authorize in each owning service?** — Only the owner understands object/action business rules and current state.
40. **What is contract testing?** — Automated verification that provider and consumer expectations remain compatible.
41. **Why are mocks insufficient?** — They omit serialization, network, identity, storage, and infrastructure semantics.
42. **What is expand/migrate/contract?** — Add compatible state, move use/data, then remove old state after evidence.
43. **Why can image rollback fail?** — Data schemas and emitted events may no longer support the previous version.
44. **What should traces propagate across messages?** — Correlation context and safe metadata, not secrets or full payloads.
45. **What is saga age?** — Time a distributed business workflow has remained incomplete.
46. **Why is a catalog operational?** — Incidents and changes require current owners, dependencies, SLOs, and runbooks.
47. **How are derived views recovered?** — Rebuild/replay from authority and verify freshness and business invariants.
48. **What is a strangler migration?** — Incrementally route a business capability to a new boundary and retire the old path.
49. **What should be extracted first?** — A capability with clear owner, boundary, pain/value, and manageable dependencies.
50. **What is the strongest microservices metric?** — Improved independent business change and reliability, not service count.
