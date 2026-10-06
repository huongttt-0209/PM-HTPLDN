# Test Cases — FR-II-03 (UC12): Tiếp nhận xử lý Hỏi đáp

> **SRS Ref**: FR-II-03 (lines 274-336), SCR-II-02 dòng 9 nút "Tiếp nhận", SM-HOIDAP transition `MOI → TIEP_NHAN`
> **Ngày tạo**: 2026-05-10
> **Đặc thù**: Transition `MOI → TIEP_NHAN` + tính `deadline = ngay_tiep_nhan + N ngày LV` theo `muc_do_phuc_tap`. **N=15 nếu THUONG, N=30 nếu PHUC_TAP** (BR-CALC-03 + NĐ55/2019 Đ.8 K.1). Optimistic locking → ERR-TN-03 nếu 2 CB đồng thời. Modal nhỏ với textarea `ghi_chu_tiep_nhan` (max 1000 ký, counter `{n}/1000`). Cross-ref FR-II-CROSS-01 SLA scheduled job.

---

## Quy ước

- **Priority**: 🔴 P0 · 🟡 P1 · 🟢 P2
- **TraceID**: `FR-II-03 / {section}`
- **Pre-conditions**: User login CB_NV_{cap} cùng đơn vị bản ghi (`user.don_vi_id = record.don_vi_id`).

---

## Trường input

| # | Field | Bắt buộc | Kiểu | Ràng buộc |
|---|-------|----------|------|-----------|
| 1 | hoi_dap_id | Y | identifier | URL/system |
| 2 | ghi_chu_tiep_nhan | N | text | Max 1000 ký, counter `{n}/1000` (F-14) |

---

## A. TIẾP NHẬN — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-TN-001 | FR-II-03 / AC #2 + BR-CALC-03 (THUONG) | Tiếp nhận MOI → TIEP_NHAN với muc_do_phuc_tap=THUONG → deadline +15 ngày LV | cb_nv_tw_01 login. HD-X state MOI, muc_do_phuc_tap=THUONG, ngay_tao=2026-04-15 (Thứ Tư). CAU_HINH_SLA[HOI_DAP_THUONG]=15. | — | 1. Mở SCR-II-02 HD-X. 2. Click [Tiếp nhận]. 3. Modal mở (ghi_chu trống OK). 4. Click [Xác nhận tiếp nhận]. | (1) PUT /hoi-dap/{id}/tiep-nhan thành công. (2) Modal đóng + toast "Đã tiếp nhận". (3) State badge → "Tiếp nhận" (xanh lá). `nguoi_tiep_nhan_id=cb_nv_tw_01`, `ngay_tiep_nhan=NOW()`, `deadline = ngay_tiep_nhan + 15 ngày LV`. (4) Audit log INSERT action='TIEP_NHAN'. | Happy 🔴 |
| TC-TN-002 | FR-II-03 / AC #3 + BR-CALC-03 (PHUC_TAP) | Tiếp nhận với muc_do_phuc_tap=PHUC_TAP → deadline +30 ngày LV (NĐ55/2019 Đ.8 K.1) | cb_nv_dp_01 login. HD-Y state MOI, muc_do_phuc_tap=PHUC_TAP, ngay_tao=2026-04-01. CAU_HINH_SLA[HOI_DAP_PHUC_TAP]=30. | — | 1. Click [Tiếp nhận]. 2. Confirm. | (3) `deadline = ngay_tiep_nhan + 30 ngày LV` (loại trừ Thứ 7, CN, ngày lễ VN — BR-SLA-04). Hiển thị "Hạn xử lý: dd/mm/yyyy" tooltip. | Happy 🔴 |
| TC-TN-003 | FR-II-03 / AC #1 | Hiển thị danh sách chờ tiếp nhận (Tab Mới) | cb_nv_tw_01 login. ≥3 HD state MOI thuộc TW. | — | 1. SCR-II-01 click tab "Mới". | (3) Tab badge "(3)" + danh sách records MOI. Mỗi record có nút Xem → SCR-II-02 với nút [Tiếp nhận] enabled. | Happy 🟡 |
| TC-TN-004 | FR-II-03 / Inputs #2 | Tiếp nhận với ghi_chu_tiep_nhan có nội dung | cb_nv_tw_01 login. HD-Z state MOI. | ghi_chu="Đã chuyển cho Phòng Pháp chế xem xét sơ bộ" | 1. Click [Tiếp nhận]. 2. Nhập ghi chú. 3. Counter `54/1000`. 4. Confirm. | (1) PUT thành công. (4) Audit log lưu `ghi_chu_tiep_nhan` trong action payload. | Happy 🟡 |

---

## B. TIẾP NHẬN — NEGATIVE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-TN-100 | FR-II-03 / E1 ERR-TN-01 | Tiếp nhận state ≠ MOI (vd TIEP_NHAN) | cb_nv_tw_01 login. HD-A state TIEP_NHAN. | — | 1. Mở SCR-II-02 HD-A. | (2) Nút [Tiếp nhận] KHÔNG hiển thị (Điều kiện hiển thị: state=MOI). Force PUT API → ERR-TN-01 **"Hỏi đáp đã được tiếp nhận bởi {người khác}"**. | Negative 🔴 |
| TC-TN-101 | FR-II-03 / E2 ERR-TN-02 + F-14 | HD đã bị xóa giữa chừng | cb_nv_tw_01 mở SCR-II-02 HD-B (MOI). cb_nv_tw_02 xóa HD-B (soft delete) song song. | — | 1. cb_nv_tw_01 click [Tiếp nhận] sau khi cb_nv_tw_02 đã xóa. | (2) Server reject ERR-TN-02. UI: đóng modal tiếp nhận + mở modal lỗi **"Hỏi đáp này không còn tồn tại (đã bị xóa hoặc không có quyền truy cập)"** + nút "Về danh sách" → SCR-II-01 (F-14). | Negative 🔴 |
| TC-TN-102 | FR-II-03 / EC-01 ERR-TN-03 | Concurrent — 2 CB tiếp nhận cùng lúc | cb_nv_tw_01 + cb_nv_tw_02 mở SCR-II-02 HD-C (MOI) đồng thời. | — | 1. cb_nv_tw_01 click Tiếp nhận. 2. **Trước khi PUT response**, cb_nv_tw_02 cũng click Tiếp nhận. | (2) Optimistic locking — version mismatch. Người thứ 2 nhận ERR-TN-03 **"Bản ghi đã được tiếp nhận bởi người khác"**. UI: toast persistent + nút Tải lại để reload state mới (TIEP_NHAN by cb_nv_tw_01). | Negative 🔴 |
| TC-TN-103 | FR-II-03 / BR-AUTH-08 cross-tenant | cb_nv_dp_02 (BG) attempt tiếp nhận HD-AG | cb_nv_dp_01 (AG) tạo HD-AG state MOI. cb_nv_dp_02 paste URL `/hoi-dap/HD-AG-id`. | — | 1. cb_nv_dp_02 mở SCR-II-02. | (2) HTTP 404 (BR-AUTH-08 IDOR block). UI dòng 30: "Hỏi đáp #{id} không tồn tại hoặc đã bị xóa". KHÔNG hiển thị nút Tiếp nhận. | Negative 🔴 |
| TC-TN-104 | FR-II-03 / Permission CB_PD | CB_PD attempt Tiếp nhận | cb_pd_tw_01 login. HD-D state MOI scope TW. | — | 1. Mở SCR-II-02 HD-D. | (2) Nút [Tiếp nhận] KHÔNG hiển thị (chỉ CB_NV cùng đơn vị). | Negative 🟡 |

---

## C. TIẾP NHẬN — EDGE & BOUNDARY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-TN-200 | FR-II-03 / BR-SLA-04 (line 1663 "Ngày làm việc: Thứ 2-6, trừ ngày lễ") | Tiếp nhận trên ngày Thứ 7 → deadline tính đúng skip CN/Thứ 7 + ngày lễ | cb_nv_tw_01 login. HD-E state MOI, muc_do_phuc_tap=THUONG. Tiếp nhận vào Thứ 7 (vd 2026-04-18). | — | 1. Tiếp nhận. | (3) `deadline = 2026-04-18 + 15 ngày LV` đếm chỉ Thứ 2-6, skip Thứ 7 + CN + ngày lễ 30/4 + 1/5. **Expected: Thứ 2 ngày 12/05/2026** (15 working days từ Mon 20/04: Mon 20/04 + 4 days week 1 → Mon 27/04..Tue 28/04..Wed 29/04 [skip 30/4 lễ + 1/5 lễ] → Mon 04/05..Fri 08/05 → Mon 11/05..Tue 12/05 = ngày làm việc thứ 15). KHÔNG bao giờ deadline rơi vào Thứ 7/CN/lễ. | Edge 🟡 |
| TC-TN-201 | FR-II-03 / BR-SLA-04 ngày lễ | Tiếp nhận trước ngày lễ 30/4-1/5 | cb_nv_tw_01 login. HD-F state MOI, muc_do_phuc_tap=THUONG. Tiếp nhận ngày 28/04/2026 (Thứ Ba). | — | 1. Tiếp nhận. | (3) `deadline` skip 30/4 + 1/5 (ngày lễ VN) → đẩy thêm 2 ngày. Verify CAU_HINH_SLA load lịch lễ VN từ DM_NGAY_LE. | Edge 🟡 |
| TC-TN-202 | FR-II-03 / Inputs #2 boundary | ghi_chu_tiep_nhan exact 1000 ký | cb_nv_tw_01 login. HD-G MOI. | ghi_chu=1000 ký | 1. Paste 1000 ký. 2. Counter `1000/1000` (đỏ ở 1001). 3. Confirm. | (3) Tiếp nhận OK. Audit log lưu full 1000 ký. | Edge 🟢 |
| TC-TN-203 | FR-II-03 / Inputs #2 over-cap | ghi_chu_tiep_nhan 1001 ký | cb_nv_tw_01 login. HD-H MOI. | ghi_chu=1001 ký | 1. Paste 1001 ký. | (2) Counter `1001/1000` đỏ + nút Xác nhận disabled (F-14 block submit khi vượt). | Edge 🟢 |
| TC-TN-204 | FR-II-03 / FR-II-CROSS-01 cross-ref | Sau Tiếp nhận → SLA scheduled job tính cảnh báo BINH_THUONG | cb_nv_tw_01 login. HD-I MOI vừa tiếp nhận. | — | 1. Tiếp nhận. 2. Wait 30 phút (hoặc trigger manual SLA scan). 3. Reload SCR-II-01. | (3) Cột "Cảnh báo thời hạn xử lý" hiển thị badge "Còn N ngày" (xanh lá BINH_THUONG, vì >50% còn lại). Tooltip "Hạn xử lý: dd/mm/yyyy". | Edge 🟡 |
| TC-TN-205 | FR-II-03 / Inputs #1 missing ID | URL không có ID hợp lệ | cb_nv_tw_01 login. | URL `/hoi-dap/INVALID` | 1. Paste URL. | (2) UI dòng 30: error block "Hỏi đáp #INVALID không tồn tại hoặc đã bị xóa" + nút "Về danh sách". | Edge 🟢 |

---

---

## D. EDGE BỔ SUNG (A4 merged 2026-05-10)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-TN-206 | FR-II-03 / Same-day boundary | Tiếp nhận HD vừa tạo cùng ngày | cb_nv_tw_01 login. HD-NEW vừa tạo lúc 09:00. | — | 1. Tiếp nhận lúc 09:05. | (3) `ngay_tao = ngay_tiep_nhan = 2026-05-10`. Deadline = 2026-05-10 + 15 LV. OK. | Edge 🟢 |
| TC-TN-207 | FR-II-03 / File ClamAV pending | Tiếp nhận HD có file đang scan ClamAV | cb_nv_tw_01 login. HD-X MOI có 1 file `clamav_status=PENDING`. | — | 1. Tiếp nhận. | (3) BE allow tiếp nhận (ClamAV không block transition). File status update sau. | Edge 🟢 |
| TC-TN-208 | FR-II-03 / Boundary 23:59:59 | Tiếp nhận lúc 23:59:59 cuối ngày → deadline tính từ ngày kế | cb_nv_tw_01 login. HD-Y MOI. NOW=2026-05-10 23:59:59. | — | 1. Tiếp nhận. | (3) `ngay_tiep_nhan=2026-05-10 23:59:59`. Deadline tính từ 2026-05-10 + 15 LV (skip CN/Thứ 7). Verify boundary correctly count. | Edge 🟢 |

---

## Tổng kết file 03

- **Tổng số TC: 17** (4 Happy + 5 Negative + 5 Edge + 3 A4 merged)
- **Critical TC (🔴)**: TC-TN-001, 002, 100, 101, 102, 103
- **Coverage**: BR-CALC-03 (15/30 ngày LV), BR-SLA-04 (skip cuối tuần + ngày lễ), BR-AUTH-08, FR-II-CROSS-01 cross-ref, optimistic locking
- **Error codes**: ERR-TN-01, ERR-TN-02, ERR-TN-03, F-14 modal
- **SPEC-CLARIFY**: TN-01 (CAU_HINH_SLA load lịch lễ VN từ đâu — DM_NGAY_LE entity?)

*Generated 2026-05-10 — Phase A step A3*
