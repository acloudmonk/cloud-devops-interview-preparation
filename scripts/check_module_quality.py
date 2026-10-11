#!/usr/bin/env python3
"""Validate the minimum study and assessment path for released modules."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MAP = DOCS / "master-competency-map.md"

REQUIRED_PAGES = (
    "index.md",
    "concepts.md",
    "scenarios.md",
    "scenario-drills.md",
    "presentation-template.md",
    "rapid-fire.md",
    "flashcards.md",
    "references.md",
)

CASE_STUDY_FILES = (
    "global-commerce.md",
    "regulated-saas.md",
    "platform-transformation.md",
    "hybrid-modernization.md",
    "cyber-recovery.md",
    "reliability-finops.md",
    "ai-operations-copilot.md",
    "capstone.md",
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def table_flashcard_count(text: str) -> int:
    """Count data rows in Markdown tables after their separator rows."""
    count = 0
    in_body = False
    for line in text.splitlines():
        if not line.lstrip().startswith("|"):
            in_body = False
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if cells and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            in_body = True
            continue
        if in_body:
            count += 1
    return count


def drill_sections(text: str) -> list[tuple[str, str]]:
    numbered = re.compile(r"^##\s+(?:Drill\s+)?\d+(?:\.|\s+[—-])", re.MULTILINE)
    all_headings = list(re.finditer(r"^##\s+", text, re.MULTILINE))
    sections: list[tuple[str, str]] = []
    for match in numbered.finditer(text):
        end = len(text)
        for heading in all_headings:
            if heading.start() > match.start():
                end = heading.start()
                break
        title_end = text.find("\n", match.start())
        title = text[match.start() : title_end].strip()
        sections.append((title, text[match.end() : end]))
    return sections


def released_modules() -> list[Path]:
    pattern = re.compile(
        r"\[[^\]]+\]\((?P<path>\d{2}-[^)]+/index\.md)\)"
        r"\s*\|\s*Initial release\s*\|"
    )
    modules = [
        DOCS / Path(match.group("path")).parent
        for match in pattern.finditer(read(MAP))
    ]
    if not modules:
        raise RuntimeError("No Initial release modules found in master competency map")
    return modules


def validate_module(module: Path) -> list[str]:
    errors: list[str] = []
    label = module.relative_to(DOCS).as_posix()

    for page in REQUIRED_PAGES:
        if not (module / page).is_file():
            errors.append(f"{label}: missing required page {page}")

    if errors:
        return errors

    index = read(module / "index.md")
    for marker in (
        "Last reviewed:",
        "Where to start",
        "Recommended module path",
        "Completion checklist",
    ):
        if marker not in index:
            errors.append(f"{label}/index.md: missing '{marker}'")
    path_steps = len(re.findall(r"^\|\s*\d+\s*\|", index, re.MULTILINE))
    if path_steps < 15:
        errors.append(
            f"{label}/index.md: expected at least 15 ordered steps, found {path_steps}"
        )

    scenarios = read(module / "scenarios.md")
    scenario_count = len(re.findall(r"^##\s+\d+\.", scenarios, re.MULTILINE))
    answer_count = len(
        re.findall(r"\*\*(?:Model answer|Architect-level answer):\*\*", scenarios)
    )
    if scenario_count < 15:
        errors.append(
            f"{label}/scenarios.md: expected at least 15 scenarios, "
            f"found {scenario_count}"
        )
    if answer_count < 15:
        errors.append(
            f"{label}/scenarios.md: expected at least 15 model answers, "
            f"found {answer_count}"
        )

    drills = drill_sections(read(module / "scenario-drills.md"))
    if len(drills) < 10:
        errors.append(
            f"{label}/scenario-drills.md: expected at least 10 separately headed "
            f"drills, "
            f"found {len(drills)}"
        )
    for title, body in drills:
        words = re.findall(r"\b[\w][\w/-]*\b", body, re.UNICODE)
        if len(words) < 20:
            errors.append(
                f"{label}/scenario-drills.md: '{title}' needs a substantive response"
            )

    rapid = read(module / "rapid-fire.md")
    rapid_count = len(re.findall(r"^\d+\.\s+\*\*", rapid, re.MULTILINE))
    if rapid_count < 50:
        errors.append(
            f"{label}/rapid-fire.md: expected at least 50 questions, "
            f"found {rapid_count}"
        )

    flashcards = read(module / "flashcards.md")
    numbered_cards = len(
        re.findall(r"^\d+\.\s+\*\*", flashcards, re.MULTILINE)
    )
    flashcard_count = max(numbered_cards, table_flashcard_count(flashcards))
    if flashcard_count < 25:
        errors.append(
            f"{label}/flashcards.md: expected at least 25 cards, "
            f"found {flashcard_count}"
        )

    references = read(module / "references.md")
    reference_count = len(re.findall(r"https?://", references))
    video_count = len(
        re.findall(r"youtu(?:be\.com|\.be)", references, re.IGNORECASE)
    )
    if reference_count < 15:
        errors.append(
            f"{label}/references.md: expected at least 15 links, "
            f"found {reference_count}"
        )
    if video_count < 3:
        errors.append(
            f"{label}/references.md: expected at least 3 video sources, "
            f"found {video_count}"
        )
    if not re.search(r"^## .*Books", references, re.MULTILINE | re.IGNORECASE):
        errors.append(f"{label}/references.md: missing a books section")
    guidance_markers = (
        "Suggested reading order",
        "Suggested review loop",
        "After each source",
        "After reading",
        "Use sources",
        "Use books",
    )
    if not any(marker in references for marker in guidance_markers):
        errors.append(
            f"{label}/references.md: missing source-use or review-loop guidance"
        )

    mock_match = re.search(
        r"\(\.\./mock-interviews/(?P<name>[^)]+\.md)\)", index
    )
    if not mock_match:
        errors.append(f"{label}/index.md: missing mock-interview link")
    else:
        mock = DOCS / "mock-interviews" / mock_match.group("name")
        if not mock.is_file():
            errors.append(
                f"{label}/index.md: mock interview does not exist: {mock.name}"
            )
        else:
            mock_text = read(mock)
            has_scoring = re.search(
                r"^## (?:Scoring rubric|Scorecard)", mock_text, re.MULTILINE
            )
            if not has_scoring or "50" not in mock_text:
                errors.append(
                    f"{mock.relative_to(ROOT).as_posix()}: missing scoring or timing"
                )

    return errors


def validate_case_studies() -> list[str]:
    """Validate the released cross-domain case-study learning path."""
    errors: list[str] = []
    case_dir = DOCS / "case-studies"
    required = (
        "index.md",
        "method.md",
        "scorecard.md",
        *CASE_STUDY_FILES,
        "references.md",
    )
    for name in required:
        if not (case_dir / name).is_file():
            errors.append(f"case-studies: missing required page {name}")
    if errors:
        return errors

    index = read(case_dir / "index.md")
    for marker in (
        "Last reviewed:",
        "Where to start",
        "Recommended case-study path",
        "Completion checklist",
    ):
        if marker not in index:
            errors.append(f"case-studies/index.md: missing '{marker}'")
    path_steps = len(re.findall(r"^\|\s*\d+\s*\|", index, re.MULTILINE))
    if path_steps < 10:
        errors.append(
            f"case-studies/index.md: expected at least 10 ordered steps, "
            f"found {path_steps}"
        )

    for name in CASE_STUDY_FILES:
        text = read(case_dir / name)
        for marker in (
            "## Discovery prompts",
            "## Candidate tasks",
            "## Failure injects",
            "## Model direction",
            "## Strong close",
        ):
            if marker not in text:
                errors.append(f"case-studies/{name}: missing '{marker}'")
        bullet_count = len(re.findall(r"^-\s+", text, re.MULTILINE))
        if bullet_count < 5:
            errors.append(
                f"case-studies/{name}: expected substantive prompts and injects"
            )

    references = read(case_dir / "references.md")
    if len(re.findall(r"https?://", references)) < 15:
        errors.append("case-studies/references.md: expected at least 15 links")
    if len(re.findall(r"youtu(?:be\.com|\.be)", references, re.IGNORECASE)) < 3:
        errors.append("case-studies/references.md: expected at least 3 video sources")
    if not re.search(r"^## .*Books", references, re.MULTILINE | re.IGNORECASE):
        errors.append("case-studies/references.md: missing a books section")
    return errors


def main() -> int:
    modules = released_modules()
    errors = [error for module in modules for error in validate_module(module)]
    errors.extend(validate_case_studies())
    if errors:
        print("Released-module quality validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Released-module quality validation passed for {len(modules)} modules.")
    print(
        "Cross-domain case-study validation passed for "
        f"{len(CASE_STUDY_FILES)} cases."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
