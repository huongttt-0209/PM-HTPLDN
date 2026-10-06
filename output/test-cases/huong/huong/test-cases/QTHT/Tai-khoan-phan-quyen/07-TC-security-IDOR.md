# Test Cases — Security/IDOR Suite (Cross UC112-115 + FR-VIII-26)

> **SRS Ref**: BR-AUTH-01 (srs-fr-10:2155), BR-AUTH-09 (srs-fr-10:2197). Phụ lục này chứa các TC test direct API authorization qua devtools `fetch()` hoặc URL/payload injection — KHÔNG phải UI flow tester thông thường.
> **Ngày tạo**: 2026-05-08 (Codex R2 round — tách từ file UC 01-04, 06)
> **Tài khoản test**: Non-QTHT (cb_nv_*, cb_pd_*, dn_01...) — verify JWT authorization gating.

> **Lý do tách file:** Codex R2 review (2026-05-08) flag rằng các TC IDOR dùng `evaluate_script` + `fetch('/api/...')` thực chất là API authorization test "đội lốt" UI bridge. A7 rule cấm test API thuần. Tách ra suite riêng để **tester phụ trách security chạy bằng tool API (Postman/Burp/devtools)**, KHÔNG trộn vào functional UC suite.

> **Phase B execution note:** File này KHÔNG nằm trong B-block của todo.md functional UC. Phase B Security riêng (post-functional) sẽ pick suite này — hoặc dev/security team chạy như part of penetration test. Vẫn validate spec-defined behaviour (BR-AUTH-01 cấm non-QTHT mọi UC112-115).

---

## A. UC112 — Vai trò (1 TC)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-IDOR-VT-001 | BR-AUTH-01 (srs-fr-10:2155) | Non-QTHT direct POST /vai-tro qua fetch | `cb_nv_tw_01` đăng nhập (JWT hợp lệ). | `POST /api/v1/vai-tro` body `{"ma_vai_tro":"HACK","ten_vai_tro":"Hack"}` | 1. Login `cb_nv_tw_01`. 2. Devtools console: `fetch('/api/v1/vai-tro', {method:'POST', headers:{'Content-Type':'application/json','Authorization':'Bearer '+token}, body:JSON.stringify({ma_vai_tro:'HACK',ten_vai_tro:'Hack'})}).then(r=>r.status)`. | **STATE**: BE reject 403 Forbidden (BR-AUTH-01). VAI_TRO không có dòng "HACK". **API**: Status 403. | Negative | P0 |

---

## B. UC113 — Tài khoản (5 TC)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-IDOR-TK-001 | ERR-TK-05 (E5, srs-fr-10:721) | Đơn vị không tồn tại — inject don_vi_id=99999 qua devtools | `qtht_01` đang ở form Thêm TK. | `don_vi_id=99999` (FK injection) | 1. [+ Thêm]. 2. Chọn đơn vị bất kỳ. 3. Devtools: trước submit, intercept payload đổi don_vi_id thành 99999. 4. Submit. | **STATE**: BE reject 400. **API**: Toast/response ERROR "Đơn vị không tồn tại hoặc đã bị vô hiệu hóa" (srs-fr-10:721). | Negative | P0 |
| TC-IDOR-TK-002 | ERR-TK-06 (E6, srs-fr-10:722) | Vai trò ID inject 99999 | `qtht_01`. | `vai_tro_ids=[99999]` | 1. [+ Thêm]. 2. Chọn vai trò bất kỳ. 3. Devtools: thay vai_tro_ids → [99999]. 4. Submit. | **STATE**: BE reject. **API**: "Vai trò ID 99999 không tồn tại" (srs-fr-10:722). | Negative | P0 |
| TC-IDOR-TK-003 | BR-AUTH-09 (srs-fr-10:2197) | CB nội bộ KHÔNG được set vneid_subject khi tạo TK — inject field | `qtht_01`. | Inject `vneid_subject="cccd_qt"` payload | 1. Tạo TK NOI_BO với vai_tro=CB_NV. 2. Devtools: thêm vneid_subject vào payload. 3. Submit. | **STATE**: BE reject 400 hoặc bỏ qua field (BR-AUTH-09 srs-fr-10:2197). **API**: ERROR hoặc tạo thành công nhưng vneid_subject=NULL. | Negative | P1 |
| TC-IDOR-TK-004 | BR-AUTH-01 (srs-fr-10:2155) | Non-QTHT direct DELETE /tai-khoan/:id qua fetch | `cb_nv_tw_01`. | `DELETE /api/v1/tai-khoan/{qtht_01_id}` | 1. Login `cb_nv_tw_01`. 2. Devtools: DELETE qua fetch với JWT. | **STATE**: BE reject 403. qtht_01 vẫn còn HOAT_DONG. **API**: Status 403. | Negative | P0 |
| TC-IDOR-TK-005 | SM-TAIKHOAN guard (srs-fr-10:2114) | Cố mở khóa TK đang HOAT_DONG (SM invalid transition) qua API | `qtht_01`. TK m HOAT_DONG. | `PATCH /api/v1/tai-khoan/{m_id}/unlock` | 1. Devtools: gọi PATCH `/api/v1/tai-khoan/{m_id}/unlock`. | **STATE**: BE reject 400 "Tài khoản không ở trạng thái Tạm khóa". **API**: Verify guard SM-T8 enforce. | Negative | P1 |

---

## C. UC114 — Phân quyền dữ liệu (2 TC)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-IDOR-PQDL-001 | ERR-PQ-03 (E3, srs-fr-10:782) | Đơn vị ID không tồn tại — inject qua devtools | `qtht_01`. | `don_vi_ids=[99999]` (inject) | 1. Chọn vai trò. 2. Devtools: thay don_vi_ids trong payload. 3. Submit. | **STATE**: BE check FK exist → reject 400. **API**: "Đơn vị ID 99999 không tồn tại" (srs-fr-10:782). | Negative | P1 |
| TC-IDOR-PQDL-002 | BR-AUTH-01 (srs-fr-10:2155) | Non-QTHT direct PUT /phan-quyen-du-lieu qua fetch | `cb_nv_tw_01`. | PUT body bất kỳ | 1. Login `cb_nv_tw_01`. 2. Devtools: PUT /api/v1/phan-quyen-du-lieu với JWT. | **STATE**: BE reject 403. **API**: Status 403. **PERSIST**: Quyền không đổi. | Negative | P0 |

---

## D. UC115 — Phân quyền chức năng (2 TC)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-IDOR-PQCN-001 | ERR-PQ-04 (E2, srs-fr-10:834) | Quyền ID không tồn tại — inject qua devtools | `qtht_01`. | `quyen_ids=[99999]` (inject) | 1. Chọn vai trò. 2. Devtools: thay quyen_ids trong payload. 3. Submit. | **STATE**: BE check FK exist → reject 400. **API**: "Quyền chức năng ID 99999 không tồn tại" (srs-fr-10:834). | Negative | P1 |
| TC-IDOR-PQCN-002 | BR-AUTH-01 (srs-fr-10:2155) | Non-QTHT direct PUT /phan-quyen-chuc-nang qua fetch | `cb_nv_tw_01`. | PUT body bất kỳ | 1. Login `cb_nv_tw_01`. 2. Devtools: PUT /api/v1/phan-quyen-chuc-nang với JWT. | **STATE**: BE reject 403. **API**: Status 403. | Negative | P0 |

---

## E. Cross-FR IDOR — Direct API call với JWT non-QTHT (6 TC)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-IDOR-PERM-001 | BR-AUTH-01 IDOR (UC112) | `cb_nv_tw_01` direct POST /vai-tro qua fetch | `cb_nv_tw_01`. | POST /api/v1/vai-tro body | 1. Login `cb_nv_tw_01`. 2. Devtools `evaluate_script` POST. | **STATE**: BE reject 403. VAI_TRO unchanged. **API**: Status 403. (Note: trùng case TC-IDOR-VT-001 — giữ ở suite cross để nhóm IDOR matrix theo role.) | Negative | P0 |
| TC-IDOR-PERM-002 | BR-AUTH-01 IDOR (UC112) | DELETE /vai-tro/:id từ JWT non-QTHT | `cb_pd_tw_01`. | DELETE /api/v1/vai-tro/{QTHT_id} | 1. Login `cb_pd_tw_01`. 2. Devtools DELETE. | **STATE**: 403. **API**: KHÔNG xóa được vai trò QTHT. | Negative | P0 |
| TC-IDOR-PERM-003 | BR-AUTH-01 IDOR (UC113) | POST /tai-khoan từ non-QTHT | `cb_nv_bn_01`. | POST /api/v1/tai-khoan body | 1. Login. 2. Devtools POST. | **STATE**: 403. | Negative | P0 |
| TC-IDOR-PERM-004 | BR-AUTH-01 IDOR (UC113) | PATCH /tai-khoan/:id/lock từ non-QTHT (cố khóa TK QTHT) | `cb_nv_dp_01`. | PATCH /api/v1/tai-khoan/{qtht_01_id}/lock | 1. Login. 2. Devtools PATCH. | **STATE**: 403. qtht_01 vẫn HOAT_DONG. | Negative | P0 |
| TC-IDOR-PERM-005 | BR-AUTH-01 IDOR (UC114) | PUT /phan-quyen-du-lieu từ non-QTHT | `cb_pd_bn_01`. | PUT body | 1. Login. 2. Devtools PUT. | **STATE**: 403. | Negative | P0 |
| TC-IDOR-PERM-006 | BR-AUTH-01 IDOR (UC115) | PUT /phan-quyen-chuc-nang từ non-QTHT | `cb_pd_dp_01`. | PUT body | 1. Login. 2. Devtools PUT. | **STATE**: 403. | Negative | P0 |

---

## Tổng số TC: 16 (1 + 5 + 2 + 2 + 6) — moved từ 5 file UC

**Priority**: P0=11 / P1=5

**Coverage:**
- BR-AUTH-01 IDOR matrix: 4 UC × 2-3 method (POST/PUT/PATCH/DELETE) = full
- BR-AUTH-09: TC-IDOR-TK-003 (vneid_subject inject — verify CB không sync VNeID)
- ERR-TK-05/06 + ERR-PQ-03/04: FK injection negative
- SM-T8 invalid transition guard: TC-IDOR-TK-005

---

## Note về A7 + Phase B execution

> **Đây KHÔNG phải UC functional suite.** File này:
> - KHÔNG có B-block trong todo.md cho Phase B functional run.
> - Tester functional KHÔNG chạy file này — security/dev team chạy như part of pen-test hoặc API authz test.
> - Spec-defined behavior (BR-AUTH-01 + BR-AUTH-09 + ERR codes) vẫn được verify, nhưng qua tool security (Postman/Burp/devtools) thay vì MCP chrome-devtools UI flow.
> - **A7 compliant** vì các TC này được TÁCH RA, không lẫn trong functional suite.
