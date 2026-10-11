# Platform Engineering References and Videos

[← Active-recall flashcards](flashcards.md) · [Module overview](index.md)

Verify current service behavior, quotas, versions, pricing, and support before
production decisions. Prefer primary sources and measure local developer outcomes.

## Suggested reading order

1. [AWS: Building an internal developer platform](https://docs.aws.amazon.com/prescriptive-guidance/latest/internal-developer-platform/introduction.html)
2. [CNCF Platforms white paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/)
3. [Backstage overview](https://backstage.io/docs/overview/what-is-backstage/)
4. [Microsoft: What is platform engineering?](https://learn.microsoft.com/platform-engineering/what-is-platform-engineering)
5. [Google Cloud: Platform engineering](https://cloud.google.com/solutions/platform-engineering)

## Product, architecture, and interfaces

- [AWS principles for an internal developer platform](https://docs.aws.amazon.com/prescriptive-guidance/latest/internal-developer-platform/principles.html)
- [AWS internal developer platform preparation](https://docs.aws.amazon.com/prescriptive-guidance/latest/internal-developer-platform/preparation.html)
- [AWS internal developer platform architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/internal-developer-platform/design-architecture.html)
- [Backstage software catalog](https://backstage.io/docs/features/software-catalog/)
- [Backstage software templates](https://backstage.io/docs/features/software-templates/)
- [Backstage TechDocs](https://backstage.io/docs/features/techdocs/)
- [Crossplane documentation](https://docs.crossplane.io/latest/)
- [Kubernetes controllers](https://kubernetes.io/docs/concepts/architecture/controller/)

## Delivery, security, and operations

- [SLSA supply-chain framework](https://slsa.dev/)
- [OpenSSF Scorecard](https://securityscorecards.dev/)
- [NIST Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final)
- [Kubernetes multi-tenancy](https://kubernetes.io/docs/concepts/security/multi-tenancy/)
- [OpenTelemetry documentation](https://opentelemetry.io/docs/)
- [Google SRE books](https://sre.google/books/)
- [FinOps Framework](https://www.finops.org/framework/)

## Product, adoption, and multi-cloud

- [DORA research and guidance](https://dora.dev/)
- [Microsoft platform engineering guide](https://learn.microsoft.com/platform-engineering/)
- [Microsoft platform engineering capabilities model](https://learn.microsoft.com/platform-engineering/capability-model/)
- [Microsoft self-service with guardrails](https://learn.microsoft.com/platform-engineering/about/self-service)
- [Google Cloud: Internal developer platforms](https://cloud.google.com/discover/what-is-an-internal-developer-platform)
- [Team Topologies](https://teamtopologies.com/)

## Video sources

- [CNCF](https://www.youtube.com/@cncf)
- [AWS Events](https://www.youtube.com/@AWSEventsChannel)
- [Microsoft Azure](https://www.youtube.com/@MicrosoftAzure)
- [Google Cloud Tech](https://www.youtube.com/@googlecloudtech)

Use videos for architecture narratives and practitioner lessons, then verify
technical claims in current primary documentation.

## Books for deeper study

- *Team Topologies* by Matthew Skelton and Manuel Pais
- *Platform Engineering on Kubernetes* by Mauricio Salatino
- *Accelerate* by Nicole Forsgren, Jez Humble, and Gene Kim
- *Building Secure and Reliable Systems* by Heather Adkins and others
- *Fundamentals of Software Architecture* by Mark Richards and Neal Ford

## Suggested review loop

1. Identify one developer journey and record its current wait, failure, and effort.
2. Map responsibility, interface, control, lifecycle, and evidence for a thin path.
3. Test failure, upgrade, exception, and deletion—not only happy-path provisioning.
4. Compare AWS implementation with Azure and Google while preserving outcomes.
5. Measure flow, quality, reliability, experience, adoption, and unit economics.
6. Return to scenarios and explain what the platform deliberately does not own.
