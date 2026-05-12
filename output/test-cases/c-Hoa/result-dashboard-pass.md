# Test Cases PASS — dashboard
> **Nguồn**: result-dashboard-all.md
> **Ngày tổng hợp**: 2026-05-11
> **Phạm vi**: chỉ Result ∈ {PASS, PASS-DEVIATE, PASS-RESOLVED}

## Summary

| File test-case | PASS | PASS-DEVIATE | PASS-RESOLVED | Tổng PASS-class |
|----------------|------|--------------|---------------|-----------------|
| 01-TC-FR-I-01-04-vu-viec-hoi-dap | 4 | 0 | 0 | 4 |
| 02-TC-FR-I-05-07-khoa-hoc-tvv | 2 | 0 | 0 | 2 |
| 03-TC-FR-I-08-bieu-do-danh-gia-sla | 0 | 0 | 0 | 0 |
| 04-TC-FR-I-09-bieu-do-dao-tao | 2 | 0 | 0 | 2 |
| 05-TC-KPI-S-bo-sung | 1 | 0 | 0 | 1 |
| 06-TC-FR-I-CROSS-02-auto-refresh | 0 | 0 | 0 | 0 |
| 07-TC-SCR-I-01-bo-loc-header | 5 | 0 | 0 | 5 |
| 08-TC-permission-matrix | 0 | 0 | 0 | 0 |
| **Tổng** | **14** | **0** | **0** | **14** |

---

## 01-TC-FR-I-01-04-vu-viec-hoi-dap

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\dashboard\01-TC-FR-I-01-04-vu-viec-hoi-dap.md`
> Source report: ❌ MISSING (không có folder `report-01-TC-...`) — status suy ra từ `BUG-REPORT-TONG-HOP-FR01-2026-05-11.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-DASH-001 | FR-I-01 / Processing step 4 | KPI-01 đếm HD `MOI` đúng theo phạm vi đơn vị | cb_nv_tw_01 login. Năm hiện tại + Tháng "Tất cả". Có ≥3 HD trạng_thái=`MOI` thuộc TW. | Default filter | 1. Vào `/dashboard`. 2. Quan sát thẻ KPI-01 "Hỏi đáp / vướng mắc mới". | (1) `gia_tri` = số HD MOI thuộc phạm vi (toàn TW + cấp con per BR-AUTH-04). (2) `don_vi_tinh="yêu cầu"`. (3) `nhan="Hỏi đáp / vướng mắc mới"`. (4) Định dạng vi-VN. (5) Có chỉ dấu xu hướng so kỳ trước (TANG/GIAM/KHONG_DOI). | Happy 🔴 | PASS |  |
| TC-DASH-002 | FR-I-02 / Processing step 4 | KPI-02 đếm VV theo `ngay_tiep_nhan` trong kỳ | cb_nv_tw_01 login. Có ≥5 VV `ngay_tiep_nhan` ∈ kỳ hiện tại. | Default filter | 1. Vào `/dashboard`. 2. Quan sát thẻ KPI-02 "Vụ việc đã tiếp nhận". | (1) `gia_tri` = COUNT VV `ngay_tiep_nhan` ∈ [tu_ngay_boundary, den_ngay_boundary]. (2) `don_vi_tinh="vụ việc"`. (3) Áp BR-AUTH-08. | Happy 🔴 | PASS |  |
| TC-DASH-015 | FR-I-01..04 / E1 INFO-DASH-01 | Không có dữ liệu KPI → text "Chưa có dữ liệu trong kỳ" | cb_nv_tw_01 login. Đơn vị X=BTC không có HD/VV nào trong kỳ. | nam=2026, thang=1, don_vi_id=BTC | 1. Apply filter. 2. Quan sát các thẻ KPI. | (1) `gia_tri=0`. (2) UI text "0" + chú thích phụ "Chưa có dữ liệu trong kỳ" (E1 INFO-DASH-01). (3) Trend "—" (xám trung tính, không icon). | Negative 🟡 | PASS |  |
| TC-DASH-025 | FR-I-01 / BR-AUTH-08 (A4 merged) | BR-AUTH-08 — cb_nv_dp_01 (AG) chỉ đếm VV của AG, KHÔNG đếm BG | cb_nv_dp_01 (Sở TP An Giang) login. AG có 5 VV. BG (Bắc Giang) có 8 VV. | Default | 1. Vào `/dashboard`. 2. Quan sát KPI-02. | (1) KPI-02 = 5 (chỉ AG). (2) KPI không đếm 8 VV BG (BR-AUTH-08). (3) Chip phạm vi "Phạm vi: Sở Tư pháp An Giang". | Edge 🔴 | PASS |  |

---

## 02-TC-FR-I-05-07-khoa-hoc-tvv

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\dashboard\02-TC-FR-I-05-07-khoa-hoc-tvv.md`
> Source report: ❌ MISSING

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-DASH-030 | FR-I-05 / Processing step 4 + AC#1 | KPI-05 đếm KH `DANG_DIEN_RA` (ảnh chụp) | cb_nv_tw_01 login. Có ≥3 KH `DANG_DIEN_RA` thuộc TW (chế độ DP default). | Default | 1. Vào `/dashboard`. 2. Quan sát KPI-05 "Khóa đào tạo / tập huấn đang diễn ra". | (1) `gia_tri` = COUNT KH `DANG_DIEN_RA` thuộc phạm vi (DP scope). (2) `don_vi_tinh="khóa"`. (3) Chú thích phụ "Tính đến hôm nay (DD/MM/YYYY)". (4) Áp BR-AUTH-08. | Happy 🔴 | PASS |  |
| TC-DASH-031 | FR-I-06 / Processing step 4 | KPI-06 đếm KH `DA_KET_THUC` `ngay_ket_thuc` trong kỳ | cb_nv_tw_01 login. Có ≥2 KH `DA_KET_THUC` `ngay_ket_thuc` ∈ kỳ. | Default kỳ hiện tại | 1. Vào `/dashboard`. 2. Quan sát KPI-06. | (1) `gia_tri` = COUNT KH `DA_KET_THUC` & `ngay_ket_thuc` ∈ kỳ. (2) Filter ngày phát sinh. | Happy 🔴 | PASS |  |

---

## 04-TC-FR-I-09-bieu-do-dao-tao

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\dashboard\04-TC-FR-I-09-bieu-do-dao-tao.md`
> Source report: ❌ MISSING

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-DASH-080 | FR-I-09 / Processing step 2 + AC#1 (SRS line 543) | UC9 render donut 2 phần với center label + caption | cb_nv_tw_01 login. Có 50 học viên: 40 Đạt, 10 KHONG_DAT. Điểm TB=7,5/10. | Default | 1. Vào `/dashboard`. 2. Quan sát Vùng 5 — biểu đồ UC9. | (1) Donut 2 phần: "Đạt" 80% + "Không đạt" 20%. (2) Nhãn trung tâm "Điểm trung bình: 7,5/10". (3) Caption "Dựa trên 50 học viên". | Happy 🔴 | PASS |  |
| TC-DASH-081 | FR-I-09 / Processing step 2 (SRS line 516) | Tỷ lệ đạt counts 4 enum xếp loại + KHONG_DAT loại trừ | cb_nv_tw_01 login. 30 học viên: 5 GIOI + 10 KHA + 8 TRUNG_BINH + 2 DAT + 5 KHONG_DAT. | Default | 1. Apply. 2. Inspect ty_le_dat. | (1) Tử số = 25. (2) Mẫu số = 30. (3) ty_le_dat = 83,3%. | Happy 🔴 | PASS |  |

---

## 05-TC-KPI-S-bo-sung

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\dashboard\05-TC-KPI-S-bo-sung.md`
> Source report: ❌ MISSING

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-DASH-110 | KPI-S-01 / AC#3 (SRS line 590) | Mẫu số = 0 (không có vụ HT trong kỳ) → UI "—" | cb_nv_tw_01 login. Đơn vị X 0 vụ HT trong tháng 1. | nam=2026, thang=1, don_vi_id=X | 1. Apply. 2. Inspect KPI-S-01. | (1) `gia_tri=NULL`. (2) UI hiển thị "—". (3) Trend KHÔNG hiển thị. | Negative 🟡 | PASS |  |

---

## 07-TC-SCR-I-01-bo-loc-header

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\dashboard\07-TC-SCR-I-01-bo-loc-header.md`
> Source report: ❌ MISSING

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-DASH-160 | SCR-I-01 / Vùng 2 #8 (SRS line 742) | Đổi L1 → L2 tự reset "Tất cả [L1]" (pending) | cb_nv_tw_01 login. Đã chọn L1=DP, L2=ĐP X. | Đổi L1=BN | 1. Đã chọn L1=DP, L2=ĐP X. 2. Đổi L1 sang BN. 3. Inspect L2. | L2 tự đổi về "Tất cả bộ ngành" (pending). | Happy 🟡 | PASS |  |
| TC-DASH-161 | SCR-I-01 / Vùng 2 #6 (SRS line 740) | Năm hiện tại + Tháng tương lai → tự reset Tháng "Tất cả" | cb_nv_tw_01 login. Đang chọn Năm=2025, Tháng=10. | Đổi Năm=2026 | 1. Đang ở Năm=2025+Tháng=10. 2. Đổi Năm=2026. 3. Inspect Tháng. | Tháng tự reset về "Tất cả". | Happy 🔴 | PASS |  |
| TC-DASH-162 | SCR-I-01 / Vùng 1 #5 (SRS line 717) (A4 merged) | Chip phạm vi truncate >25 ký tự + tooltip full | cb_nv_tw_01 login. ĐP có tên dài. | L2=ĐP đó | 1. Apply. 2. Hover chip. | (1) Chip text truncated. (2) Hover tooltip full name. | Edge 🟡 | PASS |  |
| TC-DASH-163 | SCR-I-01 / Vùng 2 user BN/DP locked (SRS line 770) (A4 merged) | User BN/DP login → L1+L2 disabled, KHÔNG nhãn phụ | cb_nv_dp_01 (AG) login. | — | 1. Vào `/dashboard`. 2. Inspect dropdown L1+L2. | (1) L1 dropdown mờ. (2) L2 dropdown mờ. (3) KHÔNG nhãn phụ "(khoá theo đơn vị bạn)". | Edge 🔴 | PASS |  |
| TC-DASH-170 | SCR-I-01 / Multi-tab độc lập (SRS line 853) (A4 merged) | 2 tab giữ filter state riêng (KHÔNG sync cross-tab) | cb_nv_tw_01 login. | Tab1: Năm=2026 / Tab2: Năm=2025 | 1. Mở 2 tab `/dashboard`. 2. Tab1 Năm=2026 Apply. 3. Tab2 Năm=2025 Apply. 4. Đổi qua Tab1. | (1) Tab1 vẫn giữ filter Năm=2026. (2) Tab2 vẫn Năm=2025. | Edge 🟡 | PASS |  |

---

## Skipped

Các file test-case sau không có TC PASS / PASS-DEVIATE / PASS-RESOLVED nào:

- **03-TC-FR-I-08-bieu-do-danh-gia-sla** — 0 PASS (toàn bộ NOT-EXECUTED hoặc FAIL trong source).
- **06-TC-FR-I-CROSS-02-auto-refresh** — 0 PASS (toàn bộ DEFERRED do thiếu stub backend 5xx hoặc NOT-EXECUTED).
- **08-TC-permission-matrix** — 0 PASS (toàn bộ NOT-EXECUTED — orphan TC-DASH-200/201 trong BUG report không thuộc test-case file này).
