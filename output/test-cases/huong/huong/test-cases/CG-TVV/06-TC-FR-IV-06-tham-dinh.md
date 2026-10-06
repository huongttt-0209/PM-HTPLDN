# Test Cases — FR-IV-06: Thẩm định hồ sơ TVV

> **SRS Ref**: FR-IV-06 (UC44), SCR-IV-03 Tab Thẩm định, Entity DANH_GIA_TU_VAN_VIEN, SM-TVV (DANG_THAM_DINH → CHO_PHE_DUYET / YEU_CAU_BO_SUNG / TU_CHOI)
> **Nguồn**: NotebookLM `4dd0675e-a4fa-4ea6-80ae-48e76b3fa264` + LOCAL `srs-fr-04-chuyen-gia-tvv- v3.1.md:484-552`
> **Ngày tạo**: 2026-05-09

---

## A. UI FIELD VERIFICATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-TD-UI-01 | FR-IV-06 / SCR-IV-03 Tab Thẩm định / UI 4 nhóm | Verify Tab Thẩm định form 4 nhóm tiêu chí | cb_nv_tw_01, TVV-TW-400 DANG_THAM_DINH | — | 1. Login cb_nv_tw_01<br>2. Mở chi tiết TVV-TW-400 → tab Thẩm định | **FIELDS (5+ action)**:<br>- Nhóm 1 Pháp lý: radio Đạt / Không đạt (boolean *)<br>- Nhóm 2 Năng lực chuyên môn: star-rating 1-5 (DECIMAL(3,1) step 1, *)<br>- Nhóm 3 Hiệu quả & uy tín: star-rating 1-5 + checkbox "N/A (TVV mới)" cho phép NULL<br>- Nhóm 4 Mạng lưới: radio Có / Không (boolean *)<br>- Kết luận: dropdown DAT / KHONG_DAT / YEU_CAU_BO_SUNG (*)<br>- Lý do: textarea (≥10 ký, conditional khi YEU_CAU_BO_SUNG/KHONG_DAT)<br>- Lĩnh vực: multi-select (CB NV được sửa nếu cần)<br>**ACTIONS**: 4 nút header (D.2.1 design polish): "Yêu cầu bổ sung" / "Trình duyệt" (chỉ khi kết luận DAT) / "Từ chối" / "Lưu nháp" | Happy 🔴 |

## B. Thẩm định 3 kết luận

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-TD-001 | FR-IV-06 / AC1 + Trình duyệt | Happy path DAT + Trình duyệt → CHO_PHE_DUYET | cb_nv_tw_01, TVV-TW-400 DANG_THAM_DINH | nhom1=true, nhom2=4.5, nhom3=4.0, nhom4=true, ket_luan=DAT | 1. Nhập 4 nhóm + DAT<br>2. Click "Trình duyệt"<br>3. Modal MD-TRINH-DUYET confirm<br>4. Verify | **STATE**: DANH_GIA_TU_VAN_VIEN insert (ket_qua_phap_ly=true, diem_nang_luc=4.5, diem_hieu_qua=4.0, tham_gia_mang_luoi=true, ket_luan=DAT, diem_tong_tham_dinh = AVG(4.5,4.0)=4.3); TU_VAN_VIEN.trang_thai = CHO_PHE_DUYET; HO_SO_TU_VAN_VIEN.trang_thai_tham_dinh=DAT, ket_qua_tham_dinh="DAT 4 nhóm"; AUDIT_LOG INSERT<br>**UI**: Toast "Trình duyệt thành công"; Badge update "Chờ phê duyệt"; Notification gửi cb_pd_tw_01 cùng cấp<br>**PERSIST**: Tab "Chờ phê duyệt" SCR-IV-01 cho cb_pd_tw_01 → TVV-TW-400 xuất hiện | Happy 🔴 |
| TC-TD-002 | FR-IV-06 / E1 | Kết luận DAT khi nhóm Pháp lý FALSE → ERR-TD-02 | cb_nv_tw_01 | nhom1=false, ket_luan=DAT | 1. Nhập nhom1=Không đạt<br>2. Chọn DAT<br>3. Click Trình duyệt | API 400 "Không thể kết luận ĐẠT khi nhóm Pháp lý chưa đạt" (NGUYÊN VĂN ERR-TD-02); KHÔNG insert DANH_GIA; KHÔNG chuyển trạng thái | Negative 🔴 |
| TC-TD-003 | FR-IV-06 / YEU_CAU_BO_SUNG | YEU_CAU_BO_SUNG + lý do → chuyển trạng thái + thông báo TVV | cb_nv_tw_01, TVV-TW-401 DANG_THAM_DINH | ket_luan=YEU_CAU_BO_SUNG, ly_do="Thiếu chứng chỉ hành nghề luật sư" | 1. Nhập ly_do ≥10 ký<br>2. Click "Yêu cầu bổ sung"<br>3. Verify | **STATE**: TU_VAN_VIEN.trang_thai = YEU_CAU_BO_SUNG; DANH_GIA_TU_VAN_VIEN insert với ket_luan=YEU_CAU_BO_SUNG + ly_do<br>**UI**: Toast "Đã gửi yêu cầu bổ sung"<br>**PERSIST**: Email gửi TVV/CG (chủ hồ sơ); Notification badge cập nhật | Happy 🔴 |
| TC-TD-004 | FR-IV-06 / E2 | YEU_CAU_BO_SUNG thiếu lý do → ERR-TD-03 | cb_nv_tw_01 | ly_do: "" | 1. Click "Yêu cầu bổ sung" không nhập lý do | Inline error "Lý do yêu cầu bổ sung là bắt buộc" (NGUYÊN VĂN ERR-TD-03); KHÔNG submit | Negative 🟡 |
| TC-TD-005 | FR-IV-06 / Lý do <10 ký | YEU_CAU_BO_SUNG lý do <10 ký → ERR-TD-03 | cb_nv_tw_01 | ly_do: "thieu" (5 ký) | 1. Nhập 5 ký<br>2. Submit | Inline error "Lý do yêu cầu bổ sung là bắt buộc" (NGUYÊN VĂN ERR-TD-03 — SRS line 539; SRS không có "(≥10 ký)" trong text. SPEC-CLARIFY-CGTVV-26: SRS có ràng buộc ≥10 ký không? Field định nghĩa trong Inputs row 6 nói "Bắt buộc nếu YEU_CAU_BO_SUNG hoặc KHONG_DAT (≥ 10 ký tự)" — nhưng ERR text thiếu. Tester verify message exact match SRS) | Negative 🟡 |
| TC-TD-006 | FR-IV-06 / KHONG_DAT | KHONG_DAT + lý do → TU_CHOI + thông báo TVV | cb_nv_tw_01, TVV-TW-402 DANG_THAM_DINH | ket_luan=KHONG_DAT, ly_do="Không đáp ứng tiêu chí năng lực chuyên môn" | 1. Click "Từ chối" với lý do<br>2. Verify | **STATE**: TU_VAN_VIEN.trang_thai=TU_CHOI; DANH_GIA_TU_VAN_VIEN insert với KHONG_DAT + ly_do; AUDIT_LOG<br>**UI**: Toast "Đã từ chối"; Notification gửi TVV/CG (chủ hồ sơ) | Happy 🔴 |
| TC-TD-007 | FR-IV-06 / E3 | Trình duyệt khi kết luận khác DAT → ERR-TD-04 | cb_nv_tw_01 | ket_luan=KHONG_DAT, click Trình duyệt | 1. KHONG_DAT + Trình duyệt | API 400 "Chỉ trình duyệt khi kết luận ĐẠT" (NGUYÊN VĂN ERR-TD-04) | Negative 🟡 |
| TC-TD-008 | FR-IV-06 / Nhóm 3 N/A | Nhóm 3 Hiệu quả NULL (TVV mới) → DAT vẫn OK | cb_nv_tw_01, TVV-TW-403 mới (chưa có VV) | nhom1=true, nhom2=4.0, nhom3=NULL (check N/A), nhom4=true | 1. Check "N/A" nhóm 3<br>2. Trình duyệt | DANH_GIA insert với diem_hieu_qua=NULL, diem_tong_tham_dinh=4.0 (chỉ AVG nhóm 2 vì nhóm 3 NULL bỏ qua); STATE: CHO_PHE_DUYET | Edge 🔴 |
| TC-TD-009 | FR-IV-06 / Boundary 1.0 | Nhóm 2 boundary low diem=1.0 | cb_nv_tw_01 | nhom2=1.0 | 1. Star-rating tới mức 1<br>2. Submit | Insert OK (CHECK BETWEEN 1.0 AND 5.0); diem_tong tính bao gồm 1.0 | Edge 🟡 |
| TC-TD-010 | FR-IV-06 / Boundary 5.0 | Nhóm 2 boundary high diem=5.0 | cb_nv_tw_01 | nhom2=5.0 | 1. Star-rating 5<br>2. Submit | Insert OK | Edge 🟡 |
| TC-TD-011 | FR-IV-06 / Out of range | Nhóm 2 ngoài thang (DevTools tamper 6.0) → reject | cb_nv_tw_01 | nhom2=6.0 (DevTools) | 1. Tamper request<br>2. Submit | API 400 "Điểm phải từ 1.0 đến 5.0" — SPEC-CLARIFY-CGTVV-03 nếu SRS không có ERR code | Negative 🟡 |
| TC-TD-012 | FR-IV-06 / Round-half-up | diem_tong AVG round-half-up | cb_nv_tw_01 | nhom2=4.5, nhom3=4.6 | 1. Submit | diem_tong_tham_dinh = (4.5+4.6)/2 = 4.55 → round-half-up = 4.6 (1 chữ số thập phân) | Edge 🟡 |
| TC-TD-013 | FR-IV-06 / Sửa lĩnh vực | CB NV sửa lĩnh vực chuyên môn khi thẩm định | cb_nv_tw_01, TVV-TW-404 LV ban đầu [Lao động] | linh_vuc_ids: [Lao động, Đầu tư] | 1. Tab Thẩm định sửa LV thêm "Đầu tư"<br>2. Submit Trình duyệt | TVV_LINH_VUC junction insert "Đầu tư"; AUDIT_LOG diff [Lao động] → [Lao động, Đầu tư] | Happy 🟡 |
| TC-TD-014 | FR-IV-06 / Auto chuyển CHO_THAM_DINH→DANG_THAM_DINH | Tab Thẩm định mở khi CHO_THAM_DINH → ngầm chuyển DANG_THAM_DINH | cb_nv_tw_01, TVV-TW-405 CHO_THAM_DINH | — | 1. Mở chi tiết TVV-TW-405<br>2. Click "Bắt đầu thẩm định" (D.2.1 — gộp 1 thao tác) | TU_VAN_VIEN.trang_thai chuyển CHO_THAM_DINH → DANG_THAM_DINH (ngầm theo step 1 của Processing FR-IV-06 + D.2.1); ngay_tiep_nhan=NOW; KHÔNG có nút riêng "Tiếp nhận" | Happy 🔴 |
| TC-TD-015 | FR-IV-06 / Lưu nháp | Lưu nháp partial fill → KHÔNG đổi trạng thái | cb_nv_tw_01 | nhom1=true, nhom2=3.0, các nhóm khác trống | 1. Nhập 1 phần<br>2. Click "Lưu nháp" | DANH_GIA_TU_VAN_VIEN KHÔNG insert (hoặc draft flag); TU_VAN_VIEN.trang_thai vẫn DANG_THAM_DINH; SPEC-CLARIFY-CGTVV-04 nếu SRS không quy định Lưu nháp | Edge 🟡 |

---

**Tổng số TC**: 16 (1 UI + 15 thẩm định) — A4/A6 sẽ điều chỉnh
