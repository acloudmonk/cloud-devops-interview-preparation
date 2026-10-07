# References and Videos

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last verified: **2026-10-04**

The reading path favors durable architecture guidance over product catalogs.

## Required reading

### AWS Well-Architected Framework

- **Source:** Amazon Web Services
- **Type:** Architecture framework
- **Level:** Architect
- **Why:** Review architectural decisions across operational excellence,
  security, reliability, performance, cost, and sustainability.
- **Link:** [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)

### Azure Well-Architected Framework

- **Source:** Microsoft
- **Type:** Architecture framework
- **Level:** Architect
- **Why:** Connect workload quality and business value to reliability, security,
  cost, operations, and performance decisions.
- **Link:** [Azure Well-Architected Framework](https://learn.microsoft.com/azure/well-architected/)

### Google Cloud Well-Architected Framework

- **Source:** Google Cloud
- **Type:** Architecture framework
- **Level:** Architect
- **Why:** Study cross-cloud-relevant principles such as designing for change,
  simplicity, decoupling, statelessness, and documented decisions.
- **Link:** [Google Cloud Well-Architected Framework](https://cloud.google.com/architecture/framework)

### Amazon Builders' Library

- **Source:** Amazon Web Services
- **Type:** First-party engineering articles
- **Level:** Advanced/architect
- **Why:** Practical material on timeouts, retries, backoff, jitter, load shedding,
  health checks, deployment safety, and distributed-system operations.
- **Link:** [Amazon Builders' Library](https://aws.amazon.com/builders-library/)

### Site Reliability Engineering books

- **Source:** Google
- **Type:** Free online books
- **Level:** Advanced/architect
- **Why:** Reliability objectives, monitoring, overload, incident response,
  release engineering, and organizational practice.
- **Link:** [Google SRE books](https://sre.google/books/)

### Architecture styles and patterns

- **Source:** Microsoft Azure Architecture Center
- **Type:** Pattern catalog
- **Level:** Advanced/architect
- **Why:** Compare architecture styles and implementation-neutral cloud design
  patterns, including messaging and resilience patterns.
- **Link:** [Azure architecture patterns](https://learn.microsoft.com/azure/architecture/patterns/)

## Videos

### Introduction to the Azure Well-Architected Framework

- **Publisher:** Microsoft Learn / Microsoft Developer
- **Type:** Guided session
- **Level:** Foundation/architect
- **Why:** Introduces a structured quality review instead of a service-first
  architecture discussion.
- **Link:** [Learn Live: Introduction to the Microsoft Azure Well-Architected Framework](https://www.youtube.com/watch?v=BF1Tw9MNa5U)

### Improving workload reliability

- **Publisher:** Microsoft Developer
- **Type:** Architecture discussion
- **Level:** Foundation/advanced
- **Why:** Connects reliability concepts to platform and application building
  blocks and walks through an architecture diagram.
- **Link:** [Start improving the reliability of your Azure workloads](https://www.youtube.com/watch?v=HEUPIxFyxB0)

## Video discovery sources

Use the following official channels to find current conference talks. Add exact
videos to this page only after reviewing their content and publication date.

- [Amazon Web Services](https://www.youtube.com/@amazonwebservices)
- [Microsoft Azure](https://www.youtube.com/@MicrosoftAzure)
- [Google Cloud Tech](https://www.youtube.com/@googlecloudtech)
- [CNCF](https://www.youtube.com/@cncf)

Recommended search themes include distributed-system failure modes, overload,
multi-region consistency, cell-based architecture, safe deployments, and
Well-Architected reviews.

## Deferred implementation references

These sources support optional future implementation practice. They are not
required for the current theory, documentation, and scenario-based pilot.

### AWS reliability testing guidance

- **Source:** Amazon Web Services
- **Type:** Well-Architected implementation guidance
- **Lifecycle:** Current when last verified
- **Why:** Defines production-like, representative, IaC-based resiliency,
  scaling, and quota testing practices.
- **Link:** [Test resiliency using chaos engineering](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_testing_resiliency_test_non_functional.html)

### DynamoDB conditional writes

- **Source:** Amazon Web Services
- **Type:** Product documentation
- **Lifecycle:** Current when last verified
- **Why:** Provides the conditional-expression mechanism used to protect the
  reservation state transition.
- **Link:** [Condition expressions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ConditionExpressions.html)

### CloudFront visitor prioritization

- **Source:** AWS Networking & Content Delivery Blog
- **Type:** Reference implementation guidance
- **Lifecycle:** Preferred current pattern when last verified
- **Why:** Demonstrates admission control with CloudFront Functions, AWS WAF,
  CloudWatch, and an S3 waiting-room origin.
- **Link:** [Visitor prioritization with CloudFront and CloudFront Functions](https://aws.amazon.com/blogs/networking-and-content-delivery/visitor-prioritization-on-e-commerce-websites-with-cloudfront-and-cloudfront-functions/)

### Virtual Waiting Room on AWS

- **Source:** Amazon Web Services
- **Type:** Archived solution
- **Lifecycle:** **Discontinued; do not use for a new implementation**
- **Replacement:** Use the CloudFront visitor-prioritization pattern above and
  validate it against current requirements.
- **Link:** [Virtual Waiting Room on AWS lifecycle notice](https://aws.amazon.com/solutions/implementations/virtual-waiting-room-on-aws/)

### Distributed Load Testing on AWS

- **Source:** Amazon Web Services
- **Type:** Optional managed solution
- **Lifecycle:** Verify version and cost before deployment
- **Why:** Provides a distributed path when a workstation cannot generate the
  required test load; the core lab uses local k6 first.
- **Link:** [Distributed Load Testing on AWS](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/solution-overview.html)

### AWS Fault Injection Service

- **Source:** Amazon Web Services
- **Type:** Product documentation
- **Lifecycle:** Current when last verified
- **Why:** Supports bounded, observable fault experiments after stop conditions
  and rollback are established.
- **Link:** [AWS Fault Injection Service user guide](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html)

## Books

- Martin Kleppmann, *Designing Data-Intensive Applications*
- Michael Nygard, *Release It!*
- Sam Newman, *Building Microservices*
- Mark Richards and Neal Ford, *Fundamentals of Software Architecture*
- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate*

Books are listed for durable mental models. Check the publisher for the latest
edition before purchasing.

## Suggested reading order

1. This module's core concepts and patterns
2. The capacity/SLO example and AWS decision matrix
3. One cloud Well-Architected framework end to end
4. Builders' Library articles on timeouts/retries and overload
5. The SRE chapters on service objectives and handling overload
6. The design lab, scenario drills, and troubleshooting playbook
7. The timed mock interview and active-recall cards
8. Relevant chapters from *Designing Data-Intensive Applications* and *Release It!*
