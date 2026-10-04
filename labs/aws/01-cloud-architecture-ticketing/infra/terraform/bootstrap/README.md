# Terraform State Bootstrap

Create remote state separately from the workload. Define encryption, public
access blocking, versioning, least-privilege access, and the current supported
state-locking approach selected by the team.

Record how the state infrastructure is initialized, recovered, and eventually
removed. Never commit state, plan files, account IDs, or sensitive variables.

Before implementation, review state bucket naming, encryption, role access,
locking, recovery, and safe teardown order.
