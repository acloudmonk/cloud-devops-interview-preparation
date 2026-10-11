# Rapid-Fire Revision

[← Ten-minute platform review](presentation-template.md) · [Next: Active-recall flashcards →](flashcards.md)

Answer each in one or two sentences before revealing the text after the dash.

1. **What is platform engineering?** — Product-oriented delivery of reusable internal capabilities that reduce cognitive load and improve safe flow.
2. **Who is the platform customer?** — Internal teams performing defined engineering journeys, not an abstract “developer” persona.
3. **What is an IDP?** — The integrated platform of interfaces, workflows, controls, automation, and services supporting delivery and operation.
4. **Is a developer portal the platform?** — No; it is one discovery and interaction surface over platform capabilities.
5. **What is a golden path?** — A supported, opinionated, self-service path for a common workload or journey.
6. **Should golden paths be mandatory?** — Usually value-led defaults with governed exceptions; mandatory controls should be explicit and narrow.
7. **What is cognitive load?** — Mental effort required to understand and operate systems beyond a team's core domain.
8. **When is a platform justified?** — When repeated high-value or high-risk problems can be solved better through a reusable owned capability.
9. **What is a thin viable platform?** — The smallest end-to-end platform slice that solves a meaningful customer journey.
10. **Why not start with a portal?** — A polished interface cannot repair missing APIs, manual workflows, unclear ownership, or unsafe authority.
11. **What does platform-as-product change?** — It introduces discovery, roadmap, customers, support, lifecycle, outcomes, and feedback.
12. **What remains with product teams?** — Application behavior, data, service SLO, tests, rollout health, and business outcomes.
13. **What should the platform own?** — Shared contracts, automation, controls, reliability, documentation, support, and lifecycle.
14. **What is an enabling team?** — Specialists who help teams adopt capabilities and build skill without permanently taking ownership.
15. **What is a platform contract?** — Versioned interface, behavior, guarantees, limits, ownership, support, and lifecycle promises.
16. **What is a control plane?** — A system that validates and reconciles desired state toward actual state.
17. **Why use reconciliation?** — It can converge after partial failure and detect drift across a resource lifecycle.
18. **Why is CI alone not always a control plane?** — A job may end while resources, drift, retries, and deletion continue.
19. **What makes self-service complete?** — Request, policy, execution, status, failure recovery, update, ownership, and deletion.
20. **Why return an operation ID?** — Long-running work needs durable status and safe retry after client timeout.
21. **What is idempotency?** — Repeating an operation with the same intent does not create unintended duplicate effects.
22. **Why separate portal and platform APIs?** — Interfaces remain replaceable and privileged lifecycle logic stays in owned services.
23. **What is “start right”?** — New workloads begin with approved structure, controls, ownership, and evidence.
24. **What is “stay right”?** — Versions, policy, dependencies, ownership, and posture remain maintained after creation.
25. **Why can copied templates drift?** — Consumers own snapshots that do not automatically receive corrections and upgrades.
26. **What should an escape hatch contain?** — Risk owner, minimum controls, support boundary, expiry, and re-entry or retirement plan.
27. **Why are platform plugins risky?** — They expand supply chain, compatibility, identity, and ownership surfaces.
28. **Where should production credentials live?** — Outside user-controlled build steps, issued as short-lived scoped identities.
29. **Why promote artifacts?** — Reusing one verified immutable artifact preserves provenance across environments.
30. **What is a platform evidence layer?** — Inventory, ownership, delivery, policy, posture, SLO, usage, cost, and feedback records.
31. **How should policy be introduced?** — Test, shadow, canary, enforce, observe false positives, and provide remediation/exception paths.
32. **What determines tenancy boundaries?** — Threat, compliance, failure, noisy-neighbor, performance, and cost requirements.
33. **Why partition controllers?** — Scoped cells reduce credential reach and common-mode blast radius.
34. **What is failure demand?** — Support or rework created because the platform journey failed or was unclear.
35. **What is a platform journey SLI?** — A measure of a user outcome such as successful environment request latency.
36. **Should portal uptime equal platform uptime?** — No; interfaces and control/runtime paths have distinct criticality and degradation.
37. **What is a platform canary?** — Controlled release to representative consumers before broad rollout.
38. **Why inventory consumers?** — Compatibility, vulnerability, communication, migration, and deprecation require knowing impact.
39. **What is nominal adoption?** — Enrollment or logins without successful use or outcome improvement.
40. **What adoption measure matters?** — Repeat successful journey use with improved flow, quality, and experience.
41. **Why not mandate 100% adoption?** — Unsupported needs and bypass can hide behind the number and increase risk.
42. **What are vanity platform metrics?** — Logins, templates, code, tickets closed, or resources without outcome context.
43. **Which metric categories should balance?** — Flow, quality/reliability, experience, adoption, economics, and business value.
44. **What is cost per active team?** — Total platform cost divided by teams receiving measurable ongoing value.
45. **Why can chargeback harm adoption?** — Poor allocation or pricing can reward duplicated unsafe alternatives.
46. **What should multi-cloud standardize?** — Outcomes, identity principles, metadata, evidence, and lifecycle contracts where valuable.
47. **What should remain cloud-native?** — Capabilities whose provider-specific value exceeds portability benefit and is explicitly accepted.
48. **How should old paths retire?** — Inventory, migration support, evidence of success, deadlines, exceptions, and ownership.
49. **When should a platform feature be stopped?** — When evidence shows weak customer value relative to lifecycle and opportunity cost.
50. **What is the architect's platform test?** — Can teams safely complete and operate a valuable journey without opening a specialist ticket?
