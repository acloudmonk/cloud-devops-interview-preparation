# Packaging and Customization: Helm and Kustomize

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last reviewed: **2026-10-10**

Helm packages and renders parameterized templates; Kustomize transforms declarative
resources through composition and patches. Both can be effective. The architecture
question is where abstraction, environment difference, validation, release state, and
ownership should live.

## Helm model

A chart contains templates, default values, metadata, optional dependencies, schema,
tests/hooks, and notes. Rendering combines chart/version, values, capabilities, and
template functions into Kubernetes resources. A Helm release records package and
revision state in the cluster.

Benefits include packaging/versioning, reuse, dependencies, install/upgrade/rollback,
and a distribution ecosystem. Risks include overly programmable templates, huge value
surfaces, unvalidated types, hidden generated names, hook side effects, dependency
drift, sensitive release data, and believing rollback reverses external data/state.

Use values schemas, deterministic rendering, chart/library ownership, immutable
dependencies, rendered-manifest review/policy, minimal hooks, and documented upgrade/
rollback semantics. Treat chart templates and plugins as executable supply-chain input.

## Kustomize model

A base declares reusable resources; overlays compose bases and apply targeted patches,
generators, name changes, labels, images, and replacements. It keeps ordinary YAML
visible and avoids a general template language.

Benefits include transparent resources, compositional overlays, and native integration
with Kubernetes tooling. Risks include deep overlay inheritance, brittle path/patch
coupling, generated-name churn, accidental cross-environment drift, and difficulty
expressing higher-level optional structures.

Keep bases cohesive, overlays shallow, environment differences intentional, patches
small and selector-safe, generators deterministic, and rendered output validated.

## Choosing a boundary

| Need | Likely fit | Warning |
| --- | --- | --- |
| Distribute versioned third-party/application package | Helm | Audit values, templates, CRDs, hooks, and dependencies |
| Apply controlled environment overlays to owned resources | Kustomize | Avoid inheritance maze and patching generated internals |
| Offer a small product-facing configuration API | Either behind a platform contract | Do not expose every low-level field as a value |
| Compose Helm output with environment policy | Helm renderer plus Kustomize/GitOps | Define the single source and rendering order |

Do not layer Helm-in-Helm, templates generating Kustomizations generating charts,
or multiple post-renderers without a clear debug/evidence path. Every abstraction
should reduce cognitive load for its users.

## CRDs and lifecycle

Package managers often treat CRDs differently from ordinary resources because safe
upgrade/delete semantics require care. Define who installs/upgrades CRDs, how stored
versions and conversion are handled, and whether uninstall retains CRs/data. Never
assume uninstalling a chart safely deletes external resources or application state.

## Promotion and evidence

Record source revision, chart/base/dependency versions, values/overlays, renderer
version, rendered manifest digest, policy results, target, approval, and observed
reconciliation. Prefer promotion of reviewed configuration intent rather than manual
environment rendering with undocumented inputs.

## Failure diagnosis

Separate template/render error, invalid API/schema, admission rejection, apply/field
ownership conflict, hook failure, controller reconciliation failure, and unhealthy
workload. Preserve rendered manifests and release/source identity before retrying.
