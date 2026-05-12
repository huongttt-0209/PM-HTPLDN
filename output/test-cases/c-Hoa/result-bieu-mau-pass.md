# Test Cases PASS — bieu-mau
> **Nguồn**: result-bieu-mau-all.md
> **Ngày tổng hợp**: 2026-05-11
> **Phạm vi**: chỉ Result ∈ {PASS, PASS-DEVIATE, PASS-RESOLVED}

## Summary

| File test-case | PASS | PASS-DEVIATE | PASS-RESOLVED | Tổng PASS |
|----------------|-----:|-------------:|--------------:|----------:|
| 01-TC-quan-ly-thu-muc           | 12 | 0 | 0 | 12 |
| 02-TC-tim-kiem-thu-muc          | 11 | 0 | 0 | 11 |
| 03-TC-cong-khai-thu-muc         |  4 | 0 | 0 |  4 |
| 04-TC-quan-ly-bieu-mau          | 10 | 0 | 0 | 10 |
| 05-TC-tim-kiem-bieu-mau         |  9 | 0 | 0 |  9 |
| 06-TC-import-hang-loat          |  5 | 0 | 0 |  5 |
| 07-TC-permission-matrix         |  4 | 0 | 0 |  4 |
| **Tổng**                        | **55** | **0** | **0** | **55** |

> Ghi chú: file nguồn không có TC nào ở status `PASS-DEVIATE` hoặc `PASS-RESOLVED` — chỉ có `PASS` literal. Section 04 trong summary file gốc ghi 12 PASS nhưng đếm literal `PASS` trên bảng chỉ ra 10 (đã verify lại 25 row); 2 row chênh có khả năng gốc đã include PARTIAL/BUG.

---

## 01-TC-quan-ly-thu-muc

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\bieu-mau\01-TC-quan-ly-thu-muc.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\bieu-mau\report-01-quan-ly-thu-muc\Tcs-report\TC-EXECUTION-2026-05-10.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-TM-001 | FR-VII-01 / Processing Tạo step 2-7 | Tạo thư mục thành công — happy path | cb_nv_tw_01 login. Lĩnh vực PL "Dân sự" tồn tại. | ten_thu_muc="Biểu mẫu HĐ Lao động", linh_vuc_id=Dân sự | 1. Click [+ Thêm thư mục]. 2. Nhập tên + chọn lĩnh vực + Lưu. | (1) POST thành công. (3) Thư mục xuất hiện trong danh sách, trạng thái=NHAP, Số BM=0, ngày_tao=NOW(), nguoi_tao=cb_nv_tw_01. | Happy 🔴 | PASS |  |
| TC-TM-002 | FR-VII-01 / Processing Cập nhật | Sửa thư mục thành công | cb_nv_tw_01 login. TM tồn tại (NHAP). | ten_thu_muc="BM HĐ LĐ (Sửa)", mo_ta="Cập nhật mô tả" | 1. Click Sửa trên TM. 2. Đổi tên + thêm mô tả + Lưu. | (1) PUT thành công. (3) Danh sách hiển thị tên mới. Audit log ghi nhận (BR-DATA-05). | Happy 🔴 | PASS |  |
| TC-TM-003 | FR-VII-01 / Processing Xóa step 1-4 | Xóa thư mục rỗng thành công | cb_nv_tw_01 login. TM "TM Trống" tồn tại, 0 BM, trạng thái NHAP. | — | 1. Click Xóa trên TM. 2. Xác nhận dialog. | (1) Soft delete (is_deleted=1, BR-DATA-01). (3) TM biến mất khỏi danh sách. Audit log ghi nhận. | Happy 🔴 | PASS |  |
| TC-TM-004 | FR-VII-01 / AC#1 | Hiển thị danh sách thư mục — phân trang | cb_nv_tw_01 login. ≥25 TM thuộc đơn vị TW. | — | 1. Truy cập "Thư viện biểu mẫu". | (3) Danh sách TM phân trang 20/page (BR-DATA-07). Cột: tên, lĩnh vực, số BM, trạng thái badge, ngày tạo, người tạo. | Happy 🟡 | PASS |  |
| TC-TM-005 | FR-VII-01 / AC#6 | Xuất Excel danh sách thư mục | cb_nv_tw_01 login. ≥5 TM. | — | 1. Click [Xuất Excel]. | (3) File .xlsx tải về chứa danh sách TM (scope đơn vị). | Happy 🟡 | PASS |  |
| TC-TM-010 | FR-VII-01 / E1 ERR-TM-01 | Tạo TM trùng tên trong đơn vị | cb_nv_tw_01 login. TM "HĐ LĐ" đã tồn tại. | ten_thu_muc="HĐ LĐ" | 1. Thêm TM trùng tên + Lưu. | (2) Error: "Thư mục 'HĐ LĐ' đã tồn tại trong đơn vị" (ERR-TM-01). Form giữ. | Negative 🔴 | PASS |  |
| TC-TM-011 | FR-VII-01 / E2 ERR-TM-02 | Xóa TM chứa biểu mẫu | cb_nv_tw_01 login. TM chứa 3 BM. | — | 1. Click Xóa. 2. Xác nhận. | (2) Error: "Thư mục chứa 3 biểu mẫu, không thể xóa" (ERR-TM-02). | Negative 🔴 | PASS |  |
| TC-TM-013 | FR-VII-01 / E4 ERR-TM-04 | Lĩnh vực PL không tồn tại | cb_nv_tw_01 login. | linh_vuc_id=INVALID | 1. Tạo TM + lĩnh vực invalid + Lưu. | (2) Error: "Lĩnh vực PL không tồn tại" (ERR-TM-04). | Negative 🟡 | PASS |  |
| TC-TM-020 | FR-VII-01 / Inputs#1 | Tên TM boundary 500 ký tự (exact) | cb_nv_tw_01 login. | ten_thu_muc=500 chars | 1. Nhập 500 ký tự + Lưu. | (1) Tạo thành công (boundary inclusive). | Edge 🟡 | PASS |  |
| TC-TM-022 | FR-VII-01 / AC#7 | Click "Làm mới" reload | cb_nv_tw_01 login. | — | 1. Click [Làm mới]. | (3) Danh sách reload mới nhất. | Edge 🟢 | PASS |  |
| TC-TM-025 | FR-VII-01 / Inputs#5 | thu_tu_hien_thi out of range (0 hoặc 21, A4 merged) | cb_nv_tw_01 login. | thu_tu_hien_thi=0 (test 1), thu_tu_hien_thi=21 (test 2) | 1. Tạo TM với thu_tu=0 + Lưu. 2. Repeat với thu_tu=21. | (2) BE reject (srs-fr-09:91 quote "1-20"). UI: Toast error/inline "Thứ tự hiển thị từ 1-20" (SRS Gap message — mark gap-report). PERSIST: KHÔNG có record. Boundary: thu_tu=1 + thu_tu=20 phải PASS. | Edge 🟢 | PASS |  |
| TC-TM-026 | FR-VII-01 / BR-BM-01 + concurrency | Concurrent CREATE 2 tab cùng tên → race condition (A4 merged) | cb_nv_tw_01 login. Mở 2 tab cùng SCR-VII-01. | Tab1 + Tab2: cùng ten_thu_muc="Race Test" | 1. Tab1 fill form + click Lưu (delay backend). 2. Tab2 fill form cùng tên + click Lưu trước khi Tab1 response. | STATE: Backend race — 1 INSERT thành công (UNIQUE constraint per don_vi_id), 1 reject. UI: Tab thắng → toast success; tab thua → toast error nguyên văn "Thư mục 'Race Test' đã tồn tại trong đơn vị" (ERR-TM-01). PERSIST: Chỉ 1 record THU_MUC_BIEU_MAU với ten="Race Test". Audit log có 1 INSERT + 1 attempt fail. | Edge 🟡 | PASS |  |

---

## 02-TC-tim-kiem-thu-muc

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\bieu-mau\02-TC-tim-kiem-thu-muc.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\bieu-mau\report-02-tim-kiem-thu-muc\Tcs-report\TC-EXECUTION-2026-05-10.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-BM-201 | FR-VII-02 AC1 | Tìm theo keyword khớp tên thư mục | `cb_nv_tw_01` đăng nhập. Đã có thư mục "Hợp đồng lao động" + "Hợp đồng dịch vụ" + "Mẫu đơn xin việc" thuộc TW. | keyword="Hợp đồng" | 1. Vào SCR-VII-01. 2. Nhập "Hợp đồng" vào ô từ khóa. 3. Click [Tìm kiếm] (hoặc Enter). | STATE: Backend WHERE ten_thu_muc LIKE '%Hợp đồng%' OR mo_ta LIKE '%Hợp đồng%' AND is_deleted=0 AND don_vi_id=TW.id. UI: Bảng hiển thị 2 thư mục match. | Happy | PASS |  |
| TC-BM-202 | FR-VII-02 AC2 | Filter date range + lĩnh vực kết hợp | `cb_nv_tw_01`. 4 thư mục: 2026-01-15 (DAN_SU), 2026-03-20 (HINH_SU), 2026-04-25 (DAN_SU), 2026-05-01 (LAO_DONG). | tu_ngay=2026-02-01, den_ngay=2026-04-30, linh_vuc=DAN_SU | 1. Filter từ ngày + đến ngày + lĩnh vực=DAN_SU. 2. [Tìm kiếm]. | STATE: Backend WHERE created_at BETWEEN dates AND linh_vuc_id=DAN_SU (AND logic). UI: Bảng hiển thị 1 record. | Happy | PASS |  |
| TC-BM-203 | FR-VII-02 AC3 | Filter trạng thái = CONG_KHAI | `cb_nv_tw_01`. 5 thư mục: 2 NHAP + 2 CONG_KHAI + 1 AN. | trang_thai=CONG_KHAI | 1. Filter trạng thái = "Đã công khai". 2. [Tìm kiếm]. | STATE: Backend WHERE trang_thai='CONG_KHAI'. UI: Bảng 2 record CONG_KHAI. Tab badge số = 2. | Happy | PASS |  |
| TC-BM-204 | ERR-TK-01 | Date range invalid: tu_ngay > den_ngay | `cb_nv_tw_01`. | tu_ngay=2026-05-01, den_ngay=2026-04-01 | 1. Filter date range invalid. 2. [Tìm kiếm]. | STATE: Backend reject hoặc client validate. UI: Toast error nguyên văn "Ngày bắt đầu phải trước ngày kết thúc" (ERR-TK-01). | Negative | PASS |  |
| TC-BM-205 | INF-TM-TK-01 | Search 0 result | `cb_nv_tw_01`. | keyword="ZZZZ-NOT-EXIST-9999" | 1. Search keyword không match. | STATE: Backend trả 0 row. UI: Empty state nguyên văn "Không tìm thấy thư mục phù hợp" (INF-TM-TK-01). Bảng trống. | Negative | PASS |  |
| TC-BM-206 | BR-EC-13 | Search SQL injection — sanitize | `cb_nv_tw_01`. | keyword=`'; DROP TABLE THU_MUC_BIEU_MAU; --` | 1. Paste payload. 2. [Tìm kiếm]. | STATE: Backend escape/parameterize query. KHÔNG drop table. UI: Empty state hoặc match literal. PERSIST: Verify table còn data. | Negative | PASS |  |
| TC-BM-207 | BR-EC-13 | Search XSS — sanitize | `cb_nv_tw_01`. | keyword=`<script>alert('XSS')</script>` | 1. Paste XSS payload. 2. [Tìm kiếm]. | STATE: Backend lưu plain string. UI: Trình duyệt KHÔNG execute script. Hiển thị payload escaped. | Negative | PASS |  |
| TC-BM-208 | FR-VII-02 / Vietnamese Unicode (A4 merged) | Search keyword tiếng Việt có dấu — Unicode collation | `cb_nv_tw_01`. TM "Lê Văn Cường" tồn tại. | keyword="Lê Văn" | 1. Search. | STATE: Backend handle Vietnamese Unicode collation. UI: Bảng match "Lê Văn Cường". | Edge | PASS |  |
| TC-BM-209 | BR-EC-13 / SQL LIKE wildcard escape (A4 merged) | Search keyword `100%` và `user_name` — escape `%` `_` | `cb_nv_tw_01`. TM "Báo cáo 100%" + TM "user_name_test" tồn tại. | keyword="100%" rồi "user_name" | 1. Search 2 keyword (2 lần). | STATE: Backend escape `%` và `_` trước khi build LIKE. UI: Bảng hiển thị chỉ TM match LITERAL. | Edge | PASS |  |
| TC-BM-210 | BR-EC-13 / boundary 200 ký tự (A4 merged) | Search keyword exactly 200 ký tự (BR-EC-13 boundary) | `cb_nv_tw_01`. | keyword="A"×200 | 1. Paste 200 ký tự. 2. [Tìm kiếm]. | STATE: BE accept (BR-EC-13 max 200 ký tự). UI: Hiển thị empty/match. PERSIST: Test thêm boundary 201 → expect reject hoặc truncate. | Edge | PASS |  |
| TC-BM-211 | FR-VII-02 / BR-DATA-07 (Codex 2026-05-09) | Search TM pagination boundary — default 20/page, max 100, page=2 navigation | `cb_nv_tw_01` login. ≥125 TM thuộc TW (seed). | page_size không set (default), keyword=`""` empty | 1. Vào SCR-VII-01 search (no keyword). 2. Verify page 1 = 20 rows. 3. Click page 2 → verify 20 rows. 4. Đổi page_size=100 → verify 100 rows. 5. URL `?page_size=101` direct. | STATE: Backend LIMIT 20 OFFSET 0 mặc định. page_size=100 accepted. page_size=101 reject hoặc clamp về 100 (mark SPEC-CLARIFY-BM-18 nếu silent clamp). | Edge | PASS |  |

---

## 03-TC-cong-khai-thu-muc

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\bieu-mau\03-TC-cong-khai-thu-muc.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\bieu-mau\report-03-cong-khai-thu-muc\Tcs-report\TC-EXECUTION-2026-05-10.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-BM-301 | FR-VII-03 AC1 / BR-FLOW-07 | Công khai thư mục có ≥1 biểu mẫu | `cb_nv_tw_01`. Thư mục "HĐ Lao động" trạng thái NHAP, chứa 3 BM. | hanh_dong=CONG_KHAI | 1. Hover dòng thư mục → click [Công khai]. 2. Confirm dialog. 3. Click [Xác nhận]. | STATE: Backend UPDATE trang_thai=CONG_KHAI, gọi API outbound push lên Cổng PLQG (BR-FLOW-05). KHÔNG có bước phê duyệt CB_PD (BR-FLOW-07). | Happy | PASS |  |
| TC-BM-302 | FR-VII-03 AC2 | Hủy công khai (Ẩn) thư mục | TC-BM-301 done (thư mục đang CONG_KHAI). | hanh_dong=AN | 1. Click [Ẩn] trên dòng thư mục CONG_KHAI. 2. Confirm. | STATE: Backend UPDATE trang_thai=AN, gọi API outbound gỡ thư mục khỏi Cổng. UI: Toast success. Badge AN. | Happy | PASS |  |
| TC-BM-303 | FR-VII-03 AC4 | Xem danh sách "Đã công khai" | `cb_nv_tw_01`. ≥3 thư mục CONG_KHAI tồn tại. | — | 1. Click tab "Đã công khai". | UI: Bảng filter chỉ thư mục trang_thai=CONG_KHAI. Số đếm trên tab khớp số dòng hiển thị. | Happy | PASS |  |
| TC-BM-308 | FR-VII-03 / SM-BIEUMAU AN→CONG_KHAI (A4 merged) | Re-publish thư mục đã ẨN: AN → CONG_KHAI | TC-BM-302 done (TM trạng thái AN, có ≥1 BM). | hanh_dong=CONG_KHAI | 1. Click [Công khai] trên TM trạng thái AN. 2. Confirm. | STATE: Backend UPDATE trang_thai=CONG_KHAI (SM-BIEUMAU AN → CONG_KHAI), gọi API outbound đẩy lại lên Cổng PLQG. | Happy | PASS |  |

---

## 04-TC-quan-ly-bieu-mau

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\bieu-mau\04-TC-quan-ly-bieu-mau.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\bieu-mau\report-04-quan-ly-bieu-mau\Tcs-report\TC-EXECUTION-2026-05-10.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-BM-UI-04 | FR-VII-04 / SCR-VII-02 | Verify form Switch CR-01 ON/OFF | `cb_nv_tw_01`. Vào thư mục → click [+ Thêm biểu mẫu]. | — | 1. Quan sát form mặc định. 2. Bật Switch "Công khai trên Cổng PLQG". 3. Tắt lại. | DEFAULT (OFF): 4 field bắt buộc/option + Switch OFF. SWITCH ON: 3 field bổ sung (Ảnh đại diện, Mô tả công khai, File đính kèm công khai). SWITCH OFF: 3 field bổ sung ẩn lại. | Happy | PASS |  |
| TC-BM-401 | FR-VII-04 AC3 / BR-BM-03 | Tạo biểu mẫu mới với file .docx ≤ 20MB (Switch OFF) | `cb_nv_tw_01`. Thư mục "HĐ LĐ" tồn tại. File `mau-hd-ld.docx` 5MB sẵn local. | thu_muc=HĐ LĐ, ten_BM="Mẫu HĐLĐ chuẩn 2026", file=`mau-hd-ld.docx` | 1. Vào SCR-VII-02. 2. [+ Thêm biểu mẫu]. 3. Fill form, upload file, Switch OFF. 4. [Lưu]. | STATE: Backend validate file format=DOCX, kích thước ≤20MB, ClamAV scan, lưu AES-256, INSERT BIEU_MAU + FILE_DINH_KEM, trang_thai='NHAP', cong_khai=0. | Happy | PASS |  |
| TC-BM-403 | FR-VII-04 (Download) | Tải file biểu mẫu | TC-BM-401 done. | — | 1. Click [Tải về]. | STATE: Backend stream file gốc, AUDIT_LOG hành động='TAI_BIEU_MAU'. UI: Browser download. PERSIST: BIEU_MAU.so_luot_tai +=1. | Happy | PASS |  |
| TC-BM-404 | FR-VII-04 AC7 / BR-PUBLIC-01 + 03 | Bật Switch "Công khai" → auto fill thoi_gian_dang_tai + ảnh đại diện + mô tả công khai | TC-BM-401 done. File ảnh `cover.jpg` 1MB + 1 PDF công khai 3MB. | switch=ON, anh_dai_dien=cover.jpg, mo_ta_cong_khai="...", file_dinh_kem_cong_khai=[hd-ld-cong-khai.pdf] | 1. Sửa BM. 2. Bật Switch. 3. Upload ảnh + nhập mô tả + upload PDF. 4. [Lưu]. | STATE: Backend BR-PUBLIC-01 không có quy trình PD, auto fill thoi_gian_dang_tai=NOW(), gọi API outbound push lên Cổng PLQG. | Happy | PASS |  |
| TC-BM-405 | FR-VII-04 AC8 / BR-PUBLIC-02 | Tắt Switch → cong_khai=0, thoi_gian_dang_tai=NULL, gỡ Cổng | TC-BM-404 done. | switch=OFF | 1. Sửa BM. 2. Tắt Switch. 3. [Lưu]. | STATE: Backend cong_khai=0, clear thoi_gian_dang_tai=NULL, gọi API outbound DELETE gỡ khỏi chuyên trang. | Happy | PASS |  |
| TC-BM-406 | FR-VII-04 AC6 / BR-DATA-01 | Xóa mềm biểu mẫu | TC-BM-401 done (BM trạng thái NHAP). | — | 1. Click [Xóa]. 2. Confirm. | STATE: Backend UPDATE BIEU_MAU SET is_deleted=1 (BR-DATA-01). Nếu trang_thai=CONG_KHAI: gọi API gỡ Cổng trước. | Happy | PASS |  |
| TC-BM-421 | ERR-BM-05 (A6 bổ sung) | Thư mục đích không tồn tại (concurrent delete) | `cb_nv_tw_01`. Mở 2 tab. Tab1: form thêm BM với thư mục "TM-X". Tab2: xóa "TM-X" khi Tab1 chưa submit. | thu_muc_id=TM-X (đã bị xóa) | 1. Tab1 fill form chọn TM-X. 2. Tab2 xóa TM-X. 3. Tab1 click [Lưu]. | STATE: Backend reject (FK invalid sau soft delete). UI: Toast error nguyên văn "Thư mục đích không tồn tại" (ERR-BM-05). | Negative | PASS |  |
| TC-BM-415 | FR-VII-04 Inputs#2 / boundary (A4 merged) | Tên biểu mẫu boundary 500 ký tự (max srs-fr-09:295) | `cb_nv_tw_01`. | ten_BM="A"×500 (boundary), ten_BM="A"×501 (over) | 1. Test ten_BM 500 ký tự + Lưu. 2. Test ten_BM 501 ký tự + Lưu. | STATE: 500 ký tự → INSERT thành công; 501 ký tự → BE reject hoặc client maxlength truncate. UI: 500 → success; 501 → error inline. | Negative | PASS |  |
| TC-BM-422 | FR-VII-04 AC1 (srs-fr-09:370) (Codex 2026-05-09) | Danh sách BM thuộc thư mục — phân trang | `cb_nv_tw_01` login. TM "HĐ LĐ" có ≥25 BM (mix NHAP/CONG_KHAI/AN, mix cong_khai 0/1). | — | 1. Vào SCR-VII-02. 2. Filter thu_muc="HĐ LĐ". | STATE: Backend WHERE thu_muc_id={id} AND don_vi_id=TW.id AND is_deleted=0. Phân trang 20/page. UI: SCR-VII-02 hiển thị 20 BM page 1. | Happy | PASS |  |
| TC-BM-423 | FR-VII-04 AC2 (srs-fr-09:371) (Codex 2026-05-09) | Xem chi tiết biểu mẫu — modal/drawer hiển thị metadata | `cb_nv_tw_01` login. BM "Mẫu HĐLĐ chuẩn 2026" tồn tại (TC-BM-401 done). | — | 1. SCR-VII-02. 2. Click tên BM (hoặc icon Xem chi tiết) trên dòng "Mẫu HĐLĐ". | STATE: Backend GET /bieu-mau/{id} trả full metadata. UI: Modal/drawer/detail page hiển thị tên, ten_linh_vuc, file_ten, kích thước, định dạng, mô tả, ngày tạo, người tạo, badge trạng thái + cong_khai. | Happy | PASS |  |

---

## 05-TC-tim-kiem-bieu-mau

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\bieu-mau\05-TC-tim-kiem-bieu-mau.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\bieu-mau\report-05-tim-kiem-bieu-mau\Tcs-report\TC-EXECUTION-2026-05-10.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-BM-501 | FR-VII-05 AC1 | Tìm theo keyword khớp tên BM | `cb_nv_tw_01`. ≥3 BM thuộc TW: "Mẫu HĐ LĐ", "Mẫu HĐ DV", "Đơn xin việc". | keyword="Mẫu HĐ" | 1. Vào SCR-VII-02. 2. Nhập keyword. 3. [Tìm kiếm]. | STATE: Backend WHERE ten_bieu_mau LIKE '%Mẫu HĐ%' AND is_deleted=0 AND don_vi_id=TW.id. UI: Bảng 2 BM match. | Happy | PASS |  |
| TC-BM-502 | FR-VII-05 AC2 | Filter lĩnh vực + loại hình + thư mục (AND) | `cb_nv_tw_01`. Seed 5 BM với combo khác nhau. | linh_vuc=DAN_SU, loai_hinh=HOP_DONG, thu_muc=HĐ_LĐ | 1. Set 3 filter. 2. [Tìm kiếm]. | STATE: Backend WHERE linh_vuc_id=DAN_SU AND loai_hinh='HOP_DONG' AND thu_muc_id=HĐ_LĐ.id AND auth scope (AND logic). | Happy | PASS |  |
| TC-BM-503 | FR-VII-05 AC3 | Filter định dạng file (.docx) | `cb_nv_tw_01`. Seed 4 BM: 2 docx + 1 xlsx + 1 doc. | dinh_dang=DOCX | 1. Filter định dạng=DOCX. 2. [Tìm kiếm]. | STATE: Backend WHERE dinh_dang='DOCX'. UI: Bảng 2 record. | Happy | PASS |  |
| TC-BM-507 | FR-VII-05 / mã BM scope-out / SPEC-CLARIFY-BM-17 (Codex fix 2026-05-09) | Search keyword vs mã BM — verify SRS scope chỉ tên + mô tả | `cb_nv_tw_01`. Seed 2 BM: mã="BM-001" + mã="BM-0011" (mã auto-gen). | keyword="BM-001" | 1. Search keyword. | STATE: SRS srs-fr-09:402 nguyên văn keyword scope tên + mô tả — KHÔNG quote mã BM. Behavior thực tế cần verify. Mark SPEC-CLARIFY-BM-17. | Edge | PASS |  |
| TC-BM-504 | INF-BM-TK-01 | Search 0 result | `cb_nv_tw_01`. | keyword="ZZZ-NONE-9999" | 1. Search keyword không match. | STATE: Backend trả 0 row. UI: Empty state nguyên văn "Không tìm thấy biểu mẫu phù hợp" (INF-BM-TK-01). | Negative | PASS |  |
| TC-BM-505 | BR-EC-13 | Search SQL injection / XSS payload | `cb_nv_tw_01`. | keyword=`'; DROP TABLE BIEU_MAU; --` rồi `<img src=x onerror=alert(1)>` | 1. Paste 2 payload (2 lần test). 2. [Tìm kiếm]. | STATE: Backend escape/parameterize. KHÔNG drop table; KHÔNG execute script. UI: Empty state hoặc literal match. | Negative | PASS |  |
| TC-BM-508 | INF-BM-TK-01 / multi-filter empty (A4 merged) | Multi-filter AND không có kết quả intersection | `cb_nv_tw_01`. Seed 5 BM với combo lĩnh vực + thư mục đa dạng. | linh_vuc=DAN_SU, thu_muc="HĐ DV" | 1. Set 2 filter intersect không có kết quả. 2. [Tìm kiếm]. | STATE: Backend trả 0 row (AND logic strict). UI: Empty state nguyên văn "Không tìm thấy biểu mẫu phù hợp". | Negative | PASS |  |
| TC-BM-506 | BR-EC-12 | Pagination boundary — page=0 / page_size=200 | `cb_nv_tw_01`. ≥30 BM tồn tại. | URL `?page=0`, `?page=-1`, `?page_size=200` | 1. URL direct hoặc API call. | STATE: Backend reject (BR-EC-12 page_size ∈ [1,100], page ≥ 1). UI: HTTP 400 hoặc fallback default 20/1 — message ERR-PARAM-01. | Edge | PASS |  |
| TC-BM-509 | FR-VII-05 AC1 / BR-DATA-07 (Codex 2026-05-09) | Search BM pagination positive — default 20/page + page navigation + total_count | `cb_nv_tw_01` login. ≥45 BM thuộc TW match keyword="HĐ". | keyword="HĐ" | 1. SCR-VII-02 search "HĐ". 2. Verify page 1 = 20 rows + footer "1-20 / 45". 3. Click page 2 → 20 rows. 4. Click page 3 → 5 rows. | STATE: Backend LIMIT 20 OFFSET 0/20/40. Output total_count=45. UI: Bảng hiển thị 20→20→5 BM mỗi page. | Happy | PASS |  |

---

## 06-TC-import-hang-loat

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\bieu-mau\06-TC-import-hang-loat.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\bieu-mau\report-06-import-hang-loat\Tcs-report\TC-EXECUTION-2026-05-10.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-BM-UI-06 | FR-VII-06 / SCR-VII-03 | Verify wizard SCR-VII-03 | `cb_nv_tw_01`. Vào SCR-VII-02 → click [Nhập hàng loạt]. | — | 1. Quan sát wizard. | WIZARD: 6 component: (1) Thư mục đích select bắt buộc; (2) Tải file Excel metadata + nút [Tải mẫu Excel]; (3) Multi-file upload kéo-thả (max 50 file, max 20MB/file); (4) Bảng kiểm tra; (5) Thống kê; (6) Nút [Xác nhận nhập]. | Happy | PASS |  |
| TC-BM-601 | FR-VII-06 AC1 | Import 5 file hợp lệ vào thư mục đích | `cb_nv_tw_01`. Thư mục "HĐ LĐ" tồn tại. 5 file `.docx` hợp lệ (≤20MB). | thu_muc=HĐ_LĐ.id, files=5 docx | 1. Mở wizard. 2. Chọn thư mục. 3. Upload 5 file. 4. Quan sát bảng kiểm tra (5 rows Hợp lệ). 5. Click [Xác nhận nhập 5 file hợp lệ]. | STATE: Backend validate format + size + virus scan, INSERT 5 BIEU_MAU + 5 FILE_DINH_KEM. UI: Toast success. AUDIT_LOG hành động='BULK_IMPORT', count=5. | Happy | PASS |  |
| TC-BM-602 | ERR-IMP-01 | Tất cả file lỗi (.exe, .pdf) | `cb_nv_tw_01`. | files=[a.exe, b.pdf] | 1. Upload 2 file. 2. Bảng kiểm tra: 2 rows "Lỗi". 3. Nút [Xác nhận] disable. | STATE: Client validate ngay. UI: Bảng kiểm tra cột Trạng thái=Lỗi, lý do "Định dạng không hỗ trợ". Toast error nguyên văn "Không có file nào hợp lệ để import" (ERR-IMP-01). | Negative | PASS |  |
| TC-BM-603 | WRN-IMP-01 | Một số file lỗi — partial import | `cb_nv_tw_01`. | files=[ok1.docx, ok2.docx, bad.exe, big.docx 25MB] | 1. Upload 4 file. 2. Bảng: 2 Hợp lệ + 2 Lỗi. 3. [Xác nhận nhập 2 file hợp lệ]. | STATE: Backend INSERT 2 BM hợp lệ; ghi báo cáo lỗi. UI: Toast warning nguyên văn "Import thành công 2 file. 2 file lỗi: xem chi tiết" (WRN-IMP-01). | Negative | PASS |  |
| TC-BM-604 | ERR-IMP-02 / BR-BM-07 | Vượt 50 file | `cb_nv_tw_01`. 51 file `.docx` valid mỗi file 1MB. | files=51 | 1. Upload 51 file (kéo thả batch). | STATE: Client/Backend reject. UI: Toast error nguyên văn "Tối đa 50 file mỗi lần import" (ERR-IMP-02). KHÔNG hiển thị bảng kiểm tra. | Negative | PASS |  |

---

## 07-TC-permission-matrix

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\bieu-mau\07-TC-permission-matrix.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\bieu-mau\report-07-permission-matrix\Tcs-report\TC-EXECUTION-2026-05-10.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-BM-PERM-001 | BR-AUTH-08 | CB_NV_TW thấy thư mục/BM thuộc TW (own scope) | `cb_nv_tw_01` đăng nhập. Seed 3 thư mục: 1 TW + 1 BN + 1 ĐP, mỗi thư mục có 2 BM. | — | 1. Vào SCR-VII-01. 2. Quan sát danh sách thư mục. 3. Vào SCR-VII-02 → quan sát danh sách BM. | STATE: Backend filter WHERE don_vi_id=TW.id (BR-AUTH-08). UI: SCR-VII-01 chỉ thấy 1 thư mục TW + 2 BM TW; KHÔNG thấy BN/ĐP. | Happy | PASS |  |
| TC-BM-PERM-003 | BR-AUTH-08 | CB_NV_TW KHÔNG sửa được thư mục của BN (cross-don_vi) | `cb_nv_tw_01` đăng nhập. Thư mục BN ID=`thu-muc-bn-001` tồn tại. | thu_muc_id=`thu-muc-bn-001` (cross-don_vi) | 1. Direct URL `/bieu-mau/thu-muc/thu-muc-bn-001/edit`. | STATE: Backend reject (don_vi_id mismatch, BR-AUTH-08). UI: HTTP 403 hoặc redirect SCR-VII-01 với toast. | Negative | PASS |  |
| TC-BM-PERM-005 | BR-FLOW-07 | CB_PD_TW KHÔNG có nút "Phê duyệt" cho biểu mẫu (BR-FLOW-07) | `cb_pd_tw_01` đăng nhập. ≥1 thư mục NHAP có ≥1 BM. | — | 1. Vào SCR-VII-01. 2. Quan sát workflow. | STATE: BR-FLOW-07 nguyên văn "công khai trực tiếp, KHÔNG cần phê duyệt". UI: CB_PD chỉ thấy view + filter, KHÔNG có nút [Phê duyệt]/[Từ chối]. | Negative | PASS |  |
| TC-BM-PERM-009 | Permission Matrix §2.3 / CB_PD Import + Công khai chặn (Codex 2026-05-09) | CB_PD KHÔNG thấy nút [Nhập hàng loạt] + KHÔNG thấy [Công khai] (per matrix CB_PD = ❌ cho 2 action) | `cb_pd_tw_01` đăng nhập. ≥1 thư mục NHAP có ≥3 BM. | — | 1. Vào SCR-VII-01. 2. Quan sát toolbar + cột Hành động. 3. Vào SCR-VII-02. 4. Try URL direct `/bieu-mau/import` (SCR-VII-03). 5. Try URL direct trigger publish API. | STATE: Backend role check. CB_PD permission = chỉ Read. UI: Toolbar SCR-VII-02 KHÔNG có nút [Nhập hàng loạt]. Dòng Hành động KHÔNG có [Công khai]/[Ẩn]. URL direct SCR-VII-03 → 403. | Negative | PASS |  |

---

## Skipped

Không có section nào bị skip — cả 7 file đều có ≥1 TC PASS.
