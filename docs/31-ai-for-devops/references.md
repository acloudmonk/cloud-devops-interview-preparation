# AI for Cloud and DevOps References

[← Active-recall flashcards](flashcards.md) · [Module overview](index.md)

AI services, models, quotas, Regions, prices, and data terms change quickly. Verify
current primary documentation before any production recommendation.

## Suggested reading order

1. [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
2. [NIST Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1)
3. [AWS Generative AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html)
4. [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)
5. [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)

## AWS architecture anchor

- [Amazon Bedrock security and privacy](https://docs.aws.amazon.com/bedrock/latest/userguide/security.html)
- [Amazon Bedrock model evaluation](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html)
- [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)
- [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
- [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html)
- [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)
- [AWS responsible AI policy](https://aws.amazon.com/machine-learning/responsible-ai/policy/)
- [AWS AI service cards](https://aws.amazon.com/ai/responsible-ai/resources/)

## Azure and Google Cloud translation

- [Microsoft Foundry documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Generative AI observability in Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/concepts/observability)
- [Responsible AI in Azure workloads](https://learn.microsoft.com/azure/well-architected/ai/responsible-ai)
- [Google Cloud Vertex AI generative AI](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
- [Vertex AI evaluation](https://cloud.google.com/vertex-ai/generative-ai/docs/models/evaluation-overview)
- [Vertex AI RAG Engine](https://cloud.google.com/vertex-ai/generative-ai/docs/rag-overview)
- [Google Secure AI Framework](https://saif.google/)

## Security, operations, and standards

- [NIST AI RMF Playbook](https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-playbook)
- [NIST secure software practices for generative AI](https://doi.org/10.6028/NIST.SP.800-218A)
- [MITRE ATLAS](https://atlas.mitre.org/)
- [OpenTelemetry generative AI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/)
- [Kubernetes scheduling GPUs](https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/)
- [FinOps Framework: AI](https://www.finops.org/framework/capabilities/ai/)

## Video sources

- [AWS Events channel](https://www.youtube.com/@AWSEventsChannel)
- [Microsoft Mechanics channel](https://www.youtube.com/@MicrosoftMechanicsSeries)
- [Google Cloud Tech channel](https://www.youtube.com/@googlecloudtech)
- [NIST channel](https://www.youtube.com/@NIST)

Use video to build intuition, then confirm service behavior and controls in the
current written primary source.

## Books for deeper study

- *Designing Machine Learning Systems* by Chip Huyen
- *AI Engineering* by Chip Huyen
- *Designing Data-Intensive Applications* by Martin Kleppmann
- *Site Reliability Engineering* by Betsy Beyer and others

Use books for durable systems reasoning; use primary documentation for current
model, platform, security, pricing, quota, and regional details.

## Suggested review loop

1. Map one use case to value, harm, evidence, autonomy, and fallback.
2. Draw its identity, data, retrieval, model, tool, and approval boundaries.
3. Build a small evaluation matrix covering quality, safety, operations, and cost.
4. Translate the AWS design to Azure and Google, recording material differences.
5. Red-team injection, disclosure, excessive agency, and denial-of-wallet paths.
6. Return to the scenarios and explain the decision without product-name dumping.
