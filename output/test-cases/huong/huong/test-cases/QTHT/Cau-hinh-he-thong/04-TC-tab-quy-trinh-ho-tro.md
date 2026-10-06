# Test Cases — Tab 4: Quy trình hỗ trợ (snapshot config)

> **SRS Ref**: SCR-VIII-06 Tab 4 (srs-fr-10:1669-1676), Entity `CAU_HINH_QUY_TRINH_VV` (snapshot pattern)
> **Ngày tạo**: 2026-05-08 (BMAD A3, A4 inline merge)
> **Tài khoản chính**: `qtht_01` (chỉ QTHT — line 1682)
> **URL:** `/quan-tri/cau-hinh` → Tab 4

> **SPEC-CLARIFY-CAUHINH-02:** SCR-VIII-06 line 1612 ghi `FR-VIII-25` (Đồng bộ VNeID) — không match Tab 4 (Quy trình HTPL). Spec field detail (`ten_buoc / SLA per-step / phan_cong_tu_dong`) chưa có ở srs-fr-10. Cần BA cung cấp FR đầy đủ — TC mức happy path basic.

> **SPEC-CLARIFY-CAUHINH-08:** Spec Tab 4 chỉ có 4 component-level (bảng / nút thêm / alert snapshot / nút lưu) — KHÔNG có chi tiết field, validation, error code. TC viết theo pattern Vụ việc CR-NEW-01 (versioning quy trình) tham chiếu, defer detailed validation đến khi BA cung cấp spec.

> **Pre-condition:** `qtht_01` đăng nhập, vào SCR-VIII-06 Tab 4. Seed CAU_HINH_QUY_TRINH_VV ≥ 1 quy trình DEFAULT.

---

## A. HAPPY PATH — VIEW + ADD STEP

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-CH-QT-001 | line 1673 | Tab 4 hiển thị bảng các bước quy trình | `qtht_01`. ≥ 3 bước seed (Tiếp nhận / Phân công / Phản hồi). | — | 1. Tab 4. 2. Quan sát bảng. | **STATE**: BE GET `/api/cau-hinh-quy-trinh-vv`. **UI**: Bảng cột "Thứ tự / Tên bước / SLA per-step / Phân công tự động / Hành động". Sắp xếp theo thu_tu ASC. **PERSIST**: — | Happy | P0 |
| TC-CH-QT-002 | line 1675 alert | Cảnh báo snapshot hiển thị | `qtht_01`. | — | 1. Tab 4. 2. Quan sát alert box. | **UI**: Alert nguyên văn "Khi thay đổi quy trình, hồ sơ đang xử lý giữ nguyên quy trình cũ (snapshot). Chỉ hồ sơ mới áp dụng quy trình mới" (line 1675). | Happy | P1 |
| TC-CH-QT-003 | line 1674 | Click [+ Thêm bước] mở modal CRUD | `qtht_01`. | — | 1. Click [+ Thêm bước]. | **UI**: Modal hiển thị form các field tên bước / SLA / phân công auto. (Spec field chưa rõ — defer detailed validation.) | Happy | P1 |
| TC-CH-QT-004 | line 1676 + BR-DATA-05 | Click [Lưu cấu hình quy trình] | `qtht_01`. Đã sửa ≥ 1 bước. | — | 1. Sửa thu_tu/ten_buoc. 2. Save. | **STATE**: BE PATCH/PUT. AUDIT_LOG action=UPDATE entity=CAU_HINH_QUY_TRINH_VV. **UI**: Toast success. | Happy | P0 |

---

## B. SNAPSHOT BEHAVIOR

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-CH-QT-010 | line 1675 + line 1697 (A4 merged) | **Snapshot pattern: VV đang xử lý giữ quy trình cũ** | `qtht_01`. Seed: 1 VV state DANG_XU_LY tạo trước khi sửa Tab 4 quy trình. | Sửa quy trình thêm bước "Bước 4 mới" | 1. Sửa quy trình. 2. Save. 3. Mở VV đó. 4. Quan sát các bước. | **STATE**: VV vẫn theo quy trình cũ (3 bước cũ). **UI**: Tab/section "Quy trình" trên VV detail KHÔNG có "Bước 4 mới". **PERSIST**: VV.cau_hinh_quy_trinh_id trỏ về snapshot version cũ. | Edge | P0 |
| TC-CH-QT-011 | line 1675 (A4 merged) | **Snapshot pattern: VV mới áp quy trình mới** | `qtht_01`. Sau TC-010. | — | 1. Tạo VV mới (qua FR-V.I-03). 2. Quan sát quy trình. | **STATE**: VV mới có quy trình version mới (4 bước). **UI**: Tab "Quy trình" hiển thị 4 bước. **PERSIST**: — | Edge | P0 |

---

## C. PERMISSION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-CH-QT-020 | line 1682 | CB_NV_TW không thấy Tab 4 | `cb_nv_tw_01`. | — | 1. Vào /quan-tri/cau-hinh. | **UI**: Tab 4 ẨN. CB_NV chỉ thấy Tab 3. | Negative | P0 |
| TC-CH-QT-021 | line 1682 | CB_PD không thấy Tab 4 | `cb_pd_tw_01`. | — | Tương tự. | **UI**: Tab 4 ẨN. | Negative | P0 |
| TC-CH-QT-022 | BR-AUTH-01 Tier 2 | DN không vào CMS | `dn_01`. | — | 1. URL direct. | 403/redirect. | Negative | P1 |

---

## D. EDGE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-CH-QT-030 | BR-EC-01 (A4 merged) | Optimistic lock — 2 QTHT sửa cùng lúc | `qtht_01` + `qtht_02`. | Concurrent | 1. 2 tab. 2. Save lệch. | BE 409 cho save thứ 2. Toast WARNING. | Edge | P1 |
| TC-CH-QT-031 | BR-DATA-05 (A4 merged) | Audit log delta khi sửa quy trình | `qtht_01`. Sau TC-004. | — | 1. Vào Nhật ký HT. 2. Filter entity=CAU_HINH_QUY_TRINH_VV. | AUDIT_LOG có chi_tiet old/new. | Edge | P1 |
| TC-CH-QT-032 | A4 immutable snapshot (A4 merged) | Verify VV cũ KHÔNG nhảy sang quy trình mới khi reload | `qtht_01`. VV TC-010 đang xử lý. | — | 1. Reload VV detail nhiều lần. | UI luôn hiển thị quy trình cũ. | Edge | P1 |

---

## Tổng số TC: 12 (4 Happy + 2 Snapshot + 3 Permission + 3 Edge) — minimal vì spec field chưa đầy đủ
**Priority**: P0=5 / P1=7 / P2=0

**Coverage:**
- BR: BR-AUTH-01 (TC-020-022), BR-DATA-05 (TC-031), BR-EC-01 (TC-030)
- Snapshot pattern: ✅ (TC-010, 011, 032)
- A4 merged 2026-05-08: TC-010, TC-011, TC-030, TC-031, TC-032
- SPEC-CLARIFY: CAUHINH-02 (FR ref), CAUHINH-08 (field detail) → P0 escalate BA

> **Note Phase B:** TC file này chờ BA cung cấp spec field chi tiết (`ten_buoc / SLA per-step / phan_cong_tu_dong`). Nếu Phase B phát hiện Tab 4 implement đầy đủ field validation → bổ sung TC chi tiết theo spec. Hiện tại TC happy path basic + permission + snapshot pattern là tối thiểu.
