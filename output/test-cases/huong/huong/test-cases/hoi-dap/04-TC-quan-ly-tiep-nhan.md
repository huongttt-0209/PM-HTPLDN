# Test Cases — FR-II-04 (UC13): Quản lý thông tin tiếp nhận xử lý

> **SRS Ref**: FR-II-04 (lines 339-427), SCR-II-02 dòng 13 (Cập nhật thời hạn) + dòng 13a (Đổi mức độ phức tạp) + dòng 27 (Lịch sử xử lý), SCR-II-01 cột Cảnh báo (dòng 26) + filter Đang xử lý
> **Ngày tạo**: 2026-05-10
> **Đặc thù**:
> - **Cập nhật thời hạn**: state ∈ {TIEP_NHAN, DANG_XU_LY}, optimistic locking (F-40), `thoi_han_moi > NOW()`, lý do 10-500 ký, ERR-TH-01/02/03/CONFLICT.
> - **Đổi muc_do_phuc_tap (BR-CALC-04)**: state ∈ {TIEP_NHAN, DANG_XU_LY}, lý do bắt buộc 10-500 ký, tính lại `deadline = ngay_tiep_nhan + N_mới` (BR-CALC-03).
> - **Xem lịch sử**: timeline AUDIT_LOG (thời gian, người, hành động, cũ→mới).
> - **Filter danh sách Đang xử lý**: trang_thai cứng IN (TIEP_NHAN, DANG_XU_LY).

---

## Quy ước

- **Priority**: 🔴 P0 · 🟡 P1 · 🟢 P2
- **TraceID**: `FR-II-04 / {section}`
- **Pre-conditions**: User CB_NV_{cap} cùng đơn vị bản ghi (BR-AUTH-08).

---

## Trường input

**Filter danh sách Đang xử lý** (giống FR-II-05):

| # | Field | Bắt buộc | Kiểu | Ràng buộc |
|---|-------|----------|------|-----------|
| 1 | trang_thai_filter | Y (auto) | enum | Cứng IN (TIEP_NHAN, DANG_XU_LY) |
| 2-7 | keyword/linh_vuc/tu_ngay/den_ngay/page/page_size | N | mixed | Như FR-II-05 |

**Cập nhật thời hạn xử lý**:

| # | Field | Bắt buộc | Kiểu | Ràng buộc |
|---|-------|----------|------|-----------|
| 1 | hoi_dap_id | Y | identifier | URL/system |
| 2 | thoi_han_moi | Y | date | dd/mm/yyyy, > NOW() |
| 3 | ly_do_thay_doi | Y | text | Min 10, max 500 ký |
| 4 | version | Y (hidden) | number | Optimistic locking |

**Đổi mức độ phức tạp**:

| # | Field | Bắt buộc | Kiểu | Ràng buộc |
|---|-------|----------|------|-----------|
| 1 | hoi_dap_id | Y | identifier | URL/system |
| 2 | muc_do_phuc_tap | Y | enum 2 | THUONG / PHUC_TAP (radio) |
| 3 | ly_do | Y | text | Min 10, max 500 ký |
| 4 | version | Y (hidden) | number | Optimistic locking |

---

## A. CẬP NHẬT THỜI HẠN XỬ LÝ — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-DXL-001 | FR-II-04 / Processing Cập nhật thời hạn step 1-7 | Cập nhật thời hạn xử lý mới — happy | cb_nv_tw_01 login. HD-X state TIEP_NHAN, deadline cũ=2026-04-30. | thoi_han_moi=2026-05-15, ly_do="Cần thêm thời gian thu thập VBPL" (33 ký) | 1. SCR-II-02 HD-X. 2. Click [Cập nhật thời hạn]. 3. Modal mở. 4. Date-picker chọn 15/05. 5. Nhập lý do. 6. Lưu. | (1) PUT /hoi-dap/{id}/cap-nhat-thoi-han thành công. (3) Modal đóng + toast "Đã cập nhật thời hạn". `deadline=2026-05-15`. version+=1. (4) Audit log entry: "Cập nhật thời hạn 2026-04-30 → 2026-05-15. Lý do: Cần thêm...". (5) Thông báo người được phân công nếu có (BR-DATA-05). | Happy 🔴 |
| TC-DXL-002 | FR-II-04 / Processing Xem lịch sử | Xem timeline AUDIT_LOG (Lịch sử xử lý) | cb_nv_tw_01 login. HD-Y có ≥3 audit entries (CREATE → TIEP_NHAN → PHAN_CONG). | — | 1. SCR-II-02 HD-Y. 2. Click expand Accordion "Lịch sử xử lý" dòng 27. | (3) Timeline render từ AUDIT_LOG: thời gian (dd/mm/yyyy HH:mm), người (ho_ten + role), hành động (CREATE/TIEP_NHAN/PHAN_CONG), giá trị cũ→mới. Tự cuộn entry mới nhất. | Happy 🟡 |
| TC-DXL-003 | FR-II-04 / Filter cứng | Tab "Đang xử lý" filter cứng + filter user | cb_nv_tw_01 login. ≥10 HD scope TW: 4 TIEP_NHAN + 6 DANG_XU_LY + 3 khác state. | linh_vuc=Đất đai filter user thêm | 1. Tab "Đang xử lý". 2. Apply filter Lĩnh vực. | (3) AND logic: 10 records (TIEP_NHAN OR DANG_XU_LY) + thêm filter user → giảm scope. URL `?tab=dang-xu-ly&linh_vuc=...`. | Happy 🟡 |

---

## B. CẬP NHẬT THỜI HẠN — NEGATIVE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-DXL-100 | FR-II-04 / E5 ERR-TH-01 | thoi_han_moi <= ngày hiện tại | cb_nv_tw_01 login. HD-A state DANG_XU_LY. NOW=2026-05-10. | thoi_han_moi=2026-05-08 (quá khứ) | 1. Mở modal Cập nhật. 2. Chọn date past. 3. Lưu. | (2) Inline error đỏ dưới date-picker: **"Thời hạn mới phải sau ngày hiện tại"** (ERR-TH-01). KHÔNG PUT. | Negative 🔴 |
| TC-DXL-101 | FR-II-04 / E6 ERR-TH-02 | ly_do < 10 ký | cb_nv_tw_01 login. HD-B DANG_XU_LY. | thoi_han_moi=2026-06-01, ly_do="ngắn" (5 ký) | 1. Nhập lý do 5 ký. 2. Lưu. | (2) Inline error: **"Lý do thay đổi phải từ 10 đến 500 ký tự"** (ERR-TH-02). | Negative 🔴 |
| TC-DXL-102 | FR-II-04 / E6 ERR-TH-02 | ly_do > 500 ký | cb_nv_tw_01 login. HD-C DANG_XU_LY. | ly_do=501 ký | 1. Paste 501 ký. 2. Counter `501/500` đỏ. 3. Lưu. | (2) Counter đỏ + nút disabled HOẶC submit reject ERR-TH-02. | Negative 🟡 |
| TC-DXL-103 | FR-II-04 / E7 ERR-TH-03 | Cập nhật thời hạn state ngoài (vd CHO_PHE_DUYET) | cb_nv_tw_01 login. HD-D state CHO_PHE_DUYET. | — | 1. Mở SCR-II-02 HD-D. | (2) Nút [Cập nhật thời hạn] KHÔNG hiển thị. Force PUT API → ERR-TH-03 **"Không thể cập nhật thời hạn cho bản ghi ở trạng thái 'Chờ phê duyệt'"**. | Negative 🟡 |
| TC-DXL-104 | FR-II-04 / E4 ERR-TH-CONFLICT (F-40) | Concurrent update — version mismatch HTTP 409 | cb_nv_tw_01 + cb_nv_tw_02 cùng mở modal Cập nhật HD-E (DANG_XU_LY). | cb_nv_tw_01 thoi_han=2026-06-01, cb_nv_tw_02 thoi_han=2026-06-15 | 1. cb_nv_tw_01 Lưu (version+=1). 2. cb_nv_tw_02 Lưu sau. | (2) cb_nv_tw_02 nhận HTTP 409 ERR-TH-CONFLICT. Toast persistent: **"Thời hạn đã bị thay đổi bởi cb_nv_tw_01 lúc {time} thành 2026-06-01. Vui lòng Tải lại hoặc Ghi đè"**. 2 nút "Tải lại" (reload form) / "Ghi đè" (force update, audit log flag `force=true`). | Negative 🔴 |

---

## C. ĐỔI MỨC ĐỘ PHỨC TẠP (BR-CALC-04) — HAPPY + NEGATIVE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-DXL-110 | FR-II-04 / SCR-II-02 dòng 13a + BR-CALC-04 | Đổi THUONG → PHUC_TAP → tính lại deadline +30 LV | cb_nv_tw_01 login. HD-F state TIEP_NHAN, muc_do_phuc_tap=THUONG, ngay_tiep_nhan=2026-05-01, deadline cũ=ngay_tiep_nhan+15LV. | muc_do_phuc_tap=PHUC_TAP, ly_do="Sau khi nghiên cứu, vướng mắc liên quan đến nhiều ngành luật" (60 ký) | 1. SCR-II-02. 2. Click [Đổi mức độ phức tạp]. 3. Modal: chọn radio PHUC_TAP. 4. Nhập lý do. 5. Warning hiển thị "Đổi mức độ sẽ tính lại hạn xử lý theo mức độ phức tạp mới". 6. Lưu. | (1) PUT thành công. (3) `muc_do_phuc_tap=PHUC_TAP`, `deadline = 2026-05-01 + 30 LV` (skip CN/Thứ 7/lễ). Audit log: "Đổi mức độ THUONG → PHUC_TAP. Lý do: ...". | Happy 🔴 |
| TC-DXL-111 | FR-II-04 / BR-CALC-04 reverse | Đổi PHUC_TAP → THUONG → tính lại deadline -15 LV | cb_nv_dp_01 login. HD-G state DANG_XU_LY, muc_do_phuc_tap=PHUC_TAP, ngay_tiep_nhan=2026-05-01, deadline cũ=+30LV. | muc_do_phuc_tap=THUONG, ly_do="Sau khi rà soát, vướng mắc thuộc 1 ngành đơn giản" (50 ký) | 1. Click [Đổi mức độ]. 2. Chọn THUONG. 3. Lưu. | (3) `muc_do_phuc_tap=THUONG`, `deadline = 2026-05-01 + 15 LV`. Audit log. | Happy 🟡 |
| TC-DXL-112 | FR-II-04 / BR-CALC-04 state ngoài | Đổi mức độ state CHO_PHE_DUYET → cấm | cb_nv_tw_01 login. HD-H state CHO_PHE_DUYET. | — | 1. Mở SCR-II-02 HD-H. | (2) Nút [Đổi mức độ phức tạp] KHÔNG hiển thị (state ngoài {TIEP_NHAN, DANG_XU_LY}, BR-CALC-04). | Negative 🟡 |
| TC-DXL-113 | FR-II-04 / BR-CALC-04 ly_do | Đổi mức độ thiếu lý do | cb_nv_tw_01 login. HD-I TIEP_NHAN. | ly_do="" hoặc <10 ký | 1. Mở modal. 2. Chọn radio mới. 3. Bỏ trống lý do. 4. Lưu. | (2) Inline error: **"Lý do bắt buộc, từ 10 đến 500 ký tự"** (BR-CALC-04). KHÔNG PUT. | Negative 🟡 |

---

## D. EDGE & BOUNDARY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-DXL-200 | FR-II-04 / E1 ERR-DXL-01 (filter) | Filter tu_ngay > den_ngay | cb_nv_tw_01 login. Tab Đang xử lý. | từ=15/04, đến=10/04 | 1. Apply filter. | (2) Inline error ERR-DXL-01 "Ngày bắt đầu phải trước ngày kết thúc". | Negative 🟡 |
| TC-DXL-201 | FR-II-04 / E2 INF-DXL-01 | Filter empty result | cb_nv_tw_01 login. Tab Đang xử lý + filter Lĩnh vực="Hôn nhân". Không có HD. | — | 1. Apply. | (3) Empty: "Không có hỏi đáp đang xử lý phù hợp" (INF-DXL-01). | Negative 🟢 |
| TC-DXL-202 | FR-II-04 / E3 ERR-AUTH-DXL-01 | Cross-tenant filter scope | cb_nv_dp_02 (BG) login. | — | 1. Tab Đang xử lý. | (3) Chỉ records BG. (2) Force API params `?don_vi_id=AG` → ERR-AUTH-DXL-01 (nếu có UI bypass). | Negative 🟡 |
| TC-DXL-203 | FR-II-04 / Inputs #2 boundary | thoi_han_moi = NOW + 1 phút (boundary) | cb_nv_tw_01 login. HD-J DANG_XU_LY. | thoi_han_moi=NOW+1phút | 1. Lưu. | (3) BE check `thoi_han_moi > NOW()` — pass nếu > NOW chính xác đến giây. PASS. | Edge 🟢 |
| TC-DXL-204 | FR-II-04 / SCR-II-01 row 26 | Badge cảnh báo cột "Còn N ngày" hiển thị | cb_nv_tw_01 login. SCR-II-01. HD: 1 deadline +5 ngày + 1 deadline = hôm nay + 1 deadline -3 ngày. | — | 1. Verify cột Cảnh báo. | (3) "Còn 5 ngày" (xanh BINH_THUONG nếu >50% còn lại), "Hết hạn hôm nay" (vàng/đỏ tùy %), "Quá 3 ngày" (đỏ QUA_HAN). Tooltip "Hạn xử lý: dd/mm/yyyy". | Edge 🟡 |
| TC-DXL-205 | FR-II-04 / FR-II-CROSS-01 | SLA scheduled job auto chuyển mức cảnh báo | cb_nv_tw_01 login. HD-K muc_do_phuc_tap=THUONG, deadline 2026-05-15, đã qua 8/15 ngày (>50%). | — | 1. Trigger SLA scan (manual hoặc wait 30 phút). 2. Reload SCR-II-01. | (3) `muc_do_canh_bao` chuyển BINH_THUONG → SAP_HET_HAN (vàng). Notification in-app cho người được phân công (BR-SLA-03). | Edge 🟡 |

---

---

## E. EDGE BỔ SUNG (A4 + A6 merged 2026-05-10)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-DXL-206 | FR-II-04 / Inputs #2 boundary | thoi_han_moi = ngay_tiep_nhan (boundary) | cb_nv_tw_01 login. HD-K state TIEP_NHAN, ngay_tiep_nhan=2026-05-01. | thoi_han_moi=2026-05-01 (= ngay_tiep_nhan) | 1. Modal Cập nhật. 2. Date 01/05. 3. Submit. | (2) ERR-TH-01 vì thoi_han_moi <= NOW (giả sử NOW > 2026-05-01). Hoặc PASS nếu NOW = 2026-05-01. Verify boundary condition `> NOW()`. | Edge 🟢 |
| TC-DXL-207 | FR-II-04 / SCR-II-02 dòng 27 pagination | Lịch sử có ≥100 entries | qtht_01 login. HD-J có 105 audit entries (CRUD nhiều lần). | — | 1. Click Accordion Lịch sử. | (3) UI render: hoặc scrolling list (lazy load) hoặc pagination. SPEC-CLARIFY-DXL-04 cho UX. | Edge 🟢 |
| TC-DXL-208 | FR-II-04 / BR-CALC-04 spam | Đổi mức độ liên tục 5 lần trong 1 phút | cb_nv_tw_01 login. HD-I TIEP_NHAN. | 5 lần đổi THUONG↔PHUC_TAP | 1. Đổi liên tục 5 lần (mỗi lần ly_do 10 ký). | (3) Audit log đầy đủ 5 entries. Deadline cuối cùng tính theo mức độ thứ 5. Optimistic locking đảm bảo không race. | Edge 🟢 |
| TC-DXL-209 | FR-II-04 / Inputs #2 upper bound / SPEC-CLARIFY-DXL-03 | thoi_han_moi xa 10 năm sau | cb_nv_tw_01 login. HD-H DANG_XU_LY. | thoi_han_moi=2036-05-10 | 1. Submit. | (3) BE behavior: hoặc accept (không upper bound trong SRS) hoặc reject với validation message. **SPEC-CLARIFY-DXL-03**. | Edge 🟢 |
| TC-DXL-210 | FR-II-04 / BR-SLA-02 mức QUA_HAN_NGHIEM_TRONG (GAP-A5-01 fix) | Cảnh báo SLA mức 4 (QUA_HAN_NGHIEM_TRONG) | cb_nv_tw_01 login. HD-G muc_do_phuc_tap=THUONG, deadline 2026-04-01 (đã qua >200% so với 15 LV). | — | 1. SCR-II-01. 2. Verify cột 26 cho HD-G. | (3) Badge "Quá N ngày" với màu hồng tím/đen (QUA_HAN_NGHIEM_TRONG). Tooltip "Hạn xử lý: 01/04/2026". `muc_do_canh_bao = QUA_HAN_NGHIEM_TRONG`. (4) BR-SLA-03 escalate notification cấp trên. | Edge 🔴 |
| TC-DXL-211 | FR-II-04 / BR-SLA-03 email verify (GAP-A5-02 fix) | Email cảnh báo SLA gửi qua MailHog | cb_nv_tw_01 login. HD-F vừa chuyển mức cảnh báo SAP_HET_HAN. SLA scan 30 phút trigger. | — | 1. Trigger SLA scan. 2. Mở MailHog `http://103.172.236.130:8025`. 3. Verify inbox cb_nv_tw_01@hoaag.vn. | (3) Email subject "Cảnh báo SLA: Hỏi đáp #{ma} sắp hết hạn" + body chứa thông tin HD + nút Link to detail. Verify CC CB PD cùng cấp. | Edge 🟡 (env-dependent) |

---

## Tổng kết file 04

- **Tổng số TC: 25** (3 Happy + 5 Negative cập nhật + 4 Đổi mức độ + 7 Edge/filter + 6 A4/A6 merged)
- **Critical TC (🔴)**: TC-DXL-001, 100, 101, 104, 110, 210
- **Coverage**: FR-II-04 cập nhật + đổi mức độ + xem lịch sử + filter Đang xử lý + cảnh báo 4 mức cột 26 SCR-II-01 (✅ TC-DXL-210 fix GAP-A5-01) + cross-ref FR-II-CROSS-01 SLA + email notification (TC-DXL-211 fix GAP-A5-02)
- **Error codes**: ERR-TH-01, 02, 03, CONFLICT, ERR-DXL-01, INF-DXL-01, ERR-AUTH-DXL-01, BR-CALC-04 ly_do
- **F-40 optimistic locking** verified TC-DXL-104
- **A6 merged 2026-05-10**: TC-DXL-210 (BR-SLA-02 mức 4), TC-DXL-211 (BR-SLA-03 email)

*Generated 2026-05-10 — Phase A step A3 + A4 + A6 GAP fix*
