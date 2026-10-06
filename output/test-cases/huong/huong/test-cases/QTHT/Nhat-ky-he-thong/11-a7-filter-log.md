# A7 Filter Log — UI/Function-Testable Filter (audit log)

> **Module**: QTHT Nhật ký Hệ thống (FR-VIII-28)
> **Ngày chạy**: 2026-05-08
> **Action**: Manual scan TC để LOẠI/SỬA TC chỉ-DB/API thuần. Tester chỉ chạy qua chrome-devtools MCP — KHÔNG curl/Postman/SQL trực tiếp.

---

## 1. A7 Filter Rule (plan §3.1)

- ❌ **LOẠI**: TC require query DB trực tiếp (vd "verify row trong bảng X", "check INDEX tồn tại"), TC require curl/Postman call API thuần (vd "POST /api/v1/... với header X"), TC verify cron job / queue / background worker không có UI feedback.
- ✏️ **SỬA**: TC có verification chỉ-DB → chuyển thành verification UI tương đương (vd "verify network request fired" thay "verify DB row"); TC API-only nếu module có UI bridge → re-route qua UI flow.
- ✅ **GIỮ**: TC chạy 100% qua UI/function user-facing — bao gồm verify network response qua MCP `list_network_requests` (API call gián tiếp khi user thao tác UI vẫn OK).

---

## 2. Scan kết quả — 54 TC

| TC ID | Action | Lý do |
|-------|--------|-------|
| TC-NK-101..113 | ✅ GIỮ | UI flow: navigate, filter, sort, pagination, expand JSON. Tất cả qua chrome-devtools MCP `click/fill/take_snapshot/list_network_requests`. |
| TC-NK-120..124 | ✅ GIỮ | Validation UI + toast + empty state. |
| TC-NK-130..133 | ✅ GIỮ | Sanitize qua filter input UI. Verify console không có alert (`list_console_messages`) + DB bảng còn nguyên (`evaluate_script` GET request). |
| TC-NK-134..136 | ✅ GIỮ | Boundary 89/90/91 ngày — set qua date-picker UI, verify toast. |
| TC-NK-137 | ✅ GIỮ | Timezone — verify qua filter UI + `list_network_requests` payload check timestamp. |
| TC-NK-138 | ✅ GIỮ | Dropdown empty state — UI behavior. |
| TC-NK-139 | ✅ GIỮ | Soft-delete user — verify dropdown UI behavior + filter result. |
| TC-NK-140 | ✅ GIỮ | Sort badge column — UI behavior. |
| TC-NK-141 | ✅ GIỮ | UI verify KHÔNG có nút Sửa/Xóa — pure UI scan. |
| TC-NK-142 | ✏️ SỬA → ✅ GIỮ | **Đã được rewrite** dùng `evaluate_script` trong devtools console UI context (KHÔNG curl thuần). MCP `evaluate_script` chạy JS trong tab đang mở của browser đã login → qualifies UI bridge. KHÔNG cần loại. |
| TC-NK-143 | ✅ GIỮ | Performance — đo qua `list_network_requests` response time. |
| TC-NK-144 | ✅ GIỮ | Reset filter — UI behavior. |
| TC-NK-EXP-001..006 | ✅ GIỮ | Export Excel — click nút UI + verify file download. |
| TC-NK-EXP-007..010 | ✅ GIỮ | Boundary export — UI flow + verify file row count. (Lưu ý: verify file `.xlsx` qua download + manual count, KHÔNG SQL trực tiếp.) |
| TC-NK-EXP-011 | ✅ GIỮ | Performance — đo qua network request. |
| TC-NK-EXP-012 | ✅ GIỮ | Download URL security — UI flow login khác user paste URL. |
| TC-NK-PERM-001..007 | ✅ GIỮ | Role-based access — UI login + URL navigate. |
| TC-NK-PERM-008 | ✅ GIỮ | UI scan KHÔNG có nút sửa/xóa. |
| TC-NK-PERM-009 | ✏️ SỬA → ✅ GIỮ | **Tương tự TC-NK-142** — `evaluate_script` qua devtools console (UI context) gửi DELETE/PATCH với JWT QTHT để verify BE reject. KHÔNG curl thuần. A7 OK. |

---

## 3. Tổng kết

| Action | Count |
|--------|------:|
| ✅ GIỮ (chạy qua MCP UI) | 54 |
| ✏️ SỬA (chuyển sang UI bridge) | 0 explicit (TC-NK-142, PERM-009 đã design ngay từ đầu với UI context — note ở C section file 03) |
| ❌ LOẠI (DB/API thuần) | 0 |

**A7 verdict: 0 TC LOẠI, 0 TC SỬA in-place. Tất cả TC chạy được qua chrome-devtools MCP.**

---

## 4. Note quan trọng cho Phase B

- **TC-NK-142 + TC-NK-PERM-009** là edge của A7 rule. Tester PHẢI chạy DELETE/PATCH qua **devtools console của browser đã login QTHT** (sử dụng MCP `evaluate_script`), KHÔNG được dùng Postman/curl bên ngoài. Lý do: devtools console kế thừa cookie/JWT của session đang đăng nhập → đây là UI bridge hợp lệ. Nếu tester chạy curl bên ngoài cần JWT thủ công, TC sẽ bị treat là API-only và bị LOẠI A7.

- **TC-NK-EXP-007/008/009/010** verify row count file Excel: Phase B tester có thể dùng MCP `evaluate_script` để parse file `.xlsx` blob nếu cần (FE đã download blob), hoặc manual count. KHÔNG được SQL `SELECT count(*)` trực tiếp.

- **TC-NK-130 (SQL injection)** verify "AUDIT_LOG còn data sau request" — Phase B dùng `list_network_requests` GET reload SCR-VIII-10 sau injection thay vì SQL count.

---

## 5. Comparison với sibling A7

| Module | TC LOẠI A7 | Lý do | Reference |
|--------|-----------|-------|-----------|
| Biểu mẫu (W2.3) | 1 (UC98 API) | API outbound thuần Cổng PLQG | bieu-mau/11-a7-filter-log.md |
| TVCS (W3.3) | 0 | UC149/151/153 đã thiết kế verify SIDE-EFFECT UI từ A3 | tv-chuyen-sau/11-a7-filter-log.md |
| Đào tạo (W3.4) | 1 (TC-NHCH-012 migration) | DB migration backfill thuần | dao-tao/11-a7-filter-log.md |
| **Nhật ký HT (W1.1)** | **0** | **Module fully UI-driven (read + filter + export). Verify immutability qua UI scan + devtools console (UI bridge).** | (file này) |
