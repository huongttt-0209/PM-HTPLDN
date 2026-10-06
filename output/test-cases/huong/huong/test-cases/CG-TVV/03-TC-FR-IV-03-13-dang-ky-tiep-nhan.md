# Test Cases — FR-IV-03 + FR-IV-13: NHT đăng ký TVV + Tiếp nhận / Chuyển trạng thái tiền thẩm định

> **SRS Ref**: FR-IV-03 (UC41) + FR-IV-13, SCR-IV-02, Entity TU_VAN_VIEN, SM-TVV ([*]→MOI_DANG_KY→CHO_THAM_DINH; YEU_CAU_BO_SUNG→DANG_THAM_DINH; TU_CHOI→CHO_THAM_DINH)
> **Nguồn**: NotebookLM `4dd0675e-a4fa-4ea6-80ae-48e76b3fa264` + LOCAL `srs-fr-04-chuyen-gia-tvv- v3.1.md:274-358 + 950-1015`
> **Ngày tạo**: 2026-05-09

---

## A. UI FIELD VERIFICATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-DK-UI-01 | FR-IV-03 / SCR-IV-02 / UI form NHT đăng ký | Verify form NHT đăng ký TVV gồm 18 trường + Đơn vị auto-set readonly | nht_01 đã đăng nhập | URL `/chuyen-gia-tvv/form` | 1. Login nht_01 (don_vi: Sở TP HN)<br>2. Click "+ Thêm tư vấn viên"<br>3. Verify form | **FIELDS (18+1)**: loai_tvv* (radio TVV/CG mặc định TVV), ho_ten*, cmnd_cccd*, ngay_sinh* (≤today), gioi_tinh* (NAM/NU/KHAC), email*, so_dien_thoai* (10-11 số), dia_chi*, chuc_vu, noi_cong_tac, trinh_do*, chuyen_nganh*, so_nam_kinh_nghiem*, linh_vuc_ids* (multi ≥1), to_chuc_id, **don_vi_id (auto-set "Sở TP HN" readonly)**, anh_dai_dien (jpg/png max 5MB), file_bang_cap* (PDF max 10MB/file), file_the_hanh_nghe (PDF max 10MB — bắt buộc nếu loai_tvv=TVV theo NĐ 77/2008 Đ.20)<br>**NEGATIVE**: KHÔNG có dropdown "Đơn vị quản lý" cho NHT (auto-set NHT.don_vi_id); KHÔNG có ô "Địa bàn"; KHÔNG có nút "Tiếp nhận hồ sơ" sau khi tạo (D.2.1 OUT) | Happy 🔴 |
| TC-DK-UI-02 | FR-IV-13 / SCR-IV-03 / UI Tiếp nhận | Verify action header phụ thuộc trạng thái TVV (Conflict D.2.1 vs SRS body) | cb_nv_tw_01, TVV-TW-100 (MOI_DANG_KY) + TVV-TW-101 (CHO_THAM_DINH) | — | 1. Mở chi tiết TVV-TW-100 (MOI_DANG_KY)<br>2. Verify action header<br>3. Mở TVV-TW-101 (CHO_THAM_DINH)<br>4. Verify | **MOI_DANG_KY**: Theo SRS line 1606 vẫn có nút "Tiếp nhận hồ sơ" header + MD-TIEP-NHAN; Theo CHANGELOG D.2.1 OUT thì gộp 1 thao tác "Bắt đầu thẩm định". **SPEC-CLARIFY-CGTVV-27**: Tester verify thực tế UI build, ghi finding cho BA. **CHO_THAM_DINH**: Có nút "Bắt đầu thẩm định" → mở Tab Thẩm định + chuyển DANG_THAM_DINH | Happy 🔴 |

## B. NHT đăng ký TVV (FR-IV-03)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-DK-001 | FR-IV-03 / AC1+AC2 | Happy path NHT đăng ký TVV mới | nht_01 (don_vi=Sở TP HN), Tổ chức TV "Công ty Luật ABC" HOAT_DONG | loai_tvv=TVV, full 18 fields valid + 1 file bằng cấp + 1 file thẻ hành nghề | 1. Login nht_01<br>2. Mở form Thêm<br>3. Nhập đủ 18 fields + upload 2 file<br>4. Click Lưu | **STATE**: TU_VAN_VIEN insert với `loai_tvv='TVV'`, `trang_thai='MOI_DANG_KY'`, **`don_vi_id=NHT.don_vi_id` (Sở TP HN auto)**, version=0; TVV_LINH_VUC junction insert; FILE_DINH_KEM 2 record; AUDIT_LOG action=CREATE; **Notification gửi cb_nv_dp_01 cùng đơn vị HN**<br>**UI**: Toast "Đăng ký thành công, chờ thẩm định"<br>**PERSIST**: List tab "Mới đăng ký" → record mới; cb_nv_dp_01 nhận notification badge | Happy 🔴 |
| TC-DK-002 | FR-IV-03 / E1 | NHT đăng ký TVV đã có hồ sơ chờ → ERR-DK-01 | nht_01, đã có TVV CCCD `001234567890` trạng thái MOI_DANG_KY | CCCD trùng | 1. Submit form CCCD trùng | **STATE**: KHÔNG insert<br>**UI**: Toast "Ứng viên (theo CCCD) đã có hồ sơ đang chờ xử lý" (NGUYÊN VĂN ERR-DK-01) | Negative 🔴 |
| TC-DK-003 | FR-IV-03 / E2 | File bằng cấp >10MB → ERR-DK-02 | nht_01 | 1 file PDF 11MB | 1. Upload 11MB<br>2. Submit | Inline error "File tải lên tối đa 10MB/file" (NGUYÊN VĂN ERR-DK-02); KHÔNG insert | Negative 🟡 |
| TC-DK-004 | FR-IV-03 / E3 | Thiếu file bằng cấp → ERR-DK-03 | nht_01, loai_tvv=CG | KHÔNG upload file bằng cấp | 1. Submit không upload | Inline error "Bằng cấp/chứng chỉ là bắt buộc" (NGUYÊN VĂN ERR-DK-03) | Negative 🟡 |
| TC-DK-005 | FR-IV-03 / E5 | File tổng >50MB → ERR-DK-05 | nht_01 | 6 file × 9MB = 54MB | 1. Upload 6 file<br>2. Submit | Inline error "Tổng dung lượng file tối đa 50MB" (NGUYÊN VĂN ERR-DK-05) | Negative 🟡 |
| TC-DK-006 | FR-IV-03 / E6 | Virus scan ClamAV phát hiện → ERR-DK-06 | nht_01 | EICAR `eicar.pdf` | 1. Upload EICAR<br>2. Submit | Toast "File eicar.pdf chứa mã độc, bị từ chối" (NGUYÊN VĂN ERR-DK-06); KHÔNG insert | Negative 🟡 |
| TC-DK-007 | FR-IV-03 / E7 | Email format invalid → ERR-DK-07 | nht_01 | email: "invalid" | 1. Submit | "Email không đúng định dạng" (NGUYÊN VĂN ERR-DK-07) | Negative 🟡 |
| TC-DK-008 | FR-IV-03 / E8 | Thiếu lĩnh vực → ERR-DK-08 | nht_01 | linh_vuc_ids: [] | 1. Submit không chọn LV | "Chọn ít nhất 1 lĩnh vực pháp lý" (NGUYÊN VĂN ERR-DK-08) | Negative 🟡 |
| TC-DK-009 | FR-IV-03 / E9 | Email đã tồn tại → ERR-DK-09 | nht_01, email "a@example.com" đã có TVV khác | email trùng | 1. Submit | "Email này đã được sử dụng bởi tư vấn viên khác" (NGUYÊN VĂN ERR-DK-09) | Negative 🟡 |
| TC-DK-010 | FR-IV-03 / Loai TVV thẻ HN | TVV bắt buộc file thẻ hành nghề (NĐ 77/2008 Đ.20) | nht_01 | loai_tvv=TVV, KHÔNG upload thẻ | 1. Chọn loai_tvv=TVV<br>2. Submit không có thẻ | API reject với message "Số thẻ hành nghề là bắt buộc cho loại Tư vấn viên (NĐ 77/2008 Điều 20)" — SPEC-CLARIFY-CGTVV-02 nếu SRS không có ERR code chính xác | Negative 🟡 |
| TC-DK-011 | FR-IV-03 / loai_tvv=CG bypass thẻ | CG KHÔNG bắt buộc file thẻ | nht_01 | loai_tvv=CG, KHÔNG thẻ HN | 1. Chọn CG<br>2. Submit | TVV insert OK, không validate file_the_hanh_nghe | Edge 🟡 |
| TC-DK-012 | FR-IV-03 / BR-AUTH-08 don_vi_id auto | Verify don_vi_id KHÔNG sửa được, auto-set NHT.don_vi_id | nht_01 (HN) | DevTools tamper don_vi_id → "Sở TP HP" | 1. Submit với tampered don_vi_id<br>2. Verify | Backend ghi đè `don_vi_id = nht_01.don_vi_id (HN)` ignore client value; Reload chi tiết → don_vi = "Sở TP HN" (HN) | Negative 🔴 |

## C. FR-IV-13 — Transition tiền thẩm định (3 transitions)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-TN-001a | FR-IV-13 / Transition 1 MOI_DANG_KY→CHO_THAM_DINH | CB NV tiếp nhận hồ sơ qua nút header "Tiếp nhận hồ sơ" → MD-TIEP-NHAN | cb_nv_tw_01, TVV-TW-200 MOI_DANG_KY | — | 1. Login cb_nv_tw_01<br>2. Mở chi tiết TVV-TW-200<br>3. Click nút header "Tiếp nhận hồ sơ" (SRS line 1606)<br>4. Modal MD-TIEP-NHAN confirm | **STATE**: TU_VAN_VIEN.trang_thai chuyển **MOI_DANG_KY → CHO_THAM_DINH**; ngay_tiep_nhan=NOW(), nguoi_tiep_nhan=cb_nv_tw_01.id; AUDIT_LOG INSERT<br>**UI**: Badge "Chờ thẩm định" xám; Toast theo MD-TIEP-NHAN<br>**PERSIST**: Notification gửi TVV/CG email "Hồ sơ đã được tiếp nhận"; **SPEC-CLARIFY-CGTVV-27: Conflict CHANGELOG D.2.1 (OUT FR-IV-13 wrapper, gộp 1 thao tác) vs SRS body line 1606 (vẫn có nút "Tiếp nhận hồ sơ" + MD-TIEP-NHAN). Tester verify thực tế UI: nếu có nút "Tiếp nhận hồ sơ" riêng → 2-step; nếu chỉ "Bắt đầu thẩm định" → 1-step ngầm chuyển 2 transition** | Happy 🔴 |
| TC-TN-001b | FR-IV-13 / Transition CHO_THAM_DINH → DANG_THAM_DINH | CB NV bắt đầu thẩm định | cb_nv_tw_01, TVV-TW-200 đã CHO_THAM_DINH (sau TC-TN-001a) | — | 1. Mở chi tiết TVV-TW-200 (CHO_THAM_DINH)<br>2. Click "Bắt đầu thẩm định"<br>3. Verify | **STATE**: TU_VAN_VIEN.trang_thai **CHO_THAM_DINH → DANG_THAM_DINH**; ghi thời điểm bắt đầu; AUDIT_LOG<br>**UI**: Tab "Thẩm định" mở; Badge "Đang thẩm định" vàng nhạt | Happy 🔴 |
| TC-TN-002 | FR-IV-13 / Transition 2 YEU_CAU_BO_SUNG→DANG_THAM_DINH (auto) | NHT bổ sung xong → auto trigger | nht_01, TVV-TW-201 YEU_CAU_BO_SUNG | Cập nhật trinh_do qua FR-IV-04 | 1. Login nht_01<br>2. Mở chi tiết TVV-TW-201 tab Năng lực<br>3. Sửa Trình độ → Lưu | **STATE**: TU_VAN_VIEN.trang_thai chuyển **YEU_CAU_BO_SUNG → DANG_THAM_DINH** (auto trigger từ FR-IV-04 step 7); HO_SO_TU_VAN_VIEN cập nhật<br>**UI**: Toast "Cập nhật năng lực thành công + Chuyển sang đang thẩm định"<br>**PERSIST**: Notification gửi CB NV đã thẩm định trước đó (`nguoi_tham_dinh_id`); reload chi tiết → trạng thái "Đang thẩm định" | Happy 🔴 |
| TC-TN-003 | FR-IV-13 / E3 BO_SUNG_XONG no change | YEU_CAU_BO_SUNG nhưng không cập nhật gì → ERR-CT-03 | nht_01, TVV-TW-202 YEU_CAU_BO_SUNG | KHÔNG sửa field nào | 1. Mở chi tiết tab Năng lực<br>2. Click Lưu (no change) | Inline error "Vui lòng cập nhật ít nhất 1 trường trước khi gửi lại" (NGUYÊN VĂN ERR-CT-03); KHÔNG chuyển trạng thái | Negative 🟡 |
| TC-TN-004 | FR-IV-13 / Transition 3 TU_CHOI→CHO_THAM_DINH | TVV/CG nộp lại sau từ chối — KHÔNG cooldown | tvv_01 chuyên trang, hồ sơ TU_CHOI | Sửa hồ sơ + Submit "Nộp lại" | 1. Login tvv_01 chuyên trang<br>2. Mở hồ sơ TU_CHOI<br>3. Sửa file bằng cấp + click "Nộp lại"<br>4. Verify | **STATE**: TU_VAN_VIEN.trang_thai **TU_CHOI → CHO_THAM_DINH**; HO_SO_TU_VAN_VIEN.trang_thai_tham_dinh = 'CHUA_THAM_DINH' (reset kết quả thẩm định cũ); ket_qua_tham_dinh clear; AUDIT_LOG INSERT<br>**UI**: Toast "Hồ sơ đã được nộp lại, chờ thẩm định"<br>**PERSIST**: KHÔNG có cooldown 6 tháng (NĐ 77/2008 + NĐ 55/2019 không quy định — F-FR04-06); Notification gửi CB NV cùng đơn vị | Happy 🔴 |
| TC-TN-005 | FR-IV-13 / NO cooldown | Verify nộp lại ngay sau từ chối — KHÔNG bị chặn 6 tháng | tvv_01, hồ sơ TU_CHOI thoi_gian_tu_choi=NOW()-1h | Submit Nộp lại sau 1 giờ | 1. Submit nộp lại sau 1h từ TU_CHOI | KHÔNG có error "phải đợi 6 tháng"; transition thành công như TC-TN-004 | Edge 🔴 |
| TC-TN-006 | FR-IV-13 / E1 invalid transition | Cố chuyển từ HOAT_DONG → CHO_THAM_DINH (invalid) → ERR-CT-01 | cb_nv_tw_01, TVV-TW-203 HOAT_DONG | DevTools call API trực tiếp transition | 1. Tamper API call FR-IV-13 từ HOAT_DONG | API 400 "Không thể chuyển từ Đang hoạt động sang Chờ thẩm định" (NGUYÊN VĂN ERR-CT-01 với label substitution) | Negative 🟡 |

---

## D. EDGE bổ sung (A4 inline merge — 4 edge)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-DK-501 | EDGE-A4-b / Race auto-trigger | NHT update YEU_CAU_BO_SUNG đồng thời CB NV thẩm định cùng record | nht_01 + cb_nv_tw_01, TVV-TW-201 YEU_CAU_BO_SUNG | NHT cập nhật + CB NV thay đổi kết luận | 1. 2 tab khác nhau<br>2. Submit cùng lúc | Race: NHT auto-trigger DANG_THAM_DINH (FR-IV-13 transition 2) chạy trước; CB NV submit thẩm định bị reject vì state changed; SPEC-CLARIFY-CGTVV-12 nếu SRS không có optimistic lock cho HO_SO | Edge 🔴 |
| TC-DK-502 | EDGE-A4-h / Whitespace trim email | Email "  a@b.com  " trim trước validate | nht_01 | email: "  a@b.com  " | 1. Submit | Trim → save "a@b.com"; RFC validate PASS | Edge 🟡 |
| TC-DK-503 | EDGE-A4-u / 0-byte file | File bằng cấp 0 byte → reject | nht_01 | file: empty.pdf 0 byte | 1. Upload empty.pdf<br>2. Submit | API reject "File không hợp lệ (0 byte)"; SPEC-CLARIFY nếu SRS không có ERR code | Edge 🟡 |
| TC-DK-504 | EDGE-A4-v / Extension mismatch | File .pdf actually .exe (rename) → ClamAV magic bytes detect | nht_01 | malware.exe rename to malware.pdf | 1. Upload<br>2. Submit | ClamAV detect magic bytes mismatch → reject ERR-DK-06 (NGUYÊN VĂN); KHÔNG insert | Edge 🔴 |

---

## E. A6 fill gap (Traceability matrix forward — 1 TC)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-TN-601 | A6-FILL / ERR-CT-02 explicit | TVV/CG khác đơn vị cố thực hiện FR-IV-13 transition → ERR-CT-02 | tvv_other (đơn vị HP) cố Submit "Nộp lại" cho hồ sơ TU_CHOI khác đơn vị | DevTools tamper API tvv_id=TVV-HN-001 | 1. Login tvv_other<br>2. Tamper API call FR-IV-13 transition NOP_LAI cho TVV-HN-001 | API 403 "Bạn không có quyền thực hiện thao tác này" (NGUYÊN VĂN ERR-CT-02); KHÔNG chuyển trạng thái | Negative 🟡 |

---

**Tổng số TC**: 25 (2 UI + 12 Đăng ký + 6 Transition tiền thẩm định + 4 Edge A4 + 1 A6 fill)
