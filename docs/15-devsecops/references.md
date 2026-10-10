# DevSecOps References and Videos

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Prefer primary standards and official product documentation. Check publication
and product versions before using a control in an interview recommendation.

## Core reading order

1. [NIST Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final)
2. [OWASP Threat Modeling Project](https://owasp.github.io/www-project-threat-modeling/)
3. [SLSA specification](https://slsa.dev/spec/)
4. [Sigstore documentation](https://docs.sigstore.dev/)
5. [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

## Secure development and threat modeling

- [NIST SSDF project](https://csrc.nist.gov/projects/ssdf)
- [OWASP SAMM](https://owaspsamm.org/)
- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
- [OpenSSF Scorecard](https://scorecard.dev/)
- [OpenSSF Best Practices](https://www.bestpractices.dev/)

## Supply-chain evidence

- [SLSA](https://slsa.dev/)
- [SLSA build provenance](https://slsa.dev/spec/v1.0/provenance)
- [in-toto](https://in-toto.io/)
- [Sigstore Cosign](https://docs.sigstore.dev/cosign/)
- [Sigstore keyless signing overview](https://docs.sigstore.dev/cosign/signing/overview/)
- [Sigstore policy controller](https://docs.sigstore.dev/policy-controller/overview/)
- [SPDX](https://spdx.dev/)
- [CycloneDX](https://cyclonedx.org/)

## Vulnerability and container guidance

- [CISA KEV Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [NIST National Vulnerability Database](https://nvd.nist.gov/)
- [FIRST CVSS](https://www.first.org/cvss/)
- [Kubernetes security documentation](https://kubernetes.io/docs/concepts/security/)
- [Kubernetes admission controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/)
- [Kubernetes Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)

## AWS anchor

- [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html)
- [Amazon ECR image scanning](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html)
- [AWS Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html)
- [AWS IAM OIDC federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html)
- [AWS Signer](https://docs.aws.amazon.com/signer/latest/developerguide/Welcome.html)
- [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/welcome.html)

## Azure and Google Cloud translation

- [Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction)
- [Microsoft Defender for DevOps](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-devops-introduction)
- [Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/overview)
- [Google Cloud software supply-chain security](https://cloud.google.com/software-supply-chain-security/docs/overview)
- [Artifact Analysis](https://cloud.google.com/artifact-analysis/docs)
- [Binary Authorization](https://cloud.google.com/binary-authorization/docs)
- [Security Command Center](https://cloud.google.com/security-command-center/docs/concepts-security-command-center-overview)

## Video channels

- [OWASP Foundation](https://www.youtube.com/@OWASPGLOBAL)
- [OpenSSF](https://www.youtube.com/@OpenSSF)
- [Sigstore](https://www.youtube.com/@sigstore)
- [AWS Events](https://www.youtube.com/@AWSEventsChannel)
- [Microsoft Security](https://www.youtube.com/@MicrosoftSecurity)
- [Google Cloud Tech](https://www.youtube.com/@googlecloudtech)

## Books

- *Threat Modeling: Designing for Security* by Adam Shostack
- *Alice and Bob Learn Application Security* by Tanya Janca
- *Securing DevOps* by Julien Vehent

Use books for durable reasoning and current standards/product documentation for
version-specific behavior.

## Suggested review loop

Read one page, explain the threat/control/evidence/decision chain aloud, answer a
[scenario](scenarios.md), verify uncertain behavior in a primary reference, and
record the gap as a flashcard.

Return to the [module overview](index.md) when ready to continue.
