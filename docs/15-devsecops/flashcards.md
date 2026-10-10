# DevSecOps Active-Recall Flashcards

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

| Prompt | Answer cue |
| --- | --- |
| Seven-part model | outcome → threat → control → trust → evidence → decision → feedback |
| Threat model | architecture plus abuse paths converted into owned controls, tests, and residual risk |
| Layered assurance | early feedback plus independent build, release, admission, and runtime evidence |
| Finding versus risk | evidence enriched with exploitability, reachability, exposure, asset, and controls |
| SAST boundary | code-pattern/flow evidence without complete runtime context |
| SCA boundary | component/vulnerability presence without automatic exploitability proof |
| Secret incident | revoke first; investigate use; rotate; redesign to short-lived retrieval |
| Protected build | reviewed source, isolated runner, pinned inputs, scoped identity, immutable evidence |
| Runner invariant | untrusted code cannot access protected secrets, authority, tenants, or persistence |
| Digest | byte identity only; no origin or safety guarantee |
| Signature | signer/integrity assertion evaluated against trusted identity policy |
| SBOM | artifact-bound component inventory used for exposure queries and response |
| Provenance | signed evidence connecting artifact to source, builder, inputs, and parameters |
| Attestation | signed claim with predicate whose meaning and producer must be trusted |
| SLSA | progressive source/build integrity requirements, not total product security |
| Keyless signing | ephemeral key plus short-lived identity certificate and transparency evidence |
| Promotion | move same digest and evidence; record environment decision separately |
| Image admission | verify immutable digest, expected producer/provenance, evidence, and exception |
| Policy rollout | observe → advise → fix paved path → enforce changed/new → retire legacy |
| Exception | scoped, owned, justified, compensated, observable, expiring, and remediated |
| IaC remediation | update authoritative source; emergency contain then reconcile source/state |
| Vulnerability priority | exploitation + reachability + exposure + privilege + asset + impact |
| Fix proof | rebuilt fixed digest deployed; vulnerable artifact removed or isolated |
| Supply-chain containment | stop release, revoke, preserve, enumerate artifacts/consumers, quarantine, rebuild |
| Leadership outcome | reduced deployed exposure and recovery time without unsafe delivery friction |

Review missed cards after one day, three days, and seven days.

Return to the [module overview](index.md) when ready to continue.
