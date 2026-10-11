# AWS Architecture References and Videos

[← Active-recall flashcards](flashcards.md) · [Module overview](index.md)

AWS services, quotas, feature scope, Regions, pricing, and recommended practices change.
Verify current service documentation, quotas, pricing, and compliance eligibility before
production decisions.

## Suggested reading order

1. [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
2. [AWS Architecture Center](https://aws.amazon.com/architecture/)
3. [Organizing your AWS environment using multiple accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html)
4. [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/)
5. [AWS Builders' Library](https://aws.amazon.com/builders-library/)

## Foundation, governance, and security

- [AWS global infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)
- [AWS Organizations introduction](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)
- [AWS Control Tower overview](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)
- [AWS Resource Access Manager](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html)
- [AWS CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html)
- [AWS Service Catalog Administrator Guide](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html)
- [IAM introduction](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
- [Policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html)
- [AWS KMS concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html)
- [AWS CloudTrail concepts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html)
- [Amazon GuardDuty User Guide](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)

## Networking, compute, and application platforms

- [Amazon VPC User Guide](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
- [AWS Transit Gateway concepts](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html)
- [AWS PrivateLink concepts](https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html)
- [Amazon Route 53 Developer Guide](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html)
- [Amazon EC2 User Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)
- [Amazon ECS Developer Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)
- [Amazon EKS User Guide](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html)
- [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)

## Data, integration, reliability, and cost

- [Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
- [Amazon RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)
- [Amazon DynamoDB Developer Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)
- [Amazon SQS Developer Guide](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)
- [Amazon EventBridge User Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)
- [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
- [AWS service quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html)
- [AWS Cost Management documentation](https://docs.aws.amazon.com/cost-management/)
- [AWS Resilience Hub User Guide](https://docs.aws.amazon.com/resilience-hub/latest/userguide/what-is.html)

## Video sources

- [AWS Events](https://www.youtube.com/@AWSEventsChannel)
- [AWS Developers](https://www.youtube.com/@awsdevelopers)
- [AWS Online Tech Talks](https://www.youtube.com/@AWSOnlineTechTalks)
- [AWS](https://www.youtube.com/@amazonwebservices)

Search official channels for recent sessions on AWS Well-Architected, multi-account
strategy, identity, VPC and hybrid networking, serverless, containers, data services,
resilience, observability, quotas, and cost. Prefer current sessions because service
capabilities and recommended patterns evolve.

## Books for deeper study

- *AWS Well-Architected Framework* (AWS documentation)
- *Amazon Web Services in Action* by Andreas Wittig and Michael Wittig
- *AWS for Solutions Architects* by Alberto Artasanchez and Saurabh Shrivastava
- *Cloud Strategy* by Gregor Hohpe
- *Designing Data-Intensive Applications* by Martin Kleppmann
- *Site Reliability Engineering* by Betsy Beyer and others

## Suggested review loop

1. Choose one workload and write its journeys, qualities, demand, and constraints.
2. Draw Region, AZ, account, VPC, identity, data, and ownership boundaries.
3. Compare two runtime, data, and integration options using service semantics.
4. Inject AZ capacity, identity, network, quota, data, and control-plane failures.
5. Restore an isolated backup and define business integrity evidence conceptually.
6. Model bill dimensions, failure capacity, allocation, and one unit-cost metric.
7. Answer scenarios aloud, score the mock, and revisit only weak primary sources.
