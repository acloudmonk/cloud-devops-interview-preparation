# SaaS Architecture References and Videos

[← Active-recall flashcards](flashcards.md) · [Module overview](index.md)

Verify current service semantics, quotas, Regions, pricing, identity behavior, and
compliance scope before production decisions. Read for principles first; translate
product examples through your tenant and operating model.

## Suggested reading order

1. [AWS SaaS Architecture Fundamentals](https://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/welcome.html)
2. [AWS Well-Architected SaaS Lens](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/welcome.html)
3. [Azure SaaS and multitenant solution architecture](https://learn.microsoft.com/azure/architecture/guide/saas-multitenant-solution-architecture/)
4. [Azure tenancy models](https://learn.microsoft.com/azure/architecture/guide/multitenant/considerations/tenancy-models)
5. [AWS tenant isolation strategies](https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/)

## SaaS foundations and isolation

- [AWS SaaS Lens general design principles](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/general-design-principles.html)
- [AWS SaaS tenant isolation](https://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/tenant-isolation.html)
- [AWS multi-tenant SaaS authorization and API access control](https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/introduction.html)
- [AWS SaaS Lens full-stack isolation](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/full-stack-isolation.html)
- [Azure architectural approaches for multitenancy](https://learn.microsoft.com/azure/architecture/guide/multitenant/approaches/overview)
- [Azure Deployment Stamps pattern](https://learn.microsoft.com/azure/architecture/patterns/deployment-stamp)
- [Azure storage and data approaches for multitenancy](https://learn.microsoft.com/azure/architecture/guide/multitenant/approaches/storage-data)
- [Google Cloud Identity Platform multitenancy](https://docs.cloud.google.com/identity-platform/docs/multi-tenancy)

## Lifecycle, operations, and economics

- [AWS SaaS Lens tenant activity and consumption](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/tenant-activity-and-consumption.html)
- [AWS SaaS Lens tenant insights](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/tenant-insights.html)
- [AWS SaaS Lens expenditure awareness](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/expenditure-awareness.html)
- [Azure considerations for updating multitenant solutions](https://learn.microsoft.com/azure/architecture/guide/multitenant/considerations/updates)
- [Azure tenant lifecycle considerations](https://learn.microsoft.com/azure/architecture/guide/multitenant/considerations/tenant-life-cycle)
- [OpenTelemetry documentation](https://opentelemetry.io/docs/)
- [Stripe usage-based billing documentation](https://docs.stripe.com/billing/subscriptions/usage-based)
- [FinOps Framework](https://www.finops.org/framework/)

## Security and reliability

- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
- [AWS Builders' Library](https://aws.amazon.com/builders-library/)
- [OWASP API Security Top 10](https://owasp.org/API-Security/)
- [NIST Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)
- [Google SRE books](https://sre.google/books/)

## Video sources

- [AWS Events](https://www.youtube.com/@AWSEventsChannel)
- [AWS Developers](https://www.youtube.com/@awsdevelopers)
- [Microsoft Azure](https://www.youtube.com/@MicrosoftAzure)
- [Google Cloud Tech](https://www.youtube.com/@googlecloudtech)

Search within the official channels for current sessions on SaaS tenant isolation,
control planes, deployment stamps, identity federation, and usage-based billing.

## Books for deeper study

- *Cloud Strategy* by Gregor Hohpe
- *Designing Data-Intensive Applications* by Martin Kleppmann
- *Building Microservices* by Sam Newman
- *Release It!* by Michael T. Nygard
- *Software Architecture: The Hard Parts* by Neal Ford and others
- *Implementing Domain-Driven Design* by Vaughn Vernon

## Suggested review loop

1. Select one SaaS product and write its tenant, tier, isolation, and residency contract.
2. Map control plane, data plane, catalog authority, and lifecycle state machines.
3. Trace verified tenant context through API, data, job, event, cache, and telemetry.
4. Inject noisy neighbor, catalog corruption, metering replay, and regional failure.
5. Reconcile usage to invoice and tenant cost to product-tier economics.
6. Translate the design across AWS, Azure, and Google Cloud without false parity.
7. Re-answer the scenarios and state which evidence would change each decision.
