# Microservices Architecture References and Videos

[← Active-recall flashcards](flashcards.md) · [Module overview](index.md)

Verify current cloud service semantics, limits, Regions, pricing, and support before
production decisions. Use patterns as trade-off vocabulary, not mandatory components.

## Suggested reading order

1. [AWS Prescriptive Guidance: Decomposing monoliths](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/introduction.html)
2. [Azure Architecture Center: Microservices architecture style](https://learn.microsoft.com/azure/architecture/guide/architecture-styles/microservices)
3. [Azure: Use domain analysis to model microservices](https://learn.microsoft.com/azure/architecture/microservices/model/domain-analysis)
4. [AWS Builders' Library](https://aws.amazon.com/builders-library/)
5. [Microservices pattern language](https://microservices.io/patterns/)

## Domain, data, and contracts

- [Azure: Identify microservice boundaries](https://learn.microsoft.com/azure/architecture/microservices/model/microservice-boundaries)
- [Azure: Data considerations for microservices](https://learn.microsoft.com/azure/architecture/microservices/design/data-considerations)
- [AWS: Data persistence in microservices](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/introduction.html)
- [Database per service pattern](https://microservices.io/patterns/data/database-per-service.html)
- [Saga pattern](https://microservices.io/patterns/data/saga.html)
- [Transactional outbox pattern](https://microservices.io/patterns/data/transactional-outbox.html)
- [OpenAPI specification](https://spec.openapis.org/oas/latest.html)
- [AsyncAPI specification](https://www.asyncapi.com/docs/reference/specification/latest)

## AWS architecture anchor

- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
- [AWS Serverless Applications Lens](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html)
- [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)
- [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)
- [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html)
- [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)
- [Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)
- [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)

## Multi-cloud, resilience, and operations

- [Azure microservices design patterns](https://learn.microsoft.com/azure/architecture/microservices/design/patterns)
- [Google Cloud Architecture Framework](https://cloud.google.com/architecture/framework)
- [Google SRE books](https://sre.google/books/)
- [OpenTelemetry documentation](https://opentelemetry.io/docs/)
- [Kubernetes documentation](https://kubernetes.io/docs/)
- [OWASP API Security Top 10](https://owasp.org/API-Security/)

## Video sources

- [AWS Events](https://www.youtube.com/@AWSEventsChannel)
- [Microsoft Azure](https://www.youtube.com/@MicrosoftAzure)
- [Google Cloud Tech](https://www.youtube.com/@googlecloudtech)
- [CNCF](https://www.youtube.com/@cncf)

## Books for deeper study

- *Building Microservices* by Sam Newman
- *Monolith to Microservices* by Sam Newman
- *Microservices Patterns* by Chris Richardson
- *Domain-Driven Design* by Eric Evans
- *Implementing Domain-Driven Design* by Vaughn Vernon
- *Designing Data-Intensive Applications* by Martin Kleppmann

## Suggested review loop

1. Select one business workflow and identify language, invariants, and authority.
2. Compare modular-monolith and service options with organizational readiness.
3. Draw sync/async paths, data ownership, intermediate states, and reconciliation.
4. Inject timeout-after-success, duplicates, overload, and regional recovery.
5. Translate required capabilities across AWS, Azure, and Google Cloud.
6. Return to scenarios and explain when merging services is the better decision.
