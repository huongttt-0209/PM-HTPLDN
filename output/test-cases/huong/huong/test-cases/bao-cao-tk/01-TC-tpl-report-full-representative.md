# Test Cases — FR-IX Representative (TPL-REPORT-FULL): BC Hỏi đáp (FR-IX-01 / UC124)

> **SRS Ref**: srs-fr-11:55-176 (template TPL-REPORT-FULL + FR-IX-01 đặc thù), SCR-IX-01, Entity BAO_CAO + HOI_DAP
> **Ngày tạo**: 2026-05-10
> **Đặc thù**: File này test toàn bộ template TPL-REPORT-FULL chung cho 23 BC, dùng FR-IX-01 BC Hỏi đáp làm representative. Mọi TC PASS ở file này hàm ý 22 BC còn lại được expect cùng hành vi cho input/processing/output/error chung. Đặc thù riêng từng BC test ở `02-TC-smoke-23-loai-bc.md`.

---

## Quy ước

- **Priority**: 🔴 P0 (critical) · 🟡 P1 (high) · 🟢 P2 (medium)
- **TraceID**: `FR-IX-01 / TPL.{section}` hoặc `FR-IX-01 / E{N}`
- **Pre-conditions mặc định**: User đã đăng nhập (BR-AUTH-01), có quyền xem BC, dữ liệu HOI_DAP đã duyệt tồn tại trong kỳ test (BR-RPT-01).

---

## Trường input — FR-IX-01 (template + đặc thù)

| # | Field | Bắt buộc | Kiểu | Ràng buộc | Mặc định |
|---|-------|----------|------|-----------|----------|
| 1 | ky_bao_cao | Y | text | TUAN / THANG / QUY / NAM / KHOANG | — |
| 2 | tu_ngay | Y | datetime | <= den_ngay | — |
| 3 | den_ngay | Y | datetime | >= tu_ngay | — |
| 4 | don_vi_id | N | identifier | Auto phân quyền nếu không truyền | — |
| 5 | format_xuat | Y | text | XLSX / PDF | XLSX |
| 6 | linh_vuc_id | N | identifier | FK → DANH_MUC (đặc thù FR-IX-01) | — |
| 7 | trang_thai_hd | N | text | DA_TRA_LOI / CHO_TRA_LOI (đặc thù FR-IX-01) | — |

---

## A. HAPPY — Input chung + Processing + Output

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BC-REP-001 | FR-IX-01 / TPL.Process step 1-6 + AC#1 | Tạo BC Hỏi đáp kỳ THANG đơn vị TW — happy | cb_nv_tw_01 login. ≥10 HOI_DAP (5 DA_TRA_LOI + 5 CHO_TRA_LOI) trong tháng hiện tại scope toàn quốc. | ky=THANG, tu_ngay/den_ngay auto = tháng hiện tại, don_vi=Toàn quốc, format=XLSX | 1. SCR-IX-01. 2. Chọn dropdown "BC Số lượng hỏi đáp/vướng mắc pháp luật". 3. Chọn kỳ THANG. 4. Click [Xem báo cáo]. | (1) GET `/bao-cao/hoi-dap?ky=THANG&...` 200. (3) Bảng hiện: tong_hoi_dap=10, da_tra_loi=5, cho_tra_loi=5, ty_le_tra_loi=50%. Biểu đồ Donut 2 phần + Trend line. tong_ban_ghi=10, ngay_tao_bc=NOW(), nguoi_tao=cb_nv_tw_01. | Happy 🔴 |
| TC-BC-REP-002 | FR-IX-01 / TPL.Input#1 (kỳ TUAN) | Tạo BC kỳ TUAN auto fill ngày | cb_nv_tw_01 login. HOI_DAP tuần hiện tại tồn tại. | ky=TUAN | 1. Chọn kỳ TUAN. | (1) tu_ngay/den_ngay auto = thứ 2 đầu tuần đến CN cuối tuần. (3) Bảng + biểu đồ render. | Happy 🟡 |
| TC-BC-REP-003 | FR-IX-01 / TPL.Input#1 (kỳ QUY) | Tạo BC kỳ QUY | cb_nv_tw_01 login. HOI_DAP quý hiện tại. | ky=QUY | 1. Chọn kỳ QUY. | (1) tu_ngay/den_ngay = đầu/cuối quý hiện tại (90-92 ngày). | Happy 🟡 |
| TC-BC-REP-004 | FR-IX-01 / TPL.Input#1 (kỳ NAM) | Tạo BC kỳ NAM (skip rule 366 ngày) | cb_nv_tw_01 login. HOI_DAP năm hiện tại. | ky=NAM | 1. Chọn kỳ NAM. | (1) tu_ngay=01/01, den_ngay=31/12. (3) Không trigger ERR-RPT-02 (NAM exempt). | Happy 🟡 |
| TC-BC-REP-005 | FR-IX-01 / TPL.Input#1 (kỳ KHOANG) | Tạo BC kỳ KHOANG tùy chọn ≤366 ngày | cb_nv_tw_01 login. HOI_DAP khoảng 60 ngày. | ky=KHOANG, tu_ngay=01/03/2026, den_ngay=30/04/2026 (60 ngày) | 1. Chọn kỳ KHOANG. 2. Chọn 2 ngày. 3. [Xem]. | (3) Bảng render data trong khoảng 60 ngày. | Happy 🟡 |
| TC-BC-REP-006 | FR-IX-01 / TPL.Input#5 + AC#2 | Xuất Excel sau khi đã xem BC | cb_nv_tw_01 login. Đã chạy TC-BC-REP-001 thành công. | format=XLSX | 1. Click [Xuất Excel (.xlsx)]. | (1) POST `/bao-cao/.../export?format=xlsx` 200. (2) File `bao-cao-hoi-dap-{YYYYMMDD}.xlsx` tải về. (3) Mở file: header có tieu_de + ky_bao_cao + don_vi_ten + ngay_tao_bc + nguoi_tao (TT17/2025). Bảng dữ liệu sticky header. | Happy 🔴 |
| TC-BC-REP-007 | FR-IX-01 / TPL.Input#5 + AC#3 | Xuất PDF sau khi đã xem BC | cb_nv_tw_01 login. Đã chạy TC-BC-REP-001. | format=PDF | 1. Click [Xuất PDF (.pdf)]. | (1) POST export 200. (2) File `.pdf` tải về. (3) Khổ A4, font Times New Roman cỡ 13 (TT17/2025). Header BC + bảng + biểu đồ embed. | Happy 🔴 |
| TC-BC-REP-008 | FR-IX-01 / TPL.Output#1-8 | Verify đầy đủ output chung | cb_nv_tw_01 login. Data ≥1 HD. | ky=THANG | 1. [Xem]. | (3) Bảng có 8 trường output chung: ten_bao_cao, ky_bao_cao, tu_ngay/den_ngay, don_vi_ten, ngay_tao_bc, nguoi_tao, tong_ban_ghi, data[]. | Happy 🟡 |
| TC-BC-REP-009 | FR-IX-01 / TPL.Output đặc thù IX01 | Verify 7 trường output đặc thù FR-IX-01 | cb_nv_tw_01 login. ≥10 HD nhiều lĩnh vực. | ky=THANG | 1. [Xem]. | (3) Output có: tong_hoi_dap, da_tra_loi, cho_tra_loi, ty_le_tra_loi, theo_linh_vuc[], theo_don_vi[], theo_ky[]. | Happy 🟡 |
| TC-BC-REP-010 | FR-IX-01 / TPL.Process step 10 + BR-DATA-05 | Verify nhật ký ghi nhận xem BC | cb_nv_tw_01 login. | ky=THANG | 1. [Xem]. 2. Login qtht_01. 3. Mở Nhật ký HT (`/quan-tri/audit-log`). | (3) Có 1 bản ghi: hanh_dong=XEM_BC, doi_tuong=BC_HOI_DAP, user=cb_nv_tw_01, thoi_gian≈NOW, bo_loc(JSON) chứa ky=THANG + don_vi=Toàn quốc. | Happy 🔴 |
| TC-BC-REP-011 | FR-IX-01 / TPL.Process step 10 + BR-DATA-05 | Verify nhật ký ghi nhận xuất BC | cb_nv_tw_01 login. Đã xem. | format=XLSX | 1. Xuất Excel. 2. qtht_01 mở Nhật ký HT. | (3) Có 1 bản ghi: hanh_dong=XUAT_BC, format=XLSX, doi_tuong=BC_HOI_DAP, user=cb_nv_tw_01. | Happy 🟡 |

---

## B. NEGATIVE — Error Handling chung E1-E9 + đặc thù

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BC-REP-020 | FR-IX-01 / E1 ERR-RPT-01 | tu_ngay > den_ngay | cb_nv_tw_01 login. | ky=KHOANG, tu_ngay=10/05/2026, den_ngay=01/05/2026 | 1. Chọn KHOANG. 2. Nhập tu_ngay > den_ngay. 3. [Xem]. | (2) Toast/inline error: **"Ngày bắt đầu phải trước hoặc bằng ngày kết thúc"** (ERR-RPT-01). Không gọi API. | Negative 🔴 |
| TC-BC-REP-021 | FR-IX-01 / E2 ERR-RPT-02 | Khoảng thời gian > 366 ngày (kỳ KHOANG) | cb_nv_tw_01 login. | ky=KHOANG, tu_ngay=01/01/2025, den_ngay=15/01/2026 (380 ngày) | 1. Chọn KHOANG. 2. Nhập khoảng 380 ngày. 3. [Xem]. | (2) Error: **"Khoảng thời gian tối đa 1 năm. Sử dụng kỳ 'NAM' cho BC dài hơn"** (ERR-RPT-02). | Negative 🔴 |
| TC-BC-REP-022 | FR-IX-01 / E3 INF-RPT-01 / Codex F-08 | Không có dữ liệu | cb_nv_tw_01 login. Không có HOI_DAP trong tháng test. | ky=THANG, tu_ngay/den_ngay tháng không có data | 1. Chọn kỳ THANG có 0 record. 2. [Xem]. | (3) Empty state: **"Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn"** (INF-RPT-01). Không có bảng + biểu đồ. **Export behavior khi empty xem SPEC-CLARIFY-BC-06** (TC-BC-REP-042 verify thực tế disabled hay xuất file rỗng — KHÔNG assert disabled deterministic ở đây để tránh mâu thuẫn). | Negative 🔴 |
| TC-BC-REP-023 | FR-IX-01 / E5 ERR-RPT-03 | Timeout truy vấn > 30s | cb_nv_tw_01 login. (Khó reproduce — mark MANUAL-INJECTION nếu BE trả 504/timeout) | ky=NAM toàn quốc với data lớn | 1. Tạo BC NAM toàn quốc. (BE inject delay 35s qua test fixture) | (2) Toast: **"Truy vấn quá thời gian. Vui lòng thu hẹp khoảng thời gian hoặc bộ lọc"** (ERR-RPT-03). | Negative 🟡 (manual) |
| TC-BC-REP-024 | FR-IX-01 / E6 ERR-RPT-04 | Lỗi xuất file (BE inject) | cb_nv_tw_01 login. Đã xem BC. | format=XLSX | 1. (BE inject lỗi tạo file .xlsx). 2. Click Xuất Excel. | (2) Toast: **"Không thể tạo file xuất. Vui lòng thử lại"** (ERR-RPT-04). | Negative 🟡 (manual) |
| TC-BC-REP-025 | FR-IX-01 / E7 ERR-RPT-05 | Không có quyền (NHT/TVV/CG/DN/GV) | nht_01 login (hoặc tvv_01/cg_01/dn_01/gv_01) | — | 1. Truy cập `/bao-cao` URL trực tiếp. | (1) GET 403. (3) Toast/page: **"Bạn không có quyền xem báo cáo này"** (ERR-RPT-05). Sidebar không có mục "Báo cáo thống kê" cho role này. | Negative 🔴 |
| TC-BC-REP-026 | FR-IX-01 / E8 ERR-RPT-06 | Format xuất không hợp lệ (manual API) | cb_nv_tw_01 login. | format=DOCX (không hợp lệ) | 1. Mở DevTools. 2. POST `/bao-cao/.../export?format=DOCX`. | (1) 400. (3) Toast: **"Định dạng xuất chỉ hỗ trợ XLSX hoặc PDF"** (ERR-RPT-06). | Negative 🟡 (manual API via DevTools) |
| TC-BC-REP-027 | FR-IX-01 / E9 ERR-RPT-07 / SPEC-CLARIFY-BC-02 | Template báo cáo bị hỏng | cb_nv_tw_01 login. | (BE inject template missing) | 1. Click [Xem]. (Template BAO_CAO bị xóa/hỏng). | (2) Toast: **"Mẫu báo cáo không khả dụng. Vui lòng liên hệ QTHT"** (ERR-RPT-07). | Negative 🟢 (manual injection — SPEC-CLARIFY-BC-02 reproducibility) |
| TC-BC-REP-028 | FR-IX-01 / E1 đặc thù ERR-RPT-IX01-01 | Lĩnh vực PL không tồn tại (manual injection) | cb_nv_tw_01 login. | linh_vuc_id=999999 (không tồn tại) | 1. Mở DevTools modify request. 2. POST với linh_vuc_id invalid. | (1) 400. (3) Toast: **"Lĩnh vực PL không tồn tại"** (ERR-RPT-IX01-01). | Negative 🟢 |

---

## C. EDGE — Boundary + Special

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BC-REP-040 | FR-IX-01 / TPL.Input#2-3 boundary | Khoảng 366 ngày exact (kỳ KHOANG) | cb_nv_tw_01 login. | ky=KHOANG, 366 ngày exact | 1. Nhập tu_ngay=01/01/2025 + den_ngay=01/01/2026 (366 ngày inclusive). 2. [Xem]. | (1) Pass (boundary inclusive). KHÔNG ERR-RPT-02. | Edge 🟡 |
| TC-BC-REP-041 | FR-IX-01 / TPL.Input#2-3 boundary | Khoảng 367 ngày (kỳ KHOANG) — fail | cb_nv_tw_01 login. | ky=KHOANG, 367 ngày | 1. Nhập 367 ngày. 2. [Xem]. | (2) ERR-RPT-02 trigger (boundary +1 fail). | Edge 🟡 |
| TC-BC-REP-042 | FR-IX-01 / TPL.Process step 7-8 | Empty kết quả nhưng vẫn xuất file | cb_nv_tw_01 login. Tháng không có HD. | ky=THANG empty | 1. [Xem] → empty state. 2. Click Xuất XLSX. | (3) **SPEC-CLARIFY-BC-06**: Behavior pending — (a) nút Xuất disabled khi empty state, hoặc (b) xuất file rỗng (chỉ header). Verify thực tế + log. | Edge 🟢 |
| TC-BC-REP-043 | FR-IX-01 / TPL.Input#1 (giao kỳ) | Đổi kỳ giữa lần xem | cb_nv_tw_01 login. | ky=THANG → đổi sang QUY | 1. Chọn THANG + [Xem]. 2. Đổi sang QUY + [Xem]. | (3) Bảng + biểu đồ refresh đúng kỳ mới. tu_ngay/den_ngay tự cập nhật. | Edge 🟢 |
| TC-BC-REP-044 | SCR-IX-01 row#3 + AC | Đổi loại BC giữa lần xem (dropdown grouped) | cb_nv_tw_01 login. | BC HD → BC VV đã tiếp nhận | 1. Chọn HD + [Xem]. 2. Đổi dropdown sang BC VV đã tiếp nhận. | (3) Bộ lọc đặc thù tự render lại theo loại BC mới (linh_vuc + trang_thai_hd → kenh_tiep_nhan + linh_vuc). Bảng/biểu đồ refresh. | Edge 🟡 |
| TC-BC-REP-045 | SCR-IX-01 row#10 | Toggle hiện/ẩn biểu đồ | cb_nv_tw_01 login. Đã xem BC. | — | 1. Click toggle "Ẩn biểu đồ". 2. Click "Hiện biểu đồ". | (3) Biểu đồ ẩn → bảng full width. Toggle hiện lại → bảng + biểu đồ. | Edge 🟢 |
| TC-BC-REP-046 | SCR-IX-01 row#12 | Skeleton loading khi đang query | cb_nv_tw_01 login. | ky=NAM toàn quốc (slow query) | 1. [Xem]. (Quan sát trong khi loading). | (3) Skeleton placeholder hiện trước khi data load. Sau khi 200 → skeleton biến mất, bảng + biểu đồ hiện. | Edge 🟢 |
| TC-BC-REP-047 | TPL.Process step 4 + BR-RPT-01 | Chỉ bản ghi đã duyệt được tính | cb_nv_tw_01 login. 5 HD CHO_DUYET (chưa duyệt) + 3 HD DA_TRA_LOI + 2 HD CHO_TRA_LOI. | ky=THANG | 1. [Xem]. | (3) tong_hoi_dap=5 (3 + 2 đã duyệt). 5 HD CHO_DUYET KHÔNG được tính (BR-RPT-01). | Edge 🔴 |
| TC-BC-REP-048 | SCR-IX-01 row#11 | Bảng cuộn ngang trên màn hình 1024-1279px | cb_nv_tw_01 login. Bảng 8+ cột. | viewport=1280px | 1. Resize browser xuống 1024px. 2. [Xem]. | (3) Bảng có scroll-x ngang, sticky header giữ nguyên. | Edge 🟢 |

---

## D. CROSS — Filter đặc thù FR-IX-01

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BC-REP-060 | FR-IX-01 / Input đặc thù #1 + AC#bổ sung | Filter theo lĩnh vực PL | cb_nv_tw_01 login. ≥5 HD lĩnh vực "Dân sự" + ≥5 HD "Hình sự". | linh_vuc=Dân sự | 1. Chọn dropdown lĩnh vực Dân sự. 2. [Xem]. | (3) Chỉ HD lĩnh vực Dân sự được tính. theo_linh_vuc[] chỉ có 1 entry "Dân sự". | Happy 🟡 |
| TC-BC-REP-061 | FR-IX-01 / Input đặc thù #2 | Filter theo trạng thái HD | cb_nv_tw_01 login. ≥3 HD DA_TRA_LOI + ≥3 HD CHO_TRA_LOI. | trang_thai_hd=CHO_TRA_LOI | 1. Chọn trang_thai_hd=CHO_TRA_LOI. 2. [Xem]. | (3) Chỉ HD CHO_TRA_LOI được tính. cho_tra_loi=≥3, da_tra_loi=0. | Happy 🟡 |
| TC-BC-REP-062 | FR-IX-01 / Combined filter | Combine filter linh_vuc + trang_thai | cb_nv_tw_01 login. | linh_vuc=Dân sự + trang_thai_hd=DA_TRA_LOI | 1. Chọn cả 2. 2. [Xem]. | (3) Chỉ HD Dân sự đã trả lời được tính. | Happy 🟢 |

---

## E. EDGE bổ sung (A4 inline merge 2026-05-10)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BC-REP-049 | TPL.Input#2 boundary date / A4 E1 | BC kỳ THANG cuối tháng 31 ngày auto fill | cb_nv_tw_01 login. Đang ở tháng có 31 ngày (vd 03/2026). | ky=THANG | 1. Chọn THANG. (Auto fill). | (3) tu_ngay=01/03/2026, den_ngay=**31/03/2026** (đầy đủ 31 ngày, không bị truncate về 30). | Edge 🟡 |
| TC-BC-REP-050 | TPL.Input#2 boundary date / A4 E2 | BC kỳ THANG tháng 2 năm nhuận 29/02 | cb_nv_tw_01 login. Năm nhuận 2024. | ky=THANG, tháng 02/2024 | 1. Chọn KHOANG, fill tu_ngay=01/02/2024 + den_ngay=29/02/2024. | (3) Date picker accept 29/02/2024 (không skip). BC chạy đúng kỳ. | Edge 🟢 |
| TC-BC-REP-051 | TPL.Process step 1-6 / A4 E3 | Refresh trang giữa khi đang [Xem] BC slow query | cb_nv_tw_01 login. BC NAM toàn quốc data lớn. | ky=NAM | 1. Click [Xem]. 2. Trong khi loading skeleton, F5. | (3) **Behavior verify**: (a) URL deep-link giữ filter → tự re-trigger query, hoặc (b) reset SCR về initial. Log nếu surprising. KHÔNG crash. | Edge 🟡 |
| TC-BC-REP-052 | TPL.Process / A4 E4 / A7 SỬA | Đóng tab giữa query slow | cb_nv_tw_01 login. | ky=NAM | 1. [Xem]. 2. Đóng tab. 3. Login lại. 4. Mở Nhật ký HT (`/quan-tri/audit-log`). | (3) Audit log có entry XEM_BC start (hành_dong=XEM_BC, doi_tuong=BC_HOI_DAP, user=cb_nv_tw_01) nhưng KHÔNG có entry follow-up "XUAT_BC" hoặc trạng_thai_BC=HOAN_THANH (BE cancel). UI bridge verify qua audit log only (không cần DB query). | Edge 🟢 |
| TC-BC-REP-053 | TPL.Output#4 FR-IX-01 ty_le_tra_loi / A4 E7 | Rounding tỷ lệ % — sum ≠ 100% (case 3 entries 33.33%) | cb_nv_tw_01 login. 3 HD cùng lĩnh vực: 1 DA + 1 CHO + 1 CHO. ty_le=33.33% mỗi entry trong theo_linh_vuc[]. | ky=THANG | 1. Chạy BC. | (3) ty_le_tra_loi=33.33% (1/3 ÷ tổng 3 = 33.33). Sum % theo lĩnh vực có thể 99.99% hoặc 100.00% sau làm tròn. Verify hành vi rounding (banker's vs half-up). | Edge 🟡 |
| TC-BC-REP-054 | SCR-IX-01 / A4 E10 | Deep-link URL pre-filled filter | cb_nv_tw_01 login. | URL `/bao-cao?loai=HOI_DAP&ky=THANG` | 1. Paste URL trực tiếp vào browser. | (3) **Behavior verify**: (a) SCR auto-select dropdown HD + kỳ THANG, hoặc (b) bỏ qua param, mở SCR clean. Log nếu surprising. | Edge 🟡 |
| TC-BC-REP-055 | TPL.Output#8 data[] / A4 E11 / SPEC-CLARIFY-BC-10 | Pagination data table — verify hành vi với data lớn | cb_nv_tw_01 login. 250 rows trong BC. | ky=NAM | 1. Chạy BC. | (3) **SPEC-CLARIFY-BC-10**: TPL không nói pagination cho BC table. Verify (a) pagination 20/page (BR-DATA-07), hoặc (b) virtual scroll show all, hoặc (c) load all không pagination. Log finding. | Edge 🟢 |

---

## Tổng kết file 01-TC

- **39 TC**: 11 A Happy + 9 B Negative + 9 C Edge + 3 D Cross filter + 7 E Edge bổ sung A4.
  - Recount: A=11 (001-011), B=9 (020-028), C=9 (040-048), D=3 (060-062), E=7 (049-055). **Tổng 39 TC**.
- **Critical TC (🔴)**: REP-001, 006, 007, 010, 020, 021, 022, 025, 047.
- **Manual injection TC**: REP-023 (timeout), REP-024 (export error), REP-027 (template hỏng).
- **SPEC-CLARIFY ref**: BC-02 (REP-027), BC-06 (REP-042 export empty), BC-10 (REP-055 pagination).
- **A4 inline merged 2026-05-10**: TC-BC-REP-049..055 (was A4 proposal E1, E2, E3, E4, E7, E10, E11).

*Generated 2026-05-10 — Phase A step A3 (BMAD generate-e2e-tests)*
