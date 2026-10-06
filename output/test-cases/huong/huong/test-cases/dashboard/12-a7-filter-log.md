# A7 — Manual UI/function-testable Filter Log

> **Phase:** A7 (Manual review + Edit IN-PLACE — Iron Rule §3.1)
> **Generated:** 2026-05-10
> **Reviewer:** QA Automation Lead
> **Scope:** Quét toàn bộ 168 TC sau A6 fill — loại / sửa TC chỉ test được DB/API thuần

---

## 1. Quy trình A7

Per `plan.md` §3.1 + §4 Phase A:

1. Đọc 168 TC (8 file UC)
2. Phân loại mỗi TC:
   - ✅ **GIỮ** — UI testable trên chrome-devtools MCP (form/click/snapshot/network capture)
   - ⏸️ **DEFERRED** — cần stub backend, có workaround Chrome DevTools network throttling/block (mark trong file UC, không xóa)
   - ❌ **LOẠI** — chỉ test được qua DB query thuần / cURL API thuần, KHÔNG có UI bridge
   - ✏️ **SỬA** — rewrite TC để test qua UI thay vì DB/API
3. Edit IN-PLACE file UC nếu LOẠI/SỬA. Log action ở file này.

---

## 2. Kết quả phân loại

| File | Total | GIỮ | DEFERRED (UI workaround) | LOẠI | SỬA |
|------|-------|-----|--------------------------|------|-----|
| 01-TC | 23 | 22 | 1 (TC-DASH-016) | 0 | 0 |
| 02-TC | 20 | 20 | 0 | 0 | 0 |
| 03-TC | 25 | 25 | 0 | 0 | 0 |
| 04-TC | 16 | 16 | 0 | 0 | 0 |
| 05-TC | 15 | 15 | 0 | 0 | 0 |
| 06-TC | 23 | 13 | 10 (TC-DASH-130, 131, 132, 133, 134, 141, 144, 147, 148, 149) | 0 | 0 |
| 07-TC | 27 | 27 | 0 | 0 | 0 |
| 08-TC | 19 | 19 | 0 | 0 | 0 |
| **Tổng** | **168** | **157** | **11** | **0** | **0** |

---

## 3. DEFERRED list — chi tiết workaround

| TC ID | File | Scope | Workaround Chrome DevTools |
|-------|------|-------|----------------------------|
| TC-DASH-016 | 01-TC | Widget hỏng do API 5xx (ERR-DASH-02) | Use `mcp__chrome-devtools__evaluate_script` → throttle/block /api/dashboard/kpi-01 endpoint, observe Trạng thái 28 ("Không tải được dữ liệu" + nút "Thử lại") |
| TC-DASH-130 | 06-TC | 1 widget timeout 30s | Network throttling slow-3G hoặc block specific request URL pattern |
| TC-DASH-131 | 06-TC | Per-widget fail isolation | Block 1 endpoint, verify 11 widget khác vẫn render OK |
| TC-DASH-132 | 06-TC | Đã load thành công + sau đó fail (Trạng thái 29) | Allow first load, block subsequent tick |
| TC-DASH-133 | 06-TC | "Dữ liệu cũ" indicator giữ giá trị | Same as 132 + verify giá trị cũ stale display |
| TC-DASH-134 | 06-TC | Không có nút retry tại widget Trạng thái 29 | Same as 132 + verify UI elements absent |
| TC-DASH-141 | 06-TC | ≥50% widget (≥6/12) cùng fail → banner Trạng thái 30 | Block 6+ endpoints simultaneously |
| TC-DASH-144 | 06-TC | 3 chu kỳ liên tiếp banner → dòng phụ "Đã thử lại 3 lần..." | Block 6+ endpoints + wait 3×60s + capture banner text |
| TC-DASH-147 | 06-TC | Quyền user revoke giữa phiên | Cần backend hook hoặc QTHT manual revoke trong tab khác — nếu không feasible mark OBS |
| TC-DASH-148 | 06-TC | Đơn vị đang chọn bị vô hiệu hóa giữa phiên | QTHT vô hiệu hóa đơn vị trong tab khác → Dashboard tick refresh dropdown → tự đổi về "Tất cả [cấp L1]" |
| TC-DASH-149 | 06-TC | Nút "Làm mới" disabled khi đang tải | Network throttling + click Làm mới + observe button state mid-flight |

**Ghi chú:** 11 TC DEFERRED này KHÔNG bị LOẠI — vẫn test được qua Chrome DevTools MCP bằng `evaluate_script` để intercept network. Khi Phase B chạy, nếu workaround không khả thi trong env (ví dụ MCP API hạn chế) thì mark OBS với evidence rõ ràng.

---

## 4. LOẠI / SỬA

**Không có TC nào LOẠI hoặc SỬA.**

Lý do:
- Dashboard là module READ-ONLY → chỉ render KPI/biểu đồ
- Mọi TC đều có UI bridge: render giá trị / verify URL params / verify text / verify icon state / verify dropdown state
- Permission TC: redirect URL test qua UI navigation
- Drill-down TC: chỉ verify URL params (KHÔNG test module target)
- Backend stub: workaround network throttling

→ **0 TC LOẠI, 0 TC SỬA, 168 TC giữ nguyên.**

---

## 5. Confirm Iron Rule

- [x] **A4 inline merge:** 30 edge TC đã Edit trực tiếp vào file UC (TraceID suffix `(A4 merged)`) — verified bằng grep `(A4 merged)` ở 8 file UC
- [x] **A6 inline fill:** 7 fill TC đã Edit trực tiếp vào file UC (TraceID suffix `(A6 fill)`) — verified bằng grep `(A6 fill)`
- [x] **A7 inline edit:** 0 LOẠI / 0 SỬA → không có thay đổi inline
- [x] **0 TC sống ở file phụ (09/10/11/12)** — file phụ chỉ là audit log
- [x] **0 TC chỉ-DB/API thuần** — tất cả UI testable hoặc DEFERRED có workaround network throttling

---

## 6. Phase A — Done acceptance check

| Acceptance | Status |
|------------|--------|
| 7 bước A1-A7 done | ✅ A1 read SRS → A2 test plan → A3 base TC → A4 edge inline → A5 traceability → A6 review + fill inline → A7 filter |
| Traceability ≥95% BR + 100% AC | ✅ BR 6/6 = 100%, AC 74/74 = 100% (sau A6 fill) |
| 0 TC chỉ-DB/API thuần | ✅ 0 LOẠI |
| 0 TC sống ở file phụ | ✅ Mọi TC trong `01..08-TC-*.md` |
| SPEC-CLARIFY listed | ✅ 5 SPEC-CLARIFY-DASH-01..05 từ A4 (xem `09-REVIEW-edge-case-hunter.md`) |

→ **Phase A FR-01 Dashboard ready for Codex review (next step).**

---

## 7. Pending — Codex review

Sau A7 này, user yêu cầu chạy **/codex review TC vs SRS** để gate quality. Focus areas Codex sẽ rà:
- Enum exhaustive (KPI-03 5 sống / KPI-07 8 trạng thái loại trừ)
- BR-SLA-05 mẫu số semantic (HT đúng hạn vs HT + đang xử lý quá hạn)
- KPI-S-01 % point vs % relative (SPEC-CLARIFY-DASH-02)
- TPL-DASH-KPI 12 outputs verify đầy đủ
- Permission Matrix 8×7 cells effective
- Drill-down URL params chính xác (7 module target)

---

*Generated 2026-05-10 — Phase A7 (a7-filter-log)*
