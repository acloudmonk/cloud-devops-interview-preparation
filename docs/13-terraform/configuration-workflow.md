# Configuration, Graph, and Workflow

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Terraform and OpenTofu evaluate configuration, construct a dependency graph, read
provider state, propose actions, and execute approved graph nodes. Think in graph and
lifecycle terms rather than reading files top to bottom.

## Configuration layers

| Layer | Responsibility | Common risk |
| --- | --- | --- |
| Variables | Explicit caller contract | weak types, secret defaults, excessive knobs |
| Locals | Derived internal values | hidden complexity and duplicated policy |
| Data sources | Read existing remote data | apply-time uncertainty and external coupling |
| Resources | Desired managed objects | ownership conflict and replacement |
| Outputs | Supported result contract | leaking secrets or coupling consumers to internals |
| Modules | Composed capability | oversized blast radius and version lock-in |
| Providers | API schema and behavior | version drift, credentials, aliases, breaking changes |

## Dependency graph

References create implicit edges. Use explicit dependencies only when a real operational
ordering exists but no data reference expresses it. Excessive explicit dependencies
serialize work, spread unknown values, and conceal a weak module interface.

The graph controls execution order, not application readiness. A database API returning
“created” does not prove schema initialization or downstream application health.

## Write, plan, apply

1. **Write:** format and statically validate configuration; select pinned dependencies.
2. **Plan:** refresh/read remote objects, compare configuration and state, calculate
   proposed create/update/replace/delete actions, and evaluate available policy.
3. **Approve:** review the exact saved plan, identity, target, replacement, deletion,
   unknown values, cost/security effect, and recovery evidence.
4. **Apply:** execute that reviewed plan once with controlled credentials and locking.
5. **Verify:** confirm cloud and service outcomes independently of command success.

Do not approve a human-readable plan and later generate a different plan for apply.
A saved plan is still time-bound: state, credentials, provider behavior, and the remote
system can change before execution.

## Values and uncertainty

Values can be known during configuration evaluation, discovered during planning, or
remain unknown until apply. A good reviewer identifies whether an unknown value can
change resource count, identity, policy, or replacement behavior. Avoid designs whose
topology depends on apply-time results when stable keys can be chosen earlier.

## Resource identity and lifecycle

- `count` uses numeric position; list reordering may shift addresses.
- `for_each` uses stable keys; changing a key changes identity.
- Replacement destroys and recreates unless lifecycle and provider behavior allow a
  safe create-before-destroy sequence.
- Lifecycle rules can reduce risk but can also hide drift or block legitimate changes.
- Preconditions and postconditions express assumptions close to the resource contract.

Never use “prevent destroy” as the only data-protection control. Combine it with cloud
deletion protection, backups, scoped roles, policy, and recovery tests.

## Common planning traps

- Reviewing only the action count instead of attribute-level changes.
- Ignoring provider-induced replacement or computed/unknown fields.
- Using targeted plans as a routine deployment strategy.
- Treating refresh-only results as harmless without investigating ownership.
- Passing entire resource objects between modules and creating accidental coupling.
- Using provisioners for lifecycle work better owned by images, services, or pipelines.

## Interview diagnosis sequence

When plan and expectation differ, inspect configuration and inputs, resource addresses,
state binding, provider/version lock, refreshed remote data, lifecycle rules, unknowns,
and recent manual or external-controller changes—in that order.
