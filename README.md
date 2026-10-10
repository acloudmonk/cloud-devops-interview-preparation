# Cloud & DevOps Architect Knowledge Base

An architect-level, scenario-driven knowledge base for senior Cloud, DevOps,
Platform Engineering, SRE, and consulting interviews.

## Start here

Begin with [Cloud Architecture & Distributed Systems](docs/01-cloud-architecture/index.md),
continue to [Linux & OS Fundamentals](docs/06-linux/index.md), and then study
[Cloud Networking & DNS](docs/07-networking/index.md) followed by
[Git & Source-Control Strategy](docs/08-git/index.md), then
[CI/CD & Progressive Delivery](docs/09-cicd/index.md), followed by
[Docker & Container Engineering](docs/10-docker/index.md), then
[Kubernetes](docs/11-kubernetes/index.md). Follow each module's numbered path
from concepts to its scored mock interview. Use the
[site home](docs/index.md) for study guidance and the
[master competency map](docs/master-competency-map.md) to see all 36 topics and
their delivery status.

The curriculum covers AWS, Azure, GCP, Linux, networking, CI/CD, containers,
Kubernetes, Infrastructure as Code, security, observability, reliability,
modernization, FinOps, distributed systems, and technical consulting.

## Current status

The documentation foundation and the Cloud Architecture, Linux, Networking,
Git, CI/CD, Docker, and Kubernetes modules are complete initial releases. The
Kubernetes Ecosystem is the next planned milestone. See the
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
- lightweight design exercises and paper labs;
- scenario-based questions with architect-level answers;
- curated documentation, books, talks, and videos.

Executable application and cloud-deployment labs are optional future material.
The current priority is theoretical depth, architecture reasoning,
troubleshooting, and scenario-based interview practice.

See [CONTRIBUTING.md](CONTRIBUTING.md) before adding or changing content.
