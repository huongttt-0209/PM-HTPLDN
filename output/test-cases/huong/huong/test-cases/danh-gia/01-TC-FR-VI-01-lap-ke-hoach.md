# TC FR-VI-01 — Lập kế hoạch đợt đánh giá hiệu quả + Phần A Danh sách (UC83)

> **SRS:** [`srs-fr-08-danh-gia.-v3.1.md`](../../../input/srs-v3/srs-fr-08-danh-gia.-v3.1.md) §FR-VI-01 (line 81-159) + §3 Phần A (line 793-826)
> **SCR:** SCR-VI-01 — Phần A Danh sách + Form tạo/sửa
> **URL:** `/danh-gia/ke-hoach/danh-sach`
> **Actor chính:** CB Nghiệp vụ (TW/BN/ĐP) — `cb_nv_*_01`
> **Entity:** KE_HOACH_DANH_GIA (owned, 16 cột)
> **Total TC:** 18 (16 base + 2 fill ban đầu)

---

## Test Cases

| TC ID | Mô tả | Pre-condition | Steps | Expected | Priority | BR/AC/ERR |
|-------|-------|---------------|-------|----------|----------|-----------|
| TC-DG-KH-001 | List đợt đánh giá hiển thị đúng cấu trúc bảng (18 cột) | Login `cb_nv_tw_01`. ≥1 đợt KH-DG. | 1. Click sidebar "Đánh giá hiệu quả hỗ trợ pháp lý"<br>2. Reload nếu blank (recon) | Hiển thị `/danh-gia/ke-hoach/danh-sach`. Bảng có cột: Mã đợt / Tên đợt / Tần suất / Đối tượng / Kỳ đánh giá / Trạng thái / Người tạo / Ngày tạo / Hành động. Pagination 20/trang | High | AC-1 |
| TC-DG-KH-002 | Filter trạng thái — chọn `LAP_KE_HOACH` chỉ hiển thị đợt LAP_KE_HOACH | Login `cb_nv_tw_01`. ≥2 đợt khác state. | 1. Mở filter trạng thái<br>2. Chọn `LAP_KE_HOACH` | Bảng filter chỉ đợt LAP_KE_HOACH. Tổng count cập nhật. URL có query param `?trang_thai=LAP_KE_HOACH` | High | SCR row #6 |
| TC-DG-KH-003 | Filter tần suất + đối tượng đồng thời | Login. | 1. Filter tần suất = `SO_BO_6_THANG`<br>2. Filter đối tượng = `VU_VIEC` | Bảng AND 2 filter. Đợt thỏa cả 2 mới hiển thị | Medium | SCR row #4-5 |
| TC-DG-KH-004 | Filter khoảng ngày — Từ ngày 2026-01-01 đến 2026-06-30 | Login. | 1. Chọn date range<br>2. Apply | Đợt có `tu_ngay` trong range hiển thị. Đợt ngoài bị ẩn | Medium | SCR row #7 |
| TC-DG-KH-005 | Search keyword — nhập tên đợt "Q2/2026" | Login. Đợt DG-20260502-0001 có tên "Q2/2026". | 1. Nhập "Q2" vào ô search<br>2. Enter | Bảng filter — match cả tên đợt + mã đợt. Result chính xác | Medium | SCR row #3 |
| TC-DG-KH-006 | Tạo đợt mới — happy path | Login `cb_nv_tw_01`. | 1. Click [+ Tạo đợt đánh giá]<br>2. Nhập: ten_dot="ĐG Test 2026 H1", muc_tieu="Đánh giá hiệu quả Q1+Q2/2026", tan_suat=`SO_BO_6_THANG`, tu_ngay=`2026-01-01`, den_ngay=`2026-06-30`, doi_tuong=`VU_VIEC`, co_quan_duoc_danh_gia_id chọn BN BKH<br>3. Click [Lưu nháp] | Toast "Tạo đợt đánh giá thành công". Entity `ma_ke_hoach` (UI label: "Mã đợt") format `DG-{YYYYMMDD}-{SEQ}`. Trạng thái = LAP_KE_HOACH. AUDIT_LOG có record CREATE với `created_by`, `don_vi_id`, `created_at` đầy đủ (BR-DATA-03) | Critical | UC83 happy path, BR-DATA-03/04/05, SM-DANHGIA #1 |
| TC-DG-KH-007 | Tạo đợt — thiếu nhiều trường bắt buộc → ERR-DG-KH-01 | Login. | 1. Click [+ Tạo đợt]<br>2. Để trống `ten_dot` + `muc_tieu`<br>3. Click [Lưu nháp] | Form không submit. Hiển thị inline error trên 2 trường + toast NGUYÊN VĂN "Vui lòng nhập đầy đủ thông tin bắt buộc" (ERR-DG-KH-01) | High | ERR-DG-KH-01, AC E1 |
| TC-DG-KH-008 | Tạo đợt — `tu_ngay >= den_ngay` → ERR-DG-KH-02 | Login. | 1. Click [+ Tạo đợt]<br>2. Nhập tu_ngay=`2026-06-30`, den_ngay=`2026-01-01`<br>3. Lưu | Hiển thị "Ngày bắt đầu phải trước ngày kết thúc" (ERR-DG-KH-02) | High | ERR-DG-KH-02, AC E2 |
| TC-DG-KH-009 | Tạo đợt — `tan_suat` chỉ chấp nhận `SO_BO_6_THANG` / `TRON_NAM` (BR-LEGAL-08) | Login. | 1. Mở dropdown tần suất | Dropdown chỉ có 2 option (KHÔNG có DOT_XUAT). Verify per BR-LEGAL-08 | Critical | BR-LEGAL-08 |
| TC-DG-KH-010 | Tạo đợt — auto gợi ý `tan_suat` theo tháng hiện tại | Login. Tháng hiện tại 2026-05. | 1. Click [+ Tạo đợt]<br>2. Quan sát default tần suất | Default = `SO_BO_6_THANG` (tháng 1-6 → Sơ bộ 6 tháng) per SCR row #23 | Low | SCR row #23 |
| TC-DG-KH-011 | Sửa đợt LAP_KE_HOACH — happy path | Login. Đợt mới tạo state LAP_KE_HOACH. | 1. Click icon Sửa hàng đợt<br>2. Đổi ten_dot="ĐG Test 2026 H1 v2"<br>3. Lưu | Toast success. Bảng cập nhật ten_dot mới. AUDIT_LOG có UPDATE | High | AC-3 (chỉnh sửa KH chưa duyệt) |
| TC-DG-KH-012 | Sửa đợt — guard chỉ cho LAP_KE_HOACH/PHAN_CONG | Login. Đợt state THUC_HIEN. | 1. Click icon Sửa hàng đợt | Icon Sửa disabled hoặc click → toast "Đợt không ở trạng thái cho phép sửa" | High | SCR row #18 (Sửa chỉ LAP/PHAN_CONG) |
| TC-DG-KH-013 | Xóa đợt LAP_KE_HOACH (soft delete) | Login. Đợt LAP_KE_HOACH. | 1. Click icon Xóa<br>2. Confirm modal | Toast success. Đợt biến khỏi danh sách. DB: `is_deleted=1` (soft) | High | AC-4 |
| TC-DG-KH-014 | Xóa đợt — guard chỉ cho LAP_KE_HOACH | Login. Đợt PHAN_CONG/THUC_HIEN. | 1. Click icon Xóa | Icon Xóa disabled hoặc click → toast "Đợt đã chuyển trạng thái, không thể xóa" | High | SCR row #18 (Xóa chỉ LAP_KE_HOACH) |
| TC-DG-KH-015 | Hủy đợt từ LAP_KE_HOACH → HUY (lý do bắt buộc) | Login. Đợt LAP_KE_HOACH. | 1. Mở chi tiết đợt<br>2. Click [Hủy đợt]<br>3. Nhập lý do "Đợt sai kỳ đánh giá, hủy"<br>4. Confirm | Toast success. Trạng thái → HUY. AUDIT_LOG có CANCEL | High | SM-DANHGIA #10, GAP-VI-01 |
| TC-DG-KH-016 | Mở chi tiết đợt → 4 Tabs hiển thị | Login. Đợt bất kỳ. | 1. Click mã đợt | Mở chi tiết với 4 tabs: Tiêu chí / Phân công / Thực hiện chấm điểm / Báo cáo | Critical | SCR §3 Phần B |
| TC-DG-KH-017 | Xuất Excel danh sách đợt | Login `cb_nv_tw_01`. ≥3 đợt. | 1. Click [Xuất Excel] toolbar | Tải file `.xlsx`. Cột header khớp bảng UI. Data đúng dòng filter hiện tại | High | SCR row #2 |
| TC-DG-KH-018 | Pagination 20 mục/trang | Login. ≥25 đợt. | 1. Vào trang 1<br>2. Đếm row<br>3. Click trang 2 | Trang 1 hiển thị 20. Trang 2 hiển thị phần còn lại. URL có `?page=2` | Medium | SCR row #20 |

---

## Edge bổ sung (A4 — merge 2026-05-10)

| TC ID | Mô tả | Pre-condition | Steps | Expected | Priority | BR/AC/ERR |
|-------|-------|---------------|-------|----------|----------|-----------|
| TC-DG-KH-019 | Boundary `ten_dot` đúng 500 ký tự (max) | Login. | 1. Click [+ Tạo đợt]<br>2. Nhập ten_dot 500 ký tự | Lưu thành công. DB persist đầy đủ 500 | Medium | UC83 input #1 max 500 |
| TC-DG-KH-020 | Boundary `ten_dot` 501 ký tự → block | Login. | 1. Nhập ten_dot 501 ký tự | Inline error "Tên đợt tối đa 500 ký tự" | Medium | UC83 input #1 |
| TC-DG-KH-021 | Boundary `ghi_chu` 2000 ký tự (max) | Login. | 1. Nhập ghi_chu 2000 ký tự | Lưu OK | Low | UC83 input #7 max 2000 |
| TC-DG-KH-022 | Tu_ngay = den_ngay → ERR-DG-KH-02 (boundary) | Login. | 1. Nhập tu_ngay = den_ngay = 2026-06-30 | ERR-DG-KH-02 (vì spec yêu cầu `tu_ngay < den_ngay`) | High | UC83 input #4-5 ràng buộc, ERR-DG-KH-02 |
| TC-DG-KH-023 | Concurrency — 2 user TW tạo đợt cùng `ma_dot` | Login 2 tab `cb_nv_tw_01` + `cb_nv_tw_01` (2 session). | 1. Cùng lúc click [+ Tạo đợt]<br>2. Cùng kỳ + đối tượng | Cả 2 tạo OK với `SEQ` khác nhau (BR-DATA-04 monotonic). KHÔNG conflict ma_dot | Medium | BR-DATA-04 SEQ monotonic |
| TC-DG-KH-024 | Soft-delete cycle — đợt đã xóa không hiển thị + không tạo trùng `ma_dot` | Login. Tạo + xóa đợt DG-X. | 1. Tạo đợt mới cùng kỳ | `ma_dot` mới SEQ kế tiếp (không reuse SEQ cũ). DB `is_deleted=1` cho đợt cũ | Medium | BR-DATA-01 (working label soft delete) |
| TC-DG-KH-025 | Hủy đợt khi đang HOAN_THANH → block | Login. Đợt HOAN_THANH. | 1. Tìm nút [Hủy đợt] | Nút ẩn. Force trigger → block "Đợt đã hoàn thành, không thể hủy" | Medium | SM-DANHGIA guard "chưa HOAN_THANH" |
| TC-DG-KH-026 | XSS payload trong `ten_dot` — sanitize | Login. | 1. Nhập ten_dot = `<script>alert('xss')</script>Test` | Lưu OK với HTML escape (text hiển thị literal, KHÔNG execute script) | High | Security baseline |
| TC-DG-KH-027 | File đính kèm KH (file_dinh_kem v3.5) — upload PDF 19MB | Login. CR-07 v3.5. | 1. Form tạo đợt → upload PDF 19MB | Lưu OK. File link xuất hiện ở chi tiết đợt | Medium | KE_HOACH_DANH_GIA col #15 (CR-07) |
| TC-DG-KH-028 | File đính kèm KH > 20MB → block | Login. | 1. Upload file 21MB | Inline error "Mỗi file tối đa 20MB" | Medium | Col #15 ràng buộc |
| TC-DG-KH-029 | `co_quan_duoc_danh_gia_id` field bắt buộc (CR-10 v3.5) | Login. | 1. Tạo đợt KHÔNG chọn cơ quan được ĐG<br>2. Lưu | Inline error "Vui lòng chọn cơ quan được đánh giá" (Q-07 + CR-10) | High | Col #16 bắt buộc Y |
| TC-DG-KH-030 | `co_quan_duoc_danh_gia_id` ≠ `don_vi_id` user lập | Login `cb_nv_tw_01`. | 1. Mở dropdown chọn cơ quan được ĐG<br>2. Cố chọn TW | Tự loại trừ chính `don_vi_id` user (TW). Dropdown chỉ chứa BN/ĐP per spec "Khác don_vi_id" | High | Col #16 ràng buộc "Khác don_vi_id" |

## Codex Review apply (2026-05-10)

| TC ID | Mô tả | Pre-condition | Steps | Expected | Priority | BR/AC/ERR |
|-------|-------|---------------|-------|----------|----------|-----------|
| TC-DG-KH-031 | Required `muc_tieu` đơn lẻ → ERR-DG-KH-01 (P2 F-023) | Login. | 1. [+ Tạo đợt]<br>2. Nhập đủ ten_dot + tu_ngay + den_ngay + tan_suat + doi_tuong nhưng để trống `muc_tieu`<br>3. Lưu | Inline error trên trường `muc_tieu` + toast NGUYÊN VĂN "Vui lòng nhập đầy đủ thông tin bắt buộc" (ERR-DG-KH-01) | High | ERR-DG-KH-01 single-field |
| TC-DG-KH-032 | Required `ten_dot` đơn lẻ → ERR-DG-KH-01 (P2 F-023) | Login. | 1. [+ Tạo đợt]<br>2. Đầy đủ trừ `ten_dot`<br>3. Lưu | Inline error trên `ten_dot` + ERR-DG-KH-01 NGUYÊN VĂN "Vui lòng nhập đầy đủ thông tin bắt buộc" | High | ERR-DG-KH-01 single-field |
| TC-DG-KH-033 | `doi_tuong` enum coverage 3 valid + 1 invalid (P2 F-024) | Login. | 1. Tạo 3 đợt với doi_tuong = VU_VIEC, DAO_TAO, TONG_HOP<br>2. Force submit doi_tuong="INVALID_VALUE" qua devtools/API | 3 đợt valid lưu OK. Forced invalid → 400 + lỗi enum constraint | Medium | UC83 input #6 enum |
| TC-DG-KH-034 | File đính kèm extension whitelist (P1 F-009) | Login. | 1. Tạo đợt với file_dinh_kem upload `test.exe`<br>2. Upload `test.png`<br>3. Upload `test.docx`<br>4. Upload `test.xlsx` | `.exe` + `.png` reject "Định dạng file không được hỗ trợ. Chỉ chấp nhận PDF/DOC/DOCX/XLS/XLSX". `.docx` + `.xlsx` accept | High | KE_HOACH_DANH_GIA col #15 ràng buộc PDF/DOC/DOCX/XLS/XLSX |
| TC-DG-KH-035 | `co_quan_duoc_danh_gia_id` invalid FK (P1 F-010) | Login. | 1. Force submit POST `/api/danh-gia/ke-hoach` với `co_quan_duoc_danh_gia_id` = 99999999 (không tồn tại) | 400/422 + lỗi FK constraint "Cơ quan được đánh giá không hợp lệ" | High | KE_HOACH_DANH_GIA col #16 FK validity |
| TC-DG-KH-036 | Default sort ngày tạo giảm dần (P2 F-022) | Login. ≥3 đợt tạo cách nhau. | 1. Mở danh sách<br>2. Quan sát thứ tự cột "Ngày tạo" | Đợt mới nhất ở top. Sort desc default per SCR §3.7 | Low | SCR §3.7 quy tắc tương tác |
| TC-DG-KH-037 | Batch delete checkbox + [Xóa hàng loạt] (P2 F-021) | Login. ≥3 đợt LAP_KE_HOACH. | 1. Tích checkbox 2 đợt<br>2. Banner "Đã chọn 2 mục" + nút [Xóa hàng loạt]<br>3. Click + confirm | Cả 2 soft delete. Đợt PHAN_CONG/THUC_HIEN trong selection bị skip + cảnh báo "X đợt đã chuyển trạng thái không thể xóa" | Medium | SCR row #19 |

## Tổng số TC: 37 (18 base + 12 edge A4 + 7 Codex apply)

> **A4 done 2026-05-10** — 12 TC mới merge inline. Audit log ở [`08-REVIEW-edge-case-hunter.md`](./08-REVIEW-edge-case-hunter.md).
> **A6 placeholder — TC fill GAP-A5 sẽ MERGE vào Section "Fill GAP A5".**
> **A7 placeholder — TC bị LOẠI/SỬA sẽ Edit IN-PLACE + log ở `11-a7-filter-log.md`.**
