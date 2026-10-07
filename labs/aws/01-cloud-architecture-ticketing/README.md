# AWS Ticketing Architecture Lab Workspace

> [!NOTE]
> **Deferred optional material:** Executable implementation is not required for
> the current interview-focused curriculum. Use the documentation module's
> design lab, scenario drills, and AWS design walkthrough. This workspace is
> retained only for a possible future practical milestone.

This workspace supports the pilot module's
[AWS implementation guide](../../../docs/01-cloud-architecture/implementation-guide.md).
It provides safe structure and test artifacts without pretending that
unreviewed example infrastructure is production ready.

## Working agreement

- Use a dedicated sandbox AWS account and short-lived federation.
- Set an AWS Budget before deployment.
- Tag resources with `Project=ticketing-lab` and `Environment=lab`.
- Do not commit credentials, account IDs, state, plans, `.env`, or raw telemetry.
- Open a feature-branch PR and require manual approval for milestone changes.
- Run load and failure tests only against an endpoint you are authorized to test.

## Workspace

```text
01-cloud-architecture-ticketing/
├── .env.example
├── architecture/
│   ├── decisions/0001-compute-platform.md
│   └── threat-model.md
├── evidence/README.md
├── infra/terraform/
│   ├── bootstrap/README.md
│   └── workload/README.md
├── load/k6/ticket-release.js
├── observability/README.md
├── runbooks/order-processing.md
└── tests/README.md
```

Application and Terraform implementations should be added incrementally after
the matching decision record and acceptance test are reviewed. Recommended
application boundaries are `app/api`, `app/worker`, and `app/payment-stub`.

## Milestones

1. Complete assumptions, SLOs, threat model, and ADRs.
2. Prove seat and idempotency invariants locally.
3. Deploy the two-AZ AWS core using Terraform.
4. Add edge admission, security, telemetry, and delivery controls.
5. Run load, failure, and restore tests.
6. Record cost, measured RTO/RPO, limitations, and teardown.

## Definition of done

- All four business invariants in the lab are covered by automated tests.
- `terraform fmt -check -recursive` and `terraform validate` pass.
- No static cloud credential exists in source, image, configuration, or logs.
- The deployment can roll back to the prior known-good task definition.
- SLO, queue, payment-reconciliation, and DLQ behavior are observable.
- Load and fault reports state hypothesis, environment, result, and limitations.
- Destroy is followed by service/tag and cost verification.
