# Test Cases — FR-IV-09 + FR-IV-CROSS-01: Đánh giá TVV (3 điểm 1-5) + Tổng hợp điểm TB

> **SRS Ref**: FR-IV-09 (UC47), FR-IV-CROSS-01, SCR-IV-03 Tab Đánh giá, Entity DANH_GIA_SAU_VU_VIEC, BR-CALC-06
> **Nguồn**: NotebookLM `4dd0675e-a4fa-4ea6-80ae-48e76b3fa264` + LOCAL `srs-fr-04-chuyen-gia-tvv- v3.1.md:688-746 + 924-947`
> **Ngày tạo**: 2026-05-09

---

## A. UI FIELD VERIFICATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-DG-UI-01 | FR-IV-09 / SCR-IV-03 Tab Đánh giá / UI 3 star + thống kê | Verify Tab Đánh giá form 3 star + danh sách | tvv login chuyên trang DN, hoặc qtht_01 view, TVV-TW-700 HOAT_DONG có ≥2 đánh giá | — | 1. Mở chi tiết TVV-TW-700 → tab Đánh giá | **FORM (DN nhập sau VV)**: vu_viec_id (dropdown VV liên kết), star-rating diem_chuyen_mon* (1-5 step 0.5), star-rating diem_thai_do* (1-5 step 0.5), star-rating diem_dung_han* (1-5 step 0.5), nhan_xet (textarea max 5000 ký, sanitize)<br>**STATS card**: "Điểm TB: X.X/5", "Số đánh giá: N"; nếu chưa có đánh giá → "—/5"<br>**LIST**: bảng danh sách đánh giá (DN, Vụ việc, 3 điểm, TB, Nhận xét, Ngày đánh giá) | Happy 🔴 |

## B. Đánh giá CRUD

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-DG-001 | FR-IV-09 / AC1 | DN happy path đánh giá TVV sau VV | dn_001 chuyên trang, VV-001 HOAN_THANH với TVV-TW-700, chưa đánh giá | diem_cm=4.5, diem_td=5.0, diem_th=4.0, nhan_xet="TVV chuyên môn cao, phục vụ nhiệt tình" | 1. Login dn_001<br>2. Mở chi tiết VV-001 (FR-V) hoặc tab Đánh giá TVV<br>3. Nhập 3 điểm + nhận xét<br>4. Submit | **STATE**: DANH_GIA_SAU_VU_VIEC insert (tu_van_vien_id=TVV-TW-700, vu_viec_id=VV-001, doanh_nghiep_id=dn_001, diem_chuyen_mon=4.5, diem_thai_do=5.0, diem_dung_han=4.0, **diem_trung_binh = AVG = (4.5+5.0+4.0)/3 = 4.5**, ngay_danh_gia=NOW); **TU_VAN_VIEN.diem_danh_gia_tb update qua FR-IV-CROSS-01 trigger**; AUDIT_LOG<br>**UI**: Toast "Đánh giá đã được ghi nhận"<br>**PERSIST**: Reload tab Đánh giá TVV-TW-700 → mục mới + Stats cập nhật điểm TB | Happy 🔴 |
| TC-DG-002 | FR-IV-09 / E1 | Điểm ngoài thang 1-5 → ERR-DG-01 | dn_001 (DevTools tamper) | diem_cm=6.0 | 1. DevTools tamper request<br>2. Submit | API 400 "Điểm đánh giá phải từ 1 đến 5" (NGUYÊN VĂN ERR-DG-01); KHÔNG insert | Negative 🟡 |
| TC-DG-003 | FR-IV-09 / E2 ERR-DG-02 | TVV không tồn tại → ERR-DG-02 | dn_001 | tu_van_vien_id: 99999 | 1. Tamper TVV ID<br>2. Submit | "Tư vấn viên không tồn tại" (NGUYÊN VĂN ERR-DG-02) | Negative 🟡 |
| TC-DG-004 | FR-IV-09 / E3 nhận xét >5000 ký → ERR-DG-03 | dn_001 | nhan_xet: 5001 ký | 1. Paste text 5001 ký<br>2. Submit | "Nhận xét tối đa 5000 ký tự" (NGUYÊN VĂN ERR-DG-03) | Negative 🟡 |
| TC-DG-005 | FR-IV-09 / Sanitize XSS nhan_xet | nhan_xet chứa `<script>` → strip | dn_001 | nhan_xet: `<script>alert(1)</script>Tốt` | 1. Submit XSS<br>2. Verify | DB lưu sau sanitize (strip `<script>`, `on*`, `javascript:`); UI render plain "Tốt", KHÔNG execute alert | Edge 🔴 |
| TC-DG-006 | FR-IV-09 / Boundary 1.0 | Điểm boundary low 1.0 | dn_001 | diem_cm=1.0, diem_td=1.0, diem_th=1.0 | 1. Submit | Insert OK; diem_trung_binh=1.0 | Edge 🟡 |
| TC-DG-007 | FR-IV-09 / Boundary 5.0 | Điểm boundary high 5.0 | dn_001 | 3 điểm = 5.0 | 1. Submit | Insert OK; diem_trung_binh=5.0 | Edge 🟡 |

## C. FR-IV-CROSS-01 — Tổng hợp điểm TB (BR-CALC-06)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-CROSS-001 | FR-IV-CROSS-01 / Round-half-up | AVG round-half-up khi 4.55 → 4.6 | TVV-TW-700 có 2 DANH_GIA_SAU_VU_VIEC (4.5 + 4.6) | — | 1. Sau insert đánh giá thứ 2<br>2. Verify TVV.diem_danh_gia_tb | TU_VAN_VIEN.diem_danh_gia_tb = AVG(4.5, 4.6) = 4.55 → round-half-up = **4.6** (1 chữ số thập phân, BR-CALC-06) | Edge 🔴 |
| TC-CROSS-002 | FR-IV-CROSS-01 / AC2 chưa có đánh giá | TVV chưa có đánh giá → "—/5" KHÔNG hiển thị 0 | qtht_01, TVV-TW-701 chưa có DANH_GIA_SAU_VU_VIEC | — | 1. Mở chi tiết TVV-TW-701<br>2. Stats card | UI hiển thị "—/5" hoặc "Chưa có đánh giá" (NGUYÊN VĂN INF-TVV-DG-01); KHÔNG hiển thị "0/5" hoặc "0.0/5" | Negative 🔴 |

---

## D. EDGE bổ sung (A4 inline merge — 2 edge)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-CROSS-101 | EDGE-A4-y / Round-half-up 3 tie cases | Verify round-half-up tie behavior | TVV với 2 đánh giá có TB tie | — | 1. Test 3 case TB: 4.45 / 4.55 / 4.65<br>2. Verify diem_danh_gia_tb | 4.45 → 4.5; 4.55 → 4.6; 4.65 → 4.7 (ROUND_HALF_UP — không phải banker's rounding); BR-CALC-06 | Edge 🔴 |
| TC-CROSS-102 | EDGE-A4-z / 1 đánh giá no-round | TVV mới có đúng 1 đánh giá → diem_tb = exact value | TVV-TW-702 chỉ 1 DANH_GIA_SAU_VU_VIEC diem_trung_binh=4.3 | — | 1. Verify TVV.diem_danh_gia_tb | TU_VAN_VIEN.diem_danh_gia_tb = 4.3 (exact, không round vì chỉ 1 record); UI hiển thị "4.3/5" | Edge 🟡 |

---

**Tổng số TC**: 12 (1 UI + 7 đánh giá + 2 CROSS-01 + 2 Edge A4) — A6 sẽ điều chỉnh
