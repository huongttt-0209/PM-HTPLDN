# Test Cases PASS — chuyen-gia-tu-van-vien
> **Nguồn**: result-chuyen-gia-tu-van-vien-all.md
> **Ngày tổng hợp**: 2026-05-11
> **Phạm vi**: chỉ Result ∈ {PASS, PASS-DEVIATE, PASS-RESOLVED}

## Summary

| File test-case | PASS gom được |
|----------------|--------------:|
| 01-TC-FR-IV-01-quan-ly-tvv-CRUD | 12 |
| 02-TC-FR-IV-02-tim-kiem-tvv | 5 |
| 03-TC-FR-IV-03-13-dang-ky-tiep-nhan | 3 |
| 04-TC-FR-IV-04-cap-nhat-nang-luc | 0 |
| 05-TC-FR-IV-05-10-xem-chi-tiet-lich-su | 3 |
| 06-TC-FR-IV-06-tham-dinh | 6 |
| 07-TC-FR-IV-07-phe-duyet | 0 |
| 08-TC-FR-IV-08-cong-khai | 3 |
| 09-TC-FR-IV-09-CROSS-01-danh-gia | 3 |
| 10-TC-FR-IV-11-12-cap-nhat-trang-thai | 8 |
| 11-TC-FR-IV-NEW-01-quan-ly-TC-TV | 2 |
| 12-TC-FR-IV-NEW-02-04-trang-thai-phe-duyet-TC-TV | 6 |
| 13-TC-FR-IV-NHT-01-02-03-quan-ly-NHT | 13 |
| 14-TC-permission-matrix | 7 |
| **Tổng** | **71** |

> Không có TC nào có Result `PASS-DEVIATE` hoặc `PASS-RESOLVED` trong nguồn — toàn bộ 71 TC dưới đây đều Result = `PASS`. Các status custom khác (PASS w/ drift, PASS-IMPLICIT, PASS-VIA, FAIL/*) KHÔNG đưa vào file này.

---

## 01-TC-FR-IV-01-quan-ly-tvv-CRUD

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\CG-TVV\01-TC-FR-IV-01-quan-ly-tvv-CRUD.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\chuyen-gia-tu-van-vien\report-01-TC-FR-IV-01-quan-ly-tvv-CRUD\Tcs-report\01-TC-FR-IV-01-execution-report-2026-05-09.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-TVV-001 | FR-IV-01 / AC1 | CB NV TW xem danh sách TVV thuộc TW | cb_nv_tw_01 đã đăng nhập, ≥5 TVV TW + ≥3 TVV BN + ≥3 TVV ĐP | — | 1. Login cb_nv_tw_01<br>2. Mở SCR-IV-01<br>3. Verify danh sách | Hiển thị ≥5 TVV TW (TW xem được toàn bộ theo BR-AUTH-08 ngoại lệ TW); KHÔNG có toast | Happy | PASS |  |
| TC-TVV-003 | FR-IV-01 / Tab filter | Switch tab "Đang hoạt động" → "Mới đăng ký" filter trang_thai chính xác | qtht_01, mixed state TVV | — | 1. Mở SCR-IV-01 mặc định Đang hoạt động<br>2. Click tab "Mới đăng ký"<br>3. Verify network request | Network call có param trang_thai=MOI_DANG_KY,YEU_CAU_BO_SUNG; table chỉ render record có trạng thái này | Happy | PASS |  |
| TC-TVV-005 | FR-IV-05 / Detail | Click row → mở SCR-IV-03 chi tiết với 5 tab | qtht_01, có TVV TVV-TW-001 HOAT_DONG | — | 1. Mở SCR-IV-01<br>2. Click row TVV-TW-001 hoặc icon "Xem chi tiết"<br>3. Verify 5 tab | URL chuyển /chi-tiet/TVV-TW-001; 5 tab visible; Header badge | Happy | PASS |  |
| TC-TVV-101 | FR-IV-01 / AC2 | Happy path tạo TVV mới đầy đủ field bắt buộc | cb_nv_tw_01, ≥1 Tổ chức TV HOAT_DONG, ≥1 Lĩnh vực PL | Họ tên, CCCD, Email, SĐT, Địa chỉ, Trình độ, Tổ chức chính, Lĩnh vực | 1. Click "+ Thêm tư vấn viên"<br>2. Nhập đủ 5 accordion<br>3. Click "Lưu"<br>4. Verify network + DB | Insert TVV-TW-{seq}, trang_thai='MOI_DANG_KY', version=0; Toast thành công; 201 | Happy | PASS |  |
| TC-TVV-105 | FR-IV-01 / E4 | Tổ chức chính không tồn tại → ERR-TVV-04 | cb_nv_tw_01 | to_chuc_chinh_id: 99999 (FK invalid) | 1. Mở form Thêm<br>2. DevTools tamper to_chuc_chinh_id thành 99999<br>3. Submit | KHÔNG insert; Toast "Tổ chức tư vấn không tồn tại" | Negative | PASS |  |
| TC-TVV-201 | FR-IV-01 / Update | CB NV cùng đơn vị sửa thông tin TVV (chưa duyệt) | cb_nv_tw_01, TVV TVV-TW-005 MOI_DANG_KY | Sửa Họ tên: "Nguyễn Văn B (sửa)" | 1. Mở chi tiết TVV-TW-005<br>2. Click "Sửa hồ sơ"<br>3. Sửa Họ tên<br>4. Lưu | UPDATE OK; Toast "Cập nhật thành công"; version+1 | Happy | PASS |  |
| TC-TVV-202 | FR-IV-01 / BR-FLOW-03 | KHÔNG sửa được TVV đã CHO_KICH_HOAT/HOAT_DONG (sau phê duyệt) | cb_nv_tw_01, TVV TVV-TW-010 HOAT_DONG | — | 1. Mở chi tiết TVV-TW-010<br>2. Tab Hồ sơ — verify | Tab Hồ sơ chỉ hiển thị readonly; KHÔNG có nút "Sửa hồ sơ" | Happy | PASS |  |
| TC-TVV-203 | FR-IV-01 / BR-AUTH-08 | CB NV khác đơn vị KHÔNG sửa được TVV | cb_nv_dp_01 (Sở TP HN), TVV TVV-HP-001 (Sở TP HP) | — | 1. Login cb_nv_dp_01<br>2. Tamper URL chi-tiet/TVV-HP-001<br>3. Cố sửa | API 403 hoặc redirect; KHÔNG có nút Sửa visible | Negative | PASS |  |
| TC-TVV-301 | FR-IV-01 / Delete soft | Xóa mềm TVV chưa có VV | cb_nv_tw_01, TVV TVV-TW-099 MOI_DANG_KY | — | 1. Mở chi tiết TVV-TW-099<br>2. Click icon Xóa<br>3. Modal MD-XOA confirm<br>4. Xác nhận | Soft delete is_deleted=1; Toast "Xóa thành công" | Happy | PASS |  |
| TC-TVV-502 | EDGE-A4-e / Unicode + emoji | Họ tên Unicode tiếng Việt + emoji | cb_nv_tw_01 | ho_ten: "Nguyễn Văn 🇻🇳" | 1. Submit | DB save UTF-8 đầy đủ; UI render đúng emoji + dấu | Edge | PASS |  |
| TC-TVV-507 | EDGE-A4-r / Leap year | Ngày sinh 29/02/2024 (leap year) | cb_nv_tw_01 | ngay_sinh: 2024-02-29 | 1. Submit | DB lưu OK; UI render dd/mm/yyyy "29/02/2024" | Edge | PASS |  |
| TC-TVV-601 | A6-FILL / BR-DATA-03 explicit | Verify common fields (created_at, created_by, updated_at, updated_by) per record | cb_nv_tw_01 vừa tạo TVV-TW-XYZ | — | 1. Tạo TVV mới<br>2. Reload chi tiết<br>3. Verify metadata fields | Record có created_at, created_by, updated_at, updated_by | Happy | PASS |  |

---

## 02-TC-FR-IV-02-tim-kiem-tvv

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\CG-TVV\02-TC-FR-IV-02-tim-kiem-tvv.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\chuyen-gia-tu-van-vien\report-02-TC-tim-kiem-tvv\Tcs-report\02-TC-tim-kiem-tvv-execution-report-2026-05-09-v2.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-TIMKIEM-UI-01 | FR-IV-02 / SCR-IV-01 / UI Filter Bar | Verify thanh filter 6 trường + nút Xuất Excel | qtht_01 đã đăng nhập | URL `/chuyen-gia-tvv/danh-sach` | 1. Mở SCR-IV-01<br>2. Verify từng filter component | 6 filters + Xuất Excel tooltip "Mẫu Phụ lục 1 — QĐ 1322/QĐ-BTP" | Happy | PASS |  |
| TC-TIMKIEM-001 | FR-IV-02 / AC1 | Tìm theo từ khóa Họ tên | qtht_01, có TVV "Nguyễn Văn A" + "Trần Thị B" + "Lê Văn C" | tu_khoa: "Nguyễn" | 1. Mở SCR-IV-01<br>2. Nhập "Nguyễn" vào ô tìm kiếm<br>3. Wait debounce ~300ms | Network call có param tu_khoa; Table chỉ hiển thị "Nguyễn Văn A"; pagination total=1 | Happy | PASS |  |
| TC-TIMKIEM-002 | FR-IV-02 / Search by ma_tvv | Tìm theo mã TVV | qtht_01, TVV-TW-005 tồn tại | tu_khoa: "TVV-TW-005" | 1. Nhập "TVV-TW-005"<br>2. Verify | Table 1 record TVV-TW-005 | Happy | PASS |  |
| TC-TIMKIEM-101 | FR-IV-02 / AC2 | Filter Lĩnh vực + Trạng thái (AND) | qtht_01, ≥3 TVV LV "Lao động" HOAT_DONG + 2 TVV LV "Thuế" TAM_DUNG | linh_vuc_ids: ["Lao động"], trang_thai: ["HOAT_DONG"] | 1. Click filter Lĩnh vực chọn "Lao động"<br>2. Click filter Trạng thái chọn "Đang hoạt động"<br>3. Verify | Network có 2 param; Table 3 record (AND logic) | Happy | PASS |  |
| TC-TIMKIEM-301 | EDGE-A4-m / SQL injection | Tìm với SQL injection payload | qtht_01 | tu_khoa: `'; DROP TABLE TU_VAN_VIEN--` | 1. Nhập payload<br>2. Submit | Sanitize PASS — query parameterized; trả empty | Edge | PASS |  |

---

## 03-TC-FR-IV-03-13-dang-ky-tiep-nhan

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\CG-TVV\03-TC-FR-IV-03-13-dang-ky-tiep-nhan.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\chuyen-gia-tu-van-vien\report-03-TC-FR-IV-03-13-dang-ky-tiep-nhan\Tcs-report\03-TC-FR-IV-03-13-execution-report-2026-05-10.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-DK-011 | FR-IV-03 / loai_tvv=CG bypass thẻ | CG KHÔNG bắt buộc file thẻ | nht_01 | loai_tvv=CG, KHÔNG thẻ HN | 1. Chọn CG<br>2. Submit | TVV insert OK, không validate file_the_hanh_nghe | Edge | PASS |  |
| TC-DK-012 | FR-IV-03 / BR-AUTH-08 don_vi_id auto | Verify don_vi_id KHÔNG sửa được, auto-set NHT.don_vi_id | nht_01 (HN) | DevTools tamper don_vi_id → "Sở TP HP" | 1. Submit với tampered don_vi_id<br>2. Verify | Backend ghi đè don_vi_id = nht_01.don_vi_id; ignore client value | Negative | PASS |  |
| TC-TN-006 | FR-IV-13 / E1 invalid transition | Cố chuyển từ HOAT_DONG → CHO_THAM_DINH (invalid) → ERR-CT-01 | cb_nv_tw_01, TVV-TW-203 HOAT_DONG | DevTools call API trực tiếp transition | 1. Tamper API call FR-IV-13 từ HOAT_DONG | API 400 "Không thể chuyển từ Đang hoạt động sang Chờ thẩm định" | Negative | PASS |  |

---

## 05-TC-FR-IV-05-10-xem-chi-tiet-lich-su

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\CG-TVV\05-TC-FR-IV-05-10-xem-chi-tiet-lich-su.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\chuyen-gia-tu-van-vien\report-05-TC-FR-IV-05-10-xem-chi-tiet-lich-su\Tcs-report\05-TC-FR-IV-05-10-execution-report-2026-05-10.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-CT-004 | FR-IV-05 / E1 | TVV không tồn tại → ERR-HS-01 | qtht_01 | URL `/chuyen-gia-tvv/chi-tiet/99999` | 1. Direct URL ID không tồn tại | API 404 hoặc UI Error "Hồ sơ tư vấn viên không tồn tại" | Negative | PASS |  |
| TC-LS-004 | FR-IV-10 / Empty state | Tab Lịch sử khi TVV chưa có VV | qtht_01, TVV-TW-007 chưa có VV | — | 1. Mở tab Lịch sử | Empty state "Chưa có vụ việc nào"; Stats: —/5 (KHÔNG hiển thị 0/5) | Negative | PASS |  |
| TC-LS-601 | A6-FILL / ERR-LS-01 explicit | Tab Lịch sử cho TVV không tồn tại → ERR-LS-01 | qtht_01 | URL `/chuyen-gia-tvv/chi-tiet/99999` rồi click tab Lịch sử | 1. Direct URL invalid ID<br>2. Click tab Lịch sử | API 404 hoặc UI Error "Tư vấn viên không tồn tại" | Negative | PASS |  |

---

## 06-TC-FR-IV-06-tham-dinh

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\CG-TVV\06-TC-FR-IV-06-tham-dinh.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\chuyen-gia-tu-van-vien\report-06-TC-FR-IV-06-tham-dinh\Tcs-report\06-TC-FR-IV-06-execution-report-2026-05-09.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-TD-001 | FR-IV-06 / AC1 + Trình duyệt | Happy path DAT + Trình duyệt → CHO_PHE_DUYET | cb_nv_tw_01, TVV-TW-400 DANG_THAM_DINH | nhom1=true, nhom2=4.5, nhom3=4.0, nhom4=true, ket_luan=DAT | 1. Nhập 4 nhóm + DAT<br>2. Click "Trình duyệt"<br>3. Modal MD-TRINH-DUYET confirm<br>4. Verify | DANH_GIA insert; TVV → CHO_PHE_DUYET; Toast | Happy | PASS |  |
| TC-TD-002 | FR-IV-06 / E1 | Kết luận DAT khi nhóm Pháp lý FALSE → ERR-TD-02 | cb_nv_tw_01 | nhom1=false, ket_luan=DAT | 1. Nhập nhom1=Không đạt<br>2. Chọn DAT<br>3. Click Trình duyệt | API 400 NGUYÊN VĂN "Không thể kết luận ĐẠT khi nhóm Pháp lý chưa đạt"; KHÔNG insert | Negative | PASS |  |
| TC-TD-006 | FR-IV-06 / KHONG_DAT | KHONG_DAT + lý do → TU_CHOI + thông báo TVV | cb_nv_tw_01, TVV-TW-402 DANG_THAM_DINH | ket_luan=KHONG_DAT, ly_do="Không đáp ứng tiêu chí năng lực" | 1. Click "Từ chối" với lý do<br>2. Verify | TVV → TU_CHOI; Toast; Email | Happy | PASS |  |
| TC-TD-008 | FR-IV-06 / Nhóm 3 N/A | Nhóm 3 Hiệu quả NULL (TVV mới) → DAT vẫn OK | cb_nv_tw_01, TVV-TW-403 mới | nhom1=true, nhom2=4.0, nhom3=NULL, nhom4=true | 1. Check "N/A" nhóm 3<br>2. Trình duyệt | DANH_GIA insert; diem_tong AVG bỏ NULL | Edge | PASS |  |
| TC-TD-009 | FR-IV-06 / Boundary 1.0 | Nhóm 2 boundary low diem=1.0 | cb_nv_tw_01 | nhom2=1.0 | 1. Star-rating tới mức 1<br>2. Submit | Insert OK; diem_tong bao gồm 1.0 | Edge | PASS |  |
| TC-TD-010 | FR-IV-06 / Boundary 5.0 | Nhóm 2 boundary high diem=5.0 | cb_nv_tw_01 | nhom2=5.0 | 1. Star-rating 5<br>2. Submit | Insert OK | Edge | PASS |  |

---

## 08-TC-FR-IV-08-cong-khai

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\CG-TVV\08-TC-FR-IV-08-cong-khai.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\chuyen-gia-tu-van-vien\report-08-TC-FR-IV-08-cong-khai\Tcs-report\08-TC-FR-IV-08-execution-report-2026-05-10.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-CK-001 | FR-IV-08 / AC1 | Happy path công khai TVV HOAT_DONG | cb_nv_tw_01, TVV-TW-600 HOAT_DONG, MailHog UP | mo_ta_cong_khai: "TVV chuyên môn Lao động 10+ năm" + 1 file PDF 5MB | 1. Click Công khai → Modal<br>2. Nhập mô tả + upload file<br>3. Confirm | TVV cong_khai=1; API outbound Cổng; Toast | Happy | PASS |  |
| TC-CK-002 | FR-IV-08 / TVV CHO_KICH_HOAT công khai (mới v3.1) | TVV vừa được phê duyệt CHO_KICH_HOAT vẫn được công khai | cb_nv_tw_01, TVV-TW-601 CHO_KICH_HOAT | mo_ta_cong_khai | 1. Click Công khai TVV CHO_KICH_HOAT<br>2. Verify | PASS — v3.1 nới BR-PUBLIC-01 | Edge | PASS |  |
| TC-CK-005 | FR-IV-08 / Hủy công khai | Hủy công khai → giữ lại mô tả + file để tái công khai | cb_nv_tw_01, TVV-TW-600 cong_khai=1 | — | 1. Click "Hủy công khai" → Modal MD-HUY-CONG-KHAI<br>2. Confirm | cong_khai=0; mô tả + file GIỮ LẠI; API outbound DELETE Cổng | Happy | PASS |  |

---

## 09-TC-FR-IV-09-CROSS-01-danh-gia

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\CG-TVV\09-TC-FR-IV-09-CROSS-01-danh-gia.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\chuyen-gia-tu-van-vien\report-09-TC-FR-IV-09-CROSS-01-danh-gia\Tcs-report\09-TC-FR-IV-09-CROSS-01-execution-report-2026-05-10.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-DG-002 | FR-IV-09 / E1 | Điểm ngoài thang 1-5 → ERR-DG-01 | dn_001 (DevTools tamper) | diem_cm=6.0 | 1. DevTools tamper request<br>2. Submit | API 400 "Điểm đánh giá phải từ 1 đến 5"; KHÔNG insert | Negative | PASS |  |
| TC-DG-006 | FR-IV-09 / Boundary 1.0 | Điểm boundary low 1.0 | dn_001 | diem_cm=1.0, diem_td=1.0, diem_th=1.0 | 1. Submit | Insert OK; diem_trung_binh=1.0 | Edge | PASS |  |
| TC-CROSS-002 | FR-IV-CROSS-01 / AC2 chưa có đánh giá | TVV chưa có đánh giá → "—/5" KHÔNG hiển thị 0 | qtht_01, TVV-TW-701 chưa có DANH_GIA_SAU_VU_VIEC | — | 1. Mở chi tiết TVV-TW-701<br>2. Stats card | UI hiển thị "—/5" (NGUYÊN VĂN INF-TVV-DG-01); KHÔNG hiển thị "0/5" | Negative | PASS |  |

---

## 10-TC-FR-IV-11-12-cap-nhat-trang-thai

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\CG-TVV\10-TC-FR-IV-11-12-cap-nhat-trang-thai.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\chuyen-gia-tu-van-vien\report-10-TC-FR-IV-11-12-cap-nhat-trang-thai\Tcs-report\10-TC-FR-IV-11-12-execution-report-2026-05-10.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-CNTT-101 | FR-IV-12 / HOAT_DONG → TAM_DUNG | Tạm dừng TVV HOAT_DONG | cb_nv_tw_01, TVV-TW-810 HOAT_DONG | ly_do: "TVV xin nghỉ tạm thời 3 tháng" | 1. Header "Tạm dừng" → MD-TAM-DUNG<br>2. Nhập lý do<br>3. Confirm | TVV → TAM_DUNG, version+1; AUDIT_LOG | Happy | PASS |  |
| TC-CNTT-102 | FR-IV-12 / TAM_DUNG → HOAT_DONG | Kích hoạt lại TVV TAM_DUNG | cb_nv_tw_01, TVV-TW-811 TAM_DUNG | ly_do: "TVV trở lại làm việc" | 1. Header "Kích hoạt lại"<br>2. Confirm | TVV → HOAT_DONG; AUDIT_LOG | Happy | PASS |  |
| TC-CNTT-103 | FR-IV-12 / HOAT_DONG → VO_HIEU_HOA + GUARD VV+HĐ | TVV không có VV + HĐ → vô hiệu hóa OK | cb_nv_tw_01, TVV-TW-812 HOAT_DONG, KHÔNG có VV + HOI_DAP DANG_XU_LY/CHO_PHE_DUYET | ly_do: "Hết hạn thẻ" | 1. Header "Vô hiệu hóa" → MD-VO-HIEU-HOA<br>2. Confirm | TVV → VO_HIEU_HOA; nếu cong_khai=1 → API DELETE Cổng | Happy | PASS |  |
| TC-CNTT-104 | FR-IV-12 / E2 ERR-TT-02 GUARD VV | TVV có 1 VV DANG_XU_LY → reject | cb_nv_tw_01, TVV-TW-813 HOAT_DONG có 1 VU_VIEC DANG_XU_LY | — | 1. Click Vô hiệu hóa | API 400 "Tư vấn viên đang có 1 vụ việc và 0 hỏi đáp..." | Negative | PASS |  |
| TC-CNTT-105 | FR-IV-12 / GUARD HOI_DAP (mới v3.1) | TVV có 1 HỎI ĐÁP DANG_XU_LY → reject | cb_nv_tw_01, TVV-TW-814 HOAT_DONG có 0 VV + 1 HOI_DAP DANG_XU_LY | — | 1. Click Vô hiệu hóa | API 400 "Tư vấn viên đang có 0 vụ việc và 1 hỏi đáp..."; v3.1 guard HOI_DAP | Negative | PASS |  |
| TC-CNTT-108 | FR-IV-12 / E1 ERR-TT-01 | Transition không hợp lệ HOAT_DONG → MOI_DANG_KY | cb_nv_tw_01, TVV-TW-817 HOAT_DONG | DevTools call API trang_thai_moi=MOI_DANG_KY | 1. Tamper API | API 400 "Không thể chuyển từ Đang hoạt động sang Mới đăng ký" | Negative | PASS |  |
| TC-CNTT-109 | FR-IV-12 / E3 ERR-TT-03 | Cập nhật trạng thái thiếu lý do → ERR-TT-03 | cb_nv_tw_01 | ly_do: "" | 1. Modal MD-TAM-DUNG submit không lý do | "Lý do thay đổi là bắt buộc (≥ 10 ký tự)" | Negative | PASS |  |
| TC-CNTT-110 | FR-IV-12 / Lý do <10 ký | Lý do <10 ký → ERR-TT-03 | cb_nv_tw_01 | ly_do: "ngan" | 1. Submit | ERR-TT-03 (NGUYÊN VĂN) | Negative | PASS |  |

---

## 11-TC-FR-IV-NEW-01-quan-ly-TC-TV

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\CG-TVV\11-TC-FR-IV-NEW-01-quan-ly-TC-TV.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\chuyen-gia-tu-van-vien\report-11-TC-NEW-01-quan-ly-TC-TV\Tcs-report\11-TC-NEW-01-quan-ly-TC-TV-execution-report-2026-05-09-v2.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-TC-101 | FR-IV-NEW-01 / List filter loại hình | Filter Loại hình "CONG_TY_LUAT" | qtht_01, mixed loại hình | loai_hinh=CONG_TY_LUAT | 1. Filter loại hình | Table chỉ TC TV CONG_TY_LUAT | Happy | PASS |  |
| TC-TC-401 | FR-IV-NEW-01 / Export PL2 BTP | Xuất Excel theo Phụ lục 2 — QĐ 1322/QĐ-BTP (12 cột) | qtht_01, ≥10 TC TV HOAT_DONG | filter: Loại hình CONG_TY_LUAT | 1. Click "Xuất Excel"<br>2. Verify file | API export-pl2 200; File Excel 12 cột PL2 | Happy | PASS |  |

---

## 12-TC-FR-IV-NEW-02-04-trang-thai-phe-duyet-TC-TV

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\CG-TVV\12-TC-FR-IV-NEW-02-04-trang-thai-phe-duyet-TC-TV.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\chuyen-gia-tu-van-vien\report-12-TC-NEW-02-04-trang-thai-phe-duyet-TC-TV\Tcs-report\12-TC-NEW-02-04-execution-report-2026-05-09-v3.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-TCPD-001 | FR-IV-NEW-01 / MOI_DANG_KY → CHO_PHE_DUYET | Trình duyệt TC TV | cb_nv_tw_01, TC-TW-100 MOI_DANG_KY | — | 1. Click "Trình duyệt" → MD-TRINH-DUYET<br>2. Confirm | TC TV → CHO_PHE_DUYET; AUDIT_LOG; Notification | Happy | PASS |  |
| TC-TCPD-002 | FR-IV-NEW-02 / HOAT_DONG → TAM_DUNG | Tạm dừng TC TV | cb_nv_tw_01, TC-TW-101 HOAT_DONG | ly_do: "Tạm dừng do tổ chức xin nghỉ" | 1. Click "Tạm dừng"<br>2. Nhập lý do<br>3. Confirm | TC TV → TAM_DUNG; AUDIT_LOG; ERR-TT-TC-03 nếu thiếu lý do | Happy | PASS |  |
| TC-TCPD-003 | FR-IV-NEW-02 / HOAT_DONG → VO_HIEU_HOA + GUARD | TC TV không có TVV liên kết → vô hiệu hóa OK | cb_nv_tw_01, TC-TW-102 HOAT_DONG, TVV_TO_CHUC count HOAT_DONG = 0 | ly_do: "Hết hạn hoạt động" | 1. Click Vô hiệu hóa<br>2. Confirm | TC TV → VO_HIEU_HOA; nếu cong_khai=1 → API DELETE Cổng | Happy | PASS |  |
| TC-TCPD-005 | FR-IV-NEW-02 / VO_HIEU_HOA → HOAT_DONG | Khôi phục TC TV | cb_nv_tw_01, TC-TW-104 VO_HIEU_HOA | — | 1. Click "Khôi phục" | TC TV → HOAT_DONG; AUDIT_LOG | Happy | PASS |  |
| TC-TCPD-101 | FR-IV-NEW-04 / AC1+AC2 Happy | Phê duyệt TC TV cùng cấp | cb_pd_tw_01, TC-TW-100 CHO_PHE_DUYET | so_quyet_dinh: "QĐ-002/QĐ-TW", y_kien: "Đạt" | 1. Mở chi tiết TC-TW-100<br>2. Click Phê duyệt → MD-PHE-DUYET<br>3. Nhập Số QĐ<br>4. Confirm | TC TV → HOAT_DONG, ngay_cong_nhan; AUDIT_LOG; Notification | Happy | PASS |  |
| TC-TCPD-603 | A6-FILL / SM-TCTV TAM_DUNG → HOAT_DONG explicit | Kích hoạt lại TC TV TAM_DUNG | cb_nv_tw_01, TC-TW-112 TAM_DUNG | — | 1. Click "Kích hoạt lại" | TC TV → HOAT_DONG; AUDIT_LOG | Happy | PASS |  |

---

## 13-TC-FR-IV-NHT-01-02-03-quan-ly-NHT

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\CG-TVV\13-TC-FR-IV-NHT-01-02-03-quan-ly-NHT.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\chuyen-gia-tu-van-vien\report-13-TC-NHT-01-02-03-quan-ly-NHT\Tcs-report\13-TC-NHT-execution-report-2026-05-09-v3.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-NHT-UI-01 | FR-IV-NHT-01 / SCR-IV-NHT-01 / UI DS | Verify SCR-IV-NHT-01 DS Người hỗ trợ pháp lý (3 tab + 4 filter + table) | qtht_01 | URL `/chuyen-gia-tvv/nguoi-ho-tro` | 1. Mở list NHT | 3 tabs (Đang HĐ/Tạm dừng/Vô hiệu hóa), 4 filters, table columns | Happy | PASS |  |
| TC-NHT-UI-03 | FR-IV-NHT-03 / SCR-IV-NHT-03 / UI 3 tab | Verify SCR-IV-NHT-03 chi tiết NHT 3 tab | qtht_01, NHT-TW-001 HOAT_DONG có ≥2 VV | — | 1. Mở chi tiết | 3 tabs: Thông tin / Bồi dưỡng / Vụ việc đã hỗ trợ | Happy | PASS |  |
| TC-NHT-001 | FR-IV-NHT-01 / AC1 | Happy path tạo NHT mới | cb_nv_tw_01, ≥1 lĩnh vực PL, MailHog UP | ho_ten, email, username, don_vi_id, linh_vuc | 1. Click + Thêm<br>2. Nhập 5 fields<br>3. Lưu | TAI_KHOAN insert; NGUOI_HO_TRO insert; Mail kích hoạt | Happy | PASS |  |
| TC-NHT-003 | FR-IV-NHT-01 / E1 ERR-NHT-01 | Email/username trùng → ERR-NHT-01 | cb_nv_tw_01, đã có NHT email "b@example.com" | email trùng | 1. Submit | "Email hoặc tên đăng nhập đã được sử dụng" | Negative | PASS |  |
| TC-NHT-004 | FR-IV-NHT-01 / E2 ERR-NHT-02 | CB NV ĐP cố tạo NHT cho đơn vị TW → ERR-NHT-02 | cb_nv_dp_01 (HN), DevTools tamper don_vi_id=TW | — | 1. Tamper don_vi_id<br>2. Submit | "Bạn không có quyền tạo NHT cho đơn vị này" | Negative | PASS |  |
| TC-NHT-005 | FR-IV-NHT-01 / E3 ERR-NHT-03 | Thiếu lĩnh vực → ERR-NHT-03 | cb_nv_tw_01 | linh_vuc_ids: [] | 1. Submit | "Vui lòng chọn ít nhất 1 lĩnh vực chuyên môn" | Negative | PASS |  |
| TC-NHT-006 | FR-IV-NHT-01 / Username 4-50 ký | Username boundary 3 ký → reject | cb_nv_tw_01 | username: "abc" (3 ký) | 1. Submit | API 400 "Tên đăng nhập 4-50 ký tự" | Negative | PASS |  |
| TC-NHT-103 | FR-IV-NHT-01 / SM-NHT HOAT_DONG → TAM_DUNG | Tạm dừng NHT | qtht_01, NHT-TW-005 HOAT_DONG | — | 1. Action Tạm dừng + ly_do | NHT → TAM_DUNG; AUDIT_LOG | Happy | PASS |  |
| TC-NHT-104 | FR-IV-NHT-01 / SM-NHT TAM_DUNG → HOAT_DONG | Kích hoạt lại NHT | qtht_01, NHT-TW-006 TAM_DUNG | — | 1. Action Kích hoạt lại | NHT → HOAT_DONG | Happy | PASS |  |
| TC-NHT-201 | FR-IV-NHT-02 / AC1 | Tìm NHT theo lĩnh vực | cb_nv_tw_01, NHT đa lĩnh vực | linh_vuc_ids: ["Lao động"] | 1. Filter LV<br>2. Verify | Table chỉ NHT có lĩnh vực Lao động | Happy | PASS |  |
| TC-NHT-302 | FR-IV-NHT-03 / AC2 CB NV xem NHT cùng đơn vị | cb_nv_dp_01 (HN) xem NHT thuộc HN | cb_nv_dp_01, NHT-HN-001 | — | 1. Mở chi tiết NHT-HN-001 | 3 tab full data | Happy | PASS |  |
| TC-NHT-303 | FR-IV-NHT-03 / BR-AUTH-08 | CB NV ĐP HN cố xem NHT TW → reject | cb_nv_dp_01, NHT-TW-001 | — | 1. Direct URL chi-tiet/NHT-TW-001 | API 403 hoặc redirect | Negative | PASS |  |
| TC-NHT-501 | A6-FILL / SM-NHT VO_HIEU_HOA → HOAT_DONG | Khôi phục NHT VO_HIEU_HOA (admin) | qtht_01, NHT-TW-007 VO_HIEU_HOA | — | 1. Action "Khôi phục" (admin only) | NHT → HOAT_DONG; TK → HOAT_DONG; AUDIT_LOG | Happy | PASS |  |

---

## 14-TC-permission-matrix

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\CG-TVV\14-TC-permission-matrix.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\chuyen-gia-tu-van-vien\report-14-TC-permission-matrix\Tcs-report\14-TC-permission-matrix-execution-report-2026-05-10.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-PERM-001 | BR-AUTH-08 / TW ngoại lệ | TW xem được toàn bộ data | cb_nv_tw_01, mixed data TW/BN/HN/HP | — | 1. Login cb_nv_tw_01<br>2. Mở SCR-IV-01 + SCR-IV-NEW-01 + SCR-IV-NHT-01 | TW thấy toàn bộ TVV + TC TV + NHT cả 3 cấp | Happy | PASS |  |
| TC-PERM-003 | BR-AUTH-08 / ĐP ngang cấp | cb_nv_dp_HN_01 KHÔNG xem được data HP (cùng cấp khác đơn vị) | cb_nv_dp_HN_01, TVV-HP-001 | — | 1. Direct URL chi-tiet/TVV-HP-001 | API 403; UI redirect hoặc empty | Negative | PASS |  |
| TC-PERM-004 | BR-AUTH-08 / IDOR cross-tenant | IDOR: cb_nv_dp_HN_01 cố sửa TVV-HP-001 qua DevTools | cb_nv_dp_HN_01 | — | 1. DevTools call PUT /api/v1/tu-van-vien/{TVV-HP-001-id} | API 403; AUDIT_LOG ghi attempt; KHÔNG cập nhật | Negative | PASS |  |
| TC-PERM-101 | BR-AUTH-05 / TVV cùng cấp pass | cb_pd_tw_01 duyệt TVV cb_nv_tw_01 thẩm định | cb_pd_tw_01, TVV-TW-CHO_PHE_DUYET | — | 1. Phê duyệt | PASS — chuyển CHO_KICH_HOAT | Happy | PASS |  |
| TC-PERM-201 | BR-AUTH-01 / Unauthorized | Truy cập SCR-IV-01 không login → redirect login | — | URL `/chuyen-gia-tvv/danh-sach` | 1. Direct URL không session | Redirect /login; URL gốc lưu để callback | Negative | PASS |  |
| TC-PERM-202 | BR-AUTH-01 / TOTP 2FA | Login Tier 1 + OTP qua email (mặc định 666666 trong môi trường test) | qtht_01 | OTP: 666666 | 1. Submit username/password<br>2. OTP screen<br>3. Nhập 666666 | Login PASS; redirect home | Happy | PASS |  |
| TC-PERM-501 | EDGE-A4-aa / IDOR direct API | IDOR trực tiếp API KHÔNG qua UI | cb_nv_dp_HN_01 | DevTools PUT cross-tenant TVV-HP-001 | 1. Capture token<br>2. PUT trực tiếp body | API 403 ERR-AUTH-08 (NGUYÊN VĂN); AUDIT_LOG ghi attempt | Edge | PASS |  |

---

## Skipped

Các section dưới đây KHÔNG có TC nào có Result ∈ {PASS, PASS-DEVIATE, PASS-RESOLVED} nên không liệt kê bảng chi tiết:

- **04-TC-FR-IV-04-cap-nhat-nang-luc** — toàn bộ TC là DEFERRED / FAIL / N/A / PASS w/ drift; 0 PASS.
- **07-TC-FR-IV-07-phe-duyet** — toàn bộ TC là DEFERRED / FAIL / PASS w/ drift; 0 PASS.
