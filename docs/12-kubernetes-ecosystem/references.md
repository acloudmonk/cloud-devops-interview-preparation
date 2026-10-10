# Kubernetes Ecosystem References and Videos

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Last verified: **2026-10-10**

Ecosystem projects and managed-cloud integrations change faster than the Kubernetes
core. Prefer the current version of primary documentation, verify the support matrix,
and test upgrade and removal paths before making a production decision.

## Packaging and customization

- [Helm documentation](https://helm.sh/docs/)
  — chart structure, dependencies, lifecycle, security, and command behavior.
- [Helm chart best practices](https://helm.sh/docs/chart_best_practices/)
  — conventions for values, templates, labels, dependencies, and maintainable charts.
- [Helm charts and CRDs](https://helm.sh/docs/topics/charts/)
  — chart composition and the special install/upgrade behavior of CRDs.
- [Kustomize in Kubernetes](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/)
  — bases, overlays, generators, patches, and native `kubectl` integration.
- [Declarative object management](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/)
  — apply semantics, field ownership, pruning, and management-method boundaries.

## GitOps and reconciliation

- [OpenGitOps principles](https://opengitops.dev/)
  — vendor-neutral principles for declarative, versioned, pulled, and reconciled state.
- [Argo CD architecture](https://argo-cd.readthedocs.io/en/stable/operator-manual/architecture/)
  — API server, repository server, application controller, cache, and reconciliation roles.
- [Argo CD security](https://argo-cd.readthedocs.io/en/stable/operator-manual/security/)
  — threat model, authentication, authorization, credentials, and supply-chain controls.
- [Flux documentation](https://fluxcd.io/flux/)
  and [core concepts](https://fluxcd.io/flux/concepts/)
  — source, Kustomize, Helm, notification, image-automation, and tenancy controllers.
- [Flux from end to end](https://fluxcd.io/flux/flux-e2e/)
  — the artifact and reconciliation path from source revision to cluster state.

## Networking, eBPF, Gateway API, and service mesh

- [Kubernetes network model](https://kubernetes.io/docs/concepts/services-networking/)
  and [NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
  — portable contracts that a selected CNI and policy implementation must satisfy.
- [CNI specification](https://www.cni.dev/docs/spec/)
  — the runtime-to-network-plugin contract and result semantics.
- [Cilium documentation](https://docs.cilium.io/en/stable/)
  and [AWS VPC CNI chaining](https://docs.cilium.io/en/stable/installation/cni-chaining-aws-cni/)
  — eBPF data-plane capabilities and an EKS-specific integration model.
- [Gateway API introduction](https://gateway-api.sigs.k8s.io/docs/introduction/)
  and [API overview](https://gateway-api.sigs.k8s.io/docs/concepts/api-overview/)
  — role-oriented routing resources, attachment, status, and portability goals.
- [Gateway API conformance](https://gateway-api.sigs.k8s.io/guides/implementers-guide/)
  — version-specific implementation profiles and evidence for supported features.
- [Gateway API for service mesh](https://gateway-api.sigs.k8s.io/docs/mesh/mesh-overview/)
  — east-west route attachment and the GAMMA initiative.
- [Istio architecture](https://istio.io/latest/docs/ops/deployment/architecture/)
  and [Gateway API support](https://istio.io/latest/docs/tasks/traffic-management/ingress/gateway-api/)
  — mesh control/data planes and standards-based traffic configuration.
- [Linkerd architecture](https://linkerd.io/2/features/architecture/)
  and [Gateway API support](https://linkerd.io/2/features/gateway-api/)
  — a contrasting mesh architecture and its use of Gateway API resources.

## Autoscaling and capacity

- [Kubernetes workload autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/)
  and [Horizontal Pod Autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)
  — horizontal, vertical, custom/external metric, and control-loop behavior.
- [KEDA scaling concepts](https://keda.sh/docs/latest/concepts/scaling-deployments/)
  and [scalers](https://keda.sh/docs/latest/scalers/)
  — event activation, HPA integration, scale-to-zero, and supported event sources.
- [Karpenter concepts](https://karpenter.sh/docs/concepts/)
  and [reference](https://karpenter.sh/docs/reference/)
  — node provisioning, disruption, scheduling inputs, limits, metrics, and security.
- [EKS compute autoscaling](https://docs.aws.amazon.com/eks/latest/userguide/autoscaling.html)
  and [Karpenter best practices](https://docs.aws.amazon.com/eks/latest/best-practices/karpenter.html)
  — EKS Auto Mode, Karpenter, Cluster Autoscaler, ownership, and operational trade-offs.

## Policy, secrets, and certificates

- [Kubernetes admission controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/)
  and [Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/)
  — built-in validation, enforcement modes, exemptions, and failure implications.
- [Kyverno policy types](https://kyverno.io/docs/policy-types/)
  and [applying policies](https://kyverno.io/docs/guides/applying-policies/)
  — validation, mutation, generation, image verification, audit, and pipeline checks.
- [OPA for Kubernetes admission](https://www.openpolicyagent.org/docs/kubernetes)
  and [Gatekeeper documentation](https://open-policy-agent.github.io/gatekeeper/website/docs/)
  — Rego-based constraints, templates, admission, and audit.
- [Kubernetes Secrets good practices](https://kubernetes.io/docs/concepts/security/secrets-good-practices/)
  — storage, encryption, least privilege, access, and lifecycle fundamentals.
- [External Secrets Operator](https://external-secrets.io/latest/)
  and [ExternalSecret API](https://external-secrets.io/latest/api/externalsecret/)
  — provider-backed synchronization, refresh, ownership, and deletion behavior.
- [Secrets Store CSI Driver](https://secrets-store-csi-driver.sigs.k8s.io/)
  — node-mounted external secrets, providers, rotation, and optional Secret synchronization.
- [cert-manager documentation](https://cert-manager.io/docs/)
  and [Certificate resource](https://cert-manager.io/docs/usage/certificate/)
  — issuers, requests, renewal, private-key handling, and workload delivery.

## Operators, CRDs, and add-on lifecycle

- [Kubernetes operator pattern](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)
  — custom-resource control loops and the operational knowledge they encode.
- [Custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
  — when to extend the API, coupling, access, storage, and controller considerations.
- [CRD versioning](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/)
  — served/stored versions, conversion, migration, and removal safety.
- [Kubernetes API deprecation policy](https://kubernetes.io/docs/reference/using-api/deprecation-policy/)
  — lifecycle guarantees that constrain cluster and ecosystem upgrades.
- [Amazon EKS add-ons](https://docs.aws.amazon.com/eks/latest/userguide/eks-add-ons.html)
  and [available AWS add-ons](https://docs.aws.amazon.com/eks/latest/userguide/workloads-add-ons-available-eks.html)
  — managed/self-managed ownership, compatibility, configuration, and support boundaries.

## Amazon EKS anchor

- [EKS Best Practices Guide](https://docs.aws.amazon.com/eks/latest/best-practices/introduction.html)
  — the primary AWS operating baseline for reliability, security, scale, and cost.
- [EKS networking best practices](https://docs.aws.amazon.com/eks/latest/best-practices/networking.html)
  and [network security](https://docs.aws.amazon.com/eks/latest/best-practices/network-security.html)
  — VPC CNI, address capacity, policy, segmentation, and traffic visibility.
- [EKS cluster autoscaling best practices](https://docs.aws.amazon.com/eks/latest/best-practices/cluster-autoscaling.html)
  — Cluster Autoscaler, Karpenter, and EKS Auto Mode guidance.
- [EKS workload identities](https://docs.aws.amazon.com/eks/latest/userguide/service-accounts.html)
  — EKS Pod Identity and IAM roles for service accounts.
- [AWS Secrets Store CSI Driver provider](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_csi_driver.html)
  — Secrets Manager and Parameter Store delivery into EKS Pods.
- [EKS cluster upgrades](https://docs.aws.amazon.com/eks/latest/best-practices/cluster-upgrades.html)
  — API, add-on, controller, and data-plane compatibility planning.

## AKS and GKE translation

- [AKS GitOps with Flux](https://learn.microsoft.com/azure/azure-arc/kubernetes/conceptual-gitops-flux2)
  — Azure's managed Flux extension and configuration model for AKS and Arc.
- [AKS Azure Policy](https://learn.microsoft.com/azure/governance/policy/concepts/policy-for-kubernetes)
  — Gatekeeper-based governance across AKS and connected clusters.
- [AKS Key Vault CSI integration](https://learn.microsoft.com/azure/aks/csi-secrets-store-driver)
  — managed Secrets Store CSI add-on, identity, rotation, and limitations.
- [AKS node autoscaling](https://learn.microsoft.com/azure/aks/cluster-autoscaler-overview)
  — managed Cluster Autoscaler ownership and operational guidance.
- [GKE Config Sync](https://cloud.google.com/kubernetes-engine/config-sync/docs/overview)
  — Google's fleet-oriented GitOps configuration and policy synchronization service.
- [GKE Policy Controller](https://cloud.google.com/kubernetes-engine/enterprise/policy-controller/docs/overview)
  — managed Gatekeeper constraints, audit, and policy bundles.
- [GKE workload autoscaling](https://cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler)
  and [cluster autoscaling](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler)
  — Google-managed workload and node scaling behavior.
- [GKE Secret Manager add-on](https://cloud.google.com/secret-manager/docs/secret-manager-managed-csi-component)
  — managed CSI-based secret access and workload identity integration.

## Videos

- [AWS re:Invent 2024 — How to build scalable platforms with Amazon EKS](https://www.youtube.com/watch?v=WkPrmHKZsq4)
  — official AWS Events session on platform capabilities, scale, and operating patterns.
- [AWS re:Invent 2023 — Platform engineering with Amazon EKS](https://www.youtube.com/watch?v=eLxBnGoBltc)
  — official AWS Events session on platform-team architecture and developer enablement.

Official channels for newer, version-aware material:

- [Kubernetes](https://www.youtube.com/@KubernetesCommunity)
- [Cloud Native Computing Foundation](https://www.youtube.com/@cncf)
- [AWS Events](https://www.youtube.com/@AWSEventsChannel)
- [Argo Project](https://www.youtube.com/@argoproj)
- [Microsoft Developer](https://www.youtube.com/@MicrosoftDeveloper)
- [Google Cloud Tech](https://www.youtube.com/@googlecloudtech)

## Books

- Kief Morris, *Infrastructure as Code* — declarative systems, testing, change, and
  operational design; translate examples to Kubernetes controller ownership.
- Cornelia Davis, *Cloud Native Patterns* — distributed-system and platform patterns
  behind many ecosystem choices.
- Bilgin Ibryam and Roland Huß, *Kubernetes Patterns* — reusable application and
  controller patterns; verify all APIs against current Kubernetes documentation.
- Billy Yuen, Alexander Matyushentsev, Todd Ekenstam, and Jesse Suen,
  *GitOps and Kubernetes* — GitOps design and operating models; validate product details
  against current Argo CD and Flux documentation.

Check edition, Kubernetes version, product maturity, and managed-service assumptions
before purchasing or following commands.

## Suggested reading order

1. OpenGitOps principles, Kubernetes declarative management, and controller ownership
2. Helm/Kustomize and one GitOps controller's architecture and security model
3. CNI, Gateway API, service mesh, scaling, admission, secrets, and certificates
4. CRD/operator lifecycle, EKS add-ons, upgrades, and removal planning
5. AKS/GKE translations, official talks, and selected book chapters
