# Rapid-Fire Revision

[← Module overview](index.md) · [Active-recall flashcards](flashcards.md)

Answer each in one or two sentences. Expand only when challenged.

1. **What is a Well-Architected review?** A structured, evidence-based conversation about workload decisions, risks, trade-offs, and improvements.
2. **Is it an audit?** No; specialist audit or assurance can use findings but has different authority and evidence standards.
3. **Is it a certification?** No; framework review completion does not certify or guarantee a workload.
4. **What is a workload?** Technology and operational components that together deliver a business outcome.
5. **Why not review an account?** An account is an administrative boundary and may contain several outcomes or only part of one workload.
6. **What should a review charter contain?** Purpose, scope, exclusions, trigger, participants, framework/lenses, evidence, schedule, and outputs.
7. **Who must participate?** Accountable product/workload owner plus architecture, engineering, operations, security, finance, and relevant specialists.
8. **What is the evidence ladder?** Claim → document/design → configuration → telemetry → controlled test → demonstrated representative behavior.
9. **Is missing evidence proof of missing control?** No; it is uncertainty requiring validation.
10. **Design intent versus current state?** What should exist versus what evidence shows exists and operates now.
11. **What are AWS’s six pillars?** Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, and Sustainability.
12. **How many Azure core pillars?** Five: Reliability, Security, Cost Optimization, Operational Excellence, and Performance Efficiency.
13. **How many current Google Cloud pillars?** Six, including sustainability plus operations, security/privacy/compliance, reliability, cost, and performance.
14. **What is an AWS lens?** Additional technology, industry, or organization-specific review guidance applied with the core framework.
15. **What is an AWS milestone?** An immutable snapshot of workload review state at a point in time.
16. **What does the AWS Well-Architected Tool provide?** Workload, lens, answer, improvement-item, and milestone recording for consistent reviews.
17. **What does a provider advisor know?** Configuration and telemetry in its supported scope—not full business context or application behavior.
18. **Can scores compare providers?** No; scopes, questions, semantics, evidence, and scoring differ.
19. **Can scores compare teams?** Rarely safely; they create gaming and ignore criticality and scope differences.
20. **What is an observation?** A factual condition supported by a source, scope, and date.
21. **What is a risk?** A credible uncertain event or condition and its potential business consequence.
22. **What is a recommendation?** A proposed outcome or option to change risk; it is not the decision itself.
23. **What is a decision?** An authorized choice to remediate, investigate, transfer, avoid, defer, or accept risk.
24. **What makes a good finding?** Condition, evidence, scenario, consequence, controls, uncertainty, priority, options, owner, and validation.
25. **Why separate observation and recommendation?** To prevent reviewer preference from being presented as proven risk.
26. **What affects prioritization?** Consequence, exposure, likelihood, controls, urgency, confidence, effort, dependency, and reversibility.
27. **Who accepts residual risk?** The authorized business or risk owner, not the facilitator by default.
28. **What belongs in an exception?** Scope, rationale, controls, residual risk, acceptor, expiry, and reassessment trigger.
29. **What is a cross-pillar trade-off?** A decision that improves one quality attribute while affecting others.
30. **Example reliability/cost tension?** Standby capacity improves recovery but increases ongoing spend and resource use.
31. **What is an ADR?** A record of context, drivers, options, decision, consequences, owner, and revisit triggers.
32. **Why record rejected options?** Future teams need to understand constraints and avoid repeating analysis.
33. **How do you handle conflicting evidence?** Preserve source, date, and scope; assign validation rather than forcing premature agreement.
34. **How do you challenge safely?** Ask which requirement drove the choice and what evidence shows the intended outcome.
35. **What if serious active exposure appears?** Stop normal review flow and use the incident/security escalation process.
36. **Why split large reviews?** Focus and evidence quality decline in long questionnaire sessions.
37. **What is a parking lot?** A recorded follow-up topic kept from derailing the current review scope.
38. **What should the executive report contain?** Context, confidence, top risks, choices, roadmap, owners, residual risk, and decisions needed.
39. **What should engineers receive?** Detailed evidence, failure/trust context, options, dependencies, and validation criteria.
40. **When does a finding close?** When evidence proves target risk reduction or authorized acceptance, with records updated.
41. **Is ticket closure evidence?** No; validate workload outcome and cross-pillar consequences.
42. **What triggers re-review?** Major design, incident, threat, demand, regulation, SLO, provider, dependency, or exception change.
43. **What belongs in continuous review?** Lightweight change checks, automated facts, outcome tests, milestones, and periodic deep review.
44. **What is portfolio governance?** Workload inventory and aggregated risks/actions used to improve shared platforms, standards, and funding.
45. **Why aggregate recurring findings?** Repeated gaps often indicate a platform, policy, skill, ownership, or incentive problem.
46. **What can evidence automation do?** Collect scoped, timestamped deterministic facts and policy differences.
47. **What can automation not decide?** Business impact, applicability, trade-off, risk appetite, and accountable acceptance.
48. **How should framework changes be handled?** Assess whether the changed guidance alters current workload risk; do not reopen mechanically.
49. **What measures review value?** Validated risk reduction and workload outcomes, not review count or answer completion.
50. **Best closing interview point?** State context, evidence confidence, top risk, trade-off, owner, action, validation, and residual decision.

Return to the [module overview](index.md) when ready to continue.
