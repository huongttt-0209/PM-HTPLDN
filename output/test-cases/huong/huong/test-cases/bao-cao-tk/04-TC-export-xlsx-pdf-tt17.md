# Test Cases — Export XLSX + PDF (TT17/2025) + Cap Rows

> **SRS Ref**: srs-fr-11:71 (Input format_xuat), srs-fr-11:83-85 (TPL Process step 7-9), srs-fr-11:112 (WRN-RPT-01 cap), srs-fr-11:1043-1051 (SCR-IX-01 row#8-9), srs-fr-11:1270-1274 (BR-DATA-06 formal)
> **Ngày tạo**: 2026-05-10
> **Đặc thù**: Test xuất file đặc thù — format TT17/2025 (A4, Times New Roman 13), cap rows, header chứa metadata BC. **SPEC-CLARIFY-BC-01 RE-OPEN (Codex 2026-05-10 F-01)**: BR-DATA-06 formal §6 line 1274 quy định cap **10,000 rows/file** (authoritative). TPL inline line 85 + 112 nói "50.000 dòng" — mâu thuẫn cần BA xác nhận update TPL về 10K hoặc nâng BR-DATA-06 cho FR-IX. **Default TC: 10K theo BR formal** (rule BR formal §6 authoritative hơn TPL inline).

---

## Quy ước

- **Priority**: 🔴 P0 · 🟡 P1 · 🟢 P2
- **TraceID**: `FR-IX / Export.{format}` hoặc `BR-DATA-06`

---

## A. XLSX

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BC-EXP-001 | FR-IX / Export.XLSX + AC#2 | Xuất XLSX với header TT17/2025 | cb_nv_tw_01 login. Đã chạy BC HD. | format=XLSX | 1. Click [Xuất Excel (.xlsx)]. | (1) POST `/bao-cao/.../export?format=xlsx` 200. (2) File `bao-cao-{loai}-{YYYYMMDD-HHmmss}.xlsx` tải về. (3) Mở file: header có `tieu_de_bc`, `ky_bao_cao`, `tu_ngay - den_ngay`, `don_vi_ten`, `ngay_tao_bc`, `nguoi_tao` (TT17/2025). Body bảng dữ liệu. | Happy 🔴 |
| TC-BC-EXP-002 | FR-IX / Export.XLSX | XLSX có sticky header data table | cb_nv_tw_01 login. ≥30 dòng data. | format=XLSX | 1. Xuất XLSX. 2. Mở file. | (3) Row đầu tiên data table = header in đậm + freeze pane (sticky). | Happy 🟡 |
| TC-BC-EXP-003 | FR-IX / Export.XLSX | Tên file chứa loại BC + timestamp | cb_nv_tw_01 login. | — | 1. Xuất 2 BC khác nhau. | (3) Mỗi file tên unique, format `bao-cao-{slug-loai}-{timestamp}.xlsx`. | Happy 🟢 |
| TC-BC-EXP-004 | BR-DATA-06 / Codex F-01 | Boundary cap rows = 10,000 (per BR formal §6) | cb_nv_tw_01 login. (Manual seed 10,000 record nguồn — SPEC-CLARIFY-BC-07) | data=10,000 rows | 1. Chạy BC. 2. Xuất XLSX. | (3) File chứa đúng 10,000 rows. KHÔNG warning. | Edge 🔴 |
| TC-BC-EXP-005 | BR-DATA-06 / WRN-RPT-01 / Codex F-01 | Vượt cap 10K → cảnh báo + cắt | cb_nv_tw_01 login. data=10,001 rows. | data=10,001 | 1. Chạy BC. 2. Xuất XLSX. | (3) Toast WRN-RPT-01: **"Dữ liệu vượt 10.000 dòng. Hệ thống xuất 10.000 dòng đầu tiên"** (per BR formal §6 line 1274; TPL inline line 112 ghi 50K mâu thuẫn — verify thực tế FE follow BR formal hay TPL). File chỉ có 10,000 rows. | Edge 🔴 |
| TC-BC-EXP-006 | BR-DATA-06 / SPEC-CLARIFY-BC-01 verify path | Verify thực tế FE follow BR formal (10K) hay TPL inline (50K) | cb_nv_tw_01 login. data=10,001 rows. | — | 1. Chạy BC + xuất XLSX. | (3) **SPEC-CLARIFY-BC-01 verify path**: Nếu cap=10K (BR formal) → file chỉ 10K + WRN-RPT-01. Nếu cap=50K (TPL inline) → file đủ 10,001 rows + KHÔNG WRN. Log finding vào gap-report — cần BA chốt update TPL hoặc nâng BR. | Edge 🔴 |

---

## B. PDF

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BC-EXP-010 | FR-IX / Export.PDF + AC#3 | Xuất PDF format TT17/2025 | cb_nv_tw_01 login. Đã chạy BC. | format=PDF | 1. Click [Xuất PDF (.pdf)]. | (1) POST `/bao-cao/.../export?format=pdf` 200. (2) File `bao-cao-{loai}-{timestamp}.pdf` tải về. (3) Mở file: khổ A4 portrait. Font Times New Roman cỡ 13. Header BC + bảng + biểu đồ embed. | Happy 🔴 |
| TC-BC-EXP-011 | FR-IX / Export.PDF / SPEC-CLARIFY-BC-04 | Verify font Times New Roman trong PDF | cb_nv_tw_01 login. | format=PDF | 1. Xuất PDF. 2. Open PDF reader → File Info / Properties / Embedded fonts. | (3) Embedded fonts list có "Times New Roman" hoặc fallback (vd. "Liberation Serif"). Mark **SPEC-CLARIFY-BC-04** nếu fallback Arial/Calibri. | Edge 🟡 |
| TC-BC-EXP-012 | FR-IX / Export.PDF | PDF embed biểu đồ | cb_nv_tw_01 login. BC có biểu đồ Donut. | format=PDF | 1. Xuất PDF. 2. Verify trang biểu đồ. | (3) PDF có trang/section render biểu đồ Donut (vector hoặc raster image). | Happy 🟡 |
| TC-BC-EXP-013 | FR-IX / Export.PDF cap / Codex F-02 | PDF cap rows = 10K (per BR formal §6 line 1274 áp dụng "mọi danh sách có tính năng xuất") | cb_nv_tw_01 login. data=10,001 rows. | format=PDF | 1. Xuất PDF. | (3) Toast WRN-RPT-01. PDF chỉ chứa 10,000 rows đầu. Header/footer TT17/2025 vẫn đúng (A4, Times New Roman 13). KHÔNG vỡ format. | Edge 🟡 |

---

## C. Negative + Edge

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BC-EXP-020 | E8 ERR-RPT-06 | Format không hợp lệ | cb_nv_tw_01 login. | format=DOCX (manual API) | 1. DevTools modify request `format=DOCX`. POST. | (1) 400. (3) Toast "Định dạng xuất chỉ hỗ trợ XLSX hoặc PDF" (ERR-RPT-06). | Negative 🟡 |
| TC-BC-EXP-021 | E6 ERR-RPT-04 | Lỗi tạo file (BE inject) | cb_nv_tw_01 login. | format=XLSX | 1. (BE inject lỗi tạo XLSX). 2. Click Xuất. | (2) Toast "Không thể tạo file xuất. Vui lòng thử lại" (ERR-RPT-04). | Negative 🟢 (manual) |
| TC-BC-EXP-022 | TPL.Output#5 | Header file có ngay_tao_bc + nguoi_tao | cb_nv_tw_01 login. | format=XLSX | 1. Xuất XLSX. 2. Mở file. | (3) Header có `Ngày tạo BC: {DD/MM/YYYY HH:mm}` + `Người tạo: cb_nv_tw_01 - {ho_ten}`. | Happy 🟡 |
| TC-BC-EXP-023 | SCR-IX-01 row#14 | Toast progress khi xuất | cb_nv_tw_01 login. data lớn ~30K rows. | format=XLSX | 1. Click Xuất XLSX. (Quan sát trong khi tạo file). | (3) Toast "Đang tạo file..." → khi xong "Xuất thành công" + auto-download trigger. | Happy 🟢 |

---

## D. EDGE bổ sung (A4 inline merge 2026-05-10)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BC-EXP-024 | FR-IX / Export / A4 E5 | Concurrent xuất 2 tab cùng BC | cb_nv_tw_01 login. Mở 2 tab cùng SCR. | format=XLSX | 1. Tab1: chạy BC + Xuất XLSX. 2. Tab2 (cách 2s): chạy BC + Xuất XLSX. | (3) 2 file unique tên timestamp khác nhau (ms precision). Cả 2 tải về thành công. KHÔNG lock/race condition. | Edge 🟡 |
| TC-BC-EXP-025 | FR-IX / Export / A4 E6 | Tên BC chứa ký tự đặc biệt → filename slug | cb_nv_tw_01 login. | BC HD (tên có "/") | 1. Xuất XLSX BC HD. | (3) Filename không chứa "/" (sanitize → "bao-cao-hoi-dap-vuong-mac" hoặc "bao-cao-so-luong-hoi-dap"). KHÔNG có đường dẫn lừa. | Edge 🟢 |
| TC-BC-EXP-026 | FR-IX / Export / A4 E12 | Locale number format VN trong export | cb_nv_tw_01 login. data có money 1000000 VND. | format=XLSX | 1. Xuất XLSX BC chi phí. 2. Mở file. | (3) Cell money format "1.000.000 ₫" hoặc "1,000,000 VND" — locale VN consistent. KHÔNG mix "1,000,000.50" (US locale). | Edge 🟢 |
| TC-BC-EXP-027 | TPL.Output#5 ngay_tao_bc / A4 E14 | Timezone UTC+7 trong header file | cb_nv_tw_01 login. Hiện tại 14:30 UTC+7 (07:30 UTC). | format=XLSX | 1. Xuất XLSX. 2. Mở file. | (3) Header `Ngày tạo BC: 14:30 {DD/MM/YYYY}` (UTC+7 VN time, KHÔNG 07:30 UTC). | Edge 🟡 |

---

## Tổng kết file 04-TC

- **19 TC**: 6 A XLSX + 4 B PDF + 5 C Negative/Edge + 4 D Edge bổ sung A4.
- **Critical TC (🔴)**: EXP-001, 010.
- **SPEC-CLARIFY ref**: BC-01 (EXP-006), BC-04 (EXP-011 font), BC-07 (EXP-004 manual seed 50K env), BC-08 (EXP-013 PDF cap).
- **Manual injection**: EXP-021 (BE inject lỗi).
- **A4 inline merged 2026-05-10**: TC-BC-EXP-024..027 (was A4 proposal E5, E6, E12, E14).

*Generated 2026-05-10 — Phase A step A3 (BMAD generate-e2e-tests)*
