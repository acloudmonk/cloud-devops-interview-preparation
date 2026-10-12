# Cloud & DevOps Architect Knowledge Base

An architect-level, scenario-driven knowledge base for senior Cloud, DevOps,
Platform Engineering, SRE, and consulting interviews.

## Start here

| Goal | Start page |
| --- | --- |
| Begin learning now | [Module 01: Cloud Architecture & Distributed Systems](docs/01-cloud-architecture/index.md) |
| See the recommended dependency-based learning order | [Documentation home and current learning path](docs/index.md#current-learning-path) |
| Inspect all 36 original topics and their status | [Master competency map](docs/master-competency-map.md) |
| Understand future delivery and study phases | [Study and delivery roadmap](docs/roadmap.md) |
| Practise cross-domain architecture decisions | [Architecture case studies](docs/case-studies/index.md) |
| Practise consulting discovery and stakeholder skills | [Consultant Discovery Playbook](docs/interview-playbook/index.md) |
| Review curriculum completeness and validation evidence | [v1 readiness report](docs/release-readiness.md) |

Within each released module, follow its numbered path from concepts through the
scored mock interview. Module IDs preserve the complete curriculum structure, so
the current released path follows Modules 01–31 in their documented study order.

The curriculum covers AWS, Azure, GCP, Linux, networking, CI/CD, containers,
Kubernetes, Infrastructure as Code, security, observability, reliability,
modernization, FinOps, distributed systems, and technical consulting.

## Current status

The documentation foundation and the Cloud Architecture, AWS Architecture, Azure
Architecture, GCP Architecture, Cross-Cloud Capability Mapping, Linux, Networking,
Git, CI/CD, Docker, Kubernetes, Kubernetes Ecosystem,
Terraform/OpenTofu,
Ansible, DevSecOps, Zero Trust Architecture, Observability, Site Reliability
Engineering, High Availability, Disaster Recovery, Business Continuity, FinOps,
Cross-Cloud Well-Architected Reviews, Hybrid and Multi-Cloud, APIs and Enterprise
Identity, Python Automation, AI for Cloud and DevOps, Platform Engineering,
Microservices Architecture, SaaS Architecture, Messaging and Event-Driven
Architecture, Database Architecture, Cloud Migration and Modernization, and
Cross-Domain Architecture Case Studies are complete initial releases.
See the
[master competency map](docs/master-competency-map.md) for coverage status.

## View the documentation

Two viewing methods are supported:

1. **GitHub Markdown:** Start from the
   [Cloud Architecture module](docs/01-cloud-architecture/index.md) and follow its
   numbered page links. This requires no local setup.
2. **Local MkDocs site:** Use this when you want full-text search, sidebar and
   previous/next navigation, Mermaid diagrams, and the complete site theme.

To start the local site:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m mkdocs serve
```

Open `http://127.0.0.1:8000`.

The repository does not publish a hosted documentation website. This avoids an
additional deployment and maintenance path while the knowledge base is used
through GitHub and locally.

## Validate

```powershell
python -m mkdocs build --strict
```

## Content model

Every major module is designed to contain:

- core concepts and mental models;
- architecture decisions and trade-offs;
- security, reliability, operations, and cost considerations;
- AWS, Azure, and GCP relevance;
- troubleshooting guidance;
- lightweight paper-and-whiteboard design exercises;
- scenario-based questions with architect-level answers;
- curated documentation, books, talks, and videos.

Executable application and cloud-deployment labs are optional future material.
The current priority is theoretical depth, architecture reasoning,
troubleshooting, and scenario-based interview practice.

See [CONTRIBUTING.md](CONTRIBUTING.md) before adding or changing content.
