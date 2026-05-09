#!/usr/bin/env python3
"""PreToolUse hook: enforce QA report file path convention.

Trigger: Write/Edit/MultiEdit on QA report files.
Logic: filename pattern → required parent folder under output/qa-reports/round*/.

Convention (project HTPLDN, 2026-05-09):
  bug-report-*.md            → output/qa-reports/round*/bug-reports/<module>/
  functional-test-report-*.md → output/qa-reports/round*/functional/<module>/
  workflow-test-report-*.md   → output/qa-reports/round*/workflow/<module>/
  seed-checklist-*.md         → output/qa-reports/round*/seed/<module>/

Memory ref: qa_htpldn_report_path_convention.md (2026-05-09 R7.7.4.5 — user nhắc).
Exit 2 = block + show stderr to Claude.
"""
import json
import re
import sys

# (filename pattern, required parent folder segment)
RULES = [
    (re.compile(r"bug-report[^/]*\.md$", re.IGNORECASE), "bug-reports"),
    (re.compile(r"functional-test-report[^/]*\.md$", re.IGNORECASE), "functional"),
    (re.compile(r"workflow-test-report[^/]*\.md$", re.IGNORECASE), "workflow"),
    (re.compile(r"seed-checklist[^/]*\.md$", re.IGNORECASE), "seed"),
]

# Only enforce when path is inside qa-reports/
QA_REPORTS_MARKER = "/output/qa-reports/"


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    tool_name = payload.get("tool_name", "")
    tool_input = payload.get("tool_input", {})
    file_path = tool_input.get("file_path", "")

    if not file_path or QA_REPORTS_MARKER not in file_path:
        sys.exit(0)

    if tool_name not in {"Write", "Edit", "MultiEdit"}:
        sys.exit(0)

    for filename_re, required_segment in RULES:
        if not filename_re.search(file_path):
            continue
        # Path must contain /<required_segment>/ between qa-reports/round*/ and filename
        # e.g. .../qa-reports/round7-2026-05-06/bug-reports/nguoi-ho-tro/bug-report-...md
        segments = file_path.split("/")
        if required_segment in segments:
            sys.exit(0)
        # Block — wrong folder
        sys.stderr.write(
            f"BLOCKED: {filename_re.pattern} phải lưu trong folder `{required_segment}/<module>/`.\n\n"
            f"  File path hiện tại: {file_path}\n"
            f"  Folder bắt buộc:    output/qa-reports/round*/{required_segment}/<module>/\n\n"
            "Convention QA project (memory `qa_htpldn_report_path_convention`):\n"
            "  bug-report-*.md             → bug-reports/<module>/  (ảnh ở image/)\n"
            "  functional-test-report-*.md → functional/<module>/   (evidence ở evidence-rN/ hoặc screenshots-rN/)\n"
            "  workflow-test-report-*.md   → workflow/<module>/     (evidence ở evidence-rN/)\n"
            "  seed-checklist-*.md         → seed/<module>/         (ảnh ở image/)\n\n"
            "Nếu cần đổi convention → update memory + hook trước khi tạo file ngoài rule.\n"
        )
        sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
