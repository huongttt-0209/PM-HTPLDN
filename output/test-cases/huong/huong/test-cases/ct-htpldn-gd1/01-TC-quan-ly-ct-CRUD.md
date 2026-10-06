# Test Cases — FR-XI-01 (UC160): Quản lý CT HTPLDN — CRUD core

> **SRS Ref**: FR-XI-01, SCR-XI-01 (Trang Danh sách + Tab Thông tin), Entity CHUONG_TRINH_HTPL
> **Ngày tạo**: 2026-05-06
> **Đặc thù**: CRUD chỉ khi DU_THAO. Auto-gen mã `CT-{YYYYMMDD}-{SEQ}`. Trạng thái mặc định DU_THAO. Phân trang 20/page. Soft-delete.
> **Scope**: CRUD core — KHÔNG bao gồm sub-actions lifecycle (xem `03-TC-lifecycle-ct.md`)

---

## Quy ước

- **Priority**: 🔴 P0 (critical) · 🟡 P1 (high) · 🟢 P2 (medium)
- **TraceID**: `FR-XI-01 / {section}` — truy vết SRS
- **Pre-conditions mặc định**: User đã đăng nhập, có quyền "Quản lý CT HTPLDN" (UC115)

---

## Trường input FR-XI-01

| # | Field | Bắt buộc | Kiểu | Ràng buộc |
|---|-------|----------|------|-----------|
| 1 | ma_chuong_trinh | Y (auto) | text | `CT-{YYYYMMDD}-{SEQ}` — auto |
| 2 | ten_chuong_trinh | Y | text | — |
| 3 | muc_tieu | Y | text (long) | — |
| 4 | thoi_gian_bat_dau | Y | date | — |
| 5 | thoi_gian_ket_thuc | N | date | > thoi_gian_bat_dau (nếu có) |
| 6 | ngan_sach | N | money | >= 0 |
| 7 | doi_tuong | Y | text (long) | Đối tượng thụ hưởng |
| 8 | don_vi_id | Y (auto) | identifier | Auto từ user |
| 9 | ghi_chu | N | text (long) | — |

---

## A. CRUD CT — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-CT-CRUD-001 | FR-XI-01 / Processing Tạo step 1-7 | Tạo CT thành công — happy path | cb_nv_tw_01 login. | ten_chuong_trinh="CT HTPLDN 2026 Q1", muc_tieu="Tăng cường nhận thức PL DN", thoi_gian_bat_dau="2026-06-01", doi_tuong="DN nhỏ và vừa" | 1. Click [+ Thêm CT]. 2. Nhập đủ trường bắt buộc. 3. Lưu. | (1) POST `/api/v1/chuong-trinh-htpl` 200. (3) CT xuất hiện trong DS với ma_chuong_trinh auto `CT-{YYYYMMDD}-001`, trạng thái=DU_THAO, don_vi_id=user, ngày_tao=NOW(), nguoi_tao=cb_nv_tw_01. Audit log INSERT (BR-DATA-05). | Happy 🔴 |
| TC-CT-CRUD-002 | FR-XI-01 / Processing Cập nhật | Sửa CT khi DU_THAO | cb_nv_tw_01 login. CT-DT01 trạng thái DU_THAO. | ten="CT HTPLDN 2026 Q1 (Sửa)", ngan_sach=500000000 | 1. Click Sửa trên CT-DT01. 2. Đổi tên + thêm ngân sách. 3. Lưu. | (1) PUT 200. (3) Hiển thị tên mới + ngân sách. Audit log UPDATE. | Happy 🔴 |
| TC-CT-CRUD-003 | FR-XI-01 / Processing Xóa step 1-5 | Xóa mềm CT khi DU_THAO | cb_nv_tw_01 login. CT-DT02 trạng thái DU_THAO. | — | 1. Click Xóa trên CT-DT02. 2. Xác nhận. | (1) DELETE 200, soft delete (`is_deleted=1`, BR-DATA-01). (3) CT-DT02 biến mất khỏi DS. Audit log DELETE. | Happy 🔴 |
| TC-CT-CRUD-004 | FR-XI-01 / AC#1 + BR-DATA-07 | Hiển thị DS CT phân trang | cb_nv_tw_01 login. ≥25 CT thuộc đơn vị. | — | 1. Truy cập SCR-XI-01. | (3) DS phân trang 20/page. Cột: Mã CT / Tên / Mục tiêu (cắt 100 ký tự) / Thời gian / Ngân sách / Đơn vị / Trạng thái (badge) / Số đợt BC / Hành động. | Happy 🟡 |
| TC-CT-CRUD-005 | FR-XI-01 / AC#2 | Xem chi tiết CT (Tab Thông tin) | cb_nv_tw_01 login. CT-DT01 tồn tại. | — | 1. Click row CT-DT01. | (3) Mở Tab "Thông tin": form đầy đủ field + Thanh tiến trình SM-KH-CTHTPL highlight DU_THAO. | Happy 🟢 |
| TC-CT-CRUD-006 | FR-XI-01 / AC#1 + BR-AUTH-08 | DS CT scope theo đơn vị | cb_nv_dp_01 (Sở TP AG) login. CT-AG01 + CT-BG01 (Sở TP BG) tồn tại. | — | 1. Truy cập SCR-XI-01. | (3) Chỉ thấy CT-AG01 (cùng đơn vị); KHÔNG thấy CT-BG01. | Happy 🟡 |

---

## B. CRUD CT — NEGATIVE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-CT-CRUD-010 | FR-XI-01 / E1 ERR-XI-01-01 | Thiếu trường bắt buộc | cb_nv_tw_01 login. | ten="" | 1. Mở form Thêm CT. 2. Bỏ trống tên + Lưu. | (2) Error: **"Vui lòng nhập đầy đủ thông tin bắt buộc"** (ERR-XI-01-01). Form giữ. | Negative 🔴 |
| TC-CT-CRUD-011 | FR-XI-01 / E2 ERR-XI-01-02 + BR-FLOW-03 | Sửa CT khi ≠ DU_THAO | cb_nv_tw_01 login. CT-PD01 trạng thái CHO_PHE_DUYET. | — | 1. Click Sửa trên CT-PD01. | (1) Nút Sửa ẩn HOẶC backend reject với **"Chỉ chỉnh sửa CT ở trạng thái Dự thảo"** (ERR-XI-01-02). | Negative 🔴 |
| TC-CT-CRUD-012 | FR-XI-01 / E3 ERR-XI-01-03 + BR-FLOW-03 | Xóa CT khi ≠ DU_THAO | cb_nv_tw_01 login. CT-DD01 trạng thái DA_DUYET. | — | 1. Click Xóa trên CT-DD01. | (1) Nút Xóa ẩn HOẶC backend reject **"Chỉ xóa CT ở trạng thái Dự thảo"** (ERR-XI-01-03). | Negative 🔴 |
| TC-CT-CRUD-013 | FR-XI-01 / Inputs#5 | thoi_gian_ket_thuc <= thoi_gian_bat_dau | cb_nv_tw_01 login. | thoi_gian_bat_dau="2026-06-01", thoi_gian_ket_thuc="2026-05-31" | 1. Tạo CT với end < start + Lưu. | (2) Error inline trên field "Thời gian kết thúc phải sau Thời gian bắt đầu". KHÔNG persist. | Negative 🟡 |
| TC-CT-CRUD-014 | FR-XI-01 / Inputs#6 | ngan_sach < 0 | cb_nv_tw_01 login. | ngan_sach=-1000000 | 1. Nhập ngân sách âm + Lưu. | (2) Validation reject. KHÔNG persist. | Negative 🟢 |
| TC-CT-CRUD-015 | FR-XI-01 / Inputs#5 (A4 merged) | thoi_gian_bat_dau = thoi_gian_ket_thuc (boundary equal — strict `>`) | cb_nv_tw_01 login. | thoi_gian_bat_dau="2026-06-01", thoi_gian_ket_thuc="2026-06-01" | 1. Tạo CT với 2 ngày bằng nhau + Lưu. | (2) Backend reject vì spec quote "> thoi_gian_bat_dau". Toast/inline error. KHÔNG persist. | Negative 🟡 |

---

## C. CRUD CT — EDGE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-CT-CRUD-016 | FR-XI-01 / Inputs#6 (A4 merged) | ngan_sach = 0 (boundary inclusive `>=0`) | cb_nv_tw_01 login. | ngan_sach=0 | 1. Tạo CT với ngân sách=0 + Lưu. | (1) PASS — boundary `>=0` inclusive. CT lưu với ngân sách=0. UI hiển thị "0" hoặc "—" tùy spec format. | Edge 🟡 |
| TC-CT-CRUD-017 | FR-XI-01 / BR-EC-01 (A4 merged) | Concurrent UPDATE 2 tab cùng CT | cb_nv_tw_01 login. CT-DT10 DU_THAO mở 2 tab. | Tab1: ten="A"; Tab2: ten="B" | 1. Tab1 Sửa → đổi tên A → Lưu (delay backend). 2. Tab2 Sửa → đổi tên B → Lưu trước khi Tab1 response. | (2) 1 PUT thành công, 1 reject với optimistic-lock ERR-SYS-02 (BR-EC-01 — check `updated_at`). UI tab thua → toast error + reload latest. PERSIST: 1 record với tên thắng. Audit log có 1 UPDATE + 1 attempt fail. | Edge 🟡 |
| TC-CT-AUDIT-001 | FR-XI-01 / BR-DATA-05 (A6 merged) | Audit log E2E full-cycle Tạo→Sửa→Xóa | cb_nv_tw_01 login. | ten="CT Audit Test" | 1. Tạo CT mới (POST). 2. Sửa tên CT (PUT). 3. Xóa CT (DELETE). 4. Mở module Nhật ký HT (FR-10) lọc theo `entity=CHUONG_TRINH_HTPL` + `record_id`. | (3) 3 entries trong AUDIT_LOG: action_type=INSERT/UPDATE/DELETE, actor=cb_nv_tw_01, timestamp incrementing, before/after diff cho UPDATE (vd `ten_chuong_trinh: "X" → "Y"`). Log immutable (không thể edit). | Edge 🟢 |

---

## Tổng kết file 01-TC

- **15 TC**: 6 Happy + 6 Negative + 3 Edge (A3 base 11 + A4 merged 3 + A6 merged 1)
- **Critical TC (🔴)**: 001, 002, 003, 010, 011, 012
- **A4 merged 2026-05-06**: TC-CT-CRUD-015..017
- **A6 merged 2026-05-06**: TC-CT-AUDIT-001 (BR-DATA-05 dedicated)

*Generated 2026-05-06 — Phase A step A3 + A4 + A6 inline merge*
