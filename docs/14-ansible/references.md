# Ansible References and Videos

[← Module overview](index.md) · [Master competency map](../master-competency-map.md)

Use this as a curated follow-up list. Prefer current official documentation for
behavior and compatibility; use books and videos for explanation and context.

## Core reading order

1. Read [Getting started with Ansible](https://docs.ansible.com/projects/ansible/latest/getting_started/index.html).
2. Study [inventory](https://docs.ansible.com/projects/ansible/latest/inventory_guide/intro_inventory.html)
   and [variables](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_variables.html).
3. Review the [playbook guide](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks.html).
4. Study [testing strategies](https://docs.ansible.com/projects/ansible/latest/reference_appendices/test_strategies.html).
5. Return to cloud and controller references for the architecture you operate.

## Inventory, variables, and execution

- [Inventory guide](https://docs.ansible.com/projects/ansible/latest/inventory_guide/index.html)
- [Building inventory](https://docs.ansible.com/projects/ansible/latest/inventory_guide/intro_inventory.html)
- [Working with dynamic inventory](https://docs.ansible.com/projects/ansible/latest/inventory_guide/intro_dynamic_inventory.html)
- [Using variables](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_variables.html)
- [Controlling how Ansible behaves: precedence](https://docs.ansible.com/projects/ansible/latest/reference_appendices/general_precedence.html)
- [Ansible configuration settings](https://docs.ansible.com/projects/ansible/latest/reference_appendices/config.html)
- [Playbook keywords](https://docs.ansible.com/projects/ansible/latest/reference_appendices/playbooks_keywords.html)
- [Connection plugin index](https://docs.ansible.com/projects/ansible/latest/collections/index_connection.html)

## Playbooks and reusable content

- [Working with playbooks](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks.html)
- [Handlers](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_handlers.html)
- [Error handling](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_error_handling.html)
- [Blocks](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_blocks.html)
- [Roles](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_reuse_roles.html)
- [Collections](https://docs.ansible.com/projects/ansible/latest/collections_guide/index.html)
- [Collection structure](https://docs.ansible.com/projects/ansible/latest/dev_guide/developing_collections_structure.html)

## Runtime and controller platforms

- [Getting started with execution environments](https://docs.ansible.com/projects/ansible/latest/getting_started_ee/index.html)
- [Building an execution environment](https://docs.ansible.com/projects/ansible/latest/getting_started_ee/build_execution_environment.html)
- [AWX documentation](https://ansible.readthedocs.io/projects/awx/en/latest/)
- [Ansible Runner documentation](https://ansible.readthedocs.io/projects/runner/en/latest/)
- [Ansible Builder documentation](https://ansible.readthedocs.io/projects/builder/en/latest/)

AWX is the upstream project. For a Red Hat Ansible Automation Platform design,
also consult the documentation matching the exact supported product version.

## Security and testing

- [Ansible Vault](https://docs.ansible.com/projects/ansible/latest/vault_guide/vault.html)
- [Encrypting Vault content](https://docs.ansible.com/projects/ansible/latest/vault_guide/vault_encrypting_content.html)
- [Become and privilege escalation](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_privilege_escalation.html)
- [Check and diff mode](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_checkmode.html)
- [Testing strategies](https://docs.ansible.com/projects/ansible/latest/reference_appendices/test_strategies.html)
- [Testing Ansible and collections](https://docs.ansible.com/projects/ansible/latest/dev_guide/testing_running_locally.html)
- [Ansible Lint](https://ansible.readthedocs.io/projects/lint/)
- [Molecule](https://ansible.readthedocs.io/projects/molecule/)

## AWS anchor

- [`amazon.aws` collection](https://docs.ansible.com/projects/ansible/latest/collections/amazon/aws/)
- [EC2 inventory plugin](https://docs.ansible.com/projects/ansible/latest/collections/amazon/aws/aws_ec2_inventory.html)
- [AWS Systems Manager connection plugin](https://docs.ansible.com/projects/ansible/latest/collections/amazon/aws/aws_ssm_connection.html)
- [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html)
- [AWS Systems Manager VPC endpoints](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-create-vpc.html)

Read the SSM connection-plugin requirements carefully. Removing inbound SSH does
not remove controller IAM, SSM Agent, Session Manager plugin, network, S3
transfer, encryption, cleanup, and audit considerations.

## Azure and Google Cloud translation

- [`azure.azcollection`](https://docs.ansible.com/projects/ansible/latest/collections/azure/azcollection/)
- [Azure Resource Manager inventory](https://docs.ansible.com/projects/ansible/latest/collections/azure/azcollection/azure_rm_inventory.html)
- [`google.cloud` collection](https://docs.ansible.com/projects/ansible/latest/collections/google/cloud/)
- [Google Compute Engine inventory](https://docs.ansible.com/projects/ansible/latest/collections/google/cloud/gcp_compute_inventory.html)
- [Inventory plugin index](https://docs.ansible.com/projects/ansible/latest/collections/index_inventory.html)

## Video learning

- [Ansible official YouTube channel](https://www.youtube.com/@AnsibleAutomation)
- [Red Hat official YouTube channel](https://www.youtube.com/@RedHat)
- [AWS Events channel](https://www.youtube.com/@AWSEventsChannel)
- [Microsoft Developer channel](https://www.youtube.com/@MicrosoftDeveloper)
- [Google Cloud Tech channel](https://www.youtube.com/@googlecloudtech)

Prefer recent official sessions. Check the Ansible, collection, controller, and
cloud-service versions before adopting commands or product-specific behavior.

## Books for deeper study

- *Ansible for DevOps* by Jeff Geerling
- *Practical Ansible* by Daniel Oh and James Freeman

Books provide mental models and examples; current official documentation remains
the authority for supported behavior and version compatibility.

## Suggested review loop

1. Read one concept page from this module.
2. Explain the ownership, target, identity, and recovery boundaries aloud.
3. Answer a related [scenario](scenarios.md) before reading its model answer.
4. Verify uncertain version-specific behavior in official documentation.
5. Record the gap as a flashcard and repeat it after several days.

Return to the [module overview](index.md) when ready to continue.
