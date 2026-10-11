# HA, DR, and Business Continuity References

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Prefer current primary standards and official provider guidance. Verify service,
Region, tier, quota, consistency, failover, backup, and SLA behavior before using
a provider-specific feature in a production design.

## Core reading order

1. [AWS Well-Architected: Plan for disaster recovery](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-13.html)
2. [AWS: Disaster recovery options in the cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html)
3. [NIST SP 800-34 Rev. 1: Contingency Planning Guide](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final)
4. [Azure Well-Architected: Architecture strategies for disaster recovery](https://learn.microsoft.com/azure/well-architected/reliability/disaster-recovery)
5. [Google Cloud disaster-recovery planning guide](https://cloud.google.com/architecture/dr-scenarios-planning-guide)

## AWS anchor

- [AWS Well-Architected Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)
- [AWS fault-isolation boundaries](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/aws-fault-isolation-boundaries.html)
- [AWS Resilience Hub](https://docs.aws.amazon.com/resilience-hub/latest/userguide/what-is.html)
- [AWS Backup Developer Guide](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)
- [AWS Backup cross-account copies](https://docs.aws.amazon.com/aws-backup/latest/devguide/create-cross-account-backup.html)
- [AWS Backup Vault Lock](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html)
- [Amazon S3 replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html)
- [Amazon S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html)
- [Amazon Route 53 disaster-recovery mechanisms](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/disaster-recovery-resiliency.html)
- [AWS Elastic Disaster Recovery](https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html)
- [AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html)

## Azure translation

- [Azure reliability documentation](https://learn.microsoft.com/azure/reliability/)
- [Business continuity, high availability, and disaster recovery](https://learn.microsoft.com/azure/reliability/concept-business-continuity-high-availability-disaster-recovery)
- [Develop a multi-region disaster-recovery plan](https://learn.microsoft.com/azure/well-architected/design-guides/disaster-recovery)
- [Azure Backup documentation](https://learn.microsoft.com/azure/backup/)
- [Azure Site Recovery documentation](https://learn.microsoft.com/azure/site-recovery/)
- [Azure regions and availability zones](https://learn.microsoft.com/azure/reliability/regions-overview)
- [Azure Chaos Studio](https://learn.microsoft.com/azure/chaos-studio/chaos-studio-overview)

## Google Cloud translation

- [Google Cloud Well-Architected reliability pillar](https://cloud.google.com/architecture/framework/reliability)
- [Google Cloud disaster-recovery scenarios](https://cloud.google.com/architecture/dr-scenarios-building-blocks)
- [Google Cloud geographic management](https://cloud.google.com/docs/geography-and-regions)
- [Backup and DR Service documentation](https://cloud.google.com/backup-disaster-recovery/docs)
- [Cloud Storage availability and durability](https://cloud.google.com/storage/docs/availability-durability)
- [Cloud SQL disaster recovery](https://cloud.google.com/sql/docs/mysql/intro-to-cloud-sql-disaster-recovery)

## Continuity and security guidance

- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework)
- [NIST SP 800-53 Rev. 5: Contingency Planning controls](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)
- [CISA StopRansomware Guide](https://www.cisa.gov/stopransomware/ransomware-guide)
- [Ready.gov business continuity planning](https://www.ready.gov/business-continuity-planning-suite)

## Video channels

- [AWS Events](https://www.youtube.com/@AWSEventsChannel)
- [AWS Online Tech Talks](https://www.youtube.com/@AWSOnlineTechTalks)
- [Microsoft Azure](https://www.youtube.com/@MicrosoftAzure)
- [Google Cloud Tech](https://www.youtube.com/@googlecloudtech)
- [USENIX](https://www.youtube.com/@USENIXAssociation)

## Books

- *Site Reliability Engineering* by Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy
- *Building Secure and Reliable Systems* by Heather Adkins and others
- *Release It!* by Michael T. Nygard
- *The Practice of Cloud System Administration* by Thomas Limoncelli, Strata Chalup, and Christina Hogan

After reading, explain the protected business outcome, failure assumption,
objective, decision authority, recovery mechanism, evidence, cost, and residual
risk. Avoid memorizing provider product lists without these relationships.

Return to the [module overview](index.md) when ready to continue.
