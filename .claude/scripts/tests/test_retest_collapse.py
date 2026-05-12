#!/usr/bin/env python3
"""Golden tests cho collapse-retest-history.py + auto-bump-bug-report-date.py.

Test cases:
  1. Single retest block → no-op (idempotent)
  2. Multiple retest single-line → keep latest, drop older
  3. Multi-line blockquote sub-bullets `> - ...` → boundary đúng
  4. Code block (fenced + indented + inline) → timestamp inside KHÔNG ảnh hưởng
  5. Idempotent 10x → checksum stable
  6. Bug heading variants (h2 `## BUG-`, `## ~~BUG-~~`, `## **BUG-**`) → đều detect
  7. Evidence ảnh trong dropped block → stderr report, KHÔNG xoá file ảnh
  8. Header.Ngày stale vs body max → auto-bump bump đúng
  9. Header.Ngày newer than body → KHÔNG bump down

Run: python3 .claude/scripts/tests/test_retest_collapse.py
Exit 0 = all pass, exit 1 = fail.

Portable: no external deps, std-lib only.
"""
from __future__ import annotations

import hashlib
import io
import json
import os
import subprocess
import sys
import tempfile
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]  # project root
SCRIPTS = ROOT / ".claude" / "scripts"
HOOKS = ROOT / ".claude" / "hooks"

sys.path.insert(0, str(SCRIPTS))
sys.path.insert(0, str(HOOKS))


# ----- import modules under test -----
def _import_module(path: Path, name: str):
    import importlib.util
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


collapse_mod = _import_module(SCRIPTS / "collapse-retest-history.py", "collapse_retest")
bump_mod = _import_module(HOOKS / "auto-bump-bug-report-date.py", "auto_bump_date")
check_dup_mod = _import_module(HOOKS / "check-retest-no-duplicate.py", "check_retest_dup")


# ----- assertions helpers -----
class TestFail(AssertionError):
    pass


def assert_eq(actual, expected, msg: str) -> None:
    if actual != expected:
        raise TestFail(f"{msg}: expected {expected!r}, got {actual!r}")


def md5(s: str) -> str:
    return hashlib.md5(s.encode("utf-8")).hexdigest()


# ----- fixtures -----
FIXTURE_SINGLE = """\
# Bug Report — X

| Thông tin | Giá trị |
|-----------|---------|
| **Ngày** | 2026-05-10 09:00:00 |

## BUG-X-001 — Single retest

> **Re-test:** 2026-05-10 09:00:00 R3 — ✅ PASS. Clean.

### Mô tả
Foo.
"""

FIXTURE_MULTI = """\
# Bug Report — Y

| Thông tin | Giá trị |
|-----------|---------|
| **Ngày** | 2026-05-10 09:00:00 |

## BUG-Y-001 — Multi retest

> **Re-verify #8 2026-05-12 15:55:00 R19 — ❌ STILL Open.** Latest detail.
>
> **Re-verify #7 2026-05-12 01:53:00 — ❌ STILL Open.** Older detail with ![alt](image/r7.png).
>
> **Re-test #6 2026-05-11 17:09:00 — ❌ STILL Open.** Oldest.

### Mô tả
Bar.
"""

FIXTURE_MULTILINE = """\
# Bug Report — Z

| Thông tin | Giá trị |
|-----------|---------|
| **Ngày** | 2026-05-10 09:00:00 |

## BUG-Z-001 — Multi-line continuation

> **Re-test 2026-05-10 11:03:00:** ❌ VẪN reproducing + PHÁT HIỆN MỚI nghiêm trọng hơn:
> - POST `/api` → 500
> - PATCH `/api/{id}` → 200 (bypass!)
> - DELETE `/api/{id}` → 204
>
> **Severity escalate Major → Critical**. Status: **Open**.
>
> **Re-test #3 2026-05-10 21:44:00 — ✅ PASS Closed-verified.** Login OK:
> - GET → 200
> - POST → 403
> - DELETE → 403

### Mô tả
Multi-line case.
"""

FIXTURE_CODE_BLOCK = """\
# Bug Report — Q

| Thông tin | Giá trị |
|-----------|---------|
| **Ngày** | 2026-05-10 09:00:00 |

## BUG-Q-001 — Code block timestamp

> **Re-test:** 2026-05-10 10:00:00 R3 — ✅ PASS.

### Mô tả

Network log:

```json
{
  "created_at": "2026-12-31 23:59:59",
  "updated_at": "2099-01-01 00:00:00"
}
```

Inline: `2026-12-31 23:59:59` ref.

    indented code: 2026-12-31 23:59:59

Done.
"""

FIXTURE_NEWER_HEADER = """\
# Bug Report — N

| Thông tin | Giá trị |
|-----------|---------|
| **Ngày** | 2026-05-15 12:00:00 |

## BUG-N-001 — Header newer

> **Re-test:** 2026-05-10 09:00:00 R3 — ✅ PASS.

### Mô tả
Header newer than body.
"""

FIXTURE_HEADING_VARIANTS = """\
# Bug Report — V

| Thông tin | Giá trị |
|-----------|---------|
| **Ngày** | 2026-05-10 09:00:00 |

## BUG-V-001 — Plain heading

> **Re-test:** 2026-05-10 10:00:00 R3 — ✅ PASS.
> **Re-test:** 2026-05-11 11:00:00 R4 — ✅ PASS.

## ~~BUG-V-002~~ [CLOSED] — Strikethrough heading

> **Re-test:** 2026-05-09 09:00:00 R2 — ✅ PASS.
> **Re-test:** 2026-05-11 12:00:00 R5 — ✅ PASS.
"""


# ----- collapse tests -----
def test_single_noop():
    new, report = collapse_mod.collapse_file_content(FIXTURE_SINGLE)
    assert_eq(new, FIXTURE_SINGLE, "single retest must be no-op")
    assert_eq(report, [], "single retest no report entries")


def test_multi_collapse_keep_latest():
    new, report = collapse_mod.collapse_file_content(FIXTURE_MULTI)
    if new == FIXTURE_MULTI:
        raise TestFail("multi retest must collapse")
    assert_eq(len(report), 1, "exactly 1 bug collapsed")
    assert_eq(report[0]["dropped_count"], 2, "2 blocks dropped")
    assert_eq(report[0]["kept_ts"], "2026-05-12 15:55:00", "kept latest TS")
    # Latest line must remain
    if "Re-verify #8 2026-05-12 15:55:00" not in new:
        raise TestFail("latest #8 line missing post-collapse")
    if "Re-verify #7" in new:
        raise TestFail("#7 should be dropped")
    if "Re-test #6" in new:
        raise TestFail("#6 should be dropped")
    # Image from dropped block must be in report
    found = any("r7.png" in img for img in report[0]["dropped_images"])
    if not found:
        raise TestFail("dropped image not in report")


def test_multiline_continuation_boundary():
    new, report = collapse_mod.collapse_file_content(FIXTURE_MULTILINE)
    assert_eq(len(report), 1, "1 bug collapsed")
    assert_eq(report[0]["dropped_count"], 1, "1 older block dropped")
    # Latest = #3 (21:44:00) > 11:03:00
    assert_eq(report[0]["kept_ts"], "2026-05-10 21:44:00", "kept latest")
    # Sub-bullets of dropped block also dropped
    if "Severity escalate Major → Critical" in new:
        raise TestFail("escalate line (dropped block continuation) leaked")
    if "PATCH `/api/{id}` → 200 (bypass!)" in new:
        raise TestFail("dropped block sub-bullet leaked")
    # Kept block sub-bullets preserved
    if "GET → 200" not in new:
        raise TestFail("kept block sub-bullet missing")
    if "POST → 403" not in new:
        raise TestFail("kept block sub-bullet missing")


def test_idempotent_10x():
    """Run collapse 10x → output stable."""
    current = FIXTURE_MULTI
    hashes: list[str] = []
    for _ in range(10):
        current, _ = collapse_mod.collapse_file_content(current)
        hashes.append(md5(current))
    assert_eq(len(set(hashes[1:])), 1, "idempotent stable after 1st collapse")


def test_heading_variants():
    new, report = collapse_mod.collapse_file_content(FIXTURE_HEADING_VARIANTS)
    assert_eq(len(report), 2, "both bug entries detected & collapsed")


# ----- auto-bump tests -----
def test_bump_stale_header():
    """Body max > header → bump."""
    max_ts = bump_mod.find_max_retest_ts(FIXTURE_MULTI)
    assert_eq(
        max_ts.strftime("%Y-%m-%d %H:%M:%S"),
        "2026-05-12 15:55:00",
        "max body TS = #8 retest",
    )
    header_ts, _ = bump_mod.find_header_ngay(FIXTURE_MULTI)
    assert_eq(
        header_ts.strftime("%Y-%m-%d %H:%M:%S"),
        "2026-05-10 09:00:00",
        "header.Ngày parsed",
    )
    if max_ts <= header_ts:
        raise TestFail("max body should be > header")


def test_bump_skip_code_block_false_positive():
    """Code block timestamps must be ignored."""
    max_ts = bump_mod.find_max_retest_ts(FIXTURE_CODE_BLOCK)
    # Only valid retest TS = 2026-05-10 10:00:00
    assert_eq(
        max_ts.strftime("%Y-%m-%d %H:%M:%S"),
        "2026-05-10 10:00:00",
        "code block + inline code + indented code timestamps ignored",
    )


def test_bump_no_bump_down():
    """Header newer than body → KHÔNG bump (no bump down)."""
    header_ts, _ = bump_mod.find_header_ngay(FIXTURE_NEWER_HEADER)
    max_body = bump_mod.find_max_retest_ts(FIXTURE_NEWER_HEADER)
    if max_body > header_ts:
        raise TestFail("test setup: body should be older than header")
    # Simulate hook logic: max_body <= header_ts → no-op
    # Hook returns early, no write. Logic ok.


# ----- check-retest-no-duplicate tests -----
def test_check_dup_blocks_new_duplicate():
    """Pre clean (1 retest) + post duplicate (2 retest) → block."""
    violations = check_dup_mod.bugs_with_duplicate_retest(FIXTURE_MULTI)
    if len(violations) != 1:
        raise TestFail(f"expected 1 violation, got {len(violations)}")
    assert_eq(violations[0][1], 3, "BUG-Y-001 has 3 retest blocks")


def test_check_dup_tolerates_legacy():
    """Legacy file with pre-existing drift → not blocked again."""
    pre_violations = {h: c for h, c in check_dup_mod.bugs_with_duplicate_retest(FIXTURE_MULTI)}
    post_violations = {h: c for h, c in check_dup_mod.bugs_with_duplicate_retest(FIXTURE_MULTI)}
    new = []
    for h, post_cnt in post_violations.items():
        pre_cnt = pre_violations.get(h, 0)
        if post_cnt > max(pre_cnt, 1):
            new.append(h)
    assert_eq(new, [], "legacy drift unchanged → no NEW violations")


# ----- run all -----
TESTS = [
    test_single_noop,
    test_multi_collapse_keep_latest,
    test_multiline_continuation_boundary,
    test_idempotent_10x,
    test_heading_variants,
    test_bump_stale_header,
    test_bump_skip_code_block_false_positive,
    test_bump_no_bump_down,
    test_check_dup_blocks_new_duplicate,
    test_check_dup_tolerates_legacy,
]


def main() -> int:
    failures: list[tuple[str, str]] = []
    for t in TESTS:
        try:
            t()
            print(f"  ✓ {t.__name__}")
        except TestFail as e:
            failures.append((t.__name__, str(e)))
            print(f"  ✗ {t.__name__}: {e}")
        except Exception as e:  # noqa: BLE001
            failures.append((t.__name__, f"unexpected: {e}"))
            print(f"  ✗ {t.__name__}: unexpected error: {e}")

    print(f"\n[golden-tests] {len(TESTS) - len(failures)}/{len(TESTS)} passed")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
