# A7 Filter Log — UI/Function-Testable Filter (audit log)

> **Module**: QTHT Cấu hình Hệ thống (SCR-VIII-06 + FR-VIII-29)
> **Ngày chạy**: 2026-05-08
> **Action**: Manual scan TC để LOẠI/SỬA TC chỉ-DB/API thuần. Tester chỉ chạy qua chrome-devtools MCP — KHÔNG curl/Postman/SQL trực tiếp.

---

## 1. A7 Filter Rule (plan §3.1)

- ❌ **LOẠI**: TC require query DB trực tiếp, TC require curl/Postman thuần, TC verify cron job / queue / background worker không có UI feedback.
- ✏️ **SỬA**: TC có verification chỉ-DB → chuyển thành verification UI tương đương (vd "verify network request fired" thay "verify DB row").
- ✅ **GIỮ**: TC chạy 100% qua UI/function user-facing — bao gồm verify network response qua MCP `list_network_requests` + `evaluate_script` trong UI context.

---

## 2. Scan kết quả — 124 TC

### File 01-TC-tab-sla.md (27 TC)

| TC ID range | Action | Note |
|-------------|--------|------|
| TC-CH-SLA-001..009 | ✅ GIỮ | UI inline edit + toggle, click [Lưu] qua MCP `click/fill/take_snapshot`. |
| TC-CH-SLA-010..015 | ✅ GIỮ | Validation UI + toast. |
| TC-CH-SLA-020..022 | ✅ GIỮ | Snapshot pattern verify qua mở HS detail trên menu Vụ việc — UI flow. |
| TC-CH-SLA-030..032 | ✅ GIỮ | Tab gating + URL direct verify qua UI. |
| TC-CH-SLA-040..043 | ✅ GIỮ | Optimistic lock qua 2 tab MCP; audit log delta verify qua màn hình Nhật ký HT (W1.1). |

**Note TC-CH-SLA-022:** Race condition (concurrent save SLA + create HS). A7 OK vì test qua 2 tab MCP `new_page` parallel — KHÔNG cần curl thuần.

### File 02-TC-tab-phan-cong-deprecated.md (3 TC)

| TC ID | Action | Note |
|-------|--------|------|
| TC-CH-PC-001 | ✅ GIỮ | UI scan Tab 2 — verify behavior. |
| TC-CH-PC-002 | ✏️ SỬA → ✅ GIỮ | **Đã design** dùng `evaluate_script` qua devtools console (UI context với JWT của session đang login) — A7 OK. |
| TC-CH-PC-003 | ✅ GIỮ | Cross-FR verify qua UI Hỏi đáp. |

### File 03-TC-tab-mau-phan-hoi.md (41 TC)

| TC ID range | Action | Note |
|-------------|--------|------|
| TC-CH-MPH-001..008 | ✅ GIỮ | CRUD + sanitize XSS qua UI modal. |
| TC-CH-MPH-010..014 | ✅ GIỮ | READ scope verify qua UI bảng + filter. |
| TC-CH-MPH-020..022 | ✅ GIỮ | UPDATE/DELETE/Toggle qua UI. |
| TC-CH-MPH-030..032 | ✅ GIỮ | Validation UI inline error. |
| TC-CH-MPH-033..038 | ✏️ SỬA → ✅ GIỮ | **`evaluate_script` UI context** cho test BE check direct API (ERR-MPH-04/05/06). KHÔNG curl thuần — UI bridge. |
| TC-CH-MPH-040..050 | ✅ GIỮ | Filter / search / pagination / modal — UI behavior. |
| TC-CH-MPH-060..062 | ✅ GIỮ | Sanitize qua search box + verify qua `list_console_messages` + reload. |
| TC-CH-MPH-063..068 | ✅ GIỮ | Concurrent edit (2 tab), boundary, IDOR (`evaluate_script`), dropdown FR-II-07 cross-module — UI flow. |

### File 04-TC-tab-quy-trinh-ho-tro.md (12 TC)

| TC ID range | Action | Note |
|-------------|--------|------|
| TC-CH-QT-001..004 | ✅ GIỮ | UI bảng + modal. |
| TC-CH-QT-010..011 | ✅ GIỮ | Snapshot pattern qua mở VV detail. |
| TC-CH-QT-020..022 | ✅ GIỮ | Tab gating + permission UI. |
| TC-CH-QT-030..032 | ✅ GIỮ | Optimistic lock + audit log + reload — UI flow. |

### File 05-TC-ngay-le.md (22 TC)

| TC ID range | Action | Note |
|-------------|--------|------|
| TC-CH-NL-001..006 | ✅ GIỮ | CRUD modal qua UI. |
| TC-CH-NL-010..014 | ✅ GIỮ | Validation UI. |
| TC-CH-NL-020..024 | ✅ GIỮ | Import Excel qua UI upload — `mcp__chrome-devtools__upload_file`. Verify file row count qua bảng refresh. |
| TC-CH-NL-030 | ✅ GIỮ | Calendar view — UI toggle. |
| TC-CH-NL-040..041 | ✅ GIỮ | Integration e2e qua mở VV detail trên menu Vụ việc — UI flow. |
| TC-CH-NL-050..051 | ✅ GIỮ | Permission UI. |

### File 06-TC-permission-matrix.md (19 TC)

| TC ID range | Action | Note |
|-------------|--------|------|
| TC-CH-PERM-001..007 | ✅ GIỮ | Tab gating UI. |
| TC-CH-PERM-010..012 | ✅ GIỮ | Cross-don_vi isolation qua bảng. |
| TC-CH-PERM-020..021 | ✅ GIỮ | Tier 2 block qua URL direct. |
| TC-CH-PERM-030..033 | ✅ GIỮ | Element gating UI (disabled state, tooltip, read-only field). |
| TC-CH-PERM-040..043 | ✏️ SỬA → ✅ GIỮ | **`evaluate_script` UI context** cho IDOR + cross-cấp BE check — A7 OK. |

---

## 3. Tổng kết

| Action | Count |
|--------|------:|
| ✅ GIỮ (chạy qua MCP UI) | 124 |
| ✏️ SỬA (chuyển sang UI bridge) | 0 explicit (TC dùng `evaluate_script` đã design ngay từ A3 với UI context — pattern từ W1.1) |
| ❌ LOẠI (DB/API thuần) | 0 |

**A7 verdict: 0 TC LOẠI, 0 TC SỬA in-place. Tất cả 124 TC chạy được qua chrome-devtools MCP.**

---

## 4. Note quan trọng cho Phase B

- **TC-CH-MPH-033..038, TC-CH-PERM-040..042, TC-CH-PC-002** dùng `evaluate_script` qua **devtools console của browser đã login user tương ứng** (UI bridge hợp lệ). KHÔNG được dùng Postman/curl bên ngoài. Lý do: devtools console kế thừa cookie/JWT của session đang đăng nhập → UI context hợp lệ. Nếu tester chạy curl bên ngoài cần JWT thủ công, TC sẽ bị treat là API-only và bị LOẠI A7.

- **TC-CH-NL-020..024 Import Excel:** Phase B dùng MCP `mcp__chrome-devtools__upload_file` để upload file `.xlsx` đã prepare sẵn. Verify row count qua bảng refresh + manual count.

- **TC-CH-NL-040..041 Integration:** Phase B sau khi seed ngày lễ → tạo VV mới qua UI Vụ việc → quan sát deadline VV detail. KHÔNG SQL trực tiếp `SELECT deadline FROM VU_VIEC`.

- **TC-CH-SLA-005, TC-CH-SLA-009 (toggle gửi email/TB app):** Phase B chỉ verify được toggle persist + reload + UI behavior. Verify scheduled job thực sự không gửi email/TB là cross-FR test thuộc FR-II-CROSS-01 (cron job) — defer hoặc partial verify.

- **TC-CH-MPH-068 (dropdown FR-II-07):** Phase B sang menu Hỏi đáp → soạn phản hồi → verify dropdown chèn mẫu hiển thị đúng 2 nhóm. Cross-module verify hợp lệ qua UI flow.

---

## 5. Comparison với sibling A7

| Module | TC LOẠI A7 | Lý do | Reference |
|--------|-----------|-------|-----------|
| Biểu mẫu (W2.3) | 1 (UC98 API) | API outbound thuần Cổng PLQG | bieu-mau/11-a7-filter-log.md |
| Đào tạo (W3.4) | 1 (TC-NHCH-012 migration) | DB migration backfill thuần | dao-tao/11-a7-filter-log.md |
| Nhật ký HT (W1.1) | 0 | Module fully UI-driven; verify immutability qua UI scan + devtools console | Nhat-ky-he-thong/11-a7-filter-log.md |
| **Cấu hình HT (W1.2)** | **0** | **Module fully UI-driven; cross-cấp BE check qua `evaluate_script` UI bridge; integration e2e qua UI flow.** | (file này) |
