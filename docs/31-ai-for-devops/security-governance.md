# Security, Safety, and Governance

[← AIOps and incident assistance](aiops-incident-automation.md) · [Next: Observability, cost, and sustainability →](observability-cost.md)

## Threat model the whole system

Assets include prompts, documents, embeddings, model weights, tool credentials,
outputs, feedback, evaluation data, and audit trails. Threats include prompt
injection, data poisoning, disclosure, excessive agency, insecure output handling,
denial of wallet, supply-chain compromise, and tenant boundary failure.

## Control layers

- classify and minimize input; redact secrets and regulated data before inference;
- use private connectivity and encryption where risk requires it;
- separate user, application, retrieval, model, and tool identities;
- authorize retrieval and every tool call outside the model;
- validate structured input/output and encode before downstream use;
- apply safety filters as defense in depth, not the only security boundary;
- log decisions with privacy-aware sampling and restricted access;
- red-team misuse, indirect injection, exfiltration, and resource exhaustion;
- maintain kill switches, incident response, notification, and deletion paths.

## Governance lifecycle

Use NIST AI RMF's Govern, Map, Measure, and Manage functions as a durable frame.
Maintain inventory, owner, purpose, affected users, data lineage, risk tier, model
and supplier record, evaluation evidence, exceptions, incidents, and retirement.
Obligations vary by jurisdiction and use; architecture must support evidence rather
than claim compliance from a service badge.

## Supply chain, privacy, and responsibility

Review model licenses, provider retention, region processing, subprocessors, SDKs,
containers, adapters, and datasets. Sign and scan artifacts, pin dependencies, and
verify provenance. Avoid full prompt/output capture when it includes credentials,
personal data, customer content, or incident details. The model may propose;
deterministic systems authorize, and accountable owners remain responsible.
