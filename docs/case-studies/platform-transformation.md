# Case 3: Platform and Delivery Transformation

[← Regulated SaaS](regulated-saas.md) · [Next: Hybrid modernization →](hybrid-modernization.md)

## Brief

Two hundred developers run 80 services across manually managed Kubernetes clusters.
Teams copy CI pipelines, hold static cloud keys, and wait ten days for environments.
Change failure rate is 22%, ownership is unclear, and security proposes a central
approval board. Leadership wants an internal developer platform in six months.

## Discovery prompts

- Which developer journeys cause the most delay or incidents?
- What should product teams own versus the platform, security, and SRE teams?
- Which workload classes, compliance tiers, and cluster boundaries exist?
- What adoption, reliability, delivery, and satisfaction baselines are available?
- Is the constraint technology, cognitive load, policy, funding, or operating model?

## Candidate tasks

1. Define platform-as-product outcomes, personas, golden paths, and non-goals.
2. Design source-to-production flow, workload identity, artifacts, policy, and evidence.
3. Decide cluster/tenant boundaries and the roles of IaC, GitOps, and service catalog.
4. Create SLOs, support, upgrade, exception, deprecation, and funding models.
5. Plan adoption without a forced big-bang migration or central bottleneck.

## Failure injects

- A compromised build runner publishes a signed malicious image.
- A GitOps controller receives organization-wide administrator permissions.
- Platform upgrades break an API used by 30 services.
- Teams bypass the paved road because onboarding still takes four days.
- The central platform becomes a Sev-1 dependency with no defined SLO.

## Model direction

Start with two high-friction journeys and define measurable product outcomes such as
time to first safe deployment and change failure rate. Provide reusable templates,
ephemeral workload identity, isolated runners, immutable artifacts, provenance,
policy feedback, progressive delivery, observability, and ownership metadata. Keep
credentials and production mutation outside untrusted build code.

Treat platform APIs and templates as versioned products with compatibility,
telemetry, support, and deprecation. Use cell or account boundaries aligned to
risk; scope GitOps reconciliation per environment rather than granting universal
authority. Offer paved roads with escape hatches governed by evidence and ownership.
Pilot willing teams, measure adoption and outcomes, improve from feedback, and
migrate in waves. A central approval board is not a substitute for automated,
auditable policy and risk-tiered review.

## Strong close

Present a six-month roadmap that delivers one useful thin slice early. Explain how
the platform avoids becoming a ticket queue, how consumers influence priorities,
and which metrics prove reduced cognitive load and safer delivery.
