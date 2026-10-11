# Cross-Cloud Mapping References, Books, and Videos

[← Flashcards](flashcards.md) · [Module overview](index.md)

Mappings age quickly. Verify product documentation, regional availability, quotas,
pricing, SLAs, compliance, and current names before making a production decision.

## Suggested reading order

1. [Google Cloud comparison of AWS, Azure, and GCP services](https://docs.cloud.google.com/docs/get-started/aws-azure-gcp-service-comparison)
2. [Azure for AWS professionals](https://learn.microsoft.com/azure/architecture/aws-professional/)
3. [AWS multicloud strategy recommendations](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-multicloud-fsi/recommendations.html)
4. [Google Cloud hybrid and multicloud strategy](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns/strategy)
5. [Google Cloud hybrid and multicloud patterns](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices)

## Provider architecture and foundations

- [AWS Architecture Center](https://aws.amazon.com/architecture/)
- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
- [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)
- [Azure Architecture Center](https://learn.microsoft.com/azure/architecture/)
- [Azure landing zones](https://learn.microsoft.com/azure/cloud-adoption-framework/ready/landing-zone/)
- [Azure Well-Architected Framework](https://learn.microsoft.com/azure/well-architected/)
- [Google Cloud Architecture Center](https://cloud.google.com/architecture)
- [Google Cloud landing zones](https://docs.cloud.google.com/architecture/landing-zones)
- [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)

## Cross-cloud engineering

- [AWS cloud deployment strategies](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-multicloud-fsi/cloud-strategies.html)
- [Azure AWS account and subscription comparison](https://learn.microsoft.com/azure/architecture/aws-professional/accounts)
- [Azure AWS networking comparison](https://learn.microsoft.com/azure/architecture/aws-professional/networking)
- [Google Cloud distributed architecture patterns](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/distributed-patterns)
- [OpenTelemetry documentation](https://opentelemetry.io/docs/)
- [OpenTofu documentation](https://opentofu.org/docs/)
- [Terraform provider documentation](https://developer.hashicorp.com/terraform/language/providers)
- [Kubernetes documentation](https://kubernetes.io/docs/home/)

## Video sources

- [AWS Events](https://www.youtube.com/@AWSEventsChannel)
- [Microsoft Azure](https://www.youtube.com/@MicrosoftAzure)
- [Google Cloud Tech](https://www.youtube.com/@googlecloudtech)
- [CNCF](https://www.youtube.com/@cncf)

## Books for deeper study

- *Cloud Strategy* by Gregor Hohpe
- *Designing Data-Intensive Applications* by Martin Kleppmann
- *Building Secure and Reliable Systems* by Heather Adkins and others
- *Site Reliability Engineering* by Betsy Beyer and others
- *Infrastructure as Code* by Kief Morris

## Suggested review loop

1. Choose a capability and write provider-neutral requirements.
2. Compare all three providers using scope, semantics, failure, operations, and cost.
3. Label equivalence, gaps, composition, or no match.
4. Verify volatile facts in current primary documentation.
5. Prototype the critical behavior and record evidence and exit triggers.
