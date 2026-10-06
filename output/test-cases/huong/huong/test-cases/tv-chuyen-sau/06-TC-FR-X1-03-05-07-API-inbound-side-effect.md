# Test Cases — UC149 + UC151 + UC153 API Inbound Side-Effect Verify (FR-X.1-03 / -05 / -07)

> **Module:** FR-12 — Quản lý Tư vấn pháp luật chuyên sâu
> **SRS Ref:** `input/srs-v3/srs-fr-12-tv-chuyen-sau-v3.1.md`
> **UC scope:** UC149 (line 402-509) + UC151 (line 675-775) + UC153 (line 955-1048)
> **Loại UC:** M (API inbound từ Cổng PLQG — KHÔNG có UI CMS gốc)
> **Phase:** A3 (BMAD test-design) — 2026-05-06

> ⚠️ **A7 Filter rule:** TC API curl thuần (POST /api/v1/inbound/...) sẽ bị **LOẠI** module-level. File này chỉ chứa TC verify **SIDE-EFFECT UI** sau khi API inbound thực thi. Trigger API có thể qua:
> 1. **Test endpoint admin nội bộ** (nếu có) — fallback seed data.
> 2. **Postman / mock client** với API Key hợp lệ — đề cập trong Notes, KHÔNG phải step chính.
> 3. **Verify UI passive** sau khi Cổng PLQG push thực tế.
> Mỗi TC quy ước trigger trong **Notes** + steps chỉ verify UI consequence.

---

## Section A: UI Verify — side-effect indicator trên SCR-X1-01

### TC-API-IN-001 — UI Verify: list TVCS hiện badge "Mới" / count tab "Chờ xử lý" tăng sau khi API inbound thành công

- **Type:** UI Verify
- **Priority:** P0
- **Tài khoản:** cb_nv_dp_01 (STP An Giang — phụ trách theo BR-ROUTE-TVCS-01)
- **Preconditions:**
  - Login `cb_nv_dp_01`, vào SCR-X1-01 tab "Chờ xử lý" — ghi nhớ count hiện tại N (vd 5 record).
  - Cổng PLQG mock client hoặc test endpoint admin sẵn sàng push 1 payload UC149 hợp lệ vào don_vi STP-AG.
- **Steps:**
  1. Quan sát SCR-X1-01: count tab "Chờ xử lý" = N. Cột "Nguồn" / badge "Mới" baseline.
  2. Trigger API inbound POST `/api/v1/inbound/tu-van-chuyen-sau` với payload hợp lệ (xem Notes).
  3. Đợi 5-10s, click `[Làm mới]` SCR-X1-01.
  4. Quan sát badge + count + cột nguồn.
  5. Click record mới → SCR-X1-02 quan sát stepper + accordion 1.
- **Expected:**
  - Bước 3-4: Count tab "Chờ xử lý" = N+1. Record mới hiển thị top list. Badge "Mới" / icon `nguon = CONG_PLQG` hiển thị (theo overview §2.5 cột "Trạng thái 7 màu" line 1086-1095 + cột nguồn). Badge chuông in-app +1.
  - Bước 5: Stepper SM-TVCS active TIEP_NHAN. Mã = `TVCS-{YYYYMMDD}-{SEQ}` (BR-DATA-04 line 1549). Field `nguon` = `CONG_PLQG`. Field `ma_noi_dung_cong` echo lại từ payload Cổng.
- **SRS ref:** UC149 Step 10 line 464 "Tạo bản ghi tư vấn chuyên sâu, trạng thái = TIEP_NHAN, nguồn = CONG_PLQG" + Step 13 line 472 "Gửi thông báo CB NV phụ trách (in-app + email) BR-NOTIF-01" + Postcondition line 487-490.
- **Notes:** Trigger payload mẫu: `{ma_noi_dung_cong: "CONG-2026-0001", noi_dung_tu_van: "Test...", thong_tin_dn: {ten:"DN AG", ma_so_thue:"1234567890", dia_chi:"An Giang"}, don_vi_id: STP-AG.id}`. Không phải step chính — viết bằng test endpoint admin/Postman trong môi trường dev.

---

## Section B: UC149 TVCS inbound — side-effect verify

### TC-API-IN-002 — UC149 Happy: Cổng push TVCS hợp lệ → CB NV thấy record + TB in-app + email + SM-TVCS = TIEP_NHAN

- **Type:** Happy
- **Priority:** P0
- **Tài khoản:** cb_nv_tw_01 (CB NV TW phụ trách)
- **Preconditions:**
  - DN `dn-test-001` MST `1234567890` đã tồn tại (không yêu cầu — UC149 Step 7 upsert).
  - Cổng PLQG có API Key hợp lệ.
  - cb_nv_tw_01 đăng nhập, mở SCR-X1-01 + icon chuông notification.
- **Steps:**
  1. Trigger API POST `/api/v1/inbound/tu-van-chuyen-sau` với payload (xem Notes) — đặt `don_vi_id = TW.id` để route cho cb_nv_tw_01.
  2. Đợi 5-10s.
  3. Reload SCR-X1-01 tab "Chờ xử lý".
  4. Click icon chuông notification (in-app).
  5. Click record mới → SCR-X1-02 → quan sát accordion 1, 2, 5.
  6. Verify email box (env LuatDN5 mặc định không cần MailHog, có thể skip nếu env không support) — ưu tiên verify in-app.
- **Expected:**
  - Bước 3: Record mới hiển thị với mã `TVCS-{YYYYMMDD}-{SEQ}` (BR-DATA-04). Trạng thái badge "TIEP_NHAN" (overview §2.5 nhãn 7 màu). Cột nguồn = "CONG_PLQG".
  - Bước 4: Notification list có entry "Yêu cầu tư vấn mới: {ma_noi_dung_cong}" — BR-NOTIF-01 (line 472, 1585-1589).
  - Bước 5: Accordion 1 hiện DN với `ten_dn`, `ma_so_thue`, `dia_chi` upsert từ payload (UC149 Step 7 line 461). Accordion 2 có `noi_dung_tu_van`. Accordion 5 (Nhật ký) có entry "Tiếp nhận từ Cổng PLQG" + actor=SYSTEM (BR-DATA-05).
  - Stepper SM-TVCS active TIEP_NHAN.
- **SRS ref:** UC149 Bước 7-13 line 461-473 + Postcondition line 487-490 + AC line 506-509 "Given Cổng PLQG gửi nội dung tư vấn... When dữ liệu hợp lệ Then HT tạo hồ sơ tư vấn + trả mã hồ sơ".
- **Notes:** Trigger qua Postman với headers `X-API-Key: {valid-key}`. Step verify email box ưu tiên skip (env LuatDN5 fix cứng). Routing don_vi_id verify ở TC-API-IN-004.

### TC-API-IN-003 — UC149 Negative duplicate: Cổng push lại cùng `ma_noi_dung_cong` → ERR-TVCS-API-03 + UI list KHÔNG thêm record

- **Type:** Negative
- **Priority:** P1
- **Tài khoản:** cb_nv_tw_01
- **Preconditions:**
  - TVCS `tvcs-existing-001` đã tồn tại với `ma_noi_dung_cong = "CONG-2026-DUP-001"` (do API inbound trước đó).
  - cb_nv_tw_01 mở SCR-X1-01, đếm count tab "Chờ xử lý" = N.
- **Steps:**
  1. Trigger API POST `/api/v1/inbound/tu-van-chuyen-sau` với payload `ma_noi_dung_cong = "CONG-2026-DUP-001"` (cùng mã đã tồn tại).
  2. Đợi 5-10s. Quan sát response API.
  3. Reload SCR-X1-01.
  4. Đếm count tab "Chờ xử lý".
- **Expected:**
  - Bước 2: API response HTTP 4xx với body `{ket_qua: "THAT_BAI", ma_loi: "ERR-TVCS-API-03", chi_tiet_loi: "Nội dung 'CONG-2026-DUP-001' đã tồn tại (mã: TVCS-..)"}` (UC149 E3 line 498 + Output table line 478-483 echo back).
  - Bước 3-4: Count tab "Chờ xử lý" = N (KHÔNG đổi). KHÔNG có record mới với cùng mã. KHÔNG có notification mới.
  - AUDIT_LOG có thể ghi attempt failed (BR-DATA-05) nhưng KHÔNG insert TU_VAN_CHUYEN_SAU mới.
- **SRS ref:** UC149 Step 5 line 454 "Kiểm tra trùng: đã tồn tại nội dung với cùng mã Cổng chưa" + E3 line 498 "ERR-TVCS-API-03" + AC line 508 "Given Cổng gửi nội dung trùng (mã Cổng) When kiểm tra Then trả lỗi ERR-TVCS-API-03".
- **Notes:** Idempotency check cùng pattern UC153 GUI_LAI nhưng UC149 KHÔNG có hành động GUI_LAI — duplicate mã = hard error.

### TC-API-IN-004 — UC149 Edge BR-ROUTE-TVCS-01: payload thiếu don_vi_id → default Sở TP tỉnh DN theo địa chỉ/MST

- **Type:** Edge
- **Priority:** P1
- **Tài khoản:** cb_nv_dp_01 (STP An Giang) + cb_nv_tw_01 (TW)
- **Preconditions:**
  - DN MST `9876543210` địa chỉ "An Giang" → mapping STP-AG.
  - cb_nv_dp_01 đăng nhập SCR-X1-01.
- **Steps:**
  1. Trigger API POST `/api/v1/inbound/tu-van-chuyen-sau` payload với `thong_tin_dn.ma_so_thue = "9876543210"`, `thong_tin_dn.dia_chi = "An Giang"`, **`don_vi_id` = null/missing**.
  2. Đợi 5-10s.
  3. cb_nv_dp_01 reload SCR-X1-01 tab "Chờ xử lý" → quan sát.
  4. cb_nv_tw_01 reload SCR-X1-01 tab "Chờ xử lý" → quan sát.
- **Expected:**
  - Bước 3: cb_nv_dp_01 (AG) THẤY record mới với `don_vi_id = STP-AG`. (BR-ROUTE-TVCS-01 default Sở TP tỉnh DN line 447 + 1591-1595).
  - Bước 4: cb_nv_tw_01 (TW) KHÔNG thấy record (BR-AUTH-08 — TW không phải đơn vị routed).
  - Record có cột nguồn = CONG_PLQG, mã `TVCS-{date}-{seq}`, DN linked theo MST 9876543210.
- **SRS ref:** UC149 Step 3a line 447 "nếu không có hoặc không hợp lệ → áp default Sở TP tỉnh DN theo địa chỉ/MST" + BR-ROUTE-TVCS-01 line 1591-1595 `[CR-06]` + Input field 7 line 436 "Mặc định Sở TP tỉnh DN".
- **Notes:** Verify routing default — kết hợp BR-AUTH-08 multi-tenant filter side-effect.

---

## Section C: UC151 HSPL inbound — side-effect verify

### TC-API-IN-005 — UC151 Happy: Cổng push HSPL → tab "Hồ sơ PL" của DN có record mới + ma_ho_so_cong + đưa vào danh sách chờ xử lý CB NV

- **Type:** Happy
- **Priority:** P0
- **Tài khoản:** cb_nv_tw_01
- **Preconditions:**
  - DN `dn-hspl-001` MST `1111122222` có sẵn (hoặc upsert tạo mới).
  - cb_nv_tw_01 mở chi tiết DN (FR-07) tab "Hồ sơ PL" — count baseline = M (vd 3 HSPL).
  - Hoặc mở "Danh sách chờ xử lý" CB NV trên dashboard.
- **Steps:**
  1. Trigger API POST `/api/v1/inbound/ho-so-phap-ly-dn` với payload: `{ma_ho_so_cong: "HSPL-CONG-2026-001", thong_tin_dn: {ma_so_thue: "1111122222", ten: "DN HSPL Test"}, ten_ho_so: "Giấy phép kinh doanh", loai_ho_so: "GIAY_PHEP", file_dinh_kem: [{ten_file:"gp.pdf", noi_dung_base64:"..."}]}`.
  2. Đợi 5-10s.
  3. cb_nv_tw_01 reload chi tiết DN → tab "Hồ sơ PL".
  4. Click record HSPL mới → quan sát detail.
  5. Click icon chuông notification.
  6. Mở dashboard "Danh sách chờ xử lý" / queue HSPL CB NV.
- **Expected:**
  - Bước 3: Tab "Hồ sơ PL" count = M+1. Record mới có:
    - Mã: `HSPL-{YYYYMMDD}-{SEQ}` (BR-DATA-04 UC151 Step 7 line 728)
    - Tên: "Giấy phép kinh doanh"
    - Loại: GIAY_PHEP
    - Trạng thái: HIEU_LUC (UC151 Step 8 line 729)
    - Nguồn: CONG_PLQG
    - File `gp.pdf` đã quét virus, lưu trữ
  - Bước 4: Field `ma_ho_so_cong` hiển thị = "HSPL-CONG-2026-001" (echo back UC151 Output line 747).
  - Bước 5: Notification "Hồ sơ pháp lý mới từ Cổng PLQG" — BR-NOTIF-01 (UC151 Step 11 line 737).
  - Bước 6: Record xuất hiện trong "Danh sách chờ xử lý" CB NV (UC151 Step 12 line 738 "Đưa hồ sơ vào danh sách chờ xử lý cho CB NV").
- **SRS ref:** UC151 Bước 7-12 line 728-738 + Postcondition line 753-756 + AC line 771-774 "Given Cổng gửi hồ sơ When dữ liệu hợp lệ Then HT tiếp nhận, tạo mới HSPL... đưa vào danh sách chờ xử lý cho CB NV".
- **Notes:** Trigger qua Postman với valid API Key. SPEC-CLARIFY-HSPL-QUEUE — UI dashboard "Danh sách chờ xử lý CB NV" SRS không quote rõ route — Phase B verify route thực tế hoặc fallback verify qua tab "Hồ sơ PL" filter `nguon = CONG_PLQG AND processed = false`.

---

## Section D: UC153 Đánh giá inbound — side-effect verify

### TC-API-IN-006 — UC153 Happy: Cổng push DANH_GIA cho TVCS DA_DUYET → accordion "Đánh giá CL" trên SCR-X1-02 hiển thị + tổng hợp Điểm TB cập nhật

- **Type:** Happy
- **Priority:** P0
- **Tài khoản:** cb_nv_tw_01 + cb_pd_tw_01 (read accordion)
- **Preconditions:**
  - TVCS `tvcs-da-duyet-001` trạng thái DA_DUYET, chuyên gia = `cg_01` (mã = "CG001"), `ma_noi_dung_cong` = "CONG-DG-001".
  - Accordion "Đánh giá CL" baseline: Điểm TB = N/A, Số lượng = 0 (chưa có đánh giá).
- **Steps:**
  1. cb_nv_tw_01 mở SCR-X1-02 chi tiết `tvcs-da-duyet-001` → accordion 4 "Đánh giá CL". Quan sát baseline.
  2. Trigger API POST `/api/v1/inbound/danh-gia-chat-luong-tv` với payload:
     ```
     {ma_noi_dung_cong: "CONG-DG-001", ma_danh_gia_cong: "DG-CONG-001",
      diem_so: 5, nhan_xet: "Tư vấn rất tốt", ma_chuyen_gia: "CG001",
      ngay_danh_gia: "2026-05-06T10:00:00Z", hanh_dong: "TAO_MOI"}
     ```
  3. Đợi 5-10s. Reload SCR-X1-02 → accordion 4.
  4. Quan sát chi tiết bảng + tổng hợp.
  5. Verify action button trên accordion 4.
- **Expected:**
  - Bước 3-4: Accordion 4 "Đánh giá CL" hiển thị 1 row:
    - Mã: `ma_danh_gia_cong = "DG-CONG-001"` (echo back UC153 Output line 1019)
    - Điểm: 5 sao (1-5 range UC153 Input field 3 line 985)
    - Nhận xét: "Tư vấn rất tốt"
    - Ngày: 2026-05-06
  - Tổng hợp: Điểm TB = 5.0, Số lượng = 1.
  - Profile cg_01 cập nhật điểm trung bình chuyên gia (UC153 Step 9 line 1010 — verify FR-04 detail CG nếu cần cross-FR).
  - Bước 5: **Read-only** — KHÔNG có action button [Sửa]/[Xóa]/[Phê duyệt] trên accordion (Permission Matrix overview §2.4 line 174 DANH_GIA = R\* cho mọi role nội bộ, C† chỉ qua Cổng).
- **SRS ref:** UC153 Step 5 line 1006 "Nếu TAO_MOI: kiểm tra chưa có đánh giá cho mã Cổng → tạo bản ghi đánh giá" + Step 9 line 1010 "Cập nhật điểm đánh giá trung bình cho chuyên gia" + Postcondition line 1023-1028 + Overview §2.5 SCR-X1-02 Accordion 4 line 210 "(UC153 read-only): Bảng (Mã/Điểm 1-5 sao/Nhận xét DN/Ngày) + Tổng hợp Điểm TB + Số lượng".
- **Notes:** Verify CG profile điểm TB cross-FR-04 ngoài scope file này — assumption side-effect đúng. Trigger qua Postman.

### TC-API-IN-007 — UC153 Edge GUI_LAI idempotency: Cổng push lại cùng `ma_danh_gia_cong` → KHÔNG ghi đè + count KHÔNG tăng + audit log GUI_LAI handled

- **Type:** Edge
- **Priority:** P1
- **Tài khoản:** cb_nv_tw_01
- **Preconditions:**
  - TVCS `tvcs-da-duyet-001` đã có 1 đánh giá `ma_danh_gia_cong = "DG-CONG-001"`, điểm = 5, nhận xét = "Tư vấn rất tốt" (từ TC-API-IN-006).
  - Accordion 4 baseline: Số lượng = 1, Điểm TB = 5.0.
- **Steps:**
  1. Trigger API POST `/api/v1/inbound/danh-gia-chat-luong-tv` với payload:
     ```
     {ma_noi_dung_cong: "CONG-DG-001", ma_danh_gia_cong: "DG-CONG-001",
      diem_so: 3, nhan_xet: "Updated text via GUI_LAI",
      ma_chuyen_gia: "CG001", ngay_danh_gia: "2026-05-06T11:00:00Z",
      hanh_dong: "GUI_LAI"}
     ```
     (Cùng `ma_danh_gia_cong` nhưng diem_so + nhan_xet thay đổi.)
  2. Đợi 5-10s. Quan sát API response.
  3. Reload SCR-X1-02 → accordion 4.
  4. Verify count + giá trị field cũ vs mới.
  5. Mở accordion 5 "Nhật ký" / AUDIT_LOG.
- **Expected:**
  - Bước 2: API trả `ket_qua: "THANH_CONG"` (UC153 Step 7 line 1008 "GUI_LAI idempotency: kiểm tra trùng lặp. Nếu đã tồn tại → không ghi đè, trả success"). Field `ma_danh_gia` echo back mã đã tồn tại (cũ).
  - Bước 3-4: Accordion 4 vẫn hiển thị 1 row với **dữ liệu CŨ**: Điểm = 5 (KHÔNG đổi thành 3), Nhận xét = "Tư vấn rất tốt" (KHÔNG đổi). Số lượng = 1 (KHÔNG +1). Điểm TB = 5.0.
  - Bước 5: AUDIT_LOG có entry "GUI_LAI handled — duplicate ma_danh_gia_cong, no overwrite" (BR-DATA-05).
- **SRS ref:** UC153 Step 7 line 1008 "Nếu GUI_LAI (idempotency): kiểm tra trùng lặp. Nếu đã tồn tại → không ghi đè, trả success" + AC line 1046 "Given Cổng gửi lại khi đồng bộ thất bại When HT nhận Then kiểm tra trùng lặp, không ghi đè sai lệch" + SPEC-CLARIFY-TVCS-09 (overview line 305 — payload mới có nhan_xet thay đổi có warn audit không).
- **Notes:** SPEC-CLARIFY-TVCS-09 đang Open. Test theo assumption hiện tại "không ghi đè" + audit log có entry handled. Phase B verify thực tế. Nếu BA respond conflict resolution = warn → re-test.

---

## Section E: Edge bổ sung A4 (Rate limit + Payload corrupt + Concurrent push)

### TC-API-IN-008 — Edge rate limit ngưỡng API inbound (verify UI count + TB indicator)

- **Type:** Edge
- **Priority:** P2
- **Tài khoản:** cb_nv_tw_01 (verify UI side-effect)
- **Preconditions:**
  - API rate limit config: 100 req/phút/API Key (assumption per BR-EC cross-cutting).
  - cb_nv_tw_01 mở SCR-X1-01 + icon chuông notification.
  - Test endpoint admin sẵn sàng burst push.
- **Test Data:** Burst 110 payload UC149 hợp lệ vào 1 phút.
- **Steps:**
  1. Trigger burst 110 POST `/api/v1/inbound/tu-van-chuyen-sau` qua test endpoint admin (mỗi payload `ma_noi_dung_cong` unique).
  2. Đợi 60s.
  3. cb_nv_tw_01 reload SCR-X1-01 tab "Chờ xử lý" → đếm count delta.
  4. Mở admin log endpoint hoặc audit log để verify rate limit triggered.
- **Expected:**
  - **STATE:** 100 record đầu tiên success (HTTP 200). Record 101-110: response 429 Too Many Requests (rate limit).
  - **UI:** Tab "Chờ xử lý" count tăng +100 (KHÔNG phải +110). KHÔNG có 10 record dở dang. AUDIT_LOG có entry "RATE_LIMIT_EXCEEDED" với count failed=10.
  - **TB indicator:** Notification badge tăng +100, KHÔNG có spam indicator hoặc lỗi.
- **SRS ref:** BR-EC cross-cutting (rate limit) + UC149 line 442 (API Key auth).
- **Notes:** A7 IN-PLACE — verify UI side-effect (count delta), KHÔNG verify thuần API rate limit. Trigger qua admin endpoint nếu có. SPEC-CLARIFY-TVCS-API-RL — rate limit threshold + retry-after header chưa quote.

### TC-API-IN-009 — Edge payload corrupt: JSON malformed / oversize / missing required field

- **Type:** Negative / Edge
- **Priority:** P1
- **Tài khoản:** cb_nv_tw_01 (verify UI count không đổi)
- **Preconditions:** SCR-X1-01 baseline count = N.
- **Test Data:**
  - Lần 1: JSON malformed `{"ma_noi_dung_cong": "X", noi_dung_tu_van: missing-quote}` (parse error).
  - Lần 2: payload oversize 10MB (chuỗi noi_dung_tu_van 10MB).
  - Lần 3: payload missing required `ma_noi_dung_cong` field.
- **Steps:**
  1. Trigger 3 payload trên qua POST `/api/v1/inbound/tu-van-chuyen-sau`.
  2. Đợi 5s.
  3. Reload SCR-X1-01 → verify count = N (KHÔNG đổi).
  4. Verify response code per case.
- **Expected:**
  - **Lần 1 JSON malformed:** HTTP 400 Bad Request với `ma_loi="ERR-TVCS-API-02"`, body chứa parser error chi tiết. Message nguyên văn line 497: `"Dữ liệu không hợp lệ: {chi_tiet_loi}"`.
  - **Lần 2 oversize:** HTTP 413 Payload Too Large (BR-EC cross-cutting payload size limit). HOẶC HTTP 400 với `ma_loi="ERR-TVCS-API-02"` nếu noi_dung_tu_van vượt 50KB constraint (line 446).
  - **Lần 3 missing field `ma_noi_dung_cong`:** HTTP 400 với `ma_loi="ERR-TVCS-API-02"` (line 497 — "Cấu trúc dữ liệu không hợp lệ"), `chi_tiet_loi` chứa thông tin "ma_noi_dung_cong is required". **KHÔNG dùng ERR-TVCS-API-01** (= API key invalid HTTP 401, line 496).
  - **STATE:** Cả 3 lần KHÔNG INSERT TU_VAN_CHUYEN_SAU. Count tab "Chờ xử lý" = N. AUDIT_LOG có entry inbound-failed (BR-DATA-05).
- **SRS ref:** UC149 Step 1-3 line 444-447 (validation auth + cấu trúc + format) + Step 4 line 451 + E1 line 496 (ERR-TVCS-API-01 auth) + E2 line 497 (ERR-TVCS-API-02 cấu trúc).
- **Notes:** No SRS quote payload size limit — best practice. SPEC-CLARIFY-TVCS-API-PAYLOAD — exact size threshold + error response schema. **Sửa 2026-05-09 (codex review):** Original TC map missing-field → ERR-TVCS-API-01 sai vì API-01 = invalid API key (HTTP 401). Validation payload phải dùng ERR-TVCS-API-02.

### TC-API-IN-010 — Edge concurrent push 2 record cùng `ma_noi_dung_cong` race → 1 success + 1 ERR-TVCS-API-03

- **Type:** Edge
- **Priority:** P1
- **Tài khoản:** cb_nv_tw_01
- **Preconditions:**
  - SCR-X1-01 baseline count = N.
  - 2 client mock Cổng PLQG sẵn sàng push parallel.
- **Test Data:** payload 1 + payload 2 cùng `ma_noi_dung_cong = "CONG-RACE-001"`, `noi_dung_tu_van` khác nhau.
- **Steps:**
  1. Trigger 2 POST `/api/v1/inbound/tu-van-chuyen-sau` cùng `ma_noi_dung_cong` parallel (interval <100ms).
  2. Đợi 5s.
  3. Reload SCR-X1-01 → verify count delta.
  4. Verify response 2 request.
- **Expected:**
  - **STATE:** Backend dùng DB unique constraint hoặc distributed lock trên `ma_noi_dung_cong` → chỉ 1 INSERT TU_VAN_CHUYEN_SAU thành công (request đến trước hoặc lock holder).
  - **Response 1:** HTTP 200 `ket_qua: "THANH_CONG"`, mã TVCS auto-gen.
  - **Response 2:** HTTP 4xx `ket_qua: "THAT_BAI"`, `ma_loi: "ERR-TVCS-API-03"`, message "Nội dung đã tồn tại" (UC149 E3 line 498).
  - **UI:** Tab "Chờ xử lý" count = N+1 (KHÔNG +2). KHÔNG có duplicate. AUDIT_LOG: 1 entry CREATE + 1 entry inbound-duplicate-failed.
- **SRS ref:** UC149 Step 5 line 454 (kiểm tra trùng) + E3 line 498 (ERR-TVCS-API-03).
- **Notes:** No SRS quote concurrent race policy — best practice DB unique constraint. Verify tại Phase B nếu có thể chạy song song. SPEC-CLARIFY-TVCS-API-RACE.

### TC-API-IN-011 — UC151 Negative duplicate: Cổng push lại cùng `ma_ho_so_cong` → ERR-HSPL-API-03 + UI count tab Hồ sơ PL KHÔNG tăng

- **Type:** Negative
- **Priority:** P1
- **Tài khoản:** cb_nv_tw_01
- **Preconditions:**
  - HSPL `hspl-existing-001` đã tồn tại với `ma_ho_so_cong = "HSPL-CONG-DUP-001"` (do API inbound trước đó hoặc seed).
  - DN parent `dn-hspl-dup-001` MST `2222233333`. cb_nv_tw_01 mở chi tiết DN → tab "Hồ sơ PL". Đếm count baseline = M.
  - Bell notification baseline count.
- **Test Data:** Payload UC151 với `ma_ho_so_cong = "HSPL-CONG-DUP-001"` (cùng mã đã tồn tại) + `thong_tin_dn.ma_so_thue = "2222233333"`.
- **Steps:**
  1. Trigger API POST `/api/v1/inbound/ho-so-phap-ly-dn` payload duplicate ma_ho_so_cong (Postman/test endpoint admin).
  2. Đợi 5-10s. Quan sát API response.
  3. cb_nv_tw_01 reload tab "Hồ sơ PL" của dn-hspl-dup-001.
  4. Đếm count + verify list KHÔNG có HSPL trùng mã mới.
  5. Click icon chuông notification → verify không có entry "Hồ sơ pháp lý mới" cho duplicate này.
  6. (Nếu UI có) verify admin error log / toast cho actor=SYSTEM.
- **Expected:**
  - **Bước 2:** API response HTTP 4xx (400/409) với body nguyên văn line 764: `{ket_qua: "THAT_BAI", ma_loi: "ERR-HSPL-API-03", chi_tiet_loi: "Hồ sơ 'HSPL-CONG-DUP-001' đã tồn tại (mã: HSPL-{date}-{seq})"}` — template `"Hồ sơ '{mã}' đã tồn tại (mã: {ma_ho_so})"` (UC151 line 764 + AC-3 line 773).
  - **Bước 3-4:** Count tab "Hồ sơ PL" = M (KHÔNG đổi). KHÔNG có HSPL mới. KHÔNG có duplicate row.
  - **Bước 5:** Notification list KHÔNG có entry HSPL mới (BR-NOTIF-01 chỉ trigger khi inbound thành công).
  - **STATE:** AUDIT_LOG có entry attempt-failed `INBOUND_HSPL_DUPLICATE` (BR-DATA-05) với chi_tiet_loi = ma_ho_so_cong + actor=SYSTEM. KHÔNG INSERT HO_SO_PHAP_LY_DN.
- **SRS ref:** UC151 line 762-763 (ERR-HSPL-API-03 nguyên văn) + AC line 773 (Given Cổng gửi hồ sơ trùng mã When kiểm tra Then trả lỗi ERR-HSPL-API-03 + không insert).
- **Notes:** A6 fill A5-G8 (UC151 AC-3 explicit). Pattern same TC-API-IN-003 (UC149 duplicate) nhưng cho UC151 HSPL. Trigger qua Postman với valid API Key, KHÔNG step chính.

### TC-API-IN-013 — UC149 Negative matrix: ERR-TVCS-API-01..05 + ERR-FILE-SIZE-01 + ERR-FILE-02 (codex review fill 2026-05-09)

- **Type:** Negative
- **Priority:** P0
- **Tài khoản:** cb_nv_tw_01 (verify UI count + bell)
- **Preconditions:**
  - SCR-X1-01 baseline count tab "Chờ xử lý" = N. Bell notification baseline.
  - Mock client có/không API Key hợp lệ. EICAR test file + 21MB file sẵn sàng.
- **Test Data per case:**
  - C1 — `ERR-TVCS-API-01`: API Key invalid hoặc thiếu `X-API-Key` header.
  - C2 — `ERR-TVCS-API-02`: payload thiếu `noi_dung_tu_van` (required line 431).
  - C3 — `ERR-TVCS-API-02`: ma_so_thue=`12345` (5 chữ số, line 432 yêu cầu 10-13).
  - C4 — `ERR-TVCS-API-03`: cùng ma_noi_dung_cong đã tồn tại (đã cover TC-API-IN-003 — chỉ ref).
  - C5 — `ERR-TVCS-API-05`: linh_vuc_id=`DM-INVALID-99` (không tồn tại trong DANH_MUC).
  - C6 — `ERR-FILE-SIZE-01`: tai_lieu_dinh_kem chứa 1 file 21MB (vượt 20MB line 435).
  - C7 — `ERR-FILE-02`: tai_lieu_dinh_kem chứa file EICAR signature (mã độc).
  - C8 — `ERR-TVCS-API-04`: rate limit (đã cover TC-API-IN-008 — chỉ ref).
- **Steps:**
  1. Trigger 6 case C1-C3, C5-C7 lần lượt POST `/api/v1/inbound/tu-van-chuyen-sau` qua Postman/test endpoint admin.
  2. Đợi 5s mỗi case. Capture API response.
  3. Reload SCR-X1-01 → đếm count delta = 0 (KHÔNG INSERT cho mọi case).
  4. Click chuông notification → verify KHÔNG có entry inbound thành công.
- **Expected per case:**
  - **C1:** HTTP 401, body `{ket_qua:"THAT_BAI", ma_loi:"ERR-TVCS-API-01"}` + message `"Unauthorized"` (line 496 nguyên văn).
  - **C2:** HTTP 400, body `{ma_loi:"ERR-TVCS-API-02", chi_tiet_loi:"Dữ liệu không hợp lệ: noi_dung_tu_van là bắt buộc"}` (line 497 template).
  - **C3:** HTTP 400, `ma_loi:"ERR-TVCS-API-02"`, chi_tiet_loi chứa "ma_so_thue phải 10-13 chữ số".
  - **C5:** HTTP 400, body `{ma_loi:"ERR-TVCS-API-05", chi_tiet_loi:"Lĩnh vực pháp lý không hợp lệ hoặc đã ngừng hoạt động"}` (line 502 nguyên văn).
  - **C6:** HTTP 400, body `{ma_loi:"ERR-FILE-SIZE-01", chi_tiet_loi:"Tệp 'doc21mb.pdf' vượt quá 20MB"}` (line 499 template).
  - **C7:** HTTP 400, body `{ma_loi:"ERR-FILE-02", chi_tiet_loi:"Tệp 'eicar.com' chứa mã độc, không thể tiếp nhận"}` (line 500 nguyên văn).
  - **STATE all cases:** KHÔNG INSERT TU_VAN_CHUYEN_SAU. Count tab "Chờ xử lý" = N. Bell notification KHÔNG +1. AUDIT_LOG có entry `INBOUND_TVCS_FAILED` (BR-DATA-05) với chi_tiet_loi.
- **SRS ref:** UC149 line 496-502 (Error Handling 7 codes) + Step 1-3 line 444-447 (validation) + line 432 (ma_so_thue 10-13) + line 435 (file 20MB).
- **Notes:** Codex review fill 2026-05-09. Trigger qua Postman/test endpoint, KHÔNG step chính. Mỗi case 1 trigger riêng để verify response code/wording. Cover toàn bộ matrix UC149 — closes G3 (codex P0 GAP).

### TC-API-IN-014 — UC151 Negative matrix: ERR-HSPL-API-01/02/04 + ERR-FILE-SIZE-01 + ERR-FILE-02 (codex review fill 2026-05-09)

- **Type:** Negative
- **Priority:** P1
- **Tài khoản:** cb_nv_tw_01
- **Preconditions:**
  - DN parent `dn-hspl-neg-001` MST `3333344444`. cb_nv_tw_01 mở chi tiết DN → tab "Hồ sơ PL". Count baseline = M.
  - Bell notification baseline.
- **Test Data per case:**
  - C1 — `ERR-HSPL-API-01`: API Key invalid (HTTP 401).
  - C2 — `ERR-HSPL-API-02`: payload thiếu `ten_ho_so` (required line 705).
  - C3 — `ERR-HSPL-API-02`: loai_ho_so="LOAI_INVALID" (không nằm 5 enum line 706).
  - C4 — `ERR-HSPL-API-03`: duplicate ma_ho_so_cong (đã cover TC-API-IN-011 — chỉ ref).
  - C5 — `ERR-HSPL-API-04`: rate limit burst >100 req/phút.
  - C6 — `ERR-FILE-SIZE-01`: file_dinh_kem 21MB (vượt 20MB).
  - C7 — `ERR-FILE-02`: file EICAR signature.
- **Steps:**
  1. Trigger 6 case C1-C3, C5-C7 lần lượt POST `/api/v1/inbound/ho-so-phap-ly-dn`.
  2. Đợi 5s. Capture API response.
  3. cb_nv_tw_01 reload tab "Hồ sơ PL" của DN parent → count = M (KHÔNG đổi).
  4. Bell notification KHÔNG +1 entry HSPL mới.
- **Expected per case:**
  - **C1:** HTTP 401 `ma_loi:"ERR-HSPL-API-01"` "Unauthorized" (line 762 nguyên văn).
  - **C2:** HTTP 400 `ma_loi:"ERR-HSPL-API-02"`, chi_tiet_loi="Dữ liệu không hợp lệ: ten_ho_so là bắt buộc" (line 763 template).
  - **C3:** HTTP 400 `ma_loi:"ERR-HSPL-API-02"`, chi_tiet_loi chứa "loai_ho_so không hợp lệ".
  - **C5:** HTTP 429 + header `Retry-After`, `ma_loi:"ERR-HSPL-API-04"` (line 767 nguyên văn).
  - **C6:** HTTP 400 `ma_loi:"ERR-FILE-SIZE-01"`, chi_tiet_loi="Tệp '{ten_file}' vượt quá 20MB" (line 765 template — placeholder `{ten_file}` nguyên văn).
  - **C7:** HTTP 400 `ma_loi:"ERR-FILE-02"`, chi_tiet_loi="Tệp '{ten_file}' chứa mã độc" (line 766 nguyên văn — placeholder `{ten_file}` nguyên văn).
  - **STATE all cases:** KHÔNG INSERT HO_SO_PHAP_LY_DN. Count tab = M. Bell KHÔNG +1. AUDIT_LOG entry `INBOUND_HSPL_FAILED` (BR-DATA-05).
- **SRS ref:** UC151 line 762-767 (Error Handling 6 codes) + line 717-720 (validation) + line 704 (ma_so_thue 10-13) + line 706 (loai_ho_so 5 enum).
- **Notes:** Codex review fill 2026-05-09. Closes G4 (codex P0 GAP). Trigger qua Postman.

### TC-API-IN-015 — UC153 Negative matrix: ERR-DG-API-01..07 (codex review fill 2026-05-09)

- **Type:** Negative
- **Priority:** P0
- **Tài khoản:** cb_nv_tw_01 (verify accordion 4 không đổi)
- **Preconditions:**
  - TVCS `tvcs-da-duyet-neg-001` DA_DUYET, đã có 1 đánh giá `ma_danh_gia_cong="DG-CONG-EXIST-001"` điểm=4.
  - Accordion 4 baseline: Số lượng=1, Điểm TB=4.0.
  - cb_nv_tw_01 mở SCR-X1-02 → accordion 4 quan sát baseline.
- **Test Data per case:**
  - C1 — `ERR-DG-API-01`: API Key invalid → HTTP 401.
  - C2 — `ERR-DG-API-02`: payload thiếu `ma_danh_gia_cong` (required line 984).
  - C3 — `ERR-DG-API-03`: diem_so=0 (ngoài 1-5).
  - C4 — `ERR-DG-API-03`: diem_so=6 (ngoài 1-5).
  - C5 — `ERR-DG-API-04`: ma_noi_dung_cong="CONG-NOTFOUND-XYZ" (không tồn tại trong CSDL).
  - C6 — `ERR-DG-API-05`: hanh_dong=TAO_MOI nhưng ma_danh_gia_cong="DG-CONG-EXIST-001" (đã tồn tại).
  - C7 — `ERR-DG-API-06`: hanh_dong=CAP_NHAT cho mã không tồn tại HOẶC trạng thái đánh giá không cho phép cập nhật.
  - C8 — `ERR-DG-API-07`: rate limit burst.
- **Steps:**
  1. Trigger **8 case C1-C8** lần lượt POST `/api/v1/inbound/danh-gia-chat-luong-tv` (C8 burst >100 req/phút để trigger rate limit).
  2. Đợi 5s mỗi case. Capture API response.
  3. Reload SCR-X1-02 → accordion 4 verify Số lượng=1, Điểm TB=4.0 (KHÔNG đổi).
  4. Verify CG profile điểm TB cũng KHÔNG đổi.
  5. Mở accordion 5 "Nhật ký" verify entries `INBOUND_DG_FAILED`.
- **Expected per case:**
  - **C1:** HTTP 401, `ma_loi:"ERR-DG-API-01"` "Unauthorized" (line 1034 nguyên văn).
  - **C2:** HTTP 400, `ma_loi:"ERR-DG-API-02"`, chi_tiet_loi="Dữ liệu không hợp lệ: ma_danh_gia_cong là bắt buộc" (line 1035 template).
  - **C3-C4:** HTTP 400, `ma_loi:"ERR-DG-API-03"`, message="Điểm đánh giá phải từ 1 đến 5" (line 1036 nguyên văn).
  - **C5:** HTTP 400, `ma_loi:"ERR-DG-API-04"`, message="Không tìm thấy hồ sơ tư vấn 'CONG-NOTFOUND-XYZ'" (line 1037 template).
  - **C6:** HTTP 400, `ma_loi:"ERR-DG-API-05"`, message="Đánh giá 'DG-CONG-EXIST-001' đã tồn tại" (line 1038 template). Phân biệt với GUI_LAI (TC-API-IN-007 = idempotent success).
  - **C7:** HTTP 400, `ma_loi:"ERR-DG-API-06"`, message="Đánh giá không ở trạng thái cho phép cập nhật" (line 1039 nguyên văn).
  - **C8:** HTTP 429 + `Retry-After`, `ma_loi:"ERR-DG-API-07"` (line 1040).
  - **STATE all cases:** Accordion 4 không đổi (Số lượng=1, Điểm TB=4.0). KHÔNG INSERT/UPDATE DANH_GIA_CHAT_LUONG_TV. CG profile điểm TB không đổi. AUDIT_LOG có entries failed (BR-DATA-05).
- **SRS ref:** UC153 line 1034-1040 (Error Handling 7 codes) + line 999 (Bước 3 điểm 1-5) + line 1007 (CAP_NHAT trạng thái hợp lệ) + line 1006 (TAO_MOI chưa tồn tại).
- **Notes:** Codex review fill 2026-05-09. Closes G5 (codex P0 GAP — biggest gap, cover toàn bộ 7 error codes UC153). Trigger qua Postman. Phân biệt rõ:
  - `ERR-DG-API-05` (TAO_MOI trùng) vs `GUI_LAI idempotent` (TC-API-IN-007): GUI_LAI trả `ket_qua=THANH_CONG` không ghi đè; TAO_MOI trùng trả `ket_qua=THAT_BAI ma_loi=ERR-DG-API-05`.
  - `ERR-DG-API-06` (CAP_NHAT sai trạng thái) vs `TC-API-IN-012` (CAP_NHAT happy): C7 negative khi đánh giá không ở trạng thái cho phép.

### TC-API-IN-012 — UC153 Edge CAP_NHAT: Cổng push DG hành động `CAP_NHAT` cho mã đã tồn tại → accordion update + count KHÔNG tăng + audit CAP_NHAT entry

- **Type:** Edge
- **Priority:** P1
- **Tài khoản:** cb_nv_tw_01
- **Preconditions:**
  - TVCS `tvcs-da-duyet-002` DA_DUYET, có 1 đánh giá `ma_danh_gia_cong = "DG-CONG-CN-001"`, diem_so=4, nhan_xet="Khá tốt".
  - Accordion 4 baseline: Số lượng=1, Điểm TB=4.0.
  - cb_nv_tw_01 mở SCR-X1-02 → accordion 4 quan sát baseline.
- **Test Data:** Payload UC153 hành động CAP_NHAT.
- **Steps:**
  1. Trigger API POST `/api/v1/inbound/danh-gia-chat-luong-tv` payload:
     ```
     {ma_noi_dung_cong: "CONG-DG-002", ma_danh_gia_cong: "DG-CONG-CN-001",
      diem_so: 5, nhan_xet: "Cập nhật: Rất tốt sau khi xem lại",
      ma_chuyen_gia: "CG001", ngay_danh_gia: "2026-05-07T09:00:00Z",
      hanh_dong: "CAP_NHAT"}
     ```
  2. Đợi 5-10s. Quan sát API response HTTP 200.
  3. Reload SCR-X1-02 → accordion 4 "Đánh giá CL".
  4. Verify giá trị field mới + count + Điểm TB.
  5. Mở accordion 5 "Nhật ký" / AUDIT_LOG.
  6. Verify CG profile điểm TB cập nhật (cross-FR-04).
- **Expected:**
  - **Bước 2:** API trả `ket_qua: "THANH_CONG"` (UC153 Step 6 line 1007 "Nếu CAP_NHAT: kiểm tra trạng thái hợp lệ → cập nhật bản ghi").
  - **Bước 3-4:** Accordion 4 vẫn 1 row với **dữ liệu MỚI**: Điểm=5 (đổi từ 4), Nhận xét="Cập nhật: Rất tốt sau khi xem lại" (đổi). Số lượng=1 (KHÔNG +1, vì cùng ma_danh_gia_cong). Điểm TB=5.0 (recalc).
  - **Bước 5:** AUDIT_LOG có entry `CAP_NHAT` với `du_lieu_cu={diem_so:4, nhan_xet:"Khá tốt"}` + `du_lieu_moi={diem_so:5, nhan_xet:"Cập nhật:..."}` (BR-DATA-05).
  - **Bước 6:** CG cg_01 profile điểm TB cập nhật theo điểm mới (UC153 Step 9 line 1010).
- **SRS ref:** UC153 Step 6 line 1006-1007 (Nếu CAP_NHAT: kiểm tra trạng thái hợp lệ → cập nhật) + AC line 1045-1046 (Given Cổng gửi đánh giá hành động When CAP_NHAT mã đã tồn tại Then cập nhật bản ghi + audit log).
- **Notes:** A6 fill A5-G9 (UC153 AC-2 CAP_NHAT explicit). Phân biệt với TC-API-IN-007 (GUI_LAI = idempotent no-overwrite) — CAP_NHAT = explicit overwrite + audit. Trigger qua Postman.

---

**Tổng số TC: 15**

**Phân bổ:**
- 🟢 UI Verify: 1 (TC-API-IN-001)
- 🟢 Happy: 3 (002, 005, 006)
- 🔴 Negative: 6 (003, 009, 011, 013, 014, 015)
- 🟡 Edge: 5 (004, 007, 008, 010, 012)

**Priority:** P0=6 (001, 002, 005, 006, 013, 015) / P1=8 (003, 004, 007, 009, 010, 011, 012, 014) / P2=1 (008)

**Coverage:**
- UC149 TVCS inbound: Happy + Duplicate ERR-TVCS-API-03 + Routing BR-ROUTE-TVCS-01 default Sở TP + **Negative matrix ERR-TVCS-API-01..05 + ERR-FILE-SIZE-01 + ERR-FILE-02** (TC-API-IN-013)
- UC151 HSPL inbound: Happy + ma_ho_so_cong + queue chờ xử lý CB NV + **Negative matrix ERR-HSPL-API-01/02/04 + ERR-FILE** (TC-API-IN-014)
- UC153 Đánh giá inbound: Happy TAO_MOI + Edge GUI_LAI idempotency + accordion read-only + CAP_NHAT happy + **Negative matrix ERR-DG-API-01..07 toàn bộ 7 error codes** (TC-API-IN-015)
- BR-NOTIF-01 (in-app + email TB CB NV): TC-API-IN-002, 005
- BR-DATA-04 (auto-gen TVCS-/HSPL-): TC-API-IN-002, 005
- BR-DATA-05 (audit log): mọi TC, kể cả failed inbound (013-015)
- BR-AUTH-08 multi-tenant + BR-ROUTE-TVCS-01 default routing: TC-API-IN-004
- Permission DANH_GIA C† chỉ qua Cổng (no internal CRUD): TC-API-IN-006 read-only verify

**SPEC-CLARIFY phát sinh trong file này:**
- SPEC-CLARIFY-HSPL-QUEUE — SRS không quote route UI "Danh sách chờ xử lý CB NV" cho HSPL inbound (UC151 Step 12). Phase B verify route hoặc fallback filter tab "Hồ sơ PL" `nguon=CONG_PLQG`.
- SPEC-CLARIFY-TVCS-API-PAYLOAD — SRS không quote payload size limit threshold (TC-API-IN-009). Phase B BA respond.
- (Tham chiếu hiện hữu: SPEC-CLARIFY-TVCS-09 — GUI_LAI conflict resolution.)

**A7 audit note:**
- Không có TC API curl thuần. Mọi TC verify SIDE-EFFECT UI (badge "Mới", count tab, accordion, notification, audit log).
- Trigger API là phương tiện setup data (Postman/test endpoint), KHÔNG phải step verify chính.
- Negative matrix TC (013-015) verify count UI = baseline + bell KHÔNG +1 → side-effect "no insert" cũng là UI verifiable.

*Tạo bởi BMAD A3 — 2026-05-06. Cập nhật A4 (+3 edge cases) + A6 (+2 fill gap) + A7 finalized 2026-05-07. Codex review 2026-05-09: +3 negative matrix TC (013/014/015) close G3/G4/G5 + fix TC-API-IN-009 ERR mapping + TC-API-IN-011 wording.*

---

**Tổng số TC: 15**
