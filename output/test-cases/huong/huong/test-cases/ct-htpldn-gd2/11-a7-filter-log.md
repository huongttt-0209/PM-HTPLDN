# A7 — Manual Filter UI/Function-testable Log

> **Phase A step**: A7 (Manual review + Edit IN-PLACE)
> **Ngày chạy**: 2026-05-10
> **Scope**: 73 TC sau A6 — verify mỗi TC chạy được qua MCP chrome-devtools (UI-driven)
> **Iron rule**: TC chỉ-DB/API thuần → LOẠI hoặc REWRITE thành UI-driven. Edit IN-PLACE file UC. File này CHỈ là audit log.

---

## 1. A7 filter checklist

Mỗi TC phải PASS các check sau để được GIỮ:

1. ✅ Có MCP UI action (`click`/`fill`/`take_snapshot`/`wait_for`) trong "Các bước thực hiện"
2. ✅ Expected results có UI assertion (DOM state / toast / modal / table render)
3. ✅ Network call (nếu test API) phải verify qua MCP `list_network_requests` (không curl thuần)
4. ✅ DB state assertion (nếu có) phải verify gián tiếp qua UI reload (KHÔNG SQL query thuần)

---

## 2. Phân loại 73 TC

| Status | Count | Note |
|--------|------:|------|
| ✅ GIỮ — UI-driven full | 70 | Toàn bộ TC dùng MCP click/snapshot + UI assertion |
| ⚠️ SỬA — convert API thuần thành UI-driven | 3 | (xem bảng dưới) |
| ❌ LOẠI — chỉ test DB/API không UI hook | 0 | None |

## 3. SỬA — convert TC API thuần (3 TC)

| TC ID | File | Issue | Fix |
|-------|------|-------|-----|
| TC-TH-018 | 06 | Test pagination param boundary `?page=0` `?size=101` qua MCP request URL — đậm chất API test | Fix: thêm UI step "MCP `evaluate_script` set window.location.search = '?page=0' rồi `wait_for` table re-render" — verify UI render lại đúng default page hoặc error toast |
| TC-TH-019 | 06 | Test field `loai=TONG_HOP_TW` qua API response — không UI hook | Fix: thêm UI step "Drill-down BC tổng hợp → MCP `evaluate_script` đọc data attribute `data-loai` của card hoặc badge label hiển thị 'BC tổng hợp toàn quốc'" — verify UI có visual marker cho loại TONG_HOP_TW |
| TC-PD-BC-016 | 04 | Test audit log dual entry — query log qua MCP — partially API | Fix: thêm UI step "Mở module Nhật ký HT (FR-10) lọc `entity IN (DOT_BAO_CAO, BAO_CAO_CT_HTPL)`" — verify 2 entries hiển thị trong UI grid table |

→ Các fix trên áp dụng INLINE bằng cách giữ description + thêm UI assertion vào "Kết quả mong đợi". KHÔNG đổi ID, KHÔNG đổi count.

## 4. LOẠI — không có

Không có TC nào thuộc loại "chỉ test DB/API không UI hook". Toàn bộ 73 TC sau A4/A6 đều có UI entry point qua SCR-XI-01 + drill-down.

## 5. Coverage delta sau A7

| File | Before A7 | A7 LOẠI | A7 SỬA in-place | After A7 |
|------|----------:|--------:|----------------:|---------:|
| 01 | 7 | 0 | 0 | 7 |
| 02 | 12 | 0 | 0 | 12 |
| 03 | 8 | 0 | 0 | 8 |
| 04 | 12 | 0 | 1 | 12 |
| 05 | 8 | 0 | 0 | 8 |
| 06 | 16 | 0 | 2 | 16 |
| 07 | 10 | 0 | 0 | 10 |
| **TỔNG** | **73** | **0** | **3** | **73** |

## 6. Acceptance A7

- ✅ 0 TC LOẠI (tất cả UI-testable)
- ✅ 3 TC SỬA in-place (cập nhật UI assertion trong expected)
- ✅ Final count: **73 TC** (51 A3 + 19 A4 + 3 A6 = 73)
- ✅ All 7 file UC sẵn sàng Phase B (B-block ref 01..07 — file 08-11 audit log)

*Generated 2026-05-10 — Phase A step A7 (Manual filter)*
