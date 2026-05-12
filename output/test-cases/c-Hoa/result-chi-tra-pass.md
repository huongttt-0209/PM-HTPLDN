# Test Cases PASS — chi-tra

> **Nguồn**: result-chi-tra-all.md
> **Ngày tổng hợp**: 2026-05-11
> **Phạm vi**: chỉ Result ∈ {PASS, PASS-DEVIATE, PASS-RESOLVED}

## Summary

| File test-case | PASS |
|----------------|------|
| 01-TC-FR-V.II-02-quan-ly-HS-de-nghi | 7 |
| 02-TC-FR-V.II-03-kiem-tra-HS | 1 |
| 03-TC-FR-V.II-05-danh-gia-tieu-chi | 1 |
| 04-TC-FR-V.II-09-tham-dinh | 1 |
| 05-TC-FR-V.II-11-12-trinh-PD-phe-duyet | 7 |
| 06-TC-FR-V.II-13-cap-nhat-thanh-toan | 5 |
| 10-TC-permission-matrix | 7 |
| **Tổng** | **29** |

> Ghi chú: source file không có TC nào ở trạng thái PASS-DEVIATE hoặc PASS-RESOLVED — tất cả 29 entry đều PASS. Các section 07/08/09 không có TC PASS nào → liệt kê tại `## Skipped`.

---

## 01-TC-FR-V.II-02-quan-ly-HS-de-nghi

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\chi-tra\01-TC-FR-V.II-02-quan-ly-HS-de-nghi.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\chi-tra\report-01-TC-FR-V.II-02-quan-ly-HS-de-nghi\Tcs-report\TCs-result.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-CT-LIST-001 | AC#1, BR-DATA-07 |  | Login `cb_nv_tw_01` |  | 1. Vào /chi-tra/danh-sach 2. Verify 5 tab + count 3. Verify 9 cột | DS hiện đầy đủ 5 tab "Tất cả / Chờ xử lý (CHO_TIEP_NHAN+DANG_KIEM_TRA+YEU_CAU_BO_SUNG) / Đang đánh giá (DANG_DANH_GIA+DANG_THAM_DINH) / Chờ PD (CHO_PHE_DUYET) / Đã xử lý (DA_DUYET+DA_THANH_TOAN+TU_CHOI+HUY)". 9 cột (Mã HS / Tên DN / Quy mô / Số tiền đề nghị / Số tiền duyệt / Trạng thái / SLA / Ngày nộp / Hành động). Mặc định 20 dòng/trang | P0 | PASS |  |
| TC-CT-LIST-002 | AC#1 |  | Login `cb_nv_tw_01` |  | 1. Click tab "Chờ xử lý" 2. Verify count tab vs số dòng | Tab filter đúng 3 trạng thái CHO_TIEP_NHAN+DANG_KIEM_TRA+YEU_CAU_BO_SUNG. Số đếm tab = số dòng | P0 | PASS |  |
| TC-CT-LIST-003 | AC#3 |  | Login `cb_nv_tw_01` |  | 1. Filter "Quy mô DN" = "Siêu nhỏ" 2. Filter "Trạng thái" = "Đang kiểm tra" 3. Range ngày 01/01/2026 - 31/12/2026 4. Click "Tìm kiếm" | DS lọc AND logic — chỉ HS quy mô SIEU_NHO + trạng thái DANG_KIEM_TRA + ngày nộp trong range. Combobox quy mô hiển thị nhãn Việt "Siêu nhỏ/Nhỏ/Vừa" (giá trị nội bộ SIEU_NHO/NHO/VUA — srs-fr-06:916) | P1 | PASS |  |
| TC-CT-LIST-004 | AC#3 |  | Login `cb_nv_tw_01` |  | 1. Nhập keyword "test_DN" trong ô tìm kiếm 2. Click Tìm kiếm | DS filter theo tên DN OR mã HS chứa keyword | P1 | PASS |  |
| TC-CT-LIST-007 | AC#1, srs-fr-06:928 |  | Login `cb_nv_tw_01` + HS X ở CHO_TIEP_NHAN |  | 1. Click hàng HS X 2. Verify nút Hành động hiện | Cột Hành động hiện nút "Tiếp nhận" cho HS CHO_TIEP_NHAN. Click → mở SCR-V.II-02 chi tiết tại section tương ứng | P0 | PASS |  |
| TC-CT-LIST-011 | srs-fr-06:912 |  | Login `cb_nv_tw_01` |  | 1. Click "Xuất Excel" toolbar | File .xlsx download. Nội dung khớp DS đang filter (cùng filter trạng thái/quy mô/range ngày) | P1 | PASS |  |
| TC-CT-LIST-012 | INF-CT-01, srs-fr-06:220 |  | Login `cb_nv_tw_01` |  | 1. Vào /chi-tra/danh-sach 2. Nhập keyword "không-tồn-tại-zzzzz" 3. Click "Tìm kiếm" | DS empty với INF-CT-01 "Không tìm thấy hồ sơ phù hợp" hiển thị placeholder. KHÔNG crash | P1 | PASS |  |

---

## 02-TC-FR-V.II-03-kiem-tra-HS

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\chi-tra\02-TC-FR-V.II-03-kiem-tra-HS.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\chi-tra\report-02-TC-FR-V.II-03-kiem-tra-HS\Tcs-report\TCs-result.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-CT-KT-010 | ERR-CT-KT-01, srs-fr-06:290 |  | HS Z DANG_DANH_GIA (đã qua kiểm tra) |  | 1. Force POST API kiểm tra với HS Z | ERR-CT-KT-01 "Hồ sơ không ở trạng thái đang kiểm tra" — HTTP 400 | P0 | PASS |  |

---

## 03-TC-FR-V.II-05-danh-gia-tieu-chi

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\chi-tra\03-TC-FR-V.II-05-danh-gia-tieu-chi.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\chi-tra\report-03-TC-FR-V.II-05-danh-gia-tieu-chi\Tcs-report\TCs-result.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-CT-DG-012 | BR-CALC-02 (defense) |  | HS DANG_DANH_GIA, phí 2.500.000đ, đề nghị 2.500.000đ. CB NV nhập field readonly thử bypass |  | 1. Inspect element DOM, gỡ readonly attribute từ field "Số tiền được duyệt" 2. Sửa giá trị 5.000.000đ 3. Submit | Backend validate — ignore client value, recalculate theo BR-CALC-02. Số tiền được duyệt vẫn = 2.500.000đ. KHÔNG cho client tampering | P0 | PASS |  |

---

## 04-TC-FR-V.II-09-tham-dinh

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\chi-tra\04-TC-FR-V.II-09-tham-dinh.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\chi-tra\report-04-TC-FR-V.II-09-tham-dinh\Tcs-report\TCs-result.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-CT-TD-005 | srs-fr-06:586 |  | HS X DANG_THAM_DINH |  | 1. Chọn "Cần bổ sung" 2. Nhập nhận xét "Cần bổ sung biên nhận thanh toán phí TV" 3. Submit | HS X giữ DANG_THAM_DINH, `ket_qua_tham_dinh = CAN_BO_SUNG`. Gửi TB DN/TVV bổ sung tài liệu (KHÔNG chuyển state). Nút Trình PD KHÔNG mở | P0 | PASS |  |

---

## 05-TC-FR-V.II-11-12-trinh-PD-phe-duyet

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\chi-tra\05-TC-FR-V.II-11-12-trinh-PD-phe-duyet.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\chi-tra\report-05-TC-FR-V.II-11-12-trinh-PD-phe-duyet\Tcs-report\TCs-result.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-CT-TRINH-003 | ERR-CT-TRINH-01 |  | HS Z DANG_DANH_GIA (chưa thẩm định) |  | 1. Force POST API trình PD HS Z | ERR-CT-TRINH-01 "Hồ sơ chưa đủ điều kiện trình phê duyệt" | P0 | PASS |  |
| TC-CT-PD-001 | AC#1, srs-fr-06:993-995 |  | HS X CHO_PHE_DUYET cùng cấp TW, login `cb_pd_tw_01` |  | 1. Vào /chi-tra/:id 2. Verify section "Phê duyệt" hiện | Section 6 hiện Info card tóm tắt: DN/Quy mô/Phí TV/Số tiền đề nghị/Số tiền duyệt/Mức hỗ trợ%. Nút "Phê duyệt" + "Từ chối — trả về thẩm định" hiện | P0 | PASS |  |
| TC-CT-PD-002 | SM-CHITRA, srs-fr-06:736, srs-fr-06:1227-1244 |  | HS X CHO_PHE_DUYET, login `cb_pd_tw_01` |  | 1. Click "Phê duyệt" 2. Modal xác nhận hiện 3. Nhập số tiền duyệt 2.500.000đ 4. Confirm | HS X → DA_DUYET. `ngay_phe_duyet=NOW()`, `nguoi_phe_duyet_id=cb_pd_tw_01.id`. Tạo PHE_DUYET_CHI_TRA (quyet_dinh=DUYET, so_tien_duyet=2500000). TB CB NV + TVV + DN. | P0 | PASS |  |
| TC-CT-PD-003 | ERR-CT-PD-03, srs-fr-06:762 |  | HS X CHO_PHE_DUYET, login `cb_pd_tw_01` |  | 1. Click "Phê duyệt" 2. Để số tiền duyệt trống | Validation error "Số tiền phê duyệt là bắt buộc" (ERR-CT-PD-03) | P0 | PASS |  |
| TC-CT-PD-005 | ERR-CT-PD-02, srs-fr-06:761 |  | HS X CHO_PHE_DUYET, login `cb_pd_tw_01` |  | 1. Click "Từ chối" 2. Để Lý do trống | Validation "Lý do từ chối là bắt buộc" (ERR-CT-PD-02) | P0 | PASS |  |
| TC-CT-PD-006 | BR-FLOW-04, srs-fr-06:1238, srs-fr-06:766 |  | HS X CHO_PHE_DUYET, login `cb_pd_tw_01` |  | 1. Click "Từ chối" 2. Nhập lý do 5 ký tự "ngắn" 3. Confirm | Validation "Lý do từ chối phải ≥ 10 ký tự" (BR-FLOW-04) | P0 | PASS |  |
| TC-CT-PD-009 | ERR-CT-PD-01, srs-fr-06:760 |  | HS Y trạng thái khác (DA_DUYET đã duyệt) |  | 1. Force POST API duyệt Y | ERR-CT-PD-01 "Hồ sơ không ở trạng thái chờ phê duyệt" | P0 | PASS |  |

---

## 06-TC-FR-V.II-13-cap-nhat-thanh-toan

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\chi-tra\06-TC-FR-V.II-13-cap-nhat-thanh-toan.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\chi-tra\report-06-TC-FR-V.II-13-cap-nhat-thanh-toan\Tcs-report\TCs-result.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-CT-TT-001 | AC#1, srs-fr-06:996-1001 |  | HS X DA_DUYET, login `cb_nv_tw_01` |  | 1. Vào /chi-tra/:id 2. Verify section "Cập nhật Thanh toán" | Section 7 hiện 4 field: "Số tiền thực trả" (Number, bắt buộc, > 0 AND ≤ so_tien_duoc_duyet), "Ngày thanh toán" (DatePicker, bắt buộc, default hôm nay, ≤ hôm nay), "Số biên nhận" (Text, optional), "Ghi chú thanh toán" (Textarea, optional) + nút "Cập nhật thanh toán" | P0 | PASS |  |
| TC-CT-TT-003 | ERR-CT-TT-02, srs-fr-06:823 |  | HS X DA_DUYET, so_tien_duoc_duyet=2.500.000đ |  | 1. Nhập so_tien_thuc_tra = 3.000.000đ (vượt) 2. Submit | Validation error "Số tiền thực trả không được vượt số tiền được duyệt" (ERR-CT-TT-02). KHÔNG submit | P0 | PASS |  |
| TC-CT-TT-004 | ERR-CT-TT-03, srs-fr-06:824 |  | HS X DA_DUYET |  | 1. Nhập so_tien_thuc_tra = 2.000.000đ 2. Để Ngày TT trống 3. Submit | Validation error "Ngày thanh toán là bắt buộc" (ERR-CT-TT-03) | P0 | PASS |  |
| TC-CT-TT-007 | ERR-CT-TT-01, srs-fr-06:822 |  | HS Y trạng thái khác (CHO_PHE_DUYET) |  | 1. Force POST API cập nhật TT Y | ERR-CT-TT-01 "Hồ sơ không ở trạng thái đã duyệt" — HTTP 400 | P0 | PASS |  |
| TC-CT-TT-009 | srs-fr-06:997, **SPEC-CLARIFY-CT-08** |  | HS X DA_DUYET, so_tien_duoc_duyet=2.500.000đ |  | 1. Nhập so_tien_thuc_tra = 0 đ 2. Submit | Validation error "Số tiền thực trả phải > 0 và không được vượt số tiền được duyệt" (srs-fr-06:997 "Validate: > 0 AND ≤ so_tien_duoc_duyet"). KHÔNG submit. **Edge case riêng**: Nếu so_tien_duoc_duyet=0 (do EC-01 phí TV=0), không thực hiện luồng cập nhật thanh toán — xử lý theo BA clarification riêng (SPEC-CLARIFY-CT-08 forward) | P1 | PASS |  |

---

## 10-TC-permission-matrix

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\chi-tra\10-TC-permission-matrix.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\chi-tra\report-10-TC-permission-matrix\Tcs-report\TCs-result.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-CT-PERM-002 | BR-AUTH-08 |  | cb_nv_tw_01 scope TW |  | 1. Vào /chi-tra/danh-sach | Thấy HS toàn quốc (TW + BN + DP). Có quyền tiếp nhận/kiểm tra/đánh giá/thẩm định/trình PD/cập nhật TT trên HS thuộc đơn vị TW | P0 | PASS |  |
| TC-CT-PERM-003 | BR-AUTH-08 |  | cb_nv_dp_01 scope AG |  | 1. Vào /chi-tra/danh-sach | CHỈ thấy HS đơn vị AG. KHÔNG thấy HS BG/BNI hay TW. Force GET /chi-tra/:id của HS BG → 403/404 | P0 | PASS |  |
| TC-CT-PERM-004 | BR-AUTH-05 |  | cb_pd_tw_01 duyệt HS X TW (CHO_PHE_DUYET) |  | 1. Login cb_pd_tw_01 2. Click Phê duyệt HS X | Cho phép — cùng cấp đơn vị TW | P0 | PASS |  |
| TC-CT-PERM-005 | BR-AUTH-05, BR-AUTH-08 |  | cb_pd_dp_01 duyệt HS X TW (CHO_PHE_DUYET) |  | 1. Login cb_pd_dp_01 2. Force GET /chi-tra/:id HS X | 403/404 — CB PD DP KHÔNG duyệt được HS TW (BR-AUTH-05 cùng cấp + BR-AUTH-08 scope) | P0 | PASS |  |
| TC-CT-PERM-013 | ERR-CT-KT-01 |  | cb_nv_tw_01 force POST API kiểm tra HS X (CHO_TIEP_NHAN) chưa tiếp nhận |  | 1. Force POST /chi-tra/:id/kiem-tra | ERR-CT-KT-01 — HS không ở DANG_KIEM_TRA. State guard backend | P1 | PASS |  |
| TC-CT-PERM-016 | BR-AUTH-08 (IDOR) |  | login dn_01, IDOR test |  | 1. dn_01 vào HS X (của dn_01) qua /chi-tra/:id?id=100 2. Đổi URL thành /chi-tra/:id?id=200 (HS dn_02) | 403/404 — backend validate ownership theo session, KHÔNG dựa vào URL param | P0 | PASS |  |
| TC-CT-PERM-017 | BR-AUTH-05, srs-fr-06:734 |  | login cb_pd_dp_01 (AG) — HS X TW đang CHO_PHE_DUYET |  | 1. cb_pd_dp_01 force POST /api/chi-tra/:id/duyet HS X | 403 — BR-AUTH-05 cùng cấp đơn vị. Backend validate `cb_pd.don_vi_id == hs.don_vi_id` (srs-fr-06:734) | P0 | PASS |  |

---

## Skipped

Các section sau KHÔNG có TC nào ở trạng thái PASS/PASS-DEVIATE/PASS-RESOLVED → bỏ qua:

- `07-TC-FR-V.II-14-DN-bo-sung-HS` — toàn bộ 10 TC BLOCKED (DN bổ sung qua DVC, endpoint LGSP không expose local).
- `08-TC-FR-V.II-08-thong-bao-TVV` — 6 TC: 1 PARTIAL + 4 DEFERRED + 1 N/A.
- `09-TC-API-side-effect` — toàn bộ 7 TC BLOCKED (không có cách trigger LGSP inbound/outbound từ local).
