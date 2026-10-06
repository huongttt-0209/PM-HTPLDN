# Test Cases — FR-X.3-01 (UC159): Liên kết Vụ việc N:N + Xóa chặn

> **SRS Ref**: FR-X.3-01, SCR-X3-01 row#7 (Accordion "Vụ việc liên kết"), business-flow §⑩ FR-14 + §3 (junction `HD_VV`), Entity HOP_DONG_TU_VAN ↔ VU_VIEC (M2M)
> **Ngày tạo**: 2026-05-10
> **Đặc thù**: Many-to-many. Modal multi-select chọn VV. Lọc VV theo BR-AUTH-08 (chỉ VV cùng đơn vị). Bỏ liên kết. Xóa HĐ chặn nếu còn VV (E4 ERR-HDTV-04).

---

## Quy ước

- **Priority**: 🔴 P0 · 🟡 P1 · 🟢 P2
- **TraceID**: `FR-X.3-01 / Vụ việc liên kết`
- **Pre-conditions mặc định**: cb_nv_tw_01 login. ≥3 VV thuộc đơn vị TW: V001 ("VV DN ABC"), V002, V003. HĐ "HDTV-link-01" tồn tại.

---

## Trường input (VV liên kết — Accordion 2)

| # | Field | Bắt buộc | Kiểu | Ràng buộc |
|---|-------|----------|------|-----------|
| 1 | vu_viec_ids[] | N | identifier[] | FK[] → VU_VIEC; lọc BR-AUTH-08 (đơn vị user); M2M |

---

## A. LIÊN KẾT VV — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-LVV-001 | FR-X.3-01 / Processing step 6 | Liên kết HĐ với 2 VV qua modal multi-select | Form Sửa HĐ "HDTV-link-01" mở. | vu_viec_ids=[V001, V002] | 1. Mở accordion "VV liên kết". 2. Click [+ Liên kết VV]. 3. Modal mở, multi-select V001 + V002. 4. [Xác nhận]. 5. [Lưu] HĐ. | (1) POST junction `HD_VV` 2 row (hd_id, V001), (hd_id, V002). (2) Bảng accordion list 2 VV: cột Mã VV / Tên DN / Lĩnh vực / Trạng thái / [Bỏ liên kết]. (3) Cột "Số VV liên kết" trên danh sách HĐ = 2 (badge). (4) Audit log INSERT. | Happy 🔴 |
| TC-LVV-002 | FR-X.3-01 / N:N | 1 VV liên kết nhiều HĐ (M2M test) | HĐ "HDTV-A" đã link V001. HĐ "HDTV-B" tồn tại. | HDTV-B link V001 | 1. Mở Form Sửa HDTV-B. 2. Liên kết V001. 3. [Lưu]. | (1) Junction có cả (HDTV-A, V001) + (HDTV-B, V001). (2) Detail VV V001 hiển thị 2 HĐ liên kết. | Happy 🟡 |
| TC-LVV-003 | FR-X.3-01 / Bỏ liên kết | Bỏ liên kết 1 VV khỏi HĐ | HĐ "HDTV-link-01" link V001 + V002. | Bỏ link V002 | 1. Form Sửa HĐ. 2. Accordion VV liên kết. 3. Click [Bỏ liên kết] trên row V002. 4. Confirm. 5. [Lưu]. | (1) DELETE junction (hd_id, V002). (2) Bảng còn 1 VV (V001). (3) Cột "Số VV" trên list = 1. (4) Audit log DELETE link. | Happy 🔴 |

---

## B. LIÊN KẾT VV — NEGATIVE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-LVV-010 | FR-X.3-01 / E4 ERR-HDTV-04 | Xóa HĐ đang link VV — chặn | HĐ "HDTV-link-01" link V001. | — | 1. Quay về danh sách HĐ. 2. Click Xóa HDTV-link-01. 3. Confirm. | (1) Reject: **"Không thể xóa hợp đồng đang có vụ việc liên kết"** (ERR-HDTV-04). (2) HĐ tồn tại. (3) KHÔNG audit DELETE HĐ. | Negative 🔴 |
| TC-LVV-011 | FR-X.3-01 / BR-AUTH-08 | cb_nv_dp_01 (Sở TP AG) chỉ thấy VV thuộc AG trong modal liên kết | cb_nv_dp_01 login. VV V001 thuộc TW. VV V_AG_01 thuộc AG. | — | 1. Mở Form Sửa HĐ thuộc AG. 2. Click [+ Liên kết VV]. 3. Search "" (all). | (1) Modal chỉ list VV của AG (V_AG_01). (2) KHÔNG hiển thị V001 (TW). (BR-AUTH-08 enforce). | Negative 🔴 |

---

## C. LIÊN KẾT VV — EDGE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-LVV-020 | FR-X.3-01 / N:N idempotent | Liên kết VV đã liên kết — không tạo trùng | HĐ "HDTV-link-01" đã link V001. | Liên kết lại V001 | 1. Form Sửa HĐ. 2. [+ Liên kết VV]. 3. Modal: V001 đã checked sẵn (hoặc disabled). | (1) UI prevent re-select V001 (disabled hoặc check sẵn). (2) Nếu submit lại: junction không có row trùng (UNIQUE constraint hoặc UPSERT idempotent). | Edge 🟡 |
| TC-LVV-021 | FR-X.3-01 / unlink audit | Bỏ liên kết VV — audit log riêng (SPEC-CLARIFY-HDTV-07) | HĐ link V001. | — | 1. Bỏ liên kết V001. 2. Xem Accordion Nhật ký. | **SPEC-CLARIFY-HDTV-07**: SRS không nói rõ unlink có audit entry riêng không. Kỳ vọng: timeline có entry "Bỏ liên kết VV V001 by cb_nv_tw_01 at NOW()". Flag BA. | Edge 🟢 |
| TC-LVV-022 | FR-X.3-01 / cascade after VV soft-delete (A4 merged) | VV bị soft-delete → liên kết HD_VV phải hide khỏi accordion HĐ | HĐ "HDTV-link-01" link V001. V001 bị soft-delete (is_deleted=1) ở module FR-05. | — | 1. Reload Form Sửa HĐ. 2. Xem accordion VV liên kết. | (1) Bảng VV không list V001 (BR-DATA-01 — soft delete VV không hiển thị). (2) Cột "Số VV" trên list HĐ = 0. (3) Cho phép Xóa HĐ (E4 không trigger). | Edge 🔴 |
| TC-LVV-023 | FR-X.3-01 / VV detail back-ref (A4 merged) | Detail VV (FR-05 SCR-V.I-03) accordion "HĐ tư vấn liên kết" hiển thị HĐ | HĐ "HDTV-link-01" link V001. | — | 1. Login cb_nv_tw_01. 2. Vào FR-05 chi tiết V001. 3. Mở accordion "HĐ tư vấn liên kết". | (1) Accordion list HDTV-link-01 với mã + tên + giá trị + trạng thái. (2) Click row drill-down mở Form Sửa HĐ. (Embedded drawer per business §⑩). | Edge 🟡 |
| TC-LVV-024 | FR-X.3-01 / TVV detail back-ref (A4 merged) | Detail TVV (FR-04 SCR-IV-03 tab Lịch sử) hiển thị HĐ link TVV | HĐ "HDTV-link-01" tvv_id=TVV001. | — | 1. Login cb_nv_tw_01. 2. Vào FR-04 chi tiết TVV001. 3. Tab "Lịch sử hỗ trợ" → mục HĐ. | (1) List HDTV-link-01 với mã + tên + giá trị + thời hạn. (2) Click drill-down. (Embedded drawer per business §⑩). | Edge 🟡 |
| TC-LVV-025 | FR-X.3-01 / N:N many HD per VV (A4 merged) | 1 VV link 5 HĐ — verify count đúng + scope đơn vị | V001 thuộc TW link với HDTV-A, B, C (TW) + HDTV-D, E (BN). | — | 1. cb_nv_tw_01 vào FR-05 detail V001 → accordion HĐ. 2. cb_nv_bn_01 vào cùng V001. | (1) cb_nv_tw_01 thấy 5 HĐ (A..E) nếu BR-AUTH-08 áp lên VV (V001 owner) hay 3 HĐ (chỉ TW)? **SPEC-CLARIFY**: scope đơn vị áp trên HĐ list trong accordion VV → cb_nv_tw_01 thấy 3 (TW only) hay 5 (theo VV owner)? Mark gap. | Edge 🟡 |

---

## Tổng kết file 04-TC

- **Tổng số TC: 11** (3 Happy + 2 Negative + 6 Edge — A4 +4)
- **Critical TC (🔴)**: TC-LVV-001, 003, 010, 011, 022
- **A4 merged 2026-05-10**: TC-LVV-022, 023, 024, 025

*Generated 2026-05-10 — Phase A step A3*
