# Terraform and OpenTofu Rapid-Fire Revision

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Answer each in 30–60 seconds with a definition, ownership boundary, failure mode, and one
condition that changes the choice.

## Core model and workflow

1. **Infrastructure as Code?** Versioned declaration plus reviewed, automated, controlled lifecycle and evidence.
2. **Desired configuration?** Authored intent; it is not recorded state, observed cloud state, or customer outcome.
3. **Plan?** Target-specific proposal based on configuration, inputs, state, provider reads, and versions.
4. **Saved-plan rule?** Apply the exact approved plan once; expire it when relevant context changes.
5. **Dependency graph?** Resource/module ordering from references; it does not prove application readiness.
6. **Unknown value?** Value unavailable until a later evaluation/apply phase; assess effect on identity and policy.
7. **Replacement?** Destroy/create lifecycle caused by schema or identity change; requires protection and recovery.
8. **`count` risk?** Positional identity can shift when a list changes.
9. **`for_each` strength?** Stable semantic keys when keys themselves remain stable.
10. **Provisioner concern?** Imperative side effects, weak idempotency/state semantics, and difficult recovery.

## State, modules, and environments

1. **State purpose?** Bind resource addresses to remote identities and retain planning metadata.
2. **Sensitive value?** Redacted in selected output but may remain plaintext in state/plan.
3. **Backend?** State storage and coordination integration with durability, access, locking, and recovery choices.
4. **Lock?** Concurrent-writer protection, not protection from console or other-controller changes.
5. **Force unlock?** Exceptional action only after proving the original writer is inactive.
6. **State boundary?** Align with owner, credentials, lifecycle, cadence, SLO, and failure radius.
7. **Root module?** Deployable ownership/state/provider/execution boundary.
8. **Reusable module?** Versioned capability contract with inputs, outputs, invariants, tests, and support.
9. **CLI workspace?** Multiple state instances for one configuration; not a strong security boundary.
10. **Promotion?** Reuse versioned code/dependencies and plan separately against each target's current state.

## Identity, testing, and policy

1. **Provider?** Executable API integration with schema, credentials, lifecycle behavior, and supply-chain risk.
2. **Dependency lock file?** Selected provider versions/checksums for reproducible initialization.
3. **Provider alias?** Explicit additional provider configuration for another account, region, or identity.
4. **Preferred CI identity?** Federated short-lived workload identity into a scoped cloud role.
5. **Plan permission?** Broad read plus limited needs; separate from narrower controlled write where practical.
6. **Policy as code?** Versioned evaluated organizational decisions with tests, owner, exceptions, and failure mode.
7. **Static versus plan policy?** Source-pattern check versus action/value-aware evaluated-plan check.
8. **Integration test?** Real provider/module behavior in a bounded disposable environment.
9. **Supply-chain scope?** Tool, provider, module, CI action, policy, registry, and runner.
10. **Exception?** Scoped, justified, approved, compensated, owned, observable, and expiring deviation.

## Operations and recovery

1. **Drift?** Difference among configuration, recorded state, and observed remote object requiring classification.
2. **Import?** Bind an existing remote identity to an address; it does not author safe configuration.
3. **Moved declaration?** Versioned address migration that avoids interpreting a refactor as destroy/create.
4. **Partial apply?** Some graph actions succeeded; preserve evidence, refresh, and choose deliberate recovery.
5. **Refresh-only use?** Inspect/record remote changes without normal desired-state actions; still review ownership.
6. **Targeted apply?** Exceptional recovery mechanism that can omit graph changes; not routine delivery.
7. **Provider upgrade?** Dedicated, tested, canaried lifecycle change with schema/replacement review.
8. **State restore proof?** Correct lineage/serial, cloud identity reconciliation, read-only plan, and rehearsal.
9. **Emergency console change?** Bounded break glass with audit, owner/expiry, source reconciliation, and verification.
10. **IaC SLO?** User-facing plan/apply/recovery outcomes, not runner uptime alone.

## Terraform, OpenTofu, and leadership

1. **Shared foundation?** HCL lineage, providers, modules, graph, plan/apply, state, backends, and lifecycle concepts.
2. **Terraform-specific area?** HCP Terraform/Enterprise services and Terraform Stacks.
3. **OpenTofu-specific area?** Linux Foundation governance and independently developed features such as state encryption.
4. **Compatibility rule?** Verify exact versions/features and pin one tool per root; never assume perpetual symmetry.
5. **Migration first step?** Inventory versions, dependencies, automation, state graph, features, and support obligations.
6. **State encryption limit?** Adds confidentiality but also key availability/recovery; backend access control remains necessary.
7. **Multi-cloud module trap?** Same interface can hide materially different identity, network, hierarchy, and lifecycle semantics.
8. **Platform success?** Faster safe provisioning, lower failure/recovery time, adoption, fewer exceptions, and satisfied users.
9. **Tool standardization?** Supported default plus evidence-based exceptions, not forced uniformity without migration.
10. **Principal-level close?** Outcome, boundaries, trust, controls, recovery, tool decision, adoption, measures, next decision.
