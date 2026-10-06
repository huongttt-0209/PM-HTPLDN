# Test Cases — Biểu đồ (Chart Types) trên SCR-IX-01

> **SRS Ref**: srs-fr-11:1048 (SCR-IX-01 row#10 biểu đồ), srs-fr-11:1056-1080 (mapping chart type per BC), srs-fr-11:82 (TPL Process step 6 format kết quả)
> **Ngày tạo**: 2026-05-10
> **Đặc thù**: Verify chart types đúng theo mapping 23 BC (Line/Bar/Stacked bar/Donut/Radar). Toggle hiện/ẩn chart. Responsive khi resize.

---

## Quy ước

- **Priority**: 🔴 P0 · 🟡 P1 · 🟢 P2
- **TraceID**: `SCR-IX-01 / chart` hoặc `FR-IX-{NN} / chart`

---

## A. Chart Type Mapping (5 type chính)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BC-CHART-001 | FR-IX-01 / chart Donut + Trend | Donut + Trend cho BC HD | cb_nv_tw_01 login. ≥10 HD mix DA_TRA_LOI/CHO_TRA_LOI 6 tháng. | ky=KHOANG 6 tháng | 1. Chạy BC HD. | (3) 2 biểu đồ: Donut (đã trả lời/chờ) + Line trend 6 điểm. | Happy 🟡 |
| TC-BC-CHART-002 | FR-IX-05 / chart Line | Line chart trend BC VV theo thời gian | cb_nv_tw_01 login. VV phân bố 6 tháng. | ky=KHOANG 6 tháng | 1. Chạy BC FR-IX-05. | (3) 1 Line chart 6 điểm trend. | Happy 🟡 |
| TC-BC-CHART-003 | FR-IX-08 / chart Donut + Bar | Donut + Bar BC CG/TVV | cb_nv_tw_01 login. TVV/CG/NHT đều có. | (snapshot) | 1. Chạy BC FR-IX-08. | (3) Donut (TVV/CG/NHT) + Bar (theo đơn vị). | Happy 🟡 |
| TC-BC-CHART-004 | FR-IX-09 / chart Bar + Radar | Bar + Radar BC Đánh giá hiệu quả | cb_nv_tw_01 login. KH ĐG có ≥4 tiêu chí. | ky=NAM | 1. Chạy BC FR-IX-09. | (3) Bar (theo đơn vị) + **Radar** (theo tiêu chí, 4-5 trục). | Happy 🟡 |
| TC-BC-CHART-005 | FR-IX-11 / chart Stacked bar | Stacked bar cross-tab BC VV theo đơn vị | cb_nv_tw_01 login. VV phân bố 4 trạng thái × 5+ đơn vị. | ky=NAM | 1. Chạy BC FR-IX-11. | (3) Stacked bar: trục X = đơn vị, stack = 4 trạng thái (moi/tiep_nhan/dang_ho_tro/hoan_thanh). | Happy 🔴 |
| TC-BC-CHART-006 | FR-IX-14 / chart Stacked bar trend | Stacked bar trend BC VV theo thời gian chi tiết | cb_nv_tw_01 login. VV 6 tháng × 4 trạng thái. | ky=KHOANG 6 tháng | 1. Chạy BC FR-IX-14. | (3) Stacked bar 6 cột (1 cột/tháng), stack = 4 trạng thái. | Happy 🟡 |
| TC-BC-CHART-007 | FR-IX-12 / chart Grouped bar | Grouped bar BC VV theo lĩnh vực | cb_nv_tw_01 login. VV ≥3 lĩnh vực × 3 đơn vị. | ky=NAM | 1. Chạy BC FR-IX-12. | (3) Grouped bar: trục X = lĩnh vực, group = đơn vị (3 cột/lĩnh vực). | Happy 🟡 |

---

## B. Toggle hiện/ẩn

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BC-CHART-020 | SCR-IX-01 row#10 | Toggle "Ẩn biểu đồ" → bảng full width | cb_nv_tw_01 login. Đã chạy BC có biểu đồ. | — | 1. Click toggle "Ẩn biểu đồ". | (3) Vùng biểu đồ collapse, bảng full width. Toggle label đổi thành "Hiện biểu đồ". | Happy 🟡 |
| TC-BC-CHART-021 | SCR-IX-01 row#10 | Toggle "Hiện biểu đồ" → restore | cb_nv_tw_01 login. Đã ẩn. | — | 1. Click "Hiện biểu đồ". | (3) Biểu đồ render lại, bảng resize. | Happy 🟢 |
| TC-BC-CHART-022 | SCR-IX-01 row#10 | Toggle persist khi đổi loại BC | cb_nv_tw_01 login. Đã ẩn biểu đồ. | — | 1. Đổi sang BC khác. 2. [Xem]. | (3) **Behavior pending** — verify thực tế: (a) toggle persist (vẫn ẩn), hoặc (b) reset (hiện lại). Log nếu surprising. | Edge 🟢 |

---

## C. Edge — Empty data + Responsive

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BC-CHART-040 | SCR-IX-01 row#13 | Empty data → biểu đồ ẩn (không render placeholder rỗng) | cb_nv_tw_01 login. Tháng không có data. | ky=THANG empty | 1. [Xem]. | (3) Empty state INF-RPT-01 hiện. Vùng biểu đồ KHÔNG render (không placeholder rỗng/loading vô tận). | Edge 🟡 |
| TC-BC-CHART-041 | SCR-IX-01 row#11 | Responsive 1024px — chart resize không vỡ | cb_nv_tw_01 login. Đã chạy BC. | viewport=1024px | 1. Resize browser xuống 1024. | (3) Biểu đồ resize giữ tỷ lệ (không cắt). Bảng cuộn ngang. | Edge 🟢 |
| TC-BC-CHART-042 | SCR-IX-01 row#11 | Responsive mobile 375px | cb_nv_tw_01 login. | viewport=375px | 1. Resize 375px. | (3) **SPEC-CLARIFY-BC-09**: Chưa rõ SCR-IX-01 có spec mobile responsive không. Verify thực tế. | Edge 🟢 |

---

## Tổng kết file 05-TC

- **12 TC**: 7 chart type A + 3 toggle B + 3 edge C - bỏ 1 redundant = **12 TC**.
- **Critical TC (🔴)**: CHART-005 (Stacked bar — đặc trưng cross-tab).
- **SPEC-CLARIFY ref**: BC-09 mới (CHART-042 mobile responsive).

*Generated 2026-05-10 — Phase A step A3 (BMAD generate-e2e-tests)*
