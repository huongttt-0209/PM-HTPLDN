# Bug Report — ~~R7.7.1 HD-049/050/051 TC TV assignment UI blocker~~ [CLOSED]

| Trường | Giá trị |
|--------|---------|
| **Bug ID** | ~~BUG-HD-049-TC-ORG-UI-001~~ |
| **Module** | Hỏi đáp pháp lý |
| **Round** | R7.7.1 Phase 3b |
| **Ngày test** | 2026-05-10 00:44-00:47 UTC+7 |
| **Tester** | QA Automation |
| **Severity** | Major |
| **Priority** | P0 |
| **Status** | Closed-verified |
| **Method** | UI-only via Chrome browser automation, no API calls |
| **Account** | `cb_nv_tw_04` |

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial | Closed | Open |
|------|----------|-------|--------|-------|---------|--------|------|
| 1    | 0        | 1     | 0      | 0     | 0       | 1      | 0    |

> **Quy tắc đếm:** Single-bug file (1 bug Major, Closed-verified). `Closed` đếm Status ∈ {Closed, Closed-verified, ~~closed~~}; `Open` đếm phần còn lại (Open, Reopen, Defer, Withdrawn).

> **Re-test:** 2026-05-10 03:20:00 R10c — ✅ PASS (Closed-verified). Same record HD-20260509-004 (DANG_XU_LY, version=4). Mở modal Phân công → click segment "Tổ chức tư vấn" → section "Tổ chức tư vấn (HOAT_DONG)" render đúng table headers `Mã tổ chức / Tên tổ chức / Lĩnh vực / Người đại diện` với **7 TC TV** (TC-BTP-TW-0001..0005, 0007, 0008) — match BE response. 2 TC cover Doanh nghiệp: TC-0001 Alpha + TC-0002 Beta. Click TC-0001 Alpha → section "Tư vấn viên chịu trách nhiệm" cấp 2 render đúng với 6 TVV của TC (API `GET /api/v1/tu-van-viens?toChucId=beb25e6f-...&trangThai=HOAT_DONG&pageSize=100&page=1` reqid=240). Validation: button [Phân công] disabled khi TC=null TVV=null + TC=selected TVV=null → enabled khi cả 2 selected → đúng spec FR-II-06.
>
> **Re-test:** 2026-05-10 01:25:24 R10b — ❌ REPRODUCES (Open). Same record HD-20260509-004 (cấp DANG_XU_LY giờ, version=4). Mở modal Phân công → click segment "Tổ chức tư vấn" → segmented control selected="Tổ chức tư vấn" nhưng table headers vẫn `Họ tên/Email/Workload` (table cá nhân) với 40 rows. API `GET /api/v1/to-chuc-tu-vans?trangThai=HOAT_DONG&pageSize=100&page=1` reqid=232 trả 200 với 7 TC TV active (2 cover linhVuc Doanh nghiệp). FE không bind data API vào UI section "Tổ chức tư vấn". → root cause: FE bug (binding/render), không phải BE. Severity giữ Major P0.

## Summary

Trong modal **Phân công xử lý**, khi chuyển **Đối tượng xử lý** từ `Cá nhân` sang `Tổ chức tư vấn`, UI có hiện field `Tổ chức tư vấn (HOAT_DONG)` nhưng không render danh sách tổ chức cấp 1. Phần bên dưới vẫn là bảng **Cá nhân chịu trách nhiệm** của luồng cá nhân.

Kết quả: không thể hoàn tất HD-049/050 qua UI, và HD-051 validation thiếu Tổ chức + TVV cũng không thể verify đúng vì UI không cho chọn TC TV.

## Repro Steps

1. Login bằng `cb_nv_tw_04`.
2. Vào `Quản lý hỏi đáp pháp lý`.
3. Mở bản ghi `HD-20260509-004`.
4. Click `Phân công`.
5. Chọn segmented option `Tổ chức tư vấn`.
6. Click dropdown `Chọn tổ chức tư vấn`.

## Expected

- Tab `Tổ chức tư vấn` hiển thị bảng cấp 1 danh sách TC TV `HOAT_DONG` có TVV thuộc tổ chức.
- Sau khi chọn TC, bảng cấp 2 chỉ hiển thị TVV thuộc TC đã chọn.
- Submit thiếu TC hoặc thiếu TVV phải báo `ERR-PC-04`.

## Actual

- Field `Chọn tổ chức tư vấn` hiển thị nhưng không có options nhìn thấy khi mở dropdown.
- Bảng bên dưới vẫn là danh sách cá nhân chịu trách nhiệm, không phải bảng TC TV/TVV.
- Không thể chọn TC TV để đi tiếp HD-050.

## Evidence

- [r7-7-1-hd-049-modal-viewport-tc-tab.png](../../functional/hoi-dap/r7-7-1-hd-049-modal-viewport-tc-tab.png)
- [r7-7-1-hd-049-org-dropdown-open-viewport.png](../../functional/hoi-dap/r7-7-1-hd-049-org-dropdown-open-viewport.png)
- [r7-7-1-hd-049-retest-tc-tab-broken.png](../../functional/hoi-dap/r7-7-1-hd-049-retest-tc-tab-broken.png) — R10b retest 2026-05-10 01:25:24
- [r7-7-1-hd-049-tc-tab-fixed.png](../../functional/hoi-dap/r7-7-1-hd-049-tc-tab-fixed.png) — R10c verify 2026-05-10 03:20:00 (cấp 1 render đúng 7 TC TV)
- [r7-7-1-hd-050-tvv-filter-by-tc.png](../../functional/hoi-dap/r7-7-1-hd-050-tvv-filter-by-tc.png) — R10c verify 2026-05-10 03:20:00 (cấp 2 TVV filter theo TC-0001)
- [r7-7-1-hd-051-validation-button-enabled.png](../../functional/hoi-dap/r7-7-1-hd-051-validation-button-enabled.png) — R10c verify 2026-05-10 03:20:00 (button [Phân công] enabled sau khi chọn cả TC + TVV)

### Network evidence retest (R10b 2026-05-10 01:25:24)

```
GET /api/v1/to-chuc-tu-vans?trangThai=HOAT_DONG&pageSize=100&page=1 → 200
{ "success": true, "meta": { "page": 1, "pageSize": 100, "total": 7, "totalPages": 1 },
  "data": [ ...7 TC TV HOAT_DONG, 2 covering linhVuc Doanh nghiệp (TC-BTP-TW-0001 Alpha, TC-BTP-TW-0002 Beta)... ] }
```

→ BE returns 7 active TC TV. FE doesn't render any. Confirms FE binding bug.

## Impact

Block toàn bộ nhánh phân công `TO_CHUC` trong FR-II-06:

- `HD-049` FAIL: không thấy danh sách tổ chức tư vấn cấp 1.
- `HD-050` BLOCKED: không chọn được TC để lọc TVV thuộc TC.
- `HD-051` BLOCKED: không verify được validation thiếu TC/TVV đúng spec.
- `HD-052` không chạy theo yêu cầu UI-only vì spec gốc là bypass API negative.

