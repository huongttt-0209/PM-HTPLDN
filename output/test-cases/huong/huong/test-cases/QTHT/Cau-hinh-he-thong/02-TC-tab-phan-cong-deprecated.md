# Test Cases — Tab 2: Phân công mặc định (FR-II-NEW-01 ⚠️ ĐÃ BỎ)

> **SRS Ref**: FR-II-NEW-01 ĐÃ BỎ (srs-fr-02:885-887, BA chốt 2026-05-07 Q11), Entity CAU_HINH_PHAN_CONG ĐÃ BỎ (srs-fr-02:1461). SCR-VIII-06 line 1647-1653 vẫn render Tab 2 (UI spec chưa update theo business spec).
> **Ngày tạo**: 2026-05-08 (BMAD A3, A4 inline merge); CAUHINH-01 RESOLVED 2026-05-08
> **Tài khoản chính**: `qtht_01`
> **URL:** `/quan-tri/cau-hinh` → Tab 2

> **CAUHINH-01 RESOLVED 2026-05-08 (theo business spec):** FR-II-NEW-01 đã BỎ (BA Q11) + entity bỏ → **business spec thắng**. Expected behavior: Tab 2 **ẨN khỏi tab list** HOẶC **hiển thị deprecation banner** (cả 2 đều acceptable). **NẾU Tab 2 vẫn render bảng CRUD cũ → BUG implementation chưa update theo BA Q11.** SCR-VIII-06 line 1647-1653 (UI spec) coi như chưa sync — KHÔNG dùng làm chuẩn test.

> **Pre-condition:** `qtht_01` đăng nhập, vào SCR-VIII-06.

---

## A. DEPRECATION VERIFICATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-CH-PC-001 | CAUHINH-01 RESOLVED (theo business — FR-II-NEW-01 BỎ) | Tab 2 ẨN/banner — verify implementation tuân business spec | `qtht_01`. | — | 1. Login. 2. Vào /quan-tri/cau-hinh. 3. Quan sát tab list. | **STATE**: BE/UI tuân BA Q11 BỎ. **UI**: 2 behavior PASS: (a) Tab 2 **ẨN khỏi tab list**; (b) Tab 2 hiển thị **với deprecation banner** "Tính năng đã bỏ. FR-II-06 dùng auto-filter 4 tiêu chí thay thế." + nội dung empty. **BEHAVIOR (c) FAIL = BUG: Tab 2 vẫn render bảng CRUD cũ → BUG implementation chưa update theo BA Q11 (severity High).** **PERSIST**: — | Negative | P0 |
| TC-CH-PC-002 | srs-fr-02:1461 entity bỏ | Backend reject mọi GET/POST `/api/cau-hinh-phan-cong` | `qtht_01`. | GET / POST endpoint cũ | 1. Devtools console: `fetch('/api/cau-hinh-phan-cong', {method:'GET'})`. 2. Tương tự POST + DELETE. | **STATE**: BE return 404 Not Found hoặc 410 Gone (entity đã bỏ). **UI**: KHÔNG có endpoint trong Network. **PERSIST**: — | Negative | P1 |
| TC-CH-PC-003 | A4 cross-FR (A4 merged) | FR-II-06 auto-filter 4 tiêu chí thay thế hoạt động | `qtht_01` + `cb_nv_tw_01`. Có ≥ 1 hỏi đáp DUY_TIEP_NHAN cần phân công. | — | 1. Login `cb_nv_tw_01`. 2. Vào Hỏi đáp → Phân công. 3. Verify auto-filter dropdown CB phụ trách áp 4 tiêu chí: lĩnh vực + đơn vị + workload + FIFO (srs-fr-02:887). | **STATE**: BE auto-filter từ `TU_VAN_VIEN.linh_vuc_chuyen_mon`, `NGUOI_HO_TRO.linh_vuc_ids[]`, etc. **UI**: Dropdown CB phụ trách filter sẵn theo 4 tiêu chí. **PERSIST**: — Note: TC này thực tế thuộc W3.1 Hỏi đáp; ở đây chỉ verify cross-reference rằng cấu hình tĩnh không cần. | Edge | P1 |

---

## Tổng số TC: 3 (3 Negative/Edge — minimal vì FR đã bỏ)
**Priority**: P0=1 / P1=2 / P2=0

**Coverage:**
- SPEC-CLARIFY-CAUHINH-01 (TC-001)
- Verify endpoint cũ deprecated (TC-002)
- Cross-FR replacement FR-II-06 (TC-003)

> **Note Phase B:** File này minimal vì FR-II-NEW-01 đã bỏ (BA Q11). Nếu Phase B phát hiện Tab 2 vẫn render bảng CRUD cũ → log bug "Tab 2 chưa được ẩn theo BA chốt 2026-05-07 Q11". Nếu Tab 2 ẨN hoặc hiển thị deprecation banner → đúng spec final.
