# Test Cases — UC97: Import Biểu mẫu Hàng loạt (FR-VII-06)

> **SRS Ref**: FR-VII-06 (srs-fr-09:447-509), SCR-VII-03 (Wizard), Entity BIEU_MAU + FILE_DINH_KEM
> **Ngày tạo**: 2026-05-06 (BMAD A3)
> **Tài khoản chính**: `cb_nv_tw_01` (có quyền + thư mục đích tồn tại — srs-fr-09:455-457)

---

## A. UI / WIZARD VERIFY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-BM-UI-06 | FR-VII-06 / SCR-VII-03 | Verify wizard SCR-VII-03 | `cb_nv_tw_01`. Vào SCR-VII-02 → click [Nhập hàng loạt]. | — | 1. Quan sát wizard. | **WIZARD**: 6 component (srs-fr-09:660-667): (1) Thư mục đích select bắt buộc; (2) Tải file Excel metadata `.xlsx` (max 5MB) + nút [Tải mẫu Excel]; (3) Multi-file upload kéo-thả (max 50 file, max 20MB/file); (4) Bảng kiểm tra (STT/Tên file/Định dạng/Kích thước/Trạng thái Hợp lệ-Lỗi) — hiện sau upload; (5) Thống kê "Tổng: {N} file. Hợp lệ: {X}. Lỗi: {Y}"; (6) Nút [Xác nhận nhập {X} file hợp lệ] — disable nếu X=0. | Happy | P2 |

---

## B. HAPPY PATH

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-BM-601 | FR-VII-06 AC1 | Import 5 file hợp lệ vào thư mục đích | `cb_nv_tw_01`. Thư mục "HĐ LĐ" tồn tại. 5 file `.docx` hợp lệ (≤20MB). | thu_muc=HĐ_LĐ.id, files=5 docx | 1. Mở wizard. 2. Chọn thư mục. 3. Upload 5 file. 4. Quan sát bảng kiểm tra (5 rows Hợp lệ). 5. Click [Xác nhận nhập 5 file hợp lệ]. | **STATE**: Backend (1) validate từng file format + size (BR-BM-03); (2) virus scan (BR-EC-03); (3) INSERT 5 BIEU_MAU + 5 FILE_DINH_KEM (BR-DATA-03). **UI**: Toast/dialog success "Import thành công 5 file. 0 file lỗi" (suy ra từ srs-fr-09:474, 502 AC). Wizard close. Bảng SCR-VII-02 reload, 5 BM mới xuất hiện trong thư mục HĐ_LĐ. **PERSIST**: AUDIT_LOG hành động='BULK_IMPORT', count=5 (srs-fr-09:475). | Happy | P0 |

---

## C. NEGATIVE — VALIDATION & BOUNDARY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-BM-602 | ERR-IMP-01 | Tất cả file lỗi (.exe, .pdf) | `cb_nv_tw_01`. | files=[a.exe, b.pdf] | 1. Upload 2 file. 2. Bảng kiểm tra: 2 rows "Lỗi". 3. Nút [Xác nhận] disable. | **STATE**: Client validate ngay khi upload (format không thuộc {doc,docx,xls,xlsx}). **UI**: Bảng kiểm tra cột Trạng thái=Lỗi, lý do "Định dạng không hỗ trợ". Thống kê: Tổng=2, Hợp lệ=0, Lỗi=2. Toast/inline error nguyên văn "Không có file nào hợp lệ để import" (srs-fr-09:481 ERR-IMP-01). [Xác nhận] disable. **PERSIST**: KHÔNG có BIEU_MAU mới. | Negative | P0 |
| TC-BM-603 | WRN-IMP-01 | Một số file lỗi — partial import | `cb_nv_tw_01`. | files=[ok1.docx, ok2.docx, bad.exe, big.docx 25MB] | 1. Upload 4 file. 2. Bảng: 2 Hợp lệ + 2 Lỗi. 3. [Xác nhận nhập 2 file hợp lệ]. | **STATE**: Backend INSERT 2 BM cho file hợp lệ; ghi báo cáo lỗi cho 2 file fail (srs-fr-09:472-474). **UI**: Toast warning nguyên văn "Import thành công 2 file. 2 file lỗi: xem chi tiết" (srs-fr-09:482 WRN-IMP-01). Modal/drawer "Chi tiết lỗi" hiển thị: bad.exe (định dạng không hỗ trợ) + big.docx (vượt 20MB). **PERSIST**: 2 BM mới + AUDIT_LOG hành động='BULK_IMPORT' count=2. | Negative | P0 |
| TC-BM-604 | ERR-IMP-02 / BR-BM-07 | Vượt 50 file | `cb_nv_tw_01`. 51 file `.docx` valid mỗi file 1MB. | files=51 | 1. Upload 51 file (kéo thả batch). | **STATE**: Client/Backend reject (srs-fr-09:483 BR-BM-07). **UI**: Toast error nguyên văn "Tối đa 50 file mỗi lần import" (srs-fr-09:483 ERR-IMP-02). KHÔNG hiển thị bảng kiểm tra (hoặc cắt 50 đầu — verify behavior **SPEC-CLARIFY-BM-08**). **PERSIST**: KHÔNG có BM mới. | Negative | P1 |
| TC-BM-605 | ERR-IMP-03 / BR-BM-07 | Tổng > 500MB | `cb_nv_tw_01`. 30 file × 18MB = 540MB. | files=30 (tổng 540MB) | 1. Upload 30 file. | **STATE**: Backend reject (srs-fr-09:484 BR-BM-07). **UI**: Toast error nguyên văn "Tổng dung lượng tối đa 500MB" (srs-fr-09:484 ERR-IMP-03). **PERSIST**: KHÔNG có BM mới. | Negative | P0 |
| TC-BM-608 | FR-VII-06 / metadata mismatch (A4 merged) | Excel metadata file mismatch số file content | `cb_nv_tw_01`. Excel metadata 5 row (5 BM) + multi-file content 7 file. | metadata=5 row, content=7 file | 1. Upload Excel metadata 5 row. 2. Upload 7 file content. 3. Quan sát bảng kiểm tra. | **STATE**: BE behavior **SRS Gap** (srs-fr-09:663 yêu cầu metadata + content nhưng không quote rule mismatch). 2 case: (a) Reject toàn bộ với error "Số metadata không khớp số file" (mark gap-report); (b) Import theo intersect metadata × content (5 thành công, 2 dư bỏ qua). **UI**: Bảng kiểm tra hiển thị mismatch warning. **PERSIST**: Mark **SPEC-CLARIFY-BM-14** behavior chuẩn. | Negative | P1 |
| TC-BM-609 | FR-VII-06 / SPEC-CLARIFY-BM-12 (A4 merged) | Duplicate file names trong cùng batch | `cb_nv_tw_01`. | files=[`a.docx` (1MB), `a.docx` (2MB, khác content)] (2 file cùng tên) | 1. Upload 2 file cùng tên. 2. Quan sát bảng kiểm tra. | **STATE**: BE behavior **SRS Gap**. 2 case: (a) Reject duplicate với error "Tên file trùng trong batch"; (b) Auto rename `a.docx`, `a-1.docx`. **UI**: Bảng hiển thị trạng thái phù hợp. **PERSIST**: Mark **SPEC-CLARIFY-BM-12**. | Negative | P1 |
| TC-BM-610 | FR-VII-06 / metadata size boundary (A4 merged) | Excel metadata file > 5MB (boundary srs-fr-09:663) | `cb_nv_tw_01`. | metadata=`big.xlsx` (6MB) | 1. Upload Excel metadata 6MB. | **STATE**: BE reject (srs-fr-09:663 nguyên văn "max 5MB"). **UI**: Toast error/inline "File metadata vượt 5MB" (SRS Gap message). **PERSIST**: KHÔNG import. Boundary: 5MB phải PASS. | Negative | P2 |

---

## D. EDGE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-BM-606 | EC-01 / BR-EC-04 | Storage quota 100% — đơn vị đầy 10GB | `cb_nv_tw_01`. Đơn vị TW đã dùng 10GB storage (set = 10GB qua dữ liệu seed). | files=5 docx (50MB) | 1. Upload 5 file. 2. [Xác nhận]. | **STATE**: Backend reject (BR-EC-04 storage quota 10GB/đơn vị, 100% từ chối). **UI**: Toast error nguyên văn `ERR-FILE-01` (SRS Gap message hoàn chỉnh trong srs-fr-09 → mark **SPEC-CLARIFY-BM-09**). **PERSIST**: KHÔNG có BM mới. AUDIT_LOG ghi attempt fail. | Edge | P1 |
| TC-BM-607 | BR-EC-03 | File chứa virus mixed với valid | `cb_nv_tw_01`. | files=[ok1.docx, virus.docx (EICAR), ok2.docx] | 1. Upload 3 file. 2. [Xác nhận nhập file hợp lệ]. | **STATE**: ClamAV detect file 2 → mark Lỗi. **UI**: Bảng kiểm tra: ok1+ok2 Hợp lệ, virus.docx Lỗi (lý do "Phát hiện mã độc" — message **SRS Gap** → SPEC-CLARIFY-BM-04). Click [Xác nhận nhập 2 file hợp lệ] → success import 2. **PERSIST**: 2 BM mới. virus.docx KHÔNG lưu vào storage. | Edge | P0 |

---

## Tổng số TC: 11 (1 UI + 1 Happy + 7 Negative + 2 Edge) — A3 base 8 + A4 merged 3
**Priority**: P0=4 / P1=5 / P2=2

**Coverage:**
- BR (formal SRS §6): BR-AUTH-01, BR-DATA-03/05
- BR-DATA-01 (Soft delete) — SRS srs-fr-09:863 áp dụng FR-VII-06 nhưng module Import KHÔNG có path xóa; soft-delete được verify trong file 04 TC-BM-406 (CRUD BM). Note: import lỗi không tạo BIEU_MAU record (verify TC-BM-602/603 PERSIST=KHÔNG record), nên không vi phạm BR-DATA-01.
- BR (working labels srs-v3.md inline / inline rule labels — see 00-test-plan §2.1 footnote): BR-BM-07 (50 file/500MB), BR-BM-03 (gián tiếp), BR-EC-03 (virus), BR-EC-04 (storage quota)
- Error codes: ERR-IMP-01/02/03, WRN-IMP-01
- AC SRS: 3/3 (srs-fr-09:499-502)
- Edge case SRS: EC-01 import (srs-fr-09:507-508)
- A4 merged 2026-05-06: TC-BM-608 (metadata mismatch), TC-BM-609 (duplicate filename), TC-BM-610 (metadata >5MB boundary)
- Codex review 2026-05-09: BM-HIGH-002 finding partial-valid → giải đáp bằng note BR-DATA-01 trên (không thêm TC vì module không có delete path).
- SPEC-CLARIFY: BM-04 (virus message), BM-08 (>50 file UI behavior), BM-09 (ERR-FILE-01 message), BM-12 (duplicate filename rule), BM-14 (metadata mismatch behavior)
