# Threat Modeling and Security Requirements

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Threat modeling is a collaborative design activity. Its output is not a diagram;
it is a prioritized set of assumptions, mitigations, tests, owners, and accepted risks.

## Four-question flow

1. What are we building?
2. What can go wrong?
3. What will we do about it?
4. Did we do a good enough job?

Model data flows, identities, trust boundaries, assets, external dependencies,
administrative paths, tenancy, failure modes, and recovery. Use STRIDE, attack
trees, abuse cases, or another method as prompts—not as a substitute for context.

## Supply-chain threats

Include malicious or compromised contributors, stolen source tokens, dependency
confusion, typosquatting, poisoned build images, runner persistence, untrusted pull
requests, cache poisoning, artifact substitution, signing-identity theft, policy
bypass, registry compromise, and vulnerable update mechanisms.

## From threat to requirement

A useful security requirement includes:

- the protected asset and threat;
- enforceable behavior and control location;
- accountable owner and implementation boundary;
- verification method and retained evidence;
- failure behavior, exception path, and recovery;
- review trigger such as architecture, exposure, dependency, or incident change.

Example: "Production admits only immutable image digests with provenance from the
approved protected workflow and expected repository identity; verification fails
closed except through an audited, expiring emergency process."

## Prioritization

Use likelihood, impact, exposure, attacker effort, detection, recovery, and
control cost. Separate inherent from residual risk. Record assumptions and the
business risk owner; do not let an automated numeric score silently accept risk.

## Continuous triggers

Revisit the model when trust boundaries, authentication, sensitive data, tenancy,
internet exposure, build platform, deployment model, major dependency, or incident
changes. A lightweight delta review is often better than an annual workshop.

Return to the [module overview](index.md) when ready to continue.
