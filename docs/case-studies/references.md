# Case-Study References and Module Map

[← Principal architect capstone](capstone.md) · [Case-study overview](index.md)

Use sources to repair a weak decision after attempting a case. Do not read a large
service catalogue before framing the problem.

## Internal module map

| Decision area | Primary module |
| --- | --- |
| Distributed systems, scale, and trade-offs | [Cloud Architecture](../01-cloud-architecture/index.md) |
| Linux and network diagnosis | [Linux](../06-linux/index.md) and [Networking](../07-networking/index.md) |
| Delivery and runtime platforms | [CI/CD](../09-cicd/index.md), [Docker](../10-docker/index.md), [Kubernetes](../11-kubernetes/index.md) |
| Infrastructure and configuration automation | [Terraform/OpenTofu](../13-terraform/index.md), [Ansible](../14-ansible/index.md) |
| Supply chain and Zero Trust | [DevSecOps](../15-devsecops/index.md), [Zero Trust](../16-zero-trust/index.md) |
| Signals, SLOs, and incident learning | [Observability](../17-observability/index.md), [SRE](../18-sre/index.md) |
| Recovery and economics | [HA/DR/BCP](../25-ha-dr-bcp/index.md), [FinOps](../26-finops/index.md) |
| Reviews and distributed estates | [Well-Architected](../27-well-architected/index.md), [Hybrid/Multi-Cloud](../28-hybrid-multicloud/index.md) |
| APIs, automation, and AI | [API/Identity](../29-api-identity/index.md), [Python](../30-python-automation/index.md), [AI](../31-ai-for-devops/index.md) |

## Architecture and cloud guidance

- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
- [AWS Architecture Center](https://aws.amazon.com/architecture/)
- [AWS Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/)
- [Azure Well-Architected Framework](https://learn.microsoft.com/azure/well-architected/)
- [Azure Architecture Center](https://learn.microsoft.com/azure/architecture/)
- [Google Cloud Well-Architected Framework](https://cloud.google.com/architecture/framework)
- [Google Cloud Architecture Center](https://cloud.google.com/architecture)

## Reliability, security, delivery, and economics

- [AWS Builders' Library](https://aws.amazon.com/builders-library/)
- [Google SRE books](https://sre.google/books/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [NIST Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)
- [CISA Zero Trust Maturity Model](https://www.cisa.gov/resources-tools/resources/zero-trust-maturity-model)
- [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)
- [SLSA supply-chain framework](https://slsa.dev/)
- [FinOps Framework](https://www.finops.org/framework/)
- [Cloud Adoption Framework for AWS](https://aws.amazon.com/cloud-adoption-framework/)
- [Azure Cloud Adoption Framework](https://learn.microsoft.com/azure/cloud-adoption-framework/)
- [Google Cloud Adoption Framework](https://cloud.google.com/adoption-framework)

## Video sources

- [AWS Events](https://www.youtube.com/@AWSEventsChannel)
- [Microsoft Azure](https://www.youtube.com/@MicrosoftAzure)
- [Google Cloud Tech](https://www.youtube.com/@googlecloudtech)
- [CNCF](https://www.youtube.com/@cncf)

Use conference case studies to observe trade-off communication, then verify current
service behavior in primary written documentation.

## Books for deeper study

- *Fundamentals of Software Architecture* by Mark Richards and Neal Ford
- *Designing Data-Intensive Applications* by Martin Kleppmann
- *Building Evolutionary Architectures* by Neal Ford, Rebecca Parsons, and Patrick Kua
- *Accelerate* by Nicole Forsgren, Jez Humble, and Gene Kim
- *Site Reliability Engineering* by Betsy Beyer and others

## Suggested review loop

1. Score the case and select the lowest two dimensions.
2. Read the corresponding internal module before following external references.
3. Update the decision record, failure table, and phased roadmap.
4. Repeat with two different injects and a stricter stakeholder challenge.
5. Explain what evidence changed the recommendation; avoid memorizing a model answer.
