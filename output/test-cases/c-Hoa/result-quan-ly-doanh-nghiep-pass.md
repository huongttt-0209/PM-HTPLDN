# Test Cases PASS — quan-ly-doanh-nghiep

> **Nguồn**: result-quan-ly-doanh-nghiep-all.md
> **Ngày tổng hợp**: 2026-05-11
> **Phạm vi**: chỉ Result ∈ {PASS, PASS-DEVIATE, PASS-RESOLVED}

## Summary

| File test-case | PASS | PASS-DEVIATE | PASS-RESOLVED | Tổng |
|----------------|-----:|-------------:|--------------:|-----:|
| 01-TC-FR-V.III-01-quan-ly-dn-CRUD | 6 | 0 | 0 | 6 |
| 02-TC-FR-V.III-02-tim-kiem-dn | 5 | 0 | 0 | 5 |
| 03-TC-tab-ho-so-phap-ly-dn | 0 | 0 | 0 | 0 |
| 04-TC-tab-lich-su-ho-tro | 5 | 0 | 0 | 5 |
| 05-TC-tab-ho-so-chi-tra | 2 | 0 | 0 | 2 |
| 06-TC-permission-matrix | 4 | 0 | 0 | 4 |
| **Tổng** | **22** | **0** | **0** | **22** |

---

## 01-TC-FR-V.III-01-quan-ly-dn-CRUD

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\quan-ly-doanh-nghiep\01-TC-FR-V.III-01-quan-ly-dn-CRUD.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\quan-ly-doanh-nghiep\report-01-TC-quan-ly-dn-CRUD\Tcs-report\01-TC-quan-ly-dn-CRUD-execution-report-2026-05-09.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|-----------------------|----------|
| TC-DN-UI-01 | SCR-V.III-01 / Toolbar không có "Thêm mới" + "Import Excel" | Verify toolbar SCR-V.III-01 chỉ có Xuất Excel + Làm mới (KHÔNG có Thêm mới + Import Excel) | qtht_01 đã đăng nhập | URL `/doanh-nghiep/danh-sach` | 1. Mở SCR-V.III-01<br>2. Verify toolbar buttons | **STATE**: Toolbar có 2 nút: "Xuất Excel" + "Làm mới"<br>**UI**: KHÔNG có nút "Thêm mới" (NGUYÊN VĂN bỏ — Thay đổi 2); KHÔNG có nút "Import Excel" (NGUYÊN VĂN bỏ — Thay đổi 1)<br>**REGRESSION**: Nếu vẫn còn UI → SPEC-CLARIFY-DN-01 + log bug | Happy 🔴 | PASS |  |
| TC-DN-UI-04 | SCR-V.III-02 / 4 Tab visibility chế độ chi tiết | Verify SCR-V.III-02 4 tab khi xem chi tiết | qtht_01, DN có ≥1 VV + ≥1 HSPL + ≥1 HSCT | URL `/doanh-nghiep/{id}` | 1. Click mã DN từ list | **TABS (4)**: (1) Thông tin cơ bản (mặc định active), (2) Hồ sơ PL doanh nghiệp, (3) Lịch sử Hỗ trợ, (4) Hồ sơ Chi trả<br>**URL**: `/doanh-nghiep/{id}` (xem) — readonly mode<br>**ACTION-BAR**: 2 nút "Hủy" + "Lưu" — disabled khi chế độ xem | Happy 🔴 | PASS |  |
| TC-DN-001 | FR-V.III-01 / AC2 Edit happy | Edit DN happy path — sửa các trường không bắt buộc | cb_nv_tw_01, DN-TW-001 HOAT_DONG | dien_thoai mới: "0987654321"; ghi_chu: "Cập nhật 2026-05-09" | 1. Login cb_nv_tw_01<br>2. Mở `/doanh-nghiep/DN-TW-001/sua`<br>3. Sửa 2 trường<br>4. Click "Lưu" | **STATE**: Network `PUT /api/v1/doanh-nghieps/{id}` body chứa 2 trường thay đổi<br>**UI**: Toast "Cập nhật thành công"; redirect `/doanh-nghiep/DN-TW-001` (xem)<br>**PERSIST**: Reload — 2 trường đúng giá trị mới<br>**AUDIT_LOG**: Thêm row `entity=DOANH_NGHIEP`, `entity_id={id}`, `hanh_dong=UPDATE`, `gia_tri_cu`/`moi` chứa 2 field changed (BR-DATA-05) | Happy 🔴 | PASS |  |
| TC-DN-002 | FR-V.III-01 / ERR-DN-01 | Edit để Tên DN rỗng → ERR-DN-01 | cb_nv_tw_01, DN-TW-001 | ten_doanh_nghiep: "" | 1. Mở edit<br>2. Xóa Tên DN<br>3. Submit | **UI**: Inline error "Tên doanh nghiệp là bắt buộc" (NGUYÊN VĂN ERR-DN-01)<br>**STATE**: Network response 422 hoặc UI block client-side<br>**PERSIST**: ten_doanh_nghiep cũ giữ nguyên | Negative 🔴 | PASS |  |
| TC-DN-018 | FR-V.III-01 / Mã DN auto-gen readonly | Mã DN format DN-{TINH}-{SEQ} readonly | cb_nv_tw_01, DN-HN-001 | — | 1. Mở edit<br>2. Verify field "Mã DN" | Field readonly (HTML disabled hoặc input readonly); KHÔNG sửa được; format match regex `^DN-[A-Z]{2,5}-\d+$` | Happy 🟡 | PASS |  |
| TC-DN-204 | FR-V.III-01 / Counter so_lan_ho_tro | Hiển thị đúng số VV của DN | qtht_01, DN-TW-001 có 5 VV | — | 1. Mở chi tiết<br>2. Verify trên Tab 3 + cột list | Tổng VV = 5; KPI Tab 3 đồng bộ list cột "Số lần hỗ trợ" | Happy 🟡 | PASS |  |

---

## 02-TC-FR-V.III-02-tim-kiem-dn

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\quan-ly-doanh-nghiep\02-TC-FR-V.III-02-tim-kiem-dn.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\quan-ly-doanh-nghiep\report-02-TC-tim-kiem-dn\Tcs-report\02-TC-tim-kiem-dn-execution-report-2026-05-09.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|-----------------------|----------|
| TC-DN-TK-001 | FR-V.III-02 / AC1 từ khóa tên DN | Tìm theo từ khóa Tên DN | qtht_01, DN "Công ty A", "Công ty B", "Đại lý C" | tu_khoa: "Công ty" | 1. Nhập "Công ty"<br>2. Click "Tìm kiếm" hoặc debounce | **STATE**: Network `GET /api/v1/doanh-nghieps?tu_khoa=Công ty&page=1`<br>**UI**: Table 2 record A + B; pagination total=2 | Happy 🔴 | PASS |  |
| TC-DN-TK-008 | FR-V.III-02 / Search empty | Tu_khoa rỗng → trả full list | qtht_01, ≥5 DN | tu_khoa: "" | 1. Click "Xóa bộ lọc"<br>2. Verify | Table list mặc định 20/trang (BR-DATA-07) | Happy 🟡 | PASS |  |
| TC-DN-TK-103 | FR-V.III-02 / Reset filter | Click "Xóa bộ lọc" → reset all | qtht_01, có filter đang active | — | 1. Set 3 filter<br>2. Click "Xóa bộ lọc" | Filter UI clear; URL bỏ query param; Table list mặc định | Happy 🟡 | PASS |  |
| TC-DN-TK-201 | BR-DATA-07 / Default 20/page | Pagination default 20/trang | qtht_01, ≥21 DN | — | 1. Mở list<br>2. Đếm row | Table 20 row; pagination "1 / N"; Network response `page_size=20` | Happy 🔴 | PASS |  |
| TC-DN-TK-301 | FR-V.III-01 Excel / Happy export | Xuất Excel với filter hiện tại | qtht_01, ≥10 DN match filter | filter quy_mo=NHO | 1. Apply filter<br>2. Click "Xuất Excel"<br>3. Verify file | **STATE**: Network `GET /api/v1/doanh-nghieps/export?quy_mo=NHO`<br>**UI**: Toast "Xuất Excel thành công"; File `.xlsx` auto-download<br>**PERSIST**: Mở file — header chứa các cột: STT/Mã DN/Tên DN/MST/Quy mô/Địa chỉ/Số lần hỗ trợ/Tổng chi phí; Số dòng = số record sau filter | Happy 🔴 | PASS |  |

---

## 04-TC-tab-lich-su-ho-tro

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\quan-ly-doanh-nghiep\04-TC-tab-lich-su-ho-tro.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\quan-ly-doanh-nghiep\report-04-TC-tab-lich-su-ho-tro\Tcs-report\04-TC-tab-lich-su-ho-tro-execution-report-2026-05-09.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|-----------------------|----------|
| TC-LS-UI-01 | SCR-V.III-02 Tab 3 / 3 KPI cards | Verify 3 KPI cards hiển thị | qtht_01, DN-TW-001 có 5 VV (3 HOAN_THANH + 2 DANG_XU_LY), tổng chi phí 100M | URL `/doanh-nghiep/DN-TW-001` Tab 3 | 1. Click Tab 3 | **3 KPI** (per srs:382 "Tab Lịch sử Hỗ trợ hiển thị 3 KPI: Tổng VV, VV hoàn thành, Tổng chi phí"): (1) Tổng VV: 5, (2) VV hoàn thành: 3, (3) Tổng chi phí: 100.000.000 VND format | Happy 🔴 | PASS |  |
| TC-LS-UI-02 | SCR-V.III-02 Tab 3 / DS VV table | Verify table VV liên kết | qtht_01, DN-001 có 5 VV | — | 1. Tab 3<br>2. Verify table cấu trúc | **TABLE COLUMNS** (cross-ref FR-05 SCR-V.I-01): Mã VV (VV-{TINH}-{SEQ}), Tiêu đề, Trạng thái (badge SM-VV), Ngày tạo, Chi phí; KHÔNG có cột Hành động (readonly Tab) | Happy 🔴 | PASS |  |
| TC-LS-001 | FR-V.III-01 / Tổng VV count | Tổng VV = COUNT(vv WHERE doanh_nghiep_id = DN AND is_deleted=0) | qtht_01, DN-TW-001 có 5 VV active + 1 VV soft-deleted | — | 1. Tab 3<br>2. Verify KPI 1 | KPI 1 = 5 (KHÔNG đếm VV is_deleted=1) | Happy 🔴 | PASS |  |
| TC-LS-102 | BR-DATA-07 / Sort default ngày | Sort default updated_at DESC | qtht_01, DN có VV ngày khác nhau | — | 1. Verify sort | VV mới nhất ở đầu | Happy 🟡 | PASS |  |
| TC-LS-103 | FR-V.III-01 / KHÔNG ảnh hưởng cross-DN | DN-001 Tab 3 không hiển thị VV của DN-002 | qtht_01, DN-001 5 VV + DN-002 3 VV | — | 1. Tab 3 DN-001<br>2. Tab 3 DN-002 | DN-001 chỉ thấy 5; DN-002 chỉ thấy 3; KHÔNG cross-leak | Happy 🔴 | PASS |  |

---

## 05-TC-tab-ho-so-chi-tra

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\quan-ly-doanh-nghiep\05-TC-tab-ho-so-chi-tra.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\quan-ly-doanh-nghiep\report-05-TC-tab-ho-so-chi-tra\Tcs-report\05-TC-tab-ho-so-chi-tra-execution-report-2026-05-09.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|-----------------------|----------|
| TC-CT-UI-01 | SCR-V.III-02 Tab 4 / Table HSCT | Verify table HS chi trả Tab 4 | qtht_01, DN-TW-001 có 3 HSCT (DA_DUYET, DANG_XU_LY, YC_BO_SUNG) | URL `/doanh-nghiep/DN-TW-001` Tab 4 | 1. Click Tab 4<br>2. Verify cấu trúc | **TABLE COLUMNS** (cross-ref FR-06): Mã HS chi trả (HSCT-{YYYYMMDD}-{SEQ}), Mã VV liên kết, Số tiền chi trả (VND format), Trạng thái (badge SM-HSCT), Ngày tạo, Ngày cập nhật; KHÔNG có cột Hành động (readonly Tab) | Happy 🔴 | PASS |  |
| TC-CT-UI-02 | SCR-V.III-02 Tab 4 / Empty state | DN không có HSCT → empty state | qtht_01, DN-TW-099 chưa có HSCT | — | 1. Tab 4 | Empty state "Chưa có hồ sơ chi trả nào liên kết" hoặc tương đương; SPEC-CLARIFY-DN-16 nếu SRS không define text | Happy 🟡 | PASS |  |

---

## 06-TC-permission-matrix

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\quan-ly-doanh-nghiep\06-TC-permission-matrix.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\quan-ly-doanh-nghiep\report-06-TC-permission-matrix\Tcs-report\06-TC-permission-matrix-execution-report-2026-05-09.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|-----------------------|----------|
| TC-DN-PERM-UI-01 | BR-AUTH-01 + Sidebar visibility per role | Verify sidebar menu DN visibility per role | 8 role test | — | 1. Login 8 role tuần tự<br>2. Verify sidebar Doanh nghiệp | **qtht_01**: ✅ Doanh nghiệp (R toàn cục)<br>**cb_nv_tw_01/bn_01/dp_01**: ✅ Doanh nghiệp (CRUD scope)<br>**cb_pd_tw_01/bn_01/dp_01**: ✅ Doanh nghiệp (chỉ R*, KHÔNG nút Edit/Delete)<br>**nht_01**: ❌ KHÔNG có sidebar Doanh nghiệp (Permission Matrix DN row "—")<br>**tvv_01/cg_01**: ❌ KHÔNG có sidebar CMS — chỉ chuyên trang xem hồ sơ TVV của mình<br>**dn_01**: ❌ KHÔNG truy cập CMS — chuyên trang riêng (Cổng PLQG) | Happy 🔴 | PASS |  |
| TC-DN-PERM-001 | BR-AUTH-08 / TW ngoại lệ | TW xem được toàn bộ DN | cb_nv_tw_01, mixed data TW/BN/HN/HP | — | 1. Login cb_nv_tw_01<br>2. Mở SCR-V.III-01 | TW thấy toàn bộ DN cả 3 cấp (READ ngoại lệ TW per BR-AUTH-08); CRUD chỉ trên DN do TW tạo | Happy 🔴 | PASS |  |
| TC-DN-PERM-003 | BR-AUTH-08 / ĐP ngang cấp | cb_nv_dp_HN_01 KHÔNG xem được DN-HP (cùng cấp khác đơn vị) | cb_nv_dp_HN_01, DN-HP-001 | — | 1. Direct URL `/doanh-nghiep/DN-HP-001` | API 403; UI redirect hoặc empty list | Negative 🔴 | PASS |  |
| TC-DN-PERM-102 | BR-AUTH-01 / TOTP 2FA happy | Login Tier 1 + OTP 666666 (env test) | qtht_01 | OTP: 666666 | 1. Submit username/password<br>2. OTP screen<br>3. Nhập 666666 | Login PASS; redirect home | Happy 🟡 | PASS |  |

---

## Skipped

Các section sau KHÔNG có TC với Result ∈ {PASS, PASS-DEVIATE, PASS-RESOLVED}:

- **03-TC-tab-ho-so-phap-ly-dn** (0/40 TC PASS — toàn bộ BLOCKED/FAIL/PARTIAL do form thiếu fields + chưa seed HSPL)
