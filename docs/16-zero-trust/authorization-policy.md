# Authorization and Policy

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Authentication establishes evidence about a subject. Authorization decides
whether that subject may perform an action on a resource under current conditions.
Zero Trust fails when strong authentication fronts broad, permanent permissions.

## Access models

| Model | Useful for | Primary risk |
| --- | --- | --- |
| RBAC | stable job functions and understandable administration | role explosion and accumulated privilege |
| ABAC | scalable decisions using subject, resource, and context attributes | bad attributes or opaque policies |
| ReBAC | ownership, tenancy, hierarchy, and sharing relationships | complex graph correctness and review |
| Risk-adaptive | challenge or constrain using current signals | false confidence, bias, and poor explainability |

Most enterprises combine models: roles establish a baseline, attributes and
relationships narrow it, and risk may add restrictions or require stronger
authentication. Machine-learning risk should not invent grants absent from
declarative policy.

## Decision and enforcement

A policy information point supplies signals; a policy decision point evaluates
them; a policy enforcement point applies the result. These may be separate
services or functions inside an application, gateway, cloud service, or host.
Place enforcement where it cannot be bypassed and as close to the resource as
needed for action-level context.

## Policy engineering

- Write policy from business transactions and data classification.
- Use stable, authoritative attributes with defined owners and freshness.
- Version, review, test, simulate, and progressively deploy policy as code.
- Log inputs, decision, policy version, enforcement result, and correlation ID.
- Define deny behavior, degraded mode, exception, rollback, and break-glass.
- Test negative cases, tenant isolation, stale data, and conflicting policies.

## Least-privilege dimensions

Constrain resource, action, condition, environment, duration, session, network
path, data field, and transaction value. Just-in-time access reduces standing
privilege; just-enough access reduces scope. Both require timely revocation and
proof that the enforcement point actually applied the decision.

## Governance without paralysis

Central teams should define common vocabulary, mandatory boundaries, reusable
policy components, and evidence requirements. Resource-owning teams should own
fine-grained permissions. Report unreachable policy, unused access, wildcard
grants, orphaned exceptions, and decision errors—not merely policy count.

Return to the [module overview](index.md) when ready to continue.
