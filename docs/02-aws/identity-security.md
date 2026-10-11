# Identity, Security, and Data Protection

[← Enterprise platform](enterprise-platform.md) · [Next: Networking and edge →](networking-edge.md)

## Build from identities and resources

Federate workforce access through IAM Identity Center or a justified alternative; use
short-lived roles and MFA, not long-lived IAM users. Give workloads roles scoped to
their task. Protect root and break-glass access, separate duties, review unused access,
and log role assumption across accounts.

## Evaluate effective authorization

Authorization can involve Organizations policies, identity policies, resource
policies, permissions boundaries, session policies, VPC endpoint policies, KMS key
policies, and service-specific controls. Explicit deny wins. Trace the principal,
action, resource, condition, trust policy, organization/account, and request context
rather than changing policies blindly.

## Protect data and keys

Classify data; minimize collection and copies; encrypt transport and storage; choose
AWS-owned, AWS-managed, or customer-managed keys deliberately; restrict key use and
administration; rotate where required; and plan deletion and recovery. KMS policy,
grants, Region, quotas, and unavailable or deleted keys can make otherwise durable data
unusable.

## Detect and respond

Centralize protected CloudTrail, AWS Config, security findings, access analysis, and
relevant workload/network logs. Services such as GuardDuty, Security Hub, Inspector,
Macie, Detective, and Security Lake can add capability, but require coverage,
delegation, routing, retention, triage, and response ownership. Test containment with
forensic preservation and safe automation.

## Apply shared responsibility precisely

AWS secures the cloud; customers secure their configuration and use of cloud services.
The boundary varies by service abstraction. Capture patching, runtime, data, identity,
network, logging, backup, vulnerability, incident, compliance, and supplier duties in
a responsibility matrix with evidence owners.
