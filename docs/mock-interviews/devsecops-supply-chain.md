# DevSecOps and Software-Supply-Chain Mock Interview

[← Mock interview overview](index.md) ·
[Module 15 overview](../15-devsecops/index.md) ·
[Scenario answer framework](../interview-playbook/scenario-answer-framework.md)

Duration: **50 minutes**

Level: **Senior / Architect**
Primary context: **AWS and EKS with Azure and Google Cloud follow-ups**

## Candidate brief

A regulated enterprise has 500 repositories, persistent shared runners,
long-lived credentials, mutable tags, inconsistent scanners, no reliable
SBOM/provenance, and weak deployed-component visibility. Design its secure
software delivery operating model and migration.

## Interview structure

### 0–5 minutes — Discovery

Ask about assets, adversaries, data, exposure, delivery paths, builders,
identities, artifacts, deployments, regulations, incidents, owners, and recovery.

### 5–15 minutes — Threat and architecture

Map source, dependency, runner, cache, build, registry, signing, deployment,
admission, and runtime trust boundaries. Assign product/platform/security owners.

### 15–25 minutes — Evidence and policy

Design assurance layers, workload identity, protected builds, artifact digests,
SBOMs, provenance, signatures, promotion, verification, release/admission policy,
exceptions, degraded mode, and break-glass.

### 25–35 minutes — Incident branches

Choose two:

1. A shared runner is compromised after publishing production images.
2. A signing identity creates artifacts from an unknown repository.
3. A poisoned dependency reached staging and perhaps production.
4. Admission policy was changed to allow all for several hours.
5. A critical zero-day affects a common base image and build runners.

Contain, preserve evidence, enumerate artifacts/consumers, recover trust, rebuild,
verify deployments, communicate, and prevent recurrence.

### 35–42 minutes — Trade-offs and multi-cloud

Discuss warn versus block, keyless versus managed keys, availability versus
fail-closed policy, scanner breadth versus signal, and common outcomes with AWS,
Azure, and Google Cloud native controls.

### 42–47 minutes — Executive recommendation

Summarize target state, largest risks, migration waves, investment, trade-offs,
and success measures in two minutes.

### 47–50 minutes — Candidate questions

Ask about incidents, regulatory evidence, platform ownership, team incentives,
risk appetite, or the first business outcome to improve.

## Scoring rubric

| Dimension | Expected evidence |
| --- | --- |
| Discovery and threat model | assets, adversaries, trust, abuse paths, assumptions |
| Ownership | accountable product, platform, security, and risk roles |
| Build trust | source, identity, isolation, inputs, credentials, and recovery |
| Artifact assurance | digest, SBOM, provenance, signing, verification, retention |
| Policy and exceptions | context, enforcement, availability, bypass, expiry |
| Incident response | containment, evidence, blast radius, trust recovery, communication |
| Cloud translation | AWS depth with accurate Azure and Google Cloud mapping |
| Adoption and measures | phased rollout, usable paved path, outcomes, feedback |
| Communication | structured decision, trade-offs, and next validation |

Score each 0–4. Maximum: **36**. Scores of 31–36 show strong architect signal;
24–30 are credible with gaps; 17–23 need deeper operating-model reasoning; below
17 should revisit fundamentals and scenarios.

Return to the [module overview](../15-devsecops/index.md) after scoring.
