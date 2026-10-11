# Delivery, Artifacts, and Infrastructure as Code

[← Integration](integration.md) · [Next: Operations →](operations.md)

Common delivery intent can coexist with provider-native implementations.

| Capability | AWS | Azure | Google Cloud |
| --- | --- | --- | --- |
| Native IaC | CloudFormation/CDK | ARM/Bicep | Infrastructure Manager / Config Connector patterns |
| Cross-cloud IaC | Terraform/OpenTofu | Terraform/OpenTofu | Terraform/OpenTofu |
| Artifact registry | ECR/CodeArtifact | Azure Container Registry/Artifacts | Artifact Registry |
| Native pipeline family | CodePipeline/Build/Deploy | Azure DevOps/GitHub Actions | Cloud Build/Deploy |

Standardize source controls, review, identity federation, signed immutable artifacts,
provenance, scanning, policy intent, promotion evidence, rollback, and change metrics.
Keep provider adapters where APIs and semantics differ.

Separate build, deployment, and runtime identities. Prefer short-lived federation from
CI systems. Pin modules/providers/actions, review generated plans, serialize state
where required, detect drift, and test policy before enforcement.

A single giant cross-cloud module creates coupling and lowest-common-denominator
design. Prefer small versioned modules with common interfaces only where the underlying
capability is truly stable, plus explicit provider implementations and conformance tests.
