# Python Automation References

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Verify supported Python/runtime, SDK behavior, API quotas, retry defaults, credentials,
pricing, and Region support in current documentation before production decisions.

## Core reading order

1. [Python tutorial](https://docs.python.org/3/tutorial/)
2. [Python standard library](https://docs.python.org/3/library/)
3. [Python packaging user guide](https://packaging.python.org/)
4. [Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
5. [pytest documentation](https://docs.pytest.org/en/stable/)

## Language and runtime

- [Python typing](https://docs.python.org/3/library/typing.html)
- [Python logging](https://docs.python.org/3/library/logging.html)
- [Python asyncio](https://docs.python.org/3/library/asyncio.html)
- [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)
- [Python exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Python virtual environments](https://docs.python.org/3/library/venv.html)
- [pyproject.toml specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/)

## AWS anchor

- [Boto3 credentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html)
- [Boto3 configuration and retries](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html)
- [Boto3 paginators](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/paginators.html)
- [Boto3 waiters](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/clients.html#waiters)
- [AWS Lambda Python](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html)
- [AWS Lambda best practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)
- [Powertools for AWS Lambda Python](https://docs.aws.amazon.com/powertools/python/latest/)

## Azure and Google Cloud translation

- [Azure SDK for Python](https://learn.microsoft.com/azure/developer/python/sdk/azure-sdk-overview)
- [Authenticate Python apps to Azure](https://learn.microsoft.com/azure/developer/python/sdk/authentication/overview)
- [Google Cloud client libraries](https://cloud.google.com/python/docs/reference)
- [Google Application Default Credentials](https://cloud.google.com/docs/authentication/application-default-credentials)
- [Google API Core retry](https://googleapis.dev/python/google-api-core/latest/retry.html)

## Testing, quality, and security

- [unittest.mock](https://docs.python.org/3/library/unittest.mock.html)
- [Hypothesis documentation](https://hypothesis.readthedocs.io/)
- [mypy documentation](https://mypy.readthedocs.io/)
- [Ruff documentation](https://docs.astral.sh/ruff/)
- [Bandit documentation](https://bandit.readthedocs.io/)
- [OpenTelemetry Python](https://opentelemetry.io/docs/languages/python/)

## Video discovery channels

- [PyCon US](https://www.youtube.com/@PyConUS)
- [AWS Events](https://www.youtube.com/@AWSEventsChannel)
- [Microsoft Developer](https://www.youtube.com/@MicrosoftDeveloper)
- [Google Cloud Tech](https://www.youtube.com/@googlecloudtech)

## Books for deeper study

- *Effective Python* by Brett Slatkin
- *Fluent Python* by Luciano Ramalho
- *Architecture Patterns with Python* by Harry Percival and Bob Gregory
- *Robust Python* by Patrick Viafore

Use books for durable design and official documentation for current language, SDK,
runtime, identity, and service behavior.

## Suggested review loop

1. Learn language/data boundaries and structure a pure planning core.
2. Study Boto3 credentials, pagination, configuration, retries, and waiters.
3. Translate one workflow to Azure and Google without hiding native semantics.
4. Test timeout-after-success, throttling, denial, partial failure, resume, and dry run.
5. Use video for a weak concept, then verify details in the primary written source.
6. Return to scenarios and explain authority, state, blast radius, proof, and recovery.

Return to the [module overview](index.md) when ready to continue.
