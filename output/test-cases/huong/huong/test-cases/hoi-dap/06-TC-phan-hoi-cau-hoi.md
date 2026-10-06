# Test Cases — FR-II-07 (UC16): Phản hồi câu hỏi

> **SRS Ref**: FR-II-07 (lines 555-628), SCR-II-02 dòng 19-26 (form soạn phản hồi), SM-HOIDAP transition `DANG_XU_LY → DA_TRA_LOI → CHO_PHE_DUYET` (auto BR-FLOW-01)
> **Ngày tạo**: 2026-05-10
> **Đặc thù**:
> - **Lưu nháp**: UPSERT PHAN_HOI WHERE `hoi_dap_id={id} AND ngay_tra_loi IS NULL` (chỉ 1 draft active per HD). KHÔNG SET ngay_tra_loi.
> - **Auto-save 60s** silent (chỉ đổi indicator "Đã lưu lúc {HH:mm:ss}").
> - **Gửi phản hồi**: SET `ngay_tra_loi = NOW()` → đánh dấu đã gửi → state DA_TRA_LOI → AUTO CHO_PHE_DUYET (BR-FLOW-01).
> - **Modal xác nhận tích "Đã trả lời" (F-18)**: 2-step confirm trước transition (không hoàn tác).
> - **Chèn mẫu MAU_PHAN_HOI** scope MPH_READ Mô hình B 2 tầng.
> - **XSS sanitize 3-layer (F-38)** trên rich-text editor.
> - **Optimistic locking PHAN_HOI** chống concurrent draft.
> - **Permission**: CB NV cùng đơn vị HOẶC NHT/TVV được phân công (`HOI_DAP_READ_ASSIGNED`).

---

## Quy ước

- **Priority**: 🔴 P0 · 🟡 P1 · 🟢 P2
- **TraceID**: `FR-II-07 / {section}`
- **Pre-conditions**: User CB_NV cùng đơn vị OR `nguoi_phan_cong_id = user.id`. HD state DANG_XU_LY.

---

## Trường input

| # | Field | Bắt buộc | Kiểu | Ràng buộc |
|---|-------|----------|------|-----------|
| 1 | hoi_dap_id | Y | identifier | URL/system |
| 2 | noi_dung_phan_hoi | Y khi gửi | text long | Max 5000 ký (plain text), rich-text editor, XSS sanitize F-38 |
| 3 | van_ban_phap_luat | N | text | Trích dẫn VBPL |
| 4 | goi_y | N | text | Gợi ý cho DN |
| 5 | da_tra_loi | N | boolean | Tích = trigger auto-transition (BR-FLOW-01) |
| 6 | mau_phan_hoi_id | N | identifier | FK MAU_PHAN_HOI scope MPH_READ |
| 7 | file_dinh_kem | N | binary[] | Như SCR-II-01 form (10 file, 100MB total, 20MB/file, ClamAV) |

---

## A. SOẠN PHẢN HỒI — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PH-001 | FR-II-07 / AC #1 | Mở form phản hồi từ SCR-II-02 | cb_nv_tw_01 login. HD-X DANG_XU_LY, đã phân công cho cb_nv_tw_01. | — | 1. SCR-II-02 HD-X. 2. Click [Soạn phản hồi] dòng 11. | (3) Cuộn đến form phản hồi (rich-text editor + dropdown chèn mẫu + checkbox + nút Lưu nháp + Gửi). Khối thông tin câu hỏi gốc accordion mở. | Happy 🔴 |
| TC-PH-002 | FR-II-07 / Processing step 5 (Lưu nháp) | Click [Lưu nháp] manual → UPSERT PHAN_HOI ngay_tra_loi=NULL | cb_nv_tw_01 login. HD-Y DANG_XU_LY. | noi_dung="Phản hồi nháp lần 1..." | 1. Nhập nội dung. 2. Click [Lưu nháp]. | (1) POST /phan-hoi UPSERT thành công. (2) Toast "Đã lưu lúc HH:mm:ss". Indicator dòng 25 hiển thị thời gian. (3) PHAN_HOI: `hoi_dap_id=HD-Y`, `nguoi_tra_loi_id=cb_nv_tw_01`, `noi_dung=...`, `ngay_tra_loi=NULL` (draft marker per F-FR02-04). HD trang_thai vẫn DANG_XU_LY (KHÔNG trigger BR-FLOW-01). | Happy 🔴 |
| TC-PH-003 | FR-II-07 / SCR-II-02 dòng 25 (Auto-save 60s) | Auto-save silent sau 60s không thao tác | cb_nv_tw_01 login. HD-Z DANG_XU_LY. | noi_dung="Đang gõ..." | 1. Nhập 1 câu. 2. Wait 60s không thao tác. | (3) Auto-save trigger silent (KHÔNG toast). Indicator dòng 25 đổi thành "Đã lưu lúc HH:mm:ss". PHAN_HOI updated. | Happy 🟡 |
| TC-PH-004 | FR-II-07 / AC #4 (load draft) | Mở lại SCR-II-02 → load draft vào editor | cb_nv_tw_01 login. HD-W DANG_XU_LY. PHAN_HOI draft tồn tại với ngay_tra_loi=NULL. | — | 1. Reload SCR-II-02 HD-W. | (3) Editor pre-fill draft content (auto-recovery từ PHAN_HOI có ngay_tra_loi IS NULL). Indicator "Đã lưu lúc {time}". | Happy 🔴 |
| TC-PH-005 | FR-II-07 / Processing step 6 + AC #5 + BR-FLOW-01 | Tích "Đã trả lời" + Gửi → Auto CHO_PHE_DUYET | cb_nv_tw_01 login. HD-V DANG_XU_LY. Draft đã có. | noi_dung hoàn chỉnh + da_tra_loi=true | 1. Nhập đầy đủ noi_dung. 2. Click checkbox "Đã trả lời" dòng 24. 3. **Modal xác nhận F-18 mở**: tiêu đề "Xác nhận đã trả lời?", nội dung "Tích sẽ tự động chuyển sang Chờ phê duyệt (BR-FLOW-01). Bạn sẽ KHÔNG thể sửa phản hồi sau khi chuyển (BR-FLOW-03). Hãy chắc chắn nội dung phản hồi đã hoàn chỉnh." 4. Click [Xác nhận đã trả lời]. 5. Click [Gửi phản hồi]. | (1-2) Modal F-18 mở trước khi tick. User confirm → tick + auto-transition. (3) PHAN_HOI: `ngay_tra_loi=NOW()` (đánh dấu đã gửi). HD: `trang_thai=DA_TRA_LOI` → AUTO `CHO_PHE_DUYET` (BR-FLOW-01). (4) Notification in-app + email cho CB PD cùng cấp (BR-AUTH-05, SLA email ≤5 phút). | Happy 🔴 |
| TC-PH-006 | FR-II-07 / AC #5 + F-18 cancel | Hủy modal F-18 → checkbox không tick | cb_nv_tw_01 login. HD-U DANG_XU_LY. | — | 1. Tick "Đã trả lời" dòng 24. 2. Modal F-18 mở. 3. Click [Quay lại tiếp tục sửa]. | (3) Checkbox bỏ tick. KHÔNG transition. State DANG_XU_LY giữ. | Happy 🟡 |
| TC-PH-007 | FR-II-07 / SCR-II-02 dòng 19 (chèn mẫu) | Dropdown chèn mẫu hiển thị 2 nhóm theo MPH_READ Mô hình B | cb_nv_dp_01 (Sở TP AG) login. HD-T DANG_XU_LY linh_vuc=Đất đai. MAU_PHAN_HOI seed: 3 mẫu TW_QUOC_GIA + 2 mẫu DP_RIENG (Sở TP AG) + 1 mẫu DP_RIENG (Sở TP BG) + 1 mẫu BN_RIENG. Tất cả linh_vuc=Đất đai, KICH_HOAT. | — | 1. Click dropdown chèn mẫu dòng 19. | (3) 2 nhóm: (a) "Mẫu khung quốc gia (TW)" — 3 mẫu TW (badge 🟦), (b) "Mẫu của Sở TP AG" — 2 mẫu DP_RIENG (badge 🟨). KHÔNG hiển thị 1 mẫu BG (khác đơn vị) hoặc mẫu BN. | Happy 🔴 |
| TC-PH-008 | FR-II-07 / dòng 19 chọn mẫu | Chọn mẫu → điền sẵn editor + tăng counter | cb_nv_dp_01 login. HD-S DANG_XU_LY. Chọn mẫu MAU-001 có `noi_dung="Theo Đ.X NĐ55/2019..."`. | mau_phan_hoi_id=MAU-001 | 1. Mở dropdown. 2. Click MAU-001. | (3) Editor pre-fill nội dung mẫu. (4) `MAU_PHAN_HOI[MAU-001].so_lan_su_dung += 1`. | Happy 🟡 |

---

## B. PHẢN HỒI BỞI NHT (Người được phân công)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PH-010 | FR-II-07 / Preconditions NHT + HOI_DAP_READ_ASSIGNED | NHT được phân công soạn phản hồi | nht_01 login. HD-R DANG_XU_LY, `nguoi_phan_cong_id=nht_01`. | noi_dung="Phản hồi của NHT" | 1. NHT thấy HD-R trong danh sách (HOI_DAP_READ_ASSIGNED). 2. Mở SCR-II-02. 3. Click [Soạn phản hồi]. 4. Lưu nháp. | (3) Form mở. NHT có quyền POST PHAN_HOI. PHAN_HOI: `nguoi_tra_loi_id=nht_01`. | Happy 🔴 |
| TC-PH-011 | FR-II-07 / E3 WRN-PH-01 | NHT KHÁC attempt phản hồi (không được phân công) | nht_02 login. HD-Q DANG_XU_LY, `nguoi_phan_cong_id=nht_01` (KHÔNG nht_02). | — | 1. nht_02 mở SCR-II-02. 2. Click [Soạn phản hồi]. | (2) UI cảnh báo WRN-PH-01 modal: **"Bạn không phải người được phân công. Vẫn muốn phản hồi?"** + 2 nút Hủy / Tiếp tục. **OR** UI block cứng (BR-AUTH-08 enforce). **SPEC-CLARIFY-PH-01** behavior. | Negative 🟡 |

---

## C. NEGATIVE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PH-100 | FR-II-07 / E1 ERR-PH-01 | Gửi phản hồi với noi_dung trống | cb_nv_tw_01 login. HD-P DANG_XU_LY. | noi_dung="" | 1. Editor để trống. 2. Click [Gửi phản hồi]. | (2) Validate noi_dung not blank → reject. Inline error đỏ: **"Nội dung phản hồi là bắt buộc"** (ERR-PH-01). KHÔNG POST. | Negative 🔴 |
| TC-PH-101 | FR-II-07 / E2 ERR-PH-02 | Phản hồi state CHO_PHE_DUYET → cấm | cb_nv_tw_01 login. HD-O state CHO_PHE_DUYET. | — | 1. Mở SCR-II-02 HD-O. | (2) Form phản hồi disabled (read-only). Force POST API → ERR-PH-02 **"Hỏi đáp ở trạng thái 'Chờ phê duyệt' không thể phản hồi"**. | Negative 🔴 |
| TC-PH-102 | FR-II-07 / SCR-II-02 dòng 20 XSS sanitize F-38 | Paste HTML chứa `<script>` | cb_nv_tw_01 login. HD-N DANG_XU_LY. | noi_dung="Câu trả lời<script>alert('xss')</script>" | 1. Paste payload vào editor. 2. Lưu nháp. | (2) Client DOMPurify strip `<script>`. Inline error highlight: **"Nội dung chứa HTML không được phép. Vui lòng chỉ dùng định dạng cơ bản"**. (3) Server check lần 2 (defense in depth). PHAN_HOI.noi_dung sạch không có `<script>`. | Negative 🔴 |
| TC-PH-103 | FR-II-07 / dòng 20 XSS event handler | Paste HTML có onclick | cb_nv_tw_01 login. HD-M DANG_XU_LY. | noi_dung=`<a href="#" onclick="alert(1)">Click</a>` | 1. Paste. 2. Lưu nháp. | (2) Sanitize loại bỏ `onclick`. Còn lại `<a href="#">Click</a>`. | Negative 🟡 |
| TC-PH-104 | FR-II-07 / dòng 20 XSS javascript: | Paste link `javascript:` | cb_nv_tw_01 login. HD-L DANG_XU_LY. | noi_dung=`<a href="javascript:alert(1)">XSS</a>` | 1. Paste. | (2) Sanitize loại bỏ `javascript:` (chỉ allow http://, https://). `<a>` tag bị strip href. | Negative 🟡 |

---

## D. EDGE & BOUNDARY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PH-200 | FR-II-07 / Inputs #2 boundary | noi_dung exact 5000 ký plain text | cb_nv_tw_01 login. HD-K DANG_XU_LY. | noi_dung=5000 ký plain | 1. Paste 5000 ký. 2. Counter `5000/5000`. 3. Gửi. | (3) Lưu OK. PHAN_HOI.noi_dung 5000 ký. | Edge 🟢 |
| TC-PH-201 | FR-II-07 / SCR-II-02 dòng 25 concurrent draft | 2 user cùng nguoi_phan_cong (hiếm) sửa đồng thời → conflict | cb_nv_tw_01 login. HD-J DANG_XU_LY phân công cb_nv_tw_01. cb_nv_tw_02 cũng có quyền (CB NV cùng đơn vị). | — | 1. cb_nv_tw_01 + cb_nv_tw_02 mở form, sửa nội dung. 2. cb_nv_tw_01 Lưu nháp. 3. cb_nv_tw_02 Lưu nháp. | (3) cb_nv_tw_02 nhận conflict (PHAN_HOI version mismatch). Toast persistent: **"Bản nháp đã được cb_nv_tw_01 cập nhật lúc {time}"** + 2 nút Tải lại (load nội dung mới) / Ghi đè. | Edge 🟡 |
| TC-PH-202 | FR-II-07 / Inputs #7 file upload | Upload 5 file pdf phản hồi | cb_nv_tw_01 login. HD-I DANG_XU_LY. | 5 files .pdf < 20MB | 1. Drag drop 5 files vào dòng 23. 2. ClamAV scan OK. 3. Lưu nháp. | (3) PHAN_HOI tạo 5 FILE_DINH_KEM (entity_type='PHAN_HOI'). | Edge 🟡 |
| TC-PH-203 | FR-II-07 / SM transition skip DA_TRA_LOI | DA_TRA_LOI thoáng qua — user không thấy state này | cb_nv_tw_01 login. HD-H DANG_XU_LY. | — | 1. Tích "Đã trả lời" + Gửi. 2. Reload SCR-II-02 ngay sau khi gửi. | (3) State badge hiển thị "Chờ phê duyệt" (CHO_PHE_DUYET). DA_TRA_LOI KHÔNG hiển thị (auto-transition tức thì BR-FLOW-01). Filter dropdown row 14 SCR-II-01 cũng loại DA_TRA_LOI khỏi options. | Edge 🟡 |
| TC-PH-204 | FR-II-07 / Permission CB_PD attempt soạn phản hồi | CB_PD attempt POST PHAN_HOI | cb_pd_tw_01 login. HD-G DANG_XU_LY. | — | 1. Mở SCR-II-02. | (3) Form phản hồi KHÔNG hiển thị (chỉ CB NV được phân công + CB NV cùng đơn vị). Force POST → 403. | Edge 🟡 |
| TC-PH-205 | FR-II-07 / dòng 19 mẫu vô hiệu | Mẫu KICH_HOAT=VO_HIEU_HOA không xuất hiện dropdown | cb_nv_tw_01 login. HD-F DANG_XU_LY. MAU-VOHIEU `trang_thai=VO_HIEU_HOA`, linh_vuc match. | — | 1. Mở dropdown. | (3) MAU-VOHIEU KHÔNG xuất hiện (filter `trang_thai='KICH_HOAT'`). | Edge 🟢 |
| TC-PH-206 | FR-II-07 / SCR-II-02 dòng 32 session expired | Session expired giữa lúc soạn → auto-save draft localStorage | cb_nv_tw_01 login. HD-E DANG_XU_LY. Soạn nội dung 200 ký. | — | 1. Soạn nội dung. 2. Backend invalidate session (mock 401). 3. User click Lưu nháp. | (3) Modal full-screen "Phiên đăng nhập đã hết hạn..." + 2 nút "Đăng nhập lại" + "Sao chép nội dung". Backend lưu localStorage `hoi-dap-draft-{id}` AES-256-GCM (SEC-07). Sau login lại → prompt "Khôi phục bản nháp đã soạn lúc {time}?". | Edge 🟡 |
| TC-PH-207 | FR-II-07 / SCR-II-02 dòng 33 mất quyền giữa chừng | User bị admin revoke quyền giữa chừng (HTTP 403) | cb_nv_tw_01 login. HD-D DANG_XU_LY. Đang soạn. Admin revoke quyền HOI_DAP_RESPOND. | — | 1. Soạn nội dung. 2. Click Lưu nháp. | (3) Toast persistent "Bạn vừa bị thu hồi quyền cho thao tác này" (KHÔNG dismiss tự động). Action-bar 9-18 disabled. Nút floating "Sao chép nội dung". Form data giữ trên client. | Edge 🟡 |

---

---

## E. EDGE BỔ SUNG (A4 merged 2026-05-10)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PH-208 | FR-II-07 / Auto-save race typing | Auto-save trigger trong khi user đang gõ | cb_nv_tw_01 login. HD-X DANG_XU_LY. | Đang gõ liên tục 70s | 1. Bắt đầu gõ. 2. Sau 60s auto-save fire. 3. Tiếp tục gõ. | (3) Auto-save lấy snapshot tại thời điểm trigger (không overwrite typing in progress). Indicator update. KHÔNG làm gián đoạn input focus. | Edge 🟡 |
| TC-PH-209 | FR-II-07 / Page Visibility API | Switch tab browser → quay lại sau 5 phút | cb_nv_tw_01 login. HD-Y DANG_XU_LY. Soạn 100 ký. | — | 1. Switch tab khác. 2. Sau 5 phút quay lại. | (3) Verify auto-save trong tab inactive: hoặc skip (Page Visibility hidden) hoặc vẫn fire. Behavior tùy implementation. | Edge 🟢 |
| TC-PH-210 | FR-II-07 / Chèn mẫu / SPEC-CLARIFY-PH-02 | Chèn mẫu khi editor đã có content → overwrite hay append? | cb_nv_tw_01 login. HD-Z DANG_XU_LY. Editor có "Đã soạn 1 đoạn..." (50 ký). | mau_phan_hoi_id=MAU-001 | 1. Editor có content. 2. Mở dropdown chèn mẫu. 3. Chọn MAU-001. | (3) **SPEC-CLARIFY-PH-02**: hoặc (a) modal C12 "Editor có nội dung. Ghi đè/Thêm sau?" hoặc (b) auto append cuối hoặc (c) overwrite. Verify thực tế. | Edge 🟡 |
| TC-PH-211 | FR-II-07 / Tích/Untick checkbox | Tích "Đã trả lời" rồi UNCheck → modal F-18? | cb_nv_tw_01 login. HD-W DANG_XU_LY. | — | 1. Tích checkbox. 2. Modal F-18 mở. 3. Click [Quay lại tiếp tục sửa] → bỏ tích. 4. Tích lại. | (3) Lần 2 tích → modal F-18 mở lại (mỗi lần tích đều hỏi). UNcheck KHÔNG cần modal (an toàn). | Edge 🟢 |
| TC-PH-212 | FR-II-07 / Reload during upload | Reload SCR-II-02 trong khi đang upload file | cb_nv_tw_01 login. HD-V DANG_XU_LY. Upload file 50MB (slow). | — | 1. Bắt đầu upload. 2. Khi progress 50%, reload page. | (3) Upload aborted. File KHÔNG attached. UI sau reload không có file. User cần re-upload. | Edge 🟢 |

---

## Tổng kết file 06

- **Tổng số TC: 28** (8 Happy + 2 NHT-specific + 5 Negative + 8 Edge + 5 A4 merged)
- **Critical TC (🔴)**: TC-PH-001, 002, 004, 005, 007, 010, 100, 101, 102
- **Coverage**: FR-II-07 đầy đủ (lưu nháp + auto-save 60s + tích "Đã trả lời" với F-18 confirm + auto-transition BR-FLOW-01 + chèn mẫu Mô hình B 2 tầng + XSS 3-layer + optimistic locking + permission CB_NV + NHT assigned)
- **Error codes**: ERR-PH-01, ERR-PH-02, WRN-PH-01
- **F-references**: F-18 (modal confirm tích "Đã trả lời"), F-38 (XSS), SEC-07 (localStorage AES-256-GCM)
- **SPEC-CLARIFY**: PH-01 (NHT khác attempt phản hồi → WRN modal vs hard block?)

*Generated 2026-05-10 — Phase A step A3*
