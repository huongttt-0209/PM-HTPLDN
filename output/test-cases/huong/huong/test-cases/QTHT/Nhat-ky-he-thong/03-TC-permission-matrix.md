# Test Cases — Permission Matrix Cross-cutting (FR-VIII-28 / BR-AUTH-01 + BR-DATA-05)

> **SRS Ref**: BR-AUTH-01 (srs-v3.1.md §B.1, srs-fr-10:1343, 1372), BR-DATA-05 (srs-v3.1.md:5330 — immutable), Permission matrix module-level (xem 00-test-plan-overview §2.3)
> **Ngày tạo**: 2026-05-08 (BMAD A3, A4 inline merge)
> **Pattern reference**: `output/test-cases/bieu-mau/07-TC-permission-matrix.md`

> **Iron rule:** Chỉ QTHT đọc được. KHÔNG ai (kể cả QTHT) sửa/xóa AUDIT_LOG.

---

## A. ROLE-BASED ACCESS HAPPY PATH

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-NK-PERM-001 | BR-AUTH-01 + AC1 | QTHT đọc được toàn HT (cross-don_vi) | `qtht_01` đăng nhập. Seed AUDIT_LOG đa cấp TW + BN + ĐP. | — | 1. Mở SCR-VIII-10. 2. Quan sát cột "Đơn vị". | **STATE**: BE bypass `don_vi_id` filter cho QTHT (BR-AUTH-08 ngoại lệ — pattern từ FR-09). **UI**: Bảng hiển thị log từ TW + BN + ĐP. Cột "Đơn vị" có ≥ 3 giá trị khác nhau (TW, BN, ĐP). **PERSIST**: — | Happy | P0 |
| TC-NK-PERM-002 | BR-AUTH-01 + AC2 | QTHT export Excel chứa log toàn HT | `qtht_01`. Tương tự TC-001. | — | 1. Export file. 2. Mở file. | **STATE**: BE export không filter `don_vi_id`. **UI**: File chứa cả 3 cấp. **PERSIST**: — | Happy | P1 |

---

## B. NEGATIVE — NON-QTHT BLOCK

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-NK-PERM-003 | ERR-LOG-01 + AC3 | CB_NV_TW không truy cập được SCR-VIII-10 | `cb_nv_tw_01` đăng nhập. | — | 1. Direct URL `/quan-tri/audit-log` (hoặc menu nếu có). | **STATE**: BE reject 403 (BR-AUTH-01 + ERR-LOG-01). **UI**: Hai option hợp lệ: (a) HTTP 403 page với toast "Bạn không có quyền truy cập nhật ký hệ thống" (srs-fr-10:1362); (b) Sidebar không có entry → URL direct redirect về home. **PERSIST**: — | Negative | P0 |
| TC-NK-PERM-004 | ERR-LOG-01 + AC3 | CB_NV_BN không truy cập được | `cb_nv_bn_01`. | — | 1. URL direct. | **STATE/UI/PERSIST**: Same TC-003. | Negative | P0 |
| TC-NK-PERM-005 | ERR-LOG-01 + AC3 | CB_NV_DP không truy cập được | `cb_nv_dp_01`. | — | 1. URL direct. | **STATE/UI/PERSIST**: Same TC-003. | Negative | P1 |
| TC-NK-PERM-006 | ERR-LOG-01 + AC3 | CB_PD (TW/BN/DP) không truy cập được | `cb_pd_tw_01`, `cb_pd_bn_01`, `cb_pd_dp_01` (3 lượt). | — | 1. Mỗi tài khoản, URL direct. | **STATE/UI/PERSIST**: Same TC-003 cho cả 3 tài khoản. Sidebar không có menu Nhật ký. | Negative | P1 |
| TC-NK-PERM-007 | BR-AUTH-01 Tier 2 | DN/CG/TVV/NHT (Tier 2 SSO) không có entry vào CMS | `dn_01`, `cg_01`, `tvv_01`, `nht_01` (4 lượt). | — | 1. Mỗi tài khoản, URL direct CMS `/quan-tri/audit-log`. | **STATE**: Tier 2 SSO VNeID/Email không vào được CMS app — chỉ truy được Cổng PLQG. **UI**: Redirect về Cổng PLQG hoặc 403/login page CMS. **PERSIST**: — | Negative | P0 |

---

## C. IMMUTABILITY (BR-DATA-05) — KHÔNG AI ĐƯỢC SỬA/XÓA

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-NK-PERM-008 | BR-DATA-05 immutable (A4 merged) | QTHT KHÔNG có nút Sửa/Xóa trên SCR-VIII-10 | `qtht_01`. ≥ 1 bản ghi. | — | 1. Mở SCR-VIII-10. 2. Quan sát toolbar + bảng + context menu (right-click). | **STATE**: A.3 + BR-DATA-05 nguyên văn "không bao giờ bị xóa, INSERT-only". **UI**: KHÔNG có nút [Sửa] / [Xóa]. KHÔNG có cột "Hành động" trên bảng. KHÔNG context menu sửa/xóa. Chỉ có [Xuất Excel] + [Tìm kiếm] + [Xóa bộ lọc]. **PERSIST**: — | Negative | P0 |
| TC-NK-PERM-009 | BR-DATA-05 immutable backend (A4 merged) | Backend reject DELETE/PATCH endpoint trên AUDIT_LOG dù QTHT | `qtht_01`. Audit log id biết trước. | DELETE /api/audit-log/:id; PATCH /api/audit-log/:id (qua MCP `evaluate_script` trong UI context — KHÔNG curl thuần) | 1. Login `qtht_01`. 2. Devtools console: `fetch('/api/audit-log/'+id, {method:'DELETE', headers:{Authorization:'Bearer '+token}})`. 3. Kiểm tra status code + GET lại để verify. | **STATE**: BE reject 405 Method Not Allowed hoặc 403 Forbidden. AUDIT_LOG vẫn đầy đủ. **UI**: KHÔNG có endpoint UI nào trigger DELETE/PATCH. **PERSIST**: Reload SCR-VIII-10, bản ghi vẫn còn. | Negative | P1 |

---

## Tổng số TC: 9 (2 Happy + 5 Negative role-block + 2 Immutability) — A3 base 7 + A4 merged 2
**Priority**: P0=5 / P1=4 / P2=0

**Coverage:**
- BR: BR-AUTH-01 (Tier 1+2 + chỉ QTHT), BR-DATA-05 (immutable verify), BR-AUTH-08 (cross-don_vi QTHT exception)
- AC SRS: AC3 ✅ (TC003-007 — user không có quyền QTHT từ chối truy cập)
- Error codes: ERR-LOG-01 (TC003-006)
- Roles tested: QTHT (full + immutable), CB_NV (TW/BN/DP), CB_PD (TW/BN/DP), Tier 2 (DN/CG/TVV/NHT)
- A4 merged 2026-05-08: TC008-009 (immutability UI + backend)

---

## D. Note về A7 — UI vs API

> TC-NK-PERM-009 dùng `evaluate_script` trong UI context (devtools console của browser đã login QTHT) chứ KHÔNG phải curl/Postman thuần. Theo plan §3.1 A7 rule, đây là VALID UI-bridge: tester thao tác qua devtools mà MCP `evaluate_script` đã hỗ trợ → KHÔNG bị LOẠI A7.
