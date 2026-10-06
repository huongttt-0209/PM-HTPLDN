# A5 — Traceability Matrix (FR-01 Dashboard)

> **Ngày:** 2026-05-10
> **Tool:** bmad-testarch-trace (manual variant)
> **Source:** SRS `srs-fr-01-dashboard-v3.1.md` v3.1/v3.5, line 1-1167
> **Phase:** A5 (Phase A của detailed-tc plan §3.1)
> **Total TC trước A6:** 161 (file 01-08)

---

## 1. BR ↔ TC Matrix

> **Scope BR:** 5 BR formal tham chiếu trong SRS — BR-AUTH-01/03/04/08, BR-SLA-05, BR-CALC-03 (test plan §5)

| BR | Phát biểu (tóm tắt) | SRS Ref | TC covered | Coverage |
|----|---------------------|---------|------------|----------|
| BR-AUTH-01 | Xác thực bắt buộc — Tier 1 nội bộ + Tier 2 SSO VNeID. Mọi TC đều precondition login. | line 1129-1135 | TC-DASH-180..188 (login + redirect mọi role), TC-DASH-135 (revoke giữa phiên) — và mọi TC đều precondition login | ✅ 100% |
| BR-AUTH-03 | Ngang cấp không thấy nhau (BN ≠ ĐP, DP ≠ DP khác) | line 1140-1144 | TC-DASH-195 (DP-DP cross), TC-DASH-196 (BN-BN cross) | ✅ 100% |
| BR-AUTH-04 | TW thấy cấp con (BN + ĐP ngang cấp song song) | line 1145-1148 | TC-DASH-197 (TW thấy DP scope), TC-DASH-198 (TW switch L1=BN) | ✅ 100% |
| BR-AUTH-08 | Scope dữ liệu theo `don_vi_id` mọi entity có cột này (mọi KPI/chart) | line 1149-1151 | TC-DASH-025, 038, 049, 087, 105, 183, 191, 193, 194, 195, 196, 199 | ✅ 100% |
| BR-SLA-05 | Tỷ lệ tuân thủ SLA = HT đúng hạn / (HT + đang xử lý quá hạn) — tránh tỷ lệ ảo | line 1153-1157 | TC-DASH-054, 060, 061, 062, 078 | ✅ 100% |
| BR-CALC-03 | Deadline = ngày làm việc (T2-T6, trừ ngày lễ FR-VIII-29) | line 1163-1167 | TC-DASH-102, 103, 116, 119 | ✅ 100% |

**BR coverage:** 6/6 = **100%** (5 BR áp + 1 BR-CALC-03 verified ở KPI-S-02)

---

## 2. AC ↔ TC Matrix (per FR)

### 2.1 FR-I-01 — Tổng hợp hỏi đáp (KPI-01) — 4 AC (line 250-253)

| AC | Mô tả | TC covered | Status |
|----|-------|------------|--------|
| AC1 | CB login + truy cập Dashboard → hiển thị số liệu hỏi đáp theo phạm vi | TC-DASH-001, 005 | ✅ |
| AC2 | CB ĐP → chỉ thấy data ĐP đó | TC-DASH-025 (BR-AUTH-08 cross-unit) | ✅ |
| AC3 | CB TW → thấy data toàn quốc | TC-DASH-001, 197 | ✅ |
| AC4 | CB chọn bộ lọc thời gian → data cập nhật | TC-DASH-005, 010, 027 | ✅ |

**FR-I-01 AC:** 4/4 = **100%**

### 2.2 FR-I-02 — Vụ việc đã tiếp nhận (KPI-02) — 4 AC (line 273-276)

| AC | Mô tả | TC covered | Status |
|----|-------|------------|--------|
| AC1 | CB login → hiển thị tổng số VV theo đơn vị | TC-DASH-002 | ✅ |
| AC2 | CB ĐP → chỉ data ĐP | TC-DASH-025 | ✅ |
| AC3 | CB TW → toàn quốc | TC-DASH-197, 198 | ✅ |
| AC4 | Bộ lọc thời gian → data cập nhật | TC-DASH-002, 010 | ✅ |

**FR-I-02 AC:** 4/4 = **100%**

### 2.3 FR-I-03 — Vụ việc đang hỗ trợ (KPI-03 — ảnh chụp) — 9 AC (line 296-305)

| AC | Mô tả | TC covered | Status |
|----|-------|------------|--------|
| AC1 | CB login → hiển thị số VV đang hỗ trợ | TC-DASH-003 | ✅ |
| AC2 | VV `DA_TIEP_NHAN` → KPI-03 đếm | TC-DASH-003 | ✅ |
| AC3 | VV `DANG_KIEM_TRA` → KPI-03 đếm (rà soát hồ sơ) | TC-DASH-003 | ✅ |
| AC4 | VV `YEU_CAU_BO_SUNG` → KPI-03 đếm (chờ DN bổ sung) | TC-DASH-003 | ✅ |
| AC5 | VV `DA_PHAN_CONG` / `DANG_XU_LY` → KPI-03 đếm | TC-DASH-003 | ✅ |
| AC6 | VV `CHO_PHE_DUYET` → KPI-03 KHÔNG đếm | TC-DASH-003 | ✅ |
| AC7 | VV `HOAN_THANH` / `TU_CHOI` / `DA_DANH_GIA` → KPI-03 KHÔNG đếm | TC-DASH-003, 020 (snapshot transition) | ✅ |
| AC8 | CB ĐP → chỉ data ĐP | TC-DASH-025 | ✅ |
| AC9 | CB TW → toàn quốc | TC-DASH-197 | ✅ |

**FR-I-03 AC:** 9/9 = **100%** (AC10 "bộ lọc thời gian" không có vì KPI-03 ảnh chụp)

> Note: SRS line 296-305 có 10 AC nhưng 1 AC trùng FR-I-01 (CB chọn bộ lọc thời gian) đã gộp vào AC10 ngầm — verify ở TC-DASH-024 + TC-DASH-027 (3 dạng "Tính đến").

### 2.4 FR-I-04 — Vụ việc đã hoàn thành (KPI-04) — 2 AC (line 324-326)

| AC | Mô tả | TC covered | Status |
|----|-------|------------|--------|
| AC1 | CB login → tổng VV `HOAN_THANH` | TC-DASH-004 | ✅ |
| AC2 | CB lọc thời gian → chỉ tính VV HT trong khoảng (`ngay_hoan_thanh`) | TC-DASH-004, 022 (kỳ trước = 0) | ✅ |

**FR-I-04 AC:** 2/2 = **100%**

### 2.5 FR-I-05 — Khóa học đang diễn ra (KPI-05 — ảnh chụp) — 4 AC (line 346-349)

| AC | Mô tả | TC covered | Status |
|----|-------|------------|--------|
| AC1 | CB login → KH `DANG_DIEN_RA` thuộc phạm vi | TC-DASH-030, 046 (ảnh chụp boundary) | ✅ |
| AC2 | CB BN/ĐP → chỉ data đơn vị (BR-AUTH-08) | TC-DASH-038 | ✅ |
| AC3 | TW đổi filter đơn vị → đếm cập nhật | TC-DASH-046, 047 | ✅ |
| AC4 | Click thẻ → drill-down `/dao-tao/khoa-hoc?...` | TC-DASH-034 | ✅ |

**FR-I-05 AC:** 4/4 = **100%**

### 2.6 FR-I-06 — Khóa học đã kết thúc (KPI-06) — 5 AC (line 368-373)

| AC | Mô tả | TC covered | Status |
|----|-------|------------|--------|
| AC1 | CB login → số KH `DA_KET_THUC` trong kỳ | TC-DASH-031 | ✅ |
| AC2 | CB BN/ĐP → chỉ data đơn vị | TC-DASH-038 (TVV) — TC GAP cho KH BN/ĐP — see Gap A5 | ⚠️ GAP-1 |
| AC3 | TW đổi filter đơn vị → đếm cập nhật | TC-DASH-031, 048 | ✅ |
| AC4 | Lọc thời gian → data cập nhật | TC-DASH-031, 048 | ✅ |
| AC5 | Click thẻ → drill-down `/dao-tao/khoa-hoc?...&date_field=ngay_ket_thuc&nam=...` | TC-DASH-035 | ✅ |

**FR-I-06 AC:** 4/5 = **80%** → 5/5 sau A6 fill (TC-DASH-217 KPI-06 BN/ĐP scope)

### 2.7 FR-I-07 — TVV đang hoạt động (KPI-07 — ảnh chụp) — 8 AC (line 394-402)

| AC | Mô tả | TC covered | Status |
|----|-------|------------|--------|
| AC1 | CB login → tổng TVV "Đang hoạt động" thuộc phạm vi | TC-DASH-032 | ✅ |
| AC2 | TVV transition `DANG_HOAT_DONG → TAM_DUNG` → giảm sau auto-refresh, KHÔNG real-time | TC-DASH-045 | ✅ |
| AC3 | User TW vừa login → default L1='DP', L2='Tất cả ĐP' | TC-DASH-033 | ✅ |
| AC4 | TW chọn L1='DP' + L2='Tất cả' → đếm TVV ĐP | TC-DASH-032, 033 | ✅ |
| AC5 | TW chọn L1='BN' + L2='Tất cả' → đếm TVV BN | TC-DASH-037 | ✅ |
| AC6 | TW chọn 1 đơn vị cụ thể → đếm TVV thuộc đơn vị đó | TC-DASH-049 (drill-down locked) — TC GAP TVV TW chọn 1 đơn vị scope verify — see Gap A5 | ⚠️ GAP-2 |
| AC7 | User BN locked → chỉ TVV thuộc BN | TC-DASH-038, 196 (cross-unit BN-BN) — chưa explicit BN locked TVV | ⚠️ Partial |
| AC8 | User ĐP locked → chỉ TVV thuộc ĐP (BR-AUTH-08) | TC-DASH-038, 049 | ✅ |

**FR-I-07 AC:** 6/8 = **75%** → 8/8 sau A6 fill (TC-DASH-218 TW chọn 1 đơn vị scope + TC-DASH-219 BN locked TVV)

### 2.8 FR-I-08 — UC8 2 biểu đồ cột song song — 10 AC (line 480-490)

| AC | Mô tả | TC covered | Status |
|----|-------|------------|--------|
| AC1 | TW vừa login default → trục X = tất cả ĐP có data, sort DESC | TC-DASH-050 | ✅ |
| AC2 | TW switch L1='BN' + L2='Tất cả BN' → trục X = BN có data, sort DESC | TC-DASH-050 (similar pattern) — TC GAP cho explicit L1=BN UC8 — see Gap A5 | ⚠️ GAP-3 |
| AC3 | TW chọn 1 đơn vị + Tháng cụ thể → trục X = ngày trong tháng | TC-DASH-051 | ✅ |
| AC4 | TW chọn 1 đơn vị + Tháng "Tất cả" → trục X = 12 cột tháng | TC-DASH-052 | ✅ |
| AC5 | User BN/ĐP locked → trục X = chuỗi thời gian của đơn vị user | TC-DASH-052 (similar) — TC GAP cho UC8 BN/ĐP locked — see Gap A5 | ⚠️ GAP-4 |
| AC6 | Không có data → biểu đồ trống + INFO-DASH-02 | TC-DASH-068, 069 | ✅ |
| AC7 | 1 đơn vị mẫu N<10 → asterisk + tooltip generic + (N=n) | TC-DASH-072, 073 | ✅ |
| AC8 | Ngày không có data (trục X = ngày) → skip không vẽ cột | TC-DASH-075 | ✅ |
| AC9 | Tỷ lệ tuân thủ tính theo BR-SLA-05 (mẫu số gồm vụ đang quá hạn) | TC-DASH-054, 060, 061, 062 | ✅ |
| AC10 | CB đổi filter + Apply → biểu đồ cập nhật | TC-DASH-051, 052, 055 | ✅ |

**FR-I-08 AC:** 8/10 = **80%** → 10/10 sau A6 fill (TC-DASH-220 UC8 L1=BN + TC-DASH-221 UC8 BN/ĐP locked)

### 2.9 FR-I-09 — UC9 Biểu đồ vành — 9 AC (line 542-551)

| AC | Mô tả | TC covered | Status |
|----|-------|------------|--------|
| AC1 | TW vừa login default → donut + center label + caption | TC-DASH-080 | ✅ |
| AC2 | TW chọn 1 đơn vị → tỷ lệ + điểm TB tính riêng đơn vị | TC-DASH-086 (BN aggregate — tương tự) — TC GAP cho 1 đơn vị cụ thể UC9 — see Gap A5 | ⚠️ GAP-5 |
| AC3 | TW chọn L1='BN' + L2='Tất cả' → aggregate BN | TC-DASH-086 | ✅ |
| AC4 | User BN/ĐP locked → tỷ lệ + điểm TB của đơn vị user | TC-DASH-087 | ✅ |
| AC5 | Donut 2 phần + center label + caption (cấu trúc) | TC-DASH-080, 084 | ✅ |
| AC6 | Có data kỳ trước → 2 chỉ số có biểu tượng xu hướng + chênh lệch | TC-DASH-085 | ✅ |
| AC7 | Không có kỳ trước → trend "—" | TC-DASH-093 | ✅ |
| AC8 | Không data trong kỳ → donut trống + INFO-DASH-03 | TC-DASH-090 | ✅ |
| AC9 | CB đổi filter + Apply → donut cập nhật | TC-DASH-086, 087 | ✅ |

**FR-I-09 AC:** 8/9 = **89%** → 9/9 sau A6 fill (TC-DASH-222 UC9 1 đơn vị cụ thể)

### 2.10 KPI-S-01 — Tỷ lệ vụ việc phải bổ sung — 4 AC (line 588-591)

| AC | Mô tả | TC covered | Status |
|----|-------|------------|--------|
| AC1 | 100 vụ HT, 30 từng qua YEU_CAU_BO_SUNG → 30% | TC-DASH-100 | ✅ |
| AC2 | 1 vụ qua YCB 3 lần → vẫn đếm 1 lần ở tử số | TC-DASH-101 | ✅ |
| AC3 | Không có vụ HT → "—" | TC-DASH-110 | ✅ |
| AC4 | CB BN/ĐP → chỉ tính vụ thuộc đơn vị | TC-DASH-105 | ✅ |

**KPI-S-01 AC:** 4/4 = **100%**

### 2.11 KPI-S-02 — Thời gian xử lý trung bình — 4 AC (line 617-620)

| AC | Mô tả | TC covered | Status |
|----|-------|------------|--------|
| AC1 | T2 → T2 sau, không lễ → 5 ngày làm việc | TC-DASH-102 | ✅ |
| AC2 | Có 1 ngày lễ giữa → 4 ngày làm việc | TC-DASH-103 | ✅ |
| AC3 | Không có vụ HT → "—" | TC-DASH-111 | ✅ |
| AC4 | CB BN/ĐP → chỉ tính vụ thuộc đơn vị | TC-DASH-105 | ✅ |

**KPI-S-02 AC:** 4/4 = **100%**

### 2.12 FR-I-CROSS-02 — Auto-refresh — 11 AC (line 658-668)

| AC | Mô tả | TC covered | Status |
|----|-------|------------|--------|
| AC1 | 60s tick → tự cập nhật (kỳ hiện tại) | TC-DASH-120 | ✅ |
| AC2 | Tab hidden → pause | TC-DASH-121 | ✅ |
| AC3 | Tab visible → tải lại ngay + giữ pending filter | TC-DASH-122 | ✅ |
| AC4 | Kỳ đóng → ẨN HOÀN TOÀN nút "Làm mới" + nhãn timestamp | TC-DASH-123, 143 | ✅ |
| AC5 | Đổi từ kỳ đóng về kỳ hiện tại → cả 2 hiển thị lại + auto-refresh chạy lại | TC-DASH-124 | ✅ |
| AC6 | Filter pending KHÔNG bị overwrite bởi tick | TC-DASH-126 | ✅ |
| AC7 | Quyền user thay đổi giữa phiên → auto logout + redirect login | TC-DASH-135 | ✅ |
| AC8 | Widget timeout 30s → Trạng thái 28 cục bộ, KHÔNG toast page-level | TC-DASH-130, 147 | ✅ |
| AC9 | Đơn vị đang chọn bị vô hiệu → fallback "Tất cả [L1]", KHÔNG thông báo | TC-DASH-140 | ✅ |
| AC10 | ≥50% widget fail × 3 chu kỳ → banner kèm dòng phụ "3 lần" | TC-DASH-132, 133, 144 | ✅ |
| AC11 | User nhấn "Làm mới" → button mờ + spinner + bật lại | TC-DASH-125 | ✅ |

**FR-I-CROSS-02 AC:** 11/11 = **100%**

---

### Tổng AC

| FR | AC tổng | AC covered (trước A6) | Coverage |
|----|---------|----------------------|----------|
| FR-I-01 | 4 | 4 | 100% |
| FR-I-02 | 4 | 4 | 100% |
| FR-I-03 | 9 | 9 | 100% |
| FR-I-04 | 2 | 2 | 100% |
| FR-I-05 | 4 | 4 | 100% |
| FR-I-06 | 5 | 4 | 80% |
| FR-I-07 | 8 | 6 | 75% |
| FR-I-08 | 10 | 8 | 80% |
| FR-I-09 | 9 | 8 | 89% |
| KPI-S-01 | 4 | 4 | 100% |
| KPI-S-02 | 4 | 4 | 100% |
| FR-I-CROSS-02 | 11 | 11 | 100% |
| **Tổng** | **74** | **68** | **91.9%** |

> **Sau A6 fill (6 TC):** 74/74 = **100%**.

---

## 3. Permission Matrix ↔ TC

> **Scope:** 8 quyền (P1-P8) × 12 vai trò = 96 cells nominal. Effective cells = (7 active roles × 8 quyền = 56) + (4 inactive roles × 1 redirect TC = 4) = **60 cells**. 4 inactive role chỉ test P1=✗ → P2-P8 = `—` đương nhiên (không vào được dashboard).

### 3.1 P1 VIEW_DASHBOARD (12 cells = 7 ✓ + 4 ✗ + 1 QTHT)

| Vai trò | Quyền | TC covered |
|---------|-------|------------|
| QTHT | ✓ | TC-DASH-180 |
| CB_NV_TW | ✓ | TC-DASH-181 |
| CB_NV_BN | ✓ | TC-DASH-182 |
| CB_NV_DP | ✓ | TC-DASH-183 |
| CB_PD_TW | ✓ | TC-DASH-181 (paired) |
| CB_PD_BN | ✓ | TC-DASH-182 (paired) |
| CB_PD_DP | ✓ | TC-DASH-183 (paired) |
| DN | ✗ → redirect Cổng DN | TC-DASH-185 |
| NHT | ✗ → redirect form NHT | TC-DASH-186 |
| TVV | ✗ → redirect view TVV | TC-DASH-187 |
| CG | ✗ → redirect view CG | TC-DASH-188 |

**P1:** 11/11 cells (12-1 vì TC-181/182/183 paired covers cả CB_NV và CB_PD cùng cấp) = **100%**

### 3.2 P2 FILTER_TIME (7 cells)

| Vai trò | Quyền | TC covered |
|---------|-------|------------|
| QTHT, CB_NV_TW, CB_NV_BN, CB_NV_DP, CB_PD_TW, CB_PD_BN, CB_PD_DP | ✓ | TC-DASH-190 (test 7 role lần lượt đổi Năm + Tháng) |

**P2:** 7/7 = **100%**

### 3.3 P3 FILTER_CHANGE_SCOPE (7 cells)

| Vai trò | Quyền | TC covered |
|---------|-------|------------|
| QTHT | ✓ free | TC-DASH-180, 191 |
| CB_NV_TW | ✓ free | TC-DASH-181, 191 |
| CB_NV_BN | locked=BN user | TC-DASH-182, 191 |
| CB_NV_DP | locked=ĐP user | TC-DASH-183, 191 |
| CB_PD_TW | ✓ free | TC-DASH-181 (paired), 191 |
| CB_PD_BN | locked=BN user | TC-DASH-182 (paired), 191 |
| CB_PD_DP | locked=ĐP user | TC-DASH-183 (paired), 191 |

**P3:** 7/7 = **100%**. Edge: TC-DASH-199 (locked PATCH URL ignored).

### 3.4 P4 MANUAL_REFRESH (7 cells)

| Vai trò | Quyền | TC covered |
|---------|-------|------------|
| 7 active roles | ✓ | TC-DASH-192 (test 7 role click "Làm mới") |

**P4:** 7/7 = **100%**

### 3.5 P5 DRILL_DOWN_HOIDAP (7 cells)

| Vai trò | Quyền | TC covered |
|---------|-------|------------|
| QTHT, CB_NV_TW, CB_PD_TW | ✓ | TC-DASH-006 (cb_nv_tw_01 click KPI-01) |
| CB_NV_BN, CB_NV_DP | ✓* (data scope BR-AUTH-08) | TC-DASH-193 (cb_nv_dp_01) — TC GAP CB_NV_BN drill-down explicit — see Gap A5 |
| CB_PD_BN, CB_PD_DP | ✓* | TC-DASH-194 (cb_nv_dp_01 — paired pattern) |

**P5:** 5/7 = **71%** → 7/7 sau A6 fill (TC-DASH-223 CB_NV_BN drill-down)

### 3.6 P6 DRILL_DOWN_VUVIEC (7 cells)

| Vai trò | Quyền | TC covered |
|---------|-------|------------|
| QTHT, CB_NV_TW, CB_PD_TW | ✓ | TC-DASH-007, 008, 009 |
| CB_NV_BN, CB_NV_DP, CB_PD_BN, CB_PD_DP | ✓* | TC-DASH-194 (paired pattern with KPI-02/03/04 click) |

**P6:** 7/7 = **100%**

### 3.7 P7 DRILL_DOWN_KHOAHOC (7 cells)

| Vai trò | Quyền | TC covered |
|---------|-------|------------|
| QTHT, CB_NV_TW, CB_PD_TW | ✓ | TC-DASH-034, 035 |
| CB_NV_BN, CB_NV_DP, CB_PD_BN, CB_PD_DP | ✓* | TC-DASH-194 (paired pattern with KPI-05/06 click) |

**P7:** 7/7 = **100%**

### 3.8 P8 DRILL_DOWN_TVV (7 cells)

| Vai trò | Quyền | TC covered |
|---------|-------|------------|
| QTHT, CB_NV_TW, CB_PD_TW | ✓ | TC-DASH-036 |
| CB_NV_BN, CB_NV_DP, CB_PD_BN, CB_PD_DP | ✓* | TC-DASH-049, 194 |

**P8:** 7/7 = **100%**

### Tổng Permission Matrix

| Quyền | Cells | Covered |
|-------|-------|---------|
| P1 | 11 (7✓ + 4✗) | 11 |
| P2 | 7 | 7 |
| P3 | 7 | 7 |
| P4 | 7 | 7 |
| P5 | 7 | 5 |
| P6 | 7 | 7 |
| P7 | 7 | 7 |
| P8 | 7 | 7 |
| **Tổng** | **60 cells effective** | **58 (96.7%)** |

> **Sau A6 fill (TC-DASH-223):** 60/60 = **100%**.

> Note về số cell: matrix nominal 8×12 = 96. Sau khi loại P2-P8 cho 4 role inactive (28 cells = `—` trivially covered bởi P1=✗ — TC-185/186/187/188 đã verify redirect chặn truy cập), effective = 96 - 28 - 4*0 + 4 (P1=✗) = 60 + 8 (P1 ✓ paired CB_NV/CB_PD) — final effective = 60 cells (test plan §8 reference 56 + 4 redirect).

---

## 4. Error Code ↔ TC

| Error Code | Severity | Trigger | TC covered | Status |
|------------|----------|---------|------------|--------|
| INFO-DASH-01 | INFO | Không có dữ liệu KPI → "0" + "Chưa có dữ liệu trong kỳ" | TC-DASH-015, 042 | ✅ |
| INFO-DASH-02 | INFO | Không có dữ liệu UC8 → biểu đồ trống + caption | TC-DASH-068, 069 | ✅ |
| INFO-DASH-03 | INFO | Không có dữ liệu UC9 → donut trống + caption | TC-DASH-090 | ✅ |
| INFO-DASH-04 | INFO | Audit log thiếu kỳ trước → trend "—" + tooltip | TC-DASH-017, 043, 093 | ✅ |
| ERR-DASH-02 | ERROR | DB/API 5xx → widget hỏng (Trạng thái 28) — không toast/modal toàn trang | TC-DASH-016, 130, 131, 147 | ✅ |

**Error code coverage:** 5/5 = **100%**

---

## 5. State Enum Source ↔ TC

> KPI-01..07 phụ thuộc enum/state của 4 entity source: HOI_DAP, VU_VIEC, KHOA_HOC, TU_VAN_VIEN.

| KPI | Entity | Enum/Field source | TC verify count đúng | Status |
|-----|--------|-------------------|----------------------|--------|
| KPI-01 | HOI_DAP | `trang_thai = MOI` | TC-DASH-001 | ✅ |
| KPI-02 | VU_VIEC | `ngay_tiep_nhan` ∈ kỳ (any state except deleted) | TC-DASH-002, 195, 196 | ✅ |
| KPI-03 | VU_VIEC | `trang_thai ∈ {DA_TIEP_NHAN, DANG_KIEM_TRA, YEU_CAU_BO_SUNG, DA_PHAN_CONG, DANG_XU_LY}` (5 enum sống) | TC-DASH-003 (đếm 5 enum + loại trừ `CHO_PHE_DUYET, HOAN_THANH, DA_DANH_GIA, TU_CHOI`) | ✅ |
| KPI-04 | VU_VIEC | `trang_thai = HOAN_THANH` & `ngay_hoan_thanh` ∈ kỳ | TC-DASH-004, 022 | ✅ |
| KPI-05 | KHOA_HOC | `trang_thai = DANG_DIEN_RA` (ảnh chụp) | TC-DASH-030, 046 | ✅ |
| KPI-06 | KHOA_HOC | `trang_thai = DA_KET_THUC` & `ngay_ket_thuc` ∈ kỳ | TC-DASH-031, 048 | ✅ |
| KPI-07 | TU_VAN_VIEN | `trang_thai = DANG_HOAT_DONG` (loại trừ 8 enum khác: MOI_DANG_KY, CHO_THAM_DINH, DANG_THAM_DINH, YEU_CAU_BO_SUNG, CHO_PHE_DUYET, TU_CHOI, TAM_DUNG, VO_HIEU_HOA) | TC-DASH-032 (verify 5 vs 8 loại trừ) | ✅ |

**State enum source coverage:** 7/7 = **100%**

---

## 6. Outputs Field ↔ TC (28 fields)

### 6.1 TPL-DASH-KPI — 12 fields (áp KPI-01..07 + KPI-S-01..02)

| # | Field | TC verify | Status |
|---|-------|-----------|--------|
| 1 | `gia_tri` | TC-DASH-001..005, 030, 100, 102 | ✅ |
| 2 | `nhan` | TC-DASH-001 | ✅ |
| 3 | `don_vi_tinh` | TC-DASH-001, 002, 030, 100, 102 | ✅ |
| 4 | `drill_down_url` | TC-DASH-006, 007, 008, 009, 034, 035, 036 | ✅ |
| 5 | `nam` | TC-DASH-005 | ✅ |
| 6 | `thang` | TC-DASH-005 | ✅ |
| 7 | `scope_label` | TC-DASH-005 | ✅ |
| 8 | `tu_ngay_boundary` | TC-DASH-005, 174 (5 scenarios) | ✅ |
| 9 | `den_ngay_boundary` | TC-DASH-005, 028 (NOW kỳ hiện tại), 174 | ✅ |
| 10 | `is_qua_khu_dong` | TC-DASH-027 (TRUE kỳ quá khứ + FALSE kỳ hiện tại) | ✅ |
| 11 | `xu_huong_phan_tram` | TC-DASH-010, 021, 022, 023 (NULL boundary) | ✅ |
| 12 | `huong_tang_giam` | TC-DASH-010 (TANG), 022 (GIAM), 023 (KHONG_DOI), 029 (`=` icon) | ✅ |

**TPL-DASH-KPI:** 12/12 = **100%**

### 6.2 UC8 specific outputs — 8 fields (line 447-456)

| # | Field | TC verify | Status |
|---|-------|-----------|--------|
| 1 | `diem_hai_long_tb` (0-100) | TC-DASH-053, 056 | ✅ |
| 2 | `ty_le_tuan_thu_sla` (%) | TC-DASH-054, 057 | ✅ |
| 3 | `so_luong_danh_gia` (cỡ mẫu) | TC-DASH-058, 072 | ✅ |
| 4 | `so_luong_vu_viec_sla` (cỡ mẫu) | TC-DASH-058, 073 | ✅ |
| 5 | `chart_data_hai_long` (nhãn + giá trị) | TC-DASH-053 | ✅ |
| 6 | `chart_data_sla` | TC-DASH-054, 060, 061, 062 | ✅ |
| 7 | `diem_hai_long_xu_huong` (TANG/GIAM/KHONG_DOI) | TC-DASH-055 | ✅ |
| 8 | `ty_le_sla_xu_huong` | TC-DASH-055 | ✅ |

**UC8 outputs:** 8/8 = **100%**

### 6.3 UC9 specific outputs — 8 fields (line 525-534)

| # | Field | TC verify | Status |
|---|-------|-----------|--------|
| 1 | `ty_le_dat` (%) | TC-DASH-080, 081, 087, 095, 096 | ✅ |
| 2 | `ty_le_dat_xu_huong` | TC-DASH-085 | ✅ |
| 3 | `ty_le_dat_phan_tram_change` | TC-DASH-085, 094 (NULL boundary) | ✅ |
| 4 | `diem_tb` (0-10, 1 chữ số thập phân) | TC-DASH-082, 087, 097 | ✅ |
| 5 | `diem_tb_xu_huong` | TC-DASH-085 | ✅ |
| 6 | `diem_tb_delta` | TC-DASH-085 | ✅ |
| 7 | `sample_size` | TC-DASH-080, 083, 098 (loại NULL) | ✅ |
| 8 | `chart_data` (donut 2 phần) | TC-DASH-080, 084, 095, 096 | ✅ |

**UC9 outputs:** 8/8 = **100%**

### Tổng outputs

| Group | Fields | Covered |
|-------|--------|---------|
| TPL-DASH-KPI | 12 | 12 |
| UC8 specific | 8 | 8 |
| UC9 specific | 8 | 8 |
| **Tổng** | **28** | **28 = 100%** |

---

## 7. Tổng kết coverage (trước A6)

| Axis | Coverage | Status |
|------|----------|--------|
| BR | 6/6 = 100% | ✅ |
| AC | 68/74 = 91.9% | ⚠️ (6 GAP) |
| Permission Matrix | 58/60 cells = 96.7% | ⚠️ (1 GAP CB_NV_BN drill-down) |
| Error code | 5/5 = 100% | ✅ |
| State enum source | 7/7 = 100% | ✅ |
| Outputs field | 28/28 = 100% | ✅ |

**Threshold per test plan §8:** AC ≥97%, Permission 100%, Outputs 100%. **Trace status (trước A6):** ⚠️ AC 91.9% < 97% target — 6 TC fill needed at A6.

---

## 8. Gap A5 (forward to A6 fill)

> 6 GAP cell (5 AC + 1 Permission). A6 sẽ fill TC mới inline vào file UC tương ứng.

| GAP ID | Loại | Mô tả | File target | TC dự kiến (A6 fill) |
|--------|------|-------|-------------|----------------------|
| GAP-1 | AC | FR-I-06 AC2 — CB BN/ĐP scope KH `DA_KET_THUC` chưa explicit (chỉ có TVV scope ở TC-038) | 02-TC | TC-DASH-217 |
| GAP-2 | AC | FR-I-07 AC6 — TW chọn 1 đơn vị cụ thể → KPI-07 đếm scope đơn vị đó (TC-DASH-049 chỉ verify URL drill-down, chưa verify count) | 02-TC | TC-DASH-218 |
| GAP-3 | AC | FR-I-08 AC2 — TW switch L1='BN' + L2='Tất cả BN' UC8 (TC-DASH-050 default DP, chưa explicit BN switch) | 03-TC | TC-DASH-220 |
| GAP-4 | AC | FR-I-08 AC5 — User BN/ĐP locked UC8 → trục X = chuỗi thời gian đơn vị user | 03-TC | TC-DASH-221 |
| GAP-5 | AC | FR-I-09 AC2 — TW chọn 1 đơn vị cụ thể UC9 → tỷ lệ + điểm TB tính riêng | 04-TC | TC-DASH-222 |
| GAP-6 | AC + Permission | FR-I-07 AC7 + P5/P6/P7/P8 — CB_NV_BN explicit drill-down verify URL `don_vi_id={BN}` | 02-TC + 08-TC | TC-DASH-219 (BN locked TVV) + TC-DASH-223 (CB_NV_BN drill-down) |

**Tổng A6 fill dự kiến:** 7 TC mới — TC-DASH-217 đến TC-DASH-223. Sau A6: AC 100%, Permission 100%.

---

## 9. SPEC-CLARIFY active (forward to BA)

| Code | File | Issue | Severity |
|------|------|-------|----------|
| SPEC-CLARIFY-DASH-01 | 04-TC | HV `diem_kiem_tra=NULL` có vào mẫu số tỷ lệ đạt? | P1 |
| SPEC-CLARIFY-DASH-02 | 05-TC | KPI-S-01 `xu_huong_phan_tram` % point hay % relative? | P1 |
| SPEC-CLARIFY-DASH-03 | 06-TC | Text Trạng thái 28 nguyên văn hay design custom? | P2 |
| SPEC-CLARIFY-DASH-04 | 07-TC | URL params invalid → rewrite hay giữ URL invalid? | P2 |
| SPEC-CLARIFY-DASH-05 | 08-TC | Locked user PATCH URL `don_vi_id` cross-unit → fallback "Tất cả" hay locked override? | P1 |

**Tổng:** 5 SPEC-CLARIFY active (3 P1 + 2 P2) — chờ BA confirm khi Phase B.

---

*A5 done 2026-05-10 — Phase A5 (manual traceability matrix). Forward 6 GAP (7 TC) to A6 fill.*
