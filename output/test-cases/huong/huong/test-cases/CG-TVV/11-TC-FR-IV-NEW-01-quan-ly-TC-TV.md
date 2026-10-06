# Test Cases — FR-IV-NEW-01: Quản lý Tổ chức Tư vấn (CRUD + Xuất Phụ lục 2 BTP)

> **SRS Ref**: FR-IV-NEW-01, SCR-IV-NEW-01/02/03, Entity TO_CHUC_TU_VAN, SM-TCTV (start MOI_DANG_KY)
> **Nguồn**: NotebookLM `4dd0675e-a4fa-4ea6-80ae-48e76b3fa264` + LOCAL `srs-fr-04-chuyen-gia-tvv- v3.1.md:1080-1187`
> **Ngày tạo**: 2026-05-09

---

## A. UI FIELD VERIFICATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-TC-UI-01 | FR-IV-NEW-01 / SCR-IV-NEW-01 / UI DS | Verify SCR-IV-NEW-01 DS Tổ chức TV (4 tab + 4 filter + table) | qtht_01 đã đăng nhập | URL `/to-chuc-tv/danh-sach` | 1. Sidebar "Tổ chức tư vấn" → "Danh sách" | **TABS (4)**: Đang hoạt động (default), Tạm dừng, Mới đăng ký, Chờ phê duyệt (visible chỉ CB PD)<br>**FILTERS (4)**: Tìm kiếm (Placeholder "Tìm theo mã, tên TC TV, Số ĐKHĐ"), Loại hình (CONG_TY_LUAT/VP_LUAT_SU/TT_TVPL/KHAC), Đơn vị quản lý (cây 2 tầng), Trạng thái (multi)<br>**TABLE columns**: Mã TC, Tên, Loại hình (label VN), Người đại diện, Đơn vị, Trạng thái (badge SM-TCTV), Số TVV liên kết (count), Hành động<br>**Header**: 2 nút (+ Thêm tổ chức tư vấn / Xuất Excel với tooltip "Mẫu Phụ lục 2 — QĐ 1322/QĐ-BTP") | Happy 🔴 |
| TC-TC-UI-02 | FR-IV-NEW-01 / SCR-IV-NEW-02 / UI Form | Verify form Thêm/Sửa TC TV (17 fields) | qtht_01 | URL `/to-chuc-tv/form` | 1. Click "+ Thêm" | **FIELDS (17)**: ma_to_chuc (auto), ten_to_chuc*, loai_hinh* (dropdown 4 enum), nguoi_dai_dien*, chuc_vu_dai_dien, **so_giay_dkhd* + ngay_cap_dkhd* (BẮT BUỘC theo NĐ 77/2008 Đ.13)**, linh_vuc_ids* (multi ≥1), so_lao_dong, dia_chi*, dien_thoai, email (RFC 5322), website, so_qd_cong_bo, ngay_qd_cong_bo, ghi_chu (max 5000 ký), file_dinh_kem (PDF/DOC/DOCX/XLS/XLSX max 20MB/file)<br>**NEGATIVE**: KHÔNG có field "Trạng thái" (auto MOI_DANG_KY); KHÔNG cho phép tạo trực tiếp HOAT_DONG (NĐ 55/2019 Đ.9) | Happy 🔴 |

## B. CREATE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-TC-001 | FR-IV-NEW-01 / AC1+AC2 | Happy path tạo TC TV mới | cb_nv_tw_01, ≥1 lĩnh vực PL | ten: "Công ty Luật ABC", loai_hinh: CONG_TY_LUAT, nguoi_dai_dien: "Nguyễn Văn A", so_giay_dkhd: "ĐKHĐ-001", ngay_cap_dkhd: 2025-01-15, linh_vuc: ["Lao động"], dia_chi: "Hà Nội" | 1. Click + Thêm<br>2. Nhập 17 fields valid<br>3. Lưu | **STATE**: TO_CHUC_TU_VAN insert ma_to_chuc=TC-TW-{seq}, **trang_thai=MOI_DANG_KY (theo NĐ 55/2019 Đ.9, KHÔNG tạo HOAT_DONG trực tiếp)**, version=0, don_vi_id=current_user.don_vi_id; junction TC_LINH_VUC insert; AUDIT_LOG; Notification gửi CB NV cùng cấp để trình CB PD<br>**UI**: Toast "Thêm tổ chức tư vấn 'Công ty Luật ABC' thành công"<br>**PERSIST**: Tab "Mới đăng ký" có record mới | Happy 🔴 |
| TC-TC-002 | FR-IV-NEW-01 / E1 ERR-TCTV-01 | Tên trống → ERR-TCTV-01 | cb_nv_tw_01 | ten: "" | 1. Submit | "Tên tổ chức là bắt buộc" (NGUYÊN VĂN ERR-TCTV-01) | Negative 🟡 |
| TC-TC-003 | FR-IV-NEW-01 / NĐ 77/2008 Đ.13 | so_giay_dkhd + ngay_cap_dkhd BẮT BUỘC | cb_nv_tw_01 | so_giay_dkhd: "" | 1. Submit thiếu Số ĐKHĐ | API 400 "Số giấy ĐKHĐ là bắt buộc theo NĐ 77/2008 Điều 13" (NGUYÊN VĂN hoặc tương đương) — SPEC-CLARIFY-CGTVV-07 nếu SRS không có ERR code chính xác | Negative 🔴 |
| TC-TC-004 | FR-IV-NEW-01 / E5 ERR-TCTV-05 | File >20MB → ERR-TCTV-05 | cb_nv_tw_01 | file 21MB | 1. Upload 21MB | "File tối đa 20MB/file" (NGUYÊN VĂN ERR-TCTV-05) | Negative 🟡 |
| TC-TC-005 | FR-IV-NEW-01 / E6 ERR-TCTV-06 | Thiếu lĩnh vực → ERR-TCTV-06 | cb_nv_tw_01 | linh_vuc_ids: [] | 1. Submit | "Chọn ít nhất 1 lĩnh vực pháp lý" (NGUYÊN VĂN ERR-TCTV-06) | Negative 🟡 |
| TC-TC-006 | FR-IV-NEW-01 / E7 ERR-TCTV-07 | Email invalid → ERR-TCTV-07 | cb_nv_tw_01 | email: "invalid" | 1. Submit | "Email không đúng định dạng" (NGUYÊN VĂN ERR-TCTV-07) | Negative 🟡 |
| TC-TC-007 | FR-IV-NEW-01 / E8 ERR-TCTV-08 | Virus scan → ERR-TCTV-08 | cb_nv_tw_01 | EICAR | 1. Upload EICAR | "File eicar.pdf chứa mã độc, bị từ chối" (NGUYÊN VĂN ERR-TCTV-08) | Negative 🟡 |

## C. READ / List

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-TC-101 | FR-IV-NEW-01 / List filter loại hình | Filter Loại hình "CONG_TY_LUAT" | qtht_01, mixed loại hình | loai_hinh=CONG_TY_LUAT | 1. Filter loại hình | Table chỉ TC TV CONG_TY_LUAT | Happy 🟡 |
| TC-TC-102 | FR-IV-NEW-01 / Detail | Mở chi tiết SCR-IV-NEW-03 | qtht_01, TC-TW-001 HOAT_DONG | — | 1. Click row → SCR-IV-NEW-03 | URL `/to-chuc-tv/chi-tiet/TC-TW-001`; tabs/sections: Thông tin chung, Lĩnh vực, TVV liên kết (count), Lịch sử trạng thái, File đính kèm | Happy 🟡 |
| TC-TC-103 | FR-IV-NEW-01 / BR-AUTH-08 | CB NV ĐP CHỈ thấy TC TV cùng đơn vị | cb_nv_dp_01 (HN) | TC TV thuộc HN: 2; HP: 1 | 1. Login cb_nv_dp_01<br>2. Mở list | Chỉ 2 TC TV HN; HP không thấy | Negative 🔴 |

## D. UPDATE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-TC-201 | FR-IV-NEW-01 / Update | Sửa TC TV chưa duyệt | cb_nv_tw_01, TC-TW-002 MOI_DANG_KY | nguoi_dai_dien: "Trần Thị B" | 1. Sửa<br>2. Lưu | UPDATE OK; AUDIT_LOG diff | Happy 🟡 |
| TC-TC-202 | FR-IV-NEW-01 / BR-FLOW-03 | KHÔNG sửa TC TV đã HOAT_DONG (qua phê duyệt) | cb_nv_tw_01, TC-TW-001 HOAT_DONG | — | 1. Mở chi tiết | KHÔNG có nút Sửa các field core; chỉ field optional editable (mô tả công khai); SPEC-CLARIFY-CGTVV-08 nếu SRS không phân biệt rõ field nào sửa được sau duyệt | Edge 🟡 |

## E. DELETE soft

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-TC-301 | FR-IV-NEW-01 / Delete soft | Xóa TC TV không có TVV liên kết | cb_nv_tw_01, TC-TW-099 không có TVV_TO_CHUC HOAT_DONG | — | 1. Action Xóa | TO_CHUC_TU_VAN.is_deleted=1; AUDIT_LOG | Happy 🟡 |
| TC-TC-302 | FR-IV-NEW-01 / E2 ERR-TCTV-02 | Xóa TC TV có TVV liên kết → ERR-TCTV-02 | cb_nv_tw_01, TC-TW-001 có ≥1 TVV liên kết HOAT_DONG | — | 1. Action Xóa | "Tổ chức đang có tư vấn viên hoạt động, không thể xóa" (NGUYÊN VĂN ERR-TCTV-02) | Negative 🔴 |

## F. EXPORT Phụ lục 2 BTP

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-TC-401 | FR-IV-NEW-01 / Export PL2 BTP | Xuất Excel theo Phụ lục 2 — QĐ 1322/QĐ-BTP (12 cột) | qtht_01, ≥10 TC TV HOAT_DONG | filter: Loại hình CONG_TY_LUAT | 1. Click "Xuất Excel"<br>2. Verify file | **STATE**: Network `GET /api/v1/to-chuc-tv/export-pl2?...`; Content-Type Excel<br>**UI**: Toast "Xuất Excel thành công"<br>**PERSIST**: File mở Excel — header chứa **12 cột Phụ lục 2** (theo SRS line 1151 + bảng entity TO_CHUC_TU_VAN cột "Nguồn mẫu BTP"): Cột 2 (Đơn vị), 3 (Tên), 4 (Loại hình), 5 (Người đại diện + chức vụ), 6 (Số ĐKHĐ + Ngày cấp), 7 (Lĩnh vực), 8 (Số lao động), 9 (Địa chỉ), 10 (SĐT/Email/Web), 11 (Số QĐ + Ngày QĐ), 12 (Ghi chú); max 10K rows | Happy 🔴 |

## G. Công khai TC TV (link FR-IV-08)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-TC-501 | FR-IV-NEW-01 / AC3 | Công khai TC TV HOAT_DONG | cb_nv_tw_01, TC-TW-001 HOAT_DONG | mo_ta + 1 file | 1. Mở chi tiết<br>2. Switch Công khai → Modal MD-CONG-KHAI<br>3. Confirm | TO_CHUC_TU_VAN cập nhật cong_khai=1, thoi_gian_dang_tai=NOW; API outbound POST Cổng (BR-PUBLIC-01); AUDIT_LOG | Happy 🟡 |
| TC-TC-502 | FR-IV-NEW-01 / E3 ERR-TCTV-03 | Công khai TC TV không HOAT_DONG → ERR-TCTV-03 | cb_nv_tw_01, TC-TW-002 MOI_DANG_KY | — | 1. Cố Công khai | "Chỉ tổ chức đang hoạt động mới được công khai" (NGUYÊN VĂN ERR-TCTV-03) | Negative 🟡 |

---

## H. EDGE bổ sung (A4 inline merge — 3 edge)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-TC-601 | EDGE-A4-f / Mã TC diacritics | Mã TC TV với diacritics URL escape | qtht_01 | URL `/to-chuc-tv/chi-tiet/TC-TW-Hà-Nội-001` (encoded `%C3%A0...`) | 1. Direct URL với encoded | URL parse OK; chi tiết hiển thị đúng record; SPEC-CLARIFY nếu mã TC TV không support diacritics | Edge 🟡 |
| TC-TC-602 | EDGE-A4-bb / IDOR field-level don_vi_id | DevTools tamper don_vi_id của TC TV chính mình → backend reject | cb_nv_dp_HN_01, TC-HN-001 | DevTools PUT với don_vi_id=HP | 1. Tamper PUT request | Backend ghi đè don_vi_id = current TC.don_vi_id (HN); KHÔNG cho user move TC sang đơn vị khác (BR-AUTH-08) | Edge 🔴 |
| TC-TC-603 | EDGE-A4-kk / Export PL2 legacy data | Export PL2 khi TC TV chưa có Số ĐKHĐ (data legacy migration) | qtht_01, TC-TW-099 so_giay_dkhd=NULL | — | 1. Export Excel | File Excel có cell trống cho cột Số ĐKHĐ; KHÔNG block export; SPEC-CLARIFY-CGTVV-17 nếu SRS yêu cầu so_giay_dkhd NOT NULL hoàn toàn | Edge 🟡 |

---

## I. A6 fill gap (Traceability matrix forward — 1 TC)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-TC-701 | A6-FILL / WRN-TCTV-04 API Cổng fail | Công khai TC TV — API Cổng PLQG fail → WRN-TCTV-04 (verify qua UI) | cb_nv_tw_01, TC-TW-001 HOAT_DONG, mock Cổng API down | mo_ta + 1 file | 1. Click Công khai<br>2. Confirm<br>3. **Verify qua list reload sau 5 phút** | **STATE**: cong_khai vẫn 0 (BR-EC-20)<br>**UI**: Warning "Cập nhật Cổng pháp luật quốc gia thất bại, sẽ thử lại" (NGUYÊN VĂN WRN-TCTV-04) immediately<br>**A7 SỬA**: verify retry qua list reload + Cổng public hiển thị TC sau retry success; KHÔNG verify queue trực tiếp + admin email (cần admin tool ngoài scope tester) | Edge 🟡 |

---

**Tổng số TC**: 22 (2 UI + 6 Create + 3 Read + 2 Update + 2 Delete + 1 Export + 2 Công khai + 3 Edge A4 + 1 A6 fill)
