# Test Cases — FR-IV-04: NHT cập nhật năng lực TVV

> **SRS Ref**: FR-IV-04 (UC42), SCR-IV-03 Tab Năng lực, Entity HO_SO_TU_VAN_VIEN
> **Nguồn**: NotebookLM `4dd0675e-a4fa-4ea6-80ae-48e76b3fa264` + LOCAL `srs-fr-04-chuyen-gia-tvv- v3.1.md:361-429`
> **Ngày tạo**: 2026-05-09

---

## A. UI FIELD VERIFICATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-NL-UI-01 | FR-IV-04 / SCR-IV-03 Tab Năng lực / UI | Verify Tab Năng lực inline edit form NHT | nht_01 (HN), TVV-TW-300 cùng đơn vị HOAT_DONG | — | 1. Login nht_01<br>2. Mở chi tiết TVV-TW-300<br>3. Click tab Năng lực<br>4. Verify form | **FIELDS**: trinh_do (dropdown Cử nhân/Thạc sĩ/Tiến sĩ/Khác), so_nam_kinh_nghiem (number ≥0), chuyen_nganh, bang_cap_chi_tiet (JSON array editor), chung_chi_chi_tiet (JSON array), chung_chi_moi (file upload PDF max 10MB tổng 50MB max 10 files), so_the_hanh_nghe, file_the_hanh_nghe (PDF max 10MB), linh_vuc_ids (multi ≥1), mo_ta_kinh_nghiem (textarea max 5000 ký), ghi_chu_cap_nhat (max 2000 ký)<br>**LAYOUT**: Nút "Sửa" / "Lưu" / "Hủy" footer; KHÔNG có nút này khi user là tvv_01/cg_01 (read-only) | Happy 🔴 |
| TC-NL-UI-02 | FR-IV-04 / Read-only TVV/CG | Verify TVV/CG đăng nhập chuyên trang chỉ xem tab Năng lực, KHÔNG sửa | tvv_01, hồ sơ TVV-TW-001 của tvv_01 | — | 1. Login tvv_01 chuyên trang<br>2. Xem hồ sơ → tab Năng lực | KHÔNG có nút Sửa; tất cả field readonly; Banner "Liên hệ Người hỗ trợ pháp lý cùng đơn vị để cập nhật" | Negative 🔴 |

## B. UPDATE năng lực

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-NL-001 | FR-IV-04 / AC1+AC2 | Happy path NHT cập nhật năng lực | nht_01 (HN), TVV-TW-300 cùng đơn vị | so_nam_kinh_nghiem: 5→8, thêm 1 chứng chỉ mới + 1 file PDF | 1. Click Sửa tab Năng lực<br>2. Update field<br>3. Upload PDF<br>4. Lưu | **STATE**: HO_SO_TU_VAN_VIEN cập nhật so_nam_kinh_nghiem=8, chung_chi_chi_tiet thêm entry; FILE_DINH_KEM insert mới link tới TVV; updated_at + updated_by; AUDIT_LOG INSERT diff old→new<br>**UI**: Toast "Cập nhật năng lực thành công"<br>**PERSIST**: Reload tab Năng lực → giá trị mới | Happy 🔴 |
| TC-NL-002 | FR-IV-04 / E1 | NHT khác đơn vị → ERR-NL-01 | nht_HP_01 (HP), TVV-TW-300 (HN) | — | 1. Login nht_HP_01<br>2. Mở chi tiết TVV-TW-300<br>3. Cố sửa | **UI**: KHÔNG có nút Sửa visible (BR-AUTH-08); nếu DevTools tamper → API 403 "Bạn không có quyền cập nhật hồ sơ tư vấn viên này (khác đơn vị)" (NGUYÊN VĂN ERR-NL-01) | Negative 🔴 |
| TC-NL-003 | FR-IV-04 / E2 | File >10MB/file → ERR-NL-02 | nht_01 | 1 file 11MB | 1. Upload 11MB<br>2. Lưu | Inline error "File tải lên tối đa 10MB/file" (NGUYÊN VĂN ERR-NL-02) | Negative 🟡 |
| TC-NL-004 | FR-IV-04 / E3 | File tổng >50MB → ERR-NL-03 | nht_01 | 6 file × 9MB | 1. Upload 6 file<br>2. Lưu | Inline error "Tổng dung lượng file tối đa 50MB" (NGUYÊN VĂN ERR-NL-03) | Negative 🟡 |
| TC-NL-005 | FR-IV-04 / E4 | Virus scan → ERR-NL-04 | nht_01 | EICAR `eicar.pdf` | 1. Upload EICAR<br>2. Lưu | Toast "File eicar.pdf chứa mã độc, bị từ chối" (NGUYÊN VĂN ERR-NL-04) | Negative 🟡 |
| TC-NL-006 | FR-IV-04 / E5 | TVV VO_HIEU_HOA → ERR-NL-05 | nht_01, TVV-TW-301 VO_HIEU_HOA | — | 1. Mở chi tiết TVV-TW-301<br>2. Tab Năng lực — verify | Tab Năng lực KHÔNG có nút Sửa; nếu DevTools force submit → "Hồ sơ đã bị vô hiệu hóa, không thể chỉnh sửa" (NGUYÊN VĂN ERR-NL-05) | Negative 🟡 |
| TC-NL-007 | FR-IV-04 / Auto trigger transition | Cập nhật khi YEU_CAU_BO_SUNG → auto chuyển DANG_THAM_DINH | nht_01, TVV-TW-302 YEU_CAU_BO_SUNG | Sửa trinh_do | 1. Sửa Trình độ<br>2. Lưu | **STATE**: HO_SO cập nhật + TU_VAN_VIEN.trang_thai chuyển DANG_THAM_DINH (theo FR-IV-04 step 7 + FR-IV-13 transition 2); AUDIT_LOG 2 entries (UPDATE + STATE_CHANGE)<br>**UI**: Toast "Cập nhật + chuyển sang đang thẩm định"; Badge trạng thái update real-time | Happy 🔴 |
| TC-NL-008 | FR-IV-04 / Update không đụng linh_vuc | Sửa chỉ trinh_do, không đụng linh_vuc → KHÔNG affect TVV_LINH_VUC | nht_01, TVV-TW-303 HOAT_DONG | trinh_do: Cử nhân→Thạc sĩ | 1. Sửa trinh_do<br>2. Lưu | TVV_LINH_VUC KHÔNG insert/update; chỉ HO_SO_TU_VAN_VIEN.trinh_do thay đổi | Edge 🟡 |
| TC-NL-009 | FR-IV-04 / Update lĩnh vực | Sửa linh_vuc_ids → cập nhật junction TVV_LINH_VUC | nht_01, TVV-TW-303 LV ban đầu [Lao động] | linh_vuc_ids: [Lao động, Thuế] | 1. Thêm "Thuế" vào LV<br>2. Lưu | TVV_LINH_VUC: thêm row (tvv_id, "Thuế"); AUDIT_LOG diff [Lao động] → [Lao động, Thuế] | Happy 🟡 |
| TC-NL-010 | FR-IV-04 / Sanitize XSS | mo_ta_kinh_nghiem chứa `<script>` → sanitize | nht_01 | mo_ta_kinh_nghiem: `<script>alert(1)</script>Test` | 1. Nhập mô tả XSS<br>2. Lưu | DB lưu sau sanitize: "Test" (strip script); Reload UI render plain text, KHÔNG execute alert | Edge 🔴 |

---

## C. EDGE bổ sung (A4 inline merge — 1 edge)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-NL-501 | EDGE-A4-b / Race NHT update + CB NV thẩm định | NHT update Năng lực cùng lúc CB NV submit Thẩm định | nht_01 + cb_nv_tw_01, TVV-TW-302 DANG_THAM_DINH | — | 1. NHT đang sửa năng lực<br>2. CB NV submit kết luận DAT đồng thời | Race: state thay đổi sang CHO_PHE_DUYET → NHT save fail "Hồ sơ đã chuyển sang trạng thái Chờ phê duyệt, không thể chỉnh sửa năng lực"; SPEC-CLARIFY-CGTVV-12 | Edge 🔴 |

---

## D. A6 fill gap (Traceability matrix forward — 1 TC)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-NL-601 | A6-FILL / BR-FLOW-03 HO_SO sau approval | NHT cố sửa HO_SO_TU_VAN_VIEN của TVV đã HOAT_DONG (sau approval) → reject | nht_01, TVV-TW-310 HOAT_DONG | bang_cap_chi_tiet thêm 1 entry | 1. Mở chi tiết TVV-TW-310 tab Năng lực<br>2. Verify nút Sửa | UI: nút Sửa visible cho NHT cùng đơn vị (FR-IV-04 cho phép update năng lực bất kỳ trạng thái); SPEC-CLARIFY-CGTVV-23: BR-FLOW-03 có override cho HO_SO không? Nếu reject → cần ERR code; nếu allow → audit critical change | Edge 🟡 |

---

**Tổng số TC**: 14 (2 UI + 10 Update + 1 Edge A4 + 1 A6 fill)
