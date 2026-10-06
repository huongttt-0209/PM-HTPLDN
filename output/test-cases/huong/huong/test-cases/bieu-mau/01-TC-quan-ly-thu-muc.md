# Test Cases — FR-VII-01 (UC92): Quản lý Thư mục Biểu mẫu

> **SRS Ref**: FR-VII-01, SCR-VII-01, Entity THU_MUC_BIEU_MAU
> **Ngày tạo**: 2026-05-06
> **Đặc thù**: CRUD thư mục 1 cấp flat. Tên unique per đơn vị. Xóa chỉ khi rỗng (không chứa BM). Xuất Excel.

---

## Quy ước

- **Priority**: 🔴 P0 (critical) · 🟡 P1 (high) · 🟢 P2 (medium)
- **TraceID**: `FR-VII-01 / {section}` — truy vết SRS
- **Pre-conditions mặc định**: User đã đăng nhập, có quyền "Thư viện biểu mẫu" (UC115)

---

## Trường input FR-VII-01

| # | Field | Bắt buộc | Kiểu | Ràng buộc |
|---|-------|----------|------|-----------|
| 1 | ten_thu_muc | Y | text | Max 500 ký tự, unique per don_vi_id |
| 2 | linh_vuc_id | Y | identifier | FK → DANH_MUC (Lĩnh vực PL từ UC99) |
| 3 | mo_ta | N | text | Max 2000 ký tự (SCR-VII-01 row#17) |
| 4 | trang_thai | Y | text | NHAP / CONG_KHAI (default NHAP) |
| 5 | thu_tu_hien_thi | N | number | 1-20 |

---

## A. CRUD THƯ MỤC — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-TM-001 | FR-VII-01 / Processing Tạo step 2-7 | Tạo thư mục thành công — happy path | cb_nv_tw_01 login. Lĩnh vực PL "Dân sự" tồn tại. | ten_thu_muc="Biểu mẫu HĐ Lao động", linh_vuc_id=Dân sự | 1. Click [+ Thêm thư mục]. 2. Nhập tên + chọn lĩnh vực + Lưu. | (1) POST thành công. (3) Thư mục xuất hiện trong danh sách, trạng thái=NHAP, Số BM=0, ngày_tao=NOW(), nguoi_tao=cb_nv_tw_01. | Happy 🔴 |
| TC-TM-002 | FR-VII-01 / Processing Cập nhật | Sửa thư mục thành công | cb_nv_tw_01 login. TM tồn tại (NHAP). | ten_thu_muc="BM HĐ LĐ (Sửa)", mo_ta="Cập nhật mô tả" | 1. Click Sửa trên TM. 2. Đổi tên + thêm mô tả + Lưu. | (1) PUT thành công. (3) Danh sách hiển thị tên mới. Audit log ghi nhận (BR-DATA-05). | Happy 🔴 |
| TC-TM-003 | FR-VII-01 / Processing Xóa step 1-4 | Xóa thư mục rỗng thành công | cb_nv_tw_01 login. TM "TM Trống" tồn tại, 0 BM, trạng thái NHAP. | — | 1. Click Xóa trên TM. 2. Xác nhận dialog. | (1) Soft delete (is_deleted=1, BR-DATA-01). (3) TM biến mất khỏi danh sách. Audit log ghi nhận. | Happy 🔴 |
| TC-TM-004 | FR-VII-01 / AC#1 | Hiển thị danh sách thư mục — phân trang | cb_nv_tw_01 login. ≥25 TM thuộc đơn vị TW. | — | 1. Truy cập "Thư viện biểu mẫu". | (3) Danh sách TM phân trang 20/page (BR-DATA-07). Cột: tên, lĩnh vực, số BM, trạng thái badge, ngày tạo, người tạo. | Happy 🟡 |
| TC-TM-005 | FR-VII-01 / AC#6 | Xuất Excel danh sách thư mục | cb_nv_tw_01 login. ≥5 TM. | — | 1. Click [Xuất Excel]. | (3) File .xlsx tải về chứa danh sách TM (scope đơn vị). | Happy 🟡 |

---

## B. CRUD THƯ MỤC — NEGATIVE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-TM-010 | FR-VII-01 / E1 ERR-TM-01 | Tạo TM trùng tên trong đơn vị | cb_nv_tw_01 login. TM "HĐ LĐ" đã tồn tại. | ten_thu_muc="HĐ LĐ" | 1. Thêm TM trùng tên + Lưu. | (2) Error: **"Thư mục 'HĐ LĐ' đã tồn tại trong đơn vị"** (ERR-TM-01). Form giữ. | Negative 🔴 |
| TC-TM-011 | FR-VII-01 / E2 ERR-TM-02 | Xóa TM chứa biểu mẫu | cb_nv_tw_01 login. TM chứa 3 BM. | — | 1. Click Xóa. 2. Xác nhận. | (2) Error: **"Thư mục chứa 3 biểu mẫu, không thể xóa"** (ERR-TM-02). | Negative 🔴 |
| TC-TM-012 | FR-VII-01 / E3 ERR-TM-03 | Tên TM vượt 500 ký tự | cb_nv_tw_01 login. | ten_thu_muc=501 chars | 1. Nhập tên 501 ký tự + Lưu. | (2) Error: **"Tên thư mục tối đa 500 ký tự"** (ERR-TM-03). | Negative 🟡 |
| TC-TM-013 | FR-VII-01 / E4 ERR-TM-04 | Lĩnh vực PL không tồn tại | cb_nv_tw_01 login. | linh_vuc_id=INVALID | 1. Tạo TM + lĩnh vực invalid + Lưu. | (2) Error: **"Lĩnh vực PL không tồn tại"** (ERR-TM-04). | Negative 🟡 |

---

## C. CRUD THƯ MỤC — EDGE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-TM-020 | FR-VII-01 / Inputs#1 | Tên TM boundary 500 ký tự (exact) | cb_nv_tw_01 login. | ten_thu_muc=500 chars | 1. Nhập 500 ký tự + Lưu. | (1) Tạo thành công (boundary inclusive). | Edge 🟡 |
| TC-TM-021 | FR-VII-01 / Inputs#1 | Tên TM trùng nhưng KHÁC đơn vị — OK | cb_nv_tw_01 đã tạo "HĐ XYZ". cb_nv_bn_01 login. | ten_thu_muc="HĐ XYZ" | 1. cb_nv_bn_01 tạo TM cùng tên. | (1) Tạo OK (unique per don_vi_id). | Edge 🟡 |
| TC-TM-022 | FR-VII-01 / AC#7 | Click "Làm mới" reload | cb_nv_tw_01 login. | — | 1. Click [Làm mới]. | (3) Danh sách reload mới nhất. | Edge 🟢 |
| TC-TM-023 | FR-VII-01 / Inputs#1 / SPEC-CLARIFY-BM-11 | Tên TM trailing/leading whitespace `"  HĐ LĐ  "` (A4 merged) | cb_nv_tw_01 login. TM "HĐ LĐ" đã tồn tại (no whitespace). | ten_thu_muc=`"  HĐ LĐ  "` (2 space đầu + 2 cuối) | 1. Tạo TM với tên có whitespace + Lưu. | (3) BE behavior **SRS Gap**: (a) trim → trùng "HĐ LĐ" → ERR-TM-01 nhầm; (b) không trim → tạo OK với tên có space; (c) reject với validation message. Mark **SPEC-CLARIFY-BM-11** cho rule trim. | Edge 🟡 |
| TC-TM-024 | FR-VII-01 / Inputs#3 / SCR-VII-01 row#17 | Mô tả TM boundary 2000 ký tự (max textarea, A4 merged) | cb_nv_tw_01 login. | mo_ta=2001 chars | 1. Tạo TM hợp lệ + paste mô tả 2001 ký + Lưu. | (2) Hoặc client validate `<textarea maxlength=2000>` truncate ở 2000 ký; hoặc submit → BE reject với toast "Mô tả tối đa 2000 ký tự" (SRS Gap message — mark trong gap-report). **PERSIST**: KHÔNG có record nếu reject; record với mô tả 2000 ký nếu truncate. | Edge 🟡 |
| TC-TM-025 | FR-VII-01 / Inputs#5 | thu_tu_hien_thi out of range (0 hoặc 21, A4 merged) | cb_nv_tw_01 login. | thu_tu_hien_thi=0 (test 1), thu_tu_hien_thi=21 (test 2) | 1. Tạo TM với thu_tu=0 + Lưu. 2. Repeat với thu_tu=21. | (2) BE reject (srs-fr-09:91 quote "1-20"). **UI**: Toast error/inline "Thứ tự hiển thị từ 1-20" (SRS Gap message — mark gap-report). **PERSIST**: KHÔNG có record. Boundary: thu_tu=1 + thu_tu=20 phải PASS. | Edge 🟢 |
| TC-TM-026 | FR-VII-01 / BR-BM-01 + concurrency | Concurrent CREATE 2 tab cùng tên → race condition (A4 merged) | cb_nv_tw_01 login. Mở 2 tab cùng SCR-VII-01. | Tab1 + Tab2: cùng ten_thu_muc="Race Test" | 1. Tab1 fill form + click Lưu (delay backend). 2. Tab2 fill form cùng tên + click Lưu trước khi Tab1 response. | **STATE**: Backend race — 1 INSERT thành công (UNIQUE constraint per don_vi_id), 1 reject. **UI**: Tab thắng → toast success; tab thua → toast error nguyên văn "Thư mục 'Race Test' đã tồn tại trong đơn vị" (ERR-TM-01). **PERSIST**: Chỉ 1 record THU_MUC_BIEU_MAU với ten="Race Test". Audit log có 1 INSERT + 1 attempt fail. | Edge 🟡 |
| TC-TM-027 | FR-VII-01 / AC#2 (srs-fr-09:141) | Xem chi tiết thư mục — expand thấy danh sách BM bên trong (Codex review 2026-05-09 added) | cb_nv_tw_01 login. TM "HĐ LĐ" có 25 BM thuộc TW. | — | 1. SCR-VII-01. 2. Click icon mở rộng (SCR-VII-01 row#9) trên dòng "HĐ LĐ" hoặc click tên TM. | **STATE**: Backend GET `/thu-muc/{id}` trả info TM + GET `/bieu-mau?thu_muc_id={id}` trả danh sách BM scope đơn vị (BR-AUTH-08, srs-fr-09:141, 883). **UI**: Expand panel hiển thị: thông tin TM (tên, lĩnh vực, mô tả, trạng thái, ngày tạo, người tạo) + bảng BM bên trong với pagination 20/page (BR-DATA-07). Cột BM: Mã, Tên, Định dạng, Kích thước, Trạng thái lifecycle, Đã công khai. **PERSIST**: URL/query state giữ TM expanded khi reload (qua URL fragment hoặc state). | Happy 🟡 |

---

## Tổng kết file 01-TC

- **17 TC**: 5 Happy + 4 Negative + 7 Edge + 1 (Codex 2026-05-09)
- **Critical TC (🔴)**: 001, 002, 003, 010, 011
- **A4 merged 2026-05-06**: TC-TM-023..026 (was TC-BM-111..114 in file 08 proposal). SPEC-CLARIFY-BM-11 (whitespace trim).
- **Codex review 2026-05-09**: TC-TM-027 (fill AC#2 detail view srs-fr-09:141 — Codex BM-CRIT-002).

*Generated 2026-05-06 — Phase A step A3 + A4 inline merge · updated 2026-05-09 sau Codex review*
