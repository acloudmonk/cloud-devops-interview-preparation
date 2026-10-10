# CI/CD References and Videos

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last verified: **2026-10-10**

Prefer official product and specification documentation for behavior that changes.
The module teaches portable invariants; use these sources to confirm current syntax,
limits, permissions, and service availability before implementation.

## GitHub Actions

- [Understanding GitHub Actions](https://docs.github.com/actions/about-github-actions/understanding-github-actions)
  — workflows, events, jobs, actions, runners, and delivery vocabulary.
- [Workflow syntax](https://docs.github.com/actions/reference/workflows-and-actions/workflow-syntax)
  — triggers, permissions, concurrency, jobs, environments, and expressions.
- [Secure use reference](https://docs.github.com/actions/reference/security/secure-use)
  — untrusted input, tokens, third-party actions, OIDC, runners, and supply-chain controls.
- [Configure OIDC in AWS](https://docs.github.com/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-aws)
  — short-lived GitHub-to-AWS workload identity and trust-policy guidance.
- [OpenID Connect reference](https://docs.github.com/actions/reference/security/oidc)
  — issuer, token claims, subject formats, and reusable-workflow considerations.
- [Managing deployment environments](https://docs.github.com/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments)
  — protection rules, secrets, branch/tag restrictions, and environment history.
- [Store and share data with workflow artifacts](https://docs.github.com/actions/how-tos/writing-workflows/choosing-what-your-workflow-does/storing-and-sharing-data-from-a-workflow)
  — artifact upload, download, identity, and retention.
- [Dependency caching reference](https://docs.github.com/actions/reference/workflows-and-actions/dependency-caching)
  — cache matching, access, eviction, and current security guidance.
- [Reuse workflows](https://docs.github.com/actions/how-tos/sharing-automations/reusing-workflows)
  — organization-scale workflow interfaces and permission behavior.

## AWS delivery anchor

- [AWS CodePipeline concepts](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts.html)
  — stages, actions, transitions, executions, and artifacts.
- [CodeDeploy deployment configurations](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html)
  — EC2 minimum-health, Lambda, and ECS traffic-shift behavior.
- [Amazon ECS deployment types](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html)
  — rolling, blue/green, external, and platform-specific considerations.
- [Amazon ECS blue/green deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-bluegreen.html)
  — target groups, lifecycle hooks, test traffic, and traffic shifting.
- [Amazon ECS canary deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/canary-deployment.html)
  — phased exposure, hooks, bake time, and cleanup.
- [AWS Lambda aliases](https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html)
  — stable names and weighted routing across immutable function versions.
- [AWS AppConfig deployment strategies](https://docs.aws.amazon.com/appconfig/latest/userguide/deployment-strategies.html)
  — controlled configuration rollout, growth, bake time, and rollback signals.
- [IAM roles for GitHub Actions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html)
  — AWS-side OIDC provider, trust, and role configuration.

## Supply-chain evidence and measurement

- [SLSA specification](https://slsa.dev/spec/)
  — supply-chain levels, build track, provenance model, and verification.
- [Sigstore documentation](https://docs.sigstore.dev/)
  — signing, identity, transparency, policy, and Cosign workflows.
- [SPDX specification](https://spdx.github.io/spdx-spec/)
  — standardized software-bill-of-materials data and relationships.
- [CycloneDX specification](https://cyclonedx.org/specification/overview/)
  — BOM models for components, services, vulnerabilities, and attestations.
- [DORA guides](https://dora.dev/guides/)
  — delivery-performance measurement and evidence-based improvement.

## Platform translations

- [GitLab pipeline architecture](https://docs.gitlab.com/ci/pipelines/pipeline_architectures/)
  — basic, DAG, parent-child, and multi-project designs.
- [GitLab pipeline types](https://docs.gitlab.com/ci/pipelines/pipeline_types/)
  — branch, tag, merge request, merged-results, and merge-train pipelines.
- [Azure Pipelines approvals and checks](https://learn.microsoft.com/azure/devops/pipelines/process/approvals)
  — resource-owned approval, branch, artifact, monitoring, and lock controls.
- [Azure workload identity federation](https://learn.microsoft.com/azure/devops/pipelines/release/configure-workload-identity)
  — secret-free Azure service connections for pipeline workloads.
- [Jenkins Pipeline handbook](https://www.jenkins.io/doc/book/pipeline/)
  — Jenkinsfile, agents, stages, shared libraries, and pipeline syntax.
- [Securing Jenkins](https://www.jenkins.io/doc/book/security/)
  — controller isolation, build access, credentials, environment, and content risks.
- [Argo Rollouts concepts](https://argo-rollouts.readthedocs.io/en/stable/concepts/)
  — rolling, blue/green, canary, traffic routing, and progressive delivery.
- [Argo Rollouts analysis](https://argo-rollouts.readthedocs.io/en/stable/features/analysis/)
  — metric analysis, baselines, promotion, pause, and abort behavior.

## Video

- [Securely deploy to AWS with GitHub Actions and OIDC](https://www.youtube.com/watch?v=Io5UFJlEJKc)
  — official GitHub walkthrough of federated AWS access. Use current GitHub and AWS
  documentation to validate every claim and policy before production use.

Official channels for newer material:

- [GitHub](https://www.youtube.com/@GitHub)
- [AWS Events](https://www.youtube.com/@AWSEventsChannel)
- [GitLab](https://www.youtube.com/@GitLab)
- [Microsoft Developer](https://www.youtube.com/@MicrosoftDeveloper)
- [CNCF](https://www.youtube.com/@cncf)

## Books

- Jez Humble and David Farley, *Continuous Delivery*
- Dave Farley, *Continuous Delivery Pipelines*
- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate*
- Gene Kim, Jez Humble, Patrick Debois, and John Willis, *The DevOps Handbook*
- Steve McConnell, *Software Estimation* (useful for uncertainty and delivery decisions)

Check edition, publication date, and supported platform versions before purchasing.

## Suggested reading order

1. GitHub Actions concepts, syntax, secure use, OIDC, and environments
2. AWS CodePipeline/CodeDeploy/ECS/Lambda/AppConfig deployment behavior
3. SLSA, Sigstore, SBOM specifications, and DORA measurement guidance
4. GitLab, Azure Pipelines, Jenkins, and Argo Rollouts translations
5. Official video and selected book chapters for deeper practice
