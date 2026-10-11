# Use Cases and Operating Model

[← AI systems decision model](concepts.md) · [Next: Foundation-model architecture →](foundation-model-architecture.md)

## Prioritize bounded value

Score candidates by frequency, time saved, decision quality, data readiness,
detectability of error, reversibility, and blast radius. Good first uses include
runbook search, incident chronology, ticket classification, change summarization,
query generation with review, and postmortem drafting. Poor first uses include
autonomous production mutation, access approval, compliance attestation, or final
root-cause declaration.

Use a deterministic baseline. Compare the AI-assisted workflow against current
time-to-answer, acceptance rate, escalation rate, false action rate, operator
effort, and cost per successful task. A demo without a baseline is not a business
case.

## Product ownership

| Role | Accountability |
| --- | --- |
| Product owner | Outcome, users, acceptable harm, adoption, retirement |
| Domain owner/SRE | Runbooks, operational truth, action boundary, incident process |
| AI/platform team | Gateway, retrieval, evaluation, telemetry, quotas, paved road |
| Security/privacy | Threat model, data classification, testing, exception process |
| Model/data owner | Provenance, licensing, quality, version, retention, deletion |

Create a system card recording intended and prohibited uses, data classes, model
and prompt versions, evaluation thresholds, known limitations, human escalation,
and owner. Review it on material model, data, tool, or policy changes.

## Human control

Human-in-the-loop is a designed control, not a button added later. Present source
citations, assumptions, proposed parameters, impact preview, and rollback. Prevent
approval fatigue with risk tiers: low-risk read-only assistance may be automatic;
privilege, deletion, traffic, or data changes need explicit authorization.

## Adoption and failure

Start with shadow mode, then advisory mode, limited users, bounded actions, and
progressive expansion. Preserve a non-AI path for provider outage, quota exhaustion,
unsafe output, or loss of trust. Measure whether operators over-trust or routinely
ignore recommendations; both are control failures.
