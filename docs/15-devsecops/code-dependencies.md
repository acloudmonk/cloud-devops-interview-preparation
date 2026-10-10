# Source, Code, Dependencies, and Secrets

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Different analysis methods answer different questions. Layer them around threat
and release context instead of requiring every scanner on every commit.

## Assurance methods

| Method | Best question | Important limitation |
| --- | --- | --- |
| SAST | Does source contain risky patterns or flows? | False positives and incomplete runtime context |
| SCA | Which components and known vulnerabilities are present? | Package presence does not prove reachability or exploitability |
| Secret scanning | Did a credential-like value enter source or history? | Detection follows exposure; custom formats may be missed |
| DAST | How does a running interface behave to external probes? | Limited internal visibility and environment coverage |
| IAST/fuzzing | What emerges during instrumented or generated execution? | Harness, coverage, and operational cost |
| Manual review | Are business logic and design assumptions safe? | Skill, time, and consistency |

## Source controls

Protect branches, require attributable reviews, minimize administrator bypass,
verify commit/workflow changes, separate code owner from release authority, and
audit token and deploy-key use. High-risk pipeline and policy files deserve
special ownership and review.

## Dependency discipline

Use declared dependencies, lock files, trusted registries, integrity verification,
minimal scopes, automated update proposals, provenance where available, and an
owner for exceptions. Protect against dependency confusion with namespace and
registry policy. Inventory direct and transitive components.

An SBOM is an inventory artifact, not proof that dependencies are safe or used.

## Secret response

When a secret is detected:

1. revoke or rotate it first;
2. identify scope, permissions, use, and exposure window;
3. preserve audit evidence and investigate access;
4. remove it from current source and history when appropriate;
5. replace the delivery pattern with runtime retrieval and short-lived identity;
6. add detection for that format and verify revocation.

Deleting the string from the latest commit is not containment.

## Finding workflow

Normalize, deduplicate, map to the exact component and artifact, enrich with
reachability/exposure/asset context, assign one owner, set a risk-based due date,
track exception evidence, and verify the deployed fix. Measure age and exposure,
not total findings created.

Return to the [module overview](index.md) when ready to continue.
