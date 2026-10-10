# Container and Kubernetes Security

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Container security spans source, build, image, registry, admission, workload,
cluster, node, and runtime. A clean image scan does not prove safe deployment.

## Image controls

Use minimal maintained bases, pinned digests, non-root users, read-only filesystems
where possible, no embedded secrets, declared ownership, predictable package
sources, vulnerability scans, SBOMs, provenance, signatures, and retention policy.
Rebuild regularly so patched dependencies reach artifacts.

Scan the final image, not only source manifests. Distinguish operating-system
packages, language components, copied binaries, and unreachable findings. Record
scanner database/version and artifact digest.

## Registry controls

Separate repositories and promotion rights, prevent mutable production tags,
scan on push and on new intelligence, replicate deliberately, restrict deletion,
log access, retain evidence, and quarantine compromised digests. Protect registry
administration independently from pipeline publication.

## Kubernetes controls

- authenticate workloads with scoped workload identity;
- enforce namespace, RBAC, Pod Security, network, resource, and secret controls;
- admit only approved immutable digests with required evidence;
- protect admission controllers and their policy/configuration;
- monitor drift, privileged actions, unexpected processes, and network behavior;
- keep nodes, control plane, add-ons, and workload supply chains patched.

Admission policy must define exempt system namespaces, bootstrap, disaster
recovery, controller outage, and break-glass. Test fail-open versus fail-closed
behavior against business availability and threat impact.

## Runtime feedback

Runtime observations can validate reachability, exploit attempts, unexpected
behavior, and asset exposure. Feed them into prioritization and threat models.
Runtime detection is not permission to ship known preventable risk without an owner.

## AWS anchor and translation

For ECR/EKS, combine registry scanning, Inspector findings, IAM roles for service
accounts or pod identity, admission controls, Security Hub, GuardDuty signals, and
CloudTrail evidence. Translate to ACR/AKS and Defender on Azure, and Artifact
Registry/GKE, Artifact Analysis, Binary Authorization, and SCC on Google Cloud.

Return to the [module overview](index.md) when ready to continue.
