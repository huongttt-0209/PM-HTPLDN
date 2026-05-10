# QA Report — R7.4.D1 Đánh giá Hiệu quả HTPL

| Field | Value |
|---|---|
| Status | DONE_WITH_CONCERNS |
| Date | 2026-05-09 |
| Target | http://103.172.236.130:3000 |
| Scope | R7.4.D1 — Tạo kỳ Đánh giá Hiệu quả HTPL `LAP_KE_HOACH` |
| Account set | 03 |
| Account used | `cb_nv_tw_03` |
| Mode | qa-only, browser-based |
| Pages visited | 4: login, OTP, dashboard, `/danh-gia/ke-hoach/danh-sach`, detail |
| Screenshots | 8 |
| Framework signal | React/Vite + Ant Design |
| Test framework detected | No test framework detected. Run `/qa` to bootstrap one and enable regression test generation. |

## Verdict

R7.4.D1 passes the main acceptance path.

Created a new evaluation plan:

- Name: `QA R7.4.D1 bo 03 202605091141`
- Code: `DG-20260509-0001`
- UUID: `c521f1f1-82b2-424a-a14c-6d01e91ce540`
- State: `LAP_KE_HOACH`
- URL: `http://103.172.236.130:3000/danh-gia/ke-hoach/c521f1f1-82b2-424a-a14c-6d01e91ce540`

The flow successfully redirected to the detail page with tab `Tiêu chí` active. The detail tab rendered `Thêm tiêu chí`, `Nhập từ danh mục`, criteria table headers, and `Lưu thay đổi`.

## Health Score

Overall: 91/100

| Category | Score | Notes |
|---|---:|---|
| Console | 70 | 1 expected unauthenticated `GET /auth/me` 401 on login page, plus AntD `maskClosable` warning logged as console error |
| Links | 100 | No broken visible navigation in tested path |
| Visual | 92 | Date display offset is visible in detail/list |
| Functional | 95 | Main create and detail flow passed |
| UX | 88 | Date offset can mislead users setting an evaluation period |
| Performance | 100 | No user-visible load issue observed |
| Content | 100 | Vietnamese labels render clearly |
| Accessibility | 95 | Keyboard/standard controls usable in tested path |

## Evidence

| Evidence | File |
|---|---|
| Login page | `r74d1-login.png` |
| OTP screen after `cb_nv_tw_03` login | `r74d1-after-login-click.png` |
| Dashboard after OTP | `r74d1-dashboard.png` |
| Empty list before create | `r74d1-01-list-empty-before-create.png` |
| Create form with required fields and v3.5 fields | `r74d1-02-create-form-filled.png` |
| Detail after save, state `Lập kế hoạch`, tab `Tiêu chí` active | `r74d1-03-after-save-detail.png` |
| List search finds created plan | `r74d1-04-list-search-created.png` |

## API Proof

`GET /api/v1/ke-hoach-danh-gias/c521f1f1-82b2-424a-a14c-6d01e91ce540` returned 200:

```json
{
  "maKeHoach": "DG-20260509-0001",
  "tenDot": "QA R7.4.D1 bo 03 202605091141",
  "trangThai": "LAP_KE_HOACH",
  "tanSuat": "SO_BO_6_THANG",
  "doiTuong": "VU_VIEC",
  "mucTieu": "QA report-only R7.4.D1 bằng bộ tài khoản 03. Kiểm tra tạo kỳ Đánh giá Hiệu quả HTPL trạng thái LAP_KE_HOACH và chuyển sang tab Tiêu chí.",
  "ghiChu": "QA-only R7.4.D1, account cb_nv_tw_03.",
  "thoiGianBatDau": "2026-03-31",
  "thoiGianKetThuc": "2026-06-29"
}
```

`GET /api/v1/ke-hoach-danh-gias/c521f1f1-82b2-424a-a14c-6d01e91ce540/tieu-chis` returned 200 with `[]`, which matches a newly created plan before criteria are added.

Search list API returned 200 with 1 matching record.

## Findings

### ISSUE-001 — Medium — Date input shifts back one day after save

Input during create:

- Start: `01/04/2026`
- End: `30/06/2026`

Observed after save:

- Detail/list display: `31/03/2026` → `29/06/2026`
- API detail: `thoiGianBatDau = 2026-03-31`, `thoiGianKetThuc = 2026-06-29`

This is the same timezone-offset pattern already noted in prior R7.4.D1 evidence. It does not block the create flow, but it is risky because evaluation periods drive downstream filtering.

Repro:

1. Login `cb_nv_tw_03`.
2. Open `/danh-gia/ke-hoach/danh-sach`.
3. Click `Tạo kế hoạch`.
4. Enter dates `01/04/2026` and `30/06/2026`.
5. Click `Lưu & Chuyển tiêu chí`.
6. Observe detail/list dates show one day earlier.

Evidence:

- `r74d1-02-create-form-filled.png`
- `r74d1-03-after-save-detail.png`
- `r74d1-04-list-search-created.png`

### OBS-001 — Low — Login page emits expected pre-auth 401 and AntD deprecation warning

Console/network during login:

- `GET /api/v1/auth/me` → 401 before login, expected for unauthenticated page load.
- AntD warning: `Modal maskClosable is deprecated. Please use mask.closable instead.`

No user-facing break was observed.

## Acceptance Checklist

| Check | Result |
|---|---|
| Login with account set 03 | PASS |
| Create plan from `/danh-gia/ke-hoach/danh-sach` | PASS |
| Required fields accepted | PASS |
| v3.5 fields `Mục tiêu` and `Ghi chú` visible and persisted | PASS |
| Submit `[Lưu & Chuyển tiêu chí]` | PASS |
| Redirect to detail page | PASS |
| State is `LAP_KE_HOACH` / `Lập kế hoạch` | PASS |
| Tab `Tiêu chí` active after save | PASS |
| Criteria controls render | PASS |
| Created plan searchable in list | PASS |

## Top 3 Things To Fix

1. Fix date-only handling so user-entered `01/04/2026` persists and displays as `01/04/2026`, not `31/03/2026`.
2. Clean the AntD `maskClosable` deprecation warning so console health is not noisy.
3. Consider adding a regression test for R7.4.D1 create flow with exact date assertions.

