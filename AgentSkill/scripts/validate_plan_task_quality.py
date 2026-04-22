#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


ANGLE_TOKEN_RE = re.compile(r"<[^>]+>")
# Allow structured placeholder-tokens that are part of the *domain spec* (e.g., link/equation/citation anchors).
# Examples: <LINK_42>, <EQ_1>, <CITE_7>, <URL_3>
ALLOWED_ANGLE_TOKEN_RE = re.compile(r"^<[A-Z]{2,}[A-Z0-9_]*>$")

PLACEHOLDER_PATTERNS = [
    re.compile(r"\bTODO\b", re.IGNORECASE),
    re.compile(r"\bTBD\b", re.IGNORECASE),
    re.compile(r"path/to/", re.IGNORECASE),
]

MIN_RESEARCH_ROWS_L3 = 8
MIN_URLS_L3 = 5

PDF_MARKER_GROUPS: list[tuple[str, list[str]]] = [
    ("Domain preflight spec (`preflight.json`)", ["preflight.json"]),
    ("Functional snapshot (links/toc/annotations/...)", ["Functional snapshot", "功能快照", "func_snapshot"]),
    ("Coordinate/rotation unification", ["坐标", "coordinate", "rotation", "旋转"]),
    ("Layout IR/DOM (stable IDs + schema)", ["Layout DOM", "IR/DOM", "dom.json", "layout_dom"]),
    ("Structured translation schema + cache", ["JSON schema", "SQLite", "cache.sqlite", "translation_cache"]),
    ("Typesetting tiers (textbox/htmlbox/shaping)", ["insert_htmlbox", "insert_textbox", "Pango", "HarfBuzz", "WeasyPrint", "shaping"]),
    ("Redaction strategy + side effects", ["redaction", "apply_redactions", "add_redact_annot"]),
    ("Multi-renderer QA (pdfium/poppler/etc)", ["pdfium", "poppler", "multi-renderer", "多渲染"]),
    ("Digital signature / modification constraints", ["digital signature", "签名", "signature"]),
]

SKIP_WEB_JUSTIFICATION_RE = re.compile(
    r"(未做|没有做).{0,30}(外网|联网|web).{0,30}用户未要求",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class CheckResult:
    ok: bool
    issues: list[str]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def check_placeholders(text: str, label: str) -> CheckResult:
    issues: list[str] = []

    # Angle-bracket placeholders are common in templates, but angle-bracket tokens can also be
    # legitimate domain-spec anchors (e.g., <LINK_42>). Treat only non-allowed tokens as placeholders.
    for m in ANGLE_TOKEN_RE.finditer(text):
        token = m.group(0)
        if ALLOWED_ANGLE_TOKEN_RE.match(token):
            continue
        issues.append(f"{label}: placeholder-like angle token detected: {token!r}")
        break

    for pat in PLACEHOLDER_PATTERNS:
        m = pat.search(text)
        if m:
            issues.append(f"{label}: placeholder-like token detected: {m.group(0)!r}")
    return CheckResult(ok=(len(issues) == 0), issues=issues)


def require_any(text: str, label: str, needles: list[str]) -> CheckResult:
    issues: list[str] = []
    for needle in needles:
        if needle not in text:
            issues.append(f"{label}: missing required marker: {needle!r}")
    return CheckResult(ok=(len(issues) == 0), issues=issues)


def require_any_of(text: str, label: str, description: str, options: list[str]) -> CheckResult:
    for opt in options:
        if opt in text:
            return CheckResult(ok=True, issues=[])
    return CheckResult(
        ok=False,
        issues=[f"{label}: missing required concept: {description} (need any of: {options})"],
    )


def detect_level(text: str) -> Optional[str]:
    m = re.search(r"(?m)^Level\\s*[:：]\\s*(L\\d)\\b", text)
    if m:
        return m.group(1)
    return None


def is_pdf_like_plan(text: str) -> bool:
    """
    Detect PDF/format-surgery plans.

    Avoid false positives where a plan merely *mentions* "PDF" (e.g., as an example in a skill plan).
    Require both:
    - the 'pdf' token appears; and
    - at least 2 strong, PDF-surgery-specific markers appear.
    """
    if not re.search(r"\\bpdf\\b", text, flags=re.IGNORECASE):
        return False
    lower = text.lower()
    strong_markers = [
        "mineru",
        "pymupdf",
        "pikepdf",
        "qpdf",
        "redaction",
        "insert_textbox",
        "insert_htmlbox",
        "preflight.json",
        "func_snapshot",
        "layout dom",
        "ir/dom",
        "保排版",
        "写回",
    ]
    hits = 0
    for m in strong_markers:
        if m in lower or m in text:
            hits += 1
    return hits >= 2


def count_urls(text: str) -> int:
    # Count URL-like tokens. Keep it simple; we only need a gate signal.
    return len(re.findall(r"https?://", text))


def count_research_log_rows(text: str) -> int:
    """
    Heuristic: find the first Markdown table that looks like a Research Log:
    it must contain a 'Query' column and a 'Source' column.
    Count data rows until the table ends.
    """
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if "| Query |" not in line or "Source" not in line:
            continue
        # Next line should be the separator row with ---.
        if i + 1 >= len(lines) or "---" not in lines[i + 1]:
            continue
        # Count subsequent table rows.
        count = 0
        for j in range(i + 2, len(lines)):
            row = lines[j].rstrip()
            if not row.strip():
                break
            if not row.lstrip().startswith("|"):
                break
            if row.count("|") >= 6:
                count += 1
        return count
    return 0


def count_pipeline_stage_rows(text: str) -> int:
    """
    Heuristic: find the first Markdown table header that looks like a pipeline stages mapping:
    it must contain a 'Stage' column and at least 5 other columns (to avoid false positives).
    Count data rows until the table ends.
    """
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if "| Stage |" not in line:
            continue
        # Next line should be the separator row with ---.
        if i + 1 >= len(lines) or "---" not in lines[i + 1]:
            continue
        # Count subsequent table rows.
        count = 0
        for j in range(i + 2, len(lines)):
            row = lines[j].rstrip()
            if not row.strip():
                break
            if not row.lstrip().startswith("|"):
                break
            # Require at least 6 pipes so it looks like a multi-column mapping table.
            if row.count("|") >= 6:
                count += 1
        return count
    return 0


def validate_plan(plan_path: Path, text: str) -> CheckResult:
    checks: list[CheckResult] = []
    checks.append(check_placeholders(text, f"Plan ({plan_path})"))

    # Keep these checks keyword-based to avoid coupling to exact headings.
    checks.append(
        require_any(
            text,
            f"Plan ({plan_path})",
            [
                "User Intent Lock",
                "Requirements",
                "Acceptance",
                "Validation",
                "Constraints",
                "Milestones",
                "Resumption",
            ],
        )
    )

    level = detect_level(text)
    if level == "L3":
        if SKIP_WEB_JUSTIFICATION_RE.search(text):
            checks.append(
                CheckResult(
                    ok=False,
                    issues=[
                        f"Plan ({plan_path}): L3 must not justify skipping web research as 'user didn't ask' (Research Gate violation)."
                    ],
                )
            )

        research_rows = count_research_log_rows(text)
        if research_rows < MIN_RESEARCH_ROWS_L3:
            checks.append(
                CheckResult(
                    ok=False,
                    issues=[
                        f"Plan ({plan_path}): L3 requires a non-trivial Research Log table (>= {MIN_RESEARCH_ROWS_L3} rows); got {research_rows}"
                    ],
                )
            )

        url_count = count_urls(text)
        if url_count < MIN_URLS_L3:
            checks.append(
                CheckResult(
                    ok=False,
                    issues=[
                        f"Plan ({plan_path}): L3 requires external web sources (>= {MIN_URLS_L3} URLs found); got {url_count}"
                    ],
                )
            )

        checks.append(
            require_any(
                text,
                f"Plan ({plan_path})",
                [
                    "Candidate Solutions",
                    "Architecture Decision",
                    "Pipeline Stages",
                    "Workdir & Resume",
                    "QA Plan",
                    "Validation Matrix",
                ],
            )
        )
        stage_rows = count_pipeline_stage_rows(text)
        if stage_rows < 8:
            checks.append(
                CheckResult(
                    ok=False,
                    issues=[
                        f"Plan ({plan_path}): L3 requires a non-trivial Pipeline Stages table (>=8 rows); got {stage_rows}"
                    ],
                )
            )

        if is_pdf_like_plan(text):
            for (desc, options) in PDF_MARKER_GROUPS:
                checks.append(require_any_of(text, f"Plan ({plan_path})", f"PDF/format-surgery: {desc}", options))

    issues: list[str] = []
    ok = True
    for c in checks:
        ok = ok and c.ok
        issues.extend(c.issues)
    return CheckResult(ok=ok, issues=issues)


def validate_task(task_path: Path, text: str) -> CheckResult:
    checks: list[CheckResult] = []
    checks.append(check_placeholders(text, f"Task ({task_path})"))

    checks.append(
        require_any(
            text,
            f"Task ({task_path})",
            [
                "Task Group",
                "Checkpoint",
                "Final Validation",
                "Final Review",
                "- [",
            ],
        )
    )

    issues: list[str] = []
    ok = True
    for c in checks:
        ok = ok and c.ok
        issues.extend(c.issues)
    return CheckResult(ok=ok, issues=issues)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate Plan.md and Task.md quality gates (placeholders + required sections).",
    )
    parser.add_argument(
        "--plan",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "v0.3.0" / "Plan.md",
        help="Path to Plan.md (default: AgentSkill/v0.3.0/Plan.md).",
    )
    parser.add_argument(
        "--task",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "v0.3.0" / "Task.md",
        help="Path to Task.md (default: AgentSkill/v0.3.0/Task.md).",
    )
    args = parser.parse_args()

    plan_path: Path = args.plan.resolve()
    task_path: Path = args.task.resolve()

    all_ok = True

    if not plan_path.exists():
        print(f"Plan: FAIL (file not found): {plan_path}")
        return 1
    if not task_path.exists():
        print(f"Task: FAIL (file not found): {task_path}")
        return 1

    plan_text = read_text(plan_path)
    task_text = read_text(task_path)

    plan_res = validate_plan(plan_path, plan_text)
    task_res = validate_task(task_path, task_text)

    for issue in plan_res.issues + task_res.issues:
        print(issue)

    all_ok = all_ok and plan_res.ok and task_res.ok

    if all_ok:
        print("Result: PASS (Plan/Task quality gate satisfied)")
        return 0

    print("Result: FAIL (Plan/Task quality gate failed)")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
