# Hybrid and Multi-Cloud References

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Verify provider capability, Region, SLA, routing, encryption, quota, support, and
commercial behavior in current documentation before production decisions.

## Core reading order

1. [Google Cloud: Plan a hybrid and multi-cloud strategy](https://cloud.google.com/architecture/hybrid-multicloud-patterns/strategy)
2. [Google Cloud hybrid and multi-cloud patterns](https://cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices)
3. [AWS hybrid-cloud best practices](https://docs.aws.amazon.com/prescriptive-guidance/latest/hybrid-cloud-best-practices/welcome.html)
4. [Azure hybrid and adaptive cloud architecture](https://learn.microsoft.com/azure/architecture/hybrid/hybrid-start-here)
5. [NIST Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)

## AWS anchor

- [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)
- [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html)
- [AWS Cloud WAN](https://docs.aws.amazon.com/network-manager/latest/cloudwan/what-is-cloudwan.html)
- [AWS Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html)
- [Amazon EKS Anywhere](https://anywhere.eks.amazonaws.com/docs/)
- [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
- [IAM roles anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html)
- [Route 53 Resolver](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html)
- [Data Residency and Hybrid Cloud Services Lens](https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/welcome.html)

## Azure translation

- [Azure Arc overview](https://learn.microsoft.com/azure/azure-arc/overview)
- [Azure ExpressRoute](https://learn.microsoft.com/azure/expressroute/expressroute-introduction)
- [Azure Virtual WAN](https://learn.microsoft.com/azure/virtual-wan/virtual-wan-about)
- [Azure Local overview](https://learn.microsoft.com/azure/azure-local/overview)
- [Microsoft Entra workload identity federation](https://learn.microsoft.com/entra/workload-id/workload-identity-federation)
- [Azure hybrid identity](https://learn.microsoft.com/entra/identity/hybrid/whatis-hybrid-identity)

## Google Cloud translation

- [Distributed, hybrid, and multi-cloud](https://cloud.google.com/docs/dhm-cloud)
- [Hybrid and multi-cloud network reference architectures](https://cloud.google.com/architecture/network-hybrid-multicloud)
- [Cloud Interconnect](https://cloud.google.com/network-connectivity/docs/interconnect)
- [Cross-Cloud Interconnect](https://cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview)
- [Google Distributed Cloud](https://cloud.google.com/distributed-cloud)
- [Workload Identity Federation](https://cloud.google.com/iam/docs/workload-identity-federation)

## Open and operational standards

- [OpenTelemetry](https://opentelemetry.io/docs/)
- [CloudEvents](https://cloudevents.io/)
- [OCI image specification](https://github.com/opencontainers/image-spec)
- [CNCF Cloud Native Maturity Model](https://maturitymodel.cncf.io/)
- [Kubernetes multi-cluster concepts](https://kubernetes.io/docs/concepts/cluster-administration/networking/)

## Targeted videos

- [AWS re:Invent 2024: AWS wherever you need it—from cloud to edge](https://www.youtube.com/watch?v=_1quMnn2TI0)
- [Microsoft: Introduction to the hybrid and multicloud scenario](https://www.youtube.com/watch?v=FxGyXb-cP6M)
- [Google Cloud: Five hybrid and multicloud architecture designs](https://www.youtube.com/watch?v=tE9FcKiDJxo)

Use these sessions to compare placement and operating choices, then verify current
service behavior in the official documentation above.

## Video discovery channels

- [AWS Events](https://www.youtube.com/@AWSEventsChannel)
- [Microsoft Azure](https://www.youtube.com/@MicrosoftAzure)
- [Google Cloud Tech](https://www.youtube.com/@googlecloudtech)
- [CNCF](https://www.youtube.com/@cncf)

## Books for deeper study

- *Cloud Strategy: A Decision-Based Approach to Successful Cloud Migration* by
  Gregor Hohpe
- *Enterprise Integration Patterns* by Gregor Hohpe and Bobby Woolf
- *Building Secure & Reliable Systems* by Heather Adkins and others

Use books for durable decision models and current official documentation for
provider capability, limits, and operating behavior.

## Suggested review loop

1. Start with the strategy sources and state the durable business reason for
   using more than one environment.
2. Study the AWS anchor for the primary implementation model.
3. Translate the same requirement to Azure and Google Cloud without assuming
   product names imply identical semantics.
4. Use the standards and books to test portability, integration, security,
   resilience, and operating assumptions.
5. Select targeted videos only for a weak concept; verify product details in
   the corresponding official documentation.
6. Return to the scenarios or mock interview and explain the business driver,
   placement, trust/data/failure boundaries, operating owner, lifecycle cost,
   evidence, and simplification trigger.

Return to the [module overview](index.md) when ready to continue.
