# Kế Hoạch Kiểm Thử — Báo cáo Thống kê (FR-11, SCR-IX-01, UC124–UC146)

> **Phiên bản**: 1.0
> **Ngày tạo**: 2026-05-10
> **Nguồn dữ liệu**: SRS v3.5 ([srs-fr-11-bao-cao-v3.1.md](../../../input/srs-v3/srs-fr-11-bao-cao-v3.1.md)) + master `srs-v3.md` Phụ lục B (BR formal).
> **SRS Reference**: Nhóm IX — 23 FR (FR-IX-01..FR-IX-23) trên **1 màn hình thống nhất SCR-IX-01**, kế thừa **TPL-REPORT-FULL** (input/processing/output/error chung).
>
> **Strategy** (per todo.md W5.2): **1 đại diện + smoke** — không viết 23 file UC riêng. Thay bằng:
> - 1 file `01-TC-tpl-report-full-representative.md` cover toàn bộ template (input chung, processing, output, error E1-E9, AC chung, export XLSX/PDF) — chọn FR-IX-01 BC Hỏi đáp làm representative.
> - 1 file `02-TC-smoke-23-loai-bc.md` smoke 23 loại BC × 1-2 TC/loại để verify dropdown + filter đặc thù render + data load đúng dimension.
> - 1 file `03-TC-permission-2tier-bc.md` permission matrix TW/BN/ĐP (BR-AUTH-08).
> - 1 file `04-TC-export-xlsx-pdf-tt17.md` export đặc thù (50K/10K cap row, TT17/2025 format, header A4 Times New Roman 13).
> - 1 file `05-TC-bieu-do-charts.md` biểu đồ Line/Bar/Stacked/Donut/Radar + toggle hiện-ẩn.

---

## 1. Phạm Vi Kiểm Thử

### 1.1 Chức năng được kiểm thử

- **23 FR** (UC124–UC146) trên **1 màn hình** SCR-IX-01 (Unified Report Page).
- **Entity owned**: BAO_CAO (metadata 23 loại BC). 9 entity referenced (HOI_DAP, VU_VIEC, TU_VAN_VIEN, DOANH_NGHIEP, KHOA_HOC, HO_SO_CHI_TRA, TAI_KHOAN, DON_VI, KE_HOACH_DANH_GIA, CHUONG_TRINH_HTPL).
- **State**: BAO_CAO trạng thái đơn giản DANG_TAO → HOAN_THANH | LOI (không SM diagram per srs-fr-11:1233).
- **Đặc thù**:
  - Chỉ truy vấn bản ghi đã duyệt (BR-RPT-01) — TC seed phải có data ở các module nguồn ở trạng thái duyệt cuối (HOAN_THANH/DA_THANH_TOAN/v.v.).
  - Phân quyền 2-tier (BR-AUTH-08): TW = toàn quốc, BN = chỉ BN, ĐP = chỉ ĐP.
  - Export XLSX + PDF format theo TT17/2025 (A4, Times New Roman 13).
  - Cap 50K rows/file (TPL-REPORT-FULL Bước 9) **vs** BR-DATA-06 master "10K rows" → **SPEC-CLARIFY-BC-01** (mâu thuẫn template-IX vs BR formal).
  - Timeout 30s (E5).
  - Khoảng thời gian ≤ 366 ngày (trừ kỳ NAM) (E2).

### 1.2 Danh sách FR / UC mapping

| Nhóm SRS | UC | Tên BC | Filter đặc thù | Biểu đồ | Smoke ID |
|----------|----|--------|----------------|---------|----------|
| **Hỏi đáp** | UC124 | FR-IX-01 BC Số lượng hỏi đáp | linh_vuc, trang_thai_hd | Donut + Trend | TC-BC-SM-01 |
| **Vụ việc** | UC125 | FR-IX-02 VV đã tiếp nhận | kenh_tiep_nhan, linh_vuc | Bar + Trend | TC-BC-SM-02 |
| | UC126 | FR-IX-03 VV đang hỗ trợ (snapshot) | nht_id, muc_sla | Bar (snapshot) | TC-BC-SM-03 |
| | UC127 | FR-IX-04 VV đã hoàn thành | linh_vuc, ket_qua | Bar + Donut | TC-BC-SM-04 |
| | UC128 | FR-IX-05 VV theo thời gian | — | Line trend | TC-BC-SM-05 |
| **Đào tạo** | UC129 | FR-IX-06 KH đang diễn ra | hinh_thuc, linh_vuc | Bar (snapshot) | TC-BC-SM-06 |
| | UC130 | FR-IX-07 KH đã diễn ra | hinh_thuc | Bar + Trend | TC-BC-SM-07 |
| **CG/TVV** | UC131 | FR-IX-08 Số lượng CG/TVV | loai_tvv, linh_vuc, don_vi | Donut + Bar | TC-BC-SM-08 |
| **Đánh giá** | UC132 | FR-IX-09 Hiệu quả HTPL | ke_hoach_dg_id | Bar + Radar | TC-BC-SM-09 |
| | UC133 | FR-IX-10 Chất lượng đào tạo | khoa_hoc_id | Bar + Line | TC-BC-SM-10 |
| **VV cross-tab** | UC134 | FR-IX-11 VV theo đơn vị | — | Stacked bar | TC-BC-SM-11 |
| | UC135 | FR-IX-12 VV theo lĩnh vực | — | Grouped bar | TC-BC-SM-12 |
| | UC136 | FR-IX-13 VV theo loại DN | loai_dn | Grouped bar | TC-BC-SM-13 |
| | UC137 | FR-IX-14 VV theo thời gian chi tiết | — | Stacked bar trend | TC-BC-SM-14 |
| **Chi phí** | UC138 | FR-IX-15 Chi phí chi trả | — | Bar + Summary | TC-BC-SM-15 |
| | UC139 | FR-IX-16 Chi phí theo đơn vị | — | Bar cross-tab | TC-BC-SM-16 |
| | UC140 | FR-IX-17 Chi phí theo lĩnh vực | linh_vuc | Bar | TC-BC-SM-17 |
| | UC141 | FR-IX-18 Chi phí theo loại DN | loai_dn | Grouped bar | TC-BC-SM-18 |
| | UC142 | FR-IX-19 Chi phí theo thời gian | — | Line trend | TC-BC-SM-19 |
| **CT HTPLDN** | UC143 | FR-IX-20 Số lượng CT | trang_thai_ct | Bar + Trend | TC-BC-SM-20 |
| | UC144 | FR-IX-21 CT theo đơn vị | — | Bar cross-tab | TC-BC-SM-21 |
| | UC145 | FR-IX-22 CT theo lĩnh vực | linh_vuc | Bar | TC-BC-SM-22 |
| | UC146 | FR-IX-23 CT theo thời gian | — | Line trend | TC-BC-SM-23 |

### 1.3 Tài khoản & role liên quan

| Role | Cấp | Username (users.csv) | Dùng cho TC loại |
|------|-----|----------------------|------------------|
| QTHT | — | qtht_01 | Verify quyền BC (BR-AUTH-08 ngoại lệ — bypass scope) |
| CB_NV_TW | TW | cb_nv_tw_01 | Representative + smoke (scope toàn quốc). `_02` fallback, `_03` permission |
| CB_NV_BN | BN | cb_nv_bn_01 (Bộ KH&ĐT) | Permission scoped BN |
| CB_NV_DP | DP | cb_nv_dp_01 (Sở TP AG) | Permission scoped ĐP |
| CB_PD_TW | TW | cb_pd_tw_01 | Verify CB_PD cũng có quyền xem BC (theo SRS Tác nhân chính) |
| CB_PD_BN | BN | cb_pd_bn_01 | Permission scoped BN cho CB_PD |
| CB_PD_DP | DP | cb_pd_dp_01 | Permission scoped ĐP cho CB_PD |
| NHT/TVV/CG/DN/GV | — | nht_01, tvv_01, cg_01, dn_01, gv_01 | Negative — verify 403 chặn module BC (ERR-RPT-05) |

---

## 2. Quy Tắc Nghiệp Vụ Trích Xuất Từ SRS

### 2.1 Business Rules (BR)

> **Footnote convention**:
> - **BR formal §6 srs-fr-11**: 5 BR declared trong srs-fr-11:1242-1280 — BR-AUTH-01, BR-AUTH-08, BR-DATA-05, BR-DATA-06, BR-SLA-02.
> - **BR working labels (srs-v3.md inline)**: thừa kế khi ref (vd BR-RPT-01 cho rule "chỉ bản ghi đã duyệt" trong template Bước 4).
> - **BR inline label (BR-RPT-*)**: working label cho inline rules trong template TPL-REPORT-FULL processing/output. KHÔNG phải BR formal — dùng cho traceability nội bộ.

| Mã | Quy tắc | Nguồn SRS | Áp dụng? | TC áp dụng |
|----|---------|-----------|----------|-----------|
| BR-AUTH-01 | Mọi user phải xác thực trước truy cập | srs-fr-11:1252-1257 | ✅ | Pre-condition login mọi UC |
| BR-AUTH-08 | Phân quyền 2-tier theo don_vi_id (TW/BN/ĐP) | srs-fr-11:1258-1262 | ✅ | TC-BC-PERM-* (file 03) |
| BR-DATA-05 | Audit trail — log mọi xem/xuất BC | srs-fr-11:1264-1268 | ✅ | TC verify AUDIT_LOG (file 01) |
| BR-DATA-06 | Export Excel max 10,000 rows/file | srs-fr-11:1270-1274 | ⚠️ SPEC-CLARIFY-BC-01 (mâu thuẫn 50K vs 10K — template TPL-REPORT-FULL Bước 9 nói 50K) | TC export boundary (file 04) |
| BR-SLA-02 | 4 mức cảnh báo SLA: Bình thường (>50%), Sắp hết hạn (<50%, vàng), Quá hạn (>100%, đỏ), QHNT (>2x, đen) | srs-fr-11:1276-1280 | ✅ | TC-BC-SM-03 (BC VV đang hỗ trợ) |
| BR-RPT-01 | Chỉ truy vấn bản ghi đã duyệt (đã duyệt / hoàn thành / đã thanh toán) | srs-fr-11:80 (template Bước 4) | ✅ | Mọi TC seed yêu cầu data đã duyệt cuối |
| BR-RPT-02 | Khoảng thời gian ≤ 366 ngày (trừ kỳ NAM) | srs-fr-11:78 (template Bước 2) | ✅ | TC-BC-NEG-E2 |

### 2.2 Error Codes (TPL-REPORT-FULL — chung 23 BC)

| Mã | Điều kiện | Severity | TC áp dụng |
|----|-----------|----------|-----------|
| ERR-RPT-01 | tu_ngay > den_ngay | ERROR | TC-BC-NEG-E1 |
| ERR-RPT-02 | Khoảng thời gian > 366 ngày (trừ NAM) | ERROR | TC-BC-NEG-E2 |
| INF-RPT-01 | Không có dữ liệu | INFO | TC-BC-NEG-E3 (empty state) |
| WRN-RPT-01 | Export vượt cap rows | WARNING | TC-BC-EDGE-EXPORT-CAP (file 04) |
| ERR-RPT-03 | Timeout truy vấn > 30s | ERROR | TC-BC-NEG-E5 |
| ERR-RPT-04 | Lỗi xuất file | ERROR | TC-BC-NEG-E6 |
| ERR-RPT-05 | Không có quyền | ERROR | TC-BC-PERM-NEG-* (file 03) |
| ERR-RPT-06 | Format xuất không hợp lệ | ERROR | TC-BC-NEG-E8 |
| ERR-RPT-07 | Template báo cáo bị hỏng | ERROR | TC-BC-NEG-E9 (manual injection — mark SPEC-CLARIFY-BC-02 reproducibility) |
| ERR-RPT-IX01-01 | Lĩnh vực không tồn tại (FR-IX-01) | ERROR | TC-BC-REP-028 (Codex F-06: mapping đúng — TC-BC-SM-01 chỉ smoke render, không có negative path) |

### 2.3 Permission Matrix (BR-AUTH-08, 2-tier)

| Action / BC nhóm | QTHT | CB_NV_TW | CB_NV_BN | CB_NV_DP | CB_PD_TW | CB_PD_BN | CB_PD_DP | NHT/TVV/CG/DN/GV |
|------------------|------|----------|----------|----------|----------|----------|----------|------------------|
| Xem 23 loại BC (UC124-UC146) | 👁️* | ✅ toàn quốc | ✅ BN mình | ✅ ĐP mình | ✅ toàn quốc | ✅ BN mình | ✅ ĐP mình | ❌ 403 |
| Xuất XLSX/PDF | 👁️* | ✅ | ✅ scope | ✅ scope | ✅ | ✅ scope | ✅ scope | ❌ |
| Filter đơn vị (cross-scope) | 👁️* | ✅ chọn BN/ĐP bất kỳ | ❌ locked BN mình | ❌ locked ĐP mình | ✅ chọn BN/ĐP bất kỳ | ❌ locked | ❌ locked | ❌ |

> *QTHT theo srs-fr-11:1262 ngoại lệ "QTHT bypass" — verify hành vi bypass scope hay 403. Mark **SPEC-CLARIFY-BC-03** nếu mâu thuẫn UI/BR.

### 2.4 State Machine

> Không có SM diagram. BAO_CAO entity dùng 3 trạng thái đơn giản (DANG_TAO → HOAN_THANH | LOI). Xem `01-TC-tpl-report-full-representative.md` Section H verify state transitions qua DB → mark mọi case verify trang_thai dùng UI bridge (badge trên màn hình lịch sử BC nếu có, hoặc audit log entry).

---

## 3. Cấu Trúc File Test Case

```
bao-cao-tk/
├── 00-test-plan-overview.md                      ← Plan này
├── 01-TC-tpl-report-full-representative.md       ← Representative FR-IX-01 cover template chung (input + process + output + error E1-E9 + AC + export + audit) (~25 TC)
├── 02-TC-smoke-23-loai-bc.md                     ← Smoke 23 BC × 1-2 TC = 23 + 8 cross-cut (~30 TC)
├── 03-TC-permission-2tier-bc.md                  ← Permission matrix BR-AUTH-08 (~12 TC)
├── 04-TC-export-xlsx-pdf-tt17.md                 ← Export đặc thù TT17/2025 + cap rows (~10 TC)
├── 05-TC-bieu-do-charts.md                       ← Biểu đồ chart types + toggle (~8 TC)
├── 08-REVIEW-edge-case-hunter.md                 ← A4 audit log
├── 09-traceability-matrix.md                     ← A5 BR/AC ↔ TC matrix
├── 10-REVIEW-test-quality.md                     ← A6 quality score
├── 11-a7-filter-log.md                           ← A7 UI/function-testable filter log
└── 12-codex-review-log.md                        ← Codex review apply log
```

**Estimate Phase A:** ~80 TC (theo todo.md), thực tế dự kiến A3 base ~60 + A4 +10 edge + A6 +5 fill + Codex +5 = **~80 TC**.

---

## 4. SPEC-CLARIFY pending BA

| ID | Mâu thuẫn / câu hỏi | SRS lines | Default behavior trong TC | Trạng thái |
|----|---------------------|-----------|---------------------------|------------|
| SPEC-CLARIFY-BC-01 | BR-DATA-06 cap "10,000 rows" (formal §6) vs TPL-REPORT-FULL Bước 9 cap "50,000 rows" (inline) | srs-fr-11:85 + 112 vs 1274 | **RE-OPEN per Codex F-01 2026-05-10**: TC default về 10K (BR formal authoritative). Cần BA xác nhận update TPL về 10K hoặc nâng BR. Memory feedback "UI vs business" KHÔNG áp dụng đây (đây là TPL inline vs BR formal, không phải UI vs business). | Pending |
| SPEC-CLARIFY-BC-02 | E9 ERR-RPT-07 "Template báo cáo bị hỏng" — không có cách reproduce qua UI | srs-fr-11:117 | TC mark `MANUAL-INJECTION` — verify UI render error message khi BE trả mã ERR-RPT-07 | Pending |
| SPEC-CLARIFY-BC-03 | QTHT bypass BR-AUTH-08 — chưa rõ BC có thực sự cho phép QTHT xem hay 403 | srs-fr-11:1262 | TC verify hành vi thực, log discrepancy nếu có | Pending |
| SPEC-CLARIFY-BC-04 | Format PDF "Times New Roman cỡ 13" — không rõ font fallback nếu hệ thống chưa cài font | srs-fr-11:84 | TC verify file PDF khi mở có font đúng; nếu fallback Arial/Calibri → log SPEC | Pending |
| SPEC-CLARIFY-BC-05 | "API outbound không yêu cầu session" (BR-AUTH-01 ngoại lệ) — không rõ BC có endpoint outbound nào không | srs-fr-11:1256 | TC bỏ qua, không có UI | Pending |
| SPEC-CLARIFY-BC-11 | BR-SLA-02 mâu thuẫn ngưỡng % giữa FR-IX-03 line 249 (`<50%` = bình thường, `50-100%` = sắp hết hạn) vs BR-SLA-02 line 1280 (`>50%` = bình thường, `<50%` = sắp hết hạn) | srs-fr-11:249 vs 1280 | TC-BC-SM-03 verify thực tế FE follow chiều nào, log finding | Pending (Codex F-04) |

---

## 5. Risk + Note

- **Data dependency**: BC phụ thuộc 9 module nguồn có data đã duyệt. TC representative + smoke phải có precondition rõ ràng "Module nguồn X có ≥N record DA_DUYET trong kỳ Y". Phase B sẽ block 🚫 cho đến khi 9 module có data DA_DUYET (per todo.md W5.2 B note).
- **Nhật ký xem/xuất BC** (BR-DATA-05): verify qua UI Nhật ký HT (FR-VIII-28) — KHÔNG verify trực tiếp DB row.
- **Snapshot vs trend**: BC snapshot (UC126, UC129, UC131) tính tại thời điểm query — TC verify thời gian phải lock data trước khi run.
- **Cross-tab BC** (UC134-UC137, UC139, UC144): verify cấu trúc bảng (hàng/cột) khớp dimensions.

---

*Generated 2026-05-10 — Phase A step A2 (BMAD test-design)*
