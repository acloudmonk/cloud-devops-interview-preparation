# Cloud & DevOps Architect Knowledge Base

An architect-level, scenario-driven knowledge base for senior Cloud, DevOps,
Platform Engineering, SRE, and consulting interviews.

The curriculum covers AWS, Azure, GCP, Linux, networking, CI/CD, containers,
Kubernetes, Infrastructure as Code, security, observability, reliability,
modernization, FinOps, distributed systems, and technical consulting.

## Current status

The documentation foundation and the first pilot module—Cloud Architecture &
Distributed Systems—are under active development. See the
[master competency map](docs/master-competency-map.md) for coverage status.

## Run locally

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m mkdocs serve
```

Open `http://127.0.0.1:8000`.

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
- hands-on exercises;
- scenario-based questions with architect-level answers;
- curated documentation, books, talks, and videos.

See [CONTRIBUTING.md](CONTRIBUTING.md) before adding or changing content.
