# Test Cases — FR-XI-06 (UC166): Lập BC kết quả thực hiện CT

> **SRS Ref**: FR-XI-06, SCR-XI-01 Drill-down (form 21a/21b editable), Entity BAO_CAO_CT_HTPL
> **Ngày tạo**: 2026-05-10
> **Đặc thù**: CB NV nhập số liệu vào biểu mẫu TT17/2025 21a (hỗ trợ pháp lý) hoặc 21b (chương trình HTPL) tùy `bieu_mau_su_dung` của đợt. Hệ thống gợi ý số liệu từ Vụ việc/Chi trả/Đánh giá nếu có. CB NV chỉnh sửa + nhận xét + lưu nháp + trình duyệt.
> **Scope**: Form lập BC khi đợt ở DANG_LAP_BC + BC ở DU_THAO. KHÔNG gồm trình duyệt (xem `03-TC-trinh-phe-duyet-bc.md`).

---

## Quy ước

- **Priority**: 🔴 P0 · 🟡 P1 · 🟢 P2
- **TraceID**: `FR-XI-06 / {section}` — truy vết SRS
- **Pre-conditions mặc định**: User đã đăng nhập, có quyền "Lập BC kết quả CT", đợt BC ở DANG_LAP_BC, BAO_CAO_CT_HTPL đã được tạo (UC166 step 5 đã chạy qua UC165→UC166 transition).

---

## Trường input FR-XI-06

| # | Field | Bắt buộc | Kiểu | Ràng buộc |
|---|-------|----------|------|-----------|
| 1 | chuong_trinh_id | Y | identifier | FK CHUONG_TRINH_HTPL — Context (read-only) |
| 2 | ky_bao_cao | Y | text | SO_BO_6_THANG / SO_BO_NAM / TRON_NAM — Context (read-only) |
| 3 | tu_ngay | Y | date | Context (read-only) |
| 4 | den_ngay | Y | date | Context (read-only) |
| 5 | so_lieu | Y | structured (JSON cột 21a/21b) | Số liệu theo cột; gợi ý từ HT |
| 6 | nhan_xet | N | text (long) | Max 5000 ký tự |

---

## A. Lập BC — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BC-001 | FR-XI-06 / Processing step 4-5 | Lập BC happy path nhập tay | cb_nv_tw_01 login. Đợt DOT-CTW01-001 DANG_LAP_BC, biểu mẫu MAU_21A. | so_lieu (cột 21a): 5 dòng dữ liệu cơ bản; nhan_xet="Hoàn thành tốt 80% mục tiêu Q1." | 1. Drill-down đợt. 2. Nhập số liệu vào editable table 21a (5 cột × 5 dòng). 3. Nhập nhận xét. 4. Click [Lưu nháp]. | (4) PUT `/api/v1/bao-cao-ct/{id}` 200. (4) Toast "Lưu nháp thành công". (4) `so_lieu_tong_hop` = JSON serialize đúng cấu trúc 21a. (4) Reload page → render lại đúng dữ liệu. (4) `trang_thai`=DU_THAO. Audit log UPDATE (BR-DATA-05). | Happy 🔴 |
| TC-BC-002 | FR-XI-06 / Processing step 2 — biểu mẫu 21b | Lập BC với biểu mẫu 21b | cb_nv_dp_01 login. Đợt DOT-CDP01-002 DANG_LAP_BC, biểu mẫu MAU_21B. | so_lieu (cột 21b CT-HTPL): 4 cột × 3 dòng | 1. Drill-down. 2. MCP `evaluate_script` verify chỉ render bảng 21b (KHÔNG có 21a). 3. Nhập + Lưu nháp. | (2) Chỉ form 21b render. (3) Lưu thành công, JSON đúng schema 21b. | Happy 🟡 |
| TC-BC-003 | FR-XI-06 / Processing step 2 — biểu mẫu CA_HAI | Lập BC với CA_HAI (cả 21a và 21b) | cb_nv_tw_01 login. Đợt DOT-CTW01-003 DANG_LAP_BC, biểu mẫu CA_HAI. | so_lieu cả 21a+21b | 1. Drill-down. 2. Verify cả 2 form render. 3. Nhập đủ + Lưu. | (2) Render CẢ 2 form 21a + 21b. (3) `so_lieu_tong_hop` JSON chứa cả 2 schema. | Happy 🟡 |
| TC-BC-004 | FR-XI-06 / Inputs#6 | nhan_xet optional — bỏ trống vẫn lưu | cb_nv_tw_01 login. Đợt DOT-CTW01-004 DANG_LAP_BC. | so_lieu đủ; nhan_xet="" | 1. Nhập số liệu, bỏ trống nhận xét. 2. Lưu nháp. | (2) PASS — nhan_xet là optional. Lưu thành công, `nhan_xet`=null. | Happy 🟢 |
| TC-BC-005 | FR-XI-06 / Processing step 3 — gợi ý số liệu (SPEC-CLARIFY-CT-GD2-03) | Gợi ý số liệu auto từ hệ thống | cb_nv_tw_01 login. Đợt DOT-CTW01-005 DANG_LAP_BC. **Pre-seed cross-module:** ≥3 vụ việc HOAN_THANH cùng kỳ + ≥2 chi trả DA_DUYET (cascade W3.2 + W4.2). | — | 1. Drill-down. 2. Click [Gợi ý số liệu]. (Hoặc auto-fill khi mở form lần đầu — tùy UI implementation) | (2) ⚠️ SPEC-CLARIFY-CT-GD2-03: SRS dòng 728 nói "Gợi ý số liệu từ dữ liệu hệ thống (đếm VV, tổng chi phí...) nếu có" nhưng KHÔNG mapping cột nào lấy từ entity nào. Expected: số liệu auto-fill các cột tương ứng (vd cột "Số DN tham gia tư vấn" = COUNT VV unique DN; cột "Tổng chi phí" = SUM Chi trả). Nếu mapping rỗng → log GAP. | Edge 🟡 |

---

## B. Lập BC — NEGATIVE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BC-010 | FR-XI-06 / E1 ERR-XI-06-01 | Thiếu số liệu bắt buộc khi Trình | cb_nv_tw_01 login. Đợt DOT-CTW01-010 DANG_LAP_BC, BC `so_lieu`=null. | so_lieu rỗng | 1. Drill-down (số liệu rỗng). 2. Click [Trình duyệt KQ]. | (2) Reject với **"Vui lòng nhập đầy đủ số liệu bắt buộc"** (ERR-XI-06-01). KHÔNG transition đợt sang CHO_DUYET_KQ. Form giữ. | Negative 🔴 |
| TC-BC-011 | SM-BC sub / BC ≠ DU_THAO/TU_CHOI | Sửa BC khi BC ở CHO_PHE_DUYET | cb_nv_tw_01 login. Đợt DOT-CTW01-011 CHO_DUYET_KQ, BC ở CHO_PHE_DUYET. | — | 1. Drill-down. 2. Verify form 21a/21b. | (2) Form **read-only** (KHÔNG editable) vì BC đang chờ duyệt. Nút [Lưu nháp] ẩn. Nút [Trình duyệt KQ] cũng ẩn (đã trình rồi). | Negative 🔴 |
| TC-BC-012 | FR-XI-06 / Inputs#6 — nhan_xet > 5000 ký tự | Nhập nhận xét vượt 5000 ký tự | cb_nv_tw_01 login. Đợt DOT-CTW01-012 DANG_LAP_BC. | nhan_xet=5001 ký tự (1 ký tự vượt giới hạn) | 1. Nhập 5001 ký tự vào nhận xét. 2. Lưu. | (1) Counter cảnh báo "5001/5000". (2) Backend reject 400 hoặc input bị truncate. KHÔNG persist >5000 ký tự. | Negative 🟡 |

---

## C. Lập BC — EDGE (A4 merged)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BC-013 | BR-EC-13 / XSS sanitize nhan_xet (A4) | Inject XSS vào nhận xét | cb_nv_tw_01 login. Đợt DOT-CTW01-013 DANG_LAP_BC. | nhan_xet=`<script>alert('xss')</script>` + 100 ký tự normal | 1. Nhập payload XSS vào nhận xét. 2. Lưu. 3. Reload page. | (2) Backend chấp nhận text raw (sanitize ở render). (3) Render: HTML escape, hiển thị literal `<script>alert('xss')</script>` KHÔNG execute. KHÔNG popup XSS. | Edge 🔴 |
| TC-BC-014 | BR-EC-01 / Concurrent edit (A4) | 2 tab cùng sửa BC | cb_nv_tw_01 login 2 tab. Đợt DOT-CTW01-014 DANG_LAP_BC. | Tab1: cell so_lieu="100"; Tab2: cell so_lieu="200" | 1. Tab1 sửa cell → Lưu (delay backend). 2. Tab2 sửa cell → Lưu trước khi Tab1 response. | (2) 1 PUT thành công, 1 reject với optimistic-lock ERR-SYS-02 (BR-EC-01). UI tab thua → toast error + reload latest. PERSIST: 1 record với value thắng. | Edge 🟡 |
| TC-BC-015 | FR-XI-06 / Inputs#5 — boundary số liệu lớn (A4) | Số liệu cell vượt giới hạn int | cb_nv_tw_01 login. Đợt DOT-CTW01-015 DANG_LAP_BC. | so_lieu cell = 9999999999 (10 chữ số, vượt int32 max) | 1. Nhập số 10 chữ số vào cell. 2. Lưu. | (2) Backend reject hoặc cell convert sang bigint/text. KHÔNG silent overflow → hiển thị giá trị âm sai. | Edge 🟡 |
| TC-BC-016 | FR-XI-06 / Auto-save (A4) | Auto-save khi điền form lâu (nếu có) | cb_nv_tw_01 login. Đợt DOT-CTW01-016 DANG_LAP_BC. | so_lieu phần lớn cell | 1. Nhập 50% cell. 2. Đợi 30s không click Lưu. 3. Reload page. | (3) ⚠️ SRS không nói explicit auto-save. Expected: dữ liệu mất nếu không Lưu nháp HOẶC còn nếu UI có auto-save. Log behavior thực tế. Nếu mất → cảnh báo user "Cần Lưu nháp định kỳ". | Edge 🟢 |

---

## Tổng kết file 02-TC

- **12 TC**: 5 Happy + 3 Negative + 4 Edge (A3 base 8 + A4 merged 4)
- **Critical TC (🔴)**: 001, 010, 011, 013
- **A4 merged 2026-05-10**: TC-BC-013..016
- **SPEC-CLARIFY**: CT-GD2-03 (TC-BC-005 mapping gợi ý số liệu)

*Generated 2026-05-10 — Phase A step A3 + A4 inline merge*
