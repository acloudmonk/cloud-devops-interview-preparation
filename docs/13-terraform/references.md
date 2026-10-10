# Terraform and OpenTofu References

Use this page as a curated follow-up list, not as a requirement to read every
link before continuing. Start with the core reading, then choose material that
supports a weak area discovered in the scenarios or mock interview.

## Core reading order

1. Read the [Terraform overview](https://developer.hashicorp.com/terraform/docs)
   and [core workflow](https://developer.hashicorp.com/terraform/intro/core-workflow).
2. Study [Terraform state](https://developer.hashicorp.com/terraform/language/state)
   and [backend configuration](https://developer.hashicorp.com/terraform/language/backend).
3. Review the [AWS Provider best-practices guide](https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/introduction.html).
4. Read the [OpenTofu language documentation](https://opentofu.org/docs/language/)
   and [migration guide](https://opentofu.org/docs/intro/migration/).
5. Return to the specialized sections below when preparing a design answer.

## Terraform language and workflow

- [Terraform documentation](https://developer.hashicorp.com/terraform/docs)
- [Core workflow](https://developer.hashicorp.com/terraform/intro/core-workflow)
- [Modules overview](https://developer.hashicorp.com/terraform/language/modules)
- [Developing reusable modules](https://developer.hashicorp.com/terraform/language/modules/develop)
- [Refactoring modules with moved blocks](https://developer.hashicorp.com/terraform/language/modules/develop/refactoring)
- [Import existing resources](https://developer.hashicorp.com/terraform/language/import)
- [Import block reference](https://developer.hashicorp.com/terraform/language/block/import)
- [Terraform test](https://developer.hashicorp.com/terraform/cli/test)
- [Dependency lock file](https://developer.hashicorp.com/terraform/language/files/dependency-lock)
- [Terraform style guide](https://developer.hashicorp.com/terraform/language/style)

## State and backends

- [State overview](https://developer.hashicorp.com/terraform/language/state)
- [Purpose of state](https://developer.hashicorp.com/terraform/language/state/purpose)
- [Backend overview](https://developer.hashicorp.com/terraform/language/backend)
- [S3 backend](https://developer.hashicorp.com/terraform/language/backend/s3)
- [AWS guidance for Terraform backends](https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/backend.html)

The current S3 backend documentation supports lock files with
`use_lockfile = true`. DynamoDB-based locking is deprecated, so describe it as
a legacy pattern when it appears in an interview or an existing platform.

## Automation, governance, and managed Terraform

- [Automate Terraform](https://developer.hashicorp.com/terraform/tutorials/automation/automate-terraform)
- [HCP Terraform overview](https://developer.hashicorp.com/terraform/cloud-docs/overview)
- [HCP Terraform run tasks](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/settings/run-tasks)
- [Terraform Stacks](https://developer.hashicorp.com/terraform/language/stacks)
- [AWS security best practices](https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/security.html)
- [AWS repository-structure guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/structure.html)

## OpenTofu

- [OpenTofu language documentation](https://opentofu.org/docs/language/)
- [State](https://opentofu.org/docs/language/state/)
- [Backends](https://opentofu.org/docs/language/state/backends/)
- [Remote state](https://opentofu.org/docs/language/state/remote/)
- [Remote-state data considerations](https://opentofu.org/docs/language/state/remote-state-data/)
- [State and plan encryption](https://opentofu.org/docs/language/state/encryption/)
- [Modules](https://opentofu.org/docs/language/modules/)
- [Providers](https://opentofu.org/docs/language/providers/)
- [Migrate from Terraform](https://opentofu.org/docs/intro/migration/)
- [Migrate interdependent configurations](https://opentofu.org/docs/intro/migration/multiple-configurations/)
- [OpenTofu general-availability announcement](https://opentofu.org/blog/opentofu-is-going-ga/)

Do not treat Terraform and OpenTofu as permanently interchangeable. Verify
provider compatibility, state format, backend behavior, automation integration,
and rollback before a migration.

## AWS anchor and multi-cloud translation

### AWS

- [Terraform on AWS Provider best practices](https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/introduction.html)
- [AWS IaC tool-selection guide](https://docs.aws.amazon.com/prescriptive-guidance/latest/choose-iac-tool/choose-tool.html)
- [Terraform selection considerations](https://docs.aws.amazon.com/prescriptive-guidance/latest/choose-iac-tool/terraform.html)

### Azure

- [Terraform on Azure](https://learn.microsoft.com/en-us/azure/developer/terraform/)
- [Authenticate Terraform to Azure](https://learn.microsoft.com/en-us/azure/developer/terraform/authenticate/authenticate-to-azure)
- [Store Terraform state in Azure Storage](https://learn.microsoft.com/azure/developer/terraform/store-state-in-azure-storage)

### Google Cloud

- [Terraform general style and structure](https://cloud.google.com/docs/terraform/best-practices/general-style-structure)
- [Root-module best practices](https://cloud.google.com/docs/terraform/best-practices/root-modules)
- [Service-account impersonation](https://cloud.google.com/iam/docs/service-account-impersonation)

Use the Azure and Google Cloud references to translate identity, backend,
organization, and environment decisions. The interview reasoning remains the
same even when the resource names differ.

## Video learning

- [Introduction to Terraform — HashiCorp](https://www.youtube.com/watch?v=ZFLWA1kQ3ls)
- [HashiCorp official channel](https://www.youtube.com/@HashiCorp)
- [AWS Events channel](https://www.youtube.com/@AWSEventsChannel)
- [Microsoft Developer channel](https://www.youtube.com/@MicrosoftDeveloper)
- [Google Cloud Tech channel](https://www.youtube.com/@googlecloudtech)

Prefer official conference sessions and documentation-linked recordings. Check
the publication date because backend behavior, product names, and licensing
context can change.

## Books for deeper study

- *Terraform: Up & Running* by Yevgeniy Brikman
- *Infrastructure as Code* by Kief Morris

Books are useful for principles and design vocabulary, but use current official
documentation for commands, feature availability, and migration constraints.

## Suggested review loop

1. Read one concept page in this module.
2. Explain it without notes in two minutes.
3. Answer a related [scenario](scenarios.md) using evidence and trade-offs.
4. Verify any uncertain product detail in the official references above.
5. Record the gap as a flashcard and repeat it after several days.

Return to the [module overview](index.md) when you are ready to continue the
required path.
