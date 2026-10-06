# Test Cases — FR-IV-11 + FR-IV-12: NHT cập nhật thông tin TVV + Cập nhật trạng thái (guard VV+HĐ)

> **SRS Ref**: FR-IV-11 (UC49), FR-IV-12 (UC50), SCR-IV-03 (Tab Hồ sơ + nút header), Entity TU_VAN_VIEN, SM-TVV (HOAT_DONG ↔ TAM_DUNG ↔ VO_HIEU_HOA)
> **Nguồn**: NotebookLM `4dd0675e-a4fa-4ea6-80ae-48e76b3fa264` + LOCAL `srs-fr-04-chuyen-gia-tvv- v3.1.md:808-862 + 866-921`
> **Ngày tạo**: 2026-05-09

---

## A. UI FIELD VERIFICATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-CNTT-UI-01 | FR-IV-11 / SCR-IV-03 Tab Hồ sơ / UI Edit | Verify Tab Hồ sơ form NHT cập nhật thông tin TVV | nht_01, TVV-TW-800 cùng đơn vị HOAT_DONG | — | 1. Login nht_01<br>2. Mở chi tiết → tab Hồ sơ<br>3. Click "Cập nhật thông tin" | **FIELDS**: dia_chi (text), so_dien_thoai (10-11 số), email (RFC 5322), linh_vuc_ids (multi)<br>**Buttons**: Lưu / Hủy<br>**NEGATIVE**: TVV/CG đăng nhập chuyên trang KHÔNG có nút "Cập nhật thông tin" (chỉ NHT cùng đơn vị) | Happy 🔴 |
| TC-CNTT-UI-02 | FR-IV-12 / Modal MD-TAM-DUNG / MD-VO-HIEU-HOA | Verify modal Tạm dừng + Vô hiệu hóa | cb_nv_tw_01, TVV-TW-800 HOAT_DONG | — | 1. Header click "Tạm dừng" → MD-TAM-DUNG<br>2. Verify modal | **MD-TAM-DUNG**: title "Xác nhận tạm dừng?", body với tên TVV, textarea ly_do (≥10 ký *), buttons Tạm dừng / Hủy<br>**MD-VO-HIEU-HOA**: title "Xác nhận vô hiệu hóa?", body cảnh báo "tự động gỡ khỏi Cổng PLQG", textarea ly_do | Happy 🟡 |

## B. FR-IV-11 — NHT cập nhật thông tin TVV

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-CNTT-001 | FR-IV-11 / AC1+AC2 | NHT cập nhật SĐT + email TVV cùng đơn vị | nht_01 (HN), TVV-TW-800 HOAT_DONG | sdt: "0911111111", email: "newemail@example.com" | 1. Click Cập nhật<br>2. Sửa SĐT + email<br>3. Lưu | **STATE**: TU_VAN_VIEN cập nhật fields, updated_at + updated_by; AUDIT_LOG diff old→new<br>**UI**: Toast "Cập nhật thông tin thành công"<br>**PERSIST**: Reload chi tiết → giá trị mới | Happy 🔴 |
| TC-CNTT-002 | FR-IV-11 / E1 ERR-CN-01 | Email không hợp lệ → ERR-CN-01 | nht_01 | email: "invalid" | 1. Submit | "Định dạng email không hợp lệ" (NGUYÊN VĂN ERR-CN-01) | Negative 🟡 |
| TC-CNTT-003 | FR-IV-11 / E2 ERR-CN-02 | NHT khác đơn vị → ERR-CN-02 | nht_HP_01 (HP), TVV-TW-800 (HN) | — | 1. Cố sửa qua DevTools | API 403 "Bạn không có quyền cập nhật hồ sơ tư vấn viên này (khác đơn vị)" (NGUYÊN VĂN ERR-CN-02); UI ẩn nút Cập nhật | Negative 🔴 |
| TC-CNTT-004 | FR-IV-11 / E3 ERR-CN-03 | TVV VO_HIEU_HOA → ERR-CN-03 | nht_01, TVV-TW-801 VO_HIEU_HOA | — | 1. Tab Hồ sơ verify | UI ẩn nút Cập nhật; nếu DevTools force → "Hồ sơ đã bị vô hiệu hóa, không thể chỉnh sửa" (NGUYÊN VĂN ERR-CN-03) | Negative 🟡 |
| TC-CNTT-005 | FR-IV-11 / E4 ERR-CN-04 | Email mới đã tồn tại TVV khác → ERR-CN-04 | nht_01, đã có TVV email "exists@example.com" | email: "exists@example.com" | 1. Submit email trùng | "Email này đã được sử dụng bởi tư vấn viên khác" (NGUYÊN VĂN ERR-CN-04) | Negative 🟡 |
| TC-CNTT-006 | FR-IV-11 / TVV/CG readonly | TVV/CG đăng nhập chuyên trang chỉ xem, KHÔNG sửa | tvv_01, hồ sơ TVV-TW-800 của tvv_01 | — | 1. Login tvv_01 chuyên trang<br>2. Tab Hồ sơ | KHÔNG có nút "Cập nhật thông tin"; banner "Liên hệ Người hỗ trợ pháp lý cùng đơn vị" | Negative 🔴 |

## C. FR-IV-12 — Cập nhật trạng thái (SM-TVV transitions)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-CNTT-101 | FR-IV-12 / HOAT_DONG → TAM_DUNG | Tạm dừng TVV HOAT_DONG | cb_nv_tw_01, TVV-TW-810 HOAT_DONG | ly_do: "TVV xin nghỉ tạm thời 3 tháng" | 1. Header "Tạm dừng" → MD-TAM-DUNG<br>2. Nhập lý do<br>3. Confirm | **STATE**: TU_VAN_VIEN.trang_thai=TAM_DUNG, version+1; AUDIT_LOG action=STATE_CHANGE diff HOAT_DONG→TAM_DUNG<br>**UI**: Toast "Tạm dừng thành công"; Badge cập nhật "Tạm dừng" vàng đậm<br>**PERSIST**: List tab "Tạm dừng" có TVV-TW-810; Notification gửi TVV/CG (chủ hồ sơ) | Happy 🔴 |
| TC-CNTT-102 | FR-IV-12 / TAM_DUNG → HOAT_DONG | Kích hoạt lại TVV TAM_DUNG | cb_nv_tw_01, TVV-TW-811 TAM_DUNG | ly_do: "TVV trở lại làm việc" | 1. Header "Kích hoạt lại"<br>2. Confirm | TU_VAN_VIEN.trang_thai=HOAT_DONG; AUDIT_LOG | Happy 🟡 |
| TC-CNTT-103 | FR-IV-12 / HOAT_DONG → VO_HIEU_HOA + GUARD VV+HĐ | TVV không có VV + HĐ → vô hiệu hóa OK | cb_nv_tw_01, TVV-TW-812 HOAT_DONG, KHÔNG có VU_VIEC + HOI_DAP DANG_XU_LY/CHO_PHE_DUYET | ly_do: "Hết hạn thẻ" | 1. Header "Vô hiệu hóa" → MD-VO-HIEU-HOA<br>2. Confirm | TU_VAN_VIEN.trang_thai=VO_HIEU_HOA; nếu cong_khai=1 → API DELETE Cổng (BR-PUBLIC-02); AUDIT_LOG; Notification realtime gửi TVV/CG | Happy 🔴 |
| TC-CNTT-104 | FR-IV-12 / E2 ERR-TT-02 GUARD VV | TVV có 1 VV DANG_XU_LY → reject | cb_nv_tw_01, TVV-TW-813 HOAT_DONG có 1 VU_VIEC trang_thai=DANG_XU_LY | — | 1. Click Vô hiệu hóa | API 400 "Tư vấn viên đang có 1 vụ việc và 0 hỏi đáp chưa hoàn thành, không thể vô hiệu hóa" (NGUYÊN VĂN ERR-TT-02 với count substitution); KHÔNG cập nhật trạng thái | Negative 🔴 |
| TC-CNTT-105 | FR-IV-12 / GUARD HOI_DAP (mới v3.1) | TVV có 1 HỎI ĐÁP DANG_XU_LY → reject | cb_nv_tw_01, TVV-TW-814 HOAT_DONG có 0 VV + 1 HOI_DAP trang_thai=DANG_XU_LY | — | 1. Click Vô hiệu hóa | API 400 "Tư vấn viên đang có 0 vụ việc và 1 hỏi đáp chưa hoàn thành, không thể vô hiệu hóa" (NGUYÊN VĂN ERR-TT-02); v3.1 thêm guard HOI_DAP (Thay đổi 18) | Negative 🔴 |
| TC-CNTT-106 | FR-IV-12 / TAM_DUNG → VO_HIEU_HOA | Vô hiệu hóa từ TAM_DUNG (cùng guard) | cb_nv_tw_01, TVV-TW-815 TAM_DUNG, không VV/HĐ | — | 1. Click Vô hiệu hóa | TU_VAN_VIEN.trang_thai=VO_HIEU_HOA; AUDIT_LOG | Happy 🟡 |
| TC-CNTT-107 | FR-IV-12 / VO_HIEU_HOA → HOAT_DONG | Khôi phục TVV VO_HIEU_HOA | cb_nv_tw_01, TVV-TW-816 VO_HIEU_HOA | ly_do: "Quyết định khôi phục" | 1. Click "Khôi phục" | TU_VAN_VIEN.trang_thai=HOAT_DONG; AUDIT_LOG | Happy 🟡 |
| TC-CNTT-108 | FR-IV-12 / E1 ERR-TT-01 | Transition không hợp lệ HOAT_DONG → MOI_DANG_KY | cb_nv_tw_01, TVV-TW-817 HOAT_DONG | DevTools call API trang_thai_moi=MOI_DANG_KY | 1. Tamper API | API 400 "Không thể chuyển từ Đang hoạt động sang Mới đăng ký" (NGUYÊN VĂN ERR-TT-01) | Negative 🟡 |
| TC-CNTT-109 | FR-IV-12 / E3 ERR-TT-03 | Cập nhật trạng thái thiếu lý do → ERR-TT-03 | cb_nv_tw_01 | ly_do: "" | 1. Modal MD-TAM-DUNG submit không lý do | "Lý do thay đổi là bắt buộc (≥ 10 ký tự)" (NGUYÊN VĂN ERR-TT-03) | Negative 🟡 |
| TC-CNTT-110 | FR-IV-12 / Lý do <10 ký | Lý do <10 ký → ERR-TT-03 | cb_nv_tw_01 | ly_do: "ngan" | 1. Submit | ERR-TT-03 (NGUYÊN VĂN) | Negative 🟡 |
| TC-CNTT-111 | FR-IV-12 / Push realtime to TVV/CG | Notification realtime nếu TVV/CG đang mở form FR-IV-11 | cb_nv_tw_01, tvv_01 đang mở chuyên trang FR-IV-11 | — | 1. cb_nv_tw_01 vô hiệu hóa<br>2. Verify tvv_01 màn | tvv_01 nhận push realtime banner "Hồ sơ của bạn vừa bị vô hiệu hóa" + form disabled | Edge 🔴 |
| TC-CNTT-112 | FR-IV-12 / SPEC-CLARIFY guard scope HOI_DAP | Verify guard HOI_DAP filter chỉ trạng thái DANG_XU_LY/CHO_PHE_DUYET (không count CONG_KHAI) | cb_nv_tw_01, TVV-TW-818 HOAT_DONG có 1 HOI_DAP CONG_KHAI (đã đóng) | — | 1. Click Vô hiệu hóa | PASS — guard filter chỉ trạng thái xử lý đang dở; HOI_DAP CONG_KHAI không count; SPEC-CLARIFY-CGTVV-06 nếu SRS không list rõ enum | Edge 🟡 |

---

## D. EDGE bổ sung (A4 inline merge — 1 edge)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-CNTT-501 | EDGE-A4-gg / TVV CHO_KICH_HOAT bị vô hiệu hóa | TVV CHO_KICH_HOAT (chưa kích hoạt) bị vô hiệu hóa giữa chừng | cb_nv_tw_01, TVV-TW-820 CHO_KICH_HOAT | ly_do | 1. Vô hiệu hóa TVV CHO_KICH_HOAT | SPEC-CLARIFY-CGTVV-16: SM-TVV không có transition CHO_KICH_HOAT → VO_HIEU_HOA explicit; có thể: (a) Chỉ allow Cancel/Reject (về TU_CHOI?), (b) Allow VO_HIEU_HOA + invalidate TK token, (c) Reject — phải đợi HOAT_DONG; chờ BA clarify | Edge 🔴 |

---

**Tổng số TC**: 17 (2 UI + 6 NHT update + 12 SM transition + 1 Edge A4) — A6 sẽ điều chỉnh
