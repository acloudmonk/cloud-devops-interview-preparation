# Identity, Security, and Data Protection

[← Enterprise platform](enterprise-platform.md) · [Next: Networking →](networking-edge.md)

Use Cloud Identity or Google Workspace groups for workforce access, least-privilege IAM
roles, separation of duties, strong authentication, and time-bound privilege. Service
accounts are workload identities. Prefer attached identities and Workload Identity
Federation over downloadable keys; for GKE, use Workload Identity Federation for GKE.

| Layer | Representative controls |
| --- | --- |
| Prevent | IAM, deny, Organization Policy, VPC Service Controls, firewall policy |
| Protect | Cloud KMS/CMEK where justified, Secret Manager, TLS, tokenization |
| Detect | Cloud Audit Logs, Security Command Center, Event Threat Detection |
| Respond | isolated roles/projects, playbooks, evidence retention, tested access |

VPC Service Controls reduce exfiltration paths for supported services; they do not
replace IAM, network controls, secure application logic, or classification. CMEK adds
key availability, permission, rotation, regional, disablement, and recovery obligations.

To diagnose authorization, identify principal and token, permission, resource,
inherited allow/deny, condition, organization constraint, service perimeter, network
path, and audit record. Never solve an unexplained denial by granting Owner broadly.

Classify data, minimize collection, set residency and retention, encrypt, separate key
administration, audit access, protect backups, and test deletion and restoration.
