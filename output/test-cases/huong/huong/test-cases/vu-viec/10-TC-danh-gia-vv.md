# Test Cases — UC67: Đánh giá kết quả hỗ trợ Vụ việc (FR-V.I-17)

> **SRS Ref**: FR-V.I-17 (srs-fr-05:1164-1228), SCR-V.I-03 (Accordion 8 — Đánh giá), Entity DANH_GIA_VU_VIEC, BR-AUTH-08 (srs-fr-05:2391), BR-CALC-06 (srs-fr-05:2481)
> **Ngày tạo**: 2026-05-06 (BMAD A3) · **A7 filter applied**: 2026-05-06
> **Tài khoản chính**: `cb_nv_tw_01` (CB NV scope đơn vị TW), `cb_nv_tw_02` (CB NV TW khác — concurrent), `dn_01` (DN scope AG — chủ sở hữu VV), `cb_pd_tw_01` (role PD — chặn role check)
> **A7 note**: BR-CALC-06 cập nhật điểm TVV TB chỉ verify GIÁN TIẾP qua trigger (cross sang FR-IV-CROSS-01) — không có UI bridge trong UC67 nên KHÔNG tạo TC verify giá trị diem_danh_gia_tb (chuyển trách nhiệm sang FR-IV TC suite). UC67 chỉ verify entry DANH_GIA_VU_VIEC + transition VV → DA_DANH_GIA.

---

## A. UI FIELD VERIFICATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-VV-DG-UI-01 | FR-V.I-17 / SCR-V.I-03 Accordion 8 | Verify form đánh giá UC67: 3 slider điểm + 1 textarea + diem_tong auto-calc | `cb_nv_tw_01`. VV-X ở HOAN_THANH thuộc đơn vị user. Mở SCR-V.I-03 → expand Accordion 8 "Đánh giá". | — | 1. Quan sát form mặc định. 2. Set diem_chat_luong=8, diem_thoi_gian=7, diem_thai_do=9. 3. Quan sát diem_tong. 4. Quan sát textarea nhan_xet. | **UI**: (1) 3 slider/input số 0-10 cho diem_chat_luong / diem_thoi_gian / diem_thai_do, label rõ ràng (srs-fr-05:1184-1186). (2) Field diem_tong hiển thị `8.0` (read-only, AVG = (8+7+9)/3 = 8.0) — auto-calc realtime, không edit tay (srs-fr-05:1187). (3) Textarea nhan_xet không bắt buộc, max 2000 ký tự, có counter "{n}/2000" (srs-fr-05:1188). (4) Nút [Lưu đánh giá] disable khi 3 điểm chưa nhập đủ. | Happy | P1 |
| TC-VV-DG-UI-02 | FR-V.I-17 / role-based render | Verify form chỉ hiện cho role CB_NV và DN; CB PD/NHT/QTHT KHÔNG thấy | `cb_pd_tw_01` (role PD). VV-X ở HOAN_THANH. Mở SCR-V.I-03. | — | 1. Mở Accordion 8 với role PD. 2. Repeat với role NHT (giả lập). | **UI**: Accordion 8 hiển thị bản ghi DG đã có (read-only) nhưng KHÔNG có form nhập (role ∉ {CB_NV, DN} per srs-fr-05:1177). Hoặc hiển thị banner "Vai trò của bạn không có quyền đánh giá vụ việc". | Happy | P1 |

---

## B. CRUD HAPPY PATH

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-VV-DG-101 | FR-V.I-17 AC1 | CB NV đánh giá VV ở HOAN_THANH thành công → VV chuyển DA_DANH_GIA | `cb_nv_tw_01`. VV-X ở HOAN_THANH thuộc don_vi_id của user. Chưa có entry DANH_GIA_VU_VIEC. | diem_chat_luong=9, diem_thoi_gian=8, diem_thai_do=10, nhan_xet="DN hợp tác tốt, hồ sơ đầy đủ" | 1. Mở Accordion 8. 2. Nhập 3 điểm + nhận xét. 3. Click [Lưu đánh giá]. | **STATE**: Backend INSERT DANH_GIA_VU_VIEC (vu_viec_id, loai_nguoi_danh_gia='CB_NV', 3 điểm, diem_tong=9.0, nhan_xet) (srs-fr-05:1200). UPDATE VU_VIEC.trang_thai HOAN_THANH → DA_DANH_GIA (srs-fr-05:1201 — lần đầu). **UI**: Toast success. Stepper VV cập nhật state DA_DANH_GIA. Form chuyển read-only hiển thị giá trị đã lưu + label "Bạn đã đánh giá lúc dd/mm HH:mm". **PERSIST**: AUDIT_LOG / LICH_SU_VU_VIEC entry hanh_dong='DANH_GIA', vai_tro='CB_NV' (srs-fr-05:1203). Verify GET /vu-viec/{id}/lich-su trả entry mới (`list_network_requests`). | Happy | P0 |
| TC-VV-DG-102 | FR-V.I-17 AC1 / role DN | DN đánh giá VV của chính mình thành công | `dn_01`. VV-Y ở HOAN_THANH thuộc doanh_nghiep_id của dn_01. Chưa có DG. Login chuyên trang DN (Tier 2 VNeID, OTP=666666). | diem_chat_luong=10, diem_thoi_gian=9, diem_thai_do=10, nhan_xet="Cảm ơn cán bộ rất nhiệt tình" | 1. DN mở SCR-V.I-03 chế độ DN VV-Y. 2. Mở Accordion Đánh giá. 3. Submit form. | **STATE**: Backend scope check `VU_VIEC.doanh_nghiep_id = current_user.doanh_nghiep_id` (srs-fr-05:1195) → pass. INSERT DANH_GIA_VU_VIEC với loai_nguoi_danh_gia='DN'. UPDATE VV → DA_DANH_GIA. **UI**: Toast success. Form lock read-only. **PERSIST**: 1 entry DG role='DN'. AUDIT_LOG entry. | Happy | P0 |
| TC-VV-DG-103 | FR-V.I-17 / 2 entry độc lập | CB NV + DN cùng đánh giá 1 VV → 2 entry DG độc lập (UNIQUE per role) | TC-VV-DG-101 done (CB NV đã DG, VV ở DA_DANH_GIA). | DN đánh giá: diem_chat_luong=8, diem_thoi_gian=8, diem_thai_do=8 | 1. `dn_01` login chuyên trang DN. 2. Mở VV-X. 3. Submit form đánh giá. | **STATE**: Backend duplicate check key=(vu_viec_id, loai_nguoi_danh_gia='DN') → KHÔNG trùng (CB_NV và DN là 2 loại khác nhau, UNIQUE constraint per role per VV — srs-fr-05:1198). INSERT entry mới role='DN'. VV vẫn DA_DANH_GIA (srs-fr-05:1201 — không transition lần 2, giữ nguyên). **UI**: Toast success. **PERSIST**: 2 entry DANH_GIA_VU_VIEC (1 CB_NV + 1 DN) cho cùng VV-X. AUDIT_LOG 2 entry. | Happy | P0 |
| TC-VV-DG-104 | FR-V.I-17 Inputs#5 / auto-calc | Verify diem_tong = AVG(3 điểm) auto-calc realtime, làm tròn 1 chữ số | `cb_nv_tw_01`. VV-Z ở HOAN_THANH. | Case 1: 7+8+9 → 8.0; Case 2: 6+7+8 → 7.0; Case 3: 5+5+6 → 5.33 (boundary làm tròn) | 1. Nhập case 1 → quan sát diem_tong. 2. Đổi sang case 2. 3. Đổi sang case 3. | **UI**: Realtime update diem_tong khi 3 điểm thay đổi (debounce 200-300ms hoặc sync). Case 1=8.0, Case 2=7.0, Case 3=5.3 hoặc 5.33 (verify rounding behavior — SPEC-CLARIFY-VV-DG-01 nếu SRS không quote precision). Field diem_tong **disabled** không cho gõ. **STATE**: Submit → BE re-tính diem_tong, không tin client value (srs-fr-05:1199). | Happy | P1 |
| TC-VV-DG-105 | FR-V.I-17 / boundary điểm 0 và 10 | Boundary điểm 0 (min) và 10 (max) hợp lệ | `cb_nv_tw_01`. VV-W ở HOAN_THANH. | Submit 1: 0+0+0=0.0. Submit 2 (VV khác): 10+10+10=10.0. | 1. Submit case min. 2. Submit case max. | **STATE**: Backend accept boundary inclusive (0 ≤ x ≤ 10, srs-fr-05:1184-1186). INSERT thành công cả 2 case. **UI**: Toast success. **PERSIST**: Entry DG diem_tong=0.0 và 10.0. | Happy | P1 |

---

## C. NEGATIVE — VALIDATION ERRORS

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-VV-DG-201 | ERR-DG-VV-01 / SM-VUVIEC | Đánh giá VV chưa HOAN_THANH (VV ở DANG_XU_LY) | `cb_nv_tw_01`. VV ở DANG_XU_LY. | diem_chat_luong=8, diem_thoi_gian=8, diem_thai_do=8 | 1. Mở SCR-V.I-03 VV. 2. Quan sát Accordion 8. 3. Nếu hiện form → submit. (Best-case: form ẩn / readonly khi VV chưa HOAN_THANH.) | **STATE**: Backend reject với ERR-DG-VV-01 (srs-fr-05:1218). PRE-02 VV ∈ {HOAN_THANH, DA_DANH_GIA} fail. **UI**: Form ẩn hoặc disabled. Nếu user bypass FE submit → toast error nguyên văn "Vụ việc chưa hoàn thành" (ERR-DG-VV-01). **PERSIST**: KHÔNG entry DG. | Negative | P0 |
| TC-VV-DG-202 | ERR-DG-VV-02 / boundary < 0 | Điểm < 0 (vd -1) → reject | `cb_nv_tw_01`. VV ở HOAN_THANH. | diem_chat_luong=-1, diem_thoi_gian=5, diem_thai_do=5 | 1. Submit form với diem_chat_luong=-1 (bypass FE clamp bằng DevTools sửa value). | **STATE**: Backend reject ERR-DG-VV-02 (srs-fr-05:1219). **UI**: Hoặc client clamp [0,10] (input không cho nhập âm); hoặc submit → toast error nguyên văn "Điểm phải từ 0 đến 10". **PERSIST**: KHÔNG entry. | Negative | P0 |
| TC-VV-DG-203 | ERR-DG-VV-02 / boundary > 10 | Điểm > 10 (vd 11) → reject | `cb_nv_tw_01`. VV ở HOAN_THANH. | diem_chat_luong=11, diem_thoi_gian=5, diem_thai_do=5 | 1. Submit form bypass FE. | **STATE**: Backend reject ERR-DG-VV-02. **UI**: Toast error "Điểm phải từ 0 đến 10". **PERSIST**: KHÔNG entry. | Negative | P0 |
| TC-VV-DG-204 | ERR-DG-VV-03 / UNIQUE | CB NV đánh giá lần 2 cùng VV (cùng role) → ERR-DG-VV-03 | TC-VV-DG-101 done. `cb_nv_tw_01` đã có entry DG cho VV-X. | Submit lần 2: 5+5+5=5.0 | 1. Mở Accordion 8 lần 2. 2. Nếu form vẫn cho submit → click Lưu. | **STATE**: Backend duplicate check UNIQUE(vu_viec_id, loai_nguoi_danh_gia='CB_NV') trùng → reject (srs-fr-05:1198). ERR-DG-VV-03. **UI**: Best-case form lock read-only sau lần đầu (verify FE behavior). Nếu submit → toast error nguyên văn "Bạn đã đánh giá vụ việc này rồi" (ERR-DG-VV-03 srs-fr-05:1220). **PERSIST**: vẫn 1 entry DG (KHÔNG ghi đè). | Negative | P0 |
| TC-VV-DG-205 | ERR-DG-VV-04 / BR-AUTH-08 DN khác | DN đánh giá VV của DN khác → ERR-DG-VV-04 | `dn_01` (DN AG). VV-K thuộc `dn_02` (DN khác). VV-K ở HOAN_THANH. | diem_chat_luong=5, diem_thoi_gian=5, diem_thai_do=5 | 1. `dn_01` cố mở `/ho-so-cua-toi/vu-viec/{VV-K-id}` qua sửa URL. 2. Hoặc bypass FE submit POST /vu-viec/{VV-K}/danh-gia. | **STATE**: Backend scope check `VU_VIEC.doanh_nghiep_id = current_user.doanh_nghiep_id` fail (srs-fr-05:1195). Reject ERR-DG-VV-04 (srs-fr-05:1221). **UI**: 403 + redirect SCR-V.I-04, hoặc toast error nguyên văn "Bạn không có quyền đánh giá vụ việc này (DN khác/đơn vị khác)". **PERSIST**: KHÔNG entry DG. AUDIT_LOG ghi attempt 403 (best practice). | Negative | P0 |
| TC-VV-DG-206 | ERR-DG-VV-04 / BR-AUTH-08 đơn vị khác | CB NV đơn vị A đánh giá VV của đơn vị B → ERR-DG-VV-04 | `cb_nv_bn_01` (CB NV scope đơn vị BN). VV-M thuộc đơn vị DP-AG. VV-M ở HOAN_THANH. | diem_chat_luong=5, diem_thoi_gian=5, diem_thai_do=5 | 1. CB NV BN cố submit DG VV-M qua bypass FE (BR-AUTH-02 ngang cấp KHÔNG thấy nhau). | **STATE**: Backend scope `VU_VIEC.don_vi_id = user.don_vi_id` fail. Reject ERR-DG-VV-04. **UI**: 403/toast error. **PERSIST**: KHÔNG entry DG. | Negative | P0 |
| TC-VV-DG-207 | BR-EC-13 / XSS nhan_xet | XSS payload trong nhan_xet | `cb_nv_tw_01`. VV-N ở HOAN_THANH. | nhan_xet=`<script>alert('XSS-DG-VV')</script><img src=x onerror=alert(2)>` | 1. Submit form với XSS payload. 2. Sau lưu, refresh trang đọc lại DG. | **STATE**: Backend sanitize HTML trước khi store (whitelist tag — strip `<script>`, `onerror`, etc.). **UI**: Sau lưu, render nhan_xet trên Accordion 8 → KHÔNG execute script (`list_console_messages` clean, không alert popup). Raw text escaped hiển thị literal hoặc clean. **PERSIST**: BE store sanitized text. **CRITICAL**: Vì nhan_xet có thể hiện cho DN/PD đọc → XSS persistent = nguy cơ session hijack. | Negative | P0 |
| TC-VV-DG-208 | FR-V.I-17 Inputs#6 / boundary nhan_xet 2000 | Boundary nhan_xet 2000 ký tự (max) và 2001 (over) | `cb_nv_tw_01`. VV ở HOAN_THANH. | nhan_xet="A"×2000 (boundary), nhan_xet="A"×2001 (over) | 1. Submit case 2000. 2. Submit case 2001 (VV khác). | **STATE**: 2000 → INSERT OK (boundary inclusive). 2001 → BE reject hoặc client maxlength truncate xuống 2000. **UI**: 2000 → success; 2001 → toast error/inline "Nhận xét tối đa 2000 ký tự" (SRS Gap message — mark **SPEC-CLARIFY-VV-DG-02**). **PERSIST**: 2000 record OK; 2001 KHÔNG record / record cắt 2000. | Negative | P1 |

---

## D. EDGE CASES

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-VV-DG-301 | FR-V.I-17 srs-fr-05:1201 / state machine | Đánh giá lần 2 cùng VV khác role (DN sau khi CB NV) → VV vẫn DA_DANH_GIA (không transition lần 2) | TC-VV-DG-103 setup. CB NV đã DG VV-X (VV → DA_DANH_GIA). DN đánh giá tiếp. | DN: 7+7+7=7.0 | 1. `dn_01` submit DG. 2. Verify trang_thai VV. | **STATE**: Backend INSERT entry DG role='DN'. State transition logic: VV đã DA_DANH_GIA → giữ nguyên (srs-fr-05:1201 "chỉ lần đánh giá đầu tiên transition; nếu VV đã DA_DANH_GIA thì giữ nguyên"). **UI**: Stepper vẫn DA_DANH_GIA. **PERSIST**: 2 DG entry. AUDIT_LOG entry vai_tro='DN'. KHÔNG có duplicate entry LICH_SU_VU_VIEC `STATE_CHANGE` (chỉ ghi lần đầu). | Edge | P1 |
| TC-VV-DG-302 | FR-V.I-17 / VV ở DA_DANH_GIA + role chưa DG | Đánh giá VV ở DA_DANH_GIA bằng role chưa DG (CB NV chưa đánh giá, DN đã đánh giá trước) | DN đã DG VV-Q (VV ở DA_DANH_GIA). CB NV chưa DG. `cb_nv_tw_01`. | CB NV: 8+8+8=8.0 | 1. CB NV mở Accordion 8. 2. Submit form. | **STATE**: Backend PRE-02 check VV ∈ {HOAN_THANH, DA_DANH_GIA} → pass (srs-fr-05:1176). Duplicate check role=CB_NV không trùng → INSERT OK. VV giữ DA_DANH_GIA. **UI**: Form vẫn hiện cho CB NV (vì entry DG của role CB_NV chưa có). Toast success sau submit. **PERSIST**: 2 DG entry (1 DN + 1 CB_NV). | Edge | P0 |
| TC-VV-DG-303 | BR-CALC-06 / cross FR-IV trigger gián tiếp | Verify TVV.diem_danh_gia_tb KHÔNG đổi sau UC67 (UC67 → DANH_GIA_VU_VIEC; TVV trigger từ DANH_GIA_SAU_VU_VIEC FR-IV) | `cb_nv_tw_01`. VV-T có nguoi_xu_ly_id=`tvv_01`. VV ở HOAN_THANH. Trước test: ghi nhận `tvv_01.diem_danh_gia_tb` (qua FR-IV UI nếu có, không qua DB). | CB NV: 9+9+9=9.0 | 1. CB NV submit DG VV-T. 2. Sau 1 phút (cho async trigger nếu có). 3. Mở UI FR-IV xem điểm `tvv_01`. | **STATE**: BR-CALC-06 srs-fr-05:2481 nguyên văn "UC67 chỉ tạo DANH_GIA_VU_VIEC; trigger cập nhật điểm TVV nằm ở **FR-IV-CROSS-01**" — nguồn data là DANH_GIA_SAU_VU_VIEC, KHÔNG phải DANH_GIA_VU_VIEC. **UI**: Sau UC67, `tvv_01.diem_danh_gia_tb` KHÔNG đổi (vì FR-IV trigger không activate). **PERSIST**: 1 entry DANH_GIA_VU_VIEC. KHÔNG có entry DANH_GIA_SAU_VU_VIEC từ flow này. **CRITICAL** (gap-report): Nếu BE nhầm lẫn entity và update từ DANH_GIA_VU_VIEC → bug pollute điểm TVV. | Edge | P1 |
| TC-VV-DG-304 | BR-EC-01 / Optimistic lock concurrent | 2 tab cùng role CB NV submit DG cùng VV → 1 success, 1 fail UNIQUE | Tab1 + Tab2 cùng `cb_nv_tw_01`. VV-S ở HOAN_THANH chưa DG. | Tab1: 8+8+8. Tab2: 5+5+5. | 1. Tab1 fill form. 2. Tab2 (chưa reload) cũng fill form. 3. Tab1 submit. 4. Tab2 submit. | **STATE**: Tab1 SUCCESS — INSERT DG. Tab2 FAIL với UNIQUE constraint conflict (vu_viec_id, loai_nguoi_danh_gia='CB_NV' trùng) → trả ERR-DG-VV-03. **UI**: Tab1 toast success. Tab2 toast error nguyên văn "Bạn đã đánh giá vụ việc này rồi" (srs-fr-05:1220). **PERSIST**: 1 entry duy nhất (Tab1). | Edge | P0 |

---

## Tổng kết file

**Tổng TC: 19** (2 UI + 5 Happy + 8 Negative + 4 Edge) — ổn định sau Codex review 2026-05-09

**Priority**: P0=11 / P1=8

**Coverage:**
- BR: BR-AUTH-01, BR-AUTH-08 (scope DN/đơn vị — TC-205/206), BR-CALC-06 (cross FR-IV — verify gián tiếp KHÔNG đổi — TC-303), BR-DATA-05, BR-EC-01 (TC-304), BR-EC-13 (XSS nhan_xet — TC-207), SM-VUVIEC (HOAN_THANH → DA_DANH_GIA **chỉ lần đầu** — TC-301 explicit verify state không đổi lần 2)
- Error codes: ERR-DG-VV-01/02/03/04 (**full coverage 4/4** srs-fr-05:1218-1221)
- AC SRS: 2/2 (srs-fr-05:1224-1225)
- UNIQUE per role: TC-204 + TC-304 (concurrent)
- 2 entry DG độc lập (CB NV + DN cùng VV): TC-103 + TC-302
- SPEC-CLARIFY: VV-DG-01 (rounding precision diem_tong), VV-DG-02 (nhan_xet boundary 2000 message)

> **Changelog 2026-05-06:**
> - **A3 base 19** — UI 2 + Happy 5 + Negative 8 + Edge 4. Loại verify DB query trực tiếp diem_danh_gia_tb (chuyển FR-IV TC suite per BR-CALC-06 cross-ref).
>
> **Codex review 2026-05-09:**
> - File coverage đã đầy đủ — KHÔNG thêm TC mới
> - Điểm nổi bật: BR-CALC-06 cross-ref handle đúng (UC67 → DANH_GIA_VU_VIEC, KHÔNG pollute TVV averaging via TC-303 negative verify), UNIQUE constraint per role tested, SM transition chỉ lần đầu verified explicit
