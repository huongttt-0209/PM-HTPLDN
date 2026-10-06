# Test Cases — Tab 1: Cấu hình SLA (FR-VIII-10 / UC108)

> **SRS Ref**: FR-VIII-10 (srs-fr-10:440-516), SCR-VIII-06 Tab 1 (srs-fr-10:1631-1646), Entity `CAU_HINH_SLA`
> **Ngày tạo**: 2026-05-08 (BMAD A3, A4 inline merge)
> **Tài khoản chính**: `qtht_01` (chỉ QTHT — line 1682)
> **URL:** `/quan-tri/cau-hinh` → Tab 1

> **Pre-condition chung:** `qtht_01` đăng nhập, vào SCR-VIII-06 Tab 1. CAU_HINH_SLA có 4 record seed mặc định (HOI_DAP=5/50/90, VU_VIEC=10/50/90, HO_SO_HT=15/50/90, HO_SO_TT=10/50/90 — line 510-515).

---

## A. HAPPY PATH — READ + VIEW

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-CH-SLA-001 | FR-VIII-10 AC1 (sync CAUHINH-03 — không có cột QH-NT) | QTHT vào Tab 1 — bảng 4 cấu hình SLA seed | `qtht_01`. Seed CAU_HINH_SLA 4 record. | — | 1. Login. 2. Vào `/quan-tri/cau-hinh`. 3. Tab 1 active mặc định (hoặc click). | **STATE**: BE GET `/api/cau-hinh-sla`. **UI**: Bảng 4 dòng ứng với 4 loai_yeu_cau. Cột readonly "Loại YC" (HOI_DAP/VU_VIEC/HO_SO_HT/HO_SO_TT). Cột inline-edit "Thời hạn", "CB1 %", "CB2 %". Cột readonly "Quá hạn (%)" = 100. Toggle "Gửi email" + "Gửi TB app" mặc định ON. **KHÔNG có cột "QH nghiêm trọng (%)" trong UI** (CAUHINH-03 RESOLVED — FR-VIII-10 Inputs line 457-466 không có field này; SCR-VIII-06 #10 là UI spec sai). **Info box** trên đầu hiển thị 4 mức "Bình thường / Sắp hết hạn / Quá hạn / Quá hạn nghiêm trọng" — BR-SLA-02 line 1635 (info-only display, KHÔNG cấu hình được ngưỡng). **Cảnh báo snapshot** (line 1645): "Hồ sơ MỚI áp dụng cấu hình mới. Hồ sơ đang xử lý giữ deadline cũ (snapshot SLA)". **Nút [Lưu cấu hình]**. | Happy | P0 |
| TC-CH-SLA-002 | BR-SLA-01 + Seed Data (CAUHINH-09 RESOLVED 2026-05-08 — BA chốt HOI_DAP=5 ngày) | Verify default values match seed table | `qtht_01`. | — | 1. Tab 1. 2. Quan sát từng dòng. | **UI**: Row HOI_DAP: thoi_han=**5**, CB1=50, CB2=90 (BA chốt — FR-VIII-10 seed line 515 đúng; BR-CALC-03 line 5362 viết 15/30 là **sai**, cần update SRS — KHÔNG ảnh hưởng test). Row VU_VIEC: thoi_han=10, CB1=50, CB2=90. Row HO_SO_HT: thoi_han=15. Row HO_SO_TT: thoi_han=10 (per srs-fr-10:511-515). **PERSIST**: — | Happy | P1 |

---

## B. HAPPY PATH — UPDATE INLINE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-CH-SLA-003 | FR-VIII-10 step 4 + AC3 | Sửa Thời hạn (ngày LV) — VU_VIEC từ 10 → 12 | `qtht_01`. | thoi_han_ngay=12 cho VU_VIEC | 1. Inline edit cell "Thời hạn" row VU_VIEC. 2. Nhập 12. 3. Click [Lưu cấu hình]. | **STATE**: BE PATCH/PUT `/api/cau-hinh-sla/{id}` với `thoi_han_ngay=12`. AUDIT_LOG INSERT `action=UPDATE`, `old=10`, `new=12` (BR-DATA-05). **UI**: Toast success "Lưu cấu hình thành công" hoặc tương đương. Cell hiển thị 12. Reload trang giữ giá trị 12. **PERSIST**: — | Happy | P0 |
| TC-CH-SLA-004 | FR-VIII-10 step 4 | Sửa CB1 + CB2 cùng lúc — HOI_DAP CB1=40, CB2=85 | `qtht_01`. | CB1=40, CB2=85 | 1. Inline edit 2 cell. 2. Save. | **STATE**: BE PATCH với cả 2 field. **UI**: Toast success. Reload giữ giá trị mới. | Happy | P0 |
| TC-CH-SLA-005 | SCR-VIII-06 #11/#12 toggle | Toggle Gửi email OFF — verify scheduled job không gửi mail | `qtht_01`. | gui_email_canh_bao=0 | 1. Toggle OFF cột Gửi email row HO_SO_TT. 2. Save. 3. (Phase B): trigger SLA crossing threshold → verify mail không gửi. | **STATE**: BE PATCH `gui_email_canh_bao=0`. **UI**: Toggle visual chuyển OFF. Reload giữ. **PERSIST**: Phase B verify scheduled job không gửi. | Happy | P1 |
| TC-CH-SLA-006 | CAUHINH-03 RESOLVED (theo business — KHÔNG có field QH-NT) | **Verify cột "QH nghiêm trọng (%)" KHÔNG xuất hiện trong UI Tab 1** | `qtht_01`. | — | 1. Tab 1. 2. Quan sát header bảng SLA. 3. Đếm số cột. | **STATE**: — (UI scan). **UI**: Header bảng có **đúng các cột theo FR-VIII-10 Inputs** (line 457-466): Loại YC / Tên loại / Thời hạn ngày / CB1 % / CB2 % / Quá hạn % / Gửi email / Gửi TB app. **KHÔNG có cột QH nghiêm trọng (%) 200%.** SCR-VIII-06 #10 thêm cột QH-NT là UI spec chưa khớp business schema → **nếu UI render cột QH-NT → BUG implementation thừa field**. **PERSIST**: — | Negative | P1 |
| TC-CH-SLA-007 | A6 fill A5-GAP-CH-01 + FR-VIII-10 AC2 | Thêm cấu hình SLA cho loại YC mới (nếu có nút Add new) | `qtht_01`. | loai_yeu_cau="DOI_TAI_KHOAN", ten_loai="Đổi tài khoản", thoi_han_ngay=7, CB1=50, CB2=90 | 1. Click [+ Thêm cấu hình SLA] (nếu có). 2. Modal/Form. 3. Fill + Save. | **STATE**: Tùy implementation: (a) Nếu UI inline-only 4 record fixed → KHÔNG có nút Add new (verify SPEC-CLARIFY: spec FR-VIII-10 input #1 nói loai_yeu_cau UNIQUE = 4 giá trị enum HOI_DAP/VU_VIEC/HO_SO_HT/HO_SO_TT — line 459); (b) Nếu có Add new → BE INSERT new record. **UI**: Verify behavior thực tế. **PERSIST**: AUDIT_LOG CREATE nếu thành công. Note: AC2 SRS line 505 nói "Thêm mới cấu hình" nhưng schema chỉ có 4 enum value cố định — mâu thuẫn nội bộ SRS. | Edge | P1 |
| TC-CH-SLA-008 | A6 fill A5-GAP-CH-02 + ERR-SLA-03 | loai_yeu_cau duplicate khi Add new | `qtht_01`. | loai_yeu_cau="VU_VIEC" (đã có) | 1. Click [+ Thêm cấu hình SLA]. 2. Chọn VU_VIEC. 3. Save. | **STATE**: BE check unique. **UI**: Toast ERROR nguyên văn "Loại yêu cầu đã có cấu hình SLA" (srs-fr-10:501). KHÔNG persist. (TC này chỉ apply nếu TC-007 verify có nút Add new — paired.) | Negative | P1 |
| TC-CH-SLA-009 | A6 fill A5-GAP-CH-03 + SCR-VIII-06 #12 | Toggle gui_thong_bao_app OFF — verify scheduled job không gửi TB in-app | `qtht_01`. | gui_thong_bao_app=0 | 1. Toggle OFF cột "Gửi TB app" row VU_VIEC. 2. Save. 3. (Phase B): trigger SLA crossing → quan sát THONG_BAO không có entry. | **STATE**: BE PATCH `gui_thong_bao_app=0`. **UI**: Toggle visual OFF. Reload giữ. **PERSIST**: Phase B verify scheduled job (FR-II-CROSS-01 cron 30 phút) không INSERT THONG_BAO khi crossing. | Happy | P1 |

---

## C. NEGATIVE — VALIDATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-CH-SLA-010 | ERR-SLA-01 (E1) | thoi_han_ngay = 0 → reject | `qtht_01`. | thoi_han_ngay=0 | 1. Inline edit thoi_han = 0. 2. Save. | **STATE**: BE reject. **UI**: Inline error/toast nguyên văn "Thời hạn xử lý phải là số nguyên dương" (srs-fr-10:499). Cell highlight đỏ. KHÔNG persist. **PERSIST**: GET reload giá trị cũ. | Negative | P0 |
| TC-CH-SLA-011 | ERR-SLA-01 boundary | thoi_han_ngay = -1 → reject | `qtht_01`. | thoi_han_ngay=-1 | 1. Inline edit -1. 2. Save. | Same TC-010 message. | Negative | P0 |
| TC-CH-SLA-012 | ERR-SLA-02 (E2) | CB1 >= CB2 (CB1=80, CB2=70) → reject | `qtht_01`. | CB1=80, CB2=70 | 1. Edit. 2. Save. | **STATE**: BE reject. **UI**: Toast nguyên văn "Mức cảnh báo 1 phải nhỏ hơn mức cảnh báo 2" (srs-fr-10:500). KHÔNG persist. | Negative | P0 |
| TC-CH-SLA-013 | ERR-SLA-02 boundary | CB1 = CB2 (CB1=50, CB2=50) → reject | `qtht_01`. | CB1=50, CB2=50 | 1. Edit. 2. Save. | Same TC-012 message (validate `CB1 < CB2` strict, line 463). | Negative | P0 |
| TC-CH-SLA-014 | FR-VIII-10 step 2 | CB2 >= 100 → reject (line 463 `CB2 < 100`) | `qtht_01`. | CB1=50, CB2=100 | 1. Edit. 2. Save. | **STATE**: BE reject. **UI**: Toast (verify spec — có thể ERR-SLA-02 hoặc message riêng). | Negative | P0 |
| TC-CH-SLA-015 | FR-VIII-10 input #1 | thoi_han_ngay = chuỗi "abc" → reject (type) | `qtht_01`. | thoi_han_ngay="abc" | 1. Inline paste. 2. Blur cell. | **UI**: Inline validate `type=number`. Cell reject input non-numeric ngay (HTML5 input type number). KHÔNG submit BE. | Negative | P1 |

---

## D. SNAPSHOT BEHAVIOR (đặc thù v3.1 — line 492-493, 1645)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-CH-SLA-020 | FR-VIII-10 Postcondition + line 1645 (A4 merged) | **Snapshot pattern: HS đang xử lý giữ deadline cũ khi sửa SLA** | `qtht_01`. Seed: 1 HS VU_VIEC state DANG_XU_LY tạo trước khi sửa SLA, deadline = today + 10 ngày LV. | thoi_han_ngay VU_VIEC: 10 → 15 | 1. Sửa SLA VU_VIEC từ 10 → 15. 2. Save. 3. Mở HS đó (qua menu Vụ việc). 4. Quan sát deadline. | **STATE**: HS giữ deadline `today + 10` (snapshot SLA cũ). **UI**: Field deadline trên HS KHÔNG đổi sau save SLA. Alert v3.1 trên Tab 1 confirm ngay. **PERSIST**: HS deadline không match config mới (15 ngày) → đúng spec snapshot. | Edge | P0 |
| TC-CH-SLA-021 | FR-VIII-10 Postcondition (A4 merged) | **Snapshot pattern: HS tạo MỚI sau save áp config mới** | `qtht_01`. Sửa SLA VU_VIEC 10→15 (TC-020). | — | 1. Sau khi save, tạo HS VU_VIEC mới (qua FR-V.I-03 Nhập thủ công). 2. Quan sát deadline HS mới. | **STATE**: HS mới có deadline `today + 15` (config mới). **UI**: Field deadline = today + 15. **PERSIST**: BR-CALC-03 áp dụng config mới cho HS mới. | Edge | P0 |
| TC-CH-SLA-022 | SPEC-CLARIFY-CAUHINH-07 (A4 merged) | **Race condition: tạo HS cùng giây với save SLA** | `qtht_01` + 2nd user CB_NV. | Concurrent | 1. Mở 2 tab: tab 1 QTHT đang sửa SLA; tab 2 CB_NV mở form tạo HS. 2. QTHT click Save (T0). 3. CB_NV click Submit HS (T0+ε). | **STATE**: Tùy implementation — HS có thể áp config cũ hoặc mới. **UI**: Verify behavior — log SPEC-CLARIFY-CAUHINH-07 với BA. **PERSIST**: Phase B verify thực tế. | Edge | P2 |

---

## E. PERMISSION + AUTH

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-CH-SLA-030 | line 1682 + BR-AUTH-01 | CB_NV_TW không thấy Tab 1 (tab gating) | `cb_nv_tw_01`. | — | 1. Login. 2. Vào `/quan-tri/cau-hinh`. | **STATE**: BE check role. **UI**: Tab 1 ẨN — chỉ thấy Tab 3. KHÔNG thấy "Thời hạn xử lý / SLA" trong tab list. **PERSIST**: — | Negative | P0 |
| TC-CH-SLA-031 | BR-AUTH-01 + Tab gating | CB_PD_TW không thấy Tab 1 | `cb_pd_tw_01`. | — | 1. Login. 2. URL direct Tab 1 (param `?tab=1`). | **STATE**: BE reject hoặc redirect. **UI**: Tab 1 ẨN. URL direct → fallback Tab 3 hoặc 403. | Negative | P0 |
| TC-CH-SLA-032 | BR-AUTH-01 Tier 2 | DN không vào được CMS | `dn_01`. | — | 1. URL direct CMS. | **STATE/UI**: 403 hoặc redirect Cổng PLQG. | Negative | P0 |

---

## F. SECURITY & EDGE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-CH-SLA-040 | BR-EC-01 (A4 merged) | Optimistic locking — 2 QTHT sửa cùng record | `qtht_01` + `qtht_02`. | Concurrent edit | 1. 2 tab QTHT. 2. Cả 2 mở Tab 1, sửa thoi_han VU_VIEC. 3. QTHT_01 save trước (T0). 4. QTHT_02 save sau (T0+ε). | **STATE**: BE reject save thứ 2 với 409 Conflict (BR-EC-01). **UI**: Toast WARNING "Cấu hình đã được sửa bởi người khác. Vui lòng tải lại." (verify text). **PERSIST**: Save đầu tiên thắng. | Edge | P0 |
| TC-CH-SLA-041 | A4 boundary | thoi_han_ngay = 999 (giá trị lớn) | `qtht_01`. | thoi_han_ngay=999 | 1. Edit. 2. Save. | **STATE**: BE accept (spec không có upper bound). **UI**: Toast success. **PERSIST**: HS mới có deadline today + 999 ngày LV. | Edge | P2 |
| TC-CH-SLA-042 | A4 boundary | thoi_han_ngay = 1 (min hợp lệ) | `qtht_01`. | thoi_han_ngay=1 | Same. | **STATE**: BE accept (> 0). **UI**: Toast success. | Edge | P1 |
| TC-CH-SLA-043 | BR-DATA-05 (A4 merged) | Audit log ghi chi tiết old → new khi sửa SLA | `qtht_01`. Sau TC-003 (10→12). | — | 1. Vào Nhật ký HT (W1.1). 2. Filter `entity=CAU_HINH_SLA`. 3. Quan sát log mới. | **STATE**: AUDIT_LOG có record `entity=CAU_HINH_SLA`, `chi_tiet={"field":"thoi_han_ngay","old":10,"new":12}`. **UI**: Cột chi tiết JSON expand thấy đúng giá trị. **PERSIST**: BR-DATA-05 verified. | Edge | P1 |

---

## Tổng số TC: 27 (8 Happy + 7 Negative + 3 Snapshot + 3 Permission + 4 Security/Edge + 2 READ) — A3 base + A4 merged + A6 fill 3
**Priority**: P0=11 / P1=12 / P2=4

**Coverage:**
- BR: BR-AUTH-01, BR-DATA-05, BR-SLA-01, BR-SLA-02, BR-EC-01 (TC-040), BR-CALC-03 (TC-021)
- AC SRS: AC1 (TC-001), AC2 (TC-007 — A6 fill, paired SPEC-CLARIFY), AC3 (TC-003-004)
- Error codes: ERR-SLA-01 (TC-010, 011), ERR-SLA-02 (TC-012, 013), ERR-SLA-03 (TC-008 — A6 fill paired)
- A4 merged 2026-05-08: TC-020 (snapshot HS cũ), TC-021 (HS mới áp config mới), TC-022 (race condition), TC-040 (optimistic locking), TC-043 (audit log delta)
- A6 fill 2026-05-08: TC-007 (Add new SLA AC2), TC-008 (ERR-SLA-03 duplicate), TC-009 (toggle gui_thong_bao_app)
- SPEC-CLARIFY: CAUHINH-03 (QH-NT field — TC-006), CAUHINH-07 (race condition — TC-022), AC2 mâu thuẫn với schema enum 4 value cố định (TC-007)
